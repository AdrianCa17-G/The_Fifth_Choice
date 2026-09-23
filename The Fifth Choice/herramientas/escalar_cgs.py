#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
escalar_cgs.py — Pasa un lote de CG y fondos a 1920x1080 (Lanczos) y los guarda
en WebP 95.

Reglas del set:
  - Realce de nitidez SOLO a las fuentes JPEG, y con umbral (unsharp mask).
  - Saturacion de referencia: media de S (HSV, 0-255) entre 68 y 84.
    Lo que salga por debajo se corrige aqui, en el escalado, no regenerando.

Requisitos: Python 3.8+, pillow, numpy
    pip install pillow numpy

Uso:
    python escalar_cgs.py entrada/ salida/
    python escalar_cgs.py entrada/ salida/ --modo contain
    python escalar_cgs.py cg_suelto.png salida/ --sobrescribir
    python escalar_cgs.py entrada/ salida/ --simular        (solo informe)
"""

import argparse
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageEnhance, ImageFilter, ImageOps

Image.MAX_IMAGE_PIXELS = None
LANCZOS = getattr(Image, "Resampling", Image).LANCZOS

# ----------------------------------------------------------------------------
# Valores por defecto del set
# ----------------------------------------------------------------------------
ANCHO, ALTO = 1920, 1080
CALIDAD = 95
SAT_MIN, SAT_MAX = 68.0, 84.0
FACTOR_SAT_MAX = 1.8

# Unsharp mask suave, con umbral para no levantar el ruido de bloque del JPEG
UNSHARP_RADIO = 1.0
UNSHARP_PORC = 55
UNSHARP_UMBRAL = 4

EXTS = {".png", ".jpg", ".jpeg", ".webp", ".bmp", ".tif", ".tiff"}
JPEG_EXTS = {".jpg", ".jpeg"}


# ----------------------------------------------------------------------------
# Utilidades
# ----------------------------------------------------------------------------
def listar_imagenes(entrada: Path, recursivo: bool):
    if entrada.is_file():
        return [entrada] if entrada.suffix.lower() in EXTS else []
    patron = "**/*" if recursivo else "*"
    return sorted(
        p for p in entrada.glob(patron)
        if p.is_file() and p.suffix.lower() in EXTS
    )


def saturacion_media(img: Image.Image) -> float:
    """Media de S en HSV (0-255), igual que la que usa el resto del set.
    Ignora los pixeles totalmente transparentes."""
    if img.mode == "RGBA":
        arr = np.asarray(img, dtype=np.float32)
        rgb, alfa = arr[..., :3], arr[..., 3]
        mascara = alfa > 8
    else:
        rgb = np.asarray(img.convert("RGB"), dtype=np.float32)
        mascara = None

    mx = rgb.max(axis=2)
    mn = rgb.min(axis=2)
    sat = np.where(mx > 0, (mx - mn) / np.maximum(mx, 1e-6) * 255.0, 0.0)

    if mascara is not None:
        if not mascara.any():
            return 0.0
        return float(sat[mascara].mean())
    return float(sat.mean())


def encajar(img: Image.Image, ancho: int, alto: int, modo: str, anclaje: str) -> Image.Image:
    """Lleva la imagen a ancho x alto. cover = recorta, contain = barras, estirar = deforma."""
    if img.size == (ancho, alto):
        return img

    if modo == "estirar":
        return img.resize((ancho, alto), LANCZOS)

    ratio_dst = ancho / alto
    ratio_src = img.width / img.height

    if modo == "cover":
        if abs(ratio_src - ratio_dst) > 1e-3:
            if ratio_src > ratio_dst:  # mas ancha de la cuenta: recorto laterales
                nuevo_w = max(1, round(img.height * ratio_dst))
                x = (img.width - nuevo_w) // 2
                img = img.crop((x, 0, x + nuevo_w, img.height))
            else:                       # mas alta: recorto arriba/abajo
                nuevo_h = max(1, round(img.width / ratio_dst))
                if anclaje == "arriba":
                    y = 0
                elif anclaje == "abajo":
                    y = img.height - nuevo_h
                else:
                    y = (img.height - nuevo_h) // 2
                img = img.crop((0, y, img.width, y + nuevo_h))
        return img.resize((ancho, alto), LANCZOS)

    # contain
    esc = min(ancho / img.width, alto / img.height)
    w = max(1, round(img.width * esc))
    h = max(1, round(img.height * esc))
    reducida = img.resize((w, h), LANCZOS)
    fondo = (0, 0, 0, 0) if img.mode == "RGBA" else (0, 0, 0)
    lienzo = Image.new(img.mode, (ancho, alto), fondo)
    lienzo.paste(reducida, ((ancho - w) // 2, (alto - h) // 2))
    return lienzo


def realzar_jpeg(img: Image.Image) -> Image.Image:
    """Unsharp con umbral. El umbral es lo que evita amplificar el bloque JPEG."""
    if img.mode == "RGBA":
        rgb = img.convert("RGB").filter(
            ImageFilter.UnsharpMask(UNSHARP_RADIO, UNSHARP_PORC, UNSHARP_UMBRAL)
        )
        rgb.putalpha(img.getchannel("A"))
        return rgb
    return img.filter(ImageFilter.UnsharpMask(UNSHARP_RADIO, UNSHARP_PORC, UNSHARP_UMBRAL))


def buscar_factor_saturacion(img: Image.Image, objetivo: float, factor_max: float) -> float:
    """Biseccion sobre una miniatura: barata y suficientemente exacta."""
    peq = img.convert("RGB")
    peq.thumbnail((512, 512), LANCZOS)

    if saturacion_media(ImageEnhance.Color(peq).enhance(factor_max)) <= objetivo:
        return factor_max

    lo, hi = 1.0, factor_max
    for _ in range(14):
        mid = (lo + hi) / 2.0
        if saturacion_media(ImageEnhance.Color(peq).enhance(mid)) < objetivo:
            lo = mid
        else:
            hi = mid
    return round((lo + hi) / 2.0, 3)


def aplicar_saturacion(img: Image.Image, factor: float) -> Image.Image:
    if abs(factor - 1.0) < 0.005:
        return img
    if img.mode == "RGBA":
        alfa = img.getchannel("A")
        rgb = ImageEnhance.Color(img.convert("RGB")).enhance(factor)
        rgb.putalpha(alfa)
        return rgb
    return ImageEnhance.Color(img).enhance(factor)


# ----------------------------------------------------------------------------
# Proceso
# ----------------------------------------------------------------------------
def procesar(ruta: Path, destino: Path, args) -> dict:
    info = {"archivo": ruta.name, "estado": "ok", "nitidez": False, "factor": 1.0}

    with Image.open(ruta) as abierta:
        img = ImageOps.exif_transpose(abierta)
        es_jpeg = ruta.suffix.lower() in JPEG_EXTS
        info["origen"] = f"{img.width}x{img.height}"

        if img.mode in ("P", "LA", "PA"):
            img = img.convert("RGBA" if "A" in img.mode or "transparency" in img.info else "RGB")
        elif img.mode not in ("RGB", "RGBA"):
            img = img.convert("RGB")

        if img.width < args.ancho or img.height < args.alto:
            info["aviso"] = "fuente menor que el destino, se esta ampliando"

        img = encajar(img, args.ancho, args.alto, args.modo, args.anclaje)

        # Nitidez: solo fuentes JPEG, y con umbral.
        if (es_jpeg or args.nitidez_siempre) and not args.sin_nitidez:
            img = realzar_jpeg(img)
            info["nitidez"] = True

        sat = saturacion_media(img)
        info["sat_antes"] = round(sat, 1)

        if not args.sin_saturacion:
            if sat < args.sat_min:
                objetivo = args.sat_objetivo if args.sat_objetivo else args.sat_min + 2.0
                factor = buscar_factor_saturacion(img, objetivo, args.factor_max)
                img = aplicar_saturacion(img, factor)
                info["factor"] = factor
            elif sat > args.sat_max and args.bajar_saturacion:
                objetivo = args.sat_max - 1.0
                lo, hi = 0.5, 1.0
                peq = img.convert("RGB")
                peq.thumbnail((512, 512), LANCZOS)
                for _ in range(14):
                    mid = (lo + hi) / 2.0
                    if saturacion_media(ImageEnhance.Color(peq).enhance(mid)) > objetivo:
                        hi = mid
                    else:
                        lo = mid
                factor = round((lo + hi) / 2.0, 3)
                img = aplicar_saturacion(img, factor)
                info["factor"] = factor

        info["sat_despues"] = round(saturacion_media(img), 1)

        if info["sat_despues"] < args.sat_min - 0.5:
            info["aviso"] = "sigue por debajo del rango del set, revisar a mano"
        elif info["sat_despues"] > args.sat_max + 0.5:
            info["aviso"] = "por encima del rango del set"

        if args.simular:
            info["estado"] = "simulado"
            return info

        destino.parent.mkdir(parents=True, exist_ok=True)
        if img.mode == "RGBA" and not args.mantener_alfa:
            fondo = Image.new("RGB", img.size, (0, 0, 0))
            fondo.paste(img, mask=img.getchannel("A"))
            img = fondo

        img.save(destino, "WEBP", quality=args.calidad, method=6)

    info["salida"] = destino.name
    info["peso_kb"] = round(destino.stat().st_size / 1024, 1) if destino.exists() else 0
    return info


def main():
    ap = argparse.ArgumentParser(
        description="Escala CG y fondos a 1920x1080 con Lanczos y los guarda en WebP 95."
    )
    ap.add_argument("entrada", type=Path, help="archivo o carpeta de origen")
    ap.add_argument("salida", type=Path, help="carpeta de destino")
    ap.add_argument("--ancho", type=int, default=ANCHO)
    ap.add_argument("--alto", type=int, default=ALTO)
    ap.add_argument("--calidad", type=int, default=CALIDAD, help="calidad WebP (por defecto 95)")
    ap.add_argument("--modo", choices=["cover", "contain", "estirar"], default="cover")
    ap.add_argument("--anclaje", choices=["centro", "arriba", "abajo"], default="centro",
                    help="que parte se conserva al recortar en vertical")
    ap.add_argument("--sat-min", type=float, default=SAT_MIN, dest="sat_min")
    ap.add_argument("--sat-max", type=float, default=SAT_MAX, dest="sat_max")
    ap.add_argument("--sat-objetivo", type=float, default=None, dest="sat_objetivo")
    ap.add_argument("--factor-max", type=float, default=FACTOR_SAT_MAX, dest="factor_max")
    ap.add_argument("--sin-saturacion", action="store_true", dest="sin_saturacion")
    ap.add_argument("--bajar-saturacion", action="store_true", dest="bajar_saturacion",
                    help="tambien corrige hacia abajo los que pasan de 84")
    ap.add_argument("--sin-nitidez", action="store_true", dest="sin_nitidez")
    ap.add_argument("--nitidez-siempre", action="store_true", dest="nitidez_siempre",
                    help="aplica unsharp tambien a PNG/WebP (fuera del estandar)")
    ap.add_argument("--mantener-alfa", action="store_true", dest="mantener_alfa")
    ap.add_argument("--recursivo", action="store_true")
    ap.add_argument("--sobrescribir", action="store_true")
    ap.add_argument("--simular", action="store_true", help="no escribe nada, solo informa")
    args = ap.parse_args()

    if not args.entrada.exists():
        sys.exit(f"No existe: {args.entrada}")

    imagenes = listar_imagenes(args.entrada, args.recursivo)
    if not imagenes:
        sys.exit("No se encontraron imagenes compatibles.")

    base = args.entrada if args.entrada.is_dir() else args.entrada.parent
    print(f"{len(imagenes)} imagen(es) -> {args.ancho}x{args.alto}, WebP {args.calidad}\n")

    hechos = saltados = fallos = 0
    for ruta in imagenes:
        relativa = ruta.relative_to(base) if args.recursivo else Path(ruta.name)
        destino = args.salida / relativa.with_suffix(".webp")

        if destino.exists() and not args.sobrescribir and not args.simular:
            print(f"  = {ruta.name}  (ya existe, se salta)")
            saltados += 1
            continue

        try:
            info = procesar(ruta, destino, args)
        except Exception as e:
            print(f"  x {ruta.name}  ERROR: {e}")
            fallos += 1
            continue

        nitidez = "unsharp" if info["nitidez"] else "sin unsharp"
        sat = f"sat {info['sat_antes']} -> {info['sat_despues']}"
        factor = f" (x{info['factor']})" if info["factor"] != 1.0 else ""
        peso = f" {info.get('peso_kb', 0)} KB" if not args.simular else ""
        print(f"  + {ruta.name}  [{info['origen']}] {nitidez}, {sat}{factor}{peso}")
        if "aviso" in info:
            print(f"      ! {info['aviso']}")
        hechos += 1

    print(f"\nListo. {hechos} procesadas, {saltados} saltadas, {fallos} con error.")


if __name__ == "__main__":
    main()