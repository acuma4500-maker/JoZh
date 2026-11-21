// Giriş, PIN kurulumu ve kilit ekranı.
import { USERS, ALLOWED_UIDS, userName, userEmoji } from '../constants.js';
import { login, rememberedEmail, resetPassword } from '../auth.js';
import { setPin, verifyPin, MAX_FAILS, removePin } from '../services/pinlock.js';
import { h, clear, vibrate, sleep, fill, add } from '../utils/helpers.js';
import { icons, logoSvg } from '../utils/icons.js';
import { toast, errorMessage, setLoading } from '../utils/ui.js';

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

function userCard(uid, { selected, disabled, onClick, sub }) {
  const u = USERS[uid];
  return h('button', {
    class: `user-card user-card--${u.tone}${selected ? ' is-selected' : ''}`, type: 'button', disabled,
    'aria-pressed': selected ? 'true' : 'false', onclick: onClick
  },
    h('span', { class: 'user-card__avatar', 'aria-hidden': 'true' }, u.emoji),
    h('span', { class: 'user-card__name' }, u.name),
    sub ? h('span', { class: 'user-card__sub' }, sub) : null);
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

// ---------------- Giriş ----------------
export function renderLogin(root, { reason, onLoggedIn }) {
  let selected = null;
  const cards = h('div', { class: 'user-cards', role: 'group', 'aria-label': 'Kim giriş yapıyor?' });
  const formWrap = h('div', { class: 'auth-form-wrap' });
  const screen = h('div', { class: 'auth-screen' }, floatingHearts(),
    h('div', { class: 'auth-card glass' }, brand(), h('p', { class: 'auth-q' }, 'Kim geldi bakalım?'), cards, formWrap));
  fill(root, screen);

  if (reason === 'not-allowed') toast('Bu hesabın Bizim Kutu\'ya erişimi yok.', { type: 'error', duration: 6000 });

  const drawCards = () => {
    fill(cards, ...ALLOWED_UIDS.map((uid) => userCard(uid, { selected: selected === uid, onClick: () => { selected = uid; drawCards(); drawForm(); } })));
  };

  function drawForm() {
    clear(formWrap);
    if (!selected) {
      add(formWrap, h('p', { class: 'auth-hint' }, 'Kartına dokun, ardından hesabınla güvenli giriş yap.'));
      return;
    }
    const email = h('input', { class: 'input', type: 'email', autocomplete: 'username', inputmode: 'email', required: true, placeholder: 'ornek@eposta.com', value: rememberedEmail(selected), 'aria-label': 'E-posta' });
    const pass = h('input', { class: 'input', type: 'password', autocomplete: 'current-password', required: true, placeholder: 'Parolan', 'aria-label': 'Parola', minlength: '6' });
    const toggle = h('button', { class: 'input-addon', type: 'button', 'aria-label': 'Parolayı göster', svg: icons.eye, onclick: () => { pass.type = pass.type === 'password' ? 'text' : 'password'; toggle.setAttribute('aria-label', pass.type === 'password' ? 'Parolayı göster' : 'Parolayı gizle'); } });
    const remember = h('input', { type: 'checkbox', checked: true });
    const err = h('p', { class: 'form-error', role: 'alert' });
    const submit = h('button', { class: 'btn btn--primary btn--block', type: 'submit' }, `${userName(selected)} olarak giriş yap`);
    const forgot = h('button', { class: 'link-btn', type: 'button', onclick: async () => {
      if (!email.value.trim()) { err.textContent = 'Önce e-posta adresini yaz.'; email.focus(); return; }
      try { await resetPassword(email.value); toast('Parola sıfırlama bağlantısı e-postana gönderildi 💌'); }
      catch (e) { err.textContent = errorMessage(e); }
    } }, 'Parolamı unuttum');
    const form = h('form', { class: 'auth-form', novalidate: true, onsubmit: async (e) => {
      e.preventDefault();
      err.textContent = '';
      if (!email.value.trim() || !pass.value) { err.textContent = 'E-posta ve parola gerekli.'; return; }
      setLoading(submit, true, 'Kutumuz açılıyor…');
      try {
        const user = await login(email.value, pass.value, selected, remember.checked);
        pass.value = '';
        await celebrate(screen);
        onLoggedIn(user, true);
      } catch (e2) {
        err.textContent = e2.code?.startsWith('app/') ? e2.message : errorMessage(e2);
        screen.querySelector('.auth-card')?.classList.add('shake');
        setTimeout(() => screen.querySelector('.auth-card')?.classList.remove('shake'), 500);
        setLoading(submit, false);
      }
    } },
      h('label', { class: 'field__label' }, 'E-posta', email),
      h('label', { class: 'field__label' }, 'Parola', h('div', { class: 'input-group' }, pass, toggle)),
      h('label', { class: 'check' }, remember, h('span', {}, 'E-postamı bu cihazda hatırla')),
      err, submit, forgot,
      h('p', { class: 'auth-note' }, h('span', { svg: icons.shield }), ' İlk girişten sonra bu cihaz için 4 haneli PIN belirleyip uygulamayı PIN ile açabilirsin.'));
    add(formWrap, form);
    requestAnimationFrame(() => (email.value ? pass : email).focus());
  }
  drawCards(); drawForm();
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

export function renderPinSetup(root, { uid, onDone }) {
  let first = null;
  const title = h('h2', { class: 'auth-step-title' }, 'Bu cihaz için PIN belirle');
  const msg = h('p', { class: 'auth-hint' }, 'Uygulamayı her açtığında bu 4 haneli PIN istenir.');
  const pad = pinPad({ onComplete: async (v) => {
    if (!first) { first = v; title.textContent = 'PIN\'i tekrar gir'; msg.textContent = 'Onaylamak için aynı PIN\'i bir kez daha gir.'; return; }
    if (v !== first) { first = null; pad.shake(); title.textContent = 'PIN\'ler eşleşmedi'; msg.textContent = 'Baştan başlayalım: yeni PIN\'i gir.'; return; }
    await setPin(uid, v);
    pad.destroy();
    toast('PIN kaydedildi 🔐');
    onDone();
  } });
  fill(root, h('div', { class: 'auth-screen' }, floatingHearts(),
    h('div', { class: 'auth-card glass' }, brand(`Hoş geldin ${userName(uid)} ${userEmoji(uid)}`), title, msg, pad.el,
      h('details', { class: 'auth-details' }, h('summary', {}, 'PIN ne kadar güvenli?'),
        h('p', {}, 'PIN yalnızca bu cihazda uygulamayı kilitler; karması (PBKDF2) bu cihazda saklanır, sunucuya gönderilmez. Hesabın asıl güvenliği Firebase parolanla sağlanır. 5 hatalı denemede PIN silinir ve tekrar parolayla giriş gerekir.')),
      h('button', { class: 'btn btn--ghost btn--block', type: 'button', onclick: () => { pad.destroy(); onDone(); } }, 'Şimdilik geç'))));
}

export function renderLock(root, { uid, onUnlock, onSwitch }) {
  const other = ALLOWED_UIDS.find((u) => u !== uid);
  const msg = h('p', { class: 'auth-hint', 'aria-live': 'polite' }, 'PIN\'ini gir');
  const card = h('div', { class: 'auth-card glass' });
  const pad = pinPad({ onComplete: async (v) => {
    const r = await verifyPin(uid, v);
    if (r.ok) { pad.destroy(); card.classList.add('unlocking'); await celebrate(card); onUnlock(); return; }
    pad.shake();
    if (r.wiped) {
      pad.destroy();
      toast('Çok fazla hatalı deneme. Güvenliğin için parolayla yeniden giriş yapmalısın.', { type: 'error', duration: 7000 });
      removePin(uid);
      onSwitch();
      return;
    }
    msg.textContent = `Hatalı PIN. ${r.remaining} deneme hakkın kaldı.`;
  } });
  add(card, brand(),
    h('div', { class: 'user-cards' },
      userCard(uid, { selected: true, sub: 'Bu cihazda oturum açık' }),
      userCard(other, { disabled: true, sub: 'Kilitli' })),
    msg, pad.el,
    h('button', { class: 'link-btn', type: 'button', onclick: () => { pad.destroy(); onSwitch(); } }, 'Parolayla / farklı hesapla giriş yap'),
    h('p', { class: 'auth-note' }, `En fazla ${MAX_FAILS} deneme hakkın var.`));
  fill(root, h('div', { class: 'auth-screen' }, floatingHearts(), card));
}
