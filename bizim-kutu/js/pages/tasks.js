// Ortak yapılacaklar (Firestore: couples/main/tasks).
import { getState } from '../state.js';
import { userName } from '../constants.js';
import { h, clear, fill, add } from '../utils/helpers.js';
import { icons } from '../utils/icons.js';
import { toast, confirmDialog, emptyState, openModal, skeletonList, errorState, field, counted, errorMessage, setLoading } from '../utils/ui.js';
import { dueLabel, formatISODate, relativeTime } from '../utils/dates.js';
import { LIMITS, validateText, isISODate } from '../utils/validation.js';
import { col, listen, query, where, orderBy, limit, createItem, updateItem, deleteItem } from '../services/firestore.js';
import { notify } from '../services/notifications.js';
import { serverTimestamp } from '../vendor/firebase.js';

const PRIORITY = { high: { label: 'Yüksek', emoji: '🔥', rank: 0 }, medium: { label: 'Orta', emoji: '🌤️', rank: 1 }, low: { label: 'Düşük', emoji: '🌱', rank: 2 } };

/** Sıralama: son tarihi olanlar önce (yakından uzağa), sonra önceliğe göre. */
export function sortTasks(items) {
  return [...items].sort((a, b) => {
    if (!!a.dueDate !== !!b.dueDate) return a.dueDate ? -1 : 1;
    if (a.dueDate !== b.dueDate) return a.dueDate < b.dueDate ? -1 : 1;
    return (PRIORITY[a.priority]?.rank ?? 1) - (PRIORITY[b.priority]?.rank ?? 1);
  });
}

export default async function tasks(page, { scope }) {
  const { uid } = getState();
  let tab = 'open';
  let unsub = null;
  const listEl = h('div', { class: 'card-list' });
  const counts = h('span', { class: 'muted' });
  const tabsEl = h('div', { class: 'tabs', role: 'tablist' });
  const drawTabs = () => fill(tabsEl, 
    ...[['open', '⏳ Yapılacaklar'], ['done', '✅ Tamamlananlar']].map(([id, label]) => h('button', {
      class: `tabs__btn${tab === id ? ' is-active' : ''}`, type: 'button', role: 'tab', 'aria-selected': String(tab === id),
      onclick: () => { tab = id; drawTabs(); sub(); } }, label)));

  function sub() {
    unsub?.();
    fill(listEl, skeletonList(3));
    // Tek alana göre sıralı tek sorgu; bekleyen/tamamlanan ayrımı cihazda yapılır (Firestore'da ek dizin gerekmez).
    const q = query(col('tasks'), orderBy('createdAt', 'desc'), limit(300));
    unsub = listen(q, (all) => {
      const ms = (x) => x?.toMillis?.() || 0;
      draw(tab === 'open' ? sortTasks(all.filter((t) => !t.done)) : all.filter((t) => t.done).sort((a, b) => ms(b.doneAt) - ms(a.doneAt)));
    }, (e) => fill(listEl, errorState(errorMessage(e), sub)));
  }
  scope.add(() => unsub?.());

  function draw(items) {
    clear(listEl);
    counts.textContent = `${items.length} görev`;
    if (!items.length) {
      add(listEl, tab === 'open'
        ? emptyState({ emoji: '✨', title: 'Hepsi tamam!', text: 'Yeni bir plan, bir hayal, bir alışveriş listesi… Ekleyin.', action: { label: 'Görev ekle', onClick: () => editor() } })
        : emptyState({ emoji: '🌱', title: 'Henüz tamamlanan yok', text: 'Birlikte bitirdikleriniz burada görünecek.' }));
      return;
    }
    for (const t of items) {
      const p = PRIORITY[t.priority] || PRIORITY.medium;
      const due = t.dueDate ? dueLabel(t.dueDate) : '';
      const box = h('button', { class: `task-check${t.done ? ' is-done' : ''}`, type: 'button', role: 'checkbox', 'aria-checked': String(!!t.done), 'aria-label': t.done ? 'Tamamlanmadı olarak işaretle' : 'Tamamlandı olarak işaretle', svg: icons.check, onclick: () => toggle(t) });
      add(listEl, h('article', { class: `card task task--${t.priority || 'medium'}${t.done ? ' task--done' : ''}` },
        h('div', { class: 'card__row' }, box,
          h('div', { class: 'task__main' },
            h('h4', { class: 'card__title' }, t.title),
            t.description ? h('p', { class: 'card__text' }, t.description) : null,
            h('div', { class: 'task__tags' },
              h('span', { class: `pill pill--${t.priority || 'medium'}` }, `${p.emoji} ${p.label}`),
              t.dueDate ? h('span', { class: `pill${due.includes('gecikti') && !t.done ? ' pill--danger' : ''}` }, `📅 ${formatISODate(t.dueDate)} · ${due}`) : null),
            h('p', { class: 'card__meta' }, t.done ? `${userName(t.doneBy)} tamamladı · ${relativeTime(t.doneAt)}` : `${userName(t.createdBy)} ekledi · ${relativeTime(t.createdAt)}`)),
          h('div', { class: 'card__actions' },
            h('button', { class: 'icon-btn icon-btn--sm', type: 'button', 'aria-label': 'Düzenle', svg: icons.edit, onclick: () => editor(t) }),
            h('button', { class: 'icon-btn icon-btn--sm', type: 'button', 'aria-label': 'Sil', svg: icons.trash, onclick: () => remove(t) })))));
    }
  }

  async function toggle(t) {
    try {
      const done = !t.done;
      await updateItem('tasks', t.id, done ? { done: true, doneBy: uid, doneAt: serverTimestamp() } : { done: false, doneBy: '', doneAt: null });
      if (done) { toast('Harika! Görev tamamlandı ✅'); notify('task_done', { title: `Görev tamamlandı: ${t.title}`, body: `${userName(uid)} işaretledi`, link: '#/tasks' }); }
    } catch (e) { toast(errorMessage(e), { type: 'error' }); }
  }
  async function remove(t) {
    if (!(await confirmDialog({ title: 'Görev silinsin mi?', message: `"${t.title}" silinecek.`, confirmText: 'Sil', danger: true }))) return;
    try { await deleteItem('tasks', t.id); toast('Görev silindi'); } catch (e) { toast(errorMessage(e), { type: 'error' }); }
  }

  function editor(t = null) {
    const title = h('input', { class: 'input', value: t?.title || '', placeholder: 'Örn. Hafta sonu piknik', required: true });
    const desc = h('textarea', { class: 'input', rows: '3', placeholder: 'Detaylar (isteğe bağlı)', value: t?.description || '' });
    const due = h('input', { class: 'input', type: 'date', value: t?.dueDate || '' });
    const prio = h('select', { class: 'input' }, Object.entries(PRIORITY).map(([k, v]) => h('option', { value: k, selected: (t?.priority || 'medium') === k }, `${v.emoji} ${v.label}`)));
    const err = h('p', { class: 'form-error', role: 'alert' });
    const save = h('button', { class: 'btn btn--primary btn--block', type: 'submit' }, t ? 'Kaydet' : 'Görev ekle');
    const form = h('form', { class: 'form', novalidate: true, onsubmit: async (e) => {
      e.preventDefault();
      const tt = validateText(title.value, { label: 'Başlık', max: LIMITS.taskTitle, multiline: false });
      const dd = validateText(desc.value, { label: 'Açıklama', min: 0, max: LIMITS.taskText });
      if (!tt.ok || !dd.ok) { err.textContent = (tt.ok ? dd : tt).error; return; }
      if (due.value && !isISODate(due.value)) { err.textContent = 'Geçerli bir tarih seç.'; return; }
      setLoading(save, true, 'Kaydediliyor…');
      const data = { title: tt.value, description: dd.value, dueDate: due.value || '', priority: prio.value };
      try {
        if (t) await updateItem('tasks', t.id, data);
        else {
          await createItem('tasks', { ...data, done: false, doneBy: '', doneAt: null });
          notify('task', { title: `Yeni görev: ${data.title}`, body: data.dueDate ? `Son tarih: ${formatISODate(data.dueDate)}` : '', link: '#/tasks' });
        }
        toast(t ? 'Görev güncellendi' : 'Görev eklendi 📝');
        modal.close();
      } catch (e2) { err.textContent = errorMessage(e2); setLoading(save, false); }
    } },
      field('Başlık', title), field('Açıklama', counted(desc, LIMITS.taskText)),
      h('div', { class: 'grid-2' }, field('Son tarih', due), field('Öncelik', prio)), err, save);
    const modal = openModal({ title: t ? 'Görevi düzenle' : 'Yeni görev', content: form });
  }

  add(page, 
    h('div', { class: 'page-head' },
      h('div', {}, h('h2', { class: 'page-title' }, 'Yapılacaklar'), h('p', { class: 'page-sub' }, 'Ortak planlarımız, hayallerimiz.')),
      h('button', { class: 'btn btn--primary', type: 'button', onclick: () => editor() }, h('span', { svg: icons.plus }), 'Görev ekle')),
    tabsEl, h('div', { class: 'toolbar' }, counts), listEl);
  drawTabs(); sub();
}
