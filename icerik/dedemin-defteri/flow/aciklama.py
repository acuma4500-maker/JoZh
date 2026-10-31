# -*- coding: utf-8 -*-
"""Instagram video açıklamaları (4 hashtag). {kasa} ifadesi bölümün kapanış kasasıyla değiştirilir."""

ACIKLAMA = {
    1: ("Londra'da hayalini kurduğu sneaker dükkânı battı. Kapıda ev sahibi, cebinde borç, kafasında tek soru: şimdi ne olacak? 🌧️\n\n"
        "Gece dükkânı son kez kapatırken telefonunda 14 cevapsız çağrı çıkıyor. Sence arayan kim?\n\n"
        "Hikâye başlıyor, takipte kal. 👇",
        ["#DedeminDefteri", "#Londra", "#Animasyon", "#81İl"]),
    2: ("Bazen bir telefon her şeyi değiştirir. Dedesini kaybeden Kerem'in cebinde bilet parası bile yok. ✈️\n\n"
        "Koleksiyonunu satıp yola çıkıyor ama tek bir çifti kendine saklıyor. Sence neden?\n\n"
        "Annesinin son sözü kulağında: 'Hadi dön artık.' Devamı bir sonraki bölümde.",
        ["#DedeminDefteri", "#Kayseri", "#Animasyon", "#81İl"]),
    3: ("Dedesinden ev bekliyordu, dükkân bekliyordu. Elinde kalan: eski bir deri defter, son sayfası mühürlü. 📖\n\n"
        "Vasiyette tek cümle var: 'Yol bitmeden açılmaz.' Defterin ilk sayfasında ise bir adres ve bir uyarı: 'Kimseye güvenme.'\n\n"
        "Sence defterde ne saklı? Yorumlara yaz!",
        ["#DedeminDefteri", "#Miras", "#Kayseri", "#81İl"]),
    4: ("Kapalı Çarşı'nın içinde dedesinin can dostu Hüseyin Usta bekliyordu. Ahiliğin üç kuralını öğrendi: eline, beline, diline sahip ol. 🤝\n\n"
        "5.000 ₺ sermaye aldı ama tek şartla: kasa sıfıra düşmeyecek. Çarşı kapısında ise takım elbiseli bir adam: 'Bir milyon veririm, defteri bana sat.'\n\n"
        "Sen satar mıydın? 💬 Kasa: {kasa}",
        ["#DedeminDefteri", "#Kayseri", "#Ahilik", "#81İl"]),
    5: ("İlk pastırma ticareti! Londra'dan kalan son sneaker çiftini sattı, Kayseri pastırması aldı. 🥩\n\n"
        "Usta bir ders verdi: 'Malın kusurunu önce sen söyle.' Otobüste iki koltuk arkada ise biri telefonda fısıldıyor... 👀\n\n"
        "Kasa: {kasa}. Yolculuk başlıyor!",
        ["#DedeminDefteri", "#Kayseri", "#Pastırma", "#81İl"]),
    6: ("Kapadokya'da gün doğumu, balonlar ve yeni bir tanışma: belgeselci Elif. 🎈\n\n"
        "Pastırmayı sattı, Avanos'tan çömlek aldı. Ama Elif'in fotoğrafında arka planda biri var: Kerem'i dürbünle izleyen biri.\n\n"
        "Kasa: {kasa}",
        ["#DedeminDefteri", "#Kapadokya", "#Nevşehir", "#81İl"]),
    7: ("Niğde'de elma, Gümüşler Manastırı'nda bin yıllık freskler. 🍎\n\n"
        "Kaptan Yaşar yolda Niğde'yi anlattı ama defterin kapağındaki el yazısını görünce frene bastı. Bu yazıyı nereden tanıyor?\n\n"
        "Kasa: {kasa}",
        ["#DedeminDefteri", "#Niğde", "#GümüşlerManastırı", "#81İl"]),
    8: ("Sultanhanı'nda bir gece. 🌙 'Kervan nerede konaklarsa tüccar orada öğrenir.'\n\n"
        "Taşpınar halılarını aldı ama gece biri defterin mührünü kazımaya çalıştı. Kim yaptı?\n\n"
        "Kasa: {kasa}",
        ["#DedeminDefteri", "#Aksaray", "#Sultanhanı", "#81İl"]),
    9: ("Konya'da acele edince az kâr etti: sabır, pazarlığın yarısıdır. ⏳\n\n"
        "Mevlana Müzesi'nde Dr. Leyla defterin kenar notlarını okudu. Hepsi 1979'dan. Ve sayfada tam 81 isimlik bir liste var...\n\n"
        "Kasa: {kasa}",
        ["#DedeminDefteri", "#Konya", "#Mevlana", "#81İl"]),
    10: ("Etli ekmek fırınında çalıştı, Mevlana şekeri aldı, sema izledi: dönmek için önce durmayı bil. 🌀\n\n"
         "Sonra masasına tatlı dilli biri oturdu ve kartvizit bıraktı: Karahan Lojistik. Selim'in adamı!\n\n"
         "Kasa: {kasa}",
         ["#DedeminDefteri", "#Konya", "#Sema", "#81İl"]),
    11: ("Türkçe'nin başkenti Karaman: 1277 fermanı, Divle Obruk peyniri ve mağarada bir sürpriz. 🧀\n\n"
         "Yaşlı usta zarf uzattı: 'Hacı Rıza bana borçlu değildi, ben ona borçluydum.' Zarfta ne var?\n\n"
         "Kasa: {kasa}",
         ["#DedeminDefteri", "#Karaman", "#Peynir", "#81İl"]),
    12: ("İlk büyük zarar! Mersin'e inince soğutucunun kablosu kesilmişti, peynirin bir kısmı gitti. 😔\n\n"
         "Ama Kerem dersi aldı: zararından ders almayan batar. Zarfı açtı: yırtık bir fotoğraf, 1979. Dedesinin yanındaki adam kim?\n\n"
         "Kasa: {kasa}",
         ["#DedeminDefteri", "#Mersin", "#Kızkalesi", "#81İl"]),
    13: ("Adana'da Taşköprü, zırhla kıyma çeken kebap ustası ve otel lobisinde sürpriz: Selim Karahan'ın kendisi geldi. 🔥\n\n"
         "'Bir ay içinde o defter benim olacak.' Kerem ne yapacak?\n\n"
         "Kasa: {kasa}",
         ["#DedeminDefteri", "#Adana", "#Taşköprü", "#81İl"]),
    14: ("Şalgam tezgâhında çalıştı, Kozan'dan portakal aldı. 🍊\n\n"
         "Elif belgesel çekmek istiyor ama telefonuna 'S.K.' imzalı bir mesaj geldi. Elif kime çalışıyor?\n\n"
         "Kasa: {kasa}",
         ["#DedeminDefteri", "#Adana", "#Kozan", "#81İl"]),
    15: ("Karatepe-Aslantaş'ta iki dilli yazıt, Osmaniye'de yer fıstığı. 🦁\n\n"
         "Leyla aradı: defterin sayfalarının altında gizli bir ikinci metin var ve ilk kelimesi bir soyadı: Karahan.\n\n"
         "Kasa: {kasa}",
         ["#DedeminDefteri", "#Osmaniye", "#Karatepe", "#81İl"]),
    16: ("Depremden sonra yeniden ayağa kalkan Antakya'da Uzun Çarşı'da dayanışmayı gördü. ❤️\n\n"
         "Habib-i Neccar Camii'nin yeniden inşa alanında enkazdan çıkan eski bir bağış levhasında bir isim: Hacı Rıza Aksoy, 1981. Dedesi her yerde izini bırakmış.\n\n"
         "Kasa: {kasa}",
         ["#DedeminDefteri", "#Hatay", "#Antakya", "#81İl"]),
    17: ("Künefe ustasının yanında bir gün çalıştı, Harbiye'den defne sabunu aldı. 🧼\n\n"
         "Gece gizli bir mesaj geldi: 'Kilis'e gitme. Seni bekliyorlar.' Gidecek mi?\n\n"
         "Kasa: {kasa}",
         ["#DedeminDefteri", "#Hatay", "#Künefe", "#81İl"]),
    18: ("Uyarıya rağmen Kilis'e gitti. Zeytinyağı suyun üstüne çıkar, doğru da öyle. 🫒\n\n"
         "Mesajı atan Yaşar Kaptan çıktı ve kötü haber verdi: Gaziantep'te kimse ondan mal almayacak.\n\n"
         "Kasa: {kasa}",
         ["#DedeminDefteri", "#Kilis", "#Zeytinyağı", "#81İl"]),
    19: ("Gaziantep'te toptancılar kapıyı kapattı. Nazlı Abla'nın kadın kooperatifi kapısını açtı. 💪\n\n"
         "Duvarda eski bir fotoğraf asılı ve Kerem'in elindeki yırtık fotoğrafın öbür yarısı bu!\n\n"
         "Kasa: {kasa}",
         ["#DedeminDefteri", "#Gaziantep", "#Zeugma", "#81İl"]),
    20: ("İki yarım fotoğraf birleşti ama dedenin yanındaki adamın yüzü yanık. 🖼️\n\n"
         "Antep fıstığı aldı, baklava atölyesinde çalıştı. Sonra Leyla aradı: 81 isimlik listenin birinci sırasında yazan isim Cevdet Karahan.\n\n"
         "Kasa: {kasa}",
         ["#DedeminDefteri", "#Gaziantep", "#AntepFıstığı", "#81İl"]),
}
