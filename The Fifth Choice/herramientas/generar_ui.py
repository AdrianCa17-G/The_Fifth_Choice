#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generar_ui.py — Genera los PNG de la interfaz en game/ui/.
Uso (desde la carpeta herramientas/):  python generar_ui.py
Requiere: pip install pillow
"""
import os
from PIL import Image, ImageDraw, ImageChops

SALIDA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "game", "ui")
SS = 4  # supersampling: se dibuja 4 veces más grande y se reduce (bordes suaves)

# Estos dos números tienen que coincidir con screens.rpy
CAJA_W, CAJA_H = 1340, 240

os.makedirs(SALIDA, exist_ok=True)


def guardar(img, nombre):
    ruta = os.path.join(SALIDA, nombre)
    img.save(ruta)
    print("Guardado:", ruta)


def mascara_redondeada(ancho, alto, radio):
    grande = Image.new("L", (ancho * SS, alto * SS), 0)
    d = ImageDraw.Draw(grande)
    d.rounded_rectangle((0, 0, ancho * SS - 1, alto * SS - 1),
                        radius=radio * SS, fill=255)
    return grande.resize((ancho, alto), Image.LANCZOS)


def borde_redondeado(ancho, alto, radio, color, grosor):
    grande = Image.new("RGBA", (ancho * SS, alto * SS), (0, 0, 0, 0))
    d = ImageDraw.Draw(grande)
    d.rounded_rectangle((0, 0, ancho * SS - 1, alto * SS - 1),
                        radius=radio * SS, outline=color, width=grosor * SS)
    return grande.resize((ancho, alto), Image.LANCZOS)


def degradado(ancho, alto, arriba, abajo):
    """Degradado vertical RGBA de color 'arriba' a color 'abajo'."""
    img = Image.new("RGBA", (ancho, alto))
    px = img.load()
    for y in range(alto):
        t = y / float(alto - 1)
        color = []
        for k in range(4):
            color.append(int(arriba[k] + (abajo[k] - arriba[k]) * t))
        color = tuple(color)
        for x in range(ancho):
            px[x, y] = color
    return img


def panel(ancho, alto, radio, arriba, abajo, color_borde=None, grosor=2):
    """Rectángulo redondeado con degradado, translúcido, con borde opcional."""
    img = degradado(ancho, alto, arriba, abajo)
    alfa = ImageChops.multiply(img.getchannel("A"),
                               mascara_redondeada(ancho, alto, radio))
    img.putalpha(alfa)
    if color_borde is not None:
        img = Image.alpha_composite(
            img, borde_redondeado(ancho, alto, radio, color_borde, grosor))
    return img


def petalo():
    """Un pétalo de sakura (con muesca) apuntando hacia arriba, en un lienzo
    de 160x160. El CENTRO del lienzo es el centro de la flor: así Ren'Py puede
    rotarlo 72 grados cinco veces y las cinco copias encajan."""
    g = Image.new("RGBA", (160 * SS, 160 * SS), (0, 0, 0, 0))
    d = ImageDraw.Draw(g)
    blanco = (255, 255, 255, 255)
    # cabeza redonda del pétalo
    d.ellipse(((80 - 26) * SS, (30 - 26) * SS, (80 + 26) * SS, (30 + 26) * SS),
              fill=blanco)
    # base en punta, hacia el centro de la flor
    d.polygon([(80 * SS, 80 * SS), (56 * SS, 36 * SS), (104 * SS, 36 * SS)],
              fill=blanco)
    # muesca de sakura en la punta
    d.polygon([(70 * SS, 0), (90 * SS, 0), (80 * SS, 17 * SS)],
              fill=(0, 0, 0, 0))
    return g.resize((160, 160), Image.LANCZOS)


def flor(petalo_img, tam):
    base = Image.new("RGBA", (160, 160), (0, 0, 0, 0))
    for i in range(5):
        giro = petalo_img.rotate(-72 * i, resample=Image.BICUBIC)
        base = Image.alpha_composite(base, giro)
    return base.resize((tam, tam), Image.LANCZOS)


def libreta():
    """Hoja de libreta: crema, margen rojo y tres agujeros de argolla."""
    img = panel(CAJA_W, CAJA_H, 40, (246, 238, 220, 242), (234, 223, 196, 242),
                (120, 90, 60, 110), 2)

    # margen rojo
    g = Image.new("RGBA", (CAJA_W * SS, CAJA_H * SS), (0, 0, 0, 0))
    d = ImageDraw.Draw(g)
    d.rectangle((118 * SS, 24 * SS, 121 * SS, (CAJA_H - 24) * SS),
                fill=(205, 85, 85, 210))
    g = g.resize((CAJA_W, CAJA_H), Image.LANCZOS)
    img = Image.alpha_composite(img, g)

    # agujeros: se borran del alfa para que se vea la escena detrás
    agujeros = Image.new("L", (CAJA_W * SS, CAJA_H * SS), 255)
    da = ImageDraw.Draw(agujeros)
    for y in (60, 120, 180):
        da.ellipse(((58 - 13) * SS, (y - 13) * SS, (58 + 13) * SS, (y + 13) * SS),
                   fill=0)
    agujeros = agujeros.resize((CAJA_W, CAJA_H), Image.LANCZOS)
    img.putalpha(ImageChops.multiply(img.getchannel("A"), agujeros))
    return img


if __name__ == "__main__":
    # Caja de diálogo: BLANCA con borde gris. Ren'Py la tiñe por personaje.
    guardar(panel(CAJA_W, CAJA_H, 40, (255, 255, 255, 228), (238, 238, 244, 228),
                  (140, 140, 150, 255), 3), "caja.png")

    # Caja del narrador: más transparente y casi sin borde
    guardar(panel(CAJA_W, CAJA_H, 40, (40, 28, 60, 175), (22, 14, 32, 175),
                  (255, 255, 255, 30), 2), "caja_narrador.png")

    guardar(libreta(), "libreta.png")

    # Placa de nombre: BLANCA, Ren'Py la tiñe con el color de cada personaje
    guardar(panel(300, 72, 36, (255, 255, 255, 255), (232, 226, 240, 255)),
            "placa.png")

    # Flor
    p = petalo()
    guardar(p, "petalo.png")
    guardar(flor(p, 56), "flor.png")

    # Botones de decisión
    guardar(panel(400, 100, 28, (52, 34, 78, 220), (27, 16, 38, 220),
                  (255, 255, 255, 60), 2), "opcion.png")
    guardar(panel(400, 100, 28, (70, 44, 104, 240), (40, 24, 60, 240),
                  (255, 183, 197, 255), 3), "opcion_hover.png")