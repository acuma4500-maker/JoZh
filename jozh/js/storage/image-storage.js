// Fotoğraflar images deposunda Blob olarak saklanır (Base64 ve localStorage yasak) ve buluta gönderilmez.
// Yeniden kodlama EXIF/GPS bilgisini siler; saydam alanlar beyaz olur.
import * as db from './local-db.js';
import { newId } from '../utils/id-generator.js';
import { logError, logInfo } from '../utils/logger.js';

export const MAX_FILE_BYTES = 30 * 1024 * 1024;
const FULL_EDGE = 2048;
const THUMB_EDGE = 400;
const ACCEPTED_TYPES = ['image/jpeg', 'image/png', 'image/webp', 'image/gif', 'image/heic', 'image/heif'];
const ACCEPTED_EXT = /\.(jpe?g|png|webp|gif|heic|heif)$/i;
export const ACCEPT_ATTR = 'image/jpeg,image/png,image/webp,image/gif,image/heic,image/heif,.heic,.heif';
const WEEK_MS = 7 * 24 * 60 * 60 * 1000;

function imageError(message) {
  const err = new Error(message);
  err.type = 'validation';
  err.userMessage = message;
  return err;
}

async function decode(file) {
  if (typeof createImageBitmap === 'function') {
    try {
      return await createImageBitmap(file, { imageOrientation: 'from-image' });
    } catch {
      // <img> ile dene
    }
  }
  const url = URL.createObjectURL(file);
  try {
    const img = new Image();
    img.decoding = 'async';
    img.src = url;
    await img.decode();
    return img;
  } finally {
    URL.revokeObjectURL(url);
  }
}

function sourceSize(src) {
  return { w: src.naturalWidth || src.width, h: src.naturalHeight || src.height };
}

function render(src, maxEdge, quality) {
  const { w, h } = sourceSize(src);
  const scale = Math.min(1, maxEdge / Math.max(w, h));
  const cw = Math.max(1, Math.round(w * scale));
  const ch = Math.max(1, Math.round(h * scale));
  const canvas = document.createElement('canvas');
  canvas.width = cw;
  canvas.height = ch;
  const ctx = canvas.getContext('2d');
  ctx.fillStyle = '#ffffff';
  ctx.fillRect(0, 0, cw, ch);
  ctx.imageSmoothingQuality = 'high';
  ctx.drawImage(src, 0, 0, cw, ch);
  return new Promise((resolve, reject) => {
    canvas.toBlob((blob) => {
      canvas.width = 0;
      canvas.height = 0;
      if (blob) resolve({ blob, width: cw, height: ch });
      else reject(imageError('Fotoğraf işlenemedi.'));
    }, 'image/jpeg', quality);
  });
}

// Dosyayı doğrular, küçültür ve yönünü düzeltir: { blob, thumb, width, height, type, size }
export async function processImage(file) {
  if (!file) throw imageError('Dosya seçilmedi.');
  const typeOk = ACCEPTED_TYPES.includes((file.type || '').toLowerCase()) || (!file.type && ACCEPTED_EXT.test(file.name || ''));
  if (!typeOk) throw imageError(`"${file.name || 'Dosya'}" bir fotoğraf değil. JPEG, PNG, WebP, GIF ya da HEIC seç.`);
  if (file.size > MAX_FILE_BYTES) throw imageError(`"${file.name || 'Dosya'}" çok büyük (en fazla 30 MB).`);
  if (file.size === 0) throw imageError(`"${file.name || 'Dosya'}" boş.`);
  let src;
  try {
    src = await decode(file);
  } catch {
    const heic = /heic|heif/i.test(file.type || file.name || '');
    throw imageError(heic
      ? 'Bu HEIC fotoğrafı bu tarayıcıda açılamadı. iPhone\'da Safari ile dene ya da JPEG olarak paylaş.'
      : `"${file.name || 'Dosya'}" açılamadı. Dosya bozuk ya da desteklenmeyen bir fotoğraf olabilir.`);
  }
  try {
    const full = await render(src, FULL_EDGE, 0.85);
    const thumb = await render(src, THUMB_EDGE, 0.75);
    return { blob: full.blob, thumb: thumb.blob, width: full.width, height: full.height, type: 'image/jpeg', size: full.blob.size };
  } finally {
    if (src && typeof src.close === 'function') src.close();
  }
}

export async function saveImage(file, owner, caption = '') {
  const processed = await processImage(file);
  const now = new Date().toISOString();
  const record = {
    id: newId('img'),
    owner,
    blob: processed.blob,
    thumb: processed.thumb,
    type: processed.type,
    width: processed.width,
    height: processed.height,
    size: processed.size,
    caption,
    createdAt: now,
    updatedAt: now
  };
  await db.put('images', record);
  return record;
}

export function getImage(id) {
  return db.get('images', id);
}

export async function getImageUrl(id, { thumb = false } = {}) {
  const rec = await db.get('images', id);
  if (!rec) return null;
  return URL.createObjectURL(thumb ? rec.thumb : rec.blob);
}

export async function deleteImages(ids) {
  const list = (ids || []).filter(Boolean);
  if (!list.length) return;
  await db.transaction('images', 'readwrite', async (tx) => {
    const os = tx.objectStore('images');
    for (const id of list) await db.requestToPromise(os.delete(id));
  });
}

export async function setOwner(ids, owner) {
  const list = (ids || []).filter(Boolean);
  if (!list.length) return;
  await db.transaction('images', 'readwrite', async (tx) => {
    const os = tx.objectStore('images');
    for (const id of list) {
      const rec = await db.requestToPromise(os.get(id));
      if (rec && rec.owner !== owner) {
        rec.owner = owner;
        rec.updatedAt = new Date().toISOString();
        await db.requestToPromise(os.put(rec));
      }
    }
  });
}

export async function updateCaption(id, caption) {
  return db.update('images', id, (rec) => (rec ? { ...rec, caption: String(caption || '').slice(0, 300), updatedAt: new Date().toISOString() } : undefined));
}

export function listByOwner(owner) {
  return db.getAll('images', { index: 'owner', query: owner });
}

export async function stats() {
  const all = await db.getAll('images');
  let bytes = 0;
  for (const r of all) bytes += (r.blob ? r.blob.size : 0) + (r.thumb ? r.thumb.size : 0);
  return { count: all.length, bytes };
}

// Varsayılan fotoğraf kaynağı (components/photos.js). Gizli Kasa kendi şifreli kaynağını verir.
export const defaultSource = {
  save: (file, owner) => saveImage(file, owner),
  url: (id, opts) => getImageUrl(id, opts),
  remove: (ids) => deleteImages(ids),
  setOwner: (ids, owner) => setOwner(ids, owner),
  exists: async (id) => Boolean(await db.get('images', id))
};

// Hiçbir kayda (silinmiş ama geri alınabilir kayıtlar ve taslaklar dahil) bağlı olmayan fotoğraflar.
async function referencedIds() {
  const refs = new Set();
  const addAll = (arr) => (arr || []).forEach((id) => id && refs.add(id));
  for (const r of await db.getAll('profile')) if (r.photoId) refs.add(r.photoId);
  for (const r of await db.getAll('partner')) if (r.photoId) refs.add(r.photoId);
  for (const r of await db.getAll('dreams')) if (r.photoId) refs.add(r.photoId);
  for (const r of await db.getAll('diary')) addAll(r.photoIds);
  for (const r of await db.getAll('memories')) addAll(r.photoIds);
  for (const m of await db.getMetaByPrefix('draft:')) addAll(m.value && m.value.photoIds);
  return refs;
}

export async function cleanupOrphans(minAgeMs) {
  const refs = await referencedIds();
  const cutoff = Date.now() - minAgeMs;
  const all = await db.getAll('images');
  const orphans = all.filter((r) => r.owner !== 'gallery' && !refs.has(r.id) && Date.parse(r.createdAt) < cutoff);
  await deleteImages(orphans.map((r) => r.id));
  let bytes = 0;
  for (const r of orphans) bytes += (r.blob ? r.blob.size : 0) + (r.thumb ? r.thumb.size : 0);
  return { count: orphans.length, bytes };
}

export function scheduleWeeklyCleanup() {
  setTimeout(async () => {
    try {
      const last = (await db.getMeta('images:lastCleanup')) || 0;
      if (Date.now() - last < WEEK_MS) return;
      const res = await cleanupOrphans(24 * 60 * 60 * 1000);
      await db.setMeta('images:lastCleanup', Date.now());
      if (res.count) logInfo('images.cleanup', `${res.count} fotoğraf silindi`);
    } catch (err) {
      logError('images.cleanup', err);
    }
  }, 5000);
}
