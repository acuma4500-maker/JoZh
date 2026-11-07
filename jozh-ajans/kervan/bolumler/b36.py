# -*- coding: utf-8 -*-
"""B36 · Yusufeli · DERE YOLU — kasa 1.930.000 → 1.950.000 → 1.990.000"""
from bolumler._ortak import EKIP, VAN, EP, s, ac, et, kapak

B = EP(
    36,
    aciklama=ac(36, "⛰️", "Sahaf telefonda \"Defteri size ben seçtim\" diyor ve gerisini Rize'de anlatacağını söylüyor. "
                "Dar dere yolunda heyelan; kamyonet yirmi kilometre geri geri gidiyor. Ve Kerem defterin son "
                "sayfalarının birbirine yapıştırıldığını fark ediyor…", "Sahaf neden sayfaları yapıştırmış olabilir?"),
    etiketler=et(36, "Yusufeli", "Artvin", "kestanebalı"),
    kapak=kapak("kaan", ["kerem", "defne"],
                "A narrow winding road along a wild turquoise river in a deep green canyon near Yusufeli, Artvin; "
                "steep cliffs, a landslide of rocks and mud blocking the road ahead, wooden beehives on the slopes.",
                "Kaan in the center leaning out of the driver's window of the van, looking backward with a terrified "
                "face as he reverses. Kerem on the left in the passenger seat holding the notebook, trying to separate "
                "two stuck pages. Defne on the right standing outside with a jar of dark chestnut honey, waving him "
                "back.",
                "Wild nature, tension and a quiet mystery."),
    senaryolar=[
        # 1
        s("HOOK", ["kerem"], "Outside the Twin Minaret Madrasa in Erzurum at night; snow falling; Kerem on the phone.",
          ("Kerem listens to the old woman's voice on the phone.",
           "Defne and Kaan crowd close to hear.",
           "The call ends; Kerem stares at the screen."),
          "Close-up on Kerem, then three faces.",
          "Wind, phone beep, emotional music.",
          "Shock.",
          r=("Sahaf", "Sebebini Rize'de anlatacağım.")),
        # 2
        s("ARRIVAL", EKIP, VAN + " driving into the green Çoruh river canyon toward Yusufeli.",
          ("Snow gives way to green forests and a turquoise river.",
           "The road gets narrow and winding.",
           "Kaan drives carefully, gripping the wheel."),
          "Drone shot following the river.",
          "Rushing river, majestic music.",
          "Awe.",
          alt="YUSUFELİ"),
        # 3
        s("TRADE", ["defne"], "A small shop in Yusufeli town.",
          ("Defne sells the extra oltu stone pieces to a souvenir shop.",
           "The owner loves the black stone.",
           "Defne writes the profit."),
          "Medium shot.",
          "Light music.",
          "Deal.",
          r=("Defne", "Kalan oltu taşları yirmi bin."),
          k=(1_930_000, 1_950_000)),
        # 4
        s("TRADE", ["defne", "kaan"], "A hillside apiary with wooden hives.",
          ("A beekeeper shows them dark chestnut honey.",
           "Kaan tastes it and coughs: it's bitter.",
           "The beekeeper laughs; Defne loves it."),
          "Close-up on honey, comic Kaan.",
          "Bees, comic music.",
          "Comedy."),
        # 5
        s("TRADE", ["defne"], "The apiary.",
          ("Defne buys a large batch of chestnut honey.",
           "The beekeeper packs jars in boxes.",
           "They load the van."),
          "Medium shot.",
          "Warm music.",
          "Trade."),
        # 6
        s("CRISIS", EKIP, "The narrow canyon road; rocks and mud blocking the way.",
          ("A rumble; rocks and mud slide down onto the road ahead.",
           "Kaan brakes hard.",
           "The road is completely blocked."),
          "Wide shot of the landslide.",
          "Rumble, crash, tense music.",
          "Danger.",
          r=("Kaan", "Heyelan! Yol kapandı!")),
        # 7
        s("CRISIS", ["kaan", "defne"], "The narrow road; no space to turn.",
          ("There's no space to turn the van around.",
           "Defne gets out to guide him.",
           "Kaan starts reversing slowly."),
          "Wide shot of the narrow road.",
          "Engine, tense music.",
          "Problem."),
        # 8
        s("CRISIS", ["kaan"], "The van reversing along the cliff road.",
          ("Kaan reverses for kilometers, leaning out of the window.",
           "The river roars below.",
           "Sweat runs down his face."),
          "Comic but tense close-ups.",
          "River, beeping reverse alarm.",
          "Tension and comedy.",
          r=("Kaan", "Yirmi kilometre geri geri…")),
        # 9
        s("CRISIS", EKIP, "A wider spot on the road.",
          ("They finally reach a wide spot.",
           "Kaan turns the van around.",
           "He collapses on the steering wheel."),
          "Wide shot.",
          "Relief music.",
          "Relief."),
        # 10
        s("SECRET", ["kerem"], "A riverside tea garden while waiting for another route.",
          ("Kerem flips through the notebook.",
           "He notices the last pages are thicker.",
           "Two pages are glued together."),
          "Close-up on the thick pages.",
          "River, mysterious music.",
          "Discovery."),
        # 11
        s("SECRET", ["kerem", "defne"], "The tea garden.",
          ("Kerem tries to separate the pages with his fingernail.",
           "Defne stops him; it could tear.",
           "She suggests steam later."),
          "Two-shot.",
          "Soft tension.",
          "Caution.",
          r=("Defne", "Yırtılır. Buharla açmalıyız.")),
        # 12
        s("TRADE", ["defne"], "The tea garden; Defne on the phone.",
          ("Defne calls a breakfast chain about chestnut honey.",
           "They order everything.",
           "She toasts with tea."),
          "Medium shot.",
          "Triumphant music.",
          "Success.",
          r=("Defne", "Kestane balı kırk bin getirdi!"),
          k=(1_950_000, 1_990_000)),
        # 13
        s("SECRET", EKIP, "The tea garden at sunset.",
          ("Kerem holds the glued pages to the light.",
           "Through the paper, a map shape is visible.",
           "All three lean in."),
          "Backlit close-up of the pages.",
          "Music building.",
          "Mystery."),
        # 14
        s("SECRET", ["kerem"], "The tea garden.",
          ("Kerem notices a fingerprint in old ink on the glued edge.",
           "It looks recent, not a hundred years old.",
           "He remembers the bookseller's hands."),
          "Macro on the fingerprint.",
          "Heartbeat.",
          "Suspicion."),
        # 15
        s("CLIFFHANGER", EKIP, VAN + " on a new mountain road at night toward Rize.",
          ("The van drives toward Rize in the dark.",
           "Kerem holds the glued pages.",
           "He whispers the question that haunts him. Cut to black."),
          "Close-up on Kerem, cut to black.",
          "Engine, deep music hit.",
          "Cliffhanger.",
          r=("Kerem", "Sayfaları sahaf yapıştırmış. Neden?")),
    ],
)

BOLUMLER = [B]
