// OYUN 1 — XOX (3x3). Sıra ve hücre geçerliliği hem istemcide hem RTDB kurallarında denetlenir.
import { h, clear, fill, add } from '../utils/helpers.js';
import { turnBanner, resultTitle, otherOf } from './common.js';

export const LINES = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]];
export const emptyBoard = () => Object.fromEntries(Array.from({ length: 9 }, (_, i) => [`c${i}`, '-']));

/** Kazanan çizgiyi döndürür ya da null. board: { c0..c8: 'X'|'O'|'-' } */
export function winningLine(board) {
  for (const l of LINES) {
    const [a, b, c] = l.map((i) => board[`c${i}`]);
    if (a !== '-' && a === b && b === c) return l;
  }
  return null;
}

/** Saf hamle fonksiyonu: geçersizse null, geçerliyse yeni durum. */
export function applyMove(state, uid, index, players) {
  const key = `c${index}`;
  if (state.winner || state.turn !== uid || !(index >= 0 && index < 9) || state.board[key] !== '-') return null;
  const next = structuredClone(state);
  next.board[key] = state.marks[uid];
  next.moves += 1;
  const line = winningLine(next.board);
  if (line) { next.winner = uid; next.line = line.join(','); next.tally[uid] = (next.tally[uid] || 0) + 1; }
  else if (next.moves === 9) { next.winner = 'draw'; next.tally.draw = (next.tally.draw || 0) + 1; }
  else next.turn = otherOf(players, uid);
  return next;
}

export default {
  create({ players, host, prev }) {
    const other = otherOf(players, host);
    const starter = prev ? otherOf(players, prev.starter) : host;
    return {
      board: emptyBoard(), marks: { [host]: 'X', [other]: 'O' }, turn: starter, starter, moves: 0, winner: '', line: '',
      tally: prev?.tally || { [host]: 0, [other]: 0, draw: 0 },
    };
  },

  mount(el, api) {
    const banner = h('div');
    const grid = h('div', { class: 'xox', role: 'grid', 'aria-label': 'XOX tahtası' });
    const cells = Array.from({ length: 9 }, (_, i) => {
      const b = h('button', { class: 'xox__cell', type: 'button', role: 'gridcell', onclick: () => move(i) });
      add(grid, b);
      return b;
    });
    const tally = h('div', { class: 'xox-tally' });
    add(el, banner, grid, tally);

    async function move(i) {
      const s = api.session;
      if (!s || s.status !== 'active') return;
      const players = Object.keys(s.players);
      if (!applyMove(s.state, api.me, i, players)) return;
      cells[i].classList.add('is-pending');
      await api.act((sess, st) => {
        const next = applyMove(st, api.me, i, players);
        if (!next) return undefined;
        sess.state = next;
        if (next.winner) { sess.status = 'finished'; sess.result = { winner: next.winner }; }
        return sess;
      });
      cells[i].classList.remove('is-pending');
    }

    return {
      update(s) {
        const st = s.state;
        const line = st.line ? st.line.split(',').map(Number) : [];
        cells.forEach((c, i) => {
          const v = st.board[`c${i}`];
          c.textContent = v === '-' ? '' : v;
          c.className = `xox__cell${v !== '-' ? ` is-${v.toLowerCase()} is-filled` : ''}${line.includes(i) ? ' is-win' : ''}`;
          c.disabled = v !== '-' || st.turn !== api.me || !!st.winner || s.status !== 'active';
          c.setAttribute('aria-label', `Satır ${Math.floor(i / 3) + 1}, sütun ${(i % 3) + 1}: ${v === '-' ? 'boş' : v}`);
        });
        fill(banner, st.winner ? h('div', { class: 'turn-banner' }, st.winner === 'draw' ? 'Berabere!' : `${api.name(st.winner)} kazandı!`)
          : turnBanner(api, st.turn, `Sıra sende! (${st.marks[api.me]})`, `${api.name(st.turn)} oynuyor… (${st.marks[st.turn]})`));
        fill(tally, 
          h('span', {}, `${api.name(api.me)} (${st.marks[api.me]}): `, h('b', {}, String(st.tally?.[api.me] || 0))),
          h('span', {}, 'Berabere: ', h('b', {}, String(st.tally?.draw || 0))),
          h('span', {}, `${api.name(api.partner)} (${st.marks[api.partner]}): `, h('b', {}, String(st.tally?.[api.partner] || 0))));
      },
    };
  },

  summary(s, api) {
    const st = s.state;
    return h('div', {}, resultTitle(api, s.result?.winner),
      h('p', { class: 'muted' }, `Bu oturumda: ${api.name(api.me)} ${st.tally?.[api.me] || 0} · ${api.name(api.partner)} ${st.tally?.[api.partner] || 0} · Berabere ${st.tally?.draw || 0}`));
  },
};
