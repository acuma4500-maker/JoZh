# -*- coding: utf-8 -*-
"""Kervan — prompt şablonları.

KAPAK1, PEK_YAKINDA ve SENARYO metinleri tasarım belgesinin 4.1–4.3 bölümlerinden
birebir alınmıştır (tests/test_sablonlar.py bunu denetler). Yalnızca köşeli
parantezli yerler doldurulur.
"""
import io
import os
import re

from karakterler import K, SOGUK

KAPAK1 = 'Instagram Reels cover image, vertical 9:16 (1080x1920), semi-realistic stylized 3D animation still, Pixar-like proportions with realistic textures, cinematic lighting, rich saturated colors, high detail, professional animated movie poster quality.\n\nTITLE TEXT (IMPORTANT):\n\nAdd a large, visually striking Turkish title at the top of the image:\n\n“BÖLÜM [BÖLÜM NUMARASI]”\n“[BÖLÜM ADI]”\n\nTypography:\n\n* “BÖLÜM [NUMARA]” in smaller, elegant, bold uppercase letters.\n* “[BÖLÜM ADI]” in large, bold, cinematic typography.\n* Use a slightly distressed white font with subtle warm golden lighting.\n* Make the most important words particularly prominent.\n* Add a subtle dark shadow behind the letters for readability.\n* Perfect Turkish spelling and clearly readable typography.\n* Position the title in the upper portion without covering the characters or important visual elements.\n\nKeep all main characters and important visual elements inside the central square area so the cover works when Instagram crops it to 1:1 or 4:5.\n\nCHARACTERS (SAME FIXED DESIGN AS PREVIOUS EPISODES):\n\n[ANA KARAKTERİN SABİT TASARIMI]\n\n[YAN KARAKTERLERİN SABİT TASARIMLARI]\n\nAll characters must maintain absolute visual consistency with their previous appearances, including faces, hairstyles, clothing, accessories and body proportions.\n\nSETTING:\n\n[MEKÂNIN DETAYLI AÇIKLAMASI]\n\nCOMPOSITION:\n\n[SAHNENİN NASIL GÖRÜNECEĞİ]\n\nDescribe:\n\n* Where each character stands.\n* What each character is holding.\n* Their facial expressions.\n* Their body language.\n* Important objects in the scene.\n* Background details.\n\nMOOD AND EMOTION:\n\n[SAHNENİN DUYGUSU VE HİKÂYENİN ATMOSFERİ]\n\nLIGHTING AND QUALITY:\n\nCinematic lighting, dramatic rim lighting, realistic textures, expressive facial details, beautiful depth of field, detailed environments, professional color grading and premium 3D animated feature film rendering.\n\nThe final image should feel like the official cover of Episode [BÖLÜM NUMARASI] of the exact same animated series as previous episodes.\n\nMaintain absolute character consistency throughout the entire series.\n\nNo additional text, no random letters, no logos, no watermark.\n\nThe ONLY permitted text elements are:\n“BÖLÜM [NUMARA]”\n“[BÖLÜM ADI]”'

PEK_YAKINDA = 'ADDITIONAL TEXT – PEK YAKINDA:\n\nAdd the exact Turkish text:\n\n“PEK YAKINDA”\n\nTypography and positioning:\n\n* Place “PEK YAKINDA” prominently in the middle area of the image.\n* Use bold, uppercase cinematic lettering.\n* White or warm golden color with a subtle glowing effect.\n* Add a soft dark shadow for maximum readability.\n* Make it visually prominent, like an official animated movie trailer announcement.\n* Position it carefully without covering the main characters’ faces or important objects.\n* Maintain a premium cinematic movie-poster appearance.\n\nThe ONLY permitted text elements are:\n“BÖLÜM [NUMARA]”\n“[BÖLÜM ADI]”\n“PEK YAKINDA”'

SENARYO = 'Vertical 9:16 video, 8 seconds, semi-realistic stylized 3D animation, Pixar-like proportions with realistic textures, cinematic lighting, rich saturated colors — same animated series as previous episodes.\n\nSCENE [NUMARA] OF 15 — ROLE: [HOOK / ARRIVAL / TRADE / CRISIS / SECRET / CLIFFHANGER]\n\nCHARACTERS (SAME FIXED DESIGN AS PREVIOUS EPISODES):\n[SAHNEDEKİ KARAKTERLERİN SABİT TASARIMLARI]\nAll characters must keep absolute visual consistency: faces, hairstyles, clothing, accessories, proportions.\n\nSETTING:\n[MEKÂN — gerçek şehir, saat, hava]\n\nACTION (EXACT TIMELINE):\n0–2 s: [açılış hareketi]\n2–6 s: [ana olay]\n6–8 s: [dönüş — soru, şaşkınlık veya gerilim]\n\nCAMERA:\n[dinamik kamera hareketi]\n\nDIALOGUE (TURKISH, SHORT, LIP-SYNCED):\n[KARAKTER]: "[en fazla 6–8 kelime]"\nPerfect Turkish pronunciation. No other spoken lines.\n\nSOUND:\n[ortam sesi + müzik]\n\nMOOD AND TENSION:\n[duygu]\n\nAVOID: subtitles, on-screen text, logos, watermark, extra characters, changes in character design.'

ROLLER = ("HOOK", "ARRIVAL", "TRADE", "CRISIS", "SECRET", "CLIFFHANGER")
REPLIK_SINIRI = 8
_KAPAK1_KAPANIS = "\n\nThe ONLY permitted text elements are:\n“BÖLÜM [NUMARA]”\n“[BÖLÜM ADI]”"
_PROFIL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "profil", "profil-fotografi-prompt.md")


def _doldur(metin, alanlar):
    for k, v in alanlar.items():
        metin = metin.replace(k, v)
    return metin


def _tarifler(kimler, soguk):
    metin = "\n\n".join(K[ad] for ad in kimler)
    return metin + ("\n\n" + SOGUK if soguk else "")


def kapak1(no, baslik, ana, yanlar, mekan, kompozisyon, duygu, soguk=False):
    """Ana kapak promptu. ana/yanlar: karakter anahtarları ('kerem', 'defne', 'kaan')."""
    return _doldur(KAPAK1, {
        "[BÖLÜM NUMARASI]": str(no),
        "[NUMARA]": str(no),
        "[BÖLÜM ADI]": baslik,
        "[ANA KARAKTERİN SABİT TASARIMI]": K[ana],
        "[YAN KARAKTERLERİN SABİT TASARIMLARI]": _tarifler(yanlar, soguk),
        "[MEKÂNIN DETAYLI AÇIKLAMASI]": mekan,
        "[SAHNENİN NASIL GÖRÜNECEĞİ]": kompozisyon,
        "[SAHNENİN DUYGUSU VE HİKÂYENİN ATMOSFERİ]": duygu,
    })


def kapak2(no, baslik, ana, yanlar, mekan, kompozisyon, duygu, soguk=False):
    """Pek yakında kapağı: Kapak 1'in kapanış listesi çıkarılır, PEK YAKINDA bloğu eklenir."""
    assert KAPAK1.endswith(_KAPAK1_KAPANIS)
    govde = KAPAK1[:-len(_KAPAK1_KAPANIS)] + "\n\n" + PEK_YAKINDA
    return _doldur(govde, {
        "[BÖLÜM NUMARASI]": str(no),
        "[NUMARA]": str(no),
        "[BÖLÜM ADI]": baslik,
        "[ANA KARAKTERİN SABİT TASARIMI]": K[ana],
        "[YAN KARAKTERLERİN SABİT TASARIMLARI]": _tarifler(yanlar, soguk),
        "[MEKÂNIN DETAYLI AÇIKLAMASI]": mekan,
        "[SAHNENİN NASIL GÖRÜNECEĞİ]": kompozisyon,
        "[SAHNENİN DUYGUSU VE HİKÂYENİN ATMOSFERİ]": duygu,
    })


def senaryo(no, rol, kimler, mekan, aksiyon, kamera, replik, ses, duygu, soguk=False):
    """Tek senaryo promptu. replik: (konuşan, 'Türkçe metin') ya da None. aksiyon: (0–2 s, 2–6 s, 6–8 s)."""
    if rol not in ROLLER:
        raise ValueError("bilinmeyen rol: %s" % rol)
    metin = SENARYO
    if replik is None:
        metin = re.sub(r"DIALOGUE \(TURKISH.*?No other spoken lines\.", "DIALOGUE: No dialogue.", metin, flags=re.S)
    else:
        kim, soz = replik
        if len(soz.split()) > REPLIK_SINIRI:
            raise ValueError("replik %d kelimeyi geçiyor: %s" % (REPLIK_SINIRI, soz))
        metin = metin.replace('[KARAKTER]: "[en fazla 6–8 kelime]"', '%s: "%s"' % (kim.upper(), soz))
    a0, a1, a2 = aksiyon
    return _doldur(metin, {
        "[NUMARA]": str(no),
        "[HOOK / ARRIVAL / TRADE / CRISIS / SECRET / CLIFFHANGER]": rol,
        "[SAHNEDEKİ KARAKTERLERİN SABİT TASARIMLARI]": _tarifler(kimler, soguk),
        "[MEKÂN — gerçek şehir, saat, hava]": mekan,
        "[açılış hareketi]": a0,
        "[ana olay]": a1,
        "[dönüş — soru, şaşkınlık veya gerilim]": a2,
        "[dinamik kamera hareketi]": kamera,
        "[ortam sesi + müzik]": ses,
        "[duygu]": duygu,
    })


def profil_prompt():
    """Profil fotoğrafı promptu (jozh-ajans/profil/profil-fotografi-prompt.md içindeki kod bloğu)."""
    with io.open(_PROFIL, encoding="utf-8") as fh:
        metin = fh.read()
    return re.search(r"```\n(.*?)\n```", metin, re.S).group(1)
