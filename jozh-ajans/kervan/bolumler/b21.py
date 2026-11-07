# -*- coding: utf-8 -*-
"""B21 · Hatay · ÜÇÜNCÜ MÜHÜR — kasa 940.000 → 985.000 → 1.030.000"""
from bolumler._ortak import EKIP, VAN, EP, s, ac, et, kapak

B = EP(
    21,
    aciklama=ac(21, "🏆", "\"Hatay'da her şeyi kaybettik.\" Ama Sabri'nin kaybettiği para değilmiş. Uzun Çarşı'da "
                "elektrik kesiliyor, peynirler bozulmadan bütün mahalle seferber oluyor. Yüz yıldır bir parçayı "
                "saklayan bir aile… Ve kasa ilk kez 1.000.000 ₺'yi geçiyor!", "Yolun ikiye ayrıldığı yer neresi?"),
    etiketler=et(21, "Hatay", "Antakya", "künefe"),
    kasa_baslar=2,  # S1 ileri-sarma: kasa milyonu geçmişken gösterilmez
    kapak=kapak("defne", ["kerem", "kaan"],
                "Antakya's Long Bazaar (Uzun Çarşı) in Hatay at dusk during a power cut; hundreds of candles and "
                "oil lamps lighting stone arches, shelves of laurel soap, trays of künefe cheese.",
                "Defne in the center holding her ledger up triumphantly, a glowing number reflected on her glasses, "
                "candlelight on her face. Kerem on the left holding three joined bronze camel pieces in his palm. "
                "Kaan on the right carrying a tray of künefe cheese, shopkeepers cheering behind him.",
                "Warm, communal, a huge milestone: the first million."),
    senaryolar=[
        # 1
        s("HOOK", ["defne"], "Antakya's Long Bazaar at night in candlelight.",
          ("Defne writes a number in her ledger by candlelight.",
           "She stares at it, then counts the digits again.",
           "She slowly raises her head with tears of joy."),
          "Extreme close-up on the pencil, then a slow pull back.",
          "Candle flicker, a rising emotional music.",
          "Huge joy.",
          r=("Defne", "Bir milyon. Bir milyonu geçtik!")),
        # 2
        s("ARRIVAL", EKIP, VAN + " entering Antakya in the morning; the Asi River and old stone houses.",
          ("The van crosses the Asi River into Antakya.",
           "Kaan tests his voice; it's back.",
           "Everyone cheers; Kaan sings."),
          "Drone shot, then a comic inside shot.",
          "River, singing, warm music.",
          "Joy.",
          r=("Kaan", "Sesim geldi! Hatay, geldik!"),
          alt="SABAH · HATAY"),
        # 3
        s("TRADE", ["defne"], "A spice and textile shop in Antakya's Long Bazaar; the Hatay buyer, a friendly man with a gray beard.",
          ("Defne delivers the cotton fabric and pepper flakes.",
           "The buyer pays the rest of the amount.",
           "He invites them for künefe."),
          "Medium shot, close-up on the payment.",
          "Bazaar sounds, warm music.",
          "Good deal."),
        # 4
        s("TRADE", ["defne", "kaan"], "A künefe shop in the Long Bazaar.",
          ("Kaan tastes künefe and almost faints with pleasure.",
           "Defne writes the profit in her ledger.",
           "The total is now very close to one million."),
          "Close-up on the stretching cheese, then the ledger.",
          "Sizzle, happy music.",
          "Joy.",
          k=(940_000, 985_000)),
        # 5
        s("TRADE", ["defne"], "A cheese and laurel soap workshop in the Long Bazaar.",
          ("Defne buys künefe cheese and laurel soap in bulk.",
           "She arranges delivery to Gaziantep.",
           "The cheese must stay cold."),
          "Medium shot, close-up on cheese blocks.",
          "Shop sounds, focused music.",
          "Careful trade."),
        # 6
        s("CRISIS", EKIP, "The Long Bazaar in the afternoon; suddenly all lights go out.",
          ("A buzz, then the whole bazaar goes dark.",
           "Refrigerators stop humming.",
           "Shopkeepers shout; the cheese will spoil."),
          "Wide shot as lights go out, close-up on a fridge.",
          "Power-down sound, rising alarm music.",
          "Crisis.",
          r=("Peynirci", "Elektrik yok! Peynirler bozulacak!")),
        # 7
        s("CRISIS", EKIP, "The dark Long Bazaar; shopkeepers gathering.",
          ("Defne climbs on a crate and organizes everyone.",
           "Shopkeepers form a chain passing cheese blocks.",
           "Kaan runs to buy ice from a fish market."),
          "Low-angle shot of Defne, then the human chain.",
          "Shouts, footsteps, energetic drums.",
          "Community."),
        # 8
        s("CRISIS", ["kaan"], "A fish market at dusk; ice crushers.",
          ("Kaan buys all the ice.",
           "He loads sacks into the van, slipping on fish scales.",
           "He arrives back cheering with ice."),
          "Comic tracking shots.",
          "Ice crashing, comic music.",
          "Heroic comedy."),
        # 9
        s("CRISIS", EKIP, "The dark bazaar lit by candles; cheese packed in ice.",
          ("All the cheese is packed in ice.",
           "Candles and lamps light the bazaar.",
           "Shopkeepers applaud the three."),
          "Wide candlelit shot.",
          "Applause, warm music.",
          "Triumph."),
        # 10
        s("SECRET", ["kerem"], "An old stone house in Antakya; a family of three generations in a courtyard with a lemon tree.",
          ("The grateful cheese shop owner brings Kerem to his family house.",
           "His elderly mother sees the notebook and stands up.",
           "She goes inside without a word."),
          "Medium shot in the courtyard.",
          "Fountain, mysterious music.",
          "Mystery."),
        # 11
        s("SECRET", ["kerem"], "The courtyard of the stone house.",
          ("The old woman comes back with a small wooden box.",
           "She opens it: a bronze camel piece.",
           "She places it in Kerem's hand."),
          "Close-up on the box and the piece.",
          "Magical chime.",
          "Revelation.",
          r=("Yaşlı Kadın", "Yüz yıldır bekliyoruz. Kaybettiği buydu.")),
        # 12
        s("SECRET", EKIP, "The courtyard at dusk.",
          ("Kerem joins the three bronze pieces together.",
           "They click; three camels in a row.",
           "Defne and Kaan hug him."),
          "Macro on the pieces clicking.",
          "Click, emotional music swell.",
          "Joy."),
        # 13
        s("TRADE", ["defne"], "The Long Bazaar at night in candlelight.",
          ("The shopkeepers insist on buying the laurel soaps at a good price as thanks.",
           "Defne writes the number in her ledger.",
           "She counts the digits twice."),
          "Close-up on the ledger by candlelight.",
          "A rising emotional music.",
          "Milestone.",
          r=("Defne", "Bir milyon otuz bin!"),
          k=(985_000, 1_030_000)),
        # 14
        s("SECRET", ["kerem"], "The courtyard under the lemon tree at night.",
          ("Kerem turns over the third piece.",
           "There is a warning engraved on the back.",
           "His smile fades."),
          "Close-up on the engraving.",
          "Music fades.",
          "Unease."),
        # 15
        s("CLIFFHANGER", EKIP, "The courtyard at night.",
          ("Kerem reads the warning aloud.",
           "Defne and Kaan stop celebrating.",
           "The candle flame bends in a sudden wind. Cut to black."),
          "Slow push-in on Kerem, then the candle, cut to black.",
          "Wind, a deep bass hit.",
          "Cliffhanger.",
          r=("Kerem", "Güneydoğu'da yol ikiye ayrılır.")),
    ],
)

BOLUMLER = [B]
