// Oyunlar için ortak yardımcılar.
// "Taahhüt et – sonra göster" (commit–reveal): gizli cevaplar veritabanına önce yalnızca
// SHA-256(nonce + cevap) olarak yazılır. İki taraf da taahhüt ettikten sonra cihazlar cevabı
// ve nonce'u açıklar; diğer cihaz karmayı doğrular. Böylece cevaplar karşı tarafça önceden
// okunamaz (veritabanında düz metin yoktur) ve sonradan değiştirilemez.
import { h } from '../utils/helpers.js';
import { randomId, sha256Hex } from '../utils/helpers.js';

const stashKey = (sid, tag) => `bk.secret.${sid}.${tag}`;

export async function commitSecret(sid, tag, text) {
  const nonce = randomId(16);
  const hash = await sha256Hex(`${nonce}:${text}`);
  try { sessionStorage.setItem(stashKey(sid, tag), JSON.stringify({ text, nonce })); } catch {}
  return { hash, nonce, text };
}

export function readSecret(sid, tag) {
  try { return JSON.parse(sessionStorage.getItem(stashKey(sid, tag)) || 'null'); } catch { return null; }
}
export function dropSecret(sid, tag) { try { sessionStorage.removeItem(stashKey(sid, tag)); } catch {} }

export async function verifySecret(reveal, hash) {
  if (!reveal || typeof reveal.text !== 'string' || !reveal.nonce) return false;
  return (await sha256Hex(`${reveal.nonce}:${reveal.text}`)) === hash;
}

export const otherOf = (players, uid) => players.find((p) => p !== uid);
export const toArray = (v) => (Array.isArray(v) ? v.filter((x) => x !== null && x !== undefined) : v && typeof v === 'object' ? Object.keys(v).sort((a, b) => a - b).map((k) => v[k]) : []);

/** Sıra göstergesi. */
export function turnBanner(api, turnUid, mineText = 'Sıra sende!', theirText) {
  const mine = turnUid === api.me;
  return h('div', { class: `turn-banner${mine ? ' is-mine' : ''}`, role: 'status', 'aria-live': 'polite' },
    h('span', { 'aria-hidden': 'true' }, api.emoji(turnUid)), mine ? mineText : (theirText || `${api.name(turnUid)} düşünüyor…`));
}

/** Sonuç başlığı (kazanan/berabere). */
export function resultTitle(api, winner) {
  if (winner === 'draw') return h('h3', { class: 'result__title' }, 'Berabere! 🤝');
  if (winner === api.me) return h('h3', { class: 'result__title' }, 'Kazandın! 🏆');
  if (winner) return h('h3', { class: 'result__title' }, `${api.name(winner)} kazandı! 💐`);
  return h('h3', { class: 'result__title' }, 'Oyun bitti 💞');
}

export function scoreLine(api, scores = {}) {
  return h('div', { class: 'score-line' },
    [api.me, api.partner].map((u) => h('div', { class: 'score-line__item' },
      h('span', { 'aria-hidden': 'true' }, api.emoji(u)), h('span', {}, api.name(u)), h('b', {}, String(scores[u] || 0)))));
}

/** Kazananı puanlara göre belirler. */
export function winnerByScore(scores, players) {
  const [a, b] = players;
  const sa = scores?.[a] || 0, sb = scores?.[b] || 0;
  return sa === sb ? 'draw' : sa > sb ? a : b;
}

// Taslak koruma: oyun ekranı her oturum güncellemesinde yeniden çizilir; yazılmakta olan
// metin ve odak kaybolmasın diye taslaklar burada tutulur.
const drafts = new Map();
let focusedDraft = null;
export function draft(key, input) {
  if (drafts.has(key)) input.value = drafts.get(key);
  input.dataset.draft = key;
  input.addEventListener('input', () => {
    drafts.set(key, input.value);
    // Yazarken ekran yeniden çizildiyse metni canlı alana taşı
    if (!input.isConnected) document.querySelectorAll(`[data-draft="${CSS.escape(key)}"]`).forEach((live) => { if (live !== input && live.value !== input.value) live.value = input.value; });
  });
  input.addEventListener('focus', () => { focusedDraft = key; });
  input.addEventListener('blur', () => { if (focusedDraft === key) setTimeout(() => { if (document.activeElement?.dataset?.draft !== key) focusedDraft = null; }, 0); });
  if (focusedDraft === key) requestAnimationFrame(() => { input.focus({ preventScroll: true }); try { input.setSelectionRange(input.value.length, input.value.length); } catch {} });
  return input;
}
export function clearDraft(key) { drafts.delete(key); if (focusedDraft === key) focusedDraft = null; }
