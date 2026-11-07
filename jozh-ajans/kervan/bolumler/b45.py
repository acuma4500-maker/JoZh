# -*- coding: utf-8 -*-
"""B45 · Ankara · BÜYÜK SİPARİŞ — kasa 2.520.000 → 2.410.000 → 2.430.000"""
from bolumler._ortak import EKIP, VAN, EP, s, ac, et, kapak

B = EP(
    45,
    aciklama=ac(45, "📦", "Ankara'da sezonun en büyük siparişi: bir zincir mağaza! Mallar hazır, kamyonet dolu… ve "
                "zincir mağaza iflas ediyor. Sezonun en büyük zararı. Ama Ulus'taki eski hanın arşivinden 1926 "
                "tarihli bir tapu çıkıyor.", "Sabri Kapadokya'da neden arazi almış?"),
    etiketler=et(45, "Ankara", "Ulus", "tiftik"),
    kapak=kapak("defne", ["kerem", "kaan"],
                "An old stone han in Ulus, Ankara, at dusk; dusty archive shelves full of old ledgers and deeds, "
                "Ankara Castle visible through an arched window, stacked boxes of meerschaum and helva in the van "
                "outside.",
                "Defne in the center sitting on a pile of unsold boxes, holding a phone with a bankruptcy news "
                "headline (no readable text), eyes closed. Kerem on the left pulling an old deed document from an "
                "archive box, amazed. Kaan on the right wrapped in a soft white mohair scarf, hugging Defne's shoulder.",
                "Heavy loss and a sudden ray of hope."),
    senaryolar=[
        # 1
        s("HOOK", ["defne"], "A big chain store's loading dock in Ankara; closed metal shutters with a notice taped on them.",
          ("Defne runs to the loading dock with the van behind her.",
           "The shutters are closed; a notice is taped on them.",
           "She reads it and drops her ledger."),
          "Tracking shot, then close-up on her face.",
          "Footsteps, a heavy music hit.",
          "Shock.",
          r=("Defne", "İflas mı? Bütün sipariş…")),
        # 2
        s("ARRIVAL", EKIP, VAN + " entering Ankara; wide boulevards and Anıtkabir on the hill.",
          ("The van enters the capital.",
           "Defne talks on the phone about the big order.",
           "Kaan cheers about the 'biggest deal ever'."),
          "Drone shot.",
          "City, ambitious music.",
          "Excitement.",
          alt="İKİ GÜN ÖNCE · ANKARA"),
        # 3
        s("TRADE", ["defne"], "A chain store headquarters office in Ankara; a buyer in a suit.",
          ("The buyer orders meerschaum and helva for all branches.",
           "Defne asks for a deposit; he says payment on delivery.",
           "She hesitates, then agrees."),
          "Two-shot.",
          "Office, tense music.",
          "Risky deal.",
          r=("Alıcı", "Teslimatta öderiz. Merak etmeyin.")),
        # 4
        s("TRADE", ["defne", "kaan"], "The meerschaum master's workshop by phone and a helva factory.",
          ("Defne orders extra meerschaum and big batches of helva.",
           "The van fills up to the roof.",
           "Kaan barely closes the doors."),
          "Medium shots.",
          "Upbeat but uneasy music.",
          "All in."),
        # 5
        s("CRISIS", ["defne"], "Inside " + VAN + " in Ankara traffic.",
          ("Defne reads breaking business news on her phone.",
           "The chain store company is in trouble.",
           "She calls the buyer; no answer."),
          "Close-up on Defne.",
          "Traffic, rising tension.",
          "Dread."),
        # 6
        s("CRISIS", ["defne"], "The loading dock.",
          ("They arrive; the shutters are closed.",
           "A notice says the company declared bankruptcy.",
           "Defne drops her ledger."),
          "Close-up on the notice (no readable text), then Defne.",
          "A heavy music hit.",
          "Shock."),
        # 7
        s("CRISIS", EKIP, "The loading dock.",
          ("The three stand silently in front of the closed shutters.",
           "The van behind them is full of goods.",
           "Rain begins."),
          "Wide shot.",
          "Rain, sad strings.",
          "Despair."),
        # 8
        s("CRISIS", ["defne"], "Inside the van in the rain.",
          ("Defne calculates the loss.",
           "Goods they cannot return, paid on credit.",
           "She writes the biggest red number yet."),
          "Close-up on the ledger.",
          "Rain on the roof.",
          "Biggest loss.",
          r=("Defne", "Yüz on bin. En büyük zararımız."),
          k=(2_520_000, 2_410_000)),
        # 9
        s("CRISIS", ["kaan", "kerem", "defne"], "Inside the van.",
          ("Kaan wraps a soft mohair scarf around Defne.",
           "Kerem says Sabri lost everything once too.",
           "Defne smiles weakly."),
          "Close three-shot.",
          "Soft music.",
          "Comfort."),
        # 10
        s("SECRET", ["kerem"], "An old stone han in Ulus; an archive room with dusty shelves.",
          ("Kerem follows the photo's address to an old han.",
           "An archivist leads him into a dusty room.",
           "He searches boxes from 1926."),
          "Tracking shot.",
          "Dust, mysterious music.",
          "Search."),
        # 11
        s("SECRET", ["kerem"], "The archive.",
          ("Kerem finds a folder with the camel symbol.",
           "Inside is an old land deed.",
           "He reads the location."),
          "Close-up on the deed.",
          "Heartbeat.",
          "Discovery.",
          r=("Kerem", "Bir tapu. Kapadokya'da bir arazi!")),
        # 12
        s("TRADE", ["defne"], "A handicraft fair in Ankara; mohair scarves and helva.",
          ("Defne sets up a stand at a handicraft fair.",
           "She sells mohair scarves and some helva.",
           "A small recovery."),
          "Medium shot.",
          "Light hopeful music.",
          "Recovery.",
          k=(2_410_000, 2_430_000)),
        # 13
        s("SECRET", EKIP, "The archive; Defne and Kaan arrive.",
          ("Kerem shows them the deed.",
           "Defne reads the owner names.",
           "There are three names."),
          "Close-up on the deed.",
          "Music building.",
          "Revelation."),
        # 14
        s("SECRET", ["defne"], "The archive.",
          ("Defne reads the first name: Sabri Kervancı.",
           "The other two names are partly faded.",
           "Only one letter of each is clear."),
          "Macro on the faded names.",
          "Heartbeat.",
          "Mystery."),
        # 15
        s("CLIFFHANGER", EKIP, "The archive at night.",
          ("Kerem traces the faded letters.",
           "One of them matches his own family name's first letter.",
           "He freezes. Cut to black."),
          "Extreme close-up, cut to black.",
          "A deep music hit.",
          "Cliffhanger.",
          r=("Defne", "Sabri Kervancı ve iki ortağı.")),
    ],
)

BOLUMLER = [B]
