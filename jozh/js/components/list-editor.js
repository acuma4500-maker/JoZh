// Düzenlenebilir madde listesi (hazırlık listesi, sevdikleri, yapılacaklar…) ve işaretlenebilir liste görünümü.
import { el, iconButton, button, uid } from '../ui.js';
import { shortId } from '../utils/id-generator.js';

// options: { label, items, checkable, placeholder, max, addLabel, maxLength }
export function createListEditor({ label, items = [], checkable = false, placeholder = '', max = 100, addLabel = 'Madde ekle', maxLength = 200 } = {}) {
  const listId = uid('list');
  const list = el('div', { class: 'edit-list', id: listId });
  const errorEl = el('p', { class: 'field-error', hidden: true });
  const addBtn = button(addLabel, () => addRow({ id: shortId(), text: '', done: false }, true), { iconName: 'plus', className: 'btn-small' });
  const node = el('div', { class: 'field list-editor' }, el('span', { class: 'field-label' }, label), list, errorEl, el('div', null, addBtn));

  function renumber() {
    [...list.children].forEach((row, i) => {
      const input = row.querySelector('input[type="text"]');
      input.setAttribute('aria-label', `${label} ${i + 1}`);
      const cb = row.querySelector('input[type="checkbox"]');
      if (cb) cb.setAttribute('aria-label', `${label} ${i + 1} tamamlandı`);
      row.querySelector('.btn-icon').setAttribute('aria-label', `${label} ${i + 1} maddesini sil`);
    });
    addBtn.disabled = list.children.length >= max;
  }

  function addRow(item, focus = false) {
    if (list.children.length >= max) return;
    const row = el('div', { class: 'edit-row', dataset: { id: item.id || shortId() } });
    if (checkable) row.append(el('input', { type: 'checkbox', class: 'checkbox', checked: Boolean(item.done) }));
    const input = el('input', { type: 'text', class: 'input', value: item.text || '', placeholder, maxlength: maxLength });
    input.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') {
        e.preventDefault();
        if (input.value.trim()) addRow({ id: shortId(), text: '', done: false }, true);
      }
    });
    row.append(input, iconButton('trash', 'Sil', () => {
      const next = row.nextElementSibling || row.previousElementSibling;
      row.remove();
      renumber();
      if (next) next.querySelector('input[type="text"]').focus();
      else addBtn.focus();
    }));
    list.append(row);
    renumber();
    if (focus) input.focus();
  }

  for (const item of items) addRow(item);
  renumber();

  return {
    node,
    getItems() {
      return [...list.children]
        .map((row) => {
          const text = row.querySelector('input[type="text"]').value.trim();
          const out = { id: row.dataset.id, text };
          if (checkable) out.done = row.querySelector('input[type="checkbox"]').checked;
          return out;
        })
        .filter((i) => i.text);
    },
    showError(message) {
      errorEl.textContent = message || '';
      errorEl.hidden = !message;
    }
  };
}

// Kartlarda işaretlenebilir liste. onToggle(id, done) kaydı günceller.
export function checkListView(items, onToggle, { emptyText = 'Henüz madde yok' } = {}) {
  if (!items || !items.length) return el('p', { class: 'muted small' }, emptyText);
  const list = el('ul', { class: 'check-list' });
  for (const item of items) {
    const id = uid('chk');
    const cb = el('input', { type: 'checkbox', id, class: 'checkbox', checked: Boolean(item.done) });
    const row = el('li', { class: `check-row${item.done ? ' is-done' : ''}` }, cb, el('label', { for: id, class: 'check-text' }, item.text));
    cb.addEventListener('change', async () => {
      cb.disabled = true;
      try {
        await onToggle(item.id, cb.checked);
        row.classList.toggle('is-done', cb.checked);
      } catch {
        cb.checked = !cb.checked;
      } finally {
        cb.disabled = false;
      }
    });
    list.append(row);
  }
  return list;
}

export function textListView(items, { emptyText = 'Henüz eklenmedi' } = {}) {
  if (!items || !items.length) return el('p', { class: 'muted small' }, emptyText);
  return el('ul', { class: 'chips text-list' }, items.map((i) => el('li', { class: 'chip' }, i.text)));
}
