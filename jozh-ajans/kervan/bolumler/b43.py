# -*- coding: utf-8 -*-
"""B43 · Beypazarı · HAVUÇ LOKUMU — kasa 2.390.000 → 2.415.000 → 2.405.000 → 2.450.000"""
from bolumler._ortak import EKIP, VAN, EP, s, ac, et, kapak

B = EP(
    43,
    aciklama=ac(43, "🥕", "Beypazarı havucun memleketi. Kaan bir tarifi yanlış anlıyor ve bin kutu \"havuçlu lokum\" "
                "yanlış basılıyor… Sonuç? Hiç beklenmedik bir şey! Bir konağın kapı tokmağı ise yüz yıllık bir "
                "hikâyeyi açıyor.", "Havuçlu lokum yer miydiniz? 😄"),
    etiketler=et(43, "Beypazarı", "Ankara", "havuç"),
    kapak=kapak("kaan", ["kerem", "defne"],
                "The historic Ottoman mansions of Beypazarı on a sunny day; white and wooden houses on a slope, a "
                "street market with carrots, dried fruit and mineral water bottles, a carved wooden door with a brass "
                "camel-shaped knocker.",
                "Kaan in the center holding up a box of orange carrot-flavored Turkish delight with a sheepish grin, "
                "boxes piled behind him. Kerem on the left touching the brass camel knocker on an old mansion door. "
                "Defne on the right laughing with a tourist who is buying three boxes.",
                "Bright, funny, nostalgic."),
    senaryolar=[
        # 1
        s("HOOK", ["kaan"], "A small printing house in Beypazarı; a machine printing orange lokum boxes.",
          ("A machine spits out box after box with a carrot printed on it.",
           "Kaan picks one up proudly.",
           "Defne arrives and freezes."),
          "Close-up on the boxes flying out.",
          "Machine rhythm, comic music.",
          "Comedy setup.",
          r=("Defne", "Bin kutu havuçlu lokum mu?!")),
        # 2
        s("ARRIVAL", EKIP, VAN + " arriving in Beypazarı; Ottoman mansions on the slope.",
          ("The van drives up to the historic town.",
           "Orange carrots everywhere in the market.",
           "Kaan's eyes shine."),
          "Drone shot.",
          "Market, warm music.",
          "Arrival.",
          alt="BİR GÜN ÖNCE · BEYPAZARI"),
        # 3
        s("TRADE", ["defne"], "A gift shop in Beypazarı.",
          ("Defne sells extra Safranbolu lokum to a gift shop.",
           "The owner likes the saffron flavor.",
           "He buys all."),
          "Medium shot.",
          "Light music.",
          "Deal."),
        # 4
        s("TRADE", ["defne", "kaan"], "The gift shop.",
          ("The owner suggests making a Beypazarı carrot lokum.",
           "Kaan gets excited and volunteers.",
           "Defne agrees, cautiously."),
          "Medium shot.",
          "Comic music.",
          "Setup."),
        # 5
        s("TRADE", ["defne"], "The gift shop.",
          ("Defne writes the lokum profit.",
           "She gives Kaan the box order to manage.",
           "Kaan salutes."),
          "Close-up on the ledger.",
          "Upbeat music.",
          "Success.",
          r=("Defne", "Yirmi beş bin. Kaan, kutular sende."),
          k=(2_390_000, 2_415_000)),
        # 6
        s("CRISIS", ["kaan"], "The printing house.",
          ("Kaan reads the recipe note on his phone quickly.",
           "He orders boxes with a giant carrot design.",
           "He orders a thousand instead of a hundred."),
          "Close-up on the order.",
          "Comic music.",
          "Mistake."),
        # 7
        s("CRISIS", ["defne", "kaan"], "The printing house; boxes piled to the ceiling.",
          ("A thousand boxes stand in piles.",
           "Defne stares in disbelief.",
           "Kaan smiles nervously."),
          "Wide comic shot.",
          "Comic silence.",
          "Comedy.",
          r=("Kaan", "Yüz yazacaktım… sıfır kaydı.")),
        # 8
        s("CRISIS", ["defne"], "The printing house.",
          ("Defne pays the printing bill.",
           "She writes the expense.",
           "She sighs deeply."),
          "Close-up on the ledger.",
          "Sad comic music.",
          "Small loss."),
        # 9
        s("CRISIS", ["defne", "kaan"], "A lokum workshop.",
          ("A lokum maker agrees to fill the boxes with carrot lokum.",
           "Kaan stirs the orange mixture.",
           "It smells surprisingly good."),
          "Close-up on the mixture.",
          "Bubbling, hopeful music.",
          "Hope.",
          k=(2_415_000, 2_405_000)),
        # 10
        s("SECRET", ["kerem"], "A street of historic mansions; a carved door with a brass camel knocker.",
          ("Kerem walks along the old mansions with the notebook.",
           "He finds a door with a brass camel knocker.",
           "He knocks three times."),
          "Close-up on the knocker.",
          "Knocking, mysterious music.",
          "Discovery."),
        # 11
        s("SECRET", ["kerem"], "Inside the mansion; an old man in his eighties with a cane.",
          ("An old man opens the door.",
           "He sees the notebook and invites Kerem in.",
           "He sits slowly by the window."),
          "Medium shot.",
          "Clock, soft music.",
          "Meeting."),
        # 12
        s("TRADE", EKIP, "The Beypazarı street market; tourists crowding a stand.",
          ("Tourists crowd the carrot lokum stand.",
           "The funny boxes go viral on a tourist's phone.",
           "All thousand boxes sell out."),
          "Wide shot of the crowd.",
          "Cheering, triumphant music.",
          "Comic triumph.",
          r=("Defne", "Bin kutu bitti! Kaan, sen dâhisin!"),
          k=(2_405_000, 2_450_000)),
        # 13
        s("SECRET", ["kerem"], "The mansion sitting room.",
          ("The old man says his father met Sabri here.",
           "He remembers his father's story.",
           "He looks at Kerem closely."),
          "Close-up on the old man.",
          "Strings.",
          "Story."),
        # 14
        s("SECRET", ["kerem"], "The mansion.",
          ("The old man shows an old guest book.",
           "Sabri's signature is there, with only one other name.",
           "Kerem frowns."),
          "Close-up on the guest book (no readable text).",
          "Heartbeat.",
          "Mystery."),
        # 15
        s("CLIFFHANGER", ["kerem"], "The mansion at dusk.",
          ("The old man says the words his father always said.",
           "Kerem looks at the two signatures.",
           "One partner is missing. Cut to black."),
          "Close-up on the old man, cut to black.",
          "A deep music hit.",
          "Mystery.",
          r=("Yaşlı Adam", "Sabri'nin yanında sadece bir kişi vardı.")),
    ],
)

BOLUMLER = [B]
