// Web Crypto yardımcıları: PBKDF2-SHA-256 anahtar türetme, AES-256-GCM şifreleme.
// Anahtarlar dışa aktarılamaz (extractable: false); açık anahtar baytları kullanımdan sonra sıfırlanır.

export const PBKDF2_ITERATIONS = 600000;
const enc = new TextEncoder();
const dec = new TextDecoder();

export function isCryptoAvailable() {
  return Boolean(window.isSecureContext && window.crypto && window.crypto.subtle);
}

export function randomBytes(n) {
  return crypto.getRandomValues(new Uint8Array(n));
}

export function wipe(bytes) {
  if (bytes && typeof bytes.fill === 'function') bytes.fill(0);
}

export function textBytes(text) {
  return enc.encode(text);
}

export function bytesText(bytes) {
  return dec.decode(bytes);
}

function toU8(data) {
  if (data instanceof Uint8Array) return data;
  if (data instanceof ArrayBuffer) return new Uint8Array(data);
  if (ArrayBuffer.isView(data)) return new Uint8Array(data.buffer, data.byteOffset, data.byteLength);
  throw new TypeError('Beklenmeyen veri türü');
}

export function toBase64(bytes) {
  const u8 = toU8(bytes);
  let bin = '';
  const chunk = 0x8000;
  for (let i = 0; i < u8.length; i += chunk) {
    bin += String.fromCharCode.apply(null, u8.subarray(i, i + chunk));
  }
  return btoa(bin);
}

export function fromBase64(b64) {
  const bin = atob(b64);
  const out = new Uint8Array(bin.length);
  for (let i = 0; i < bin.length; i += 1) out[i] = bin.charCodeAt(i);
  return out;
}

async function passwordKey(secret) {
  const bytes = textBytes(secret);
  try {
    return await crypto.subtle.importKey('raw', bytes, 'PBKDF2', false, ['deriveBits', 'deriveKey']);
  } finally {
    wipe(bytes);
  }
}

// 256 bitlik özet (açılış PIN'i doğrulaması için)
export async function deriveBits(secret, salt, iterations = PBKDF2_ITERATIONS) {
  const base = await passwordKey(secret);
  const bits = await crypto.subtle.deriveBits({ name: 'PBKDF2', hash: 'SHA-256', salt, iterations }, base, 256);
  return new Uint8Array(bits);
}

// AES-GCM kilit anahtarı (Gizli Kasa KEK'i, yedek anahtarı)
export async function deriveAesKey(secret, salt, iterations = PBKDF2_ITERATIONS) {
  const base = await passwordKey(secret);
  return crypto.subtle.deriveKey(
    { name: 'PBKDF2', hash: 'SHA-256', salt, iterations },
    base,
    { name: 'AES-GCM', length: 256 },
    false,
    ['encrypt', 'decrypt']
  );
}

export function importAesKey(rawBytes) {
  return crypto.subtle.importKey('raw', rawBytes, { name: 'AES-GCM' }, false, ['encrypt', 'decrypt']);
}

export async function encryptBytes(key, data, aad) {
  const iv = randomBytes(12);
  const params = { name: 'AES-GCM', iv };
  if (aad) params.additionalData = textBytes(aad);
  const ct = await crypto.subtle.encrypt(params, key, toU8(data));
  return { iv, data: new Uint8Array(ct) };
}

export async function decryptBytes(key, iv, data, aad) {
  const params = { name: 'AES-GCM', iv: toU8(iv) };
  if (aad) params.additionalData = textBytes(aad);
  const pt = await crypto.subtle.decrypt(params, key, toU8(data));
  return new Uint8Array(pt);
}

export async function encryptJSON(key, obj, aad) {
  const bytes = textBytes(JSON.stringify(obj));
  try {
    return await encryptBytes(key, bytes, aad);
  } finally {
    wipe(bytes);
  }
}

export async function decryptJSON(key, iv, data, aad) {
  const bytes = await decryptBytes(key, iv, data, aad);
  try {
    return JSON.parse(bytesText(bytes));
  } finally {
    wipe(bytes);
  }
}

export function constantTimeEqual(a, b) {
  const x = toU8(a);
  const y = toU8(b);
  let diff = x.length ^ y.length;
  const n = Math.max(x.length, y.length);
  for (let i = 0; i < n; i += 1) diff |= (x[i] || 0) ^ (y[i] || 0);
  return diff === 0;
}

// Aynı ya da ardışık rakamlardan oluşan PIN'ler (1111, 1234, 9876, 0987, 7890…) zayıftır.
export function isWeakPin(pin) {
  if (!/^\d{4}$/.test(pin)) return true;
  const d = pin.split('').map(Number);
  if (d.every((x) => x === d[0])) return true;
  const up = d.every((x, i) => i === 0 || x === (d[i - 1] + 1) % 10);
  const down = d.every((x, i) => i === 0 || x === (d[i - 1] + 9) % 10);
  return up || down;
}

// Yanlış deneme bekleme süresi: ilk 5 yanlışta yok, sonra 30 sn'den ikiye katlanır (en çok 1 saat).
export const FREE_ATTEMPTS = 5;
export function lockoutDelayMs(failures) {
  if (failures <= FREE_ATTEMPTS) return 0;
  const sec = Math.min(3600, 30 * 2 ** (failures - FREE_ATTEMPTS - 1));
  return sec * 1000;
}
