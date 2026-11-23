import test from 'node:test';
import assert from 'node:assert/strict';
import { sectionOf, fmtDuration, dayKey, messageSummary } from '../../js/utils/stats-logic.js';
import { extractEmojis } from '../../js/games/emoji.js';

test('rota → bölüm', () => {
  assert.equal(sectionOf('/home'), 'home');
  assert.equal(sectionOf('/chat'), 'chat');
  assert.equal(sectionOf('/play/:id'), 'games');
  assert.equal(sectionOf('/stories'), 'games');
  assert.equal(sectionOf('/watch'), 'watch');
  assert.equal(sectionOf('/profile'), 'other');
});

test('süre biçimi', () => {
  assert.equal(fmtDuration(0), '0 dk');
  assert.equal(fmtDuration(40), '1 dk\'dan az');
  assert.equal(fmtDuration(125), '2 dk');
  assert.equal(fmtDuration(3725), '1 sa 2 dk');
  assert.equal(fmtDuration(7200), '2 sa');
  assert.equal(fmtDuration(90000), '1 gün 1 sa');
  assert.equal(dayKey(new Date(2026, 7, 2, 15)), '2026-08-02');
});

test('mesaj özeti: silinenler sayılmaz, en yoğun gün, ortalama', () => {
  const A = 'a', B = 'b';
  const d = (day, h) => new Date(2026, 8, day, h).getTime();
  const msgs = [
    { uid: A, ts: d(1, 10) }, { uid: B, ts: d(1, 11) }, { uid: B, ts: d(2, 9) },
    { uid: A, ts: d(2, 10) }, { uid: A, ts: d(2, 12), deleted: true }, { uid: B, ts: d(2, 13) }, { uid: 'x', ts: d(2, 14) },
  ];
  const s = messageSummary(msgs, [A, B], d(5, 10));
  assert.equal(s.total, 5);
  assert.deepEqual(s.per, { a: 2, b: 3 });
  assert.equal(s.first, d(1, 10));
  assert.deepEqual(s.busiest, { day: '2026-09-02', n: 3 });
  assert.equal(s.perDay, 5 / 4);
});

test('emojiyle anlat: klavyeden yazılan metinden yalnızca emojiler alınır', () => {
  assert.deepEqual(extractEmojis('🍕 pizza 🎉'), ['🍕', '🎉']);
  assert.deepEqual(extractEmojis('👩‍❤️‍👨🇹🇷1️⃣❤️'), ['👩‍❤️‍👨', '🇹🇷', '1️⃣', '❤️'], 'birleşik emojiler ve bayraklar tek parça');
  assert.deepEqual(extractEmojis('abc 123'), []);
  assert.equal(extractEmojis('😀'.repeat(20)).length, 12, 'en fazla 12');
});
