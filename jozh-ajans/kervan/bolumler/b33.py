# -*- coding: utf-8 -*-
"""B33 · Kars · KAŞAR — kasa 1.650.000 → 1.670.000 → 1.760.000"""
from bolumler._ortak import EKIP, VAN, EP, s, ac, et, kapak

B = EP(
    33,
    aciklama=ac(33, "🧀", "Tren bileti onları Kars'a getirdi. Gravyer peyniri olgunlaşmayı bekliyor; Defne parayı "
                "bağlamaktan korkuyor ama riske giriyor. Eski Kars garının bekleme salonunda ise Sabri'nin duvara "
                "kazıdığı bir harita var: donmuş bir göl.", "Defne'nin riski tutacak mı?"),
    etiketler=et(33, "Kars", "kaşar", "gravyer"),
    kapak=kapak("defne", ["kerem", "kaan"],
                "The historic Kars train station waiting hall in winter; old wooden benches, a big arched window "
                "showing snow and Baltic-style stone buildings, a carved map on the plaster wall; a cheese cellar "
                "with giant gruyère wheels visible through a door.",
                "Defne in the center holding a giant gruyère wheel with both arms, determined. Kerem on the left "
                "tracing a carved map on the wall with his gloved finger. Kaan on the right sitting on a bench with a "
                "plate of kaşar slices, eyes closed in bliss.",
                "Cold outside, warm inside, a brave bet and a frozen clue."),
    senaryolar=[
        # 1
        s("HOOK", ["defne"], "A cheese aging cellar in Kars; huge gruyère wheels on wooden shelves.",
          ("Defne stands among giant cheese wheels.",
           "The cheese maker says it needs months to age.",
           "Defne stares at her ledger, torn."),
          "Wide cellar shot, then close-up on Defne.",
          "Dripping, tense music.",
          "Dilemma.",
          r=("Defne", "Paramızı aylarca bağlarsak…")),
        # 2
        s("ARRIVAL", EKIP, VAN + " entering snowy Kars; Baltic-style stone buildings and the castle.",
          ("The van enters Kars through snowy streets.",
           "Old Baltic-style buildings line the road.",
           "Kerem holds the 1926 train ticket."),
          "Drone shot.",
          "Snow crunch, nostalgic music.",
          "Arrival.",
          alt="BİR GÜN ÖNCE · KARS"),
        # 3
        s("TRADE", ["defne", "kaan"], "A fruit shop in Kars.",
          ("Defne sells the giant melon and some apricots to a shop.",
           "The owner laughs at the melon's size.",
           "Kaan says goodbye to the melon sadly."),
          "Comic medium shot.",
          "Comic music.",
          "Fun."),
        # 4
        s("TRADE", ["defne"], "A café in Kars.",
          ("Defne delivers apricots to the shop chain's driver.",
           "She gets the payment confirmation.",
           "She writes it down."),
          "Close-up on the ledger.",
          "Upbeat music.",
          "Success."),
        # 5
        s("TRADE", ["defne"], "The café.",
          ("Defne adds the melon money.",
           "She smiles.",
           "She opens a cheese map of Kars."),
          "Close-up.",
          "Light music.",
          "Planning.",
          r=("Defne", "Yirmi bin daha. Sırada peynir var."),
          k=(1_650_000, 1_670_000)),
        # 6
        s("TRADE", ["defne", "kaan"], "A traditional Kars kaşar dairy.",
          ("A cheesemaker shows them fresh kaşar.",
           "Kaan tastes it and melts.",
           "Defne buys a large amount of kaşar."),
          "Close-up on cheese.",
          "Warm music.",
          "Trade."),
        # 7
        s("CRISIS", ["defne"], "The gruyère aging cellar.",
          ("The cheese maker offers aged gruyère at a high price, or young wheels cheap.",
           "Young wheels need more aging before selling.",
           "Defne thinks hard."),
          "Medium shot.",
          "Ticking, tense music.",
          "Dilemma."),
        # 8
        s("CRISIS", ["defne", "kerem"], "Outside the cellar in the snow.",
          ("Defne asks Kerem what Sabri would do.",
           "Kerem opens the notebook to a page about patience.",
           "Defne decides to take the risk."),
          "Two-shot in the snow.",
          "Soft music.",
          "Decision.",
          r=("Kerem", "Sabri yazmış: Sabırlı tüccar kazanır.")),
        # 9
        s("TRADE", ["defne"], "The cellar.",
          ("Defne buys young gruyère wheels.",
           "She arranges to leave them aging in the cellar.",
           "She signs a storage agreement."),
          "Close-up on signing.",
          "Pen, determined music.",
          "Bold move."),
        # 10
        s("SECRET", ["kerem"], "The historic Kars train station waiting hall.",
          ("Kerem enters the old waiting hall with the ticket.",
           "He walks along the old plaster walls.",
           "He finds a carved map behind a bench."),
          "Tracking shot, reveal.",
          "Echoes, mysterious music.",
          "Discovery."),
        # 11
        s("SECRET", ["kerem", "kaan"], "The carved map.",
          ("Kaan helps move the bench.",
           "The map shows a lake and a small sled.",
           "A camel is carved next to it."),
          "Close-up on the map.",
          "Heartbeat.",
          "Clue."),
        # 12
        s("TRADE", ["defne"], "The dairy office; Defne on the phone.",
          ("Defne calls a gourmet chain in Istanbul.",
           "They order kaşar now and gruyère in advance.",
           "They pay a big deposit."),
          "Medium shot.",
          "Triumphant music.",
          "Risk pays.",
          r=("Defne", "Gravyere ön ödeme geldi! Risk tuttu!"),
          k=(1_670_000, 1_760_000)),
        # 13
        s("SECRET", EKIP, "The waiting hall at night.",
          ("The three study the carved map.",
           "Kerem matches it with a lake on the phone.",
           "The lake is near the Georgian border."),
          "Three-shot, close-up on the phone.",
          "Music building.",
          "Next step."),
        # 14
        s("SECRET", ["kerem"], "The waiting hall.",
          ("Kerem finds words carved under the map.",
           "He brushes them with his glove.",
           "He reads them slowly."),
          "Close-up on the words.",
          "Wind outside.",
          "Riddle."),
        # 15
        s("CLIFFHANGER", EKIP, "The station at night, snow outside.",
          ("Kerem reads the line aloud.",
           "Outside, snow keeps falling.",
           "A train whistle sounds in the dark. Cut to black."),
          "Close-up on Kerem, cut to black.",
          "Train whistle, deep music hit.",
          "Riddle.",
          r=("Kerem", "Göl buz tutunca, buzun altına bak.")),
    ],
)

BOLUMLER = [B]
