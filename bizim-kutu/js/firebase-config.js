// Firebase bağlantısı ve uygulama sabitleri.
// Not: Firebase web "apiKey" bir gizli anahtar değildir; erişimi Firebase Güvenlik Kuralları korur.
// Ek önlem olarak Google Cloud Console'da bu anahtarı bizimkutu.technology alan adına kısıtlayın (README).
import { initializeApp, initializeAuth, indexedDBLocalPersistence, browserLocalPersistence, initializeFirestore, memoryLocalCache, getDatabase, connectAuthEmulator, connectFirestoreEmulator, connectDatabaseEmulator } from './vendor/firebase.js';

export const firebaseConfig = {
  apiKey: 'AIzaSyCLe803P8hfdk_ywP84wXYj_t6XxMHke3o',
  authDomain: 'jozh-love.firebaseapp.com',
  databaseURL: 'https://jozh-love-default-rtdb.firebaseio.com',
  projectId: 'jozh-love',
  storageBucket: 'jozh-love.firebasestorage.app',
  messagingSenderId: '525542061019',
  appId: '1:525542061019:web:34f820d012efaabe9c6dfe',
  measurementId: 'G-9VNBEND9GK'
};

export const app = initializeApp(firebaseConfig);
// initializeAuth: yalnızca e-posta/parola; Google açılır pencere betiği (apis.google.com) yüklenmez → katı CSP.
export const auth = initializeAuth(app, { persistence: [indexedDBLocalPersistence, browserLocalPersistence] });
// Bellek içi önbellek: oturum kapatıldığında cihazda Firestore verisi kalmaz.
export const db = initializeFirestore(app, { localCache: memoryLocalCache() });
export const rtdb = getDatabase(app);

// Yalnızca yerel testler: http://127.0.0.1:…/?emulator ile açılırsa Firebase Emülatörlerine bağlanır.
// Gerçek alan adında (bizimkutu.technology) bu blok asla çalışmaz.
export const USING_EMULATOR = ['127.0.0.1', 'localhost'].includes(location.hostname) && new URLSearchParams(location.search).has('emulator');
if (USING_EMULATOR) {
  connectAuthEmulator(auth, 'http://127.0.0.1:9099', { disableWarnings: true });
  connectFirestoreEmulator(db, '127.0.0.1', 8080);
  connectDatabaseEmulator(rtdb, '127.0.0.1', 9000);
}

export { USERS, ALLOWED_UIDS, COUPLE_ID, START_DATE, partnerOf, userName, isAllowedUid } from './constants.js';
