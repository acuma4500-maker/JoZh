/* Bizim Kutu service worker
 * - Uygulama kabuğu sürümlü önbellekte tutulur (çevrim dışı açılış + hızlı yükleme).
 * - Firebase ve diğer üçüncü taraf istekleri ASLA önbelleğe alınmaz (kişisel veri cihaza yazılmaz).
 * - Yeni sürüm "bekleyen" durumda kalır; uygulama kullanıcıya "Güncelle" sorar ve SKIP_WAITING gönderir.
 * Dağıtımda tools/make-zip.sh VERSION değerini dosya içeriklerinin karmasıyla otomatik günceller.
 */
const VERSION = 'bk-1.0.0-dev';
const CACHE = `bizim-kutu-${VERSION}`;
const SHELL = [
  './', './index.html', './manifest.json',
  './css/variables.css', './css/global.css', './css/components.css', './css/animations.css', './css/responsive.css',
  './js/app.js', './js/features.js', './js/viewport.js', './js/auth.js', './js/router.js', './js/state.js', './js/constants.js', './js/firebase-config.js', './js/vendor/firebase.js',
  './js/services/firestore.js', './js/services/realtime.js', './js/services/presence.js', './js/services/notifications.js',
  './js/services/games.js', './js/services/crypto.js',
  './js/pages/login.js', './js/pages/home.js', './js/pages/chat.js', './js/pages/memories.js', './js/pages/movies.js', './js/pages/tasks.js',
  './js/pages/vault.js', './js/pages/games.js', './js/pages/play.js', './js/pages/stories.js', './js/pages/notifications.js',
  './js/pages/profile.js', './js/pages/more.js',
  './js/games/registry.js', './js/games/common.js', './js/games/xox.js', './js/games/know-me.js', './js/games/truth-dare.js',
  './js/games/emoji.js', './js/games/memory.js', './js/games/story.js', './js/games/story-data.js', './js/games/questions.js',
  './js/utils/helpers.js', './js/utils/dates.js', './js/utils/validation.js', './js/utils/icons.js', './js/utils/ui.js',
  './js/utils/chat-logic.js', './js/utils/questions-data.js',
  './data/questions.json',
  './assets/icons/icon.svg', './assets/icons/icon-192.png', './assets/icons/icon-512.png', './assets/icons/apple-touch-icon.png', './assets/icons/maskable-512.png',
  './assets/fonts/nunito-latin-wght-normal.woff2', './assets/fonts/nunito-latin-ext-wght-normal.woff2',
  './assets/fonts/fraunces-latin-wght-normal.woff2', './assets/fonts/fraunces-latin-ext-wght-normal.woff2', './assets/fonts/fraunces-latin-wght-italic.woff2',
];

self.addEventListener('install', (event) => {
  // Yeni sürüm beklemeden devreye girer (uygulama sayfayı bir kez yeniler).
  event.waitUntil(caches.open(CACHE).then((c) => c.addAll(SHELL.map((u) => new Request(u, { cache: 'reload' })))).then(() => self.skipWaiting()));
});

self.addEventListener('activate', (event) => {
  event.waitUntil((async () => {
    const keys = await caches.keys();
    await Promise.all(keys.filter((k) => k.startsWith('bizim-kutu-') && k !== CACHE).map((k) => caches.delete(k)));
    await self.clients.claim();
  })());
});

self.addEventListener('message', (event) => {
  if (event.data?.type === 'SKIP_WAITING') self.skipWaiting();
});

self.addEventListener('fetch', (event) => {
  const req = event.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.origin !== self.location.origin) return; // Firebase vb.: doğrudan ağ

  // Sayfa gezintisi: önce ağ (güncel index), çevrim dışıysa önbellek
  if (req.mode === 'navigate') {
    event.respondWith((async () => {
      try {
        const fresh = await fetch(req);
        const cache = await caches.open(CACHE);
        cache.put('./index.html', fresh.clone());
        return fresh;
      } catch {
        return (await caches.match('./index.html')) || Response.error();
      }
    })());
    return;
  }

  // Statik dosyalar: önce önbellek, yoksa ağ (ve önbelleğe ekle)
  event.respondWith((async () => {
    const cached = await caches.match(req, { ignoreSearch: true });
    if (cached) return cached;
    const res = await fetch(req);
    if (res.ok && res.type === 'basic') (await caches.open(CACHE)).put(req, res.clone());
    return res;
  })());
});
