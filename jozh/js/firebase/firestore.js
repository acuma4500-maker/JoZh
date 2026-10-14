// Firestore'un tek erişim noktası. SDK, çevrimdışıyken sayfa kırılmasın diye dinamik import() ile yüklenir.
// Firestore'un kendi çevrimdışı önbelleği açılmaz (varsayılan bellek önbelleği).
import { firebaseConfig, SDK_URLS } from './firebase-config.js';

const META_FIELDS = new Set(['syncedAt', 'syncedRev']);
const PAGE_SIZE = 300;
let sdkPromise = null;

export function loadSdk() {
  if (!sdkPromise) {
    sdkPromise = Promise.all([import(SDK_URLS.app), import(SDK_URLS.firestore)])
      .then(([appMod, fs]) => {
        const app = appMod.getApps().length ? appMod.getApp() : appMod.initializeApp(firebaseConfig);
        return { fs, db: fs.getFirestore(app) };
      })
      .catch((err) => {
        sdkPromise = null;
        const e = new Error('Firebase SDK yüklenemedi');
        e.type = 'network';
        e.cause = err;
        throw e;
      });
  }
  return sdkPromise;
}

function revOf(record) {
  return record ? `${record.version}@${record.updatedAt}` : null;
}

// Buluttan gelen belgeyi yerel kayıt biçimine çevirir.
export function fromRemote(data) {
  const out = {};
  for (const [k, v] of Object.entries(data || {})) {
    if (!META_FIELDS.has(k)) out[k] = v;
  }
  return out;
}

function toRemote(record, serverTimestamp) {
  const out = {};
  for (const [k, v] of Object.entries(record)) {
    if (META_FIELDS.has(k) || v === undefined) continue;
    out[k] = v;
  }
  out.syncedAt = serverTimestamp();
  return out;
}

// Son görülen sunucu zamanından sonra değişen belgeler: [{ record, syncedAtMs }]
export async function fetchChanged(key, store, sinceMs) {
  const { fs, db } = await loadSdk();
  const col = fs.collection(db, 'jozh', key, store);
  const out = [];
  let cursor = fs.Timestamp.fromMillis(sinceMs || 0);
  for (;;) {
    const q = fs.query(col, fs.where('syncedAt', '>', cursor), fs.orderBy('syncedAt'), fs.limit(PAGE_SIZE));
    const snap = await fs.getDocs(q);
    for (const d of snap.docs) {
      const data = d.data();
      out.push({ record: fromRemote(data), syncedAtMs: data.syncedAt ? data.syncedAt.toMillis() : 0 });
    }
    if (snap.docs.length < PAGE_SIZE) break;
    cursor = snap.docs[snap.docs.length - 1].data().syncedAt;
  }
  return out;
}

// Buluttaki sürüm beklenen sürümse yazar; değilse { ok:false, remote } döner.
export async function pushIfUnchanged(key, store, record, expectedRev) {
  const { fs, db } = await loadSdk();
  const ref = fs.doc(db, 'jozh', key, store, record.id);
  return fs.runTransaction(db, async (tx) => {
    const snap = await tx.get(ref);
    const remote = snap.exists() ? fromRemote(snap.data()) : null;
    const currentRev = remote ? revOf(remote) : null;
    if (currentRev !== expectedRev) return { ok: false, remote };
    tx.set(ref, toRemote(record, fs.serverTimestamp));
    return { ok: true };
  });
}

export async function fetchOne(key, store, id) {
  const { fs, db } = await loadSdk();
  const snap = await fs.getDoc(fs.doc(db, 'jozh', key, store, id));
  return snap.exists() ? fromRemote(snap.data()) : null;
}

// Firestore'a gerçekten okuma yapar.
export async function testConnection(key) {
  const started = performance.now();
  try {
    await fetchOne(key || 'aaaaaaaaaaaaaaaaaaaaaaaaaa', 'settings', 'main');
    return { ok: true, ms: Math.round(performance.now() - started) };
  } catch (err) {
    const code = String((err && err.code) || (err && err.cause && err.cause.code) || '');
    let message = 'Firestore\'a ulaşılamadı. İnternet bağlantını kontrol et.';
    if (code.includes('permission-denied')) message = 'Bağlantı var ama Firestore kuralları erişime izin vermedi: kurallar yayınlanmamış olabilir (README → Firestore kuralları).';
    else if (err && err.message === 'Firebase SDK yüklenemedi') message = 'Firebase SDK indirilemedi. İnternet bağlantını kontrol et.';
    else if (code.includes('not-found') || code.includes('failed-precondition')) message = 'Firestore veritabanı bu projede oluşturulmamış görünüyor (README → Firestore\'u oluştur).';
    return { ok: false, code, message };
  }
}
