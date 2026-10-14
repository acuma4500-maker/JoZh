// Sevdiğim kadın bölümleri ve önemli tarih hesapları.
import { nextOccurrence, todayISO, diffDays, isValidISODate } from './dates.js';

// 14 bölüm: genel bilgiler, 7 liste, önemli tarihler, anılar, galeri, yapılacaklar, sürprizler, özel notlar
export const LIST_SECTIONS = [
  { key: 'traits', title: 'Kişilik özellikleri', placeholder: 'ör. Sabırlı' },
  { key: 'likes', title: 'Sevdikleri', placeholder: 'ör. Deniz kenarında yürüyüş' },
  { key: 'dislikes', title: 'Sevmedikleri', placeholder: 'ör. Geç kalınması' },
  { key: 'foods', title: 'Sevdiği yemekler', placeholder: 'ör. Mantı' },
  { key: 'colors', title: 'Renkler', placeholder: 'ör. Bordo' },
  { key: 'perfumes', title: 'Parfümler', placeholder: 'ör. Marka ve adı' },
  { key: 'hobbies', title: 'Hobiler', placeholder: 'ör. Fotoğrafçılık' }
];

export const CHECK_SECTIONS = [
  { key: 'todos', title: 'Birlikte yapılacaklar', placeholder: 'ör. Kapadokya\'da balon turu' },
  { key: 'surprises', title: 'Sürpriz fikirleri', placeholder: 'ör. Doğum gününde sürpriz kahvaltı' }
];

// Önemli tarihler kendiliğinden sıralanır. Doğum günü, birliktelik yıl dönümü ve "her yıl" işaretli
// tarihler her yıl yeniden hesaplanır.
export function importantDates(partner, today = todayISO()) {
  if (!partner) return [];
  const out = [];
  if (isValidISODate(partner.birthDate)) {
    const n = nextOccurrence(partner.birthDate, today);
    if (n) out.push({ id: 'birthday', title: 'Doğum günü', original: partner.birthDate, date: n.date, daysLeft: n.daysLeft, note: `${n.years}. yaşı`, yearly: true, kind: 'birthday' });
  }
  if (isValidISODate(partner.togetherSince)) {
    const n = nextOccurrence(partner.togetherSince, today);
    if (n && n.years > 0) out.push({ id: 'anniversary', title: 'Birliktelik yıl dönümü', original: partner.togetherSince, date: n.date, daysLeft: n.daysLeft, note: `${n.years}. yıl`, yearly: true, kind: 'anniversary' });
  }
  for (const item of partner.importantDates || []) {
    if (!isValidISODate(item.date)) continue;
    if (item.yearly) {
      const n = nextOccurrence(item.date, today);
      if (n) out.push({ id: item.id, title: item.title, original: item.date, date: n.date, daysLeft: n.daysLeft, note: n.years > 0 ? `${n.years}. yıl` : '', yearly: true, kind: 'custom' });
    } else {
      out.push({ id: item.id, title: item.title, original: item.date, date: item.date, daysLeft: diffDays(today, item.date), note: '', yearly: false, kind: 'custom' });
    }
  }
  // Yaklaşanlar önce (en yakın başta), geçmiş tek seferlik tarihler en sonda (en yeni başta).
  return out.sort((a, b) => {
    const ap = a.daysLeft < 0;
    const bp = b.daysLeft < 0;
    if (ap !== bp) return ap ? 1 : -1;
    return ap ? b.daysLeft - a.daysLeft : a.daysLeft - b.daysLeft;
  });
}

export function nextImportantDate(partner, today = todayISO()) {
  return importantDates(partner, today).find((d) => d.daysLeft >= 0) || null;
}

export function togetherDuration(partner, today = todayISO()) {
  if (!partner || !isValidISODate(partner.togetherSince) || partner.togetherSince > today) return null;
  const days = diffDays(partner.togetherSince, today);
  const [sy, sm, sd] = partner.togetherSince.split('-').map(Number);
  const [ty, tm, td] = today.split('-').map(Number);
  let months = (ty - sy) * 12 + (tm - sm);
  if (td < sd) months -= 1;
  const years = Math.floor(months / 12);
  const rest = months % 12;
  let text = '';
  if (years) text += `${years} yıl`;
  if (rest) text += `${text ? ' ' : ''}${rest} ay`;
  if (!text) text = `${days} gün`;
  return { days, text };
}
