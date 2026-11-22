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
  await step('Adım 4: yanlış PIN engelleniyor', async () => {
    await login(third.page, 'x', { pin: '9999', expectError: 'PIN hatalı' });
    assert.equal(await third.page.locator('.shell').count(), 0);
  });
  await step('Çift dokunuş: aynı rakama hızlı iki dokunuş iki rakam girer, yakınlaştırma olmaz', async () => {
    const phone = await newUser(devices['iPhone 13']);
    const p = phone.page;
    await p.goto(`${BASE}#/home`);
    await p.locator('.pin-pad').waitFor();
    const key = p.locator('.pin-key', { hasText: '2' }).first();
    const scale0 = await p.evaluate(() => window.visualViewport?.scale || 1);
    await key.tap(); await key.tap();
    await p.waitForTimeout(150);
    assert.equal(await p.locator('.pin-dot.is-filled').count(), 2, 'iki rakam girilmeli');
    assert.equal(await p.evaluate(() => window.visualViewport?.scale || 1), scale0, 'yakınlaştırma olmamalı');
    assert.equal(await p.evaluate(() => getComputedStyle(document.documentElement).touchAction), 'pan-x pan-y');
    await phone.ctx.close();
  });

  await step('Adım 4: Cuma PIN ile giriyor, ana sayfa açılıyor', async () => { await login(cuma.page, 'cuma'); });
  await step('Adım 4: İlayda PIN ile giriyor', async () => { await login(ilayda.page, 'ilayda'); });
  await step('Adım 4: menüde Ana Sayfa, Sohbet, Anılar, Profil, Daha; kapalı bölüm "yakında"', async () => {
    const labels = await cuma.page.locator('.tab:visible .tab__label').allInnerTexts();
    assert.deepEqual(labels, ['Ana Sayfa', 'Sohbet', 'Anılar', 'Profil', 'Daha']);
    await go(cuma.page, '#/movies');
    await cuma.page.getByText('Bu bölüm yakında açılacak').waitFor();
    await go(cuma.page, '#/home');
  });
  await step('Adım 4: sayaç ve çevrim içi durum', async () => {
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

  await step('Yazıyor göstergesi yazmaya devam ettikçe kesintisiz kalıyor', async () => {
    await go(cuma.page, '#/chat'); await go(ilayda.page, '#/chat');
    await ilayda.page.locator('.composer__input').fill('');
    await ilayda.page.locator('.composer__input').click();
    const samples = [];
    const sampler = (async () => { for (let i = 0; i < 26; i++) { await cuma.page.waitForTimeout(500); samples.push(await cuma.page.locator('.chat-head__status').innerText()); } })();
    // Düşünerek yazma: kelimeler arasında 4 sn duraklama
    for (const word of ['seni ', 'çok ', 'seviyorum']) { await ilayda.page.keyboard.type(word, { delay: 120 }); await ilayda.page.waitForTimeout(4000); }
    await sampler;
    console.log('    durumlar:', samples.join(' | '));
    assert.ok(samples.slice(2, 24).every((t) => t === 'yazıyor…'), 'duraklamalarla yazarken de "yazıyor…" sürmeli');
    // Gönderince hemen kalkmalı
    await ilayda.page.locator('.composer__send').click();
    await cuma.page.locator('.chat-head__status:not(.is-typing)').waitFor({ timeout: 3000 });
  });

  await step('Klavye düzeni: üst bar sabit, klavye açıkken alt menü gizli, yazı kutusu görünür', async () => {
    await go(cuma.page, '#/chat');
    await cuma.page.locator('.composer__input').waitFor();
    const top0 = (await cuma.page.locator('.topbar').boundingBox()).y;
    // Klavyeyi taklit: görünen alan 400px'e düşer
    await cuma.page.evaluate(() => { document.activeElement?.blur(); window.__vvTest = { height: 400 }; });
    await cuma.page.locator('.composer__input').focus();
    await cuma.page.waitForTimeout(500);
    const top1 = (await cuma.page.locator('.topbar').boundingBox()).y;
    assert.equal(top1, top0, 'üst bar yerinde kalmalı');
    assert.equal(await cuma.page.locator('.tabbar').isVisible(), false, 'alt menü gizlenmeli');
    const comp = await cuma.page.locator('.composer').boundingBox();
    assert.ok(comp.y + comp.height <= 400 + 1, `yazı kutusu görünen alanda olmalı (${comp.y + comp.height})`);
    await shot(cuma.page, 'kb-open-chat');
    await cuma.page.evaluate(() => { delete window.__vvTest; document.activeElement.blur(); });
    await cuma.page.waitForTimeout(600);
    assert.equal(await cuma.page.locator('.tabbar').isVisible(), true);
    await shot(cuma.page, 'kb-closed-chat');
    // sayfa (belge) hiç kaymamalı; yalnızca orta alan kayar
    assert.equal(await cuma.page.evaluate(() => document.scrollingElement.scrollHeight <= innerHeight + 1), true, 'belge kaymamalı');
    await go(cuma.page, '#/home');
    await cuma.page.locator('.hero').waitFor();
    await cuma.page.waitForTimeout(300);
    const active = await cuma.page.locator('.tab.is-active .tab__label').allInnerTexts();
    assert.deepEqual(active, ['Ana Sayfa'], 'yalnızca Ana Sayfa seçili olmalı');
    await shot(cuma.page, 'home-layout');
  });

  await step('9. Anı defteri: ekleme (Cuma) → İlayda görür → düzenleme (İlayda) → Cuma görür', async () => {
    await go(cuma.page, '#/memories'); await go(ilayda.page, '#/memories');
    await cuma.page.getByRole('button', { name: 'Anı ekle' }).click();
    await cuma.page.fill('.modal input.input:not([type=date])', 'İlk kahvemiz');
    await cuma.page.fill('.modal input[type=date]', '2026-08-22');
    await cuma.page.fill('.modal textarea', 'Moda sahilinde, rüzgârlı bir akşam.');
    await cuma.page.click('.modal button[type=submit]');
    await ilayda.page.locator('.timeline__item .card__title', { hasText: 'İlk kahvemiz' }).waitFor({ timeout: 10000 });
    await ilayda.page.locator('.timeline__item').first().getByRole('button', { name: 'Düzenle' }).click();
    await ilayda.page.fill('.modal input.input:not([type=date])', 'İlk kahvemiz ☕');
    await ilayda.page.click('.modal button[type=submit]');
    await cuma.page.locator('.timeline__item .card__title', { hasText: 'İlk kahvemiz ☕' }).waitFor({ timeout: 10000 });
    await cuma.page.locator('.card__meta', { hasText: 'İlayda düzenledi' }).waitFor({ timeout: 10000 });
    await shot(cuma.page, '03-memories');
  });

  await step('Anı defteri: ana sayfada "Son anı" kartı, silme iki tarafta, tarih sırası', async () => {
    await go(ilayda.page, '#/home');
    await ilayda.page.locator('.home-card', { hasText: 'Son anı' }).locator('.home-card__text', { hasText: 'İlk kahvemiz' }).waitFor({ timeout: 10000 });
    await go(cuma.page, '#/memories'); await go(ilayda.page, '#/memories');
    await cuma.page.getByRole('button', { name: 'Anı ekle' }).click();
    await cuma.page.fill('.modal input.input:not([type=date])', 'Silinecek anı');
    await cuma.page.fill('.modal input[type=date]', '2026-09-01');
    await cuma.page.click('.modal button[type=submit]');
    await ilayda.page.locator('.timeline__item .card__title', { hasText: 'Silinecek anı' }).waitFor({ timeout: 10000 });
    await ilayda.page.locator('.timeline__item', { hasText: 'Silinecek anı' }).getByRole('button', { name: 'Sil' }).click();
    await ilayda.page.getByRole('button', { name: 'Sil', exact: true }).last().click();
    await cuma.page.locator('.timeline__item .card__title', { hasText: 'Silinecek anı' }).waitFor({ state: 'detached', timeout: 10000 });
    await cuma.page.getByRole('button', { name: 'Anı ekle' }).click();
    await cuma.page.fill('.modal input.input:not([type=date])', 'Eylül yürüyüşü');
    await cuma.page.fill('.modal input[type=date]', '2026-09-10');
    await cuma.page.click('.modal button[type=submit]');
    await cuma.page.locator('.timeline__item .card__title', { hasText: 'Eylül yürüyüşü' }).waitFor();
    const titles = await cuma.page.locator('.timeline__item .card__title').allInnerTexts();
    assert.deepEqual(titles, ['Eylül yürüyüşü', 'İlk kahvemiz ☕']);
    await shot(cuma.page, 'adim3-memories');
  });

  await step('11. Görevler iki cihazda güncelleniyor (ekle → tamamla)', async () => {
    await go(cuma.page, '#/tasks'); await go(ilayda.page, '#/tasks');
    await cuma.page.getByRole('button', { name: 'Görev ekle' }).first().click();
    await cuma.page.fill('.modal input.input >> nth=0', 'Hafta sonu piknik');
    await cuma.page.fill('.modal input[type=date]', '2026-12-05');
    await cuma.page.click('.modal button[type=submit]');
    await ilayda.page.locator('.task .card__title', { hasText: 'Hafta sonu piknik' }).waitFor({ timeout: 10000 });
    await ilayda.page.locator('.task', { hasText: 'Hafta sonu piknik' }).locator('.task-check').click();
    await cuma.page.locator('.task .card__title', { hasText: 'Hafta sonu piknik' }).waitFor({ state: 'detached', timeout: 10000 });
    await cuma.page.getByRole('tab', { name: /Tamamlananlar/ }).click();
    await cuma.page.locator('.task--done', { hasText: 'İlayda tamamladı' }).waitFor({ timeout: 10000 });
  });

  const PASS = 'İlkKahvemiz@Moda2026';
  await step('Görevler: son tarihli görev ana sayfada "Yaklaşan görev", geri alma, silme', async () => {
    await go(cuma.page, '#/tasks'); await go(ilayda.page, '#/tasks');
    await cuma.page.getByRole('tab', { name: /Yapılacaklar/ }).click();
    await cuma.page.getByRole('button', { name: 'Görev ekle' }).first().click();
    await cuma.page.fill('.modal input.input >> nth=0', 'Sinema bileti al');
    await cuma.page.fill('.modal input[type=date]', '2026-11-28');
    await cuma.page.locator('.modal select').selectOption('high');
    await cuma.page.click('.modal button[type=submit]');
    await ilayda.page.locator('.task .card__title', { hasText: 'Sinema bileti al' }).waitFor({ timeout: 10000 });
    await ilayda.page.locator('.task', { hasText: 'Sinema bileti al' }).locator('.pill', { hasText: 'Yüksek' }).waitFor();
    await go(ilayda.page, '#/home');
    await ilayda.page.locator('.home-card', { hasText: 'Yaklaşan görev' }).locator('.home-card__text', { hasText: 'Sinema bileti al' }).waitFor({ timeout: 10000 });
    // tamamla → geri al
    await cuma.page.locator('.task', { hasText: 'Sinema bileti al' }).locator('.task-check').click();
    await cuma.page.getByRole('tab', { name: /Tamamlananlar/ }).click();
    await cuma.page.locator('.task--done', { hasText: 'Sinema bileti al' }).locator('.task-check').click();
    await cuma.page.getByRole('tab', { name: /Yapılacaklar/ }).click();
    await cuma.page.locator('.task:not(.task--done) .card__title', { hasText: 'Sinema bileti al' }).waitFor({ timeout: 10000 });
    // sil
    await cuma.page.locator('.task', { hasText: 'Sinema bileti al' }).getByRole('button', { name: 'Sil' }).click();
    await cuma.page.getByRole('button', { name: 'Sil', exact: true }).last().click();
    await cuma.page.locator('.task .card__title', { hasText: 'Sinema bileti al' }).waitFor({ state: 'detached', timeout: 10000 });
    await shot(cuma.page, 'adim4-tasks');
  });

  await step('Mobil menü: Görevler "Daha" menüsünden açılıyor', async () => {
    await go(cuma.page, '#/more');
    await cuma.page.locator('.more-item', { hasText: 'Yapılacaklar' }).click();
    await cuma.page.locator('.page-title', { hasText: 'Yapılacaklar' }).waitFor();
  });

  await step('Adım 4: profil kaydı (takma ad) ve çıkış', async () => {
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
