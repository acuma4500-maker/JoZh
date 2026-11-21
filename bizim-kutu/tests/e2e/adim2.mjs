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
    body: JSON.stringify({ fields: { [A]: { integerValue: String(Number(PINS.cuma)) }, [B]: { stringValue: PINS.ilayda } } }),
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
  await step('Adım 2: yanlış PIN engelleniyor', async () => {
    await login(third.page, 'x', { pin: '9999', expectError: 'PIN hatalı' });
    assert.equal(await third.page.locator('.shell').count(), 0);
  });
  await step('Adım 2: Cuma PIN ile giriyor, ana sayfa açılıyor', async () => { await login(cuma.page, 'cuma'); });
  await step('Adım 2: İlayda PIN ile giriyor', async () => { await login(ilayda.page, 'ilayda'); });
  await step('Adım 2: menüde Ana Sayfa, Sohbet, Profil; kapalı bölüm "yakında"', async () => {
    const labels = await cuma.page.locator('.tab:visible .tab__label').allInnerTexts();
    assert.deepEqual(labels, ['Ana Sayfa', 'Sohbet', 'Profil']);
    await go(cuma.page, '#/memories');
    await cuma.page.getByText('Bu bölüm yakında açılacak').waitFor();
    await go(cuma.page, '#/home');
  });
  await step('Adım 2: sayaç ve çevrim içi durum', async () => {
    await cuma.page.locator('.counter-days__num').waitFor();
    await cuma.page.locator('.partner-chip__sub', { hasText: 'Çevrim içi' }).waitFor({ timeout: 10000 });
    await cuma.page.locator('.home-card__quote').waitFor();
    await shot(cuma.page, 'adim1-home');
  });
  await step('5. Sohbet: mesaj anlık iletiliyor + yazıyor göstergesi', async () => {
    await go(cuma.page, '#/chat'); await go(ilayda.page, '#/home');
    await cuma.page.locator('.composer__input').waitFor();
    await cuma.page.fill('.composer__input', 'Günaydın sevgilim ☀️');
    await cuma.page.click('.composer__send');
    await ilayda.page.locator('.home-card__text', { hasText: 'Günaydın sevgilim' }).waitFor({ timeout: 10000 });
    await ilayda.page.locator('.tab .badge:not([hidden])').first().waitFor({ timeout: 5000 });
    await go(ilayda.page, '#/chat');
    await ilayda.page.locator('.msg--them .msg__text', { hasText: 'Günaydın sevgilim' }).waitFor({ timeout: 10000 });
    await ilayda.page.locator('.composer__input').type('Sana da güna', { delay: 30 });
    await cuma.page.locator('.chat-head__status.is-typing').waitFor({ timeout: 8000 });
  });

  await step('6. Görüldü bilgisi: İlayda okuyunca Cuma\'da çift pembe tik', async () => {
    await cuma.page.locator('.msg--me .tick--read').last().waitFor({ timeout: 10000 });
    await ilayda.page.fill('.composer__input', 'Sana da günaydın 💕');
    await ilayda.page.locator('.composer__send').click();
    await cuma.page.locator('.msg--them .msg__text', { hasText: 'Sana da günaydın' }).waitFor({ timeout: 10000 });
    await shot(cuma.page, '02-chat-cuma');
  });

  await step('XSS: HTML içeren mesaj metin olarak gösterilir, çalıştırılmaz', async () => {
    await cuma.page.fill('.composer__input', '<img src=x onerror="window.__xss=1"><b>kalın</b>');
    await cuma.page.click('.composer__send');
    await ilayda.page.locator('.msg__text', { hasText: '<b>kalın</b>' }).waitFor({ timeout: 10000 });
    assert.equal(await ilayda.page.evaluate(() => window.__xss), undefined);
    assert.equal(await ilayda.page.locator('.msg__text img, .msg__text b').count(), 0);
  });

  await step('Sohbet: mesaj silme iki tarafta da "silindi" olur; boş mesaj gönderilemez', async () => {
    await cuma.page.locator('.msg--me .msg__bubble').last().click();
    await cuma.page.getByRole('button', { name: 'Herkesten sil' }).click();
    await cuma.page.getByRole('button', { name: 'Sil', exact: true }).click();
    await ilayda.page.locator('.msg--deleted', { hasText: 'Bu mesaj silindi' }).waitFor({ timeout: 10000 });
    await cuma.page.fill('.composer__input', '    ');
    assert.equal(await cuma.page.locator('.composer__send').isDisabled(), true);
  });

  await step('Adım 2: profil kaydı (takma ad) ve çıkış', async () => {
    await go(cuma.page, '#/profile');
    await cuma.page.locator('.settings input.input').first().fill('Ayıcık');
    await cuma.page.getByRole('button', { name: 'Kaydet' }).click();
    await ilayda.page.evaluate(() => { location.hash = '#/profile'; });
    await ilayda.page.locator('.profile-card__nick', { hasText: 'Ayıcık' }).waitFor({ timeout: 10000 });
    await cuma.page.getByRole('button', { name: 'Oturumu kapat' }).click();
    await cuma.page.getByRole('button', { name: 'Çıkış yap' }).click();
    await cuma.page.locator('.pin-pad').waitFor({ timeout: 15000 });
  });
} catch (e) { failures++; results.push(`❌ beklenmeyen hata: ${e.stack}`); }
finally { await browser.close(); server.kill(); }
console.log('\n' + results.join('\n'));
if (errors.length) console.log('\nTarayıcı hataları:\n' + [...new Set(errors)].slice(0, 20).join('\n'));
console.log(`\n${results.length - failures}/${results.length} adım başarılı`);
process.exit(failures || errors.length ? 1 : 0);
