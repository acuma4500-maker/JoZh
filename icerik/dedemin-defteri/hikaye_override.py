# -*- coding: utf-8 -*-
"""Sahnelerle uyuşan bölüm özetleri. sezon1.py içindeki ilk taslak metinlerin yerine geçer.
Alanlar: hikaye, son, baslik, satilan, alinan (sadece değişenler)."""

OVERRIDE = {
    4: dict(hikaye="Cenazeden bir gün sonra Kerem, defterin ilk sayfasındaki adresi bulur: Kapalı Çarşı, 42 numara. Dedesinin can dostu Hüseyin Usta "
                   "ona ahiliğin üç kuralını öğretir ve 5.000 ₺ sermaye verir; şartı, kasanın sıfıra düşmemesi, yalan söylenmemesi ve her kuruşun "
                   "deftere yazılmasıdır. Kasa dizide ilk kez bu bölümde belirir."),
    5: dict(hikaye="Hüseyin Usta sermayenin küçük olduğunu söyler ve Kerem'den son sneaker çiftini satmasını ister: malın kusurunu önce kendin söyle. "
                   "Kerem çifti Bit Pazarı'nda satar; Hüseyin'in tanıdığı imalathanede çemenin ve Erciyes rüzgârının sırrını öğrenip pastırma ile sucuk alır. "
                   "Usta, mührün yolun sonunda, seksen bir ilin ardından açılacağını söyler."),
    6: dict(hikaye="Şafakta Göreme'de balonları izlerken belgeselci Elif Sarı ile tanışır; pastırmayı mağara otele satar, öğle yemeğinde testi kebabı yer. "
                   "Avanos'ta Kızılırmak kilinden çömlek yapan ustadan çömlek alırken defterin altıncı sayfasını okur. "
                   "Gün batımında Elif'in fotoğrafında kendisini dürbünle izleyen birini görür."),
    7: dict(hikaye="Yaşar Kaptan'ın otobüsüyle Niğde'ye gelir, çömlekleri çarşıda satar, Niğde tavası yer. Gümüşler Manastırı'nda defterin yedinci "
                   "sayfasını okur ve elmayı aracısız, bahçıvan Ayten'in soğuk deposundan alır. Akşam otobüste defterin kapağını gören Yaşar frene basar."),
    8: dict(hikaye="Aksaray'da Yaşar yazıyı 'eski bir yolcu'ya bağlayıp konuyu kapatır. Kerem elmaları pazarda satar, Sultanhanı Kervansarayı'nda "
                   "defterin sekizinci sayfasını okur ve Taşpınar'da bir dokumacıdan küçük halılar alır. Gece pansiyonda defterin mührü bıçakla kazınmıştır.",
           son="Gece Sultanhanı'ndaki pansiyonda uyandığında çantası açık, defterin mührü bir bıçakla kazınmış ama kırılamamış."),
    9: dict(hikaye="Konya'da acele edip halıları Bedesten'de ucuza satar: sabır pazarlığın yarısıdır. Öğle yemeğinde defterdeki yazıyı fark eden Dr. Leyla, "
                   "Mevlana Müzesi'nde kenar notlarını okur: hepsi 1979. Akşam bir kütüphanede defterin ortasında seksen bir isimlik bir liste bulurlar."),
    10: dict(baslik="Dönmeden Önce Dur (2)",
             hikaye="Defterin kuralı gereği çalışma günü: Kerem etli ekmek fırınında yevmiye karşılığı çalışır, Mevlana şekeri alır ve akşam sema ayinini izler. "
                    "Gece sokak kafesinde tatlı dilli bir adam ona yarı fiyatına peynir satmak ister; Kerem faturasını sorunca adam kartvizit bırakır."),
    11: dict(hikaye="Karaman'da dünkü kartviti yırtar, Mevlana şekerini satar, Türkçe'nin 1277'de devlet dili olduğunu öğrenir ve Yunus Emre'nin türbesinde "
                    "defterin on birinci sayfasını okur. Divle'deki mağaradan Obruk peyniri alırken yaşlı sahibi ona bir zarf verir."),
    12: dict(hikaye="Mersin'e inince soğutucunun kablosunun kesildiğini ve peynirin bir kısmının bozulduğunu görür: ilk zarar. Tarsus'ta sağlam kalanı "
                    "dürüstçe satar, Kleopatra Kapısı'nda defterin on ikinci sayfasını okur ve cezeriye alır. Gece Karaman'da aldığı zarfı açar."),
    13: dict(hikaye="Adana'da Mersin cezeriyesini Taşköprü yakınındaki tatlıcıya sert bir pazarlıktan sonra satar. Kebap ustası zırhla kıyma çekerken "
                    "'iş elle yapılır' der. Bu gün alım yoktur; gün batımında siyah bir arabanın onu izlediğini fark eder, gece otel lobisinde Selim Karahan onu bekler."),
    14: dict(hikaye="Defterin kuralı gereği çalışma günü: Kerem bir şalgam tezgâhında çalışıp yevmiye alır. Öğle yemeğinde Elif çıkagelir ve '81 İl' belgeseli "
                    "çekmek ister. Akşama Kozan'dan portakal alır; gece Elif'in telefonuna 'S.K.' imzalı bir mesaj düşer.",
             satilan="Yan iş: şalgam tezgâhında yevmiye",
             son="Kerem, Elif'in kendisini çekmesini kabul eder. O gece Elif'in telefonuna 'S.K.' imzalı bir mesaj düşer; ekranı hızla kapatır."),
    15: dict(hikaye="Osmaniye'de Kozan portakalı halde satılır. Elif, Karatepe-Aslantaş'taki iki dilli yazıtı anlatır; Kerem defterin kenarında da iki ayrı yazı "
                    "olduğunu fark edip fotoğrafını Leyla'ya gönderir. Yer fıstığı alır; gece Leyla arar."),
    16: dict(hikaye="Antakya'da depremden sonra yeniden ayağa kalkan Uzun Çarşı'da yeni açılan bir dükkâna yer fıstığı satar; öğle yemeğinde askıda yemek bırakır. "
                    "Habib-i Neccar Camii'nin yeniden inşa alanında bir usta ona enkazdan çıkan eski bir mermer bağış levhasını gösterir.",
             son="Levhada dedesinin adı yazılı: 'Hacı Rıza Aksoy — 1981.'"),
    17: dict(hikaye="Defterin kuralı gereği çalışma günü: Kerem künefe ustasının yanında çalışıp yevmiye alır, öğle arasında Elif'le Karahan adını konuşur. "
                    "Harbiye'deki atölyeden defne sabunu alır; gece gizli bir mesaj gelir.",
             satilan="Yan iş: künefeci yanında yevmiye"),
    18: dict(hikaye="Uyarıya rağmen Kilis'e gelir; defne sabunlarını aktara satar, lokantacıdan kürdanlı bir adamın onu sorduğunu öğrenir. Zeytinyağı "
                    "değirmeninde yağın suyun üstüne çıktığını görür ve Kilis zeytinyağı alır. Akşam otogarda Yaşar çıkagelir."),
    19: dict(hikaye="Toptancılar kapıyı kapatır. Yaşar'ın götürdüğü Nazlı Abla'nın kadın kooperatifi zeytinyağını adil fiyata alır. Kerem Zeugma Mozaik "
                    "Müzesi'nde defterin on dokuzuncu sayfasını okur; akşam kooperatifin duvarında asılı çerçeve, elindeki yırtık fotoğrafın öbür yarısıdır."),
    20: dict(hikaye="İki yarım fotoğraf birleşir ama dedenin yanındaki adamın yüzü yanmıştır. Kerem baklava atölyesinde çalışıp yevmiye alır, Bakırcılar "
                    "Çarşısı'nda bakırcıyla oturur ve Nazlı'nın tanıdığı üreticiden Antep fıstığı alır. Gün batımında Leyla arar."),
}

OVERRIDE.update({
    21: dict(hikaye="Kahramanmaraş'ta Antep fıstığını dondurma ustasına satar, öğle yemeğinde Elif'le dava konusunu konuşur, Maraş işi atölyesinde "
                    "defterin yirmi birinci sayfasını okur ve pul biber alır. Gece annesi arar: dava açılmıştır."),
    22: dict(hikaye="Malatya'da pul biberi satar, Arslantepe Höyüğü'nde dünyanın bilinen en eski kılıçlarının burada çıktığını öğrenir ve gün kurusu kayısı alır. "
                    "Gece annesinin gönderdiği avukat mektubunun ikinci sayfasını okur."),
    23: dict(hikaye="Adıyaman'da kayısıları Kahta'da satar, çiğ köfte yoğurmayı dener, Besni'den kuru üzüm alır ve gün batımında Nemrut'un karlı zirvesinde "
                    "defterin yirmi üçüncü sayfasını okur. Gece Elif'in telefonunda defter fotoğraflarını görür."),
    24: dict(hikaye="Şanlıurfa'da Besni üzümü beklenenin altında satılır: biri onun adına sahte ürün satmaktadır. Göbeklitepe'de defterin yirmi dördüncü sayfasını okur. "
                    "Akşam çarşıda kendi fotoğrafını taşıyan sahte paketleri ve arkasındaki Necmi'yi bulur."),
    25: dict(hikaye="Balıklıgöl'de sahte ürünler hakkında gerçeği anlatır; çarşı ona sahip çıkar. Harran'da defterin yirmi beşinci sayfasını okur, Urfa'dan isot alır, "
                    "akşam bir sıra gecesinde servis yapıp yevmiye alır. Gece Yaşar ilk kez 1979'dan bahseder."),
    26: dict(hikaye="Mardin'de Urfa isotunu lokantaya satar, Deyrulzafaran Manastırı'nda defterin yirmi altıncı sayfasını okur ve Midyat'ta telkari ustasından takı alır. "
                    "Usta, dedenin yaptırdığı gümüş anahtarın yarısını Kerem'e verir."),
    27: dict(hikaye="Diyarbakır'da telkari takıları Hasan Paşa Hanı'ndaki kuyumcuya satar; handa Leyla çıkagelir. Surların üstünde defterin yirmi yedinci sayfasını okur. "
                    "Akşam Leyla, listedeki seksen bir ismin alacaklı değil, dedenin borçlu olduğu kişiler olduğunu söyler."),
    28: dict(hikaye="On Gözlü Köprü'de dedesinin neden her ile gittiğini anlamaya çalışır. Burma kadayıf alır, akşam bir ciğerci dükkânında servis yapıp yevmiye kazanır. "
                    "Gece Selim'in paylaştığı videonun viral olduğunu görür."),
    29: dict(hikaye="Batman'da kadayıfları satar, yeni yerine taşınan Zeynel Bey Türbesi'nin önünde defterin yirmi dokuzuncu sayfasını okur ve dondurulmuş gılorik alır. "
                    "Gece otobüsün bagajında soğutucunun fişinin çekildiğini görür."),
    30: dict(hikaye="Siirt'e inince gıloriklerin yarısının bozulduğunu görür: ikinci zarar. Kalanını satar, büryan yer, Tillo'da defterin otuzuncu sayfasını okur ve "
                    "Siirt fıstığı alır. Gece Leyla mührün kenarındaki yazıyı çözer."),
})

OVERRIDE.update({
    31: dict(hikaye="Cizre'de Siirt fıstığını satar, Mem û Zîn'in hikâyesini dinler, Kırmızı Medrese'de defterin otuz birinci sayfasını okur ve kenger kahvesi alır. "
                    "Gece Hakkari otobüsünde Yaşar ona soluk bir zarf verir."),
    32: dict(hikaye="Hakkari'de kenger kahvesini satar, Cilo-Sat dağlarına bakarak defterin otuz ikinci sayfasını okur ve kilim dokuma evinden küçük kilim alır. "
                    "Gece Van yolunda tipiye yakalanır."),
    33: dict(hikaye="Van'da Hakkari kilimlerini satar, Van kahvaltısında kırk çeşidi tadar, gün batımında Van Kalesi'nden göle bakar. Gece zarftan 1979'dan bir "
                    "otobüs bileti çıkar; Elif'in telefonunda 'S.K.' mesajı yanar."),
    34: dict(baslik="Güven Kırılınca (2)",
             hikaye="Defterin kuralı gereği çalışma günü: Kerem sabah servisinde kahvaltı salonunda çalışıp yevmiye alır; Elif açıklamaya çalışır ama Kerem dinlemez. "
                    "Otlu peynir alır. Ertesi sabah Elif'in odası boştur."),
    35: dict(hikaye="Bitlis'te otlu peyniri satar, tek başına yemek yer, Ahlat'ın oymalı Selçuklu mezar taşlarının arasında defterin otuz beşinci sayfasını okur ve "
                    "Ahlat taşından hediyelik alır. Taş ustası dedenin sözünü aktarır."),
    36: dict(hikaye="Muş'ta Ahlat taşlarını satar, Leyla'dan haber alır, Malazgirt ovasında defterin otuz altıncı sayfasını okur ve lale motifli yün çorap alır. "
                    "Gece annesi duruşma tarihini bildirir.",
             son="Annesi arar: duruşma altmış gün sonra Ankara'da; dedenin masum olduğunu gösteren belge yoksa dükkân gidecek."),
    37: dict(baslik="Kaşıktan Akan Bal",
             hikaye="Bingöl'de Muş çoraplarını satar; yarı fiyatına bal satmaya çalışan adamı kaşık testiyle yakalar, arıcının deposundan gerçek Bingöl balı alır. "
                    "Akşam Necmi'nin arabası görünür."),
    38: dict(hikaye="Elazığ'da Bingöl balını satar, Hazar Gölü kıyısında yemek yer, Harput'ta yaşlı bir saz ustasını dinleyip defterin otuz sekizinci sayfasını okur "
                    "ve cevizli orcik alır. Gece Necmi karşısına oturur."),
    39: dict(alinan="Tunceli yayla tereyağı",
             hikaye="Tunceli'de orcikleri satar, Munzur'un kıyısında alabalık yer, yayla tereyağı alır ve Munzur Gözeleri'nin başında defterin otuz dokuzuncu "
                    "sayfasını okur. Gün batımında Elif onu bekler."),
    40: dict(baslik="Buz Tutan Şelale", satilan="Tunceli yayla tereyağı",
             hikaye="Erzincan'da tereyağını satar, Elif'e bir şans daha verir, buz tutmuş Girlevik Şelalesi'nin önünde defterin kırkıncı sayfasını okur ve tulum peyniri alır. "
                    "Gece Selim'den mesaj gelir."),
})

OVERRIDE.update({
    41: dict(hikaye="Erzurum'da Erzincan tulum peynirini satar, cağ kebabı ustasından ateşi eşit yakmayı öğrenir, Çifte Minareli Medrese'nin önünde defterin "
                    "kırk birinci sayfasını okur. Gece Leyla, listenin son isminin Hüseyin Usta olduğunu söyler."),
    42: dict(hikaye="Kerem Hüseyin Usta'yı arar ama usta konuşmak istemez. Defterin kuralı gereği çalışma günü: Oltu taşı atölyesinde tesbih ipliği takıp yevmiye alır, "
                    "Oltu taşı tesbih alır. Gece usta sonunda konuşur."),
    43: dict(hikaye="Doğubayazıt'ta Oltu tesbihlerini satar, abdigör köftesi yer, İshak Paşa Sarayı'nda Ağrı Dağı'nın karşısında defterin kırk üçüncü sayfasını okur "
                    "ve el dokuması kilim alır. Gece Yaşar'ın uyarı telefonu kesilir."),
    44: dict(alinan="Iğdır kuru kayısısı",
             hikaye="Iğdır'da kilimi satar, Aras Kuş Cenneti'nde kışlayan kuşları izler, Iğdır ile Malatya kayısısının farkını öğrenip kuru kayısı alır. "
                    "Gece Kars'tan bir toptancı iki katı fiyat teklif eder: ödeme çekle."),
    45: dict(satilan="Iğdır kuru kayısısı (çekle satıldı, nakit girmedi)",
             hikaye="Sabah Ani Harabeleri'ni gezen Kerem, öğleden sonra kayısıları çek karşılığı toptancıya teslim eder, nakitle Kars gravyeri alır. "
                    "Bankanın kapanmasına on dakika kala çeki yatırır."),
    46: dict(satilan="Kars gravyeri",
             hikaye="ÜÇÜNCÜ ZARAR: kayısıların parası yoktur; Elif karşılıksız çekin izini sürmek için ayrılır. Kerem gravyeri satar, donmuş Çıldır Gölü'nde buz "
                    "balıkçısına yardım eder ve kurutulmuş kaz alır. Akşam Yaşar çıkagelir."),
    47: dict(hikaye="Artvin'de kurutulmuş kazı satar, Macahel ormanında defterin kırk yedinci sayfasını okur ve Kafkas arısının Macahel balını alır. "
                    "Gece Elif, Selim'in karşılıksız çek yazışmalarını gönderir."),
    48: dict(hikaye="Rize'de Macahel balını satar, Zil Kale'nin sisli manzarasına bakar, çay bahçesinde 'iki yaprak bir tomurcuk' kuralını öğrenip Rize çayı alır. "
                    "Elif kanıt dosyasıyla yeniden yanındadır. Gece annesi Hüseyin Usta'nın kalp krizi geçirdiğini bildirir."),
    49: dict(hikaye="Trabzon'da Rize çayını düşük kârla satar: ait olduğu yerden uzağa sat. Hamsi yer, sisler içindeki Sümela Manastırı'na tırmanır, kemençe ustasıyla "
                    "horon dener. Gece annesi Hüseyin Usta'nın dükkânına girildiğini ve mühür yüzüğünün çalındığını bildirir."),
    50: dict(hikaye="Kerem hasır bilezik ustasını bulur, bir gün atölyede çalışıp yevmiye alır, ince gümüş tellerle hasır örmeyi öğrenir. Usta anahtarın ikinci "
                    "yarısını verir; iki yarı birleşir. Kerem gümüş hasır bilezik alır."),
})

OVERRIDE.update({
    51: dict(alinan="Bayburt taşı hediyelik",
             hikaye="Bayburt'ta gümüş hasır bilezikleri kuyumcuya satar, kale kahvehanesinde bir ozanı dinler, taş atölyesinden Bayburt taşı hediyelik alır. "
                    "Gece pansiyonun kapısında Necmi, parmağında Hüseyin Usta'nın yüzüğüyle durur."),
    52: dict(satilan="Bayburt taşı hediyelik",
             hikaye="Gümüşhane'de Necmi'nin şartını okur: iki anahtar yarısı karşılığında yüzük. Bayburt taşlarını satar, Karaca Mağarası'nda damlayan suyun taşı oyuşunu "
                    "görür, pestil ve köme alır. Gece Necmi buluşma yerini söyler."),
    53: dict(hikaye="Giresun'da pestilleri satar, öğle yemeğinde Yaşar'la tuzağı planlar, fındık deposunda Giresun'un eski adının Kerasus olduğunu öğrenir. "
                    "Gün batımında sahil yolunda tuzak işler ve yüzük geri alınır."),
    54: dict(hikaye="DÖRDÜNCÜ ZARAR: Kerem fındığı fındığın başkenti Ordu'ya getirir ve zararına satar. Boztepe'ye teleferikle çıkar, fındık ezmesi alır. "
                    "Gün batımında Yason Burnu'nda Leyla arar."),
    55: dict(hikaye="Samsun'da fındık ezmesini satar, Bandırma Vapuru Müzesi'nde defterin elli beşinci sayfasını okur ve Bafra nokulu alır. "
                    "Gece Selim'den Sinop'ta buluşma mesajı gelir."),
    56: dict(hikaye="Sinop'ta nokulları satar, Tarihi Cezaevi'nin avlusunda Selim'le buluşur; Selim babasından duyduğu hikâyeyi anlatır. Kerem gemi maketi alır. "
                    "Gün batımında Selim ona 1979 tarihli bir gazete kupürü uzatır."),
    57: dict(hikaye="Kastamonu'da gemi maketini satar, çekme helva ustasını izler, bir banka arşivinde Leyla'yla dedenin izini sürer ve siyez bulguru alır. "
                    "Akşam Rıza'nın 1980–1995 arasındaki ödeme dekontlarını bulurlar."),
    58: dict(hikaye="Safranbolu'da siyez bulgurunu satar, Cinci Hanı'nda dekontları gözden geçirir ve safranlı lokum alır. "
                    "Gece Leyla bir dekonttaki alıcıyı okur: Cevdet Karahan."),
    59: dict(hikaye="Amasra'da lokumu satar, Amasra salatası yer, Ceneviz Kalesi'nin surlarında defterin elli dokuzuncu sayfasını okur ve ahşap el işi alır. "
                    "Gece Elif'e tehdit mesajı gelir."),
    60: dict(hikaye="Zonguldak'ta ahşap işleri satar, Uzun Mehmet Anıtı'nın önünde defterin altmışıncı sayfasını okur ve Devrek bastonu alır. "
                    "Gece emekli bir madenci Rıza'nın emanet ettiği mektubu getirir."),
})

OVERRIDE.update({
    61: dict(baslik="Çerkes Sofrası", alinan="Düzce Çerkes peyniri",
             hikaye="Düzce'de Devrek bastonlarını satar, öğle yemeğinde Çerkes bir ailenin sofrasına misafir olur, Konuralp Antik Kenti'nde defterin altmış birinci "
                    "sayfasını okur ve tütsülenmiş Çerkes peyniri alır. Gece sahilde Rıza'nın mektubunu açar."),
    62: dict(satilan="Düzce Çerkes peyniri",
             hikaye="Bolu'da Çerkes peynirini satar, Mengenli bir aşçıdan 'tencereye iyi niyet koy' dersini alır, Abant Gölü'nde mektuptaki çırağı düşünür ve "
                    "Mudurnu tavuğu alır. Gece Yaşar'ı arar; Yaşar telefonu kapatır."),
    63: dict(hikaye="Sakarya'da Mudurnu tavuğunu ıslama köftecisine satar, Sapanca Gölü kıyısında defterin altmış üçüncü sayfasını okur ve Geyve ayvası alır. "
                    "Akşam minibüsün yan aynasında Necmi'yi görür."),
    64: dict(hikaye="Kocaeli'de ayvayı satar, SEKA Kâğıt Müzesi'nde defterin altmış dördüncü sayfasını okur ve İzmit pişmaniyesi alır. Akşam otogarda biri "
                    "Kerem'e çarpar; defter çantasından kaybolmuştur."),
    65: dict(hikaye="Defter olmadan ilk gün: Kerem Yalova'da pişmaniyeleri dalgınca satar, Yürüyen Köşk'ün önünde düşünür ve kesme çiçek alır. "
                    "Elif, Necmi'nin paylaşımlarından defterin yerini bulur."),
    66: dict(hikaye="Eminönü'nde kısmen solmuş çiçekleri satar, Yaşar'ın minibüsüyle Galata'ya gider. Necmi defterle kaçar; Kapalıçarşı'nın boyalı koridorlarında "
                    "kovalamaca yaşanır ve Kerem defteri geri alır."),
    67: dict(hikaye="Selim, Galata Kulesi'nde babasının her şeyini kaybettiğini anlatır. Kerem Mısır Çarşısı'nda bir baharatçının yanında çalışıp yevmiye alır, "
                    "UNESCO listesindeki Türk kahvesi kültürünü öğrenip kahve alır. Akşam Selim son sözünü söyler."),
    68: dict(hikaye="Tekirdağ'da Türk kahvesini satar, Rákóczi Müzesi'nde defterin altmış sekizinci sayfasını okur ve peynir helvası alır. "
                    "Gece Leyla, mahkemenin 1978 tarihli ortaklık senedini isteyeceğini söyler."),
    69: dict(hikaye="Kırklareli'nde peynir helvasını satar, İğneada Longoz Ormanı'nın sessizliğinde defterin altmış dokuzuncu sayfasını okur ve hardaliye alır. "
                    "Gece mührün üstüne bıçağı koyar; Hüseyin Usta tam o anda arar."),
    70: dict(hikaye="Edirne'de hardaliyeyi satar, Elif'e fragmanı yayınlama izni verir, Selimiye'nin kubbesi altında defterin yetmişinci sayfasını okur ve badem ezmesi alır. "
                    "Ertesi sabah üç bin sipariş ve Selim'den bir mesaj gelir."),
})

OVERRIDE.update({
    70: dict(hikaye="Edirne'de hardaliyeyi satar, Elif'e fragmanı yayınlama izni verir, Selimiye'nin kubbesi altında defterin yetmişinci sayfasını okur ve badem ezmesi alır. "
                    "Gece fragman patlar: üç bin sipariş ve Selim'den bir mesaj gelir.",
             son="Elif belgeselin fragmanını yayınlar. Gece telefonunda 3.000 sipariş mesajı… ve Selim'den tek kelime: 'Akıllıca.'"),
    71: dict(hikaye="Sabahın ilk otobüsüyle Çanakkale'ye gelir, Edirne badem ezmesini fragmanı izleyen bir tatlıcıya satar, Çanakkale Şehitliği'nde defterin yetmiş birinci "
                    "sayfasını okur ve Ezine peyniri alır. Akşam kordonda 'Ege Gıda' adlı bir firma dev sipariş teklif eder; adresi boş bir arsadır."),
    72: dict(hikaye="Ege Gıda teklifini reddeder, Ezine peynirini şarküteriye satar, Edremit'te öğle yemeği yer, Kaz Dağları'nda dere kıyısında defterin yetmiş ikinci "
                    "sayfasını okur ve Balıkesir höşmerimi alır. Gece pansiyonda imzasız bir mesaj düşer: Koza Han'da dedenin eski ortağı onu bekliyor."),
    73: dict(hikaye="Höşmerimi Bursa çarşısında satar, İnegöl köftesi yer, Ulu Cami'nin kubbeleri altında defterin yetmiş üçüncü sayfasını okur. "
                    "Akşamüstü Koza Han'da mesajı atan yaşlı ipekçiyle buluşur: Rıza ile Cevdet'i tanıştıran odur."),
    74: dict(hikaye="Defterin kuralıyla çalışma günü: ipekçinin dükkânında eşarp katlamayı öğrenip yevmiye alır, İskender yer, Karagöz-Hacivat gölge oyununu izler ve "
                    "defterin yetmiş dördüncü sayfasının sözünü duyar. Akşam ipekçiden Bursa ipeği eşarp alır; gece Selim'i arar."),
    75: dict(hikaye="Bursa ipeği eşarpları Bilecik'te satar, Söğüt'te Ertuğrul Gazi Türbesi'nin çınarı altında defterin yetmiş beşinci sayfasını okur ve Bozüyük'ten seramik alır. "
                    "Mahkemeye 21 gün kalmıştır; gece karşı tarafın tanığının Yaşar Demirci olduğunu öğrenir.",
             son="Annesi arar: 'Avukat aradı. Karşı taraf tanık bulmuş: otobüs şoförü Yaşar Demirci.' Kerem donar: Yaşar Kaptan?!"),
    76: dict(hikaye="Bozüyük seramiklerini Eskişehir'de satar, çibörek yer, Odunpazarı'nın renkli evleri arasında defterin yetmiş altıncı sayfasını okur ve lületaşı alır. "
                    "Akşam Porsuk kıyısında Yaşar'la yüz yüze konuşur."),
    77: dict(hikaye="Lületaşını Kütahya'da satar, Aizanoi'de Zeus Tapınağı'nın sütunları arasında defterin yetmiş yedinci sayfasını okur ve çini atölyesinden Kütahya çinisi alır. "
                    "Çıkarken usta eski bir karonun arkasını çevirir."),
    78: dict(hikaye="Kütahya çinilerini Uşak'ta satar, Uşak Müzesi'nde yıllarca yurt dışında kalıp geri dönen Karun Hazinesi'ni görür: 'Asıl hazine, döndüğü yere aittir.' "
                    "Halı atölyesinden seccade boy Uşak halısı alır. Gece Elif'in annesinden sesli mesaj gelir."),
    79: dict(hikaye="Uşak halılarını Manisa'da satar, Manisa kebabı yer, Sultan Camii'nin avlusunda defterin yetmiş dokuzuncu sayfasını okur ve mesir macunu alır. "
                    "Gece pansiyonda telefonuna ihbar düşer: Kemeraltı'nda adıyla sahte mesir satılıyor.",
             son="Gece pansiyonda Kerem'in telefonuna ihbar düşer: 'Kemeraltı'nda senin adınla sahte mesir satılıyor.'"),
    80: dict(hikaye="BEŞİNCİ ZARAR: Kemeraltı'nda Kerem'in adıyla satılan sahte mesir piyasayı bozmuştur; Kerem asıl mesiri neredeyse maliyetine satar. "
                    "Saat Kulesi'nin önünde boyoz-gevrek yer, tarihî hanın avlusunda defterin sekseninci sayfasını okur ve akşam Elif'in ailesinin evine gider. "
                    "Yemekte Elif'in dedesi eski bir kasetçalar getirir."),
})

OVERRIDE.update({
    81: dict(hikaye="Defterin kuralıyla çalışma günü: Kerem sabah erkenden balkonda dedesinin kasetini dinler ('önce yükünü taşı'), Görece'deki Nazarköy'de cam atölyesinde "
                    "çalışıp yevmiye alır, Efes'te Celsus Kütüphanesi'nin önünde defterin seksen birinci sayfasını okur ve nazar boncuğu alır. "
                    "Gece kasetin son saniyesinde dedesinin sesini duyar."),
    82: dict(hikaye="Nazar boncuklarını Aydın çarşısında satar, Nazilli'de öğle yemeği yer, Afrodisias'ta defterin seksen ikinci sayfasını okur ve kuru incir alır. "
                    "Gece Leyla arar: mahkeme öne alınmış, sekiz gün kalmıştır.",
             son="Leyla: 'Mahkeme duruşmayı öne aldı. Sekiz gün kaldı. Ve Selim tedbir kararı istiyor: defter mahkemeye teslim edilsin.'"),
    83: dict(hikaye="Aydın incirini Bodrum'da satar, Halikarnas Mozolesi'ni hatırlatan öğle yemeğini yer, Bodrum Kalesi'nde defterin seksen üçüncü sayfasını okur ve son "
                    "kasalardan Bodrum mandalinası alır. Gece limanda Yaşar'ın sesli mesajını dinler.",
             son="Yaşar sesli mesaj bırakır: 'Mahkemede ne diyeceğimi bilmiyorum. Cevdet'in yüzüne bakmadan konuşmam.'"),
    84: dict(hikaye="Bodrum mandalinasını Denizli'de satar, Pamukkale'nin beyaz teraslarında defterin seksen dördüncü sayfasını okur ve Buldan bezi alır. "
                    "Akşam dokumacının tezgâhında kopan ipin düğümlenişini izleyen Kerem fikrini değiştirir.",
             son="Buldan dokumacısı kopan ipi düğümlerken Kerem fikrini değiştirir: 'Davayı kazanmak istemiyorum. Bitirmek istiyorum.'"),
    85: dict(hikaye="Buldan bezini Burdur çarşısında satar, Salda Gölü'nün beyaz kıyısında defterin seksen beşinci sayfasını okur ve ceviz ezmesi alır. "
                    "Akşam sokakta Necmi yalnız ve yorgun karşısına çıkar.",
             son="Akşam sokakta Necmi karşısına çıkar; bu kez yalnız ve yorgun: 'Selim beni kovdu. Sana bir şey söylemem lazım.'"),
    86: dict(hikaye="Ceviz ezmesini Antalya çarşısında satar, Kaleiçi'nde öğle yemeği yer. Hadrian Kapısı'nda defterin seksen altıncı sayfasını okur ve Necmi'yi dinler: "
                    "Selim defteri yok etmek istiyormuş, çünkü babası ona sayfayı asla açtırmamasını söylemiş."),
    87: dict(hikaye="Defterin kuralıyla çalışma günü: Aspendos Antik Tiyatrosu'nda akşamki konser için sahne kurulumunda çalışıp yevmiye alır, Necmi'yle birlikte kasa taşır, "
                    "Antalya piyazı yer ve tiyatronun üst sırasında defterin seksen yedinci sayfasını okur. Akşam muz toptancısından Alanya muzu alırken yağmur başlar.",
             son="Yağmur şiddetlenir ve Isparta yolu kapanır. Muzlar beklemez, saatler daralıyor."),
    88: dict(hikaye="ALTINCI ZARAR: yol açılana kadar muzlar sararır, Kerem yarısı kararmış muzları ancak düşük fiyata satar. Eğirdir Gölü'nün kıyısında defterin seksen sekizinci "
                    "sayfasını okur ve gül yağı atölyesinden gül yağı ve gül suyu alır. Akşam Hüseyin Usta hastaneden çıktığını haber verir.",
             son="Hüseyin Usta hastaneden çıkmış: 'Kerem, yüzüğü sakın kaybetme; mührü o açacak.'"),
    89: dict(hikaye="Gül ürünlerini Afyon'da satar, sucuklu yumurta yer, Kocatepe'de defterin seksen dokuzuncu sayfasını okur ve Afyon sucuğu alır (Kayseri sucuğuyla dostça kıyaslar). "
                    "Gece Selim'in avukatı arar: defter yarın mahkemeye emanet edilmezse tedbir kararı istenecektir.",
             son="Gece pansiyonda Selim'in avukatı arar: 'Yarın duruşmada defteri mahkemeye emanet etmezseniz tedbir kararıyla elinizden alırız.'"),
    90: dict(hikaye="Sabah Anıtkabir'de defterin doksanıncı sayfasını okur, Afyon sucuğunu satar, avukatını öder. Duruşmada hâkim Elif'in getirdiği karşılıksız çek delilini dosyaya alır, "
                    "tedbir talebini reddeder ve mührün on gün içinde Kayseri'de bilirkişi huzurunda açılmasına karar verir."),
})

OVERRIDE.update({
    91: dict(hikaye="Mahkemeden ertesi gün çalışma günü: Hamamönü'nde tarihî bir konağın restorasyonunda usta Şevket'in yanında çalışır. Leyla Devlet Arşivleri'nde 1979 kaza tutanağını "
                    "bulur: Rıza hakkında hiçbir suçlama yoktur. Akşam yevmiyesini alır ve Beypazarı kurusu satın alır."),
    92: dict(hikaye="Beypazarı kurusunu Kırıkkale'de satar, Kızılırmak kıyısında defterin doksan ikinci sayfasını okur ve Keskin'den üzüm pekmezi alır. "
                    "Akşam köprü başında Yaşar otobüsüyle gelir."),
    93: dict(hikaye="Pekmezi Çankırı'da satar, öğle yemeğinde Yaşar'la tuz ekmeğin hakkını konuşur, Tuz Mağarası'nda defterin doksan üçüncü sayfasını okur ve kaya tuzu alır. "
                    "Gece telefonuna Selim'in hastane fotoğrafı düşer."),
    94: dict(hikaye="Kaya tuzunu Çorum'da satar, İskilip dolması yer, Hattuşa'nın Aslanlı Kapısı'nda ilk yazılı barış antlaşmasının hikâyesini dinler: 'Barış da bir ticarettir; iki taraf da kazanır.' "
                    "Çorum leblebisi alır. Gece Selim arar."),
    95: dict(hikaye="Leblebiyi Amasya'da satar, Ferhat ile Şirin efsanesini dinler, Kral Kaya Mezarları'nda defterin doksan beşinci sayfasını okur ve misket elması alır. "
                    "Akşam nehir kıyısında Hüseyin Usta'ya yüzüğünü geri verir."),
    96: dict(hikaye="Amasya misket elmasını Tokat Bedesteni'nde satar, Necmi'yle Tokat kebabı yer, Ballıca Mağarası'nda acele etmeleri gerektiğini konuşur, yazma atölyesinde "
                    "defterin doksan altıncı sayfasını okur ve Tokat yazması alır. Gece Selim'in sesi ilk kez kırıktır."),
    97: dict(hikaye="Gece yolculuğuyla Divriği'ye varır, Tokat yazmasını satar, Ulu Camii'nin taş kapısı önünde defterin doksan yedinci sayfasını okur ve el yapımı bıçak alır. "
                    "Gün batımında taş kapının önünde Cevdet ile karşılaşır."),
    98: dict(hikaye="Sivas bıçaklarını Yozgat'ta satar, kadın kooperatifinde tarhana çorbası içip tarhana alır. Çamlık'ın kenarındaki mezarlıkta Yaşar, Cevdet ve Selim'in önünde "
                    "1979 gecesini anlatır: kızının ameliyatı için kasayı alan Cevdet, suçu üstlenen Rıza."),
    99: dict(hikaye="Yozgat tarhanasını Kırşehir'de satar, Ahi Evran Türbesi'nde defterin doksan dokuzuncu sayfasını okur ve Mucur el dokuması halı alır. "
                    "Akşam avluda Hüseyin Usta onları bekler."),
})
