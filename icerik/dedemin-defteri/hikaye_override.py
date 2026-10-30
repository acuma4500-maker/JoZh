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
