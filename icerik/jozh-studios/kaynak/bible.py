# -*- coding: utf-8 -*-
"""Dizi biblisi: ana hikâye, sezonlar, rota, ticaret stratejisi, karakter gelişimi.

Rota kuralı: Doğu Anadolu'dan başlanır (Video 6'daki duyuru). Bölgeler arası geçiş komşu illerden yapılır.
Bölüm numarası: 1-6 başlangıç videoları, 7-87 il bölümleri (rota sırasıyla).
"""

BIBLIO = dict(
    logline=("Bir motosiklet kazası yüzünden 800.000 TL borca giren 21 yaşındaki iki çocukluk arkadaşı, Mert ve Ali, "
             "100.000 TL'lik bir kasayla Türkiye'nin 81 ilini dolaşıp ticaret yaparak borcu ödemeye ve kendi markalarını kurmaya çalışır."),
    ana_hikaye=[
        "Malatya'da yeni bir eve çıkan Mert ve Ali, apartmanın üst katında oturan Cemil Bey'in markasız spor motosikletini ödünç alır. "
        "Şehir içinde yola fırlayan bir köpeği ezmemek için direksiyonu kıran Mert motoru park hâlindeki bir kamyonetin kasasına sürter; "
        "ikisi de kasklı olduğu için yara almaz ama motor ağır hasar görür.",
        "Cemil Bey tamir edilmiş motor istemez: 'Sıfırı 800 bin. Parayı getirin, motor sizin olsun.' Bir hafta süre verir. Aileler yardım "
        "edemeyecek durumdadır: Mert'in annesi Hatice reçel satarak geçinir, Ali'nin babası Hasan sera kredisiyle boğuşur.",
        "İnternette al-sat fırsatlarını inceleyen ikili, Ali'nin birikimi ve Mert'in oyun bilgisayarı başta olmak üzere ellerindeki her şeyi "
        "satıp 100.000 TL'lik bir kasa kurar. İlk gün Malatya'da kayısı ve ikinci el ürünlerle kâr edince Cemil Bey'e bir teklif götürürler: "
        "81 ili gezip ticaret yapacak, her bölgenin sonunda taksit ödeyecek, bütün yolculuğu da TikTok ve Instagram'da yayınlayacaklardır.",
        "Cemil Bey kabul eder ama şart koşar: tek bir taksit gecikirse senet mahkemeye gider. Yolculuk Doğu Anadolu'dan başlar ve yedi "
        "bölgeyle yedi sezona yayılır. Her ilde yerel bir ürün alınır, bir sonraki durakta ya da takipçi siparişleriyle satılır; her kuruş "
        "Ali'nin kahverengi defterine ve ekrandaki KASA sayacına yazılır.",
        "Yol boyunca kazanç kadar zarar, dostluk kadar kavga da vardır. Akdeniz'de Ali'nin babası onlara eski kamyonetini verir; Ege'de "
        "'81 Şehir Kutusu' fikri doğar; İstanbul'da Mert'in acelesi kasanın bir kısmını eritir ve iki arkadaş ilk kez yollarını ayırır; "
        "Karadeniz'in yağmurunda yeniden bir araya gelirler. Final Ankara'da yılbaşı gecesi, son taksitle gelir.",
    ],
    temalar=["Emek ve dürüst ticaret", "Arkadaşlık ve güven", "Acelecilik ile planlama arasındaki denge", "Yerel üreticiye saygı",
             "Şeffaflık: reklam ve iş birliği her zaman açıkça söylenir"],
    ticaret=[
        "Model: Her ilde o ilin bilinen, gerçek bir yerel ürünü üreticiden ya da çarşı esnafından alınır; bir sonraki ilde dükkânlara, "
        "lokantalara ya da takipçi siparişleriyle (kargo) satılır. Böylece her bölüm iki şehri birbirine bağlar.",
        "Fiyatlar 2026 piyasasına yakın tahminlerdir ve sahnede adet x birim fiyat olarak söylenir; kasa sayacı bu hesaba göre değişir.",
        "Giderler: otobüs/feribot/yakıt (ulaşım), pansiyon (konaklama), yemek, kargo ve ambalaj (diğer gider). Akdeniz'den sonra "
        "Hasan'ın kamyoneti ile yakıt gideri ödenir.",
        "Borç: 800.000 TL, yedi taksitte ödenir (Doğu 50 bin, Güneydoğu 80 bin, Akdeniz 100 bin, Ege 120 bin, Marmara 150 bin, "
        "Karadeniz 150 bin, İç Anadolu 150 bin). Taksit kasadan çıkar ama net kârdan düşülmez; panelde ayrı gösterilir.",
        "Sponsorluk: Hikâyede işletmeler mesaj atabilir ('Sizi takip ediyoruz...'), ama gerçek bir anlaşma olmadan hiçbir işletme sponsor "
        "olarak gösterilmez. Bölümlerdeki işletmeler kurgusal ve isimsizdir. Gerçek bir iş birliği yapılırsa ilgili bölümün sahnesi o "
        "işletmeye göre yeniden yazılır ve videoda 'reklam / iş birliği' ibaresi kullanılır.",
        "Ürün bilgisi: Her ürün o ilin gerçekten bilinen bir ürünüdür (ör. Malatya kayısısı, Tunceli sarımsağı, Kars gravyeri, Van otlu "
        "peyniri, Bingöl balı, Siirt fıstığı, Gaziantep fıstığı, Kahramanmaraş biberi, Isparta gül ürünleri, Denizli havlusu, Bursa ipeği, "
        "Rize çayı, Çorum leblebisi, Kayseri pastırması). Belirsiz bilgilerde 'yerel' denir, iddia kurulmaz.",
    ],
    gelisim=[
        ("Mert", "Aceleci girişimciden plan yapan bir lidere. Doğu'da cesareti işe yarar ama Ağrı'da taze kayısıyla zarar eder; İstanbul'da "
                 "hızlı kazanç peşinde kasayı riske atıp en büyük dersini alır; Karadeniz'de sabretmeyi, İç Anadolu'da Ali'ye güvenmeyi öğrenir. "
                 "Finalde 'önce hesap, sonra cesaret' der."),
        ("Ali", "Çekingen hesap adamından kendine güvenen bir ortağa. Önce Mert'in arkasında durur; Kars'ta ilk büyük pazarlığı kendisi yapar, "
                "Antalya'da babasına 'hayır' demeyi öğrenir, İstanbul'da Mert'e karşı çıkar ve haklı çıkar. Finalde kamera önünde markayı o anlatır."),
        ("Cemil Bey", "Sert alacaklıdan sessiz bir hamiye. Taksitleri alırken hep soğuktur, ama videoları gizlice izler. Finalde motoru tamir "
                      "ettirip onlara verir: 'Ben paranın değil, sözün peşindeydim.'"),
    ],
    dunyagorsel=[
        "Stil: semi-realistic stylized 3D animasyon, Pixar benzeri oranlar, gerçekçi anatomi, cilt, saç ve kumaş dokuları.",
        "Dış dünya: gerçekçi, sinematik şehir ve doğa; gerçek sokaklar, taş, ahşap, toprak dokuları; film kalitesinde ışık.",
        "Format: dikey 9:16, 1080x1920, her video 60 saniye = 6 sahne x 10 saniye. Konuşmalar Türkçe, prompt'lar İngilizce.",
        "Süreklilik: karakter tarifleri her prompt'a aynen girer. Kıyafet yalnızca Bölüm 57 Düzce'de (yağmur, pazardan mont) değişir.",
        "Kasa göstergesi: Bölüm 4'ün son sahnesinde açılır; o andan sonra her sahnenin arasında hazır bir kasa videosu prompt'u vardır.",
    ],
)

SEZONLAR = [
    dict(id="s0", no=0, bolge=None, ad="Başlangıç: 800 Bin Lira", alt="Malatya · Video 1-6", rota=[],
         acilis="Yeni eve çıkan iki arkadaş, ödünç alınan bir motosiklet ve tek bir kaza.",
         hikaye="Kaza, borç, ailelerin çaresizliği, ticaret fikri, ilk alışveriş ve 81 şehir duyurusu. Kasa Video 4'ün son sahnesinde 100.000 TL ile açılır.",
         hedef="Bir hafta içinde 800.000 TL bulmak imkânsız; hedef ilk kârla Cemil Bey'i taksit planına ikna etmek.",
         orta="Video 3'te ailelerin de borçlu olduğu ortaya çıkar; Video 4'te ikili ellerindeki her şeyi satıp kasayı kurar.",
         final="Video 6: Kameraya dönüp 81 il yolculuğunu, sponsorluk ve iş birliği çağrısını duyururlar.",
         gecis="Yarın sabah ilk durak Malatya: kayısı bahçeleri ve Arslantepe.", taksit=0),
    dict(id="s1", no=1, bolge="dogu", ad="Sezon 1 · Dağların Pazarı", alt="Doğu Anadolu · 14 il · Haziran",
         rota=["Malatya", "Elazığ", "Tunceli", "Erzincan", "Erzurum", "Ardahan", "Kars", "Iğdır", "Ağrı", "Van", "Hakkari",
               "Bitlis", "Muş", "Bingöl"],
         acilis="Malatya'da Hatice'nin kahvaltısı ve büyük kayısı alımıyla yola çıkış.",
         hikaye="Dağ yolları, yaylalar ve sınır şehirleri. Otobüs, dolmuş ve feribotla ilerleyip her ilde bir yerel ürün alırlar. "
                "Takipçileri ilk siparişleri vermeye başlar; Ali ilk büyük pazarlığını Kars'ta yapar.",
         hedef="Kasayı büyütmek ve sezon sonunda 50.000 TL'lik ilk taksiti ödemek.",
         orta="Ağrı'da taze kayısı sıcakta bozulur: ilk zarar. Van'da Mert'in acelesine karşı Ali ilk kez sesini yükseltir. "
              "Hakkari'de dağ yolunda yolları bir sürüyle kesilir.",
         final="Bingöl'de yüzen adaların kıyısında ilk taksit Cemil Bey'e gönderilir. Cemil Bey'in cevabı tek kelime: 'Gördüm.'",
         gecis="Diyarbakır surlarının arasında sıcak bir yaz başlıyor.", taksit=50000),
    dict(id="s2", no=2, bolge="guneydogu", ad="Sezon 2 · Mezopotamya Hesabı", alt="Güneydoğu Anadolu · 9 il · Temmuz",
         rota=["Diyarbakır", "Batman", "Siirt", "Şırnak", "Mardin", "Şanlıurfa", "Adıyaman", "Gaziantep", "Kilis"],
         acilis="Diyarbakır'da Hasanpaşa Hanı kahvaltısı ve kırk derecelik bir sıcak.",
         hikaye="Kadim şehirler, taş evler, bereketli ovalar. Fıstık, isot, telkari ve zeytinyağı. Takipçi sayısı artar, ilk işletme "
                "mesajları gelir ama ikili hiçbirini 'sponsor' diye göstermez.",
         hedef="80.000 TL'lik ikinci taksit ve büyük hacimli ilk alım (Gaziantep fıstığı).",
         orta="Siirt'te Mert'in sırtı güneşte yanar; Şanlıurfa'daki sıra gecesinde Ali ilk kez sahneye çıkıp türkü söyler. "
              "Gaziantep'te sahte etiketli fıstık satmaya çalışan biri yakalanır.",
         final="Kilis'te zeytin ağaçlarının altında ikinci taksit ödenir. Ali'nin babası arar: 'Antalya'ya uğrayın, sizi bekliyorum.'",
         gecis="Akdeniz yolu: Hatay'ın künefesi.", taksit=80000),
    dict(id="s3", no=3, bolge="akdeniz", ad="Sezon 3 · Eve Dönüş Yolu", alt="Akdeniz · 8 il · Ağustos",
         rota=["Hatay", "Osmaniye", "Kahramanmaraş", "Adana", "Mersin", "Antalya", "Isparta", "Burdur"],
         acilis="Hatay'da depremden sonra yeniden açılan dükkânlar ve dayanışma.",
         hikaye="Nemli sıcak, narenciye, sera ve deniz. Antalya'da Ali'nin evine dönüş: Hasan'ın serası, borç ve bir aile meselesi. "
                "Hasan onlara eski beyaz kamyoneti verir; artık mallarını kendileri taşırlar.",
         hedef="100.000 TL'lik üçüncü taksit ve kamyonetle daha büyük alımlar.",
         orta="Kahramanmaraş'ta dondurma ustası Mert'i yedi kez kandırır (geleneksel şov); Anamur'da muz seralarının önünde Mert kendi kuralını hatırlar. "
              "Antalya'da Ali, babasının serası için kasadan para istemez: 'Önce söz verdiğimiz borç.'",
         final="Burdur'da Salda Gölü kıyısında üçüncü taksit. Mert ilk kez Ali'ye kasanın anahtarını tamamen bırakır.",
         gecis="Ege'ye iniş: Denizli'nin havluları ve Pamukkale.", taksit=100000),
    dict(id="s4", no=4, bolge="ege", ad="Sezon 4 · Zeytin Dalı", alt="Ege · 8 il · Eylül",
         rota=["Denizli", "Muğla", "Aydın", "İzmir", "Manisa", "Uşak", "Afyonkarahisar", "Kütahya"],
         acilis="Denizli'de tekstil atölyesinde bir günlük iş ve horoz efsanesi.",
         hikaye="Zeytin, incir, üzüm, bal ve çini. Ege'de '81 Şehir Kutusu' fikri doğar: her bölgenin ürünlerinden oluşan bir kutu. "
                "İlk kutular İzmir'de hazırlanır, siparişler yağmaya başlar.",
         hedef="120.000 TL'lik dördüncü taksit ve marka fikrinin ilk denemesi.",
         orta="Muğla'da çam balı ormanında kaybolurlar; Manisa'da bağ bozumunda çalışırlar; Uşak'ta bir halı ustası "
              "onlara 'acele işe şeytan karışır' dersini verir.",
         final="Kütahya'da çini atölyesinde kutunun logosu çiniye işlenir; dördüncü taksit ödenir.",
         gecis="Marmara'ya, büyük pazara.", taksit=120000),
    dict(id="s5", no=5, bolge="marmara", ad="Sezon 5 · Büyük Pazar", alt="Marmara · 11 il · Ekim",
         rota=["Bilecik", "Bursa", "Balıkesir", "Çanakkale", "Edirne", "Kırklareli", "Tekirdağ", "İstanbul", "Yalova", "Kocaeli",
               "Sakarya"],
         acilis="Bilecik Söğüt'te bir başlangıç hikâyesi: 'Her büyük iş küçük bir çadırla başlar.'",
         hikaye="Kalabalık şehirler, büyük siparişler, büyük riskler. Bursa'da ipek, Edirne'de badem ezmesi, İstanbul'da toptan pazar. "
                "Mert, İstanbul'da 'garantili' bir toptan teklifine atlar ve kasanın bir kısmını kaybeder. İki arkadaş ilk kez ayrılır.",
         hedef="150.000 TL'lik beşinci taksit ve kayıptan sonra toparlanmak.",
         orta="İstanbul'da kayıp ve kavga; Yalova'da Ali tek başına çalışır; Kocaeli'de Mert pişmaniye atölyesinde özür dilemenin "
              "yolunu bulur.",
         final="Sakarya'da Sapanca kıyısında barışırlar; beşinci taksit son kuruşuna kadar ödenir.",
         gecis="Karadeniz'in yağmuru başlıyor.", taksit=150000),
    dict(id="s6", no=6, bolge="karadeniz", ad="Sezon 6 · Fırtına ve Fındık", alt="Karadeniz · 18 il · Ekim-Kasım",
         rota=["Düzce", "Bolu", "Zonguldak", "Bartın", "Karabük", "Kastamonu", "Sinop", "Samsun", "Ordu", "Giresun", "Trabzon",
               "Rize", "Artvin", "Bayburt", "Gümüşhane", "Tokat", "Amasya", "Çorum"],
         acilis="Düzce'de yağmur başlar; pazardan mont alırlar (kıyafet değişimi).",
         hikaye="Yeşil vadiler, fırtınalı deniz, fındık, çay, hamsi. En uzun sezon. Kutu siparişleri büyür, kamyonet yorulur. "
                "Mert sabrı, Ali cesareti öğrenir.",
         hedef="150.000 TL'lik altıncı taksit; kış bastırmadan dağ yollarını aşmak.",
         orta="Zonguldak'ta maden şehrinin emeğini görürler; Trabzon'da büyük kutu siparişi; Bayburt'ta ilk kar ve kamyonet yolda kalır.",
         final="Çorum'da leblebi kavurucusunun yanında altıncı taksit. Cemil Bey ilk kez kendisi arar: 'Ankara'da görüşelim.'",
         gecis="İç Anadolu'nun karlı bozkırına.", taksit=150000),
    dict(id="s7", no=7, bolge="icanadolu", ad="Sezon 7 · Son Hesap", alt="İç Anadolu · 13 il · Aralık",
         rota=["Çankırı", "Kırıkkale", "Kırşehir", "Yozgat", "Sivas", "Kayseri", "Nevşehir", "Niğde", "Aksaray", "Karaman",
               "Konya", "Eskişehir", "Ankara"],
         acilis="Çankırı'da tuz mağarası: 'Tuz bozulmaz, söz de bozulmamalı.'",
         hikaye="Kar, bozkır, kervansaraylar ve ahilik geleneği. Kırşehir'de Ahi Evran'ın 'eline, beline, diline sahip ol' öğüdü sezonun "
                "sözü olur. Son taksitin parası Konya'da tamamlanır.",
         hedef="Son 150.000 TL ve yılbaşı gecesi Ankara'da Cemil Bey'le buluşma.",
         orta="Sivas'ta tipiye yakalanırlar; Kayseri'de pastırma pazarlığında Ali, Mert'ten daha sert çıkar; Kapadokya'da balonları "
              "izlerken geleceği konuşurlar.",
         final="Ankara'da Hamamönü'nde son taksit. Cemil Bey tamir ettirdiği motoru getirir: 'Motor sizin.'",
         gecis="Yeni sezon fikri: '81 Şehir Kutusu' bir markaya dönüşüyor. 'Bir sonraki yolculuk: Türkiye'den dünyaya?'", taksit=150000),
]
