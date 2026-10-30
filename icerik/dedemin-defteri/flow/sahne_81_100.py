# -*- coding: utf-8 -*-
from ortak import EP, S

# ------------------------------------------------------------------ B81 İZMİR (2)
EP(81, {
    "elifdede": ("ELİF'İN DEDESİ", "ELİF'S GRANDFATHER, an 84-year-old Turkish man, white hair, thick glasses, cardigan, holding an old cassette player", "elderly male voice, warm Aegean accent"),
    "camci": ("NAZARKÖY CAM USTASI", "GLASS BEAD MAKER, a 58-year-old Turkish man, heat-reddened face, leather apron, holding molten blue glass on a rod in front of a furnace", "male voice"),
}, {
    "A": ("Elif'in ailesinin evi, sabah", "a cozy family home in İzmir in the morning, an old cassette player on the table"),
    "B": ("Efes Antik Kenti", "the ancient city of Ephesus with the Library of Celsus facade"),
    "C": ("Nazarköy cam atölyesi", "a glass workshop in Nazarköy with a glowing furnace and strings of blue evil-eye beads"),
}, [
    S("Kasette dedenin sesi.", "A", ["kerem", "elif", "~riza"],
      "Kerem presses play on the cassette; static, then a voice; Kerem's eyes fill.",
      [("riza", "Kerem... bir gün birine kızarsan, önce onun yükünü taşı.")], kam="close-up on spinning cassette, then Kerem"),
    S("Efes'te Celsus Kütüphanesi.", "B", ["kerem", "elif"],
      "They stand before the Library of Celsus.",
      [("elif", "Antik dünyanın en büyük kütüphanelerinden."), ("kerem", "Dedemin defteri de küçük bir kütüphane.")]),
    S("Nazarköy'de cam fırınında çalışır.", "C", ["kerem", "camci"],
      "Kerem helps hold a rod with molten glass; the master shapes a blue bead.",
      [("camci", "Nazar boncuğu ateşte doğar."), ("kerem", "Usta, burası cehennem gibi sıcak!")]),
    S("Yevmiye alır.", "C", ["kerem", "camci"],
      "The master pays Kerem.",
      [("camci", "Al bakalım, alnının terini."), ("kerem", "Sağ olun.")], k="s"),
    S("Nazar boncuğu alır.", "C", ["kerem", "camci"],
      "Kerem pays for strings of evil-eye beads.",
      [("kerem", "Aydın'a nazar boncuğu. Biraz da kendime.")], k="a"),
    S("Kasetin son saniyesi: 'Cevdet'e kızma.'", "A", ["kerem", "~riza"],
      "Night; Kerem plays the last seconds of the tape alone.",
      [("riza", "Cevdet'e kızma. O gece onun yerinde olsam ben de aynısını yapardım.")], kam="slow push-in on Kerem"),
])

# ------------------------------------------------------------------ B82 AYDIN
EP(82, {
    "aydinli": ("AYDINLI ESNAF", "AYDIN SHOPKEEPER, a 50-year-old Turkish man, straw hat, linen shirt", "male voice"),
    "incirci": ("İNCİR ÜRETİCİSİ", "FIG FARMER, a 55-year-old Turkish woman, wide-brim hat, laying figs to dry", "female voice"),
}, {
    "A": ("Aydın çarşısı", "a market in Aydın"),
    "B": ("Afrodisias Antik Kenti", "the ancient city of Aphrodisias with marble statues and the Tetrapylon gate"),
    "C": ("İncir bahçesi", "a fig orchard with figs drying on trays"),
}, [
    S("Nazar boncuklarını satar.", "A", ["kerem", "aydinli"],
      "The shopkeeper pays.",
      [("aydinli", "Nazarköy işi, turistler bayılır."), ("kerem", "Nazardan korur!")], k="s"),
    S("Afrodisias'ın heykeltıraş okulu.", "B", ["kerem", "elif"],
      "They walk among marble statues.",
      [("elif", "Antik çağın heykeltıraş okulu buradaymış."), ("kerem", "Mermere can vermişler.")]),
    S("Kerem Cevdet'e kızgınlığını sorgular.", "B", ["kerem", "elif"],
      "Kerem sits on marble steps.",
      [("kerem", "Dedem 'kızma' diyor. Ama Selim dedemi hırsız ilan etti."), ("elif", "Belki o da bilmiyor.")]),
    S("Aydın incirinin kuruması.", "C", ["kerem", "incirci"],
      "The farmer shows figs drying.",
      [("incirci", "Aydın inciri coğrafi işaretli, dünyaya gider."), ("kerem", "Bal gibi!")]),
    S("Kuru incir alır.", "C", ["kerem", "incirci"],
      "Kerem pays.",
      [("kerem", "Muğla'ya incir.")], k="a"),
    S("Leyla: 'Duruşma öne alındı, 20 gün. Selim defterin teslimini istiyor.'", "C", ["kerem", "~leyla"],
      "Kerem answers a call in the orchard.",
      [("leyla", "Mahkeme duruşmayı öne aldı. 20 gün kaldı. Ve Selim defterin mahkemeye teslimini istiyor.")], kam="slow push-in"),
])

# ------------------------------------------------------------------ B83 MUĞLA
EP(83, {
    "muglali": ("MUĞLALI ESNAF", "MUĞLA SHOPKEEPER, a 48-year-old Turkish woman, sunhat, linen dress", "female voice"),
    "mandalinaci": ("MANDALİNA ÜRETİCİSİ", "MANDARIN FARMER, a 60-year-old Turkish man, cap, rolled-up sleeves, basket of mandarins", "male voice"),
}, {
    "A": ("Muğla evleri", "the white-washed traditional houses of Muğla with tall chimneys"),
    "B": ("Bodrum Kalesi", "Bodrum Castle by the turquoise sea with white sailboats"),
    "C": ("Kaunos kaya mezarları", "the Lycian rock tombs of Kaunos carved into a cliff above the Dalyan river"),
    "D": ("Mandalina bahçesi", "a mandarin orchard in Bodrum"),
}, [
    S("İncirleri satar.", "A", ["kerem", "muglali"],
      "The shopkeeper pays.",
      [("muglali", "Aydın inciri, Muğla kahvaltısına."), ("kerem", "Ege'nin şekeri!")], k="s"),
    S("Bodrum Kalesi ve Halikarnas.", "B", ["kerem", "elif"],
      "They walk along the harbor with the castle behind.",
      [("elif", "Halikarnas Mozolesi dünyanın yedi harikasından biriydi."), ("kerem", "Şimdi taşları kalede.")]),
    S("Kaunos kaya mezarları.", "C", ["kerem"],
      "Kerem looks up at the rock tombs from a boat.",
      [("kerem", "Kayaya oyulmuş tapınak mezarlar. Burada caretta caretta da yaşıyor.")]),
    S("Bodrum mandalinası.", "D", ["kerem", "mandalinaci"],
      "The farmer peels a mandarin.",
      [("mandalinaci", "Bodrum mandalinası küçük ama kokusu büyük."), ("kerem", "Bütün bahçe kokuyor!")]),
    S("Mandalina alır.", "D", ["kerem", "mandalinaci"],
      "Kerem pays.",
      [("kerem", "Denizli'ye mandalina.")], k="a"),
    S("Yaşar mesaj atar: 'Mahkemeden önce Sivas'a, Cevdet'in yanına git.'", "A", ["kerem"],
      "Kerem reads a message at night.",
      [("kerem", "Yaşar: 'Sivas'a git, ben de orada olacağım.'")], kurgu="Mesaj: 'Mahkemeden önce Sivas'a, Cevdet'in yanına git. Ben de orada olacağım. — Yaşar'"),
])

# ------------------------------------------------------------------ B84 DENİZLİ
EP(84, {
    "denizlili": ("DENİZLİLİ ESNAF", "DENİZLİ SHOPKEEPER, a 52-year-old Turkish man, glasses, cardigan", "male voice"),
    "dokumaci2": ("BULDAN DOKUMACISI", "BULDAN WEAVER, a 58-year-old Turkish woman, white scarf, at a wooden loom weaving white cotton cloth", "female voice"),
}, {
    "A": ("Denizli çarşısı", "a market in Denizli with a rooster statue"),
    "B": ("Pamukkale travertenleri", "the white travertine terraces of Pamukkale with blue pools, Hierapolis ruins above"),
    "C": ("Buldan dokuma atölyesi", "a weaving workshop in Buldan, white cotton cloth on looms"),
}, [
    S("Mandalinaları satar.", "A", ["kerem", "denizlili"],
      "The shopkeeper pays.",
      [("denizlili", "Bodrum mandalinası, kışın ilacı."), ("kerem", "Kokusundan belli!")], k="s"),
    S("Pamukkale ve Hierapolis.", "B", ["kerem", "elif"],
      "They walk barefoot on the white terraces.",
      [("elif", "Pamuk gibi beyaz, ama taş."), ("kerem", "Doğanın kalesi.")]),
    S("Denizli horozunun hikâyesi.", "A", ["kerem"],
      "Kerem stands by the rooster statue.",
      [("kerem", "Denizli horozu uzun öter. Ben de uzun yoldayım.")]),
    S("Buldan bezi dokunur.", "C", ["kerem", "dokumaci2"],
      "The weaver works the loom.",
      [("dokumaci2", "Buldan bezi tertemiz pamuk."), ("kerem", "İki ipliği birbirine bağlıyorsunuz...")]),
    S("Buldan bezi alır.", "C", ["kerem", "dokumaci2"],
      "Kerem pays.",
      [("kerem", "Burdur'a Buldan bezi.")], k="a"),
    S("Kerem karar değiştirir: 'Davayı kazanmak istemiyorum. Bitirmek istiyorum.'", "C", ["kerem", "elif"],
      "Kerem ties two threads together on the loom, then looks at Elif.",
      [("kerem", "Davayı kazanmak istemiyorum. Bitirmek istiyorum.")], kam="close-up on joined threads, then Kerem"),
])

# ------------------------------------------------------------------ B85 BURDUR
EP(85, {
    "burdurlu": ("BURDURLU ESNAF", "BURDUR SHOPKEEPER, a 50-year-old Turkish woman, scarf, cardigan", "female voice"),
    "cevizci": ("CEVİZ EZMECİSİ", "WALNUT PASTE MAKER, a 55-year-old Turkish man, apron, rolling walnut paste", "male voice"),
}, {
    "A": ("Burdur çarşısı", "a market in Burdur"),
    "B": ("Salda Gölü", "Lake Salda with white sandy shores and turquoise water"),
    "C": ("Sagalassos", "the ancient city of Sagalassos high in the mountains, the Antonine fountain"),
    "D": ("Ceviz ezmesi atölyesi", "a workshop making Burdur walnut paste"),
}, [
    S("Buldan bezini satar.", "A", ["kerem", "burdurlu"],
      "The shopkeeper pays.",
      [("burdurlu", "Buldan bezi, havlu gibi."), ("kerem", "Pamuk yumuşaklığında!")], k="s"),
    S("Salda Gölü'nün beyaz kıyıları.", "B", ["kerem", "elif"],
      "They walk on the white shore.",
      [("elif", "Bilim insanları Salda'yı Mars'a benzetiyor."), ("kerem", "Mars'a da mal satarız!")]),
    S("Sagalassos.", "C", ["kerem"],
      "Kerem stands at the ancient fountain.",
      [("kerem", "Dağın tepesinde bir şehir. Ticaret yolları buradan geçmiş.")]),
    S("Ceviz ezmesi.", "D", ["kerem", "cevizci"],
      "The maker rolls walnut paste.",
      [("cevizci", "Burdur ceviz ezmesi: ceviz, şeker, sabır."), ("kerem", "Sabır her tarifte var!")]),
    S("Ceviz ezmesi alır.", "D", ["kerem", "cevizci"],
      "Kerem pays.",
      [("kerem", "Antalya'ya ceviz ezmesi.")], k="a"),
    S("Necmi son kez çıkar, yalnız ve yorgun.", "A", ["kerem", "necmi"],
      "Necmi sits on a bench, tired, without his gold chain.",
      [("necmi", "Selim beni kovdu. Sana bir şey söylemem lazım.")], kam="slow push-in on Necmi"),
])

# ------------------------------------------------------------------ B86 ANTALYA (1)
EP(86, {
    "antalyali": ("ANTALYALI ESNAF", "ANTALYA SHOPKEEPER, a 45-year-old Turkish man, linen shirt, sunglasses", "male voice"),
}, {
    "A": ("Kaleiçi sokakları", "the narrow old streets of Kaleiçi in Antalya with Ottoman houses and bougainvillea"),
    "B": ("Hadrian Kapısı", "Hadrian's Gate in Antalya, Roman triple arch"),
    "C": ("Kaleiçi limanı, akşam", "the old harbor of Kaleiçi at sunset"),
}, [
    S("Ceviz ezmesini satar.", "A", ["kerem", "antalyali"],
      "The shopkeeper pays.",
      [("antalyali", "Burdur ezmesi turistlerin gözdesi."), ("kerem", "Hediyelik niyetine!")], k="s"),
    S("Hadrian Kapısı'nda Necmi'yi dinler.", "B", ["kerem", "necmi"],
      "Kerem and Necmi walk under the Roman arch.",
      [("necmi", "Selim defteri almak değil, yok etmek istiyordu."), ("kerem", "Neden?")]),
    S("Necmi: 'Babası ona sayfayı asla açtırmamasını söylemiş.'", "B", ["kerem", "necmi"],
      "Necmi stops and looks at Kerem seriously.",
      [("necmi", "Babası ona 'O sayfa asla açılmasın' demiş."), ("kerem", "Çünkü gerçek orada.")]),
    S("Kaleiçi'nde Elif ile düşünür.", "A", ["kerem", "elif"],
      "Kerem and Elif sit on stone steps.",
      [("elif", "Necmi'ye güvenebilir miyiz?"), ("kerem", "Dedem 'Güveni kıran da onarabilir' dedi.")]),
    S("Deftere yazar.", "C", ["kerem"],
      "Kerem writes at the harbor.",
      [("kerem", "Antalya dersi: Düşmanın da bir hikâyesi var. Bugün alım yok.")]),
    S("Necmi: 'Cevdet Bey ölmeden önce gerçeği söylemek istiyor.'", "C", ["kerem", "necmi"],
      "At sunset Necmi speaks quietly.",
      [("necmi", "Cevdet Bey ölmeden önce oğluna gerçeği söylemek istiyor ama Selim dinlemiyor. Sen dinletebilirsin.")], kam="slow push-in"),
])

# ------------------------------------------------------------------ B87 ANTALYA (2)
EP(87, {
    "sahneci": ("SAHNE AMİRİ", "STAGE MANAGER, a 40-year-old Turkish woman, black t-shirt, headset, clipboard", "female voice, fast"),
    "muzcu": ("ALANYA MUZ ÜRETİCİSİ", "BANANA FARMER, a 52-year-old Turkish man, cap, carrying a banana bunch", "male voice"),
}, {
    "A": ("Aspendos Antik Tiyatrosu", "the 2000-year-old Aspendos Roman theater lit for an evening concert"),
    "B": ("Piyazcı", "a restaurant serving Antalya piyaz"),
    "C": ("Alanya muz serası", "a banana greenhouse in Alanya"),
    "D": ("Kapalı yol, fırtına", "a closed mountain road in a storm, rain, traffic stopped"),
}, [
    S("Aspendos'ta konser sahne arkasında çalışır.", "A", ["kerem", "sahneci"],
      "Kerem carries equipment backstage in the ancient theater.",
      [("sahneci", "Kabloyu oraya, hızlı!"), ("kerem", "İki bin yıllık sahnede kablo taşıyorum!")]),
    S("Yevmiye alır.", "A", ["kerem", "sahneci"],
      "The stage manager pays Kerem.",
      [("sahneci", "Iyi iş çıkardın."), ("kerem", "Akustik efsane!")], k="s"),
    S("Necmi ekibe katılmak ister.", "B", ["kerem", "necmi", "elif"],
      "They eat piyaz; Necmi asks humbly.",
      [("necmi", "Size katılabilir miyim? Yol bilirim."), ("kerem", "Kural basit: yalan yok.")]),
    S("Alanya muzu.", "C", ["kerem", "muzcu"],
      "The farmer cuts a banana bunch.",
      [("muzcu", "Alanya muzu küçük ama tatlı."), ("kerem", "Isparta'ya muz!")]),
    S("Muz alır.", "C", ["kerem", "muzcu"],
      "Kerem pays.",
      [("kerem", "Muz çabuk olgunlaşır, hızlı gitmeliyim.")], k="a"),
    S("Fırtına çıkar, Isparta yolu kapanır.", "D", ["kerem", "necmi"],
      "The bus stops in a storm; Kerem looks at the banana boxes.",
      [("kerem", "Yol kapandı... Muzlar sararıyor!"), ("necmi", "Bu sefer suç bende değil!")], kam="rain on the window"),
])

# ------------------------------------------------------------------ B88 ISPARTA
EP(88, {
    "ispartali": ("ISPARTALI ESNAF", "ISPARTA SHOPKEEPER, a 50-year-old Turkish man, cardigan", "male voice"),
    "gulcu": ("GÜL TOPLAYICI", "ROSE PICKER, a 48-year-old Turkish woman, scarf, basket full of pink roses", "female voice"),
}, {
    "A": ("Isparta çarşısı", "a market in Isparta"),
    "B": ("Gül bahçesi, şafak", "a pink rose field at dawn with dew, pickers with baskets"),
    "C": ("Eğirdir Gölü", "Lake Eğirdir with a peninsula and old houses"),
    "D": ("Gül yağı imalathanesi", "a rose oil distillery with copper stills"),
}, [
    S("Muzların bir kısmı fazla olgunlaşmış; kalanını satar. Zarar.", "A", ["kerem", "ispartali"],
      "The shopkeeper picks out ripe bananas.",
      [("ispartali", "Kararmışları alamam, sağlamları alırım."), ("kerem", "Fırtınaya kızamam, zarar yazıldı.")], k="s"),
    S("Şafakta gül hasadı.", "B", ["kerem", "gulcu"],
      "Pickers gather roses at dawn; Kerem joins.",
      [("gulcu", "Güneş çiyi almadan toplanır."), ("kerem", "Sabahın beşinde bile güzel kokuyor!")]),
    S("Eğirdir Gölü.", "C", ["kerem", "elif"],
      "They walk by the lake.",
      [("elif", "Eğirdir, Türkiye'nin büyük göllerinden."), ("kerem", "Göller bölgesi bitiyor, final yaklaşıyor.")]),
    S("Gül yağı damıtılır.", "D", ["kerem", "gulcu"],
      "Rose oil drips from a copper still.",
      [("gulcu", "Bir damla gül yağı için binlerce gül."), ("kerem", "Damla damla emek!")]),
    S("Gül yağı ve gül suyu alır.", "D", ["kerem", "gulcu"],
      "Kerem pays for bottles.",
      [("kerem", "Afyon'a gül kokusu.")], k="a"),
    S("Hüseyin Usta: 'Sivas'a geldiğinde ben de orada olacağım. Yüzüğü getir.'", "C", ["kerem", "~husey"],
      "Kerem answers a call by the lake.",
      [("husey", "Kerem, hastaneden çıktım. Sivas'ta ben de olacağım. Yüzüğü getir.")], kam="slow push-in"),
])

# ------------------------------------------------------------------ B89 AFYONKARAHİSAR
EP(89, {
    "afyonlu": ("AFYONLU ESNAF", "AFYON SHOPKEEPER, a 52-year-old Turkish woman, scarf, apron", "female voice"),
    "sucukcu": ("AFYON SUCUKÇUSU", "SUCUK MAKER, a 56-year-old Turkish man, white coat, hanging sucuk", "male voice"),
}, {
    "A": ("Afyon çarşısı", "a market in Afyonkarahisar with the castle on a rock above"),
    "B": ("Kocatepe", "the Kocatepe memorial hill, Turkish flags"),
    "C": ("Frig Vadisi", "the Phrygian Valley with rock-cut monuments"),
    "D": ("Ankara otobüsü", "inside an intercity bus to Ankara at night"),
}, [
    S("Gül ürünlerini satar.", "A", ["kerem", "afyonlu"],
      "The shopkeeper smells rose water and pays.",
      [("afyonlu", "Isparta gülü, Afyon kaymağına kardeş."), ("kerem", "Kokulu satış!")], k="s"),
    S("Kocatepe'de Büyük Taarruz.", "B", ["kerem", "elif"],
      "They stand at the memorial at dawn.",
      [("elif", "26 Ağustos 1922, Büyük Taarruz buradan başladı."), ("kerem", "Burada her şey değişmiş.")]),
    S("Frig Vadisi.", "C", ["kerem"],
      "Kerem looks at rock-cut monuments.",
      [("kerem", "Frigler kayaya anıt oymuş. Kral Midas'ın memleketi.")]),
    S("Afyon sucuğu.", "A", ["kerem", "sucukcu"],
      "The maker shows sucuk.",
      [("sucukcu", "Afyon sucuğu meşhurdur."), ("kerem", "Kayseri sucuğuyla dostça yarışır!")]),
    S("Afyon sucuğu alır.", "A", ["kerem", "sucukcu"],
      "Kerem pays.",
      [("kerem", "Ankara'ya sucuk.")], k="a"),
    S("Selim'in avukatı arar: 'Defteri teslim etmezseniz tutuklama talep edeceğiz.'", "D", ["kerem"],
      "Kerem on the phone on the night bus, serious.",
      [("kerem", "Tutuklama mı? Defteri hâkimden başkasına vermem.")], kam="close-up", kurgu="Telefondaki ses (avukat): 'Defteri yarın teslim etmezseniz tutuklama talep edeceğiz.'"),
])

# ------------------------------------------------------------------ B90 ANKARA (1)
EP(90, {
    "hakim": ("HÂKİM", "JUDGE, a 55-year-old Turkish woman, black judge's robe with red collar, glasses, grey hair in a bun", "female voice, calm authoritative"),
    "ankarali": ("ANKARALI ESNAF", "ANKARA SHOPKEEPER, a 50-year-old Turkish man, suit vest", "male voice"),
}, {
    "A": ("Anıtkabir", "Anıtkabir mausoleum in Ankara at morning, wide ceremonial square"),
    "B": ("Ankara çarşısı", "a market in Ankara Ulus"),
    "C": ("Mahkeme salonu", "a Turkish courtroom, wooden benches, judge's bench"),
    "D": ("Adliye merdivenleri", "the steps outside the courthouse in Ankara"),
}, [
    S("Sabah Anıtkabir.", "A", ["kerem", "elif"],
      "They walk in the ceremonial square at morning.",
      [("kerem", "Bugün büyük gün. Önce buraya gelmek istedim.")], kam="wide shot"),
    S("Sucukları satar.", "B", ["kerem", "ankarali"],
      "The shopkeeper pays.",
      [("ankarali", "Afyon sucuğu, Ankara'da kapışılır."), ("kerem", "Avukat parası çıktı!")], k="s"),
    S("Mahkemede Selim ile karşı karşıya.", "C", ["kerem", "selim"],
      "Kerem and Selim sit on opposite sides in the courtroom.",
      [("selim", "Defteri getirdin mi?"), ("kerem", "Getirdim. Ama mühür burada açılmayacak.")]),
    S("Elif'in karşılıksız çek delili sunulur.", "C", ["kerem", "elif", "hakim"],
      "Elif hands documents to the judge.",
      [("hakim", "Karşılıksız çek yazışmaları dosyaya alındı."), ("elif", "Hepsi orijinal, Sayın Hâkim.")]),
    S("Hâkim duruşmayı erteler.", "C", ["kerem", "selim", "hakim"],
      "The judge speaks; Selim looks surprised.",
      [("hakim", "Mühürlü sayfa ehil bir kişi huzurunda açılsın. Duruşma ertelenmiştir.")]),
    S("Selim: 'Babam seni görmek istiyor. Sivas'ta. Yalnız gel.'", "D", ["kerem", "selim"],
      "On the courthouse steps Selim stops Kerem.",
      [("selim", "Babam seni görmek istiyor. Sivas'ta. Ama yalnız gel.")], kam="slow push-in"),
])

# ------------------------------------------------------------------ B91 ANKARA (2)
EP(91, {
    "konakci": ("KONAK SAHİBİ", "MANSION CAFÉ OWNER, a 50-year-old Turkish woman, elegant scarf, cardigan", "female voice"),
    "beypazarli": ("BEYPAZARI KURUSUCU", "BEYPAZARI BAKER, a 55-year-old Turkish man, white apron, trays of kurusu biscuits", "male voice"),
}, {
    "A": ("Anadolu Medeniyetleri Müzesi arşivi", "the archive room of the Museum of Anatolian Civilizations in Ankara, files and documents"),
    "B": ("Hamamönü konağı", "a restored Ottoman mansion café in Hamamönü, Ankara"),
    "C": ("Beypazarı fırını", "a bakery in Beypazarı with trays of crunchy kurusu"),
}, [
    S("Leyla 1979 kaza tutanağını arşivden bulur.", "A", ["kerem", "leyla"],
      "Leyla pulls out an old police report.",
      [("leyla", "1979 kaza tutanağı! Rıza hakkında hiçbir suçlama yok."), ("kerem", "Dedem suçsuz!")]),
    S("Tutanağı okurlar.", "A", ["kerem", "leyla"],
      "They read the document together.",
      [("leyla", "Kervan kasası 'kayıp' yazılmış, çalındı değil."), ("kerem", "O zaman parayı kim aldı?")]),
    S("Hamamönü'nde konakta çalışır.", "B", ["kerem", "konakci"],
      "Kerem serves tea in the mansion.",
      [("konakci", "Hamamönü'ne hoş geldiniz!"), ("kerem", "Çaylar geliyor!")]),
    S("Yevmiye alır.", "B", ["kerem", "konakci"],
      "The owner pays.",
      [("konakci", "Al evladım."), ("kerem", "Teşekkürler.")], k="s"),
    S("Beypazarı kurusu alır.", "C", ["kerem", "beypazarli"],
      "Kerem pays for kurusu.",
      [("beypazarli", "Beypazarı kurusu çıtır çıtır."), ("kerem", "Kırıkkale'ye kurusu.")], k="a"),
    S("Tutanağın altında tanık imzası: 'Yaşar Demirci, 15 yaşında, kamyon çırağı.'", "A", ["kerem", "leyla"],
      "Leyla points to a signature at the bottom.",
      [("kerem", "Yaşar Demirci, 15 yaşında, kamyon çırağı... Yaşar Kaptan!")], kam="extreme close-up on signature"),
])

# ------------------------------------------------------------------ B92 KIRIKKALE
EP(92, {
    "kirikkaleli": ("KIRIKKALELİ ESNAF", "KIRIKKALE SHOPKEEPER, a 50-year-old Turkish man, cap, vest", "male voice"),
    "pekmezci": ("PEKMEZ ÜRETİCİSİ", "MOLASSES MAKER, a 58-year-old Turkish woman, scarf, stirring grape molasses in a big cauldron", "female voice"),
}, {
    "A": ("Kırıkkale çarşısı", "a market in Kırıkkale"),
    "B": ("Kızılırmak kıyısı", "the banks of the Kızılırmak river near Kırıkkale at dusk"),
    "C": ("Keskin bağları ve pekmez kazanı", "vineyards in Keskin and a cauldron boiling grape molasses"),
}, [
    S("Beypazarı kurusunu satar.", "A", ["kerem", "kirikkaleli"],
      "The shopkeeper pays.",
      [("kirikkaleli", "Beypazarı kurusu çayın yanına."), ("kerem", "Çıtır kâr!")], k="s"),
    S("Hasandede ve Kızılırmak.", "B", ["kerem"],
      "Kerem walks by the river.",
      [("kerem", "Kızılırmak... Avanos'ta çömleğini gördüğüm nehir. Yol dönüyor.")]),
    S("Keskin bağlarında pekmez.", "C", ["kerem", "pekmezci"],
      "The woman stirs molasses.",
      [("pekmezci", "Üzüm suyunu saatlerce kaynatırız."), ("kerem", "Yine sabır.")]),
    S("Pekmez alır.", "C", ["kerem", "pekmezci"],
      "Kerem pays.",
      [("kerem", "Çankırı'ya pekmez.")], k="a"),
    S("Yaşar'ı bekler.", "B", ["kerem"],
      "Kerem sits by the river looking at the road.",
      [("kerem", "Kaptan gelecek mi?")]),
    S("Yaşar gelir: 'Kırk yedi yıl sustum.'", "B", ["kerem", "yasar"],
      "Yaşar arrives, eyes wet.",
      [("yasar", "Kırk yedi yıl sustum. Sivas'ta Cevdet'in yüzüne karşı konuşacağım.")], kam="slow push-in"),
])

# ------------------------------------------------------------------ B93 ÇANKIRI
EP(93, {
    "cankirili": ("ÇANKIRILI ESNAF", "ÇANKIRI SHOPKEEPER, a 48-year-old Turkish woman, scarf", "female voice"),
    "tuzcu": ("TUZ MAĞARASI GÖREVLİSİ", "SALT CAVE GUIDE, a 45-year-old Turkish man, hard hat, work jacket", "male voice"),
}, {
    "A": ("Çankırı çarşısı", "a market in Çankırı"),
    "B": ("Çankırı Tuz Mağarası", "the Çankırı salt cave, huge glittering white salt walls and tunnels"),
}, [
    S("Pekmezi satar.", "A", ["kerem", "cankirili"],
      "The shopkeeper pays.",
      [("cankirili", "Keskin pekmezi, kış ilacı."), ("kerem", "Şifa olsun!")], k="s"),
    S("Tuz mağarasının Hititlerden beri işletilmesi.", "B", ["kerem", "yasar", "tuzcu"],
      "They walk into glittering salt tunnels.",
      [("tuzcu", "Bu mağara Hititlerden beri işletiliyor."), ("kerem", "Binlerce yıllık maden!")]),
    S("Yaşar sessiz kalır, Kerem sorar.", "B", ["kerem", "yasar"],
      "Kerem and Yaşar stand in the salt cave.",
      [("kerem", "Neden bu kadar sustun kaptan?"), ("yasar", "Rıza'ya söz verdim. Söz tuz gibidir, bozulmaz.")]),
    S("Deftere öğüt.", "B", ["kerem"],
      "Kerem writes.",
      [("kerem", "'Tuz gibi dürüst ol; az olsun, öz olsun.'")]),
    S("Kaya tuzu alır.", "B", ["kerem", "tuzcu"],
      "Kerem pays for rock salt blocks.",
      [("kerem", "Çorum'a kaya tuzu.")], k="a"),
    S("Selim'den fotoğraf: hastanede babasının başında. 'Acele et.'", "A", ["kerem"],
      "Kerem looks at a photo on his phone.",
      [("kerem", "Cevdet hastanede... Acele etmeliyiz.")], kurgu="Fotoğraf: Selim hastanede babasının başında, alt yazı 'Acele et.'"),
])

# ------------------------------------------------------------------ B94 ÇORUM
EP(94, {
    "corumlu": ("ÇORUMLU ESNAF", "ÇORUM SHOPKEEPER, a 50-year-old Turkish man, cap", "male voice"),
    "leblebici": ("LEBLEBİCİ", "LEBLEBI ROASTER, a 60-year-old Turkish man, white apron, roasting chickpeas in a big drum", "male voice"),
}, {
    "A": ("Çorum çarşısı", "a market in Çorum"),
    "B": ("Hattuşa", "the ruins of Hattusa, Hittite capital, the Lion Gate"),
    "C": ("Leblebi kavurma atölyesi", "a leblebi roasting workshop"),
}, [
    S("Kaya tuzunu satar.", "A", ["kerem", "corumlu"],
      "The shopkeeper pays.",
      [("corumlu", "Çankırı tuzu, sofra şifası."), ("kerem", "Tuzu kuru!")], k="s"),
    S("Hattuşa'da Kadeş Antlaşması.", "B", ["kerem", "elif"],
      "They stand at the Lion Gate.",
      [("elif", "Kadeş, bilinen ilk yazılı barış antlaşması."), ("kerem", "Barış da bir ticarettir. İki taraf da kazanır.")]),
    S("Kerem Selim'le barış fikrini düşünür.", "B", ["kerem"],
      "Kerem sits on ancient stones.",
      [("kerem", "Selim'le savaşmak değil, anlaşmak lazım.")]),
    S("Leblebi kavrulur.", "C", ["kerem", "leblebici"],
      "The roaster turns chickpeas.",
      [("leblebici", "Çorum leblebisi üç kez kavrulur."), ("kerem", "Üç kez sabır!")]),
    S("Leblebi alır.", "C", ["kerem", "leblebici"],
      "Kerem pays.",
      [("kerem", "Amasya'ya leblebi.")], k="a"),
    S("Selim: 'Babam taburcu oldu. Divriği'de buluşmak istiyor.'", "A", ["kerem", "~selim"],
      "Kerem answers a call.",
      [("selim", "Babam taburcu oldu, Sivas'a götürüyorum. Seninle Divriği'de buluşmak istiyor.")], kam="slow push-in"),
])

# ------------------------------------------------------------------ B95 AMASYA
EP(95, {
    "amasyali": ("AMASYALI ESNAF", "AMASYA SHOPKEEPER, a 52-year-old Turkish woman, scarf", "female voice"),
    "elmaci2": ("MİSKET ELMASI ÜRETİCİSİ", "APPLE FARMER, a 55-year-old Turkish man, cap, crate of small fragrant apples", "male voice"),
}, {
    "A": ("Yalıboyu evleri", "the Ottoman Yalıboyu houses along the Yeşilırmak river in Amasya with rock tombs above"),
    "B": ("Kral Kaya Mezarları", "the Pontic rock-cut royal tombs on the cliff above Amasya"),
    "C": ("Misket elması bahçesi", "an apple orchard with small misket apples"),
}, [
    S("Leblebiyi satar.", "A", ["kerem", "amasyali"],
      "The shopkeeper pays.",
      [("amasyali", "Çorum leblebisi, çayın yanında."), ("kerem", "Komşu ikramı!")], k="s"),
    S("Kral Kaya Mezarları.", "B", ["kerem", "elif"],
      "They look up at the rock tombs.",
      [("elif", "Pontus kralları kayaya gömülmüş."), ("kerem", "Kayaya söz yazmışlar.")]),
    S("Ferhat ile Şirin efsanesi.", "A", ["kerem", "elif"],
      "They walk by the river.",
      [("elif", "Ferhat, Şirin için dağı delip su getirmiş."), ("kerem", "Ben de dedem için 81 il deldim!")]),
    S("Misket elması.", "C", ["kerem", "elmaci2"],
      "The farmer shows small fragrant apples.",
      [("elmaci2", "Amasya misket elması kokusuyla bilinir."), ("kerem", "Niğde'den başladım, Amasya'yla bitiyor elma serüvenim.")]),
    S("Misket elması alır.", "C", ["kerem", "elmaci2"],
      "Kerem pays.",
      [("kerem", "Tokat'a elma.")], k="a"),
    S("Hüseyin Usta yüzüğü takar: 'Son borç benim borcum.'", "A", ["kerem", "husey"],
      "Hüseyin Usta, back on his feet with a cane, puts the silver ring on his finger by the river.",
      [("husey", "Sivas'tan sonra Kayseri. Ve son borç, Kerem... benim borcum.")], kam="close-up on the ring, then his face"),
])

# ------------------------------------------------------------------ B96 TOKAT
EP(96, {
    "tokatli": ("TOKATLI ESNAF", "TOKAT SHOPKEEPER, a 48-year-old Turkish man, vest", "male voice"),
    "yazmaci": ("YAZMA USTASI", "BLOCK PRINT MASTER, a 62-year-old Turkish man, apron stained with colors, pressing a wooden block onto cloth", "male voice"),
}, {
    "A": ("Tokat çarşısı", "a market in Tokat"),
    "B": ("Gök Medrese", "the Seljuk Gök Madrasa in Tokat with blue tiles"),
    "C": ("Ballıca Mağarası", "Ballıca Cave with colorful formations"),
    "D": ("Yazma atölyesi", "a Tokat block-printing workshop with wooden blocks and colorful printed cloths"),
}, [
    S("Elmaları satar.", "A", ["kerem", "tokatli"],
      "The shopkeeper pays.",
      [("tokatli", "Amasya elması, Tokat'ın tezgâhında."), ("kerem", "Kokusu dükkânı sardı!")], k="s"),
    S("Gök Medrese.", "B", ["kerem", "elif"],
      "They look at blue tiles.",
      [("elif", "Selçuklu çinileri."), ("kerem", "Kütahya'nın mavisinin büyük ablası.")]),
    S("Ballıca Mağarası.", "C", ["kerem"],
      "Kerem walks in the cave.",
      [("kerem", "Ballıca, Türkiye'nin en güzel mağaralarından.")]),
    S("Tokat yazmasının yapılışı.", "D", ["kerem", "yazmaci"],
      "The master presses a wooden block onto cloth.",
      [("yazmaci", "Her renk ayrı kalıpla basılır."), ("kerem", "Her il ayrı bir renk gibi.")]),
    S("Tokat yazması alır.", "D", ["kerem", "yazmaci"],
      "Kerem pays.",
      [("kerem", "Sivas'a yazma.")], k="a"),
    S("Selim arar: 'Babamın durumu kötüleşti. Yarın Divriği'de değilsen...'", "A", ["kerem", "~selim"],
      "Kerem answers a call at night.",
      [("selim", "Babamın durumu kötüleşti. Yarın sabah Divriği'de değilsen belki onu hiç göremezsin.")], kam="slow push-in"),
])

# ------------------------------------------------------------------ B97 SİVAS
EP(97, {
    "sivasli": ("SİVASLI ESNAF", "SİVAS SHOPKEEPER, a 52-year-old Turkish woman, scarf", "female voice"),
    "bicakci": ("BIÇAK USTASI", "KNIFE MAKER, a 58-year-old Turkish man, leather apron, forging a blade", "male voice"),
}, {
    "A": ("Sivas çarşısı", "a market in Sivas"),
    "B": ("Divriği Ulu Camii ve Darüşşifası", "the UNESCO-listed Divriği Great Mosque and Hospital with its extraordinary carved stone portal"),
    "C": ("Sivas Kongresi binası", "the historic Sivas Congress building"),
    "D": ("Bıçak atölyesi", "a Sivas knife-making workshop"),
}, [
    S("Yazmaları satar.", "A", ["kerem", "sivasli"],
      "The shopkeeper pays.",
      [("sivasli", "Tokat yazması, çeyizlik."), ("kerem", "Renk renk!")], k="s"),
    S("Sivas Kongresi binası.", "C", ["kerem", "elif"],
      "They stand at the building.",
      [("elif", "1919 Sivas Kongresi burada toplandı."), ("kerem", "Bir araya gelmek her şeyin başı.")]),
    S("Bıçak ustası.", "D", ["kerem", "bicakci"],
      "The maker forges a blade.",
      [("bicakci", "Sivas bıçağı ateşte sertleşir."), ("kerem", "İnsan da öyle.")]),
    S("Sivas bıçağı alır.", "D", ["kerem", "bicakci"],
      "Kerem pays.",
      [("kerem", "Yozgat'a bıçak.")], k="a"),
    S("Divriği'nin taş kapısında Cevdet Karahan.", "B", ["kerem", "cevdet"],
      "An old man with a cane stands at the carved portal; Kerem approaches slowly.",
      [("cevdet", "Rıza'nın torunu... Gözlerin onun gözleri."), ("kerem", "Cevdet Bey.")]),
    S("Cevdet: 'Rıza beni bırakmadı. Ben onu yarı yolda bıraktım.' Selim kapıda.", "B", ["kerem", "cevdet", "selim"],
      "Cevdet's voice breaks; Selim appears at the portal behind.",
      [("cevdet", "Rıza beni bırakmadı, Kerem. Ben onu yarı yolda bıraktım."), ("selim", "Baba?!")], kam="slow push-in, then cut to Selim"),
])

# ------------------------------------------------------------------ B98 YOZGAT
EP(98, {
    "yozgatli": ("YOZGATLI ESNAF", "YOZGAT SHOPKEEPER, a 50-year-old Turkish man, cap", "male voice"),
    "tarhanaci": ("TARHANACI", "TARHANA MAKER, a 60-year-old Turkish woman, scarf, spreading tarhana to dry", "female voice"),
}, {
    "A": ("Yozgat çarşısı", "a market in Yozgat"),
    "B": ("Yozgat Çamlığı", "Yozgat Çamlık national park, Türkiye's first national park, tall pines"),
    "C": ("1979 geri dönüşü: karlı yol", "a snowy road in February 1979 at night, an old 1970s truck stopped, headlights, warm faded film look"),
    "D": ("Tarhana damı", "a rooftop with tarhana drying"),
}, [
    S("Bıçakları satar.", "A", ["kerem", "yozgatli"],
      "The shopkeeper pays.",
      [("yozgatli", "Sivas bıçağı, mutfağın kralı."), ("kerem", "Keskin kâr!")], k="s"),
    S("Çamlık'ta herkes bir araya gelir.", "B", ["kerem", "yasar", "cevdet", "selim"],
      "Under tall pines, Yaşar faces Cevdet and Selim; Kerem watches.",
      [("yasar", "Kırk yedi yıl önceki geceyi anlatacağım.")]),
    S("1979 geri dönüş: Cevdet kasayı alır.", "C", ["cevdetg", "yasarg"],
      "Flashback: young Cevdet takes a money box from the truck in the snow, crying; a teenage apprentice watches from the cab.",
      [("cevdetg", "Kızım ameliyatta... Başka çarem yok!")], kam="handheld, snow, faded 1970s look"),
    S("1979 geri dönüş: Rıza suçu üstlenir.", "C", ["rizag", "cevdetg", "yasarg"],
      "Young Rıza puts his hand on Cevdet's shoulder; the apprentice listens.",
      [("rizag", "Git, kızını kurtar. Herkese ben aldım derim. Sen de, çırak, sus.")], kam="slow push-in, faded 1970s look"),
    S("Tarhana alır.", "D", ["kerem", "tarhanaci"],
      "Kerem pays for tarhana, still emotional.",
      [("tarhanaci", "Yozgat tarhanası, kış sofrasının çorbası."), ("kerem", "Kırşehir'e tarhana.")], k="a"),
    S("Selim: 'O kız... benim ablam mıydı?' Cevdet başını sallar; Selim gider.", "B", ["kerem", "cevdet", "selim"],
      "Selim turns to his father, voice cracking; Cevdet nods; Selim walks away to his car.",
      [("selim", "O kız... benim ablam mıydı?"), ("cevdet", "Evet oğlum.")], kam="slow push-in on Selim, then wide as he leaves"),
])

# ------------------------------------------------------------------ B99 KIRŞEHİR
EP(99, {
    "kirsehirli": ("KIRŞEHİRLİ ESNAF", "KIRŞEHİR SHOPKEEPER, a 50-year-old Turkish man, flat cap", "male voice"),
    "mucurlu": ("MUCURLU DOKUMACI", "MUCUR WEAVER, a 60-year-old Turkish woman, scarf, at a carpet loom", "female voice"),
    "bozlakci": ("BOZLAK ÇALGICISI", "STEPPE FOLK MUSICIAN, a 50-year-old Turkish man, black vest, playing a bağlama", "music"),
}, {
    "A": ("Kırşehir çarşısı", "a market in Kırşehir"),
    "B": ("Ahi Evran Türbesi", "the Ahi Evran tomb and mosque in Kırşehir"),
    "C": ("Mucur dokuma evi", "a weaving house in Mucur with handwoven carpets"),
    "D": ("Bozkır, akşam", "the Central Anatolian steppe at sunset"),
}, [
    S("Tarhanayı satar.", "A", ["kerem", "kirsehirli"],
      "The shopkeeper pays.",
      [("kirsehirli", "Yozgat tarhanası, kışın şifası."), ("kerem", "Son satışlardan biri!")], k="s"),
    S("Ahi Evran Türbesi'nde Hüseyin Usta ile buluşur.", "B", ["kerem", "husey"],
      "Kerem and Hüseyin Usta stand at the tomb.",
      [("husey", "Ahiliğin piri Ahi Evran. Yolun başladığı yer."), ("kerem", "Ve bitmeye yakın olduğu yer.")]),
    S("Neşet Ertaş'ın bozkır türküleri.", "D", ["kerem", "husey", "bozlakci"],
      "A musician plays a steppe song at sunset.",
      [("kerem", "Neşet Ertaş... Bozkırın tezenesi.")], kam="wide sunset shot"),
    S("Mucur el dokuması halı alır.", "C", ["kerem", "mucurlu"],
      "Kerem pays for a carpet.",
      [("mucurlu", "Mucur halısı, ömürlük."), ("kerem", "Bu, Kayseri'ye hediyem.")], k="a"),
    S("Usta: 'Yarın Kayseri'de 82. adım.'", "D", ["kerem", "husey"],
      "Hüseyin Usta puts a hand on Kerem's shoulder at sunset.",
      [("husey", "Yarın Kayseri'de 82. adım.")]),
    S("Selim: 'Ben çarşıdayım. Dükkânın önünde.'", "D", ["kerem", "~selim"],
      "Kerem's phone rings.",
      [("selim", "Ben çarşıdayım. Dükkânın önünde.")], kam="slow push-in"),
])

# ------------------------------------------------------------------ B100 KAYSERİ FİNAL
EP(100, {
    "carsili": ("KAPALI ÇARŞI ESNAFI", "BAZAAR SHOPKEEPER, a 55-year-old Turkish man, vest, smiling", "male voice"),
}, {
    "A": ("Kayseri Kapalı Çarşı", "inside the historic Kayseri Covered Bazaar, vaulted stone corridor, crowd gathering"),
    "B": ("Dükkânın önü", "the front of the old Aksoy-Karahan shop in the Kayseri Covered Bazaar, warm light, everyone gathered"),
    "C": ("Dükkân içi, açılış", "the shop transformed into '81 İl Yol Hanı', shelves full of products from all 81 provinces, Mount Erciyes visible through the door at dusk"),
}, [
    S("Mucur halısını Kapalı Çarşı'da satar.", "A", ["kerem", "carsili"],
      "Kerem sells the carpet to a shopkeeper as the crowd watches.",
      [("carsili", "Rıza'nın torunu döndü!"), ("kerem", "Döndüm amca. Son satış!")], k="s"),
    S("82. adım: Kerem 5.000 ₺'yi Hüseyin Usta'ya iade eder.", "B", ["kerem", "husey", "ayse", "elif", "leyla", "nazli", "yasar"],
      "Kerem hands an envelope to Hüseyin Usta in front of everyone; the old man's eyes fill.",
      [("kerem", "Beş bin lira, usta. Sermayeniz."), ("husey", "81. borç kapandı. 82. adım atıldı.")]),
    S("Hüseyin yüzüğüyle mührü kırar; Kerem iki anahtar yarısıyla kilidi açar.", "B", ["kerem", "husey", "selim", "cevdet"],
      "Hüseyin Usta presses the ring into the red wax and breaks it; Kerem joins the two silver key halves and opens the lock.",
      [("husey", "Bismillah."), ("kerem", "Açıldı!")], kam="extreme close-up on wax breaking and key turning"),
    S("Sayfada 1978 senedi: dükkân yarı yarıya Aksoy & Karahan adına.", "B", ["kerem", "selim", "cevdet", "leyla"],
      "Leyla reads the page aloud; Selim and Cevdet listen, stunned.",
      [("leyla", "1978 ortaklık senedi. Dükkân yarı yarıya: Aksoy ve Karahan."), ("cevdet", "Rıza... yarısını bize saklamış.")]),
    S("Kerem Selim'e elini uzatır; dükkân '81 İl Yol Hanı' olur.", "C", ["kerem", "selim", "elif", "nazli", "yasar", "necmi", "husey"],
      "Kerem holds out his hand; Selim shakes it; everyone cheers in the shop full of products from 81 provinces.",
      [("kerem", "Ortak mıyız?"), ("selim", "Ortağız.")], kurgu="Kurguda tabela: '81 İl Yol Hanı'"),
    S("Sayfanın arkasında yeni harita: İpek Yolu, Semerkant. 2. sezon.", "C", ["kerem", "husey", "~riza"],
      "Kerem turns the page; on the back is an old map of the Silk Road; the grandfather's voice is heard.",
      [("riza", "Kerem... Sırada İpek Yolu var. Sermayen: kasandaki her şey."), ("kerem", "Semerkant mı?!")],
      kam="slow push-in on the map, Erciyes at dusk", kurgu="Harita üzerinde: 'İpek Yolu – Semerkant'. Ekranda: '2. SEZON'"),
])
