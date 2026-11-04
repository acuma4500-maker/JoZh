# JOZH STUDIOS · 81 Şehir – Bir Ticaret ve Macera Hikâyesi

Mert ve Ali'nin 81 il dizisinin bütün senaryolarını, Flow prompt'larını, kasa hesaplarını ve sosyal medya metinlerini tek yerden yöneten panel.
HTML5 + CSS3 + düz JavaScript + LocalStorage. Framework yok, Firebase yok, sunucu gerekmez: `index.html` dosyasını tarayıcıda açman yeter (internetsiz de çalışır).

## İçerik (hepsi yazılı, örnek veri yok)
- **87 video = 6 başlangıç videosu + 81 il**, her biri 6 sahne × 10 sn = **522 sahne**.
- Her sahne: başlık, Türkçe açıklama, Türkçe diyalog, 13 başlıklı tam İngilizce Flow prompt'u (VIDEO FORMAT → AVOID), sade "yeniden dene" prompt'u.
- **Sahnelerin arasında hazır kasa prompt'u** (Video 4 sahne 6'dan itibaren): azalış (kırmızı), artış (yeşil), sabit kasa. Aynı bakiyeli sabit sahneler tek klibi paylaşır.
- Her videoda: video kapağı ve **"Pek yakında" kapağı** prompt'u + görsel alanı, kasa hareketleri, TikTok başlığı ve açıklaması, Instagram açıklaması, hashtag'ler, sponsorluk iletişim metni, bölüm tanıtım metni.
- Dizi biblisi: ana hikâye, 8 sezonun açılış/hikâye/ticari hedef/şehir sırası/sezon ortası/final/geçiş bilgisi, ticaret stratejisi, karakter gelişimi.
- Karakterler: sabit İngilizce yüz/saç/vücut/ses tanımları ve kıyafetler (Bölüm 57 Düzce'de yağmur yüzünden mont; sonrası hep aynı).

## Rota (Doğu Anadolu'dan başlar)
Doğu Anadolu 14 · Güneydoğu 9 · Akdeniz 8 · Ege 8 · Marmara 11 · Karadeniz 18 · İç Anadolu 13 = 81 il. Final: 31 Aralık gecesi Ankara.

## Kasa
Başlangıç 100.000 TL (Video 4'te açılır). Her işlem bir videonun bir sahnesine bağlıdır; alış/satış adet × birim fiyatla hesaplanır.
Borç 800.000 TL yedi taksitte ödenir (50 + 80 + 100 + 120 + 150 + 150 + 150 bin). Senaryo sonu kasa: 344.300 TL.
Panelde yeni işlem eklenebilir: bakiye otomatik hesaplanır, mükerrer kayıt ve kasayı eksiye düşüren işlem engellenir, işlem anında kasa prompt'u üretilir.
Ürünler o ilin bilinen yerel ürünleridir; hikâyedeki işletmeler kurgusal ve isimsizdir; hiçbir işletme sponsor olarak gösterilmez.

## Dosya yapısı
```
jozh-studios/
├── index.html
├── css/style.css
├── js/
│   ├── app.js       arayüz, yönlendirme, prompt kurucular
│   ├── data.js      ÜRETİLİR (kaynak/build.py) — bütün içerik
│   ├── kasa.js      kasa prompt şablonu + kasa defteri
│   └── storage.js   LocalStorage, JSON dışa/içe aktarma
├── assets/{images,icons}
├── kaynak/          içeriğin kaynağı (Python): karakterler, bible, sezon dosyaları, build.py
└── tests/panel.test.cjs
```

## İçeriği değiştirmek
Senaryolar `kaynak/*.py` dosyalarındadır. Değiştirdikten sonra:
```
python3 jozh-studios/kaynak/build.py      # doğrular ve js/data.js'i yeniden yazar
node jozh-studios/tests/panel.test.cjs    # uçtan uca test (Playwright)
```
`build.py` her il tam bir kez ve doğru bölgede mi, her bölümde 6 sahne var mı, konuşan karakter sahnede mi, saatler ileri mi gidiyor,
diyalog 10 saniyeye sığıyor mu, kasa hiçbir anda eksiye düşüyor mu ve taksitler toplamı 800.000 TL mi diye kontrol eder; biri tutmazsa durur.

## Veri
Senaryolar silinmez. Senin verin (eklediğin işlemler, "üretildi" işaretleri, notlar, ayarlar, yüklediğin kapaklar) bu tarayıcının LocalStorage'ında
durur. "Veri ve yedek" sayfasından JSON olarak indirip başka cihazda içe aktarabilirsin.
