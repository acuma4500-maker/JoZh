# -*- coding: utf-8 -*-
"""B31 · Doğubayazıt · KAR FIRTINASI — kasa 1.610.000 → 1.545.000 → 1.560.000"""
from bolumler._ortak import EKIP, VAN, EP, s, ac, et, kapak

B = EP(
    31,
    aciklama=ac(31, "❄️", "Rüstem'in uyarısı gerçek çıktı: kar fırtınası! Kamyonet İshak Paşa Sarayı yolunda mahsur "
                "kalıyor, peynir teslimatı kaçıyor. Fırtınada sığındıkları sarayda ise defterde çizilmiş bir pencere "
                "var…", "Sarayın penceresinden ne görülüyor?"),
    etiketler=et(31, "Doğubayazıt", "Ağrı", "İshakPaşaSarayı"),
    kapak=kapak("defne", ["kerem", "kaan"],
                "İshak Pasha Palace on a cliff above Doğubayazıt during a heavy snowstorm at dusk; the palace's domes "
                "and minaret covered in snow, Mount Ararat a ghostly white shape behind, the van half-buried in snow "
                "on the road below.",
                "Defne in the center inside a carved stone window of the palace, holding a lantern, looking out at "
                "the white mountain, snow in her hair. Kerem on the left comparing the window to a notebook drawing. "
                "Kaan on the right wrapped in a kilim like a blanket, teeth chattering.",
                "Freezing, epic, a desperate refuge with a magical view."),
    senaryolar=[
        # 1
        s("HOOK", EKIP, "A mountain road below İshak Pasha Palace in a blizzard; " + VAN + " half-buried in snow.",
          ("The van's wheels spin in deep snow.",
           "The headlights barely cut through the blizzard.",
           "Kaan turns off the engine; silence and howling wind."),
          "Wide blizzard shot, then inside the dark van.",
          "Howling wind, engine dying.",
          "Danger.",
          r=("Kaan", "Kar bizi yuttu.")),
        # 2
        s("ARRIVAL", EKIP, VAN + " on the road from Van to Doğubayazıt; gray sky, first heavy flakes.",
          ("The van rushes along the road, snow getting heavier.",
           "Defne checks the cheese delivery time.",
           "Mount Ararat disappears into clouds."),
          "Drone shot, then inside.",
          "Wind, tense music.",
          "Race.",
          alt="BİR GÜN ÖNCE"),
        # 3
        s("TRADE", ["defne"], "A carpet and kilim shop in Doğubayazıt.",
          ("Defne quickly buys kilims and Ağrı honey.",
           "The shop owner warns about the storm.",
           "Defne says they must deliver the cheese tomorrow."),
          "Medium shot.",
          "Wind outside, urgent music.",
          "Haste.",
          r=("Dükkâncı", "Fırtına geliyor. Yola çıkmayın.")),
        # 4
        s("CRISIS", EKIP, "The road toward the palace in a blizzard.",
          ("They drive into the storm toward the main road.",
           "Visibility drops to almost nothing.",
           "The van slides into a snowdrift."),
          "Inside shot, then a wide slide.",
          "Crash into snow.",
          "Danger."),
        # 5
        s("CRISIS", ["kaan", "kerem"], "The snowdrift.",
          ("Kaan and Kerem try to dig the van out with their hands.",
           "The snow is too deep.",
           "Kerem points at lights above: the palace."),
          "Handheld blizzard shot.",
          "Wind, effort.",
          "Struggle."),
        # 6
        s("ARRIVAL", EKIP, "The gate of İshak Pasha Palace in a blizzard at night.",
          ("The three climb to the palace gate.",
           "A guard lets them in to shelter.",
           "They enter the snowy courtyard."),
          "Low-angle shot of the gate.",
          "Wind, relief music.",
          "Refuge."),
        # 7
        s("CRISIS", EKIP, "Inside a palace room; the three wrapped in kilims around a guard's heater.",
          ("They wrap themselves in the kilims.",
           "Kaan's teeth chatter loudly.",
           "Defne checks her phone: no signal."),
          "Close three-shot, warm heater light.",
          "Chattering, wind outside.",
          "Cold misery.",
          r=("Kaan", "Kilimler bizi kurtardı.")),
        # 8
        s("CRISIS", ["defne"], "The palace room at dawn; Defne finally gets a signal.",
          ("Defne gets a message: the cheese order is cancelled due to the delay.",
           "She closes her eyes.",
           "She writes the loss."),
          "Close-up on Defne's face.",
          "A heavy drum hit.",
          "Loss.",
          r=("Defne", "Peynir siparişi iptal. Altmış beş bin."),
          k=(1_610_000, 1_545_000)),
        # 9
        s("SECRET", ["kerem"], "A carved stone window in the palace at dawn.",
          ("Kerem walks the palace corridors.",
           "He finds a window that matches a notebook drawing.",
           "He brushes snow off the sill."),
          "Match cut from drawing to window.",
          "Wind, mysterious music.",
          "Discovery."),
        # 10
        s("SECRET", ["kerem"], "The window sill.",
          ("A number is carved on the stone sill: 1926.",
           "Next to it, a tiny camel.",
           "Kerem looks out of the window."),
          "Close-up on the carving.",
          "Heartbeat.",
          "Clue."),
        # 11
        s("SECRET", EKIP, "The window view; the storm clears, revealing Mount Ararat.",
          ("The clouds part; Mount Ararat appears in the morning sun.",
           "Its shadow falls across the plain to the north.",
           "Defne and Kaan join Kerem at the window."),
          "Epic reveal shot through the window.",
          "Choir-like epic music.",
          "Awe."),
        # 12
        s("TRADE", ["defne"], "The palace courtyard in the sun; tourists arriving after the storm.",
          ("Tourists arrive after the storm.",
           "Defne sells some kilims and honey jars to them.",
           "A small recovery."),
          "Medium shot.",
          "Light music.",
          "Recovery.",
          k=(1_545_000, 1_560_000)),
        # 13
        s("SECRET", ["kerem"], "The notebook page.",
          ("Kerem reads the line under the window drawing.",
           "It speaks about the mountain's shadow.",
           "He looks at the shadow on the plain."),
          "Close-up on the line.",
          "Music building.",
          "Clue.",
          r=("Kerem", "Dağın gölgesi Iğdır'a düşer.")),
        # 14
        s("CRISIS", ["kaan"], "The van in the snow; a snowplow arrives.",
          ("A snowplow clears the road.",
           "The driver pulls the van out with a chain.",
           "Kaan cheers."),
          "Wide shot.",
          "Engine, cheering.",
          "Relief."),
        # 15
        s("CLIFFHANGER", EKIP, "The road below the palace; the van ready.",
          ("The three look at the mountain's shadow pointing north.",
           "Kerem notices a second camel carving on a rock by the road.",
           "Its head points the same way. Cut to black."),
          "Close-up on the rock carving, cut to black.",
          "Wind, deep music hit.",
          "Next destination.",
          r=("Defne", "Bir sonraki durak: Iğdır.")),
    ],
)

BOLUMLER = [B]
