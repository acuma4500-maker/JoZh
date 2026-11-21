// Firebase'e bağımlı olmayan sabitler (testlerde de kullanılır).
// Yetkilendirme yalnızca UID ile yapılır; isimler sadece görüntüleme içindir.
export const USERS = Object.freeze({
  pt0Kmbc9rqdJekFyvA1wLItUnxw1: Object.freeze({ key: 'cuma', name: 'Cuma', emoji: '🧸', tone: 'blue' }),
  cf6RqCRF6dPEWtSR1L9Dm2Uv4Ap1: Object.freeze({ key: 'ilayda', name: 'İlayda', emoji: '🌷', tone: 'pink' })
});
export const ALLOWED_UIDS = Object.freeze(Object.keys(USERS));
export const COUPLE_ID = 'main';
// İlişki başlangıcı: 22 Ağustos 2026, cihazın yerel saatiyle gece yarısı.
export const START_DATE = Object.freeze({ year: 2026, month: 8, day: 22 });
export const APP_VERSION = '1.0.0';
export const BUILD = 'dev'; // tools/make-zip.sh dağıtımda bunu sürüm karmasıyla değiştirir

export const isAllowedUid = (uid) => typeof uid === 'string' && ALLOWED_UIDS.includes(uid);
export const partnerOf = (uid) => ALLOWED_UIDS.find((u) => u !== uid) || null;
export const userName = (uid) => USERS[uid]?.name || 'Bilinmeyen';
export const userEmoji = (uid) => USERS[uid]?.emoji || '💗';
