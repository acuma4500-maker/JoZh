// Firestore kural testleri (emülatör, kimliksiz bağlam).
// Çalıştırma (tests/ içinde): npm install && npm run test:rules   (Firebase CLI ve Java gerekir)
import { test, before, after, beforeEach } from 'node:test';
import { readFileSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { initializeTestEnvironment, assertSucceeds, assertFails } from '@firebase/rules-unit-testing';
import { doc, getDoc, setDoc, deleteDoc, collection, getDocs, serverTimestamp, updateDoc } from 'firebase/firestore';

const root = join(dirname(fileURLToPath(import.meta.url)), '..');
const KEY = 'abcdefghijklmnopqrstuvwxyz';
const OTHER_KEY = 'zyxwvutsrqponmlkjihgfedcba';
const UUID = '123e4567-e89b-42d3-a456-426614174000';
const NOW = '2026-10-14T11:05:00.000Z';

let env;
let db;

before(async () => {
  env = await initializeTestEnvironment({
    projectId: 'demo-jozh',
    firestore: { rules: readFileSync(join(root, 'firestore.rules'), 'utf8') }
  });
});

after(async () => {
  await env.cleanup();
});

beforeEach(async () => {
  await env.clearFirestore();
  db = env.unauthenticatedContext().firestore();
});

const base = (id) => ({ id, createdAt: NOW, updatedAt: NOW, version: 1, deleted: false, syncedAt: serverTimestamp() });
const noteId = `note_${UUID}`;
const note = (extra = {}) => ({ ...base(noteId), title: 'Başlık', body: 'Metin', tags: ['a'], pinned: false, ...extra });
const ref = (col, id, key = KEY) => doc(db, 'jozh', key, col, id);

test('geçerli anahtar yazar ve okur', async () => {
  await assertSucceeds(setDoc(ref('notes', noteId), note()));
  await assertSucceeds(getDoc(ref('notes', noteId)));
  await assertSucceeds(getDocs(collection(db, 'jozh', KEY, 'notes')));
});

test('kök belge okunamaz ve kök listelenemez', async () => {
  await assertFails(getDoc(doc(db, 'jozh', KEY)));
  await assertFails(getDocs(collection(db, 'jozh')));
});

test('geçersiz anahtar ve bilinmeyen koleksiyon reddedilir', async () => {
  await assertFails(setDoc(doc(db, 'jozh', 'KISA', 'notes', noteId), note()));
  await assertFails(setDoc(doc(db, 'jozh', `${KEY}1`, 'notes', noteId), note()));
  await assertFails(setDoc(doc(db, 'jozh', KEY, 'secrets', noteId), note()));
  await assertFails(getDocs(collection(db, 'jozh', KEY, 'vault')));
});

test('silme kapalı', async () => {
  await assertSucceeds(setDoc(ref('notes', noteId), note()));
  await assertFails(deleteDoc(ref('notes', noteId)));
});

test('syncedAt sunucu zamanı olmalı', async () => {
  await assertFails(setDoc(ref('notes', noteId), { ...note(), syncedAt: new Date() }));
  const { syncedAt, ...withoutSyncedAt } = note();
  void syncedAt;
  await assertFails(setDoc(ref('notes', noteId), withoutSyncedAt));
});

test('tanımsız alan ve kimlik uyuşmazlığı reddedilir', async () => {
  await assertFails(setDoc(ref('notes', noteId), note({ secret: 'x' })));
  await assertFails(setDoc(ref('notes', noteId), { ...note(), id: `note_${'0'.repeat(8)}-0000-4000-8000-000000000000` }));
  await assertFails(setDoc(ref('notes', 'yanlis-kimlik'), { ...note(), id: 'yanlis-kimlik' }));
  await assertFails(setDoc(ref('notes', noteId), { ...note(), createdAt: '14.10.2026' }));
});

test('createdAt güncellemede değişmez', async () => {
  await assertSucceeds(setDoc(ref('notes', noteId), note()));
  await assertFails(updateDoc(ref('notes', noteId), { createdAt: '2020-01-01T00:00:00.000Z', syncedAt: serverTimestamp() }));
  await assertSucceeds(updateDoc(ref('notes', noteId), { title: 'Yeni', syncedAt: serverTimestamp() }));
});

test('başka anahtarın verisi ayrı kalır', async () => {
  await assertSucceeds(setDoc(ref('notes', noteId), note()));
  const snap = await getDoc(ref('notes', noteId, OTHER_KEY));
  if (snap.exists()) throw new Error('Başka anahtarda veri görünmemeli');
});

test('not sınırları', async () => {
  await assertFails(setDoc(ref('notes', noteId), note({ title: 'x'.repeat(201) })));
  await assertFails(setDoc(ref('notes', noteId), note({ body: 'x'.repeat(20001) })));
  await assertFails(setDoc(ref('notes', noteId), note({ tags: Array.from({ length: 21 }, (_, i) => `t${i}`) })));
  await assertSucceeds(setDoc(ref('notes', noteId), note({ title: 'x'.repeat(200) })));
});

test('günlük sınırları', async () => {
  const id = `diary_${UUID}`;
  const d = (extra) => ({ ...base(id), title: 'Gün', date: '2026-10-14', body: '', tags: [], photoIds: [], ...extra });
  await assertSucceeds(setDoc(ref('diary', id), d({})));
  await assertFails(setDoc(ref('diary', id), d({ title: '' })));
  await assertFails(setDoc(ref('diary', id), d({ date: '14-10-2026' })));
  await assertFails(setDoc(ref('diary', id), d({ photoIds: Array.from({ length: 21 }, (_, i) => `img_${i}`) })));
});

test('plan sınırları', async () => {
  const id = `plan_${UUID}`;
  const p = (extra) => ({ ...base(id), name: 'Tatil', type: 'trip', status: 'planned', startDate: '2026-10-14', startTime: '10:00', endDate: '2026-10-16', endTime: '09:00', budget: 1500, spent: 0, checklist: [], trip: { city: 'İzmir', places: [], accommodation: '', transport: '', expenses: [] }, ...extra });
  await assertSucceeds(setDoc(ref('plans', id), p({})));
  await assertFails(setDoc(ref('plans', id), p({ type: 'uzay' })));
  await assertFails(setDoc(ref('plans', id), p({ endDate: '2026-10-13' })));
  await assertFails(setDoc(ref('plans', id), p({ endDate: '2026-10-14', endTime: '09:00' })));
  await assertFails(setDoc(ref('plans', id), p({ startTime: '25:00' })));
  await assertFails(setDoc(ref('plans', id), p({ budget: 100000001 })));
});

test('hedef, profil ve ayar sınırları', async () => {
  const id = `dream_${UUID}`;
  const dr = (extra) => ({ ...base(id), title: 'Maraton', progress: 50, status: 'inProgress', priority: 'high', ...extra });
  await assertSucceeds(setDoc(ref('dreams', id), dr({})));
  await assertFails(setDoc(ref('dreams', id), dr({ progress: 101 })));
  await assertFails(setDoc(ref('dreams', id), dr({ progress: 50.5 })));
  const pr = (extra) => ({ ...base('main'), firstName: 'Ali', bloodType: 'A Rh+', height: 180, weight: 72.5, ...extra });
  await assertSucceeds(setDoc(ref('profile', 'main'), pr({})));
  await assertFails(setDoc(ref('profile', 'main'), pr({ bloodType: 'Z' })));
  await assertFails(setDoc(ref('profile', 'main'), pr({ height: 251 })));
  await assertFails(setDoc(ref('profile', `note_${UUID}`), { ...pr({}), id: `note_${UUID}` }));
  await assertSucceeds(setDoc(ref('settings', 'main'), { ...base('main'), calendarView: 'agenda' }));
  await assertFails(setDoc(ref('settings', 'main'), { ...base('main'), calendarView: 'agenda', theme: 'dark' }));
  await assertSucceeds(setDoc(ref('profile', 'main'), pr({ photoId: `img_${UUID}` })));
  await assertFails(setDoc(ref('profile', 'main'), pr({ photoId: 'resim.jpg' })));
});

test('gelir-gider sınırları', async () => {
  const id = `txn_${UUID}`;
  const t = (extra) => ({ ...base(id), type: 'expense', amount: 250.5, category: 'Market', date: '2026-10-14', account: 'cash', note: '', ...extra });
  await assertSucceeds(setDoc(ref('transactions', id), t({})));
  await assertFails(setDoc(ref('transactions', id), t({ amount: 0 })));
  await assertFails(setDoc(ref('transactions', id), t({ type: 'transfer' })));
  await assertFails(setDoc(ref('transactions', id), t({ category: '' })));
  await assertFails(setDoc(ref('transactions', id), t({ account: 'altin' })));
});

test('birikim hedefi sınırları', async () => {
  const id = `save_${UUID}`;
  const g = (extra) => ({ ...base(id), title: 'Araba', targetAmount: 200000, targetDate: '2027-06-01', note: '', contributions: [{ id: 'a1', date: '2026-10-19', amount: 2500, note: '', txnId: '' }], ...extra });
  await assertSucceeds(setDoc(ref('savings', id), g({})));
  await assertFails(setDoc(ref('savings', id), g({ title: '' })));
  await assertFails(setDoc(ref('savings', id), g({ targetAmount: 0 })));
  await assertFails(setDoc(ref('savings', id), g({ targetDate: '01.06.2027' })));
  await assertFails(setDoc(ref('savings', id), g({ extra: 1 })));
});
