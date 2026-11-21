// Ekran klavyesi uyumu (özellikle iPhone Safari).
// iOS klavye açılınca sayfanın tamamını yukarı kaydırır; sabit üst bar ve alt menü kayar, ekran
// "yarım" görünür. Burada uygulama kutusunu o an GÖRÜNEN alana (visualViewport) sabitliyoruz:
//   --app-h  : görünen yükseklik (klavye hariç)
//   --vv-top : görünen alanın üst kenarı
// ve klavye açıkken <html> öğesine "kb-open" sınıfı ekleniyor (alt menü gizlenir).
const root = document.documentElement;
const vv = window.visualViewport;
let raf = 0;

function sync() {
  raf = 0;
  // window.__vvTest: yalnızca otomatik testlerde klavyeyi taklit etmek için
  const height = window.__vvTest?.height ?? (vv ? vv.height : window.innerHeight);
  // iOS'un sayfayı kaydırmasını geri al: içerik zaten görünen alana sığdırılıyor.
  if (window.scrollY || document.documentElement.scrollTop) window.scrollTo(0, 0);
  const top = vv ? Math.max(0, vv.offsetTop) : 0;
  root.style.setProperty('--app-h', `${Math.round(height)}px`);
  root.style.setProperty('--vv-top', `${Math.round(top)}px`);
  const keyboard = window.innerHeight - height > 120 && isEditable(document.activeElement);
  root.classList.toggle('kb-open', keyboard);
}
const schedule = () => { if (!raf) raf = requestAnimationFrame(sync); };
const isEditable = (el) => !!el && (el.tagName === 'TEXTAREA' || (el.tagName === 'INPUT' && !['checkbox', 'radio', 'button', 'submit'].includes(el.type)) || el.isContentEditable);

if (vv) {
  vv.addEventListener('resize', schedule);
  vv.addEventListener('scroll', schedule);
}
window.addEventListener('resize', schedule);
window.addEventListener('orientationchange', schedule);
document.addEventListener('focusin', () => { schedule(); setTimeout(schedule, 300); });
document.addEventListener('focusout', () => { setTimeout(schedule, 50); setTimeout(schedule, 400); });
// Klavye kapanırken iOS bazen kaydırmayı geri almaz; garanti olsun.
window.addEventListener('scroll', () => { if (window.scrollY) window.scrollTo(0, 0); }, { passive: true });
sync();
export const syncViewport = schedule;
