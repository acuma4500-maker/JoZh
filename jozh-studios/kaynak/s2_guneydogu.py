# -*- coding: utf-8 -*-
"""Sezon 2 · Mezopotamya Hesabı · Güneydoğu Anadolu (Bölüm 21-29). Temmuz, sıcak.
Rota: Diyarbakır → Batman → Siirt → Şırnak (Cizre) → Mardin → Şanlıurfa → Adıyaman → Gaziantep → Kilis"""
from ortak import EP, S, T, U

AY = "Temmuz"

# ======================================================================= 21 DİYARBAKIR
EP(21, "Diyarbakır", "Surların Gölgesinde",
   "Hasanpaşa Hanı'nda kahvaltı, surlarda şafak koşusu, Hevsel Bahçeleri ve bir karpuz iddiası.",
   "Diyarbakır'a temmuz sıcağında, şafakta varırlar ve surların üstünden Dicle'ye bakan Hevsel Bahçeleri'ni görürler. Hasanpaşa Hanı'nda "
   "kahvaltı ederken bir kahvaltıcı Bingöl balının yarısını alır, kalanı da siparişlerle satılır. Ulu Cami'nin avlusunda serinlerler. Çarşıda "
   "kurutulmuş dolmalık patlıcan ve biber alırlar. Akşam ciğer kebabı yerken bir bahçıvan Mert'e meydan okur: 'Kırk kiloluk karpuzu "
   "kucaklayıp kaldırabilirsen sana bedava.'",
   {"sur": ("Diyarbakır Surları", "the top of the ancient black basalt city walls of Diyarbakır at dawn: a wide stone walkway, towers, and below "
            "the green Hevsel Gardens stretching to the Tigris river"),
    "han": ("Hasanpaşa Hanı", "the arcaded stone courtyard of the historic Hasanpaşa Han in Diyarbakır: black-and-white striped stone arches, "
            "breakfast tables with honey, cream, cheese, olives and tea, morning shade"),
    "ulucami": ("Ulu Cami avlusu", "the large stone courtyard of the Great Mosque of Diyarbakır: arcades with carved columns, a fountain in "
                "the middle, dark basalt and light limestone"),
    "carsi": ("Diyarbakır çarşısı", "a narrow covered bazaar lane in Diyarbakır: strings of dried hollowed eggplants and peppers hanging "
              "from shop fronts, sacks of bulgur and spices"),
    "cigerci": ("Ciğer kebapçısı", "a lively liver-kebab grill street in Diyarbakır at night: small grills with skewers over glowing charcoal, "
                "plastic stools, a pile of giant watermelons on the sidewalk")},
   [
       S("05:50 şafak", "sur", ["mert", "ali"], "Sur Üstünde Şafak",
         "Şafakta surların üstündedirler. Aşağıda Hevsel Bahçeleri ve Dicle. Gündüz kırk dereceyi bulacak.",
         "Mert jogs along the top of the black basalt wall and stops at a tower edge; Ali catches up holding a water bottle; both look down at the "
         "green gardens and the river as the sun rises.",
         [("ali", "Bu surlar ve Hevsel Bahçeleri UNESCO listesinde.", "breathless, impressed"),
          ("mert", "Sabahın altısında bile terledim Ali.", "panting")],
         "slow crane-up along the wall revealing the gardens and the river", h="sıcak"),
       S("08:00 sabah", "han", ["mert", "ali", "hanci"], "Bal Handa",
         "Hasanpaşa Hanı'nda kahvaltıdadırlar. Kahvaltı salonu sahibi Bingöl balını tadar ve 25 kilo alır.",
         "The breakfast salon owner dips a spoon into a jar of Bingöl honey, tastes it, closes his eyes and nods; Ali slides the honey crate "
         "across the table and they shake hands.",
         [("hanci", "Bingöl balı... Yirmi beş kilo bırakın, kahvaltıma yakışır.", "satisfied"),
          ("ali", "Kilosu bin yüz. Afiyet olsun misafirlerinize.", "polite")],
         "static medium three-shot at the breakfast table",
         t=[U(25, "kg", 1100, "satis", "Bingöl balı, kahvaltı salonuna ({adet} kg x {fiyat} TL)"), T("yemek", 900, "Handa kahvaltı (2 kişi)")]),
       S("11:30 öğle", "ulucami", ["mert", "ali"], "Avluda Serinlik",
         "Ulu Cami'nin avlusundaki şadırvanda yüzlerini yıkarlar. Ali kalan balın da siparişlerle satıldığını söyler.",
         "Mert splashes cool water from the fountain onto his face and neck; Ali sits on the stone edge checking his phone and holds it up "
         "triumphantly.",
         [("ali", "Kalan yirmi beş kilo bal da siparişle gitti!", "happy"),
          ("mert", "Bingöl'ün arıları Diyarbakır'da çalışıyor.", "grinning, wet face")],
         "static wide shot of the courtyard, slow push-in", h="sıcak",
         t=U(25, "kg", 1100, "satis", "Bingöl balı, takipçi siparişi ({adet} kg x {fiyat} TL)")),
       S("15:00 ikindi", "carsi", ["mert", "ali", "esnaf"], "Kuru Dolmalık",
         "Çarşıda iplere dizili kurutulmuş patlıcan ve biberleri görürler. Kurusu bozulmaz: Mert'in kuralına uygun. 30 kilo alırlar.",
         "The shopkeeper takes down a long string of dried hollowed eggplants and lays it over Mert's arms; Mert holds it up and turns to Ali, "
         "raising one finger as if reciting a rule.",
         [("mert", "Kural bir: iki günde bozulan mal almıyoruz. Bu iki yıl dayanır!", "proud"),
          ("esnaf", "Kışın dolmasını yapan bizi anar. Kilosu dört yüz elli.", "smiling")],
         "slow tracking shot along the hanging strings",
         t=U(30, "kg", 450, "alis", "Kurutulmuş dolmalık patlıcan ve biber ({adet} kg x {fiyat} TL)")),
       S("20:30 akşam", "cigerci", ["mert", "ali"], "Ciğer Kebabı",
         "Akşam ciğer kebabı yerler. Kömür ateşi, sıcak gece, kalabalık bir sokak.",
         "Mert wraps a skewer of grilled liver in thin flatbread with onions and parsley and bites it, eyes wide; Ali laughs and hands him a "
         "glass of ayran.",
         [("mert", "Diyarbakır'da gece de kırk derece, ciğer de ateş!", "mouth full, happy"),
          ("ali", "Ayranı iç, sonra konuş.", "laughing")],
         "static medium two-shot at a small table by the grill",
         t=T("yemek", 800, "Ciğer kebabı (2 kişi)")),
       S("21:30 gece", "cigerci", ["mert", "ali", "bahcivan"], "Kırk Kiloluk Karpuz",
         "Kaldırımdaki dev karpuzların sahibi Mert'e meydan okur: kırk kiloluk karpuzu kucaklayıp kaldırırsa bedava.",
         "The watermelon seller pats an enormous watermelon on the pile and points at Mert; Mert rolls up his sleeves, bends his knees and wraps "
         "his arms around it; Ali covers his eyes with one hand.",
         [("bahcivan", "Kaldırırsan senin. Kaldıramazsan iki tane alırsın!", "challenging, laughing"),
          ("mert", "Ali, kasadan iki karpuz parası ayır.", "straining")],
         "static medium shot from the sidewalk, slight push-in",
         t=[T("konaklama", 1300, "Otel, 1 gece"), U(2, "bilet", 200, "ulasim", "Diyarbakır-Batman otobüsü ({adet} x {fiyat} TL)")]),
   ],
   misafir={"hanci": ("KAHVALTICI", "BREAKFAST SALON OWNER, a 50-year-old Turkish man, tall, a neat grey beard, a white shirt and a black vest",
                      "adult male voice, calm and pleased, Diyarbakır Turkish"),
            "esnaf": ("ESNAF", "SHOPKEEPER, a 60-year-old Turkish man, slim, a white skullcap, a grey beard and a long light shirt",
                      "elderly male voice, kind, Diyarbakır Turkish"),
            "bahcivan": ("KARPUZCU", "WATERMELON SELLER, a 45-year-old Turkish man, huge and strong, a big belly, a black mustache, a sleeveless "
                         "white undershirt and a straw hat", "adult male voice, booming, playful Diyarbakır Turkish")},
   ay=AY, hava="sıcak", urun="Diyarbakır karpuzu, ciğer kebabı, kurutulmuş dolmalık; Surlar ve Hevsel Bahçeleri (UNESCO), Ulu Cami",
   sponsor="Kahvaltı salonu, yöresel gıda ya da turizm alanında",
   kapak=("cigerci", ["mert", "bahcivan"], "Mert strains with all his strength to lift a gigantic watermelon in his arms on a lively night street, "
          "the watermelon seller laughing behind him, glowing charcoal grills", "Dev bir karpuzu kaldırmaya çalışan Mert."),
   yakinda=("sur", ["mert", "ali"], "Two silhouettes on top of massive black ancient city walls at dawn, a burning orange sun rising over green "
            "gardens and a river", "Şafakta kara surların üstünde iki silüet."),
   tiktok="40 kiloluk karpuzu kaldırırsam bedava 🍉😂 #JozhStudios",
   ig=("Güneydoğu sezonu başladı! ☀️ Şafakta Diyarbakır Surları'nda koştuk, Hevsel Bahçeleri'ni izledik.\n\n"
       "Hasanpaşa Hanı'nda kahvaltıda Bingöl balının hepsi satıldı. Akşam ciğer kebabından sonra karpuzcu meydan okudu: 40 kiloluk karpuzu kaldırırsan bedava! 🍉\n\n"
       "Sizce Mert kaldırdı mı? Kasa: {KASA}"),
   tags=["#Diyarbakır", "#HevselBahçeleri", "#Karpuz"],
   son="Mert kırk kiloluk karpuzu kaldırabilecek mi?",
   teaser="Kara surlar, ateş gibi bir gece ve kırk kiloluk bir iddia. Bölüm 21: Diyarbakır. Pek yakında.")

# ======================================================================= 22 BATMAN
EP(22, "Batman", "Suyun Altındaki Şehir",
   "Karpuz iddiasının sonu, Hasankeyf'te tekne ve ilk takipçi buluşması.",
   "Sabah Batman'a giderken iddianın sonu ortaya çıkar: Mert karpuzu kaldırmış ama kucağından düşürmüştür; karpuzcu iki karpuzu yine de "
   "hediye etmiştir. Batman'da Hasankeyf'e geçip baraj gölünün üstünde tekneyle eski Hasankeyf'in yerini gezer, yeni yerine taşınan tarihi "
   "eserleri görürler. Öğlen ilk takipçi buluşması olur: lise öğrencisi Berfin, onlara annesinin yaptığı yemeği getirmiştir. Kurutulmuş "
   "dolmalığın bir kısmı Batman'da satılır. Akşam Ali'nin yüzü güneşte yanmış Mert'e bakınca kızarır: Siirt'e kırk beş derecede gidecekler.",
   {"otobus": ("Batman yolu, otobüs", "the interior of an intercity bus on a sunny road to Batman: blue seats, two big watermelons on the seat "
               "beside them, dry golden hills outside"),
    "tekne": ("Hasankeyf, baraj gölünde tekne", "a small tour boat on the wide turquoise dam lake at Hasankeyf: steep limestone cliffs with old "
              "cave openings rising from the water, the top of an old stone structure just above the surface"),
    "park": ("Yeni Hasankeyf, kültür parkı", "the new Hasankeyf cultural park: historic stone monuments relocated onto a green landscaped "
             "terrace, a round tomb with turquoise tiles, palm-free dry hills and the lake behind"),
    "kafe": ("Batman, çay bahçesi", "a shaded tea garden in Batman: plastic tables under a vine canopy, a big fan, glasses of tea"),
    "sokak": ("Batman sokağı", "a busy shopping street in Batman in the late afternoon: shop awnings, a grocer with crates, heat haze")},
   [
       S("08:30 sabah", "otobus", ["mert", "ali"], "İddianın Sonu",
         "Otobüste iki dev karpuzun yanında otururlar. Mert karpuzu kaldırmış ama düşürmüştür; karpuzcu yine de iki tane hediye etmiştir.",
         "Mert sits beside two huge watermelons on the bus seat and pats one proudly; Ali, by the window, mimics with his hands the watermelon "
         "falling and bursting, and both burst out laughing.",
         [("mert", "Kaldırdım ama! Sadece... yere indirmeyi beceremedim.", "defensive, laughing"),
          ("ali", "Karpuz patladı, karpuzcu güldü, bize iki tane verdi.", "laughing")],
         "static medium two-shot across the aisle", h="sıcak"),
       S("10:30 sabah", "tekne", ["mert", "ali", "kaptan"], "Suyun Altında",
         "Hasankeyf'te tekneyle baraj gölüne açılırlar. Kaptan eski şehrin suyun altında kaldığını, eserlerin taşındığını anlatır.",
         "The boat glides slowly past the steep limestone cliffs with ancient cave openings; the captain points down at the water; Mert leans over "
         "the side looking into the turquoise depth.",
         [("kaptan", "Eski çarşı şurada, suyun altında. Bazı eserleri taşıdılar.", "quiet, nostalgic"),
          ("mert", "Bir şehrin üstünde tekneyle geziyoruz yani.", "hushed")],
         "slow tracking shot from the boat along the cliffs", h="sıcak",
         t=U(2, "kişi", 250, "diger_gider", "Hasankeyf tekne turu ({adet} x {fiyat} TL)")),
       S("12:00 öğle", "park", ["mert", "ali"], "Taşınan Türbe",
         "Kültür parkında yeni yerine taşınmış turkuaz çinili türbenin önündedirler.",
         "Mert and Ali walk up the terrace path to the round tomb with turquoise tiles and stop in its shade; Ali reads from his phone; Mert "
         "touches the old stone base.",
         [("ali", "Bu türbeyi tek parça hâlinde taşımışlar, kilometrelerce.", "amazed"),
          ("mert", "Biz iki çuval kayısıyı taşırken öldük.", "joking")],
         "slow crane-up from their faces to the tiled dome", h="sıcak"),
       S("13:30 öğle", "kafe", ["mert", "ali", "berfin"], "İlk Takipçi",
         "Çay bahçesinde ilk takipçi buluşması: lise öğrencisi Berfin, annesinin yaptığı içli köfteyi getirmiştir.",
         "Berfin places a covered plate on the table and lifts the cloth to reveal fried stuffed meatballs; Mert stands up and bows dramatically "
         "while Ali shakes her hand.",
         [("berfin", "Annem dedi ki, bu çocuklar aç gezer, götür.", "shy, smiling"),
          ("mert", "Annene söyle, Malatya'dan selam var!", "touched, warm")],
         "static medium three-shot at the table"),
       S("17:00 ikindi", "sokak", ["ali", "manav"], "Batman'da Dolmalık",
         "Bir manav 15 kilo kuru dolmalık alır. Ali kalan 15 kiloyu Siirt'e saklar.",
         "The grocer inspects a string of dried peppers and nods, then counts banknotes into Ali's hand; Ali ties the remaining strings back into "
         "a bag.",
         [("manav", "Kurusu iyi. On beş kilo, altı yüz elliden.", "practical"),
          ("ali", "Hayırlı olsun. Kalanı Siirt'e.", "polite")],
         "static medium two-shot at the stall", h="sıcak",
         t=U(15, "kg", 650, "satis", "Kurutulmuş dolmalık, Batman'da ({adet} kg x {fiyat} TL)")),
       S("20:00 akşam", "sokak", ["mert", "ali"], "Kırk Beş Derece",
         "Akşam Ali, Mert'in güneşten kıpkırmızı olmuş ensesine bakar. Yarın Siirt'te hava kırk beş derece olacaktır.",
         "Ali looks at the back of Mert's bright red sunburned neck and winces; Mert touches it and yelps; Ali holds up his phone showing the "
         "weather forecast.",
         [("ali", "Yarın Siirt'te kırk beş derece. Şapka alıyoruz.", "serious"),
          ("mert", "Şapka değil Ali, buzdolabı alalım.", "whining, comic")],
         "static medium two-shot on the street",
         t=[T("yemek", 600, "Akşam yemeği"), T("konaklama", 1100, "Otel, 1 gece"), U(2, "bilet", 250, "ulasim", "Batman-Siirt otobüsü ({adet} x {fiyat} TL)")]),
   ],
   misafir={"kaptan": ("TEKNE KAPTANI", "BOAT CAPTAIN, a 52-year-old Turkish man, sun-darkened, a white stubble, a faded blue cap and a light "
                       "short-sleeved shirt", "adult male voice, quiet and nostalgic"),
            "berfin": ("BERFİN", "BERFİN, a 16-year-old Turkish high-school girl, slim, long black hair in a braid, a light yellow t-shirt and "
                       "jeans, a backpack", "teenage female voice, shy and friendly"),
            "manav": ("MANAV", "GROCER, a 48-year-old Turkish man, round face, a short grey beard, an apron", "adult male voice, practical")},
   ay=AY, hava="sıcak", urun="İçli köfte, Hasankeyf, Raman Dağı; Türkiye'nin ilk petrol şehirlerinden",
   sponsor="Turizm, tekne turu ya da yöresel gıda alanında",
   kapak=("tekne", ["mert", "ali"], "Mert and Ali lean over the side of a small boat gliding past towering limestone cliffs with ancient caves "
          "on a turquoise lake, looking down into the water in wonder", "Turkuaz gölde mağaralı kayalıkların önünden geçen teknede Mert ve Ali."),
   yakinda=("tekne", ["mert"], "Mert's silhouette leaning over a boat railing, his reflection on dark turquoise water, the faint shape of an old "
            "stone structure beneath the surface", "Suya bakan bir silüet ve suyun altında belli belirsiz eski taşlar."),
   tiktok="Suyun altında kalan şehrin üstünde tekneyle gezdik 🚤 #JozhStudios",
   ig=("Mert karpuzu kaldırdı... ve düşürdü. 😂 Karpuzcu yine de iki tane verdi.\n\n"
       "Hasankeyf'te baraj gölünde tekneyle eski şehrin üstünden geçtik, taşınan türbeyi gördük. İlk takipçi buluşmamızda Berfin annesinin içli köftesini getirdi. 🥹\n\n"
       "Yarın Siirt: 45 derece. Kasa: {KASA}"),
   tags=["#Batman", "#Hasankeyf", "#TakipçiBuluşması"],
   son="Yarın Siirt'te hava kırk beş derece ve Mert'in ensesi şimdiden yanmış.",
   teaser="Suyun altındaki şehir, ilk takipçi ve kırk beş dereceye hazırlık. Bölüm 22: Batman. Pek yakında.")

# ======================================================================= 23 SİİRT
EP(23, "Siirt", "Fıstık ve Battaniye",
   "Kırk beş derecede Siirt fıstığı, tiftik battaniyesi ve perde pilavı.",
   "Siirt'e geldiklerinde Mert'in sırtı yanmıştır; Ali eczaneden krem, pazardan iki hasır şapka alır. Kalan dolmalık bir lokantaya satılır. "
   "Fıstık bahçesinde iri ve yağlı Siirt fıstığını tadar, 60 kilo alırlar. Bir atölyede tiftik keçisinin yününden dokunan Siirt "
   "battaniyesini görürler ve kışın satmak için iki tane alırlar. Akşam perde pilavını yerken Mert battaniyeye sarılıp 'temmuzda battaniye "
   "satan ilk tüccar' olmakla övünür. Gece Cizre'den bir düğün daveti gelir.",
   {"carsi": ("Siirt çarşısı", "a hot sunny market street in Siirt: a pharmacy with a green cross, a stall of straw hats, shade cloths "
              "stretched overhead"),
    "lokanta": ("Siirt lokantası", "a traditional Siirt restaurant: tiled walls, a big copper pot, steel trays of stews"),
    "bahce": ("Fıstık bahçesi", "a pistachio orchard on dry hills near Siirt: low pistachio trees heavy with clusters of pink-red pistachio "
              "hulls, dry golden soil, harsh bright sun"),
    "atolye": ("Battaniye atölyesi", "a small weaving workshop in Siirt: a wide wooden loom with a soft white mohair blanket in progress, "
               "folded blankets with simple colored stripes on shelves"),
    "sofra": ("Perde pilavı sofrası", "a family-style restaurant table in Siirt at night: a golden domed perde pilaf with a crisp pastry crust "
              "being cut open, steam rising, salad and ayran")},
   [
       S("09:00 sabah", "carsi", ["mert", "ali"], "Şapka ve Krem",
         "Mert'in sırtı yanmıştır. Ali eczaneden krem ve pazardan iki hasır şapka alır.",
         "Ali puts a straw hat on Mert's head and adjusts it, then squeezes cream onto Mert's red shoulders; Mert winces and complains while Ali "
         "laughs.",
         [("ali", "Yavaş dur, kremi sürüyorum.", "patient, amused"),
          ("mert", "Ali, ben artık kızarmış biberim.", "groaning")],
         "static medium two-shot under the shade cloth", h="sıcak",
         t=T("diger_gider", 700, "Güneş kremi ve iki hasır şapka")),
       S("10:30 iç-gündüz", "lokanta", ["ali", "lokantaci"], "Son Dolmalık",
         "Kalan 15 kilo kuru dolmalık bir lokantaya satılır.",
         "The restaurant owner takes the bag of dried eggplants and peppers and weighs it on a kitchen scale; Ali writes the amount in his "
         "notebook and they shake hands.",
         [("lokantaci", "Kışın dolma yapacağım, on beş kilonun hepsi.", "satisfied"),
          ("ali", "Bu kez ilk alıştan yüzde kırk kâr. Mert duymasın, şımarır.", "whispering joke")],
         "static medium two-shot at the counter",
         t=U(15, "kg", 650, "satis", "Kurutulmuş dolmalık, lokantaya ({adet} kg x {fiyat} TL)")),
       S("12:30 öğle", "bahce", ["mert", "ali", "fistikci"], "Siirt Fıstığı",
         "Fıstık bahçesinde Siirt fıstığının iri ve yağlı olduğunu görürler. Bahçe sahibi bir avuç kırıp ikram eder.",
         "The orchard owner cracks a handful of large pistachios and pours them into Mert's palm; Mert eats one under his straw hat and stares at "
         "the shell, Ali picks a pink cluster from a branch.",
         [("fistikci", "Siirt fıstığı iri olur, yağlı olur. Ağzına koyduğun an anlarsın.", "proud"),
          ("mert", "Bu fıstık değil, ceviz kadar!", "amazed, exaggerating")],
         "slow push-in under the trees", h="sıcak"),
       S("13:00 öğle", "bahce", ["ali", "fistikci"], "Altmış Kilo",
         "Altmış kilo kabuklu Siirt fıstığı alırlar. Sezonun ilk büyük fıstık alımı.",
         "The orchard owner pours pistachios from a sack onto a scale; Ali counts a thick stack of money into his hand and they bump fists.",
         [("fistikci", "Kilosu yedi yüz elli. Antep'e de götürseniz mahcup olmazsınız.", "confident"),
          ("ali", "Antep'e fıstık götürmek... Kars'a kaşar gibi olmasın.", "laughing")],
         "static medium two-shot at the scale", h="sıcak",
         t=U(60, "kg", 750, "alis", "Kabuklu Siirt fıstığı ({adet} kg x {fiyat} TL)")),
       S("16:30 iç-gündüz", "atolye", ["mert", "ali", "dokumaci"], "Temmuzda Battaniye",
         "Tiftik keçisinin yününden dokunan Siirt battaniyesini görürler. Kış için iki tane alırlar.",
         "The weaver drapes a soft white striped mohair blanket over Mert's shoulders; Mert wraps himself in it in the heat and poses like a "
         "king while Ali takes a photo.",
         [("dokumaci", "Tiftik keçisinin yünü. Hafiftir ama sıcak tutar.", "gentle"),
          ("mert", "Temmuzda battaniye alan ilk tüccar benim!", "proud, comic")],
         "static medium three-shot by the loom",
         t=U(2, "battaniye", 4500, "alis", "Siirt tiftik battaniyesi ({adet} x {fiyat} TL)")),
       S("21:00 iç-gece", "sofra", ["mert", "ali"], "Perde Pilavı ve Davet",
         "Akşam perde pilavını keserler. Ali'nin telefonuna Cizre'den bir düğün daveti gelir: Berfin'in kuzeni evleniyordur.",
         "Ali cuts open the golden pastry dome of the perde pilaf and steam rises; his phone buzzes on the table, he reads it and raises his "
         "eyebrows; Mert leans in to read too.",
         [("ali", "Berfin'in kuzeni Cizre'de evleniyor. Bizi düğüne çağırıyorlar!", "surprised"),
          ("mert", "Düğün mü? Halay çekeceğiz Ali!", "excited")],
         "slow push-in on the pilaf and their faces",
         t=[T("yemek", 800, "Perde pilavı sofrası"), T("konaklama", 1100, "Otel, 1 gece"), U(2, "bilet", 350, "ulasim", "Siirt-Cizre otobüsü ({adet} x {fiyat} TL)")]),
   ],
   misafir={"lokantaci": ("LOKANTACI", "RESTAURANT OWNER, a 55-year-old Turkish man, stout, a grey beard, a white apron", "mature male voice"),
            "fistikci": ("FISTIK ÜRETİCİSİ", "PISTACHIO FARMER, a 50-year-old Turkish man, lean, sun-darkened, a black mustache, a white "
                         "skullcap and a light shirt", "adult male voice, proud Siirt Turkish"),
            "dokumaci": ("DOKUMACI", "WEAVER, a 62-year-old Turkish woman, small, a white headscarf, a dark vest and a long skirt",
                         "elderly female voice, gentle")},
   ay=AY, hava="sıcak", urun="Siirt fıstığı, Siirt battaniyesi (tiftik), perde pilavı, büryan",
   sponsor="Siirt fıstığı, tiftik battaniyesi ya da yöresel yemek alanında",
   kapak=("atolye", ["mert", "ali"], "Mert wrapped like a king in a soft white mohair blanket in summer heat, wearing a straw hat, Ali laughing "
          "and taking a photo, loom behind", "Temmuz sıcağında battaniyeye sarılıp kral gibi poz veren Mert."),
   yakinda=("bahce", ["mert"], "A pink cluster of pistachios glowing in harsh backlight in the foreground, Mert's straw-hatted silhouette "
            "behind among the trees", "Ters ışıkta parlayan fıstık salkımı ve hasır şapkalı silüet."),
   tiktok="45 derecede battaniye aldım 🥵 ve ceviz kadar Siirt fıstığı #JozhStudios",
   ig=("Siirt'te 45 derece! Mert'in sırtı yandı, Ali şapka aldı. 🥵\n\n"
       "Ceviz kadar iri Siirt fıstığından 60 kilo aldık, perde pilavını kestik. Mert ise temmuzda tiftik battaniyesi aldı. 🧣\n\n"
       "Gece Cizre'den bir düğün daveti geldi! Kasa: {KASA}"),
   tags=["#Siirt", "#SiirtFıstığı", "#PerdePilavı"],
   son="Cizre'den düğün daveti: Berfin'in kuzeni evleniyor.",
   teaser="Kırk beş derece, ceviz kadar fıstık ve temmuzda battaniye. Bölüm 23: Siirt. Pek yakında.")

# ======================================================================= 24 ŞIRNAK
EP(24, "Şırnak", "Cizre'de Düğün",
   "Dicle kıyısında bir düğün, Cudi Dağı manzarası ve halayda bir pazarlık.",
   "Cizre'de Dicle kıyısında sabah serinliğinde yürür, ufukta Cudi Dağı'nı görürler. Nuh'un gemisinin bu dağda karaya oturduğuna dair "
   "anlatılar dinlerler. Fıstığın bir kısmını bir tatlıcıya satarlar. Düğünde davul zurna eşliğinde halay çekerler; Mert halayın başına "
   "geçer, Ali ritmi tutturamaz. Düğünde damadın babası fıstığın kalanını çerez için ister. Gece Ali sahte etiketli fıstık videolarından söz "
   "eden bir takipçi mesajı okur: 'Antep'te dikkat edin.'",
   {"dicle": ("Dicle kıyısı, Cizre", "the bank of the Tigris river at Cizre in the early morning: a wide brown-green river, palm-free dry banks, "
              "a stone embankment, and the long ridge of Mount Cudi on the horizon"),
    "tatlici": ("Tatlıcı", "a dessert shop in Cizre: glass counter with trays of baklava and kadayıf, ceiling fans, white tiles"),
    "dugun": ("Düğün alanı", "an open-air wedding courtyard in Cizre at night: strings of colorful lights, plastic chairs around a dance area, "
              "a drum and zurna players at one side, guests in festive clothes far in the background"),
    "otel": ("Otel odası", "a simple hotel room in Cizre at night: two beds, an air conditioner, sacks of pistachios by the wall")},
   [
       S("07:00 sabah", "dicle", ["mert", "ali"], "Cudi'ye Bakış",
         "Sabah Dicle kıyısında yürürler. Ufukta Cudi Dağı; yaşlılar Nuh'un gemisinin bu dağda karaya oturduğunu anlatır.",
         "Mert and Ali walk along the stone embankment by the wide river; Ali stops and points at the long mountain ridge on the horizon, Mert "
         "shades his eyes under his straw hat.",
         [("ali", "Rivayete göre Nuh'un gemisi şu dağda karaya oturmuş.", "thoughtful"),
          ("mert", "Gemi bile buraya kadar gelmiş, biz de geldik.", "smiling")],
         "slow tracking shot along the embankment", h="sıcak"),
       S("10:30 iç-gündüz", "tatlici", ["mert", "tatlici"], "Fıstık Tatlıcıya",
         "Bir tatlıcı 20 kilo Siirt fıstığını baklava için alır.",
         "The dessert maker cracks a pistachio, inspects the bright green kernel and nods; Mert lifts a sack onto the counter and they shake hands "
         "over the trays of baklava.",
         [("tatlici", "Bu yeşilliği baklavaya yakışır. Yirmi kilo, binden.", "pleased"),
          ("mert", "Tatlınızı tatmadan gitmeyiz ama.", "charming")],
         "static medium two-shot over the glass counter",
         t=U(20, "kg", 1000, "satis", "Siirt fıstığı, tatlıcıya ({adet} kg x {fiyat} TL)")),
       S("13:00 iç-gündüz", "tatlici", ["mert", "ali"], "Öğle Sıcağı",
         "Öğle sıcağında tatlıcıda dinlenirler. Ali düğün için ikisine birer gömlek ütületmeyi düşünür; Mert tek gömleğiyle gurur duyar.",
         "Mert and Ali sit under the ceiling fan eating small pieces of pistachio baklava; Ali points at Mert's black t-shirt and raises an "
         "eyebrow; Mert pulls at his t-shirt proudly.",
         [("ali", "Düğüne bu tişörtle mi gideceksin?", "teasing"),
          ("mert", "Bu tişört benim imzam. Halayı da bununla çekerim.", "proud")],
         "static medium two-shot at a small table",
         t=T("yemek", 600, "Öğle yemeği ve baklava")),
       S("21:00 gece", "dugun", ["mert", "ali"], "Halayın Başı",
         "Düğünde davul zurna çalar. Mert halayın başına geçip mendil sallar; Ali ritmi tutturamaz ama vazgeçmez.",
         "Mert leads a line dance waving a white handkerchief high, stepping in rhythm; Ali next to him holds his pinky finger, steps on the wrong "
         "beat, laughs and keeps trying.",
         [("mert", "Sağ, sol, sağ, vur! Ali, ritme gel!", "shouting over music, joyful"),
          ("ali", "Ben hesap yaparım Mert, ritim tutamam!", "laughing")],
         "smooth orbit around them at shoulder height"),
       S("22:30 gece", "dugun", ["mert", "ali", "baba"], "Damadın Babası",
         "Damadın babası kalan fıstığı düğün çerezi için ister. Ali halaydan nefes nefese çıkıp pazarlığa girer.",
         "The groom's father pulls Ali aside from the dance and points at the sacks of pistachios by the wall; Ali, out of breath, nods and shakes "
         "his hand; Mert waves from the dance line.",
         [("baba", "Kalan fıstıkların hepsi düğün çerezine. Bin yüzden olur mu?", "warm, generous"),
          ("ali", "Sizin düğününüze bin olsun amca. Hayırlı olsun.", "touched")],
         "static medium two-shot by the wall, lights blurred behind",
         t=U(40, "kg", 1000, "satis", "Siirt fıstığı, düğün çerezi ({adet} kg x {fiyat} TL)")),
       S("23:50 iç-gece", "otel", ["mert", "ali"], "Antep'te Dikkat",
         "Gece otelde Ali bir takipçinin mesajını okur: Antep'te sahte etiketli fıstık satanlar var, dikkat edin.",
         "Mert collapses face-down onto the bed, still wearing his straw hat; Ali sits on the other bed reading his phone, frowns and reads the "
         "message aloud; Mert lifts his head.",
         [("ali", "Bir takipçi yazmış: 'Antep'te sahte etiketli fıstığa dikkat edin.'", "serious"),
          ("mert", "Sahte fıstık mı? Bizi kimse kandıramaz.", "sleepy, overconfident")],
         "static high-angle shot from the corner",
         t=[T("konaklama", 1100, "Otel, 1 gece"), U(2, "bilet", 350, "ulasim", "Cizre-Mardin otobüsü ({adet} x {fiyat} TL)")]),
   ],
   misafir={"tatlici": ("TATLICI", "DESSERT MAKER, a 46-year-old Turkish man, round face, a black beard, a white baker's cap and apron",
                        "adult male voice, pleased"),
            "baba": ("DAMADIN BABASI", "GROOM'S FATHER, a 60-year-old Turkish man, dignified, a grey mustache, a dark suit jacket over a white "
                     "shirt, a red flower pin", "elderly male voice, warm and generous, Southeastern Turkish")},
   ay=AY, hava="sıcak", urun="Cudi Dağı, Dicle kıyısı, Cizre; yöresel tatlılar ve bal",
   sponsor="Tatlıcı, düğün ve organizasyon ya da yöresel gıda alanında",
   kapak=("dugun", ["mert", "ali"], "Mert leads a joyful line dance under colorful string lights waving a white handkerchief, Ali beside him "
          "laughing and stepping wrong, festive night", "Rengârenk ışıklar altında halay başı Mert ve ritmi kaçıran Ali."),
   yakinda=("dicle", ["mert", "ali"], "Two small silhouettes on a riverbank at dawn facing a long dark mountain ridge on the horizon, mist "
            "over the river", "Şafakta nehir kıyısında uzaktaki dağa bakan iki silüet."),
   tiktok="Cizre'de düğüne davet edildik 💃 Halay başı Mert! #JozhStudios",
   ig=("Cizre'de Dicle kıyısında Cudi Dağı'na baktık, Nuh'un gemisinin hikâyesini dinledik. ⛰️\n\n"
       "Gece Berfin'in kuzeninin düğünündeydik! Mert halay başı, Ali ritimsiz ama mutlu. 💃 Fıstığın kalanı düğün çerezi oldu.\n\n"
       "Bir takipçimiz uyardı: 'Antep'te sahte etiketli fıstığa dikkat!' Kasa: {KASA}"),
   tags=["#Şırnak", "#Cizre", "#Halay"],
   son="Bir takipçi uyarıyor: Antep'te sahte etiketli fıstık satanlar var.",
   teaser="Dicle kıyısında şafak, halay başında Mert ve bir uyarı mesajı. Bölüm 24: Şırnak. Pek yakında.")

# ======================================================================= 25 MARDİN
EP(25, "Mardin", "Taşın Şehri",
   "Taş evlerin arasında kaybolurlar; bıttım sabunu, Deyrulzafaran ve Mezopotamya ovasına bakan bir teras.",
   "Mardin'in taş merdivenli sokaklarında kaybolurlar; bir çocuk onları çarşıya götürür. Siirt battaniyelerinden biri bir butik otelde "
   "satılır. Deyrulzafaran Manastırı'nın sarı taşlarını görürler. Bir sabun atölyesinde menengiç (bıttım) ağacının meyvesinden yapılan "
   "geleneksel sabunu öğrenir, 300 kalıp alırlar. Akşam terasta Mezopotamya ovasının ışıkları yanarken sembusek yerler. Ali bir mesajı "
   "okuyunca yüzü değişir: babası arıyordur.",
   {"sokak": ("Mardin taş sokakları", "a steep narrow stone-stepped alley in old Mardin: honey-colored limestone houses with carved windows "
              "and arches, laundry lines, a donkey-wide passage"),
    "otel": ("Butik otel", "the arched stone courtyard of a boutique hotel in old Mardin: carved stone walls, a fountain, cushions on a "
             "stone bench"),
    "manastir": ("Deyrulzafaran Manastırı", "the Deyrulzafaran Monastery near Mardin: a large honey-yellow stone monastery with arched "
                 "gates and a courtyard, dry rocky hills around"),
    "sabun": ("Sabun atölyesi", "a traditional soap workshop in Mardin: rows of dark green bıttım soap bars stacked in towers to dry, a "
              "large copper cauldron, stone vaults"),
    "teras": ("Teras, Mezopotamya manzarası", "a stone rooftop terrace in Mardin at dusk overlooking the vast flat Mesopotamian plain with "
              "lights starting to glow, a low table with sembusek and tea")},
   [
       S("08:30 sabah", "sokak", ["mert", "ali", "cocuk"], "Taşın İçinde Kaybolmak",
         "Taş merdivenli sokaklarda kaybolurlar. Mahalleli bir çocuk, Yusuf, onları çarşıya götürmeyi teklif eder.",
         "Mert and Ali stop at a fork of two identical stone stairways, each pointing a different way; a boy appears at the top of the stairs, "
         "grins and waves for them to follow.",
         [("cocuk", "Abi, çarşı bu taraf. Turistler hep oraya gider, yanlış!", "cheeky"),
          ("mert", "Biz turist değiliz, tüccarız!", "mock offended")],
         "slow crane-up from the stairs to the boy", h="sıcak"),
       S("10:00 sabah", "otel", ["ali", "otelci"], "Bir Battaniye",
         "Butik otelin sahibi Siirt battaniyelerinden birini kış için alır. Ali ikinciyi Kapadokya'ya saklamaya karar verir.",
         "The hotel owner unfolds the white mohair blanket over a stone bench and smooths it with her hand; Ali hands her the folded blanket's "
         "twin, then takes it back with a smile.",
         [("otelci", "Kışın bu taş odalar soğuk olur. Birini alırım.", "practical"),
          ("ali", "Diğerini kışa, Kapadokya'ya saklıyoruz.", "planning ahead")],
         "static medium two-shot in the courtyard",
         t=U(1, "battaniye", 7500, "satis", "Siirt tiftik battaniyesi, butik otele ({adet} x {fiyat} TL)")),
       S("12:00 öğle", "manastir", ["mert", "ali"], "Sarı Taş",
         "Deyrulzafaran Manastırı'nın kapısında dururlar. Bin beş yüz yıllık sarı taş, sıcakta bile serin.",
         "Mert and Ali walk through the arched gate of the honey-yellow monastery into the cool shade; Mert places his palm on the stone wall and "
         "sighs with relief.",
         [("mert", "Taş serin Ali. Bu duvarı otel odasına götürelim.", "relieved"),
          ("ali", "Bu taşlar asırlardır bu sıcağa dayanıyor.", "awed")],
         "slow dolly-in through the gate", h="sıcak"),
       S("15:00 iç-gündüz", "sabun", ["mert", "ali", "sabuncu"], "Bıttım Sabunu",
         "Sabun ustası menengiç (bıttım) meyvesinden yapılan geleneksel sabunu anlatır. Kurusu bozulmaz, kuralı bozmaz: 300 kalıp alırlar.",
         "The soap master lifts a dark green soap bar from a tall drying tower and breaks it to show the inside; Mert smells it and nods; Ali "
         "starts counting the bars stacked in a box.",
         [("sabuncu", "Bıttım ağacının meyvesinden. Aylarca kurur, yıllarca kokar.", "proud"),
          ("ali", "Üç yüz kalıp alıyoruz. Kalıbı altmıştan.", "decisive")],
         "slow tracking shot along the soap towers",
         t=U(300, "kalıp", 60, "alis", "Mardin bıttım sabunu ({adet} kalıp x {fiyat} TL)")),
       S("20:00 akşam", "teras", ["mert", "ali"], "Ovanın Işıkları",
         "Terasta Mezopotamya ovasının ışıkları yanarken sembusek yerler. Ova deniz gibi uzanır.",
         "Mert bites into a warm sembusek and looks out at the plain where lights flicker on one by one; Ali pours tea and sits back on the low "
         "cushion beside him.",
         [("mert", "Şu ova binlerce yıldır ticaret yolu, biz de bir kervanız.", "dreamy"),
          ("ali", "İki kişilik, sabunlu bir kervan.", "smiling")],
         "slow dolly-out revealing the glowing plain",
         t=T("yemek", 900, "Akşam yemeği: sembusek ve kaburga dolması")),
       S("22:00 gece", "teras", ["ali", "~hasan"], "Babam Arıyor",
         "Ali'nin telefonu çalar: babası. Sesi yorgundur. Sera kredisi için banka bir tarih vermiştir.",
         "Ali steps to the edge of the terrace with the phone at his ear, listening in silence with his free hand on the stone parapet; the plain "
         "lights glitter behind him. His lips stay closed while his father speaks.",
         [("hasan", "Oğlum, banka eylül sonuna kadar süre verdi. Sonra seraya el koyacaklar.", "tired, from the phone speaker"),
          ("ali", "Baba, Antalya'ya geliyoruz. Birlikte bakacağız.", "steady, holding emotion")],
         "slow push-in from behind Ali",
         t=[T("konaklama", 1500, "Taş evde pansiyon, 1 gece"), U(2, "bilet", 350, "ulasim", "Mardin-Şanlıurfa otobüsü ({adet} x {fiyat} TL)")]),
   ],
   misafir={"cocuk": ("YUSUF", "YUSUF, a 10-year-old Turkish boy, skinny, a big gap-toothed grin, short black hair, a faded red t-shirt and "
                      "shorts, sandals", "child voice, cheeky and quick, Mardin Turkish"),
            "otelci": ("OTEL SAHİBİ", "HOTEL OWNER, a 44-year-old Turkish woman, elegant, short curly dark hair, a long linen dress",
                       "adult female voice, practical and warm"),
            "sabuncu": ("SABUN USTASI", "SOAP MASTER, a 66-year-old Turkish man, thin, a white beard, a faded blue work coat",
                        "elderly male voice, proud, Mardin Turkish")},
   ay=AY, hava="sıcak", urun="Bıttım (menengiç) sabunu, telkari, sembusek, kaburga dolması; taş evler, Deyrulzafaran Manastırı",
   sponsor="Sabun, telkari, butik otel ya da yöresel mutfak alanında",
   kapak=("sokak", ["mert", "ali", "cocuk"], "A cheeky boy leads Mert and Ali up a steep golden stone stairway in old Mardin, carved arches and "
          "warm stone glowing in the morning sun", "Taş merdivenlerde Mert ve Ali'ye yol gösteren çocuk."),
   yakinda=("teras", ["ali"], "Ali stands alone at the edge of a dark stone terrace with a phone to his ear, his back to the camera, the vast "
            "glittering plain at night below", "Gece terasın kenarında telefonla konuşan Ali'nin sırtı ve parıldayan ova."),
   tiktok="Mardin'de kaybolduk, 10 yaşında bir rehber bulduk 🧭 #JozhStudios",
   ig=("Mardin'in taş sokaklarında kaybolduk; Yusuf (10 yaşında) bizi kurtardı: 'Turistler hep yanlış yere gider!' 😂\n\n"
       "Deyrulzafaran'ın serin taşları, bıttım sabununun kokusu ve Mezopotamya ovasına bakan bir teras. 🌄\n\n"
       "Gece Ali'nin babası aradı. Seranın süresi eylül sonu. Kasa: {KASA}"),
   tags=["#Mardin", "#BıttımSabunu", "#Mezopotamya"],
   son="Ali'nin babası aradı: banka eylül sonuna kadar süre vermiş.",
   teaser="Taşın içinde kaybolmak, menengiç sabunu ve gece gelen bir telefon. Bölüm 25: Mardin. Pek yakında.")

# ======================================================================= 26 ŞANLIURFA
EP(26, "Şanlıurfa", "Sıra Gecesi",
   "Göbeklitepe'de şafak, Balıklıgöl, isot ve Ali'nin sahneye çıktığı gece.",
   "Ali'nin keyfi yoktur; Mert onu şafakta Göbeklitepe'ye götürür. On iki bin yıllık dikili taşların önünde Ali biraz rahatlar. Balıklıgöl'de "
   "kutsal balıkları izler, sabunların bir kısmını Bakırcılar çarşısında satarlar. Bir isot üreticisinin damında güneşte kuruyan Urfa biberini "
   "görür, 100 kilo alırlar. Gece bir sıra gecesinde Mert, Ali'yi sahneye çıkarır: Ali babasının en sevdiği türküyü söyler.",
   {"gobekli": ("Göbeklitepe", "the Göbeklitepe archaeological site at dawn: huge carved T-shaped limestone pillars with animal reliefs "
                "standing in circular enclosures under a modern protective canopy, a golden plain"),
    "balikligol": ("Balıklıgöl", "Balıklıgöl in Şanlıurfa: a long rectangular pool full of sacred carp, stone arcades and a mosque with a "
                   "minaret reflected in the green water, plane trees"),
    "carsi": ("Bakırcılar ve kapalı çarşı", "the covered bazaar of Şanlıurfa: stone vaults, shops with copper pots, spices, soaps and textiles"),
    "dam": ("İsot damı", "a flat rooftop near Şanlıurfa covered with red peppers drying under black sheets in the sun, sacks of dark "
            "purple-red isot flakes, a tin-roof shed"),
    "sira": ("Sıra gecesi odası", "a traditional sıra gecesi room in Şanlıurfa at night: guests sitting cross-legged on cushions along the "
             "walls of a stone room, a bağlama and a darbuka, small tea glasses, warm lamp light")},
   [
       S("05:40 şafak", "gobekli", ["mert", "ali"], "On İki Bin Yıl",
         "Şafakta Göbeklitepe'dedirler. Mert, keyfi yerinde olmayan Ali'ye dikili taşları gösterir.",
         "Mert and Ali stand on the walkway above the circular enclosure as the first sunlight touches the huge carved pillars; Ali, quiet and "
         "tired, slowly lifts his head toward the stones.",
         [("mert", "On iki bin yıl önce dikmişler. Bizim borç bunun yanında dün akşam.", "gentle"),
          ("ali", "Haklısın. Her şey geçiyor.", "quiet, a small smile")],
         "slow crane-down from the canopy to their faces", h="sıcak"),
       S("09:00 sabah", "balikligol", ["mert", "ali"], "Balıklıgöl",
         "Balıklıgöl'de kutsal balıkları izlerler. Ali yem atar, balıklar toplanır.",
         "Ali tosses a small handful of fish food into the green pool and dozens of carp swarm to the surface; Mert crouches beside him and "
         "laughs as the fish splash.",
         [("ali", "Babam bana küçükken balık tutmayı öğretmişti.", "nostalgic"),
          ("mert", "Burada tutmak yasak ama. Sadece izleyeceğiz.", "teasing softly")],
         "static medium two-shot at the pool edge"),
       S("11:00 sabah", "carsi", ["mert", "esnaf"], "Sabun Urfa'da",
         "Kapalı çarşıda bir dükkân 150 kalıp Mardin sabununu alır.",
         "The shopkeeper smells a green soap bar and stacks the box on his shelf next to copper pots; Mert accepts the money and points to the "
         "copper pots with curiosity.",
         [("esnaf", "Mardin'in bıttımı burada çok sorulur. Yüz elli kalıp alırım.", "practical"),
          ("mert", "Kalıbı yüz on. Bereketli olsun.", "cheerful")],
         "static medium two-shot inside the bazaar",
         t=U(150, "kalıp", 110, "satis", "Mardin bıttım sabunu, çarşıda ({adet} kalıp x {fiyat} TL)")),
       S("15:00 ikindi", "dam", ["mert", "ali", "isotcu"], "Güneşte Terleyen Biber",
         "İsot üreticisi Halil Bey biberin gündüz güneşte, gece örtü altında 'terleyerek' koyu rengini aldığını anlatır. 100 kilo alırlar.",
         "Halil lifts a black sheet to reveal glossy dark red peppers and scoops isot flakes into his palm for them to smell; Mert sneezes loudly, "
         "Ali laughs and writes in the notebook.",
         [("isotcu", "Gündüz güneş, gece örtü. Biber terler, rengi koyulaşır.", "knowledgeable"),
          ("ali", "Yüz kilo alıyoruz. Kilosu iki yüz altmış.", "decisive")],
         "slow push-in across the rooftop of drying peppers", h="sıcak",
         t=U(100, "kg", 260, "alis", "Urfa isotu ({adet} kg x {fiyat} TL)")),
       S("21:30 iç-gece", "sira", ["mert", "ali"], "Sahneye Çık",
         "Sıra gecesinde Mert, Ali'yi kolundan tutup ortaya çıkarır. Ali bağlamaya bakar, tereddüt eder.",
         "Mert stands up from the cushions and gently pulls Ali by the arm to the middle of the room; Ali hesitates, looks around at the guests, "
         "then sits down cross-legged beside the bağlama player.",
         [("mert", "Babanın sevdiği türküyü söyle Ali. O da dinlesin.", "encouraging"),
          ("ali", "Sesim kötü ama... peki.", "nervous")],
         "slow dolly-in from the wall cushions",
         t=T("yemek", 900, "Sıra gecesi yemeği: çiğ köfte, içli köfte")),
       S("22:00 iç-gece", "sira", ["ali", "mert"], "Ali'nin Türküsü",
         "Ali gözlerini kapatıp bir türkünün ilk dizelerini söyler. Mert telefonu kaldırmış, babası için kayıt alıyordur.",
         "Ali sings with his eyes closed, one hand on his knee, the bağlama strings shining in the lamp light; Mert, sitting in front, holds up "
         "his phone recording, with wet eyes and a smile.",
         [("ali", "Uzun ince bir yoldayım, gidiyorum gündüz gece...", "singing softly, emotional"),
          ("mert", "Gönderiyorum babana.", "whisper")],
         "slow push-in to Ali's face",
         t=[T("konaklama", 1300, "Otel, 1 gece"), U(2, "bilet", 300, "ulasim", "Şanlıurfa-Adıyaman otobüsü ({adet} x {fiyat} TL)")],
         kurgu="Türkü: 'Uzun İnce Bir Yoldayım' (Âşık Veysel). Yalnızca ilk dize, telif sorununa karşı kendi seslendirmenizle."),
   ],
   misafir={"esnaf": ("ESNAF", "SHOPKEEPER, a 52-year-old Turkish man, heavy-set, a grey beard, a white skullcap, a brown vest", "adult male voice"),
            "isotcu": ("HALİL BEY", "HALİL, a 57-year-old Turkish pepper farmer, wiry, a sun-darkened face, a red-and-white checked headscarf "
                       "(puşi) around his neck, a light shirt", "mature male voice, knowledgeable, Urfa Turkish")},
   ay=AY, hava="sıcak", urun="İsot (Urfa biberi), çiğ köfte, sıra gecesi; Göbeklitepe (UNESCO), Balıklıgöl",
   sponsor="İsot, yöresel mutfak ya da kültür turizmi alanında",
   kapak=("gobekli", ["mert", "ali"], "Mert and Ali stand tiny beside the giant carved T-shaped pillars of Göbeklitepe at golden dawn, looking up "
          "in awe, dramatic long shadows", "Göbeklitepe'nin dev dikili taşlarının yanında küçücük kalan Mert ve Ali."),
   yakinda=("sira", ["ali"], "Ali singing with his eyes closed in a dark stone room, his face lit only by a warm lamp, a bağlama's strings "
            "shining in the foreground", "Loş taş odada gözleri kapalı türkü söyleyen Ali."),
   tiktok="12.000 yıllık taşlar ve Ali'nin türküsü 🎶 #JozhStudios",
   ig=("Ali'nin keyfi yoktu. Şafakta Göbeklitepe'ye gittik: 12.000 yıllık taşların önünde 'her şey geçiyor' dedi. 🌅\n\n"
       "Halil Bey'in damında terleyen isotlardan 100 kilo aldık. Gece sıra gecesinde Ali babası için türkü söyledi. 🎶🥹\n\nKasa: {KASA}"),
   tags=["#Şanlıurfa", "#Göbeklitepe", "#SıraGecesi"],
   son="Ali'nin türküsü babasına gönderildi. Cevap gelecek mi?",
   teaser="On iki bin yıllık taşlar, terleyen biberler ve Ali'nin türküsü. Bölüm 26: Şanlıurfa. Pek yakında.")

# ======================================================================= 27 ADIYAMAN
EP(27, "Adıyaman", "Nemrut'un Başları",
   "Nemrut Dağı'nda gün doğumu, babadan gelen cevap, isotun satışı ve Besni'nin üzümü.",
   "Gece yarısı yola çıkıp Nemrut Dağı'nın zirvesine gün doğumunda varırlar; dev taş başların arkasından güneş yükselir. Tam o anda Ali'nin "
   "babasından sesli mesaj gelir: türküyü dinlemiş, ağlamıştır. Kahta'da Cendere Köprüsü'nün Roma taşları üzerinde yürürler. İsotun yarısını "
   "çiğ köfteciler alır. Besni'de bağdan çıkan kuru üzümü tadar, 80 kilo alırlar. Akşam Mert Gaziantep için bir plan yapar: fıstık alırken "
   "sahte etiketi nasıl anlayacaklarını Ali'ye sorar.",
   {"nemrut": ("Nemrut Dağı zirvesi", "the summit terrace of Mount Nemrut at sunrise: colossal ancient stone heads of kings and gods lined up "
               "on the ground in front of a huge cone of stones, mountain ranges below in pink morning haze"),
    "cendere": ("Cendere Köprüsü", "the ancient Roman Cendere Bridge near Kahta: a single high stone arch with tall columns, a clear green "
                "stream below, dry hills"),
    "cigkofte": ("Çiğ köfteci", "a busy çiğ köfte shop in Adıyaman: a long steel counter, a master kneading a huge tray of spicy bulgur "
                 "mixture by hand, lettuce and lemons"),
    "bag": ("Besni bağı", "a vineyard near Besni at late afternoon: rows of grapevines, grapes drying on clean cloths on the ground into "
            "golden raisins, dry hills"),
    "otel": ("Otel odası", "a simple hotel room in Adıyaman at night: two beds, a small table with a notebook, sacks of raisins and isot")},
   [
       S("05:20 şafak", "nemrut", ["mert", "ali"], "Taş Başlar",
         "Nemrut Dağı'nın zirvesinde gün doğar. Dev taş başların arkasından güneş yükselir.",
         "Mert and Ali sit wrapped in their jackets on the stone terrace beside the colossal stone heads; the sun rises over the mountains and "
         "lights up the faces of the statues and then their own faces.",
         [("mert", "Bu kral iki bin yıl önce buraya kendi heykelini koymuş.", "whisper, awed"),
          ("ali", "Biz de bir kasa sayacı koyuyoruz.", "smiling")],
         "slow lateral dolly along the row of stone heads to Mert and Ali", h="serin"),
       S("05:40 şafak", "nemrut", ["ali", "~hasan"], "Babadan Cevap",
         "Ali'nin telefonuna babasından sesli mesaj gelir. Türküyü dinlemiş ve ağlamıştır.",
         "Ali holds his phone to his ear with both hands, his eyes filling with tears as he listens; he lowers his head and smiles; Mert, out of "
         "focus behind him, looks away to give him privacy. Ali's lips stay closed.",
         [("hasan", "Oğlum, türküyü dinledim. Sesin annenin sesine benziyor. Gel, bekliyorum.", "emotional, from the phone speaker")],
         "slow push-in to Ali's face lit by the sunrise", h="serin"),
       S("10:00 sabah", "cendere", ["mert", "ali"], "Roma'dan Kalma",
         "Cendere Köprüsü'nün iki bin yıllık kemerinin üstünden yürürler.",
         "Mert and Ali walk across the top of the high Roman stone arch; Mert stops at the middle, looks down at the green stream and spreads his "
         "arms; Ali walks on, lighter than before.",
         [("ali", "Bu köprü iki bin yıldır ayakta. Biz de dayanırız.", "lighter, hopeful"),
          ("mert", "İşte benim Ali'm geri geldi!", "happy")],
         "slow crane-up from the stream to the arch", h="sıcak"),
       S("13:00 iç-gündüz", "cigkofte", ["mert", "cigkofteci"], "İsot Çiğ Köfteye",
         "Çiğ köfte ustası isotu tadar ve 50 kilo alır. Mert bir avuç çiğ köfteyi yoğurmayı dener.",
         "The master kneads a big tray of spicy bulgur and hands Mert a portion; Mert tries to knead with both hands and makes a mess, the master "
         "laughs and pays him from his apron.",
         [("cigkofteci", "Bu isot iyi terlemiş. Elli kilo bırak.", "satisfied"),
          ("mert", "Usta, yoğurmak pazarlıktan zor!", "laughing, messy hands")],
         "static medium two-shot over the counter",
         t=[U(50, "kg", 380, "satis", "Urfa isotu, çiğ köfteciye ({adet} kg x {fiyat} TL)"), T("yemek", 600, "Öğle yemeği: çiğ köfte")]),
       S("17:30 ikindi", "bag", ["mert", "ali", "bagci"], "Besni'nin Üzümü",
         "Besni'de bağcı Meryem Abla bezlerin üstünde kuruyan üzümleri gösterir. Kuru üzüm bozulmaz; 80 kilo alırlar.",
         "Meryem scoops golden raisins from a drying cloth into Ali's hands; Ali tastes one and nods; Mert lifts a full sack onto a scale with a "
         "grunt.",
         [("bagci", "Güneşte kurur, bezde döner. Kilosu yüz seksen.", "warm"),
          ("ali", "Seksen kilo alıyoruz abla.", "decisive")],
         "slow tracking shot along the drying cloths", h="sıcak",
         t=U(80, "kg", 180, "alis", "Besni kuru üzümü ({adet} kg x {fiyat} TL)")),
       S("22:30 iç-gece", "otel", ["mert", "ali"], "Sahte Etiket",
         "Gece Mert, Gaziantep'te sahte etiketi nasıl anlayacaklarını sorar. Ali'nin bir planı vardır.",
         "Mert sits on the bed holding a pistachio between two fingers like a detective; Ali, at the small table, draws a checklist in the "
         "notebook and taps it with his pen.",
         [("mert", "Sahte fıstığı nasıl anlarız Ali?", "curious"),
          ("ali", "Menşe belgesi, üretici adı ve tadım. Üçü yoksa almayız.", "confident")],
         "static medium two-shot from the doorway",
         t=[T("konaklama", 1100, "Otel, 1 gece"), U(2, "bilet", 350, "ulasim", "Adıyaman-Gaziantep otobüsü ({adet} x {fiyat} TL)")]),
   ],
   misafir={"cigkofteci": ("ÇİĞ KÖFTE USTASI", "ÇİĞ KÖFTE MASTER, a 40-year-old Turkish man, muscular forearms, a shaved head, a short "
                           "black beard, a white t-shirt and apron", "adult male voice, cheerful"),
            "bagci": ("MERYEM ABLA", "MERYEM, a 50-year-old Turkish vineyard owner, sturdy, a light green headscarf, a long floral dress and "
                      "an apron", "middle-aged female voice, warm, Adıyaman Turkish")},
   ay=AY, hava="sıcak", urun="Adıyaman çiğ köftesi, Besni üzümü, Kahta; Nemrut Dağı (UNESCO), Cendere Köprüsü",
   sponsor="Çiğ köfte, kuru meyve ya da kültür turizmi alanında",
   kapak=("nemrut", ["mert", "ali"], "Mert and Ali sit beside the colossal ancient stone heads on Mount Nemrut as the sunrise lights everything "
          "gold, huge mountain panorama", "Nemrut'ta gün doğumunda dev taş başların yanında Mert ve Ali."),
   yakinda=("nemrut", ["ali"], "Ali's tearful face in profile, lit by the first sunrise light, a phone at his ear, a colossal stone head in "
            "shadow behind him", "Gün doğumunda gözleri dolan Ali ve arkasında dev taş bir baş."),
   tiktok="Nemrut'ta gün doğumu ve babamdan gelen mesaj 🥹 #JozhStudios",
   ig=("Nemrut Dağı'nda dev taş başların arkasından güneş doğdu. 🌄 Tam o anda Ali'nin babası yazdı: türküyü dinlemiş... 🥹\n\n"
       "Cendere Köprüsü'nde Roma'nın taşlarından geçtik, çiğ köfte ustası isotu aldı, Besni'de kuru üzüm aldık.\n\n"
       "Yarın Gaziantep. Plan hazır: belge, üretici, tadım. Kasa: {KASA}"),
   tags=["#Adıyaman", "#NemrutDağı", "#Besni"],
   son="Gaziantep'te sahte etiketli fıstığa karşı plan: belge, üretici, tadım.",
   teaser="Taş başların arkasından doğan güneş ve bir babanın sesi. Bölüm 27: Adıyaman. Pek yakında.")

# ======================================================================= 28 GAZİANTEP
EP(28, "Gaziantep", "Fıstığın Sınavı",
   "Zeugma'nın mozaikleri, baklava ustası, sahte etiket ve doğru fıstık.",
   "Gaziantep'te sabah Zeugma Mozaik Müzesi'ndeki 'Çingene Kızı' mozaiğinin bakışlarıyla karşılaşırlar. Kalan sabun ve isot çarşıda satılır. "
   "Bir aracı onlara 'Antep fıstığı' etiketli ucuz çuvallar gösterir; Ali'nin üç soruluk testi aracıyı ele verir. Bakırcılar Çarşısı'nda "
   "bakır döven ustaları izler, kurulu bir baklava atölyesinde ustanın fıstığı nasıl seçtiğini öğrenirler. Gerçek üreticiden belgeli "
   "100 kilo Antep fıstığı alırlar. Gece Kilis'te ikinci taksit günü yaklaşmaktadır.",
   {"zeugma": ("Zeugma Mozaik Müzesi", "the Zeugma Mosaic Museum in Gaziantep: a large dim hall with huge colorful Roman floor mosaics lit "
               "by spotlights, the famous mosaic of a girl's face with haunting eyes on a dark wall"),
    "carsi": ("Bakırcılar Çarşısı", "the coppersmiths' bazaar in Gaziantep: narrow stone lanes with shops full of hanging copper pots and "
              "trays, a craftsman hammering copper, spice sacks"),
    "araci": ("Han avlusu", "the courtyard of an old stone han in Gaziantep: sacks of pistachios stacked by a pillar, a plastic table, shade"),
    "baklava": ("Baklava atölyesi", "a traditional baklava workshop in Gaziantep: masters rolling paper-thin dough sheets on long wooden tables, "
                "huge round trays of golden baklava, bowls of bright green pistachios"),
    "bahce": ("Fıstık bahçesi", "a pistachio orchard outside Gaziantep at late afternoon: rows of pistachio trees with pink clusters, a farm "
              "warehouse with stacked sacks and a small office desk with papers")},
   [
       S("09:00 iç-gündüz", "zeugma", ["mert", "ali"], "Çingene Kızı",
         "Zeugma Mozaik Müzesi'nde ünlü 'Çingene Kızı' mozaiğinin karşısındadırlar. Gözleri sizi her yerden izler.",
         "Mert walks slowly from left to right in front of the mosaic of a girl's face, keeping his eyes on hers; he stops, turns to Ali and "
         "points at the mosaic's eyes.",
         [("mert", "Ali, nereye gitsem bana bakıyor.", "whisper, spooked"),
          ("ali", "Belki kasayı o da kontrol ediyordur.", "whisper, joking")],
         "slow lateral dolly following Mert in front of the mosaic"),
       S("11:00 sabah", "carsi", ["mert", "ali", "bakirci"], "Bakır ve Sabun",
         "Bakırcılar Çarşısı'nda bir dükkân kalan 150 kalıp sabunu ve 50 kilo isotu alır. Usta bakır dövmeye devam eder.",
         "A coppersmith hammers a copper tray with rhythmic blows while his son stacks the soap box and isot sacks inside the shop; Ali receives "
         "the money and Mert tries a few hammer taps on scrap copper.",
         [("bakirci", "Sabunu da isotu da alırım, çarşı bunu sever.", "busy, friendly"),
          ("mert", "Usta, bu ses kasa sayacından güzel!", "delighted")],
         "slow tracking shot through the copper shop", h="sıcak",
         t=[U(150, "kalıp", 110, "satis", "Mardin bıttım sabunu, çarşıda ({adet} kalıp x {fiyat} TL)"),
            U(50, "kg", 380, "satis", "Urfa isotu, çarşıda (50 kg x 380 TL)")]),
       S("13:00 öğle", "araci", ["mert", "ali", "araci"], "Üç Soru",
         "Bir aracı 'Antep fıstığı' etiketli ucuz çuvallar gösterir. Ali'nin üç sorusu: belge, üretici, tadım. Aracı ikisine cevap veremez.",
         "The middleman pats a sack with a printed label and quotes a low price; Ali calmly asks for papers; the middleman shrugs and avoids his "
         "eyes; Mert cracks a pistachio, tastes it and spits it out.",
         [("ali", "Menşe belgesi? Üretici kim? Tadına bakabilir miyiz?", "calm, firm"),
          ("mert", "Bu Antep fıstığı değil abi. Bayat ve başka yerden.", "sure, cold")],
         "static medium three-shot, slow push-in on the label",
         kurgu="Aracı kurgusaldır; gerçek bir işletmeyi temsil etmez. Etiket yazıları prompt'ta yoktur."),
       S("15:00 iç-gündüz", "baklava", ["mert", "ali", "usta"], "Ustanın Seçimi",
         "Baklava ustası Şemsettin Usta iyi fıstığı nasıl seçtiğini gösterir: rengi, kokusu, kırılışı.",
         "The baklava master rolls a paper-thin sheet of dough and lifts it so light passes through it; then he picks a bright green pistachio "
         "from a bowl, breaks it and shows the color to Ali.",
         [("usta", "Antep fıstığı yeşildir, kokusu tatlıdır. Gözün de dilin de bilir.", "masterful"),
          ("ali", "Usta, sahtesini az önce dilimizle yakaladık.", "proud")],
         "slow push-in along the long wooden table",
         t=T("yemek", 1000, "Baklava ve öğle yemeği")),
       S("18:00 ikindi", "bahce", ["mert", "ali", "uretici"], "Belgeli Fıstık",
         "Gerçek bir üreticiden belgeli, tadımlı 100 kilo Antep fıstığı alırlar. Sezonun en büyük alımı.",
         "The producer slides papers across the office desk and opens a sack for tasting; Ali reads the papers carefully, Mert tastes and nods "
         "firmly; Ali signs and counts a large stack of money.",
         [("uretici", "Belgesi, bahçesi, tadı. Kilosu sekiz yüz elli.", "confident"),
          ("ali", "Yüz kilo alıyoruz. Üç soru da tamam.", "satisfied")],
         "static medium three-shot at the desk", h="sıcak",
         t=U(100, "kg", 850, "alis", "Belgeli kabuklu Antep fıstığı ({adet} kg x {fiyat} TL)")),
       S("22:30 gece", "bahce", ["mert", "ali"], "Seksen Bin",
         "Gece bahçede Ali hesap yapar: Kilis'te ikinci taksit, 80.000 lira. Fıstığın yarısı satılmazsa yetmeyecek.",
         "Ali sits on a sack of pistachios under a warehouse lamp writing numbers in the notebook; Mert sits beside him, reads the page and "
         "slowly exhales.",
         [("ali", "Kilis'te seksen bin. Fıstığın yarısını satmamız lazım.", "serious"),
          ("mert", "Kilis'in zeytinyağı da var ama... önce taksit.", "determined")],
         "slow push-in under the lamp",
         t=[T("konaklama", 1300, "Otel, 1 gece"), U(2, "bilet", 250, "ulasim", "Gaziantep-Kilis otobüsü ({adet} x {fiyat} TL)")]),
   ],
   misafir={"bakirci": ("BAKIRCI USTA", "COPPERSMITH, a 63-year-old Turkish man, strong arms, a white mustache, a leather apron, a hammer",
                        "elderly male voice, busy and friendly, Gaziantep Turkish"),
            "araci": ("ARACI", "MIDDLEMAN, a 35-year-old Turkish man, slick, gelled hair, a shiny short-sleeved shirt, gold chain, fidgety",
                      "adult male voice, fast talker, evasive"),
            "usta": ("ŞEMSETTİN USTA", "ŞEMSETTİN, a 67-year-old Turkish baklava master, slim, a neat white mustache, a white baker's cap and "
                     "spotless white jacket", "elderly male voice, masterful, Gaziantep Turkish"),
            "uretici": ("ÜRETİCİ", "PRODUCER, a 48-year-old Turkish woman, confident, short dark hair, glasses, a light blue shirt",
                        "adult female voice, confident, Gaziantep Turkish")},
   ay=AY, hava="sıcak", urun="Antep fıstığı, baklava, bakır işçiliği, yemeni; Zeugma Mozaik Müzesi",
   sponsor="Fıstık, baklava ya da bakır el sanatları alanında",
   kapak=("baklava", ["mert", "ali", "usta"], "A baklava master lifts a paper-thin sheet of dough to the light while Mert and Ali watch with wide "
          "eyes over huge golden trays of pistachio baklava", "Işığa tutulan incecik yufkayı hayranlıkla izleyen Mert ve Ali."),
   yakinda=("zeugma", ["mert"], "In a dark museum hall a spotlit ancient mosaic face with haunting eyes stares at the viewer, Mert's silhouette "
            "small in the foreground", "Karanlık salonda spot ışığında bakan mozaik gözler ve önde küçük bir silüet."),
   tiktok="Sahte etiketli fıstığı 3 soruda yakaladık 🕵️ #JozhStudios",
   ig=("Gaziantep'te bir aracı bize 'Antep fıstığı' etiketli ucuz çuvallar gösterdi. Ali'nin üç sorusu: belge, üretici, tadım. Cevap yok. 🕵️\n\n"
       "Şemsettin Usta bize iyi fıstığı nasıl seçtiğini öğretti ve gerçek üreticiden belgeli 100 kilo aldık. Zeugma'nın 'Çingene Kızı' ise hâlâ bize bakıyor. 👀\n\n"
       "Yarın Kilis: 80.000 TL'lik taksit. Kasa: {KASA}"),
   tags=["#Gaziantep", "#AntepFıstığı", "#Zeugma"],
   son="Kilis'te ikinci taksit: 80.000 TL. Fıstığın yarısı satılmalı.",
   teaser="Mozaikteki gözler, sahte bir etiket ve üç soru. Bölüm 28: Gaziantep. Pek yakında.")

# ======================================================================= 29 KİLİS
EP(29, "Kilis", "Zeytinin Altında Taksit",
   "Sezon finali: fıstık siparişleri, Kilis tava, cennet çamuru ve ikinci taksit.",
   "Kilis'te sabah zeytinliklerin arasında bir yağhanede soğuk sıkım zeytinyağını tadarlar. Gaziantep'ten aldıkları fıstığın yarısı takipçi "
   "siparişleriyle, besni üzümü bir kuruyemişçiye satılır. Öğlen Kilis tava ve tatlısı cennet çamuru yerler. Ali kasayı kontrol edip ikinci "
   "taksiti gönderir: 80.000 TL. Bu kez Cemil Bey arar ve iki cümle kurar. Akşam zeytinyağından 100 litre alırlar. Sezon biter; Hasan "
   "Antalya'da bekliyordur.",
   {"yaghane": ("Zeytinyağı fabrikası", "a small olive oil mill in Kilis: stainless steel tanks, a golden stream of fresh olive oil pouring into "
                "a container, tasting glasses on a wooden table, olive groves outside the window"),
    "zeytinlik": ("Zeytinlik", "an olive grove near Kilis: ancient twisted olive trees with silver-green leaves in rows on red soil, harsh "
                  "summer sun"),
    "kuruyemis": ("Kuruyemişçi", "a dried fruit and nut shop in Kilis: open sacks of raisins, pistachios and almonds, a brass scale"),
    "lokanta": ("Kilis lokantası", "a traditional restaurant in Kilis: a copper tray of Kilis tava (oven-baked meat and vegetables), a bowl of "
                "a creamy dessert, ceiling fan")},
   [
       S("08:30 sabah", "yaghane", ["mert", "ali", "yagci"], "Yeşil Altın",
         "Yağhanede soğuk sıkım zeytinyağını tadarlar. Usta, yağın biber gibi yakmasının tazelik olduğunu söyler.",
         "The mill owner pours fresh green-gold olive oil into a small glass and hands it to Mert; Mert sips it and coughs at the peppery bite; Ali "
         "laughs and tastes his own glass carefully.",
         [("yagci", "Boğazını yaktıysa taze demektir. İyi zeytinyağı yakar.", "knowledgeable"),
          ("mert", "Yaktı usta, hem de çok taze!", "coughing, laughing")],
         "static medium three-shot at the tasting table", h="sıcak"),
       S("10:30 sabah", "zeytinlik", ["mert", "ali"], "Fıstık Kapışılıyor",
         "Zeytin ağaçlarının gölgesinde Ali siparişleri açar: Antep fıstığının yarısı, 50 kilo, satılmıştır.",
         "Ali sits under an ancient olive tree scrolling orders on his phone and holds up five fingers twice; Mert claps once, then hugs the "
         "twisted olive trunk dramatically.",
         [("ali", "Elli kilo fıstık sipariş! Kilosu bin iki yüz!", "excited"),
          ("mert", "Bu ağaç bize uğur getirdi, sarılıyorum.", "comic, hugging the tree")],
         "slow push-in through the olive branches", h="sıcak",
         t=U(50, "kg", 1200, "satis", "Belgeli Antep fıstığı, takipçi siparişi ({adet} kg x {fiyat} TL)")),
       S("12:00 öğle", "kuruyemis", ["mert", "kuruyemisci"], "Besni Üzümü",
         "Bir kuruyemişçi 80 kilo Besni üzümünün hepsini alır.",
         "The shopkeeper pours raisins from the sack onto his brass scale, tastes one, nods and counts money into Mert's hand; Mert flexes his "
         "arm proudly toward the camera.",
         [("kuruyemisci", "Besni'nin üzümü tatlıdır. Seksen kilo, iki yüz elliden.", "satisfied"),
          ("mert", "Kural bir: kurusu bozulmaz, kârı da bozulmaz.", "proud")],
         "static medium two-shot at the scale",
         t=U(80, "kg", 250, "satis", "Besni kuru üzümü, kuruyemişçiye ({adet} kg x {fiyat} TL)")),
       S("13:30 iç-gündüz", "lokanta", ["mert", "ali"], "Tava ve Cennet Çamuru",
         "Kilis tava ve tatlısı cennet çamurunu yerler. Mert tatlının adını duyunca kahkahayı basar.",
         "Mert spoons a creamy dessert and laughs when Ali reads the name; Ali takes a spoonful too and nods with closed eyes over the copper tray "
         "of Kilis tava.",
         [("ali", "Bu tatlının adı cennet çamuru.", "smiling"),
          ("mert", "Adı da tadı da cennet. Çamur kısmı yalan.", "laughing")],
         "static medium two-shot across the table",
         t=T("yemek", 800, "Kilis tava ve cennet çamuru")),
       S("16:00 ikindi", "zeytinlik", ["mert", "ali", "~cemil"], "İkinci Taksit",
         "Zeytinlikte Ali ikinci taksiti gönderir: 80.000 TL. Bu kez Cemil Bey arar. İki cümle kurar.",
         "Ali presses send on his phone and exhales; the phone immediately rings; he puts it on speaker and holds it between himself and Mert "
         "under the olive tree; both lean in, listening with closed mouths.",
         [("cemil", "Seksen bin geldi. Antalya'da dikkat edin, deniz insanı tembel yapar.", "gruff, from the phone speaker"),
          ("mert", "Cemil Abi bize şaka mı yaptı?", "whisper, astonished")],
         "slow push-in on the phone between their faces", h="sıcak",
         t=T("borc", 80000, "2. taksit: Cemil Bey (Güneydoğu sezonu sonu)")),
       S("19:00 gün batımı", "yaghane", ["mert", "ali", "yagci"], "Yüz Litre",
         "Akşam yağhanede 100 litre soğuk sıkım zeytinyağı alırlar. Hatay ve Antalya'da satılacaktır. Sezon biter.",
         "The mill owner fills tin cans with golden oil from the steel tank and seals them; Ali counts the cans while Mert carries two at once to "
         "the door, the sunset glowing on the olive grove outside.",
         [("yagci", "Litresi iki yüz seksen. Bunu satan utanmaz.", "proud"),
          ("ali", "Antalya'da babama da bir teneke götürürüz.", "warm")],
         "slow dolly-out to the sunset through the door",
         t=[U(100, "litre", 280, "alis", "Soğuk sıkım Kilis zeytinyağı ({adet} litre x {fiyat} TL)"), T("konaklama", 1100, "Otel, 1 gece"),
            U(2, "bilet", 350, "ulasim", "Kilis-Hatay otobüsü (2 x 350 TL)")],
         kurgu="Sezon sonu kartı (kurguda): SEZON 2 BİTTİ · 9 İL · 2. TAKSİT ÖDENDİ"),
   ],
   misafir={"yagci": ("YAĞHANE SAHİBİ", "OLIVE MILL OWNER, a 58-year-old Turkish man, stocky, a grey beard, a cap, a work vest over a white "
                      "shirt", "mature male voice, knowledgeable, Kilis Turkish"),
            "kuruyemisci": ("KURUYEMİŞÇİ", "SHOPKEEPER, a 45-year-old Turkish woman, round face, a beige headscarf, a dark blue apron",
                            "adult female voice, satisfied")},
   ay=AY, hava="sıcak", urun="Kilis zeytinyağı, Kilis tava, cennet çamuru; zeytinlikler",
   sponsor="Zeytinyağı ya da yöresel mutfak alanında",
   kapak=("zeytinlik", ["mert", "ali"], "Mert hugs an ancient twisted olive tree while Ali laughs holding up his phone full of orders, silver "
          "leaves and golden sunlight", "Yaşlı bir zeytin ağacına sarılan Mert ve siparişleri gösteren Ali."),
   yakinda=("zeytinlik", ["mert", "ali"], "Two faces leaning toward a phone glowing between them under the dark shade of an olive tree, sun "
            "rays cutting through the leaves", "Zeytin gölgesinde aralarındaki telefona eğilen iki yüz."),
   tiktok="Sezon 2 finali: 80.000 TL taksit ve Cemil Abi'nin ilk şakası 😳 #JozhStudios",
   ig=("Güneydoğu bitti! 9 il, bir düğün, bir türkü ve sahte etiketi yakalayan üç soru. ☀️\n\n"
       "Kilis'te fıstık siparişleri yağdı, cennet çamuru yedik ve ikinci taksiti gönderdik: 80.000 TL. Cemil Abi aradı ve... şaka yaptı! 😳\n\n"
       "Sezon 3: Akdeniz. Ali'nin evine gidiyoruz. Kasa: {KASA}"),
   tags=["#Kilis", "#Zeytinyağı", "#SezonFinali"],
   son="Cemil Bey ilk kez şaka yapar. Sırada Akdeniz ve Ali'nin babasının serası var.",
   teaser="Zeytinliklerde bir taksit, cennet çamuru ve Cemil Bey'in ilk şakası. Bölüm 29: Kilis, sezon finali. Pek yakında.")
