import { initializeTestEnvironment } from '@firebase/rules-unit-testing';
import { readFileSync } from 'node:fs';

export const A = 'pt0Kmbc9rqdJekFyvA1wLItUnxw1'; // Cuma
export const B = 'cf6RqCRF6dPEWtSR1L9Dm2Uv4Ap1'; // İlayda
export const X = 'ucuncuKisiUid000000000000000'; // izinsiz üçüncü hesap

export async function env() {
  return initializeTestEnvironment({
    projectId: 'demo-bizimkutu',
    firestore: { rules: readFileSync(new URL('../../firebase/firestore.rules', import.meta.url), 'utf8'), host: '127.0.0.1', port: 8080 },
    database: { rules: readFileSync(new URL('../../firebase/database.rules.json', import.meta.url), 'utf8'), host: '127.0.0.1', port: 9000 },
  });
}
