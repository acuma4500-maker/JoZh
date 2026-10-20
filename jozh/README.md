# JOZH — Kişisel Yaşam Paneli (v1.4.0)

JOZH tek kullanıcılı, kişisel bir yaşam panelidir. İçinde profil, sevdiğim kadın, günlük, hayaller ve hedefler, planlar ve seyahatler, takvim, hızlı notlar, **gelir ve gider**, Gizli Kasa, yedekleme ve ayarlar bulunur.

- Uygulama 4 haneli PIN ile açılır. E-posta, şifre ya da hesap yoktur.
- Bütün veriler önce cihazdaki IndexedDB'ye yazılır. Bulut senkronizasyonu isteğe bağlıdır; Firebase'den yalnızca **Firestore** kullanılır.
- Ana ekrana eklenebilir (PWA) ve bir kez açıldıktan sonra internet olmadan da açılır.
- HTML5, CSS3 ve düz JavaScript (ES modülleri) ile yazıldı. Framework ya da derleme aracı yoktur.

---

## 1. Yayınlama (HTTPS zorunlu)

PIN ekranı, Gizli Kasa ve yedek şifrelemesi tarayıcının Web Crypto özelliğini kullanır. Çevrimdışı çalışma için de Service Worker gerekir. İkisi de **yalnızca HTTPS'te** (ya da bilgisayarda `localhost`'ta) çalışır. Uygulama HTTP ile açılırsa bunu söyleyen bir uyarı gösterir.

Bu klasörün (`jozh/`) içeriğini olduğu gibi yayınlaman yeterli. Bütün yollar göreli olduğu için alt klasörde de çalışır.

**Seçenek A: Firebase Hosting (önerilen; kurallar da buradan yayınlanır)**

```bash
npm install -g firebase-tools
firebase login
cd jozh
firebase use jozh-pro
firebase deploy --only hosting,firestore:rules
```

`firebase.json` dosyası `tests/`, kurallar ve README hariç her şeyi yayınlar. `sw.js`, `manifest.json`, `.html`, `.js` ve `.css` dosyaları için `Cache-Control: no-cache` ve güvenlik başlıkları ekler.

**Seçenek B: GitHub Pages.** Depo ayarlarından Pages'i aç. Uygulama `https://<kullanıcı>.github.io/<depo>/jozh/` adresinde çalışır. Bu durumda Firestore kurallarını ayrıca yayınlaman gerekir (bkz. 2. adım).

**Bilgisayarda deneme:** `cd jozh && npx http-server -p 8080 -c-1`, sonra `http://localhost:8080` adresini aç.

## 2. Firestore'u oluştur ve kuralları yayınla (yalnızca senkronizasyon için)

Senkronizasyonu kullanmayacaksan bu adımı atlayabilirsin; uygulama yalnızca cihazda eksiksiz çalışır.

1. [Firebase Console](https://console.firebase.google.com) → **jozh-pro** projesi → **Firestore Database** → **Create database**. Konum olarak `eur3` ya da yakın bir bölge seç, **production mode** ile başlat.
2. Kuralları yayınla. İki yol var:
   - `firebase deploy --only firestore:rules`
   - ya da Console → Firestore → **Rules** sekmesine `firestore.rules` dosyasının içeriğini yapıştırıp **Publish**'e bas.
3. Uygulamada **Ayarlar → Firebase bağlantısını dene** düğmesine bas. "kurallar yayınlanmamış" uyarısı çıkarsa 2. adımı tekrarla.

Authentication, Storage ve Analytics **kullanılmaz**; bunları açmana gerek yok. `apiKey` bir parola değildir; erişimi kurallar belirler.

## 3. İlk kullanım

1. **Açılış PIN'i:** İlk açılışta 4 haneli PIN'ini iki kez tuşla. Aynı ya da ardışık rakamlar (1111, 1234, 9876…) kabul edilmez. PIN kurtarılamaz.
   - 5 yanlış denemeden sonra bekleme başlar: 30 sn, sonra her yanlışta iki katı (en çok 1 saat). Sayfayı yenilemek süreyi sıfırlamaz.
   - Sayfalar arasında gezerken PIN tekrar sorulmaz. Uygulama kapanınca, yeni sekmede ya da 10 dakika işlem yapılmayınca kilitlenir. Menüdeki **Kilitle** düğmesi hemen kilitler.
2. **Ana ekrana ekle:** iPhone'da Safari → **Paylaş** → **Ana Ekrana Ekle**. Android/Chrome'da **Ayarlar → Uygulamayı yükle**. Sonra **Ayarlar → Kalıcı depolama iste** düğmesine bas; bu, Safari'nin verileri kendiliğinden silmesini önler.
3. **Gizli Kasa:** Menü → **Gizli Kasa**. Açılış PIN'inden farklı 4 haneli bir kasa PIN'i belirle.
4. **Senkronizasyon anahtarı (isteğe bağlı):** **Ayarlar → Senkronizasyonu aç**. 26 karakterlik anahtar üretilir.
   - Anahtar bir paroladır; kimseyle paylaşma.
   - Başka cihazda **Ayarlar → Bu anahtarla bağlan** ile aynı verileri alırsın.
5. **İlk yedek:** **Yedekleme** sayfasında en az 10 karakterlik bir yedek parolasıyla yedek al ve dosyayı (ör. iCloud Drive'a) kaydet. Fotoğrafları ve Gizli Kasa'yı yeni telefona taşımanın **tek yolu** budur.

## 4. Gelir ve gider

Bu sayfa üç soruya cevap verir: **Bu ay ne kadar geldi?**, **Para nereye ne kadar gitti?**, **Cebimde ne var?**

- **Gelir ekle / Gider ekle:** tutar, kategori, tarih, hesap (Nakit / Banka / Kredi kartı) ve açıklama girilir. Tutarlar Türkçe yazılır: `1.500` = 1500, `2.750,50` = 2750,5.
- **Bu ay gelen / giden / ay farkı:** Seçili ayın toplamları. Gideri geçen ayla da karşılaştırır.
- **Para nereye gitti:** Giderlerin kategorilere göre dağılımı, tutar ve yüzdeyle.
- **Para nereden geldi:** Gelirlerin kategorilere göre dağılımı.
- **Cebimde ne var:** Bütün kayıtlardan hesaplanan nakit ve banka bakiyesi ile kullanılabilir toplam.
  - Kredi kartıyla yapılan harcamalar kart borcu olarak ayrıca gösterilir. Nakit ya da bankadan yapılan "Kart ödemesi" giderleri bu borçtan düşülür.
- **Bakiye gir:** Bir kez, şu an cebindeki ve bankandaki gerçek parayı yaz. Fark "Başlangıç bakiyesi" olarak kaydedilir ve aylık gelire ya da gidere sayılmaz.
- Önceki ve sonraki aylara geçilebilir. Hareketler tür, hesap ve aramayla süzülebilir. Her kayıt düzenlenebilir ve silindiğinde geri alınabilir.
- Sayfanın üstünde üç sekme var: **Özet**, **Grafikler**, **Birikim**.
- **Grafikler:**
  - **Son 6 ay: gelen ve giden.** Her ay için gelen (mavi) ve giden (turuncu) çubuklar, aylık ortalamalarla birlikte.
  - **Günlük harcama.** Seçili ayın her günü için toplam gider; ayrıca aylık toplam, günlük ortalama ve en çok harcanan gün.
  - Bir çubuğa dokununca ya da üzerine gelince tutarlar görünür. Her grafiğin altında **Tablo olarak göster** seçeneği var.
- **Birikim hedefleri:** Ad, hedef tutar ve isteğe bağlı hedef tarihi girilir. Her hedef için biriken tutar, ilerleme yüzdesi ve kalan tutar görünür. Hedef tarihi varsa ayda ne kadar biriktirmen gerektiği hesaplanır.
  - **Para ekle / Para çek:** "Nakit ya da bankadan düş" işaretliyse para seçilen hesaptan düşülür (çekerken hesaba eklenir).
  - Bu aktarımlar ("Birikime aktarılan", "Birikimden çekilen") aylık gelire ya da gidere sayılmaz; yalnızca bakiyeyi değiştirir.
  - "Cebimde ne var" kartında **Birikimlerde** ve **Toplam varlık** satırları da görünür.
  - Bir hareket silinirse ona bağlı bakiye kaydı da silinir.
- Kayıtlar ve birikim hedefleri senkronizasyona ve yedeğe dahildir. Ana panelde de bu ayın özeti ve toplam birikim görünür.

## 4a. Face ID ile açma

**Ayarlar → Face ID ile açma → Etkinleştir** dedikten sonra kilit ekranında **Face ID ile aç** düğmesi çıkar.
- Cihazın kendi doğrulamasını (WebAuthn/passkey) kullanır. Yüz ya da parmak izi bilgisi uygulamaya hiç gelmez; uygulama yalnızca cihazın imzasını kayıtlı açık anahtarla denetler.
- PIN her zaman yedek yöntemdir. Gizli Kasa yine kendi PIN'iyle açılır.
- Kayıt cihaza bağlıdır; yedeğe girmez. Yeni telefonda yeniden etkinleştir.

## 4b. Mülakat hazırlık (uzman çavuş)

Menü → **Mülakat hazırlık**. Beş bölüm var:
- **Çalış:** 219 soruluk banka, 8 kategori (kişisel, durum soruları, TSK, Atatürk ve Milli Mücadele, Türk tarihi, anayasa, coğrafya, güncel ve savunma sanayii).
  - Kartlar akıllı tekrar (Leitner) ile gelir: bilemediğin kart sık, bildiğin seyrek gelir. "Öğrenilen", 4. kutuya ulaşan kartlardır.
  - Kendi sorularını ekleyebilirsin; bütün bankada arama yapabilirsin.
  - "Kontrol et" işaretli cevaplar (isimler, güncel olaylar) zamanla değişebilir; resmî kaynaktan doğrula.
- **Deneme:** Seçtiğin sayıda soruyla deneme mülakatı yaparsın. Sorular sesli okunur, süre tutulur, kendine puan verirsin; zayıf sorular çalışma listesine eklenebilir.
- **Cevaplarım:** Kişisel sorulara kendi cevabını yazar, kelime sayısını ve yaklaşık konuşma süresini görürsün.
- **Fiziki:** Koşu, şınav ve mekik kayıtları, hedefler ve gelişim grafiği. Hedefleri başvuru kılavuzundaki tabloya göre gir.
- **Rehber:** Mülakat günü kontrol listesi ve mülakat odası davranış kuralları.

Notlar:
- Sorular resmî "çıkmış sorular" değildir; resmî liste yayımlanmaz. MSB mülakat kitapçığı derlemesi ve adayların sık aktardığı soru türlerinden hazırlanmıştır.
- İlerleme cihazda tutulur ve yedeğe dahildir; buluta gönderilmez.

## 4c. Antrenman (ekipmansız fiziki hazırlık)

Menü → **Antrenman**. Hiç ekipman gerekmez; yalnızca zemin ve duvar.
- **Kurulum:** Antrenman günlerini (3–5) ve bugünkü en iyi değerlerini (şınav, mekik, squat, plank, kesintisiz koşu dakikası) gir. Bilmiyorsan "Önce seviye testi yap" ile başla.
- **8 haftalık dönem:** Temel → Gelişim → ara test → Yoğun → sınav haftası. Setler senin maksimumlarından hesaplanır. 3 gün: üst vücut, aralıklı koşu, bacak + kondisyon; 4 gün: + uzun koşu; 5 gün: + komando devresi. 5. ve 8. haftanın son antrenmanı fiziki testtir.
- **Kendini ayarlayan yük:** Antrenman sonunda "Kolay / Tam kıvamında / Zor" seçersin; ilgili kas grubunun yükü %5–7 değişir. "Yapabildiğin kadar" son setlerinde beklenenden çok yaparsan maksimumun yükselir. Test sonuçları maksimumları doğrudan günceller ve Mülakat → Fiziki kayıtlarına da yazılır.
- **Antrenman yöneticisi:** Isınmadan esnemeye adım adım; süreli hareketlerde halka sayaç, dinlenmede geri sayım (+15 sn, atla, duraklat), son 3 saniyede bip, Türkçe sesli komut, ekranın kapanmaması (destekleyen tarayıcılarda). Yarıda bırakılan antrenman kaldığı adımdan sürer.
- **Rütbe ve rozetler:** Her tekrar ve süre puan kazandırır; puanla acemi erden astsubaya rütbe atlarsın. Rozetler kalıcıdır.
- **Gelişim:** maksimumların başlangıca göre değişimi, haftalık hacim grafiği, test sonuçları grafiği, 12 haftalık antrenman takvimi ve geçmiş.
- **Hareketler:** 39 hareket; doğru form, sık hatalar, kolay/zor hâli.

Notlar:
- Antrenman ekranı açık ve görünürken uygulama kilidinin 10 dakikalık süresi işlemez (uzun koşuda kilitlenmesin diye). Telefonu kilitlersen ya da başka uygulamaya geçersen süre normal işler.
- Veriler cihazda (meta `sport:*`) tutulur ve yedeğe dahildir; buluta gönderilmez.
- Program genel fiziki hazırlık içindir; sağlık sorunun varsa önce hekime danış.

## 5. Bilinen sınırlar

- **Açılış PIN'i ekranı korur.** Telefondaki kayıtlar bu PIN ile şifrelenmez; yalnızca Gizli Kasa ayrıca şifrelidir.
- **Gizli Kasa:**
  - 4 haneli PIN, cihazın dosyalarına teknik olarak erişebilen birine karşı zayıftır (10.000 olasılık).
  - PIN unutulursa kasa yalnızca sıfırlanabilir; içindekiler kaybolur.
  - Kasa açıkken çözülmüş içerik tarayıcı belleğindedir.
- **Firestore kuralları herkese açıktır** (hesap yok). Başkaları kendi rastgele anahtarlarıyla boş veri yazabilir, ama senin anahtarını bilmeden senin verine erişemez. Anahtarı bilen herkes bulut verini okuyabilir.
- **Fotoğraflar, Gizli Kasa ve taslaklar buluta gönderilmez.** Cihazlar arası taşıma yalnızca yedekle yapılır. Başka cihazda bir fotoğraf yoksa "Fotoğraf bu cihazda yok" yazar.
- **Senkronizasyon:** Aynı kayıt iki cihazda farklı değiştirilirse **Ayarlar → Çakışmalar** bölümünden hangisinin kalacağı seçilir.
- **HEIC fotoğraflar:** Yalnızca HEIC'i çözebilen tarayıcılarda (iPhone Safari) eklenebilir.
- **Safari:** Uzun süre açılmayan sitelerin verilerini silebilir. Kalıcı depolama iste ve düzenli yedek al; 30 günü geçince uygulama hatırlatır.

## 6. Dosyaların görevleri

```
jozh/
├── index.html              Açılış: kilit açıksa ana panele, değilse PIN ekranına gider (js/index.js)
├── manifest.json           PWA tanımı (ad, simgeler, renkler, standalone)
├── sw.js                   Service Worker: uygulama dosyalarını ve Firebase SDK'sını önbelleğe alır
├── firestore.rules         Firestore güvenlik kuralları (anahtarlı yol, alan doğrulaması)
├── firebase.json           Hosting + kurallar + önbellek ve güvenlik başlıkları
├── pages/                  Her sayfanın HTML'i (satır içi betik/stil yok)
├── css/
│   ├── base.css            Renk değişkenleri, sıfırlama, yazı, düğme ve form öğeleri
│   ├── themes.css          Açık tema (yalnızca değişkenler)
│   ├── layout.css          İskelet: menü, üst başlık, içerik alanı
│   ├── components.css      Kart, liste, pencere, bildirim, PIN tuş takımı, fotoğraf, durum blokları
│   ├── responsive.css      Menü modları (full / rail / drawer) ve ekran boyutları
│   └── pages/<sayfa>.css   Sayfaya özel stiller
├── js/
│   ├── boot.js             İlk boyamadan önce tema ve menü modu (klasik betik)
│   ├── index.js            index.html yönlendirmesi
│   ├── app.js              Ortak başlatıcı: HTTPS denetimi, veritabanı, kilit, menü, senkronizasyon, PWA
│   ├── router.js           Sayfa adresleri (yalnızca #new ve #change parçaları)
│   ├── navigation.js       Menü ve çekmece
│   ├── ui.js               Güvenli öğe oluşturma, bildirim, pencere, form alanları, durum blokları
│   ├── validators.js       Forma özel küçük doğrulamalar
│   ├── pwa.js              Service Worker kaydı, "Güncelle" bildirimi, yükleme, çevrimdışı durumu
│   ├── firebase/
│   │   ├── firebase-config.js   Firebase yapılandırması ve SDK sürümü (10.12.2)
│   │   ├── firestore.js         Firestore'un tek erişim noktası (dinamik import)
│   │   └── sync-manager.js      Çek/gönder turu, çakışmalar, üstel bekleme, Web Locks
│   ├── storage/
│   │   ├── local-db.js          Ham IndexedDB işlemleri ve şema sürümleri (MIGRATIONS)
│   │   ├── records.js           Kayıt kuralları + senkronizasyon kuyruğu
│   │   ├── schemas.js           Alan doğrulaması (kurallarla birebir aynı sınırlar)
│   │   ├── image-storage.js     Fotoğraf işleme (küçültme, yön, EXIF silme), Blob depolama, temizlik
│   │   ├── encryption.js        PBKDF2 + AES-256-GCM yardımcıları
│   │   ├── vault-storage.js     Gizli Kasa: DEK/KEK, şifreli içerik ve fotoğraflar, oturum aktarımı
│   │   ├── app-lock.js          Açılış PIN'i (özet), deneme sınırı, oturum
│   │   ├── sync-key.js          Senkronizasyon anahtarı üretme/biçimlendirme
│   │   └── backup-manager.js    Şifreli .jozh yedeği: oluşturma, doğrulama, geri yükleme
│   ├── components/
│   │   ├── pin-pad.js           4 haneli PIN tuş takımı (açılış ve kasa ortak)
│   │   ├── charts.js            SVG çubuk grafik (bilgi balonu, gösterge, tablo görünümü)
│   │   ├── photos.js            Fotoğraf alanı (commit/discard), görüntüleyici, avatar
│   │   ├── plan-editor.js       Plan düzenleyici (Planlar, Takvim, Ana panel)
│   │   ├── list-editor.js       Düzenlenebilir ve işaretlenebilir listeler
│   │   └── day-plans.js         Bir günün planları
│   ├── modules/<sayfa>.js       Her sayfanın kodu
│   └── utils/                   Tarih, sayı/para biçimi, kimlik, log, simge, etiket, otomatik kayıt,
│                                Türkçe adlar, plan/partner/finans hesapları
├── assets/icons/           icon-192, icon-512, icon-maskable-512, apple-touch-icon (180), favicon-32
└── tests/                  firestore.rules.test.mjs, precache-check.mjs, package.json
```

### Hangi sayfa hangi dosyaları kullanır

Her sayfa ortak olarak şunları kullanır: `base/themes/layout/components/responsive.css`, `boot.js`, `app.js`, `ui.js`, `navigation.js`, `router.js`, `pwa.js`, `local-db.js`, `app-lock.js`, `sync-manager.js`.

| Sayfa | Sayfa dosyaları | Ek olarak kullandıkları |
|---|---|---|
| index.html | – | `index.js` |
| login.html | `login.css`, `login.js` | `pin-pad.js`, `encryption.js` |
| dashboard.html | `dashboard.css`, `dashboard.js` | `records.js`, `photos.js`, `day-plans.js`, `plan-editor.js`, `plan-/partner-/finance-helpers.js` |
| profile.html | `profile.css`, `profile.js` | `records.js`, `photos.js`, `image-storage.js` |
| partner.html | `partner.css`, `partner.js` | `records.js`, `photos.js`, `list-editor.js`, `partner-helpers.js`, `tags.js` |
| diary.html | `diary.css`, `diary.js` | `records.js`, `photos.js`, `autosave.js`, `tags.js` |
| dreams.html | `dreams.css`, `dreams.js` | `records.js`, `photos.js` |
| plans.html | `plans.css`, `plans.js` | `plan-editor.js`, `list-editor.js`, `day-plans.js`, `plan-helpers.js` |
| calendar.html | `calendar.css`, `calendar.js` | `plan-editor.js`, `day-plans.js`, `plan-helpers.js` |
| notes.html | `notes.css`, `notes.js` | `records.js`, `autosave.js`, `tags.js` |
| finance.html | `finance.css`, `finance.js` | `records.js`, `finance-helpers.js`, `charts.js` |
| vault-login.html | `vault-login.css`, `vault-login.js` | `pin-pad.js`, `vault-storage.js` |
| vault.html | `vault.css`, `vault.js` | `vault-storage.js`, `photos.js` (şifreli kaynak) |
| backup.html | `backup.css`, `backup.js` | `backup-manager.js`, `validators.js` |
| settings.html | `settings.css`, `settings.js` | `sync-key.js`, `firestore.js`, `image-storage.js` |

## 7. Veri modeli

- **IndexedDB `jozh` şema sürümleri:**
  - 1: profile, partner, settings, memories, diary, dreams, plans, notes, syncQueue, meta
  - 2: images
  - 3: vault, vaultImages, vaultSession
  - 4: transactions (gelir ve gider)
  - 5: savings (birikim hedefleri)
  - Eski adımlar asla değiştirilmez; yeni ihtiyaçta `MIGRATIONS` dizisine adım eklenir.
- **Her kaydın ortak alanları:** `id` (`<önek>_<uuid>`, tek belgelilerde `main`), `createdAt`, `updatedAt`, `version`, `deleted` (geri alınabilir silme), `syncedRev` (yalnızca cihazda).
- **Firestore yolu:** `jozh/{anahtar}/{koleksiyon}/{belge}`. Koleksiyonlar: profile, settings, partner, memories, notes, diary, dreams, plans, transactions, savings.

## 8. Testler

```bash
node tests/precache-check.mjs          # sw.js APP_ASSETS listesi ↔ diskteki dosyalar, sürüm eşleşmesi
cd tests && npm install && npm run test:rules   # Firestore kural testleri (Firebase CLI + Java gerekir)
```

**Kurallar değiştiğinde** (ör. v1.2.0'da `savings` koleksiyonu eklendi) `firestore.rules` dosyasını Firebase Console → Firestore → Rules'a yeniden yapıştırıp **Publish**'e bas; yoksa yeni koleksiyonun kayıtları buluta gönderilemez.

Yeni bir dosya eklediğinde onu `sw.js` içindeki `APP_ASSETS` listesine ekle ve `VERSION` ile `js/app.js` içindeki `APP_VERSION` değerini birlikte artır.
