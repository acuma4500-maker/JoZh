# -*- coding: utf-8 -*-
"""B14 · Bodrum · İKİNCİ MÜHÜR — kasa 603.000 → 648.000 → 672.000"""
from bolumler._ortak import EKIP, VAN, EP, s, ac, et, kapak

B = EP(
    14,
    aciklama=ac(14, "🌊", "\"Kalenin gölgesinde, suyun altında.\" Bodrum'da incirler yatlara satılıyor, ama asıl hazine "
                "denizin dibinde. Kaan tekneden düşüyor ve suyun altında parlayan bir şey görüyor… İkinci mühür "
                "parçası!", "Sıradaki şehri tahmin edebilir misiniz?"),
    etiketler=et(14, "Bodrum", "Muğla", "BodrumKalesi"),
    kapak=kapak("kaan", ["kerem", "defne"],
                "Bodrum harbor at golden hour; the medieval Bodrum Castle with its towers, white houses on the hills, "
                "wooden gulet boats on crystal-clear turquoise water.",
                "Kaan in the center bursting out of the turquoise water holding a small bronze camel piece high, "
                "water splashing around him, ecstatic face. Kerem on the left leaning over the side of a wooden gulet "
                "reaching toward him. Defne on the right on the boat holding a life ring and a mandarin, laughing in "
                "disbelief. The castle towers behind them.",
                "Triumphant, sunlit, the second piece of the puzzle."),
    senaryolar=[
        # 1
        s("HOOK", ["kaan"], "Under the turquoise water below Bodrum Castle; sunbeams through the water, rocks and seagrass.",
          ("Kaan sinks underwater after falling, eyes wide.",
           "Between the rocks, something bronze glints in a sunbeam.",
           "He reaches toward it as bubbles rise around him."),
          "Underwater slow-motion shot, light rays, push-in on the glint.",
          "Muffled underwater sounds, a magical music swell.",
          "Wonder.",
          alt="SUYUN ALTINDA"),
        # 2
        s("ARRIVAL", EKIP, VAN + " coming down the hill into Bodrum, morning; white houses and the castle below.",
          ("The van descends toward the bright harbor.",
           "Kaan sits silently, pale, looking at the sea.",
           "Defne pats him on the back encouragingly."),
          "Drone shot of Bodrum bay, then a close-up of Kaan.",
          "Seagulls, bright music with a comic nervous note.",
          "Funny nerves.",
          r=("Defne", "Sadece biraz deniz, Kaan."),
          alt="BİR GÜN ÖNCE · BODRUM"),
        # 3
        s("TRADE", ["defne"], "Bodrum marina with luxury yachts; a yacht captain in a white uniform.",
          ("Defne walks the docks with a basket of dried figs.",
           "A yacht captain tastes one and calls his crew.",
           "Soon three yachts want figs for their guests."),
          "Tracking shot along the yachts, close-ups of tasting.",
          "Marina ambience, light jazzy music.",
          "Luxury sales."),
        # 4
        s("TRADE", ["defne", "kerem"], "The marina; crew members carry boxes of figs aboard yachts.",
          ("Kerem and yacht crews carry fig boxes onto the yachts.",
           "Captains pay Defne one after another.",
           "Defne's ledger can barely keep up."),
          "Wide marina shot, quick cuts of payments.",
          "Footsteps on wood, upbeat music.",
          "Momentum."),
        # 5
        s("TRADE", ["defne"], "The end of the marina dock at noon.",
          ("Defne closes the ledger and looks at the total.",
           "She shows it to Kerem; he whistles.",
           "She tosses the empty basket into the van."),
          "Close-up on the ledger, then a two-shot.",
          "Upbeat music hit.",
          "Success.",
          r=("Defne", "İncirler bitti. Kırk beş bin kâr!"),
          k=(603_000, 648_000)),
        # 6
        s("SECRET", ["kerem"], "The walls of Bodrum Castle; Kerem looks down at the water.",
          ("Kerem stands on the castle walls with the notebook.",
           "He finds where the castle's shadow falls on the water at noon.",
           "He marks the spot on his phone map."),
          "High-angle shot down to the water, shadow line visible.",
          "Wind, a mysterious motif.",
          "Clue.",
          r=("Kerem", "Kalenin gölgesi tam şuraya düşüyor.")),
        # 7
        s("ARRIVAL", EKIP, "A wooden gulet boat leaving Bodrum harbor; a cheerful old captain at the wheel.",
          ("The three board a small boat tour.",
           "Kaan clings to the railing with both hands.",
           "The captain laughs and offers him a life jacket."),
          "Wide shot of the gulet leaving, comic close-up of Kaan.",
          "Engine, waves, playful music.",
          "Comic nerves."),
        # 8
        s("CRISIS", ["kaan"], "The gulet deck near the castle; the boat rocks in a wave.",
          ("A wave rocks the boat while Kaan leans over to look.",
           "He loses his balance and flips over the railing.",
           "Splash; Defne screams his name."),
          "Slow-motion fall, then a wide splash.",
          "Splash, scream, music cut.",
          "Shock and comedy.",
          r=("Defne", "Kaan! Kaan düştü!")),
        # 9
        s("SECRET", ["kaan"], "Underwater below Bodrum Castle; sunbeams, seagrass, rocks.",
          ("Kaan sinks, eyes open, panicking for a second.",
           "He sees a bronze glint between two rocks.",
           "He swims down and grabs it."),
          "Underwater slow-motion, push-in on the glint.",
          "Muffled water, magical music.",
          "Wonder."),
        # 10
        s("SECRET", ["kaan", "kerem", "defne"], "The water beside the gulet.",
          ("Kaan bursts out of the water holding the bronze piece high.",
           "Kerem and Defne pull him onto the boat.",
           "He lies on the deck, coughing and laughing."),
          "Low water-level shot, then a top-down shot on the deck.",
          "Splash, cheering, triumphant music.",
          "Triumph.",
          r=("Kaan", "Buldum! İkinci parça!")),
        # 11
        s("SECRET", EKIP, "The gulet deck in the afternoon sun.",
          ("Kerem takes out the first bronze piece from his bag.",
           "He fits the two pieces together; they click.",
           "Two camels of the caravan are now complete."),
          "Extreme close-up on the pieces clicking together.",
          "Metal click, a chime, emotional music.",
          "Joy."),
        # 12
        s("TRADE", ["defne"], "A shop of natural sponges and mandarins in Bodrum's old bazaar.",
          ("Defne buys natural sea sponges and crates of Bodrum mandarins.",
           "She calls an Antalya hotel group from the shop.",
           "They pre-order everything; she pumps her fist."),
          "Medium shot in the shop, close-up of the phone call.",
          "Bazaar sounds, a bright music hit.",
          "Smart trade.",
          r=("Defne", "Antalya otelleri hepsini istiyor!"),
          k=(648_000, 672_000)),
        # 13
        s("SECRET", EKIP, "Bodrum harbor at sunset; the three sit on the dock with wet hair.",
          ("Kaan wraps himself in a towel, still shivering and grinning.",
           "Kerem polishes the joined pieces with his shirt.",
           "Defne notices letters engraved on the back."),
          "Wide sunset shot, then a close-up on the back of the pieces.",
          "Calm sea, gentle music turning curious.",
          "Curiosity."),
        # 14
        s("SECRET", ["kerem", "defne"], "The dock at dusk.",
          ("Defne cleans the engraving with a mandarin peel.",
           "A word appears letter by letter.",
           "Kerem holds his breath."),
          "Macro shot of the engraving appearing.",
          "Heartbeat drum.",
          "Suspense."),
        # 15
        s("CLIFFHANGER", EKIP, "Bodrum dock at night, harbor lights on the water.",
          ("The engraving is complete: one place name.",
           "Kerem looks at the map: it is the next coast to the east.",
           "A strong wind rises and the boats begin to rock. Cut to black."),
          "Close-up on the engraving, then a wide shot of rocking boats, cut to black.",
          "Wind rising, a bold music hit.",
          "Next destination.",
          r=("Kerem", "Arkasında yazıyor: Kaş.")),
    ],
)

BOLUMLER = [B]
