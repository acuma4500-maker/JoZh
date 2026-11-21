import test from 'node:test';
import assert from 'node:assert/strict';
import { togetherDuration, daysBetweenISO, dueLabel, lastSeenText, relativeTime, formatISODate, parseISODate } from '../../js/utils/dates.js';

const START = { year: 2026, month: 8, day: 22 };

test('başlangıç gününde 0 gün', () => {
  const d = togetherDuration(new Date(2026, 7, 22, 13, 5, 9), START);
  assert.deepEqual({ ...d }, { future: false, days: 0, hours: 13, minutes: 5, seconds: 9 });
});

test('21 Kasım 2026: 91 gün', () => {
  const d = togetherDuration(new Date(2026, 10, 21, 0, 0, 1), START);
  assert.equal(d.days, 91);
  assert.equal(d.seconds, 1);
});

test('artık yıl ve yıl geçişi', () => {
  assert.equal(togetherDuration(new Date(2028, 7, 22, 12), START).days, 731); // 2027 (365) + 2028 artık yıl, 29 Şubat dahil (366)
});

test('başlangıçtan önce geri sayım', () => {
  const d = togetherDuration(new Date(2026, 7, 21, 0, 0, 0), START);
  assert.equal(d.future, true);
  assert.equal(d.days, 1);
});

test('yaz/kış saati geçişinde gün sayısı kaymaz (TZ ile çalıştırılır)', () => {
  // TZ=Europe/Berlin ile: 25 Ekim 2026'da saatler geri alınır.
  const before = togetherDuration(new Date(2026, 9, 24, 23, 59, 59), START).days;
  const after = togetherDuration(new Date(2026, 9, 25, 0, 0, 1), START).days;
  const next = togetherDuration(new Date(2026, 9, 26, 0, 0, 1), START).days;
  assert.equal(after - before, 1);
  assert.equal(next - after, 1);
});

test('ISO tarih yardımcıları', () => {
  assert.equal(daysBetweenISO('2026-08-22', '2026-11-21'), 91);
  assert.equal(parseISODate('2026-02-30'), null);
  assert.equal(formatISODate('2026-08-22'), '22 Ağustos 2026');
  const now = new Date(2026, 10, 21, 10);
  assert.equal(dueLabel('2026-11-21', now), 'Bugün');
  assert.equal(dueLabel('2026-11-22', now), 'Yarın');
  assert.equal(dueLabel('2026-11-25', now), '4 gün kaldı');
  assert.equal(dueLabel('2026-11-19', now), '2 gün gecikti');
});

test('son görülme ve göreli zaman', () => {
  const now = new Date(2026, 10, 21, 18, 0).getTime();
  assert.equal(lastSeenText(new Date(2026, 10, 21, 14, 5).getTime(), now), 'Son görülme bugün 14:05');
  assert.equal(lastSeenText(new Date(2026, 10, 20, 9, 30).getTime(), now), 'Son görülme dün 09:30');
  assert.equal(lastSeenText(0, now), 'Henüz görülmedi');
  assert.equal(relativeTime(now - 10 * 60000, now), '10 dk önce');
});
