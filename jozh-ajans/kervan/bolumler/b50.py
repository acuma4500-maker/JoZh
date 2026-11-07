# -*- coding: utf-8 -*-
"""B50 · Kapadokya · KERVANIN KAPISI (Sezon finali) — kasa 2.860.000 → 2.920.000 → 2.980.000"""
from bolumler._ortak import EKIP, VAN, EP, s, ac, et, kapak

B = EP(
    50,
    aciklama=ac(50, "🎈", "SEZON FİNALİ. Yedi parçalı mühür, Derinkuyu yeraltı şehrinin en alt katındaki taş kapının "
                "önünde. Sahaf da onlarla. Kapının ardında Sabri'nin ikinci defteri ve 1926'dan bir fotoğraf var… "
                "ve fotoğraftaki yüz her şeyi değiştiriyor.", "Sezon 2'de sizce neler olacak?"),
    etiketler=et(50, "Kapadokya", "Derinkuyu", "sezonfinali"),
    kapak=kapak("kerem", ["defne", "kaan", "sahaf"],
                "The lowest level of Derinkuyu underground city in Cappadocia; a massive round stone door with a "
                "circular seal-shaped recess, narrow carved tunnels, warm lamp light; above ground in a small inset "
                "at the top, hot air balloons over fairy chimneys at sunrise.",
                "Kerem in the center pressing the complete seven-camel bronze seal into the round stone door, golden "
                "light bursting through the cracks onto his face. Defne on the left holding a lamp high, eyes wide. "
                "Kaan on the right gripping Defne's sleeve, mouth open. The elderly bookseller behind them with her "
                "hands clasped, tears in her eyes.",
                "Epic, emotional season finale; the door to everything."),
    senaryolar=[
        # 1
        s("HOOK", ["kerem"], "The lowest level of Derinkuyu underground city; a massive round stone door with a seal-shaped recess.",
          ("Kerem presses the seven-camel seal into the recess.",
           "The stone door rumbles; golden light bursts through the cracks.",
           "The door begins to roll aside."),
          "Close-up on the seal, then a wide shot of the rolling door.",
          "Deep stone rumble, epic choir music.",
          "Climax.",
          r=("Kerem", "Kervanın kapısı açılıyor!")),
        # 2
        s("ARRIVAL", EKIP, "Cappadocia at sunrise; hundreds of hot air balloons over fairy chimneys; " + VAN + " on a hill.",
          ("Hot air balloons rise over the fairy chimneys.",
           "The three watch from the van's roof.",
           "Kerem holds the complete seal in the sunrise light."),
          "Epic drone shot with balloons.",
          "Wind, majestic music.",
          "Awe.",
          alt="SABAH · KAPADOKYA"),
        # 3
        s("TRADE", ["defne"], "A cave hotel's kitchen in Göreme.",
          ("Defne delivers pastırma and sucuk to the Istanbul deli's courier.",
           "She sells extra to a cave hotel.",
           "The chef tastes and nods."),
          "Medium shot.",
          "Warm music.",
          "Delivery."),
        # 4
        s("TRADE", ["defne"], "The cave hotel.",
          ("Defne gets paid.",
           "She writes it in the ledger.",
           "She looks at the total with a smile."),
          "Close-up on the ledger.",
          "Upbeat music.",
          "Success.",
          r=("Defne", "Pastırma altmış bin getirdi."),
          k=(2_860_000, 2_920_000)),
        # 5
        s("ARRIVAL", ["sahaf", "kerem", "defne", "kaan"], "The entrance of Derinkuyu underground city; the bookseller waits.",
          ("The elderly bookseller waits at the entrance.",
           "She hugs each of them.",
           "She looks at the seal in Kerem's hand."),
          "Medium shot.",
          "Emotional strings.",
          "Reunion.",
          r=("Sahaf", "Dedem bu günü yüz yıl bekledi.")),
        # 6
        s("CRISIS", EKIP, "The ticket office at Derinkuyu.",
          ("A guard says the lowest level needs special permission.",
           "The permit is still being processed.",
           "Defne calls the office again and again."),
          "Medium shot.",
          "Ticking, tense music.",
          "Obstacle."),
        # 7
        s("CRISIS", ["defne"], "The ticket office.",
          ("Defne's phone finally rings.",
           "The permit is approved at the last minute.",
           "The guard opens the gate."),
          "Close-up on the phone.",
          "Ring, a relief music hit.",
          "Relief.",
          r=("Defne", "İzin çıktı! Son dakikada!")),
        # 8
        s("ARRIVAL", ["sahaf", "kerem", "defne", "kaan"], "Narrow carved tunnels of Derinkuyu; lamps on the walls.",
          ("They walk down narrow tunnels, deeper and deeper.",
           "Kaan bends low, bumping his head.",
           "The bookseller walks slowly with a lamp."),
          "Tracking shot down tunnels.",
          "Footsteps, echoes, suspense.",
          "Descent."),
        # 9
        s("SECRET", EKIP, "The lowest level; a massive round stone door.",
          ("They reach the lowest level.",
           "A huge round stone door blocks the way.",
           "In its center: a circular recess shaped like the seal."),
          "Reveal of the door.",
          "Deep silence.",
          "Awe."),
        # 10
        s("SECRET", ["kerem"], "The stone door.",
          ("Kerem lifts the seal.",
           "He looks at Defne, Kaan and the bookseller.",
           "He presses it into the recess."),
          "Close-up on the seal entering.",
          "Click, heartbeat.",
          "Climax."),
        # 11
        s("SECRET", EKIP, "The stone door.",
          ("The door rumbles and rolls aside.",
           "Golden lamp light fills the tunnel.",
           "A small chamber appears with a wooden chest."),
          "Wide shot of the rolling door.",
          "Rumble, epic choir.",
          "Revelation."),
        # 12
        s("TRADE", ["defne"], "A message on Defne's phone in the tunnel (moment of calm).",
          ("Defne's phone vibrates: the Ürgüp molasses and Avanos pottery order is confirmed.",
           "She looks at the final number of the season.",
           "She shows it to Kaan; he grins."),
          "Close-up on the ledger.",
          "Soft triumphant music.",
          "Season's total.",
          r=("Defne", "Sezonu iki milyon dokuz yüz seksenle kapattık!"),
          k=(2_920_000, 2_980_000)),
        # 13
        s("SECRET", ["sahaf", "kerem"], "The hidden chamber; a wooden chest.",
          ("Kerem opens the chest.",
           "Inside is a second leather notebook with the same compass rose.",
           "The bookseller covers her mouth."),
          "Close-up on the second notebook.",
          "Magical chime.",
          "Discovery.",
          r=("Kerem", "İkinci defter!")),
        # 14
        s("SECRET", EKIP, "The hidden chamber.",
          ("Under the notebook lies an old photograph from 1926.",
           "Sabri stands with two partners in front of a caravan.",
           "Kerem lifts it into the light and freezes."),
          "Close-up on the photo.",
          "Music stops.",
          "Shock."),
        # 15
        s("CLIFFHANGER", ["sahaf", "kerem", "defne", "kaan"], "The hidden chamber in golden lamp light.",
          ("Kerem stares at one partner's face: his great-grandfather from the family album.",
           "Defne and Kaan look from the photo to Kerem.",
           "The bookseller speaks softly. Cut to black: end of season one."),
          "Slow push-in on Kerem, then on the bookseller, cut to black.",
          "Heartbeat, final epic music hit, silence.",
          "Season finale.",
          r=("Sahaf", "Bu defter size tesadüfen gelmedi.")),
    ],
)

BOLUMLER = [B]
