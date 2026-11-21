import { initializeTestEnvironment } from '@firebase/rules-unit-testing';
import { readFileSync } from 'node:fs';
import { doc, setDoc } from 'firebase/firestore';
import { ref, set } from 'firebase/database';

export const A = 'pt0Kmbc9rqdJekFyvA1wLItUnxw1'; // Cuma (kişi kimliği)
export const B = 'cf6RqCRF6dPEWtSR1L9Dm2Uv4Ap1'; // İlayda
export const X = 'ucuncuKisi';                    // yanlış PIN girmiş üçüncü cihaz
// Testlerde gerçek PIN'ler KULLANILMAZ.
export const PINS = { [A]: '1111', [B]: '2222' };
// Kişi → anonim cihaz kimliği
export const DEV = { [A]: 'cihazCuma', [B]: 'cihazIlayda', [X]: 'cihazYabanci' };

export async function env() {
  return initializeTestEnvironment({
    projectId: 'demo-bizimkutu',
    firestore: { rules: readFileSync(new URL('../../firebase/firestore.rules', import.meta.url), 'utf8'), host: '127.0.0.1', port: 8080 },
    database: { rules: readFileSync(new URL('../../firebase/database.rules.json', import.meta.url), 'utf8'), host: '127.0.0.1', port: 9000 },
  });
}

/** PIN'leri ve doğrulanmış cihazları kurallar devre dışıyken yerleştirir. */
export async function seedFirestore(t) {
  await t.withSecurityRulesDisabled(async (ctx) => {
    const db = ctx.firestore();
    await setDoc(doc(db, 'secrets/pins'), PINS);
    await setDoc(doc(db, `pinTry/${DEV[A]}`), { pin: PINS[A], person: A, n: 1 });
    await setDoc(doc(db, `pinTry/${DEV[B]}`), { pin: PINS[B], person: B, n: 1 });
    await setDoc(doc(db, `pinTry/${DEV[X]}`), { pin: '9999', person: A, n: 1 });
  });
}
export async function seedDatabase(t) {
  await t.withSecurityRulesDisabled(async (ctx) => {
    const db = ctx.database();
    await set(ref(db, 'secrets/pins'), PINS);
    await set(ref(db, `pinTry/${DEV[A]}`), { pin: PINS[A], person: A, n: 1 });
    await set(ref(db, `pinTry/${DEV[B]}`), { pin: PINS[B], person: B, n: 1 });
    await set(ref(db, `pinTry/${DEV[X]}`), { pin: '9999', person: A, n: 1 });
  });
}
