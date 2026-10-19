// Gelir ve gider: bu ay ne kadar geldi, nereye ne kadar gitti, cebimde ne var; grafikler ve birikim hedefleri.
import { initApp, renderLoadError } from '../app.js';
import { listRecords, createRecord, updateRecord, deleteRecord, restoreRecord } from '../storage/records.js';
import { el, replace, field, openDialog, toast, toastError, emptyState, loadingState, debounce, button, iconButton, segmented, showFieldErrors, clearFieldErrors, uid } from '../ui.js';
import { icon } from '../utils/icons.js';
import { TXN_TYPES, TXN_ACCOUNTS, OPENING_CATEGORY, SAVING_IN_CATEGORY, SAVING_OUT_CATEGORY } from '../utils/labels.js';
import { formatMoney, formatNumber, matchesSearch, numberToInput, parseTrNumber } from '../utils/formatters.js';
import { todayISO, formatDate, MONTHS, diffDays } from '../utils/dates.js';
import { inMonth, totals, byCategory, balances, categoriesFor, sortTxns, previousMonth, nextMonth, isOpening, monthlySeries, dailyExpenses, savedAmount, savingsSummary } from '../utils/finance-helpers.js';
import { barChart } from '../components/charts.js';
import { shortId } from '../utils/id-generator.js';
import { takeHash } from '../router.js';

const main = document.getElementById('main');
const TAB_KEY = 'jozh.financeTab';
const state = { txns: [], goals: [], month: todayISO().slice(0, 7), type: 'all', query: '', account: '', tab: readTab() };

function readTab() {
  try {
    const t = localStorage.getItem(TAB_KEY);
    return ['summary', 'charts', 'savings'].includes(t) ? t : 'summary';
  } catch {
    return 'summary';
  }
}

const monthTitle = el('h2', { class: 'fin-month', 'aria-live': 'polite' });
const summaryEl = el('section', { class: 'fin-summary', 'aria-label': 'Bu ayın özeti' });
const walletEl = el('section', { class: 'card fin-wallet', 'aria-labelledby': 'wallet-title' });
const breakdownEl = el('section', { class: 'card fin-breakdown', 'aria-labelledby': 'breakdown-title' });
const incomeEl = el('section', { class: 'card fin-income', 'aria-labelledby': 'income-title' });
const listEl = el('div', { class: 'fin-list', 'aria-live': 'polite' });
const summaryPanel = el('div', { class: 'fin-panel', id: 'panel-summary' });
const chartsPanel = el('div', { class: 'fin-panel', id: 'panel-charts' });
const savingsPanel = el('div', { class: 'fin-panel', id: 'panel-savings' });
const monthNav = el('div', { class: 'fin-monthnav' });

function monthLabel(ym) {
  const [y, m] = ym.split('-').map(Number);
  return `${MONTHS[m - 1]} ${y}`;
}

function signed(t) {
  return `${t.type === 'income' ? '+' : '−'}${formatMoney(t.amount)}`;
}

function stat(label, value, kind = '', note = '') {
  return el('div', { class: `card stat fin-stat${kind ? ` is-${kind}` : ''}` },
    el('span', { class: 'stat-label' }, label),
    el('span', { class: `stat-value${kind === 'income' ? ' text-green' : kind === 'expense' ? ' text-red' : ''}` }, value),
    note ? el('span', { class: 'stat-note small muted' }, note) : null);
}

function renderSummary() {
  const month = state.txns.filter((t) => inMonth(t, state.month));
  const prev = state.txns.filter((t) => inMonth(t, previousMonth(state.month)));
  const cur = totals(month);
  const before = totals(prev);
  let note = '';
  if (before.expense > 0) {
    const diff = cur.expense - before.expense;
    const pct = Math.round((Math.abs(diff) / before.expense) * 100);
    note = diff === 0 ? 'Geçen ayla aynı' : `Geçen aya göre %${pct} ${diff > 0 ? 'fazla' : 'az'}`;
  }
  replace(summaryEl,
    stat('Bu ay gelen', formatMoney(cur.income), 'income'),
    stat('Bu ay giden', formatMoney(cur.expense), 'expense', note),
    stat('Ay farkı', `${cur.net >= 0 ? '+' : '−'}${formatMoney(Math.abs(cur.net))}`, cur.net >= 0 ? 'positive' : 'negative', cur.net >= 0 ? 'Gelir giderden fazla' : 'Gider gelirden fazla'));
}

function renderWallet() {
  const b = balances(state.txns);
  const saved = savingsSummary(state.goals).saved;
  const rows = [
    ['Nakit (cebimde)', b.cash],
    ['Banka', b.bank],
    ['Kullanılabilir toplam', b.available]
  ];
  if (state.goals.length) rows.push(['Birikimlerde', saved], ['Toplam varlık', Math.round((b.available + saved) * 100) / 100]);
  replace(walletEl,
    el('div', { class: 'card-header' }, el('h2', { id: 'wallet-title' }, 'Cebimde ne var'), button('Bakiye gir', openOpeningDialog, { className: 'btn-small', iconName: 'wallet' })),
    el('dl', { class: 'wallet-rows' }, rows.flatMap(([k, v], i) => [
      el('dt', { class: i === 2 || i === 4 ? 'is-total' : '' }, k),
      el('dd', { class: `${i === 2 || i === 4 ? 'is-total ' : ''}${v < 0 ? 'text-red' : ''}` }, `${v < 0 ? '−' : ''}${formatMoney(Math.abs(v))}`)
    ])),
    b.cardDebt > 0 ? el('p', { class: 'notice notice-warning mt' }, icon('alert'), el('span', null, `Kredi kartı borcu: ${formatMoney(b.cardDebt)}. Net durumun: ${b.net < 0 ? '−' : ''}${formatMoney(Math.abs(b.net))}.`)) : null,
    !state.txns.some(isOpening)
      ? el('p', { class: 'muted small mt' }, 'Doğru bakiye için bir kez "Bakiye gir" ile şu an cebindeki ve bankandaki parayı yaz; sonrasında her gelir ve gider bakiyeyi kendiliğinden günceller.')
      : null);
}

function bars(list, emptyText, kind) {
  if (!list.length) return el('p', { class: 'muted small' }, emptyText);
  const max = list[0].amount || 1;
  return el('ul', { class: 'cat-bars' }, list.map((c) => {
    const fill = el('span', { class: `cat-fill ${kind}` });
    fill.style.width = `${Math.max(2, (c.amount / max) * 100)}%`;
    return el('li', { class: 'cat-row' },
      el('div', { class: 'cat-label' }, el('span', { class: 'grow' }, c.category), el('span', { class: 'cat-amount' }, formatMoney(c.amount)), el('span', { class: 'cat-pct muted small' }, `%${formatNumber(c.percent, 1)}`)),
      el('span', { class: 'cat-track', role: 'img', 'aria-label': `${c.category}: ${formatMoney(c.amount)}, yüzde ${formatNumber(c.percent, 1)}` }, fill));
  }));
}

function renderBreakdown() {
  const month = state.txns.filter((t) => inMonth(t, state.month));
  replace(breakdownEl,
    el('div', { class: 'card-header' }, el('h2', { id: 'breakdown-title' }, 'Para nereye gitti')),
    bars(byCategory(month, 'expense'), 'Bu ay gider yok.', 'expense'));
  replace(incomeEl,
    el('div', { class: 'card-header' }, el('h2', { id: 'income-title' }, 'Para nereden geldi')),
    bars(byCategory(month, 'income'), 'Bu ay gelir yok.', 'income'));
}

function renderList() {
  const month = sortTxns(state.txns.filter((t) => inMonth(t, state.month)));
  if (!state.txns.length) {
    replace(listEl, emptyState('Henüz gelir ya da gider yok. İlk kaydını ekle.', 'Gider ekle', () => openEditor(null, 'expense'), 'wallet'));
    return;
  }
  const visible = month.filter((t) => (state.type === 'all' || t.type === state.type)
    && (!state.account || t.account === state.account)
    && matchesSearch(state.query, t.category, t.note, TXN_ACCOUNTS[t.account]));
  if (!visible.length) {
    replace(listEl, el('p', { class: 'muted state' }, `${monthLabel(state.month)} için uyan kayıt yok.`));
    return;
  }
  replace(listEl, el('ul', { class: 'list txn-list' }, visible.map((t) => {
    const open = el('button', { type: 'button', class: 'open-button txn-open' },
      el('span', { class: `txn-icon ${t.type}`, 'aria-hidden': 'true' }, icon(t.type === 'income' ? 'income' : 'expense', { size: 18 })),
      el('span', { class: 'item-main' },
        el('span', { class: 'item-title' }, t.category),
        el('span', { class: 'item-meta' }, formatDate(t.date, { short: true }), el('span', null, TXN_ACCOUNTS[t.account]), t.note ? el('span', null, t.note) : null)),
      el('span', { class: `txn-amount ${t.type === 'income' ? 'text-green' : 'text-red'}` }, signed(t), el('span', { class: 'visually-hidden' }, ` ${TXN_TYPES[t.type]}`)));
    open.addEventListener('click', () => openEditor(t));
    return el('li', { class: 'list-item txn-item' }, open);
  })));
}

function render() {
  monthTitle.textContent = monthLabel(state.month);
  summaryPanel.hidden = state.tab !== 'summary';
  chartsPanel.hidden = state.tab !== 'charts';
  savingsPanel.hidden = state.tab !== 'savings';
  monthNav.hidden = state.tab === 'savings';
  if (state.tab === 'summary') {
    renderSummary();
    renderWallet();
    renderBreakdown();
    renderList();
  } else if (state.tab === 'charts') {
    renderCharts();
  } else {
    renderSavings();
  }
}

async function load() {
  try {
    state.txns = await listRecords('transactions');
    state.goals = await listRecords('savings');
    render();
  } catch (err) {
    renderLoadError(listEl, err, load);
  }
}

function openEditor(txn, presetType = 'expense') {
  const t = txn || { type: presetType, amount: null, category: '', date: state.month === todayISO().slice(0, 7) ? todayISO() : `${state.month}-01`, account: 'cash', note: '' };
  let type = t.type;
  const listId = uid('cats');
  const datalist = el('datalist', { id: listId });
  const fillCategories = () => replace(datalist, categoriesFor(type, state.txns).map((c) => el('option', { value: c })));
  fillCategories();
  const form = el('form', { class: 'form-stack', novalidate: true });
  const typeSwitch = segmented([['expense', 'Gider'], ['income', 'Gelir']], type, (v) => {
    type = v;
    fillCategories();
    const acc = form.elements.account;
    acc.querySelector('option[value="card"]').disabled = v === 'income';
    if (v === 'income' && acc.value === 'card') acc.value = 'bank';
  }, 'Kayıt türü');
  form.append(
    typeSwitch,
    el('div', { class: 'form-grid' },
      field({ label: 'Tutar (₺)', name: 'amount', value: numberToInput(t.amount), required: true, inputmode: 'decimal', placeholder: 'ör. 1.250,50' }),
      field({ label: 'Kategori', name: 'category', value: t.category, required: true, maxlength: 60, list: listId, hint: 'Listeden seç ya da yeni yaz.' }),
      field({ label: 'Tarih', name: 'date', type: 'date', value: t.date, required: true }),
      field({ label: 'Hesap', name: 'account', type: 'select', value: t.account, options: Object.entries(TXN_ACCOUNTS) })),
    field({ label: 'Açıklama', name: 'note', value: t.note, maxlength: 500, placeholder: 'ör. Haftalık market' }),
    datalist);
  form.elements.account.querySelector('option[value="card"]').disabled = type === 'income';
  const collect = () => ({
    type,
    amount: form.elements.amount.value,
    category: form.elements.category.value,
    date: form.elements.date.value,
    account: form.elements.account.value,
    note: form.elements.note.value
  });
  const initial = JSON.stringify(collect());

  async function save(dlg) {
    clearFieldErrors(form);
    try {
      if (txn) await updateRecord('transactions', txn.id, collect());
      else await createRecord('transactions', collect());
      await dlg.close(true);
      toast(txn ? 'Kayıt güncellendi.' : `${type === 'income' ? 'Gelir' : 'Gider'} eklendi.`, { kind: 'success' });
      load();
    } catch (err) {
      if (err.fields) showFieldErrors(form, err.fields);
      else toastError('finance.save', err, () => save(dlg));
    }
  }
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    save(dlg);
  });

  const actions = [];
  if (txn) {
    actions.push({
      label: 'Sil', kind: 'danger', icon: 'trash', className: 'mr-auto',
      onClick: async (d) => {
        try {
          await deleteRecord('transactions', txn.id);
          await d.close(true);
          toast('Kayıt silindi.', { actionLabel: 'Geri al', onAction: async () => { await restoreRecord('transactions', txn.id); load(); } });
          load();
        } catch (err) {
          toastError('finance.delete', err);
        }
      }
    });
  }
  actions.push({ label: 'Vazgeç', onClick: (d) => d.close() });
  actions.push({ label: 'Kaydet', kind: 'primary', onClick: (d) => save(d) });
  const dlg = openDialog({
    title: txn ? 'Kaydı düzenle' : (presetType === 'income' ? 'Gelir ekle' : 'Gider ekle'),
    content: form,
    actions,
    isDirty: () => JSON.stringify(collect()) !== initial
  });
  return dlg;
}

function openOpeningDialog() {
  const b = balances(state.txns);
  const form = el('form', { class: 'form-stack', novalidate: true },
    el('p', { class: 'muted small' }, `Şu an cebinde ve bankanda gerçekte ne kadar para var? Fark, "${OPENING_CATEGORY}" olarak kaydedilir ve aylık gelire sayılmaz.`),
    el('div', { class: 'form-grid' },
      field({ label: 'Nakit (₺)', name: 'cash', value: numberToInput(b.cash), inputmode: 'decimal' }),
      field({ label: 'Banka (₺)', name: 'bank', value: numberToInput(b.bank), inputmode: 'decimal' })));
  form.addEventListener('submit', (e) => e.preventDefault());
  openDialog({
    title: 'Bakiye gir',
    content: form,
    size: 'sm',
    actions: [
      { label: 'Vazgeç', onClick: (d) => d.close() },
      {
        label: 'Kaydet',
        kind: 'primary',
        onClick: async (d) => {
          clearFieldErrors(form);
          const errors = {};
          const want = {};
          for (const acc of ['cash', 'bank']) {
            const v = parseTrNumber(form.elements[acc].value);
            if (v === null) want[acc] = b[acc];
            else if (!Number.isFinite(v)) errors[acc] = 'Geçerli bir tutar yaz (ör. 1.500 ya da 250,75).';
            else want[acc] = v;
          }
          if (Object.keys(errors).length) {
            showFieldErrors(form, errors);
            return;
          }
          try {
            for (const acc of ['cash', 'bank']) {
              const diff = Math.round((want[acc] - b[acc]) * 100) / 100;
              if (diff === 0) continue;
              await createRecord('transactions', {
                type: diff > 0 ? 'income' : 'expense',
                amount: Math.abs(diff),
                category: OPENING_CATEGORY,
                date: todayISO(),
                account: acc,
                note: 'Bakiye düzeltmesi'
              });
            }
            await d.close(true);
            toast('Bakiye güncellendi.', { kind: 'success' });
            load();
          } catch (err) {
            toastError('finance.opening', err);
          }
        }
      }
    ]
  });
}

// --- Grafikler ---

const SERIES = [
  { key: 'income', name: 'Gelen', className: 'series-income' },
  { key: 'expense', name: 'Giden', className: 'series-expense' }
];

function shortMonth(ym) {
  return MONTHS[Number(ym.slice(5, 7)) - 1].slice(0, 3);
}

function renderCharts() {
  const months = monthlySeries(state.txns, state.month, 6);
  const withData = months.filter((m) => m.income || m.expense);
  const days = dailyExpenses(state.txns, state.month);
  const monthTotal = days.reduce((sum, d) => sum + d.amount, 0);
  const top = days.reduce((best, d) => (d.amount > best.amount ? d : best), { day: 0, amount: 0 });
  const avgExpense = withData.length ? withData.reduce((sum, m) => sum + m.expense, 0) / withData.length : 0;
  const avgIncome = withData.length ? withData.reduce((sum, m) => sum + m.income, 0) / withData.length : 0;

  const monthsCard = el('section', { class: 'card chart-card', 'aria-labelledby': 'chart6-title' },
    el('div', { class: 'card-header' }, el('h2', { id: 'chart6-title' }, 'Son 6 ay: gelen ve giden')));
  if (!withData.length) {
    monthsCard.append(el('p', { class: 'muted small' }, 'Bu ay ve önceki 5 ayda kayıt yok.'));
  } else {
    monthsCard.append(
      barChart({
        title: 'Son 6 ayın aylık gelen ve giden tutarları',
        tableCaption: 'Son 6 ay: gelen ve giden',
        rowHeader: 'Ay',
        series: SERIES,
        format: formatMoney,
        groups: months.map((m) => ({
          label: shortMonth(m.month),
          title: monthLabel(m.month),
          values: { income: m.income, expense: m.expense },
          note: `Fark: ${m.net >= 0 ? '+' : '−'}${formatMoney(Math.abs(m.net))}`
        }))
      }),
      el('dl', { class: 'chart-facts' },
        el('dt', null, 'Aylık ortalama gelen'), el('dd', null, formatMoney(Math.round(avgIncome))),
        el('dt', null, 'Aylık ortalama giden'), el('dd', null, formatMoney(Math.round(avgExpense)))));
  }

  const dailyCard = el('section', { class: 'card chart-card', 'aria-labelledby': 'chartd-title' },
    el('div', { class: 'card-header' }, el('h2', { id: 'chartd-title' }, `${monthLabel(state.month)}: günlük harcama`)));
  if (!monthTotal) {
    dailyCard.append(el('p', { class: 'muted small' }, 'Bu ay gider yok.'));
  } else {
    const [y, m] = state.month.split('-').map(Number);
    const daysPassed = state.month === todayISO().slice(0, 7) ? Number(todayISO().slice(8, 10)) : days.length;
    dailyCard.append(
      barChart({
        title: `${monthLabel(state.month)} ayında günlere göre harcama`,
        tableCaption: 'Günlük harcama',
        rowHeader: 'Gün',
        series: [{ key: 'expense', name: 'Giden', className: 'series-expense' }],
        format: formatMoney,
        height: 200,
        groups: days.map((d) => ({
          label: String(d.day),
          title: formatDate(`${y}-${String(m).padStart(2, '0')}-${String(d.day).padStart(2, '0')}`, { weekday: true }),
          values: { expense: d.amount }
        }))
      }),
      el('dl', { class: 'chart-facts' },
        el('dt', null, 'Bu ay toplam'), el('dd', null, formatMoney(monthTotal)),
        el('dt', null, 'Günlük ortalama'), el('dd', null, formatMoney(Math.round(monthTotal / Math.max(1, daysPassed)))),
        el('dt', null, 'En çok harcanan gün'), el('dd', null, `${top.day} ${MONTHS[m - 1]} · ${formatMoney(top.amount)}`)));
  }
  replace(chartsPanel, el('div', { class: 'fin-charts' }, monthsCard, dailyCard));
}

// --- Birikim hedefleri ---

function monthsLeft(targetDate) {
  const days = diffDays(todayISO(), targetDate);
  return days <= 0 ? 0 : Math.max(1, Math.ceil(days / 30.44));
}

function goalCard(goal) {
  const saved = savedAmount(goal);
  const pct = Math.min(100, Math.round((saved / goal.targetAmount) * 100));
  const remaining = Math.max(0, Math.round((goal.targetAmount - saved) * 100) / 100);
  const reached = saved >= goal.targetAmount;
  let plan = null;
  if (!reached && goal.targetDate) {
    const ml = monthsLeft(goal.targetDate);
    plan = ml === 0
      ? el('p', { class: 'small text-red' }, `Hedef tarihi geçti (${formatDate(goal.targetDate)}); kalan ${formatMoney(remaining)}.`)
      : el('p', { class: 'small muted' }, `Hedef: ${formatDate(goal.targetDate)} · ayda yaklaşık ${formatMoney(Math.ceil(remaining / ml))} biriktirmelisin (${ml} ay).`);
  } else if (goal.targetDate && reached) {
    plan = el('p', { class: 'small muted' }, `Hedef tarihi: ${formatDate(goal.targetDate)}`);
  }
  const history = (goal.contributions || []).slice().sort((a, b) => b.date.localeCompare(a.date));
  return el('li', { class: 'card goal-card' },
    el('div', { class: 'card-header' },
      el('h3', { class: 'goal-title' }, goal.title),
      reached ? el('span', { class: 'chip chip-green' }, 'Hedefe ulaşıldı') : null,
      iconButton('edit', `${goal.title} hedefini düzenle`, () => openGoalEditor(goal))),
    el('p', { class: 'goal-amounts' }, el('strong', null, formatMoney(saved)), el('span', { class: 'muted' }, ` / ${formatMoney(goal.targetAmount)}`)),
    el('div', { class: 'progress-row' },
      (() => {
        const bar = el('div', { class: 'progress', role: 'progressbar', 'aria-valuemin': '0', 'aria-valuemax': '100', 'aria-valuenow': String(pct), 'aria-label': `${goal.title} birikimi` }, el('div', { class: 'progress-fill' }));
        bar.firstChild.style.width = `${pct}%`;
        return bar;
      })(),
      el('span', { class: 'small' }, `%${pct}`)),
    reached ? null : el('p', { class: 'small' }, `Kalan: ${formatMoney(remaining)}`),
    plan,
    goal.note ? el('p', { class: 'small muted' }, goal.note) : null,
    el('div', { class: 'row mt' },
      button('Para ekle', () => openContribution(goal, 1), { kind: 'primary', iconName: 'plus', className: 'btn-small' }),
      saved > 0 ? button('Para çek', () => openContribution(goal, -1), { iconName: 'expense', className: 'btn-small' }) : null),
    history.length ? el('details', { class: 'goal-history mt' },
      el('summary', null, `Hareketler (${history.length})`),
      el('ul', { class: 'compact-list' }, history.map((c) => el('li', null,
        el('div', { class: 'grow' },
          el('p', { class: `${c.amount > 0 ? 'text-green' : 'text-red'}` }, `${c.amount > 0 ? '+' : '−'}${formatMoney(Math.abs(c.amount))}`),
          el('p', { class: 'muted small' }, `${formatDate(c.date, { short: true })}${c.note ? ` · ${c.note}` : ''}${c.txnId ? ' · bakiyeden' : ''}`)),
        iconButton('trash', 'Bu hareketi sil', () => removeContribution(goal, c)))))) : null);
}

function renderSavings() {
  const sum = savingsSummary(state.goals);
  const head = el('div', { class: 'row savings-head' },
    el('div', { class: 'stats grow' },
      el('div', { class: 'card stat' }, el('span', { class: 'stat-label' }, 'Toplam biriken'), el('span', { class: 'stat-value' }, formatMoney(sum.saved))),
      el('div', { class: 'card stat' }, el('span', { class: 'stat-label' }, 'Hedeflerin toplamı'), el('span', { class: 'stat-value' }, formatMoney(sum.target))),
      el('div', { class: 'card stat' }, el('span', { class: 'stat-label' }, 'Ulaşılan hedef'), el('span', { class: 'stat-value' }, `${sum.reached} / ${sum.count}`))));
  const add = el('div', { class: 'row mt' }, button('Yeni birikim hedefi', () => openGoalEditor(null), { kind: 'primary', iconName: 'plus' }));
  if (!state.goals.length) {
    replace(savingsPanel, emptyState('Henüz birikim hedefi yok. Ör. "Araba için 200.000 ₺" gibi bir hedef ekle; para ayırdıkça ilerlemesini gör.', 'Birikim hedefi ekle', () => openGoalEditor(null), 'target'));
    return;
  }
  const sorted = state.goals.slice().sort((a, b) => {
    const ar = savedAmount(a) >= a.targetAmount;
    const br = savedAmount(b) >= b.targetAmount;
    if (ar !== br) return ar ? 1 : -1;
    return (a.targetDate || '9999').localeCompare(b.targetDate || '9999') || a.createdAt.localeCompare(b.createdAt);
  });
  replace(savingsPanel, head, add, el('ul', { class: 'card-grid goals mt' }, sorted.map(goalCard)));
}

function openGoalEditor(goal) {
  const g = goal || { title: '', targetAmount: null, targetDate: '', note: '' };
  const form = el('form', { class: 'form-stack', novalidate: true },
    el('div', { class: 'form-grid' },
      field({ label: 'Hedefin adı', name: 'title', value: g.title, required: true, maxlength: 100, placeholder: 'ör. Araba' }),
      field({ label: 'Hedef tutar (₺)', name: 'targetAmount', value: numberToInput(g.targetAmount), required: true, inputmode: 'decimal', placeholder: 'ör. 200.000' }),
      field({ label: 'Hedef tarihi (isteğe bağlı)', name: 'targetDate', type: 'date', value: g.targetDate })),
    field({ label: 'Not', name: 'note', value: g.note, maxlength: 500 }));
  form.addEventListener('submit', (e) => e.preventDefault());
  const collect = () => ({ title: form.elements.title.value, targetAmount: form.elements.targetAmount.value, targetDate: form.elements.targetDate.value, note: form.elements.note.value });
  const initial = JSON.stringify(collect());
  const actions = [];
  if (goal) {
    actions.push({
      label: 'Sil', kind: 'danger', icon: 'trash', className: 'mr-auto',
      onClick: async (d) => {
        try {
          await deleteRecord('savings', goal.id);
          await d.close(true);
          toast('Birikim hedefi silindi. Hedefe bağlı bakiye hareketleri olduğu gibi kaldı.', { actionLabel: 'Geri al', onAction: async () => { await restoreRecord('savings', goal.id); load(); } });
          load();
        } catch (err) {
          toastError('savings.delete', err);
        }
      }
    });
  }
  actions.push({ label: 'Vazgeç', onClick: (d) => d.close() });
  actions.push({
    label: 'Kaydet',
    kind: 'primary',
    onClick: async (d) => {
      clearFieldErrors(form);
      try {
        if (goal) await updateRecord('savings', goal.id, collect());
        else await createRecord('savings', { ...collect(), contributions: [] });
        await d.close(true);
        toast(goal ? 'Hedef güncellendi.' : 'Birikim hedefi eklendi.', { kind: 'success' });
        load();
      } catch (err) {
        if (err.fields) showFieldErrors(form, err.fields);
        else toastError('savings.save', err);
      }
    }
  });
  openDialog({ title: goal ? 'Birikim hedefini düzenle' : 'Yeni birikim hedefi', content: form, actions, isDirty: () => JSON.stringify(collect()) !== initial });
}

// direction: 1 = para ekle, -1 = para çek
function openContribution(goal, direction) {
  const saved = savedAmount(goal);
  const adding = direction > 0;
  const form = el('form', { class: 'form-stack', novalidate: true },
    el('p', { class: 'small muted' }, `${goal.title}: şu an ${formatMoney(saved)} birikti.`),
    el('div', { class: 'form-grid' },
      field({ label: 'Tutar (₺)', name: 'amount', required: true, inputmode: 'decimal', placeholder: 'ör. 2.500' }),
      field({ label: 'Tarih', name: 'date', type: 'date', value: todayISO(), required: true })),
    field({ label: 'Açıklama', name: 'note', maxlength: 200 }),
    field({ label: adding ? 'Bu tutarı nakit ya da bankadan düş' : 'Bu tutarı nakit ya da bankaya ekle', name: 'linked', type: 'checkbox', value: true,
      hint: adding ? 'İşaretliyse "Cebimde ne var" bakiyen azalır; aylık gidere sayılmaz.' : 'İşaretliyse "Cebimde ne var" bakiyen artar; aylık gelire sayılmaz.' }),
    field({ label: 'Hesap', name: 'account', type: 'select', value: 'bank', options: [['bank', TXN_ACCOUNTS.bank], ['cash', TXN_ACCOUNTS.cash]] }));
  form.addEventListener('submit', (e) => e.preventDefault());
  const accountField = form.elements.account.closest('.field');
  form.elements.linked.addEventListener('change', () => {
    accountField.hidden = !form.elements.linked.checked;
  });
  openDialog({
    title: adding ? 'Birikime para ekle' : 'Birikimden para çek',
    content: form,
    size: 'sm',
    actions: [
      { label: 'Vazgeç', onClick: (d) => d.close() },
      {
        label: adding ? 'Ekle' : 'Çek',
        kind: 'primary',
        onClick: async (d) => {
          clearFieldErrors(form);
          const amount = parseTrNumber(form.elements.amount.value);
          if (amount === null || !Number.isFinite(amount) || amount <= 0) {
            showFieldErrors(form, { amount: 'Sıfırdan büyük bir tutar yaz (ör. 2.500 ya da 750,50).' });
            return;
          }
          if (!adding && amount > saved) {
            showFieldErrors(form, { amount: `En çok ${formatMoney(saved)} çekebilirsin.` });
            return;
          }
          const date = form.elements.date.value;
          const note = form.elements.note.value.trim();
          let txnId = '';
          try {
            if (form.elements.linked.checked) {
              const txn = await createRecord('transactions', {
                type: adding ? 'expense' : 'income',
                amount,
                category: adding ? SAVING_IN_CATEGORY : SAVING_OUT_CATEGORY,
                date,
                account: form.elements.account.value,
                note: note ? `${goal.title}: ${note}` : goal.title
              });
              txnId = txn.id;
            }
            const contributions = [...(goal.contributions || []), { id: shortId(), date, amount: adding ? amount : -amount, note, txnId }];
            await updateRecord('savings', goal.id, { contributions });
            await d.close(true);
            toast(adding ? `${formatMoney(amount)} birikime eklendi.` : `${formatMoney(amount)} birikimden çekildi.`, { kind: 'success' });
            load();
          } catch (err) {
            if (txnId) await deleteRecord('transactions', txnId).catch(() => {});
            if (err.fields) showFieldErrors(form, err.fields);
            else toastError('savings.contribution', err);
          }
        }
      }
    ]
  });
}

async function removeContribution(goal, c) {
  try {
    const contributions = (goal.contributions || []).filter((x) => x.id !== c.id);
    await updateRecord('savings', goal.id, { contributions });
    if (c.txnId) await deleteRecord('transactions', c.txnId).catch(() => {});
    toast('Hareket silindi.', {
      actionLabel: 'Geri al',
      onAction: async () => {
        const fresh = state.goals.find((g) => g.id === goal.id) || goal;
        await updateRecord('savings', goal.id, { contributions: [...(fresh.contributions || []), c] });
        if (c.txnId) await restoreRecord('transactions', c.txnId).catch(() => {});
        load();
      }
    });
    load();
  } catch (err) {
    toastError('savings.removeContribution', err);
  }
}

async function setup() {
  replace(main, loadingState());
  const search = el('input', { type: 'search', class: 'input', id: 'fin-search', placeholder: 'Kategori ya da açıklama', autocomplete: 'off' });
  search.addEventListener('input', debounce(() => {
    state.query = search.value;
    renderList();
  }, 150));
  const accSel = el('select', { class: 'input select', id: 'fin-account' }, el('option', { value: '' }, 'Bütün hesaplar'), Object.entries(TXN_ACCOUNTS).map(([v, l]) => el('option', { value: v }, l)));
  accSel.addEventListener('change', () => {
    state.account = accSel.value;
    renderList();
  });
  const goMonth = (ym) => {
    state.month = ym;
    render();
  };
  replace(monthNav,
    iconButton('chevronLeft', 'Önceki ay', () => goMonth(previousMonth(state.month))),
    monthTitle,
    iconButton('chevronRight', 'Sonraki ay', () => goMonth(nextMonth(state.month))),
    button('Bu ay', () => goMonth(todayISO().slice(0, 7)), { className: 'btn-small' }));
  const tabs = segmented([['summary', 'Özet'], ['charts', 'Grafikler'], ['savings', 'Birikim']], state.tab, (v) => {
    state.tab = v;
    try {
      localStorage.setItem(TAB_KEY, v);
    } catch {
      // yok say
    }
    render();
  }, 'Bölüm');
  tabs.classList.add('fin-tabs');
  replace(summaryPanel,
    summaryEl,
    el('div', { class: 'fin-grid' }, walletEl, breakdownEl, incomeEl),
    el('section', { class: 'fin-history', 'aria-labelledby': 'history-title' },
      el('h2', { id: 'history-title', class: 'section-heading' }, 'Hareketler'),
      el('div', { class: 'page-toolbar' },
        segmented([['all', 'Tümü'], ['income', 'Gelir'], ['expense', 'Gider']], state.type, (v) => {
          state.type = v;
          renderList();
        }, 'Tür süzgeci'),
        el('div', { class: 'field search' }, el('label', { class: 'field-label', for: 'fin-search' }, 'Ara'), search),
        el('div', { class: 'field' }, el('label', { class: 'field-label', for: 'fin-account' }, 'Hesap'), accSel)),
      listEl));
  replace(main,
    el('div', { class: 'fin-toolbar' },
      monthNav,
      el('span', { class: 'toolbar-spacer' }),
      button('Gelir ekle', () => openEditor(null, 'income'), { iconName: 'income', className: 'btn-income' }),
      button('Gider ekle', () => openEditor(null, 'expense'), { kind: 'primary', iconName: 'expense' })),
    tabs,
    summaryPanel,
    chartsPanel,
    savingsPanel);
  await load();
  if (takeHash('new')) openEditor(null, 'expense');
}

const ready = await initApp({ page: 'finance', title: 'Gelir ve gider' });
if (ready) await setup();
