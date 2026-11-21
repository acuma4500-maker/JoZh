// Anı Defteri (Firestore: couples/main/memories) — zaman çizelgesi görünümü.
import { userName } from '../constants.js';
import { h, clear, fill, add } from '../utils/helpers.js';
import { icons } from '../utils/icons.js';
import { toast, confirmDialog, emptyState, openModal, skeletonList, errorState, field, counted, emojiPicker, errorMessage, setLoading } from '../utils/ui.js';
import { formatISODate, parseISODate, todayISO, relativeTime } from '../utils/dates.js';
import { LIMITS, validateText, isISODate } from '../utils/validation.js';
import { col, listen, query, orderBy, limit, createItem, updateItem, deleteItem } from '../services/firestore.js';
import { notify } from '../services/notifications.js';

const MONTHS = ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran', 'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık'];

export default async function memories(page, { scope }) {
  let pageSize = 30;
  let unsub = null;
  let order = 'desc';
  const listEl = h('div', { class: 'timeline' }, skeletonList(3));
  const more = h('button', { class: 'btn btn--ghost btn--block', type: 'button', hidden: true, onclick: () => { pageSize += 30; sub(); } }, 'Daha fazla anı');
  const orderBtn = h('button', { class: 'chip', type: 'button', onclick: () => { order = order === 'desc' ? 'asc' : 'desc'; orderBtn.textContent = order === 'desc' ? 'En yeni önce' : 'En eski önce'; sub(); } }, 'En yeni önce');

  function sub() {
    unsub?.();
    // Tek alana göre sıralama: Firestore'da ek (bileşik) dizin gerekmez. Aynı gündeki anılar eklenme sırasına göre.
    unsub = listen(query(col('memories'), orderBy('date', order), limit(pageSize)), (items) => {
      const t = (m) => m.createdAt?.toMillis?.() || 0;
      items.sort((a, b) => (a.date === b.date ? (order === 'desc' ? t(b) - t(a) : t(a) - t(b)) : 0));
      draw(items);
      more.hidden = items.length < pageSize;
    }, (e) => fill(listEl, errorState(errorMessage(e), sub)));
  }
  scope.add(() => unsub?.());

  function draw(items) {
    clear(listEl);
    if (!items.length) {
      add(listEl, emptyState({ emoji: '📖', title: 'Anı defteriniz boş', text: 'İlk buluşmanız, ilk "günaydın"ınız… Hepsini buraya yazın.', action: { label: 'İlk anıyı ekle', onClick: () => editor() } }));
      return;
    }
    let lastGroup = '';
    for (const m of items) {
      const d = parseISODate(m.date);
      const group = d ? `${MONTHS[d.getMonth()]} ${d.getFullYear()}` : 'Tarihsiz';
      if (group !== lastGroup) { add(listEl, h('h3', { class: 'timeline__group' }, group)); lastGroup = group; }
      add(listEl, h('article', { class: 'timeline__item card' },
        h('div', { class: 'timeline__dot', 'aria-hidden': 'true' }, m.emoji || '💗'),
        h('div', { class: 'timeline__content' },
          h('div', { class: 'card__row' },
            h('h4', { class: 'card__title' }, m.title),
            h('div', { class: 'card__actions' },
              h('button', { class: 'icon-btn icon-btn--sm', type: 'button', 'aria-label': 'Düzenle', svg: icons.edit, onclick: () => editor(m) }),
              h('button', { class: 'icon-btn icon-btn--sm', type: 'button', 'aria-label': 'Sil', svg: icons.trash, onclick: () => remove(m) }))),
          h('p', { class: 'card__date' }, h('span', { svg: icons.calendar }), formatISODate(m.date)),
          m.description ? h('p', { class: 'card__text' }, m.description) : null,
          h('p', { class: 'card__meta' }, `${userName(m.createdBy)} ekledi · ${relativeTime(m.createdAt)}`,
            m.updatedBy && (m.updatedBy !== m.createdBy || (m.updatedAt?.toMillis?.() || 0) - (m.createdAt?.toMillis?.() || 0) > 60000) ? ` · ${userName(m.updatedBy)} düzenledi ${relativeTime(m.updatedAt)}` : ''))));
    }
  }

  async function remove(m) {
    if (!(await confirmDialog({ title: 'Anı silinsin mi?', message: `"${m.title}" kalıcı olarak silinecek.`, confirmText: 'Sil', danger: true }))) return;
    try { await deleteItem('memories', m.id); toast('Anı silindi'); } catch (e) { toast(errorMessage(e), { type: 'error' }); }
  }

  function editor(m = null) {
    let emoji = m?.emoji || '💗';
    const title = h('input', { class: 'input', value: m?.title || '', placeholder: 'Örn. İlk kahvemiz', required: true });
    const date = h('input', { class: 'input', type: 'date', value: m?.date || todayISO(), required: true, max: '2100-12-31' });
    const desc = h('textarea', { class: 'input', rows: '5', placeholder: 'O gün neler oldu?', value: m?.description || '' });
    const emojiBtn = h('button', { class: 'emoji-choice', type: 'button', 'aria-label': 'Emoji seç' }, emoji);
    const picker = emojiPicker((e) => { emoji = e; emojiBtn.textContent = e; picker.hidden = true; });
    picker.hidden = true;
    emojiBtn.addEventListener('click', () => { picker.hidden = !picker.hidden; });
    const err = h('p', { class: 'form-error', role: 'alert' });
    const save = h('button', { class: 'btn btn--primary btn--block', type: 'submit' }, m ? 'Kaydet' : 'Anıyı ekle');
    const form = h('form', { class: 'form', novalidate: true, onsubmit: async (e) => {
      e.preventDefault();
      const t = validateText(title.value, { label: 'Başlık', max: LIMITS.memoryTitle, multiline: false });
      const d = validateText(desc.value, { label: 'Açıklama', min: 0, max: LIMITS.memoryText });
      if (!t.ok) { err.textContent = t.error; return; }
      if (!d.ok) { err.textContent = d.error; return; }
      if (!isISODate(date.value)) { err.textContent = 'Geçerli bir tarih seç.'; return; }
      setLoading(save, true, 'Kaydediliyor…');
      const data = { title: t.value, date: date.value, description: d.value, emoji };
      try {
        if (m) { await updateItem('memories', m.id, data); toast('Anı güncellendi 💗'); }
        else { await createItem('memories', data); toast('Anı deftere eklendi 📖'); notify('memory', { title: `Yeni anı: ${data.title}`, body: formatISODate(data.date), link: '#/memories' }); }
        modal.close();
      } catch (e2) { err.textContent = errorMessage(e2); setLoading(save, false); }
    } },
      h('div', { class: 'field' }, h('span', { class: 'field__label' }, 'Emoji'), emojiBtn, picker),
      field('Başlık', title), field('Tarih', date), field('Açıklama', counted(desc, LIMITS.memoryText)), err, save);
    const modal = openModal({ title: m ? 'Anıyı düzenle' : 'Yeni anı', content: form });

  }

  add(page, 
    h('div', { class: 'page-head' },
      h('div', {}, h('h2', { class: 'page-title' }, 'Anı Defteri'), h('p', { class: 'page-sub' }, 'Birlikte biriktirdiğimiz her şey.')),
      h('button', { class: 'btn btn--primary', type: 'button', onclick: () => editor() }, h('span', { svg: icons.plus }), 'Anı ekle')),
    h('div', { class: 'toolbar' }, orderBtn), listEl, more);
  sub();
}
