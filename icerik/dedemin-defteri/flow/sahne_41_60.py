# -*- coding: utf-8 -*-
from ortak import EP, S

# ------------------------------------------------------------------ B41 ERZURUM (1)
EP(41, {
    "erzurumlu": ("ERZURUMLU ESNAF", "ERZURUM SHOPKEEPER, a 55-year-old Turkish man, thick grey mustache, black wool coat, astrakhan hat", "male voice, Erzurum accent"),
    "cagci": ("CAĞ KEBABI USTASI", "CAĞ KEBAB MASTER, a 50-year-old Turkish man, white chef coat, slicing a horizontal rotating kebab over wood fire", "male voice, proud"),
}, {
    "A": ("Erzurum çarşısı, kar", "a snowy market street in Erzurum, people in heavy coats"),
    "B": ("Çifte Minareli Medrese", "the Seljuk Double Minaret Madrasa in Erzurum with twin fluted brick minarets, snow on the ground"),
    "C": ("Cağ kebabı ocağı", "a cağ kebab restaurant with a horizontal rotating skewer over a wood fire"),
    "D": ("Pansiyon odası, gece", "a warm guesthouse room at night, snow falling outside the window"),
}, [
    S("Tulum peynirini Erzurum çarşısında satar.", "A", ["kerem", "erzurumlu"],
      "In the snow, the shopkeeper tastes the tulum and pays.",
      [("erzurumlu", "Erzincan tulumu! Dadaş sofrası bunsuz olmaz."), ("kerem", "Soğukta da peynir sıcak satıyor!")], k="s"),
    S("Çifte Minareli Medrese'yi gezer.", "B", ["kerem", "elif"],
      "Kerem and Elif look up at the twin minarets in the snow.",
      [("elif", "Selçuklu'dan kalma, sekiz yüz yıllık."), ("kerem", "İki minare, tek kapı. Ortaklık böyle olmalı.")]),
    S("Cağ kebabı ustası 'ateşi eşit yakmak' dersini verir.", "C", ["kerem", "cagci"],
      "The master slices meat from the horizontal skewer onto a small skewer and hands it to Kerem.",
      [("cagci", "Ateşi eşit yakacaksın; bir taraf yanarsa öbürü çiğ kalır."), ("kerem", "Adalet gibi.")]),
    S("Deftere not alır.", "C", ["kerem"],
      "Kerem eats cağ kebab and writes in the notebook.",
      [("kerem", "Erzurum dersi: Herkese eşit ateş. Bugün alım yok, yarın var.")]),
    S("Leyla görüntülü arar; listenin sonunu çözmüştür.", "D", ["kerem", "~leyla"],
      "Kerem answers a video call by the window, snow falling outside.",
      [("leyla", "Kerem, listenin son satırını çözdüm."), ("kerem", "Kim?")]),
    S("'81. isim... Hüseyin Usta.'", "D", ["kerem", "~leyla"],
      "Kerem's face freezes; he slowly sits on the bed.",
      [("leyla", "81. isim... Hüseyin Usta.")], kam="slow push-in, snow outside"),
])

# ------------------------------------------------------------------ B42 ERZURUM (2)
EP(42, {
    "oltucu": ("OLTU TAŞI USTASI", "OLTU STONE CRAFTSMAN, a 60-year-old Turkish man, black jet stone dust on fingers, grey beard, magnifier glasses", "male voice, gentle"),
    "barci": ("BAR EKİBİ", "a group of Erzurum folk dancers in traditional black and red costumes, holding hands in a line", "silent"),
}, {
    "A": ("Kar altında meydan", "a snowy square in Erzurum with folk dancers performing bar dance"),
    "B": ("Oltu taşı atölyesi", "an Oltu stone workshop, black shiny jet stone prayer beads hanging"),
    "C": ("Palandöken eteği, akşam", "a viewpoint at the foot of Palandöken mountain at dusk, ski lights"),
}, [
    S("Hüseyin Usta'yı arar; usta konuşmak istemez.", "C", ["kerem", "~husey"],
      "Kerem calls on the phone at dusk; he looks frustrated.",
      [("kerem", "Usta, listedeki 81. isim siz misiniz?"), ("husey", "Telefonda olmaz evlat.")]),
    S("Bar oyununu izler.", "A", ["kerem", "barci"],
      "Folk dancers perform the bar dance in the snow; Kerem joins the line awkwardly, laughing.",
      [("kerem", "Omuz omuza, adım adım... Ben ters adım attım!")], kam="wide shot, dancers in line"),
    S("Oltu taşı atölyesinde tesbih ipliği takarak çalışır.", "B", ["kerem", "oltucu"],
      "Kerem threads black Oltu stone beads onto a string.",
      [("oltucu", "Oltu taşı ele alındıkça parlar."), ("kerem", "İnsan da öyle galiba.")]),
    S("Yevmiye alır.", "B", ["kerem", "oltucu"],
      "The craftsman pays Kerem.",
      [("oltucu", "Elin yatkın, al hakkını."), ("kerem", "Sağ olun usta.")], k="s"),
    S("Oltu taşı tesbih alır.", "B", ["kerem", "oltucu"],
      "Kerem buys bundles of black prayer beads.",
      [("kerem", "Ağrı'ya Oltu taşı.")], k="a"),
    S("Hüseyin Usta sonunda konuşur: 'Ben de o gece oradaydım.'", "C", ["kerem", "~husey"],
      "Kerem's phone rings again; he answers, listens, and his breath fogs in the cold.",
      [("husey", "Ben de o gece oradaydım, Kerem. Ama yemin ettim.")], kam="slow push-in, city lights below"),
])

# ------------------------------------------------------------------ B43 AĞRI
EP(43, {
    "dogubayazitli": ("DOĞUBAYAZITLI ESNAF", "DOĞUBAYAZIT SHOPKEEPER, a 50-year-old Turkish man, flat cap, long coat", "male voice"),
    "kilimci_a": ("KİLİM DOKUYUCUSU", "WEAVER, a 52-year-old Turkish woman, dark red headscarf, layered skirts, at a vertical loom", "female voice"),
}, {
    "A": ("Doğubayazıt çarşısı", "a market in Doğubayazıt with snowy Mount Ararat towering behind"),
    "B": ("İshak Paşa Sarayı", "the Ishak Pasha Palace on a hillside, Ottoman palace with domes and carved portal, Mount Ararat in the background"),
    "C": ("Lokanta", "a small restaurant serving abdigör köftesi"),
    "D": ("Dokuma evi", "a weaving house with handwoven wool kilims"),
}, [
    S("Oltu tesbihleri satar.", "A", ["kerem", "dogubayazitli"],
      "The shopkeeper rolls the beads in his palm and pays.",
      [("dogubayazitli", "Oltu taşı hakiki, ele yapışıyor."), ("kerem", "Usta işi abi.")], k="s"),
    S("İshak Paşa Sarayı'nı gezer.", "B", ["kerem", "elif"],
      "Kerem and Elif stand at the carved stone portal of the palace, Mount Ararat behind.",
      [("elif", "Bu saray tam bir sınır kalesi gibi."), ("kerem", "Ve arkada Ağrı Dağı. Türkiye'nin en yükseği.")], kam="wide shot of palace and mountain"),
    S("Abdigör köftesi yer.", "C", ["kerem", "elif"],
      "Kerem and Elif eat abdigör köftesi.",
      [("kerem", "Etin dövülmüşü... yumuşacık."), ("elif", "Belgeselin yemek bölümü uzayacak.")]),
    S("Deftere not alır.", "A", ["kerem"],
      "Kerem writes in the notebook with Mount Ararat behind him.",
      [("kerem", "Ağrı dersi: Dağ ne kadar büyükse, eteğindeki insan o kadar sabırlı.")]),
    S("El dokuması kilim alır.", "D", ["kerem", "kilimci_a"],
      "The weaver shows a wool kilim; Kerem pays.",
      [("kilimci_a", "Kış uzun, kilim de uzun dokunur."), ("kerem", "Iğdır'a götürüyorum.")], k="a"),
    S("Yaşar arar: 'Iğdır'da iyi bir teklif gelecek, kabul etme.' Hat kesilir.", "A", ["kerem", "~yasar"],
      "Kerem answers the phone; static and wind; the line cuts off.",
      [("yasar", "Iğdır'da sana çok iyi bir teklif yapacaklar. Sakın kabul..."), ("kerem", "Kaptan? Kaptan!")], kam="close-up, wind blowing"),
])

# ------------------------------------------------------------------ B44 IĞDIR
EP(44, {
    "igdirli": ("IĞDIRLI ESNAF", "IĞDIR SHOPKEEPER, a 46-year-old Turkish woman, brown headscarf, wool cardigan", "female voice"),
    "kayisici_i": ("IĞDIR KAYISI ÜRETİCİSİ", "APRICOT FARMER, a 55-year-old Turkish man, straw hat, blue work jacket", "male voice"),
}, {
    "A": ("Iğdır pazarı", "a market in Iğdır with Mount Ararat on the horizon"),
    "B": ("Aras Kuş Cenneti", "the Aras Bird Paradise wetland, reeds and flocks of birds, Ararat behind"),
    "C": ("Kayısı bahçesi", "an apricot orchard in the Iğdır plain"),
}, [
    S("Kilimleri satar.", "A", ["kerem", "igdirli"],
      "The shopkeeper unrolls a kilim and pays.",
      [("igdirli", "Ağrı'nın kilimi, Iğdır'ın evine."), ("kerem", "Komşu eli, komşu evi.")], k="s"),
    S("Aras Kuş Cenneti'nde kuşları izler.", "B", ["kerem", "elif"],
      "Flocks of birds rise from the reeds; Elif films, Kerem watches through binoculars.",
      [("elif", "Yüzlerce kuş türü burada konaklıyormuş."), ("kerem", "Kuşlar da kervansaray seviyor.")]),
    S("Ağrı Dağı'nın en güzel göründüğü ova.", "B", ["kerem"],
      "Kerem looks at the mountain at golden hour.",
      [("kerem", "Ağrı Dağı'nı en güzel Iğdır'dan görüyorsun.")], kam="wide shot"),
    S("Iğdır kayısısı ile Malatya kayısısının farkını öğrenir.", "C", ["kerem", "kayisici_i"],
      "The farmer hands Kerem a fresh apricot.",
      [("kayisici_i", "Iğdır kayısısı coğrafi işaretlidir, iri ve suludur."), ("kerem", "Malatya'yla kardeş ama huyu farklı.")]),
    S("Iğdır kayısısı alır.", "C", ["kerem", "kayisici_i"],
      "Kerem pays for crates of apricots.",
      [("kerem", "Kars'a kayısı.")], k="a"),
    S("Kars'tan bir toptancı iki katı fiyat teklif eder, ödeme çekle.", "A", ["kerem"],
      "Kerem listens to a phone call, eyes widening at the offer, Elif looks suspicious.",
      [("kerem", "Bütün kayısıya iki katı mı? Ödeme çekle, yarın Kars'ta... Olur!")], kam="close-up on Kerem, Elif shaking her head behind"),
])

# ------------------------------------------------------------------ B45 KARS
EP(45, {
    "karsli_toptanci": ("SAHTE TOPTANCI", "FAKE WHOLESALER, a 45-year-old Turkish man, expensive coat, slick hair, briefcase", "male voice, smooth"),
    "gravyerci": ("GRAVYER USTASI", "GRUYERE CHEESE MAKER, a 58-year-old Turkish man, white coat, hairnet, large cheese wheels", "male voice"),
    "bankaci": ("BANKA GİŞE GÖREVLİSİ", "BANK TELLER, a 30-year-old Turkish woman, navy blazer, neat bun", "female voice, polite"),
}, {
    "A": ("Kars depo önü", "a warehouse yard in Kars, snow, a truck"),
    "B": ("Ani Harabeleri", "the ruins of Ani, medieval stone churches on a windswept plateau"),
    "C": ("Kars Baltık binaları", "Baltic-style stone buildings in Kars city center"),
    "D": ("Gravyer mandırası", "a Kars gruyere dairy with big cheese wheels on wooden shelves"),
    "E": ("Banka gişesi", "a bank branch counter in Kars"),
}, [
    S("Kayısıları çek karşılığı toptancıya verir; kasaya nakit girmez.", "A", ["kerem", "karsli_toptanci"],
      "A smooth man in an expensive coat hands Kerem a cheque while workers load apricots into his truck.",
      [("karsli_toptanci", "Çek sağlam, üç gün sonra tahsil edersin."), ("kerem", "Kasaya şimdilik sıfır giriyor ama olsun.")], k="s",
      kurgu="Kasa değişmez: satış 0 ₺ (çek)"),
    S("Ani Harabeleri'ni gezer.", "B", ["kerem", "elif"],
      "Kerem and Elif walk among medieval ruins on the windy plateau.",
      [("elif", "Ani'ye bin bir kilise şehri derlermiş."), ("kerem", "İpek Yolu'nun büyük şehriymiş.")], kam="wide drone shot"),
    S("Kars'ın Baltık mimarisi binaları.", "C", ["kerem"],
      "Kerem walks past stone Baltic-style buildings.",
      [("kerem", "Kars'ta sokaklar Avrupa gibi, sofra Anadolu gibi.")]),
    S("Gravyer yapımını öğrenir.", "D", ["kerem", "gravyerci"],
      "The cheese maker taps a giant wheel of gruyere.",
      [("gravyerci", "Kars gravyeri en az altı ay bekler."), ("kerem", "Bu tekerlek benden ağır!")]),
    S("Kasadaki nakitle Kars gravyeri alır.", "D", ["kerem", "gravyerci"],
      "Kerem pays and gets wedges of gruyere.",
      [("kerem", "Çekin parası gelince kasa dolacak zaten.")], k="a"),
    S("Banka: 'Çek karşılıksız. Keşideci: Karahan Gıda.'", "E", ["kerem", "bankaci"],
      "The teller hands the cheque back across the counter apologetically.",
      [("bankaci", "Çek karşılıksız beyefendi. Keşideci firma: Karahan Gıda."), ("kerem", "Karahan...")], kam="close-up on the cheque, then Kerem's face"),
])

# ------------------------------------------------------------------ B46 ARDAHAN
EP(46, {
    "ardahanli": ("ARDAHANLI ESNAF", "ARDAHAN SHOPKEEPER, a 50-year-old Turkish man, fur hat, thick coat", "male voice"),
    "balikci": ("BUZ BALIKÇISI", "ICE FISHERMAN, a 55-year-old Turkish man, fur hat, heavy coat, fishing net over an ice hole", "male voice"),
    "kazci": ("KAZ ÜRETİCİSİ", "GOOSE FARMER, a 60-year-old Turkish woman, wool headscarf, long coat, near hanging dried geese", "female voice"),
}, {
    "A": ("Ardahan çarşısı", "a small snowy market in Ardahan"),
    "B": ("Çıldır Gölü, buz", "the frozen Lake Çıldır, horse-drawn sleighs on the ice, fishermen at ice holes"),
    "C": ("Kaz kurutma evi", "a village house with dried geese hanging in a cold room"),
}, [
    S("Çek zararını kabullenir; gravyeri satar.", "A", ["kerem", "ardahanli"],
      "Kerem sells gruyere to the shopkeeper, looking tired.",
      [("ardahanli", "Kars gravyeri burada da sevilir."), ("kerem", "Kayısının parası yandı, gravyer kurtarsın.")], k="s"),
    S("Çıldır Gölü'nde atlı kızak.", "B", ["kerem", "elif"],
      "Kerem and Elif ride a horse-drawn sleigh across the frozen lake, laughing.",
      [("elif", "Göl donmuş, atlar üstünde koşuyor!"), ("kerem", "Kasa donmuş, ben üstünde koşuyorum!")], kam="tracking shot alongside the sleigh"),
    S("Buz balıkçılarına yardım edip yevmiye alır.", "B", ["kerem", "balikci"],
      "Kerem pulls a net from an ice hole with the fisherman, fish flapping.",
      [("balikci", "Aferin delikanlı, al hakkını."), ("kerem", "Ellerim dondu ama kasa ısındı.")]),
    S("Deftere öğüdü yazar.", "B", ["kerem"],
      "Kerem writes in the notebook on the ice.",
      [("kerem", "Dedem yazmış: 'Çek kâğıttır, para değildir. Parayı görmeden mal verme.'")]),
    S("Ardahan kazı alır.", "C", ["kerem", "kazci"],
      "The woman shows dried geese; Kerem pays.",
      [("kazci", "Kaz kış boyu soğukta kurur."), ("kerem", "Artvin'e kaz götürüyorum.")], k="a"),
    S("Yaşar: 'Cevdet Sivas'ta yaşıyor. Önce anahtarın öbür yarısını bul: Trabzon'da.'", "A", ["kerem", "yasar"],
      "Yaşar arrives in his bus, steps down in the snow and speaks quietly.",
      [("yasar", "Cevdet Karahan Sivas'ta yaşıyor. Ama önce anahtarın öbür yarısını bul: Trabzon'da, hasır bilezik ustasında.")], kam="two-shot in snow, bus lights"),
])

# ------------------------------------------------------------------ B47 ARTVİN
EP(47, {
    "artvinli": ("ARTVİNLİ ESNAF", "ARTVIN SHOPKEEPER, a 45-year-old Turkish man, beard, fleece jacket", "male voice"),
    "balci_m": ("MACAHEL ARICISI", "MACAHEL BEEKEEPER, a 65-year-old Turkish man, white beard, beekeeping veil, wooden hive frames", "elderly male voice"),
}, {
    "A": ("Artvin çarşısı", "a mountain town market in Artvin on steep slopes"),
    "B": ("Şavşat Karagöl", "Karagöl lake in Şavşat surrounded by dense pine forest, mist"),
    "C": ("Macahel arı kovanları", "wooden beehives in the lush green Macahel forest, a UNESCO biosphere area"),
}, [
    S("Kurutulmuş kazı satar.", "A", ["kerem", "artvinli"],
      "The shopkeeper inspects the dried goose and pays.",
      [("artvinli", "Ardahan kazı, kış sofrasının kralı."), ("kerem", "Soğukta kurudu, sıcakta satıldı!")], k="s"),
    S("Şavşat Karagöl'de sis.", "B", ["kerem", "elif"],
      "Kerem and Elif walk around the misty lake.",
      [("elif", "Burası masal gibi."), ("kerem", "Masal değil, Artvin.")], kam="slow drone over the misty lake"),
    S("Macahel'in biyosfer alanı ve Kafkas arısı.", "C", ["kerem", "balci_m"],
      "The beekeeper lifts a hive frame full of honey.",
      [("balci_m", "Macahel UNESCO biyosfer alanı. Arısı da saf Kafkas arısı."), ("kerem", "Arılar bile koruma altında!")]),
    S("Deftere not alır.", "C", ["kerem"],
      "Kerem writes among the hives, bees buzzing.",
      [("kerem", "Artvin dersi: Saf olanı korursan, o da seni korur.")]),
    S("Macahel balı alır.", "C", ["kerem", "balci_m"],
      "Kerem pays for jars of honey.",
      [("kerem", "Rize'ye bal götürüyorum.")], k="a"),
    S("Elif dosya gönderir: Selim'in karşılıksız çek mesajları.", "A", ["kerem", "elif"],
      "Elif shows Kerem documents on her laptop; Kerem reads, amazed.",
      [("elif", "Selim'in 'Karahan Gıda' adına çek yazdırdığı mesajlar. Bu senin delilin."), ("kerem", "Elif... sen bunu nasıl buldun?")], kam="close-up on laptop, then their faces"),
])

# ------------------------------------------------------------------ B48 RİZE
EP(48, {
    "rizeli": ("RİZELİ ESNAF", "RIZE SHOPKEEPER, a 50-year-old Turkish woman, colorful Rize scarf, apron", "female voice, Black Sea accent"),
    "cayci": ("ÇAY TOPLAYICI", "TEA PICKER, a 45-year-old Turkish woman, traditional striped feretiko cloth, basket on her back", "female voice, cheerful Black Sea accent"),
}, {
    "A": ("Rize çarşısı", "a market in Rize near the Black Sea, green hills"),
    "B": ("Ayder Yaylası ve Zil Kale", "Ayder plateau with wooden houses in the mist, and the medieval Zil Castle in a green forest"),
    "C": ("Çay bahçesi", "terraced tea gardens on steep green hills in Rize"),
}, [
    S("Macahel balını satar.", "A", ["kerem", "rizeli"],
      "The shopkeeper tastes the honey and pays.",
      [("rizeli", "Macahel balı! Kahvaltıya gider da!"), ("kerem", "Karadeniz ağzı başladı!")], k="s"),
    S("Ayder Yaylası ve Zil Kale.", "B", ["kerem", "elif"],
      "Kerem and Elif walk in the misty plateau.",
      [("elif", "Zil Kale ormanın içinden çıkıyor gibi."), ("kerem", "Burada bulutlar yerde yürüyor.")], kam="wide misty shot"),
    S("Çay toplayan kadınlardan 'iki yaprak bir tomurcuk' kuralını öğrenir.", "C", ["kerem", "cayci"],
      "The tea picker shows how to pluck two leaves and a bud.",
      [("cayci", "İki yaprak bir tomurcuk! Fazlası olmaz."), ("kerem", "Az olsun, öz olsun.")]),
    S("Çay toplamayı dener.", "C", ["kerem", "cayci"],
      "Kerem tries picking, grabbing too much; she laughs and fixes it.",
      [("cayci", "O çay değil, çalı!"), ("kerem", "Pardon abla!")]),
    S("Rize çayı alır.", "C", ["kerem", "cayci"],
      "Kerem pays for packages of Rize tea.",
      [("kerem", "Trabzon'a çay götürüyorum.")], k="a"),
    S("Annesi arar: Hüseyin Usta kalp krizi geçirmiş.", "C", ["kerem", "~ayse"],
      "Kerem answers his phone in the tea garden; he drops the basket.",
      [("ayse", "Kerem, Hüseyin Usta kalp krizi geçirdi, hastanede!")], kam="slow push-in"),
])

# ------------------------------------------------------------------ B49 TRABZON (1)
EP(49, {
    "trabzonlu": ("TRABZONLU ÇAYCI", "TRABZON TEA SHOP OWNER, a 55-year-old Turkish man, black cap, black vest", "male voice, Black Sea accent"),
    "kemenceci": ("KEMENÇECİ", "KEMENÇE PLAYER, a 40-year-old Turkish man in traditional black Black Sea costume, playing a kemençe fiddle", "silent, music"),
}, {
    "A": ("Trabzon çay ocağı", "a tea house in Trabzon"),
    "B": ("Sümela Manastırı", "the Sümela Monastery built into a steep cliff in a misty forest"),
    "C": ("Uzungöl", "Uzungöl lake with wooden houses and a mosque, pine mountains"),
}, [
    S("Hüseyin Usta için endişelenir ama yola devam eder; Rize çayını satar.", "A", ["kerem", "trabzonlu"],
      "The tea house owner pays Kerem a low price.",
      [("trabzonlu", "Uşağum, burası da çay memleketi; fazla veremem."), ("kerem", "Malı ait olduğu yerden uzağa sat... dersi aldım.")], k="s"),
    S("Sümela Manastırı'na tırmanış.", "B", ["kerem", "elif"],
      "Kerem and Elif climb the forest path toward the monastery on the cliff.",
      [("elif", "Kayaya oyulmuş bir manastır!"), ("kerem", "Burada inşaat yapan ustalar korkusuzmuş.")], kam="wide shot of cliff"),
    S("Uzungöl'de kemençe ve horon.", "C", ["kerem", "kemenceci"],
      "A kemençe player plays; Kerem tries the horon dance shaking his shoulders.",
      [("kerem", "Horon omuzdan başlar dediler... omzum kaydı!")], kam="dynamic dance shot"),
    S("Annesini arar, ustanın durumunu sorar.", "C", ["kerem", "~ayse"],
      "Kerem calls home by the lake.",
      [("kerem", "Anne, usta nasıl?"), ("ayse", "İyiye gidiyor oğlum, merak etme.")]),
    S("Deftere not alır.", "C", ["kerem"],
      "Kerem writes by the lake.",
      [("kerem", "Trabzon dersi: Herkesin sattığını satma. Bugün alım yok.")]),
    S("Annesi tekrar arar: ustanın dükkânına girilmiş, mühür yüzüğü çalınmış.", "C", ["kerem", "~ayse"],
      "Kerem's phone rings again at night by the lake; his face drops.",
      [("ayse", "Hüseyin Usta'nın dükkânına girmişler. Mühür yüzüğü çalınmış!")], kam="slow push-in, night lights on lake"),
])

# ------------------------------------------------------------------ B50 TRABZON (2)
EP(50, {
    "hasirci": ("HASIR BİLEZİK USTASI", "HASIR BRACELET MASTER, a 70-year-old Turkish man, white mustache, black vest, jeweler's loupe, weaving fine silver wires", "elderly male voice, Black Sea accent"),
}, {
    "A": ("Hasır bilezik atölyesi", "a small jewelry workshop in Trabzon, fine silver wires being woven into flexible straw-like Trabzon hasır bracelets"),
    "B": ("Akçaabat köftecisi", "a famous Akçaabat meatball restaurant in Trabzon"),
    "C": ("Atölye, gece", "the jewelry workshop at night, a single lamp"),
}, [
    S("Defterin işaret ettiği hasır bilezik ustasını bulur.", "A", ["kerem", "hasirci"],
      "Kerem shows the notebook page to the old master; the master smiles knowingly.",
      [("hasirci", "Rıza'nın torunu... Seni yıllardır bekliyorum."), ("kerem", "Usta, siz de mi tanıyordunuz?")]),
    S("Gümüş tellerle hasır örgüsünü öğrenir, atölyede çalışır.", "A", ["kerem", "hasirci"],
      "The master weaves fine silver wires into a flexible bracelet; Kerem tries with tweezers.",
      [("hasirci", "Yüzlerce tel, tek bilezik."), ("kerem", "Tıpkı 81 il gibi.")]),
    S("Yevmiye alır.", "A", ["kerem", "hasirci"],
      "The master pays Kerem.",
      [("hasirci", "Al bakalım çırak."), ("kerem", "Sağ olun usta.")], k="s"),
    S("Usta anahtarın ikinci yarısını verir.", "C", ["kerem", "hasirci"],
      "The master opens a small box and gives the second half of the ornate silver key; Kerem joins the two halves, they fit perfectly.",
      [("kerem", "Tam oturdu!"), ("hasirci", "Deden iki ustaya böldü ki tek kişi açamasın.")], kam="extreme close-up on the two halves joining"),
    S("Akçaabat köftesi yer; gümüş hasır bilezik alır.", "B", ["kerem", "elif"],
      "Kerem and Elif eat Akçaabat köfte, a box of silver bracelets on the table.",
      [("elif", "Anahtar tamam, sırada yüzük var."), ("kerem", "Önce Bayburt'a gümüş götürelim.")], k="a"),
    S("Usta: 'Geçen hafta Karahan kartvizitli biri anahtarı almak istedi.'", "C", ["kerem", "hasirci"],
      "At night the master locks the workshop and turns to Kerem, worried.",
      [("hasirci", "Geçen hafta biri bu anahtarı almak için kapıma dayandı. Kartvizitinde Karahan yazıyordu.")], kam="slow push-in"),
])

# ------------------------------------------------------------------ B51 BAYBURT
EP(51, {
    "bayburtlu": ("BAYBURTLU KUYUMCU", "BAYBURT JEWELER, a 48-year-old Turkish man, round glasses, grey vest", "male voice"),
    "ozan": ("OZAN", "FOLK BARD, a 60-year-old Turkish man, long grey beard, felt cloak, holding a kopuz lute", "elderly male voice, storyteller"),
    "helvaci": ("TEL HELVACI", "TEL HELVA MAKER, a 52-year-old Turkish man, white apron, pulling thin strands of sugar", "male voice"),
}, {
    "A": ("Bayburt çarşısı", "a market in Bayburt with the castle on the hill"),
    "B": ("Bayburt Kalesi, Dede Korkut Şenliği", "Bayburt Castle on a hill, a folk festival with a storyteller bard and a crowd"),
    "C": ("Helva atölyesi", "a tel helva workshop, thin white sugar threads"),
    "D": ("Pansiyon kapısı, gece", "the door of a small guesthouse at night, a dim street lamp"),
}, [
    S("Gümüş bilezikleri satar.", "A", ["kerem", "bayburtlu"],
      "The jeweler examines a silver hasır bracelet and pays.",
      [("bayburtlu", "Trabzon hasırı, eşsiz işçilik."), ("kerem", "Yüzlerce tel, tek bilezik abi.")], k="s"),
    S("Dede Korkut Şenlikleri'nde ozanı dinler.", "B", ["kerem", "elif", "ozan"],
      "The bard plays a kopuz and tells a story to a crowd.",
      [("ozan", "Dede Korkut der ki: Kul bir işe başlarsa, dosttan kalkar."), ("kerem", "Dedem de bir Dede Korkut'tu, hikâyesini bana bıraktı.")]),
    S("Bayburt Kalesi'nde manzara.", "B", ["kerem", "elif"],
      "They stand on the castle walls at sunset.",
      [("elif", "Bayburt Dede Korkut'un yurdu sayılır."), ("kerem", "Hikâyeler buradan doğmuş.")]),
    S("Tel helvanın yapılışını görür.", "C", ["kerem", "helvaci"],
      "The maker pulls sugar into thousands of thin threads.",
      [("helvaci", "Şekeri binlerce tel yaparsın; kopmadan."), ("kerem", "Sabır yine sabır.")]),
    S("Bayburt tel helvası alır.", "C", ["kerem", "helvaci"],
      "Kerem pays for boxes of tel helva.",
      [("kerem", "Gümüşhane'ye tatlı yolculuk.")], k="a"),
    S("Pansiyon kapısında Necmi, parmağında ustanın yüzüğüyle.", "D", ["kerem", "necmi"],
      "Necmi leans on the guesthouse door, raising his hand to show a large silver signet ring.",
      [("necmi", "Bunu mu arıyorsun?")], kam="close-up on the ring on Necmi's finger"),
])

# ------------------------------------------------------------------ B52 GÜMÜŞHANE
EP(52, {
    "gumushaneli": ("GÜMÜŞHANELİ ESNAF", "GÜMÜŞHANE SHOPKEEPER, a 50-year-old Turkish woman, maroon headscarf, cardigan", "female voice"),
    "pestilci": ("PESTİL USTASI", "PESTIL MAKER, a 60-year-old Turkish woman, white headscarf, spreading mulberry paste on cloths", "female voice"),
}, {
    "A": ("Gümüşhane çarşısı", "a market in Gümüşhane"),
    "B": ("Karaca Mağarası", "Karaca Cave with colorful stalactites and stalagmites, lit with warm lights"),
    "C": ("Santa Harabeleri", "the abandoned stone village of Santa on a misty mountainside"),
    "D": ("Pestil damı", "a rooftop where sheets of mulberry pestil dry on cloths, köme strings hanging"),
}, [
    S("Tel helvayı satar.", "A", ["kerem", "gumushaneli"],
      "The shopkeeper tastes tel helva and pays.",
      [("gumushaneli", "Bayburt helvası çayın yanına."), ("kerem", "Tel tel tatlı!")], k="s"),
    S("Necmi şart koyar: anahtarları getirirse yüzüğü verecek.", "A", ["kerem", "necmi"],
      "Necmi walks beside Kerem in the market, playing with the ring.",
      [("necmi", "İki anahtar yarısını ver, yüzüğü al."), ("kerem", "O yüzük benim değil, ustanın!")]),
    S("Karaca Mağarası'nda Elif'le plan yapar.", "B", ["kerem", "elif"],
      "In the colorful cave, Kerem and Elif whisper a plan.",
      [("elif", "Ona istediğini veriyormuş gibi yapacağız."), ("kerem", "Ama yüzüğü almadan değil.")]),
    S("Santa Harabeleri'nde düşünür.", "C", ["kerem"],
      "Kerem stands in the misty abandoned village.",
      [("kerem", "Terk edilmiş bir köy... Ama taşlar hâlâ evin şeklini hatırlıyor.")]),
    S("Pestil ve köme alır.", "D", ["kerem", "pestilci"],
      "The maker folds sheets of pestil; Kerem pays.",
      [("pestilci", "Dut, ceviz, güneş."), ("kerem", "Giresun'a pestil götürüyorum.")], k="a"),
    S("Necmi: 'Yarın Giresun Adası'nın karşısında. Tek gel.'", "A", ["kerem", "necmi"],
      "Necmi walks away, turning back once.",
      [("necmi", "Yarın Giresun Adası'nın karşısında. Tek gel. Polise gidersen yüzüğü denize atarım.")], kam="medium shot, Necmi walking off"),
])

# ------------------------------------------------------------------ B53 GİRESUN
EP(53, {
    "giresunlu": ("GİRESUNLU ESNAF", "GIRESUN SHOPKEEPER, a 52-year-old Turkish man, black cap, vest", "male voice, Black Sea accent"),
    "findikci": ("FINDIK ÜRETİCİSİ", "HAZELNUT FARMER, a 58-year-old Turkish woman, colorful scarf, sack of hazelnuts", "female voice"),
}, {
    "A": ("Giresun çarşısı", "a market in Giresun"),
    "B": ("Giresun Adası manzarası, sahil", "the Giresun coastline at dusk, Giresun Island visible offshore"),
    "C": ("Fındık bahçesi", "a hazelnut orchard on green hills above the Black Sea"),
}, [
    S("Pestili satar.", "A", ["kerem", "giresunlu"],
      "The shopkeeper tastes pestil and pays.",
      [("giresunlu", "Gümüşhane pestili, çocuklar bayılır."), ("kerem", "Büyükler de.")], k="s"),
    S("Kirazın Kerasus'tan Avrupa'ya gidişini anlatır.", "B", ["kerem", "elif"],
      "Kerem and Elif sit at the coast looking at the island.",
      [("elif", "Kirazın adı Giresun'un eski adı Kerasus'tan geliyor."), ("kerem", "Kiraz da bizim ihracatımızmış!")]),
    S("Elif ve Yaşar ile tuzak kurarlar.", "B", ["kerem", "elif", "yasar"],
      "The three crouch behind a parked bus at dusk.",
      [("yasar", "Ben otobüsle yolu kapatırım."), ("elif", "Ben her şeyi kaydediyorum.")]),
    S("Tuzak işler: yüzük geri alınır.", "B", ["kerem", "necmi", "yasar"],
      "Kerem hands Necmi a fake key; as Necmi checks it, Yaşar's bus blocks his car and Kerem snatches the ring.",
      [("kerem", "Yüzük bende!"), ("necmi", "Bu anahtar sahte!")], kam="fast action, handheld"),
    S("Fındık alır.", "C", ["kerem", "findikci"],
      "Kerem pays for sacks of hazelnuts.",
      [("findikci", "Giresun tombul fındığı, en iyisi."), ("kerem", "Ordu'ya fındık götürüyorum.")], k="a"),
    S("Kaçarken Necmi bağırır: 'Deden Selim'in babasını mahvetti!'", "B", ["kerem", "necmi"],
      "Necmi runs to his car and shouts back before driving away.",
      [("necmi", "Deden Selim'in babasını mahvetti! Sayfayı açınca görürsün!")], kam="slow push-in on Kerem holding the ring"),
])

# ------------------------------------------------------------------ B54 ORDU
EP(54, {
    "ordulu": ("ORDULU TOPTANCI", "ORDU WHOLESALER, a 55-year-old Turkish man, grey suit jacket, shaking his head", "male voice, Black Sea accent"),
    "ezmeci": ("FINDIK EZMESİ USTASI", "HAZELNUT PASTE MAKER, a 45-year-old Turkish woman, apron, jars of hazelnut paste", "female voice"),
}, {
    "A": ("Ordu toptancı deposu", "a hazelnut wholesale warehouse in Ordu, mountains of hazelnut sacks"),
    "B": ("Boztepe teleferik", "a cable car going up to Boztepe hill overlooking Ordu city and the Black Sea"),
    "C": ("Yason Burnu", "Cape Jason with a small historic chapel on the coast"),
    "D": ("Fındık ezmesi atölyesi", "a small hazelnut paste workshop"),
}, [
    S("Fındığı Ordu'ya getirir; fiyatlar düşük. Zarar.", "A", ["kerem", "ordulu"],
      "The wholesaler points to mountains of hazelnut sacks and laughs.",
      [("ordulu", "Ordu'ya fındık mı getirdin? Burası fındık başkenti!"), ("kerem", "Maliyetin altında... Yine zarar.")], k="s"),
    S("Boztepe'ye teleferikle çıkar.", "B", ["kerem", "elif"],
      "Kerem and Elif in a cable car above the city.",
      [("elif", "Bu yüzden 'Ordu'ya fındık satılmaz' derler."), ("kerem", "Ders pahalıya patladı.")], kam="cable car shot over city"),
    S("Yason Burnu'nda düşünür.", "C", ["kerem"],
      "Kerem sits near the small chapel at the cape.",
      [("kerem", "Altın Post efsanesinin geçtiği yer. Ben altın değil, ders arıyorum.")]),
    S("Deftere not alır.", "C", ["kerem"],
      "Kerem writes.",
      [("kerem", "Ordu dersi: Pazarı tanımadan mal getirme.")]),
    S("Fındık ezmesi alır.", "D", ["kerem", "ezmeci"],
      "Kerem pays for jars of hazelnut paste.",
      [("ezmeci", "İşlenmiş fındık başka yerde daha değerli."), ("kerem", "Samsun'a ezme götürüyorum.")], k="a"),
    S("Leyla arar: '14 Şubat 1979, Kayseri–Sivas yolu, bir kaza raporu var.'", "C", ["kerem", "~leyla"],
      "Kerem answers his phone at the cape at sunset.",
      [("leyla", "Yeni bir tarih çözdüm: 14 Şubat 1979. Kayseri–Sivas yolu. Bir kaza raporu var.")], kam="slow push-in"),
])

# ------------------------------------------------------------------ B55 SAMSUN
EP(55, {
    "samsunlu": ("SAMSUNLU ESNAF", "SAMSUN SHOPKEEPER, a 50-year-old Turkish man, flat cap, brown jacket", "male voice"),
    "nokulcu": ("NOKUL USTASI", "NOKUL BAKER, a 55-year-old Turkish woman, white apron, rolling dough with walnut filling", "female voice"),
}, {
    "A": ("Samsun çarşısı", "a market in Samsun"),
    "B": ("Bandırma Vapuru Müzesi", "the replica Bandırma steamship museum on the Samsun coast"),
    "C": ("Amisos Tepesi", "Amisos hill with ancient tumulus graves overlooking Samsun and the sea"),
    "D": ("Bafra fırını", "a bakery in Bafra making nokul pastries"),
}, [
    S("Fındık ezmesini satar.", "A", ["kerem", "samsunlu"],
      "The shopkeeper tastes the paste and pays.",
      [("samsunlu", "Ezmeyi ekmeğe sürersin, çocuklar bayılır."), ("kerem", "Fındık zararını ezme kapattı!")], k="s"),
    S("Bandırma Vapuru Müzesi'nde 19 Mayıs 1919.", "B", ["kerem", "elif"],
      "Kerem and Elif stand on the deck of the replica ship.",
      [("elif", "19 Mayıs 1919, Kurtuluş Savaşı burada başladı."), ("kerem", "Her büyük yol küçük bir vapurla başlar.")]),
    S("Amisos Tepesi'nden manzara.", "C", ["kerem"],
      "Kerem looks over the city and sea from the hill.",
      [("kerem", "Amisos... Samsun'un antik adı.")]),
    S("Nokul yapımını öğrenir.", "D", ["kerem", "nokulcu"],
      "The baker rolls dough with walnut filling.",
      [("nokulcu", "Bafra nokulu cevizle sarılır."), ("kerem", "Rulo yapmakta usta oldum sayılır.")]),
    S("Bafra nokulu alır.", "D", ["kerem", "nokulcu"],
      "Kerem pays for trays of nokul.",
      [("kerem", "Sinop'a nokul.")], k="a"),
    S("Selim'den mesaj: 'Sinop'ta konuşalım. Sadece ikimiz.'", "A", ["kerem"],
      "Kerem reads a message on his phone at night.",
      [("kerem", "Sinop'ta konuşalım... Gerçeği duymak istiyorsan gel.")], kurgu="Mesaj: 'Sinop'ta konuşalım. Sadece ikimiz. — S.K.'"),
])

# ------------------------------------------------------------------ B56 SİNOP
EP(56, {
    "sinoplu": ("SİNOPLU ESNAF", "SINOP SHOPKEEPER, a 48-year-old Turkish woman, sailor-striped shirt, short hair", "female voice"),
    "maketci": ("GEMİ MAKETÇİSİ", "SHIP MODEL MAKER, a 68-year-old Turkish man, white beard, sailor cap, carving a tiny wooden ship", "elderly male voice"),
}, {
    "A": ("Sinop çarşısı", "a market in Sinop by the harbor"),
    "B": ("Sinop Tarihi Cezaevi avlusu", "the courtyard of the historic Sinop Fortress Prison museum, stone walls, cold light"),
    "C": ("Hamsilos koyu", "the fjord-like Hamsilos bay with green cliffs"),
    "D": ("Gemi maketi atölyesi", "a workshop full of detailed wooden ship models"),
}, [
    S("Nokulları satar.", "A", ["kerem", "sinoplu"],
      "The shopkeeper tastes nokul and pays.",
      [("sinoplu", "Bafra'nın nokulu, Sinop'un çayına."), ("kerem", "Karadeniz kahvaltısı tamam!")], k="s"),
    S("Tarihi Cezaevi'nde Selim ile buluşur.", "B", ["kerem", "selim"],
      "Kerem walks into the prison courtyard; Selim waits alone, hands behind his back.",
      [("selim", "Burası doğru yer. Hapsolmak ne demek, iyi bilir."), ("kerem", "Dinliyorum.")]),
    S("Selim'in versiyonu: Rıza kervanın kasasıyla kaçmış.", "B", ["kerem", "selim"],
      "Selim speaks coldly, looking at the stone walls.",
      [("selim", "Babam her şeyini kaybetti. Rıza kasayla kaçtı, biz yoksullukta büyüdük."), ("kerem", "Dedem kaçmadı, borç ödedi!")]),
    S("Hamsilos koyunda düşünür.", "C", ["kerem"],
      "Kerem sits on a cliff above the bay.",
      [("kerem", "Selim de kendi gerçeğine inanıyor... İkimiz de dedelerimizi savunuyoruz.")]),
    S("Gemi maketi alır.", "D", ["kerem", "maketci"],
      "The maker places a tiny wooden ship in a box; Kerem pays.",
      [("maketci", "Sinop'un denizcileri bu gemileri yaparak büyüdü."), ("kerem", "Kastamonu'ya gemi götürüyorum!")], k="a"),
    S("Selim gazete kupürü uzatır: 'Kervan kasası kayıp, ortak ortadan kayboldu.'", "B", ["kerem", "selim"],
      "Selim hands Kerem an old yellowed newspaper clipping.",
      [("selim", "15 Şubat 1979. Oku.")], kam="extreme close-up on the clipping", kurgu="Gazete: 'Kervan kasası kayıp, ortak ortadan kayboldu' — 15 Şubat 1979"),
])

# ------------------------------------------------------------------ B57 KASTAMONU
EP(57, {
    "kastamonulu": ("KASTAMONULU ESNAF", "KASTAMONU SHOPKEEPER, a 52-year-old Turkish man, wool vest, cap", "male voice"),
    "siyezci": ("SİYEZ ÜRETİCİSİ", "SIYEZ FARMER, a 60-year-old Turkish woman, flowered headscarf, holding ancient wheat ears", "female voice"),
}, {
    "A": ("Kastamonu çarşısı", "a market in Kastamonu with old Ottoman houses and the castle on the hill"),
    "B": ("Mahmut Bey Camii", "the wooden Mahmut Bey Mosque with painted wooden ceiling and columns"),
    "C": ("Siyez tarlası ve değirmen", "a field of ancient siyez wheat and a stone mill"),
    "D": ("Banka arşivi", "a dusty old bank archive room with shelves of ledgers"),
}, [
    S("Gemi maketlerini satar.", "A", ["kerem", "kastamonulu"],
      "The shopkeeper admires a ship model and pays.",
      [("kastamonulu", "Sinop'un gemisi Kastamonu'ya demir attı."), ("kerem", "Hem de el işi!")], k="s"),
    S("Ahşap Mahmut Bey Camii.", "B", ["kerem", "elif"],
      "Kerem and Elif look up at the painted wooden ceiling.",
      [("elif", "Çivisiz ahşap, yedi yüz yıllık."), ("kerem", "Ustalar çiviyi değil sabrı kullanmış.")]),
    S("Siyez buğdayının Göbeklitepe'ye uzanan hikâyesi.", "C", ["kerem", "siyezci"],
      "The farmer shows wheat ears.",
      [("siyezci", "Siyez, insanlığın ilk buğdaylarından."), ("kerem", "Göbeklitepe'de de bunu yiyorlarmış!")]),
    S("Siyez bulguru alır.", "C", ["kerem", "siyezci"],
      "Kerem pays for sacks of siyez bulgur.",
      [("kerem", "Karabük'e bin yıllık buğday.")], k="a"),
    S("Leyla eski banka arşivine ulaşır.", "D", ["kerem", "leyla"],
      "Leyla and Kerem search dusty ledgers with flashlights.",
      [("leyla", "Deden 1980'den sonra buradaki şubeyi kullanmış."), ("kerem", "Neyi arıyoruz?")]),
    S("Arşiv: Rıza'nın 81 kişiye yaptığı ödeme dekontları.", "D", ["kerem", "leyla"],
      "Leyla opens a ledger full of payment slips; Kerem's eyes widen.",
      [("leyla", "1980'den 1995'e... 81 ayrı kişiye ödeme."), ("kerem", "Kaçan biri neden borç ödesin?")], kam="slow push-in on the ledger"),
])

# ------------------------------------------------------------------ B58 KARABÜK
EP(58, {
    "safranbolulu": ("SAFRANBOLULU ESNAF", "SAFRANBOLU SHOPKEEPER, a 55-year-old Turkish woman, embroidered headscarf, apron", "female voice"),
    "lokumcu": ("LOKUM USTASI", "LOKUM MAKER, a 60-year-old Turkish man, white apron, cutting Turkish delight with saffron", "male voice"),
}, {
    "A": ("Safranbolu çarşısı", "the old bazaar of Safranbolu with white Ottoman houses"),
    "B": ("Safranbolu konakları", "UNESCO-listed Ottoman mansions of Safranbolu with wooden bay windows"),
    "C": ("Cinci Hanı", "the Cinci Han caravanserai in Safranbolu, stone courtyard"),
    "D": ("Lokum atölyesi", "a Turkish delight workshop with copper pots and saffron"),
}, [
    S("Siyez bulgurunu satar.", "A", ["kerem", "safranbolulu"],
      "The shopkeeper pays for the bulgur.",
      [("safranbolulu", "Siyez bulguru sağlıklı, tükenir."), ("kerem", "Bin yıllık sağlık!")], k="s"),
    S("UNESCO listesindeki konaklar.", "B", ["kerem", "elif"],
      "Kerem and Elif walk among the mansions.",
      [("elif", "Safranbolu UNESCO listesinde."), ("kerem", "Her pencere bir göz gibi bakıyor.")]),
    S("Cinci Hanı'nda kervan ruhu.", "C", ["kerem", "leyla"],
      "Kerem and Leyla sit in the han courtyard with papers.",
      [("leyla", "Dekontları tek tek eşleştiriyorum."), ("kerem", "Bir han daha... Dedem hanları severmiş.")]),
    S("Safranlı lokumun yapılışı.", "D", ["kerem", "lokumcu"],
      "The maker cuts saffron lokum.",
      [("lokumcu", "Safran dünyanın en pahalı baharatı, bir tutam yeter."), ("kerem", "Az olsun öz olsun!")]),
    S("Safranbolu lokumu alır.", "D", ["kerem", "lokumcu"],
      "Kerem pays for boxes of lokum.",
      [("kerem", "Amasra'ya lokum.")], k="a"),
    S("Bir dekontta alıcı: 'Cevdet Karahan, 1985.'", "C", ["kerem", "leyla"],
      "Leyla holds up a slip under lamplight; both stare.",
      [("leyla", "Alıcı: Cevdet Karahan, 1985. Deden kaçmamış... Cevdet'e para göndermiş!")], kam="extreme close-up on the slip"),
])

# ------------------------------------------------------------------ B59 BARTIN
EP(59, {
    "amasrali": ("AMASRALI ESNAF", "AMASRA SHOPKEEPER, a 50-year-old Turkish man, fisherman's sweater, beard", "male voice"),
    "oymaci": ("AHŞAP OYMACISI", "WOOD CARVER, a 65-year-old Turkish man, wood shavings on clothes, carving a spoon", "elderly male voice"),
}, {
    "A": ("Amasra çarşısı", "the small souvenir bazaar of Amasra with wooden goods"),
    "B": ("Amasra Ceneviz Kalesi", "the Genoese castle of Amasra on a peninsula, turquoise sea"),
    "C": ("Oymacı dükkânı", "a wood carving shop with handmade wooden spoons and bowls"),
    "D": ("Sahil, gece", "the Amasra harbor at night"),
}, [
    S("Lokumları satar.", "A", ["kerem", "amasrali"],
      "The shopkeeper tastes lokum and pays.",
      [("amasrali", "Safranbolu lokumu turistlerin gözdesi."), ("kerem", "Safranlı, bereketli!")], k="s"),
    S("Ceneviz kalesinde gezer.", "B", ["kerem", "elif"],
      "Kerem and Elif walk on the castle walls above the sea.",
      [("elif", "Cenevizliler buradan ticaret yaparmış."), ("kerem", "Tüccarların uğrak yeri!")]),
    S("Amasra salatası yer.", "B", ["kerem", "elif"],
      "They eat Amasra salad by the sea.",
      [("kerem", "Amasra salatası. Basit ama efsane."), ("elif", "Belgesel de basit ama efsane olacak.")]),
    S("Oymacı kaşık oyar.", "C", ["kerem", "oymaci"],
      "The carver shapes a wooden spoon.",
      [("oymaci", "Amasra'nın oymacılığı kuşaktan kuşağa geçer."), ("kerem", "Dededen toruna, benim gibi.")]),
    S("Ahşap el işleri alır.", "C", ["kerem", "oymaci"],
      "Kerem pays for spoons and bowls.",
      [("kerem", "Zonguldak'a ahşap götürüyorum.")], k="a"),
    S("Elif'e tehdit mesajı gelir.", "D", ["kerem", "elif"],
      "Elif reads her phone at the harbor, frightened; Kerem comforts her.",
      [("elif", "Belgeseli yayınlarsan kariyerin biter diyor."), ("kerem", "Korkma. Bu sefer yalnız değilsin.")],
      kurgu="Mesaj: 'Belgeseli yayınlarsan kariyerin biter.'"),
])

# ------------------------------------------------------------------ B60 ZONGULDAK
EP(60, {
    "zonguldakli": ("ZONGULDAKLI ESNAF", "ZONGULDAK SHOPKEEPER, a 52-year-old Turkish man, mustache, work jacket", "male voice"),
    "madenci": ("EMEKLİ MADENCİ", "RETIRED MINER, a 75-year-old Turkish man, coal-darkened lines on his hands, old miner's helmet in his hands, flat cap", "elderly male voice, hoarse"),
    "bastonci": ("DEVREK BASTONCUSU", "CANE MAKER, a 58-year-old Turkish man, carving patterns into a wooden walking stick", "male voice"),
}, {
    "A": ("Zonguldak çarşısı", "a market in Zonguldak"),
    "B": ("Maden müzesi", "a mining museum with old helmets, lamps and a statue of Uzun Mehmet"),
    "C": ("Gökgöl Mağarası", "Gökgöl Cave with stalactites"),
    "D": ("Devrek baston atölyesi", "a Devrek cane workshop with carved wooden walking sticks"),
}, [
    S("Ahşap ürünleri satar.", "A", ["kerem", "zonguldakli"],
      "The shopkeeper pays for wooden spoons.",
      [("zonguldakli", "Amasra işi kaşık, annem bayılır."), ("kerem", "Selam söyle!")], k="s"),
    S("Uzun Mehmet ve kömürün bulunuşu.", "B", ["kerem"],
      "Kerem looks at the statue of Uzun Mehmet in the museum.",
      [("kerem", "1829'da Uzun Mehmet kömürü buldu. Bu şehir yerin altından ekmek çıkardı.")]),
    S("Gökgöl Mağarası.", "C", ["kerem", "elif"],
      "They walk through the cave.",
      [("elif", "Madencilerin şehri, mağaraların şehri."), ("kerem", "Bu şehirde herkes karanlıkta ışık aramış.")]),
    S("Devrek bastonunun yapılışı.", "D", ["kerem", "bastonci"],
      "The cane maker carves a pattern.",
      [("bastonci", "Devrek bastonu el oyması, her biri tek."), ("kerem", "Hüseyin Usta'ya bir tane ayıracağım.")]),
    S("Devrek bastonu alır.", "D", ["kerem", "bastonci"],
      "Kerem pays for walking sticks.",
      [("kerem", "Düzce'ye baston.")], k="a"),
    S("Emekli madenci, Rıza'nın 2010'da emanet ettiği mektubu getirir.", "B", ["kerem", "madenci"],
      "An old miner approaches Kerem in the museum and hands him a sealed old envelope.",
      [("madenci", "Rıza bunu 2010'da bana emanet etti. 'Torunum Kerem'e' yazıyor.")], kam="close-up on the envelope with Kerem's name"),
])
