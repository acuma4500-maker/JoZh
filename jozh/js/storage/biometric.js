// Face ID / Touch ID ile açma (WebAuthn, cihazın kendi doğrulayıcısı).
// Yüz ya da parmak izi bilgisi uygulamaya hiç gelmez: doğrulamayı cihaz yapar, uygulama yalnızca
// kayıtta saklanan açık anahtarla imzayı denetler. Kimlik bilgisi cihaza bağlıdır; yedeğe girmez.
// Açılış PIN'i her zaman yedek yöntem olarak kalır.
import * as db from './local-db.js';
import { randomBytes } from './encryption.js';

const META_KEY = 'appLock:biometric';

function b64url(bytes) {
  let bin = '';
  for (const b of new Uint8Array(bytes)) bin += String.fromCharCode(b);
  return btoa(bin).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
}

function biometricError(message, code) {
  const err = new Error(message);
  err.userMessage = message;
  err.code = code;
  return err;
}

export async function isSupported() {
  try {
    return Boolean(window.PublicKeyCredential && window.isSecureContext
      && await PublicKeyCredential.isUserVerifyingPlatformAuthenticatorAvailable());
  } catch {
    return false;
  }
}

export async function isEnrolled() {
  const cfg = await db.getMeta(META_KEY);
  return Boolean(cfg && cfg.credentialId && cfg.publicKey);
}

// Cihaza göre düğme adı
export function methodName() {
  const ua = navigator.userAgent;
  if (/iPhone|iPad/.test(ua) || (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1)) return 'Face ID';
  if (/Macintosh/.test(ua)) return 'Touch ID';
  return 'Yüz / parmak izi';
}

function friendly(err) {
  if (err && err.userMessage) return err;
  const name = err && err.name;
  if (name === 'NotAllowedError' || name === 'AbortError') return biometricError('Doğrulama iptal edildi ya da süresi doldu.', 'cancelled');
  if (name === 'InvalidStateError') return biometricError('Bu cihazda zaten kayıtlı bir giriş var. Önce kapatıp yeniden aç.', 'exists');
  if (name === 'SecurityError') return biometricError('Bu adreste Face ID kullanılamıyor (HTTPS gerekli).', 'security');
  return biometricError('Face ID ile doğrulama yapılamadı.', 'failed');
}

export async function enroll() {
  const userId = randomBytes(16);
  let cred;
  try {
    cred = await navigator.credentials.create({
      publicKey: {
        challenge: randomBytes(32),
        rp: { name: 'JOZH', id: location.hostname },
        user: { id: userId, name: 'jozh', displayName: 'JOZH' },
        pubKeyCredParams: [{ type: 'public-key', alg: -7 }, { type: 'public-key', alg: -257 }],
        authenticatorSelection: { authenticatorAttachment: 'platform', userVerification: 'required', residentKey: 'preferred' },
        timeout: 60000,
        attestation: 'none'
      }
    });
  } catch (err) {
    throw friendly(err);
  }
  const res = cred.response;
  if (typeof res.getPublicKey !== 'function' || !res.getPublicKey()) {
    throw biometricError('Bu tarayıcı Face ID ile açmayı desteklemiyor. iOS ve Safari\'yi güncelle.', 'unsupported');
  }
  await db.setMeta(META_KEY, {
    credentialId: new Uint8Array(cred.rawId),
    publicKey: new Uint8Array(res.getPublicKey()),
    alg: res.getPublicKeyAlgorithm(),
    createdAt: new Date().toISOString()
  });
}

export function disable() {
  return db.removeMeta(META_KEY);
}

// ECDSA imzası DER biçiminde gelir; Web Crypto r||s (64 bayt) bekler.
function derToRaw(der) {
  const d = new Uint8Array(der);
  let i = 2;
  if (d[1] & 0x80) i += d[1] & 0x7f;
  const read = () => {
    if (d[i] !== 0x02) throw new Error('İmza biçimi geçersiz');
    const len = d[i + 1];
    let v = d.slice(i + 2, i + 2 + len);
    i += 2 + len;
    while (v.length > 32 && v[0] === 0) v = v.slice(1);
    const out = new Uint8Array(32);
    out.set(v, 32 - v.length);
    return out;
  };
  const r = read();
  const s = read();
  const raw = new Uint8Array(64);
  raw.set(r, 0);
  raw.set(s, 32);
  return raw;
}

// Cihaz doğrulaması ister ve imzayı kayıtlı açık anahtarla denetler. Başarılıysa true döner.
export async function verify() {
  const cfg = await db.getMeta(META_KEY);
  if (!cfg) throw biometricError('Face ID ile açma kurulu değil.', 'not-enrolled');
  const challenge = randomBytes(32);
  let assertion;
  try {
    assertion = await navigator.credentials.get({
      publicKey: {
        challenge,
        rpId: location.hostname,
        allowCredentials: [{ type: 'public-key', id: cfg.credentialId }],
        userVerification: 'required',
        timeout: 60000
      }
    });
  } catch (err) {
    throw friendly(err);
  }
  const res = assertion.response;
  const clientDataBytes = new Uint8Array(res.clientDataJSON);
  const clientData = JSON.parse(new TextDecoder().decode(clientDataBytes));
  if (clientData.type !== 'webauthn.get' || clientData.challenge !== b64url(challenge) || clientData.origin !== location.origin) {
    throw biometricError('Doğrulama yanıtı geçersiz.', 'invalid');
  }
  const authData = new Uint8Array(res.authenticatorData);
  const flags = authData[32];
  // 0x01: kullanıcı var, 0x04: kullanıcı doğrulandı (Face ID / Touch ID / cihaz kodu)
  if (!(flags & 0x01) || !(flags & 0x04)) throw biometricError('Kullanıcı doğrulanmadı.', 'not-verified');
  const hash = new Uint8Array(await crypto.subtle.digest('SHA-256', clientDataBytes));
  const signed = new Uint8Array(authData.length + hash.length);
  signed.set(authData, 0);
  signed.set(hash, authData.length);
  let ok = false;
  if (cfg.alg === -7) {
    const key = await crypto.subtle.importKey('spki', cfg.publicKey, { name: 'ECDSA', namedCurve: 'P-256' }, false, ['verify']);
    ok = await crypto.subtle.verify({ name: 'ECDSA', hash: 'SHA-256' }, key, derToRaw(res.signature), signed);
  } else if (cfg.alg === -257) {
    const key = await crypto.subtle.importKey('spki', cfg.publicKey, { name: 'RSASSA-PKCS1-v1_5', hash: 'SHA-256' }, false, ['verify']);
    ok = await crypto.subtle.verify('RSASSA-PKCS1-v1_5', key, res.signature, signed);
  }
  if (!ok) throw biometricError('İmza doğrulanamadı.', 'bad-signature');
  return true;
}
