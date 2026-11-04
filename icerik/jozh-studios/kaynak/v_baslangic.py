# -*- coding: utf-8 -*-
"""Başlangıç videoları (Bölüm 1-6). Malatya, mayıs sonu. Kasa Bölüm 4 sahne 6'da açılır."""
from ortak import EP, S, T, U

EV = ("their small newly rented apartment in Malatya: a modest living room with a second-hand grey fabric sofa, a low wooden coffee "
      "table, stacked cardboard moving boxes in one corner, bare white walls, a large window looking out on mid-rise apartment blocks "
      "and dry brown hills in the distance")
OTOPARK = ("the paved courtyard and small parking area of a six-storey Malatya apartment building with cream-colored walls, balconies "
           "with laundry racks, a row of young plane trees and an iron garden gate")
MALATYA_CADDE = ("a wide, clean avenue in Malatya lined with new mid-rise apartment blocks, young plane trees, small shops with "
                 "plain awnings and light traffic far in the background")
YAN_SOKAK = ("a quiet residential side street in Malatya with parked cars along one curb, a small white pickup truck parked at the "
             "right curb, low garden walls and an apricot tree hanging over a wall")
PAZAR = ("the Malatya apricot market (kayısı pazarı): long rows of covered stalls with open sacks and wooden crates full of sun-dried "
         "golden and dark brown apricots, hanging scales, paper bags, and a corrugated metal roof letting in strips of sunlight")
CATI = ("the flat rooftop terrace of their apartment building in Malatya with a low parapet wall, a small plastic table and two "
        "chairs, potted geraniums, and a wide view over the city's apartment blocks toward the hills")

RAMAZAN = ("RAMAZAN AMCA", "RAMAZAN, a 62-year-old Turkish apricot merchant, short and round, a sun-darkened smiling face, a white "
           "short beard, wearing a flat grey cap, a cream shirt with rolled sleeves and a dark blue vest with a pen in its pocket",
           "elderly male voice, warm husky baritone, cheerful Malatya Turkish, a seasoned bargainer")

# ======================================================================= VİDEO 1
EP(1, None, "Kaza",
   "Yeni eve çıkan Mert ve Ali, komşuları Cemil Bey'in motosikletini ödünç alır ve bir kaza geçirir.",
   "Mert ve Ali Malatya'da ilk evlerine taşınmıştır; kolilerin arasında para kazanma hayalleri kurarlar. Çarşıya gidip gelmek için "
   "apartmanın üst katındaki Cemil Bey'in markasız spor motosikletini ödünç alırlar. Cemil Bey tek şart koşar: kasksız binmek yok. "
   "Şehrin yeni caddesinde ilk kez rüzgârı yüzlerinde hissederler. Ama bir yan sokakta önlerine fırlayan köpeği ezmemek için direksiyonu "
   "kıran Mert, motoru park hâlindeki bir kamyonetin arkasına sürter. İkisi de kasklı oldukları için yara almaz, ama motor ağır hasarlıdır. "
   "Tam o anda Mert'in telefonu çalar: arayan Cemil Bey'dir.",
   {"ev": ("Yeni ev, salon", EV), "otopark": ("Apartman bahçesi", OTOPARK), "cadde": ("Malatya, yeni cadde", MALATYA_CADDE),
    "sokak": ("Malatya, yan sokak", YAN_SOKAK)},
   [
       S("17:10 iç-gündüz", "ev", ["mert", "ali"], "Kolilerin Arasında Hayaller",
         "Taşınmanın ilk günü. Ali kolileri açarken Mert koltuğa yayılmış, büyük hayaller kuruyor.",
         "Ali kneels by an open cardboard box and lifts out a stack of plates, while Mert lies back on the grey sofa with his hands behind his head, "
         "gazing at the ceiling and smiling; Ali glances at him and shakes his head with a small laugh.",
         [("mert", "Ali, ev tamam. Şimdi tek eksik para.", "dreamy, upbeat"),
          ("ali", "Bir de buzdolabı. Bir de koltuğun dördüncü ayağı.", "dry, amused")],
         "slow dolly-in from the doorway to a medium two-shot"),
       S("17:40 ikindi", "otopark", ["mert", "ali", "cemil"], "Cemil Bey'in Şartı",
         "Cemil Bey motorun anahtarını ve iki kaskı uzatır. Çarşıya gidip geleceklerdir; kasksız binmek yasak.",
         "Cemil Bey stands beside the parked motorcycle (" + "an unbranded high-end sport motorcycle in glossy red and black with no logos" + ") and "
         "holds out a key; Mert takes it eagerly while Ali takes two black full-face helmets from the motorcycle seat with both hands.",
         [("cemil", "Bir saat. Çarşıya gidip geleceksiniz. Kasksız binmek yok.", "stern, slow"),
          ("mert", "Söz Cemil Abi, çizik bile almaz.", "eager, confident")],
         "static medium three-shot at eye level, slight push-in on the key"),
       S("18:00 gün batımı", "cadde", ["mert", "ali"], "Rüzgârı İlk Kez Hissetmek",
         "Malatya'nın yeni caddesinde motorla ilerliyorlar. Mert sürüyor, Ali arkada; ikisi de kasklı ve mutlu.",
         "Mert rides the unbranded red-and-black sport motorcycle at a calm moderate speed along the avenue with Ali seated behind him, both wearing "
         "black full-face helmets with open visors; Mert lifts his chin with joy and Ali holds his shoulders.",
         [("mert", "Bir gün böyle bir motor bizim olacak!", "shouting happily over the wind"),
          ("ali", "Önce bunu sağ salim geri verelim.", "loud, half-laughing")],
         "smooth tracking shot from the side, matching their speed"),
       S("18:10 gün batımı", "sokak", ["mert", "ali"], "Köpek",
         "Yan sokakta bir sokak köpeği aniden yola fırlar. Mert köpeği ezmemek için frene basıp direksiyonu kırar; motor kayar ve park hâlindeki kamyonetin arkasına sürter. Kaza sert ama kanlı değil.",
         "A medium-sized stray dog suddenly runs across the street; Mert brakes and swerves, the motorcycle skids sideways at low speed and its front "
         "scrapes against the rear bumper of the parked white pickup truck; Mert and Ali slide off onto the asphalt and roll once, helmets on, "
         "while the dog runs away unharmed.",
         [("ali", "Mert, köpek!", "alarmed shout")],
         "wide static shot from the sidewalk, the action crosses the frame from left to right",
         kurgu="Kaza tek çekimde, yavaş hızda ve kansız. Gerekirse sondaki 2 saniyeyi ağır çekim yap."),
       S("18:11 gün batımı", "sokak", ["mert", "ali"], "İyi misin?",
         "İkisi de yerden kalkar, kasklarını çıkarır. Yara yok; ama gözleri yerde yatan motora takılır.",
         "Mert and Ali sit up on the asphalt and pull off their helmets; they look at each other, check their arms, then both turn slowly toward "
         "the motorcycle lying on its side, now badly damaged with a cracked front fairing, a bent handlebar and a broken headlight.",
         [("ali", "Mert, iyi misin?", "shaken, breathless"),
          ("mert", "Ben iyiyim... Motor iyi değil.", "stunned, quiet")],
         "slow push-in from a low angle near the ground"),
       S("18:15 gün batımı", "sokak", ["mert", "ali"], "Arayan Cemil Bey",
         "Kaldırımda oturup hasarlı motora bakarken Mert'in telefonu çalar. Ekranda 'Cemil Abi' yazıyor. Donup kalırlar.",
         "Mert and Ali sit side by side on the curb with their helmets in their laps, staring at the damaged motorcycle; Mert's phone vibrates in his "
         "hand, he lifts it, looks at the screen and freezes, then slowly turns the screen toward Ali, whose eyes widen.",
         [("mert", "Cemil Abi arıyor.", "whisper, frozen"),
          ("ali", "Aç. Açmak zorundayız.", "tense, quiet")],
         "static medium shot from across the street, very slow push-in",
         kurgu="Telefon ekranı yazısı ('Cemil Abi') kurguda eklenir; prompt'ta ekran yazısı yoktur."),
   ],
   ay="Mayıs sonu", hava="açık",
   kapak=("sokak", ["mert", "ali"],
          "Mert and Ali sit on the curb in golden sunset light holding their helmets, both looking shocked at the badly damaged red-and-black sport "
          "motorcycle lying in the foreground; Mert holds a ringing phone",
          "Gün batımında kaldırımda oturan Mert ve Ali, ön planda hasarlı motor, Mert'in elinde çalan telefon."),
   yakinda=("cadde", ["mert", "ali"],
            "Silhouettes of Mert and Ali riding the sport motorcycle against a blazing sunset, seen from behind, the road ahead disappearing into "
            "shadow; a single streetlight flickers on",
            "Gün batımına karşı motor üstünde iki silüet; yol karanlığa uzanıyor."),
   tiktok="Ödünç motorla ilk tur... ve ilk kaza 🏍️💥 #JozhStudios",
   ig=("Yeni eve çıktık, hayallerimiz büyük, cebimiz boş. Komşumuz Cemil Bey motorunu bir saatliğine verdi... "
       "Ama bir köpek, bir fren ve bir kamyonet her şeyi değiştirdi. 🏍️\n\nİkimiz de kasklıydık, iyiyiz. Motor... değil.\n\n"
       "Telefonda Cemil Abi. Sence açmalı mıyız?"),
   tags=["#Malatya", "#Motosiklet"],
   son="Mert'in telefonu çalıyor, ekranda 'Cemil Abi' yazıyor. Açacaklar mı?",
   teaser="Bir saatlik ödünç motor, bir yan sokak ve hayatlarını değiştirecek bir telefon. Bölüm 1: Kaza. Pek yakında.")

# ======================================================================= VİDEO 2
EP(2, None, "800.000 TL",
   "Cemil Bey hasarlı motoru görür ve şartını söyler: sıfır bedeli 800.000 TL, süre bir hafta.",
   "Mert ve Ali hasarlı motoru apartmanın bahçesine iterek getirir. Cemil Bey merdivenlerden iner ve motoru görünce donar. Kaportayı, "
   "farı, gidonu tek tek inceler. Ali tamir masrafını karşılamayı teklif eder ama Cemil Bey'in cevabı nettir: 'Bu motorun sıfır fiyatı 800 bin TL. "
   "Ben tamir edilmiş motor istemiyorum. Bana motorun sıfır bedelini getirin, motor sizin olsun.' Bir hafta süre verir. Gece evde Ali "
   "hesap yapar: günde 114 bin lira. Mert ise yerde yatıp tavana bakar ve 'bir fikrim var' der.",
   {"otopark": ("Apartman bahçesi", OTOPARK), "ev": ("Yeni ev, salon", EV)},
   [
       S("19:20 akşam", "otopark", ["mert", "ali"], "Motoru İterek Getirmek",
         "Hasarlı motoru apartmanın bahçesine iterek getirirler. Ali umutlu, Mert saklamanın yollarını düşünüyor.",
         "Mert and Ali push the damaged motorcycle through the open iron gate into the courtyard, one on each side, the bent handlebar wobbling; "
         "they park it on its stand and step back to look at it.",
         [("ali", "Belki tamir edilir.", "hopeful, quiet"),
          ("mert", "Belki fark etmez.", "nervous joke")],
         "static wide shot from inside the courtyard as they come through the gate"),
       S("19:30 akşam", "otopark", ["mert", "ali", "cemil"], "Bu Ne?",
         "Cemil Bey apartmandan çıkar, motoru görünce olduğu yerde durur. Mert anlatmaya çalışır.",
         "Cemil Bey steps out of the apartment entrance, sees the damaged motorcycle and stops dead; his keys slip from his fingers and dangle on the "
         "key ring; Mert raises both palms and steps forward to explain while Ali stays half a step behind him.",
         [("cemil", "Bu ne?", "low, cold"),
          ("mert", "Bir köpek çıktı abi, ona çarpmamak için...", "rushed, apologetic")],
         "static over-the-shoulder shot from behind the motorcycle toward Cemil Bey"),
       S("19:32 akşam", "otopark", ["ali", "cemil"], "Hasar Tespiti",
         "Cemil Bey çömelip kaportayı, farı ve gidonu inceler. Ali tamir masrafını karşılamayı teklif eder.",
         "Cemil Bey crouches next to the damaged motorcycle and runs two fingers slowly along the cracked fairing, then taps the broken headlight; "
         "Ali stands beside him with his hands clasped in front of him.",
         [("cemil", "Kaporta gitmiş, far gitmiş, gidon eğri.", "flat, counting"),
          ("ali", "Tamir masrafını biz karşılarız Cemil Bey.", "polite, sincere")],
         "slow lateral dolly along the motorcycle at knee height"),
       S("19:34 akşam", "otopark", ["mert", "ali", "cemil"], "Sıfır Bedeli",
         "Cemil Bey ayağa kalkar ve şartını söyler: tamir istemiyor, motorun sıfır bedelini istiyor.",
         "Cemil Bey stands up slowly, wipes his fingers on a handkerchief and looks Mert and Ali in the eye one after the other while speaking; "
         "Mert's mouth falls slightly open and Ali stops breathing.",
         [("cemil", "Bu motorun sıfır fiyatı 800 bin TL. Ben tamir edilmiş motor istemiyorum. Bana motorun sıfır bedelini getirin, motor sizin olsun.",
           "slow, firm, every word deliberate")],
         "slow push-in to a close-up of Cemil Bey's face"),
       S("19:35 akşam", "otopark", ["mert", "ali", "cemil"], "Bir Hafta",
         "Cemil Bey bir hafta süre verip içeri girer. Mert ve Ali şokla birbirine bakar.",
         "Cemil Bey turns and walks back into the building with his keys jingling; Mert and Ali stay frozen, then slowly turn their heads to look at "
         "each other.",
         [("cemil", "Bir haftanız var.", "without turning back"),
          ("mert", "Sekiz yüz bin mi dedi?", "whisper"),
          ("ali", "Sekiz yüz bin dedi Mert.", "whisper")],
         "static medium two-shot, Cemil Bey exits through the background door"),
       S("21:00 iç-gece", "ev", ["mert", "ali"], "Günde 114 Bin",
         "Gece evde Ali deftere hesap yapar: 800.000 bölü 7, günde 114 bin. Mert yerde yatıyor. Sonra bir fikri olduğunu söyler.",
         "Ali sits at the coffee table writing numbers in a small brown leather ledger notebook with a black pen and then stares at the page; Mert lies "
         "flat on the rug staring at the ceiling, then suddenly sits up and points at Ali.",
         [("ali", "Günde yüz on dört bin lira kazanmamız lazım.", "numb"),
          ("mert", "Ali... bir fikrim var.", "sudden, intense"),
          ("ali", "Korkuyorum.", "deadpan")],
         "static high-angle shot looking down at both of them",
         kurgu="Ekrana yazı ekle (kurguda): 800.000 ÷ 7 = 114.286 TL / GÜN"),
   ],
   ay="Mayıs sonu", hava="açık",
   kapak=("otopark", ["cemil", "mert", "ali"],
          "Cemil Bey stands tall in the foreground in evening light, pointing at the damaged motorcycle; Mert and Ali stand behind it looking "
          "terrified, Ali gripping Mert's sleeve",
          "Ön planda motoru işaret eden Cemil Bey, arkada korkmuş Mert ve Ali."),
   yakinda=("otopark", ["cemil"],
            "Cemil Bey's stern face half-lit by a single courtyard lamp, his silhouette looming over the damaged motorcycle in deep shadow, his "
            "gold watch catching the light",
            "Avlu lambasının yarısını aydınlattığı sert bir yüz ve gölgede hasarlı motor."),
   tiktok="Sıfır fiyatı 800 bin. Süre: 1 hafta. 😳 #JozhStudios",
   ig=("Cemil Bey motoru gördü. Tamir istemiyor. 'Sıfır bedelini getirin, motor sizin olsun.' 💸\n\n"
       "Bir haftamız var. Ali hesapladı: günde 114 bin lira kazanmamız lazım. Mert'in ise bir fikri var... 😅\n\n"
       "Sizce o fikir ne?"),
   tags=["#800Bin", "#Malatya"],
   son="Mert'in bir fikri var. Ali korkuyor.",
   teaser="Bir motorun sıfır fiyatı ve bir haftalık süre. Bölüm 2: 800.000 TL. Pek yakında.")

# ======================================================================= VİDEO 3
BANKA = ("the sidewalk in front of a modern bank branch on a Malatya street: a glass facade with frosted panels and no readable signs, "
         "a stone bench, a young tree and passing cars far in the background")
BALKON = ("the small balcony of their apartment at night: a metal railing, two plastic stools, a potted mint plant, and the lights of "
          "Malatya's apartment blocks spread below toward dark hills")
EP(3, None, "Para Arayışı",
   "Mert ve Ali ailelerinden borç istemeye kalkar; ama aileler de onlardan para ister.",
   "Ertesi sabah ikili 'kimden isteriz' listesi yapar. Mert annesini arar ama Hatice'nin elektrik faturası gelmiştir ve oğlundan iki bin "
   "lira ister. Ali babasını arar; Hasan'ın sera kredisi taksiti yaklaşmıştır. Ali elindeki son parayı babasına gönderir. Kumbaralar "
   "boşaltılır: dört bin üç yüz on iki lira. Bankadan kredi çıkmaz. Gece balkonda Ali aileleri için üzülür; Mert ise kararını verir: "
   "'Kendi paramızı kendimiz kazanacağız.' Ve dizüstü bilgisayarı açar.",
   {"ev": ("Yeni ev, salon", EV), "banka": ("Banka önü", BANKA), "balkon": ("Balkon", BALKON)},
   [
       S("10:00 iç-gündüz", "ev", ["mert", "ali"], "Kimden İsteriz?",
         "Sabah koltukta oturup telefonlarına bakarak borç listesi yaparlar. Mert'e göre annesi onu kırmaz.",
         "Mert and Ali sit side by side on the grey sofa, each holding a phone; Mert taps his phone confidently and lifts it to call, while Ali "
         "takes a deep breath and scrolls to his father's number.",
         [("mert", "Önce annem. Annem beni asla kırmaz.", "confident"),
          ("ali", "Ben de babamı arıyorum.", "hesitant")],
         "static medium two-shot from the coffee table"),
       S("10:05 iç-gündüz", "ev", ["mert", "~hatice"], "Annemin Faturası",
         "Mert annesini arar ama daha derdini anlatamadan annesi ondan elektrik faturası için para ister.",
         "Mert holds the phone to his ear, opens his mouth to speak, then his confident smile slowly collapses as he listens; he closes his eyes "
         "and drops his head back against the sofa. His lips stay closed while his mother speaks.",
         [("hatice", "Oğlum tam zamanında aradın! Elektrik faturası gelmiş, sende iki bin var mı?", "warm, relieved, from the phone speaker"),
          ("mert", "Var anne... yollarım.", "defeated, gentle")],
         "slow push-in to a close-up of Mert's face"),
       S("10:12 iç-gündüz", "ev", ["ali", "~hasan"], "Babamın Serası",
         "Ali babasını arar; Hasan sera kredisinin taksitinden söz eder. Ali kendi derdini söyleyemez ve son birikimini gönderir.",
         "Ali sits on the edge of the sofa with the phone at his ear, nodding silently; then he lowers the phone, opens a banking screen and presses "
         "send with his thumb, staring at the screen. His lips stay closed while his father speaks.",
         [("hasan", "Oğlum, seranın taksiti yaklaştı. Biraz bir şey var mı sende?", "quiet, ashamed, from the phone speaker"),
          ("ali", "Var baba. Şimdi gönderiyorum.", "soft, steady")],
         "static medium close-up from the side"),
       S("13:00 iç-gündüz", "ev", ["mert", "ali"], "Kumbaralar",
         "Öğlen bütün kumbaraları ve ceplerini masaya boşaltırlar. Ali sayar: 4.312 lira.",
         "Mert turns a glass jar upside down and coins pour noisily onto the coffee table; Ali sorts the coins and a few banknotes into small piles "
         "with one finger, then writes the total in the brown leather notebook.",
         [("ali", "Toplam dört bin üç yüz on iki lira.", "flat"),
          ("mert", "Yetmiş ikisi bozuk para.", "deadpan comic")],
         "top-down static shot over the coffee table"),
       S("16:40 ikindi", "banka", ["mert", "ali"], "Kredi Yok",
         "Bankadan çıkarlar: öğrenci oldukları ve düzenli gelirleri olmadığı için kredi verilmemiştir.",
         "Mert pushes the glass door open and walks out of the bank with a folded paper in his hand, Ali right behind him; Mert crumples the paper "
         "slowly and both sit down heavily on the stone bench.",
         [("mert", "Kredi vermediler. 'Geliriniz yok' dediler.", "bitter"),
          ("ali", "Haklılar. Yok.", "tired, honest")],
         "static wide shot from across the sidewalk, slight push-in as they sit"),
       S("22:00 gece", "balkon", ["mert", "ali"], "Kendi Paramız",
         "Gece balkonda şehrin ışıklarına bakarlar. Ali aileleri için üzülür. Mert kararını verir ve dizüstü bilgisayarını açar.",
         "Mert and Ali sit on plastic stools on the balcony looking at the city lights; Ali rubs his face; Mert opens a laptop on his knees, its "
         "screen lighting his face, and turns it toward Ali with a determined look.",
         [("ali", "Ailelerimiz bize muhtaç, biz onlara değil.", "quiet, heavy"),
          ("mert", "O zaman kendi paramızı kendimiz kazanacağız.", "determined, low")],
         "slow push-in from behind their shoulders toward the laptop glow"),
   ],
   ay="Mayıs sonu", hava="açık",
   kapak=("ev", ["mert", "ali"],
          "Mert and Ali sit on the sofa surrounded by a pile of coins and an empty glass jar on the table, both holding phones to their ears "
          "with comically devastated expressions",
          "Bozuk paraların ortasında telefonla konuşan, yıkılmış ama komik yüz ifadeli Mert ve Ali."),
   yakinda=("balkon", ["mert", "ali"],
            "Two silhouettes on a night balcony above the city lights, the only bright light is a laptop screen glowing on Mert's face",
            "Gece balkonda iki silüet, yüzü aydınlatan tek ışık bir dizüstü bilgisayar."),
   tiktok="Anneme borç istemek için aradım... annem benden istedi 😂 #JozhStudios",
   ig=("Plan basitti: ailelerimizden borç isteyecektik. 📞\n\nAnnemin elektrik faturası gelmiş. Ali'nin babasının sera taksiti yaklaşmış. "
       "Kumbaralardan 4.312 lira çıktı, bankadan kredi çıkmadı.\n\nGece balkonda tek karar kaldı: kendi paramızı kendimiz kazanacağız. Ama nasıl?"),
   tags=["#Aile", "#Malatya"],
   son="Mert dizüstü bilgisayarı açıyor: 'Kendi paramızı kendimiz kazanacağız.'",
   teaser="Herkesten borç istemeye çıktılar, herkes onlardan istedi. Bölüm 3: Para Arayışı. Pek yakında.")

# ======================================================================= VİDEO 4
APART_ONU = ("the front steps of their Malatya apartment building in the early evening: cream walls, a glass entrance door, a row of "
             "mailboxes, a young plane tree and a quiet street behind")
ALICI = ("ALICI", "BUYER, a 30-year-old Turkish man, slim, short curly black hair, round glasses, wearing a grey hoodie and jeans",
         "adult male voice, friendly and quick, standard Turkish")
EP(4, None, "Ticaret Fikri",
   "İnternette al-sat fırsatlarını keşfeden ikili, ellerindeki her şeyi satıp 100.000 TL'lik bir kasa kurar.",
   "Sabah Mert ikinci el ilanlarını tararken aynı espresso makinesinin iki ilan arasında dört bin beş yüz lira fark ettiğini görür. "
   "Ali hemen defterine alış, satış ve gider sütunlarını çizer: kâr, aradaki farktır. Malatya'nın en değerli malının kayısı olduğunu "
   "düşünüp kayısı pazarında fiyat toplarlar: gün kurusu toptan 240 lira, internette 350'nin üstünde. Sermaye için Mert üç yıldır "
   "biriktirdiği oyun bilgisayarını, gitarını ve bisikletini satar; Ali burs birikimini koyar. Gece masaya konan para tam 100.000 TL'dir. "
   "KASA ilk kez açılır.",
   {"ev": ("Yeni ev, salon", EV), "pazar": ("Malatya Kayısı Pazarı", PAZAR), "onu": ("Apartman önü", APART_ONU)},
   [
       S("08:30 iç-gündüz", "ev", ["mert", "ali"], "Aynı Makine, İki Fiyat",
         "Mert ikinci el ilanlarında aynı espresso makinesini iki farklı fiyattan bulur: 6.500 ve 11.000 lira.",
         "Mert sits cross-legged on the sofa with the laptop, scrolling, then freezes and turns the screen toward Ali, who leans in from the "
         "armrest holding a cup of tea; Mert taps the screen twice with his finger.",
         [("mert", "Aynı makine, iki ilan. Arada dört bin beş yüz lira fark var!", "excited, fast"),
          ("ali", "Kargo, zaman, risk... Ama dur, mantıklı.", "skeptical, then curious")],
         "slow push-in over Ali's shoulder toward the laptop",
         kurgu="Ekrandaki ilanlar kurguda bulanık gösterilir; gerçek site adı ya da logo kullanma."),
       S("08:45 iç-gündüz", "ev", ["mert", "ali"], "Ali'nin Defteri",
         "Ali kahverengi deri defterine üç sütun çizer: alış, satış, gider. Kâr, aradaki farktır.",
         "Ali opens the small brown leather notebook on the coffee table and draws three neat columns with a black pen, then turns the notebook "
         "toward Mert; Mert grins and offers a handshake, and Ali shakes it.",
         [("ali", "Alış, satış, gider. Aradaki fark kâr. Her kuruşu buraya yazacağız.", "calm, clear"),
          ("mert", "Sen hesap, ben pazarlık.", "grinning")],
         "top-down shot on the notebook, slowly tilting up to their faces"),
       S("11:00 sabah", "pazar", ["mert", "ali", "ramazan"], "Kayısı Pazarında Keşif",
         "Malatya'nın en değerli malı kayısı. Pazarda Ramazan Amca'ya gün kurusunun toptan fiyatını sorarlar: 240 lira.",
         "Mert picks up a sun-dried apricot from an open sack and smells it, Ali holds the notebook ready; behind the stall Ramazan places a "
         "handful of apricots on a hanging scale and points at it.",
         [("mert", "Amca, gün kurusunun toptanı kaç?", "friendly"),
          ("ramazan", "Kilosu iki yüz kırk. Ama sizin gibi gençlere pazarlık payı da var.", "warm, teasing")],
         "slow tracking shot along the stall, ending on a three-shot",
         kurgu="Fiyat araştırması: toptan 240 TL/kg, internette 1 kg paket 350 TL üstü."),
       S("14:00 iç-gündüz", "ev", ["mert", "ali"], "Bilgisayarın Fişi",
         "Sermaye lazım. Mert üç yıldır biriktirip aldığı oyun bilgisayarına bakar; Ali vazgeçirmeye çalışır, Mert fişi çeker.",
         "Mert stands in front of a desk with a gaming computer tower and lays his hand flat on top of it; Ali steps toward him with an open hand "
         "to stop him, but Mert reaches down and pulls the power plug from the wall socket.",
         [("ali", "Satma, başka bir yol buluruz.", "pleading"),
          ("mert", "Yol bu Ali. Üç yıl biriktirdim, bir günde satarım.", "decisive, a bit emotional")],
         "slow dolly-in from behind Ali toward Mert"),
       S("18:20 akşam", "onu", ["mert", "ali", "alici"], "Her Şeyi Satmak",
         "Apartman önünde alıcı bilgisayarı alır, parayı Mert'e verir. Gitar ve bisiklet de satılmıştır; Ali burs birikimini ortaya koyar.",
         "The buyer carries the computer tower in a cardboard box with both arms and nods; Mert receives a thick white envelope with both hands; "
         "Ali stands beside him holding his phone with a banking app open and nods firmly.",
         [("mert", "Bilgisayar otuz sekiz, gitarla bisiklet on yedi bin.", "counting, proud"),
          ("ali", "Benim birikimim de kırk beş bin.", "steady")],
         "static medium three-shot at eye level on the front steps"),
       S("21:30 iç-gece", "ev", ["mert", "ali"], "Kasa Açıldı",
         "Gece masaya zarfı ve telefondaki bakiyeyi koyarlar: tam 100.000 TL. Ali defterin ilk sayfasına yazar: KASA. Kasa göstergesi ilk kez ekranda belirir.",
         "Mert places the thick white envelope on the coffee table next to Ali's phone; Ali writes slowly on the first page of the brown leather "
         "notebook and underlines it twice; Mert reaches toward the envelope and Ali gently pushes his hand away.",
         [("mert", "Yüz bin lira. Hayatımda ilk kez bu kadar paraya dokunuyorum.", "awed"),
          ("ali", "Dokunma. Çalıştıracağız.", "smiling, firm")],
         "slow push-in from table height",
         t=T("acilis", 100000, "Başlangıç kasası: Ali'nin burs birikimi 45.000 + bilgisayar 38.000 + gitar ve bisiklet 17.000"),
         kurgu="KASA sayacı ilk kez bu sahnede ekrana gelir (sahnenin altındaki kasa prompt'u)."),
   ],
   misafir={"ramazan": RAMAZAN, "alici": ALICI}, ay="Mayıs sonu", hava="açık",
   kapak=("ev", ["mert", "ali"],
          "Mert and Ali at the coffee table at night, a thick envelope and the open brown leather notebook between them, Mert's eyes wide with "
          "excitement, Ali holding the pen with a proud small smile, warm lamp light",
          "Gece masada zarf ve açık defter; heyecanlı Mert, gururlu Ali."),
   yakinda=("pazar", ["mert"],
            "Mert's face lit by a single strip of sunlight in the dim apricot market, holding one golden dried apricot up to the light like a "
            "precious stone, sacks of apricots fading into shadow",
            "Loş pazarda tek ışık şeridinde bir kayısıyı mücevher gibi tutan Mert."),
   tiktok="Bilgisayarımı sattım, kasayı kurduk: 100.000 TL 💰 #JozhStudios",
   ig=("Aynı ürün, iki ilan, 4.500 lira fark. İşte o an anladık: al-sat. 📈\n\n"
       "Sermaye için oyun bilgisayarımı, gitarımı, bisikletimi sattım; Ali burs birikimini koydu. Masada tam 100.000 TL var. "
       "Ali defterin ilk sayfasına yazdı: KASA.\n\nYarın sabah ilk alış. Sizce neyle başlamalıyız?"),
   tags=["#AlSat", "#Kayısı"],
   son="Kasa açıldı: 100.000 TL. Yarın sabah ilk alış.",
   teaser="Ellerindeki her şeyi satıp tek bir kasa kurdular. Bölüm 4: Ticaret Fikri. Pek yakında.")

# ======================================================================= VİDEO 5
SATICI_EV = ("the entrance of an older Malatya apartment building at noon: a worn marble step, a green metal door, a few potted plants, "
             "and a quiet narrow street")
KURUYEMIS = ("a small traditional dried-fruit and nut shop in Malatya's old bazaar: wooden shelves of glass jars, open sacks of "
             "apricots, walnuts and pistachios, a brass scale on the counter and warm light from a single lamp")
KAFE = ("a small modern café on a Malatya street corner: light wood counter, an empty spot behind the counter for an espresso machine, "
        "plants by the window and late-afternoon light")
SATICI = ("SATICI", "SELLER, a 26-year-old Turkish man, tall and sleepy-looking, messy brown hair, dark circles under his eyes, wearing a "
          "faded blue t-shirt and grey sweatpants", "young male voice, slow and sleepy, casual Turkish")
NURAY = ("NURAY ABLA", "NURAY, a 45-year-old Turkish woman shopkeeper, sturdy build, sharp kind eyes, short dark hair with a few grey "
         "strands, small gold earrings, wearing a navy shop apron over a beige blouse", "middle-aged female voice, brisk practical alto, Malatya Turkish")
ZEYNEP = ("ZEYNEP", "ZEYNEP, a 28-year-old Turkish woman café owner, slim, long dark brown hair in a low ponytail, wearing a black apron "
          "over a white shirt", "young female voice, bright and friendly, standard Turkish")
EP(5, None, "İlk Ticaret",
   "İlk gün: kayısı alırlar, paketlerler, ikinci el bir espresso makinesi alıp satarlar. Kasa ilk kez büyür ve kapı çalar.",
   "Sabah Ramazan Amca'dan 80 kilo gün kurusu kayısı alırlar; Mert'in pazarlığı tutmaz ama kutular hediye olur. Evde bir kiloluk paketler "
   "hazırlayıp paylaşırlar, ilk siparişler gelir. Öğlen ilandaki espresso makinesini 6.500 liraya alırlar. Çarşıda Nuray Abla 40 kiloyu "
   "300'den alır. Akşam Zeynep'in yeni kafesi makineyi 11.000'e satın alır. Gece Ali kırk paketi kargoya verdiklerini yazarken kapı çalar: "
   "bir hafta dolmuştur ve gelen Cemil Bey'dir.",
   {"pazar": ("Malatya Kayısı Pazarı", PAZAR), "ev": ("Yeni ev, salon", EV), "satici": ("İlan sahibinin apartmanı", SATICI_EV),
    "kuruyemis": ("Çarşıda kuruyemişçi", KURUYEMIS), "kafe": ("Zeynep'in kafesi", KAFE)},
   [
       S("08:30 sabah", "pazar", ["mert", "ali", "ramazan"], "İlk Pazarlık",
         "Ramazan Amca'dan 80 kilo gün kurusu kayısı. Mert 220 ister, Ramazan 240'ta kalır ama kutuları hediye eder.",
         "Ramazan weighs a big sack of dried apricots on a floor scale; Mert holds up two fingers and leans in to bargain, Ramazan laughs and "
         "shakes his head, then pats a stack of empty cardboard boxes; Ali counts banknotes onto the counter.",
         [("mert", "Seksen kilo alırsak iki yüz yirmi olur mu?", "bargaining, charming"),
          ("ramazan", "İki yüz kırk evladım. Ama kutular benden.", "laughing")],
         "static medium three-shot, slight push-in on the scale",
         t=U(80, "kg", 240, "alis", "Gün kurusu Malatya kayısısı ({adet} kg x {fiyat} TL)"),
         kurgu="Ekrana yazı ekle (kurguda): DÖRDÜNCÜ GÜN"),
       S("10:30 iç-gündüz", "ev", ["mert", "ali"], "Paketler ve İlk Siparişler",
         "Evde kayısıları bir kiloluk paketlere doldururlar; ambalaj ve etiket 1.800 lira. Paylaşımdan sonra ilk siparişler gelir.",
         "Mert scoops apricots into clear one-kilo bags on a kitchen scale and Ali seals them with a sticker; Ali's phone on the table buzzes "
         "again and again, he picks it up and turns it to Mert with a surprised smile.",
         [("ali", "On iki sipariş geldi bile!", "surprised, happy"),
          ("mert", "Dedim sana, Malatya kayısısı kendini satar.", "proud")],
         "static medium shot across the table full of bags",
         t=T("diger_gider", 1800, "Ambalaj poşeti, etiket ve koli")),
       S("12:00 öğle", "satici", ["mert", "ali", "satici"], "Espresso Makinesi",
         "İlandaki espresso makinesini almaya gelirler. Mert pompasını kontrol eder, 6.500 liraya alırlar.",
         "The sleepy seller holds a stainless steel espresso machine in both arms at his door; Mert lifts the lid of the water tank and looks "
         "inside carefully, then nods to Ali, who hands over the money.",
         [("mert", "Pompası sağlam mı?", "suspicious"),
          ("satici", "Hiç bozulmadı. Sadece çok kahve içiyordum.", "sleepy, flat")],
         "static medium three-shot at the doorway",
         t=T("alis", 6500, "İkinci el espresso makinesi")),
       S("15:00 ikindi", "kuruyemis", ["ali", "nuray"], "Çarşıda İlk Satış",
         "Çarşıda Nuray Abla 40 kilo kayısıyı kilosu 300'den alır. Pazarlığı bu kez Ali yapar.",
         "Nuray tastes an apricot from an open sack and nods slowly; Ali stands at the counter with the brown notebook, writes a number and "
         "turns it toward her; she taps the page and pulls cash from the drawer.",
         [("nuray", "Kırk kilonun hepsini alırım, ama üç yüzden fazla vermem.", "brisk"),
          ("ali", "Üç yüz olsun Nuray Abla, hayırlı olsun.", "polite, pleased")],
         "slow push-in over the counter",
         t=U(40, "kg", 300, "satis", "Kuru kayısı, çarşıda toptan ({adet} kg x {fiyat} TL)")),
       S("18:00 akşam", "kafe", ["mert", "zeynep"], "Makine Yeni Yuvasında",
         "Espresso makinesi, yeni açılan Zeynep'in kafesine 11.000 liraya satılır. Mert ilk kahveyi çeker.",
         "Mert sets the stainless steel espresso machine on the light wood counter; Zeynep pulls the first shot into a small cup, tastes it and "
         "smiles, then slides an envelope across the counter to Mert.",
         [("zeynep", "Tam aradığım gibi. On bir bin, anlaştık.", "pleased"),
          ("mert", "Bu kafe bu makineyle çok sevilecek.", "charming")],
         "static medium two-shot across the counter",
         t=T("satis", 11000, "Espresso makinesi, Zeynep'in kafesine")),
       S("21:30 iç-gece", "ev", ["mert", "ali"], "Kapı Çalıyor",
         "Gece Ali kırk paketin kargoya verildiğini yazar: 14.400 lira. Tam o sırada kapı çalar. Bir hafta dolmuştur.",
         "Ali writes in the brown notebook at the coffee table and shows the page to Mert, who raises both fists in celebration; then three slow, "
         "heavy knocks sound at the door and both freeze and turn toward it.",
         [("ali", "Kırk paket sipariş: on dört bin dört yüz lira!", "excited"),
          ("mert", "Bu saatte kim?", "whisper, uneasy")],
         "static medium shot from behind the sofa toward the front door",
         t=U(40, "paket", 360, "satis", "Takipçi siparişi: 1 kg kayısı paketi ({adet} x {fiyat} TL, kargo dahil)"),
         kurgu="Ekrana yazı ekle (kurguda): BİR HAFTA DOLDU. Kapının arkasındaki ses: Cemil Bey (bir sonraki videoda)."),
   ],
   misafir={"ramazan": RAMAZAN, "satici": SATICI, "nuray": NURAY, "zeynep": ZEYNEP}, ay="Mayıs sonu", hava="açık",
   kapak=("pazar", ["mert", "ali", "ramazan"],
          "Mert and Ali stand at the apricot stall shaking hands with Ramazan over a big sack of golden dried apricots, strips of sunlight falling "
          "through the market roof, Mert beaming, Ali holding the brown notebook",
          "Kayısı pazarında Ramazan Amca'yla el sıkışan Mert ve Ali."),
   yakinda=("ev", ["mert", "ali"],
            "Mert and Ali frozen on the sofa at night, lit only from the side by a lamp, both staring at a dark front door with a thin strip of "
            "hallway light under it and a long shadow of someone standing outside",
            "Gece kapının altından sızan ışık ve bir gölge; donup kalmış Mert ve Ali."),
   tiktok="İlk günümüz: 4 alışveriş, 3 satış ve kapıda biri 🚪 #JozhStudios",
   ig=("İlk ticaret günü! 🍑 Ramazan Amca'dan 80 kilo kayısı aldık, paketledik, Nuray Abla'ya ve size sattık. "
       "Bir de ikinci el espresso makinesi alıp Zeynep'in yeni kafesine sattık. ☕\n\n"
       "Kasa ilk günün sonunda: {KASA}. Ama bir hafta doldu... ve kapı çalıyor.\n\nAli'nin defteri her şeyi yazıyor. Siz olsanız ne alırdınız?"),
   tags=["#İlkTicaret", "#MalatyaKayısısı"],
   son="Bir hafta doldu. Kapı çalıyor.",
   teaser="İlk alış, ilk satış, ilk kâr... ve kapıda bekleyen hesap. Bölüm 5: İlk Ticaret. Pek yakında.")

# ======================================================================= VİDEO 6
HARITA = ("the same rooftop terrace in Malatya: on the small plastic table lies a large unfolded paper map of Turkey with colored regions "
          "and small red dots, without any readable text, held down by two tea glasses")
EP(6, None, "81 Şehir Duyurusu",
   "Mert ve Ali kameraya dönüp Cemil Bey'le yaptıkları anlaşmayı ve Türkiye'nin 81 ilini gezme hedeflerini duyurur.",
   "Cemil Bey o gece teklifi dinlemiştir: 81 ili gezip ticaret yapacak, her bölge bitince bir taksit ödeyeceklerdir. Kabul eder ama "
   "tek bir taksit gecikirse senet mahkemeye gidecektir. Sabah Mert ve Ali kameraya döner: kim olduklarını, borçlarını ve planlarını "
   "anlatırlar. Doğu Anadolu'dan başlayıp yedi bölgeyi gezecek; şehirlerin kültürünü, tarihini, yemeklerini, yerel işletmelerini ve "
   "ticaret fırsatlarını keşfedeceklerdir. Kasaları ekranda olacak. İşletmeleri iş birliği için davet eder, reklamı her zaman açıkça "
   "söyleyeceklerine söz verirler. Gün batımında sırt çantalarıyla son çağrıyı yaparlar: ilk durak Malatya.",
   {"ev": ("Yeni ev, salon", EV), "cati": ("Apartman çatı terası", CATI), "harita": ("Çatı terası, harita", HARITA)},
   [
       S("09:00 iç-gündüz", "ev", ["mert", "ali"], "Merhaba, Biz Mert ve Ali",
         "Kameraya doğrudan konuşurlar: kendilerini tanıtıp başlarına geleni özetlerler.",
         "Mert and Ali sit on the grey sofa facing the camera directly like vloggers; Mert waves at the lens with a big smile, Ali gives a small "
         "polite nod, then Mert makes a crashing gesture with his hands.",
         [("mert", "Merhaba! Ben Mert, bu Ali. Ödünç aldığımız bir motoru... kazayla hurdaya çevirdik.", "cheerful, embarrassed"),
          ("ali", "Ve sahibine sekiz yüz bin lira borçluyuz.", "dry")],
         "static medium two-shot, both looking straight into the lens"),
       S("09:02 iç-gündüz", "ev", ["mert", "ali"], "Anlaşma",
         "Cemil Bey'le yaptıkları anlaşmayı anlatırlar: 81 il, her bölge sonunda taksit.",
         "Ali holds up a single folded sheet of paper toward the camera and taps it, Mert leans into the frame and points at it with two fingers, "
         "both still speaking to the lens.",
         [("mert", "Cemil Abi'ye bir teklif yaptık: Türkiye'nin seksen bir ilini gezip ticaret yapacağız.", "energetic"),
          ("ali", "Her bölge bitince bir taksit. Kabul etti.", "serious")],
         "slow push-in toward the paper and their faces"),
       S("18:00 ikindi", "harita", ["mert", "ali"], "Yedi Bölge, Seksen Bir İl",
         "Çatı terasında Türkiye haritasını açarlar. Rota: Doğu Anadolu'dan başlayıp yedi bölge.",
         "Ali smooths the large paper map of Turkey on the table with both hands; Mert places his finger on the eastern part of the map and "
         "slowly slides it westward across the country, both glancing between the map and the camera.",
         [("mert", "Doğu Anadolu'dan başlıyoruz. Yedi bölge, seksen bir il.", "excited"),
          ("ali", "Her şehrin kültürünü, tarihini ve yemeklerini göreceğiz.", "warm")],
         "slow crane-down from above the map to their faces",
         kurgu="Haritadaki rota çizgisini kurguda animasyonla ekle (Malatya'dan başlayan kırmızı çizgi)."),
       S("18:20 gün batımı", "cati", ["mert", "ali"], "Kasamız Ekranda",
         "Ticaret kısmını anlatırlar: yerel esnafla tanışacak, ürün alıp satacaklar; kasa her zaman ekranda olacak.",
         "Mert stands by the parapet and speaks to the camera, counting on his fingers; Ali stands beside him holding the brown notebook open "
         "toward the lens and taps the page.",
         [("mert", "Yerel esnafla tanışacak, ürün alıp satacağız.", "confident"),
          ("ali", "Kasamız hep ekranda olacak. Kazancı da zararı da göreceksiniz.", "honest")],
         "static medium two-shot with the city behind them"),
       S("18:40 gün batımı", "cati", ["mert", "ali"], "İşletmelere Çağrı",
         "İşletmeleri iş birliğine davet ederler ve reklamın her zaman açıkça söyleneceğine söz verirler.",
         "Ali steps forward toward the camera with an open, inviting hand gesture; Mert raises his right hand like taking an oath, then both "
         "smile.",
         [("ali", "Şehrinizde bir işletmeniz varsa ve bizi ağırlamak isterseniz bize yazın.", "polite, inviting"),
          ("mert", "Reklam olursa da açık açık söyleyeceğiz. Söz!", "sincere, playful")],
         "slow push-in to a medium close-up"),
       S("19:40 gün batımı", "cati", ["mert", "ali"], "İlk Durak",
         "Sırt çantalarını omuzlayıp son çağrıyı yaparlar: takip, beğeni ve şehir yorumları. İlk durak Malatya.",
         "Mert and Ali swing backpacks onto their shoulders, step side by side toward the camera and point at the lens together, then turn and "
         "look out at the sunset over the city.",
         [("mert", "Takip edin, beğenin, yorumlara şehrinizi yazın!", "energetic"),
          ("ali", "İlk durak Malatya. Yarın sabah başlıyoruz.", "excited, warm")],
         "slow dolly-out and crane-up revealing the city at sunset",
         kurgu="Ekrana yazı ekle (kurguda): JOZH STUDIOS · 81 ŞEHİR. İş birliği için iletişim bilgisini açıklamaya yaz."),
   ],
   ay="Mayıs sonu", hava="açık",
   kapak=("harita", ["mert", "ali"],
          "Mert and Ali lean over the large paper map of Turkey on the rooftop at golden hour, both pointing at the far east of the map and "
          "looking up toward the camera with big confident smiles, the city behind them",
          "Gün batımında çatıda Türkiye haritasının başında, doğuyu işaret eden Mert ve Ali."),
   yakinda=("cati", ["mert", "ali"],
            "Backlit silhouettes of Mert and Ali with backpacks standing on the rooftop edge, facing a huge orange sunset over the city; "
            "their long shadows stretch toward the camera",
            "Gün batımına karşı sırt çantalı iki silüet, gölgeleri kameraya uzanıyor."),
   tiktok="81 il, 7 bölge, 800 bin borç. Yolculuk başlıyor! 🇹🇷 #JozhStudios",
   ig=("Biz Mert ve Ali. 👋 Ödünç bir motoru kazayla hurdaya çevirdik ve sahibine 800.000 TL borçluyuz.\n\n"
       "Anlaşmamız şu: Doğu Anadolu'dan başlayıp Türkiye'nin 81 ilini gezeceğiz. Her şehirde kültürü, tarihi, yemekleri ve yerel esnafı "
       "keşfedip ticaret yapacağız. Kasamız hep ekranda: {KASA}.\n\n"
       "Şehrinizde bir işletmeniz varsa bize yazın; reklam olursa açıkça söyleyeceğiz. Takip et, şehrini yorumlara yaz! 🗺️"),
   tags=["#81İl", "#TürkiyeTuru"],
   son="İlk durak Malatya. Yarın sabah başlıyorlar.",
   teaser="81 il, 7 bölge ve ödenmesi gereken 800 bin lira. Bölüm 6: 81 Şehir Duyurusu. Pek yakında.",
   sponsor="İşletmeler için genel çağrı. Bu videoda hiçbir işletme sponsor olarak gösterilmez.")
