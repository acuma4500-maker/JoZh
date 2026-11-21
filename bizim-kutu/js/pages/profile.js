// Profil ve ayarlar.
import { getState, subscribe } from '../state.js';
import { ALLOWED_UIDS, START_DATE, APP_VERSION, userName, userEmoji } from '../constants.js';
import { h, clear, fill, add } from '../utils/helpers.js';
import { icons } from '../utils/icons.js';
import { toast, confirmDialog, openModal, errorMessage, field } from '../utils/ui.js';
import { lastSeenText, formatLongDate } from '../utils/dates.js';
import { LIMITS, validateText } from '../utils/validation.js';
import { saveProfile } from '../services/firestore.js';
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

  // Otomatik kilit
  const lockSel = h('select', { class: 'input', onchange: (e) => persist({ lockAfter: Number(e.target.value) }) },
    [[0, 'Hemen'], [1, '1 dakika'], [2, '2 dakika'], [5, '5 dakika'], [15, '15 dakika'], [-1, 'Otomatik kilitleme yok']].map(([v, l]) => h('option', { value: String(v), selected: Number(prefs().lockAfter ?? 2) === v }, l)));

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
        h('dt', {}, 'Giriş yöntemi'), h('dd', {}, '4 haneli PIN (Firebase sunucusunda doğrulanır, sitede yazmaz)'),
        h('dt', {}, 'Bu cihaz'), h('dd', { class: 'mono' }, user?.uid || '—'),
        h('dt', {}, 'Veri erişimi'), h('dd', {}, 'Yalnızca doğru PIN girilmiş cihazlar')),
      field('Arka plandan dönünce PIN iste', lockSel),
      h('p', { class: 'muted small' }, 'PIN\'i değiştirmek için Firebase Console\'da secrets/pins kaydını güncelleyin (README). Ortak bir cihazda mutlaka çıkış yap.'),
      h('button', { class: 'btn btn--danger btn--block', type: 'button', onclick: async () => {
        if (await confirmDialog({ title: 'Çıkış yapılsın mı?', message: 'Bu cihazdaki oturum kapanacak. Tekrar girmek için PIN gerekir.', confirmText: 'Çıkış yap', danger: true })) logout();
      } }, h('span', { svg: icons.logout }), 'Oturumu kapat')),
    h('p', { class: 'muted small center' }, `Bizim Kutu v${APP_VERSION} · İki kişi, bir dünya, binlerce anı.`));
}
