#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
normalizar_chibi.py — Normaliza los chibis de los minijuegos del Evento 6.

Qué hace, por hermana:
  1. Quita el fondo blanco liso del render (o respeta el alfa si ya viene
     recortado con quitar_fondo_ia.py).
  2. Borra motas sueltas y mide la caja del contenido de cada expresión.
  3. Calcula UNA escala común para todas las expresiones de esa hermana, de modo
     que `neutral`, `animo`, `esfuerzo`, `triste` y `feliz` midan lo mismo y el
     cambio de expresión no se vea como un salto de tamaño.
  4. Coloca cada chibi en un lienzo de 512x512 RGBA: pies en la fila 496 y eje
     horizontal en el centro (columna 256).

La escala común sale de la expresión `neutral` (por defecto mide 420 px de alto)
pero nunca sube tanto como para cortar la expresión más alta (`feliz` con los
brazos arriba) ni la más ancha. Si el tope lo pone otra expresión, el informe lo
dice y propone el valor de --alto-neutral que evita la reducción.

Los nombres de entrada tienen que ser  <hermana>_<expresion>.png  (o .jpg/.webp):
    ichika_neutral.png   nino_animo.png   miku_esfuerzo.png
    yotsuba_triste.png   itsuki_feliz.png itsuki_mano.png
Los de salida se llaman igual y van a game/images/chibis/.

Uso (desde herramientas/):
    python normalizar_chibi.py renders_crudos/chibis/ ../game/images/chibis/
    python normalizar_chibi.py renders_crudos/chibis/ ../game/images/chibis/ --hermana nino
    python normalizar_chibi.py renders_crudos/chibis/ ../game/images/chibis/ --hermana yotsuba --sin-huecos
    python normalizar_chibi.py renders_crudos/chibis/ ../game/images/chibis/ --simular
    python normalizar_chibi.py renders_crudos/chibis/ ../game/images/chibis/ --alto-neutral 400
    python normalizar_chibi.py renders_crudos/chibis/ ../game/images/chibis/ --eje masa

Importante: procesa SIEMPRE las cinco expresiones de una hermana a la vez (misma
carpeta). Si pasas un solo archivo hay que dar --escala a mano, o el tamaño no
coincidirá con el resto del set.

Requiere Pillow, numpy y scipy, y normalizar_extra.py en la misma carpeta
(de ahí se reutilizan el recorte de fondo y el escalado con alfa premultiplicado).
"""

import sys
import argparse
from pathlib import Path

import numpy as np
from PIL import Image
from scipy import ndimage

from normalizar_extra import remove_background, remove_enclosed_holes, resize_premultiplied

LIENZO = 512
PIES = 496               # fila donde queda la planta de los pies
MARGEN_SUP = 8           # aire mínimo sobre la cabeza o las manos levantadas
MARGEN_LADO = 8          # aire mínimo a cada lado
ALTO_NEUTRAL = 420       # alto por defecto del chibi neutral, en px del lienzo
UMBRAL_ALFA = 8
MIN_COMPONENTE = 30      # px; las motas opacas más chicas se borran

HERMANAS = ["ichika", "nino", "miku", "yotsuba", "itsuki"]
EXPRESIONES = ["neutral", "animo", "esfuerzo", "triste", "feliz", "mano"]
EXTS = [".png", ".jpg", ".jpeg", ".webp"]


# ---------------------------------------------------------------------------
# Lectura y limpieza
# ---------------------------------------------------------------------------

def listar(entrada, hermana):
    """Devuelve {hermana: [(expresion, ruta), ...]} a partir de la entrada."""
    if entrada.is_file():
        archivos = [entrada]
    else:
        archivos = []
        for p in sorted(entrada.iterdir()):
            if p.is_file() and p.suffix.lower() in EXTS:
                archivos.append(p)

    grupos = {}
    for p in archivos:
        stem = p.stem.lower()
        if "_" not in stem:
            print("  ! " + p.name + ": el nombre debe ser <hermana>_<expresion>. Se salta.")
            continue
        partes = stem.split("_", 1)
        h = partes[0]
        expr = partes[1]
        if h not in HERMANAS:
            print("  ! " + p.name + ": '" + h + "' no es una hermana conocida. Se salta.")
            continue
        if hermana is not None and h != hermana:
            continue
        if expr not in EXPRESIONES:
            print("  ! " + p.name + ": expresión '" + expr + "' fuera de la lista " + ", ".join(EXPRESIONES) + ". Se procesa igual.")
        if h not in grupos:
            grupos[h] = []
        grupos[h].append((expr, p))
    return grupos


def cargar_rgba(ruta, huecos):
    """Devuelve (array RGBA uint8, texto de cómo se obtuvo el alfa)."""
    img = Image.open(ruta).convert("RGBA")
    arr = np.array(img)
    transparentes = float((arr[:, :, 3] < 250).mean())
    if transparentes > 0.05:
        return arr, "alfa propio conservado"

    rgb, alpha, etiquetas, borde = remove_background(img, suave=True)
    if huecos:
        alpha = remove_enclosed_holes(rgb, alpha, etiquetas, borde)
    return np.dstack([rgb, alpha]), "fondo blanco quitado"


def limpiar_islas(arr):
    """Borra componentes opacas diminutas (restos de fondo). Devuelve (arr, borradas)."""
    alfa = arr[:, :, 3]
    solido = alfa > UMBRAL_ALFA
    etiquetas, n = ndimage.label(solido)
    if n <= 1:
        return arr, 0

    tamanos = ndimage.sum(solido, etiquetas, range(1, n + 1))
    conservar = []
    for i in range(n):
        if tamanos[i] >= MIN_COMPONENTE:
            conservar.append(i + 1)

    mascara = np.isin(etiquetas, conservar)
    borradas = n - len(conservar)
    salida = arr.copy()
    sobra = solido & (~mascara)
    salida[sobra, 3] = 0
    return salida, borradas


def caja(arr):
    """(x0, y0, x1, y1) del contenido opaco, o None si no queda nada."""
    alfa = arr[:, :, 3]
    filas = np.where(alfa.max(axis=1) > UMBRAL_ALFA)[0]
    cols = np.where(alfa.max(axis=0) > UMBRAL_ALFA)[0]
    if len(filas) == 0 or len(cols) == 0:
        return None
    return (int(cols[0]), int(filas[0]), int(cols[-1]) + 1, int(filas[-1]) + 1)


def eje_x(recorte, modo):
    """Columna del eje del cuerpo, en px del recorte original.
    pies: centro de masa del 30 % inferior (no lo desplazan brazos ni pelo).
    masa: centro de masa de todo el chibi.
    bbox: centro de la caja."""
    alfa = recorte[:, :, 3].astype(np.float64)
    alto = alfa.shape[0]
    ancho = alfa.shape[1]

    if modo == "bbox":
        return ancho / 2.0

    if modo == "masa":
        zona = alfa
    else:
        inicio = int(alto * 0.70)
        zona = alfa[inicio:, :]

    pesos = zona.sum(axis=0)
    total = float(pesos.sum())
    if total <= 0.0:
        return ancho / 2.0
    return float(np.average(np.arange(ancho), weights=pesos))


# ---------------------------------------------------------------------------
# Proceso de un grupo (una hermana)
# ---------------------------------------------------------------------------

def procesar_grupo(h, items, args, salida):
    print("\n== " + h.capitalize() + " ==")

    datos = []
    for item in items:
        expr = item[0]
        ruta = item[1]
        try:
            arr, via = cargar_rgba(ruta, not args.sin_huecos)
        except Exception as e:
            print("  x " + ruta.name + "  ERROR: " + str(e))
            continue

        arr, borradas = limpiar_islas(arr)
        c = caja(arr)
        if c is None:
            print("  x " + ruta.name + ": no quedó nada opaco tras quitar el fondo.")
            continue

        recorte = arr[c[1]:c[3], c[0]:c[2]].copy()
        info = ruta.name + ": " + via + ", contenido " + str(c[2] - c[0]) + "x" + str(c[3] - c[1]) + " px"
        if borradas > 0:
            info = info + ", " + str(borradas) + " mota(s) borrada(s)"
        print("  · " + info)

        datos.append({
            "expr": expr,
            "ruta": ruta,
            "recorte": recorte,
            "ancho": c[2] - c[0],
            "alto": c[3] - c[1],
        })

    if len(datos) == 0:
        print("  (nada que procesar)")
        return 0

    # --- Escala común ---------------------------------------------------------
    ref = None
    for d in datos:
        if d["expr"] == "neutral":
            ref = d

    max_alto = 0
    max_ancho = 0
    for d in datos:
        if d["alto"] > max_alto:
            max_alto = d["alto"]
        if d["ancho"] > max_ancho:
            max_ancho = d["ancho"]

    if args.escala is not None:
        escala = float(args.escala)
        motivo = "forzada con --escala"
    else:
        if ref is None:
            ref = datos[0]
            print("  AVISO: no hay " + h + "_neutral; la escala se toma de '" + ref["expr"] + "'. Revisa que el tamaño coincida.")
        e_ref = float(args.alto_neutral) / float(ref["alto"])
        e_alto = float(PIES - MARGEN_SUP) / float(max_alto)
        e_ancho = float(LIENZO - 2 * MARGEN_LADO) / float(max_ancho)

        escala = e_ref
        motivo = "'" + ref["expr"] + "' queda en " + str(args.alto_neutral) + " px de alto"

        if e_alto < escala:
            escala = e_alto
            motivo = "tope por la expresión más alta (" + str(max_alto) + " px de origen)"
        if e_ancho < escala:
            escala = e_ancho
            motivo = "tope por la expresión más ancha (" + str(max_ancho) + " px de origen)"

        if motivo.startswith("tope"):
            nuevo = int(round(escala * float(ref["alto"])))
            print("  AVISO: " + motivo + ". El neutral queda en " + str(nuevo) + " px en vez de " + str(args.alto_neutral) + ".")
            print("         Para evitarlo, regenera la expresión más grande con el chibi más pequeño, o usa --alto-neutral " + str(nuevo) + ".")

    print("  Escala común: " + "{:.4f}".format(escala) + "  (" + motivo + ")")

    # --- Composición ----------------------------------------------------------
    hechos = 0
    for d in datos:
        nuevo_w = int(round(d["ancho"] * escala))
        nuevo_h = int(round(d["alto"] * escala))
        if nuevo_w < 1:
            nuevo_w = 1
        if nuevo_h < 1:
            nuevo_h = 1

        peq = resize_premultiplied(d["recorte"], (nuevo_w, nuevo_h))
        eje = eje_x(d["recorte"], args.eje) * escala

        x0 = int(round(LIENZO / 2.0 - eje))
        y0 = PIES - nuevo_h

        lienzo = np.zeros((LIENZO, LIENZO, 4), dtype=np.uint8)

        sx0 = 0
        if x0 < 0:
            sx0 = -x0
        sy0 = 0
        if y0 < 0:
            sy0 = -y0
        dx0 = 0
        if x0 > 0:
            dx0 = x0
        dy0 = 0
        if y0 > 0:
            dy0 = y0

        cw = nuevo_w - sx0
        if cw > LIENZO - dx0:
            cw = LIENZO - dx0
        ch = nuevo_h - sy0
        if ch > LIENZO - dy0:
            ch = LIENZO - dy0

        cortado = []
        if sx0 > 0:
            cortado.append("izquierda " + str(sx0) + " px")
        if x0 + nuevo_w > LIENZO:
            cortado.append("derecha " + str(x0 + nuevo_w - LIENZO) + " px")
        if sy0 > 0:
            cortado.append("arriba " + str(sy0) + " px")

        if cw > 0 and ch > 0:
            lienzo[dy0:dy0 + ch, dx0:dx0 + cw] = peq[sy0:sy0 + ch, sx0:sx0 + cw]
        else:
            print("  x " + d["ruta"].name + ": el chibi cae fuera del lienzo. Revisa --eje y --escala.")
            continue

        resumen = "  + " + d["expr"] + ": " + str(nuevo_w) + "x" + str(nuevo_h) + " px, aire sobre la cabeza " + str(y0) + " px, eje en x=" + str(int(round(LIENZO / 2.0)))
        if len(cortado) > 0:
            resumen = resumen + "   AVISO: se cortó " + ", ".join(cortado)
        print(resumen)

        if args.simular:
            hechos += 1
            continue

        destino = salida / (h + "_" + d["expr"] + ".png")
        if destino.exists() and not args.sobrescribir:
            print("      = " + destino.name + " ya existe, se salta (usa --sobrescribir)")
            continue

        Image.fromarray(lienzo).save(destino)
        hechos += 1

    return hechos


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(
        description="Normaliza los chibis de los minijuegos a 512x512 RGBA, con una escala común por hermana."
    )
    ap.add_argument("entrada", type=Path, help="carpeta con <hermana>_<expresion>.png (o un solo archivo con --escala)")
    ap.add_argument("salida", type=Path, help="carpeta de destino (game/images/chibis/)")
    ap.add_argument("--hermana", choices=HERMANAS, default=None, help="procesa solo esa hermana")
    ap.add_argument("--escala", type=float, default=None, help="fuerza la escala (px de origen -> px de lienzo)")
    ap.add_argument("--alto-neutral", type=int, default=ALTO_NEUTRAL, dest="alto_neutral",
                    help="alto en px del chibi neutral en el lienzo (por defecto " + str(ALTO_NEUTRAL) + ")")
    ap.add_argument("--eje", choices=["pies", "masa", "bbox"], default="pies",
                    help="cómo se calcula el eje horizontal (por defecto pies)")
    ap.add_argument("--sin-huecos", action="store_true", dest="sin_huecos",
                    help="no borra huecos blancos encerrados (caso Yotsuba: cuello blanco junto al chaleco amarillo)")
    ap.add_argument("--sobrescribir", action="store_true")
    ap.add_argument("--simular", action="store_true", help="no escribe nada, solo informa")
    args = ap.parse_args()

    if not args.entrada.exists():
        sys.exit("No existe: " + str(args.entrada))

    if args.entrada.is_file() and args.escala is None:
        sys.exit("Con un solo archivo hay que pasar --escala; si no, no coincidirá con el resto del set.")

    if args.alto_neutral < 100 or args.alto_neutral > PIES - MARGEN_SUP:
        sys.exit("--alto-neutral debe estar entre 100 y " + str(PIES - MARGEN_SUP) + ".")

    grupos = listar(args.entrada, args.hermana)
    if len(grupos) == 0:
        sys.exit("No se encontraron imágenes <hermana>_<expresion> compatibles.")

    if not args.simular:
        args.salida.mkdir(parents=True, exist_ok=True)

    total = 0
    for h in HERMANAS:
        if h in grupos:
            total += procesar_grupo(h, grupos[h], args, args.salida)

    print("\nListo. " + str(total) + " chibi(s) " + "procesado(s)" + ".")
    if args.simular:
        print("(simulación: no se escribió nada)")


if __name__ == "__main__":
    main()
