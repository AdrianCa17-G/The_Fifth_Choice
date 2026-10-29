#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generar_fondos_collage.py — Fondos del collage de pensamientos (beat casa).

Cada hermana tiene un muro de pétalos de su color (a la manera del arte de las
cinco con pétalos de colores) y, repartidos por encima, su motivo: destello
(Ichika), mariposa (Nino), ecualizador (Miku), trébol (Yotsuba) y estrella
(Itsuki). Los pétalos que caen en el juego los pone Ren'Py encima.

Uso (desde la carpeta herramientas/):  python generar_fondos_collage.py
Salida: ../game/ui/collage_fondo_<hermana>.webp  (1920x1080)
Requiere: generar_ui.py en la misma carpeta, y pillow.
"""
import os
import random

from PIL import Image, ImageDraw, ImageFilter

from generar_ui import (
    SALIDA, COLORES_HERMANAS,
    motivo_destello, motivo_mariposa, motivo_ecualizador,
    motivo_trebol, motivo_estrella5,
)

ANCHO, ALTO = 1920, 1080

## --- Ajustes ---------------------------------------------------------------
N_PETALOS = 1000                    # más = muro más tupido
ALTOS_PETALO = [70, 95, 125, 160, 200]   # tamaños posibles (alto en px)
N_MOTIVOS = 26                      # motivos de la hermana repartidos
DISTANCIA_MOTIVOS = 200             # separación mínima entre motivos
ALFA_MOTIVO = 160                   # 0-255, opacidad del motivo (blanco)
OSCURECER = 0.10                    # velo negro general (0 = nada)
CALIDAD = 90                        # calidad WebP

HERMANAS = [
    ("ichika", motivo_destello),
    ("nino", motivo_mariposa),
    ("miku", motivo_ecualizador),
    ("yotsuba", motivo_trebol),
    ("itsuki", motivo_estrella5),
]


def mezclar(color, objetivo, t):
    """Mezcla dos colores RGB. t=0 devuelve color, t=1 devuelve objetivo."""
    r = []
    for i in range(3):
        r.append(int(color[i] + (objetivo[i] - color[i]) * t))
    return tuple(r)


def forma_petalo(alto, ss=4):
    """Pétalo de sakura con muesca, blanco sobre transparente, de `alto` px.
    Es la misma geometría de petalo() en generar_ui.py, pero dibujada al
    tamaño pedido para que no se vea borroso al ampliarla."""
    s = ss * alto / 76.0            # el original mide 76 px de alto (y 4 a 80)
    lado = int(160 * s)
    g = Image.new("RGBA", (lado, lado), (0, 0, 0, 0))
    d = ImageDraw.Draw(g)
    blanco = (255, 255, 255, 255)
    d.ellipse(((80 - 26) * s, (30 - 26) * s, (80 + 26) * s, (30 + 26) * s), fill=blanco)
    d.polygon([(80 * s, 80 * s), (56 * s, 36 * s), (104 * s, 36 * s)], fill=blanco)
    d.polygon([(70 * s, 0), (90 * s, 0), (80 * s, 17 * s)], fill=(0, 0, 0, 0))
    g = g.crop(g.getbbox())
    return g.resize((max(1, g.width // ss), max(1, g.height // ss)), Image.LANCZOS)


def sello_motivo(motivo, r, angulo, ss=4):
    """Un motivo blanco de radio r, girado `angulo` grados, sobre transparente."""
    lado = int(r * 3)
    g = Image.new("RGBA", (lado * ss, lado * ss), (0, 0, 0, 0))
    d = ImageDraw.Draw(g)
    motivo(d, lado * ss / 2.0, lado * ss / 2.0, r * ss, (255, 255, 255, 255))
    g = g.resize((lado, lado), Image.LANCZOS)
    return g.rotate(angulo, resample=Image.BICUBIC)


def pegar(lienzo, forma, rgb, x, y, alfa=255):
    """Pega `forma` (blanca con alfa) teñida de `rgb` en (x, y). Admite
    coordenadas negativas o fuera del lienzo."""
    mascara = forma.getchannel("A")
    if alfa < 255:
        mascara = mascara.point(lambda v: v * alfa // 255)
    solido = Image.new("RGB", forma.size, rgb)
    lienzo.paste(solido, (x, y), mascara)


def fondo(color, motivo, semilla):
    azar = random.Random(semilla)
    base = mezclar(color, (0, 0, 0), 0.45)
    lienzo = Image.new("RGB", (ANCHO, ALTO), base)

    ## Una forma por tamaño, y se gira una copia para cada pétalo.
    formas = {}
    for alto in ALTOS_PETALO:
        formas[alto] = forma_petalo(alto)

    ## Muro de pétalos: tonos claros y oscuros del mismo color.
    for i in range(N_PETALOS):
        alto = azar.choice(ALTOS_PETALO)
        if azar.random() < 0.6:
            tono = mezclar(color, (255, 255, 255), azar.uniform(0.0, 0.40))
        else:
            tono = mezclar(color, (0, 0, 0), azar.uniform(0.05, 0.30))
        giro = formas[alto].rotate(azar.uniform(0, 360), resample=Image.BICUBIC, expand=True)
        x = azar.randint(-giro.width // 2, ANCHO - giro.width // 2)
        y = azar.randint(-giro.height // 2, ALTO - giro.height // 2)
        pegar(lienzo, giro, tono, x, y)

    ## Velo oscuro: baja el brillo para que polaroids y sprite destaquen.
    if OSCURECER > 0:
        velo = Image.new("RGB", (ANCHO, ALTO), (0, 0, 0))
        lienzo = Image.blend(lienzo, velo, OSCURECER)

    ## Motivos de la hermana, repartidos sin amontonarse.
    puestos = []
    intentos = 0
    while len(puestos) < N_MOTIVOS and intentos < 4000:
        intentos += 1
        cx = azar.randint(40, ANCHO - 40)
        cy = azar.randint(40, ALTO - 40)
        lejos = True
        for (px, py) in puestos:
            if (px - cx) ** 2 + (py - cy) ** 2 < DISTANCIA_MOTIVOS ** 2:
                lejos = False
                break
        if not lejos:
            continue
        puestos.append((cx, cy))
        r = azar.randint(30, 52)
        sello = sello_motivo(motivo, r, azar.uniform(-25, 25))
        pegar(lienzo, sello, (255, 255, 255), cx - sello.width // 2, cy - sello.height // 2, ALFA_MOTIVO)

    ## Un toque de desenfoque para que no compita con los polaroids.
    return lienzo.filter(ImageFilter.GaussianBlur(1.2))


if __name__ == "__main__":
    os.makedirs(SALIDA, exist_ok=True)
    for k in range(len(HERMANAS)):
        nombre, motivo = HERMANAS[k]
        img = fondo(COLORES_HERMANAS[k], motivo, 100 + k)
        ruta = os.path.join(SALIDA, "collage_fondo_" + nombre + ".webp")
        img.save(ruta, "WEBP", quality=CALIDAD, method=6)
        print("Guardado:", ruta, round(os.path.getsize(ruta) / 1024), "KB")
