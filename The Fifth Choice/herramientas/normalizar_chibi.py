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

La escala común sale de la expresión `neutral`: de la coronilla a los pies mide
--alto-neutral px (420). La coronilla es el punto más alto del PELO, sin contar
accesorios: el ahoge de Itsuki, el lazo de Yotsuba o los moños de Nino quedan
fuera, así que no encogen el cuerpo.

  - Si la hermana no lleva nada sobre la cabeza (Ichika, Miku), la coronilla es
    el borde superior del contenido y no hay que medir nada.
  - Si lleva accesorio, la fila de la coronilla se mide a mano en el render
    crudo (fila Y en px del archivo crudo, p. ej. con el panel Info de
    Photoshop) y se guarda en CORONILLA["<hermana>_neutral"] o se pasa con
    --coronilla-y. --medir genera una regla sobre el neutral crudo.
  - AJUSTE_OPTICO permite un retoque final a ojo (1.00 = sin cambio).

MODO INDIVIDUAL: si una expresión tiene su propia entrada en CORONILLA (p. ej.
"itsuki_feliz": 160), esa imagen se escala sola para medir también 420 px de
coronilla a pies. Sirve cuando la IA dibujó esa expresión con otras proporciones.
Las expresiones sin entrada usan la escala común del neutral.

En los dos casos la escala nunca sube tanto como para cortar la expresión más
alta (`feliz` con los brazos arriba) ni la más ancha; si hay tope, el informe lo
dice.

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
    python normalizar_chibi.py renders_crudos/chibis/ ../game/images/chibis/ --hermana nino --medir
    python normalizar_chibi.py renders_crudos/chibis/ ../game/images/chibis/ --hermana nino --coronilla-y 180

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
ALTO_NEUTRAL = 420       # de la coronilla (sin accesorios) a los pies del neutral, px del lienzo

# Fila Y de la coronilla (lo más alto del pelo, SIN ahoge, lazo ni moños) en el
# render CRUDO, en px del archivo crudo (no del lienzo de 512). Clave:
# "<hermana>_<expresion>", igual que el nombre del archivo.
#   - "<hermana>_neutral" fija la escala común de la hermana. Si no está, la
#     coronilla del neutral es el borde superior del contenido.
#   - Cualquier otra expresión que aparezca aquí se escala sola (modo individual).
# Si regeneras un crudo, vuelve a medir su fila.
CORONILLA = {
    "itsuki_neutral": 137,
    "itsuki_feliz": 109,
    "itsuki_triste": 87,
    "itsuki_esfuerzo": 131,
    "itsuki_animo": 90,

    "nino_neutral": 111,
    "nino_feliz": 87,
    "nino_triste": 42,
    "nino_esfuerzo": 138,
    "nino_animo": 67,

    "yotsuba_neutral": 208,
    "yotsuba_feliz": 170,
    "yotsuba_triste": 128,
    "yotsuba_esfuerzo": 178,
    "yotsuba_animo": 183,
}

# Retoque a ojo después de medir (1.00 = sin cambio; 0.97 = 3 % más pequeña).
AJUSTE_OPTICO = {
    "ichika": 1.00,
    "nino": 1.00,
    "miku": 1.00,
    "yotsuba": 1.00,
    "itsuki": 1.00,
}
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


def guardar_regla(h, datos):
    """Guarda medir_<hermana>_<expresion>.png: el crudo con una regla horizontal
    cada 10 px (etiquetada cada 50) para leer la fila de la coronilla."""
    from PIL import ImageDraw

    ref = None
    for d in datos:
        if d["expr"] == "neutral":
            ref = d
    if ref is None:
        ref = datos[0]
        print("  AVISO: no hay " + h + "_neutral; la regla se hace sobre '" + ref["expr"] + "'.")

    arr = ref["arr"]
    alto = arr.shape[0]
    ancho = arr.shape[1]
    fondo = Image.new("RGBA", (ancho + 90, alto), (70, 70, 80, 255))
    fondo.alpha_composite(Image.fromarray(arr), (90, 0))
    dib = ImageDraw.Draw(fondo)

    y = 0
    while y < alto:
        if y % 50 == 0:
            dib.line([(0, y), (ancho + 90, y)], fill=(255, 60, 60, 200), width=1)
            dib.text((4, y + 2), str(y), fill=(255, 255, 255, 255))
        else:
            dib.line([(60, y), (ancho + 90, y)], fill=(255, 230, 0, 90), width=1)
        y += 10

    destino = Path("medir_" + h + "_" + ref["expr"] + ".png")
    fondo.save(destino)
    print("  Regla guardada en " + str(destino.resolve()))
    print("  Contenido del crudo: filas " + str(ref["y_top"]) + " a " + str(ref["y_pies"]) + ".")
    print("  Lee la fila de la coronilla (lo más alto del PELO, sin ahoge, lazo ni moños)")
    print("  y pásala con --coronilla-y, o guárdala en CORONILLA[\"" + h + "_" + ref["expr"] + "\"].")


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
            "y_top": c[1],
            "y_pies": c[3],
            "arr": arr,
        })

    if len(datos) == 0:
        print("  (nada que procesar)")
        return 0

    if args.medir:
        guardar_regla(h, datos)
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
        coronilla = None
        if args.coronilla_y is not None:
            coronilla = args.coronilla_y
        elif CORONILLA.get(h + "_" + ref["expr"]) is not None:
            coronilla = CORONILLA[h + "_" + ref["expr"]]

        if coronilla is None:
            coronilla = ref["y_top"]
            origen = "borde superior del contenido"
        else:
            origen = "fila " + str(coronilla) + " del crudo"

        dist = ref["y_pies"] - coronilla
        if dist <= 0 or coronilla < ref["y_top"]:
            sys.exit("  La coronilla " + str(coronilla) + " no cae dentro del chibi '" + ref["expr"] + "' (filas "
                     + str(ref["y_top"]) + " a " + str(ref["y_pies"]) + " del crudo). Revisa --coronilla-y / CORONILLA.")

        ajuste = AJUSTE_OPTICO.get(h, 1.0)
        if args.ajuste is not None:
            ajuste = args.ajuste

        e_ref = float(args.alto_neutral) * ajuste / float(dist)
        motivo = "'" + ref["expr"] + "' mide " + str(args.alto_neutral) + " px de coronilla a pies (coronilla: " + origen + ")"
        if ajuste != 1.0:
            motivo = motivo + ", ajuste óptico x" + "{:.2f}".format(ajuste)

        e_alto = float(PIES - MARGEN_SUP) / float(max_alto)
        e_ancho = float(LIENZO - 2 * MARGEN_LADO) / float(max_ancho)

        escala = e_ref

        if e_alto < escala:
            escala = e_alto
            motivo = "tope por la expresión más alta (" + str(max_alto) + " px de origen)"
        if e_ancho < escala:
            escala = e_ancho
            motivo = "tope por la expresión más ancha (" + str(max_ancho) + " px de origen)"

        if motivo.startswith("tope"):
            print("  AVISO: " + motivo + ". Esta hermana queda más pequeña que el resto del set.")
            nuevo = int(round(escala * float(dist)))
            print("         Para igualarla, usa --alto-neutral " + str(nuevo) + " en TODAS las hermanas,")
            print("         o regenera la expresión más grande con el chibi más pequeño en el encuadre.")

        fila = PIES - int(round(escala * float(dist)))
        print("  Coronilla del neutral en el lienzo: fila " + str(fila))

    print("  Escala común: " + "{:.4f}".format(escala) + "  (" + motivo + ")")

    # --- Composición ----------------------------------------------------------
    alto_objetivo = float(args.alto_neutral) * AJUSTE_OPTICO.get(h, 1.0)
    if args.ajuste is not None:
        alto_objetivo = float(args.alto_neutral) * args.ajuste

    hechos = 0
    for d in datos:
        escala_d = escala
        clave = h + "_" + d["expr"]
        propia = CORONILLA.get(clave)
        if d is ref:
            propia = None
        if args.escala is not None:
            propia = None

        if propia is not None:
            dist_d = d["y_pies"] - propia
            if dist_d <= 0 or propia < d["y_top"]:
                print("  x " + d["ruta"].name + ": la coronilla " + str(propia) + " no cae dentro del chibi (filas "
                      + str(d["y_top"]) + " a " + str(d["y_pies"]) + "). Revisa CORONILLA[\"" + clave + "\"].")
                continue
            escala_d = alto_objetivo / float(dist_d)
            tope_alto = float(PIES - MARGEN_SUP) / float(d["alto"])
            tope_ancho = float(LIENZO - 2 * MARGEN_LADO) / float(d["ancho"])
            if tope_alto < escala_d:
                escala_d = tope_alto
                print("  AVISO: " + clave + " toca el tope de alto; queda algo más pequeña.")
            if tope_ancho < escala_d:
                escala_d = tope_ancho
                print("  AVISO: " + clave + " toca el tope de ancho; queda algo más pequeña.")
            print("  " + clave + ": escala individual " + "{:.4f}".format(escala_d)
                  + " (común " + "{:.4f}".format(escala) + ", coronilla en fila " + str(PIES - int(round(escala_d * dist_d))) + ")")

        nuevo_w = int(round(d["ancho"] * escala_d))
        nuevo_h = int(round(d["alto"] * escala_d))
        if nuevo_w < 1:
            nuevo_w = 1
        if nuevo_h < 1:
            nuevo_h = 1

        peq = resize_premultiplied(d["recorte"], (nuevo_w, nuevo_h))
        eje = eje_x(d["recorte"], args.eje) * escala_d

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
                    help="px del lienzo de la coronilla a los pies del neutral (por defecto " + str(ALTO_NEUTRAL) + ")")
    ap.add_argument("--coronilla-y", type=int, default=None, dest="coronilla_y",
                    help="fila de la coronilla (sin accesorio) en el neutral CRUDO, px del archivo. Solo con --hermana")
    ap.add_argument("--ajuste", type=float, default=None,
                    help="retoque óptico de esta pasada (1.0 = nada); pisa AJUSTE_OPTICO. Solo con --hermana")
    ap.add_argument("--medir", action="store_true",
                    help="no normaliza: guarda medir_<hermana>_neutral.png con una regla para leer la fila de la coronilla")
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

    if args.coronilla_y is not None and args.hermana is None:
        sys.exit("--coronilla-y es de una sola hermana: úsalo junto con --hermana.")

    if args.ajuste is not None and args.hermana is None:
        sys.exit("--ajuste es de una sola hermana: úsalo junto con --hermana.")

    if args.ajuste is not None and (args.ajuste < 0.8 or args.ajuste > 1.2):
        sys.exit("--ajuste debe estar entre 0.8 y 1.2.")

    if args.alto_neutral < 100 or args.alto_neutral > PIES - MARGEN_SUP:
        sys.exit("--alto-neutral debe estar entre 100 y " + str(PIES - MARGEN_SUP) + ".")

    grupos = listar(args.entrada, args.hermana)
    if len(grupos) == 0:
        sys.exit("No se encontraron imágenes <hermana>_<expresion> compatibles.")

    if not args.simular and not args.medir:
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
