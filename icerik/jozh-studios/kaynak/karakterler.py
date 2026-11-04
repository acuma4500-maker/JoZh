# -*- coding: utf-8 -*-
"""JOZH STUDIOS · 81 Şehir: sabit karakter tanımları.

BU METİNLER DİZİ BOYUNCA DEĞİŞMEZ. Yüz, saç, göz, vücut ve ses her sahnede aynen prompt'a girer.
Kıyafet yalnızca hikâyede sebebi olduğunda değişir (kıyafet anahtarı bölümde belirtilir):
  "temel" : Bölüm 1 - Bölüm 56 (yaz ve erken sonbahar)
  "ceket" : Bölüm 57 Düzce'den itibaren (yağmurda pazardan mont alırlar, sahnede gösterilir)
"""

K = {}


def kar(id, ad, yas, ilk, rol, tr, gecmis, en, ses, kiyafet=None, ana=False):
    K[id] = dict(id=id, ad=ad, yas=yas, ilk=ilk, rol=rol, tr=tr, gecmis=gecmis, en=en, ses=ses,
                 kiyafet=kiyafet or {}, ana=ana)


kar("mert", "MERT", 21, "Bölüm 1 · Malatya",
    "Ana karakter. Hikâye onun gözünden ilerler. Girişimci, cesur, aceleci, insanlarla arası iyi, büyük hayalli; bazen düşünmeden hareket eder.",
    "Koyu kahverengi, hafif dalgalı saç; ela-kahverengi gözler; hafif kirli sakal; buğday ten; yaklaşık 178 cm; fit ama aşırı kaslı değil. "
    "Siyah tişört, bol koyu gri pantolon, siyah detaylı beyaz spor ayakkabı.",
    "Malatyalı. Babası devlet memuruyken çocukluğu Antalya'da geçti; Ali'yle aynı sokakta büyüdü. 14 yaşında ailesi Malatya'ya döndü, "
    "arkadaşlık telefonda sürdü. Liseden sonra kuryelik, garsonluk, pazarda tezgâhtarlık yaptı. Hiçbir işte uzun kalmadı ama her işten "
    "bir pazarlık dersi aldı. Babasını 18 yaşında kaybetti; annesi Hatice'ye ve küçük kardeşine destek olmak için para kazanmak zorunda. "
    "Hayali: 'bir gün kendi markamız olacak.'",
    "MERT, a 21-year-old Turkish man from Malatya, about 178 cm tall, fit athletic build that is NOT overly muscular, warm wheat-toned "
    "light olive skin, a slightly handsome and memorable face with defined cheekbones, a straight nose and a confident half-smile, "
    "hazel-brown eyes under thick dark eyebrows, dark brown slightly wavy hair, medium length on top and shorter on the sides, "
    "light even stubble on his jaw and upper lip",
    "young male voice, warm energetic baritone, fast and expressive, natural Turkish with a light Malatya (Eastern Anatolian) flavor, playful and confident",
    kiyafet={
        "temel": "a plain black crew-neck t-shirt, loose-fit dark charcoal-grey trousers and white sneakers with black details",
        "ceket": "a black hooded rain jacket worn open over a plain black crew-neck t-shirt, loose-fit dark charcoal-grey trousers and white sneakers with black details",
    }, ana=True)

kar("ali", "ALİ", 21, "Bölüm 1 · Malatya",
    "Yardımcı ana karakter. Efendi, hevesli, meraklı; Mert'ten sakin ve mantıklı. Hesap kitapta iyi, kasayı o tutar. Mert'in çılgın fikirlerine itiraz eder ama onu asla yarı yolda bırakmaz.",
    "Koyu siyah, düzgün şekillendirilmiş, yandan ayrılmış saç; kahverengi gözler; temiz, sakalsız yüz; açık buğday ten; yaklaşık 177 cm; fit vücut. "
    "Beyaz tişört üstüne açık bırakılmış kum beji gömlek-ceket, lacivert chino pantolon, temiz beyaz deri spor ayakkabı, sol bileğinde sade siyah saat.",
    "Antalyalı. Babası Hasan Antalya'da küçük bir domates serası işletiyor; seranın borçları yüzünden aile zor durumda. Ali Malatya İnönü "
    "Üniversitesi'nde İşletme okuyor, burslu. Mert'le çocukluk arkadaşı; üniversite için Malatya'ya gelince yeni bir eve birlikte çıktılar. "
    "Her kuruşu küçük kahverengi deri bir deftere yazar. Hayali: ailesinin serasını borçtan kurtarmak.",
    "ALI, a 21-year-old Turkish man from Antalya, about 177 cm tall, fit lean build, light wheat-toned skin, a clean-shaven neat face with "
    "soft friendly features, calm warm brown eyes, deep black hair neatly styled with a tidy side part and short sides",
    "young male voice, calm clear tenor, measured and polite Turkish with a light Mediterranean Antalya lilt, thoughtful",
    kiyafet={
        "temel": "a light sand-beige button-up overshirt worn open over a plain white crew-neck t-shirt, dark navy slim chino trousers, clean white leather sneakers and a simple black wristwatch on his left wrist",
        "ceket": "a dark olive quilted jacket over a light sand-beige overshirt and a plain white crew-neck t-shirt, dark navy slim chino trousers, clean white leather sneakers and a simple black wristwatch on his left wrist",
    }, ana=True)

kar("cemil", "CEMİL BEY", 54, "Bölüm 1 · Malatya (motorun sahibi)",
    "Apartmanın üst katında oturan, motosikletin sahibi. Ciddi, paraya önem veren, kuralcı. 800.000 TL'lik borcun alacaklısı. Sezon finallerinde taksitleri alır.",
    "İri, tıknaz; köşeli sert yüz, alnında derin çizgiler, kısa kesilmiş gri saç, bakımlı kalın gri bıyık, keskin koyu gözler. Açık mavi gömlek üstüne lacivert kapitone yelek, koyu gri pantolon, kahverengi deri ayakkabı, iri altın saat; elinde anahtarlık.",
    "Malatya'da oto yedek parça toptancısı. Gençliğinde kamyon şoförlüğünden gelip kendi işini kurmuş. 'Para emekle kazanılır, hatır için verilmez' der. "
    "Motoru oğlu için almış ama oğlu İstanbul'a taşınınca garajda kalmış. Sert görünür, ama söz tutanlara saygı duyar.",
    "CEMİL BEY, a 54-year-old Turkish man, solid heavy-set build, a square stern face with deep frown lines on his forehead, short-cropped grey hair, "
    "a thick neatly trimmed grey mustache, sharp dark eyes; wears a navy-blue quilted vest over a light-blue collared shirt, dark grey trousers, "
    "polished brown leather shoes and a heavy gold wristwatch",
    "mature male voice, deep gruff bass, slow and firm Turkish, every word deliberate")

kar("hatice", "HATİCE", 47, "Bölüm 3 · Malatya (telefon), Bölüm 7 · Malatya",
    "Mert'in annesi. Sevecen ama yorgun; kendisi de geçim sıkıntısında.",
    "Orta yapılı; sıcak yuvarlak yüz, yorgun ama sevecen kahverengi gözler, gülme çizgileri; çenenin altından bağlı açık lila pamuk başörtüsü. Gri hırka, lacivert çiçekli elbise.",
    "Eşini üç yıl önce kaybetti. Evde kayısı reçeli ve pestil yapıp komşulara satarak geçiniyor. Mert'in küçük kardeşi Elif lisede okuyor.",
    "HATİCE, a 47-year-old Turkish woman, medium build, a warm round face with tired but loving brown eyes and soft smile lines, a light lilac cotton "
    "headscarf tied under her chin; wears a grey knitted cardigan over a navy dress with small white flowers",
    "middle-aged female voice, soft warm alto, caring, slightly tired, Malatya Turkish")

kar("hasan", "HASAN", 52, "Bölüm 3 · Antalya (telefon), Bölüm 35 · Antalya",
    "Ali'nin babası. Antalya'da küçük bir domates serası var, sera kredisi yüzünden sıkışmış.",
    "Zayıf, güneşten yanmış; uzun yüz, derin kaz ayakları, gür kır kaşlar, kısa gri sakal, seyrek kır saç. Kolları sıvanmış soluk yeşil iş gömleği, eski kot, toprak lekeli lastik çizme.",
    "Kumluca'da 40 yıllık seracı bir ailenin oğlu. Dürüst, sessiz, gururlu. Oğlunun okumasını her şeyden önemli sayar.",
    "HASAN, a 52-year-old Turkish man, lean and sun-tanned, a long face with deep crow's feet, bushy salt-and-pepper eyebrows, a short grey beard and "
    "thinning grey hair; wears a faded green work shirt with rolled-up sleeves, old blue jeans and soil-stained rubber boots",
    "mature male voice, quiet husky baritone, slow Mediterranean Antalya Turkish, proud and gentle")

# Sabit nesneler (prop). Prompt'ta gerektiği sahnede bu tarifle geçer.
NESNE = {
    "motor": "an unbranded high-end sport motorcycle in glossy red and black with no logos and no lettering",
    "motor_hasar": "the same unbranded red-and-black sport motorcycle, now badly damaged: cracked front fairing, bent handlebar, broken headlight and scraped paint, no logos",
    "defter": "a small brown leather ledger notebook and a black pen",
    "kamyonet": "an old white single-cab pickup truck from the early 2000s with a faded blue side stripe, a slightly dented tailgate, no brand logos and no lettering",
}
