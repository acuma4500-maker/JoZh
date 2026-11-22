// YouTube yardımcıları: link çözümleme ve IFrame Player API yükleyici.

/** YouTube linkinden 11 karakterlik video kimliğini çıkarır; bulamazsa null. */
export function parseYouTubeId(input) {
  const s = String(input || '').trim();
  if (/^[A-Za-z0-9_-]{11}$/.test(s)) return s;
  let url;
  try { url = new URL(s.startsWith('http') ? s : `https://${s}`); } catch { return null; }
  const host = url.hostname.replace(/^www\.|^m\.|^music\./, '');
  let id = null;
  if (host === 'youtu.be') id = url.pathname.split('/')[1];
  else if (host === 'youtube.com' || host === 'youtube-nocookie.com') {
    if (url.pathname === '/watch') id = url.searchParams.get('v');
    else {
      const m = url.pathname.match(/^\/(?:shorts|embed|live|v)\/([^/?#]+)/);
      if (m) id = m[1];
    }
  }
  return id && /^[A-Za-z0-9_-]{11}$/.test(id) ? id : null;
}

/** Linkteki başlangıç saniyesi (?t=90 / ?t=1m30s / ?start=90), yoksa 0. */
export function parseStartSeconds(input) {
  try {
    const url = new URL(String(input).trim().startsWith('http') ? String(input).trim() : `https://${String(input).trim()}`);
    const t = url.searchParams.get('t') || url.searchParams.get('start');
    if (!t) return 0;
    if (/^\d+$/.test(t)) return Number(t);
    const m = t.match(/(?:(\d+)h)?(?:(\d+)m)?(?:(\d+)s)?/);
    return m ? (Number(m[1] || 0) * 3600 + Number(m[2] || 0) * 60 + Number(m[3] || 0)) : 0;
  } catch { return 0; }
}

export const thumbUrl = (id) => `https://i.ytimg.com/vi/${id}/mqdefault.jpg`;

let loading = null;
/** YouTube IFrame Player API'yi bir kez yükler. */
export function loadYouTubeApi() {
  if (window.YT?.Player) return Promise.resolve(window.YT);
  if (!loading) {
    loading = new Promise((resolve, reject) => {
      const prev = window.onYouTubeIframeAPIReady;
      window.onYouTubeIframeAPIReady = () => { try { prev?.(); } catch {} resolve(window.YT); };
      const s = document.createElement('script');
      s.src = 'https://www.youtube.com/iframe_api';
      s.async = true;
      s.onerror = () => { loading = null; reject(new Error('YouTube yüklenemedi. İnternet bağlantını kontrol et.')); };
      document.head.appendChild(s);
    });
  }
  return loading;
}
