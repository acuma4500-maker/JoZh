// Giriş: yalnızca 4 haneli PIN.
//
// Nasıl çalışır (kullanıcı hiçbir e-posta/parola görmez):
//  1. Cihaz Firebase'e sessizce ANONİM olarak bağlanır (her cihazın kendi gizli kimliği olur).
//  2. Girilen PIN, "pinTry/{cihazKimliği}" kaydına { pin (sayı), pinText (metin), person, n } olarak yazılır.
//     Böylece secrets/pins'te PIN sayı (ör. 123) ya da metin (ör. "0123") olarak kayıtlı olsa da eşleşir.
//  3. Firebase güvenlik kuralları bu PIN'i, yalnızca sunucunun okuyabildiği "secrets/pins"
//     kaydıyla karşılaştırır. Eşleşirse o cihaz Cuma'nın / İlayda'nın verilerine erişir,
//     eşleşmezse hiçbir veriye erişemez.
//  4. PIN'ler sitenin kaynak kodunda YOKTUR; tarayıcı doğru PIN'i hiçbir zaman bilmez.
//  5. Her deneme sayılır (n artar). Bir cihaz kimliği en fazla 10 deneme yapabilir; sonra
//     uygulama yeni bir anonim kimlik alır (Firebase yeni anonim hesap açmayı IP başına sınırlar).
import { auth, rtdb, db } from './firebase-config.js';
import { onAuthStateChanged, signInAnonymously, signOut } from './vendor/firebase.js';
import { ref, get, set } from './vendor/firebase.js';
import { doc, setDoc, getDoc } from './vendor/firebase.js';
import { ALLOWED_UIDS } from './constants.js';
import { isPin } from './utils/validation.js';

export const MAX_TRIES_PER_DEVICE_ID = 10;
const LAST_KEY = 'bk.lastPerson';

const lastPerson = () => { try { return localStorage.getItem(LAST_KEY); } catch { return null; } };
const rememberPerson = (p) => { try { localStorage.setItem(LAST_KEY, p); } catch {} };

/** Firebase oturum durumunu dinler (anonim cihaz oturumu). */
export function watchAuth(cb) {
  return onAuthStateChanged(auth, (user) => cb(user));
}

const fail = (code, message) => Object.assign(new Error(message), { code });

async function ensureDeviceId(forceNew = false) {
  if (forceNew && auth.currentUser) await signOut(auth);
  if (!auth.currentUser) {
    try { await signInAnonymously(auth); }
    catch (e) {
      if (/admin-restricted|operation-not-allowed/.test(e.code || '')) throw fail('app/anon-off', 'Firebase\'de Anonim giriş kapalı (Kurulum 1. adım).');
      throw e;
    }
  }
  return auth.currentUser.uid;
}

/** RTDB'de bu cihazın doğrulanmış olup olmadığını dener (yalnızca doğrulanmışlar okuyabilir). */
async function canRead() {
  try { await get(ref(rtdb, 'presence')); return true; } catch { return false; }
}

// ---- Hızlı giriş: PIN yazılırken bağlantılar önceden hazırlanır ----
// Giriş ekranı açılınca cihaz kimliği alınır, iki veritabanına bağlanılır ve deneme sayaçları okunur.
// Böylece 4. rakama basıldığında yalnızca PIN'in kendisi gönderilir (2 kısa istek, ikisi paralel).
let prep = null;
export function prepareLogin() {
  if (!prep) {
    prep = (async () => {
      const devId = await ensureDeviceId();
      const [rt, fs] = await Promise.all([
        get(ref(rtdb, `pinTry/${devId}`)).then((s) => s.val()).catch(() => null),
        getDoc(doc(db, 'pinTry', devId)).then((s) => (s.exists() ? s.data() : null)).catch(() => null),
      ]);
      return { devId, rt, fsN: fs?.n || 0 };
    })();
    prep.catch(() => { prep = null; });
  }
  return prep;
}

/**
 * PIN ile giriş. Döner: person (sabit kullanıcı kimliği) ya da hata fırlatır.
 * Hata kodları: app/bad-pin, app/offline, app/anon-off, app/rtdb-rules, app/firestore-rules, app/firestore-secrets
 */
export async function loginWithPin(pin) {
  if (!isPin(pin)) throw Object.assign(new Error('PIN 4 rakam olmalı.'), { code: 'app/bad-pin' });
  if (!navigator.onLine) throw Object.assign(new Error('İnternet bağlantısı yok.'), { code: 'app/offline' });
  let st;
  try { st = await prepareLogin(); } finally { prep = null; } // sayaçlar değişecek: bir sonraki giriş yeniden hazırlasın
  let { devId, rt: current, fsN } = st;
  if (auth.currentUser?.uid !== devId) { devId = await ensureDeviceId(); current = null; fsN = 0; }
  const order = [lastPerson(), ...ALLOWED_UIDS].filter((p, i, a) => p && ALLOWED_UIDS.includes(p) && a.indexOf(p) === i);
  const fsWrite = (dev, person, n) => setDoc(doc(db, 'pinTry', dev), { pin: Number(pin), pinText: pin, person, n }).then(() => true, () => false);

  for (const person of order) {
    if ((current?.n || 0) >= MAX_TRIES_PER_DEVICE_ID || fsN >= MAX_TRIES_PER_DEVICE_ID) {
      devId = await ensureDeviceId(true);
      current = null; fsN = 0;
    }
    const attempt = { pin: Number(pin), pinText: pin, person, n: (current?.n || 0) + 1 };
    // Firestore doğrulama kaydı RTDB ile AYNI ANDA yazılır (sırayla beklemek girişi yavaşlatıyordu)
    const fsDev = devId;
    const fsDone = fsWrite(fsDev, person, fsN + 1);
    try { await set(ref(rtdb, `pinTry/${devId}`), attempt); current = attempt; } // her deneme sayılır; kurallar sayaç atlamaya izin vermez
    catch {
      // Eski biçimde/takılı kalmış bir deneme kaydı olabilir: yeni cihaz kimliğiyle bir kez daha dene
      try {
        await fsDone;
        devId = await ensureDeviceId(true);
        fsN = 0;
        const fresh = { ...attempt, n: 1 };
        await set(ref(rtdb, `pinTry/${devId}`), fresh);
        current = fresh;
      } catch { throw fail('app/rtdb-rules', 'Realtime Database kuralları reddetti (Kurulum 3. adım: kuralları kontrol et).'); }
    }
    const [ok, fsOk] = await Promise.all([canRead(), fsDone]);
    if (fsOk && fsDev === devId) fsN += 1;
    if (!ok) continue;

    // Firestore tarafı: paralel yazım olmadıysa (sayaç uyuşmazlığı / kimlik değişti) sırayla yaz
    if (!fsOk || fsDev !== devId) {
      const prev = await getDoc(doc(db, 'pinTry', devId)).catch(() => null);
      let fn = ((prev?.exists() && prev.data().n) || 0) + 1;
      if (fn > MAX_TRIES_PER_DEVICE_ID) {
        // Firestore sayacı dolduysa yeni cihaz kimliğiyle baştan doğrula
        await ensureDeviceId(true);
        return loginWithPin(pin);
      }
      if (!(await fsWrite(devId, person, fn))) throw fail('app/firestore-rules', 'Firestore kuralları yüklenmemiş (Kurulum 4. adım).');
    }
    // Firestore tarafında da PIN eşleşiyor mu? (Firestore'daki secrets/pins ayrı bir kayıttır)
    try { await getDoc(doc(db, 'couples', 'main')); }
    catch (e) { throw fail('app/firestore-secrets', 'Firestore\'daki secrets/pins PIN\'i eşleşmiyor. Firestore → Data → secrets → pins değerlerini kontrol et (tırnak işareti olmamalı).'); }
    rememberPerson(person);
    return person;
  }
  throw fail('app/bad-pin', 'PIN hatalı. (Doğru PIN\'i girdiğine eminsen: secrets/pins kaydını kontrol et — Kurulum 2. adım.)');
}

/** Çıkış: cihazın doğrulamasını bozar ve anonim oturumu kapatır. */
export async function logoutDevice() {
  try { await signOut(auth); } catch {}
}
