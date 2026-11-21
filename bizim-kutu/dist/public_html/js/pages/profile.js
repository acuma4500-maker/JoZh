// Profil ve ayarlar.
import { getState, subscribe } from '../state.js';
import { ALLOWED_UIDS, START_DATE, APP_VERSION, userName, userEmoji } from '../constants.js';
import { h, clear, fill, add } from '../utils/helpers.js';
import { icons } from '../utils/icons.js';
import { toast, confirmDialog, openModal, errorMessage, field } from '../utils/ui.js';
import { lastSeenText, formatLongDate } from '../utils/dates.js';
import { LIMITS, validateText, isPin } from '../utils/validation.js';
import { saveProfile } from '../services/firestore.js';
import { hasPin, setPin, removePin, verifyPin } from '../services/pinlock.js';
import { setPrefs, logout } from '../app.js';

export default async function profile(page, { scope }) {
  const { uid, user } = getState();
  const cards = h('div', { class: 'profile-cards' });
  const drawCards = () => {
    const s = getState();
    fill(cards, ...ALLOWED_UIDS.map((u) => {
      const p = s.presence[u];
      const prof = s.profiles[u] || {};
      return h('article', { class: `card profile-card${u === uid ? ' is-me' : ''}` },
        h('div', { class: 'profile-card__avatar', 'aria-hidden': 'true' }, userEmoji(u), h('span', { class: `dot ${p?.online ? 'dot--on' : 'dot--off'}` })),
        h('h3', {}, userName(u), u === uid ? h('span', { class: 'pill' }, 'sen') : null),
        prof.nickname ? h('p', { class: 'profile-card__nick' }, `“${prof.nickname}”`) : null,
        h('p', { class: 'muted small' }, p?.online ? '🟢 Çevrim içi' : `⚪ ${lastSeenText(p?.lastSeen)}`),
        h('dl', { class: 'kv' },
          h('dt', {}, 'Kullanıcı kimliği'), h('dd', { class: 'mono' }, u),
          h('dt', {}, 'Birliktelik başlangıcı'), h('dd', {}, formatLongDate(new Date(START_DATE.year, START_DATE.month - 1, START_DATE.day)))));
    }));
  };
  drawCards();
  scope.add(subscribe(drawCards, ['presence', 'profiles']));

  const prefs = () => getState().prefs;
  const persist = async (patch) => {
    const next = { ...prefs(), ...patch, notif: { ...prefs().notif, ...(patch.notif || {}) } };
    setPrefs(next);
    try { await saveProfile({ prefs: next }); } catch (e) { toast(errorMessage(e), { type: 'error' }); }
  };

  // Takma ad
  const nick = h('input', { class: 'input', value: getState().profiles[uid]?.nickname || '', maxlength: String(LIMITS.nickname), placeholder: 'Örn. Ayıcık' });
  const nickForm = h('form', { class: 'row', onsubmit: async (e) => {
    e.preventDefault();
    const v = validateText(nick.value, { label: 'Takma ad', min: 0, max: LIMITS.nickname, multiline: false });
    if (!v.ok) return toast(v.error, { type: 'error' });
    try { await saveProfile({ nickname: v.value }); toast('Kaydedildi'); } catch (er) { toast(errorMessage(er), { type: 'error' }); }
  } }, nick, h('button', { class: 'btn btn--soft btn--sm', type: 'submit' }, 'Kaydet'));

  // Tema
  const themeGroup = h('div', { class: 'segmented', role: 'radiogroup', 'aria-label': 'Tema' });
  const drawTheme = () => fill(themeGroup, ...[['system', '🖥️ Sistem'], ['light', '☀️ Açık'], ['dark', '🌙 Koyu']].map(([v, l]) =>
    h('button', { class: `segmented__btn${prefs().theme === v ? ' is-active' : ''}`, type: 'button', role: 'radio', 'aria-checked': String(prefs().theme === v), onclick: async () => { await persist({ theme: v }); drawTheme(); } }, l)));
  drawTheme();

  const toggle = (label, checked, onChange, hint) => {
    const input = h('input', { type: 'checkbox', role: 'switch', checked, onchange: (e) => onChange(e.target.checked, e.target) });
    return h('label', { class: 'switch-row' }, h('span', {}, h('span', { class: 'switch-row__label' }, label), hint ? h('small', { class: 'muted' }, hint) : null), h('span', { class: 'switch' }, input, h('span', { class: 'switch__track', 'aria-hidden': 'true' })));
  };

  const notifRows = [['message', '💬 Yeni mesajlar'], ['game', '🎮 Oyun davetleri'], ['memory', '📖 Yeni anılar'], ['task', '✅ Görevler']]
    .map(([k, l]) => toggle(l, prefs().notif?.[k] !== false, (v) => persist({ notif: { [k]: v } })));
  const systemToggle = toggle('Tarayıcı bildirimleri', !!prefs().system, async (v, input) => {
    if (v) {
      if (!('Notification' in window)) { input.checked = false; return toast('Bu tarayıcı bildirimleri desteklemiyor. iPhone\'da önce "Ana Ekrana Ekle" ile uygulamayı yükleyin.', { type: 'error', duration: 6000 }); }
      const perm = await Notification.requestPermission();
      if (perm !== 'granted') { input.checked = false; return toast('Bildirim izni verilmedi.', { type: 'error' }); }
    }
    persist({ system: v });
  }, 'Uygulama açıkken arka plandaki sekmede bildirim gösterir.');

  // Cihaz PIN'i
  const pinSection = h('div', {});
  const drawPin = () => {
    const on = hasPin(uid);
    const lockSel = h('select', { class: 'input', onchange: (e) => persist({ lockAfter: Number(e.target.value) }) },
      [[0, 'Hemen'], [1, '1 dakika'], [2, '2 dakika'], [5, '5 dakika'], [15, '15 dakika'], [-1, 'Otomatik kilitleme yok']].map(([v, l]) => h('option', { value: String(v), selected: Number(prefs().lockAfter ?? 2) === v }, l)));
    fill(pinSection, 
      h('p', { class: 'muted small' }, on ? '🔐 Bu cihazda PIN kilidi açık.' : 'Bu cihazda PIN kilidi kapalı.'),
      on ? field('Arka plandan dönünce kilitle', lockSel) : null,
      h('div', { class: 'row' },
        h('button', { class: 'btn btn--soft btn--sm', type: 'button', onclick: () => pinDialog(on) }, on ? 'PIN\'i değiştir' : 'PIN belirle'),
        on ? h('button', { class: 'btn btn--ghost btn--sm', type: 'button', onclick: removeDialog }, 'PIN\'i kaldır') : null));
  };
  function removeDialog() {
    const cur = h('input', { class: 'input', type: 'password', inputmode: 'numeric', maxlength: '4', autocomplete: 'off' });
    const err = h('p', { class: 'form-error', role: 'alert' });
    const m = openModal({ title: 'PIN kilidini kaldır', sheet: false, content: h('form', { class: 'form', onsubmit: async (e) => {
      e.preventDefault();
      const r = await verifyPin(uid, cur.value);
      if (!r.ok && !r.wiped) { err.textContent = `PIN hatalı (${r.remaining} hak).`; return; }
      removePin(uid); m.close(); drawPin();
      toast(r.ok ? 'PIN kilidi kaldırıldı' : 'Çok fazla hata: PIN silindi.', { type: r.ok ? 'info' : 'error' });
    } }, field('Mevcut PIN', cur), err, h('button', { class: 'btn btn--danger btn--block', type: 'submit' }, 'Kaldır')) });
  }
  function pinDialog(change) {
    const cur = h('input', { class: 'input', type: 'password', inputmode: 'numeric', maxlength: '4', autocomplete: 'off' });
    const p1 = h('input', { class: 'input', type: 'password', inputmode: 'numeric', maxlength: '4', autocomplete: 'off' });
    const p2 = h('input', { class: 'input', type: 'password', inputmode: 'numeric', maxlength: '4', autocomplete: 'off' });
    const err = h('p', { class: 'form-error', role: 'alert' });
    const m = openModal({ title: change ? 'PIN\'i değiştir' : 'Cihaz PIN\'i belirle', sheet: false, content: h('form', { class: 'form', onsubmit: async (e) => {
      e.preventDefault();
      if (change) { const r = await verifyPin(uid, cur.value); if (!r.ok) { err.textContent = r.wiped ? 'Çok fazla hata: PIN silindi.' : `Mevcut PIN hatalı (${r.remaining} hak).`; if (r.wiped) { m.close(); drawPin(); } return; } }
      if (!isPin(p1.value)) { err.textContent = 'PIN 4 rakam olmalı.'; return; }
      if (p1.value !== p2.value) { err.textContent = 'PIN\'ler eşleşmiyor.'; return; }
      await setPin(uid, p1.value);
      toast('PIN kaydedildi 🔐'); m.close(); drawPin();
    } }, change ? field('Mevcut PIN', cur) : null, field('Yeni PIN (4 rakam)', p1), field('Yeni PIN tekrar', p2), err,
      h('button', { class: 'btn btn--primary btn--block', type: 'submit' }, 'Kaydet')) });
  }
  drawPin();

  const lastSignIn = user?.metadata?.lastSignInTime ? new Date(user.metadata.lastSignInTime) : null;
  add(page, 
    h('div', { class: 'page-head' }, h('div', {}, h('h2', { class: 'page-title' }, 'Profil'), h('p', { class: 'page-sub' }, 'İkimiz ve ayarlarımız.'))),
    cards,
    h('section', { class: 'card settings' },
      h('h3', {}, 'Profilim'), field('Takma ad (isteğe bağlı)', nickForm)),
    h('section', { class: 'card settings' },
      h('h3', {}, 'Görünüm'), h('div', { class: 'field' }, h('span', { class: 'field__label' }, 'Tema'), themeGroup),
      toggle('Animasyonları azalt', !!prefs().reduceMotion, (v) => persist({ reduceMotion: v }), 'Cihazın "hareketi azalt" ayarına zaten uyulur.')),
    h('section', { class: 'card settings' }, h('h3', {}, 'Bildirimler'), ...notifRows, systemToggle,
      h('p', { class: 'muted small' }, 'Not: Tarayıcı tamamen kapalıyken gelen push bildirimleri için Firebase Cloud Messaging + sunucu tarafı gönderici (Cloud Functions, Blaze planı) gerekir; bu sürümde yoktur.')),
    h('section', { class: 'card settings' }, h('h3', {}, 'Oturum güvenliği'),
      h('dl', { class: 'kv' },
        h('dt', {}, 'Giriş yöntemi'), h('dd', {}, 'Firebase Authentication (e-posta/parola)'),
        h('dt', {}, 'E-posta'), h('dd', {}, user?.email || '—'),
        h('dt', {}, 'Son giriş'), h('dd', {}, lastSignIn ? lastSignIn.toLocaleString('tr-TR') : '—'),
        h('dt', {}, 'Veri erişimi'), h('dd', {}, 'Güvenlik kurallarıyla yalnızca iki kullanıcı kimliğine (UID) açık')),
      h('h4', {}, 'Cihaz PIN kilidi'), pinSection,
      h('p', { class: 'muted small' }, 'PIN yalnızca bu cihazda uygulamayı kilitler; hesabın asıl koruması parolandır. Ortak bir cihazda mutlaka çıkış yap.'),
      h('button', { class: 'btn btn--danger btn--block', type: 'button', onclick: async () => {
        if (await confirmDialog({ title: 'Çıkış yapılsın mı?', message: 'Bu cihazdaki oturum kapanacak. Tekrar girmek için e-posta ve parola gerekir.', confirmText: 'Çıkış yap', danger: true })) logout();
      } }, h('span', { svg: icons.logout }), 'Oturumu kapat')),
    h('p', { class: 'muted small center' }, `Bizim Kutu v${APP_VERSION} · İki kişi, bir dünya, binlerce anı.`));
}
