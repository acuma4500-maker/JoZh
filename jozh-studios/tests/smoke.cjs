(async () => {
const { chromium } = require("playwright");
const url = "file://" + process.argv[2];
const b = await chromium.launch();
const p = await b.newPage({ viewport: { width: 390, height: 844 } });
const errs = [];
p.on("pageerror", e => errs.push(e.message)); p.on("console", m => { if (m.type() === "error") errs.push(m.text()); });
for (const h of ["#/", "#/biblio", "#/karakterler", "#/rehber", "#/bolgeler", "#/baslangic", "#/video/1", "#/video/4", "#/video/5", "#/kasa", "#/veri"]) {
  await p.goto(url + h); await p.waitForTimeout(150);
  const w = await p.evaluate(() => [document.documentElement.scrollWidth, innerWidth]);
  console.log(h, (await p.title()), w[0] > w[1] ? "TAŞMA " + w : "ok");
}
console.log(await p.evaluate(() => JOZH.sahnePrompt(JOZH.EP.get(3), JOZH.EP.get(3).sahneler[1])));
console.log("HATALAR:", errs);
await b.close();
})();
