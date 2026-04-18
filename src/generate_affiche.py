#!/usr/bin/env python3
"""
Générateur d'affiche réglementaire pour vidéoprotection

Génère une affiche conformes aux articles L223-1 à L223-9 et L251-1 à L255-1
du Code de la sécurité intérieure avec QR-code intégré vers le site CNIL.

Usage:
    python generate_affiche.py --autorisation "2024-12345" --telephone "01 23 45 67 89"
    python generate_affiche.py --autorisation "2024-12345" --telephone "01 23 45 67 89" --format png --output my_affiche
"""

import argparse
import os
import sys
from pathlib import Path

try:
    import qrcode
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("Erreur: Installez les dépendances avec: pip install -r requirements.txt")
    sys.exit(1)

SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
TEMPLATE_PATH = PROJECT_ROOT / "src" / "template.txt"
OUTPUT_DIR = PROJECT_ROOT / "output"

CNIL_URL = "https://www.cnil.fr/fr/videoprotection-droits-des-personnes"
QR_CODE_SIZE = 200
QR_CODE_CM = 2

AFFICHE_WIDTH = 800
AFFICHE_HEIGHT = 600
MARGIN = 40
QR_MARGIN = 20

FONT_SIZE_TITLE = 28
FONT_SIZE_BODY = 16
FONT_SIZE_FOOTER = 12

DEFAULT_FONT = "Arial"


def load_template():
    """Charge le template depuis le fichier."""
    if not TEMPLATE_PATH.exists():
        raise FileNotFoundError(f"Template non trouvé: {TEMPLATE_PATH}")
    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        return f.read()


def generate_text(template: str, numero_autorisation: str, telephone: str) -> str:
    """Remplace les variables dans le template."""
    return template.replace("{{NUMERO_AUTORISATION}}", numero_autorisation).replace(
        "{{TELEPHONE_RESPONSABLE}}", telephone
    )


def generate_qr_code(output_path: str = None) -> Image.Image:
    """Génère le QR-code pointant vers la page CNIL."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(CNIL_URL)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img = img.resize((QR_CODE_SIZE, QR_CODE_SIZE), Image.Resampling.LANCZOS)

    if output_path:
        img.save(output_path)

    return img


def create_affiche(
    text: str,
    qr_image: Image.Image,
    output_path: str,
    format: str = "PNG",
):
    """Crée l'affiche complète avec texte et QR-code."""
    img = Image.new("RGB", (AFFICHE_WIDTH, AFFICHE_HEIGHT), "white")
    draw = ImageDraw.Draw(img)

    try:
        font_title = ImageFont.truetype(f"{DEFAULT_FONT}.ttf", FONT_SIZE_TITLE)
        font_body = ImageFont.truetype(f"{DEFAULT_FONT}.ttf", FONT_SIZE_BODY)
        font_footer = ImageFont.truetype(f"{DEFAULT_FONT}.ttf", FONT_SIZE_FOOTER)
    except IOError:
        font_title = ImageFont.load_default()
        font_body = ImageFont.load_default()
        font_footer = ImageFont.load_default()

    lines = text.split("\n")
    y_position = MARGIN

    for i, line in enumerate(lines):
        font = font_title if i == 0 else font_body
        draw.text((MARGIN, y_position), line, fill="black", font=font)
        y_position += FONT_SIZE_BODY + 10

    qr_x = AFFICHE_WIDTH - QR_CODE_SIZE - QR_MARGIN
    qr_y = AFFICHE_HEIGHT - QR_CODE_SIZE - QR_MARGIN
    img.paste(qr_image, (qr_x, qr_y))

    footer_text = "Scannez pour connaître vos droits sur les images"
    draw.text(
        (qr_x, qr_y + QR_CODE_SIZE + 5),
        footer_text,
        fill="black",
        font=font_footer,
    )

    img.save(output_path, format=format.upper())
    print(f"Affiche générée: {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Générateur d'affiche réglementaire vidéoprotection"
    )
    parser.add_argument(
        "--autorisation",
        required=True,
        help="Numéro d'autorisation préfectorale (ex: 2024-12345)",
    )
    parser.add_argument(
        "--telephone",
        required=True,
        help="Numéro de téléphone du responsable sécurité (ex: 01 23 45 67 89)",
    )
    parser.add_argument(
        "--format",
        default="PNG",
        choices=["PNG", "SVG"],
        help="Format de sortie (PNG ou SVG)",
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Nom du fichier de sortie (sans extension)",
    )

    args = parser.parse_args()

    OUTPUT_DIR.mkdir(exist_ok=True)

    template = load_template()
    text = generate_text(template, args.autorisation, args.telephone)

    output_name = args.output or f"affiche_{args.autorisation}"
    qr_output = OUTPUT_DIR / f"qrcode_{args.autorisation}.png"

    qr_image = generate_qr_code(str(qr_output))

    affiche_output = OUTPUT_DIR / f"{output_name}.{args.format.lower()}"
    create_affiche(text, qr_image, str(affiche_output), args.format)


if __name__ == "__main__":
    main()