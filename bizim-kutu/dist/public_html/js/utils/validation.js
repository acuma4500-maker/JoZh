// Girdi doğrulama. Sınırlar Firebase güvenlik kurallarıyla birebir aynıdır (firebase/*.rules).
export const LIMITS = Object.freeze({
  message: 2000,
  memoryTitle: 80, memoryText: 2000, emoji: 16,
  movieTitle: 120, movieGenre: 40, movieText: 1000,
  taskTitle: 120, taskText: 1000,
  storyTitle: 80, storyLine: 300, storyText: 20000,
  answer: 1000, nickname: 24,
  notifTitle: 80, notifBody: 200,
  vaultPlain: 15000, vaultCipher: 30000,
});

const CONTROL = /[\u0000-\u0008\u000B\u000C\u000E-\u001F\u007F]/g;

/** Kontrol karakterlerini temizler, kırpar. */
export function cleanText(value, max = Infinity, { multiline = true } = {}) {
  let s = String(value ?? '').replace(CONTROL, '');
  if (!multiline) s = s.replace(/[\r\n\t]+/g, ' ');
  s = s.replace(/\r\n/g, '\n').trim();
  return s.length > max ? s.slice(0, max) : s;
}

export function validateText(value, { label = 'Alan', min = 1, max, multiline = true } = {}) {
  const raw = String(value ?? '').replace(CONTROL, '').trim();
  if (raw.length < min) return { ok: false, error: min <= 1 ? `${label} boş bırakılamaz.` : `${label} en az ${min} karakter olmalı.` };
  if (max && raw.length > max) return { ok: false, error: `${label} en fazla ${max} karakter olabilir.` };
  return { ok: true, value: cleanText(raw, max, { multiline }) };
}

export function isISODate(s) {
  const m = /^(\d{4})-(\d{2})-(\d{2})$/.exec(s || '');
  if (!m) return false;
  const d = new Date(Date.UTC(+m[1], +m[2] - 1, +m[3]));
  return d.getUTCFullYear() === +m[1] && d.getUTCMonth() === +m[2] - 1 && d.getUTCDate() === +m[3];
}

export const isPin = (s) => /^\d{4}$/.test(String(s || ''));

export const MOVIE_STATUS = Object.freeze(['watchlist', 'watching', 'watched']);
export const MOVIE_KIND = Object.freeze(['film', 'dizi']);
export const TASK_PRIORITY = Object.freeze(['low', 'medium', 'high']);
export const NOTIF_TYPES = Object.freeze(['message', 'game_invite', 'game_accept', 'memory', 'task', 'task_done']);
export const GAME_IDS = Object.freeze(['xox', 'know-me', 'truth-dare', 'emoji', 'memory', 'story', 'questions']);
