# -*- coding: utf-8 -*-
from ortak import EP, S

# ------------------------------------------------------------------ B61 DÜZCE
EP(61, {
    "duzceli": ("DÜZCELİ ESNAF", "DÜZCE SHOPKEEPER, a 60-year-old Turkish man, grey cap, cardigan", "male voice"),
    "cerkez": ("ÇERKEZ PEYNİRCİ TEYZE", "CIRCASSIAN CHEESE MAKER, a 62-year-old Turkish woman of Circassian heritage, light eyes, white headscarf tied back, embroidered apron, holding a round smoked cheese", "female voice, warm"),
}, {
    "A": ("Düzce çarşısı", "a market in Düzce"),
    "B": ("Konuralp Antik Kenti", "the ancient theater ruins of Konuralp (Prusias ad Hypium) in Düzce"),
    "C": ("Çerkez köy evi", "a Circassian village house kitchen with round cheeses, a set table"),
    "D": ("Akçakoca sahili, gece", "the Akçakoca coast at night, waves"),
}, [
    S("Devrek bastonlarını satar.", "A", ["kerem", "duzceli"],
      "The old shopkeeper tries a cane and pays.",
      [("duzceli", "Devrek bastonu, ömürlük."), ("kerem", "Size çok yakıştı amca.")], k="s"),
    S("Konuralp Antik Kenti.", "B", ["kerem", "elif"],
      "They sit on the ancient theater steps.",
      [("elif", "Prusias ad Hypium. Roma'dan kalma."), ("kerem", "Seyirci gitmiş, sahne kalmış.")]),
    S("Çerkez sofra geleneği.", "C", ["kerem", "elif", "cerkez"],
      "The woman serves them at a table with Circassian cheese and dishes.",
      [("cerkez", "Misafir sofradan aç kalkmaz."), ("kerem", "Teyze, ben artık kalkamam bile.")]),
    S("Çerkez peyniri alır.", "C", ["kerem", "cerkez"],
      "Kerem pays for round smoked cheeses.",
      [("cerkez", "Bu peynir dumanla tütsülenir."), ("kerem", "Bolu'ya götürüyorum.")], k="a"),
    S("Mektubu açar.", "D", ["kerem"],
      "Kerem sits on the beach at night, unfolds the letter under his phone light.",
      [("kerem", "Dedemin el yazısı... 'Kerem, bunu okuyorsan yarı yoldasın.'")]),
    S("Mektup: 'Cevdet'in kızı ağır hastaydı. Bilen tek kişi o kamyonun çırağı.'", "D", ["kerem", "~riza"],
      "Close on the letter; the grandfather's voice is heard reading as Kerem's eyes fill.",
      [("riza", "Cevdet'in kızı ağır hastaydı. O gece ne olduğunu bilen tek kişi o kamyonun çırağı.")],
      kam="extreme close-up on handwriting, slow push to Kerem's face"),
])

# ------------------------------------------------------------------ B62 BOLU
EP(62, {
    "bolulu": ("BOLULU ESNAF", "BOLU SHOPKEEPER, a 48-year-old Turkish woman, short hair, green cardigan", "female voice"),
    "asci": ("MENGEN AŞÇISI", "MENGEN CHEF, a 62-year-old Turkish man, tall white chef hat, white double-breasted chef jacket, big smile", "male voice, proud"),
}, {
    "A": ("Bolu çarşısı", "a market in Bolu"),
    "B": ("Yedigöller", "Yedigöller national park with autumn forests reflected in lakes"),
    "C": ("Mengen Aşçılar Festivali", "the Mengen chefs' festival, cooks in white hats at long tables"),
    "D": ("Abant Gölü kıyısı", "the shore of Lake Abant"),
}, [
    S("Çerkez peynirini satar.", "A", ["kerem", "bolulu"],
      "The shopkeeper pays for the cheese.",
      [("bolulu", "Düzce'nin Çerkez peyniri kahvaltının yıldızı."), ("kerem", "Dumanı tütüyor!")], k="s"),
    S("Yedigöller'de sonbahar.", "B", ["kerem", "elif"],
      "They walk through autumn colors by the lakes.",
      [("elif", "Yedi göl, bin renk."), ("kerem", "Bir de yedi ders.")]),
    S("Mengen aşçısı 'tencereye iyi niyet koy' der.", "C", ["kerem", "asci"],
      "The chef stirs a pot and lets Kerem taste.",
      [("asci", "Tencerenin içine iyi niyet koy, yemek kendiliğinden güzel olur."), ("kerem", "Ticarete de mi?")]),
    S("Mudurnu tavuk ürünleri alır.", "C", ["kerem", "asci"],
      "Kerem buys vacuum-packed chicken products at a festival stall.",
      [("asci", "Mudurnu tavuğu meşhurdur."), ("kerem", "Soğuk zincir, gözüm üstünde!")], k="a"),
    S("Yaşar'ı arar ve 'çırak' kelimesini sorar.", "D", ["kerem", "~yasar"],
      "Kerem calls by the lake.",
      [("kerem", "Kaptan, mektupta bir çıraktan bahsediyor."), ("yasar", "...")]),
    S("Yaşar telefonu yüzüne kapatır.", "D", ["kerem"],
      "The call ends; Kerem stares at the phone.",
      [("kerem", "Kapattı... Kaptan, o çırak sensin değil mi?")], kam="slow push-in"),
])

# ------------------------------------------------------------------ B63 SAKARYA
EP(63, {
    "kofteci": ("ISLAMA KÖFTECİ", "ISLAMA KÖFTE COOK, a 50-year-old Turkish man, white apron, dipping bread in broth", "male voice"),
    "ayvaci": ("GEYVE AYVA ÜRETİCİSİ", "QUINCE FARMER, a 57-year-old Turkish woman, straw hat, cardigan, basket of yellow quinces", "female voice"),
}, {
    "A": ("Islama köfteci", "an islama köfte restaurant in Sakarya, grilled meatballs and broth-soaked bread"),
    "B": ("Sapanca Gölü", "Lake Sapanca with forested hills, a calm afternoon"),
    "C": ("Ayva bahçesi", "a quince orchard in Geyve with yellow quinces"),
    "D": ("Otoyol, dikiz aynası", "a highway seen through a car's side mirror, a white van following"),
}, [
    S("Tavuk ürünlerini köfteciye satar.", "A", ["kerem", "kofteci"],
      "The cook checks the packages and pays.",
      [("kofteci", "Mudurnu malı, güvenilir."), ("kerem", "Soğuk zincir sağlam abi.")], k="s"),
    S("Islama köfte yer.", "A", ["kerem", "elif"],
      "Kerem and Elif eat islama köfte.",
      [("elif", "Ekmeği köfte suyuna batırıyorlar!"), ("kerem", "Islama dedikleri bu!")]),
    S("1921 Sakarya Meydan Muharebesi ve Sapanca.", "B", ["kerem"],
      "Kerem sits by the lake.",
      [("kerem", "1921'de Sakarya'da kader değişti. Benim kaderim de yolda değişiyor.")]),
    S("Geyve ayvasını tanır.", "C", ["kerem", "ayvaci"],
      "The farmer hands Kerem a fragrant quince.",
      [("ayvaci", "Geyve ayvası kokusundan bilinir."), ("kerem", "Oda parfümü gibi!")]),
    S("Geyve ayvası alır.", "C", ["kerem", "ayvaci"],
      "Kerem pays for crates of quince.",
      [("kerem", "Kocaeli'ye ayva.")], k="a"),
    S("Dikiz aynasında üç gündür aynı beyaz kamyonet: Necmi.", "D", ["kerem", "necmi"],
      "In the side mirror, a white van follows; the driver is Necmi.",
      [("kerem", "Üç gündür aynı kamyonet... Necmi!")], kam="close-up on the side mirror reflection"),
])

# ------------------------------------------------------------------ B64 KOCAELİ
EP(64, {
    "kocaelili": ("KOCAELİLİ ESNAF", "KOCAELİ SHOPKEEPER, a 45-year-old Turkish man, glasses, blue shirt", "male voice"),
    "pismaniyeci": ("PİŞMANİYE USTASI", "PIŞMANIYE MAKER, a 55-year-old Turkish woman, pulling fine sugar threads with flour", "female voice"),
}, {
    "A": ("İzmit çarşısı", "a market in İzmit"),
    "B": ("SEKA Kâğıt Müzesi", "the SEKA Paper Museum in a converted old paper factory"),
    "C": ("Pişmaniye atölyesi", "a pişmaniye workshop, cotton-like sugar threads"),
    "D": ("İzmit otogarı", "the crowded İzmit bus terminal"),
}, [
    S("Ayvaları satar.", "A", ["kerem", "kocaelili"],
      "The shopkeeper smells a quince and pays.",
      [("kocaelili", "Geyve ayvası, tatlısı olur."), ("kerem", "Ayva tatlısına kaymak da lazım!")], k="s"),
    S("SEKA Kâğıt Müzesi.", "B", ["kerem", "elif"],
      "Kerem and Elif look at old paper machines.",
      [("elif", "Türkiye'nin ilk kâğıt fabrikası."), ("kerem", "Dedemin defteri de buradan çıkmış olabilir!")]),
    S("Pişmaniyenin yapılışı.", "C", ["kerem", "pismaniyeci"],
      "The maker and helpers pull sugar into fine threads in a circle.",
      [("pismaniyeci", "Kırk kişi çeker, ip gibi ince olur."), ("kerem", "Pişman olmayacağım bir tatlı!")]),
    S("Pişmaniye alır.", "C", ["kerem", "pismaniyeci"],
      "Kerem pays for boxes.",
      [("kerem", "Yalova'ya pişmaniye.")], k="a"),
    S("Otogarda kalabalıkta biri çarpar.", "D", ["kerem", "necmi"],
      "In the crowded terminal, a man in a black leather jacket bumps into Kerem and disappears.",
      [("kerem", "Hey, dikkat etsene!")], kam="handheld, crowded"),
    S("Kerem çantasına bakar: DEFTER YOK.", "D", ["kerem"],
      "Kerem opens his bag in panic; the notebook is gone.",
      [("kerem", "Defter... DEFTER YOK!")], kam="fast push-in, panic"),
])

# ------------------------------------------------------------------ B65 YALOVA
EP(65, {
    "yalovali": ("YALOVALI ESNAF", "YALOVA SHOPKEEPER, a 50-year-old Turkish woman, sunglasses on head, floral blouse", "female voice"),
    "cicekci": ("ÇİÇEK ÜRETİCİSİ", "FLOWER GROWER, a 45-year-old Turkish man, greenhouse apron, holding bunches of carnations", "male voice"),
}, {
    "A": ("Yalova çarşısı", "a market in Yalova"),
    "B": ("Atatürk Köşkü (Yürüyen Köşk)", "the historic 'Walking Mansion' of Atatürk in Yalova, a white wooden house beside a large plane tree"),
    "C": ("Sera", "a large greenhouse full of colorful cut flowers in Yalova"),
    "D": ("Termal, gece", "outside the Termal hot springs area at night, steam"),
}, [
    S("Panik içinde pişmaniyeleri satar.", "A", ["kerem", "yalovali"],
      "Kerem sells pişmaniye distractedly.",
      [("yalovali", "İyi misin evladım?"), ("kerem", "Değilim abla ama malım iyi.")], k="s"),
    S("Elif Necmi'nin konumunu sosyal medyadan arar.", "A", ["kerem", "elif"],
      "Elif scrolls through social media on her laptop.",
      [("elif", "Necmi gösteriş yapmayı sever, mutlaka paylaşım yapar."), ("kerem", "Bul onu Elif!")]),
    S("Yürüyen Köşk'ün hikâyesi.", "B", ["kerem"],
      "Kerem looks at the white mansion and the plane tree.",
      [("kerem", "Ağacı kesmemek için köşkü yürütmüşler. Değerli olan korunur.")]),
    S("Yalova'nın kesme çiçekleri.", "C", ["kerem", "cicekci"],
      "The grower shows rows of flowers.",
      [("cicekci", "Türkiye'nin kesme çiçeğinin büyük kısmı Yalova'dan."), ("kerem", "İstanbul'a çiçek götürüyorum.")]),
    S("Kesme çiçek alır.", "C", ["kerem", "cicekci"],
      "Kerem pays for buckets of flowers.",
      [("cicekci", "Çabuk sat, çiçek beklemez."), ("kerem", "Biliyorum.")], k="a"),
    S("Elif ekranı çevirir: 'Defter İstanbul'da, Galata'da, Karahan ofisinde.'", "D", ["kerem", "elif"],
      "Elif turns her laptop to Kerem in the steamy night.",
      [("elif", "Defter İstanbul'da. Galata'da, Karahan ofisinde.")], kam="close-up on the map on the screen"),
])

# ------------------------------------------------------------------ B66 İSTANBUL (1)
EP(66, {
    "eminonu": ("EMİNÖNÜ ÇİÇEKÇİSİ", "EMİNÖNÜ FLOWER SELLER, a 55-year-old Turkish woman, colorful scarf, sitting with buckets of flowers", "female voice, Istanbul accent"),
}, {
    "A": ("Eminönü meydanı", "Eminönü square in Istanbul with the New Mosque, seagulls, ferries"),
    "B": ("Galata, Karahan ofisi önü", "a narrow Galata street with the Galata Tower behind, an office door"),
    "C": ("Kapalıçarşı koridorları", "the Grand Bazaar in Istanbul, endless painted vaulted corridors full of lamps, carpets and jewelry"),
}, [
    S("Çiçeklerin bir kısmı solmuş; kalanını Eminönü'nde satar.", "A", ["kerem", "eminonu"],
      "Kerem shows the flower seller his buckets; some flowers are wilted.",
      [("eminonu", "Bunlar solmuş, bunları alırım."), ("kerem", "Az kâr, ama kâr.")], k="s"),
    S("Yaşar'ın minibüsüyle Galata'ya giderler.", "B", ["kerem", "elif", "yasar"],
      "Yaşar parks a minibus; the three get out and look at an office door.",
      [("yasar", "Ben arabada beklerim, motor çalışır."), ("kerem", "Defterimi alacağım.")]),
    S("Necmi defterle kapıdan çıkar ve kaçar.", "B", ["kerem", "necmi"],
      "Necmi walks out of the office with the notebook, sees Kerem and runs.",
      [("kerem", "Necmi! Dur!"), ("necmi", "Yakalarsan senin!")], kam="action, handheld chase"),
    S("Kapalıçarşı'da kovalamaca (1461'den beri açık, 60'tan fazla sokak).", "C", ["kerem", "necmi"],
      "Kerem chases Necmi through the Grand Bazaar's colorful corridors, dodging lamps and carpets.",
      [("kerem", "Bu çarşının altmış sokağı var ama çıkışı belli!")], kam="fast tracking chase"),
    S("Elif çıkışı kapatır, Kerem defteri geri alır.", "C", ["kerem", "elif", "necmi"],
      "Elif blocks an exit; Necmi trips over a carpet roll; Kerem grabs the notebook.",
      [("elif", "Buradan geçiş yok!"), ("kerem", "Defterim!")]),
    S("Mühür sağlam. Selim kapıda: 'Açmadım. Çünkü içinde ne yazdığını biliyorum.'", "C", ["kerem", "selim"],
      "Kerem checks the seal, intact; Selim appears at a bazaar gate.",
      [("selim", "Açmadım. Çünkü içinde ne yazdığını zaten biliyorum.")], kam="slow push-in on Selim"),
])

# ------------------------------------------------------------------ B67 İSTANBUL (2)
EP(67, {
    "baharatci": ("MISIR ÇARŞISI BAHARATÇISI", "SPICE MERCHANT, a 60-year-old Turkish man, grey beard, red vest, standing before pyramids of spices", "male voice, Istanbul accent"),
}, {
    "A": ("Galata Kulesi terası", "the top balcony of Galata Tower with the Golden Horn and historic peninsula below at sunset"),
    "B": ("Mısır Çarşısı", "the Spice Bazaar in Istanbul, colorful spice pyramids, Turkish coffee"),
    "C": ("Kahve dükkânı", "a traditional Turkish coffee roaster with a cezve on hot sand"),
}, [
    S("Galata Kulesi'nde Selim babasının hikâyesini anlatır.", "A", ["kerem", "selim"],
      "Selim and Kerem stand at the tower balcony, the city below.",
      [("selim", "Babam her şeyini kaybetti. Ben yoksullukta büyüdüm."), ("kerem", "Ben de kaybettim. Ama dedemi kaybetmedim.")]),
    S("Selim'in kırılgan anı.", "A", ["kerem", "selim"],
      "Selim looks away, jaw tight.",
      [("selim", "Babam Rıza'nın adını her duyduğunda ağlardı."), ("kerem", "Belki suçtan değil, vicdandan ağlıyordu.")]),
    S("Mısır Çarşısı'nda baharatçıda çalışır.", "B", ["kerem", "baharatci"],
      "Kerem weighs spices on a scale.",
      [("baharatci", "Kimyon, sumak, pul biber! Hızlı ol!"), ("kerem", "Burnum sekiz il gezdi!")]),
    S("Yevmiye alır.", "B", ["kerem", "baharatci"],
      "The merchant pays Kerem.",
      [("baharatci", "Al bakalım."), ("kerem", "Eyvallah.")], k="s"),
    S("UNESCO listesindeki Türk kahvesi kültürü; kahve alır.", "C", ["kerem", "elif"],
      "Kerem and Elif drink Turkish coffee; Kerem buys packs.",
      [("elif", "Türk kahvesi UNESCO listesinde."), ("kerem", "Bir fincan kahvenin kırk yıl hatırı var. Tekirdağ'a götürüyorum.")], k="a"),
    S("Selim: 'Sayfayı açarsan dava senin aleyhine delil olur.'", "A", ["kerem", "selim"],
      "Selim leaves, turning back once in the evening light.",
      [("selim", "Ankara'da mahkemede görüşürüz. Sayfayı o güne kadar açarsan, aleyhine delil olur.")], kam="medium shot, city lights"),
])

# ------------------------------------------------------------------ B68 TEKİRDAĞ
EP(68, {
    "tekirdagli": ("TEKİRDAĞLI ESNAF", "TEKİRDAĞ SHOPKEEPER, a 52-year-old Turkish man, white shirt, grey trousers", "male voice"),
    "helvaci2": ("PEYNİR HELVACI", "CHEESE HALVA MAKER, a 58-year-old Turkish woman, apron, stirring halva in a big pan", "female voice"),
}, {
    "A": ("Tekirdağ çarşısı", "a market in Tekirdağ near the sea"),
    "B": ("Rákóczi Müzesi", "the Rákóczi Museum, a wooden Ottoman house where a Hungarian prince lived in exile"),
    "C": ("Helva dükkânı", "a shop making Tekirdağ cheese halva"),
    "D": ("Sahil, akşam", "the Tekirdağ seafront at dusk"),
}, [
    S("Türk kahvesini satar.", "A", ["kerem", "tekirdagli"],
      "The shopkeeper smells coffee and pays.",
      [("tekirdagli", "İstanbul kahvesi, köpüğü bol."), ("kerem", "Kırk yıl hatırı var abi.")], k="s"),
    S("Tekirdağ köftesi yer.", "A", ["kerem", "elif"],
      "Kerem and Elif eat Tekirdağ köfte.",
      [("elif", "Akçaabat'tan sonra köfte maratonu!"), ("kerem", "Her ilin köftesi bir başka.")]),
    S("Rákóczi Müzesi'ni gezer.", "B", ["kerem"],
      "Kerem walks through the wooden house museum.",
      [("kerem", "Macar prensi Rákóczi sürgün yıllarını burada geçirmiş. Bu şehir yabancıyı misafir etmiş.")]),
    S("Peynir helvasının yapılışı.", "C", ["kerem", "helvaci2"],
      "The maker stirs halva in a pan.",
      [("helvaci2", "Tatlı peynir, şeker, irmik."), ("kerem", "Peynirden tatlı mı? Tekirdağ şaşırtıyor!")]),
    S("Tekirdağ peynir helvası alır.", "C", ["kerem", "helvaci2"],
      "Kerem pays for halva.",
      [("kerem", "Kırklareli'ne helva.")], k="a"),
    S("Leyla: 'Mahkeme 1978 senedini isteyecek. O senet mühürlü sayfada.'", "D", ["kerem", "~leyla"],
      "Kerem answers a call at the seafront.",
      [("leyla", "Mahkeme 1978 tarihli orijinal ortaklık senedini isteyecek. Bence o senet... mühürlü sayfanın içinde.")], kam="slow push-in"),
])

# ------------------------------------------------------------------ B69 KIRKLARELİ
EP(69, {
    "kirklareli": ("KIRKLARELİLİ ESNAF", "KIRKLARELİ SHOPKEEPER, a 50-year-old Turkish woman, short curly hair, cardigan", "female voice"),
    "hardaliyeci": ("HARDALİYE ÜRETİCİSİ", "HARDALIYE MAKER, a 60-year-old Turkish man, flat cap, vest, bottles of dark grape drink", "male voice"),
}, {
    "A": ("Kırklareli çarşısı", "a market in Kırklareli"),
    "B": ("İğneada Longoz Ormanları", "the flooded Longoz forest of İğneada, still water among tall trees"),
    "C": ("Dupnisa Mağarası", "Dupnisa Cave with dramatic stalactites"),
    "D": ("Pansiyon odası, gece", "a small guesthouse room at night, a desk lamp"),
}, [
    S("Peynir helvasını satar.", "A", ["kerem", "kirklareli"],
      "The shopkeeper tastes halva and pays.",
      [("kirklareli", "Tekirdağ helvası, Trakya'nın tadı."), ("kerem", "Komşudan tatlı!")], k="s"),
    S("Longoz ormanında sessizlik.", "B", ["kerem", "elif"],
      "They walk on a wooden path above still water among trees.",
      [("elif", "Burası Türkiye'nin nadir su basan ormanlarından."), ("kerem", "Sessizliği duyabiliyorum.")]),
    S("Dupnisa Mağarası.", "C", ["kerem"],
      "Kerem walks in the cave.",
      [("kerem", "Trakya'nın yer altı sarayı.")]),
    S("Hardaliye'nin yapılışı.", "A", ["kerem", "hardaliyeci"],
      "The maker pours a dark grape drink.",
      [("hardaliyeci", "Üzüm ve hardal tohumu; alkolsüz, coğrafi işaretli."), ("kerem", "Ekşi-tatlı, çok başka!")]),
    S("Hardaliye alır.", "A", ["kerem", "hardaliyeci"],
      "Kerem pays for bottles.",
      [("kerem", "Edirne'ye hardaliye.")], k="a"),
    S("Mührü açmaya kalkar; Hüseyin Usta telefonda durdurur.", "D", ["kerem", "~husey"],
      "Kerem places a knife above the red seal; his phone rings.",
      [("husey", "Sakın! Ahi mührü yolda açılmaz."), ("kerem", "Usta, beklemekten yoruldum!")], kam="close-up on the knife above the seal"),
])

# ------------------------------------------------------------------ B70 EDİRNE
EP(70, {
    "edirneli": ("EDİRNELİ ESNAF", "EDİRNE SHOPKEEPER, a 55-year-old Turkish man, round glasses, cardigan", "male voice"),
    "bademci": ("BADEM EZMECİSİ", "ALMOND PASTE MAKER, a 50-year-old Turkish woman, apron, shaping almond paste", "female voice"),
}, {
    "A": ("Edirne Ali Paşa Çarşısı", "the Ali Pasha Bazaar in Edirne with striped arches"),
    "B": ("Selimiye Camii", "the Selimiye Mosque by Mimar Sinan, a huge dome and four slender minarets, interior light"),
    "C": ("Kırkpınar alanı", "the Kırkpınar oil wrestling field with a crowd"),
    "D": ("Badem ezmesi dükkânı", "a shop making Edirne almond paste"),
}, [
    S("Hardaliyeyi satar.", "A", ["kerem", "edirneli"],
      "The shopkeeper tastes and pays.",
      [("edirneli", "Hardaliye ciğerin yanına yakışır."), ("kerem", "Edirne ciğeri de sırada!")], k="s"),
    S("Selimiye'nin kubbesi altında öğüt.", "B", ["kerem", "elif"],
      "Kerem stands under the giant dome looking up; Elif films.",
      [("elif", "Mimar Sinan buna 'ustalık eserim' demiş."), ("kerem", "Dedemin defterinde: 'Sabır ustalıktır.'")], kam="tilt up to the dome"),
    S("Kırkpınar'ın tarihi.", "C", ["kerem"],
      "Kerem watches wrestlers in leather trousers.",
      [("kerem", "Kırkpınar, dünyanın en eski spor festivallerinden.")]),
    S("Badem ezmesi alır.", "D", ["kerem", "bademci"],
      "Kerem pays for almond paste.",
      [("bademci", "Edirne badem ezmesi."), ("kerem", "Çanakkale'ye tatlı yolculuk.")], k="a"),
    S("Elif belgeselin fragmanını yayınlar.", "D", ["kerem", "elif"],
      "Elif presses 'upload' on her laptop; they look at each other.",
      [("elif", "Fragman yayında."), ("kerem", "Bismillah.")]),
    S("Sabah 3.000 sipariş mesajı... ve Selim'den tek kelime: 'Akıllıca.'", "A", ["kerem", "elif"],
      "Morning: Kerem's phone shows thousands of notifications; one message stands out.",
      [("kerem", "Üç bin sipariş! Ve Selim: 'Akıllıca.'")], kam="close-up on the phone", kurgu="Bildirimler: 3.000 sipariş + 'S.K.: Akıllıca.'"),
])

# ------------------------------------------------------------------ B71 ÇANAKKALE
EP(71, {
    "ezineci": ("EZİNE PEYNİRCİSİ", "EZİNE CHEESE MAKER, a 56-year-old Turkish man, white cap, white coat, slicing white cheese", "male voice"),
}, {
    "A": ("Çanakkale kordonu", "the Çanakkale seafront with the wooden Trojan Horse replica and the 1915 Çanakkale Bridge in the distance"),
    "B": ("Çanakkale Şehitliği", "the Çanakkale Martyrs' Memorial on the Gallipoli peninsula, quiet and respectful, flags"),
    "C": ("Truva Antik Kenti", "the ruins of ancient Troy"),
    "D": ("Peynir mandırası", "an Ezine cheese dairy with white cheese tins"),
}, [
    S("Badem ezmesini siparişlerle hızla satar.", "A", ["kerem", "elif"],
      "Kerem packs orders while Elif reads them out.",
      [("elif", "İzmir, Bursa, Ankara... Hepsi badem ezmesi istiyor!"), ("kerem", "Tükendi!")], k="s"),
    S("Çanakkale Şehitliği'nde saygı duruşu.", "B", ["kerem", "elif"],
      "Kerem and Elif stand silently at the memorial, heads bowed.",
      [("kerem", "Bu topraklar için canını verenlere...")], kam="slow wide shot, respectful"),
    S("Truva ve Truva Atı.", "C", ["kerem"],
      "Kerem walks among ancient ruins.",
      [("kerem", "Truva Atı'nın hikâyesi: Hediye gibi görünen tuzak. Not aldım.")]),
    S("Ezine peynirini tanır.", "D", ["kerem", "ezineci"],
      "The cheese maker slices white cheese.",
      [("ezineci", "Koyun, keçi, inek sütü; Ezine peyniri coğrafi işaretli."), ("kerem", "Kahvaltının şahı.")]),
    S("Ezine peyniri alır.", "D", ["kerem", "ezineci"],
      "Kerem pays for tins.",
      [("kerem", "Balıkesir'e Ezine.")], k="a"),
    S("'Ege Gıda' dev sipariş teklif eder; Elif: 'Adresi boş bir arsa.'", "A", ["kerem", "elif"],
      "Elif shows a satellite map on her laptop: an empty lot.",
      [("elif", "Bu firmanın adresi... boş bir arsa."), ("kerem", "Truva Atı geldi.")], kam="close-up on the empty lot on the screen"),
])

# ------------------------------------------------------------------ B72 BALIKESİR
EP(72, {
    "sarkuteri": ("ŞARKÜTERİCİ", "DELICATESSEN OWNER, a 48-year-old Turkish woman, black apron, glasses", "female voice"),
    "hosmerimci": ("HÖŞMERİMCİ", "HÖŞMERIM MAKER, a 62-year-old Turkish man, white apron, stirring cheese dessert in a copper pan", "male voice"),
}, {
    "A": ("Şarküteri", "a delicatessen in Balıkesir"),
    "B": ("Kaz Dağları", "the green Kazdağları (Mount Ida) forests, streams"),
    "C": ("Manyas Kuş Cenneti", "the Manyas Bird Paradise, birds over a lake"),
    "D": ("Höşmerim dükkânı", "a shop making höşmerim dessert"),
}, [
    S("Ege Gıda teklifini reddeder; peyniri doğrudan şarküteriye satar.", "A", ["kerem", "sarkuteri"],
      "The owner tastes Ezine cheese and pays.",
      [("sarkuteri", "Sahte firmaya değil bize sattın, iyi ettin."), ("kerem", "Truva Atı'na kapıyı açmadım.")], k="s"),
    S("Kaz Dağları'nda yürür.", "B", ["kerem", "elif"],
      "They walk by a stream in the forest.",
      [("elif", "Kaz Dağları, Türkiye'nin oksijen deposu."), ("kerem", "Nefes almak bedava, keyfini çıkar.")]),
    S("Manyas Kuş Cenneti.", "C", ["kerem"],
      "Kerem watches birds.",
      [("kerem", "Kuşlar burada mola veriyor. Ben de veriyorum.")]),
    S("Höşmerimin yapılışı.", "D", ["kerem", "hosmerimci"],
      "The maker stirs dessert.",
      [("hosmerimci", "Peynir, irmik, şeker; Balıkesir'in höşmerimi."), ("kerem", "Peynirli tatlıların ülkesi!")]),
    S("Höşmerim alır.", "D", ["kerem", "hosmerimci"],
      "Kerem pays.",
      [("kerem", "Bursa'ya höşmerim.")], k="a"),
    S("Bursa'dan imzasız mesaj: 'Koza Han'da dedenin eski ortağı seni bekliyor.'", "D", ["kerem"],
      "Kerem reads a message at night.",
      [("kerem", "Dedemin eski ortağı mı? Cevdet mi?")], kurgu="Mesaj: 'Koza Han'da dedenin eski ortağı seni bekliyor.'"),
])

# ------------------------------------------------------------------ B73 BURSA (1)
EP(73, {
    "bursali": ("BURSALI ESNAF", "BURSA SHOPKEEPER, a 50-year-old Turkish man, brown vest", "male voice"),
    "ipekci": ("YAŞLI İPEKÇİ", "OLD SILK MERCHANT, an 85-year-old Turkish man, tiny and thin, white goatee, black fez-style cap, silk scarf, cane", "elderly male voice, soft"),
}, {
    "A": ("Bursa çarşısı", "a market in Bursa"),
    "B": ("Koza Han", "the Koza Han silk caravanserai in Bursa (1491), courtyard with a small mosque, silk shops"),
    "C": ("Ulu Cami ve Cumalıkızık", "the Bursa Grand Mosque with its many domes and a fountain inside; and the Ottoman village Cumalıkızık"),
}, [
    S("Höşmerimi satar.", "A", ["kerem", "bursali"],
      "The shopkeeper pays.",
      [("bursali", "Balıkesir höşmerimi, kestane şekerinin kardeşi."), ("kerem", "Tatlı komşuluk!")], k="s"),
    S("Koza Han'a gelir.", "B", ["kerem", "elif"],
      "Kerem and Elif enter the han courtyard.",
      [("elif", "1491'den beri ipek ticaretinin merkezi."), ("kerem", "Burada kim bekliyor?")]),
    S("Ulu Cami ve Cumalıkızık.", "C", ["kerem"],
      "Kerem visits the mosque with its interior fountain, then walks in a cobbled village.",
      [("kerem", "Ulu Cami'nin içinde şadırvan var. Bursa her şeyi içinde saklıyor.")]),
    S("Mesajı atan yaşlı ipekçi çıkar.", "B", ["kerem", "ipekci"],
      "A tiny old man with a cane approaches.",
      [("ipekci", "Mesajı ben attım. Ortak değilim, aracıydım."), ("kerem", "Neyin aracısı?")]),
    S("İpekçi: 'Deden ile Cevdet'i ben tanıştırdım.'", "B", ["kerem", "ipekci"],
      "They sit on a bench in the han, the old man speaking slowly.",
      [("ipekci", "Deden ile Cevdet'i ben tanıştırdım. İkisi de benim çırağımdı.")]),
    S("İpekçi: 'O gece para Cevdet'teydi, Rıza'da değil.'", "B", ["kerem", "ipekci"],
      "The old man grips Kerem's hand.",
      [("ipekci", "O gece Cevdet'in kızı ameliyattaydı... Para Cevdet'teydi, Kerem. Rıza'da değil.")], kam="slow push-in"),
])

# ------------------------------------------------------------------ B74 BURSA (2)
EP(74, {
    "ipekci": ("YAŞLI İPEKÇİ", "OLD SILK MERCHANT, an 85-year-old Turkish man, tiny and thin, white goatee, black fez-style cap, silk scarf, cane", "elderly male voice, soft"),
    "karagozcu": ("KARAGÖZ USTASI", "SHADOW PUPPETEER, a 55-year-old Turkish man behind a white screen with colorful leather puppets", "male voice, theatrical"),
}, {
    "A": ("Karagöz perdesi", "a traditional Karagöz shadow theater with a lit white screen and colorful leather puppets"),
    "B": ("İskenderci", "a historic İskender kebab restaurant in Bursa"),
    "C": ("Koza Han ipek dükkânı", "a silk shop in Koza Han with scarves"),
    "D": ("Han avlusu, gece", "the Koza Han courtyard at night"),
}, [
    S("Karagöz-Hacivat gölge oyunu.", "A", ["kerem", "karagozcu"],
      "Shadow puppets argue on the screen; Kerem laughs.",
      [("karagozcu", "Biri sözünü tutar, biri tutmaz; iki dost yine de birbirini bırakmaz!"), ("kerem", "Dedem ile Cevdet gibi.")]),
    S("İskender kebabı yer.", "B", ["kerem", "elif"],
      "Butter is poured over İskender kebab at their table.",
      [("elif", "Tereyağını masada döküyorlar!"), ("kerem", "Bursa gösterişi!")]),
    S("İpekçinin dükkânında bir gün çalışır.", "C", ["kerem", "ipekci"],
      "Kerem folds silk scarves carefully.",
      [("ipekci", "İpek ince iştir, sert tutarsan yırtılır."), ("kerem", "İnsan kalbi gibi.")]),
    S("Yevmiye alır, ipek eşarp alır.", "C", ["kerem", "ipekci"],
      "The old man pays Kerem and sells him silk scarves.",
      [("ipekci", "Bilecik'te iyi satarsın."), ("kerem", "Ustamın ustası!")], k="a"),
    S("Kerem Selim'i arar.", "D", ["kerem", "~selim"],
      "Kerem calls at night.",
      [("kerem", "Selim, baban sana yalan söylemiş olabilir.")]),
    S("Selim: 'Benim babam yalan söylemez!' Hat kesilir.", "D", ["kerem", "~selim"],
      "Kerem hears an angry voice, the line goes dead.",
      [("selim", "Benim babam yalan söylemez!")], kam="close-up on Kerem lowering the phone"),
])

# ------------------------------------------------------------------ B75 BİLECİK
EP(75, {
    "bilecikli": ("BİLECİKLİ ESNAF", "BİLECİK SHOPKEEPER, a 48-year-old Turkish woman, scarf, blouse", "female voice"),
    "seramikci": ("BOZÜYÜK SERAMİKÇİSİ", "CERAMIC ARTIST, a 40-year-old Turkish man, clay-stained apron, glazing a bowl", "male voice"),
}, {
    "A": ("Bilecik çarşısı", "a market in Bilecik"),
    "B": ("Söğüt, Ertuğrul Gazi Türbesi", "the Ertuğrul Gazi tomb in Söğüt with a big old plane tree"),
    "C": ("Bozüyük seramik atölyesi", "a ceramic workshop in Bozüyük, glazed plates and bowls"),
}, [
    S("İpek eşarpları satar.", "A", ["kerem", "bilecikli"],
      "The shopkeeper pays for scarves.",
      [("bilecikli", "Bursa ipeği, hediyelik."), ("kerem", "Koza Han'dan selam var.")], k="s"),
    S("Söğüt'te Osmanlı'nın kuruluşu.", "B", ["kerem", "elif"],
      "Kerem and Elif stand under the old plane tree.",
      [("elif", "Osmanlı burada küçük bir obadan doğdu."), ("kerem", "Büyük devlet küçük bir çadırdan.")]),
    S("Deftere not alır.", "B", ["kerem"],
      "Kerem writes under the tree.",
      [("kerem", "Söğüt dersi: Küçük başlamaktan utanma.")]),
    S("Bozüyük seramiği.", "C", ["kerem", "seramikci"],
      "The artist glazes a bowl.",
      [("seramikci", "Bozüyük Türkiye'nin seramik merkezlerinden."), ("kerem", "Avanos'un kili, Bozüyük'ün sırı.")]),
    S("Seramik alır.", "C", ["kerem", "seramikci"],
      "Kerem pays.",
      [("kerem", "Eskişehir'e seramik.")], k="a"),
    S("Avukat: 'Karşı tarafın tanığı: Yaşar Demirci.'", "A", ["kerem", "~ayse"],
      "Kerem on the phone with his mother, stunned.",
      [("ayse", "Avukat aradı. Karşı taraf tanık bulmuş. Adı Yaşar Demirci."), ("kerem", "Yaşar Kaptan mı?!")], kam="slow push-in"),
])

# ------------------------------------------------------------------ B76 ESKİŞEHİR
EP(76, {
    "eskisehirli": ("ESKİŞEHİRLİ ESNAF", "ESKİŞEHİR SHOPKEEPER, a 45-year-old Turkish man, hipster beard, denim apron", "male voice"),
    "luleci": ("LÜLETAŞI USTASI", "MEERSCHAUM CARVER, a 66-year-old Turkish man, white mustache, carving a white meerschaum pipe", "elderly male voice"),
}, {
    "A": ("Eskişehir çarşısı", "a modern street in Eskişehir by the Porsuk river with trams"),
    "B": ("Odunpazarı evleri", "the colorful Ottoman houses of Odunpazarı"),
    "C": ("Lületaşı atölyesi", "a meerschaum carving workshop, white stone pipes"),
    "D": ("Porsuk kıyısı, akşam", "the Porsuk river at dusk with gondolas"),
}, [
    S("Seramikleri satar.", "A", ["kerem", "eskisehirli"],
      "The shopkeeper pays.",
      [("eskisehirli", "Bozüyük seramiği, öğrenciler bayılır."), ("kerem", "Kahve kupası niyetine!")], k="s"),
    S("Odunpazarı ve çibörek.", "B", ["kerem", "elif"],
      "Kerem and Elif eat çibörek among colorful houses.",
      [("elif", "Çibörek! Tatar mutfağından."), ("kerem", "Sıcak, sıcak!")]),
    S("Lületaşı oymacılığı.", "C", ["kerem", "luleci"],
      "The carver shapes a white stone.",
      [("luleci", "Lületaşı dünyada çok az yerde çıkar; Eskişehir'in beyaz altını."), ("kerem", "Beyaz altın!")]),
    S("Lületaşı alır.", "C", ["kerem", "luleci"],
      "Kerem pays.",
      [("kerem", "Kütahya'ya lületaşı.")], k="a"),
    S("Yaşar ile yüz yüze konuşur.", "D", ["kerem", "yasar"],
      "Yaşar sits on a bench by the river; Kerem approaches.",
      [("kerem", "Selim'in tanığı mı olacaksın?"), ("yasar", "Selim'in avukatı beni çağırdı.")]),
    S("Yaşar: 'Ne söyleyeceğime mahkemede karar vereceğim.'", "D", ["kerem", "yasar"],
      "Yaşar stands and walks away slowly.",
      [("yasar", "Ne söyleyeceğime mahkemede karar vereceğim.")], kam="medium shot of Yaşar walking away"),
])

# ------------------------------------------------------------------ B77 KÜTAHYA
EP(77, {
    "kutahyali": ("KÜTAHYALI ESNAF", "KÜTAHYA SHOPKEEPER, a 55-year-old Turkish woman, blue scarf", "female voice"),
    "cinici": ("ÇİNİ USTASI", "TILE MASTER, a 68-year-old Turkish man, white beard, blue-stained fingers, painting a tile", "elderly male voice"),
}, {
    "A": ("Kütahya çarşısı", "a market in Kütahya"),
    "B": ("Aizanoi Zeus Tapınağı", "the Temple of Zeus at Aizanoi, standing ancient columns"),
    "C": ("Çini atölyesi", "a Kütahya tile workshop with blue and white tiles"),
}, [
    S("Lületaşını satar.", "A", ["kerem", "kutahyali"],
      "The shopkeeper pays.",
      [("kutahyali", "Eskişehir lületaşı, koleksiyonluk."), ("kerem", "Beyaz altın teslim!")], k="s"),
    S("Aizanoi'nin Zeus Tapınağı.", "B", ["kerem", "elif"],
      "They walk among ancient columns.",
      [("elif", "Dünyanın en iyi korunmuş Zeus tapınaklarından."), ("kerem", "Burada da bir borsa varmış!")]),
    S("Evliya Çelebi'yi anar.", "A", ["kerem"],
      "Kerem stands in front of Evliya Çelebi's house.",
      [("kerem", "Evliya Çelebi de dünyayı gezip yazmış. Ben de il il yazıyorum.")]),
    S("Çininin mavisi.", "C", ["kerem", "cinici"],
      "The master paints blue patterns on a tile.",
      [("cinici", "Kütahya mavisi sırrını fırında söyler."), ("kerem", "Usta, bu desenler çok eski.")]),
    S("Çini alır.", "C", ["kerem", "cinici"],
      "Kerem pays for tiles.",
      [("kerem", "Uşak'a çini.")], k="a"),
    S("Usta bir karonun arkasını çevirir: iki ailenin mühürleri yan yana, 1978.", "C", ["kerem", "cinici"],
      "The master turns over an old tile, revealing two family seals side by side.",
      [("cinici", "Bu karoyu 1978'de iki ortak sipariş etti. Aksoy ve Karahan.")], kam="extreme close-up on the seals"),
])

# ------------------------------------------------------------------ B78 UŞAK
EP(78, {
    "usakli": ("UŞAKLI ESNAF", "UŞAK SHOPKEEPER, a 50-year-old Turkish man, grey suit", "male voice"),
    "halici": ("UŞAK HALICISI", "CARPET WEAVER, a 55-year-old Turkish woman, scarf, at a large loom", "female voice"),
}, {
    "A": ("Uşak çarşısı", "a market in Uşak"),
    "B": ("Uşak Müzesi, Karun Hazinesi", "the Uşak Museum displaying the Lydian Karun treasure, gold and silver artifacts under spotlights"),
    "C": ("Halı atölyesi", "an Uşak carpet workshop, large looms"),
}, [
    S("Çinileri satar.", "A", ["kerem", "usakli"],
      "The shopkeeper pays.",
      [("usakli", "Kütahya çinisi, evin süsü."), ("kerem", "Mavi bereket!")], k="s"),
    S("Karun Hazinesi.", "B", ["kerem", "elif"],
      "They look at the gold treasure in glass cases.",
      [("elif", "Yurt dışına kaçırılmış, yıllar sonra geri dönmüş."), ("kerem", "Asıl hazine döndüğü yere aittir.")]),
    S("Deftere yazar.", "B", ["kerem"],
      "Kerem writes in front of the cases.",
      [("kerem", "Uşak dersi: Çalınan geri döner. Doğru da.")]),
    S("Uşak halısının dokunuşu.", "C", ["kerem", "halici"],
      "The weaver ties knots fast.",
      [("halici", "Uşak halısı saraylara gitmiş."), ("kerem", "Ben seccade boyunu alayım.")]),
    S("Uşak halısı alır.", "C", ["kerem", "halici"],
      "Kerem pays.",
      [("kerem", "Manisa'ya halı.")], k="a"),
    S("Elif'in annesinden mesaj: 'İzmir'e gelin. Babam dedenizi tanıyormuş.'", "A", ["kerem", "elif"],
      "Elif reads a message and looks at Kerem surprised.",
      [("elif", "Annem yazmış: 'Babam sizin dedenizi tanıyormuş.'"), ("kerem", "Senin deden de mi?!")], kam="two-shot, surprised faces"),
])

# ------------------------------------------------------------------ B79 MANİSA
EP(79, {
    "manisali": ("MANİSALI ESNAF", "MANISA SHOPKEEPER, a 52-year-old Turkish man, mustache, vest", "male voice"),
    "mesirci": ("MESİR MACUNCU", "MESIR PASTE MAKER, a 60-year-old Turkish woman, white headscarf, stirring a dark paste", "female voice"),
}, {
    "A": ("Manisa çarşısı", "a market in Manisa"),
    "B": ("Sultan Camii ve Mesir şenliği", "the Sultan Mosque in Manisa with people catching paper-wrapped mesir candies thrown from the minaret"),
    "C": ("Spil Dağı", "Spil Mountain national park"),
    "D": ("İzmir otobüsü", "inside an intercity bus to İzmir"),
}, [
    S("Uşak halılarını satar.", "A", ["kerem", "manisali"],
      "The shopkeeper pays.",
      [("manisali", "Uşak halısı, değer kaybetmez."), ("kerem", "Saraylık!")], k="s"),
    S("Mesir şenliği ve Hafsa Sultan hikâyesi.", "B", ["kerem", "elif"],
      "Mesir candies are thrown from the minaret; they catch some.",
      [("elif", "Hafsa Sultan'ın şifası, UNESCO listesinde."), ("kerem", "Yakaladım!")]),
    S("Spil Dağı.", "C", ["kerem"],
      "Kerem looks at the view.",
      [("kerem", "Spil'in ağlayan kayası... Her şehrin bir gözyaşı var.")]),
    S("Mesir macununun 41 baharatı.", "A", ["kerem", "mesirci"],
      "The maker stirs dark paste.",
      [("mesirci", "Kırk bir çeşit baharat."), ("kerem", "Kırk bir! Kasama da iyi gelsin.")]),
    S("Mesir macunu alır.", "A", ["kerem", "mesirci"],
      "Kerem pays.",
      [("kerem", "İzmir'e mesir.")], k="a"),
    S("İhbar: 'Kemeraltı'nda senin adınla sahte mesir satılıyor.'", "D", ["kerem"],
      "Kerem reads a message on the bus.",
      [("kerem", "Yine mi sahte ürün?!")], kurgu="Mesaj: 'Kemeraltı'nda senin adınla sahte mesir satılıyor.'"),
])

# ------------------------------------------------------------------ B80 İZMİR (1)
EP(80, {
    "kemeralti": ("KEMERALTI ESNAFI", "KEMERALTI SHOPKEEPER, a 45-year-old Turkish woman, sunglasses on head, colorful shirt", "female voice, Izmir accent"),
    "elifdede": ("ELİF'İN DEDESİ", "ELİF'S GRANDFATHER, an 84-year-old Turkish man, white hair, thick glasses, cardigan, holding an old cassette player", "elderly male voice, warm Aegean accent"),
}, {
    "A": ("Kemeraltı Çarşısı", "Kemeraltı bazaar in İzmir, busy lanes"),
    "B": ("Saat Kulesi, Konak", "the İzmir Clock Tower in Konak Square with pigeons and the sea"),
    "C": ("Elif'in ailesinin evi", "a cozy family home in İzmir, dinner table with Aegean dishes"),
}, [
    S("Sahte ürün piyasayı bozmuştur; mesiri ucuza satar. Zarar.", "A", ["kerem", "kemeralti"],
      "The shopkeeper points to fake products with Kerem's photo.",
      [("kemeralti", "Senin adınla daha ucuzu satılıyor."), ("kerem", "O benim değil abla... Mecburen ucuza.")], k="s"),
    S("Saat Kulesi'nde boyoz ve gevrek.", "B", ["kerem", "elif"],
      "They eat boyoz and simit at the Clock Tower.",
      [("elif", "Burada simide gevrek denir!"), ("kerem", "Bir gevrek, bir boyoz, bir zarar.")]),
    S("Elif'in ailesiyle akşam yemeği.", "C", ["kerem", "elif", "elifdede"],
      "They sit at the family dinner table.",
      [("elifdede", "Hoş geldin evladım, otur bakalım."), ("kerem", "Teşekkürler amca.")]),
    S("Dede Rıza'yı anlatır.", "C", ["kerem", "elifdede"],
      "The grandfather smiles remembering.",
      [("elifdede", "Rıza, İzmir'e gelince bizim evde kalırdı."), ("kerem", "Dedem her yerde dost bırakmış.")]),
    S("Kerem deftere not alır.", "C", ["kerem"],
      "Kerem writes at the table.",
      [("kerem", "İzmir dersi: Adını korumak, malını korumaktan zor.")]),
    S("Dede eski bir kasetçalar getirir: 'Torunu gelirse dinlesin.'", "C", ["kerem", "elifdede"],
      "The grandfather places an old cassette player on the table.",
      [("elifdede", "Rıza bunu 2012'de bana bıraktı. 'Torunum gelirse dinlesin' dedi.")], kam="close-up on the cassette"),
])
