# -*- coding: utf-8 -*-
from ortak import EP, S

# ------------------------------------------------------------------ B21 KAHRAMANMARAŞ
EP(21, {
    "dondurmaci": ("DONDURMA USTASI", "ICE CREAM MASTER, a 45-year-old Turkish man, red vest over white shirt, red fez, long metal paddle, big mustache", "male voice, playful showman"),
    "biberci": ("PUL BİBER ÜRETİCİSİ", "RED PEPPER PRODUCER, a 52-year-old Turkish woman, purple headscarf, red-stained apron, crushed red pepper on trays", "female voice, Maraş accent"),
}, {
    "A": ("Maraş dondurma dükkânı", "a traditional Maraş ice cream shop, a cold metal well of stretchy goat-milk ice cream, long paddles"),
    "B": ("Maraş işi atölyesi", "a small embroidery workshop, gold thread Maraş-style embroidered velvet bundles"),
    "C": ("Biber kurutma damı", "rooftops in Kahramanmaraş with red peppers drying in the sun, sacks of crushed pul biber"),
}, [
    S("Kerem Antep fıstığını dondurmacıya satar.", "A", ["kerem", "dondurmaci"],
      "The ice cream master tastes a pistachio, then playfully stretches a long rope of ice cream on his paddle; he pays Kerem.",
      [("dondurmaci", "Fıstıklı dondurmamız Antep'in fıstığıyla olur. Hepsini alıyorum!"), ("kerem", "Bu dondurma kopmuyor mu?!")], k="s"),
    S("Usta dövme dondurmanın sırrını anlatır, Kerem'le şaka yapar.", "A", ["kerem", "dondurmaci"],
      "The master offers Kerem a cone and keeps pulling it away with tricks; Kerem finally catches it, laughing.",
      [("dondurmaci", "Keçi sütü ve salep! Dövdükçe uzar."), ("kerem", "Tamam usta, yenildim!")]),
    S("Maraş işi sırma işlemeli bohçayı görür.", "B", ["kerem"],
      "Kerem looks at a velvet bundle embroidered with gold thread under a lamp, touching it gently.",
      [("kerem", "Altın tel ile işleme... Bir bohça aylar sürüyormuş.")]),
    S("Deftere not alır.", "C", ["kerem"],
      "Kerem sits on a rooftop among drying red peppers, writing in the notebook.",
      [("kerem", "Maraş'ın dersi: Ustalık acele kabul etmez.")]),
    S("Maraş pul biberi alır.", "C", ["kerem", "biberci"],
      "The producer scoops crushed red pepper into sacks; Kerem sneezes from the pepper dust, they both laugh, he pays.",
      [("biberci", "Güneşte kurudu, yağında kavruldu."), ("kerem", "Hapşu! Kalitesi burnumdan belli!")], k="a"),
    S("Annesi arar: eve avukat mektubu gelmiş, dükkân için dava açılmış.", "C", ["kerem", "~ayse"],
      "Kerem answers the phone; his face goes pale as he listens, the red pepper sacks around him.",
      [("ayse", "Kerem, eve avukat mektubu geldi. Dedenin dükkânı için dava açılmış. Davacı: Karahan.")], kam="slow push-in on Kerem's face"),
])

# ------------------------------------------------------------------ B22 MALATYA
EP(22, {
    "kayisici": ("KAYISI ÜRETİCİSİ", "APRICOT FARMER, a 60-year-old Turkish man, white cap, grey beard, blue work jacket", "male voice, calm, Malatya accent"),
    "malatyali": ("MALATYALI BAKKAL", "GROCER, a 38-year-old Turkish man, round glasses, green apron", "male voice"),
}, {
    "A": ("Malatya çarşısı", "a bazaar street in Malatya with spice shops and apricot stalls"),
    "B": ("Arslantepe Höyüğü", "the Arslantepe archaeological mound near Malatya, excavated mudbrick walls under a protective roof, a display case with ancient swords"),
    "C": ("Kayısı kurutma sergisi", "an apricot drying field, thousands of orange apricots laid on cloths under the sun"),
}, [
    S("Pul biberi bakkala satar.", "A", ["kerem", "malatyali"],
      "The grocer opens a sack of red pepper, smells it and pays Kerem.",
      [("malatyali", "Maraş biberi! Kebapçılar kapışır."), ("kerem", "Tadına baktım, yanaklarım hâlâ yanıyor.")], k="s"),
    S("Annesinden mektubun detayını öğrenir; endişelidir.", "A", ["kerem", "~ayse"],
      "Kerem walks slowly in the bazaar on the phone, worried.",
      [("ayse", "Mektupta dedene 'hırsız' diyorlar oğlum."), ("kerem", "Anne, ben dedemi temize çıkaracağım.")]),
    S("Arslantepe'de dünyanın en eski kılıçlarını görür.", "B", ["kerem"],
      "Kerem looks at ancient swords in a glass case at the mound, reading a sign, impressed.",
      [("kerem", "Beş bin yıllık kılıçlar... Arslantepe, UNESCO listesinde. İnsanlar o zaman da hakkını savunuyormuş.")]),
    S("Üretici kurutma sergisinden almanın farkını anlatır.", "C", ["kerem", "kayisici"],
      "The farmer picks up a sun-dried apricot from the drying cloth and breaks it open for Kerem.",
      [("kayisici", "Ağaçtan değil, sergiden alacaksın. Gün kurusu en tatlısıdır."), ("kerem", "Bal gibi!")]),
    S("Gün kurusu kayısı alır.", "C", ["kerem", "kayisici"],
      "Kerem fills sacks with dried apricots and pays.",
      [("kerem", "Malatya kayısısı, Nemrut'a gidiyor!")], k="a"),
    S("Mektubun ikinci sayfası: 'Hacı Rıza 1979'da kasayı alıp kaçmıştır.'", "C", ["kerem"],
      "At sunset on the drying field, Kerem reads a photo of the lawyer's letter on his phone, clenching his jaw.",
      [("kerem", "Hacı Rıza Aksoy 1979'da ortaklık kasasını alıp kaçmıştır... Yalan!")],
      kam="close-up on phone screen, then Kerem's angry eyes", kurgu="Telefonda mektup: '...1979'da ortaklık kasasını alıp kaçmıştır.'"),
])

# ------------------------------------------------------------------ B23 ADIYAMAN
EP(23, {
    "kahtali": ("KAHTALI ESNAF", "KAHTA SHOPKEEPER, a 44-year-old Turkish man, black beard, grey jacket", "male voice"),
    "besnili": ("BESNİLİ ÜZÜM ÜRETİCİSİ", "GRAPE FARMER, a 58-year-old Turkish woman, white headscarf, dark vest, smiling", "female voice"),
}, {
    "A": ("Nemrut Dağı, gün doğumu", "the summit of Mount Nemrut at sunrise, giant ancient stone heads of kings and gods lined up, golden light"),
    "B": ("Kahta pazarı", "a small market in Kahta, Adıyaman"),
    "C": ("Besni bağı", "a vineyard in Besni with grapes drying into raisins on the ground"),
}, [
    S("Nemrut'ta Elif'le gün doğumunu beklerler.", "A", ["kerem", "elif"],
      "Kerem and Elif wrapped in blankets wait among the giant stone heads as the sun rises; Elif's camera clicks.",
      [("elif", "İki bin yıldır her sabah bu güneşi bekliyorlar."), ("kerem", "Biz de bir sabahlığına onlara katıldık.")]),
    S("Defterdeki öğüdü okur.", "A", ["kerem", "elif"],
      "Kerem reads the notebook in golden light next to a fallen stone head.",
      [("kerem", "'Taş heykel yıkılır, verilen söz kalır.'"), ("elif", "Deden şair miymiş?")]),
    S("Kayısıları Kahta'da satar.", "B", ["kerem", "kahtali"],
      "The shopkeeper tastes an apricot and pays Kerem for the sacks.",
      [("kahtali", "Malatya'nın kayısısı bizim pazarın yıldızı."), ("kerem", "Sergide kurudu abi, gün kurusu!")], k="s"),
    S("Besni bağında kuru üzümün yapılışını görür.", "C", ["kerem", "besnili"],
      "The farmer shows grapes drying on the ground; Kerem tastes a raisin.",
      [("besnili", "Besni'nin üzümü güneşte kurur, şekeri kendinden."), ("kerem", "Doğal şeker deposu!")]),
    S("Besni üzümü alır.", "C", ["kerem", "besnili"],
      "Kerem fills sacks of raisins and pays.",
      [("kerem", "Urfa'ya üzüm götürüyorum.")], k="a"),
    S("Elif'in açık kalan telefon galerisi: defter sayfalarının fotoğrafları, 'Gönderildi'.", "C", ["kerem", "elif"],
      "Elif leaves her phone on a crate; Kerem picks it up to hand it back and sees the screen: photos of his notebook pages; he frowns.",
      [("kerem", "Elif... bunlar benim defterimin sayfaları?")],
      kam="over-the-shoulder on phone screen, Elif walking back unaware", kurgu="Ekranda: defter sayfası fotoğrafları + 'Gönderildi ✓'"),
])

# ------------------------------------------------------------------ B24 ŞANLIURFA (1)
EP(24, {
    "urfali": ("URFALI KURUYEMİŞÇİ", "URFA NUT SELLER, a 50-year-old Turkish man, white skullcap, grey shalwar outfit, traditional vest", "male voice, Urfa accent"),
}, {
    "A": ("Göbeklitepe", "the Göbeklitepe archaeological site under its large protective roof, circles of giant T-shaped carved stone pillars with animal reliefs"),
    "B": ("Urfa çarşısı", "the historic Urfa bazaar (Kapalı Çarşı), narrow lanes, colorful textiles and spices"),
    "C": ("Çarşıda sahte tezgâh", "a market stall in Urfa selling suspicious packages labeled with Kerem's name"),
}, [
    S("Elif telefonu 'belgesel arşivi' diye geçiştirir; Kerem şüphelenir. Göbeklitepe'ye giderler.", "A", ["kerem", "elif"],
      "Kerem and Elif walk on the boardwalk around the giant T-shaped pillars; there is tension between them.",
      [("elif", "O fotoğraflar belgesel arşivi için."), ("kerem", "Peki 'gönderildi' ne demek?")]),
    S("Göbeklitepe'nin 12.000 yıllık hikâyesi.", "A", ["kerem"],
      "Kerem looks at a carved fox on a stone pillar, speaking softly.",
      [("kerem", "On iki bin yıl önce insanlar burada ilk kez bir araya gelip bir şey inşa etmiş. Ticaret de bir arada durmak demek.")],
      kam="slow crane shot over the stone circles"),
    S("Kuru üzümü çarşıda satar ama satış düşük kalır.", "B", ["kerem", "urfali"],
      "The nut seller pays Kerem less than he expected, shaking his head.",
      [("urfali", "Senin adını taşıyan malı sabah daha ucuza aldım."), ("kerem", "Benim adımı taşıyan mal mı?!")], k="s"),
    S("Kerem defterine not alır; şüphesi büyür.", "B", ["kerem"],
      "Kerem sits on a stone step in the bazaar, writing quickly, worried.",
      [("kerem", "Biri adımı kullanıyor. Bu sefer kasadan değil, itibardan çalıyorlar.")]),
    S("Çarşıda 'Kerem'in Kayseri Pastırması' etiketli sahte paketler görür.", "C", ["kerem"],
      "Kerem walks through the lanes and stops in front of a stall full of packages with his own photo on them.",
      [("kerem", "Kerem'in Kayseri Pastırması?! Benim fotoğrafım!")], kurgu="Paket etiketi: 'Kerem'in Kayseri Pastırması'"),
    S("Satıcının arkasında Necmi gülümser.", "C", ["kerem", "necmi"],
      "Behind the stall, a wiry man with a toothpick leans against the wall and smiles at Kerem.",
      [("necmi", "Marka oldun pastırmacı! Hayırlı olsun.")], kam="rack focus from fake packages to Necmi"),
])

# ------------------------------------------------------------------ B25 ŞANLIURFA (2)
EP(25, {
    "urfaesnaf": ("URFALI ESNAF", "URFA SHOPKEEPER, a 65-year-old Turkish man, white beard, traditional black vest and keffiyeh scarf", "elderly male voice, respected elder"),
    "isotcu": ("İSOT ÜRETİCİSİ", "ISOT PEPPER MAKER, a 47-year-old Turkish woman, dark headscarf, sleeves rolled, dark red isot flakes on a cloth", "female voice"),
}, {
    "A": ("Balıklıgöl", "the sacred Balıklıgöl pool in Şanlıurfa with carp fish, stone arches and a mosque reflected in the water"),
    "B": ("Sıra gecesi", "a traditional Urfa sıra gecesi evening, men sitting on floor cushions in a stone room, bağlama and drums, tea and çiğ köfte"),
    "C": ("Harran kümbet evleri ve isot damı", "the beehive-shaped mud-brick dome houses of Harran, with dark red isot peppers drying in the sun"),
}, [
    S("Kerem Balıklıgöl'de sahte ürünler hakkında gerçeği anlatır; esnaf sahip çıkar.", "A", ["kerem", "urfaesnaf", "elif"],
      "By the pool, Kerem speaks to a small crowd while Elif films; the elder shopkeeper raises his hand in support.",
      [("kerem", "O paketler benim değil. Ben malımı kendi elimle satarım."), ("urfaesnaf", "Bu çarşı yalancıya mal sattırmaz!")]),
    S("Sıra gecesinde servis yapar.", "B", ["kerem", "yasar"],
      "Kerem serves tea in a sıra gecesi; Yaşar sits with a bağlama among the musicians.",
      [("kerem", "Kaptan, sen burada da mı varsın?"), ("yasar", "Her türkünün bir durağı var evlat.")]),
    S("Yevmiye alır.", "B", ["kerem"],
      "The host hands Kerem his wage at the door of the sıra gecesi, music continuing inside.",
      [("kerem", "Kasa da türkü söylüyor bu gece.")], k="s"),
    S("Harran'ın kümbet evlerini gezer.", "C", ["kerem", "elif"],
      "Kerem and Elif walk between the beehive-shaped mud houses of Harran at golden hour.",
      [("elif", "Bu evler yazın serin, kışın sıcak tutarmış."), ("kerem", "Binlerce yıllık klima!")]),
    S("İsot alır.", "C", ["kerem", "isotcu"],
      "The woman fills sacks of dark red isot; Kerem pays.",
      [("isotcu", "Güneşte terler, gecede dinlenir; öyle kararır."), ("kerem", "Mardin'e Urfa'nın ateşini götürüyorum.")], k="a"),
    S("Yaşar türküden sonra itiraf eder: '1979 kışında o kervanda ben de vardım.'", "B", ["kerem", "yasar"],
      "Late at night, the room is empty; Yaşar puts down his bağlama and looks at Kerem seriously.",
      [("yasar", "1979 kışında o kervanda ben de vardım, Kerem. Ama şimdi değil... zamanı gelince.")], kam="slow push-in, candle light"),
])

# ------------------------------------------------------------------ B26 MARDİN
EP(26, {
    "lokantaci_m": ("MARDİNLİ LOKANTACI", "MARDIN RESTAURANT OWNER, a 50-year-old Turkish man, short grey hair, white shirt, black vest", "male voice"),
    "telkari": ("TELKARİ USTASI", "FILIGREE MASTER, a 72-year-old Turkish man, thin, magnifying glasses on forehead, black vest, delicate silver wire tools", "elderly male voice, gentle"),
}, {
    "A": ("Mardin taş sokakları", "the honey-colored stone houses of Mardin terraced on a hillside overlooking the Mesopotamian plain"),
    "B": ("Deyrulzafaran Manastırı", "the Deyrulzafaran Monastery near Mardin, golden stone walls and arches"),
    "C": ("Midyat telkari atölyesi", "a filigree silver workshop in Midyat, fine silver wires, glass display cases with silver jewelry"),
}, [
    S("İsotu Mardin'deki lokantaya satar.", "A", ["kerem", "lokantaci_m"],
      "On a stone terrace restaurant, the owner smells the isot and pays Kerem.",
      [("lokantaci_m", "Kaburga dolmasına Urfa isotu yakışır."), ("kerem", "Komşudan komşuya!")], k="s"),
    S("Taş sokaklarda yürürken Mezopotamya ovasına bakar.", "A", ["kerem", "elif"],
      "Kerem and Elif stand on a terrace looking at the endless plain; Elif films.",
      [("elif", "Bu taşlar güneşi içine çekip akşam geri veriyor."), ("kerem", "Şehir değil, açık hava müzesi.")]),
    S("Deyrulzafaran Manastırı'nı gezer.", "B", ["kerem"],
      "Kerem walks through the golden stone arches of the monastery, quiet and respectful.",
      [("kerem", "Yüzyıllardır aynı yerde duruyor... Sabır taştan öğrenilir.")]),
    S("Midyat'ta telkari ustası gümüş telleri örmeyi gösterir.", "C", ["kerem", "telkari"],
      "The old master twists thin silver wires into a delicate pattern with tweezers under a lamp.",
      [("telkari", "Gümüş tel saç teli kadar incedir; nefes alırken bile dikkat."), ("kerem", "Nefesimi tutuyorum usta.")]),
    S("Telkari takılar alır.", "C", ["kerem", "telkari"],
      "Kerem pays for delicate silver filigree jewelry placed in velvet boxes.",
      [("kerem", "Diyarbakır'ın hanlarına Midyat gümüşü.")], k="a"),
    S("Usta çekmeceden gümüş bir anahtar yarısı çıkarır.", "C", ["kerem", "telkari"],
      "The master opens a hidden drawer and places half of a small ornate silver filigree key in Kerem's palm.",
      [("telkari", "Deden 2008'de yaptırdı. 'Torunum gelirse ver' dedi.")], kam="extreme close-up on the half key in Kerem's palm"),
])

# ------------------------------------------------------------------ B27 DİYARBAKIR (1)
EP(27, {
    "kuyumcu": ("HAN KUYUMCUSU", "JEWELER, a 55-year-old Turkish man, neat grey beard, burgundy vest, jeweler's loupe", "male voice, polite"),
}, {
    "A": ("Hasan Paşa Hanı", "the historic Hasan Paşa Han in Diyarbakır, black and white striped stone arches, a courtyard full of breakfast tables"),
    "B": ("Diyarbakır Surları ve Hevsel Bahçeleri", "the massive black basalt city walls of Diyarbakır overlooking the green Hevsel Gardens and the Tigris river"),
}, [
    S("Telkari takıları handaki kuyumcuya satar.", "A", ["kerem", "kuyumcu"],
      "The jeweler inspects the filigree with a loupe and nods, paying Kerem.",
      [("kuyumcu", "Midyat işi, hakiki usta eli."), ("kerem", "Ustası 72 yaşında, eli hâlâ titremiyor.")], k="s"),
    S("Handa kahvaltı eder, hanların ticaretteki yerini anlatır.", "A", ["kerem", "elif"],
      "Kerem and Elif eat a huge Diyarbakır breakfast in the han courtyard.",
      [("kerem", "Hanlar eskiden tüccarların oteli, bankası, borsasıymış."), ("elif", "Ve kahvaltısı efsane.")]),
    S("Surlarda yürür, Hevsel'e bakar.", "B", ["kerem", "elif"],
      "Kerem and Elif walk on top of the black basalt walls, the green gardens and the Tigris below.",
      [("elif", "Bu surlar ve Hevsel Bahçeleri UNESCO listesinde."), ("kerem", "Kale gibi şehir, bahçe gibi yürek.")]),
    S("Kerem iki anahtar fikrini düşünür; deftere yazar.", "B", ["kerem"],
      "Kerem sits on the wall holding the half silver key against the sky, then writes in the notebook.",
      [("kerem", "Yarım anahtar... Öbür yarısı nerede dede?")]),
    S("Leyla Diyarbakır'a gelir, elinde notlar.", "A", ["kerem", "leyla"],
      "Leyla hurries into the han courtyard with a satchel of papers and sits down breathless.",
      [("leyla", "Uçakla geldim, telefonda anlatılmazdı."), ("kerem", "Ne buldunuz?")]),
    S("Leyla: '81 isim alacaklı değil, deden onlara borçluymuş.'", "A", ["kerem", "leyla"],
      "Leyla spreads papers on the table and points to the list; Kerem leans forward in shock.",
      [("leyla", "81 isim alacaklı değil Kerem. Deden onlara borçluymuş. Ve senin rotan... onun borç ödeme rotası.")],
      kam="slow push-in on Kerem's face"),
])

# ------------------------------------------------------------------ B28 DİYARBAKIR (2)
EP(28, {
    "cigerci": ("CİĞERCİ USTA", "LIVER KEBAB MASTER, a 48-year-old Turkish man, black beard, white t-shirt, black apron, fanning a charcoal grill", "male voice, Diyarbakır accent"),
    "kadayifci": ("KADAYIFÇI", "DESSERT MAKER, a 60-year-old Turkish man, white cap, round belly, white apron, trays of burma kadayıf", "male voice, cheerful"),
}, {
    "A": ("On Gözlü Köprü", "the ancient Ten-Eyed Bridge (On Gözlü Köprü) over the Tigris river near Diyarbakır at sunset"),
    "B": ("Ciğerci dükkânı, akşam", "a busy liver kebab shop in Diyarbakır at night, charcoal smoke, skewers"),
    "C": ("Kadayıf dükkânı", "a dessert shop with trays of rolled green pistachio burma kadayıf"),
}, [
    S("On Gözlü Köprü'de dedesinin neden her ile gittiğini anlar.", "A", ["kerem", "leyla"],
      "Kerem and Leyla walk on the ancient bridge at sunset; Kerem looks at the notebook's map.",
      [("kerem", "Dedem kaçmamış... borç ödemek için il il gezmiş."), ("leyla", "Kaçan biri dönüp borç ödemez.")]),
    S("Ciğerci dükkânında akşam servisinde çalışır.", "B", ["kerem", "cigerci"],
      "Kerem carries plates of liver kebab through a crowded shop; the master fans the grill.",
      [("cigerci", "Ciğer sıcak gidecek, soğursa yüzüme bakmaz müşteri!"), ("kerem", "Koşuyorum usta!")]),
    S("Yevmiye alır.", "B", ["kerem", "cigerci"],
      "The master gives Kerem his wage and a skewer.",
      [("cigerci", "Hızlısın, yine gel."), ("kerem", "Kasam da hızlandı sayenizde.")], k="s"),
    S("Defterine öğüt yazar.", "A", ["kerem"],
      "Kerem sits on the bridge at night writing, the river reflecting the lights.",
      [("kerem", "Diyarbakır'ın dersi: Borç, kapanana kadar insanın sırtındadır.")]),
    S("Burma kadayıf alır.", "C", ["kerem", "kadayifci"],
      "The dessert maker packs trays of green pistachio kadayıf; Kerem pays.",
      [("kadayifci", "Batman'a gidene ikram da var!"), ("kerem", "Bu tepsiler kasamdan tatlı.")], k="a"),
    S("Selim'in videosu viral olur: 'Aksoy ailesi dolandırıcıdır.'", "C", ["kerem"],
      "Kerem's phone buzzes nonstop with notifications; he opens a video and his face falls.",
      [("kerem", "Aksoy ailesi dolandırıcıdır... Bir milyon izlenme?!")],
      kam="phone light on Kerem's face", kurgu="Telefonda viral video: Selim, başlık 'Aksoy ailesi dolandırıcıdır'"),
])

# ------------------------------------------------------------------ B29 BATMAN
EP(29, {
    "batmanli": ("BATMANLI ESNAF", "BATMAN SHOPKEEPER, a 42-year-old Turkish woman, light blue headscarf, red cardigan", "female voice"),
    "gilorikci": ("GILORİK USTASI", "GILORIK COOK, a 55-year-old Turkish woman, white headscarf, flour on hands, shaping stuffed bulgur balls", "female voice, warm"),
}, {
    "A": ("Batman çarşısı", "a market street in Batman city"),
    "B": ("Hasankeyf, Zeynel Bey Türbesi", "the relocated Zeynel Bey Tomb in New Hasankeyf, a cylindrical tomb with blue tiles near the Tigris"),
    "C": ("Gılorik mutfağı", "a home kitchen making gılorik stuffed bulgur balls, trays, steam"),
    "D": ("Otobüs bagajı, gece", "the luggage compartment of an intercity bus at night at a stop, an insulated cooler box"),
}, [
    S("Viral videoya rağmen kadayıfları satar.", "A", ["kerem", "batmanli"],
      "The shopkeeper recognizes Kerem from the video, hesitates, then tastes the kadayıf and pays.",
      [("batmanli", "Videonu gördüm ama malın konuşuyor."), ("kerem", "Malım yalan söylemez abla.")], k="s"),
    S("Taşınan Zeynel Bey Türbesi'ni görür.", "B", ["kerem"],
      "Kerem stands before the blue-tiled tomb, the river behind.",
      [("kerem", "Baraj yüzünden taşınmış. Bazı şeyler korumak için yerinden oynatılır.")]),
    S("Elif'e videoyu sorar; Elif cevap vermez.", "B", ["kerem", "elif"],
      "Kerem shows Elif the viral video; she looks away.",
      [("kerem", "Bu videodaki fotoğraflar senin kamerandan."), ("elif", "Ben... sonra konuşalım.")]),
    S("Gılorik yapımını öğrenir.", "C", ["kerem", "gilorikci"],
      "The cook shapes a stuffed bulgur ball with her finger quickly; Kerem's falls apart.",
      [("gilorikci", "Batman'ın içli köftesine gılorik derler. Coğrafi işaretli!"), ("kerem", "Benimki gılorik değil, gıl-oops!")]),
    S("Dondurulmuş gılorik alır.", "C", ["kerem", "gilorikci"],
      "Kerem packs frozen gılorik in an insulated cooler and pays.",
      [("kerem", "Soğutucuyu bu sefer gözümden ayırmayacağım.")], k="a"),
    S("Bagajda soğutucunun fişi çekilmiş; yanında kartvizit.", "D", ["kerem"],
      "At a night stop Kerem checks the luggage; the cooler plug is pulled out, a business card stuck on top.",
      [("kerem", "Yine mi?! Necmi!")], kam="flashlight reveals the unplugged cable and the card", kurgu="Kartvizit: 'Karahan Lojistik'"),
])

# ------------------------------------------------------------------ B30 SİİRT
EP(30, {
    "siirtli": ("SİİRTLİ LOKANTACI", "SIIRT RESTAURANT OWNER, a 50-year-old Turkish man, round face, black mustache, white apron", "male voice, sympathetic"),
    "fistikci_s": ("SİİRT FISTIĞI ÜRETİCİSİ", "PISTACHIO FARMER, a 62-year-old Turkish man, white skullcap, grey beard, brown jacket", "elderly male voice"),
}, {
    "A": ("Siirt lokantası", "a büryan kebab restaurant in Siirt with a deep pit oven"),
    "B": ("Tillo, İbrahim Hakkı türbesi", "the hilltop town of Tillo near Siirt, a small stone tomb with a window where sunlight falls on a specific day"),
    "C": ("Siirt fıstığı bahçesi", "a pistachio orchard near Siirt, large Siirt pistachios"),
}, [
    S("Gıloriklerin yarısı çözülüp bozulmuş; ikinci zarar.", "A", ["kerem"],
      "Kerem opens the cooler; half the gılorik are thawed and spoiled, he closes his eyes in frustration.",
      [("kerem", "Yarısı gitti... Kasa yine zarar.")]),
    S("Kalanını ucuza lokantaya satar.", "A", ["kerem", "siirtli"],
      "The restaurant owner takes the good ones and pays a lower price, patting Kerem's shoulder.",
      [("siirtli", "Bozukları alma dedin, dürüstlüğüne büryan ısmarlıyorum."), ("kerem", "Zarar ettim ama aç kalmadım.")], k="s"),
    S("Büryan kebabının tandırdan çıkışı.", "A", ["kerem", "siirtli"],
      "The owner pulls a whole slow-cooked lamb out of a pit oven; Kerem's eyes widen.",
      [("siirtli", "Büryan: kuyu tandırda saatlerce pişer."), ("kerem", "Kebap değil, sabır ödülü!")]),
    S("Tillo'da İbrahim Hakkı'nın astronomi mirasını öğrenir.", "B", ["kerem", "~leyla"],
      "Kerem stands at the small tomb on the hill; a beam of sunlight comes through a window.",
      [("kerem", "Yılda iki kez güneş ışığı tam buraya düşüyormuş!"), ("leyla", "İbrahim Hakkı... Marifetname'nin yazarı.")]),
    S("Siirt fıstığı alır.", "C", ["kerem", "fistikci_s"],
      "The farmer shows big pistachios; Kerem buys sacks.",
      [("fistikci_s", "Siirt fıstığı iri ve yağlıdır."), ("kerem", "Cizre'ye fıstık götürüyorum.")], k="a"),
    S("Leyla mührün kenarındaki yazıyı çözer: '82. adımda açılır.'", "B", ["kerem", "~leyla"],
      "At sunset on the hill Kerem holds the notebook close to the camera on a video call, the red seal visible.",
      [("leyla", "Mührün kenarındaki yazı: 'Son sayfa 81. ilde değil... 82. adımda açılır.'")], kam="close-up on the red wax seal"),
])

# ------------------------------------------------------------------ B31 ŞIRNAK
EP(31, {
    "cizreli": ("CİZRELİ ESNAF", "CIZRE SHOPKEEPER, a 45-year-old Turkish man, black beard, traditional şal-şapik outfit", "male voice"),
    "kengerci": ("KENGER KAHVESİ ÜRETİCİSİ", "KENGER COFFEE MAKER, a 50-year-old Turkish woman, colorful headscarf, roasting kenger seeds in a pan", "female voice"),
}, {
    "A": ("Cizre çarşısı", "a market in Cizre near the Tigris"),
    "B": ("Cudi Dağı manzarası", "Mount Cudi rising in the distance under a dramatic sky, seen from a hill"),
    "C": ("Kırmızı Medrese", "the historic Red Madrasa (Kırmızı Medrese) in Cizre, red stone walls"),
    "D": ("Otobüs içi, akşam", "inside a bus in the evening, mountain road outside"),
}, [
    S("Siirt fıstığını Cizre çarşısında satar.", "A", ["kerem", "cizreli"],
      "The shopkeeper cracks a pistachio and pays Kerem.",
      [("cizreli", "Siirt'in fıstığı, Cizre'nin tezgâhı."), ("kerem", "Komşu malı!")], k="s"),
    S("Cudi Dağı ve Nuh'un gemisi rivayeti.", "B", ["kerem", "elif"],
      "Kerem and Elif look at the mountain from a hill; Elif points.",
      [("elif", "Rivayete göre Nuh'un gemisi Cudi'ye oturmuş."), ("kerem", "Tufandan sonra yeniden başlamak...")]),
    S("Kırmızı Medrese'de Mem û Zîn hikâyesini dinler.", "C", ["kerem"],
      "Kerem walks through the red stone madrasa courtyard.",
      [("kerem", "Mem ile Zin'in aşkı burada anlatılırmış. Bazı hikâyeler yüzyıllar sürüyor.")]),
    S("Kenger kahvesinin yapılışını görür.", "A", ["kerem", "kengerci"],
      "The woman roasts kenger seeds in a pan and pours dark coffee; Kerem tastes it.",
      [("kengerci", "Kenger dikenli bir bitkidir, kahvesi şifadır."), ("kerem", "Kahve değil, dağın tadı.")]),
    S("Kenger kahvesi alır.", "A", ["kerem", "kengerci"],
      "Kerem pays for packages of kenger coffee.",
      [("kerem", "Hakkari yolcusu kenger!")], k="a"),
    S("Yaşar Hakkari otobüsünde soluk bir zarf uzatır.", "D", ["kerem", "yasar"],
      "Yaşar driving, hands an old yellowed envelope back to Kerem without turning.",
      [("yasar", "1979'dan... Ama içini Van'da aç.")], kam="over-the-shoulder from Kerem to Yaşar's eyes in the mirror"),
])

# ------------------------------------------------------------------ B32 HAKKARİ
EP(32, {
    "hakkarili": ("HAKKARİLİ ESNAF", "HAKKARI SHOPKEEPER, a 40-year-old Turkish man, wool cap, thick jacket", "male voice"),
    "kilimci": ("HAKKARİ KİLİMCİSİ", "KILIM WEAVER, a 55-year-old Turkish woman, colorful layered headscarf, embroidered vest, at a loom", "female voice, proud"),
}, {
    "A": ("Hakkari çarşısı", "a mountain town market in Hakkari with the snowy Cilo mountains behind"),
    "B": ("Meydan Medresesi", "the 14th-century Meydan Madrasa in Hakkari, old stone building"),
    "C": ("Kilim dokuma evi", "a weaving house in Hakkari, famous geometric Hakkari kilims on looms"),
    "D": ("Güzeldere geçidi, tipi", "a snowy mountain pass road in a blizzard, a stopped bus with hazard lights"),
}, [
    S("Kenger kahvesini satar.", "A", ["kerem", "hakkarili"],
      "The shopkeeper smells the kenger and pays.",
      [("hakkarili", "Dağın kahvesi dağa yakışır."), ("kerem", "Cilo'nun eteğinde kahve molası!")], k="s"),
    S("Cilo-Sat dağlarının manzarası.", "A", ["kerem", "elif"],
      "Kerem and Elif stare at the giant snowy peaks; Elif films.",
      [("elif", "Cilo, Türkiye'nin en yüksek dağlarından."), ("kerem", "Kasam da bu kadar yükselse...")]),
    S("Meydan Medresesi'ni gezer.", "B", ["kerem"],
      "Kerem walks in the old madrasa, touching the stone wall.",
      [("kerem", "Altı yüz yıllık okul. Dedem de burada ders almış gibi.")]),
    S("Kilimci kadın Hakkari kilimlerinin motiflerini anlatır.", "C", ["kerem", "kilimci"],
      "The weaver points to motifs on a kilim; Kerem listens.",
      [("kilimci", "Bu motif koç boynuzu: güç. Bu da el ele: birlik."), ("kerem", "Her kilim bir mektup gibi.")]),
    S("Hakkari kilimi alır.", "C", ["kerem", "kilimci"],
      "Kerem pays and the weaver rolls small kilims.",
      [("kerem", "Van'a Hakkari'nin mektuplarını götürüyorum.")], k="a"),
    S("Van yolunda tipi; otobüs geçitte durur, zarf ıslanmaya başlar.", "D", ["kerem", "yasar"],
      "Inside the stopped bus in a blizzard, snow hits the windows; Kerem protects the envelope under his jacket as melting snow drips.",
      [("yasar", "Yol kapandı, sabaha kadar buradayız."), ("kerem", "Zarf ıslanıyor kaptan!")], kam="handheld, snow storm outside"),
])

# ------------------------------------------------------------------ B33 VAN (1)
EP(33, {
    "vanli": ("VANLI HALICI", "VAN CARPET SHOP OWNER, a 52-year-old Turkish man, grey beard, wool vest", "male voice"),
}, {
    "A": ("Van çarşısı", "a market street in Van with carpet and cheese shops"),
    "B": ("Van kahvaltı salonu", "a Van breakfast salon, a table covered with dozens of small plates of cheeses, honey, kaymak, herbs"),
    "C": ("Van Kedisi Evi", "the Van Cat House, white fluffy Van cats with one blue and one amber eye"),
    "D": ("Otel odası", "a small hotel room in Van, window with view of Lake Van"),
}, [
    S("Tipi diner; kilimleri Van çarşısında satar.", "A", ["kerem", "vanli"],
      "The carpet seller examines the kilims and pays Kerem generously.",
      [("vanli", "Hakkari kilimi! Bu motifleri tanırım."), ("kerem", "Tipiden sağ çıktı, fiyatı da sağlam olsun abi.")], k="s"),
    S("Van kahvaltısında kırk çeşit.", "B", ["kerem", "elif", "yasar"],
      "Kerem, Elif and Yaşar sit at a table covered with dozens of small plates; Kerem tries to count them.",
      [("kerem", "Otuz sekiz, otuz dokuz, kırk!"), ("yasar", "Van kahvaltısı say diye değil, ye diye var.")]),
    S("Van Kedisi Evi'nde kediler.", "C", ["kerem", "elif"],
      "A white Van cat with one blue and one amber eye jumps into Kerem's lap.",
      [("elif", "Bir gözü mavi, bir gözü kehribar."), ("kerem", "Bu kedi de iki yüzlü mü?")]),
    S("Zarfı açar: 1979'dan bir otobüs bileti, 'Kayseri–Sivas'.", "D", ["kerem"],
      "Kerem opens the slightly wet envelope; inside is an old bus ticket.",
      [("kerem", "Kayseri–Sivas... 14 Şubat 1979. Yaşar bunu neden saklamış?")], kam="close-up on the old ticket", kurgu="Bilet: 'Kayseri – Sivas, 14.02.1979'"),
    S("Elif telefonunu masada unutur; Kerem ekranda bir mesaj görür.", "D", ["kerem"],
      "Elif's phone lights up on the table; Kerem glances at it and freezes.",
      [("kerem", "S.K.?")], kurgu="Telefon ekranı: 'S.K.: Defterin son sayfalarını da çek. Ödemen yattı.'"),
    S("Kerem mesajı okur: 'Ödemen yattı.' Elif kapıda belirir.", "D", ["kerem", "elif"],
      "Elif enters the room and sees Kerem holding her phone; they stare at each other in silence.",
      [("kerem", "Selim Karahan sana para mı ödüyor?")], kam="slow push-in on Elif's face, guilt"),
])

# ------------------------------------------------------------------ B34 VAN (2)
EP(34, {
    "kahvaltici": ("KAHVALTI SALONU SAHİBİ", "BREAKFAST SALON OWNER, a 58-year-old Turkish woman, black headscarf, embroidered apron", "female voice"),
    "otluci": ("OTLU PEYNİRCİ", "HERB CHEESE MAKER, a 60-year-old Turkish man, white mustache, grey cap, wool sweater", "male voice"),
}, {
    "A": ("Akdamar tekne yolu", "a small boat crossing Lake Van toward Akdamar Island with its medieval stone church, turquoise water"),
    "B": ("Van Kalesi", "the ancient Van Fortress (Tuşpa, Urartian) on a long rock above the lake"),
    "C": ("Kahvaltı salonu, sabah", "a Van breakfast salon in the early morning"),
    "D": ("Otel odası, sabah", "a small hotel room in Van, morning light, an empty bed"),
}, [
    S("Kerem soğuk bir sessizlikle tekneyle Akdamar'a gider; Elif açıklamaya çalışır.", "A", ["kerem", "elif"],
      "On the boat, Kerem stares at the island, Elif sits next to him trying to talk.",
      [("elif", "Açıklayabilirim."), ("kerem", "Akdamar'ı izliyorum.")]),
    S("Van Kalesi'nde Urartu'nun Tuşpa'sı.", "B", ["kerem"],
      "Kerem climbs the rock fortress alone, looking at cuneiform inscriptions.",
      [("kerem", "Urartular bu kayaya şehir kurmuş. Ben güvenimi kuramıyorum.")]),
    S("Kahvaltı salonunda sabah servisinde çalışır.", "C", ["kerem", "kahvaltici"],
      "Kerem serves dozens of plates quickly; the owner nods.",
      [("kahvaltici", "Ağzın sıkı, elin çabuk. İyi çalıştın."), ("kerem", "Kafamı dağıtmam lazımdı abla.")]),
    S("Yevmiye alır.", "C", ["kerem", "kahvaltici"],
      "The owner pays Kerem's wage.",
      [("kerem", "Teşekkürler.")], k="s"),
    S("Otlu peynir alır.", "C", ["kerem", "otluci"],
      "The cheese maker shows cheese with wild herbs inside; Kerem buys.",
      [("otluci", "Dağ otları peynirin içinde bir yıl bekler."), ("kerem", "Bitlis'e otlu peynir.")], k="a"),
    S("Sabah Elif'in odası boş; masada bir not.", "D", ["kerem"],
      "Kerem enters Elif's room; the bed is empty, a handwritten note on the table.",
      [("kerem", "Her şeyi düzelteceğim. Bana güven... Elif!")], kam="slow pan to the note", kurgu="Not: 'Her şeyi düzelteceğim. Bana güven. — Elif'"),
])

# ------------------------------------------------------------------ B35 BİTLİS
EP(35, {
    "bitlisli": ("BİTLİSLİ ESNAF", "BITLIS SHOPKEEPER, a 48-year-old Turkish man, grey jacket", "male voice"),
    "tasci": ("AHLAT TAŞ USTASI", "STONE CARVER, a 67-year-old Turkish man, stone dust on clothes, thick hands, chisel and hammer", "elderly male voice"),
}, {
    "A": ("Bitlis çarşısı", "a narrow valley town market in Bitlis with old stone houses"),
    "B": ("Ahlat Selçuklu Meydan Mezarlığı", "the Seljuk cemetery in Ahlat with tall carved tombstones covered with intricate patterns, Lake Van behind"),
    "C": ("Nemrut Krater Gölü", "the Nemrut crater lake near Tatvan, blue water inside a volcanic crater"),
    "D": ("Taş atölyesi", "an Ahlat stone carving workshop, reddish volcanic stone, small carved souvenirs"),
}, [
    S("Otlu peyniri satar.", "A", ["kerem", "bitlisli"],
      "The shopkeeper tastes the herb cheese and pays.",
      [("bitlisli", "Van'ın otlusu, Bitlis'in kahvaltısı."), ("kerem", "Afiyet olsun abi.")], k="s"),
    S("Ahlat'ın oymalı mezar taşları.", "B", ["kerem"],
      "Kerem walks among tall carved Seljuk tombstones.",
      [("kerem", "Selçuklu mezar taşları... Taşa dantel işlemişler.")]),
    S("Nemrut Krater Gölü.", "C", ["kerem"],
      "Kerem stands on the crater rim, wind blowing.",
      [("kerem", "Bir yanardağın içinde göl. Ateşten sonra su gelirmiş.")]),
    S("Şerefname'yi ve Bitlis'in tarihini düşünür, deftere yazar.", "C", ["kerem"],
      "Kerem sits on a rock writing.",
      [("kerem", "Elif gitti. Ama dedem yazmış: 'Güveni kıran da onarabilir.'")]),
    S("Ahlat taşından hediyelik alır.", "D", ["kerem", "tasci"],
      "The carver hands Kerem small carved stones; Kerem pays.",
      [("tasci", "Ahlat taşı yumuşak işlenir, sert durur."), ("kerem", "Muş'a taş götürüyorum, ağır ama değerli.")], k="a"),
    S("Usta: 'Deden her yıl gelip bir borç kapatırdı.'", "D", ["kerem", "tasci"],
      "The old carver stops working and looks at the notebook in Kerem's bag.",
      [("tasci", "Deden her yıl gelip bir borç kapatırdı. Son gelişinde 'Bir gün torunum son borcu kapatacak' dedi.")], kam="close-up on the carver's eyes"),
])

# ------------------------------------------------------------------ B36 MUŞ
EP(36, {
    "muslu": ("MUŞLU ESNAF", "MUŞ SHOPKEEPER, a 50-year-old Turkish man, flat cap, brown coat", "male voice"),
    "orucu": ("KOOPERATİF ÖRÜCÜSÜ", "WOOL KNITTER, a 46-year-old Turkish woman, red headscarf, knitting colorful wool socks", "female voice, warm"),
}, {
    "A": ("Muş çarşısı", "a market street in Muş, plains behind"),
    "B": ("Malazgirt Meydan Muharebesi alanı", "the wide Malazgirt plain with a memorial monument, open sky"),
    "C": ("Muş lalesi tarlası", "a field of endemic red Muş tulips on a hillside"),
    "D": ("Kadın kooperatifi", "a women's cooperative room with colorful knitted wool socks with tulip patterns"),
}, [
    S("Ahlat taşı hediyelikleri satar.", "A", ["kerem", "muslu"],
      "The shopkeeper turns a carved stone in his hand and pays.",
      [("muslu", "Ahlat işi sağlamdır."), ("kerem", "Taşın kendisi de ustası da sağlam.")], k="s"),
    S("Malazgirt ovasında 1071'i anlatır.", "B", ["kerem"],
      "Kerem stands at the monument on the wide plain, wind blowing.",
      [("kerem", "1071, Malazgirt. Anadolu'nun kapısı burada açıldı.")], kam="wide drone shot"),
    S("Endemik Muş lalesi tarlası.", "C", ["kerem"],
      "Kerem kneels among red tulips without picking them.",
      [("kerem", "Muş lalesi sadece burada yetişiyor. Koparmak yok, bakmak serbest.")]),
    S("Kooperatifte lale motifli çorap örülür.", "D", ["kerem", "orucu"],
      "The knitter shows a sock with a red tulip pattern.",
      [("orucu", "Laleyi koparmayız, çoraba öreriz."), ("kerem", "Bu çoraplar Bingöl'ün soğuğunda kapışılır.")]),
    S("El örgüsü yün çorap alır.", "D", ["kerem", "orucu"],
      "Kerem pays and fills a bag with knitted socks.",
      [("kerem", "Kasamı da ısıtsın inşallah.")], k="a"),
    S("Avukattan mesaj: Duruşma 60 gün sonra, belge yoksa dükkân gider.", "A", ["kerem", "~ayse"],
      "Kerem on the phone with his mother, looking down.",
      [("ayse", "Avukat aradı. Duruşma 60 gün sonra Ankara'da. Belge yoksa dükkânı kaybediyoruz."), ("kerem", "60 gün... yetişeceğim anne.")], kam="slow push-in"),
])

# ------------------------------------------------------------------ B37 BİNGÖL
EP(37, {
    "binglu": ("BİNGÖLLÜ ESNAF", "BINGÖL SHOPKEEPER, a 45-year-old Turkish man, thick wool coat, beanie", "male voice"),
    "sahtebalci": ("SAHTE BALCI", "FAKE HONEY SELLER, a 35-year-old Turkish man, shifty eyes, leather jacket, too-wide smile", "male voice, pushy"),
    "aricı": ("ARICI", "BEEKEEPER, a 60-year-old Turkish man, beekeeping veil on hat, white overalls, honeycomb in hand", "male voice, calm"),
}, {
    "A": ("Bingöl yayla pazarı", "a cold highland market in Bingöl, snowy peaks"),
    "B": ("Solhan yüzen adalar", "the floating islands of Solhan, small grassy islands moving on a lake"),
    "C": ("Arı kovanları", "beehives on a mountain slope in Bingöl, flowers"),
}, [
    S("Yün çorapları soğukta kolayca satar.", "A", ["kerem", "binglu"],
      "The shopkeeper rubs his cold hands and buys all the wool socks.",
      [("binglu", "Bu soğukta çorap altın değerinde!"), ("kerem", "Muş'un lalesi Bingöl'ü ısıtsın.")], k="s"),
    S("Solhan'ın yüzen adaları.", "B", ["kerem"],
      "Kerem watches a small grassy island slowly drift on the lake.",
      [("kerem", "Ada yüzüyor! Burada toprak bile yolculuk yapıyor.")]),
    S("Bir satıcı çok ucuza 'Bingöl balı' teklif eder.", "A", ["kerem", "sahtebalci"],
      "A pushy seller holds a jar of honey very close to Kerem's face.",
      [("sahtebalci", "Hakiki Bingöl balı, yarı fiyatına!"), ("kerem", "Bir kaşık deneyelim.")]),
    S("Kerem kaşık testini yapar: ip gibi akmıyor, sahte.", "A", ["kerem", "sahtebalci"],
      "Kerem pours honey from a spoon; it drips watery instead of flowing like a thread; he puts it down firmly.",
      [("kerem", "Dedem yazmış: İp gibi akmıyorsa alma. Bu bal değil, şeker şurubu."), ("sahtebalci", "Ne anlarsın sen!")]),
    S("Gerçek Bingöl balını arıcıdan alır.", "C", ["kerem", "aricı"],
      "The beekeeper pours thick honey from a comb; it flows like a golden thread; Kerem pays.",
      [("aricı", "İşte Bingöl balı. Kaşıktan ip gibi iner."), ("kerem", "Fark bu!")], k="a"),
    S("Sahte balcının önünde Necmi'nin arabası; gülümseyip gaza basar.", "A", ["kerem", "necmi"],
      "A car parked behind the fake honey stall; Necmi lowers the window, smiles at Kerem and drives away.",
      [("necmi", "Bu sefer yırttın pastırmacı.")], kam="medium shot, car pulling away"),
])

# ------------------------------------------------------------------ B38 ELAZIĞ
EP(38, {
    "elazigli": ("ELAZIĞLI ESNAF", "ELAZIĞ SHOPKEEPER, a 55-year-old Turkish woman, grey headscarf, burgundy coat", "female voice"),
    "orcikci": ("ORCİK USTASI", "ORCIK MAKER, a 50-year-old Turkish man, white apron, dipping strings of walnuts into grape molasses paste", "male voice"),
}, {
    "A": ("Elazığ çarşısı", "a market in Elazığ"),
    "B": ("Harput Kalesi", "the hilltop Harput Castle and old town above Elazığ, sunset"),
    "C": ("Hazar Gölü", "the blue Lake Hazar surrounded by mountains"),
    "D": ("Orcik atölyesi", "a workshop making orcik walnut sausages dipped in grape molasses paste, hanging to dry"),
    "E": ("Çay bahçesi, akşam", "a quiet tea garden by the lake at dusk"),
}, [
    S("Gerçek Bingöl balını satar.", "A", ["kerem", "elazigli"],
      "The shopkeeper tests the honey on a spoon, it flows like a thread; she pays.",
      [("elazigli", "İp gibi akıyor, bu hakiki."), ("kerem", "Testten geçti abla!")], k="s"),
    S("Harput Kalesi'nde Harput ezgileri.", "B", ["kerem"],
      "Kerem listens to an old musician playing a folk tune at the castle at sunset.",
      [("kerem", "Harput'un türküleri... Taşlar bile ezber biliyor.")]),
    S("Hazar Gölü'nde dinlenir.", "C", ["kerem"],
      "Kerem skips stones on the lake.",
      [("kerem", "Gölün altında batık bir şehir varmış. Her şeyin altında bir hikâye var.")]),
    S("Orcik yapımını görür.", "D", ["kerem", "orcikci"],
      "The maker dips a string of walnuts into thick grape paste; Kerem helps hang them.",
      [("orcikci", "Ceviz, pekmez, sabır."), ("kerem", "Elazığ'ın cevizli sucuğu!")]),
    S("Orcik alır.", "D", ["kerem", "orcikci"],
      "Kerem pays for bundles of orcik.",
      [("kerem", "Tunceli'ye tatlı bir hediye.")], k="a"),
    S("Necmi karşısına oturur: 'Defteri ver, yoksa annenin evi de gider.'", "E", ["kerem", "necmi"],
      "Necmi sits across Kerem at the tea table, stirring his tea slowly.",
      [("necmi", "Defteri ver, Selim Bey davayı çeksin. Yoksa annenin evi de gider.")], kam="tight two-shot, tension"),
])

# ------------------------------------------------------------------ B39 TUNCELİ
EP(39, {
    "tunceli_esnaf": ("TUNCELİLİ ESNAF", "TUNCELİ SHOPKEEPER, a 52-year-old Turkish man, salt-and-pepper beard, wool vest", "male voice"),
    "sarimsakci": ("SARIMSAK ÜRETİCİSİ", "GARLIC FARMER, a 58-year-old Turkish woman, flowered headscarf, holding a bunch of large single-clove mountain garlic", "female voice"),
}, {
    "A": ("Tunceli çarşısı", "a small market in Tunceli city"),
    "B": ("Munzur Gözeleri", "the Munzur springs, crystal clear water gushing from rocks into a green valley"),
    "C": ("Munzur Vadisi", "the deep green Munzur valley with a river and cliffs"),
}, [
    S("Necmi'yi reddettikten sonra orcikleri satar.", "A", ["kerem", "tunceli_esnaf"],
      "The shopkeeper tastes orcik and pays.",
      [("tunceli_esnaf", "Elazığ'ın orciği çayın yanına gider."), ("kerem", "Tehdit yedim ama satış yaptım.")], k="s"),
    S("Munzur Gözeleri'nin başında düşünür.", "B", ["kerem"],
      "Kerem sits by the springs watching water burst from rocks.",
      [("kerem", "Su taşın içinden çıkıyor. Gerçek de böyle çıkar herhalde.")]),
    S("Munzur Vadisi'nde yürür.", "C", ["kerem"],
      "Kerem walks through the green valley along the river.",
      [("kerem", "Munzur Vadisi milli park. Burada korunan sadece doğa değil, sessizlik.")], kam="wide tracking shot"),
    S("Endemik dağ sarımsağını tanır.", "C", ["kerem", "sarimsakci"],
      "The farmer shows a giant single-clove garlic.",
      [("sarimsakci", "Tunceli sarımsağı dağda kendiliğinden biter, tek dişlidir."), ("kerem", "Bu sarımsak değil, yumruk!")]),
    S("Tunceli dağ sarımsağı alır.", "C", ["kerem", "sarimsakci"],
      "Kerem pays for jars of pickled mountain garlic.",
      [("kerem", "Erzincan'a turşu götürüyorum.")], k="a"),
    S("Elif bir kayanın üstünde onu bekliyor: 'Gönderdiklerim sahte sayfalardı.'", "B", ["kerem", "elif"],
      "Kerem returns to the springs; Elif sits on a rock waiting, nervous.",
      [("elif", "Evet, Selim bana para verdi. Ama gönderdiklerim sahte sayfalardı.")], kam="slow push-in on Elif, Kerem frozen"),
])

# ------------------------------------------------------------------ B40 ERZİNCAN
EP(40, {
    "erzincanli": ("ERZİNCANLI ESNAF", "ERZİNCAN SHOPKEEPER, a 47-year-old Turkish man, grey coat, glasses", "male voice"),
    "tulumcu": ("TULUM PEYNİRCİSİ", "TULUM CHEESE MAKER, a 63-year-old Turkish man, white beard, white apron, cutting crumbly cheese from a goatskin", "elderly male voice"),
}, {
    "A": ("Erzincan çarşısı", "a market in Erzincan"),
    "B": ("Kemaliye Taş Yol ve Karanlık Kanyon", "the Stone Road of Kemaliye carved into a cliff above the deep Dark Canyon and the Euphrates"),
    "C": ("Girlevik Şelalesi", "the Girlevik waterfall cascading over mossy rocks"),
    "D": ("Tulum peyniri mahzeni", "a cheese cellar with tulum cheeses in goatskin sacks"),
}, [
    S("Elif'i dinler ve affeder; sarımsakları satar.", "A", ["kerem", "elif", "erzincanli"],
      "Kerem sells garlic to the shopkeeper while Elif films again, both smiling cautiously.",
      [("erzincanli", "Tunceli sarımsağı? Alıyorum!"), ("kerem", "Ekibimiz yeniden tam.")], k="s"),
    S("Kemaliye Taş Yol'dan Karanlık Kanyon'a bakar.", "B", ["kerem", "elif"],
      "Kerem and Elif walk along the narrow road carved into the cliff, the river far below.",
      [("elif", "Bu yolu köylüler elleriyle kazmış."), ("kerem", "Ben de yolumu elimle açacağım.")], kam="wide drone shot over the canyon"),
    S("Girlevik Şelalesi.", "C", ["kerem", "elif"],
      "They stand at the waterfall, Elif filming.",
      [("kerem", "Burayı belgesele koy, Erzincan herkesi şaşırtsın.")]),
    S("Tulum peynirinin yapılışını öğrenir.", "D", ["kerem", "tulumcu"],
      "The cheese maker cuts crumbly cheese from a goatskin.",
      [("tulumcu", "Erzincan tulumu deride olgunlaşır, ufalanır ama dağılmaz."), ("kerem", "Tıpkı iyi bir ekip gibi.")]),
    S("Erzincan tulum peyniri alır.", "D", ["kerem", "tulumcu"],
      "Kerem pays for tulum cheese.",
      [("kerem", "Erzurum'a tulum!")], k="a"),
    S("Selim'den mesaj: 'Asıl kozum başka: babam Cevdet Karahan yaşıyor.'", "A", ["kerem", "elif"],
      "Kerem reads a message on his phone, Elif reading over his shoulder.",
      [("kerem", "Babam Cevdet Karahan yaşıyor..."), ("elif", "Listedeki ilk isim!")],
      kam="close-up on two faces lit by the phone", kurgu="Mesaj: 'Sahte sayfalar için Elif'e teşekkür et. Asıl kozum başka: Babam Cevdet Karahan yaşıyor.'"),
])
