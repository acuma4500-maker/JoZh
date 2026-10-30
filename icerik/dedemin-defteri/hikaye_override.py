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
