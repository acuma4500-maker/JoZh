// Realtime Database: sohbet, yazıyor göstergesi, iletildi/görüldü bilgileri.
import { rtdb } from '../firebase-config.js';
import {
  ref, push, set, update, onValue, onChildAdded, onChildChanged, onChildRemoved, get,
  rtdbQuery, orderByKey, limitToLast, endBefore, rtdbServerTimestamp, onDisconnect
} from '../vendor/firebase.js';
import { LIMITS, cleanText } from '../utils/validation.js';

const messagesRef = () => ref(rtdb, 'chat/messages');

const toMsg = (snap) => ({ id: snap.key, ...snap.val() });

/** Son n mesajı canlı dinler. Dönüş: abonelikten çıkış. */
export function subscribeMessages({ onAdd, onChange, onRemove, onError }, n = 40) {
  const q = rtdbQuery(messagesRef(), orderByKey(), limitToLast(n));
  const u1 = onChildAdded(q, (s) => onAdd?.(toMsg(s)), onError);
  const u2 = onChildChanged(q, (s) => onChange?.(toMsg(s)), onError);
  const u3 = onChildRemoved(q, (s) => onRemove?.(s.key), onError);
  return () => { u1(); u2(); u3(); };
}

/** Daha eski mesajları sayfalı getirir. */
export async function loadOlderMessages(beforeKey, n = 40) {
  const snap = await get(rtdbQuery(messagesRef(), orderByKey(), endBefore(beforeKey), limitToLast(n)));
  const out = [];
  snap.forEach((c) => { out.push(toMsg(c)); });
  return out;
}

/** Son mesajları dinler (ana sayfa, okunmamış sayacı, bildirimler). */
export function subscribeRecent(cb, n = 30) {
  return onValue(rtdbQuery(messagesRef(), orderByKey(), limitToLast(n)), (snap) => {
    const list = [];
    snap.forEach((c) => { list.push(toMsg(c)); });
    cb(list);
  }, (e) => console.warn('recent messages', e));
}

/** Mesaj gönderir. Anahtar hemen döner; `done` sunucu onayında çözülür. */
export function sendMessage(uid, text) {
  const clean = cleanText(text, LIMITS.message);
  if (!clean) throw new Error('Boş mesaj gönderilemez.');
  const r = push(messagesRef());
  const done = set(r, { uid, text: clean, ts: rtdbServerTimestamp() });
  return { id: r.key, text: clean, done };
}

/** Mesajı herkes için siler (yalnızca gönderen; kurallar da bunu zorlar). */
export function deleteMessage(id) {
  return update(ref(rtdb, `chat/messages/${id}`), { text: '', deleted: true });
}

// --- Yazıyor göstergesi ---
// Yazarken sinyal en fazla 2 sn'de bir yenilenir (karşı taraf 8 sn içinde yenilenmeyen sinyali yok sayar).
export const TYPING_REFRESH_MS = 2000;
export const TYPING_STALE_MS = 8000;
let typingSet = false;
let lastTypingWrite = 0;
export function setTyping(uid, typing) {
  if (!typing && !typingSet) return Promise.resolve();
  if (typing && typingSet && Date.now() - lastTypingWrite < TYPING_REFRESH_MS) return Promise.resolve();
  typingSet = typing;
  lastTypingWrite = typing ? Date.now() : 0;
  const r = ref(rtdb, `typing/${uid}`);
  if (typing) onDisconnect(r).remove().catch(() => {});
  return set(r, typing ? { typing: true, ts: rtdbServerTimestamp() } : null).catch(() => {});
}
export function subscribeTyping(partnerUid, cb) {
  return onValue(ref(rtdb, `typing/${partnerUid}`), (s) => cb(s.val()), () => cb(null));
}

// --- İletildi / görüldü ---
const lastWritten = { readAt: 0, deliveredAt: 0 };
/** Monoton artan şekilde okuma/iletme zamanını yazar. */
export function markReceipt(uid, kind, ts) {
  if (!ts || ts <= lastWritten[kind]) return;
  lastWritten[kind] = ts;
  const patch = { [kind]: ts };
  if (kind === 'readAt' && ts > lastWritten.deliveredAt) { lastWritten.deliveredAt = ts; patch.deliveredAt = ts; }
  update(ref(rtdb, `chat/readReceipts/${uid}`), patch).catch((e) => console.warn('receipt', e));
}
export function primeReceipts(own) {
  lastWritten.readAt = Math.max(lastWritten.readAt, own?.readAt || 0);
  lastWritten.deliveredAt = Math.max(lastWritten.deliveredAt, own?.deliveredAt || 0);
}
export function subscribeReceipts(cb) {
  return onValue(ref(rtdb, 'chat/readReceipts'), (s) => cb(s.val() || {}), (e) => console.warn('receipts', e));
}

export { messageStatus, unreadCount } from '../utils/chat-logic.js';
