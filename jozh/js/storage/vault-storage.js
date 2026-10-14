// Gizli Kasa depolaması. Kasanın asıl anahtarı (DEK) rastgele 256 bittir ve içerikleri/fotoğrafları
// AES-256-GCM ile şifreler. PIN'den PBKDF2 ile türetilen kilit anahtarı (KEK) yalnızca DEK'i şifreler.
// PIN ya da PIN özeti saklanmaz; yanlış PIN, AES-GCM doğrulamasından geçemez.
import * as db from './local-db.js';
import {
  randomBytes, wipe, deriveAesKey, importAesKey, encryptBytes, decryptBytes, encryptJSON, decryptJSON,
  isWeakPin, lockoutDelayMs, FREE_ATTEMPTS, PBKDF2_ITERATIONS
} from './encryption.js';
import { processImage } from './image-storage.js';
import { newId } from '../utils/id-generator.js';
import { parseTags } from '../utils/tags.js';
import { isValidISODate } from '../utils/dates.js';
import { ValidationError } from './schemas.js';

const CONFIG_KEY = 'vault:config';
const ATTEMPTS_KEY = 'vault:attempts';
const DEK_AAD = 'jozh-vault-dek';
const SESSION_ID = 'current';
const SESSION_TOKEN_KEY = 'jozh.vaultToken';
const SESSION_MAX_AGE = 30 * 1000;
export const VAULT_TYPE_KEYS = ['note', 'thought', 'diary', 'photos', 'surprise', 'memory'];

export { isWeakPin };

export async function isConfigured() {
  const cfg = await db.getMeta(CONFIG_KEY);
  return Boolean(cfg && cfg.wrappedDek);
}

async function wrapDek(pin, rawDek) {
  const salt = randomBytes(16);
  const kek = await deriveAesKey(pin, salt, PBKDF2_ITERATIONS);
  const { iv, data } = await encryptBytes(kek, rawDek, DEK_AAD);
  return { salt, iterations: PBKDF2_ITERATIONS, iv, wrappedDek: data, lockType: 'pin4', updatedAt: new Date().toISOString() };
}

export async function setup(pin) {
  if (isWeakPin(pin)) throw new ValidationError({ pin: 'Zayıf PIN' });
  const raw = randomBytes(32);
  try {
    const cfg = await wrapDek(pin, raw);
    cfg.createdAt = cfg.updatedAt;
    await db.setMeta(CONFIG_KEY, cfg);
    await db.removeMeta(ATTEMPTS_KEY);
    return await importAesKey(raw);
  } finally {
    wipe(raw);
  }
}

export async function getAttemptState() {
  const st = (await db.getMeta(ATTEMPTS_KEY)) || { failures: 0, lockedUntil: 0 };
  return {
    failures: st.failures || 0,
    lockedUntil: st.lockedUntil && st.lockedUntil > Date.now() ? st.lockedUntil : 0,
    remainingFree: Math.max(0, FREE_ATTEMPTS - (st.failures || 0))
  };
}

// PIN ile DEK'in açık baytlarını çözer. Yanlışsa deneme sayacını artırır.
async function unwrapRaw(pin) {
  const state = await getAttemptState();
  if (state.lockedUntil) return { ok: false, lockedUntil: state.lockedUntil, remainingFree: 0 };
  const cfg = await db.getMeta(CONFIG_KEY);
  if (!cfg) return { ok: false, notConfigured: true };
  const kek = await deriveAesKey(pin, cfg.salt, cfg.iterations);
  try {
    const raw = await decryptBytes(kek, cfg.iv, cfg.wrappedDek, DEK_AAD);
    await db.removeMeta(ATTEMPTS_KEY);
    return { ok: true, raw };
  } catch {
    const failures = state.failures + 1;
    const delay = lockoutDelayMs(failures);
    const lockedUntil = delay ? Date.now() + delay : 0;
    await db.setMeta(ATTEMPTS_KEY, { failures, lockedUntil });
    return { ok: false, lockedUntil, remainingFree: Math.max(0, FREE_ATTEMPTS - failures) };
  }
}

export async function unlock(pin) {
  const res = await unwrapRaw(pin);
  if (!res.ok) return res;
  try {
    return { ok: true, key: await importAesKey(res.raw) };
  } finally {
    wipe(res.raw);
  }
}

// PIN değişince içerikler yeniden şifrelenmez; yalnızca DEK yeni KEK ile yeniden şifrelenir.
export async function changePin(oldPin, newPin) {
  if (isWeakPin(newPin)) throw new ValidationError({ pin: 'Zayıf PIN' });
  const res = await unwrapRaw(oldPin);
  if (!res.ok) return res;
  try {
    const prev = await db.getMeta(CONFIG_KEY);
    const cfg = await wrapDek(newPin, res.raw);
    cfg.createdAt = prev.createdAt;
    await db.setMeta(CONFIG_KEY, cfg);
    return { ok: true };
  } finally {
    wipe(res.raw);
  }
}

// "PIN'imi unuttum": yalnızca kasa sıfırlanır.
export async function reset() {
  await db.transaction(['vault', 'vaultImages', 'vaultSession', 'meta'], 'readwrite', async (tx) => {
    await db.requestToPromise(tx.objectStore('vault').clear());
    await db.requestToPromise(tx.objectStore('vaultImages').clear());
    await db.requestToPromise(tx.objectStore('vaultSession').clear());
    await db.requestToPromise(tx.objectStore('meta').delete(CONFIG_KEY));
    await db.requestToPromise(tx.objectStore('meta').delete(ATTEMPTS_KEY));
  });
  try {
    sessionStorage.removeItem(SESSION_TOKEN_KEY);
  } catch {
    // yok say
  }
}

// --- Oturum aktarımı: giriş ekranından kasa sayfasına en fazla 30 sn, aynı sekme ---

function randomToken() {
  return Array.from(randomBytes(16), (b) => b.toString(16).padStart(2, '0')).join('');
}

export async function handOff(key) {
  const token = randomToken();
  sessionStorage.setItem(SESSION_TOKEN_KEY, token);
  await db.put('vaultSession', { id: SESSION_ID, key, token, createdAt: Date.now() });
}

export async function takeSession() {
  let row = null;
  try {
    row = await db.get('vaultSession', SESSION_ID);
  } finally {
    await db.remove('vaultSession', SESSION_ID).catch(() => {});
  }
  let token = null;
  try {
    token = sessionStorage.getItem(SESSION_TOKEN_KEY);
    sessionStorage.removeItem(SESSION_TOKEN_KEY);
  } catch {
    token = null;
  }
  if (!row || !token || row.token !== token || Date.now() - row.createdAt > SESSION_MAX_AGE) return null;
  return row.key;
}

// --- İçerikler ---

const itemAad = (id) => `jozh-vault-item:${id}`;
const imageAad = (id, part) => `jozh-vault-image:${id}:${part}`;

export function validateItem(item) {
  const errors = {};
  const out = {
    type: VAULT_TYPE_KEYS.includes(item.type) ? item.type : 'note',
    title: String(item.title || '').replace(/\s+/g, ' ').trim(),
    date: String(item.date || '').trim(),
    body: String(item.body || '').replace(/\r\n/g, '\n').trimEnd(),
    tags: parseTags(item.tags || []),
    photoIds: [...new Set((item.photoIds || []).filter(Boolean))]
  };
  if (!out.title) errors.title = 'Başlık zorunlu.';
  else if (out.title.length > 200) errors.title = 'En çok 200 karakter olabilir.';
  if (out.date && !isValidISODate(out.date)) errors.date = 'Geçerli bir tarih seç.';
  if (out.body.length > 100000) errors.body = 'En çok 100.000 karakter olabilir.';
  if (out.tags.length > 20) errors.tags = 'En çok 20 etiket olabilir.';
  if (out.photoIds.length > 20) errors.photoIds = 'En çok 20 fotoğraf eklenebilir.';
  if (Object.keys(errors).length) throw new ValidationError(errors);
  return out;
}

export async function listItems(key) {
  const rows = await db.getAll('vault');
  const out = [];
  for (const row of rows) {
    try {
      const data = await decryptJSON(key, row.iv, row.data, itemAad(row.id));
      out.push({ ...data, id: row.id, createdAt: row.createdAt, updatedAt: row.updatedAt });
    } catch {
      out.push({ id: row.id, corrupt: true, createdAt: row.createdAt, updatedAt: row.updatedAt, title: 'Bozuk içerik', type: 'note', tags: [], photoIds: [], body: '', date: '' });
    }
  }
  return out;
}

// Saklanan kayıt yalnızca { id, iv, data, createdAt, updatedAt }; başlık, tür, metin dahil her şey şifreli.
export async function saveItem(key, item) {
  const clean = validateItem(item);
  const id = item.id || newId('vault');
  const now = new Date().toISOString();
  const existing = item.id ? await db.get('vault', id) : null;
  const { iv, data } = await encryptJSON(key, clean, itemAad(id));
  const row = { id, iv, data, createdAt: existing ? existing.createdAt : now, updatedAt: now };
  await db.put('vault', row);
  return { ...clean, id, createdAt: row.createdAt, updatedAt: now };
}

export async function deleteItem(id, photoIds = []) {
  await db.transaction(['vault', 'vaultImages'], 'readwrite', async (tx) => {
    await db.requestToPromise(tx.objectStore('vault').delete(id));
    for (const pid of photoIds) await db.requestToPromise(tx.objectStore('vaultImages').delete(pid));
  });
}

// --- Şifreli fotoğraf kaynağı (components/photos.js ile kullanılır; normal depoya hiç girmez) ---

export function createVaultSource(key) {
  const urls = new Set();
  return {
    async save(file, owner) {
      const processed = await processImage(file);
      const id = newId('img');
      const full = new Uint8Array(await processed.blob.arrayBuffer());
      const thumb = new Uint8Array(await processed.thumb.arrayBuffer());
      try {
        const encFull = await encryptBytes(key, full, imageAad(id, 'full'));
        const encThumb = await encryptBytes(key, thumb, imageAad(id, 'thumb'));
        const now = new Date().toISOString();
        await db.put('vaultImages', { id, owner, iv: encFull.iv, data: encFull.data, thumbIv: encThumb.iv, thumb: encThumb.data, createdAt: now });
        return { id };
      } finally {
        wipe(full);
        wipe(thumb);
      }
    },
    async url(id, { thumb = false } = {}) {
      const row = await db.get('vaultImages', id);
      if (!row) return null;
      const bytes = thumb
        ? await decryptBytes(key, row.thumbIv, row.thumb, imageAad(id, 'thumb'))
        : await decryptBytes(key, row.iv, row.data, imageAad(id, 'full'));
      const url = URL.createObjectURL(new Blob([bytes], { type: 'image/jpeg' }));
      wipe(bytes);
      urls.add(url);
      return url;
    },
    async remove(ids) {
      const list = (ids || []).filter(Boolean);
      if (!list.length) return;
      await db.transaction('vaultImages', 'readwrite', async (tx) => {
        for (const id of list) await db.requestToPromise(tx.objectStore('vaultImages').delete(id));
      });
    },
    async setOwner(ids, owner) {
      await db.transaction('vaultImages', 'readwrite', async (tx) => {
        const os = tx.objectStore('vaultImages');
        for (const id of ids || []) {
          const row = await db.requestToPromise(os.get(id));
          if (row && row.owner !== owner) {
            row.owner = owner;
            await db.requestToPromise(os.put(row));
          }
        }
      });
    },
    revokeAll() {
      for (const u of urls) URL.revokeObjectURL(u);
      urls.clear();
    }
  };
}

// Hiçbir kasa içeriğine bağlı olmayan, 1 saatten eski şifreli fotoğrafları siler.
export async function cleanupVaultImages(items) {
  const refs = new Set(items.flatMap((i) => i.photoIds || []));
  const cutoff = Date.now() - 60 * 60 * 1000;
  const rows = await db.getAll('vaultImages');
  const orphans = rows.filter((r) => !refs.has(r.id) && Date.parse(r.createdAt) < cutoff).map((r) => r.id);
  if (orphans.length) {
    await db.transaction('vaultImages', 'readwrite', async (tx) => {
      for (const id of orphans) await db.requestToPromise(tx.objectStore('vaultImages').delete(id));
    });
  }
  return orphans.length;
}
