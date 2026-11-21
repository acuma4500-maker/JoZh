// Ekran klavyesi uyumu (iPhone Safari ve uygulama içi tarayıcılar, Android Chrome).
//
// iPhone'da klavye açılınca "görünen alan" (visualViewport) küçülür ve sayfa yukarı kaydırılır.
// Uygulama kutusunu (.shell, giriş ekranı, pencereler) her an tam olarak görünen alana yerleştiriyoruz:
//   --app-h  : görünen alanın yüksekliği (klavye hariç)
//   --vv-top : görünen alanın, sayfaya göre üst kenarı
// Böylece üst çerçeve görünen alanın en üstünde, mesaj yazma kutusu klavyenin hemen üstünde kalır.
// iPhone'un kaydırmasını GERİ ALMIYORUZ (geri almak konumların kaymasına yol açıyordu); sadece takip ediyoruz.
// Klavye açıkken <html> öğesine "kb-open" sınıfı eklenir (alt menü gizlenir).
const root = document.documentElement;
const vv = window.visualViewport;
let raf = 0;
let fullHeight = 0; // klavye kapalıyken görülen en büyük yükseklik

const isEditable = (el) => !!el && (el.tagName === 'TEXTAREA' || el.isContentEditable
  || (el.tagName === 'INPUT' && !['checkbox', 'radio', 'button', 'submit', 'range', 'color'].includes(el.type)));

function sync() {
  raf = 0;
  // window.__vvTest: yalnızca otomatik testlerde klavyeyi taklit etmek için
  const test = window.__vvTest;
  const height = test?.height ?? (vv ? vv.height : window.innerHeight);
  const top = test ? 0 : (vv ? vv.offsetTop : 0);
  const editing = isEditable(document.activeElement);
  if (!editing) fullHeight = Math.max(height, window.innerHeight);
  else fullHeight = Math.max(fullHeight, window.innerHeight);
  root.style.setProperty('--app-h', `${Math.round(height)}px`);
  root.style.setProperty('--vv-top', `${Math.max(0, Math.round(top))}px`);
  root.classList.toggle('kb-open', editing && fullHeight - height > 120);
}
const schedule = () => { if (!raf) raf = requestAnimationFrame(sync); };

if (vv) {
  vv.addEventListener('resize', schedule);
  vv.addEventListener('scroll', schedule);
}
window.addEventListener('resize', schedule);
window.addEventListener('orientationchange', () => { fullHeight = 0; schedule(); setTimeout(schedule, 400); });
// Klavye animasyonu boyunca birkaç kez ölç (bazı tarayıcılar olay göndermeyi geciktirir)
document.addEventListener('focusin', () => { [0, 100, 300, 600].forEach((t) => setTimeout(schedule, t)); });
document.addEventListener('focusout', () => { [0, 100, 300, 600].forEach((t) => setTimeout(schedule, t)); });
// Eski iOS sürümleri touch-action'ı her yerde uygulamayabilir: 350 ms içindeki ikinci dokunuşta
// yakınlaştırmayı engelle (dokunuş yine tıklama olarak çalışır; iki parmak yakınlaştırması etkilenmez).
let lastTouchEnd = 0;
document.addEventListener('touchend', (e) => {
  const now = Date.now();
  if (now - lastTouchEnd <= 350 && e.touches.length === 0 && e.changedTouches.length === 1) {
    const t = e.target.closest?.('button, a, [role="button"], .pin-key');
    if (t) { e.preventDefault(); t.click(); }
  }
  lastTouchEnd = now;
}, { passive: false });

sync();
export const syncViewport = schedule;
