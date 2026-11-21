// Uygulama içi bildirim merkezi (Firestore: couples/main/notifications).
// Mesaj bildirimleri ayrıca sohbetin okundu bilgisinden türetilir (her mesaj için belge yazılmaz).
import { col, docRef, listen, query, where, orderBy, limit, serverTimestamp } from './firestore.js';
import { addDoc, updateDoc, writeBatch, deleteDoc } from '../vendor/firebase.js';
import { db } from '../firebase-config.js';
import { getState, setState } from '../state.js';
import { cleanText, LIMITS } from '../utils/validation.js';
import { toast } from '../utils/ui.js';

const PREF_OF = { message: 'message', game_invite: 'game', game_accept: 'game', memory: 'memory', task: 'task', task_done: 'task' };
export const NOTIF_EMOJI = { message: '💬', game_invite: '🎮', game_accept: '🎉', memory: '📖', task: '📝', task_done: '✅' };

export function allowed(type) {
  const p = getState().prefs?.notif || {};
  return p[PREF_OF[type]] !== false;
}

/** Partnere bildirim gönderir. Başarısız olsa bile ana işlemi engellemez. */
export async function notify(type, { title, body = '', link = '' }) {
  const { uid, partnerUid } = getState();
  if (!uid || !partnerUid) return;
  try {
    await addDoc(col('notifications'), {
      type, to: partnerUid, from: uid,
      title: cleanText(title, LIMITS.notifTitle, { multiline: false }),
      body: cleanText(body, LIMITS.notifBody, { multiline: false }),
      link: String(link).slice(0, 100), read: false, createdAt: serverTimestamp()
    });
  } catch (e) { console.warn('bildirim gönderilemedi', e); }
}

let seen = null;
export function startNotifications(uid, onNew) {
  seen = null;
  const q = query(col('notifications'), where('to', '==', uid), orderBy('createdAt', 'desc'), limit(40));
  return listen(q, (items) => {
    const first = seen === null;
    seen ||= new Set();
    for (const n of items) {
      if (!seen.has(n.id)) {
        seen.add(n.id);
        if (!first && !n.read && allowed(n.type)) onNew?.(n);
      }
    }
    setState({ notifications: items });
  }, () => {});
}

export const markNotificationRead = (id) => updateDoc(docRef('notifications', id), { read: true });

export async function markAllRead() {
  const unread = getState().notifications.filter((n) => !n.read);
  if (!unread.length) return;
  const batch = writeBatch(db);
  unread.forEach((n) => batch.update(docRef('notifications', n.id), { read: true }));
  await batch.commit();
}

export async function clearNotifications() {
  const items = getState().notifications;
  const batch = writeBatch(db);
  items.forEach((n) => batch.delete(docRef('notifications', n.id)));
  await batch.commit();
}

export const deleteNotification = (id) => deleteDoc(docRef('notifications', id));

/** Sekme arka plandayken tarayıcı bildirimi (izin verildiyse). Push altyapısı gerektirmez. */
export function systemNotify(title, body, link) {
  try {
    if (!getState().prefs.system || !('Notification' in window) || Notification.permission !== 'granted') return;
    if (document.visibilityState === 'visible') return;
    const n = new Notification(title, { body, icon: 'assets/icons/icon-192.png', tag: link || 'bizim-kutu', badge: 'assets/icons/icon-192.png' });
    n.onclick = () => { window.focus(); if (link) location.hash = link; n.close(); };
  } catch {}
}

export function announce(n) {
  const emoji = NOTIF_EMOJI[n.type] || '🔔';
  toast(`${emoji} ${n.title}`, { duration: 4500, action: n.link ? { label: 'Aç', onClick: () => { location.hash = n.link; } } : undefined });
  systemNotify(n.title, n.body, n.link);
}
