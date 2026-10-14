// Gelir ve gider hesapları: aylık toplamlar, kategori dağılımı, hesap bakiyeleri.
import { INCOME_CATEGORIES, EXPENSE_CATEGORIES, OPENING_CATEGORY } from './labels.js';

export function isOpening(txn) {
  return txn.category === OPENING_CATEGORY;
}

function round2(n) {
  return Math.round(n * 100) / 100;
}

export function inMonth(txn, ym) {
  return txn.date && txn.date.slice(0, 7) === ym;
}

export function totals(txns) {
  let income = 0;
  let expense = 0;
  for (const t of txns) {
    if (isOpening(t)) continue;
    if (t.type === 'income') income += Number(t.amount) || 0;
    else expense += Number(t.amount) || 0;
  }
  return { income: round2(income), expense: round2(expense), net: round2(income - expense) };
}

// Giderlerin kategoriye göre dağılımı (büyükten küçüğe), yüzdeleriyle.
export function byCategory(txns, type = 'expense') {
  const map = new Map();
  let total = 0;
  for (const t of txns) {
    if (t.type !== type || isOpening(t)) continue;
    const amount = Number(t.amount) || 0;
    total += amount;
    map.set(t.category, (map.get(t.category) || 0) + amount);
  }
  return [...map.entries()]
    .map(([category, amount]) => ({ category, amount: round2(amount), percent: total ? Math.round((amount / total) * 1000) / 10 : 0 }))
    .sort((a, b) => b.amount - a.amount);
}

// Cebimde ne var: nakit ve banka bakiyesi, kredi kartı borcu.
// Kart borcu = kartla yapılan giderler − nakit/bankadan yapılan "Kart ödemesi" giderleri.
export function balances(txns) {
  let cash = 0;
  let bank = 0;
  let cardSpent = 0;
  let cardPaid = 0;
  for (const t of txns) {
    const amount = Number(t.amount) || 0;
    const sign = t.type === 'income' ? 1 : -1;
    if (t.account === 'cash') cash += sign * amount;
    else if (t.account === 'bank') bank += sign * amount;
    else if (t.account === 'card' && t.type === 'expense') cardSpent += amount;
    if (t.type === 'expense' && t.category === 'Kart ödemesi' && t.account !== 'card') cardPaid += amount;
  }
  const cardDebt = round2(cardSpent - cardPaid);
  return {
    cash: round2(cash),
    bank: round2(bank),
    cardDebt,
    available: round2(cash + bank),
    net: round2(cash + bank - Math.max(0, cardDebt))
  };
}

export function categoriesFor(type, txns = []) {
  const base = type === 'income' ? [...INCOME_CATEGORIES, OPENING_CATEGORY] : EXPENSE_CATEGORIES;
  const used = txns.filter((t) => t.type === type).map((t) => t.category);
  return [...new Set([...base, ...used])];
}

export function sortTxns(txns) {
  return txns.slice().sort((a, b) => b.date.localeCompare(a.date) || b.createdAt.localeCompare(a.createdAt));
}

export function previousMonth(ym) {
  const [y, m] = ym.split('-').map(Number);
  const d = new Date(y, m - 2, 1);
  return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}`;
}

export function nextMonth(ym) {
  const [y, m] = ym.split('-').map(Number);
  const d = new Date(y, m, 1);
  return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}`;
}
