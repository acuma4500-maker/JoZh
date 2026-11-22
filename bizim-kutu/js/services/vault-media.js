// Özel Kasa: şifreli fotoğraf ve ses kayıtları (Firebase Storage KULLANILMAZ).
// Dosya cihazda AES-GCM ile şifrelenir ve en fazla 600 KB'lık parçalar hâlinde
// couples/main/vaultMedia/{notId}_{sıra} belgelerine yazılır (Firestore belge sınırı 1 MiB).
// Her parça not kimliği + sırasıyla bağlanır (AAD); parçalar yer değiştirilemez.
import { docRef, setDoc, getDoc, deleteDoc, serverTimestamp } from './firestore.js';
import { encryptBytes, decryptBytes } from './crypto.js';

export const CHUNK_BYTES = 600 * 1024;
export const MAX_MEDIA_BYTES = 6 * 1024 * 1024;
export const MAX_AUDIO_SECONDS = 180;

const chunkId = (noteId, i) => `${noteId}_${i}`;

/** Şifreleyip kaydeder; döner: parça sayısı. Hata olursa yazılan parçaları geri siler. */
export async function saveMedia(key, noteId, bytes, uid, onProgress) {
  if (bytes.length > MAX_MEDIA_BYTES) throw new Error('Dosya çok büyük (en fazla 6 MB).');
  const n = Math.max(1, Math.ceil(bytes.length / CHUNK_BYTES));
  const written = [];
  try {
    for (let i = 0; i < n; i++) {
      const part = bytes.subarray(i * CHUNK_BYTES, (i + 1) * CHUNK_BYTES);
      const { iv, ct } = await encryptBytes(key, part, `${noteId}/${i}`);
      await setDoc(docRef('vaultMedia', chunkId(noteId, i)), { v: 1, noteId, i, n, iv, ct, createdBy: uid, createdAt: serverTimestamp() });
      written.push(i);
      onProgress?.((i + 1) / n);
    }
  } catch (e) {
    await Promise.allSettled(written.map((i) => deleteDoc(docRef('vaultMedia', chunkId(noteId, i)))));
    throw e;
  }
  return n;
}

/** Parçaları okuyup çözer, birleştirir. */
export async function loadMedia(key, noteId, n) {
  const parts = await Promise.all(Array.from({ length: n }, async (_, i) => {
    const snap = await getDoc(docRef('vaultMedia', chunkId(noteId, i)));
    if (!snap.exists()) throw new Error('Dosyanın bir parçası eksik.');
    return decryptBytes(key, snap.data(), `${noteId}/${i}`);
  }));
  const total = parts.reduce((s, p) => s + p.length, 0);
  const out = new Uint8Array(total);
  let o = 0;
  for (const p of parts) { out.set(p, o); o += p.length; }
  return out;
}

export async function deleteMedia(noteId, n) {
  await Promise.allSettled(Array.from({ length: n }, (_, i) => deleteDoc(docRef('vaultMedia', chunkId(noteId, i)))));
}

/** Fotoğrafı küçültüp JPEG'e çevirir (iPhone HEIC dahil; yön bilgisi korunur). */
export async function compressImage(file, maxSide = 1600, quality = 0.82) {
  let src;
  try { src = await createImageBitmap(file, { imageOrientation: 'from-image' }); }
  catch {
    src = await new Promise((resolve, reject) => {
      const url = URL.createObjectURL(file);
      const img = new Image();
      img.onload = () => { URL.revokeObjectURL(url); resolve(img); };
      img.onerror = () => { URL.revokeObjectURL(url); reject(new Error('Fotoğraf açılamadı.')); };
      img.src = url;
    });
  }
  const w0 = src.width, h0 = src.height;
  const scale = Math.min(1, maxSide / Math.max(w0, h0));
  const w = Math.round(w0 * scale), h = Math.round(h0 * scale);
  const canvas = document.createElement('canvas');
  canvas.width = w; canvas.height = h;
  const ctx = canvas.getContext('2d');
  ctx.fillStyle = '#ffffff'; // saydam alanlar JPEG'de siyah çıkmasın
  ctx.fillRect(0, 0, w, h);
  ctx.drawImage(src, 0, 0, w, h);
  src.close?.();
  const blob = await new Promise((r) => canvas.toBlob(r, 'image/jpeg', quality));
  if (!blob) throw new Error('Fotoğraf işlenemedi.');
  return { bytes: new Uint8Array(await blob.arrayBuffer()), mime: 'image/jpeg', w, h };
}

/** Ses kaydedici. start() → stop() → { bytes, mime, seconds } */
export function createRecorder() {
  const mime = ['audio/mp4', 'audio/webm;codecs=opus', 'audio/webm', 'audio/ogg;codecs=opus']
    .find((m) => typeof MediaRecorder !== 'undefined' && MediaRecorder.isTypeSupported?.(m)) || '';
  let stream = null, rec = null, chunks = [], startedAt = 0;
  return {
    supported: typeof MediaRecorder !== 'undefined' && !!navigator.mediaDevices?.getUserMedia,
    async start() {
      stream = await navigator.mediaDevices.getUserMedia({ audio: { echoCancellation: true, noiseSuppression: true } });
      rec = new MediaRecorder(stream, mime ? { mimeType: mime, audioBitsPerSecond: 48000 } : undefined);
      chunks = [];
      rec.ondataavailable = (e) => { if (e.data?.size) chunks.push(e.data); };
      rec.start(1000);
      startedAt = Date.now();
    },
    elapsed: () => (startedAt ? (Date.now() - startedAt) / 1000 : 0),
    stop() {
      return new Promise((resolve) => {
        if (!rec || rec.state === 'inactive') { resolve(null); return; }
        rec.onstop = async () => {
          stream?.getTracks().forEach((t) => t.stop());
          const blob = new Blob(chunks, { type: rec.mimeType || mime || 'audio/webm' });
          resolve({ bytes: new Uint8Array(await blob.arrayBuffer()), mime: blob.type, seconds: Math.round((Date.now() - startedAt) / 1000) });
        };
        rec.stop();
      });
    },
    cancel() { try { rec?.stop(); } catch {} stream?.getTracks().forEach((t) => t.stop()); },
  };
}
