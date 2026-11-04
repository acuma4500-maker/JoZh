# -*- coding: utf-8 -*-
"""Sezon 6 · Fırtına ve Fındık · Karadeniz (Bölüm 57-74). Ekim sonu - Kasım. Kamyonetle.
Rota: Düzce → Bolu → Zonguldak → Bartın → Karabük → Kastamonu → Sinop → Samsun → Ordu → Giresun → Trabzon → Rize → Artvin
      → Bayburt → Gümüşhane → Tokat → Amasya → Çorum
KIYAFET: Bölüm 57'de yağmur başlayınca Düzce pazarından mont alırlar; bu bölümden itibaren kıyafet anahtarı "ceket".
Trabzon'da kurgusal bir şirketle YAZILI sözleşme: 300 'Karadeniz Kutusu' (250 g Rize çayı, 250 g Giresun tombul fındığı,
1 kavanoz Ordu fındık ezmesi, 200 g Safranbolu lokumu), kutusu 900 TL; %30 peşin (Trabzon), kalanı teslimde (Artvin)."""
from ortak import EP, S, T, U

AY = "Kasım"
K = "ceket"

# ======================================================================= 57 DÜZCE
EP(57, "Düzce", "Yağmur ve Mont",
   "Karadeniz'in ilk yağmuru, pazardan alınan montlar ve Marmara Kutusu'nun ikinci yarısı.",
   "Düzce'ye yağmurla girerler. Pazarda Mert siyah bir yağmurluk, Ali haki bir mont alır; artık bütün sezon bu kıyafetlerle yollardadırlar. "
   "Kalan 200 Marmara Kutusu'nun yarısı Düzce ve çevresinden gelen siparişlerle satılır. Güzeldere Şelalesi'nin yağmurla coşan sesinde "
   "yürürler. Akçakoca'da denize bakan bir lokantada balık yerler. Akşam Ali Karadeniz'in uzun rotasını haritaya çizer: on sekiz il.",
   {"pazar": ("Düzce pazarı", "a covered street market in Düzce on a rainy morning: stalls of jackets and raincoats under plastic awnings, "
              "rain dripping, wet pavement"),
    "depo": ("Kargo şubesi", "a small cargo office in Düzce: a counter, stacks of kraft gift boxes ready to ship, a scale, rain on the window"),
    "selale": ("Güzeldere Şelalesi", "the Güzeldere waterfall near Düzce after rain: a tall stream of white water falling into a green pool, "
               "lush wet forest, a wooden viewing platform"),
    "akcakoca": ("Akçakoca sahili", "a seaside fish restaurant in Akçakoca with big windows facing the stormy grey Black Sea, waves hitting "
                 "the breakwater"),
    "pansiyon": ("Pansiyon odası", "a warm guesthouse room in Düzce at night: rain on the window, wet jackets hanging, a paper map of the Black "
                 "Sea coast spread on the bed")},
   [
       S("09:00 sabah", "pazar", ["mert", "ali"], "Mont Zamanı",
         "Yağmurla Düzce'ye girerler. Pazarda Mert siyah bir yağmurluk, Ali haki bir mont alır ve hemen giyerler.",
         "Mert zips up a newly bought black hooded rain jacket over his black t-shirt and pulls up the hood; Ali buttons a dark olive quilted "
         "jacket; they look at each other under the dripping awning and nod approvingly.",
         [("mert", "Tişört dönemi bitti. Siyah yağmurluk, yine imzam.", "proud"),
          ("ali", "Haki mont. Karadeniz'e hazırız.", "satisfied")],
         "static medium two-shot under the awning", h="yağmur",
         t=T("diger_gider", 3800, "Yağmurluk ve mont (2 adet)"),
         kurgu="Kıyafet değişimi bu sahnede gösterilir; Bölüm 57'den itibaren karakter tarifleri mont ile kullanılır."),
       S("11:00 iç-gündüz", "depo", ["mert", "ali"], "Yüz Kutu",
         "Kalan 200 Marmara Kutusu'nun 100'ü siparişle satılır, kargo şubesinden gönderilir.",
         "Mert carries a stack of kraft boxes onto the cargo counter while Ali checks a list on his phone and tapes shipping labels; the clerk, "
         "out of focus, scans the boxes.",
         [("ali", "Yüz kutu, yüz adres. Kalan yüz Bolu'ya.", "organized"),
          ("mert", "Kural iki tamam: hepsinin parası önceden geldi.", "proud")],
         "static medium shot at the counter",
         t=[U(100, "kutu", 800, "satis", "Marmara Kutusu, takipçi siparişi ({adet} x {fiyat} TL)"), U(100, "kutu", 40, "diger_gider", "Kargo, 100 kutu (100 x 40 TL)")]),
       S("13:30 öğle", "selale", ["mert", "ali"], "Yağmurla Coşan Şelale",
         "Güzeldere Şelalesi yağmurla coşmuştur. Yeni montlarıyla ıslak ormanda yürürler.",
         "Mert and Ali stand on the wooden platform in front of the roaring waterfall with their hoods up; spray blows toward them; Mert opens "
         "his arms to feel the spray and Ali pulls his hood tighter, laughing.",
         [("mert", "Mont alınca yağmur bile güzel!", "shouting over the water"),
          ("ali", "Bunu Sapanca'da söylemiyordun!", "laughing")],
         "slow crane-down from the waterfall to the platform", h="yağmur"),
       S("16:00 iç-gündüz", "akcakoca", ["mert", "ali"], "Fırtınalı Deniz",
         "Akçakoca'da fırtınalı Karadeniz'e bakan bir lokantada balık yerler.",
         "Mert and Ali eat grilled fish at a window table while big grey waves crash against the breakwater outside; Mert flinches at a loud wave "
         "and Ali laughs.",
         [("ali", "Karadeniz'in denizi Akdeniz'e benzemiyor.", "watching the waves"),
          ("mert", "Bu deniz bağırıyor Ali, Akdeniz fısıldıyordu.", "impressed")],
         "static medium two-shot at the window, waves behind",
         t=T("yemek", 900, "Balık (2 kişi)")),
       S("21:00 iç-gece", "pansiyon", ["mert", "ali"], "On Sekiz İl",
         "Gece Ali Karadeniz rotasını haritaya çizer: Düzce'den Çorum'a on sekiz il.",
         "Ali draws a long line along the coast on the paper map spread on the bed while Mert counts the dots aloud with his finger; rain taps on "
         "the window and their wet jackets drip on hooks.",
         [("mert", "On sekiz! Bu sezon bir yıl sürer!", "overwhelmed"),
          ("ali", "Bir ay sürer. Kış gelmeden dağları geçmeliyiz.", "serious")],
         "top-down shot over the map", h="yağmur",
         t=[T("konaklama", 1200, "Pansiyon, 1 gece"), T("ulasim", 800, "Yakıt: Düzce-Bolu")]),
       S("22:00 iç-gece", "pansiyon", ["mert", "ali"], "Bir Söz Daha",
         "Işığı kapatmadan önce Mert bir şey söyler: bu sezon her kararı birlikte vereceklerdir. Ali gülümser.",
         "Mert reaches for the lamp, stops and turns to Ali with a serious face; Ali, already lying down, opens one eye and smiles; Mert switches "
         "off the lamp.",
         [("mert", "Bu sezon her karar ortak. Yazılı olmasına gerek yok... ama yaz istersen.", "sincere, joking"),
          ("ali", "Yazdım bile.", "sleepy smile")],
         "static medium two-shot, the lamp goes off"),
   ],
   ay=AY, hava="yağmur", kiyafet=K, urun="Fındık, Akçakoca balığı; Güzeldere Şelalesi, Konuralp",
   sponsor="Fındık, balık ya da doğa turizmi alanında",
   kapak=("pazar", ["mert", "ali"], "Mert in a new black hooded rain jacket and Ali in a dark olive quilted jacket pose proudly under a dripping "
          "market awning in the rain, like a fashion shoot", "Pazarda yeni montlarıyla poz veren Mert ve Ali."),
   yakinda=("akcakoca", ["mert"], "A huge grey storm wave crashing against a breakwater seen through a rain-streaked window, Mert's silhouette "
            "flinching inside", "Yağmurlu camın ardında dalgaya irkilen bir silüet."),
   tiktok="Karadeniz'e girdik: tişört dönemi bitti 🧥🌧️ #JozhStudios",
   ig=("Karadeniz bizi yağmurla karşıladı. 🌧️ Düzce pazarından mont aldık: Mert siyah yağmurluk (yine imza 😂), Ali haki mont.\n\n"
       "Marmara Kutusu'nun 100'ü daha gitti. Güzeldere Şelalesi coşmuş, Akçakoca'da deniz bağırıyor.\n\nOn sekiz il, bir ay, kış gelmeden. Kasa: {KASA}"),
   tags=["#Düzce", "#Akçakoca", "#Karadeniz"],
   son="On sekiz il ve kış gelmeden aşılması gereken dağlar.",
   teaser="İlk yağmur, yeni montlar ve on sekiz ilik bir harita. Bölüm 57: Düzce. Pek yakında.")

# ======================================================================= 58 BOLU
EP(58, "Bolu", "Aşçılar Diyarı",
   "Mengen'de aşçı ustası, Yedigöller'de sonbahar ve son Marmara kutuları.",
   "Bolu'da sabah kalan 100 Marmara Kutusu'nun siparişleri kapanır. Ünlü aşçılarıyla bilinen Mengen'de bir aşçı ustanın mutfağında Mert "
   "soğan doğramayı öğrenir, Ali hesap yapar gibi ölçü tutar. Yedigöller'in kırmızı-sarı sonbahar ormanında yürürler; göllerin sessizliği "
   "ikisini de susturur. Abant'ta gece ateş başında Mert bir soru sorar: 'Borç bitince ne olacağız?'",
   {"kargo": ("Bolu kargo şubesi", "a small cargo office in Bolu with stacks of kraft boxes, a counter and a scale"),
    "mutfak": ("Mengen'de aşçı mutfağı", "a professional kitchen in Mengen: steel counters, big pots steaming, rows of knives, a master chef "
               "teaching at a wooden board full of chopped onions"),
    "yedigol": ("Yedigöller", "Yedigöller National Park in autumn: a still dark lake reflecting a forest blazing in red, orange and yellow "
                "leaves, mist over the water, a wooden footbridge"),
    "abant": ("Abant, ateş başı", "a lakeside spot at Abant at night: a small fire in a stone fire pit, two camping chairs, the dark lake and "
              "pine forest, cold breath visible")},
   [
       S("09:00 iç-gündüz", "kargo", ["mert", "ali"], "Son Yüz Kutu",
         "Kalan 100 Marmara Kutusu'nun siparişleri kapanır ve gönderilir.",
         "Ali places the last kraft box on the cargo scale and taps the counter twice; Mert crosses an item off a paper list with a big flourish.",
         [("ali", "Beş yüz kutunun beş yüzü de gitti.", "relieved"),
          ("mert", "İstanbul'un kaybını kutular kapattı.", "proud")],
         "static medium two-shot at the counter",
         t=[U(100, "kutu", 800, "satis", "Marmara Kutusu, takipçi siparişi ({adet} x {fiyat} TL)"), U(100, "kutu", 40, "diger_gider", "Kargo, 100 kutu (100 x 40 TL)")]),
       S("11:30 iç-gündüz", "mutfak", ["mert", "asci"], "Soğan Doğramak",
         "Mengen'de aşçı usta Mert'e soğan doğramayı öğretir. Mert ağlar, usta güler.",
         "The master chef guides Mert's hand on a big knife chopping an onion into fine pieces; Mert's eyes water heavily; the chef laughs and "
         "taps the board with the back of his own knife.",
         [("asci", "Bıçağı sen yönet, soğan seni yönetmesin.", "laughing master"),
          ("mert", "Usta, soğan beni Kars'taki peynirciden beter ağlattı.", "tearful, comic")],
         "slow push-in on the cutting board"),
       S("12:30 iç-gündüz", "mutfak", ["ali", "asci"], "Ölçü",
         "Usta, Ali'nin baharatları gram gram tarttığını görünce takdir eder: 'Mutfak da ticaret gibi, ölçü ister.'",
         "Ali measures spices on a small kitchen scale with great care and writes the numbers down; the chef looks over his shoulder, raises his "
         "eyebrows and pats his back.",
         [("asci", "Mutfak da ticaret gibi, ölçü ister. Sen iyi aşçı olurdun.", "approving"),
          ("ali", "Ben ölçerim, Mert tadına bakar.", "smiling")],
         "static medium two-shot at the counter",
         t=T("yemek", 900, "Mengen'de öğle yemeği")),
       S("15:30 ikindi", "yedigol", ["mert", "ali"], "Kırmızı Orman",
         "Yedigöller'de kırmızı ve sarı sonbahar ormanında yürürler. Göllerin sessizliği ikisini de susturur.",
         "Mert and Ali walk slowly across the wooden footbridge over the still lake that mirrors the blazing red and yellow forest; mist rises "
         "from the water; Mert stops and simply looks, silent.",
         [], "slow crane-up from the footbridge revealing the reflected forest", h="sis"),
       S("21:00 gece", "abant", ["mert", "ali"], "Borç Bitince",
         "Abant'ta ateş başında Mert bir soru sorar: borç bitince ne olacaklar?",
         "Mert and Ali sit in camping chairs wrapped in their jackets beside a small fire; Mert pokes the fire with a stick and asks without "
         "looking up; Ali looks at the flames for a long moment.",
         [("mert", "Borç bitince ne olacağız Ali? Biz?", "thoughtful"),
          ("ali", "Kutu var. Marka var. Belki biz yeni başlıyoruz.", "hopeful")],
         "slow push-in through the fire to their faces", h="serin"),
       S("22:00 gece", "abant", ["mert", "ali"], "Kamyonet Kasası",
         "Ateş sönerken Ali kasayı hesaplar: Karadeniz'e iyi girmişlerdir.",
         "Ali opens the notebook by the firelight and shows Mert the total; Mert whistles softly and throws a last stick onto the dying fire.",
         [("ali", "Kasa yolculuğun en iyi yerinde.", "pleased"),
          ("mert", "O zaman iyi bir iş daha bulalım. Ortak kararla.", "smiling")],
         "static medium two-shot by the fire",
         t=[T("konaklama", 1400, "Abant'ta pansiyon, 1 gece"), T("ulasim", 900, "Yakıt: Bolu-Zonguldak")]),
   ],
   misafir={"asci": ("AŞÇI USTA", "MASTER CHEF, a 62-year-old Turkish man from Mengen, broad, a white chef's jacket and tall white hat, a "
                     "neat grey mustache, a towel on his shoulder", "elderly male voice, laughing master, Bolu Turkish")},
   ay=AY, hava="serin", kiyafet=K, urun="Mengen aşçıları, Bolu peyniri ve keşi; Yedigöller, Abant Gölü",
   sponsor="Aşçılık, yöresel mutfak ya da doğa turizmi alanında",
   kapak=("yedigol", ["mert", "ali"], "Mert and Ali stand on a wooden footbridge over a still lake mirroring a blazing red-and-gold autumn forest, "
          "mist on the water, breathtaking", "Kırmızı-sarı ormanı yansıtan gölün üstünde köprüde Mert ve Ali."),
   yakinda=("abant", ["mert", "ali"], "Two faces lit only by a small fire in a dark forest by a lake, cold breath visible, one staring into the "
            "flames asking a question", "Karanlık göl kıyısında yalnızca ateşle aydınlanan iki yüz."),
   tiktok="Mengen'de soğan beni ağlattı 🧅😭 Yedigöller'de sonbahar #JozhStudios",
   ig=("500 Marmara Kutusu'nun hepsi gitti! İstanbul'un kaybını kutular kapattı. 📦\n\n"
       "Mengen'de aşçı usta Mert'e soğan doğramayı öğretti (Mert ağladı 🧅). Yedigöller'de kırmızı orman göle düşmüştü. 🍁\n\n"
       "Abant'ta ateş başında Mert sordu: 'Borç bitince ne olacağız?' Kasa: {KASA}"),
   tags=["#Bolu", "#Yedigöller", "#Mengen"],
   son="Mert: 'Borç bitince ne olacağız?' Ali: 'Belki biz yeni başlıyoruz.'",
   teaser="Bir aşçı mutfağı, kırmızı bir orman ve ateş başında bir soru. Bölüm 58: Bolu. Pek yakında.")

# ======================================================================= 59 ZONGULDAK
EP(59, "Zonguldak", "Kömürün Emeği",
   "Maden müzesi, bir madenci ailesinin sofrası ve Devrek bastonları.",
   "Zonguldak'ta sabah maden müzesinde yer altındaki galerilerin bir benzerine inerler; baretli bir emekli madenci, kömürün nasıl "
   "çıkarıldığını anlatır. Öğlen aynı madencinin evinde, ailesinin sofrasında yemek yerler. Devrek'te el oyması bastonları yapan bir ustadan "
   "40 baston alırlar. Akşam Gökgöl Mağarası'nın serin damlalarının altında Mert, madencinin sözünü tekrar eder: 'Biz yerin altında "
   "çalışırız ki siz yerin üstünde ısınasınız.'",
   {"muze": ("Maden müzesi galerisi", "a replica underground mine gallery in a mining museum in Zonguldak: low tunnel supported by wooden and "
             "steel beams, rail tracks, a coal cart, helmet lamps, dim light"),
    "ev": ("Madenci evi", "the modest home of a retired miner in Zonguldak: a small living room with a low table set for lunch, a coal stove, "
           "family photos of miners on the wall"),
    "devrek": ("Devrek baston atölyesi", "a walking-cane workshop in Devrek: carved wooden canes with ornate handles hanging on the walls, "
               "a lathe, wood shavings, a warm stove"),
    "magara": ("Gökgöl Mağarası", "inside Gökgöl Cave near Zonguldak: illuminated stalactites and stalagmites, wet rock walls, dripping water, "
               "a metal walkway")},
   [
       S("09:00 iç-gündüz", "muze", ["mert", "ali", "madenci"], "Yerin Altında",
         "Maden müzesinde galerinin benzerine inerler. Emekli madenci Recep Abi kömürün nasıl çıkarıldığını anlatır.",
         "Recep, wearing an old miner's helmet with a lamp, walks ahead through the low tunnel and taps a wooden support beam; Mert and Ali follow "
         "him bent over, their faces lit by his helmet lamp.",
         [("madenci", "Burada başını eğmeyen başını yarar. Yer altı saygı ister.", "serious, kind"),
          ("mert", "Abi, siz otuz yıl böyle mi çalıştınız?", "hushed, respectful")],
         "slow tracking shot behind them through the tunnel"),
       S("10:00 iç-gündüz", "muze", ["mert", "ali", "madenci"], "Isınasınız Diye",
         "Recep Abi bir cümle söyler; ikisi de susar.",
         "Recep stops beside the coal cart, takes off his helmet and holds it against his chest; Mert and Ali stand still, listening, the lamp "
         "light flickering softly on the black walls.",
         [("madenci", "Biz yerin altında çalışırız ki siz yerin üstünde ısınasınız.", "quiet, proud")],
         "slow push-in to Recep's face"),
       S("12:30 iç-gündüz", "ev", ["mert", "ali", "madenci"], "Madenci Sofrası",
         "Recep Abi'nin evinde, ailesinin hazırladığı sofrada yemek yerler. Duvarda madenci fotoğrafları vardır.",
         "Recep ladles soup into bowls at the low table and passes them; Mert looks at the miners' photos on the wall; Ali accepts his bowl with "
         "both hands.",
         [("madenci", "Babam da dedem de madenciydi. Hepsi bu duvarda.", "proud"),
          ("ali", "Ellerinize sağlık. Bu sofrayı unutmayacağız.", "grateful")],
         "static medium three-shot at the table"),
       S("15:30 iç-gündüz", "devrek", ["mert", "ali", "bastoncu"], "Devrek Bastonu",
         "Devrek'te baston ustası el oyması bastonları gösterir. Kırk baston alırlar.",
         "The cane maker turns a wooden cane on the lathe, then holds up a finished cane with a carved handle; Mert tries it, walks a few steps "
         "like an old man, and Ali laughs while counting money.",
         [("bastoncu", "Her baston bir dost. Kırk tane, tanesi altı yüz.", "warm"),
          ("mert", "Bunu Hatice Sultan'a götüreceğim. Anneme yani.", "playful, warm")],
         "slow push-in on the carved handle",
         t=[U(40, "baston", 600, "alis", "El oyması Devrek bastonu ({adet} x {fiyat} TL)"), T("yemek", 400, "Çay ve simit")]),
       S("18:00 iç-gündüz", "magara", ["mert", "ali"], "Damla Damla",
         "Gökgöl Mağarası'nda sarkıtların altında yürürler. Damlalar binlerce yılda taş olmuştur.",
         "Mert and Ali walk slowly along the metal walkway under glowing stalactites; a drop falls onto Mert's hood; he looks up, then at Ali.",
         [("ali", "Her damla binlerce yılda taş olmuş.", "awed"),
          ("mert", "Recep Abi'nin sözü gibi. Emek görünmez ama birikir.", "thoughtful")],
         "slow crane-up along the stalactites"),
       S("21:00 akşam", "devrek", ["mert", "ali"], "Kime Satacağız?",
         "Akşam Ali sorar: kırk bastonu kime satacaklar? Mert'in cevabı hazırdır: yaşlıları seven torunlara.",
         "Mert leans on a carved cane by the warm stove with a big grin; Ali holds his notebook, skeptical, then laughs as Mert pretends to be "
         "an elderly salesman.",
         [("ali", "Kırk bastonu kime satacağız?", "skeptical"),
          ("mert", "Dedesini seven torunlara, evlat. Bartın'da başlarız.", "elderly voice, comic")],
         "static medium two-shot by the stove",
         t=[T("konaklama", 1100, "Pansiyon, 1 gece"), T("ulasim", 700, "Yakıt: Zonguldak-Bartın")]),
   ],
   misafir={"madenci": ("RECEP ABİ", "RECEP, a 62-year-old retired Turkish coal miner, stocky, a deeply lined face, a grey mustache, coal-darkened "
                        "nails, an old miner's helmet with a lamp, a dark work jacket", "mature male voice, deep, proud, Zonguldak Turkish"),
            "bastoncu": ("BASTON USTASI", "CANE MAKER, a 70-year-old Turkish man, thin, a white beard, a flat cap, a brown work apron covered "
                         "in wood shavings", "elderly male voice, warm")},
   ay=AY, hava="bulutlu", kiyafet=K, urun="Taşkömürü madenciliği, Devrek bastonu; Gökgöl Mağarası",
   sponsor="Devrek bastonu ya da maden kültürü turizmi alanında",
   kapak=("muze", ["mert", "ali", "madenci"], "In a low mine tunnel lit only by a helmet lamp, a retired miner holds his helmet to his chest "
          "while Mert and Ali listen respectfully, coal walls glistening", "Maden galerisinde baretini göğsüne bastıran madenci ve dinleyen Mert ile Ali."),
   yakinda=("magara", ["mert"], "A single water drop falling from a glowing stalactite toward Mert's upturned face in a dark cave",
            "Parlayan sarkıttan düşen tek bir damla ve yukarı bakan bir yüz."),
   tiktok="'Biz yerin altında çalışırız ki siz ısınasınız' ⛏️ #JozhStudios",
   ig=("Zonguldak'ta emekli madenci Recep Abi bizi galeriye götürdü: 'Biz yerin altında çalışırız ki siz yerin üstünde ısınasınız.' ⛏️🖤\n\n"
       "Ailesinin sofrasında yemek yedik. Devrek'te el oyması 40 baston aldık. Gökgöl Mağarası'nda damlaların binlerce yılda taş olduğunu gördük.\n\nKasa: {KASA}"),
   tags=["#Zonguldak", "#Madenci", "#DevrekBastonu"],
   son="Kırk bastonu dedesini seven torunlara satacaklar.",
   teaser="Yerin altında bir galeri, bir madenci sofrası ve kırk baston. Bölüm 59: Zonguldak. Pek yakında.")

# ======================================================================= 60 BARTIN
EP(60, "Bartın", "Amasra'nın Kaşıkları",
   "Amasra'da çekiciler çarşısı, ahşap kaşıklar, balık ve ilk baston satışı.",
   "Bartın'ın ahşap evlerinin arasından Amasra'ya inerler. Çekiciler Çarşısı'nda ahşap oymacılarının kaşıklarını görür, 100 el yapımı "
   "ahşap kaşık alırlar. Bir torun, dedesi için baston arar; 20 baston iki gün içinde siparişle satılır. Amasra salatası ve balık yerler. "
   "Akşam Amasra kalesinin surlarında rüzgâra karşı dururlar. Ali'nin telefonuna bir mesaj gelir: Trabzon'da bir şirket kutuları "
   "görmüştür ve görüşmek istemektedir.",
   {"bartin": ("Bartın ahşap evleri", "a street of old wooden Ottoman houses in Bartın with bay windows, a river, autumn trees, light rain"),
    "carsi": ("Amasra Çekiciler Çarşısı", "the craftsmen's lane in Amasra: tiny shops full of hand-carved wooden spoons, ladles and boxes, "
              "a craftsman carving at his doorway, cobbled street"),
    "lokanta": ("Amasra balık lokantası", "a fish restaurant in Amasra with a view of the small harbor and the castle peninsula, plates of "
                "fried fish and Amasra salad"),
    "kale": ("Amasra kalesi surları", "the old castle walls of Amasra on a rocky peninsula at sunset: stone walls, a small arched bridge, the "
             "rough Black Sea on both sides, wind")},
   [
       S("09:00 sabah", "bartin", ["mert", "ali"], "Ahşap Evler",
         "Bartın'ın ahşap evlerinin arasında hafif yağmurda yürürler.",
         "Mert and Ali walk along the riverside street of old wooden houses with their hoods up; Mert knocks gently on an old wooden door frame "
         "as he passes, admiring it.",
         [("mert", "Bu evler yüz yıldır yağmura dayanıyor.", "admiring"),
          ("ali", "Ahşap iyi bakılırsa taştan uzun yaşar.", "thoughtful")],
         "slow tracking shot along the houses", h="yağmur"),
       S("11:00 sabah", "carsi", ["mert", "ali", "oymaci"], "Yüz Kaşık",
         "Amasra'nın Çekiciler Çarşısı'nda ahşap oymacısı Halil Usta'dan 100 el yapımı ahşap kaşık alırlar.",
         "Halil carves a wooden spoon with a small knife at his doorway, blows away the shavings and hands it to Ali; Ali turns it in his hand and "
         "nods; Mert counts a stack of spoons on the counter.",
         [("oymaci", "Şimşir ağacından. Bir ömür dayanır. Tanesi yüz yirmi.", "proud"),
          ("ali", "Yüz tane alıyoruz usta.", "decisive")],
         "slow push-in on the carving hands",
         t=U(100, "kaşık", 120, "alis", "Amasra el yapımı ahşap kaşık ({adet} x {fiyat} TL)")),
       S("12:30 öğle", "carsi", ["mert", "ali"], "Torunlar",
         "Mert'in paylaştığı baston videosundan sonra 20 baston siparişle satılır: hepsi dedeleri için alan torunlar.",
         "Mert reads messages on his phone aloud, sitting on the shop's doorstep; Ali leans over to see; Mert puts his hand on his heart.",
         [("mert", "'Dedem için bir baston.' 'Babaannem için.' Yirmi sipariş Ali!", "moved"),
          ("ali", "Dedesini seven torunlar. Haklıydın.", "smiling")],
         "static medium two-shot on the doorstep",
         t=U(20, "baston", 1100, "satis", "Devrek bastonu, takipçi siparişi ({adet} x {fiyat} TL)")),
       S("14:00 iç-gündüz", "lokanta", ["mert", "ali"], "Amasra Salatası",
         "Amasra salatası ve kızarmış balık yerler. Limanda küçük tekneler sallanır.",
         "Mert squeezes lemon over fried fish while Ali mixes the salad; through the window small boats rock in the harbor; Mert steals a piece "
         "of fish from Ali's plate.",
         [("ali", "O benim balığım.", "deadpan"),
          ("mert", "Ortak kasa, ortak balık.", "grinning")],
         "static medium two-shot by the window",
         t=T("yemek", 1000, "Balık ve Amasra salatası")),
       S("17:30 gün batımı", "kale", ["mert", "ali"], "Rüzgâra Karşı",
         "Amasra'nın surlarında rüzgâra karşı dururlar. Dalgalar kayalara çarpar.",
         "Mert and Ali stand on the old castle wall leaning into the strong wind, jackets flapping; Mert spreads his arms like wings; Ali grabs the "
         "back of his jacket, laughing.",
         [("mert", "Ali, uçuyorum!", "shouting into the wind"),
          ("ali", "Uçma, kasayı tutan benim!", "laughing")],
         "slow crane-up revealing the sea on both sides", h="rüzgar"),
       S("20:00 akşam", "kale", ["mert", "ali"], "Trabzon'dan Mesaj",
         "Akşam Ali'nin telefonuna Trabzon'dan bir şirketin mesajı gelir: kutuları görmüşlerdir, yılbaşı için görüşmek isterler.",
         "Ali reads a message under a street lamp at the castle gate, his eyebrows rising; he shows Mert, who reads it and immediately raises his "
         "little finger toward Ali with a grin.",
         [("ali", "Trabzon'dan bir şirket yılbaşı için kutu istiyor. Görüşelim diyorlar.", "surprised"),
          ("mert", "Önce sana soruyorum: görüşelim mi? Ve... sözleşmeyle.", "careful, grinning")],
         "static medium two-shot under the street lamp",
         t=[T("konaklama", 1200, "Pansiyon, 1 gece"), T("ulasim", 700, "Yakıt: Bartın-Karabük")]),
   ],
   misafir={"oymaci": ("HALİL USTA", "HALİL, a 68-year-old Turkish wood carver, thin, a white beard, round glasses, a knitted cap, a leather "
                       "apron full of shavings", "elderly male voice, proud, Black Sea Turkish")},
   ay=AY, hava="bulutlu", kiyafet=K, urun="Amasra ahşap el sanatları, Amasra salatası, balık; Bartın ahşap evleri, Amasra kalesi",
   sponsor="Ahşap el sanatları, balık lokantası ya da Amasra turizmi alanında",
   kapak=("kale", ["mert", "ali"], "Mert spreads his arms like wings into a strong wind on the old Amasra castle wall while Ali holds the back of "
          "his jacket laughing, stormy sea on both sides at sunset", "Amasra surlarında rüzgâra kollarını açan Mert ve onu tutan Ali."),
   yakinda=("carsi", ["mert"], "Wood shavings flying in a beam of light in a tiny craftsman's shop, a half-carved wooden spoon in the foreground, "
            "Mert's curious face behind", "Işık huzmesinde uçuşan talaşlar ve yarım oyulmuş bir kaşık."),
   tiktok="Dedesini seven torunlar 20 baston aldı 🥹 #JozhStudios",
   ig=("Amasra'nın Çekiciler Çarşısı'nda Halil Usta'nın şimşir kaşıklarından 100 tane aldık. 🥄\n\n"
       "Baston videosundan sonra 20 sipariş geldi: 'Dedem için.' 'Babaannem için.' 🥹 Amasra'nın surlarında Mert uçtu, Ali tuttu.\n\n"
       "Ve Trabzon'dan bir şirket yazdı: yılbaşı kutuları! Kasa: {KASA}"),
   tags=["#Bartın", "#Amasra", "#AhşapKaşık"],
   son="Trabzon'dan bir şirket yılbaşı kutuları için görüşmek istiyor.",
   teaser="Ahşap kaşıklar, dedeler için bastonlar ve Trabzon'dan gelen bir mesaj. Bölüm 60: Bartın. Pek yakında.")

# ======================================================================= 61 KARABÜK
EP(61, "Karabük", "Safranbolu'da Lokum",
   "Safranbolu'nun konakları, safranın hikâyesi, lokum ve kaşık satışı.",
   "Karabük'te sabah Safranbolu'nun UNESCO listesindeki konaklarının arasında yürürler. Bir konak müzesinde eski evlerin kış ve yaz odalarını "
   "görürler. Safranın bir çiçeğin üç küçük tepeciğinden toplandığını ve bu yüzden çok pahalı olduğunu öğrenirler. Bir lokumcudan 60 kilo "
   "Safranbolu lokumu alırlar: Trabzon görüşmesi tutarsa kutuya girecektir. Ahşap kaşıkların yarısı bir hediyelik dükkânına satılır. Akşam "
   "Hıdırlık Tepesi'nden şehrin kırmızı kiremitli çatılarına bakarlar.",
   {"sokak": ("Safranbolu sokakları", "the cobbled streets of old Safranbolu: white-plastered timber-framed Ottoman mansions with red tile roofs "
              "and wooden shutters, autumn trees, light mist"),
    "konak": ("Konak müzesi", "the interior of a restored Ottoman mansion in Safranbolu: a wooden ceiling, cushioned benches along the walls, "
              "a built-in cupboard with a hidden bathing cabinet, carpets, soft daylight"),
    "lokumcu": ("Lokumcu", "a traditional lokum shop in Safranbolu: trays of lokum dusted with powdered sugar, some with saffron color, copper "
                "cauldrons, a long wooden counter"),
    "hediyelik": ("Hediyelik dükkânı", "a small gift shop in old Safranbolu with wooden toys, copper items and handmade goods"),
    "hidirlik": ("Hıdırlık Tepesi", "Hıdırlık Hill above Safranbolu at sunset: a stone terrace overlooking the sea of red tile roofs of the old "
                 "town, autumn trees, a few benches")},
   [
       S("09:00 sabah", "sokak", ["mert", "ali"], "Kırmızı Çatılar",
         "Safranbolu'nun arnavut kaldırımlı sokaklarında konakların arasında yürürler.",
         "Mert and Ali walk up a cobbled lane between white timber-framed mansions; Mert stops to look up at a carved wooden bay window and almost "
         "slips on the wet cobbles; Ali catches his arm.",
         [("ali", "Bütün şehir UNESCO listesinde.", "impressed"),
          ("mert", "Kaldırımı da listede, ben az kalsın düşüyordum.", "laughing")],
         "slow tracking shot up the lane", h="sis"),
       S("10:30 iç-gündüz", "konak", ["mert", "ali", "rehber"], "Dolapta Hamam",
         "Konak müzesinde rehber, dolabın içine gizlenmiş küçük yıkanma yerini gösterir. Mert hayran kalır.",
         "The guide opens a wooden cupboard door to reveal a tiny hidden bathing space inside; Mert leans in, amazed, and Ali laughs behind him.",
         [("rehber", "Eski evlerde dolabın içinde yıkanma yeri olurdu.", "storytelling"),
          ("mert", "Dolapta hamam! Bizim eve de lazım.", "amazed")],
         "static medium three-shot by the cupboard"),
       S("12:30 iç-gündüz", "lokumcu", ["mert", "ali", "lokumcu"], "Safranın Bedeli",
         "Lokumcu safranın bir çiçeğin üç küçük tepeciğinden toplandığını anlatır. Altmış kilo Safranbolu lokumu alırlar.",
         "The lokum maker holds up a tiny pinch of deep red saffron threads between two fingers, then cuts a golden saffron lokum and offers it; "
         "Ali counts money onto the counter while Mert tastes.",
         [("lokumcu", "Bir çiçekten üç tel çıkar. O yüzden altın gibidir.", "proud"),
          ("ali", "Altmış kilo lokum alıyoruz. Trabzon tutarsa kutuya girecek.", "planning")],
         "slow push-in on the saffron threads",
         t=U(60, "kg", 350, "alis", "Safranbolu lokumu ({adet} kg x {fiyat} TL)")),
       S("14:00 iç-gündüz", "hediyelik", ["ali", "dukkan"], "Elli Kaşık",
         "Bir hediyelik dükkânı 50 Amasra ahşap kaşığını alır.",
         "The shop owner arranges wooden spoons in a basket by the door and nods; Ali hands over the bundle and receives the money.",
         [("dukkan", "Turistler el yapımı kaşığı sever. Elli tane, iki yüz elliden.", "pleased"),
          ("ali", "Amasra'dan Safranbolu'ya. Hayırlı olsun.", "polite")],
         "static medium two-shot at the counter",
         t=[U(50, "kaşık", 250, "satis", "Amasra ahşap kaşık, hediyelik dükkânına ({adet} x {fiyat} TL)"), T("yemek", 800, "Öğle yemeği")]),
       S("17:30 gün batımı", "hidirlik", ["mert", "ali"], "Kiremit Denizi",
         "Hıdırlık Tepesi'nden kırmızı kiremitli çatılara bakarlar. Mert, ileride kendi küçük dükkânlarının nasıl olacağını hayal eder.",
         "Mert and Ali lean on the stone parapet overlooking the sea of red roofs; Mert draws a small house shape in the air with his finger; Ali "
         "smiles and draws a door on it.",
         [("mert", "Bir gün böyle bir sokakta küçük bir dükkânımız olsa.", "dreamy"),
          ("ali", "Kapısını ben çizerim, tabelasını sen.", "warm")],
         "slow dolly-out revealing the old town"),
       S("21:00 akşam", "sokak", ["mert", "ali"], "Kastamonu Yolu",
         "Akşam kalan 20 bastonu Kastamonu'da satmaya karar verirler. Yağmur yeniden başlar.",
         "Mert and Ali walk back to the pickup in the drizzle carrying boxes; Mert lifts a carved cane from the back and points it forward like "
         "a general.",
         [("mert", "Kastamonu! Yirmi baston ileri!", "comic general"),
          ("ali", "Yavaş general, kaldırım ıslak.", "laughing")],
         "static wide shot of the street", h="yağmur",
         t=[T("konaklama", 1500, "Konak pansiyon, 1 gece"), T("ulasim", 900, "Yakıt: Karabük-Kastamonu")]),
   ],
   misafir={"rehber": ("REHBER", "GUIDE, a 34-year-old Turkish woman, a beige trench coat, a scarf, a lanyard without readable text",
                       "adult female voice, storytelling"),
            "lokumcu": ("LOKUMCU", "LOKUM MAKER, a 57-year-old Turkish man, round, a grey mustache, a white coat dusted with sugar",
                        "mature male voice, proud"),
            "dukkan": ("DÜKKÂN SAHİBİ", "SHOP OWNER, a 43-year-old Turkish woman, short red-dyed hair, a knitted cardigan", "adult female voice")},
   ay=AY, hava="sis", kiyafet=K, urun="Safranbolu lokumu, safran, demir-çelik; Safranbolu (UNESCO), Hıdırlık Tepesi",
   sponsor="Lokum, safran ya da Safranbolu turizmi alanında",
   kapak=("hidirlik", ["mert", "ali"], "Mert and Ali lean on a stone parapet above a misty sea of red tile roofs of Safranbolu at sunset, Mert "
          "drawing a house shape in the air", "Safranbolu'nun kırmızı çatılarına bakıp havada ev çizen Mert."),
   yakinda=("lokumcu", ["mert"], "A tiny pinch of glowing deep-red saffron threads held between two fingers in the foreground, Mert's amazed eyes "
            "behind in soft focus", "Parmaklar arasında parlayan kırmızı safran telleri."),
   tiktok="Bir çiçekten sadece 3 tel safran çıkıyor 🌸 #JozhStudios",
   ig=("Safranbolu'nun konaklarında dolabın içine gizlenmiş hamamlar gördük! 🛁\n\n"
       "Safran bir çiçeğin üç küçük telinden toplanıyormuş, o yüzden altın gibi. 60 kilo Safranbolu lokumu aldık: Trabzon tutarsa kutuya girecek. 🤞\n\n"
       "Hıdırlık Tepesi'nde küçük bir dükkân hayal ettik. Kasa: {KASA}"),
   tags=["#Karabük", "#Safranbolu", "#Safran"],
   son="Safranbolu lokumu Trabzon'daki görüşmeyi bekliyor.",
   teaser="Kiremit denizi, dolapta bir hamam ve altın değerinde üç tel. Bölüm 61: Karabük. Pek yakında.")

# ======================================================================= 62 KASTAMONU
EP(62, "Kastamonu", "Taşköprü'nün Sarımsağı",
   "Kastamonu Kalesi, Nasrullah Camii'nin kuşları, Taşköprü sarımsağı ve Ilgaz'a düşen ilk kar.",
   "Kastamonu'da sabah kale eteğindeki eski konakların arasından Nasrullah Camii'nin avlusuna inerler; şadırvanda güvercinler toplanır. "
   "Kalan 20 baston ve 50 kaşık bir kooperatif dükkânına satılır. Taşköprü'de sarımsak üreticisinden, kurutulmuş 60 kilo Taşköprü sarımsağı "
   "alırlar; Mert Tunceli'nin tek dişlisini hatırlar. Öğlen etli ekmek yerler. Akşam Ilgaz Dağı'na ilk kar düşer. Ali Trabzon görüşmesi için "
   "bir sözleşme taslağı hazırlar.",
   {"cami": ("Nasrullah Camii avlusu", "the courtyard of the Nasrullah Mosque in Kastamonu: an old stone fountain with many taps, pigeons, "
             "autumn plane trees, the hilltop castle visible above"),
    "kooperatif": ("Kooperatif dükkânı", "a women's cooperative shop in Kastamonu selling handmade goods and local products on wooden shelves"),
    "taskopru": ("Taşköprü sarımsak deposu", "a garlic storage barn in Taşköprü: braided bunches of dried white garlic hanging from wooden beams, "
                 "crates, a scale"),
    "firin": ("Etli ekmek fırını", "a Kastamonu bakery serving long thin etli ekmek flatbreads from a wood-fired oven"),
    "ilgaz": ("Ilgaz yolu", "a mountain road on Ilgaz at dusk with the first snow dusting the pine forest, the old white pickup truck at a "
              "roadside pull-out, cold mist")},
   [
       S("09:00 sabah", "cami", ["mert", "ali"], "Güvercinler",
         "Nasrullah Camii'nin avlusunda şadırvanın başında güvercinler toplanır.",
         "Mert crouches by the old stone fountain and holds out a few bread crumbs; pigeons gather around his feet; Ali stands back smiling with "
         "his hands in his jacket pockets.",
         [("mert", "Ali, güvercinler de takipçi oldu!", "delighted"),
          ("ali", "Ekmek bitince takibi bırakırlar.", "teasing")],
         "slow push-in at ground level", h="serin"),
       S("10:30 iç-gündüz", "kooperatif", ["ali", "kooperatif"], "Baston ve Kaşık",
         "Bir kadın kooperatifinin dükkânı kalan 20 bastonu ve 50 kaşığı alır.",
         "The cooperative manager hangs carved canes on a wall rack and places wooden spoons in a basket; Ali hands her the bundle and she pays "
         "him, smiling.",
         [("kooperatif", "Bastonlar ve kaşıklar burada çok sorulur. Hepsini alırım.", "practical"),
          ("ali", "Baston bin yüz, kaşık iki yüz elli.", "businesslike")],
         "static medium two-shot by the rack",
         t=[U(20, "baston", 1100, "satis", "Devrek bastonu, kooperatif dükkânına ({adet} x {fiyat} TL)"),
            U(50, "kaşık", 250, "satis", "Amasra ahşap kaşık, kooperatif dükkânına (50 x 250 TL)")]),
       S("12:30 iç-gündüz", "taskopru", ["mert", "ali", "sarimsakci"], "Örgülü Sarımsak",
         "Taşköprü'de örgü hâlinde kurutulmuş sarımsakların altında üretici Necati Bey ile konuşurlar. Altmış kilo alırlar.",
         "Necati lifts a long braid of dried white garlic from a beam and drapes it over Mert's shoulder; Mert poses like wearing a scarf; Ali "
         "counts money into Necati's hand.",
         [("sarimsakci", "Taşköprü sarımsağı keskin olur, uzun dayanır. Kilosu üç yüz.", "proud"),
          ("mert", "Tunceli'nin tek dişlisi kıskanacak!", "joking")],
         "static medium three-shot under the hanging braids",
         t=U(60, "kg", 300, "alis", "Taşköprü sarımsağı, kurutulmuş ({adet} kg x {fiyat} TL)")),
       S("14:00 iç-gündüz", "firin", ["mert", "ali"], "Etli Ekmek",
         "Kastamonu'nun ince uzun etli ekmeğini yerler. Mert sarımsak kokusundan şikâyet eder, sonra güler.",
         "A long thin etli ekmek flatbread slides out of the wood-fired oven onto the table; Mert tears a piece; Ali sniffs Mert's jacket and makes "
         "a face; both laugh.",
         [("ali", "Montun sarımsak kokuyor.", "making a face"),
          ("mert", "Karadeniz'de vampir yok, sayemde.", "grinning")],
         "static medium two-shot at the table",
         t=T("yemek", 700, "Etli ekmek")),
       S("18:00 akşam", "ilgaz", ["mert", "ali"], "İlk Kar",
         "Ilgaz Dağı'na ilk kar düşer. Kamyonetin yanında dururlar, nefesleri buhar olur.",
         "Light snow begins to fall on the pine forest; Mert holds out his palm to catch a snowflake; Ali pulls his jacket tighter and looks at the "
         "road ahead with concern.",
         [("mert", "Kar! Yolculuğun ilk karı!", "childlike joy"),
          ("ali", "Kış yaklaşıyor. Dağları hızlı geçmeliyiz.", "worried")],
         "slow crane-up from the pickup to the snowy forest", h="kar"),
       S("21:30 iç-gece", "kooperatif", ["mert", "ali"], "Sözleşme Taslağı",
         "Gece Ali Trabzon görüşmesi için bir sözleşme taslağı hazırlar. Mert her maddeyi okur ve imza yerini işaret eder.",
         "Ali writes clauses in the notebook at a small table; Mert reads over his shoulder, then points at the bottom of the page and makes a "
         "signature gesture in the air.",
         [("ali", "Kutu sayısı, fiyat, yüzde otuz peşin, teslim tarihi.", "precise"),
          ("mert", "Ve iki imza. Kâğıt olmadan para yok.", "proud")],
         "slow push-in on the notebook",
         t=[T("konaklama", 1200, "Pansiyon, 1 gece"), T("ulasim", 900, "Yakıt: Kastamonu-Sinop")]),
   ],
   misafir={"kooperatif": ("KOOPERATİF YÖNETİCİSİ", "COOPERATIVE MANAGER, a 50-year-old Turkish woman, a burgundy headscarf, glasses, a grey "
                           "cardigan", "adult female voice, practical"),
            "sarimsakci": ("NECATİ BEY", "NECATİ, a 59-year-old Turkish garlic producer, broad, a white stubble, a flat cap, a padded vest",
                           "mature male voice, proud, Kastamonu Turkish")},
   ay=AY, hava="serin", kiyafet=K, urun="Taşköprü sarımsağı, etli ekmek, pastırma; Kastamonu Kalesi, Nasrullah Camii, Ilgaz Dağı",
   sponsor="Sarımsak, kooperatif ürünleri ya da Ilgaz turizmi alanında",
   kapak=("taskopru", ["mert", "ali", "sarimsakci"], "Mert wears a long braid of dried white garlic like a scarf and poses dramatically under "
          "hanging garlic braids, Ali and the farmer laughing", "Sarımsak örgüsünü atkı gibi takan Mert."),
   yakinda=("ilgaz", ["mert"], "The first snowflakes falling on a dark pine forest at dusk, Mert's open palm catching one in the foreground",
            "Karanlık çam ormanına düşen ilk kar ve bir avuç."),
   tiktok="Sarımsak atkısı + yolculuğun ilk karı ❄️🧄 #JozhStudios",
   ig=("Kastamonu'da Nasrullah Camii'nin güvercinleri bizi takip etti (ekmek bitene kadar 😂).\n\n"
       "Taşköprü'den 60 kilo sarımsak aldık; Mert sarımsak örgüsünü atkı yaptı. 🧄 Akşam Ilgaz'a ilk kar düştü. ❄️\n\n"
       "Ali, Trabzon için sözleşme taslağını hazırladı: kâğıt olmadan para yok. Kasa: {KASA}"),
   tags=["#Kastamonu", "#TaşköprüSarımsağı", "#Ilgaz"],
   son="İlk kar düştü. Trabzon için sözleşme taslağı hazır.",
   teaser="Güvercinler, sarımsak örgüleri ve dağa düşen ilk kar. Bölüm 62: Kastamonu. Pek yakında.")

# ======================================================================= 63 SİNOP
EP(63, "Sinop", "Tarihi Cezaevi",
   "Sinop'un tarihi cezaevi, tekne ustaları, Sinop mantısı ve İnceburun'da rüzgâr.",
   "Sinop'ta sabah müzeye dönüştürülmüş tarihi cezaevinin taş koridorlarında yürürler; özgürlüğün ne demek olduğunu konuşurlar. Limanda "
   "ahşap tekne yapan ustayı izler; usta bir teknenin bir yılda yapıldığını anlatır. Taşköprü sarımsağının yarısı bir lokantaya satılır. Öğlen "
   "cevizli Sinop mantısı yerler. Akşam Türkiye'nin en kuzey ucu İnceburun'da rüzgârın içinde dururlar ve Trabzon'daki şirketle görüşme "
   "günü kesinleşir.",
   {"cezaevi": ("Sinop tarihi cezaevi müzesi", "the historic Sinop prison, now a museum: thick stone walls, long dim corridors with heavy iron "
                "doors, a courtyard with an old tree, grey light"),
    "tersane": ("Ahşap tekne tezgâhı", "a traditional wooden boatyard in Sinop harbor: the wooden ribs of a half-built fishing boat on wooden "
                "supports, planks, tools, the calm harbor behind"),
    "lokanta": ("Sinop lokantası", "a small restaurant in Sinop with a harbor view: plates of Sinop mantı topped with crushed walnuts and "
                "yogurt, simple tables"),
    "inceburun": ("İnceburun", "the İnceburun cape near Sinop at sunset: a white lighthouse on a rocky point, strong wind, waves crashing, "
                  "open dark sea to the north")},
   [
       S("09:00 iç-gündüz", "cezaevi", ["mert", "ali"], "Taş Koridorlar",
         "Müzeye dönüştürülmüş tarihi cezaevinin taş koridorlarında yürürler. Mert ağır bir demir kapıya dokunur.",
         "Mert and Ali walk slowly down a long dim stone corridor lined with heavy iron doors; Mert touches the cold iron of a door and pulls his "
         "hand back; Ali looks into an empty cell through a small window.",
         [("ali", "Burada insanlar yıllarca kalmış.", "quiet"),
          ("mert", "Biz borç yüzünden yollardayız ama özgürüz. Şükür.", "thoughtful")],
         "slow tracking shot along the corridor", h="bulutlu"),
       S("11:00 sabah", "tersane", ["mert", "ali", "teknici"], "Bir Yılda Bir Tekne",
         "Limanda ahşap tekne ustası Kemal Usta bir teknenin kaburgalarını çakarken bir teknenin bir yılda yapıldığını anlatır.",
         "Kemal hammers a wooden peg into the curved rib of the half-built boat; Mert holds a plank steady for him; Ali runs his hand along the "
         "smooth curve of the hull.",
         [("teknici", "Bir tekne bir yılda biter. Acele eden denizde kalır.", "wise, gruff"),
          ("mert", "Sabır her şehirde başka bir ustanın ağzından çıkıyor.", "smiling")],
         "slow orbit around the boat ribs", h="bulutlu"),
       S("13:00 iç-gündüz", "lokanta", ["mert", "ali", "lokantaci"], "Cevizli Mantı",
         "Sinop mantısını yerler; lokantacı Taşköprü sarımsağından 30 kiloyu alır.",
         "The restaurant owner places plates of mantı topped with crushed walnuts in front of them, then lifts the braid of garlic Mert offers "
         "and smells it, nodding.",
         [("lokantaci", "Mantının yoğurduna Taşköprü sarımsağı! Otuz kilo alırım.", "delighted"),
          ("ali", "Kilosu dört yüz elli. Mantı da bizden olsun.", "smiling")],
         "static medium three-shot at the table",
         t=[U(30, "kg", 450, "satis", "Taşköprü sarımsağı, lokantaya ({adet} kg x {fiyat} TL)"), T("yemek", 900, "Sinop mantısı")]),
       S("17:00 gün batımı", "inceburun", ["mert", "ali"], "En Kuzey",
         "Türkiye'nin en kuzey ucu İnceburun'da rüzgârın içinde dururlar. Fenerin ışığı yanar.",
         "Mert and Ali stand on the rocky point near the white lighthouse, leaning into the strong wind; Mert points north over the dark sea; Ali "
         "holds his jacket closed with one hand.",
         [("mert", "Buradan sonrası deniz. Türkiye'nin en kuzeyi!", "shouting into the wind"),
          ("ali", "Malatya'dan buraya kamyonetle!", "amazed")],
         "slow crane-up past the lighthouse", h="rüzgar"),
       S("19:30 akşam", "inceburun", ["ali", "~sirket"], "Görüşme Günü",
         "Trabzon'daki şirketten Selma Hanım arar: görüşme üç gün sonra, Trabzon'dadır.",
         "Ali stands by the lighthouse with the phone at his ear, sheltering from the wind with his back turned; he nods and gives a thumbs-up "
         "toward the camera with his free hand. His lips stay closed while she speaks.",
         [("sirket", "Görüşmeyi üç gün sonra Trabzon'da yapalım. Sözleşmenizi getirin.", "professional, from the phone speaker"),
          ("ali", "Taslak hazır, Selma Hanım. Görüşürüz.", "confident")],
         "static medium shot by the lighthouse", h="rüzgar"),
       S("21:30 iç-gece", "lokanta", ["mert", "ali"], "Üç Gün",
         "Akşam Ali rotayı hesaplar: Samsun, Ordu, Giresun ve sonra Trabzon. Kutunun içeriği yolda tamamlanacaktır.",
         "Ali lays out the brown notebook and a small paper map on the table; Mert places a piece of Safranbolu lokum, a garlic clove and a "
         "walnut on the map as markers; Ali moves the walnut to Trabzon.",
         [("ali", "Ordu'da fındık ezmesi, Giresun'da tombul fındık, Rize'de çay.", "planning"),
          ("mert", "Ve Trabzon'da imza. Bu sefer kâğıtla.", "determined")],
         "top-down shot over the map",
         t=[T("konaklama", 1100, "Pansiyon, 1 gece"), T("ulasim", 900, "Yakıt: Sinop-Samsun")]),
   ],
   misafir={"teknici": ("KEMAL USTA", "KEMAL, a 66-year-old Turkish wooden boat builder, strong and weathered, a white beard, a knitted fisherman's "
                        "cap, a patched navy sweater", "elderly male voice, wise, gruff, Black Sea Turkish"),
            "lokantaci": ("LOKANTACI", "RESTAURANT OWNER, a 50-year-old Turkish woman, round, a white headscarf, an apron", "adult female voice, delighted"),
            "sirket": ("SELMA HANIM", "SELMA, a 40-year-old Turkish company manager, short dark hair, a navy blazer", "adult female voice, professional")},
   ay=AY, hava="bulutlu", kiyafet=K, urun="Sinop mantısı, ahşap tekne yapımı, Sinop işi; tarihi cezaevi müzesi, İnceburun",
   sponsor="Ahşap tekne, yöresel mutfak ya da kıyı turizmi alanında",
   kapak=("inceburun", ["mert", "ali"], "Mert and Ali stand on a rocky point beside a white lighthouse at sunset, leaning into a strong wind, Mert "
          "pointing north over the dark stormy sea", "Fenerin yanında rüzgâra karşı kuzeyi gösteren Mert."),
   yakinda=("cezaevi", ["mert"], "A long dark stone corridor with heavy iron doors, a single beam of light falling on Mert's hand touching a cold "
            "iron door", "Uzun taş koridorda demir kapıya dokunan bir el."),
   tiktok="Türkiye'nin en kuzey ucundayız 🧭 #JozhStudios",
   ig=("Sinop'un tarihi cezaevinde taş koridorlarda yürüdük; özgürlüğün kıymetini konuştuk. 🕊️\n\n"
       "Kemal Usta: 'Bir tekne bir yılda biter. Acele eden denizde kalır.' ⛵ Cevizli Sinop mantısı yedik ve İnceburun'da Türkiye'nin en kuzeyindeydik!\n\n"
       "Trabzon görüşmesi üç gün sonra. Kasa: {KASA}"),
   tags=["#Sinop", "#İnceburun", "#SinopMantısı"],
   son="Trabzon görüşmesi üç gün sonra. Kutunun içeriği yolda tamamlanacak.",
   teaser="Taş koridorlar, bir yılda biten tekne ve en kuzeyde rüzgâr. Bölüm 63: Sinop. Pek yakında.")

# ======================================================================= 64 SAMSUN
EP(64, "Samsun", "Bandırma Vapuru",
   "Bandırma Vapuru Müzesi, Bafra pidesi, Kızılırmak Deltası ve kalan sarımsak.",
   "Samsun'da sabah Bandırma Vapuru'nun müzedeki replikasını gezer, 19 Mayıs 1919'un hikâyesini dinlerler. Kalan 30 kilo sarımsak bir "
   "toptancıya satılır. Öğlen Bafra pidesini ikiye katlayarak yerler. Kızılırmak Deltası'nın sazlıklarında kuşların göçünü izlerler; Ali "
   "sessizce saydığı kuşları deftere yazar. Akşam Safranbolu lokumunun 30 kilosu bir pastaneye satılmak istenir ama Ali hatırlatır: lokum "
   "kutuya ayrılmıştır.",
   {"vapur": ("Bandırma Vapuru Müzesi", "the full-size replica of the steamship Bandırma at the Samsun museum park: a black-hulled old steamer "
              "with a tall funnel, wooden deck, by the seaside"),
    "toptanci": ("Samsun hali", "a wholesale produce market hall in Samsun: stacked crates, a forklift, scales, bustling but far in the "
                 "background"),
    "pide": ("Bafra pidecisi", "a Bafra pide restaurant: a long wood-fired oven, long thin pides with minced meat being sliced, simple tables"),
    "delta": ("Kızılırmak Deltası", "the Kızılırmak Delta wetlands near Bafra: tall golden reeds, shallow lagoons, flocks of migrating birds "
              "in the sky, a wooden birdwatching tower")},
   [
       S("09:00 sabah", "vapur", ["mert", "ali"], "Bir Vapur",
         "Bandırma Vapuru'nun replikasının güvertesindedirler. Ali, 1919'da buradan başlayan yolculuğu anlatır.",
         "Mert and Ali stand on the wooden deck of the old black steamer replica near the tall funnel; Ali points toward the shore; Mert grips the "
         "railing and looks out quietly.",
         [("ali", "Bin dokuz yüz on dokuzda bir vapur, büyük bir yolculuğun başlangıcı oldu.", "respectful"),
          ("mert", "Her büyük yolculuk küçük bir adımla başlıyor.", "thoughtful")],
         "slow crane-up from the deck to the funnel", h="bulutlu"),
       S("11:00 sabah", "toptanci", ["mert", "toptanci"], "Kalan Sarımsak",
         "Samsun halinde bir toptancı kalan 30 kilo Taşköprü sarımsağını alır.",
         "The wholesaler weighs a braid of garlic on a floor scale and nods; Mert hands him the rest of the braids and receives money; a forklift "
         "passes far behind.",
         [("toptanci", "Taşköprü sarımsağı halde aranır. Otuz kilo, dört yüz elliden.", "brisk"),
          ("mert", "Sarımsak bitti, montum hâlâ kokuyor.", "joking")],
         "static medium two-shot at the scale",
         t=U(30, "kg", 450, "satis", "Taşköprü sarımsağı, Samsun halinde ({adet} kg x {fiyat} TL)")),
       S("13:00 iç-gündüz", "pide", ["mert", "ali"], "Bafra Pidesi",
         "Bafra pidesini ikiye katlayarak yerler. Mert ustanın hamuru nasıl incelttiğine hayran kalır.",
         "Mert folds a long thin pide in half and bites into it; Ali watches the baker, out of focus behind them, stretching dough at the oven; "
         "Mert gives a thumbs-up with his mouth full.",
         [("ali", "Hamur kâğıt gibi ince.", "admiring"),
          ("mert", "Bafra pidesi katlanır, Mert de katlanır.", "mouth full, happy")],
         "static medium two-shot at the table",
         t=T("yemek", 800, "Bafra pidesi")),
       S("15:30 ikindi", "delta", ["mert", "ali"], "Göç",
         "Kızılırmak Deltası'nın sazlıklarında göçmen kuşları izlerler. Ali kuşları sayar.",
         "Mert and Ali stand on the wooden birdwatching tower above the golden reeds; a huge flock of birds lifts off the lagoon and turns in the "
         "sky; Ali counts with his pen moving in the air.",
         [("ali", "Binlerce kuş... her yıl aynı yolu buluyorlar.", "awed"),
          ("mert", "Haritasız, defterli de değiller. Ama kaybolmuyorlar.", "amazed")],
         "slow crane-up following the flock", h="bulutlu"),
       S("18:30 akşam", "pide", ["mert", "ali", "pastaci"], "Lokum Kutunun",
         "Bir pastaneci Safranbolu lokumunu görünce almak ister. Mert satmaya hazırlanırken Ali hatırlatır: lokum kutuya ayrılmıştır.",
         "A pastry shop owner points eagerly at a box of saffron lokum in Mert's hands and pulls out his wallet; Mert starts to hand it over, but "
         "Ali gently places his hand on the box; Mert stops and smiles apologetically.",
         [("pastaci", "Bu lokumu satarsanız hepsini alırım!", "eager"),
          ("ali", "Kusura bakmayın, bu lokum bir söze ayrıldı.", "polite, firm")],
         "static medium three-shot"),
       S("21:00 akşam", "delta", ["mert", "ali"], "Teşekkür",
         "Akşam Mert, Ali'ye teşekkür eder: lokumu satsaydı Trabzon'da eli boş kalacaklardı.",
         "Mert and Ali sit in the pickup cab parked by the dark delta, the reeds silver in the moonlight; Mert taps Ali's shoulder twice and Ali "
         "nods.",
         [("mert", "Lokumu satsam Trabzon'da eli boş kalırdık. Sağ ol.", "grateful"),
          ("ali", "Ortak karar. Sen olsan sen de durdururdun.", "warm")],
         "static medium two-shot through the windshield",
         t=[T("konaklama", 1300, "Otel, 1 gece"), T("ulasim", 1000, "Yakıt: Samsun-Ordu")]),
   ],
   misafir={"toptanci": ("TOPTANCI", "WHOLESALER, a 55-year-old Turkish man, heavy, a grey cap, a padded vest", "mature male voice, brisk"),
            "pastaci": ("PASTANECİ", "PASTRY SHOP OWNER, a 46-year-old Turkish man, slim, a black beard, a white apron", "adult male voice, eager")},
   ay=AY, hava="bulutlu", kiyafet=K, urun="Bafra pidesi, Çarşamba ve Bafra ovaları; Bandırma Vapuru Müzesi, Kızılırmak Deltası",
   sponsor="Pide, tarım ürünleri ya da delta turizmi alanında",
   kapak=("delta", ["mert", "ali"], "Mert and Ali on a wooden birdwatching tower above golden reeds as a giant flock of migrating birds swirls in "
          "the sky above them", "Kuş gözlem kulesinde dev bir kuş sürüsünü izleyen Mert ve Ali."),
   yakinda=("vapur", ["mert", "ali"], "Two silhouettes on the deck of an old black steamship with a tall funnel against a grey morning sea",
            "Gri sabahta eski bir vapurun güvertesinde iki silüet."),
   tiktok="Binlerce kuş haritasız yolunu buluyor 🐦 #JozhStudios",
   ig=("Samsun'da Bandırma Vapuru'nun güvertesindeydik: her büyük yolculuk küçük bir adımla başlar. ⚓\n\n"
       "Bafra pidesini katladık, Kızılırmak Deltası'nda binlerce göçmen kuşu izledik. 🐦\n\n"
       "Bir pastaneci lokumumuzu istedi, Ali 'bu lokum bir söze ayrıldı' dedi. Kasa: {KASA}"),
   tags=["#Samsun", "#BandırmaVapuru", "#KızılırmakDeltası"],
   son="Lokum söze ayrıldı. Sırada Ordu'nun fındık ezmesi var.",
   teaser="Bir vapur, binlerce kuş ve bir söze ayrılmış lokum. Bölüm 64: Samsun. Pek yakında.")

# ======================================================================= 65 ORDU
EP(65, "Ordu", "Fındığın Başkenti",
   "Boztepe'de teleferik, fındık ezmesi atölyesi ve Ordu'ya fındık satmaya kalkan Mert.",
   "Ordu'da sabah Mert, Düzce'de kalan bir avuç fındığı bir esnafa satmaya kalkar; Ali gülerek durdurur: 'Kars. Hatay. Ordu.' Teleferikle "
   "Boztepe'ye çıkıp fındık bahçeleriyle kaplı yamaçları ve denizi görürler. Bir fındık ezmesi atölyesinde kavrulan fındığın taş değirmende "
   "ezmeye dönüşmesini izler, kutu için 300 kavanoz alırlar. Akşam bir ev pansiyonunda fındıklı karalahana çorbası içerler.",
   {"carsi": ("Ordu çarşısı", "a busy street in central Ordu with shops selling hazelnuts in sacks and jars, a sea view at the end of the street"),
    "teleferik": ("Boztepe teleferiği", "the inside of a cable car cabin rising from Ordu city up to Boztepe hill: big windows, the city, the sea "
                  "and green hazelnut-covered slopes below"),
    "boztepe": ("Boztepe", "the Boztepe viewpoint above Ordu: a wide terrace overlooking the Black Sea coast, the city, and hills covered with "
                "hazelnut orchards"),
    "atolye": ("Fındık ezmesi atölyesi", "a hazelnut paste workshop in Ordu: a large roaster with hazelnuts turning, a stone grinder producing "
               "smooth brown paste, rows of glass jars"),
    "pansiyon": ("Ev pansiyonu", "a cozy family guesthouse kitchen in Ordu at night: a wooden table, a pot of soup, a wood stove, rain on the "
                 "window")},
   [
       S("09:00 sabah", "carsi", ["mert", "ali"], "Ordu'ya Fındık",
         "Mert cebindeki bir avuç fındığı bir esnafa satmaya kalkar. Ali gülerek kolundan çeker.",
         "Mert holds out a small paper bag of hazelnuts to a shopkeeper standing in front of a mountain of hazelnut sacks; Ali grabs Mert's arm and "
         "pulls him away while laughing; the shopkeeper, out of focus, laughs too.",
         [("ali", "Kars. Hatay. Ordu. Mert, lütfen!", "laughing"),
          ("mert", "Alışkanlık Ali! Elim kendiliğinden uzandı.", "embarrassed, laughing")],
         "static medium two-shot on the street", h="bulutlu"),
       S("10:30 iç-gündüz", "teleferik", ["mert", "ali"], "Yükseliş",
         "Teleferikle Boztepe'ye çıkarlar. Aşağıda şehir, deniz ve fındık bahçeleri.",
         "Mert presses his face and hands to the cable car window as the city and the sea shrink below; Ali sits calmly but grips the seat edge.",
         [("mert", "Bütün yamaçlar fındık Ali! Her yer!", "excited"),
          ("ali", "Pencereye yaslanma, kabin sallanıyor.", "nervous")],
         "static medium shot inside the cabin, the view rising behind"),
       S("11:00 sabah", "boztepe", ["mert", "ali"], "Yeşil Yamaçlar",
         "Boztepe'den sahile ve fındık bahçeleriyle kaplı yamaçlara bakarlar.",
         "Mert and Ali stand at the railing of the Boztepe terrace; Ali points out the patchwork of hazelnut orchards on the hills; Mert breathes "
         "in deeply.",
         [("ali", "Türkiye dünyanın en çok fındık üreten ülkesi. Burası kalbi.", "informative"),
          ("mert", "Bu manzarayı da kutuya koyabilsek.", "dreamy")],
         "slow crane-up revealing the coast and the hills", h="bulutlu"),
       S("14:00 iç-gündüz", "atolye", ["mert", "ali", "ezmeci"], "Taşta Ezme",
         "Fındık ezmesi atölyesinde kavrulan fındığın taş değirmende ezmeye dönüştüğünü izler, kutu için 300 kavanoz alırlar.",
         "The workshop owner opens the roaster and lets hot hazelnuts pour into a tray; the stone grinder turns them into smooth brown paste that "
         "flows into a jar; Mert dips a spoon and tastes, eyes closed; Ali counts money.",
         [("ezmeci", "Sadece fındık. Şeker yok, katkı yok. Kavanozu yüz on.", "proud"),
          ("ali", "Üç yüz kavanoz. Trabzon kutusu için.", "decisive")],
         "slow push-in on the paste flowing into the jar",
         t=U(300, "kavanoz", 110, "alis", "Ordu fındık ezmesi ({adet} kavanoz x {fiyat} TL)")),
       S("20:00 iç-gece", "pansiyon", ["mert", "ali", "evsahibi"], "Karalahana Çorbası",
         "Akşam ev pansiyonunda ev sahibi fındıklı karalahana çorbası koyar.",
         "The guesthouse host ladles steaming dark green soup into two bowls and sprinkles crushed hazelnuts on top; Mert and Ali warm their hands "
         "on the bowls by the wood stove.",
         [("evsahibi", "Karadeniz'in kışı karalahanayla geçer. Afiyet olsun.", "motherly"),
          ("mert", "Teyze, bu çorba bize kış montu gibi geldi.", "grateful")],
         "static medium three-shot at the table", h="yağmur",
         t=T("yemek", 600, "Öğle yemeği")),
       S("22:00 iç-gece", "pansiyon", ["mert", "ali"], "Yarın Giresun",
         "Gece Ali listeyi kontrol eder: lokum tamam, fındık ezmesi tamam. Sırada Giresun'un tombul fındığı.",
         "Ali checks items off a list in the notebook by the stove; Mert stacks jars of hazelnut paste into a crate and taps the lid.",
         [("ali", "Lokum tamam, ezme tamam. Yarın tombul fındık.", "satisfied"),
          ("mert", "Fındığı Ordu'da satmadık, Giresun'da alıyoruz. Gelişme!", "proud")],
         "static medium two-shot by the stove",
         t=[T("konaklama", 1000, "Ev pansiyonu, 1 gece"), T("ulasim", 700, "Yakıt: Ordu-Giresun")]),
   ],
   misafir={"ezmeci": ("FINDIK EZMECİSİ", "HAZELNUT PASTE MAKER, a 44-year-old Turkish man, slim, a black beard, a brown apron dusted with "
                       "hazelnut skins", "adult male voice, proud"),
            "evsahibi": ("EV SAHİBİ TEYZE", "GUESTHOUSE HOST, a 66-year-old Turkish woman, small, a colorful Black Sea headscarf, a thick "
                         "knitted vest", "elderly female voice, motherly, Black Sea Turkish")},
   ay=AY, hava="bulutlu", kiyafet=K, urun="Fındık, fındık ezmesi, karalahana; Boztepe",
   sponsor="Fındık, fındık ezmesi ya da yayla turizmi alanında",
   kapak=("atolye", ["mert", "ali"], "Mert tastes smooth hazelnut paste from a spoon with eyes closed in bliss as paste flows from a stone grinder "
          "into a jar, Ali laughing beside him", "Fındık ezmesini gözleri kapalı tadan Mert."),
   yakinda=("teleferik", ["mert"], "A cable car cabin silhouette rising above a coastal city at dusk, Mert's hands pressed against the glass",
            "Alacakaranlıkta yükselen teleferik kabini ve cama dayanan eller."),
   tiktok="Ordu'ya fındık satmaya kalktım 🌰😂 #JozhStudios",
   ig=("Ordu'da Mert bir avuç fındığı satmaya kalktı. Ali: 'Kars. Hatay. Ordu.' 😂🌰\n\n"
       "Boztepe'den bütün yamaçların fındık bahçesi olduğunu gördük. Atölyede sadece fındıktan yapılan ezmeden 300 kavanoz aldık. "
       "Karalahana çorbası ise kış montu gibi. 🥣\n\nKasa: {KASA}"),
   tags=["#Ordu", "#Fındık", "#Boztepe"],
   son="Lokum ve fındık ezmesi tamam. Sırada Giresun'un tombul fındığı.",
   teaser="Fındık yamaçları, taşta ezme ve Mert'in eski alışkanlığı. Bölüm 65: Ordu. Pek yakında.")

# ======================================================================= 66 GİRESUN
EP(66, "Giresun", "Tombul Fındık",
   "Giresun Adası'na fırtınada tekne, tombul fındık ve kalede kutu planı.",
   "Giresun'da sabah Mert, Doğu Karadeniz'in tek adası Giresun Adası'na gitmek ister; dalgalar yüksektir ve tekneci ancak kıyıdan uzakta bir "
   "tur atar. Bir fındık işleme tesisinde Giresun'un ünlü tombul fındığını görür, kutu için 75 kilo iç fındık alırlar. Öğlen Giresun "
   "pidesi yerler. Giresun Kalesi'nde Ali kutunun son hâlini çizer: çay, fındık, ezme ve lokum. Akşam Trabzon'a yarım saat kala sözleşmeyi "
   "son kez okurlar.",
   {"liman": ("Giresun limanı", "Giresun harbor on a windy morning: small fishing boats rocking, waves breaking on the breakwater, the green "
              "Giresun Island visible offshore"),
    "tekne": ("Fırtınada tekne", "a small motorboat bouncing on choppy grey waves offshore near Giresun, spray flying, the green island in the "
              "distance"),
    "tesis": ("Fındık işleme tesisi", "a hazelnut processing facility in Giresun: conveyor belts carrying round shelled hazelnuts, sorting "
              "machines, sacks stacked high"),
    "kale": ("Giresun Kalesi", "the hilltop park of Giresun Castle at sunset: old stone walls, tall trees, benches, a view over the city and "
             "the sea")},
   [
       S("09:00 sabah", "liman", ["mert", "ali", "tekneci"], "Ada Gözüküyor",
         "Mert Giresun Adası'na gitmek ister. Tekneci dalgaları gösterir: adaya yanaşılamaz, sadece kıyıdan bir tur.",
         "The boatman points at the big waves breaking on the breakwater and shakes his head; Mert pleads with joined hands; the boatman sighs and "
         "waves them toward a small motorboat.",
         [("tekneci", "Bu dalgada adaya yanaşılmaz. Kıyıdan bir tur, o kadar.", "firm"),
          ("mert", "Bir tur yeter abi! Uzaktan bile olsun.", "pleading")],
         "static medium three-shot on the pier", h="rüzgar"),
       S("09:30 sabah", "tekne", ["mert", "ali"], "Dalgalar",
         "Teknede dalgalar yüksektir. Ali sıkıca tutunur, Mert kahkahalar atar.",
         "The small boat bounces over choppy waves, spray splashing over the bow; Ali grips the side with both hands, soaking wet; Mert laughs and "
         "points at the island.",
         [("ali", "Bu da bir sözleşmeli iş miydi Mert?", "drenched, scared"),
          ("mert", "Tek ada! Doğu Karadeniz'in tek adası!", "laughing")],
         "handheld-feel but stable tracking shot from the bow", h="rüzgar",
         t=U(2, "kişi", 250, "diger_gider", "Giresun Adası tekne turu ({adet} x {fiyat} TL)")),
       S("12:00 iç-gündüz", "tesis", ["mert", "ali", "fabrikaci"], "Tombul",
         "Fındık işleme tesisinde tombul fındığın yuvarlak ve dolgun olduğunu görürler. Kutu için 75 kilo iç fındık alırlar.",
         "The facility manager scoops round shelled hazelnuts from a conveyor belt and pours them into Ali's palms; Ali compares one to a regular "
         "hazelnut; Mert sniffs a handful.",
         [("fabrikaci", "Tombul fındık yuvarlak ve dolgundur. Kilosu dört yüz yirmi.", "proud"),
          ("ali", "Yetmiş beş kilo. Üç yüz kutuya ikişer yüz elli gram.", "calculating")],
         "slow tracking shot along the conveyor",
         t=U(75, "kg", 420, "alis", "Giresun tombul iç fındık ({adet} kg x {fiyat} TL)")),
       S("13:30 iç-gündüz", "tesis", ["mert", "ali"], "Islak Kıyafet",
         "Öğlen Giresun pidesi yerken ıslak montları ısıtıcının önünde kurur.",
         "Mert and Ali sit by a space heater in a small canteen, their wet jackets steaming on chairs; Mert bites into a pide and wiggles his cold "
         "toes in socks.",
         [("mert", "Islandık ama ada gördük.", "satisfied"),
          ("ali", "Ben ada görmedim, dalga gördüm.", "sulking, smiling")],
         "static medium two-shot by the heater",
         t=T("yemek", 700, "Giresun pidesi")),
       S("17:30 gün batımı", "kale", ["mert", "ali"], "Kutunun Son Hâli",
         "Giresun Kalesi'nde Ali kutunun son hâlini çizer: çay, fındık, ezme, lokum.",
         "Ali draws a box with four compartments in the notebook on a bench; Mert places a hazelnut, a lokum piece and a tiny jar beside the "
         "notebook as models; the sun sets over the sea behind them.",
         [("ali", "Rize çayı, tombul fındık, fındık ezmesi, Safranbolu lokumu.", "precise"),
          ("mert", "Karadeniz Kutusu. Kokusu bile güzel.", "proud")],
         "slow push-in over the bench toward the sea"),
       S("21:00 akşam", "kale", ["mert", "ali"], "Son Okuma",
         "Akşam sözleşmeyi son kez okurlar. Yarın Trabzon'da imza vardır.",
         "Ali reads the contract draft aloud under a park lamp; Mert listens and nods at each line, then takes the pen and practices his "
         "signature on a blank corner of the page.",
         [("ali", "Üç yüz kutu, dokuz yüz lira, yüzde otuz peşin, teslimde kalanı.", "careful"),
          ("mert", "İmza provası yapıyorum. Ciddi iş bu.", "focused, comic")],
         "static medium two-shot under the lamp",
         t=[T("konaklama", 1100, "Pansiyon, 1 gece"), T("ulasim", 900, "Yakıt: Giresun-Trabzon")]),
   ],
   misafir={"tekneci": ("TEKNECİ", "BOATMAN, a 57-year-old Turkish man, sturdy, a grey beard, a yellow rain jacket and rubber boots",
                        "mature male voice, firm, Black Sea Turkish"),
            "fabrikaci": ("TESİS MÜDÜRÜ", "FACILITY MANAGER, a 41-year-old Turkish woman, a white hairnet cap, a white work coat, glasses",
                          "adult female voice, proud")},
   ay=AY, hava="rüzgar", kiyafet=K, urun="Giresun tombul fındığı, kiraz (yaz), Giresun pidesi; Giresun Adası, Giresun Kalesi",
   sponsor="Fındık işleme ya da kıyı turizmi alanında",
   kapak=("tekne", ["mert", "ali"], "In a small boat bouncing over choppy grey waves with spray flying, Mert laughs and points at a green island "
          "while Ali clings to the side soaked", "Dalgalarda zıplayan teknede gülen Mert ve sırılsıklam Ali."),
   yakinda=("kale", ["mert", "ali"], "Two silhouettes on a bench in a castle park at sunset bent over a notebook with small objects beside it, "
            "the sea glowing behind", "Gün batımında defterin üstüne eğilmiş iki silüet."),
   tiktok="Doğu Karadeniz'in tek adasına fırtınada gittik 🌊 #JozhStudios",
   ig=("Giresun'da Doğu Karadeniz'in tek adasına gitmek istedik; dalgalar 'hayır' dedi, tekneci 'kıyıdan bir tur' dedi. 🌊 Ali sırılsıklam!\n\n"
       "Giresun'un tombul fındığından kutu için 75 kilo aldık. Kalede kutunun son hâlini çizdik: çay, fındık, ezme, lokum. 📦\n\n"
       "Yarın Trabzon'da imza. Kasa: {KASA}"),
   tags=["#Giresun", "#TombulFındık", "#GiresunAdası"],
   son="Yarın Trabzon'da imza günü.",
   teaser="Fırtınada bir tekne, tombul fındık ve imza provası. Bölüm 66: Giresun. Pek yakında.")

# ======================================================================= 67 TRABZON
EP(67, "Trabzon", "İmza",
   "Sümela'da sabah, Akçaabat köftesi, yazılı sözleşme ve yüzde otuz peşin.",
   "Trabzon'da sabah sisin içinde kayalığa oyulmuş Sümela Manastırı'na bakarlar. Öğlen Akçaabat köftesi ve muhlama yerler. Öğleden sonra "
   "Selma Hanım'ın şirketinde sözleşme masaya konur: 300 Karadeniz Kutusu, kutusu 900 TL, yüzde otuz peşin, kalanı teslimde. İki imza atılır, "
   "peşinat kasaya girer. Mert imzadan sonra Ali'ye sarılır: 'Kâğıtla!' Akşam Uzungöl yerine Rize yolunu seçerler; çay ve teslim tarihi "
   "beklemektedir.",
   {"sumela": ("Sümela Manastırı manzarası", "the Sümela Monastery built into a steep cliff face in the Altındere valley near Trabzon, wrapped in "
               "morning mist, dense green forest below, a viewing path"),
    "kofteci": ("Akçaabat köftecisi", "an Akçaabat meatball restaurant: plates of grilled köfte with piyaz and peppers, a small pan of bubbling "
                "muhlama (cheese and cornmeal), wooden tables"),
    "ofis": ("Şirket toplantı odası", "a modern meeting room of a company in Trabzon: a long table, two printed contracts, pens, a window with "
             "a view of the city and the sea"),
    "sahil": ("Trabzon sahili", "the Trabzon seaside at dusk: a promenade, the old white pickup truck parked, the sea and the city lights")},
   [
       S("08:30 sabah", "sumela", ["mert", "ali"], "Kayadaki Manastır",
         "Sisin içinde kayaya oyulmuş Sümela Manastırı'na bakarlar.",
         "Mert and Ali stop on the forest path and look up; the mist parts slowly to reveal the monastery clinging to the cliff face; Mert's "
         "mouth opens; Ali raises his phone but then lowers it to just look.",
         [("mert", "Kayanın içine nasıl yapmışlar bunu?", "awed whisper"),
          ("ali", "Sabırla. Yine sabırla.", "smiling")],
         "slow crane-up through the trees to the cliff", h="sis"),
       S("12:30 iç-gündüz", "kofteci", ["mert", "ali"], "Muhlama",
         "Akçaabat köftesi ve muhlama yerler. Mert muhlamanın uzayan peynirini kaşıkla çekiştirir.",
         "Mert lifts a spoonful of muhlama and the melted cheese stretches longer and longer; Ali watches the stretch with fascination as it "
         "reaches arm's length.",
         [("mert", "Ali, peynir bitmiyor! Sözleşme kadar uzun!", "laughing"),
          ("ali", "İmzadan önce peynirle oynama.", "laughing")],
         "static medium two-shot at the table",
         t=T("yemek", 1000, "Akçaabat köftesi ve muhlama")),
       S("15:00 iç-gündüz", "ofis", ["mert", "ali", "selma"], "Sözleşme Masada",
         "Selma Hanım sözleşmeyi masaya koyar. Ali maddeleri tek tek okur; Mert bu kez acele etmez.",
         "Selma slides two printed contracts across the long table; Ali reads each page slowly with his finger along the lines; Mert sits with his "
         "hands folded, calm, glancing at Ali.",
         [("selma", "Üç yüz kutu, kutusu dokuz yüz. Yüzde otuz peşin, kalanı teslimde.", "professional"),
          ("ali", "Teslim tarihi yirmi gün sonra. Kabul ediyoruz.", "careful")],
         "slow lateral dolly along the table"),
       S("15:20 iç-gündüz", "ofis", ["mert", "ali", "selma"], "İki İmza",
         "İki imza atılır, peşinat kasaya girer. Mert imzadan sonra Ali'ye sarılır.",
         "Ali signs the contract, then Mert signs carefully; Selma signs and shakes their hands; the moment she leaves the frame, Mert hugs Ali "
         "tightly and whispers.",
         [("selma", "Hayırlı olsun. Peşinat bugün hesabınızda.", "smiling"),
          ("mert", "Kâğıtla Ali! Bu sefer kâğıtla!", "joyful whisper")],
         "static medium three-shot, then push-in on the hug",
         t=T("satis", 81000, "Karadeniz Kutusu kurumsal sipariş, %30 peşinat (300 x 900 TL'nin %30'u)"),
         kurgu="Şirket kurgusaldır; gerçek bir şirketi temsil etmez. Gerçek bir iş birliği olursa sahne yeniden yazılır."),
       S("18:30 akşam", "sahil", ["mert", "ali"], "Uzungöl mü, Rize mi?",
         "Akşam sahilde Mert Uzungöl'ü görmek ister; Ali takvimi gösterir. Birlikte Rize'yi seçerler.",
         "Mert points inland toward the mountains with a hopeful face; Ali shows him a calendar page in the notebook; Mert looks, sighs, then "
         "smiles and points the other way toward the coast road.",
         [("mert", "Uzungöl çok yakın Ali...", "hopeful"),
          ("ali", "Teslim yirmi gün sonra. Önce çay, sonra göl.", "gentle")],
         "static medium two-shot on the promenade", h="bulutlu"),
       S("21:00 akşam", "sahil", ["mert", "ali"], "Ortak Karar",
         "Mert kararı onaylar: önce iş. Ali, Uzungöl'ü finalden sonra gitmek üzere deftere yazar.",
         "Ali writes something at the bottom of the notebook page and shows Mert; Mert reads it and laughs, then they climb into the pickup.",
         [("ali", "Yazdım: 'Borç bitince Uzungöl.'", "smiling"),
          ("mert", "Kâğıtla söz. Artık kaçamazsın.", "laughing")],
         "static medium two-shot by the pickup",
         t=[T("konaklama", 1400, "Otel, 1 gece"), T("ulasim", 800, "Yakıt: Trabzon-Rize")]),
   ],
   misafir={"selma": ("SELMA HANIM", "SELMA, a 40-year-old Turkish company manager, short dark hair, a navy blazer over a white blouse, a thin "
                      "silver watch", "adult female voice, professional, warm")},
   ay=AY, hava="bulutlu", kiyafet=K, urun="Akçaabat köftesi, muhlama, hamsi, Trabzon tereyağı; Sümela Manastırı, Uzungöl",
   sponsor="Karadeniz mutfağı, kurumsal hediye ya da turizm alanında",
   kapak=("ofis", ["mert", "ali", "selma"], "Mert and Ali sign a printed contract at a long meeting table with a sea view while Selma smiles, Mert's "
          "signature careful and proud", "Deniz manzaralı toplantı masasında sözleşmeyi imzalayan Mert ve Ali."),
   yakinda=("sumela", ["mert", "ali"], "A monastery clinging to a sheer cliff slowly revealed through thick mist, two tiny silhouettes on a forest "
            "path below looking up", "Sisin içinden beliren kayadaki manastır ve aşağıda iki küçük silüet."),
   tiktok="Bu sefer kâğıtla! ✍️ 300 kutuluk sözleşme #JozhStudios",
   ig=("Trabzon'da Sümela sisin içinden belirdi, muhlamanın peyniri bitmedi. 🧀\n\n"
       "Ve büyük an: 300 Karadeniz Kutusu için yazılı sözleşme! Yüzde otuz peşin, kalanı teslimde. İki imza. ✍️ Mert'in tek cümlesi: 'Kâğıtla!'\n\n"
       "Uzungöl borç bitince (deftere yazıldı 😄). Kasa: {KASA}"),
   tags=["#Trabzon", "#Sümela", "#Sözleşme"],
   son="Sözleşme imzalandı. Teslim yirmi gün sonra. Sırada Rize'nin çayı.",
   teaser="Kayadaki manastır, uzayan peynir ve iki imza. Bölüm 67: Trabzon. Pek yakında.")

# ======================================================================= 68 RİZE
EP(68, "Rize", "Çay ve Kutu",
   "Çay bahçeleri, çay fabrikası, Ayder'de yağmur ve 300 kutunun hazırlanması.",
   "Rize'de sabah dik çay bahçelerinde son hasadı yapan bir aileyle tanışırlar; makasla çay kesmeyi denerler. Bir çay fabrikasında yaş "
   "yaprağın soldurulup kıvrılarak siyah çaya dönüştüğünü öğrenir, 75 kilo çay alırlar. Kiraladıkları bir depoda 300 Karadeniz Kutusu'nu "
   "hazırlayıp Trabzon'a gönderirler. Akşam Ayder yaylasına çıkan yolda yağmur başlar; ahşap bir yayla evinde feretiko denen Rize bezinden "
   "bir örtünün altında çay içerler.",
   {"bahce": ("Dik çay bahçesi", "a steep tea plantation on hills above Rize: dense rows of bright green tea bushes on terraces, mist on the "
              "hilltops, a small monorail cart for tea sacks"),
    "fabrika": ("Çay fabrikası", "a tea factory in Rize: withering troughs of green leaves, rolling machines, conveyor belts carrying dark "
                "fermenting leaves, the smell of tea, workers far in the background"),
    "depo": ("Kiralık depo", "a rented storage room in Rize: long tables with 300 kraft gift boxes being filled with tea packs, hazelnut "
             "packs, hazelnut paste jars and lokum boxes, rain on the window"),
    "ayder": ("Ayder yayla evi", "a wooden highland house in Ayder at dusk: a wooden porch, a striped red feretiko cloth on the table, tea "
              "glasses, fog drifting through dark pine forest, rain")},
   [
       S("08:30 sabah", "bahce", ["mert", "ali", "caykadin"], "Son Hasat",
         "Dik çay bahçesinde son hasadı yapan Fadime Abla, çay makasıyla nasıl kesileceğini gösterir.",
         "Fadime cuts the top leaves of tea bushes with a pair of tea shears with a basket on her back; Mert tries the shears and almost slips on "
         "the steep slope; Ali grabs a bush to stay upright, laughing.",
         [("caykadin", "Yamaçta ayağını sağlam bas, sonra kes.", "teaching, amused"),
          ("mert", "Abla, yamaç beni kesiyor!", "slipping, laughing")],
         "slow tracking shot across the steep terraces", h="sis"),
       S("11:00 iç-gündüz", "fabrika", ["mert", "ali", "fabrikaci"], "Soldurma, Kıvırma",
         "Çay fabrikasında yaş yaprağın soldurulup kıvrılarak siyah çaya dönüştüğünü öğrenir, 75 kilo çay alırlar.",
         "The factory supervisor lifts a handful of dark rolled tea leaves from the conveyor and lets them fall; Ali smells them; Mert reads a "
         "number on his notebook to the supervisor and they shake hands.",
         [("fabrikaci", "Soldurma, kıvırma, oksitlenme, kurutma. Kilosu iki yüz altmış.", "expert"),
          ("ali", "Yetmiş beş kilo, üç yüz kutuya.", "decisive")],
         "slow tracking shot along the conveyor",
         t=U(75, "kg", 260, "alis", "Rize siyah çayı ({adet} kg x {fiyat} TL)")),
       S("13:00 iç-gündüz", "depo", ["mert", "ali"], "Üç Yüz Karadeniz Kutusu",
         "Kiralık depoda 300 kutuyu doldururlar: çay, tombul fındık, fındık ezmesi, Safranbolu lokumu.",
         "Mert and Ali work along the long tables in a rhythm: Mert places tea and hazelnut packs, Ali adds a jar of hazelnut paste and lokum and "
         "closes each lid; the stack of finished boxes grows behind them.",
         [("ali", "Çay, fındık, ezme, lokum, kapak.", "rhythmic"),
          ("mert", "İzmir'de yüz yirmi kutuda ölmüştük. Bak şimdi üç yüz!", "proud, tired")],
         "slow dolly along the table",
         t=[U(300, "kutu", 60, "diger_gider", "Karadeniz Kutusu ambalajı ({adet} x {fiyat} TL)"), T("diger_gider", 1500, "Depo kirası, 1 gün")]),
       S("16:00 iç-gündüz", "depo", ["mert", "ali"], "Kamyon Trabzon'a",
         "Kutular bir nakliye kamyonuyla Trabzon'a gönderilir. Teslim tarihinden çok önce.",
         "Mert and Ali carry the last boxes to the open door where stacked pallets wait; Ali signs a delivery paper on a clipboard held by an "
         "unseen driver's hand and keeps a copy.",
         [("ali", "Teslim tutanağı da imzalı. Bir kopyası defterde.", "satisfied"),
          ("mert", "Kâğıt, kâğıt, kâğıt. Yeni hayatım bu.", "laughing")],
         "static wide shot at the depot door", h="yağmur",
         t=[T("diger_gider", 6000, "Nakliye: Rize-Trabzon, 300 kutu"), T("yemek", 800, "Öğle yemeği")]),
       S("19:00 akşam", "ayder", ["mert", "ali"], "Feretiko",
         "Ayder'de ahşap bir yayla evinde Rize bezinin kırmızı çizgili örtüsü altında çay içerler. Dışarıda yağmur ve sis.",
         "Mert and Ali sit on the wooden porch with a striped red feretiko cloth on the table and tea glasses steaming; fog drifts through the "
         "pines; Mert raises his glass toward Ali.",
         [("mert", "Rize'de, Rize çayı, Rize bezinin üstünde.", "content"),
          ("ali", "Ve kutular yolda. Bugün güzel bir gün.", "peaceful")],
         "slow dolly-in along the porch", h="yağmur"),
       S("22:00 iç-gece", "ayder", ["mert", "ali"], "Selma Hanım'dan",
         "Gece Selma Hanım'dan mesaj gelir: kutular teslim alınmıştır, kalan ödeme Artvin'e varmadan yapılacaktır.",
         "Ali reads a message by the light of the wood stove and smiles widely; Mert, half asleep under a thick blanket, lifts his head and sees "
         "Ali's smile, then lies back with a grin.",
         [("ali", "Kutular teslim alındı. Kalan ödeme yarın.", "relieved"),
          ("mert", "Yazılı iş uyutuyor Ali. Ben uyudum bile.", "sleepy")],
         "static medium two-shot by the stove",
         t=[T("konaklama", 1600, "Ayder'de yayla evi, 1 gece"), T("ulasim", 900, "Yakıt: Rize-Artvin")]),
   ],
   misafir={"caykadin": ("FADİME ABLA", "FADİME, a 54-year-old Turkish tea farmer, strong and lean, a colorful Black Sea headscarf, a wicker "
                         "basket on her back, rubber boots", "middle-aged female voice, teaching, amused, Rize Turkish"),
            "fabrikaci": ("FABRİKA SORUMLUSU", "TEA FACTORY SUPERVISOR, a 48-year-old Turkish man, a white work coat, a cap, a grey mustache",
                          "adult male voice, expert")},
   ay=AY, hava="yağmur", kiyafet=K, urun="Rize çayı, Rize bezi (feretiko), Anzer balı; Ayder Yaylası",
   sponsor="Çay, Rize bezi ya da yayla turizmi alanında",
   kapak=("bahce", ["mert", "ali", "caykadin"], "On a steep misty tea plantation, Mert almost slips holding tea shears while Ali grabs a bush and "
          "Fadime laughs with a basket on her back", "Dik çay bahçesinde kaymak üzere olan Mert ve gülen Fadime Abla."),
   yakinda=("ayder", ["mert", "ali"], "Two silhouettes on a wooden porch in thick mountain fog, steam rising from tea glasses on a striped red "
            "cloth, pine trees fading into white", "Sisli yayla evinin verandasında çay buharı ve iki silüet."),
   tiktok="300 Karadeniz Kutusu yola çıktı 📦🍵 #JozhStudios",
   ig=("Rize'de dik çay bahçelerinde Fadime Abla'yla son hasadı yaptık (Mert az kalsın yuvarlanıyordu 😅). Fabrikada yaş yaprağın siyah çaya dönüşünü gördük. 🍵\n\n"
       "Depoda 300 Karadeniz Kutusu hazırlandı ve Trabzon'a gönderildi; teslim tutanağı imzalı! ✍️ Ayder'de feretikonun üstünde çay içtik.\n\nKasa: {KASA}"),
   tags=["#Rize", "#RizeÇayı", "#Ayder"],
   son="Kutular teslim edildi. Kalan ödeme yarın gelecek.",
   teaser="Dik yamaçlar, siyah çay, üç yüz kutu ve sisin içinde bir veranda. Bölüm 68: Rize. Pek yakında.")

# ======================================================================= 69 ARTVİN
EP(69, "Artvin", "Kafkas Arısı",
   "Kalan ödeme gelir; Karagöl'de sonbahar, Macahel'de Kafkas arısı balı.",
   "Artvin'e Çoruh vadisinden kıvrılan yollarla girerken Selma Hanım'ın şirketinden kalan ödeme gelir; Mert kamyoneti kenara çekip bağırır. "
   "Borçka Karagöl'ün sonbahar renkleri içinde yürürler. Macahel'de, Kafkas arısının yaşadığı vadide bir arıcıdan 30 kilo bal alırlar. "
   "Akşam Ali hesap yapar: Çorum'daki taksit için para hazırdır. Ama hava raporu kötüdür: Bayburt yolunda kar beklenmektedir.",
   {"yol": ("Çoruh vadisi yolu", "a winding mountain road above the deep Çoruh river valley near Artvin: steep rocky slopes, autumn colors, "
            "the old white pickup truck pulled over at a bend"),
    "karagol": ("Borçka Karagöl", "Borçka Karagöl lake in autumn: a dark mirror-still lake surrounded by forest in deep red, orange and green, "
                "mist, a wooden path along the shore"),
    "macahel": ("Macahel arılığı", "a remote apiary in the Macahel valley near Artvin: colorful wooden beehives on a green slope, wooden "
                "village houses, forested mountains"),
    "pansiyon": ("Pansiyon odası", "a wooden guesthouse room in Artvin at night: honey jars in a crate, a phone showing a weather map, rain")},
   [
       S("09:00 sabah", "yol", ["mert", "ali"], "Kalan Ödeme",
         "Çoruh vadisinin yolunda Ali'nin telefonuna kalan ödeme düşer. Mert kamyoneti kenara çekip bağırır.",
         "Mert pulls the pickup over at a bend above the deep valley, jumps out and shouts into the valley with both fists raised; Ali stands by the "
         "open door holding up the phone, laughing.",
         [("ali", "Yüz seksen dokuz bin! Kalan ödeme geldi!", "excited"),
          ("mert", "Kâğıt kazandı! Vadi duysun!", "shouting with joy")],
         "slow crane-up from the pickup revealing the valley",
         t=T("satis", 189000, "Karadeniz Kutusu kurumsal sipariş, teslimde kalan %70 (300 x 900 TL'nin %70'i)")),
       S("11:30 sabah", "karagol", ["mert", "ali"], "Karagöl",
         "Borçka Karagöl'ün kıyısında sonbahar ormanının içinde yürürler.",
         "Mert and Ali walk along the wooden path by the dark still lake that reflects the red and orange forest; Mert stops and skips a stone, "
         "breaking the perfect mirror; Ali sighs theatrically.",
         [("ali", "Ayna gibiydi, bozdun.", "mock annoyed"),
          ("mert", "Kutlama taşı Ali. Göl de sevindi.", "grinning")],
         "slow tracking shot along the shore", h="sis"),
       S("14:00 öğle", "macahel", ["mert", "ali", "arici"], "Kafkas Arısı",
         "Macahel'de arıcı Temel Amca, Kafkas arısının bu vadide korunduğunu anlatır. Arılar sakin ve uysaldır.",
         "Temel lifts the lid of a colorful hive without a veil, calm bees crawling on the frame; Mert holds very still with his eyes wide; Ali "
         "leans closer, fascinated.",
         [("arici", "Kafkas arısı uysaldır, çalışkandır. Bu vadide korunur.", "proud"),
          ("mert", "Amca, arılar benden daha sakin.", "whispering, frozen")],
         "slow push-in on the frame with bees"),
       S("15:00 öğle", "macahel", ["ali", "arici"], "Otuz Kilo Bal",
         "Temel Amca'dan 30 kilo Kafkas arısı balı alırlar. İç Anadolu'da satılacaktır.",
         "Temel fills large jars with golden honey from a spout and stacks them in a crate; Ali counts money into his hand and they shake hands.",
         [("arici", "Kilosu bin iki yüz. Az bal, temiz bal.", "proud"),
          ("ali", "Otuz kilo alıyoruz amca. Kışın İç Anadolu'ya.", "decisive")],
         "static medium two-shot at the crate",
         t=[U(30, "kg", 1200, "alis", "Macahel Kafkas arısı balı ({adet} kg x {fiyat} TL)"), T("yemek", 800, "Öğle yemeği")]),
       S("20:00 iç-gece", "pansiyon", ["mert", "ali"], "Hazır",
         "Akşam Ali hesap yapar: Çorum'daki altıncı taksit için para hazırdır.",
         "Ali shows Mert the notebook total by lamp light; Mert takes the notebook, reads it twice, then hugs it to his chest dramatically.",
         [("ali", "Çorum'daki taksit hazır. Üstü bile kalıyor.", "proud"),
          ("mert", "Bu defteri çerçeveletip asacağım.", "dramatic, happy")],
         "static medium two-shot at the table"),
       S("22:00 iç-gece", "pansiyon", ["mert", "ali"], "Kar Raporu",
         "Ali hava raporuna bakar: Bayburt yolunda kar beklenmektedir. Kamyonetin kar lastiği yoktur.",
         "Ali turns his phone toward Mert showing a weather map with snow symbols; Mert's smile fades; he looks out of the rainy window toward the "
         "dark mountains.",
         [("ali", "Bayburt yolunda kar. Kamyonetin kar lastiği yok.", "worried"),
          ("mert", "O zaman sabah ilk iş lastik. Ortak karar?", "serious")],
         "slow push-in to the phone screen",
         t=[T("konaklama", 1200, "Pansiyon, 1 gece"), T("ulasim", 1200, "Yakıt: Artvin-Bayburt")]),
   ],
   misafir={"arici": ("TEMEL AMCA", "TEMEL, a 69-year-old Turkish beekeeper, wiry, a white mustache, a knitted cap, a patched wool jacket, no "
                      "veil", "elderly male voice, proud, Artvin Black Sea Turkish")},
   ay=AY, hava="sis", kiyafet=K, urun="Kafkas arısı balı (Macahel), Artvin yayla ürünleri; Borçka Karagöl, Çoruh vadisi",
   sponsor="Bal, arıcılık ya da doğa turizmi alanında",
   kapak=("karagol", ["mert", "ali"], "Mert and Ali on a wooden path by a mirror-still dark lake surrounded by a blazing red and orange autumn "
          "forest, Mert skipping a stone across the reflection", "Sonbahar ormanını yansıtan Karagöl'de taş sektiren Mert."),
   yakinda=("pansiyon", ["mert"], "A phone screen glowing with a snowy weather map in a dark room, rain on the window, Mert's worried face "
            "reflected in the glass", "Karanlık odada kar haritası gösteren telefon ve camda endişeli yüz."),
   tiktok="Kâğıt kazandı! 189.000 TL ödeme geldi 📄🎉 #JozhStudios",
   ig=("Çoruh vadisinde telefon titredi: Karadeniz Kutusu'nun kalan ödemesi geldi! Mert kamyoneti kenara çekip vadiye bağırdı: 'Kâğıt kazandı!' 📄🎉\n\n"
       "Borçka Karagöl'de sonbahar, Macahel'de uysal Kafkas arıları. 30 kilo bal aldık. 🐝\n\nAma Bayburt yolunda kar var ve kamyonetin kar lastiği yok. Kasa: {KASA}"),
   tags=["#Artvin", "#Karagöl", "#KafkasArısı"],
   son="Bayburt yolunda kar bekleniyor ve kamyonetin kar lastiği yok.",
   teaser="Vadiye bağıran bir sevinç, uysal arılar ve bir kar raporu. Bölüm 69: Artvin. Pek yakında.")

# ======================================================================= 70 BAYBURT
EP(70, "Bayburt", "Kar Yolu",
   "Kar lastiği, karda kalan kamyonet, Baksı Müzesi ve Çoruh kıyısında bir kale.",
   "Sabah Artvin'de kar lastiği taktırırlar. Bayburt'a giden dağ yolunda kar bastırır; kamyonet bir rampada kayar ve kenarda kalır. Zincir "
   "takmayı bilmeyen iki arkadaşa yoldan geçen bir kamyon şoförü yardım eder. Bayburt'ta Baksı Müzesi'nde bir köyün tepesine kurulmuş çağdaş "
   "sanat ve el sanatları müzesini görürler. Kafkas arısı balının bir kısmını bir kahvaltıcıya satarlar. Akşam karlı Bayburt Kalesi'nin "
   "eteğinde Çoruh'un sesini dinlerler.",
   {"lastikci": ("Lastikçi", "a tire shop garage in Artvin in the early morning: stacks of winter tires, a tire changer machine, the old white "
                 "pickup truck on a jack"),
    "yol": ("Karlı dağ yolu", "a snowy mountain road to Bayburt: falling snow, a white landscape, low visibility, the old white pickup truck "
            "stopped at the roadside with hazard lights on"),
    "baksi": ("Baksı Müzesi", "the Baksı Museum on a hilltop near Bayburt: a modern stone and glass building blending with a village, snowy "
              "hills all around, a gallery with traditional handicrafts and contemporary art"),
    "kahvalti": ("Bayburt kahvaltıcısı", "a small breakfast and restaurant place in Bayburt with a warm stove, tables with honey and butter"),
    "kale": ("Bayburt Kalesi eteği", "the foot of Bayburt Castle at dusk with snow on the old walls on a rocky hill above the Çoruh river, "
             "streetlights coming on")},
   [
       S("08:00 sabah", "lastikci", ["mert", "ali", "lastikci"], "Kar Lastiği",
         "Artvin'de bir lastikçide kar lastiği taktırırlar. Usta zinciri de verir.",
         "The tire man spins the wrench to fasten a winter tire on the pickup's wheel and tosses a bag of snow chains to Mert; Mert catches it and "
         "looks at it confused; Ali pays at the counter.",
         [("lastikci", "Kar lastiği tamam. Zinciri de koydum, lazım olur.", "practical"),
          ("mert", "Usta, bu zincir nasıl takılıyor?", "confused")],
         "static medium three-shot in the garage",
         t=T("diger_gider", 9500, "Kar lastiği (4 adet), montaj ve zincir")),
       S("11:00 sabah", "yol", ["mert", "ali"], "Rampada",
         "Bayburt yolunda kar bastırır. Kamyonet bir rampada kayar ve kenarda kalır. İkisi de zinciri takmayı bilmez.",
         "The pickup slides slowly sideways on a snowy slope and stops at the roadside; Mert and Ali get out into the falling snow and kneel by a "
         "wheel holding the tangled chains, completely lost.",
         [("ali", "Bu zincir sözleşmeden zor.", "freezing, frustrated"),
          ("mert", "Lastikçiye sormuştum, cevap vermeden gitti!", "panicking")],
         "static wide shot in the snow, hazard lights blinking", h="kar"),
       S("11:30 sabah", "yol", ["mert", "ali", "sofor"], "Kamyon Şoförü",
         "Yoldan geçen bir kamyon şoförü durur ve zinciri iki dakikada takar.",
         "A big truck stops behind them; the driver walks over through the snow, takes the chains from Mert's hands and fits them around the wheel "
         "with quick practiced moves; Mert and Ali watch, then shake his gloved hand.",
         [("sofor", "Kırk yıldır bu yolları geçerim. Böyle takılır, iki dakika.", "calm, kind"),
          ("mert", "Abi, Cemil Abi gibi konuşuyorsun ama çok daha iyisin.", "grateful, joking")],
         "slow push-in on the chains being fitted", h="kar"),
       S("14:30 iç-gündüz", "baksi", ["mert", "ali"], "Köyün Tepesinde Müze",
         "Baksı Müzesi'nde bir köyün tepesine kurulmuş, el sanatlarıyla çağdaş sanatı bir araya getiren galeriyi gezerler.",
         "Mert and Ali walk slowly through a gallery where traditional handwoven pieces hang beside contemporary artworks; through the large window "
         "the snowy hills stretch out; Ali stops in front of an old weaving.",
         [("ali", "Eski ile yeni aynı duvarda. Kutularımız gibi.", "thoughtful"),
          ("mert", "Köyün tepesinde bir müze... cesaretli iş.", "impressed")],
         "slow tracking shot through the gallery", h="kar"),
       S("17:00 iç-gündüz", "kahvalti", ["ali", "kahvaltici"], "Bal Satışı",
         "Bayburt'ta bir kahvaltıcı 10 kilo Kafkas arısı balı alır.",
         "The breakfast place owner tastes honey from a spoon by the warm stove and nods slowly; Ali sets a jar on the table and receives money.",
         [("kahvaltici", "Macahel balı buralarda az bulunur. On kilo alırım.", "pleased"),
          ("ali", "Kilosu bin altı yüz. Kış balı olsun.", "warm")],
         "static medium two-shot by the stove",
         t=[U(10, "kg", 1600, "satis", "Macahel Kafkas arısı balı, kahvaltıcıya ({adet} kg x {fiyat} TL)"), T("yemek", 900, "Öğle yemeği")]),
       S("19:30 akşam", "kale", ["mert", "ali"], "Çoruh'un Sesi",
         "Akşam karlı kalenin eteğinde Çoruh'un sesini dinlerler. Mert zincir takmayı öğrenmeye söz verir.",
         "Mert and Ali stand by the railing below the snowy castle walls, the river rushing below in the dark; Mert mimes fitting a chain with his "
         "hands; Ali laughs and nods.",
         [("mert", "Yarın sabah zinciri ben takacağım. Öğrendim.", "determined"),
          ("ali", "Ben de yanında fotoğraf çekeceğim. Kanıt lazım.", "teasing")],
         "slow crane-up to the snowy castle", h="kar",
         t=[T("konaklama", 1200, "Otel, 1 gece"), T("ulasim", 900, "Yakıt: Bayburt-Gümüşhane")]),
   ],
   misafir={"lastikci": ("LASTİKÇİ", "TIRE MAN, a 50-year-old Turkish man, stout, oil-stained overalls, a woolen cap", "adult male voice, practical"),
            "sofor": ("KAMYON ŞOFÖRÜ", "TRUCK DRIVER, a 60-year-old Turkish man, big, a thick grey beard, a sheepskin-lined jacket, work gloves",
                      "elderly male voice, calm and kind"),
            "kahvaltici": ("KAHVALTICI", "BREAKFAST PLACE OWNER, a 45-year-old Turkish man, round face, a black mustache, a knitted vest",
                           "adult male voice, pleased")},
   ay=AY, hava="kar", kiyafet=K, urun="Bayburt tava, tereyağı ve yayla ürünleri; Baksı Müzesi, Bayburt Kalesi, Çoruh",
   sponsor="Yayla ürünleri, kültür sanat ya da kış turizmi alanında",
   kapak=("yol", ["mert", "ali", "sofor"], "In heavy falling snow on a mountain road, a big bearded truck driver fits chains on the pickup's wheel "
          "while Mert and Ali watch shivering and grateful, hazard lights glowing", "Karlı dağ yolunda zinciri takan kamyon şoförü ve üşüyen Mert ile Ali."),
   yakinda=("yol", ["mert", "ali"], "A small white pickup stopped on a white mountain road in a blizzard, two silhouettes kneeling by a wheel, "
            "orange hazard lights blinking in the snow", "Tipide beyaz yolda duran kamyonet ve tekerleğin yanında diz çökmüş iki silüet."),
   tiktok="Karda kaldık, zincir takmayı bilmiyorduk ❄️⛓️ #JozhStudios",
   ig=("Kar lastiği taktırdık, zinciri de aldık... ama takmayı bilmiyorduk. ❄️ Bayburt yolunda kamyonet kaydı, kar bastırdı.\n\n"
       "Bir kamyon şoförü durdu ve zinciri iki dakikada taktı: 'Kırk yıldır bu yolları geçerim.' 🚛❤️ Baksı Müzesi'nde eski ve yeni aynı duvardaydı.\n\nKasa: {KASA}"),
   tags=["#Bayburt", "#BaksıMüzesi", "#Kar"],
   son="Mert yarın sabah zinciri kendisi takacak. Ali kanıt için fotoğraf çekecek.",
   teaser="Kar, bir rampa, bir zincir ve yolda bir yardım eli. Bölüm 70: Bayburt. Pek yakında.")

# ======================================================================= 71 GÜMÜŞHANE
EP(71, "Gümüşhane", "Pestil ve Köme",
   "Zinciri Mert takar; Karaca Mağarası, pestil ve köme atölyesi.",
   "Sabah Mert zinciri kendisi takar, Ali fotoğrafını çeker. Gümüşhane'de Karaca Mağarası'nın renkli sarkıtlarını görürler. Bir pestil "
   "atölyesinde dut ve üzüm pekmezinin bezlere sürülüp kurutularak pestile, cevizin pekmezle köme'ye dönüştüğünü izler, 80 kilo alırlar. "
   "Kafkas arısı balının bir kısmı da satılır. Akşam Kelkit'e inen dağ yolunda kar diner, gökyüzü açılır.",
   {"otopark": ("Otel otoparkı", "a snowy hotel parking lot in Bayburt in the early morning: the old white pickup truck, snow on the ground, a "
                "clear cold sky"),
    "magara": ("Karaca Mağarası", "inside Karaca Cave near Gümüşhane: colorful stalactites and stalagmites in shades of white, pink and "
               "orange, lit walkway, damp air"),
    "atolye": ("Pestil ve köme atölyesi", "a pestil and köme workshop in Gümüşhane: thin sheets of fruit pestil drying on cloths on wooden "
               "racks, strings of walnuts coated in molasses (köme) hanging, a copper cauldron of grape molasses"),
    "zigana": ("Kelkit yolu", "a mountain road south of Gümüşhane toward Kelkit at sunset after a snowfall: snowy pine forest, the sky clearing into pink and gold, "
               "the old white pickup truck driving")},
   [
       S("07:30 sabah", "otopark", ["mert", "ali"], "Zinciri Mert Taktı",
         "Sabah Mert zinciri kendisi takar. Ali fotoğraf çeker, Mert poz verir.",
         "Mert kneels in the snow by the wheel and fits the chain around the tire with concentrated, careful moves; he stands up proudly with his "
         "arms crossed while Ali takes a photo, laughing.",
         [("mert", "Bitti! İki dakika... tamam, on iki dakika.", "proud, out of breath"),
          ("ali", "Kanıt alındı. Deftere de yazıyorum.", "laughing")],
         "static medium two-shot by the wheel", h="kar"),
       S("10:30 iç-gündüz", "magara", ["mert", "ali"], "Renkli Sarkıtlar",
         "Karaca Mağarası'nın pembe, turuncu ve beyaz sarkıtlarının arasında yürürler.",
         "Mert and Ali walk along the lit walkway among colorful stalactites; Mert stops and points at a pink formation shaped like a curtain; Ali "
         "looks up with his mouth open.",
         [("mert", "Pembe bir perde gibi! Taştan!", "amazed"),
          ("ali", "Doğa da ustalık istiyor. Binlerce yıl.", "awed")],
         "slow crane-up along the formations",
         t=U(2, "kişi", 200, "diger_gider", "Karaca Mağarası giriş ({adet} x {fiyat} TL)")),
       S("13:00 iç-gündüz", "atolye", ["mert", "ali", "pestilci"], "Bezde Kuruyan Meyve",
         "Pestil atölyesinde dut ve üzüm pekmezinin bezlere ince sürülüp kurutulduğunu görürler.",
         "The pestil maker spreads a thin layer of fruit paste on a cloth with a wooden spatula, then peels a dried pestil sheet from another rack "
         "and holds it up to the light; it glows amber; Mert tears off a piece and tastes it.",
         [("pestilci", "Dut ve pekmez. İnce sürersin, güneşte ve rüzgârda kurutursun.", "proud"),
          ("mert", "Bu pestil değil, meyveden yapılmış ipek!", "amazed")],
         "slow push-in on the glowing pestil sheet"),
       S("14:00 iç-gündüz", "atolye", ["ali", "pestilci"], "Seksen Kilo",
         "Pestil ve köme karışık 80 kilo alırlar. Kafkas arısı balından 10 kiloyu da atölyenin dükkânı alır.",
         "The pestil maker stacks folded pestil sheets and strings of köme into boxes; Ali hands him money and receives an envelope back for the "
         "honey jars he places on the counter.",
         [("pestilci", "Pestil köme karışık seksen kilo, dört yüzden. Bal da bana.", "businesslike"),
          ("ali", "Takas gibi oldu, ama hepsi defterde.", "smiling")],
         "static medium two-shot at the counter",
         t=[U(80, "kg", 400, "alis", "Gümüşhane pestili ve kömesi ({adet} kg x {fiyat} TL)"),
            U(10, "kg", 1600, "satis", "Macahel Kafkas arısı balı, atölye dükkânına (10 kg x 1.600 TL)"), T("yemek", 800, "Öğle yemeği")]),
       S("17:00 gün batımı", "zigana", ["mert", "ali"], "Gökyüzü Açılıyor",
         "Kelkit'e inen dağ yolunda kar diner, gökyüzü pembe ve altın rengine açılır.",
         "The pickup drives slowly down the snowy mountain road as the clouds part into pink and gold; Mert, driving, slows down; Ali rolls down "
         "the window and breathes in the cold air.",
         [("ali", "Kar durdu. Gökyüzü açıldı.", "relieved"),
          ("mert", "Dağlar bize izin verdi Ali.", "grateful")],
         "smooth tracking shot alongside the pickup", h="serin"),
       S("20:30 akşam", "zigana", ["mert", "ali"], "Dört Şehir",
         "Akşam Ali sezonun son dört şehrini sayar: Gümüşhane, Tokat, Amasya, Çorum. Sonra İç Anadolu.",
         "Mert and Ali sit in the pickup cab parked at a roadside teahouse, steam on the windows; Ali counts on his fingers; Mert draws four dots "
         "on the fogged window and connects them.",
         [("ali", "Tokat, Amasya, Çorum. Sonra İç Anadolu ve son taksit.", "focused"),
          ("mert", "Buğulu camda çizdim, silinmeden bitirelim.", "smiling")],
         "static medium two-shot through the fogged windshield",
         t=[T("konaklama", 1100, "Pansiyon, 1 gece"), T("ulasim", 1300, "Yakıt: Gümüşhane-Tokat")]),
   ],
   misafir={"pestilci": ("PESTİL USTASI", "PESTIL MAKER, a 61-year-old Turkish man, slim, a grey beard, a knitted cap, a brown apron stained with "
                         "molasses", "elderly male voice, proud, Gümüşhane Turkish")},
   ay=AY, hava="kar", kiyafet=K, urun="Gümüşhane pestili ve kömesi, dut; Karaca Mağarası, Zigana",
   sponsor="Pestil, köme ya da mağara turizmi alanında",
   kapak=("atolye", ["mert", "ali", "pestilci"], "The pestil maker holds up a glowing amber sheet of dried fruit pestil to the light while Mert "
          "tears off a piece in amazement, strings of köme hanging around them", "Işığa tutulan amber renkli pestil ve hayran Mert."),
   yakinda=("magara", ["mert"], "A curtain-shaped pink stalactite formation glowing in a dark cave, Mert's small silhouette pointing at it",
            "Karanlık mağarada parlayan pembe perde biçimli sarkıt."),
   tiktok="Zinciri bu sefer ben taktım! ⛓️ (12 dakika) #JozhStudios",
   ig=("Sabah zinciri Mert kendisi taktı: 'İki dakika... tamam, on iki.' ⛓️😂\n\n"
       "Karaca Mağarası'nda pembe taştan perdeler gördük. Gümüşhane'de dut pekmezinden pestil ve cevizli kömenin yapılışını izledik, 80 kilo aldık. 🍇\n\n"
       "Kelkit yolunda kar durdu, gökyüzü açıldı. Kasa: {KASA}"),
   tags=["#Gümüşhane", "#Pestil", "#KaracaMağarası"],
   son="Sezonun son dört şehri: Tokat, Amasya, Çorum.",
   teaser="On iki dakikada takılan zincir, pembe taştan perdeler ve meyveden ipek. Bölüm 71: Gümüşhane. Pek yakında.")

# ======================================================================= 72 TOKAT
EP(72, "Tokat", "Yazmanın Kalıbı",
   "Tokat kebabı, el baskısı yazma, Ballıca Mağarası ve pestil satışı.",
   "Tokat'ta sabah bir yazma atölyesinde ahşap kalıplarla bezlere desen basılmasını izlerler; Ali kalıbı ilk kez bastığında desen kayar, "
   "Mert güler, sonra kendi bastığı desen de kayar. 100 el baskısı yazma alırlar. Pestilin yarısı bir kuruyemişçiye satılır. Öğlen kuzu "
   "eti, patlıcan ve patatesle yapılan Tokat kebabını yerler. Ballıca Mağarası'nın sarkıtları arasında yürürler. Akşam Ali, İç Anadolu "
   "kutusunun ilk fikrini söyler.",
   {"yazma": ("Yazma atölyesi", "a hand-block printing workshop in Tokat: long tables with white cotton cloths, carved wooden printing blocks, "
              "trays of natural dye, finished patterned scarves hanging to dry"),
    "kuruyemis": ("Kuruyemişçi", "a dried fruit and nut shop in Tokat with sacks, jars and pestil sheets on the counter"),
    "kebap": ("Tokat kebapçısı", "a Tokat kebab restaurant: a tall vertical oven with hanging skewers of lamb, eggplant, potato and tomato "
              "slices, a plate of the finished kebab with garlic"),
    "ballica": ("Ballıca Mağarası", "inside Ballıca Cave near Tokat: large chambers with layered stalactites, cream and brown dripstone "
                "formations, a lit walkway")},
   [
       S("09:30 iç-gündüz", "yazma", ["mert", "ali", "yazmaci"], "Kayan Kalıp",
         "Yazma atölyesinde usta ahşap kalıpla bezlere desen basar. Ali'nin bastığı desen kayar, Mert güler; sonra onunki de kayar.",
         "The master presses a carved wooden block dipped in dye firmly onto white cloth and lifts it to reveal a crisp pattern; Ali tries and his "
         "pattern smudges; Mert laughs, tries himself and smudges even more; the master laughs.",
         [("yazmaci", "Kalıbı dik bas, bir kere bas, kaldır. Tereddüt ederse kayar.", "master"),
          ("mert", "Ali, benimki seninkinden de kötü!", "laughing")],
         "slow push-in on the block and the cloth"),
       S("10:30 iç-gündüz", "yazma", ["ali", "yazmaci"], "Yüz Yazma",
         "Ustanın elinden çıkan 100 el baskısı yazma alırlar.",
         "The master folds printed scarves with crisp patterns into a stack; Ali counts money into his hand and holds up one scarf to the window "
         "light, admiring it.",
         [("yazmaci", "Tanesi iki yüz elli. Bunlar bizim bastıklarımız, sizinkiler değil.", "teasing"),
          ("ali", "Bizimkileri hatıra diye saklıyoruz.", "laughing")],
         "static medium two-shot at the table",
         t=U(100, "yazma", 250, "alis", "Tokat el baskısı yazma ({adet} x {fiyat} TL)")),
       S("12:00 iç-gündüz", "kuruyemis", ["mert", "kuruyemisci"], "Pestil Tokat'ta",
         "Bir kuruyemişçi 40 kilo Gümüşhane pestili ve kömesini alır.",
         "The shopkeeper tears a piece of pestil and tastes it, nods and pulls money from the drawer; Mert places the boxes on the counter.",
         [("kuruyemisci", "Gümüşhane pestili kışın çok gider. Kırk kilo, altı yüzden.", "practical"),
          ("mert", "Hayırlı olsun. Kış tatlı geçsin.", "cheerful")],
         "static medium two-shot at the counter",
         t=U(40, "kg", 600, "satis", "Gümüşhane pestili ve kömesi, Tokat'ta ({adet} kg x {fiyat} TL)")),
       S("13:30 iç-gündüz", "kebap", ["mert", "ali"], "Tokat Kebabı",
         "Dikey fırında kuzu eti, patlıcan ve patatesle pişen Tokat kebabını yerler.",
         "The waiter's hand slides a plate of Tokat kebab with roasted eggplant, potato and lamb onto the table; Mert breathes in the garlic "
         "smell with eyes closed; Ali tears bread.",
         [("mert", "Patlıcan, patates, kuzu... bu kebap bir orkestra.", "blissful"),
          ("ali", "Sarımsak da şefi.", "smiling")],
         "static medium two-shot at the table",
         t=T("yemek", 1000, "Tokat kebabı")),
       S("16:00 iç-gündüz", "ballica", ["mert", "ali"], "Ballıca",
         "Ballıca Mağarası'nın katman katman sarkıtları arasında yürürler.",
         "Mert and Ali walk along the lit walkway through a huge chamber of layered cream and brown dripstones; Ali stops and touches the railing; "
         "Mert looks up at the ceiling.",
         [("ali", "Her katman bir mevsim.", "quiet"),
          ("mert", "Bizim yolculuğun da katmanları var: kayısı, fıstık, kutu.", "thoughtful")],
         "slow crane-up through the chamber",
         t=U(2, "kişi", 200, "diger_gider", "Ballıca Mağarası giriş ({adet} x {fiyat} TL)")),
       S("20:30 akşam", "kebap", ["mert", "ali"], "Son Kutu Fikri",
         "Akşam Ali, İç Anadolu için son kutunun ilk fikrini söyler: 'Final Kutusu.'",
         "Ali draws a box in the notebook and writes a few words inside it; Mert reads it and slowly nods with a growing smile.",
         [("ali", "Son sezona bir kutu: Final Kutusu. Her bölgeden bir şey.", "inspired"),
          ("mert", "Yedi bölge, bir kutu. Bu bizim hikâyemiz.", "moved")],
         "slow push-in on the notebook",
         t=[T("konaklama", 1200, "Otel, 1 gece"), T("ulasim", 800, "Yakıt: Tokat-Amasya")]),
   ],
   misafir={"yazmaci": ("YAZMA USTASI", "BLOCK-PRINT MASTER, a 65-year-old Turkish man, slim, a white mustache, dye-stained fingers, a dark "
                        "blue work apron", "elderly male voice, teasing master, Tokat Turkish"),
            "kuruyemisci": ("KURUYEMİŞÇİ", "SHOPKEEPER, a 52-year-old Turkish woman, round, a beige headscarf, an apron", "adult female voice")},
   ay=AY, hava="bulutlu", kiyafet=K, urun="Tokat yazması (el baskısı), Tokat kebabı, bez dokuma; Ballıca Mağarası, Gök Medrese",
   sponsor="El baskısı yazma ya da Tokat mutfağı alanında",
   kapak=("yazma", ["mert", "ali", "yazmaci"], "Mert and Ali laugh at their smudged block prints on white cloth while the master holds up a perfect "
          "crisp pattern beside them, colorful scarves drying above", "Kayan desenlerine gülen Mert ve Ali, kusursuz deseni gösteren usta."),
   yakinda=("ballica", ["mert", "ali"], "Two tiny silhouettes on a lit walkway inside a vast cave chamber of layered dripstones, warm light from "
            "below", "Katman katman sarkıtlı dev mağara salonunda iki küçük silüet."),
   tiktok="El baskısı yazma denedik, ikimizin de deseni kaydı 😂 #JozhStudios",
   ig=("Tokat'ta yazma ustası ahşap kalıpla kusursuz desenler bastı. Biz denedik: Ali'ninki kaydı, Mert'inki daha çok kaydı. 😂\n\n"
       "Ustanın 100 yazmasını aldık, Tokat kebabı yedik, Ballıca Mağarası'nda her katmanın bir mevsim olduğunu konuştuk.\n\n"
       "Ali'nin yeni fikri: Final Kutusu. Kasa: {KASA}"),
   tags=["#Tokat", "#Yazma", "#BallıcaMağarası"],
   son="Ali'nin yeni fikri: yedi bölgeden bir şey içeren 'Final Kutusu'.",
   teaser="Kayan desenler, bir kebap orkestrası ve son kutunun fikri. Bölüm 72: Tokat. Pek yakında.")

# ======================================================================= 73 AMASYA
EP(73, "Amasya", "Kayadaki Krallar",
   "Yalıboyu evleri, Kral Kaya Mezarları, Ferhat ile Şirin ve misket elması.",
   "Amasya'da sabah Yeşilırmak kıyısındaki Yalıboyu evlerinin önünde yürürler; nehrin karşısında kayalara oyulmuş Pontus kral mezarları "
   "yükselir. Yazmaların yarısı, pestil ve bal Amasya'da satılır. Ferhat ile Şirin efsanesinin anlatıldığı yerde Mert, 'dağı delmek' ile "
   "borcu ödemek arasında bir benzerlik kurar. Bir bahçede misket elmasının hasadını görürler. Akşam Ali'nin telefonuna Hasan'dan bir mesaj "
   "gelir: seranın ilk yapılandırılmış taksitini ödemiştir.",
   {"yaliboyu": ("Yalıboyu evleri", "the Yalıboyu Ottoman wooden houses lined up along the Yeşilırmak river in Amasya, with the rock-cut tombs of "
                 "the Pontic kings carved high in the cliff behind them, autumn light"),
    "carsi": ("Amasya çarşısı", "a shopping street in Amasya with small shops, a scarf shop, a nut shop and a gift shop"),
    "ferhat": ("Ferhat su kanalı", "a rocky hillside near Amasya with an old water channel carved into the rock, linked to the Ferhat and Şirin "
               "legend, a view of the valley"),
    "bahce": ("Misket elması bahçesi", "an apple orchard near Amasya in late autumn: small striped red-yellow misket apples on bare-leaved trees, "
              "wooden crates, mountains"),
    "kopru": ("Nehir kıyısı", "the Yeşilırmak riverside promenade in Amasya at night: the lit rock tombs on the cliff, wooden houses reflected "
              "in the river")},
   [
       S("09:00 sabah", "yaliboyu", ["mert", "ali"], "Krallar Kayada",
         "Yeşilırmak kıyısında Yalıboyu evlerinin önündedirler. Nehrin karşısında kayalara oyulmuş kral mezarları.",
         "Mert and Ali walk along the riverside in front of the old wooden houses; Ali stops and points up at the rock-cut tombs high in the cliff; "
         "Mert tilts his head back so far he almost loses balance.",
         [("ali", "Pontus kralları mezarlarını kayaya oydurmuş.", "fascinated"),
          ("mert", "Biz borcu bitirince kayaya ne yazdırırız acaba?", "joking")],
         "slow crane-up from the river to the cliff tombs", h="serin"),
       S("11:00 iç-gündüz", "carsi", ["mert", "ali", "esnaf"], "Amasya'da Satış",
         "Amasya çarşısında bir dükkân 50 yazmayı, 40 kilo pestili ve 10 kilo balı alır.",
         "The shop owner drapes a printed scarf over her arm, then tastes a piece of pestil and a spoon of honey; she nods to each and counts money "
         "into Ali's hand while Mert stacks items on her counter.",
         [("esnaf", "Yazma, pestil, bal... Hepsini alırım. Kış geliyor.", "pleased"),
          ("ali", "Hepsi el emeği. Hayırlı satışlar.", "warm")],
         "static medium three-shot at the counter",
         t=[U(50, "yazma", 450, "satis", "Tokat yazması, Amasya'da ({adet} x {fiyat} TL)"),
            U(40, "kg", 600, "satis", "Gümüşhane pestili ve kömesi, Amasya'da (40 kg x 600 TL)"),
            U(10, "kg", 1600, "satis", "Macahel Kafkas arısı balı, Amasya'da (10 kg x 1.600 TL)")]),
       S("13:00 öğle", "ferhat", ["mert", "ali"], "Dağı Delmek",
         "Ferhat ile Şirin efsanesinin anlatıldığı kaya kanalının yanında dururlar. Mert dağı delmekle borcu ödemek arasında benzerlik kurar.",
         "Mert places his hand on the carved rock channel and looks along it toward the valley; Ali sits on a rock beside him with the notebook on "
         "his knees.",
         [("mert", "Ferhat dağı delmiş, biz seksen bir ili deliyoruz.", "dramatic"),
          ("ali", "Şirin de sekiz yüz bin lira mı istemişti?", "laughing")],
         "slow push-in along the rock channel", h="serin",
         t=T("yemek", 900, "Öğle yemeği")),
       S("15:30 ikindi", "bahce", ["mert", "ali", "bahcivan"], "Misket Elması",
         "Bir bahçede küçük, çizgili misket elmasının hasadını görürler. Bahçıvan bir sepet ikram eder.",
         "The farmer twists a small striped red-yellow apple off a nearly bare branch and hands it to Mert; Mert bites it with a loud crunch and "
         "grins; the farmer gives Ali a small basket of apples as a gift.",
         [("bahcivan", "Misket elması küçüktür ama kokusu bütün evi sarar.", "proud"),
          ("mert", "Kokusu kadar tadı da var amca!", "crunching, happy")],
         "static medium three-shot under the tree", h="serin"),
       S("20:00 akşam", "kopru", ["ali", "~hasan"], "Babadan Haber",
         "Akşam nehir kıyısında Ali'nin telefonuna babasından haber gelir: seranın yapılandırılmış ilk taksitini ödemiştir.",
         "Ali walks along the riverside with the phone to his ear, the lit tombs glowing on the cliff across the water; he stops and smiles widely. "
         "His lips stay closed while his father speaks.",
         [("hasan", "Oğlum, seranın ilk taksitini ödedim. Domatesler yine yetti.", "proud, from the phone speaker"),
          ("ali", "Baba, ikimizin de taksitleri yolunda.", "happy")],
         "slow tracking shot along the promenade"),
       S("21:30 akşam", "kopru", ["mert", "ali"], "Yarın Çorum",
         "Mert ve Ali nehrin karşısındaki ışıklı kral mezarlarına bakarak yarını konuşur: Çorum'da altıncı taksit.",
         "Mert and Ali lean on the river railing side by side; Mert holds up six fingers; Ali adds his hand with one more finger and they both "
         "laugh.",
         [("mert", "Yarın altıncı taksit. Sonra bir tane kaldı.", "excited"),
          ("ali", "Yedi bölge, yedi taksit. Bitiyor Mert.", "emotional")],
         "slow dolly-out revealing the lit cliff and river",
         t=[T("konaklama", 1300, "Yalıboyu'nda konak pansiyon, 1 gece"), T("ulasim", 800, "Yakıt: Amasya-Çorum")]),
   ],
   misafir={"esnaf": ("DÜKKÂN SAHİBİ", "SHOP OWNER, a 56-year-old Turkish woman, sturdy, a white headscarf, a knitted cardigan", "adult female voice, pleased"),
            "bahcivan": ("BAHÇIVAN", "APPLE FARMER, a 63-year-old Turkish man, lean, a grey stubble, a flat cap, a thick vest", "elderly male voice, proud")},
   ay=AY, hava="serin", kiyafet=K, urun="Amasya misket elması, çörek; Kral Kaya Mezarları, Yalıboyu evleri, Ferhat ile Şirin",
   sponsor="Elma, yöresel ürün ya da kültür turizmi alanında",
   kapak=("yaliboyu", ["mert", "ali"], "Mert and Ali stand by the river in front of old wooden houses, looking up at ancient royal tombs carved high "
          "in the cliff, autumn golden light", "Kayalara oyulmuş kral mezarlarına bakan Mert ve Ali."),
   yakinda=("kopru", ["mert", "ali"], "Two silhouettes on a riverside railing at night facing illuminated rock-cut tombs on a cliff reflected in "
            "the dark river", "Gece nehirde yansıyan ışıklı kaya mezarlarına bakan iki silüet."),
   tiktok="Krallar mezarlarını kayaya oymuş, biz 81 ili deliyoruz 🪨 #JozhStudios",
   ig=("Amasya'da Yeşilırmak'ın kıyısında, kayalara oyulmuş kral mezarlarının altındaydık. 👑\n\n"
       "Yazma, pestil ve balın bir kısmı Amasya'da satıldı. Ferhat dağı delmiş; biz seksen bir ili deliyoruz. 😄 Misket elmasının kokusu bütün kamyoneti sardı. 🍎\n\n"
       "Ve Hasan Amca seranın ilk taksitini ödedi! Yarın Çorum. Kasa: {KASA}"),
   tags=["#Amasya", "#KralKayaMezarları", "#MisketElması"],
   son="Yarın Çorum'da altıncı taksit. Sonra bir tane kalacak.",
   teaser="Kayadaki krallar, Ferhat'ın kanalı ve bir babadan iyi haber. Bölüm 73: Amasya. Pek yakında.")

# ======================================================================= 74 ÇORUM
EP(74, "Çorum", "Leblebi ve Hattuşa",
   "Sezon finali: leblebi kavurucusu, Hattuşa'nın aslanlı kapısı, altıncı taksit ve Cemil Bey'in telefonu.",
   "Çorum'da sabah bir leblebi kavurucusunda nohudun günlerce dinlendirilip kavrularak leblebiye dönüştüğünü öğrenir, Final Kutusu için "
   "150 kilo leblebi alırlar. Kalan yazmalar satılır. Boğazkale'de Hititlerin başkenti Hattuşa'nın Aslanlı Kapı'sında dururlar: dünyanın "
   "bilinen ilk yazılı barış antlaşmalarından birini yapanların şehri. Altıncı taksiti burada gönderirler: 150.000 TL. Akşam Cemil Bey ilk "
   "kez kendisi arar: 'Yılbaşı gecesi Ankara'da görüşelim.'",
   {"leblebi": ("Leblebi kavurucusu", "a traditional leblebi roastery in Çorum: big rotating roasting drums, sacks of chickpeas, trays of pale "
                "yellow roasted chickpeas, warm air"),
    "carsi": ("Çorum çarşısı", "a shopping street in Çorum with shops of leblebi, nuts and textiles"),
    "hattusa": ("Hattuşa, Aslanlı Kapı", "the Lion Gate of Hattusa at Boğazkale: two ancient carved stone lions on either side of a massive "
                "stone gateway on a hillside, cold steppe, cloudy sky, the ruins of the Hittite capital around"),
    "otel": ("Otel odası", "a hotel room in Çorum at night: sacks of leblebi, the brown notebook on a table, two beds")},
   [
       S("09:00 iç-gündüz", "leblebi", ["mert", "ali", "leblebici"], "Nohuttan Leblebiye",
         "Leblebi kavurucusu Hamdi Usta nohudun günlerce dinlendirilip birkaç kez kavrulduğunu anlatır.",
         "Hamdi opens the hatch of a rotating roasting drum and pale yellow roasted chickpeas pour into a tray in a warm cloud; Mert takes a "
         "handful and blows on them; Ali leans in to smell.",
         [("leblebici", "Nohut dinlenir, kavrulur, yine dinlenir. Leblebi sabır ister.", "master"),
          ("mert", "Usta, bu yolculukta sabırsız tek şey benmişim.", "laughing")],
         "slow push-in on the pouring chickpeas"),
       S("10:00 iç-gündüz", "leblebi", ["ali", "leblebici"], "Yüz Elli Kilo",
         "Final Kutusu için 150 kilo sarı leblebi alırlar.",
         "Hamdi fills sacks with roasted chickpeas and weighs them; Ali counts money into his hand and ties the last sack.",
         [("leblebici", "Kilosu yüz seksen. Kutunuzda Çorum'u temsil etsin.", "proud"),
          ("ali", "Yüz elli kilo. Final Kutusu'nun ilk malı.", "proud")],
         "static medium two-shot at the scale",
         t=U(150, "kg", 180, "alis", "Çorum leblebisi ({adet} kg x {fiyat} TL)")),
       S("11:30 sabah", "carsi", ["mert", "esnaf"], "Son Yazmalar",
         "Bir tekstil dükkânı kalan 50 Tokat yazmasını alır.",
         "The textile shop owner unfolds a printed scarf and holds it to the light, nods and counts money into Mert's hand; Mert hands her the "
         "stack.",
         [("esnaf", "Tokat yazması Çorum'da da sevilir. Elli tane.", "pleased"),
          ("mert", "Dört yüz elliden. Karadeniz bitti, yazmalar da bitti!", "cheerful")],
         "static medium two-shot at the counter",
         t=[U(50, "yazma", 450, "satis", "Tokat yazması, Çorum'da ({adet} x {fiyat} TL)"), T("yemek", 800, "Öğle yemeği: Çorum mantısı")]),
       S("15:00 ikindi", "hattusa", ["mert", "ali"], "Aslanlı Kapı",
         "Hattuşa'nın Aslanlı Kapı'sındadırlar. Ali, Hititlerin bilinen ilk yazılı barış antlaşmalarından birini yaptığını anlatır.",
         "Mert and Ali stand between the two ancient stone lions of the massive gateway in the cold wind; Ali touches the weathered lion's mane; "
         "Mert looks out over the ruins of the capital.",
         [("ali", "Burada bir zamanlar kâğıda yazılmış bir barış imzalanmış. Kil tablete.", "awed"),
          ("mert", "Kâğıtla! Hititler de kural ikiyi biliyormuş.", "delighted")],
         "slow crane-up through the gate revealing the ruins", h="rüzgar"),
       S("16:00 ikindi", "hattusa", ["mert", "ali"], "Altıncı Taksit",
         "Aslanlı Kapı'nın önünde altıncı taksiti gönderirler: 150.000 TL. Ödenen 650.000, kalan 150.000.",
         "Ali holds out the phone; this time Mert and Ali place their thumbs on the screen together and press send; they exhale and lean against "
         "the stone lion.",
         [("ali", "Altı yüz elli bin ödendi. Kalan yüz elli.", "emotional"),
          ("mert", "Son taksit Ankara'da. Bir bölge kaldı Ali!", "triumphant")],
         "slow push-in on their hands on the phone",
         t=T("borc", 150000, "6. taksit: Cemil Bey (Karadeniz sezonu sonu)")),
       S("21:30 iç-gece", "otel", ["mert", "ali", "~cemil"], "Ankara'da Görüşelim",
         "Gece Cemil Bey ilk kez kendisi arar. Sesi her zamankinden yumuşaktır.",
         "Ali's phone rings on the table; both see the caller and freeze; Ali puts it on speaker; they lean in over the brown notebook, listening "
         "with closed mouths; at the end Mert slowly sits back, stunned.",
         [("cemil", "Yılbaşı gecesi Ankara'da görüşelim. Son taksiti elden alacağım.", "slow, softer than ever, from the phone speaker"),
          ("mert", "Cemil Abi ilk kez kendisi aradı Ali.", "stunned whisper")],
         "slow push-in on the phone between them",
         t=[T("konaklama", 1200, "Otel, 1 gece"), T("ulasim", 800, "Yakıt: Çorum-Çankırı")],
         kurgu="Sezon sonu kartı (kurguda): SEZON 6 BİTTİ · 18 İL · 6. TAKSİT ÖDENDİ · KALAN 150.000 TL"),
   ],
   misafir={"leblebici": ("HAMDİ USTA", "HAMDİ, a 64-year-old Turkish leblebi roaster, stout, a white mustache, a flat cap, a dusty work apron",
                          "elderly male voice, master, Çorum Turkish"),
            "esnaf": ("DÜKKÂN SAHİBİ", "SHOP OWNER, a 47-year-old Turkish woman, short black hair, a grey coat", "adult female voice, pleased")},
   ay=AY, hava="bulutlu", kiyafet=K, urun="Çorum leblebisi, Çorum mantısı; Hattuşa (UNESCO), Alacahöyük",
   sponsor="Leblebi ya da Hitit kültür turizmi alanında",
   kapak=("hattusa", ["mert", "ali"], "Mert and Ali stand between the two ancient carved stone lions of the massive Lion Gate of Hattusa, pressing "
          "a phone together, cold wind and dramatic clouds", "Hattuşa'nın Aslanlı Kapı'sında birlikte telefona basan Mert ve Ali."),
   yakinda=("otel", ["mert", "ali"], "Two faces leaning toward a phone glowing on a dark table beside a worn brown notebook, both frozen in "
            "surprise", "Karanlık masada parlayan telefona eğilmiş, donup kalmış iki yüz."),
   tiktok="Sezon 6 finali: Hattuşa'da 150.000 TL taksit 🦁 #JozhStudios",
   ig=("Karadeniz bitti! 18 il, ilk kar, bir zincir ve kâğıtla imzalanan 300 kutu. 🌲\n\n"
       "Çorum'da Hamdi Usta'nın leblebisinden Final Kutusu için 150 kilo aldık. Hattuşa'nın Aslanlı Kapı'sında altıncı taksiti gönderdik: 150.000 TL. Ödenen: 650.000 TL! 🦁\n\n"
       "Ve Cemil Abi ilk kez kendisi aradı: 'Yılbaşı gecesi Ankara'da görüşelim.' Kasa: {KASA}. Son sezon: İç Anadolu!"),
   tags=["#Çorum", "#Hattuşa", "#SezonFinali"],
   son="Cemil Bey: 'Yılbaşı gecesi Ankara'da görüşelim.' Son sezon başlıyor.",
   teaser="Sabırla kavrulan leblebi, taş aslanlar ve Cemil Bey'in telefonu. Bölüm 74: Çorum, sezon finali. Pek yakında.")
