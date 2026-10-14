// Plan hesapları: tarih aralığı, kalan gün, bütçe ve takvim şeritleri.
import { diffDays, relativeDayLabel, formatDate, todayISO, dayNumber } from './dates.js';
import { formatMoney } from './formatters.js';

export function planStart(plan) {
  return plan.startDate;
}

export function planEnd(plan) {
  return plan.endDate && plan.endDate >= plan.startDate ? plan.endDate : plan.startDate;
}

export function isOnDay(plan, iso) {
  return planStart(plan) <= iso && iso <= planEnd(plan);
}

export function overlapsRange(plan, from, to) {
  return planStart(plan) <= to && planEnd(plan) >= from;
}

export function isUpcomingOrOngoing(plan, today = todayISO()) {
  return plan.status !== 'cancelled' && planEnd(plan) >= today;
}

export function isPast(plan, today = todayISO()) {
  return planEnd(plan) < today;
}

// Kartta gösterilen zaman etiketi: "3 gün kaldı", "Bugün", "Devam ediyor", "Geçti"
export function timingLabel(plan, today = todayISO()) {
  if (plan.status === 'cancelled') return { text: 'İptal', kind: 'red' };
  const start = planStart(plan);
  const end = planEnd(plan);
  if (today < start) {
    const d = diffDays(today, start);
    return { text: relativeDayLabel(d), kind: d <= 3 ? 'yellow' : 'accent' };
  }
  if (today <= end) {
    if (start === end) return { text: 'Bugün', kind: 'green' };
    return { text: 'Devam ediyor', kind: 'green' };
  }
  return { text: plan.status === 'completed' ? 'Tamamlandı' : 'Geçti', kind: '' };
}

export function formatPlanRange(plan) {
  const start = planStart(plan);
  const end = planEnd(plan);
  const sameYear = start.slice(0, 4) === end.slice(0, 4);
  const s = `${formatDate(start, { short: true, year: !sameYear || start === end })}${plan.startTime ? ` ${plan.startTime}` : ''}`;
  if (start === end) {
    return plan.endTime ? `${s} – ${plan.endTime}` : s;
  }
  return `${s} – ${formatDate(end, { short: true })}${plan.endTime ? ` ${plan.endTime}` : ''}`;
}

export function durationDays(plan) {
  return diffDays(planStart(plan), planEnd(plan)) + 1;
}

export function tripTotals(plan) {
  const expenses = (plan.trip && plan.trip.expenses) || [];
  const estimated = expenses.reduce((s, e) => s + (Number(e.estimated) || 0), 0);
  const actual = expenses.reduce((s, e) => s + (Number(e.actual) || 0), 0);
  return { estimated: round2(estimated), actual: round2(actual) };
}

export function budgetSummary(plan) {
  const budget = Number(plan.budget) || 0;
  const spent = plan.type === 'trip' ? tripTotals(plan).actual : Number(plan.spent) || 0;
  return { budget, spent, remaining: round2(budget - spent), hasBudget: plan.budget !== null && plan.budget !== undefined };
}

export function budgetLabel(plan) {
  const b = budgetSummary(plan);
  if (!b.hasBudget && !b.spent) return '';
  if (!b.hasBudget) return `Harcama ${formatMoney(b.spent)}`;
  return `Bütçe ${formatMoney(b.budget)} · Kalan ${formatMoney(b.remaining)}`;
}

function round2(n) {
  return Math.round(n * 100) / 100;
}

export function sortByStart(plans) {
  return plans.slice().sort((a, b) => (a.startDate + (a.startTime || '')).localeCompare(b.startDate + (b.startTime || '')) || a.name.localeCompare(b.name, 'tr'));
}

// Bir haftadaki planları şeritlere yerleştirir. Bir plan hafta içinde hep aynı satırda kalır.
// Dönüş: { lanes: [[{ plan, startCol, endCol }]], hidden: [her gün için gizli plan sayısı] }
export function layoutWeek(weekDates, plans, maxLanes = 3) {
  const weekStart = weekDates[0];
  const weekEnd = weekDates[6];
  const startNum = dayNumber(weekStart);
  const segments = plans
    .filter((p) => p.status !== 'cancelled' && overlapsRange(p, weekStart, weekEnd))
    .map((p) => ({
      plan: p,
      startCol: Math.max(0, dayNumber(planStart(p)) - startNum),
      endCol: Math.min(6, dayNumber(planEnd(p)) - startNum)
    }))
    .sort((a, b) => a.startCol - b.startCol || (b.endCol - b.startCol) - (a.endCol - a.startCol) || (a.plan.startTime || '').localeCompare(b.plan.startTime || ''));
  const lanes = [];
  const hidden = [0, 0, 0, 0, 0, 0, 0];
  for (const seg of segments) {
    let placed = false;
    for (const lane of lanes) {
      if (lane[lane.length - 1].endCol < seg.startCol) {
        lane.push(seg);
        placed = true;
        break;
      }
    }
    if (!placed) lanes.push([seg]);
  }
  const visible = lanes.slice(0, maxLanes);
  for (const lane of lanes.slice(maxLanes)) {
    for (const seg of lane) {
      for (let c = seg.startCol; c <= seg.endCol; c += 1) hidden[c] += 1;
    }
  }
  return { lanes: visible, hidden };
}

export function plansOnDay(plans, iso) {
  return sortByStart(plans.filter((p) => p.status !== 'cancelled' && isOnDay(p, iso)));
}
