// Yalnızca bağlam + hata adı/kodu/kısa mesajı kaydeder. Kullanıcı verisi asla loglanmaz.

const MAX_ENTRIES = 200;
const entries = [];
const DEBUG = ['localhost', '127.0.0.1'].includes(location.hostname);

export const ERROR_TYPES = {
  network: 'ağ',
  permission: 'yetki',
  validation: 'doğrulama',
  storage: 'depolama',
  sync: 'senkronizasyon',
  unknown: 'bilinmeyen'
};

export function classifyError(err) {
  if (!err) return 'unknown';
  if (err.type && ERROR_TYPES[err.type]) return err.type;
  const name = String(err.name || '');
  const code = String(err.code || '');
  if (err.fields) return 'validation';
  if (code.includes('permission-denied') || name === 'NotAllowedError') return 'permission';
  if (code.includes('unavailable') || code.includes('deadline') || name === 'NetworkError' || /network|fetch/i.test(String(err.message || ''))) return 'network';
  if (['QuotaExceededError', 'DataError', 'InvalidStateError', 'TransactionInactiveError', 'AbortError', 'VersionError', 'UnknownError'].includes(name)) return 'storage';
  return 'unknown';
}

function shortMessage(err) {
  const msg = String((err && err.message) || '');
  return msg.length > 160 ? `${msg.slice(0, 157)}…` : msg;
}

function push(level, context, err) {
  const entry = {
    at: new Date().toISOString(),
    level,
    context: String(context || ''),
    type: classifyError(err),
    name: err ? String(err.name || '') : '',
    code: err ? String(err.code || '') : '',
    message: err ? shortMessage(err) : ''
  };
  entries.push(entry);
  if (entries.length > MAX_ENTRIES) entries.shift();
  return entry;
}

export function logError(context, err) {
  const e = push('error', context, err);
  console.error(`[JOZH] ${e.context}: ${e.name}${e.code ? ` (${e.code})` : ''} ${e.message}`);
  return e;
}

export function logWarn(context, err) {
  const e = push('warn', context, err);
  console.warn(`[JOZH] ${e.context}: ${e.name}${e.code ? ` (${e.code})` : ''} ${e.message}`);
  return e;
}

export function logInfo(context, message) {
  push('info', context, { message });
  if (DEBUG) console.info(`[JOZH] ${context}: ${message}`);
}

export function getLogs() {
  return entries.slice();
}
