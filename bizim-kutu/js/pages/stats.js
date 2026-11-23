// İstatistiklerimiz 📊 — sitede nerede ne kadar zaman geçirdik, ne kadar mesajlaştık, ne kadar oynadık.
import { rtdb } from '../firebase-config.js';
import { ref, get, onValue } from '../vendor/firebase.js';
import { getState } from '../state.js';
import { ALLOWED_UIDS, userName, userEmoji } from '../constants.js';
import { h, fill, add } from '../utils/helpers.js';
import { formatLongDate } from '../utils/dates.js';
import { col, countOf, query, where } from '../services/firestore.js';
import { GAMES } from '../games/registry.js';
import { SECTIONS, fmtDuration, dayKey } from '../services/usage.js';
import { messageSummary } from '../utils/stats-logic.js';

const num = (n) => (typeof n === 'number' ? n.toLocaleString('tr-TR') : '—');
const sum = (obj) => Object.values(obj || {}).reduce((a, b) => a + (Number(b) || 0), 0);

export default async function stats(page, { scope }) {
  const { uid } = getState();
  const people = [uid, ...ALLOWED_UIDS.filter((p) => p !== uid)];
  const color = (p) => (p === ALLOWED_UIDS[0] ? 'var(--burgundy)' : 'var(--primary)');

  const timeBox = h('div', { class: 'stats-stack' }, h('div', { class: 'card stats-loading' }, 'Hesaplanıyor…'));
  const msgBox = h('div', { class: 'card stats-card' }, h('h3', { class: 'stats-title' }, '💬 Mesajlaşma'), h('p', { class: 'muted small' }, 'Sayılıyor…'));
  const gameBox = h('div', { class: 'card stats-card' }, h('h3', { class: 'stats-title' }, '🎮 Oyunlar'), h('p', { class: 'muted small' }, 'Sayılıyor…'));
  const otherBox = h('div', { class: 'card stats-card' }, h('h3', { class: 'stats-title' }, '💗 Birlikte biriktirdiklerimiz'), h('p', { class: 'muted small' }, 'Sayılıyor…'));

  add(page,
    h('div', { class: 'page-head' }, h('div', {}, h('h2', { class: 'page-title' }, 'İstatistiklerimiz'), h('p', { class: 'page-sub' }, 'Nerede ne kadar zaman geçirdik?'))),
    timeBox, msgBox, gameBox, otherBox,
    h('p', { class: 'muted small center' }, 'Süreler yalnızca uygulama açık ve ekranda iken sayılır. Süre sayımı bu sürümle başladı; daha önceki zamanlar sayılmadı.'));

  const legend = () => h('div', { class: 'stats-legend' }, people.map((p) => h('span', {}, h('i', { style: { background: color(p) } }), p === uid ? 'Sen' : userName(p))));

  // ---------- Zaman (canlı) ----------
  scope.add(onValue(ref(rtdb, 'stats'), (s) => {
    const v = s.val() || {};
    const time = v.time || {};
    const daily = v.daily || {};
    const total = (p) => sum(Object.fromEntries(Object.entries(time[p] || {}).filter(([k]) => k !== 'together')));
    const grand = people.reduce((a, p) => a + total(p), 0);
    const together = Math.max(...people.map((p) => Number(time[p]?.together) || 0));
    const today = dayKey();
    const week = new Set(Array.from({ length: 7 }, (_, i) => dayKey(new Date(Date.now() - i * 86400000))));
    const todaySum = people.reduce((a, p) => a + (Number(daily[p]?.[today]) || 0), 0);
    const weekSum = people.reduce((a, p) => a + Object.entries(daily[p] || {}).filter(([d]) => week.has(d)).reduce((x, [, n]) => x + n, 0), 0);

    const rows = Object.keys(SECTIONS)
      .map((k) => ({ k, per: Object.fromEntries(people.map((p) => [p, Number(time[p]?.[k]) || 0])) }))
      .map((r) => ({ ...r, total: sum(r.per) }))
      .filter((r) => r.total >= 1)
      .sort((a, b) => b.total - a.total);
    const max = rows[0]?.total || 1;

    fill(timeBox,
      h('div', { class: 'card stats-hero' },
        h('small', {}, 'Bizim Kutu\'da geçirdiğimiz toplam zaman'),
        h('strong', { class: 'stats-hero__big' }, fmtDuration(grand)),
        h('div', { class: 'stats-hero__people' }, people.map((p) => h('span', {}, `${userEmoji(p)} ${p === uid ? 'Sen' : userName(p)}: `, h('b', {}, fmtDuration(total(p))))))),
      h('div', { class: 'stats-tiles' },
        tile('🫶', fmtDuration(together), 'Aynı anda buradaydık'),
        tile('☀️', fmtDuration(todaySum), 'Bugün'),
        tile('📊', fmtDuration(weekSum), 'Son 7 gün')),
      h('div', { class: 'card stats-card' },
        h('div', { class: 'stats-card__head' }, h('h3', { class: 'stats-title' }, '⏱ Nerede ne kadar?'), legend()),
        rows.length
          ? h('div', { class: 'stats-bars' }, rows.map((r) => h('div', { class: 'stats-bar' },
            h('div', { class: 'stats-bar__label' }, h('span', {}, `${SECTIONS[r.k].emoji} ${SECTIONS[r.k].label}`), h('b', {}, fmtDuration(r.total))),
            h('div', { class: 'stats-bar__track', role: 'img', 'aria-label': people.map((p) => `${p === uid ? 'Sen' : userName(p)} ${fmtDuration(r.per[p])}`).join(', ') },
              h('div', { class: 'stats-bar__fill', style: { width: `${Math.max(2, (r.total / max) * 100)}%` } },
                people.map((p) => (r.per[p] ? h('i', { style: { flexGrow: String(r.per[p]), background: color(p) } }) : null)))))))
          : h('p', { class: 'muted small' }, 'Henüz süre birikmedi. Uygulamayı kullandıkça burası dolacak 💕')));
  }, () => fill(timeBox, h('div', { class: 'card' }, h('p', { class: 'muted' }, 'İstatistikler okunamadı. Realtime Database kurallarını güncelledin mi?')))));

  function tile(emoji, value, label) {
    return h('div', { class: 'stats-tile' }, h('span', { class: 'stats-tile__emoji' }, emoji), h('b', {}, value), h('small', {}, label));
  }

  // ---------- Mesajlar ----------
  (async () => {
    try {
      const snap = await get(ref(rtdb, 'chat/messages'));
      if (scope.disposed) return;
      const list = [];
      snap.forEach((c) => { list.push(c.val()); });
      const m = messageSummary(list, people);
      fill(msgBox, h('div', { class: 'stats-card__head' }, h('h3', { class: 'stats-title' }, '💬 Mesajlaşma'), legend()),
        h('div', { class: 'stats-tiles' },
          tile('💌', num(m.total), 'Toplam mesaj'),
          ...people.map((p) => tile(userEmoji(p), num(m.per[p]), p === uid ? 'Senin mesajın' : `${userName(p)}'nın mesajı`)),
          tile('📈', m.perDay ? num(Math.round(m.perDay)) : '—', 'Günde ortalama')),
        m.total ? h('div', { class: 'stats-split' }, people.map((p) => h('i', { style: { flexGrow: String(m.per[p] || 0), background: color(p) } }))) : null,
        h('ul', { class: 'stats-facts' },
          m.first ? h('li', {}, '🕊 İlk mesaj: ', h('b', {}, formatLongDate(new Date(m.first)))) : null,
          m.busiest ? h('li', {}, '🔥 En çok konuştuğumuz gün: ', h('b', {}, formatLongDate(new Date(`${m.busiest.day}T12:00:00`))), ` (${num(m.busiest.n)} mesaj)`) : null));
    } catch { fill(msgBox, h('h3', { class: 'stats-title' }, '💬 Mesajlaşma'), h('p', { class: 'muted small' }, 'Mesajlar sayılamadı.')); }
  })();

  // ---------- Oyunlar ----------
  (async () => {
    try {
      const snap = await get(ref(rtdb, 'games/scores'));
      if (scope.disposed) return;
      const all = snap.val() || {};
      const lines = GAMES.map((g) => ({ g, s: all[g.id] || {} })).map((x) => ({ ...x, n: sum(x.s) })).filter((x) => x.n > 0).sort((a, b) => b.n - a.n);
      const totalGames = lines.reduce((a, x) => a + x.n, 0);
      const wins = (p) => lines.reduce((a, x) => a + (Number(x.s[p]) || 0), 0);
      fill(gameBox, h('div', { class: 'stats-card__head' }, h('h3', { class: 'stats-title' }, '🎮 Oyunlar'), legend()),
        h('div', { class: 'stats-tiles' },
          tile('🏁', num(totalGames), 'Biten oyun'),
          ...people.map((p) => tile('🏆', num(wins(p)), p === uid ? 'Senin galibiyetin' : `${userName(p)} kazandı`)),
          tile('🤝', num(lines.reduce((a, x) => a + (Number(x.s.draw) || 0), 0)), 'Berabere')),
        lines.length
          ? h('ul', { class: 'stats-games' }, lines.map(({ g, s, n }) => h('li', {},
            h('span', {}, `${g.emoji} ${g.name}`),
            h('small', { class: 'muted' }, `${n} oyun · ${people.map((p) => `${p === uid ? 'Sen' : userName(p)} ${Number(s[p]) || 0}`).join(' · ')}${s.draw ? ` · berabere ${s.draw}` : ''}`))))
          : h('p', { class: 'muted small' }, 'Henüz biten oyun yok. Oyun Merkezi seni bekliyor 🎲'),
        h('p', { class: 'muted small' }, 'Oyunlarda geçen süre yukarıdaki "Nerede ne kadar?" listesinde.'));
    } catch { fill(gameBox, h('h3', { class: 'stats-title' }, '🎮 Oyunlar'), h('p', { class: 'muted small' }, 'Oyunlar sayılamadı.')); }
  })();

  // ---------- Diğer ----------
  (async () => {
    const safe = (p) => p.catch(() => null);
    const [memories, watched, done, videos] = await Promise.all([
      safe(countOf(col('memories'))),
      safe(countOf(query(col('movies'), where('status', '==', 'watched')))),
      safe(countOf(query(col('tasks'), where('done', '==', true)))),
      safe(get(ref(rtdb, 'watch/history')).then((s) => s.size)),
    ]);
    if (scope.disposed) return;
    fill(otherBox, h('h3', { class: 'stats-title' }, '💗 Birlikte biriktirdiklerimiz'),
      h('div', { class: 'stats-tiles' },
        tile('📖', num(memories), 'Anı'),
        tile('🍿', num(watched), 'İzlenen film/dizi'),
        tile('✅', num(done), 'Tamamlanan görev'),
        tile('🎬', num(videos), 'Birlikte açılan video')));
  })();
}
