// ── NÖBET ÇİZELGESİ v4
// Sadece çizelge oluştur ve kim nöbet tutuyor göster
// Personel window.PERSONEL'den gelir (izinliler hariç)

var nobetCizelgesi = [];
var nobetBaslangicIdx = 0;

window.onFirebaseReady(function() { nobetRender(); });

// Personel güncellenince çizelge varsa yenile
window.onPersonelGuncelle && window.onPersonelGuncelle(function() {
  if (nobetCizelgesi.length) anaNobetWidget && anaNobetWidget();
});

// ─── ANA RENDER ───────────────────────────────────────────
function nobetRender() {
  var el = document.getElementById("nobet-icerik");
  if (!el) return;

  try {
    var idx = localStorage.getItem("nobet_baslangic_idx");
    if (idx !== null) nobetBaslangicIdx = parseInt(idx) || 0;
  } catch(e) {}

  el.innerHTML =
    // ── Form
    '<div class="card">' +
      '<div class="card-head"><span class="card-icon">📋</span><h2>Çizelge Oluştur</h2></div>' +
      '<div class="form-row">' +
        '<div class="form-group" style="flex:1"><label>Başlangıç Tarihi</label><input class="inp" id="nc-bas-tarih" type="date"/></div>' +
        '<div class="form-group" style="flex:1"><label>Başlangıç Saati</label><input class="inp" id="nc-bas-saat" type="time" value="08:00"/></div>' +
      '</div>' +
      '<div class="form-row">' +
        '<div class="form-group" style="flex:1"><label>Bitiş Tarihi</label><input class="inp" id="nc-bit-tarih" type="date"/></div>' +
        '<div class="form-group" style="flex:1"><label>Bitiş Saati</label><input class="inp" id="nc-bit-saat" type="time" value="08:00"/></div>' +
      '</div>' +
      '<button class="btn btn-primary" id="nc-olustur-btn" style="width:100%">📋 Çizelge Oluştur</button>' +
    '</div>' +
    // ── Çizelge alanı
    '<div id="nc-cizelge-wrap"></div>';

  var bugun = new Date().toISOString().split("T")[0];
  document.getElementById("nc-bas-tarih").value = bugun;
  document.getElementById("nc-bit-tarih").value = bugun;

  if (nobetCizelgesi.length) nobetCizelgeGoster();

  document.getElementById("nc-olustur-btn").addEventListener("click", nobetCizelgeOlustur);
}

// ─── AKTİF PERSONEL ───────────────────────────────────────
function nobetAktifPersonel() {
  if (window.PERSONEL && window.PERSONEL.length) {
    var pData = window.personelData || {};
    return window.PERSONEL
      .filter(function(p) { return !pData[p.id] || !pData[p.id].izinli; })
      .map(function(p) { return p.isim; });
  }
  // Fallback
  return ["Cuma","Mustafa","Ahmet","Mertali","Hasan","Hüseyin","Mert","Taner","Yusuf","Samet","Ali"];
}

// ─── ÇİZELGE OLUŞTUR ──────────────────────────────────────
function nobetCizelgeOlustur() {
  var basTarih = document.getElementById("nc-bas-tarih").value;
  var basSaat  = document.getElementById("nc-bas-saat").value;
  var bitTarih = document.getElementById("nc-bit-tarih").value;
  var bitSaat  = document.getElementById("nc-bit-saat").value;

  if (!basTarih || !basSaat || !bitTarih || !bitSaat) { showToast("Tüm tarih ve saatleri gir!", "error"); return; }

  var bas = new Date(basTarih + "T" + basSaat + ":00");
  var bit = new Date(bitTarih + "T" + bitSaat + ":00");
  if (bit <= bas) { showToast("Bitiş, başlangıçtan sonra olmalı!", "error"); return; }

  var toplamSaat  = (bit - bas) / (1000 * 60 * 60);
  var dilimSayisi = Math.ceil(toplamSaat / 2);
  if (dilimSayisi > 200) { showToast("Çok uzun aralık!", "error"); return; }

  var aktif  = nobetAktifPersonel();
  nobetCizelgesi = [];
  var kisiIdx = nobetBaslangicIdx;

  for (var i = 0; i < dilimSayisi; i++) {
    var dilimBas = new Date(bas.getTime() + i * 2 * 60 * 60 * 1000);
    var dilimBit = new Date(dilimBas.getTime() + 2 * 60 * 60 * 1000);
    if (dilimBit > bit) dilimBit = bit;
    nobetCizelgesi.push({
      no:    i + 1,
      bas:   dilimBas,
      bit:   dilimBit,
      kisi1: aktif[kisiIdx % aktif.length],
      kisi2: aktif[(kisiIdx + 1) % aktif.length]
    });
    kisiIdx += 2;
  }

  nobetBaslangicIdx = kisiIdx % aktif.length;
  try { localStorage.setItem("nobet_baslangic_idx", nobetBaslangicIdx); } catch(e) {}

  nobetCizelgeGoster();
  showToast("✅ " + dilimSayisi + " nöbet dilimi oluşturuldu!", "success");
}

// ─── ÇİZELGEYİ GÖSTER ────────────────────────────────────
function nobetCizelgeGoster() {
  var wrap = document.getElementById("nc-cizelge-wrap");
  if (!wrap) return;

  var html =
    '<div class="nc-indirme-row">' +
      '<button class="btn btn-primary" id="nc-pdf-btn">📄 PDF İndir</button>' +
      '<button class="btn btn-secondary" id="nc-png-btn">🖼️ Resim İndir</button>' +
      '<button class="btn btn-ghost btn-sm" id="nc-sifirla-btn">🗑️ Temizle</button>' +
    '</div>' +
    '<div class="card" id="nc-cizelge-kart" style="padding:0;overflow:hidden">' +
      '<div class="nc-tablo-baslik">' +
        '<div class="nc-tablo-baslik-metin">🌙 NÖBET ÇİZELGESİ</div>' +
        '<div class="nc-tablo-tarih">' + nobetAralikMetni() + '</div>' +
      '</div>' +
      '<div class="nc-tablo-wrap">' +
      '<table class="nc-tablo" id="nc-tablo">' +
        '<thead><tr><th>#</th><th>Başlangıç</th><th>Bitiş</th><th>1. Nöbetçi</th><th>2. Nöbetçi</th></tr></thead>' +
        '<tbody>' + nobetSatirlar() + '</tbody>' +
      '</table>' +
      '</div>' +
      '<div class="nc-tablo-footer">JOZH Panel • Her dilim 2 saattir • Toplam ' + nobetCizelgesi.length + ' dilim</div>' +
    '</div>';

  wrap.innerHTML = html;

  document.getElementById("nc-pdf-btn").addEventListener("click", nobetPdfIndir);
  document.getElementById("nc-png-btn").addEventListener("click", nobetPngIndir);
  document.getElementById("nc-sifirla-btn").addEventListener("click", function() {
    nobetCizelgesi = [];
    wrap.innerHTML = "";
    showToast("Çizelge temizlendi.");
  });
}

function nobetAralikMetni() {
  if (!nobetCizelgesi.length) return "";
  return formatAnSaatTarih(nobetCizelgesi[0].bas) + " → " + formatAnSaatTarih(nobetCizelgesi[nobetCizelgesi.length-1].bit);
}

function nobetSatirlar() {
  var gunRenk = {}; var renkSira = 0;
  return nobetCizelgesi.map(function(d) {
    var gk = d.bas.toISOString().split("T")[0];
    if (!(gk in gunRenk)) { gunRenk[gk] = renkSira % 2 === 0 ? "" : "nc-tr-alt"; renkSira++; }
    return '<tr class="' + gunRenk[gk] + '">' +
      '<td class="nc-td-no">' + d.no + '</td>' +
      '<td class="nc-td-saat">' + formatAnSaatTarih(d.bas) + '</td>' +
      '<td class="nc-td-saat">' + formatAnSaatTarih(d.bit) + '</td>' +
      '<td class="nc-td-kisi">' + escN(d.kisi1) + '</td>' +
      '<td class="nc-td-kisi">' + escN(d.kisi2) + '</td>' +
    '</tr>';
  }).join("");
}

// ─── PDF ──────────────────────────────────────────────────
function nobetPdfIndir() {
  var kart = document.getElementById("nc-cizelge-kart");
  if (!kart) return;
  var tabloHTML = kart.outerHTML;
  var html = '<!DOCTYPE html><html lang="tr"><head><meta charset="UTF-8"/><title>Nöbet Çizelgesi</title><style>' +
    '* { box-sizing:border-box; margin:0; padding:0; }' +
    'body { font-family:Arial,sans-serif; background:#fff; color:#111; padding:20px; }' +
    '.nc-tablo-baslik { background:#1a2035; color:#fff; padding:16px 20px; border-radius:10px 10px 0 0; }' +
    '.nc-tablo-baslik-metin { font-size:18px; font-weight:700; letter-spacing:2px; }' +
    '.nc-tablo-tarih { font-size:12px; color:#8891aa; margin-top:4px; }' +
    '.nc-tablo { width:100%; border-collapse:collapse; font-size:13px; }' +
    '.nc-tablo thead tr { background:#f0f2f8; }' +
    '.nc-tablo th { padding:10px 12px; text-align:left; font-size:11px; font-weight:700; text-transform:uppercase; color:#555; border-bottom:2px solid #dde2ec; }' +
    '.nc-tablo td { padding:9px 12px; border-bottom:1px solid #eef1f6; }' +
    '.nc-tr-alt { background:#f8f9fc; }' +
    '.nc-td-no { font-weight:700; color:#888; font-size:11px; text-align:center; }' +
    '.nc-td-saat { font-family:monospace; font-size:12px; color:#333; }' +
    '.nc-td-kisi { font-weight:600; color:#1a2035; }' +
    '.nc-tablo-footer { text-align:center; font-size:10px; color:#aaa; padding:10px; border-top:1px solid #eee; }' +
    '.nc-indirme-row { display:none !important; }' +
    '</style></head><body>' + tabloHTML + '</body></html>';
  var blob = new Blob([html], { type: 'text/html;charset=utf-8' });
  var url  = URL.createObjectURL(blob);
  var a    = document.createElement('a'); a.href = url; a.download = 'nobet_cizelgesi.html';
  document.body.appendChild(a); a.click(); document.body.removeChild(a);
  setTimeout(function() { URL.revokeObjectURL(url); }, 2000);
  showToast("📄 İndirildi — Safari'de Paylaş → PDF", "success");
}

function nobetPngIndir() {
  var kart = document.getElementById("nc-cizelge-kart");
  if (!kart) return;
  var btns = document.querySelector(".nc-indirme-row");
  if (btns) btns.style.display = "none";
  function doCapture() {
    html2canvas(kart, { backgroundColor:"#ffffff", scale:2, useCORS:true, logging:false })
      .then(function(canvas) {
        if (btns) btns.style.display = "";
        var a = document.createElement("a"); a.download = "nobet_cizelgesi.png";
        a.href = canvas.toDataURL("image/png"); a.click();
        showToast("🖼️ Resim indirildi!", "success");
      }).catch(function() { if (btns) btns.style.display = ""; showToast("Resim oluşturulamadı!", "error"); });
  }
  if (typeof html2canvas === "undefined") {
    var s = document.createElement("script");
    s.src = "https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js";
    s.onload = doCapture;
    s.onerror = function() { if (btns) btns.style.display = ""; showToast("Kütüphane yüklenemedi!", "error"); };
    document.head.appendChild(s); showToast("⏳ Yükleniyor...");
  } else { doCapture(); }
}

// ─── YARDIMCI ─────────────────────────────────────────────
var _AYLAR = ["Oca","Şub","Mar","Nis","May","Haz","Tem","Ağu","Eyl","Eki","Kas","Ara"];
var _GUNLER = ["Paz","Pzt","Sal","Çar","Per","Cum","Cmt"];
function formatAnSaatTarih(d) {
  return d.getDate() + " " + _AYLAR[d.getMonth()] + " " + _GUNLER[d.getDay()] +
    " " + ("0"+d.getHours()).slice(-2) + ":" + ("0"+d.getMinutes()).slice(-2);
}
function escN(s) { return (s||"").replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;"); }
