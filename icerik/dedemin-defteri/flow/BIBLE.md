# Dedemin Defteri: sahne yazım defteri

Bu dosya, sahneleri yazarken uyulan kuralları tutar. Yeni bir bölüm yazmadan önce oku.

## Flow için 10 kural (kullanıcının listesi) ve bu projedeki karşılığı

1. **Sahneyi net tanımla** → her prompt'ta LOCATION, TIME AND LIGHT, ACTION satırları ayrı ayrı yazılır.
2. **Kamera hareketini belirt** → her sahnede `kam` zorunlu. Tek hareket: dolly-in, pan, tilt, tracking, static, over-the-shoulder.
3. **Işığı sabit tut** → `z` alanında saat + evre ("07:10 şafak"). Evre metni tek yerden (build.py `FAZ`) gelir, aynı evre aynı ışık cümlesini alır. Hava bölüm başında (`hava`) verilir.
4. **Karakteri tutarlı anlat** → karakter tarifleri karakterler.py'dedir, aynen eklenir. Kıyafet hiç değişmez.
5. **Fizik kurallarını unutma** → eylem tek ve gerçekçi: taşıma, uzatma, oturma. Prompt'a sabit PHYSICS satırı eklenir.
6. **Arka planı sadeleştir** → kalabalık yok. En çok 2-3 uzak, bulanık figür. BACKGROUND satırı sabit.
7. **Kısa planlarla başla** → 8 sn, tek çekim, tek eylem. Bir bölüm 6 sahne.
8. **Yüz ve el detaylarını kontrol et** → eller tek nesne tutar, AVOID satırında bozulmalar yazılı, sayfada kontrol listesi var.
9. **Ses ve dudak uyumunu düşün** → sahne başına en çok ~18 kelime, en çok 2 replik. Telefon sesi için konuşan görünmez, dinleyenin dudağı kapalı.
10. **İlk çıktıyla yetinme** → her sahnenin yanında "yeniden dene" için sadeleştirilmiş prompt var (tek karakter, sabit kamera, tek eylem).

## Zaman

- **Gün N = Bölüm N.** 100 bölüm = 100 gün.
- Mevsim: Gün 1-60 kış, 61-80 kış sonu, 81-100 ilkbahar. Tarih verilmez (Ramazan, bayram çakışmasın).
- Mahkeme: B36'da "60 gün sonra" (Gün 96). B82'de öne alınır, "8 gün kaldı" (Gün 90). B90 Ankara'da görülür.
- 1979: Rıza 31, Cevdet 35, Yaşar 15 yaşındaydı. Şimdi 2026: Rıza ölmeden önce 78, Cevdet 82, Yaşar 62, Selim 45.
- B1 akşam 17:40 → gece 22:30. B2 B1'in aynı gecesiyle başlar (22:50). B3 Kayseri'de cenaze günü.

## Günlük ritim (bölüm 4'ten itibaren)

| Sahne | Saat | Ne olur | Kasa olayı |
|---|---|---|---|
| 1 | erken sabah | şehre varış, kuruluş çekimi, önceki cliffhanger'ın devamı | yol (y) |
| 2 | sabah | önceki şehirden gelen malı satış | satış (s) |
| 3 | öğle | öğle yemeği + o ilin kültürü (kısa, doğal) | masraf (m) |
| 4 | öğleden sonra | tarihî/kültürel mekân, defterden öğüt, ipucu | - |
| 5 | ikindi, gün batımı | üreticiden alış | alış (a) |
| 6 | akşam, gece | cliffhanger | - |

Ritim kalıp değildir; iş günü, sabotaj, yolculuk günü olursa bozulur. Saatler bir bölüm içinde hep artar (anı sahneleri hariç).

## Defter sayfası

Her şehir için defterde bir sayfa var: Rıza'nın tek cümlelik öğüdü. Kerem Sc4'te (ya da Sc3'te) sayfayı açar, öğüdü sesli okur. Öğüt o günün olayıyla ilgili olur.

## Para

- Tüm tutarlar sezon1.py'dan gelir. Diyalogda ve metinde `{satis}`, `{alis}`, `{yol}`, `{masraf}`, `{acilis}`, `{kapanis}`, `{stok}`, `{kar}`, `{kasa_s}`, `{kasa_m}`, `{kasa_a}` kullanılır.
  - diyalogda yazıya çevrilir ("on üç bin yedi yüz elli"), yani `"{satis} lira"` yazılır.
  - `tr` ve `kurgu` içinde rakam olur ("13.750"), yani `"{satis} ₺"` yazılır.
  - `en` içinde "13,750" olur.
- `kasa=dict(y=0, s=1, m=2, a=4)` olay hangi sahnede olur (0'dan başlar). Tutar 0 ise olay yok.
- B4'te kasa 3. sahnede (indeks 3) 0 → 5.000 olur: `kasa_baslar=3`.
- B1-B3'te kasa yok.

## Sahne yazma biçimi

```python
S("07:10 şafak", "A", ["kerem", "elif"],
  "Türkçe özet: ne olur, neden olur, hangi saat/yer bağlantısıyla.",
  "English action: one shot, one action, physically plausible.",
  [("elif", "Replik.", "ton"), ("kerem", "Replik.")],
  "kamera: tek hareket", et="NEVŞEHİR", kurgu="ek not")
```

- `~ayse` = sadece sesi duyulur (telefon). Konuşan herkes `kim` listesinde olmalı.
- Replik: en çok ~18 kelime toplam, en çok 2 konuşma. Tırnak içinde Türkçe.
- Bir sahnede en çok 2 görünür karakter (3'ü ancak sessiz ya da çok gerekirse).
- `fb=True` anı sahnesi, `z="anı-gece"` gibi.

## Karakter varlığı

- Elif: B6'da tanışır, B14'te katılır, B34 sabahı gider, B39'da döner (itiraf), B40'ta yeniden ekipte. B46 Sc1'de kanıt toplamak için ayrılır; B47'de yok (Sc6'da telefondan dosya yollar), B48 Sc1'de döner, sonra hep var.
- Yaşar: B7-8, 18-19, 25, 31-33, 43 (telefon), 46, 53, 62 (telefon), 66, 75-76, 83 (sesli mesaj), 92-93, 98-100.
- Leyla: B9-10, 15 (tel.), 20 (tel.), 27-28, 30 (tel.), 41 (tel.), 54 (tel.), 57-58, 68 (tel.), 82 (tel.), 91, 100 (bilirkişi).
- Hüseyin Usta: B3 mezarlıkta uzaktan, B4-5, 41-42 (tel.), 48 (kalp krizi, hastane), 49 (yüzük çalınır), 88 (tel., taburcu), 95 (yüzüğü geri alır), 99-100.
- Necmi: B5 otobüs, B10, 24, 29, 37-38, 51-53, 63-66, 85-87, 93-100.
- Selim: B4, 13, 56, 67, 90, 93 (fotoğraf), 94 ve 96 (telefon), 97-100.
- Cevdet: B97 (Divriği taş kapısı), 98 (Yozgat mezarlığı), 100. 1979 sahneleri: B98 anı.

## Son kısım (B81-B100) akış notları

- B80-81 İzmir: Elif'in dedesi kaseti verir; "önce onun yükünü taşı" (B81 Sc1), "Cevdet'e kızma" (B81 Sc6).
- B82 Aydın: Leyla telefonda "duruşma öne alındı, 8 gün kaldı" (Gün 90). Selim tedbir istiyor.
- B83-89: Yaşar'ın mesajı (B83), Kerem'in "bitirmek istiyorum" kararı (B84), Necmi yalnız kalır (B85), Selim'in defteri yok etmek istediğini anlatır (B86), ekibe katılır (B87), altıncı zarar (B88), mahkeme tehdidi (B89).
- B90 Ankara: Hâkim çek delilini dosyaya alır, tedbir talebini reddeder, mührün 10 gün içinde Kayseri'de bilirkişi huzurunda açılmasına karar verir (Gün 100).
- B91: Leyla 1979 kaza tutanağını bulur (14 Şubat 1979, Kayseri–Sivas yolu); tanık imzası Yaşar Demirci (15 yaşında).
- B97 Divriği: Cevdet kısmen itiraf eder, Selim çıkagelir. B98 Yozgat: Yaşar 1979 gecesini anlatır (anı sahnesi), Cevdet'in kızı ameliyattan sonra bir yıl daha yaşamıştır; Selim "ablam mıydı?" diye sorar.
- B100 Kayseri: 5.000 ₺ sermaye iade edilir, Hüseyin mührü yüzüğüyle kırar, iki anahtar yarısı kilidi açar, 1978 ortaklık senedi çıkar, dükkân "81 İl Yol Hanı", haritanın arkasında "İpek Yolu - Semerkant".
- Uzun yolculuklarda ilk sahne 09:00-09:30 olabilir ("sabahın ilk otobüsü"); önceki bölümün son sahnesi sabaha sarkıyorsa varış saati yol süresine göre kaydırılır.
- Gümüş anahtar: yarısı B26 Mardin'de, yarısı B50 Trabzon'da.
- Hüseyin'in mühür yüzüğü: B49'da çalınır, B53'te geri alınır, B95'te Hüseyin'e verilir.

## GitHub Pages yayını

- Artifact biçimindeki sayfalar (`flow/dedemin-defteri-flow.html`, `kasa/kasa-prompt.html`) tam HTML iskeleti taşımaz. GitHub'dan telefonda doğru açılsınlar diye `yayin_hazirla.py` bunları `yayin/` klasörüne tam sayfa olarak yazar. Hepsini sırayla üretmek için: `python3 icerik/dedemin-defteri/uret.py` (Kasa Prompt Aracı, Dedemin Defteri sayfası, `yayin/` kopyaları).
- Adres: `https://acuma4500-maker.github.io/JoZh/icerik/dedemin-defteri/yayin/`. `main`'e birleşince Pages kendiliğinden yayınlar.
- Depo herkese açıktır; sayfalarda `noindex` var ama adresi bilen herkes görebilir.

## Kasa prompt'u (sabit şablon)

- Tek kaynak: `kasa/kasa-motor.js`. Dedemin Defteri sayfasındaki sahne kasa kutuları ve Kasa Prompt Aracı bu dosyayı build sırasında içine alır; prompt metni artık Python'da üretilmez.
- Değişen kasa: siyah zemin, sağ üstte KASA + bakiye, altında yeşil `+` ya da kırmızı `-` fark. Para efekti yok. Süre 8 sn: 1 sn eski bakiye, 1-1,4 sn fark belirir, 1,4-3,4 sn bakiye yeni değere gider, kalanı sabit.
- Sabit kasa (kasası değişmeyen sahne): aynı sayaç, 8 sn boyunca aynı bakiye, altında yazı yok. Aynı bölümde aynı bakiyeyi taşıyan sabit sahneler tek klibi paylaşır, sahne kutusu bunu yazar.
- Ayarlar (para birimi ₺/TL, rakamlar akıcı/anında, KASA yazısı var/yok) `localStorage` anahtarı `kasa-prompt-ayar` ile iki sayfada ortaktır (aynı adreste).
- Sahne video prompt'larına dokunulmaz; kasa kutusu her sahne kartının en altında ayrı durur.
