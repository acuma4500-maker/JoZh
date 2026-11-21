// Kimlik doğrulama: Firebase Authentication (e-posta/parola).
// Yetki UID ile kontrol edilir; izinli iki UID dışındaki her hesap anında oturumdan çıkarılır
// (asıl engel Firebase güvenlik kurallarıdır — bkz. firebase/).
import { auth } from './firebase-config.js';
import { onAuthStateChanged, signInWithEmailAndPassword, signOut, sendPasswordResetEmail } from './vendor/firebase.js';
import { isAllowedUid, userName } from './constants.js';

const EMAIL_KEY = (uid) => `bk.email.${uid}`;

export function rememberedEmail(uid) { try { return localStorage.getItem(EMAIL_KEY(uid)) || ''; } catch { return ''; } }
function rememberEmail(uid, email, remember) {
  try { remember ? localStorage.setItem(EMAIL_KEY(uid), email) : localStorage.removeItem(EMAIL_KEY(uid)); } catch {}
}

// Giriş formu işlemi sürerken (doğrulama + kart kontrolü) dinleyici araya girmesin.
let loginInProgress = false;

/** cb(user | null, reason?) — yalnızca izinli kullanıcılar geçer. */
export function watchAuth(cb) {
  return onAuthStateChanged(auth, async (user) => {
    if (loginInProgress) return;
    if (user && !isAllowedUid(user.uid)) {
      await signOut(auth).catch(() => {});
      cb(null, 'not-allowed');
      return;
    }
    cb(user);
  });
}

export async function login(email, password, expectedUid, remember = true) {
  loginInProgress = true;
  try { return await doLogin(email, password, expectedUid, remember); } finally { loginInProgress = false; }
}

async function doLogin(email, password, expectedUid, remember) {
  const cred = await signInWithEmailAndPassword(auth, String(email).trim(), password);
  const uid = cred.user.uid;
  if (!isAllowedUid(uid)) {
    await signOut(auth);
    throw Object.assign(new Error('Bu hesap Bizim Kutu\'ya erişemez.'), { code: 'app/not-allowed' });
  }
  if (expectedUid && uid !== expectedUid) {
    await signOut(auth);
    throw Object.assign(new Error(`Bu hesap ${userName(uid)}'ya ait. Lütfen doğru kartı seç.`), { code: 'app/wrong-card' });
  }
  rememberEmail(uid, String(email).trim(), remember);
  return cred.user;
}

export const logoutFirebase = () => signOut(auth);

export function resetPassword(email) {
  return sendPasswordResetEmail(auth, String(email).trim());
}
