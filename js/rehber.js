// ── REHBER v2
// FİX: Favori/öne çıkar özelliği eklendi
// FİX: Numara formatı iyileştirildi

var db;
var kisiler = [];

var KATEGORILER = [
  { id: "acil",  label: "🚨 Acil",     renk: "#e74c3c" },
  { id: "asker", label: "🎖️ Askeri",  renk: "#4f8ef7" },
  { id: "aile",  label: "👨‍👩‍👧 Aile",  renk: "#2ecc71" },
  { id: "diger", label: "📇 Diğer",   renk: "#8891aa" },
];

window.onFirebaseReady(function() {
  db = window.__db;
  rehberYukle();
});

async function rehberYukle() {
  var cached = window.cacheOku("rehber");
  if (cached) { kisiler = cached; rehberRender(); }

  try {
    var snap = await db.collection("rehber_kayitlar").get();
    kisiler = [];
    snap.forEach(function(s) { kisiler.push(Object.assign({ id: s.id }, s.data())); });
    // Favoriler önce, sonra oluşturulma sırası
    kisiler.sort(function(a,b) {
      if (b.favori && !a.favori) return 1;
      if (a.favori && !b.favori) return -1;
      return (a.olusturuldu||0) - (b.olusturuldu||0);
    });
    window.cacheYaz("rehber", kisiler);
  } catch(e) {}
  rehberRender();
}

function rehberRender() {
  var el = document.getElementById("rehber-icerik");
  if (!el) return;

  el.innerHTML =
    '<div class="btn-row" style="margin-bottom:12px">' +
      '<button class="btn btn-primary" id="btn-rehber-ekle">➕ Numara Ekle</button>' +
    '</div>' +
    '<div class="rehber-arama-wrap">' +
      '<span class="rehber-arama-icon">🔍</span>' +
      '<input class="inp rehber-arama" id="rehber-arama" type="text" placeholder="İsim veya numara ara..." />' +
    '</div>' +
    '<div class="card" id="rehber-form" style="display:none">' +
      '<div class="card-head"><span class="card-icon">📞</span><h2>Yeni Numara</h2></div>' +
      '<div class="form-group"><label>İsim / Kişi</label><input class="inp" id="rehber-isim" type="text" placeholder="Bölük Komutanı" maxlength="30"/></div>' +
      '<div class="form-group"><label>Numara</label><input class="inp" id="rehber-numara" type="tel" placeholder="0555 555 55 55" maxlength="20"/></div>' +
      '<div class="form-group"><label>Kategori</label><div class="btn-row" id="rehber-kat-btns">' +
        KATEGORILER.map(function(k) {
          return '<button class="btn btn-outline rehber-kat-btn" data-kat="' + k.id + '">' + k.label + '</button>';
        }).join("") +
      '</div></div>' +
      '<div class="form-group">' +
        '<label style="display:flex;align-items:center;gap:8px">' +
          '<input type="checkbox" id="rehber-favori" style="width:18px;height:18px;cursor:pointer"> ' +
          '⭐ Favori (Acil Erişim)' +
        '</label>' +
      '</div>' +
      '<div class="btn-row"><button class="btn btn-primary" id="btn-rehber-kaydet">💾 Kaydet</button>' +
        '<button class="btn btn-ghost" id="btn-rehber-iptal">İptal</button></div>' +
    '</div>' +
    '<div id="rehber-liste"></div>';

  rehberListeRender();
  rehberDinle();
}

function rehberListeRender() {
  var liste = document.getElementById("rehber-liste");
  if (!liste) return;

  var arama = "";
  var aramaEl = document.getElementById("rehber-arama");
  if (aramaEl) arama = (aramaEl.value || "").toLowerCase().trim();

  var gosterilecek = kisiler;
  if (arama) {
    gosterilecek = kisiler.filter(function(k) {
      return (k.isim || "").toLowerCase().indexOf(arama) >= 0 ||
             (k.numara || "").indexOf(arama) >= 0;
    });
  }

  if (!gosterilecek.length) {
    liste.innerHTML = '<p class="empty-text">' + (arama ? "Sonuç bulunamadı." : "Henüz numara eklenmedi.") + '</p>';
    return;
  }

  liste.innerHTML = "";

  // Favoriler bloku
  var favoriler = gosterilecek.filter(function(k) { return k.favori; });
  if (favoriler.length) {
    var favBaslik = document.createElement("div");
    favBaslik.className = "rehber-grup-baslik";
    favBaslik.innerHTML = '⭐ Favoriler <span style="color:var(--text3)">(' + favoriler.length + ')</span>';
    liste.appendChild(favBaslik);
    favoriler.forEach(function(k) {
      var idx = kisiler.indexOf(k);
      liste.appendChild(rehberItemOlustur(k, idx));
    });
  }

  // Kategoriye göre grupla
  KATEGORILER.forEach(function(kat) {
    var grup = gosterilecek.filter(function(k) {
      return (k.kategori || "diger") === kat.id && !k.favori;
    });
    if (!grup.length) return;

    var baslik = document.createElement("div");
    baslik.className = "rehber-grup-baslik";
    baslik.innerHTML = kat.label + ' <span style="color:var(--text3)">(' + grup.length + ')</span>';
    liste.appendChild(baslik);

    grup.forEach(function(k) {
      var idx = kisiler.indexOf(k);
      liste.appendChild(rehberItemOlustur(k, idx));
    });
  });
}

function rehberItemOlustur(k, idx) {
  var kat = KATEGORILER.find(function(x) { return x.id === (k.kategori || "diger"); }) || KATEGORILER[KATEGORILER.length-1];
  var div = document.createElement("div");
  div.className = "rehber-item";
  div.style.borderLeftColor = k.favori ? "#f39c12" : kat.renk;
  div.innerHTML =
    '<div class="rehber-sol">' +
      '<div class="rehber-isim">' + escHTMLr(k.isim) + (k.favori ? ' ⭐' : '') + '</div>' +
      '<div class="rehber-numara">' + escHTMLr(k.numara) + '</div>' +
    '</div>' +
    '<div class="rehber-sag">' +
      '<button class="rehber-fav" title="' + (k.favori ? "Favoriden çıkar" : "Favoriye ekle") + '" data-i="' + idx + '">' + (k.favori ? "⭐" : "☆") + '</button>' +
      '<a href="tel:' + (k.numara||"").replace(/\s/g,"") + '" class="rehber-ara">📞</a>' +
      '<button class="rehber-sil" data-i="' + idx + '">🗑️</button>' +
    '</div>';

  div.querySelector(".rehber-fav").addEventListener("click", function() { rehberFavoriToggle(idx); });
  div.querySelector(".rehber-sil").addEventListener("click", function() { rehberSil(idx); });
  return div;
}

function rehberDinle() {
  document.getElementById("btn-rehber-ekle").addEventListener("click", function() {
    var f = document.getElementById("rehber-form");
    f.style.display = f.style.display === "none" ? "" : "none";
  });

  var aramaEl = document.getElementById("rehber-arama");
  if (aramaEl) aramaEl.addEventListener("input", function() { rehberListeRender(); });

  document.getElementById("btn-rehber-kaydet").addEventListener("click", rehberKaydet);
  document.getElementById("btn-rehber-iptal").addEventListener("click", function() {
    document.getElementById("rehber-form").style.display = "none";
  });
  document.querySelectorAll(".rehber-kat-btn").forEach(function(btn) {
    btn.addEventListener("click", function() {
      document.querySelectorAll(".rehber-kat-btn").forEach(function(b) { b.classList.remove("selected"); });
      btn.classList.add("selected");
    });
  });

  var numInp = document.getElementById("rehber-numara");
  numInp.addEventListener("input", function() {
    var v = numInp.value.replace(/\D/g,"").slice(0,11);
    var f = "";
    if (v.length > 0) f = v.slice(0,4);
    if (v.length > 4) f += " " + v.slice(4,7);
    if (v.length > 7) f += " " + v.slice(7,9);
    if (v.length > 9) f += " " + v.slice(9,11);
    numInp.value = f;
  });
}

async function rehberKaydet() {
  var isim   = (document.getElementById("rehber-isim").value || "").trim();
  var numara = (document.getElementById("rehber-numara").value || "").trim();
  var katBtn = document.querySelector(".rehber-kat-btn.selected");
  var favori = document.getElementById("rehber-favori").checked;
  if (!isim)   { showToast("İsim gir!", "error"); return; }
  if (!numara) { showToast("Numara gir!", "error"); return; }
  var yeni = {
    isim: isim, numara: numara,
    kategori: katBtn ? katBtn.dataset.kat : "diger",
    favori: favori,
    olusturuldu: Date.now()
  };
  try {
    var ref = await db.collection("rehber_kayitlar").add(yeni);
    kisiler.push(Object.assign({ id: ref.id }, yeni));
    // Sırayı koru
    kisiler.sort(function(a,b) {
      if (b.favori && !a.favori) return 1;
      if (a.favori && !b.favori) return -1;
      return (a.olusturuldu||0) - (b.olusturuldu||0);
    });
    window.cacheYaz("rehber", kisiler);
  } catch(e) {}
  rehberRender();
  showToast("📞 Numara eklendi!", "success");
}

async function rehberFavoriToggle(i) {
  var k = kisiler[i];
  k.favori = !k.favori;
  try { await db.collection("rehber_kayitlar").doc(k.id).update({ favori: k.favori }); } catch(e) {}
  kisiler.sort(function(a,b) {
    if (b.favori && !a.favori) return 1;
    if (a.favori && !b.favori) return -1;
    return (a.olusturuldu||0) - (b.olusturuldu||0);
  });
  window.cacheYaz("rehber", kisiler);
  rehberListeRender();
  showToast(k.favori ? "⭐ Favoriye eklendi" : "Favoriden çıkarıldı");
}

async function rehberSil(i) {
  var k = kisiler[i];
  if (!confirm(k.isim + " silinsin mi?")) return;
  try { await db.collection("rehber_kayitlar").doc(k.id).delete(); } catch(e) {}
  kisiler.splice(i, 1);
  window.cacheYaz("rehber", kisiler);
  rehberRender();
  showToast("Numara silindi.");
}

function escHTMLr(s) {
  return (s||"").replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;");
}
