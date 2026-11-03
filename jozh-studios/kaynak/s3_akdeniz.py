# -*- coding: utf-8 -*-
"""Sezon 3 · Eve Dönüş Yolu · Akdeniz (Bölüm 30-37). Ağustos, nemli sıcak.
Rota: Hatay → Osmaniye → Kahramanmaraş → Adana → Mersin → Antalya → Isparta → Burdur
Antalya'da Hasan eski beyaz kamyonetini verir; Bölüm 36'dan itibaren ulaşım = yakıt."""
from ortak import EP, S, T, U

AY = "Ağustos"
KAMYONET = ("an old white single-cab pickup truck from the early 2000s with a faded blue side stripe, a slightly dented tailgate, no brand "
            "logos and no lettering")

# ======================================================================= 30 HATAY
EP(30, "Hatay", "Yeniden Açılan Dükkânlar",
   "Depremden sonra ayağa kalkan Antakya'da künefe, defne sabunu ve dayanışma.",
   "Antakya'da 2023 depreminden sonra yeniden açılan dükkânların arasında yürürler. Mert zeytinyağını Hatay'da satmaya kalkınca Ali onu "
   "durdurur: Hatay'ın zeytinyağı zaten meşhurdur. Yeni açılmış bir künefe dükkânı Antep fıstığının yarısını alır; usta Mert'e künefe "
   "çevirmeyi öğretir. Hatay Arkeoloji Müzesi'nin mozaiklerini görürler. Harbiye'de defne sabunu yapan bir aile atölyesinden 200 kalıp alırlar. "
   "Gece bir esnaf onlara Hatay'ın dayanışmasını anlatır: 'Burada kimse kimseyi yarı yolda bırakmadı.'",
   {"carsi": ("Antakya, yeniden açılan çarşı", "a street in Antakya's bazaar area being rebuilt after the earthquake: some newly reopened "
              "small shops with fresh paint and bright awnings, scaffolding on a building behind, a few people working"),
    "kunefe": ("Künefe dükkânı", "a newly reopened künefe shop in Antakya: a round copper pan over a charcoal brazier, golden shredded pastry "
               "with melted cheese, a bowl of green pistachios, white tiles"),
    "muze": ("Hatay Arkeoloji Müzesi", "a large modern museum hall in Hatay with enormous colorful Roman floor mosaics displayed under soft "
             "spotlights, wooden walkways"),
    "sabun": ("Defne sabunu atölyesi", "a family laurel soap workshop in Harbiye: stacks of green laurel-oil soap bars drying in towers, "
              "laurel branches, a large cauldron, a window to green hills"),
    "avlu": ("Esnaf avlusu", "a small stone courtyard in Antakya at night: a lemon tree, plastic chairs, a tea kettle on a small stove, "
             "string lights")},
   [
       S("08:30 sabah", "carsi", ["mert", "ali"], "Yeniden",
         "Antakya'da yeniden açılan dükkânların arasında yürürler. İskelelerin önünde taze boyalı tabelasız kepenkler.",
         "Mert and Ali walk slowly down the street past freshly painted reopened shops and scaffolding; a shopkeeper raises his shutter and "
         "waves at them; Mert waves back and stops, looking around quietly.",
         [("ali", "Her açılan kepenk bir umut.", "quiet, moved"),
          ("mert", "Biz de buradan alışveriş yapacağız Ali. Burada bırakacağız paramızı.", "determined")],
         "slow tracking shot alongside them", h="nemli"),
       S("09:30 sabah", "carsi", ["mert", "ali"], "Hatay'a Zeytinyağı",
         "Mert zeytinyağı tenekesini açıp satmaya kalkar. Ali gülerek durdurur: Hatay'ın zeytinyağı zaten meşhurdur.",
         "Mert lifts a tin of olive oil onto a shop counter with a big smile; Ali gently takes the tin back down with both hands and shakes his "
         "head, trying not to laugh.",
         [("ali", "Mert. Hatay. Zeytinyağı. Kars'ı hatırla.", "laughing, patient"),
          ("mert", "Haklısın. Kaşar travması.", "embarrassed")],
         "static medium two-shot at the shop counter", h="nemli"),
       S("11:30 iç-gündüz", "kunefe", ["mert", "kunefeci"], "Künefe Çevirmek",
         "Yeni açılan künefe dükkânı Antep fıstığının yarısını alır. Usta, Mert'e künefe çevirmeyi öğretir.",
         "The künefe master guides Mert's hands as he flips the copper pan; the golden künefe lands perfectly, Mert shouts with joy; the master "
         "sprinkles green pistachio over it and pats Mert's back.",
         [("kunefeci", "Yirmi beş kilo fıstık alıyorum. Ama önce bir künefe çevir!", "jovial"),
          ("mert", "Çevirdim usta! Bak, düşmedi!", "triumphant")],
         "slow push-in on the copper pan and their hands",
         t=U(25, "kg", 1200, "satis", "Belgeli Antep fıstığı, künefe dükkânına ({adet} kg x {fiyat} TL)")),
       S("14:00 iç-gündüz", "muze", ["mert", "ali"], "Mozaiklerin Şehri",
         "Hatay Arkeoloji Müzesi'nin dev mozaiklerinin üstündeki yürüme yolundadırlar.",
         "Mert and Ali walk along a wooden walkway above a vast colorful mosaic floor; Ali kneels to look closely at the tiny stone pieces; Mert "
         "gazes at the whole picture from above.",
         [("ali", "Her biri küçücük bir taş. Ama birlikte bir dünya.", "thoughtful"),
          ("mert", "Bizim seksen bir il gibi.", "smiling")],
         "slow crane-up revealing the full mosaic",
         t=T("yemek", 900, "Öğle yemeği ve künefe")),
       S("17:00 ikindi", "sabun", ["mert", "ali", "sabuncu"], "Defne Sabunu",
         "Harbiye'de defne sabunu yapan bir aile atölyesinden 200 kalıp alırlar.",
         "The soap maker holds a green laurel soap bar under Ali's nose; Ali breathes in and smiles; Mert loads stacked bars into a cardboard box "
         "while the soap maker counts money.",
         [("sabuncu", "Defne yağı ve zeytinyağı. Kalıbı yetmiş.", "proud"),
          ("ali", "İki yüz kalıp alıyoruz. Sizden almak istedik.", "sincere")],
         "static medium three-shot among the soap towers", h="nemli",
         t=U(200, "kalıp", 70, "alis", "Hatay defne sabunu ({adet} kalıp x {fiyat} TL)")),
       S("21:30 gece", "avlu", ["mert", "ali", "esnaf"], "Yarı Yolda Bırakmamak",
         "Gece bir avluda çay içerken yaşlı bir esnaf Hatay'ın dayanışmasını anlatır.",
         "The old shopkeeper pours tea into three glasses under the lemon tree; Mert and Ali sit close, listening; the old man places his hand "
         "over his heart while speaking.",
         [("esnaf", "Burada kimse kimseyi yarı yolda bırakmadı evlat.", "slow, heartfelt"),
          ("mert", "Biz de bırakmayacağız. Ne birbirimizi ne de sözümüzü.", "moved")],
         "slow push-in under the string lights",
         t=[T("konaklama", 1200, "Pansiyon, 1 gece"), U(2, "bilet", 200, "ulasim", "Hatay-Osmaniye otobüsü ({adet} x {fiyat} TL)")]),
   ],
   misafir={"kunefeci": ("KÜNEFE USTASI", "KÜNEFE MASTER, a 49-year-old Turkish man, stocky, a round cheerful face, a black mustache, a white "
                         "cap and apron", "adult male voice, jovial, Hatay Turkish"),
            "sabuncu": ("SABUN USTASI", "SOAP MAKER, a 44-year-old Turkish woman, slim, curly dark hair tied back, a green work apron",
                        "adult female voice, proud"),
            "esnaf": ("YAŞLI ESNAF", "OLD SHOPKEEPER, a 76-year-old Turkish man, thin, a white mustache, a grey cardigan, a cane leaning on "
                      "his chair", "elderly male voice, slow, heartfelt Hatay Turkish")},
   ay=AY, hava="nemli", urun="Künefe, defne sabunu, zeytinyağı, kömbe; Hatay Arkeoloji Müzesi, Uzun Çarşı",
   sponsor="Künefe, defne sabunu ya da yeniden açılan yerel esnaf olarak",
   kapak=("kunefe", ["mert", "kunefeci"], "Mert flips a golden künefe in a copper pan with the master guiding his hands, pistachio flying, both "
          "laughing, warm charcoal glow", "Ustayla birlikte künefe çeviren Mert."),
   yakinda=("carsi", ["mert", "ali"], "Two silhouettes walking down a street at dawn toward a single shop whose shutter is being raised, warm "
            "light spilling out, scaffolding in shadow", "Şafakta kepengi açılan tek bir dükkâna yürüyen iki silüet."),
   tiktok="Antakya'da künefe çevirdim 🧀 ve kimse kimseyi yarı yolda bırakmadı #JozhStudios",
   ig=("Antakya ayağa kalkıyor. Yeni açılan dükkânlardan alışveriş yaptık. ❤️\n\n"
       "Mert zeytinyağını Hatay'da satmaya kalktı (evet, yine 😂), künefe ustası ona künefe çevirmeyi öğretti, Harbiye'den defne sabunu aldık.\n\n"
       "'Burada kimse kimseyi yarı yolda bırakmadı.' Kasa: {KASA}"),
   tags=["#Hatay", "#Antakya", "#Künefe"],
   son="Yaşlı esnafın sözü: 'Burada kimse kimseyi yarı yolda bırakmadı.'",
   teaser="Yeniden açılan kepenkler, bir künefe ve dayanışma. Bölüm 30: Hatay. Pek yakında.")

# ======================================================================= 31 OSMANİYE
EP(31, "Osmaniye", "Yer Fıstığı Hasadı",
   "Karatepe'nin aslanları, yer fıstığı tarlası ve ilk zeytinyağı satışı.",
   "Osmaniye'de sabah Karatepe-Aslantaş Açık Hava Müzesi'nde iki dilli yazıtların ve taş aslanların önündedirler. Zeytinyağının bir kısmını "
   "bir lokantacıya, defne sabununun bir kısmını bir eczaneye satarlar. Öğleden sonra yer fıstığı tarlasında söküm yapan bir aileye yardım "
   "eder, 150 kilo kabuklu yer fıstığı alırlar. Akşam Ali, Antalya'ya varmadan babası için bir plan yapmak ister. Mert'in aklında bir fikir "
   "vardır ama bu kez önce Ali'ye sorar.",
   {"karatepe": ("Karatepe-Aslantaş", "the Karatepe-Aslantaş open-air museum: ancient carved stone lion statues and relief slabs with "
                 "inscriptions among pine trees on a hill above a reservoir"),
    "lokanta": ("Osmaniye lokantası", "a simple restaurant kitchen in Osmaniye: steel pots, a big window, stacked plates"),
    "eczane": ("Eczane", "a small pharmacy in Osmaniye with white shelves of products, a counter and a natural-products corner"),
    "tarla": ("Yer fıstığı tarlası", "a peanut field near Osmaniye at afternoon: freshly pulled peanut plants with clusters of pods drying on "
              "the soil, a tractor, cotton fields beyond"),
    "otel": ("Otel balkonu", "a hotel balcony in Osmaniye at night: two plastic chairs, a small table, distant mountain silhouettes")},
   [
       S("08:30 sabah", "karatepe", ["mert", "ali"], "Aslanlar",
         "Karatepe'de taş aslanların ve iki dilli yazıtın önündedirler. Ali, aynı metnin iki dilde yazıldığını anlatır.",
         "Mert crouches eye to eye with an ancient stone lion statue and mimics its open-mouthed roar; Ali stands by a carved relief slab tracing "
         "the lines of inscription in the air with one finger.",
         [("ali", "Aynı metni iki dilde yazmışlar. Herkes anlasın diye.", "fascinated"),
          ("mert", "Biz de etiketleri iki dilde yazalım, gurbetçiler için!", "inspired")],
         "slow dolly-in between the stone lions", h="nemli"),
       S("10:30 iç-gündüz", "lokanta", ["ali", "lokantaci"], "Zeytinyağı Bulduğu Yerde",
         "Bir lokantacı 30 litre Kilis zeytinyağı alır.",
         "The restaurant owner pours a little olive oil onto a piece of bread, tastes it and gives a thumbs-up; Ali sets three tins onto the "
         "kitchen counter.",
         [("lokantaci", "Kilis'in yağı mı? Otuz litre bırak.", "satisfied"),
          ("ali", "Litresi dört yüz yirmi. Afiyet olsun.", "polite")],
         "static medium two-shot in the kitchen",
         t=U(30, "litre", 420, "satis", "Kilis zeytinyağı, lokantaya ({adet} litre x {fiyat} TL)")),
       S("12:00 iç-gündüz", "eczane", ["mert", "eczaci"], "Eczanede Defne",
         "Bir eczacı doğal ürün rafı için 100 kalıp defne sabunu alır.",
         "The pharmacist arranges laurel soap bars on a white shelf in a neat row; Mert hands her the box and leans on the counter with a charming "
         "smile while she pays.",
         [("eczaci", "Defne sabunu çok soruluyor. Yüz kalıp alırım.", "professional"),
          ("mert", "Kalıbı yüz yirmi. Hatay'dan, yeni açılan bir atölyeden.", "proud")],
         "static medium two-shot at the counter",
         t=U(100, "kalıp", 120, "satis", "Hatay defne sabunu, eczaneye ({adet} kalıp x {fiyat} TL)")),
       S("15:30 ikindi", "tarla", ["mert", "ali", "ciftci"], "Söküm",
         "Yer fıstığı tarlasında söküm yapan Emine Teyze'nin ailesine yardım ederler. Bitkiyi çekince altından fıstıklar çıkar.",
         "Mert grips a peanut plant with both hands and pulls it out of the soil; a cluster of pods comes up with it and he holds it up in "
         "surprise; Emine laughs and shakes the soil off another plant.",
         [("mert", "Fıstık ağaçta değil, toprağın altındaymış!", "astonished"),
          ("ciftci", "Osmaniye'nin fıstığı yerin altında büyür evlat.", "laughing")],
         "slow push-in at ground level", h="nemli"),
       S("17:30 ikindi", "tarla", ["ali", "ciftci"], "Yüz Elli Kilo",
         "Emine Teyze'den 150 kilo kurutulmuş kabuklu yer fıstığı alırlar.",
         "Emine ties the top of a full sack of dried peanuts and drags it to a scale; Ali counts money into her hand and she presses a small bag "
         "of roasted peanuts into his palm as a gift.",
         [("ciftci", "Kilosu yüz yirmi. Bu da yolda yiyin diye.", "motherly"),
          ("ali", "Teşekkürler teyze. Yüz elli kilo.", "warm")],
         "static medium two-shot at the scale", h="nemli",
         t=[U(150, "kg", 120, "alis", "Kabuklu Osmaniye yer fıstığı ({adet} kg x {fiyat} TL)"), T("yemek", 700, "Öğle ve akşam yemeği")]),
       S("22:00 gece", "otel", ["mert", "ali"], "Önce Sana Soruyorum",
         "Gece balkonda Mert'in bir fikri vardır ama bu kez önce Ali'ye sorar: Antalya'da babasının domatesini takipçilere satmak.",
         "Mert sits on the balcony chair, starts to speak excitedly, stops himself and raises his hand politely like a student; Ali laughs and "
         "nods for him to go on.",
         [("mert", "Bir fikrim var ama önce sana soruyorum: babanın domatesini takipçilere satsak?", "careful, hopeful"),
          ("ali", "İlk kez önce sordun. Anlat.", "touched, smiling")],
         "static medium two-shot on the balcony",
         t=[T("konaklama", 1100, "Otel, 1 gece"), U(2, "bilet", 250, "ulasim", "Osmaniye-Kahramanmaraş otobüsü ({adet} x {fiyat} TL)")]),
   ],
   misafir={"lokantaci": ("LOKANTACI", "RESTAURANT OWNER, a 50-year-old Turkish man, round, a grey mustache, an apron", "adult male voice"),
            "eczaci": ("ECZACI", "PHARMACIST, a 36-year-old Turkish woman, neat ponytail, a white coat, glasses", "adult female voice, professional"),
            "ciftci": ("EMİNE TEYZE", "EMİNE, a 63-year-old Turkish farm woman, sun-tanned, a white headscarf, a colorful loose shirt and baggy "
                       "trousers, soil on her hands", "elderly female voice, warm, Çukurova Turkish")},
   ay=AY, hava="nemli", urun="Osmaniye yer fıstığı; Karatepe-Aslantaş Açık Hava Müzesi",
   sponsor="Yer fıstığı ya da tarım ürünleri alanında",
   kapak=("tarla", ["mert", "ciftci"], "Mert holds up a freshly pulled peanut plant with dangling pods in astonishment while Emine laughs beside "
          "him in a sunny field", "Topraktan çektiği fıstıkları şaşkınlıkla gösteren Mert."),
   yakinda=("karatepe", ["mert"], "Mert crouches face to face with an ancient stone lion in dramatic low light among dark pines, the lion's "
            "open mouth in sharp shadow", "Karanlık çamların arasında taş bir aslanla yüz yüze Mert."),
   tiktok="Fıstığın toprağın altında büyüdüğünü bugün öğrendim 🥜 #JozhStudios",
   ig=("Karatepe'de iki dilli yazıtın önünde Mert'in aklına fikir geldi: etiketleri iki dilde yazalım! 🦁\n\n"
       "Emine Teyze'nin tarlasında yer fıstığı söktük. Evet, fıstık toprağın altında büyüyormuş. 😅🥜\n\n"
       "Gece Mert ilk kez fikrini söylemeden önce Ali'ye sordu. Kasa: {KASA}"),
   tags=["#Osmaniye", "#YerFıstığı", "#Karatepe"],
   son="Mert'in fikri: Ali'nin babasının domatesini takipçilere satmak.",
   teaser="Taş aslanlar, toprağın altındaki fıstık ve önce sorulan bir fikir. Bölüm 31: Osmaniye. Pek yakında.")

# ======================================================================= 32 KAHRAMANMARAŞ
EP(32, "Kahramanmaraş", "Dondurmanın Oyunu",
   "Dondurma ustasının şovu, Maraş biberi ve bakırcılar çarşısı.",
   "Kahramanmaraş'ta dövme dondurma ustası Mert'i külahla tam yedi kez kandırır; Ali gülmekten yere çöker. Usta, dondurmanın salep ve keçi "
   "sütünden olduğunu, dövülerek uzadığını anlatır. Yer fıstığının yarısı bir kuruyemişçiye satılır. Güneşte kuruyan kırmızı biber "
   "tarlasında Maraş biberinin nasıl öğütüldüğünü görür, 80 kilo pul biber alırlar. Akşam deprem sonrası yeniden kurulan çarşıda bir "
   "bakırcıdan tarhana çorbası için bakır tas hediye alırlar. Ali babasını arar; Mert'in domates fikrini anlatır.",
   {"dondurma": ("Dondurmacı", "a traditional ice cream shop in Kahramanmaraş: a big metal tub of stretchy white ice cream, a long iron "
                 "paddle, cones, a vendor in a traditional embroidered vest behind the counter"),
    "kuruyemis": ("Kuruyemişçi", "a nut shop in Kahramanmaraş with sacks of peanuts and chickpeas, a scale and a ceiling fan"),
    "biber": ("Biber tarlası ve değirmen", "a sunny yard near Kahramanmaraş with bright red peppers drying on large sheets, and a small "
              "stone mill grinding red pepper flakes into sacks"),
    "carsi": ("Bakırcılar çarşısı", "a rebuilt coppersmiths' row in Kahramanmaraş at dusk: new shop fronts with hanging copper bowls and "
              "trays glowing in warm light")},
   [
       S("10:00 sabah", "dondurma", ["mert", "dondurmaci"], "Yedi Kere",
         "Dondurma ustası külahı Mert'e uzatır, son anda geri çeker. Mert yedi kez kandırılır.",
         "The ice cream vendor holds out a cone on the long iron paddle; Mert reaches for it and it flips away upside down, again and again; Mert "
         "grabs the air, laughing in frustration.",
         [("dondurmaci", "Al bakalım! Hop! Gitti!", "playful showman"),
          ("mert", "Usta, bu yedinci! Bırak artık!", "laughing, frustrated")],
         "static medium two-shot across the counter", h="nemli"),
       S("10:10 sabah", "dondurma", ["mert", "ali", "dondurmaci"], "Salep ve Sabır",
         "Sonunda külah Mert'e verilir. Usta dondurmanın salep ve keçi sütünden yapıldığını, dövülerek uzadığını anlatır.",
         "The vendor finally places the cone into Mert's hand and pats his shoulder; he lifts a long rope of stretchy ice cream on the paddle to "
         "show it; Ali, still laughing on the floor, gets up and wipes his eyes.",
         [("dondurmaci", "Salep ve keçi sütü. Dövdükçe uzar, sabrettikçe tatlanır.", "proud"),
          ("ali", "Mert, sabır dersi seni her şehirde buluyor.", "laughing")],
         "slow push-in on the stretching ice cream",
         t=T("yemek", 400, "İki dövme dondurma")),
       S("12:00 öğle", "kuruyemis", ["ali", "kuruyemisci"], "Yarısı Gitti",
         "Bir kuruyemişçi 75 kilo yer fıstığını alır.",
         "The shopkeeper pours peanuts onto the scale and nods; Ali writes the line in the notebook and they shake hands under the turning fan.",
         [("kuruyemisci", "Osmaniye fıstığı kavrulunca kokusu çarşıyı sarar. Yetmiş beş kilo.", "pleased"),
          ("ali", "Kilosu iki yüz. Hayırlı olsun.", "polite")],
         "static medium two-shot at the scale",
         t=U(75, "kg", 200, "satis", "Osmaniye yer fıstığı, kuruyemişçiye ({adet} kg x {fiyat} TL)")),
       S("15:00 ikindi", "biber", ["mert", "ali", "biberci"], "Kırmızı Altın",
         "Güneşte kuruyan kırmızı biberlerin arasında Maraş biberinin taş değirmende öğütülmesini izlerler.",
         "The pepper maker pours dried red peppers into the stone mill and bright flakes stream into a sack; Mert sniffs too close and sneezes "
         "explosively; Ali laughs and fans the air with his notebook.",
         [("biberci", "Maraş biberi yağlıdır, rengi kırmızı kalır.", "knowledgeable"),
          ("mert", "Hapşu! Gözüm yanıyor ama alıyoruz!", "sneezing, laughing")],
         "slow tracking shot across the drying sheets to the mill", h="nemli"),
       S("16:00 ikindi", "biber", ["ali", "biberci"], "Seksen Kilo",
         "Seksen kilo Maraş pul biberi alırlar.",
         "The pepper maker ties four sacks of red flakes and stacks them; Ali counts money into his hand and they nod to each other.",
         [("biberci", "Kilosu iki yüz elli. Bunu kim yerse Maraş'ı hatırlar.", "proud"),
          ("ali", "Seksen kilo alıyoruz.", "decisive")],
         "static medium two-shot by the stacked sacks", h="nemli",
         t=U(80, "kg", 250, "alis", "Maraş pul biberi ({adet} kg x {fiyat} TL)")),
       S("19:30 akşam", "carsi", ["mert", "ali", "~hasan"], "Babana Anlat",
         "Yeniden kurulan bakırcılar çarşısında Ali babasını arar ve Mert'in domates fikrini anlatır. Hasan bir süre susar.",
         "Ali walks slowly along the glowing copper shops with the phone at his ear; Mert walks beside him holding a small copper bowl they "
         "bought; Ali stops and waits for an answer, his lips closed.",
         [("ali", "Baba, takipçilerimiz senin domatesini almak istiyor. Ne dersin?", "hopeful"),
          ("hasan", "Ben yıllarca hale sattım... İnsanlara doğrudan mı? Gelin konuşalım.", "surprised, from the phone speaker")],
         "slow tracking shot along the copper shops",
         t=[T("diger_gider", 600, "Hasan için hediye bakır tas"), T("konaklama", 1100, "Otel, 1 gece"),
            U(2, "bilet", 250, "ulasim", "Kahramanmaraş-Adana otobüsü ({adet} x {fiyat} TL)")]),
   ],
   misafir={"dondurmaci": ("DONDURMA USTASI", "ICE CREAM VENDOR, a 45-year-old Turkish man, a big mustache, a red fez-like cap and an embroidered "
                           "red-and-gold vest over a white shirt", "adult male voice, playful showman, Maraş Turkish"),
            "kuruyemisci": ("KURUYEMİŞÇİ", "SHOPKEEPER, a 54-year-old Turkish man, thin, a grey beard, glasses, a brown vest", "mature male voice"),
            "biberci": ("BİBERCİ", "PEPPER MAKER, a 50-year-old Turkish man, sturdy, red-stained hands, a cap, a dusty apron",
                        "adult male voice, knowledgeable, Maraş Turkish")},
   ay=AY, hava="nemli", urun="Maraş dondurması, Maraş biberi, tarhana, bakırcılık",
   sponsor="Dondurma, biber ya da bakır el sanatları alanında",
   kapak=("dondurma", ["mert", "dondurmaci"], "The ice cream vendor flips a cone upside down on a long iron paddle just out of Mert's reach, "
          "Mert lunging with a comic face, stretchy white ice cream in the air", "Külahı yakalamaya çalışan Mert ve oyuncu dondurma ustası."),
   yakinda=("biber", ["mert"], "A cloud of red pepper dust glowing in strong backlight around Mert's silhouette in front of a stone mill",
            "Ters ışıkta parlayan kırmızı biber tozu ve bir silüet."),
   tiktok="Dondurmacı beni 7 kez kandırdı 🍦😂 #JozhStudios",
   ig=("Kahramanmaraş'ta dondurma ustası beni tam 7 kez kandırdı. 🍦 Ali yerlerde. Usta: 'Sabrettikçe tatlanır.'\n\n"
       "Maraş biberinin taş değirmende öğütüldüğünü gördük (ve hapşırdık 🌶️), 80 kilo aldık.\n\n"
       "Ali babasına domates fikrini anlattı. Cevap: 'Gelin konuşalım.' Kasa: {KASA}"),
   tags=["#Kahramanmaraş", "#MaraşDondurması", "#MaraşBiberi"],
   son="Hasan, domates fikri için 'Gelin konuşalım' der.",
   teaser="Yedi kere kaçan bir külah, kırmızı bir toz bulutu ve bir babanın cevabı. Bölüm 32: Kahramanmaraş. Pek yakında.")

# ======================================================================= 33 ADANA
EP(33, "Adana", "Kebap ve Şalgam",
   "Taşköprü'de sabah, zırhla kıyma, şalgam ve Adana'nın sıcak gecesi.",
   "Adana'da sabah Seyhan Nehri üstündeki Roma döneminden kalma Taşköprü'den geçerler. Bir kebap ustası etin zırhla nasıl elde kıyıldığını "
   "gösterir ve Maraş biberinin yarısını alır. Öğlen şalgamla kebap yerler; Mert şalgamın acısıyla gözyaşı döker. Kalan yer fıstığı bir "
   "pazarcıya, zeytinyağının bir kısmı bir şarküteriye satılır. Gece Sabancı Merkez Camii'nin ışıkları nehre yansırken Ali takipçilerden "
   "gelen ilk domates ön siparişlerini sayar.",
   {"kopru": ("Taşköprü", "the ancient Roman stone bridge Taşköprü over the Seyhan river in Adana at morning: many stone arches, wide calm "
              "river, palm trees on the banks"),
    "kebapci": ("Kebapçı", "a traditional Adana kebab shop: a long charcoal grill with skewers of minced meat, a wooden board with a big "
                "curved zırh knife, plates of onions, sumac and parsley, white tiles"),
    "pazar": ("Adana pazarı", "a covered market in Adana: stalls of vegetables, nuts and spices, fans hanging from the ceiling"),
    "nehir": ("Seyhan kıyısı", "the Seyhan riverside in Adana at night: a promenade with palm trees and benches, a huge mosque with six "
              "illuminated minarets reflected in the river")},
   [
       S("08:30 sabah", "kopru", ["mert", "ali"], "Taşköprü",
         "Sabah Seyhan Nehri üstündeki Taşköprü'den yürüyerek geçerler. Sıcak şimdiden bastırmıştır.",
         "Mert and Ali walk across the old stone bridge carrying bags; Mert wipes sweat with the bottom of his t-shirt; Ali stops halfway and "
         "looks down the river at the arches.",
         [("ali", "Bu köprü yaklaşık iki bin yıldır kullanılıyor.", "impressed"),
          ("mert", "İki bin yıldır da bu kadar sıcak mı?", "melting")],
         "slow tracking shot along the bridge", h="nemli"),
       S("11:00 iç-gündüz", "kebapci", ["mert", "ali", "kebapci"], "Zırh",
         "Kebap ustası Memo Usta zırhla eti elde kıyar. Maraş biberini tadar ve 40 kilo alır.",
         "The kebab master rocks the big curved zırh knife over minced meat on the wooden board with a steady rhythm, then pinches red pepper "
         "flakes from Ali's sack, smells and nods; Mert tries to lift the heavy knife.",
         [("kebapci", "Adana kebabı zırhla kıyılır, makineyle olmaz. Biber de Maraş'ın olacak!", "proud"),
          ("ali", "Kırk kilo biber, kilosu dört yüz.", "businesslike")],
         "slow push-in on the zırh knife",
         t=U(40, "kg", 400, "satis", "Maraş pul biberi, kebapçıya ({adet} kg x {fiyat} TL)")),
       S("13:00 iç-gündüz", "kebapci", ["mert", "ali"], "Şalgamın Acısı",
         "Öğlen kebap ve acı şalgam. Mert bir yudum alır ve gözleri yaşarır.",
         "Mert takes a big gulp of deep purple şalgam juice, freezes, and his eyes water; he fans his mouth with his hand while Ali calmly sips "
         "his own glass and smiles.",
         [("mert", "Ali, bu şalgam değil, yangın!", "eyes watering"),
          ("ali", "Acılı istedin. Ben acısız aldım.", "innocent smile")],
         "static medium two-shot across the table",
         t=T("yemek", 900, "Adana kebabı ve şalgam")),
       S("16:00 ikindi", "pazar", ["mert", "pazarci"], "Pazar Satışı",
         "Pazarda kalan 75 kilo yer fıstığı bir pazarcıya satılır.",
         "The market trader pours peanuts from the sack into a large basket on his stall; Mert receives the money, holding a fan the trader "
         "lent him in the other hand.",
         [("pazarci", "Yetmiş beş kilo, iki yüzden. Kavurur satarım.", "fast"),
          ("mert", "Anlaştık abi. Vantilatörü de veriyor musun?", "joking")],
         "static medium two-shot at the stall", h="nemli",
         t=U(75, "kg", 200, "satis", "Osmaniye yer fıstığı, pazarcıya ({adet} kg x {fiyat} TL)")),
       S("18:00 ikindi", "pazar", ["ali", "sarkuteri"], "Zeytinyağı",
         "Pazarın kenarındaki bir şarküteri 30 litre zeytinyağı alır. Kalan 40 litre Antalya için ayrılır.",
         "The deli owner taps one of the oil tins and nods; Ali slides three tins onto her counter and keeps the rest on a hand trolley.",
         [("sarkuteri", "Kilis yağı aranır. Otuz litre bırakın.", "practical"),
          ("ali", "Kalan kırk litre Antalya'ya, babama.", "warm")],
         "static medium two-shot at the deli counter",
         t=U(30, "litre", 420, "satis", "Kilis zeytinyağı, şarküteriye ({adet} litre x {fiyat} TL)")),
       S("22:00 gece", "nehir", ["mert", "ali"], "Ön Sipariş",
         "Gece nehir kıyısında Ali takipçilerden gelen domates ön siparişlerini sayar: yüz yirmi aile.",
         "Mert and Ali sit on a riverside bench with the illuminated mosque reflected in the water; Ali scrolls on his phone, stops, and slowly "
         "shows Mert the number; Mert grabs Ali's shoulder and shakes him with joy.",
         [("ali", "Yüz yirmi aile babamın domatesini istiyor.", "overwhelmed"),
          ("mert", "Hasan Amca'nın serası kurtuluyor Ali!", "joyful")],
         "slow dolly-out revealing the river and the mosque",
         t=[T("konaklama", 1300, "Otel, 1 gece"), U(2, "bilet", 250, "ulasim", "Adana-Mersin otobüsü ({adet} x {fiyat} TL)")],
         kurgu="Domates ön siparişlerinin parası doğrudan Hasan'a gider; JOZH kasasına girmez."),
   ],
   misafir={"kebapci": ("MEMO USTA", "MEMO, a 56-year-old Turkish kebab master, big and strong, a thick black-grey mustache, a white chef "
                        "jacket with rolled sleeves, a towel on his shoulder", "mature male voice, proud, Adana Turkish"),
            "pazarci": ("PAZARCI", "MARKET TRADER, a 38-year-old Turkish man, lanky, a cap backwards, a sleeveless shirt", "adult male voice, fast"),
            "sarkuteri": ("ŞARKÜTERİCİ", "DELI OWNER, a 47-year-old Turkish woman, short blond-dyed hair, a white apron", "adult female voice")},
   ay=AY, hava="nemli", urun="Adana kebabı, şalgam, Çukurova pamuğu, Kozan portakalı (kışın); Taşköprü, Sabancı Merkez Camii",
   sponsor="Kebap, şalgam ya da Çukurova tarım ürünleri alanında",
   kapak=("kebapci", ["mert", "ali", "kebapci"], "Mert with tears in his eyes fanning his mouth after drinking purple şalgam while Ali sips calmly "
          "and the kebab master laughs behind skewers over glowing charcoal", "Şalgamın acısıyla ağlayan Mert, sakin Ali ve gülen usta."),
   yakinda=("nehir", ["mert", "ali"], "Two silhouettes on a riverside bench at night, a giant illuminated mosque reflected in the dark river, one "
            "of them holding up a glowing phone", "Gece nehir kıyısında bankta iki silüet ve parlayan bir telefon."),
   tiktok="Adana'da acılı şalgam içtim, hâlâ ağlıyorum 🥵 #JozhStudios",
   ig=("Taşköprü'den geçtik, Memo Usta'nın zırhla kıyma kıydığını izledik ve Maraş biberimizin yarısını kebapçı aldı. 🔪🌶️\n\n"
       "Şalgamı acılı istedim. Hata. 😭\n\nGece güzel bir haber: Ali'nin babasının domatesine 120 aile ön sipariş verdi! 🍅 (Bu para doğrudan Hasan Amca'ya gidiyor.) Kasa: {KASA}"),
   tags=["#Adana", "#AdanaKebabı", "#Şalgam"],
   son="Yüz yirmi aile Hasan'ın domatesini ön siparişle istiyor.",
   teaser="İki bin yıllık bir köprü, bir zırh, bir şalgam ve yüz yirmi aile. Bölüm 33: Adana. Pek yakında.")

# ======================================================================= 34 MERSİN
EP(34, "Mersin", "Kızkalesi'nde Cezerye",
   "Tantuni, cezerye, Kızkalesi ve Anamur'da muzun önünde hatırlanan kural.",
   "Mersin'de sabah Mert tantuni dürümünü üç ısırıkta bitirir. Kalan Maraş biberi bir tantunici zincirine değil, mahalle tantunicisine "
   "satılır. Bir cezerye atölyesinde havuçtan yapılan bu tatlının nasıl piştiğini öğrenir, 100 kilo alırlar. Kızkalesi'nde denizin "
   "ortasındaki kaleye bakıp ilk kez yüzerler. Anamur yolunda muz seralarını görünce Mert'in gözleri parlar, ama kendi kuralını hatırlar. "
   "Gece Antalya'ya giden otobüste Ali uyuyamaz: yarın eve dönüyordur.",
   {"tantuni": ("Tantunici", "a small tantuni shop in Mersin: a wide shallow pan with sizzling chopped meat, thin lavash wraps, tomatoes and "
                "parsley, a stainless counter"),
    "cezerye": ("Cezerye atölyesi", "a cezerye workshop in Mersin: a big copper cauldron of thick orange carrot paste being stirred, trays "
                "of cezerye bars rolled in coconut and walnuts, white tiles"),
    "kizkalesi": ("Kızkalesi sahili", "the beach at Kızkalesi in Mersin: golden sand, turquoise sea, and the medieval stone Maiden's Castle "
                  "on a tiny island a short distance offshore"),
    "muz": ("Anamur yolu, muz seraları", "a coastal road near Anamur at sunset: rows of banana greenhouses and banana plants with green "
            "bunches, a small roadside stall, the sea beyond"),
    "otobus": ("Gece otobüsü", "the dim interior of an intercity night bus on the coastal road: reading lights off, sleeping passengers far "
               "behind, moonlight on the sea through the window")},
   [
       S("09:00 sabah", "tantuni", ["mert", "ali", "tantunici"], "Üç Isırık",
         "Mert tantuni dürümünü üç ısırıkta bitirir. Usta Maraş biberini tadar ve 40 kiloyu alır.",
         "The tantuni master wraps sizzling meat in thin lavash and hands it to Mert, who finishes it in three huge bites; the master pinches "
         "red pepper flakes from Ali's sack, tastes and nods.",
         [("tantunici", "Benim tantuniye Maraş biberi yakışır. Kalan kırk kilo benim.", "pleased"),
          ("mert", "Usta, bir tane daha. Pazarlık değil, açlık.", "mouth full")],
         "static medium three-shot over the sizzling pan",
         t=[U(40, "kg", 400, "satis", "Maraş pul biberi, tantuniciye ({adet} kg x {fiyat} TL)"), T("yemek", 600, "Tantuni (4 dürüm)")]),
       S("11:30 iç-gündüz", "cezerye", ["mert", "ali", "cezeryeci"], "Havuçtan Tatlı",
         "Cezerye ustası havucun saatlerce kaynayıp ceviz ve hindistan cevizine bulandığını gösterir.",
         "The cezerye maker stirs the thick orange paste in the copper cauldron with a long wooden paddle; Mert takes the paddle and tries to stir, "
         "struggling; Ali tastes a cezerye bar rolled in coconut.",
         [("cezeryeci", "Havuç saatlerce kaynar. Kıvamını kolun bilir.", "proud"),
          ("mert", "Kolum bilmiyor usta, kolum bitti!", "straining, laughing")],
         "slow push-in on the copper cauldron"),
       S("12:30 iç-gündüz", "cezerye", ["ali", "cezeryeci"], "Yüz Kilo Cezerye",
         "Yüz kilo cezerye alırlar. Cezerye aylarca bozulmaz; kural tamam.",
         "The cezerye maker stacks wrapped boxes on the counter; Ali checks the date on a box, nods and counts money; Mert raises a finger behind "
         "him, mouthing the rule.",
         [("cezeryeci", "Kilosu iki yüz altmış. Aylarca dayanır.", "confident"),
          ("ali", "Yüz kilo alıyoruz. Kural bir de tamam.", "smiling")],
         "static medium two-shot at the counter",
         t=U(100, "kg", 260, "alis", "Mersin cezeryesi ({adet} kg x {fiyat} TL)")),
       S("15:00 ikindi", "kizkalesi", ["mert", "ali"], "İlk Deniz",
         "Kızkalesi'nde yolculuğun ilk denizine girerler. Kale denizin ortasında durur.",
         "Mert runs across the sand and dives into the turquoise water; Ali follows more carefully, then floats on his back looking at the stone "
         "castle on the island, both laughing.",
         [("mert", "Ali! Seksen bir ilin ilk denizi!", "shouting, joyful"),
          ("ali", "Kale bile denize girmiş, bize ne oluyor!", "laughing")],
         "smooth tracking shot from the shore into the water", h="nemli"),
       S("19:00 gün batımı", "muz", ["mert", "ali"], "Kuralı Hatırla",
         "Anamur yolunda muz seralarının yanında mola verirler. Mert'in gözleri parlar, sonra kendi kuralını hatırlar.",
         "Mert stops at a roadside stall and holds up a heavy bunch of green bananas with shining eyes; he slowly lowers it, puts it back and raises "
         "one finger toward Ali, who claps.",
         [("mert", "Muz... Hayır. Kural bir: iki günde bozulan mal yok.", "struggling, proud"),
          ("ali", "Mert büyüyor, kayıtlara geçsin!", "clapping")],
         "static medium two-shot at the stall, sunset sea behind",
         t=[T("yemek", 300, "Yol molası: iki muz ve ayran"), U(2, "bilet", 450, "ulasim", "Mersin-Antalya otobüsü ({adet} x {fiyat} TL)")]),
       S("23:30 iç-gece", "otobus", ["mert", "ali"], "Yarın Ev",
         "Gece otobüsünde Mert uyur; Ali camdan denizi izler. Yarın eve dönüyordur.",
         "Mert sleeps with his head against the bus window; Ali sits awake beside him, looking at the moonlit sea, holding his phone with a photo "
         "of a greenhouse on the screen.",
         [("ali", "Yarın ev. Babam, sera, annemin bahçesi...", "whispering to himself, emotional")],
         "slow push-in to Ali's face lit by moonlight"),
   ],
   misafir={"tantunici": ("TANTUNİCİ", "TANTUNI MASTER, a 42-year-old Turkish man, slim, a quick smile, a black cap and a white apron",
                          "adult male voice, pleased, Mersin Turkish"),
            "cezeryeci": ("CEZERYE USTASI", "CEZERYE MAKER, a 60-year-old Turkish man, round, a white mustache, white work clothes",
                          "elderly male voice, proud")},
   ay=AY, hava="nemli", urun="Tantuni, cezerye, Anamur muzu, narenciye; Kızkalesi",
   sponsor="Cezerye, tantuni ya da narenciye alanında",
   kapak=("kizkalesi", ["mert", "ali"], "Mert dives into turquoise water and Ali floats laughing, the stone Maiden's Castle rising from the sea "
          "behind them in bright sun", "Turkuaz denize atlayan Mert, arkada denizdeki Kızkalesi."),
   yakinda=("otobus", ["ali"], "Ali's face lit by moonlight through a night bus window, the dark sea glittering outside, a sleeping figure "
            "beside him", "Gece otobüsünde ay ışığında denize bakan Ali."),
   tiktok="Kızkalesi'nde 81 ilin ilk denizi 🌊 ve muza 'hayır' diyen Mert #JozhStudios",
   ig=("Mersin'de tantuni üç ısırık, cezerye yüz kilo! 🥕 Kızkalesi'nde yolculuğun ilk denizine girdik. 🌊\n\n"
       "Anamur'da muz seralarını görünce Mert durdu, düşündü ve dedi ki: 'Kural bir.' Herkes alkışlasın. 👏🍌\n\nYarın Antalya: Ali eve dönüyor. Kasa: {KASA}"),
   tags=["#Mersin", "#Kızkalesi", "#Cezerye"],
   son="Yarın Antalya: Ali eve dönüyor.",
   teaser="Üç ısırıkta tantuni, denizdeki kale ve eve giden bir gece otobüsü. Bölüm 34: Mersin. Pek yakında.")

# ======================================================================= 35 ANTALYA
EP(35, "Antalya", "Eve Dönüş",
   "Ali'nin evi, Hasan'ın serası, bir 'hayır' ve eski beyaz kamyonet.",
   "Sabah Kumluca'da Hasan oğluna sarılır. Seranın borcu ağırdır; Hasan, Ali'nin yolculuk kasasından yardım teklif etmesini bekler ama Ali "
   "'hayır' der: 'Önce söz verdiğimiz borç, baba. Ama domatesini biz satacağız.' Yüz yirmi ailenin siparişleri için seradan domates toplarlar; "
   "para doğrudan Hasan'a gider. Kalan zeytinyağı, fıstık, sabun ve cezeryenin yarısı Kaleiçi'nde satılır. Akşam Hasan onları eski beyaz kamyonetin önüne "
   "götürür ve anahtarı Mert'e değil Ali'ye verir. Gece sahilde Ali babasıyla barışmanın huzurunu yaşar.",
   {"sera": ("Kumluca, domates serası", "a long plastic-covered tomato greenhouse in Kumluca, Antalya: tall rows of tomato plants with red and "
             "green tomatoes, drip irrigation pipes, warm diffused light through the plastic"),
    "bahce": ("Hasan'ın evinin bahçesi", "the small garden of Hasan's simple village house near Kumluca: a lemon tree, a lemon-yellow wall, "
              "plastic crates, a garden table with tea glasses"),
    "kaleici": ("Kaleiçi", "a narrow cobbled street in Antalya's old town Kaleiçi: Ottoman houses with wooden bay windows and bougainvillea, "
                "small shops with colorful goods"),
    "garaj": ("Kamyonetin önü", "a dusty yard beside Hasan's greenhouse at sunset with an old white single-cab pickup truck from the early 2000s "
              "with a faded blue side stripe, a slightly dented tailgate, no brand logos and no lettering"),
    "sahil": ("Konyaaltı sahili", "Konyaaltı beach in Antalya at night: pebbles, calm dark sea, the lights of the city and the dark Beydağları "
              "mountains behind")},
   [
       S("08:00 sabah", "bahce", ["ali", "hasan", "mert"], "Baba",
         "Kumluca'da Hasan oğluna sarılır. Mert bir adım geride, bakır tası elinde bekler.",
         "Hasan walks out of the house door and stops; Ali drops his backpack and hugs his father tightly; Mert stands a step behind holding the "
         "small copper bowl, smiling with wet eyes.",
         [("hasan", "Oğlum... zayıflamışsın.", "emotional"),
          ("ali", "Sen de baba. Sen de.", "choked up")],
         "slow push-in from the garden gate", h="nemli"),
       S("09:30 sabah", "bahce", ["ali", "hasan"], "Hayır",
         "Bahçe masasında Hasan borcu anlatır ve Ali'nin kasasından yardım teklif etmesini bekler. Ali 'hayır' der ama bir yol gösterir.",
         "Hasan sits at the garden table turning his tea glass slowly; Ali sits across from him, takes a breath and shakes his head gently, then "
         "places his hand on his father's hand.",
         [("ali", "Kasadan veremem baba. Önce söz verdiğimiz borç. Ama domatesini biz satacağız.", "gentle, firm"),
          ("hasan", "Benim oğlum adam olmuş.", "proud, quiet")],
         "static medium two-shot across the table", h="nemli"),
       S("11:30 iç-gündüz", "sera", ["mert", "ali", "hasan"], "Yüz Yirmi Aile",
         "Serada yüz yirmi ailenin siparişi için domates toplarlar. Para doğrudan Hasan'a gidecektir.",
         "Mert, Ali and Hasan pick ripe red tomatoes into plastic crates between the tall plant rows; Mert holds up a perfect tomato to the light "
         "and grins; Hasan shows Ali how to twist the stem gently.",
         [("hasan", "Sapından çevir, koparma. Domates de insan gibi, nazik ister.", "teaching"),
          ("mert", "Hasan Amca, bu domatesler Instagram'da ünlü olacak!", "cheerful")],
         "slow tracking shot along the greenhouse row",
         kurgu="Domates satışı Hasan'ın kendi geliridir; JOZH kasasına yazılmaz."),
       S("15:30 ikindi", "kaleici", ["mert", "ali", "dukkan"], "Kaleiçi'nde Satış",
         "Kaleiçi'nde bir yöresel ürünler dükkânı kalan 40 litre zeytinyağını, 50 kilo cezeryeyi, 25 kilo Antep fıstığını ve 100 kalıp defne sabununu alır.",
         "The shop owner stacks oil tins and cezerye boxes on her shelves between colorful local products; Mert and Ali stand at the counter, Ali "
         "writing in the notebook, Mert waving at passing tourists.",
         [("dukkan", "Turist Kilis yağını da Mersin cezeryesini de sever. Hepsini alırım.", "pleased"),
          ("ali", "Yağ dört yüz elli, cezerye dört yüz.", "businesslike")],
         "static medium three-shot inside the shop",
         t=[U(40, "litre", 450, "satis", "Kilis zeytinyağı, Kaleiçi'nde ({adet} litre x {fiyat} TL)"),
            U(50, "kg", 400, "satis", "Mersin cezeryesi, Kaleiçi'nde (50 kg x 400 TL)"),
            U(25, "kg", 1300, "satis", "Belgeli Antep fıstığı, Kaleiçi'nde (25 kg x 1.300 TL)"),
            U(100, "kalıp", 120, "satis", "Hatay defne sabunu, Kaleiçi'nde (100 kalıp x 120 TL)")]),
       S("19:00 gün batımı", "garaj", ["mert", "ali", "hasan"], "Anahtar",
         "Hasan onları eski beyaz kamyonetin önüne götürür. Anahtarı Mert'e değil, Ali'ye verir.",
         "Hasan pats the hood of the old white pickup truck, pulls a key from his pocket and holds it out; Mert reaches for it automatically, but "
         "Hasan places it in Ali's palm; Mert laughs and raises his hands.",
         [("hasan", "Bu kamyonet yirmi yıl domates taşıdı. Şimdi sizin malınızı taşısın.", "warm, proud"),
          ("mert", "Anahtar Ali'de. Akıllıca Hasan Amca.", "laughing")],
         "slow push-in on the key in Ali's palm with the pickup behind",
         t=T("diger_gider", 3500, "Kamyonet bakımı: yağ, filtre ve lastik kontrolü")),
       S("22:00 gece", "sahil", ["mert", "ali"], "Ev Gibi",
         "Gece Konyaaltı'nda çakılların üstünde otururlar. Ali eve dönmenin huzurunu yaşar.",
         "Mert and Ali sit on the pebble beach with their shoes off, the sea quietly washing in; Ali throws a pebble into the dark water and leans "
         "back on his elbows; Mert lies down and looks at the stars.",
         [("ali", "Babam ilk kez bana 'adam olmuşsun' dedi.", "peaceful"),
          ("mert", "Ben söylemiştim. Sadece kamyonetin anahtarını vermedim.", "teasing")],
         "slow dolly-out revealing the city lights and the mountains",
         kurgu="Bu gece Hasan'ın evinde kalırlar; konaklama gideri yok."),
   ],
   misafir={"dukkan": ("DÜKKÂN SAHİBİ", "SHOP OWNER, a 52-year-old Turkish woman, elegant, grey-streaked hair in a bun, a linen shirt, "
                       "colorful necklace", "adult female voice, pleased, Antalya Turkish")},
   ay=AY, hava="nemli", urun="Sera domatesi, Antalya portakalı, piyaz; Kaleiçi, Konyaaltı, Kumluca seraları",
   sponsor="Sera üreticisi, yerel üretici ya da turizm alanında",
   kapak=("garaj", ["ali", "hasan", "mert"], "Hasan places a key into Ali's palm in front of an old white pickup truck at golden sunset while "
          "Mert laughs with his hands raised beside them", "Kamyonetin anahtarını Ali'ye veren Hasan, gülen Mert."),
   yakinda=("sera", ["ali", "hasan"], "Inside a greenhouse glowing with warm diffused light, a father's and son's silhouettes facing each "
            "other between tall tomato rows", "Işıl ışıl bir serada karşılıklı duran baba ve oğulun silüeti."),
   tiktok="Ali eve döndü 🥹 Babası anahtarı ona verdi #JozhStudios",
   ig=("Ali eve döndü. 🏡 Babası 'zayıflamışsın' dedi, Ali 'sen de baba' dedi. Ağlamadık. Yalan.\n\n"
       "Ali kasadan para vermedi: 'Önce söz verdiğimiz borç.' Ama 120 aile Hasan Amca'nın domatesini aldı (para doğrudan ona). 🍅\n\n"
       "Ve Hasan Amca bize 20 yıllık kamyonetini verdi. Anahtar? Ali'de. 😂 Kasa: {KASA}"),
   tags=["#Antalya", "#Kumluca", "#EveDönüş"],
   son="Artık bir kamyonetleri var. Anahtar Ali'de.",
   teaser="Bir baba, bir sera ve yirmi yıllık bir kamyonet. Bölüm 35: Antalya. Pek yakında.")

# ======================================================================= 36 ISPARTA
EP(36, "Isparta", "Gülün Şehri",
   "Kamyonetle ilk yolculuk, gül ürünleri, Eğirdir Gölü ve bir arıza sesi.",
   "Kamyonetle ilk yolculuk Isparta'ya: Ali direksiyonda, Mert yolcu koltuğunda radyoyu açmaya çalışır. Isparta'da gülün hasadının mayıs-haziran "
   "olduğunu, gül yağının bir kilosu için tonlarca gül gerektiğini öğrenirler. Bir gül atölyesinden gül suyu ve gül reçeli alırlar. Kalan "
   "cezerye bir pastaneye satılır. Eğirdir Gölü kıyısında Mert ilk kez direksiyona geçmek ister; Ali tereddüt eder. Akşam kamyonetten tuhaf "
   "bir ses gelir.",
   {"yol": ("Isparta yolu, kamyonet içi", "the cab of the old white pickup truck driving on a mountain road toward Isparta: worn grey seats, an "
            "old radio, a cracked dashboard, pine forests and lakes outside"),
    "gul": ("Gül atölyesi", "a rose products workshop in Isparta: copper stills for rose oil, glass bottles of rose water, jars of rose jam, "
            "dried pink rose petals in baskets, sweet light"),
    "pastane": ("Pastane", "a small patisserie in Isparta with glass cases of cakes and baklava, a marble counter"),
    "egirdir": ("Eğirdir Gölü", "the shore of Lake Eğirdir at sunset: calm turquoise-blue water, a small peninsula with old houses, mountains "
                "around, the old white pickup truck parked at the roadside"),
    "otopark": ("Pansiyon önü", "the gravel parking area of a lakeside guesthouse at night with the old white pickup truck under a single lamp, "
                "its hood open")},
   [
       S("08:30 sabah", "yol", ["mert", "ali"], "İlk Yolculuk",
         "Kamyonetle ilk yolculuk. Ali direksiyonda dikkatli, Mert eski radyoyu çalıştırmaya uğraşır.",
         "Ali drives with both hands firmly on the wheel; Mert twists the old radio knob, gets only static, then slaps the dashboard and a cheerful "
         "song crackles on; Mert dances in his seat, Ali smiles at the road.",
         [("mert", "Çalıştı! Bu kamyonet benden hoşlanıyor.", "triumphant"),
          ("ali", "Radyoyu sen yönet, direksiyonu ben.", "focused, amused")],
         "static medium two-shot through the windshield from outside, moving with the truck",
         t=T("ulasim", 1800, "Yakıt: Antalya-Isparta")),
       S("11:00 iç-gündüz", "gul", ["mert", "ali", "gulcu"], "Bir Kilo Gül Yağı",
         "Gül atölyesinde Ayten Hanım gül yağının imbikte nasıl damıtıldığını anlatır: bir kilo yağ için tonlarca gül.",
         "Ayten lifts a small glass vial of golden rose oil to the light by the copper still; Mert leans in to smell and closes his eyes; Ali "
         "scoops a handful of dried pink petals from a basket.",
         [("gulcu", "Bir kilo gül yağı için yaklaşık dört ton gül gerekir.", "proud"),
          ("mert", "Dört ton mu? Bu şişe bir servet!", "amazed")],
         "slow push-in on the vial in the light"),
       S("12:00 iç-gündüz", "gul", ["ali", "gulcu"], "Gül Suyu ve Reçel",
         "Gül yağı çok pahalıdır; onun yerine 200 şişe gül suyu ve gül reçeli alırlar.",
         "Ayten packs bottles of rose water and jars of rose jam into boxes; Ali checks a jar's seal and nods; she adds a few dried petals on top "
         "as a gift.",
         [("gulcu", "Gül suyu ve reçel karışık iki yüz adet, tanesi doksan.", "businesslike"),
          ("ali", "Gül yağı bir gün, inşallah. Bugün su ve reçel.", "smiling")],
         "static medium two-shot at the packing table",
         t=U(200, "adet", 90, "alis", "Isparta gül suyu ve gül reçeli ({adet} adet x {fiyat} TL)")),
       S("14:00 iç-gündüz", "pastane", ["mert", "pastaci"], "Cezerye Pastanede",
         "Bir pastane kalan 50 kilo cezeryeyi alır.",
         "The pastry chef cuts a cezerye bar in half, tastes it and nods; Mert sets the boxes on the marble counter and takes the money with a "
         "small bow.",
         [("pastaci", "Mersin cezeryesi vitrinime yakışır. Elli kilo.", "pleased"),
          ("mert", "Dört yüz yirmiden. Afiyet olsun Isparta!", "cheerful")],
         "static medium two-shot at the counter",
         t=[U(50, "kg", 420, "satis", "Mersin cezeryesi, pastaneye ({adet} kg x {fiyat} TL)"), T("yemek", 700, "Öğle yemeği")]),
       S("19:00 gün batımı", "egirdir", ["mert", "ali"], "Direksiyon",
         "Eğirdir Gölü kıyısında Mert direksiyona geçmek ister. Ali motor kazasını hatırlar ve tereddüt eder.",
         "Mert stands by the driver's door of the pickup with an open hand; Ali holds the key tightly, looks at the lake, then at Mert, and slowly "
         "drops the key into his palm.",
         [("mert", "Ben de sürmek istiyorum Ali. Dikkatli, söz.", "sincere"),
          ("ali", "Motoru hatırlıyorsun değil mi? Yavaş. Çok yavaş.", "nervous, trusting")],
         "slow push-in on the key passing hands, the lake glowing behind"),
       S("22:00 gece", "otopark", ["mert", "ali"], "Tuhaf Ses",
         "Gece pansiyonun önünde kamyonetin kaputunu açarlar. Motordan tuhaf bir tıkırtı gelmektedir.",
         "Mert holds a phone flashlight over the open engine while Ali listens with his head tilted; a metallic ticking sound comes from the "
         "engine; they look at each other in worry.",
         [("ali", "Bu ses iyi bir ses değil.", "worried"),
          ("mert", "Ben sürünce mi başladı? Lütfen hayır de.", "guilty")],
         "static medium two-shot under the lamp",
         t=T("konaklama", 1200, "Göl kenarı pansiyon, 1 gece")),
   ],
   misafir={"gulcu": ("AYTEN HANIM", "AYTEN, a 55-year-old Turkish woman rose producer, elegant, short silver hair, a rose-pink scarf, a white "
                      "linen apron", "adult female voice, proud and gentle, Isparta Turkish"),
            "pastaci": ("PASTACI", "PASTRY CHEF, a 40-year-old Turkish man, chubby, a white chef hat, a friendly round face", "adult male voice")},
   ay=AY, hava="ılık", urun="Gül yağı, gül suyu, gül reçeli, Isparta halısı; Eğirdir Gölü",
   sponsor="Gül ürünleri, halı ya da göl turizmi alanında",
   kapak=("gul", ["mert", "ali"], "Mert and Ali stand in a shower of dried pink rose petals in a workshop with copper stills, Mert throwing petals "
          "in the air, Ali laughing, soft rosy light", "Gül yaprağı yağmurunda gülen Mert ve Ali."),
   yakinda=("otopark", ["mert", "ali"], "An old pickup truck with its hood open under a single lamp at night, two worried faces lit by a "
            "flashlight over the dark engine", "Gece tek lamba altında kaputu açık kamyonet ve iki endişeli yüz."),
   tiktok="1 kilo gül yağı için 4 ton gül 🌹 ve kamyonetten gelen tuhaf ses #JozhStudios",
   ig=("Kamyonetle ilk yolculuk! Ali direksiyonda, Mert radyoda. 🚚🎶\n\n"
       "Isparta'da öğrendik: 1 kilo gül yağı için yaklaşık 4 ton gül gerekiyor. 🌹 Gül suyu ve reçel aldık, cezeryenin kalanı pastanede.\n\n"
       "Eğirdir'de Ali anahtarı Mert'e verdi... ve gece motordan bir ses geldi. 😬 Kasa: {KASA}"),
   tags=["#Isparta", "#Gül", "#Eğirdir"],
   son="Kamyonetin motorundan tuhaf bir tıkırtı geliyor. Yarın Burdur'da taksit günü.",
   teaser="Dört ton gül, bir anahtar ve gece gelen bir ses. Bölüm 36: Isparta. Pek yakında.")

# ======================================================================= 37 BURDUR
EP(37, "Burdur", "Salda'nın Beyazı",
   "Sezon finali: sanayi sitesinde bir usta, Salda Gölü, ceviz ezmesi ve 100.000 TL'lik üçüncü taksit.",
   "Sabah Burdur sanayi sitesinde usta kamyonetin sesini dinler: Mert suçsuzdur, eski bir supap ayarıdır. Tamir parası çıkar. Ceviz "
   "ezmesi atölyesinde Burdur'un meşhur ceviz ezmesini tadar, gül ürünlerinin bir kısmını aynı atölyenin dükkânına satarlar. Şiş köfte "
   "yerler. Öğleden sonra Salda Gölü'nün bembeyaz kıyısında üçüncü taksiti gönderirler: 100.000 TL. Mert kasanın anahtarını, yani defteri, "
   "tamamen Ali'ye bırakır. Gün batımında Ege'ye bakarlar.",
   {"sanayi": ("Burdur sanayi sitesi", "a small auto repair shop in Burdur's industrial estate: an open garage door, tools on the wall, the old "
               "white pickup truck with its hood up, oil stains on the concrete"),
    "ceviz": ("Ceviz ezmesi atölyesi", "a walnut paste workshop in Burdur: trays of walnut paste rolls, a stone grinder, sacks of walnuts, a "
              "small shop counter with shelves"),
    "kofte": ("Şiş köfteci", "a Burdur şiş köfte restaurant: long skewers of grilled meatballs on a charcoal grill, roasted peppers and "
              "tomatoes, simple tables"),
    "salda": ("Salda Gölü", "the shore of Lake Salda: blinding white mineral sand beaches, incredibly clear turquoise water, pine-covered hills "
              "around, the old white pickup truck parked far behind on the road")},
   [
       S("08:30 sabah", "sanayi", ["mert", "ali", "usta"], "Suçlu Kim?",
         "Sanayi ustası motoru dinler. Mert suçsuzdur: eski bir supap ayarıdır.",
         "The mechanic leans over the open engine with a stethoscope-like listening tool, listens, then straightens up and points at Mert with a "
         "wrench; Mert freezes, the mechanic laughs and shakes his head.",
         [("usta", "Senin suçun yok delikanlı. Supap ayarı, kamyonet yaşlı.", "amused"),
          ("mert", "Duydun mu Ali? Suçsuzum!", "relieved, triumphant")],
         "static medium three-shot in the garage doorway",
         t=T("diger_gider", 4200, "Kamyonet tamiri: supap ayarı ve işçilik")),
       S("10:30 iç-gündüz", "ceviz", ["mert", "ali", "cevizci"], "Ceviz Ezmesi",
         "Ceviz ezmesi atölyesinde taş değirmende öğütülen cevizin şekerle yoğrulduğunu görürler. Atölyenin dükkânı gül ürünlerinin bir kısmını alır.",
         "The workshop owner breaks a walnut paste roll and hands pieces to Mert and Ali; both taste and their eyes widen; Ali then places a box "
         "of rose water bottles on her counter.",
         [("cevizci", "Ceviz ezmesi Burdur'un tatlısıdır. Gül suyunu da dükkânıma alırım.", "proud"),
          ("ali", "Yüz adet gül suyu ve reçel, tanesi yüz altmış.", "businesslike")],
         "slow push-in on the stone grinder and their faces",
         t=U(100, "adet", 160, "satis", "Isparta gül suyu ve reçeli, Burdur'da ({adet} x {fiyat} TL)")),
       S("11:30 iç-gündüz", "ceviz", ["ali", "cevizci"], "Altmış Kilo",
         "Altmış kilo ceviz ezmesi alırlar. Ege'de satılacaktır.",
         "The workshop owner stacks wrapped walnut paste rolls into boxes; Ali counts money onto the counter and Mert carries boxes toward the "
         "door, sneaking a bite.",
         [("cevizci", "Kilosu dört yüz elli. Serin yerde dayanır.", "confident"),
          ("ali", "Altmış kilo. Mert, kutudan yeme!", "scolding, laughing")],
         "static medium two-shot at the counter",
         t=U(60, "kg", 450, "alis", "Burdur ceviz ezmesi ({adet} kg x {fiyat} TL)")),
       S("13:00 iç-gündüz", "kofte", ["mert", "ali"], "Şiş Köfte",
         "Burdur şiş köftesiyle sezonun son öğle yemeği. Gül suyunun kalanı da siparişlerle satılmıştır.",
         "Mert slides a juicy meatball off a long skewer onto his bread; Ali shows his phone with a satisfied nod; Mert gives a thumbs-up with "
         "his mouth full.",
         [("ali", "Kalan yüz gül suyu da siparişle gitti.", "pleased"),
          ("mert", "Isparta'nın gülü, Burdur'un köftesi. Akdeniz bize iyi geldi.", "mouth full")],
         "static medium two-shot across the table",
         t=[U(100, "adet", 160, "satis", "Isparta gül suyu ve reçeli, takipçi siparişi ({adet} x {fiyat} TL)"), T("yemek", 800, "Şiş köfte (2 kişi)")]),
       S("16:00 ikindi", "salda", ["mert", "ali"], "Yüz Bin",
         "Salda Gölü'nün bembeyaz kıyısında üçüncü taksiti gönderirler: 100.000 TL. Mert onay tuşuna basmaz; Ali'ye bırakır.",
         "Mert and Ali sit on the white mineral sand by the turquoise water; Ali holds the phone ready and offers it to Mert as before; Mert "
         "pushes it gently back to Ali and nods; Ali presses send.",
         [("mert", "Bu sefer sen bas. Kasa senin, ben satarım.", "sincere"),
          ("ali", "Yüz bin lira... gitti.", "breathless, proud")],
         "slow push-in from the water toward them",
         t=T("borc", 100000, "3. taksit: Cemil Bey (Akdeniz sezonu sonu)")),
       S("19:30 gün batımı", "salda", ["mert", "ali"], "Defterin Sahibi",
         "Gün batımında Mert, kahverengi defteri Ali'nin ceketinin cebine koyar: kasanın tamamı artık Ali'dedir. Sırada Ege var.",
         "Mert takes the brown leather notebook from the sand, brushes it off and tucks it into Ali's shirt pocket with a pat; Ali looks at him, "
         "then both stand and look west at the sunset over the lake.",
         [("mert", "Defter artık tamamen senin. Ben sadece hayal ederim.", "warm"),
          ("ali", "Hayal etmeyi bırakma. Ege'de büyük bir fikre ihtiyacımız var.", "smiling")],
         "slow dolly-out and crane-up revealing the white shore and the lake",
         t=[T("konaklama", 1100, "Pansiyon, 1 gece"), T("ulasim", 1600, "Yakıt: Burdur-Denizli")],
         kurgu="Sezon sonu kartı (kurguda): SEZON 3 BİTTİ · 8 İL · 3. TAKSİT ÖDENDİ"),
   ],
   misafir={"usta": ("SANAYİ USTASI", "MECHANIC, a 58-year-old Turkish man, stocky, grey stubble, oil-stained blue overalls, a rag on his shoulder",
                     "mature male voice, amused, Burdur Turkish"),
            "cevizci": ("CEVİZ EZMESİ USTASI", "WALNUT PASTE MAKER, a 50-year-old Turkish woman, sturdy, a navy headscarf, a white apron",
                        "adult female voice, proud")},
   ay=AY, hava="ılık", urun="Ceviz ezmesi, Burdur şiş köfte, kilim; Salda Gölü, Sagalassos",
   sponsor="Ceviz ezmesi, yöresel yemek ya da göl turizmi alanında",
   kapak=("salda", ["mert", "ali"], "Mert and Ali sit on a blinding white beach by impossibly turquoise water, Ali pressing a phone screen, Mert "
          "beside him with a proud smile, pine hills behind", "Salda'nın beyaz kıyısında taksiti gönderen Ali ve Mert."),
   yakinda=("salda", ["mert", "ali"], "Two silhouettes on a white shore against a fiery sunset, one tucking a small notebook into the other's "
            "pocket, the lake glowing", "Gün batımında bembeyaz kıyıda defteri arkadaşının cebine koyan bir el."),
   tiktok="Salda'nın beyazında 100.000 TL taksit 🏝️ #JozhStudios",
   ig=("Akdeniz bitti! 🌊 Kamyonetin sesi Mert'in suçu değilmiş (supap ayarı 😅). Burdur'da ceviz ezmesi aldık, şiş köfte yedik.\n\n"
       "Salda Gölü'nün bembeyaz kıyısında üçüncü taksiti gönderdik: 100.000 TL. Ve Mert defteri tamamen Ali'ye bıraktı. 📒\n\n"
       "Sezon 4: Ege. Büyük bir fikre ihtiyacımız var. Kasa: {KASA}"),
   tags=["#Burdur", "#SaldaGölü", "#SezonFinali"],
   son="Defter artık tamamen Ali'de. Ege'de büyük bir fikre ihtiyaçları var.",
   teaser="Suçsuz bir sürücü, beyaz bir kıyı ve yüz binlik bir taksit. Bölüm 37: Burdur, sezon finali. Pek yakında.")
