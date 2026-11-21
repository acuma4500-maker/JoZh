// OYUN 5 — Hafıza (kart eşleştirme). İki oyuncu aynı tahtayı görür, sırayla iki kart çevirir.
import { h, clear, shuffle, fill, add } from '../utils/helpers.js';
import { turnBanner, resultTitle, scoreLine, otherOf, toArray, winnerByScore } from './common.js';

export const SYMBOLS = ['💖', '🌹', '🧸', '🍓', '🌙', '☕', '🎁', '🦋', '🌻', '🍰', '🎈', '💍', '🐱', '🌈', '🍿', '🎵'];
export const PAIRS = 8;
const MISMATCH_MS = 1300;

export function newDeck(pairs = PAIRS) {
  const chosen = shuffle(SYMBOLS).slice(0, pairs);
  return shuffle([...chosen, ...chosen]);
}

/** Saf çevirme mantığı. Döner: yeni durum ya da null (geçersiz). */
export function applyFlip(state, uid, index, players, now) {
  const cards = toArray(state.cards);
  const matched = state.matched || {};
  const flipped = toArray(state.flipped);
  if (state.turn !== uid || flipped.length >= 2 || index < 0 || index >= cards.length || matched[`m${index}`] || flipped.includes(index)) return null;
  const next = structuredClone(state);
  next.flipped = [...flipped, index];
  next.moves = (state.moves || 0) + 1;
  if (next.flipped.length === 2) {
    const [a, b] = next.flipped;
    if (cards[a] === cards[b]) {
      next.matched = { ...matched, [`m${a}`]: uid, [`m${b}`]: uid };
      next.scores = { ...next.scores, [uid]: (next.scores?.[uid] || 0) + 1 };
      next.flipped = [];
      next.resolveAt = 0;
      if (Object.keys(next.matched).length === cards.length) next.done = true;
    } else {
      next.resolveAt = now + MISMATCH_MS;
    }
  }
  return next;
}

/** Eşleşmeyen iki kartı kapatıp sırayı devreder. */
export function applyResolve(state, players) {
  const flipped = toArray(state.flipped);
  if (flipped.length !== 2) return null;
  const next = structuredClone(state);
  next.flipped = [];
  next.resolveAt = 0;
  next.turn = otherOf(players, state.turn);
  return next;
}

export default {
  create({ players, host, prev }) {
    const starter = prev ? otherOf(players, prev.starter) : host;
    return { cards: newDeck(), matched: {}, flipped: [], turn: starter, starter, moves: 0, resolveAt: 0, done: false, scores: { [players[0]]: 0, [players[1]]: 0 } };
  },

  mount(el, api) {
    const banner = h('div');
    const score = h('div');
    const board = h('div', { class: 'memory', role: 'grid', 'aria-label': 'Hafıza kartları' });
    add(el, banner, score, board);
    let cardEls = [];
    let resolveTimer = null;
    api.scope.add(() => clearTimeout(resolveTimer));

    const players = () => Object.keys(api.session.players);

    async function flip(i) {
      const s = api.session;
      if (!applyFlip(s.state, api.me, i, players(), api.serverNow())) return;
      await api.act((sess, st) => {
        const next = applyFlip(st, api.me, i, players(), api.serverNow());
        if (!next) return undefined;
        sess.state = next;
        if (next.done) { sess.status = 'finished'; sess.result = { winner: winnerByScore(next.scores, players()) }; }
        return sess;
      });
    }

    function scheduleResolve(st) {
      clearTimeout(resolveTimer);
      const flipped = toArray(st.flipped);
      if (flipped.length !== 2 || !st.resolveAt) return;
      // Sıradaki oyuncu çevrim dışı kalırsa diğer cihaz da 2 sn sonra çözebilir.
      const delay = Math.max(0, st.resolveAt - api.serverNow()) + (st.turn === api.me ? 0 : 2000);
      resolveTimer = setTimeout(() => api.act((sess, cur) => {
        const next = applyResolve(cur, players());
        if (!next || cur.resolveAt !== st.resolveAt) return undefined;
        sess.state = next;
        return sess;
      }), delay);
    }

    return {
      update(s) {
        const st = s.state;
        const cards = toArray(st.cards);
        const matched = st.matched || {};
        const flipped = toArray(st.flipped);
        if (cardEls.length !== cards.length) {
          clear(board);
          cardEls = cards.map((_, i) => {
            const b = h('button', { class: 'mcard', type: 'button', onclick: () => flip(i) },
              h('span', { class: 'mcard__inner' }, h('span', { class: 'mcard__back', 'aria-hidden': 'true' }, '❤'), h('span', { class: 'mcard__front' })));
            add(board, b);
            return b;
          });
        }
        cards.forEach((sym, i) => {
          const owner = matched[`m${i}`];
          const up = !!owner || flipped.includes(i);
          const b = cardEls[i];
          b.classList.toggle('is-up', up);
          b.classList.toggle('is-matched', !!owner);
          b.classList.toggle('is-mine', owner === api.me);
          b.querySelector('.mcard__front').textContent = up ? sym : '';
          b.disabled = up || st.turn !== api.me || flipped.length >= 2 || s.status !== 'active';
          b.setAttribute('aria-label', up ? `Kart ${i + 1}: ${sym}${owner ? ', eşleşti' : ''}` : `Kart ${i + 1}: kapalı`);
        });
        fill(banner, turnBanner(api, st.turn, flipped.length === 2 && st.resolveAt ? 'Eşleşmedi… 🙈' : 'Sıra sende, iki kart çevir!'));
        fill(score, scoreLine(api, st.scores));
        scheduleResolve(st);
      },
    };
  },

  summary(s, api) {
    return h('div', {}, resultTitle(api, s.result?.winner), scoreLine(api, s.state.scores), h('p', { class: 'muted' }, `${s.state.moves} kart çevrildi`));
  },
};
