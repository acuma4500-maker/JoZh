// Şifreli yedek (.jozh, biçim sürümü 1).
// [8 bayt "JOZHBAK1"][4 bayt açık başlık uzunluğu (big-endian)][açık başlık JSON]
// [bloklar: 4 bayt şifreli uzunluk][12 bayt IV][AES-GCM şifreli veri]
// Blok açık hâli: [4 bayt JSON uzunluğu][JSON][isteğe bağlı ikili veri]
// Her bloğun ek verisi "jozh-backup-v1:<tuz>:<sıra>": yeri değişen, başka yedekle karışan ya da yarım kalan dosya reddedilir.
import * as db from './local-db.js';
import { DB_VERSION } from './local-db.js';
import { deriveAesKey, encryptBytes, decryptBytes, randomBytes, toBase64, fromBase64, textBytes, bytesText, wipe, PBKDF2_ITERATIONS } from './encryption.js';
import { SINGLETON_STORES, validateRecordShape } from './schemas.js';
import { RECORD_ID_RE, IMAGE_ID_RE } from '../utils/id-generator.js';
import { enqueueAll } from './records.js';
import { APP_VERSION } from '../app.js';

const MAGIC = 'JOZHBAK1';
const FORMAT = 'jozh-backup';
const FORMAT_VERSION = 1;
const RECORDS_PER_BLOCK = 200;
const RECORD_STORES = ['profile', 'partner', 'settings', 'memories', 'diary', 'dreams', 'plans', 'notes', 'transactions', 'savings'];
const META_EXACT = ['sync:key', 'vault:config', 'appLock:config'];
const META_PREFIXES = ['draft:', 'study:'];
const LEGACY_META = ['ownerUid'];
const VAULT_ID_RE = /^vault_[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/;

export class BackupError extends Error {
  constructor(message, code) {
    super(message);
    this.name = 'BackupError';
    this.code = code;
    this.userMessage = message;
  }
}

function replacer(_key, value) {
  if (value instanceof Uint8Array) return { __u8: toBase64(value) };
  if (value instanceof ArrayBuffer) return { __u8: toBase64(new Uint8Array(value)) };
  return value;
}

function reviver(_key, value) {
  if (value && typeof value === 'object' && !Array.isArray(value) && typeof value.__u8 === 'string' && Object.keys(value).length === 1) {
    return fromBase64(value.__u8);
  }
  return value;
}

const aad = (saltB64, index) => `jozh-backup-v1:${saltB64}:${index}`;

function isMetaAllowed(key) {
  return META_EXACT.includes(key) || META_PREFIXES.some((p) => key.startsWith(p));
}

// --- Oluşturma ---

class BlockWriter {
  constructor(key, saltB64) {
    this.key = key;
    this.saltB64 = saltB64;
    this.parts = [];
    this.index = 0;
  }

  async write(obj, binary) {
    const json = textBytes(JSON.stringify(obj, replacer));
    const binLen = binary ? binary.length : 0;
    const plain = new Uint8Array(4 + json.length + binLen);
    new DataView(plain.buffer).setUint32(0, json.length);
    plain.set(json, 4);
    if (binary) plain.set(binary, 4 + json.length);
    const { iv, data } = await encryptBytes(this.key, plain, aad(this.saltB64, this.index));
    wipe(plain);
    wipe(json);
    const head = new Uint8Array(16);
    new DataView(head.buffer).setUint32(0, data.length);
    head.set(iv, 4);
    this.parts.push(head, data);
    this.index += 1;
  }
}

async function blobBytes(blob) {
  return blob ? new Uint8Array(await blob.arrayBuffer()) : new Uint8Array(0);
}

function concat(a, b) {
  const out = new Uint8Array(a.length + b.length);
  out.set(a, 0);
  out.set(b, a.length);
  return out;
}

export async function createBackup(password, { includePhotos = true, onProgress } = {}) {
  const salt = randomBytes(16);
  const saltB64 = toBase64(salt);
  const key = await deriveAesKey(password, salt, PBKDF2_ITERATIONS);
  const createdAt = new Date().toISOString();

  const counts = {};
  const recordData = {};
  for (const store of [...RECORD_STORES, 'vault']) {
    recordData[store] = await db.getAll(store);
    counts[store] = recordData[store].length;
  }
  const metaRows = (await db.getAll('meta')).filter((m) => isMetaAllowed(m.key));
  counts.meta = metaRows.length;
  const imageIds = includePhotos ? await db.getAllKeys('images') : [];
  const vaultImageIds = await db.getAllKeys('vaultImages');
  counts.images = imageIds.length;
  counts.vaultImages = vaultImageIds.length;

  const totalSteps = 3 + Object.values(recordData).reduce((s, list) => s + Math.ceil(list.length / RECORDS_PER_BLOCK), 0) + imageIds.length + vaultImageIds.length;
  let done = 0;
  const step = () => {
    done += 1;
    if (onProgress) onProgress(done, totalSteps);
  };

  const header = {
    format: FORMAT,
    formatVersion: FORMAT_VERSION,
    createdAt,
    appVersion: APP_VERSION,
    kdf: { name: 'PBKDF2', hash: 'SHA-256', iterations: PBKDF2_ITERATIONS, salt: saltB64 }
  };
  const headerBytes = textBytes(JSON.stringify(header));
  const prefix = new Uint8Array(12);
  prefix.set(textBytes(MAGIC), 0);
  new DataView(prefix.buffer).setUint32(8, headerBytes.length);

  const w = new BlockWriter(key, saltB64);
  await w.write({ t: 'manifest', createdAt, appVersion: APP_VERSION, dbVersion: DB_VERSION, includesPhotos: includePhotos, counts });
  step();
  for (const [store, list] of Object.entries(recordData)) {
    for (let i = 0; i < list.length; i += RECORDS_PER_BLOCK) {
      await w.write({ t: 'records', store, items: list.slice(i, i + RECORDS_PER_BLOCK) });
      step();
    }
  }
  await w.write({ t: 'meta', entries: metaRows.map((m) => ({ key: m.key, value: m.value })) });
  step();
  // Fotoğraflar Base64'e çevrilmeden ikili veri olarak, tek tek işlenir.
  for (const id of imageIds) {
    const rec = await db.get('images', id);
    if (!rec) continue;
    const full = await blobBytes(rec.blob);
    const thumb = await blobBytes(rec.thumb);
    const { blob: _blob, thumb: _thumb, ...meta } = rec;
    await w.write({ t: 'image', record: { ...meta, blobLen: full.length, thumbLen: thumb.length } }, concat(full, thumb));
    step();
  }
  // Gizli Kasa fotoğrafları kendi şifreli hâliyle girer; yedek parolasıyla bir kez daha şifrelenir.
  for (const id of vaultImageIds) {
    const rec = await db.get('vaultImages', id);
    if (!rec) continue;
    const { data, thumb, ...meta } = rec;
    await w.write({ t: 'vaultImage', record: { ...meta, dataLen: data.length, thumbLen: thumb.length } }, concat(new Uint8Array(data), new Uint8Array(thumb)));
    step();
  }
  await w.write({ t: 'end', blocks: w.index + 1 });
  step();

  const blob = new Blob([prefix, headerBytes, ...w.parts], { type: 'application/octet-stream' });
  return { blob, createdAt, counts, fileName: `jozh-yedek-${createdAt.slice(0, 10)}.jozh` };
}

// --- Okuma ---

async function readSlice(file, start, end) {
  if (end > file.size) throw new BackupError('Yedek dosyası yarım kalmış (beklenenden kısa).', 'truncated');
  return new Uint8Array(await file.slice(start, end).arrayBuffer());
}

export async function readHeader(file) {
  if (!file || file.size < 12) throw new BackupError('Bu dosya bir JOZH yedeği değil.', 'not-backup');
  const prefix = await readSlice(file, 0, 12);
  if (bytesText(prefix.subarray(0, 8)) !== MAGIC) throw new BackupError('Bu dosya bir JOZH yedeği değil.', 'not-backup');
  const len = new DataView(prefix.buffer).getUint32(8);
  if (len <= 0 || len > 64 * 1024) throw new BackupError('Yedek dosyasının başlığı bozuk.', 'corrupt');
  let header;
  try {
    header = JSON.parse(bytesText(await readSlice(file, 12, 12 + len)));
  } catch (err) {
    if (err instanceof BackupError) throw err;
    throw new BackupError('Yedek dosyasının başlığı bozuk.', 'corrupt');
  }
  if (header.format !== FORMAT || !header.kdf || typeof header.kdf.salt !== 'string') throw new BackupError('Bu dosya bir JOZH yedeği değil.', 'not-backup');
  if (header.formatVersion > FORMAT_VERSION) throw new BackupError('Bu yedek daha yeni bir JOZH sürümüyle oluşturulmuş. Önce uygulamayı güncelle.', 'newer');
  return { header, offset: 12 + len, size: file.size, createdAt: header.createdAt };
}

// Bütün blokları sırayla çözer: onBlock(obj, binary, index)
async function readBlocks(file, password, onBlock, onProgress) {
  const { header, offset: start } = await readHeader(file);
  const saltB64 = header.kdf.salt;
  const iterations = Number(header.kdf.iterations) || PBKDF2_ITERATIONS;
  if (iterations < 100000 || iterations > 10000000) throw new BackupError('Yedek dosyasının başlığı bozuk.', 'corrupt');
  const key = await deriveAesKey(password, fromBase64(saltB64), iterations);
  let offset = start;
  let index = 0;
  let manifest = null;
  let ended = false;
  while (offset < file.size) {
    if (ended) throw new BackupError('Yedek dosyası bozuk (bitişten sonra fazladan veri var).', 'corrupt');
    const head = await readSlice(file, offset, offset + 16);
    const len = new DataView(head.buffer).getUint32(0);
    const iv = head.subarray(4, 16);
    if (len < 16 || len > 64 * 1024 * 1024) throw new BackupError('Yedek dosyası bozuk.', 'corrupt');
    const data = await readSlice(file, offset + 16, offset + 16 + len);
    let plain;
    try {
      plain = await decryptBytes(key, iv, data, aad(saltB64, index));
    } catch {
      if (index === 0) throw new BackupError('Yedek parolası yanlış ya da dosya bozuk.', 'bad-password');
      throw new BackupError('Yedek dosyası bozuk ya da değiştirilmiş.', 'corrupt');
    }
    const jsonLen = new DataView(plain.buffer, plain.byteOffset).getUint32(0);
    if (jsonLen > plain.length - 4) throw new BackupError('Yedek dosyası bozuk.', 'corrupt');
    let obj;
    try {
      obj = JSON.parse(bytesText(plain.subarray(4, 4 + jsonLen)), reviver);
    } catch {
      throw new BackupError('Yedek dosyası bozuk.', 'corrupt');
    }
    const binary = plain.subarray(4 + jsonLen);
    if (index === 0) {
      if (obj.t !== 'manifest') throw new BackupError('Yedek dosyası bozuk (içerik listesi yok).', 'corrupt');
      if (Number(obj.dbVersion) > DB_VERSION) throw new BackupError('Bu yedek daha yeni bir JOZH sürümüyle oluşturulmuş. Önce uygulamayı güncelle.', 'newer');
      manifest = obj;
    } else if (obj.t === 'end') {
      if (obj.blocks !== index + 1) throw new BackupError('Yedek dosyası eksik ya da bozuk.', 'corrupt');
      ended = true;
    }
    await onBlock(obj, binary, index);
    offset += 16 + len;
    index += 1;
    if (onProgress) onProgress(offset, file.size);
  }
  if (!ended) throw new BackupError('Yedek dosyası yarım kalmış.', 'truncated');
  return { header, manifest };
}

function emptyCounts() {
  const c = { meta: 0, images: 0, vaultImages: 0, vault: 0 };
  for (const s of RECORD_STORES) c[s] = 0;
  return c;
}

function checkRecord(store, rec) {
  if (store === 'vault') {
    return rec && VAULT_ID_RE.test(rec.id) && rec.iv instanceof Uint8Array && rec.data instanceof Uint8Array && typeof rec.createdAt === 'string';
  }
  if (!rec || typeof rec.id !== 'string') return false;
  if (SINGLETON_STORES.includes(store) ? rec.id !== 'main' : !RECORD_ID_RE.test(rec.id)) return false;
  return validateRecordShape(store, rec);
}

// Yapıyı, sürümü, izinli kayıt türlerini, kimlik biçimlerini ve içerik listesindeki sayıları denetler.
// Mevcut verilere dokunmaz.
export async function inspectBackup(file, password, onProgress) {
  const counts = emptyCounts();
  const { header, manifest } = await readBlocks(file, password, (obj, binary) => {
    switch (obj.t) {
      case 'manifest':
      case 'end':
        return;
      case 'records': {
        if (!RECORD_STORES.includes(obj.store) && obj.store !== 'vault') throw new BackupError('Yedekte tanınmayan bir kayıt türü var.', 'corrupt');
        if (!Array.isArray(obj.items)) throw new BackupError('Yedek dosyası bozuk.', 'corrupt');
        for (const rec of obj.items) {
          if (!checkRecord(obj.store, rec)) throw new BackupError('Yedekte geçersiz bir kayıt var.', 'corrupt');
        }
        counts[obj.store] += obj.items.length;
        return;
      }
      case 'meta':
        for (const e of obj.entries || []) {
          if (!isMetaAllowed(e.key) && !LEGACY_META.includes(e.key)) throw new BackupError('Yedekte tanınmayan bir ayar var.', 'corrupt');
        }
        counts.meta += (obj.entries || []).filter((e) => !LEGACY_META.includes(e.key)).length;
        return;
      case 'image': {
        const r = obj.record || {};
        if (!IMAGE_ID_RE.test(r.id) || r.blobLen + r.thumbLen !== binary.length) throw new BackupError('Yedekteki bir fotoğraf bozuk.', 'corrupt');
        counts.images += 1;
        return;
      }
      case 'vaultImage': {
        const r = obj.record || {};
        if (!IMAGE_ID_RE.test(r.id) || r.dataLen + r.thumbLen !== binary.length) throw new BackupError('Yedekteki bir kasa fotoğrafı bozuk.', 'corrupt');
        counts.vaultImages += 1;
        return;
      }
      default:
        throw new BackupError('Yedekte tanınmayan bir bölüm var.', 'corrupt');
    }
  }, onProgress);
  const expected = manifest.counts || {};
  for (const [k, v] of Object.entries(counts)) {
    if (k === 'meta') continue; // eski sürümlerin ayarları (ownerUid) sayıya dahil olabilir
    const exp = expected[k];
    if (exp !== undefined && exp !== v) throw new BackupError('Yedekteki kayıt sayıları içerik listesiyle uyuşmuyor; dosya eksik olabilir.', 'corrupt');
  }
  return { createdAt: header.createdAt, appVersion: header.appVersion, includesPhotos: Boolean(manifest.includesPhotos), counts };
}

export async function checkFreeSpace(file) {
  if (!navigator.storage || !navigator.storage.estimate) return { ok: true, unknown: true };
  try {
    const { usage = 0, quota = 0 } = await navigator.storage.estimate();
    if (!quota) return { ok: true, unknown: true };
    const free = quota - usage;
    return { ok: free > file.size * 1.5, free };
  } catch {
    return { ok: true, unknown: true };
  }
}

const CLEAR_STORES = [...RECORD_STORES, 'images', 'vault', 'vaultImages', 'vaultSession', 'syncQueue', 'meta'];

// Yerel veriler temizlenir ve yedek yazılır (açılış PIN'i ve senkronizasyon anahtarı da yedektekiyle değişir).
export async function restoreBackup(file, password, onProgress) {
  // Önce bütün dosya doğrulanır; hatalı dosyada hiçbir şeye dokunulmaz.
  await inspectBackup(file, password);
  await db.transaction(CLEAR_STORES, 'readwrite', async (tx) => {
    for (const s of CLEAR_STORES) await db.requestToPromise(tx.objectStore(s).clear());
    await db.requestToPromise(tx.objectStore('meta').put({ key: 'restore:inProgress', value: { startedAt: new Date().toISOString() } }));
  });
  let hasSyncKey = false;
  await readBlocks(file, password, async (obj, binary) => {
    if (obj.t === 'records') {
      await db.transaction(obj.store, 'readwrite', async (tx) => {
        const os = tx.objectStore(obj.store);
        for (const rec of obj.items) await db.requestToPromise(os.put(rec));
      });
    } else if (obj.t === 'meta') {
      await db.transaction('meta', 'readwrite', async (tx) => {
        for (const e of obj.entries || []) {
          if (LEGACY_META.includes(e.key)) continue; // eski ownerUid kabul edilir ama yazılmaz
          if (e.key === 'sync:key') hasSyncKey = true;
          await db.requestToPromise(tx.objectStore('meta').put({ key: e.key, value: e.value }));
        }
      });
    } else if (obj.t === 'image') {
      const r = obj.record;
      const blob = new Blob([binary.slice(0, r.blobLen)], { type: r.type || 'image/jpeg' });
      const thumb = new Blob([binary.slice(r.blobLen)], { type: 'image/jpeg' });
      const { blobLen: _bl, thumbLen: _tl, ...meta } = r;
      await db.put('images', { ...meta, blob, thumb });
    } else if (obj.t === 'vaultImage') {
      const r = obj.record;
      const { dataLen, thumbLen: _tl, ...meta } = r;
      await db.put('vaultImages', { ...meta, data: binary.slice(0, dataLen), thumb: binary.slice(dataLen) });
    }
  }, onProgress);
  if (hasSyncKey) await enqueueAll();
  await db.removeMeta('restore:inProgress');
  await db.setMeta('backup:lastRestoreAt', new Date().toISOString());
}
