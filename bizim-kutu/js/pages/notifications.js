// Bildirim merkezi.
import { getState, subscribe } from '../state.js';
import { userName } from '../constants.js';
import { h, clear, add } from '../utils/helpers.js';
import { icons } from '../utils/icons.js';
import { emptyState, toast, errorMessage, confirmDialog } from '../utils/ui.js';
import { relativeTime } from '../utils/dates.js';
import { markNotificationRead, markAllRead, clearNotifications, deleteNotification, NOTIF_EMOJI } from '../services/notifications.js';

export default async function notifications(page, { scope }) {
  const { partnerUid } = getState();
  const list = h('div', { class: 'notif-list' });
  const draw = () => {
    const s = getState();
    clear(list);
    if (s.unreadMessages) {
      add(list, h('a', { class: 'notif card is-unread', href: '#/chat' },
        h('span', { class: 'notif__emoji', 'aria-hidden': 'true' }, NOTIF_EMOJI.message),
        h('div', { class: 'notif__body' }, h('strong', {}, `${userName(partnerUid)}'dan ${s.unreadMessages} yeni mesaj`), h('small', { class: 'muted' }, 'Okumak için dokun'))));
    }
    if (!s.notifications.length && !s.unreadMessages) {
      add(list, emptyState({ emoji: '🔔', title: 'Her şey yolunda', text: 'Yeni anı, görev ve oyun davetleri burada görünür.' }));
      return;
    }
    for (const n of s.notifications) {
      add(list, h('div', { class: `notif card${n.read ? '' : ' is-unread'}` },
        h('span', { class: 'notif__emoji', 'aria-hidden': 'true' }, NOTIF_EMOJI[n.type] || '🔔'),
        h('a', { class: 'notif__body', href: n.link || '#/notifications', onclick: () => { if (!n.read) markNotificationRead(n.id).catch(() => {}); } },
          h('strong', {}, n.title), n.body ? h('span', {}, n.body) : null, h('small', { class: 'muted' }, relativeTime(n.createdAt))),
        h('div', { class: 'notif__actions' },
          !n.read ? h('button', { class: 'icon-btn icon-btn--sm', type: 'button', 'aria-label': 'Okundu işaretle', svg: icons.check, onclick: () => markNotificationRead(n.id).catch((e) => toast(errorMessage(e), { type: 'error' })) }) : null,
          h('button', { class: 'icon-btn icon-btn--sm', type: 'button', 'aria-label': 'Sil', svg: icons.trash, onclick: () => deleteNotification(n.id).catch((e) => toast(errorMessage(e), { type: 'error' })) }))));
    }
  };
  add(page, 
    h('div', { class: 'page-head' }, h('div', {}, h('h2', { class: 'page-title' }, 'Bildirimler'), h('p', { class: 'page-sub' }, 'Kutumuzda neler oldu?'))),
    h('div', { class: 'toolbar' },
      h('button', { class: 'chip', type: 'button', onclick: () => markAllRead().then(() => toast('Hepsi okundu')).catch((e) => toast(errorMessage(e), { type: 'error' })) }, '✓ Tümünü okundu yap'),
      h('button', { class: 'chip', type: 'button', onclick: async () => { if (await confirmDialog({ title: 'Tüm bildirimler silinsin mi?', confirmText: 'Temizle', danger: true })) clearNotifications().catch((e) => toast(errorMessage(e), { type: 'error' })); } }, '🗑 Temizle')),
    list);
  draw();
  scope.add(subscribe(draw, ['notifications', 'unreadMessages']));
}
