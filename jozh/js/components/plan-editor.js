// Plan düzenleyici (Planlar, Takvim ve Ana panel ortak).
import { el, field, openDialog, showFieldErrors, clearFieldErrors, toast, toastError, iconButton, button, uid } from '../ui.js';
import { createRecord, updateRecord, deleteRecord, restoreRecord } from '../storage/records.js';
import { PLAN_TYPES, PLAN_STATUS } from '../utils/labels.js';
import { createListEditor } from './list-editor.js';
import { parseTrNumber, numberToInput, formatMoney } from '../utils/formatters.js';
import { shortId } from '../utils/id-generator.js';
import { todayISO } from '../utils/dates.js';

function moneyField(label, name, value, opts = {}) {
  return field({ label, name, value: numberToInput(value), inputmode: 'decimal', placeholder: 'ör. 1.500', hint: opts.hint, disabled: opts.disabled });
}

function expenseRow(exp, onInput) {
  const row = el('tr', { dataset: { id: exp.id || shortId() } });
  const nameId = uid('exp');
  const mk = (cls, value, label, mode) => {
    const input = el('input', { type: 'text', class: `input ${cls}`, value, 'aria-label': label, inputmode: mode });
    input.addEventListener('input', onInput);
    return input;
  };
  row.append(
    el('td', null, mk('exp-name', exp.name || '', 'Masraf adı'), el('p', { class: 'field-error', id: `${nameId}-error`, hidden: true })),
    el('td', null, mk('exp-est', numberToInput(exp.estimated), 'Tahmini tutar', 'decimal')),
    el('td', null, mk('exp-act', numberToInput(exp.actual), 'Gerçekleşen tutar', 'decimal')),
    el('td', null, iconButton('trash', 'Masrafı sil', () => {
      row.remove();
      onInput();
    })));
  return row;
}

// options: { plan, defaults: { startDate }, onSaved(plan), onDeleted(plan) }
export function openPlanEditor({ plan = null, defaults = {}, onSaved, onDeleted } = {}) {
  const p = plan || {
    name: '', type: 'personal', status: 'planned', startDate: defaults.startDate || todayISO(), startTime: '', endDate: defaults.startDate || '',
    endTime: '', location: '', description: '', budget: null, spent: null, checklist: [], notes: '', trip: null
  };
  const trip = p.trip || { city: '', places: [], accommodation: '', transport: '', expenses: [] };

  const form = el('form', { class: 'form-stack plan-form', novalidate: true });
  const typeField = field({ label: 'Tür', name: 'type', type: 'select', value: p.type, options: Object.entries(PLAN_TYPES) });
  const spentField = moneyField('Harcama (₺)', 'spent', p.spent, { hint: p.type === 'trip' ? 'Seyahatte masraf tablosundaki gerçekleşen toplamdır.' : '' });
  const budgetField = moneyField('Bütçe (₺)', 'budget', p.budget);

  const checklist = createListEditor({ label: 'Hazırlık listesi', items: p.checklist || [], checkable: true, placeholder: 'ör. Pasaportu al' });
  const places = createListEditor({ label: 'Gidilecek yerler', items: trip.places || [], checkable: true, placeholder: 'ör. Galata Kulesi' });

  const tbody = el('tbody');
  const totalsEl = el('div', { class: 'stats trip-totals', 'aria-live': 'polite' });
  function recompute() {
    let est = 0;
    let act = 0;
    for (const row of tbody.children) {
      est += parseTrNumber(row.querySelector('.exp-est').value) || 0;
      act += parseTrNumber(row.querySelector('.exp-act').value) || 0;
    }
    const budget = parseTrNumber(form.elements.budget.value);
    const remaining = Number.isFinite(budget) && budget !== null ? budget - act : null;
    totalsEl.replaceChildren(
      el('div', { class: 'stat' }, el('span', { class: 'stat-value' }, formatMoney(est)), el('span', { class: 'stat-label' }, 'Tahmini toplam')),
      el('div', { class: 'stat' }, el('span', { class: 'stat-value' }, formatMoney(act)), el('span', { class: 'stat-label' }, 'Gerçekleşen toplam')),
      el('div', { class: 'stat' }, el('span', { class: `stat-value${remaining !== null && remaining < 0 ? ' text-red' : ''}` }, remaining === null ? '—' : formatMoney(remaining)),
        el('span', { class: 'stat-label' }, remaining !== null && remaining < 0 ? 'Bütçe aşıldı' : 'Kalan bütçe')));
    if (form.elements.type.value === 'trip') form.elements.spent.value = numberToInput(Math.round(act * 100) / 100);
  }
  for (const e of trip.expenses || []) tbody.append(expenseRow(e, recompute));

  const tripSection = el('fieldset', { class: 'trip-section' },
    el('legend', null, 'Seyahat bilgileri'),
    el('div', { class: 'form-grid' },
      field({ label: 'Şehir', name: 'trip.city', value: trip.city, maxlength: 100 }),
      field({ label: 'Konaklama', name: 'trip.accommodation', value: trip.accommodation, maxlength: 500 }),
      field({ label: 'Ulaşım', name: 'trip.transport', value: trip.transport, maxlength: 500 })),
    places.node,
    el('div', { class: 'field' },
      el('span', { class: 'field-label' }, 'Masraf tablosu'),
      el('div', { class: 'table-wrap' },
        el('table', { class: 'table expense-table' },
          el('thead', null, el('tr', null, el('th', null, 'Ad'), el('th', null, 'Tahmini (₺)'), el('th', null, 'Gerçekleşen (₺)'), el('th', null, el('span', { class: 'visually-hidden' }, 'İşlem')))),
          tbody)),
      el('div', null, button('Masraf ekle', () => {
        const row = expenseRow({ id: shortId() }, recompute);
        tbody.append(row);
        row.querySelector('input').focus();
      }, { iconName: 'plus', className: 'btn-small' }))),
    totalsEl);

  form.append(
    el('div', { class: 'form-grid' },
      field({ label: 'Ad', name: 'name', value: p.name, required: true, maxlength: 200, className: 'span-all' }),
      typeField,
      field({ label: 'Durum', name: 'status', type: 'select', value: p.status, options: Object.entries(PLAN_STATUS) }),
      field({ label: 'Başlangıç tarihi', name: 'startDate', type: 'date', value: p.startDate, required: true }),
      field({ label: 'Başlangıç saati', name: 'startTime', type: 'time', value: p.startTime }),
      field({ label: 'Bitiş tarihi', name: 'endDate', type: 'date', value: p.endDate }),
      field({ label: 'Bitiş saati', name: 'endTime', type: 'time', value: p.endTime }),
      field({ label: 'Konum', name: 'location', value: p.location, maxlength: 200, className: 'span-all' }),
      budgetField,
      spentField,
      field({ label: 'Açıklama', name: 'description', type: 'textarea', value: p.description, rows: 3, className: 'span-all' })),
    tripSection,
    checklist.node,
    field({ label: 'Notlar', name: 'notes', type: 'textarea', value: p.notes, rows: 3 }));

  function syncType() {
    const isTrip = form.elements.type.value === 'trip';
    tripSection.hidden = !isTrip;
    form.elements.spent.disabled = isTrip;
    if (isTrip) recompute();
  }
  form.elements.type.addEventListener('change', syncType);
  form.elements.budget.addEventListener('input', recompute);
  syncType();

  function collect() {
    const f = form.elements;
    const data = {
      name: f.name.value,
      type: f.type.value,
      status: f.status.value,
      startDate: f.startDate.value,
      startTime: f.startTime.value,
      endDate: f.endDate.value || f.startDate.value,
      endTime: f.endTime.value,
      location: f.location.value,
      description: f.description.value,
      budget: f.budget.value,
      spent: f.spent.value,
      checklist: checklist.getItems(),
      notes: f.notes.value,
      trip: null
    };
    if (data.type === 'trip') {
      data.trip = {
        city: f['trip.city'].value,
        accommodation: f['trip.accommodation'].value,
        transport: f['trip.transport'].value,
        places: places.getItems(),
        expenses: [...tbody.children].map((row) => ({
          id: row.dataset.id,
          name: row.querySelector('.exp-name').value,
          estimated: row.querySelector('.exp-est').value,
          actual: row.querySelector('.exp-act').value
        })).filter((e) => e.name.trim() || e.estimated.trim() || e.actual.trim())
      };
    }
    return data;
  }

  const initial = JSON.stringify(collect());
  let saving = false;

  async function save(dlg) {
    if (saving) return;
    saving = true;
    clearFieldErrors(form);
    try {
      const data = collect();
      const saved = plan ? await updateRecord('plans', plan.id, data) : await createRecord('plans', data);
      await dlg.close(true);
      toast(plan ? 'Plan güncellendi.' : 'Plan eklendi.', { kind: 'success' });
      if (onSaved) onSaved(saved);
    } catch (err) {
      if (err.fields) {
        // Masraf satırı hataları ilgili satırın altına yazılır.
        const rest = {};
        for (const [path, msg] of Object.entries(err.fields)) {
          const m = /^trip\.expenses\.(\d+)\./.exec(path);
          if (m && tbody.children[Number(m[1])]) {
            const input = tbody.children[Number(m[1])].querySelector('.exp-name');
            input.setAttribute('aria-invalid', 'true');
            const errEl = input.parentElement.querySelector('.field-error');
            errEl.textContent = msg;
            errEl.hidden = false;
          } else rest[path] = msg;
        }
        const unmatched = showFieldErrors(form, rest);
        if (unmatched.length) toast(unmatched.join(' '), { kind: 'error' });
      } else {
        toastError('plan.save', err, () => save(dlg));
      }
    } finally {
      saving = false;
    }
  }

  const actions = [];
  if (plan) {
    actions.push({
      label: 'Sil',
      kind: 'danger',
      icon: 'trash',
      className: 'mr-auto',
      onClick: async (dlg) => {
        try {
          await deleteRecord('plans', plan.id);
          await dlg.close(true);
          toast('Plan silindi.', {
            actionLabel: 'Geri al',
            onAction: async () => {
              await restoreRecord('plans', plan.id);
              if (onSaved) onSaved(plan);
            }
          });
          if (onDeleted) onDeleted(plan);
        } catch (err) {
          toastError('plan.delete', err);
        }
      }
    });
  }
  actions.push({ label: 'Vazgeç', onClick: (dlg) => dlg.close() });
  actions.push({ label: 'Kaydet', kind: 'primary', onClick: (dlg) => save(dlg) });

  form.addEventListener('submit', (e) => e.preventDefault());
  return openDialog({
    title: plan ? 'Planı düzenle' : 'Yeni plan',
    content: form,
    size: 'lg',
    actions,
    isDirty: () => JSON.stringify(collect()) !== initial
  });
}
