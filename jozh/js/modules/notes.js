// Hızlı notlar: yazdıkça otomatik kayıt (600 ms, sıralı), sabitleme, etiket süzgeci, arama.
import { initApp, renderLoadError } from '../app.js';
import { listRecords, createRecord, updateRecord, deleteRecord, restoreRecord } from '../storage/records.js';
import { el, replace, field, openDialog, toast, toastError, emptyState, loadingState, saveStatus, debounce, chip, button, confirmDialog } from '../ui.js';
import { icon } from '../utils/icons.js';
import { createAutosave } from '../utils/autosave.js';
import { parseTags, tagsToInput, collectTags, hasTag } from '../utils/tags.js';
import { matchesSearch, truncate } from '../utils/formatters.js';
import { formatDateTime } from '../utils/dates.js';
import { takeHash } from '../router.js';

const main = document.getElementById('main');
const state = { notes: [], query: '', tag: '' };
const listEl = el('div', { class: 'notes-list', 'aria-live': 'polite' });
const tagSelect = el('select', { class: 'input select', id: 'notes-tag', name: 'tag' });

function sortNotes(notes) {
  return notes.slice().sort((a, b) => (Number(b.pinned) - Number(a.pinned)) || b.updatedAt.localeCompare(a.updatedAt));
}

function renderTags() {
  const tags = collectTags(state.notes);
  replace(tagSelect, el('option', { value: '' }, 'Bütün etiketler'), tags.map((t) => el('option', { value: t }, t)));
  tagSelect.value = tags.includes(state.tag) ? state.tag : '';
  state.tag = tagSelect.value;
}

function render() {
  const visible = sortNotes(state.notes).filter((n) => hasTag(n, state.tag) && matchesSearch(state.query, n.title, n.body, n.tags));
  if (!state.notes.length) {
    replace(listEl, emptyState('Henüz not yok.', 'Yeni not', () => openEditor(null), 'note'));
    return;
  }
  if (!visible.length) {
    replace(listEl, emptyState('Aramaya uyan not yok.', null, null, 'search'));
    return;
  }
  replace(listEl, el('ul', { class: 'card-grid' }, visible.map((n) => {
    const open = el('button', { type: 'button', class: 'open-button note-open' },
      el('span', { class: 'item-title row' }, n.pinned ? icon('pin', { size: 16, label: 'Sabitlenmiş' }) : null, n.title || truncate(n.body.split('\n')[0], 60) || 'Adsız not'),
      n.body ? el('span', { class: 'item-excerpt' }, truncate(n.body, 280)) : null);
    open.addEventListener('click', () => openEditor(n));
    return el('li', { class: `card note-card${n.pinned ? ' is-pinned' : ''}` },
      open,
      el('div', { class: 'item-meta' },
        el('span', null, formatDateTime(n.updatedAt)),
        n.tags.length ? el('span', { class: 'chips' }, n.tags.map((t) => chip(t))) : null));
  })));
}

async function load() {
  replace(listEl, loadingState());
  try {
    state.notes = await listRecords('notes');
    renderTags();
    render();
  } catch (err) {
    renderLoadError(listEl, err, load);
  }
}

function openEditor(note) {
  let recordId = note ? note.id : null;
  let current = note;
  const status = saveStatus();
  const form = el('form', { class: 'form-stack', novalidate: true },
    field({ label: 'Başlık', name: 'title', value: note ? note.title : '', maxlength: 200 }),
    field({ label: 'Metin', name: 'body', type: 'textarea', value: note ? note.body : '', rows: 10, maxlength: 20000 }),
    field({ label: 'Etiketler', name: 'tags', value: note ? tagsToInput(note.tags) : '', hint: 'Virgülle ayır, en çok 20 etiket.' }),
    field({ label: 'Sabitle (listede üstte göster)', name: 'pinned', type: 'checkbox', value: note ? note.pinned : false }),
    status.node);
  form.addEventListener('submit', (e) => e.preventDefault());

  const collect = () => ({
    title: form.elements.title.value,
    body: form.elements.body.value,
    tags: parseTags(form.elements.tags.value),
    pinned: form.elements.pinned.checked
  });

  const autosave = createAutosave({
    delay: 600,
    async save(data) {
      if (!recordId) {
        if (!data.title.trim() && !data.body.trim()) return null; // boş not oluşturulmaz
        current = await createRecord('notes', data);
        recordId = current.id;
      } else {
        current = await updateRecord('notes', recordId, data);
      }
      return current;
    },
    onState(s, info) {
      if (s === 'error') {
        status.set('error', { err: info, retry: () => autosave.schedule(collect()) });
        if (info && info.fields) toast(Object.values(info.fields).join(' '), { kind: 'error' });
      } else if (s === 'saved' && !info) status.set('');
      else status.set(s);
    }
  });
  form.addEventListener('input', () => autosave.schedule(collect()));
  form.addEventListener('change', () => autosave.schedule(collect()));

  async function closeAndReload(dlg) {
    try {
      await autosave.flush();
    } catch {
      const ok = await confirmDialog({ title: 'Not kaydedilemedi', message: 'Son değişiklikler kaydedilemedi. Yine de kapatılsın mı?', confirmText: 'Kapat', danger: true });
      if (!ok) return;
    }
    await dlg.close(true);
  }

  const dlg = openDialog({
    title: note ? 'Notu düzenle' : 'Yeni not',
    content: form,
    size: 'lg',
    // Kapatma düğmesi ve Esc bekleyen kaydı tamamlar; kayıt başarısızsa bildirim çıkar.
    onClose: async () => {
      try {
        await autosave.flush();
      } catch (err) {
        toastError('notes.autosave', err);
      }
      load();
    },
    actions: [
      {
        label: 'Sil',
        kind: 'danger',
        icon: 'trash',
        className: 'mr-auto',
        onClick: async (d) => {
          autosave.cancel();
          if (!recordId) {
            await d.close(true);
            return;
          }
          try {
            const id = recordId;
            await deleteRecord('notes', id);
            await d.close(true);
            toast('Not silindi.', { actionLabel: 'Geri al', onAction: async () => { await restoreRecord('notes', id); load(); } });
          } catch (err) {
            toastError('notes.delete', err);
          }
        }
      },
      { label: 'Bitti', kind: 'primary', onClick: (d) => closeAndReload(d) }
    ]
  });
  return dlg;
}

async function setup() {
  const search = el('input', { type: 'search', class: 'input', id: 'notes-search', placeholder: 'Notlarda ara', autocomplete: 'off' });
  search.addEventListener('input', debounce(() => {
    state.query = search.value;
    render();
  }, 150));
  tagSelect.addEventListener('change', () => {
    state.tag = tagSelect.value;
    render();
  });
  replace(main,
    el('div', { class: 'page-toolbar' },
      el('div', { class: 'field search' }, el('label', { class: 'field-label', for: 'notes-search' }, 'Ara'), search),
      el('div', { class: 'field' }, el('label', { class: 'field-label', for: 'notes-tag' }, 'Etiket'), tagSelect),
      button('Yeni not', () => openEditor(null), { kind: 'primary', iconName: 'plus' })),
    listEl);
  await load();
  if (takeHash('new')) openEditor(null);
}

const ready = await initApp({ page: 'notes', title: 'Hızlı notlar' });
if (ready) await setup();
