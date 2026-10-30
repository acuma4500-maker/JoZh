# -*- coding: utf-8 -*-
"""Bölüm 1-3. Kasa göstergesi Bölüm 4'te başlar, bu yüzden bu bölümlerde kasa hesabı yoktur."""
from ortak import EP, S

META = {
    1: dict(il="Londra", baslik="Londra'da Battım",
            hikaye="Kerem Aksoy'un Londra'daki sneaker dükkânı batmıştır. Ev sahibi dükkânı boşaltmasını söyler, borç büyür. "
                   "Son gece dükkânı kapatırken telefonunda annesinden 14 cevapsız çağrı bulur.",
            satilan="—", alinan="—",
            son="Telefondaki sesli mesajda annesinin sesi titriyor: 'Dedeni kaybettik.'"),
    2: dict(il="Londra → Kayseri", baslik="Hadi Dön Artık",
            hikaye="Annesi onu eve çağırır. Bilet parası olmayan Kerem sneaker koleksiyonunu satar, sadece bir çifti saklar. "
                   "Kayseri'de annesine sarılır; dedesinin evinde vasiyetin ertesi gün okunacağını öğrenir.",
            satilan="Sneaker koleksiyonu (bir çift hariç)", alinan="Uçak bileti",
            son="Annesi: 'Dedenin vasiyeti yarın noterde okunacak. Sadece sana bir şey bırakmış.'"),
    3: dict(il="Kayseri", baslik="Miras Bir Defter mi?!",
            hikaye="Noterde vasiyet okunur: ev ve dükkân annesine kalır, Kerem'e ise tek şey, son sayfası mühürlü eski bir deri defter. "
                   "Öfkelenir, ama dedesinin video kaydı onu yumuşatır. Defterin ilk sayfasında bir adres ve bir uyarı vardır.",
            satilan="—", alinan="—",
            son="Defterin ilk sayfası: 'Kapalı Çarşı, 42 numara. Hüseyin'e git. Kimseye güvenme.' Pencerenin dışında ışıkları kapalı bir araba."),
}

# ------------------------------------------------------------------ B1 LONDRA
EP(1, {
    "evsahibi": ("EV SAHİBİ", "LANDLORD, a 62-year-old British man, thin, neat grey mustache, tweed flat cap, long beige raincoat, holding a white envelope", "elderly male voice, polite but firm, speaks calm Turkish"),
}, {
    "A": ("Londra sneaker dükkânı, yağmurlu akşam", "a small independent sneaker shop in London on a rainy evening, shelves of colorful unsold sneakers, an almost empty shop floor, a counter with an old cash register, a rain-streaked window with blurred red double-decker bus lights outside"),
    "B": ("Dükkân önü, gece", "a rainy London street at night in front of the sneaker shop, wet pavement reflecting neon lights, a metal roller shutter"),
    "C": ("Kerem'in küçük evi", "Kerem's tiny cramped London bedsit, a narrow bed covered with sneaker boxes, a laptop on a small desk, a small window with rain"),
    "D": ("Açılış günü anısı", "a warm, bright memory scene: the same sneaker shop on its opening day with balloons and a ribbon, friends and happy customers, golden light"),
}, [
    S("Kerem yağmurlu akşam boş dükkânda tezgâhın başında beklemektedir; tek müşteri yoktur.", "A", ["kerem"],
      "Kerem stands alone behind the shop counter, looking at the empty door and the clock on the wall; rain runs down the window; he sighs and rests his chin on his hand.",
      [("kerem", "Üç aydır tek bir çift satmadım... Londra bana küstü.")]),
    S("Ev sahibi kapıdan girer ve tahliye zarfını uzatır.", "A", ["kerem", "evsahibi"],
      "The landlord enters shaking rain off his raincoat, places a white envelope on the counter; Kerem looks at it, then at him, pleading.",
      [("evsahibi", "Kira üç aylık gecikti. Cuma günü dükkânı boşaltıyorsun."), ("kerem", "Bir hafta daha verin, toparlarım.")]),
    S("Kerem gece evinde bilgisayarda borçlarına bakar.", "C", ["kerem"],
      "Kerem sits on his bed among sneaker boxes, staring at a laptop screen full of red numbers, running his hands through his hair.",
      [("kerem", "Kırk bin sterlin borç... Kasam sıfırın bile altında.")], kam="close-up over the shoulder on the red laptop screen, then Kerem's tired face"),
    S("Dükkânın açılış gününü hatırlar.", "D", ["kerem"],
      "Flashback: a younger-looking, excited Kerem cuts the ribbon of his new shop while friends cheer and balloons float.",
      [("kerem", "On dokuz yaşında açmıştım. Herkes 'Londra'yı sen mi fethedeceksin' demişti.")], kam="warm golden light, slow motion, soft glow"),
    S("Son gece dükkânın panjurunu kapatır.", "B", ["kerem"],
      "In the rain Kerem pulls the metal shutter down, locks it, puts the key in his pocket and looks at the shop one last time.",
      [("kerem", "Hoşça kal dükkân.")], kam="wide shot from across the wet street, slow push-in"),
    S("Telefonunda 14 cevapsız çağrı; sesli mesajı dinler.", "B", ["kerem", "~ayse"],
      "Under a street lamp Kerem sees his phone screen full of missed calls, presses play on a voice message and his face drains of color; the phone slips slightly in his hand.",
      [("ayse", "Kerem oğlum... dedeni kaybettik.")],
      kam="slow dramatic push-in to a close-up", kurgu="Telefon ekranında: '14 cevapsız çağrı — Anne'"),
])

# ------------------------------------------------------------------ B2 LONDRA -> KAYSERİ
EP(2, {
    "koleksiyoncu": ("SNEAKER KOLEKSİYONCUSU", "SNEAKER COLLECTOR, a 30-year-old woman, short bleached-blonde hair, round glasses, oversized black bomber jacket, white high-top sneakers, holding a thick roll of banknotes", "young female voice, quick, cool tone"),
}, {
    "A": ("Londra, gece caddesi", "a rainy London street at night, wet pavement, a bridge with city lights in the distance"),
    "B": ("Kerem'in küçük evi", "Kerem's tiny cramped London bedsit, an open suitcase on the bed, stacks of sneaker boxes, rain on the window"),
    "C": ("Koleksiyoncunun evi", "a collector's modern apartment with glass shelves displaying rare sneakers under spotlights"),
    "D": ("Havalimanı", "a modern airport terminal gate area, large windows with a plane outside, travelers with suitcases"),
    "E": ("Kayseri havalimanı çıkışı", "the arrival hall of a small Turkish airport with large glass windows showing snowy Mount Erciyes in the distance, family members waiting with open arms"),
    "F": ("Dede evi salonu", "Hacı Rıza's old living room in Kayseri, a worn leather armchair, framed family photos, a tulip-shaped tea glass on a side table, warm lamp light"),
}, [
    S("Yağmurda yürürken annesini arar; annesi onu eve çağırır.", "A", ["kerem", "~ayse"],
      "Kerem walks along the wet street holding his phone to his ear, eyes red, unable to speak for a moment.",
      [("ayse", "Hadi dön artık oğlum. Dedeni birlikte uğurlayalım."), ("kerem", "Anne, bilet parasını bile bulamıyorum.")]),
    S("Eve gelir ve valizini toplamaya başlar; sneaker kutularına bakar.", "B", ["kerem"],
      "Kerem throws clothes into an open suitcase, then stops and looks at the stacked sneaker boxes along the wall, making a decision.",
      [("kerem", "Hepsini satacağım. Ama bir çift bende kalacak.")]),
    S("Koleksiyoncuya sneaker'ları satar; son bir çifti vermez.", "C", ["kerem", "koleksiyoncu"],
      "The collector inspects rare sneakers under spotlight and counts banknotes into Kerem's hand; Kerem holds one pair back, hugging the shoebox to his chest.",
      [("koleksiyoncu", "Bu koleksiyona bilet parası fazlasıyla yeter."), ("kerem", "Bu çifti vermiyorum. O benim şansım.")]),
    S("Havalimanında telefondaki dede fotoğrafına bakar.", "D", ["kerem"],
      "Kerem sits at the gate with a boarding pass in one hand, looking at an old photo of his grandfather on his phone; a plane waits outside the window.",
      [("kerem", "Dede... iki yıldır seni aramadım.")], kam="slow push-in on Kerem's face, warm reflection of the phone light"),
    S("Kayseri'de annesine sarılır.", "E", ["kerem", "ayse"],
      "Through the glass doors Kerem sees his mother; they run to each other and hug tightly, Mount Erciyes behind them.",
      [("ayse", "Hoş geldin oğlum. Çok zayıflamışsın."), ("kerem", "Anne...")]),
    S("Dede evinde dedesinin koltuğuna bakar; annesi vasiyetten bahseder.", "F", ["kerem", "ayse"],
      "Kerem touches the worn armchair; Ayşe puts a tea glass beside him and speaks quietly, looking at him.",
      [("ayse", "Vasiyet yarın noterde okunacak. Sadece sana bir şey bırakmış.")], kam="slow dramatic push-in to a close-up"),
])

# ------------------------------------------------------------------ B3 KAYSERİ
EP(3, {
    "noter": ("NOTER", "NOTARY, a 55-year-old Turkish man, rimless glasses, grey suit, dark red tie, holding a folder with the will", "adult male voice, formal, measured Turkish"),
}, {
    "A": ("Dede evi salonu, sabah", "Hacı Rıza's old living room in Kayseri in the morning, framed family photos on the wall, a tea tray on a table, soft daylight"),
    "B": ("Noter ofisi", "a Turkish notary's office, a large wooden desk, leather chairs, shelves of law books, a window with winter light"),
    "C": ("Dedenin odası, gece", "Hacı Rıza's old bedroom study at night, a wooden desk with a lamp, a tablet leaning on a stand, a worn armchair, bookshelves"),
    "D": ("Pencere dışı, gece", "a snowy street seen through a window at night, a dark car parked with its headlights off, a faint figure beside it"),
}, [
    S("Sabah kahvaltısında Kerem duvardaki aile fotoğraflarına bakar.", "A", ["kerem", "ayse"],
      "Kerem stares at framed family photos on the wall while Ayşe pours tea for him.",
      [("kerem", "Belki ev bıraktı, belki dükkân. Londra'daki borcumu kapatırım."), ("ayse", "Hadi, noter bekliyor.")]),
    S("Noter vasiyeti okur: ev ve dükkân annesine kalmıştır.", "B", ["kerem", "ayse", "noter"],
      "The notary opens a folder and reads aloud; Ayşe lowers her head, Kerem leans forward hopefully.",
      [("noter", "Evim ve dükkânım ömür boyu Ayşe'nin. Torunum Kerem'e ise tek bir şey bırakıyorum.")]),
    S("Noter eski bir deri defteri masaya koyar.", "B", ["kerem", "noter"],
      "The notary places an old worn leather notebook with a red wax seal on its last page on the desk; Kerem's face falls.",
      [("noter", "Son sayfası mühürlü. Yol bitmeden açılamaz."), ("kerem", "Defter mi?! Bir defter mi?")], kam="close-up on the notebook and the red seal, then Kerem's face"),
    S("Kerem eve dönünce defteri masaya fırlatır; annesi alır.", "A", ["kerem", "ayse"],
      "Kerem tosses the notebook onto the table in anger; Ayşe picks it up gently and presses it to her chest.",
      [("kerem", "Londra'da batmış adamım, bana defter mi bıraktı!"), ("ayse", "Dedenin her kuruşunu bu defterle kazandığını biliyorsun.")]),
    S("Gece dedesinin odasında tablette bir video kaydı bulur.", "C", ["kerem", "riza"],
      "Kerem presses play on a tablet; on its screen the old grandfather appears sitting in the same armchair, speaking warmly to the camera.",
      [("riza", "Kerem... bu defter sana yük değil, yol. İlk adres birinci sayfada.")],
      kam="over-the-shoulder shot of Kerem watching the tablet, then close-up on the grandfather's face on the screen"),
    S("Defterin ilk sayfasını açar; pencerenin dışında bir araba ve gölge.", "D", ["kerem"],
      "Kerem reads the first handwritten page by lamplight; he hears an engine, walks to the window and sees a dark car with its lights off and a figure watching the house.",
      [("kerem", "'Kimseye güvenme.' Dede... kimden saklıyordun bunu?")],
      kam="slow dramatic push-in toward the window", kurgu="Defterin birinci sayfası: 'Kapalı Çarşı, 42 numara. Hüseyin'e git. Kimseye güvenme.'"),
])
