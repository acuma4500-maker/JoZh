# -*- coding: utf-8 -*-
"""Sezon 5 · Büyük Pazar · Marmara (Bölüm 46-56). Ekim. Kamyonetle.
Rota: Bilecik → Bursa → Balıkesir → Çanakkale → Edirne → Kırklareli → Tekirdağ → İstanbul → Yalova → Kocaeli → Sakarya
Kriz: Tekirdağ'da Mert, Ali'ye sormadan sözlü bir toptan teklifini kabul edip 20.000 TL ön ödeme yapar ve 500 kutuluk mal/ambalaj alır.
İstanbul'da toptancı fiyatı yarıya indirir; anlaşma bozulur, ön ödeme yanar. Ali Yalova'ya tek başına gider. Kocaeli'de özür,
Sakarya'da barışma: 500 kutunun 300'ü 'Marmara Kutusu' olarak satılır (her kutuda 200 g Edirne badem ezmesi, 1 Edirne meyve
sabunu, 1 küçük kutu İzmit pişmaniyesi). Kalan 200 kutu Karadeniz'de satılır.
Toptancı kurgusaldır, gerçek bir kişi ya da işletmeyi temsil etmez."""
from ortak import EP, S, T, U

AY = "Ekim"

# ======================================================================= 46 BİLECİK
EP(46, "Bilecik", "Küçük Bir Çadır",
   "Söğüt'te bir başlangıç hikâyesi, lokum satışı ve büyük pazara hazırlık.",
   "Marmara'nın ilk durağı Bilecik. Söğüt'te Ertuğrul Gazi Türbesi'nin çevresinde yürür, bir imparatorluğun küçük bir obadan doğduğunu "
   "anlatan rehberi dinlerler: 'Her büyük iş küçük bir çadırla başlar.' Afyon lokumunun yarısı Söğüt'te bir şekerciye satılır. Öğlen "
   "Bilecik'in taş evli eski sokaklarında yemek yerler. Akşam Mert, Marmara'nın büyük şehirlerinde 'büyük oynamak' istediğini söyler. Ali "
   "Söğüt'teki sözü hatırlatır.",
   {"sogut": ("Söğüt, türbe çevresi", "a calm green park area in Söğüt with old plane trees, a stone path leading to a historic tomb complex "
              "with a dome, autumn leaves on the ground"),
    "sekerci": ("Söğüt'te şekerci", "a traditional candy and Turkish delight shop in Söğüt: glass jars of colorful candies, trays of lokum, "
                "a wooden counter"),
    "sokak": ("Bilecik eski sokakları", "a quiet old street in Bilecik with restored wooden Ottoman houses on stone foundations, autumn trees "
              "and a small lokanta with outdoor tables"),
    "tepe": ("Bilecik manzarası", "a hillside viewpoint above Bilecik at sunset with autumn trees, the town in the valley, the old white "
             "pickup truck parked nearby")},
   [
       S("09:00 sabah", "sogut", ["mert", "ali", "rehber"], "Küçük Bir Oba",
         "Söğüt'te rehber Kemal Bey bir imparatorluğun küçük bir obadan doğduğunu anlatır: 'Her büyük iş küçük bir çadırla başlar.'",
         "The guide walks slowly along the stone path under the plane trees and gestures with one open hand toward the domed tomb; Mert and Ali "
         "walk beside him, Ali taking notes, autumn leaves falling.",
         [("rehber", "Her büyük iş küçük bir çadırla başlar evlatlar. Sabırla büyür.", "warm, storytelling"),
          ("ali", "Bizim çadırımız da bir kamyonet.", "smiling")],
         "slow tracking shot along the path", h="serin"),
       S("11:00 iç-gündüz", "sekerci", ["mert", "sekerci"], "Lokum Söğüt'te",
         "Söğüt'te bir şekerci Afyon lokumunun yarısını, 25 kiloyu alır.",
         "The candy shop owner tastes a piece of cream lokum, nods and lifts the box onto his counter; Mert accepts the money and pops a candy "
         "from a jar into his mouth with a wink.",
         [("sekerci", "Afyon'un kaymaklı lokumu... yirmi beş kilo, dört yüz elliden.", "pleased"),
          ("mert", "Bir şeker de benden olsun. Ah, sizin şekeriniz zaten.", "playful")],
         "static medium two-shot at the counter",
         t=U(25, "kg", 450, "satis", "Afyon lokumu, Söğüt'te şekerciye ({adet} kg x {fiyat} TL)")),
       S("13:00 öğle", "sokak", ["mert", "ali"], "Taş Temelli Evler",
         "Bilecik'in eski sokaklarında öğle yemeği yerler. Ali kasanın Marmara'ya sağlıklı girdiğini söyler.",
         "Mert and Ali sit at an outdoor lokanta table under autumn trees; Ali taps the notebook proudly; Mert looks up at the wooden bay windows "
         "of the old houses.",
         [("ali", "Kasa iyi, kutu fikri iyi, borcun yarısına yaklaştık.", "content"),
          ("mert", "O zaman Marmara'da büyük oynayalım!", "excited")],
         "static medium two-shot at the table", h="serin",
         t=T("yemek", 700, "Öğle yemeği")),
       S("16:00 ikindi", "sogut", ["mert", "ali"], "Büyük Oynamak",
         "Mert büyük şehirlerde büyük anlaşmalar yapmak ister. Ali sabahki sözü hatırlatır.",
         "Mert walks fast ahead on the path, talking with big gestures; Ali stops, picks up a single fallen leaf and holds it up; Mert turns back "
         "and stops.",
         [("mert", "İstanbul'da toptancılarla binlerce kutu konuşuruz!", "ambitious"),
          ("ali", "Küçük çadır Mert. Sabırla büyür. Unutma.", "gentle warning")],
         "static medium two-shot, slow push-in on the leaf", h="serin"),
       S("18:30 gün batımı", "tepe", ["mert", "ali"], "Söz",
         "Tepede gün batarken Mert söz verir: büyük bir karar olursa önce Ali'ye soracak.",
         "Mert and Ali sit on the tailgate of the pickup looking at the valley; Mert holds out his little finger like children making a promise; "
         "Ali laughs and hooks his little finger with his.",
         [("mert", "Büyük karar olursa önce sana sorarım. Söz.", "sincere"),
          ("ali", "Serçe parmak sözü. Çocukken de böyle yapardık.", "nostalgic, smiling")],
         "slow dolly-out revealing the valley", h="serin"),
       S("21:00 akşam", "tepe", ["mert", "ali"], "Bursa'ya",
         "Akşam Bursa yoluna çıkmadan önce Ali kasayı ve stoğu son kez yazar.",
         "Ali writes in the notebook by the pickup's cab light; Mert closes the tailgate and climbs into the driver's seat, then waves Ali in.",
         [("ali", "Yirmi beş kilo lokum kaldı, Bursa'da biter.", "organized"),
          ("mert", "Bursa'da da İskender bekler.", "hungry grin")],
         "static medium shot through the open passenger door",
         t=[T("konaklama", 1200, "Pansiyon, 1 gece"), T("ulasim", 1000, "Yakıt: Kütahya-Bilecik-Bursa")]),
   ],
   misafir={"rehber": ("KEMAL BEY", "KEMAL, a 63-year-old Turkish local guide, tall, a neat grey beard, a tweed flat cap, a brown wool jacket",
                       "elderly male voice, warm storyteller"),
            "sekerci": ("ŞEKERCİ", "CANDY SHOP OWNER, a 57-year-old Turkish man, round, a white mustache, a white shop coat", "mature male voice")},
   ay=AY, hava="serin", urun="Söğüt, Osmaneli ayvası, mermer, ahşap Osmanlı evleri",
   sponsor="Şekerleme, ayva ya da kültür turizmi alanında",
   kapak=("tepe", ["mert", "ali"], "Mert and Ali sit on the tailgate of an old white pickup at sunset hooking their little fingers in a childhood "
          "promise, autumn valley below", "Kamyonetin kasasında serçe parmak sözü veren Mert ve Ali."),
   yakinda=("sogut", ["ali"], "A single autumn leaf held up between two fingers in the foreground, golden backlight, a domed tomb and plane trees "
            "softly blurred behind", "İki parmak arasında tutulan tek bir sonbahar yaprağı."),
   tiktok="Her büyük iş küçük bir çadırla başlar ⛺ #JozhStudios",
   ig=("Marmara başladı! 🍂 Söğüt'te rehberimiz Kemal Bey'in sözü: 'Her büyük iş küçük bir çadırla başlar.'\n\n"
       "Lokumun yarısı Söğüt'te bir şekerciye gitti. Mert büyük oynamak istiyor, Ali 'küçük çadır' diyor. Serçe parmak sözü verdiler. 🤙\n\n"
       "Bu söz tutulacak mı? Kasa: {KASA}"),
   tags=["#Bilecik", "#Söğüt", "#Marmara"],
   son="Mert serçe parmak sözü verir: büyük karar olursa önce Ali'ye soracak.",
   teaser="Küçük bir çadır, sonbahar yaprakları ve bir serçe parmak sözü. Bölüm 46: Bilecik. Pek yakında.")

# ======================================================================= 47 BURSA
EP(47, "Bursa", "Koza Han'da İpek",
   "İskender, Koza Han'da ipek eşarp ve Uludağ'ın gölgesinde bir telefon.",
   "Bursa'da sabah kalan lokum bir kafeye satılır. Koza Han'ın avlusunda ipek böcekçiliğinin ve ipek ticaretinin yüzyıllık hikâyesini "
   "dinler, el baskısı 30 ipek eşarp alırlar. Öğlen tereyağı dökülen İskender kebabını yerler. Yeşil Türbe'nin çinilerini görür, Uludağ'a "
   "bakan bir çay bahçesinde dinlenirler. Akşam Mert'in telefonuna İstanbul'dan bir toptancıdan mesaj gelir; Mert mesajı Ali'ye göstermek "
   "üzereyken telefonu cebine koyar.",
   {"kafe": ("Bursa'da kafe", "a cozy café in central Bursa with wooden tables and a display of desserts, autumn light"),
    "kozahan": ("Koza Han", "the courtyard of Koza Han in Bursa: a two-storey Ottoman stone and brick caravanserai with arcades, a small "
                "octagonal mesjid in the middle, silk shops with colorful scarves hanging, plane trees and tea tables"),
    "iskender": ("İskenderci", "a traditional İskender kebab restaurant in Bursa: thin döner slices over bread with tomato sauce and yogurt, a "
                 "waiter pouring sizzling melted butter from a small pan, tiled walls"),
    "turbe": ("Yeşil Türbe ve çay bahçesi", "a tea garden next to the turquoise-tiled Green Tomb in Bursa at sunset, Uludağ mountain rising "
              "behind with its first snow")},
   [
       S("09:00 iç-gündüz", "kafe", ["ali", "kafeci"], "Son Lokum",
         "Bir kafe kalan 25 kilo Afyon lokumunu çay yanına alır.",
         "The café owner arranges pieces of lokum on a small plate next to a tea glass and smiles; Ali hands over the box and receives the money.",
         [("kafeci", "Çayın yanına Afyon lokumu... müşteri bayılır.", "pleased"),
          ("ali", "Yirmi beş kilo, dört yüz elliden. Afyon bitti.", "satisfied")],
         "static medium two-shot at the counter",
         t=U(25, "kg", 450, "satis", "Afyon lokumu, Bursa'da kafeye ({adet} kg x {fiyat} TL)")),
       S("10:30 sabah", "kozahan", ["mert", "ali", "ipekci"], "İpeğin Yolu",
         "Koza Han'da ipekçi Leyla Hanım koza ticaretinin yüzyıllardır bu avluda yapıldığını anlatır.",
         "Leyla holds a white silk cocoon in her palm and then pulls a single shimmering thread from it; Mert leans in, astonished; Ali looks up at "
         "the arcades of the han.",
         [("ipekci", "Bir kozadan yüzlerce metre ipek çıkar. Bu avluda yüzyıllardır alınıp satılıyor.", "elegant"),
          ("mert", "Bir böceğin emeği... bir eşarp.", "amazed")],
         "slow push-in on the cocoon and the thread", h="serin"),
       S("11:30 iç-gündüz", "kozahan", ["ali", "ipekci"], "Otuz Eşarp",
         "El baskısı 30 ipek eşarp alırlar. Ege'de ve Trakya'da butiklere satılacaktır.",
         "Leyla unfolds silk scarves in rich colors one by one over a table; Ali touches one gently, nods and counts money; Leyla folds the "
         "scarves into tissue paper.",
         [("ipekci", "El baskısı, tanesi dokuz yüz.", "businesslike"),
          ("ali", "Otuz tane alıyoruz. Ayvalık ve Çanakkale'de butiklere.", "planning")],
         "static medium two-shot at the table",
         t=U(30, "eşarp", 900, "alis", "Bursa el baskısı ipek eşarp ({adet} x {fiyat} TL)")),
       S("13:00 iç-gündüz", "iskender", ["mert", "ali"], "Tereyağı",
         "İskender kebabının üstüne cızırdayan tereyağı dökülür. Mert'in gözleri parlar.",
         "A waiter's hand pours sizzling melted butter over a plate of thin döner slices with tomato sauce and yogurt; steam rises; Mert leans in, "
         "closes his eyes and inhales; Ali laughs.",
         [("mert", "Ali, bu sesi kaydet. Tereyağı sesi.", "ecstatic"),
          ("ali", "Kaydettim. Kasaya da yazdım.", "laughing")],
         "slow push-in on the plate",
         t=T("yemek", 1000, "İskender kebabı (2 kişi)")),
       S("17:30 gün batımı", "turbe", ["mert", "ali"], "Uludağ'ın İlk Karı",
         "Yeşil Türbe'nin yanındaki çay bahçesinde Uludağ'ın ilk karına bakarlar.",
         "Mert and Ali sit with tea glasses at a garden table; Ali points at the first snow on the mountain peak; Mert shivers theatrically and "
         "pulls his t-shirt sleeves down.",
         [("ali", "Uludağ'a kar düştü. Karadeniz'de mont lazım olacak.", "practical"),
          ("mert", "Tişört benim imzam Ali. Ama... evet, mont.", "reluctant")],
         "slow dolly-out revealing the turquoise tomb and the mountain", h="serin"),
       S("21:00 akşam", "turbe", ["mert", "ali"], "Bir Mesaj",
         "Mert'in telefonuna İstanbul'dan bir toptancıdan mesaj gelir. Mert mesajı Ali'ye göstermek üzereyken telefonu cebine koyar.",
         "Mert reads a message on his phone, his eyes widen; he turns toward Ali to show it, hesitates, then slowly slides the phone into his "
         "pocket and smiles innocently when Ali looks at him.",
         [("ali", "Kim yazdı?", "casual"),
          ("mert", "Hiç... bir takipçi.", "evasive")],
         "slow push-in to Mert's face",
         t=[T("konaklama", 1500, "Otel, 1 gece"), T("ulasim", 1000, "Yakıt: Bursa-Balıkesir")]),
   ],
   misafir={"kafeci": ("KAFECİ", "CAFÉ OWNER, a 35-year-old Turkish woman, curly hair, a green apron", "adult female voice"),
            "ipekci": ("LEYLA HANIM", "LEYLA, a 54-year-old Turkish silk merchant, elegant, silver-streaked hair in a low bun, a silk scarf "
                       "around her neck, a camel coat", "adult female voice, elegant, Bursa Turkish")},
   ay=AY, hava="serin", urun="İpek, İskender kebabı, kestane şekeri, havlu; Koza Han, Yeşil Türbe, Uludağ (Bursa UNESCO)",
   sponsor="İpek, kestane şekeri ya da Bursa mutfağı alanında",
   kapak=("kozahan", ["mert", "ali", "ipekci"], "In the arcaded courtyard of Koza Han, Leyla pulls a shimmering silk thread from a cocoon while "
          "Mert and Ali watch amazed, colorful silk scarves hanging around them", "Koza Han'da kozadan ipek çeken ipekçi ve hayran Mert ile Ali."),
   yakinda=("turbe", ["mert"], "Mert's face lit by a phone screen at dusk, his expression hiding a secret, a turquoise-tiled dome and a snowy "
            "mountain blurred behind", "Alacakaranlıkta bir sırrı saklayan, telefon ışığıyla aydınlanan yüz."),
   tiktok="Bursa'da tereyağı sesi ve gizli bir mesaj 🤫 #JozhStudios",
   ig=("Koza Han'da bir kozadan yüzlerce metre ipek çıktığını öğrendik ve 30 el baskısı eşarp aldık. 🧣\n\n"
       "İskender'in üstüne dökülen tereyağının sesi... 🤤 Uludağ'a ilk kar düşmüş, Mert'in tişört dönemi bitiyor.\n\n"
       "Ama Mert'in telefonuna bir mesaj geldi ve onu Ali'den sakladı. 🤫 Kasa: {KASA}"),
   tags=["#Bursa", "#KozaHan", "#İskender"],
   son="Mert, İstanbul'dan gelen bir toptancı mesajını Ali'den saklar.",
   teaser="Bir kozadan çıkan ipek, tereyağı sesi ve saklanan bir mesaj. Bölüm 47: Bursa. Pek yakında.")

# ======================================================================= 48 BALIKESİR
EP(48, "Balıkesir", "Cunda'da Eşarp",
   "Ayvalık'ın taş sokakları, Cunda'da butik, höşmerim ve Kazdağları'nda bir sır.",
   "Ayvalık'ın taş sokaklarında eski zeytinyağı fabrikalarının bacalarını görürler. Cunda Adası'ndaki bir butik 15 ipek eşarp alır. "
   "Öğlen Balıkesir'in tatlısı höşmerimi tadarlar. Kazdağları'nın eteklerinde kekik ve adaçayı kokusu arasında yürürken Ali, Mert'in "
   "telefonla gizlice konuştuğunu fark eder. Akşam Şeytan Sofrası'nda gün batımını izlerken Mert sır vermeye çok yaklaşır ama vazgeçer.",
   {"ayvalik": ("Ayvalık sokakları", "a narrow street in Ayvalık with old stone houses, colorful shutters, and the tall brick chimney of an old "
                "olive oil factory against a blue sky"),
    "butik": ("Cunda'da butik", "a small boutique on Cunda Island with whitewashed stone walls, linen clothes and silk scarves on wooden "
              "hangers, the sea visible through the door"),
    "tatlici": ("Höşmerimci", "a small dessert shop near Balıkesir with a tray of höşmerim (a soft cheese-and-semolina dessert in syrup), "
                "marble tables"),
    "kazdag": ("Kazdağları eteği", "a pine and oak forest trail on the foothills of Kazdağları with wild thyme and sage bushes, a stream, "
               "autumn light"),
    "seytan": ("Şeytan Sofrası", "the Şeytan Sofrası viewpoint near Ayvalık at sunset: a rocky hilltop overlooking dozens of small islands "
               "scattered in the glowing sea")},
   [
       S("09:00 sabah", "ayvalik", ["mert", "ali"], "Bacalar",
         "Ayvalık'ın taş sokaklarında eski zeytinyağı fabrikalarının tuğla bacalarını görürler.",
         "Mert and Ali walk up a narrow stone street; Ali stops and points up at a tall brick factory chimney against the blue sky; Mert checks "
         "his phone quickly and pockets it.",
         [("ali", "Bu bacalar bir zamanlar zeytinyağı fabrikalarınınmış.", "interested"),
          ("mert", "Hı hı. Çok güzel. Cunda'ya gidelim mi?", "distracted")],
         "slow crane-up to the chimney", h="serin"),
       S("11:00 iç-gündüz", "butik", ["ali", "butikci"], "On Beş Eşarp",
         "Cunda'daki bir butik 15 ipek eşarp alır.",
         "The boutique owner drapes a silk scarf over a hanger next to linen dresses and steps back; Ali hands her the folded scarves and receives "
         "an envelope.",
         [("butikci", "Bursa ipeği adaya çok yakışır. On beş tane.", "pleased"),
          ("ali", "Tanesi bin altı yüz. Kalan on beşi Çanakkale'ye.", "businesslike")],
         "static medium two-shot by the hangers",
         t=U(15, "eşarp", 1600, "satis", "Bursa ipek eşarp, Cunda'da butiğe ({adet} x {fiyat} TL)")),
       S("13:30 iç-gündüz", "tatlici", ["mert", "ali"], "Höşmerim",
         "Balıkesir'in tatlısı höşmerimi tadarlar. Mert'in telefonu masada titrer; ekranı aşağı çevirir.",
         "Mert takes a spoonful of soft höşmerim and makes a happy face; his phone buzzes on the table and he quickly turns it face down; Ali "
         "notices, glances at the phone, then at Mert.",
         [("mert", "Bu tatlı peynirden mi yapılıyor? İnanılmaz.", "too cheerful"),
          ("ali", "Telefonun çaldı.", "flat, noticing")],
         "static medium two-shot at the marble table",
         t=T("yemek", 800, "Öğle yemeği ve höşmerim")),
       S("16:00 ikindi", "kazdag", ["mert", "ali"], "Kekik Kokusu",
         "Kazdağları'nda kekik ve adaçayı kokuları arasında yürürler. Mert geride kalıp fısıldayarak telefonla konuşur.",
         "Ali walks ahead on the forest trail and crushes a thyme leaf between his fingers to smell it; he turns and sees Mert far behind him, "
         "talking on the phone in a low voice with his back turned.",
         [("ali", "Mert? Kimle konuşuyorsun?", "suspicious"),
          ("mert", "Kimseyle! Kargo şirketi.", "too quick")],
         "slow tracking shot along the trail, rack focus from Ali to Mert", h="serin"),
       S("18:30 gün batımı", "seytan", ["mert", "ali"], "Neredeyse",
         "Şeytan Sofrası'nda adaların üstünde güneş batar. Mert bir an sırrını söyleyecek gibi olur ama vazgeçer.",
         "Mert and Ali sit on the rocks overlooking the islands; Mert opens his mouth and turns to Ali, takes a breath, then closes his mouth and "
         "looks back at the sea; Ali waits, then looks away too.",
         [("mert", "Ali, sana bir şey...", "hesitant"),
          ("ali", "Ne?", "hopeful"),
          ("mert", "Yok. Güneş çok güzel.", "backing off")],
         "slow push-in to their profiles against the sunset"),
       S("21:30 akşam", "seytan", ["ali"], "Yalnız Düşünce",
         "Ali karanlıkta tek başına oturur ve defterine bir şey yazar.",
         "Ali sits alone on the rock after dark, the islands now black shapes, writing slowly in the brown notebook by phone light; he stops, "
         "looks at the sea and closes the notebook.",
         [("ali", "Söz vermişti. Büyük karar olursa önce bana soracaktı.", "quiet, to himself")],
         "static wide shot, slow push-in",
         t=[T("konaklama", 1200, "Pansiyon, 1 gece"), T("ulasim", 1400, "Yakıt: Balıkesir-Çanakkale")]),
   ],
   misafir={"butikci": ("BUTİK SAHİBİ", "BOUTIQUE OWNER, a 46-year-old Turkish woman, short grey hair, linen dress, big silver rings",
                        "adult female voice, pleased")},
   ay=AY, hava="ılık", urun="Ayvalık zeytinyağı, höşmerim, Kazdağları kekiği; Cunda Adası, Şeytan Sofrası",
   sponsor="Zeytinyağı, höşmerim ya da ada turizmi alanında",
   kapak=("seytan", ["mert", "ali"], "Mert and Ali sit on rocks above dozens of islands scattered in a glowing sunset sea, Mert turning toward Ali "
          "as if to confess something", "Adaların üstünde gün batımında bir şey söylemeye hazırlanan Mert."),
   yakinda=("kazdag", ["mert"], "Mert whispering on a phone with his back turned on a dark forest trail, a figure watching from far ahead out "
            "of focus", "Ormanda sırtı dönük telefonla fısıldayan Mert ve uzakta izleyen biri."),
   tiktok="Mert bir şey saklıyor 🤐 Şeytan Sofrası'nda gün batımı #JozhStudios",
   ig=("Ayvalık'ın bacaları, Cunda'da eşarp satışı, höşmerim ve Kazdağları'nda kekik kokusu. 🌿\n\n"
       "Ama Mert'in telefonu hiç susmuyor ve o hep geride kalıp fısıldıyor... Şeytan Sofrası'nda bir şey söyleyecekti, söylemedi. 🤐\n\n"
       "Ali deftere yazdı: 'Söz vermişti.' Kasa: {KASA}"),
   tags=["#Balıkesir", "#Ayvalık", "#Cunda"],
   son="Ali, Mert'in bir şey sakladığından emin.",
   teaser="Bacalar, höşmerim, kekik kokusu ve söylenmeyen bir söz. Bölüm 48: Balıkesir. Pek yakında.")

# ======================================================================= 49 ÇANAKKALE
EP(49, "Çanakkale", "Boğazın İki Yakası",
   "Truva atı, Ezine peyniri, Gelibolu'da sessiz bir saygı ve boğazı geçen feribot.",
   "Çanakkale'de sabah kordonda Truva atının maketinin önünde fotoğraf çekerler. Bir butik kalan 15 eşarbı alır. Ezine'de bir mandıradan "
   "60 kilo Ezine peyniri alırlar. Feribotla boğazın Avrupa yakasına geçip Gelibolu Yarımadası Tarihi Alanı'nda sessizce yürürler; Mert "
   "ilk kez telefonunu tamamen kapatır. Akşam feribot dönüşünde Ali, Mert'e açıkça sorar. Mert 'Edirne'de anlatacağım' der.",
   {"kordon": ("Çanakkale kordonu", "the Çanakkale seafront promenade in the morning: a large wooden Trojan horse film prop on the waterfront, "
               "the narrow Dardanelles strait with a ship passing"),
    "butik": ("Butik", "a small boutique in Çanakkale's old bazaar with scarves and handmade goods"),
    "mandira": ("Ezine mandırası", "a white cheese dairy near Ezine: steel vats, tins of white cheese in brine, a cool room"),
    "feribot": ("Boğaz feribotu", "the open deck of a car ferry crossing the Dardanelles strait, gulls, the old white pickup truck parked "
                "on the car deck, hills on both sides"),
    "gelibolu": ("Gelibolu Yarımadası Tarihi Alanı", "a quiet memorial landscape on the Gallipoli peninsula: green hills, cypress and pine "
                 "trees, a simple stone memorial path, the sea far below, respectful calm atmosphere")},
   [
       S("08:30 sabah", "kordon", ["mert", "ali"], "Truva Atı",
         "Kordonda Truva atı maketinin önündedirler. Ali, atın içinde saklananların hikâyesini anlatır.",
         "Mert poses under the giant wooden horse with his arms raised; Ali takes the photo, lowers the phone and looks at Mert meaningfully.",
         [("ali", "Atın içinde askerler saklanmış. İçinde bir şey saklayan hediyeler tehlikelidir.", "pointed"),
          ("mert", "Ben bir şey saklamıyorum Ali.", "defensive")],
         "static wide shot with the horse and the strait", h="serin"),
       S("10:00 iç-gündüz", "butik", ["ali", "butikci"], "Son Eşarplar",
         "Bir butik kalan 15 ipek eşarbı alır.",
         "The boutique owner hangs silk scarves on a rack one by one; Ali hands her the last scarf and receives an envelope, his face serious.",
         [("butikci", "On beşini de alıyorum. Bursa ipeği iyi satar.", "pleased"),
          ("ali", "Tanesi bin altı yüz. İpek bitti.", "flat")],
         "static medium two-shot at the rack",
         t=U(15, "eşarp", 1600, "satis", "Bursa ipek eşarp, Çanakkale'de butiğe ({adet} x {fiyat} TL)")),
       S("12:00 iç-gündüz", "mandira", ["mert", "ali", "peynirci"], "Ezine Peyniri",
         "Ezine'de bir mandıradan 60 kilo tam yağlı Ezine peyniri alırlar. Salamurada haftalarca dayanır.",
         "The dairyman lifts a block of white cheese out of a tin of brine and cuts a piece for each of them; Mert tastes and nods; Ali counts "
         "money in silence.",
         [("peynirci", "İnek, koyun, keçi sütü. Salamurada beklemiş. Kilosu dört yüz seksen.", "proud"),
          ("mert", "Altmış kilo. Edirne ve İstanbul'da gider.", "confident")],
         "static medium three-shot by the vats",
         t=[U(60, "kg", 480, "alis", "Ezine peyniri ({adet} kg x {fiyat} TL)"), T("yemek", 800, "Öğle yemeği")]),
       S("14:30 ikindi", "feribot", ["mert", "ali"], "Boğazı Geçmek",
         "Kamyonetle feribota binip boğazın Avrupa yakasına geçerler. Martılar peşlerinden gelir.",
         "Mert and Ali stand at the ferry railing beside their pickup on the car deck as gulls glide alongside; Mert throws a small piece of simit "
         "and a gull catches it in the air; Ali watches the water.",
         [("mert", "Asya'dan Avrupa'ya kamyonetle geçiyoruz!", "trying to lighten the mood"),
          ("ali", "Evet. Bir kıtadan ötekine.", "distant")],
         "slow dolly along the railing", h="serin",
         t=T("ulasim", 900, "Çanakkale-Eceabat feribotu (kamyonet + 2 kişi)")),
       S("16:30 ikindi", "gelibolu", ["mert", "ali"], "Sessizlik",
         "Gelibolu Yarımadası Tarihi Alanı'nda sessizce yürürler. Mert telefonunu tamamen kapatır.",
         "Mert and Ali walk slowly and silently along the memorial path under cypress trees; Mert takes his phone out, looks at it, switches it "
         "off and puts it away; Ali notices and looks at him.",
         [], "slow tracking shot behind them along the path", h="serin",
         kurgu="Tarihi alan saygıyla, müziksiz ve konuşmasız gösterilir. Ekrana yalnızca yer adı yazılır."),
       S("19:30 akşam", "feribot", ["mert", "ali"], "Açık Soru",
         "Akşam dönüş feribotunda Ali açıkça sorar. Mert, Edirne'de anlatacağını söyler.",
         "On the ferry deck at dusk, Ali turns to face Mert directly; Mert looks down, then meets his eyes and nods slowly; the lights of the "
         "town shine across the water.",
         [("ali", "Mert, ne saklıyorsun? Açık söyle.", "direct, calm"),
          ("mert", "Edirne'de anlatacağım. Söz. Bir gün ver.", "uneasy")],
         "static medium two-shot by the railing",
         t=[T("konaklama", 1300, "Pansiyon, 1 gece"), T("ulasim", 1500, "Feribot dönüşü ve yakıt: Çanakkale-Edirne")]),
   ],
   misafir={"butikci": ("BUTİK SAHİBİ", "BOUTIQUE OWNER, a 39-year-old Turkish man, neat beard, round glasses, a knitted vest", "adult male voice"),
            "peynirci": ("MANDIRACI", "DAIRYMAN, a 60-year-old Turkish man, stout, a white cap, white rubber boots, a white apron",
                         "elderly male voice, proud")},
   ay=AY, hava="serin", urun="Ezine peyniri, Bozcaada, Truva; Gelibolu Yarımadası Tarihi Alanı, Çanakkale Boğazı",
   sponsor="Ezine peyniri ya da kültür turizmi alanında",
   kapak=("feribot", ["mert", "ali"], "Mert and Ali stand at the ferry railing by their old white pickup as gulls glide beside them over the "
          "Dardanelles, hills on both shores", "Boğazda feribotta martıların arasında Mert ve Ali."),
   yakinda=("kordon", ["mert"], "The dark silhouette of a giant wooden horse against a dim sky, a small figure standing in its shadow",
            "Dev tahta bir atın karanlık silüeti ve gölgesinde küçük bir figür."),
   tiktok="Bir kıtadan ötekine kamyonetle 🚚⛴️ Ama aramızda bir sır var #JozhStudios",
   ig=("Çanakkale'de Truva atının önünde Ali bir şey söyledi: 'İçinde bir şey saklayan hediyeler tehlikelidir.' 🐴\n\n"
       "Ezine peyniri aldık, boğazı kamyonetle geçtik, Gelibolu'da sessizce yürüdük. Mert telefonunu kapattı.\n\n"
       "Dönüşte Ali açıkça sordu. Mert: 'Edirne'de anlatacağım.' Kasa: {KASA}"),
   tags=["#Çanakkale", "#EzinePeyniri", "#Gelibolu"],
   son="Mert, sırrını Edirne'de anlatacağına söz verir.",
   teaser="Bir tahta at, iki kıta ve cevap bekleyen bir soru. Bölüm 49: Çanakkale. Pek yakında.")

# ======================================================================= 50 EDİRNE
EP(50, "Edirne", "Selimiye'nin Gölgesinde",
   "Selimiye'de itiraf, tava ciğer, badem ezmesi ve meyve sabunu.",
   "Edirne'de sabah Selimiye Camii'nin kubbesinin altında Mert sırrını anlatır: İstanbul'dan bir toptancı 500 kutu istiyordur, kutu başı "
   "700 lira. Ali sevinmek yerine sözleşme ve ön ödeme sorar; Mert yazılı bir şey olmadığını itiraf eder. Ali dikkatli olmalarını ister. Ezine "
   "peynirinin yarısı satılır. Tava ciğer yerler. Bir badem ezmesi atölyesinden 50 kilo, meyve sabunu ustasından 200 meyve biçimli sabun "
   "alırlar. Gece Mert, Ali'nin 'sözleşme olmadan hiçbir şey yapmayalım' şartını kabul eder.",
   {"selimiye": ("Selimiye Camii", "the vast interior of the Selimiye Mosque in Edirne: a huge central dome on eight pillars, intricate tiles, "
                 "soft daylight through many windows, carpeted floor, very calm"),
    "sarkuteri": ("Edirne şarküterisi", "a delicatessen in Edirne's Ali Paşa Bazaar with cheeses, jars and a marble counter"),
    "ciger": ("Tava ciğerci", "a famous-style Edirne liver restaurant: thin crispy fried liver slices with fried dried red peppers on plates, "
              "simple tables"),
    "badem": ("Badem ezmesi atölyesi", "an almond paste workshop in Edirne: bowls of blanched almonds, a stone grinder, trays of white almond "
              "paste pieces"),
    "sabun": ("Meyve sabunu atölyesi", "a small fruit-soap workshop in Edirne: colorful handmade soaps shaped like apples, pears, quinces and "
              "strawberries on wooden shelves, scented air"),
    "otel": ("Otel odası", "a hotel room in Edirne at night: boxes of almond paste and fruit soaps on a table, two beds, a window to the lit "
             "minarets")},
   [
       S("09:00 iç-gündüz", "selimiye", ["mert", "ali"], "İtiraf",
         "Selimiye'nin kubbesi altında Mert anlatır: İstanbul'dan bir toptancı 500 kutu istiyor, kutu başı 700 lira.",
         "Mert and Ali sit on the carpet under the enormous dome, shoes off, speaking in low voices; Mert looks up at the dome and then at Ali, "
         "confessing; Ali listens without moving.",
         [("mert", "İstanbul'dan bir toptancı beş yüz kutu istiyor. Kutusu yedi yüz.", "low, confessing"),
          ("ali", "Sözleşme var mı? Ön ödeme var mı?", "calm, serious")],
         "slow crane-up from them to the dome"),
       S("09:20 iç-gündüz", "selimiye", ["mert", "ali"], "Yazılı Bir Şey Yok",
         "Mert yazılı bir şey olmadığını itiraf eder. Ali kızmaz ama kararlıdır.",
         "Mert shakes his head and looks down at his hands; Ali exhales slowly, places a hand on Mert's shoulder and speaks quietly but firmly.",
         [("mert", "Yok. Sözlü. Ama adam çok ciddi.", "weak"),
          ("ali", "Yazılı olmadan tek kuruş yok Mert. Bu da kural iki.", "firm, gentle")],
         "static medium two-shot at carpet level"),
       S("11:00 iç-gündüz", "sarkuteri", ["ali", "sarkuteri"], "Peynir Edirne'de",
         "Ali Paşa Çarşısı'ndaki bir şarküteri 30 kilo Ezine peynirini alır.",
         "The deli owner tastes a piece of white cheese and nods; Ali places the tin on the counter and accepts the money.",
         [("sarkuteri", "Ezine peyniri her zaman satılır. Otuz kilo, altı yüz elliden.", "practical"),
          ("ali", "Hayırlı olsun.", "polite, distracted")],
         "static medium two-shot at the counter",
         t=U(30, "kg", 650, "satis", "Ezine peyniri, Edirne'de şarküteriye ({adet} kg x {fiyat} TL)")),
       S("13:00 iç-gündüz", "ciger", ["mert", "ali"], "Tava Ciğer",
         "Edirne'nin tava ciğerini kızarmış kuru biberle yerler. Gerginlik biraz çözülür.",
         "Mert holds up a crispy fried liver slice and a dried red pepper and offers the pepper to Ali; Ali takes it and a small smile appears.",
         [("mert", "Barış biberi. Acı ama tatlı.", "hopeful"),
          ("ali", "Biberi aldım. Ama kural iki geçerli.", "half-smiling")],
         "static medium two-shot across the table",
         t=T("yemek", 900, "Tava ciğer (2 kişi)")),
       S("15:30 iç-gündüz", "badem", ["mert", "ali", "ustabadem"], "Badem ve Meyve",
         "Bir badem ezmesi atölyesinden 50 kilo, bir meyve sabunu atölyesinden 200 meyve biçimli sabun alırlar. Hepsi bir 'Marmara Kutusu' için.",
         "The almond paste maker cuts white almond paste into small pieces and places them in a box; Mert holds up a fruit-shaped soap that looks "
         "exactly like a quince and pretends to bite it; Ali laughs despite himself.",
         [("ustabadem", "Badem ezmesi kilosu yedi yüz. Sabuncu komşu, ona da selam söyleyin.", "friendly"),
          ("mert", "Bu ayva sabun Ali! Neredeyse ısırıyordum.", "comic")],
         "slow tracking shot from the almond paste to the soap shelves",
         t=[U(50, "kg", 700, "alis", "Edirne badem ezmesi ({adet} kg x {fiyat} TL)"), U(200, "sabun", 60, "alis", "Edirne meyve sabunu (200 x 60 TL)")]),
       S("22:00 iç-gece", "otel", ["mert", "ali"], "Kural İki",
         "Gece otelde Mert, Ali'nin şartını kabul eder: sözleşme olmadan hiçbir şey yapılmayacak. Serçe parmaklar yeniden.",
         "Ali holds out his little finger across the gap between the beds; Mert looks at it, smiles with relief and hooks it with his own; the "
         "minarets glow outside the window.",
         [("ali", "Kural iki: sözleşme olmadan hiçbir şey. Söz mü?", "serious"),
          ("mert", "Söz. İkinci serçe parmak.", "relieved")],
         "static medium two-shot between the beds",
         t=[T("konaklama", 1400, "Otel, 1 gece"), T("ulasim", 1500, "Yakıt: Edirne-Kırklareli")]),
   ],
   misafir={"sarkuteri": ("ŞARKÜTERİCİ", "DELI OWNER, a 52-year-old Turkish man, bald, a grey goatee, a white apron", "adult male voice"),
            "ustabadem": ("BADEM EZMESİ USTASI", "ALMOND PASTE MAKER, a 59-year-old Turkish woman, petite, white hair in a bun, a white apron "
                          "and cap", "elderly female voice, friendly, Edirne Turkish")},
   ay=AY, hava="serin", urun="Tava ciğer, badem ezmesi, meyve sabunu, Kırkpınar; Selimiye Camii (UNESCO)",
   sponsor="Badem ezmesi, meyve sabunu ya da Edirne mutfağı alanında",
   kapak=("badem", ["mert", "ali"], "Mert pretends to bite a fruit-shaped soap that looks exactly like a quince while Ali laughs, shelves of "
          "colorful fruit soaps behind them", "Ayva biçimli sabunu ısırmaya kalkan Mert ve gülen Ali."),
   yakinda=("selimiye", ["mert", "ali"], "Two small figures sitting on a vast carpet under an enormous glowing dome, seen from high above, light "
            "rays from the windows", "Devasa bir kubbenin altında halıda oturan iki küçük figür."),
   tiktok="Selimiye'nin kubbesi altında itiraf 🕌 #JozhStudios",
   ig=("Selimiye'nin kubbesi altında Mert sırrını anlattı: bir toptancı 500 kutu istiyor, kutusu 700 lira! 😳\n\n"
       "Ali'nin tek sorusu: 'Sözleşme var mı?' Yokmuş. Kural iki doğdu: yazılı olmadan tek kuruş yok. ✍️\n\n"
       "Tava ciğer yedik, badem ezmesi ve ayvaya benzeyen sabunlar aldık. Kasa: {KASA}"),
   tags=["#Edirne", "#Selimiye", "#BademEzmesi"],
   son="Kural iki: sözleşme olmadan hiçbir şey yapılmayacak. Mert söz verir.",
   teaser="Bir kubbenin altında itiraf ve ikinci serçe parmak sözü. Bölüm 50: Edirne. Pek yakında.")

# ======================================================================= 51 KIRKLARELİ
EP(51, "Kırklareli", "Longozda Çamur",
   "İğneada'nın longoz ormanı, çamura saplanan kamyonet ve bir traktör.",
   "Kırklareli'de sabah bir lokanta Ezine peynirinin bir kısmını alır. İğneada Longoz Ormanları'na doğru giderken toprak yolda kamyonet "
   "çamura saplanır. Bir traktörlü çiftçi onları kurtarır ve karşılığında sadece bir fotoğraf ister. Longozun su basmış ormanında sessiz "
   "bir yürüyüş yaparlar. Akşam Demirköy'de Dupnisa Mağarası'nın girişine giderler. Gece toptancı yeniden arar; Mert telefonu açar ve "
   "hoparlöre verir.",
   {"lokanta": ("Kırklareli lokantası", "a simple restaurant in Kırklareli with steel trays and a glass display of stews, autumn light"),
    "yol": ("İğneada yolu, çamur", "a muddy dirt road through a dense green forest near İğneada after rain: deep puddles, the old white pickup "
            "truck stuck with its rear wheel sunk in mud"),
    "longoz": ("Longoz ormanı", "the İğneada floodplain forest (longoz): tall ash and oak trees standing in still dark water, a wooden "
               "boardwalk, mist, fallen autumn leaves on the water"),
    "magara": ("Dupnisa Mağarası girişi", "the entrance of Dupnisa Cave near Demirköy at dusk: a rocky opening in a forested hillside, wooden "
               "stairs, cool air"),
    "pansiyon": ("Pansiyon odası", "a wooden guesthouse room near Demirköy at night: two beds, a small table, muddy shoes by the door")},
   [
       S("09:30 sabah", "lokanta", ["mert", "lokantaci"], "Peynir Kırklareli'de",
         "Bir lokanta 20 kilo Ezine peyniri alır. Kalan 10 kilo İstanbul'a.",
         "The restaurant owner cuts a piece of white cheese, tastes it and nods; Mert sets the tin on the counter and takes the money with a grin.",
         [("lokantaci", "Kahvaltıya Ezine peyniri koymayan yer kaybeder. Yirmi kilo.", "practical"),
          ("mert", "Altı yüz elliden. Kalan on kilo İstanbul'a.", "cheerful")],
         "static medium two-shot at the counter",
         t=U(20, "kg", 650, "satis", "Ezine peyniri, Kırklareli'de lokantaya ({adet} kg x {fiyat} TL)")),
       S("12:00 öğle", "yol", ["mert", "ali"], "Saplandık",
         "İğneada yolunda kamyonet çamura saplanır. Mert gaza bastıkça tekerlek daha çok gömülür.",
         "The rear wheel of the pickup spins in the mud spraying dirt; Ali, standing behind, gets splashed and steps back; Mert leans out of the "
         "driver's window looking back with a guilty face.",
         [("ali", "Gaza basma Mert! Daha çok gömülüyor!", "shouting, splattered"),
          ("mert", "Çamur da İstanbul toptancısı gibi, bırakmıyor!", "frustrated joke")],
         "static wide shot from behind the pickup", h="bulutlu"),
       S("12:40 öğle", "yol", ["mert", "ali", "ciftci"], "Traktör",
         "Bir traktörlü çiftçi onları çamurdan çeker ve karşılığında sadece bir fotoğraf ister.",
         "A farmer on an old red tractor ties a rope to the front of the pickup and slowly pulls it out of the mud; Mert and Ali cheer, then pose "
         "with the farmer beside the tractor while Ali holds up the phone for a selfie.",
         [("ciftci", "Para istemem. Bir fotoğraf çekelim, torunum sizi izliyor.", "jovial"),
          ("mert", "Abi sen bizim kahramanımızsın!", "grateful")],
         "static wide shot, slow push-in as they pose", h="bulutlu"),
       S("15:00 ikindi", "longoz", ["mert", "ali"], "Suyun İçindeki Orman",
         "Longoz ormanında ahşap yolda yürürler. Ağaçlar suyun içinde durur; her şey sessizdir.",
         "Mert and Ali walk slowly along the wooden boardwalk over the still dark water among tall trees; Mert stops and looks at their reflections "
         "in the water; mist drifts between the trunks.",
         [("ali", "Ağaçlar suyun içinde yaşıyor. Sabırla.", "quiet"),
          ("mert", "Burada insanın aklı sakinleşiyor.", "soft")],
         "slow tracking shot along the boardwalk", h="sis"),
       S("18:00 gün batımı", "magara", ["mert", "ali"], "Mağaranın Ağzı",
         "Demirköy'de Dupnisa Mağarası'nın girişine giderler. İçeriden serin bir hava gelir.",
         "Mert and Ali stand at the rocky mouth of the cave; cool air moves their hair; Mert shouts a short 'Hey!' into the darkness and the echo "
         "returns; Ali smiles.",
         [("mert", "Hey! Toptancı burada mı?", "joking shout"),
          ("ali", "Yankı bile 'sözleşme' diyor.", "laughing")],
         "static wide shot from inside the cave mouth looking out",
         t=T("yemek", 700, "Öğle ve akşam yemeği")),
       S("22:00 iç-gece", "pansiyon", ["mert", "ali"], "Hoparlör",
         "Gece toptancı yeniden arar. Mert telefonu açar ve bu kez hoparlöre verir. Toptancı Tekirdağ'da buluşmak ister.",
         "Mert's phone rings; he looks at Ali, then answers and puts it on speaker on the table between them; Ali leans in and listens with his "
         "arms crossed. Their lips stay closed while the voice speaks.",
         [("mert", "Ortağım da dinliyor. Buyurun.", "steady"),
          ("ali", "Sözleşmeyi Tekirdağ'da imzalarız. Önce kâğıt.", "firm, to the phone")],
         "static medium two-shot over the table",
         t=[T("konaklama", 1100, "Pansiyon, 1 gece"), T("ulasim", 900, "Yakıt: Kırklareli-Tekirdağ")]),
   ],
   misafir={"lokantaci": ("LOKANTACI", "RESTAURANT OWNER, a 48-year-old Turkish woman, sturdy, a navy apron", "adult female voice, practical"),
            "ciftci": ("ÇİFTÇİ", "FARMER, a 65-year-old Turkish man, red cheeks, a flat cap, a thick wool sweater and rubber boots",
                       "elderly male voice, jovial, Thracian Turkish")},
   ay=AY, hava="bulutlu", urun="Trakya peyniri ve kaşarı, hardaliye; İğneada Longoz Ormanları, Dupnisa Mağarası",
   sponsor="Süt ürünleri ya da doğa turizmi alanında",
   kapak=("yol", ["mert", "ali", "ciftci"], "A farmer's old red tractor pulls the white pickup out of deep mud on a forest road, Ali splattered "
          "with mud laughing, Mert cheering from the window", "Traktörün çamurdan çektiği kamyonet; çamura bulanmış Ali gülüyor."),
   yakinda=("longoz", ["mert", "ali"], "Two silhouettes on a wooden boardwalk in a misty flooded forest, trees standing in dark still water",
            "Sisli, su basmış ormanda ahşap yolda iki silüet."),
   tiktok="Kamyonet çamura saplandı, bir traktör bizi kurtardı 🚜 #JozhStudios",
   ig=("İğneada yolunda kamyonet çamura saplandı. Mert gaza bastı, Ali çamur oldu. 😂 Bir çiftçi traktörüyle bizi çekti, karşılığında sadece bir fotoğraf istedi. 🚜❤️\n\n"
       "Longoz ormanında ağaçların suyun içinde yaşadığını gördük.\n\nGece toptancı aradı. Bu kez hoparlörde. Kasa: {KASA}"),
   tags=["#Kırklareli", "#İğneada", "#Longoz"],
   son="Toptancıyla Tekirdağ'da buluşulacak. Ali'nin şartı: önce kâğıt.",
   teaser="Çamura saplanan bir kamyonet, suyun içindeki orman ve hoparlöre verilen bir telefon. Bölüm 51: Kırklareli. Pek yakında.")

# ======================================================================= 52 TEKİRDAĞ
EP(52, "Tekirdağ", "Kâğıtsız Söz",
   "Tekirdağ köftesi, kâğıtsız bir anlaşma, 20.000 TL'lik ön ödeme ve bozulan söz.",
   "Tekirdağ'da sahilde Tekirdağ köftesi yerler. Toptancı buluşmaya gelmez, telefonla 'sözleşme İstanbul'da, ama malı şimdiden hazırlayın, "
   "depo için 20.000 ön ödeme' der. Ali reddeder. Ali bir eczaneye gittiğinde Mert, kaçırmaktan korkarak ön ödemeyi gönderir, 500 kutuluk "
   "ambalajı ve ek badem ezmesi ile sabunu sipariş eder. Rákóczi Müzesi'nin bahçesinde Ali gerçeği öğrenir. Akşam sahilde ilk kez gerçekten "
   "kavga ederler.",
   {"sahil": ("Tekirdağ sahili", "the Tekirdağ seafront promenade on an overcast day: a long waterfront with benches, a pier, the grey Sea of "
              "Marmara"),
    "kofteci": ("Köfteci", "a Tekirdağ meatball restaurant: small elongated grilled meatballs on plates with piyaz and roasted peppers, simple "
                "tables, a window to the sea"),
    "kamyonet": ("Kamyonetin içi", "the cab of the old white pickup truck parked by the seafront, rain drops on the windshield, the grey sea "
                 "outside"),
    "muze": ("Rákóczi Müzesi bahçesi", "the garden of the Rákóczi Museum in Tekirdağ: an old wooden Ottoman house with a small garden, autumn "
             "trees, a stone wall")},
   [
       S("10:00 iç-gündüz", "kofteci", ["mert", "ali"], "Tekirdağ Köftesi",
         "Sahilde Tekirdağ köftesi yerler. Mert sürekli telefonuna bakar; toptancı gecikmektedir.",
         "Mert eats a small grilled meatball while checking his phone every few seconds; Ali calmly squeezes lemon on his piyaz and watches him.",
         [("mert", "Saat on, adam hâlâ yok.", "nervous"),
          ("ali", "Gelmiyorsa bu da bir cevaptır.", "calm")],
         "static medium two-shot by the window", h="bulutlu",
         t=T("yemek", 800, "Tekirdağ köftesi ve piyaz")),
       S("11:30 sabah", "sahil", ["mert", "ali", "~toptanci"], "Önce Para",
         "Toptancı telefonla arar: sözleşme İstanbul'da, ama depo için şimdiden 20.000 ön ödeme ister. Ali reddeder.",
         "Mert holds the phone on speaker between them on the promenade; Ali shakes his head firmly at the phone; Mert bites his lip. Their lips "
         "stay closed while the voice speaks.",
         [("toptanci", "Sözleşme İstanbul'da. Ama depo için yirmi bin ön ödeme lazım, bugün.", "smooth, pushy, from the phone speaker"),
          ("ali", "Önce sözleşme. Para sonra.", "firm")],
         "static medium two-shot on the promenade", h="bulutlu"),
       S("13:00 iç-gündüz", "kamyonet", ["mert"], "Yalnız Karar",
         "Ali bir eczaneye gittiğinde Mert kamyonette tek başına kalır. Kaçırmaktan korkup ön ödemeyi gönderir ve 500 kutuluk mal sipariş eder.",
         "Mert sits alone in the pickup cab with rain on the windshield, staring at his phone; he types, hesitates, closes his eyes and presses "
         "send; then he leans his head back against the seat.",
         [("mert", "Kaçırırsak bir daha böyle iş gelmez... Gönder.", "whisper, convincing himself")],
         "slow push-in through the windshield to Mert's face", h="yağmur",
         t=[T("diger_gider", 20000, "Toptancıya depo ön ödemesi (sözlü, belgesiz)"),
            U(500, "kutu", 60, "diger_gider", "500 kutuluk ambalaj siparişi (500 x 60 TL)"),
            U(50, "kg", 700, "alis", "Ek Edirne badem ezmesi, telefonla sipariş (50 kg x 700 TL)"),
            U(300, "sabun", 60, "alis", "Ek Edirne meyve sabunu, telefonla sipariş (300 x 60 TL)")]),
       S("15:30 ikindi", "muze", ["mert", "ali"], "Ali Öğreniyor",
         "Rákóczi Müzesi'nin bahçesinde Ali defteri güncellerken bankadan çıkan parayı görür. Mert itiraf eder.",
         "Ali looks at his phone's banking screen, then slowly turns it toward Mert under the autumn trees; Mert looks away, then nods; Ali "
         "closes the notebook very slowly.",
         [("ali", "Yirmi bin ön ödeme. Ambalaj, badem, sabun. Ben eczanedeyken.", "cold, quiet"),
          ("mert", "Kaçırmak istemedim Ali. Bu bizim büyük şansımız.", "pleading")],
         "slow push-in to Ali's face", h="bulutlu"),
       S("18:00 akşam", "sahil", ["mert", "ali"], "Kavga",
         "Sahilde ilk kez gerçekten kavga ederler. Ali sözün bozulduğunu söyler, Mert büyük düşünmekle suçlanmaktan bıkmıştır.",
         "On the windy grey promenade Ali and Mert stand face to face; Ali raises the brown notebook and lets it drop to his side; Mert throws his "
         "arms wide; a wave crashes on the pier behind them.",
         [("ali", "İki kere söz verdin Mert. İki kere!", "hurt, loud"),
          ("mert", "Ben de bu işi büyütmek istiyorum! Hep küçük mü kalacağız?", "angry")],
         "static medium two-shot, the sea behind", h="rüzgar"),
       S("21:00 akşam", "kamyonet", ["mert", "ali"], "Sessiz Kabin",
         "Gece kamyonette ikisi de konuşmaz. Yarın İstanbul'da sözleşme imzalanacaktır, ya da imzalanmayacak.",
         "Mert sits behind the wheel and Ali in the passenger seat, both staring forward in silence; the windshield wipers move slowly; Ali "
         "finally speaks without turning his head.",
         [("ali", "Yarın İstanbul. Sözleşme yoksa ben yokum.", "quiet, final")],
         "static medium two-shot through the windshield", h="yağmur",
         t=[T("konaklama", 1200, "Pansiyon, 1 gece"), T("ulasim", 1000, "Yakıt: Tekirdağ-İstanbul")]),
   ],
   misafir={"toptanci": ("TOPTANCI", "WHOLESALER, a 45-year-old Turkish man, slicked-back hair, a shiny grey suit, a heavy watch",
                         "adult male voice, smooth and pushy, fast Istanbul Turkish")},
   ay=AY, hava="bulutlu", urun="Tekirdağ köftesi, Hayrabolu tatlısı, ayçiçeği; Rákóczi Müzesi",
   sponsor="Köfte, tatlı ya da Trakya tarım ürünleri alanında",
   kapak=("sahil", ["mert", "ali"], "Mert and Ali stand face to face in a heated argument on a windy grey seafront promenade, a wave crashing on "
          "the pier behind them, dramatic overcast sky", "Rüzgârlı sahilde karşı karşıya kavga eden Mert ve Ali."),
   yakinda=("kamyonet", ["mert"], "Mert alone in a dark pickup cab, his face lit by a phone screen, rain streaking down the windshield, his "
            "thumb hovering over the screen", "Yağmurlu camın ardında telefon ekranına bakan yalnız bir yüz."),
   tiktok="Mert sözünü bozdu 💔 İlk büyük kavga #JozhStudios",
   ig=("Toptancı gelmedi, telefonda 'önce 20.000 ön ödeme' dedi. Ali 'önce sözleşme' dedi.\n\n"
       "Ali eczanedeyken Mert parayı gönderdi ve 500 kutuluk mal sipariş etti. 💔 Rákóczi Müzesi'nin bahçesinde Ali öğrendi.\n\n"
       "İlk kez gerçekten kavga ettik. 'Sözleşme yoksa ben yokum.' Kasa: {KASA}"),
   tags=["#Tekirdağ", "#TekirdağKöftesi", "#Kavga"],
   son="Ali: 'Yarın İstanbul. Sözleşme yoksa ben yokum.'",
   teaser="Gelmeyen bir toptancı, yağmurda verilen yalnız bir karar ve ilk büyük kavga. Bölüm 52: Tekirdağ. Pek yakında.")

# ======================================================================= 53 İSTANBUL
EP(53, "İstanbul", "Büyük Pazar",
   "Toptancı fiyatı yarıya indirir, ön ödeme yanar; Ali gider, Mert İstanbul'da yalnız kalır.",
   "Sabah Eminönü'nde, Mısır Çarşısı'nın arkasındaki bir hanın deposunda toptancıyla buluşurlar. Toptancı sözleşme yerine yeni bir fiyat "
   "söyler: kutu başı 350 lira, yarı fiyat. Ali kalkar; Mert de reddeder. Ön ödeme yanmıştır. Han avlusunda Ali çantasını alır: 'Biraz yalnız "
   "kalmam lazım. Yalova'da babamın bir tanıdığının fidanlığı var.' Mert tek başına Mısır Çarşısı'nda son peyniri satar, Kapalıçarşı'nın "
   "kalabalığında kaybolur. Gece Galata Köprüsü'nde yalnızdır. Ali'den tek satırlık bir mesaj gelir.",
   {"eminonu": ("Eminönü sabahı", "the Eminönü waterfront in İstanbul in the early morning: the New Mosque with its domes, ferries at the "
                "piers, gulls, the Galata Tower across the Golden Horn, light rain"),
    "depo": ("Han deposu", "a dim storage room inside an old stone han behind the Spice Bazaar: stacked cardboard boxes, a single bulb, a "
             "small desk with a calculator"),
    "avlu": ("Han avlusu", "the inner courtyard of an old stone han in Eminönü: worn stone arches, a few parked hand trolleys, a stairway, "
             "grey light"),
    "misir": ("Mısır Çarşısı", "inside the Spice Bazaar in İstanbul: a long vaulted hall with shops piled with colorful spices, Turkish "
              "delight, dried fruits and cheeses, warm lamps"),
    "kopru": ("Galata Köprüsü", "the Galata Bridge at night: fishermen's rods along the railing, the lit mosques and the Galata Tower, lights "
              "reflected in the Golden Horn, light rain")},
   [
       S("08:30 sabah", "eminonu", ["mert", "ali"], "Büyük Şehir",
         "Eminönü'nde sabah. Vapurlar, martılar, Yeni Cami. Kamyoneti otoparka bırakıp sessizce hana yürürler.",
         "Mert and Ali walk side by side along the waterfront without speaking, gulls overhead, ferries arriving; Mert glances at Ali, who keeps "
         "his eyes forward.",
         [("mert", "İstanbul... Hep hayal ederdim buraya böyle gelmeyi.", "trying"),
          ("ali", "Sözleşmeyi görelim, sonra hayal ederiz.", "flat")],
         "slow tracking shot along the waterfront", h="yağmur",
         t=T("ulasim", 1200, "Köprü, otoyol ve otopark")),
       S("10:00 iç-gündüz", "depo", ["mert", "ali", "toptanci"], "Yarı Fiyat",
         "Han deposunda toptancı sözleşme getirmez; yeni bir fiyat söyler: kutu başı 350 lira.",
         "The wholesaler leans back in his chair behind the small desk and taps the calculator, then turns it toward them; Ali stands up "
         "immediately; Mert stares at the number.",
         [("toptanci", "Piyasa değişti. Kutusu üç yüz elli, istersen.", "smooth, cold"),
          ("ali", "Sözleşme yok, söz yok. Gidiyoruz.", "firm")],
         "static medium three-shot across the desk"),
       S("10:15 iç-gündüz", "depo", ["mert", "toptanci"], "Ön Ödeme",
         "Mert ön ödemeyi geri ister. Toptancı 'depo ayrıldı, yanar' der. Kâğıt olmadığı için yapacak bir şey yoktur.",
         "Mert leans on the desk with both hands and asks; the wholesaler spreads his hands with a fake apologetic smile; Mert straightens up slowly, "
         "his jaw tight.",
         [("mert", "Yirmi bini geri ver.", "angry, controlled"),
          ("toptanci", "Depo ayrıldı. Yanar. Kâğıdı olmayanın hakkı da olmaz.", "smug")],
         "slow push-in to Mert's face",
         kurgu="Toptancı kurgusaldır; gerçek bir kişi ya da işletmeyi temsil etmez. Ders: sözlü anlaşmaya para gönderilmez."),
       S("11:00 öğle", "avlu", ["mert", "ali"], "Yalnız Kalmam Lazım",
         "Han avlusunda Ali çantasını omzuna alır: biraz yalnız kalması lazımdır, Yalova'ya gidecektir.",
         "In the stone courtyard Ali swings his backpack onto his shoulder and holds out the brown notebook to Mert; Mert doesn't take it; Ali "
         "places it on a stone step and walks toward the archway; Mert stays frozen.",
         [("ali", "Biraz yalnız kalmam lazım. Yalova'da babamın tanıdığının fidanlığı var.", "tired, sad"),
          ("mert", "Ali... gitme.", "barely audible")],
         "static wide shot of the courtyard, Ali walks away through the arch", h="yağmur"),
       S("15:00 iç-gündüz", "misir", ["mert", "baharatci"], "Tek Başına",
         "Mert tek başına Mısır Çarşısı'nda kalan 10 kilo Ezine peynirini bir dükkâna satar. Defter onun elindedir ama yazmayı bilmez.",
         "Mert hands a tin of cheese to a spice shop owner and receives money; he opens the brown notebook, looks at Ali's neat columns, hesitates "
         "with the pen, and writes clumsily.",
         [("baharatci", "Ezine peyniri mi? On kilo alırım. Arkadaşın nerede?", "curious"),
          ("mert", "Yalova'da. Ben de bu deftere nasıl yazılır bilmiyorum.", "lost")],
         "static medium two-shot in the bazaar",
         t=[U(10, "kg", 650, "satis", "Ezine peyniri, Mısır Çarşısı'nda ({adet} kg x {fiyat} TL)"), T("yemek", 600, "Öğle yemeği (tek kişi)")]),
       S("22:00 gece", "kopru", ["mert"], "Galata Köprüsü",
         "Gece Galata Köprüsü'nde Mert yalnızdır. Ali'den tek satırlık bir mesaj gelir.",
         "Mert leans on the bridge railing between fishermen's rods in the light rain, looking at the lit mosques; his phone buzzes; he reads it "
         "and slowly lowers his head onto his forearms.",
         [("mert", "'Kasa defteri sende. Doğru yaz.' Bu kadar mı Ali?", "reading aloud, broken")],
         "slow push-in from behind the fishermen to Mert", h="yağmur",
         t=T("konaklama", 1500, "Hostel, 1 gece (Mert)")),
   ],
   misafir={"toptanci": ("TOPTANCI", "WHOLESALER, a 45-year-old Turkish man, slicked-back hair, a shiny grey suit, a heavy watch",
                         "adult male voice, smooth, cold, fast Istanbul Turkish"),
            "baharatci": ("BAHARATÇI", "SPICE SHOP OWNER, a 62-year-old Turkish man, white beard, a brown vest, kind eyes", "elderly male voice, curious")},
   ay=AY, hava="yağmur", urun="Mısır Çarşısı, Kapalıçarşı, Eminönü; İstanbul'un tarihi alanları (UNESCO)",
   sponsor="İstanbul'daki yerel esnaf ya da gastronomi alanında",
   kapak=("avlu", ["mert", "ali"], "In a rainy stone courtyard of an old han, Ali walks away through an arch with his backpack while Mert stands "
          "frozen, a brown notebook left on a stone step between them", "Yağmurlu han avlusunda giden Ali, donup kalan Mert ve basamakta defter."),
   yakinda=("kopru", ["mert"], "A lone silhouette on a rainy bridge at night between fishing rods, lit domes and a tower glowing across the "
            "dark water", "Yağmurlu gecede köprüde yalnız bir silüet ve ışıklı kubbeler."),
   tiktok="İstanbul'da her şeyi kaybettik mi? 💔 #JozhStudios",
   ig=("Büyük pazara geldik ama sözleşme gelmedi. Toptancı 'kutusu 350' dedi; 20.000 TL ön ödeme yandı. Kâğıdı olmayanın hakkı olmazmış. 📄💔\n\n"
       "Ali çantasını aldı: 'Biraz yalnız kalmam lazım.' Mert, Mısır Çarşısı'nda defteri tek başına doldurmaya çalıştı.\n\n"
       "Gece Galata Köprüsü'nde tek bir mesaj: 'Kasa defteri sende. Doğru yaz.' Kasa: {KASA}"),
   tags=["#İstanbul", "#Eminönü", "#Ders"],
   son="Ali Yalova'ya gitti. Mert Galata Köprüsü'nde yalnız.",
   teaser="Büyük şehir, yarı fiyat, yanan bir ön ödeme ve giden bir arkadaş. Bölüm 53: İstanbul. Pek yakında.")

# ======================================================================= 54 YALOVA
EP(54, "Yalova", "Fidanlıkta Yalnız",
   "Ali fidanlıkta tek başına çalışır; Mert vapurla peşinden gelir ama kapıda bekler.",
   "Ali, Yalova'da babasının bir tanıdığı olan Gönül Hanım'ın fidanlığında bütün gün saksı taşır ve çiçek fideleri sular; Yalova'nın süs "
   "bitkisi seralarını öğrenir. Gönül Hanım ona 'öfke de fide gibidir, sularsan büyür' der. Mert sabah kamyonetle feribota biner, Ali'nin "
   "videosunu izleyerek gelir. Öğleden sonra fidanlığın kapısına varır ama içeri girmez; dışarıda bekler. Akşam Ali yevmiyesini alıp kapıdan "
   "çıkar ve Mert'i görür.",
   {"fidanlik": ("Yalova fidanlığı", "a large ornamental plant nursery in Yalova: long rows of potted flowers and young shrubs in greenhouses "
                 "and outdoor beds, watering hoses, wheelbarrows, autumn light"),
    "feribot": ("Yalova feribotu", "the car deck and upper deck of a ferry crossing from İstanbul to Yalova: the old white pickup truck parked "
                "below, the grey-blue Sea of Marmara, gulls"),
    "kapi": ("Fidanlık kapısı", "the green metal gate of the plant nursery in Yalova at late afternoon, a low wall with flower pots, the old "
             "white pickup truck parked across the road")},
   [
       S("08:00 sabah", "fidanlik", ["ali", "gonul"], "Saksılar",
         "Ali fidanlıkta saksı taşımaya başlar. Gönül Hanım ona ne yapacağını gösterir ve soru sormaz.",
         "Ali lifts two potted shrubs and carries them along a greenhouse row; Gönül points to where they go with a pair of pruning shears and "
         "watches him with a knowing look.",
         [("gonul", "Hasan'ın oğlu sensin. Soru sormayacağım. Saksılar şuraya.", "kind, brisk"),
          ("ali", "Teşekkürler Gönül Hanım. Soru sormamanız iyi geldi.", "quiet")],
         "slow tracking shot along the greenhouse row"),
       S("09:30 sabah", "feribot", ["mert"], "Peşinden",
         "Mert kamyonetle İstanbul'dan Yalova feribotuna binmiştir. Ali'nin eski videolarını izler.",
         "Mert stands at the ferry railing watching an old video of Ali laughing on his phone; he smiles sadly, locks the phone and looks across "
         "the sea toward the approaching shore.",
         [("mert", "Pazarlığı sen yaparsın, hesabı sen tutarsın... Ben ne yaparım Ali?", "to himself, sad")],
         "slow push-in from the side", h="serin",
         t=T("ulasim", 1100, "İstanbul-Yalova feribotu (kamyonet + 1 kişi)")),
       S("12:30 öğle", "fidanlik", ["ali", "gonul"], "Öfke de Fide Gibidir",
         "Öğle arasında Gönül Hanım çay koyar ve tek bir cümle söyler. Ali ilk kez gülümser.",
         "Gönül pours tea from a thermos into two glasses on an upturned crate between the flower beds; Ali sits on a stool with soil on his hands "
         "and accepts the glass; she speaks while watering a seedling with a small can.",
         [("gonul", "Öfke de fide gibidir. Sularsan büyür, sulamazsan kurur.", "wise"),
          ("ali", "Ben dün akşam çok suladım galiba.", "small smile")],
         "static medium two-shot by the crate"),
       S("15:00 ikindi", "kapi", ["mert"], "Kapıda",
         "Mert fidanlığın kapısına varır ama içeri girmez. Kamyonetin yanında bekler.",
         "Mert parks the pickup across the road, walks to the green gate, raises his hand to open it, stops, and steps back; he leans against the "
         "low wall beside the flower pots and waits, looking at the ground.",
         [("mert", "Bu sefer acele etmeyeceğim. Bekleyeceğim.", "quiet, to himself")],
         "static wide shot across the road"),
       S("17:00 ikindi", "fidanlik", ["ali", "gonul"], "Yevmiye",
         "Akşamüstü Gönül Hanım yevmiyesini verir ve kapıyı işaret eder: dışarıda biri bekliyordur.",
         "Gönül hands Ali folded banknotes and then nods toward the gate with her chin; Ali turns, sees a figure waiting by the wall far away, and "
         "stands still for a moment.",
         [("gonul", "Bir de kapıda iki saattir bekleyen biri var. Sulamamaya karar ver.", "knowing smile"),
          ("ali", "İki saattir mi?", "surprised")],
         "slow push-in past Ali toward the distant gate",
         t=T("diger_gelir", 1500, "Fidanlıkta günlük iş (Ali)")),
       S("18:30 gün batımı", "kapi", ["mert", "ali"], "Kapının İki Yanı",
         "Ali kapıdan çıkar ve Mert'i görür. Mert bir şey söylemez, sadece kamyonetin anahtarını uzatır. Ali almaz: 'Yarın Kocaeli'de konuşalım.'",
         "Ali steps out of the green gate; Mert straightens up from the wall and holds out the pickup key in his open palm without a word; Ali "
         "looks at the key, then at Mert, and gently closes Mert's fingers over it.",
         [("ali", "Anahtar sende kalsın. Yarın Kocaeli'de konuşalım.", "calm, not cold"),
          ("mert", "Tamam. Yarın.", "hopeful")],
         "static medium two-shot at the gate, sunset light",
         t=T("konaklama", 1000, "İki ayrı pansiyon odası, 1 gece")),
   ],
   misafir={"gonul": ("GÖNÜL HANIM", "GÖNÜL, a 58-year-old Turkish nursery owner, sturdy, short grey hair, a green fleece vest, gardening gloves "
                      "tucked in her pocket, rubber boots", "middle-aged female voice, kind, brisk, wise")},
   ay=AY, hava="serin", urun="Süs bitkileri ve fidan, Yalova termal kaplıcaları",
   sponsor="Fidancılık, süs bitkileri ya da termal turizm alanında",
   kapak=("kapi", ["mert", "ali"], "At a green nursery gate at sunset, Mert holds out a key in his open palm and Ali gently closes Mert's fingers "
          "over it, flower pots around them", "Fidanlık kapısında anahtarı uzatan Mert ve parmaklarını kapatan Ali."),
   yakinda=("fidanlik", ["ali"], "Ali alone between long rows of plants in a greenhouse at dusk, soil on his hands, warm light coming through "
            "the plastic roof", "Alacakaranlıkta seranın içinde ellerinde toprakla yalnız Ali."),
   tiktok="Ali fidanlıkta, Mert kapıda 2 saat bekledi 🌱 #JozhStudios",
   ig=("Ali, Yalova'da Gönül Hanım'ın fidanlığında bütün gün çalıştı. Gönül Hanım: 'Öfke de fide gibidir. Sularsan büyür.' 🌱\n\n"
       "Mert vapurla geldi ama içeri girmedi; kapıda iki saat bekledi. Anahtarı uzattı, Ali almadı: 'Yarın Kocaeli'de konuşalım.'\n\n"
       "Kasa: {KASA}"),
   tags=["#Yalova", "#Fidanlık", "#Arkadaşlık"],
   son="Ali: 'Yarın Kocaeli'de konuşalım.' Mert umutlu.",
   teaser="Bir fidanlık, iki saat bekleyen biri ve kapatılan parmaklar. Bölüm 54: Yalova. Pek yakında.")

# ======================================================================= 55 KOCAELİ
EP(55, "Kocaeli", "Pişmaniye",
   "Mert pişmaniye atölyesinde özür dilemenin yolunu bulur; Marmara Kutusu fikri.",
   "Kocaeli'de Mert sabah erkenden bir pişmaniye atölyesine gider. Usta, şeker hamurunun unla binlerce kez çekilerek ince tellere "
   "dönüştüğünü gösterir: 'Sabır olmadan pişmaniye olmaz.' Mert bir kutu pişmaniyeyi kendi eliyle çeker ve içine bir not koyar. Öğlen "
   "Ali'yle İzmit körfezine bakan bir parkta buluşurlar. Ali kutuyu açar, notu okur. Birlikte bir karar verirler: elde kalan 500 kutu "
   "boşa gitmeyecek, 'Marmara Kutusu' olacak. 500 küçük kutu pişmaniye alırlar. Akşam Kartepe'nin yamacında ilk kez yeniden gülerler.",
   {"atolye": ("Pişmaniye atölyesi", "a pişmaniye (cotton candy-like halva) workshop in Kocaeli: masters pulling a ring of caramelized sugar "
               "dough with roasted flour into thousands of fine threads on a big round tray, white flour dust in the air"),
    "park": ("Körfez kıyısında park", "a seaside park in İzmit by the Gulf of İzmit: benches, a promenade, calm grey-blue water, ships far "
             "away, autumn trees"),
    "kartepe": ("Kartepe yamacı", "a viewpoint on the slopes of Kartepe above Kocaeli at sunset: autumn forest in red and gold, the gulf and "
                "the city below, the old white pickup truck parked")},
   [
       S("08:30 iç-gündüz", "atolye", ["mert", "pismaniyeci"], "Binlerce Tel",
         "Mert sabah erkenden pişmaniye atölyesine gider. Usta, şeker hamurunun unla binlerce kez çekilerek tele dönüştüğünü gösterir.",
         "Two masters' hands pull and fold a ring of golden sugar dough on a large round tray dusted with roasted flour, again and again, until it "
         "turns into fine white threads; Mert watches, then joins in, his arms quickly getting tired.",
         [("pismaniyeci", "Çekeceksin, katlayacaksın, yine çekeceksin. Sabır olmadan pişmaniye olmaz.", "rhythmic, wise"),
          ("mert", "Usta, özür de böyle mi? Çekip katlayarak?", "thoughtful, panting")],
         "slow orbit around the round tray"),
       S("10:00 iç-gündüz", "atolye", ["mert", "pismaniyeci"], "Bir Not",
         "Mert kendi çektiği pişmaniyeyi kutuya koyar ve içine elle yazdığı bir not bırakır.",
         "Mert places the fine white threads he pulled into a small box, then writes a short note on a piece of paper, folds it and tucks it under "
         "the lid; the master watches with a small smile and nods.",
         [("pismaniyeci", "Kutu güzel oldu. Not daha güzel olsun.", "encouraging"),
          ("mert", "Bu sefer kâğıda yazdım usta. Sözleşme gibi.", "small smile")],
         "slow push-in on the note and the box"),
       S("12:30 öğle", "park", ["mert", "ali"], "Kutuyu Açmak",
         "Körfez kıyısındaki parkta buluşurlar. Ali kutuyu açar, notu okur. Not: 'Kural iki: önce sana sorarım. Kâğıda yazdım ki unutmayayım.'",
         "Mert hands the small box to Ali on a bench by the water; Ali opens it, unfolds the note and reads it silently; his face softens; he "
         "takes a piece of pişmaniye and eats it slowly.",
         [("ali", "'Kural iki: önce sana sorarım. Kâğıda yazdım ki unutmayayım.'", "reading softly"),
          ("mert", "Bir de... özür dilerim Ali. Yirmi bin için değil. Sözüm için.", "sincere")],
         "slow push-in from the promenade to the bench", h="serin"),
       S("13:00 öğle", "park", ["mert", "ali"], "Marmara Kutusu",
         "Ali bir fikir söyler: elde kalan 500 kutu boşa gitmesin; badem ezmesi, meyve sabunu ve pişmaniyeyle 'Marmara Kutusu' olsun. Mert ona sorar: 'Senin kararın?'",
         "Ali takes the brown notebook from Mert's jacket pocket, opens it and draws a box with three items; Mert leans in, then asks with an open "
         "hand; Ali nods and they shake hands.",
         [("ali", "Beş yüz kutu boşa gitmesin. Badem, sabun, pişmaniye: Marmara Kutusu.", "planning"),
          ("mert", "Önce sana soruyorum: kararın ne?", "careful, smiling")],
         "static medium two-shot over the notebook", h="serin"),
       S("15:00 iç-gündüz", "atolye", ["ali", "pismaniyeci"], "Beş Yüz Küçük Kutu",
         "Atölyeden 500 küçük kutu pişmaniye alırlar. Bu kez pazarlığı birlikte yaparlar.",
         "The workshop master stacks small boxes of pişmaniye on the counter; Ali counts the money while Mert carries boxes to the pickup; they "
         "exchange a quick look and a nod.",
         [("pismaniyeci", "Beş yüz küçük kutu, tanesi altmış.", "businesslike"),
          ("ali", "Anlaştık usta. Faturasıyla lütfen.", "smiling")],
         "static medium two-shot at the counter",
         t=[U(500, "kutu", 60, "alis", "İzmit pişmaniyesi, küçük kutu ({adet} x {fiyat} TL)"), T("yemek", 700, "Öğle yemeği")]),
       S("18:30 gün batımı", "kartepe", ["mert", "ali"], "Yeniden Gülmek",
         "Kartepe'nin yamacında gün batarken ilk kez yeniden gülerler. Mert anahtarı uzatır; Ali bu kez alır.",
         "Mert holds out the pickup key; Ali takes it this time, tosses it once in the air and catches it; both burst out laughing as the autumn "
         "forest glows red and gold around them.",
         [("ali", "Anahtar bende. Defter de bende. Sen de yanımda.", "warm, laughing"),
          ("mert", "Bundan iyi anlaşma olmaz!", "joyful")],
         "slow crane-up revealing the gulf and the forest",
         t=[T("konaklama", 1200, "Otel, 1 gece"), T("ulasim", 600, "Yakıt: Kocaeli-Sakarya")]),
   ],
   misafir={"pismaniyeci": ("PİŞMANİYE USTASI", "PİŞMANİYE MASTER, a 63-year-old Turkish man, slim, white flour dust on his hair and arms, a "
                            "white cap and apron", "elderly male voice, rhythmic and wise")},
   ay=AY, hava="serin", urun="İzmit pişmaniyesi, Kartepe, İzmit Körfezi, sanayi",
   sponsor="Pişmaniye ya da Kartepe turizmi alanında",
   kapak=("park", ["mert", "ali"], "On a seaside bench Ali reads a small handwritten note from an open box of white pişmaniye threads while Mert "
          "watches hopefully, calm gulf behind", "Pişmaniye kutusundaki notu okuyan Ali ve umutla bakan Mert."),
   yakinda=("atolye", ["mert"], "Fine white sugar threads flying in a cloud of flour dust lit by a single shaft of light, Mert's determined face "
            "behind them", "Tek ışık huzmesinde uçuşan ince şeker telleri ve kararlı bir yüz."),
   tiktok="Özür dilemenin en tatlı yolu: pişmaniye 🤍 #JozhStudios",
   ig=("Mert sabah pişmaniye atölyesine gitti. Usta: 'Sabır olmadan pişmaniye olmaz.' Kendi eliyle bir kutu pişmaniye çekti ve içine bir not koydu. 🤍\n\n"
       "Not: 'Kural iki: önce sana sorarım. Kâğıda yazdım ki unutmayayım.'\n\n"
       "Elde kalan 500 kutu boşa gitmeyecek: Marmara Kutusu geliyor! Kartepe'de yeniden güldük. Kasa: {KASA}"),
   tags=["#Kocaeli", "#Pişmaniye", "#Barış"],
   son="Marmara Kutusu hazırlanıyor. Sakarya'da beşinci taksit günü.",
   teaser="Binlerce tel, bir kutu, bir not ve yeniden gülmek. Bölüm 55: Kocaeli. Pek yakında.")

# ======================================================================= 56 SAKARYA
EP(56, "Sakarya", "Sapanca'da Barış",
   "Sezon finali: Marmara Kutusu, ıslama köfte, Sapanca Gölü ve 150.000 TL'lik beşinci taksit.",
   "Sakarya'da bir depoda 300 'Marmara Kutusu' hazırlanır: Edirne badem ezmesi, meyve sabunu ve İzmit pişmaniyesi. Ön siparişler gece "
   "açılmış, sabah tükenmiştir. Öğlen Akyazı usulü ıslama köfte yerler. Sapanca Gölü kıyısında beşinci taksiti gönderirler: 150.000 TL. Ali "
   "onay tuşunu Mert'e bastırır: 'Güven de pişmaniye gibi, yeniden çekilir.' Gölün kıyısında yağmur başlar; Mert ilk kez tişörtüyle "
   "üşüdüğünü itiraf eder. Sırada Karadeniz vardır.",
   {"depo": ("Kiralık depo", "a small rented storage room in Sakarya: long folding tables with rows of plain kraft gift boxes, almond paste, fruit-shaped soaps and pişmaniye boxes, tape and labels"),
    "kofte": ("Islama köfteci", "a roadside ıslama köfte restaurant in Sakarya: grilled meatballs on bread soaked in hot broth, sprinkled with "
              "red pepper, pickles, simple tables"),
    "sapanca": ("Sapanca Gölü kıyısı", "the shore of Lake Sapanca in autumn: a wooden pier, golden and red trees on the hills, calm grey-blue "
                "water, clouds gathering")},
   [
       S("08:30 iç-gündüz", "depo", ["mert", "ali"], "Üç Yüz Kutu",
         "Depoda 300 Marmara Kutusu hazırlanır. Ön sipariş gece açılmış, sabah tükenmiştir.",
         "Mert and Ali work side by side packing boxes on the long table, Mert placing almond paste and a fruit soap, Ali adding pişmaniye and "
         "closing the lid; Ali's phone on the table shows constant notifications.",
         [("ali", "Üç yüz kutu gece açıldı, sabah bitti. Kutusu sekiz yüz.", "proud"),
          ("mert", "Kalan iki yüz kutu Karadeniz'e. Ama önce sana soruyorum.", "smiling")],
         "slow tracking shot along the table",
         t=[U(300, "kutu", 800, "satis", "Marmara Kutusu ({adet} x {fiyat} TL)"), U(300, "kutu", 40, "diger_gider", "Kargo, 300 kutu (300 x 40 TL)")]),
       S("10:30 iç-gündüz", "depo", ["mert", "ali"], "Kayıp Defteri",
         "Ali defterin İstanbul sayfasına kırmızıyla yazar: 20.000 TL ön ödeme. Altına bir ders: 'Kâğıt olmadan para yok.'",
         "Ali opens the brown notebook to a page and writes a line in red, then a sentence under it; Mert reads it over his shoulder and nods "
         "slowly, not looking away.",
         [("ali", "Yirmi bin, kırmızıyla. Altına da ders: kâğıt olmadan para yok.", "calm"),
          ("mert", "Bu sayfayı hiç koparma.", "sincere")],
         "slow push-in on the red line in the notebook"),
       S("13:00 iç-gündüz", "kofte", ["mert", "ali"], "Islama Köfte",
         "Islama köfteyi yerler: sıcak etsuyuna batırılmış ekmeğin üstünde köfte.",
         "Mert lifts a piece of broth-soaked bread with a meatball on it and bites; his eyes go wide; Ali laughs and pushes the pickles toward him.",
         [("mert", "Ekmek etsuyuna batırılmış... Sakarya bunu nasıl buldu?", "amazed, mouth full"),
          ("ali", "Ye. Göl bizi bekliyor.", "smiling")],
         "static medium two-shot across the table",
         t=T("yemek", 800, "Islama köfte (2 kişi)")),
       S("15:30 ikindi", "sapanca", ["mert", "ali"], "Yüz Elli Bin",
         "Sapanca Gölü'nün iskelesinde beşinci taksit gönderilir. Ali onay tuşunu Mert'e bastırır.",
         "Ali holds the phone with the transfer ready and offers it to Mert; Mert hesitates, looking at him; Ali nods; Mert presses send and "
         "they both exhale, the lake behind them.",
         [("ali", "Sen bas. Güven de pişmaniye gibi, yeniden çekilir.", "warm"),
          ("mert", "Yüz elli bin... gitti. Teşekkür ederim Ali.", "moved")],
         "slow push-in on the phone between them on the pier",
         t=T("borc", 150000, "5. taksit: Cemil Bey (Marmara sezonu sonu)")),
       S("17:30 ikindi", "sapanca", ["mert", "ali"], "Beş Yüz Elli Bin",
         "İskelede oturup hesap yaparlar: ödenen 500.000, kalan 300.000. İki bölge kaldı.",
         "Mert and Ali sit on the edge of the wooden pier with their feet above the water; Ali writes the totals in the notebook and shows Mert; "
         "Mert raises two fingers.",
         [("ali", "Beş yüz bin ödendi. Üç yüz bin kaldı.", "focused"),
          ("mert", "İki bölge kaldı. Karadeniz ve İç Anadolu.", "determined")],
         "static medium two-shot on the pier", h="bulutlu"),
       S("19:00 akşam", "sapanca", ["mert", "ali"], "Üşüyorum",
         "Gölün üstünde yağmur başlar. Mert ilk kez tişörtüyle üşüdüğünü itiraf eder. Ali güler: Düzce'de mont alınacaktır.",
         "Rain begins to fall on the lake; Mert hugs himself in his black t-shirt, shivering; Ali laughs, puts his own overshirt over Mert's "
         "shoulders and they run toward the pickup.",
         [("mert", "Ali... itiraf ediyorum. Üşüyorum.", "shivering, comic"),
          ("ali", "Düzce'de ilk iş mont. Karadeniz geliyor!", "laughing")],
         "static wide shot, they run out of frame", h="yağmur",
         t=[T("konaklama", 1200, "Göl kenarı pansiyon, 1 gece"), T("ulasim", 700, "Yakıt: Sakarya-Düzce")],
         kurgu="Sezon sonu kartı (kurguda): SEZON 5 BİTTİ · 11 İL · 5. TAKSİT ÖDENDİ · ÖDENEN 500.000 TL"),
   ],
   ay=AY, hava="bulutlu", urun="Islama köfte, Geyve ayvası, fındık; Sapanca Gölü",
   sponsor="Islama köfte, ayva ya da göl turizmi alanında",
   kapak=("sapanca", ["mert", "ali"], "On a wooden pier at Lake Sapanca with golden autumn hills behind, Mert presses a phone that Ali holds out "
          "to him, both smiling with relief", "Sapanca iskelesinde Ali'nin uzattığı telefona basan Mert."),
   yakinda=("sapanca", ["mert", "ali"], "Two figures running through the first rain along a misty lake shore at dusk, one with a shirt thrown "
            "over the other's shoulders", "Alacakaranlıkta göl kıyısında ilk yağmurda koşan iki figür."),
   tiktok="Sezon 5 finali: barıştık ve 150.000 TL taksit 🤝 #JozhStudios",
   ig=("Marmara bitti! 300 Marmara Kutusu bir gecede tükendi: Edirne badem ezmesi, meyve sabunu, İzmit pişmaniyesi. 📦\n\n"
       "Sapanca'da beşinci taksiti gönderdik: 150.000 TL. Toplam ödenen: 500.000 TL. Ali onay tuşunu Mert'e bastırdı: 'Güven de pişmaniye gibi, yeniden çekilir.' 🤝\n\n"
       "Yağmur başladı, Mert üşüdü. Sezon 6: Karadeniz! Kasa: {KASA}"),
   tags=["#Sakarya", "#Sapanca", "#SezonFinali"],
   son="Yağmur başladı. Düzce'de ilk iş mont. Sırada Karadeniz var.",
   teaser="Üç yüz kutu, bir göl, yüz elli bin ve yeniden kurulan güven. Bölüm 56: Sakarya, sezon finali. Pek yakında.")
