# ❤️ Bizim Kutu

**İki kişi, bir dünya, binlerce anı.**
Cuma & İlayda için özel, gerçek zamanlı web uygulaması — `bizimkutu.technology`

- Saf HTML + CSS + Vanilla JS (ES modülleri). Derleme gerekmez, cPanel `public_html` içinde çalışır.
- Firebase: Authentication (anonim, görünmez) + Cloud Firestore + Realtime Database. **Firebase Storage yok**, ücretsiz **Spark** planında çalışır.
- Firebase SDK (13.2.0) `js/vendor/firebase.js` içinde yerel olarak paketlidir; harici CDN yok, katı CSP.
- PWA: ana ekrana eklenebilir; yeni sürüm yüklenince kendini otomatik günceller.

---

## İçindekiler
1. [Özellikler](#özellikler)
2. [Giriş ve güvenlik nasıl çalışıyor](#giriş-ve-güvenlik-nasıl-çalışıyor)
3. [Firebase kurulumu](#firebase-kurulumu)
4. [Yayınlama (cPanel)](#yayınlama-cpanel)
5. [Sorun giderme](#sorun-giderme)
6. [Mimari ve veri modeli](#mimari-ve-veri-modeli)
7. [Testler](#testler)
8. [Geliştirme](#geliştirme)
9. [Bilinen sınırlar](#bilinen-sınırlar)

---

## Özellikler

| Bölüm | Ne yapar |
|---|---|
| **Giriş** | Yalnızca 4 haneli PIN. Cuma'nın PIN'i Cuma'yı, İlayda'nınki İlayda'yı açar. E-posta/parola yok. Her açılışta ve arka plandan dönüşte PIN istenir. |
| **Ana sayfa** | 22.08.2026'dan beri canlı sayaç (gün/saat/dk/sn), çevrim içi durumlar, son mesaj, oyun davetleri, son anı, yaklaşan görev, izlenecek film, günün sorusu |
| **Sohbet** | Anlık mesaj, tarih ayraçları, gönderiliyor / iletildi / cihaza ulaştı / görüldü, "yazıyor…", mesaj silme, emoji, eski mesajlar, kopunca yeniden bağlanma |
| **Çevrim içi** | Gerçek bağlantı takibi, çoklu cihaz, sunucu saatiyle son görülme |
| **Anı defteri** | Başlık, tarih, açıklama, emoji; ekle/düzenle/sil; aylara göre zaman çizelgesi |
| **Görevler** | Son tarih, öncelik, tamamla/geri al, düzenle, sil; bekleyen/tamamlanan |
| **Film & dizi** | İzlemek istediklerimiz · İzliyoruz · İzlediklerimiz · Favorilerimiz; tür, ⭐ puan, ortak yorum |
| **Bildirimler** | Yeni mesaj, oyun daveti/kabulü, yeni anı, yeni görev, görev tamamlandı; okundu/okunmadı; tür bazında açma/kapama; 14 günden eski okunmuşlar otomatik silinir |
| **Özel Kasa 🔐** | Sabit 4 haneli kasa PIN'i ile açılan şifreli gizli notlar; 3 dk hareketsizlikte ve manuel kilit |
| **Oyun Merkezi** | Davet → kabul/ret → canlı oyun → sonuç → tekrar oyna. 7 oyun: XOX · Birbirimizi Ne Kadar Tanıyoruz? · Doğruluk mu Cesaret mi? · Emojiyle Anlat · Hafıza · Birlikte Hikâye · Soru Cevap (400 soru) |
| **Profil** | İsimler, kimlikler, durumlar; tema (sistem/açık/koyu), animasyonları azalt, bildirim tercihleri, otomatik kilit süresi, çıkış |
| **Mobil** | Klavye açılınca üst çerçeve ve yazı kutusu yerinde kalır, alt menü gizlenir; çift dokunma ve iki parmakla yakınlaştırma kapalı |

---

## Giriş ve güvenlik nasıl çalışıyor

### Giriş PIN'i
1. Cihaz Firebase'e sessizce **anonim** olarak bağlanır; kullanıcı hiçbir şey görmez.
2. Girilen PIN, `pinTry/{cihaz}` kaydına yazılır.
3. **Güvenlik kuralları**, bu PIN'i yalnızca sunucunun okuyabildiği `secrets/pins` kaydıyla karşılaştırır. Eşleşirse cihaz o kişinin verilerine erişir; eşleşmezse hiçbir veriye erişemez.
4. PIN'ler sitenin kaynak kodunda **yoktur**; tarayıcı doğru PIN'i hiçbir zaman öğrenmez.
5. Her deneme sayılır; bir cihaz kimliği en fazla 10 deneme yapabilir ve sayaç silinemez.

### Kasa PIN'i
- Kasa PIN'i Firestore'daki `secrets/pins` belgesinin `vault` alanındadır.
- Girilen PIN `vaultTry/{cihaz}` kaydına yazılır; kurallar eşleşmezse kasa notlarını **okumaya izin vermez**. Telefon girişli olsa bile kasa PIN'i olmadan notlar görünmez.
- Cihaz başına 10 dakikada en fazla 10 deneme yapılabilir.
- Doğru PIN'den sonra sunucu erişimi 15 dakika geçerlidir. Ekranda kasa 3 dakika hareketsizlikte, uygulamadan çıkınca ve "Kilitle" ile kilitlenir.
- Notlar ayrıca PIN'den türetilen anahtarla (PBKDF2 600.000 tur + AES-GCM-256) cihazda şifrelenir. Firebase Console'da düz metin görünmez.

### Dürüst sınırlar
- Güvenlik **4 haneli PIN kadardır** (10.000 olasılık). Deneme sınırları rastgele birini durdurur, ama çok sayıda cihaz/IP kullanan kararlı biri zamanla PIN'i bulabilir.
- 4 haneli PIN'den türetilen kasa anahtarı, uzun bir parolaya göre zayıftır. Asıl koruma, PIN'in sunucuda doğrulanması ve deneme sınırıdır.
- Oyunlarda kazanan cihazda hesaplanır. XOX'ta sıra ve hücre kuralları sunucuda zorlanır, diğer oyunlarda kurallar yalnızca katılımcıyı denetler.

### Diğer önlemler
- **XSS:** Kullanıcı verisi yalnızca metin olarak basılır (`textContent`). `innerHTML` sadece uygulamanın sabit ikonlarında kullanılır; bu, statik testle denetlenir.
- **CSP:** `script-src 'self'`, `style-src 'self'`, `object-src 'none'`, `frame-ancestors 'none'`; `unsafe-inline` ve `unsafe-eval` yok.
- **Başlıklar** (`.htaccess`): HTTPS yönlendirmesi, HSTS, `X-Frame-Options: DENY`, `nosniff`, `Referrer-Policy`, `Permissions-Policy`, `noindex`.
- Firestore önbelleği yalnızca bellekte tutulur. Service worker Firebase isteklerini **asla** önbelleğe almaz.
- Gizli cevaplı oyunlar (Tanıyor muyuz, Soru Cevap, Emojiyle Anlat) commit–reveal kullanır: cevaplar iki taraf da cevaplamadan veritabanında okunamaz.

---

## Firebase kurulumu

Şu an canlıda yapılmış olan kurulum budur; yeni bir proje kuracaksanız aynı adımları izleyin.

1. **Authentication → Sign-in method → Anonymous:** Etkin.
   **Authorized domains:** `bizimkutu.technology` ekli.
2. **PIN'ler — iki yerde:**
   - **Firestore** → `secrets` koleksiyonu → `pins` belgesi:
     | Alan | Tür | Değer |
     |---|---|---|
     | `pt0Kmbc9rqdJekFyvA1wLItUnxw1` | string | Cuma'nın giriş PIN'i |
     | `cf6RqCRF6dPEWtSR1L9Dm2Uv4Ap1` | string | İlayda'nın giriş PIN'i |
     | `vault` | string | Kasa PIN'i |
   - **Realtime Database** → kökte `secrets` → `pins` → aynı iki kişi anahtarı ve giriş PIN'leri. `vault` burada gerekmez.
   - Kurallar yazım farklarına dayanıklıdır: tırnak, boşluk, sayı/metin farkı ve baştaki 0'ın düşmesi sorun olmaz.
3. **Realtime Database → Rules:** `firebase/database.rules.json` içeriği → Publish.
4. **Firestore → Rules:** `firebase/firestore.rules` içeriği → Publish.
5. **Dizin (index) gerekmez.** Tüm sorgular tek alanlıdır; `firestore.indexes.json` bilerek boştur.

**Firebase CLI ile kuralları tek komutla yayınlamak için** (isteğe bağlı, bilgisayarda):
```bash
cd bizim-kutu && npm install
npx firebase login
npx firebase deploy --only firestore:rules,database --project jozh-love
```

**PIN değiştirmek:** Yalnızca `secrets/pins` değerlerini güncelleyin. Giriş PIN'i iki yerde (Firestore + Realtime Database), kasa PIN'i sadece Firestore'da.
⚠️ Kasa PIN'i değişirse eski notlar yeni PIN ile çözülemez. Uygulama "Kasayı bu PIN ile yeniden kur" seçeneği sunar; bu seçenek **eski notları siler**.

> `firebase/adimlar/` klasörü, sitenin bölüm bölüm açıldığı sıradaki ara kural dosyalarıdır (1–8). Son hâli `firebase/firestore.rules` ve `firebase/database.rules.json`'dur.

---

## Yayınlama (cPanel)

1. Hazır arşiv: `dist/bizimkutu-public_html.zip`. Yeniden üretmek için: `npm run zip`.
2. cPanel → Dosya Yöneticisi → `public_html` → **Yükle** → ZIP'i seç → sağ tık → **Extract** → üzerine yaz: **evet**.
   Sonuçta `public_html/index.html`, `public_html/.htaccess`, `public_html/js/…` olmalı; iç içe `public_html/public_html` **olmamalı**.
3. Gizli dosyalar görünmüyorsa: Ayarlar → **Gizli dosyaları göster** (`.htaccess` için).
4. HTTPS: cPanel → SSL/TLS Status → AutoSSL yeşil olmalı. `.htaccess` her isteği `https://`'e yönlendirir.
5. Kontrol: PIN ekranının en altında **Sürüm: bk-…** yazar. Bu numara her ZIP'te değişir; yükledikten sonra yeni numarayı görmelisiniz. Uygulama yeni sürümü kendisi yükler.

---

## Sorun giderme

| Ekranda / belirti | Sebep | Çözüm |
|---|---|---|
| "Firebase'de Anonim giriş kapalı" | Anonymous kapalı | Kurulum 1 |
| "Realtime Database kuralları reddetti" | RTDB kuralları eski/yayınlanmamış | Kurulum 3 (Publish'e basıldığından emin olun) |
| "PIN hatalı" (doğru PIN girildiği hâlde) | RTDB'de `secrets/pins` eksik veya yanlış | Kurulum 2 |
| "Firestore kuralları yüklenmemiş" | Firestore kuralları eski | Kurulum 4 |
| "Firestore'daki secrets/pins PIN'i eşleşmiyor" | Firestore'da `secrets/pins` eksik veya yanlış | Kurulum 2 (Firestore tarafı) |
| Kasada "PIN hatalı" | Firestore `secrets/pins` içinde `vault` alanı yok | `vault` alanını ekleyin |
| Kasada "Çok fazla deneme" | 10 dakikada 10 deneme doldu | 10 dk bekleyin ya da Firestore → `vaultTry` koleksiyonunu silin |
| Bir bölüm "yetkin yok" diyor | O bölümün kuralı eksik | `firebase/firestore.rules`'un tamamını yeniden yayınlayın |
| Eski görünüm duruyor | Telefon eski sürümü çalıştırıyor | Sayfayı yenileyin; olmazsa Safari → Web Sitesi Verileri → sitenin verisini silin |

iPhone'da konsola değer yazarken: Ayarlar → Genel → Klavye → **Akıllı Noktalama** kapalı olsun; yoksa tırnaklar eğik (`“ ”`) yazılır.

---

## Mimari ve veri modeli

```
bizim-kutu/
├── index.html · manifest.json · service-worker.js · .htaccess
├── css/          variables · global · components · animations · responsive
├── js/
│   ├── app.js           kabuk, oturum akışı, global dinleyiciler, rozetler, SW güncellemesi
│   ├── auth.js          PIN girişi (anonim cihaz + pinTry)
│   ├── features.js      bölüm aç/kapa (hepsi açık)
│   ├── viewport.js      klavye/görünen alan uyumu, yakınlaştırma engeli
│   ├── firebase-config.js · constants.js · router.js (hash) · state.js
│   ├── vendor/firebase.js   (Firebase SDK, yerel paket; Storage yok)
│   ├── services/   firestore · realtime (sohbet) · presence · notifications · games · crypto
│   ├── pages/      login · home · chat · memories · movies · tasks · vault · games · play · stories · notifications · profile · more
│   ├── games/      registry · common · xox · know-me · truth-dare · emoji · memory · story(+story-data) · questions
│   └── utils/      helpers (güvenli DOM) · dates · validation · icons · ui · chat-logic · questions-data
├── data/questions.json      400 soru (8 kategori × 50)
├── assets/icons · assets/fonts (Fraunces, Nunito — OFL)
├── firebase/     firestore.rules · database.rules.json · firestore.indexes.json · adimlar/
├── tests/        unit/ · rules/ · e2e/
└── tools/        build-vendor · make-zip.sh · serve · make-icons · questions_source.py
```

**Firestore**

| Yol | İçerik |
|---|---|
| `secrets/pins` | Kişi UID'leri → giriş PIN'i, `vault` → kasa PIN'i (istemci okuyamaz) |
| `pinTry/{cihaz}` | Giriş denemesi: pin, pinText, person, n |
| `vaultTry/{cihaz}` | Kasa denemesi: pin, pinText, n, at |
| `couples/main/memories` | Anılar |
| `couples/main/tasks` | Görevler |
| `couples/main/movies` | Film & dizi |
| `couples/main/notifications` | Bildirimler (to/from) |
| `couples/main/profiles/{kişi}` | Takma ad, tercihler |
| `couples/main/stories` | Kaydedilen hikâyeler |
| `couples/main/qaAnswers` | Soru Cevap geçmişi (herkes yalnızca kendi cevabını yazar) |
| `couples/main/vault/config` | Kasa anahtar tuzu ve doğrulama bloğu |
| `couples/main/vaultNotes` | Şifreli notlar (yalnızca iv/ct) |

**Realtime Database:** `secrets/pins`, `pinTry`, `presence`, `typing`, `chat/messages`, `chat/readReceipts`, `games/invitations`, `games/sessions`, `games/scores`.

Kişi kimlikleri (Cuma `pt0Kmbc9…`, İlayda `cf6RqCRF…`) veri anahtarı olarak kullanılır. Hangi cihazın hangi kişi olduğunu kurallar PIN üzerinden belirler.

---

## Testler

| Komut | Kapsam | Son sonuç |
|---|---|---|
| `npm test` | 44 birim/statik test: tarih & yaz/kış saati, oyun kuralları, şifreleme, sohbet durumları, doğrulama, 400 soru (sayı/benzersizlik/benzerlik), import yolları, SW listesi, kaynakta PIN yok, Storage yok, `innerHTML` ve `append` denetimi, CSP | ✅ 44/44 |
| `npm run test:rules` | Firebase emülatörlerinde güvenlik kuralları: yanlış PIN'li cihaz engeli, PIN deneme sayaçları, secrets okunamaz, yazım farklarına dayanıklı PIN eşleşmesi, kasa PIN'i, başkası adına yazma, şema, XOX sıra/hücre, davetler, skorlar | ✅ 31/31 |
| `npm run test:e2e` | İki tarayıcı (iPhone 13 + Pixel 5 öykünmesi) + Auth/Firestore/RTDB emülatörleri, tüm bölümler | ✅ 28/28 |
| `tests/e2e/adim1…8.mjs` | Her adımı yalnızca o adımın kurallarıyla test eder (`firebase.adimN.json`) | ✅ adım 8: 32/32 |

Testlerde gerçek PIN'ler kullanılmaz. Emülatörler Java 11+ ister.

---

## Geliştirme

```bash
cd bizim-kutu
npm install                 # yalnızca test/derleme araçları; site bunlara ihtiyaç duymaz
node tools/serve.mjs        # http://127.0.0.1:5173/ (gerçek Firebase'e bağlanır)
npx firebase emulators:start --only auth,firestore,database --project jozh-love
#                           # ve http://127.0.0.1:5173/?emulator (emülatöre bağlanır)
npm run build:vendor        # Firebase SDK'sını yeniden paketle
python3 tools/questions_source.py   # data/questions.json'u yeniden üret
npm run zip                 # dist/bizimkutu-public_html.zip (sürüm numarası otomatik)
```

Yeni bir bölüm eklerken kapalı başlatmak için `js/features.js` kullanılabilir.

---

## Bilinen sınırlar

- **Push bildirimi yok:** Telefon kilitliyken ya da uygulama kapalıyken bildirim gelmez. Bunun için Firebase **Blaze** planı + Cloud Functions gerekir.
- **Fotoğraf/ses/video yok:** Kasaya medya ekleme denendi, kullanıcı isteğiyle kaldırıldı. Kasa yalnızca yazılı not tutar.
- **PIN güvenliği:** 4 hane ile sınırlıdır (yukarıda açıklandı). Gerçek sunucu tarafı deneme sınırı için Cloud Functions (Blaze) gerekir.
- **Kasa PIN'i değişirse** eski notlar açılamaz (sıfırlama eski notları siler).
- **Eski tarayıcılar:** iOS Safari 15.4+ ve güncel Android Chrome hedeflenir.
