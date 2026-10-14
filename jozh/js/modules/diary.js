// Günlük: okuma görünümü, düzenleme, taslak (800 ms'de bir), en çok 20 fotoğraf, arama, tarih ve etiket süzgeci.
import { initApp, renderLoadError } from '../app.js';
import { listRecords, getRecord, createRecord, updateRecord, deleteRecord, restoreRecord } from '../storage/records.js';
import * as db from '../storage/local-db.js';
import { el, replace, field, openDialog, toast, toastError, emptyState, loadingState, saveStatus, debounce, chip, button, confirmDialog, showFieldErrors, clearFieldErrors } from '../ui.js';
import { createAutosave } from '../utils/autosave.js';
import { parseTags, tagsToInput, collectTags, hasTag } from '../utils/tags.js';
import { matchesSearch, truncate } from '../utils/formatters.js';
import { formatDate, todayISO } from '../utils/dates.js';
import { createPhotoField, thumbStrip, openViewer } from '../components/photos.js';
import { defaultSource } from '../storage/image-storage.js';
import { takeHash } from '../router.js';

const main = document.getElementById('main');
const state = { entries: [], query: '', from: '', to: '', tag: '' };
const listEl = el('div', { class: 'diary-list', 'aria-live': 'polite' });
const tagSelect = el('select', { class: 'input select', id: 'diary-tag' });

const draftKey = (id) => `draft:diary:${id || 'new'}`;

function sortEntries(list) {
  return list.slice().sort((a, b) => b.date.localeCompare(a.date) || b.createdAt.localeCompare(a.createdAt));
}

function renderTags() {
  const tags = collectTags(state.entries);
  replace(tagSelect, el('option', { value: '' }, 'Bütün etiketler'), tags.map((t) => el('option', { value: t }, t)));
  tagSelect.value = tags.includes(state.tag) ? state.tag : '';
  state.tag = tagSelect.value;
}

function render() {
  if (!state.entries.length) {
    replace(listEl, emptyState('Henüz günlük yazısı yok.', 'Yeni yazı', () => openEditor(null), 'book'));
    return;
  }
  const visible = sortEntries(state.entries).filter((e) => hasTag(e, state.tag)
    && (!state.from || e.date >= state.from) && (!state.to || e.date <= state.to)
    && matchesSearch(state.query, e.title, e.body, e.tags));
  if (!visible.length) {
    replace(listEl, emptyState('Süzgece uyan yazı yok.', null, null, 'search'));
    return;
  }
  replace(listEl, el('ul', { class: 'list' }, visible.map((e) => {
    const open = el('button', { type: 'button', class: 'open-button' },
      el('span', { class: 'item-title' }, e.title),
      el('span', { class: 'item-meta' }, el('span', null, formatDate(e.date, { weekday: true })), e.photoIds.length ? el('span', null, `${e.photoIds.length} fotoğraf`) : null),
      e.body ? el('span', { class: 'item-excerpt' }, truncate(e.body, 300)) : null);
    open.addEventListener('click', () => openReader(e));
    return el('li', { class: 'list-item' },
      el('div', { class: 'item-main' }, open,
        e.tags.length ? el('div', { class: 'chips mt-s' }, e.tags.map((t) => chip(t))) : null),
      e.photoIds.length ? thumbStrip(e.photoIds, { max: 3 }) : null);
  })));
}

async function load() {
  replace(listEl, loadingState());
  try {
    state.entries = await listRecords('diary');
    renderTags();
    render();
  } catch (err) {
    renderLoadError(listEl, err, load);
  }
}

function openReader(entry) {
  const photos = el('div', { class: 'photo-grid' });
  entry.photoIds.forEach((id, i) => {
    const cell = el('div', { class: 'photo-thumb' });
    photos.append(cell);
    defaultSource.url(id, { thumb: true }).then((url) => {
      if (!url) {
        cell.append(el('div', { class: 'photo-missing' }, 'Fotoğraf bu cihazda yok'));
        return;
      }
      const img = el('img', { src: url, alt: '' });
      img.addEventListener('load', () => URL.revokeObjectURL(url), { once: true });
      const b = el('button', { type: 'button', class: 'open-button', 'aria-label': `Fotoğrafı büyüt (${i + 1}/${entry.photoIds.length})` }, img);
      b.addEventListener('click', () => openViewer({ ids: entry.photoIds, index: i }));
      cell.append(b);
    });
  });
  const content = el('article', { class: 'reader' },
    el('p', { class: 'muted' }, formatDate(entry.date, { weekday: true })),
    entry.tags.length ? el('div', { class: 'chips' }, entry.tags.map((t) => chip(t))) : null,
    entry.photoIds.length ? photos : null,
    el('div', { class: 'prose reader-body' }, entry.body || 'Bu yazıda metin yok.'));
  openDialog({
    title: entry.title,
    content,
    size: 'lg',
    actions: [
      {
        label: 'Sil',
        kind: 'danger',
        icon: 'trash',
        className: 'mr-auto',
        onClick: async (d) => {
          try {
            await deleteRecord('diary', entry.id);
            await d.close(true);
            toast('Yazı silindi.', { actionLabel: 'Geri al', onAction: async () => { await restoreRecord('diary', entry.id); load(); } });
            load();
          } catch (err) {
            toastError('diary.delete', err);
          }
        }
      },
      {
        label: 'Düzenle',
        kind: 'primary',
        icon: 'edit',
        onClick: async (d) => {
          await d.close(true);
          openEditor(entry);
        }
      }
    ]
  });
}

async function openEditor(entry, { restoredDraft } = {}) {
  const key = draftKey(entry && entry.id);
  const draft = restoredDraft || (await db.getMeta(key));
  const base = draft || (entry
    ? { title: entry.title, date: entry.date, body: entry.body, tags: entry.tags, photoIds: entry.photoIds, addedPhotoIds: [] }
    : { title: '', date: todayISO(), body: '', tags: [], photoIds: [], addedPhotoIds: [] });

  const status = saveStatus();
  const photos = createPhotoField({ label: 'Fotoğraflar', max: 20, initial: base.photoIds || [], initialAdded: base.addedPhotoIds || [], onChange: () => scheduleDraft() });
  const form = el('form', { class: 'form-stack', novalidate: true },
    el('div', { class: 'form-grid' },
      field({ label: 'Başlık', name: 'title', value: base.title, required: true, maxlength: 200 }),
      field({ label: 'Tarih', name: 'date', type: 'date', value: base.date, required: true })),
    field({ label: 'Metin', name: 'body', type: 'textarea', value: base.body, rows: 12, maxlength: 100000 }),
    field({ label: 'Etiketler', name: 'tags', value: tagsToInput(base.tags), hint: 'Virgülle ayır, en çok 20 etiket.' }),
    photos.node,
    status.node);
  form.addEventListener('submit', (e) => e.preventDefault());

  const collect = () => ({
    title: form.elements.title.value,
    date: form.elements.date.value,
    body: form.elements.body.value,
    tags: parseTags(form.elements.tags.value),
    photoIds: photos.getIds(),
    addedPhotoIds: photos.addedIds(),
    savedAt: new Date().toISOString()
  });

  let hasDraft = Boolean(draft);
  const drafter = createAutosave({
    delay: 800,
    async save(data) {
      await db.setMeta(key, data);
      hasDraft = true;
    },
    onState(s, info) {
      if (s === 'saved') status.node.textContent = 'Taslak kaydedildi; kaydetmeden çıkarsan sonra kaldığın yerden devam edersin.';
      else if (s === 'error') status.set('error', { err: info });
      else if (s === 'dirty') status.set('dirty');
    }
  });
  const scheduleDraft = () => drafter.schedule(collect());
  form.addEventListener('input', scheduleDraft);
  form.addEventListener('change', scheduleDraft);

  let finished = false;

  async function save(dlg) {
    clearFieldErrors(form);
    status.set('saving');
    try {
      drafter.cancel();
      const data = collect();
      const payload = { title: data.title, date: data.date, body: data.body, tags: data.tags, photoIds: data.photoIds };
      const saved = entry ? await updateRecord('diary', entry.id, payload) : await createRecord('diary', payload);
      await photos.commit(`diary:${saved.id}`);
      await db.removeMeta(key);
      finished = true;
      await dlg.close(true);
      toast(entry ? 'Yazı güncellendi.' : 'Yazı kaydedildi.', { kind: 'success' });
      load();
    } catch (err) {
      status.set('error', { err, retry: () => save(dlg) });
      if (err.fields) {
        const unmatched = showFieldErrors(form, err.fields);
        if (unmatched.length) toast(unmatched.join(' '), { kind: 'error' });
      } else toastError('diary.save', err, () => save(dlg));
    }
  }

  async function discard(dlg) {
    const ok = await confirmDialog({ title: 'Değişikliklerden vazgeç', message: 'Kaydedilmemiş değişiklikler ve taslak silinecek.', confirmText: 'Vazgeç ve sil', danger: true });
    if (!ok) return;
    drafter.cancel();
    await photos.discard();
    await db.removeMeta(key).catch(() => {});
    finished = true;
    await dlg.close(true);
  }

  const dlg = openDialog({
    title: entry ? 'Yazıyı düzenle' : 'Yeni günlük yazısı',
    content: form,
    size: 'lg',
    onClose: async () => {
      if (finished) return;
      // Kapatma düğmesi/Esc: taslak saklanır, fotoğraflar taslakta kalır.
      try {
        await drafter.flush();
      } catch (err) {
        toastError('diary.draft', err);
      }
      photos.release();
      if (hasDraft) toast('Taslak saklandı. Günlüğü yeniden açtığında kaldığın yerden devam edersin.');
    },
    actions: [
      { label: 'Vazgeç', onClick: (d) => discard(d) },
      { label: 'Kaydet', kind: 'primary', icon: 'check', onClick: (d) => save(d) }
    ]
  });
  if (draft) {
    status.node.textContent = 'Kaydedilmemiş taslak geri yüklendi.';
    toast('Kaydedilmemiş taslak geri yüklendi.');
  }
  return dlg;
}

async function restoreDrafts() {
  const drafts = await db.getMetaByPrefix('draft:diary:');
  if (!drafts.length) return false;
  const d = drafts.sort((a, b) => String(b.value.savedAt).localeCompare(String(a.value.savedAt)))[0];
  const id = d.key.slice('draft:diary:'.length);
  if (id === 'new') {
    await openEditor(null, { restoredDraft: d.value });
    return true;
  }
  const entry = await getRecord('diary', id);
  if (!entry || entry.deleted) {
    await db.removeMeta(d.key);
    return false;
  }
  await openEditor(entry, { restoredDraft: d.value });
  return true;
}

async function setup() {
  const search = el('input', { type: 'search', class: 'input', id: 'diary-search', placeholder: 'Yazılarda ara', autocomplete: 'off' });
  const from = el('input', { type: 'date', class: 'input', id: 'diary-from' });
  const to = el('input', { type: 'date', class: 'input', id: 'diary-to' });
  search.addEventListener('input', debounce(() => {
    state.query = search.value;
    render();
  }, 150));
  from.addEventListener('change', () => {
    state.from = from.value;
    render();
  });
  to.addEventListener('change', () => {
    state.to = to.value;
    render();
  });
  tagSelect.addEventListener('change', () => {
    state.tag = tagSelect.value;
    render();
  });
  replace(main,
    el('div', { class: 'page-toolbar' },
      el('div', { class: 'field search' }, el('label', { class: 'field-label', for: 'diary-search' }, 'Ara'), search),
      el('div', { class: 'field' }, el('label', { class: 'field-label', for: 'diary-from' }, 'Başlangıç'), from),
      el('div', { class: 'field' }, el('label', { class: 'field-label', for: 'diary-to' }, 'Bitiş'), to),
      el('div', { class: 'field' }, el('label', { class: 'field-label', for: 'diary-tag' }, 'Etiket'), tagSelect),
      button('Yeni yazı', () => openEditor(null), { kind: 'primary', iconName: 'plus' })),
    listEl);
  await load();
  const restored = await restoreDrafts().catch(() => false);
  if (!restored && takeHash('new')) openEditor(null);
}

const ready = await initApp({ page: 'diary', title: 'Günlük' });
if (ready) await setup();
