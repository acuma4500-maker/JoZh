import test, { before, after, beforeEach } from 'node:test';
import { assertFails, assertSucceeds } from '@firebase/rules-unit-testing';
import { doc, setDoc, getDoc, getDocs, updateDoc, deleteDoc, collection, query, where, serverTimestamp, Timestamp } from 'firebase/firestore';
import { env, A, B, X, DEV, PINS, seedFirestore } from './setup.mjs';

let t;
before(async () => { t = await env(); });
after(async () => { await t.cleanup(); });
beforeEach(async () => { await t.clearFirestore(); await seedFirestore(t); });

const fs = (who) => (who ? t.authenticatedContext(DEV[who] || who).firestore() : t.unauthenticatedContext().firestore());
const p = (...s) => ['couples', 'main', ...s].join('/');
const memory = (uid, extra = {}) => ({ title: 'İlk kahve', date: '2026-08-22', description: 'Moda sahili', emoji: '☕', createdBy: uid, createdAt: serverTimestamp(), updatedBy: uid, updatedAt: serverTimestamp(), ...extra });

test('oturumsuz kullanıcı hiçbir şey okuyamaz/yazamaz', async () => {
  await assertFails(getDoc(doc(fs(), p('memories', 'm1'))));
  await assertFails(setDoc(doc(fs(), p('memories', 'm1')), memory('x')));
});

test('yanlış PIN girmiş cihaz hiçbir veriye erişemez', async () => {
  await assertFails(getDoc(doc(fs(X), p('memories', 'm1'))));
  await assertFails(setDoc(doc(fs(X), p('memories', 'm1')), memory(X)));
  await assertFails(getDocs(collection(fs(X), p('tasks'))));
  await assertFails(getDoc(doc(fs(X), 'couples/main')));
});

test('Cuma ve İlayda ortak anı ekler, ikisi de okur', async () => {
  await assertSucceeds(setDoc(doc(fs(A), p('memories', 'm1')), memory(A)));
  await assertSucceeds(getDoc(doc(fs(B), p('memories', 'm1'))));
  await assertSucceeds(updateDoc(doc(fs(B), p('memories', 'm1')), { title: 'İlk kahvemiz', updatedBy: B, updatedAt: serverTimestamp() }));
  await assertSucceeds(deleteDoc(doc(fs(B), p('memories', 'm1'))));
});

test('başka kullanıcı adına veri oluşturulamaz', async () => {
  await assertFails(setDoc(doc(fs(A), p('memories', 'm1')), memory(B)));
  await assertFails(setDoc(doc(fs(A), p('memories', 'm2')), memory(A, { createdAt: Timestamp.fromDate(new Date(2020, 1, 1)) })));
});

test('şema doğrulaması: fazla alan, uzun başlık, hatalı tarih reddedilir', async () => {
  await assertFails(setDoc(doc(fs(A), p('memories', 'm1')), memory(A, { photoUrl: 'x' })));
  await assertFails(setDoc(doc(fs(A), p('memories', 'm1')), memory(A, { title: 'x'.repeat(81) })));
  await assertFails(setDoc(doc(fs(A), p('memories', 'm1')), memory(A, { date: '22.08.2026' })));
  await assertFails(setDoc(doc(fs(A), p('memories', 'm1')), memory(A, { title: '' })));
});

test('güncellemede oluşturan bilgisi değiştirilemez', async () => {
  await setDoc(doc(fs(A), p('memories', 'm1')), memory(A));
  await assertFails(updateDoc(doc(fs(B), p('memories', 'm1')), { createdBy: B, updatedBy: B, updatedAt: serverTimestamp() }));
  await assertFails(updateDoc(doc(fs(B), p('memories', 'm1')), { title: 'x', updatedBy: A, updatedAt: serverTimestamp() }));
});

test('film: geçersiz durum/puan reddedilir', async () => {
  const base = { title: 'Amélie', kind: 'film', genre: 'Romantik', description: '', status: 'watchlist', favorite: false, rating: 0, comment: '', createdBy: A, createdAt: serverTimestamp(), updatedBy: A, updatedAt: serverTimestamp() };
  await assertSucceeds(setDoc(doc(fs(A), p('movies', 'f1')), base));
  await assertFails(setDoc(doc(fs(A), p('movies', 'f2')), { ...base, status: 'trash' }));
  await assertFails(setDoc(doc(fs(A), p('movies', 'f3')), { ...base, rating: 9 }));
  await assertSucceeds(updateDoc(doc(fs(B), p('movies', 'f1')), { status: 'watched', rating: 5, updatedBy: B, updatedAt: serverTimestamp() }));
});

test('görev: tamamlayan kişi ben olmalıyım', async () => {
  const task = { title: 'Piknik', description: '', dueDate: '2026-12-01', priority: 'high', done: false, doneBy: '', doneAt: null, createdBy: A, createdAt: serverTimestamp(), updatedBy: A, updatedAt: serverTimestamp() };
  await assertSucceeds(setDoc(doc(fs(A), p('tasks', 't1')), task));
  await assertFails(updateDoc(doc(fs(B), p('tasks', 't1')), { done: true, doneBy: A, doneAt: serverTimestamp(), updatedBy: B, updatedAt: serverTimestamp() }));
  await assertSucceeds(updateDoc(doc(fs(B), p('tasks', 't1')), { done: true, doneBy: B, doneAt: serverTimestamp(), updatedBy: B, updatedAt: serverTimestamp() }));
  await assertFails(setDoc(doc(fs(A), p('tasks', 't2')), { ...task, done: true }));
});

test('kasa: yalnızca şifreli alanlar kabul edilir', async () => {
  const note = { v: 1, iv: 'AAAAAAAAAAAAAAAA', ct: 'c2lmcmVsaQ==', createdBy: A, createdAt: serverTimestamp(), updatedBy: A, updatedAt: serverTimestamp() };
  await assertSucceeds(setDoc(doc(fs(A), p('vaultNotes', 'n1')), note));
  await assertFails(setDoc(doc(fs(A), p('vaultNotes', 'n2')), { ...note, title: 'düz metin başlık' }));
  await assertFails(setDoc(doc(fs(A), p('vaultNotes', 'n3')), { ...note, body: 'düz metin' }));
  await assertFails(getDoc(doc(fs(X), p('vaultNotes', 'n1'))));
  const cfg = { v: 1, salt: 'MDEyMzQ1Njc4OWFiY2RlZg==', iterations: 600000, check: { iv: 'AAAA', ct: 'BBBB' }, createdBy: A, createdAt: serverTimestamp(), updatedBy: A, updatedAt: serverTimestamp() };
  await assertSucceeds(setDoc(doc(fs(A), p('vault', 'config')), cfg));
  await assertFails(setDoc(doc(fs(A), p('vault', 'other')), cfg));
  await assertFails(setDoc(doc(fs(A), p('vault', 'config')), { ...cfg, pin: '1234' }, { merge: true }));
  await assertFails(deleteDoc(doc(fs(B), p('vault', 'config'))));
});

test('bildirimler: yalnızca partnere gönderilir, yalnızca alıcı okur ve okundu yapar', async () => {
  const n = (from, to) => ({ type: 'memory', to, from, title: 'Yeni anı', body: '', link: '#/memories', read: false, createdAt: serverTimestamp() });
  await assertSucceeds(setDoc(doc(fs(A), p('notifications', 'n1')), n(A, B)));
  await assertFails(setDoc(doc(fs(A), p('notifications', 'n2')), n(A, A)));
  await assertFails(setDoc(doc(fs(A), p('notifications', 'n3')), n(B, A)));
  await assertSucceeds(getDocs(query(collection(fs(B), p('notifications')), where('to', '==', B))));
  await assertFails(getDocs(query(collection(fs(A), p('notifications')), where('to', '==', B))));
  await assertFails(updateDoc(doc(fs(A), p('notifications', 'n1')), { read: true }));
  await assertSucceeds(updateDoc(doc(fs(B), p('notifications', 'n1')), { read: true }));
  await assertFails(updateDoc(doc(fs(B), p('notifications', 'n1')), { title: 'değişti' }));
});

test('soru-cevap: herkes yalnızca kendi cevabını yazar', async () => {
  const ref = (u) => doc(fs(u), p('qaAnswers', 's1-5'));
  await assertFails(setDoc(ref(A), { qid: 5, category: 'romantik', question: 'Soru?', answers: { [B]: 'sahte' }, sessionId: 's1', createdBy: A, createdAt: serverTimestamp() }));
  await assertSucceeds(setDoc(ref(A), { qid: 5, category: 'romantik', question: 'Soru?', answers: { [A]: 'benim cevabım' }, sessionId: 's1', createdBy: A, createdAt: serverTimestamp() }));
  await assertSucceeds(updateDoc(ref(B), { [`answers.${B}`]: 'onun cevabı' }));
  await assertFails(updateDoc(ref(B), { [`answers.${A}`]: 'değiştirdim' }));
  await assertFails(updateDoc(ref(B), { question: 'başka' }));
  await assertFails(setDoc(doc(fs(A), p('qaAnswers', 'x')), { qid: 999, category: 'r', question: 'S?', answers: { [A]: 'a' }, sessionId: 's', createdBy: A, createdAt: serverTimestamp() }));
});

test('profil: yalnızca kendi profilim ve izinli alanlar', async () => {
  await assertSucceeds(setDoc(doc(fs(A), p('profiles', A)), { nickname: 'Ayıcık', prefs: { theme: 'dark' }, updatedAt: serverTimestamp() }));
  await assertFails(setDoc(doc(fs(A), p('profiles', B)), { nickname: 'x', updatedAt: serverTimestamp() }));
  await assertFails(setDoc(doc(fs(A), p('profiles', A)), { nickname: 'x', role: 'admin', updatedAt: serverTimestamp() }));
  await assertFails(setDoc(doc(fs(A), p('profiles', A)), { nickname: 'x'.repeat(25), updatedAt: serverTimestamp() }));
  await assertSucceeds(getDoc(doc(fs(B), p('profiles', A))));
});

test('couples/main dışındaki yollar kapalı', async () => {
  await assertFails(setDoc(doc(fs(A), 'couples/other/memories/m1'), memory(A)));
  await assertFails(setDoc(doc(fs(A), 'anything/else'), { a: 1 }));
  await assertFails(getDoc(doc(fs(A), 'users/' + A)));
});

test('PIN kayıtları: herkes yalnızca kendi cihaz kaydını yazar, sayaç atlanamaz ve 10\'u geçemez', async () => {
  const yeni = t.authenticatedContext('yeniCihaz').firestore();
  await assertFails(setDoc(doc(yeni, 'pinTry/yeniCihaz'), { pin: Number('1111'), pinText: '1111', person: A, n: 5 }), 'ilk deneme n=1 olmalı');
  await assertSucceeds(setDoc(doc(yeni, 'pinTry/yeniCihaz'), { pin: Number('0000'), pinText: '0000', person: A, n: 1 }));
  await assertFails(getDoc(doc(yeni, p('memories', 'x'))), 'yanlış PIN → erişim yok');
  await assertFails(setDoc(doc(yeni, 'pinTry/yeniCihaz'), { pin: Number('1111'), pinText: '1111', person: A, n: 1 }), 'sayaç sıfırlanamaz');
  await assertSucceeds(setDoc(doc(yeni, 'pinTry/yeniCihaz'), { pin: Number(PINS[A]), pinText: PINS[A], person: A, n: 2 }));
  await assertSucceeds(getDoc(doc(yeni, p('memories', 'x'))), 'doğru PIN → erişim var');
  await assertFails(setDoc(doc(yeni, 'pinTry/cihazCuma'), { pin: Number('0000'), pinText: '0000', person: A, n: 2 }), 'başka cihazın kaydı');
  await assertFails(deleteDoc(doc(yeni, 'pinTry/yeniCihaz')), 'silinip sayaç sıfırlanamaz');
  await assertFails(setDoc(doc(yeni, 'pinTry/yeniCihaz'), { pin: Number('0000'), pinText: '0000', person: A, n: 11 }));
});

test('PIN\'ler (secrets) okunamaz ve yazılamaz', async () => {
  await assertFails(getDoc(doc(fs(A), 'secrets/pins')));
  await assertFails(setDoc(doc(fs(A), 'secrets/pins'), { [A]: '0000' }));
});

test('Cuma\'nın PIN\'iyle İlayda olunamaz', async () => {
  const c = t.authenticatedContext('sahte').firestore();
  await assertSucceeds(setDoc(doc(c, 'pinTry/sahte'), { pin: Number(PINS[A]), pinText: PINS[A], person: B, n: 1 }));
  await assertFails(getDoc(doc(c, p('memories', 'x'))));
});
