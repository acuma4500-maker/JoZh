// Kışla: mıntıka (temizlik) dağıtımı ve nöbet çizelgesi. DOM kullanmaz.
// Adalet kuralı: zor yerler, o güne kadar en az puan toplamış kişiye verilir; dün aynı yerde olan mümkünse oraya verilmez.

export const DEFAULT_AREAS = [
  { id: 'tuvalet', name: 'Tuvalet', people: 2, weight: 5, overflow: false },
  { id: 'banyo', name: 'Banyo', people: 1, weight: 4, overflow: false },
  { id: 'yazhane', name: 'Yazhane + Koğuş', people: 1, weight: 2, overflow: false },
  { id: 'koridor', name: 'Koridor', people: 1, weight: 2, overflow: false },
  { id: 'dis', name: 'Dış mıntıka + Çamaşırhane', people: 2, weight: 3, overflow: true }
];

export const WEIGHT_LABELS = { 1: 'Çok hafif', 2: 'Hafif', 3: 'Orta', 4: 'Ağır', 5: 'Çok ağır' };

export function isAbsent(person, date) {
  if (!person.absentUntil) return false;
  return person.absentUntil >= date && (!person.absentFrom || person.absentFrom <= date);
}

export function presentOn(personnel, date) {
  return personnel.filter((p) => !isAbsent(p, date));
}

// Geçmiş listelerden kişi başı yer sayıları ve puan (since tarihinden itibaren, exclude tarihi hariç)
export function cleaningStats(lists, { since = '', exclude = '' } = {}) {
  const counts = {};
  const points = {};
  for (const [date, entry] of Object.entries(lists || {})) {
    if (date < since || date === exclude || !entry || !Array.isArray(entry.areas)) continue;
    for (const a of entry.areas) {
      for (const id of a.ids || []) {
        counts[id] = counts[id] || {};
        counts[id][a.id] = (counts[id][a.id] || 0) + 1;
        points[id] = (points[id] || 0) + (Number(a.weight) || 1);
      }
    }
  }
  return { counts, points };
}

function previousEntry(lists, date) {
  const dates = Object.keys(lists || {}).filter((d) => d < date).sort();
  return dates.length ? lists[dates[dates.length - 1]] : null;
}

export function buildCleaning({ personnel, areas, lists, date, since = '', random = Math.random }) {
  const present = presentOn(personnel, date);
  const areaIds = new Set(areas.map((a) => a.id));
  const out = areas.map((a) => ({ id: a.id, name: a.name, weight: Number(a.weight) || 1, people: Number(a.people) || 0, ids: [], fixed: [] }));
  const byId = Object.fromEntries(out.map((a) => [a.id, a]));
  for (const p of present) {
    if (p.fixed && areaIds.has(p.fixed)) {
      byId[p.fixed].ids.push(p.id);
      byId[p.fixed].fixed.push(p.id);
    }
  }
  const { counts, points } = cleaningStats(lists, { since, exclude: date });
  const prev = previousEntry(lists, date);
  const lastArea = {};
  if (prev) for (const a of prev.areas || []) for (const id of a.ids || []) lastArea[id] = a.id;
  const jitter = Object.fromEntries(present.map((p) => [p.id, random()]));
  let pool = present.filter((p) => !(p.fixed && areaIds.has(p.fixed))).map((p) => p.id);
  // Ağır yerden hafife; eşitlikte listedeki sıra
  const order = out.map((a, i) => ({ a, i })).sort((x, y) => y.a.weight - x.a.weight || x.i - y.i).map((x) => x.a);
  // Önce her yere en az bir kişi, sonra kalan yerler (kişi eksikse hafif yer boş kalmasın diye)
  const open = out.reduce((n, a) => n + Math.max(0, a.people - a.ids.length), 0);
  const passes = pool.length < open ? [1, Infinity] : [Infinity];
  for (const pass of passes) for (const area of order) {
    while (area.ids.length < Math.min(area.people, pass) && pool.length) {
      pool.sort((x, y) =>
        (points[x] || 0) - (points[y] || 0)
        || ((counts[x] || {})[area.id] || 0) - ((counts[y] || {})[area.id] || 0)
        || (lastArea[x] === area.id) - (lastArea[y] === area.id)
        || jitter[x] - jitter[y]);
      const pick = pool.shift();
      area.ids.push(pick);
      // Aynı gün içindeki sonraki seçimler de adil olsun
      points[pick] = (points[pick] || 0) + area.weight;
    }
  }
  const overflow = out.find((a) => areas.find((x) => x.id === a.id).overflow);
  let spare = [];
  if (pool.length) {
    if (overflow) overflow.ids.push(...pool);
    else spare = pool;
  }
  return { date, areas: out.map(({ fixed, ...a }) => ({ ...a, fixed })), spare, createdAt: new Date().toISOString() };
}

export function shortages(entry) {
  return (entry.areas || []).filter((a) => a.ids.length < a.people).map((a) => ({ id: a.id, name: a.name, missing: a.people - a.ids.length }));
}

// --- Nöbet ---

// people: nöbete girebilecek kişiler (sırayla). startIndex: dönüşün kaldığı yer.
export function buildDuty({ start, end, hours = 2, perSlot = 2, people, startIndex = 0, absentOn = () => false }) {
  const s = new Date(start);
  const e = new Date(end);
  if (!(e > s)) throw new Error('Bitiş, başlangıçtan sonra olmalı.');
  if (!people.length) throw new Error('Nöbet tutabilecek kimse yok.');
  const slotMs = hours * 3600000;
  const count = Math.ceil((e - s) / slotMs);
  if (count > 200) throw new Error('Aralık çok uzun (en fazla 200 dilim).');
  const slots = [];
  let idx = ((startIndex % people.length) + people.length) % people.length;
  for (let i = 0; i < count; i++) {
    const bs = new Date(s.getTime() + i * slotMs);
    const be = new Date(Math.min(bs.getTime() + slotMs, e.getTime()));
    const ids = [];
    let guard = 0;
    while (ids.length < Math.min(perSlot, people.length) && guard < people.length * 2) {
      const p = people[idx % people.length];
      idx += 1;
      guard += 1;
      if (ids.includes(p.id) || absentOn(p, bs)) continue;
      ids.push(p.id);
    }
    slots.push({ start: bs.toISOString(), end: be.toISOString(), ids });
  }
  return { slots, nextIndex: idx % people.length };
}

export function currentSlot(schedule, now = new Date()) {
  if (!schedule) return null;
  const t = now.getTime();
  return schedule.slots.find((x) => new Date(x.start).getTime() <= t && t < new Date(x.end).getTime()) || null;
}

export function dutyCounts(schedules, since = '') {
  const c = {};
  for (const sch of schedules || []) {
    if ((sch.createdAt || '').slice(0, 10) < since) continue;
    for (const slot of sch.slots || []) for (const id of slot.ids) c[id] = (c[id] || 0) + 1;
  }
  return c;
}
