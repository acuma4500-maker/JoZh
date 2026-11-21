// Önceki hikâyeler (Firestore: couples/main/stories)
import { h, clear, fill, add } from '../utils/helpers.js';
import { userName, userEmoji } from '../constants.js';
import { emptyState, skeletonList, errorState, errorMessage, openModal, confirmDialog, toast } from '../utils/ui.js';
import { relativeTime } from '../utils/dates.js';
import { col, listen, query, orderBy, limit, deleteItem } from '../services/firestore.js';
import { icons } from '../utils/icons.js';

export default async function stories(page, { scope }) {
  const list = h('div', { class: 'card-list' }, skeletonList(2));
  add(page, h('div', { class: 'page-head' }, h('div', {}, h('h2', { class: 'page-title' }, 'Hikâyelerimiz'), h('p', { class: 'page-sub' }, 'Birlikte yazdığımız masallar.')),
    h('a', { class: 'btn btn--primary btn--sm', href: '#/games' }, 'Yeni hikâye')), list);
  scope.add(listen(query(col('stories'), orderBy('createdAt', 'desc'), limit(50)), (items) => {
    clear(list);
    if (!items.length) { add(list, emptyState({ emoji: '📜', title: 'Henüz hikâye yok', text: 'Oyun Merkezi\'nden "Birlikte Hikâye" başlatın.' })); return; }
    for (const s of items) {
      add(list, h('article', { class: 'card story-card' },
        h('div', { class: 'card__row' }, h('h4', { class: 'card__title' }, s.title),
          h('button', { class: 'icon-btn icon-btn--sm', type: 'button', 'aria-label': 'Sil', svg: icons.trash, onclick: async () => {
            if (!(await confirmDialog({ title: 'Hikâye silinsin mi?', confirmText: 'Sil', danger: true }))) return;
            try { await deleteItem('stories', s.id); toast('Silindi'); } catch (e) { toast(errorMessage(e), { type: 'error' }); }
          } })),
        h('p', { class: 'card__text clamp-3' }, s.text),
        h('p', { class: 'card__meta' }, `${(s.lines || []).length + 1} cümle · ${relativeTime(s.createdAt)}`),
        h('button', { class: 'btn btn--ghost btn--sm', type: 'button', onclick: () => openModal({ title: s.title, wide: true, content: h('div', { class: 'story-paper story-paper--read' },
          h('p', { class: 'story-line story-line--opening' }, s.opening),
          (s.lines || []).map((l) => h('p', { class: 'story-line' }, h('span', { class: 'story-line__who', title: userName(l.uid) }, userEmoji(l.uid)), ' ', l.text))) }) }, 'Oku')));
    }
  }, (e) => fill(list, errorState(errorMessage(e)))));
}
