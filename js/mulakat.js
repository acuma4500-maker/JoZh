// ── MÜLAKAT HAZIRLIK v4 — Sorular + Simülasyon + Rehber
// Kaynak: MSB Mülakat Kitabı PDF, Mülakat Soruları PDF, Rehber PDF, Bilgi Yıldızı PDF

// ════════════════════════════════════════════════════════════
// SORU BANKASI
// ════════════════════════════════════════════════════════════
var ORNEK_SORULAR = [
  // ── ATATÜRK İLKELERİ & İNKILAP TARİHİ ──
  { kat:"ataturk", soru:"Atatürk'ün 6 ilkesi nelerdir?", cevap:"Cumhuriyetçilik, Milliyetçilik, Halkçılık, Devletçilik, Laiklik, İnkılapçılık." },
  { kat:"ataturk", soru:"Cumhuriyetçilik ilkesini açıklayın.", cevap:"Ulusal egemenlik ve cumhuriyet yönetimi anlayışının benimsenmesini, halkın yönetime etkin biçimde katılmasını hedefler." },
  { kat:"ataturk", soru:"Milliyetçilik ilkesini açıklayın.", cevap:"Ortak dil, tarih ve kültür birliğiyle Türk milletinin refahını hedefleyen anlayıştır; ırkçılığı reddeder." },
  { kat:"ataturk", soru:"Halkçılık ilkesini açıklayın.", cevap:"Halk arasında demokrasi kültürünün geliştirilmesi; herkesin kanun önünde eşit olması, sınıf ayrımı gözetilmemesi." },
  { kat:"ataturk", soru:"Devletçilik ilkesini açıklayın.", cevap:"Devletin kalkınma için gereken ekonomik alanlarda teşebbüsler kurmasıdır. Özel sektörün yetersiz kaldığı alanlarda devlet devreye girer." },
  { kat:"ataturk", soru:"Laiklik ilkesini açıklayın.", cevap:"Din ve devlet işlerinin birbirinden ayrılmasıdır. Devlet tüm dinlere eşit yaklaşır; bireyler din ve vicdan özgürlüğüne sahiptir." },
  { kat:"ataturk", soru:"İnkılapçılık ilkesini açıklayın.", cevap:"Çağın gerisinde kalan kurumları kaldırarak modern kurumların oluşmasını sağlamaktır. Yapılan devrimlerin kalıcı ve sürekli olması esastır." },
  { kat:"ataturk", soru:"Nutuk'ta nelerden bahsedilmektedir?", cevap:"Atatürk 15 Ekim 1927'de 36,5 saat süren konuşmasında 1919-1927 yılları arasındaki olayları anlattı. Osmanlı'nın son günleri, Milli Mücadele ve Cumhuriyet'in kuruluşu aktarıldı." },
  { kat:"ataturk", soru:"Atatürk'ün katıldığı savaşlar hangileridir?", cevap:"Trablusgarp (1911), Balkan Savaşları (1912-13), Çanakkale (1915), Doğu-Kafkas (1916-17), Suriye-Filistin (1917-18), Kurtuluş Savaşı (1919-23)." },
  { kat:"ataturk", soru:"Saltanat ne zaman kaldırıldı?", cevap:"1 Kasım 1922'de kaldırıldı. Osmanlı hanedanlığının siyasi iktidarı sona erdi." },
  { kat:"ataturk", soru:"Halifelik ne zaman kaldırıldı?", cevap:"3 Mart 1924'te kaldırıldı. Laiklik ilkesi doğrultusunda din ve devlet işleri ayrıldı." },
  { kat:"ataturk", soru:"Medeni Kanun ne zaman yürürlüğe girdi ve önemi nedir?", cevap:"17 Şubat 1926'da yürürlüğe girdi. Kadın-erkek eşitliğini sağladı, çok eşliliği kaldırdı, herkese miras hakkı tanıdı." },
  { kat:"ataturk", soru:"Lozan Antlaşması ne zaman imzalandı?", cevap:"24 Temmuz 1923. Türkiye'nin bağımsızlığını uluslararası alanda tanıyan antlaşmadır; Kurtuluş Savaşı'nın diplomatik zaferidir." },
  { kat:"ataturk", soru:"Cumhuriyet ne zaman ilan edildi?", cevap:"29 Ekim 1923. Mustafa Kemal Atatürk ilk Cumhurbaşkanı seçildi." },
  { kat:"ataturk", soru:"Harf İnkılabı ne zaman yapıldı?", cevap:"1 Kasım 1928. Arap alfabesinden Latin alfabesine geçildi." },
  { kat:"ataturk", soru:"Amasya Genelgesi'nin önemi nedir?", cevap:"'Milletin bağımsızlığını yine milletin azim ve kararı kurtaracaktır' ibaresiyle egemenliğin millete ait olduğunu ilk kez vurgular; Milli Mücadele'nin başlangıcı sayılır." },
  { kat:"ataturk", soru:"Sivas Kongresi'nin önemi nedir?", cevap:"Manda ve himayenin kesin olarak reddedildiği, tüm cemiyetlerin Anadolu ve Rumeli Müdafaa-i Hukuk Cemiyeti altında birleştiği kongre." },
  { kat:"ataturk", soru:"Misak-ı Milli nedir?", cevap:"1920'de Osmanlı Mebusan Meclisi'nce kabul edilen milli yemin belgesi; vatanın sınırlarını ve bağımsızlık koşullarını belirler." },
  { kat:"ataturk", soru:"Misak-ı Milli sınırlarına en son katılan il hangisidir?", cevap:"Hatay, 1939'da Türkiye'ye katıldı." },
  { kat:"ataturk", soru:"TBMM ne zaman açıldı?", cevap:"23 Nisan 1920. Ulusal Egemenlik ve Çocuk Bayramı olarak kutlanmaktadır." },
  { kat:"ataturk", soru:"Büyük Taarruz ne zaman başladı, amacı nedir?", cevap:"26 Ağustos 1922. Batı Anadolu'daki Yunan işgalini sona erdirmek ve tüm yurdu kurtarmak amacıyla yapıldı." },
  { kat:"ataturk", soru:"Lale Devrini bitiren isyan hangisidir?", cevap:"Patrona Halil İsyanı (1730)." },
  { kat:"ataturk", soru:"Kasr-ı Şirin Antlaşması nedir?", cevap:"1639'da Osmanlı ile Safevi (bugünkü İran) arasında imzalandı; bugünkü Türkiye-İran sınırının temelini oluşturur." },
  { kat:"ataturk", soru:"İzmir'de ilk kurşunu atan kimdir?", cevap:"Hasan Tahsin. 15 Mayıs 1919'da Yunan işgaline karşı direniş ateşini başlattı." },
  { kat:"ataturk", soru:"Preveze Deniz Savaşı'nın önemi nedir?", cevap:"1538'de gerçekleşti. Türklerin Akdeniz'deki üstünlüğü ve denizcilik kabiliyeti kanıtlandı; Akdeniz kontrolü sağlandı." },
  { kat:"ataturk", soru:"Divan-ı Lügati't-Türk'ün yazarı kimdir?", cevap:"Kaşgarlı Mahmut; 11. yüzyılda yazdı. Türk dilinin ilk büyük sözlüğü ve ansiklopedisidir." },
  { kat:"ataturk", soru:"Gençliğe Hitabe ne anlatmaktadır?", cevap:"İstiklal ve Cumhuriyeti koruma görevini Türk gençliğine emanet eder; milletin bağımsızlığının gençlerin elinde olduğunu vurgular." },
  { kat:"ataturk", soru:"İstiklal Marşı kim tarafından, nerede yazıldı?", cevap:"Mehmet Akif Ersoy; Ankara'daki Tacettin Dergahı'nda 1921'de yazıldı. 10 kıtadan oluşur." },
  { kat:"ataturk", soru:"Atatürk'ün Kara Harp Okulu numarası kaçtır?", cevap:"1283." },
  { kat:"ataturk", soru:"Kurtuluş Savaşı'nda Doğu Cephesindeki savaş kimler arasındaydı?", cevap:"Kazım Karabekir komutasındaki Türk kuvvetleriyle Ermeni ordusu arasında; Kars alınarak Ermenistan ile Kars Antlaşması imzalandı." },
  { kat:"ataturk", soru:"Kuvayı Milliye nedir?", cevap:"Halkın kendi imkânlarıyla oluşturduğu, düzenli ordu kurulana kadar işgale karşı direnen yerel silahlı güç." },
  { kat:"ataturk", soru:"Milli Mücadele döneminin önemli yazarları kimlerdir?", cevap:"Halide Edib Adıvar, Yakup Kadri Karaosmanoğlu, Yahya Kemal Beyatlı." },
  { kat:"ataturk", soru:"Birinci Dünya Savaşı'nın nedenleri nelerdir?", cevap:"Ham madde ve sömürge yarışı, milliyetçilik akımları, silahlanma yarışı, Balkan gerginlikleri ve Avusturya-Macaristan veliahtının Saraybosna'da öldürülmesi." },
  { kat:"ataturk", soru:"Birinci Dünya Savaşı'nda Osmanlı'nın cepheleri hangileridir?", cevap:"Kafkas, Çanakkale, Yemen, Hicaz, Kanal, Filistin, Suriye, Irak, Galiçya ve Makedonya." },
  { kat:"ataturk", soru:"Milli Mücadelede ünvan alan şehirler hangileridir?", cevap:"Gaziantep ('Gazi'), Kahramanmaraş ('Kahraman'), Şanlıurfa ('Şanlı')." },
  { kat:"ataturk", soru:"Marshall Planı nedir?", cevap:"1947'de ABD'nin İkinci Dünya Savaşı sonrası Avrupa'yı kalkındırmak için uyguladığı ekonomik yardım programı. Türkiye de yararlandı." },
  { kat:"ataturk", soru:"İstiklal Yolu neresidir?", cevap:"Kastamonu-İnebolu'dan Ankara'ya uzanan, Kurtuluş Savaşı'nda cephane taşınan tarihi yol." },
  { kat:"ataturk", soru:"Osmanlı Devleti'nin son padişahı kimdir?", cevap:"VI. Mehmet (Vahdettin)." },
  { kat:"ataturk", soru:"Atatürk'ün 'Vatanını en çok seven görevini en iyi yapandır' sözü ne anlama gelir?", cevap:"Vatan sevgisi hamasetle değil, liyakat ve çalışma azmiyle ölçülür. Görevini en iyi yapan kişi vatanına en büyük katkıyı sağlar." },

  // ── TSK & MSB — ASKERİ BİLGİ & MESLEK ──
  { kat:"tskmeslek", soru:"TSK'nın temel görevi nedir?", cevap:"Türk vatanını ve Cumhuriyet'i iç ve dış tehditlere karşı korumak ve kollamaktır." },
  { kat:"tskmeslek", soru:"Uzman erbaş nedir, ne zamandan beri alınmaktadır?", cevap:"Uzman onbaşı ve uzman çavuşları kapsayan sözleşmeli personel. 1986'dan itibaren alınmaktadır." },
  { kat:"tskmeslek", soru:"Uzman erbaş ile uzman çavuş arasındaki fark nedir?", cevap:"Uzman erbaş; onbaşı ve çavuş rütbelerini kapsar. Uzman çavuş, 4+ yıl sonunda yükselinen rütbedir." },
  { kat:"tskmeslek", soru:"Sözleşmeli personel ne zaman kadroya geçer?", cevap:"4. yılın sonunda kadroya geçiş hakkı doğar." },
  { kat:"tskmeslek", soru:"TSK rütbe hiyerarşisini sayınız (er'den yukarı).", cevap:"Er → Onbaşı → Çavuş (erbaş) | Astsubay Çavuş → Kd.Başçavuş (astsubay) | Asteğmen → Yarbay → Albay (subay) | Tuğgeneral → Orgeneral → Mareşal (general/amiral)." },
  { kat:"tskmeslek", soru:"TSK'da en üst rütbe nedir?", cevap:"Mareşal." },
  { kat:"tskmeslek", soru:"Subay ile astsubay arasındaki temel fark nedir?", cevap:"Subaylar sevk ve idare görevlerini yürütür; astsubaylar teknik, idari ve eğitim işlerinde subaylara yardımcı olan profesyonel kadrolardır." },
  { kat:"tskmeslek", soru:"Onbaşı ve çavuş hangi kategoridir?", cevap:"Erbaş kategorisi." },
  { kat:"tskmeslek", soru:"Milli Savunma Bakanı kimdir?", cevap:"Yaşar Güler." },
  { kat:"tskmeslek", soru:"Genelkurmay Başkanı kimdir?", cevap:"Org. Selçuk Bayraktaroğlu." },
  { kat:"tskmeslek", soru:"MSB'nin teşkilat yapısı hangi kanunla düzenlenmiştir?", cevap:"1 sayılı Cumhurbaşkanlığı Kararnamesi." },
  { kat:"tskmeslek", soru:"MSB merkez teşkilatındaki genel müdürlükleri sayınız.", cevap:"Askeralma, Askeri Fabrikalar, Askeri Sağlık, Bütçe-Mali, Hukuk, Lojistik, Personel, Savunma-Güvenlik, Tedarik, Teknik, Tersaneler, Yönetim Hizmetleri GM." },
  { kat:"tskmeslek", soru:"Milli Güvenlik Kurulu (MGK) üyeleri kimlerdir?", cevap:"Cumhurbaşkanı başkanlığında; C.Başkanı Yardımcıları, Adalet, Milli Savunma, İçişleri, Dışişleri Bakanları, Genelkurmay Başkanı, Kara/Deniz/Hava Kuvvetleri Komutanları." },
  { kat:"tskmeslek", soru:"Sahil Güvenlik barışta hangi bakanlığa bağlıdır?", cevap:"İçişleri Bakanlığı; savaşta Deniz Kuvvetleri emrine girer." },
  { kat:"tskmeslek", soru:"MSB Üniversitesi (MSÜ) rektörü kimdir?", cevap:"Prof. Dr. Erhan Afyoncu." },
  { kat:"tskmeslek", soru:"Askeralma Genel Müdürlüğü'nün (ASAL) görevi nedir?", cevap:"Askerlik yükümlülüğüyle ilgili tecil, sevk, muafiyet ve terhis sonrası işlemleri yürütmek." },
  { kat:"tskmeslek", soru:"YAŞ (Yüksek Askeri Şura) üyeleri kimlerdir?", cevap:"Cumhurbaşkanı, C.Başkanı Yardımcıları, Adalet/Dışişleri/İçişleri/Hazine-Maliye/Milli Eğitim/Milli Savunma Bakanları, Genelkurmay Başkanı ve Kuvvet Komutanları." },
  { kat:"tskmeslek", soru:"Türk askeri hangi ülkelerde bulunmaktadır?", cevap:"Suriye, Irak, Libya, KKTC, Katar, Somali, Azerbaycan, Kosova ve Bosna-Hersek." },
  { kat:"tskmeslek", soru:"TSK'da ast üste selam verme ne zaman sona erer?", cevap:"Selamı üst aldığında veya üst yanından tamamen uzaklaşıncaya kadar devam eder." },
  { kat:"tskmeslek", soru:"Sivil memur üst rütbeli ile karşılaşınca nasıl selamlar?", cevap:"Başında kep olmadığından el selamı vermez; vücudunu dik tutarak başıyla ve sözlü (İyi günler komutanım) selamlar." },
  { kat:"tskmeslek", soru:"Türk Bayrağı Kanunu'na göre bayrağa ne yapılamaz?", cevap:"Üzerine amblem, logo, yazı konulamaz; elbise olarak giyilemez." },
  { kat:"tskmeslek", soru:"MSB logosundaki sekiz köşeli yıldız neyi temsil eder?", cevap:"Selçuklu yıldızı; zaferi, gururu ve Türk milletinin şanlı tarihini simgeler." },
  { kat:"tskmeslek", soru:"Cumhurbaşkanlığı forsundaki 16 yıldız ne anlama gelir?", cevap:"Tarihteki 16 büyük Türk devletini temsil eder; ortadaki güneş Türkiye Cumhuriyeti'ni simgeler." },
  { kat:"tskmeslek", soru:"Türk bayrağındaki hilal ve yıldız ne anlama gelir?", cevap:"Hilal İslamiyet'i, yıldız Türklüğü temsil eder. Kırmızı şehit kanını simgeler." },
  { kat:"tskmeslek", soru:"Sınır ötesi düzenlenen temel harekatlar hangileridir?", cevap:"Fırat Kalkanı, Zeytin Dalı, Barış Pınarı ve Pençe-Kilit Harekatları." },
  { kat:"tskmeslek", soru:"Kıbrıs Barış Harekâtı ne zaman yapıldı, parolası neydi?", cevap:"1974. Parolası 'Ayşe Tatile Çıksın' idi. Yanlışlıkla vurulan gemimiz TCG Kocatepe'dir." },
  { kat:"tskmeslek", soru:"KAAN nedir?", cevap:"Türkiye'nin yerli 5. nesil savaş uçağı. 2024'te ilk uçuşunu gerçekleştirdi." },
  { kat:"tskmeslek", soru:"KIZILELMA nedir?", cevap:"Türkiye'nin ilk insansız savaş uçağı (MİUS); radardan kaçınma özelliğine sahip." },
  { kat:"tskmeslek", soru:"SİPER nedir?", cevap:"Türkiye'nin yerli uzun menzilli ve çok katmanlı milli hava savunma sistemi." },
  { kat:"tskmeslek", soru:"İHA ve SİHA arasındaki fark nedir?", cevap:"İHA silahsız gözlem yapar; SİHA mühimmatlı saldırı yeteneğine sahiptir." },
  { kat:"tskmeslek", soru:"MİLGEM projesi nedir?", cevap:"Milli Gemi Projesi; TCG Heybeliada, TCG Büyükada gibi savaş gemilerinin yerli üretimidir." },
  { kat:"tskmeslek", soru:"Mavi Vatan doktrini nedir?", cevap:"Türkiye'nin Karadeniz, Akdeniz ve Ege'deki deniz yetki alanlarını (karasuları, kıta sahanlığı, MEB) kapsayan strateji." },
  { kat:"tskmeslek", soru:"Münhasır Ekonomik Bölge (MEB) nedir?", cevap:"Kıyıdan 200 deniz miline kadar uzanan; kıyı devletlerine deniz kaynaklarını işletme ve yönetme egemen hakkı veren BM Deniz Hukuku bölgesi." },
  { kat:"tskmeslek", soru:"Disiplin nedir?", cevap:"Kanunlara, nizamlara ve amirlere mutlak itaat; bireylerin toplumun kurallarına uymasını sağlayan önlemlerin tümü." },
  { kat:"tskmeslek", soru:"Seferberlik nedir?", cevap:"Ülkenin silahlı kuvvetleri ve ekonomisini savaşa hazır hale getiren hazırlıkların tümü." },
  { kat:"tskmeslek", soru:"Kanunsuz emir nedir?", cevap:"Kanun, tüzük veya yönetmeliğe aykırı emirdir. Memur yerine getirmez ve aykırılığı emri verene bildirir." },
  { kat:"tskmeslek", soru:"Ömer Halisdemir kimdir?", cevap:"15 Temmuz darbe girişiminde darbeci generali etkisiz hale getirerek hayatını kaybeden Kahraman Şehidimiz." },
  { kat:"tskmeslek", soru:"Fethi Sekin kimdir?", cevap:"İzmir Adliyesi'ne yapılan terör saldırısında teröristleri etkisiz hale getiren, ardından şehit olan kahraman polisimiz." },
  { kat:"tskmeslek", soru:"Eren Bülbül kimdir?", cevap:"Trabzon Maçka'da PKK'lı teröristlerin yerini jandarmaya gösterirken 15 yaşında şehit olan gencimiz." },
  { kat:"tskmeslek", soru:"MSB'de 'Askeri Gizli Bilgileri' ifşa etmenin TCK'daki karşılığı nedir?", cevap:"TCK m.326 ve devamı uyarınca 'Devlet Sırlarına Karşı Suçlar' kapsamında hapis ve ömür boyu kamu hizmetlerinden men cezası öngörülür." },
  { kat:"tskmeslek", soru:"657 sayılı Kanun'a göre memurların disiplin cezaları nelerdir?", cevap:"Uyarma, kınama, aylıktan kesme, kademe ilerlemesinin durdurulması ve devlet memurluğundan çıkarma." },
  { kat:"tskmeslek", soru:"Neden uzman erbaş olmak istiyorsunuz?", cevap:"(Kişiye özgü) Vatan sevgisi, disiplinli yaşam anlayışı, kariyer güvencesi ve millete hizmet etme isteği gibi samimi gerekçelerinizi belirtin." },

  // ── GENEL KÜLTÜR & TARİH ──
  { kat:"genel", soru:"Türkiye'nin kara komşuları kaç tanedir, hangileridir?", cevap:"8 kara komşusu: Yunanistan, Bulgaristan, Gürcistan, Ermenistan, Nahçıvan, İran, Irak, Suriye." },
  { kat:"genel", soru:"İran ile sınır olan illerimiz hangileridir?", cevap:"Van, Hakkari, Ağrı ve Iğdır." },
  { kat:"genel", soru:"Türkiye'nin en büyük dağı hangisidir?", cevap:"Ağrı Dağı — 5.137 metre." },
  { kat:"genel", soru:"Türkiye'nin en uzun nehri hangisidir?", cevap:"Kızılırmak — yaklaşık 1.355 km." },
  { kat:"genel", soru:"Türkiye'nin en büyük gölü hangisidir?", cevap:"Van Gölü." },
  { kat:"genel", soru:"Türkiye'nin yüzölçümü nedir?", cevap:"783.562 km²." },
  { kat:"genel", soru:"Türkiye kaç coğrafi bölgeye ayrılır?", cevap:"7 coğrafi bölge." },
  { kat:"genel", soru:"Türkiye'nin üç tarafını çeviren denizler nelerdir?", cevap:"Kuzeyde Karadeniz, batıda Ege, güneyde Akdeniz." },
  { kat:"genel", soru:"Türkiye'deki boğazlar hangileridir?", cevap:"İstanbul Boğazı ve Çanakkale Boğazı." },
  { kat:"genel", soru:"Türkiye'nin tek iç denizi hangisidir?", cevap:"Marmara Denizi." },
  { kat:"genel", soru:"Türkiye ile Yunanistan arasındaki doğal sınırı oluşturan nehir hangisidir?", cevap:"Meriç Nehri." },
  { kat:"genel", soru:"Türkiye ile Yunanistan arasındaki başlıca sorunlar nelerdir?", cevap:"Ege kıta sahanlığı, karasuları genişliği, adaların silahlandırılması ve FIR (hava sahası) sorunları." },
  { kat:"genel", soru:"NATO ne zaman kuruldu, Türkiye ne zaman üye oldu?", cevap:"NATO 1949'da kuruldu; Türkiye 1952'de üye oldu." },
  { kat:"genel", soru:"BM Güvenlik Konseyi'nin 5 daimi üyesi kimlerdir?", cevap:"ABD, Rusya, Çin, İngiltere ve Fransa." },
  { kat:"genel", soru:"NATO'ya üye olup ordusu bulunmayan ülke hangisidir?", cevap:"İzlanda." },
  { kat:"genel", soru:"Türkiye Cumhurbaşkanı seçilebilmek için minimum yaş kaçtır?", cevap:"40." },
  { kat:"genel", soru:"Milletvekili seçilebilmek için alt yaş sınırı nedir?", cevap:"18." },
  { kat:"genel", soru:"Anayasa Mahkemesi kaç üyeden oluşur ve kim seçer?", cevap:"15 üye; Cumhurbaşkanı 12'sini, TBMM 3'ünü seçer." },
  { kat:"genel", soru:"TBMM ve Cumhurbaşkanlığı seçimleri kaç yılda bir yapılır?", cevap:"5 yılda bir." },
  { kat:"genel", soru:"Uyuşmazlık Mahkemesi nedir?", cevap:"Adli ve idari yargı mercileri arasındaki görev ve hüküm uyuşmazlıklarını kesin olarak çözen bağımsız yüksek mahkeme." },
  { kat:"genel", soru:"Kamu Denetçiliği (Ombudsman) nedir?", cevap:"İdarenin eylem ve işlemlerini insan haklarına dayalı adalet anlayışıyla inceleyen, araştıran ve önerilerde bulunan bağımsız denetim kurumu." },
  { kat:"genel", soru:"İstanbul'u fetheden komutan kimdir?", cevap:"Fatih Sultan Mehmet — 1453." },
  { kat:"genel", soru:"Malazgirt Savaşı ne zaman yapıldı, önemi nedir?", cevap:"1071; Türklerin Anadolu'ya yerleşmesinin önü açıldı." },
  { kat:"genel", soru:"Osmanlı Devleti'nin kuruluş tarihi ve kurucusu kimdir?", cevap:"1299; Osman Gazi." },
  { kat:"genel", soru:"Mescid-i Aksa nerededir?", cevap:"İsrail işgali altındaki Kudüs'te; İslamiyet'in ilk kıblesi." },
  { kat:"genel", soru:"Mimar Sinan'ın üç eserini ve anlamını söyleyin.", cevap:"Şehzade Camii (çıraklık), Süleymaniye Camii (kalfalık), Selimiye Camii (ustalık eseri)." },
  { kat:"genel", soru:"Göbeklitepe nerededir ve önemi nedir?", cevap:"Şanlıurfa; dünyanın bilinen en eski tapınak merkezi, yaklaşık 12.000 yıllık." },
  { kat:"genel", soru:"Naim Süleymanoğlu kimdir?", cevap:"'Cep Herkülü' lakaplı, Türkiye'nin ilk olimpiyat şampiyonu haltercisi." },
  { kat:"genel", soru:"Abdullah Öcalan ne zaman ve nerede yakalandı?", cevap:"16 Şubat 1999, Kenya." },
  { kat:"genel", soru:"Asya Hun Devleti'nin kurucusu kimdir?", cevap:"Teoman." },
  { kat:"genel", soru:"Kuzey Kıbrıs Türk Cumhuriyeti'nin ilk Cumhurbaşkanı kimdir?", cevap:"Rauf Denktaş." },
  { kat:"genel", soru:"Demokrasi nedir?", cevap:"Halkın kendi kendini yönettiği; halk egemenliğine dayalı yönetim biçimi." },
  { kat:"genel", soru:"Meşru müdafaa nedir?", cevap:"Uğranılan saldırıya karşı orantılı savunma hakkı." },
  { kat:"genel", soru:"Muhacir ve mülteci arasındaki fark nedir?", cevap:"Muhacir gönüllü/ekonomik göç eder; mülteci zulüm ya da savaştan kaçarak yasal koruma arayan kişidir." },
  { kat:"genel", soru:"Rögar kapağı neden yuvarlaktır?", cevap:"Daire olduğundan hiçbir açıdan içine düşmez; köşeli olsaydı köşesinden deliğe girebilirdi." },
  { kat:"genel", soru:"Rüzgar kuzeyden eserse bayrak nereye dalgalanır?", cevap:"Güneye." },
  { kat:"genel", soru:"Haritada yüksek yerler hangi renkle gösterilir?", cevap:"Kahverengi ve beyaz; yükseklik arttıkça koyulaşır." },
  { kat:"genel", soru:"Meridyenlerin başlangıç noktası neresidir?", cevap:"İngiltere'nin Greenwich şehri (0° meridyeni)." },
  { kat:"genel", soru:"İbn-i Sina kimdir?", cevap:"Büyük Türk-İslam hekimi ve filozofu; 'Kanun fit-Tıbb' adlı eserin yazarı." },
  { kat:"genel", soru:"Fevzi Çakmak kimdir?", cevap:"Kurtuluş Savaşı kahramanı; Türkiye Cumhuriyeti'nin ilk Genelkurmay Başkanı ve ikinci Mareşali." },
  { kat:"genel", soru:"Türkiye'nin en yüksek barajı hangisidir?", cevap:"Yusufeli Barajı (Artvin, Çoruh Nehri üzerinde)." },
  { kat:"genel", soru:"Türkiye'nin yerli otomobili TOGG nerede üretiliyor?", cevap:"Bursa/Gemlik." },
  { kat:"genel", soru:"Şangay İşbirliği Örgütü (ŞİÖ) kurucu ülkeleri kimlerdir?", cevap:"Çin, Rusya, Kazakistan, Kırgızistan ve Tacikistan (1996'da kuruldu)." },

  // ── GÜNCEL BİLGİ & POLİTİKA ──
  { kat:"guncel", soru:"15 Temmuz nedir?", cevap:"FETÖ terör örgütünün 2016'daki darbe girişimi. Türk milleti meydanlara inerek demokratik düzeni korudu." },
  { kat:"guncel", soru:"FETÖ ile PKK arasındaki temel fark nedir?", cevap:"FETÖ dini istismar ederek devlet kurumlarına sızdı; PKK silahlı bölücü terör örgütüdür. İkisi de Türkiye'yi bölmeyi hedefler." },
  { kat:"guncel", soru:"15 Temmuz'dan sonra hangi ilçe unvan aldı?", cevap:"Ankara'nın Kazan ilçesi 'Kahraman Kazan' unvanını aldı." },
  { kat:"guncel", soru:"Suriye'de ne işimiz var?", cevap:"Sınır güvenliğini sağlamak, terör koridorunu engellemek, Suriye'nin toprak bütünlüğünü ve halkın huzurunu desteklemek." },
  { kat:"guncel", soru:"Suriye Devlet Başkanı kimdir?", cevap:"Ahmet Şara (rejim değişikliği sonrası yeni yönetim)." },
  { kat:"guncel", soru:"Libya ile aramızdaki ilişki nedir?", cevap:"Deniz yetki alanları anlaşması ve askeri eğitim/danışmanlık iş birliği; ticari ilişkiler de gelişmektedir." },
  { kat:"guncel", soru:"Suriye'ye yapılan harekatlar nelerdir?", cevap:"Fırat Kalkanı, Zeytin Dalı ve Barış Pınarı Harekatları." },
  { kat:"guncel", soru:"Türkiye'nin en son milli savaş uçağı hangisidir?", cevap:"KAAN; 2024'te ilk uçuşunu tamamladı." },
  { kat:"guncel", soru:"Türkiye'nin milli helikopteri nedir?", cevap:"T625 Gökbey (genel amaçlı) ve T129 Atak (taarruz)." },
  { kat:"guncel", soru:"TOGG nedir?", cevap:"Türkiye'nin yerli ve milli elektrikli otomobili; Bursa'da üretilmektedir." },
  { kat:"guncel", soru:"Karadeniz'de keşfedilen doğalgaz sahası adı nedir?", cevap:"Sakarya Gaz Sahası." },
  { kat:"guncel", soru:"Türkiye'nin ilk astronotu kimdir?", cevap:"Alper Gezeravcı; 2024'te Uluslararası Uzay İstasyonu'na gitti." },
  { kat:"guncel", soru:"İmralı açılımı hakkında görüşünüz nedir?", cevap:"Türkiye milli değerlerinden taviz vermez; akan kanın durması için yürütülen görüşmeler devletin denetiminde sürmektedir." },
  { kat:"guncel", soru:"Hangi terör örgütleriyle mücadele ediyoruz?", cevap:"Başlıca PKK ve FETÖ ile." },

  // ── KİŞİSEL & MÜLAKAT TEKNİKLERİ ──
  { kat:"kisisel", soru:"Kendinizi kısaca tanıtın.", cevap:"(Kişiye özgü) Adınız, memleketiniz, eğitiminiz, askerlik/iş geçmişiniz ve bu göreve neden başvurduğunuzu özgüvenli biçimde aktarın." },
  { kat:"kisisel", soru:"Neden bu mesleği seçiyorsunuz?", cevap:"(Kişiye özgü) Vatan sevgisi, disiplinli yaşam, kariyer güvencesi, millete hizmet gibi samimi gerekçelerinizi içtenlikle belirtin." },
  { kat:"kisisel", soru:"Bu meslekle ilgili güçlü yönleriniz nelerdir?", cevap:"Disiplin, sorumluluk bilinci, takım çalışmasına uyum, kurallara saygı gibi özelliklerinizi somut örneklerle paylaşın." },
  { kat:"kisisel", soru:"Bu meslekle ilgili zayıf yönleriniz nelerdir?", cevap:"Gelişime açık bir özelliği dürüstçe belirtin ve nasıl çalıştığınızı ekleyin. Klişelerden kaçının." },
  { kat:"kisisel", soru:"Kendinizi üç kelimeyle tanımlayın.", cevap:"Disiplinli, sorumluluk sahibi, takım oyuncusu — ve her birini somut örnekle pekiştirin." },
  { kat:"kisisel", soru:"Bu göreve atanırsanız kuruma katkınız ne olur?", cevap:"Mesleki yetkinliğinizi ve kuruma bağlılığınızı somut görevler üzerinden aktarın." },
  { kat:"kisisel", soru:"Zor bir durumla karşılaşınca nasıl davranırsınız?", cevap:"Sakin kalarak durumu analiz ederim, çözüm odaklı adımlar atarım; gerekirse üstlerimden destek isterim." },
  { kat:"kisisel", soru:"Sizi neden seçmeliyiz?", cevap:"Bilgi birikimimi MSB'nin yüksek disiplin anlayışıyla birleştirmeye hazırım. Sorumluluk bilinci, ketumiyet ve devlet memurluğu vakarına duyduğum saygıyla en iyi şekilde hizmet ederim." },
  { kat:"kisisel", soru:"Amirinizin bir vatandaşı kayırdığını fark ederseniz ne yaparsınız?", cevap:"Eşitlik ilkesi gereği durumu nazikçe amirime arz ederim; sistematik bir durum varsa üst makama rapor ederim." },
  { kat:"kisisel", soru:"İş yerinde yangın başlangıcı fark ederseniz ne yaparsınız?", cevap:"'Yangın var!' diye uyarırım, ihbar butonuna basarım; müdahale edebileceğim boyuttaysa yangın tüpüyle müdahale ederim, değilse tahliye protokolünü uygularım." },
  { kat:"kisisel", soru:"Hassas bir evrakın yetkisizce incelendiğinden şüphelenirseniz ne yaparsınız?", cevap:"Herhangi bir gürültü çıkarmadan, doğrudan amirlerime ve güvenlik birimine gözlemlerimi somut verilerle rapor ederim." },
  { kat:"kisisel", soru:"Devlet memuru olmanın en büyük sorumluluğu nedir?", cevap:"Devletin gülen yüzü, adil eli ve sarsılmaz disiplini olmaktır. Her maaşın hakkını dürüstlük ve tarafsızlıkla vermektir." },
  { kat:"kisisel", soru:"Kamu görevlisi hediye alabilir mi?", cevap:"Hayır. Kamu Görevlileri Etik Rehberi uyarınca tarafsızlığı gölgeleyecek hiçbir hediye kabul edilemez." },
  { kat:"kisisel", soru:"Siyasi tarafsızlık ne demektir?", cevap:"Sadece yasalar ve kamu yararı doğrultusunda hizmet üretmek; vatandaşa siyasi görüşüne bakmaksızın eşit davranmak." },
  { kat:"kisisel", soru:"Atandığınız şehirde yaşayıp geçinebilecek misiniz?", cevap:"Evet; gerekli uyumu sağlarım. Devlet memuru olarak atamalara hazırım." },
];

// ════════════════════════════════════════════════════════════
// KATEGORİ ETİKETLERİ
// ════════════════════════════════════════════════════════════
var KAT_ETIKETLERI = {
  hepsi:    { label:"🎲 Tümü",       renk:"var(--accent)" },
  ataturk:  { label:"🇹🇷 Atatürk",   renk:"#e74c3c" },
  tskmeslek:{ label:"⚔️ TSK & MSB", renk:"#4f8ef7" },
  genel:    { label:"🌍 Genel",      renk:"#2ecc71" },
  guncel:   { label:"📰 Güncel",     renk:"#f39c12" },
  kisisel:  { label:"🎙️ Kişisel",   renk:"#a78bfa" },
  yanlis:   { label:"❌ Bilmedim",   renk:"#e74c3c" },
};

// ════════════════════════════════════════════════════════════
// SİMÜLASYON MODELLERİ
// ════════════════════════════════════════════════════════════
var SIM_MODLAR = [
  { id:"karisik", label:"Karışık Mülakat", icon:"🎲", aciklama:"Tüm kategorilerden 10 soru; gerçek mülakat gibi sıralı.", adet:10, kat:null },
  { id:"ataturk", label:"Atatürk & İnkılap", icon:"🇹🇷", aciklama:"Sadece Atatürk konularından 8 soru.", adet:8, kat:"ataturk" },
  { id:"tskmeslek", label:"TSK & Meslek", icon:"⚔️", aciklama:"Askeri bilgi ve MSB'ye özel 8 soru.", adet:8, kat:"tskmeslek" },
  { id:"hizli", label:"Hızlı Tur (5 Soru)", icon:"⚡", aciklama:"5 dakikada 5 soru; ısınma turları için.", adet:5, kat:null },
];

// ════════════════════════════════════════════════════════════
// DEĞİŞKENLER
// ════════════════════════════════════════════════════════════
var db;
var tumSorular = [];
var aktifSorular = [];
var aktifIdx = 0;
var aktifKat = "hepsi";
var ilerleme = { goruldu:{}, dogru:[], yanlis:[] };

// Simülasyon durumu
var simDurum = "giris"; // giris | devam | bitti
var simSorular = [];
var simIdx = 0;
var simCevaplar = []; // {soru, cevapGosterildi, puan}
var simMod = null;

// ════════════════════════════════════════════════════════════
// BAŞLANGIC
// ════════════════════════════════════════════════════════════
window.onFirebaseReady(function() {
  db = window.__db;
  baslat();
});

async function baslat() {
  tumSorular = ORNEK_SORULAR.map(function(s,i){ return Object.assign({ id:"s"+i }, s); });

  try {
    var ekSnap = await db.collection("mulakat_ozel").get();
    ekSnap.forEach(function(s){ tumSorular.push(Object.assign({ id:s.id, ozel:true }, s.data())); });
  } catch(e){}

  try {
    var iSnap = await db.collection("mulakat_ilerleme").doc("ilerleme").get();
    if (iSnap.exists) ilerleme = iSnap.data();
  } catch(e) {
    var c = window.cacheOku("mulakat_ilerleme");
    if (c) ilerleme = c;
  }

  renderFiltreBtnlari();
  filtreUygula("hepsi");
  dinleMulakat();
  dinleSoruEkle();
  renderSekmeleri();
  renderSimGiris();
  renderRehber();
}

// ════════════════════════════════════════════════════════════
// SEKME SİSTEMİ
// ════════════════════════════════════════════════════════════
function renderSekmeleri() {
  document.querySelectorAll(".mulakat-sekme").forEach(function(btn) {
    btn.addEventListener("click", function() {
      document.querySelectorAll(".mulakat-sekme").forEach(function(b){ b.classList.remove("active"); });
      document.querySelectorAll(".mulakat-panel").forEach(function(p){ p.classList.remove("active"); });
      btn.classList.add("active");
      var panel = document.getElementById("panel-" + btn.dataset.sekme);
      if (panel) panel.classList.add("active");
    });
  });
}

// ════════════════════════════════════════════════════════════
// FLASHCARD SİSTEMİ
// ════════════════════════════════════════════════════════════
function renderFiltreBtnlari() {
  var wrap = document.querySelector(".mulakat-filtre-wrap");
  if (!wrap) return;
  wrap.innerHTML = "";
  Object.keys(KAT_ETIKETLERI).forEach(function(kat) {
    var btn = document.createElement("button");
    btn.className = "btn btn-outline mulakat-filtre" + (kat === "hepsi" ? " active" : "");
    btn.dataset.kat = kat;
    var sayi = kat === "hepsi" ? tumSorular.length
      : kat === "yanlis" ? (ilerleme.yanlis||[]).length
      : tumSorular.filter(function(s){ return s.kat===kat; }).length;
    btn.textContent = KAT_ETIKETLERI[kat].label + " (" + sayi + ")";
    wrap.appendChild(btn);
  });
}

function filtreUygula(kat) {
  aktifKat = kat;
  if (kat === "hepsi") {
    aktifSorular = tumSorular.slice();
  } else if (kat === "yanlis") {
    var yanlisIds = ilerleme.yanlis||[];
    aktifSorular = tumSorular.filter(function(s){ return yanlisIds.indexOf(s.id)>=0; });
    if (!aktifSorular.length) { showToast("Hiç 'Bilmedim' yok 🎉","success"); aktifSorular=tumSorular.slice(); }
  } else {
    aktifSorular = tumSorular.filter(function(s){ return s.kat===kat; });
  }
  aktifIdx = 0;
  renderKart();
  renderIlerlemeBar();
}

function renderKart() {
  if (!aktifSorular.length) return;
  var soru = aktifSorular[aktifIdx];
  document.getElementById("mulakat-soru-text").textContent = soru.soru;
  document.getElementById("mulakat-cevap-text").textContent = soru.cevap;
  document.getElementById("mulakat-soru-no").textContent = (aktifIdx+1)+" / "+aktifSorular.length;

  var katEl = document.getElementById("mulakat-kart-kat");
  if (katEl && KAT_ETIKETLERI[soru.kat]) katEl.textContent = KAT_ETIKETLERI[soru.kat].label;

  var dotsEl = document.getElementById("mulakat-dots");
  var dogru = (ilerleme.dogru||[]).filter(function(id){ return aktifSorular.some(function(s){ return s.id===id; }); }).length;
  dotsEl.textContent = "✅ "+dogru+" / "+aktifSorular.length;

  var kart = document.getElementById("mulakat-kart");
  kart.className = "flashcard";
  if ((ilerleme.dogru||[]).indexOf(soru.id)>=0) kart.classList.add("kart-dogru");
  else if ((ilerleme.yanlis||[]).indexOf(soru.id)>=0) kart.classList.add("kart-yanlis");

  if (!ilerleme.goruldu[soru.id]) {
    ilerleme.goruldu[soru.id] = true;
    try { db.collection("mulakat_ilerleme").doc("ilerleme").set(ilerleme); } catch(e){}
    window.cacheYaz("mulakat_ilerleme", ilerleme);
  }
  renderIlerlemeBar();
}

function renderIlerlemeBar() {
  var goruldu = Object.keys(ilerleme.goruldu||{}).length;
  var dogru = (ilerleme.dogru||[]).length;
  var pct = tumSorular.length ? Math.round((goruldu/tumSorular.length)*100) : 0;
  var el = document.getElementById("mulakat-ilerleme-bar");
  if (el) el.textContent = "✅ "+dogru+" bildim  |  "+goruldu+"/"+tumSorular.length+" görüldü (%"+pct+")";
}

function dinleMulakat() {
  document.addEventListener("click", function(e) {
    var btn = e.target.closest(".mulakat-filtre");
    if (!btn) return;
    document.querySelectorAll(".mulakat-filtre").forEach(function(b){ b.classList.remove("active"); });
    btn.classList.add("active");
    filtreUygula(btn.dataset.kat);
  });

  document.getElementById("btn-mulakat-prev").addEventListener("click", function() {
    if (aktifIdx>0) { aktifIdx--; renderKart(); }
  });
  document.getElementById("btn-mulakat-next").addEventListener("click", function() {
    if (aktifIdx<aktifSorular.length-1) { aktifIdx++; renderKart(); }
  });

  var kart = document.getElementById("mulakat-kart");
  var startX = 0;
  kart.addEventListener("touchstart", function(e){ startX=e.touches[0].clientX; },{passive:true});
  kart.addEventListener("touchend", function(e){
    var diff = startX - e.changedTouches[0].clientX;
    if (Math.abs(diff)>50) {
      if (diff>0 && aktifIdx<aktifSorular.length-1){ aktifIdx++; renderKart(); }
      else if (diff<0 && aktifIdx>0){ aktifIdx--; renderKart(); }
    }
  },{passive:true});

  document.getElementById("btn-dogru").addEventListener("click", async function() {
    var soru = aktifSorular[aktifIdx];
    if ((ilerleme.dogru||[]).indexOf(soru.id)<0) (ilerleme.dogru=ilerleme.dogru||[]).push(soru.id);
    ilerleme.yanlis = (ilerleme.yanlis||[]).filter(function(id){ return id!==soru.id; });
    try { await db.collection("mulakat_ilerleme").doc("ilerleme").set(ilerleme); } catch(e){}
    window.cacheYaz("mulakat_ilerleme", ilerleme);
    renderFiltreBtnlari(); showToast("✅ Harika!","success"); renderKart();
    if (aktifIdx<aktifSorular.length-1) setTimeout(function(){ aktifIdx++; renderKart(); },400);
  });

  document.getElementById("btn-yanlis").addEventListener("click", async function() {
    var soru = aktifSorular[aktifIdx];
    if ((ilerleme.yanlis||[]).indexOf(soru.id)<0) (ilerleme.yanlis=ilerleme.yanlis||[]).push(soru.id);
    try { await db.collection("mulakat_ilerleme").doc("ilerleme").set(ilerleme); } catch(e){}
    window.cacheYaz("mulakat_ilerleme", ilerleme);
    renderFiltreBtnlari(); showToast("❌ Tekrar çalış","error"); renderKart();
    if (aktifIdx<aktifSorular.length-1) setTimeout(function(){ aktifIdx++; renderKart(); },400);
  });

  document.getElementById("btn-mulakat-karistir").addEventListener("click", function() {
    for (var i=aktifSorular.length-1;i>0;i--){ var j=Math.floor(Math.random()*(i+1)); var t=aktifSorular[i]; aktifSorular[i]=aktifSorular[j]; aktifSorular[j]=t; }
    aktifIdx=0; renderKart(); showToast("🔀 Karıştırıldı!");
  });
}

function dinleSoruEkle() {
  var acBtn = document.getElementById("btn-soru-ekle-ac");
  var form = document.getElementById("soru-ekle-form");
  if (!acBtn||!form) return;
  acBtn.addEventListener("click", function(){ form.style.display=form.style.display==="none"?"":"none"; });
  document.querySelectorAll(".soru-kat-btn").forEach(function(btn){
    btn.addEventListener("click", function(){
      document.querySelectorAll(".soru-kat-btn").forEach(function(b){ b.classList.remove("selected"); });
      btn.classList.add("selected");
    });
  });
  document.getElementById("btn-soru-kaydet").addEventListener("click", async function(){
    var s=(document.getElementById("yeni-soru-txt").value||"").trim();
    var c=(document.getElementById("yeni-cevap-txt").value||"").trim();
    var kb=document.querySelector(".soru-kat-btn.selected");
    if (!s){ showToast("Soru boş!","error"); return; }
    if (!c){ showToast("Cevap boş!","error"); return; }
    var yeni={ kat:kb?kb.dataset.kat:"genel", soru:s, cevap:c, ozel:true };
    try { var ref=await db.collection("mulakat_ozel").add(yeni); yeni.id=ref.id; } catch(e){ yeni.id="ozel_"+Date.now(); }
    tumSorular.push(yeni); aktifSorular=tumSorular.slice();
    document.getElementById("yeni-soru-txt").value=""; document.getElementById("yeni-cevap-txt").value="";
    form.style.display="none"; renderFiltreBtnlari(); filtreUygula(aktifKat);
    showToast("✅ Eklendi! Toplam: "+tumSorular.length,"success");
  });
  document.getElementById("btn-soru-iptal").addEventListener("click", function(){ form.style.display="none"; });
}

// ════════════════════════════════════════════════════════════
// SİMÜLASYON
// ════════════════════════════════════════════════════════════
function renderSimGiris() {
  var el = document.getElementById("sim-icerik");
  if (!el) return;

  var html = '<div class="card sim-giris-card">' +
    '<div style="font-size:32px;margin-bottom:8px">🎙️</div>' +
    '<h2>Mülakat Simülasyonu</h2>' +
    '<p>Gerçek mülakat ortamı gibi sorular gelir. Kendi kendine sesli cevap ver, sonra doğru cevabı gör ve değerlendir.</p>' +
    '</div>' +
    '<p class="label" style="margin-bottom:10px">Mülakat Modu Seç</p>' +
    '<div class="sim-mod-grid">';

  SIM_MODLAR.forEach(function(mod) {
    html += '<button class="sim-mod-btn" data-mod="' + mod.id + '">' +
      '<span class="sim-mod-icon">' + mod.icon + '</span>' +
      '<span style="font-size:13px;font-weight:600;color:var(--text)">' + mod.label + '</span>' +
      '<span style="font-size:11px;text-align:center;line-height:1.4">' + mod.aciklama + '</span>' +
      '</button>';
  });

  html += '</div>' +
    '<button class="btn btn-primary" id="btn-sim-baslat" style="width:100%;margin-top:4px">🎙️ Mülakatı Başlat</button>';

  el.innerHTML = html;

  var secilenMod = null;
  el.querySelectorAll(".sim-mod-btn").forEach(function(btn) {
    btn.addEventListener("click", function() {
      el.querySelectorAll(".sim-mod-btn").forEach(function(b){ b.classList.remove("selected"); });
      btn.classList.add("selected");
      secilenMod = btn.dataset.mod;
    });
  });

  document.getElementById("btn-sim-baslat").addEventListener("click", function() {
    if (!secilenMod) { showToast("Önce bir mod seç!","error"); return; }
    simMod = SIM_MODLAR.find(function(m){ return m.id===secilenMod; });
    simBaslat();
  });
}

function simBaslat() {
  // Soruları seç
  var havuz = simMod.kat ? tumSorular.filter(function(s){ return s.kat===simMod.kat; }) : tumSorular.slice();
  // Karıştır ve seç
  for (var i=havuz.length-1;i>0;i--){ var j=Math.floor(Math.random()*(i+1)); var t=havuz[i]; havuz[i]=havuz[j]; havuz[j]=t; }
  simSorular = havuz.slice(0, simMod.adet);
  simIdx = 0;
  simCevaplar = [];
  simDurum = "devam";
  renderSimSoru();
}

function renderSimSoru() {
  var el = document.getElementById("sim-icerik");
  if (!el) return;

  if (simIdx >= simSorular.length) {
    simDurum = "bitti";
    renderSimSonuc();
    return;
  }

  var soru = simSorular[simIdx];
  var katInfo = KAT_ETIKETLERI[soru.kat] || { label:"Genel", renk:"var(--accent)" };
  var ilerlecePct = Math.round((simIdx / simSorular.length) * 100);

  var html =
    '<div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:14px">' +
      '<button class="btn btn-ghost btn-sm" id="btn-sim-cikis">✕ Çıkış</button>' +
      '<span class="badge">' + (simIdx+1) + ' / ' + simSorular.length + '</span>' +
    '</div>' +
    '<div style="height:4px;background:var(--border);border-radius:2px;margin-bottom:16px;overflow:hidden">' +
      '<div style="height:100%;width:'+ilerlecePct+'%;background:var(--accent);border-radius:2px;transition:width 0.3s"></div>' +
    '</div>' +
    '<div class="sim-soru-no">' +
      '<span class="sim-ipucu-badge" style="background:'+katInfo.renk+'22;color:'+katInfo.renk+'">'+katInfo.label+'</span>' +
    '</div>' +
    '<div class="sim-soru-wrap">' +
      '<div class="sim-soru-text">' + escHTML(soru.soru) + '</div>' +
    '</div>' +
    '<p class="hint" style="margin:10px 0 4px">🎙️ Sesli cevap ver, sonra doğru cevabı gör:</p>' +
    '<textarea class="sim-cevap-alan" id="sim-cevap-inp" placeholder="Notunu buraya yazabilirsin (isteğe bağlı)..."></textarea>' +
    '<div id="sim-cevap-bolum" style="display:none">' +
      '<div class="sim-cevap-baslik">✅ Doğru Cevap</div>' +
      '<div class="sim-cevap-goster">' + escHTML(soru.cevap) + '</div>' +
      '<p class="label" style="margin:14px 0 8px">Kendinizi değerlendirin:</p>' +
      '<div class="btn-row" style="justify-content:center;gap:10px">' +
        '<button class="btn btn-success" id="btn-sim-dogru">✅ Bildim</button>' +
        '<button class="btn btn-danger" id="btn-sim-yanlis">❌ Bilmedim</button>' +
      '</div>' +
    '</div>' +
    '<button class="btn btn-primary" id="btn-sim-cevap-goster" style="width:100%;margin-top:12px">👁️ Cevabı Gör</button>';

  el.innerHTML = html;

  document.getElementById("btn-sim-cikis").addEventListener("click", function() {
    if (confirm("Simülasyondan çıkmak istiyor musun?")) { simDurum="giris"; renderSimGiris(); }
  });

  document.getElementById("btn-sim-cevap-goster").addEventListener("click", function() {
    document.getElementById("sim-cevap-bolum").style.display = "";
    this.style.display = "none";
  });

  document.getElementById("btn-sim-dogru").addEventListener("click", async function() {
    simCevaplar.push({ soru:soru, puan:1 });
    // ilerlemeye kaydet
    if ((ilerleme.dogru||[]).indexOf(soru.id)<0) (ilerleme.dogru=ilerleme.dogru||[]).push(soru.id);
    ilerleme.yanlis = (ilerleme.yanlis||[]).filter(function(id){ return id!==soru.id; });
    try { await db.collection("mulakat_ilerleme").doc("ilerleme").set(ilerleme); } catch(e){}
    window.cacheYaz("mulakat_ilerleme", ilerleme);
    simIdx++; renderSimSoru();
  });

  document.getElementById("btn-sim-yanlis").addEventListener("click", async function() {
    simCevaplar.push({ soru:soru, puan:0 });
    if ((ilerleme.yanlis||[]).indexOf(soru.id)<0) (ilerleme.yanlis=ilerleme.yanlis||[]).push(soru.id);
    try { await db.collection("mulakat_ilerleme").doc("ilerleme").set(ilerleme); } catch(e){}
    window.cacheYaz("mulakat_ilerleme", ilerleme);
    simIdx++; renderSimSoru();
  });
}

function renderSimSonuc() {
  var el = document.getElementById("sim-icerik");
  if (!el) return;

  var dogru = simCevaplar.filter(function(c){ return c.puan===1; }).length;
  var yanlis = simCevaplar.length - dogru;
  var pct = Math.round((dogru / simCevaplar.length) * 100);
  var notHarfi = pct>=90?"A":pct>=75?"B":pct>=60?"C":pct>=50?"D":"F";
  var mesaj = pct>=90?"Mükemmel! Mülakatta çok iyi bir iz bırakırsın 🏆":
              pct>=75?"Çok iyi! Küçük eksikler var, biraz daha çalış 💪":
              pct>=60?"Orta düzey. Zayıf kaldığın konuları tekrar et 📚":
              "Daha çok çalışman gerekiyor. Devam et, olacak! 🔥";

  var html =
    '<div class="card" style="text-align:center;padding:24px">' +
      '<div style="font-size:40px;margin-bottom:8px">'+
        (pct>=75?"🏆":pct>=60?"💪":"📚")+
      '</div>' +
      '<h2 style="margin-bottom:6px">Mülakat Tamamlandı</h2>' +
      '<p style="font-size:13px;color:var(--text2);margin-bottom:16px">' + simMod.label + '</p>' +
      '<div style="font-size:48px;font-weight:700;font-family:var(--mono);color:'+(pct>=75?"var(--green)":pct>=60?"var(--yellow)":"var(--red)")+';margin-bottom:4px">'+pct+'%</div>' +
      '<div style="font-size:13px;color:var(--text2);margin-bottom:16px">Not: <strong style="font-size:18px">'+notHarfi+'</strong></div>' +
    '</div>' +
    '<div class="sim-puan-bar">' +
      '<div class="sim-puan-kutu"><div class="sim-puan-sayi yesil">'+dogru+'</div><div class="sim-puan-label">Bildim</div></div>' +
      '<div class="sim-puan-kutu"><div class="sim-puan-sayi kirmizi">'+yanlis+'</div><div class="sim-puan-label">Bilmedim</div></div>' +
      '<div class="sim-puan-kutu"><div class="sim-puan-sayi mavi">'+simCevaplar.length+'</div><div class="sim-puan-label">Toplam Soru</div></div>' +
    '</div>' +
    '<div class="card" style="margin-top:4px"><p style="font-size:14px;font-weight:500;margin-bottom:12px">'+mesaj+'</p></div>' +
    '<p class="label" style="margin:14px 0 8px">Soru Özeti</p>' +
    '<div class="sim-sonuc-liste">';

  simCevaplar.forEach(function(c) {
    html +=
      '<div class="sim-sonuc-item">' +
        '<span class="sim-sonuc-emoji">'+(c.puan?"✅":"❌")+'</span>' +
        '<span class="sim-sonuc-soru">'+escHTML(c.soru.soru)+'</span>' +
        '<span class="sim-sonuc-puan" style="color:'+(c.puan?"var(--green)":"var(--red)")+'">'+(c.puan?"✓":"✗")+'</span>' +
      '</div>';
  });

  html += '</div>' +
    '<div class="btn-row" style="margin-top:16px">' +
      '<button class="btn btn-primary" id="btn-sim-yeniden">🔄 Tekrar Yap</button>' +
      '<button class="btn btn-ghost" id="btn-sim-menu">← Menüye Dön</button>' +
    '</div>';

  el.innerHTML = html;

  document.getElementById("btn-sim-yeniden").addEventListener("click", function() { simBaslat(); });
  document.getElementById("btn-sim-menu").addEventListener("click", function() { simDurum="giris"; renderSimGiris(); });
}

// ════════════════════════════════════════════════════════════
// MÜLAKAT REHBERİ
// ════════════════════════════════════════════════════════════
var REHBER_BOLUMLER = [
  {
    id:"giris",
    icon:"🚪",
    baslik:"Mülakata Giriş ve İlk Dakikalar",
    icerik: [
      { tip:"onemi", metin:"Mülakat komisyonu ilk önce sizi ne kadar tanıyıp tanımadığınız konusunda bilgi almak ister. İlk izlenim belirleyicidir." },
      { tip:"madde", icon:"✅", metin:"Kapıyı nazikçe vurun, izin alarak girin." },
      { tip:"madde", icon:"✅", metin:"Hafif bir gülümsemeyle 'Kolay gelsin efendim' veya 'Merhaba efendim' diyerek girin." },
      { tip:"madde", icon:"✅", metin:"İçeri girince komisyon heyetinin karşısında ayakta bekleyin; sandalyeye oturmanızı söyleyene kadar oturmayın." },
      { tip:"madde", icon:"✅", metin:"Çağrıldığınızda heyecan yapmadan sakin bir şekilde girin." },
      { tip:"uyari", metin:"Kesinlikle girince direk gidip sandalyeye oturmayın; bu büyük bir kural ihlalidir." },
      { tip:"ipucu", metin:"Oturduğunuzda sırtınız dik olsun; kollarınızı masaya veya dize doğal şekilde koyun." },
    ]
  },
  {
    id:"kiyafet",
    icon:"👔",
    baslik:"Kılık-Kıyafet Kuralları",
    icerik: [
      { tip:"onemi", metin:"Kıyafet ve görünüm, komisyona profesyonellik ve ciddiyetinizi yansıtır." },
      { tip:"madde", icon:"👔", metin:"Lacivert veya gri, iki parçadan oluşan resmi takım elbise tercih edin." },
      { tip:"madde", icon:"👔", metin:"İçine beyaz ya da pastel renkli resmi gömlek giyin." },
      { tip:"madde", icon:"👠", metin:"Temiz ve yeni boyanmış resmi ayakkabı; erkekler için siyah bağcıklı." },
      { tip:"madde", icon:"💈", metin:"Saçlar bakımlı ve temiz; erkeklerde kısa saç, sakalsız görünüm tercih edilir." },
      { tip:"madde", icon:"💅", metin:"Tırnaklar temiz; çok az parfüm veya kolonya kullanın." },
      { tip:"madde", icon:"🔇", metin:"Ceplerinizde ses çıkarabilecek anahtar, bozuk para gibi şeyler olmasın." },
      { tip:"uyari", metin:"Dikkat çekici aksesuar, küpe (erkekler için yasak), ve aşırı parfümden kesinlikle kaçının." },
      { tip:"ipucu", metin:"Sürprizlere karşı mülakat yerine yarım saat — bir saat erken gidin." },
    ]
  },
  {
    id:"beden",
    icon:"🤝",
    baslik:"Beden Dili ve Uslup",
    icerik: [
      { tip:"madde", icon:"👀", metin:"Konuşma boyunca iyi bir göz teması kurun; kaçamak bakışlar güvensizlik izlenimi verir." },
      { tip:"madde", icon:"🗣️", metin:"Kısa ve net cevaplar verin; soru bitmeden atlamayın, komisyon üyesinin sorusunun tamamını dinleyin." },
      { tip:"madde", icon:"🧘", metin:"Ne aşırı rahat olun ne de fazla gergin; dengeli bir duruş sergileyin." },
      { tip:"madde", icon:"🙂", metin:"Olumsuz sorulara olumlu yanıtlar verin; paniklemeden bilmediğinizi açıkça söyleyin." },
      { tip:"madde", icon:"⏱️", metin:"Cevap vermeden önce bir an düşünebilirsiniz; aceleyle yanlış cevap vermek kadar kötü bir şey yoktur." },
      { tip:"uyari", metin:"Komisyon üyelerine saçma gelen sorular sorabilir — bu tepkinizi ölçmek içindir. Aşırı tepki vermeyiniz." },
      { tip:"ipucu", metin:"Bilmiyorsanız 'Bilmiyorum efendim, ama araştırıp öğreneceğim' deyin. Bu dürüstlük artı puandır." },
    ]
  },
  {
    id:"sorular",
    icon:"❓",
    baslik:"En Çok Sorulan Mülakat Soruları",
    icerik: [
      { tip:"onemi", metin:"Komisyon ilk olarak sizi tanımak ister. Bu sorulara hazırlıklı olun." },
      { tip:"madde", icon:"❓", metin:"Kendinizi kısaca tanıtın." },
      { tip:"madde", icon:"❓", metin:"Neden bu mesleği seçiyorsunuz?" },
      { tip:"madde", icon:"❓", metin:"Güçlü ve zayıf yönleriniz nelerdir?" },
      { tip:"madde", icon:"❓", metin:"Bu göreve atanırsanız kuruma ne katkı sağlayacaksınız?" },
      { tip:"madde", icon:"❓", metin:"Nerelisiniz? Memleketinizin ismi nereden geliyor?" },
      { tip:"madde", icon:"❓", metin:"Profesyonel hayattaki amaç ve hedefleriniz nelerdir?" },
      { tip:"madde", icon:"❓", metin:"Bu meslekle ilgili tecrübeleriniz nelerdir?" },
      { tip:"madde", icon:"❓", metin:"Bu kadroya atanmada birinci amacınız nedir?" },
      { tip:"ipucu", metin:"Kendinizle ilgili sorulara kararlı ve bilinçli cevap vermek size büyük avantaj sağlar." },
    ]
  },
  {
    id:"neden",
    icon:"🎯",
    baslik:"'Neden Uzman Erbaş Olmak İstiyorsunuz?' Cevap Rehberi",
    icerik: [
      { tip:"onemi", metin:"Bu soru mülakatın en kritik sorusudur. Samimi, özgün ve dürüst cevap verin." },
      { tip:"madde", icon:"🇹🇷", metin:"Vatanıma ve miletime hizmet etmek en büyük motivasyon kaynağım." },
      { tip:"madde", icon:"⚔️", metin:"Disiplinli ve düzenli bir yaşam tarzı benim için idealdir; askerlik bu yapıya en uygun kariyerdir." },
      { tip:"madde", icon:"🏅", metin:"Kariyer güvencesi ve mesleki gelişim imkânları bu kadroyu çekici kılmaktadır." },
      { tip:"madde", icon:"🤝", metin:"Ekip çalışması ve hiyerarşik düzene saygı kişiliğimin temel parçası." },
      { tip:"uyari", metin:"'Maaş için' veya 'başka iş bulamadım' gibi cevaplardan kesinlikle kaçının." },
    ]
  },
  {
    id:"rutbeler",
    icon:"🎖️",
    baslik:"TSK Rütbe Sistemi",
    icerik: [
      { tip:"onemi", metin:"Rütbe hiyerarşisini bilmek, askeri ortama uyum sağladığınızı gösterir." },
    ],
    ozel: "rutbeler"
  },
  {
    id:"msb_yapi",
    icon:"🏛️",
    baslik:"MSB Teşkilat Yapısı",
    icerik: [
      { tip:"onemi", metin:"Başvurduğunuz kurumu tanımak, komisyona hazırlıklı geldiğinizi gösterir." },
      { tip:"madde", icon:"📌", metin:"MSB'nin teşkilat yapısı 1 sayılı Cumhurbaşkanlığı Kararnamesi ile düzenlenmiştir." },
      { tip:"madde", icon:"📌", metin:"Merkez, taşra ve yurt dışı teşkilatından oluşur." },
      { tip:"madde", icon:"📌", metin:"MSB Bakanı: Yaşar Güler." },
      { tip:"madde", icon:"📌", metin:"Genelkurmay Başkanı: Org. Selçuk Bayraktaroğlu." },
      { tip:"madde", icon:"📌", metin:"MSÜ Rektörü: Prof. Dr. Erhan Afyoncu." },
      { tip:"madde", icon:"📌", metin:"Merkez teşkilatı: 12 Genel Müdürlük + Teftiş Kurulu Başkanlığı + çeşitli daire başkanlıkları." },
      { tip:"madde", icon:"📌", metin:"Bağlı kuruluşlar: Harita Genel Müdürlüğü, ANT İşletme Başkanlığı, MSÜ." },
      { tip:"ipucu", metin:"ASAL (Askeralma GM): Askerlik yükümlülüğü işlemleri. Tersaneler GM: Deniz Kuvvetleri'ne gemi inşa ve bakım." },
    ]
  },
  {
    id:"sonu",
    icon:"🏁",
    baslik:"Mülakat Sonu ve Çıkış",
    icerik: [
      { tip:"onemi", metin:"Mülakatın son dakikaları da ilk dakikalar kadar önemlidir; pozitif bir izlenim bırakarak ayrılın." },
      { tip:"madde", icon:"✅", metin:"Soruların bittiğini anlayınca teşekkür edin: 'Verdiğiniz zaman için teşekkür ederim efendim.'" },
      { tip:"madde", icon:"✅", metin:"Ayağa kalkmadan önce izin isteyin; sandalyeyi gürültü çıkarmadan kaldırın." },
      { tip:"madde", icon:"✅", metin:"Kapıya doğru yürürken sırtınızı komisyona dönmeyin; yarı dönerek kapıya doğru çekilin." },
      { tip:"madde", icon:"✅", metin:"Çıkarken kapıyı sessizce kapatın." },
      { tip:"ipucu", metin:"Güçlü bir son izlenim bırakmak için çıkışa kadar ciddi ve saygılı duruşunuzu koruyun." },
      { tip:"uyari", metin:"Sonuç ne olursa olsun odadan çıkana kadar pozitif ve sakin kalın; komisyon sizi izlemeye devam edebilir." },
    ]
  },
];

var RUTBE_LISTESI = [
  { no:1, isim:"Er", kat:"Er/Erbaş", vurgulu:false },
  { no:2, isim:"Onbaşı", kat:"Erbaş", vurgulu:true },
  { no:3, isim:"Çavuş", kat:"Erbaş", vurgulu:true },
  { no:4, isim:"Uzman Onbaşı", kat:"Uzman Erbaş ⭐", vurgulu:true },
  { no:5, isim:"Uzman Çavuş", kat:"Uzman Erbaş ⭐", vurgulu:true },
  { no:6, isim:"Ast.Çavuş", kat:"Astsubay", vurgulu:false },
  { no:7, isim:"Ast.Üstçavuş", kat:"Astsubay", vurgulu:false },
  { no:8, isim:"Ast.Kd.Üstçavuş", kat:"Astsubay", vurgulu:false },
  { no:9, isim:"Ast.Başçavuş", kat:"Astsubay", vurgulu:false },
  { no:10, isim:"Ast.Kd.Başçavuş", kat:"Astsubay", vurgulu:false },
  { no:11, isim:"Asteğmen", kat:"Subay", vurgulu:false },
  { no:12, isim:"Teğmen", kat:"Subay", vurgulu:false },
  { no:13, isim:"Üsteğmen", kat:"Subay", vurgulu:false },
  { no:14, isim:"Yüzbaşı", kat:"Subay", vurgulu:false },
  { no:15, isim:"Binbaşı", kat:"Subay", vurgulu:false },
  { no:16, isim:"Yarbay", kat:"Subay", vurgulu:false },
  { no:17, isim:"Albay", kat:"Subay", vurgulu:false },
  { no:18, isim:"Tuğgeneral / Tuğamiral", kat:"General/Amiral", vurgulu:false },
  { no:19, isim:"Tümgeneral / Tümamiral", kat:"General/Amiral", vurgulu:false },
  { no:20, isim:"Korgeneral / Koramiral", kat:"General/Amiral", vurgulu:false },
  { no:21, isim:"Orgeneral / Oramiral", kat:"General/Amiral", vurgulu:false },
  { no:22, isim:"Mareşal", kat:"En Üst Rütbe 🏆", vurgulu:false },
];

function renderRehber() {
  var el = document.getElementById("rehber-mulakat-icerik");
  if (!el) return;

  var html = "";
  REHBER_BOLUMLER.forEach(function(bolum) {
    html += '<div class="rehber-bolum" id="rb-'+bolum.id+'">' +
      '<div class="rehber-bolum-baslik" data-bolum="'+bolum.id+'">' +
        '<span class="rehber-bolum-icon">'+bolum.icon+'</span>' +
        '<h3>'+bolum.baslik+'</h3>' +
        '<span class="rehber-bolum-ok">▼</span>' +
      '</div>' +
      '<div class="rehber-bolum-icerik">';

    bolum.icerik.forEach(function(m) {
      if (m.tip === "onemi")       html += '<div class="rehber-onemi">'+m.metin+'</div>';
      else if (m.tip === "uyari") html += '<div class="rehber-uyari">⚠️ '+m.metin+'</div>';
      else if (m.tip === "ipucu") html += '<div class="rehber-ipucu">💡 '+m.metin+'</div>';
      else html += '<div class="rehber-madde"><span class="rehber-madde-icon">'+m.icon+'</span><span>'+m.metin+'</span></div>';
    });

    // Özel içerik: rütbe tablosu
    if (bolum.ozel === "rutbeler") {
      html += '<div class="tsk-hiyerarsi">';
      RUTBE_LISTESI.forEach(function(r) {
        html += '<div class="tsk-rutbe-satir'+(r.vurgulu?" vurgulu":"")+'">' +
          '<span class="tsk-rutbe-no">'+r.no+'</span>' +
          '<span class="tsk-rutbe-isim">'+r.isim+'</span>' +
          '<span class="tsk-rutbe-kat">'+r.kat+'</span>' +
        '</div>';
      });
      html += '</div>';
    }

    html += '</div></div>';
  });

  el.innerHTML = html;

  // Akordeon
  el.querySelectorAll(".rehber-bolum-baslik").forEach(function(baslik) {
    baslik.addEventListener("click", function() {
      var bolum = baslik.closest(".rehber-bolum");
      bolum.classList.toggle("acik");
    });
  });

  // İlk bölümü açık başlat
  var ilk = el.querySelector(".rehber-bolum");
  if (ilk) ilk.classList.add("acik");
}

// Yardımcı
function escHTML(s) {
  return (s||"").replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;");
}
