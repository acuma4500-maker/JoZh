// Toast, modal, onay penceresi, boş durum ve iskelet bileşenleri.
import { h, clear, add } from './helpers.js';
import { icons } from './icons.js';

let toastRoot;
export function toast(message, { type = 'info', duration = 3200, action } = {}) {
  toastRoot ||= document.getElementById('toasts');
  if (!toastRoot) return;
  const el = h('div', { class: `toast toast--${type}`, role: type === 'error' ? 'alert' : 'status' },
    h('span', { class: 'toast__text' }, message),
    action ? h('button', { class: 'toast__action', type: 'button', onclick: () => { action.onClick(); dismiss(); } }, action.label) : null);
  const dismiss = () => { el.classList.add('toast--out'); setTimeout(() => el.remove(), 250); };
  add(toastRoot, el);
  while (toastRoot.children.length > 3) toastRoot.firstChild.remove();
  if (duration) setTimeout(dismiss, duration);
  return dismiss;
}

/** Erişilebilir modal. content: Node. Döner: { close, el, body } */
export function openModal({ title, content, onClose, wide = false, sheet = true } = {}) {
  const root = document.getElementById('modals');
  const prevFocus = document.activeElement;
  const body = h('div', { class: 'modal__body' }, content);
  const titleId = `m-${Math.random().toString(36).slice(2)}`;
  const dialog = h('div', { class: `modal${wide ? ' modal--wide' : ''}${sheet ? ' modal--sheet' : ''}`, role: 'dialog', 'aria-modal': 'true', 'aria-labelledby': titleId },
    h('div', { class: 'modal__head' },
      h('h2', { class: 'modal__title', id: titleId }, title || ''),
      h('button', { class: 'icon-btn', type: 'button', 'aria-label': 'Kapat', svg: icons.close, onclick: () => close() })),
    body);
  const backdrop = h('div', { class: 'modal-backdrop', onclick: (e) => { if (e.target === backdrop) close(); } }, dialog);
  const onKey = (e) => {
    if (e.key === 'Escape') { e.stopPropagation(); close(); }
    if (e.key === 'Tab') trapFocus(e, dialog);
  };
  let closed = false;
  function close(result) {
    if (closed) return; closed = true;
    document.removeEventListener('keydown', onKey, true);
    backdrop.classList.add('modal-backdrop--out');
    setTimeout(() => backdrop.remove(), 200);
    if (!root.querySelector('.modal-backdrop:not(.modal-backdrop--out)')) document.body.classList.remove('no-scroll');
    try { prevFocus?.focus?.({ preventScroll: true }); } catch {}
    onClose?.(result);
  }
  document.addEventListener('keydown', onKey, true);
  add(root, backdrop);
  document.body.classList.add('no-scroll');
  requestAnimationFrame(() => {
    const first = dialog.querySelector('[autofocus], input, textarea, select, button:not(.icon-btn)') || dialog.querySelector('button');
    if (!dialog.contains(document.activeElement)) first?.focus({ preventScroll: true });
  });
  return { close, el: dialog, body };
}

function trapFocus(e, container) {
  const items = [...container.querySelectorAll('a[href], button:not([disabled]), input:not([disabled]), textarea:not([disabled]), select:not([disabled]), [tabindex]:not([tabindex="-1"])')];
  if (!items.length) return;
  const first = items[0], last = items[items.length - 1];
  if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
  else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
}

export function confirmDialog({ title = 'Emin misin?', message = '', confirmText = 'Evet', cancelText = 'Vazgeç', danger = false } = {}) {
  return new Promise((resolve) => {
    let result = false;
    const m = openModal({
      title, sheet: false,
      onClose: () => resolve(result),
      content: h('div', { class: 'confirm' },
        message ? h('p', { class: 'confirm__msg' }, message) : null,
        h('div', { class: 'row row--end' },
          h('button', { class: 'btn btn--ghost', type: 'button', onclick: () => m.close() }, cancelText),
          h('button', { class: `btn ${danger ? 'btn--danger' : 'btn--primary'}`, type: 'button', autofocus: true, onclick: () => { result = true; m.close(); } }, confirmText)))
    });
  });
}

export function emptyState({ emoji = '💗', title, text, action } = {}) {
  return h('div', { class: 'empty' },
    h('div', { class: 'empty__emoji', 'aria-hidden': 'true' }, emoji),
    h('h3', { class: 'empty__title' }, title || ''),
    text ? h('p', { class: 'empty__text' }, text) : null,
    action ? h('button', { class: 'btn btn--primary', type: 'button', onclick: action.onClick }, action.label) : null);
}

export function skeletonList(count = 3, cls = '') {
  return h('div', { class: `skeleton-list ${cls}`, 'aria-busy': 'true', 'aria-label': 'Yükleniyor' },
    Array.from({ length: count }, () => h('div', { class: 'skeleton-card' },
      h('div', { class: 'sk sk--title' }), h('div', { class: 'sk sk--line' }), h('div', { class: 'sk sk--line sk--short' }))));
}

export function errorState(message, retry) {
  return h('div', { class: 'empty empty--error', role: 'alert' },
    h('div', { class: 'empty__emoji', 'aria-hidden': 'true' }, '🥺'),
    h('h3', { class: 'empty__title' }, 'Bir şeyler ters gitti'),
    h('p', { class: 'empty__text' }, message),
    retry ? h('button', { class: 'btn btn--primary', type: 'button', onclick: retry }, 'Tekrar dene') : null);
}

/** Etiketli form alanı. */
export function field(label, input, hint) {
  const id = input.id || `f-${Math.random().toString(36).slice(2)}`;
  input.id = id;
  return h('div', { class: 'field' },
    h('label', { class: 'field__label', for: id }, label), input,
    hint ? h('small', { class: 'field__hint' }, hint) : null);
}

/** Karakter sayaçlı textarea/input. */
export function counted(input, max) {
  const counter = h('small', { class: 'counter', 'aria-live': 'polite' }, `0/${max}`);
  const upd = () => { counter.textContent = `${input.value.length}/${max}`; counter.classList.toggle('counter--warn', input.value.length > max * 0.9); };
  input.maxLength = max;
  input.addEventListener('input', upd);
  queueMicrotask(upd);
  return h('div', { class: 'counted' }, input, counter);
}

export const EMOJI_SET = ['❤️', '💕', '💖', '💘', '💞', '💋', '🥰', '😍', '😘', '😊', '😂', '🥹', '😭', '😴', '🤗', '😇', '😎', '🤭', '🙈', '🫶', '👏', '🙌', '🤞', '✨', '🌙', '⭐', '☀️', '🌈', '🌸', '🌷', '🌹', '🌻', '🍀', '🔥', '🎉', '🎁', '🎂', '🍰', '🍕', '🍔', '🍿', '☕', '🍷', '🍓', '🍫', '🏖️', '🏔️', '✈️', '🚗', '🏠', '🎬', '🎮', '🎵', '📚', '💍', '🧸', '🐱', '🐶', '🦋', '🌊'];

/** Basit emoji seçici. */
export function emojiPicker(onPick, set = EMOJI_SET) {
  return h('div', { class: 'emoji-grid', role: 'listbox', 'aria-label': 'Emoji seç' },
    set.map((e) => h('button', { class: 'emoji-grid__item', type: 'button', role: 'option', 'aria-label': e, onclick: () => onPick(e) }, e)));
}

export function setLoading(btn, loading, text) {
  if (!btn) return;
  if (loading) { btn.dataset.label = btn.textContent; btn.disabled = true; btn.classList.add('is-loading'); if (text) btn.textContent = text; }
  else { btn.disabled = false; btn.classList.remove('is-loading'); if (btn.dataset.label) btn.textContent = btn.dataset.label; }
}

/** Firebase hata kodlarını anlaşılır Türkçe mesaja çevirir. */
export function errorMessage(err) {
  const code = err?.code || '';
  const map = {
    'permission-denied': 'Bu işlem için yetkin yok.',
    'PERMISSION_DENIED': 'Bu işlem için yetkin yok.',
    'unavailable': 'Sunucuya ulaşılamıyor. İnternet bağlantını kontrol et.',
    'deadline-exceeded': 'İşlem zaman aşımına uğradı. Tekrar dene.',
    'failed-precondition': 'Veritabanı hazır değil (eksik dizin olabilir).',
    'resource-exhausted': 'Firebase kotası doldu. Biraz sonra tekrar dene.',
    'not-found': 'Kayıt bulunamadı; silinmiş olabilir.',
    'auth/invalid-credential': 'E-posta veya parola hatalı.',
    'auth/wrong-password': 'E-posta veya parola hatalı.',
    'auth/user-not-found': 'E-posta veya parola hatalı.',
    'auth/invalid-email': 'Geçerli bir e-posta adresi gir.',
    'auth/too-many-requests': 'Çok fazla deneme yapıldı. Lütfen biraz bekle.',
    'auth/network-request-failed': 'İnternet bağlantısı yok gibi görünüyor.',
    'auth/user-disabled': 'Bu hesap devre dışı bırakılmış.',
  };
  if (map[code]) return map[code];
  if (/permission/i.test(String(err?.message))) return map['permission-denied'];
  return err?.message && !/firebase/i.test(err.message) ? err.message : 'Beklenmeyen bir hata oluştu. Tekrar dene.';
}

export { clear };
