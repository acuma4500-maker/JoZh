import test from 'node:test';
import assert from 'node:assert/strict';
import xox, { winningLine, applyMove, emptyBoard } from '../../js/games/xox.js';
import memory, { applyFlip, applyResolve, newDeck } from '../../js/games/memory.js';
import knowMe, { QUESTIONS, CATEGORIES, pickQuestions } from '../../js/games/know-me.js';
import truthDare, { TRUTHS, DARES, pickPrompt } from '../../js/games/truth-dare.js';
import emoji, { isCorrect, WORDS } from '../../js/games/emoji.js';
import { OPENINGS, createStory } from '../../js/games/story-data.js';
import { pickQuestion } from '../../js/utils/questions-data.js';
import { winnerByScore, toArray } from '../../js/games/common.js';
import { normalizeGuess, shuffle, randomInt } from '../../js/utils/helpers.js';

const A = 'pt0Kmbc9rqdJekFyvA1wLItUnxw1', B = 'cf6RqCRF6dPEWtSR1L9Dm2Uv4Ap1';
const P = [A, B];

test('XOX: kazanan çizgiler', () => {
  const b = emptyBoard(); b.c0 = b.c4 = b.c8 = 'X';
  assert.deepEqual(winningLine(b), [0, 4, 8]);
  assert.equal(winningLine(emptyBoard()), null);
});

test('XOX: sıra, dolu hücre ve beraberlik kontrolü', () => {
  let s = xox.create({ players: P, host: A, prev: null });
  assert.equal(s.turn, A); assert.equal(s.marks[A], 'X'); assert.equal(s.marks[B], 'O');
  assert.equal(applyMove(s, B, 0, P), null, 'sırası olmayan oynayamaz');
  s = applyMove(s, A, 4, P);
  assert.equal(s.board.c4, 'X'); assert.equal(s.turn, B); assert.equal(s.moves, 1);
  assert.equal(applyMove(s, B, 4, P), null, 'dolu hücre');
  assert.equal(applyMove(s, B, 9, P), null, 'geçersiz hücre');
  // Beraberlik: X O X / X O O / O X X
  const seq = [[B, 0], [A, 2], [B, 6], [A, 3], [B, 5], [A, 7], [B, 1], [A, 8]];
  // yeniden kur: A:4, B:0, A:2, B:6, A:3, B:5, A:7, B:1, A:8 → beraberlik
  for (const [u, i] of seq) { s = applyMove(s, u, i, P); assert.ok(s, `${u} ${i}`); }
  assert.equal(s.winner, 'draw');
  assert.equal(s.tally.draw, 1);
});

test('XOX: kazanma ve rövanşta başlayan değişir', () => {
  let s = xox.create({ players: P, host: A, prev: null });
  for (const [u, i] of [[A, 0], [B, 3], [A, 1], [B, 4], [A, 2]]) s = applyMove(s, u, i, P);
  assert.equal(s.winner, A); assert.equal(s.line, '0,1,2'); assert.equal(s.tally[A], 1);
  assert.equal(applyMove(s, B, 8, P), null, 'bitmiş oyunda hamle yok');
  const r = xox.create({ players: P, host: A, prev: s });
  assert.equal(r.starter, B); assert.equal(r.tally[A], 1); assert.equal(r.moves, 0);
});

test('Hafıza: deste 8 çift, eşleşme ve sıra devri', () => {
  const deck = newDeck();
  assert.equal(deck.length, 16);
  const counts = {}; deck.forEach((c) => { counts[c] = (counts[c] || 0) + 1; });
  assert.ok(Object.values(counts).every((n) => n === 2));
  const s0 = memory.create({ players: P, host: A, prev: null });
  const st = { ...s0, cards: ['🍓', '🍓', '🌙', '🌙'] };
  assert.equal(applyFlip(st, B, 0, P, 0), null, 'sıra A\'da');
  let s1 = applyFlip(st, A, 0, P, 1000);
  s1 = applyFlip(s1, A, 1, P, 1000);
  assert.equal(s1.scores[A], 1); assert.equal(s1.turn, A, 'eşleşince aynı oyuncu devam eder');
  assert.deepEqual(toArray(s1.flipped), []);
  let s2 = applyFlip(s1, A, 2, P, 2000);
  assert.equal(applyFlip(s2, A, 2, P, 2000), null, 'aynı kart iki kez çevrilemez');
  s2 = applyFlip(s2, A, 0, P, 2000);
  assert.equal(s2, null, 'eşleşmiş kart çevrilemez');
  let s3 = applyFlip(s1, A, 2, P, 3000);
  s3 = { ...s3, cards: ['🍓', '🍓', '🌙', '🍰'] };
  const s4 = applyFlip({ ...s1, cards: ['🍓', '🍓', '🌙', '🍰'], flipped: [2] }, A, 3, P, 3000);
  assert.equal(s4.resolveAt, 4300); assert.equal(s4.turn, A);
  const s5 = applyResolve(s4, P);
  assert.equal(s5.turn, B); assert.deepEqual(s5.flipped, []);
  void s3;
});

test('Hafıza: tüm kartlar eşleşince oyun biter', () => {
  let s = { ...memory.create({ players: P, host: A }), cards: ['a', 'a'] };
  s = applyFlip(applyFlip(s, A, 0, P, 0), A, 1, P, 0);
  assert.equal(s.done, true);
  assert.equal(winnerByScore(s.scores, P), A);
});

test('Tanıyor muyuz: 40 soru, 5 kategori, tur seçimi', () => {
  assert.equal(QUESTIONS.length, 40);
  assert.equal(CATEGORIES.length, 5);
  for (const c of CATEGORIES) assert.equal(QUESTIONS.filter((q) => q.c === c.id).length, 8);
  assert.ok(QUESTIONS.every((q) => q.guess.includes('{n}')));
  const picked = pickQuestions('hayaller');
  assert.equal(picked.length, 6);
  assert.ok(picked.every((i) => QUESTIONS[i].c === 'hayaller'));
  assert.equal(new Set(pickQuestions('mixed')).size, 6);
  const s = knowMe.create({ players: P, host: A });
  assert.equal(s.phase, 'setup'); assert.equal(s.subject, A);
});

test('Doğruluk/Cesaret: benzersiz görevler ve tekrar etmeyen seçim', () => {
  assert.equal(new Set(TRUTHS).size, TRUTHS.length);
  assert.equal(new Set(DARES).size, DARES.length);
  assert.ok(TRUTHS.length >= 40 && DARES.length >= 40);
  const used = TRUTHS.map((_, i) => i).filter((i) => i !== 7);
  assert.equal(pickPrompt('truth', used), 7);
  const s = truthDare.create({ players: P, host: B });
  assert.equal(s.turn, B); assert.equal(s.phase, 'choose');
});

test('Emojiyle anlat: tahmin normalizasyonu', () => {
  assert.ok(isCorrect('  aslan KRAL ', 'Aslan Kral'));
  assert.ok(isCorrect('cikolatali pasta', 'Çikolatalı pasta'));
  assert.ok(isCorrect('İSTANBUL', 'istanbul'));
  assert.ok(!isCorrect('aslan', 'Aslan Kral'));
  assert.ok(!isCorrect('', ''));
  assert.equal(normalizeGuess('Işık!'), 'isik');
  for (const [cat, words] of Object.entries(WORDS)) assert.equal(new Set(words).size, words.length, cat);
  const s = emoji.create({ players: P, host: A });
  assert.equal(s.teller, A); assert.equal(s.phase, 'compose');
});

test('Hikâye: başlangıçlar', () => {
  assert.ok(OPENINGS.length >= 10);
  const s = createStory({ players: P, host: A });
  assert.ok(OPENINGS.includes(s.opening)); assert.equal(s.turn, A);
});

test('Rastgelelik yardımcıları', () => {
  for (let i = 0; i < 200; i++) { const r = randomInt(7); assert.ok(r >= 0 && r < 7); }
  const arr = [1, 2, 3, 4, 5];
  assert.deepEqual(shuffle(arr).sort(), arr);
  assert.equal(winnerByScore({ [A]: 2, [B]: 2 }, P), 'draw');
});

test('Soru Cevap: kategori ve tekrar önleme', () => {
  const all = [{ id: 1, category: 'a' }, { id: 2, category: 'a' }, { id: 3, category: 'b' }];
  for (let i = 0; i < 20; i++) assert.equal(pickQuestion(all, 'a', [1]).id, 2);
  assert.equal(pickQuestion(all, 'b', []).id, 3);
  assert.ok([1, 2].includes(pickQuestion(all, 'a', [1, 2]).id), 'hepsi sorulduysa yeniden başlar');
  assert.ok(pickQuestion(all, 'random', [1, 2]).id === 3);
});
