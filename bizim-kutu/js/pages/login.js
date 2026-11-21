// Giriş, PIN kurulumu ve kilit ekranı.
import { USERS, ALLOWED_UIDS } from '../constants.js';
import { loginWithPin } from '../auth.js';
import { h, clear, vibrate, sleep, fill, add } from '../utils/helpers.js';
import { icons, logoSvg } from '../utils/icons.js';
import { errorMessage } from '../utils/ui.js';

function floatingHearts() {
  const wrap = h('div', { class: 'hearts-bg', 'aria-hidden': 'true' });
  const glyphs = ['❤', '♡', '❥', '💗', '♥'];
  for (let i = 0; i < 14; i++) {
    const s = h('span', { class: 'float-heart' }, glyphs[i % glyphs.length]);
    s.style.left = `${(i * 7.3 + 3) % 100}%`;
    s.style.animationDelay = `${(i * 1.37) % 9}s`;
    s.style.animationDuration = `${9 + (i % 5) * 2}s`;
    s.style.fontSize = `${12 + (i % 4) * 6}px`;
    add(wrap, s);
  }
  return wrap;
}

function brand(sub = 'İki kişi, bir dünya, binlerce anı.') {
  return h('div', { class: 'auth-brand' },
    h('div', { class: 'auth-brand__logo heartbeat', svg: logoSvg }),
    h('h1', { class: 'auth-brand__title' }, 'Bizim Kutu'),
    h('p', { class: 'auth-brand__slogan' }, sub));
}

/** Kalp patlaması animasyonu (giriş başarılı). */
async function celebrate(container) {
  const burst = h('div', { class: 'burst', 'aria-hidden': 'true' });
  for (let i = 0; i < 12; i++) {
    const s = h('span', {}, '❤');
    s.style.setProperty('--a', `${i * 30}deg`);
    add(burst, s);
  }
  add(container, burst);
  await sleep(650);
}

// ---------------- Giriş: yalnızca PIN ----------------
export function renderLogin(root, { onLoggedIn }) {
  const msg = h('p', { class: 'auth-hint', 'aria-live': 'polite' }, 'PIN\'ini gir');
  const card = h('div', { class: 'auth-card glass' });
  let last = null;
  try { last = localStorage.getItem('bk.lastPerson'); } catch {}
  const pad = pinPad({ onComplete: async (v) => {
    msg.textContent = 'Kutumuz açılıyor…';
    card.classList.add('is-busy');
    try {
      const person = await loginWithPin(v);
      pad.destroy();
      await celebrate(card);
      onLoggedIn(person);
    } catch (e) {
      card.classList.remove('is-busy');
      pad.shake();
      msg.textContent = e.code === 'app/bad-pin' ? 'PIN hatalı, tekrar dene 🙈'
        : e.code === 'app/offline' ? 'İnternet bağlantısı yok.'
        : /admin-restricted|operation-not-allowed/.test(e.code || '') ? 'Firebase\'de "Anonim" giriş kapalı (kurulum adımı eksik).'
        : errorMessage(e);
    }
  } });
  add(card, brand(),
    h('div', { class: 'user-cards user-cards--mini', 'aria-hidden': 'true' },
      ALLOWED_UIDS.map((uid) => h('div', { class: `user-card user-card--${USERS[uid].tone}${last === uid ? ' is-selected' : ''}` },
        h('span', { class: 'user-card__avatar' }, USERS[uid].emoji), h('span', { class: 'user-card__name' }, USERS[uid].name)))),
    msg, pad.el);
  fill(root, h('div', { class: 'auth-screen' }, floatingHearts(), card));
}

// ---------------- PIN tuş takımı ----------------
function pinPad({ onComplete, length = 4 }) {
  let value = '';
  const dots = h('div', { class: 'pin-dots', 'aria-hidden': 'true' }, Array.from({ length }, () => h('span', { class: 'pin-dot' })));
  const live = h('span', { class: 'sr-only', 'aria-live': 'polite' });
  let busy = false;
  const paint = () => { [...dots.children].forEach((d, i) => d.classList.toggle('is-filled', i < value.length)); live.textContent = `${value.length} hane girildi`; };
  const press = async (d) => {
    if (busy) return;
    if (d === 'back') value = value.slice(0, -1);
    else if (value.length < length) value += d;
    vibrate(8);
    paint();
    if (value.length === length) {
      busy = true;
      const v = value;
      await sleep(120);
      try { await onComplete(v); } finally { value = ''; paint(); busy = false; }
    }
  };
  const keys = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '', '0', 'back'];
  const pad = h('div', { class: 'pin-pad', role: 'group', 'aria-label': 'PIN tuş takımı' },
    keys.map((k) => k === '' ? h('span') : h('button', {
      class: `pin-key${k === 'back' ? ' pin-key--back' : ''}`, type: 'button', 'aria-label': k === 'back' ? 'Sil' : k,
      svg: k === 'back' ? icons.backspace : undefined, onclick: () => press(k)
    }, k === 'back' ? null : k)));
  const onKey = (e) => {
    if (/^\d$/.test(e.key)) { e.preventDefault(); press(e.key); }
    else if (e.key === 'Backspace') { e.preventDefault(); press('back'); }
  };
  document.addEventListener('keydown', onKey);
  const el = h('div', { class: 'pin' }, dots, live, pad);
  return { el, shake: () => { dots.classList.add('shake'); vibrate([30, 40, 30]); setTimeout(() => dots.classList.remove('shake'), 450); }, destroy: () => document.removeEventListener('keydown', onKey) };
}

