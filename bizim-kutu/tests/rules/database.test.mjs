import test, { before, after, beforeEach } from 'node:test';
import { assertFails, assertSucceeds } from '@firebase/rules-unit-testing';
import { ref, set, update, get, remove, serverTimestamp } from 'firebase/database';
import { env, A, B, X, DEV, PINS, seedDatabase } from './setup.mjs';

let t;
before(async () => { t = await env(); });
after(async () => { await t.cleanup(); });
beforeEach(async () => { await t.clearDatabase(); await seedDatabase(t); });

const db = (who) => (who ? t.authenticatedContext(DEV[who] || who).database() : t.unauthenticatedContext().database());
const seed = (path, val) => t.withSecurityRulesDisabled((ctx) => set(ref(ctx.database(), path), val));

test('varsayılan erişim kapalı; oturumsuz ve yanlış PIN\'li cihaz okuyamaz', async () => {
  await assertFails(get(ref(db(), 'chat/messages')));
  await assertFails(get(ref(db(X), 'chat/messages')));
  await assertFails(get(ref(db(X), 'presence')));
  await assertFails(set(ref(db(A), 'random/node'), 1));
  await assertSucceeds(get(ref(db(A), 'chat/messages')));
});

test('presence: yalnızca kendi durumunu yazar', async () => {
  await assertSucceeds(set(ref(db(A), `presence/${A}/connections/c1`), true));
  await assertSucceeds(set(ref(db(A), `presence/${A}/lastSeen`), serverTimestamp()));
  await assertFails(set(ref(db(A), `presence/${B}/connections/c1`), true));
  await assertFails(set(ref(db(X), `presence/${X}/connections/c1`), true));
  await assertFails(set(ref(db(A), `presence/${A}/online`), true));
  await assertSucceeds(get(ref(db(B), 'presence')));
});

test('typing: yalnızca kendi yazıyor bilgisini yazar', async () => {
  await assertSucceeds(set(ref(db(A), `typing/${A}`), { typing: true, ts: serverTimestamp() }));
  await assertFails(set(ref(db(B), `typing/${A}`), { typing: true, ts: serverTimestamp() }));
});

test('sohbet: gönderen doğrulanır, uzunluk ve zaman damgası denetlenir', async () => {
  await assertSucceeds(set(ref(db(A), 'chat/messages/m1'), { uid: A, text: 'Seni seviyorum', ts: serverTimestamp() }));
  await assertFails(set(ref(db(A), 'chat/messages/m2'), { uid: B, text: 'sahte', ts: serverTimestamp() }));
  await assertFails(set(ref(db(A), 'chat/messages/m3'), { uid: A, text: 'x'.repeat(2001), ts: serverTimestamp() }));
  await assertFails(set(ref(db(A), 'chat/messages/m4'), { uid: A, text: '', ts: serverTimestamp() }));
  await assertFails(set(ref(db(A), 'chat/messages/m5'), { uid: A, text: 'eski', ts: 1000 }));
  await assertFails(set(ref(db(A), 'chat/messages/m6'), { uid: A, text: 'x', ts: serverTimestamp(), html: '<b>' }));
});

test('sohbet: yalnızca gönderen kendi mesajını silebilir (silindi olarak)', async () => {
  await set(ref(db(A), 'chat/messages/m1'), { uid: A, text: 'merhaba', ts: serverTimestamp() });
  await assertFails(update(ref(db(B), 'chat/messages/m1'), { text: '', deleted: true }));
  await assertFails(update(ref(db(A), 'chat/messages/m1'), { text: 'düzenlendi', ts: 5 }));
  await assertFails(remove(ref(db(A), 'chat/messages/m1')));
  await assertSucceeds(update(ref(db(A), 'chat/messages/m1'), { text: '', deleted: true }));
});

test('görüldü bilgisi: yalnızca kendi, geriye gidemez', async () => {
  await assertSucceeds(update(ref(db(A), `chat/readReceipts/${A}`), { readAt: 2000, deliveredAt: 2000 }));
  await assertFails(update(ref(db(A), `chat/readReceipts/${A}`), { readAt: 1000 }));
  await assertFails(update(ref(db(B), `chat/readReceipts/${A}`), { readAt: 3000 }));
  await assertFails(update(ref(db(A), `chat/readReceipts/${A}`), { readAt: Date.now() + 10 * 60000 }));
});

test('oyun daveti: gönderen ben olmalıyım, yalnızca alıcı kabul eder', async () => {
  await assertSucceeds(set(ref(db(A), 'games/invitations/i1'), { from: A, to: B, game: 'xox', status: 'pending', createdAt: serverTimestamp() }));
  await assertFails(set(ref(db(A), 'games/invitations/i2'), { from: B, to: A, game: 'xox', status: 'pending', createdAt: serverTimestamp() }));
  await assertFails(set(ref(db(A), 'games/invitations/i3'), { from: A, to: A, game: 'xox', status: 'pending', createdAt: serverTimestamp() }));
  await assertFails(set(ref(db(A), 'games/invitations/i4'), { from: A, to: B, game: 'poker', status: 'pending', createdAt: serverTimestamp() }));
  await assertFails(update(ref(db(A), 'games/invitations/i1'), { status: 'accepted', respondedAt: serverTimestamp() }));
  await assertSucceeds(update(ref(db(B), 'games/invitations/i1'), { status: 'accepted', respondedAt: serverTimestamp() }));
  await assertFails(update(ref(db(B), 'games/invitations/i1'), { status: 'pending' }));
});

const board = () => Object.fromEntries(Array.from({ length: 9 }, (_, i) => [`c${i}`, '-']));
const xoxSession = () => ({ game: 'xox', players: { [A]: true, [B]: true }, host: A, status: 'active', round: 1, createdAt: serverTimestamp(), updatedAt: serverTimestamp(),
  state: { board: board(), marks: { [A]: 'X', [B]: 'O' }, turn: A, starter: A, moves: 0, winner: '', line: '', tally: { [A]: 0, [B]: 0, draw: 0 } } });

test('oyun oturumu: yalnızca iki oyuncu oluşturur/okur', async () => {
  await assertSucceeds(set(ref(db(B), 'games/sessions/s1'), xoxSession()));
  await assertFails(get(ref(db(X), 'games/sessions/s1')));
  await assertFails(set(ref(db(X), 'games/sessions/s2'), { ...xoxSession(), players: { [X]: true, [A]: true } }));
  await assertFails(set(ref(db(A), 'games/sessions/s3'), { ...xoxSession(), game: 'poker' }));
  await assertFails(remove(ref(db(A), 'games/sessions/s1')), 'aktif oyun silinemez');
});

test('XOX: sıra ve hücre geçerliliği kurallarla zorunlu', async () => {
  await seed('games/sessions/s1', { ...xoxSession(), createdAt: 1, updatedAt: 1 });
  // Sırası olmayan oyuncu hamle yapamaz
  await assertFails(update(ref(db(B), 'games/sessions/s1/state'), { 'board/c0': 'O', moves: 1, turn: A }));
  // Başkasının işaretini koyamaz
  await assertFails(update(ref(db(A), 'games/sessions/s1/state'), { 'board/c0': 'O', moves: 1, turn: B }));
  // Geçerli hamle
  await assertSucceeds(update(ref(db(A), 'games/sessions/s1/state'), { 'board/c4': 'X', moves: 1, turn: B }));
  // Aynı oyuncu art arda oynayamaz
  await assertFails(update(ref(db(A), 'games/sessions/s1/state'), { 'board/c0': 'X', moves: 2, turn: B }));
  // Dolu hücrenin üzerine yazılamaz
  await assertFails(update(ref(db(B), 'games/sessions/s1/state'), { 'board/c4': 'O', moves: 2, turn: A }));
  // Hamle sayısı atlanamaz
  await assertFails(update(ref(db(B), 'games/sessions/s1/state'), { 'board/c0': 'O', moves: 5, turn: A }));
  await assertSucceeds(update(ref(db(B), 'games/sessions/s1/state'), { 'board/c0': 'O', moves: 2, turn: A }));
  // İşaretler değiştirilemez
  await assertFails(update(ref(db(A), `games/sessions/s1/state/marks`), { [A]: 'O' }));
});

test('oyunda olma bilgisi: yalnızca kendim için', async () => {
  await seed('games/sessions/s1', { ...xoxSession(), createdAt: 1, updatedAt: 1 });
  await assertSucceeds(set(ref(db(A), `games/sessions/s1/here/${A}`), true));
  await assertFails(set(ref(db(A), `games/sessions/s1/here/${B}`), true));
});

test('skorlar yalnızca birer artar', async () => {
  await assertSucceeds(set(ref(db(A), `games/scores/xox/${A}`), 1));
  await assertSucceeds(set(ref(db(B), `games/scores/xox/${A}`), 2));
  await assertFails(set(ref(db(A), `games/scores/xox/${A}`), 10));
  await assertFails(set(ref(db(A), `games/scores/xox/${X}`), 1));
  await assertFails(set(ref(db(A), `games/scores/poker/${A}`), 1));
});

test('PIN denemeleri: sayaç her denemede 1 artar, en fazla 10, silinemez; secrets okunamaz', async () => {
  const d = t.authenticatedContext('yeni').database();
  await assertFails(set(ref(d, 'pinTry/yeni'), { pin: '0000', person: A, n: 3 }));
  await assertSucceeds(set(ref(d, 'pinTry/yeni'), { pin: '0000', person: A, n: 1 }));
  await assertFails(get(ref(d, 'chat/messages')));
  await assertFails(set(ref(d, 'pinTry/yeni'), { pin: PINS[A], person: A, n: 1 }), 'sıfırlanamaz');
  await assertFails(remove(ref(d, 'pinTry/yeni')), 'silinemez');
  await assertSucceeds(set(ref(d, 'pinTry/yeni'), { pin: PINS[A], person: A, n: 2 }));
  await assertSucceeds(get(ref(d, 'chat/messages')));
  await assertFails(set(ref(d, 'pinTry/cihazCuma'), { pin: '0000', person: A, n: 2 }), 'başka cihaz');
  await assertFails(get(ref(d, 'secrets/pins')));
  await assertFails(get(ref(d, 'pinTry/cihazCuma')));
  for (let n = 3; n <= 10; n++) await assertSucceeds(set(ref(d, 'pinTry/yeni'), { pin: '0000', person: A, n }));
  await assertFails(set(ref(d, 'pinTry/yeni'), { pin: PINS[A], person: A, n: 11 }), '10 deneme sınırı');
});

test('yanlış PIN\'li cihaz Cuma adına mesaj yazamaz', async () => {
  await assertFails(set(ref(db(X), 'chat/messages/m9'), { uid: A, text: 'sahte', ts: serverTimestamp() }));
  await assertFails(set(ref(db(X), `presence/${A}/connections/c1`), true));
});
