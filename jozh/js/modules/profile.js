// Profilim: kişisel bilgiler, profil fotoğrafı ve özet kartı. Kaydedilmemiş değişiklikte çıkarken uyarır.
import { initApp, renderLoadError } from '../app.js';
import { getSingleton, saveSingleton } from '../storage/records.js';
import { el, replace, field, toast, toastError, saveStatus, showFieldErrors, clearFieldErrors, button, loadingState } from '../ui.js';
import { BLOOD_TYPES } from '../utils/labels.js';
import { numberToInput, formatNumber, initials } from '../utils/formatters.js';
import { calcAge, formatDate } from '../utils/dates.js';
import { createPhotoField, avatar } from '../components/photos.js';

const main = document.getElementById('main');
let profile = null;
let form = null;
let photos = null;
let snapshot = '';
let leaving = false;
const summary = el('aside', { class: 'card profile-summary', 'aria-label': 'Profil özeti' });
const status = saveStatus();

function collect() {
  const f = form.elements;
  return {
    firstName: f.firstName.value,
    lastName: f.lastName.value,
    birthDate: f.birthDate.value,
    bloodType: f.bloodType.value,
    height: f.height.value,
    weight: f.weight.value,
    phone: f.phone.value,
    about: f.about.value,
    photoId: photos.getId()
  };
}

function isDirty() {
  return !leaving && Boolean(form) && (JSON.stringify(collect()) !== snapshot || photos.isDirty());
}

function renderSummary() {
  const p = profile || {};
  const name = [p.firstName, p.lastName].filter(Boolean).join(' ');
  const age = calcAge(p.birthDate);
  const rows = [];
  if (p.birthDate) rows.push(['Doğum tarihi', `${formatDate(p.birthDate)}${age !== null ? ` (${age} yaş)` : ''}`]);
  if (p.bloodType) rows.push(['Kan grubu', p.bloodType]);
  if (p.height) rows.push(['Boy', `${p.height} cm`]);
  if (p.weight) rows.push(['Kilo', `${formatNumber(p.weight, 1)} kg`]);
  if (p.height && p.weight) {
    const bmi = p.weight / ((p.height / 100) ** 2);
    rows.push(['Vücut kitle indeksi', formatNumber(bmi, 1)]);
  }
  if (p.phone) rows.push(['Telefon', p.phone]);
  replace(summary,
    el('div', { class: 'summary-head' },
      avatar({ photoId: p.photoId, text: initials(p.firstName, p.lastName), size: 'lg' }),
      el('div', null, el('h2', null, name || 'Adını ekle'), age !== null ? el('p', { class: 'muted' }, `${age} yaşında`) : null)),
    rows.length
      ? el('dl', { class: 'kv mt' }, rows.flatMap(([k, v]) => [el('dt', null, k), el('dd', null, v)]))
      : el('p', { class: 'muted mt' }, 'Bilgilerini girip kaydettiğinde özet burada görünür.'),
    p.about ? el('p', { class: 'prose mt small' }, p.about) : null);
}

async function save() {
  clearFieldErrors(form);
  status.set('saving');
  try {
    profile = await saveSingleton('profile', collect());
    await photos.commit('profile:main');
    snapshot = JSON.stringify(collect());
    status.set('saved');
    renderSummary();
    toast('Profil kaydedildi.', { kind: 'success' });
  } catch (err) {
    status.set('error', { err, retry: save });
    if (err.fields) showFieldErrors(form, err.fields);
    else toastError('profile.save', err, save);
  }
}

function buildForm() {
  const p = profile || {};
  photos = createPhotoField({ label: 'Profil fotoğrafı', max: 1, initial: p.photoId ? [p.photoId] : [], onChange: () => status.set(isDirty() ? 'dirty' : '') });
  form = el('form', { class: 'card form-stack profile-form', novalidate: true },
    el('div', { class: 'form-grid' },
      field({ label: 'Ad', name: 'firstName', value: p.firstName || '', maxlength: 60, autocomplete: 'given-name' }),
      field({ label: 'Soyad', name: 'lastName', value: p.lastName || '', maxlength: 60, autocomplete: 'family-name' }),
      field({ label: 'Doğum tarihi', name: 'birthDate', type: 'date', value: p.birthDate || '' }),
      field({ label: 'Kan grubu', name: 'bloodType', type: 'select', value: p.bloodType || '', options: [['', 'Seçilmedi'], ...BLOOD_TYPES.map((b) => [b, b])] }),
      field({ label: 'Boy (cm)', name: 'height', value: numberToInput(p.height), inputmode: 'numeric', hint: '50–250 arası' }),
      field({ label: 'Kilo (kg)', name: 'weight', value: numberToInput(p.weight), inputmode: 'decimal', hint: 'Ondalık için virgül: 72,5' }),
      field({ label: 'Telefon (isteğe bağlı)', name: 'phone', type: 'tel', value: p.phone || '', maxlength: 30, autocomplete: 'tel' })),
    field({ label: 'Hakkımda', name: 'about', type: 'textarea', value: p.about || '', rows: 5, maxlength: 2000, hint: 'En çok 2.000 karakter.' }),
    photos.node,
    el('div', { class: 'form-actions' }, button('Kaydet', null, { kind: 'primary', type: 'submit', iconName: 'check' }), status.node));
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    save();
  });
  form.addEventListener('input', () => status.set(isDirty() ? 'dirty' : ''));
  snapshot = JSON.stringify(collect());
}

async function load() {
  replace(main, loadingState());
  try {
    profile = await getSingleton('profile');
    buildForm();
    renderSummary();
    replace(main, el('div', { class: 'profile-layout' }, form, summary));
  } catch (err) {
    renderLoadError(main, err, load);
  }
}

async function setup() {
  window.addEventListener('beforeunload', (e) => {
    if (isDirty()) {
      e.preventDefault();
      e.returnValue = '';
    }
  });
  // Menü bağlantılarında da uyar.
  document.addEventListener('click', (e) => {
    const link = e.target.closest('a[href]');
    if (!link || !isDirty() || link.target) return;
    if (!window.confirm('Kaydedilmemiş değişiklikler var. Sayfadan çıkılsın mı?')) e.preventDefault();
    else leaving = true;
  }, true);
  await load();
}

const ready = await initApp({ page: 'profile', title: 'Profilim' });
if (ready) await setup();
