// Çevrim içi durum: presence/{uid}/connections/{bağlantı} + lastSeen (sunucu zamanı).
// Her sekme/cihaz kendi bağlantı kaydını ekler; onDisconnect() sunucu tarafında çalıştığı için
// sekme çöktüğünde veya internet koptuğunda da kayıt silinir. Kullanıcı, en az bir bağlantısı varsa çevrim içidir.
import { rtdb } from '../firebase-config.js';
import { ref, onValue, push, set, onDisconnect, rtdbServerTimestamp, remove } from '../vendor/firebase.js';
import { setState, getState } from '../state.js';

let myConnRef = null;
let unsubs = [];

export function startPresence(uid) {
  stopPresence();
  const connectedRef = ref(rtdb, '.info/connected');
  unsubs.push(onValue(connectedRef, async (snap) => {
    const connected = snap.val() === true;
    setState({ connected });
    if (!connected) return;
    try {
      const conn = push(ref(rtdb, `presence/${uid}/connections`));
      // Önce onDisconnect kur, sonra kendini çevrim içi yaz (sıralama önemli).
      await onDisconnect(conn).remove();
      await onDisconnect(ref(rtdb, `presence/${uid}/lastSeen`)).set(rtdbServerTimestamp());
      await set(conn, true);
      await set(ref(rtdb, `presence/${uid}/lastSeen`), rtdbServerTimestamp());
      myConnRef = conn;
    } catch (e) { console.warn('presence', e); }
  }));
  unsubs.push(onValue(ref(rtdb, '.info/serverTimeOffset'), (snap) => setState({ serverOffset: Number(snap.val()) || 0 })));
  unsubs.push(onValue(ref(rtdb, 'presence'), (snap) => {
    const val = snap.val() || {};
    const presence = {};
    for (const [u, p] of Object.entries(val)) {
      presence[u] = { online: !!(p && p.connections && Object.keys(p.connections).length), lastSeen: p?.lastSeen || 0 };
    }
    setState({ presence });
  }, (err) => console.warn('presence listen', err)));
}

/** Çıkışta: bağlantı kaydını sil, son görülmeyi yaz. */
export async function stopPresence() {
  const uid = getState().uid;
  unsubs.forEach((u) => u()); unsubs = [];
  if (myConnRef && uid) {
    try {
      await remove(myConnRef);
      await set(ref(rtdb, `presence/${uid}/lastSeen`), rtdbServerTimestamp());
    } catch {}
  }
  myConnRef = null;
}

export const isOnline = (uid) => !!getState().presence[uid]?.online;
