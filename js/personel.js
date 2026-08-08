// ── MERKEZ PERSONEL MODÜLÜ
// Tüm modüller window.PERSONEL ve window.personelData'yı kullanır.
// Sadece bu dosya Firebase'e yazar. Ana sayfa bu grid'i render eder.

window.PERSONEL     = [];
window.personelData = {};

var _pdb; // Firebase referansı

var ALANLAR_PERSONEL = [
  { id: "tuvalet", label: "🚽 Tuvalet" },
  { id: "banyo",   label: "🚿 Banyo"   },
  { id: "cevre",   label: "🌳 Çevre"   },
  { id: "oda1",    label: "🛏️ 1. Oda"  },
  { id: "oda2",    label: "🛏️ 2. Oda"  },
  { id: "yazhane", label: "📋 Yazhane" },
];

// Callback listesi — personel değişince bildir
var _personelCallbacks = [];
window.onPersonelGuncelle = function(cb) { _personelCallbacks.push(cb); };
function _personelBildir() { _personelCallbacks.forEach(function(cb) { try { cb(); } catch(e) {} }); }

// ── YÜKLE ──────────────────────────────────────────────────
window.onFirebaseReady(function() {
  _pdb = window.__db;
  personelYukle();
});

async function personelYukle() {
  // 1) Cache'den hızlı göster
  var cached = window.cacheOku("kys_personel");
  if (cached) {
    window.PERSONEL     = cached.PERSONEL     || [];
    window.personelData = cached.personelData || {};
    renderPersonelGrid();
  }

  try {
    var bugun = new Date().toISOString().split("T")[0];

    // İzin sıfırlama (yeni gün)
    var sifirSnap = await _pdb.collection("kys_meta").doc("izin_sifir").get();
    var sonSifir  = sifirSnap.exists ? sifirSnap.data().tarih : null;
    if (sonSifir !== bugun) {
      var tpSnap = await _pdb.collection("kys_personel").get();
      var batch  = _pdb.batch();
      tpSnap.forEach(function(s) {
        if (s.data().izinli) batch.update(_pdb.collection("kys_personel").doc(s.id), { izinli: false });
      });
      await batch.commit();
      await _pdb.collection("kys_meta").doc("izin_sifir").set({ tarih: bugun });
    }

    // Tüm personeli çek
    var snap = await _pdb.collection("kys_personel").get();
    if (!snap.empty) {
      window.PERSONEL     = [];
      window.personelData = {};
      snap.forEach(function(s) {
        var d = s.data();
        window.PERSONEL.push({ id: s.id, isim: d.isim, sabit: d.sabit || null, odaDongu: !!d.odaDongu });
        window.personelData[s.id] = d;
      });
    } else {
      // İlk kurulum — varsayılan liste
      var varsayilan = [
        { id:"cuma",    isim:"Cuma",    sabit:null,        odaDongu:false },
        { id:"mustafa", isim:"Mustafa", sabit:null,        odaDongu:false },
        { id:"ahmet",   isim:"Ahmet",   sabit:"oda1",      odaDongu:false },
        { id:"mertali", isim:"Mertali", sabit:"yazhane",   odaDongu:false },
        { id:"hasan",   isim:"Hasan",   sabit:null,        odaDongu:false },
        { id:"huseyin", isim:"Hüseyin", sabit:null,        odaDongu:false },
        { id:"mert",    isim:"Mert",    sabit:null,        odaDongu:false },
        { id:"taner",   isim:"Taner",   sabit:null,        odaDongu:true  },
        { id:"yusuf",   isim:"Yusuf",   sabit:null,        odaDongu:true  },
        { id:"samet",   isim:"Samet",   sabit:null,        odaDongu:true  },
        { id:"ali",     isim:"Ali",     sabit:null,        odaDongu:false },
      ];
      for (var i = 0; i < varsayilan.length; i++) {
        var p = varsayilan[i];
        var v = Object.assign({}, p, {
          izinli: false,
          sayaclar: { tuvalet:0, banyo:0, cevre:0, oda1:0, oda2:0, yazhane:0 },
          isSayac: 0, puan: 0,
        });
        await _pdb.collection("kys_personel").doc(p.id).set(v);
        window.personelData[p.id] = v;
      }
      window.PERSONEL = varsayilan;
    }

    _cacheKaydet();
  } catch(e) {}

  renderPersonelGrid();
  _personelBildir();
}

function _cacheKaydet() {
  window.cacheYaz("kys_personel", { PERSONEL: window.PERSONEL, personelData: window.personelData });
}

// ── GRID RENDER ────────────────────────────────────────────
function renderPersonelGrid() {
  var grid = document.getElementById("kys-personel-grid");
  if (!grid) return;
  grid.innerHTML = "";

  window.PERSONEL.forEach(function(p) {
    var pd = window.personelData[p.id] || p;
    var sabitAlan = pd.sabit ? ALANLAR_PERSONEL.find(function(a) { return a.id === pd.sabit; }) : null;

    var wrap = document.createElement("div");
    wrap.className = "personel-wrap";

    var btn = document.createElement("button");
    btn.className = "personel-btn" + (pd.izinli ? " yok" : "") + (pd.sabit ? " sabit-gorevli" : "");
    btn.innerHTML =
      '<div class="p-avatar">' + p.isim[0] + '</div>' +
      '<span class="p-isim">' + p.isim + '</span>' +
      (pd.sabit ? '<span class="p-sabit-badge">' + (sabitAlan ? sabitAlan.label.replace(/^[^\s]+\s/, "").split(" ")[0] : pd.sabit) + '</span>' : '') +
      (pd.izinli ? '<span class="p-yok-badge">YOK</span>' : '') +
      '<span class="p-ayar-btn">⚙️</span>';

    // Ana menü
    var menu = document.createElement("div");
    menu.className = "p-menu";
    menu.style.display = "none";
    menu.innerHTML =
      '<div class="p-menu-baslik">' + p.isim + '</div>' +
      '<button class="p-menu-item" data-action="izin">' + (pd.izinli ? '✅ Bugün Var' : '🏠 Bugün Yok') + '</button>' +
      '<button class="p-menu-item" data-action="gorev">📋 Sabit Görev ▸</button>' +
      '<button class="p-menu-item" data-action="dongu">' + (pd.odaDongu ? '✅ Oda2 Döngüsünde' : '🔄 Oda2 Döngüsüne Ekle') + '</button>' +
      '<button class="p-menu-item p-menu-sil" data-action="sil">🗑️ Sil</button>';

    // Sabit görev alt menüsü
    var gorevMenu = document.createElement("div");
    gorevMenu.className = "p-gorev-menu";
    gorevMenu.style.display = "none";
    [{ id: null, label: "❌ Sabit Görev Yok" }].concat(ALANLAR_PERSONEL).forEach(function(g) {
      var gb = document.createElement("button");
      gb.className = "p-menu-item" + (pd.sabit === g.id ? " secili" : "");
      gb.textContent = g.label;
      gb.addEventListener("click", function(e) {
        e.stopPropagation();
        pSabitGorevAta(p.id, g.id);
        menu.style.display = "none";
        gorevMenu.style.display = "none";
      });
      gorevMenu.appendChild(gb);
    });

    // Menü aksiyonları
    menu.querySelectorAll(".p-menu-item").forEach(function(item) {
      item.addEventListener("click", function(e) {
        e.stopPropagation();
        var action = item.dataset.action;
        if      (action === "izin")  { pToggleIzin(p.id); menu.style.display = "none"; }
        else if (action === "gorev") { gorevMenu.style.display = gorevMenu.style.display === "none" ? "" : "none"; }
        else if (action === "dongu") { pToggleOdaDongu(p.id); menu.style.display = "none"; }
        else if (action === "sil")   { pPersonelCikar(p.id); menu.style.display = "none"; }
      });
    });

    btn.querySelector(".p-ayar-btn").addEventListener("click", function(e) {
      e.stopPropagation();
      var acik = menu.style.display !== "none";
      document.querySelectorAll(".p-menu, .p-gorev-menu").forEach(function(m) { m.style.display = "none"; });
      if (!acik) menu.style.display = "";
    });

    wrap.appendChild(btn);
    wrap.appendChild(menu);
    wrap.appendChild(gorevMenu);
    grid.appendChild(wrap);
  });

  // + Ekle butonu
  var ekleWrap = document.createElement("div");
  ekleWrap.className = "personel-wrap";
  var ekleBtn = document.createElement("button");
  ekleBtn.className = "personel-btn personel-ekle-btn";
  ekleBtn.innerHTML = '<div class="p-avatar" style="font-size:20px;color:var(--accent)">+</div><span>Ekle</span>';
  ekleBtn.addEventListener("click", function() {
    var form = document.getElementById("personel-ekle-form");
    if (!form) return;
    form.style.display = form.style.display === "none" ? "" : "none";
    if (form.style.display !== "none") {
      var inp = document.getElementById("personel-isim-inp");
      if (inp) inp.focus();
    }
  });
  ekleWrap.appendChild(ekleBtn);
  grid.appendChild(ekleWrap);

  // Sayfa tıklamasında menüleri kapat
  document.addEventListener("click", function() {
    document.querySelectorAll(".p-menu, .p-gorev-menu").forEach(function(m) { m.style.display = "none"; });
  }, { once: false });
}

// ── PERSONEL İŞLEMLERİ ────────────────────────────────────
async function pSabitGorevAta(id, gorev) {
  var pd = window.personelData[id]; if (!pd) return;
  var pp = window.PERSONEL.find(function(p) { return p.id === id; });
  pd.sabit = gorev;
  if (pp) pp.sabit = gorev;
  try { await _pdb.collection("kys_personel").doc(id).update({ sabit: gorev }); } catch(e) {}
  _cacheKaydet();
  renderPersonelGrid();
  _personelBildir();
  showToast(pd.isim + (gorev ? " → sabit görev atandı ✅" : " → sabit görev kaldırıldı"), "success");
}

async function pToggleOdaDongu(id) {
  var pd = window.personelData[id];
  var pp = window.PERSONEL.find(function(p) { return p.id === id; });
  if (!pd || !pp) return;
  var yeni = !pd.odaDongu;
  pd.odaDongu = yeni; pp.odaDongu = yeni;
  try { await _pdb.collection("kys_personel").doc(id).update({ odaDongu: yeni }); } catch(e) {}
  _cacheKaydet();
  renderPersonelGrid();
  _personelBildir();
  showToast(pd.isim + (yeni ? " Oda2 döngüsüne eklendi" : " döngüden çıkarıldı"), "success");
}

async function pPersonelEkle(isim) {
  var id = isim.toLowerCase()
    .replace(/\s/g,"_").replace(/ş/g,"s").replace(/ç/g,"c")
    .replace(/ğ/g,"g").replace(/ü/g,"u").replace(/ö/g,"o").replace(/ı/g,"i")
    + "_" + Date.now();
  var yeni = { id:id, isim:isim, sabit:null, odaDongu:false, izinli:false,
    sayaclar:{ tuvalet:0, banyo:0, cevre:0, oda1:0, oda2:0, yazhane:0 }, isSayac:0, puan:0 };
  try { await _pdb.collection("kys_personel").doc(id).set(yeni); } catch(e) {}
  window.personelData[id] = yeni;
  window.PERSONEL.push({ id:id, isim:isim, sabit:null, odaDongu:false });
  _cacheKaydet();
  renderPersonelGrid();
  _personelBildir();
  showToast(isim + " eklendi ✅", "success");
}

async function pPersonelCikar(id) {
  var pd = window.personelData[id]; if (!pd) return;
  var isim = pd.isim;
  try { await _pdb.collection("kys_personel").doc(id).delete(); } catch(e) {}
  delete window.personelData[id];
  var idx = window.PERSONEL.findIndex(function(p) { return p.id === id; });
  if (idx >= 0) window.PERSONEL.splice(idx, 1);
  _cacheKaydet();
  renderPersonelGrid();
  _personelBildir();
  showToast(isim + " listeden çıkarıldı.", "");
}

async function pToggleIzin(id) {
  var pd = window.personelData[id]; if (!pd) return;
  pd.izinli = !pd.izinli;
  try { await _pdb.collection("kys_personel").doc(id).update({ izinli: pd.izinli }); } catch(e) {}
  _cacheKaydet();
  renderPersonelGrid();
  _personelBildir();
  showToast(pd.isim + (pd.izinli ? " → Yok ❌" : " → Var ✅"));
}

// ── FORM DİNLE (ana sayfadaki ekle formu) ─────────────────
window.addEventListener("load", function() {
  var kaydetBtn = document.getElementById("btn-personel-kaydet");
  var iptalBtn  = document.getElementById("btn-personel-iptal");
  var inp       = document.getElementById("personel-isim-inp");

  if (kaydetBtn) {
    kaydetBtn.addEventListener("click", function() {
      var isim = (inp.value || "").trim();
      if (!isim) { showToast("İsim gir!", "error"); return; }
      pPersonelEkle(isim);
      inp.value = "";
      document.getElementById("personel-ekle-form").style.display = "none";
    });
  }
  if (iptalBtn) {
    iptalBtn.addEventListener("click", function() {
      document.getElementById("personel-ekle-form").style.display = "none";
      if (inp) inp.value = "";
    });
  }
  if (inp) {
    inp.addEventListener("keydown", function(e) {
      if (e.key === "Enter") kaydetBtn && kaydetBtn.click();
    });
  }
});
