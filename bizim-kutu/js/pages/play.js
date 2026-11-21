// Ortak oyun ekranı: oturumu dinler, oyunu yükler, bağlantı kopmalarını ve sonuç ekranını yönetir.
import { getState, subscribe, serverNow } from '../state.js';
import { userName, userEmoji } from '../constants.js';
import { h, clear, fill, add } from '../utils/helpers.js';
import { icons } from '../utils/icons.js';
import { toast, confirmDialog, errorMessage, emptyState, setLoading } from '../utils/ui.js';
import { gameById } from '../games/registry.js';
import { loadGame, subscribeSession, act as rawAct, joinSession, addScore } from '../services/games.js';

export default async function play(page, { params, scope }) {
  const sid = params.id;
  const { uid, partnerUid } = getState();
  let session = null, game = null, instance = null, meta = null, lastSig = '', mounting = null;
  const headEl = h('div', { class: 'play-head card' });
  const stage = h('div', { class: 'play-stage' });
  const overlay = h('div', { class: 'play-overlay', hidden: true });
  page.classList.add('play-page');
  add(page, headEl, h('div', { class: 'play-wrap' }, stage, overlay));
  add(stage, h('div', { class: 'page-loading' }, h('span', { class: 'heart-loader' }, '❤')));

  /** Oyunlara verilen API. */
  const api = {
    sid, me: uid, partner: partnerUid, scope,
    name: userName, emoji: userEmoji,
    get session() { return session; },
    serverNow,
    toast,
    /** Atomik hamle. Oyun bu işlemle bittiyse skor bir kez (işlemi yapan cihazca) yazılır. */
    async act(fn) {
      let finished = null;
      try {
        const r = await rawAct(sid, (s) => {
          const was = s.status;
          if (was !== 'active') return undefined;
          const out = fn(s, s.state);
          finished = out && out.status === 'finished' ? out.result || null : null;
          return out;
        });
        if (r.committed && finished && finished.winner && meta?.scored !== false) addScore(session.game, finished.winner);
        return r.committed;
      } catch (e) { toast(errorMessage(e), { type: 'error' }); return false; }
    },
  };

  scope.add(subscribeSession(sid, async (s) => {
    session = s;
    if (!s) { fill(stage, emptyState({ emoji: '🕹️', title: 'Oyun bulunamadı', text: 'Bu oyun bitmiş ya da silinmiş olabilir.' })); overlay.hidden = true; return; }
    if (!s.players?.[uid]) { fill(stage, emptyState({ emoji: '🙈', title: 'Bu oyuna erişimin yok' })); return; }
    if (!mounting) {
      // Oyun modülü yalnızca bir kez yüklenir/bağlanır (yükleme sırasında gelen güncellemeler beklenir).
      mounting = (async () => {
        meta = gameById(s.game);
        game = await loadGame(s.game);
        if (scope.disposed) return;
        clear(stage);
        instance = game.mount(stage, api);
        scope.add(() => instance?.destroy?.());
      })();
    }
    try { await mounting; } catch (e) { fill(stage, emptyState({ emoji: '🥺', title: 'Oyun yüklenemedi', text: errorMessage(e) })); return; }
    if (scope.disposed || s !== session) return; // daha yeni bir güncelleme işlenecek
    drawHead();
    // Yalnızca oyun durumu değiştiğinde yeniden çiz (ör. "oyunda" sinyali yazılan metni silmesin).
    const sig = JSON.stringify([s.state, s.status, s.round]);
    if (sig !== lastSig) { lastSig = sig; try { instance?.update?.(session); } catch (e) { console.error(e); } }
    drawOverlay();
  }, (e) => fill(stage, emptyState({ emoji: '🥺', title: 'Oyuna bağlanılamadı', text: errorMessage(e) }))));

  // Oyunda olduğumu bildir (bağlantı koparsa sunucu siler)
  let leave = null;
  joinSession(sid, uid).then((fn) => { if (scope.disposed) fn(); else leave = fn; }).catch(() => {});
  scope.add(() => leave?.());

  function drawHead() {
    const g = meta;
    const here = session.here || {};
    const tally = session.state?.tally || session.state?.scores || {};
    fill(headEl, 
      h('div', { class: 'play-head__title' }, h('span', { 'aria-hidden': 'true' }, g?.emoji), h('strong', {}, g?.name), h('small', { class: 'muted' }, `${session.round || 1}. tur`)),
      h('div', { class: 'play-head__players' },
        ...[uid, partnerUid].map((u) => h('span', { class: `player-chip${here[u] ? ' is-here' : ''}` },
          h('span', { 'aria-hidden': 'true' }, userEmoji(u)), userName(u) + (u === uid ? ' (sen)' : ''),
          typeof tally[u] === 'number' ? h('b', { class: 'player-chip__score' }, tally[u]) : null,
          h('span', { class: `dot ${here[u] ? 'dot--on' : 'dot--off'}`, title: here[u] ? 'Oyunda' : 'Oyunda değil' })))),
      session.status === 'active' ? h('button', { class: 'btn btn--ghost btn--sm', type: 'button', onclick: endGame }, 'Oyunu bitir') : null);
  }

  async function endGame() {
    if (!(await confirmDialog({ title: 'Oyun bitirilsin mi?', message: 'Oyun iki taraf için de sonlanacak.', confirmText: 'Bitir', danger: true }))) return;
    await rawAct(sid, (s) => { if (s.status !== 'active') return undefined; s.status = 'ended'; s.endedBy = uid; return s; }).catch((e) => toast(errorMessage(e), { type: 'error' }));
  }

  // Bağlantı kopması: partner 4 sn'den uzun süre oyunda değilse bekleme ekranı
  let absentSince = 0;
  scope.interval(() => drawOverlay(), 1000);
  scope.add(subscribe(() => drawOverlay(), ['presence', 'connected']));

  function drawOverlay() {
    if (!session) return;
    const s = session;
    clear(overlay);
    if (s.status === 'finished') {
      overlay.hidden = false;
      const wantsMe = !!s.rematch?.[uid], wantsPartner = !!s.rematch?.[partnerUid];
      const btn = h('button', { class: 'btn btn--primary', type: 'button', disabled: wantsMe, onclick: () => rematch(btn) }, wantsMe ? 'Bekleniyor…' : wantsPartner ? 'Kabul et, tekrar oyna!' : 'Tekrar oyna');
      add(overlay, h('div', { class: 'result card pop-in', role: 'dialog', 'aria-label': 'Oyun sonucu' },
        h('div', { class: 'result__confetti', 'aria-hidden': 'true' }, '🎉'),
        game?.summary ? game.summary(s, api) : h('h3', {}, 'Oyun bitti!'),
        wantsPartner && !wantsMe ? h('p', { class: 'notice notice--ok' }, `${userName(partnerUid)} tekrar oynamak istiyor!`) : null,
        wantsMe && !wantsPartner ? h('p', { class: 'muted' }, `${userName(partnerUid)}'nın onayı bekleniyor…`) : null,
        h('div', { class: 'row row--center' }, btn, h('a', { class: 'btn btn--ghost', href: '#/games' }, 'Oyunlara dön'))));
      return;
    }
    if (s.status === 'ended') {
      overlay.hidden = false;
      add(overlay, h('div', { class: 'result card' }, h('div', { class: 'result__confetti' }, '👋'),
        h('h3', {}, s.endedBy === uid ? 'Oyunu bitirdin' : `${userName(s.endedBy)} oyunu bitirdi`),
        h('a', { class: 'btn btn--primary', href: '#/games' }, 'Oyunlara dön')));
      return;
    }
    const partnerHere = !!s.here?.[partnerUid];
    const meConnected = getState().connected;
    if (partnerHere && meConnected) { absentSince = 0; overlay.hidden = true; return; }
    absentSince ||= Date.now();
    if (Date.now() - absentSince < 4000) { overlay.hidden = true; return; }
    overlay.hidden = false;
    const online = getState().presence[partnerUid]?.online;
    add(overlay, h('div', { class: 'result card' },
      h('span', { class: 'heart-loader', 'aria-hidden': 'true' }, '❤'),
      h('h3', {}, !meConnected ? 'Bağlantın koptu' : `${userName(partnerUid)} bekleniyor…`),
      h('p', { class: 'muted' }, !meConnected ? 'İnternet geri geldiğinde oyun kaldığı yerden devam edecek.'
        : online ? `${userName(partnerUid)} oyun ekranında değil. Geri döndüğünde kaldığınız yerden devam edersiniz.` : `${userName(partnerUid)}'nın bağlantısı koptu. Yeniden bağlanınca oyun devam edecek.`),
      h('div', { class: 'row row--center' }, h('a', { class: 'btn btn--ghost', href: '#/games' }, 'Lobiye dön'), h('button', { class: 'btn btn--danger', type: 'button', onclick: endGame }, 'Oyunu bitir'))));
  }

  async function rematch(btn) {
    setLoading(btn, true);
    try {
      const fresh = await game.create({ players: Object.keys(session.players), host: session.host, prev: session.state, round: (session.round || 1) + 1 });
      await rawAct(sid, (s) => {
        if (s.status !== 'finished') return undefined;
        s.rematch = { ...(s.rematch || {}), [uid]: true };
        if (s.rematch[partnerUid]) {
          s.state = fresh; s.status = 'active'; s.round = (s.round || 1) + 1; s.rematch = null; s.result = null;
        }
        return s;
      });
    } catch (e) { toast(errorMessage(e), { type: 'error' }); setLoading(btn, false); }
  }
  void icons;
}
