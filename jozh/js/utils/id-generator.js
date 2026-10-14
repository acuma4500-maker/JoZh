// Kayıt kimlikleri: <önek>_<uuid v4>, cihazda üretilir.

export const UUID_RE = /^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/;
export const RECORD_ID_RE = /^[a-z][a-z0-9]{0,15}_[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/;
export const IMAGE_ID_RE = /^img_[0-9a-f-]{36}$/;

export function uuidv4() {
  if (typeof crypto.randomUUID === 'function') return crypto.randomUUID();
  const b = crypto.getRandomValues(new Uint8Array(16));
  b[6] = (b[6] & 0x0f) | 0x40;
  b[8] = (b[8] & 0x3f) | 0x80;
  const h = Array.from(b, (x) => x.toString(16).padStart(2, '0')).join('');
  return `${h.slice(0, 8)}-${h.slice(8, 12)}-${h.slice(12, 16)}-${h.slice(16, 20)}-${h.slice(20)}`;
}

export function newId(prefix) {
  return `${prefix}_${uuidv4()}`;
}

// Liste maddeleri için kısa kimlik (kayıt içinde kalır).
export function shortId() {
  return uuidv4().slice(0, 8);
}

export function isRecordId(id) {
  return RECORD_ID_RE.test(id || '');
}

export function isImageId(id) {
  return IMAGE_ID_RE.test(id || '');
}
