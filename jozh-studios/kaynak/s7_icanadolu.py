# -*- coding: utf-8 -*-
"""Sezon 7 · Son Hesap · İç Anadolu (Bölüm 75-87). Aralık, kar. Kamyonetle.
Rota: Çankırı → Kırıkkale → Kırşehir → Yozgat → Sivas → Kayseri → Nevşehir → Niğde → Aksaray → Karaman → Konya → Eskişehir → Ankara
'Final Kutusu' (400 adet): her bölgeden bir ürün, yolculukta tanıştıkları üreticilerden: Malatya kayısısı (Doğu, Ramazan Amca),
Antep fıstığı (Güneydoğu), Isparta gül reçeli (Akdeniz, Ayten Hanım), Aydın inciri (Ege, Halime Teyze), Edirne badem ezmesi (Marmara),
Çorum leblebisi (Karadeniz), Mevlana şekeri (İç Anadolu) ve bir paket Çankırı kaya tuzu ('tuz-ekmek hakkı').
Ön sipariş Yozgat'ta açılır; mallar Konya'da teslim alınıp kutulanır. Final: 31 Aralık gecesi Ankara."""
from ortak import EP, S, T, U

AY = "Aralık"
K = "ceket"

# ======================================================================= 75 ÇANKIRI
EP(75, "Çankırı", "Tuz Bozulmaz",
   "Son sezon tuz mağarasında başlar; eski dostlara telefonlar ve Final Kutusu'nun planı.",
   "Son sezonun ilk durağı Çankırı. Binlerce yıldır işletilen tuz mağarasının bembeyaz galerilerinde yürürler; rehber 'tuz bozulmaz' der, Ali "
   "ekler: 'söz de bozulmamalı.' Mağaradan 400 küçük paket kaya tuzu alırlar: Final Kutusu'nun 'tuz-ekmek hakkı'. Öğlen Çankırı'nın ünlü "
   "yaren sohbetlerinden birine konuk olurlar. Akşam Ali yolculuktaki üreticileri tek tek arar: Ramazan Amca, Ayten Hanım, Halime Teyze... "
   "Hepsi 'evet' der.",
   {"magara": ("Çankırı tuz mağarası", "inside the Çankırı rock salt cave: wide tunnels carved into glittering white and grey rock salt, salt "
               "sculptures, soft warm lighting, a cool dry air"),
    "yaren": ("Yaren sohbeti", "a traditional yaren gathering room in Çankırı: men sitting on cushions around a low table with tea, a bağlama "
              "on the wall, carpets, warm lamp light"),
    "otel": ("Otel odası", "a hotel room in Çankırı at night: the brown notebook open on the bed with a list of names, a phone, snow outside "
             "the window")},
   [
       S("09:30 iç-gündüz", "magara", ["mert", "ali", "rehber"], "Tuz Bozulmaz",
         "Tuz mağarasının bembeyaz galerilerinde rehber Yunus Bey, mağaranın binlerce yıldır işletildiğini anlatır.",
         "The guide runs his hand along the glittering salt wall and holds up a crystal of rock salt to the light; Mert licks his fingertip "
         "after touching the wall and makes a face; Ali laughs.",
         [("rehber", "Tuz bozulmaz. Binlerce yıldır bu dağdan çıkar.", "proud"),
          ("ali", "Söz de bozulmamalı. Son sezonun sözü bu olsun.", "thoughtful")],
         "slow tracking shot through the salt tunnel"),
       S("10:30 iç-gündüz", "magara", ["mert", "ali", "rehber"], "Tuz-Ekmek Hakkı",
         "Mağaradan Final Kutusu için 400 küçük paket kaya tuzu alırlar: tuz-ekmek hakkı.",
         "The guide places small cloth bags of rock salt crystals into a crate; Mert ties one bag with a string and holds it up; Ali counts money "
         "into the guide's hand.",
         [("rehber", "Tanesi otuz lira. Her kutuda bir avuç tuz, bereket getirir.", "warm"),
          ("mert", "Seksen bir ilde tuz-ekmek yedik. Hakkını kutuya koyuyoruz.", "moved")],
         "slow push-in on the salt bag",
         t=U(400, "paket", 30, "alis", "Çankırı kaya tuzu, küçük paket ({adet} x {fiyat} TL)")),
       S("13:00 iç-gündüz", "yaren", ["mert", "ali", "yaren"], "Yaren",
         "Öğlen Çankırı'nın yaren sohbetlerinden birine konuk olurlar. Yaşlı yaren başı onlara bir öğüt verir.",
         "The elder of the gathering pours tea into their glasses and lifts his own glass to them; the men around, softly out of focus, nod; Mert "
         "and Ali sit cross-legged, listening respectfully.",
         [("yaren", "Yarenlikte söz bir kere söylenir, yerine getirilir.", "slow, wise"),
          ("mert", "Bizim de bir sözümüz var. Ankara'da bitecek.", "respectful")],
         "static medium three-shot at the low table",
         t=T("yemek", 800, "Öğle yemeği")),
       S("17:00 ikindi", "magara", ["mert", "ali"], "Son Sezon",
         "Mağaradan çıkarken kar yağmaya başlar. Ali Final Kutusu fikrini netleştirir: her bölgeden bir ürün, tanıştıkları ustalardan.",
         "Mert and Ali walk out of the cave entrance into falling snow; Ali stops and lists items on his fingers; Mert catches snowflakes on his "
         "tongue, then turns to listen.",
         [("ali", "Her bölgeden bir ürün. Hepsi tanıştığımız ustalardan.", "inspired"),
          ("mert", "Ramazan Amca'nın kayısısıyla başlarız!", "excited")],
         "static wide shot at the cave entrance", h="kar"),
       S("20:30 iç-gece", "otel", ["ali", "~ramazan"], "İlk Telefon",
         "Ali ilk telefonu Malatya'ya, Ramazan Amca'ya açar. Ramazan Amca onları videolardan izlemektedir.",
         "Ali sits on the bed with the phone at his ear and the notebook list beside him; he starts to smile widely as he listens. His lips stay "
         "closed while Ramazan speaks.",
         [("ramazan", "Sizi her akşam izliyorum evlat! Kayısı benden, en iyisinden.", "joyful, from the phone speaker"),
          ("ali", "Ramazan Amca, yüz kilo. Konya'ya.", "happy")],
         "slow push-in to Ali's face", h="kar"),
       S("22:00 iç-gece", "otel", ["mert", "ali"], "Hepsi Evet",
         "Gece Ali listedeki son ismin yanına tik atar: Antep'teki üretici, Ayten Hanım, Halime Teyze, Edirne'nin ustası... Hepsi evet demiştir.",
         "Ali puts a final tick next to the last name on the list and shows the page to Mert, who lies on the other bed; Mert sits up and reads "
         "every name aloud slowly, smiling.",
         [("mert", "Ramazan Amca, Ayten Hanım, Halime Teyze... hepsi evet.", "moved"),
          ("ali", "Seksen bir il, bir kutuda buluşacak.", "emotional")],
         "static medium two-shot between the beds",
         t=[T("konaklama", 1200, "Otel, 1 gece"), T("ulasim", 700, "Yakıt: Çankırı-Kırıkkale")]),
   ],
   misafir={"rehber": ("YUNUS BEY", "YUNUS, a 55-year-old Turkish salt cave guide, stocky, a grey beard, a thick padded jacket and a woolen cap",
                       "mature male voice, proud, Central Anatolian Turkish"),
            "yaren": ("YAREN BAŞI", "GATHERING ELDER, a 75-year-old Turkish man, thin, a white beard, a black flat cap, a dark suit jacket over a "
                      "knitted vest", "elderly male voice, slow, wise"),
            "ramazan": ("RAMAZAN AMCA", "RAMAZAN, a 62-year-old Turkish apricot merchant from Malatya", "elderly male voice, warm husky baritone, "
                        "cheerful Malatya Turkish")},
   ay=AY, hava="kar", kiyafet=K, urun="Çankırı kaya tuzu, yaren sohbetleri, Çankırı yoğurdu; tuz mağarası",
   sponsor="Kaya tuzu ya da kültür turizmi alanında",
   kapak=("magara", ["mert", "ali", "rehber"], "Mert and Ali stand in a glittering white salt tunnel holding up a sparkling salt crystal to the "
          "warm light, the guide smiling beside them", "Işıl ışıl tuz mağarasında tuz kristalini ışığa tutan Mert ve Ali."),
   yakinda=("otel", ["ali"], "A worn brown notebook with a handwritten list of names lit by a single bedside lamp, a pen ticking the last line, "
            "snow falling outside the dark window", "Lamba ışığında isim listesi ve son satıra atılan tik."),
   tiktok="Son sezon başladı: tuz bozulmaz, söz de bozulmaz 🧂 #JozhStudios",
   ig=("Son sezon! İç Anadolu'dayız. ❄️ Çankırı'nın tuz mağarasında rehberimiz dedi ki: 'Tuz bozulmaz.' Ali ekledi: 'Söz de bozulmamalı.' 🧂\n\n"
       "Final Kutusu geliyor: her bölgeden bir ürün, hepsi yolda tanıştığımız ustalardan. Ramazan Amca, Ayten Hanım, Halime Teyze... hepsi 'evet' dedi! 🥹\n\nKasa: {KASA}"),
   tags=["#Çankırı", "#TuzMağarası", "#FinalKutusu"],
   son="Yolculuktaki bütün üreticiler Final Kutusu'na 'evet' der.",
   teaser="Bozulmayan tuz, bir yaren sözü ve bir isim listesi. Bölüm 75: Çankırı, son sezon. Pek yakında.")

# ======================================================================= 76 KIRIKKALE
EP(76, "Kırıkkale", "Yolların Kavşağı",
   "Karlı otoyolda yolda kalan bir aile, Kızılırmak kıyısı ve fazladan leblebi.",
   "Kırıkkale'ye karlı bir sabah girerler; şehir Ankara'ya giden yolların kavşağıdır. Otoyolda arabası arızalanan bir aileye yardım edip "
   "çocuklarını kamyonetin sıcak kabininde bekletirler. Kutu için gerekenden fazla kalan 50 kilo leblebi bir kuruyemişçiye satılır. "
   "Kızılırmak'ın kıyısında Mert, Ali'ye yolculuk boyunca en çok neyi öğrendiğini sorar. Ali'nin cevabı kısadır: 'Seni.' Akşam Hatice "
   "arar: Ankara'ya gelmek istemektedir.",
   {"otoyol": ("Karlı otoyol kenarı", "the snowy shoulder of a highway near Kırıkkale: a small family car with its hood up and hazard lights, the "
               "old white pickup truck parked behind it, snowy fields, grey sky"),
    "kabin": ("Kamyonetin kabini", "the warm cab of the old white pickup truck with the heater on, foggy windows, two small children wrapped in "
              "a blanket on the seat"),
    "kuruyemis": ("Kuruyemişçi", "a nut and dried fruit shop in Kırıkkale with sacks of leblebi, a scale and a warm stove"),
    "nehir": ("Kızılırmak kıyısı", "the snowy bank of the Kızılırmak river near Kırıkkale: a wide reddish-brown river, bare poplar trees, snow "
              "on the ground, a bench"),
    "otel": ("Otel lobisi", "a small hotel lobby in Kırıkkale at night with a sofa, a tea machine and snow falling outside the glass door")},
   [
       S("09:00 sabah", "otoyol", ["mert", "ali", "baba"], "Yolda Kalan Aile",
         "Karlı otoyolda arabası arızalanan bir aileyi görüp dururlar. Baba çekiciyi beklemektedir.",
         "Mert pulls the pickup onto the snowy shoulder behind a small car with its hood up; the father waves gratefully; Ali gets out and offers "
         "to let the children wait in the warm pickup cab.",
         [("baba", "Çekici bir saat sonra gelecekmiş. Çocuklar üşüyor.", "worried"),
          ("ali", "Çocuklar kamyonette beklesin, kalorifer açık.", "kind")],
         "static wide shot on the highway shoulder", h="kar"),
       S("09:30 iç-gündüz", "kabin", ["mert"], "Sıcak Kabin",
         "Mert kabinde iki çocuğa leblebi verir ve kasa sayacının hikâyesini anlatır.",
         "Mert sits sideways in the driver's seat, handing small handfuls of leblebi to two children wrapped in a blanket; he mimes a counter going "
         "up with his finger and the children giggle.",
         [("mert", "Biz seksen bir ili gezdik. Bu kamyonet her yere gitti!", "storytelling, warm")],
         "static medium shot inside the cab"),
       S("12:00 iç-gündüz", "kuruyemis", ["ali", "kuruyemisci"], "Fazla Leblebi",
         "Kutu için gerekenden fazla kalan 50 kilo leblebi bir kuruyemişçiye satılır.",
         "The shopkeeper pours roasted chickpeas onto the scale, tastes a few and nods; Ali writes in the notebook and receives the money by the "
         "warm stove.",
         [("kuruyemisci", "Çorum leblebisi! Elli kilo, üç yüzden.", "pleased"),
          ("ali", "Yüz kilo kutuya, elli kilo size. Hesap tamam.", "precise")],
         "static medium two-shot at the scale",
         t=[U(50, "kg", 300, "satis", "Çorum leblebisi, Kırıkkale'de ({adet} kg x {fiyat} TL)"), T("yemek", 700, "Öğle yemeği")]),
       S("15:00 ikindi", "nehir", ["mert", "ali"], "En Çok Ne Öğrendin?",
         "Kızılırmak'ın karlı kıyısında Mert sorar: yolculuk boyunca en çok neyi öğrendin? Ali'nin cevabı kısadır.",
         "Mert and Ali sit on a snowy bench by the wide reddish river; Mert asks while looking at the water; Ali answers without hesitation and "
         "Mert turns to him, surprised, then laughs and puts his arm around him.",
         [("mert", "Bu yolculukta en çok neyi öğrendin Ali?", "curious"),
          ("ali", "Seni. Ve kendimi.", "sincere, simple")],
         "slow push-in from across the river", h="kar"),
       S("20:00 iç-gece", "otel", ["mert", "~hatice"], "Annem Geliyor",
         "Akşam Hatice arar: oğlunun son taksiti ödeyişini görmek için yılbaşında Ankara'ya gelmek istemektedir.",
         "Mert sits on the lobby sofa with the phone at his ear, his eyes filling with tears as he listens; he nods again and again. His lips stay "
         "closed while his mother speaks.",
         [("hatice", "Oğlum, yılbaşında Ankara'ya geleceğim. O son günü görmek istiyorum.", "emotional, from the phone speaker"),
          ("mert", "Gel anne. Otobüs bileti benden.", "choked up")],
         "slow push-in to Mert's face", h="kar"),
       S("21:00 iç-gece", "otel", ["mert", "ali"], "Babamı da Çağıralım",
         "Ali de babasını çağırmak ister. İkisi aynı anda telefona sarılır.",
         "Ali sits down next to Mert on the sofa and pulls out his phone; they look at each other and smile; both start dialing at the same time, "
         "the snow falling outside the glass door.",
         [("ali", "Babamı da çağırıyorum. Hasan Bey Ankara'yı görmedi hiç.", "smiling"),
          ("mert", "Yılbaşı gecesi iki aile, bir kamyonet.", "happy")],
         "static medium two-shot on the sofa",
         t=[T("konaklama", 1100, "Otel, 1 gece"), T("ulasim", 700, "Yakıt: Kırıkkale-Kırşehir"),
            T("diger_gider", 1600, "Hatice ve Hasan için Ankara otobüs biletleri")]),
   ],
   misafir={"baba": ("BABA", "FATHER, a 38-year-old Turkish man, slim, a short beard, a grey puffer jacket, worried eyes", "adult male voice, worried"),
            "kuruyemisci": ("KURUYEMİŞÇİ", "SHOPKEEPER, a 58-year-old Turkish man, round, a grey cap, a brown vest", "mature male voice, pleased")},
   ay=AY, hava="kar", kiyafet=K, urun="Kızılırmak, Keskin bağları; Ankara yolunun kavşağı",
   sponsor="Yerel esnaf ya da yol üstü işletmeler olarak",
   kapak=("nehir", ["mert", "ali"], "Mert and Ali sit on a snowy bench by a wide reddish river, Mert's arm around Ali's shoulders, both laughing, "
          "bare poplars and falling snow", "Karlı bankta Kızılırmak kıyısında sarılan Mert ve Ali."),
   yakinda=("otoyol", ["mert", "ali"], "A small family car with hazard lights blinking on a snowy highway, the headlights of a pickup truck "
            "approaching from behind through the falling snow", "Karlı otoyolda dörtlüleri yanan bir araba ve arkadan yaklaşan farlar."),
   tiktok="'Bu yolculukta en çok neyi öğrendin?' 'Seni.' 🥹 #JozhStudios",
   ig=("Kırıkkale'de karlı otoyolda yolda kalan bir aileye yardım ettik; çocuklar kamyonetin sıcak kabininde leblebi yedi. 🚚❄️\n\n"
       "Kızılırmak kıyısında Mert sordu: 'En çok neyi öğrendin?' Ali: 'Seni. Ve kendimi.' 🥹\n\n"
       "Akşam Hatice Teyze aradı: yılbaşında Ankara'ya geliyor! Hasan Amca da geliyor. Kasa: {KASA}"),
   tags=["#Kırıkkale", "#Kızılırmak", "#Aile"],
   son="Hatice ve Hasan yılbaşı gecesi Ankara'ya gelecek.",
   teaser="Karlı bir otoyol, sıcak bir kabin ve tek kelimelik bir cevap. Bölüm 76: Kırıkkale. Pek yakında.")

# ======================================================================= 77 KIRŞEHİR
EP(77, "Kırşehir", "Eline, Beline, Diline",
   "Ahi Evran'ın öğüdü, Cacabey'in gökyüzü ve bir kahvehanede bozlak.",
   "Kırşehir'de sabah Ahi Evran Türbesi'nin önünde, ahilik geleneğini anlatan bir esnaf ustasından üç öğüdü dinlerler: eline, beline, "
   "diline sahip ol. Ali bu üç öğüdü defterin ilk sayfasına yazar. Cacabey Medresesi'nin bir zamanlar gökyüzünü gözlemek için kullanılan "
   "kubbesinin altında dururlar. Bir kahvehanede bozlak dinlerler; usta, Neşet Ertaş'ın bu topraklardan çıktığını anlatır. Akşam Mert "
   "üç öğüdün kendisi için ne demek olduğunu söyler.",
   {"turbe": ("Ahi Evran Türbesi önü", "the courtyard in front of the Ahi Evran tomb complex in Kırşehir: old stone buildings, a domed tomb, "
              "snow on the ground, a few trees"),
    "cacabey": ("Cacabey Medresesi", "the Cacabey Madrasa in Kırşehir: a 13th-century stone building with a carved portal and a central dome "
                "with an opening, once used to observe the sky, cold light"),
    "kahve": ("Kahvehane", "a warm traditional coffeehouse in Kırşehir: wooden chairs, a stove, tea glasses, a bağlama player on a low stool, "
              "photos on the wall"),
    "otel": ("Termal otel odası", "a thermal hotel room in Kırşehir at night: steam from a small private thermal bath visible through a door, "
             "two beds, snow outside")},
   [
       S("09:00 sabah", "turbe", ["mert", "ali", "ahi"], "Üç Öğüt",
         "Ahi Evran Türbesi'nin önünde esnaf ustası Kadir Usta ahiliğin üç öğüdünü anlatır.",
         "Kadir raises three fingers one by one in the snowy courtyard: hand, waist, tongue; Mert and Ali listen closely; Ali writes in the "
         "notebook with cold fingers.",
         [("ahi", "Eline, beline, diline sahip ol. Ahi esnafı böyle yaşar.", "wise, slow"),
          ("mert", "Elim, belim, dilim... en zoru dil usta.", "honest, laughing")],
         "slow push-in to Kadir's raised fingers", h="kar"),
       S("09:30 sabah", "turbe", ["ali", "ahi"], "İlk Sayfa",
         "Ali bu üç öğüdü defterin ilk sayfasına, 'KASA' yazısının altına yazar. Usta yazıya bakar ve gülümser.",
         "Ali opens the worn brown notebook to the very first page where the word KASA is underlined, and writes three short lines beneath it; "
         "Kadir leans in, reads and pats Ali's shoulder.",
         [("ahi", "Kasanın altına yazmışsın. Doğru yere yazmışsın.", "approving"),
          ("ali", "Her şey bu sayfayla başladı. Bununla da bitsin.", "moved")],
         "slow push-in on the notebook page", h="kar"),
       S("12:00 iç-gündüz", "cacabey", ["mert", "ali"], "Gökyüzünü Gözlemek",
         "Cacabey Medresesi'nin kubbesinin altında dururlar. Bir zamanlar burada gökyüzü gözlenmiştir.",
         "Mert and Ali stand in the center under the dome with its opening, looking up at the grey sky; snowflakes drift down through the opening "
         "onto their faces.",
         [("ali", "Yüzyıllar önce burada yıldızları izlemişler.", "awed"),
          ("mert", "Biz de seksen bir il boyunca kasa sayacını izledik.", "smiling")],
         "slow crane-up from their faces to the dome opening", h="kar",
         t=T("yemek", 800, "Öğle yemeği")),
       S("16:00 iç-gündüz", "kahve", ["mert", "ali", "ozan"], "Bozlak",
         "Bir kahvehanede yaşlı bir ozan bağlamayla bozlak söyler; Neşet Ertaş'ın bu topraklardan çıktığını anlatır.",
         "The old minstrel plays the bağlama and sings a long mournful bozlak note; Mert and Ali sit still with tea glasses in their hands; Ali "
         "closes his eyes.",
         [("ozan", "Bozlak bozkırın sesidir. Neşet Ertaş bu topraktan çıktı.", "soft, proud"),
          ("ali", "Bozkırın sesi... içimize işledi.", "whisper")],
         "slow push-in through the coffeehouse to the minstrel",
         kurgu="Ozanın söylediği yalnızca kısa bir uzun hava nağmesidir; telifli bir eser çalınmaz."),
       S("20:30 iç-gece", "otel", ["mert", "ali"], "Benim İçin",
         "Akşam termal otelde Mert, üç öğüdün kendisi için ne demek olduğunu söyler.",
         "Mert sits on the edge of the bed with a towel around his neck after the thermal bath, steam drifting behind him; he counts on his "
         "fingers; Ali listens, smiling.",
         [("mert", "Elim: helal kazanç. Belim: sözüm. Dilim: önce sana sormak.", "sincere"),
          ("ali", "Bunu da ilk sayfaya yazıyorum.", "touched")],
         "static medium two-shot, steam in the background"),
       S("22:00 iç-gece", "otel", ["mert", "ali"], "Yozgat'ta Ön Sipariş",
         "Gece Final Kutusu'nun ön sipariş videosunu çekerler. Sipariş Yozgat'ta açılacaktır.",
         "Mert and Ali sit side by side facing a phone propped on the table like a camera, rehearsing; Mert holds up an empty kraft box, Ali "
         "holds up a small bag of salt; they laugh at their first take and start again.",
         [("mert", "Seksen bir il, yedi bölge, tek kutu!", "rehearsing, energetic"),
          ("ali", "Yarın sabah sekizde açıyoruz. Dört yüz kutu.", "rehearsing, calm")],
         "static medium two-shot facing the phone",
         t=[T("konaklama", 1600, "Termal otel, 1 gece"), T("ulasim", 900, "Yakıt: Kırşehir-Yozgat")]),
   ],
   misafir={"ahi": ("KADİR USTA", "KADİR, a 68-year-old Turkish master craftsman, dignified, a white beard, a black wool coat, a traditional cap",
                    "elderly male voice, wise, slow Central Anatolian Turkish"),
            "ozan": ("OZAN", "MINSTREL, a 72-year-old Turkish man, thin, a lined face, a grey flat cap, a long dark coat, a bağlama in his hands",
                     "elderly male voice, soft and proud")},
   ay=AY, hava="kar", kiyafet=K, urun="Ahilik geleneği, bozlak, Kırşehir termal kaplıcaları; Ahi Evran Türbesi, Cacabey Medresesi",
   sponsor="Termal turizm ya da el sanatları alanında",
   kapak=("turbe", ["mert", "ali", "ahi"], "In a snowy courtyard, an old master raises three fingers while Mert and Ali listen closely, Ali writing "
          "in a worn notebook", "Karlı avluda üç parmağını kaldıran usta ve dinleyen Mert ile Ali."),
   yakinda=("cacabey", ["mert", "ali"], "Snowflakes drifting down through a round opening in an ancient stone dome onto two upturned faces in "
            "dim light", "Antik kubbenin açıklığından iki yüze düşen kar taneleri."),
   tiktok="Eline, beline, diline sahip ol 🤲 #JozhStudios",
   ig=("Kırşehir'de Kadir Usta ahiliğin üç öğüdünü anlattı: 'Eline, beline, diline sahip ol.' 🤲 Ali bunu defterin ilk sayfasına, KASA yazısının altına yazdı.\n\n"
       "Cacabey'de kubbeden kar yağdı, kahvehanede bozkırın sesini dinledik. Mert'in yorumu: 'Elim helal kazanç, belim sözüm, dilim önce sana sormak.' 🥹\n\n"
       "Yarın sabah sekizde Final Kutusu ön siparişi! Kasa: {KASA}"),
   tags=["#Kırşehir", "#AhiEvran", "#Ahilik"],
   son="Yarın sabah sekizde Final Kutusu ön siparişe açılıyor.",
   teaser="Üç öğüt, kubbeden yağan kar ve bozkırın sesi. Bölüm 77: Kırşehir. Pek yakında.")

# ======================================================================= 78 YOZGAT
EP(78, "Yozgat", "Dört Yüz Kutu",
   "Ön sipariş saati, Çamlık Milli Parkı, arabaşı çorbası ve tükenen 400 kutu.",
   "Yozgat'ta sabah sekizde Final Kutusu ön siparişe açılır; kutu başı 1.200 TL. İkisi bir kafede telefona bakarken ilk siparişler düşer ve "
   "400 kutu öğlene kadar tükenir. Türkiye'nin ilk milli parkı Çamlık'ta karlı çamların arasında yürürler. Akşam Yozgat'ın arabaşı "
   "çorbasını hamuruyla birlikte yemeyi öğrenirler: hamur soğuk, çorba sıcaktır. Gece Ali hesap yapar: son taksit artık güvencededir.",
   {"kafe": ("Yozgat'ta kafe", "a quiet café in Yozgat in the early morning: a wooden table with two tea glasses and a phone, steamed-up windows, "
             "snow outside"),
    "camlik": ("Çamlık Milli Parkı", "Yozgat Çamlık National Park in winter: tall black pines heavy with snow, a snowy path, quiet, soft light"),
    "arabasi": ("Arabaşı sofrası", "a family-style table in Yozgat: a pot of hot spicy arabaşı soup and a tray of cold set dough cut into squares, "
                "bowls, a warm room"),
    "otel": ("Otel odası", "a hotel room in Yozgat at night: the brown notebook, a calculator, a phone, snowy window")},
   [
       S("07:58 iç-gündüz", "kafe", ["mert", "ali"], "İki Dakika",
         "Saat 07:58. Ön sipariş sekizde açılacaktır. İkisi de telefona bakar; Mert'in dizi titrer.",
         "Mert and Ali sit side by side staring at a phone on the table; Mert's knee bounces nervously under the table; Ali puts his hand on Mert's "
         "knee to stop it without looking away from the screen.",
         [("mert", "İki dakika. Ya kimse almazsa?", "nervous"),
          ("ali", "Alırlar. Seksen bir ildir bizi izliyorlar.", "calm")],
         "static medium two-shot across the table", h="kar"),
       S("08:00 iç-gündüz", "kafe", ["mert", "ali"], "Sekiz",
         "Saat sekiz. Ön sipariş açılır ve ilk siparişler hemen düşer.",
         "The phone screen lights up repeatedly; Mert grabs Ali's arm; Ali starts counting aloud; Mert covers his mouth with both hands, eyes "
         "wide.",
         [("ali", "Bir, iki, on, elli... yüz!", "counting faster and faster"),
          ("mert", "Ali, daha bir dakika olmadı!", "shocked, joyful")],
         "slow push-in on the glowing phone and their faces"),
       S("12:00 öğle", "kafe", ["mert", "ali"], "Tükendi",
         "Öğlene kadar 400 kutunun hepsi ön siparişle tükenir. Kutu başı 1.200 lira.",
         "Ali turns the phone to Mert showing 'sold out' with no readable text, just a big icon; Mert stands up so fast his chair tips back; other "
         "customers far in the background look up; Mert sits back down sheepishly.",
         [("ali", "Dört yüz kutu tükendi. Dört yüz seksen bin lira.", "stunned"),
          ("mert", "Bu yolculuğun en büyük satışı!", "whisper-shouting")],
         "static medium two-shot at the table",
         t=U(400, "kutu", 1200, "satis", "Final Kutusu, ön sipariş ({adet} x {fiyat} TL)"),
         kurgu="Ekrandaki 'tükendi' yazısı kurguda eklenir; prompt'ta yazı yoktur."),
       S("14:30 ikindi", "camlik", ["mert", "ali"], "İlk Milli Park",
         "Türkiye'nin ilk milli parkı Çamlık'ta karlı çamların arasında yürürler.",
         "Mert and Ali walk along the snowy path among tall black pines; Mert shakes a low branch and snow falls on Ali; Ali scoops snow and "
         "throws a snowball back; both laugh.",
         [("ali", "Türkiye'nin ilk milli parkı burası.", "informative, then laughing"),
          ("mert", "İlk milli kartopu savaşı da burada!", "laughing")],
         "smooth tracking shot along the path", h="kar"),
       S("19:00 iç-gece", "arabasi", ["mert", "ali", "evsahibi"], "Arabaşı",
         "Arabaşı çorbasını hamuruyla yemeyi öğrenirler: soğuk hamuru kaşıkla alıp sıcak çorbaya batırırsın, çiğnemeden yutarsın.",
         "The host shows them how to scoop a square of cold set dough with a spoon and dip it into the hot spicy soup; Mert tries and chews, the "
         "host laughs; Ali swallows it in one go and nods proudly.",
         [("evsahibi", "Çiğneme! Hamuru çorbaya batır, yut.", "laughing"),
          ("mert", "Çiğnedim... kural mı vardı?", "confused, mouth full")],
         "static medium three-shot at the table",
         t=T("yemek", 800, "Arabaşı sofrası")),
       S("22:00 iç-gece", "otel", ["mert", "ali"], "Güvence",
         "Gece Ali hesap yapar: Final Kutusu'nun malları ödense bile son taksit güvencededir.",
         "Ali presses buttons on a calculator and writes in the notebook; he turns the page toward Mert; Mert reads it, then lies back on the bed "
         "with a deep sigh of relief.",
         [("ali", "Kutuların malını ödesek bile yüz elli bin hazır.", "relieved"),
          ("mert", "Sekiz yüz bin lira... gerçekten bitiyor.", "disbelief")],
         "static medium two-shot from the window",
         t=[T("konaklama", 1200, "Otel, 1 gece"), T("ulasim", 1200, "Yakıt: Yozgat-Sivas")]),
   ],
   misafir={"evsahibi": ("EV SAHİBİ", "HOST, a 60-year-old Turkish woman, round, a white headscarf, a red knitted vest, a ladle in her hand",
                         "elderly female voice, laughing, Yozgat Turkish")},
   ay=AY, hava="kar", kiyafet=K, urun="Arabaşı çorbası, Yozgat tandırı; Çamlık Milli Parkı (Türkiye'nin ilk milli parkı), Kerkenes",
   sponsor="Yöresel mutfak ya da doğa turizmi alanında",
   kapak=("camlik", ["mert", "ali"], "Mert and Ali in a joyful snowball fight among tall snow-laden black pines, snow bursting in the air, both "
          "laughing", "Karlı çamların arasında kartopu oynayan Mert ve Ali."),
   yakinda=("kafe", ["mert", "ali"], "Two faces lit by a glowing phone screen on a table in a dim café at dawn, steam on the windows, one hand "
            "gripping the other's arm", "Şafakta kafede parlayan telefon ekranına bakan iki yüz."),
   tiktok="400 kutu 4 saatte tükendi 📦❤️ Teşekkürler! #JozhStudios",
   ig=("Sabah sekizde Final Kutusu ön siparişe açıldı. Bir dakika dolmadan 100 sipariş! Öğlene kadar 400 kutunun hepsi tükendi. 📦❤️\n\n"
       "Her kutuda yolda tanıştığımız ustalardan yedi bölgenin tadı ve bir avuç Çankırı tuzu var.\n\n"
       "Çamlık'ta kartopu oynadık, arabaşının hamurunu çiğnememeyi öğrendik (Mert çiğnedi 😅). Kasa: {KASA}"),
   tags=["#Yozgat", "#Çamlık", "#FinalKutusu"],
   son="400 kutu tükendi. Son taksit güvencede.",
   teaser="Sekize iki kala, bir dakikada yüz sipariş ve karlı çamlar. Bölüm 78: Yozgat. Pek yakında.")

# ======================================================================= 79 SİVAS
EP(79, "Sivas", "Tipi",
   "Tipiye yakalanırlar; bir yol üstü lokantası, bir Kangal ve Gök Medrese'nin taş işçiliği.",
   "Sivas yolunda tipi bastırır; yol kapanır ve bir yol üstü lokantasında saatlerce beklerler. Lokantanın önünde sürüyü koruyan iri bir "
   "Kangal köpeği Mert'e yaklaşır; Mert önce korkar, sonra köpek başını dizine koyar. Yol açılınca Sivas'a girip Gök Medrese'nin turkuaz "
   "çinili minarelerini ve taş işçiliğini görürler. Akşam Sivas köftesi yerler. Ali, Kayseri'de pastırma pazarlığını kendisi yapacağını "
   "söyler: 'Bu sefer sert olacağım.'",
   {"yol": ("Tipide yol", "a highway near Sivas in a blizzard: blowing snow, near-zero visibility, the old white pickup truck crawling with its "
            "lights on, snow poles at the roadside"),
    "lokanta": ("Yol üstü lokantası", "a roadside truck-stop restaurant near Sivas during a blizzard: steamed windows, a big stove, truck "
                "drivers far in the background, soup bowls on tables"),
    "kapi": ("Lokanta önü", "the snowy front yard of the roadside restaurant: a big cream-colored Kangal shepherd dog with a black face and a "
             "spiked collar sitting in the snow, sheep behind a fence"),
    "medrese": ("Gök Medrese", "the Gök Medrese in Sivas: a 13th-century carved stone portal with two turquoise-tiled brick minarets, snow on "
                "the ground, soft winter light"),
    "kofteci": ("Sivas köftecisi", "a Sivas köfte restaurant: plates of grilled köfte with roasted tomatoes and peppers on lavaş, warm interior")},
   [
       S("08:30 sabah", "yol", ["mert", "ali"], "Tipi",
         "Sivas yolunda tipi bastırır. Görüş sıfıra iner; kamyonet adım adım ilerler.",
         "Inside the pickup Mert grips the steering wheel tightly, leaning forward to see through the blowing snow; Ali points at the orange "
         "snow poles at the roadside to guide him.",
         [("ali", "Sağdaki direkleri takip et. Yavaş.", "calm, focused"),
          ("mert", "Hiçbir şey görmüyorum Ali. Sadece beyaz.", "tense")],
         "static medium two-shot through the windshield from inside", h="kar"),
       S("10:00 iç-gündüz", "lokanta", ["mert", "ali"], "Yol Kapandı",
         "Yol kapanır. Bir yol üstü lokantasında beklerler; sıcak çorba ve sobanın sesi.",
         "Mert and Ali sit by the stove with bowls of hot soup, their jackets steaming on the chair backs; Ali checks his phone for the road status "
         "and shakes his head; Mert blows on his soup.",
         [("ali", "Yol akşama kadar kapalı.", "resigned"),
          ("mert", "O zaman çorba ikinci tur.", "smiling")],
         "static medium two-shot by the stove", h="kar",
         t=T("yemek", 600, "Yol üstü lokantasında çorba ve öğle yemeği")),
       S("12:00 öğle", "kapi", ["mert", "kangal"], "Kangal",
         "Lokantanın önünde sürüyü koruyan iri bir Kangal köpeği Mert'e yaklaşır. Mert önce donar, sonra köpek başını dizine koyar.",
         "Mert stands frozen in the snow as the huge Kangal dog walks slowly toward him; the dog sniffs his hand, then sits and rests its big head "
         "on Mert's knee; Mert slowly smiles and strokes its head.",
         [("mert", "Merhaba koca adam... sakin... ben dostum.", "whispering, nervous then warm")],
         "slow push-in at knee height", h="kar",
         kurgu="Köpek sakin ve dosttur; saldırı ya da tehlike gösterilmez."),
       S("15:30 ikindi", "medrese", ["mert", "ali"], "Gök Medrese",
         "Yol açılınca Sivas'a girerler. Gök Medrese'nin turkuaz çinili minarelerinin önündedirler.",
         "Mert and Ali stand in the snow in front of the carved stone portal flanked by two turquoise-tiled minarets; Ali traces the carved "
         "patterns in the air with his finger; Mert stares up.",
         [("ali", "Taş dantel gibi işlenmiş. Yedi yüz yıl önce.", "awed"),
          ("mert", "Ve hâlâ ayakta. Tipiye rağmen.", "impressed")],
         "slow crane-up from the portal to the minarets", h="kar"),
       S("19:00 iç-gece", "kofteci", ["mert", "ali"], "Sivas Köftesi",
         "Akşam Sivas köftesi yerler. Ali, Kayseri'de pazarlığı kendisinin yapacağını söyler.",
         "Mert wraps a grilled köfte with roasted tomato in lavaş and takes a big bite; Ali, across the table, makes a serious face and taps the "
         "table with his finger.",
         [("ali", "Kayseri'de pastırma pazarlığını ben yapacağım. Bu sefer sert olacağım.", "determined"),
          ("mert", "Kayserili esnafa karşı sert Ali... bunu izlerim.", "amused")],
         "static medium two-shot at the table",
         t=T("yemek", 800, "Sivas köftesi")),
       S("21:30 iç-gece", "kofteci", ["mert", "ali"], "Prova",
         "Ali pazarlık provası yapar; Mert Kayserili esnafı oynar. İkisi de gülmekten devam edemez.",
         "Mert crosses his arms and plays a tough shopkeeper with a fake stern frown; Ali tries to bargain with a serious face but both burst out "
         "laughing after two seconds.",
         [("mert", "Kilosu bin beş yüz, inmem!", "fake stern accent"),
          ("ali", "Bin iki yüz, son sözüm! ...Gülme Mert!", "trying to be tough, laughing")],
         "static medium two-shot",
         t=[T("konaklama", 1300, "Otel, 1 gece"), T("ulasim", 1300, "Yakıt: Sivas-Kayseri")]),
   ],
   misafir={"kangal": ("KANGAL KÖPEĞİ", "a huge calm cream-colored Kangal shepherd dog with a black face mask and a wide spiked protective collar, "
                       "gentle eyes", "no voice, only soft breathing")},
   ay=AY, hava="kar", kiyafet=K, urun="Sivas köftesi, Sivas halısı, Kangal köpeği; Gök Medrese, Divriği Ulu Camii (UNESCO)",
   sponsor="Yöresel mutfak, halı ya da kültür turizmi alanında",
   kapak=("kapi", ["mert", "kangal"], "In the falling snow a huge cream Kangal shepherd dog rests its big head on Mert's knee while Mert smiles and "
          "strokes it, sheep behind a fence", "Karda başını Mert'in dizine koyan dev Kangal köpeği."),
   yakinda=("yol", ["mert", "ali"], "Two faces behind a windshield in a white-out blizzard, only the orange glow of roadside snow poles visible "
            "ahead", "Tipide ön camın ardında iki yüz; önde sadece turuncu direkler."),
   tiktok="Tipide kaldık ve bir Kangal'la dost olduk 🐕❄️ #JozhStudios",
   ig=("Sivas yolunda tipi bastırdı; görüş sıfır, yol kapalı. ❄️ Bir yol üstü lokantasında çorbayla bekledik.\n\n"
       "Kapıda dev bir Kangal Mert'e yaklaştı... ve başını dizine koydu. 🐕🥹 Yol açılınca Gök Medrese'nin taş dantelini gördük.\n\n"
       "Ali'nin yeni hedefi: Kayseri'de pastırma pazarlığı. 'Bu sefer sert olacağım.' Kasa: {KASA}"),
   tags=["#Sivas", "#Kangal", "#GökMedrese"],
   son="Ali, Kayseri'de pastırma pazarlığını kendisi yapacak.",
   teaser="Tipi, bir yol üstü lokantası ve başını dize koyan bir dev. Bölüm 79: Sivas. Pek yakında.")

# ======================================================================= 80 KAYSERİ
EP(80, "Kayseri", "Pastırma Pazarlığı",
   "Kapalı Çarşı'da Ali'nin sert pazarlığı, mantı ve Erciyes'in karlı zirvesi.",
   "Kayseri'de sabah Kapalı Çarşı'nın taş kemerleri altında bir pastırmacıya girerler. Ali pazarlığı yapar; Kayserili usta bile şaşırır. "
   "Çemenin sırrını, pastırmanın Erciyes rüzgârında nasıl kuruduğunu dinlerler ve Ankara'daki yılbaşı sofrası ve Kapadokya'daki oteller için "
   "30 kilo pastırma alırlar. Öğlen yüzük kadar küçük Kayseri mantısını yerler. Akşam karlı Erciyes'e bakan bir tepede Mert, Ali'nin "
   "pazarlığını taklit eder.",
   {"carsi": ("Kayseri Kapalı Çarşı", "the covered bazaar of Kayseri: old stone arches and vaults, shops with strings of pastırma and sucuk "
              "hanging, wooden counters, warm light"),
    "pastirmaci": ("Pastırmacı", "a pastırma shop in Kayseri's bazaar: long slabs of pastırma coated in red çemen paste hanging from hooks, a "
                   "slicing machine, a marble counter"),
    "manti": ("Mantıcı", "a Kayseri mantı restaurant: bowls of tiny dumplings topped with yogurt, melted butter and red pepper, simple tables"),
    "erciyes": ("Erciyes manzarası", "a hilltop viewpoint near Kayseri at sunset facing the enormous snow-covered volcanic peak of Mount Erciyes "
                "glowing pink, the city below")},
   [
       S("09:30 iç-gündüz", "carsi", ["mert", "ali"], "Taş Kemerler",
         "Kapalı Çarşı'nın taş kemerleri altında yürürler. Ali derin bir nefes alır: pazarlık zamanı.",
         "Mert and Ali walk under the old stone arches of the bazaar past hanging strings of pastırma; Ali stops, adjusts his jacket collar, takes "
         "a deep breath; Mert pats his back like a coach.",
         [("mert", "Unutma: Kayserili esnaf pazarlığın ustası.", "coaching, amused"),
          ("ali", "Ben de seksen ilin öğrencisiyim.", "determined")],
         "slow tracking shot under the arches"),
       S("10:00 iç-gündüz", "pastirmaci", ["ali", "pastirmaci"], "Sert Ali",
         "Ali pastırmacı Halil Usta'yla pazarlık eder; hiç gülmeden, sakin ama sert.",
         "Halil names a price with a proud smile; Ali shakes his head calmly and names a lower price, holding eye contact without blinking; Halil "
         "raises his eyebrows, strokes his mustache and thinks.",
         [("pastirmaci", "Kilosu bin beş yüz. Çemeni benim elimden.", "proud, testing"),
          ("ali", "Otuz kilo alırım. Bin iki yüz elli. Peşin, şimdi.", "calm, firm")],
         "static medium two-shot across the counter, slow push-in"),
       S("10:10 iç-gündüz", "pastirmaci", ["mert", "ali", "pastirmaci"], "Usta Şaşırdı",
         "Halil Usta güler ve kabul eder: 'Kayseri'de bile böyle pazarlık az görülür.' Mert arkadan alkışlar.",
         "Halil bursts out laughing, slaps the counter and extends his hand; Ali shakes it with a small proud smile; behind him Mert claps silently "
         "with big gestures.",
         [("pastirmaci", "Bin iki yüz elli! Kayseri'de bile böyle pazarlık az görülür.", "laughing, impressed"),
          ("mert", "O benim ortağım usta!", "proud")],
         "static medium three-shot at the counter",
         t=U(30, "kg", 1250, "alis", "Kayseri pastırması ({adet} kg x {fiyat} TL)")),
       S("11:00 iç-gündüz", "pastirmaci", ["mert", "ali", "pastirmaci"], "Çemenin Sırrı",
         "Halil Usta pastırmanın tuzlanıp preslendiğini, çemenle kaplanıp Erciyes rüzgârında kuruduğunu anlatır.",
         "Halil lifts a long slab of pastırma coated in red çemen paste from its hook and slices a paper-thin piece on the machine, offering it to "
         "Mert; Mert tastes it and closes his eyes.",
         [("pastirmaci", "Tuz, pres, çemen ve Erciyes'in rüzgârı. Gerisi sabır.", "masterful"),
          ("mert", "Yine sabır! Bu yolculuk sabır ansiklopedisi oldu.", "laughing")],
         "slow push-in on the slicing machine"),
       S("13:30 iç-gündüz", "manti", ["mert", "ali"], "Yüzük Kadar Mantı",
         "Öğlen yüzük kadar küçük Kayseri mantısını yerler. Bir kaşığa kırk tane sığar.",
         "Mert scoops a spoonful of tiny dumplings and counts them with mock seriousness; Ali drizzles red pepper butter over his bowl and laughs.",
         [("mert", "Bir kaşıkta kırk mantı! Saydım.", "amazed"),
          ("ali", "Kayseri'de sabır mantıya bile işlemiş.", "smiling")],
         "static medium two-shot at the table",
         t=T("yemek", 900, "Kayseri mantısı")),
       S("18:00 gün batımı", "erciyes", ["mert", "ali"], "Erciyes'e Karşı",
         "Akşam karlı Erciyes'e bakan bir tepede Mert, Ali'nin pazarlığını taklit eder. Ali gülerken bir yandan da gurur duyar.",
         "Mert stands facing Ali on the hilltop and imitates his calm stern bargaining face and voice; Ali laughs and pushes him; the huge snowy "
         "peak glows pink behind them.",
         [("mert", "'Otuz kilo alırım. Bin iki yüz elli. Peşin, şimdi.' Efsane!", "imitating, laughing"),
          ("ali", "Seksen il önce ağzımı açamıyordum.", "proud, laughing")],
         "slow dolly-out revealing Mount Erciyes", h="kar",
         t=[T("konaklama", 1300, "Otel, 1 gece"), T("ulasim", 1000, "Yakıt: Kayseri-Nevşehir")]),
   ],
   misafir={"pastirmaci": ("HALİL USTA", "HALİL, a 63-year-old Turkish pastırma master, stout, a thick grey mustache, a white shop coat, a cap",
                           "elderly male voice, proud, Kayseri Turkish")},
   ay=AY, hava="kar", kiyafet=K, urun="Kayseri pastırması ve sucuğu, Kayseri mantısı; Kapalı Çarşı, Erciyes Dağı",
   sponsor="Pastırma, sucuk ya da Kayseri mutfağı alanında",
   kapak=("pastirmaci", ["ali", "pastirmaci", "mert"], "Ali shakes hands with a laughing pastırma master over a marble counter under hanging red "
          "çemen-coated pastırma, Mert clapping silently behind", "Pastırma ustasıyla el sıkışan Ali ve arkada alkışlayan Mert."),
   yakinda=("erciyes", ["mert", "ali"], "Two silhouettes on a hilltop facing an enormous snow-covered volcano glowing pink at dusk",
            "Alacakaranlıkta pembe parlayan dev karlı dağa bakan iki silüet."),
   tiktok="Ali, Kayserili ustayla pazarlık yaptı ve kazandı 😎 #JozhStudios",
   ig=("Kayseri Kapalı Çarşı'da Ali, Halil Usta'yla pazarlık yaptı: 'Otuz kilo alırım. Bin iki yüz elli. Peşin, şimdi.' 😎\n\n"
       "Usta güldü: 'Kayseri'de bile böyle pazarlık az görülür.' Pastırmanın Erciyes rüzgârında kuruduğunu öğrendik, bir kaşığa kırk mantı sığdı! 🥟\n\n"
       "Seksen il önce ağzını açamayan Ali... Kasa: {KASA}"),
   tags=["#Kayseri", "#Pastırma", "#KayseriMantısı"],
   son="Ali'nin pazarlığı Kayseri'de efsane oldu. Sırada Kapadokya.",
   teaser="Taş kemerler, sert bir pazarlık ve bir kaşıkta kırk mantı. Bölüm 80: Kayseri. Pek yakında.")

# ======================================================================= 81 NEVŞEHİR
EP(81, "Nevşehir", "Balonlar ve Battaniye",
   "Kapadokya'da gün doğumu, Mardin'den beri saklanan battaniye ve gelecek üzerine.",
   "Şafakta Kapadokya'nın peribacalarının üstünde yüzlerce balon yükselir; karlı vadiyi bir tepeden izlerler. Mardin'den beri sakladıkları "
   "son Siirt battaniyesini bir mağara otele satarlar; otel pastırmanın yarısını da kahvaltı için alır. Avanos'ta Kızılırmak kiliyle çömlek "
   "yapan bir ustanın tezgâhında Mert çamuru biçimlendirmeye çalışır. Akşam peribacalarının arasında, borç bittikten sonra ne yapacaklarını "
   "konuşurlar: '81 Şehir Kutusu' gerçek bir marka olacaktır.",
   {"tepe": ("Kapadokya tepesi", "a snowy hilltop above Göreme at sunrise: dozens of colorful hot air balloons rising over snow-dusted fairy "
             "chimneys and valleys, pink-orange sky"),
    "otel": ("Mağara otel", "the stone-carved lobby of a cave hotel in Göreme: arched rock walls, carpets, lanterns, a breakfast area, a stone "
             "bench"),
    "avanos": ("Avanos çömlek atölyesi", "a pottery workshop in Avanos: a kick wheel with wet red clay, shelves of red earthenware pots, a "
               "window to the Kızılırmak river"),
    "peri": ("Peribacaları arasında", "a path between tall fairy chimneys in Cappadocia at dusk, snow on the ground, warm lights from cave "
             "windows, the old white pickup truck parked nearby")},
   [
       S("06:40 şafak", "tepe", ["mert", "ali"], "Yüzlerce Balon",
         "Şafakta peribacalarının üstünde yüzlerce balon yükselir. Karlı tepede, montlarına sarılı izlerler.",
         "Mert and Ali stand wrapped in their jackets on the snowy hilltop as dozens of colorful balloons rise slowly over the fairy chimneys "
         "into the pink sky; Mert points at one; Ali just watches, smiling.",
         [("mert", "Ali... seksen birinci ilde gökyüzü bizi kutluyor.", "awed"),
          ("ali", "Henüz seksen bir değil. Sayıyorum, sabırlı ol.", "smiling")],
         "slow crane-up from their backs to the balloons", h="kar"),
       S("09:00 iç-gündüz", "otel", ["ali", "otelci"], "Mardin'den Beri",
         "Mardin'den beri sakladıkları son Siirt battaniyesini bir mağara otel alır; otel pastırmanın yarısını da kahvaltı için ister.",
         "Ali unfolds the soft white striped mohair blanket over a stone bench in the cave lobby; the hotel owner touches it and smiles; then she "
         "points at the pastırma box and nods.",
         [("otelci", "Taş odaya tiftik battaniyesi... Bir de pastırmayı kahvaltıya alırım.", "delighted"),
          ("ali", "Bu battaniye Mardin'den beri sizi bekliyordu.", "warm")],
         "slow push-in on the blanket",
         t=[U(1, "battaniye", 8000, "satis", "Siirt tiftik battaniyesi, mağara otele ({adet} x {fiyat} TL)"),
            U(15, "kg", 1900, "satis", "Kayseri pastırması, mağara otele (15 kg x 1.900 TL)")]),
       S("12:00 iç-gündüz", "avanos", ["mert", "comlekci"], "Kızılırmak Kili",
         "Avanos'ta çömlek ustası Kızılırmak kiliyle çalışır. Mert tezgâhta bir çömlek yapmaya çalışır; çömlek çöker.",
         "The potter kicks the wheel and shapes a tall red clay vase in seconds; Mert sits at the wheel, tries, and his clay pot collapses into a "
         "flat lump; the potter laughs and places his hands over Mert's to guide him.",
         [("comlekci", "Çamur acele sevmez. Ellerini yumuşat.", "patient"),
          ("mert", "Seksen ildir aynı dersi alıyorum usta!", "laughing")],
         "slow push-in on the spinning clay",
         t=T("yemek", 900, "Testi kebabı (2 kişi)")),
       S("14:00 iç-gündüz", "avanos", ["mert", "ali"], "Yamuk Çömlek",
         "Mert'in sonunda yaptığı küçük, yamuk çömleği usta fırına koyar. Ali onu Hatice'ye hediye etmeyi önerir.",
         "Mert holds up his small lopsided clay pot proudly; Ali tilts his head to match its angle and laughs; Mert places it gently on the "
         "shelf to dry.",
         [("ali", "Yamuk ama senin. Hatice Teyze'ye götür.", "warm, teasing"),
          ("mert", "Annem buna kayısı reçeli koyar.", "touched")],
         "static medium two-shot at the shelf"),
       S("18:00 akşam", "peri", ["mert", "ali"], "Borçtan Sonra",
         "Akşam peribacalarının arasında, borç bittikten sonra ne yapacaklarını konuşurlar.",
         "Mert and Ali walk slowly along the snowy path between tall fairy chimneys with warm lights glowing from cave windows; Mert stops and "
         "draws a box shape in the air; Ali nods and draws a logo-like circle on it.",
         [("mert", "Borç bitince 81 Şehir Kutusu gerçek bir marka olacak.", "dreamy, sure"),
          ("ali", "Her ustaya hakkını vererek. Sözleşmeyle.", "firm, smiling")],
         "slow tracking shot along the path", h="kar"),
       S("21:00 akşam", "peri", ["mert", "ali"], "Altı Durak",
         "Ali kalan durakları sayar: Niğde, Aksaray, Karaman, Konya, Eskişehir ve Ankara.",
         "Mert and Ali sit on the pickup's tailgate under the night sky between the fairy chimneys; Ali counts six on his fingers; Mert takes a "
         "deep breath of cold air.",
         [("ali", "Altı durak kaldı. Sonra Ankara.", "emotional"),
          ("mert", "Bitmesini istiyorum ama bitmesinden de korkuyorum.", "honest")],
         "static medium two-shot on the tailgate", h="kar",
         t=[T("konaklama", 1800, "Mağara otel, 1 gece"), T("ulasim", 800, "Yakıt: Nevşehir-Niğde")]),
   ],
   misafir={"otelci": ("OTEL SAHİBİ", "CAVE HOTEL OWNER, a 50-year-old Turkish woman, elegant, grey hair in a bun, a long knitted cardigan, a "
                       "silver necklace", "adult female voice, delighted"),
            "comlekci": ("ÇÖMLEK USTASI", "POTTER, a 66-year-old Turkish man, a long white mustache, a clay-stained apron, strong patient "
                         "hands", "elderly male voice, patient, Avanos Turkish")},
   ay=AY, hava="kar", kiyafet=K, urun="Avanos çömleği, testi kebabı, Kapadokya üzümü; peribacaları, balon turları (UNESCO)",
   sponsor="Mağara otel, çömlekçilik ya da Kapadokya turizmi alanında",
   kapak=("tepe", ["mert", "ali"], "Mert and Ali stand on a snowy hilltop at sunrise as dozens of colorful hot air balloons rise over snow-dusted "
          "fairy chimneys, the sky glowing pink", "Karlı tepede yüzlerce balonu izleyen Mert ve Ali."),
   yakinda=("avanos", ["mert"], "Wet red clay spinning on a potter's wheel collapsing in Mert's hands, warm window light from the river, an old "
            "master's hands reaching in", "Mert'in ellerinde çöken kırmızı çamur ve uzanan usta elleri."),
   tiktok="Kapadokya'da balonlar ve Mert'in yamuk çömleği 🎈🏺 #JozhStudios",
   ig=("Şafakta Kapadokya'nın karlı vadilerinin üstünde yüzlerce balon yükseldi. 🎈\n\n"
       "Mardin'den beri sakladığımız Siirt battaniyesi sonunda bir mağara otelde yuvasını buldu. Avanos'ta Mert'in çömleği çöktü, sonra yamuk bir tane yaptı: Hatice Teyze'ye! 🏺\n\n"
       "Borç bitince 81 Şehir Kutusu gerçek bir marka olacak. Kasa: {KASA}"),
   tags=["#Nevşehir", "#Kapadokya", "#Avanos"],
   son="Altı durak kaldı. Mert bitmesinden korkuyor.",
   teaser="Yüzlerce balon, Mardin'den beri saklanan bir battaniye ve yamuk bir çömlek. Bölüm 81: Nevşehir. Pek yakında.")

# ======================================================================= 82 NİĞDE
EP(82, "Niğde", "Aladağlar'ın Gölgesinde",
   "Gümüşler Manastırı'nın freskleri, taş depoda patates ve elma, pastırmanın kalanı.",
   "Niğde'de sabah kayalara oyulmuş Gümüşler Manastırı'nın bin yıllık fresklerini görürler. Niğde'nin patates ve elmasının kışın serin kalması "
   "için kullanılan taş depolardan birini gezer, bir üreticiden kışlık patates ve elmayı Ankara'daki aile sofrası için alırlar. Kalan 15 kilo "
   "pastırma bir şarküteriye satılır. Aladağlar'ın karlı sırtına bakarken Mert, Cemil Bey'e ne söyleyeceğini prova eder. Ali onu durdurur: "
   "'Kalbinden ne gelirse.'",
   {"gumusler": ("Gümüşler Manastırı", "the Gümüşler rock-cut monastery near Niğde: a courtyard carved into soft volcanic rock, a dim chapel "
                 "with well-preserved colorful medieval frescoes on the walls, cold light"),
    "depo": ("Taş depo", "a traditional stone storage cellar near Niğde carved into a hillside: cool dark interior, sacks of potatoes and crates "
             "of red apples, a wooden door"),
    "sarkuteri": ("Niğde şarküterisi", "a delicatessen in Niğde with a glass counter of cheeses and cured meats, a slicing machine"),
    "aladag": ("Aladağlar manzarası", "a roadside viewpoint near Niğde facing the jagged snow-covered Aladağlar mountain range at golden hour, "
               "the old white pickup truck parked")},
   [
       S("09:30 iç-gündüz", "gumusler", ["mert", "ali"], "Bin Yıllık Freskler",
         "Gümüşler Manastırı'nın kayaya oyulmuş şapelinde bin yıllık freskleri görürler.",
         "Mert and Ali step into the dim rock-cut chapel; Ali raises his phone flashlight carefully toward the colorful frescoes on the wall, then "
         "lowers it respectfully; Mert stands still, looking.",
         [("ali", "Bin yıl geçmiş ama renkler hâlâ duruyor.", "whisper, awed"),
          ("mert", "Kayaya oyulmuş, kalbe işlenmiş.", "quiet")],
         "slow push-in through the chapel entrance"),
       S("11:30 iç-gündüz", "depo", ["mert", "ali", "uretici"], "Taş Depo",
         "Niğde'nin patates ve elmasının kış boyunca saklandığı serin taş depolardan birini gezerler.",
         "The farmer pushes open the heavy wooden door of the stone cellar; cool air comes out; he picks a red apple from a crate and rubs it on "
         "his sleeve before handing it to Mert.",
         [("uretici", "Taş depo yazın serin, kışın ılık. Patates de elma da burada uyur.", "proud"),
          ("mert", "Kayısı için de böyle bir depo lazımmış Iğdır'da!", "laughing")],
         "static medium three-shot at the cellar door"),
       S("12:00 iç-gündüz", "depo", ["ali", "uretici"], "Aile Sofrası",
         "Ankara'daki yılbaşı aile sofrası için bir çuval patates ve bir kasa elma alırlar.",
         "The farmer ties a sack of potatoes and lifts a crate of apples onto the pickup bed; Ali pays him and the farmer adds two extra apples "
         "on top.",
         [("uretici", "Yılbaşı sofrasına Niğde'den. Elmanın ikisi benden.", "warm"),
          ("ali", "Babam Niğde patatesine bayılır.", "smiling")],
         "static medium two-shot by the pickup",
         t=T("diger_gider", 1500, "Yılbaşı aile sofrası için patates ve elma")),
       S("14:00 iç-gündüz", "sarkuteri", ["mert", "sarkuteri"], "Son Pastırma",
         "Bir şarküteri kalan 15 kilo Kayseri pastırmasını alır.",
         "The deli owner slices a thin piece of pastırma, tastes it and nods; Mert hands him the wrapped pastırma and receives the money.",
         [("sarkuteri", "Kayseri'nin pastırması komşuda biter. On beş kilo, bin dokuz yüzden.", "pleased"),
          ("mert", "Ali'nin pazarlığından aldık, size de kazandırsın.", "proud")],
         "static medium two-shot at the counter",
         t=[U(15, "kg", 1900, "satis", "Kayseri pastırması, Niğde'de şarküteriye ({adet} kg x {fiyat} TL)"), T("yemek", 800, "Öğle yemeği")]),
       S("17:00 gün batımı", "aladag", ["mert", "ali"], "Prova",
         "Aladağlar'a bakarken Mert, Cemil Bey'e ne söyleyeceğini prova eder. Ali onu durdurur.",
         "Mert stands facing the snowy mountains and rehearses with formal hand gestures, then stops and starts again; Ali walks up and gently "
         "lowers Mert's raised hand.",
         [("mert", "'Cemil Abi, sekiz yüz bin lira, seksen bir il...' Yok, olmadı.", "rehearsing, frustrated"),
          ("ali", "Prova yapma. Kalbinden ne gelirse.", "gentle")],
         "slow dolly-out revealing the mountain range", h="serin"),
       S("20:00 akşam", "aladag", ["mert", "ali"], "Kalbinden",
         "Mert prova yapmamaya karar verir. Ali, Aksaray'da Ihlara'yı görmek ister.",
         "Mert and Ali sit in the pickup cab watching the last light on the mountains; Mert nods slowly and puts his hand on his chest; Ali smiles "
         "and starts the engine.",
         [("mert", "Tamam. Kalbimden. Ama ağlarsam sen konuşursun.", "half-laughing"),
          ("ali", "Anlaştık. Yarın Ihlara.", "warm")],
         "static medium two-shot through the windshield",
         t=[T("konaklama", 1100, "Pansiyon, 1 gece"), T("ulasim", 700, "Yakıt: Niğde-Aksaray")]),
   ],
   misafir={"uretici": ("ÜRETİCİ", "FARMER, a 57-year-old Turkish man, sturdy, a grey stubble, a flat cap, a padded work jacket", "mature male voice, proud, Niğde Turkish"),
            "sarkuteri": ("ŞARKÜTERİCİ", "DELI OWNER, a 44-year-old Turkish man, a neat black beard, a white apron", "adult male voice, pleased")},
   ay=AY, hava="serin", kiyafet=K, urun="Niğde patatesi ve elması, taş depolar; Gümüşler Manastırı, Aladağlar",
   sponsor="Patates, elma ya da doğa turizmi alanında",
   kapak=("gumusler", ["mert", "ali"], "Mert and Ali stand in a dim rock-cut chapel lit by a soft beam, colorful thousand-year-old frescoes glowing "
          "on the walls around them", "Kayaya oyulmuş şapelde bin yıllık fresklere bakan Mert ve Ali."),
   yakinda=("aladag", ["mert"], "Mert standing alone facing a jagged snowy mountain range at dusk, one hand raised mid-speech, his long shadow "
            "behind him", "Karlı dağlara karşı elini kaldırmış konuşan yalnız bir figür."),
   tiktok="Cemil Abi'ye ne diyeceğimi prova ettim... olmadı 😅 #JozhStudios",
   ig=("Niğde'de Gümüşler Manastırı'nın bin yıllık fresklerinin renkleri hâlâ duruyor. 🎨\n\n"
       "Taş depoda patatesin ve elmanın kış uykusunu gördük, yılbaşı aile sofrası için aldık. Pastırmanın kalanı da gitti.\n\n"
       "Aladağlar'a karşı Mert, Cemil Abi'ye ne diyeceğini prova etti. Ali: 'Kalbinden ne gelirse.' Kasa: {KASA}"),
   tags=["#Niğde", "#GümüşlerManastırı", "#Aladağlar"],
   son="Mert prova yapmayacak: 'Kalbimden.'",
   teaser="Bin yıllık renkler, taş depolar ve yapılamayan bir prova. Bölüm 82: Niğde. Pek yakında.")

# ======================================================================= 83 AKSARAY
EP(83, "Aksaray", "Ihlara ve Kervansaray",
   "Ihlara Vadisi'nde karlı yürüyüş, Sultanhanı Kervansarayı'nda bir gece ve kervanların yolu.",
   "Aksaray'da sabah Ihlara Vadisi'nin karlı kanyonunda Melendiz Çayı boyunca yürürler; kayalara oyulmuş kiliseler başlarının üstündedir. "
   "Öğlen vadi kıyısında alabalık yerler. Akşamüstü İpek Yolu'nun en büyük Selçuklu kervansaraylarından Sultanhanı'nın kapısından girerler. "
   "Kervansarayın avlusunda Mert, yolculuğun kendi kervanları olduğunu söyler. Gece kervansarayın yanındaki pansiyonda Ali, Final "
   "Kutusu'nun malları için üreticilere ödeme planını son kez kontrol eder.",
   {"ihlara": ("Ihlara Vadisi", "the snowy Ihlara Valley canyon near Aksaray: steep rock walls with cave church openings, a stream (Melendiz) "
               "running along the bottom, bare poplars, a snowy path, wooden bridges"),
    "lokanta": ("Vadide lokanta", "a small riverside restaurant at the bottom of Ihlara valley: wooden platforms over the stream, grilled trout on "
                "plates, a warm stove"),
    "sultanhani": ("Sultanhanı Kervansarayı", "the Sultanhanı caravanserai near Aksaray: a monumental carved Seljuk stone portal, a large open "
                   "courtyard with a small raised mosque in the center, snowy ground, the vast steppe around"),
    "pansiyon": ("Pansiyon", "a guesthouse room near Sultanhanı at night: a wood stove, the brown notebook open with a payment list, two beds")},
   [
       S("09:00 sabah", "ihlara", ["mert", "ali"], "Karlı Kanyon",
         "Ihlara Vadisi'nin karlı kanyonunda Melendiz Çayı boyunca yürürler. Başlarının üstünde kayalara oyulmuş kiliseler.",
         "Mert and Ali walk along the snowy path at the bottom of the canyon beside the stream; Ali points up at a cave church opening high in the "
         "rock wall; Mert cranes his neck and slips slightly on the snow, laughing.",
         [("ali", "Yüzlerce yıl önce bu kayalara kilise oymuşlar.", "awed"),
          ("mert", "Ben karda yürüyemiyorum, onlar kayaya kilise oymuş.", "laughing")],
         "slow tracking shot along the stream", h="kar"),
       S("12:30 iç-gündüz", "lokanta", ["mert", "ali"], "Alabalık",
         "Vadide derenin üstündeki ahşap platformda alabalık yerler. Soba yanmaktadır.",
         "Mert and Ali sit on a wooden platform over the stream with grilled trout and bread; Mert warms his hands near the stove between bites; "
         "Ali squeezes lemon on the fish.",
         [("mert", "Dere sesi, soba, balık... Mutluluk bu galiba.", "content"),
          ("ali", "Bir de kasa sayacı yeşilse.", "smiling")],
         "static medium two-shot on the platform",
         t=T("yemek", 900, "Alabalık (2 kişi)")),
       S("16:30 ikindi", "sultanhani", ["mert", "ali"], "Kervanların Kapısı",
         "Sultanhanı Kervansarayı'nın oymalı taş kapısından girerler. Ali, kervanların burada konakladığını anlatır.",
         "Mert and Ali walk through the monumental carved stone portal into the snowy courtyard; Mert runs his fingers over the deep stone "
         "carvings; Ali looks around at the arched halls.",
         [("ali", "İpek Yolu'nun kervanları burada konaklarmış. Mal, hayvan, tüccar.", "fascinated"),
          ("mert", "Biz de bir kervanız. İki kişilik, bir kamyonetlik.", "smiling")],
         "slow dolly-in through the portal", h="kar"),
       S("17:30 gün batımı", "sultanhani", ["mert", "ali"], "Kervanın Sonu",
         "Avluda gün batarken Mert yolculuğun kendi kervanları olduğunu söyler. Ali deftere 'kervan' kelimesini yazar.",
         "Mert and Ali sit on the steps of the small central mosque in the courtyard as the sunset turns the stone walls orange; Ali writes a "
         "single word in the notebook and shows it to Mert, who smiles.",
         [("mert", "Seksen bir ilin kervanı. Kayısıdan leblebiye.", "moved"),
          ("ali", "Yazdım: 'Kervan.' Markanın bir sloganı olsun.", "inspired")],
         "slow crane-up revealing the courtyard and the steppe", h="kar"),
       S("21:00 iç-gece", "pansiyon", ["mert", "ali"], "Ödeme Planı",
         "Gece Ali, Final Kutusu'nun malları için üreticilere yapılacak ödemelerin planını son kez kontrol eder: hepsi Konya'da, teslimde.",
         "Ali reads a list of names and amounts in the notebook by the light of the wood stove; Mert sits across with a cup of tea and checks each "
         "one against messages on his phone.",
         [("ali", "Ramazan Amca, Antep, Ayten Hanım, Halime Teyze, Edirne, Konya. Hepsi teslimde.", "precise"),
          ("mert", "Hepsi faturalı, hepsi yazılı. Kural iki.", "proud")],
         "static medium two-shot by the stove"),
       S("22:30 iç-gece", "pansiyon", ["mert", "ali"], "Karaman Yolu",
         "Yatmadan önce Mert yarınki durağı sorar: Karaman, Türkçe'nin başkenti. Ali gülümser.",
         "Mert lies under a thick blanket and asks something toward the ceiling; Ali, turning off the lamp, answers in the dark with a smile in "
         "his voice.",
         [("mert", "Yarın Karaman. Ne var orada?", "sleepy"),
          ("ali", "Türkçe'nin başkenti. Ve mağarada olgunlaşan bir peynir.", "smiling")],
         "static medium two-shot, the lamp goes off",
         t=[T("konaklama", 1100, "Pansiyon, 1 gece"), T("ulasim", 1000, "Yakıt: Aksaray-Karaman")]),
   ],
   ay=AY, hava="kar", kiyafet=K, urun="Aksaray halısı, alabalık; Ihlara Vadisi, Sultanhanı Kervansarayı, Hasan Dağı",
   sponsor="Kervansaray turizmi, alabalık ya da halıcılık alanında",
   kapak=("sultanhani", ["mert", "ali"], "Mert and Ali sit on stone steps in the snowy courtyard of a monumental Seljuk caravanserai at sunset, the "
          "carved walls glowing orange", "Gün batımında kervansarayın karlı avlusunda oturan Mert ve Ali."),
   yakinda=("ihlara", ["mert", "ali"], "Two tiny figures walking along a snowy stream at the bottom of a deep canyon, dark cave openings in the "
            "towering rock walls above", "Derin kanyonun dibinde karlı derenin yanında yürüyen iki küçük figür."),
   tiktok="İpek Yolu'nun kervansarayında bir kervan: biz 🐫 #JozhStudios",
   ig=("Ihlara Vadisi'nin karlı kanyonunda yürüdük, kayalara oyulmuş kiliselerin altından geçtik. ❄️\n\n"
       "Sultanhanı Kervansarayı'nda kervanların konakladığı avluda gün battı. Mert: 'Biz de bir kervanız.' Ali deftere yazdı: 'Kervan.' 🐫\n\n"
       "Final Kutusu'nun bütün ödemeleri teslimde, hepsi yazılı. Kasa: {KASA}"),
   tags=["#Aksaray", "#Ihlara", "#Sultanhanı"],
   son="Yarın Karaman: Türkçe'nin başkenti ve mağara peyniri.",
   teaser="Karlı bir kanyon, bir kervansaray ve iki kişilik bir kervan. Bölüm 83: Aksaray. Pek yakında.")

# ======================================================================= 84 KARAMAN
EP(84, "Karaman", "Türkçe'nin Başkenti",
   "Karamanoğlu Mehmet Bey'in fermanı, mağarada olgunlaşan Divle peyniri ve bir mektup.",
   "Karaman'da sabah, 1277'de Türkçe'yi divanın dili ilan eden Karamanoğlu Mehmet Bey'in fermanının anıldığı yerde dururlar. Ali, yolculuk "
   "boyunca öğrendikleri en güzel yerel kelimeleri sayar. Divle'de obruk mağarasında olgunlaşan Divle Obruk peynirini görür, Konya ve "
   "Ankara için 40 kilo alırlar. Öğlen Karaman'ın yöresel yemeklerini yerler. Akşam Mert, Cemil Bey'e konuşmak yerine bir mektup yazmaya "
   "karar verir: Türkçe'nin başkentinde.",
   {"meydan": ("Karaman, ferman anıtı çevresi", "a square in Karaman with a monument commemorating the 1277 decree on the Turkish language, "
               "old stone buildings, snow on the ground, a few trees"),
    "obruk": ("Divle Obruk mağarası", "inside the Divle sinkhole cave near Karaman where cheese ripens: cool rock walls, goatskin and cloth cheese "
              "sacks resting on stone shelves, a narrow stairway, dim light"),
    "lokanta": ("Karaman lokantası", "a simple restaurant in Karaman with tables, a stove and plates of local dishes"),
    "oda": ("Pansiyon odası", "a guesthouse room in Karaman at night: a small desk with a lamp, a sheet of paper and a pen, the brown notebook")},
   [
       S("09:30 sabah", "meydan", ["mert", "ali"], "Ferman",
         "1277'de Türkçe'yi divanın dili ilan eden fermanın anıldığı yerdedirler. Ali fermanın sözünü okur.",
         "Mert and Ali stand in the snowy square in front of the monument; Ali reads from his phone in a solemn voice; Mert listens with his hands "
         "in his jacket pockets, nodding.",
         [("ali", "'Bugünden sonra divanda, dergâhta, bargâhta Türkçe'den başka dil konuşulmayacak.'", "solemn, reading"),
          ("mert", "Biz de seksen bir ilde Türkçe'nin seksen bir hâlini duyduk.", "smiling")],
         "slow push-in toward the monument", h="kar"),
       S("10:30 sabah", "meydan", ["mert", "ali"], "En Güzel Kelimeler",
         "Ali yolculukta öğrendikleri en güzel yerel kelimeleri sayar. Mert her birine bir şehir söyler.",
         "Ali counts on his fingers while saying words; Mert answers each with a city name and a grin; they walk slowly across the snowy square.",
         [("ali", "Harput'ta 'buyur', Van'da 'kahvaltı töreni', Rize'de 'feretiko'...", "playful"),
          ("mert", "Mardin'de 'turistler yanlış yere gider'!", "laughing")],
         "smooth tracking shot alongside them", h="kar"),
       S("13:00 iç-gündüz", "obruk", ["mert", "ali", "peynirci"], "Mağaranın Peyniri",
         "Divle'de obruk mağarasında olgunlaşan Divle peynirini görürler. Peynirci peyniri mağaranın serinliğinde aylarca beklettiklerini anlatır.",
         "The cheesemaker lifts a cloth-wrapped cheese sack from a stone shelf deep in the cave and cuts it open, revealing crumbly white cheese "
         "with blue-green veins; Mert tastes it and his eyes widen.",
         [("peynirci", "Obruğun serinliğinde aylarca uyur. Küfü de doğal.", "proud"),
          ("mert", "Erzincan'ın tulumu deride uyuyordu, bu mağarada!", "amazed")],
         "slow push-in in the dim cave"),
       S("14:00 iç-gündüz", "obruk", ["ali", "peynirci"], "Kırk Kilo",
         "Konya ve Ankara için 40 kilo Divle Obruk peyniri alırlar.",
         "The cheesemaker carries cheese sacks up the narrow stairway and loads them into a box; Ali counts money and writes in the notebook at "
         "the cave entrance.",
         [("peynirci", "Kilosu altı yüz elli. Sofranızın başköşesine.", "warm"),
          ("ali", "Kırk kilo. Yarısı Konya'ya, yarısı yılbaşı sofrasına.", "planning")],
         "static medium two-shot at the cave entrance",
         t=[U(40, "kg", 650, "alis", "Divle Obruk peyniri ({adet} kg x {fiyat} TL)"), T("yemek", 800, "Öğle yemeği")]),
       S("19:00 iç-gece", "oda", ["mert", "ali"], "Bir Mektup",
         "Akşam Mert, Cemil Bey'e konuşmak yerine bir mektup yazmaya karar verir. Ali ona boş bir kâğıt uzatır.",
         "Mert sits at the small desk staring at a blank sheet of paper; Ali places a pen next to it and steps back; Mert picks up the pen, "
         "hesitates, then writes the first line.",
         [("mert", "Konuşursam ağlarım. Yazayım. Türkçe'nin başkentinde.", "emotional"),
          ("ali", "Kâğıda yazılan söz unutulmaz. Sen öğrettin bunu.", "warm")],
         "slow push-in to the paper and Mert's hand"),
       S("22:00 iç-gece", "oda", ["mert", "ali"], "İlk Satır",
         "Mert ilk satırı Ali'ye okur. Ali başka bir şey söylemez, sadece başını sallar.",
         "Mert holds up the sheet and reads the first line aloud in a soft voice; Ali, sitting on the bed, nods slowly with wet eyes; Mert folds "
         "the paper carefully into the brown notebook.",
         [("mert", "'Cemil Abi, borcumuzu ödedik ama size bir teşekkür borcumuz kaldı.'", "soft, reading"),
          ("ali", "Gerisini Ankara'da oku.", "moved")],
         "static medium two-shot",
         t=[T("konaklama", 1100, "Pansiyon, 1 gece"), T("ulasim", 900, "Yakıt: Karaman-Konya")]),
   ],
   misafir={"peynirci": ("PEYNİRCİ", "CHEESEMAKER, a 58-year-old Turkish man, lean, a grey beard, a woolen cap, a padded vest, a lantern",
                         "mature male voice, proud, Karaman Turkish")},
   ay=AY, hava="kar", kiyafet=K, urun="Divle Obruk peyniri, Karaman bamyası; Türkçe'nin başkenti (1277 fermanı), Binbir Kilise",
   sponsor="Obruk peyniri ya da kültür turizmi alanında",
   kapak=("obruk", ["mert", "ali", "peynirci"], "Deep in a dim rock cave, a cheesemaker cuts open a cloth cheese sack revealing white cheese as Mert "
          "tastes it with wide eyes and Ali holds a lantern", "Loş mağarada peyniri tadan Mert ve fener tutan Ali."),
   yakinda=("oda", ["mert"], "A single sheet of paper under a warm desk lamp, a hand writing the first line, the rest of the room in darkness",
            "Masa lambası altında bir kâğıt ve ilk satırı yazan bir el."),
   tiktok="Türkçe'nin başkentinde Cemil Abi'ye bir mektup ✉️ #JozhStudios",
   ig=("Karaman'da, 1277'de Türkçe'yi divanın dili ilan eden fermanın anıldığı yerdeydik. 📜\n\n"
       "Divle'de mağarada aylarca uyuyan Divle Obruk peynirini tattık (Erzincan'ın tulumu deride, bu mağarada uyuyor!). 🧀\n\n"
       "Mert, Cemil Abi'ye konuşmak yerine bir mektup yazdı: 'Borcumuzu ödedik ama size bir teşekkür borcumuz kaldı.' ✉️ Kasa: {KASA}"),
   tags=["#Karaman", "#Türkçe", "#DivlePeyniri"],
   son="Mert'in mektubu yazıldı. Gerisi Ankara'da okunacak.",
   teaser="Bir ferman, mağarada uyuyan peynir ve bir mektubun ilk satırı. Bölüm 84: Karaman. Pek yakında.")

# ======================================================================= 85 KONYA
EP(85, "Konya", "Yedi Bölge, Bir Kutu",
   "Bütün üreticilerin malları gelir; Mevlana şekeri, 400 Final Kutusu ve son taksitin parası.",
   "Konya'da kiralık bir depoda yolculuğun yedi bölgesinden mallar gelir: Ramazan Amca'nın kayısısı, Antep'in fıstığı, Ayten Hanım'ın gül "
   "reçeli, Halime Teyze'nin inciri, Edirne'nin badem ezmesi. Hepsine teslimde ödeme yapılır. Bir şekerciden Mevlana şekeri alırlar. 400 Final "
   "Kutusu bütün gün hazırlanıp kargoya verilir. Divle peynirinin yarısı bir lokantaya satılır. Akşam Mevlana Müzesi'nin önünde Ali kasayı "
   "açar: son taksitin parası kenardadır.",
   {"depo": ("Kiralık depo", "a large rented storage room in Konya: stacks of cardboard parcels from all over Turkey, long tables with 400 kraft "
             "gift boxes, bags of apricots, pistachios, figs, jars of rose jam, almond paste, roasted chickpeas, Mevlana candy and small salt bags"),
    "sekerci": ("Mevlana şekercisi", "a traditional candy shop in Konya: big glass jars of white Mevlana candy (hard sugar drops), copper "
                "cauldrons, a marble counter"),
    "lokanta": ("Etli ekmek lokantası", "a Konya etli ekmek restaurant: very long thin flatbreads with minced meat coming out of a wood-fired oven, "
                "simple tables"),
    "mevlana": ("Mevlana Müzesi önü", "the square in front of the Mevlana Museum in Konya at dusk: the turquoise-tiled conical dome glowing, "
                "snow on the ground, a few lamps")},
   [
       S("08:30 iç-gündüz", "depo", ["mert", "ali"], "Yedi Bölgeden Koliler",
         "Depoya yolculuğun yedi bölgesinden koliler gelir. Her koliyi açtıklarında bir ustanın yüzünü hatırlarlar.",
         "Mert opens a parcel and lifts out a bag of golden dried apricots, smelling it with closed eyes; Ali opens another and holds up a jar of "
         "rose jam; parcels from all over the country are stacked around them.",
         [("mert", "Ramazan Amca'nın kayısısı! Malatya kokuyor.", "emotional"),
          ("ali", "Ayten Hanım'ın gülü. Isparta da burada.", "smiling")],
         "slow tracking shot along the stacked parcels",
         t=[U(100, "kg", 240, "alis", "Malatya kayısısı, Ramazan Amca ({adet} kg x {fiyat} TL)"),
            U(50, "kg", 900, "alis", "Antep fıstığı, Gaziantep'teki üretici (50 kg x 900 TL)"),
            U(400, "kavanoz", 90, "alis", "Isparta gül reçeli, Ayten Hanım (400 x 90 TL)"),
            U(100, "kg", 230, "alis", "Aydın kuru inciri, Halime Teyze (100 kg x 230 TL)"),
            U(40, "kg", 700, "alis", "Edirne badem ezmesi (40 kg x 700 TL)")],
         kurgu="Her ödeme teslimde, faturalı yapılmıştır. Üreticiler yolculukta tanışılan kurgusal karakterlerdir."),
       S("10:00 iç-gündüz", "sekerci", ["mert", "ali", "sekerci"], "Mevlana Şekeri",
         "Bir şekerciden İç Anadolu'nun payı olarak Mevlana şekeri alırlar.",
         "The candy maker scoops small white sugar drops from a big glass jar into a bag and hands one to each of them; Mert lets it melt on his "
         "tongue with a peaceful expression.",
         [("sekerci", "Mevlana şekeri sade ve beyazdır. Gönül gibi.", "gentle"),
          ("ali", "Kırk kilo. Yedinci bölgenin tadı.", "decisive")],
         "static medium three-shot at the counter",
         t=U(40, "kg", 300, "alis", "Konya Mevlana şekeri ({adet} kg x {fiyat} TL)")),
       S("12:00 iç-gündüz", "depo", ["mert", "ali"], "Dört Yüz Kutu",
         "Bütün gün 400 Final Kutusu hazırlanır: yedi bölgenin ürünü ve bir paket Çankırı tuzu.",
         "Mert and Ali work along the long tables placing apricots, pistachios, rose jam, figs, almond paste, leblebi, Mevlana candy and a small "
         "salt bag into each box; Ali closes each lid and stacks it.",
         [("ali", "Kayısı, fıstık, gül, incir, badem, leblebi, şeker, tuz. Kapak.", "rhythmic"),
          ("mert", "Seksen bir il, her kutuda.", "emotional, working")],
         "slow dolly along the tables",
         t=[U(400, "kutu", 70, "diger_gider", "Final Kutusu ambalajı ({adet} x {fiyat} TL)"), T("diger_gider", 2000, "Depo kirası, 1 gün")]),
       S("14:00 iç-gündüz", "lokanta", ["mert", "ali", "lokantaci"], "Etli Ekmek ve Peynir",
         "Öğlen etli ekmek yerler. Lokantacı Divle peynirinin yarısını alır.",
         "A very long thin etli ekmek slides out of the oven onto their table; the restaurant owner tastes a piece of Divle cheese Ali offers and "
         "nods, taking the box.",
         [("lokantaci", "Divle peyniri mi? Yirmi kilo alırım, dokuz yüz elliden.", "pleased"),
          ("mert", "Etli ekmek bir metre, peynir mağaradan. Konya güzel.", "happy")],
         "static medium three-shot at the table",
         t=[U(20, "kg", 950, "satis", "Divle Obruk peyniri, Konya'da lokantaya ({adet} kg x {fiyat} TL)"), T("yemek", 900, "Etli ekmek")]),
       S("17:00 ikindi", "depo", ["mert", "ali"], "Kargo",
         "Akşamüstü 400 kutu kargoya verilir. Mert son kutunun kapağını kapatır.",
         "Mert closes the last box and holds it up high like a trophy before placing it on top of a tall stack by the open door; Ali signs a cargo "
         "paper on a clipboard held by an unseen hand.",
         [("mert", "Dört yüzüncü kutu! Seksen bir ilin son kutusu!", "triumphant"),
          ("ali", "Teslim tutanağı imzalı. Yarın Türkiye'nin her yerinde.", "proud")],
         "static wide shot at the depot door",
         t=U(400, "kutu", 40, "diger_gider", "Kargo, 400 Final Kutusu ({adet} x {fiyat} TL)")),
       S("19:30 akşam", "mevlana", ["mert", "ali"], "Son Taksit Kenarda",
         "Mevlana Müzesi'nin turkuaz kubbesinin önünde Ali kasayı açar: son taksitin parası kenardadır.",
         "Mert and Ali stand in the snowy square in front of the glowing turquoise dome; Ali opens the brown notebook and shows Mert a line "
         "circled twice; Mert reads it and slowly exhales a cloud of breath.",
         [("ali", "Yüz elli bin kenarda. Dokunulmayacak.", "calm, proud"),
          ("mert", "Gel, ne olursan ol, yine gel... Biz de geldik.", "moved, quiet")],
         "slow crane-up from them to the turquoise dome", h="kar",
         t=[T("konaklama", 1300, "Otel, 1 gece"), T("ulasim", 1500, "Yakıt: Konya-Eskişehir")]),
   ],
   misafir={"sekerci": ("ŞEKERCİ", "CANDY MAKER, a 61-year-old Turkish man, slim, a white beard, a white cap and apron", "elderly male voice, gentle"),
            "lokantaci": ("LOKANTACI", "RESTAURANT OWNER, a 50-year-old Turkish man, heavy-set, a black mustache, an apron", "adult male voice, pleased")},
   ay=AY, hava="kar", kiyafet=K, urun="Etli ekmek, Mevlana şekeri, tirit; Mevlana Müzesi, Alaeddin Tepesi",
   sponsor="Etli ekmek, şekercilik ya da kültür turizmi alanında",
   kapak=("depo", ["mert", "ali"], "Mert holds up a single kraft gift box like a trophy in front of a towering stack of boxes and parcels from all "
          "over Turkey, Ali laughing beside him", "Kutu kulesinin önünde son kutuyu kupa gibi kaldıran Mert."),
   yakinda=("mevlana", ["mert", "ali"], "Two silhouettes in a snowy square in front of a glowing turquoise conical dome at dusk, breath clouds "
            "in the cold air", "Karlı meydanda parlayan turkuaz kubbenin önünde iki silüet."),
   tiktok="Yedi bölge, 400 kutu, bir gün 📦🇹🇷 #FinalKutusu #JozhStudios",
   ig=("Konya'da depoya Türkiye'nin dört bir yanından koliler geldi: Ramazan Amca'nın kayısısı, Antep fıstığı, Ayten Hanım'ın gül reçeli, Halime Teyze'nin inciri, Edirne'nin badem ezmesi. 🥹\n\n"
       "Mevlana şekeri ve Çankırı tuzuyla 400 Final Kutusu bir günde hazırlandı ve yola çıktı! 📦\n\n"
       "Mevlana'nın kubbesinin önünde: son taksitin 150.000 TL'si kenarda. Kasa: {KASA}"),
   tags=["#Konya", "#Mevlana", "#FinalKutusu"],
   son="Son taksitin parası kenarda. Sırada Eskişehir ve Ankara.",
   teaser="Yedi bölgeden koliler, dört yüz kutu ve kenara konan son taksit. Bölüm 85: Konya. Pek yakında.")

# ======================================================================= 86 ESKİŞEHİR
EP(86, "Eskişehir", "Lületaşı",
   "Odunpazarı'nın renkli evleri, lületaşı ustası, Cemil Bey için bir hediye ve çibörek.",
   "Eskişehir'de sabah Odunpazarı'nın renkli ahşap evlerinin arasında yürürler. Kalan Divle peyniri bir şarküteriye satılır. Bir lületaşı "
   "ustasının atölyesinde bu yumuşak, beyaz taşın ancak Eskişehir'de çıktığını ve oyulduğunu öğrenirler; Cemil Bey için el oyması küçük bir "
   "lületaşı tespih alırlar. Öğlen çibörek yerler. Porsuk Çayı kıyısında yürürken Hatice ve Hasan'ın otobüsü Ankara'ya doğru yola çıkmıştır. "
   "Gece son geceyi kamyonetin kasasında, battaniyelere sarılı geçirirler.",
   {"odunpazari": ("Odunpazarı evleri", "the colorful restored Ottoman wooden houses of Odunpazarı in Eskişehir: bay windows painted in pastel "
                   "colors, cobbled lanes, snow on the roofs"),
    "sarkuteri": ("Eskişehir şarküterisi", "a delicatessen in Eskişehir with a glass counter and shelves of jars"),
    "lule": ("Lületaşı atölyesi", "a meerschaum carving workshop in Eskişehir: blocks of soft white meerschaum stone, carving knives, finished "
             "pipes and prayer beads in a glass case, a warm lamp"),
    "porsuk": ("Porsuk Çayı kıyısı", "the Porsuk river walk in Eskişehir at dusk: a calm river with small bridges, a tram passing far behind, "
               "lamps, snow on the banks"),
    "kasa": ("Kamyonet kasası", "the open bed of the old white pickup truck parked by a quiet park at night, two people wrapped in thick blankets "
             "lying on it looking at the stars, cold breath")},
   [
       S("09:00 sabah", "odunpazari", ["mert", "ali"], "Renkli Evler",
         "Odunpazarı'nın renkli ahşap evlerinin arasında karlı sokaklarda yürürler.",
         "Mert and Ali walk up a cobbled lane between pastel-colored wooden houses with snow on their roofs; Mert stops in front of a pink house "
         "and pretends to knock; Ali laughs.",
         [("mert", "Şu pembe ev bizim olsa, dükkânı altına açarız.", "dreamy"),
          ("ali", "Önce borç. Yarın akşam.", "smiling")],
         "slow tracking shot up the lane", h="kar"),
       S("10:30 iç-gündüz", "sarkuteri", ["ali", "sarkuteri"], "Son Peynir",
         "Kalan 20 kilo Divle peyniri bir şarküteriye satılır. Ali yılbaşı sofrası için bir parçasını ayırır.",
         "The deli owner takes the cheese and nods; Ali cuts a small piece off with a knife, wraps it in paper and slips it into his jacket pocket "
         "with a wink.",
         [("sarkuteri", "Divle peyniri! Yirmi kilo, dokuz yüz elliden.", "pleased"),
          ("ali", "Bir parçası yılbaşı sofrasına. Kalanı sizin.", "warm")],
         "static medium two-shot at the counter",
         t=U(20, "kg", 950, "satis", "Divle Obruk peyniri, Eskişehir'de şarküteriye ({adet} kg x {fiyat} TL)")),
       S("12:00 iç-gündüz", "lule", ["mert", "ali", "luleci"], "Beyaz Altın",
         "Lületaşı ustası Şükrü Usta, yumuşak beyaz taşın Eskişehir'den çıktığını ve el oymasıyla işlendiğini gösterir.",
         "Şükrü carves a tiny bead from a soft white block with a small knife, white dust falling; he holds up a finished prayer bead string that "
         "glows creamy under the lamp; Mert and Ali lean in.",
         [("luleci", "Lületaşı ıslakken yumuşaktır, kuruyunca sertleşir. Tıpkı insan gibi.", "wise"),
          ("mert", "Bunu Cemil Abi'ye alalım Ali. Onun için.", "emotional")],
         "slow push-in on the carving"),
       S("12:30 iç-gündüz", "lule", ["ali", "luleci"], "Hediye",
         "Cemil Bey için el oyması bir lületaşı tespih alırlar. Usta kutusuna bir not koymalarını önerir.",
         "Şükrü places the creamy prayer bead string in a small velvet box; Ali pays and Mert slips the folded letter from Karaman into the box "
         "under the beads.",
         [("luleci", "Hediye sözle tamamlanır. Bir not koyun.", "gentle"),
          ("ali", "Not hazır usta. Karaman'da yazıldı.", "smiling")],
         "static medium two-shot at the glass case",
         t=[T("diger_gider", 3500, "Cemil Bey'e hediye: el oyması lületaşı tespih"), T("yemek", 700, "Çibörek ve met helvası")]),
       S("17:30 akşam", "porsuk", ["mert", "ali", "~hatice"], "Otobüs Yolda",
         "Porsuk Çayı kıyısında yürürken Hatice arar: Hasan'la aynı otobüste Ankara'ya gelmektedirler.",
         "Mert walks along the riverside with the phone on speaker held between him and Ali; both laugh as they listen; a tram passes far behind "
         "them across a small bridge. Their lips stay closed while Hatice speaks.",
         [("hatice", "Hasan Bey'le aynı otobüsteyiz! Domates ve reçel konuşuyoruz.", "cheerful, from the phone speaker"),
          ("mert", "Anne, Ali'nin babasına kayısı reçeli verme, hepsini o yer!", "laughing")],
         "smooth tracking shot along the river", h="kar"),
       S("23:00 gece", "kasa", ["mert", "ali"], "Son Gece",
         "Son geceyi kamyonetin kasasında, battaniyelere sarılı yıldızlara bakarak geçirirler.",
         "Mert and Ali lie side by side on the pickup bed wrapped in thick blankets, looking at the stars, their breath visible; Mert raises his "
         "hand and traces a long line across the sky; Ali smiles with his eyes closed.",
         [("mert", "Malatya'dan buraya... bir motor, bir kamyonet, seksen bir il.", "quiet, wondering"),
          ("ali", "Yarın Ankara. Yarın bitiyor.", "emotional")],
         "slow crane-up from above them to the stars", h="serin",
         t=[T("konaklama", 1200, "Otel, 1 gece (yarısı kamyonette geçti)"), T("ulasim", 1200, "Yakıt: Eskişehir-Ankara")]),
   ],
   misafir={"sarkuteri": ("ŞARKÜTERİCİ", "DELI OWNER, a 46-year-old Turkish woman, short dark hair, round glasses, a white apron", "adult female voice"),
            "luleci": ("ŞÜKRÜ USTA", "ŞÜKRÜ, a 70-year-old Turkish meerschaum carver, thin, a white beard, magnifying glasses on his forehead, a "
                       "white-dusted apron", "elderly male voice, wise and gentle, Eskişehir Turkish")},
   ay=AY, hava="kar", kiyafet=K, urun="Lületaşı, çibörek, met helvası; Odunpazarı evleri, Porsuk Çayı",
   sponsor="Lületaşı, çibörek ya da şehir turizmi alanında",
   kapak=("kasa", ["mert", "ali"], "Mert and Ali lie wrapped in thick blankets on the open bed of an old pickup truck under a sky full of stars, "
          "breath clouds rising, Mert tracing a line across the sky", "Kamyonet kasasında battaniyelere sarılıp yıldızlara bakan Mert ve Ali."),
   yakinda=("lule", ["mert"], "A creamy white meerschaum prayer bead string glowing under a single warm lamp in a dark workshop, white dust "
            "floating in the light", "Karanlık atölyede tek lambanın altında parlayan krem rengi tespih."),
   tiktok="Son gece: kamyonet kasasında yıldızlar ✨ Yarın Ankara #JozhStudios",
   ig=("Eskişehir'de Odunpazarı'nın renkli evleri arasında pembe bir ev hayal ettik. 🏠\n\n"
       "Şükrü Usta'dan Cemil Abi için el oyması bir lületaşı tespih aldık; kutusuna Karaman'da yazılan mektubu koyduk. ✉️ "
       "Hatice Teyze ve Hasan Amca aynı otobüste Ankara'ya geliyor! 🚌\n\nSon gece kamyonet kasasında yıldızlara baktık. Yarın Ankara. Kasa: {KASA}"),
   tags=["#Eskişehir", "#Lületaşı", "#Odunpazarı"],
   son="Son gece. Yarın Ankara'da son taksit.",
   teaser="Renkli evler, beyaz bir taş, bir hediye kutusu ve son gece. Bölüm 86: Eskişehir. Pek yakında.")

# ======================================================================= 87 ANKARA
EP(87, "Ankara", "Son Hesap",
   "Büyük final: 31 Aralık gecesi Ankara'da son taksit, mektup ve Cemil Bey'in sürprizi.",
   "Yılbaşı sabahı Ankara Kalesi'nden şehre bakarlar. Öğlen Hamamönü'nde Hatice ve Hasan'ı karşılarlar; Mert annesine yamuk çömleği verir. "
   "Akşam Hamamönü'nün tarihi bir konağında Cemil Bey gelir. Ali son taksiti uzatır: 150.000 TL. Toplam 800.000 TL ödenmiştir. Mert mektubu "
   "okur ve lületaşı tespihi verir. Cemil Bey sessizce dinler, sonra onları dışarı çağırır: konağın önünde tamir edilmiş, pırıl pırıl motor "
   "durmaktadır. 'Motor sizin. Ben paranın değil, sözün peşindeydim.' Gece yarısı kalede yeni yıl gelirken Mert ve Ali kameraya döner: "
   "'Bir sonraki yolculuk?'",
   {"kale": ("Ankara Kalesi", "the top of Ankara Castle in winter: old stone walls and towers, snow on the stones, a wide view over Ankara's "
             "rooftops and hills, flags far away"),
    "hamamonu": ("Hamamönü", "the restored Ottoman street of Hamamönü in Ankara: white and pastel wooden houses with bay windows, cobbled "
                 "street, string lights for New Year, snow, cafés"),
    "konak": ("Tarihi konak salonu", "the warm main room of a restored Ottoman mansion in Hamamönü at night: a long low table set for dinner with "
              "plates of food, cushions, carpets, lamps, snow visible through the window"),
    "konakonu": ("Konağın önü", "the snowy cobbled street in front of the mansion at night under string lights, with the same unbranded high-end "
                 "sport motorcycle in glossy red and black, now perfectly repaired and shining, no logos"),
    "kalegece": ("Kale, yılbaşı gecesi", "the top of Ankara Castle at midnight on New Year's Eve: city lights spread below, distant fireworks in "
                 "the sky, snow on the stone walls")},
   [
       S("09:30 sabah", "kale", ["mert", "ali"], "Seksen Birinci",
         "Yılbaşı sabahı Ankara Kalesi'nin surlarından şehre bakarlar. Seksen birinci il.",
         "Mert and Ali climb the last stone steps to the top of the castle wall and look out over the snowy city; Mert opens his arms; Ali takes "
         "out the brown notebook and writes a single number.",
         [("ali", "Seksen bir. Yazdım.", "emotional, quiet"),
          ("mert", "Malatya'dan Ankara'ya... seksen bir il, Ali!", "shouting with joy")],
         "slow crane-up from behind them revealing the city", h="kar"),
       S("13:00 öğle", "hamamonu", ["mert", "hatice", "hasan"], "Aileler",
         "Hamamönü'nde Hatice ve Hasan'ı karşılarlar. Mert annesine Avanos'ta yaptığı yamuk çömleği verir.",
         "Mert hugs his mother in the snowy street, then holds out a small lopsided clay pot; Hatice laughs and cries at the same time, holding it "
         "with both hands; Hasan stands beside them smiling.",
         [("mert", "Anne, kendim yaptım. Biraz yamuk ama.", "shy, emotional"),
          ("hatice", "Yamuk değil oğlum, en güzeli. Reçel koyacağım.", "crying, laughing")],
         "slow push-in on the clay pot between them", h="kar"),
       S("20:00 iç-gece", "konak", ["mert", "ali", "cemil"], "Son Taksit",
         "Konakta yılbaşı sofrasında Cemil Bey gelir. Ali son taksiti uzatır: 150.000 TL. Toplam 800.000 TL ödenmiştir.",
         "Cemil Bey sits at the head of the long low table; Ali stands, holds his phone with the transfer ready and turns it toward him, then "
         "presses send; Cemil looks at his own phone, reads it and nods once, slowly.",
         [("ali", "Yüz elli bin. Toplam sekiz yüz bin lira, Cemil Bey.", "steady, emotional"),
          ("cemil", "Tamamı geldi.", "slow, quiet")],
         "slow push-in along the table to Cemil Bey",
         t=T("borc", 150000, "7. ve son taksit: Cemil Bey (İç Anadolu sezonu sonu) · toplam 800.000 TL"),
         kurgu="Hatice ve Hasan sofradadır ama bu çekimde arka planda bulanıktır."),
       S("20:15 iç-gece", "konak", ["mert", "cemil"], "Mektup",
         "Mert lületaşı tespihin kutusunu uzatır ve Karaman'da yazdığı mektubu okur. Cemil Bey sessizce dinler.",
         "Mert places the small velvet box in front of Cemil Bey and unfolds the letter; he reads in a soft voice; Cemil Bey opens the box, takes "
         "out the creamy prayer beads and holds them without looking up.",
         [("mert", "Cemil Abi, borcumuzu ödedik ama size bir teşekkür borcumuz kaldı. Bize yolu siz açtınız.", "soft, emotional"),
          ("cemil", "Gelin. Dışarıda bir şey var.", "quiet, standing up")],
         "slow push-in to Cemil Bey's hands on the beads"),
       S("20:30 gece", "konakonu", ["mert", "ali", "cemil"], "Motor Sizin",
         "Konağın önünde tamir edilmiş, pırıl pırıl motor durmaktadır. Cemil Bey anahtarı uzatır.",
         "Cemil Bey stops beside the perfectly repaired red-and-black motorcycle shining under the string lights in the snow and holds out the key "
         "toward Mert and Ali; they stare at the motorcycle, then at him, speechless.",
         [("cemil", "Motor sizin. Ben paranın değil, sözün peşindeydim. Ama kasksız binmek yok.", "slow, warm for the first time"),
          ("mert", "Cemil Abi...", "speechless, crying")],
         "slow orbit around the motorcycle ending on the key", h="kar",
         kurgu="Motor markasızdır, logo ya da yazı yoktur."),
       S("23:59 gece", "kalegece", ["mert", "ali"], "Bir Sonraki Yolculuk",
         "Gece yarısı kalede yeni yıl gelirken Mert ve Ali kameraya döner. Uzakta havai fişekler.",
         "Mert and Ali stand on the snowy castle wall facing the camera directly as distant fireworks bloom over the city lights; Ali holds up the "
         "brown notebook, Mert holds up the motorcycle key; they look at each other and then back at the lens.",
         [("ali", "Sekiz yüz bin lira ödendi. Seksen bir il bitti. Teşekkürler.", "emotional, to the camera"),
          ("mert", "Ama hikâye bitmedi. Bir sonraki yolculuk... nereye olsun?", "grinning, to the camera")],
         "slow dolly-out revealing the city and the fireworks", h="kar",
         t=[T("yemek", 4500, "Yılbaşı sofrası (6 kişi)"), T("konaklama", 2400, "Konak pansiyon, 2 oda")],
         kurgu="Final kartı (kurguda): 87 VİDEO · 81 İL · 800.000 TL ÖDENDİ · JOZH STUDIOS. Ardından: 'Bir sonraki yolculuk? Yorumlara yazın.'"),
   ],
   ay=AY, hava="kar", kiyafet=K, urun="Ankara tavası, Beypazarı kurusu, Ankara keçisi (tiftik); Ankara Kalesi, Hamamönü",
   sponsor="Ankara'daki yerel işletmeler ya da final iş birliği için",
   kapak=("konakonu", ["cemil", "mert", "ali"], "Under string lights in falling snow, stern Cemil Bey holds out a key beside a shining repaired "
          "red-and-black sport motorcycle while Mert and Ali stare in disbelief, tears in Mert's eyes", "Karda ışıklar altında motorun anahtarını uzatan Cemil Bey ve şaşkın Mert ile Ali."),
   yakinda=("kalegece", ["mert", "ali"], "Two silhouettes on a snowy castle wall at midnight, one holding up a small notebook and the other a key, "
            "fireworks blooming over a vast city of lights", "Gece yarısı kale surunda biri defter, biri anahtar tutan iki silüet ve havai fişekler."),
   tiktok="FİNAL: 800.000 TL ödendi ve Cemil Abi'nin sürprizi 🏍️😭 #JozhStudios",
   ig=("BİTTİ. 🥹 Malatya'da bir motor kazasıyla başlayan yolculuk, 87 videoda 81 ili dolaşıp Ankara'da yılbaşı gecesi bitti.\n\n"
       "Son taksiti Cemil Abi'ye kendi elimizle verdik: toplam 800.000 TL. Mert mektubunu okudu. Ve Cemil Abi bizi dışarı çağırdı... "
       "Tamir ettirdiği motor oradaydı: 'Motor sizin. Ben paranın değil, sözün peşindeydim.' 🏍️❤️\n\n"
       "Bize yol arkadaşlığı eden herkese teşekkürler. Kasa: {KASA}. Bir sonraki yolculuk nereye olsun? 👇"),
   tags=["#Ankara", "#Final", "#81İlBitti"],
   son="Borç bitti, motor onların. Mert kameraya sorar: 'Bir sonraki yolculuk nereye olsun?'",
   teaser="Son taksit, bir mektup, bir anahtar ve yeni bir yıl. Bölüm 87: Ankara, büyük final. Pek yakında.")
