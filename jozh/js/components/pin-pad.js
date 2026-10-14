// 4 haneli PIN tuş takımı (açılış ve Gizli Kasa ortak). Girilen PIN DOM'da ya da depolamada görünmez.
import { el, clear } from '../ui.js';
import { icon } from '../utils/icons.js';

const PIN_LENGTH = 4;

export function createPinPad({ mount, brand = 'JOZH', title, prompt, onComplete }) {
  let digits = [];
  let busy = false;
  let lockTimer = null;
  let lockedUntil = 0;

  const titleEl = el('h1', { class: 'pin-title' }, title || '');
  const promptEl = el('p', { class: 'pin-prompt' }, prompt || '');
  const dots = el('div', { class: 'pin-dots', 'aria-hidden': 'true' },
    Array.from({ length: PIN_LENGTH }, () => el('span', { class: 'pin-dot' })));
  const live = el('p', { class: 'visually-hidden', 'aria-live': 'polite' });
  const message = el('p', { class: 'pin-message', role: 'status', 'aria-live': 'polite' });
  const links = el('div', { class: 'pin-links' });

  const keys = [];
  const pad = el('div', { class: 'pin-pad', role: 'group', 'aria-label': 'Tuş takımı' });
  const layout = ['1', '2', '3', '4', '5', '6', '7', '8', '9', null, '0', 'del'];
  for (const k of layout) {
    if (k === null) {
      pad.append(el('span', { class: 'pin-spacer', 'aria-hidden': 'true' }));
    } else if (k === 'del') {
      const b = el('button', { type: 'button', class: 'pin-key pin-key-ghost', 'aria-label': 'Son rakamı sil' }, icon('backspace', { size: 26 }));
      b.addEventListener('click', removeDigit);
      keys.push(b);
      pad.append(b);
    } else {
      const b = el('button', { type: 'button', class: 'pin-key' }, k);
      b.addEventListener('click', () => addDigit(k));
      keys.push(b);
      pad.append(b);
    }
  }

  const screen = el('div', { class: 'lock-screen' },
    el('div', { class: 'pin-layout' },
      el('div', { class: 'pin-info' },
        el('div', { class: 'pin-brand' }, el('span', { class: 'brand-mark', 'aria-hidden': 'true' }, 'J'), el('span', { class: 'pin-brand-name' }, brand)),
        titleEl, promptEl, dots, live, message, links),
      pad));
  clear(mount).append(screen);

  function renderDots(state) {
    dots.classList.remove('is-error', 'is-success', 'shake');
    if (state) dots.classList.add(...state.split(' '));
    [...dots.children].forEach((d, i) => d.classList.toggle('is-filled', i < digits.length));
  }

  function announce() {
    live.textContent = `${digits.length} / ${PIN_LENGTH} rakam girildi`;
  }

  function setDisabled(disabled) {
    for (const k of keys) k.disabled = disabled;
  }

  async function addDigit(d) {
    if (busy || lockedUntil > Date.now() || digits.length >= PIN_LENGTH) return;
    if (message.dataset.kind === 'error') setMessage('');
    digits.push(d);
    renderDots();
    announce();
    if (digits.length === PIN_LENGTH) {
      const pin = digits.join('');
      digits = [];
      busy = true;
      setDisabled(true);
      try {
        await onComplete(pin);
      } finally {
        busy = false;
        if (!(lockedUntil > Date.now())) setDisabled(false);
      }
    }
  }

  function removeDigit() {
    if (busy || !digits.length) return;
    digits.pop();
    renderDots();
    announce();
  }

  function onKey(e) {
    if (e.target && (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') || document.querySelector('dialog[open]')) return;
    if (/^[0-9]$/.test(e.key)) {
      e.preventDefault();
      addDigit(e.key);
    } else if (e.key === 'Backspace') {
      e.preventDefault();
      removeDigit();
    }
  }
  document.addEventListener('keydown', onKey);

  function setMessage(text, kind = '') {
    message.textContent = text || '';
    message.dataset.kind = kind;
  }

  const api = {
    setTitle(text) { titleEl.textContent = text; },
    setPrompt(text) { promptEl.textContent = text; },
    setMessage,
    setLinks(list) {
      clear(links);
      for (const l of list || []) {
        links.append(el('button', { type: 'button', class: 'link-button', onclick: l.onClick }, l.label));
      }
    },
    reset() {
      digits = [];
      renderDots();
      live.textContent = '';
    },
    error(text) {
      digits = [];
      renderDots('is-error shake');
      setMessage(text, 'error');
      live.textContent = '';
      setTimeout(() => renderDots(), 650);
    },
    success(text) {
      dots.classList.remove('is-error', 'shake');
      [...dots.children].forEach((d) => d.classList.add('is-filled'));
      dots.classList.add('is-success');
      if (text) setMessage(text, 'success');
    },
    setBusy(value, text) {
      busy = value;
      setDisabled(value);
      if (text !== undefined) setMessage(text);
    },
    lockUntil(until, format) {
      lockedUntil = until;
      clearInterval(lockTimer);
      setDisabled(true);
      const tick = () => {
        const left = Math.ceil((lockedUntil - Date.now()) / 1000);
        if (left <= 0) {
          clearInterval(lockTimer);
          lockedUntil = 0;
          setDisabled(false);
          setMessage('Tekrar deneyebilirsin.');
          return;
        }
        setMessage(format(left), 'error');
      };
      tick();
      lockTimer = setInterval(tick, 1000);
    },
    destroy() {
      document.removeEventListener('keydown', onKey);
      clearInterval(lockTimer);
    }
  };
  return api;
}

export function formatWait(seconds) {
  if (seconds >= 60) {
    const m = Math.floor(seconds / 60);
    const s = seconds % 60;
    return `${m} dk ${String(s).padStart(2, '0')} sn`;
  }
  return `${seconds} sn`;
}
