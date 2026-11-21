// Özel Kasa için istemci tarafı şifreleme (Web Crypto API).
// - Anahtar: kasa parolasından PBKDF2-SHA256 (600.000 tur) ile türetilen AES-GCM-256 anahtarı.
// - Anahtar dışa aktarılamaz (extractable: false) ve hiçbir zaman sunucuya gönderilmez.
// - Her not rastgele 96 bit IV ile şifrelenir; not kimliği "ek doğrulanmış veri" (AAD) olarak bağlanır,
//   böylece şifreli metinler belgeler arasında taşınamaz.
// - Firestore'a yalnızca {iv, ct} gider; başlık ve içerik dahil düz metin asla yazılmaz.

const enc = new TextEncoder();
const dec = new TextDecoder();
export const VAULT_ITERATIONS = 600000;
export const VAULT_CHECK = 'bizim-kutu-kasa-v1';
const AAD_PREFIX = 'bizim-kutu/vault/v1/';

export const toB64 = (buf) => {
  const bytes = new Uint8Array(buf);
  let s = '';
  for (let i = 0; i < bytes.length; i += 0x8000) s += String.fromCharCode(...bytes.subarray(i, i + 0x8000));
  return btoa(s);
};
export const fromB64 = (b64) => Uint8Array.from(atob(b64), (c) => c.charCodeAt(0));
export const randomBytes = (n) => crypto.getRandomValues(new Uint8Array(n));

export async function deriveVaultKey(passphrase, saltB64, iterations = VAULT_ITERATIONS) {
  const base = await crypto.subtle.importKey('raw', enc.encode(passphrase.normalize('NFC')), 'PBKDF2', false, ['deriveKey']);
  return crypto.subtle.deriveKey(
    { name: 'PBKDF2', hash: 'SHA-256', salt: fromB64(saltB64), iterations },
    base, { name: 'AES-GCM', length: 256 }, false, ['encrypt', 'decrypt']);
}

export async function encryptJSON(key, obj, bindTo = '') {
  const iv = randomBytes(12);
  const ct = await crypto.subtle.encrypt({ name: 'AES-GCM', iv, additionalData: enc.encode(AAD_PREFIX + bindTo) }, key, enc.encode(JSON.stringify(obj)));
  return { iv: toB64(iv), ct: toB64(ct) };
}

export async function decryptJSON(key, { iv, ct }, bindTo = '') {
  const pt = await crypto.subtle.decrypt({ name: 'AES-GCM', iv: fromB64(iv), additionalData: enc.encode(AAD_PREFIX + bindTo) }, key, fromB64(ct));
  return JSON.parse(dec.decode(pt));
}

/** Yeni kasa yapılandırması: tuz + doğrulama bloğu (parolanın doğruluğunu sunucuya göndermeden kontrol etmek için). */
export async function createVaultConfig(passphrase) {
  const salt = toB64(randomBytes(16));
  const key = await deriveVaultKey(passphrase, salt, VAULT_ITERATIONS);
  const check = await encryptJSON(key, { check: VAULT_CHECK }, 'check');
  return { key, config: { v: 1, salt, iterations: VAULT_ITERATIONS, check } };
}

/** Parola doğruysa anahtarı, yanlışsa null döndürür. */
export async function unlockVault(passphrase, config) {
  try {
    const key = await deriveVaultKey(passphrase, config.salt, config.iterations);
    const out = await decryptJSON(key, config.check, 'check');
    return out?.check === VAULT_CHECK ? key : null;
  } catch { return null; }
}

/** Parola gücü: kabaca entropi tahmini (bit). */
export function passphraseStrength(p) {
  const s = String(p || '');
  let pool = 0;
  if (/[a-zçğıöşü]/.test(s)) pool += 29;
  if (/[A-ZÇĞİÖŞÜ]/.test(s)) pool += 29;
  if (/\d/.test(s)) pool += 10;
  if (/[^A-Za-z0-9çğıöşüÇĞİÖŞÜ]/.test(s)) pool += 20;
  const unique = new Set(s).size;
  const bits = Math.round(Math.min(s.length, unique * 1.5) * Math.log2(Math.max(pool, 1)));
  return { bits, ok: s.length >= 10 && bits >= 50, label: bits >= 80 ? 'Çok güçlü' : bits >= 60 ? 'Güçlü' : bits >= 50 ? 'Yeterli' : 'Zayıf' };
}

/** PIN gibi kısa sırlar için yerel karma (cihaz kilidi). */
export async function pbkdf2Hex(secret, saltB64, iterations) {
  const base = await crypto.subtle.importKey('raw', enc.encode(secret), 'PBKDF2', false, ['deriveBits']);
  const bits = await crypto.subtle.deriveBits({ name: 'PBKDF2', hash: 'SHA-256', salt: fromB64(saltB64), iterations }, base, 256);
  return [...new Uint8Array(bits)].map((b) => b.toString(16).padStart(2, '0')).join('');
}

/** Sabit zamanlı dize karşılaştırması. */
export function safeEqual(a, b) {
  if (typeof a !== 'string' || typeof b !== 'string' || a.length !== b.length) return false;
  let r = 0;
  for (let i = 0; i < a.length; i++) r |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return r === 0;
}
