// Birlikte Hikâye: veri ve saf durum oluşturucu (Firebase'siz, test edilebilir).
import { pick } from '../utils/helpers.js';
import { otherOf } from './common.js';

export const OPENINGS = [
  'Bir sabah uyandığımızda, balkonumuzda bize ait olmayan küçük bir valiz duruyordu…',
  'Kayıp bir trenin son vagonunda ikimizden başka kimse yoktu…',
  'Haritada olmayan bir adaya çıktığımızda kumda adlarımız yazıyordu…',
  'Gece yarısı çalan kapının ardında elinde bir mektup tutan yaşlı bir postacı vardı…',
  'Bir sabah tüm şehrin dili tersine dönmüştü ve sadece biz birbirimizi anlayabiliyorduk…',
  'Kafede garson bize gelecekte içeceğimiz kahveleri getirdi…',
  'Eski bir kitapçının en üst rafında, kapağında ikimizin resmi olan bir kitap bulduk…',
  'Bir gün kedimiz konuşmaya başladı ve ilk cümlesi şuydu…',
  'Uçağımız yanlış yere indi ama orası hayal ettiğimiz her şeydi…',
  'Yağmur durduğunda gökyüzünde iki gökkuşağı birbirine sarılmıştı…',
  'Zaman makinesinin tek bir yakıtı vardı: birlikte güldüğümüz anlar…',
  'Bir sabah aynaya baktığımızda birbirimizin yerine uyandığımızı fark ettik…',
];
export const MAX_LINES = 30;

export function createStory({ players, host, prev }) {
  const starter = prev ? otherOf(players, prev.starter) : host;
  return { title: '', opening: pick(OPENINGS), lines: [], turn: starter, starter, saved: '' };
}
