# Montaj (Mert ile Ali)

Her bölüm için tek bir Reels videosu çıkarır:

1. **Kapak (1,2 sn):** `kapak.png`, bölümün kapağı (yazı görselin içinde: BÖLÜM N + bölüm adı).
2. **Sahneler:** `1.mp4 … 6.mp4` arka arkaya. Kasa açıldıysa (Video 4 sahne 6'dan itibaren) sağ üstte **KASA** sayacı
   montajda çizilir: rakamlar paneldeki kasa defterinden gelir, artışta yeşil, azalışta kırmızı, sayaç akar.
   Bu yüzden Flow'da kasa videosu üretmene gerek yok.
3. **Pek yakında (3 sn):** SONRAKİ bölümün `yakinda.png`'si (BÖLÜM N+1 + adı + PEK YAKINDA).
   Yoksa sonraki bölümün kapağı karartılıp yazı montajda eklenir.

```
montaj/girdi/bolum-07/kapak.png
montaj/girdi/bolum-07/yakinda.png
montaj/girdi/bolum-07/1.mp4 … 6.mp4
```
`python3 montaj/montaj.py 1-20` → `montaj/cikti/mert-ali-bolum-07.mp4` …  (`--kasasiz` ile sayaç çizilmez)

Not: Panelde elle eklediğin kasa işlemleri tarayıcıda durur, montaj yalnızca senaryodaki işlemleri bilir.
