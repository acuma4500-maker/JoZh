// Fotoğraf alanı, büyük görüntüleyici ve avatar.
// Alan işlem mantığıyla çalışır: seçilen fotoğraf hemen kaydedilir; commit() kayıt kaydedilince
// kaldırılan eski fotoğrafları siler ve sahibini günceller; discard() yeni eklenenleri siler.
import { el, clear, openDialog, toast, friendlyError, iconButton } from '../ui.js';
import { icon } from '../utils/icons.js';
import { defaultSource, ACCEPT_ATTR } from '../storage/image-storage.js';
import { logError } from '../utils/logger.js';

const PENDING_OWNER = 'pending';

// options: { label, max, initial: [ids], initialAdded: [ids], source, onChange, canDelete = true }
export function createPhotoField({ label = 'Fotoğraflar', max = 1, initial = [], initialAdded = [], source = defaultSource, onChange } = {}) {
  let ids = [...initial];
  const original = new Set(initial.filter((id) => !initialAdded.includes(id)));
  const added = new Set(initialAdded);
  const removed = new Set();
  const urls = [];
  let busy = false;

  const inputId = `photo-input-${Math.random().toString(36).slice(2, 8)}`;
  const input = el('input', { type: 'file', id: inputId, accept: ACCEPT_ATTR, class: 'visually-hidden', multiple: max > 1, tabindex: '-1', 'aria-hidden': 'true' });
  const grid = el('div', { class: 'photo-grid' });
  const status = el('p', { class: 'photo-field-status', 'aria-live': 'polite' });
  const node = el('div', { class: 'field photo-field' },
    el('span', { class: 'field-label' }, label, max > 1 ? ` (en çok ${max})` : ''),
    grid, status, input);

  function revokeAll() {
    while (urls.length) URL.revokeObjectURL(urls.pop());
  }

  async function render() {
    revokeAll();
    clear(grid);
    for (let i = 0; i < ids.length; i += 1) {
      const id = ids[i];
      const cell = el('div', { class: 'photo-thumb' });
      grid.append(cell);
      let url = null;
      try {
        url = await source.url(id, { thumb: true });
      } catch (err) {
        logError('photos.url', err);
      }
      if (url) {
        urls.push(url);
        const open = el('button', { type: 'button', class: 'open-button', 'aria-label': `Fotoğrafı büyüt (${i + 1}/${ids.length})` }, el('img', { src: url, alt: '' }));
        open.addEventListener('click', () => openViewer({ ids, index: i, source }));
        cell.append(open);
      } else {
        cell.append(el('div', { class: 'photo-missing' }, 'Fotoğraf bu cihazda yok'));
      }
      cell.append(iconButton('close', 'Fotoğrafı kaldır', () => removeAt(i), { className: 'btn-icon photo-remove' }));
    }
    if (ids.length < max) {
      const add = el('button', { type: 'button', class: 'photo-add', disabled: busy }, icon('image', { size: 22 }), el('span', null, busy ? 'İşleniyor…' : (max === 1 && ids.length === 0 ? 'Fotoğraf ekle' : 'Ekle')));
      add.addEventListener('click', () => input.click());
      grid.append(add);
    } else if (max === 1) {
      const change = el('button', { type: 'button', class: 'photo-add', disabled: busy }, icon('image', { size: 22 }), el('span', null, 'Değiştir'));
      change.addEventListener('click', () => input.click());
      grid.append(change);
    }
    status.textContent = max > 1 ? `${ids.length} / ${max} fotoğraf` : '';
  }

  async function removeAt(index) {
    const [id] = ids.splice(index, 1);
    if (added.has(id)) {
      added.delete(id);
      await source.remove([id]).catch((err) => logError('photos.remove', err));
    } else {
      removed.add(id);
    }
    await render();
    if (onChange) onChange(ids.slice());
  }

  input.addEventListener('change', async () => {
    const files = [...(input.files || [])];
    input.value = '';
    if (!files.length) return;
    const room = max === 1 ? 1 : max - ids.length;
    if (files.length > room) toast(`En çok ${max} fotoğraf eklenebilir; ilk ${room} tanesi eklenecek.`, { kind: 'warning' });
    busy = true;
    status.textContent = 'Fotoğraf işleniyor…';
    await render();
    for (const file of files.slice(0, room)) {
      try {
        const rec = await source.save(file, PENDING_OWNER);
        if (max === 1 && ids.length) await removeAt(0);
        ids.push(rec.id);
        added.add(rec.id);
      } catch (err) {
        if (!err.userMessage) logError('photos.save', err);
        toast(err.userMessage || `Fotoğraf eklenemedi: ${friendlyError(err)}`, { kind: 'error' });
      }
    }
    busy = false;
    await render();
    if (onChange) onChange(ids.slice());
  });

  render();

  return {
    node,
    getIds: () => ids.slice(),
    getId: () => ids[0] || null,
    isDirty: () => added.size > 0 || removed.size > 0,
    addedIds: () => [...added],
    // Kayıt kaydedildikten sonra çağrılır.
    async commit(owner) {
      await source.setOwner(ids, owner);
      if (removed.size) await source.remove([...removed]);
      for (const id of ids) original.add(id);
      added.clear();
      removed.clear();
    },
    // Düzenleyici kaydedilmeden kapanınca çağrılır.
    async discard() {
      if (added.size) await source.remove([...added]).catch((err) => logError('photos.discard', err));
      added.clear();
      removed.clear();
      revokeAll();
    },
    // Taslak için: eklenenleri silmeden bırakır (taslak onları hatırlar).
    release() {
      revokeAll();
    }
  };
}

// Büyük görüntüleyici: önceki/sonraki, ok tuşları, sayaç, izinliyse sil.
export function openViewer({ ids, index = 0, source = defaultSource, onDelete, captions }) {
  let i = index;
  let currentUrl = null;
  const stage = el('div', { class: 'viewer-stage' });
  const counter = el('span', { class: 'viewer-counter', 'aria-live': 'polite' });
  const caption = el('p', { class: 'muted small viewer-caption' });
  const prev = iconButton('chevronLeft', 'Önceki fotoğraf', () => show(i - 1));
  const next = iconButton('chevronRight', 'Sonraki fotoğraf', () => show(i + 1));
  const bar = el('div', { class: 'viewer-bar' }, prev, counter, next);
  if (onDelete) {
    bar.append(iconButton('trash', 'Fotoğrafı sil', async () => {
      const deleted = await onDelete(ids[i]);
      if (deleted) {
        ids = ids.filter((_, k) => k !== i);
        if (!ids.length) dlg.close(true);
        else show(Math.min(i, ids.length - 1));
      }
    }));
  }
  const content = el('div', { class: 'viewer' }, stage, caption, bar);

  async function show(k) {
    if (!ids.length) return;
    i = (k + ids.length) % ids.length;
    counter.textContent = `${i + 1} / ${ids.length}`;
    prev.disabled = ids.length < 2;
    next.disabled = ids.length < 2;
    caption.textContent = captions ? captions[ids[i]] || '' : '';
    if (currentUrl) URL.revokeObjectURL(currentUrl);
    currentUrl = null;
    clear(stage);
    try {
      currentUrl = await source.url(ids[i], { thumb: false });
    } catch (err) {
      logError('viewer.url', err);
    }
    if (currentUrl) stage.append(el('img', { src: currentUrl, alt: `Fotoğraf ${i + 1} / ${ids.length}` }));
    else stage.append(el('div', { class: 'photo-missing' }, 'Fotoğraf bu cihazda yok'));
  }

  const onKey = (e) => {
    if (e.key === 'ArrowLeft') show(i - 1);
    if (e.key === 'ArrowRight') show(i + 1);
  };
  document.addEventListener('keydown', onKey);
  const dlg = openDialog({
    title: 'Fotoğraf',
    content,
    size: 'full',
    className: 'viewer-dialog',
    onClose: () => {
      document.removeEventListener('keydown', onKey);
      if (currentUrl) URL.revokeObjectURL(currentUrl);
    }
  });
  show(i);
  return dlg;
}

// Fotoğraflı avatar (yoksa baş harfler)
export function avatar({ photoId, text = '?', size = '', source = defaultSource, label = '' }) {
  const node = el('span', { class: `avatar${size ? ` avatar-${size}` : ''}`, role: label ? 'img' : null, 'aria-label': label || null, 'aria-hidden': label ? null : 'true' }, text);
  if (photoId) {
    source.url(photoId, { thumb: true }).then((url) => {
      if (!url) return;
      const img = el('img', { src: url, alt: '' });
      img.addEventListener('load', () => URL.revokeObjectURL(url), { once: true });
      clear(node).append(img);
    }).catch((err) => logError('avatar', err));
  }
  return node;
}

// Kayıt listelerinde küçük önizleme şeridi
export function thumbStrip(photoIds, { source = defaultSource, max = 4 } = {}) {
  const strip = el('div', { class: 'thumb-strip' });
  for (const id of (photoIds || []).slice(0, max)) {
    const cell = el('span', { class: 'thumb-mini' });
    strip.append(cell);
    source.url(id, { thumb: true }).then((url) => {
      if (!url) {
        cell.title = 'Fotoğraf bu cihazda yok';
        return;
      }
      const img = el('img', { src: url, alt: '' });
      img.addEventListener('load', () => URL.revokeObjectURL(url), { once: true });
      cell.append(img);
    }).catch(() => {});
  }
  if ((photoIds || []).length > max) strip.append(el('span', { class: 'chip' }, `+${photoIds.length - max}`));
  return strip;
}

// Dosya seçici (galeri gibi doğrudan ekleme yapan yerler için)
export function pickFiles({ multiple = true } = {}) {
  return new Promise((resolve) => {
    const input = el('input', { type: 'file', accept: ACCEPT_ATTR, multiple, class: 'visually-hidden' });
    let settled = false;
    input.addEventListener('change', () => {
      settled = true;
      const files = [...(input.files || [])];
      input.remove();
      resolve(files);
    });
    input.addEventListener('cancel', () => {
      if (!settled) {
        input.remove();
        resolve([]);
      }
    });
    document.body.append(input);
    input.click();
  });
}
