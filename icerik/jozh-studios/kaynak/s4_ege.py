# -*- coding: utf-8 -*-
"""Sezon 4 · Zeytin Dalı · Ege (Bölüm 38-45). Eylül, ılık. Kamyonetle.
Rota: Denizli → Muğla → Aydın → İzmir → Manisa → Uşak → Afyonkarahisar → Kütahya
'81 Şehir Kutusu': Aydın'da bir takipçinin yorumuyla doğar, İzmir'de ilk 120 kutu hazırlanır
(her kutuda 250 g çam balı, 250 g ceviz ezmesi, 500 g kuru incir)."""
from ortak import EP, S, T, U

AY = "Eylül"

# ======================================================================= 38 DENİZLİ
EP(38, "Denizli", "Havlu ve Traverten",
   "Tekstil atölyesinde bir günlük iş, Pamukkale'nin beyaz basamakları ve horozun sesi.",
   "Ege'nin ilk durağı Denizli. Sabah bir havlu atölyesinde dokuma tezgâhlarının arasında bir gün çalışıp yevmiye alırlar ve pamuklu "
   "havlunun kalitesini öğrenirler. Ceviz ezmesinin yarısı bir kuruyemişçiye satılır. Atölyeden 100 havlu alırlar. İkindi Pamukkale'nin "
   "bembeyaz travertenlerinde yalınayak yürür, Hierapolis'in tiyatrosuna çıkarlar. Akşam bir Denizli horozu ötünce Mert sabah alarmı "
   "kurmayı unuttuğunu fark eder.",
   {"atolye": ("Havlu atölyesi", "a towel weaving workshop in Denizli: rows of modern looms weaving white and colored cotton towels, stacks of "
               "folded towels, bright factory light"),
    "kuruyemis": ("Kuruyemişçi", "a dried fruit and nut shop in central Denizli with sacks of nuts, jars and a scale"),
    "pamukkale": ("Pamukkale travertenleri", "the white travertine terraces of Pamukkale: dazzling white calcium pools filled with turquoise "
                  "water stepping down a hillside, a few distant visitors barefoot, the valley below"),
    "hierapolis": ("Hierapolis tiyatrosu", "the ancient Roman theater of Hierapolis above Pamukkale: steep stone seating rows, a restored stage "
                   "building, dry hills and the valley at golden hour"),
    "avlu": ("Pansiyon bahçesi", "the garden of a guesthouse in Denizli at dusk: a big tall Denizli rooster with long legs standing on a low wall, "
             "a pomegranate tree, plastic chairs, the old white pickup truck parked")},
   [
       S("08:00 iç-gündüz", "atolye", ["mert", "ali", "ustabasi"], "Tezgâhların Arasında",
         "Havlu atölyesinde bir gün çalışırlar. Ustabaşı Nurten Hanım iyi havlunun suyu ilk yıkamadan sonra çektiğini anlatır.",
         "Mert carries a tall stack of folded white towels between the clattering looms while Ali checks towels against a light and folds them "
         "neatly; Nurten walks past and adjusts Ali's fold with one quick move.",
         [("ustabasi", "İyi havlu ilk yıkamadan sonra suyu çeker. Pamuğu iyi olmalı.", "brisk, expert"),
          ("ali", "Katlamayı da öğrendik, Nurten Hanım.", "proud")],
         "slow tracking shot along the looms"),
       S("11:00 sabah", "kuruyemis", ["mert", "kuruyemisci"], "Ceviz Ezmesi Denizli'de",
         "Öğle arasında bir kuruyemişçi 30 kilo Burdur ceviz ezmesini alır.",
         "The shopkeeper tastes a piece of walnut paste, raises his eyebrows and nods; Mert sets the box on the counter and accepts the money "
         "with both hands.",
         [("kuruyemisci", "Burdur'un ezmesi buraya yakışır. Otuz kilo, altı yüz elliden.", "pleased"),
          ("mert", "Kalanı bir sürpriz için saklıyoruz.", "mysterious")],
         "static medium two-shot at the counter",
         t=U(30, "kg", 650, "satis", "Burdur ceviz ezmesi, kuruyemişçiye ({adet} kg x {fiyat} TL)")),
       S("13:30 iç-gündüz", "atolye", ["ali", "ustabasi"], "Yevmiye ve Yüz Havlu",
         "Nurten Hanım yevmiyelerini verir; atölyeden toptan fiyatına 100 pamuklu havlu alırlar.",
         "Nurten counts the day's wages into Ali's hand, then points to a stack of soft cotton towels; Ali runs his hand over them, nods and "
         "hands back a larger stack of money.",
         [("ustabasi", "Yevmiyeniz bu. Havluyu da toptan veririm, tanesi yüz seksen.", "fair"),
          ("ali", "Yüz tane alıyoruz. Gördük, öğrendik, güveniyoruz.", "confident")],
         "static medium two-shot by the stacks",
         t=[T("diger_gelir", 3000, "Havlu atölyesinde günlük iş (2 kişi)"), U(100, "havlu", 180, "alis", "Denizli pamuklu havlu (100 x 180 TL)")]),
       S("16:30 ikindi", "pamukkale", ["mert", "ali"], "Beyaz Basamaklar",
         "Pamukkale'nin bembeyaz travertenlerinde yalınayak yürürler. Sıcak su ayaklarını ısıtır.",
         "Mert and Ali walk barefoot along the white travertine edge with their shoes in their hands; Mert steps into a shallow turquoise pool and "
         "gasps at the warm water; Ali laughs and steps in beside him.",
         [("mert", "Ali, kar gibi görünüyor ama su sıcak!", "amazed"),
          ("ali", "Binlerce yılda kireçten oluşmuş basamaklar.", "awed")],
         "slow crane-down along the terraces to their feet in the water",
         t=U(2, "kişi", 600, "diger_gider", "Pamukkale-Hierapolis giriş ({adet} x {fiyat} TL)")),
       S("18:30 gün batımı", "hierapolis", ["mert", "ali"], "Tiyatronun Basamakları",
         "Hierapolis'in antik tiyatrosunun en üst sırasına çıkarlar. Mert sahneye doğru bağırır, ses geri döner.",
         "Mert cups his hands and shouts toward the empty stage from the top row; the echo returns; Ali sits on the stone seat and claps slowly "
         "like an audience of one.",
         [("mert", "Seksen bir il, yedi bölge, bir kamyonet!", "shouting, joyful"),
          ("ali", "Ve bir seyirci. Bravo.", "clapping, amused")],
         "slow crane-up from the stage to the top rows",
         t=T("yemek", 800, "Öğle ve akşam yemeği")),
       S("21:00 akşam", "avlu", ["mert", "ali"], "Denizli Horozu",
         "Pansiyon bahçesinde uzun bacaklı bir Denizli horozu ötmeye başlar. Mert sabah alarmı kurmadığını hatırlar.",
         "A tall long-legged rooster on the garden wall throws back its head and crows loudly; Mert jumps from his chair; Ali looks at him and "
         "points at the rooster.",
         [("ali", "Alarm kurmana gerek yok, Denizli horozu var.", "laughing"),
          ("mert", "Bu horoz akşam dokuzda ötüyorsa sabah kaçta öter?", "worried")],
         "static medium two-shot with the rooster in the foreground",
         t=[T("konaklama", 1200, "Pansiyon, 1 gece"), T("ulasim", 1500, "Yakıt: Denizli-Muğla")]),
   ],
   misafir={"ustabasi": ("NURTEN HANIM", "NURTEN, a 50-year-old Turkish workshop forewoman, slim, short dark hair, glasses on a chain, a navy "
                         "work smock", "adult female voice, brisk and expert, Denizli Turkish"),
            "kuruyemisci": ("KURUYEMİŞÇİ", "SHOPKEEPER, a 60-year-old Turkish man, round, a grey mustache, a beige vest", "elderly male voice")},
   ay=AY, hava="ılık", urun="Denizli havlusu ve tekstili, Buldan bezi, Denizli horozu; Pamukkale ve Hierapolis (UNESCO)",
   sponsor="Ev tekstili, havlu ya da termal turizm alanında",
   kapak=("pamukkale", ["mert", "ali"], "Mert and Ali stand barefoot in a turquoise pool on the dazzling white travertine terraces of Pamukkale, "
          "holding their shoes, the valley behind, bright sun", "Pamukkale'nin bembeyaz basamaklarında yalınayak Mert ve Ali."),
   yakinda=("avlu", ["mert"], "A huge rooster silhouette crowing on a garden wall against a deep blue dusk sky, Mert's startled face in the "
            "foreground lit by a warm lamp", "Lacivert gökyüzüne karşı öten bir horoz ve irkilen Mert."),
   tiktok="Pamukkale'de yalınayak + akşam 9'da öten horoz 🐓 #JozhStudios",
   ig=("Ege başladı! ☀️ Denizli'de bir havlu atölyesinde bütün gün çalıştık, iyi havlunun sırrını öğrendik. 🧺\n\n"
       "Pamukkale'nin beyaz basamaklarında yalınayak yürüdük, Hierapolis'te Mert seyircisiz bir konser verdi. 😂\n\nVe Denizli horozu akşam dokuzda öttü. Kasa: {KASA}"),
   tags=["#Denizli", "#Pamukkale", "#DenizliHorozu"],
   son="Denizli horozu akşam dokuzda ötüyor. Sabah ne olacak?",
   teaser="Havlu tezgâhları, beyaz basamaklar ve vaktinden önce öten bir horoz. Bölüm 38: Denizli. Pek yakında.")

# ======================================================================= 39 MUĞLA
EP(39, "Muğla", "Çam Ormanında Kaybolmak",
   "Çam balının peşinde ormanda kaybolurlar; Muğla'nın beyaz evleri ve otelde havlu satışı.",
   "Horoz sabah beşte öter; kimse uyuyamaz. Muğla'nın beyaz badanalı eski evlerinin arasında kahvaltı ederler. Bir otel 50 havlu alır. Çam "
   "balı üreticisi Fikret Bey'i bulmak için ormana girerler ama telefon çekmez ve kaybolurlar. Çam ağaçlarının gövdesindeki beyaz salgıyı "
   "gören Ali, arıların burada çalıştığını anlar ve sesi takip ederler. Fikret Bey onları bulur ve dünyadaki çam balının büyük kısmının bu "
   "ormanlardan geldiğini anlatır. 60 kilo alırlar. Gece kasa tehlikeli derecede azalmıştır.",
   {"ev": ("Muğla eski evleri", "a narrow cobbled street of old Muğla: whitewashed houses with tall chimneys and wooden bay windows, flower pots, "
           "a small café table"),
    "otel": ("Otel çamaşırhanesi", "the laundry room of a seaside hotel near Muğla: shelves of folded white towels, big washing machines, a "
             "window with a glimpse of the sea"),
    "orman": ("Çam ormanı", "a dense red pine forest on hills near Muğla: tall pines with white waxy secretions on their bark, dry needles on "
              "the ground, beams of light through the branches, no path"),
    "arilik": ("Çam balı arılığı", "a clearing in the pine forest with blue and white wooden beehives, a small shed, honey frames, a pickup "
               "path"),
    "pansiyon": ("Pansiyon odası", "a simple guesthouse room in Muğla at night: two beds, honey jars stacked in crates, a window open to the "
                 "crickets")},
   [
       S("08:00 sabah", "ev", ["mert", "ali"], "Beşte Öten Horoz",
         "Horoz sabah beşte ötmüş, gözleri şiş. Muğla'nın beyaz evlerinin arasında kahvaltı ederler.",
         "Mert sits at a small café table with heavy eyes, slowly lowering his head onto his folded arms; Ali, equally sleepy, pushes a tea glass "
         "toward him and yawns.",
         [("mert", "Horoz beşte öttü Ali. Beşte!", "exhausted"),
          ("ali", "Denizli horozu sözünü tutar.", "yawning, smiling")],
         "static medium two-shot at the café table",
         t=T("yemek", 600, "Kahvaltı")),
       S("10:30 iç-gündüz", "otel", ["ali", "otelci"], "Elli Havlu",
         "Bir otelin çamaşırhanesinde kat şefi 50 Denizli havlusunu alır.",
         "The housekeeping manager unfolds a white towel, rubs it between her fingers and nods; Ali hands over the stack and she signs a receipt "
         "on his notebook.",
         [("otelci", "Denizli pamuğu. Elli tane alırım, tanesi üç yüz.", "practical"),
          ("ali", "Misafirleriniz farkı hissedecek.", "polite")],
         "static medium two-shot among the shelves",
         t=U(50, "havlu", 300, "satis", "Denizli havlusu, otele ({adet} x {fiyat} TL)")),
       S("13:00 öğle", "orman", ["mert", "ali"], "Kaybolduk",
         "Çam balı üreticisini bulmak için ormana girerler. Telefon çekmez; her çam birbirine benzer.",
         "Mert holds his phone high in the air searching for signal while turning in a circle among identical pines; Ali stands still, looking at "
         "the white waxy secretions on a pine trunk and touching it with a finger.",
         [("mert", "Çekmiyor! Her ağaç aynı Ali!", "panicking"),
          ("ali", "Dur. Bu beyaz salgı... arılar bundan bal yapıyor. Arılar yakında.", "focused")],
         "slow orbit around them among the pines"),
       S("13:30 öğle", "orman", ["mert", "ali", "fikret"], "Arıların Sesi",
         "Arıların vızıltısını takip ederler. Ağaçların arasından Fikret Bey çıkar.",
         "Mert and Ali walk slowly toward a growing buzzing sound, pushing branches aside; a man in a beekeeper's hat steps out from behind a pine "
         "and raises his eyebrows at them.",
         [("fikret", "Kaybolanlar siz misiniz? Sesinizi arılar duydu.", "amused"),
          ("mert", "Fikret Bey! Arılarınız hayatımızı kurtardı.", "relieved")],
         "static medium three-shot between the pines"),
       S("15:30 ikindi", "arilik", ["mert", "ali", "fikret"], "Çam Balı",
         "Fikret Bey çam balının çiçekten değil, çamdaki salgıdan yapıldığını anlatır. 60 kilo alırlar; kasa çok azalır.",
         "Fikret pours dark amber pine honey from a frame into a jar and hands a spoon to Mert; Ali counts money slowly, looks at what is left in "
         "his hand and swallows.",
         [("fikret", "Dünyadaki çam balının büyük kısmı bu ormanlardan çıkar. Kilosu beş yüz elli.", "proud"),
          ("ali", "Altmış kilo. Kasada çok az kaldı ama doğru mal bu.", "nervous, sure")],
         "slow push-in on the jar and the money",
         t=U(60, "kg", 550, "alis", "Muğla çam balı ({adet} kg x {fiyat} TL)")),
       S("22:00 iç-gece", "pansiyon", ["mert", "ali"], "Kasa İnce",
         "Gece pansiyonda Ali kasayı gösterir: yolculuğun en ince günü. Mert endişelenmek yerine gülümser.",
         "Ali sits on his bed showing the notebook page to Mert and taps a low number; Mert, sitting on the crates of honey, leans back and smiles "
         "calmly.",
         [("ali", "Kasa yolculuğun en ince yerinde Mert.", "worried"),
          ("mert", "Ama ilk kez mal elimizde ve satılacağını biliyoruz.", "calm, confident")],
         "static medium two-shot from the window",
         t=[T("konaklama", 1300, "Pansiyon, 1 gece"), T("ulasim", 1600, "Yakıt: Muğla-Aydın")]),
   ],
   misafir={"otelci": ("KAT ŞEFİ", "HOUSEKEEPING MANAGER, a 45-year-old Turkish woman, neat bun, a grey hotel uniform, a name badge without text",
                       "adult female voice, practical"),
            "fikret": ("FİKRET BEY", "FİKRET, a 61-year-old Turkish beekeeper, wiry, a tanned lined face, a grey beard, a beekeeper's hat with "
                       "the veil pushed back, a light khaki shirt", "elderly male voice, amused, Aegean Turkish")},
   ay=AY, hava="ılık", urun="Çam balı, beyaz badanalı Muğla evleri, Bodrum, Datça bademi",
   sponsor="Çam balı, arıcılık ya da otel turizmi alanında",
   kapak=("orman", ["mert", "ali"], "Mert holds his phone high searching for signal among towering identical pines while Ali calmly touches the "
          "white waxy bark, beams of light through the forest", "Ormanda kaybolmuş Mert telefonunu kaldırıyor, Ali çamdaki salgıya dokunuyor."),
   yakinda=("orman", ["fikret"], "A mysterious figure in a beekeeper's hat steps out from behind a pine in a dark forest, backlit by a beam of "
            "light, bees glowing in the air", "Karanlık ormanda ağacın arkasından çıkan arıcı şapkalı bir figür."),
   tiktok="Çam balının peşinde ormanda kaybolduk 🌲🐝 #JozhStudios",
   ig=("Horoz sabah beşte öttü. 😴 Muğla'nın beyaz evlerinde kendimize geldik, bir otel 50 havlumuzu aldı.\n\n"
       "Çam balı üreticisini ararken ormanda kaybolduk! Ali çamdaki beyaz salgıyı gördü: 'Arılar yakında.' 🐝 Fikret Bey bizi buldu.\n\n"
       "60 kilo çam balı aldık. Kasa yolculuğun en ince yerinde: {KASA}"),
   tags=["#Muğla", "#ÇamBalı", "#Kaybolduk"],
   son="Kasa yolculuğun en ince yerinde. Ama mal ellerinde.",
   teaser="Her ağacın aynı göründüğü bir orman ve arıların sesi. Bölüm 39: Muğla. Pek yakında.")

# ======================================================================= 40 AYDIN
EP(40, "Aydın", "İncir Zamanı",
   "İncir hasadı, zeybek ve bir takipçinin fikri: '81 Şehir Kutusu'.",
   "Eylül Aydın'da incir zamanıdır. Sabah Kuşadası'nda bir otel kalan 50 havluyu alır. Çam balının yarısı Aydın'da bir kahvaltıcıya satılır. "
   "İncir bahçesinde yere düşen olgun incirlerin güneşte kurutulmasını izler, 150 kilo kuru incir alırlar. Akşam bir köy meydanında "
   "zeybek oynayan efelere katılırlar. Gece Ali bir yorumu yüksek sesle okur: 'Her şehirden bir şey koyduğunuz bir kutu yapsanıza.' "
   "Mert yatağından fırlar.",
   {"otel": ("Kuşadası'nda otel", "the back service entrance of a hotel in Kuşadası: a loading area, the old white pickup truck with towels in "
             "the back, palm-free sea view between buildings"),
    "kahvalti": ("Köy kahvaltısı", "a village breakfast garden near Aydın: wooden tables under olive trees, honey, olives, figs and cheese"),
    "incir": ("İncir bahçesi", "a fig orchard near Aydın in September: broad-leafed fig trees, ripe purple-green figs fallen onto clean drying "
              "mats, figs drying in the sun on wooden racks"),
    "meydan": ("Köy meydanı", "a village square near Aydın at dusk: a big plane tree, string lights, a drum and zurna, men in traditional efe "
               "costumes with wide sashes and headscarves dancing zeybek slowly"),
    "oda": ("Pansiyon odası", "a simple guesthouse room near Aydın at night: two beds, sacks of dried figs, a phone glowing")},
   [
       S("08:30 sabah", "otel", ["mert", "ali", "otelci"], "Son Havlular",
         "Kuşadası'nda bir otel kalan 50 Denizli havlusunu alır.",
         "The hotel manager pulls a towel from the stack in the pickup bed and checks the weave against the light; she nods and signals two "
         "staff members, out of focus, to carry the stack inside; Ali receives an envelope.",
         [("otelci", "Kalanların hepsini alıyorum. Tanesi üç yüz.", "decisive"),
          ("ali", "Havlular bitti, Denizli bitti.", "satisfied")],
         "static medium three-shot behind the pickup",
         t=U(50, "havlu", 300, "satis", "Denizli havlusu, Kuşadası'nda otele ({adet} x {fiyat} TL)")),
       S("10:30 sabah", "kahvalti", ["mert", "kahvaltici"], "Çam Balı Kahvaltıda",
         "Köy kahvaltıcısı 30 kilo çam balını alır. Kasa yeniden nefes alır.",
         "The breakfast garden owner drizzles dark pine honey over a slice of bread, tastes it and claps her hands; Mert hands her the jars from "
         "a crate and counts the money she gives him.",
         [("kahvaltici", "Çam balı kahvaltının sultanıdır. Otuz kilo, sekiz yüz elliden.", "delighted"),
          ("mert", "Ali, kasa nefes aldı!", "relieved, shouting")],
         "static medium two-shot at the table under the olive trees",
         t=[U(30, "kg", 850, "satis", "Muğla çam balı, kahvaltıcıya ({adet} kg x {fiyat} TL)"), T("yemek", 500, "Köy kahvaltısı")]),
       S("14:00 öğle", "incir", ["mert", "ali", "incirci"], "Yere Düşen İncir",
         "İncir bahçesinde Halime Teyze, incirin dalda değil yere düşünce toplandığını, güneşte kurutulduğunu anlatır.",
         "Halime picks a ripe fig from a drying mat and splits it open to show the sweet inside; Mert takes a bite and closes his eyes; Ali turns "
         "a rack of drying figs.",
         [("incirci", "İncir olgunlaşınca kendi düşer. Sabırla beklersin.", "gentle"),
          ("mert", "Sabır yine karşımda. Ama bu sefer bal gibi.", "smiling")],
         "slow push-in under the fig trees"),
       S("15:00 ikindi", "incir", ["ali", "incirci"], "Yüz Elli Kilo İncir",
         "Yüz elli kilo kuru incir alırlar. Kuru incir uzun dayanır.",
         "Halime fills sacks with dried figs and weighs them; Ali counts money into her hand and lifts a sack onto his shoulder.",
         [("incirci", "Kilosu iki yüz yirmi. Kuru incir aylarca dayanır.", "confident"),
          ("ali", "Yüz elli kilo alıyoruz teyze.", "decisive")],
         "static medium two-shot at the scale",
         t=U(150, "kg", 220, "alis", "Aydın kuru inciri ({adet} kg x {fiyat} TL)")),
       S("20:00 akşam", "meydan", ["mert", "ali", "efe"], "Zeybek",
         "Köy meydanında efeler zeybek oynar. Yaşlı efe Mert'i çağırır; Mert ağır adımları taklit eder.",
         "An old efe in traditional costume dances zeybek slowly with arms raised, then beckons Mert; Mert steps in and imitates the slow proud "
         "movements, wobbling on one leg; Ali films and laughs.",
         [("efe", "Zeybek acele etmez. Ağır, vakur, toprağa basarak.", "proud, slow"),
          ("mert", "Ağır, vakur... düşmeden!", "concentrating")],
         "slow orbit around the dancers under the plane tree"),
       S("23:00 iç-gece", "oda", ["mert", "ali"], "Bir Kutu Fikri",
         "Gece Ali bir takipçi yorumunu okur: 'Her şehirden bir şey koyduğunuz bir kutu yapsanıza.' Mert yatağından fırlar.",
         "Ali lies on his bed reading comments on his phone and suddenly sits up; he reads one aloud; Mert jumps out of bed, grabs a dried fig "
         "from a sack and holds it up like a lightbulb idea.",
         [("ali", "Bir takipçi yazmış: 'Her şehirden bir şey koyduğunuz bir kutu yapsanıza.'", "excited"),
          ("mert", "Seksen Bir Şehir Kutusu! Ali, bu bizim markamız!", "electrified")],
         "slow push-in on Mert holding up the fig",
         t=[T("konaklama", 1200, "Pansiyon, 1 gece"), T("ulasim", 1000, "Yakıt: Aydın-İzmir")]),
   ],
   misafir={"otelci": ("OTEL MÜDÜRÜ", "HOTEL MANAGER, a 42-year-old Turkish woman, sharp bob haircut, a navy blazer", "adult female voice, decisive"),
            "kahvaltici": ("KAHVALTICI", "BREAKFAST GARDEN OWNER, a 55-year-old Turkish woman, cheerful, a straw hat, a floral apron",
                           "adult female voice, delighted, Aegean Turkish"),
            "incirci": ("HALİME TEYZE", "HALİME, a 67-year-old Turkish fig farmer, small, a white headscarf, a light cardigan, fig-stained "
                        "hands", "elderly female voice, gentle, Aydın Turkish"),
            "efe": ("YAŞLI EFE", "OLD EFE, a 70-year-old Turkish man in a traditional efe costume: a short embroidered jacket, wide sash, "
                    "knee-length baggy trousers and a headscarf with tassels, a white mustache", "elderly male voice, proud")},
   ay=AY, hava="ılık", urun="Aydın inciri (kuru incir), zeytin, zeybek; Afrodisias, Didim, Kuşadası",
   sponsor="İncir, zeytinyağı ya da Ege kültürü alanında",
   kapak=("meydan", ["mert", "efe", "ali"], "Under a huge plane tree with string lights, Mert imitates an old efe's proud zeybek pose with arms "
          "raised, wobbling, Ali laughing and filming", "Ulu çınarın altında zeybek pozu veren Mert ve yaşlı efe."),
   yakinda=("oda", ["mert"], "In a dark room Mert holds up a single dried fig into a beam of phone light as if it were a glowing lightbulb, "
            "his eyes shining with an idea", "Karanlık odada fikir ampulü gibi bir inciri kaldıran Mert."),
   tiktok="Bir takipçinin yorumu her şeyi değiştirdi 💡 #81ŞehirKutusu #JozhStudios",
   ig=("Aydın'da incir zamanı! 🍯 Halime Teyze: 'İncir olgunlaşınca kendi düşer.' Köy meydanında zeybek oynadık (Mert düşmedi!). 🕺\n\n"
       "Gece bir takipçimizin yorumu: 'Her şehirden bir şey koyduğunuz bir kutu yapsanıza.' 💡\n\n"
       "81 Şehir Kutusu doğuyor. Kutuda ne olsun? Yorumlara yazın! Kasa: {KASA}"),
   tags=["#Aydın", "#İncir", "#81ŞehirKutusu"],
   son="Bir takipçinin yorumu: '81 Şehir Kutusu' fikri doğar.",
   teaser="Yere düşen incirler, ağır bir zeybek ve bir yorumla doğan marka. Bölüm 40: Aydın. Pek yakında.")

# ======================================================================= 41 İZMİR
EP(41, "İzmir", "İlk Kutular",
   "Kemeraltı'nda ambalaj, boyoz ve gevrek, Kordon'da 120 kutu ve Hasan'dan müjde.",
   "İzmir'de sabah boyoz ve gevrekle güne başlarlar. Kemeraltı Çarşısı'nda kutu için bir matbaacı ve ambalajcı bulurlar. Bir öğrenci "
   "evinin salonunu bir günlüğüne kiralayıp ilk 120 '81 Şehir Kutusu'nu hazırlarlar: Muğla'nın çam balı, Burdur'un ceviz ezmesi, Aydın'ın "
   "inciri. Kutular ön siparişle tükenir. Akşam Kordon'da gün batarken Hasan arar: banka, domates satışları sayesinde sera kredisini "
   "yapılandırmıştır. Saat Kulesi'nin önünde Ali ilk kez gözyaşını saklamaz.",
   {"boyoz": ("Boyozcu", "a small boyoz bakery stand in İzmir in the morning: trays of flaky round boyoz pastries, boiled eggs, simit-like "
              "gevrek rings, tea glasses, a busy street behind"),
    "kemeralti": ("Kemeraltı Çarşısı", "a narrow lane in İzmir's Kemeraltı bazaar: a small printing and packaging shop with stacks of plain "
                  "kraft cardboard boxes, rolls of paper and a printing press"),
    "salon": ("Kiralık salon", "a bright rented apartment living room in İzmir turned into a packing room: long tables covered with plain kraft "
              "boxes, jars of honey, walnut paste rolls and bags of dried figs, tape rolls"),
    "kordon": ("Kordon", "İzmir's Kordon seaside promenade at sunset: a wide grassy waterfront, the calm bay glowing orange, palm trees, "
               "distant ferries"),
    "saat": ("Konak, Saat Kulesi", "Konak Square in İzmir at dusk: the ornate Ottoman clock tower lit up, pigeons, the sea behind")},
   [
       S("08:30 sabah", "boyoz", ["mert", "ali"], "Boyoz ve Gevrek",
         "İzmir'de güne boyoz ve haşlanmış yumurtayla başlarlar. Mert simide 'gevrek' denmesine alışamaz.",
         "Mert holds up a sesame ring and looks at it suspiciously; Ali bites into a flaky boyoz with a boiled egg; Mert finally bites the ring "
         "and shrugs approvingly.",
         [("mert", "Ali, bu bildiğin simit!", "protesting"),
          ("ali", "İzmir'de gevrek. Tartışma, ye.", "laughing")],
         "static medium two-shot at the stand",
         t=T("yemek", 400, "Boyoz, gevrek ve çay")),
       S("10:30 sabah", "kemeralti", ["mert", "ali", "matbaaci"], "Kutunun Kendisi",
         "Kemeraltı'nda bir matbaacıdan 120 sade kraft kutu, iç ambalaj ve etiket alırlar. Kutunun üstünde sadece bir harita çizimi olacaktır.",
         "The printer unfolds a plain kraft box and shows a simple printed outline of a map on its lid without readable text; Mert holds it up to "
         "the light like a trophy; Ali counts money onto the counter.",
         [("matbaaci", "Yüz yirmi kutu, iç ambalaj, etiket. Tanesi altmış.", "businesslike"),
          ("mert", "Bu kutuyu bir gün herkes tanıyacak.", "dreamy")],
         "slow push-in on the box lid",
         t=U(120, "kutu", 60, "diger_gider", "81 Şehir Kutusu ambalajı: kutu, iç ambalaj, etiket ({adet} x {fiyat} TL)")),
       S("13:00 iç-gündüz", "salon", ["mert", "ali"], "Yüz Yirmi Kutu",
         "Kiralık salonda kutuları doldururlar: 250 gram çam balı, 250 gram ceviz ezmesi, yarım kilo incir.",
         "Mert and Ali work at the long table like an assembly line: Mert places a jar of honey and a roll of walnut paste in each box, Ali adds a "
         "bag of figs, closes the lid and stacks it on a growing tower.",
         [("ali", "Bal, ezme, incir, kapak. Bal, ezme, incir, kapak.", "rhythmic, focused"),
          ("mert", "Yüz on dokuz... yüz yirmi! Bitti!", "exhausted, triumphant")],
         "static wide shot from the end of the table, slow push-in",
         t=T("diger_gider", 1500, "Salon kirası, 1 gün")),
       S("16:00 ikindi", "salon", ["mert", "ali"], "Tükendi",
         "İlk 120 kutu ön siparişle tükenir. Ali ekrana bakıp donar.",
         "Ali sits on the floor against the tower of boxes refreshing his phone; he freezes, then slowly turns the screen to Mert; Mert falls "
         "backward onto a pile of empty cardboard with his arms spread.",
         [("ali", "Yüz yirmi kutu... hepsi satıldı. Kırk dakikada.", "stunned"),
          ("mert", "Biz marka olduk Ali!", "ecstatic, lying down")],
         "slow crane-down onto them",
         t=U(120, "kutu", 950, "satis", "81 Şehir Kutusu, ilk seri (Ege) ({adet} x {fiyat} TL)"),
         kurgu="Kutuda gerçek bir marka logosu yoktur; iş birliği yapılırsa üreticiler videoda belirtilir."),
       S("19:00 gün batımı", "kordon", ["mert", "ali", "~hasan"], "Babadan Müjde",
         "Kordon'da gün batarken Hasan arar: banka, domates satışları sayesinde sera kredisini yapılandırmıştır.",
         "Ali walks along the waterfront with the phone at his ear, stops, and covers his mouth with his hand; Mert, a step behind, sees his face "
         "and starts to smile. Ali's lips stay closed while his father speaks.",
         [("hasan", "Oğlum, banka yapılandırdı! Domatesler kurtardı serayı!", "joyful, from the phone speaker"),
          ("ali", "Baba... çok sevindim.", "emotional, barely speaking")],
         "slow push-in from behind Mert toward Ali and the glowing bay"),
       S("21:00 akşam", "saat", ["mert", "ali"], "Saat Kulesi",
         "Saat Kulesi'nin önünde Ali ilk kez gözyaşını saklamaz. Mert ona sarılır.",
         "Ali stands in front of the lit clock tower wiping tears with the back of his hand and laughing at the same time; Mert pulls him into a "
         "big hug and pats his back; pigeons rise behind them.",
         [("mert", "Ağla kardeşim. Bunu hak ettik.", "warm"),
          ("ali", "Seksen bir ilin en güzel akşamı bu.", "crying and laughing")],
         "slow orbit around them with the clock tower behind",
         t=[T("konaklama", 1500, "Otel, 1 gece"), T("ulasim", 900, "Yakıt: İzmir-Manisa")]),
   ],
   misafir={"matbaaci": ("MATBAACI", "PRINTER, a 58-year-old Turkish man, grey ponytail, round glasses, ink-stained apron", "mature male voice, businesslike")},
   ay=AY, hava="ılık", urun="Boyoz, gevrek, kumru; Kemeraltı Çarşısı, Saat Kulesi, Kordon, Efes",
   sponsor="Yerel üretici, ambalaj ya da İzmir gastronomisi alanında",
   kapak=("salon", ["mert", "ali"], "Mert and Ali sit exhausted but beaming in front of a tall tower of plain kraft gift boxes, Mert lying back "
          "on cardboard with arms spread, Ali showing his phone", "Kraft kutulardan bir kulenin önünde yorgun ama mutlu Mert ve Ali."),
   yakinda=("saat", ["mert", "ali"], "Two silhouettes embracing in front of a glowing ornate clock tower at dusk, pigeons rising into the sky",
            "Işıklı saat kulesinin önünde sarılan iki silüet."),
   tiktok="81 Şehir Kutusu: 120 kutu 40 dakikada tükendi 📦 #JozhStudios",
   ig=("İzmir'de boyozla başladık (Mert hâlâ 'simit' diyor 😅). Kemeraltı'ndan kutularımızı aldık ve ilk 120 '81 Şehir Kutusu'nu hazırladık: "
       "Muğla çam balı, Burdur ceviz ezmesi, Aydın inciri. 📦\n\nKırk dakikada tükendi!\n\n"
       "Ve akşam Hasan Amca aradı: sera kurtuldu. 🍅🥹 Kasa: {KASA}"),
   tags=["#İzmir", "#81ŞehirKutusu", "#Kemeraltı"],
   son="İlk 120 kutu tükendi ve Hasan'ın serası kurtuldu.",
   teaser="Boyoz, gevrek, yüz yirmi kutu ve bir babadan müjde. Bölüm 41: İzmir. Pek yakında.")

# ======================================================================= 42 MANİSA
EP(42, "Manisa", "Bağ Bozumu",
   "Sultaniye üzüm bağında hasat, mesir macunu ve Spil Dağı'nın eteğinde bir ders.",
   "Manisa'da sabah sultaniye üzüm bağında bağ bozumuna katılır, yevmiye alırlar. Kalan 90 kilo incir bir kuru meyve toptancısına satılır. "
   "Öğlen kırk bir çeşit baharattan yapıldığı anlatılan mesir macununun hikâyesini dinler, bir macun ustasından 300 kavanoz alırlar. Spil "
   "Dağı'nın eteğinde Mert, İzmir'deki başarıdan sonra hemen bin kutu sipariş almak ister; Ali bu kez sesini yükseltmeden 'hayır' der ve "
   "nedenini anlatır. Mert ilk kez hemen ikna olur.",
   {"bag": ("Sultaniye üzüm bağı", "a vineyard near Manisa during harvest: rows of vines heavy with pale green seedless grapes, plastic crates "
            "full of bunches, workers far in the background, Spil mountain behind"),
    "toptanci": ("Kuru meyve toptancısı", "a dried fruit wholesale warehouse in Manisa: stacked sacks of raisins and figs, a forklift parked, "
                 "a big floor scale"),
    "macun": ("Mesir macunu ustası", "a small traditional sweets workshop in Manisa: a big copper cauldron of thick dark mesir paste, rows of "
              "small glass jars, bundles of spices, warm light"),
    "spil": ("Spil Dağı eteği", "a viewpoint on the lower slopes of Spil mountain above Manisa at sunset: pine trees, a wide view of the "
             "plain and vineyards, the old white pickup truck parked")},
   [
       S("07:30 sabah", "bag", ["mert", "ali", "bagci"], "Makasla Hasat",
         "Sultaniye üzüm bağında hasada katılırlar. Bağcı Ramiz Amca salkımın nasıl kesileceğini gösterir.",
         "Ramiz shows Mert how to hold a pale green bunch from below and snip the stem with small shears; Mert cuts one and places it gently in a "
         "crate; Ali works the next vine.",
         [("bagci", "Salkımı alttan tut, sapından kes. Üzüm ezilmesin.", "teaching"),
          ("mert", "Kayısıdan sonra üzüm. Ben meyve uzmanı oluyorum.", "proud")],
         "slow tracking shot along the vine row"),
       S("11:30 sabah", "toptanci", ["ali", "toptanci"], "Kalan İncir",
         "Bir kuru meyve toptancısı kalan 90 kilo Aydın incirini alır. Yevmiye de cepte.",
         "The wholesaler pours figs onto the big floor scale and nods; Ali writes in the notebook and receives the money, then pats his pocket "
         "where the day's wages are.",
         [("toptanci", "Doksan kilo, üç yüz yirmiden. İyi incir.", "brief"),
          ("ali", "Bağ yevmiyesi de cepte. Güzel sabah.", "pleased")],
         "static medium two-shot by the scale",
         t=[U(90, "kg", 320, "satis", "Aydın kuru inciri, toptancıya ({adet} kg x {fiyat} TL)"), T("diger_gelir", 2400, "Bağ bozumu yevmiyesi (2 kişi)")]),
       S("14:00 iç-gündüz", "macun", ["mert", "ali", "macuncu"], "Kırk Bir Baharat",
         "Mesir macunu ustası macunun yüzyıllar önce bir şifa için yapıldığı söylenen hikâyesini anlatır.",
         "The sweets maker stirs the dark thick paste in the copper cauldron and lifts the paddle so it stretches; she lets Mert taste a little "
         "from a spoon; Mert's eyes water at the spicy taste.",
         [("macuncu", "Kırk bir çeşit baharat derler. Her bahar dağıtılır, bütün yıl yenir.", "storytelling"),
          ("mert", "Acı, tatlı, baharat... hepsi bir arada!", "surprised")],
         "slow push-in on the cauldron"),
       S("15:00 iç-gündüz", "macun", ["ali", "macuncu"], "Üç Yüz Kavanoz",
         "Üç yüz kavanoz mesir macunu alırlar. Uşak ve Kütahya'da satılacaktır.",
         "The sweets maker seals small glass jars and places them in boxes; Ali checks the seals, nods and counts money onto the table.",
         [("macuncu", "Kavanozu yetmiş. Bozulmaz, kuralınıza uyar.", "smiling"),
          ("ali", "Üç yüz kavanoz alıyoruz.", "decisive")],
         "static medium two-shot by the jars",
         t=[U(300, "kavanoz", 70, "alis", "Manisa mesir macunu ({adet} kavanoz x {fiyat} TL)"), T("yemek", 800, "Öğle ve akşam yemeği")]),
       S("18:30 gün batımı", "spil", ["mert", "ali"], "Bin Kutu",
         "Spil Dağı'nın eteğinde Mert hemen bin kutu sipariş almak ister. Ali bu kez sakin bir 'hayır' der.",
         "Mert paces excitedly in front of the parked pickup, gesturing at the plain; Ali leans on the hood, listens, then calmly holds up the "
         "notebook and counts on his fingers; Mert stops pacing.",
         [("mert", "Bin kutu ön sipariş alalım Ali! Talep var!", "excited"),
          ("ali", "Bin kutuyu kim doldurur, nerede, hangi parayla? Önce iki yüz.", "calm, firm")],
         "static medium two-shot by the pickup, the plain glowing behind"),
       S("19:00 gün batımı", "spil", ["mert", "ali"], "İkna",
         "Mert bir an düşünür ve ilk kez hemen ikna olur. Ali şaşırır.",
         "Mert stands still for a moment, then nods slowly and offers his hand; Ali blinks in surprise, shakes it, and they both laugh at the "
         "sunset.",
         [("mert", "Haklısın. İki yüz kutu, sağlam iş.", "thoughtful"),
          ("ali", "Mert... hiç itiraz etmedin. Hasta mısın?", "astonished, laughing")],
         "slow dolly-out to the wide view",
         t=[T("konaklama", 1200, "Pansiyon, 1 gece"), T("ulasim", 1300, "Yakıt: Manisa-Uşak")]),
   ],
   misafir={"bagci": ("RAMİZ AMCA", "RAMİZ, a 68-year-old Turkish vineyard owner, thin, a white stubble, a straw hat and a sweat-stained shirt",
                      "elderly male voice, teaching, Manisa Turkish"),
            "toptanci": ("TOPTANCI", "WHOLESALER, a 50-year-old Turkish man, heavy, short grey hair, a polo shirt", "adult male voice, brief"),
            "macuncu": ("MACUN USTASI", "SWEETS MAKER, a 58-year-old Turkish woman, round, a white cap, a white apron, warm eyes",
                        "adult female voice, storytelling")},
   ay=AY, hava="ılık", urun="Sultaniye üzüm, kuru üzüm, mesir macunu; Spil Dağı",
   sponsor="Üzüm, kuru meyve ya da mesir macunu alanında",
   kapak=("bag", ["mert", "ali"], "Mert and Ali hold up big bunches of pale green grapes in a sunny vineyard with Spil mountain behind, Mert with "
          "pruning shears in his teeth, both laughing", "Bağda iri salkımları kaldıran Mert ve Ali."),
   yakinda=("spil", ["mert", "ali"], "Two silhouettes shaking hands in front of an old pickup truck on a mountainside at sunset, the vast plain "
            "glowing below", "Dağ yamacında kamyonetin önünde el sıkışan iki silüet."),
   tiktok="Bağ bozumu + Mert ilk kez itiraz etmedi 😳 #JozhStudios",
   ig=("Manisa'da sultaniye üzüm bağında hasada katıldık! 🍇 Ramiz Amca: 'Salkımı alttan tut.'\n\n"
       "Mesir macununun kırk bir baharatlı hikâyesini dinledik ve 300 kavanoz aldık.\n\n"
       "Mert bin kutu istedi, Ali 'önce iki yüz' dedi... ve Mert hemen ikna oldu. 😳 Kasa: {KASA}"),
   tags=["#Manisa", "#BağBozumu", "#MesirMacunu"],
   son="Bir sonraki kutu serisi iki yüz adet olacak.",
   teaser="Salkım salkım üzüm, kırk bir baharat ve şaşırtıcı bir uzlaşma. Bölüm 42: Manisa. Pek yakında.")

# ======================================================================= 43 UŞAK
EP(43, "Uşak", "Acele İşe Şeytan Karışır",
   "Uşak halısı ustasının dersi, Karun Hazinesi ve bir ilmeğin hikâyesi.",
   "Uşak'ta mesir macununun yüz kavanozu bir şarküteriye satılır; kalanı ikinci kutu serisine ayrılır. Uşak Arkeoloji Müzesi'nde Lidya'dan kalma Karun Hazinesi'nin "
   "parıltısını görürler. Bir halı atölyesinde Zeliha Usta'nın tezgâhında ilmek atmayı denerler; Mert hızlı gitmek için ilmeği yanlış atar ve "
   "usta bütün sırayı söker: 'Acele işe şeytan karışır.' Dört küçük el dokuması halı alırlar. Akşam Mert sırayı söken ustaya kızmak yerine "
   "teşekkür eder.",
   {"sarkuteri": ("Uşak şarküterisi", "a delicatessen in central Uşak with shelves of jars, cheeses and local products, a marble counter"),
    "muze": ("Uşak Arkeoloji Müzesi", "a quiet museum gallery in Uşak with glass cases of ancient Lydian gold and silver treasures glowing "
             "under spotlights: a golden hippocampus brooch, silver vessels"),
    "atolye": ("Halı atölyesi", "a hand-knotted carpet workshop in Uşak: a large vertical loom with a half-finished carpet in deep red and "
               "blue patterns, balls of wool, a weaver's comb and knife"),
    "avlu": ("Pansiyon avlusu", "a quiet courtyard of a guesthouse in Uşak at night: a fig tree, two chairs, four rolled small carpets "
             "leaning against the wall")},
   [
       S("09:30 sabah", "sarkuteri", ["mert", "sarkuteri"], "Macun Satışı",
         "Bir şarküteri 100 kavanoz mesir macunu alır. Kalan 200 kavanoz ikinci kutu serisine ayrılır.",
         "The deli owner lines up mesir paste jars on a shelf; Mert hands over a box and looks at his phone, then grins at the deli owner.",
         [("sarkuteri", "Mesir macunu her mevsim satılır. Yüz kavanoz alırım.", "pleased"),
          ("mert", "Kavanozu yüz kırk. Kalanı kutulara saklıyoruz.", "cheerful")],
         "static medium two-shot at the counter",
         t=U(100, "kavanoz", 140, "satis", "Manisa mesir macunu, şarküteriye ({adet} kavanoz x {fiyat} TL)")),
       S("11:30 iç-gündüz", "muze", ["mert", "ali"], "Karun Hazinesi",
         "Müzede Karun Hazinesi'nin altın kanatlı denizatı broşunun önünde dururlar. Hazine yıllar önce yurt dışından geri getirilmiştir.",
         "Mert and Ali lean close to a glass case where a tiny winged golden seahorse brooch glows; Mert's breath fogs the glass a little and Ali "
         "pulls him back by the shoulder.",
         [("ali", "Lidyalılar parayı ilk kullananlardan. Ve bu hazine geri döndü.", "fascinated"),
          ("mert", "Ali, Lidyalılar bizim meslektaşlarımız!", "whisper, excited")],
         "slow push-in to the glowing brooch"),
       S("14:00 iç-gündüz", "atolye", ["mert", "zeliha"], "İlmek",
         "Halı atölyesinde Zeliha Usta ilmek atmayı gösterir. Mert hızlanmak isteyince ilmekleri yanlış atar.",
         "Zeliha ties a knot on the loom with quick precise fingers and cuts the yarn; Mert copies her, then speeds up and ties several knots "
         "fast; Zeliha stops his hand and looks closely at the row.",
         [("zeliha", "Bir ilmek, bir nefes. Sayarak.", "calm"),
          ("mert", "Usta, ben hızlandım, bakın beş tane attım!", "proud")],
         "slow push-in on the hands on the loom"),
       S("14:30 iç-gündüz", "atolye", ["mert", "ali", "zeliha"], "Bütün Sıra",
         "Zeliha Usta, Mert'in yanlış attığı ilmekler yüzünden bütün sırayı söker: 'Acele işe şeytan karışır.'",
         "Zeliha calmly cuts and pulls out the whole row of knots with her knife while Mert watches, mouth open; Ali puts a hand on Mert's "
         "shoulder, holding back a laugh.",
         [("zeliha", "Acele işe şeytan karışır evlat. Bir yanlış ilmek bütün halıyı bozar.", "firm, kind"),
          ("mert", "Bütün sıra mı? Benim yüzümden...", "stunned")],
         "static medium three-shot by the loom"),
       S("16:00 iç-gündüz", "atolye", ["ali", "zeliha"], "Dört Küçük Halı",
         "Dört küçük el dokuması Uşak halısı alırlar.",
         "Zeliha unrolls four small hand-knotted carpets one by one on the floor; Ali kneels, runs his hand over the dense knots and counts money "
         "into her hand.",
         [("zeliha", "Her biri iki ay. Tanesi altı bin.", "proud"),
          ("ali", "Dördünü de alıyoruz. Emeğinize sağlık.", "respectful")],
         "slow crane-down over the carpets",
         t=[U(4, "halı", 6000, "alis", "El dokuması küçük Uşak halısı ({adet} x {fiyat} TL)"), T("yemek", 700, "Öğle ve akşam yemeği")]),
       S("21:00 akşam", "avlu", ["mert", "ali"], "Teşekkür",
         "Akşam Mert, sırayı söken ustaya kızmak yerine mesaj atıp teşekkür eder. Ali bunu deftere 'büyük gelişme' diye yazar.",
         "Mert types a message on his phone, hesitates, then sends it and puts the phone down; Ali, beside him, opens the notebook and writes "
         "something with a smile.",
         [("mert", "Zeliha Usta'ya teşekkür ettim. Haklıydı.", "humble"),
          ("ali", "Deftere yazıyorum: Mert büyüdü, bugün ikinci kez.", "teasing, warm")],
         "static medium two-shot under the fig tree",
         t=[T("konaklama", 1100, "Pansiyon, 1 gece"), T("ulasim", 1200, "Yakıt: Uşak-Afyonkarahisar")]),
   ],
   misafir={"sarkuteri": ("ŞARKÜTERİCİ", "DELI OWNER, a 46-year-old Turkish man, neat beard, glasses, a white apron", "adult male voice"),
            "zeliha": ("ZELİHA USTA", "ZELİHA, a 64-year-old Turkish master carpet weaver, slim, a light blue headscarf, reading glasses, a long "
                       "grey cardigan, very precise hands", "elderly female voice, calm, firm, kind")},
   ay=AY, hava="ılık", urun="Uşak halısı, tarhana; Karun Hazinesi (Uşak Arkeoloji Müzesi), Ulubey Kanyonu",
   sponsor="El dokuması halı ya da kültür turizmi alanında",
   kapak=("atolye", ["mert", "zeliha", "ali"], "Zeliha calmly pulls out a whole row of knots from a red-and-blue carpet on a big loom while Mert "
          "stares in shock and Ali holds back laughter", "Halıdaki bütün sırayı söken usta ve şaşkın Mert."),
   yakinda=("muze", ["mert"], "A tiny golden winged seahorse brooch glowing in a dark glass case, Mert's amazed face reflected faintly in the "
            "glass", "Karanlık vitrinde parlayan altın kanatlı denizatı ve camda bir yansıma."),
   tiktok="Hızlı ilmek attım, usta bütün sırayı söktü 😬 #JozhStudios",
   ig=("Uşak'ta Karun Hazinesi'nin altın denizatını gördük. Lidyalılar paranın öncülerinden; meslektaşlarımız! 🪙\n\n"
       "Halı atölyesinde Mert hızlı ilmek attı, Zeliha Usta bütün sırayı söktü: 'Acele işe şeytan karışır.' 😬\n\n"
       "Mert akşam ustaya teşekkür etti. Kasa: {KASA}"),
   tags=["#Uşak", "#UşakHalısı", "#KarunHazinesi"],
   son="Mert ustaya teşekkür eder. Ali deftere 'büyük gelişme' yazar.",
   teaser="Altın bir denizatı, yanlış atılan ilmekler ve bir teşekkür. Bölüm 43: Uşak. Pek yakında.")

# ======================================================================= 44 AFYONKARAHİSAR
EP(44, "Afyonkarahisar", "Kaymak ve Kale",
   "Kaymaklı kahvaltı, 700 basamaklı kale, lokum ve termal otelde halı satışı.",
   "Afyon'da sabah kaymaklı ekmek kadayıfıyla kahvaltı ederler. Ardından kayalık tepenin üstündeki Afyon Kalesi'ne yüzlerce basamak çıkarlar; "
   "Mert yarı yolda pes etmek ister, Ali onu bekler. Bir termal otel iki Uşak halısını lobisi için alır. Bir lokum imalathanesinde "
   "kaymaklı lokumun yapılışını izler, 100 kilo lokum alırlar. Akşam Ali Kütahya'daki taksit için son hesabı yapar: 120.000 TL'ye az "
   "kalmıştır.",
   {"kahvalti": ("Kaymakçı", "a traditional kaymak shop in Afyonkarahisar: thick clotted cream on a tray, ekmek kadayıfı soaked in syrup, "
                 "honey, tea glasses, marble tables"),
    "kale": ("Afyon Kalesi basamakları", "the steep stone stairway climbing the huge black volcanic rock of Afyonkarahisar Castle, the city's "
             "rooftops and minarets far below"),
    "termal": ("Termal otel lobisi", "the lobby of a thermal spa hotel near Afyonkarahisar: polished stone floor, large windows, steam rising "
               "from outdoor pools beyond the glass"),
    "lokum": ("Lokum imalathanesi", "a Turkish delight workshop in Afyonkarahisar: a big steaming kettle of starch and sugar, trays of lokum "
              "dusted with powdered sugar, rolls of cream-filled lokum being cut"),
    "teras": ("Otel terası", "a hotel terrace in Afyonkarahisar at night with the lit castle on its dark rock above the city")},
   [
       S("08:30 sabah", "kahvalti", ["mert", "ali"], "Kaymak",
         "Kaymaklı ekmek kadayıfıyla kahvaltı ederler. Mert kaymağı kaşıkla değil, ekmekle kepçe gibi alır.",
         "Mert scoops a huge slab of thick white clotted cream onto a piece of syrupy ekmek kadayıfı and lifts it toward his mouth; Ali watches with "
         "his spoon frozen halfway.",
         [("ali", "O kadar kaymak bir kişilik değil Mert.", "laughing"),
          ("mert", "Kalede yakarım, merak etme.", "confident, mouth full")],
         "static medium two-shot at the marble table",
         t=T("yemek", 900, "Kaymaklı kahvaltı")),
       S("10:30 sabah", "kale", ["mert", "ali"], "Yüzlerce Basamak",
         "Afyon Kalesi'nin yüzlerce basamağına tırmanırlar. Mert yarı yolda oturur; Ali onu bekler.",
         "Mert sits down heavily on a stone step halfway up the castle stairway, panting; Ali, a few steps above, sits down too and waits, offering "
         "a water bottle, the city spread below.",
         [("mert", "Kaymak kalede yakılmıyor Ali, kalede kalıyor.", "panting, comic"),
          ("ali", "Beraber çıktık, beraber ineriz. Ama önce çıkacağız.", "patient")],
         "slow crane-up from the steps to the city view"),
       S("13:00 iç-gündüz", "termal", ["ali", "otelci"], "Lobide İki Halı",
         "Bir termal otel lobisi için iki küçük Uşak halısı alır.",
         "The hotel manager unrolls a small red-and-blue Uşak carpet on the polished stone floor and steps back to admire it; Ali holds the second "
         "carpet rolled under his arm and smiles.",
         [("otelci", "El dokuması Uşak halısı lobime değer katar. İkisini alıyorum.", "pleased"),
          ("ali", "Tanesi on bir bin. Dokuyan elleri misafirlerinize anlatın.", "warm")],
         "slow crane-down onto the unrolled carpet",
         t=U(2, "halı", 11000, "satis", "El dokuması Uşak halısı, termal otele ({adet} x {fiyat} TL)")),
       S("15:30 iç-gündüz", "lokum", ["mert", "ali", "lokumcu"], "Kaymaklı Lokum",
         "Lokum imalathanesinde kaymaklı lokumun rulo hâline getirilip kesildiğini izler, 100 kilo lokum alırlar.",
         "The lokum maker rolls a slab of lokum around a thick line of cream and slices it into pieces with a long knife, then hands one to each of "
         "them; Mert's eyes close; Ali nods and counts money.",
         [("lokumcu", "Kaymaklı lokum Afyon'un imzasıdır. Kilosu üç yüz.", "proud"),
          ("ali", "Yüz kilo alıyoruz. Kutuya da çok yakışır.", "planning")],
         "slow push-in on the knife cutting the roll",
         t=U(100, "kg", 300, "alis", "Afyon kaymaklı ve sade lokum ({adet} kg x {fiyat} TL)")),
       S("21:00 gece", "teras", ["mert", "ali"], "Son Hesap",
         "Gece terasta ışıklı kaleye bakarken Ali Kütahya'daki taksit için son hesabı yapar.",
         "Ali writes figures in the notebook by the light of his phone, with the lit castle on its dark rock behind; Mert leans over his shoulder "
         "and points at a number.",
         [("ali", "Kütahya'da yüz yirmi bin. Macun ve halıları satarsak tamam.", "focused"),
          ("mert", "İkinci kutu serisi de olursa üstü bile kalır.", "hopeful")],
         "static medium two-shot with the castle behind",
         t=[T("konaklama", 1300, "Otel, 1 gece"), T("ulasim", 1100, "Yakıt: Afyonkarahisar-Kütahya")]),
       S("22:30 gece", "teras", ["mert", "ali"], "Çini Fikri",
         "Mert bir fikir söyler: kutunun kapağına Kütahya'da çiniden bir harita mührü. Ali gülümser.",
         "Mert draws a small circle in the air with his finger as if designing a seal; Ali looks at him, then at the castle, and slowly smiles and "
         "nods.",
         [("mert", "Kütahya'da kutunun mührünü çiniden yaptıralım.", "inspired"),
          ("ali", "Bu fikri bütçeye yazıyorum. Küçük harfle.", "smiling, careful")],
         "slow push-in to their faces"),
   ],
   misafir={"otelci": ("OTEL MÜDÜRÜ", "HOTEL MANAGER, a 50-year-old Turkish man, tall, silver hair, a grey suit", "adult male voice, pleased"),
            "lokumcu": ("LOKUM USTASI", "LOKUM MAKER, a 55-year-old Turkish man, stout, white hair under a white cap, sugar dust on his apron",
                        "mature male voice, proud, Afyon Turkish")},
   ay=AY, hava="ılık", urun="Afyon kaymağı, sucuk, lokum, mermer, termal; Afyon Kalesi",
   sponsor="Kaymak, lokum, sucuk ya da termal turizm alanında",
   kapak=("kahvalti", ["mert", "ali"], "Mert lifts a huge slab of thick clotted cream on syrupy dessert toward his mouth while Ali watches, spoon "
          "frozen, on a marble breakfast table", "Kocaman bir kaymak dilimini ağzına götüren Mert ve donakalan Ali."),
   yakinda=("kale", ["mert", "ali"], "Two small figures resting on a steep stone stairway carved into a giant black rock, a castle silhouette "
            "above against a pale sky", "Dev kara bir kayaya oyulmuş merdivende dinlenen iki küçük figür."),
   tiktok="Afyon kaymağı vs. 700 basamak 😮‍💨 #JozhStudios",
   ig=("Afyon'da kaymaklı kahvaltı sonrası kaleye tırmandık. Mert: 'Kaymak kalede yakılmıyor, kalede kalıyor.' 😮‍💨\n\n"
       "İki Uşak halısı bir termal otelin lobisine gitti, kaymaklı lokumun yapılışını izledik ve 100 kilo aldık.\n\n"
       "Yarın Kütahya: 120.000 TL'lik taksit ve çiniden bir mühür fikri. Kasa: {KASA}"),
   tags=["#Afyonkarahisar", "#Kaymak", "#Lokum"],
   son="Yarın Kütahya: 120.000 TL'lik taksit ve kutu için çini mühür.",
   teaser="Kaymak, yüzlerce basamak ve kaymaklı lokum. Bölüm 44: Afyonkarahisar. Pek yakında.")

# ======================================================================= 45 KÜTAHYA
EP(45, "Kütahya", "Çiniden Mühür",
   "Sezon finali: çini atölyesinde kutunun mührü, ikinci kutu serisi ve 120.000 TL'lik dördüncü taksit.",
   "Kütahya'da sabah bir çini atölyesinde ustanın fırçasıyla kobalt mavisi motiflerin nasıl çizildiğini görürler. Usta, '81 Şehir Kutusu' "
   "için küçük, yazısız bir harita mührü tasarlar. Kalan iki halı satılır. Öğleden sonra 200 kutuluk ikinci seri (Afyon lokumu, "
   "Manisa macunu ve bir Kütahya çini magneti) ön siparişle tükenir. Kütahya Kalesi'nde gün batarken dördüncü taksit gider: 120.000 TL. "
   "Cemil Bey bu kez sesli mesaj bırakır.",
   {"cini": ("Çini atölyesi", "a tile workshop in Kütahya: an artist painting cobalt blue and turquoise floral motifs on a white ceramic plate "
             "with a fine brush, shelves of finished tiles and plates, a kiln"),
    "carsi": ("Kütahya çarşısı", "a shopping street in old Kütahya with Ottoman houses, a gift shop with ceramic plates and carpets in the window"),
    "salon": ("Paketleme alanı", "the back room of the tile workshop turned into a packing room: long tables with kraft gift boxes, lokum boxes, "
              "mesir jars and small round tile magnets"),
    "kale": ("Kütahya Kalesi", "the hilltop of Kütahya Castle at sunset: old stone walls and a round tower, the red-roofed city and green "
             "hills below")},
   [
       S("09:00 iç-gündüz", "cini", ["mert", "ali", "ciniusta"], "Kobalt Mavisi",
         "Çini ustası Hüsnü Usta ince fırçayla kobalt mavisi motifleri çizer. Mert'e bir yaprak çizdirir.",
         "Hüsnü guides Mert's hand as he paints a single cobalt leaf on a white plate with a fine brush; Mert holds his breath; Ali watches over "
         "their shoulders.",
         [("ciniusta", "Fırça nefesle gider. Nefes acele ederse çizgi titrer.", "calm, master"),
          ("mert", "Nefesimi tuttum usta, çizgi titremedi!", "whispering, proud")],
         "slow push-in on the brush and the plate"),
       S("10:30 iç-gündüz", "cini", ["mert", "ali", "ciniusta"], "Kutunun Mührü",
         "Usta kutu için küçük, yazısız bir harita mührü tasarlar: Türkiye'nin silüeti ve küçük bir lale.",
         "Hüsnü lifts a small round tile with a hand-painted cobalt silhouette of a map and a tiny tulip; Mert takes it in both hands like a medal; "
         "Ali pays the master.",
         [("ciniusta", "Yazı yok, sadece harita ve lale. Görüldüğü yerde tanınsın.", "proud"),
          ("ali", "İki yüz tane magnet, tanesi yüz.", "businesslike")],
         "static medium three-shot at the work table",
         t=U(200, "magnet", 100, "alis", "El yapımı çini magnet, kutu mührü ({adet} x {fiyat} TL)")),
       S("12:30 öğle", "carsi", ["ali", "dukkan"], "Macun ve Halı",
         "Bir hediyelik dükkânı kalan iki Uşak halısını alır; mesir macununun kalanı kutulara ayrılır.",
         "The shop owner unrolls a small carpet in her shop window next to ceramic plates and nods; Ali hands over the second carpet and receives "
         "an envelope.",
         [("dukkan", "Çininin yanına Uşak halısı... vitrin tamam. İkisi de benim.", "pleased"),
          ("ali", "Tanesi on bir bin. Hayırlı satışlar.", "polite")],
         "static medium two-shot by the shop window",
         t=[U(2, "halı", 11000, "satis", "El dokuması Uşak halısı, hediyelik dükkânına ({adet} x {fiyat} TL)"), T("yemek", 800, "Öğle yemeği")]),
       S("15:00 iç-gündüz", "salon", ["mert", "ali"], "İkinci Seri",
         "İkinci seri 200 kutu hazırlanır: Afyon lokumu, Manisa macunu ve çini mühür. Kutular ön siparişle tükenir.",
         "Mert places a small round cobalt tile magnet on top of each closed kraft box like a seal while Ali stacks them; Ali's phone buzzes "
         "continuously on the table and he shows Mert the screen; Mert taps the last magnet down.",
         [("ali", "İki yüz kutu, hepsi satıldı. Kutu başı bin yüz.", "proud, calm"),
          ("mert", "Ve her birinde çiniden bir mühür.", "beaming")],
         "slow tracking shot along the table of boxes",
         t=[U(200, "kutu", 1100, "satis", "81 Şehir Kutusu, ikinci seri (Ege) ({adet} x {fiyat} TL)"),
            U(200, "kutu", 80, "diger_gider", "İkinci seri ambalaj ve kargo kolisi (200 x 80 TL)")]),
       S("18:30 gün batımı", "kale", ["mert", "ali"], "Yüz Yirmi Bin",
         "Kütahya Kalesi'nde gün batarken dördüncü taksiti gönderirler: 120.000 TL.",
         "Mert and Ali sit on the old stone wall of the castle; Ali presses send on his phone and lets out a long breath; Mert places the cobalt "
         "tile seal on the stone between them and they both look at it.",
         [("ali", "Yüz yirmi bin gitti. Toplam üç yüz elli bin.", "relieved"),
          ("mert", "Yarıya yaklaştık Ali. Ve artık bir markamız var.", "proud")],
         "slow push-in from the tower toward them",
         t=T("borc", 120000, "4. taksit: Cemil Bey (Ege sezonu sonu)")),
       S("20:30 akşam", "kale", ["mert", "ali", "~cemil"], "Sesli Mesaj",
         "Cemil Bey bu kez sesli mesaj bırakır. Kutuları görmüştür.",
         "Ali holds the phone between them with the speaker on; they both lean in and listen with closed mouths as the city lights come on below; "
         "at the end Mert slowly turns to Ali, astonished.",
         [("cemil", "Kutuları gördüm. Bir tane de bana ayırın. Parasını veririm.", "gruff, slow, from the phone speaker"),
          ("mert", "Cemil Abi müşterimiz oldu!", "astonished whisper")],
         "slow dolly-out revealing the lit city",
         t=[T("konaklama", 1200, "Otel, 1 gece"), T("ulasim", 1000, "Yakıt: Kütahya-Bilecik")],
         kurgu="Sezon sonu kartı (kurguda): SEZON 4 BİTTİ · 8 İL · 4. TAKSİT ÖDENDİ · 320 KUTU"),
   ],
   misafir={"ciniusta": ("HÜSNÜ USTA", "HÜSNÜ, a 66-year-old Turkish tile master, thin, a white goatee, round glasses, a blue work smock with "
                         "paint spots", "elderly male voice, calm master, Kütahya Turkish"),
            "dukkan": ("DÜKKÂN SAHİBİ", "SHOP OWNER, a 48-year-old Turkish woman, short silver hair, a turquoise scarf", "adult female voice")},
   ay=AY, hava="ılık", urun="Kütahya çinisi ve porseleni, Kütahya Kalesi, Aizanoi",
   sponsor="Çini, porselen ya da el sanatları alanında",
   kapak=("cini", ["mert", "ali", "ciniusta"], "Mert holds up a small round hand-painted cobalt-blue tile seal like a medal, the tile master and "
          "Ali smiling beside him, shelves of blue tiles behind", "Çini mührü madalya gibi tutan Mert."),
   yakinda=("kale", ["mert", "ali"], "Two silhouettes on an old castle wall at sunset with a small glowing blue tile between them on the stone, "
            "the city below in blue dusk", "Kale duvarında aralarında parlayan küçük mavi bir çini."),
   tiktok="Sezon 4 finali: çiniden mühür, 200 kutu ve 120.000 TL 🔵 #JozhStudios",
   ig=("Ege bitti! 🫒 Kütahya'da Hüsnü Usta kutumuz için çiniden, yazısız bir mühür tasarladı: harita ve lale. 🔵\n\n"
       "İkinci seri 200 kutu tükendi, dördüncü taksit gitti: 120.000 TL. Toplam ödenen: 350.000 TL.\n\n"
       "Ve Cemil Abi sesli mesaj bıraktı: 'Bir kutu da bana ayırın.' 😳 Kasa: {KASA}. Sezon 5: Marmara!"),
   tags=["#Kütahya", "#Çini", "#SezonFinali"],
   son="Cemil Bey bir kutu ister. Sırada büyük pazar: Marmara.",
   teaser="Kobalt mavisi bir mühür, iki yüz kutu ve Cemil Bey'den bir sipariş. Bölüm 45: Kütahya, sezon finali. Pek yakında.")
