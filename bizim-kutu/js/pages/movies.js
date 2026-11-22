// Film & Dizi listesi (Firestore: couples/main/movies).

import { userName } from '../constants.js';
import { h, clear, fill, add } from '../utils/helpers.js';
import { icons } from '../utils/icons.js';
import { toast, confirmDialog, emptyState, openModal, skeletonList, errorState, field, counted, errorMessage, setLoading } from '../utils/ui.js';
import { relativeTime } from '../utils/dates.js';
import { LIMITS, validateText } from '../utils/validation.js';
import { col, listen, query, where, orderBy, limit, createItem, updateItem, deleteItem } from '../services/firestore.js';

const TABS = [
  { id: 'watchlist', label: 'İzlemek istediklerimiz', emoji: '🍿' },
  { id: 'watching', label: 'İzliyoruz', emoji: '▶️' },
  { id: 'watched', label: 'İzlediklerimiz', emoji: '✅' },
  { id: 'favorites', label: 'Favorilerimiz', emoji: '⭐' },
];
const GENRES = ['Romantik', 'Komedi', 'Dram', 'Aksiyon', 'Bilim kurgu', 'Fantastik', 'Korku', 'Gerilim', 'Animasyon', 'Belgesel', 'Suç', 'Macera', 'Müzikal', 'Diğer'];

function stars(value, onChange) {
  const wrap = h('div', { class: 'stars', role: onChange ? 'radiogroup' : 'img', 'aria-label': `Puan: ${value || 0}/5` });
  for (let i = 1; i <= 5; i++) {
    const s = h(onChange ? 'button' : 'span', { class: `star${i <= value ? ' is-on' : ''}`, type: onChange ? 'button' : undefined, role: onChange ? 'radio' : undefined, 'aria-checked': onChange ? String(i === value) : undefined, 'aria-label': onChange ? `${i} yıldız` : undefined, svg: icons.star });
    if (onChange) s.addEventListener('click', () => onChange(i === value ? 0 : i));
    add(wrap, s);
  }
  return wrap;
}

export default async function movies(page, { scope }) {
  let tab = sessionStorage.getItem('bk.moviesTab') || 'watchlist';
  let unsub = null;
  const listEl = h('div', { class: 'card-list' });
  const tabsEl = h('div', { class: 'tabs', role: 'tablist', 'aria-label': 'Film kategorileri' });

  const drawTabs = () => fill(tabsEl, ...TABS.map((t) => h('button', {
    class: `tabs__btn${t.id === tab ? ' is-active' : ''}`, role: 'tab', type: 'button', 'aria-selected': String(t.id === tab),
    onclick: () => { tab = t.id; sessionStorage.setItem('bk.moviesTab', tab); drawTabs(); sub(); }
  }, `${t.emoji} ${t.label}`)));

  function sub() {
    unsub?.();
    fill(listEl, skeletonList(3));
    // Tek alana göre sıralı tek sorgu; kategori/favori ayrımı cihazda yapılır (Firestore'da ek dizin gerekmez).
    const q = query(col('movies'), orderBy('createdAt', 'desc'), limit(300));
    unsub = listen(q, (all) => {
      const ms = (x) => x?.toMillis?.() || 0;
      draw(tab === 'favorites' ? all.filter((m) => m.favorite).sort((a, b) => ms(b.updatedAt) - ms(a.updatedAt)) : all.filter((m) => m.status === tab));
    }, (e) => fill(listEl, errorState(errorMessage(e), sub)));
  }
  scope.add(() => unsub?.());

  function draw(items) {
    clear(listEl);
    if (!items.length) {
      const t = TABS.find((x) => x.id === tab);
      add(listEl, emptyState({ emoji: t.emoji, title: 'Bu liste boş', text: tab === 'favorites' ? 'Bir filmi yıldızlayarak favorilere ekleyin.' : 'Birlikte izlemek istediğiniz bir şey ekleyin.', action: tab !== 'favorites' ? { label: 'Ekle', onClick: () => editor(null) } : undefined }));
      return;
    }
    for (const m of items) {
      add(listEl, h('article', { class: 'card movie' },
        h('div', { class: 'card__row' },
          h('div', { class: 'movie__icon', 'aria-hidden': 'true' }, m.kind === 'dizi' ? '📺' : '🎬'),
          h('div', { class: 'movie__main' },
            h('h4', { class: 'card__title' }, m.title),
            h('p', { class: 'card__meta' }, [m.kind === 'dizi' ? 'Dizi' : 'Film', m.genre].filter(Boolean).join(' · '))),
          h('button', { class: `icon-btn icon-btn--sm fav${m.favorite ? ' is-on' : ''}`, type: 'button', 'aria-label': m.favorite ? 'Favorilerden çıkar' : 'Favorilere ekle', 'aria-pressed': String(!!m.favorite), svg: icons.heart, onclick: () => quick(m, { favorite: !m.favorite }) })),
        m.description ? h('p', { class: 'card__text' }, m.description) : null,
        m.rating ? stars(m.rating) : null,
        m.comment ? h('blockquote', { class: 'movie__comment' }, m.comment) : null,
        h('p', { class: 'card__meta' }, `${userName(m.createdBy)} ekledi · ${relativeTime(m.createdAt)}`),
        h('div', { class: 'card__footer' },
          m.status === 'watchlist' ? h('button', { class: 'chip', type: 'button', onclick: () => quick(m, { status: 'watching' }) }, '▶️ İzlemeye başladık') : null,
          m.status !== 'watched' ? h('button', { class: 'chip chip--primary', type: 'button', onclick: () => finish(m) }, '✅ İzledik') : null,
          h('button', { class: 'icon-btn icon-btn--sm', type: 'button', 'aria-label': 'Düzenle', svg: icons.edit, onclick: () => editor(m) }),
          h('button', { class: 'icon-btn icon-btn--sm', type: 'button', 'aria-label': 'Sil', svg: icons.trash, onclick: () => remove(m) }))));
    }
  }

  async function quick(m, patch) {
    try { await updateItem('movies', m.id, patch); } catch (e) { toast(errorMessage(e), { type: 'error' }); }
  }
  async function finish(m) {
    await quick(m, { status: 'watched' });
    toast('İzlediklerimize taşındı. Puan vermek ister misin?', { action: { label: 'Puanla', onClick: () => editor({ ...m, status: 'watched' }) } });
  }
  async function remove(m) {
    if (!(await confirmDialog({ title: 'Silinsin mi?', message: `"${m.title}" listeden kaldırılacak.`, confirmText: 'Sil', danger: true }))) return;
    try { await deleteItem('movies', m.id); toast('Silindi'); } catch (e) { toast(errorMessage(e), { type: 'error' }); }
  }

  function editor(m) {
    let rating = m?.rating || 0;
    const title = h('input', { class: 'input', value: m?.title || '', placeholder: 'Film ya da dizi adı', required: true });
    const kind = h('select', { class: 'input' }, h('option', { value: 'film', selected: m?.kind !== 'dizi' }, 'Film'), h('option', { value: 'dizi', selected: m?.kind === 'dizi' }, 'Dizi'));
    const genre = h('input', { class: 'input', value: m?.genre || '', placeholder: 'Örn. Romantik', list: 'genre-list' });
    const genreList = h('datalist', { id: 'genre-list' }, GENRES.map((g) => h('option', { value: g })));
    const desc = h('textarea', { class: 'input', rows: '3', placeholder: 'Kısa açıklama', value: m?.description || '' });
    const status = h('select', { class: 'input' }, TABS.filter((t) => t.id !== 'favorites').map((t) => h('option', { value: t.id, selected: (m?.status || (tab === 'favorites' ? 'watchlist' : tab)) === t.id }, t.label)));
    const fav = h('input', { type: 'checkbox', checked: !!m?.favorite });
    const comment = h('textarea', { class: 'input', rows: '3', placeholder: 'İkimizin ortak yorumu', value: m?.comment || '' });
    const starWrap = h('div', {});
    const drawStars = () => fill(starWrap, stars(rating, (v) => { rating = v; drawStars(); }));
    drawStars();
    const err = h('p', { class: 'form-error', role: 'alert' });
    const save = h('button', { class: 'btn btn--primary btn--block', type: 'submit' }, m?.id ? 'Kaydet' : 'Listeye ekle');
    const form = h('form', { class: 'form', novalidate: true, onsubmit: async (e) => {
      e.preventDefault();
      const t = validateText(title.value, { label: 'Ad', max: LIMITS.movieTitle, multiline: false });
      const g = validateText(genre.value, { label: 'Tür', min: 0, max: LIMITS.movieGenre, multiline: false });
      const d = validateText(desc.value, { label: 'Açıklama', min: 0, max: LIMITS.movieText });
      const c = validateText(comment.value, { label: 'Yorum', min: 0, max: LIMITS.movieText });
      const bad = [t, g, d, c].find((x) => !x.ok);
      if (bad) { err.textContent = bad.error; return; }
      setLoading(save, true, 'Kaydediliyor…');
      const data = { title: t.value, kind: kind.value, genre: g.value, description: d.value, status: status.value, favorite: fav.checked, rating, comment: c.value };
      try {
        if (m?.id) await updateItem('movies', m.id, data); else await createItem('movies', data);
        toast(m?.id ? 'Güncellendi 🎬' : 'Listeye eklendi 🍿');
        modal.close();
      } catch (e2) { err.textContent = errorMessage(e2); setLoading(save, false); }
    } },
      field('Ad', title), h('div', { class: 'grid-2' }, field('Tür', kind), field('Kategori', genre)), genreList,
      field('Açıklama', counted(desc, LIMITS.movieText)), field('Durum', status),
      h('label', { class: 'check' }, fav, h('span', {}, '⭐ Favorilerimize ekle')),
      h('div', { class: 'field' }, h('span', { class: 'field__label' }, 'Puanımız'), starWrap),
      field('Ortak yorum', counted(comment, LIMITS.movieText)), err, save);
    const modal = openModal({ title: m?.id ? 'Düzenle' : 'Yeni film / dizi', content: form });
  }

  add(page, 
    h('div', { class: 'page-head' },
      h('div', {}, h('h2', { class: 'page-title' }, 'Film & Dizi'), h('p', { class: 'page-sub' }, 'Koltuk, battaniye, patlamış mısır.')),
      h('button', { class: 'btn btn--primary', type: 'button', onclick: () => editor(null) }, h('span', { svg: icons.plus }), 'Ekle')),
    tabsEl, listEl);
  drawTabs(); sub();

}
