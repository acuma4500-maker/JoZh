// Kışla: mıntıka (temizlik) listesi, nöbet çizelgesi, personel ve istatistik.
// Veriler cihazda (meta 'kisla:*') tutulur ve yedeğe dahildir; buluta gönderilmez.
import { initApp } from '../app.js';
import * as db from '../storage/local-db.js';
import { el, replace, button, iconButton, segmented, field, openDialog, toast, toastError, chip, confirmDialog, showFieldErrors, clearFieldErrors, loadingState, emptyState } from '../ui.js';
import { icon } from '../utils/icons.js';
import * as K from '../utils/kisla.js';
import { todayISO, addDays, formatDate, isValidISODate, isValidTime, pad2 } from '../utils/dates.js';
import { shortId } from '../utils/id-generator.js';
import { drawTable, shareCanvas, copyText } from '../components/table-image.js';

const main = document.getElementById('main');
const KEYS = {
  personnel: 'kisla:personnel',
  areas: 'kisla:areas',
  lists: 'kisla:lists',
  duties: 'kisla:duties',
  dutyNext: 'kisla:dutyNext',
  since: 'kisla:statsSince'
};
const TAB_KEY = 'jozh.kislaTab';
const TABS = [['mintika', 'Mıntıka'], ['nobet', 'Nöbet'], ['personel', 'Personel'], ['stats', 'İstatistik']];
const KEEP_DAYS = 180;

const S = {
  tab: readTab(),
  personnel: [],
  areas: [],
  lists: {},
  duties: [],
  dutyNext: 0,
  since: '',
  day: 'today'
};

const panels = Object.fromEntries(TABS.map(([k]) => [k, el('div', { class: 'ks-panel' })]));

function readTab() {
  try {
    const t = localStorage.getItem(TAB_KEY);
    return TABS.some(([k]) => k === t) ? t : 'mintika';
  } catch {
    return 'mintika';
  }
}

async function save(key, value) {
  try {
    await db.setMeta(key, value);
    return true;
  } catch (err) {
    toastError('kisla.save', err);
    return false;
  }
}

const nameOf = (id) => (S.personnel.find((p) => p.id === id) || {}).name || 'Silinmiş kişi';
const areaName = (id) => (S.areas.find((a) => a.id === id) || {}).name || '';
const selectedDate = () => (S.day === 'tomorrow' ? addDays(todayISO(), 1) : todayISO());

function avatar(name) {
  return el('span', { class: 'ks-avatar', 'aria-hidden': 'true' }, (name || '?').trim().charAt(0).toLocaleUpperCase('tr-TR'));
}

function personChip(id, { fixed = false } = {}) {
  return el('span', { class: `ks-person${fixed ? ' is-fixed' : ''}` }, avatar(nameOf(id)), el('span', null, nameOf(id)),
    fixed ? el('span', { class: 'ks-fixed-mark', title: 'Sabit görev' }, icon('pin', { size: 14 }), el('span', { class: 'visually-hidden' }, ' (sabit)')) : null);
}

function fmtDateTime(iso) {
  const d = new Date(iso);
  const date = `${d.getFullYear()}-${pad2(d.getMonth() + 1)}-${pad2(d.getDate())}`;
  return { day: formatDate(date, { short: true, year: false, weekday: true }), time: `${pad2(d.getHours())}:${pad2(d.getMinutes())}`, date };
}

function goTab(t) {
  S.tab = t;
  try {
    localStorage.setItem(TAB_KEY, t);
  } catch {
    // yok say
  }
  setup.tabs.querySelectorAll('.segment').forEach((b) => b.setAttribute('aria-checked', String(b.dataset.value === t)));
  render();
}

function needPersonnel(panel) {
  replace(panel, emptyState('Önce personeli ekle. Mıntıka ve nöbet bu listeden yapılır.', 'Personel ekle', () => goTab('personel'), 'user'));
}

// --- Mıntıka ---

function cleaningText(entry) {
  const lines = [`MINTIKA LİSTESİ – ${formatDate(entry.date, { weekday: true })}`, ''];
  for (const a of entry.areas) lines.push(`${a.name}: ${a.ids.length ? a.ids.map(nameOf).join(', ') : '—'}`);
  if (entry.spare && entry.spare.length) lines.push(`Boşta: ${entry.spare.map(nameOf).join(', ')}`);
  return lines.join('\n');
}

function cleaningImage(entry) {
  const canvas = drawTable({
    title: 'MINTIKA LİSTESİ',
    subtitle: formatDate(entry.date, { weekday: true }),
    head: ['Yer', 'Personel'],
    widths: [4, 6],
    rows: [...entry.areas.map((a) => [a.name, a.ids.length ? a.ids.map(nameOf).join(', ') : '—']), ...(entry.spare && entry.spare.length ? [['Boşta', entry.spare.map(nameOf).join(', ')]] : [])],
    footer: 'JOZH · Kışla'
  });
  shareCanvas(canvas, `mintika-${entry.date}.png`, 'Mıntıka listesi');
}

async function makeList(date, { confirmRedo = false } = {}) {
  if (confirmRedo) {
    const ok = await confirmDialog({ title: 'Yeniden dağıt', message: 'Bu günün listesi silinip baştan, adalet puanına göre yeniden yapılır. Elle yaptığın değişiklikler kaybolur.', confirmText: 'Yeniden dağıt' });
    if (!ok) return;
  }
  const entry = K.buildCleaning({ personnel: S.personnel, areas: S.areas, lists: S.lists, date, since: S.since });
  S.lists = { ...S.lists, [date]: entry };
  // Eski kayıtları budama
  const cutoff = addDays(todayISO(), -KEEP_DAYS);
  for (const d of Object.keys(S.lists)) if (d < cutoff) delete S.lists[d];
  if (await save(KEYS.lists, S.lists)) {
    const short = K.shortages(entry);
    toast(short.length ? `Liste hazır. Kişi yetmedi: ${short.map((s) => `${s.name} (${s.missing} eksik)`).join(', ')}.` : 'Mıntıka listesi hazır.', { kind: short.length ? 'warning' : 'success' });
    render();
  }
}

function editArea(entry, area) {
  const present = K.presentOn(S.personnel, entry.date);
  const where = {};
  for (const a of entry.areas) for (const id of a.ids) where[id] = a.id;
  for (const id of entry.spare || []) where[id] = '__spare';
  const boxes = present.map((p) => {
    const id = `ks-ea-${p.id}`;
    const other = where[p.id] && where[p.id] !== area.id ? (where[p.id] === '__spare' ? 'Boşta' : areaName(where[p.id]) || entry.areas.find((a) => a.id === where[p.id])?.name) : '';
    return el('label', { class: 'ks-check', for: id },
      el('input', { type: 'checkbox', class: 'checkbox', id, value: p.id, checked: area.ids.includes(p.id) }),
      el('span', null, p.name),
      other ? el('span', { class: 'small muted' }, `şu an: ${other}`) : null);
  });
  const form = el('form', { class: 'form-stack', novalidate: true },
    el('p', { class: 'small muted' }, `Bu yer için ${area.people} kişi planlı. Başka yerdeki birini seçersen oradan alınır.`),
    el('div', { class: 'ks-checks' }, boxes));
  form.addEventListener('submit', (e) => e.preventDefault());
  openDialog({
    title: area.name,
    content: form,
    size: 'sm',
    actions: [
      { label: 'Vazgeç', onClick: (d) => d.close() },
      {
        label: 'Kaydet', kind: 'primary',
        onClick: async (d) => {
          const ids = [...form.querySelectorAll('input:checked')].map((x) => x.value);
          const next = {
            ...entry,
            edited: true,
            areas: entry.areas.map((a) => (a.id === area.id ? { ...a, ids } : { ...a, ids: a.ids.filter((x) => !ids.includes(x)) })),
            spare: (entry.spare || []).filter((x) => !ids.includes(x))
          };
          // Bir yerden çıkarılan kişi hiçbir yerde değilse boşta görünsün
          const placed = new Set(next.areas.flatMap((a) => a.ids));
          for (const id of area.ids) if (!placed.has(id) && !next.spare.includes(id)) next.spare.push(id);
          S.lists = { ...S.lists, [entry.date]: next };
          if (await save(KEYS.lists, S.lists)) {
            await d.close(true);
            render();
          }
        }
      }
    ]
  });
}

function areaEditor(area) {
  const isNew = !area;
  const a = area || { id: '', name: '', people: 1, weight: 3, overflow: false };
  const form = el('form', { class: 'form-stack', novalidate: true },
    field({ label: 'Yerin adı', name: 'name', value: a.name, required: true, maxlength: 60, placeholder: 'ör. Yazhane + Koğuş', hint: 'Bir kişi iki yeri birlikte temizleyecekse ikisini tek yer olarak yaz.' }),
    el('div', { class: 'form-grid' },
      field({ label: 'Kaç kişi', name: 'people', type: 'select', value: String(a.people), options: [1, 2, 3, 4, 5, 6].map((n) => [String(n), `${n} kişi`]) }),
      field({ label: 'Zorluk', name: 'weight', type: 'select', value: String(a.weight), options: [5, 4, 3, 2, 1].map((n) => [String(n), `${n} – ${K.WEIGHT_LABELS[n]}`]), hint: 'Zor yerler en az puanı olan kişiye düşer.' })),
    field({ label: 'Fazla kişi olursa buraya ekle', name: 'overflow', type: 'checkbox', value: a.overflow, hint: 'Yerlerden fazla kişi varsa artanlar bu yere yazılır. Tek yer seçilebilir.' }));
  form.addEventListener('submit', (e) => e.preventDefault());
  const actions = [];
  if (!isNew) {
    actions.push({
      label: 'Sil', kind: 'danger', icon: 'trash', className: 'mr-auto',
      onClick: async (d) => {
        const fixedHere = S.personnel.filter((p) => p.fixed === a.id);
        const ok = await confirmDialog({ title: 'Yeri sil', message: `"${a.name}" silinsin mi?${fixedHere.length ? ` Sabit görevi burası olan ${fixedHere.map((p) => p.name).join(', ')} serbest kalır.` : ''} Geçmiş listeler değişmez.`, confirmText: 'Sil', danger: true });
        if (!ok) return;
        S.areas = S.areas.filter((x) => x.id !== a.id);
        S.personnel = S.personnel.map((p) => (p.fixed === a.id ? { ...p, fixed: null } : p));
        await save(KEYS.areas, S.areas);
        await save(KEYS.personnel, S.personnel);
        await d.close(true);
        render();
      }
    });
  }
  actions.push({ label: 'Vazgeç', onClick: (d) => d.close() });
  actions.push({
    label: 'Kaydet', kind: 'primary',
    onClick: async (d) => {
      clearFieldErrors(form);
      const name = form.elements.name.value.trim();
      if (!name) {
        showFieldErrors(form, { name: 'Yerin adını yaz.' });
        return;
      }
      if (S.areas.some((x) => x.id !== a.id && x.name.toLocaleLowerCase('tr-TR') === name.toLocaleLowerCase('tr-TR'))) {
        showFieldErrors(form, { name: 'Bu adla bir yer zaten var.' });
        return;
      }
      const item = { id: a.id || shortId(), name, people: Number(form.elements.people.value), weight: Number(form.elements.weight.value), overflow: form.elements.overflow.checked };
      let areas = isNew ? [...S.areas, item] : S.areas.map((x) => (x.id === a.id ? item : x));
      if (item.overflow) areas = areas.map((x) => (x.id === item.id ? x : { ...x, overflow: false }));
      S.areas = areas;
      if (await save(KEYS.areas, S.areas)) {
        await d.close(true);
        render();
      }
    }
  });
  openDialog({ title: isNew ? 'Yer ekle' : 'Yeri düzenle', content: form, actions });
}

async function moveArea(i, dir) {
  const j = i + dir;
  if (j < 0 || j >= S.areas.length) return;
  const list = [...S.areas];
  [list[i], list[j]] = [list[j], list[i]];
  S.areas = list;
  await save(KEYS.areas, S.areas);
  render();
}

function areasCard() {
  const slots = S.areas.reduce((n, a) => n + a.people, 0);
  return el('section', { class: 'card mt' },
    el('div', { class: 'card-header' }, el('h2', null, 'Yerler'), chip(`${S.areas.length} yer · ${slots} kişilik`)),
    S.areas.length ? el('ol', { class: 'ks-areas' }, S.areas.map((a, i) => el('li', null,
      el('span', { class: 'ks-area-main' },
        el('span', { class: 'ks-area-name' }, a.name),
        el('span', { class: 'small muted' }, [`${a.people} kişi`, `zorluk ${a.weight}`, a.overflow ? 'fazlalar buraya' : '', ...S.personnel.filter((p) => p.fixed === a.id).map((p) => `sabit: ${p.name}`)].filter(Boolean).join(' · '))),
      el('span', { class: 'ks-row-actions' },
        iconButton('arrowUp', `${a.name} yukarı taşı`, () => moveArea(i, -1), { disabled: i === 0 }),
        iconButton('arrowDown', `${a.name} aşağı taşı`, () => moveArea(i, 1), { disabled: i === S.areas.length - 1 }),
        iconButton('edit', `${a.name} düzenle`, () => areaEditor(a)))))) : el('p', { class: 'muted' }, 'Henüz yer yok.'),
    el('div', { class: 'row mt' }, button('Yer ekle', () => areaEditor(null), { iconName: 'plus' })));
}

function listCard(entry) {
  const short = K.shortages(entry);
  return el('section', { class: 'card ks-list', 'aria-labelledby': 'ks-list-title' },
    el('div', { class: 'card-header' },
      el('h2', { id: 'ks-list-title' }, formatDate(entry.date, { weekday: true })),
      entry.edited ? chip('Elle düzenlendi') : chip('Otomatik', { kind: 'green' })),
    short.length ? el('p', { class: 'notice notice-warning' }, icon('alert'), el('span', null, `Kişi yetmedi: ${short.map((s) => `${s.name} (${s.missing} eksik)`).join(', ')}. Yere dokunup elle tamamlayabilirsin.`)) : null,
    el('ul', { class: 'ks-assign' }, entry.areas.map((a) => {
      const btn = el('button', { type: 'button', class: 'ks-assign-row', 'aria-label': `${a.name}: ${a.ids.map(nameOf).join(', ') || 'kimse yok'}. Düzenle` },
        el('span', { class: 'ks-assign-area' }, el('span', { class: 'ks-assign-name' }, a.name), el('span', { class: 'small muted' }, `${a.ids.length}/${a.people} kişi`)),
        el('span', { class: 'ks-assign-people' }, a.ids.length ? a.ids.map((id) => personChip(id, { fixed: (a.fixed || []).includes(id) })) : el('span', { class: 'muted' }, 'Kimse yok')),
        icon('edit', { size: 16, className: 'ks-assign-edit' }));
      btn.addEventListener('click', () => editArea(entry, a));
      return el('li', null, btn);
    })),
    entry.spare && entry.spare.length ? el('p', { class: 'small' }, el('strong', null, 'Boşta: '), entry.spare.map(nameOf).join(', ')) : null,
    el('div', { class: 'row mt' },
      button('Resim olarak paylaş', () => cleaningImage(entry), { kind: 'primary', iconName: 'image' }),
      button('Metni kopyala', () => copyText(cleaningText(entry)), { iconName: 'copy' }),
      button('Yeniden dağıt', () => makeList(entry.date, { confirmRedo: true }), { iconName: 'refresh' }),
      button('Listeyi sil', async () => {
        const ok = await confirmDialog({ title: 'Listeyi sil', message: 'Bu günün listesi silinsin mi? Puanlardan da düşer.', confirmText: 'Sil', danger: true });
        if (!ok) return;
        const next = { ...S.lists };
        delete next[entry.date];
        S.lists = next;
        await save(KEYS.lists, S.lists);
        render();
      }, { kind: 'ghost', iconName: 'trash' })));
}

function renderMintika() {
  const panel = panels.mintika;
  if (!S.personnel.length) {
    needPersonnel(panel);
    panel.append(areasCard());
    return;
  }
  const date = selectedDate();
  const entry = S.lists[date];
  const present = K.presentOn(S.personnel, date);
  const slots = S.areas.reduce((n, a) => n + a.people, 0);
  const absent = S.personnel.filter((p) => K.isAbsent(p, date));
  const daySel = segmented([['today', 'Bugün'], ['tomorrow', 'Yarın']], S.day, (v) => {
    S.day = v;
    render();
  }, 'Liste günü');
  const past = Object.keys(S.lists).filter((d) => d < todayISO()).sort().reverse().slice(0, 7);
  replace(panel,
    el('div', { class: 'ks-toolbar' }, daySel,
      el('span', { class: 'small muted' }, `${present.length} kişi mevcut · ${slots} kişilik yer${absent.length ? ` · yok: ${absent.map((p) => p.name).join(', ')}` : ''}`)),
    entry ? listCard(entry) : el('section', { class: 'card ks-make' },
      el('div', { class: 'ks-make-head' }, icon('list', { size: 28 }),
        el('div', null, el('h2', null, `${S.day === 'tomorrow' ? 'Yarının' : 'Bugünün'} listesi henüz yapılmadı`),
          el('p', { class: 'muted' }, 'Sabit görevliler kendi yerine yazılır; kalanlar en az puanı olandan başlayarak zor yerlere dağıtılır. Dün aynı yerde olan mümkünse aynı yere düşmez.'))),
      present.length !== slots ? el('p', { class: 'notice notice-info' }, icon('info'), el('span', null, present.length < slots ? `${slots - present.length} kişi eksik; önce her yere en az bir kişi verilir.` : `${present.length - slots} kişi fazla; ${S.areas.find((a) => a.overflow) ? `"${S.areas.find((a) => a.overflow).name}" yerine eklenir` : 'boşta kalır'}.`)) : null,
      el('div', { class: 'row' }, button('Listeyi yap', () => makeList(date), { kind: 'primary', iconName: 'check', className: 'ks-big' }))),
    areasCard(),
    past.length ? el('section', { class: 'card mt' },
      el('h2', { class: 'ks-h2' }, 'Son listeler'),
      el('div', { class: 'stack' }, past.map((d) => el('details', { class: 'ks-past' },
        el('summary', null, formatDate(d, { weekday: true })),
        el('ul', { class: 'ks-past-list' }, S.lists[d].areas.map((a) => el('li', null, el('span', null, a.name), el('span', { class: 'muted' }, a.ids.map(nameOf).join(', ') || '—')))))))) : null);
}

// --- Nöbet ---

function dutyPeople() {
  return S.personnel.filter((p) => !p.noDuty);
}

function scheduleRows(sch) {
  return sch.slots.map((s, i) => {
    const a = fmtDateTime(s.start);
    const b = fmtDateTime(s.end);
    return { i, a, b, names: s.ids.map(nameOf) };
  });
}

function dutyText(sch) {
  const lines = ['NÖBET ÇİZELGESİ', ''];
  let day = '';
  for (const r of scheduleRows(sch)) {
    if (r.a.date !== day) {
      day = r.a.date;
      lines.push(`— ${r.a.day} —`);
    }
    lines.push(`${r.a.time}–${r.b.time}  ${r.names.join(' / ') || '—'}`);
  }
  return lines.join('\n');
}

function dutyImage(sch) {
  const now = K.currentSlot(sch);
  const rows = scheduleRows(sch);
  const first = rows[0];
  const last = rows[rows.length - 1];
  const canvas = drawTable({
    title: 'NÖBET ÇİZELGESİ',
    subtitle: `${first.a.day} ${first.a.time} → ${last.b.day} ${last.b.time}`,
    head: ['#', 'Saat', 'Nöbetçiler'],
    widths: [1, 4, 6],
    rows: rows.map((r) => [String(r.i + 1), `${r.a.day} ${r.a.time}–${r.b.time}`, r.names.join(', ') || '—']),
    footer: `JOZH · Kışla · ${sch.hours} saatlik ${rows.length} dilim`,
    highlight: now ? sch.slots.indexOf(now) : -1
  });
  shareCanvas(canvas, `nobet-${first.a.date}.png`, 'Nöbet çizelgesi');
}

function editSlot(sch, index) {
  const slot = sch.slots[index];
  const r = scheduleRows(sch)[index];
  const boxes = S.personnel.map((p) => {
    const id = `ks-slot-${p.id}`;
    return el('label', { class: 'ks-check', for: id },
      el('input', { type: 'checkbox', class: 'checkbox', id, value: p.id, checked: slot.ids.includes(p.id) }),
      el('span', null, p.name),
      p.noDuty ? el('span', { class: 'small muted' }, 'nöbetten muaf') : null);
  });
  const form = el('form', { class: 'form-stack' }, el('div', { class: 'ks-checks' }, boxes));
  form.addEventListener('submit', (e) => e.preventDefault());
  openDialog({
    title: `${r.a.day} ${r.a.time}–${r.b.time}`,
    content: form,
    size: 'sm',
    actions: [
      { label: 'Vazgeç', onClick: (d) => d.close() },
      {
        label: 'Kaydet', kind: 'primary',
        onClick: async (d) => {
          const ids = [...form.querySelectorAll('input:checked')].map((x) => x.value);
          const next = { ...sch, edited: true, slots: sch.slots.map((s, i) => (i === index ? { ...s, ids } : s)) };
          S.duties = S.duties.map((x) => (x.id === sch.id ? next : x));
          if (await save(KEYS.duties, S.duties)) {
            await d.close(true);
            render();
          }
        }
      }
    ]
  });
}

function dutyForm() {
  const people = dutyPeople();
  const today = todayISO();
  const next = people.length ? people[((S.dutyNext % people.length) + people.length) % people.length] : null;
  const form = el('form', { class: 'form-stack', novalidate: true },
    el('div', { class: 'form-grid ks-duty-grid' },
      field({ label: 'Başlangıç tarihi', name: 'sd', type: 'date', value: today, required: true }),
      field({ label: 'Başlangıç saati', name: 'st', type: 'time', value: '08:00', required: true }),
      field({ label: 'Bitiş tarihi', name: 'ed', type: 'date', value: addDays(today, 1), required: true }),
      field({ label: 'Bitiş saati', name: 'et', type: 'time', value: '08:00', required: true }),
      field({ label: 'Dilim süresi', name: 'hours', type: 'select', value: '2', options: [['1', '1 saat'], ['2', '2 saat'], ['3', '3 saat'], ['4', '4 saat']] }),
      field({ label: 'Her dilimde', name: 'per', type: 'select', value: '2', options: [['1', '1 nöbetçi'], ['2', '2 nöbetçi'], ['3', '3 nöbetçi']] }),
      field({ label: 'İlk nöbetçi', name: 'first', type: 'select', value: next ? next.id : '', options: people.map((p) => [p.id, p.name]), hint: 'Sıra, bir önceki çizelgenin kaldığı yerden devam eder.' })),
    el('div', { class: 'row' }, button('Çizelge oluştur', null, { kind: 'primary', type: 'submit', iconName: 'calendar' })));
  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    clearFieldErrors(form);
    const f = form.elements;
    const errors = {};
    if (!isValidISODate(f.sd.value)) errors.sd = 'Tarih seç.';
    if (!isValidISODate(f.ed.value)) errors.ed = 'Tarih seç.';
    if (!isValidTime(f.st.value)) errors.st = 'Saat seç.';
    if (!isValidTime(f.et.value)) errors.et = 'Saat seç.';
    if (Object.keys(errors).length) {
      showFieldErrors(form, errors);
      return;
    }
    const start = new Date(`${f.sd.value}T${f.st.value}:00`);
    const end = new Date(`${f.ed.value}T${f.et.value}:00`);
    if (!(end > start)) {
      showFieldErrors(form, { ed: 'Bitiş, başlangıçtan sonra olmalı.' });
      return;
    }
    const hours = Number(f.hours.value);
    try {
      const startIndex = Math.max(0, people.findIndex((p) => p.id === f.first.value));
      const res = K.buildDuty({
        start, end, hours, perSlot: Number(f.per.value), people, startIndex,
        absentOn: (p, d) => K.isAbsent(p, `${d.getFullYear()}-${pad2(d.getMonth() + 1)}-${pad2(d.getDate())}`)
      });
      const sch = { id: shortId(), createdAt: new Date().toISOString(), hours, perSlot: Number(f.per.value), slots: res.slots };
      S.duties = [...S.duties, sch].slice(-30);
      S.dutyNext = res.nextIndex;
      await save(KEYS.duties, S.duties);
      await save(KEYS.dutyNext, S.dutyNext);
      toast(`${res.slots.length} nöbet dilimi oluşturuldu.`, { kind: 'success' });
      render();
    } catch (err) {
      showFieldErrors(form, { ed: err.message });
    }
  });
  return form;
}

function scheduleCard(sch) {
  const now = K.currentSlot(sch);
  const rows = scheduleRows(sch);
  let day = '';
  return el('section', { class: 'card ks-duty mt', 'aria-labelledby': 'ks-duty-title' },
    el('div', { class: 'card-header' },
      el('h2', { id: 'ks-duty-title' }, 'Son çizelge'),
      chip(`${rows.length} dilim · ${sch.hours} saat`)),
    now ? el('p', { class: 'ks-now' }, icon('clock'), el('span', null, el('strong', null, 'Şu an nöbette: '), now.ids.map(nameOf).join(', ') || '—', ` (${fmtDateTime(now.end).time}'e kadar)`)) : null,
    el('div', { class: 'table-wrap' }, el('table', { class: 'table ks-duty-table' },
      el('caption', { class: 'visually-hidden' }, 'Nöbet çizelgesi'),
      el('thead', null, el('tr', null, el('th', { class: 'num' }, '#'), el('th', null, 'Saat'), el('th', null, 'Nöbetçiler'), el('th', null, el('span', { class: 'visually-hidden' }, 'İşlem')))),
      el('tbody', null, rows.flatMap((r) => {
        const out = [];
        if (r.a.date !== day) {
          day = r.a.date;
          out.push(el('tr', { class: 'ks-day-row' }, el('th', { colspan: '4', scope: 'colgroup' }, r.a.day)));
        }
        out.push(el('tr', { class: sch.slots[r.i] === now ? 'is-now' : '' },
          el('td', { class: 'num muted' }, String(r.i + 1)),
          el('td', { class: 'ks-time' }, `${r.a.time}–${r.b.time}`),
          el('td', null, r.names.join(', ') || el('span', { class: 'muted' }, '—')),
          el('td', null, iconButton('edit', `${r.a.time} dilimini düzenle`, () => editSlot(sch, r.i)))));
        return out;
      })))),
    el('div', { class: 'row mt' },
      button('Resim olarak paylaş', () => dutyImage(sch), { kind: 'primary', iconName: 'image' }),
      button('Metni kopyala', () => copyText(dutyText(sch)), { iconName: 'copy' }),
      button('Çizelgeyi sil', async () => {
        const ok = await confirmDialog({ title: 'Çizelgeyi sil', message: 'Bu çizelge silinsin mi? Nöbet sayaçlarından da düşer.', confirmText: 'Sil', danger: true });
        if (!ok) return;
        S.duties = S.duties.filter((x) => x.id !== sch.id);
        await save(KEYS.duties, S.duties);
        render();
      }, { kind: 'ghost', iconName: 'trash' })));
}

function renderNobet() {
  const panel = panels.nobet;
  if (!S.personnel.length) {
    needPersonnel(panel);
    return;
  }
  const sch = S.duties[S.duties.length - 1];
  const muaf = S.personnel.filter((p) => p.noDuty);
  replace(panel,
    el('section', { class: 'card' },
      el('div', { class: 'card-header' }, el('h2', null, 'Çizelge oluştur')),
      el('p', { class: 'small muted' }, `Sıra personel listesindeki sırayla döner; izinde olanlar o gün atlanır.${muaf.length ? ` Nöbetten muaf: ${muaf.map((p) => p.name).join(', ')}.` : ''}`),
      dutyPeople().length ? dutyForm() : el('p', { class: 'muted' }, 'Nöbet tutabilecek kimse yok (herkes muaf).')),
    sch ? scheduleCard(sch) : null);
}

// --- Personel ---

function personEditor(person) {
  const isNew = !person;
  const p = person || { id: '', name: '', fixed: null, noDuty: false, absentUntil: '' };
  const today = todayISO();
  const absentMode = !p.absentUntil || p.absentUntil < today ? 'none' : p.absentUntil === today ? 'today' : 'until';
  const form = el('form', { class: 'form-stack', novalidate: true },
    field({ label: 'Ad', name: 'name', value: p.name, required: true, maxlength: 40 }),
    field({ label: 'Sabit görev', name: 'fixed', type: 'select', value: p.fixed || '', options: [['', 'Yok (her gün dağıtılır)'], ...S.areas.map((a) => [a.id, a.name])], hint: 'Sabit görevli her gün aynı yere yazılır ve puan dağıtımına girmez.' }),
    field({ label: 'Nöbetten muaf', name: 'noDuty', type: 'checkbox', value: p.noDuty }),
    field({ label: 'Durum', name: 'absent', type: 'select', value: absentMode, options: [['none', 'Mevcut'], ['today', 'Bugün yok'], ['until', 'İzinde (tarihe kadar)']] }),
    field({ label: 'İzin bitişi (bu gün dahil yok)', name: 'until', type: 'date', value: absentMode === 'until' ? p.absentUntil : addDays(today, 1) }));
  const untilField = form.elements.until.closest('.field');
  const sync = () => {
    untilField.hidden = form.elements.absent.value !== 'until';
  };
  form.elements.absent.addEventListener('change', sync);
  sync();
  form.addEventListener('submit', (e) => e.preventDefault());
  const actions = [];
  if (!isNew) {
    actions.push({
      label: 'Sil', kind: 'danger', icon: 'trash', className: 'mr-auto',
      onClick: async (d) => {
        const ok = await confirmDialog({ title: 'Personeli sil', message: `${p.name} listeden silinsin mi? Geçmiş listelerde "Silinmiş kişi" olarak görünür.`, confirmText: 'Sil', danger: true });
        if (!ok) return;
        S.personnel = S.personnel.filter((x) => x.id !== p.id);
        await save(KEYS.personnel, S.personnel);
        await d.close(true);
        render();
      }
    });
  }
  actions.push({ label: 'Vazgeç', onClick: (d) => d.close() });
  actions.push({
    label: 'Kaydet', kind: 'primary',
    onClick: async (d) => {
      clearFieldErrors(form);
      const f = form.elements;
      const name = f.name.value.trim();
      const errors = {};
      if (!name) errors.name = 'Adı yaz.';
      else if (S.personnel.some((x) => x.id !== p.id && x.name.toLocaleLowerCase('tr-TR') === name.toLocaleLowerCase('tr-TR'))) errors.name = 'Bu adla biri zaten var; soyadının baş harfini ekleyebilirsin.';
      if (f.absent.value === 'until' && (!isValidISODate(f.until.value) || f.until.value < today)) errors.until = 'Bugün ya da sonrası bir tarih seç.';
      if (Object.keys(errors).length) {
        showFieldErrors(form, errors);
        return;
      }
      const absentUntil = f.absent.value === 'today' ? today : f.absent.value === 'until' ? f.until.value : '';
      const item = { ...p, id: p.id || shortId(), name, fixed: f.fixed.value || null, noDuty: f.noDuty.checked, absentUntil, absentFrom: absentUntil ? (p.absentUntil >= today && p.absentFrom ? p.absentFrom : today) : '' };
      S.personnel = isNew ? [...S.personnel, item] : S.personnel.map((x) => (x.id === p.id ? item : x));
      if (await save(KEYS.personnel, S.personnel)) {
        await d.close(true);
        render();
      }
    }
  });
  openDialog({ title: isNew ? 'Personel ekle' : p.name, content: form, actions });
}

async function toggleToday(p) {
  const today = todayISO();
  const absent = K.isAbsent(p, today);
  S.personnel = S.personnel.map((x) => (x.id === p.id ? { ...x, absentUntil: absent ? '' : today, absentFrom: absent ? '' : today } : x));
  await save(KEYS.personnel, S.personnel);
  render();
}

async function movePerson(i, dir) {
  const j = i + dir;
  if (j < 0 || j >= S.personnel.length) return;
  const list = [...S.personnel];
  [list[i], list[j]] = [list[j], list[i]];
  S.personnel = list;
  await save(KEYS.personnel, S.personnel);
  render();
}

function renderPersonel() {
  const today = todayISO();
  const present = K.presentOn(S.personnel, today);
  const quick = el('form', { class: 'ks-quick-add', novalidate: true },
    el('input', { type: 'text', name: 'name', class: 'input', maxlength: 40, placeholder: 'Ad yaz, Ekle\'ye bas', 'aria-label': 'Yeni personelin adı', autocomplete: 'off' }),
    button('Ekle', null, { kind: 'primary', type: 'submit', iconName: 'plus' }));
  quick.addEventListener('submit', async (e) => {
    e.preventDefault();
    const name = quick.elements.name.value.trim();
    if (!name) return;
    if (S.personnel.some((x) => x.name.toLocaleLowerCase('tr-TR') === name.toLocaleLowerCase('tr-TR'))) {
      toast('Bu adla biri zaten var.', { kind: 'warning' });
      return;
    }
    S.personnel = [...S.personnel, { id: shortId(), name, fixed: null, noDuty: false, absentUntil: '', absentFrom: '' }];
    if (await save(KEYS.personnel, S.personnel)) {
      render();
      panels.personel.querySelector('.ks-quick-add input').focus();
    }
  });
  replace(panels.personel,
    el('section', { class: 'card' },
      el('div', { class: 'card-header' }, el('h2', null, 'Personel'), chip(`${S.personnel.length} kişi · bugün ${present.length} mevcut`)),
      quick,
      S.personnel.length ? el('ol', { class: 'ks-people' }, S.personnel.map((p, i) => {
        const absent = K.isAbsent(p, today);
        return el('li', { class: absent ? 'is-absent' : '' },
          avatar(p.name),
          el('span', { class: 'ks-people-main' },
            el('span', { class: 'ks-people-name' }, p.name),
            el('span', { class: 'ks-people-tags' },
              p.fixed && areaName(p.fixed) ? chip(`Sabit: ${areaName(p.fixed)}`, { kind: 'yellow' }) : null,
              p.noDuty ? chip('Nöbetten muaf') : null,
              absent ? chip(p.absentUntil === today ? 'Bugün yok' : `İzinde · ${formatDate(p.absentUntil, { short: true, year: false })}'e kadar`, { kind: 'red' }) : null)),
          el('span', { class: 'ks-row-actions' },
            button(absent ? 'Var' : 'Yok', () => toggleToday(p), { className: 'btn-small' }),
            iconButton('arrowUp', `${p.name} yukarı taşı`, () => movePerson(i, -1), { disabled: i === 0 }),
            iconButton('arrowDown', `${p.name} aşağı taşı`, () => movePerson(i, 1), { disabled: i === S.personnel.length - 1 }),
            iconButton('edit', `${p.name} düzenle`, () => personEditor(p))));
      })) : el('p', { class: 'muted' }, 'Henüz kimse yok. Adları tek tek ekle; sıra nöbet sırasıdır.')),
    el('p', { class: 'small muted mt' }, '"Yok" yalnızca bugün içindir, yarın kendiliğinden mevcut olur. Birkaç günlük izin için kişiyi düzenle → Durum: İzinde.'));
}

// --- İstatistik ---

function bar(pct) {
  const fill = el('span', { class: 'ks-bar-fill' });
  fill.style.width = `${Math.round(pct)}%`;
  return el('span', { class: 'ks-bar', 'aria-hidden': 'true' }, fill);
}

function renderStats() {
  const panel = panels.stats;
  if (!S.personnel.length) {
    needPersonnel(panel);
    return;
  }
  const { counts, points } = K.cleaningStats(S.lists, { since: S.since });
  const duty = K.dutyCounts(S.duties, S.since);
  const rows = S.personnel.slice().sort((a, b) => (points[b.id] || 0) - (points[a.id] || 0));
  const max = Math.max(1, ...rows.map((p) => points[p.id] || 0));
  replace(panel,
    el('section', { class: 'card' },
      el('div', { class: 'card-header' }, el('h2', null, 'Sayaçlar'), chip(S.since ? `${formatDate(S.since, { short: true })} tarihinden beri` : 'Başlangıçtan beri')),
      el('p', { class: 'small muted' }, 'Puan = temizlik yaptığı yerlerin zorluk toplamı. Dağıtım en düşük puanlıdan başlar.'),
      el('div', { class: 'table-wrap' }, el('table', { class: 'table ks-stats' },
        el('thead', null, el('tr', null,
          el('th', null, 'Kişi'),
          ...S.areas.map((a) => el('th', { class: 'num' }, a.name)),
          el('th', { class: 'num' }, 'Nöbet'),
          el('th', { class: 'num' }, 'Puan'))),
        el('tbody', null, rows.map((p) => el('tr', null,
          el('th', { scope: 'row' }, p.name, p.fixed ? el('span', { class: 'small muted' }, ' (sabit)') : null),
          ...S.areas.map((a) => el('td', { class: 'num' }, String((counts[p.id] || {})[a.id] || 0))),
          el('td', { class: 'num' }, String(duty[p.id] || 0)),
          el('td', { class: 'num ks-points' },
            el('span', null, String(points[p.id] || 0)),
            bar(((points[p.id] || 0) / max) * 100))))))),
      el('div', { class: 'row mt' }, button('Sayaçları sıfırla', async () => {
        const ok = await confirmDialog({ title: 'Sayaçları sıfırla', message: 'Puanlar ve sayaçlar bugünden itibaren yeniden sayılır. Geçmiş listeler silinmez.', confirmText: 'Sıfırla', danger: true });
        if (!ok) return;
        S.since = todayISO();
        await save(KEYS.since, S.since);
        render();
      }, { kind: 'danger', iconName: 'refresh' }))));
}

// --- Genel ---

function render() {
  for (const [k, node] of Object.entries(panels)) node.hidden = k !== S.tab;
  if (S.tab === 'mintika') renderMintika();
  else if (S.tab === 'nobet') renderNobet();
  else if (S.tab === 'personel') renderPersonel();
  else renderStats();
}

async function load() {
  const get = async (k, def) => {
    const v = await db.getMeta(k);
    return v === undefined || v === null ? def : v;
  };
  S.personnel = await get(KEYS.personnel, []);
  const areas = await get(KEYS.areas, null);
  S.areas = Array.isArray(areas) ? areas : K.DEFAULT_AREAS.map((a) => ({ ...a }));
  if (!Array.isArray(areas)) await db.setMeta(KEYS.areas, S.areas);
  S.lists = await get(KEYS.lists, {});
  S.duties = await get(KEYS.duties, []);
  S.dutyNext = await get(KEYS.dutyNext, 0);
  S.since = await get(KEYS.since, '');
}

async function setup() {
  replace(main, loadingState());
  try {
    await load();
  } catch (err) {
    toastError('kisla.load', err);
  }
  setup.tabs = segmented(TABS, S.tab, goTab, 'Bölüm');
  setup.tabs.classList.add('ks-tabs');
  replace(main, setup.tabs, ...Object.values(panels));
  render();
}

const ready = await initApp({ page: 'kisla', title: 'Kışla' });
if (ready) await setup();
