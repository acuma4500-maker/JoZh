// Formlara özel küçük doğrulayıcılar (asıl kayıt doğrulaması storage/schemas.js'tedir).

export function validateBackupPassword(password, repeat) {
  const errors = {};
  if (!password || password.length < 10) errors.password = 'Yedek parolası en az 10 karakter olmalı.';
  if (repeat !== undefined && password !== repeat) errors.passwordRepeat = 'İki parola aynı değil.';
  return errors;
}

export function validateRequired(data, names) {
  const errors = {};
  for (const name of names) {
    if (!String(data[name] ?? '').trim()) errors[name] = 'Bu alan zorunlu.';
  }
  return errors;
}

export function hasErrors(errors) {
  return Object.keys(errors || {}).length > 0;
}

export function isPinComplete(pin) {
  return /^\d{4}$/.test(pin);
}
