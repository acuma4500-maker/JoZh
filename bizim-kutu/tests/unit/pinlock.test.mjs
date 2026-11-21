import test from 'node:test';
import assert from 'node:assert/strict';

const store = new Map();
globalThis.localStorage = { getItem: (k) => (store.has(k) ? store.get(k) : null), setItem: (k, v) => store.set(k, String(v)), removeItem: (k) => store.delete(k) };
const { setPin, verifyPin, hasPin, removePin, MAX_FAILS } = await import('../../js/services/pinlock.js');
const U = 'pt0Kmbc9rqdJekFyvA1wLItUnxw1';

test('PIN düz metin olarak saklanmaz', async () => {
  await setPin(U, '4711');
  const raw = store.get(`bk.pin.${U}`);
  assert.ok(raw && !raw.includes('4711'));
  assert.ok(hasPin(U));
});

test('doğru PIN açar, yanlış PIN deneme hakkını azaltır', async () => {
  await setPin(U, '4711');
  assert.equal((await verifyPin(U, '4711')).ok, true);
  const r = await verifyPin(U, '0000');
  assert.equal(r.ok, false); assert.equal(r.remaining, MAX_FAILS - 1);
  assert.equal((await verifyPin(U, '4711')).ok, true, 'başarılı giriş sayacı sıfırlar');
});

test(`${MAX_FAILS} hatalı denemede PIN silinir`, async () => {
  await setPin(U, '4711');
  let r;
  for (let i = 0; i < MAX_FAILS; i++) r = await verifyPin(U, '1234');
  assert.equal(r.wiped, true);
  assert.equal(hasPin(U), false);
  assert.equal((await verifyPin(U, '4711')).ok, false);
});

test('geçersiz PIN biçimi reddedilir', async () => {
  await assert.rejects(setPin(U, '12a4'));
  await assert.rejects(setPin(U, '123'));
  removePin(U);
});
