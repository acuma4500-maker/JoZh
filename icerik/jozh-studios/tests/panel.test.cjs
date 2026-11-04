/* JOZH STUDIOS paneli uçtan uca testi.  Kullanım: node jozh-studios/tests/panel.test.cjs
   Playwright ve Chromium ortamda kurulu olmalı. Panel file:// ile açılır (sunucu gerekmez). */
const { chromium } = require("playwright");
const path = require("path");
const fs = require("fs");
const os = require("os");

const URL = "file://" + path.resolve(__dirname, "..", "index.html");
let pass = 0, fail = 0;
const ok = (c, m) => { if (c) { pass++; console.log("  ✓ " + m); } else { fail++; console.log("  ✗ " + m); } };

(async () => {
  const browser = await chromium.launch();
  const ctx = await browser.newContext({ viewport: { width: 1280, height: 900 }, acceptDownloads: true });
  const page = await ctx.newPage();
  const errors = [];
  page.on("pageerror", e => errors.push(e.message));
  page.on("console", m => { if (m.type() === "error") errors.push(m.text()); });
  const go = async h => { await page.goto(URL + h); await page.waitForSelector("#view h1, #view .brand"); };
  const overflow = () => page.evaluate(() => document.documentElement.scrollWidth - innerWidth);

  console.log("1) Menüler ve sayfalar");
  await go("#/");
  await page.evaluate(() => localStorage.clear());
  await go("#/");
  const navs = await page.$$eval("#nav a", a => a.map(x => x.getAttribute("href")));
  ok(navs.length >= 15, "yan menüde " + navs.length + " bağlantı");
  for (const h of navs) {
    await go(h);
    const t = await page.textContent("#view");
    ok(t.length > 200 && !/Sayfa bulunamadı/.test(t), "açılıyor: " + h);
  }
  const ana = await page.goto(URL + "#/").then(() => page.textContent("#view"));
  ok(/87/.test(ana) && /81 \/ 81/.test(ana) && /100\.000 TL/.test(ana), "ana sayfada video, şehir ve başlangıç kasası");

  console.log("2) Bölgeler ve şehirler");
  const data = await page.evaluate(() => window.JOZH_DATA);
  ok(data.bolumler.length === 87, "87 bölüm");
  const sehirSay = {}; data.sehirler.forEach(s => sehirSay[s.bolge] = (sehirSay[s.bolge] || 0) + 1);
  const beklenen = { marmara: 11, ege: 8, akdeniz: 8, icanadolu: 13, karadeniz: 18, dogu: 14, guneydogu: 9 };
  ok(Object.keys(beklenen).every(k => sehirSay[k] === beklenen[k]), "bölge başına il sayısı doğru (11/8/8/13/18/14/9)");
  for (const sz of data.sezonlar.filter(s => s.bolge)) {
    await go("#/bolge/" + sz.bolge);
    const liste = await page.$$eval(".cities .city-b b", b => b.map(x => x.textContent));
    ok(JSON.stringify(liste) === JSON.stringify(sz.rota), sz.bolge + ": " + liste.length + " şehir rota sırasıyla");
    const yanlis = sz.rota.filter(il => data.sehirler.find(s => s.ad === il).bolge !== sz.bolge);
    ok(yanlis.length === 0, sz.bolge + ": bütün iller doğru bölgede");
  }
  await page.click(".cities a.card.city >> nth=0");
  await page.waitForSelector(".ep-card");
  await page.click(".ep-card");
  await page.waitForSelector(".scene");
  ok((await page.$$(".scene")).length === 6, "şehirden videoya geçiş, 6 sahne");

  console.log("3) Bütün videolar");
  let sahneToplam = 0, kasaKutu = 0, bos = 0;
  for (const b of data.bolumler) {
    await go("#/video/" + b.no);
    const n = await page.$$eval(".scene", x => x.length);
    sahneToplam += n;
    kasaKutu += await page.$$eval(".kasa-ara", x => x.length);
    const p = await page.evaluate(no => window.JOZH.sahnePrompt(window.JOZH.EP.get(no), window.JOZH.EP.get(no).sahneler[0]), b.no);
    const basliklar = ["VIDEO FORMAT", "VISUAL STYLE", "CHARACTER DEFINITIONS", "LOCATION", "TIME AND LIGHT", "BACKGROUND", "ACTION", "CAMERA", "DIALOGUE", "LIP SYNC", "PHYSICS", "AUDIO", "AVOID"];
    if (!basliklar.every(x => p.includes(x))) bos++;
    const sos = await page.$$eval(".social .tbox", x => x.length);
    if (n !== 6 || sos !== 6) bos++;
  }
  ok(sahneToplam === 522, "toplam 522 sahne kartı");
  ok(kasaKutu === 6 * 83 + 1, "kasa kutusu sayısı " + kasaKutu + " (Video 4 sahne 6'dan itibaren her sahne)");
  ok(bos === 0, "her videoda 13 başlıklı prompt, 6 sahne, 6 sosyal medya alanı");

  console.log("4) Kopyalama");
  await ctx.grantPermissions(["clipboard-read", "clipboard-write"]);
  await go("#/video/12");
  await page.click("#s-12-3 [data-copy='12-3']");
  await page.waitForTimeout(200);
  const pano = await page.evaluate(() => navigator.clipboard.readText());
  const beklenenP = await page.evaluate(() => window.JOZH.sahnePrompt(window.JOZH.EP.get(12), window.JOZH.EP.get(12).sahneler[2]));
  ok(pano === beklenenP, "sahne prompt'u panoya birebir kopyalandı");
  ok(!pano.includes("SAHNE 04") && pano.startsWith("VIDEO FORMAT"), "yalnızca ilgili prompt kopyalandı");
  await page.click("[data-copy='12-3-kasa']");
  await page.waitForTimeout(150);
  const kp = await page.evaluate(() => navigator.clipboard.readText());
  ok(/PURE SOLID BLACK/.test(kp) && /KASA/.test(kp), "kasa prompt'u kopyalandı");
  await page.click("[data-copy='12-ig']");
  await page.waitForTimeout(150);
  ok(/#JozhStudios/.test(await page.evaluate(() => navigator.clipboard.readText())), "Instagram açıklaması kopyalandı");

  console.log("5) Kasa hesapları");
  const d0 = await page.evaluate(() => { const d = window.JOZH.defter(); return { g: d.guncel, net: d.net, borc: d.toplam.borc, kontrol: d.kontrol, eksi: !!d.eksi }; });
  ok(d0.kontrol && !d0.eksi, "başlangıç + net kâr − borç = güncel bakiye, eksiye düşen an yok");
  ok(d0.borc === 800000, "senaryodaki borç ödemeleri 800.000 TL");
  // senaryo içi zincir kontrolü
  const zincir = await page.evaluate(() => window.JOZH.defter().entries.every((e, i, a) => i === 0 || e.onceki === a[i - 1].sonraki));
  ok(zincir, "her işlemin önceki bakiyesi bir öncekinin yeni bakiyesi");
  await go("#/kasa?no=10");
  await page.selectOption("#islem-form select[name=sahne]", "6");
  await page.selectOption("#islem-form select[name=tip]", "satis");
  await page.fill("#islem-form input[name=tutar]", "12.500");
  await page.fill("#islem-form input[name=aciklama]", "Test satışı");
  await page.click("#islem-form button[type=submit]");
  await page.waitForSelector("#sonuc");
  const d1 = await page.evaluate(() => window.JOZH.defter().guncel);
  ok(d1 === d0.g + 12500, "satış eklenince güncel bakiye +12.500");
  const sonuc = await page.textContent("#sonuc");
  ok(/Önceki bakiye/.test(sonuc) && /Yeni bakiye/.test(sonuc) && /Artış/.test(sonuc), "sonuç kartı: önceki, miktar, yeni, durum");
  const sb = await page.evaluate(() => { const x = window.JOZH.sahneBakiye().get("10-6"); return x.son - x.bas; });
  ok(sb === 12500 + (await page.evaluate(() => { const x = window.JOZH.EP.get(10).sahneler[5].tx; return x.reduce((a, t) => a + window.JOZH_DATA.tipler[t.tip].isaret * t.tutar, 0); })), "işlem ilgili sahnenin kasa klibine yansıdı");
  // mükerrer
  await page.selectOption("#islem-form select[name=no]", "10");
  await page.selectOption("#islem-form select[name=sahne]", "6");
  await page.selectOption("#islem-form select[name=tip]", "satis");
  await page.fill("#islem-form input[name=tutar]", "12500");
  await page.fill("#islem-form input[name=aciklama]", "Test satışı");
  await page.click("#islem-form button[type=submit]");
  ok(/zaten kayıtlı/.test(await page.textContent("#form-err")), "mükerrer işlem engellendi");
  ok((await page.evaluate(() => JSON.parse(localStorage.getItem("jozh-studios:v1")).islemler.length)) === 1, "depoda tek kayıt");
  // eksiye düşürme
  await page.selectOption("#islem-form select[name=no]", "5");
  await page.selectOption("#islem-form select[name=tip]", "diger_gider");
  await page.fill("#islem-form input[name=tutar]", "500.000");
  await page.fill("#islem-form input[name=aciklama]", "Çok büyük gider");
  await page.click("#islem-form button[type=submit]");
  ok(/eksiye düşürür/.test(await page.textContent("#form-err")), "kasayı eksiye düşüren işlem engellendi");
  // serbest prompt
  await page.fill("#serbest-form input[name=a]", "100.000");
  await page.fill("#serbest-form input[name=b]", "102.500");
  await page.click("#serbest-form button[type=submit]");
  const sp = await page.textContent("#serbest-sonuc");
  ok(/\+2\.500/.test(sp) && /#00E676/.test(sp), "serbest kasa prompt'u: yeşil +2.500");
  await page.fill("#serbest-form input[name=b]", "95.000");
  await page.click("#serbest-form button[type=submit]");
  ok(/-5\.000 TL/.test(await page.textContent("#serbest-sonuc")) && /#FF1744/.test(await page.textContent("#serbest-sonuc")), "serbest kasa prompt'u: kırmızı −5.000");
  await page.fill("#serbest-form input[name=b]", "100.000");
  await page.click("#serbest-form button[type=submit]");
  ok(/There is NO change line/.test(await page.textContent("#serbest-sonuc")), "serbest kasa prompt'u: sabit");

  console.log("6) Yenileme ve kalıcılık");
  await page.reload(); await page.waitForSelector("#view h1");
  ok((await page.evaluate(() => window.JOZH.defter().guncel)) === d1, "sayfa yenilenince işlem korunuyor");
  await go("#/video/7");
  await page.check("[data-made='7-1']");
  await page.fill("[data-note='7']", "test notu");
  await page.waitForTimeout(500);
  await page.reload(); await page.waitForSelector(".scene");
  ok(await page.isChecked("[data-made='7-1']"), "üretildi işareti korunuyor");
  ok((await page.inputValue("[data-note='7']")) === "test notu", "not korunuyor");

  console.log("7) Görsel yükleme");
  const pngUrl = await page.evaluate(() => { const c = document.createElement("canvas"); c.width = 90; c.height = 160; const x = c.getContext("2d"); x.fillStyle = "#d9ad55"; x.fillRect(0, 0, 90, 160); return c.toDataURL("image/png"); });
  const png = Buffer.from(pngUrl.split(",")[1], "base64");
  const tmp = path.join(os.tmpdir(), "jozh-test-kapak.png"); fs.writeFileSync(tmp, png);
  await page.setInputFiles("[data-upload='7-kapak']", tmp);
  await page.waitForSelector(".slot[data-slot='7-kapak'] img");
  await page.reload(); await page.waitForSelector(".scene");
  ok(!!(await page.$(".slot[data-slot='7-kapak'] img")), "kapak görseli yüklendi ve korunuyor");

  console.log("8) JSON dışa / içe aktarma");
  await go("#/veri");
  const [dl] = await Promise.all([page.waitForEvent("download"), page.click("#disa")]);
  const dosya = await dl.path();
  const j = JSON.parse(fs.readFileSync(dosya, "utf8"));
  ok(j.uygulama && j.durum.islemler.length === 1 && j.durum.uretildi.includes("7-1") && j.gorseller["7-kapak"], "dışa aktarılan JSON işlemleri, işaretleri ve görseli içeriyor");
  page.once("dialog", d => d.accept());
  await page.click("#sifirla");
  await page.waitForTimeout(200);
  ok((await page.evaluate(() => window.JOZH.defter().guncel)) === d0.g, "sıfırlayınca senaryo bakiyesine dönüldü");
  const kopya = path.join(os.tmpdir(), "jozh-yedek.json"); fs.copyFileSync(dosya, kopya);
  await page.setInputFiles("#ice", kopya);
  await page.waitForSelector("#ice-uygula");
  await page.click("#ice-uygula");
  await page.waitForTimeout(200);
  ok((await page.evaluate(() => window.JOZH.defter().guncel)) === d1, "içe aktarınca işlem ve bakiye geri geldi");
  fs.writeFileSync(kopya, "{bozuk json");
  await go("#/veri");
  await page.setInputFiles("#ice", kopya);
  await page.waitForSelector("#ice-sonuc .form-err");
  ok(/geçerli bir JSON değil/.test(await page.textContent("#ice-sonuc")), "bozuk dosya reddedildi");
  // işlem silme
  await go("#/kasa?f=kullanici");
  page.once("dialog", d => d.accept());
  await page.click("[data-del]");
  await page.waitForTimeout(200);
  ok((await page.evaluate(() => window.JOZH.defter().guncel)) === d0.g, "kullanıcı işlemi silinebildi");

  console.log("9) Mobil görünüm");
  for (const w of [320, 375, 390, 430]) {
    await page.setViewportSize({ width: w, height: 800 });
    let maks = 0;
    for (const h of ["#/", "#/biblio", "#/karakterler", "#/bolgeler", "#/bolge/karadeniz", "#/sehir/44", "#/video/4", "#/video/53", "#/video/87", "#/kasa", "#/veri", "#/rehber"]) {
      await go(h); maks = Math.max(maks, await overflow());
    }
    ok(maks <= 0, w + " px genişlikte yatay taşma yok");
  }
  await page.setViewportSize({ width: 390, height: 800 });
  await go("#/");
  ok(!(await page.isVisible("#nav a[href='#/kasa']")) || (await page.evaluate(() => getComputedStyle(document.querySelector(".sidebar")).transform)) !== "none", "mobilde menü kapalı başlıyor");
  await page.click("#menu-btn");
  await page.waitForTimeout(350);
  ok(await page.evaluate(() => document.body.classList.contains("menu-open")), "menü butonu menüyü açıyor");
  await page.click("#nav a[href='#/kasa']");
  await page.waitForTimeout(350);
  ok(!(await page.evaluate(() => document.body.classList.contains("menu-open"))) && /Kasa/.test(await page.title()), "menüden gidince menü kapanıyor");
  const kucuk = await page.$$eval("#view button, #view .btn, #nav a", els => els.filter(e => e.offsetParent && e.getBoundingClientRect().height < 36).length);
  ok(kucuk === 0, "dokunmatik hedefler en az 36 px");

  ok(errors.length === 0, "konsol hatası yok" + (errors.length ? ": " + errors.slice(0, 3).join(" | ") : ""));
  await browser.close();
  console.log(`\nSONUÇ: ${pass} geçti, ${fail} kaldı`);
  process.exit(fail ? 1 : 0);
})().catch(e => { console.error(e); process.exit(1); });
