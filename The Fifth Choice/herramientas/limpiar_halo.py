#!/usr/bin/env python3
"""
limpiar_halo.py — Limpia un sprite YA NORMALIZADO (salida de normalizar_sprite.py
o normalizar_extra.py): desmatteado del contorno + borrado de huecos blancos
encerrados. Ver GUIA_ARTE.md, secciones 4 y 5.

Qué hace cada parte:
  1. Desmatteado del halo del contorno. Un recorte binario deja los píxeles del
     borde con el blanco del fondo mezclado dentro del color (C = a*C_real +
     (1-a)*255); se despeja C_real. Se excluyen los alpha < 0,28, donde la
     división amplifica ruido. No hace falta filtrar por color: si el píxel es
     blanco de verdad, quitarle el blanco devuelve blanco.
  2. Borrado de huecos blancos encerrados DENTRO del propio sprite (dedos,
     cuello, etc.), con el mismo discriminante que normalizar_sprite.py:
     pureza media >= 253,5 Y calidez del contorno (r-b, excluyendo lineart por
     luminancia > 70) >= 20. Área mínima 40 px.

--solo-halo: hace solo el paso 1. Es el caso de Yotsuba (paleta amarillo/
naranja/verde: su cuello blanco mide cálido igual que el pelo y el paso 2 le
come una tira) y, en general, sirve para cuando los huecos encerrados ya se
limpiaron a mano y solo falta el contorno.

Uso:
  python limpiar_halo.py entrada.png salida.png
  python limpiar_halo.py entrada.png salida.png --solo-halo

Requiere Pillow, numpy y scipy.
"""

import sys
import argparse
import numpy as np
from PIL import Image
from scipy import ndimage

ALPHA_EXCLUDE = 0.28 * 255  # por debajo de esto no se desmatea (ruido)
HOLE_MIN_AREA = 40
HOLE_PURITY_MIN = 253.5
HOLE_WARMTH_MIN = 20
HOLE_ALPHA_MIN = 200  # solo se consideran huecos los píxeles ya opacos


def desmatte(rgba_arr):
    """
    Despeja C_real = (C - (1-a)*255) / a para alpha >= 0,28 (0,28*255 ~= 71,4).
    Deja intactos alpha=0 y los píxeles por debajo del umbral.
    """
    arr = rgba_arr.astype(np.float64)
    rgb = arr[..., :3]
    alpha = arr[..., 3]
    a_frac = alpha / 255.0

    mask = alpha >= ALPHA_EXCLUDE
    out_rgb = rgb.copy()

    with np.errstate(divide="ignore", invalid="ignore"):
        corrected = (rgb - (1 - a_frac[..., None]) * 255.0) / a_frac[..., None]

    out_rgb[mask] = corrected[mask]
    out_rgb = np.clip(out_rgb, 0, 255)

    return np.dstack([out_rgb, alpha]).astype(np.uint8)


def remove_enclosed_holes(rgba_arr):
    """
    Mismo discriminante que normalizar_sprite.py, aplicado a huecos blancos
    OPACOS dentro del sprite (el fondo ya es transparente, no hace falta
    distinguirlo por contacto con el borde del lienzo).
    """
    arr = rgba_arr.copy()
    rgb = arr[..., :3].astype(np.int16)
    alpha = arr[..., 3]

    whiteness = rgb.min(axis=2)
    is_white_opaque = (whiteness > 240) & (alpha > HOLE_ALPHA_MIN)

    labeled, n = ndimage.label(is_white_opaque)
    if n == 0:
        return arr

    for lbl in range(1, n + 1):
        mask = labeled == lbl
        area = mask.sum()
        if area < HOLE_MIN_AREA:
            continue

        purity = rgb[mask].min(axis=1).mean()
        if purity < HOLE_PURITY_MIN:
            continue

        ring = ndimage.binary_dilation(mask, iterations=2) & ~mask & (alpha > HOLE_ALPHA_MIN)
        if ring.sum() == 0:
            continue

        ring_pixels = rgb[ring]
        luminance = ring_pixels.mean(axis=1)
        colored = ring_pixels[luminance > 70]
        if len(colored) == 0:
            continue

        warmth = colored[:, 0].mean() - colored[:, 2].mean()
        if warmth >= HOLE_WARMTH_MIN:
            alpha[mask] = 0

    return np.dstack([arr[..., :3], alpha])


def main():
    parser = argparse.ArgumentParser(
        description="Limpia el halo de contorno (y opcionalmente los huecos "
                     "encerrados) de un sprite YA normalizado."
    )
    parser.add_argument("entrada")
    parser.add_argument("salida")
    parser.add_argument(
        "--solo-halo", action="store_true",
        help="Solo desmatea el contorno, no toca huecos encerrados "
             "(caso Yotsuba, o cuando ya los limpiaste a mano)."
    )
    args = parser.parse_args()

    img = Image.open(args.entrada).convert("RGBA")
    arr = np.array(img)

    before_semitransparent = int(
        ((arr[..., 3] > 0) & (arr[..., 3] < 255)).sum()
    )

    arr = desmatte(arr)

    if not args.solo_halo:
        before_holes_alpha = int((arr[..., 3] > HOLE_ALPHA_MIN).sum())
        arr = remove_enclosed_holes(arr)
        after_holes_alpha = int((arr[..., 3] > HOLE_ALPHA_MIN).sum())
        print(f"Huecos: {before_holes_alpha - after_holes_alpha} px borrados.")
    else:
        print("--solo-halo: no se tocan huecos encerrados.")

    print(f"Contorno: {before_semitransparent} px semitransparentes desmateados.")

    Image.fromarray(arr, mode="RGBA").save(args.salida)
    print(f"Guardado: {args.salida}")


if __name__ == "__main__":
    main()
