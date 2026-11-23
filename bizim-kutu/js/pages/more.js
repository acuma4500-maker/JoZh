// Mobil "Daha" menüsü.
import { h, add } from '../utils/helpers.js';
import { icons } from '../utils/icons.js';
import { on } from '../features.js';

const ITEMS = [
  ['#/watch', 'tv', 'Birlikte İzle', 'YouTube\'u aynı anda izleyin'],
  ['#/movies', 'film', 'Film & Dizi', 'İzleme listemiz'],
  ['#/tasks', 'tasks', 'Yapılacaklar', 'Ortak planlar'],
  ['#/vault', 'lock', 'Özel Kasamız', 'Şifreli notlar'],
  ['#/memories', 'book', 'Anı Defteri', 'Zaman çizelgemiz'],
  ['#/stats', 'chart', 'İstatistiklerimiz', 'Nerede ne kadar zaman geçirdik'],
  ['#/notifications', 'bell', 'Bildirimler', 'Son olanlar'],
  ['#/profile', 'user', 'Profil & Ayarlar', 'Tema, bildirim, güvenlik'],
];

export default async function more(page) {
  add(page, h('div', { class: 'page-head' }, h('div', {}, h('h2', { class: 'page-title' }, 'Kutumuz'), h('p', { class: 'page-sub' }, 'Her şey bir dokunuş uzağında.'))),
    h('div', { class: 'more-grid' }, ITEMS.filter(([href]) => on({ '#/watch': 'watch', '#/movies': 'movies', '#/tasks': 'tasks', '#/vault': 'vault', '#/memories': 'memories', '#/stats': 'stats', '#/notifications': 'notifications' }[href])).map(([href, icon, title, sub]) => h('a', { class: 'more-item card', href },
      h('span', { class: 'more-item__icon', svg: icons[icon] }), h('strong', {}, title), h('small', { class: 'muted' }, sub)))));
}
