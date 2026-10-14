// Bir günün planları (Takvim ve Ana panel ortak).
import { el, button } from '../ui.js';
import { PLAN_TYPES } from '../utils/labels.js';
import { plansOnDay, formatPlanRange, timingLabel, budgetLabel } from '../utils/plan-helpers.js';
import { formatDate } from '../utils/dates.js';

export function planTypeMarker(type) {
  return el('span', { class: `type-dot type-${type}`, 'aria-hidden': 'true' });
}

export function planRow(plan, onOpen, today) {
  const t = timingLabel(plan, today);
  const budget = budgetLabel(plan);
  const btn = el('button', { type: 'button', class: 'open-button' },
    el('span', { class: 'item-title' }, plan.name),
    el('span', { class: 'item-meta' },
      el('span', { class: 'row type-label' }, planTypeMarker(plan.type), PLAN_TYPES[plan.type]),
      el('span', null, formatPlanRange(plan)),
      plan.location ? el('span', null, plan.location) : null,
      el('span', { class: `chip${t.kind ? ` chip-${t.kind}` : ''}` }, t.text),
      budget ? el('span', null, budget) : null));
  btn.addEventListener('click', () => onOpen(plan));
  return el('li', { class: 'list-item' }, el('div', { class: 'item-main' }, btn));
}

// options: { date, plans, onOpen, onAdd, today }
export function renderDayPlans({ date, plans, onOpen, onAdd, today }) {
  const list = plansOnDay(plans, date);
  const wrap = el('section', { class: 'day-plans', 'aria-label': `${formatDate(date)} planları` },
    el('div', { class: 'card-header' },
      el('h3', null, formatDate(date, { weekday: true })),
      onAdd ? button('Bu güne plan ekle', () => onAdd(date), { iconName: 'plus', className: 'btn-small' }) : null));
  if (!list.length) wrap.append(el('p', { class: 'muted small' }, 'Bu gün için plan yok.'));
  else wrap.append(el('ul', { class: 'list' }, list.map((p) => planRow(p, onOpen, today))));
  return wrap;
}
