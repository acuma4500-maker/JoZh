# -*- coding: utf-8 -*-
"""Kervan — Bölüm 1–10."""
from karakterler import KAMYONET
from model import EP, S

EKIP = ["kerem", "defne", "kaan"]

# ── BÖLÜM 1 · İSTANBUL · ESKİ DEFTER ────────────────────────────────────────
# Kasa: 200.000 → 185.000 (defter, S5) → 186.000 (ilk satış, S13).
# S1 bir ileri-sarmadır (S11'in anı); kasa göstergesi S2'de "üç saat önce" ile başlar.
B01 = EP(
    1,
    aciklama=(
        "Bölüm 1: Eski Defter 📜\n\n"
        "Üç genç, 200.000 ₺ ve tek bir hayal… Kapalıçarşı'daki eski bir sahaftan aldıkları yüz yıllık defter, "
        "onları Türkiye'nin dört bir yanına götürecek bir yolculuğun ilk sayfası.\n\n"
        "Ama sahafın son sözü ve defterin arka kapağındaki iz… 👀\n\n"
        "Sence bu mühür kime ait? Yorumlara yaz 👇\n"
        "Takip et, yolculuğu kaçırma. Bölüm 2 yolda 🐪"
    ),
    etiketler=["#Kervan", "#KervanBölüm1", "#animasyon", "#dizi", "#İstanbul", "#Kapalıçarşı", "#macera",
               "#gizem", "#ticaret", "#keşfet", "#reels"],
    kapak=dict(
        ana="kerem", yanlar=["defne", "kaan"],
        mekan=("Inside a tiny, very old secondhand bookshop in the Sahaflar Bazaar of Istanbul's Grand Bazaar at "
               "golden hour. Tall wooden shelves packed with dusty antique books, Ottoman-era maps on the walls, warm "
               "sunbeams cutting through floating dust, a brass oil lamp on the counter."),
        kompozisyon=("Kerem stands in the center holding the old brown leather notebook open with both hands; the "
                     "golden compass rose on its cover glows softly and lights his amazed face from below. Defne "
                     "stands on the left, arms crossed, holding her black ledger, one eyebrow raised in suspicion. "
                     "Kaan stands on the right with a half-open box of Turkish delight, cheeks full, staring at the "
                     "notebook with wide eyes. Dusty shelves and hanging old maps fill the background."),
        duygu="Wonder and mystery: the first page of a great adventure, with a hint that the notebook hides a secret.",
    ),
    kasa_baslar=2,
    senaryolar=[
        S("HOOK", EKIP,
          "The vaulted main corridor of Istanbul's Grand Bazaar at closing time, evening; shop lights switching off "
          "one by one, metal shutters rolling down.",
          ("Kerem sprints straight toward the camera through the empty corridor, clutching the leather notebook "
           "to his chest; Defne and Kaan run right behind him.",
           "At the end of the corridor a heavy metal shutter is coming down; Defne points at it, shouting.",
           "All three dive and slide under the shutter at the last second; it slams shut behind them."),
          "Low-angle tracking shot moving backward fast in front of Kerem, then a sharp tilt down to the shutter.",
          "Running footsteps echoing under the domes, rattling shutter, fast tense percussion.",
          "Urgent, breathless, thrilling.",
          replik=("Defne", "Kerem, kepenk iniyor!")),
        S("ARRIVAL", EKIP,
          "Eminönü waterfront in Istanbul on a sunny morning, Galata Tower and seagulls in the background; "
          + KAMYONET + " is parked by the pier.",
          ("The three friends lean against the van; Kaan eats a sesame simit, Kerem gazes at the Golden Horn.",
           "Defne counts a thick stack of banknotes and writes the total in her black ledger.",
           "She snaps the ledger shut and looks at the other two seriously."),
          "Slow dolly-in from a wide shot to a medium shot on Defne.",
          "Seagulls, ferry horn, calm hopeful music.",
          "Hopeful, the calm before everything starts.",
          replik=("Defne", "İki yüz bin. Tek kuruş fazlası yok."),
          altyazi="ÜÇ SAAT ÖNCE"),
        S("ARRIVAL", EKIP,
          "The grand Nuruosmaniye Gate entrance of the Grand Bazaar in the morning, crowded with shoppers.",
          ("The three walk through the gate into the busy bazaar.",
           "Kaan stops at a Turkish delight stall glowing with colorful cubes and grabs a tester.",
           "Defne pulls him by the collar back into the crowd; he waves the cube at her."),
          "Steadicam following them from behind through the gate, then a quick whip pan to the stall.",
          "Bazaar crowd chatter, merchants calling out, upbeat playful music.",
          "Playful and lively.",
          replik=("Kaan", "Önce lokum, sonra hayaller.")),
        S("TRADE", ["kerem", "sahaf"],
          "Inside a tiny, very old secondhand bookshop in the Sahaflar Bazaar; dusty wooden shelves, sunbeams "
          "full of floating dust.",
          ("Kerem runs his finger along the spines on a low shelf.",
           "He pulls out an old brown leather notebook with a golden compass rose on its cover and blows the dust off.",
           "Behind the counter, the bookseller slowly lowers her reading glasses and watches him."),
          "Close-up on Kerem's hand, then a rack focus to the bookseller in the background.",
          "Quiet shop ambience, a clock ticking, a single mysterious music note.",
          "Mysterious, the feeling that something has been waiting."),
        S("TRADE", ["sahaf", "defne", "kerem"],
          "The same old bookshop counter; the notebook lies between them.",
          ("Defne slides a small stack of banknotes across the counter with a confident smile.",
           "The bookseller calmly pushes the money back without looking at it.",
           "Defne sighs, adds more banknotes; Kerem hugs the notebook."),
          "Over-the-shoulder shot from Defne to the bookseller, then a top-down shot of the counter.",
          "Coins and paper rustling, a short comic sting when Defne gives in.",
          "Tense negotiation that ends in a small defeat.",
          replik=("Sahaf", "On beş bin. Pazarlık yok."),
          kasa=(200_000, 185_000)),
        S("SECRET", ["kerem", "defne", "kaan"],
          "Outside the bookshop in a narrow bazaar passage, soft daylight.",
          ("Kerem carefully opens the notebook to its first page; old faded ink handwriting, illegible.",
           "Defne and Kaan lean over his shoulders; the page seems to glow faintly.",
           "Kerem looks up slowly with a stunned expression."),
          "Extreme close-up on the yellowed page, then a slow pull back to their three faces.",
          "Soft paper sounds, warm mysterious music swells.",
          "Wonder and curiosity.",
          replik=("Kerem", "Kervan İstanbul'dan çıkar, Edirne'de ilk hanı bulur.")),
        S("TRADE", ["defne", "kaan"],
          "A wholesale Turkish delight shop near the Spice Bazaar in Eminönü, stacks of colorful boxes and "
          "rock candy jars.",
          ("Defne points at stacks of boxes while the shopkeeper nods.",
           "Kaan secretly tastes cube after cube from the open trays.",
           "Defne catches him and slaps his hand; a cube flies into the air."),
          "Medium two-shot, then a quick push-in on Kaan's guilty face.",
          "Shop noise, a comic pop when the cube flies, playful music.",
          "Funny and energetic.",
          replik=("Defne", "Kaan! Sattığımızı yiyoruz şu an!")),
        S("SECRET", EKIP,
          "Next to " + KAMYONET + " on a sloping Eminönü street, midday.",
          ("Kaan and Defne load boxes of Turkish delight into the van.",
           "Kerem sits on the back step reading the notebook; a page shows a hand-drawn map of Anatolia with "
           "a dotted route.",
           "Kaan peeks over his shoulder and freezes with a box in his hands."),
          "Low angle from inside the van looking out, then an insert of the map page.",
          "Street traffic, cardboard thuds, curious music.",
          "Curious excitement.",
          replik=("Kaan", "Defter bize rota mı veriyor?")),
        S("CRISIS", EKIP,
          "A steep, busy street in Eminönü with honking traffic; " + KAMYONET + " has stalled.",
          ("Kerem turns the key; the engine coughs and dies.",
           "Defne and Kaan push the van uphill while drivers honk behind them.",
           "Kaan slips, lands on his bottom, and the van rolls back a little; everyone screams."),
          "Wide handheld shot from the front of the van, then a quick zoom on Kaan falling.",
          "Honking horns, engine coughing, comic chaos music.",
          "Comic panic.",
          replik=("Kaan", "İlk gün, ilk arıza!")),
        S("CRISIS", EKIP,
          "The same street; a friendly taxi driver has parked beside the van with jumper cables.",
          ("The engine finally starts and the three cheer.",
           "Kerem opens the notebook again; a small old receipt with the bookshop's stamp falls out.",
           "On its back is fresh handwriting; Kerem's smile disappears."),
          "Medium shot of the cheering, then a slow-motion insert of the falling receipt.",
          "Engine roar, cheers, then sudden silence and a low suspense drone.",
          "Relief turning into suspense.",
          replik=("Kerem", "Kapanmadan geri gel, yazıyor.")),
        S("CRISIS", EKIP,
          "The vaulted main corridor of the Grand Bazaar at closing time, evening; metal shutters rolling down.",
          ("Kerem, Defne and Kaan sprint through the emptying corridor.",
           "A heavy metal shutter is coming down at the end; Defne shouts and points.",
           "They dive and slide under it; it slams shut, and they lie panting inside the dark bookshop passage."),
          "Fast tracking shot from behind, then a ground-level shot as they slide under the shutter.",
          "Running footsteps echoing, shutter rattling, music hits a peak then cuts.",
          "Breathless suspense.",
          replik=("Kerem", "Bekleyin! Geliyoruz!")),
        S("SECRET", ["sahaf", "kerem", "defne", "kaan"],
          "Inside the dark old bookshop, lit only by a single brass oil lamp on the counter.",
          ("The bookseller sits behind the counter as if she was waiting for them.",
           "She looks at the three for a long moment, then gently taps the notebook's back cover with one finger.",
           "She smiles a small, knowing smile; the three exchange puzzled looks."),
          "Slow push-in on the bookseller's face in the lamplight.",
          "Lamp flame crackling, deep quiet, a mysterious music motif.",
          "Mysterious and warm.",
          replik=("Sahaf", "Defteri yanlış ellere vermedim, değil mi?")),
        S("TRADE", ["kaan", "defne"],
          "Eminönü square in front of the New Mosque at night, lit by street lamps; tourists walking around.",
          ("Kaan opens a box of Turkish delight and offers a taste to a group of tourists.",
           "The tourists buy two boxes and hand him cash; Kaan bows dramatically.",
           "Defne writes in her ledger and can't hide her proud smile."),
          "Handheld medium shot, then a close-up of Defne's ledger and smile.",
          "Night city ambience, tourists laughing, warm upbeat music.",
          "Joy of the first success.",
          replik=("Kaan", "İlk satış! Ortaklık kutlu olsun!"),
          kasa=(185_000, 186_000)),
        S("SECRET", EKIP,
          "Inside " + KAMYONET + " at night, parked under a street lamp by the Golden Horn.",
          ("Kerem turns the notebook over and shines his phone's flashlight on the back cover.",
           "Under the light, a deep pressed mark appears in the leather: half of a bronze camel caravan seal.",
           "Kerem's eyes widen; Defne and Kaan lean in from the front seats."),
          "Close-up on the back cover as the flashlight moves, then a reaction shot of the three faces.",
          "Silence, the hum of the city far away, a slow heartbeat-like drum.",
          "Rising mystery."),
        S("CLIFFHANGER", EKIP,
          "Inside " + KAMYONET + " at night; only the phone flashlight lights their faces.",
          ("Extreme close-up: Kerem's finger traces the pressed outline of the camel caravan; the right half "
           "of the seal is missing, broken off.",
           "Kerem slowly raises his eyes to the others.",
           "The flashlight flickers and goes out; darkness."),
          "Very slow push-in on the seal mark, then a quick cut to Kerem's eyes.",
          "Heartbeat drum stops; a single deep bass hit at the blackout.",
          "Shock and suspense: the adventure has just begun.",
          replik=("Kerem", "Bu bir mühür. Ve yarısı eksik.")),
    ],
)

BOLUMLER = [B01]
