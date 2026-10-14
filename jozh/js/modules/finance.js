// Gelir ve gider: bu ay ne kadar geldi, nereye ne kadar gitti, cebimde ne var.
import { initApp, renderLoadError } from '../app.js';
import { listRecords, createRecord, updateRecord, deleteRecord, restoreRecord } from '../storage/records.js';
import { el, replace, field, openDialog, toast, toastError, emptyState, loadingState, debounce, button, iconButton, segmented, showFieldErrors, clearFieldErrors, uid } from '../ui.js';
import { icon } from '../utils/icons.js';
import { TXN_TYPES, TXN_ACCOUNTS, OPENING_CATEGORY } from '../utils/labels.js';
import { formatMoney, formatNumber, matchesSearch, numberToInput, parseTrNumber } from '../utils/formatters.js';
import { todayISO, formatDate, MONTHS } from '../utils/dates.js';
import { inMonth, totals, byCategory, balances, categoriesFor, sortTxns, previousMonth, nextMonth, isOpening } from '../utils/finance-helpers.js';
import { takeHash } from '../router.js';

const main = document.getElementById('main');
const state = { txns: [], month: todayISO().slice(0, 7), type: 'all', query: '', account: '' };

const monthTitle = el('h2', { class: 'fin-month', 'aria-live': 'polite' });
const summaryEl = el('section', { class: 'fin-summary', 'aria-label': 'Bu ayın özeti' });
const walletEl = el('section', { class: 'card fin-wallet', 'aria-labelledby': 'wallet-title' });
const breakdownEl = el('section', { class: 'card fin-breakdown', 'aria-labelledby': 'breakdown-title' });
const incomeEl = el('section', { class: 'card fin-income', 'aria-labelledby': 'income-title' });
const listEl = el('div', { class: 'fin-list', 'aria-live': 'polite' });

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
  const rows = [
    ['Nakit (cebimde)', b.cash],
    ['Banka', b.bank],
    ['Kullanılabilir toplam', b.available]
  ];
  replace(walletEl,
    el('div', { class: 'card-header' }, el('h2', { id: 'wallet-title' }, 'Cebimde ne var'), button('Bakiye gir', openOpeningDialog, { className: 'btn-small', iconName: 'wallet' })),
    el('dl', { class: 'wallet-rows' }, rows.flatMap(([k, v], i) => [
      el('dt', { class: i === 2 ? 'is-total' : '' }, k),
      el('dd', { class: `${i === 2 ? 'is-total ' : ''}${v < 0 ? 'text-red' : ''}` }, `${v < 0 ? '−' : ''}${formatMoney(Math.abs(v))}`)
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
  renderSummary();
  renderWallet();
  renderBreakdown();
  renderList();
}

async function load() {
  try {
    state.txns = await listRecords('transactions');
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
  replace(main,
    el('div', { class: 'fin-toolbar' },
      iconButton('chevronLeft', 'Önceki ay', () => goMonth(previousMonth(state.month))),
      monthTitle,
      iconButton('chevronRight', 'Sonraki ay', () => goMonth(nextMonth(state.month))),
      button('Bu ay', () => goMonth(todayISO().slice(0, 7)), { className: 'btn-small' }),
      el('span', { class: 'toolbar-spacer' }),
      button('Gelir ekle', () => openEditor(null, 'income'), { iconName: 'income', className: 'btn-income' }),
      button('Gider ekle', () => openEditor(null, 'expense'), { kind: 'primary', iconName: 'expense' })),
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
  await load();
  if (takeHash('new')) openEditor(null, 'expense');
}

const ready = await initApp({ page: 'finance', title: 'Gelir ve gider' });
if (ready) await setup();
