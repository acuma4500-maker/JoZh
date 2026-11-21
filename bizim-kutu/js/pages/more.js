// Mobil "Daha" menüsü.
import { h, add } from '../utils/helpers.js';
import { icons } from '../utils/icons.js';
import { on } from '../features.js';

const ITEMS = [
  ['#/movies', 'film', 'Film & Dizi', 'İzleme listemiz'],
  ['#/tasks', 'tasks', 'Yapılacaklar', 'Ortak planlar'],
  ['#/vault', 'lock', 'Özel Kasamız', 'Şifreli notlar'],
  ['#/memories', 'book', 'Anı Defteri', 'Zaman çizelgemiz'],
  ['#/stories', 'sparkles', 'Hikâyelerimiz', 'Birlikte yazdıklarımız'],
  ['#/notifications', 'bell', 'Bildirimler', 'Son olanlar'],
  ['#/profile', 'user', 'Profil & Ayarlar', 'Tema, bildirim, güvenlik'],
];

export default async function more(page) {
  add(page, h('div', { class: 'page-head' }, h('div', {}, h('h2', { class: 'page-title' }, 'Kutumuz'), h('p', { class: 'page-sub' }, 'Her şey bir dokunuş uzağında.'))),
    h('div', { class: 'more-grid' }, ITEMS.filter(([href]) => on({ '#/movies': 'movies', '#/tasks': 'tasks', '#/vault': 'vault', '#/memories': 'memories', '#/stories': 'games', '#/notifications': 'notifications' }[href])).map(([href, icon, title, sub]) => h('a', { class: 'more-item card', href },
      h('span', { class: 'more-item__icon', svg: icons[icon] }), h('strong', {}, title), h('small', { class: 'muted' }, sub)))));
}
