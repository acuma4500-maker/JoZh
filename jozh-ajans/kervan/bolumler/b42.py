# -*- coding: utf-8 -*-
"""B42 · Safranbolu · ALTINCI MÜHÜR — kasa 2.300.000 → 2.345.000 → 2.390.000"""
from bolumler._ortak import EKIP, VAN, EP, s, ac, et, kapak

B = EP(
    42,
    aciklama=ac(42, "🌸", "Safran hasadı tek gün sürüyor ve yağmur yağıyor; çiçekleri sabaha kadar elle topluyorlar. "
                "Ailenin büyükannesi defteri görünce parçayı kendi eliyle veriyor: altıncı mühür! Kervanda tek bir "
                "deve eksik…", "Son parça nerede olabilir?"),
    etiketler=et(42, "Safranbolu", "Karabük", "safran"),
    kapak=kapak("kerem", ["defne", "kaan"],
                "A historic Ottoman mansion courtyard in Safranbolu at dawn after rain; white houses with wooden "
                "frames, a field of purple saffron crocus flowers on the hill, baskets of flowers on the courtyard "
                "table.",
                "Kerem in the center holding six joined camel pieces, one gap left at the end, facing an elderly "
                "grandmother in a headscarf who smiles. Defne on the left with a basket of purple saffron flowers. "
                "Kaan on the right asleep at the table with red saffron threads stuck to his fingers.",
                "Warm, emotional, nearly complete."),
    senaryolar=[
        # 1
        s("HOOK", ["kerem"], "The courtyard of an old Safranbolu mansion at dawn; an elderly grandmother with a small cloth bundle.",
          ("The grandmother unwraps a cloth bundle.",
           "Inside is the bronze camel piece from the museum.",
           "She places it in Kerem's hands herself."),
          "Close-up on the unwrapping, then the hands.",
          "Morning birds, emotional strings.",
          "Emotion.",
          r=("Nine", "Sahibine gidiyor. Ben veriyorum.")),
        # 2
        s("ARRIVAL", EKIP, VAN + " arriving in Safranbolu; white Ottoman houses in a valley.",
          ("The van drives down into the historic town.",
           "White wooden houses fill the valley.",
           "Kerem holds the museum director's card."),
          "Drone shot of the town.",
          "Warm nostalgic music.",
          "Arrival.",
          alt="İKİ GÜN ÖNCE · SAFRANBOLU"),
        # 3
        s("TRADE", ["defne"], "A design shop in Safranbolu's bazaar.",
          ("Defne delivers model boats to the design store's courier.",
           "She sells embroidery to a local shop too.",
           "The owner loves the Sinop patterns."),
          "Medium shot.",
          "Light music.",
          "Deal."),
        # 4
        s("TRADE", ["defne"], "The shop.",
          ("Defne writes the profit.",
           "She asks about the saffron harvest.",
           "The owner says it's only one day: tomorrow."),
          "Close-up on the ledger.",
          "Upbeat music.",
          "Success.",
          r=("Defne", "Nakışlar kırk beş bin getirdi."),
          k=(2_300_000, 2_345_000)),
        # 5
        s("SECRET", ["kerem"], "A historic mansion door with a brass knocker.",
          ("Kerem knocks on a mansion door.",
           "A middle-aged woman opens.",
           "Kerem explains about the museum piece."),
          "Medium shot.",
          "Knocking, soft music.",
          "Meeting."),
        # 6
        s("SECRET", ["kerem"], "The mansion's sitting room.",
          ("The woman says only her mother can decide.",
           "Her elderly mother is in the saffron field.",
           "Kerem looks at the hills."),
          "Two-shot.",
          "Clock, soft music.",
          "Obstacle."),
        # 7
        s("CRISIS", EKIP, "A saffron field on the hillside; purple flowers; rain begins.",
          ("Rain starts falling on the saffron field.",
           "The pickers worry; the flowers must be picked today.",
           "The three join without a word."),
          "Wide shot of the purple field.",
          "Rain, urgent music.",
          "Urgency."),
        # 8
        s("CRISIS", EKIP, "The saffron field at night with lamps.",
          ("They pick flowers by lamp light in the rain.",
           "Their fingers are purple and red.",
           "Kaan almost falls asleep standing."),
          "Lamp-lit shots.",
          "Rain, soft folk music.",
          "Hard work.",
          r=("Kaan", "Sabaha kaç çiçek kaldı?")),
        # 9
        s("CRISIS", EKIP, "The mansion courtyard at dawn; baskets of flowers.",
          ("They separate red threads from the flowers.",
           "The family works with them.",
           "Kaan falls asleep at the table."),
          "Wide dawn shot.",
          "Birds, warm music.",
          "Exhaustion."),
        # 10
        s("SECRET", ["kerem"], "The courtyard; the elderly grandmother watches Kerem.",
          ("The grandmother has watched them work all night.",
           "She asks to see the notebook.",
           "Kerem gives it to her."),
          "Two-shot.",
          "Soft music.",
          "Trust."),
        # 11
        s("SECRET", ["kerem"], "The courtyard.",
          ("The grandmother touches the camel drawing.",
           "She smiles and calls her son to bring the piece from Sinop.",
           "He says he already has it."),
          "Close-up on her hand.",
          "Strings.",
          "Emotion."),
        # 12
        s("TRADE", ["defne"], "The courtyard; Defne on the phone.",
          ("Defne sells saffron and Safranbolu lokum to a gourmet chain.",
           "They pay a high price for real saffron.",
           "The family cheers."),
          "Medium shot.",
          "Triumphant music.",
          "Success.",
          r=("Defne", "Safran kırk beş bin getirdi!"),
          k=(2_345_000, 2_390_000)),
        # 13
        s("SECRET", EKIP, "The courtyard table.",
          ("Kerem joins the sixth piece.",
           "Six camels in a row; one gap remains.",
           "Everyone falls silent."),
          "Macro on the click.",
          "Click, emotional swell.",
          "Joy."),
        # 14
        s("SECRET", ["kerem"], "The courtyard.",
          ("Kerem turns the sixth piece.",
           "One word is engraved on the back.",
           "He reads it slowly."),
          "Close-up on the engraving.",
          "Heartbeat.",
          "Clue."),
        # 15
        s("CLIFFHANGER", EKIP, "The courtyard at sunrise.",
          ("The word on the back is 'KAPI'.",
           "Kerem looks at the gap in the caravan.",
           "Defne opens the map: the road goes to Central Anatolia. Cut to black."),
          "Close-up on the gap, then the map, cut to black.",
          "A deep music hit.",
          "Next region.",
          r=("Kerem", "Bir deve eksik. Ve bir kapı.")),
    ],
)

BOLUMLER = [B]
