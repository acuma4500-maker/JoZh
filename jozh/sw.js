// JOZH Service Worker. VERSION, js/app.js içindeki APP_VERSION ile aynı olmalıdır.
// Yeni dosya eklendiğinde APP_ASSETS listesine eklenir ve VERSION artırılır (tests/precache-check.mjs denetler).
const VERSION = '1.3.1';
const APP_CACHE = `jozh-app-${VERSION}`;
const SDK_VERSION = '10.12.2';
const SDK_CACHE = `jozh-firebase-sdk-${SDK_VERSION}`;
const SDK_URLS = [
  `https://www.gstatic.com/firebasejs/${SDK_VERSION}/firebase-app.js`,
  `https://www.gstatic.com/firebasejs/${SDK_VERSION}/firebase-firestore.js`
];

const APP_ASSETS = [
  './',
  './index.html',
  './manifest.json',
  './pages/backup.html',
  './pages/calendar.html',
  './pages/dashboard.html',
  './pages/diary.html',
  './pages/dreams.html',
  './pages/finance.html',
  './pages/interview.html',
  './pages/login.html',
  './pages/notes.html',
  './pages/partner.html',
  './pages/plans.html',
  './pages/profile.html',
  './pages/settings.html',
  './pages/vault-login.html',
  './pages/vault.html',
  './css/base.css',
  './css/components.css',
  './css/layout.css',
  './css/responsive.css',
  './css/themes.css',
  './css/pages/backup.css',
  './css/pages/calendar.css',
  './css/pages/dashboard.css',
  './css/pages/diary.css',
  './css/pages/dreams.css',
  './css/pages/finance.css',
  './css/pages/interview.css',
  './css/pages/login.css',
  './css/pages/notes.css',
  './css/pages/partner.css',
  './css/pages/plans.css',
  './css/pages/profile.css',
  './css/pages/settings.css',
  './css/pages/vault-login.css',
  './css/pages/vault.css',
  './js/app.js',
  './js/boot.js',
  './js/index.js',
  './js/navigation.js',
  './js/pwa.js',
  './js/router.js',
  './js/ui.js',
  './js/validators.js',
  './js/components/charts.js',
  './js/components/day-plans.js',
  './js/components/list-editor.js',
  './js/components/photos.js',
  './js/components/pin-pad.js',
  './js/components/plan-editor.js',
  './js/data/interview-bank.js',
  './js/firebase/firebase-config.js',
  './js/firebase/firestore.js',
  './js/firebase/sync-manager.js',
  './js/modules/backup.js',
  './js/modules/calendar.js',
  './js/modules/dashboard.js',
  './js/modules/diary.js',
  './js/modules/dreams.js',
  './js/modules/finance.js',
  './js/modules/interview.js',
  './js/modules/login.js',
  './js/modules/notes.js',
  './js/modules/partner.js',
  './js/modules/plans.js',
  './js/modules/profile.js',
  './js/modules/settings.js',
  './js/modules/vault-login.js',
  './js/modules/vault.js',
  './js/storage/app-lock.js',
  './js/storage/backup-manager.js',
  './js/storage/biometric.js',
  './js/storage/encryption.js',
  './js/storage/image-storage.js',
  './js/storage/local-db.js',
  './js/storage/records.js',
  './js/storage/schemas.js',
  './js/storage/sync-key.js',
  './js/storage/vault-storage.js',
  './js/utils/autosave.js',
  './js/utils/dates.js',
  './js/utils/finance-helpers.js',
  './js/utils/formatters.js',
  './js/utils/icons.js',
  './js/utils/id-generator.js',
  './js/utils/labels.js',
  './js/utils/logger.js',
  './js/utils/partner-helpers.js',
  './js/utils/plan-helpers.js',
  './js/utils/tags.js',
  './assets/icons/apple-touch-icon.png',
  './assets/icons/favicon-32.png',
  './assets/icons/icon-192.png',
  './assets/icons/icon-512.png',
  './assets/icons/icon-maskable-512.png'
];

self.addEventListener('install', (event) => {
  event.waitUntil((async () => {
    // Tek dosya bile inmezse kurulum başarısız sayılır.
    const cache = await caches.open(APP_CACHE);
    await cache.addAll(APP_ASSETS.map((url) => new Request(url, { cache: 'reload' })));
    // Firebase SDK ayrıca önbelleğe alınır; inmezse ilk kullanımda alınır.
    try {
      const sdk = await caches.open(SDK_CACHE);
      await Promise.all(SDK_URLS.map(async (url) => {
        const res = await fetch(new Request(url, { mode: 'cors' }));
        if (res.ok) await sdk.put(url, res);
      }));
    } catch (err) {
      // çevrimdışı kurulum: SDK sonra alınır
    }
  })());
});

self.addEventListener('activate', (event) => {
  event.waitUntil((async () => {
    const keys = await caches.keys();
    await Promise.all(keys
      .filter((k) => (k.startsWith('jozh-app-') && k !== APP_CACHE) || (k.startsWith('jozh-firebase-sdk-') && k !== SDK_CACHE))
      .map((k) => caches.delete(k)));
    await self.clients.claim();
  })());
});

async function fromAppCache(request) {
  const cache = await caches.open(APP_CACHE);
  const hit = await cache.match(request, { ignoreSearch: true });
  if (hit) return hit;
  try {
    return await fetch(request);
  } catch (err) {
    if (request.mode === 'navigate') {
      // İçeriği yerinde sunmak göreli yolları bozar; index.html'e yönlendirilir.
      return Response.redirect(new URL('./index.html', self.registration.scope).href, 302);
    }
    throw err;
  }
}

async function fromSdkCache(request) {
  const cache = await caches.open(SDK_CACHE);
  const hit = await cache.match(request);
  if (hit) return hit;
  const res = await fetch(request);
  if (res.ok) await cache.put(request, res.clone());
  return res;
}

self.addEventListener('fetch', (event) => {
  const { request } = event;
  if (request.method !== 'GET') return;
  const url = new URL(request.url);
  if (url.origin === self.location.origin) {
    event.respondWith(fromAppCache(request));
    return;
  }
  if (url.origin === 'https://www.gstatic.com' && url.pathname.startsWith(`/firebasejs/${SDK_VERSION}/`)) {
    event.respondWith(fromSdkCache(request));
  }
  // Firestore istekleri ve diğer her şey araya girilmeden ağa gider. Kişisel veri asla Cache API'ye konmaz.
});

self.addEventListener('message', (event) => {
  const data = event.data || {};
  if (data.type === 'SKIP_WAITING') self.skipWaiting();
  if (data.type === 'GET_VERSION' && event.ports && event.ports[0]) {
    event.ports[0].postMessage({ version: VERSION, assetCount: APP_ASSETS.length });
  }
});
