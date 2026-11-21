// Küçük, bağımlılıksız uygulama durumu deposu.
const state = {
  user: null,          // Firebase kullanıcısı
  uid: null,
  partnerUid: null,
  connected: true,     // Realtime Database bağlantısı (.info/connected)
  online: navigator.onLine,
  serverOffset: 0,     // .info/serverTimeOffset
  presence: {},        // { uid: { online, lastSeen } }
  profiles: {},        // { uid: profil belgesi }
  prefs: { theme: 'system', reduceMotion: false, notif: { message: true, game: true, memory: true, task: true }, system: false, lockAfter: 2 },
  recentMessages: [],  // son mesajlar (ana sayfa, okunmamış sayısı)
  unreadMessages: 0,
  receipts: {},        // { uid: { readAt, deliveredAt } }
  notifications: [],
  invites: [],
  route: '',
};
const listeners = new Set();

export function getState() { return state; }

export function setState(patch) {
  let changed = false;
  for (const [k, v] of Object.entries(patch)) {
    if (state[k] !== v) { state[k] = v; changed = true; }
  }
  if (changed) for (const fn of [...listeners]) { try { fn(state, patch); } catch (e) { console.error(e); } }
}

/** Durum değişikliklerine abone olur; keys verilirse yalnızca o anahtarlar değişince çağrılır. */
export function subscribe(fn, keys = null) {
  const wrapped = keys ? (s, patch) => { if (keys.some((k) => k in patch)) fn(s, patch); } : fn;
  listeners.add(wrapped);
  return () => listeners.delete(wrapped);
}

/** Sunucu saatine göre şimdiki zaman (ms). */
export const serverNow = () => Date.now() + (state.serverOffset || 0);
