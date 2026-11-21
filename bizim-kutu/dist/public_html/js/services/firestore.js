// Cloud Firestore yardımcıları. Tüm ortak veriler couples/main altındadır.
import { db, COUPLE_ID } from '../firebase-config.js';
import {
  collection, doc, addDoc, setDoc, updateDoc, deleteDoc, getDoc, getDocs, onSnapshot,
  query, where, orderBy, limit, startAfter, serverTimestamp, getCountFromServer
} from '../vendor/firebase.js';
import { getState } from '../state.js';

export const coupleDoc = () => doc(db, 'couples', COUPLE_ID);
export const col = (name) => collection(db, 'couples', COUPLE_ID, name);
export const docRef = (name, id) => doc(db, 'couples', COUPLE_ID, name, id);

const me = () => {
  const uid = getState().uid;
  if (!uid) throw Object.assign(new Error('Oturum bulunamadı.'), { code: 'permission-denied' });
  return uid;
};

/** Yeni ortak kayıt: oluşturan + sunucu zaman damgaları otomatik eklenir. */
export function createItem(name, data) {
  const uid = me();
  return addDoc(col(name), { ...data, createdBy: uid, createdAt: serverTimestamp(), updatedBy: uid, updatedAt: serverTimestamp() });
}

export function updateItem(name, id, data) {
  return updateDoc(docRef(name, id), { ...data, updatedBy: me(), updatedAt: serverTimestamp() });
}

export const deleteItem = (name, id) => deleteDoc(docRef(name, id));

/** Snapshot dinleyicisi; dönüş değeri aboneliği kapatır. */
export function listen(q, onData, onError) {
  return onSnapshot(q, (snap) => {
    onData(snap.docs.map((d) => ({ id: d.id, ...d.data({ serverTimestamps: 'estimate' }) })), snap);
  }, (err) => { console.error('Firestore dinleyici hatası', err); onError?.(err); });
}

export async function countOf(q) {
  const snap = await getCountFromServer(q);
  return snap.data().count;
}

// Profil (kullanıcı başına, yalnızca izin verilen alanlar)
export const profileRef = (uid) => docRef('profiles', uid);
export function saveProfile(patch) {
  const uid = me();
  return setDoc(profileRef(uid), { ...patch, updatedAt: serverTimestamp() }, { merge: true });
}

export { query, where, orderBy, limit, startAfter, getDocs, getDoc, setDoc, updateDoc, deleteDoc, doc, serverTimestamp };
