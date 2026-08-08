// ── ANA SAYFA (Dashboard) v1
// Tüm modüllerden özet bilgi çeker

var anaYuklendi = false;

// Sayfa her aktif olduğunda çağrılır
window.anaRefresh = function() {
  anaYuklendi = false;
  anaYukle();
};

function anaYukle() {
  if (anaYuklendi) return;
  anaYuklendi = true;

  anaSaatGuncelle();
  anaSaatInterval = setInterval(anaSaatGuncelle, 30000);

  anaKysWidget();
  anaSporWidget();
  anaCuzdanWidget();
  anaRehberWidget();
  anaNobetWidget();
}

// ── SAAT / TARİH ──────────────────────────────────────────
var anaSaatInterval;
function anaSaatGuncelle() {
  var el = document.getElementById("ana-saat");
  var tel = document.getElementById("ana-tarih-label");
  if (!el) return;
  var d = new Date();
  var saatStr = ("0"+d.getHours()).slice(-2) + ":" + ("0"+d.getMinutes()).slice(-2);
  var aylar = ["Ocak","Şubat","Mart","Nisan","Mayıs","Haziran","Temmuz","Ağustos","Eylül","Ekim","Kasım","Aralık"];
  var gunler = ["Pazar","Pazartesi","Salı","Çarşamba","Perşembe","Cuma","Cumartesi"];
  el.textContent = saatStr;
  if (tel) tel.textContent = gunler[d.getDay()] + ", " + d.getDate() + " " + aylar[d.getMonth()] + " " + d.getFullYear();
}

// ── PERSONEL WIDGET (KYS'ten bağımsız) ──────────────────
var ANA_PERSONEL = [
  { id: "cuma",    isim: "Cuma" },
  { id: "mustafa", isim: "Mustafa" },
  { id: "ahmet",   isim: "Ahmet" },
  { id: "mertali", isim: "Mertali" },
  { id: "hasan",   isim: "Hasan" },
  { id: "huseyin", isim: "Hüseyin" },
  { id: "mert",    isim: "Mert" },
  { id: "taner",   isim: "Taner" },
  { id: "yusuf",   isim: "Yusuf" },
  { id: "samet",   isim: "Samet" },
  { id: "ali",     isim: "Ali" }
];

function anaIzinOku() {
  try {
    var s = localStorage.getItem("ana_izin");
    return s ? JSON.parse(s) : {};
  } catch(e) { return {}; }
}

function anaIzinYaz(izinMap) {
  try { localStorage.setItem("ana_izin", JSON.stringify(izinMap)); } catch(e) {}
}

function anaPersonelWidget() {
  var el = document.getElementById("ana-personel-icerik");
  if (!el) return;

  var izinMap = anaIzinOku();
  // Bugün kontrolü — yeni gün gelince izinleri sıfırla
  var bugun = new Date().toISOString().split("T")[0];
  if (izinMap.__tarih && izinMap.__tarih !== bugun) {
    izinMap = { __tarih: bugun };
    anaIzinYaz(izinMap);
  }
  if (!izinMap.__tarih) {
    izinMap.__tarih = bugun;
    anaIzinYaz(izinMap);
  }

  var yoklar = ANA_PERSONEL.filter(function(p) { return izinMap[p.id]; });
  var varSayisi = ANA_PERSONEL.length - yoklar.length;

  var html = '<div class="ana-personel-ozet">' +
    '<span class="ana-p-var"><span class="ana-p-sayi">' + varSayisi + '</span> Hazır</span>' +
    (yoklar.length ? '<span class="ana-p-yok"><span class="ana-p-sayi">' + yoklar.length + '</span> Yok</span>' : '') +
  '</div>';

  html += '<div class="ana-personel-grid">';
  ANA_PERSONEL.forEach(function(p) {
    var yokMu = !!izinMap[p.id];
    html += '<button class="ana-p-btn' + (yokMu ? ' yok' : '') + '" data-pid="' + p.id + '">' +
      '<span class="ana-p-avatar">' + p.isim[0] + '</span>' +
      '<span class="ana-p-isim">' + p.isim + '</span>' +
      (yokMu ? '<span class="ana-p-yok-badge">YOK</span>' : '') +
    '</button>';
  });
  html += '</div>';

  el.innerHTML = html;

  el.querySelectorAll(".ana-p-btn").forEach(function(btn) {
    btn.addEventListener("click", function() {
      var pid = btn.dataset.pid;
      var izin = anaIzinOku();
      if (!izin.__tarih) izin.__tarih = new Date().toISOString().split("T")[0];
      izin[pid] = !izin[pid];
      anaIzinYaz(izin);
          var p = ANA_PERSONEL.find(function(x){ return x.id === pid; });
      var isim = p ? p.isim : pid;
      showToast(izin[pid] ? "❌ " + isim + " — Yok" : "✅ " + isim + " — Hazır", izin[pid] ? "error" : "success");
    });
  });
}

// ── KYS WIDGET ────────────────────────────────────────────
function anaKysWidget() {
  var el = document.getElementById("ana-kys-icerik");
  if (!el) return;

  var bugun = new Date().toISOString().split("T")[0];
  var liste = (typeof gunlukData !== "undefined") ? gunlukData : null;

  if (!liste) {
    var c = window.cacheOku("kys_gunluk_" + bugun);
    if (c) liste = c;
  }

  if (!liste || liste.tarih !== bugun) {
    el.innerHTML = '<div class="ana-kys-bos">' +
      '<span style="font-size:22px">🧹</span>' +
      '<span>Bugün henüz temizlik listesi çıkmadı</span>' +
      '<button class="btn btn-ghost btn-sm" onclick="gotoPage(\'kys\')">KYS\'ye Git →</button>' +
    '</div>';
    return;
  }

  var pList = (typeof PERSONEL !== "undefined") ? PERSONEL : [];
  var pData = (typeof personelData !== "undefined") ? personelData : {};
  if (!pList.length) {
    var c = window.cacheOku("kys_personel");
    if (c) { pList = c.PERSONEL || []; pData = c.personelData || {}; }
  }

  var ALANLAR_MAP = {
    tuvalet: "🚽 Tuvalet", banyo: "🚿 Banyo",
    cevre: "🌳 Çevre", oda1: "🛏️ 1. Oda",
    oda2: "🛏️ 2. Oda", yazhane: "📋 Yazhane"
  };

  var html = '<div class="ana-kys-liste">';
  var listeObj = liste.liste || {};
  Object.keys(listeObj).forEach(function(alanId) {
    var kisiler = listeObj[alanId];
    if (!kisiler || !kisiler.length) return;
    var isimler = kisiler.map(function(kid) {
      var p = pList.find(function(x) { return x.id === kid; });
      return p ? p.isim : kid;
    }).join(", ");
    html += '<div class="ana-kys-satir">' +
      '<span class="ana-kys-alan">' + (ALANLAR_MAP[alanId]||alanId) + '</span>' +
      '<span class="ana-kys-kisiler">' + isimler + '</span>' +
    '</div>';
  });
  html += '</div>';

  el.innerHTML = html || '<p class="empty-text">Liste boş.</p>';
}

// ── SPOR WIDGET ───────────────────────────────────────────
function anaSporWidget() {
  var el = document.getElementById("ana-spor-icerik");
  if (!el) return;

  var p = (typeof profil !== "undefined") ? profil : null;
  if (!p) {
    var c = window.cacheOku("spor_profil");
    if (c) p = c;
  }

  if (!p) {
    el.innerHTML = '<p class="empty-text" style="padding:6px 0">Spor profili oluşturulmamış.</p>';
    return;
  }

  // Bugünkü program
  var gunIdx = (new Date().getDay() + 6) % 7;
  var prog = (typeof program !== "undefined") ? program : null;
  if (!prog) {
    var c = window.cacheOku("spor_program");
    if (c) prog = c;
  }

  var bugunkuGun = prog ? prog[gunIdx] : null;
  var bugunYapildi = false;
  var bugunStr2 = new Date().toISOString().split("T")[0];
  var antCache = window.cacheOku("spor_antrenman_" + bugunStr2);
  if (antCache) bugunYapildi = true;

  var kazanilanRozetler = (p.rozetler||[]).length;
  var toplamRozet = 9;

  var hedefler = { askerlik: "🎖️ Askerlik", kas_yap: "💪 Kas", kondisyon: "🏃 Kondisyon", yag_yak: "🔥 Yağ Yak" };
  var seviyeStr = ["","🟢 Başlangıç","🟡 Orta","🔴 İleri"][p.seviye] || "";

  var html =
    '<div class="ana-spor-stat-row">' +
      '<div class="ana-stat-kutu"><div class="ana-stat-sayi">' + (p.xp||0) + '</div><div class="ana-stat-label">XP</div></div>' +
      '<div class="ana-stat-kutu"><div class="ana-stat-sayi">' + (p.seri||0) + '</div><div class="ana-stat-label">Seri 🔥</div></div>' +
      '<div class="ana-stat-kutu"><div class="ana-stat-sayi">' + (p.toplamAntrenman||0) + '</div><div class="ana-stat-label">Antrenman</div></div>' +
      '<div class="ana-stat-kutu"><div class="ana-stat-sayi">' + kazanilanRozetler + '/' + toplamRozet + '</div><div class="ana-stat-label">🏅 Rozet</div></div>' +
    '</div>';

  if (bugunkuGun) {
    html += '<div class="ana-spor-bugun' + (bugunYapildi ? ' yapildi' : '') + '">' +
      '<span>' + bugunkuGun.emoji + ' <strong>' + bugunkuGun.kas + '</strong></span>' +
      (bugunYapildi
        ? '<span class="badge badge-green">✅ Tamamlandı</span>'
        : '<button class="btn btn-primary btn-sm" onclick="gotoPage(\'spor\')">Başlat →</button>') +
    '</div>';
  }

  el.innerHTML = html;
}

// ── CÜZDAN WIDGET ─────────────────────────────────────────
function anaCuzdanWidget() {
  var el = document.getElementById("ana-cuzdan-icerik");
  if (!el) return;

  var pinVar = !!localStorage.getItem("cuzdan_v");
  var kartSayisi = 0;
  if (pinVar) {
    // Şifreli veri var ama sayıyı decode etmeden bilemeyiz;
    // kartlar dizisini kullan (cüzdan açıksa dolu olur)
    var k = (typeof kartlar !== "undefined") ? kartlar : [];
    kartSayisi = k.length;
  }

  if (!pinVar) {
    el.innerHTML = '<p class="empty-text" style="padding:4px 0">Henüz kart eklenmemiş.</p>';
    return;
  }

  el.innerHTML =
    '<div class="ana-cuzdan-satir">' +
      '<span class="ana-cuzdan-ikon">💳</span>' +
      '<span class="ana-cuzdan-metin">' +
        (kartSayisi > 0
          ? '<strong>' + kartSayisi + '</strong> kart kayıtlı'
          : 'Kartlar kilitli') +
      '</span>' +
      '<button class="btn btn-ghost btn-sm" onclick="gotoPage(\'cuzdan\')">Görüntüle →</button>' +
    '</div>';
}

// ── REHBER WIDGET ─────────────────────────────────────────
function anaRehberWidget() {
  var el = document.getElementById("ana-rehber-icerik");
  if (!el) return;

  var k = (typeof kisiler !== "undefined") ? kisiler : [];
  if (!k.length) {
    var c = window.cacheOku("rehber");
    if (c) k = c;
  }

  if (!k.length) {
    el.innerHTML = '<p class="empty-text" style="padding:4px 0">Henüz numara eklenmemiş.</p>';
    return;
  }

  // Favoriler önce, max 3
  var siralı = k.slice().sort(function(a,b) {
    if (b.favori && !a.favori) return 1;
    if (a.favori && !b.favori) return -1;
    return 0;
  }).slice(0, 3);

  var html = siralı.map(function(kisi) {
    return '<div class="ana-rehber-satir">' +
      '<div class="ana-rehber-sol">' +
        '<span class="ana-rehber-isim">' + escAna(kisi.isim||"") + '</span>' +
        '<span class="ana-rehber-num">' + escAna(kisi.numara||"") + '</span>' +
      '</div>' +
      '<a href="tel:' + escAna(kisi.numara||"") + '" class="ana-ara-btn">📞</a>' +
    '</div>';
  }).join("");

  el.innerHTML = html;
}

// ── NÖBET WIDGET ──────────────────────────────────────────
function anaNobetWidget() {
  var el = document.getElementById("ana-nobet-icerik");
  if (!el) return;

  // Kayıtlı çizelge var mı?
  var cizelge = (typeof nobetCizelgesi !== "undefined") ? nobetCizelgesi : [];

  if (!cizelge.length) {
    el.innerHTML = '<div class="ana-nobet-bos">' +
      '<span style="font-size:22px">🌙</span>' +
      '<span>Aktif nöbet çizelgesi yok</span>' +
      '<button class="btn btn-ghost btn-sm" onclick="gotoPage(\'nobet\')">Çizelge Oluştur →</button>' +
    '</div>';
    return;
  }

  var simdi = new Date();
  var yaklasin = null;
  var aktif = null;

  cizelge.forEach(function(d) {
    if (d.bas <= simdi && d.bit > simdi) aktif = d;
    else if (d.bas > simdi && !yaklasin) yaklasin = d;
  });

  var html = "";

  if (aktif) {
    html += '<div class="ana-nobet-aktif">' +
      '<div class="ana-nobet-aktif-label">⚡ ŞU AN NÖBETTE</div>' +
      '<div class="ana-nobet-kisiler">' +
        '<span class="ana-nobet-kisi">' + escAna(aktif.kisi1) + '</span>' +
        '<span class="ana-nobet-kisi">' + escAna(aktif.kisi2) + '</span>' +
      '</div>' +
      '<div class="ana-nobet-saat">' + formatAnaSaat(aktif.bas) + ' → ' + formatAnaSaat(aktif.bit) + '</div>' +
    '</div>';
  }

  if (yaklasin) {
    var kalanMs = yaklasin.bas - simdi;
    var kalanSaat = Math.floor(kalanMs / (1000*60*60));
    var kalanDak = Math.floor((kalanMs % (1000*60*60)) / (1000*60));
    var kalanStr = kalanSaat > 0
      ? kalanSaat + " sa " + kalanDak + " dk"
      : kalanDak + " dakika";

    html += '<div class="ana-nobet-yaklasan">' +
      '<div class="ana-nobet-y-label">🔜 Sonraki Nöbet — ' + kalanStr + ' sonra</div>' +
      '<div class="ana-nobet-kisiler">' +
        '<span class="ana-nobet-kisi">' + escAna(yaklasin.kisi1) + '</span>' +
        '<span class="ana-nobet-kisi">' + escAna(yaklasin.kisi2) + '</span>' +
      '</div>' +
      '<div class="ana-nobet-saat">' + formatAnaSaatTarih(yaklasin.bas) + '</div>' +
    '</div>';
  }

  if (!html) {
    html = '<div class="ana-nobet-bos"><span>Tüm nöbetler tamamlandı ✅</span></div>';
  }

  el.innerHTML = html;
}

function formatAnaSaat(d) {
  return ("0"+d.getHours()).slice(-2) + ":" + ("0"+d.getMinutes()).slice(-2);
}
var ANA_AYLAR = ["Oca","Şub","Mar","Nis","May","Haz","Tem","Ağu","Eyl","Eki","Kas","Ara"];
function formatAnaSaatTarih(d) {
  return d.getDate() + " " + ANA_AYLAR[d.getMonth()] + " " + formatAnaSaat(d);
}
function escAna(s) {
  return (s||"").replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;");
}

// Sayfa değişince temizle
window.addEventListener("beforeunload", function() {
  clearInterval(anaSaatInterval);
});
