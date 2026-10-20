// Ekipmansız hareket kütüphanesi. Yalnızca vücut ağırlığı ve zemin; sandalye/bar gerekmez.
// type: 'reps' (tekrar) | 'time' (saniye). base: hangi maksimum test değerinden türetildiği.

export const GROUPS = {
  warmup: 'Isınma',
  push: 'Üst vücut',
  core: 'Karın ve gövde',
  legs: 'Bacak',
  cardio: 'Kondisyon',
  run: 'Koşu',
  stretch: 'Esneme'
};

export const EXERCISES = {
  // --- Isınma ---
  jumpingJack: {
    name: 'Jumping jack', group: 'warmup', type: 'time',
    muscles: 'Tüm vücut, kalp atışını yükseltir',
    cues: ['Kollar başın üstünde birleşsin, ayaklar omuz genişliğinden geniş açılsın.', 'Parmak uçlarına yumuşak bas, dizler hafif bükük.', 'Ritmi sabit tut, nefesi tutma.'],
    mistakes: ['Topukla sert inmek', 'Kolları yarım kaldırmak'],
    easier: 'Zıplamadan yana adım + kol açma', harder: 'Daha hızlı tempo'
  },
  armCircles: {
    name: 'Kol çevirme', group: 'warmup', type: 'time',
    muscles: 'Omuz eklemi',
    cues: ['Kollar yana açık, önce küçük sonra büyük daireler.', 'Yarı süre öne, yarı süre geriye çevir.'],
    mistakes: ['Omuzları kulağa kaldırmak'],
    easier: 'Tek kol', harder: 'Daha geniş daireler'
  },
  hipOpener: {
    name: 'Kalça açma (ayakta diz çevirme)', group: 'warmup', type: 'time',
    muscles: 'Kalça eklemi, kasık',
    cues: ['Dizi beline kaldır, dışarı doğru daire çiz.', 'Her bacakla sırayla, gövde dik.'],
    mistakes: ['Gövdeyi yana yatırmak'],
    easier: 'Duvara tutunarak', harder: 'Daha yavaş ve geniş'
  },
  inchworm: {
    name: 'Inchworm (ellerle yürüme)', group: 'warmup', type: 'time',
    muscles: 'Arka bacak, omuz, karın',
    cues: ['Ayakta öne eğil, ellerle şınav pozisyonuna yürü.', 'Geri yürü ve doğrul; dizleri gerekirse bük.'],
    mistakes: ['Belin çökmesi'],
    easier: 'Dizler bükük', harder: 'Şınav pozisyonunda 1 şınav ekle'
  },
  highKnees: {
    name: 'Yerinde diz çekme', group: 'warmup', type: 'time',
    muscles: 'Kalça bükücüler, kondisyon',
    cues: ['Dizleri bel hizasına çek, kollar koşar gibi.', 'Ayak ucunda kal.'],
    mistakes: ['Geriye yaslanmak'],
    easier: 'Yürüyerek diz çekme', harder: 'Daha hızlı'
  },

  // --- Üst vücut ---
  pushup: {
    name: 'Şınav', group: 'push', type: 'reps', base: 'pushups',
    muscles: 'Göğüs, ön omuz, arka kol, karın',
    cues: ['Eller omuz genişliğinde, parmaklar öne.', 'Baş-kalça-topuk tek çizgi; kalçayı sık.', 'Göğüs yere bir yumruk kalana kadar in, dirsekler gövdeyle ~45°.', 'Tam kilitleyerek it; sınavda yarım şınav sayılmaz.'],
    mistakes: ['Belin çökmesi', 'Yarım inmek', 'Dirsekleri yana açmak', 'Başı öne uzatmak'],
    easier: 'Dizler yerde şınav', harder: 'Yavaş iniş (3 sn) şınav'
  },
  wideP: {
    name: 'Geniş şınav', group: 'push', type: 'reps', base: 'pushups', ratio: 0.8,
    muscles: 'Göğüs (dış), ön omuz',
    cues: ['Eller omuzdan bir karış geniş.', 'Gövde dimdik, göğsü yere yaklaştır.'],
    mistakes: ['Omuzları kulağa kaldırmak'],
    easier: 'Dizler yerde', harder: 'Üstte 1 sn bekle'
  },
  diamondP: {
    name: 'Elmas şınav', group: 'push', type: 'reps', base: 'pushups', ratio: 0.55,
    muscles: 'Arka kol, iç göğüs',
    cues: ['Başparmak ve işaret parmakları göğsün altında elmas yapsın.', 'Dirsekler gövdeye yakın geriye.', 'Gövde tek çizgi.'],
    mistakes: ['Dirsekleri dışarı açmak', 'Kalçayı yukarı kaldırmak'],
    easier: 'Dizler yerde elmas', harder: 'Yavaş iniş'
  },
  pikeP: {
    name: 'Pike şınav', group: 'push', type: 'reps', base: 'pushups', ratio: 0.45,
    muscles: 'Omuz, arka kol',
    cues: ['Kalça yukarıda ters V pozisyonu.', 'Başın tepesi ellerin arasına doğru insin.', 'Dirsekler geriye doğru bükülsün.'],
    mistakes: ['Kalçanın düşüp normal şınava dönmesi'],
    easier: 'Daha az derin', harder: 'Ayakları yakınlaştır'
  },
  archerP: {
    name: 'Okçu şınav', group: 'push', type: 'reps', base: 'pushups', ratio: 0.3,
    muscles: 'Tek taraflı göğüs ve arka kol',
    cues: ['Eller çok geniş; bir kola doğru in, diğer kol düz kalsın.', 'Her tekrar yön değiştir.'],
    mistakes: ['Gövdeyi bükmek'],
    easier: 'Geniş şınav', harder: 'Düz kolu yerden hafif kaldır'
  },
  explosiveP: {
    name: 'Patlayıcı şınav', group: 'push', type: 'reps', base: 'pushups', ratio: 0.35,
    muscles: 'Göğüs, arka kol – hız ve güç',
    cues: ['Kontrollü in, ellerin yerden kesilecek kadar hızlı it.', 'Yumuşak iniş, dirsekler hafif bükük.'],
    mistakes: ['Sert iniş', 'Belin çökmesi'],
    easier: 'Hızlı şınav (eller yerde)', harder: 'Havada el çırp'
  },
  plankShoulder: {
    name: 'Plankta omuz dokunma', group: 'push', type: 'time',
    muscles: 'Omuz dengesi, karın',
    cues: ['Şınav pozisyonu, ayaklar biraz açık.', 'Sırayla elini karşı omzuna değdir; kalça sallanmasın.'],
    mistakes: ['Kalçayı sağa sola sallamak'],
    easier: 'Dizler yerde', harder: 'Ayaklar bitişik'
  },

  // --- Karın ---
  situp: {
    name: 'Mekik', group: 'core', type: 'reps', base: 'situps',
    muscles: 'Karın, kalça bükücüler',
    cues: ['Dizler bükük, ayak tabanları yerde.', 'Eller göğüste çapraz ya da şakakta; boynu çekme.', 'Dirsekler dizlere değene kadar kalk, kürek kemikleri yere değene kadar in.'],
    mistakes: ['Elle başı çekmek', 'Yere tam inmemek', 'Belden fırlatmak'],
    easier: 'Yarım mekik (crunch)', harder: 'Yavaş iniş (3 sn)'
  },
  plank: {
    name: 'Plank', group: 'core', type: 'time', base: 'plank',
    muscles: 'Karın, bel, omuz',
    cues: ['Dirsekler omuzun altında.', 'Kalçayı ve karnı sık; vücut düz bir tahta.', 'Nefes almaya devam et.'],
    mistakes: ['Kalçanın düşmesi ya da çok yükselmesi', 'Nefes tutmak'],
    easier: 'Dizler yerde plank', harder: 'Tek ayak kaldırarak'
  },
  sidePlank: {
    name: 'Yan plank', group: 'core', type: 'time', base: 'plank', ratio: 0.5,
    muscles: 'Yan karın, kalça',
    cues: ['Dirsek omzun altında, vücut yan düz çizgi.', 'Sürenin yarısı sağ, yarısı sol.'],
    mistakes: ['Kalçanın sarkması'],
    easier: 'Alt diz yerde', harder: 'Üst bacağı kaldır'
  },
  legRaise: {
    name: 'Bacak kaldırma', group: 'core', type: 'reps', base: 'situps', ratio: 0.5,
    muscles: 'Alt karın',
    cues: ['Sırt üstü, eller kalça altında.', 'Düz bacakları 90°\'ye kaldır, yere değmeden indir.', 'Bel yere yapışık kalsın.'],
    mistakes: ['Belin boşluk yapması', 'Bacakları düşürmek'],
    easier: 'Dizler bükük', harder: 'Yavaş iniş'
  },
  bicycle: {
    name: 'Bisiklet mekik', group: 'core', type: 'time',
    muscles: 'Yan karın',
    cues: ['Dirseği karşı dize götür, diğer bacak uzansın.', 'Acele etme, döndürme hareketini hisset.'],
    mistakes: ['Boynu çekmek'],
    easier: 'Yavaş tempo', harder: 'Her tekrarda 1 sn bekle'
  },
  hollowHold: {
    name: 'Hollow hold (kayık)', group: 'core', type: 'time', base: 'plank', ratio: 0.4,
    muscles: 'Tüm karın',
    cues: ['Sırt üstü, bel yere bastırılı.', 'Kollar ve bacaklar uzanık, yerden 20–30 cm yukarıda.'],
    mistakes: ['Belin kalkması'],
    easier: 'Dizler bükük', harder: 'Kollar başın üstünde'
  },
  superman: {
    name: 'Superman', group: 'core', type: 'time',
    muscles: 'Bel, sırt, kalça',
    cues: ['Yüzüstü, kollar önde uzun.', 'Kol ve bacakları aynı anda kaldır, 2 sn tut, indir.'],
    mistakes: ['Boynu geriye kırmak'],
    easier: 'Karşı kol ve bacak sırayla', harder: 'Üstte 5 sn tut'
  },

  // --- Bacak ---
  squat: {
    name: 'Squat (çömel-kalk)', group: 'legs', type: 'reps', base: 'squats',
    muscles: 'Ön bacak, kalça',
    cues: ['Ayaklar omuz genişliği, parmaklar hafif dışarı.', 'Kalçayı geriye it, uyluklar yere paralel olana kadar in.', 'Dizler ayak uçlarıyla aynı yöne baksın, topuklar yerde.'],
    mistakes: ['Dizlerin içe kapanması', 'Topuk kaldırmak', 'Sırtı yuvarlamak'],
    easier: 'Yarım squat', harder: 'Altta 2 sn bekle'
  },
  lunge: {
    name: 'Lunge (öne hamle)', group: 'legs', type: 'reps', base: 'squats', ratio: 0.5,
    muscles: 'Ön bacak, kalça, denge',
    cues: ['Öne büyük adım, arka diz yere yaklaşsın.', 'Ön diz ayak bileğinin üstünde.', 'Bacak başına sayı; toplamı yaz.'],
    mistakes: ['Ön dizin ayak ucunu çok geçmesi', 'Gövdeyi öne eğmek'],
    easier: 'Geriye hamle', harder: 'Zıplamalı lunge'
  },
  jumpSquat: {
    name: 'Zıplamalı squat', group: 'legs', type: 'reps', base: 'squats', ratio: 0.4,
    muscles: 'Bacak gücü – koşu ve sprint',
    cues: ['Squat\'a in, patlayarak zıpla.', 'Yumuşak iniş, doğrudan sonraki tekrara geç.'],
    mistakes: ['Dizi kilitleyerek sert iniş'],
    easier: 'Squat + parmak ucuna kalk', harder: 'Daha yükseğe zıpla'
  },
  wallSit: {
    name: 'Duvarda oturma', group: 'legs', type: 'time', base: 'plank', ratio: 0.8,
    muscles: 'Ön bacak dayanıklılığı',
    cues: ['Sırtın duvarda, dizler 90°.', 'Eller dizlere bastırmasın.'],
    mistakes: ['Dizlerin 90°\'den yukarıda kalması'],
    easier: 'Daha yüksek pozisyon', harder: 'Tek bacak kaldır'
  },
  calfRaise: {
    name: 'Parmak ucuna kalkma', group: 'legs', type: 'reps', base: 'squats', ratio: 0.8,
    muscles: 'Baldır – koşu için önemli',
    cues: ['Topukları olabildiğince yükselt, yavaş indir.', 'Denge için duvara dokunabilirsin.'],
    mistakes: ['Zıplar gibi hızlı yapmak'],
    easier: 'İki ayak', harder: 'Tek ayak'
  },
  glueBridge: {
    name: 'Kalça köprüsü', group: 'legs', type: 'reps', base: 'squats', ratio: 0.7,
    muscles: 'Kalça, arka bacak',
    cues: ['Sırt üstü, dizler bükük.', 'Kalçayı sıkarak kaldır, omuz-kalça-diz düz çizgi.', 'Üstte 1 sn sık.'],
    mistakes: ['Belden kaldırmak'],
    easier: 'Kısa hareket', harder: 'Tek bacak köprü'
  },

  // --- Kondisyon ---
  burpee: {
    name: 'Burpee', group: 'cardio', type: 'time',
    muscles: 'Tüm vücut, kondisyon',
    cues: ['Çömel, ellerini koy, ayakları geri at.', 'Şınav pozisyonu (isteğe bağlı şınav), ayakları getir, zıpla.', 'Temiz form > hız.'],
    mistakes: ['Belin çökmesi', 'Yarım zıplamak'],
    easier: 'Zıplamadan, adım adım', harder: 'Şınavlı burpee'
  },
  mountainClimber: {
    name: 'Dağcı (mountain climber)', group: 'cardio', type: 'time',
    muscles: 'Karın, omuz, kondisyon',
    cues: ['Şınav pozisyonu, dizleri sırayla göğse çek.', 'Kalça omuz hizasında, hızlı ama kontrollü.'],
    mistakes: ['Kalçayı havaya kaldırmak'],
    easier: 'Yavaş tempo', harder: 'Çapraz diz (dirseğe)'
  },
  skaterJump: {
    name: 'Patenci sıçrayışı', group: 'cardio', type: 'time',
    muscles: 'Bacak, denge, çeviklik',
    cues: ['Yana sıçra, tek ayakla in, diğer ayak çaprazda.', 'Kollar dengeyi sağlasın.'],
    mistakes: ['Sert iniş'],
    easier: 'Yana adım', harder: 'Daha geniş sıçrayış'
  },
  sprintPlace: {
    name: 'Yerinde sprint', group: 'cardio', type: 'time',
    muscles: 'Hız, kondisyon',
    cues: ['Ayak ucunda olabildiğince hızlı koş.', 'Kollar dirsekten 90° bükük, güçlü salla.'],
    mistakes: ['Topuğa basmak'],
    easier: 'Yerinde tempolu koşu', harder: 'Diz çekerek sprint'
  },
  bearCrawl: {
    name: 'Ayı yürüyüşü', group: 'cardio', type: 'time',
    muscles: 'Omuz, karın, koordinasyon (askerî parkur hazırlığı)',
    cues: ['Eller ve ayak uçları yerde, dizler yerden 5 cm.', 'Çapraz el-ayak ile öne ve geri hareket et.'],
    mistakes: ['Kalçayı kaldırmak'],
    easier: 'Yerinde dizleri kaldırıp tutmak', harder: 'Daha uzun mesafe'
  },

  // --- Koşu (aralık zamanlayıcı) ---
  runEasy: {
    name: 'Rahat koşu', group: 'run', type: 'time',
    muscles: 'Aerobik taban',
    cues: ['Konuşabileceğin hızda koş.', 'Kısa adım, ayak gövdenin altına basmalı.', 'Omuzlar gevşek, nefes düzenli.'],
    mistakes: ['Başta çok hızlı çıkmak'],
    easier: 'Koşu-yürüyüş', harder: 'Son 5 dakikayı hızlandır'
  },
  runFast: {
    name: 'Hızlı koşu', group: 'run', type: 'time',
    muscles: 'Hız, laktat eşiği',
    cues: ['Zor ama sürdürülebilir hız; ~8/10 efor.', 'Kolları güçlü salla, dik dur.'],
    mistakes: ['İlk tekrarda tükenmek – hepsini eşit hızda koş'],
    easier: 'Biraz yavaş tempo', harder: 'Son tekrarda tam gaz'
  },
  runWalk: {
    name: 'Yürü / hafif jog', group: 'run', type: 'time',
    muscles: 'Toparlanma',
    cues: ['Nefesini düzenle, durma; yürümeye devam et.'],
    mistakes: ['Tamamen durup oturmak'],
    easier: 'Yürüyüş', harder: 'Hafif jog'
  },
  runTempo: {
    name: 'Tempolu koşu', group: 'run', type: 'time',
    muscles: 'Dayanıklılık – sınav koşusu temposu',
    cues: ['Rahat koşudan belirgin hızlı, ~7/10 efor.', 'Cümle kurmak zor, kelime söyleyebiliyorsun.'],
    mistakes: ['Sprint yapmak'],
    easier: 'Süreyi böl', harder: 'Son 2 dk hızlan'
  },

  // --- Esneme ---
  stretchHam: {
    name: 'Arka bacak esnetme', group: 'stretch', type: 'time',
    muscles: 'Arka bacak',
    cues: ['Ayakta ya da otururken öne eğil, sırt düz.', 'Yarı süre bir bacak, yarı süre diğeri.'],
    mistakes: ['Yaylanmak'], easier: 'Dizler hafif bükük', harder: 'Daha derin'
  },
  stretchQuad: {
    name: 'Ön bacak esnetme', group: 'stretch', type: 'time',
    muscles: 'Ön bacak',
    cues: ['Ayakta topuğu kalçaya çek, dizler yan yana.', 'Yarı süre bir bacak, yarı süre diğeri.'],
    mistakes: ['Belini boşluk yapmak'], easier: 'Duvara tutun', harder: 'Kalçayı öne it'
  },
  stretchChest: {
    name: 'Göğüs ve omuz esnetme', group: 'stretch', type: 'time',
    muscles: 'Göğüs, ön omuz',
    cues: ['Eller arkada kenetli, göğsü aç, kolları hafif kaldır.'],
    mistakes: ['Omuzları kaldırmak'], easier: 'Duvarda tek kol', harder: 'Daha yukarı'
  },
  childPose: {
    name: 'Çocuk pozu', group: 'stretch', type: 'time',
    muscles: 'Bel, sırt',
    cues: ['Dizler yerde, kalça topuklara, kollar önde uzun.', 'Derin nefes al-ver.'],
    mistakes: [], easier: 'Dizleri aç', harder: 'Kolları daha ileri uzat'
  },
  calfStretch: {
    name: 'Baldır esnetme', group: 'stretch', type: 'time',
    muscles: 'Baldır, aşil',
    cues: ['Duvara dayan, arka bacak düz, topuk yerde.', 'Yarı süre bir bacak, yarı süre diğeri.'],
    mistakes: ['Topuğu kaldırmak'], easier: 'Kısa adım', harder: 'Arka dizi hafif bük'
  }
};

export const RANKS = [
  { xp: 0, name: 'Acemi er' },
  { xp: 300, name: 'Er' },
  { xp: 900, name: 'Onbaşı' },
  { xp: 2000, name: 'Çavuş' },
  { xp: 3800, name: 'Uzman çavuş' },
  { xp: 6500, name: 'Kıdemli uzman çavuş' },
  { xp: 10000, name: 'Başçavuş' },
  { xp: 15000, name: 'Astsubay' }
];

export const BADGES = [
  { key: 'first', name: 'İlk adım', desc: 'İlk antrenmanı bitir' },
  { key: 'week', name: 'Tam hafta', desc: 'Bir haftanın bütün antrenmanlarını yap' },
  { key: 'streak3', name: 'Disiplin', desc: '3 hafta üst üste planı tamamla' },
  { key: 'push50', name: 'Elli şınav', desc: 'Testte 50 şınav' },
  { key: 'sit60', name: 'Çelik karın', desc: 'Testte 60 mekik' },
  { key: 'plank3', name: 'Kaya', desc: '3 dakika plank' },
  { key: 'run30', name: 'Uzun yol', desc: 'Tek seferde 30 dakika koşu' },
  { key: 'ten', name: 'On antrenman', desc: '10 antrenman tamamla' },
  { key: 'fifty', name: 'Elli antrenman', desc: '50 antrenman tamamla' },
  { key: 'cycle', name: 'Dönem bitti', desc: '8 haftalık dönemi tamamla' }
];
