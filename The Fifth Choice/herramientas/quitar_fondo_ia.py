#!/usr/bin/env python3
"""
quitar_fondo_ia.py — Quita el fondo de un render con IA (rembg, modelo de anime)
y devuelve un PNG con transparencia real, listo para normalizar_sprite.py.

Úsalo sobre el PNG ORIGINAL (no sobre versiones pasadas por Gemini ni JPG/JFIF:
la compresión JPEG ensucia los bordes).

Instalación (una sola vez; la primera ejecución descarga el modelo, ~170 MB,
y necesita internet):
    pip install "rembg[cpu]" pillow numpy scipy

Uso:
    python quitar_fondo_ia.py original.png sin_fondo.png
    python quitar_fondo_ia.py original.png sin_fondo.png --modelo isnet-general-use
    python quitar_fondo_ia.py original.png sin_fondo.png --sin-matting
    python quitar_fondo_ia.py original.png sin_fondo.png --normalizar

Flujo recomendado:
    quitar_fondo_ia.py  ->  normalizar_sprite.py  ->  limpiar_halo.py --solo-halo
    (o usa --normalizar para encadenar el paso 2 automáticamente)

Qué hace además de llamar a rembg:
  - Alpha matting opcional (activado por defecto): bordes más finos en pelo y
    cintas. Si falla o tarda demasiado, usa --sin-matting.
  - Desmatteado del borde: el color de los píxeles semitransparentes sale
    mezclado con el fondo original; se despeja igual que en limpiar_halo.py
    (solo alpha >= 0,28).
  - Descarta motas sueltas de alpha muy bajo y componentes diminutas.
"""

import sys
import argparse
import subprocess
import os
import numpy as np
from PIL import Image
from scipy import ndimage

ALPHA_EXCLUDE = 0.28 * 255
ALPHA_FLOOR = 10          # por debajo de esto el alpha se manda a 0 (ruido)
MIN_COMPONENT = 30        # px; componentes opacas más chicas se borran


def postprocesar(original_rgb, alpha, desmatte=True):
    """
    original_rgb: array HxWx3 uint8 del render ORIGINAL (con su fondo).
    alpha: array HxW uint8 devuelto por rembg.
    Devuelve RGBA uint8.
    """
    alpha = alpha.copy()
    alpha[alpha < ALPHA_FLOOR] = 0

    # Borrar islas diminutas (restos de fondo que la IA dejó sueltos)
    solid = alpha > 0
    lab, n = ndimage.label(solid)
    if n > 1:
        sizes = ndimage.sum(solid, lab, range(1, n + 1))
        keep = [i + 1 for i, s in enumerate(sizes) if s >= MIN_COMPONENT]
        alpha[~np.isin(lab, keep)] = 0

    rgb = original_rgb.astype(np.float64)

    if desmatte:
        a = alpha.astype(np.float64) / 255.0
        mask = alpha >= ALPHA_EXCLUDE
        with np.errstate(divide="ignore", invalid="ignore"):
            corrected = (rgb - (1 - a[..., None]) * 255.0) / a[..., None]
        rgb[mask] = corrected[mask]
        rgb = np.clip(rgb, 0, 255)

    return np.dstack([rgb, alpha]).astype(np.uint8)


def quitar_con_rembg(img_rgb, modelo, matting):
    try:
        from rembg import remove, new_session
    except ImportError:
        sys.exit(
            "No está instalado rembg. Ejecuta primero:\n"
            '    pip install "rembg[cpu]"\n'
            "(la primera vez descarga el modelo, necesita internet)."
        )

    session = new_session(modelo)
    kwargs = {}
    if matting:
        kwargs = dict(
            alpha_matting=True,
            alpha_matting_foreground_threshold=240,
            alpha_matting_background_threshold=10,
            alpha_matting_erode_size=10,
        )
    try:
        out = remove(img_rgb, session=session, **kwargs)
    except Exception as e:  # matting puede fallar (pymatting) en imágenes raras
        if matting:
            print(f"Aviso: alpha matting falló ({e}); reintento sin matting.")
            out = remove(img_rgb, session=session)
        else:
            raise
    return np.array(out.convert("RGBA"))[..., 3]


def main():
    p = argparse.ArgumentParser(description="Quita el fondo de un sprite con rembg (modelo de anime).")
    p.add_argument("entrada")
    p.add_argument("salida")
    p.add_argument("--modelo", default="isnet-anime",
                   help="Modelo de rembg (default isnet-anime; alternativa: isnet-general-use, u2net).")
    p.add_argument("--sin-matting", action="store_true", help="Desactiva el alpha matting.")
    p.add_argument("--sin-desmatte", action="store_true", help="No corrige el color del borde.")
    p.add_argument("--normalizar", action="store_true",
                   help="Al terminar, corre normalizar_sprite.py (debe estar en la misma carpeta) "
                        "sobre el resultado. Se guarda como <salida>_norm.png. "
                        "Pasa opciones extra con --args-normalizar.")
    p.add_argument("--args-normalizar", default="",
                   help='Opciones para normalizar_sprite.py entre comillas, p.ej. "--ojos 100,200,180,200".')
    a = p.parse_args()

    img = Image.open(a.entrada).convert("RGB")  # acepta PNG, JPG, JFIF...
    alpha = quitar_con_rembg(img, a.modelo, not a.sin_matting)
    rgba = postprocesar(np.array(img), alpha, desmatte=not a.sin_desmatte)

    Image.fromarray(rgba, mode="RGBA").save(a.salida)
    pct = 100 * (rgba[..., 3] == 0).mean()
    print(f"Fondo transparente: {pct:.1f}% de la imagen. Guardado: {a.salida}")

    if a.normalizar:
        base = os.path.splitext(a.salida)[0]
        destino = base + "_norm.png"
        script = os.path.join(os.path.dirname(os.path.abspath(__file__)), "normalizar_sprite.py")
        if not os.path.exists(script):
            sys.exit("No encuentro normalizar_sprite.py junto a este script.")
        cmd = [sys.executable, script, a.salida, destino] + a.args_normalizar.split()
        print("Normalizando:", " ".join(cmd))
        subprocess.run(cmd, check=True)


if __name__ == "__main__":
    main()
