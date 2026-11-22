// Birlikte İzle 🎬 — YouTube videosunu iki cihazda eşzamanlı izleme.
//
// Realtime Database:
//   watch/room            { videoId, state: 'playing'|'paused', pos, at (sunucu zamanı), by, cid }
//   watch/here/{kişi}     true — sayfada olan (bağlantı koparsa sunucu siler)
//   watch/history/{video} { videoId, title, by, at } — son izlenenler
//   watch/reactions/{id}  { by, emoji, at } — anlık emoji tepkileri
//
// Eşleşme: kim oynatır/durdurur/sararsa "room" kaydını günceller; diğer cihaz kaydı görünce
// kendi oynatıcısını aynı konuma ve duruma getirir. Oynarken konum = pos + (şimdi - at).
// İkiniz de sayfada değilseniz video oynamaz; biri çıkarsa video iki tarafta da durur.
import { rtdb } from '../firebase-config.js';
import {
  ref, set, update, remove, push, onValue, onChildAdded, onDisconnect, rtdbQuery, orderByChild, limitToLast,
  rtdbServerTimestamp,
} from '../vendor/firebase.js';
import { getState, serverNow } from '../state.js';
import { userName } from '../constants.js';
import { h, clear, fill, add, randomId } from '../utils/helpers.js';
import { toast, emptyState, errorMessage, setLoading } from '../utils/ui.js';
import { relativeTime } from '../utils/dates.js';
import { parseYouTubeId, parseStartSeconds, thumbUrl, loadYouTubeApi } from '../utils/youtube.js';

export const REACTIONS = ['❤️', '😂', '😮', '😢', '🔥', '👏'];
const PLAYING = 1, PAUSED = 2, ENDED = 0, BUFFERING = 3;

export default async function watch(page, { scope }) {
  const { uid, partnerUid } = getState();
  const cid = randomId(8);                 // bu sekmenin kimliği (kendi yazdığımızı tanımak için)
  const roomRef = ref(rtdb, 'watch/room');
  const hereRef = ref(rtdb, `watch/here/${uid}`);
  let room = null, partnerHere = false, player = null, playerReady = false, playerVideo = null;
  let quietUntil = 0;                      // uzaktan konum uygulandıktan hemen sonra sarma denetimini beklet
  const joinedAt = serverNow();

  // ---------- Arayüz ----------
  const linkInput = h('input', { class: 'input', type: 'url', inputmode: 'url', placeholder: 'YouTube linkini yapıştır', 'aria-label': 'YouTube linki' });
  const openBtn = h('button', { class: 'btn btn--primary', type: 'submit' }, 'Aç');
  const form = h('form', { class: 'watch-form', onsubmit: (e) => { e.preventDefault(); openFromLink(); } }, linkInput, openBtn);
  const playerHost = h('div', { class: 'watch-player__frame' });
  const reactionsLayer = h('div', { class: 'watch-reactions-layer', 'aria-hidden': 'true' });
  const overlay = h('div', { class: 'watch-overlay', hidden: true });
  const playerBox = h('div', { class: 'watch-player' }, playerHost, reactionsLayer, overlay);
  const status = h('p', { class: 'watch-status', 'aria-live': 'polite' });
  const reactBar = h('div', { class: 'watch-react-bar', role: 'group', 'aria-label': 'Emoji tepkisi gönder' },
    REACTIONS.map((e) => h('button', { class: 'watch-react', type: 'button', 'aria-label': `${e} gönder`, onclick: () => sendReaction(e) }, e)));
  const historyEl = h('div', { class: 'watch-history' });
  const emptyBox = emptyState({ emoji: '🎬', title: 'Birlikte izleyelim', text: 'YouTube\'da bir video aç, "Paylaş → Bağlantıyı kopyala" de ve linki yukarıya yapıştır.' });

  add(page,
    h('div', { class: 'page-head' }, h('div', {}, h('h2', { class: 'page-title' }, 'Birlikte İzle'), h('p', { class: 'page-sub' }, 'Biriniz durdurunca ikinizde de durur.'))),
    form, emptyBox, playerBox, status, reactBar,
    h('h3', { class: 'watch-history__title' }, 'Son izlenenler'), historyEl);
  playerBox.hidden = true; reactBar.hidden = true;

  // ---------- Varlık (sayfada mıyım) ----------
  try { await onDisconnect(hereRef).remove(); await set(hereRef, true); } catch (e) { toast(errorMessage(e), { type: 'error' }); }
  scope.add(() => {
    // Sayfadan çıkarken oynuyorsa durdur, sonra varlığı kaldır
    if (room?.state === 'playing' && playerReady) writeRoom({ state: 'paused', pos: currentTime() }).catch(() => {});
    onDisconnect(hereRef).cancel().catch(() => {});
    remove(hereRef).catch(() => {});
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
    room = s.val();
    if (!room?.videoId) { emptyBox.hidden = false; playerBox.hidden = true; reactBar.hidden = true; drawStatus(); return; }
    emptyBox.hidden = true; playerBox.hidden = false; reactBar.hidden = false;
    await ensurePlayer(room.videoId);
    if (room.cid !== cid) applyRemote();
    drawOverlay(); drawStatus();
  }, (e) => toast(errorMessage(e), { type: 'error' })));

  function writeRoom(patch) {
    return update(roomRef, { ...patch, at: rtdbServerTimestamp(), by: uid, cid });
  }
  const quiet = (ms = 1500) => { quietUntil = Date.now() + ms; };
  const currentTime = () => { try { return Math.max(0, Number(player?.getCurrentTime?.()) || 0); } catch { return 0; } };
  const expectedPos = () => (!room ? 0 : room.state === 'playing' ? room.pos + Math.max(0, (serverNow() - (room.at || serverNow())) / 1000) : room.pos);

  // ---------- Oynatıcı ----------
  async function ensurePlayer(videoId) {
    if (player && playerVideo === videoId) return;
    let YT;
    try { YT = await loadYouTubeApi(); } catch (e) { fill(playerHost, h('p', { class: 'watch-error' }, e.message)); return; }
    if (scope.disposed) return;
    if (player && playerReady) {
      playerVideo = videoId; quiet();
      player.cueVideoById({ videoId, startSeconds: expectedPos() });
      return;
    }
    playerVideo = videoId; playerReady = false;
    const mount = h('div', { id: `yt-${cid}` });
    fill(playerHost, mount);
    player = new YT.Player(mount, {
      videoId, width: '100%', height: '100%',
      playerVars: { playsinline: 1, rel: 0, modestbranding: 1, origin: location.origin },
      events: {
        onReady: () => { playerReady = true; applyRemote(); saveTitle(); },
        onStateChange: (e) => onLocalState(e.data),
      },
    });
    scope.add(() => { try { player?.destroy?.(); } catch {} player = null; });
  }

  /** Odadaki durumu bu cihaza uygula. */
  function applyRemote() {
    if (!player || !playerReady || !room) return;
    quiet();
    const target = expectedPos();
    if (Math.abs(currentTime() - target) > 1.2) player.seekTo(target, true);
    if (room.state === 'playing' && partnerHere) {
      player.playVideo();
      // iPhone, sesli videonun kendiliğinden başlamasına izin vermeyebilir → dokunma iste
      setTimeout(() => { if (room?.state === 'playing' && partnerHere && player?.getPlayerState?.() !== PLAYING && player?.getPlayerState?.() !== BUFFERING) drawOverlay(true); }, 1800);
    } else if (player.getPlayerState?.() === PLAYING) player.pauseVideo();
  }

  /**
   * Oynatıcı olayları. Odanın durumuyla AYNI olan olaylar (bizim uzaktan uyguladıklarımız) yok sayılır;
   * FARKLI olanlar kullanıcının bu cihazdaki basışıdır ve odaya yazılır.
   */
  function onLocalState(state) {
    if (!room) return;
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
    if (!player || !playerReady || !room || Date.now() < quietUntil) return;
    const st = player.getPlayerState?.();
    const drift = Math.abs(currentTime() - expectedPos());
    if (room.state === 'paused' && st === PAUSED && drift > 1.5) writeRoom({ state: 'paused', pos: currentTime() }).catch(() => {});
    if (room.state === 'playing' && st === PLAYING && drift > 3) writeRoom({ state: 'playing', pos: currentTime() }).catch(() => {});
  }, 1000);

  function drawOverlay(needTap = false) {
    clear(overlay);
    if (room?.videoId && !partnerHere) {
      overlay.hidden = false;
      add(overlay, h('div', { class: 'watch-overlay__box' }, h('span', { class: 'heart-loader' }, '❤'), h('strong', {}, `${userName(partnerUid)} bekleniyor…`),
        h('small', {}, 'O da "Birlikte İzle" sayfasını açınca başlayabilirsiniz.')));
      return;
    }
    if (needTap) {
      overlay.hidden = false;
      add(overlay, h('button', { class: 'watch-overlay__tap', type: 'button', onclick: () => { overlay.hidden = true; quiet(); player?.playVideo?.(); setTimeout(applyRemote, 300); } }, '▶️ Başlamak için dokun'));
      return;
    }
    overlay.hidden = true;
  }

  function drawStatus() {
    if (!room?.videoId) { status.textContent = partnerHere ? `🟢 ${userName(partnerUid)} burada` : ''; return; }
    const who = room.by === uid ? 'Sen' : userName(room.by);
    const what = room.state === 'playing' ? 'oynattı ▶️' : 'durdurdu ⏸';
    status.textContent = `${partnerHere ? `🟢 ${userName(partnerUid)} burada` : `⚪ ${userName(partnerUid)} sayfada değil`} · ${who} ${what}`;
  }
  scope.interval(drawStatus, 5000);

  // ---------- Video açma ----------
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

  /** Video adını son izlenenlere yaz (oynatıcı başlığı öğrenince). */
  function saveTitle() {
    try {
      const d = player?.getVideoData?.();
      if (d?.title && room?.videoId && d.video_id !== undefined) update(ref(rtdb, `watch/history/${room.videoId}`), { title: String(d.title).slice(0, 200) }).catch(() => {});
    } catch {}
  }
  scope.interval(saveTitle, 4000);

  // ---------- Son izlenenler ----------
  scope.add(onValue(rtdbQuery(ref(rtdb, 'watch/history'), orderByChild('at'), limitToLast(10)), (s) => {
    const list = [];
    s.forEach((c) => { list.push(c.val()); });
    list.reverse();
    clear(historyEl);
    if (!list.length) { add(historyEl, h('p', { class: 'muted small' }, 'Henüz video açılmadı.')); return; }
    for (const v of list) {
      add(historyEl, h('button', { class: `watch-history__item${room?.videoId === v.videoId ? ' is-current' : ''}`, type: 'button', onclick: () => openFromLink(v.videoId) },
        h('img', { src: thumbUrl(v.videoId), alt: '', loading: 'lazy' }),
        h('span', { class: 'watch-history__text' }, h('strong', {}, v.title || 'YouTube videosu'), h('small', { class: 'muted' }, `${userName(v.by)} · ${relativeTime(v.at)}`))));
    }
  }));

  // ---------- Emoji tepkileri ----------
  async function sendReaction(emoji) {
    try {
      const r = push(ref(rtdb, 'watch/reactions'));
      await set(r, { by: uid, emoji, at: rtdbServerTimestamp() });
      setTimeout(() => remove(r).catch(() => {}), 10000); // birikmesin
    } catch (e) { toast(errorMessage(e), { type: 'error' }); }
  }
  scope.add(onChildAdded(rtdbQuery(ref(rtdb, 'watch/reactions'), limitToLast(5)), (s) => {
    const r = s.val();
    if (!r || typeof r.at !== 'number' || r.at < joinedAt - 3000) return;
    const el = h('span', { class: 'reaction-float' }, r.emoji, h('small', {}, userName(r.by)));
    el.style.left = `${10 + Math.random() * 75}%`;
    add(reactionsLayer, el);
    setTimeout(() => el.remove(), 2600);
  }));
}
