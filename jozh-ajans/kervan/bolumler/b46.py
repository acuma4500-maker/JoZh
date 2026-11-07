# -*- coding: utf-8 -*-
"""B46 · Konya · BÜYÜK PAZAR — kasa 2.430.000 → 2.540.000 → 2.580.000"""
from bolumler._ortak import EKIP, VAN, EP, s, ac, et, kapak

B = EP(
    46,
    aciklama=ac(46, "🛒", "Elde kalan malları Konya'nın büyük pazarında satmak için tek şans var… ve sabah kar yağıyor! "
                "Tezgâh kurulamıyor; tarihi bir hanın avlusunda pazar kuruyorlar. Avludaki semazen figürü ise bir yol "
                "gösteriyor.", "Ankara'daki zarar geri gelir mi?"),
    etiketler=et(46, "Konya", "etliekmek", "pazar"),
    kapak=kapak("defne", ["kerem", "kaan"],
                "The courtyard of a historic Seljuk caravanserai in Konya on a snowy morning; arched stone galleries, "
                "a busy improvised market with stalls of meerschaum, mohair scarves and helva, snow falling softly, a "
                "carved whirling dervish figure on a column.",
                "Defne in the center behind a stall full of customers, holding cash up high with a huge smile. Kerem on "
                "the left pointing at the carved whirling dervish on the column. Kaan on the right with a long Konya "
                "flatbread with meat (etli ekmek) hanging from his mouth.",
                "Snowy, warm, a joyful comeback."),
    senaryolar=[
        # 1
        s("HOOK", ["defne"], "A historic caravanserai courtyard in Konya; snow falling on a crowded improvised market.",
          ("Customers crowd Defne's stall in the snow.",
           "She sells piece after piece.",
           "She raises a handful of cash, laughing."),
          "Wide shot of the market, then Defne.",
          "Crowd, triumphant music.",
          "Comeback.",
          r=("Defne", "Ankara'nın zararı geri geliyor!")),
        # 2
        s("ARRIVAL", EKIP, VAN + " arriving in Konya; the green dome of the Mevlana Museum in the morning.",
          ("The van enters Konya.",
           "The green dome of Mevlana shines.",
           "Defne prepares a big market plan."),
          "Drone shot.",
          "Calm spiritual music.",
          "Hope.",
          alt="SABAH · KONYA"),
        # 3
        s("CRISIS", EKIP, "The open market square at dawn; snow falling heavily.",
          ("Snow covers the market square.",
           "Stall owners pack up and go home.",
           "Defne looks at the full van."),
          "Wide snowy shot.",
          "Wind, sad music.",
          "Setback.",
          r=("Kaan", "Pazar iptal mi? Bu kar…")),
        # 4
        s("CRISIS", ["kerem", "defne"], "A historic caravanserai gate near the square.",
          ("Kerem notices an old caravanserai with a covered courtyard.",
           "He asks the guard if they can sell inside.",
           "The guard agrees."),
          "Medium shot.",
          "Hopeful music.",
          "Idea."),
        # 5
        s("TRADE", EKIP, "The caravanserai courtyard; stalls set up under the arches.",
          ("They set up a market under the arches.",
           "Other sellers follow them inside.",
           "Customers pour in from the snow."),
          "Wide shot filling with people.",
          "Crowd, joyful music.",
          "Comeback.",
          r=("Defne", "Lületaşı, tiftik, helva! Buyurun!"),
          k=(2_430_000, 2_540_000)),
        # 6
        s("TRADE", ["kaan"], "A famous etli ekmek bakery.",
          ("Kaan watches a baker pull a meter-long flatbread from the oven.",
           "He eats it on the street in the snow.",
           "He says this is the best day ever."),
          "Close-up on the bread.",
          "Oven crackle, comic music.",
          "Joy."),
        # 7
        s("TRADE", ["defne"], "A flour mill in Konya.",
          ("Defne visits a flour mill.",
           "She buys wheat flour in bulk.",
           "The miller shows her the stone mill."),
          "Medium shot.",
          "Mill sounds, warm music.",
          "Trade."),
        # 8
        s("SECRET", ["kerem"], "The caravanserai courtyard; a carved column.",
          ("Kerem notices a carved whirling dervish on a column.",
           "He compares it with a notebook drawing.",
           "They match."),
          "Match cut.",
          "Soft ney-like music.",
          "Discovery."),
        # 9
        s("SECRET", ["kerem"], "The column.",
          ("Kerem looks closer at the dervish's skirt.",
           "A tiny arrow and a camel are carved in its folds.",
           "The arrow points southeast."),
          "Macro on the carving.",
          "Heartbeat.",
          "Clue."),
        # 10
        s("SECRET", ["kerem", "defne"], "The courtyard.",
          ("Kerem shows Defne the arrow.",
           "She opens the map on her phone.",
           "The line points to a deep valley."),
          "Two-shot.",
          "Music building.",
          "Next step."),
        # 11
        s("TRADE", EKIP, "The courtyard at sunset; the market ends.",
          ("The van is empty.",
           "Defne counts the earnings.",
           "Kaan dances in the snow."),
          "Wide shot.",
          "Joyful music.",
          "Celebration."),
        # 12
        s("TRADE", ["defne"], "The flour mill office.",
          ("Defne presells the flour to bakeries in Aksaray.",
           "They pay a deposit.",
           "She writes it down."),
          "Medium shot.",
          "Triumphant music.",
          "Success.",
          r=("Defne", "Un da satıldı. Kırk bin daha!"),
          k=(2_540_000, 2_580_000)),
        # 13
        s("SECRET", ["kerem"], "The notebook.",
          ("Kerem finds a page about a valley.",
           "It shows a canyon and a rock church.",
           "He reads the line."),
          "Close-up on the page.",
          "Mysterious music.",
          "Riddle."),
        # 14
        s("SECRET", EKIP, "The courtyard at night.",
          ("The three look at the page together.",
           "Defne recognizes the canyon: Ihlara.",
           "Kaan zips his jacket."),
          "Three-shot.",
          "Wind, music.",
          "Decision."),
        # 15
        s("CLIFFHANGER", EKIP, "The caravanserai gate at night, snow stopped.",
          ("Kerem reads the last line on the page.",
           "Only two cities remain on the map.",
           "The moon appears over the dome. Cut to black."),
          "Close-up on Kerem, cut to black.",
          "A deep music hit.",
          "Next destination.",
          r=("Kerem", "Vadinin dibinde son harita.")),
    ],
)

BOLUMLER = [B]
