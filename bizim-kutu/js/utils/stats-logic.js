// İstatistik hesapları (saf fonksiyonlar — birim testleri bunları sınar).

/** Rota → bölüm adı */
export function sectionOf(route = '') {
  if (route === '/home' || route === '/' || !route) return 'home';
  if (route.startsWith('/chat')) return 'chat';
  if (route.startsWith('/games') || route.startsWith('/play') || route.startsWith('/stories')) return 'games';
  for (const s of ['watch', 'memories', 'movies', 'tasks', 'vault']) if (route.startsWith(`/${s}`)) return s;
  return 'other';
}

export const dayKey = (d = new Date()) => `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`;

/** 3725 sn → "1 sa 2 dk"; 40 sn → "1 dk'dan az" */
export function fmtDuration(sec) {
  const s = Math.max(0, Math.round(Number(sec) || 0));
  if (s < 60) return s ? '1 dk\'dan az' : '0 dk';
  const d = Math.floor(s / 86400), hh = Math.floor((s % 86400) / 3600), mm = Math.floor((s % 3600) / 60);
  if (d) return `${d} gün ${hh} sa`;
  if (hh) return mm ? `${hh} sa ${mm} dk` : `${hh} sa`;
  return `${mm} dk`;
}

/** Mesaj listesinden özet (silinenler hariç). Testler için dışa açık. */
export function messageSummary(messages, people, now = Date.now()) {
  const per = Object.fromEntries(people.map((p) => [p, 0]));
  const days = {};
  let first = 0, total = 0;
  for (const m of messages) {
    if (!m || m.deleted || !people.includes(m.uid)) continue;
    total += 1; per[m.uid] += 1;
    const ts = Number(m.ts) || 0;
    if (ts) {
      if (!first || ts < first) first = ts;
      const k = dayKey(new Date(ts));
      days[k] = (days[k] || 0) + 1;
    }
  }
  let busiest = null;
  for (const [day, n] of Object.entries(days)) if (!busiest || n > busiest.n) busiest = { day, n };
  const spanDays = first ? Math.max(1, Math.ceil((now - first) / 86400000)) : 0;
  return { total, per, first, busiest, perDay: spanDays ? total / spanDays : 0 };
}

