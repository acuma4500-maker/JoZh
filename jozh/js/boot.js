// İlk boyamadan önce tema ve menü modunu uygular (klasik betik, <head> içinde).
(function () {
  var root = document.documentElement;
  var theme = 'system';
  var nav = 'expanded';
  try {
    theme = localStorage.getItem('jozh.theme') || 'system';
    nav = localStorage.getItem('jozh.nav') || 'expanded';
  } catch (err) {
    theme = 'system';
  }
  var resolved = theme;
  if (theme !== 'light' && theme !== 'dark') {
    resolved = window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark';
  }
  root.setAttribute('data-theme', resolved);
  root.setAttribute('data-theme-pref', theme);

  function navMode() {
    var w = window.innerWidth;
    var h = window.innerHeight;
    if (w <= 699) return 'drawer';
    if (h <= 500) return 'rail';
    return nav === 'collapsed' ? 'rail' : 'full';
  }
  root.setAttribute('data-nav-mode', navMode());
})();
