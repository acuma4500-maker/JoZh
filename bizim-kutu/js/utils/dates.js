// Tarih yardımcıları. Tüm hesaplar cihazın yerel saat dilimini kullanır;
// gün sayısı takvim günü farkıyla hesaplandığı için yaz/kış saati geçişlerinden etkilenmez.
import { START_DATE } from '../constants.js';

const DAY = 86400000;
const MONTHS = ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran', 'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık'];

/** Yerel takvim tarihini (y, m, d) DST'den bağımsız bir gün sayısına çevirir. */
const dayNumber = (y, m, d) => Math.round(Date.UTC(y, m - 1, d) / DAY);

/**
 * Birliktelik süresi. Gün = takvim günü farkı; saat/dakika/saniye = bugün yerel gece yarısından beri geçen süre.
 * Başlangıç gelecekteyse `future: true` ve geri sayım değerleri döner.
 */
export function togetherDuration(now = new Date(), start = START_DATE) {
  const startLocal = new Date(start.year, start.month - 1, start.day, 0, 0, 0, 0);
  if (now < startLocal) {
    let ms = startLocal - now;
    const days = Math.floor(ms / DAY); ms -= days * DAY;
    const hours = Math.floor(ms / 3600000); ms -= hours * 3600000;
    const minutes = Math.floor(ms / 60000); ms -= minutes * 60000;
    return { future: true, days, hours, minutes, seconds: Math.floor(ms / 1000) };
  }
  const days = dayNumber(now.getFullYear(), now.getMonth() + 1, now.getDate()) - dayNumber(start.year, start.month, start.day);
  const midnight = new Date(now.getFullYear(), now.getMonth(), now.getDate(), 0, 0, 0, 0);
  let ms = now - midnight;
  const hours = Math.floor(ms / 3600000); ms -= hours * 3600000;
  const minutes = Math.floor(ms / 60000); ms -= minutes * 60000;
  return { future: false, days, hours, minutes, seconds: Math.floor(ms / 1000) };
}

export const pad2 = (n) => String(n).padStart(2, '0');

export function toMillis(ts) {
  if (!ts) return 0;
  if (typeof ts === 'number') return ts;
  if (typeof ts.toMillis === 'function') return ts.toMillis();
  if (ts instanceof Date) return ts.getTime();
  if (typeof ts.seconds === 'number') return ts.seconds * 1000;
  return 0;
}

export function formatTime(ts) {
  const d = new Date(toMillis(ts));
  return `${pad2(d.getHours())}:${pad2(d.getMinutes())}`;
}

export function formatLongDate(d) {
  return `${d.getDate()} ${MONTHS[d.getMonth()]} ${d.getFullYear()}`;
}

/** 'YYYY-MM-DD' → '22 Ağustos 2026' (saat dilimi kaymasından kaçınmak için yerel olarak ayrıştırılır). */
export function formatISODate(iso) {
  const p = parseISODate(iso);
  return p ? formatLongDate(p) : '';
}

export function parseISODate(iso) {
  const m = /^(\d{4})-(\d{2})-(\d{2})$/.exec(iso || '');
  if (!m) return null;
  const d = new Date(+m[1], +m[2] - 1, +m[3]);
  return d.getMonth() === +m[2] - 1 ? d : null;
}

export function todayISO(now = new Date()) {
  return `${now.getFullYear()}-${pad2(now.getMonth() + 1)}-${pad2(now.getDate())}`;
}

/** İki ISO tarih arası gün farkı (b - a). */
export function daysBetweenISO(a, b) {
  const pa = parseISODate(a), pb = parseISODate(b);
  if (!pa || !pb) return null;
  return dayNumber(pb.getFullYear(), pb.getMonth() + 1, pb.getDate()) - dayNumber(pa.getFullYear(), pa.getMonth() + 1, pa.getDate());
}

export function dayKey(ts) {
  const d = new Date(toMillis(ts));
  return `${d.getFullYear()}-${pad2(d.getMonth() + 1)}-${pad2(d.getDate())}`;
}

export function dayLabel(ts, now = new Date()) {
  const diff = daysBetweenISO(dayKey(ts), todayISO(now));
  if (diff === 0) return 'Bugün';
  if (diff === 1) return 'Dün';
  const d = new Date(toMillis(ts));
  if (diff > 1 && diff < 7) return d.toLocaleDateString('tr-TR', { weekday: 'long' });
  return formatLongDate(d);
}

export function relativeTime(ts, now = Date.now()) {
  const ms = toMillis(ts);
  if (!ms) return '';
  const s = Math.max(0, Math.round((now - ms) / 1000));
  if (s < 45) return 'az önce';
  const m = Math.round(s / 60);
  if (m < 60) return `${m} dk önce`;
  const hr = Math.round(m / 60);
  if (hr < 24) return `${hr} saat önce`;
  const d = Math.round(hr / 24);
  if (d < 7) return `${d} gün önce`;
  return formatLongDate(new Date(ms));
}

export function lastSeenText(ts, now = Date.now()) {
  const ms = toMillis(ts);
  if (!ms) return 'Henüz görülmedi';
  const label = dayLabel(ms, new Date(now));
  if (label === 'Bugün') return `Son görülme bugün ${formatTime(ms)}`;
  if (label === 'Dün') return `Son görülme dün ${formatTime(ms)}`;
  return `Son görülme ${label} ${formatTime(ms)}`;
}

/** Son tarih için kısa açıklama: "Bugün", "3 gün kaldı", "2 gün geçti". */
export function dueLabel(iso, now = new Date()) {
  if (!iso) return '';
  const diff = daysBetweenISO(todayISO(now), iso);
  if (diff === null) return '';
  if (diff === 0) return 'Bugün';
  if (diff === 1) return 'Yarın';
  if (diff > 1) return `${diff} gün kaldı`;
  return `${-diff} gün gecikti`;
}

/** Yılın kaçıncı günü — "günün sorusu" için deterministik indeks. */
export function dayOfYearIndex(now = new Date()) {
  return dayNumber(now.getFullYear(), now.getMonth() + 1, now.getDate());
}
