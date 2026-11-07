// Duman testi: node tests/duman.js yayin/kervan.html [ekran-goruntusu.png]
const { chromium } = require("playwright");
const path = require("path");
const url = "file://" + path.resolve(process.argv[2]);
const hata = m => { console.error("DUMAN HATA: " + m); process.exit(1); };

(async () => {
  const b = await chromium.launch();
  const ctx = await b.newContext({ viewport: { width: 375, height: 812 } });
  await ctx.route(/fonts\.(googleapis|gstatic)\.com/, r => r.abort());
  const p = await ctx.newPage();
  const konsol = [];
  p.on("pageerror", e => konsol.push(e.message));
  await p.goto(url);
  for (const h of ["#bolumler", "#rota", "#karakterler", "#kasa", "#profil", "#b01"]) {
    await p.evaluate(x => { location.hash = x; }, h);
    await p.waitForTimeout(150);
    const w = await p.evaluate(() => document.documentElement.scrollWidth);
    if (w > 375) hata(h + " yatay taşma: " + w);
  }
  const n = await p.locator(".scene").count();
  if (n !== 15) hata("B01'de " + n + " senaryo kartı");
  const btn = p.locator(".scene [data-kopya]").first();
  await btn.click();
  await p.waitForTimeout(200);
  const t = await btn.textContent();
  if (!/Kopyalandı|uzun basıp/.test(t)) hata("Kopyala tepki vermedi: " + t);
  await p.locator(".scene [data-made]").first().click();
  if (process.argv[3]) { await p.evaluate(() => { location.hash = "#b01"; }); await p.screenshot({ path: process.argv[3] }); }
  if (konsol.length) hata("sayfa hatası: " + konsol.join(" | "));

  // localStorage kapalıyken de açılmalı
  const ctx2 = await b.newContext({ viewport: { width: 375, height: 812 } });
  await ctx2.addInitScript(() => {
    Object.defineProperty(window, "localStorage", { get() { throw new Error("engelli"); } });
  });
  const p2 = await ctx2.newPage();
  const k2 = [];
  p2.on("pageerror", e => k2.push(e.message));
  await p2.goto(url);
  const satir = await p2.locator(".row").count();
  if (satir !== 50 || k2.length) hata("localStorage yokken: " + satir + " satır, " + k2.join(" | "));
  await b.close();
  console.log("DUMAN: TAMAM");
})().catch(e => hata(e.message));
