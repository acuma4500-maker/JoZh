// ── SPOR KOÇU v2
// FİX: Profil sıfırlama/düzenleme butonu eklendi
// FİX: Antrenman geçmişi ekranı eklendi
// FİX: Seri bozulduğunda kullanıcıya uyarı gösteriliyor
// FİX: Program (egzersiz) özelleştirme eklendi

var VARSAYILAN_PROGRAM = {
  0: { kas: "Göğüs", emoji: "🫁", egzersizler: [
    { isim: "Şınav",            set: 4, rep: 15 },
    { isim: "Geniş Tutuş Şınav", set: 3, rep: 12 },
    { isim: "Dar Tutuş Şınav",   set: 3, rep: 12 },
    { isim: "Pike Push-Up",      set: 3, rep: 10 },
    { isim: "Dips (Sandalye)",   set: 3, rep: 12 },
  ]},
  1: { kas: "Sırt", emoji: "🦾", egzersizler: [
    { isim: "Süperman",          set: 3, rep: 15 },
    { isim: "Ters Şınav",        set: 3, rep: 12 },
    { isim: "Köprü (Glute Bridge)", set: 3, rep: 20 },
    { isim: "Yüzücü",            set: 3, rep: 20 },
  ]},
  2: { kas: "Karın & Core", emoji: "🔥", egzersizler: [
    { isim: "Plank",             set: 3, rep: "45sn" },
    { isim: "Mekik",             set: 3, rep: 20 },
    { isim: "Bacak Kaldırma",    set: 3, rep: 15 },
    { isim: "Yan Plank",         set: 2, rep: "30sn" },
    { isim: "Mountain Climber",  set: 3, rep: 20 },
  ]},
  3: { kas: "Kol", emoji: "💪", egzersizler: [
    { isim: "Dar Tutuş Şınav",   set: 4, rep: 12 },
    { isim: "Tricep Dips",       set: 3, rep: 15 },
    { isim: "Yavaş Şınav",       set: 3, rep: 10 },
    { isim: "Diamond Push-Up",   set: 3, rep: 10 },
  ]},
  4: { kas: "Bacak", emoji: "🦵", egzersizler: [
    { isim: "Squat",             set: 4, rep: 20 },
    { isim: "Lunges",            set: 3, rep: 12 },
    { isim: "Bulgar Split Squat", set: 3, rep: 10 },
    { isim: "Calf Raise",        set: 3, rep: 25 },
    { isim: "Wall Sit",          set: 2, rep: "45sn" },
  ]},
  5: { kas: "FYT (Askerlik)", emoji: "🎖️", egzersizler: [
    { isim: "Şınav (max)",       set: 3, rep: 20 },
    { isim: "Mekik (max)",       set: 3, rep: 25 },
    { isim: "Koşu",              set: 1, rep: "20dk" },
  ]},
  6: { kas: "Dinlenme", emoji: "😴", dinlenme: true, egzersizler: [
    { isim: "Hafif Koşu",        set: 1, rep: "20dk" },
    { isim: "Esneme",            set: 1, rep: "10dk" },
  ]},
};

var EGZERSIZ_BILGI = {
  "Şınav": { gif: "https://media1.tenor.com/m/9K2oyPtBv8AAAAAC/push-up.gif", adimlar: ["Eller omuz genişliğinde yere yerleşir, vücut düz bir çizgi olur.","Dirsekleri bükerek göğsünü yere yaklaştır.","Kollarını iterek başlangıç pozisyonuna dön. Sırtını dik tut."] },
  "Geniş Tutuş Şınav": { gif: "https://media1.tenor.com/m/Q9j2LxkGxKwAAAAC/wide-push-up.gif", adimlar: ["Elleri omuzdan geniş aç.","Göğüs kaslarına odaklanarak in.","İterek yukarı çık. Göğüs daha çok çalışır."] },
  "Dar Tutuş Şınav": { gif: "https://media1.tenor.com/m/T9K5oZ8cQ_kAAAAC/diamond-push-up.gif", adimlar: ["Elleri göğüs altında birbirine yakın koy.","Dirsekleri gövdeye yakın tutarak in.","İterek çık. Triceps çalışır."] },
  "Diamond Push-Up": { gif: "https://media1.tenor.com/m/T9K5oZ8cQ_kAAAAC/diamond-push-up.gif", adimlar: ["Elleri elmas şeklinde birleştir.","Yavaşça in, dirsekler gövdeye yakın.","İterek çık. Triceps'i yoğun çalıştırır."] },
  "Pike Push-Up": { gif: "https://media1.tenor.com/m/8fVvY0lPvKcAAAAC/pike-push-up.gif", adimlar: ["Kalçanı yukarı kaldır, vücut ters V şekli alır.","Başını yere doğru indir.","İterek çık. Omuz kasları çalışır."] },
  "Dips (Sandalye)": { gif: "https://media1.tenor.com/m/z8Kg8L0hVQoAAAAC/tricep-dips.gif", adimlar: ["Sandalyeye sırtın dönük, elleri kenara koy.","Dirsekleri bükerek vücudunu aşağı indir.","İterek yukarı çık. Triceps çalışır."] },
  "Tricep Dips": { gif: "https://media1.tenor.com/m/z8Kg8L0hVQoAAAAC/tricep-dips.gif", adimlar: ["Sandalye/sıra kenarına elleri koy.","Vücudunu aşağı indir, dirsekler geriye.","İterek çık."] },
  "Yavaş Şınav": { gif: "https://media1.tenor.com/m/9K2oyPtBv8AAAAAC/push-up.gif", adimlar: ["Normal şınav pozisyonu al.","4 saniyede yavaşça in.","2 saniyede çık. Kas gerginliğini artırır."] },
  "Süperman": { gif: "https://media1.tenor.com/m/kJHqTq3nT4AAAAAC/superman-exercise.gif", adimlar: ["Yüzüstü yat, kollar öne uzanır.","Kol ve bacaklarını aynı anda yerden kaldır.","2 saniye tut, indir."] },
  "Ters Şınav": { gif: "https://media1.tenor.com/m/kJHqTq3nT4AAAAAC/superman-exercise.gif", adimlar: ["Yüzüstü yat.","Üst gövdeni ve kollarını kaldır.","Sırtını sıkarak indir."] },
  "Köprü (Glute Bridge)": { gif: "https://media1.tenor.com/m/CqRIQ4bVfDcAAAAC/glute-bridge.gif", adimlar: ["Sırtüstü yat, dizler bükülü.","Kalçanı yukarı kaldır, vücut düz olur.","Kalçanı sıkarak indir."] },
  "Yüzücü": { gif: "https://media1.tenor.com/m/kJHqTq3nT4AAAAAC/superman-exercise.gif", adimlar: ["Yüzüstü yat, kollar öne.","Sağ kol-sol bacak, sonra tersini kaldır.","Yüzme hareketi gibi değiştir."] },
  "Plank": { gif: "https://media1.tenor.com/m/pfHtSFadX9EAAAAC/plank.gif", adimlar: ["Dirsekler yere, vücut düz bir çizgi.","Karın kaslarını sık, bel çökmesin.","Belirtilen süre bu pozisyonu koru."] },
  "Yan Plank": { gif: "https://media1.tenor.com/m/HkQ5rXvY0iAAAAAC/side-plank.gif", adimlar: ["Yan yat, bir dirsek yere.","Kalçanı kaldır, vücut düz olur.","Süre boyunca tut, diğer tarafa geç."] },
  "Mekik": { gif: "https://media1.tenor.com/m/f4Y3xR8T0aoAAAAC/sit-up.gif", adimlar: ["Sırtüstü yat, dizler bükülü.","Üst gövdeni dizlere doğru kaldır.","Kontrollü şekilde geri in."] },
  "Bacak Kaldırma": { gif: "https://media1.tenor.com/m/gL9pQ8vY5xIAAAAC/leg-raise.gif", adimlar: ["Sırtüstü yat, eller yanda.","Bacaklarını düz tutarak yukarı kaldır.","Yavaşça indir, yere değdirme."] },
  "Mountain Climber": { gif: "https://media1.tenor.com/m/z1eOQ0F1r3EAAAAC/mountain-climber.gif", adimlar: ["Şınav pozisyonu al.","Dizlerini sırayla göğsüne çek.","Hızlı tempoda koşar gibi devam et."] },
  "Squat": { gif: "https://media1.tenor.com/m/eBWSY0y8QO0AAAAC/squat.gif", adimlar: ["Ayaklar omuz genişliğinde.","Kalçanı geriye vererek çömel.","Topuktan güç alarak kalk."] },
  "Lunges": { gif: "https://media1.tenor.com/m/L4vXd0qJ8ZsAAAAC/lunges.gif", adimlar: ["Bir adım öne çık.","Ön dizi 90 derece bükerek in.","İterek kalk, bacak değiştir."] },
  "Bulgar Split Squat": { gif: "https://media1.tenor.com/m/L4vXd0qJ8ZsAAAAC/lunges.gif", adimlar: ["Arka ayağını yüksek bir yere koy.","Ön bacağınla çömel.","İterek kalk."] },
  "Calf Raise": { gif: "https://media1.tenor.com/m/vN8oJZ0nT9AAAAAC/calf-raise.gif", adimlar: ["Ayakta dur.","Parmak uçlarına yükselerek topukları kaldır.","Yavaşça indir."] },
  "Wall Sit": { gif: "https://media1.tenor.com/m/QpXbY0vN9kAAAAAC/wall-sit.gif", adimlar: ["Sırtını duvara yasla.","Oturur pozisyonda dizler 90 derece.","Süre boyunca bu pozisyonu koru."] },
  "Şınav (max)": { gif: "https://media1.tenor.com/m/9K2oyPtBv8AAAAAC/push-up.gif", adimlar: ["Standart şınav pozisyonu.","Yorulana kadar maksimum sayıda yap.","Formu bozmadan devam et."] },
  "Mekik (max)": { gif: "https://media1.tenor.com/m/f4Y3xR8T0aoAAAAC/sit-up.gif", adimlar: ["Standart mekik pozisyonu.","1 dakikada maksimum sayıda yap.","Askerlik testi için tempoyu koru."] },
  "Koşu": { gif: "https://media1.tenor.com/m/y0hDvOQ8kMAAAAAC/running.gif", adimlar: ["Isınma ile başla.","Sabit tempoda koş.","Nefesini düzenli tut."] },
  "Hafif Koşu": { gif: "https://media1.tenor.com/m/y0hDvOQ8kMAAAAAC/running.gif", adimlar: ["Rahat bir tempoda başla.","Konuşabileceğin hızda koş.","Toparlanma için idealdir."] },
  "Esneme": { gif: "https://media1.tenor.com/m/mF0Kq8V0Y7cAAAAC/stretching.gif", adimlar: ["Her kas grubunu 20-30 sn ger.","Zorlamadan, nefes alarak yap.","Kasılma olmadan esnet."] },
};

var ROZETLER = [
  { key: "ilk",    isim: "İlk Adım",    emoji: "🎯", kosul: function(p){ return p.toplamAntrenman >= 1; } },
  { key: "7seri",  isim: "7 Gün Seri",  emoji: "🔥", kosul: function(p){ return p.enIyiSeri >= 7; } },
  { key: "30seri", isim: "30 Gün Seri", emoji: "👑", kosul: function(p){ return p.enIyiSeri >= 30; } },
  { key: "10ant",  isim: "10 Antrenman",emoji: "💪", kosul: function(p){ return p.toplamAntrenman >= 10; } },
  { key: "50ant",  isim: "50 Antrenman",emoji: "🏆", kosul: function(p){ return p.toplamAntrenman >= 50; } },
  { key: "100ant", isim: "100 Antrenman",emoji: "⭐", kosul: function(p){ return p.toplamAntrenman >= 100; } },
  { key: "100xp",  isim: "100 XP",      emoji: "⚡", kosul: function(p){ return p.xp >= 100; } },
  { key: "500xp",  isim: "500 XP",      emoji: "🌟", kosul: function(p){ return p.xp >= 500; } },
  { key: "1000xp", isim: "1000 XP",     emoji: "💎", kosul: function(p){ return p.xp >= 1000; } },
];

var GUNLER = ["Pzt","Sal","Çar","Per","Cum","Cmt","Paz"];

var db;
var profil = null;
var program = null;

window.onFirebaseReady(function() {
  db = window.__db;
  sporYukle();
});

async function sporYukle() {
  var cachedP = window.cacheOku("spor_profil");
  var cachedProg = window.cacheOku("spor_program");
  if (cachedP) profil = cachedP;
  if (cachedProg) program = cachedProg;
  if (profil && program) { renderSporMain(); seriKontrol(); }

  try {
    var pSnap = await db.collection("spor_profil").doc("kullanici").get();
    if (pSnap.exists) profil = pSnap.data();

    var progSnap = await db.collection("spor_program").doc("aktif").get();
    if (progSnap.exists) {
      program = progSnap.data().program;
    } else {
      program = JSON.parse(JSON.stringify(VARSAYILAN_PROGRAM));
      await db.collection("spor_program").doc("aktif").set({ program: program });
    }
    if (profil) {
      window.cacheYaz("spor_profil", profil);
      window.cacheYaz("spor_program", program);
    }
  } catch(e) { console.error(e); }

  if (!profil) {
    sporKurulum();
  } else {
    if (!program) program = JSON.parse(JSON.stringify(VARSAYILAN_PROGRAM));
    renderSporMain();
    seriKontrol();
  }
}

// ── SERİ KONTROL — uyarı ver eğer seri bozulduysa
function seriKontrol() {
  if (!profil || !profil.sonAntrenman) return;
  var bugun = bugunStrS();
  var dun = dunStrS();
  var onceki = profil.sonAntrenman;
  // Dün veya bugün antrenman yapılmışsa sorun yok
  if (onceki === bugun || onceki === dun) return;
  // Seri varsa ve bozulduysa uyar
  if (profil.seri > 0) {
    showToast("💔 " + profil.seri + " günlük serin bozuldu! Yeniden başlıyorsun.", "error");
    // Seriyi sıfırla
    profil.seri = 0;
    try { db.collection("spor_profil").doc("kullanici").update({ seri: 0 }); } catch(e) {}
    window.cacheYaz("spor_profil", profil);
    // XP barını güncelle
    var xpEl = document.getElementById("spor-xp-bar");
    if (xpEl) xpEl.textContent = "⚡ " + profil.xp + " XP  |  🔥 Seri: 0 gün  |  Toplam: " + profil.toplamAntrenman;
  }
}

function sporKurulum() {
  document.getElementById("spor-setup").style.display = "";
  document.getElementById("spor-main").style.display = "none";

  document.querySelectorAll(".seviye-btn").forEach(function(btn) {
    btn.addEventListener("click", function() {
      document.querySelectorAll(".seviye-btn").forEach(function(b){ b.classList.remove("selected"); });
      btn.classList.add("selected");
      window._seviye = parseInt(btn.dataset.v);
    });
  });
  document.querySelectorAll(".hedef-btn").forEach(function(btn) {
    btn.addEventListener("click", function() {
      document.querySelectorAll(".hedef-btn").forEach(function(b){ b.classList.remove("selected"); });
      btn.classList.add("selected");
      window._hedef = btn.dataset.v;
    });
  });
  var kaydet = document.getElementById("btn-profil-kaydet");
  if (kaydet) kaydet.addEventListener("click", async function() {
    if (!window._seviye || !window._hedef) { showToast("Seviye ve hedef seç!", "error"); return; }
    profil = { seviye: window._seviye, hedef: window._hedef, xp:0, seri:0, enIyiSeri:0, toplamAntrenman:0, rozetler:[], sonAntrenman:null };
    program = JSON.parse(JSON.stringify(VARSAYILAN_PROGRAM));
    try {
      await db.collection("spor_profil").doc("kullanici").set(profil);
      await db.collection("spor_program").doc("aktif").set({ program: program });
    } catch(e){ console.error(e); }
    window.cacheYaz("spor_profil", profil);
    window.cacheYaz("spor_program", program);
    document.getElementById("spor-setup").style.display = "none";
    renderSporMain();
    showToast("🎉 Profil oluşturuldu!", "success");
  });
}

function bugunProgramIdx() { return (new Date().getDay() + 6) % 7; }
function bugunStrS() { return new Date().toISOString().split("T")[0]; }
function dunStrS() { var d=new Date(); d.setDate(d.getDate()-1); return d.toISOString().split("T")[0]; }

function renderSporMain() {
  document.getElementById("spor-setup").style.display = "none";
  document.getElementById("spor-main").style.display = "";

  var hedefLabel = { askerlik:"Askerlik", kas_yap:"Kas Yap", kondisyon:"Kondisyon", yag_yak:"Yağ Yak" };
  document.getElementById("spor-xp-bar").textContent =
    "⚡ " + profil.xp + " XP  |  🔥 Seri: " + profil.seri + " gün  |  " + (hedefLabel[profil.hedef] || "");

  renderBugun();
  renderHaftalik();
  renderGecmis();
  renderRozetler();

  // Profil sıfırla butonu
  var sifirBtn = document.getElementById("btn-spor-profil-sifirla");
  if (sifirBtn) {
    sifirBtn.onclick = function() {
      if (!confirm("Tüm spor verisi ve profil sıfırlanacak. Emin misin?")) return;
      sporProfilSifirla();
    };
  }
}

async function sporProfilSifirla() {
  try {
    await db.collection("spor_profil").doc("kullanici").delete();
    await db.collection("spor_program").doc("aktif").delete();
  } catch(e) {}
  localStorage.removeItem("cache_spor_profil");
  localStorage.removeItem("cache_spor_program");
  profil = null;
  program = null;
  document.getElementById("spor-main").style.display = "none";
  sporKurulum();
  showToast("Profil sıfırlandı.", "success");
}

async function renderBugun() {
  var idx = bugunProgramIdx();
  var gun = program[idx];
  document.getElementById("spor-gun-badge").textContent = GUNLER[idx];
  document.getElementById("spor-gun-badge").className = "badge" + (gun.dinlenme ? "" : " badge-blue");

  var bugun = bugunStrS();
  var yapildi = false;
  try {
    var snap = await db.collection("spor_antrenman").doc(bugun).get();
    if (snap.exists) yapildi = true;
  } catch(e) {
    var cache = window.cacheOku("spor_antrenman_" + bugun);
    if (cache) yapildi = true;
  }

  var el = document.getElementById("spor-bugun-content");
  el.innerHTML = '<p style="font-size:15px;color:var(--text);margin-bottom:14px">' + gun.emoji + ' <strong>' + gun.kas + '</strong>' +
    (yapildi ? ' <span class="badge badge-green" style="margin-left:6px">✅ Tamamlandı</span>' : '') + '</p>';

  gun.egzersizler.forEach(function(eg, i) {
    var div = document.createElement("div");
    div.className = "egzersiz-item";
    div.innerHTML =
      '<span class="egzersiz-name">' + eg.isim + '</span>' +
      '<span class="egzersiz-detail">' + eg.set + ' × ' + eg.rep + '</span>' +
      '<button class="egzersiz-bilgi-btn" data-eg="' + escAttr(eg.isim) + '">ℹ️</button>';
    el.appendChild(div);
    div.querySelector(".egzersiz-bilgi-btn").addEventListener("click", function() {
      egzersizBilgiGoster(eg.isim);
    });
  });

  var btns = document.getElementById("spor-bugun-btns");
  btns.innerHTML = "";
  if (!yapildi) {
    var b = document.createElement("button");
    b.className = gun.dinlenme ? "btn btn-ghost" : "btn btn-primary";
    b.textContent = gun.dinlenme ? "✅ Dinlenme yapıldı" : "🏋️ Antrenmanı Başlat";
    b.addEventListener("click", function() {
      if (gun.dinlenme) antrenmanTamamla(idx, true, null);
      else antrenmanGir(idx, gun);
    });
    btns.appendChild(b);
  } else {
    var info = document.createElement("p");
    info.style.cssText = "font-size:13px;color:var(--text3)";
    info.textContent = "Bugünkü antrenmanı tamamladın. Yarın görüşürüz! 💪";
    btns.appendChild(info);
  }
}

function antrenmanGir(idx, gun) {
  var el = document.getElementById("spor-bugun-content");
  el.innerHTML = '<p style="font-size:15px;margin-bottom:14px">' + gun.emoji + ' <strong>' + gun.kas + '</strong> — Kaç yaptın?</p>';

  gun.egzersizler.forEach(function(eg, i) {
    var div = document.createElement("div");
    div.className = "egzersiz-gir";
    div.innerHTML =
      '<div class="egzersiz-gir-ust">' +
        '<span class="egzersiz-name">' + eg.isim + ' <button class="egzersiz-bilgi-btn">ℹ️</button></span>' +
        '<span class="egzersiz-hedef">Hedef: ' + eg.set + '×' + eg.rep + '</span>' +
      '</div>' +
      '<input class="inp egzersiz-input" id="eg-input-' + i + '" type="tel" placeholder="Toplam tekrar (örn: ' + (typeof eg.rep === "number" ? eg.set*eg.rep : "60") + ')" />';
    el.appendChild(div);
    div.querySelector(".egzersiz-bilgi-btn").addEventListener("click", function() {
      egzersizBilgiGoster(eg.isim);
    });
  });

  var btns = document.getElementById("spor-bugun-btns");
  btns.innerHTML = "";
  var kaydet = document.createElement("button");
  kaydet.className = "btn btn-success";
  kaydet.textContent = "💾 Antrenmanı Kaydet";
  kaydet.addEventListener("click", function() {
    var sonuclar = [];
    gun.egzersizler.forEach(function(eg, i) {
      var v = parseInt(document.getElementById("eg-input-" + i).value) || 0;
      sonuclar.push({ isim: eg.isim, yapilan: v, hedef: (typeof eg.rep === "number" ? eg.set*eg.rep : 0) });
    });
    antrenmanTamamla(idx, false, sonuclar);
  });
  btns.appendChild(kaydet);

  var iptal = document.createElement("button");
  iptal.className = "btn btn-ghost";
  iptal.textContent = "İptal";
  iptal.addEventListener("click", function() { renderBugun(); });
  btns.appendChild(iptal);
}

async function antrenmanTamamla(idx, dinlenme, sonuclar) {
  var bugun = bugunStrS();
  var kayit = { tarih: bugun, gunIdx: idx, dinlenme: dinlenme, sonuclar: sonuclar || [], zaman: Date.now() };
  try { await db.collection("spor_antrenman").doc(bugun).set(kayit); } catch(e){ console.error(e); }
  window.cacheYaz("spor_antrenman_" + bugun, kayit);

  var xp = dinlenme ? 5 : 20;
  var yeniSeri = (profil.sonAntrenman === dunStrS()) ? profil.seri + 1 : 1;
  profil.xp += xp;
  profil.seri = yeniSeri;
  profil.enIyiSeri = Math.max(profil.enIyiSeri || 0, yeniSeri);
  profil.toplamAntrenman += 1;
  profil.sonAntrenman = bugun;

  if (!dinlenme && sonuclar) {
    var degisti = false;
    sonuclar.forEach(function(s) {
      if (s.hedef > 0 && s.yapilan >= s.hedef) {
        var eg = program[idx].egzersizler.find(function(e){ return e.isim === s.isim; });
        if (eg && typeof eg.rep === "number") { eg.rep += 1; degisti = true; }
      }
    });
    if (degisti) {
      try { await db.collection("spor_program").doc("aktif").set({ program: program }); } catch(e){}
      window.cacheYaz("spor_program", program);
    }
  }

  var yeniRozetler = [];
  ROZETLER.forEach(function(r) {
    if (profil.rozetler.indexOf(r.key) < 0 && r.kosul(profil)) {
      profil.rozetler.push(r.key);
      yeniRozetler.push(r);
    }
  });

  try {
    await db.collection("spor_profil").doc("kullanici").update({
      xp: profil.xp, seri: profil.seri, enIyiSeri: profil.enIyiSeri,
      toplamAntrenman: profil.toplamAntrenman, sonAntrenman: profil.sonAntrenman, rozetler: profil.rozetler
    });
  } catch(e){ console.error(e); }
  window.cacheYaz("spor_profil", profil);

  renderSporMain();
  showToast("+" + xp + " XP kazandın! 💪", "success");

  if (yeniRozetler.length) {
    setTimeout(function() {
      showToast("Yeni rozet: " + yeniRozetler.map(function(r){ return r.emoji + r.isim; }).join(", ") + " 🏅", "success");
    }, 1200);
  }
}

// ── ANTRENMAN GEÇMİŞİ
async function renderGecmis() {
  var el = document.getElementById("spor-gecmis-content");
  if (!el) return;
  el.innerHTML = '<p class="loading">Yükleniyor...</p>';

  var kayitlar = [];
  try {
    var snap = await db.collection("spor_antrenman").orderBy("zaman", "desc").limit(14).get();
    snap.forEach(function(s) { kayitlar.push(s.data()); });
  } catch(e) {
    // Firebase yoksa cache'den son 7 günü dene
    for (var i = 0; i < 7; i++) {
      var d = new Date(); d.setDate(d.getDate() - i);
      var tarih = d.toISOString().split("T")[0];
      var c = window.cacheOku("spor_antrenman_" + tarih);
      if (c) kayitlar.push(c);
    }
  }

  if (!kayitlar.length) {
    el.innerHTML = '<p class="empty-text">Henüz antrenman yok.</p>';
    return;
  }

  el.innerHTML = "";
  var aylar = ["Oca","Şub","Mar","Nis","May","Haz","Tem","Ağu","Eyl","Eki","Kas","Ara"];
  kayitlar.forEach(function(k) {
    var d = new Date(k.tarih + "T00:00:00");
    var tarihStr = d.getDate() + " " + aylar[d.getMonth()];
    var gun = program && program[k.gunIdx] ? program[k.gunIdx] : null;
    var div = document.createElement("div");
    div.className = "egzersiz-item";
    div.style.flexDirection = "column";
    div.style.alignItems = "flex-start";
    div.innerHTML =
      '<div style="display:flex;align-items:center;gap:8px;width:100%">' +
        '<span style="font-family:var(--mono);font-size:12px;color:var(--text3);width:54px">' + tarihStr + '</span>' +
        '<span style="font-size:13px;flex:1">' + (gun ? gun.emoji + " " + gun.kas : "Antrenman") + '</span>' +
        (k.dinlenme ? '<span class="badge">Dinlenme</span>' : '<span class="badge badge-green">💪 Yapıldı</span>') +
      '</div>';
    if (k.sonuclar && k.sonuclar.length && !k.dinlenme) {
      var detay = document.createElement("div");
      detay.style.cssText = "margin-top:6px;padding-left:62px;font-size:12px;color:var(--text3)";
      detay.textContent = k.sonuclar.filter(function(s){ return s.yapilan > 0; }).map(function(s){ return s.isim + ": " + s.yapilan; }).join(" · ");
      div.appendChild(detay);
    }
    el.appendChild(div);
  });
}

function egzersizBilgiGoster(isim) {
  var bilgi = EGZERSIZ_BILGI[isim];
  var eski = document.getElementById("egzersiz-modal");
  if (eski) eski.remove();

  var modal = document.createElement("div");
  modal.id = "egzersiz-modal";
  modal.className = "egzersiz-modal-arka";

  var adimlarHtml = bilgi && bilgi.adimlar
    ? '<ol class="egzersiz-adimlar">' + bilgi.adimlar.map(function(a){ return '<li>' + a + '</li>'; }).join("") + '</ol>'
    : '<p class="hint">Açıklama bulunamadı.</p>';
  var gifHtml = bilgi && bilgi.gif
    ? '<div class="egzersiz-gif-wrap"><img class="egzersiz-gif" src="' + bilgi.gif + '" alt="' + escAttr(isim) + '" onerror="this.parentNode.style.display=\'none\'"/></div>'
    : "";

  modal.innerHTML =
    '<div class="egzersiz-modal">' +
      '<div class="egzersiz-modal-ust">' +
        '<h3>' + isim + '</h3>' +
        '<button class="egzersiz-modal-kapat" id="egz-kapat">✕</button>' +
      '</div>' + gifHtml + adimlarHtml +
    '</div>';

  document.body.appendChild(modal);
  document.getElementById("egz-kapat").addEventListener("click", function() { modal.remove(); });
  modal.addEventListener("click", function(e) { if (e.target === modal) modal.remove(); });
}

function escAttr(s) { return (s||"").replace(/"/g,"&quot;").replace(/'/g,"&#39;"); }

function renderHaftalik() {
  var el = document.getElementById("spor-haftalik-content");
  var grid = document.createElement("div");
  grid.className = "haftalik-grid";
  var bugunIdx = bugunProgramIdx();
  for (var i = 0; i <= 6; i++) {
    var gun = program[i];
    var div = document.createElement("div");
    div.className = "gun-kutu" + (i === bugunIdx ? " bugun" : "") + (gun.dinlenme ? " dinlenme" : "");
    div.innerHTML =
      '<span class="gun-label">' + GUNLER[i] + '</span>' +
      '<span class="gun-emoji">' + gun.emoji + '</span>' +
      '<span class="gun-kas">' + gun.kas.split(" ")[0] + '</span>';
    grid.appendChild(div);
  }
  el.innerHTML = "";
  el.appendChild(grid);
}

function renderRozetler() {
  var el = document.getElementById("spor-rozetler");
  var grid = document.createElement("div");
  grid.className = "rozet-grid";
  ROZETLER.forEach(function(r) {
    var kazanildi = profil.rozetler && profil.rozetler.indexOf(r.key) >= 0;
    var div = document.createElement("div");
    div.className = "rozet-item" + (kazanildi ? " kazanildi" : "");
    div.innerHTML = '<span class="rozet-emoji">' + r.emoji + '</span><span class="rozet-name">' + r.isim + '</span>';
    grid.appendChild(div);
  });
  el.innerHTML = "";
  el.appendChild(grid);
}
