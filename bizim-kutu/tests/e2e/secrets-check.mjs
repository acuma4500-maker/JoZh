// Uçtan uca test: iki gerçek tarayıcı (Cuma & İlayda) + Firebase Emülatörleri (Auth, Firestore, RTDB).
// Çalıştırma: npm run test:e2e   (firebase emulators:exec içinde çalışır; ayrıntı README'de)
import { spawn, execSync } from 'node:child_process';
import { createRequire } from 'node:module';
// Playwright yerel ya da global kurulumdan yüklenir.
const require = createRequire(import.meta.url);
const pw = (() => { try { return require('playwright'); } catch { return require(`${execSync('npm root -g').toString().trim()}/playwright`); } })();
const { chromium, devices } = pw;
import { fileURLToPath } from 'node:url';
import assert from 'node:assert/strict';

const A = 'pt0Kmbc9rqdJekFyvA1wLItUnxw1', B = 'cf6RqCRF6dPEWtSR1L9Dm2Uv4Ap1';
const PINS = { cuma: '0111', ilayda: '2222' }; // test PIN'leri (gerçekleri değil)
const PORT = 5174;
const BASE = `http://127.0.0.1:${PORT}/?emulator`;
const SHOTS = process.env.SHOTS_DIR || '';
const results = [];
let failures = 0;
const live = {};

async function step(name, fn) {
  const t0 = Date.now();
  try { await fn(); results.push(`✅ ${name} (${Date.now() - t0} ms)`); }
  catch (e) { failures++; if (SHOTS) for (const [n, pg] of Object.entries(live)) await pg.screenshot({ path: `${SHOTS}/fail-${failures}-${n}.png` }).catch(() => {}); results.push(`❌ ${name}\n     ${String(e.message).split('\n').slice(0, 4).join('\n     ')}`); }
  console.log(results.at(-1));
}

async function seed() {
  // Temiz başlangıç + emülatöre test PIN'lerini (secrets/pins) yerleştir
  await fetch('http://127.0.0.1:9099/emulator/v1/projects/jozh-love/accounts', { method: 'DELETE' });
  await fetch('http://127.0.0.1:8080/emulator/v1/projects/jozh-love/databases/(default)/documents', { method: 'DELETE' });
  const pins = { [A]: Number(PINS.cuma), [B]: Number(PINS.ilayda) }; // konsoldaki gibi sayı
  await fetch('http://127.0.0.1:9000/.json?ns=jozh-love-default-rtdb', { method: 'PUT', headers: { Authorization: 'Bearer owner' }, body: JSON.stringify({ secrets: { pins } }) });
  const r = await fetch('http://127.0.0.1:8080/v1/projects/jozh-love/databases/(default)/documents/secrets/pins', {
    method: 'PATCH', headers: { Authorization: 'Bearer owner', 'Content-Type': 'application/json' },
    body: JSON.stringify({ fields: { [A]: { stringValue: `“${PINS.cuma}”` }, [B]: { stringValue: PINS.ilayda } } }), // bilerek eğik tırnaklı
  });
  if (!r.ok) throw new Error('secrets yazılamadı: ' + await r.text());
}

async function firestoreDocs(path) {
  const r = await fetch(`http://127.0.0.1:8080/v1/projects/jozh-love/databases/(default)/documents/${path}`, { headers: { Authorization: 'Bearer owner' } });
  return r.json();
}

const server = spawn(process.execPath, [fileURLToPath(new URL('../../tools/serve.mjs', import.meta.url)), String(PORT)], { stdio: 'ignore' });
await new Promise((r) => setTimeout(r, 600));
const browser = await chromium.launch();
const errors = [];
async function newUser(device) {
  const ctx = await browser.newContext({ ...device, locale: 'tr-TR', timezoneId: 'Europe/Istanbul' });
  const page = await ctx.newPage();
  page.setDefaultTimeout(12000);
  page.on('pageerror', (e) => errors.push(`pageerror: ${e.message}`));
  page.on('console', (m) => { if (m.type() === 'error' && !/permission|PERMISSION|ERR_|Failed to load resource|WebChannel|transport errored/i.test(m.text())) errors.push(`console: ${m.text()}`); });
  return { ctx, page };
}
const shot = async (page, name) => { if (SHOTS) await page.screenshot({ path: `${SHOTS}/${name}.png` }); };

async function enterPin(page, pin) {
  for (const d of pin) await page.locator('.pin-key', { hasText: d }).first().click();
}
async function login(page, who, { pin, expectError } = {}) {
  await page.goto(`${BASE}#/home`);
  await page.locator('.pin-pad').waitFor();
  await enterPin(page, pin || PINS[who]);
  if (expectError) { await page.locator('.auth-hint', { hasText: expectError }).waitFor({ timeout: 15000 }); return; }
  await page.locator('.hero').waitFor({ timeout: 20000 });
}
const go = (page, hash) => page.evaluate((h) => { location.hash = h; }, hash);

try {
  await seed();
  const cuma = await newUser(devices['iPhone 13']);
  const ilayda = await newUser(devices['Pixel 5']);
  const third = await newUser({ viewport: { width: 1280, height: 800 } });
  Object.assign(live, { cuma: cuma.page, ilayda: ilayda.page });
  await step('Firestore PIN\'i yanlışsa giriş ekranı bunu açıkça söylüyor', async () => {
    await login(cuma.page, 'cuma', { expectError: 'Firestore' });
    assert.equal(await cuma.page.locator('.shell').count(), 0);
  });
  await step('İlayda (Firestore PIN\'i doğru) girebiliyor', async () => { await login(ilayda.page, 'ilayda'); });
} catch (e) { failures++; results.push(`❌ beklenmeyen hata: ${e.stack}`); }
finally { await browser.close(); server.kill(); }
console.log('\n' + results.join('\n'));
if (errors.length) console.log('\nTarayıcı hataları:\n' + [...new Set(errors)].slice(0, 20).join('\n'));
console.log(`\n${results.length - failures}/${results.length} adım başarılı`);
process.exit(failures || errors.length ? 1 : 0);
