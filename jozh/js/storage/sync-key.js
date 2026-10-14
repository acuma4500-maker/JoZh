// Senkronizasyon anahtarı: 26 karakter, alfabe a-z2-7 (~130 bit), crypto.getRandomValues ile üretilir.
import * as db from './local-db.js';

const ALPHABET = 'abcdefghijklmnopqrstuvwxyz234567';
export const KEY_RE = /^[a-z2-7]{26}$/;
const META_KEY = 'sync:key';

export function generateKey() {
  const bytes = crypto.getRandomValues(new Uint8Array(26));
  let out = '';
  for (const b of bytes) out += ALPHABET[b & 31];
  bytes.fill(0);
  return out;
}

// Boşluk, tire ve büyük harf önemsizdir.
export function normalizeKey(input) {
  return String(input || '').toLowerCase().replace(/[\s-]/g, '');
}

export function isValidKey(key) {
  return KEY_RE.test(key || '');
}

// xxxx-xxxx-…-xx
export function formatKey(key) {
  return (key || '').match(/.{1,4}/g)?.join('-') || '';
}

export function maskKey(key) {
  return formatKey(key).replace(/[a-z2-7]/g, '•');
}

export async function getKey() {
  const key = await db.getMeta(META_KEY);
  return isValidKey(key) ? key : null;
}

export function setKey(key) {
  if (!isValidKey(key)) throw new Error('Geçersiz anahtar');
  return db.setMeta(META_KEY, key);
}

export function clearKey() {
  return db.removeMeta(META_KEY);
}
