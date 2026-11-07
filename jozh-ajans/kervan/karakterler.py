# -*- coding: utf-8 -*-
"""Kervan — sabit karakter tarifleri.

Bu metinler bütün promptlara HARFİ HARFİNE aynı girer. Bir kelime bile değişirse
Flow karakterin yüzünü/kıyafetini değiştirebilir; değişiklik yalnızca burada yapılır.
"""

K = {
    "kerem": (
        "KEREM: a 20-year-old Turkish young man, tall and lean, warm olive skin, short wavy dark brown hair "
        "that is always slightly messy, thick dark eyebrows, hazel eyes, light stubble. He wears a faded "
        "mustard-yellow canvas jacket over a plain white t-shirt, dark green cargo trousers and worn brown "
        "leather boots. A small brass compass hangs on a leather cord around his neck. He carries a brown "
        "canvas messenger bag across his body, where he keeps an old brown leather notebook with a golden "
        "compass rose on its cover. Curious, dreamy, thoughtful expression."
    ),
    "defne": (
        "DEFNE: a 19-year-old Turkish young woman, medium height, slim, light olive skin, long straight black "
        "hair tied in a high ponytail, sharp dark brown eyes, thin round gold-rimmed glasses, small silver hoop "
        "earrings. She wears an oversized burgundy hoodie, light blue straight-leg jeans and clean white "
        "sneakers. A small black crossbody bag rests on her hip and a pencil is tucked behind her right ear. "
        "She often holds a smartphone or a small black ledger notebook. Confident, quick-witted, sharp "
        "expression."
    ),
    "kaan": (
        "KAAN: an 18-year-old Turkish young man, shorter and stocky, round friendly face, tanned skin, curly "
        "black hair under a backwards navy blue baseball cap, big brown eyes, wide playful grin. He wears a "
        "light-wash denim jacket with rolled-up sleeves over a bright orange t-shirt, black jogger pants and "
        "red sneakers. A wooden spoon sticks out of his jacket's chest pocket and a small tan leather food "
        "pouch hangs from his belt. Energetic, funny, impulsive expression."
    ),
}

# Soğuk yerlerde (Doğu Anadolu, kış) eklenecek sabit cümle; kıyafetin geri kalanı değişmez.
SOGUK = ("Because it is cold, each character also wears a plain dark grey wool scarf and simple black gloves; "
         "everything else about their clothing stays exactly the same.")


def referans_prompt(ad):
    """Flow'da karakterin referans görselini üretmek için prompt."""
    return (
        "Character reference sheet, 16:9, semi-realistic stylized 3D animation, Pixar-like proportions with "
        "realistic textures, soft even studio lighting, plain light grey background.\n\n"
        "Show the same single character three times side by side: full body front view, full body three-quarter "
        "view, and a close-up portrait of the face. Neutral standing pose, arms relaxed.\n\n"
        "CHARACTER:\n" + K[ad] + "\n\n"
        "This is the official fixed design for an animated series: every detail of the face, hair, clothing and "
        "accessories must be clear and consistent across all three views.\n\n"
        "No text, no letters, no labels, no logos, no watermark."
    )
