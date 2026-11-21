// SVG ikondan PNG ikonlar üretir (Playwright/Chromium). Çalıştırma: node tools/make-icons.cjs
const { chromium } = require('playwright');
const fs = require('fs'); const path = require('path');
const svg = fs.readFileSync(path.join(__dirname, '../assets/icons/icon.svg'), 'utf8');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  const shots = [
    ['icon-192.png', 192, 1, false], ['icon-512.png', 512, 1, false],
    ['apple-touch-icon.png', 180, 1, true], ['maskable-512.png', 512, 0.72, true],
  ];
  for (const [name, size, scale, fullBleed] of shots) {
    const inner = Math.round(size * scale);
    await page.setViewportSize({ width: size, height: size });
    await page.setContent(`<html><body style="margin:0;width:${size}px;height:${size}px;display:grid;place-items:center;background:${fullBleed ? '#FFF0E6' : 'transparent'}">
      <div style="width:${inner}px;height:${inner}px">${svg.replace('<svg ', `<svg width="${inner}" height="${inner}" `)}</div></body></html>`);
    await page.screenshot({ path: path.join(__dirname, '../assets/icons', name), omitBackground: !fullBleed });
  }
  await browser.close();
  console.log('ikonlar üretildi');
})();
