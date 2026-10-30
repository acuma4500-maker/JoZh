# -*- coding: utf-8 -*-
from ortak import EP, S

# ------------------------------------------------------------------ B4 KAYSERİ
EP(4, {}, {
    "A": ("Kayseri Kapalı Çarşı koridoru", "inside the historic Kayseri Covered Bazaar built in 1859, a long vaulted stone corridor, small shops with hanging copper pots, carpets and pastırma, warm afternoon light falling from skylights, busy shoppers"),
    "B": ("Hüseyin Usta'nın dükkânı", "Hüseyin Usta's tiny old shop inside the Kayseri Covered Bazaar, wooden shelves full of old ledgers, a brass scale, tulip-shaped tea glasses on a copper tray, a framed black-and-white photo of two young merchants on the wall"),
    "C": ("Çarşının taş kapısı, akşam", "the arched stone entrance gate of the Kayseri Covered Bazaar at dusk, street lamps turning on, snowy Mount Erciyes glowing in the distance"),
}, [
    S("Kerem defterdeki adresi okuyarak kalabalık çarşıda dükkân arar, kaybolmuş gibidir.", "A", ["kerem"],
      "Kerem walks through the crowded vaulted corridor holding the old leather notebook open, reading an address, looking up at the shop numbers, confused and a little lost.",
      [("kerem", "Dedem 'Kapalı Çarşı, kırk iki numara' yazmış... Burada yüz tane dükkân var!")]),
    S("Hüseyin Usta çay doldururken Kerem'in elindeki defteri görür ve donar.", "B", ["kerem", "husey"],
      "Hüseyin Usta is pouring tea; he sees the leather notebook in Kerem's hand, freezes, slowly takes off his reading glasses, his eyes fill with emotion.",
      [("husey", "O defter... Rıza'nın defteri. Sen Kerem'sin."), ("kerem", "Dedemi tanıyor muydunuz?")]),
    S("Usta ahiliğin üç kuralını parmaklarıyla sayar; Kerem alçak taburede şüpheyle dinler.", "B", ["kerem", "husey"],
      "Hüseyin Usta raises three fingers one by one while Kerem sits on a low wooden stool, listening with a skeptical half-smile.",
      [("husey", "Ahilik üç şeydir evlat: Eline, beline, diline sahip olacaksın."), ("kerem", "Yani çalma, kandırma, yalan söyleme?")]),
    S("Usta çekmeceden 5.000 ₺'lik zarfı çıkarır ama Kerem tutunca bırakmaz, şartlarını söyler.", "B", ["kerem", "husey"],
      "Hüseyin Usta takes an envelope of Turkish lira banknotes from a wooden drawer and holds it out; when Kerem grabs it, the old man does not let go, looking him straight in the eye.",
      [("husey", "Beş bin lira. Kasa sıfıra inmeyecek, yalan yok, her kuruş deftere yazılacak."), ("kerem", "Anlaştık usta!")]),
    S("Kerem deftere ilk satırı yazar; usta dua eder.", "B", ["kerem", "husey"],
      "Close-up of Kerem's hand writing the first line in the notebook with an old fountain pen, banknotes beside it; Hüseyin Usta smiles and puts a hand on Kerem's shoulder.",
      [("kerem", "Kasa: beş bin lira."), ("husey", "Bismillah. Bereketi bol olsun.")],
      kurgu="KASA göstergesi ilk kez animasyonla belirir: 5.000 ₺"),
    S("Kerem çarşıdan çıkarken gölgeden Selim Karahan çıkar ve 1 milyon teklif eder.", "C", ["kerem", "selim"],
      "As Kerem steps out of the bazaar gate at dusk, a tall man in a charcoal suit steps out of the shadow and blocks his way with a cold smile; Kerem instinctively grips his bag.",
      [("selim", "O defter için bir milyon lira veririm. Çünkü o mühür... aslında babamındı.")],
      kam="slow dramatic push-in on Selim's face, then cut to Kerem's shocked eyes"),
])

# ------------------------------------------------------------------ B5 KAYSERİ
EP(5, {
    "pastirmaci": ("PASTIRMACI USTA", "PASTIRMA MASTER, a 58-year-old Turkish man, broad shoulders, round red-cheeked face, short grey beard, white butcher coat, white cotton cap, sleeves rolled up", "male voice, loud cheerful baritone, Kayseri accent"),
    "bitpazari": ("BİT PAZARI SATICISI", "FLEA MARKET BUYER, a 30-year-old Turkish man, slim, short black hair, black hoodie, gold-rimmed glasses, holding a phone", "young male voice, casual Turkish"),
}, {
    "A": ("Kayseri Bit Pazarı", "an open-air flea market in Kayseri on a sunny morning, tables full of old radios, shoes and clothes, people bargaining"),
    "B": ("Pastırma imalathanesi", "a traditional Kayseri pastırma workshop, rows of cured beef hanging to dry in the wind, bowls of red çemen paste, wooden tables, Mount Erciyes visible through an open door"),
    "C": ("Hüseyin Usta'nın dükkânı", "Hüseyin Usta's tiny old shop inside the Kayseri Covered Bazaar, wooden shelves full of ledgers, brass scale, tea glasses"),
    "D": ("Kayseri otogarı, gece", "Kayseri intercity bus terminal at night, a white intercity bus with its engine running, passengers loading luggage"),
}, [
    S("Kerem, Selim'in teklifini düşünür ama defteri çantasına bastırıp reddeder; Bit Pazarı'na gider.", "A", ["kerem"],
      "Kerem walks into the flea market holding a pair of limited-edition sneakers from London, looking at them one last time with a bittersweet smile.",
      [("kerem", "Londra'dan kalan son hatıra... Hadi bakalım, sermayeye katkı!")]),
    S("Kerem son sneaker çiftini satar; alıcı ilk fiyatı düşük verir, Kerem kusurunu dürüstçe söyler.", "A", ["kerem", "bitpazari"],
      "Kerem shows the sneakers to a young buyer, then honestly points at a small scuff on the sole; the buyer is surprised by his honesty and hands him cash.",
      [("kerem", "Burada küçük bir çizik var, baştan söyleyeyim."), ("bitpazari", "Dürüst adamsın. İki bin beş yüz, tamam.")], k="s"),
    S("Hüseyin Usta onu pastırmacıya götürür; usta çemenin sırrını anlatır.", "B", ["kerem", "husey", "pastirmaci"],
      "The pastırma master spreads red çemen paste on a slab of cured beef while Hüseyin Usta and Kerem watch; wind moves the hanging meat.",
      [("pastirmaci", "Erciyes'in rüzgârı kurutur, çemen korur. Acele eden pastırma yapamaz."), ("kerem", "Yani işin sırrı sabır.")]),
    S("Usta öğüdü verir: 'Malın kusurunu önce sen söyle.'", "B", ["kerem", "husey"],
      "Hüseyin Usta opens Kerem's notebook to a page and taps it with his finger; Kerem reads, nodding slowly.",
      [("husey", "Deden ne yazmış? Malın kusurunu önce sen söyle, müşteri seni ömür boyu unutmaz.")]),
    S("Kerem 6.000 ₺'lik pastırma-sucuk alır; usta mühürlü sayfanın 81 ilden sonra açılacağını söyler.", "C", ["kerem", "husey"],
      "Kerem packs wrapped pastırma and sucuk into a cardboard box; Hüseyin Usta touches the red wax seal on the notebook's last page with his silver ring.",
      [("husey", "Bu mühür ancak 81 ili dolaşıp dönersen açılır."), ("kerem", "81 il mi?! Usta, bu bir sezon sürer!")], k="a"),
    S("Nevşehir otobüsünde iki koltuk arkada bir adam telefonda fısıldar.", "D", ["kerem", "necmi"],
      "Inside the bus at night Kerem sits by the window hugging the box; two rows behind him a wiry man with a toothpick whispers into his phone, watching him.",
      [("necmi", "Evet Selim Bey... yola çıktı.")], kam="slow dolly from Kerem past the seats to the whispering man in the back"),
])

# ------------------------------------------------------------------ B6 NEVŞEHİR
EP(6, {
    "otelci": ("OTEL SAHİBİ", "CAVE HOTEL OWNER, a 50-year-old Turkish woman, elegant, short grey hair, linen beige outfit, turquoise necklace", "female voice, calm and friendly"),
    "comlekci": ("AVANOS ÇÖMLEKÇİSİ", "AVANOS POTTER, a 65-year-old Turkish man, white beard, clay on his hands and forearms, brown work vest, flat cap", "elderly male voice, gentle and slow"),
}, {
    "A": ("Göreme, gün doğumu", "Göreme valley in Cappadocia at sunrise, fairy chimneys, dozens of colorful hot-air balloons rising in a pink sky"),
    "B": ("Mağara otel terası", "the terrace of a boutique cave hotel carved into rock in Göreme, kilim cushions, breakfast tables, balloons in the background"),
    "C": ("Avanos çömlek atölyesi", "a pottery workshop in Avanos by the Kızılırmak river, a kick wheel, red clay jugs drying on shelves"),
}, [
    S("Kerem gün doğumunda balonları izler; yanında fotoğraf çeken Elif'le tanışır.", "A", ["kerem", "elif"],
      "Kerem stands on a hill holding his box, amazed by the balloons; next to him a young woman photographs the sky, then turns her camera to him and clicks.",
      [("elif", "Pardon, kadrajın tam ortasındaydın. Ben Elif."), ("kerem", "Kerem. Pastırma satıyorum... balonlara değil tabii.")]),
    S("Kerem mağara otel sahibine pastırmayı tattırır ve satar.", "B", ["kerem", "otelci"],
      "Kerem slices pastırma on a wooden board for the hotel owner, who tastes it and nods, then counts banknotes into his hand.",
      [("otelci", "Kahvaltı tabağına tam gider. Hepsini alıyorum."), ("kerem", "Bereketli olsun!")], k="s"),
    S("Elif yolculuğunu merak eder, Kerem defteri gösterir.", "B", ["kerem", "elif"],
      "Elif sits across from Kerem with tea; he shows her the old notebook, she gently touches the red wax seal.",
      [("elif", "81 il mi? Bu bir belgesel olur!"), ("kerem", "Önce kasa batmasın, sonra belgesel.")]),
    S("Avanos'ta usta, Kızılırmak kiliyle Hititlerden beri süren çömlekçiliği anlatır.", "C", ["kerem", "comlekci"],
      "The old potter spins the kick wheel and shapes a red clay jug; Kerem tries and the clay collapses, the potter laughs.",
      [("comlekci", "Bu kil Kızılırmak'ın. Hititlerden beri böyle döner."), ("kerem", "Benimki çömlek değil, kek oldu!")]),
    S("Kerem çömlek alır; defterdeki öğüdü okur.", "C", ["kerem", "comlekci"],
      "Kerem carefully wraps several red clay jugs in newspaper and places them in his box, then reads a line from the notebook.",
      [("kerem", "Dedem yazmış: 'Elinle yapılanı ucuza alma, ustanın emeğine saygı.'")], k="a"),
    S("Elif fotoğrafı büyütür: arka planda dürbünle onları izleyen bir adam.", "A", ["kerem", "elif"],
      "Elif zooms into a photo on her camera screen and turns it toward Kerem; both lean in, worried, as balloons fly behind them.",
      [("elif", "Kerem... bu adamı tanıyor musun? Dürbünle seni izliyor.")],
      kam="extreme close-up of the camera screen, then rack focus to Kerem's face",
      kurgu="Kamera ekranında: arka planda dürbünlü Necmi'nin fotoğrafı (kurguda eklenebilir)"),
])

# ------------------------------------------------------------------ B7 NİĞDE
EP(7, {
    "elmaci": ("ELMA ÜRETİCİSİ", "APPLE FARMER, a 45-year-old Turkish woman, sun-tanned face, green headscarf, checked shirt, work gloves, holding a basket of red apples", "female voice, cheerful, Niğde accent"),
    "esnaf": ("NİĞDE ESNAFI", "NIĞDE SHOPKEEPER, a 55-year-old Turkish man, grey mustache, brown vest, flat cap", "male voice, friendly"),
}, {
    "A": ("Otobüs içi, gündüz", "inside a modern white intercity bus driving through the Central Anatolian steppe, sunlight through windows, the driver's seat visible"),
    "B": ("Niğde çarşısı", "a traditional market street in Niğde with stone buildings, the Alaaddin Mosque in the background"),
    "C": ("Gümüşler Manastırı", "the rock-cut Gümüşler Monastery near Niğde, carved stone halls with faded colorful frescoes"),
    "D": ("Elma bahçesi", "an apple orchard near Niğde with the Aladağlar mountains behind, wooden crates full of red apples"),
}, [
    S("Otobüs şoförü Yaşar Kaptan yolda Kerem'e Niğde'yi anlatır.", "A", ["kerem", "yasar"],
      "Kerem sits in the front seat behind the driver; the heavyset driver talks while driving, pointing at the mountains, Kerem laughs.",
      [("yasar", "Niğde'nin elması da gazozu da meşhurdur delikanlı."), ("kerem", "Kaptan, sen her yeri biliyor musun?")]),
    S("Kerem çömlekleri Niğde çarşısındaki esnafa satar.", "B", ["kerem", "esnaf"],
      "Kerem unwraps the red clay jugs on a shop counter; the shopkeeper inspects one, taps it, and nods approvingly.",
      [("esnaf", "Avanos işi bu, sesi bile başka. Alıyorum."), ("kerem", "Usta eli değdi abi.")], k="s"),
    S("Gümüşler Manastırı'nın kaya freskolarını gezer.", "C", ["kerem"],
      "Kerem walks slowly through the rock-cut monastery, shining his phone flashlight on ancient frescoes, whispering in awe.",
      [("kerem", "Bin yıl önce biri buraya renk taşımış... ve hâlâ duruyor.")]),
    S("Defterdeki öğüt: 'Elmayı dalından değil, bahçıvanın elinden al.'", "D", ["kerem"],
      "Kerem sits on an apple crate in the orchard reading the notebook, then looks up toward a farmer working among the trees.",
      [("kerem", "'Elmayı dalından değil, bahçıvanın elinden al.' Tamam dede, aracı yok.")]),
    S("Kerem elmayı doğrudan üreticiden alır.", "D", ["kerem", "elmaci"],
      "The farmer fills a crate with red apples; Kerem shakes her hand and pays her directly.",
      [("elmaci", "Toptancıya verdiğim fiyattan iyi verdin, Allah razı olsun."), ("kerem", "Emeğin hakkı bu abla.")], k="a"),
    S("Dönüş otobüsünde Yaşar defterin kapağındaki el yazısını görür ve frene basar.", "A", ["kerem", "yasar"],
      "The notebook slips from Kerem's bag onto the floor near the driver; Yaşar glances at the handwriting on the cover, his face turns pale and he hits the brakes, passengers jolt forward.",
      [("yasar", "Bu yazıyı tanıyorum... Bunu nereden buldun?")], kam="fast cut: the handwriting, Yaşar's eyes in the rear-view mirror, the bus braking"),
])

# ------------------------------------------------------------------ B8 AKSARAY
EP(8, {
    "dokumaci": ("TAŞPINAR DOKUMACISI", "CARPET WEAVER, a 60-year-old Turkish woman, kind wrinkled face, white headscarf, purple floral cardigan, sitting at a wooden loom", "elderly female voice, soft, Central Anatolian accent"),
    "pazarci": ("AKSARAY PAZARCISI", "MARKET VENDOR, a 40-year-old Turkish man, chubby, black mustache, blue apron", "male voice, loud market caller"),
}, {
    "A": ("Aksaray pazarı", "a busy open-air market in Aksaray, fruit stalls, vendors calling out, Mount Hasan in the background"),
    "B": ("Sultanhanı Kervansarayı", "the monumental 13th-century Seljuk Sultanhanı caravanserai, a huge carved stone portal, a wide courtyard with a small mosque kiosk in the middle"),
    "C": ("Taşpınar dokuma evi", "a village house in Taşpınar with wooden looms, colorful wool yarn, small handwoven carpets hanging on the walls"),
    "D": ("Kervansaray avlusu, gece", "the Sultanhanı caravanserai courtyard at night, moonlight on the carved stones, a sleeping bag on the floor"),
}, [
    S("Yaşar 'Eski bir yolcuydu' diyerek konuyu kapatır; Kerem Aksaray'da indirilir.", "A", ["kerem", "yasar"],
      "At the bus stop Yaşar hands Kerem his box of apples, avoiding his eyes; Kerem looks at him suspiciously.",
      [("yasar", "Eski bir yolcuydu, o kadar. Hadi, elmaların bayatlamasın."), ("kerem", "Kaptan, bir şey saklıyorsun.")]),
    S("Kerem elmaları pazarda satar.", "A", ["kerem", "pazarci"],
      "Kerem shouts like a market vendor next to a fruit stall, the vendor laughs and buys his whole crate.",
      [("kerem", "Niğde'nin elması, bahçıvanın elinden!"), ("pazarci", "Bu gençte ses var. Hepsini ver!")], k="s"),
    S("Defter onu Sultanhanı Kervansarayı'na yollar.", "B", ["kerem"],
      "Kerem stands tiny in front of the giant carved stone portal of the caravanserai, reading the notebook, then looking up in awe.",
      [("kerem", "'Kervan nerede konaklarsa tüccar orada öğrenir.' Dede, sen buralarda yatmışsın!")]),
    S("Kerem, kervansarayların İpek Yolu'ndaki rolünü hayal eder.", "B", ["kerem"],
      "Kerem walks in the courtyard and imagines a ghostly caravan of camels and merchants passing beside him, then the vision fades.",
      [("kerem", "Burada her gece yüzlerce tüccar... ve şimdi sadece ben.")], kam="wide shot with translucent ghost caravan overlay, slow pan"),
    S("Taşpınar'da dokumacı kadınlardan küçük halılar alır.", "C", ["kerem", "dokumaci"],
      "The old weaver shows Kerem a small handwoven carpet, tracing the pattern with her finger; Kerem pays and she folds the carpets for him.",
      [("dokumaci", "Her düğümde bir dua var oğlum."), ("kerem", "O zaman bu halılar çok bereketli.")], k="a"),
    S("Gece avluda uyanır: çantası açık, defterin mührü bıçakla kazınmış ama kırılamamış.", "D", ["kerem"],
      "Kerem wakes up in his sleeping bag, sees his bag open; he grabs the notebook and shines his phone on the red wax seal, which has deep knife scratches but is unbroken. A shadow disappears behind a column.",
      [("kerem", "Biri mührü açmaya çalışmış!")], kam="handheld, tense, flashlight beam"),
])

# ------------------------------------------------------------------ B9 KONYA (1)
EP(9, {
    "bedestenci": ("BEDESTEN TÜCCARI", "BAZAAR MERCHANT, a 62-year-old Turkish man, thin, white goatee, black vest over white shirt, prayer beads", "elderly male voice, slow bargainer"),
}, {
    "A": ("Konya Bedesteni", "the historic Konya Bedesten covered market, narrow lanes with carpet and textile shops"),
    "B": ("Mevlana Müzesi avlusu", "the courtyard of the Mevlana Museum in Konya with its iconic turquoise fluted dome, rose gardens, visitors"),
    "C": ("Müze kütüphanesi okuma odası", "a quiet manuscript reading room with old Ottoman books, green-shaded desk lamps"),
}, [
    S("Kerem halıları Bedesten'de satmaya çalışır ama kimse ilgilenmez.", "A", ["kerem"],
      "Kerem stands with his rolled carpets in a quiet market lane, shopkeepers ignore him; he checks his watch impatiently.",
      [("kerem", "Üç saattir bekliyorum, bir kişi bile sormadı...")]),
    S("Sabırsızlanıp fiyat kırar; tüccar halıları ucuza alır, az kâr eder.", "A", ["kerem", "bedestenci"],
      "The old merchant slowly counts prayer beads while Kerem lowers his price again and again; finally they shake hands, Kerem looks disappointed with the cash.",
      [("bedestenci", "Acele eden tüccar, malını değil kendini ucuza satar."), ("kerem", "Tamam... ders alındı.")], k="s"),
    S("Mevlana Müzesi'nin turkuaz kubbesinin altında Dr. Leyla ile tanışır.", "B", ["kerem", "leyla"],
      "Under the turquoise dome, Leyla notices the Ottoman script on Kerem's notebook and stops him, adjusting her glasses.",
      [("leyla", "Affedersiniz, o defterdeki yazı Osmanlıca. Okuyabilir miyim?"), ("kerem", "Siz okuyabiliyor musunuz?!")]),
    S("Leyla kenar notlarını okur: hepsi 1979 tarihli.", "C", ["kerem", "leyla"],
      "Leyla turns the notebook pages under a green desk lamp with a magnifying glass, Kerem leans over her shoulder.",
      [("leyla", "Kenar notlarının hepsi aynı yıl: 1979."), ("kerem", "Dedem o yıl ne yaptı ki?")]),
    S("Kerem deftere günün dersini yazar: 'Sabır, pazarlığın yarısıdır.'", "B", ["kerem"],
      "Kerem sits on a bench in the rose garden writing in the notebook, the turquoise dome behind him at golden hour.",
      [("kerem", "Bugünün dersi: Sabır, pazarlığın yarısıdır.")]),
    S("Leyla bir sayfada durur: 81 isimlik bir borç listesi.", "C", ["kerem", "leyla"],
      "Leyla stops at a page, her face changes; she slowly turns the notebook toward Kerem and points to a long handwritten list.",
      [("leyla", "Kerem... bu bir borç listesi. Tam 81 isim var.")], kam="slow push-in on the list, then on Kerem's face"),
])

# ------------------------------------------------------------------ B10 KONYA (2)
EP(10, {
    "firinci": ("ETLİ EKMEKÇİ", "ETLI EKMEK BAKER, a 50-year-old Turkish man, flour on his face, white apron, thick black mustache, wooden peel in hand", "male voice, hearty laugh"),
    "semazen": ("SEMAZEN", "WHIRLING DERVISH, a young man in a tall felt sikke hat and a flowing white tennure skirt, black cloak", "silent"),
}, {
    "A": ("Etli ekmek fırını", "a traditional Konya etli ekmek bakery with a wood-fired stone oven, long flat breads on wooden peels"),
    "B": ("Sema töreni salonu", "a Mevlevi sema ceremony hall in Konya, whirling dervishes in white, soft ney flute music, dim warm light"),
    "C": ("Mevlana şekeri dükkânı", "a small old candy shop selling white Mevlana sugar candies in glass jars"),
    "D": ("Konya sokağı, akşam", "an evening street in Konya, warm shop lights, a café table outside"),
}, [
    S("Kerem etli ekmek fırınında bir gün çalışır, yevmiye alır.", "A", ["kerem", "firinci"],
      "Kerem awkwardly slides a long etli ekmek into the stone oven with a wooden peel; the baker laughs and hands him a daily wage.",
      [("firinci", "Fırına korkmadan gireceksin!"), ("kerem", "Usta, kaşlarım yandı galiba!")], k="s"),
    S("Sema gösterisini izler.", "B", ["kerem", "semazen"],
      "Kerem watches a whirling dervish turning slowly, arms open, white skirt flowing; Kerem is mesmerized.",
      [("kerem", "Dönmek için önce durmayı bilmek gerekiyormuş...")], kam="slow motion circular camera around the dervish"),
    S("Deftere öğüdü yazar.", "D", ["kerem"],
      "Kerem sits at a street café writing in the notebook, steam rising from his tea.",
      [("kerem", "Dede'nin notu: 'Önce dur, sonra dön. Önce dinle, sonra sat.'")]),
    S("Mevlana şekeri alır.", "C", ["kerem"],
      "Kerem fills bags with white Mevlana sugar candies from glass jars and pays the shopkeeper.",
      [("kerem", "Karaman'a tatlı bir giriş yapalım.")], k="a"),
    S("Tatlı dilli bir adam yarı fiyatına Karaman peyniri teklif eder; Kerem reddeder.", "D", ["kerem", "necmi"],
      "A smiling wiry man sits uninvited at Kerem's table, offering a deal with exaggerated friendliness; Kerem shakes his head firmly.",
      [("necmi", "Karaman peyniri, yarı fiyatına! Kaçmaz bu fırsat."), ("kerem", "Faturası yoksa almam abi.")]),
    S("Adam giderken masaya bir kartvizit bırakır: Necmi — Karahan Lojistik.", "D", ["kerem", "necmi"],
      "The man stands, flicks a business card onto the table with a wink and walks away; Kerem picks it up and his expression darkens.",
      [("necmi", "Yolun açık olsun... şimdilik."), ("kerem", "Karahan... Selim'in adamı!")],
      kam="close-up on the business card on the table", kurgu="Kartvizit yazısı kurguda: 'Necmi — Karahan Lojistik'"),
])

# ------------------------------------------------------------------ B11 KARAMAN
EP(11, {
    "obrukcu": ("MAĞARA SAHİBİ", "CAVE CHEESE MAKER, an 80-year-old Turkish man, very wrinkled kind face, long white beard, black wool vest, cane", "elderly male voice, slow and emotional"),
    "karamanli": ("KARAMANLI ESNAF", "KARAMAN SHOPKEEPER, a 35-year-old Turkish woman, round glasses, brown headscarf, blue shop apron", "female voice, friendly"),
}, {
    "A": ("Karaman şehir meydanı", "the city center of Karaman with the Karamanoğlu Mehmet Bey statue and a stone inscription about the 1277 Turkish language decree"),
    "B": ("Yunus Emre Camii", "the small historic Yunus Emre Mosque and tomb in Karaman, quiet garden"),
    "C": ("Divle Obruk peynir mağarası", "a deep cool natural cave in Divle where wheels of cheese in goatskin sacks age on stone shelves, dim light"),
}, [
    S("Kerem 1277 fermanını okur.", "A", ["kerem"],
      "Kerem stands in front of the statue reading the inscription, then turns to the camera as if talking to his followers.",
      [("kerem", "1277'de burada bir ferman: 'Bugünden sonra Türkçe'den başka dil konuşulmayacak.' Türkçe'nin başkenti Karaman!")]),
    S("Mevlana şekerini esnafa satar.", "A", ["kerem", "karamanli"],
      "Kerem offers a white Mevlana candy to a shopkeeper; she tastes it, smiles and buys all the bags.",
      [("karamanli", "Konya'nın şekeri Karaman'da da tatlı."), ("kerem", "Komşuluk hakkı!")], k="s"),
    S("Yunus Emre Camii'nde dedesinin notunu okur.", "B", ["kerem"],
      "Kerem sits in the quiet garden of the Yunus Emre Mosque reading the notebook, wind moving the trees.",
      [("kerem", "'Yaratılanı severiz Yaratan'dan ötürü.' Dedem bunu her sayfaya yazmış.")]),
    S("Divle Obruk mağarasına iner; peynirin mağarada nasıl olgunlaştığını görür.", "C", ["kerem", "obrukcu"],
      "The old man leads Kerem down into the cool cave with a lantern, showing goatskin sacks of cheese aging on stone shelves.",
      [("obrukcu", "Bu peynir dört ay mağaranın nefesiyle olgunlaşır."), ("kerem", "Buzdolabı değil, doğa dolabı!")]),
    S("Divle peyniri alır.", "C", ["kerem", "obrukcu"],
      "Kerem pays and loads wrapped cheese into an insulated cooler box; the old man watches the notebook in his bag closely.",
      [("kerem", "Soğuk zincire dikkat edeceğim, söz.")], k="a"),
    S("Mağaranın yaşlı sahibi zarf uzatır: 'Ben ona borçluydum.'", "C", ["kerem", "obrukcu"],
      "The old man takes an old yellowed envelope from his vest and places it in Kerem's hands, his eyes wet.",
      [("obrukcu", "Hacı Rıza bana borçlu değildi evlat... ben ona borçluydum.")], kam="close-up on the envelope, then on the old man's teary eyes"),
])

# ------------------------------------------------------------------ B12 MERSİN
EP(12, {
    "lokantaci": ("TARSUS LOKANTACISI", "TARSUS RESTAURANT OWNER, a 48-year-old Turkish man, bald, thick black beard, white chef jacket", "male voice, warm, southern accent"),
    "cezeriyeci": ("CEZERİYE USTASI", "CEZERIYE MAKER, a 55-year-old Turkish woman, colorful headscarf, orange apron, stirring a copper pot", "female voice, cheerful"),
}, {
    "A": ("Otobüs bagajı, mola yeri", "a highway rest stop in the hot Mediterranean afternoon, an open bus luggage compartment, heat haze"),
    "B": ("Tarsus, Kleopatra Kapısı", "the ancient stone Cleopatra Gate in Tarsus, palm trees, small restaurants nearby"),
    "C": ("Kızkalesi sahili", "the beach of Kızkalesi with the medieval Maiden's Castle on an island in the turquoise sea, sunset"),
    "D": ("Cezeriye imalathanesi", "a small cezeriye sweet workshop in Mersin, copper pots of carrot paste, trays of cezeriye bars with coconut"),
}, [
    S("Mola yerinde Kerem soğutucuyu açar: peynirlerin bir kısmı bozulmuş. İlk zarar.", "A", ["kerem"],
      "Kerem opens his cooler box in the luggage compartment; he recoils from the smell, seeing some cheese spoiled and the cooler cable cut.",
      [("kerem", "Soğutucu kapalı?! Kablo... kesilmiş!")], kam="close-up on the cut cable, then Kerem's face"),
    S("Sağlam kalan peyniri Tarsus'taki lokantaya satar.", "B", ["kerem", "lokantaci"],
      "Near the Cleopatra Gate, Kerem honestly shows the restaurant owner which cheeses are good and which were spoiled; the owner buys the good ones.",
      [("kerem", "Şunlar bozuldu abi, onları satmam. Bunlar sağlam."), ("lokantaci", "Dürüstlüğün için sağlamları alıyorum.")], k="s"),
    S("Kızkalesi'ne bakarken defterdeki öğüdü okur.", "C", ["kerem"],
      "Kerem sits on the sand at sunset looking at the castle on the sea, reading the notebook, then writing his loss.",
      [("kerem", "'Zarar eden değil, zararından ders almayan batar.' Ders: Soğutucuyu gözünün önünden ayırma.")]),
    S("Kerem kasayı hesaplar, moral bozukluğunu atlatır.", "C", ["kerem"],
      "Kerem counts his remaining banknotes, sighs, then stands up, brushes off the sand and smiles determinedly.",
      [("kerem", "Kasa küçüldü ama bitmedi. Devam!")]),
    S("Cezeriye ustasından cezeriye alır.", "D", ["kerem", "cezeriyeci"],
      "The cezeriye maker cuts bars of orange carrot cezeriye coated in coconut and packs them for Kerem.",
      [("cezeriyeci", "Havuç, bal, ceviz... bu sıcakta bile bozulmaz."), ("kerem", "Tam bana göre!")], k="a"),
    S("Karaman'daki zarfı açar: yırtık bir fotoğrafın yarısı, 1979.", "C", ["kerem"],
      "At night by a lamp Kerem opens the yellowed envelope and pulls out half of a torn black-and-white photo: young Rıza in front of a 1970s truck; the other man's face is torn away.",
      [("kerem", "1979... Dedem. Peki yanındaki adam kim?")],
      kam="extreme close-up on the torn photograph", kurgu="Fotoğraf: Genç Rıza bir kamyonun önünde, yanındaki adamın yüzü yırtık"),
])

# ------------------------------------------------------------------ B13 ADANA (1)
EP(13, {
    "tatlici": ("ADANALI TATLICI", "SWEET SHOP OWNER, a 60-year-old Turkish man, white hair, thin mustache, white shirt with suspenders", "male voice, Adana accent"),
    "kebapci": ("KEBAP USTASI", "KEBAB MASTER, a 52-year-old Turkish man, big build, black beard, red scarf on head, holding a large curved zırh knife", "male voice, deep and proud"),
}, {
    "A": ("Taşköprü", "the ancient Roman stone bridge Taşköprü over the Seyhan river in Adana, the Sabancı Central Mosque with six minarets behind"),
    "B": ("Tatlıcı dükkânı", "a traditional sweet shop near the Taşköprü in Adana, glass display with desserts"),
    "C": ("Kebapçı ocakbaşı", "an Adana kebab grill restaurant, charcoal fire, skewers of minced meat, a wooden chopping board"),
    "D": ("Otel lobisi, gece", "a modest hotel lobby in Adana at night, dim light, an old leather armchair"),
}, [
    S("Kerem Taşköprü'yü geçerken izleyiciye köprünün hikâyesini anlatır.", "A", ["kerem"],
      "Kerem walks across the ancient bridge with his box, gesturing at the stones as if vlogging.",
      [("kerem", "Bu köprü Romalılardan kalma ve hâlâ kullanılıyor. İki bin yıllık müşteri sadakati!")]),
    S("Cezeriyeleri tatlıcıya satar.", "B", ["kerem", "tatlici"],
      "The sweet shop owner tastes a cezeriye bar, closes his eyes in pleasure and pays Kerem.",
      [("tatlici", "Mersin'in cezeriyesi, Adana'nın vitrininde. Hepsini koy."), ("kerem", "Komşu tadı!")], k="s"),
    S("Kebap ustası zırhla kıyma çekerken 'iş elle yapılır' dersini verir.", "C", ["kerem", "kebapci"],
      "The kebab master rhythmically chops meat with a big curved zırh knife, then hands Kerem a skewer to try.",
      [("kebapci", "Makineyle çekilen kıyma kebap olmaz. İş de elle yapılır."), ("kerem", "Anladım usta, kısa yol yok.")]),
    S("Kerem kebabını yerken defterine not alır.", "C", ["kerem"],
      "Kerem eats an Adana kebab wrapped in lavash with şalgam juice, writing notes with his free hand.",
      [("kerem", "Not: Bugün alım yok. Sabır. Yarın Adana'nın ürününü bulacağım.")]),
    S("Otele döner; lobide biri onu beklemektedir.", "D", ["kerem"],
      "Kerem enters the dim hotel lobby yawning, then stops: someone sits in the armchair with his back turned, gloved fingers tapping.",
      [("kerem", "Kim var orada?")], kam="slow approach from behind the armchair"),
    S("Selim Karahan: 'Bir ay içinde o defter benim olacak.'", "D", ["kerem", "selim"],
      "Selim turns in the armchair, stands up slowly, buttons his suit jacket and walks past Kerem, stopping close to his ear.",
      [("selim", "Bir ay içinde o defter benim olacak. İster kolay yoldan, ister zor yoldan.")], kam="tight two-shot, low angle on Selim"),
])

# ------------------------------------------------------------------ B14 ADANA (2)
EP(14, {
    "salgamci": ("ŞALGAMCI", "ŞALGAM SELLER, a 45-year-old Turkish man, red cap, purple-stained apron, big friendly smile", "male voice, energetic"),
    "kozanli": ("KOZANLI ÜRETİCİ", "ORANGE FARMER, a 50-year-old Turkish man, sun-tanned, straw hat, green work shirt", "male voice, calm"),
}, {
    "A": ("Lezzet festivali tezgâhı", "a busy food festival in Adana, colorful stalls, crowds, string lights, a purple şalgam juice stand"),
    "B": ("Kozan portakal bahçesi", "an orange orchard in Kozan with the medieval Kozan castle on a hill behind, orange trees heavy with fruit"),
    "C": ("Festival alanı, akşam", "the Adana food festival area at sunset, people dancing, lights turning on"),
}, [
    S("Kerem lezzet festivalinde şalgam tezgâhında çalışır.", "A", ["kerem", "salgamci"],
      "Kerem pours purple şalgam juice into cups as fast as he can for a long queue, the seller cheering him on.",
      [("salgamci", "Acılı mı acısız mı, sor!"), ("kerem", "Acılı mı acısız mı abla? Acılı! Tamam!")]),
    S("Akşam yevmiyesini alır.", "C", ["kerem", "salgamci"],
      "The seller counts out Kerem's daily wage and gives him an extra cup of şalgam with a pat on the back.",
      [("salgamci", "İyi çalıştın, al bu da ikramım."), ("kerem", "Dilim mor oldu ama kasam güldü!")], k="s"),
    S("Elif festivalde yeniden belirir; '81 İl' belgeseli çektiğini söyler.", "C", ["kerem", "elif"],
      "Elif appears among the festival crowd, filming; she spots Kerem and laughs, walking toward him.",
      [("elif", "Pastırmacı! Ben de 81 il belgeseli çekiyorum. Seni çekebilir miyim?"), ("kerem", "Kasam kameraya çıkacak kadar dolu değil ama olur.")]),
    S("Kozan'a gider; portakal bahçesi ve Kozan kalesi.", "B", ["kerem", "elif"],
      "Kerem and Elif walk through the orange orchard; Elif films the castle on the hill, Kerem picks an orange and smells it.",
      [("kerem", "Bu kokuyu kutulayıp satabilsem zengin olurdum.")]),
    S("Kozan portakalını üreticiden alır.", "B", ["kerem", "kozanli"],
      "The farmer fills crates with oranges; Kerem pays and shakes his hand while Elif films.",
      [("kozanli", "Kozan portakalının suyu bol, kabuğu ince."), ("kerem", "Osmaniye'de görüşürüz portakallar!")], k="a"),
    S("Elif'in telefonuna 'S.K.' imzalı mesaj gelir; ekranı hızla kapatır.", "C", ["kerem", "elif"],
      "Elif's phone buzzes; she glances at it, her smile disappears and she quickly locks the screen and hides it; Kerem notices.",
      [("kerem", "Kötü bir haber mi?"), ("elif", "Yok... önemli değil.")],
      kam="close-up on Elif's eyes, then the phone screen going dark", kurgu="Telefon ekranında kısa bir an: 'S.K.: Takipte kal.'"),
])

# ------------------------------------------------------------------ B15 OSMANİYE
EP(15, {
    "halci": ("OSMANİYE HALCİSİ", "WHOLESALE MARKET TRADER, a 47-year-old Turkish man, stocky, grey t-shirt, cap, calculator in hand", "male voice, quick talker"),
    "fistikci": ("YER FISTIĞI ÜRETİCİSİ", "PEANUT FARMER, a 58-year-old Turkish woman, sun-tanned face, red headscarf, floral shalwar trousers, holding peanut plants", "female voice, warm"),
}, {
    "A": ("Osmaniye hali", "a wholesale produce market in Osmaniye, trucks, crates of fruit, workers"),
    "B": ("Karatepe-Aslantaş Açık Hava Müzesi", "the Karatepe-Aslantaş open-air museum in a pine forest, ancient Neo-Hittite stone lion sculptures and carved reliefs with bilingual inscriptions"),
    "C": ("Yer fıstığı tarlası", "a peanut field in Osmaniye, freshly harvested peanut plants drying in rows"),
}, [
    S("Kerem portakalları halde satar.", "A", ["kerem", "halci"],
      "Kerem negotiates with the trader over crates of oranges; the trader punches numbers on his calculator and shows him.",
      [("halci", "Kozan'ın portakalı mı? Bu fiyata alırım."), ("kerem", "Kokla abi, sonra fiyatı yükselt!")], k="s"),
    S("Elif ile Karatepe-Aslantaş'taki aslan heykellerini gezer.", "B", ["kerem", "elif"],
      "Kerem and Elif walk among ancient stone lion statues in the pine forest; Elif photographs the carved reliefs.",
      [("elif", "Bu yazıt iki dilde yazılmış. Hitit hiyeroglifi ve Fenike dili."), ("kerem", "Yani bir çeşit sözlük!")]),
    S("Kerem defterdeki iki ayrı yazı stilini fark eder ve Leyla'yı arar.", "B", ["kerem", "~leyla"],
      "Kerem compares a page of the notebook with the bilingual inscription and calls on his phone, excited.",
      [("kerem", "Leyla Hanım, defterde de iki farklı yazı var gibi!"), ("leyla", "Fotoğrafını hemen gönder!")]),
    S("Yer fıstığı tarlasında hasadı izler.", "C", ["kerem", "fistikci"],
      "The farmer pulls a peanut plant from the soil and shows the peanuts hanging from the roots; Kerem is surprised.",
      [("fistikci", "Fıstık toprağın altında yetişir oğlum."), ("kerem", "Ben ağaçta biter sanıyordum!")]),
    S("Osmaniye yer fıstığı alır.", "C", ["kerem", "fistikci"],
      "Kerem fills sacks with roasted peanuts and pays the farmer, Elif filming them laughing.",
      [("kerem", "Osmaniye fıstığı, Hatay yolcusu!")], k="a"),
    S("Leyla geri arar: sayfaların altında ikinci bir metin var, ilk kelime KARAHAN.", "A", ["kerem", "elif", "~leyla"],
      "At dusk Kerem answers the phone on speaker; Elif leans in to listen; both freeze at the news.",
      [("leyla", "Karatepe'deki gibi... sayfaların altında ikinci bir metin var. Ve ilk kelime bir soyadı: Karahan.")],
      kam="slow push-in on Kerem's shocked face, Elif's eyes shifting nervously"),
])

# ------------------------------------------------------------------ B16 HATAY (1)
EP(16, {
    "kuruyemisci": ("ANTAKYALI KURUYEMİŞÇİ", "NUT SHOP OWNER, a 57-year-old Turkish man, white shirt, grey vest, kind tired face, short grey beard", "male voice, warm, Antakya accent"),
    "firinci2": ("FIRINCI ABLA", "BAKER WOMAN, a 42-year-old Turkish woman, long black hair in a bun, white apron, flour on her hands", "female voice, emotional"),
}, {
    "A": ("Antakya, Uzun Çarşı", "the rebuilt Uzun Çarşı market street in Antakya after the earthquake, new and restored stone shops reopening, scaffolding, hopeful atmosphere"),
    "B": ("Yeniden açılan fırın", "a small bakery being reopened in Antakya, fresh paint, a ribbon at the door, neighbors gathering"),
    "C": ("Habib-i Neccar Camii", "the restored Habib-i Neccar Mosque in Antakya, stone courtyard, a marble donor plaque on the wall"),
}, [
    S("Kerem yeniden inşa edilen Uzun Çarşı'ya girer; şehrin ayağa kalkışını görür.", "A", ["kerem", "elif"],
      "Kerem and Elif walk through the rebuilt market street among scaffolding and newly opened shops; shopkeepers raise their shutters.",
      [("elif", "Depremden sonra her dükkân tek tek yeniden açılıyor."), ("kerem", "Bu şehir pes etmeyi bilmiyor.")]),
    S("Yer fıstığını kuruyemişçiye satar.", "A", ["kerem", "kuruyemisci"],
      "Kerem pours peanuts onto the scale in the nut shop; the owner smiles and pays him.",
      [("kuruyemisci", "Yeni açıldık, ilk malımız senden olsun."), ("kerem", "İlk satışınız bereketli olsun abi.")], k="s"),
    S("Fırının yeniden açılışına katkıda bulunur.", "B", ["kerem", "firinci2"],
      "Kerem quietly places some banknotes in a box at the bakery's reopening; the baker woman hugs him with tears.",
      [("firinci2", "Hiç tanımadığın birine neden yardım ediyorsun?"), ("kerem", "Dedem öyle yazmış: Bereket paylaşınca gelir.")]),
    S("Antakya künefesi yerler, sofrada dayanışma konuşulur.", "B", ["kerem", "elif", "firinci2"],
      "The three share a hot künefe at a small table outside the bakery, laughing as the cheese stretches.",
      [("elif", "Bu peynir nasıl uzuyor böyle?"), ("firinci2", "Hatay'ın sabrı gibi, kopmaz.")]),
    S("Kerem Habib-i Neccar Camii'ni ziyaret eder.", "C", ["kerem"],
      "Kerem walks into the restored mosque courtyard and reads a marble plaque of donors on the wall.",
      [("kerem", "Restorasyona katkı verenler listesi...")]),
    S("Bağışçı listesinde bir isim: 'Hacı Rıza Aksoy — 1981.'", "C", ["kerem"],
      "Kerem's finger stops on one name on the marble plaque; his eyes widen.",
      [("kerem", "Hacı Rıza Aksoy... 1981. Dede, sen her yerdesin.")],
      kam="extreme close-up on the engraved name, then Kerem's face", kurgu="Mermer levhada: 'Hacı Rıza Aksoy — 1981'"),
])

# ------------------------------------------------------------------ B17 HATAY (2)
EP(17, {
    "kunefeci": ("KÜNEFE USTASI", "KÜNEFE MASTER, a 63-year-old Turkish man, white chef hat, grey mustache, round copper tray in hand", "male voice, Antakya accent, jokey"),
    "sabuncu": ("DEFNE SABUNCUSU", "LAUREL SOAP MAKER, a 50-year-old Turkish woman, green headscarf, rubber apron, rolled sleeves", "female voice, calm"),
}, {
    "A": ("Hatay Arkeoloji Müzesi", "the Hatay Archaeology Museum, huge Roman floor mosaics under glass, soft lighting"),
    "B": ("Künefe dükkânı", "a künefe shop with round copper trays over a charcoal fire, golden shredded kadayıf"),
    "C": ("Harbiye defne sabunu atölyesi", "a laurel soap workshop in Harbiye, green soap bars stacked in towers to dry, waterfalls nearby"),
    "D": ("Pansiyon odası, gece", "a small guesthouse room in Antakya at night, a bed, a window with city lights"),
}, [
    S("Hatay Arkeoloji Müzesi'nde mozaikleri gezer.", "A", ["kerem", "elif"],
      "Kerem and Elif walk over glass floors above giant Roman mosaics; Elif photographs a mosaic face.",
      [("elif", "Bunlar dünyanın en büyük mozaik koleksiyonlarından."), ("kerem", "Binlerce taş, tek bir resim.")]),
    S("Künefe ustasının yanında yarım gün çalışır.", "B", ["kerem", "kunefeci"],
      "Kerem tries to flip a künefe tray like the master and nearly drops it; the master catches it and laughs.",
      [("kunefeci", "Bilek değil, gönül çevirir!"), ("kerem", "Gönlüm çevirdi ama bileğim yetişmedi.")]),
    S("Yevmiyesini alır.", "B", ["kerem", "kunefeci"],
      "The master gives Kerem his half-day wage and a small plate of künefe.",
      [("kunefeci", "Al evlat, emeğinin karşılığı."), ("kerem", "Sağ olun usta!")], k="s"),
    S("Harbiye'de defne sabununun yapılışını öğrenir.", "C", ["kerem", "sabuncu"],
      "The soap maker shows towers of green laurel soap drying; she breaks a bar to show the green inside.",
      [("sabuncu", "Zeytinyağı ve defne yağı. Bir yıl kurur, öyle satılır."), ("kerem", "Bir yıl mı? Sabrın kokusu bu!")]),
    S("Defne sabunu alır.", "C", ["kerem", "sabuncu"],
      "Kerem packs laurel soap bars into his box and pays.",
      [("kerem", "Kilis'e defne kokusu götürüyorum.")], k="a"),
    S("Gece numarası gizli mesaj gelir: 'Kilis'e gitme.'", "D", ["kerem"],
      "Kerem lies on the bed; his phone lights up in the dark, he reads it and sits up abruptly, looking out the window.",
      [("kerem", "Kilis'e gitme... seni bekliyorlar? Kim bu?")],
      kam="phone light on Kerem's face in darkness", kurgu="Telefon mesajı: 'Kilis'e gitme. Seni bekliyorlar.' (Gizli numara)"),
])

# ------------------------------------------------------------------ B18 KİLİS
EP(18, {
    "zeytinci": ("ZEYTİNYAĞI ÜRETİCİSİ", "OLIVE OIL PRODUCER, a 66-year-old Turkish man, white mustache, brown wool vest, flat cap, kind eyes", "elderly male voice, wise"),
    "aktar": ("KİLİSLİ AKTAR", "SPICE SHOP OWNER, a 40-year-old Turkish woman, black headscarf, maroon cardigan", "female voice, friendly"),
}, {
    "A": ("Kilis Mevlevihanesi", "the historic Kilis Mevlevi lodge with a stone courtyard and a domed building"),
    "B": ("Kilis çarşısı aktar dükkânı", "a traditional spice and soap shop in Kilis bazaar"),
    "C": ("Zeytinlik ve yağhane", "an olive grove and a traditional olive oil press in Kilis, golden oil flowing"),
    "D": ("Kilis otogarı", "a small bus terminal in Kilis in the evening"),
}, [
    S("Uyarıya rağmen Kilis'e gelir; tedirgin şekilde etrafa bakar.", "A", ["kerem"],
      "Kerem walks into the Mevlevi lodge courtyard carefully, checking over his shoulder.",
      [("kerem", "Kimse yok gibi... ama mesaj boşuna gelmedi.")]),
    S("Defne sabunlarını aktara satar.", "B", ["kerem", "aktar"],
      "The spice shop owner smells a laurel soap bar and nods, putting them on her shelf and paying Kerem.",
      [("aktar", "Harbiye sabunu! Müşterim hemen tanır."), ("kerem", "Bir yıl kurumuş, ona göre fiyat abla!")], k="s"),
    S("Zeytinyağı üreticisi ona 'yağ suyun üstüne çıkar' der.", "C", ["kerem", "zeytinci"],
      "In the olive press, golden oil flows; the old producer pours oil into a glass of water, the oil rises to the top.",
      [("zeytinci", "Yağ suyun üstüne çıkar, doğru da öyle."), ("kerem", "Yalan ne kadar saklanırsa saklansın...")]),
    S("Deftere öğüdü yazar.", "C", ["kerem"],
      "Kerem sits under an olive tree writing in the notebook.",
      [("kerem", "Kilis'in dersi: Doğru, er geç yüzeye çıkar.")]),
    S("Kilis zeytinyağı alır.", "C", ["kerem", "zeytinci"],
      "Kerem fills tin cans with olive oil and pays the producer.",
      [("zeytinci", "Gaziantep'te iyi fiyat bulursun."), ("kerem", "İnşallah usta.")], k="a"),
    S("Mesajı atan çıkar: Yaşar Kaptan. Gaziantep'te boykot var.", "D", ["kerem", "yasar"],
      "At the terminal, a familiar heavyset bus driver steps off a bus and approaches Kerem, serious.",
      [("yasar", "Mesajı ben attım. Gaziantep'teki toptancıların hepsine Karahan'dan telefon geldi. Kimse senden mal almayacak.")],
      kam="medium two-shot, bus headlights behind Yaşar"),
])

# ------------------------------------------------------------------ B19 GAZİANTEP (1)
EP(19, {
    "toptanci": ("GAZİANTEPLİ TOPTANCI", "WHOLESALER, a 50-year-old Turkish man, heavy build, gold watch, white shirt, avoids eye contact", "male voice, uncomfortable"),
}, {
    "A": ("Toptancılar çarşısı", "a wholesalers' street in Gaziantep with stone hans and shops"),
    "B": ("Kadın kooperatifi", "a women's cooperative workshop in Gaziantep, women making baklava and packing products, colorful kilims, a framed old torn photo on the wall"),
    "C": ("Zeugma Mozaik Müzesi", "the Zeugma Mosaic Museum, the famous 'Gypsy Girl' mosaic in a dark room with spotlight"),
}, [
    S("Toptancılar Kerem'e kapıyı kapatır.", "A", ["kerem", "toptanci"],
      "A wholesaler pulls down his shop shutter halfway when he sees Kerem coming with oil cans, avoiding his eyes.",
      [("toptanci", "Kusura bakma kardeşim... alamam."), ("kerem", "Malı görmeden mi? Kim söyledi bunu size?")]),
    S("Yaşar onu Nazlı Abla'nın kooperatifine götürür.", "B", ["kerem", "yasar", "nazli"],
      "Yaşar brings Kerem into the cooperative; a strong cheerful woman wipes flour from her hands and greets them.",
      [("nazli", "Yaşar Abi'nin getirdiği adam bizim adamımızdır. Ne getirdin bakalım?"), ("kerem", "Kilis zeytinyağı, Nazlı Abla.")]),
    S("Kooperatif zeytinyağını adil fiyata alır.", "B", ["kerem", "nazli"],
      "Nazlı tastes the oil on a piece of bread, nods and counts banknotes into Kerem's hand while women watch smiling.",
      [("nazli", "Karahan'ın sözü bizim kapıdan içeri girmez. Hepsini alıyoruz."), ("kerem", "Abla, hayatımı kurtardın.")], k="s"),
    S("Zeugma'da 'Çingene Kızı' mozaiğinin önünde öğüdü okur.", "C", ["kerem"],
      "Kerem stands alone in the dark room facing the famous mosaic's haunting eyes, reading the notebook.",
      [("kerem", "'Her mozaik tek tek taşlardan olur.' Ben de il il, taş taş...")], kam="slow push-in from the mosaic's eyes to Kerem"),
    S("Kerem kooperatif kadınlarına teşekkür eder; Nazlı defteri merak eder.", "B", ["kerem", "nazli"],
      "Kerem shows Nazlı the half photo from his notebook while women pack baklava in the background.",
      [("kerem", "Bu fotoğrafı Karaman'da buldum. Dedem bu."), ("nazli", "Bir dakika... bir dakika...")]),
    S("Nazlı duvardaki çerçeveyi gösterir: fotoğrafın öbür yarısı.", "B", ["kerem", "nazli"],
      "Nazlı slowly turns to a framed old torn photo on the wall; Kerem looks from his half to the frame, stunned.",
      [("nazli", "Bu fotoğrafın öbür yarısı... bizim kooperatifin duvarında asılı.")], kam="pan from Kerem's photo half to the framed half on the wall"),
])

# ------------------------------------------------------------------ B20 GAZİANTEP (2)
EP(20, {
    "fistik_ureticisi": ("ANTEP FISTIĞI ÜRETİCİSİ", "PISTACHIO FARMER, a 55-year-old Turkish man, white beard, beige jacket, prayer cap", "male voice, slow, Gaziantep accent"),
    "bakirci": ("BAKIRCI USTA", "COPPERSMITH, a 70-year-old Turkish man, thin, leather apron, hammer in hand, small round glasses", "elderly male voice"),
}, {
    "A": ("Kooperatif", "a women's cooperative workshop in Gaziantep, baklava trays, a framed torn photo on the wall"),
    "B": ("Bakırcılar Çarşısı", "the Coppersmiths' Bazaar in Gaziantep, artisans hammering copper trays, shining pots hanging everywhere"),
    "C": ("Antep fıstığı bahçesi", "a pistachio orchard near Gaziantep, clusters of red-pink pistachios on trees"),
}, [
    S("İki yarım fotoğrafı birleştirirler: dedenin yanındaki adamın yüzü güneşten yanmış.", "A", ["kerem", "nazli"],
      "Kerem holds his half photo next to the framed half; together they show two young men in front of a truck, but the second man's face is burned and faded.",
      [("kerem", "Yüzü yanmış... görünmüyor!"), ("nazli", "Babam bu fotoğrafı dedenden almış. Kim olduğunu hiç söylemedi.")]),
    S("Kooperatifin baklava atölyesinde çalışır.", "A", ["kerem", "nazli"],
      "Kerem rolls thin phyllo dough with a long rolling pin, it tears; the women laugh and Nazlı shows him how.",
      [("nazli", "Yufka sabır ister, yırtılırsa baştan!"), ("kerem", "Baklava benden zor çıktı.")]),
    S("Günün yevmiyesini alır.", "A", ["kerem", "nazli"],
      "Nazlı hands Kerem his daily wage and a small box of baklava.",
      [("nazli", "Al bakalım çırak, hak ettin."), ("kerem", "Teşekkürler abla.")], k="s"),
    S("Bakırcılar Çarşısı'nda dövülen bakırın sesi.", "B", ["kerem", "bakirci"],
      "The old coppersmith hammers a copper tray rhythmically; Kerem tries one strike and makes a dent.",
      [("bakirci", "Her vuruş bir karar. Yanlış vurursan geri dönüş yok."), ("kerem", "Ticaret gibi.")]),
    S("Antep fıstığı alır.", "C", ["kerem", "fistik_ureticisi"],
      "The farmer shows red-pink pistachio clusters on the tree; Kerem buys sacks of pistachios.",
      [("fistik_ureticisi", "Nazlı'nın selamıyla gelene en iyisini veririm."), ("kerem", "Maraş'ta dondurmaya karışacak bunlar!")], k="a"),
    S("Leyla arar: listenin birinci sırasında Cevdet Karahan yazıyor.", "C", ["kerem", "~leyla"],
      "Kerem answers his phone among the pistachio trees at sunset; his smile fades.",
      [("leyla", "81 isimlik listenin birinci sırasında ne yazıyor biliyor musun? Cevdet Karahan.")], kam="slow push-in on Kerem's face, the sun setting behind"),
])
