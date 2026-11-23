import './viewport.js';
// Bizim Kutu — uygulama giriş noktası.
import { partnerOf, userName, userEmoji } from './constants.js';
import { watchAuth, logoutDevice } from './auth.js';
import { auth, rtdb } from './firebase-config.js';
import { ref as dbRef, onValue as onDbValue } from './vendor/firebase.js';
import { getState, setState, subscribe } from './state.js';
import { startRouter } from './router.js';
import { h, clear, createScope, debounce, fill } from './utils/helpers.js';
import { icons, logoSvg } from './utils/icons.js';
import { toast } from './utils/ui.js';
import { startPresence, stopPresence } from './services/presence.js';
import { startUsage } from './services/usage.js';
import { subscribeRecent, subscribeReceipts, markReceipt, primeReceipts, unreadCount } from './services/realtime.js';
import { startNotifications, announce, systemNotify, allowed } from './services/notifications.js';
import { subscribeInvites, isInviteLive, acceptInvite, cleanupOldGames } from './services/games.js';
import { col, listen } from './services/firestore.js';
import { renderLogin } from './pages/login.js';
import { on } from './features.js';
import { gameById } from './games/registry.js';
import { lastSeenText } from './utils/dates.js';

const root = document.getElementById('app');
const DEFAULT_PREFS = { theme: 'system', reduceMotion: false, notif: { message: true, game: true, memory: true, task: true }, system: false, lockAfter: 2 };
let appScope = null;

// ---------- Tercihler (tema, hareket) ----------
export function applyPrefs(prefs) {
  const p = { ...DEFAULT_PREFS, ...prefs, notif: { ...DEFAULT_PREFS.notif, ...(prefs?.notif || {}) } };
  const html = document.documentElement;
  if (p.theme === 'light' || p.theme === 'dark') html.dataset.theme = p.theme; else delete html.dataset.theme;
  html.classList.toggle('reduce-motion', !!p.reduceMotion);
  const dark = p.theme === 'dark' || (p.theme === 'system' && matchMedia('(prefers-color-scheme: dark)').matches);
  document.querySelector('meta[name="theme-color"]')?.setAttribute('content', dark ? '#2A1720' : '#FFF8F6');
  return p;
}
function cachedPrefs(uid) { try { return JSON.parse(localStorage.getItem(`bk.prefs.${uid}`) || 'null'); } catch { return null; } }
export function setPrefs(prefs) {
  const p = applyPrefs(prefs);
  setState({ prefs: p });
  try { localStorage.setItem(`bk.prefs.${getState().uid}`, JSON.stringify(p)); } catch {}
}

// ---------- Kimlik doğrulama akışı ----------
function showSplash() {
  fill(root, h('div', { class: 'splash', role: 'status', 'aria-label': 'Yükleniyor' },
    h('div', { class: 'splash__logo', svg: logoSvg }), h('p', { class: 'splash__text' }, 'Kutumuz açılıyor…')));
}

showSplash();
// Firebase önceki (anonim) cihaz oturumunu geri yükleyince PIN ekranını göster.
// Uygulama her açılışta ve arka plandan dönüşte PIN ister.
let authReady = false;
watchAuth(() => { if (!authReady) { authReady = true; showLogin(); } });

function showLogin() {
  teardown();
  setState({ user: null, uid: null, partnerUid: null });
  renderLogin(root, {
    onLoggedIn: (person) => {
      setState({ user: auth.currentUser, uid: person, partnerUid: partnerOf(person) });
      const p = cachedPrefs(person); if (p) setPrefs(p);
      startApp();
    },
  });
}
const lockScreen = () => showLogin();

/** Uygulama arka planda belirlenen süreden uzun kalırsa kilitlenir. */
function watchAutoLock(getMinutes, onLock) {
  let hiddenAt = 0;
  const handler = () => {
    if (document.visibilityState === 'hidden') hiddenAt = Date.now();
    else if (hiddenAt) {
      const min = getMinutes();
      if (min >= 0 && Date.now() - hiddenAt >= min * 60000) onLock();
      hiddenAt = 0;
    }
  };
  document.addEventListener('visibilitychange', handler);
  return () => document.removeEventListener('visibilitychange', handler);
}

export async function logout() {
  try { await stopPresence(); } catch {}
  teardown();
  try { sessionStorage.clear(); } catch {}
  await logoutDevice();
  // Bellekte kalan her şeyi temizlemek için sayfayı yeniden yükle.
  location.replace(location.pathname + '#/home');
  location.reload();
}

function teardown() {
  if (appScope) { appScope.dispose(); appScope = null; }
}

// ---------- Uygulama kabuğu ----------
const NAV_ALL = [
  { path: '/home', label: 'Ana Sayfa', icon: 'home' },
  { path: '/chat', label: 'Sohbet', icon: 'chat', badge: 'chat', feature: 'chat' },
  { path: '/games', label: 'Oyunlar', icon: 'game', badge: 'games', feature: 'games' },
  { path: '/memories', label: 'Anılar', icon: 'book', feature: 'memories' },
  { path: '/watch', label: 'Birlikte İzle', icon: 'tv', extra: true, feature: 'watch' },
  { path: '/movies', label: 'Filmler', icon: 'film', extra: true, feature: 'movies' },
  { path: '/tasks', label: 'Görevler', icon: 'tasks', extra: true, feature: 'tasks' },
  { path: '/vault', label: 'Kasa', icon: 'lock', extra: true, feature: 'vault' },
  { path: '/stats', label: 'İstatistik', icon: 'chart', extra: true, feature: 'stats' },
  // Oyunlar açıkken mobil menüye sığması için Profil 'Daha' menüsüne geçer
  { path: '/profile', label: 'Profil', icon: 'user', extra: on('games') },
  { path: '/more', label: 'Daha', icon: 'menu', mobileOnly: true },
];
// Kapalı bölümler menüde görünmez. Az bölüm açıkken "Daha" menüsüne gerek yok.
const NAV = NAV_ALL.filter((n) => on(n.feature) && !(n.mobileOnly && !['movies', 'tasks', 'vault', 'notifications', 'games', 'watch'].some(on)));

function startApp() {
  teardown();
  const scope = createScope();
  appScope = scope;
  const { uid, partnerUid } = getState();

  const titleEl = h('h1', { class: 'topbar__title' }, 'Bizim Kutu');
  const backBtn = h('a', { class: 'icon-btn topbar__back', href: '#/home', 'aria-label': 'Geri', svg: icons.back, hidden: true });
  const partnerDot = h('span', { class: 'dot' });
  const partnerSub = h('span', { class: 'partner-chip__sub' }, '');
  const partnerChip = h('a', { class: 'partner-chip', href: '#/profile', 'aria-live': 'polite' },
    h('span', { class: 'partner-chip__avatar', 'aria-hidden': 'true' }, userEmoji(partnerUid), partnerDot),
    h('span', { class: 'partner-chip__text' }, h('span', { class: 'partner-chip__name' }, userName(partnerUid)), partnerSub));
  const bellBadge = h('span', { class: 'badge', hidden: true });
  const bell = on('notifications') ? h('a', { class: 'icon-btn bell', href: '#/notifications', 'aria-label': 'Bildirimler', svg: icons.bell }, bellBadge) : null;
  const offline = h('div', { class: 'offline-banner', role: 'status', hidden: true }, h('span', { svg: icons.wifiOff }), h('span', {}, 'Bağlantı yok — yeniden bağlanılıyor…'));

  const navBadges = {};
  const navLinks = NAV.map((n) => {
    const badge = n.badge ? (navBadges[n.badge] = h('span', { class: 'badge', hidden: true })) : null;
    return h('a', { class: `tab${n.extra ? ' tab--extra' : ''}${n.mobileOnly ? ' tab--mobile' : ''}`, href: `#${n.path}`, dataset: { path: n.path } },
      h('span', { class: 'tab__icon', svg: icons[n.icon] }, badge), h('span', { class: 'tab__label' }, n.label));
  });

  const view = h('main', { class: 'view', id: 'view', tabindex: '-1' });
  const shell = h('div', { class: 'shell' },
    h('a', { class: 'skip-link', href: '#view' }, 'İçeriğe geç'),
    h('header', { class: 'topbar glass' },
      backBtn,
      h('a', { class: 'topbar__brand', href: '#/home', 'aria-label': 'Ana sayfa', svg: logoSvg }),
      titleEl, h('div', { class: 'topbar__spacer' }), partnerChip, bell),
    offline,
    h('nav', { class: 'tabbar glass', 'aria-label': 'Ana menü' },
      h('div', { class: 'tabbar__brand' }, h('span', { svg: logoSvg }), h('span', {}, 'Bizim Kutu')), navLinks),
    view);
  fill(root, shell);

  scope.add(startRouter(view, (route, path) => {
    titleEl.textContent = route.title;
    document.title = route.path === '/home' ? 'Bizim Kutu ❤️' : `${route.title} · Bizim Kutu`;
    backBtn.hidden = !route.back; if (route.back) backBtn.href = route.back;
    shell.classList.toggle('shell--full', !!route.fullHeight);
    navLinks.forEach((a) => {
      const active = path === a.dataset.path || (a.dataset.path === '/games' && (path.startsWith('/play') || path === '/stories'))
        || (a.dataset.path === '/more' && ['/movies', '/tasks', '/vault', '/profile', '/notifications', '/more', '/watch'].includes(path));
      a.classList.toggle('is-active', active);
      if (active) a.setAttribute('aria-current', 'page'); else a.removeAttribute('aria-current');
    });
  }));

  // Çevrim içi durum
  startPresence(uid);
  scope.add(() => stopPresence());
  scope.add(startUsage(uid, partnerUid)); // nerede ne kadar zaman geçirdik

  const renderPartner = () => {
    const p = getState().presence[partnerUid];
    partnerDot.className = `dot ${p?.online ? 'dot--on' : 'dot--off'}`;
    partnerSub.textContent = p?.online ? 'Çevrim içi' : lastSeenText(p?.lastSeen).replace('Son görülme ', '');
  };
  scope.add(subscribe(renderPartner, ['presence']));
  scope.interval(renderPartner, 30000);
  renderPartner();

  // Bağlantı durumu (kısa kopmalarda banner titremesin diye gecikmeli)
  const showOffline = debounce((v) => { offline.hidden = !v; }, 2500);
  const updOffline = () => {
    const s = getState();
    const bad = !s.online || !s.connected;
    if (bad) showOffline(true); else { showOffline.cancel(); offline.hidden = true; }
  };
  scope.on(window, 'online', () => setState({ online: true }));
  scope.on(window, 'offline', () => setState({ online: false }));
  scope.add(subscribe(updOffline, ['connected', 'online']));

  // Profiller ve tercihler
  scope.add(listen(col('profiles'), (items) => {
    const profiles = Object.fromEntries(items.map((p) => [p.id, p]));
    setState({ profiles });
    if (profiles[uid]?.prefs) setPrefs(profiles[uid].prefs);
  }));

  // Sohbet: okundu bilgileri + son mesajlar
  let firstMessages = true;
  let lastNotifiedTs = 0;
  if (on('chat')) scope.add(subscribeReceipts((receipts) => { primeReceipts(receipts[uid]); setState({ receipts }); recountUnread(); }));
  if (on('chat')) scope.add(subscribeRecent((list) => {
    setState({ recentMessages: list });
    const fromPartner = list.filter((m) => m.uid === partnerUid && typeof m.ts === 'number');
    const latest = fromPartner.at(-1);
    if (latest) markReceipt(uid, 'deliveredAt', latest.ts); // karşı cihaza ulaştı (çift tik)
    if (!firstMessages && latest && latest.ts > lastNotifiedTs && !latest.deleted && getState().route !== '/chat' && allowed('message')) {
      toast(`💬 ${userName(partnerUid)}: ${latest.text.slice(0, 80)}`, { duration: 4000, action: { label: 'Aç', onClick: () => { location.hash = '#/chat'; } } });
      systemNotify(`${userName(partnerUid)} sana yazdı`, latest.text.slice(0, 120), '#/chat');
    }
    if (latest) lastNotifiedTs = Math.max(lastNotifiedTs, latest.ts);
    firstMessages = false;
    recountUnread();
  }));
  function recountUnread() {
    const s = getState();
    setState({ unreadMessages: unreadCount(s.recentMessages, uid, s.receipts[uid]?.readAt || 0) });
  }

  // Bildirimler
  if (on('notifications')) scope.add(startNotifications(uid, (n) => { if (n.type !== 'game_invite') announce(n); }));

  // Oyun davetleri
  const announced = new Set();
  let firstInvites = true;
  if (on('games')) scope.add(subscribeInvites((list) => {
    setState({ invites: list });
    for (const inv of list) {
      const key = `${inv.id}:${inv.status}`;
      if (announced.has(key)) continue;
      announced.add(key);
      if (firstInvites && inv.status !== 'pending') continue;
      const g = gameById(inv.game);
      if (inv.to === uid && isInviteLive(inv) && allowed('game_invite')) {
        toast(`🎮 ${userName(inv.from)} seni ${g?.name || 'oyuna'} davet ediyor`, {
          duration: 12000,
          action: { label: 'Kabul et', onClick: async () => { try { location.hash = `#/play/${await acceptInvite(inv)}`; } catch (e) { toast(e.message, { type: 'error' }); } } }
        });
        systemNotify('Oyun daveti 🎮', `${userName(inv.from)} seni ${g?.name || 'bir oyuna'} davet ediyor`, '#/games');
      }
      if (!firstInvites && inv.from === uid && inv.status === 'accepted') {
        toast(`🎉 ${userName(inv.to)} davetini kabul etti!`);
        location.hash = `#/play/${inv.id}`;
      }
      if (!firstInvites && inv.from === uid && inv.status === 'declined') toast(`${userName(inv.to)} şu an oynayamıyor 🙈`);
    }
    firstInvites = false;
    updateBadges();
  }));

  // Birlikte izle: partner video açınca/başlatınca, başka sayfadaysam haber ver
  if (on('watch')) {
    let lastSeen = null;
    scope.add(onDbValue(dbRef(rtdb, 'watch/room'), (s) => {
      const r = s.val();
      const key = r ? `${r.videoId}|${r.state}` : '';
      const prev = lastSeen;
      lastSeen = key;
      if (prev === null || key === prev || !r?.videoId || r.by !== partnerUid || getState().route === '/watch') return;
      const newVideo = !prev.startsWith(`${r.videoId}|`);
      if (r.state === 'playing' || newVideo) {
        toast(`🎬 ${userName(partnerUid)} birlikte izlemek istiyor`, { duration: 9000, action: { label: 'Aç', onClick: () => { location.hash = '#/watch'; } } });
        systemNotify('Birlikte izleyelim 🎬', `${userName(partnerUid)} bir video açtı`, '#/watch');
      }
    }, () => {}));
  }

  // Rozetler
  function updateBadges() {
    const s = getState();
    const setBadge = (el, n) => { if (!el) return; el.hidden = !n; el.textContent = n > 9 ? '9+' : String(n); };
    setBadge(navBadges.chat, s.unreadMessages);
    setBadge(navBadges.games, s.invites.filter((i) => i.to === uid && isInviteLive(i)).length);
    setBadge(bellBadge, s.notifications.filter((n) => !n.read).length + (s.unreadMessages ? 1 : 0));
    const total = s.unreadMessages + s.notifications.filter((n) => !n.read).length;
    document.title = document.title.replace(/^\(\d+\+?\) /, '');
    if (total) document.title = `(${total > 9 ? '9+' : total}) ${document.title}`;
  }
  scope.add(subscribe(updateBadges, ['unreadMessages', 'notifications', 'invites', 'route']));
  scope.interval(updateBadges, 15000);

  // Otomatik kilit
  scope.add(watchAutoLock(() => Number(getState().prefs.lockAfter ?? 2), () => lockScreen()));

  if (on('games')) scope.timeout(() => cleanupOldGames(), 8000);
}

// ---------- Service worker ----------
if ('serviceWorker' in navigator && location.protocol !== 'file:') {
  window.addEventListener('load', async () => {
    try {
      const reg = await navigator.serviceWorker.register('service-worker.js', { scope: './' });
      // Yeni sürüm otomatik devreye girer; daha önce bir sürüm çalışıyorsa sayfa bir kez yenilenir.
      // (İlk kurulumda yenileme yapılmaz.)
      const hadController = !!navigator.serviceWorker.controller;
      let reloaded = false;
      navigator.serviceWorker.addEventListener('controllerchange', () => { if (hadController && !reloaded) { reloaded = true; location.reload(); } });
      reg.update().catch(() => {});
      setInterval(() => reg.update().catch(() => {}), 60 * 60 * 1000);
    } catch (e) { console.warn('SW kaydı başarısız', e); }
  });
}

// Sistem teması değişirse yeniden uygula
matchMedia('(prefers-color-scheme: dark)').addEventListener?.('change', () => applyPrefs(getState().prefs));
