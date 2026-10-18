#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generar_logo.py — Arma el logo del menú con tus propios sprites.
Uso (desde herramientas/):  python generar_logo.py
Salida: ../game/images/Logo_Menu_v2.png
"""
import os
import math
import random
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageChops

JUEGO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "game")
SALIDA = os.path.join(JUEGO, "images", "Logo_Menu_v2.png")
FUENTE_TITULO = os.path.join(JUEGO, "fonts", "ShipporiMinchoB1-SemiBold.ttf")
FUENTE_JP = os.path.join(JUEGO, "fonts", "NotoSansJP-Regular.ttf")
FUENTE_SUB = os.path.join(JUEGO, "fonts", "MPLUSRounded1c-Bold.ttf")

HERMANAS = ["ichika", "nino", "miku", "yotsuba", "itsuki"]
COLORES = [(255, 183, 197), (195, 155, 211), (93, 173, 226), (88, 214, 141), (236, 112, 99)]
AZUL = (27, 22, 80)
ROSA = (255, 150, 190)
BLANCO = (255, 255, 255)
ANCHO, ALTO = 1400, 1000


def silueta(hermana, color):
    ruta = os.path.join(JUEGO, "images", "sprites", hermana + "_sprites", hermana + "_neutral.png")
    sprite = Image.open(ruta).convert("RGBA").crop((100, 0, 660, 430))
    w, h = sprite.size
    desvanecer = Image.new("L", (w, h), 255)
    px = desvanecer.load()
    for y in range(300, h):
        v = int(255 * (1 - (y - 300) / float(h - 300)))
        for x in range(w):
            px[x, y] = v
    alfa = ImageChops.multiply(sprite.getchannel("A"), desvanecer)
    forma = Image.new("RGBA", (w, h), color + (255,))
    forma.putalpha(alfa)
    borde = Image.new("RGBA", (w, h), BLANCO + (255,))
    borde.putalpha(alfa.filter(ImageFilter.MaxFilter(9)))
    return Image.alpha_composite(borde, forma)


def flor_pequena(d, cx, cy, r, color):
    for k in range(5):
        ang = k * 2 * math.pi / 5 - math.pi / 2
        px = cx + 0.55 * r * math.cos(ang)
        py = cy + 0.55 * r * math.sin(ang)
        d.ellipse((px - 0.5 * r, py - 0.5 * r, px + 0.5 * r, py + 0.5 * r), fill=color + (255,))


def capa_vacia():
    return Image.new("RGBA", (ANCHO, ALTO), (0, 0, 0, 0))


def componer():
    lienzo = capa_vacia()

    # "5" grande y pálido detrás
    c5 = capa_vacia()
    f5 = ImageFont.truetype(FUENTE_TITULO, 560)
    ImageDraw.Draw(c5).text((ANCHO // 2, 330), "5", font=f5, fill=ROSA + (150,), anchor="mm")
    lienzo = Image.alpha_composite(lienzo, c5)

    # aro rosa detrás de las siluetas
    aro = capa_vacia()
    ImageDraw.Draw(aro).ellipse((300, 40, 1100, 840), outline=ROSA + (200,), width=8)
    lienzo = Image.alpha_composite(lienzo, aro.filter(ImageFilter.GaussianBlur(0.8)))

    # las cinco siluetas (la del centro se dibuja al final, por delante)
    ancho_s = 330
    paso = 215
    x0 = (ANCHO - (ancho_s + paso * 4)) // 2
    for idx in [0, 4, 1, 3, 2]:
        s = silueta(HERMANAS[idx], COLORES[idx])
        s = s.resize((ancho_s, int(s.height * ancho_s / s.width)), Image.LANCZOS)
        lienzo.alpha_composite(s, (x0 + idx * paso, 170))

    # título con resplandor rosa
    titulo = "Fifth Choice"
    f_t = ImageFont.truetype(FUENTE_TITULO, 175)
    glow = capa_vacia()
    ImageDraw.Draw(glow).text((ANCHO // 2 + 30, 650), titulo, font=f_t, fill=ROSA + (255,),
                              anchor="mm", stroke_width=22, stroke_fill=ROSA + (255,))
    lienzo = Image.alpha_composite(lienzo, glow.filter(ImageFilter.GaussianBlur(12)))

    texto = capa_vacia()
    dt = ImageDraw.Draw(texto)
    dt.text((ANCHO // 2 + 30, 650), titulo, font=f_t, fill=AZUL + (255,),
            anchor="mm", stroke_width=10, stroke_fill=BLANCO + (255,))
    f_the = ImageFont.truetype(FUENTE_TITULO, 100)
    dt.text((ANCHO // 2 - 560, 550), "The", font=f_the, fill=AZUL + (255,),
            anchor="ls", stroke_width=7, stroke_fill=BLANCO + (255,))
    lienzo = Image.alpha_composite(lienzo, texto)

    # trazo curvo y cinco flores, una por hermana
    detalle = capa_vacia()
    dd = ImageDraw.Draw(detalle)
    dd.arc((250, 640, 1150, 920), start=25, end=155, fill=ROSA + (255,), width=10)
    for k in range(5):
        flor_pequena(dd, ANCHO // 2 + (k - 2) * 78, 842, 26, COLORES[k])
    lienzo = Image.alpha_composite(lienzo, detalle)

    # subtítulos
    sub = capa_vacia()
    ds = ImageDraw.Draw(sub)
    ds.text((ANCHO // 2, 925), "五等分の花嫁", font=ImageFont.truetype(FUENTE_JP, 40),
            fill=AZUL + (255,), anchor="mm")
    ds.text((ANCHO // 2, 972), "QUINTESSENTIAL QUINTUPLETS FAN GAME",
            font=ImageFont.truetype(FUENTE_SUB, 26), fill=AZUL + (255,), anchor="mm")
    lienzo = Image.alpha_composite(lienzo, sub)

    # pétalos sueltos
    azar = random.Random(7)
    pet = capa_vacia()
    dp = ImageDraw.Draw(pet)
    for _ in range(16):
        x = azar.randint(180, ANCHO - 180)
        y = azar.randint(60, 860)
        r = azar.randint(7, 14)
        dp.ellipse((x - r, y - r // 2, x + r, y + r // 2), fill=ROSA + (190,))
    return Image.alpha_composite(pet, lienzo)


if __name__ == "__main__":
    logo = componer()
    logo = logo.crop(logo.getbbox())
    logo.thumbnail((640, 640), Image.LANCZOS)
    logo.save(SALIDA)
    print("Guardado:", SALIDA, logo.size)