// Ortak arayüz yardımcıları: güvenli öğe oluşturma, bildirimler, pencereler, form alanları.
// Kullanıcı metni her zaman textContent ile eklenir.
import { icon } from './utils/icons.js';
import { classifyError, logError } from './utils/logger.js';
import { formatClock } from './utils/dates.js';

let idCounter = 0;
export function uid(prefix = 'f') {
  idCounter += 1;
  return `${prefix}-${idCounter}`;
}

// el('button', {class:'btn', onclick: fn, dataset:{id:1}}, 'Metin', çocukÖğe)
export function el(tag, attrs, ...children) {
  const node = document.createElement(tag);
  if (attrs) {
    for (const [key, value] of Object.entries(attrs)) {
      if (value === undefined || value === null || value === false) continue;
      if (key === 'class') node.className = value;
      else if (key === 'dataset') Object.assign(node.dataset, value);
      else if (key === 'text') node.textContent = value;
      else if (key.startsWith('on') && typeof value === 'function') node.addEventListener(key.slice(2), value);
      else if (key === 'value') node.value = value;
      else if (key === 'checked' || key === 'disabled' || key === 'selected' || key === 'hidden' || key === 'required' || key === 'multiple') {
        node[key] = Boolean(value);
        if (key !== 'checked' && key !== 'selected') node.setAttribute(key, '');
      } else if (value === true) node.setAttribute(key, '');
      else node.setAttribute(key, String(value));
    }
  }
  appendChildren(node, children);
  return node;
}

function appendChildren(node, children) {
  for (const child of children.flat(Infinity)) {
    if (child === null || child === undefined || child === false) continue;
    node.append(child instanceof Node ? child : document.createTextNode(String(child)));
  }
}

export function clear(node) {
  while (node.firstChild) node.removeChild(node.firstChild);
  return node;
}

export function replace(node, ...children) {
  clear(node);
  appendChildren(node, children);
  return node;
}

export function $(selector, root = document) {
  return root.querySelector(selector);
}

export function $$(selector, root = document) {
  return [...root.querySelectorAll(selector)];
}

export function debounce(fn, wait) {
  let t = null;
  return (...args) => {
    clearTimeout(t);
    t = setTimeout(() => fn(...args), wait);
  };
}

export function iconButton(name, label, onClick, { className = 'btn-icon', disabled = false } = {}) {
  return el('button', { type: 'button', class: className, 'aria-label': label, title: label, onclick: onClick, disabled }, icon(name));
}

export function button(text, onClick, { kind = 'secondary', iconName, type = 'button', disabled = false, className = '' } = {}) {
  return el('button', { type, class: `btn btn-${kind}${className ? ` ${className}` : ''}`, onclick: onClick, disabled },
    iconName ? icon(iconName) : null, el('span', null, text));
}

// --- Hata mesajları ---

export function friendlyError(err) {
  if (!err) return 'Bilinmeyen bir sorun oluştu.';
  if (err.userMessage) return err.userMessage;
  switch (classifyError(err)) {
    case 'network': return 'İnternet bağlantısı yok ya da sunucuya ulaşılamadı.';
    case 'permission': return 'Bu işlem için izin yok.';
    case 'validation': return 'Bazı alanlar hatalı. Alanların altındaki uyarılara bak.';
    case 'storage':
      if (err.name === 'QuotaExceededError') return 'Cihazda yer kalmadı. Fotoğrafları temizlemeyi ya da yer açmayı dene.';
      return 'Cihaz depolamasına yazılamadı.';
    default: return 'Beklenmeyen bir sorun oluştu.';
  }
}

// --- Bildirimler ---

function toastRegion() {
  let region = document.getElementById('toast-region');
  if (!region) {
    region = el('div', { id: 'toast-region', class: 'toast-region', 'aria-live': 'polite', role: 'status' });
    document.body.append(region);
  }
  return region;
}

export function toast(message, { kind = 'info', actionLabel, onAction, duration } = {}) {
  const region = toastRegion();
  const item = el('div', { class: `toast toast-${kind}` }, el('span', { class: 'toast-text' }, message));
  let timer = null;
  const close = () => {
    clearTimeout(timer);
    item.remove();
  };
  if (actionLabel && onAction) {
    item.append(el('button', {
      type: 'button',
      class: 'toast-action',
      onclick: () => {
        close();
        onAction();
      }
    }, actionLabel));
  }
  item.append(el('button', { type: 'button', class: 'toast-close', 'aria-label': 'Bildirimi kapat', onclick: close }, icon('close', { size: 16 })));
  region.append(item);
  // En çok 3 bildirim aynı anda görünür; en eskisi kalkar.
  while (region.children.length > 3) region.firstElementChild.remove();
  const ms = duration ?? (actionLabel ? 8000 : 4500);
  if (ms > 0) timer = setTimeout(close, ms);
  return { close };
}

export function toastError(context, err, retry) {
  logError(context, err);
  return toast(friendlyError(err), { kind: 'error', actionLabel: retry ? 'Tekrar dene' : undefined, onAction: retry });
}

// --- Pencereler ---

const openDialogs = [];

export function openDialog({ title, content, actions = [], onClose, isDirty, size = 'md', className = '' }) {
  const titleId = uid('dlg-title');
  const body = el('div', { class: 'dialog-body' }, content);
  const footer = el('div', { class: 'dialog-footer' });
  const dialog = el('dialog', { class: `dialog dialog-${size}${className ? ` ${className}` : ''}`, 'aria-labelledby': titleId },
    el('div', { class: 'dialog-header' },
      el('h2', { id: titleId, class: 'dialog-title' }, title),
      iconButton('close', 'Pencereyi kapat', () => api.close())),
    body,
    footer);

  let closed = false;
  const api = {
    dialog,
    body,
    footer,
    setActions(list) {
      clear(footer);
      for (const a of list) {
        footer.append(button(a.label, () => a.onClick(api), { kind: a.kind || 'secondary', iconName: a.icon, className: a.className || '' }));
      }
    },
    async close(force = false) {
      if (closed) return true;
      if (!force && isDirty && isDirty()) {
        const ok = await confirmDialog({ title: 'Kaydedilmemiş değişiklikler', message: 'Yaptığın değişiklikler kaydedilmedi. Yine de kapatılsın mı?', confirmText: 'Kaydetmeden kapat', danger: true });
        if (!ok) return false;
      }
      closed = true;
      dialog.close();
      dialog.remove();
      const idx = openDialogs.indexOf(api);
      if (idx >= 0) openDialogs.splice(idx, 1);
      if (onClose) await onClose();
      return true;
    },
    setTitle(text) {
      dialog.querySelector('.dialog-title').textContent = text;
    }
  };
  api.setActions(actions);
  dialog.addEventListener('cancel', (e) => {
    e.preventDefault();
    api.close();
  });
  document.body.append(dialog);
  dialog.showModal();
  openDialogs.push(api);
  const focusable = body.querySelector('input:not([type=hidden]), textarea, select');
  if (focusable && window.matchMedia('(hover: hover)').matches) focusable.focus();
  return api;
}

export function confirmDialog({ title, message, confirmText = 'Onayla', cancelText = 'Vazgeç', danger = false, requireText }) {
  return new Promise((resolve) => {
    let result = false;
    const content = el('div', { class: 'confirm-content' });
    for (const para of String(message || '').split('\n')) content.append(el('p', null, para));
    let input = null;
    if (requireText) {
      const id = uid('confirm');
      input = el('input', { id, type: 'text', class: 'input', autocomplete: 'off', autocapitalize: 'characters', spellcheck: 'false' });
      content.append(el('label', { for: id, class: 'field-label' }, `Onaylamak için "${requireText}" yaz`), input);
    }
    const dlg = openDialog({
      title,
      content,
      size: 'sm',
      onClose: () => resolve(result),
      actions: [
        { label: cancelText, onClick: (d) => d.close(true) },
        {
          label: confirmText,
          kind: danger ? 'danger' : 'primary',
          onClick: (d) => {
            if (requireText && input.value.trim().toLocaleUpperCase('tr-TR') !== requireText) {
              input.setAttribute('aria-invalid', 'true');
              input.focus();
              return;
            }
            result = true;
            d.close(true);
          }
        }
      ]
    });
    if (input) input.focus();
    else dlg.footer.lastElementChild.focus();
  });
}

// --- Form alanları ---

// field({label, name, type, value, options, hint, required, rows, maxlength, inputmode, placeholder, autocomplete})
export function field(opts) {
  const id = opts.id || uid(opts.name || 'f');
  const errorId = `${id}-error`;
  const hintId = opts.hint ? `${id}-hint` : null;
  const describedBy = [hintId, errorId].filter(Boolean).join(' ');
  let control;
  const common = {
    id,
    name: opts.name,
    required: opts.required,
    'aria-describedby': describedBy,
    placeholder: opts.placeholder,
    disabled: opts.disabled
  };
  if (opts.type === 'textarea') {
    control = el('textarea', { ...common, class: 'input textarea', rows: opts.rows || 4, maxlength: opts.maxlength });
    control.value = opts.value ?? '';
  } else if (opts.type === 'select') {
    control = el('select', { ...common, class: 'input select' });
    for (const opt of opts.options || []) {
      const [value, label] = Array.isArray(opt) ? opt : [opt, opt];
      control.append(el('option', { value }, label));
    }
    control.value = opts.value ?? '';
  } else if (opts.type === 'checkbox') {
    control = el('input', { ...common, type: 'checkbox', class: 'checkbox', checked: Boolean(opts.value) });
    return el('div', { class: `field field-check${opts.className ? ` ${opts.className}` : ''}` },
      el('label', { class: 'check-label', for: id }, control, el('span', null, opts.label)),
      hintId ? el('p', { id: hintId, class: 'field-hint' }, opts.hint) : null,
      el('p', { id: errorId, class: 'field-error', hidden: true }));
  } else {
    control = el('input', {
      ...common,
      type: opts.type || 'text',
      class: 'input',
      maxlength: opts.maxlength,
      inputmode: opts.inputmode,
      autocomplete: opts.autocomplete || 'off',
      min: opts.min,
      max: opts.max,
      step: opts.step,
      list: opts.list
    });
    control.value = opts.value ?? '';
  }
  return el('div', { class: `field${opts.className ? ` ${opts.className}` : ''}` },
    el('label', { class: 'field-label', for: id }, opts.label, opts.required ? el('span', { class: 'req', 'aria-hidden': 'true' }, ' *') : null),
    control,
    hintId ? el('p', { id: hintId, class: 'field-hint' }, opts.hint) : null,
    el('p', { id: errorId, class: 'field-error', hidden: true }));
}

export function readForm(form) {
  const data = {};
  for (const elx of form.elements) {
    if (!elx.name || elx.disabled) continue;
    if (elx.type === 'checkbox') data[elx.name] = elx.checked;
    else if (elx.type === 'radio') {
      if (elx.checked) data[elx.name] = elx.value;
    } else data[elx.name] = elx.value;
  }
  return data;
}

export function clearFieldErrors(root) {
  for (const p of root.querySelectorAll('.field-error')) {
    p.textContent = '';
    p.hidden = true;
  }
  for (const c of root.querySelectorAll('[aria-invalid="true"]')) c.removeAttribute('aria-invalid');
}

// fields: { alan: mesaj }; iç içe alanlar ("trip.city") en yakın eşleşmeye yazılır.
export function showFieldErrors(root, fields) {
  clearFieldErrors(root);
  let first = null;
  const unmatched = [];
  for (const [path, message] of Object.entries(fields || {})) {
    const candidates = [path, path.split('.')[0], path.replace(/\.\d+\./, '.')];
    let control = null;
    for (const name of candidates) {
      control = root.querySelector(`[name="${CSS.escape(name)}"]`);
      if (control) break;
    }
    const errEl = control ? document.getElementById(`${control.id}-error`) : null;
    if (errEl) {
      errEl.textContent = message;
      errEl.hidden = false;
      control.setAttribute('aria-invalid', 'true');
      if (!first) first = control;
    } else {
      unmatched.push(message);
    }
  }
  if (first) first.focus();
  return unmatched;
}

// Kayıt durumu satırı
export function saveStatus() {
  const node = el('p', { class: 'save-status', 'aria-live': 'polite' });
  return {
    node,
    set(state, info) {
      node.dataset.state = state;
      clear(node);
      if (state === 'dirty') node.textContent = 'Kaydedilmemiş değişiklikler var';
      else if (state === 'saving') node.textContent = 'Kaydediliyor…';
      else if (state === 'saved') node.textContent = `Cihaza kaydedildi (${formatClock(new Date().toISOString())})`;
      else if (state === 'error') {
        node.append(el('span', null, `Kaydedilemedi: ${friendlyError(info && info.err)} `));
        if (info && info.retry) node.append(el('button', { type: 'button', class: 'link-button', onclick: info.retry }, 'Tekrar dene'));
      } else node.textContent = '';
    }
  };
}

// --- Durum blokları ---

export function emptyState(text, actionText, onAction, iconName = 'info') {
  return el('div', { class: 'state state-empty' },
    icon(iconName, { size: 28 }),
    el('p', null, text),
    actionText ? button(actionText, onAction, { kind: 'primary', iconName: 'plus' }) : null);
}

export function errorState(text, onRetry) {
  return el('div', { class: 'state state-error', role: 'alert' },
    icon('alert', { size: 28 }),
    el('p', null, text),
    onRetry ? button('Tekrar dene', onRetry, { iconName: 'refresh' }) : null);
}

export function loadingState(text = 'Yükleniyor…') {
  return el('div', { class: 'state state-loading', role: 'status' }, el('span', { class: 'spinner', 'aria-hidden': 'true' }), el('p', null, text));
}

export function progressBar(value, label) {
  const v = Math.max(0, Math.min(100, Math.round(Number(value) || 0)));
  const bar = el('div', { class: 'progress', role: 'progressbar', 'aria-valuemin': '0', 'aria-valuemax': '100', 'aria-valuenow': String(v), 'aria-label': label || 'İlerleme' },
    el('div', { class: 'progress-fill' }));
  bar.firstChild.style.width = `${v}%`;
  return bar;
}

export function chip(text, { kind = '', title } = {}) {
  return el('span', { class: `chip${kind ? ` chip-${kind}` : ''}`, title }, text);
}

// Birden çok alanın kirli olup olmadığını takip eder.
export function trackDirty(form, initial) {
  const snapshot = JSON.stringify(initial ?? readForm(form));
  return () => JSON.stringify(readForm(form)) !== snapshot;
}

export function segmented(options, value, onChange, label) {
  const group = el('div', { class: 'segmented', role: 'radiogroup', 'aria-label': label });
  const buttons = options.map(([val, text]) => {
    const b = el('button', { type: 'button', role: 'radio', class: 'segment', 'aria-checked': String(val === value), dataset: { value: val } }, text);
    b.addEventListener('click', () => {
      for (const other of buttons) other.setAttribute('aria-checked', String(other === b));
      onChange(val);
    });
    return b;
  });
  group.append(...buttons);
  return group;
}
