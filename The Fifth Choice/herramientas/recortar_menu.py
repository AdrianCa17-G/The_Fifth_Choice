#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
recortar_menu.py — Prepara un sprite del menú: quita el fondo blanco y recorta
al contenido (cabeza arriba, zapatos abajo).
Uso:  python recortar_menu.py entrada.png ../game/images/menu/ichika_menu.png
      (para Yotsuba añade --sin-huecos, por su cuello blanco)
"""
import sys
import numpy as np
from PIL import Image
from normalizar_extra import remove_background, remove_enclosed_holes


def main():
    if len(sys.argv) < 3:
        sys.exit("Uso: python recortar_menu.py entrada.png salida.png [--sin-huecos]")
    img = Image.open(sys.argv[1]).convert("RGBA")
    rgb, alpha, labeled, border = remove_background(img, suave=True)
    if "--sin-huecos" not in sys.argv:
        alpha = remove_enclosed_holes(rgb, alpha, labeled, border)
    filas = np.where(alpha.max(axis=1) > 8)[0]
    cols = np.where(alpha.max(axis=0) > 8)[0]
    if len(filas) == 0:
        sys.exit("No quedó nada opaco tras quitar el fondo.")
    caja = (int(cols[0]), int(filas[0]), int(cols[-1]) + 1, int(filas[-1]) + 1)
    salida = Image.fromarray(np.dstack([rgb, alpha])).crop(caja)
    salida.save(sys.argv[2])
    print("Guardado:", sys.argv[2], salida.size)


if __name__ == "__main__":
    main()