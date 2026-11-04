// ── SERVICE WORKER v2 — Offline destek
var CACHE = "jozh-v2";
var DOSYALAR = [
  "./index.html",
  "./css/style.css",
  "./js/app.js",
  "./js/kys.js",
  "./js/spor.js",
  "./js/mulakat.js",
  "./js/cuzdan.js",
  "./js/nobet.js",
  "./js/rehber.js",
  "./manifest.json"
];

self.addEventListener("install", function(e) {
  e.waitUntil(
    caches.open(CACHE).then(function(c) { return c.addAll(DOSYALAR); })
  );
  self.skipWaiting();
});

self.addEventListener("activate", function(e) {
  e.waitUntil(
    caches.keys().then(function(keys) {
      return Promise.all(keys.map(function(k) {
        if (k !== CACHE) return caches.delete(k);
      }));
    })
  );
  self.clients.claim();
});

self.addEventListener("fetch", function(e) {
  var url = e.request.url;
  if (url.indexOf("firestore") >= 0 || url.indexOf("googleapis") >= 0 || url.indexOf("gstatic") >= 0 || url.indexOf("tenor") >= 0) {
    return;
  }
  e.respondWith(
    caches.match(e.request).then(function(cevap) {
      return cevap || fetch(e.request);
    })
  );
});
