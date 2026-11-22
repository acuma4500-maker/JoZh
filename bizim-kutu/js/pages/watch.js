// Birlikte İzle 🎬 — YouTube videosunu iki cihazda eşzamanlı izleme + izlerken sohbet.
//
// Realtime Database:
//   watch/room            { videoId, state: 'playing'|'paused', pos, at (sunucu zamanı), by, cid }
//                         (null = video kapalı)
//   watch/here/{kişi}     true — sayfada olan (bağlantı koparsa sunucu siler)
//   watch/history/{video} { videoId, title, by, at } — son izlenenler
//   watch/chat/{id}       { by, text | emoji, at } — izlerken sohbet; emoji tepkileri de buraya yazılır
//
// Eşleşme: kim oynatır/durdurur/sararsa "room" kaydını günceller; diğer cihaz kaydı görünce
// kendi oynatıcısını aynı konuma ve duruma getirir. Oynarken konum = pos + (şimdi - at).
// İkiniz de sayfada değilseniz video oynamaz; biri çıkarsa video iki tarafta da durur.
//
// Oynatıcı: YouTube'un kendi düğmeleri gizli (controls: 0); oynat/durdur, sarma, ses ve tam ekran
// bizim düğmelerimizle yapılır. Tam ekran da bizim: emoji tepkileri ve mesajlar tam ekranda da görünür.
import { rtdb } from '../firebase-config.js';
import {
  ref, set, update, remove, push, onValue, onChildAdded, onChildRemoved, onDisconnect, rtdbQuery, orderByChild, limitToLast,
  rtdbServerTimestamp,
} from '../vendor/firebase.js';
import { getState, serverNow } from '../state.js';
import { userName } from '../constants.js';
import { h, clear, fill, add, randomId } from '../utils/helpers.js';
import { toast, emptyState, errorMessage, setLoading, confirmDialog } from '../utils/ui.js';
import { relativeTime, formatTime } from '../utils/dates.js';
import { parseYouTubeId, parseStartSeconds, thumbUrl, loadYouTubeApi } from '../utils/youtube.js';

export const REACTIONS = ['❤️', '😂', '😮', '😢', '🔥', '👏'];
const PLAYING = 1, PAUSED = 2, ENDED = 0, BUFFERING = 3;
const CHAT_LIMIT = 60;

/** 75 → "1:15", 3725 → "1:02:05" */
export function fmtClock(sec) {
  const s = Math.max(0, Math.floor(Number(sec) || 0));
  const hh = Math.floor(s / 3600), mm = Math.floor((s % 3600) / 60), ss = s % 60;
  const p = (n) => String(n).padStart(2, '0');
  return hh ? `${hh}:${p(mm)}:${p(ss)}` : `${mm}:${p(ss)}`;
}

export default async function watch(page, { scope }) {
  const { uid, partnerUid } = getState();
  const cid = randomId(8);                 // bu sekmenin kimliği (kendi yazdığımızı tanımak için)
  const roomRef = ref(rtdb, 'watch/room');
  const hereRef = ref(rtdb, `watch/here/${uid}`);
  const chatRef = ref(rtdb, 'watch/chat');
  let room = null, partnerHere = false, player = null, playerReady = false, playerVideo = null;
  let quietUntil = 0;                      // uzaktan konum uygulandıktan hemen sonra sarma denetimini beklet
  let seeking = false, fs = false, nativeFs = false, hideTimer = 0;
  let history = [], openRow = null;        // son izlenenler, açık kaydırma satırı
  let historySig = '', swiping = false, redrawLater = false;
  const joinedAt = serverNow();

  // ---------- Arayüz ----------
  const linkInput = h('input', { class: 'input', type: 'url', inputmode: 'url', placeholder: 'YouTube linkini yapıştır', 'aria-label': 'YouTube linki' });
  const openBtn = h('button', { class: 'btn btn--primary', type: 'submit' }, 'Aç');
  const form = h('form', { class: 'watch-form', onsubmit: (e) => { e.preventDefault(); openFromLink(); } }, linkInput, openBtn);

  // Oynatıcı + kendi kontrollerimiz
  const playerHost = h('div', { class: 'watch-player__frame' });
  const reactionsLayer = h('div', { class: 'watch-reactions-layer', 'aria-hidden': 'true' });
  const msgFloats = h('div', { class: 'watch-msg-floats', 'aria-hidden': 'true' });
  const overlay = h('div', { class: 'watch-overlay', hidden: true });
  const tapHint = h('div', { class: 'watch-taphint' }, '👆 Videoya bir kez dokun, başlasın');

  const bigPlay = h('button', { class: 'wctl__big', type: 'button', 'aria-label': 'Oynat', onclick: (e) => { e.stopPropagation(); togglePlay(); } }, '▶');
  const playBtn = h('button', { class: 'wctl__btn', type: 'button', 'aria-label': 'Oynat', onclick: (e) => { e.stopPropagation(); togglePlay(); } }, '▶');
  const backBtn = h('button', { class: 'wctl__btn', type: 'button', 'aria-label': '10 saniye geri', onclick: (e) => { e.stopPropagation(); seekBy(-10); } }, '↺10');
  const fwdBtn = h('button', { class: 'wctl__btn', type: 'button', 'aria-label': '10 saniye ileri', onclick: (e) => { e.stopPropagation(); seekBy(10); } }, '10↻');
  const timeEl = h('span', { class: 'wctl__time' }, '0:00 / 0:00');
  const seekBar = h('input', { class: 'wctl__seek', type: 'range', min: '0', max: '0', step: '1', value: '0', 'aria-label': 'Videoda konum' });
  const muteBtn = h('button', { class: 'wctl__btn', type: 'button', 'aria-label': 'Sesi kapat', onclick: (e) => { e.stopPropagation(); toggleMute(); } }, '🔊');
  const fsBtn = h('button', { class: 'wctl__btn', type: 'button', 'aria-label': 'Tam ekran', onclick: (e) => { e.stopPropagation(); toggleFs(); } }, '⛶');
  const fsReact = h('div', { class: 'watch-fs-react', role: 'group', 'aria-label': 'Emoji gönder' },
    REACTIONS.map((e) => h('button', { class: 'watch-fs-react__btn', type: 'button', 'aria-label': `${e} gönder`, onclick: (ev) => { ev.stopPropagation(); sendChat({ emoji: e }); } }, e)));
  const controls = h('div', { class: 'wctl', onclick: () => toggleControls() },
    bigPlay,
    h('div', { class: 'wctl__bar', onclick: (e) => e.stopPropagation() },
      seekBar,
      h('div', { class: 'wctl__row' }, playBtn, backBtn, fwdBtn, timeEl, h('span', { class: 'wctl__spacer' }), muteBtn, fsBtn)));
  const playerBox = h('div', { class: 'watch-player show-controls' }, playerHost, reactionsLayer, msgFloats, controls, fsReact, tapHint, overlay);
  const status = h('p', { class: 'watch-status', 'aria-live': 'polite' });

  // İzlerken sohbet (emoji tepkileri de sohbete düşer)
  const reactBar = h('div', { class: 'watch-react-bar', role: 'group', 'aria-label': 'Emoji tepkisi gönder' },
    REACTIONS.map((e) => h('button', { class: 'watch-react', type: 'button', 'aria-label': `${e} gönder`, onclick: () => sendChat({ emoji: e }) }, e)));
  const chatList = h('div', { class: 'wchat__list', role: 'log', 'aria-label': 'İzlerken sohbet' });
  const chatEmpty = h('p', { class: 'wchat__empty muted small' }, 'Henüz mesaj yok. İzlerken buradan yazışabilirsiniz 💬');
  const chatInput = h('input', { class: 'input', type: 'text', maxlength: '500', placeholder: 'Mesaj yaz…', enterkeyhint: 'send', autocomplete: 'off', 'aria-label': 'Sohbet mesajı' });
  const chatForm = h('form', { class: 'wchat__form', onsubmit: (e) => { e.preventDefault(); sendText(); } },
    chatInput, h('button', { class: 'btn btn--primary', type: 'submit' }, 'Gönder'));
  const clearChatBtn = h('button', { class: 'btn btn--ghost btn--sm', type: 'button', onclick: clearChat }, 'Temizle');
  const chatBox = h('section', { class: 'wchat card' },
    h('div', { class: 'wchat__head' }, h('strong', {}, '💬 İzlerken sohbet'), clearChatBtn),
    reactBar, chatList, chatForm);
  add(chatList, chatEmpty);

  const historyEl = h('div', { class: 'watch-history' });
  const emptyBox = emptyState({ emoji: '🎬', title: 'Birlikte izleyelim', text: 'YouTube\'da bir video aç, "Paylaş → Bağlantıyı kopyala" de ve linki yukarıya yapıştır.' });

  add(page,
    h('div', { class: 'page-head' }, h('div', {}, h('h2', { class: 'page-title' }, 'Birlikte İzle'), h('p', { class: 'page-sub' }, 'Biriniz durdurunca ikinizde de durur.'))),
    form, emptyBox, playerBox, status, chatBox,
    h('div', { class: 'watch-history__head' }, h('h3', { class: 'watch-history__title' }, 'Son izlenenler'), h('small', { class: 'muted' }, 'Kapatmak / silmek için sağa kaydır ➜')),
    historyEl);
  playerBox.hidden = true;

  // ---------- Varlık (sayfada mıyım) ----------
  try { await onDisconnect(hereRef).remove(); await set(hereRef, true); } catch (e) { toast(errorMessage(e), { type: 'error' }); }
  scope.add(() => {
    // Sayfadan çıkarken oynuyorsa durdur, sonra varlığı kaldır
    if (room?.state === 'playing' && playerReady) writeRoom({ state: 'paused', pos: currentTime() }).catch(() => {});
    onDisconnect(hereRef).cancel().catch(() => {});
    remove(hereRef).catch(() => {});
    if (fs) setFs(false);
  });

  scope.add(onValue(ref(rtdb, `watch/here/${partnerUid}`), (s) => {
    const was = partnerHere;
    partnerHere = s.val() === true;
    if (was && !partnerHere && room?.state === 'playing') {
      // Partner çıktı: iki tarafta da durdur
      quiet(); player?.pauseVideo?.();
      writeRoom({ state: 'paused', pos: currentTime() }).catch(() => {});
      toast(`${userName(partnerUid)} ayrıldı, video durduruldu ⏸`);
    }
    if (!was && partnerHere) applyRemote(); // partner geldi: kaldığımız yerden eşitle
    drawOverlay(); drawStatus();
  }));

  // ---------- Oda ----------
  scope.add(onValue(roomRef, async (s) => {
    const prev = room;
    room = s.val();
    if (!room?.videoId) {
      // Video kapatıldı (iki tarafta da)
      emptyBox.hidden = false; playerBox.hidden = true;
      if (fs) setFs(false);
      destroyPlayer();
      if (prev?.videoId) toast('Video kapatıldı 🎬');
      drawStatus(); drawHistory(); return;
    }
    emptyBox.hidden = true; playerBox.hidden = false;
    if (prev?.videoId !== room.videoId) drawHistory();
    await ensurePlayer(room.videoId);
    if (room.cid !== cid) applyRemote();
    drawOverlay(); drawStatus(); drawControls();
  }, (e) => toast(errorMessage(e), { type: 'error' })));

  function writeRoom(patch) {
    return update(roomRef, { ...patch, at: rtdbServerTimestamp(), by: uid, cid });
  }
  const quiet = (ms = 1500) => { quietUntil = Date.now() + ms; };
  const currentTime = () => { try { return Math.max(0, Number(player?.getCurrentTime?.()) || 0); } catch { return 0; } };
  const duration = () => { try { return Math.max(0, Number(player?.getDuration?.()) || 0); } catch { return 0; } };
  const expectedPos = () => (!room ? 0 : room.state === 'playing' ? room.pos + Math.max(0, (serverNow() - (room.at || serverNow())) / 1000) : room.pos);

  // ---------- Oynatıcı ----------
  async function ensurePlayer(videoId) {
    if (player && playerVideo === videoId) return;
    let YT;
    try { YT = await loadYouTubeApi(); } catch (e) { fill(playerHost, h('p', { class: 'watch-error' }, e.message)); return; }
    if (scope.disposed || room?.videoId !== videoId) return;
    if (player && playerReady) {
      playerVideo = videoId; quiet();
      player.cueVideoById({ videoId, startSeconds: expectedPos() });
      return;
    }
    if (player) return; // hazırlanıyor
    playerVideo = videoId; playerReady = false;
    const mount = h('div', { id: `yt-${cid}-${randomId(3)}` });
    fill(playerHost, mount);
    player = new YT.Player(mount, {
      videoId, width: '100%', height: '100%',
      playerVars: { playsinline: 1, rel: 0, modestbranding: 1, controls: 0, disablekb: 1, fs: 0, iv_load_policy: 3, origin: location.origin },
      events: {
        onReady: (e) => {
          if (!player || (e?.target && e.target !== player)) return; // bu arada kapatılmış eski oynatıcı
          playerReady = true;
          if (playerVideo !== room?.videoId && room?.videoId) { playerVideo = room.videoId; player.cueVideoById({ videoId: room.videoId, startSeconds: expectedPos() }); }
          applyRemote(); saveTitle(); drawControls();
        },
        onStateChange: (e) => { if (player && (!e?.target || e.target === player)) onLocalState(e.data); },
      },
    });
  }
  function destroyPlayer() {
    try { player?.destroy?.(); } catch {}
    player = null; playerReady = false; playerVideo = null;
    clear(playerHost);
    needTap(false);
  }
  scope.add(destroyPlayer);

  /** Odadaki durumu bu cihaza uygula. */
  function applyRemote() {
    if (!player || !playerReady || !room?.videoId) return;
    quiet();
    const target = expectedPos();
    if (Math.abs(currentTime() - target) > 1.2) player.seekTo(target, true);
    if (room.state === 'playing' && partnerHere) {
      player.playVideo();
      checkStarted();
    } else if (player.getPlayerState?.() === PLAYING) player.pauseVideo();
    drawControls();
  }

  // iPhone, sesli videonun kendiliğinden başlamasına izin vermeyebilir → videoya bir kez dokunmak gerekir
  function checkStarted() {
    scope.timeout(() => {
      const st = player?.getPlayerState?.();
      if (room?.state === 'playing' && partnerHere && st !== PLAYING && st !== BUFFERING) needTap(true);
    }, 1800);
  }
  function needTap(on) { playerBox.classList.toggle('needs-tap', !!on); }

  /**
   * Oynatıcı olayları. Odanın durumuyla AYNI olan olaylar (bizim uyguladıklarımız) yok sayılır;
   * FARKLI olanlar kullanıcının bu cihazdaki dokunuşudur ve odaya yazılır.
   */
  function onLocalState(state) {
    if (state === PLAYING || state === BUFFERING) needTap(false);
    drawControls();
    if (!room?.videoId) return;
    if (state === PLAYING) {
      if (room.state === 'playing') { drawOverlay(); return; }
      if (!partnerHere) {
        quiet(); player.pauseVideo();
        toast(`${userName(partnerUid)} sayfada değil. İkiniz de buradayken oynatabilirsiniz 💕`);
        return;
      }
      writeRoom({ state: 'playing', pos: currentTime() }).catch((e) => toast(errorMessage(e), { type: 'error' }));
      drawOverlay();
    } else if ((state === PAUSED || state === ENDED) && room.state === 'playing') {
      writeRoom({ state: 'paused', pos: currentTime() }).catch((e) => toast(errorMessage(e), { type: 'error' }));
    }
  }

  // İleri/geri sarmayı yakala (YouTube'un ayrı bir "sardı" olayı yok)
  scope.interval(() => {
    if (!player || !playerReady || !room?.videoId || Date.now() < quietUntil) return;
    const st = player.getPlayerState?.();
    const drift = Math.abs(currentTime() - expectedPos());
    if (room.state === 'paused' && st === PAUSED && drift > 1.5) writeRoom({ state: 'paused', pos: currentTime() }).catch(() => {});
    if (room.state === 'playing' && st === PLAYING && drift > 3) writeRoom({ state: 'playing', pos: currentTime() }).catch(() => {});
  }, 1000);

  // ---------- Kendi kontrollerimiz ----------
  function togglePlay() {
    if (!room?.videoId || !player || !playerReady) return;
    if (room.state === 'playing') {
      quiet(); player.pauseVideo();
      writeRoom({ state: 'paused', pos: currentTime() }).catch((e) => toast(errorMessage(e), { type: 'error' }));
    } else {
      if (!partnerHere) { toast(`${userName(partnerUid)} sayfada değil. İkiniz de buradayken oynatabilirsiniz 💕`); return; }
      const pos = currentTime();
      writeRoom({ state: 'playing', pos }).catch((e) => toast(errorMessage(e), { type: 'error' }));
      quiet(); player.playVideo();
      checkStarted();
    }
    drawControls(); bumpControls();
  }
  function seekTo(t) {
    if (!room?.videoId || !player || !playerReady) return;
    const dur = duration();
    const pos = Math.max(0, Math.min(dur ? dur - 1 : t, t));
    quiet(); player.seekTo(pos, true);
    writeRoom({ state: room.state, pos }).catch((e) => toast(errorMessage(e), { type: 'error' }));
    drawControls(); bumpControls();
  }
  const seekBy = (d) => seekTo(currentTime() + d);
  function toggleMute() {
    if (!player) return;
    try { if (player.isMuted?.()) player.unMute(); else player.mute(); } catch {}
    setTimeout(drawControls, 50); bumpControls();
  }
  seekBar.addEventListener('input', () => { seeking = true; timeEl.textContent = `${fmtClock(seekBar.value)} / ${fmtClock(duration())}`; });
  seekBar.addEventListener('change', () => { seeking = false; seekTo(Number(seekBar.value)); });
  seekBar.addEventListener('click', (e) => e.stopPropagation());

  function drawControls() {
    const playing = room?.state === 'playing';
    const icon = playing ? '❚❚' : '▶';
    const label = playing ? 'Durdur' : 'Oynat';
    playBtn.textContent = icon; playBtn.setAttribute('aria-label', label);
    bigPlay.textContent = icon; bigPlay.setAttribute('aria-label', label);
    playerBox.classList.toggle('is-playing', playing);
    const dur = duration(), cur = currentTime();
    if (!seeking) {
      seekBar.max = String(Math.floor(dur));
      seekBar.value = String(Math.floor(cur));
      timeEl.textContent = `${fmtClock(cur)} / ${fmtClock(dur)}`;
    }
    seekBar.style.setProperty('--p', dur ? `${(Math.min(cur, dur) / dur) * 100}%` : '0%');
    let muted = false; try { muted = !!player?.isMuted?.(); } catch {}
    muteBtn.textContent = muted ? '🔇' : '🔊';
    muteBtn.setAttribute('aria-label', muted ? 'Sesi aç' : 'Sesi kapat');
    fsBtn.setAttribute('aria-label', fs ? 'Tam ekrandan çık' : 'Tam ekran');
    fsBtn.textContent = fs ? '✕' : '⛶';
  }
  scope.interval(drawControls, 500);

  // Kontroller oynarken 3 sn sonra gizlenir; videoya dokununca geri gelir
  function bumpControls() {
    playerBox.classList.add('show-controls');
    clearTimeout(hideTimer);
    hideTimer = setTimeout(() => { if (room?.state === 'playing' && !seeking) playerBox.classList.remove('show-controls'); }, 3200);
  }
  function toggleControls() {
    if (playerBox.classList.contains('show-controls') && room?.state === 'playing') playerBox.classList.remove('show-controls');
    else bumpControls();
  }
  scope.add(() => clearTimeout(hideTimer));

  // Tam ekran: Android'de gerçek tam ekran, iPhone'da sayfayı kaplayan görünüm
  function setFs(on) {
    fs = on;
    playerBox.classList.toggle('is-fs', on);
    document.documentElement.classList.toggle('watch-fs', on);
    if (on) {
      if (playerBox.requestFullscreen && !/iPhone|iPod/.test(navigator.userAgent)) {
        playerBox.requestFullscreen({ navigationUI: 'hide' }).then(() => {
          nativeFs = true;
          try { screen.orientation?.lock?.('landscape').catch(() => {}); } catch {}
        }).catch(() => {});
      }
    } else if (nativeFs) {
      nativeFs = false;
      try { screen.orientation?.unlock?.(); } catch {}
      if (document.fullscreenElement) document.exitFullscreen().catch(() => {});
    }
    drawControls(); bumpControls();
  }
  const toggleFs = () => setFs(!fs);
  scope.on(document, 'fullscreenchange', () => { if (nativeFs && !document.fullscreenElement) { nativeFs = false; if (fs) setFs(false); } });
  scope.on(document, 'keydown', (e) => { if (e.key === 'Escape' && fs && !nativeFs) setFs(false); });

  function drawOverlay() {
    clear(overlay);
    if (room?.videoId && !partnerHere) {
      overlay.hidden = false;
      add(overlay, h('div', { class: 'watch-overlay__box' }, h('span', { class: 'heart-loader' }, '❤'), h('strong', {}, `${userName(partnerUid)} bekleniyor…`),
        h('small', {}, 'O da "Birlikte İzle" sayfasını açınca başlayabilirsiniz.')));
      return;
    }
    overlay.hidden = true;
  }

  function drawStatus() {
    if (!room?.videoId) { status.textContent = partnerHere ? `🟢 ${userName(partnerUid)} burada` : `⚪ ${userName(partnerUid)} sayfada değil`; return; }
    const who = room.by === uid ? 'Sen' : userName(room.by);
    const what = room.state === 'playing' ? 'oynattı ▶️' : 'durdurdu ⏸';
    status.textContent = `${partnerHere ? `🟢 ${userName(partnerUid)} burada` : `⚪ ${userName(partnerUid)} sayfada değil`} · ${who} ${what}`;
  }
  scope.interval(drawStatus, 5000);

  // ---------- Video açma / kapatma ----------
  async function openFromLink(link = linkInput.value) {
    const id = parseYouTubeId(link);
    if (!id) { toast('Bu bir YouTube linki gibi görünmüyor. YouTube\'da Paylaş → Bağlantıyı kopyala ile al.', { type: 'error', duration: 5000 }); return; }
    setLoading(openBtn, true);
    try {
      await writeRoom({ videoId: id, state: 'paused', pos: parseStartSeconds(link) });
      await update(ref(rtdb, `watch/history/${id}`), { videoId: id, by: uid, at: rtdbServerTimestamp() });
      linkInput.value = '';
      toast(`Video açıldı 🎬 ${partnerHere ? 'Oynat\'a bas, ikinizde de başlar.' : `${userName(partnerUid)} gelince başlayabilirsiniz.`}`);
    } catch (e) { toast(errorMessage(e), { type: 'error' }); }
    finally { setLoading(openBtn, false); }
  }

  /** Videoyu iki tarafta da kapatır ve listeden kaldırır. */
  async function closeVideo(videoId) {
    try {
      if (room?.videoId === videoId) await set(roomRef, null);
      await remove(ref(rtdb, `watch/history/${videoId}`));
    } catch (e) { toast(errorMessage(e), { type: 'error' }); }
  }

  /** Video adını son izlenenlere yaz (oynatıcı başlığı öğrenince). */
  function saveTitle() {
    try {
      const d = player?.getVideoData?.();
      const cur = history.find((v) => v.videoId === room?.videoId);
      if (d?.title && room?.videoId && cur && cur.title !== d.title) update(ref(rtdb, `watch/history/${room.videoId}`), { title: String(d.title).slice(0, 200) }).catch(() => {});
    } catch {}
  }
  scope.interval(saveTitle, 4000);

  // ---------- Son izlenenler (sağa kaydırınca kapat / sil) ----------
  scope.add(onValue(rtdbQuery(ref(rtdb, 'watch/history'), orderByChild('at'), limitToLast(10)), (s) => {
    const list = [];
    s.forEach((c) => { list.push(c.val()); });
    history = list.reverse();
    drawHistory();
  }));

  function drawHistory() {
    const sig = JSON.stringify([room?.videoId || '', history.map((v) => [v.videoId, v.title || '', v.by, v.at])]);
    if (sig === historySig) return;
    // Kaydırma sürerken/satır açıkken listeyi yeniden çizme (açık satır kapanmasın); bitince çiz
    if (swiping || openRow) { redrawLater = true; return; }
    historySig = sig; redrawLater = false;
    openRow = null;
    clear(historyEl);
    if (!history.length) { add(historyEl, h('p', { class: 'muted small' }, 'Henüz video açılmadı.')); return; }
    for (const v of history) {
      const current = room?.videoId === v.videoId;
      const item = h('div', { class: `watch-history__item swipe__content${current ? ' is-current' : ''}`, role: 'button', tabindex: '0', 'aria-label': `${v.title || 'YouTube videosu'} — aç` },
        h('img', { src: thumbUrl(v.videoId), alt: '', loading: 'lazy', draggable: 'false' }),
        h('span', { class: 'watch-history__text' },
          current ? h('span', { class: 'watch-history__now' }, '▶ Şu an izleniyor') : null,
          h('strong', {}, v.title || 'YouTube videosu'),
          h('small', { class: 'muted' }, `${userName(v.by)} · ${relativeTime(v.at)}`)));
      add(historyEl, swipeRow(item, {
        label: current ? 'Videoyu kapat' : 'Sil',
        onAction: () => closeVideo(v.videoId),
        onTap: () => { if (!current) openFromLink(v.videoId); },
      }));
    }
  }

  /** Sağa kaydırınca arkadaki düğmeyi gösteren satır. */
  function swipeRow(content, { label, onAction, onTap }) {
    const W = 128;
    const action = h('button', { class: 'swipe__action', type: 'button', tabindex: '-1', onclick: (e) => { e.stopPropagation(); onAction(); } }, '✕ ', label);
    const row = h('div', { class: 'swipe' }, action, content);
    let sx = 0, sy = 0, dx = 0, down = false, decided = false, horiz = false, isOpen = false, moved = false;
    const setX = (x, anim) => {
      content.style.transition = anim ? 'transform .22s cubic-bezier(.2,.8,.2,1)' : 'none';
      content.style.transform = x ? `translateX(${x}px)` : '';
      row.classList.toggle('is-open', x > 0);
    };
    const close = () => { isOpen = false; setX(0, true); if (openRow?.row === row) openRow = null; if (redrawLater) setTimeout(drawHistory, 250); };
    content.addEventListener('pointerdown', (e) => {
      if (e.button > 0) return;
      down = true; swiping = true; decided = false; horiz = false; moved = false; sx = e.clientX; sy = e.clientY; dx = isOpen ? W : 0;
    });
    content.addEventListener('pointermove', (e) => {
      if (!down) return;
      const mx = e.clientX - sx, my = e.clientY - sy;
      if (!decided) {
        if (Math.abs(mx) < 8 && Math.abs(my) < 8) return;
        decided = true; horiz = Math.abs(mx) > Math.abs(my);
        if (horiz) { try { content.setPointerCapture(e.pointerId); } catch {} if (openRow && openRow.row !== row) openRow.close(); }
      }
      if (!horiz) return;
      moved = true;
      dx = Math.max(0, Math.min(W * 1.35, (isOpen ? W : 0) + mx));
      setX(dx, false);
    });
    const end = () => {
      if (!down) return;
      down = false; swiping = false;
      if (!horiz) { if (redrawLater && !openRow) setTimeout(drawHistory, 0); return; }
      isOpen = dx > W * 0.45;
      setX(isOpen ? W : 0, true);
      openRow = isOpen ? { row, close } : (openRow?.row === row ? null : openRow);
      if (!openRow && redrawLater) setTimeout(drawHistory, 250);
    };
    content.addEventListener('pointerup', end);
    content.addEventListener('pointercancel', end);
    content.addEventListener('click', () => {
      if (moved) { moved = false; return; }
      if (isOpen) { close(); return; }
      if (openRow) { openRow.close(); return; }
      onTap();
    });
    content.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') onTap();
      if (e.key === 'ArrowRight') { isOpen = true; setX(W, true); openRow = { row, close }; }
      if (e.key === 'ArrowLeft' || e.key === 'Escape') close();
    });
    return row;
  }

  // ---------- İzlerken sohbet + emoji tepkileri ----------
  const chatEls = new Map();
  async function sendChat(msg) {
    try { await set(push(chatRef), { by: uid, ...msg, at: rtdbServerTimestamp() }); }
    catch (e) { toast(errorMessage(e), { type: 'error' }); }
  }
  function sendText() {
    const text = chatInput.value.trim().slice(0, 500);
    if (!text) return;
    chatInput.value = '';
    sendChat({ text });
  }
  async function clearChat() {
    if (!(await confirmDialog({ title: 'Sohbet temizlensin mi?', message: 'İzlerken yazılan mesajlar ikinizde de silinir.', confirmText: 'Temizle', danger: true }))) return;
    try { await remove(chatRef); } catch (e) { toast(errorMessage(e), { type: 'error' }); }
  }

  const chatQuery = rtdbQuery(chatRef, limitToLast(CHAT_LIMIT));
  scope.add(onChildAdded(chatQuery, (s) => {
    const m = s.val();
    if (!m || chatEls.has(s.key) || (!m.text && !m.emoji)) return;
    const mine = m.by === uid;
    const nearBottom = chatList.scrollHeight - chatList.scrollTop - chatList.clientHeight < 60;
    const el = h('div', { class: `wchat__msg${mine ? ' is-mine' : ''}${m.emoji ? ' is-emoji' : ''}` },
      h('span', { class: 'wchat__bubble' }, m.emoji || m.text),
      h('small', { class: 'wchat__meta' }, `${mine ? 'Sen' : userName(m.by)} · ${formatTime(typeof m.at === 'number' ? m.at : serverNow())}`));
    chatEls.set(s.key, el);
    chatEmpty.remove();
    add(chatList, el);
    if (nearBottom || mine) chatList.scrollTop = chatList.scrollHeight;
    // Yeni gelenler videonun üstünde de görünür
    const fresh = typeof m.at !== 'number' || m.at >= joinedAt - 5000;
    if (fresh) {
      if (m.emoji) floatEmoji(m);
      else floatText(m);
    }
  }, (e) => toast(errorMessage(e), { type: 'error' })));
  scope.add(onChildRemoved(chatQuery, (s) => {
    chatEls.get(s.key)?.remove();
    chatEls.delete(s.key);
    if (!chatEls.size) add(chatList, chatEmpty);
  }));

  function floatEmoji(m) {
    const el = h('span', { class: 'reaction-float' }, m.emoji, h('small', {}, m.by === uid ? 'Sen' : userName(m.by)));
    el.style.left = `${10 + Math.random() * 70}%`;
    add(reactionsLayer, el);
    setTimeout(() => el.remove(), 2700);
  }
  function floatText(m) {
    const el = h('div', { class: 'watch-msg-float' }, h('strong', {}, `${m.by === uid ? 'Sen' : userName(m.by)}: `), m.text);
    add(msgFloats, el);
    while (msgFloats.children.length > 3) msgFloats.firstChild.remove();
    setTimeout(() => el.remove(), 5000);
  }

  drawStatus();
}
