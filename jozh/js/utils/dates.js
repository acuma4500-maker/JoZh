// Tarih yardımcıları. Tarihler yerel saat dilimiyle YYYY-MM-DD olarak işlenir;
// new Date("YYYY-MM-DD") (UTC olarak yorumlanır) hiçbir yerde kullanılmaz.

export const MONTHS = ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran', 'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık'];
export const WEEKDAYS = ['Pazar', 'Pazartesi', 'Salı', 'Çarşamba', 'Perşembe', 'Cuma', 'Cumartesi'];
export const WEEKDAYS_SHORT_MON = ['Pzt', 'Sal', 'Çar', 'Per', 'Cum', 'Cmt', 'Paz'];

const ISO_DATE_RE = /^(\d{4})-(\d{2})-(\d{2})$/;
const TIME_RE = /^([01]\d|2[0-3]):([0-5]\d)$/;

export function pad2(n) {
  return String(n).padStart(2, '0');
}

export function isLeapYear(y) {
  return (y % 4 === 0 && y % 100 !== 0) || y % 400 === 0;
}

export function daysInMonth(year, month0) {
  return new Date(year, month0 + 1, 0).getDate();
}

export function toISODate(date) {
  return `${date.getFullYear()}-${pad2(date.getMonth() + 1)}-${pad2(date.getDate())}`;
}

export function todayISO() {
  return toISODate(new Date());
}

export function nowISO() {
  return new Date().toISOString();
}

export function isValidISODate(value) {
  const m = ISO_DATE_RE.exec(value || '');
  if (!m) return false;
  const y = Number(m[1]);
  const mo = Number(m[2]);
  const d = Number(m[3]);
  if (y < 1000 || mo < 1 || mo > 12 || d < 1) return false;
  return d <= daysInMonth(y, mo - 1);
}

export function isValidTime(value) {
  return TIME_RE.test(value || '');
}

export function parseISODate(value) {
  if (!isValidISODate(value)) return null;
  const [y, m, d] = value.split('-').map(Number);
  return new Date(y, m - 1, d);
}

export function addDays(iso, n) {
  const d = parseISODate(iso);
  d.setDate(d.getDate() + n);
  return toISODate(d);
}

export function addMonths(year, month0, n) {
  const d = new Date(year, month0 + n, 1);
  return { year: d.getFullYear(), month0: d.getMonth() };
}

// Takvim günü numarası (saat dilimi ve yaz saatinden etkilenmez).
export function dayNumber(iso) {
  const [y, m, d] = iso.split('-').map(Number);
  return Math.round(Date.UTC(y, m - 1, d) / 86400000);
}

// b - a (gün)
export function diffDays(a, b) {
  return dayNumber(b) - dayNumber(a);
}

export function monthKey(iso) {
  return iso.slice(0, 7);
}

export function formatDate(iso, { weekday = false, short = false, year = true } = {}) {
  const d = parseISODate(iso);
  if (!d) return '';
  const month = short ? MONTHS[d.getMonth()].slice(0, 3) : MONTHS[d.getMonth()];
  let text = `${d.getDate()} ${month}`;
  if (year) text += ` ${d.getFullYear()}`;
  if (weekday) text += `, ${WEEKDAYS[d.getDay()]}`;
  return text;
}

export function formatMonthYear(year, month0) {
  return `${MONTHS[month0]} ${year}`;
}

// ISO zaman damgasından (2026-10-14T11:05:00.000Z) yerel saat "14:05".
export function formatClock(isoString) {
  const d = new Date(isoString);
  if (Number.isNaN(d.getTime())) return '';
  return `${pad2(d.getHours())}:${pad2(d.getMinutes())}`;
}

export function formatDateTime(isoString) {
  const d = new Date(isoString);
  if (Number.isNaN(d.getTime())) return '';
  return `${formatDate(toISODate(d))} ${formatClock(isoString)}`;
}

export function calcAge(birthIso, today = todayISO()) {
  if (!isValidISODate(birthIso)) return null;
  const [by, bm, bd] = birthIso.split('-').map(Number);
  const [ty, tm, td] = today.split('-').map(Number);
  let age = ty - by;
  if (tm < bm || (tm === bm && td < bd)) age -= 1;
  return age >= 0 ? age : null;
}

// Yıllık tekrar eden bir tarihin bugünden itibaren bir sonraki günü.
// 29 Şubat artık olmayan yılda 28 Şubat olarak hesaplanır.
export function nextOccurrence(iso, from = todayISO()) {
  if (!isValidISODate(iso)) return null;
  const [oy, om, od] = iso.split('-').map(Number);
  const fromYear = Number(from.slice(0, 4));
  for (let y = fromYear; y <= fromYear + 1; y += 1) {
    const day = om === 2 && od === 29 && !isLeapYear(y) ? 28 : od;
    const candidate = `${y}-${pad2(om)}-${pad2(day)}`;
    if (candidate >= from) {
      return { date: candidate, years: y - oy, daysLeft: diffDays(from, candidate) };
    }
  }
  return null;
}

export function relativeDayLabel(daysLeft) {
  if (daysLeft === 0) return 'Bugün';
  if (daysLeft === 1) return 'Yarın';
  if (daysLeft > 1) return `${daysLeft} gün kaldı`;
  if (daysLeft === -1) return 'Dün';
  return `${Math.abs(daysLeft)} gün önce`;
}

// Pazartesi ile başlayan 6 haftalık ay ızgarası (her hafta 7 ISO tarih).
export function monthGrid(year, month0) {
  const first = new Date(year, month0, 1);
  const offset = (first.getDay() + 6) % 7;
  const start = new Date(year, month0, 1 - offset);
  const weeks = [];
  for (let w = 0; w < 6; w += 1) {
    const week = [];
    for (let i = 0; i < 7; i += 1) {
      const d = new Date(start.getFullYear(), start.getMonth(), start.getDate() + w * 7 + i);
      week.push(toISODate(d));
    }
    weeks.push(week);
  }
  return weeks;
}

export function weekdayIndexMon(iso) {
  return (parseISODate(iso).getDay() + 6) % 7;
}
