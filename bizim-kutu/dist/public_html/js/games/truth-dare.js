// OYUN 3 — Doğruluk mu Cesaret mi? (romantik, eğlenceli, saygılı)
import { h, clear, randomInt, add } from '../utils/helpers.js';
import { validateText } from '../utils/validation.js';
import { turnBanner, resultTitle, otherOf, toArray, winnerByScore, draft, clearDraft } from './common.js';

export const TRUTHS = [
  'Bana âşık olduğunu ilk ne zaman fark ettin?',
  'Benimle ilgili hiç söylemediğin tatlı bir sır var mı?',
  'İlk mesajımı aldığında ne düşündün?',
  'Benim en sevdiğin fotoğrafım hangisi ve neden?',
  'Benimle ilgili en çok gurur duyduğun şey ne?',
  'Seni en son ne zaman gizlice izlerken yakaladım (ya da yakalayamadım)?',
  'Benimle yaşamak istediğin ama henüz söylemediğin bir hayal ne?',
  'Hiç benim için bir şeyi gizlice provası yaptın mı?',
  'Beni ilk gördüğünde aklından geçen ilk cümle neydi?',
  'Bizim şarkımız sence hangisi olmalı?',
  'Benim hangi huyum seni en çok güldürüyor?',
  'Hiç sana söylediğim bir sözü defalarca kafanda tekrar ettin mi? Hangisi?',
  'Bende değiştirmek istediğin minicik bir şey var mı?',
  'Benimle tanışmasaydın şu an nerede olurdun sence?',
  'Birlikteyken en mutlu hissettiğin an hangisiydi?',
  'Beni kıskandığın oldu mu? Ne zaman?',
  'Benim için yaptığın en romantik şey sence hangisiydi?',
  'Ailene benden ilk nasıl bahsettin?',
  'Bana hiç söylemediğin bir lakap var mı?',
  'İlişkimizde en çok neye minnettarsın?',
  'Benimle ilgili gördüğün en tatlı rüya neydi?',
  'Mesajlarımı okurken hiç sesli güldüğün oldu mu?',
  'Bana söylemekten en çok utandığın iltifat ne?',
  'Seni en çok etkileyen hediyem hangisiydi?',
  'İlk tartışmamızdan sonra ne hissettin?',
  'Benimle ilgili hangi küçük detayı herkesten iyi biliyorsun?',
  'Birlikte yaşlandığımızı hayal ettiğinde ne görüyorsun?',
  'Benim yüzünden hiç gece uyuyamadığın oldu mu?',
  'Bana en çok benzediğini düşündüğün film karakteri kim?',
  'Benden öğrendiğin en güzel şey ne?',
  'Benim hangi sesimi/kelimemi taklit edebilirsin? Şimdi göster!',
  'İlişkimizin ilk gününe dönebilsen neyi farklı yapardın?',
  'Benim için en zor söylediğin cümle hangisiydi?',
  'Hiç benim yüzümden bir planını iptal ettin mi?',
  'Birlikte en çok gitmek istediğin şehir neresi ve orada ne yapardık?',
  'Benimle ilgili en büyük korkun ne?',
  'Sence ilişkimizin süper gücü ne?',
  'Beni üç kelimeyle anlatır mısın?',
  'Bana hiç kızıp sonra hak verdiğin oldu mu?',
  'Seni en son ne zaman gerçekten şaşırttım?',
];

export const DARES = [
  'Bana şu an en içten iltifatını sesli mesaj gibi yazarak gönder.',
  'Bir dakika boyunca sadece emojilerle konuş.',
  'Bana ilk buluşmamızı 3 cümlelik bir masal gibi anlat.',
  'Bana bir aşk şiiri yaz (en az 4 dize, kafiye şart değil 😄).',
  'Bugün beni neden sevdiğini 5 maddede sırala.',
  'En sevdiğin şarkıdan bir dizeyi bana ithaf et.',
  'Bana bir sonraki buluşmamız için sürpriz bir plan öner.',
  'Telefon galerindeki en komik fotoğrafımızı tarif et.',
  'Bana 10 saniye içinde 5 tatlı lakap bul.',
  'En sevdiğim yemeği tarif ediyormuş gibi bir “aşk tarifi” yaz.',
  'Bir sonraki görüşmemizde bana sarılma sayını şimdiden söz ver.',
  'Bana bugün bir “sevgi kuponu” ver (ör. 1 kahve ısmarlama hakkı).',
  'Ortak bir şarkı seç ve neden “bizim şarkımız” olmalı anlat.',
  'Bana gelecekten bir mesaj yaz: “10 yıl sonra biz…”',
  'Hayalindeki ortak tatilimizi 4 emojiyle anlat.',
  'Bana bir aşk mektubunun ilk cümlesini yaz.',
  'Birlikte yapacağımız yeni bir hafta sonu ritüeli icat et.',
  'Bana en sevdiğin anımızı bir film fragmanı gibi anlat.',
  'Bir dakika içinde benimle ilgili 3 güzel anıyı hatırla ve yaz.',
  'Bana bir sonraki mesajını tamamen şarkı sözleriyle yaz.',
  'Yarın sabah bana ilk “günaydın” mesajını çok yaratıcı yazacağına söz ver.',
  'Aşkımızı bir hava durumu raporu gibi anlat.',
  'Bana bir sonraki randevumuzda giyeceğin kıyafeti tarif et.',
  'Anı defterimize bugün yeni bir anı ekle.',
  'Bana sadece 3 kelimeyle bir aşk hikâyesi yaz.',
  'Ortak yapılacaklar listemize birlikte yapacağımız sürpriz bir görev ekle.',
  'Bana bir “seni seviyorum” mesajını 3 farklı dilde yaz.',
  'İzlenecekler listemize birlikte izlemek istediğin bir film ekle ve nedenini söyle.',
  'Bana bugün yaptığın en güzel şeyi anlat, sonra bana bir soru sor.',
  'Bana minik bir tekerleme ya da kafiyeli bir mısra yaz.',
  'Bizim için bir çift sloganı icat et.',
  'Bana ilk tanıştığımız günü benim gözümden anlat.',
  'Şu an bulunduğun yeri bana 3 cümlede romantik bir sahne gibi anlat.',
  'Bana “neden harikasın” başlıklı mini bir haber yaz.',
  'Ortak çalma listemize eklenecek 3 şarkı öner.',
  'Bana bir sonraki buluşmamızda yapacağımız komik bir şey öner.',
  'Benim için bir motivasyon cümlesi yaz; zor günlerde okuyacağım.',
  'Bana sevdiğin bir anımızı sadece 5 emojiyle anlat, ben tahmin edeyim.',
  'Bana çocukluğundan sevdiğin bir oyunu öğret (yazarak).',
  'Bana bugün için küçük, tatlı bir görev ver.',
];

export const MAX_ROUNDS = 10;

export function pickPrompt(kind, used) {
  const list = kind === 'truth' ? TRUTHS : DARES;
  const usedSet = new Set(toArray(used));
  const free = list.map((_, i) => i).filter((i) => !usedSet.has(i));
  const pool = free.length ? free : list.map((_, i) => i);
  return pool[randomInt(pool.length)];
}

export default {
  create({ players, host, prev }) {
    const starter = prev ? otherOf(players, prev.starter) : host;
    return {
      turn: starter, starter, phase: 'choose', kind: '', promptIdx: -1, answer: '', round: 1, maxRounds: MAX_ROUNDS,
      stats: { [players[0]]: 0, [players[1]]: 0 }, skips: { [players[0]]: 0, [players[1]]: 0 },
      usedT: toArray(prev?.usedT).slice(-30), usedD: toArray(prev?.usedD).slice(-30), history: [],
    };
  },

  mount(el, api) {
    const root = h('div', { class: 'td' });
    add(el, root);
    const players = () => Object.keys(api.session.players);

    const choose = (kind) => api.act((s, st) => {
      if (st.turn !== api.me || st.phase !== 'choose') return undefined;
      const used = kind === 'truth' ? st.usedT : st.usedD;
      st.kind = kind; st.promptIdx = pickPrompt(kind, used); st.phase = 'task'; st.answer = '';
      if (kind === 'truth') st.usedT = [...toArray(st.usedT), st.promptIdx]; else st.usedD = [...toArray(st.usedD), st.promptIdx];
      return s;
    });

    const resolve = (done, answer = '') => api.act((s, st) => {
      if (st.turn !== api.me || st.phase !== 'task') return undefined;
      const prompt = (st.kind === 'truth' ? TRUTHS : DARES)[st.promptIdx];
      if (done) st.stats[api.me] = (st.stats[api.me] || 0) + 1; else st.skips[api.me] = (st.skips[api.me] || 0) + 1;
      st.history = [...toArray(st.history), { uid: api.me, kind: st.kind, prompt, answer, done }].slice(-20);
      st.round += 1;
      st.turn = otherOf(players(), api.me);
      st.phase = 'choose'; st.kind = ''; st.promptIdx = -1; st.answer = '';
      if (st.round > st.maxRounds) { s.status = 'finished'; s.result = { winner: winnerByScore(st.stats, players()) }; }
      return s;
    });

    return {
      update(s) {
        const st = s.state;
        clear(root);
        add(root, h('div', { class: 'round-info' }, `Tur ${Math.min(st.round, st.maxRounds)}/${st.maxRounds}`,
          h('span', { class: 'pill' }, `${api.name(api.me)} ✅${st.stats[api.me] || 0}  ·  ${api.name(api.partner)} ✅${st.stats[api.partner] || 0}`)));
        add(root, turnBanner(api, st.turn, 'Sıra sende! Seç bakalım…', `${api.name(st.turn)} seçiyor…`));
        if (st.phase === 'choose') {
          if (st.turn === api.me) add(root, h('div', { class: 'td-choices' },
            h('button', { class: 'td-choice td-choice--truth', type: 'button', onclick: () => choose('truth') }, h('span', {}, '💬'), 'Doğruluk'),
            h('button', { class: 'td-choice td-choice--dare', type: 'button', onclick: () => choose('dare') }, h('span', {}, '🔥'), 'Cesaret')));
          else add(root, h('p', { class: 'muted center' }, `${api.name(st.turn)} doğruluk mu cesaret mi seçecek?`));
        } else {
          const prompt = (st.kind === 'truth' ? TRUTHS : DARES)[st.promptIdx];
          add(root, h('div', { class: `card question-card td-card td-card--${st.kind} pop-in` },
            h('small', {}, st.kind === 'truth' ? '💬 DOĞRULUK' : '🔥 CESARET'), h('h3', { class: 'question-card__text' }, prompt)));
          if (st.turn === api.me) {
            const dkey = `td-${s.round}-${st.round}`;
            const ta = draft(dkey, h('textarea', { class: 'input', rows: '3', maxlength: '500', placeholder: st.kind === 'truth' ? 'Cevabını yaz (isteğe bağlı)…' : 'Ne yaptın? (isteğe bağlı)' }));
            add(root, h('form', { class: 'form', onsubmit: (e) => { e.preventDefault(); const v = validateText(ta.value, { min: 0, max: 500 }); clearDraft(dkey); resolve(true, v.ok ? v.value : ''); } }, ta,
              h('div', { class: 'row row--center' }, h('button', { class: 'btn btn--primary', type: 'submit' }, '✅ Tamamladım'),
                h('button', { class: 'btn btn--ghost', type: 'button', onclick: () => resolve(false) }, '⏭️ Geç'))));
          } else add(root, h('p', { class: 'muted center' }, `${api.name(st.turn)} görevini yapıyor… 👀`));
        }
        const hist = toArray(st.history).slice(-4).reverse();
        if (hist.length) add(root, h('div', { class: 'td-history' }, h('h4', {}, 'Son turlar'),
          hist.map((x) => h('div', { class: 'td-history__item' },
            h('small', {}, `${api.name(x.uid)} · ${x.kind === 'truth' ? 'Doğruluk' : 'Cesaret'} · ${x.done ? '✅' : '⏭️'}`),
            h('p', {}, x.prompt), x.answer ? h('p', { class: 'td-history__answer' }, `“${x.answer}”`) : null))));
      },
    };
  },

  summary(s, api) {
    const st = s.state;
    return h('div', {}, resultTitle(api, s.result?.winner),
      h('p', {}, `Tamamlanan görevler — ${api.name(api.me)}: ${st.stats[api.me] || 0}, ${api.name(api.partner)}: ${st.stats[api.partner] || 0}`),
      h('p', { class: 'muted' }, `Geçilen: ${api.name(api.me)} ${st.skips?.[api.me] || 0} · ${api.name(api.partner)} ${st.skips?.[api.partner] || 0}`));
  },
};
