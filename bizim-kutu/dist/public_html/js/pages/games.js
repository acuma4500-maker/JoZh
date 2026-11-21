// Oyun Merkezi: davetler, devam eden oyunlar, 7 oyun.
import { getState, subscribe, serverNow } from '../state.js';
import { userName } from '../constants.js';
import { rtdb } from '../firebase-config.js';
import { ref, onValue, rtdbQuery, orderByChild, limitToLast } from '../vendor/firebase.js';
import { h, clear, add } from '../utils/helpers.js';
import { icons } from '../utils/icons.js';
import { toast, errorMessage, setLoading } from '../utils/ui.js';
import { GAMES, gameById } from '../games/registry.js';
import { sendInvite, isInviteLive, acceptInvite, declineInvite, cancelInvite, subscribeScores, INVITE_TTL } from '../services/games.js';

export default async function games(page, { scope }) {
  const { uid, partnerUid } = getState();
  const banner = h('div', { class: 'notice' });
  const invitesEl = h('div', { class: 'invite-list' });
  const activeEl = h('div', { class: 'invite-list' });
  const grid = h('div', { class: 'game-grid' });
  const scoreEls = {};
  const inviteBtns = [];

  const drawBanner = () => {
    const on = getState().presence[partnerUid]?.online;
    banner.className = `notice ${on ? 'notice--ok' : ''}`;
    banner.textContent = on ? `🟢 ${userName(partnerUid)} çevrim içi — davet gönderebilirsin!` : `⚪ ${userName(partnerUid)} şu an çevrim dışı. Canlı oyunlar ikiniz de çevrim içiyken başlar.`;
    inviteBtns.forEach((b) => { b.disabled = !on; });
  };

  const drawInvites = () => {
    const live = getState().invites.filter((i) => isInviteLive(i));
    clear(invitesEl);
    for (const inv of live) {
      const g = gameById(inv.game);
      const left = Math.max(0, Math.ceil((INVITE_TTL - (serverNow() - inv.createdAt)) / 1000));
      if (inv.to === uid) {
        const acc = h('button', { class: 'btn btn--primary btn--sm', type: 'button', onclick: async () => {
          setLoading(acc, true);
          try { location.hash = `#/play/${await acceptInvite(inv)}`; } catch (e) { toast(errorMessage(e), { type: 'error' }); setLoading(acc, false); }
        } }, 'Kabul et');
        add(invitesEl, h('div', { class: 'invite card invite--in' },
          h('span', { class: 'invite__emoji', 'aria-hidden': 'true' }, g?.emoji),
          h('div', { class: 'invite__text' }, h('strong', {}, `${userName(inv.from)} seni davet ediyor`), h('small', {}, `${g?.name} · ${left} sn`)),
          acc, h('button', { class: 'btn btn--ghost btn--sm', type: 'button', onclick: () => declineInvite(inv).catch((e) => toast(errorMessage(e), { type: 'error' })) }, 'Reddet')));
      } else {
        add(invitesEl, h('div', { class: 'invite card' },
          h('span', { class: 'invite__emoji', 'aria-hidden': 'true' }, g?.emoji),
          h('div', { class: 'invite__text' }, h('strong', {}, `${g?.name} daveti gönderildi`), h('small', {}, `${userName(inv.to)} yanıtlıyor… ${left} sn`)),
          h('span', { class: 'heart-loader small', 'aria-hidden': 'true' }, '❤'),
          h('button', { class: 'btn btn--ghost btn--sm', type: 'button', onclick: () => cancelInvite(inv).catch(() => {}) }, 'İptal')));
      }
    }
  };

  // Devam eden oturumlar
  scope.add(onValue(rtdbQuery(ref(rtdb, 'games/sessions'), orderByChild('createdAt'), limitToLast(15)), (snap) => {
    const list = [];
    snap.forEach((c) => { const v = c.val(); if (v.status === 'active' && v.players?.[uid]) list.push({ id: c.key, ...v }); });
    clear(activeEl);
    list.reverse().slice(0, 5).forEach((s) => {
      const g = gameById(s.game);
      add(activeEl, h('a', { class: 'invite card', href: `#/play/${s.id}` },
        h('span', { class: 'invite__emoji', 'aria-hidden': 'true' }, g?.emoji),
        h('div', { class: 'invite__text' }, h('strong', {}, g?.name), h('small', {}, `Devam eden oyun · ${s.round || 1}. tur`)),
        h('span', { class: 'pill pill--primary' }, 'Devam et')));
    });
  }, (e) => console.warn(e)));

  for (const g of GAMES) {
    const scoreEl = h('small', { class: 'game-card__score' }, '');
    scoreEls[g.id] = scoreEl;
    const btn = h('button', { class: 'btn btn--primary btn--sm', type: 'button', onclick: async () => {
      setLoading(btn, true, 'Gönderiliyor…');
      try { await sendInvite(g.id); toast(`Davet gönderildi 💌`); }
      catch (e) { toast(errorMessage(e), { type: 'error' }); }
      finally { setLoading(btn, false); drawBanner(); }
    } }, 'Davet et');
    inviteBtns.push(btn);
    add(grid, h('article', { class: `game-card game-card--${g.color}` },
      h('div', { class: 'game-card__emoji', 'aria-hidden': 'true' }, g.emoji),
      h('h3', { class: 'game-card__name' }, g.name),
      h('p', { class: 'game-card__tag' }, g.tagline),
      scoreEl, btn));
    if (['xox', 'know-me', 'emoji', 'memory', 'truth-dare'].includes(g.id)) {
      scope.add(subscribeScores(g.id, (sc) => {
        const parts = [`${userName(uid)} ${sc[uid] || 0}`, `${userName(partnerUid)} ${sc[partnerUid] || 0}`];
        if (sc.draw) parts.push(`berabere ${sc.draw}`);
        scoreEl.textContent = `🏆 ${parts.join(' · ')}`;
      }));
    }
  }

  add(page, 
    h('div', { class: 'page-head' }, h('div', {}, h('h2', { class: 'page-title' }, 'Oyun Merkezi'), h('p', { class: 'page-sub' }, 'Birlikte oynayan çift, birlikte güler.')),
      h('a', { class: 'btn btn--ghost btn--sm', href: '#/stories' }, '📜 Hikâyelerimiz')),
    banner, invitesEl, activeEl, grid);
  drawBanner(); drawInvites();
  scope.add(subscribe(drawBanner, ['presence']));
  scope.add(subscribe(drawInvites, ['invites']));
  scope.interval(drawInvites, 1000);
  void icons;
}
