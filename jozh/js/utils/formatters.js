// Sayı, para, boyut biçimlendirme ve Türkçe karakterlere duyarsız arama.

const numberFormatters = new Map();

function getNumberFormatter(min, max) {
  const key = `${min}:${max}`;
  if (!numberFormatters.has(key)) {
    numberFormatters.set(key, new Intl.NumberFormat('tr-TR', { minimumFractionDigits: min, maximumFractionDigits: max }));
  }
  return numberFormatters.get(key);
}

export function formatNumber(value, maxDecimals = 2, minDecimals = 0) {
  if (value === null || value === undefined || Number.isNaN(Number(value))) return '';
  return getNumberFormatter(minDecimals, maxDecimals).format(Number(value));
}

export function formatMoney(value) {
  if (value === null || value === undefined || Number.isNaN(Number(value))) return '';
  const n = Number(value);
  const hasFraction = Math.round(n * 100) % 100 !== 0;
  return `${formatNumber(n, 2, hasFraction ? 2 : 0)} ₺`;
}

// Türkçe sayı okuma: "1.500" = 1500, "2.750,50" = 2750.5, "72,5" = 72.5.
// Geçersizse NaN, boşsa null döner.
export function parseTrNumber(input) {
  if (input === null || input === undefined) return null;
  if (typeof input === 'number') return Number.isFinite(input) ? input : NaN;
  let s = String(input).trim().replace(/\s|₺|TL/gi, '');
  if (s === '') return null;
  let negative = false;
  if (s.startsWith('-')) {
    negative = true;
    s = s.slice(1);
  }
  if (s.includes(',')) {
    if (!/^\d{1,3}(\.\d{3})*(,\d+)?$|^\d+(,\d+)?$/.test(s)) return NaN;
    s = s.replace(/\./g, '').replace(',', '.');
  } else if (s.includes('.')) {
    if (/^\d{1,3}(\.\d{3})+$/.test(s)) s = s.replace(/\./g, '');
    else if (!/^\d+\.\d+$/.test(s)) return NaN;
  } else if (!/^\d+$/.test(s)) {
    return NaN;
  }
  const n = Number(s);
  if (!Number.isFinite(n)) return NaN;
  return negative ? -n : n;
}

// Form alanına yazılacak hâl: 72.5 → "72,5"
export function numberToInput(value) {
  if (value === null || value === undefined || value === '') return '';
  return String(value).replace('.', ',');
}

export function formatBytes(bytes) {
  if (!Number.isFinite(bytes) || bytes < 0) return '';
  if (bytes < 1024) return `${bytes} B`;
  const units = ['KB', 'MB', 'GB', 'TB'];
  let v = bytes / 1024;
  let i = 0;
  while (v >= 1024 && i < units.length - 1) {
    v /= 1024;
    i += 1;
  }
  return `${formatNumber(v, v < 10 ? 1 : 0)} ${units[i]}`;
}

export function truncate(text, max) {
  const s = String(text || '');
  return s.length > max ? `${s.slice(0, max - 1).trimEnd()}…` : s;
}

const TR_MAP = { ç: 'c', ğ: 'g', ı: 'i', i̇: 'i', ö: 'o', ş: 's', ü: 'u', â: 'a', î: 'i', û: 'u' };

export function normalizeSearch(text) {
  return String(text || '')
    .toLocaleLowerCase('tr-TR')
    .replace(/[çğıöşüâîû]/g, (ch) => TR_MAP[ch] || ch)
    .normalize('NFD')
    .replace(/[̀-ͯ]/g, '')
    .replace(/\s+/g, ' ')
    .trim();
}

export function matchesSearch(query, ...fields) {
  const q = normalizeSearch(query);
  if (!q) return true;
  const hay = normalizeSearch(fields.flat().filter((f) => f !== null && f !== undefined).join(' '));
  return q.split(' ').every((part) => hay.includes(part));
}

export function initials(first, last) {
  const a = String(first || '').trim().charAt(0);
  const b = String(last || '').trim().charAt(0);
  return `${a}${b}`.toLocaleUpperCase('tr-TR') || '?';
}
