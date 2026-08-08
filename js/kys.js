// ── KYS — Kışla Yönetim Sistemi v3
// Personel yönetimi personel.js'e taşındı.
// Bu dosya sadece temizlik & iş dağıtımı yapar.

var ALANLAR = [
  { id: "tuvalet", label: "🚽 Tuvalet",  kisi: 3, agirlik: 5 },
  { id: "banyo",   label: "🚿 Banyo",    kisi: 1, agirlik: 4 },
  { id: "cevre",   label: "🌳 Çevre",    kisi: 2, agirlik: 3 },
  { id: "oda1",    label: "🛏️ 1. Oda",   kisi: 1, agirlik: 2 },
  { id: "oda2",    label: "🛏️ 2. Oda",   kisi: 1, agirlik: 2 },
  { id: "yazhane", label: "📋 Yazhane",  kisi: 1, agirlik: 1 },
];

var _kysdb;
var gunlukData = null;
var isTuruData = { secilen: [], kalan: [] };

function bugunStr() { return new Date().toISOString().split("T")[0]; }
function formatTarih(str) {
  if (!str) return "";
  var p = str.split("-");
  return p[2] + "." + p[1] + "." + p[0];
}

window.onFirebaseReady(function() {
  _kysdb = window.__db;
  // personel.js yüklenince başla, yoksa doğrudan başla
  if (window.PERSONEL && window.PERSONEL.length) {
    kysYukle();
  } else {
    window.onPersonelGuncelle(function() {
      if (!_kysBasladi) { _kysBasladi = true; kysYukle(); }
    });
    // 1.5sn sonra yine de başlat (güvenlik)
    setTimeout(function() { if (!_kysBasladi) { _kysBasladi = true; kysYukle(); } }, 1500);
  }
});
var _kysBasladi = false;

async function kysYukle() {
  // Günlük cache
  var cachedG = window.cacheOku("kys_gunluk_" + bugunStr());
  if (cachedG) { gunlukData = cachedG; }

  try {
    // İş turu
    var turSnap = await _kysdb.collection("kys_is_turu").doc("tur").get();
    if (turSnap.exists) {
      isTuruData = turSnap.data();
    } else {
      isTuruData = { secilen: [], kalan: window.PERSONEL.map(function(p) { return p.id; }) };
      await _kysdb.collection("kys_is_turu").doc("tur").set(isTuruData);
    }

    // Bugünün listesi
    var gunSnap = await _kysdb.collection("kys_gunluk").doc(bugunStr()).get();
    if (gunSnap.exists) gunlukData = gunSnap.data();
    if (gunlukData) window.cacheYaz("kys_gunluk_" + bugunStr(), gunlukData);
  } catch(e) {}

  if (gunlukData) renderGunlukListe();
  actualizarYenidenBtn();
  dinleButonlar();
}

function actualizarYenidenBtn() {
  var yBtn = document.getElementById("btn-temizlik-yeniden");
  if (!yBtn) return;
  yBtn.style.display = (gunlukData && gunlukData.tarih === bugunStr()) ? "" : "none";
}

// ── TEMİZLİK LİSTESİ ──────────────────────────────────────
async function temizlikListesiYap() {
  var bugun = new Date().toISOString().split("T")[0];
  var PERSONEL     = window.PERSONEL;
  var personelData = window.personelData;

  // personelData'yı tek kaynak olarak kullan — PERSONEL array'indeki sabit alanı değil
  // Önce personelData'dan güncel sabit/odaDongu bilgisini PERSONEL'e yansıt
  PERSONEL.forEach(function(p) {
    var pd = personelData[p.id];
    if (pd) {
      p.sabit    = pd.sabit    !== undefined ? pd.sabit    : p.sabit;
      p.odaDongu = pd.odaDongu !== undefined ? pd.odaDongu : p.odaDongu;
    }
  });

  var aktifler = PERSONEL.filter(function(p) { return !personelData[p.id] || !personelData[p.id].izinli; });

  var atananlar = {};
  var sonuc = {};

  // Sabit görevler — personelData'dan oku
  PERSONEL.forEach(function(p) {
    var pd = personelData[p.id];
    if (pd && pd.sabit && !pd.izinli) {
      if (!sonuc[pd.sabit]) sonuc[pd.sabit] = [];
      sonuc[pd.sabit].push(p.id);
      atananlar[p.id] = true;
    }
  });

  // 2. Oda döngüsü — personelData'dan odaDongu oku
  if (!sonuc["oda2"]) {
    var oda2Havuz = PERSONEL.filter(function(p) {
      var pd = personelData[p.id];
      return pd ? !!pd.odaDongu : !!p.odaDongu;
    });
    if (oda2Havuz.length) {
      var siraSnap = await _kysdb.collection("kys_gunluk").doc("oda2_sira").get();
      var oda2Idx  = siraSnap.exists ? (siraSnap.data().idx || 0) : 0;
      var oda2Kisi = null;
      for (var d = 0; d < oda2Havuz.length; d++) {
        var aday = oda2Havuz[oda2Idx % oda2Havuz.length];
        if (!personelData[aday.id] || !personelData[aday.id].izinli) { oda2Kisi = aday.id; break; }
        oda2Idx++;
      }
      try { await _kysdb.collection("kys_gunluk").doc("oda2_sira").set({ idx: (oda2Idx + 1) % oda2Havuz.length }); } catch(e) {}
      if (oda2Kisi) { sonuc["oda2"] = [oda2Kisi]; atananlar[oda2Kisi] = true; }
    }
  }

  // Serbest havuz — sabit/oda2 atananlar hariç, puana göre sırala
  var serbest = aktifler
    .filter(function(p) { return !atananlar[p.id]; })
    .sort(function(a, b) {
      return ((personelData[a.id] && personelData[a.id].puan) || 0) - ((personelData[b.id] && personelData[b.id].puan) || 0);
    });

  // Sabit görev atanmamış alanlar için serbest havuzdan kişi al
  // Önce sabit görevsiz oda1, oda2 (döngü dışı), yazhane
  ["oda1", "oda2", "yazhane"].forEach(function(alan) {
    if (!sonuc[alan] || !sonuc[alan].length) {
      var yedek = serbest.shift();
      if (yedek) { sonuc[alan] = [yedek.id]; atananlar[yedek.id] = true; }
    }
  });

  // Sabit görev atanmamışsa tuvalet (3 kişi), banyo (1 kişi)
  if (!sonuc["tuvalet"] || !sonuc["tuvalet"].length) {
    sonuc["tuvalet"] = serbest.splice(0, 3).map(function(p) { return p.id; });
  } else {
    // Sabit görevden geldiyse serbest havuzdan ek kişi alma
    // Tuvalet 3 kişi lazım — eksik varsa tamamla
    var ekEksik = 3 - sonuc["tuvalet"].length;
    for (var ei = 0; ei < ekEksik; ei++) {
      var ek = serbest.shift();
      if (ek) sonuc["tuvalet"].push(ek.id);
    }
  }

  if (!sonuc["banyo"] || !sonuc["banyo"].length) {
    var banyoKisi = serbest.shift();
    if (banyoKisi) sonuc["banyo"] = [banyoKisi.id];
  }

  // Geri kalanların tamamı çevreye
  if (!sonuc["cevre"] || !sonuc["cevre"].length) {
    sonuc["cevre"] = serbest.map(function(p) { return p.id; });
  } else {
    // Sabit görevden geldiyse kalanları ekle
    serbest.forEach(function(p) { sonuc["cevre"].push(p.id); });
  }

  var kayit = { tarih: bugun, liste: sonuc, olusturuldu: Date.now() };
  try { await _kysdb.collection("kys_gunluk").doc(bugun).set(kayit); } catch(e) {}
  gunlukData = kayit;
  window.cacheYaz("kys_gunluk_" + bugun, kayit);

  // Sayaçları güncelle
  for (var alan in sonuc) {
    var kisiler = sonuc[alan];
    var agirlik = 1;
    for (var ai = 0; ai < ALANLAR.length; ai++) {
      if (ALANLAR[ai].id === alan) { agirlik = ALANLAR[ai].agirlik; break; }
    }
    for (var ki = 0; ki < kisiler.length; ki++) {
      var kid = kisiler[ki];
      var pd  = personelData[kid]; if (!pd) continue;
      pd.sayaclar = pd.sayaclar || {};
      pd.sayaclar[alan] = (pd.sayaclar[alan] || 0) + 1;
      pd.puan = (pd.puan || 0) + agirlik;
      var guncelle = { puan: pd.puan }; guncelle["sayaclar." + alan] = pd.sayaclar[alan];
      try { await _kysdb.collection("kys_personel").doc(kid).update(guncelle); } catch(e) {}
    }
  }
  window.cacheYaz("kys_personel", { PERSONEL: PERSONEL, personelData: personelData });
  renderGunlukListe();
  actualizarYenidenBtn();
  showToast("✅ Temizlik listesi oluşturuldu!", "success");
  actualizarYenidenBtn();
}

async function temizlikListesiYapZorla() {
  var personelData = window.personelData;
  if (gunlukData && gunlukData.tarih === bugunStr() && gunlukData.liste) {
    for (var alan in gunlukData.liste) {
      var kisiler = gunlukData.liste[alan];
      var agirlik = 1;
      for (var ai = 0; ai < ALANLAR.length; ai++) {
        if (ALANLAR[ai].id === alan) { agirlik = ALANLAR[ai].agirlik; break; }
      }
      for (var ki = 0; ki < kisiler.length; ki++) {
        var kid = kisiler[ki]; var pd = personelData[kid]; if (!pd) continue;
        pd.sayaclar = pd.sayaclar || {};
        pd.sayaclar[alan] = Math.max(0, (pd.sayaclar[alan] || 0) - 1);
        pd.puan = Math.max(0, (pd.puan || 0) - agirlik);
        var geri = { puan: pd.puan }; geri["sayaclar." + alan] = pd.sayaclar[alan];
        try { await _kysdb.collection("kys_personel").doc(kid).update(geri); } catch(e) {}
      }
    }
  }
  gunlukData = null;
  await temizlikListesiYap();
}

// ── RENDER ────────────────────────────────────────────────
function renderGunlukListe() {
  if (!gunlukData) return;
  var kart = document.getElementById("kys-liste-card");
  if (!kart) return;
  kart.style.display = "";
  document.getElementById("kys-tarih").textContent = formatTarih(gunlukData.tarih);

  var el = document.getElementById("kys-liste-content");
  el.innerHTML = "";

  var pngBtn = document.createElement("button");
  pngBtn.className = "btn btn-secondary btn-sm kys-png-btn";
  pngBtn.innerHTML = "🖼️ Resim İndir";
  pngBtn.style.marginBottom = "12px";
  pngBtn.addEventListener("click", kysPngIndir);
  el.appendChild(pngBtn);

  var listeDiv = document.createElement("div");
  listeDiv.id = "kys-liste-satirlar";
  el.appendChild(listeDiv);

  var PERSONEL     = window.PERSONEL;
  var personelData = window.personelData;

  ALANLAR.forEach(function(alan) {
    var kisiler = (gunlukData.liste && gunlukData.liste[alan.id]) || [];
    if (!kisiler.length) return;
    var satir = document.createElement("div"); satir.className = "gorev-satir";
    var alanEl = document.createElement("div"); alanEl.className = "gorev-alan"; alanEl.textContent = alan.label;
    var kisilerEl = document.createElement("div"); kisilerEl.className = "gorev-kisiler";
    kisiler.forEach(function(kid) {
      var pd = personelData[kid] || PERSONEL.find(function(p) { return p.id === kid; });
      var tag = document.createElement("span");
      tag.className = "kisi-tag" + (pd && pd.sabit ? " sabit" : "");
      tag.textContent = pd ? pd.isim : kid;
      kisilerEl.appendChild(tag);
    });
    satir.appendChild(alanEl); satir.appendChild(kisilerEl); listeDiv.appendChild(satir);
  });
}

function kysPngIndir() {
  var kart = document.getElementById("kys-liste-card");
  if (!kart) return;
  var pngBtn = kart.querySelector(".kys-png-btn");
  if (pngBtn) pngBtn.style.display = "none";
  function doCapture() {
    html2canvas(kart, { backgroundColor: "#151820", scale: 2, useCORS: true, logging: false })
      .then(function(canvas) {
        if (pngBtn) pngBtn.style.display = "";
        var link = document.createElement("a");
        link.download = "temizlik_listesi_" + bugunStr() + ".png";
        link.href = canvas.toDataURL("image/png"); link.click();
        showToast("🖼️ Temizlik listesi indirildi!", "success");
      }).catch(function() { if (pngBtn) pngBtn.style.display = ""; showToast("Resim oluşturulamadı!", "error"); });
  }
  if (typeof html2canvas === "undefined") {
    var s = document.createElement("script");
    s.src = "https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js";
    s.onload = doCapture;
    s.onerror = function() { if (pngBtn) pngBtn.style.display = ""; showToast("Kütüphane yüklenemedi!", "error"); };
    document.head.appendChild(s); showToast("⏳ Yükleniyor...");
  } else { doCapture(); }
}

// ── İŞ SEÇİMİ ────────────────────────────────────────────
async function isSecimi(n) {
  var PERSONEL     = window.PERSONEL;
  var personelData = window.personelData;
  var aktifIds = PERSONEL.filter(function(p) { return !personelData[p.id] || !personelData[p.id].izinli; })
                          .map(function(p) { return p.id; });
  var kalan = (isTuruData.kalan || []).filter(function(id) { return aktifIds.indexOf(id) >= 0; });
  if (kalan.length < n) kalan = aktifIds.slice();
  var secilen  = kalan.sort(function() { return Math.random() - 0.5; }).slice(0, n);
  var yeniKalan = kalan.filter(function(id) { return secilen.indexOf(id) < 0; });
  isTuruData = { secilen: (isTuruData.secilen || []).concat(secilen), kalan: yeniKalan };
  try { await _kysdb.collection("kys_is_turu").doc("tur").set(isTuruData); } catch(e) {}
  for (var i = 0; i < secilen.length; i++) {
    var kid = secilen[i]; var pd = personelData[kid]; if (!pd) continue;
    pd.isSayac = (pd.isSayac || 0) + 1;
    try { await _kysdb.collection("kys_personel").doc(kid).update({ isSayac: pd.isSayac }); } catch(e) {}
  }
  return secilen;
}

// ── İSTATİSTİK ────────────────────────────────────────────
function renderIstatistik() {
  var el = document.getElementById("kys-stat-content"); if (!el) return;
  var PERSONEL     = window.PERSONEL;
  var personelData = window.personelData;
  var maxPuan = 1;
  PERSONEL.forEach(function(p) { var v = (personelData[p.id] && personelData[p.id].puan) || 0; if (v > maxPuan) maxPuan = v; });
  var tablo = document.createElement("table"); tablo.className = "stat-tablo";
  tablo.innerHTML = '<thead><tr><th>Kişi</th><th>Tuvalet</th><th>Banyo</th><th>Çevre</th><th>İş</th><th>Puan</th></tr></thead><tbody></tbody>';
  var tbody = tablo.querySelector("tbody");
  PERSONEL.slice().sort(function(a,b) {
    return ((personelData[b.id] && personelData[b.id].puan) || 0) - ((personelData[a.id] && personelData[a.id].puan) || 0);
  }).forEach(function(p) {
    var pd = personelData[p.id]; var s = (pd && pd.sayaclar) || {};
    var puan = (pd && pd.puan) || 0; var pct = Math.round((puan / maxPuan) * 100);
    var tr = document.createElement("tr");
    tr.innerHTML = '<td>' + p.isim + (pd && pd.sabit ? ' <small style="color:var(--yellow)">★</small>' : '') + '</td>' +
      '<td><span>' + (s.tuvalet||0) + '</span><div class="stat-bar"><div class="stat-bar-fill" style="width:' + pct + '%"></div></div></td>' +
      '<td>' + (s.banyo||0) + '</td><td>' + (s.cevre||0) + '</td>' +
      '<td>' + ((pd && pd.isSayac)||0) + '</td>' +
      '<td style="color:var(--accent);font-weight:600">' + puan + '</td>';
    tbody.appendChild(tr);
  });
  el.innerHTML = ""; el.appendChild(tablo);
  var sifirlaWrap = document.createElement("div"); sifirlaWrap.style.marginTop = "16px";
  sifirlaWrap.innerHTML =
    '<button class="btn btn-ghost btn-sm" id="btn-sayac-sifirla" style="color:var(--red)">🗑️ Sayaçları Sıfırla</button>' +
    '<div id="sifirla-onay" style="display:none;margin-top:10px">' +
      '<p class="hint" style="margin-bottom:8px">Tüm temizlik ve iş sayaçları sıfırlanacak. Emin misin?</p>' +
      '<div class="btn-row"><button class="btn btn-danger btn-sm" id="btn-sifirla-evet">Evet, Sıfırla</button>' +
      '<button class="btn btn-ghost btn-sm" id="btn-sifirla-hayir">Vazgeç</button></div></div>';
  el.appendChild(sifirlaWrap);
  document.getElementById("btn-sayac-sifirla").addEventListener("click", function() { document.getElementById("sifirla-onay").style.display = ""; });
  document.getElementById("btn-sifirla-hayir").addEventListener("click", function() { document.getElementById("sifirla-onay").style.display = "none"; });
  document.getElementById("btn-sifirla-evet").addEventListener("click", sayaclariSifirla);
}

async function sayaclariSifirla() {
  var PERSONEL     = window.PERSONEL;
  var personelData = window.personelData;
  for (var i = 0; i < PERSONEL.length; i++) {
    var p = PERSONEL[i]; var pd = personelData[p.id]; if (!pd) continue;
    pd.sayaclar = { tuvalet:0, banyo:0, cevre:0, oda1:0, oda2:0, yazhane:0 }; pd.isSayac = 0; pd.puan = 0;
    try { await _kysdb.collection("kys_personel").doc(p.id).update({ sayaclar: pd.sayaclar, isSayac: 0, puan: 0 }); } catch(e) {}
  }
  isTuruData = { secilen: [], kalan: PERSONEL.map(function(p) { return p.id; }) };
  try { await _kysdb.collection("kys_is_turu").doc("tur").set(isTuruData); } catch(e) {}
  window.cacheYaz("kys_personel", { PERSONEL: PERSONEL, personelData: personelData });
  renderIstatistik();
  showToast("🗑️ Sayaçlar sıfırlandı!", "success");
}

// ── BUTONLAR ──────────────────────────────────────────────
var _dinleBasladi = false;
function dinleButonlar() {
  if (_dinleBasladi) return;
  _dinleBasladi = true;
  document.getElementById("btn-temizlik-yap").addEventListener("click", async function() {
    if (gunlukData && gunlukData.tarih === bugunStr()) {
      document.getElementById("kys-is-card").style.display   = "none";
      document.getElementById("kys-stat-card").style.display = "none";
      document.getElementById("kys-liste-card").style.display = "";
      renderGunlukListe();
      showToast("Bugünün listesi zaten hazır 📋");
      return;
    }
    await temizlikListesiYap();
    document.getElementById("kys-is-card").style.display   = "none";
    document.getElementById("kys-stat-card").style.display = "none";
    document.getElementById("kys-liste-card").style.display = "";
    actualizarYenidenBtn();
  });

  document.getElementById("btn-temizlik-yeniden").addEventListener("click", async function() {
    document.getElementById("kys-is-card").style.display    = "none";
    document.getElementById("kys-stat-card").style.display  = "none";
    document.getElementById("kys-liste-card").style.display = "none";
    showToast("🔄 Yeniden yapılıyor...");
    await temizlikListesiYapZorla();
    document.getElementById("kys-liste-card").style.display = "";
  });

  document.getElementById("btn-is-sec").addEventListener("click", function() {
    var c = document.getElementById("kys-is-card");
    c.style.display = c.style.display === "none" ? "" : "none";
    document.getElementById("kys-is-sonuc").style.display   = "none";
    document.getElementById("kys-liste-card").style.display = "none";
    document.getElementById("kys-stat-card").style.display  = "none";
  });

  document.getElementById("btn-istatistik").addEventListener("click", function() {
    var c = document.getElementById("kys-stat-card");
    c.style.display = c.style.display === "none" ? "" : "none";
    document.getElementById("kys-is-card").style.display    = "none";
    document.getElementById("kys-liste-card").style.display = "none";
    renderIstatistik();
  });

  document.querySelectorAll(".kac-kisi").forEach(function(btn) {
    btn.addEventListener("click", async function() {
      var n = parseInt(btn.dataset.n);
      document.querySelectorAll(".kac-kisi").forEach(function(b) { b.classList.remove("selected"); });
      btn.classList.add("selected");
      var secilen = await isSecimi(n);
      var kisilerEl = document.getElementById("kys-secilen-liste");
      kisilerEl.innerHTML = "";
      var personelData = window.personelData; var PERSONEL = window.PERSONEL;
      secilen.forEach(function(kid) {
        var pd = personelData[kid] || PERSONEL.find(function(p) { return p.id === kid; });
        var span = document.createElement("span");
        span.className = "kisi-tag"; span.style.fontSize = "14px"; span.style.padding = "6px 14px";
        span.textContent = pd ? pd.isim : kid; kisilerEl.appendChild(span);
      });
      document.getElementById("kys-is-sonuc").style.display = "";
      showToast(n + " kişi seçildi ✅", "success");
    });
  });

  document.getElementById("btn-is-yenile").addEventListener("click", function() {
    document.querySelectorAll(".kac-kisi").forEach(function(b) { b.classList.remove("selected"); });
    document.getElementById("kys-is-sonuc").style.display = "none";
  });
}
