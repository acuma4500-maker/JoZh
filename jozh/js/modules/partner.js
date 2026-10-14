// Sevdiğim kadın: 14 bölüm, her biri ayrı "Düzenle" penceresi. Anılar ayrı depoda, galeri fotoğrafları cihazda.
import { initApp, renderLoadError } from '../app.js';
import { getSingleton, saveSingleton, listRecords, createRecord, updateRecord, deleteRecord, restoreRecord } from '../storage/records.js';
import { el, replace, field, openDialog, toast, toastError, loadingState, button, chip, showFieldErrors, clearFieldErrors, debounce, emptyState, iconButton, confirmDialog, uid } from '../ui.js';
import { LIST_SECTIONS, CHECK_SECTIONS, importantDates, togetherDuration } from '../utils/partner-helpers.js';
import { formatDate, calcAge, relativeDayLabel } from '../utils/dates.js';
import { matchesSearch, initials, truncate } from '../utils/formatters.js';
import { parseTags, tagsToInput, collectTags, hasTag } from '../utils/tags.js';
import { shortId } from '../utils/id-generator.js';
import { createPhotoField, avatar, openViewer, pickFiles, thumbStrip } from '../components/photos.js';
import { createListEditor, checkListView, textListView } from '../components/list-editor.js';
import { listByOwner, saveImage, deleteImages, defaultSource } from '../storage/image-storage.js';

const main = document.getElementById('main');
let partner = null;
let memories = [];
const memState = { query: '', tag: '', order: 'desc' };
const sections = {};

function section(id, title, onEdit, editLabel = 'Düzenle') {
  const body = el('div', { class: 'section-body' });
  const node = el('section', { class: 'card partner-section', id: `sec-${id}`, 'aria-labelledby': `sec-${id}-title` },
    el('div', { class: 'card-header' },
      el('h2', { id: `sec-${id}-title` }, title),
      onEdit ? button(editLabel, onEdit, { iconName: 'edit', className: 'btn-small' }) : null),
    body);
  sections[id] = body;
  return node;
}

async function savePartner(changes) {
  partner = await saveSingleton('partner', changes);
  return partner;
}

// --- Düzenleme pencereleri ---

function editDialog({ title, content, collect, onSave, size = 'md' }) {
  const initial = JSON.stringify(collect());
  return openDialog({
    title,
    content,
    size,
    isDirty: () => JSON.stringify(collect()) !== initial,
    actions: [
      { label: 'Vazgeç', onClick: (d) => d.close() },
      {
        label: 'Kaydet',
        kind: 'primary',
        onClick: async (d) => {
          clearFieldErrors(content);
          try {
            await onSave();
            await d.close(true);
            toast('Kaydedildi.', { kind: 'success' });
            renderAll();
          } catch (err) {
            if (err.fields) {
              const unmatched = showFieldErrors(content, err.fields);
              if (unmatched.length) toast(unmatched.join(' '), { kind: 'error' });
            } else toastError('partner.save', err);
          }
        }
      }
    ]
  });
}

function editGeneral() {
  const p = partner || {};
  const photos = createPhotoField({ label: 'Fotoğraf', max: 1, initial: p.photoId ? [p.photoId] : [] });
  const form = el('form', { class: 'form-stack', novalidate: true },
    el('div', { class: 'form-grid' },
      field({ label: 'Ad', name: 'name', value: p.name || '', maxlength: 100 }),
      field({ label: 'Hitap', name: 'nickname', value: p.nickname || '', maxlength: 100, hint: 'Ona nasıl seslendiğin' }),
      field({ label: 'Doğum tarihi', name: 'birthDate', type: 'date', value: p.birthDate || '' }),
      field({ label: 'Birlikte olunan tarih', name: 'togetherSince', type: 'date', value: p.togetherSince || '' })),
    field({ label: 'Kısa tanım', name: 'summary', type: 'textarea', value: p.summary || '', rows: 3, maxlength: 1000 }),
    photos.node);
  form.addEventListener('submit', (e) => e.preventDefault());
  const collect = () => ({
    name: form.elements.name.value, nickname: form.elements.nickname.value, birthDate: form.elements.birthDate.value,
    togetherSince: form.elements.togetherSince.value, summary: form.elements.summary.value, photoId: photos.getId()
  });
  const dlg = editDialog({
    title: 'Genel bilgiler',
    content: form,
    collect,
    onSave: async () => {
      await savePartner(collect());
      await photos.commit('partner:main');
    }
  });
  const origClose = dlg.close;
  dlg.close = async (force) => {
    const closed = await origClose(force);
    if (closed) await photos.discard();
    return closed;
  };
}

function editList(key, title, placeholder, checkable) {
  const editor = createListEditor({ label: title, items: (partner && partner[key]) || [], checkable, placeholder });
  const content = el('div', { class: 'form-stack' }, editor.node);
  editDialog({ title, content, collect: () => editor.getItems(), onSave: () => savePartner({ [key]: editor.getItems() }) });
}

function editDates() {
  const list = el('div', { class: 'edit-list' });
  const addRow = (item, focus) => {
    const id = uid('date');
    const row = el('div', { class: 'date-row', dataset: { id: item.id || shortId() } },
      el('input', { type: 'text', class: 'input date-title', value: item.title || '', placeholder: 'ör. İlk buluşma', 'aria-label': 'Tarihin adı', maxlength: 200 }),
      el('input', { type: 'date', class: 'input date-value', value: item.date || '', 'aria-label': 'Tarih' }),
      el('label', { class: 'check-label', for: id }, el('input', { type: 'checkbox', id, class: 'checkbox date-yearly', checked: item.yearly !== false }), el('span', null, 'Her yıl')),
      iconButton('trash', 'Tarihi sil', () => row.remove()),
      el('p', { class: 'field-error span-row', hidden: true }));
    list.append(row);
    if (focus) row.querySelector('input').focus();
  };
  for (const item of (partner && partner.importantDates) || []) addRow(item);
  const collect = () => [...list.children].map((row) => ({
    id: row.dataset.id,
    title: row.querySelector('.date-title').value.trim(),
    date: row.querySelector('.date-value').value,
    yearly: row.querySelector('.date-yearly').checked
  })).filter((d) => d.title || d.date);
  const content = el('div', { class: 'form-stack' },
    el('p', { class: 'muted small' }, 'Doğum günü ve birliktelik yıl dönümü genel bilgilerden otomatik eklenir. "Her yıl" işaretli tarihler her yıl yeniden hesaplanır.'),
    list,
    el('div', null, button('Tarih ekle', () => addRow({ yearly: true }, true), { iconName: 'plus', className: 'btn-small' })));
  editDialog({
    title: 'Önemli tarihler',
    content,
    collect,
    onSave: async () => {
      const items = collect();
      const errors = {};
      items.forEach((d, i) => {
        const row = list.children[i];
        const errEl = row.querySelector('.field-error');
        let msg = '';
        if (!d.title) msg = 'Tarihin adını yaz.';
        else if (!d.date) msg = 'Tarihi seç.';
        errEl.textContent = msg;
        errEl.hidden = !msg;
        if (msg) errors[i] = msg;
      });
      if (Object.keys(errors).length) {
        const e = new Error('Doğrulama');
        e.type = 'validation';
        e.userMessage = 'Önemli tarihlerde eksik bilgi var; satırların altındaki uyarılara bak.';
        throw e;
      }
      await savePartner({ importantDates: items });
    }
  });
}

function editNotes() {
  const form = el('form', { class: 'form-stack', novalidate: true },
    field({ label: 'Özel notlar', name: 'privateNotes', type: 'textarea', value: (partner && partner.privateNotes) || '', rows: 10, maxlength: 10000 }));
  form.addEventListener('submit', (e) => e.preventDefault());
  editDialog({ title: 'Özel notlar', content: form, collect: () => form.elements.privateNotes.value, onSave: () => savePartner({ privateNotes: form.elements.privateNotes.value }), size: 'lg' });
}

// --- Anılar ---

function openMemoryEditor(memory) {
  const m = memory || { title: '', date: '', description: '', tags: [], photoIds: [] };
  const photos = createPhotoField({ label: 'Fotoğraflar', max: 10, initial: m.photoIds });
  const form = el('form', { class: 'form-stack', novalidate: true },
    el('div', { class: 'form-grid' },
      field({ label: 'Başlık', name: 'title', value: m.title, required: true, maxlength: 200 }),
      field({ label: 'Tarih', name: 'date', type: 'date', value: m.date })),
    field({ label: 'Açıklama', name: 'description', type: 'textarea', value: m.description, rows: 5, maxlength: 5000 }),
    field({ label: 'Etiketler', name: 'tags', value: tagsToInput(m.tags), hint: 'Virgülle ayır.' }),
    photos.node);
  form.addEventListener('submit', (e) => e.preventDefault());
  const collect = () => ({ title: form.elements.title.value, date: form.elements.date.value, description: form.elements.description.value, tags: parseTags(form.elements.tags.value), photoIds: photos.getIds() });
  const initial = JSON.stringify(collect());
  const actions = [];
  if (memory) {
    actions.push({
      label: 'Sil', kind: 'danger', icon: 'trash', className: 'mr-auto',
      onClick: async (d) => {
        try {
          await deleteRecord('memories', memory.id);
          await d.close(true);
          toast('Anı silindi.', { actionLabel: 'Geri al', onAction: async () => { await restoreRecord('memories', memory.id); await reloadMemories(); } });
          await reloadMemories();
        } catch (err) {
          toastError('memories.delete', err);
        }
      }
    });
  }
  actions.push({ label: 'Vazgeç', onClick: (d) => d.close() });
  actions.push({
    label: 'Kaydet',
    kind: 'primary',
    onClick: async (d) => {
      clearFieldErrors(form);
      try {
        const saved = memory ? await updateRecord('memories', memory.id, collect()) : await createRecord('memories', collect());
        await photos.commit(`memories:${saved.id}`);
        await d.close(true);
        toast(memory ? 'Anı güncellendi.' : 'Anı eklendi.', { kind: 'success' });
        await reloadMemories();
      } catch (err) {
        if (err.fields) showFieldErrors(form, err.fields);
        else toastError('memories.save', err);
      }
    }
  });
  openDialog({
    title: memory ? 'Anıyı düzenle' : 'Yeni anı',
    content: form,
    size: 'lg',
    actions,
    isDirty: () => JSON.stringify(collect()) !== initial || photos.isDirty(),
    onClose: () => photos.discard()
  });
}

async function reloadMemories() {
  memories = await listRecords('memories');
  renderMemories();
  await renderGallery();
}

function renderMemories() {
  const body = sections.memories;
  const tags = collectTags(memories);
  const search = el('input', { type: 'search', class: 'input', id: 'mem-search', placeholder: 'Anılarda ara', value: memState.query, autocomplete: 'off' });
  const tagSel = el('select', { class: 'input select', id: 'mem-tag' }, el('option', { value: '' }, 'Bütün etiketler'), tags.map((t) => el('option', { value: t }, t)));
  tagSel.value = tags.includes(memState.tag) ? memState.tag : '';
  const orderBtn = button(memState.order === 'desc' ? 'Yeniden eskiye' : 'Eskiden yeniye', () => {
    memState.order = memState.order === 'desc' ? 'asc' : 'desc';
    renderMemories();
  }, { iconName: 'sort', className: 'btn-small' });
  const listHolder = el('div', { class: 'memory-list' });

  const renderList = () => {
    const visible = memories
      .filter((m) => hasTag(m, memState.tag) && matchesSearch(memState.query, m.title, m.description, m.tags))
      .sort((a, b) => {
        const cmp = (a.date || a.createdAt.slice(0, 10)).localeCompare(b.date || b.createdAt.slice(0, 10));
        return memState.order === 'desc' ? -cmp : cmp;
      });
    if (!memories.length) {
      replace(listHolder, emptyState('Henüz anı yok.', 'Anı ekle', () => openMemoryEditor(null), 'star'));
      return;
    }
    if (!visible.length) {
      replace(listHolder, el('p', { class: 'muted small' }, 'Aramaya uyan anı yok.'));
      return;
    }
    replace(listHolder, el('ol', { class: 'timeline' }, visible.map((m) => {
      const open = el('button', { type: 'button', class: 'open-button' },
        el('span', { class: 'item-title' }, m.title),
        el('span', { class: 'item-meta' }, m.date ? formatDate(m.date) : 'Tarihsiz', m.photoIds.length ? ` · ${m.photoIds.length} fotoğraf` : ''),
        m.description ? el('span', { class: 'item-excerpt' }, truncate(m.description, 200)) : null);
      open.addEventListener('click', () => openMemoryEditor(m));
      return el('li', { class: 'timeline-item' },
        el('span', { class: 'timeline-dot', 'aria-hidden': 'true' }),
        el('div', { class: 'item-main' }, open,
          m.tags.length ? el('div', { class: 'chips mt-s' }, m.tags.map((t) => chip(t))) : null,
          m.photoIds.length ? thumbStrip(m.photoIds, { max: 5 }) : null));
    })));
  };
  search.addEventListener('input', debounce(() => {
    memState.query = search.value;
    renderList();
  }, 150));
  tagSel.addEventListener('change', () => {
    memState.tag = tagSel.value;
    renderList();
  });
  replace(body,
    el('div', { class: 'page-toolbar' },
      el('div', { class: 'field search' }, el('label', { class: 'field-label', for: 'mem-search' }, 'Ara'), search),
      el('div', { class: 'field' }, el('label', { class: 'field-label', for: 'mem-tag' }, 'Etiket'), tagSel),
      orderBtn),
    listHolder);
  renderList();
}

// --- Galeri ---

async function renderGallery() {
  const body = sections.gallery;
  const own = (await listByOwner('gallery')).sort((a, b) => b.createdAt.localeCompare(a.createdAt));
  const ownIds = own.map((r) => r.id);
  const memoryIds = memories.flatMap((m) => m.photoIds);
  const ids = [...ownIds, ...memoryIds.filter((id) => !ownIds.includes(id))];
  const ownSet = new Set(ownIds);
  const grid = el('div', { class: 'photo-grid' });
  ids.forEach((id, i) => {
    const cell = el('div', { class: 'photo-thumb' });
    grid.append(cell);
    defaultSource.url(id, { thumb: true }).then((url) => {
      if (!url) {
        cell.append(el('div', { class: 'photo-missing' }, 'Fotoğraf bu cihazda yok'));
        return;
      }
      const img = el('img', { src: url, alt: ownSet.has(id) ? 'Galeri fotoğrafı' : 'Anı fotoğrafı' });
      img.addEventListener('load', () => URL.revokeObjectURL(url), { once: true });
      const b = el('button', { type: 'button', class: 'open-button', 'aria-label': `Fotoğrafı büyüt (${i + 1}/${ids.length})` }, img);
      b.addEventListener('click', () => openViewer({
        ids: ids.slice(),
        index: i,
        onDelete: async (pid) => {
          if (!ownSet.has(pid)) {
            toast('Bu fotoğraf bir anıya ait; anıyı düzenleyerek kaldırabilirsin.', { kind: 'warning' });
            return false;
          }
          const ok = await confirmDialog({ title: 'Fotoğrafı sil', message: 'Bu fotoğraf galeriden kalıcı olarak silinecek.', confirmText: 'Sil', danger: true });
          if (!ok) return false;
          await deleteImages([pid]);
          renderGallery();
          return true;
        }
      }));
      cell.append(b);
    });
  });
  const addBtn = button('Fotoğraf ekle', async () => {
    const files = await pickFiles({ multiple: true });
    if (!files.length) return;
    addBtn.disabled = true;
    let added = 0;
    for (const f of files) {
      try {
        await saveImage(f, 'gallery');
        added += 1;
      } catch (err) {
        toast(err.userMessage || 'Fotoğraf eklenemedi.', { kind: 'error' });
      }
    }
    addBtn.disabled = false;
    if (added) toast(`${added} fotoğraf eklendi.`, { kind: 'success' });
    renderGallery();
  }, { iconName: 'plus', className: 'btn-small' });
  replace(body,
    el('div', { class: 'row' }, addBtn, el('span', { class: 'muted small' }, `${ids.length} fotoğraf · galeriye eklenenler ve anılardaki fotoğraflar`)),
    ids.length ? grid : el('p', { class: 'muted small mt' }, 'Henüz fotoğraf yok.'));
  grid.classList.add('mt');
}

// --- Bölümlerin görünümü ---

function renderGeneral() {
  const p = partner || {};
  const age = calcAge(p.birthDate);
  const together = togetherDuration(p);
  const rows = [];
  if (p.nickname) rows.push(['Hitap', p.nickname]);
  if (p.birthDate) rows.push(['Doğum tarihi', `${formatDate(p.birthDate)}${age !== null ? ` (${age} yaş)` : ''}`]);
  if (p.togetherSince) rows.push(['Birlikte', `${formatDate(p.togetherSince)}${together ? ` · ${together.text}` : ''}`]);
  replace(sections.general,
    el('div', { class: 'row partner-head' },
      avatar({ photoId: p.photoId, text: initials(p.name, ''), size: 'lg' }),
      el('div', { class: 'grow' },
        el('p', { class: 'partner-name' }, p.name || 'Adını ekle'),
        rows.length ? el('dl', { class: 'kv mt-s' }, rows.flatMap(([k, v]) => [el('dt', null, k), el('dd', null, v)])) : null)),
    p.summary ? el('p', { class: 'prose mt' }, p.summary) : null);
}

function renderDates() {
  const list = importantDates(partner);
  if (!list.length) {
    replace(sections.dates, el('p', { class: 'muted small' }, 'Genel bilgilere doğum günü ya da birlikte olunan tarihi ekle; diğer tarihleri buradan ekleyebilirsin.'));
    return;
  }
  replace(sections.dates, el('ul', { class: 'date-list' }, list.map((d) => el('li', { class: `date-item${d.daysLeft < 0 ? ' is-past' : ''}` },
    el('div', { class: 'grow' },
      el('span', { class: 'item-title' }, d.title),
      el('span', { class: 'item-meta' }, formatDate(d.date, { weekday: true }), d.note ? ` · ${d.note}` : '', d.yearly ? ' · her yıl' : '')),
    chip(relativeDayLabel(d.daysLeft), { kind: d.daysLeft >= 0 && d.daysLeft <= 7 ? 'warm' : '' })))));
}

function renderAll() {
  renderGeneral();
  for (const s of LIST_SECTIONS) replace(sections[s.key], textListView((partner && partner[s.key]) || []));
  renderDates();
  for (const s of CHECK_SECTIONS) {
    replace(sections[s.key], checkListView((partner && partner[s.key]) || [], async (id, done) => {
      try {
        const items = partner[s.key].map((i) => (i.id === id ? { ...i, done } : i));
        await savePartner({ [s.key]: items });
      } catch (err) {
        toastError('partner.check', err);
        throw err;
      }
    }));
  }
  replace(sections.privateNotes, partner && partner.privateNotes ? el('p', { class: 'prose' }, partner.privateNotes) : el('p', { class: 'muted small' }, 'Henüz not yok.'));
}

async function setup() {
  replace(main, loadingState());
  try {
    partner = await getSingleton('partner');
    memories = await listRecords('memories');
  } catch (err) {
    renderLoadError(main, err, setup);
    return;
  }
  const layout = el('div', { class: 'partner-layout' },
    section('general', 'Genel bilgiler', editGeneral),
    ...LIST_SECTIONS.map((s) => section(s.key, s.title, () => editList(s.key, s.title, s.placeholder, false))),
    section('dates', 'Önemli tarihler', editDates),
    section('memories', 'Anılar', () => openMemoryEditor(null), 'Anı ekle'),
    section('gallery', 'Fotoğraf galerisi', null),
    ...CHECK_SECTIONS.map((s) => section(s.key, s.title, () => editList(s.key, s.title, s.placeholder, true))),
    section('privateNotes', 'Özel notlar', editNotes));
  replace(main, layout);
  renderAll();
  renderMemories();
  await renderGallery();
}

const ready = await initApp({ page: 'partner', title: 'Sevdiğim kadın' });
if (ready) await setup();
