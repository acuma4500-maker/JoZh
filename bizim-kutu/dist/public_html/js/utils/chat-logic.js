// Sohbetle ilgili saf (Firebase'siz) hesaplamalar — birim testleriyle doğrulanır.

/** pending: sunucuya ulaşmadı · sent: sunucuda (iletildi) · delivered: karşı cihaza ulaştı · read: görüldü */
export function messageStatus(msg, partnerReceipt) {
  if (!msg || typeof msg.ts !== 'number') return 'pending';
  const r = partnerReceipt || {};
  if ((r.readAt || 0) >= msg.ts) return 'read';
  if ((r.deliveredAt || 0) >= msg.ts) return 'delivered';
  return 'sent';
}

/** Benim okumadığım, partnerden gelen mesaj sayısı. */
export function unreadCount(messages, myUid, myReadAt = 0) {
  return messages.filter((m) => m.uid !== myUid && !m.deleted && typeof m.ts === 'number' && m.ts > myReadAt).length;
}

/** Mesaj listesine tarih ayraçları ekler: [{type:'day', key}, {type:'msg', msg}] */
export function withDaySeparators(messages, dayKeyFn) {
  const out = [];
  let last = null;
  for (const m of messages) {
    const k = dayKeyFn(typeof m.ts === 'number' ? m.ts : Date.now());
    if (k !== last) { out.push({ type: 'day', key: k, ts: typeof m.ts === 'number' ? m.ts : Date.now() }); last = k; }
    out.push({ type: 'msg', msg: m });
  }
  return out;
}
