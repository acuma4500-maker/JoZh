// Sayfa adresleri. Bütün yollar bu dosyanın konumuna göre çözülür (js/ → ../pages/).

export const PAGES = {
  index: '../index.html',
  login: '../pages/login.html',
  dashboard: '../pages/dashboard.html',
  profile: '../pages/profile.html',
  partner: '../pages/partner.html',
  diary: '../pages/diary.html',
  dreams: '../pages/dreams.html',
  plans: '../pages/plans.html',
  calendar: '../pages/calendar.html',
  notes: '../pages/notes.html',
  finance: '../pages/finance.html',
  interview: '../pages/interview.html',
  sport: '../pages/sport.html',
  vaultLogin: '../pages/vault-login.html',
  vault: '../pages/vault.html',
  backup: '../pages/backup.html',
  settings: '../pages/settings.html'
};

// Yalnızca #new ve #change parçaları kullanılır; URL'de başka veri taşınmaz.
export function pageUrl(name, hash) {
  const url = new URL(PAGES[name], import.meta.url);
  if (hash) url.hash = hash;
  return url.href;
}

export function go(name, hash) {
  location.href = pageUrl(name, hash);
}

export function replaceWith(name, hash) {
  location.replace(pageUrl(name, hash));
}

export function currentPage() {
  return document.documentElement.dataset.page || '';
}

export function takeHash(expected) {
  if (location.hash === `#${expected}`) {
    history.replaceState(null, '', location.pathname + location.search);
    return true;
  }
  return false;
}
