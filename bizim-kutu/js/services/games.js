// Oyun merkezi altyapısı (Realtime Database):
//   games/invitations/{id}  — davetler (bekliyor → kabul/ret/iptal)
//   games/sessions/{id}     — oyun oturumu (davet kimliğiyle aynı); durum, sıra, oyuncular
//   games/scores/{oyun}/{uid|draw} — toplam galibiyetler
// Hamleler RTDB işlemleriyle (transaction) yazılır; aynı anda yapılan hamleler çakışmaz.
import { rtdb } from '../firebase-config.js';
import {
  ref, push, set, update, remove, onValue, get, rtdbQuery, orderByChild, limitToLast,
  rtdbServerTimestamp, rtdbTransaction, onDisconnect
} from '../vendor/firebase.js';
import { getState, serverNow } from '../state.js';
import { gameById } from '../games/registry.js';
import { notify } from './notifications.js';
import { userName } from '../constants.js';

export const INVITE_TTL = 2 * 60 * 1000;

export async function loadGame(id) {
  const g = gameById(id);
  if (!g) throw new Error('Bilinmeyen oyun.');
  return (await g.module()).default;
}

export async function sendInvite(gameId) {
  const { uid, partnerUid, presence } = getState();
  if (!presence[partnerUid]?.online) throw new Error(`${userName(partnerUid)} şu an çevrim dışı. Canlı oyunlar ikiniz de çevrim içiyken başlar.`);
  const r = push(ref(rtdb, 'games/invitations'));
  await set(r, { from: uid, to: partnerUid, game: gameId, status: 'pending', createdAt: rtdbServerTimestamp() });
  const g = gameById(gameId);
  notify('game_invite', { title: `${userName(uid)} seni ${g.name} oynamaya çağırıyor`, body: 'Oyun merkezinden kabul edebilirsin.', link: '#/games' });
  return r.key;
}

export function subscribeInvites(cb) {
  const q = rtdbQuery(ref(rtdb, 'games/invitations'), orderByChild('createdAt'), limitToLast(20));
  return onValue(q, (snap) => {
    const list = [];
    snap.forEach((c) => { list.push({ id: c.key, ...c.val() }); });
    cb(list.reverse());
  }, (e) => console.warn('invites', e));
}

export const isInviteLive = (inv, now = serverNow()) => inv.status === 'pending' && typeof inv.createdAt === 'number' && now - inv.createdAt < INVITE_TTL;

export async function acceptInvite(inv) {
  const { uid } = getState();
  if (inv.to !== uid) throw new Error('Bu davet sana ait değil.');
  if (!isInviteLive(inv)) throw new Error('Davetin süresi dolmuş.');
  const mod = await loadGame(inv.game);
  const players = [inv.from, inv.to];
  const state = await mod.create({ players, host: inv.from, prev: null });
  await update(ref(rtdb), {
    [`games/sessions/${inv.id}`]: {
      game: inv.game, players: { [inv.from]: true, [inv.to]: true }, host: inv.from,
      status: 'active', round: 1, state, createdAt: rtdbServerTimestamp(), updatedAt: rtdbServerTimestamp()
    },
    [`games/invitations/${inv.id}/status`]: 'accepted',
    [`games/invitations/${inv.id}/respondedAt`]: rtdbServerTimestamp(),
  });
  const g = gameById(inv.game);
  notify('game_accept', { title: `${userName(uid)} ${g.name} davetini kabul etti`, body: 'Oyun başladı!', link: `#/play/${inv.id}` });
  return inv.id;
}

export const declineInvite = (inv) => update(ref(rtdb, `games/invitations/${inv.id}`), { status: 'declined', respondedAt: rtdbServerTimestamp() });
export const cancelInvite = (inv) => update(ref(rtdb, `games/invitations/${inv.id}`), { status: 'cancelled', respondedAt: rtdbServerTimestamp() });

/** 1 günden eski, kendi gönderdiğim davetleri ve 7 günden eski bitmiş oturumları temizler. */
export async function cleanupOldGames() {
  const { uid } = getState();
  try {
    const snap = await get(rtdbQuery(ref(rtdb, 'games/invitations'), orderByChild('createdAt'), limitToLast(100)));
    const now = serverNow();
    const jobs = [];
    snap.forEach((c) => {
      const v = c.val();
      if (v.from === uid && now - (v.createdAt || 0) > 86400000) jobs.push(remove(c.ref));
    });
    await Promise.allSettled(jobs);
  } catch {}
}

// --- Oturum ---
export const sessionRef = (sid) => ref(rtdb, `games/sessions/${sid}`);

export function subscribeSession(sid, cb, onError) {
  return onValue(sessionRef(sid), (s) => cb(s.exists() ? { id: sid, ...s.val() } : null), onError);
}

/**
 * Oturum üzerinde atomik değişiklik. mutator(session) yeni oturumu döndürür ya da
 * değişiklik yoksa undefined. Döner: { committed, session }
 */
export async function act(sid, mutator) {
  const res = await rtdbTransaction(sessionRef(sid), (cur) => {
    if (cur === null) return cur; // yerel önbellek boş: sunucu verisiyle yeniden denenir
    const draft = structuredClone(cur);
    const next = mutator(draft);
    if (next === undefined) return undefined; // vazgeç
    next.updatedAt = rtdbServerTimestamp();
    return next;
  }, { applyLocally: true });
  return { committed: res.committed, session: res.snapshot.val() };
}

/** Oyuncunun oyunda olduğunu bildirir; bağlantı koparsa sunucu kaydı siler. */
export async function joinSession(sid, uid) {
  const r = ref(rtdb, `games/sessions/${sid}/here/${uid}`);
  await onDisconnect(r).remove();
  await set(r, true);
  return async () => { try { await onDisconnect(r).cancel(); await remove(r); } catch {} };
}

export function addScore(gameId, key) {
  return rtdbTransaction(ref(rtdb, `games/scores/${gameId}/${key}`), (v) => (typeof v === 'number' ? v + 1 : 1)).catch((e) => console.warn('skor', e));
}

export function subscribeScores(gameId, cb) {
  return onValue(ref(rtdb, `games/scores/${gameId}`), (s) => cb(s.val() || {}), () => cb({}));
}
