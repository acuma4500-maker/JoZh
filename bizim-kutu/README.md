# ❤️ Bizim Kutu

**İki kişi, bir dünya, binlerce anı.**
Cuma & İlayda için özel, gerçek zamanlı, güvenli web uygulaması — `bizimkutu.technology`

- Saf HTML + CSS + Vanilla JS (ES modülleri) — derleme gerektirmez, cPanel `public_html` içinde çalışır.
- Firebase Authentication + Cloud Firestore + Realtime Database. **Firebase Storage yok**, dosya/fotoğraf/ses yükleme yok.
- Firebase SDK (13.2.0) `js/vendor/firebase.js` içinde yerel olarak paketlenmiştir → harici CDN yok, katı CSP.
- PWA: ana ekrana eklenebilir, service worker ile hızlı açılış ve güncelleme bildirimi.

---

## İçindekiler
1. [Özellikler](#özellikler)
2. [Güvenlik modeli — önce bunu okuyun](#güvenlik-modeli)
3. [Mimari ve veri modeli](#mimari-ve-veri-modeli)
4. [Kurulum: Firebase](#kurulum-firebase)
5. [Yayınlama: İsimKaydet cPanel](#yayınlama-isimkaydet-cpanel)
6. [Canlı ortam kontrol listesi](#canlı-ortam-kontrol-listesi)
7. [Testler](#testler)
8. [Geliştirme](#geliştirme)
9. [Bilinen sınırlar](#bilinen-sınırlar)

---

## Özellikler

| Bölüm | Ne yapar | Nerede saklanır |
|---|---|---|
| Giriş | Yalnızca 4 haneli PIN (sunucuda, güvenlik kurallarıyla doğrulanır) | Auth (anonim) + `pinTry`, `secrets` |
| Ana sayfa | 22.08.2026'dan beri canlı sayaç (gün/saat/dk/sn), çevrim içi durumlar, son mesaj, son anı, yaklaşan görev, izlenecek film, oyun davetleri, günün sorusu | — |
| Sohbet | Anlık mesaj, tarih ayraçları, gönderiliyor/iletildi/cihaza ulaştı/görüldü, yazıyor…, silme, emoji, sayfalama, yeniden bağlanma | RTDB `chat/` |
| Çevrim içi | Gerçek bağlantı (`.info/connected` + `onDisconnect`), çoklu sekme/cihaz, sunucu zamanlı son görülme | RTDB `presence/` |
| Anı defteri | Başlık, tarih, açıklama, emoji; ekle/düzenle/sil; zaman çizelgesi | Firestore `memories` |
| Film & dizi | 4 kategori (İzlemek istediklerimiz, İzliyoruz, İzlediklerimiz, Favorilerimiz), tür, puan, ortak yorum | Firestore `movies` |
| Yapılacaklar | Son tarih, öncelik, tamamla, düzenle, sil; tamamlanan/bekleyen | Firestore `tasks` |
| Özel Kasamız 🔐 | Uçtan uca şifreli notlar (AES‑GCM‑256 + PBKDF2 600k), otomatik/manuel kilit, cihazda PIN ile hızlı açma | Firestore `vault`, `vaultNotes` (yalnızca şifreli) |
| Oyun merkezi | Davet → kabul/ret → canlı oyun → sonuç → tekrar oyna; bağlantı kopunca bekleme ekranı | RTDB `games/` |
| 7 oyun | XOX · Birbirimizi Ne Kadar Tanıyoruz? · Doğruluk mu Cesaret mi? · Emojiyle Anlat · Hafıza · Birlikte Hikâye · Soru Cevap (400 soru) | RTDB + Firestore (`stories`, `qaAnswers`) |
| Bildirimler | Yeni mesaj, oyun daveti, davet kabulü, yeni anı, yeni görev, görev tamamlandı; okundu/okunmadı | Firestore `notifications` |
| Profil | İsim, UID, durum, son görülme, başlangıç tarihi; tema, hareketi azalt, bildirim tercihleri, PIN, çıkış | Firestore `profiles` |

---

## Güvenlik modeli

Bu bölüm, isteğinizde "sahte güvenlik oluşturma" uyarısı yapılan üç konuyu açıkça ele alır.

### 1. Giriş: yalnızca 4 haneli PIN

Giriş ekranında sadece PIN vardır; e-posta/parola sorulmaz. Cuma'nın PIN'i Cuma'yı, İlayda'nın PIN'i İlayda'yı açar.

**Nasıl güvenli tutuluyor:**
- PIN'ler sitenin kaynak kodunda **yoktur**. Firebase'de yalnızca güvenlik kurallarının okuyabildiği `secrets/pins` kaydında durur (istemci okuyamaz/yazamaz).
- Cihaz arka planda sessizce **anonim Firebase oturumu** açar ve girilen PIN'i `pinTry/{cihaz}` kaydına yazar. Kurallar bunu gizli PIN'le **sunucuda** karşılaştırır; eşleşmezse cihaz hiçbir veriye erişemez. Tarayıcı doğru PIN'i hiçbir zaman öğrenmez.
- Her deneme sayılır; bir cihaz kimliği en fazla 10 deneme yapabilir, sayaç sıfırlanamaz/silinemez. Yeni kimlik almak Firebase'in IP başına anonim hesap sınırına takılır.
- Uygulama her açılışta ve arka plandan dönüşte (Profil'den ayarlanır) PIN ister. Çıkış yapınca cihazın oturumu kapanır.

**Dürüst sınır:** Güvenlik 4 haneli bir PIN kadardır (10.000 olasılık). Kararlı biri, deneme sınırlarına rağmen birçok IP adresi kullanarak zamanla PIN'i bulabilir. Mesajlar ve anılar için bu, PIN'i bilmeyen meraklılara karşı koruma sağlar; Özel Kasa notları ayrıca güçlü kasa parolasıyla şifrelidir.

**PIN değiştirme:** Firebase Console'da `secrets/pins` kaydını (Firestore **ve** Realtime Database, ikisinde de) güncelleyin.

> Eski e-posta/parola hesapları artık kullanılmaz; isterseniz Authentication'dan silebilirsiniz. Kişi kimlikleri (UID'ler) aynen veri anahtarı olarak kullanılmaya devam eder.

### 2. Özel Kasa (2208)

Firestore kuralları kasa notlarını yalnızca ikinize açar — ama ikiniz de zaten okuma yetkisine sahipsiniz. Bu yüzden "PIN'i arayüzde kontrol et" yaklaşımı **gizlilik sağlamaz**. Uygulanan çözüm **istemci tarafı şifreleme**dir:

| Katman | Ayrıntı |
|---|---|
| Sır | İkinizin birlikte belirlediği **kasa parolası** (en az 10 karakter, güç ölçerli). 4 haneli PIN şifreleme sırrı olarak **reddedilir**. |
| Anahtar türetme | PBKDF2‑SHA256, **600.000 tur**, 16 bayt rastgele tuz |
| Şifreleme | AES‑GCM‑256, her not için rastgele 96 bit IV, not kimliği AAD olarak bağlı (şifreli metin başka belgeye taşınamaz, kurcalama tespit edilir) |
| Sunucuda | Yalnızca `{v, iv, ct}` + kim/ne zaman. Başlık dahil düz metin yok; kurallar düz metin alanlarını şema gereği reddeder |
| Parola doğrulama | Sunucuya parola gitmez; şifreli bir "kontrol bloğu" yerelde çözülür |
| PIN (2208) | **Yalnızca bu cihazda hızlı açma**: parola ile bir kez açtıktan sonra dışa aktarılamaz (`extractable:false`) anahtar IndexedDB'de saklanır, PIN bu yerel anahtarın kilidini açar; 3 hatada cihazdaki anahtar silinir |
| Kilit | 3 dk hareketsizlikte, sekme gizlenince, sayfadan çıkınca ve "Kilitle" ile; anahtar bellekten silinir, notlar DOM'dan kaldırılır |

**Bunun koruduğu:** Firebase yöneticisi/veritabanı sızıntısı, çalınan Firebase oturumu, ekranı açık bırakılan telefonda kasa.
**Korumadığı:** Kasa parolasını bilen ya da "hızlı açma" etkin cihazın kilidini açabilen biri. **Parolayı unutursanız notlar kurtarılamaz.**

### 3. Oyun hamleleri

- Tüm hamleler RTDB **işlemleriyle (transaction)** yazılır → eşzamanlı hamleler çakışmaz.
- Kurallar: yalnızca iki oyuncu oturumu okur/yazar; davetleri yalnızca alıcı kabul eder; `game`, `host`, `players`, `createdAt` değiştirilemez; aktif oyun silinemez; "oyundayım" bilgisini herkes yalnızca kendisi için yazar; skorlar yalnızca 1 artabilir.
- **XOX** kurallarla tam denetlenir: sırası olmayan oynayamaz, dolu hücreye yazılamaz, başkasının işareti konamaz, hamle sayısı atlanamaz.
- **Gizli cevaplar** (Tanıyor muyuz, Soru Cevap, Emojiyle Anlat) **commit–reveal** ile korunur: veritabanına önce yalnızca `SHA‑256(nonce:cevap)` yazılır; iki taraf da taahhüt edince cevaplar açılır ve karma doğrulanır. Böylece karşı taraf cevabı önceden okuyamaz ve sonradan değiştiremez.
- **Sınır (açıkça):** Kazananın hesaplanması istemcide yapılır. Teknik bilgisi olan bir oyuncu tarayıcı konsolundan, kuralların izin verdiği alanlarda (ör. hafıza oyununda kart dizilimini okumak) hile yapabilir. Tam sunucu otoritesi için oyun mantığı Cloud Functions'a taşınmalıdır (Blaze planı).

### Diğer önlemler
- **XSS:** Kullanıcı verisi yalnızca `textContent` ile basılır (`js/utils/helpers.js` → `h()`); `innerHTML` yalnızca uygulamanın sabit SVG ikonlarında kullanılır (statik testle denetlenir).
- **CSP:** `script-src 'self'` (+ Firebase RTDB uzun yoklama yedeği), `style-src 'self'`, `object-src 'none'`, `frame-ancestors 'none'`; `unsafe-inline`/`unsafe-eval` yok.
- **Başlıklar** (`.htaccess`): HTTPS yönlendirmesi, HSTS, `X-Frame-Options: DENY`, `nosniff`, `Referrer-Policy`, `Permissions-Policy`, `noindex`.
- **Firestore önbelleği bellek içi** → çıkıştan sonra cihazda veri kalmaz. Service worker Firebase isteklerini **asla** önbelleğe almaz.
- **Firebase `apiKey`** gizli değildir (her web uygulamasında görünür); erişimi kurallar korur. Yine de aşağıdaki adımla alan adına kısıtlayın.

---

## Mimari ve veri modeli

```
bizim-kutu/
├── index.html · manifest.json · service-worker.js · .htaccess
├── css/            variables · global · components · animations · responsive
├── js/
│   ├── app.js            kabuk, oturum akışı, global dinleyiciler, rozetler, SW güncellemesi
│   ├── firebase-config.js · constants.js · auth.js · router.js (hash) · state.js
│   ├── vendor/firebase.js   (Firebase SDK 13.2.0, yerel paket; Storage yok)
│   ├── services/   firestore · realtime (sohbet) · presence · notifications · games · crypto · keystore · pinlock
│   ├── pages/      login · home · chat · memories · movies · tasks · vault · games · play · stories · notifications · profile · more
│   ├── games/      registry · common · xox · know-me · truth-dare · emoji · memory · story(+story-data) · questions
│   └── utils/      helpers (güvenli DOM) · dates · validation · icons · ui · chat-logic · questions-data
├── data/questions.json      400 soru (8 × 50)
├── assets/icons · assets/fonts (Fraunces, Nunito — OFL)
├── firebase/   firestore.rules · database.rules.json · firestore.indexes.json
├── tests/      unit/ · rules/ · e2e/
└── tools/      build-vendor · make-zip.sh · serve · make-icons · questions_source.py
```

**Firestore** (`couples/main/...`)

| Koleksiyon | Alanlar |
|---|---|
| `memories/{id}` | title≤80, date `YYYY-MM-DD`, description≤2000, emoji, createdBy/At, updatedBy/At |
| `movies/{id}` | title≤120, kind film/dizi, genre≤40, description≤1000, status watchlist/watching/watched, favorite, rating 0‑5, comment≤1000, … |
| `tasks/{id}` | title≤120, description≤1000, dueDate, priority low/medium/high, done, doneBy, doneAt, … |
| `stories/{id}` | title, opening, text≤20000, lines[], authors{}, sessionId, createdBy/At |
| `qaAnswers/{oturum-soru}` | qid 1‑400, category, question, answers{uid: metin} (herkes yalnızca kendi anahtarını yazar) |
| `vault/config` | v, salt, iterations, check{iv,ct} |
| `vaultNotes/{id}` | v, iv, ct (+ kim/ne zaman) — düz metin yok |
| `notifications/{id}` | type, to (partner), from (ben), title≤80, body≤200, link, read, createdAt |
| `profiles/{uid}` | nickname≤24, prefs{theme, reduceMotion, notif, system, lockAfter} |

**Realtime Database**

```
presence/{uid}/connections/{bağlantı}: true   (onDisconnect ile silinir)
presence/{uid}/lastSeen: sunucu zamanı
typing/{uid}: {typing, ts}
chat/messages/{pushId}: {uid, text≤2000, ts: sunucu zamanı, deleted?}
chat/readReceipts/{uid}: {readAt, deliveredAt}   (yalnızca ileri gider)
games/invitations/{id}: {from, to, game, status, createdAt, respondedAt}
games/sessions/{id}: {game, players, host, status, round, state, here, rematch, result, …}
games/scores/{oyun}/{uid|draw}: sayı
```

> Not: `presence/{uid}` altında tek bir `online` alanı yerine bağlantı listesi kullanılır. Böylece telefon + bilgisayar aynı anda açıkken birinin kapanması kişiyi yanlışlıkla çevrim dışı göstermez.

---

## Kurulum: Firebase

1. **Authentication → Sign-in method → Anonim (Anonymous): Etkinleştir.** (PIN girişi arka planda bunu kullanır; kullanıcı görmez.)
2. **PIN'leri girin (iki yere):**
   - **Firestore Database → Veri:** `secrets` koleksiyonu → belge kimliği `pins` → iki **string** alan:
     `pt0Kmbc9rqdJekFyvA1wLItUnxw1` = Cuma'nın PIN'i, `cf6RqCRF6dPEWtSR1L9Dm2Uv4Ap1` = İlayda'nın PIN'i.
   - **Realtime Database → Veri:** kökte `secrets` → `pins` → aynı iki anahtar ve PIN'ler (metin olarak, tırnaklı: `"0000"` biçiminde).
   - PIN'ler başında 0 olsa bile **metin** olarak girilmeli (sayı değil).
   - Authorized domains: `bizimkutu.technology` (ve `www.`) ekli olmalı.
3. **Firestore Database** oluşturulmuş olmalı (üretim modu). **Rules** sekmesine `firebase/firestore.rules` içeriğini yapıştırıp *Publish*.
4. **Firestore → Indexes:** `firebase/firestore.indexes.json` içindeki 7 bileşik dizini oluşturun. En kolayı Firebase CLI:
   ```bash
   npm install            # bizim-kutu klasöründe (yalnızca geliştirici bilgisayarında)
   npx firebase login
   npx firebase deploy --only firestore:rules,firestore:indexes,database --project jozh-love
   ```
   (CLI kullanmazsanız: uygulamada bir sorgu dizin isterse tarayıcı konsolundaki bağlantı dizini tek tıkla oluşturur.)
5. **Realtime Database → Rules:** `firebase/database.rules.json` içeriğini yapıştırıp *Publish* (yukarıdaki CLI komutu bunu da yapar).
6. **Önerilen:** Google Cloud Console → *APIs & Services → Credentials* → Browser key → *Application restrictions: HTTP referrers* → `https://bizimkutu.technology/*`.

Cloud Functions **kullanılmaz** → ücretsiz **Spark** planında çalışır.

> Kuralları yayınlamadan önce adım 2'deki PIN'leri girin; aksi halde kimse giriş yapamaz.

---

## Yayınlama: İsimKaydet cPanel

1. **ZIP'i hazırlayın** (hazır arşiv: `dist/bizimkutu-public_html.zip`; yeniden üretmek için `npm run zip`).
2. **Yedek alın:** cPanel → *Dosya Yöneticisi* → `public_html` → tümünü seçin → *Compress* → `yedek-YYYYMMDD.zip` → indirin. (Ya da cPanel → *Yedekleme* → *Ana Dizin Yedeği İndir*.)
3. `public_html` içindeki eski site dosyalarını silin (ya da `eski/` klasörüne taşıyın). `.well-known` klasörüne **dokunmayın** (SSL doğrulaması için).
4. *Dosya Yöneticisi → Yükle* → `bizimkutu-public_html.zip` → yüklendikten sonra sağ tık → *Extract* → hedef `/public_html`.
   Sonuçta `public_html/index.html`, `public_html/.htaccess`, `public_html/js/…` olmalı (iç içe `public_html/public_html` **olmamalı**).
5. Gizli dosyalar görünmüyorsa: *Ayarlar → Gizli dosyaları göster* ile `.htaccess` dosyasının açıldığını kontrol edin.
6. **HTTPS:** cPanel → *SSL/TLS Status* → `bizimkutu.technology` ve `www` için **AutoSSL** sertifikası yeşil olmalı (gerekirse *Run AutoSSL*). `.htaccess` tüm `http://` isteklerini `https://`'e yönlendirir.
   - Service worker, Web Crypto ve PWA **yalnızca HTTPS'te** çalışır.
7. Tarayıcıda `https://bizimkutu.technology` açın → kontrol listesine geçin.

**Güncelleme yaparken:** yeni ZIP'i aynı şekilde açın. `make-zip.sh` service worker sürümünü otomatik değiştirir; açık olan uygulamalarda "Yeni sürüm hazır ✨ → Güncelle" çıkar.

---

## Canlı ortam kontrol listesi

Bu adımlar **sizin** tarafınızdan gerçek hesaplarla yapılmalıdır (geliştirme ortamından gerçek projeye ve parolalara erişim yoktur):

| # | Kontrol | Nasıl |
|---|---|---|
| 1 | HTTPS | `http://bizimkutu.technology` → otomatik `https://` olmalı; kilit simgesi |
| 2 | Başlıklar | Tarayıcı geliştirici araçları → Network → `index.html` → `content-security-policy`, `strict-transport-security` var mı |
| 3 | Anonim giriş + secrets | PIN ekranında "Anonim giriş kapalı" uyarısı çıkarsa Kurulum adım 1; PIN hep hatalıysa adım 2 |
| 4 | Giriş | Telefonda Cuma'nın PIN'i → Cuma; ikinci telefonda İlayda'nın PIN'i → İlayda; rastgele PIN → "PIN hatalı" |
| 5 | Firestore | Anı ekleyin; diğer telefonda anında görünmeli. "missing index" hatası çıkarsa adım 4 (dizinler) |
| 6 | RTDB | Sohbette mesaj; iki telefonda da "Çevrim içi" |
| 7 | Canlı senkron | İki cihazda: mesaj + görüldü, görev tamamla, XOX oyna |
| 8 | Bağlantı kopması | Bir telefonu uçak moduna alın → diğerinde ~1 dk içinde "Son görülme" |
| 9 | Kasa | Kasa parolasını birlikte belirleyin, not ekleyin; Firebase Console'da `vaultNotes` belgesinde yalnızca `iv/ct` olmalı |
| 10 | PWA | iPhone Safari → Paylaş → *Ana Ekrana Ekle*; Android Chrome → *Uygulamayı yükle* |

---

## Testler

| Komut | Ne test eder | Durum |
|---|---|---|
| `npm test` | 44 birim/statik test: tarih & DST, sayaç, oyun kuralları (XOX, hafıza, tanıyor muyuz, D/C, emoji, hikâye, soru seçimi), kasa şifrelemesi (yanlış parola, AAD, kurcalama, dışa aktarılamaz anahtar), sohbet durumları, doğrulama, **400 soru** (sayı, benzersizlik, benzerlik), import yolları, SW önbellek listesi, kaynakta PIN/parola yok, Storage yok, `innerHTML` ve yerel `append` denetimi, CSP | ✅ |
| `npm run test:rules` | 29 güvenlik kuralı testi **Firebase Emülatörlerinde** (Firestore + RTDB): oturumsuz/yanlış PIN'li cihaz engeli, PIN deneme sayacı (artış zorunlu, en fazla 10, silinemez), secrets okunamaz, başkasının PIN'iyle kimlik değiştirme, başkası adına yazma, şema, bildirim alıcısı, kasa düz metin reddi, soru-cevap sahipliği, XOX sıra/hücre, davet akışı, skorlar | ✅ |
| `npm run test:e2e` | İki gerçek tarayıcı (iPhone 13 + Pixel 5 öykünmesi) + Auth/Firestore/RTDB emülatörleri: PIN girişi (doğru/yanlış, e-posta alanı yok, her açılışta PIN), sayaç, presence, sohbet/görüldü/yazıyor/XSS/silme, anı/film/görev senkronu, bildirim, kasa şifreleme, 7 oyun, son görülme, çevrim dışı, kilit ekranı, çıkış, masaüstü/koyu tema — 28 adım | ✅ (art arda koşularda 28/28) |

Emülatörler Java 11+ ister. Test komutları `firebase emulators:exec` içinde çalışır.

---

## Geliştirme

```bash
cd bizim-kutu
npm install                 # yalnızca test/derleme araçları; site bunlara ihtiyaç duymaz
node tools/serve.mjs        # http://127.0.0.1:5173/  (gerçek Firebase'e bağlanır)
# Emülatörlerle: npx firebase emulators:start --only auth,firestore,database --project jozh-love
#                ve http://127.0.0.1:5173/?emulator
npm run build:vendor        # Firebase SDK'sını yeniden paketle (sürüm: package.json)
python3 tools/questions_source.py   # data/questions.json'u yeniden üret
npm run zip                 # dist/bizimkutu-public_html.zip
```

---

## Bilinen sınırlar

- **Push bildirimleri (tarayıcı kapalıyken):** Yok. Firebase Cloud Messaging + sunucu tarafı gönderici (Cloud Functions, Blaze) gerekir. Uygulama açıkken arka plandaki sekmede tarayıcı bildirimi seçeneği vardır (Profil → Bildirimler). iPhone'da bu da yalnızca ana ekrana eklenmiş uygulamada (iOS 16.4+) çalışır.
- **PIN ile giriş:** Güvenlik 4 haneli PIN kadardır (yukarıda açıklandı).
- **Oyun sonucu:** İstemcide hesaplanır; XOX dışında kurallar yalnızca katılımcı/alan düzeyinde denetler.
- **Kasa parolası unutulursa** notlar kurtarılamaz. Parola değişince tüm cihazlardaki hızlı açma sıfırlanır.
- **Eski tarayıcılar:** iOS Safari 15+ ve güncel Android Chrome hedeflenir (ES2020, `structuredClone`, Web Crypto).
