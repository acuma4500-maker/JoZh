# Mert ile Ali: montaj

1. Her bölümün videolarını `girdi/bolum-NN/` klasörüne koy: `01.mp4`, `02.mp4`, ... (sıra dosya adına göre).
2. O bölümün kapak fotoğrafını aynı klasöre `kapak.png` adıyla koy.
3. `python3 montaj.py 1-20` çalıştır. Çıktılar `cikti/` klasörüne düşer.

Her bölüm şöyle çıkar: kapak + "MERT İLE ALİ / BÖLÜM N" (1.2 sn) → sahneler → sonraki bölümün kapağı + "BÖLÜM N+1 / PEK YAKINDA" (3 sn).
Sonraki bölümün kapağı yoksa bu bölümün kapağı bulanıklaştırılıp kullanılır.
