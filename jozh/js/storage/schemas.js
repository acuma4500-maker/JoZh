// Alan doğrulaması. Her yazmada şema uygulanır: bilinmeyen alanlar atılır, türler çevrilir,
// hatada err.fields = { alan: mesaj } ile ValidationError fırlatılır.
// Sınırlar firestore.rules ile birebir aynıdır.
import { isValidISODate, isValidTime } from '../utils/dates.js';
import { parseTrNumber } from '../utils/formatters.js';
import { isImageId, shortId } from '../utils/id-generator.js';
import { parseTags } from '../utils/tags.js';
import { BLOOD_TYPES } from '../utils/labels.js';

export class ValidationError extends Error {
  constructor(fields) {
    super('Doğrulama hatası');
    this.name = 'ValidationError';
    this.type = 'validation';
    this.fields = fields;
  }
}

export const BASE_FIELDS = ['id', 'createdAt', 'updatedAt', 'version', 'deleted', 'syncedRev'];

// Alan tanımı yardımcıları
const str = (max, opts = {}) => ({ kind: 'string', max, ...opts });
const date = (opts = {}) => ({ kind: 'date', ...opts });
const time = () => ({ kind: 'time' });
const num = (min, max, opts = {}) => ({ kind: 'number', min, max, ...opts });
const int = (min, max, opts = {}) => ({ kind: 'number', min, max, integer: true, ...opts });
const bool = () => ({ kind: 'bool' });
const oneOf = (values, def) => ({ kind: 'enum', values, def });
const tags = () => ({ kind: 'tags' });
const photo = () => ({ kind: 'photo' });
const photos = (max) => ({ kind: 'photos', max });
const list = (item, max) => ({ kind: 'list', item, max });
const obj = (fields, opts = {}) => ({ kind: 'object', fields, ...opts });

const textItem = obj({ id: str(16), text: str(200, { required: true }) });
const checkItem = obj({ id: str(16), text: str(200, { required: true }), done: bool() });

export const SCHEMAS = {
  profile: {
    firstName: str(60),
    lastName: str(60),
    birthDate: date(),
    bloodType: oneOf(['', ...BLOOD_TYPES], ''),
    height: int(50, 250, { label: 'cm' }),
    weight: num(20, 400, { decimals: 1 }),
    phone: str(30, { pattern: /^[0-9+()\s-]*$/, patternMessage: 'Yalnızca rakam, boşluk, +, ( ) ve - kullan.' }),
    about: str(2000, { multiline: true }),
    photoId: photo()
  },
  notes: {
    title: str(200),
    body: str(20000, { multiline: true }),
    tags: tags(),
    pinned: bool()
  },
  diary: {
    title: str(200, { required: true }),
    date: date({ required: true }),
    body: str(100000, { multiline: true }),
    tags: tags(),
    photoIds: photos(20)
  },
  dreams: {
    title: str(200, { required: true }),
    description: str(2000, { multiline: true }),
    category: str(60),
    targetDate: date(),
    priority: oneOf(['low', 'medium', 'high'], 'medium'),
    progress: int(0, 100, { def: 0 }),
    status: oneOf(['notStarted', 'inProgress', 'completed', 'postponed'], 'notStarted'),
    notes: str(5000, { multiline: true }),
    photoId: photo()
  },
  plans: {
    name: str(200, { required: true }),
    type: oneOf(['trip', 'date', 'work', 'personal', 'special', 'other'], 'personal'),
    status: oneOf(['planned', 'completed', 'cancelled'], 'planned'),
    startDate: date({ required: true }),
    startTime: time(),
    endDate: date(),
    endTime: time(),
    location: str(200),
    description: str(5000, { multiline: true }),
    budget: num(0, 100000000, { decimals: 2 }),
    spent: num(0, 100000000, { decimals: 2 }),
    checklist: list(checkItem, 200),
    notes: str(5000, { multiline: true }),
    trip: obj({
      city: str(100),
      places: list(checkItem, 100),
      accommodation: str(500, { multiline: true }),
      transport: str(500, { multiline: true }),
      expenses: list(obj({
        id: str(16),
        name: str(100, { required: true }),
        estimated: num(0, 100000000, { decimals: 2 }),
        actual: num(0, 100000000, { decimals: 2 })
      }), 100)
    }, { nullable: true })
  },
  memories: {
    title: str(200, { required: true }),
    date: date(),
    description: str(5000, { multiline: true }),
    tags: tags(),
    photoIds: photos(10)
  },
  partner: {
    name: str(100),
    nickname: str(100),
    birthDate: date(),
    togetherSince: date(),
    summary: str(1000, { multiline: true }),
    photoId: photo(),
    traits: list(textItem, 100),
    likes: list(textItem, 100),
    dislikes: list(textItem, 100),
    foods: list(textItem, 100),
    colors: list(textItem, 100),
    perfumes: list(textItem, 100),
    hobbies: list(textItem, 100),
    importantDates: list(obj({ id: str(16), title: str(200, { required: true }), date: date({ required: true }), yearly: bool() }), 100),
    todos: list(checkItem, 200),
    surprises: list(checkItem, 200),
    privateNotes: str(10000, { multiline: true })
  },
  settings: {
    calendarView: oneOf(['month', 'agenda'], 'month')
  },
  savings: {
    title: str(100, { required: true }),
    targetAmount: num(0.01, 100000000, { decimals: 2, required: true }),
    targetDate: date(),
    note: str(500),
    contributions: list(obj({
      id: str(16),
      date: date({ required: true }),
      amount: num(-100000000, 100000000, { decimals: 2, required: true }),
      note: str(200),
      txnId: str(60)
    }), 500)
  },
  transactions: {
    type: oneOf(['income', 'expense'], 'expense'),
    amount: num(0.01, 100000000, { decimals: 2, required: true }),
    category: str(60, { required: true }),
    date: date({ required: true }),
    account: oneOf(['cash', 'bank', 'card'], 'cash'),
    note: str(500)
  }
};

export const SYNCED_STORES = ['profile', 'settings', 'partner', 'memories', 'notes', 'diary', 'dreams', 'plans', 'transactions', 'savings'];
export const SINGLETON_STORES = ['profile', 'partner', 'settings'];
export const ID_PREFIX = { memories: 'mem', diary: 'diary', dreams: 'dream', plans: 'plan', notes: 'note', transactions: 'txn', savings: 'save' };

function cleanString(value, def, errors, path) {
  if (value === null || value === undefined) return '';
  if (typeof value !== 'string' && typeof value !== 'number') {
    errors[path] = 'Geçersiz değer.';
    return '';
  }
  return String(value);
}

function applyField(def, value, errors, path) {
  switch (def.kind) {
    case 'string': {
      let s = cleanString(value, def, errors, path);
      s = def.multiline ? s.replace(/\r\n/g, '\n').trimEnd() : s.replace(/\s+/g, ' ').trim();
      if (def.multiline) s = s.replace(/^\s+$/, '');
      if (def.required && !s.trim()) errors[path] = 'Bu alan zorunlu.';
      else if (s.length > def.max) errors[path] = `En çok ${def.max.toLocaleString('tr-TR')} karakter olabilir (şu an ${s.length.toLocaleString('tr-TR')}).`;
      else if (s && def.pattern && !def.pattern.test(s)) errors[path] = def.patternMessage || 'Geçersiz biçim.';
      return s;
    }
    case 'date': {
      const s = value === null || value === undefined ? '' : String(value).trim();
      if (!s) {
        if (def.required) errors[path] = 'Tarih zorunlu.';
        return '';
      }
      if (!isValidISODate(s)) errors[path] = 'Geçerli bir tarih seç.';
      return s;
    }
    case 'time': {
      const s = value === null || value === undefined ? '' : String(value).trim();
      if (s && !isValidTime(s)) errors[path] = 'Saat SS:DD biçiminde olmalı.';
      return s;
    }
    case 'number': {
      let n = value;
      if (typeof n === 'string') n = parseTrNumber(n);
      if (n === null || n === undefined || n === '') {
        if (def.required) errors[path] = 'Bu alan zorunlu.';
        return def.def ?? null;
      }
      n = Number(n);
      if (!Number.isFinite(n)) {
        errors[path] = 'Geçerli bir sayı yaz (ör. 1.500 ya da 72,5).';
        return null;
      }
      if (def.integer) {
        if (!Number.isInteger(n)) {
          errors[path] = 'Tam sayı olmalı.';
          return null;
        }
      } else if (def.decimals !== undefined) {
        n = Math.round(n * 10 ** def.decimals) / 10 ** def.decimals;
      }
      if (n < def.min || n > def.max) {
        errors[path] = `${def.min.toLocaleString('tr-TR')} ile ${def.max.toLocaleString('tr-TR')} arasında olmalı.`;
      }
      return n;
    }
    case 'bool':
      return value === true || value === 'true' || value === 'on' || value === 1;
    case 'enum': {
      const s = value === null || value === undefined || value === '' ? def.def : String(value);
      if (!def.values.includes(s)) {
        errors[path] = 'Listeden bir seçenek seç.';
        return def.def;
      }
      return s;
    }
    case 'tags': {
      const arr = parseTags(value || []);
      if (arr.length > 20) errors[path] = 'En çok 20 etiket olabilir.';
      return arr.slice(0, 20);
    }
    case 'photo': {
      if (!value) return null;
      if (!isImageId(value)) {
        errors[path] = 'Geçersiz fotoğraf.';
        return null;
      }
      return value;
    }
    case 'photos': {
      const arr = Array.isArray(value) ? value.filter(Boolean) : [];
      const unique = [...new Set(arr)];
      if (unique.some((id) => !isImageId(id))) errors[path] = 'Geçersiz fotoğraf.';
      if (unique.length > def.max) errors[path] = `En çok ${def.max} fotoğraf eklenebilir.`;
      return unique.filter(isImageId).slice(0, def.max);
    }
    case 'list': {
      // Zorunlu metni boş bırakılmış maddeler sessizce atılır.
      const requiredKeys = def.item.kind === 'object'
        ? Object.entries(def.item.fields).filter(([, d]) => d.kind === 'string' && d.required).map(([k]) => k)
        : [];
      const arr = (Array.isArray(value) ? value : []).filter((item) => !(item && typeof item === 'object'
        && requiredKeys.length && requiredKeys.every((k) => !String(item[k] ?? '').trim())));
      if (arr.length > def.max) errors[path] = `En çok ${def.max} madde olabilir.`;
      const out = [];
      arr.slice(0, def.max).forEach((item, i) => {
        const cleaned = applyField(def.item, item, errors, `${path}.${i}`);
        if (cleaned) out.push(cleaned);
      });
      return out;
    }
    case 'object': {
      if (value === null || value === undefined) return def.nullable ? null : applyObject(def.fields, {}, errors, path);
      if (typeof value !== 'object' || Array.isArray(value)) {
        errors[path] = 'Geçersiz değer.';
        return def.nullable ? null : {};
      }
      return applyObject(def.fields, value, errors, path);
    }
    default:
      return value;
  }
}

function applyObject(fields, value, errors, path) {
  const out = {};
  for (const [key, def] of Object.entries(fields)) {
    out[key] = applyField(def, value[key], errors, path ? `${path}.${key}` : key);
  }
  if ('id' in fields && !out.id) out.id = shortId();
  return out;
}

// Kayıt alanlarını şemaya göre temizler. Ortak alanlar (id, createdAt…) olduğu gibi korunur.
export function applySchema(store, data) {
  const schema = SCHEMAS[store];
  if (!schema) throw new Error(`Bilinmeyen depo: ${store}`);
  const errors = {};
  const out = applyObject(schema, data || {}, errors, '');
  for (const f of BASE_FIELDS) {
    if (data && data[f] !== undefined) out[f] = data[f];
  }
  crossValidate(store, out, errors);
  if (Object.keys(errors).length) throw new ValidationError(errors);
  return out;
}

// Alanlar arası kurallar
function crossValidate(store, rec, errors) {
  if (store === 'dreams') {
    if (rec.progress === 100) rec.status = 'completed';
    else if (rec.status === 'completed') rec.status = 'inProgress';
  }
  if (store === 'plans') {
    if (!rec.endDate) rec.endDate = rec.startDate;
    if (rec.startDate && rec.endDate && rec.endDate < rec.startDate) {
      errors.endDate = 'Bitiş tarihi başlangıçtan önce olamaz.';
    }
    if (rec.startDate && rec.startDate === rec.endDate && rec.startTime && rec.endTime && rec.endTime < rec.startTime) {
      errors.endTime = 'Aynı gün içinde bitiş saati başlangıçtan önce olamaz.';
    }
    if (rec.type !== 'trip') {
      rec.trip = null;
    } else {
      if (!rec.trip) rec.trip = applyObject(SCHEMAS.plans.trip.fields, {}, {}, 'trip');
      const actual = rec.trip.expenses.reduce((sum, e) => sum + (Number(e.actual) || 0), 0);
      rec.spent = Math.round(actual * 100) / 100;
      if (rec.spent > 100000000) errors.spent = 'Harcama toplamı çok büyük.';
    }
  }
  if (store === 'savings') {
    rec.contributions.forEach((c, i) => {
      if (c.amount === 0) errors[`contributions.${i}.amount`] = 'Tutar sıfır olamaz.';
    });
  }
  if (store === 'transactions' && rec.type === 'income' && rec.account === 'card') {
    errors.account = 'Gelir nakit ya da bankaya kaydedilir.';
  }
}

export function validateRecordShape(store, record) {
  // Yedekten ve buluttan gelen kayıtlar için: ortak alanlar + şema.
  if (!record || typeof record !== 'object') return false;
  if (typeof record.id !== 'string' || typeof record.createdAt !== 'string' || typeof record.updatedAt !== 'string') return false;
  try {
    applySchema(store, record);
    return true;
  } catch {
    return false;
  }
}
