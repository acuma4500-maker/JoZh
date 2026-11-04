# Montaj: Mert ile Ali ve Dedemin Defteri

Her bölüm tek bir Reels videosu olur:

1. **Kapak (1,2 sn):** `kapak.png` (yazısı görselin içinde).
2. **Sahneler:** dosya adındaki son sayı sahne numarasıdır (`7.3.mp4` = sahne 3).
   - Kasa açıldıysa sağ üstte **KASA** sayacı çizilir: rakamlar dizinin kendi kasa hesabından gelir
     (Mert ile Ali: `jozh-studios/js/data.js`, TL · Dedemin Defteri: `dedemin-defteri/flow`, ₺).
     Artışta yeşil, azalışta kırmızı, sayaç akar. Flow'da kasa videosu üretmeye gerek yok.
   - Dedemin Defteri'nde sahne notundaki yer-zaman yazısı (ör. `KAYSERİ · GÜN 4 · 09:40`) altta 3 sn belirir.
3. **Pek yakında (3 sn):** SONRAKİ bölümün `yakinda.png`'si. Yoksa kapak ya da son kare karartılıp yazı eklenir.

```
girdi/mert-ali/bolum-01/1.1.mp4 … 1.6.mp4, kapak.png, yakinda.png
girdi/dedemin-defteri/bolum-01/…
python3 montaj.py mert-ali 1-20
python3 montaj.py dedemin-defteri 7      # --kasasiz, --yazisiz
```
Çıktı: `cikti/<dizi>/<dizi>-bolum-NN.mp4`. Videolar ve çıktılar git'e girmez.
