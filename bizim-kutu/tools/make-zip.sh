#!/usr/bin/env bash
# public_html'e yüklenecek ZIP arşivini oluşturur: dist/bizimkutu-public_html.zip
# - Yalnızca tarayıcının ihtiyaç duyduğu dosyalar dahil edilir (testler, araçlar, kurallar hariç).
# - service-worker.js içindeki VERSION, dosya içeriklerinin karmasıyla damgalanır
#   (her dağıtımda kullanıcılara "Yeni sürüm hazır" bildirimi gider).
set -euo pipefail
cd "$(dirname "$0")/.."
OUT=dist; STAGE="$OUT/public_html"
rm -rf "$STAGE" "$OUT/bizimkutu-public_html.zip"; mkdir -p "$STAGE"
cp index.html manifest.json service-worker.js .htaccess "$STAGE/"
cp -r css js data assets "$STAGE/"
rm -f "$STAGE"/assets/fonts/*.txt.bak
HASH=$(cd "$STAGE" && find . -type f ! -name service-worker.js -print0 | sort -z | xargs -0 sha256sum | sha256sum | cut -c1-12)
sed -i "s/const VERSION = '[^']*';/const VERSION = 'bk-$HASH';/" "$STAGE/service-worker.js"
sed -i "s/export const BUILD = '[^']*';/export const BUILD = 'bk-$HASH';/" "$STAGE/js/constants.js"
grep -q "bk-$HASH" "$STAGE/service-worker.js"
(cd "$STAGE" && zip -qr -X "../bizimkutu-public_html.zip" . -x '.DS_Store')
echo "✔ $OUT/bizimkutu-public_html.zip  (sürüm bk-$HASH, $(du -h "$OUT/bizimkutu-public_html.zip" | cut -f1))"
