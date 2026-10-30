# -*- coding: utf-8 -*-
"""Dedemin Defteri - Sezon 1 (Bölüm 4-100) planı üreticisi.

Kasa hesabı burada yapılır; tablo elle değil bu betikle üretilir ki
her bölümün kapanışı bir sonrakinin açılışı olsun ve kasa eksiye düşmesin.

Kullanım:  python3 sezon1.py  ->  sezon-1-plan.md dosyasını yeniden yazar.

Kurallar:
- Yol: iki il arası otobüs bileti (2026 tahmini) = 180 ₺ + km x 1,9 ₺, 50'ye yuvarlanır.
  Aynı ilde geçen ikinci bölümde yol 0'dır (şehir içi ulaşım masrafa dahildir).
- Satış: bir önceki ilde alınan malın bu ildeki satış tutarı = alış x çarpan (m).
  m < 1 ise zarar vardır (bozulan mal, sahte ürün, doymuş pazar...).
- Alış: kasadaki paranın belli bir oranı (f) ile yerel ürün alınır (100'e aşağı yuvarlanır);
  ama tek kişinin otobüsle taşıyıp satabileceği miktar sınırlı olduğu için alış, kapasite()
  üst sınırını geçemez.
"""
import math
import os

KASA_ACILIS_B4 = 5000  # Hüseyin Usta'nın verdiği sermaye


def bilet(km):
    if km == 0:
        return 0
    return int(round((180 + km * 1.9) / 50.0)) * 50


# (no, il, başlık, kısa hikâye, satılan, alınan, km, masraf, m, f, sabit_satış, sabit_alış, cliffhanger)
B = []


def E(no, il, baslik, hikaye, satilan, alinan, km, masraf, m=None, f=0.0,
      satis=None, alis=None, son=""):
    B.append(dict(no=no, il=il, baslik=baslik, hikaye=hikaye, satilan=satilan,
                  alinan=alinan, km=km, masraf=masraf, m=m, f=f,
                  satis=satis, alis=alis, son=son))


# ---------------------------------------------------------------- KAYSERİ
E(4, "Kayseri", "Ahilik Dersi",
  "Kerem, dedesinin defterindeki ilk adresi bulur: Kayseri Kapalı Çarşı'da (1859) dedesinin can dostu Hüseyin Usta. "
  "Usta ona ahiliğin üç kuralını öğretir: 'Eline, beline, diline sahip ol.' Sermaye sınavı: 5.000 ₺ verir ama şart koşar; "
  "kasa sıfıra düşmeyecek, yalan söylenmeyecek, her kuruş deftere yazılacak. Kasa ilk kez ekranda belirir.",
  "—", "—", 0, 0, satis=0, alis=0,
  son="Çarşının kapısında takım elbiseli bir adam belirir: Selim Karahan. Defter için 1 milyon ₺ teklif eder ve ekler: 'O mühür aslında benim babamındı.'")

E(5, "Kayseri", "İlk Pastırma",
  "Kerem teklifi reddeder. Londra'dan kalan son sneaker çiftini Bit Pazarı'nda satıp sermayeye ekler. Hüseyin Usta onu "
  "pastırma ustasına götürür: çemenin sırrı, Erciyes rüzgârında kuruyan et ve pazarlıkta 'malın kusurunu önce sen söyle' dersi. "
  "Usta, mühürlü sayfanın ancak 81 ili dolaşıp dönerse açılacağını söyler.",
  "Londra'dan kalan son sneaker çifti", "Kayseri pastırması ve sucuğu", 0, 0, satis=2500, alis=6000,
  son="Nevşehir otobüsünde Kerem'in iki koltuk arkasına oturan adam telefonda fısıldar: 'Evet Selim Bey, yola çıktı.'")

# ---------------------------------------------------------------- İÇ ANADOLU - AKDENİZ
E(6, "Nevşehir", "Balonlar ve Pastırma",
  "Göreme'de peribacalarının arasındaki butik otellere pastırma satar. Gün doğumunda balon fotoğrafı çeken belgeselci Elif Sarı ile tanışır. "
  "Avanos'ta Kızılırmak kilinden çömlek yapan ustadan Hititlerden beri süren çömlekçiliği öğrenir.",
  "Kayseri pastırması ve sucuğu", "Avanos çömleği", 80, 900, m=1.8, f=0.75,
  son="Elif'in çektiği balon fotoğrafını büyütünce Kerem kalakalır: arka planda otobüsteki adam, dürbünle onu izliyor.")

E(7, "Niğde", "Gümüşler'in Sırrı",
  "Otobüs şoförü Yaşar Kaptan yolda Kerem'e Niğde'yi anlatır. Kerem çömlekleri Niğde çarşısında satar, Gümüşler Manastırı'nın kaya freskolarını görür. "
  "Defterdeki öğüt: 'Elmayı dalından değil, bahçıvanın elinden al.' Niğde elmasını doğrudan üreticiden alır.",
  "Avanos çömleği", "Niğde elması", 85, 850, m=1.7, f=0.75,
  son="Yaşar Kaptan defterin kapağındaki el yazısını görünce frene basar: 'Bu yazıyı tanıyorum… Bunu nereden buldun?'")

E(8, "Aksaray", "Sultanhanı'nda Bir Gece",
  "Yaşar sadece 'Eski bir yolcuydu' deyip konuyu kapatır. Kerem elmaları Aksaray pazarında satar. Defter onu Sultanhanı Kervansarayı'na yollar: "
  "'Kervan nerede konaklarsa tüccar orada öğrenir.' Taşpınar halısı dokuyan kadınlardan küçük halılar alır.",
  "Niğde elması", "Taşpınar halısı (küçük boy)", 120, 900, m=1.6, f=0.75,
  son="Gece kervansarayın avlusunda uyandığında çantası açık, defterin mührü bir bıçakla kazınmış ama kırılamamış.")

E(9, "Konya", "Sabır Pazarı (1)",
  "Halılar Konya Bedesteni'nde zor satılır; Kerem acele edip fiyat kırar, az kâr eder. Mevlana Müzesi'nde Osmanlıca uzmanı Dr. Leyla Tan ile tanışır. "
  "Leyla defterin kenar notlarını okur: hepsi 1979 tarihli.",
  "Taşpınar halısı", "—", 150, 1100, m=1.25, f=0.0,
  son="Leyla bir sayfada durur, yüzü değişir: 'Kerem… bu bir borç listesi. Tam 81 isim var.'")

E(10, "Konya", "Şeb-i Arus Değil Ama (2)",
  "Kerem bir sema gösterisinde 'dönmek için önce durmayı bilmek' öğüdünü anlar. Etli ekmek fırınında bir gün çalışıp yevmiye alır. "
  "Mevlana şekeri alır. Tatlı dilli bir adam ona 'yarı fiyatına' Karaman peyniri satmak ister; Kerem reddeder.",
  "Yan iş: etli ekmek fırınında yevmiye", "Mevlana şekeri", 0, 1000, satis=1000, f=0.7,
  son="Adam giderken masaya bir kartvizit bırakır: 'Necmi — Karahan Lojistik.'")

E(11, "Karaman", "Türkçe'nin Başkenti",
  "Karamanoğlu Mehmet Bey'in 1277 fermanını ('Bugünden sonra divanda, dergâhta… Türkçe'den başka dil konuşulmayacak') öğrenir, Yunus Emre Camii'ni ziyaret eder. "
  "Mevlana şekerini satıp mağarada olgunlaşan Divle Obruk peyniri alır.",
  "Mevlana şekeri", "Divle Obruk peyniri", 115, 900, m=1.45, f=0.75,
  son="Mağaranın yaşlı sahibi zarf uzatır: 'Hacı Rıza bana borçlu değildi evlat… ben ona borçluydum.'")

E(12, "Mersin", "Peynir Eridi",
  "Otobüsün bagaj soğutucusu yolda 'arızalanır'; peynirlerin bir kısmı bozulur. İLK ZARAR. Kerem kalanını Tarsus'ta, Kleopatra Kapısı yakınındaki "
  "lokantalara satar. Kızkalesi'ne bakarken öğüdü okur: 'Zarar eden değil, zararından ders almayan batar.' Cezeriye alır.",
  "Divle Obruk peyniri (bir kısmı bozuldu)", "Mersin cezeriyesi", 205, 1000, m=0.7, f=0.7,
  son="Karaman'daki zarfı açar: yırtık bir fotoğrafın yarısı. 1979, bir kamyonun önünde genç dedesi… yanındaki adamın yüzü kopmuş.")

E(13, "Adana", "Taşköprü'de Pazarlık (1)",
  "Kerem cezeriyeleri Roma'dan kalma ve hâlâ kullanılan Taşköprü'nün dibindeki tatlıcılara satar. Adana kebabı ustası ona "
  "'zırhla kıyılmış et gibi, iş de elle yapılır' der. Bu bölüm sadece satış yapar, alım ertesi güne kalır.",
  "Mersin cezeriyesi", "—", 70, 1200, m=1.4, f=0.0,
  son="Otel lobisinde Selim Karahan bekliyor: 'Bir ay içinde o defter benim olacak. İstersen kolay yoldan, istersen zor yoldan.'")

E(14, "Adana", "Şalgam ve Portakal (2)",
  "Kerem, Adana Lezzet Festivali'nde bir şalgam tezgâhında çalışıp yevmiye alır. Kozan'dan portakal alır. "
  "Elif Sarı yeniden belirir: o da '81 İl' belgeseli çekiyormuş, yolculuğu kaydetmek ister.",
  "Yan iş: lezzet festivalinde tezgâh yevmiyesi", "Kozan portakalı", 0, 1100, satis=1200, f=0.75,
  son="Kerem kabul eder. Elif kamerayı açtığı anda telefonuna 'S.K.' imzalı bir mesaj düşer; ekranı hızla kapatır.")

E(15, "Osmaniye", "Karatepe'nin Aslanları",
  "Portakallar Osmaniye halinde satılır. Karatepe-Aslantaş Açık Hava Müzesi'nde iki dilli Azatiwada yazıtını görür; "
  "Leyla telefonda heyecanlanır: defterin kenarındaki işaretler de iki dilli bir şifre olabilir. Osmaniye yer fıstığı alır.",
  "Kozan portakalı", "Osmaniye yer fıstığı", 90, 900, m=1.4, f=0.75,
  son="Leyla: 'Karatepe'deki gibi… sayfaların altında ikinci bir metin var. Ve ilk kelime bir soyadı: KARAHAN.'")

E(16, "Hatay", "Yeniden Ayağa Kalkan Şehir (1)",
  "2023 depreminden sonra yeniden inşa edilen Antakya'da Uzun Çarşı'nın açılan dükkânlarına yer fıstığı satar. "
  "Esnafın dayanışmasını görür; kazancının bir kısmıyla bir fırının yeniden açılışına destek olur (masrafa dahil).",
  "Osmaniye yer fıstığı", "—", 125, 2200, m=1.45, f=0.0,
  son="Restore edilen Habib-i Neccar Camii'nin bağışçı listesinde bir isim gözüne çarpar: 'Hacı Rıza Aksoy — 1981.'")

E(17, "Hatay", "Defnenin Kokusu (2)",
  "Hatay Arkeoloji Müzesi'nin mozaiklerini gezer, künefe ustasının yanında yarım gün çalışır. Harbiye'den defne sabunu alır.",
  "Yan iş: künefeci yanında yarım gün", "Defne sabunu", 0, 1100, satis=800, f=0.75,
  son="Gece numarası gizli bir mesaj gelir: 'Kilis'e gitme. Seni bekliyorlar.'")

E(18, "Kilis", "Zeytinin Sözü",
  "Uyarıya rağmen Kilis'e gelir; Kilis Mevlevihanesi'nin avlusunda defne sabunlarını satar. Zeytinyağı üreticisi ona "
  "'yağ suyun üstüne çıkar, doğru da' der. Kilis zeytinyağı alır.",
  "Defne sabunu", "Kilis zeytinyağı", 175, 950, m=1.4, f=0.75,
  son="Mesajı atan çıkar: Yaşar Kaptan. 'Gaziantep'teki toptancıların hepsine Karahan'dan telefon geldi. Kimse senden mal almayacak.'")

E(19, "Gaziantep", "Boykot (1)",
  "Toptancılar gerçekten kapıyı kapatır. Kerem, Nazlı Abla'nın kadın kooperatifine gider; kooperatif zeytinyağını adil fiyata alır. "
  "Zeugma Mozaik Müzesi'nde 'Çingene Kızı'nın gözlerine bakarken 'Her mozaik tek tek taşlardan olur' öğüdünü okur.",
  "Kilis zeytinyağı", "—", 65, 1100, m=1.3, f=0.0,
  son="Nazlı fotoğrafın yarısını görünce susar: 'Bu fotoğrafın öbür yarısı… bizim kooperatifin duvarında asılı.'")

E(20, "Gaziantep", "Fıstık Hasadı (2)",
  "Fotoğrafın diğer yarısında dedenin yanındaki genç adam görünür ama yüzü güneşten yanmış. Bakırcılar Çarşısı'nda dövülen bakırın sesiyle "
  "Kerem, Nazlı'nın tanıştırdığı üreticiden Antep fıstığı alır, kooperatifin baklava atölyesinde yardım edip yevmiye alır.",
  "Yan iş: kooperatifin baklava atölyesi", "Antep fıstığı", 0, 1000, satis=1000, f=0.8,
  son="Leyla arar: '81 isimlik listenin birinci sırasında ne yazıyor biliyor musun? Cevdet Karahan.'")

E(21, "Kahramanmaraş", "Dövme Dondurma",
  "Antep fıstığını dövme dondurma ustalarına satar; keçi sütü ve salep ile dövülen dondurmanın sırrını öğrenir. "
  "Maraş işi sırma işlemeli bir bohça görür. Maraş pul biberi alır.",
  "Antep fıstığı", "Maraş pul biberi", 80, 950, m=1.35, f=0.75,
  son="Annesi Ayşe arar, sesi titriyor: 'Kerem, eve avukat mektubu geldi. Dedenin çarşıdaki dükkânı için dava açılmış. Davacı: Karahan.'")

E(22, "Malatya", "Arslantepe'nin Kılıçları",
  "Pul biberi Malatya çarşısında satar. UNESCO listesindeki Arslantepe Höyüğü'nde dünyanın bilinen en eski kılıçlarını görür. "
  "Kayısı bahçesinde, ağaçtan değil kurutma sergisinden alım yapmanın farkını öğrenir. Gün kurusu kayısı alır.",
  "Maraş pul biberi", "Malatya kayısısı (gün kurusu)", 225, 950, m=1.35, f=0.75,
  son="Avukat mektubunun ikinci sayfası: 'Hacı Rıza Aksoy 1979'da ortaklık kasasını alıp kaçmıştır.'")

E(23, "Adıyaman", "Nemrut'ta Gün Doğumu",
  "Nemrut Dağı'nın dev heykellerinin başında gün doğumunu bekler, defterdeki öğüdü okur: 'Taş heykel yıkılır, verilen söz kalır.' "
  "Kayısıları Kahta'da satar, Besni üzümü alır.",
  "Malatya kayısısı", "Besni üzümü (kuru)", 150, 1000, m=1.3, f=0.75,
  son="Elif'in telefonunda yanlışlıkla açık kalan galeri: defterin sayfalarının tek tek fotoğrafları… 'Gönderildi' işaretiyle.")

E(24, "Şanlıurfa", "Göbeklitepe: Her Şeyin Başı (1)",
  "Göbeklitepe'de 12.000 yıl önce insanların ilk kez bir araya gelip bir şey inşa ettiğini öğrenir: 'Ticaret de bir arada durmaktır.' "
  "Kuru üzümleri Urfa çarşısında satar ama satış beklentinin altında kalır: biri onun adına sahte ürün satıyormuş.",
  "Besni üzümü", "—", 110, 1100, m=1.2, f=0.0,
  son="Çarşıda bir tezgâhta 'Kerem'in Kayseri Pastırması' etiketli sahte paketler… satıcının arkasındaki adam: Necmi.")

E(25, "Şanlıurfa", "Sıra Gecesi (2)",
  "Kerem, Balıklıgöl'de sahte ürün satıcısına kamera önünde gerçeği anlatır; esnaf ona sahip çıkar. Bir sıra gecesinde Yaşar Kaptan "
  "bağlamasını alıp türkü söyler, Kerem gece için yevmiye alır. Harran'ın kümbet evlerinden geçip isot alır.",
  "Yan iş: sıra gecesinde servis", "Urfa isotu", 0, 1000, satis=900, f=0.8,
  son="Türkü bitince Yaşar yavaşça söyler: '1979 kışında o kervanda ben de vardım, Kerem. Ama şimdi değil… zamanı gelince.'")

E(26, "Mardin", "Taş Şehrin Ustaları",
  "Isotu Mardin'in taş evleri arasındaki lokantalara satar. Deyrulzafaran Manastırı'nı gezer, Midyat'ta gümüş telleri örerek yapılan "
  "telkari sanatını öğrenir. Telkari takılar alır.",
  "Urfa isotu", "Midyat telkari gümüş takı", 185, 1050, m=1.35, f=0.75,
  son="Telkari ustası çekmeceden küçük bir gümüş anahtar yarısı çıkarır: 'Deden 1985'te yaptırdı. Torunum gelirse ver, dedi.'")

E(27, "Diyarbakır", "Surların İçinde (1)",
  "Kerem telkari takıları tarihi Hasan Paşa Hanı'ndaki kuyumculara satar; handa kahvaltı ederken hanların ticaretteki yerini öğrenir. "
  "Diyarbakır Surları ve Hevsel Bahçeleri'nde yürür.",
  "Midyat telkari takı", "—", 95, 1200, m=1.35, f=0.0,
  son="Leyla Diyarbakır'a gelir, elinde notlar: '81 isim alacaklı değil, Kerem. Deden onlara BORÇLUYMUŞ. Ve rotan… onun borç ödeme rotası.'")

E(28, "Diyarbakır", "On Gözlü Köprü (2)",
  "Dicle üzerindeki On Gözlü Köprü'de Kerem dedesinin her ile neden gittiğini anlar. Bir ciğerci dükkânında akşam servisinde çalışır. "
  "Burma kadayıf alır.",
  "Yan iş: ciğerci dükkânında akşam servisi", "Diyarbakır burma kadayıfı", 0, 1100, satis=900, f=0.75,
  son="Telefonu titrer: Selim Karahan'ın paylaştığı video viral olmuş. Başlık: 'Aksoy ailesi dolandırıcıdır.'")

E(29, "Batman", "Hasankeyf'in Taşınan Anıtları",
  "Kadayıfları satar, yeni yerine taşınan Zeynel Bey Türbesi'ni görür: 'Bazı şeyler korumak için yerinden oynatılır.' "
  "Batman'ın coğrafi işaretli içli köftesi gılorik alır, dondurulmuş olarak paketletir.",
  "Diyarbakır burma kadayıfı", "Batman gıloriği (dondurulmuş içli köfte)", 100, 1000, m=1.3, f=0.7,
  son="Siirt otobüsünde bagaja bakan Kerem görür: soğutma kutusunun fişi çekilmiş. Yanına bir kartvizit bırakılmış.")

E(30, "Siirt", "Büryan ve Fıstık",
  "İKİNCİ ZARAR: gıloriklerin yarısı çözülüp bozulmuştur. Kerem kalanını ucuza satar. Tillo'da İbrahim Hakkı'nın astronomi mirasını ve "
  "güneş ışığının yılda iki kez türbeye düştüğü olayı öğrenir. Büryan kebabı yer, Siirt fıstığı alır.",
  "Batman gıloriği (yarısı bozuldu)", "Siirt fıstığı", 90, 1000, m=0.6, f=0.75,
  son="Leyla mührün kenarındaki minik yazıyı çözer: 'Son sayfa 81. ilde değil… 82. adımda açılır.'")

E(31, "Şırnak", "Cudi'nin Gölgesinde",
  "Siirt fıstığını Cizre çarşısında satar. Cudi Dağı'na dair Nuh tufanı rivayetini, Kırmızı Medrese'yi ve Mem û Zîn aşk hikâyesini dinler. "
  "Kenger kahvesi alır.",
  "Siirt fıstığı", "Kenger kahvesi", 95, 1000, m=1.35, f=0.75,
  son="Yaşar Kaptan Hakkari otobüsünde Kerem'e soluk bir zarf uzatır: '1979'dan… Ama içini Van'da aç.'")

E(32, "Hakkari", "Cilo'nun Eteğinde",
  "Kenger kahvesini satar; Cilo-Sat dağlarının gölgesinde, 14. yüzyıldan Meydan Medresesi'ni gezer. Kadın dokumacılardan "
  "dünyaca bilinen Hakkari kilimlerinden küçük boy alır.",
  "Kenger kahvesi", "Hakkari kilimi", 180, 1000, m=1.35, f=0.75,
  son="Van yolunda tipi bastırır; otobüs Güzeldere geçidinde durur. Kerem'in cebindeki zarf ıslanmaya başlar.")

E(33, "Van", "Van Kahvaltısı (1)",
  "Tipi diner. Kerem kilimleri Van çarşısında satar, meşhur Van kahvaltısında kırk çeşidi tadar, Van Kedisi Evi'nde tek gözü mavi tek gözü "
  "kehribar kedileri görür. Zarfı açar: 1979'dan bir otobüs bileti, 'Kayseri-Sivas'.",
  "Hakkari kilimi", "—", 200, 1300, m=1.4, f=0.0,
  son="Elif'in telefonunu tutan Kerem ekranda okur: 'S.K.: Defterin son sayfalarını da çek. Ödemen yattı.'")

E(34, "Van", "Akdamar'a Yolculuk (2)",
  "Kerem soğuk bir sessizlik içinde tekneyle Akdamar Kilisesi'ne gider; Van Kalesi'nde Urartu'nun Tuşpa'sını görür. Elif 'Açıklayabilirim' der "
  "ama Kerem dinlemez. Otlu peynir alır, bir kahvaltı salonunda sabah servisinde yevmiye alır.",
  "Yan iş: kahvaltı salonunda sabah servisi", "Van otlu peyniri", 0, 1200, satis=900, f=0.75,
  son="Sabah Elif'in odası boş. Masada bir not: 'Her şeyi düzelteceğim. Bana güven.'")

E(35, "Bitlis", "Ahlat'ın Mezar Taşları",
  "Otlu peyniri satar. Ahlat Selçuklu Meydan Mezarlığı'nın oymalı taşlarını, Nemrut Krater Gölü'nü ve Şerefname'yi öğrenir. "
  "Ahlat taşından oyma hediyelikler alır.",
  "Van otlu peyniri", "Ahlat taşı oyma hediyelik", 165, 1000, m=1.35, f=0.75,
  son="Taş ustası: 'Deden her yıl gelip bir borç kapatırdı. Son gelişinde dedi ki: Bir gün torunum son borcu kapatacak.'")

E(36, "Muş", "Malazgirt'in Kapısı",
  "Ahlat taşı hediyelikleri satar. 1071 Malazgirt Meydan Muharebesi'nin Anadolu'nun kapısını açtığını, endemik Muş lalesini öğrenir. "
  "Bir kadın kooperatifinden lale motifli el örgüsü yün çorap alır.",
  "Ahlat taşı hediyelik", "Muş el örgüsü yün çorap (lale motifli)", 90, 950, m=1.35, f=0.75,
  son="Avukattan mesaj: 'Duruşma 60 gün sonra Ankara'da. Dedenin masum olduğunu gösteren belge yoksa dükkânı kaybedersiniz.'")

E(37, "Bingöl", "Yüzen Adalar",
  "Yün çorapları soğuk yaylada kolayca satar. Solhan'daki yüzen adaları görür. Bir satıcı ona çok ucuza 'Bingöl balı' teklif eder; "
  "Kerem defterdeki öğüdü uygular: 'Balı kaşıktan akıt; ip gibi akmıyorsa alma.' Sahte çıkar, gerçek Bingöl balını üreticiden alır.",
  "Muş yün çorap", "Bingöl balı", 120, 950, m=1.4, f=0.75,
  son="Sahte balcının dükkânının önünde Necmi'nin arabası. Necmi camı indirip gülümser ve gaza basar.")

E(38, "Elazığ", "Harput'un Sesi",
  "Gerçek Bingöl balını satar. Harput Kalesi'nde Harput ezgilerini dinler, Hazar Gölü kıyısında dinlenir. Cevizli orcik alır.",
  "Bingöl balı", "Elazığ orciği", 140, 1000, m=1.35, f=0.75,
  son="Necmi karşısına oturur: 'Defteri ver, Selim Bey davayı geri çeksin. Yoksa annenin evi de gider.'")

E(39, "Tunceli", "Munzur Gözeleri",
  "Orcikleri satar. Munzur Vadisi'nde kayaların arasından fışkıran Munzur gözelerinin başında düşünür. Endemik Tunceli dağ sarımsağı alır.",
  "Elazığ orciği", "Tunceli dağ sarımsağı", 130, 950, m=1.35, f=0.75,
  son="Elif bir kayanın üstünde onu bekliyor: 'Evet, Selim bana para verdi. Ama ona hiçbir şey göndermedim. Gönderdiklerim sahte sayfalardı.'")

E(40, "Erzincan", "Kemaliye'nin Taş Yolu",
  "Sarımsakları satar. Kemaliye'nin Taş Yolu'ndan Karanlık Kanyon'a bakar, Girlevik Şelalesi'ne gider. Erzincan tulum peyniri alır. Elif yeniden ekipte.",
  "Tunceli dağ sarımsağı", "Erzincan tulum peyniri", 135, 1000, m=1.35, f=0.75,
  son="Selim'den mesaj: 'Sahte sayfalar için Elif'e teşekkür et. Ama asıl kozum başka: Babam Cevdet Karahan yaşıyor.'")

E(41, "Erzurum", "Dadaşlar Diyarı (1)",
  "Tulum peynirini Erzurum çarşısında satar. Çifte Minareli Medrese'yi gezer, cağ kebabı ustasından 'ateşi eşit yakmak' dersini alır.",
  "Erzincan tulum peyniri", "—", 190, 1300, m=1.35, f=0.0,
  son="Leyla listenin son satırını çözer: '81. isim… Hüseyin Usta.'")

E(42, "Erzurum", "Oltu Taşı (2)",
  "Kerem, Hüseyin Usta'yı arar; usta konuşmak istemez. Bar oyunlarını izler, bir oltu taşı atölyesinde tesbih ipliği takarak yevmiye alır. Oltu taşı tesbih alır.",
  "Yan iş: oltu taşı atölyesi", "Oltu taşı tesbih", 0, 1200, satis=900, f=0.75,
  son="Hüseyin Usta sonunda konuşur: 'Ben de o gece oradaydım, Kerem. Ama yemin ettim.'")

E(43, "Ağrı", "İshak Paşa Sarayı",
  "Tesbihleri Doğubayazıt'ta satar. Ağrı Dağı'nın eteğindeki İshak Paşa Sarayı'nı gezer, abdigör köftesi yer. "
  "Doğubayazıt'ta el dokuması yün kilim alır.",
  "Oltu taşı tesbih", "Doğubayazıt el dokuması kilim", 185, 1000, m=1.35, f=0.75,
  son="Yaşar arar: 'Iğdır'da sana çok iyi bir teklif yapacaklar. Sakın kabul etme.' Hat kesilir.")

E(44, "Iğdır", "Aras'ın Kayısısı",
  "Kilimleri satar. Ağrı Dağı'nın en güzel göründüğü ovada, Aras Kuş Cenneti'nde kuşları izler. Coğrafi işaretli Iğdır kayısısını alır; "
  "Malatya kayısısıyla farkını öğrenir.",
  "Doğubayazıt kilimi", "Iğdır kayısısı", 145, 950, m=1.35, f=0.75,
  son="Kars'tan bir toptancı arar: bütün kayısıyı iki katı fiyata almak istiyor. 'Ödeme çekle, yarın Kars'ta.'")

E(45, "Kars", "Ani'nin Bin Bir Kilisesi",
  "Kerem teklifi kabul eder, kayısıları çek karşılığı verir: kasaya nakit girmez. Ani Harabeleri'ni ve Kars'ın Baltık mimarisi binalarını gezer. "
  "Çekin parasına güvenip kasadaki nakitle Kars gravyeri alır.",
  "Iğdır kayısısı (çekle satıldı, nakit girmedi)", "Kars gravyeri", 140, 1000, satis=0, f=0.8,
  son="Banka gişesi: 'Çek karşılıksız. Keşideci firma: Karahan Gıda.'")

E(46, "Ardahan", "Çıldır'da Buz Balığı",
  "ÜÇÜNCÜ ZARAR: kayısıların parası yok. Kerem gravyerleri satar, Çıldır Gölü'nde atlı kızakçılara ve buzda balık tutanlara yardım edip "
  "yevmiye alır. Ardahan kazı (kurutulmuş kaz) alır.",
  "Kars gravyeri (+ buz balıkçılığında yevmiye)", "Ardahan kazı", 95, 900, m=1.7, f=0.75,
  son="Yaşar Kaptan: 'Cevdet Karahan Sivas'ta yaşıyor. Gerçeği sadece o söyleyebilir. Ama önce anahtarın öbür yarısını bul: Trabzon'da, hasır bilezik ustasında.'")

# ---------------------------------------------------------------- KARADENİZ
E(47, "Artvin", "Macahel'in Balı",
  "Kurutulmuş kazı satar. UNESCO biyosfer alanı Macahel'de ve Şavşat Karagöl'de dolaşır. Kafkas arısının Macahel balını alır.",
  "Ardahan kazı", "Macahel balı", 115, 1000, m=1.4, f=0.75,
  son="Elif bir dosya gönderir: Selim'in 'Karahan Gıda' adına karşılıksız çek yazdırdığı mesajlar. 'Bu senin delilin.'")

E(48, "Rize", "Çay Bahçesinde",
  "Balı satar. Ayder Yaylası'nda, Zil Kale'de ve çay bahçelerinde; çay toplayan kadınların 'iki yaprak bir tomurcuk' kuralını öğrenir. Rize çayı alır.",
  "Macahel balı", "Rize çayı", 160, 1100, m=1.35, f=0.75,
  son="Annesi arıyor: 'Hüseyin Usta kalp krizi geçirdi, hastanede.'")

E(49, "Trabzon", "Sümela'ya Tırmanış (1)",
  "Rize çayını Trabzon'da satar ama burası da çay ülkesi: kâr çok düşük, 'malı ait olduğu yerden uzağa sat' dersi. "
  "Sümela Manastırı'na tırmanır, Uzungöl'de kemençe ve horon izler.",
  "Rize çayı", "—", 80, 1400, m=1.1, f=0.0,
  son="Annesi tekrar arar: 'Hüseyin Usta'nın dükkânına girmişler. Mühür yüzüğü çalınmış!'")

E(50, "Trabzon", "Hasır Bilezik (2)",
  "Kerem, defterin işaret ettiği hasır bilezik ustasını bulur; ustadan ince gümüş tellerle hasır örgüsünü öğrenir ve bir gün atölyede çalışır. "
  "Usta, anahtarın ikinci yarısını verir. Akçaabat köftesi yer, gümüş hasır bilezik alır.",
  "Yan iş: hasır bilezik atölyesi", "Trabzon gümüş hasır bilezik", 0, 1300, satis=1000, f=0.8,
  son="Usta: 'Geçen hafta biri bu anahtarı almak için kapıya dayandı. Kartvizitinde Karahan yazıyordu.'")

E(51, "Bayburt", "Dede Korkut'un Hikâyeleri",
  "Gümüş bilezikleri satar. Bayburt Kalesi'nin dibinde Dede Korkut Şenlikleri'nde ozanları dinler: 'Dedem de bir Dede Korkut'tu, hikâyesini bana bıraktı.' "
  "Bayburt tel helvası alır.",
  "Trabzon gümüş hasır bilezik", "Bayburt tel helvası", 180, 950, m=1.3, f=0.75,
  son="Pansiyon kapısında Necmi, parmağında Hüseyin Usta'nın yüzüğüyle: 'Bunu mu arıyorsun?'")

E(52, "Gümüşhane", "Pestil Yolu",
  "Tel helvayı satar. Karaca Mağarası'nı ve Santa harabelerini gezer. Necmi şart koyar: iki anahtar yarısını getirirse yüzüğü verecek. "
  "Kerem pestil ve köme alır.",
  "Bayburt tel helvası", "Gümüşhane pestili ve kömesi", 75, 950, m=1.35, f=0.75,
  son="Necmi: 'Yarın Giresun Adası'nın karşısında. Tek gel. Polise gidersen yüzüğü denize atarım.'")

E(53, "Giresun", "Kirazın Adası",
  "Pestilleri satar. Kirazın Avrupa'ya buradan, Kerasus'tan gittiğini öğrenir. Elif ve Yaşar ile Aksu kıyısında tuzak kurarlar; yüzük geri alınır. "
  "Giresun tombul fındığı alır.",
  "Gümüşhane pestili", "Giresun tombul fındığı", 150, 1000, m=1.35, f=0.75,
  son="Kaçarken Necmi bağırır: 'Deden Selim'in babasını mahvetti! Sayfayı açınca görürsün!'")

E(54, "Ordu", "Fındık Diyarına Fındık",
  "DÖRDÜNCÜ ZARAR: Kerem fındığı Ordu'ya getirdiğinde fiyatların düştüğünü görür; Ordu zaten Türkiye'nin fındık başkenti. Maliyetin altında satar. "
  "Boztepe'ye teleferikle çıkar, Yason Burnu'nda düşünür. Fındık ezmesi alır.",
  "Giresun fındığı (zararına)", "Ordu fındık ezmesi", 45, 1000, m=0.85, f=0.7,
  son="Leyla arar: 'Yeni bir tarih çözdüm: 14 Şubat 1979. Kayseri-Sivas yolu. Bir kaza raporu var.'")

E(55, "Samsun", "Bandırma'nın İzinde",
  "Fındık ezmesini satar. 19 Mayıs 1919'u, Bandırma Vapuru Müzesi'ni ve Amisos Tepesi'ni gezer: 'Her büyük yol küçük bir vapurla başlar.' Bafra nokulu alır.",
  "Ordu fındık ezmesi", "Bafra nokulu", 160, 1200, m=1.35, f=0.75,
  son="Selim'den mesaj: 'Sinop'ta konuşalım. Sadece ikimiz. Gerçeği duymak istiyorsan gel.'")

E(56, "Sinop", "Tarihi Cezaevinde Buluşma",
  "Nokulları satar. Sinop Tarihi Cezaevi'nin avlusunda Selim ile buluşur. Selim, babasından duyduğu hikâyeyi anlatır: Rıza kervanın kasasıyla kaçmış. "
  "Hamsilos koyunda düşünen Kerem, Sinop'un ünlü gemi maketlerinden alır.",
  "Bafra nokulu", "Sinop gemi maketi", 160, 1100, m=1.35, f=0.75,
  son="Selim bir gazete kupürü uzatır: 15 Şubat 1979 - 'Kervan kasası kayıp, ortak ortadan kayboldu.'")

E(57, "Kastamonu", "Siyezin Hafızası",
  "Gemi maketlerini satar. Ahşap Mahmut Bey Camii'ni ve Nasrullah Camii'ni gezer, çekme helva yapımını izler. Göbeklitepe zamanından beri ekilen "
  "siyez buğdayının bulgurunu alır. Leyla, Kastamonu'daki eski bir banka şubesinin arşivine ulaşır.",
  "Sinop gemi maketi", "Kastamonu siyez bulguru", 175, 1050, m=1.35, f=0.75,
  son="Arşiv: Rıza'nın 1980-1995 arasında 81 ayrı kişiye yaptığı ödeme dekontları. Kaçan biri neden borç ödesin?")

E(58, "Karabük", "Safranbolu Konakları",
  "Siyez bulgurunu satar. UNESCO listesindeki Safranbolu konaklarını, Cinci Hanı'nı ve safran tarlalarını gezer. Safranbolu lokumu alır.",
  "Kastamonu siyez bulguru", "Safranbolu lokumu", 115, 1200, m=1.35, f=0.75,
  son="Leyla dekontlardan birini büyütür: alıcı 'Cevdet Karahan', 1985. 'Deden kaçmamış… Cevdet'e para göndermiş!'")

E(59, "Bartın", "Amasra'nın Ustaları",
  "Lokumları satar. Amasra'nın Ceneviz kalesini, Amasra salatasını ve kuşaktan kuşağa geçen ahşap oymacılığını görür. Amasra ahşap el işleri alır.",
  "Safranbolu lokumu", "Amasra ahşap el işleri", 85, 1100, m=1.35, f=0.75,
  son="Elif'e tehdit mesajı gelir: 'Belgeseli yayınlarsan kariyerin biter.' Elif ilk kez korkuyor.")

E(60, "Zonguldak", "Kara Elmasın Şehri",
  "Ahşap işleri satar. Kömürü 1829'da bulan Uzun Mehmet'in hikâyesini, Gökgöl Mağarası'nı, maden şehrinin dayanışmasını öğrenir. Devrek bastonu alır.",
  "Amasra ahşap el işleri", "Devrek bastonu", 90, 1100, m=1.35, f=0.75,
  son="Emekli bir madenci, Rıza'nın 1979'da ona emanet ettiği mühürlü bir mektubu getirir: 'Kerem Aksoy'a.'")

E(61, "Düzce", "Çerkez Peyniri",
  "Bastonları satar. Konuralp Antik Kenti'ni gezer, Çerkez kültürünü ve sofra geleneğini tanır. Çerkez peyniri alır. Mektubu okur.",
  "Devrek bastonu", "Düzce Çerkez peyniri", 110, 1100, m=1.35, f=0.75,
  son="Mektup: 'Cevdet'in kızı ağır hastaydı. O gece ne olduğunu kimse bilmemeli. Bilen tek kişi o kamyonun çırağı.'")

E(62, "Bolu", "Mengen'in Aşçıları",
  "Peyniri satar. Yedigöller ve Abant'ı gezer, Mengen Aşçılar Festivali'nde usta aşçılardan 'tencerenin içine iyi niyet koy' dersini alır. "
  "Mudurnu'nun tavuk ürünlerinden vakumlu paket alır.",
  "Düzce Çerkez peyniri", "Mudurnu tavuğu (vakumlu)", 45, 1150, m=1.35, f=0.75,
  son="Kerem mektuptaki 'çırak' kelimesini Yaşar'a sorar. Yaşar telefonu yüzüne kapatır.")

E(63, "Sakarya", "Sapanca'da Mola",
  "Tavuk ürünlerini ıslama köfteciler ve lokantalara satar. 1921 Sakarya Meydan Muharebesi'ni, Sapanca Gölü'nü öğrenir. Geyve ayvası alır.",
  "Mudurnu tavuğu", "Geyve ayvası", 115, 1200, m=1.3, f=0.75,
  son="Dikiz aynasında üç gündür aynı beyaz kamyonet. Şoför koltuğunda Necmi.")

E(64, "Kocaeli", "Pişmaniye",
  "Ayvaları satar. SEKA Kâğıt Müzesi'nde kâğıdın serüvenini ve Kartepe'yi görür. İzmit pişmaniyesi alır.",
  "Geyve ayvası", "İzmit pişmaniyesi", 40, 1300, m=1.35, f=0.75,
  son="İzmit otogarında kalabalıkta biri çarpar. Kerem çantasına bakar: DEFTER YOK.")

E(65, "Yalova", "Defterim Nerede?",
  "Panik içinde pişmaniyeleri satar. Termal kaplıcalar ve Atatürk'ün Yürüyen Köşkü… ama aklı defterde. Elif, Necmi'nin konumunu "
  "sosyal medya paylaşımlarından bulur. Yalova'nın ünlü kesme çiçeklerinden alır.",
  "İzmit pişmaniyesi", "Yalova kesme çiçeği", 65, 1200, m=1.3, f=0.75,
  son="Elif ekranı çevirir: 'Defter İstanbul'da. Galata'da, Karahan ofisinde.'")

E(66, "İstanbul", "Kapalıçarşı Kovalamacası (1)",
  "Çiçeklerin bir kısmı yolda solar; Eminönü'nde kalanını satar. Yaşar'ın minibüsüyle Galata'ya giderler. Necmi defterle kaçar; 1461'den beri "
  "açık olan Kapalıçarşı'nın 60'tan fazla sokağında kovalamaca. Kerem defteri geri alır.",
  "Yalova kesme çiçeği (bir kısmı soldu)", "—", 100, 2500, m=1.1, f=0.0,
  son="Mühür sağlam. Selim kapıda belirir: 'Açmadım. Çünkü içinde ne yazdığını zaten biliyorum.'")

E(67, "İstanbul", "Galata'dan Bakış (2)",
  "Galata Kulesi'nde Selim babasının hikâyesini anlatır: Cevdet her şeyi kaybetmiş, Selim'i yoksullukta büyütmüş. Kerem, Mısır Çarşısı'nda "
  "bir baharatçıda çalışıp yevmiye alır; UNESCO listesindeki Türk kahvesi kültürünü öğrenip Türk kahvesi alır.",
  "Yan iş: Mısır Çarşısı'nda baharatçı yevmiyesi", "Türk kahvesi", 0, 2500, satis=1500, f=0.75,
  son="Selim: 'Ankara'da, mahkemede görüşürüz. Sayfayı o güne kadar açarsan, dava senin aleyhine delil olur.'")

# ---------------------------------------------------------------- TRAKYA - MARMARA - EGE
E(68, "Tekirdağ", "Köfte ve Helva",
  "Türk kahvesini satar. Macar prensi Rákóczi'nin sürgün evini (Rákóczi Müzesi) ve Namık Kemal'in evini gezer. Tekirdağ peynir helvası alır.",
  "Türk kahvesi", "Tekirdağ peynir helvası", 135, 1300, m=1.35, f=0.75,
  son="Leyla: 'Mahkeme 1978 tarihli orijinal ortaklık senedini isteyecek. Bence o senet… mühürlü sayfanın içinde.'")

E(69, "Kırklareli", "Longoz'un Sessizliği",
  "Peynir helvasını satar. İğneada Longoz Ormanları'nda ve Dupnisa Mağarası'nda sessizliği dinler. Coğrafi işaretli hardaliye alır.",
  "Tekirdağ peynir helvası", "Kırklareli hardaliyesi", 120, 1200, m=1.35, f=0.75,
  son="Kerem mührün üstüne bıçağı koyar… Telefon çalar, Hüseyin Usta: 'Sakın! Ahi mührü yolda açılmaz.'")

E(70, "Edirne", "Selimiye'nin Gölgesinde",
  "Hardaliyeyi satar. Mimar Sinan'ın 'ustalık eserim' dediği Selimiye'nin kubbesi altında 'sabır ustalıktır' öğüdünü okur, Kırkpınar'ın tarihini öğrenir. "
  "Edirne badem ezmesi alır.",
  "Kırklareli hardaliyesi", "Edirne badem ezmesi", 60, 1300, m=1.35, f=0.75,
  son="Elif belgeselin fragmanını yayınlar. Sabah telefonunda 3.000 sipariş mesajı… ve Selim'den tek kelime: 'Akıllıca.'")

E(71, "Çanakkale", "1915'in Hatırası",
  "Badem ezmesi siparişle hızla satılır. Çanakkale Şehitliği'nde saygı duruşu, Truva Antik Kenti ve 1915 Çanakkale Köprüsü. Ezine peyniri alır.",
  "Edirne badem ezmesi", "Ezine peyniri", 215, 1300, m=1.45, f=0.8,
  son="İzmir'den 'Ege Gıda' adlı bir firma dev bir sipariş teklif eder. Elif fısıldar: 'Bu firmanın adresi… boş bir arsa.'")

E(72, "Balıkesir", "Kaz Dağları",
  "Ege Gıda teklifini reddeder, Ezine peynirini doğrudan şarküteri ve kahvaltıcılara satar. Kaz Dağları'nı ve Manyas Kuş Cenneti'ni gezer. Höşmerim alır.",
  "Ezine peyniri", "Balıkesir höşmerimi", 195, 1300, m=1.35, f=0.75,
  son="Bursa'dan bir mesaj: 'Koza Han'da dedenin eski ortağı seni bekliyor.' İmza yok.")

E(73, "Bursa", "Koza Han'da İpek (1)",
  "Höşmerimi satar. 1491'den beri ipek ticaretinin merkezi olan Koza Han'a gelir. Ulu Cami'yi ve Cumalıkızık'ı gezer. Mesajı atan yaşlı bir ipekçi çıkar.",
  "Balıkesir höşmerimi", "—", 150, 1600, m=1.35, f=0.0,
  son="İpekçi: 'Deden ile Cevdet'i ben tanıştırdım. O gece Cevdet'in kızı ameliyattaydı… para Cevdet'teydi, Kerem. Rıza'da değil.'")

E(74, "Bursa", "Karagöz ile Hacivat (2)",
  "UNESCO listesindeki Karagöz-Hacivat gölge oyununu izler: 'Biri sözünü tutar, biri tutmaz; iki dost yine de birbirini bırakmaz.' "
  "İskender'ini yer, ipekçinin dükkânında bir gün çalışır, Bursa ipeği eşarp alır.",
  "Yan iş: Koza Han'da ipekçi yevmiyesi", "Bursa ipeği eşarp", 0, 1500, satis=1200, f=0.75,
  son="Kerem Selim'i arar: 'Baban sana yalan söylemiş olabilir.' Selim: 'Benim babam yalan söylemez!' Hat kesilir.")

E(75, "Bilecik", "Söğüt'te Bir Çınar",
  "İpek eşarpları satar. Söğüt'te Ertuğrul Gazi Türbesi'ni ve Osmanlı'nın kuruluş hikâyesini öğrenir: 'Büyük devlet küçük bir obadan doğar.' "
  "Bozüyük'ün ünlü seramiklerinden alır.",
  "Bursa ipeği eşarp", "Bozüyük seramiği", 95, 1200, m=1.35, f=0.75,
  son="Avukat: 'Karşı taraf yeni bir tanık buldu. Adı: Yaşar Demirci.' Kerem donar: Yaşar Kaptan.")

E(76, "Eskişehir", "Lületaşı",
  "Seramikleri satar. Odunpazarı'nın renkli evlerini gezer, çibörek yer, dünyada nadir bulunan lületaşının oymacılığını öğrenir. Lületaşı alır.",
  "Bozüyük seramiği", "Eskişehir lületaşı", 80, 1300, m=1.35, f=0.75,
  son="Yaşar sonunda yüz yüze konuşur: 'Selim'in avukatı beni çağırdı. Ne söyleyeceğime mahkemede karar vereceğim.'")

E(77, "Kütahya", "Çininin Mavisi",
  "Lületaşını satar. Kütahya çini atölyesinde mavinin sırrını, Aizanoi'nin Zeus Tapınağı'nı ve Evliya Çelebi'nin evini görür. Kütahya çinisi alır.",
  "Eskişehir lületaşı", "Kütahya çinisi", 80, 1200, m=1.35, f=0.75,
  son="Çini ustası bir karonun arkasını çevirir: Aksoy ve Karahan ailelerinin mühürleri yan yana. Tarih: 1978.")

E(78, "Uşak", "Karun Hazinesi",
  "Çinileri satar. Yurt dışına kaçırılıp yıllar sonra geri dönen Karun (Lidya) Hazinesi'ni Uşak Müzesi'nde görür: 'Asıl hazine, döndüğü yere aittir.' "
  "Uşak halısından seccade boy alır.",
  "Kütahya çinisi", "Uşak halısı (seccade boy)", 140, 1200, m=1.35, f=0.75,
  son="Elif'in annesinden mesaj: 'Kızım İzmir'e gelin. Babam sizin dedenizi tanıyormuş.'")

E(79, "Manisa", "Mesir Macunu",
  "Uşak halılarını satar. UNESCO listesindeki Mesir Macunu Festivali'nin hikâyesini (Hafsa Sultan) ve Spil Dağı'nı öğrenir. Mesir macunu alır.",
  "Uşak halısı", "Manisa mesir macunu", 190, 1200, m=1.35, f=0.75,
  son="İzmir otobüsünde Kerem'in telefonuna ihbar düşer: 'Kemeraltı'nda senin adınla sahte mesir satılıyor.'")

E(80, "İzmir", "Kemeraltı (1)",
  "BEŞİNCİ ZARAR: Necmi'nin adamları Kemeraltı'nda sahte ürünle piyasayı bozmuştur; Kerem mesiri düşük fiyata satar. Saat Kulesi'nde boyoz-gevrek, "
  "Elif'in ailesiyle akşam yemeği.",
  "Manisa mesir macunu (sahte ürün yüzünden ucuza)", "—", 40, 1800, m=1.05, f=0.0,
  son="Elif'in dedesi eski bir kasetçalar getirir: 'Rıza bunu bana 1990'da bıraktı. Torunu gelirse dinlesin.'")

E(81, "İzmir", "Efes'te Bir Gün (2)",
  "Kasette dedenin sesi: 'Kerem, bir gün birine kızarsan önce onun yükünü taşı.' Efes Antik Kenti'nde Celsus Kütüphanesi'ni gezer. "
  "Görece'deki Nazarköy'de cam fırınında bir gün çalışır, nazar boncuğu alır.",
  "Yan iş: Nazarköy cam atölyesi", "Nazarköy nazar boncuğu", 0, 1700, satis=1200, f=0.75,
  son="Kasetin son saniyesi: 'Cevdet'e kızma. O gece onun yerinde olsam ben de aynısını yapardım.'")

E(82, "Aydın", "İncir Bahçeleri",
  "Nazar boncuklarını satar. Afrodisias Antik Kenti'nde heykeltıraş okulunu öğrenir. Coğrafi işaretli Aydın kuru incirini alır.",
  "Nazarköy nazar boncuğu", "Aydın kuru inciri", 125, 1300, m=1.35, f=0.75,
  son="Leyla: 'Mahkeme duruşmayı öne aldı. 20 gün kaldı. Ve Selim tedbir kararı istiyor: defter mahkemeye teslim edilsin.'")

E(83, "Muğla", "Bodrum'un Mandalinası",
  "İncirleri satar. Bodrum Kalesi, Halikarnas Mozolesi'nin izleri, Kaunos kaya mezarları ve beyaz badanalı Muğla evleri. Bodrum mandalinası alır.",
  "Aydın kuru inciri", "Bodrum mandalinası", 100, 1500, m=1.35, f=0.75,
  son="Yaşar mesaj atar: 'Mahkemeden önce Sivas'a, Cevdet'in yanına git. Ben de orada olacağım.'")

E(84, "Denizli", "Pamukkale Beyazı",
  "Mandalinaları satar. Pamukkale travertenlerinde ve Hierapolis'te yürür, Denizli horozunun hikâyesini dinler. Buldan bezi alır.",
  "Bodrum mandalinası", "Buldan bezi", 140, 1300, m=1.35, f=0.75,
  son="Buldan dokumacısının tezgâhında iki ipliği birbirine bağlayan Kerem fikrini değiştirir: 'Davayı kazanmak istemiyorum. Bitirmek istiyorum.'")

# ---------------------------------------------------------------- GÖLLER - AKDENİZ - İÇ ANADOLU
E(85, "Burdur", "Salda'nın Beyazı",
  "Buldan bezini satar. Bembeyaz kıyılarıyla Salda Gölü'nü ve Sagalassos Antik Kenti'ni gezer. Burdur ceviz ezmesi alır.",
  "Buldan bezi", "Burdur ceviz ezmesi", 150, 1300, m=1.35, f=0.75,
  son="Necmi son kez karşısına çıkar ama bu kez yalnız ve yorgun: 'Selim beni kovdu. Sana bir şey söylemem lazım.'")

E(86, "Antalya", "Kaleiçi (1)",
  "Ceviz ezmesini satar. Kaleiçi'nin daracık sokaklarında, Hadrian Kapısı'nda Necmi'yi dinler: Selim aslında defteri yok etmek istiyormuş, "
  "çünkü babası ona sayfayı asla açtırmamasını söylemiş.",
  "Burdur ceviz ezmesi", "—", 120, 2000, m=1.35, f=0.0,
  son="Necmi: 'Cevdet Bey ölmeden önce oğluna gerçeği söylemek istiyor ama Selim dinlemiyor. Sen dinletebilirsin.'")

E(87, "Antalya", "Aspendos'ta Konser (2)",
  "2.000 yıllık Aspendos Antik Tiyatrosu'nda bir konserde sahne arkasında çalışıp yevmiye alır. Piyaz yer, Alanya muzu alır. Necmi ekibe katılmak ister.",
  "Yan iş: Aspendos'ta sahne ekibi", "Alanya muzu", 0, 1900, satis=1500, f=0.75,
  son="Fırtına çıkar; Isparta yolu kapanır. Muzlar sarı sarı, saatler daralıyor.")

E(88, "Isparta", "Gülün Şehri",
  "ALTINCI ZARAR: yol açılana kadar muzların bir kısmı fazla olgunlaşır. Kerem kalanını satar. Gül hasadında, sabah çiyi kalkmadan gül toplanmasını, "
  "Eğirdir Gölü'nü görür. Isparta gül yağı ve gül suyu alır.",
  "Alanya muzu (bir kısmı aşırı olgunlaştı)", "Isparta gül yağı ve gül suyu", 130, 1300, m=0.9, f=0.75,
  son="Hüseyin Usta hastaneden çıkmış: 'Kerem, Sivas'a geldiğinde ben de orada olacağım. Yüzüğü getir.'")

E(89, "Afyonkarahisar", "Kocatepe",
  "Gül ürünlerini satar. Büyük Taarruz'un başladığı Kocatepe'ye, Afyon Kalesi'ne ve Frig Vadisi'ne gider. Afyon sucuğu alır (Kayseri sucuğuyla dostça kıyaslar).",
  "Isparta gül yağı ve gül suyu", "Afyon sucuğu", 170, 1300, m=1.4, f=0.75,
  son="Ankara'ya giden otobüste Selim'in avukatı arar: 'Defteri yarın mahkemeye teslim etmezseniz tutuklama talep edeceğiz.'")

E(90, "Ankara", "Anıtkabir ve Mahkeme (1)",
  "Sucukları satar. Sabah Anıtkabir, öğlen mahkeme. Avukat ücreti masrafa eklenir. Hâkim, Elif'in getirdiği karşılıksız çek delilini dosyaya alır; "
  "duruşmayı mühürlü sayfanın ehil bir kişi huzurunda açılmasına kadar erteler.",
  "Afyon sucuğu", "—", 255, 4500, m=1.35, f=0.0,
  son="Mahkeme çıkışında Selim yanına gelir: 'Babam seni görmek istiyor. Sivas'ta. Ama yalnız gel.'")

E(91, "Ankara", "Beypazarı (2)",
  "Anadolu Medeniyetleri Müzesi'nde Leyla, 1979 kaza tutanağını arşivden bulur: Rıza hakkında hiçbir suçlama yok. Hamamönü'nde bir tarihi konakta "
  "çalışıp yevmiye alır. Beypazarı kurusu alır.",
  "Yan iş: Hamamönü'nde konak yevmiyesi", "Beypazarı kurusu", 0, 2000, satis=1500, f=0.75,
  son="Tutanağın altında tanık imzası: 'Yaşar Demirci, 15 yaşında, kamyon çırağı.'")

E(92, "Kırıkkale", "Kızılırmak Kıyısında",
  "Beypazarı kurusunu satar. Hasandede'yi ve Kızılırmak kıyısını gezer, Keskin'in bağlarından üzüm pekmezi alır. Yaşar'ı bekler.",
  "Beypazarı kurusu", "Keskin üzüm pekmezi", 75, 1200, m=1.35, f=0.75,
  son="Yaşar gelir, gözleri dolu: 'Kırk yedi yıl sustum. Sivas'ta Cevdet'in yüzüne karşı konuşacağım.'")

E(93, "Çankırı", "Tuz Mağarası",
  "Pekmezi satar. Hititlerden beri işletilen Çankırı Tuz Mağarası'nda 'tuz gibi dürüst ol, az olsun öz olsun' öğüdünü okur. Kaya tuzu alır.",
  "Keskin üzüm pekmezi", "Çankırı kaya tuzu", 105, 1200, m=1.35, f=0.75,
  son="Kerem'in telefonuna fotoğraf düşer: Selim, hastanede babasının başında. Altında tek kelime: 'Acele et.'")

E(94, "Çorum", "Hattuşa'nın Anlaşması",
  "Kaya tuzunu satar. Hitit başkenti Hattuşa'da tarihin bilinen ilk yazılı barış antlaşması Kadeş'in hikâyesini öğrenir: 'Barış da bir ticarettir; iki taraf da kazanır.' "
  "Çorum leblebisi alır.",
  "Çankırı kaya tuzu", "Çorum leblebisi", 160, 1200, m=1.4, f=0.75,
  son="Selim arar: 'Babam taburcu oldu, Sivas'a götürüyorum. Seninle Tokat'ta değil, Divriği'de buluşmak istiyor.'")

E(95, "Amasya", "Ferhat ile Şirin",
  "Leblebiyi satar. Yeşilırmak kıyısında Yalıboyu evleri, kayalara oyulmuş Kral Kaya Mezarları ve Ferhat'ın dağı delip su getirdiği efsane. "
  "Amasya misket elması alır.",
  "Çorum leblebisi", "Amasya misket elması", 95, 1200, m=1.35, f=0.75,
  son="Hüseyin Usta yüzüğü takar: 'Sivas'tan sonra Kayseri. Ve son borç, Kerem… benim borcum.'")

E(96, "Tokat", "Yazmanın Deseni",
  "Elmaları satar. Gök Medrese'yi ve Ballıca Mağarası'nı gezer, tahta kalıplarla yapılan Tokat yazmasında her rengin ayrı basıldığını öğrenir. Tokat yazması alır.",
  "Amasya misket elması", "Tokat yazması", 115, 1200, m=1.35, f=0.75,
  son="Selim arar, sesi ilk kez kırık: 'Babamın durumu kötüleşti. Yarın sabah Divriği'de değilsen belki onu hiç göremezsin.'")

E(97, "Sivas", "Divriği'nin Kapısı",
  "Yazmaları satar. UNESCO listesindeki Divriği Ulu Camii ve Darüşşifası'nın taş kapısında Cevdet Karahan ile karşılaşır. Sivas Kongresi binasını gezer. "
  "El yapımı Sivas bıçağı alır.",
  "Tokat yazması", "Sivas bıçağı (el yapımı)", 105, 1300, m=1.35, f=0.75,
  son="Cevdet titreyen sesle: 'Rıza beni bırakmadı, Kerem. Ben onu yarı yolda bıraktım.' O anda Selim kapıda belirir.")

E(98, "Yozgat", "Çamlık'ta İtiraf",
  "Bıçakları satar. Türkiye'nin ilk milli parkı Yozgat Çamlığı'nda Yaşar, Cevdet ve Selim'in önünde 1979 gecesini anlatır: kızının ameliyatı için "
  "kasayı alan Cevdet, suçu üstlenen Rıza. Kerem arabaşı yer, Yozgat tarhanası alır.",
  "Sivas bıçağı", "Yozgat tarhanası", 225, 1300, m=1.35, f=0.75,
  son="Selim babasına döner: 'O kız… benim ablam mıydı?' Cevdet başını sallar. Selim arabaya biner ve kaybolur.")

E(99, "Kırşehir", "Ahi Evran",
  "Tarhanayı satar. Ahiliğin piri Ahi Evran'ın türbesinde Hüseyin Usta ile buluşur, Neşet Ertaş'ın bozkır türkülerini dinler. "
  "Hediye olarak götürmek için Kırşehir'in Mucur el dokuması halısını alır.",
  "Yozgat tarhanası", "Mucur el dokuması halı", 110, 1300, m=1.35, f=0.75,
  son="Hüseyin Usta: 'Yarın Kayseri'de 82. adım.' Kerem'in telefonu çalar, Selim: 'Ben çarşıdayım. Dükkânın önünde.'")

E(100, "Kayseri", "82. Adım: Mühür Açılıyor (FİNAL)",
  "Kerem, Mucur halısını Kapalı Çarşı'da satar ve 82. adımı atar: Hüseyin Usta'ya 5.000 ₺ sermayeyi geri öder (masrafa dahil), 81. borç kapanır. "
  "Selim, Cevdet, Yaşar, Elif, Leyla, Nazlı ve annesi önünde Hüseyin yüzüğüyle mührü kırar, Kerem iki gümüş anahtar yarısıyla kilidi açar. "
  "Sayfada 1978 tarihli ortaklık senedi var: dükkânın tapusu baştan beri yarı yarıya, Aksoy & Karahan adına. Kerem kendi yarısını Selim'le paylaşıp dükkânı "
  "'81 İl Yol Hanı' kooperatifine çevirir.",
  "Mucur el dokuması halı", "—", 130, 1500, m=1.35, f=0.0,
  son="Son satırın altında, sayfanın arkasında dedenin yeni bir haritası: 'İpek Yolu - Semerkant. Sermaye: Kasandaki her şey.' 2. SEZON.")

# Bölüm 100'de Hüseyin Usta'ya iade edilen sermaye (masrafa eklenir)
SERMAYE_IADE = 5000


def kapasite(no):
    """Kerem'in tek seferde taşıyıp satabileceği mal (alış tutarı) üst sınırı.
    Otobüsle seyahat eden tek kişi için gerçekçi tutmak adına yavaş büyür."""
    return 6000 + (no - 6) * 300


def r50(x):
    return int(round(x / 50.0)) * 50


def hesapla():
    kasa = KASA_ACILIS_B4
    stok = 0  # elde satılmayı bekleyen malın alış tutarı
    rows = []
    for b in B:
        acilis = kasa
        yol = bilet(b["km"])
        masraf = b["masraf"] + (SERMAYE_IADE if b["no"] == 100 else 0)
        if b["satis"] is not None:
            satis = b["satis"]
        else:
            satis = r50(stok * b["m"])
            stok = 0
        kalan = acilis - yol - masraf + satis
        assert kalan >= 0, "Bölüm %d: satış sonrası kasa eksi (%d)" % (b["no"], kalan)
        if b["alis"] is not None:
            alis = b["alis"]
        else:
            alis = int(math.floor(min(kalan * b["f"], kapasite(b["no"])) / 100.0)) * 100
        if alis:
            stok = alis
        kapanis = kalan - alis
        assert kapanis >= 0, "Bölüm %d: kasa eksi" % b["no"]
        rows.append(dict(b, acilis=acilis, yol=yol, masraf_t=masraf, satis_t=satis,
                         alis_t=alis, kapanis=kapanis))
        kasa = kapanis
    return rows


def tl(x):
    return "{:,}".format(x).replace(",", ".") + " ₺"


def kontrol(rows):
    nos = [r["no"] for r in rows]
    assert nos == list(range(4, 101)), "Bölüm numaraları eksik/fazla"
    iller = [r["il"] for r in rows if 6 <= r["no"] <= 99]
    sayim = {}
    for il in iller:
        sayim[il] = sayim.get(il, 0) + 1
    assert "Kayseri" not in sayim
    assert len(sayim) == 80, "80 il olmalı, %d var" % len(sayim)
    iki = sorted(k for k, v in sayim.items() if v == 2)
    assert len(iki) == 14, "14 il iki bölüm olmalı: %s" % iki
    assert all(v in (1, 2) for v in sayim.values())
    # ardışıklık: kapanış = sonraki açılış
    for a, b in zip(rows, rows[1:]):
        assert a["kapanis"] == b["acilis"]
    # aynı il ikili bölümlerin art arda olması
    for il in iki:
        idx = [r["no"] for r in rows if r["il"] == il]
        assert idx[1] == idx[0] + 1, il
    return iki


def yaz(rows, iki):
    out = []
    w = out.append
    w("## C) Bölüm Bölüm Plan (4–100)\n")
    w("> Kasa hesabı `sezon1.py` ile üretilmiştir: **Kapanış = Açılış − Yol − Masraf + Satış − Alış**. "
      "Her kapanış bir sonraki bölümün açılışıdır. Yol = iki il arası otobüs bileti (2026 tahmini, ~180 ₺ + km × 1,9 ₺); "
      "aynı ilde geçen ikinci bölümde yol 0 ₺'dir (şehir içi ulaşım masrafa dahil). Masraf = konaklama + yemek "
      "(B90'da avukat ücreti, B100'de Hüseyin Usta'ya iade edilen 5.000 ₺ sermaye dahil). "
      "Alış tutarı, Kerem'in otobüsle taşıyıp satabileceği yükle sınırlıdır; kalan parayı dava ve kara gün için kasada tutar. "
      "Videonun üstünde gösterilecek değer **KASA: (kapanış) ₺**'dir; sahne içinde açılıştan kapanışa sayaç animasyonu önerilir.\n")
    w("> İki bölüm süren 14 il: " + ", ".join(iki) + ".\n")
    w("| Bölüm | İl | Başlık | Kısa hikâye (kültür öğesi dahil) | Satılan ürün | Alınan ürün | Açılış kasa | Yol | Masraf | Satış | Alış | Kapanış kasa | Bölüm sonu (cliffhanger) |")
    w("|---|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---|")
    for r in rows:
        cells = [str(r["no"]), r["il"], r["baslik"], r["hikaye"], r["satilan"], r["alinan"],
                 tl(r["acilis"]), tl(r["yol"]), tl(r["masraf_t"]), tl(r["satis_t"]), tl(r["alis_t"]),
                 "**" + tl(r["kapanis"]) + "**", r["son"]]
        w("| " + " | ".join(c.replace("|", "/") for c in cells) + " |")
    w("")
    return "\n".join(out)


if __name__ == "__main__":
    rows = hesapla()
    iki = kontrol(rows)
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "ust-bolum.md"), encoding="utf-8") as fh:
        ust = fh.read()
    tablo = yaz(rows, iki)
    with open(os.path.join(here, "sezon-1-plan.md"), "w", encoding="utf-8") as fh:
        fh.write(ust.rstrip() + "\n\n" + tablo)
    # kısa özet
    zararlar = [r["no"] for r in rows if r["m"] is not None and r["m"] < 1]
    print("Bölüm sayısı:", len(rows))
    print("Başlangıç:", tl(rows[0]["acilis"]), " Final kapanış:", tl(rows[-1]["kapanis"]))
    print("En düşük kapanış:", min((r["kapanis"], r["no"]) for r in rows))
    print("Zarar bölümleri (m<1):", zararlar, "+ B45 çek")
