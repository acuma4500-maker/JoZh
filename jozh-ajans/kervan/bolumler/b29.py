# -*- coding: utf-8 -*-
"""B29 · Ahlat · SELÇUKLU TAŞI — kasa 1.480.000 → 1.495.000 → 1.525.000"""
from bolumler._ortak import EKIP, VAN, EP, s, ac, et, kapak

B = EP(
    29,
    aciklama=ac(29, "🪦", "Van Gölü kıyısında lastik patlıyor, yedek lastik de patlak çıkıyor! Beklerken Selçuklu "
                "mezar taşlarının arasında yürüyorlar ve bir taşın üzerinde deve kabartması, bir isim ve bir tarih "
                "buluyorlar…", "\"R.\" harfinin sahibi sonunda belli mi oldu?"),
    etiketler=et(29, "Ahlat", "Bitlis", "VanGölü"),
    kapak=kapak("kerem", ["defne", "kaan"],
                "The Seljuk cemetery of Ahlat on the shore of Lake Van at golden hour; hundreds of tall carved "
                "tombstones with intricate geometric patterns, golden grass, the deep blue lake and snowy mountains "
                "behind, first snow on the ground.",
                "Kerem in the center kneeling before a tall carved tombstone, brushing snow off a small camel relief "
                "and an engraved name. Defne on the left holding a jar of golden Bitlis honey. Kaan on the right "
                "rolling a flat tire, breath steaming in the cold.",
                "Majestic, cold, solemn with a thrilling name revealed."),
    senaryolar=[
        # 1
        s("HOOK", ["kerem"], "A tall carved Seljuk tombstone in Ahlat; snow on the ground, Lake Van behind.",
          ("Kerem brushes snow off the tombstone.",
           "A small camel relief appears, then an engraved name and a year.",
           "He reads it, breath steaming."),
          "Close-up on the brushing hand, slow reveal.",
          "Cold wind, deep mysterious music.",
          "Revelation.",
          r=("Kerem", "Rüstem, 1926. İşte R!")),
        # 2
        s("ARRIVAL", EKIP, VAN + " driving along the shore of Lake Van; snowy mountains, deep blue water.",
          ("The van drives along the enormous blue lake.",
           "Snowflakes start falling.",
           "Everyone wraps scarves tighter."),
          "Drone shot of the lake and van.",
          "Wind, epic cold music.",
          "Awe.",
          alt="SABAH · AHLAT"),
        # 3
        s("CRISIS", EKIP, "The lakeside road; the van pulls over with a loud bang.",
          ("A loud bang; the van lurches.",
           "Kaan gets out: the front tire is shredded.",
           "He opens the spare tire compartment."),
          "Wide shot of the van stopping, close-up on the tire.",
          "Bang, hiss, tense music.",
          "Problem."),
        # 4
        s("CRISIS", ["kaan", "defne"], "The roadside by the lake.",
          ("Kaan pulls out the spare tire.",
           "It is completely flat too.",
           "Defne and Kaan stare at each other."),
          "Comic close-up on the flat spare.",
          "Comic sad trombone.",
          "Comic despair.",
          r=("Kaan", "Yedek lastik de mi patlak?")),
        # 5
        s("TRADE", ["defne"], "A souvenir shop near Ahlat's Seljuk cemetery.",
          ("While waiting for help, Defne visits a souvenir shop.",
           "She sells the few silver samples she kept.",
           "The owner loves the filigree work."),
          "Medium shot.",
          "Shop bell, warm music.",
          "Small win.",
          r=("Defne", "Beklerken bile kâr ederiz."),
          k=(1_480_000, 1_495_000)),
        # 6
        s("ARRIVAL", ["kerem", "kaan"], "Ahlat's Seljuk cemetery; hundreds of tall carved tombstones.",
          ("Kerem and Kaan walk among the tall tombstones.",
           "The patterns are incredibly detailed.",
           "Kaan whispers, impressed."),
          "Tracking shot among the stones.",
          "Wind, haunting music.",
          "Awe."),
        # 7
        s("SECRET", ["kerem"], "A tombstone in the cemetery.",
          ("Kerem compares patterns with a notebook drawing.",
           "One tombstone has a camel relief on its side.",
           "He kneels and brushes off the snow."),
          "Close-up on the relief.",
          "Heartbeat drum.",
          "Discovery."),
        # 8
        s("SECRET", ["kerem", "kaan"], "The tombstone.",
          ("A name and year appear under the camel.",
           "Kerem reads it with a trembling voice.",
           "Kaan grabs his shoulder."),
          "Close-up on the engraving.",
          "Music swell.",
          "Revelation.",
          r=("Kerem", "Rüstem, 1926.")),
        # 9
        s("SECRET", ["kerem", "kaan"], "The cemetery.",
          ("Kerem realizes this is not a grave but a memorial stone.",
           "There is a small line: 'Kervana yol gösterdi.'",
           "He photographs it."),
          "Close-up on the line.",
          "Soft strings.",
          "Understanding."),
        # 10
        s("CRISIS", ["kaan"], "The roadside; a farmer's tractor arrives.",
          ("A friendly farmer stops his tractor.",
           "He has a tire repair kit.",
           "Kaan hugs him."),
          "Medium shot.",
          "Tractor, comic warm music.",
          "Help arrives."),
        # 11
        s("TRADE", ["defne"], "A beekeeper's stall near Bitlis; jars of golden honey.",
          ("Defne tastes Bitlis mountain honey.",
           "She buys a large batch.",
           "The beekeeper gives Kaan a honeycomb to taste."),
          "Close-up on honey dripping.",
          "Bees, warm music.",
          "Trade."),
        # 12
        s("TRADE", ["defne"], "The beekeeper's stall; Defne on the phone.",
          ("Defne calls a breakfast chain from her ledger.",
           "They pre-order the honey.",
           "She gives the beekeeper a thumbs up."),
          "Two-shot.",
          "Upbeat music.",
          "Success.",
          r=("Defne", "Bal satıldı! Otuz bin daha!"),
          k=(1_495_000, 1_525_000)),
        # 13
        s("SECRET", EKIP, "The lakeside at sunset; the van repaired.",
          ("The three look at the memorial photo.",
           "Kerem says Rüstem stayed in Van.",
           "Defne searches for the surname."),
          "Three-shot at sunset.",
          "Lake waves, mysterious music.",
          "Search."),
        # 14
        s("SECRET", ["defne"], "The van at dusk.",
          ("Defne finds a breakfast house in Van with the same family name.",
           "It's a famous Van breakfast place.",
           "She shows the photo of the shop."),
          "Close-up on phone.",
          "Music hit.",
          "Clue."),
        # 15
        s("CLIFFHANGER", EKIP, "The van driving along the dark lakeshore at night, snow falling.",
          ("The van drives in the snow toward Van.",
           "Kerem looks at the memorial photo once more.",
           "He notices a second, smaller name under Rüstem's. Cut to black."),
          "Close-up on the photo, cut to black.",
          "Wind, deep bass hit.",
          "Cliffhanger.",
          r=("Kerem", "Altında bir isim daha var…")),
    ],
)

BOLUMLER = [B]
