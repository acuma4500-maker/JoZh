# -*- coding: utf-8 -*-
"""Sabit karakter tanımları. BU METİNLER SEZON BOYUNCA DEĞİŞMEZ.

Her karakter için:
  ad      : ekranda/prompt'ta görünen isim
  yas     : yaş
  ilk     : ilk göründüğü bölüm ve şehir
  rol     : hikâyedeki rolü (Türkçe)
  tr      : Türkçe görünüm özeti (yüz, saç, kıyafet) - karakter sayfası için
  en      : Flow'a giden SABİT İngilizce görünüm tarifi
  ses     : Flow'a giden SABİT İngilizce ses tarifi (kısa)
"""

STIL = ("Vertical 9:16 video, 8 seconds, semi-realistic stylized 3D animation, soft cinematic lighting, "
        "Pixar-like proportions with realistic skin, fabric and stone textures, consistent character design. "
        "No subtitles, no captions, no on-screen text, no logos.")

K = {}


def kar(id, ad, yas, ilk, rol, tr, en, ses, ana=True):
    K[id] = dict(id=id, ad=ad, yas=yas, ilk=ilk, rol=rol, tr=tr, en=en, ses=ses, ana=ana)


kar("kerem", "KEREM", 20, "Bölüm 1 · Londra",
    "Baş karakter. Londra'da sneaker dükkânı batmış, aceleci, esprili ama iyi kalpli. Dedesinin defteriyle 81 ili dolaşır.",
    "Zayıf yapılı; buğday ten, oval yüz, belirgin çene hattı. Kalın koyu kaşlar, iri koyu kahverengi gözler. Kısa, dalgalı siyah saç, alnına düşen dağınık perçem; hafif sakal. Sol kulağında küçük gümüş halka küpe. Bol, solmuş zeytin yeşili bomber ceket, altında beyaz bisiklet yaka tişört, siyah dar kargo pantolon, kırmızı bağcıklı eskimiş beyaz-gri sneaker. Çaprazdan taktığı kahverengi deri çantada eski deri defter.",
    "KEREM, a 20-year-old Turkish man, lean build, warm olive skin, oval face with a defined jawline, thick dark eyebrows, expressive dark brown eyes, short wavy black hair with a slightly messy fringe, light stubble, small silver hoop earring in his left ear; wears an oversized faded olive-green bomber jacket over a plain white crew-neck t-shirt, black slim cargo pants, worn white-and-grey sneakers with red laces, and a brown leather crossbody bag that holds an old worn brown leather notebook with a red wax seal on its last page",
    "young male voice, warm energetic tenor, fast casual Istanbul Turkish, playful but sincere")

kar("riza", "HACI RIZA", 78, "Bölüm 3 · Kayseri (vasiyet kaydı)",
    "Kerem'in dedesi, Kayserili efsane tüccar. Defterdeki öğütler, kaset kaydı ve geri dönüşlerle hikâyeye girer.",
    "Ince ve dik duruşlu; derin çizgili, sevecen yüz. Kısa kesilmiş beyaz sakal ve bıyık, ela gözler. Gri yün kasket altında beyaz saç. Kahverengi tüvit ceket, krem örgü yelek, beyaz yakalı gömlek, gri yün pantolon, siyah rugan ayakkabı. Sağ elinde gümüş yüzük, elinde kehribar tespih.",
    "HACI RIZA, a 78-year-old Turkish man, slim and upright, deeply lined kind face, neatly trimmed short white beard and white mustache, bright hazel eyes with crow's feet, white hair under a grey wool flat cap; wears a dark brown tweed jacket over a cream knitted vest and white collared shirt, grey wool trousers, polished black leather shoes, a silver ring on his right hand, holding amber prayer beads",
    "elderly male voice, deep calm baritone with a gentle rasp, slow wise Kayseri-accented Turkish")

kar("rizag", "GENÇ RIZA (1979)", 31, "Bölüm 12 · Fotoğraf / 1979 geri dönüşleri",
    "Dedenin 1979'daki hâli. Sadece geçmiş sahnelerinde kullanılır.",
    "Ince, dik; buğday ten, keskin ela gözler, kalın siyah bıyık, yandan ayrılmış kısa siyah saç. Gri yün kasket, kahverengi deri ceket, beyaz yakalı gömlek, gri pantolon (1970'ler). Sağ elinde gümüş yüzük.",
    "YOUNG RIZA, a 31-year-old Turkish man in 1979, slim and upright, olive skin, sharp hazel eyes, thick black mustache, short side-parted black hair under a grey wool flat cap; wears a brown 1970s leather jacket over a white collared shirt, grey trousers, a silver ring on his right hand; the scene has a warm, slightly faded 1970s film look",
    "male voice, firm warm baritone, Kayseri-accented Turkish, 1970s tone", ana=False)

kar("husey", "HÜSEYİN USTA", 74, "Bölüm 4 · Kayseri, Kapalı Çarşı",
    "Dedenin can dostu, ahi ustası. 5.000 ₺ sermayeyi verir, mühür yüzüğünü saklar. Listedeki 81. isimdir.",
    "Kısa ve tıknaz; yuvarlak, güler yüz. Gür gri kaşlar, kalın gri pala bıyık. Tepesi kel, yanları gri saç; burnunun ucunda küçük yuvarlak okuma gözlüğü. Bej örgü hırka, çizgili yakalı gömlek, kahverengi deri önlük, koyu pantolon. Sağ işaret parmağında mühür kazınmış iri gümüş yüzük.",
    "HÜSEYİN USTA, a 74-year-old Turkish man, short and stocky, round friendly face, bushy grey eyebrows, thick grey walrus mustache, bald head with grey hair on the sides, small round reading glasses on the tip of his nose; wears a beige knitted cardigan over a striped collared shirt, a brown leather apron, dark trousers, and a large silver signet ring with an engraved seal on his right index finger",
    "elderly male voice, warm husky bass, slow grandfatherly Kayseri-accented Turkish")

kar("ayse", "AYŞE", 46, "Bölüm 1 · Londra (telefon sesi), Bölüm 2 · Kayseri",
    "Kerem'in annesi. Kayseri'den telefonla haber getirir; finalde oradadır.",
    "Orta yapılı; yumuşak oval yüz, sıcak kahverengi gözler, hafif gülme çizgileri. Kısmen kırlaşmış koyu kahve saç ense topuz; gevşek bağlanmış açık mavi pamuk başörtüsü. Bej hırka, çiçekli bluz, uzun koyu etek, küçük altın küpe.",
    "AYŞE, a 46-year-old Turkish woman, medium build, gentle oval face, warm brown eyes, faint smile lines, dark brown hair with a few grey strands in a low bun under a loosely worn light-blue cotton headscarf; wears a beige cardigan over a floral blouse, a long dark skirt and small gold earrings",
    "middle-aged female voice, soft warm alto, caring, slightly worried, Kayseri-accented Turkish")

kar("selim", "SELİM KARAHAN", 45, "Bölüm 4 · Kayseri, çarşı kapısı",
    "Rakip. Karahan Lojistik/Gıda'nın sahibi; defteri ve dükkânı ele geçirmek ister. Finalde ortak olur.",
    "Uzun boylu, fit; çıkık elmacık kemikli köşeli yüz, soğuk gri-yeşil gözler. Gri telli, bakımlı kısa siyah sakal; şakakları kırlaşmış, geriye taranmış siyah saç. Antrasit üç parça takım, beyaz gömlek, bordo kravat, altın saat, siyah deri eldiven, parlak oxford ayakkabı.",
    "SELİM KARAHAN, a 45-year-old Turkish man, tall and fit, angular face with high cheekbones, cold grey-green eyes, neatly groomed short black beard with grey streaks, slicked-back black hair with grey temples; wears a tailored charcoal three-piece suit, crisp white shirt, dark burgundy tie, gold wristwatch, black leather gloves and polished black oxford shoes",
    "adult male voice, smooth low baritone, calm polished Istanbul Turkish, quietly threatening")

kar("necmi", "NECMİ", 38, "Bölüm 5 · Kayseri–Nevşehir otobüsü",
    "Selim'in adamı 'Tilki' Necmi. Sabotajcı; sonradan Kerem'in safına geçer.",
    "Ince, kuru yapılı; dar ve sivri yüz, kısık kurnaz koyu gözler. Ince kalem bıyık, jöleli dikleştirilmiş kısa siyah saç, sol kaşında küçük yara izi. Siyah deri ceket, hardal sarısı polo tişört, koyu kot, sivri burunlu kahverengi ayakkabı, altın zincir kolye, ağzında kürdan.",
    "NECMİ, a 38-year-old Turkish man, wiry thin build, narrow sharp face, sly squinting dark eyes, thin pencil mustache, short spiky gelled black hair, a small scar on his left eyebrow; wears a black leather jacket over a mustard-yellow polo shirt, dark jeans, pointed brown leather shoes, a gold chain necklace, a toothpick in his mouth",
    "adult male voice, nasal raspy tenor, fast slick salesman Turkish with a mocking edge")

kar("elif", "ELİF", 24, "Bölüm 6 · Nevşehir, Göreme",
    "İzmirli belgeselci-fotoğrafçı. Önce Selim'den para alır, sonra Kerem'in en büyük destekçisi olur.",
    "Ince, atletik; burnunda çiller olan açık buğday ten, parlak yeşil-kahve gözler. Omuz hizasında kıvırcık kızıl-kahve saç, dağınık yarım at kuyruğu. Hardal sarısı bere, seyahat yamalı bol kot ceket, siyah balıkçı yaka, haki kargo pantolon, kahverengi yürüyüş botu. Boynunda kırmızı askılı vintage fotoğraf makinesi.",
    "ELİF, a 24-year-old Turkish woman, slim athletic build, light olive skin with freckles across her nose, bright green-brown eyes, shoulder-length curly auburn hair in a messy half-ponytail; wears a mustard-yellow beanie, an oversized denim jacket covered with travel patches over a black turtleneck, khaki cargo pants, brown hiking boots, and a vintage mirrorless camera on a red strap around her neck",
    "young female voice, bright clear mezzo, curious and energetic, Aegean Izmir Turkish lilt")

kar("yasar", "YAŞAR KAPTAN", 62, "Bölüm 7 · Nevşehir–Niğde otobüsü",
    "Bağlama çalan bilge otobüs şoförü. 1979'da kervanın 15 yaşındaki çırağıdır; gerçeğin tek tanığı.",
    "Iri yarı, geniş omuzlu; yuvarlak, yıpranmış yüz, sevecen yorgun kahverengi gözler. Kalın kır bıyık, kısa gri saç. Kolları kıvrılmış lacivert şoför gömleği, koyu gri yelek, siyah pantolon, gömlek cebine asılı pilot gözlüğü, eskimiş deri kayışlı saat.",
    "YAŞAR KAPTAN, a 62-year-old Turkish man, heavyset with broad shoulders, round weathered face, kind tired brown eyes, thick salt-and-pepper mustache, short grey hair; wears a navy-blue bus driver uniform shirt with rolled-up sleeves, a dark grey vest, black trousers, aviator sunglasses hanging on his shirt pocket and a worn leather wristwatch",
    "adult male voice, deep gravelly baritone, slow folksy Central Anatolian Turkish, warm humor")

kar("yasarg", "ÇIRAK YAŞAR (1979)", 15, "Bölüm 98 · 1979 geri dönüşü",
    "Yaşar'ın 1979'daki 15 yaşındaki hâli. Sadece geçmiş sahnelerinde kullanılır.",
    "Sıska; yuvarlak yüz, sevecen kahverengi gözler, dağınık kısa siyah saç. Bol gri iş ceketi, yamalı pantolon, eski bot (1970'ler).",
    "YOUNG YAŞAR, a 15-year-old Turkish boy in 1979, skinny, round face, kind brown eyes, messy short black hair; wears an oversized grey work jacket, patched trousers and worn boots; warm, slightly faded 1970s film look",
    "teenage boy voice, nervous, Central Anatolian Turkish", ana=False)

kar("leyla", "DR. LEYLA", 52, "Bölüm 9 · Konya, Mevlana Müzesi",
    "Osmanlıca uzmanı ve arşivci. Defterin şifrelerini, dekontları ve 1979 tutanağını çözer.",
    "Orta yapılı; zeki, keskin yüz hatları, koyu kahve gözler. Boncuklu zincire bağlı kalın siyah dikdörtgen gözlük. Kısa gümüş-gri küt saç. Koyu petrol mavisi yün blazer, krem balıkçı yaka, uzun gri etek, düz siyah ayakkabı, göğüs cebinde gümüş kalem, kâğıt dolu eski deri çanta.",
    "DR. LEYLA, a 52-year-old Turkish woman, medium build, intelligent sharp face, dark brown eyes behind thick black rectangular glasses on a beaded chain, short silver-grey bob haircut; wears a deep teal wool blazer over a cream turtleneck, a long grey skirt, flat black shoes, a silver pen in her breast pocket, and carries a worn leather satchel full of papers",
    "middle-aged female voice, crisp articulate alto, precise academic Istanbul Turkish")

kar("nazli", "NAZLI ABLA", 44, "Bölüm 19 · Gaziantep",
    "Kadın kooperatifinin başkanı. Boykotta Kerem'e kapı açar; 1979 fotoğrafının öbür yarısını saklar.",
    "Sağlam, kendinden emin yapılı; yuvarlak sıcak yüz, canlı koyu gözler, al yanaklar. Arkadan bağlanmış beyaz işlemeli başörtüsü altında uzun siyah örgü saç. Bordo çiçekli uzun elbise, koyu yeşil örgü yelek, una bulanmış beyaz önlük, altın bilezikler.",
    "NAZLI ABLA, a 44-year-old Turkish woman, sturdy confident build, round warm face, lively dark eyes, rosy cheeks, long black braided hair under a white embroidered headscarf tied at the back; wears a burgundy floral long dress, a dark green knitted vest, a white apron dusted with flour and gold bangle bracelets",
    "middle-aged female voice, strong warm alto, cheerful, Gaziantep-accented Turkish")

kar("cevdet", "CEVDET KARAHAN", 82, "Bölüm 97 · Sivas, Divriği",
    "Selim'in babası, dedenin eski ortağı. 1979'da kasayı alan ve utancından yalan söyleyen kişi.",
    "Çelimsiz, zayıf; çökük yanaklar, hüzünlü sulu gri-yeşil gözler. Geriye taranmış seyrek beyaz saç, beyaz kirli sakal. Bej kazak üstüne uzun koyu gri yün palto, kahverengi atkı, koyu ahşap baston, titreyen eller.",
    "CEVDET KARAHAN, an 82-year-old Turkish man, frail thin build, hollow cheeks, sad watery grey-green eyes, sparse white hair combed back, white stubble; wears a long dark-grey wool overcoat over a beige sweater, a brown scarf, walks with a dark wooden cane, his hands tremble",
    "elderly male voice, thin shaky tenor, slow breathy regretful Turkish")

kar("cevdetg", "GENÇ CEVDET (1979)", 35, "Bölüm 12 · Fotoğraf / 1979 geri dönüşleri",
    "Cevdet'in 1979'daki hâli. Sadece geçmiş sahnelerinde kullanılır.",
    "Uzun boylu; köşeli yüz, gri-yeşil gözler, kalın siyah favori ve bıyık, dalgalı siyah saç. Balıkçı yaka üstüne kahverengi kadife ceket (1970'ler).",
    "YOUNG CEVDET, a 35-year-old Turkish man in 1979, tall, angular face, grey-green eyes, thick black sideburns and mustache, wavy black hair; wears a brown corduroy jacket over a dark turtleneck; warm, slightly faded 1970s film look",
    "male voice, tense tenor, Turkish, 1970s tone", ana=False)
