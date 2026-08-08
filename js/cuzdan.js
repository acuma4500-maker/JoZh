// ── CÜZDAN v2
// FİX: Kart düzenleme eklendi
// FİX: PIN sıfırlama öncesi yedek uyarısı
// FİX: Telefon değişince veri kaybolur uyarısı eklendi

var kartlar = [];
var pinDogrulandi = false;
var aktifPin = null;
var duzenleIdx = -1; // -1 = yeni kart, >=0 = düzenleme

var KART_RENKLERI = [
  { id: "mavi",    bg: "linear-gradient(135deg,#1a237e,#1565c0)" },
  { id: "koyu",    bg: "linear-gradient(135deg,#1a1a2e,#16213e)" },
  { id: "yesil",   bg: "linear-gradient(135deg,#1b5e20,#2e7d32)" },
  { id: "mor",     bg: "linear-gradient(135deg,#4a148c,#6a1b9a)" },
  { id: "kirmizi", bg: "linear-gradient(135deg,#b71c1c,#c62828)" },
];
var MARKALAR = {
  visa:       { logo: "VISA", stil: "font-style:italic;font-weight:900;font-size:20px" },
  mastercard: { logo: "MC",   stil: "font-size:16px;font-weight:700" },
  troy:       { logo: "TROY", stil: "font-weight:900;font-size:18px;letter-spacing:2px" },
  amex:       { logo: "AMEX", stil: "font-weight:700;font-size:16px;letter-spacing:2px" },
  diger:      { logo: "CARD", stil: "font-weight:600;font-size:14px;opacity:0.7" },
};

async function anahtarOlustur(pin) {
  var enc = new TextEncoder();
  var km  = await crypto.subtle.importKey("raw", enc.encode(pin), "PBKDF2", false, ["deriveKey"]);
  return crypto.subtle.deriveKey(
    { name:"PBKDF2", salt:enc.encode("jozh-cuzdan-salt"), iterations:100000, hash:"SHA-256" },
    km, { name:"AES-GCM", length:256 }, false, ["encrypt","decrypt"]
  );
}
async function sifrele(metin, pin) {
  var key = await anahtarOlustur(pin);
  var iv  = crypto.getRandomValues(new Uint8Array(12));
  var enc = await crypto.subtle.encrypt({name:"AES-GCM",iv:iv}, key, new TextEncoder().encode(metin));
  return btoa(JSON.stringify({ iv:Array.from(iv), data:Array.from(new Uint8Array(enc)) }));
}
async function coz(b64, pin) {
  try {
    var p   = JSON.parse(atob(b64));
    var key = await anahtarOlustur(pin);
    var dec = await crypto.subtle.decrypt({name:"AES-GCM",iv:new Uint8Array(p.iv)}, key, new Uint8Array(p.data));
    return new TextDecoder().decode(dec);
  } catch(e) { return null; }
}

function pinVarMi() { return !!localStorage.getItem("cuzdan_v"); }
async function pinOlustur(pin) { localStorage.setItem("cuzdan_v", await sifrele("jozh-ok", pin)); }
async function pinKontrol(pin) {
  var t = localStorage.getItem("cuzdan_v");
  if (!t) return false;
  return (await coz(t, pin)) === "jozh-ok";
}
async function kartlariKaydet() {
  localStorage.setItem("cuzdan_d", await sifrele(JSON.stringify(kartlar), aktifPin));
}
async function kartlariYukle() {
  var s = localStorage.getItem("cuzdan_d");
  if (!s) { kartlar = []; return; }
  var j = await coz(s, aktifPin);
  try { kartlar = j ? JSON.parse(j) : []; } catch(e) { kartlar = []; }
}

window.onFirebaseReady(function() { setTimeout(cuzdanBaslat, 200); });

function cuzdanBaslat() {
  pinEkraniGoster(pinVarMi() ? "gir" : "olustur");
}

function pinEkraniGoster(mod) {
  var el = document.getElementById("cuzdan-icerik");
  if (!el) return;
  if (mod === "olustur") {
    el.innerHTML =
      '<div class="card">' +
        '<div class="card-head"><span class="card-icon">🔐</span><h2>PIN Oluştur</h2></div>' +
        '<p class="hint" style="margin-bottom:4px">Kartların bu PIN ile şifrelenir.</p>' +
        '<p class="hint" style="margin-bottom:12px;color:var(--yellow)">⚠️ Kartlar telefonda saklanır. Telefon değişirse yedek al.</p>' +
        '<div class="form-group"><label>PIN (min 4 hane)</label><input class="inp" id="pin-inp1" type="password" inputmode="numeric" placeholder="••••" maxlength="8"/></div>' +
        '<div class="form-group"><label>PIN Tekrar</label><input class="inp" id="pin-inp2" type="password" inputmode="numeric" placeholder="••••" maxlength="8"/></div>' +
        '<button class="btn btn-primary" id="btn-pin-olustur" style="width:100%">✅ PIN Oluştur</button>' +
      '</div>';
    document.getElementById("btn-pin-olustur").addEventListener("click", async function() {
      var p1 = document.getElementById("pin-inp1").value;
      var p2 = document.getElementById("pin-inp2").value;
      if (p1.length < 4)  { showToast("PIN en az 4 hane!", "error"); return; }
      if (p1 !== p2)      { showToast("PIN'ler eşleşmiyor!", "error"); return; }
      await pinOlustur(p1);
      aktifPin = p1; pinDogrulandi = true; kartlar = [];
      cuzdanAnaEkran();
      showToast("🔐 PIN oluşturuldu!", "success");
    });
  } else {
    el.innerHTML =
      '<div class="card">' +
        '<div class="card-head"><span class="card-icon">🔐</span><h2>PIN Gir</h2></div>' +
        '<div class="form-group"><input class="inp" id="pin-giris" type="password" inputmode="numeric" placeholder="••••" maxlength="8"/></div>' +
        '<button class="btn btn-primary" id="btn-pin-gir" style="width:100%">🔓 Aç</button>' +
        '<div style="margin-top:12px;text-align:center">' +
          '<button class="btn btn-ghost btn-sm" id="btn-pin-sifirla" style="color:var(--red)">PIN Sıfırla</button>' +
        '</div>' +
      '</div>';
    document.getElementById("btn-pin-gir").addEventListener("click", async function() {
      var pin = document.getElementById("pin-giris").value;
      if (await pinKontrol(pin)) {
        aktifPin = pin; pinDogrulandi = true;
        await kartlariYukle();
        cuzdanAnaEkran();
      } else {
        showToast("❌ Yanlış PIN!", "error");
        document.getElementById("pin-giris").value = "";
      }
    });
    document.getElementById("pin-giris").addEventListener("keydown", function(e) {
      if (e.key === "Enter") document.getElementById("btn-pin-gir").click();
    });
    document.getElementById("btn-pin-sifirla").addEventListener("click", function() {
      // Önce yedek var mı kontrolü
      var yedekVar = !!localStorage.getItem("cuzdan_d");
      var mesaj = yedekVar
        ? "⚠️ PIN sıfırlama TÜM KARTLARI SİLER!\n\nÖnce 'Yedekle' ile verileri kopyala, sonra sıfırla.\n\nYine de sıfırlamak istiyor musun?"
        : "PIN'i sıfırlamak istiyor musun? (Kart verisi yok)";
      if (confirm(mesaj)) {
        localStorage.removeItem("cuzdan_v");
        localStorage.removeItem("cuzdan_d");
        pinEkraniGoster("olustur");
        showToast("PIN sıfırlandı.");
      }
    });
  }
}

function cuzdanAnaEkran() {
  var el = document.getElementById("cuzdan-icerik");
  if (!el) return;
  duzenleIdx = -1;
  el.innerHTML =
    '<div id="cuzdan-kart-liste"></div>' +
    '<div class="btn-row" style="margin-top:4px;flex-wrap:wrap">' +
      '<button class="btn btn-primary" id="btn-kart-ekle">➕ Kart Ekle</button>' +
      '<button class="btn btn-ghost" id="btn-cuzdan-export">📤 Yedekle</button>' +
      '<button class="btn btn-ghost" id="btn-cuzdan-import">📥 Geri Yükle</button>' +
    '</div>' +
    '<p class="hint" style="margin-top:8px;color:var(--yellow)">⚠️ Veriler bu telefonda saklanır — düzenli yedek al.</p>' +
    '<div class="card" id="cuzdan-form-card" style="display:none;margin-top:14px">' +
      '<div class="card-head"><span class="card-icon">💳</span><h2 id="form-baslik">Yeni Kart</h2></div>' +
      '<div class="form-group"><label>Kart İsmi</label><input class="inp" id="kart-isim-inp" type="text" placeholder="Ziraat Bankası" maxlength="30"/></div>' +
      '<div class="form-group"><label>Kart Numarası</label><input class="inp" id="kart-numara-inp" type="tel" placeholder="0000 0000 0000 0000" maxlength="23"/></div>' +
      '<div class="form-row">' +
        '<div class="form-group" style="flex:1"><label>Son Kullanma</label><input class="inp" id="kart-sk-inp" type="tel" placeholder="MM/YY" maxlength="5"/></div>' +
        '<div class="form-group" style="flex:1"><label>CVV</label><input class="inp" id="kart-cvv-inp" type="tel" placeholder="•••" maxlength="4"/></div>' +
      '</div>' +
      '<div class="form-group"><label>Marka</label><div class="btn-row" style="flex-wrap:wrap">' +
        '<button class="btn btn-outline marka-btn" data-marka="visa">VISA</button>' +
        '<button class="btn btn-outline marka-btn" data-marka="mastercard">Mastercard</button>' +
        '<button class="btn btn-outline marka-btn" data-marka="troy">TROY</button>' +
        '<button class="btn btn-outline marka-btn" data-marka="amex">AMEX</button>' +
        '<button class="btn btn-outline marka-btn" data-marka="diger">Diğer</button>' +
      '</div></div>' +
      '<div class="form-group"><label>Renk</label><div class="btn-row">' +
        '<button class="renk-btn selected" data-renk="mavi" style="background:linear-gradient(135deg,#1a237e,#1565c0)"></button>' +
        '<button class="renk-btn" data-renk="koyu" style="background:linear-gradient(135deg,#1a1a2e,#16213e)"></button>' +
        '<button class="renk-btn" data-renk="yesil" style="background:linear-gradient(135deg,#1b5e20,#2e7d32)"></button>' +
        '<button class="renk-btn" data-renk="mor" style="background:linear-gradient(135deg,#4a148c,#6a1b9a)"></button>' +
        '<button class="renk-btn" data-renk="kirmizi" style="background:linear-gradient(135deg,#b71c1c,#c62828)"></button>' +
      '</div></div>' +
      '<div class="btn-row" style="margin-top:8px">' +
        '<button class="btn btn-primary" id="btn-kart-kaydet">💾 Kaydet</button>' +
        '<button class="btn btn-ghost" id="btn-kart-iptal">İptal</button>' +
      '</div>' +
    '</div>' +
    '<div class="card" id="import-card" style="display:none;margin-top:14px">' +
      '<div class="card-head"><span class="card-icon">📥</span><h2>Geri Yükle</h2></div>' +
      '<textarea class="inp" id="import-txt" rows="4" style="resize:none;font-size:11px" placeholder="Yedek metni buraya yapıştır..."></textarea>' +
      '<div class="btn-row" style="margin-top:8px">' +
        '<button class="btn btn-primary" id="btn-import-yap">📥 Yükle</button>' +
        '<button class="btn btn-ghost" id="btn-import-iptal">İptal</button>' +
      '</div>' +
    '</div>';
  renderKartlar();
  dinleAnaEkran();
}

function renderKartlar() {
  var liste = document.getElementById("cuzdan-kart-liste");
  if (!liste) return;
  if (!kartlar.length) {
    liste.innerHTML = '<p class="empty-text">Henüz kart eklenmedi.</p>';
    return;
  }
  liste.innerHTML = "";
  for (var idx = 0; idx < kartlar.length; idx++) {
    (function(i) {
      var kart  = kartlar[i];
      var renk  = KART_RENKLERI.find(function(r) { return r.id === kart.renk; }) || KART_RENKLERI[0];
      var marka = MARKALAR[kart.marka] || MARKALAR["diger"];
      var son4  = (kart.numara || "").replace(/\s/g,"").slice(-4);
      var numFmt = formatNo(kart.numara || "");
      var skUyari = skDurum(kart.son_kullanma);
      var skBadge = "";
      if (skUyari === "gecti") skBadge = '<span class="kart-sk-badge gecti">SÜRESİ DOLDU</span>';
      else if (skUyari === "yakin") skBadge = '<span class="kart-sk-badge yakin">YAKINDA</span>';

      var div = document.createElement("div");
      div.className = "kart-card";
      div.style.background = renk.bg;
      div.innerHTML =
        '<div class="kart-top">' +
          '<span class="kart-isim">' + escHTML(kart.isim) + '</span>' +
          '<span style="' + marka.stil + ';color:#fff">' + marka.logo + '</span>' +
        '</div>' +
        '<div style="margin:10px 0 2px;font-size:10px;opacity:0.55;letter-spacing:1px">KART NUMARASI</div>' +
        '<div class="kart-numara" id="kno' + i + '" style="cursor:pointer">•••• •••• •••• ' + son4 + '</div>' +
        '<div class="kart-alt">' +
          '<div><div class="kart-etiket">SON KULLANMA ' + skBadge + '</div><div class="kart-deger">' + escHTML(kart.son_kullanma) + '</div></div>' +
          '<div><div class="kart-etiket">CVV</div><div class="kart-deger" id="cvv' + i + '" style="cursor:pointer">•••</div></div>' +
          '<div style="margin-left:auto;display:flex;gap:4px">' +
            '<button class="kart-sil-btn" id="duz' + i + '" title="Düzenle" style="background:rgba(255,255,255,0.15)">✏️</button>' +
            '<button class="kart-sil-btn" id="sil' + i + '" title="Sil">🗑️</button>' +
          '</div>' +
        '</div>';
      liste.appendChild(div);

      // Kart no göster/gizle
      var knoEl = document.getElementById("kno" + i);
      var knoAcik = false;
      knoEl.addEventListener("click", function() {
        if (!knoAcik) { knoEl.textContent = numFmt; knoAcik = true; setTimeout(function() { knoEl.textContent = "•••• •••• •••• " + son4; knoAcik = false; }, 5000); }
        else { knoEl.textContent = "•••• •••• •••• " + son4; knoAcik = false; }
      });

      // CVV göster/gizle
      var cvvEl = document.getElementById("cvv" + i);
      var cvvAcik = false;
      cvvEl.addEventListener("click", function() {
        if (!cvvAcik) { cvvEl.textContent = kart.cvv; cvvAcik = true; setTimeout(function() { cvvEl.textContent = "•••"; cvvAcik = false; }, 3000); }
        else { cvvEl.textContent = "•••"; cvvAcik = false; }
      });

      // Düzenle
      document.getElementById("duz" + i).addEventListener("click", function(e) {
        e.stopPropagation();
        kartDuzenlemeAc(i);
      });

      // Sil
      document.getElementById("sil" + i).addEventListener("click", function(e) {
        e.stopPropagation();
        if (!confirm(kart.isim + " kartını silmek istiyor musun?")) return;
        kartlar.splice(i, 1);
        kartlariKaydet();
        renderKartlar();
        showToast("Kart silindi.");
      });
    })(idx);
  }
}

function kartDuzenlemeAc(i) {
  duzenleIdx = i;
  var kart = kartlar[i];
  var form = document.getElementById("cuzdan-form-card");
  document.getElementById("form-baslik").textContent = "Kartı Düzenle";
  document.getElementById("kart-isim-inp").value = kart.isim || "";
  document.getElementById("kart-numara-inp").value = formatNo(kart.numara || "");
  document.getElementById("kart-sk-inp").value = kart.son_kullanma || "";
  document.getElementById("kart-cvv-inp").value = kart.cvv || "";

  document.querySelectorAll(".marka-btn").forEach(function(b) {
    b.classList.toggle("selected", b.dataset.marka === kart.marka);
  });
  document.querySelectorAll(".renk-btn").forEach(function(b) {
    b.classList.toggle("selected", b.dataset.renk === kart.renk);
  });

  form.style.display = "";
  document.getElementById("import-card").style.display = "none";
  form.scrollIntoView({ behavior: "smooth", block: "start" });
}

function dinleAnaEkran() {
  document.getElementById("btn-kart-ekle").addEventListener("click", function() {
    duzenleIdx = -1;
    document.getElementById("form-baslik").textContent = "Yeni Kart";
    formTemizle();
    var c = document.getElementById("cuzdan-form-card");
    c.style.display = c.style.display === "none" ? "" : "none";
    document.getElementById("import-card").style.display = "none";
  });

  document.getElementById("btn-kart-kaydet").addEventListener("click", kartEkleVeyaDuzenle);

  document.getElementById("btn-kart-iptal").addEventListener("click", function() {
    document.getElementById("cuzdan-form-card").style.display = "none";
    duzenleIdx = -1;
    formTemizle();
  });

  document.querySelectorAll(".renk-btn").forEach(function(btn) {
    btn.addEventListener("click", function() {
      document.querySelectorAll(".renk-btn").forEach(function(b) { b.classList.remove("selected"); });
      btn.classList.add("selected");
    });
  });
  document.querySelectorAll(".marka-btn").forEach(function(btn) {
    btn.addEventListener("click", function() {
      document.querySelectorAll(".marka-btn").forEach(function(b) { b.classList.remove("selected"); });
      btn.classList.add("selected");
    });
  });

  var numInp = document.getElementById("kart-numara-inp");
  numInp.addEventListener("input", function() {
    var v = numInp.value.replace(/\D/g,"").slice(0,19);
    var g = []; for (var i=0;i<v.length;i+=4) g.push(v.slice(i,i+4));
    numInp.value = g.join(" ");
  });
  var skInp = document.getElementById("kart-sk-inp");
  skInp.addEventListener("input", function() {
    var v = skInp.value.replace(/\D/g,"");
    if (v.length >= 2) v = v.slice(0,2)+"/"+v.slice(2,4);
    skInp.value = v;
  });
  document.getElementById("kart-cvv-inp").addEventListener("input", function() {
    this.value = this.value.replace(/\D/g,"").slice(0,4);
  });

  document.getElementById("btn-cuzdan-export").addEventListener("click", async function() {
    var yedek = localStorage.getItem("cuzdan_d") || "";
    if (!yedek) { showToast("Yedeklenecek kart yok!", "error"); return; }
    try { await navigator.clipboard.writeText(yedek); }
    catch(e) { var ta=document.createElement("textarea"); ta.value=yedek; document.body.appendChild(ta); ta.select(); document.execCommand("copy"); document.body.removeChild(ta); }
    showToast("📋 Yedek panoya kopyalandı! Güvenli bir yere kaydet.", "success");
  });

  document.getElementById("btn-cuzdan-import").addEventListener("click", function() {
    var c = document.getElementById("import-card");
    c.style.display = c.style.display === "none" ? "" : "none";
    document.getElementById("cuzdan-form-card").style.display = "none";
  });
  document.getElementById("btn-import-yap").addEventListener("click", async function() {
    var txt = document.getElementById("import-txt").value.trim();
    if (!txt) { showToast("Metin boş!", "error"); return; }
    var json = await coz(txt, aktifPin);
    if (!json) { showToast("❌ Hatalı yedek veya yanlış PIN!", "error"); return; }
    try {
      kartlar = JSON.parse(json);
      localStorage.setItem("cuzdan_d", txt);
      renderKartlar();
      document.getElementById("import-card").style.display = "none";
      showToast("✅ " + kartlar.length + " kart yüklendi!", "success");
    } catch(e) { showToast("Hatalı format!", "error"); }
  });
  document.getElementById("btn-import-iptal").addEventListener("click", function() {
    document.getElementById("import-card").style.display = "none";
  });
}

async function kartEkleVeyaDuzenle() {
  var isim  = (document.getElementById("kart-isim-inp").value||"").trim();
  var numara= (document.getElementById("kart-numara-inp").value||"").replace(/\s/g,"");
  var cvv   = (document.getElementById("kart-cvv-inp").value||"").trim();
  var sk    = (document.getElementById("kart-sk-inp").value||"").trim();
  var mb    = document.querySelector(".marka-btn.selected");
  var rb    = document.querySelector(".renk-btn.selected");
  if (!isim)            { showToast("Kart ismi gir!", "error"); return; }
  if (numara.length<13) { showToast("Kart numarası eksik!", "error"); return; }
  if (cvv.length<3)     { showToast("CVV gir!", "error"); return; }
  if (!sk)              { showToast("Son kullanma tarihi gir!", "error"); return; }

  var yeniKart = {
    isim: isim, numara: numara, cvv: cvv, son_kullanma: sk,
    marka: mb ? mb.dataset.marka : "diger",
    renk:  rb ? rb.dataset.renk  : "mavi",
    id: duzenleIdx >= 0 ? kartlar[duzenleIdx].id : Date.now()
  };

  if (duzenleIdx >= 0) {
    kartlar[duzenleIdx] = yeniKart;
    showToast("✅ Kart güncellendi!", "success");
  } else {
    kartlar.push(yeniKart);
    showToast("✅ Kart eklendi!", "success");
  }

  await kartlariKaydet();
  renderKartlar();
  formTemizle();
  document.getElementById("cuzdan-form-card").style.display = "none";
  duzenleIdx = -1;
}

function formTemizle() {
  ["kart-isim-inp","kart-numara-inp","kart-cvv-inp","kart-sk-inp"].forEach(function(id) {
    var e = document.getElementById(id); if(e) e.value="";
  });
  document.querySelectorAll(".marka-btn").forEach(function(b){b.classList.remove("selected");});
  document.querySelectorAll(".renk-btn").forEach(function(b){b.classList.remove("selected");});
  var ilk = document.querySelector(".renk-btn"); if(ilk) ilk.classList.add("selected");
  document.getElementById("form-baslik").textContent = "Yeni Kart";
}

function formatNo(n) {
  var t=n.replace(/\D/g,""); var g=[];
  for(var i=0;i<t.length;i+=4) g.push(t.slice(i,i+4));
  return g.join(" ");
}
function skDurum(sk) {
  if (!sk) return "ok";
  var p = sk.split("/"); if (p.length !== 2) return "ok";
  var ay = parseInt(p[0], 10), yil = parseInt(p[1], 10);
  if (isNaN(ay) || isNaN(yil)) return "ok";
  var tamYil = 2000 + yil;
  var sonGecerli = new Date(tamYil, ay, 0, 23, 59, 59);
  var bugun = new Date();
  if (sonGecerli < bugun) return "gecti";
  var ikiAy = new Date(); ikiAy.setMonth(ikiAy.getMonth() + 2);
  if (sonGecerli <= ikiAy) return "yakin";
  return "ok";
}
function escHTML(s) {
  return (s||"").replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;");
}
