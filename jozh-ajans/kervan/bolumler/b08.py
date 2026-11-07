# -*- coding: utf-8 -*-
"""B08 · Kütahya · ÇİNİ USTASI — kasa 348.000 → 368.000 → 392.000"""
from bolumler._ortak import EKIP, VAN, EP, s, ac, et, kapak

B = EP(
    8,
    aciklama=ac(8, "🫖", "Mühür parçası Kütahya'yı gösterdi. İznik çinileri bir koleksiyoncuya \"fazla yeni\" geliyor; "
                "Kerem'in anlattığı hikâye ise fikrini değiştiriyor. Ve yüz yıllık bir atölyenin duvarında, yüzleri "
                "silinmiş üç genç…", "Fotoğraftaki yüzleri kim sildi?"),
    etiketler=et(8, "Kütahya", "porselen", "çini"),
    kapak=kapak("kerem", ["defne", "kaan"],
                "An old Kütahya tile and porcelain workshop in warm afternoon light; walls covered with hand-painted "
                "tiles, shelves of white porcelain tea sets with blue patterns, an old framed photograph on the wall.",
                "Kerem in the center standing in front of an old framed black-and-white photo of three young people "
                "and a camel whose faces are scratched out; he holds the notebook to his chest. Defne on the left "
                "holding a delicate porcelain teacup, eyes on the photo. Kaan on the right balancing a tall stack of "
                "tea saucers, frozen mid-step.",
                "Curious and slightly eerie, a mystery staring back from the past."),
    senaryolar=[
        # 1
        s("HOOK", ["kerem"], "A dim corner of an old Kütahya workshop; an old framed photograph on a tiled wall.",
          ("A slow light sweeps across an old black-and-white photo of three young people and a camel.",
           "The three faces in the photo are scratched out.",
           "Kerem's reflection appears in the glass over the scratched faces."),
          "Slow push-in on the photo, reflection reveal.",
          "Silence, a single eerie piano note.",
          "Chilling mystery.",
          r=("Kerem", "Yüzleri… kim kazımış?")),
        # 2
        s("ARRIVAL", EKIP, VAN + " entering Kütahya in the morning; a giant porcelain vase monument at a roundabout.",
          ("The van circles a huge porcelain vase in the city square.",
           "Kaan presses his face to the window in awe.",
           "Defne checks her list of collectors."),
          "Drone shot circling the vase, cut inside to Kaan.",
          "City sounds, warm music.",
          "Fresh start.",
          alt="BİR GÜN ÖNCE · KÜTAHYA"),
        # 3
        s("TRADE", ["defne", "kerem"], "A refined antique tile collector's shop in Kütahya; a strict old collector with a monocle-like loupe.",
          ("Defne unwraps the İznik tiles on velvet.",
           "The collector inspects one with a loupe and frowns.",
           "He pushes the tile back across the table."),
          "Close-up through the loupe, then a reaction shot of Defne.",
          "Clock ticking, a tense music note.",
          "Rejection.",
          r=("Koleksiyoncu", "Fazla yeni. Ruhu yok.")),
        # 4
        s("TRADE", ["kerem"], "The same collector's shop.",
          ("Kerem steps forward and tells the story of the night in İznik.",
           "He shows a photo of the old master working at dawn and the cracked kiln.",
           "The collector slowly lowers his loupe, listening."),
          "Slow push-in on Kerem, then on the collector's softening face.",
          "Kerem's voice tone, gentle music.",
          "Persuasion through story.",
          r=("Kerem", "Bu çiniler bir gecede kurtarıldı.")),
        # 5
        s("TRADE", ["defne", "kerem"], "The collector's shop; he opens a drawer of cash.",
          ("The collector buys half of the tiles for his collection.",
           "He hands Defne the money with a nod of respect.",
           "Defne gives Kerem a surprised, impressed look."),
          "Close-up of cash, then a two-shot.",
          "Cash rustle, warm music.",
          "Success.",
          k=(348_000, 368_000)),
        # 6
        s("TRADE", ["defne", "kaan"], "A porcelain factory outlet in Kütahya; rows of white tea sets with blue patterns.",
          ("Defne orders porcelain tea sets wholesale.",
           "Kaan carries a tall stack of saucers, wobbling.",
           "A worker gasps; Kaan freezes on one foot."),
          "Wide shot, slow-motion wobble.",
          "Porcelain clinking, suspense comedy music.",
          "Comic tension.",
          r=("Kaan", "Kimse nefes almasın…")),
        # 7
        s("TRADE", ["kaan", "defne"], "The same porcelain outlet.",
          ("Kaan miraculously sets the stack down without breaking anything.",
           "Everyone in the shop applauds.",
           "Defne exhales and adds the tea sets to the ledger."),
          "Close-up on the saucers landing, then a wide applause shot.",
          "Relieved applause, comic music.",
          "Relief."),
        # 8
        s("SECRET", ["kerem"], "A quiet back street in old Kütahya with Ottoman wooden houses.",
          ("Kerem reads an old order list in the notebook dated 1926.",
           "The last name on the list matches a sign above an old workshop door.",
           "He looks up at the sign, then at the notebook again."),
          "Insert of the list, then a tilt up to the sign.",
          "Footsteps on cobbles, curious motif.",
          "Discovery."),
        # 9
        s("SECRET", EKIP, "Inside the old workshop; walls covered with tiles; an elderly woman painter in her seventies with paint-stained fingers.",
          ("The elderly painter welcomes them with tea.",
           "Kerem shows her the notebook's list; she smiles at her grandfather's name.",
           "She points at the framed photo on the wall."),
          "Warm medium shot, then a pan to the photo.",
          "Tea pouring, gentle music.",
          "Warm mystery.",
          r=("Ressam", "Dedem bu siparişi hiç unutmadı.")),
        # 10
        s("SECRET", EKIP, "The old workshop; the three stand before the framed photo.",
          ("The photo shows three young people and a camel in front of this workshop in 1926.",
           "All three faces have been scratched out of the photo.",
           "The painter says she found it like that as a child."),
          "Slow push-in on the photo, reaction shots.",
          "Silence, a low cello note.",
          "Eerie."),
        # 11
        s("CRISIS", ["defne", "kaan"], "The loading area of the porcelain outlet; " + VAN + " packed with boxes.",
          ("A box slips from Kaan's hands; Defne dives and catches it at the last second.",
           "They both stare at the box, breathing heavily.",
           "Kaan opens it: one cup is cracked."),
          "Slow-motion dive, then a close-up of the cracked cup.",
          "Gasp, a short comic sad sting.",
          "Close call."),
        # 12
        s("TRADE", ["defne"], "A cozy tea house in Kütahya; the owner admires a porcelain tea set.",
          ("The tea house owner orders tea sets for his whole café.",
           "He even buys the cracked cup 'for good luck'.",
           "Defne laughs and writes a happy number."),
          "Medium shot, close-up of the cracked cup being lifted.",
          "Tea house chatter, warm music.",
          "Happy deal.",
          r=("Defne", "Çatlak fincan bile satıldı!"),
          k=(368_000, 392_000)),
        # 13
        s("SECRET", ["kerem"], "The old workshop at dusk; the painter hands Kerem the framed photo.",
          ("The painter gives Kerem the photo to take with him.",
           "Kerem turns the frame over; a small envelope is taped to the back.",
           "He looks at the painter; she shakes her head, she never knew."),
          "Close-up on hands and the envelope.",
          "Paper tearing slowly, suspense music.",
          "Suspense."),
        # 14
        s("SECRET", EKIP, "Inside " + VAN + " at night under a street lamp.",
          ("Kerem opens the envelope; inside is a tiny woven carpet fragment.",
           "Its pattern looks like a map with a river and a small house.",
           "Defne recognizes the weaving style immediately."),
          "Macro shot of the carpet fragment, then Defne's face.",
          "Fabric rustling, mysterious music.",
          "Clue.",
          r=("Defne", "Bu dokuma… Uşak halısı.")),
        # 15
        s("CLIFFHANGER", EKIP, "Inside " + VAN + " at night.",
          ("Kerem holds the photo with the scratched faces next to the carpet map.",
           "In the corner of the photo, a tiny unscratched detail: a hand holding the same notebook.",
           "The street lamp outside flickers and goes out. Cut to black."),
          "Extreme close-up on the hand in the photo, then cut to black.",
          "Flicker buzz, deep bass hit.",
          "Cliffhanger.",
          r=("Kaan", "Fotoğraftaki defter… bizim defter!")),
    ],
)

BOLUMLER = [B]
