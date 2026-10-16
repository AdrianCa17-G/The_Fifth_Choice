#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generar_ui.py — Genera los PNG de la interfaz en game/ui/.
Uso (desde la carpeta herramientas/):  python generar_ui.py
Requiere: pip install pillow
"""
import os
import math
import random
from PIL import Image, ImageDraw, ImageChops

SALIDA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "game", "ui")
SS = 4  # supersampling: se dibuja 4 veces más grande y se reduce (bordes suaves)

# Estos dos números tienen que coincidir con screens.rpy
CAJA_W, CAJA_H = 1340, 240

# --- Ajustes de la decoración ---
ALFA_BORDE = 100                       # franjas de los bordes (0-255)
ALFA_RELLENO = 34                      # patrón tenue de fondo (0 lo apaga)
X_ARRIBA_INI = 380                     # la fila de arriba empieza después de la placa
TARJETA_ALTOS = [220, 270, 320, 370]   # tiene que coincidir con 07_ui.rpy

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


BLANCO_SUAVE = (255, 255, 255, 95)


def girar(puntos, ang):
    c = math.cos(ang)
    s = math.sin(ang)
    resultado = []
    for (x, y) in puntos:
        resultado.append((x * c - y * s, x * s + y * c))
    return resultado


def mover(puntos, cx, cy):
    resultado = []
    for (x, y) in puntos:
        resultado.append((cx + x, cy + y))
    return resultado


def motivo_estrella(d, cx, cy, r, color, puntas, interior):
    pts = []
    for k in range(puntas * 2):
        radio = r
        if k % 2 == 1:
            radio = r * interior
        ang = -math.pi / 2 + k * math.pi / puntas
        pts.append((cx + radio * math.cos(ang), cy + radio * math.sin(ang)))
    d.polygon(pts, fill=color)


def motivo_estrella5(d, cx, cy, r, color):
    motivo_estrella(d, cx, cy, r, color, 5, 0.45)


def motivo_destello(d, cx, cy, r, color):
    motivo_estrella(d, cx, cy, r, color, 4, 0.22)


def motivo_mariposa(d, cx, cy, r, color):
    for lado in (-1, 1):
        x0 = cx + lado * 0.55 * r
        y0 = cy - 0.25 * r
        d.ellipse((x0 - 0.55 * r, y0 - 0.5 * r, x0 + 0.55 * r, y0 + 0.5 * r), fill=color)
        x1 = cx + lado * 0.4 * r
        y1 = cy + 0.4 * r
        d.ellipse((x1 - 0.35 * r, y1 - 0.32 * r, x1 + 0.35 * r, y1 + 0.32 * r), fill=color)
    # el cuerpo: un hueco fino que separa las dos alas
    d.line((cx, cy - 0.6 * r, cx, cy + 0.7 * r), fill=(255, 255, 255, 0),
           width=max(2, int(r * 0.12)))


def motivo_trebol(d, cx, cy, r, color):
    hoja = []
    for k in range(40):
        t = 2 * math.pi * k / 40
        x = 16 * math.sin(t) ** 3
        y = -(13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t))
        hoja.append((x * r / 30.0, (y - 17) * r / 30.0))
    for k in range(4):
        d.polygon(mover(girar(hoja, k * math.pi / 2), cx, cy), fill=color)
    d.line((cx, cy, cx + 0.35 * r, cy + 1.2 * r), fill=color, width=max(2, int(r * 0.12)))


def motivo_ecualizador(d, cx, cy, r, color):
    alturas = [0.5, 0.9, 0.65, 1.0, 0.55]
    ancho = 0.24 * r
    hueco = 0.12 * r
    total = 5 * ancho + 4 * hueco
    x = cx - total / 2
    for h in alturas:
        alto = 1.6 * r * h
        d.rounded_rectangle((x, cy - alto / 2, x + ancho, cy + alto / 2),
                            radius=int(ancho / 2), fill=color)
        x = x + ancho + hueco

def dibujar_fila(d, motivo, azar, x_ini, x_fin, y, paso, rmin, rmax, alfa):
    x = x_ini
    while x < x_fin:
        cx = x + azar.randint(-10, 10)
        cy = y + azar.randint(-4, 4)
        r = azar.randint(rmin, rmax)
        motivo(d, cx * SS, cy * SS, r * SS, (255, 255, 255, alfa))
        x = x + paso


def dibujar_columna(d, motivo, azar, x, y_ini, y_fin, paso, rmin, rmax, alfa):
    y = y_ini
    while y < y_fin:
        cx = x + azar.randint(-3, 3)
        cy = y + azar.randint(-6, 6)
        r = azar.randint(rmin, rmax)
        motivo(d, cx * SS, cy * SS, r * SS, (255, 255, 255, alfa))
        y = y + paso


def dibujar_relleno(d, motivo, azar, x0, y0, x1, y1, paso_x, paso_y, alfa):
    """Cuadrícula escalonada de motivos pequeños y muy tenues."""
    fila = 0
    y = y0
    while y <= y1:
        x = x0
        if fila % 2 == 1:
            x = x0 + paso_x // 2
        while x <= x1:
            r = azar.randint(8, 12)
            cx = x + azar.randint(-6, 6)
            cy = y + azar.randint(-5, 5)
            motivo(d, cx * SS, cy * SS, r * SS, (255, 255, 255, alfa))
            x = x + paso_x
        y = y + paso_y
        fila = fila + 1


def recortar_redondeado(g, ancho, alto, radio):
    img = g.resize((ancho, alto), Image.LANCZOS)
    alfa = ImageChops.multiply(img.getchannel("A"),
                               mascara_redondeada(ancho, alto, radio))
    img.putalpha(alfa)
    return img


def decoracion_caja(motivo, semilla):
    """Decoración de la caja de diálogo: relleno tenue + franjas en los bordes."""
    azar = random.Random(semilla)
    g = Image.new("RGBA", (CAJA_W * SS, CAJA_H * SS), (255, 255, 255, 0))
    d = ImageDraw.Draw(g)

    if ALFA_RELLENO > 0:
        dibujar_relleno(d, motivo, azar, 100, 58, 1120, 200, 96, 52, ALFA_RELLENO)

    dibujar_fila(d, motivo, azar, X_ARRIBA_INI, CAJA_W - 30, 24, 150, 13, 20, ALFA_BORDE)
    dibujar_fila(d, motivo, azar, 90, CAJA_W - 30, CAJA_H - 24, 150, 13, 20, ALFA_BORDE)
    dibujar_columna(d, motivo, azar, 34, 74, CAJA_H - 40, 38, 11, 15, ALFA_BORDE)
    return recortar_redondeado(g, CAJA_W, CAJA_H, 40)


def decoracion_tarjeta(motivo, semilla, alto):
    azar = random.Random(semilla)
    g = Image.new("RGBA", (520 * SS, alto * SS), (255, 255, 255, 0))
    d = ImageDraw.Draw(g)

    if ALFA_RELLENO > 0:
        dibujar_relleno(d, motivo, azar, 50, 62, 470, alto - 62, 80, 50, ALFA_RELLENO)

    dibujar_fila(d, motivo, azar, 56, 500, 24, 110, 11, 16, ALFA_BORDE)
    dibujar_fila(d, motivo, azar, 56, 500, alto - 24, 110, 11, 16, ALFA_BORDE)
    return recortar_redondeado(g, 520, alto, 36)


def tarjeta_base(alto):
    """Panel NEUTRO (gris). Ren'Py lo tiñe con el tono oscuro de cada hermana."""
    return panel(520, alto, 36, (255, 255, 255, 238), (150, 150, 150, 238),
                 (255, 255, 255, 50), 2)


def marco(alto):
    """Solo el borde, blanco: Ren'Py lo tiñe con el color de la hermana."""
    return borde_redondeado(520, alto, 36, (255, 255, 255, 255), 4)


def halo(alto):
    """Resplandor que sube desde abajo (cálido o frío según la opción)."""
    img = Image.new("RGBA", (520, alto), (255, 255, 255, 0))
    px = img.load()
    for y in range(alto):
        t = y / float(alto - 1)
        a = int(255 * (max(0.0, (t - 0.45) / 0.55) ** 2))
        for x in range(520):
            px[x, y] = (255, 255, 255, a)
    alfa = ImageChops.multiply(img.getchannel("A"), mascara_redondeada(520, alto, 36))
    img.putalpha(alfa)
    return img


# --- Iconos del menú rápido ---------------------------------------------------
ICONO = 68
BLANCO = (255, 255, 255, 255)


def E(x, y):
    return (x * SS, y * SS)


def ER(x0, y0, x1, y1):
    return (x0 * SS, y0 * SS, x1 * SS, y1 * SS)


def nuevo_glifo():
    g = Image.new("RGBA", (ICONO * SS, ICONO * SS), (0, 0, 0, 0))
    return g, ImageDraw.Draw(g)


def fin_glifo(g):
    return g.resize((ICONO, ICONO), Image.LANCZOS)


def icono_base():
    return panel(ICONO, ICONO, 20, (255, 255, 255, 255), (228, 228, 238, 255))


def icono_borde():
    return borde_redondeado(ICONO, ICONO, 20, (255, 255, 255, 255), 3)


def glifo_atras():
    g, d = nuevo_glifo()
    d.polygon([E(14, 34), E(36, 15), E(36, 53)], fill=BLANCO)
    d.rounded_rectangle(ER(31, 28, 54, 40), radius=4 * SS, fill=BLANCO)
    return fin_glifo(g)


def glifo_historial():
    g, d = nuevo_glifo()
    for y in (21, 34, 47):
        d.ellipse(ER(13, y - 3, 19, y + 3), fill=BLANCO)
        d.rounded_rectangle(ER(24, y - 3, 55, y + 3), radius=3 * SS, fill=BLANCO)
    return fin_glifo(g)


def glifo_auto():
    g, d = nuevo_glifo()
    d.polygon([E(22, 16), E(54, 34), E(22, 52)], fill=BLANCO)
    return fin_glifo(g)


def glifo_saltar():
    g, d = nuevo_glifo()
    d.polygon([E(12, 18), E(31, 34), E(12, 50)], fill=BLANCO)
    d.polygon([E(31, 18), E(50, 34), E(31, 50)], fill=BLANCO)
    d.rounded_rectangle(ER(52, 18, 57, 50), radius=2 * SS, fill=BLANCO)
    return fin_glifo(g)


def glifo_guardar():
    g, d = nuevo_glifo()
    d.rounded_rectangle(ER(30, 13, 38, 33), radius=2 * SS, fill=BLANCO)
    d.polygon([E(19, 31), E(49, 31), E(34, 46)], fill=BLANCO)
    d.rounded_rectangle(ER(15, 50, 53, 56), radius=3 * SS, fill=BLANCO)
    return fin_glifo(g)


def glifo_menu():
    base = Image.new("RGBA", (ICONO, ICONO), (0, 0, 0, 0))
    f = flor(petalo(), 46)
    base.paste(f, ((ICONO - 46) // 2, (ICONO - 46) // 2), f)
    return base


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

    p = petalo()
    guardar(p, "petalo.png")
    guardar(flor(p, 56), "flor.png")

    # Botones de decisión ligeras
    guardar(panel(400, 100, 28, (52, 34, 78, 220), (27, 16, 38, 220),
                  (255, 255, 255, 60), 2), "opcion.png")
    guardar(panel(400, 100, 28, (70, 44, 104, 240), (40, 24, 60, 240),
                  (255, 183, 197, 255), 3), "opcion_hover.png")

    # Decoración por hermana: caja de diálogo y tarjetas (una por altura)
    HERMANAS = [
        ("ichika", motivo_destello, 1),
        ("nino", motivo_mariposa, 2),
        ("miku", motivo_ecualizador, 3),
        ("yotsuba", motivo_trebol, 4),
        ("itsuki", motivo_estrella5, 5),
    ]
    for nombre, motivo, semilla in HERMANAS:
        guardar(decoracion_caja(motivo, semilla), "deco_" + nombre + ".png")
        for alto in TARJETA_ALTOS:
            guardar(decoracion_tarjeta(motivo, semilla, alto),
                    "deco_tarjeta_" + nombre + "_" + str(alto) + ".png")

    # Tarjetas de decisión con peso: una versión por altura
    for alto in TARJETA_ALTOS:
        guardar(tarjeta_base(alto), "tarjeta_" + str(alto) + ".png")
        guardar(marco(alto), "tarjeta_marco_" + str(alto) + ".png")
        guardar(halo(alto), "halo_" + str(alto) + ".png")

    # Iconos del menú rápido
    guardar(icono_base(), "ico_base.png")
    guardar(icono_borde(), "ico_borde.png")
    guardar(glifo_atras(), "ico_atras.png")
    guardar(glifo_historial(), "ico_historial.png")
    guardar(glifo_auto(), "ico_auto.png")
    guardar(glifo_saltar(), "ico_saltar.png")
    guardar(glifo_guardar(), "ico_guardar.png")
    guardar(glifo_menu(), "ico_menu.png")