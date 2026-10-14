// Planlar ve seyahatler: süzgeç (yaklaşan ve süren / geçmiş / tümü), tür, arama, kalan gün, bütçe.
import { initApp, renderLoadError } from '../app.js';
import { listRecords, updateRecord } from '../storage/records.js';
import { el, replace, emptyState, loadingState, debounce, chip, button, segmented, toastError } from '../ui.js';
import { PLAN_TYPES, PLAN_STATUS } from '../utils/labels.js';
import { matchesSearch } from '../utils/formatters.js';
import { todayISO } from '../utils/dates.js';
import { isUpcomingOrOngoing, timingLabel, formatPlanRange, budgetLabel, sortByStart } from '../utils/plan-helpers.js';
import { openPlanEditor } from '../components/plan-editor.js';
import { checkListView } from '../components/list-editor.js';
import { planTypeMarker } from '../components/day-plans.js';
import { takeHash } from '../router.js';

const main = document.getElementById('main');
const state = { plans: [], query: '', filter: 'upcoming', type: '' };
const listEl = el('div', { class: 'plans-list', 'aria-live': 'polite' });

function visiblePlans() {
  const today = todayISO();
  let list = state.plans.filter((p) => (!state.type || p.type === state.type)
    && matchesSearch(state.query, p.name, p.location, p.description, p.notes, p.trip && p.trip.city));
  if (state.filter === 'upcoming') list = sortByStart(list.filter((p) => isUpcomingOrOngoing(p, today)));
  else if (state.filter === 'past') list = sortByStart(list.filter((p) => !isUpcomingOrOngoing(p, today))).reverse();
  else list = sortByStart(list).reverse();
  return list;
}

function planCard(p) {
  const today = todayISO();
  const t = timingLabel(p, today);
  const budget = budgetLabel(p);
  const open = el('button', { type: 'button', class: 'open-button' },
    el('span', { class: 'item-title' }, p.name),
    el('span', { class: 'item-meta' },
      el('span', { class: 'row type-label' }, planTypeMarker(p.type), PLAN_TYPES[p.type]),
      el('span', null, formatPlanRange(p))));
  open.addEventListener('click', () => openPlanEditor({ plan: p, onSaved: load, onDeleted: load }));
  const doneCount = p.checklist.filter((c) => c.done).length;
  return el('li', { class: `card plan-card${p.status === 'cancelled' ? ' is-cancelled' : ''}` },
    open,
    el('div', { class: 'chips mt' },
      chip(t.text, { kind: t.kind }),
      p.status !== 'planned' ? chip(PLAN_STATUS[p.status], { kind: p.status === 'completed' ? 'green' : 'red' }) : null,
      p.trip && p.trip.city ? chip(p.trip.city, { kind: 'accent' }) : null),
    p.location ? el('p', { class: 'muted small mt' }, p.location) : null,
    budget ? el('p', { class: 'small mt' }, budget) : null,
    p.checklist.length ? el('details', { class: 'mt plan-checklist' },
      el('summary', null, `Hazırlık: ${doneCount}/${p.checklist.length}`),
      checkListView(p.checklist, async (id, done) => {
        try {
          const checklist = p.checklist.map((c) => (c.id === id ? { ...c, done } : c));
          const saved = await updateRecord('plans', p.id, { checklist });
          p.checklist = saved.checklist;
          p.updatedAt = saved.updatedAt;
          p.version = saved.version;
        } catch (err) {
          toastError('plans.check', err);
          throw err;
        }
      })) : null);
}

function render() {
  if (!state.plans.length) {
    replace(listEl, emptyState('Henüz plan yok.', 'Yeni plan', () => openPlanEditor({ onSaved: load }), 'map'));
    return;
  }
  const visible = visiblePlans();
  if (!visible.length) {
    const msg = state.filter === 'upcoming' ? 'Yaklaşan ya da süren plan yok.' : 'Bu süzgece uyan plan yok.';
    replace(listEl, emptyState(msg, null, null, 'search'));
    return;
  }
  replace(listEl, el('ul', { class: 'card-grid' }, visible.map(planCard)));
}

async function load() {
  replace(listEl, loadingState());
  try {
    state.plans = await listRecords('plans');
    render();
  } catch (err) {
    renderLoadError(listEl, err, load);
  }
}

async function setup() {
  const search = el('input', { type: 'search', class: 'input', id: 'plans-search', placeholder: 'Planlarda ara', autocomplete: 'off' });
  search.addEventListener('input', debounce(() => {
    state.query = search.value;
    render();
  }, 150));
  const typeSel = el('select', { class: 'input select', id: 'plans-type' },
    el('option', { value: '' }, 'Bütün türler'),
    Object.entries(PLAN_TYPES).map(([v, l]) => el('option', { value: v }, l)));
  typeSel.addEventListener('change', () => {
    state.type = typeSel.value;
    render();
  });
  replace(main,
    el('div', { class: 'page-toolbar' },
      el('div', { class: 'field search' }, el('label', { class: 'field-label', for: 'plans-search' }, 'Ara'), search),
      el('div', { class: 'field' }, el('label', { class: 'field-label', for: 'plans-type' }, 'Tür'), typeSel),
      button('Yeni plan', () => openPlanEditor({ onSaved: load }), { kind: 'primary', iconName: 'plus' })),
    el('div', { class: 'row filter-row' },
      segmented([['upcoming', 'Yaklaşan ve süren'], ['past', 'Geçmiş'], ['all', 'Tümü']], state.filter, (v) => {
        state.filter = v;
        render();
      }, 'Zaman süzgeci')),
    listEl);
  await load();
  if (takeHash('new')) openPlanEditor({ onSaved: load });
}

const ready = await initApp({ page: 'plans', title: 'Planlar ve seyahatler' });
if (ready) await setup();
