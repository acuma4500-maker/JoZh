// Hayaller ve hedefler: ilerleme, durum, öncelik, süzgeç ve sıralama, 1 fotoğraf.
import { initApp, renderLoadError } from '../app.js';
import { listRecords, createRecord, updateRecord, deleteRecord, restoreRecord } from '../storage/records.js';
import { el, replace, field, openDialog, toast, toastError, emptyState, loadingState, debounce, chip, button, showFieldErrors, clearFieldErrors, progressBar, segmented, uid } from '../ui.js';
import { PRIORITIES, PRIORITY_ORDER, DREAM_STATUS, DREAM_CATEGORIES } from '../utils/labels.js';
import { matchesSearch, truncate } from '../utils/formatters.js';
import { formatDate, todayISO, diffDays } from '../utils/dates.js';
import { createPhotoField, avatar } from '../components/photos.js';
import { takeHash } from '../router.js';

const main = document.getElementById('main');
const state = { dreams: [], query: '', filter: 'active', sort: 'priority' };
const listEl = el('div', { class: 'dreams-list', 'aria-live': 'polite' });

const STATUS_KIND = { notStarted: '', inProgress: 'accent', completed: 'green', postponed: 'yellow' };
const PRIORITY_KIND = { high: 'red', medium: 'yellow', low: '' };

function filtered() {
  return state.dreams
    .filter((d) => {
      if (state.filter === 'active') return d.status === 'notStarted' || d.status === 'inProgress';
      if (state.filter === 'completed') return d.status === 'completed';
      if (state.filter === 'postponed') return d.status === 'postponed';
      return true;
    })
    .filter((d) => matchesSearch(state.query, d.title, d.description, d.category, d.notes))
    .sort((a, b) => {
      if (state.sort === 'target') {
        const at = a.targetDate || '9999-12-31';
        const bt = b.targetDate || '9999-12-31';
        return at.localeCompare(bt) || PRIORITY_ORDER[a.priority] - PRIORITY_ORDER[b.priority];
      }
      if (state.sort === 'updated') return b.updatedAt.localeCompare(a.updatedAt);
      return PRIORITY_ORDER[a.priority] - PRIORITY_ORDER[b.priority] || (a.targetDate || '9999').localeCompare(b.targetDate || '9999');
    });
}

function targetInfo(d) {
  if (!d.targetDate) return null;
  const left = diffDays(todayISO(), d.targetDate);
  if (d.status !== 'completed' && left < 0) return el('span', { class: 'text-red' }, `Hedef tarihi geçti: ${formatDate(d.targetDate)}`);
  return el('span', null, `Hedef: ${formatDate(d.targetDate)}${d.status !== 'completed' && left >= 0 ? ` (${left === 0 ? 'bugün' : `${left} gün`})` : ''}`);
}

function render() {
  if (!state.dreams.length) {
    replace(listEl, emptyState('Henüz hayal ya da hedef yok.', 'Hedef ekle', () => openEditor(null), 'target'));
    return;
  }
  const visible = filtered();
  if (!visible.length) {
    replace(listEl, emptyState('Bu süzgece uyan hedef yok.', null, null, 'search'));
    return;
  }
  replace(listEl, el('ul', { class: 'card-grid' }, visible.map((d) => {
    const open = el('button', { type: 'button', class: 'open-button' },
      el('span', { class: 'row dream-head' },
        d.photoId ? avatar({ photoId: d.photoId, text: '', size: 'sm' }) : null,
        el('span', { class: 'item-title grow' }, d.title)),
      d.description ? el('span', { class: 'item-excerpt' }, truncate(d.description, 160)) : null);
    open.addEventListener('click', () => openEditor(d));
    const actions = el('div', { class: 'row mt' });
    if (d.status !== 'completed') {
      actions.append(button('Tamamlandı olarak işaretle', async () => {
        try {
          await updateRecord('dreams', d.id, { status: 'completed', progress: 100 });
          toast('Hedef tamamlandı olarak işaretlendi.', { kind: 'success' });
          load();
        } catch (err) {
          toastError('dreams.complete', err);
        }
      }, { iconName: 'check', className: 'btn-small' }));
    }
    return el('li', { class: 'card dream-card' },
      open,
      el('div', { class: 'chips mt' },
        chip(DREAM_STATUS[d.status], { kind: STATUS_KIND[d.status] }),
        chip(`Öncelik: ${PRIORITIES[d.priority]}`, { kind: PRIORITY_KIND[d.priority] }),
        d.category ? chip(d.category) : null),
      el('div', { class: 'progress-row mt' }, progressBar(d.progress, `${d.title} ilerlemesi`), el('span', { class: 'small' }, `%${d.progress}`)),
      el('div', { class: 'item-meta' }, targetInfo(d)),
      actions);
  })));
}

async function load() {
  replace(listEl, loadingState());
  try {
    state.dreams = await listRecords('dreams');
    render();
  } catch (err) {
    renderLoadError(listEl, err, load);
  }
}

function openEditor(dream) {
  const d = dream || { title: '', description: '', category: '', targetDate: '', priority: 'medium', progress: 0, status: 'notStarted', notes: '', photoId: null };
  const photos = createPhotoField({ label: 'Fotoğraf', max: 1, initial: d.photoId ? [d.photoId] : [] });
  const listId = uid('cats');
  const progressOut = el('output', { class: 'progress-out' }, `%${d.progress}`);
  const progressId = uid('progress');
  const range = el('input', { type: 'range', id: progressId, name: 'progress', min: '0', max: '100', step: '5', value: String(d.progress), 'aria-valuetext': `%${d.progress}` });
  const form = el('form', { class: 'form-stack', novalidate: true },
    el('div', { class: 'form-grid' },
      field({ label: 'Başlık', name: 'title', value: d.title, required: true, maxlength: 200, className: 'span-all' }),
      field({ label: 'Kategori', name: 'category', value: d.category, maxlength: 60, list: listId }),
      field({ label: 'Hedef tarihi', name: 'targetDate', type: 'date', value: d.targetDate }),
      field({ label: 'Öncelik', name: 'priority', type: 'select', value: d.priority, options: Object.entries(PRIORITIES) }),
      field({ label: 'Durum', name: 'status', type: 'select', value: d.status, options: Object.entries(DREAM_STATUS) })),
    el('datalist', { id: listId }, DREAM_CATEGORIES.map((c) => el('option', { value: c }))),
    el('div', { class: 'field' }, el('label', { class: 'field-label', for: progressId }, 'İlerleme ', progressOut), range, el('p', { id: `${progressId}-error`, class: 'field-error', hidden: true })),
    field({ label: 'Açıklama', name: 'description', type: 'textarea', value: d.description, rows: 3, maxlength: 2000 }),
    field({ label: 'Notlar', name: 'notes', type: 'textarea', value: d.notes, rows: 3, maxlength: 5000 }),
    photos.node);
  form.addEventListener('submit', (e) => e.preventDefault());

  const statusSel = form.elements.status;
  let prevStatus = statusSel.value;
  range.addEventListener('input', () => {
    const v = Number(range.value);
    progressOut.textContent = `%${v}`;
    range.setAttribute('aria-valuetext', `%${v}`);
    if (v === 100) statusSel.value = 'completed';
    else if (statusSel.value === 'completed') statusSel.value = 'inProgress';
    else if (v > 0 && statusSel.value === 'notStarted') statusSel.value = 'inProgress';
    prevStatus = statusSel.value;
  });
  statusSel.addEventListener('change', () => {
    if (statusSel.value === 'completed') {
      range.value = '100';
    } else if (prevStatus === 'completed' && Number(range.value) === 100) {
      range.value = '90';
    }
    progressOut.textContent = `%${range.value}`;
    prevStatus = statusSel.value;
  });

  const collect = () => {
    const f = form.elements;
    return {
      title: f.title.value, category: f.category.value, targetDate: f.targetDate.value, priority: f.priority.value,
      status: f.status.value, progress: Number(range.value), description: f.description.value, notes: f.notes.value, photoId: photos.getId()
    };
  };
  const initial = JSON.stringify(collect());

  async function save(dlg) {
    clearFieldErrors(form);
    try {
      const saved = dream ? await updateRecord('dreams', dream.id, collect()) : await createRecord('dreams', collect());
      await photos.commit(`dreams:${saved.id}`);
      await dlg.close(true);
      toast(dream ? 'Hedef güncellendi.' : 'Hedef eklendi.', { kind: 'success' });
      load();
    } catch (err) {
      if (err.fields) showFieldErrors(form, err.fields);
      else toastError('dreams.save', err, () => save(dlg));
    }
  }

  const actions = [];
  if (dream) {
    actions.push({
      label: 'Sil', kind: 'danger', icon: 'trash', className: 'mr-auto',
      onClick: async (dlg) => {
        try {
          await photos.discard();
          await deleteRecord('dreams', dream.id);
          await dlg.close(true);
          toast('Hedef silindi.', { actionLabel: 'Geri al', onAction: async () => { await restoreRecord('dreams', dream.id); load(); } });
          load();
        } catch (err) {
          toastError('dreams.delete', err);
        }
      }
    });
  }
  actions.push({ label: 'Vazgeç', onClick: (dlg) => dlg.close() });
  actions.push({ label: 'Kaydet', kind: 'primary', onClick: (dlg) => save(dlg) });

  return openDialog({
    title: dream ? 'Hedefi düzenle' : 'Yeni hedef',
    content: form,
    size: 'lg',
    actions,
    isDirty: () => JSON.stringify(collect()) !== initial || photos.isDirty(),
    onClose: () => photos.discard()
  });
}

async function setup() {
  const search = el('input', { type: 'search', class: 'input', id: 'dreams-search', placeholder: 'Hedeflerde ara', autocomplete: 'off' });
  search.addEventListener('input', debounce(() => {
    state.query = search.value;
    render();
  }, 150));
  const sortSel = el('select', { class: 'input select', id: 'dreams-sort' },
    el('option', { value: 'priority' }, 'Önceliğe göre'),
    el('option', { value: 'target' }, 'Hedef tarihine göre'),
    el('option', { value: 'updated' }, 'Son güncellenen'));
  sortSel.addEventListener('change', () => {
    state.sort = sortSel.value;
    render();
  });
  replace(main,
    el('div', { class: 'page-toolbar' },
      el('div', { class: 'field search' }, el('label', { class: 'field-label', for: 'dreams-search' }, 'Ara'), search),
      el('div', { class: 'field' }, el('label', { class: 'field-label', for: 'dreams-sort' }, 'Sıralama'), sortSel),
      button('Hedef ekle', () => openEditor(null), { kind: 'primary', iconName: 'plus' })),
    el('div', { class: 'row filter-row' },
      segmented([['active', 'Aktif'], ['completed', 'Tamamlanan'], ['postponed', 'Ertelenen'], ['all', 'Tümü']], state.filter, (v) => {
        state.filter = v;
        render();
      }, 'Durum süzgeci')),
    listEl);
  await load();
  if (takeHash('new')) openEditor(null);
}

const ready = await initApp({ page: 'dreams', title: 'Hayaller ve hedefler' });
if (ready) await setup();
