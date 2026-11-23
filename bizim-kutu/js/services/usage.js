// Kullanım süresi: hangi bölümde ne kadar zaman geçirdik?
//
// Realtime Database:
//   stats/time/{kişi}/{bölüm}   saniye (home, chat, games, watch, memories, movies, tasks, vault, other, together)
//   stats/daily/{kişi}/{gün}    o gün sitede geçirilen toplam saniye (YYYY-MM-DD, yerel saat)
//
// Yalnızca ekran açık ve uygulama ön plandayken sayılır. 5 dakika hiç dokunulmazsa sayım durur
// (Birlikte İzle hariç: video izlerken ekrana dokunmamak normal). "together": partner de aynı anda çevrim içiyken.
import { rtdb } from '../firebase-config.js';
import { ref, rtdbTransaction } from '../vendor/firebase.js';
import { getState } from '../state.js';
import { sectionOf, dayKey } from '../utils/stats-logic.js';

export { sectionOf, dayKey, fmtDuration } from '../utils/stats-logic.js';

export const SECTIONS = {
  home: { label: 'Ana sayfa', emoji: '🏠' },
  chat: { label: 'Sohbet', emoji: '💬' },
  games: { label: 'Oyunlar', emoji: '🎮' },
  watch: { label: 'Birlikte İzle', emoji: '🎬' },
  memories: { label: 'Anı Defteri', emoji: '📖' },
  movies: { label: 'Film & Dizi', emoji: '🍿' },
  tasks: { label: 'Yapılacaklar', emoji: '✅' },
  vault: { label: 'Özel Kasa', emoji: '🔐' },
  other: { label: 'Diğer', emoji: '✨' },
};

const IDLE_MS = 5 * 60 * 1000;
const TICK_MS = 5000;
const FLUSH_MS = 60000;

/** Sayacı başlatır; durdurma fonksiyonu döndürür. */
export function startUsage(uid, partnerUid) {
  let last = Date.now();
  let lastActive = Date.now();
  const pending = {};          // { bölüm: saniye } — henüz yazılmamış
  const pendingDays = {};
  const add = (bag, k, v) => { bag[k] = (bag[k] || 0) + v; };

  const activity = () => { lastActive = Date.now(); };
  const evs = ['pointerdown', 'keydown', 'touchstart', 'wheel'];
  evs.forEach((e) => document.addEventListener(e, activity, { passive: true, capture: true }));

  function tick() {
    const now = Date.now();
    const dt = Math.min(now - last, TICK_MS * 3) / 1000; // uyku/arka plan sıçramalarını sayma
    last = now;
    if (document.visibilityState !== 'visible' || dt <= 0) return;
    const sec = sectionOf(getState().route);
    if (sec !== 'watch' && now - lastActive > IDLE_MS) return;
    add(pending, sec, dt);
    add(pendingDays, dayKey(), dt);
    if (getState().presence?.[partnerUid]?.online) add(pending, 'together', dt);
  }

  function flushBag(bag, path) {
    for (const [k, v] of Object.entries(bag)) {
      const whole = Math.floor(v);
      if (whole < 1) continue;
      bag[k] = v - whole;
      const amount = Math.min(whole, 3600);
      rtdbTransaction(ref(rtdb, `${path}/${k}`), (cur) => (typeof cur === 'number' ? cur : 0) + amount, { applyLocally: false })
        .catch(() => { bag[k] = (bag[k] || 0) + amount; }); // olmazsa sonra yeniden dene
    }
  }
  function flush() {
    tick();
    flushBag(pending, `stats/time/${uid}`);
    flushBag(pendingDays, `stats/daily/${uid}`);
  }

  const tickTimer = setInterval(tick, TICK_MS);
  const flushTimer = setInterval(flush, FLUSH_MS);
  const onVis = () => { if (document.visibilityState === 'hidden') flush(); else { last = Date.now(); lastActive = Date.now(); } };
  document.addEventListener('visibilitychange', onVis);
  window.addEventListener('pagehide', flush);

  return () => {
    flush();
    clearInterval(tickTimer); clearInterval(flushTimer);
    document.removeEventListener('visibilitychange', onVis);
    window.removeEventListener('pagehide', flush);
    evs.forEach((e) => document.removeEventListener(e, activity, { capture: true }));
  };
}
