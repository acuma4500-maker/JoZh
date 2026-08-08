// ── TEMA (Açık/Koyu)
(function() {
  var kayitli = null;
  try { kayitli = localStorage.getItem("tema"); } catch(e) {}
  if (kayitli === "acik") document.body.classList.add("tema-acik");

  window.addEventListener("load", function() {
    var btn = document.getElementById("btn-tema");
    if (!btn) return;
    btn.textContent = document.body.classList.contains("tema-acik") ? "☀️" : "🌙";
    btn.addEventListener("click", function() {
      document.body.classList.toggle("tema-acik");
      var acik = document.body.classList.contains("tema-acik");
      btn.textContent = acik ? "☀️" : "🌙";
      try { localStorage.setItem("tema", acik ? "acik" : "koyu"); } catch(e) {}
    });
  });
})();

// ── OFFLINE YEDEK
window.cacheYaz = function(anahtar, veri) {
  try { localStorage.setItem("cache_" + anahtar, JSON.stringify(veri)); } catch(e) {}
};
window.cacheOku = function(anahtar) {
  try {
    var v = localStorage.getItem("cache_" + anahtar);
    return v ? JSON.parse(v) : null;
  } catch(e) { return null; }
};

// ── TAB NAVİGASYON
document.querySelectorAll(".bnav-tab").forEach(function(tab) {
  tab.addEventListener("click", function() {
    gotoPage(tab.dataset.tab);
  });
});

window.gotoPage = function(target) {
  document.querySelectorAll(".page").forEach(function(p) { p.classList.remove("active"); });
  var page = document.getElementById("page-" + target);
  if (page) page.classList.add("active");

  // Nav highlight — dahası altındaki sayfalar dahası'yı aktif yapar
  var navTarget = target;
  if (target === "mulakat" || target === "rehber" || target === "cuzdan") navTarget = "dahasi";

  document.querySelectorAll(".bnav-tab").forEach(function(t) {
    t.classList.toggle("active", t.dataset.tab === navTarget);
  });

  window.scrollTo(0, 0);

  // Ana sayfaya her gidişte widget'ları yenile
  if (target === "ana") {
    if (typeof window.anaRefresh === "function") {
      setTimeout(window.anaRefresh, 50);
    }
  }
};

document.querySelectorAll(".dahasi-kart").forEach(function(kart) {
  kart.addEventListener("click", function() { gotoPage(kart.dataset.goto); });
});

document.querySelectorAll(".dahasi-geri").forEach(function(btn) {
  btn.addEventListener("click", function() { gotoPage(btn.dataset.back); });
});

// ── TOAST (sağ üst)
window.showToast = function(msg, type) {
  var el = document.getElementById("toast");
  // Öncekini hemen kapat, kısa bekle sonra yeniyi göster
  el.classList.remove("show");
  clearTimeout(window._toastTimer);
  window._toastTimer2 = setTimeout(function() {
    el.textContent = msg;
    el.className = "toast" + (type ? " " + type : "");
    el.classList.add("show");
    window._toastTimer = setTimeout(function() {
      el.classList.remove("show");
    }, 3000);
  }, el.classList.contains("show") ? 150 : 0);
};

// ── FIREBASE READY
window.onFirebaseReady = function(cb) {
  if (window.__firebaseReady) { cb(); }
  else { window.addEventListener("firebase-ready", cb); }
};

// ── Başlangıçta ana sayfayı yükle
window.addEventListener("load", function() {
  // Ana sekmeyi aktif yap
  document.querySelectorAll(".bnav-tab").forEach(function(t) {
    t.classList.toggle("active", t.dataset.tab === "ana");
  });
  // Ana widget'ları kısa gecikmeyle yükle (diğer modüller yüklensin)
  setTimeout(function() {
    if (typeof window.anaRefresh === "function") window.anaRefresh();
  }, 600);
});
