// Senkronizasyon turu: önce çek, sonra gönder. Aynı anda tek tur (sekmeler arası Web Locks).
// Yerel veri, senkronizasyon başarılı olmadan asla silinmez; silme "silindi" işaretiyle aktarılır.
import * as db from '../storage/local-db.js';
import * as records from '../storage/records.js';
import { SYNCED_STORES, validateRecordShape } from '../storage/schemas.js';
import { getKey, setKey, clearKey } from '../storage/sync-key.js';
import { fetchChanged, pushIfUnchanged } from './firestore.js';
import { classifyError, logError, logWarn } from '../utils/logger.js';

const CONFLICTS_KEY = 'sync:conflicts';
const LAST_SYNC_KEY = 'sync:lastSyncAt';
const LAST_ERROR_KEY = 'sync:lastError';
const CURSOR_PREFIX = 'sync:cursor:';
const IGNORED_FIELDS = new Set(['id', 'createdAt', 'updatedAt', 'version', 'syncedRev', 'syncedAt']);

const status = {
  enabled: false,
  online: navigator.onLine,
  running: false,
  pending: 0,
  conflicts: 0,
  failures: 0,
  lastSyncAt: null,
  lastError: null,
  nextRetryAt: 0
};

const listeners = new Set();
let started = false;
let localTimer = null;
let retryTimer = null;

function emit() {
  for (const fn of listeners) {
    try {
      fn({ ...status });
    } catch (err) {
      logError('sync.listener', err);
    }
  }
}

export function onSyncStatus(fn) {
  listeners.add(fn);
  fn({ ...status });
  return () => listeners.delete(fn);
}

export function getStatus() {
  return { ...status };
}

export function describeStatus(s) {
  if (!s.enabled) return { state: 'local', icon: 'cloudOff', text: 'Yalnızca bu cihazda' };
  if (!s.online) {
    return s.pending
      ? { state: 'offline', icon: 'cloudOff', text: `Çevrimdışı, gönderilmeyi bekliyor (${s.pending})` }
      : { state: 'offline', icon: 'cloudOff', text: 'Çevrimdışı' };
  }
  if (s.conflicts) return { state: 'conflict', icon: 'alert', text: 'Çakışma var' };
  if (s.running) return { state: 'syncing', icon: 'refresh', text: 'Senkronize ediliyor' };
  if (s.failures) return { state: 'error', icon: 'alert', text: `Senkronizasyon hatası (${s.pending})` };
  if (s.pending) return { state: 'pending', icon: 'cloud', text: `Senkronizasyon bekliyor (${s.pending})` };
  return { state: 'ok', icon: 'cloud', text: 'Senkronize edildi' };
}

async function refreshCounts() {
  try {
    status.enabled = Boolean(await getKey());
    status.pending = await records.pendingCount();
    status.conflicts = Object.keys((await db.getMeta(CONFLICTS_KEY)) || {}).length;
    status.lastSyncAt = (await db.getMeta(LAST_SYNC_KEY)) || null;
    status.lastError = (await db.getMeta(LAST_ERROR_KEY)) || null;
  } catch (err) {
    logError('sync.refreshCounts', err);
  }
  status.online = navigator.onLine;
  emit();
}

// --- İçerik karşılaştırma ---

function stable(value) {
  if (Array.isArray(value)) return `[${value.map(stable).join(',')}]`;
  if (value && typeof value === 'object') {
    return `{${Object.keys(value).sort().map((k) => `${JSON.stringify(k)}:${stable(value[k])}`).join(',')}}`;
  }
  return JSON.stringify(value ?? null);
}

export function diffFields(a, b) {
  const keys = new Set([...Object.keys(a || {}), ...Object.keys(b || {})]);
  const out = [];
  for (const k of keys) {
    if (IGNORED_FIELDS.has(k)) continue;
    if (stable(a ? a[k] : null) !== stable(b ? b[k] : null)) out.push(k);
  }
  return out;
}

function contentEqual(a, b) {
  return diffFields(a, b).length === 0;
}

// --- Çakışmalar ---

export async function getConflicts() {
  const map = (await db.getMeta(CONFLICTS_KEY)) || {};
  const out = [];
  for (const [key, c] of Object.entries(map)) {
    const local = await db.get(c.store, c.id);
    out.push({ key, ...c, local: local || null });
  }
  return out;
}

async function addConflict(store, id, remote) {
  await db.update('meta', CONFLICTS_KEY, (row) => {
    const value = { ...((row && row.value) || {}) };
    value[`${store}:${id}`] = { store, id, remote, detectedAt: new Date().toISOString() };
    return { key: CONFLICTS_KEY, value };
  });
  window.dispatchEvent(new CustomEvent('jozh:sync-conflict'));
}

async function removeConflict(key) {
  await db.update('meta', CONFLICTS_KEY, (row) => {
    const value = { ...((row && row.value) || {}) };
    delete value[key];
    return { key: CONFLICTS_KEY, value };
  });
}

// choice: 'local' (bu cihazdakini tut) | 'remote' (buluttakini al)
export async function resolveConflict(key, choice) {
  const map = (await db.getMeta(CONFLICTS_KEY)) || {};
  const c = map[key];
  if (!c) return;
  if (choice === 'remote') {
    if (c.remote) await records.putFromRemote(c.store, { ...c.remote, syncedRev: records.revOf(c.remote) }, { dropQueue: true });
  } else {
    await records.prepareKeepLocal(c.store, c.id, c.remote);
  }
  await removeConflict(key);
  await refreshCounts();
  runSync({ force: true });
}

// --- Tur ---

async function pullStore(key, store) {
  const cursorKey = `${CURSOR_PREFIX}${store}`;
  const since = (await db.getMeta(cursorKey)) || 0;
  const changes = await fetchChanged(key, store, since);
  let maxSeen = since;
  let changed = 0;
  const conflicts = ((await db.getMeta(CONFLICTS_KEY)) || {});
  for (const { record: remote, syncedAtMs } of changes) {
    maxSeen = Math.max(maxSeen, syncedAtMs);
    if (!validateRecordShape(store, remote)) {
      logWarn('sync.pull.invalid', { name: 'InvalidRemote', message: store });
      continue;
    }
    const remoteRev = records.revOf(remote);
    const local = await db.get(store, remote.id);
    const queued = await db.get('syncQueue', `${store}:${remote.id}`);
    if (!local) {
      await records.putFromRemote(store, { ...remote, syncedRev: remoteRev });
      changed += 1;
    } else if (local.syncedRev === remoteRev) {
      // zaten bu sürüm var
    } else if (!queued) {
      await records.putFromRemote(store, { ...remote, syncedRev: remoteRev });
      changed += 1;
    } else if (contentEqual(local, remote)) {
      await records.putFromRemote(store, { ...remote, syncedRev: remoteRev }, { dropQueue: true });
    } else if (!conflicts[`${store}:${remote.id}`]) {
      await addConflict(store, remote.id, remote);
    }
  }
  if (maxSeen > since) await db.setMeta(cursorKey, maxSeen);
  return changed;
}

async function pushQueue(key) {
  const queue = await db.getAll('syncQueue');
  const conflicts = (await db.getMeta(CONFLICTS_KEY)) || {};
  const failed = [];
  for (const entry of queue) {
    if (conflicts[entry.key]) continue;
    if (!SYNCED_STORES.includes(entry.store)) {
      await db.remove('syncQueue', entry.key);
      continue;
    }
    const rec = await db.get(entry.store, entry.id);
    if (!rec) {
      await db.remove('syncQueue', entry.key);
      continue;
    }
    const rev = records.revOf(rec);
    let res;
    try {
      res = await pushIfUnchanged(key, entry.store, rec, rec.syncedRev ?? null);
      if (!res.ok && !res.remote && rec.syncedRev) {
        // Bulutta hiç yok (silinmiş ya da yedekten gelme): beklenen sürüm null ile yeniden dene.
        res = await pushIfUnchanged(key, entry.store, rec, null);
      }
    } catch (err) {
      // Bir kaydın reddedilmesi (ör. kurallar güncel değil) diğerlerinin gönderilmesini durdurmaz.
      if (classifyError(err) === 'network') throw err;
      failed.push(err);
      continue;
    }
    if (res.ok) {
      await records.markSynced(entry.store, entry.id, rev);
    } else if (res.remote && contentEqual(rec, res.remote)) {
      await records.putFromRemote(entry.store, { ...res.remote, syncedRev: records.revOf(res.remote) }, { dropQueue: true });
    } else if (res.remote) {
      await addConflict(entry.store, entry.id, res.remote);
    }
    status.pending = await records.pendingCount();
    emit();
  }
  if (failed.length) throw failed[0];
}

async function doRound() {
  const key = await getKey();
  if (!key) return;
  status.running = true;
  emit();
  try {
    let changed = 0;
    for (const store of SYNCED_STORES) changed += await pullStore(key, store);
    await pushQueue(key);
    status.failures = 0;
    status.nextRetryAt = 0;
    const now = new Date().toISOString();
    await db.setMeta(LAST_SYNC_KEY, now);
    await db.removeMeta(LAST_ERROR_KEY);
    if (changed) window.dispatchEvent(new CustomEvent('jozh:remote-change', { detail: { changed } }));
  } catch (err) {
    const type = classifyError(err);
    if (type === 'network' || !navigator.onLine) {
      // Bağlantı kesintisi hata sayılmaz.
      logWarn('sync.network', err);
    } else {
      status.failures += 1;
      const delay = Math.min(30 * 60 * 1000, 5000 * 2 ** (status.failures - 1));
      status.nextRetryAt = Date.now() + delay;
      clearTimeout(retryTimer);
      retryTimer = setTimeout(() => runSync(), delay);
      logError('sync.round', err);
      await db.setMeta(LAST_ERROR_KEY, {
        at: new Date().toISOString(),
        type,
        code: String(err.code || ''),
        message: type === 'permission' ? 'Firestore kuralları erişime izin vermedi.' : 'Senkronizasyon turu tamamlanamadı.'
      }).catch(() => {});
    }
  } finally {
    status.running = false;
    await refreshCounts();
  }
}

export async function runSync({ force = false } = {}) {
  status.online = navigator.onLine;
  if (!status.enabled) {
    await refreshCounts();
    if (!status.enabled) return;
  }
  if (!navigator.onLine) {
    emit();
    return;
  }
  if (!force && status.nextRetryAt && Date.now() < status.nextRetryAt) return;
  if (navigator.locks && navigator.locks.request) {
    await navigator.locks.request('jozh-sync', { ifAvailable: true }, async (lock) => {
      if (lock) await doRound();
    });
  } else if (!status.running) {
    await doRound();
  }
}

export function startSync() {
  if (started) return;
  started = true;
  refreshCounts().then(() => {
    setTimeout(() => runSync(), 800);
  });
  window.addEventListener('jozh:local-change', () => {
    records.pendingCount().then((n) => {
      status.pending = n;
      emit();
    }).catch(() => {});
    clearTimeout(localTimer);
    localTimer = setTimeout(() => runSync(), 2000);
  });
  window.addEventListener('online', () => {
    status.online = true;
    runSync({ force: true });
  });
  window.addEventListener('offline', () => {
    status.online = false;
    emit();
  });
  document.addEventListener('visibilitychange', () => {
    if (document.visibilityState === 'visible') runSync();
  });
  setInterval(() => {
    if (document.visibilityState === 'visible') runSync();
  }, 5 * 60 * 1000);
}

// Anahtar değişince/kapanınca kuyruk, imleçler ve çakışmalar sıfırlanır; syncedRev null yapılır.
export async function resetSyncState() {
  await db.clear('syncQueue');
  const metas = await db.getMetaByPrefix('sync:');
  for (const m of metas) {
    if (m.key !== 'sync:key') await db.removeMeta(m.key);
  }
  await records.resetSyncedRevs();
  status.failures = 0;
  status.nextRetryAt = 0;
}

export async function enableSync(key) {
  await resetSyncState();
  await setKey(key);
  await records.enqueueAll();
  await refreshCounts();
  runSync({ force: true });
}

export async function disableSync() {
  await resetSyncState();
  await clearKey();
  await refreshCounts();
}

export { refreshCounts };
