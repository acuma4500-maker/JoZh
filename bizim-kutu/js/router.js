// Hash tabanlı yönlendirici (#/sohbet gibi). cPanel'de sayfa yenilemede 404 oluşmaz,
// sunucu tarafı yönlendirme kuralı gerekmez.
import { createScope, clear, h, fill, add } from './utils/helpers.js';
import { setState } from './state.js';
import { errorState, emptyState } from './utils/ui.js';
import { on } from './features.js';

const routes = [
  { path: '/home', title: 'Bizim Kutu', load: () => import('./pages/home.js') },
  { path: '/chat', feature: 'chat', title: 'Sohbet', load: () => import('./pages/chat.js'), fullHeight: true },
  { path: '/memories', feature: 'memories', title: 'Anı Defteri', load: () => import('./pages/memories.js') },
  { path: '/movies', feature: 'movies', title: 'Film & Dizi', load: () => import('./pages/movies.js') },
  { path: '/tasks', feature: 'tasks', title: 'Yapılacaklar', load: () => import('./pages/tasks.js') },
  { path: '/vault', feature: 'vault', title: 'Özel Kasamız', load: () => import('./pages/vault.js') },
  { path: '/games', feature: 'games', title: 'Oyun Merkezi', load: () => import('./pages/games.js') },
  { path: '/play/:id', feature: 'games', title: 'Oyun', load: () => import('./pages/play.js'), back: '#/games' },
  { path: '/stories', feature: 'games', title: 'Hikâyelerimiz', load: () => import('./pages/stories.js'), back: '#/games' },
  { path: '/notifications', feature: 'notifications', title: 'Bildirimler', load: () => import('./pages/notifications.js') },
  { path: '/profile', title: 'Profil', load: () => import('./pages/profile.js') },
  { path: '/more', title: 'Kutumuz', load: () => import('./pages/more.js') },
];

function match(hash) {
  const path = (hash.replace(/^#/, '') || '/home').split('?')[0];
  for (const r of routes) {
    const keys = [];
    const re = new RegExp('^' + r.path.replace(/:(\w+)/g, (_, k) => { keys.push(k); return '([^/]+)'; }) + '/?$');
    const m = re.exec(path);
    if (m) return { route: r, params: Object.fromEntries(keys.map((k, i) => [k, decodeURIComponent(m[i + 1])])), path };
  }
  return null;
}

let current = null;
let viewEl = null;
let onRoute = null;
let token = 0;

export function startRouter(el, onChange) {
  viewEl = el; onRoute = onChange;
  window.addEventListener('hashchange', render);
  render();
  return () => { window.removeEventListener('hashchange', render); current?.scope.dispose(); current = null; };
}

export const navigate = (path) => { if (location.hash !== `#${path}`) location.hash = path; else render(); };

async function render() {
  const m = match(location.hash);
  if (!m) { location.replace('#/home'); return; }
  const my = ++token;
  current?.scope.dispose();
  const scope = createScope();
  current = { scope, path: m.path };
  setState({ route: m.path });
  onRoute?.(m.route, m.path);
  clear(viewEl);
  viewEl.className = `view${m.route.fullHeight ? ' view--full' : ''}`;
  add(viewEl, h('div', { class: 'page-loading', 'aria-hidden': 'true' }, h('span', { class: 'heart-loader' }, '❤')));
  try {
    if (!on(m.route.feature)) {
      fill(viewEl, h('section', { class: 'page page-enter' }, emptyState({ emoji: '🌱', title: 'Bu bölüm yakında açılacak', text: 'Kutumuzu adım adım kuruyoruz 💕', action: { label: 'Ana sayfaya dön', onClick: () => { location.hash = '#/home'; } } })));
      return;
    }
    const mod = await m.route.load();
    if (my !== token || scope.disposed) return;
    clear(viewEl);
    const page = h('section', { class: 'page page-enter', 'aria-label': m.route.title });
    add(viewEl, page);
    await mod.default(page, { params: m.params, scope, title: m.route.title });
    viewEl.scrollTop = 0; window.scrollTo(0, 0);
    if (!document.activeElement || document.activeElement === document.body) page.focus?.({ preventScroll: true });
  } catch (e) {
    console.error(e);
    if (my !== token) return;
    fill(viewEl, errorState('Sayfa yüklenemedi. Bağlantını kontrol edip tekrar dene.', () => render()));
  }
}
