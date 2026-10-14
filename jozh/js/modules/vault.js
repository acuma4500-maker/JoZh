// Gizli Kasa sayfası (menüsüz). Anahtar yalnızca giriş ekranından 30 sn içinde, aynı sekmede devralınır.
// Kilitlenme: Kilitle düğmesi, 5 dk işlem yapılmaması, 1 dk'dan uzun arka planda kalma, sayfadan ayrılma, yenileme.
import { initApp } from '../app.js';
import * as vault from '../storage/vault-storage.js';
import { el, replace, field, openDialog, toast, toastError, emptyState, loadingState, debounce, chip, button, confirmDialog, showFieldErrors, clearFieldErrors } from '../ui.js';
import { icon } from '../utils/icons.js';
import { VAULT_TYPES } from '../utils/labels.js';
import { parseTags, tagsToInput } from '../utils/tags.js';
import { matchesSearch, truncate } from '../utils/formatters.js';
import { formatDate, todayISO } from '../utils/dates.js';
import { createPhotoField, thumbStrip } from '../components/photos.js';
import { replaceWith, pageUrl } from '../router.js';

const IDLE_MS = 5 * 60 * 1000;
const BACKGROUND_MS = 60 * 1000;

const main = document.getElementById('main');
let key = null;
let source = null;
let items = [];
const state = { query: '', type: '', order: 'desc' };
const listEl = el('div', { class: 'vault-list', 'aria-live': 'polite' });
let idleTimer = null;
let hiddenAt = 0;
let locked = false;

function lockVault(reason) {
  if (locked) return;
  locked = true;
  key = null;
  items = [];
  if (source) source.revokeAll();
  source = null;
  clearTimeout(idleTimer);
  for (const d of document.querySelectorAll('dialog')) {
    d.close();
    d.remove();
  }
  replace(main);
  if (reason !== 'pagehide') replaceWith('vaultLogin');
}

function resetIdle() {
  clearTimeout(idleTimer);
  idleTimer = setTimeout(() => {
    lockVault('idle');
  }, IDLE_MS);
}

function startGuards() {
  for (const type of ['pointerdown', 'keydown', 'scroll', 'input']) {
    window.addEventListener(type, resetIdle, { passive: true, capture: true });
  }
  resetIdle();
  document.addEventListener('visibilitychange', () => {
    if (document.visibilityState === 'hidden') hiddenAt = Date.now();
    else if (hiddenAt && Date.now() - hiddenAt > BACKGROUND_MS) lockVault('background');
  });
  window.addEventListener('pagehide', () => lockVault('pagehide'));
}

function sorted() {
  return items
    .filter((i) => (!state.type || i.type === state.type) && matchesSearch(state.query, i.title, i.body, i.tags, VAULT_TYPES[i.type]))
    .sort((a, b) => {
      const cmp = (a.date || a.createdAt.slice(0, 10)).localeCompare(b.date || b.createdAt.slice(0, 10)) || a.createdAt.localeCompare(b.createdAt);
      return state.order === 'desc' ? -cmp : cmp;
    });
}

function render() {
  if (!items.length) {
    replace(listEl, emptyState('Kasada henüz içerik yok.', 'Yeni içerik', () => openEditor(null), 'shield'));
    return;
  }
  const visible = sorted();
  if (!visible.length) {
    replace(listEl, emptyState('Süzgece uyan içerik yok.', null, null, 'search'));
    return;
  }
  replace(listEl, el('ul', { class: 'list' }, visible.map((item) => {
    if (item.corrupt) {
      return el('li', { class: 'list-item' },
        el('div', { class: 'item-main' }, el('p', { class: 'item-title text-red' }, 'Bozuk içerik'), el('p', { class: 'muted small' }, 'Bu kayıt çözülemedi; yeri değiştirilmiş ya da bozulmuş olabilir.')),
        button('Sil', () => removeItem(item), { kind: 'danger', className: 'btn-small' }));
    }
    const open = el('button', { type: 'button', class: 'open-button' },
      el('span', { class: 'item-title' }, item.title),
      el('span', { class: 'item-meta' }, el('span', null, VAULT_TYPES[item.type]), item.date ? el('span', null, formatDate(item.date)) : null, item.photoIds.length ? el('span', null, `${item.photoIds.length} fotoğraf`) : null),
      item.body ? el('span', { class: 'item-excerpt' }, truncate(item.body, 220)) : null);
    open.addEventListener('click', () => openEditor(item));
    return el('li', { class: 'list-item' },
      el('div', { class: 'item-main' }, open, item.tags.length ? el('div', { class: 'chips mt-s' }, item.tags.map((t) => chip(t))) : null),
      item.photoIds.length ? thumbStrip(item.photoIds, { source, max: 3 }) : null);
  })));
}

async function load() {
  replace(listEl, loadingState('Kasa açılıyor…'));
  try {
    items = await vault.listItems(key);
    render();
    if (!items.some((i) => i.corrupt)) vault.cleanupVaultImages(items).catch(() => {});
  } catch (err) {
    toastError('vault.load', err);
  }
}

async function removeItem(item) {
  const ok = await confirmDialog({ title: 'Kalıcı olarak sil', message: 'Bu içerik ve fotoğrafları kalıcı olarak silinecek. Geri alınamaz.', confirmText: 'Sil', danger: true });
  if (!ok) return false;
  try {
    await vault.deleteItem(item.id, item.photoIds || []);
    toast('İçerik silindi.');
    await load();
    return true;
  } catch (err) {
    toastError('vault.delete', err);
    return false;
  }
}

function openEditor(item) {
  const it = item || { type: 'note', title: '', date: todayISO(), body: '', tags: [], photoIds: [] };
  const photos = createPhotoField({ label: 'Şifreli fotoğraflar', max: 20, initial: it.photoIds, source });
  const form = el('form', { class: 'form-stack', novalidate: true },
    el('div', { class: 'form-grid' },
      field({ label: 'Tür', name: 'type', type: 'select', value: it.type, options: Object.entries(VAULT_TYPES) }),
      field({ label: 'Başlık', name: 'title', value: it.title, required: true, maxlength: 200 }),
      field({ label: 'Tarih', name: 'date', type: 'date', value: it.date })),
    field({ label: 'Metin', name: 'body', type: 'textarea', value: it.body, rows: 10, maxlength: 100000 }),
    field({ label: 'Etiketler', name: 'tags', value: tagsToInput(it.tags), hint: 'Virgülle ayır.' }),
    photos.node);
  form.addEventListener('submit', (e) => e.preventDefault());
  const collect = () => ({
    id: item ? item.id : undefined,
    type: form.elements.type.value,
    title: form.elements.title.value,
    date: form.elements.date.value,
    body: form.elements.body.value,
    tags: parseTags(form.elements.tags.value),
    photoIds: photos.getIds()
  });
  const initial = JSON.stringify(collect());
  const actions = [];
  if (item) {
    actions.push({
      label: 'Sil', kind: 'danger', icon: 'trash', className: 'mr-auto',
      onClick: async (d) => {
        if (await removeItem(item)) await d.close(true);
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
        const saved = await vault.saveItem(key, collect());
        await photos.commit(`vault:${saved.id}`);
        await d.close(true);
        toast('Şifrelenip kaydedildi.', { kind: 'success' });
        load();
      } catch (err) {
        if (err.fields) showFieldErrors(form, err.fields);
        else toastError('vault.save', err);
      }
    }
  });
  openDialog({
    title: item ? 'İçeriği düzenle' : 'Yeni içerik',
    content: form,
    size: 'lg',
    actions,
    isDirty: () => JSON.stringify(collect()) !== initial || photos.isDirty(),
    onClose: () => photos.discard()
  });
}

async function setup() {
  key = await vault.takeSession();
  if (!key) {
    replaceWith('vaultLogin');
    return;
  }
  source = vault.createVaultSource(key);
  startGuards();
  const actions = document.getElementById('vault-actions');
  replace(actions,
    el('a', { class: 'btn btn-ghost btn-small', href: pageUrl('dashboard') }, icon('home'), el('span', null, 'Ana panel')),
    button('Kilitle', () => lockVault('button'), { iconName: 'lock', className: 'btn-small' }));
  const search = el('input', { type: 'search', class: 'input', id: 'vault-search', placeholder: 'Kasada ara', autocomplete: 'off' });
  search.addEventListener('input', debounce(() => {
    state.query = search.value;
    render();
  }, 150));
  const typeSel = el('select', { class: 'input select', id: 'vault-type' }, el('option', { value: '' }, 'Bütün türler'), Object.entries(VAULT_TYPES).map(([v, l]) => el('option', { value: v }, l)));
  typeSel.addEventListener('change', () => {
    state.type = typeSel.value;
    render();
  });
  const orderBtn = button('Yeniden eskiye', () => {
    state.order = state.order === 'desc' ? 'asc' : 'desc';
    orderBtn.querySelector('span').textContent = state.order === 'desc' ? 'Yeniden eskiye' : 'Eskiden yeniye';
    render();
  }, { iconName: 'sort' });
  replace(main,
    el('p', { class: 'notice notice-info' }, icon('shield'), el('span', null, 'Kasa açık. 5 dakika işlem yapmazsan, uygulama 1 dakikadan uzun arka planda kalırsa ya da sayfadan ayrılırsan kendiliğinden kilitlenir.')),
    el('div', { class: 'page-toolbar mt' },
      el('div', { class: 'field search' }, el('label', { class: 'field-label', for: 'vault-search' }, 'Ara'), search),
      el('div', { class: 'field' }, el('label', { class: 'field-label', for: 'vault-type' }, 'Tür'), typeSel),
      orderBtn,
      button('Yeni içerik', () => openEditor(null), { kind: 'primary', iconName: 'plus' })),
    listEl);
  await load();
}

const ready = await initApp({ page: 'vault', title: 'Gizli Kasa', nav: false, sync: false });
if (ready) await setup();
