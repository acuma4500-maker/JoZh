// IndexedDB anahtar deposu: kasanın dışa aktarılamaz CryptoKey nesnesini bu cihazda saklar
// (yalnızca kullanıcı "bu cihazda PIN ile hızlı aç" seçeneğini açtıysa).
const DB_NAME = 'bizim-kutu-keys';
const STORE = 'keys';

function open() {
  return new Promise((resolve, reject) => {
    const req = indexedDB.open(DB_NAME, 1);
    req.onupgradeneeded = () => req.result.createObjectStore(STORE);
    req.onsuccess = () => resolve(req.result);
    req.onerror = () => reject(req.error);
  });
}

async function tx(mode, fn) {
  const db = await open();
  return new Promise((resolve, reject) => {
    const t = db.transaction(STORE, mode);
    const store = t.objectStore(STORE);
    let result;
    Promise.resolve(fn(store)).then((r) => { result = r; });
    t.oncomplete = () => { db.close(); resolve(result); };
    t.onerror = () => { db.close(); reject(t.error); };
  });
}

export const keyGet = (k) => tx('readonly', (s) => new Promise((res) => { const r = s.get(k); r.onsuccess = () => res(r.result); r.onerror = () => res(undefined); }));
export const keySet = (k, v) => tx('readwrite', (s) => { s.put(v, k); });
export const keyDel = (k) => tx('readwrite', (s) => { s.delete(k); });
export const keyClearAll = () => tx('readwrite', (s) => { s.clear(); });
