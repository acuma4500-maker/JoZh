// Bizim Kutu'nun kullandığı Firebase modülleri (Storage bilinçli olarak YOK).
export { initializeApp } from 'firebase/app';
export {
  getAuth, initializeAuth, indexedDBLocalPersistence, onAuthStateChanged, signInAnonymously, signInWithEmailAndPassword, signOut,
  setPersistence, browserLocalPersistence, sendPasswordResetEmail, connectAuthEmulator
} from 'firebase/auth';
export {
  initializeFirestore, memoryLocalCache, collection, doc, addDoc, setDoc, updateDoc,
  deleteDoc, getDoc, getDocs, onSnapshot, query, where, orderBy, limit, startAfter,
  serverTimestamp, writeBatch, runTransaction, getCountFromServer, Timestamp, deleteField, connectFirestoreEmulator
} from 'firebase/firestore';
export {
  getDatabase, ref, child, push, set, update, remove, onValue, onChildAdded, onChildChanged,
  onChildRemoved, off, get, query as rtdbQuery, orderByKey, orderByChild, limitToLast, endBefore,
  equalTo, startAt, serverTimestamp as rtdbServerTimestamp, onDisconnect, runTransaction as rtdbTransaction,
  goOffline, goOnline, connectDatabaseEmulator
} from 'firebase/database';
