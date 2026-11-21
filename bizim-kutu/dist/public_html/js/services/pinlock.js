// Cihaz PIN kilidi.
// ÖNEMLİ: Bu bir YEREL ekran kilididir; Firebase kimlik doğrulamasının yerine geçmez.
// Gerçek kimlik doğrulaması e-posta/parola ile yapılır. PIN, açık kalan oturumu bu cihazda
// meraklı gözlerden korur. PIN kaynak kodda yoktur; kullanıcı kendisi belirler ve yalnızca
// PBKDF2 karması bu cihazın localStorage'ında tutulur. 5 hatalı denemede yerel PIN silinir
// ve oturum kapatılır (yeniden e-posta/parola gerekir).
import { pbkdf2Hex, toB64, randomBytes, safeEqual } from './crypto.js';
import { isPin } from '../utils/validation.js';

const KEY = (uid) => `bk.pin.${uid}`;
const ITER = 150000;
export const MAX_FAILS = 5;

const read = (uid) => { try { return JSON.parse(localStorage.getItem(KEY(uid)) || 'null'); } catch { return null; } };
const write = (uid, v) => { try { localStorage.setItem(KEY(uid), JSON.stringify(v)); } catch {} };

export const hasPin = (uid) => !!read(uid)?.hash;

export async function setPin(uid, pin) {
  if (!isPin(pin)) throw new Error('PIN 4 haneli olmalı.');
  const salt = toB64(randomBytes(16));
  write(uid, { v: 1, salt, iter: ITER, hash: await pbkdf2Hex(pin, salt, ITER), fails: 0 });
}

export function removePin(uid) { try { localStorage.removeItem(KEY(uid)); } catch {} }

/** { ok, remaining, wiped } */
export async function verifyPin(uid, pin) {
  const rec = read(uid);
  if (!rec) return { ok: false, remaining: 0, wiped: true };
  const ok = isPin(pin) && safeEqual(await pbkdf2Hex(pin, rec.salt, rec.iter), rec.hash);
  if (ok) { rec.fails = 0; write(uid, rec); return { ok: true, remaining: MAX_FAILS }; }
  rec.fails = (rec.fails || 0) + 1;
  if (rec.fails >= MAX_FAILS) { removePin(uid); return { ok: false, remaining: 0, wiped: true }; }
  write(uid, rec);
  return { ok: false, remaining: MAX_FAILS - rec.fails };
}

// Kilit zamanlayıcısı: uygulama arka plana alınıp belirlenen süreden uzun kalırsa kilitlenir.
let hiddenAt = 0;
export function watchAutoLock(getMinutes, onLock) {
  const handler = () => {
    if (document.visibilityState === 'hidden') hiddenAt = Date.now();
    else if (hiddenAt) {
      const min = getMinutes();
      if (min >= 0 && Date.now() - hiddenAt >= min * 60000) onLock();
      hiddenAt = 0;
    }
  };
  document.addEventListener('visibilitychange', handler);
  return () => document.removeEventListener('visibilitychange', handler);
}
