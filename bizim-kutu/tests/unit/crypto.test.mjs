import test from 'node:test';
import assert from 'node:assert/strict';
import { createVaultConfig, unlockVault, encryptJSON, decryptJSON, passphraseStrength, safeEqual, VAULT_ITERATIONS } from '../../js/services/crypto.js';

const PASS = 'İlkKahvemiz@Moda2026';

test('kasa: doğru parola açar, yanlış parola açmaz', async () => {
  const { key, config } = await createVaultConfig(PASS);
  assert.equal(config.iterations, VAULT_ITERATIONS);
  assert.ok(config.iterations >= 600000);
  assert.ok(!JSON.stringify(config).includes(PASS), 'yapılandırmada parola yok');
  assert.ok(await unlockVault(PASS, config));
  assert.equal(await unlockVault('yanlış-parola-123', config), null);
  assert.equal(await unlockVault('2208', config), null);
  const enc = await encryptJSON(key, { title: 'Gizli', body: 'Seni seviyorum' }, 'note1');
  assert.ok(!enc.ct.includes('Seni'), 'şifreli metin düz metin içermez');
  const key2 = await unlockVault(PASS, config);
  assert.deepEqual(await decryptJSON(key2, enc, 'note1'), { title: 'Gizli', body: 'Seni seviyorum' });
});

test('kasa: şifreli metin başka belgeye taşınamaz (AAD) ve kurcalama tespit edilir', async () => {
  const { key } = await createVaultConfig(PASS);
  const enc = await encryptJSON(key, { body: 'x' }, 'noteA');
  await assert.rejects(decryptJSON(key, enc, 'noteB'));
  const bytes = Buffer.from(enc.ct, 'base64'); bytes[0] ^= 1;
  await assert.rejects(decryptJSON(key, { iv: enc.iv, ct: bytes.toString('base64') }, 'noteA'));
});

test('kasa: her şifrelemede farklı IV', async () => {
  const { key } = await createVaultConfig(PASS);
  const a = await encryptJSON(key, { b: 1 }, 'n'), b = await encryptJSON(key, { b: 1 }, 'n');
  assert.notEqual(a.iv, b.iv); assert.notEqual(a.ct, b.ct);
});

test('anahtar dışa aktarılamaz', async () => {
  const k = await unlockVault(PASS, (await createVaultConfig(PASS)).config);
  assert.equal(k.extractable, false);
  await assert.rejects(crypto.subtle.exportKey('raw', k));
});

test('parola gücü: 4 haneli PIN reddedilir', () => {
  assert.equal(passphraseStrength('2208').ok, false);
  assert.equal(passphraseStrength('sifre123').ok, false);
  assert.equal(passphraseStrength(PASS).ok, true);
});

test('sabit zamanlı karşılaştırma', () => {
  assert.ok(safeEqual('abc', 'abc'));
  assert.ok(!safeEqual('abc', 'abd'));
  assert.ok(!safeEqual('abc', 'ab'));
});
