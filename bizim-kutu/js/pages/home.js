// Ana sayfa: birliktelik sayacı, çevrim içi durumlar, özet kartlar.
import { getState, subscribe } from '../state.js';
import { userName, userEmoji, START_DATE, ALLOWED_UIDS } from '../constants.js';
import { h, clear, fill, add } from '../utils/helpers.js';
import { icons } from '../utils/icons.js';
import { togetherDuration, pad2, formatLongDate, formatTime, dayLabel, lastSeenText, formatISODate, dueLabel } from '../utils/dates.js';
import { col, listen, query, where, orderBy, limit } from '../services/firestore.js';
import { isInviteLive } from '../services/games.js';
import { gameById } from '../games/registry.js';
import { questionOfDay } from '../utils/questions-data.js';
import { on } from '../features.js';

const STATUS_TR = { watchlist: 'İzlemek istediklerimiz', watching: 'İzliyoruz', watched: 'İzlediklerimiz' };

export default async function home(page, { scope }) {
  const { uid } = getState();

  // --- Sayaç ---
  const dEl = h('span', { class: 'counter-days__num' }, '0');
  const tiles = { h: h('b', {}, '00'), m: h('b', {}, '00'), s: h('b', {}, '00') };
  const counterLabel = h('span', { class: 'counter-days__label' }, 'gündür birlikteyiz');
  const startText = formatLongDate(new Date(START_DATE.year, START_DATE.month - 1, START_DATE.day));
  const tick = () => {
    const d = togetherDuration(new Date());
    dEl.textContent = d.days.toLocaleString('tr-TR');
    tiles.h.textContent = pad2(d.hours); tiles.m.textContent = pad2(d.minutes); tiles.s.textContent = pad2(d.seconds);
    counterLabel.textContent = d.future ? 'gün kaldı' : 'gündür birlikteyiz';
  };
  tick();
  scope.interval(tick, 1000);

  const hero = h('div', { class: 'hero' },
    h('div', { class: 'hero__glow', 'aria-hidden': 'true' }),
    h('h2', { class: 'hero__title' }, 'Bizim Kutu ', h('span', { class: 'heartbeat inline-heart', 'aria-hidden': 'true' }, '❤️')),
    h('p', { class: 'hero__names' }, ALLOWED_UIDS.map(userName).join(' & ')),
    h('div', { class: 'counter', role: 'timer', 'aria-live': 'off', 'aria-label': 'Birliktelik sayacı' },
      h('div', { class: 'counter-days' }, dEl, counterLabel),
      h('div', { class: 'counter-tiles' },
        h('div', { class: 'tile' }, tiles.h, h('small', {}, 'saat')),
        h('div', { class: 'tile' }, tiles.m, h('small', {}, 'dakika')),
        h('div', { class: 'tile' }, tiles.s, h('small', {}, 'saniye')))),
    h('p', { class: 'hero__since' }, `${startText}'ten beri`));

  // --- Çevrim içi ---
  const presenceRow = h('div', { class: 'presence-row' });
  const drawPresence = () => {
    const pr = getState().presence;
    fill(presenceRow, ...ALLOWED_UIDS.map((u) => {
      const p = pr[u];
      return h('div', { class: 'presence-card' },
        h('span', { class: 'presence-card__avatar', 'aria-hidden': 'true' }, userEmoji(u), h('span', { class: `dot ${p?.online ? 'dot--on' : 'dot--off'}` })),
        h('div', {}, h('strong', {}, userName(u) + (u === uid ? ' (sen)' : '')),
          h('small', {}, p?.online ? 'Çevrim içi' : (p ? lastSeenText(p.lastSeen) : 'Çevrim dışı'))));
    }));
  };
  drawPresence();
  scope.add(subscribe(drawPresence, ['presence']));
  scope.interval(drawPresence, 30000);

  // --- Kartlar ---
  const card = (href, icon, title, cls = '') => {
    const body = h('div', { class: 'home-card__body' }, h('div', { class: 'sk sk--line' }), h('div', { class: 'sk sk--line sk--short' }));
    const el = h('a', { class: `home-card ${cls}`, href },
      h('div', { class: 'home-card__head' }, h('span', { class: 'home-card__icon', svg: icons[icon] }), h('span', { class: 'home-card__title' }, title)), body);
    return { el, set: (...nodes) => fill(body, ...nodes) };
  };
  const cMsg = card('#/chat', 'chat', 'Son mesaj', 'home-card--wide');
  const cMem = card('#/memories', 'book', 'Son anı');
  const cTask = card('#/tasks', 'tasks', 'Yaklaşan görev');
  const cMovie = card('#/movies', 'film', 'İzlenecek');
  const cGame = card('#/games', 'game', 'Oyun davetleri');
  const cQ = card(on('games') ? '#/games' : '#/home', 'sparkles', 'Günün sorusu', 'home-card--wide home-card--accent');
  const muted = (t) => h('p', { class: 'muted' }, t);

  const drawMsg = () => {
    const s = getState();
    const m = [...s.recentMessages].reverse().find((x) => !x.deleted);
    if (!m) return cMsg.set(muted('Henüz mesaj yok. İlk "seni seviyorum"u sen yaz 💌'));
    cMsg.set(h('p', { class: 'home-card__text' }, h('strong', {}, `${userName(m.uid)}: `), m.text),
      h('small', { class: 'muted' }, typeof m.ts === 'number' ? `${dayLabel(m.ts)} ${formatTime(m.ts)}` : 'gönderiliyor…'),
      s.unreadMessages ? h('span', { class: 'pill pill--primary' }, `${s.unreadMessages} okunmamış`) : null);
  };
  if (on('chat')) { drawMsg(); scope.add(subscribe(drawMsg, ['recentMessages', 'unreadMessages'])); }

  const drawGames = () => {
    const live = getState().invites.filter((i) => isInviteLive(i));
    const incoming = live.filter((i) => i.to === uid);
    if (!live.length) return cGame.set(muted('Bekleyen davet yok. Hadi bir oyun başlat 🎮'));
    cGame.set(...live.slice(0, 2).map((i) => h('p', { class: 'home-card__text' },
      `${gameById(i.game)?.emoji || '🎮'} ${i.to === uid ? `${userName(i.from)} seni ${gameById(i.game)?.name} oynamaya çağırıyor` : `${gameById(i.game)?.name} daveti bekliyor`}`)),
      incoming.length ? h('span', { class: 'pill pill--primary' }, 'Yanıtla') : null);
  };
  if (on('games')) { drawGames(); scope.add(subscribe(drawGames, ['invites'])); scope.interval(drawGames, 10000); }

  const fail = (c) => () => c.set(muted('Yüklenemedi. Bağlantını kontrol et.'));
  if (on('memories')) scope.add(listen(query(col('memories'), orderBy('createdAt', 'desc'), limit(1)), ([m]) => {
    if (!m) return cMem.set(muted('İlk anınızı deftere yazın 📖'));
    cMem.set(h('p', { class: 'home-card__text' }, `${m.emoji || '💗'} ${m.title}`), h('small', { class: 'muted' }, formatISODate(m.date)));
  }, fail(cMem)));

  if (on('tasks')) scope.add(listen(query(col('tasks'), orderBy('createdAt', 'desc'), limit(100)), (all) => {
    const open = all.filter((x) => !x.done);
    const dated = open.filter((x) => x.dueDate).sort((a, b) => (a.dueDate < b.dueDate ? -1 : 1));
    const t = dated[0] || open[0];
    if (!t) return cTask.set(muted('Bekleyen görev yok ✨'));
    cTask.set(h('p', { class: 'home-card__text' }, t.title), t.dueDate ? h('small', { class: `muted${dueLabel(t.dueDate).includes('gecikti') ? ' text-danger' : ''}` }, dueLabel(t.dueDate)) : h('small', { class: 'muted' }, 'Son tarih yok'));
  }, fail(cTask)));

  if (on('movies')) scope.add(listen(query(col('movies'), where('status', 'in', ['watching', 'watchlist']), orderBy('createdAt', 'desc'), limit(10)), (items) => {
    const m = items.find((x) => x.status === 'watching') || items[0];
    if (!m) return cMovie.set(muted('Listeye bir film ekleyin 🍿'));
    cMovie.set(h('p', { class: 'home-card__text' }, `${m.kind === 'dizi' ? '📺' : '🎬'} ${m.title}`), h('small', { class: 'muted' }, STATUS_TR[m.status]));
  }, fail(cMovie)));

  questionOfDay().then((q) => cQ.set(h('p', { class: 'home-card__text home-card__quote' }, `“${q.text}”`), h('small', { class: 'muted' }, `${q.emoji} ${q.categoryName} · ${on('games') ? 'Soru Cevap oyununda birlikte cevaplayın' : 'Bugün birbirinize sorun 💬'}`)))
    .catch(() => cQ.set(muted('Soru yüklenemedi.')));

  add(page, hero, presenceRow, h('div', { class: 'home-grid' }, on('chat') && cMsg.el, on('games') && cGame.el, on('memories') && cMem.el, on('tasks') && cTask.el, on('movies') && cMovie.el, cQ.el));
}
