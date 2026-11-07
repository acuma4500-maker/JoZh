# -*- coding: utf-8 -*-
"""Kervan — Sezon 1 rotası ve kasa planı (Bölüm 1–50).

Her satır: yer, bölge, kapak başlığı, alınan/satılan mal, bölüm sonu kasası,
aksilik, defterin ipucu ve cliffhanger. kasa_bas bir önceki bölümün kasa_son'udur.
Bölge sonlarında (B7, B14, B21, B28, B35, B42, B50) bir mühür parçası bulunur.
"""

BASLANGIC = 200_000
ROTA = []


def _b(sehir, bolge, baslik, alinan, satilan, kasa_son, aksilik, ipucu, son):
    kasa_bas = ROTA[-1]["kasa_son"] if ROTA else BASLANGIC
    ROTA.append(dict(no=len(ROTA) + 1, sehir=sehir, bolge=bolge, baslik=baslik, alinan=alinan,
                     satilan=satilan, kasa_bas=kasa_bas, kasa_son=kasa_son, aksilik=aksilik,
                     ipucu=ipucu, son=son))


# ── MARMARA (B1–B7) ─────────────────────────────────────────────────────────
_b("İstanbul", "Marmara", "ESKİ DEFTER",
   "Kapalıçarşı'daki sahaftan yüz yıllık deri defter; Eminönü'nden toptan lokum ve akide şekeri",
   "— (ilk bölüm: henüz satış yok)",
   186_000,
   "Sahaf defter için beklenmedik derecede yüksek fiyat ister; Defne pazarlıkta ilk kez geri adım atar.",
   "Defterin ilk sayfası: \"Kervan İstanbul'dan çıkar, Edirne'de ilk hanı bulur. — S.K. 1926\"",
   "Kerem defterin arka kapağında yarısı kırılmış, deve kervanı şeklinde bronz bir mühür izi fark eder.")
_b("Edirne", "Marmara", "İLK SATIŞ",
   "Edirne'nin meyve şeklindeki el yapımı sabunları",
   "İstanbul lokumu ve akide şekeri, Selimiye çarşısındaki dükkânlara",
   214_000,
   "Kaan sabun kokulu kamyonetin içinde lokumları açık bırakır; bir kutu lokum sabun kokar, ucuza gider.",
   "Defter Ali Paşa Çarşısı'nda bir sabuncu ailesinin adını verir; dükkânın torunu defterdeki mührü tanır.",
   "Sabuncunun yaşlı annesi: \"Yüz yıl önce de üç genç gelmişti… biri hiç geri dönmedi.\"")
_b("Tekirdağ", "Marmara", "KÖFTE SAVAŞI",
   "Tekirdağ köftesi için baharat karışımı ve Şarköy'den taze üzüm",
   "Edirne sabunları, sahil kasabalarındaki hediyelik dükkânlara",
   238_000,
   "Kaan köfte yarışmasına katılıp kazanır, ama ödül olarak para yerine 50 kilo baharat verilir.",
   "Defterde bir rıhtım çizimi ve \"Rüzgâr dönmeden boğazı geç\" notu.",
   "Hava raporu: yarın Çanakkale'de fırtına. Kamyonet ise tamamen dolu.")
_b("Çanakkale", "Marmara", "FIRTINA",
   "Çanakkale seramikleri (testi ve çanak)",
   "Şarköy üzümü — fırtına yüzünden yarısı bozulmuş halde",
   221_000,
   "Feribot fırtına yüzünden 9 saat gecikir, üzümlerin yarısı çürür. İlk büyük zarar.",
   "Defterde Kilitbahir Kalesi'nin bir burcunun çizimi; burcun taşında kazınmış küçük bir deve izi bulunur.",
   "Taşın arkasından 1926 tarihli, yarısı yanmış bir tren bileti çıkar: \"İstanbul → ?\"")
_b("Ayvalık (Balıkesir)", "Marmara", "ZEYTİN KARASI",
   "Ayvalık'ın soğuk sıkım zeytinyağı, 2 ton",
   "Çanakkale seramikleri, Cunda'daki butik otellere",
   262_000,
   "Defne zeytinyağını laboratuvara test ettirmeden almak istemez; test bir gün sürer, fırsat kaçmak üzeredir.",
   "Defter eski bir zeytinyağı fabrikasının bacasını çizmiş; bacada yüz yıllık bir kervan işareti var.",
   "Fabrikanın kapısındaki yaşlı bekçi defteri görünce elindeki çayı düşürür.")
_b("Bursa", "Marmara", "İPEK YOLU",
   "Koza Han'dan ipek eşarp ve kestane şekeri",
   "Ayvalık zeytinyağı, Bursa'daki şarküterilere",
   305_000,
   "Kaan kestane şekerlerinin yarısını yolda yer; Defne kasadan 'Kaan'ın midesi' diye gider yazar.",
   "Defter Koza Han'ın avlusundaki şadırvanı işaret ediyor: \"Su nereden gelirse yol oradan gider.\"",
   "Şadırvanın dibinde, yosunun altında bronz bir parçanın kenarı parlar.")
_b("İznik (Bursa)", "Marmara", "BİRİNCİ MÜHÜR",
   "El yapımı İznik çinisi, 300 parça",
   "Bursa ipeği ve kestane şekeri, İznik'teki turist dükkânlarına",
   348_000,
   "Çini atölyesinin fırını patlar; ustaya yardım edip siparişi kurtarmak için bir gece uykusuz kalırlar.",
   "Bursa'da bulunan bronz parça, deve kervanı mührünün ilk parçası çıkar. Defterde yazıyor: \"Yedi bölge, yedi parça.\"",
   "Mühür parçasının arkasında kazınmış tek kelime: \"KÜTAHYA\".")

# ── EGE (B8–B14) ────────────────────────────────────────────────────────────
_b("Kütahya", "Ege", "ÇİNİ USTASI",
   "Kütahya porseleni (çay takımı), toptan",
   "İznik çinisi, Kütahya'daki çini koleksiyoncularına",
   392_000,
   "Bir koleksiyoncu İznik çinilerini 'fazla yeni' bulur; Kerem çiniyi yapan ustanın hikâyesini anlatınca fikri değişir.",
   "Defterde 1926'dan bir çini sipariş listesi; listedeki son isim, bugün hâlâ açık olan bir atölyenin kurucusu.",
   "Atölyenin duvarında 1926 tarihli bir fotoğraf: üç genç ve bir deve. Yüzler silinmiş.")
_b("Uşak", "Ege", "SAHTE HALI",
   "El dokuması sanılan Uşak halıları, 12 adet",
   "Kütahya porseleni, Uşak'taki otellere",
   360_000,
   "Halıların 8'i makine dokuması çıkar; kimse kandırmamıştır, Defne'nin acelesi yüzünden yanlış partiyi almışlardır.",
   "Defterde halı desenleri çizilmiş; bir desenin içine gizlenmiş harita: Gediz ovası ve bir bağ evi.",
   "Defne ilk kez ağlar: \"Benim hatam.\" Kerem defterin bir sayfasını gösterir: \"Sabri de aynı hatayı yapmış.\"")
_b("Manisa", "Ege", "ÜZÜM BAĞI",
   "Sultaniye çekirdeksiz kuru üzüm, 5 ton",
   "Makine halılarını dürüst etiketle ucuz satar, el halılarını değerinden",
   418_000,
   "Bağ sahibinin traktörü bozulur; hasadı kurtarmak için üçü de bir gün boyunca üzüm toplar.",
   "Halıdaki haritadaki bağ evinin bodrumunda, 1926 tarihli bir sandık ve sandıkta defterin kayıp sayfası.",
   "Kayıp sayfada bir isim: Sabri Kervancı. Altında: \"Emaneti İzmir'de Rıhtım'daki saate bıraktım.\"")
_b("İzmir", "Ege", "SAAT KULESİ",
   "Kemeraltı'ndan Ege otları ve baharat",
   "Manisa kuru üzümü, İzmir limanındaki ihracatçıya",
   486_000,
   "İhracatçı üzümü almak için belge ister; Defne gece boyunca evrak hazırlar, sabah son dakikada yetişir.",
   "Konak Saat Kulesi'nin kaidesinde, defterdeki çizimle aynı küçük deve kabartması.",
   "Kabartmanın altına kazınmış bir yön: \"Rüzgârın sakız kokduğu yere.\"")
_b("Çeşme (İzmir)", "Ege", "SAKIZ AĞACI",
   "Çeşme sakızı (damla sakızı), değerli ve az bulunur",
   "Ege otları ve baharat, Alaçatı'daki restoranlara",
   541_000,
   "Kaan restoranlarda 'tadım' yaparken fazla cömert davranır; bedava dağıtılan baharat kâra yansır.",
   "Defter sakız ağaçlarının arasında yüz yıllık bir ağacı tarif ediyor; ağacın gövdesinde oyulmuş harfler: S.K.",
   "Ağacın kovuğunda bir mektup: \"İncirler olgunlaşınca Aydın'da beni bekle.\"")
_b("Aydın", "Ege", "İNCİR HASADI",
   "Aydın'ın kuru inciri, 4 ton",
   "Çeşme sakızı, İzmir'deki tatlıcılara",
   603_000,
   "İncir hasadında yağmur başlar; kurutma alanı ıslanmadan önce köylülerle yarışa girerler.",
   "Mektubun devamı: Sabri ve iki ortağı burada yolu ikiye ayırmış; biri deniz yoluyla Bodrum'a, ikisi karadan gitmiş.",
   "Kerem defterin kenarında eski harflerle yazılmış bir not fark eder; okuyamazlar.")
_b("Bodrum (Muğla)", "Ege", "İKİNCİ MÜHÜR",
   "Bodrum mandalinası ve el yapımı sünger",
   "Aydın inciri, Bodrum'daki marinalara",
   672_000,
   "Kaan bir tekne turunda denize düşer; bu sırada denizin dibinde parlayan bir şey görür.",
   "Eski harfli not okunur: \"İkinci parça kalenin gölgesinde, suyun altında.\" Kaan'ın gördüğü şey ikinci mühür parçası.",
   "İki parça birleşince kervanın ikinci devesi tamamlanır. Arkasında: \"KAŞ\".")

# ── AKDENİZ (B15–B21) ───────────────────────────────────────────────────────
_b("Kaş (Antalya)", "Akdeniz", "BATAN TEKNE",
   "Kaş'tan zeytin ve keçiboynuzu pekmezi",
   "Bodrum süngeri — teknenin arızası yüzünden yarısı ıslak",
   640_000,
   "Mal taşıyan kiralık tekne arıza yapar, kasaların bir kısmı denize düşer. Ege'nin kârı eriyor.",
   "Defter Kaş'taki bir Likya kaya mezarını çizmiş; mezarın altında 1926'dan bir kuyumcu fişi.",
   "Fişteki isim: \"Antalya, Kaleiçi, Kuyumcu Nesim.\" Dükkân hâlâ açık mı?")
_b("Antalya", "Akdeniz", "KALEİÇİ",
   "Antalya'nın sera domatesi ve yaz meyveleri",
   "Keçiboynuzu pekmezi ve zeytin, otellere",
   735_000,
   "Otelin satın alma müdürü izne çıkar; üç gün beklemek zorunda kalırlar, meyveler olgunlaşmaya başlar.",
   "Kuyumcu Nesim'in torunu Sabri'nin 1926'da bıraktığı bir yüzüğü saklamış. Yüzüğün taşı: gül kurusu renginde.",
   "Torun: \"Dedem bu yüzüğü bir gün defterle gelecek birine ver demişti.\"")
_b("Isparta", "Akdeniz", "GÜL YAĞI",
   "Isparta gül yağı — gramı altından değerli",
   "Antalya meyvesi, Isparta'daki toptancıya",
   812_000,
   "Gül hasadı şafakta yapılır; Kaan uyuyakalır ve en değerli saatleri kaçırırlar.",
   "Yüzüğün içine kazınmış bir gül tarlasının adı; tarlada yüz yıllık bir taş kulübe.",
   "Kulübenin kapısında bir kilit; anahtar deliği deve şeklinde.")
_b("Alanya (Antalya)", "Akdeniz", "KIZIL KULE",
   "Alanya avokadosu ve muzu",
   "Gül yağı, Alanya'daki kozmetik dükkânlarına",
   890_000,
   "Gül yağının bir şişesi kırılır; bütün kamyonet aylarca gül kokacaktır.",
   "Kızıl Kule'nin tersanesinde, defterdeki gibi bir deve oyması; içinde kulübenin anahtarı.",
   "Kerem anahtarı çevirir… kulübe Isparta'da kaldı.")
_b("Mersin", "Akdeniz", "SOĞUK ZİNCİR",
   "Mersin narenciyesi, 8 ton",
   "Alanya avokadosu ve muzu, Mersin halinde",
   845_000,
   "Kiralık soğutuculu kamyonun soğutucusu yolda bozulur; narenciyenin bir kısmı ezilir.",
   "Kaan'ın ısrarıyla kulübeye geri dönülmez; defter \"Anahtarı Adana'da kullan\" diyor.",
   "Defne kasaya bakar: \"Bir milyona bu kadar yakınken…\"")
_b("Adana", "Akdeniz", "ACI BİBER",
   "Adana'nın pul biberi ve pamuklu kumaş",
   "Narenciyenin sağlam kalan kısmı, Adana'daki meyve suyu fabrikasına",
   940_000,
   "Kaan acı biber yarışmasına girer; kazanır ama iki gün sesi çıkmaz.",
   "Anahtar Taşköprü'nün yanındaki eski bir pamuk deposunu açar; içinde Sabri'nin 1926 hesap defteri.",
   "Hesap defterinin son satırı: \"Hatay'da her şeyi kaybettik.\"")
_b("Hatay", "Akdeniz", "ÜÇÜNCÜ MÜHÜR",
   "Hatay'ın künefe peyniri ve defne sabunu",
   "Adana pul biberi ve pamuklu kumaş",
   1_030_000,
   "Uzun Çarşı'da elektrik kesilir; peynirler bozulmadan dağıtmak için bütün mahalleyle seferber olurlar.",
   "Sabri'nin 'kaybettik' dediği şey para değil; Hatay'da bir aile mühür parçasını yüz yıldır saklıyor. Üçüncü parça.",
   "Kasa ilk kez 1.000.000 ₺'yi geçer. Ama mühür parçasının arkasında bir uyarı: \"Güneydoğu'da yol ikiye ayrılır.\"")

# ── GÜNEYDOĞU ANADOLU (B22–B28) ─────────────────────────────────────────────
_b("Gaziantep", "Güneydoğu Anadolu", "FISTIK",
   "Antep fıstığı, 3 ton",
   "Künefe peyniri ve defne sabunu, Gaziantep'teki tatlıcılara",
   1_120_000,
   "Baklavacı ustası fıstığın kalitesini beğenmez; Kaan ustayla bir baklava düellosu yapar.",
   "Defterde Bakırcılar Çarşısı'ndaki bir bakır ustası; ustanın atölyesinde deve şeklinde bir kalıp.",
   "Kalıbın içinde küçük bir kâğıt: \"Gül, karanlıkta açar.\"")
_b("Halfeti (Şanlıurfa)", "Güneydoğu Anadolu", "KARA GÜL",
   "Halfeti'nin kara gülü (fide ve kurusu)",
   "Antep fıstığı, Urfa'daki toptancıya",
   1_185_000,
   "Batık köyün yakınındaki tekne motoru durur; gece suyun ortasında kalırlar.",
   "Gece suyun ortasında Kerem defteri fenerle okur; kara gül çizimi su altındaki eski camiyi gösteriyor.",
   "Su altındaki minarenin tepesinde, fener ışığında parlayan bir deve oyması.")
_b("Şanlıurfa", "Güneydoğu Anadolu", "İSOT",
   "Urfa isotu ve Harran'dan pamuk",
   "Kara gül fideleri, Urfa'daki çiçekçilere",
   1_260_000,
   "Balıklıgöl'de Kaan balıklara simit atarken telefonu suya düşer; bütün müşteri listesi o telefondadır.",
   "Defter Harran'ın kümbet evlerinden birini işaret ediyor; içinde Sabri'nin el yazısıyla bir harita.",
   "Haritanın ortasında bir dağ: \"Taş başların gözüne bak.\"")
_b("Adıyaman", "Güneydoğu Anadolu", "NEMRUT SİSİ",
   "Adıyaman'ın kuru meyveleri",
   "Urfa isotu — Nemrut yolundaki nemden yarısı küflenmiş",
   1_210_000,
   "Nemrut yolunda sis ve yağmur; kamyonet iki gün mahsur kalır, isot nem çeker.",
   "Gün doğarken taş heykellerin gözlerinin baktığı yerde bir taş yığını; içinde Sabri'nin pusulası.",
   "Pusula kuzeyi göstermiyor. Diyarbakır'ı gösteriyor.")
_b("Diyarbakır", "Güneydoğu Anadolu", "KARPUZ",
   "Diyarbakır karpuzu ve el yapımı bakır",
   "Kuru meyve, Diyarbakır'daki kuruyemişçilere",
   1_305_000,
   "Kaan dev bir karpuzu taşırken düşürür; karpuz, ticaretin anlaşma masasına yayılır. Herkes güler, anlaşma imzalanır.",
   "Pusula Hasan Paşa Hanı'nda duruyor; hanın avlusunda Sabri'nin 1926'da konakladığı odanın numarası.",
   "Odanın duvarına yazılmış bir dize: \"Taşın sustuğu şehirde gümüş konuşur.\"")
_b("Mardin", "Güneydoğu Anadolu", "TAŞ ŞEHİR",
   "Mardin'in bıttım sabunu ve badem şekeri",
   "Diyarbakır karpuzu ve bakır, Mardin'deki butik otellere",
   1_390_000,
   "Taş merdivenlerde kamyonet giremez; bütün malları eşekle taşımak zorunda kalırlar.",
   "Defterdeki dize Midyat'ın telkari ustalarını işaret ediyor; Mardin'de bir ustanın torunu yolu tarif eder.",
   "Torun: \"Dedem o gün üç değil, dört kişi geldiklerini söylerdi.\"")
_b("Midyat (Mardin)", "Güneydoğu Anadolu", "DÖRDÜNCÜ MÜHÜR",
   "Midyat telkari gümüş takılar",
   "Bıttım sabunu ve badem şekeri",
   1_480_000,
   "Gümüş fiyatı bir gecede yükselir; Defne alımı bir gün öne çekerek büyük kâr yakalar.",
   "Telkari ustası, dedesinin Sabri için yaptığı gümüş deveyi saklamış: dördüncü mühür parçası.",
   "Dördüncü parçanın arkasında: \"Dördüncü yolcu Van'da kaldı.\"")

# ── DOĞU ANADOLU (B29–B35) ──────────────────────────────────────────────────
_b("Ahlat (Bitlis)", "Doğu Anadolu", "SELÇUKLU TAŞI",
   "Ahlat taşı işlemeleri ve Bitlis balı",
   "Telkari gümüş takılar, Ahlat'taki hediyelik dükkânlarına",
   1_525_000,
   "Van Gölü kıyısında kamyonetin lastiği patlar; yedek lastik de patlaktır.",
   "Selçuklu mezar taşlarından birinde deve kabartması ve bir isim: \"Rüstem, 1926\".",
   "Rüstem kim? Sabri'nin defterinde hiç geçmiyor.")
_b("Van", "Doğu Anadolu", "VAN KAHVALTISI",
   "Van otlu peyniri ve tereyağı",
   "Ahlat taşı işlemeleri ve Bitlis balı",
   1_610_000,
   "Kaan bir Van kedisine bağlanır ve kediyi bırakmak istemez; kedi bir kamyonet dolusu peynire saldırır.",
   "Rüstem'in torunları Van'da bir kahvaltı salonu işletiyor; dedeleri Sabri'nin dördüncü yolcusuymuş.",
   "Rüstem'in eski bir mektubu: \"Kar yağmadan dağı geçin, yoksa bahara kadar beklersiniz.\"")
_b("Doğubayazıt (Ağrı)", "Doğu Anadolu", "KAR FIRTINASI",
   "Ağrı'nın balı ve el dokuması kilim",
   "Van otlu peyniri — kar yüzünden teslimat gecikiyor",
   1_560_000,
   "Kar fırtınası; kamyonet İshak Paşa Sarayı yolunda mahsur kalır, peynirin bir kısmı satılamaz.",
   "Fırtınada sığındıkları İshak Paşa Sarayı'nda defterde çizilmiş bir pencere; pencerenin taşında bir rakam: 1926.",
   "Pencereden bakınca karların arasında Ağrı Dağı. Defterde: \"Dağın gölgesi Iğdır'a düşer.\"")
_b("Iğdır", "Doğu Anadolu", "KAYISI",
   "Iğdır'ın kayısısı (kuru) ve kavunu",
   "Ağrı balı ve kilim",
   1_650_000,
   "Kilimlerin biri yanlış ölçüde çıkar; müşteri iade eder, Kaan kilimi kamyonetin yatağı yapar.",
   "Rüstem'in mektubuna göre Sabri burada bir bavul bırakmış; bavul eski bir istasyonun emanetçisinde.",
   "Bavulun içinde tek şey var: bir tren bileti, Kars'a.")
_b("Kars", "Doğu Anadolu", "KAŞAR",
   "Kars kaşarı ve gravyer peyniri",
   "Iğdır kayısısı ve kavunu",
   1_760_000,
   "Gravyerin olgunlaşmasını beklemek gerekir; Defne kasanın bağlanmasından korkar ama riske girer.",
   "Tren bileti eski Kars garını işaret ediyor; gardaki bekleme salonunda Sabri'nin kazıdığı bir harita.",
   "Haritadaki göl donmuş. Defterde: \"Göl buz tutunca, buzun altına bak.\"")
_b("Çıldır (Ardahan)", "Doğu Anadolu", "BUZ GÖLÜ",
   "Ardahan kaz eti (füme) ve bal",
   "Kars kaşarı ve gravyer, Ardahan'daki marketlere",
   1_835_000,
   "Atlı kızakla göl üzerinde giderken buz çatlar; kızak suya gömülmeden kurtarılır.",
   "Buz balıkçılarının açtığı delikten, yüz yıllık bir zincirle bağlı bir kutu çıkar.",
   "Kutunun içinde bir oltu taşı tespih ve bir not: \"Erzurum'da tespihi tamamlayan ustayı bul.\"")
_b("Erzurum", "Doğu Anadolu", "BEŞİNCİ MÜHÜR",
   "Oltu taşı tespih ve takı",
   "Ardahan kaz eti ve bal",
   1_930_000,
   "Cağ kebabı yeme yarışmasında Kaan kendini aşar; iki gün çalışamaz, bütün yük Defne ve Kerem'e kalır.",
   "Tespih ustası tespihin imamesini açar: içinden beşinci mühür parçası çıkar.",
   "Beşinci parça Karadeniz'i gösteriyor; Kerem'in telefonu çalar: arayan, İstanbul'daki sahaf.")

# ── KARADENİZ (B36–B42) ─────────────────────────────────────────────────────
_b("Yusufeli (Artvin)", "Karadeniz", "DERE YOLU",
   "Artvin'in kestane balı",
   "Oltu taşı tespih ve takılar",
   1_990_000,
   "Dar dere yolunda heyelan; kamyoneti ters yöne 20 kilometre geri sürmek zorunda kalırlar.",
   "Sahafın telefonda söylediği: \"O defteri size ben seçtim. Ama sebebini Rize'de anlatacağım.\"",
   "Telefon kapanır. Kerem defterin son sayfalarının birbirine yapıştırıldığını fark eder.")
_b("Rize", "Karadeniz", "ÇAY BAHÇESİ",
   "Rize çayı, 6 ton (yaş çay işleme anlaşması)",
   "Kestane balı, Rize'deki kahvaltıcılara",
   2_080_000,
   "Yağmur durmuyor; çay toplama günleri ertelenir, kamyonet çamura saplanır.",
   "Sahaf Rize'de bir yaylada bekliyor; Sabri'nin kızının kızı olduğunu söyler.",
   "Sahaf: \"Defterin sonu yapıştırılmış, çünkü son sayfayı yüksek sesle okumaktan korktum.\"")
_b("Trabzon", "Karadeniz", "HAMSİ",
   "Trabzon hurması ve tereyağı",
   "Rize çayı — o hafta çay fiyatı aniden düşer",
   2_010_000,
   "Çay fiyatı piyasada düşer; elleri mecbur, zararına satarlar.",
   "Sümela'ya giden yolda yapışık sayfalar buharla açılır; Sabri'nin son yolculuğunun haritası.",
   "Haritada yolun sonu Kapadokya. Altında: \"Yedi parça olmadan kapı açılmaz.\"")
_b("Giresun", "Karadeniz", "FINDIK",
   "Giresun fındığı, 10 ton",
   "Trabzon hurması ve tereyağı",
   2_150_000,
   "Fındık harmanında Kaan fındıkları yanlış çuvallara doldurur; bütün gece yeniden ayıklanır.",
   "Giresun Adası'nda Sabri'nin çizdiği bir ağaç; ağacın kökünde boş bir mühür yuvası.",
   "Yuva boş. Biri altıncı parçayı daha önce almış.")
_b("Ordu", "Karadeniz", "BOZTEPE",
   "Ordu'nun fındık ezmesi ve pestil",
   "Giresun fındığı, Ordu'daki fabrikaya",
   2_240_000,
   "Fabrika fındığı nem ölçümü yüzünden reddetmek üzereyken Defne ikinci bir laboratuvar raporu getirir.",
   "Boztepe'deki yaşlı bir yamaç paraşütçüsü, parçayı 40 yıl önce adada bulup Sinop'taki ağabeyine verdiğini söyler.",
   "Sinop'taki ağabey yıllar önce ölmüş. Ama evi müze olmuş.")
_b("Sinop", "Karadeniz", "TERSANE",
   "Sinop'un el yapımı tekne maketleri ve nakışları",
   "Ordu fındık ezmesi ve pestil",
   2_300_000,
   "Müze kapalı; bir haftalık restorasyon var. Belediyeyi ikna etmek için bütün bir gün uğraşırlar.",
   "Müzenin vitrininde, 'kimliği bilinmeyen bronz parça' etiketiyle altıncı mühür parçası.",
   "Müze müdürü: \"Parçayı veririm. Ama Safranbolu'daki ailesi izin verirse.\"")
_b("Safranbolu (Karabük)", "Karadeniz", "ALTINCI MÜHÜR",
   "Safranbolu safranı ve lokumu",
   "Sinop tekne maketleri ve nakışları",
   2_390_000,
   "Safran hasadı tek gün sürer ve yağmur yağmaktadır; çiçekleri sabaha kadar elle toplarlar.",
   "Ailenin büyükannesi defteri görünce parçayı kendi verir: altıncı mühür parçası.",
   "Altı parça birleşince kervan tamamlanmak üzere; tek bir deve eksik. Arkasında: \"KAPI\".")

# ── İÇ ANADOLU (B43–B50) ────────────────────────────────────────────────────
_b("Beypazarı (Ankara)", "İç Anadolu", "TELKARİ",
   "Beypazarı'nın havucu, kurusu ve maden suyu",
   "Safranbolu safranı ve lokumu",
   2_450_000,
   "Kaan havuç lokumu tarifini yanlış anlar; bin kutu 'havuçlu lokum' siparişi yanlış basılır.",
   "Defterde Beypazarı'nın konak evlerinden birinin kapı tokmağı; tokmak deve şeklinde.",
   "Konağın sahibi: \"Sabri buradan geçtiğinde yanında üç değil, iki kişi vardı.\"")
_b("Eskişehir", "İç Anadolu", "LÜLETAŞI",
   "Eskişehir lületaşı işlemeleri ve met helvası",
   "Beypazarı ürünleri",
   2_520_000,
   "Lületaşı ustası malı vermeden önce üçünden de birer parça işlemelerini ister; Kaan'ın parçası kırılır.",
   "Odunpazarı'ndaki bir ahşap evde Sabri'nin 1926'dan bir fotoğrafı; fotoğrafın arkasında bir Ankara adresi.",
   "Kerem fotoğraftaki yüze uzun uzun bakar. Bir şey tanıdık geliyor.")
_b("Ankara", "İç Anadolu", "BÜYÜK SİPARİŞ",
   "Ankara tiftiği ve keçisi yününden ürünler",
   "Lületaşı ve met helvası — büyük bir zincir mağaza siparişi",
   2_430_000,
   "Zincir mağaza iflas eder; sipariş iptal, mal elde kalır. Sezonun en büyük zararı.",
   "Fotoğraftaki adres Ulus'ta eski bir han; hanın arşivinde Sabri'nin 1926'dan bir tapu kaydı.",
   "Tapu Kapadokya'da bir arazi için. Sahibi: Sabri Kervancı ve \"iki ortağı\".")
_b("Konya", "İç Anadolu", "BÜYÜK PAZAR",
   "Konya'nın buğdayı, unu ve etli ekmek",
   "Elde kalan lületaşı ve tiftik ürünleri, Konya'daki büyük pazarda",
   2_580_000,
   "Pazar sabahı kar yağar; tezgâh kurulamaz, ürünleri bir tarihi hanın avlusunda satarlar.",
   "Hanın avlusunda Sabri'nin defterde çizdiği sema eden bir derviş figürü; figürün eteğinde bir yol işareti.",
   "İşaret Ihlara Vadisi'ni gösteriyor. Defterde: \"Vadinin dibinde son harita.\"")
_b("Ihlara (Aksaray)", "İç Anadolu", "VADİ",
   "Aksaray'ın bal kabağı ve kuru meyvesi",
   "Konya unu ve buğdayı, Aksaray'daki fırınlara",
   2_640_000,
   "Vadide yürüyüş yolu kapalı; ip ve halatla, rehberle inmek zorunda kalırlar.",
   "Vadinin dibinde bir kaya kilisesinin duvarında Sabri'nin çizdiği son harita: Niğde'den geçen bir yol.",
   "Haritanın kenarında: \"Kervanın son devesi, elma ağacının altında uyur.\"")
_b("Niğde", "İç Anadolu", "ELMA BAHÇESİ",
   "Niğde elması ve patatesi",
   "Aksaray bal kabağı ve kuru meyvesi",
   2_710_000,
   "Bahçenin sahibi elma ağacını kazdırmak istemez; üç gün bahçede çalışıp güvenini kazanırlar.",
   "Yüz yıllık elma ağacının altında, kurşun bir kutunun içinde yedinci mühür parçası.",
   "Yedi parça tamam. Ama mühür kendiliğinden birleşmiyor; ortasında bir boşluk var.")
_b("Kayseri", "İç Anadolu", "PASTIRMA",
   "Kayseri pastırması ve sucuğu",
   "Niğde elması ve patatesi, Kayseri'deki toptancıya",
   2_860_000,
   "Pastırma kurutma sezonu kısa; bir tüccar daha iyi fiyat teklif eder, Defne eski müşteriye sadık kalır.",
   "Kayseri Bedesteni'ndeki yaşlı bir bakırcı, mührün ortasındaki boşluğa uyan küçük bir pim yapar: 1926'da da aynısını yapmış.",
   "Sahaf mesaj atar: \"Yarın sabah Derinkuyu. Ben de geliyorum.\"")
_b("Kapadokya (Nevşehir)", "İç Anadolu", "KERVANIN KAPISI",
   "Ürgüp'ün üzüm pekmezi ve Avanos'un el yapımı çömlekleri",
   "Kayseri pastırması ve sucuğu",
   2_980_000,
   "Yeraltı şehrinin en alt katına inmek için izin gerekir; izin kâğıdı son anda yetişir.",
   "Yedi parçalı mühür, Derinkuyu'nun en alt katındaki taş kapıyı açar: içinde Sabri'nin ikinci defteri ve 1926 tarihli bir fotoğraf.",
   "Fotoğrafta Sabri ve iki ortağı. Ortaklardan biri Kerem'in büyük dedesi. Sahaf: \"Bu defter size tesadüfen gelmedi.\"")
