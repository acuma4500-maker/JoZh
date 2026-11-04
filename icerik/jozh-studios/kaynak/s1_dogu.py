# -*- coding: utf-8 -*-
"""Sezon 1 · Dağların Pazarı · Doğu Anadolu (Bölüm 7-20). Haziran.
Rota: Malatya → Elazığ → Tunceli → Erzincan → Erzurum → Ardahan → Kars → Iğdır → Ağrı → Van → Hakkari → (Van feribotu) Bitlis → Muş → Bingöl
Ulaşım: şehirler arası otobüs, dolmuş, Keban Baraj Gölü'nde Pertek feribotu, Van Gölü'nde Van-Tatvan feribotu. Mallar sırt çantası, koli ve kargoyla."""
from ortak import EP, S, T, U

AY = "Haziran"
OTOBUS = ("the interior of a modern intercity coach bus in Turkey: two rows of blue fabric seats, large side windows, small seat-back "
          "screens switched off, overhead luggage racks")

# ======================================================================= 7 MALATYA
EP(7, "Malatya", "Kayısının Başkenti",
   "Yolculuk başlıyor: annenin kahvaltısı, 150 kilo kayısı, Arslantepe ve otogarda beklenmedik bir veda.",
   "Hatice oğlu ve Ali için veda kahvaltısı hazırlar, yanlarına kayısı reçeli koyar. Ramazan Amca 150 kilo gün kurusu kayısıyı 'yolunuz "
   "uzun' diyerek 235'ten verir. Bahçede kayısının nasıl kurutulduğunu, Arslantepe'de 5.000 yıl önce burada saray ve kılıç yapıldığını "
   "görürler. Akşam elli paket takipçilere satılır. Otogarda Elazığ otobüsünü beklerken Cemil Bey gelir ve senedin bir kopyasını Ali'nin "
   "eline tutuşturur.",
   {"annev": ("Hatice'nin evi, mutfak", "Hatice's modest Malatya home kitchen in the morning: a small table set with a traditional Turkish "
              "breakfast, white cheese, olives, glass jars of homemade apricot jam, a teapot, lace curtains and a window to a small garden"),
    "pazar": ("Malatya Kayısı Pazarı", "the Malatya apricot market: long rows of covered stalls with open sacks and wooden crates of sun-dried "
              "golden and dark brown apricots, hanging scales and a corrugated metal roof letting in strips of sunlight"),
    "bahce": ("Kayısı bahçesi", "a large apricot orchard on the outskirts of Malatya: rows of apricot trees heavy with orange fruit, apricots "
              "drying on white cloths spread over the ground, dry brown hills on the horizon"),
    "arslan": ("Arslantepe Höyüğü", "the Arslantepe archaeological mound near Malatya: excavated ancient mudbrick walls and rooms under a "
               "large modern protective roof, wooden walkways, information panels without readable text, poplar trees around"),
    "ev": ("Ev, salon", "their small apartment living room in Malatya, now full of packed cardboard boxes of dried apricots, a kitchen "
           "scale on the coffee table, the grey sofa and a window at dusk"),
    "otogar": ("Malatya Otogarı", "the Malatya intercity bus terminal at night: a wide concrete platform with numbered bays, a modern coach "
               "with its luggage hatch open, bright overhead lights and a few distant travelers")},
   [
       S("08:00 iç-gündüz", "annev", ["mert", "ali", "hatice"], "Veda Kahvaltısı",
         "Hatice veda kahvaltısı hazırlamış. Yolculuk için iki kavanoz kayısı reçeli verir ve tek bir şey ister: her akşam aramalarını.",
         "Hatice places two jars of apricot jam into Mert's hands across the breakfast table; Ali pours tea for everyone; Mert stands, walks "
         "around the table and hugs his mother tightly.",
         [("hatice", "Her akşam arayacaksın. Üç ayda bir değil, her akşam.", "tender, firm"),
          ("mert", "Söz anne. Döndüğümde borç da bitmiş olacak.", "emotional, promising")],
         "slow dolly-in from the doorway to a three-shot"),
       S("10:00 sabah", "pazar", ["mert", "ali", "ramazan"], "150 Kilo",
         "Ramazan Amca yolculuğu duymuş; 150 kilo gün kurusu kayısıyı 'yolunuz uzun' diyerek 235'ten verir.",
         "Ramazan stacks three heavy sacks of dried apricots onto a hand trolley and pats them; Ali counts banknotes onto the stall counter while "
         "Mert ties the sacks closed with string.",
         [("ramazan", "Bu sefer iki yüz otuz beş. Yolunuz uzun, ilk satış bereketli olsun.", "warm, fatherly"),
          ("ali", "Allah razı olsun Ramazan Amca.", "grateful")],
         "static medium three-shot, slight push-in on the sacks",
         t=U(150, "kg", 235, "alis", "Gün kurusu Malatya kayısısı ({adet} kg x {fiyat} TL)")),
       S("12:10 öğle", "bahce", ["mert", "ali"], "Güneşte Kurumak",
         "Bahçede kayısıların beyaz bezler üstünde nasıl kurutulduğunu görürler. Ali kayısının Malatya için önemini anlatır.",
         "Mert crouches beside apricots drying on a white cloth and turns one over between two fingers; Ali walks under the trees, reaches up "
         "and gently touches a branch heavy with orange fruit.",
         [("ali", "Dünyadaki kuru kayısının büyük kısmı bu topraklardan çıkıyor.", "impressed"),
          ("mert", "Biz de dünyaya satacağız o zaman.", "grinning")],
         "slow tracking shot along the drying cloths"),
       S("14:30 ikindi", "arslan", ["mert", "ali"], "Beş Bin Yıllık Pazar",
         "Arslantepe Höyüğü'nde kerpiç duvarların arasında yürürler. Burada beş bin yıl önce bir saray, mühürler ve ilk kılıçlar varmış.",
         "Mert and Ali walk slowly along the wooden walkway above the excavated mudbrick rooms; Mert stops and points down at the ancient walls "
         "while Ali reads from his phone.",
         [("ali", "Beş bin yıl önce burada saray varmış. Mühürlerle ticaret yapıyorlarmış.", "fascinated"),
          ("mert", "Demek ki biz bu işe çok geç kalmışız.", "joking")],
         "slow crane-down from the protective roof to a medium two-shot"),
       S("19:00 iç-gece", "ev", ["mert", "ali"], "Elli Paket",
         "Akşam evde elli paket hazırlanıp takipçilere gönderilir. Ambalaj ve kargo kolisi 2.500 lira tutar.",
         "Ali tapes the last of a tall stack of cardboard boxes while Mert carries two boxes toward the door; Ali checks his phone, smiles and "
         "shows the screen to Mert.",
         [("ali", "Elli paket satıldı, hepsi kargoda.", "satisfied"),
          ("mert", "Kayısı daha yola çıkmadan kendini sattı!", "proud")],
         "static medium shot from the kitchen doorway",
         t=[U(50, "paket", 360, "satis", "Takipçi siparişi: 1 kg kayısı paketi ({adet} x {fiyat} TL)"),
            T("diger_gider", 2500, "Ambalaj, koli ve etiket")]),
       S("22:30 gece", "otogar", ["mert", "ali", "cemil"], "Senet",
         "Otogarda Elazığ otobüsüne binecekken Cemil Bey gelir. Senedin bir kopyasını Ali'ye verir ve tek söz söyler.",
         "Mert lifts a sack of apricots into the bus luggage hatch; Cemil Bey steps out of the shadows and holds out a folded paper to Ali, who "
         "takes it slowly; Mert turns around and freezes.",
         [("cemil", "Senedin kopyası. Bir taksit gecikirse, mahkemede görüşürüz.", "cold, quiet"),
          ("mert", "Gecikmeyecek Cemil Abi.", "tense, determined")],
         "slow push-in on Cemil Bey's hand and the paper",
         t=U(2, "bilet", 250, "ulasim", "Malatya-Elazığ otobüs bileti ({adet} x {fiyat} TL)")),
   ],
   misafir={"ramazan": ("RAMAZAN AMCA", "RAMAZAN, a 62-year-old Turkish apricot merchant, short and round, a sun-darkened smiling face, a white "
                        "short beard, wearing a flat grey cap, a cream shirt with rolled sleeves and a dark blue vest with a pen in its pocket",
                        "elderly male voice, warm husky baritone, cheerful Malatya Turkish")},
   ay=AY, hava="açık", urun="Kuru kayısı (gün kurusu), kayısı reçeli, pestil; Arslantepe Höyüğü (UNESCO)",
   sponsor="Kayısı üreticisi, kuruyemişçi ya da pestil-köme atölyesi olarak",
   kapak=("bahce", ["mert", "ali"], "Mert and Ali stand among apricot trees heavy with orange fruit, each holding a big handful of dried apricots "
          "toward the camera, backpacks on, bright morning light", "Kayısı ağaçlarının altında avuç dolusu kayısıyla Mert ve Ali."),
   yakinda=("otogar", ["cemil", "ali"], "At a night bus terminal, a man's hand in shadow holds out a folded paper toward Ali, whose face is lit "
            "by the cold platform light; a bus headlight glows behind", "Gece otogarda gölgeden uzanan bir el ve katlanmış bir senet."),
   tiktok="İlk durak Malatya: 150 kilo kayısıyla yola çıktık 🍑 #JozhStudios",
   ig=("Annemin kahvaltısı, Ramazan Amca'nın 150 kilosu ve 5.000 yıllık Arslantepe. 🍑 Malatya'dan yola çıktık!\n\n"
       "Elli paket daha otobüse binmeden satıldı. Ama otogarda Cemil Abi bizi bekliyordu, elinde senedin kopyası...\n\nKasa: {KASA}. Sizce ilk taksite yetişir mi?"),
   tags=["#Malatya", "#Arslantepe", "#Kayısı"],
   son="Otogarda Cemil Bey senedin kopyasını verir: 'Bir taksit gecikirse mahkemede görüşürüz.'",
   teaser="150 kilo kayısı, beş bin yıllık bir saray ve otogarda bir senet. Bölüm 7: Malatya. Pek yakında.")

# ======================================================================= 8 ELAZIĞ
EP(8, "Elazığ", "Harput'ta Misafirlik",
   "Harput'ta 'önce çay, sonra ticaret' dersi; orcik ustası ve kaybolan bir çuval.",
   "Sabah Harput'a çıkıp kaleyi ve şehri tepeden görürler. Mert hemen kayısı satmaya kalkar, ama bir Harputlu amca onları önce çaya oturtur: "
   "Harput'ta misafir alışverişten önce gelir. Aynı amcanın tanıştırdığı çarşıdaki kuruyemişçi 60 kilo kayısıyı alır. Öğlen Harput köftesi, "
   "ikindi orcik atölyesi: cevizin pekmezli bulamaca batırılıp ipte kurutulmasını izler ve 40 kilo orcik alırlar. Gece pansiyonda Ali "
   "çuvalları sayar: biri eksiktir.",
   {"harput": ("Harput Kalesi", "the hilltop of Harput above Elazığ: the old stone walls and towers of Harput Castle, a stone-paved path, "
               "a wide view over the city and plain below"),
    "cayhane": ("Harput'ta çay bahçesi", "a small shaded tea garden in Harput next to old stone houses: low wooden stools, a samovar, small "
                "tulip-shaped tea glasses on a tin tray, a big walnut tree"),
    "carsi": ("Elazığ çarşısı, kuruyemişçi", "a dried-fruit and nut shop in Elazığ's covered bazaar: wooden shelves of jars and sacks of "
              "walnuts, mulberries, apricots and orcik, a brass scale and warm hanging bulbs"),
    "lokanta": ("Esnaf lokantası", "a simple Elazığ tradesmen's restaurant: steel trays behind a glass counter, white tiled walls, small "
                "tables with paper covers"),
    "atolye": ("Orcik atölyesi", "a small family workshop in Elazığ where orcik is made: long strings of walnuts dipped in thick grape-molasses "
               "starch paste hang drying from wooden bars, a big copper cauldron, clean white walls"),
    "pansiyon": ("Pansiyon odası", "a simple guesthouse room in Elazığ at night: two single beds with white covers, cardboard boxes and two "
                 "sacks on the floor, a bedside lamp")},
   [
       S("08:40 sabah", "harput", ["mert", "ali"], "Harput'tan Şehre Bakış",
         "Elazığ'a sabah iner, dolmuşla Harput'a çıkarlar. Kale surlarından bütün şehir ayaklarının altındadır.",
         "Mert and Ali climb the last steps of the stone path to the castle wall and stop at the edge, catching their breath; Mert spreads his "
         "arms wide toward the view while Ali shades his eyes with one hand.",
         [("mert", "Elazığ ayaklarımızın altında Ali!", "exhilarated"),
          ("ali", "Kayısılar da otuz kilo sırtımızda.", "out of breath, smiling")],
         "slow crane-up from behind them revealing the plain"),
       S("09:30 sabah", "cayhane", ["mert", "ali", "harputlu"], "Önce Çay",
         "Mert kayısı paketlerini açmaya kalkınca Harputlu Nevzat Amca onları çaya oturtur: burada misafir alışverişten önce gelir.",
         "Mert opens a box of apricot packs on a stool; the old man gently closes the lid with one hand and slides two glasses of tea toward them "
         "with the other; Ali sits down at once, Mert sits more slowly.",
         [("harputlu", "Harput'ta önce çay içilir evlat, alışveriş sonra.", "kind, slow"),
          ("mert", "Peki amca, çay bizden değil ama.", "sheepish laugh")],
         "static medium three-shot at stool height"),
       S("11:30 öğle", "carsi", ["ali", "esnaf"], "Amcanın Tavsiyesi",
         "Nevzat Amca'nın tavsiyesiyle gittikleri çarşıdaki kuruyemişçi 60 kilo kayısıyı kilosu 300'den alır.",
         "The shopkeeper bites an apricot, nods and pours a sack onto the brass scale; Ali writes in his brown notebook and shakes the shopkeeper's "
         "hand across the counter.",
         [("esnaf", "Nevzat Amca yolladıysa malınız temizdir. Altmış kilo, üç yüzden.", "brisk, friendly"),
          ("ali", "Hayırlı işler. Malatya'nın en iyisi.", "polite")],
         "slow push-in over the counter",
         t=U(60, "kg", 300, "satis", "Kuru kayısı, Elazığ çarşısında toptan ({adet} kg x {fiyat} TL)")),
       S("13:00 iç-gündüz", "lokanta", ["mert", "ali"], "Harput Köftesi",
         "Öğle yemeğinde bulgurlu, içi dolgulu Harput köftesi yerler. Mert ikinci tabağı ister.",
         "Mert lifts a spoonful of Harput meatballs in broth and blows on it, eyes closed in pleasure; Ali laughs and pushes his own half-full bowl "
         "toward him.",
         [("mert", "Bu köfte borcu bile unutturur.", "blissful"),
          ("ali", "Unutturmasın. Hesabı sen ödüyorsun.", "teasing")],
         "static medium two-shot across the table",
         t=T("yemek", 600, "Öğle yemeği: Harput köftesi (2 kişi)")),
       S("16:00 ikindi", "atolye", ["mert", "ali", "usta"], "İpte Kuruyan Ceviz",
         "Orcik atölyesinde cevizlerin ipe dizilip pekmezli bulamaca batırıldığını izlerler. 40 kilo orcik alırlar.",
         "The workshop master dips a long string of walnuts into the copper cauldron of thick molasses paste and hangs it on a wooden bar; Mert "
         "touches a dried orcik and smells it while Ali counts money into the master's hand.",
         [("usta", "Orcik sabır işidir. Üç kez batırırsın, üç gün kurutursun.", "proud craftsman"),
          ("ali", "Kırk kilo alıyoruz usta.", "decisive")],
         "slow lateral dolly along the hanging strings",
         t=U(40, "kg", 380, "alis", "Elazığ orciği ({adet} kg x {fiyat} TL)")),
       S("22:00 iç-gece", "pansiyon", ["mert", "ali"], "Bir Çuval Eksik",
         "Gece pansiyonda Ali malları sayar. Bir kayısı çuvalı yoktur. Dolmuşta kalmış olmalı.",
         "Ali counts the sacks and boxes on the floor with his pen, stops, counts again and slowly looks up at Mert, who is lying on the bed; Mert "
         "sits bolt upright.",
         [("ali", "Mert... bir çuval eksik.", "alarmed whisper"),
          ("mert", "Dolmuş! Harput dolmuşunda kaldı!", "panicked")],
         "static high-angle shot from the corner of the room",
         t=[T("konaklama", 1200, "Pansiyon, 1 gece (2 kişi)"), U(2, "bilet", 200, "ulasim", "Elazığ-Pertek dolmuş ve feribot bileti ({adet} x {fiyat} TL)")]),
   ],
   misafir={"harputlu": ("NEVZAT AMCA", "NEVZAT, a 74-year-old Turkish man from Harput, thin, a white short beard, kind deep-set eyes, wearing a "
                         "grey wool vest over a white shirt and a black flat cap, holding prayer beads", "elderly male voice, slow, gentle Elazığ Turkish"),
            "esnaf": ("KURUYEMİŞÇİ", "SHOPKEEPER, a 50-year-old Turkish man, stocky, short grey hair, a thick black mustache, a beige shop coat",
                      "adult male voice, brisk and friendly, Elazığ Turkish"),
            "usta": ("ORCİK USTASI", "WORKSHOP MASTER, a 58-year-old Turkish woman, sturdy, rosy cheeks, a white cotton headscarf tied at the back, "
                     "a long brown apron over a floral dress, sleeves rolled up", "middle-aged female voice, proud and warm, Elazığ Turkish")},
   ay=AY, hava="açık", urun="Orcik (cevizli pekmez sucuğu), Harput köftesi, dut; Harput Kalesi, Hazar Gölü",
   sponsor="Orcik, kuruyemiş ya da yöresel gıda alanında",
   kapak=("atolye", ["mert", "ali"], "Mert and Ali stand between long hanging strings of orcik in the workshop, Mert biting one with a huge "
          "grin, Ali holding the brown notebook, warm window light", "Orcik dizilerinin arasında orcik ısıran Mert ve defterli Ali."),
   yakinda=("pansiyon", ["ali"], "Ali's worried face lit by a single bedside lamp, counting sacks on the floor, one empty space where a sack "
            "should be, long shadows", "Lamba ışığında çuvalları sayan Ali; bir çuvalın yeri boş."),
   tiktok="Harput'ta önce çay, sonra ticaret ☕ Ama bir çuval kayıp! #JozhStudios",
   ig=("Harput'ta Nevzat Amca bize ticaretin ilk kuralını öğretti: önce çay. ☕ Sonra 60 kilo kayısı sattık, orcik ustasından 40 kilo orcik aldık. "
       "Harput köftesi ise ayrı bir hikâye. 😋\n\nAma gece Ali çuvalları saydı... biri eksik. Kasa: {KASA}"),
   tags=["#Elazığ", "#Harput", "#Orcik"],
   son="Bir kayısı çuvalı Harput dolmuşunda unutulmuştur.",
   teaser="Önce çay, sonra ticaret... ve kaybolan bir çuval. Bölüm 8: Elazığ. Pek yakında.")

# ======================================================================= 9 TUNCELİ
EP(9, "Tunceli", "Munzur'un Sarımsağı",
   "Feribotta kayıp çuval bulunur; Munzur Vadisi'nde Tunceli sarımsağının peşine düşerler.",
   "Sabah Keban Baraj Gölü'ndeki Pertek feribotunda dün akşamki dolmuş şoförü çuvalı getirir: 'Emanet bende kalmaz.' Tunceli'de çarşıda orcik "
   "satarlar, kalan kayısı takipçi siparişleriyle gider. Öğlen tereyağlı ve sarımsaklı zerefet yerler. Munzur Vadisi'nde tek dişli Tunceli "
   "sarımsağını yetiştiren Hıdır Amca'yı bulur, 25 kilo alırlar. Akşam Munzur gözelerinde Ali'nin telefonuna Erzincan'dan bir mesaj gelir.",
   {"feribot": ("Pertek feribotu", "the deck of a small car ferry crossing the wide blue Keban Dam Lake toward Pertek: white metal railings, "
                "a few parked cars, the stone Pertek Castle on a rocky hill across the water, bare brown hills"),
    "carsi": ("Tunceli çarşısı", "a small shopping street in central Tunceli: low buildings, a grocer's stall with crates under an awning, "
              "green mountains rising right behind the town"),
    "lokanta": ("Ev yemekleri lokantası", "a small family-run restaurant in Tunceli with wooden tables, a window onto the mountains and a "
                "copper tray on the wall"),
    "tarla": ("Ovacık, sarımsak tarlası", "a mountain garlic field in the Munzur valley near Ovacık: rows of tall green garlic stalks, freshly "
              "pulled garlic bulbs drying in bundles, snow-capped Munzur mountains behind"),
    "goze": ("Munzur gözeleri", "the Munzur springs: clear ice-cold water gushing from mossy rocks into a turquoise stream, green trees "
             "and steep mountain slopes")},
   [
       S("08:20 sabah", "feribot", ["mert", "ali", "sofor"], "Emanet",
         "Pertek feribotunda dünkü dolmuş şoförü çuvalı getirir. Mert sevinçten şoföre sarılır.",
         "The minibus driver walks across the ferry deck carrying a sack of apricots on his shoulder and sets it down in front of them; Mert "
         "hugs him with both arms, Ali shakes his hand with both hands.",
         [("sofor", "Emanet bende kalmaz evlat. Dün akşamdan beri arıyorum sizi.", "warm, gruff"),
          ("mert", "Abi sen olmasan kasa kırk kilo eksikti!", "relieved, loud")],
         "slow dolly-in along the ferry railing, Pertek Castle in the background"),
       S("10:30 sabah", "carsi", ["ali", "manav"], "Orcik Tunceli'de",
         "Tunceli çarşısında bir manav orcikleri tadar ve 20 kiloyu alır.",
         "The grocer cuts a piece of orcik with a pocket knife and tastes it, then nods and lifts a box from Ali's hands onto his counter.",
         [("manav", "Elazığ orciği mi? Yirmi kilo bırak, akşama kalmaz.", "quick, friendly"),
          ("ali", "Kilosu dört yüz seksen, hayırlı satışlar.", "polite")],
         "static medium two-shot at the stall",
         t=U(20, "kg", 480, "satis", "Elazığ orciği, Tunceli çarşısında ({adet} kg x {fiyat} TL)")),
       S("12:30 iç-gündüz", "lokanta", ["mert", "ali"], "Zerefet",
         "Öğle yemeğinde tereyağlı, sarımsaklı yöresel hamur yemeği zerefeti yerler. Bu sırada kurtarılan çuvaldaki 40 kilo kayısı siparişlerle satılır.",
         "Mert eats steaming buttery pasta with a spoon while Ali scrolls on his phone; Ali turns the phone to Mert, who gives a thumbs-up with "
         "his mouth full.",
         [("ali", "Kurtardığımız çuval da bitti: kırk paket sipariş!", "happy"),
          ("mert", "Bu sarımsak kokusu da satılır mı acaba?", "eating, curious")],
         "static medium two-shot across the table",
         t=[U(40, "paket", 360, "satis", "Takipçi siparişi: 1 kg kayısı paketi ({adet} x {fiyat} TL)"), T("yemek", 500, "Öğle yemeği: zerefet (2 kişi)")]),
       S("15:30 ikindi", "tarla", ["mert", "ali", "hidir"], "Tek Dişli Sarımsak",
         "Ovacık'ta Hıdır Amca tek dişli Tunceli sarımsağını gösterir: dağda kendiliğinden yetişen türden ıslah edilmiş, yalnızca bu topraklarda olur.",
         "Hıdır pulls a large single-clove garlic bulb from the soil and places it in Mert's open palm; Mert holds it up in awe, Ali kneels to "
         "look at the rows of green stalks.",
         [("hidir", "Bunun dişi tektir. Munzur'un suyuyla büyür, başka yerde olmaz.", "proud, slow"),
          ("mert", "Amca bu sarımsak değil, hazine!", "amazed")],
         "slow push-in from wide field to the bulb in Mert's hand"),
       S("17:00 ikindi", "tarla", ["ali", "hidir"], "Yirmi Beş Kilo",
         "Hıdır Amca'dan 25 kilo sarımsak alırlar. Ali pazarlık yapmaz: 'Bu emeğe pazarlık olmaz.'",
         "Hıdır ties bundles of garlic into a mesh sack and lifts it onto a field scale; Ali counts banknotes into his weathered hand and both "
         "nod respectfully.",
         [("hidir", "Kilosu yedi yüz. Pazarlık edersen kızmam.", "teasing"),
          ("ali", "Bu emeğe pazarlık olmaz amca.", "respectful")],
         "static medium two-shot at the scale",
         t=U(25, "kg", 700, "alis", "Tunceli sarımsağı, üreticiden ({adet} kg x {fiyat} TL)")),
       S("19:30 gün batımı", "goze", ["mert", "ali"], "Erzincan'dan Mesaj",
         "Munzur gözelerinde suya ellerini sokarlar. Ali'nin telefonuna bir mesaj düşer: Erzincan'dan bir lokanta sarımsak istiyor ama bir şartı var.",
         "Mert dips both hands into the ice-cold spring water and gasps; Ali's phone buzzes, he reads it and raises his eyebrows, then holds the "
         "phone out to Mert.",
         [("ali", "Erzincan'dan bir lokanta sarımsak istiyor. Ama yarın sabah yedide.", "surprised"),
          ("mert", "Yedide mi? Otobüs altıda kalkıyor!", "shocked")],
         "slow dolly-in over the stream",
         t=[T("konaklama", 1000, "Pansiyon, 1 gece"), U(2, "bilet", 300, "ulasim", "Tunceli-Erzincan sabah otobüsü ({adet} x {fiyat} TL)")]),
   ],
   misafir={"sofor": ("DOLMUŞ ŞOFÖRÜ", "MINIBUS DRIVER, a 48-year-old Turkish man, broad shoulders, a round face with a black mustache, wearing a "
                      "light-blue short-sleeved shirt and dark trousers", "adult male voice, warm gruff Elazığ Turkish"),
            "manav": ("MANAV", "GROCER, a 40-year-old Turkish man, slim, short black beard, a dark green vest over a grey t-shirt",
                      "adult male voice, quick and friendly Turkish"),
            "hidir": ("HIDIR AMCA", "HIDIR, a 66-year-old Turkish farmer, lean and sun-tanned, a long white mustache, deep wrinkles, wearing a "
                      "flat brown cap, a faded checked shirt and dusty trousers", "elderly male voice, slow, proud, Eastern Anatolian Turkish")},
   ay=AY, hava="açık", urun="Tunceli sarımsağı (tek dişli), dağ balı, zerefet; Munzur Vadisi, Pertek Kalesi",
   sponsor="Tunceli sarımsağı, bal ya da yöresel ürün alanında",
   kapak=("tarla", ["mert", "ali", "hidir"], "Mert holds a giant single-clove garlic bulb up to the camera like a trophy, Ali and Hıdır laugh "
          "beside him, snow-capped mountains behind", "Dev tek dişli sarımsağı kupa gibi tutan Mert."),
   yakinda=("feribot", ["mert", "ali"], "Two silhouettes on a ferry deck at dawn on a vast lake, a lone figure in the distance carrying a sack "
            "on his shoulder toward them, castle on the hill", "Şafakta feribot güvertesinde iki silüet ve sırtında çuvalla yaklaşan biri."),
   tiktok="Kaybolan çuval geri geldi + tek dişli sarımsak 🧄 #JozhStudios",
   ig=("Pertek feribotunda dolmuş şoförü kayıp çuvalımızı getirdi: 'Emanet bende kalmaz.' 🙏\n\n"
       "Munzur Vadisi'nde Hıdır Amca'nın tek dişli Tunceli sarımsağını gördük ve 25 kilo aldık. Zerefet ise unutulmaz. 🧄\n\n"
       "Ama Erzincan'dan bir sipariş geldi: yarın sabah yedide! Yetişir miyiz? Kasa: {KASA}"),
   tags=["#Tunceli", "#Munzur", "#Sarımsak"],
   son="Erzincan'dan bir lokanta sarımsak istiyor: yarın sabah yedide. Otobüs altıda kalkıyor.",
   teaser="Kaybolan çuval, tek dişli bir hazine ve imkânsız bir sipariş saati. Bölüm 9: Tunceli. Pek yakında.")

# ======================================================================= 10 ERZİNCAN
EP(10, "Erzincan", "Tulum ve Şelale",
   "Sabah yedide sarımsak teslimatı için koşu; tulum peyniri ustası ve Girlevik Şelalesi.",
   "Otobüs Erzincan'a 06:50'de girer; iki arkadaş sarımsak çuvalıyla lokantaya koşar ve teslimata dakikası dakikasına yetişir. "
   "Lokantacı kalan orcikleri de alır. Bir köy evinde tulum peynirinin keçi derisinde nasıl olgunlaştığını öğrenirler ve 40 kilo alırlar. "
   "Öğleden sonra Girlevik Şelalesi'nde serinlerler. Akşam Ali hesap yaparken Mert'in yine bir 'büyük fikri' vardır: Erzurum'da tulum "
   "peynirini kebapçılara satmak.",
   {"sokak": ("Erzincan, sabah caddesi", "a wide quiet avenue in central Erzincan at early morning: modern low-rise buildings, tall poplar "
              "trees, a closed bakery with its lights on, mountains behind"),
    "lokanta": ("Lokanta mutfağı", "the open kitchen of a traditional Erzincan restaurant in the early morning: steel counters, big pots, "
                "a tiled wall, sunlight through a high window"),
    "koy": ("Köy evi, peynir odası", "a cool stone cellar of a village house near Erzincan where tulum cheese ripens: goat-skin and cloth "
            "cheese sacks on wooden shelves, a wooden table, a small window"),
    "selale": ("Girlevik Şelalesi", "the Girlevik waterfall near Erzincan: white water cascading over mossy travertine rocks into green "
               "pools, lush trees, a wooden footbridge"),
    "pansiyon": ("Pansiyon odası", "a simple Erzincan guesthouse room at night: two beds, a small desk with a lamp, cheese boxes stacked "
                 "neatly by the wall")},
   [
       S("06:52 şafak", "sokak", ["mert", "ali"], "Yedi Olmadan",
         "Otobüs 06:50'de girer. Sarımsak çuvalını aralarında taşıyarak caddede koşarlar.",
         "Mert and Ali run along the empty avenue carrying a heavy mesh sack of garlic between them, each holding one side; Ali checks his watch "
         "while running and Mert pulls ahead.",
         [("ali", "İki dakika kaldı!", "breathless"),
          ("mert", "Sarımsak kokusu bizden önce varır!", "running, laughing")],
         "fast tracking shot in front of them, moving backward",
         kurgu="Ekrana yazı ekle (kurguda): 06:58"),
       S("06:59 iç-gündüz", "lokanta", ["mert", "ali", "lokantaci"], "Tam Yedi",
         "Lokantacı Bülent Usta saate bakar, gülümser: 06:59. On kilo sarımsağı ve kalan yirmi kilo orciği alır.",
         "Mert drops the garlic sack onto the steel counter, panting; the chef glances at the wall clock, laughs, and pulls a thick envelope from "
         "his apron pocket.",
         [("lokantaci", "Bir dakika erkencisiniz. Kalan orcikleri de bırakın.", "impressed, laughing"),
          ("ali", "Sarımsak on kilo, orcik yirmi kilo.", "out of breath")],
         "static medium three-shot across the counter",
         t=[U(10, "kg", 1000, "satis", "Tunceli sarımsağı, lokantaya ({adet} kg x {fiyat} TL)"),
            U(20, "kg", 470, "satis", "Elazığ orciği, lokantaya (20 kg x 470 TL)")]),
       S("11:00 iç-gündüz", "koy", ["mert", "ali", "nadide"], "Deride Olgunlaşan Peynir",
         "Bir köy evinde Nadide Teyze tulum peynirinin keçi derisinde aylarca olgunlaştığını anlatır. Mert'e bir parça tattırır.",
         "Nadide opens a cloth-wrapped cheese sack and crumbles a piece of white tulum cheese into Mert's palm; Mert tastes it and closes his eyes, "
         "Ali leans over the shelf to look at the sacks.",
         [("nadide", "Bu peynir deride uyur, yayla otunu rüyasında görür.", "warm, poetic"),
          ("mert", "Teyze, bu rüyayı Erzurum'a götürmek istiyoruz.", "charmed")],
         "slow dolly-in between the shelves"),
       S("12:00 iç-gündüz", "koy", ["ali", "nadide"], "Kırk Kilo Tulum",
         "Kırk kilo tulum peyniri alırlar. Nadide Teyze kalıpları bezle sarıp koliye koyar.",
         "Nadide wraps cheese blocks in white cloth and lays them into a cardboard box; Ali places folded banknotes on the wooden table and she "
         "pats his hand.",
         [("nadide", "Kilosu beş yüz yirmi. Serin yerde taşıyın.", "motherly"),
          ("ali", "Gözümüz gibi bakacağız teyze.", "earnest")],
         "static medium two-shot at the table",
         t=U(40, "kg", 520, "alis", "Erzincan tulum peyniri ({adet} kg x {fiyat} TL)")),
       S("15:30 ikindi", "selale", ["mert", "ali"], "Girlevik",
         "Girlevik Şelalesi'nde ayaklarını soğuk suya sokarlar. Mert'in aklı yine işte.",
         "Mert and Ali sit on a flat rock with their trouser legs rolled up and their feet in the cold pool below the waterfall; Mert splashes "
         "Ali, who flinches and laughs.",
         [("ali", "Beş dakika iş konuşmayalım.", "relaxed"),
          ("mert", "Tamam. Dört dakika sonra bir fikrim var.", "grinning")],
         "slow crane-down from the waterfall to the two of them",
         t=T("yemek", 700, "Öğle yemeği ve şelalede çay")),
       S("21:30 iç-gece", "pansiyon", ["mert", "ali"], "Kebapçılara Peynir",
         "Gece Ali günü deftere yazar. Mert'in fikri: tulum peynirini Erzurum'da kebapçılara satmak. Ali tereddütlü.",
         "Ali writes in the brown notebook at the desk; Mert stands behind him and taps the stacked cheese boxes; Ali turns around slowly with a "
         "skeptical raised eyebrow.",
         [("mert", "Erzurum'da her kebapçının masasında peynir var. Hepsine satarız!", "excited"),
          ("ali", "Her kebapçının zaten peynircisi var Mert.", "skeptical")],
         "static medium shot from the doorway",
         t=[T("konaklama", 1100, "Pansiyon, 1 gece"), U(2, "bilet", 400, "ulasim", "Erzincan-Erzurum otobüsü ({adet} x {fiyat} TL)")]),
   ],
   misafir={"lokantaci": ("BÜLENT USTA", "BÜLENT, a 52-year-old Turkish chef, heavy-set, bald head, a thick grey mustache, white chef jacket and "
                          "white apron", "adult male voice, deep, jovial Erzincan Turkish"),
            "nadide": ("NADİDE TEYZE", "NADİDE, a 68-year-old Turkish village woman, small and sturdy, a lined smiling face, a white headscarf "
                       "with a lace edge, a dark green knitted vest over a long floral dress", "elderly female voice, warm, sing-song Eastern Turkish")},
   ay=AY, hava="serin", urun="Tulum peyniri, Cimin üzümü, Kemaliye; Girlevik Şelalesi",
   sponsor="Tulum peyniri ya da süt ürünleri alanında",
   kapak=("selale", ["mert", "ali"], "Mert and Ali sit laughing on a rock below the white Girlevik waterfall, Mert splashing water at Ali, "
          "lush green light", "Girlevik Şelalesi'nin önünde su sıçratıp gülen Mert ve Ali."),
   yakinda=("sokak", ["mert", "ali"], "Two figures running down an empty dawn avenue carrying a heavy sack between them, long shadows, a big "
            "clock face glowing on a building", "Şafakta boş caddede çuval taşıyarak koşan iki figür."),
   tiktok="Sabah 7'de teslimat yarışı + deride olgunlaşan peynir 🧀 #JozhStudios",
   ig=("Otobüs 06:50'de indi, teslimat 07:00'de. Sarımsak çuvalıyla koştuk, 06:59'da lokantadaydık! 🏃‍♂️🧄\n\n"
       "Nadide Teyze'den deride olgunlaşan Erzincan tulum peyniri aldık, Girlevik'te ayaklarımızı soğuk suya soktuk.\n\n"
       "Mert'in yeni fikri: Erzurum kebapçılarına peynir satmak. Ali'ye göre kötü fikir. Siz ne dersiniz? Kasa: {KASA}"),
   tags=["#Erzincan", "#TulumPeyniri", "#Girlevik"],
   son="Mert, tulum peynirini Erzurum'da kebapçılara satmak istiyor. Ali'ye göre her kebapçının zaten peynircisi var.",
   teaser="Bir dakika kala teslimat, deride uyuyan peynir ve şelale. Bölüm 10: Erzincan. Pek yakında.")

# ======================================================================= 11 ERZURUM
EP(11, "Erzurum", "Cağ Kebabı ve Oltu Taşı",
   "Mert'in kebapçı planı çuvallar ama cağ ustası yol gösterir; Taşhan'da oltu taşı pazarlığı.",
   "Mert sabah erkenden kebapçıları tek tek gezer; hepsinin peynircisi vardır. Öğlen cağ kebabı ustası Sabri Usta yarı yarıya güler, sonra "
   "yol gösterir: 'Peynirciye değil, gurbetçiye sat.' Ali tulum peynirini memleket özlemi çeken takipçilere ve bir şarküteriye satar. "
   "Çifte Minareli Medrese'nin önünde Mert ilk kez Ali'ye hak verir. Taşhan'da oltu taşı ustasından el işi tespih alırlar. "
   "Gece Ali'nin telefonuna sarımsak siparişi yağar.",
   {"cadde": ("Erzurum, Cumhuriyet Caddesi", "a busy stone-paved pedestrian street in central Erzurum in the morning: old stone buildings, "
              "kebab shop fronts with glass windows, a few distant pedestrians"),
    "cag": ("Cağ kebapçısı", "a traditional Erzurum cağ kebab restaurant: a horizontal rotating spit of layered lamb in front of a wood fire, "
            "long metal skewers, tiled walls, simple tables"),
    "medrese": ("Çifte Minareli Medrese", "the 13th-century Double Minaret Madrasa in Erzurum: a tall carved stone portal flanked by two "
                "fluted brick minarets with turquoise tiles, a wide stone square in front"),
    "tashan": ("Taşhan, oltu taşı çarşısı", "the inside of the old stone Taşhan (Rüstem Paşa Bedesteni) in Erzurum: small stone-arched shops "
               "with glass cases full of black oltu-stone prayer beads with silver details, a craftsman's lathe"),
    "otel": ("Otel odası", "a simple hotel room in Erzurum at night: two beds, a window with the city lights and dark mountains beyond")},
   [
       S("08:30 sabah", "cadde", ["mert"], "Her Kebapçının Peynircisi Var",
         "Mert peynir kolisiyle kebapçıları tek tek gezer. Üçüncü dükkândan da eli boş çıkar.",
         "Mert walks out of a kebab shop door holding a cardboard box of cheese, shakes his head, looks at the next shop sign and walks in again "
         "with a forced smile; a moment later he comes back out, still holding the box.",
         [("mert", "Üçüncü kebapçı... üçünün de peynircisi var.", "deflated, to himself")],
         "static wide shot across the street, slow pan following Mert"),
       S("12:00 öğle", "cag", ["mert", "ali", "sabri"], "Cağ Ustasının Dersi",
         "Cağ kebabı ustası Sabri Usta Mert'in hikâyesine güler, sonra yol gösterir: peyniri gurbetteki Erzurumlulara satın.",
         "Sabri slides a long skewer of thin lamb slices off the rotating spit onto a plate and places it in front of Mert; Ali takes notes; "
         "Sabri points the empty skewer at Mert while talking.",
         [("sabri", "Peynirciye peynir satılmaz. Gurbetteki hemşehriye satılır, o memleketi özler.", "wise, amused"),
          ("ali", "Takipçilerimizin çoğu zaten gurbette.", "realizing")],
         "slow push-in past the spit to the table",
         t=T("yemek", 800, "Cağ kebabı (2 kişi)")),
       S("14:00 öğle", "medrese", ["mert", "ali"], "Ali Haklıydı",
         "Çifte Minareli Medrese'nin önünde Ali tulum peynirinin satıldığını gösterir: 25 kilo şarküteriye ve gurbetçi siparişlerine. Mert ilk kez hak verir.",
         "Ali holds his phone toward Mert in front of the carved stone portal; Mert reads it, exhales, then bows his head theatrically toward Ali "
         "with one hand on his chest.",
         [("ali", "Yirmi beş kilo peynir sattık. Gurbetçiler ve bir şarküteri.", "calm, satisfied"),
          ("mert", "Haklıydın. Bunu bir kere söyleyeceğim, kaydet.", "theatrical, humble")],
         "slow crane-up from their faces to the twin minarets",
         t=U(25, "kg", 650, "satis", "Erzincan tulum peyniri, şarküteri ve gurbetçi siparişleri ({adet} kg x {fiyat} TL)")),
       S("16:30 ikindi", "tashan", ["mert", "ali", "oltucu"], "Kara Taş",
         "Taşhan'da oltu taşı ustası Kâzım Usta, Oltu'dan çıkan kara taşın torna tezgâhında nasıl tespihe dönüştüğünü gösterir.",
         "Kâzım holds a raw black oltu stone up to the light, then shapes a bead on his small lathe; Mert and Ali lean in close to watch the "
         "black stone turn glossy.",
         [("oltucu", "Oltu taşı ele alındıkça parlar. Emek gibi.", "proud, quiet"),
          ("mert", "Bundan on beş tane alsak, ustam?", "eager")],
         "slow push-in to a close-up of the lathe and bead"),
       S("17:00 ikindi", "tashan", ["ali", "oltucu"], "On Beş Tespih",
         "On beş el işi oltu taşı tespih alırlar. Bu kez pazarlığı Ali yapar ve küçük bir indirim alır.",
         "Kâzım lays fifteen black prayer-bead strings on a velvet cloth; Ali counts them one by one, writes a number in his notebook and turns "
         "it toward Kâzım, who smiles and nods.",
         [("ali", "On beş tane, bin iki yüzden olur mu ustam?", "polite, firm"),
          ("oltucu", "Gençsiniz, yolunuz açık olsun. Olur.", "kind")],
         "static medium two-shot over the glass case",
         t=U(15, "tespih", 1200, "alis", "El işi oltu taşı tespih ({adet} x {fiyat} TL)")),
       S("22:00 iç-gece", "otel", ["mert", "ali"], "Sarımsak Yağmuru",
         "Gece Ali'nin telefonu susmaz: Tunceli sarımsağı videosu yayılmış, kalan 15 kilo dakikalar içinde satılır.",
         "Ali sits on the bed as his phone buzzes non-stop in his hand; Mert jumps onto the other bed, grabs the phone, reads and shouts with "
         "joy, then covers his mouth to stay quiet.",
         [("ali", "Kalan on beş kilo sarımsak... on dakikada bitti.", "stunned"),
          ("mert", "Hıdır Amca'ya bir çiçek göndermemiz lazım!", "ecstatic whisper")],
         "static medium two-shot from the window",
         t=[U(15, "kg", 1000, "satis", "Tunceli sarımsağı, takipçi siparişi ({adet} kg x {fiyat} TL)"), T("konaklama", 1200, "Otel, 1 gece"),
            U(2, "bilet", 400, "ulasim", "Erzurum-Ardahan otobüsü ({adet} x {fiyat} TL)")]),
   ],
   misafir={"sabri": ("SABRİ USTA", "SABRİ, a 60-year-old Turkish cağ kebab master, big and broad, a red face, a thick grey mustache, a white cap "
                      "and white apron, sleeves rolled up", "mature male voice, deep booming Erzurum Turkish, humorous"),
            "oltucu": ("KÂZIM USTA", "KÂZIM, a 57-year-old Turkish stone craftsman, slim, short grey beard, reading glasses on a cord, a brown "
                       "work apron over a checked shirt", "mature male voice, quiet and precise Erzurum Turkish")},
   ay=AY, hava="serin", urun="Cağ kebabı, oltu taşı, civil ve göğermiş peynir; Çifte Minareli Medrese, Palandöken",
   sponsor="Oltu taşı, cağ kebabı ya da yöresel gıda alanında",
   kapak=("cag", ["mert", "ali", "sabri"], "Sabri Usta holds a long skewer of cağ kebab toward Mert, who leans in with huge eyes, Ali laughing, "
          "the glowing wood fire and rotating spit behind them", "Cağ kebabı şişini uzatan usta, kocaman gözlerle bakan Mert."),
   yakinda=("tashan", ["mert"], "Mert's face reflected in a dark glass case full of glossy black prayer beads, a single warm lamp, the stone "
            "arches fading into darkness", "Kara oltu taşlarının camında yansıyan bir yüz."),
   tiktok="Erzurum'da kebapçıya peynir satmaya çalıştım 😅 #JozhStudios",
   ig=("Mert'in kebapçı planı: 3 dükkân, 3 ret. 😅 Cağ ustası Sabri Usta güldü ve yolu gösterdi: 'Peynirciye değil, memleketini özleyen hemşehriye sat.'\n\n"
       "Taşhan'da Kâzım Usta'nın oltu taşı tespihlerini gördük, pazarlığı bu kez Ali yaptı. Gece de sarımsak 10 dakikada bitti! 🧄\n\nKasa: {KASA}"),
   tags=["#Erzurum", "#CağKebabı", "#OltuTaşı"],
   son="Kalan sarımsak on dakikada satılır. Sırada Ardahan ve sınır yaylaları var.",
   teaser="Üç kebapçı, üç ret ve bir ustanın tek cümlesi. Bölüm 11: Erzurum. Pek yakında.")

# ======================================================================= 12 ARDAHAN
EP(12, "Ardahan", "Çıldır'da Kaşar",
   "Çıldır Gölü kıyısında yayla kaşarı; Damal'daki dağ gölgesini görmek için zamana karşı yarış.",
   "Ardahan'a serin bir sabah varırlar. Kalan tulum peynirini bir markete, oltu tespihlerin bir kısmını takipçilere satarlar. Çıldır Gölü "
   "kıyısındaki küçük bir mandırada yayla sütünden kaşar yapılışını izler, 50 kilo kaşar alırlar. Akşamüstü Damal'da her haziranın sonunda "
   "dağın yamacına düşen ünlü gölgeyi görmek için dolmuşa yetişmeye çalışırlar. Gölgeyi görürler; ama Mert'in aklına yine bir fikir "
   "gelmiştir: kaşarı Kars'a götürmek.",
   {"market": ("Ardahan, market önü", "the front of a small grocery market on a quiet street in Ardahan: wooden crates, a plain awning, cool "
               "morning light, green hills behind"),
    "gol": ("Çıldır Gölü kıyısı", "the grassy shore of Lake Çıldır near Ardahan: a vast calm blue lake, a small wooden rowboat pulled up on "
            "the shore, green meadows and distant hills under a big sky"),
    "mandira": ("Yayla mandırası", "a small highland dairy near Lake Çıldır: a clean whitewashed room with stainless steel vats, round "
                "yellow kaşar wheels aging on wooden racks, a window to the meadows"),
    "dolmus": ("Damal yolu", "a narrow highland road to Damal: green rolling meadows, a white minibus stopped at the roadside, a mountain "
               "slope ahead"),
    "damal": ("Damal, seyir yeri", "a viewing spot in Damal at late afternoon: a grassy hill with a few benches, a wide mountain slope "
              "opposite where the low sun casts long shadows")},
   [
       S("09:00 sabah", "market", ["ali", "marketci"], "Son Tulum",
         "Ardahan'da bir market kalan 15 kilo tulum peynirini alır. Oltu tespihlerden altısı da takipçilere gider.",
         "The grocer opens the cheese box, smells the cloth-wrapped block and nods; Ali hands him the box and receives cash, then checks his "
         "phone and smiles.",
         [("marketci", "Erzincan tulumu burada aranır. Hepsini alırım.", "practical"),
          ("ali", "Altı tespih de az önce satıldı. Güne iyi başladık.", "pleased")],
         "static medium two-shot at the shop door",
         t=[U(15, "kg", 640, "satis", "Erzincan tulum peyniri, markete ({adet} kg x {fiyat} TL)"),
            U(6, "tespih", 2000, "satis", "Oltu taşı tespih, takipçi siparişi (6 x 2.000 TL)")]),
       S("11:30 sabah", "gol", ["mert", "ali"], "Kışın Buz, Yazın Gökyüzü",
         "Çıldır Gölü kıyısındadırlar. Ali kışın gölün donup üstünde atlı kızakların gezdiğini anlatır.",
         "Mert and Ali walk along the lakeshore; Mert picks up a flat stone and skips it across the calm water; Ali points far across the lake "
         "with a wide sweep of his arm.",
         [("ali", "Kışın bu göl donuyor, üstünde atlı kızaklar geziyor.", "fascinated"),
          ("mert", "O zaman kışın geliriz, kızakla kaşar taşırız!", "playful")],
         "slow tracking shot along the shore"),
       S("13:00 iç-gündüz", "mandira", ["mert", "ali", "gulizar"], "Yayla Sütünden Kaşar",
         "Mandırada Gülizar Abla yayla sütünden kaşarın nasıl yapıldığını gösterir, kesip tattırır.",
         "Gülizar cuts a wedge from a round yellow kaşar wheel and hands two pieces to Mert and Ali; both taste it at the same moment and their "
         "eyes widen together.",
         [("gulizar", "Bu inekler sadece yayla otu yer. Tadı ondan.", "proud"),
          ("mert", "Abla, Türkiye'de bunun tadını bilmeyen kalmasın.", "amazed")],
         "static medium three-shot at the racks",
         t=T("yemek", 500, "Mandırada öğle kahvaltısı")),
       S("14:00 iç-gündüz", "mandira", ["ali", "gulizar"], "Elli Kilo",
         "Elli kilo yayla kaşarı alırlar. Ali faturasını ister, Gülizar Abla takdir eder.",
         "Gülizar lifts kaşar wheels onto a scale and then into boxes; Ali hands her the money and holds out his notebook for her to sign a "
         "receipt line; she signs and laughs.",
         [("gulizar", "Kilosu dört yüz yirmi. Faturayı da yazayım, düzgün iş yapıyorsunuz.", "approving"),
          ("ali", "Her kuruş deftere, abla.", "proud")],
         "slow push-in on the scale and the notebook",
         t=U(50, "kg", 420, "alis", "Yayla kaşarı, Çıldır ({adet} kg x {fiyat} TL)")),
       S("17:10 ikindi", "dolmus", ["mert", "ali"], "Son Dolmuş",
         "Damal'daki gölgeyi görmek için son dolmuşa koşarlar. Dolmuş kalkmak üzeredir.",
         "Mert and Ali sprint along the roadside toward the white minibus as its door begins to close; Mert slaps the side of the minibus, the "
         "door opens again, and they jump in.",
         [("mert", "Bekle abi! Gölgeyi kaçırmayalım!", "shouting, running")],
         "fast tracking shot from the side of the road",
         t=U(2, "bilet", 150, "ulasim", "Ardahan-Damal dolmuşu ({adet} x {fiyat} TL)")),
       S("19:20 gün batımı", "damal", ["mert", "ali"], "Kaşar Kars'a mı?",
         "Damal'da batan güneşin dağa düşürdüğü ünlü gölgeyi izlerler. Mert kaşarı Kars'a götürmek ister; Ali gülmeye başlar.",
         "Mert and Ali sit on a bench watching the long shadows move across the mountain slope; Mert suddenly turns to Ali with excitement and "
         "Ali starts laughing helplessly.",
         [("mert", "Bu kaşarı Kars'ta satalım, Kars büyük şehir!", "excited"),
          ("ali", "Mert... Kars'a kaşar götürmek, Malatya'ya kayısı götürmek gibi.", "laughing")],
         "slow push-in from behind the bench toward the sunlit slope",
         t=[T("konaklama", 900, "Köy pansiyonu, 1 gece"), U(2, "bilet", 250, "ulasim", "Damal-Kars otobüsü ({adet} x {fiyat} TL)")],
         kurgu="Gölge sahnesi yalnızca uzaktan dağ yamacı olarak gösterilir; yorum katılmaz."),
   ],
   misafir={"marketci": ("MARKETÇİ", "GROCER, a 45-year-old Turkish man, tall and thin, a short dark beard, a navy fleece vest",
                         "adult male voice, practical and calm, Eastern Turkish"),
            "gulizar": ("GÜLİZAR ABLA", "GÜLİZAR, a 42-year-old Turkish dairy owner, strong build, rosy cheeks, a white hairnet cap, a white "
                        "work coat and rubber boots", "middle-aged female voice, confident, warm Ardahan Turkish")},
   ay=AY, hava="serin", urun="Yayla kaşarı, Kafkas arısı balı, kaz; Çıldır Gölü, Ardahan Kalesi, Damal",
   sponsor="Süt ürünleri, bal ya da yayla turizmi alanında",
   kapak=("gol", ["mert", "ali"], "Mert skips a stone across the vast calm Lake Çıldır while Ali laughs beside him, a small wooden boat on the "
          "shore, huge sky", "Çıldır Gölü'nde taş sektiren Mert ve gülen Ali."),
   yakinda=("damal", ["mert", "ali"], "Two silhouettes on a bench facing a mountain slope as a long dramatic sunset shadow creeps over it, the "
            "sky burning orange", "Dağa uzanan gün batımı gölgesine bakan iki silüet."),
   tiktok="Çıldır'da yayla kaşarı 🧀 ve Mert'in en kötü fikri #JozhStudios",
   ig=("Ardahan'ın serin yaylalarındayız. Çıldır Gölü kışın donuyormuş, biz yazın taş sektirdik. 🏞️\n\n"
       "Gülizar Abla'nın mandırasından 50 kilo yayla kaşarı aldık. Mert'in fikri: kaşarı Kars'ta satmak. 😂\n\nSizce Kars'a kaşar götürülür mü? Kasa: {KASA}"),
   tags=["#Ardahan", "#Çıldır", "#Kaşar"],
   son="Mert kaşarı Kars'ta satmak istiyor. Ali gülmekten konuşamıyor.",
   teaser="Kışın donan bir göl, yayla kaşarı ve en kötü ticaret fikri. Bölüm 12: Ardahan. Pek yakında.")

# ======================================================================= 13 KARS
EP(13, "Kars", "Ani'nin Kapısında",
   "Kars'ta kaşar satılmaz, bu kesin. Ama Ali ilk büyük pazarlığını Boğatepe'de gravyer için yapar.",
   "Mert inat eder ve kaşarı Kars çarşısına götürür; peynirci güler ve kendi kaşarını tattırır. Ders alınır: kaşar Iğdır'a gidecektir. "
   "Oltu tespihlerin kalanı Kars'ta bir hediyelik dükkânına satılır. Ani Ören Yeri'nde İpek Yolu'nun bu kapısından geçen kervanları "
   "düşünürler. Boğatepe köyünde gravyer ustasıyla Ali ilk kez Mert'siz pazarlık eder ve 30 kilo Kars gravyeri alır. Akşam kaz eti "
   "yerken Mert, Ali'ye kadeh yerine ayran kaldırır: 'Ortağım.'",
   {"carsi": ("Kars çarşısı, peynirci", "a cheese shop in Kars's old bazaar: shelves stacked with huge round kaşar and gravyer wheels, a long "
              "wooden counter, Russian-era stone building facade outside"),
    "hediyelik": ("Hediyelik eşya dükkânı", "a small souvenir shop on a Kars street with stone Baltic-style facades: shelves of carpets, "
                  "copper items and glass display cases"),
    "ani": ("Ani Ören Yeri", "the ruins of Ani near Kars: vast golden grassland, the tall ruined red-stone city walls and the remains of a "
            "medieval cathedral on the edge of a deep river gorge, a huge sky"),
    "bogatepe": ("Boğatepe köyü, gravyer evi", "a gravyer cheese house in Boğatepe village near Kars: thick stone walls, enormous round "
                 "gravyer wheels aging on wooden shelves in a cool cellar, a big copper cauldron"),
    "lokanta": ("Kaz eti lokantası", "a warm traditional Kars restaurant at night: wooden tables, a copper tray of roasted goose with bulgur "
                "pilaf, carpets on the walls")},
   [
       S("09:00 sabah", "carsi", ["mert", "peynirci"], "Kars'a Kaşar",
         "Mert inatla kaşarı Kars çarşısına götürür. Peynirci güler ve tezgâhındaki dev tekerleklerden birini işaret eder.",
         "Mert places a wheel of kaşar on the counter with confidence; the cheese seller laughs, cuts a slice from one of his own giant wheels and "
         "holds it out to Mert, who tastes it and his face falls.",
         [("peynirci", "Evlat, Kars'a kaşar getirmek denize su taşımaktır.", "laughing kindly"),
          ("mert", "Ali haklıymış... yine.", "defeated, comic")],
         "static medium two-shot across the counter, slow push-in on Mert's face"),
       S("10:30 sabah", "hediyelik", ["ali", "dukkan"], "Tespihler Yerini Buldu",
         "Kalan dokuz oltu taşı tespih Kars'ta bir hediyelik dükkânına satılır.",
         "The shop owner lays the black prayer beads in his glass case one by one and admires them; Ali receives an envelope and writes the sale "
         "in his notebook on the counter.",
         [("dukkan", "Ani'ye gelen turist bunu çok sorar. Dokuzunu da alırım.", "pleased"),
          ("ali", "Tanesi iki bin. Hayırlı satışlar.", "polite")],
         "static medium shot over the glass case",
         t=U(9, "tespih", 2000, "satis", "Oltu taşı tespih, hediyelik dükkânına ({adet} x {fiyat} TL)")),
       S("12:30 öğle", "ani", ["mert", "ali"], "İpek Yolu'nun Kapısı",
         "Ani'nin surları ve katedrali önündedirler. Bir zamanlar kervanların geçtiği bu kapıda ticaretin ne kadar eski olduğunu düşünürler.",
         "Mert and Ali walk through the tall gap in the ruined red-stone city walls into the open grassland; Ali stops and looks up at the walls, "
         "Mert turns around slowly taking in the vast space.",
         [("ali", "Kervanlar bin yıl önce bu kapıdan geçiyormuş.", "awed"),
          ("mert", "O zamanın Mert'i ve Ali'si de kaşar satmaya mı çalışmış acaba?", "smiling")],
         "slow crane-up through the gate revealing the ruins and the gorge"),
       S("15:00 iç-gündüz", "bogatepe", ["ali", "gravyerci"], "Ali'nin Pazarlığı",
         "Boğatepe'de gravyer ustası İsmail Bey ile Ali ilk kez tek başına pazarlık eder. Mert kapıda nefesini tutar.",
         "Ali stands at a wooden table with İsmail facing him, both calm; Ali makes an offer with one raised hand, İsmail thinks, then extends his "
         "hand and they shake firmly.",
         [("ali", "Otuz kilo alırsak dokuz yüzden bırakır mısınız?", "steady, polite"),
          ("gravyerci", "Bin diyecektim. Ama pazarlığı güzel yaptın, olsun dokuz yüz.", "amused respect")],
         "slow push-in between the huge cheese wheels",
         t=U(30, "kg", 900, "alis", "Kars gravyeri, Boğatepe ({adet} kg x {fiyat} TL)")),
       S("15:20 iç-gündüz", "bogatepe", ["mert", "ali"], "Ortağım",
         "Mert kapıdan içeri koşar ve Ali'nin elini sıkar. Pazarlık ondan iyi gitmiştir.",
         "Mert rushes in from the cellar door, grabs Ali's hand with both of his and shakes it hard; Ali laughs, embarrassed, holding the brown "
         "notebook against his chest.",
         [("mert", "Bin diyecekmiş! Sen benden iyi pazarlıkçısın Ali!", "proud, loud"),
          ("ali", "Sadece kibar sordum.", "shy smile")],
         "static medium two-shot among the shelves"),
       S("20:00 iç-gece", "lokanta", ["mert", "ali"], "Kaz ve Ayran",
         "Akşam Kars'ın meşhur kaz etini bulgur pilavıyla yerler. Mert ayran bardağını kaldırır.",
         "Mert lifts a glass of ayran toward Ali over the copper tray of roasted goose; Ali clinks his glass against it, both smiling, warm lamp "
         "light on their faces.",
         [("mert", "Ortağıma! Yarın Iğdır'da kaşarı satan da sen ol.", "warm toast"),
          ("ali", "Yarın Iğdır kırk derece. Peynir eriyecek.", "worried smile")],
         "slow dolly-in from across the restaurant",
         t=[T("yemek", 900, "Akşam yemeği: kaz eti ve bulgur pilavı"), T("konaklama", 1200, "Otel, 1 gece"),
            U(2, "bilet", 250, "ulasim", "Kars-Iğdır otobüsü ({adet} x {fiyat} TL)")]),
   ],
   misafir={"peynirci": ("PEYNİRCİ", "CHEESE SELLER, a 55-year-old Turkish man, round and jolly, a bushy grey mustache, a white shop coat",
                         "mature male voice, hearty laughter, Kars Turkish"),
            "dukkan": ("DÜKKÂN SAHİBİ", "SHOP OWNER, a 38-year-old Turkish woman, slim, dark hair in a bun, a burgundy cardigan",
                       "female voice, calm and friendly"),
            "gravyerci": ("İSMAİL BEY", "İSMAİL, a 63-year-old Turkish cheesemaker, tall and lean, a grey goatee, a wool flat cap and a "
                          "white apron over a thick sweater", "elderly male voice, slow, dry humor, Kars Turkish")},
   ay=AY, hava="serin", urun="Kars gravyeri (Boğatepe), Kars kaşarı, kaz eti, kaşar; Ani Ören Yeri, Kars Kalesi",
   sponsor="Gravyer, kaşar ya da kaz eti alanında",
   kapak=("ani", ["mert", "ali"], "Mert and Ali stand small in the gap of the towering red-stone walls of Ani, golden grass, huge dramatic sky, "
          "both looking up in awe", "Ani'nin dev surlarının kapısında küçücük kalan Mert ve Ali."),
   yakinda=("bogatepe", ["ali"], "Ali's calm face in a dim stone cellar between giant round cheese wheels, his hand extended for a handshake "
            "toward a figure in shadow", "Loş mahzende dev peynirlerin arasında el uzatan Ali."),
   tiktok="Kars'a kaşar götürdüm 🤦‍♂️ Ali ise gravyerde 100 lira indirim aldı #JozhStudios",
   ig=("Evet, Kars'a kaşar götürdüm. Peynirci güldü: 'Denize su taşımak.' 😂\n\n"
       "Ama günün kahramanı Ali: Boğatepe'de gravyer ustasıyla ilk kez tek başına pazarlık yaptı ve bin liralık peyniri dokuz yüze aldı. "
       "Ani'nin surlarında İpek Yolu'nu düşündük, kaz etiyle günü kapattık. 🦢\n\nKasa: {KASA}"),
   tags=["#Kars", "#Ani", "#Gravyer"],
   son="Yarın Iğdır'da hava kırk derece. Kaşar ve gravyer erimeden satılmalı.",
   teaser="Kars'a kaşar götürmenin bedeli ve Ali'nin ilk pazarlığı. Bölüm 13: Kars. Pek yakında.")

# ======================================================================= 14 IĞDIR
EP(14, "Iğdır", "Ağrı Dağı'nın Gölgesinde",
   "Kırk derecede peynir satışı; Mert'in taze kayısı aşkı ve Ali'nin uyarısı.",
   "Iğdır ovası sıcaktır; Ağrı Dağı ufukta karlı tepesiyle durur. Ali sözünü tutar: 50 kilo kaşarı bir otelin mutfağına kendisi satar. "
   "Gravyerin bir kısmını bir şarküteri alır. Öğlen Iğdır'ın tandır ekmeği ve yerel köftesiyle karınlarını doyururlar. Akşamüstü kayısı "
   "bahçelerinde taze Iğdır kayısısı görünce Mert dayanamaz: 300 kilo alır. Ali uyarır: 'Taze kayısı bekletilmez.' Gece kasalar otel "
   "odasının sıcağında durmaktadır.",
   {"yol": ("Iğdır ovası yolu", "a straight road across the hot green Iğdır plain at morning, poplar rows and fields, and the huge "
            "snow-capped peak of Mount Ararat rising on the horizon"),
    "otel": ("Otel mutfağı", "the large steel kitchen of a hotel in Iğdır: stainless counters, a walk-in cold room door, cooks' white "
             "jackets on hooks"),
    "sarkuteri": ("Şarküteri", "a small delicatessen in central Iğdır with a glass cheese counter and shelves of jars, a fan turning"),
    "fırın": ("Tandır fırını", "a traditional tandır bakery in Iğdır: a round clay oven in the floor, flat breads stuck on its inner wall, "
              "a wooden bench"),
    "bahce": ("Iğdır kayısı bahçesi", "an apricot orchard on the Iğdır plain at late afternoon: trees with ripe orange-red fresh apricots, "
              "plastic crates filled with fruit, Mount Ararat behind"),
    "oda": ("Otel odası", "a small hot hotel room in Iğdır at night: a window open to the warm night, a ceiling fan, plastic crates of fresh "
            "apricots stacked on the floor")},
   [
       S("09:00 sabah", "yol", ["mert", "ali"], "Kırk Derece",
         "Iğdır'a sabah varırlar. Ufukta Ağrı Dağı'nın karlı tepesi, ovada şimdiden kırk dereceye yaklaşan sıcak.",
         "Mert and Ali step off a bus at the roadside carrying cheese boxes; Mert wipes sweat from his forehead and points at the snowy peak on "
         "the horizon while Ali fans himself with his notebook.",
         [("mert", "Şu dağın tepesi kar, burası fırın!", "amazed"),
          ("ali", "Peynirler eriyor Mert, hızlı olmamız lazım.", "worried")],
         "slow crane-up from the boxes to the mountain on the horizon", h="sıcak"),
       S("10:30 iç-gündüz", "otel", ["ali", "asci"], "Sözünü Tutan Ali",
         "Ali dünkü sözünü tutar: 50 kilo yayla kaşarını bir otelin mutfak şefine kendisi satar.",
         "The head cook cuts a slice of kaşar, tastes it and nods twice; Ali slides the cheese boxes along the steel counter toward him and they "
         "shake hands.",
         [("asci", "Kahvaltıda misafirlerim bunu sever. Elli kilonun hepsi, beş yüz kırktan.", "decisive"),
          ("ali", "Anlaştık şefim. Soğuk odaya hemen koyalım.", "efficient")],
         "static medium two-shot at the counter",
         t=U(50, "kg", 540, "satis", "Yayla kaşarı, otel mutfağına ({adet} kg x {fiyat} TL)")),
       S("12:00 öğle", "sarkuteri", ["mert", "sarkuteri"], "Gravyer",
         "Mert bir şarküteriye 10 kilo gravyer satar. Kalan 20 kiloyu takipçilere saklar.",
         "The deli owner weighs a block of gravyer on his scale, then shakes Mert's hand; Mert puts the remaining cheese box back under his arm "
         "with a satisfied grin.",
         [("sarkuteri", "Kars gravyeri burada az bulunur. On kilo alırım.", "pleased"),
          ("mert", "Kalan yirmi kilo gurbetçilerin.", "smiling")],
         "static medium shot over the glass counter", h="sıcak",
         t=U(10, "kg", 1250, "satis", "Kars gravyeri, şarküteriye ({adet} kg x {fiyat} TL)")),
       S("13:30 iç-gündüz", "fırın", ["mert", "ali"], "Tandırdan Ekmek",
         "Tandır fırınında sıcak ekmek ve yerel köfteyle öğle yemeği yerler.",
         "A hot flat bread is peeled off the inner wall of the clay oven by an unseen baker's hand and placed on the bench; Mert tears it in half "
         "and hands half to Ali, steam rising.",
         [("mert", "Kırk derecede tandır başında ekmek... ama değer.", "sweaty, happy"),
          ("ali", "Değer.", "mouth full")],
         "static medium two-shot on the bench",
         t=T("yemek", 600, "Öğle yemeği: tandır ekmeği ve köfte")),
       S("18:00 gün batımı", "bahce", ["mert", "ali", "bahcivan"], "Taze Kayısı",
         "Iğdır'ın taze kayısısını gören Mert dayanamaz ve 300 kilo alır. Ali uyarır: taze kayısı bekletilmez.",
         "Mert bites into a fresh red-orange apricot and its juice runs down his hand; he waves at the farmer to load crates; Ali grabs Mert's "
         "arm and shakes his head, but the farmer is already stacking crates.",
         [("mert", "Üç yüz kilo alıyoruz, Ağrı'da kapış kapış gider!", "impulsive, excited"),
          ("ali", "Taze kayısı bekletilmez Mert. İki gün dayanmaz.", "warning")],
         "slow push-in on Mert's face, Mount Ararat glowing behind",
         t=U(300, "kg", 45, "alis", "Taze Iğdır kayısısı ({adet} kg x {fiyat} TL)")),
       S("23:00 iç-gece", "oda", ["mert", "ali"], "Sıcak Oda",
         "Gece odada vantilatör döner. Ali kasalara dokunur: kayısılar ısınmıştır. Mert uyuyormuş gibi yapar.",
         "Ali kneels by the stacked crates under the turning ceiling fan, touches the apricots and frowns; he turns to Mert lying on the bed with "
         "his eyes tightly shut, pretending to sleep.",
         [("ali", "Kayısılar ısınmış Mert.", "worried whisper"),
          ("mert", "Uyuyorum.", "eyes closed, guilty")],
         "static high-angle shot from the ceiling fan",
         t=[T("konaklama", 1000, "Otel, 1 gece"), U(2, "bilet", 300, "ulasim", "Iğdır-Doğubayazıt otobüsü ({adet} x {fiyat} TL)")]),
   ],
   misafir={"asci": ("AŞÇIBAŞI", "HEAD COOK, a 45-year-old Turkish man, stout, black beard, white chef jacket and black cap",
                     "adult male voice, decisive, Eastern Turkish"),
            "sarkuteri": ("ŞARKÜTERİCİ", "DELI OWNER, a 50-year-old Turkish man, grey hair, glasses, a white shop coat", "adult male voice, calm"),
            "bahcivan": ("BAHÇIVAN", "FARMER, a 58-year-old Turkish man, sun-darkened, white stubble, a straw hat and a sweat-darkened shirt",
                         "elderly male voice, friendly, Iğdır Turkish")},
   ay=AY, hava="sıcak", urun="Iğdır kayısısı (taze), pamuk, tandır ekmeği; Ağrı Dağı manzarası, Aras ovası",
   sponsor="Taze meyve, tarım ya da yerel gıda alanında",
   kapak=("bahce", ["mert", "ali"], "Mert bites a juicy fresh apricot with a huge grin while Ali holds his head in worry beside a tower of "
          "crates, snowy Mount Ararat glowing in the sunset", "Taze kayısıyı ısıran Mert, kasaların yanında başını tutan Ali."),
   yakinda=("oda", ["ali"], "A dark hot room lit only by the street through the window, a ceiling fan's shadow sweeping over stacked crates "
            "of fruit, Ali's worried face", "Vantilatörün gölgesi kasaların üstünde dönüyor; endişeli Ali."),
   tiktok="40 derece, 50 kilo kaşar ve 300 kilo taze kayısı... hata mı? 🍑🔥 #JozhStudios",
   ig=("Iğdır'da 40 derece! Ali sözünü tuttu: 50 kilo kaşarı otel şefine kendisi sattı. 🧀\n\n"
       "Sonra Mert taze Iğdır kayısısını gördü ve 300 kilo aldı. Ali'nin uyarısı: 'Taze kayısı iki gün dayanmaz.' 🍑\n\nGece oda sıcak, kasalar sıcak... Sizce kurtarabilecek miyiz? Kasa: {KASA}"),
   tags=["#Iğdır", "#AğrıDağı", "#TazeKayısı"],
   son="Kayısılar sıcak odada ısınmıştır. Ali'nin uyarısı kulaklarda.",
   teaser="Kırk derece, karlı bir dağ ve üç yüz kilo risk. Bölüm 14: Iğdır. Pek yakında.")

# ======================================================================= 15 AĞRI
EP(15, "Ağrı", "İlk Zarar",
   "Taze kayısıların yarısı bozulur. İshak Paşa Sarayı'nın avlusunda Mert özür diler, Ali defterine ilk kırmızı satırı yazar.",
   "Doğubayazıt'ta sabah kasaları açarlar: kayısıların yarısı yumuşamış, bir kısmı bozulmuştur. Pazarda sağlam 150 kilo ancak 50'den satılır; "
   "yumuşayanları atmak yerine reçel yapan Zehra Teyze'ye bağışlarlar. Mert bu kez özür diler. Gurbetçi takipçiler kalan gravyeri alır ve "
   "gün kurtulur. İshak Paşa Sarayı'nın avlusunda, Ağrı Dağı'nın karşısında Ali ilk zararı deftere kırmızıyla yazar. Öğlen abdigör köftesi "
   "yerler. Gece Van'dan bir kahvaltı salonu sahibi yazar.",
   {"pazar": ("Doğubayazıt pazarı", "a small open-air morning market in Doğubayazıt: wooden stalls under canvas, crates of fruit and vegetables, "
              "dusty light, the snowy peak of Mount Ararat visible above the rooftops"),
    "zehra": ("Zehra Teyze'nin bahçesi", "a modest village house courtyard near Doğubayazıt: a big pot on a wood fire for jam, glass jars on "
              "a wooden table, a mulberry tree"),
    "saray": ("İshak Paşa Sarayı", "the courtyard of İshak Paşa Palace on a hillside above Doğubayazıt: an ornate 18th-century palace of "
              "golden stone with a domed mosque and carved portals, the plain and Mount Ararat in the distance"),
    "lokanta": ("Köfteci", "a small Doğubayazıt restaurant: plain walls, a few tables, a bowl of abdigör köfte (soft pounded meatballs) "
                "with bread and onions on the table"),
    "otel": ("Otel odası", "a simple hotel room in Doğubayazıt at night: two beds, empty crates by the door, the dark mountain silhouette "
             "through the window")},
   [
       S("08:00 sabah", "pazar", ["mert", "ali"], "Kasaları Açmak",
         "Pazarda kasaları açarlar: kayısıların yarısı yumuşamış, bir kısmı bozulmuştur. Mert sessizleşir.",
         "Ali lifts the lid of a crate and presses a soft, bruised apricot with his thumb; Mert opens the next crate, looks inside and slowly "
         "sits down on an upturned crate with his elbows on his knees.",
         [("ali", "Yarısı gitmiş Mert.", "quiet, not angry"),
          ("mert", "Biliyorum. Dinlemedim seni.", "ashamed")],
         "slow push-in from the market aisle"),
       S("09:30 sabah", "pazar", ["mert", "pazarci"], "Elli Liradan",
         "Sağlam 150 kilo ancak kilosu 50'den satılır. Alış 45'ti; yol, otel ve bozulanla birlikte bu açık bir zarardır.",
         "A market trader inspects a few apricots, then counts out a small stack of banknotes into Mert's hand; Mert nods, swallowing his pride, "
         "and helps load the good crates onto the trader's cart.",
         [("pazarci", "Yüz elli kilo, ellisinden. Daha fazla veremem, mal yumuşak.", "fair, blunt"),
          ("mert", "Haklısın abi. Ver gitsin.", "resigned")],
         "static medium two-shot at the stall",
         t=U(150, "kg", 50, "satis", "Taze Iğdır kayısısı, sağlam kısım ({adet} kg x {fiyat} TL)")),
       S("10:30 sabah", "zehra", ["mert", "ali", "zehra"], "Reçel Olsun",
         "Yumuşayan kayısıları atmak yerine reçel yapan Zehra Teyze'ye bağışlarlar. Teyze buna çok sevinir.",
         "Mert and Ali carry two crates of soft apricots into the courtyard and set them by the jam pot; Zehra claps her hands and immediately "
         "starts tipping apricots into the big pot.",
         [("zehra", "Bunlar çöp değil oğlum, en tatlı reçel bunlardan olur.", "delighted"),
          ("ali", "Bir kavanozunu da bize saklarsın teyze.", "smiling")],
         "static wide shot of the courtyard, slow push-in on the pot"),
       S("13:00 öğle", "saray", ["mert", "ali"], "Kırmızı Satır",
         "İshak Paşa Sarayı'nın avlusunda Ali ilk zararı deftere yazar. Mert, gravyer siparişlerinin günü kurtardığını görür.",
         "Ali sits on a low stone ledge in the palace courtyard writing in the brown notebook with a red pen; Mert sits beside him, reads his phone "
         "and slowly smiles, showing Ali the screen.",
         [("ali", "İlk zararımız. Kırmızıyla yazıyorum ki unutmayalım.", "calm, serious"),
          ("mert", "Gravyerin hepsi gitti Ali. Gurbetçiler kurtardı bizi.", "relieved")],
         "slow crane-up from the notebook to the palace domes and the mountain",
         t=U(20, "kg", 1250, "satis", "Kars gravyeri, takipçi siparişi ({adet} kg x {fiyat} TL)")),
       S("14:30 iç-gündüz", "lokanta", ["mert", "ali"], "Abdigör Köftesi",
         "Ağrı'nın yumuşacık abdigör köftesini yerler. Mert yeni bir kural koyar: bozulan mal almak yok.",
         "Mert cuts a soft round abdigör meatball with the edge of his fork and holds up one finger like making a rule; Ali nods and writes it in "
         "the notebook.",
         [("mert", "Yeni kural: iki günde bozulan mal almıyoruz.", "serious"),
          ("ali", "Kural bir, deftere yazıldı.", "smiling")],
         "static medium two-shot across the table",
         t=T("yemek", 700, "Öğle yemeği: abdigör köftesi")),
       S("22:00 iç-gece", "otel", ["mert", "ali"], "Van'dan Mesaj",
         "Gece Van'daki bir kahvaltı salonu sahibi yazar: otlu peynirin en iyisini nerede bulacaklarını biliyordur. Ama bir şartı vardır.",
         "Ali lies on his bed reading his phone, sits up and reads the message aloud; Mert, already half asleep, opens one eye and smiles.",
         [("ali", "Van'dan bir kahvaltıcı yazdı: 'Önce kahvaltıya gelin, sonra peynir.'", "amused"),
          ("mert", "Bu şarta itirazım yok.", "sleepy, happy")],
         "static medium shot from the foot of the beds",
         t=[T("konaklama", 1000, "Otel, 1 gece"), U(2, "bilet", 450, "ulasim", "Doğubayazıt-Van otobüsü ({adet} x {fiyat} TL)")]),
   ],
   misafir={"pazarci": ("PAZARCI", "MARKET TRADER, a 47-year-old Turkish man, wiry, a grey stubble, a dusty cap and a blue work jacket",
                        "adult male voice, blunt but fair, Eastern Turkish"),
            "zehra": ("ZEHRA TEYZE", "ZEHRA, a 70-year-old Turkish village woman, small and lively, a colorful printed headscarf, a dark vest over "
                      "a long dress, an apron", "elderly female voice, cheerful, Eastern Anatolian Turkish")},
   ay=AY, hava="sıcak", urun="Abdigör köftesi, el dokuması kilim; İshak Paşa Sarayı, Ağrı Dağı",
   sponsor="Turizm, el dokuması ya da yöresel yemek alanında",
   kapak=("saray", ["mert", "ali"], "Mert and Ali sit on a stone ledge in the golden courtyard of İshak Paşa Palace, Ali writing in a notebook "
          "with a red pen, Mert looking at the mountain, Mount Ararat glowing behind", "İshak Paşa Sarayı'nın avlusunda deftere kırmızı satır yazan Ali."),
   yakinda=("pazar", ["mert"], "Mert sitting alone on an upturned crate in an early-morning market, head lowered, a crate of bruised fruit at "
            "his feet, a snowy mountain peak behind in soft light", "Ters kasanın üstünde başı önde oturan Mert."),
   tiktok="İlk zararımız: 300 kilo taze kayısı 😔 Ama ders aldık #JozhStudios",
   ig=("Ali uyarmıştı: taze kayısı iki gün dayanmaz. Dinlemedim. 😔 Yarısı bozuldu, sağlam kısmı zararına sattık.\n\n"
       "Yumuşayanları Zehra Teyze'ye verdik, reçel olacaklar. İshak Paşa Sarayı'nın avlusunda Ali ilk zararı deftere kırmızıyla yazdı.\n\n"
       "Yeni kural: iki günde bozulan mal yok. Sizin ticarette ilk dersiniz ne oldu? Kasa: {KASA}"),
   tags=["#Ağrı", "#İshakPaşaSarayı", "#İlkZarar"],
   son="Van'dan bir kahvaltı salonu sahibi yazar: 'Önce kahvaltıya gelin, sonra peynir.'",
   teaser="Bozulan kayısılar, bir saray avlusu ve deftere yazılan ilk kırmızı satır. Bölüm 15: Ağrı. Pek yakında.")

# ======================================================================= 16 VAN
EP(16, "Van", "Kahvaltının Başkenti",
   "Van kahvaltısı, iki renk gözlü kedi, otlu peynir ve ilk büyük kavga.",
   "Van'ın Kahvaltıcılar Sokağı'nda Nurettin Abi'nin sofrasında otlu peynir, murtuga ve cacığı tadarlar. Van Kedisi Evi'nde bir gözü mavi bir "
   "gözü sarı kedileri görürler. Nurettin Abi'nin tanıştırdığı peynirci, peynire katılan dağ otlarını anlatır; 60 kilo otlu peynir alırlar. "
   "Akdamar Adası'na giden teknede Mert büyük bir toptan satış için peyniri hemen ucuza elden çıkarmak ister; Ali ilk kez sesini yükseltir. "
   "Van Kalesi'nde gün batarken barışırlar. Ali'nin uyarısı: Hakkari yolu zordur.",
   {"kahvalti": ("Kahvaltıcılar Sokağı", "a famous breakfast salon on a busy street in Van: a long table covered with dozens of small plates "
                 "of herb cheese, honey with cream, olives, eggs, flatbreads and tea glasses, warm morning light through a big window"),
    "kedi": ("Van Kedisi Evi", "the Van Cat House: a bright garden enclosure with soft grass, small wooden houses and fluffy pure-white Van "
             "cats with odd-colored eyes, one blue and one amber"),
    "peynirci": ("Otlu peynirci", "an herb-cheese shop in Van: white cheese wheels flecked with green wild herbs in big tins of brine, bundles "
                 "of dried mountain herbs hanging, a wooden counter"),
    "tekne": ("Akdamar teknesi", "a small passenger boat on the deep blue water of Lake Van heading to Akdamar Island: wooden benches, a white "
              "railing, the island with its medieval stone church ahead and mountains around"),
    "kale": ("Van Kalesi", "the long ancient rock of Van Castle at sunset: weathered stone walls and steps along the cliff top, Lake Van "
             "shimmering below")},
   [
       S("08:30 iç-gündüz", "kahvalti", ["mert", "ali", "nurettin"], "Otuz Tabak",
         "Nurettin Abi'nin kahvaltı salonunda otuz küçük tabaklık bir sofraya otururlar. Önce kahvaltı, sonra peynir.",
         "Nurettin sets the last small plate on an already crowded breakfast table and gestures proudly; Mert's eyes travel over the dozens of "
         "plates while Ali dips bread into honey and cream.",
         [("nurettin", "Van'da kahvaltı bir öğün değil, bir törendir.", "proud, theatrical"),
          ("mert", "Abi ben bu töreni bitirmeden kalkmam.", "overwhelmed, happy")],
         "slow crane-down over the table to the three of them",
         t=T("yemek", 1200, "Van kahvaltısı (2 kişi)")),
       S("10:30 sabah", "kedi", ["mert", "ali"], "Bir Mavi, Bir Sarı",
         "Van Kedisi Evi'nde bir gözü mavi bir gözü kehribar rengi beyaz Van kedilerini görürler.",
         "A fluffy white Van cat with one blue and one amber eye walks up to Mert and rubs against his hand; Mert kneels down slowly and Ali "
         "crouches beside him smiling.",
         [("mert", "Bunun bir gözü mavi, bir gözü sarı!", "delighted whisper"),
          ("ali", "Bir gözüyle kâra, bir gözüyle zarara bakıyor.", "joking")],
         "slow push-in at ground level to the cat and Mert's hand"),
       S("12:30 iç-gündüz", "peynirci", ["mert", "ali", "peynirci"], "Dağ Otları",
         "Peynirci, otlu peynire katılan sirmo ve mendi gibi dağ otlarını anlatır. 60 kilo alırlar.",
         "The cheesemaker lifts a herb-flecked wheel from the brine tin, breaks it open to show the green herbs inside and hands a piece to Ali, "
         "who tastes it and nods to Mert.",
         [("peynirci", "Baharda dağdan ot toplanır, peynire basılır. Kilosu dört yüz seksen.", "knowledgeable"),
          ("ali", "Altmış kilo alıyoruz.", "decisive")],
         "static medium three-shot at the counter",
         t=U(60, "kg", 480, "alis", "Van otlu peyniri ({adet} kg x {fiyat} TL)")),
       S("15:00 ikindi", "tekne", ["mert", "ali"], "İlk Kavga",
         "Akdamar teknesinde Mert peyniri hemen bir toptancıya ucuza verip 'daha büyük' bir iş kovalamak ister. Ali ilk kez bağırır.",
         "On the boat bench Mert talks fast and waves his phone; Ali suddenly stands up, raising his voice, then the boat rocks slightly and both "
         "grab the railing, staring at each other.",
         [("mert", "Peyniri toptancıya verelim, parayla daha büyük bir iş yapalım!", "fast, impatient"),
          ("ali", "Her şeyi bir anda yapamayız Mert! Bir tane plan, bir tane!", "loud, frustrated")],
         "static medium two-shot on the boat, the island behind",
         t=U(2, "kişi", 300, "diger_gider", "Akdamar teknesi ve giriş ({adet} x {fiyat} TL)")),
       S("19:30 gün batımı", "kale", ["mert", "ali"], "Kalede Barış",
         "Van Kalesi'nde gün batarken Mert özür diler. Ali de sesini yükselttiği için üzgündür.",
         "Mert and Ali sit on the ancient stone steps of the castle wall above the glowing lake; Mert nudges Ali's shoulder with his own, Ali "
         "nudges back and both smile at the sunset.",
         [("mert", "Haklısın. Bir plan, bir adım.", "sincere"),
          ("ali", "Ben de bağırmamalıydım. Ama iyi geldi.", "half-laughing")],
         "slow dolly-out revealing the cliff and the lake"),
       S("22:30 gece", "kale", ["mert", "ali"], "Hakkari Yolu",
         "Kaleden inerken Ali yarınki yolu hatırlatır: Hakkari'ye dağ yolu, sabah beşte otobüs.",
         "Mert and Ali walk down the stone steps of the castle using their phone flashlights; Ali checks the time and holds up five fingers; "
         "Mert groans and laughs.",
         [("ali", "Hakkari yolu dağ yolu. Sabah beşte kalkıyoruz.", "firm"),
          ("mert", "Beşte mi? Kahvaltı töreni ne olacak?", "groaning")],
         "slow tracking shot following them down the steps",
         t=[T("konaklama", 1400, "Otel, 1 gece"), U(2, "bilet", 600, "ulasim", "Van-Hakkari otobüsü ({adet} x {fiyat} TL)")]),
   ],
   misafir={"nurettin": ("NURETTİN ABİ", "NURETTİN, a 49-year-old Turkish breakfast salon owner, tall, a neat salt-and-pepper beard, a big "
                         "warm smile, a white shirt with rolled sleeves and a dark vest", "adult male voice, theatrical, proud Van Turkish"),
            "peynirci": ("PEYNİRCİ", "CHEESEMAKER, a 55-year-old Turkish man, stocky, a grey mustache, a white work coat and cap",
                         "mature male voice, knowledgeable, Van Turkish")},
   ay=AY, hava="açık", urun="Van otlu peyniri, Van kahvaltısı, murtuga, inci kefali; Van Kedisi, Akdamar Adası, Van Kalesi",
   sponsor="Kahvaltı salonu, otlu peynir ya da turizm alanında",
   kapak=("kahvalti", ["mert", "ali", "nurettin"], "A huge Van breakfast table with dozens of small plates fills the foreground, Mert and Ali "
          "behind it with open mouths, Nurettin presenting it proudly with open arms", "Dev Van kahvaltısının arkasında ağzı açık kalan Mert ve Ali."),
   yakinda=("tekne", ["mert", "ali"], "Two young men standing face to face on a boat in tense silhouette, a dark lake and an island church in "
            "shadow behind them, dramatic backlight", "Teknede karşı karşıya duran iki silüet; gergin bir an."),
   tiktok="Van kahvaltısı: 30 tabak 🍳 ve ilk büyük kavgamız #JozhStudios",
   ig=("Van'da kahvaltı bir öğün değil, bir tören! 🍳 Nurettin Abi'nin otuz tabaklık sofrasından sonra otlu peynirin sırrını öğrendik: dağ otları. 🌿\n\n"
       "Akdamar teknesinde ilk kez kavga ettik. Van Kalesi'nde gün batarken barıştık.\n\nSiz en iyi arkadaşınızla iş yapar mıydınız? Kasa: {KASA}"),
   tags=["#Van", "#VanKahvaltısı", "#OtluPeynir"],
   son="Hakkari'ye dağ yolu: otobüs sabah beşte.",
   teaser="Otuz tabaklık bir kahvaltı, iki renk gözlü bir kedi ve ilk kavga. Bölüm 16: Van. Pek yakında.")

# ======================================================================= 17 HAKKARİ
EP(17, "Hakkari", "Zap'ın Kıyısında",
   "Dağ yolunda bir sürü yolu keser; Hakkari'de kilim dokuyan kadınlar ve Cemil Bey'den ilk mesaj.",
   "Sabah Zap Vadisi'nden geçen yolda yüzlerce koyun otobüsü durdurur; Mert inip çobana yardım eder. Hakkari'de otlu peynirin yarısını bir "
   "lokantaya ve takipçilere satarlar. Kilim dokuyan kadınların atölyesinde Hakkari kiliminin renklerini ve motiflerini öğrenir, altı kilim "
   "alırlar. Akşamüstü Cilo Dağları'na bakan bir tepede otururken Cemil Bey'den ilk mesaj gelir: 'Üç şehir kaldı. Hesap?'",
   {"yol": ("Zap Vadisi yolu", "a narrow mountain road along the deep Zap river valley near Hakkari: steep rocky slopes, the green-blue river "
            "far below, a white bus stopped, hundreds of sheep filling the road"),
    "lokanta": ("Hakkari lokantası", "a small restaurant in central Hakkari with a window onto steep mountains: plastic chairs, a glass "
                "counter, steel trays"),
    "atolye": ("Kilim atölyesi", "a bright kilim weaving workshop in Hakkari: two large upright wooden looms with half-woven kilims in deep "
               "red, indigo and ochre geometric patterns, balls of wool in baskets"),
    "tepe": ("Cilo manzarası", "a grassy hilltop above Hakkari at late afternoon facing the jagged snow-streaked peaks of the Cilo "
             "mountains, wildflowers, a wooden bench")},
   [
       S("07:30 sabah", "yol", ["mert", "coban"], "Koyunlar Önce",
         "Zap Vadisi yolunda yüzlerce koyun otobüsü durdurur. Mert iner ve çobanla birlikte sürüyü yolun kenarına yönlendirir.",
         "Mert walks among a river of sheep on the narrow road, gently waving his arms to guide them to the roadside; the shepherd walks ahead "
         "with his staff and laughs at Mert's clumsy technique.",
         [("coban", "Yavaş ol, koyun acele sevmez!", "laughing"),
          ("mert", "Kimse acele sevmiyor bu yolculukta!", "laughing back")],
         "slow crane-up from the sheep to the deep valley and the bus"),
       S("11:00 iç-gündüz", "lokanta", ["ali", "lokantaci"], "Otlu Peynir Dağda",
         "Hakkari'de bir lokanta 15 kilo otlu peynir alır; 15 kilo da takipçilere gider.",
         "The restaurant owner tastes the herb cheese with bread, nods and lifts the box onto his counter; Ali checks his phone, then writes two "
         "lines in his notebook.",
         [("lokantaci", "Van'ın otlusu buraya yakışır. On beş kilo bırak.", "satisfied"),
          ("ali", "On beşi de siparişle gitti. Otuz kilo bitti.", "pleased")],
         "static medium two-shot at the counter",
         t=U(30, "kg", 650, "satis", "Van otlu peyniri, lokanta ve takipçi siparişi ({adet} kg x {fiyat} TL)")),
       S("13:00 iç-gündüz", "atolye", ["mert", "ali", "gule"], "Renklerin Dili",
         "Kilim atölyesinde Gule Abla motiflerin anlamını anlatır: her desen bir dilek, her renk bir dağ bitkisinden.",
         "Gule passes the weft yarn through the loom and taps it down firmly with a wooden comb, then points to a geometric motif; Mert and Ali "
         "lean in close to the loom.",
         [("gule", "Bu desen bereket demek. Kırmızısı da dağdaki kökten gelir.", "gentle, proud"),
          ("ali", "Yani her kilim bir mektup gibi.", "fascinated")],
         "slow push-in to the loom and Gule's hands"),
       S("14:00 iç-gündüz", "atolye", ["mert", "gule"], "Altı Kilim",
         "Altı küçük kilim alırlar. Mert pazarlık etmeye kalkar, sonra emeği görüp vazgeçer.",
         "Gule unrolls six small kilims one by one on the floor; Mert opens his mouth to bargain, looks at the loom, closes his mouth and hands "
         "over the money with both hands.",
         [("gule", "Tanesi üç bin beş yüz. Bir tanesi bir ay sürer.", "calm"),
          ("mert", "Bir ay mı? O zaman pazarlık yok abla.", "humbled")],
         "static wide shot from above the kilims",
         t=U(6, "kilim", 3500, "alis", "El dokuması Hakkari kilimi, küçük boy ({adet} x {fiyat} TL)")),
       S("18:00 ikindi", "tepe", ["mert", "ali"], "Cilo'ya Karşı",
         "Cilo Dağları'na bakan tepede otururlar. Sessizlik, rüzgâr ve dağlar.",
         "Mert and Ali sit on the wooden bench facing the jagged mountains, sharing a bottle of water; the wind moves the grass and their hair; "
         "Ali leans back and closes his eyes.",
         [("ali", "Bu dağları görmeden ölseydim eksik kalırdı.", "peaceful"),
          ("mert", "Borç olmasa gelmezdik. Hayırlı borçmuş.", "half-joking, warm")],
         "slow lateral dolly behind the bench toward the peaks", h="serin",
         t=T("yemek", 700, "Öğle ve akşam yemeği")),
       S("19:30 gün batımı", "tepe", ["mert", "ali"], "Üç Şehir Kaldı",
         "Ali'nin telefonuna Cemil Bey'den ilk mesaj gelir: 'Üç şehir kaldı. Hesap?' İkisi de birden dikleşir.",
         "Ali's phone buzzes; he reads, sits up straight and turns the screen to Mert; Mert reads it, stands up and starts counting on his "
         "fingers while Ali opens the notebook.",
         [("ali", "Cemil Bey: 'Üç şehir kaldı. Hesap?'", "reading, tense"),
          ("mert", "Bitlis, Muş, Bingöl. Elli bini çıkaracağız.", "determined")],
         "slow push-in from the side", h="serin",
         t=[T("konaklama", 1200, "Otel, 1 gece"), U(2, "bilet", 500, "ulasim", "Hakkari-Van otobüsü ({adet} x {fiyat} TL)")]),
   ],
   misafir={"coban": ("ÇOBAN", "SHEPHERD, a 60-year-old Turkish man, lean and weathered, a thick black-and-grey mustache, a felt vest, a "
                      "wooden staff", "elderly male voice, hearty laugh, Eastern Turkish"),
            "lokantaci": ("LOKANTACI", "RESTAURANT OWNER, a 44-year-old Turkish man, short and broad, a short black beard, a white apron",
                          "adult male voice, friendly"),
            "gule": ("GULE ABLA", "GULE, a 46-year-old Turkish weaver woman, calm and strong, a deep purple headscarf, a long embroidered dress "
                     "and a wool vest, silver bracelets", "middle-aged female voice, gentle and proud Turkish")},
   ay=AY, hava="açık", urun="Hakkari kilimi, dağ balı, otlu peynir; Zap Vadisi, Cilo Dağları, Meydan Medresesi",
   sponsor="El dokuması kilim, bal ya da doğa turizmi alanında",
   kapak=("atolye", ["mert", "ali", "gule"], "Mert and Ali hold up a vivid red-and-indigo Hakkari kilim between them, Gule smiling at the loom "
          "behind, bright window light", "Kırmızı-lacivert bir Hakkari kilimini tutan Mert ve Ali."),
   yakinda=("yol", ["mert"], "A lone silhouette standing in the middle of a narrow mountain road filled with hundreds of sheep, a deep valley "
            "below, morning haze", "Sürünün ortasında, dağ yolunda yalnız bir silüet."),
   tiktok="Hakkari yolunda koyun trafiği 🐑 ve 1 ayda dokunan kilim #JozhStudios",
   ig=("Zap Vadisi'nde yüzlerce koyun otobüsümüzü durdurdu, Mert çobana yardım etti. 🐑\n\n"
       "Gule Abla'nın atölyesinde öğrendik: bir kilim bir ayda dokunuyor, her desen bir dilek. Pazarlık yapmadık. 🧶\n\n"
       "Sonra Cemil Bey yazdı: 'Üç şehir kaldı. Hesap?' Kasa: {KASA}"),
   tags=["#Hakkari", "#Kilim", "#ZapVadisi"],
   son="Cemil Bey yazar: 'Üç şehir kaldı. Hesap?'",
   teaser="Koyun trafiği, bir ayda dokunan kilimler ve Cemil Bey'in ilk mesajı. Bölüm 17: Hakkari. Pek yakında.")

# ======================================================================= 18 BİTLİS
EP(18, "Bitlis", "Feribotta Şafak",
   "Van Gölü'nü feribotla geçerler; Nemrut Krater Gölü, Ahlat'ın taşları ve büryan.",
   "Gece Van'a dönen ikili, sabah Van-Tatvan feribotuyla gölü geçer; güvertede kalan otlu peynir takipçilere satılır. Tatvan'dan Nemrut "
   "Krater Gölü'ne çıkıp dünyanın en büyük krater göllerinden birine bakarlar. Ahlat Selçuklu Meydan Mezarlığı'nın oymalı dev mezar "
   "taşlarının arasında sessizce yürürler. Ahlat'ta butik bir otel üç kilimi alır. Bitlis'te kuyuda pişen büryan kebabını yerken taksit "
   "hesabı tutar.",
   {"feribot": ("Van-Tatvan feribotu", "the open deck of the large Van-Tatvan ferry at dawn crossing the vast calm deep-blue Lake Van, white "
                "metal railings, a lifeboat, distant mountains glowing pink"),
    "nemrut": ("Nemrut Krater Gölü", "the rim of the huge Nemrut volcanic crater above Tatvan: a deep blue lake far below inside a wide green "
               "caldera, rocky edges, wildflowers"),
    "ahlat": ("Ahlat Selçuklu Meydan Mezarlığı", "the Seljuk cemetery of Ahlat: hundreds of tall, weathered, intricately carved stone "
              "tombstones standing in golden grass, Lake Van in the distance"),
    "otel": ("Ahlat'ta butik otel", "the stone-walled lobby of a small boutique hotel in Ahlat: a wooden reception desk, a bare stone floor "
             "waiting for rugs, a window to the lake"),
    "buryan": ("Büryan kebapçısı", "a traditional büryan kebab shop in Bitlis: a deep stone pit oven in the floor from which tender lamb is "
               "lifted on hooks, simple tables, white tiles")},
   [
       S("06:30 şafak", "feribot", ["mert", "ali"], "Gölün Ortasında",
         "Van-Tatvan feribotunun güvertesindedirler. Ali kalan 30 kilo otlu peynirin siparişlerini toplar.",
         "Mert leans on the ferry railing watching the sunrise over the lake, wrapped in the cool wind; Ali beside him types on his phone, then "
         "holds it up to show Mert with a grin.",
         [("mert", "Deniz gibi Ali. Ama tatlı değil, sodalı bir göl bu.", "wondering"),
          ("ali", "Kalan otlu peynir de sodalı gibi gitti: otuz kilo!", "playful")],
         "slow dolly along the railing toward the sunrise", h="serin",
         t=[U(30, "kg", 650, "satis", "Van otlu peyniri, takipçi siparişi ({adet} kg x {fiyat} TL)"),
            U(2, "bilet", 150, "ulasim", "Van-Tatvan feribotu (2 x 150 TL)")]),
       S("09:30 sabah", "nemrut", ["mert", "ali"], "Kraterin Kıyısında",
         "Nemrut Krater Gölü'nün kenarındadırlar. Aşağıda koca bir kraterin içinde masmavi bir göl.",
         "Mert and Ali walk to the edge of the crater rim and stop; the camera rises past them to reveal the enormous caldera and the blue lake "
         "inside; Mert puts his hands on his head in disbelief.",
         [("mert", "Bir yanardağın içinde göl var Ali!", "amazed"),
          ("ali", "Dünyanın en büyük krater göllerinden biri.", "awed")],
         "slow crane-up over their shoulders revealing the crater"),
       S("12:00 öğle", "ahlat", ["mert", "ali"], "Taşların Sessizliği",
         "Ahlat'ın Selçuklu mezar taşları arasında yürürler. Mert'in hızlı adımları yavaşlar.",
         "Mert and Ali walk slowly between the tall carved tombstones; Mert stops and runs his fingertips over the intricate stone carving; "
         "Ali stands still beside him in silence.",
         [("ali", "Sekiz yüz yıl önce biri bunu oymuş. Hiç acele etmemiş.", "quiet"),
          ("mert", "Ben de acele etmeyeceğim. Söz.", "soft")],
         "slow tracking shot between the tombstones"),
       S("14:00 iç-gündüz", "otel", ["ali", "otelci"], "Kilimler Yuvada",
         "Ahlat'ta yeni açılan butik bir otel lobisi için üç Hakkari kilimi alır.",
         "The hotel owner unrolls a red-and-indigo kilim across the bare stone floor and steps back to admire it; Ali stands at the edge of the "
         "rug holding the other two rolled under his arm.",
         [("otelci", "Lobinin eksik parçası buymuş. Üçünü de alıyorum.", "delighted"),
          ("ali", "Tanesi altı bin. Dokuyan elleri de anlatın misafirlerinize.", "warm")],
         "slow crane-down onto the unrolled kilim",
         t=U(3, "kilim", 6000, "satis", "Hakkari kilimi, butik otele ({adet} x {fiyat} TL)")),
       S("19:00 akşam", "buryan", ["mert", "ali", "buryanci"], "Kuyudan Kebap",
         "Bitlis'te büryan kebabını kuyudan çıkarırken izlerler. Ali hesabı söyler: taksit için para var.",
         "The büryan master lifts a hook of tender roasted lamb out of the stone pit and steam rises; Mert's jaw drops; Ali leans toward Mert and "
         "shows the notebook page.",
         [("buryanci", "Büryan sabır ister, kuyuda saatlerce pişer.", "proud"),
          ("ali", "Taksitin parası şimdiden kasada Mert.", "quiet, relieved")],
         "static medium three-shot by the pit",
         t=T("yemek", 800, "Büryan kebabı (2 kişi)")),
       S("22:00 gece", "buryan", ["mert", "ali"], "Muş Ovası",
         "Gece çıkarken Mert yarın Muş'ta 'ticaret yapmayacaklarını', sadece insanlarla tanışacaklarını söyler. Ali şaşırır.",
         "Mert and Ali step out of the kebab shop onto the dark street; Mert stretches his arms and says something unexpected; Ali stops walking "
         "and stares at him.",
         [("mert", "Yarın Muş'ta acele yok. Sadece insan tanıyacağız.", "calm, surprising"),
          ("ali", "Sen Mert misin, yoksa Ahlat'ın taşı mı değdi?", "amazed, teasing")],
         "static medium two-shot on the street",
         t=[T("konaklama", 1200, "Otel, 1 gece"), U(2, "bilet", 300, "ulasim", "Tatvan-Muş otobüsü ({adet} x {fiyat} TL)")]),
   ],
   misafir={"otelci": ("OTEL SAHİBİ", "HOTEL OWNER, a 39-year-old Turkish woman, elegant, short black hair, a cream linen shirt and dark "
                       "trousers", "adult female voice, warm, refined Turkish"),
            "buryanci": ("BÜRYAN USTASI", "BÜRYAN MASTER, a 55-year-old Turkish man, broad, a grey stubble, a white apron and a cap",
                         "mature male voice, proud, Bitlis Turkish")},
   ay=AY, hava="açık", urun="Büryan kebabı, bal, Ahlat taşı; Nemrut Krater Gölü, Ahlat Selçuklu Meydan Mezarlığı, Van Gölü",
   sponsor="Büryan, turizm ya da yöresel ürün alanında",
   kapak=("nemrut", ["mert", "ali"], "Mert and Ali stand on the edge of the vast Nemrut crater rim, arms raised, the deep blue crater lake far "
          "below, epic wide view", "Nemrut kraterinin kenarında kollarını açan Mert ve Ali."),
   yakinda=("ahlat", ["mert"], "Mert's hand touching an ancient carved tombstone in low golden backlight, rows of tall stones fading into haze "
            "behind him", "Altın ışıkta oymalı bir mezar taşına dokunan el."),
   tiktok="Bir yanardağın içinde göl var! 🌋 Nemrut Krater Gölü #JozhStudios",
   ig=("Van Gölü'nü feribotla geçtik, güvertede otlu peynirin kalanı da satıldı. ⛴️\n\n"
       "Nemrut Krater Gölü'nde bir yanardağın içine baktık, Ahlat'ta 800 yıllık taşların arasında yürüdük ve Mert ilk kez 'acele etmeyeceğim' dedi. "
       "Büryan ise kuyudan çıktı! 🔥\n\nKasa: {KASA}"),
   tags=["#Bitlis", "#NemrutKraterGölü", "#Ahlat"],
   son="Mert, Muş'ta ticaret değil insan tanıyacaklarını söyler. Ali şaşkın.",
   teaser="Gölün ortasında şafak, bir yanardağın içinde göl ve sekiz yüz yıllık taşlar. Bölüm 18: Bitlis. Pek yakında.")

# ======================================================================= 19 MUŞ
EP(19, "Muş", "Ovada Bir Gün",
   "Otobüs Muş Ovası'nda arızalanır; bir traktör, bir aile ve hasat yardımı.",
   "Otobüs ovanın ortasında arızalanınca bir traktörün römorkuna binerler. Traktördeki Şivan Abi'nin ailesinin tarlasında akşama kadar "
   "çalışır, yevmiye alırlar. Öğlen tarlada aileyle aynı sofrada yemek yerler. Kalan üç kilim, videoyu izleyen İstanbullu bir takipçiye "
   "satılır. Murat Nehri kıyısında Ali, Mert'e bir şey itiraf eder: babasının serası borç yüzünden satılık olabilir. Gece misafir "
   "oldukları evde sofrada tek bir lamba yanar.",
   {"yol": ("Muş Ovası yolu", "a straight road across the wide green Muş plain: fields of wheat, a broken-down white bus on the shoulder with "
            "its hood open, distant mountains"),
    "romork": ("Traktör römorku", "the open trailer of a red tractor driving slowly on a dirt road through the Muş plain, hay bales in the "
               "trailer, dust behind"),
    "tarla": ("Buğday tarlası", "a golden wheat field on the Muş plain at midday: sheaves of cut wheat, a tractor at the edge, a sofra "
              "cloth spread on the ground under a single tree"),
    "nehir": ("Murat Nehri kıyısı", "the bank of the Murat River near Muş at sunset: a wide calm river with reeds, poplars and the plain "
              "glowing gold"),
    "ev": ("Köy evi, sofra", "a simple village house in the Muş plain at night: a low round wooden table on a carpet, cushions, a single warm "
           "lamp, plates of bread and yogurt")},
   [
       S("08:30 sabah", "yol", ["mert", "ali", "sivan"], "Arıza",
         "Otobüs ovanın ortasında arızalanır. Yoldan geçen bir traktörün sürücüsü Şivan Abi onları römorka davet eder.",
         "Mert and Ali stand beside the broken bus with their bags; a red tractor slows down and stops beside them; Şivan leans out from the "
         "driver's seat and jerks his thumb toward the trailer; Mert grins at Ali.",
         [("sivan", "Otobüs bugün kalkmaz. Atlayın, köye gidiyorum!", "cheerful shout"),
          ("mert", "Ali, bu yolculuğun en iyi otobüsü bu.", "delighted")],
         "static wide shot from the roadside, slight push-in as the tractor stops"),
       S("09:00 sabah", "romork", ["mert", "ali"], "Saman Balyaları Üstünde",
         "Römorkta saman balyalarının üstünde ovayı geçerler. Rüzgâr, toz ve kahkaha.",
         "Mert and Ali sit on hay bales in the swaying open trailer as the tractor rolls along the dirt road; dust trails behind; Mert stretches "
         "his arms wide and Ali holds onto his bag, laughing.",
         [("ali", "Kasaya bir yazı ekleyelim: ulaşım, bedava.", "laughing"),
          ("mert", "Bedava değil, kahkaha karşılığı.", "laughing")],
         "smooth tracking shot from behind the trailer"),
       S("12:30 öğle", "tarla", ["mert", "ali", "sivan"], "Aynı Sofrada",
         "Şivan Abi'nin ailesinin buğday tarlasında öğlene kadar demet taşırlar; ağacın altındaki sofraya birlikte otururlar.",
         "Mert carries a sheaf of wheat on his shoulder to a pile and drops it, wiping sweat; Şivan waves them both toward the cloth spread under "
         "the tree where bread and yogurt wait; they sit down cross-legged.",
         [("sivan", "Emek yiyen ekmeği daha tatlı yer. Buyurun.", "warm"),
          ("ali", "Elinize sağlık abi, kollarım koptu ama değdi.", "tired, smiling")],
         "slow dolly-in from the field to the tree", h="sıcak"),
       S("16:00 ikindi", "tarla", ["mert", "ali", "sivan"], "Yevmiye ve Kilim",
         "Akşamüstü Şivan Abi zorla yevmiye verir. Aynı anda kalan üç kilim İstanbul'daki bir takipçiye satılır.",
         "Şivan presses folded banknotes into Mert's hand and closes his fingers over them when Mert tries to refuse; Ali's phone buzzes and he "
         "shows the screen to both with surprise.",
         [("sivan", "Alacaksın. Çalışanın hakkı yere düşmez.", "insistent"),
          ("ali", "Üç kilim İstanbul'a gidiyor, az önce satıldı.", "surprised")],
         "static medium three-shot in the field", h="sıcak",
         t=[T("diger_gelir", 2000, "Hasat yardımı yevmiyesi (2 kişi)"), U(3, "kilim", 6200, "satis", "Hakkari kilimi, İstanbul'daki takipçiye (3 x 6.200 TL)")]),
       S("19:30 gün batımı", "nehir", ["mert", "ali"], "Ali'nin İtirafı",
         "Murat Nehri kıyısında Ali itiraf eder: babasının serası borç yüzünden satılık olabilir. Bunu Mert'ten saklamıştır.",
         "Ali sits on the riverbank throwing small stones into the water; Mert sits down beside him; Ali speaks without looking at him, and Mert "
         "slowly turns his head toward Ali.",
         [("ali", "Babamın serası satılık olabilir Mert. Söylemedim, yükün yeter diye.", "quiet, ashamed"),
          ("mert", "Yükümüz ortak Ali. Antalya'ya varınca birlikte bakarız.", "firm, warm")],
         "slow push-in from across the river"),
       S("21:30 iç-gece", "ev", ["mert", "ali", "sivan"], "Tek Lamba",
         "Gece Şivan Abi'nin evinde misafir kalırlar. Sofrada tek bir lamba yanar. Ali taksit hesabını kontrol eder.",
         "Şivan sets a tea glass in front of each of them at the low table; Ali opens the notebook beside his glass and nods to Mert; Mert raises "
         "his tea glass toward Şivan.",
         [("ali", "Yarın Bingöl. Elli bin hazır.", "quiet, confident"),
          ("mert", "Şivan Abi, sen olmasan bugün yolda kalırdık.", "grateful")],
         "static medium three-shot at table height",
         t=U(2, "bilet", 300, "ulasim", "Muş-Bingöl otobüsü ({adet} x {fiyat} TL)")),
   ],
   misafir={"sivan": ("ŞİVAN ABİ", "ŞİVAN, a 41-year-old Turkish farmer, tall and strong, a sun-tanned friendly face, a black mustache, a "
                      "cap, a sweat-stained grey t-shirt and work trousers", "adult male voice, warm, cheerful Eastern Anatolian Turkish")},
   ay=AY, hava="açık", urun="Muş Ovası buğdayı, bal, yayla ürünleri; Malazgirt, Murat Nehri",
   sponsor="Tarım, bal ya da yayla ürünleri alanında",
   kapak=("romork", ["mert", "ali"], "Mert and Ali ride on hay bales in an open tractor trailer across a vast golden plain, Mert with arms wide "
          "open, Ali laughing, dust glowing in the sunlight", "Traktör römorkunda saman balyalarının üstünde gülen Mert ve Ali."),
   yakinda=("nehir", ["ali"], "Ali sitting alone on a riverbank at sunset seen from behind, throwing a small stone into glowing water, a second "
            "silhouette approaching", "Gün batımında nehir kıyısında yalnız oturan Ali."),
   tiktok="Otobüs bozuldu, traktöre bindik, buğday hasadı yaptık 🚜 #JozhStudios",
   ig=("Muş Ovası'nın ortasında otobüs bozuldu. Şivan Abi traktörüyle geldi: 'Atlayın!' 🚜\n\n"
       "Bütün gün tarlada çalıştık, aynı sofrada yemek yedik. Murat Nehri kıyısında Ali bana bir şey itiraf etti... 💔\n\nKasa: {KASA}. Yarın Bingöl: ilk taksit günü."),
   tags=["#Muş", "#MuşOvası", "#Hasat"],
   son="Ali'nin babasının serası satılık olabilir. Yarın Bingöl'de ilk taksit günü.",
   teaser="Bir arıza, bir traktör ve nehir kıyısında bir itiraf. Bölüm 19: Muş. Pek yakında.")

# ======================================================================= 20 BİNGÖL
EP(20, "Bingöl", "Yüzen Adalar ve İlk Taksit",
   "Sezon finali: Bingöl balı, yüzen adalar ve Cemil Bey'e giden ilk 50.000 TL.",
   "Bingöl'e varır varmaz Solhan'daki Yüzen Adalar'a giderler: göl üstünde sürüklenen çimenli adacıklara basıp sallanırlar. Dağdaki arıcı "
   "Rojhat Amca'dan Bingöl balının hikâyesini dinler, 50 kilo bal alırlar. Öğlen Bingöl'ün yöresel yemekleriyle karınlarını doyururlar. "
   "Akşamüstü bir bankanın önünde Ali, Cemil Bey'e ilk taksiti gönderir: 50.000 TL. Gece Cemil Bey'in cevabı gelir. Tek kelime: 'Gördüm.' "
   "Sezon biter; sıradaki durak Diyarbakır.",
   {"ada": ("Yüzen Adalar, Solhan", "the floating islands of Solhan in Bingöl: small grassy islands with reeds drifting slowly on a calm "
            "dark-green lake, a wooden jetty, green hills around"),
    "aricilik": ("Dağda arılık", "a mountainside apiary near Bingöl: rows of wooden beehives among wildflowers, a smoker, honey frames, "
                 "green mountains and blue sky"),
    "lokanta": ("Bingöl lokantası", "a simple restaurant in Bingöl: wooden tables, a window to the hills, a tray with stuffed dishes and bread"),
    "banka": ("Banka önü", "the sidewalk in front of a modern bank branch in Bingöl at late afternoon: a glass facade with frosted panels, an "
              "ATM, a small bench"),
    "teras": ("Otel terası", "a hotel rooftop terrace in Bingöl at night: plastic chairs, a low wall, city lights and dark mountains")},
   [
       S("09:00 sabah", "ada", ["mert", "ali"], "Ayağının Altında Ada",
         "Yüzen Adalar'da bir adacığa basarlar; ada yavaşça sürüklenir. Mert dengesini kaybedecek gibi olur.",
         "Mert steps from the wooden jetty onto a small floating grassy island; it sways and drifts slowly away; Mert wobbles with his arms out "
         "while Ali, still on the jetty, laughs and reaches out a hand.",
         [("mert", "Ali, ada gidiyor! Ben de gidiyorum!", "panicked laughing"),
          ("ali", "Elimi tut, taksit günü kaybolma!", "laughing")],
         "static wide shot from the jetty, slow push-in"),
       S("11:30 sabah", "aricilik", ["mert", "ali", "rojhat"], "Bingöl Balı",
         "Arıcı Rojhat Amca bal çerçevesini çıkarır: Bingöl balı yüksek dağ çiçeklerinden gelir.",
         "Rojhat lifts a dripping honey frame from a hive with slow calm movements, bees humming around; Mert holds his breath and steps back, "
         "Ali leans in to look at the golden comb.",
         [("rojhat", "Yayla çiçeği, temiz hava, sabır. Bingöl balının sırrı bu.", "calm, wise"),
          ("mert", "Amca, arılar bana bakıyor ama.", "nervous whisper")],
         "slow push-in to the honey frame in the sunlight"),
       S("12:30 öğle", "aricilik", ["ali", "rojhat"], "Elli Kilo",
         "Elli kilo süzme Bingöl balı alırlar. Ali sezonun en büyük alışını yaparken eli titremez.",
         "Rojhat sets large glass jars of golden honey into a wooden crate; Ali counts a thick stack of banknotes into his hand and both nod "
         "slowly.",
         [("rojhat", "Kilosu sekiz yüz. Bunu satan da utanmaz, yiyen de pişman olmaz.", "proud"),
          ("ali", "Elli kilo alıyoruz amca.", "steady")],
         "static medium two-shot by the hives",
         t=U(50, "kg", 800, "alis", "Bingöl balı, süzme ({adet} kg x {fiyat} TL)")),
       S("14:00 iç-gündüz", "lokanta", ["mert", "ali"], "Sezon Sofrası",
         "Öğlen yöresel yemeklerle sezonun son sofrasına otururlar ve on dört şehri sayarlar.",
         "Mert counts on his fingers while naming cities, runs out of fingers and borrows Ali's hand; Ali laughs and holds up his own fingers to "
         "continue.",
         [("mert", "Malatya, Elazığ, Tunceli... parmak yetmiyor!", "laughing"),
          ("ali", "On dört şehir. Bir tane de zarar.", "warm")],
         "static medium two-shot across the table",
         t=T("yemek", 600, "Öğle yemeği")),
       S("17:30 ikindi", "banka", ["mert", "ali"], "Elli Bin",
         "Banka önünde Ali ilk taksiti Cemil Bey'e gönderir. Mert onay tuşuna basmasını ister; Ali telefonu ona uzatır.",
         "Ali holds his phone with the transfer ready and offers it to Mert; Mert takes a breath and presses the screen with one finger; both "
         "stare at the phone, then exhale together.",
         [("ali", "Elli bin lira. Sen bas.", "solemn"),
          ("mert", "Bismillah... gitti.", "nervous, relieved")],
         "slow push-in to their faces lit by the phone",
         t=T("borc", 50000, "1. taksit: Cemil Bey (Doğu Anadolu sezonu sonu)")),
       S("22:00 gece", "teras", ["mert", "ali"], "Gördüm",
         "Gece terasta Cemil Bey'in cevabı gelir. Tek kelime: 'Gördüm.' Mert güler, Ali telefona bakmaya devam eder.",
         "Mert and Ali sit on plastic chairs on the dark terrace; Ali's phone lights up; he reads it, turns the screen toward Mert; Mert bursts "
         "out laughing and leans back, Ali keeps staring at the single word.",
         [("ali", "Cemil Bey cevap yazdı: 'Gördüm.'", "puzzled"),
          ("mert", "Cemil Abi'den bu, aşk mektubu sayılır!", "laughing")],
         "slow dolly-out revealing the city lights and dark mountains",
         t=[T("konaklama", 1100, "Otel, 1 gece"), U(2, "bilet", 250, "ulasim", "Bingöl-Diyarbakır otobüsü ({adet} x {fiyat} TL)")],
         kurgu="Sezon sonu kartı (kurguda): SEZON 1 BİTTİ · 14 İL · 1. TAKSİT ÖDENDİ"),
   ],
   misafir={"rojhat": ("ROJHAT AMCA", "ROJHAT, a 64-year-old Turkish beekeeper, slim, a white beard, calm eyes, a beekeeper's veil hat pushed "
                       "back, a light khaki shirt", "elderly male voice, calm and wise, Eastern Anatolian Turkish")},
   ay=AY, hava="açık", urun="Bingöl balı, yayla ürünleri; Yüzen Adalar (Solhan), Bingöl dağları",
   sponsor="Bal, arıcılık ya da doğa turizmi alanında",
   kapak=("ada", ["mert", "ali"], "Mert wobbles with arms out on a small floating grassy island drifting away from a wooden jetty, Ali laughing "
          "and reaching for him, calm green lake reflecting the sky", "Yüzen adada dengesini kaybeden Mert ve ona uzanan Ali."),
   yakinda=("teras", ["mert", "ali"], "Two faces lit only by a phone screen on a dark rooftop at night, city lights blurred behind, one of them "
            "laughing", "Gece terasında telefon ışığıyla aydınlanan iki yüz."),
   tiktok="Sezon finali: ilk 50.000 TL taksit gitti 💸 Cemil Abi'nin cevabı... #JozhStudios",
   ig=("Doğu Anadolu bitti! 14 il, bir zarar, bir kavga, sayısız dost. 🏔️\n\n"
       "Bingöl'de yüzen adaların üstünde sallandık, Rojhat Amca'dan Bingöl balı aldık ve ilk taksiti gönderdik: 50.000 TL. 💸\n\n"
       "Cemil Abi'nin cevabı tek kelime: 'Gördüm.' Kasa: {KASA}. Sezon 2: Güneydoğu başlıyor!"),
   tags=["#Bingöl", "#YüzenAdalar", "#SezonFinali"],
   son="Cemil Bey'in cevabı: 'Gördüm.' Sezon 2 Diyarbakır'da başlıyor.",
   teaser="Yüzen adalar, dağ balı ve Cemil Bey'e giden ilk elli bin. Bölüm 20: Bingöl, sezon finali. Pek yakında.")
