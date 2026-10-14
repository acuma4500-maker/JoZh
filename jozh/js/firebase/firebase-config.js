// Firebase yapılandırması (tek dosya). apiKey bir parola değildir; erişimi firestore.rules belirler.
// Yalnızca Firestore kullanılır: Authentication, Storage ve Analytics yüklenmez.

export const firebaseConfig = {
  apiKey: 'AIzaSyCuSyRpjxFe8cqtyCSJngcMZnMgklrQpJw',
  authDomain: 'jozh-pro.firebaseapp.com',
  projectId: 'jozh-pro',
  storageBucket: 'jozh-pro.firebasestorage.app',
  messagingSenderId: '69916760373',
  appId: '1:69916760373:web:125bc8c33dee13a5f2947c',
  measurementId: 'G-RQ8KHXQNQ3'
};

export const FIREBASE_SDK_VERSION = '10.12.2';

export const SDK_URLS = {
  app: `https://www.gstatic.com/firebasejs/${FIREBASE_SDK_VERSION}/firebase-app.js`,
  firestore: `https://www.gstatic.com/firebasejs/${FIREBASE_SDK_VERSION}/firebase-firestore.js`
};
