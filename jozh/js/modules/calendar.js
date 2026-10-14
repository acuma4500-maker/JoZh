// Takvim: planlarla aynı veri. Aylık ızgara (pazartesi başlar), çok günlük kesintisiz şeritler, liste görünümü.
import { initApp, renderLoadError } from '../app.js';
import { listRecords, getSingleton } from '../storage/records.js';
import { el, replace, loadingState, button, iconButton, segmented, emptyState } from '../ui.js';
import { PLAN_TYPES } from '../utils/labels.js';
import { todayISO, monthGrid, formatMonthYear, addMonths, WEEKDAYS_SHORT_MON, formatDate, pad2, daysInMonth } from '../utils/dates.js';
import { layoutWeek, plansOnDay, overlapsRange, sortByStart } from '../utils/plan-helpers.js';
import { openPlanEditor } from '../components/plan-editor.js';
import { renderDayPlans, planRow } from '../components/day-plans.js';

const main = document.getElementById('main');
const today = todayISO();
const state = {
  plans: [],
  year: Number(today.slice(0, 4)),
  month0: Number(today.slice(5, 7)) - 1,
  selected: today,
  view: 'month'
};
const titleEl = el('h2', { class: 'cal-title', 'aria-live': 'polite' });
const body = el('div', { class: 'cal-body' });
const dayPanel = el('div', { class: 'card cal-day-panel' });

const openPlan = (plan) => openPlanEditor({ plan, onSaved: load, onDeleted: load });
const addPlan = (date) => openPlanEditor({ defaults: { startDate: date }, onSaved: load });

function renderDayPanel() {
  replace(dayPanel, renderDayPlans({ date: state.selected, plans: state.plans, onOpen: openPlan, onAdd: addPlan, today }));
}

function selectDay(iso) {
  state.selected = iso;
  for (const b of body.querySelectorAll('.cal-day')) {
    b.classList.toggle('is-selected', b.dataset.date === iso);
    b.setAttribute('aria-pressed', String(b.dataset.date === iso));
  }
  renderDayPanel();
}

function renderMonth() {
  const weeks = monthGrid(state.year, state.month0);
  const monthPrefix = `${state.year}-${pad2(state.month0 + 1)}`;
  const grid = el('div', { class: 'cal-grid' },
    el('div', { class: 'cal-weekdays', 'aria-hidden': 'true' }, WEEKDAYS_SHORT_MON.map((d) => el('span', null, d))));
  for (const week of weeks) {
    const { lanes, hidden } = layoutWeek(week, state.plans, 3);
    const row = el('div', { class: 'cal-week' });
    week.forEach((iso, col) => {
      const count = plansOnDay(state.plans, iso).length;
      const label = `${formatDate(iso, { weekday: true })}${count ? `, ${count} plan` : ', plan yok'}${iso === today ? ', bugün' : ''}`;
      const btn = el('button', {
        type: 'button',
        class: `cal-day${iso.startsWith(monthPrefix) ? '' : ' is-other'}${iso === today ? ' is-today' : ''}${iso === state.selected ? ' is-selected' : ''}`,
        'aria-label': label,
        'aria-pressed': String(iso === state.selected),
        dataset: { date: iso }
      }, el('span', { class: 'cal-num' }, String(Number(iso.slice(8)))), hidden[col] ? el('span', { class: 'cal-more' }, `+${hidden[col]}`) : null);
      btn.style.gridColumn = String(col + 1);
      btn.addEventListener('click', () => selectDay(iso));
      row.append(btn);
    });
    lanes.forEach((lane, laneIndex) => {
      for (const seg of lane) {
        const p = seg.plan;
        const bar = el('button', {
          type: 'button',
          class: `cal-bar type-${p.type}${seg.startCol > 0 || p.startDate >= week[0] ? ' starts' : ''}${p.endDate <= week[6] ? ' ends' : ''}`,
          title: `${p.name} (${PLAN_TYPES[p.type]})`,
          'aria-label': `${p.name}, ${PLAN_TYPES[p.type]}`
        }, el('span', { class: 'cal-bar-text' }, p.name));
        bar.style.gridColumn = `${seg.startCol + 1} / ${seg.endCol + 2}`;
        bar.style.gridRow = String(laneIndex + 2);
        bar.addEventListener('click', () => openPlan(p));
        row.append(bar);
      }
    });
    grid.append(row);
  }
  const legend = el('ul', { class: 'cal-legend', 'aria-label': 'Plan türleri' },
    Object.entries(PLAN_TYPES).map(([k, v]) => el('li', null, el('span', { class: `type-dot type-${k}`, 'aria-hidden': 'true' }), v)));
  replace(body, grid, legend);
}

function renderAgenda() {
  const from = `${state.year}-${pad2(state.month0 + 1)}-01`;
  const to = `${state.year}-${pad2(state.month0 + 1)}-${pad2(daysInMonth(state.year, state.month0))}`;
  const list = sortByStart(state.plans.filter((p) => p.status !== 'cancelled' && overlapsRange(p, from, to)));
  if (!list.length) {
    replace(body, emptyState('Bu ay için plan yok.', 'Plan ekle', () => addPlan(state.selected.startsWith(from.slice(0, 7)) ? state.selected : from), 'calendar'));
    return;
  }
  const groups = new Map();
  for (const p of list) {
    const key = p.startDate < from ? from : p.startDate;
    if (!groups.has(key)) groups.set(key, []);
    groups.get(key).push(p);
  }
  replace(body, el('div', { class: 'agenda' }, [...groups.entries()].map(([date, plans]) => el('section', { class: 'agenda-day' },
    el('h3', { class: `agenda-date${date === today ? ' is-today' : ''}` }, formatDate(date, { weekday: true }), date === today ? ' · Bugün' : ''),
    el('ul', { class: 'list' }, plans.map((p) => planRow(p, openPlan, today)))))));
}

function render() {
  titleEl.textContent = formatMonthYear(state.year, state.month0);
  if (state.view === 'agenda') {
    renderAgenda();
    dayPanel.hidden = true;
  } else {
    renderMonth();
    dayPanel.hidden = false;
    renderDayPanel();
  }
}

function shift(n) {
  const m = addMonths(state.year, state.month0, n);
  state.year = m.year;
  state.month0 = m.month0;
  const prefix = `${state.year}-${pad2(state.month0 + 1)}`;
  if (!state.selected.startsWith(prefix)) state.selected = today.startsWith(prefix) ? today : `${prefix}-01`;
  render();
}

async function load() {
  try {
    state.plans = await listRecords('plans');
    render();
  } catch (err) {
    renderLoadError(body, err, load);
  }
}

async function setup() {
  replace(main, loadingState());
  try {
    const settings = await getSingleton('settings');
    state.view = (settings && settings.calendarView) || 'month';
  } catch {
    state.view = 'month';
  }
  const toolbar = el('div', { class: 'cal-toolbar' },
    iconButton('chevronLeft', 'Önceki ay', () => shift(-1)),
    titleEl,
    iconButton('chevronRight', 'Sonraki ay', () => shift(1)),
    button('Bugün', () => {
      state.year = Number(today.slice(0, 4));
      state.month0 = Number(today.slice(5, 7)) - 1;
      state.selected = today;
      render();
    }, { className: 'btn-small' }),
    el('span', { class: 'toolbar-spacer' }),
    segmented([['month', 'Ay'], ['agenda', 'Liste']], state.view, (v) => {
      state.view = v;
      render();
    }, 'Görünüm'),
    button('Plan ekle', () => addPlan(state.selected), { kind: 'primary', iconName: 'plus', className: 'btn-small' }));
  replace(main, toolbar, el('div', { class: 'cal-layout' }, body, dayPanel));
  await load();
}

const ready = await initApp({ page: 'calendar', title: 'Takvim' });
if (ready) await setup();
