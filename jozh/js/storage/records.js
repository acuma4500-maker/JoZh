// Kayıt kuralları. Bütün modüller veriye yalnızca bu dosya üzerinden erişir.
// Senkronize edilen depolarda her yazma, aynı IndexedDB işleminde syncQueue'ya tek giriş ekler.
import * as db from './local-db.js';
import { applySchema, SYNCED_STORES, SINGLETON_STORES, ID_PREFIX } from './schemas.js';
import { newId } from '../utils/id-generator.js';

export const SINGLETON_ID = 'main';

// Cihaz saati geri gitse bile öncekinden büyük bir zaman damgası üretir.
export function nextTimestamp(previous) {
  const now = Date.now();
  const prev = previous ? Date.parse(previous) : 0;
  return new Date(Math.max(now, (Number.isNaN(prev) ? 0 : prev) + 1)).toISOString();
}

export function revOf(record) {
  return record ? `${record.version}@${record.updatedAt}` : null;
}

function queueAlso(store) {
  if (!SYNCED_STORES.includes(store)) return undefined;
  return {
    stores: ['syncQueue'],
    run(tx, next) {
      const key = `${store}:${next.id}`;
      return db.requestToPromise(tx.objectStore('syncQueue').put({ key, store, id: next.id, queuedAt: new Date().toISOString() }));
    }
  };
}

function emitChange(store, id, action) {
  window.dispatchEvent(new CustomEvent('jozh:local-change', { detail: { store, id, action } }));
}

export async function createRecord(store, data) {
  if (SINGLETON_STORES.includes(store)) throw new Error('Tek belgeli depoda createRecord kullanılmaz');
  const clean = applySchema(store, { ...data, id: undefined, createdAt: undefined, updatedAt: undefined, version: undefined, deleted: undefined, syncedRev: undefined });
  const now = nextTimestamp(null);
  const record = { ...clean, id: newId(ID_PREFIX[store]), createdAt: now, updatedAt: now, version: 1, deleted: false, syncedRev: null };
  const saved = await db.update(store, record.id, (existing) => {
    if (existing) throw new Error('Kimlik çakışması');
    return record;
  }, queueAlso(store));
  emitChange(store, saved.id, 'create');
  return saved;
}

// changes: değişen alanlar. Kayıt yoksa hata verir.
export async function updateRecord(store, id, changes) {
  let notFound = false;
  const saved = await db.update(store, id, (current) => {
    if (!current) {
      notFound = true;
      return undefined;
    }
    const merged = applySchema(store, { ...current, ...changes });
    return {
      ...merged,
      id: current.id,
      createdAt: current.createdAt,
      updatedAt: nextTimestamp(current.updatedAt),
      version: (current.version || 0) + 1,
      deleted: changes.deleted !== undefined ? Boolean(changes.deleted) : Boolean(current.deleted),
      syncedRev: current.syncedRev ?? null
    };
  }, queueAlso(store));
  if (notFound) {
    const err = new Error('Kayıt bulunamadı');
    err.type = 'storage';
    err.name = 'NotFoundError';
    throw err;
  }
  emitChange(store, id, 'update');
  return saved;
}

export async function saveSingleton(store, data) {
  const saved = await db.update(store, SINGLETON_ID, (current) => {
    if (!current) {
      const now = nextTimestamp(null);
      const clean = applySchema(store, data);
      return { ...clean, id: SINGLETON_ID, createdAt: now, updatedAt: now, version: 1, deleted: false, syncedRev: null };
    }
    const merged = applySchema(store, { ...current, ...data });
    return {
      ...merged,
      id: SINGLETON_ID,
      createdAt: current.createdAt,
      updatedAt: nextTimestamp(current.updatedAt),
      version: (current.version || 0) + 1,
      deleted: false,
      syncedRev: current.syncedRev ?? null
    };
  }, queueAlso(store));
  emitChange(store, SINGLETON_ID, 'update');
  return saved;
}

export async function getRecord(store, id) {
  const rec = await db.get(store, id);
  return rec || null;
}

export async function getSingleton(store) {
  const rec = await db.get(store, SINGLETON_ID);
  return rec && !rec.deleted ? rec : null;
}

export async function listRecords(store, { includeDeleted = false, index, query, direction, filter, limit } = {}) {
  const combined = includeDeleted ? filter : (r) => !r.deleted && (!filter || filter(r));
  return db.getAll(store, { index, query, direction, filter: combined, limit });
}

export function deleteRecord(store, id) {
  return updateRecord(store, id, { deleted: true });
}

export function restoreRecord(store, id) {
  return updateRecord(store, id, { deleted: false });
}

export async function countActiveRecords(store) {
  const all = await db.getAll(store);
  return all.filter((r) => !r.deleted).length;
}

// --- Senkronizasyon ve yedek için düşük seviyeli işlemler (modüller kullanmaz) ---

// Buluttan gelen kaydı kuyruğa eklemeden yazar.
export function putFromRemote(store, record, { dropQueue = false } = {}) {
  const stores = dropQueue ? [store, 'syncQueue'] : [store];
  return db.transaction(stores, 'readwrite', async (tx) => {
    await db.requestToPromise(tx.objectStore(store).put(record));
    if (dropQueue) await db.requestToPromise(tx.objectStore('syncQueue').delete(`${store}:${record.id}`));
  });
}

// Gönderilen sürüm hâlâ yerel sürümse syncedRev'i günceller ve kuyruktan çıkarır.
export function markSynced(store, id, pushedRev) {
  return db.transaction([store, 'syncQueue'], 'readwrite', async (tx) => {
    const os = tx.objectStore(store);
    const current = await db.requestToPromise(os.get(id));
    if (!current) return false;
    if (revOf(current) !== pushedRev) return false;
    current.syncedRev = pushedRev;
    await db.requestToPromise(os.put(current));
    await db.requestToPromise(tx.objectStore('syncQueue').delete(`${store}:${id}`));
    return true;
  });
}

// "Bu cihazdakini tut": yerel kaydı bulut sürümünün üstüne yazılacak hâle getirir.
export function prepareKeepLocal(store, id, remote) {
  return db.update(store, id, (current) => {
    if (!current) return undefined;
    return {
      ...current,
      // Bulutta createdAt değiştirilemez (kurallar); buluttaki değer korunur.
      createdAt: remote && remote.createdAt ? remote.createdAt : current.createdAt,
      version: Math.max(current.version || 0, (remote && remote.version) || 0) + 1,
      updatedAt: nextTimestamp(remote && remote.updatedAt > current.updatedAt ? remote.updatedAt : current.updatedAt),
      syncedRev: remote ? revOf(remote) : null
    };
  }, queueAlso(store));
}

export async function enqueueAll() {
  for (const store of SYNCED_STORES) {
    const keys = await db.getAllKeys(store);
    if (!keys.length) continue;
    await db.transaction('syncQueue', 'readwrite', async (tx) => {
      const q = tx.objectStore('syncQueue');
      for (const id of keys) {
        await db.requestToPromise(q.put({ key: `${store}:${id}`, store, id, queuedAt: new Date().toISOString() }));
      }
    });
  }
}

export async function resetSyncedRevs() {
  for (const store of SYNCED_STORES) {
    await db.transaction(store, 'readwrite', (tx) => new Promise((resolve, reject) => {
      const req = tx.objectStore(store).openCursor();
      req.onsuccess = () => {
        const cursor = req.result;
        if (!cursor) {
          resolve();
          return;
        }
        if (cursor.value.syncedRev !== null) {
          cursor.update({ ...cursor.value, syncedRev: null });
        }
        cursor.continue();
      };
      req.onerror = () => reject(req.error);
    }));
  }
}

export async function pendingCount() {
  return db.count('syncQueue');
}
