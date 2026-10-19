// Ham IndexedDB işlemleri. Kayıt kuralları records.js'te, alan doğrulaması schemas.js'tedir.

const DB_NAME = 'jozh';

// Şema adımları. Eski adımlar asla değiştirilmez; yeni ihtiyaçta diziye adım eklenir.
// Bir adım hata verirse güncelleme işlemi tamamen iptal edilir.
const MIGRATIONS = [
  // Sürüm 1
  (db) => {
    for (const name of ['profile', 'partner', 'settings']) {
      db.createObjectStore(name, { keyPath: 'id' });
    }
    const dated = {
      memories: ['date'],
      diary: ['date'],
      dreams: ['targetDate'],
      plans: ['startDate', 'endDate'],
      notes: []
    };
    for (const [name, fields] of Object.entries(dated)) {
      const store = db.createObjectStore(name, { keyPath: 'id' });
      store.createIndex('updatedAt', 'updatedAt');
      for (const f of fields) store.createIndex(f, f);
    }
    db.createObjectStore('syncQueue', { keyPath: 'key' });
    db.createObjectStore('meta', { keyPath: 'key' });
  },
  // Sürüm 2
  (db) => {
    const images = db.createObjectStore('images', { keyPath: 'id' });
    images.createIndex('owner', 'owner');
    images.createIndex('createdAt', 'createdAt');
  },
  // Sürüm 3
  (db) => {
    db.createObjectStore('vault', { keyPath: 'id' });
    db.createObjectStore('vaultImages', { keyPath: 'id' });
    db.createObjectStore('vaultSession', { keyPath: 'id' });
  },
  // Sürüm 4: gelir ve gider kayıtları
  (db) => {
    const store = db.createObjectStore('transactions', { keyPath: 'id' });
    store.createIndex('updatedAt', 'updatedAt');
    store.createIndex('date', 'date');
  },
  // Sürüm 5: birikim hedefleri
  (db) => {
    const store = db.createObjectStore('savings', { keyPath: 'id' });
    store.createIndex('updatedAt', 'updatedAt');
  }
];

export const DB_VERSION = MIGRATIONS.length;

let dbPromise = null;
let dbInstance = null;

export function requestToPromise(request) {
  return new Promise((resolve, reject) => {
    request.onsuccess = () => resolve(request.result);
    request.onerror = () => reject(request.error);
  });
}

function txDone(tx) {
  return new Promise((resolve, reject) => {
    tx.oncomplete = () => resolve();
    tx.onabort = () => reject(tx.error || new DOMException('İşlem iptal edildi', 'AbortError'));
    tx.onerror = () => reject(tx.error);
  });
}

export function open() {
  if (dbPromise) return dbPromise;
  dbPromise = new Promise((resolve, reject) => {
    if (!('indexedDB' in window)) {
      const err = new Error('Bu tarayıcı IndexedDB desteklemiyor.');
      err.type = 'storage';
      reject(err);
      return;
    }
    const request = indexedDB.open(DB_NAME, DB_VERSION);
    request.onupgradeneeded = (event) => {
      const db = request.result;
      const tx = request.transaction;
      try {
        for (let v = event.oldVersion; v < DB_VERSION; v += 1) {
          MIGRATIONS[v](db, tx);
        }
      } catch (err) {
        tx.abort();
        throw err;
      }
    };
    request.onblocked = () => {
      window.dispatchEvent(new CustomEvent('jozh:db-blocked'));
    };
    request.onsuccess = () => {
      const db = request.result;
      db.onversionchange = () => {
        db.close();
        dbInstance = null;
        dbPromise = null;
        window.dispatchEvent(new CustomEvent('jozh:db-versionchange'));
      };
      dbInstance = db;
      resolve(db);
    };
    request.onerror = () => {
      dbPromise = null;
      reject(request.error);
    };
  });
  return dbPromise;
}

export function close() {
  if (dbInstance) dbInstance.close();
  dbInstance = null;
  dbPromise = null;
}

// fn(tx) bir IDB işlemi içinde çalışır; fn içinde IndexedDB dışı bir await kullanılmamalıdır.
export async function transaction(storeNames, mode, fn) {
  const db = await open();
  const names = Array.isArray(storeNames) ? storeNames : [storeNames];
  const tx = db.transaction(names, mode);
  const done = txDone(tx);
  let result;
  try {
    result = await fn(tx);
  } catch (err) {
    try {
      tx.abort();
    } catch {
      // işlem zaten bitmiş olabilir
    }
    await done.catch(() => {});
    throw err;
  }
  await done;
  return result;
}

export function add(store, value) {
  return transaction(store, 'readwrite', (tx) => requestToPromise(tx.objectStore(store).add(value)));
}

export function put(store, value) {
  return transaction(store, 'readwrite', (tx) => requestToPromise(tx.objectStore(store).put(value)));
}

export function get(store, key) {
  return transaction(store, 'readonly', (tx) => requestToPromise(tx.objectStore(store).get(key)));
}

export function remove(store, key) {
  return transaction(store, 'readwrite', (tx) => requestToPromise(tx.objectStore(store).delete(key)));
}

export function clear(store) {
  return transaction(store, 'readwrite', (tx) => requestToPromise(tx.objectStore(store).clear()));
}

export function count(store, query) {
  return transaction(store, 'readonly', (tx) => requestToPromise(tx.objectStore(store).count(query)));
}

// Okuma ve yazma tek işlemde. mutator(mevcut) yeni değeri döndürür (undefined = yazma).
// also(tx, yeni, eski) aynı işlemde başka depolara yazar; also.stores ile depolar bildirilir.
export function update(store, key, mutator, also) {
  const stores = [store, ...((also && also.stores) || [])];
  return transaction(stores, 'readwrite', async (tx) => {
    const os = tx.objectStore(store);
    const current = await requestToPromise(os.get(key));
    const next = mutator(current);
    if (next === undefined) return current;
    await requestToPromise(os.put(next));
    if (also && also.run) await also.run(tx, next, current);
    return next;
  });
}

export function getAll(store, { index, query, direction = 'next', limit, filter } = {}) {
  return transaction(store, 'readonly', (tx) => new Promise((resolve, reject) => {
    const os = tx.objectStore(store);
    const source = index ? os.index(index) : os;
    if (!filter && direction === 'next') {
      const req = source.getAll(query, limit);
      req.onsuccess = () => resolve(req.result);
      req.onerror = () => reject(req.error);
      return;
    }
    const out = [];
    const req = source.openCursor(query, direction);
    req.onsuccess = () => {
      const cursor = req.result;
      if (!cursor || (limit && out.length >= limit)) {
        resolve(out);
        return;
      }
      if (!filter || filter(cursor.value)) out.push(cursor.value);
      cursor.continue();
    };
    req.onerror = () => reject(req.error);
  }));
}

export function getAllKeys(store, query) {
  return transaction(store, 'readonly', (tx) => requestToPromise(tx.objectStore(store).getAllKeys(query)));
}

export async function getMeta(key) {
  const row = await get('meta', key);
  return row ? row.value : undefined;
}

export function setMeta(key, value) {
  return put('meta', { key, value });
}

export function removeMeta(key) {
  return remove('meta', key);
}

export async function getMetaByPrefix(prefix) {
  const range = IDBKeyRange.bound(prefix, `${prefix}￿`);
  return getAll('meta', { query: range });
}

export function deleteDatabase() {
  close();
  return new Promise((resolve, reject) => {
    const req = indexedDB.deleteDatabase(DB_NAME);
    req.onsuccess = () => resolve();
    req.onerror = () => reject(req.error);
    req.onblocked = () => window.dispatchEvent(new CustomEvent('jozh:db-blocked'));
  });
}

export async function getStorageInfo() {
  const info = { usage: null, quota: null, persisted: null, dbVersion: DB_VERSION };
  if (navigator.storage && navigator.storage.estimate) {
    try {
      const est = await navigator.storage.estimate();
      info.usage = est.usage ?? null;
      info.quota = est.quota ?? null;
    } catch {
      // desteklenmiyor
    }
  }
  if (navigator.storage && navigator.storage.persisted) {
    try {
      info.persisted = await navigator.storage.persisted();
    } catch {
      info.persisted = null;
    }
  }
  return info;
}

export async function requestPersistentStorage() {
  if (!navigator.storage || !navigator.storage.persist) return null;
  return navigator.storage.persist();
}

// Yazma, okuma, güncelleme ve silmenin gerçekten çalıştığını meta deposunda denetler.
export async function runSelfTest() {
  const key = `selftest:${Date.now()}`;
  const steps = [];
  const payload = { n: 42, s: 'çğıöşü', at: new Date().toISOString() };
  try {
    await setMeta(key, payload);
    steps.push('yazma');
    const read = await getMeta(key);
    if (!read || read.n !== 42 || read.s !== payload.s) throw new Error('Okunan veri yazılanla aynı değil');
    steps.push('okuma');
    await update('meta', key, (row) => ({ ...row, value: { ...row.value, n: 43 } }));
    const updated = await getMeta(key);
    if (!updated || updated.n !== 43) throw new Error('Güncelleme okunamadı');
    steps.push('güncelleme');
    await removeMeta(key);
    if ((await getMeta(key)) !== undefined) throw new Error('Silinen veri hâlâ duruyor');
    steps.push('silme');
    return { ok: true, steps };
  } catch (err) {
    await removeMeta(key).catch(() => {});
    return { ok: false, steps, error: err };
  }
}
