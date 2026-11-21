import test from 'node:test';
import assert from 'node:assert/strict';
import { messageStatus, unreadCount, withDaySeparators } from '../../js/utils/chat-logic.js';
import { cleanText, validateText, isISODate, isPin, LIMITS } from '../../js/utils/validation.js';
import { isAllowedUid, partnerOf, ALLOWED_UIDS } from '../../js/constants.js';

const A = 'pt0Kmbc9rqdJekFyvA1wLItUnxw1', B = 'cf6RqCRF6dPEWtSR1L9Dm2Uv4Ap1';

test('yalnızca iki UID izinli', () => {
  assert.deepEqual([...ALLOWED_UIDS].sort(), [A, B].sort());
  assert.ok(isAllowedUid(A) && isAllowedUid(B));
  assert.ok(!isAllowedUid('baskaBirUid')); assert.ok(!isAllowedUid(undefined)); assert.ok(!isAllowedUid(''));
  assert.equal(partnerOf(A), B); assert.equal(partnerOf(B), A);
});

test('mesaj durumları: gönderiliyor → iletildi → ulaştı → görüldü', () => {
  assert.equal(messageStatus({ ts: { '.sv': 'timestamp' } }, {}), 'pending');
  assert.equal(messageStatus({ ts: 100 }, {}), 'sent');
  assert.equal(messageStatus({ ts: 100 }, { deliveredAt: 100 }), 'delivered');
  assert.equal(messageStatus({ ts: 100 }, { deliveredAt: 150, readAt: 120 }), 'read');
  assert.equal(messageStatus({ ts: 200 }, { deliveredAt: 150, readAt: 120 }), 'sent');
});

test('okunmamış sayısı yalnızca partnerden gelen, okunduktan sonraki, silinmemiş mesajlar', () => {
  const msgs = [{ uid: B, ts: 10 }, { uid: A, ts: 20 }, { uid: B, ts: 30 }, { uid: B, ts: 40, deleted: true }, { uid: B, ts: 50 }];
  assert.equal(unreadCount(msgs, A, 25), 2);
  assert.equal(unreadCount(msgs, A, 0), 3);
  assert.equal(unreadCount(msgs, B, 0), 1);
});

test('tarih ayraçları', () => {
  const day = (ts) => String(Math.floor(ts / 100));
  const out = withDaySeparators([{ ts: 101 }, { ts: 150 }, { ts: 230 }], day);
  assert.deepEqual(out.map((x) => x.type), ['day', 'msg', 'msg', 'day', 'msg']);
});

test('metin temizleme ve doğrulama', () => {
  assert.equal(cleanText('  merhaba\u0000 dünya  '), 'merhaba dünya');
  assert.equal(cleanText('a\nb', 10, { multiline: false }), 'a b');
  assert.equal(cleanText('x'.repeat(50), 10).length, 10);
  assert.equal(validateText('   ', { label: 'Mesaj' }).ok, false);
  assert.equal(validateText('x'.repeat(LIMITS.message + 1), { max: LIMITS.message }).ok, false);
  assert.equal(validateText('<img src=x onerror=alert(1)>', { max: 100 }).value, '<img src=x onerror=alert(1)>', 'HTML olduğu gibi metin kalır (textContent ile basılır)');
  assert.ok(isISODate('2026-08-22')); assert.ok(!isISODate('2026-02-30')); assert.ok(!isISODate('22.08.2026'));
  assert.ok(isPin('0000')); assert.ok(!isPin('12345')); assert.ok(!isPin('12a4'));
});
