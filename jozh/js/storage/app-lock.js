// Açılış PIN'i ve oturum kilidi. PIN saklanmaz; PBKDF2 özeti saklanır.
import * as db from './local-db.js';
import { deriveBits, randomBytes, constantTimeEqual, wipe, isWeakPin, lockoutDelayMs, FREE_ATTEMPTS, PBKDF2_ITERATIONS } from './encryption.js';

const CONFIG_KEY = 'appLock:config';
const ATTEMPTS_KEY = 'appLock:attempts';
const SESSION_KEY = 'jozh.session';
export const SESSION_TIMEOUT_MS = 10 * 60 * 1000;
const TOUCH_INTERVAL_MS = 15 * 1000;

export { isWeakPin };

export async function isConfigured() {
  const cfg = await db.getMeta(CONFIG_KEY);
  return Boolean(cfg && cfg.hash);
}

export async function setupPin(pin) {
  if (isWeakPin(pin)) {
    const err = new Error('Zayıf PIN');
    err.type = 'validation';
    throw err;
  }
  const salt = randomBytes(16);
  const hash = await deriveBits(pin, salt, PBKDF2_ITERATIONS);
  await db.setMeta(CONFIG_KEY, { salt, iterations: PBKDF2_ITERATIONS, hash, createdAt: new Date().toISOString() });
  await db.removeMeta(ATTEMPTS_KEY);
}

export async function getAttemptState() {
  const st = (await db.getMeta(ATTEMPTS_KEY)) || { failures: 0, lockedUntil: 0 };
  const now = Date.now();
  return {
    failures: st.failures || 0,
    lockedUntil: st.lockedUntil && st.lockedUntil > now ? st.lockedUntil : 0,
    remainingFree: Math.max(0, FREE_ATTEMPTS - (st.failures || 0))
  };
}

// { ok } ya da { ok:false, lockedUntil, remainingFree }
export async function verifyPin(pin) {
  const state = await getAttemptState();
  if (state.lockedUntil) return { ok: false, lockedUntil: state.lockedUntil, remainingFree: 0 };
  const cfg = await db.getMeta(CONFIG_KEY);
  if (!cfg) return { ok: false, notConfigured: true };
  const hash = await deriveBits(pin, cfg.salt, cfg.iterations);
  const ok = constantTimeEqual(hash, cfg.hash);
  wipe(hash);
  if (ok) {
    await db.removeMeta(ATTEMPTS_KEY);
    return { ok: true };
  }
  const failures = state.failures + 1;
  const delay = lockoutDelayMs(failures);
  const lockedUntil = delay ? Date.now() + delay : 0;
  await db.setMeta(ATTEMPTS_KEY, { failures, lockedUntil });
  return { ok: false, lockedUntil, remainingFree: Math.max(0, FREE_ATTEMPTS - failures) };
}

// Face ID ile başarılı açılış sahibini doğruladığı için PIN deneme sayacı sıfırlanır.
export function clearAttempts() {
  return db.removeMeta(ATTEMPTS_KEY);
}

// --- Oturum (yalnızca sessionStorage) ---

function readSession() {
  try {
    const raw = sessionStorage.getItem(SESSION_KEY);
    return raw ? JSON.parse(raw) : null;
  } catch {
    return null;
  }
}

export function startSession() {
  const now = Date.now();
  sessionStorage.setItem(SESSION_KEY, JSON.stringify({ startedAt: now, lastActive: now }));
}

export function isSessionValid() {
  const s = readSession();
  if (!s || typeof s.lastActive !== 'number') return false;
  return Date.now() - s.lastActive < SESSION_TIMEOUT_MS;
}

export function touchSession(force = false) {
  const s = readSession();
  if (!s) return;
  const now = Date.now();
  if (force || now - s.lastActive >= TOUCH_INTERVAL_MS) {
    s.lastActive = now;
    sessionStorage.setItem(SESSION_KEY, JSON.stringify(s));
  }
}

export function lock() {
  try {
    sessionStorage.removeItem(SESSION_KEY);
    sessionStorage.removeItem('jozh.vaultToken');
  } catch {
    // depolama kapalı olabilir
  }
}

// "PIN'imi unuttum": bu cihazdaki JOZH veritabanını siler.
export async function resetDevice() {
  lock();
  await db.deleteDatabase();
  try {
    for (const key of Object.keys(localStorage)) {
      if (key.startsWith('jozh.')) localStorage.removeItem(key);
    }
    sessionStorage.clear();
  } catch {
    // yok say
  }
}
