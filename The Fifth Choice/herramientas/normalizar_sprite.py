#!/usr/bin/env python3
"""
normalizar_sprite.py — Normaliza un sprite de hermana al estándar del set.

Reconstruido a partir de GUIA_ARTE.md (secciones 3, 4 y 5), que documenta el
comportamiento exacto que tenía el script original.

Estándar del set:
  - Lienzo 760 x 930 px, PNG RGBA con transparencia real.
  - Línea de ojos en la fila y = 199.
  - Distancia interpupilar (IPD) escalada a 77,2 px.
  - Eje horizontal: el centro de la falda (eje del cuerpo), no el centro del
    bounding box.

Uso:
  python normalizar_sprite.py entrada.png salida.png
  python normalizar_sprite.py entrada.png salida.png --ojos x1,y1,x2,y2
  python normalizar_sprite.py entrada.png salida.png --eje 384
  python normalizar_sprite.py entrada.png salida.png --sin-huecos

Notas:
  - Este script NO hace el desmatteado de halo blanco (eso es limpiar_halo.py,
    que se aplica sobre un sprite ya normalizado).
  - La detección de ojos busca iris AZUL. Con ojos marrones/negros (Isanari,
    Raiha, Maruo) o con los ojos cerrados, hay que pasar --ojos a mano.
  - Requiere Pillow, numpy y scipy.
"""

import sys
import argparse
import numpy as np
from PIL import Image
from scipy import ndimage

CANVAS_W, CANVAS_H = 760, 930
EYE_ROW = 199
TARGET_IPD = 77.2
BOTTOM_EXTEND_MAX = 30  # px — extensión automática si el render vino corto por el encuadre


# ---------------------------------------------------------------------------
# 1. Recorte de fondo y huecos encerrados (GUIA_ARTE.md, sección 4)
# ---------------------------------------------------------------------------

def remove_background(img_rgba):
    """
    Vuelve transparente el fondo blanco liso. Usa flood-fill (componentes
    conexas) desde los bordes del lienzo para distinguir el fondo real de los
    huecos blancos ENCERRADOS dentro de la figura (esos se deciden aparte).
    """
    arr = np.array(img_rgba)
    rgb = arr[:, :, :3].copy()
    h, w = rgb.shape[:2]

    whiteness = rgb.min(axis=2)  # "pureza": qué tan cerca de blanco puro
    is_white_ish = whiteness > 240

    labeled, _ = ndimage.label(is_white_ish)
    border_labels = set(labeled[0, :]) | set(labeled[-1, :]) | \
        set(labeled[:, 0]) | set(labeled[:, -1])
    border_labels.discard(0)

    bg_mask = np.isin(labeled, list(border_labels))
    alpha = np.where(bg_mask, 0, 255).astype(np.uint8)

    return rgb, alpha, labeled, border_labels


def remove_enclosed_holes(rgb, alpha, labeled, border_labels):
    """
    Un hueco blanco encerrado se borra (se hace transparente) SOLO si:
      - pureza media (min(r,g,b) promedio) >= 253.5, y
      - calidez del contorno (r - b promedio, excluyendo lineart oscura por
        luminancia media > 70) >= 20.
    Área mínima considerada: 40 px. Este es el discriminante fondo-vs-ropa
    de GUIA_ARTE.md sección 4: un hueco de fondo está rodeado de piel/pelo
    (cálido), la ropa blanca y su sombra son frías.
    """
    all_labels = set(np.unique(labeled)) - {0} - border_labels

    for lbl in all_labels:
        mask = labeled == lbl
        area = mask.sum()
        if area < 40:
            continue

        region = rgb[mask]
        purity = region.min(axis=1).mean()
        if purity < 253.5:
            continue

        ring = ndimage.binary_dilation(mask, iterations=2) & ~mask
        if ring.sum() == 0:
            continue

        ring_pixels = rgb[ring].astype(np.int16)
        luminance = ring_pixels.mean(axis=1)
        colored = ring_pixels[luminance > 70]  # descarta la lineart negra
        if len(colored) == 0:
            continue

        warmth = colored[:, 0].mean() - colored[:, 2].mean()  # r - b
        if warmth >= 20:
            alpha[mask] = 0

    return alpha


# ---------------------------------------------------------------------------
# 2. Detección de ojos e IPD (GUIA_ARTE.md, secciones 3 y 5)
# ---------------------------------------------------------------------------

def detect_eyes(rgba):
    """
    Busca iris azul restringido al 42% superior de la imagen.
    Umbral: b - r > 60 y b - g > 50 (subido para no confundir con brillos
    azules en la ropa, como pasó con el blazer de Ichika).
    """
    arr = np.array(rgba)
    h, w = arr.shape[:2]
    rgb = arr[:, :, :3].astype(np.int16)
    alpha = arr[:, :, 3]

    top_limit = int(h * 0.42)
    r = rgb[:top_limit, :, 0]
    g = rgb[:top_limit, :, 1]
    b = rgb[:top_limit, :, 2]
    a = alpha[:top_limit, :]

    blue_mask = (b - r > 60) & (b - g > 50) & (a > 128)

    labeled, n = ndimage.label(blue_mask)
    if n < 2:
        raise ValueError(
            f"solo se detectaron {n} región(es) de iris azul en el 42% "
            "superior. Si el personaje no tiene ojos azules (Isanari, Raiha, "
            "Maruo) o los tiene cerrados, usa --ojos x1,y1,x2,y2 copiando las "
            "coordenadas de las pupilas de otra versión del mismo render."
        )

    sizes = ndimage.sum(blue_mask, labeled, index=range(1, n + 1))
    top_two = np.argsort(sizes)[-2:] + 1
    centroids = ndimage.center_of_mass(blue_mask, labeled, top_two)

    pts = sorted([(c[1], c[0]) for c in centroids])  # (x, y), ordenados por x
    return pts[0], pts[1]


def detect_skirt_center(rgba):
    """
    Centro de masa horizontal de la falda verde, en la mitad inferior de la
    imagen. Es el eje del cuerpo que pide GUIA_ARTE.md, no el bounding box:
    el pelo suelto o los brazos abiertos no lo desplazan.
    Sirve igual con el verde estándar (90,118,63) que con el olivaceo de
    itsuki_neutral (92,102,74): el criterio es "verde domina", no un color fijo.
    """
    arr = np.array(rgba)
    h, w = arr.shape[:2]
    rgb = arr[:, :, :3].astype(np.int16)
    alpha = arr[:, :, 3]

    bottom_start = int(h * 0.5)
    r = rgb[bottom_start:, :, 0]
    g = rgb[bottom_start:, :, 1]
    b = rgb[bottom_start:, :, 2]
    a = alpha[bottom_start:, :]

    green_mask = (g > r) & (g > b) & (g > 60) & (a > 128)

    if green_mask.sum() < 100:
        raise ValueError(
            "no se pudo detectar la falda verde automáticamente. "
            "Usa --eje X para indicar el eje horizontal a mano (coordenada X "
            "en la imagen ORIGINAL, sin escalar)."
        )

    col_weights = green_mask.sum(axis=0)
    x_center = float(np.average(np.arange(w), weights=col_weights))
    return x_center


# ---------------------------------------------------------------------------
# 3. Escalado con alpha premultiplicado (GUIA_ARTE.md, sección 4)
# ---------------------------------------------------------------------------

def resize_premultiplied(rgba_arr, new_size):
    """
    Si se reescala el RGBA sin premultiplicar, Lanczos mezcla el RGB de los
    píxeles transparentes (que sigue siendo el blanco del fondo ya borrado)
    dentro del borde, generando halo. Se premultiplica, se escala cada canal
    en precisión float, y se despremultiplica al final.
    """
    arr = rgba_arr.astype(np.float32)
    rgb = arr[..., :3]
    alpha = arr[..., 3]
    premult = rgb * (alpha[..., None] / 255.0)

    channels = []
    for c in range(3):
        im = Image.fromarray(premult[..., c], mode="F")
        im = im.resize(new_size, Image.LANCZOS)
        channels.append(np.array(im))

    alpha_im = Image.fromarray(alpha, mode="F").resize(new_size, Image.LANCZOS)
    new_alpha = np.array(alpha_im)

    new_premult = np.stack(channels, axis=-1)
    with np.errstate(divide="ignore", invalid="ignore"):
        new_rgb = np.where(
            new_alpha[..., None] > 1.0,
            new_premult / (new_alpha[..., None] / 255.0),
            0,
        )

    new_rgb = np.clip(new_rgb, 0, 255)
    new_alpha = np.clip(new_alpha, 0, 255)
    return np.dstack([new_rgb, new_alpha]).astype(np.uint8)


# ---------------------------------------------------------------------------
# 4. Extensión inferior automática (GUIA_ARTE.md, sección 5)
# ---------------------------------------------------------------------------

def extend_bottom_if_cropped(canvas, max_gap=BOTTOM_EXTEND_MAX):
    """
    Si el render venía cortado por el borde del frame y el contenido se queda
    hasta max_gap px corto del final del lienzo, prolonga la última fila
    (ahí solo hay pierna, el corte es del encuadre, no del personaje).
    """
    alpha = canvas[:, :, 3]
    rows_with_content = np.where(alpha.max(axis=1) > 0)[0]
    if len(rows_with_content) == 0:
        return canvas

    last_row = rows_with_content[-1]
    gap = (CANVAS_H - 1) - last_row
    if 0 < gap <= max_gap:
        canvas = canvas.copy()
        fill_row = canvas[last_row, :, :]
        canvas[last_row + 1:CANVAS_H, :, :] = fill_row
    return canvas


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Normaliza un sprite de hermana al estándar del set "
                     "(760x930, ojos en y=199, IPD=77.2px, eje = centro de falda)."
    )
    parser.add_argument("entrada")
    parser.add_argument("salida")
    parser.add_argument(
        "--ojos", metavar="x1,y1,x2,y2",
        help="Coordenadas manuales de las dos pupilas en la imagen ORIGINAL "
             "(usar si el ojo no es azul, o está cerrado)."
    )
    parser.add_argument(
        "--eje", type=float, metavar="X",
        help="Coordenada X manual del eje del cuerpo (centro de la falda), "
             "en la imagen ORIGINAL."
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--huecos", action="store_true",
        help="Fuerza el borrado de huecos blancos encerrados (comportamiento por defecto)."
    )
    group.add_argument(
        "--sin-huecos", action="store_true",
        help="Desactiva el borrado de huecos blancos encerrados "
             "(caso Yotsuba: usar --solo-halo en limpiar_halo.py en su lugar)."
    )
    args = parser.parse_args()

    img = Image.open(args.entrada).convert("RGBA")
    rgb, alpha, labeled, border_labels = remove_background(img)

    if not args.sin_huecos:
        alpha = remove_enclosed_holes(rgb, alpha, labeled, border_labels)

    rgba = np.dstack([rgb, alpha])

    # --- Ojos / IPD ---
    if args.ojos:
        parts = [float(v) for v in args.ojos.split(",")]
        if len(parts) != 4:
            sys.exit("--ojos requiere 4 valores: x1,y1,x2,y2")
        p1, p2 = (parts[0], parts[1]), (parts[2], parts[3])
    else:
        try:
            p1, p2 = detect_eyes(rgba)
        except ValueError as e:
            sys.exit(f"Error detectando ojos: {e}")

    (x1, y1), (x2, y2) = p1, p2
    ipd_raw = float(np.hypot(x2 - x1, y2 - y1))
    eye_y_raw = (y1 + y2) / 2.0
    scale = TARGET_IPD / ipd_raw

    # --- Eje horizontal (centro de la falda) ---
    if args.eje is not None:
        axis_x_raw = args.eje
    else:
        try:
            axis_x_raw = detect_skirt_center(rgba)
        except ValueError as e:
            sys.exit(f"Error detectando eje: {e}")

    print(f"IPD detectada: {ipd_raw:.1f} px -> escala {scale:.3f}")
    print(f"Ojos en y={eye_y_raw:.1f} (original) -> se mueve a y={EYE_ROW}")
    print(f"Eje del cuerpo en x={axis_x_raw:.1f} (original)")

    # --- Escalado ---
    h, w = rgba.shape[:2]
    new_w = max(1, round(w * scale))
    new_h = max(1, round(h * scale))
    resized = resize_premultiplied(rgba, (new_w, new_h))

    eye_y_scaled = eye_y_raw * scale
    axis_x_scaled = axis_x_raw * scale

    # --- Composición sobre el lienzo 760x930 ---
    canvas = np.zeros((CANVAS_H, CANVAS_W, 4), dtype=np.uint8)

    offset_x = round(CANVAS_W / 2 - axis_x_scaled)
    offset_y = round(EYE_ROW - eye_y_scaled)

    src_x0 = max(0, -offset_x)
    src_y0 = max(0, -offset_y)
    dst_x0 = max(0, offset_x)
    dst_y0 = max(0, offset_y)

    copy_w = min(new_w - src_x0, CANVAS_W - dst_x0)
    copy_h = min(new_h - src_y0, CANVAS_H - dst_y0)

    if copy_w > 0 and copy_h > 0:
        canvas[dst_y0:dst_y0 + copy_h, dst_x0:dst_x0 + copy_w] = \
            resized[src_y0:src_y0 + copy_h, src_x0:src_x0 + copy_w]
    else:
        print("AVISO: el sprite escalado no cae dentro del lienzo. "
              "Revisa --ojos / --eje.", file=sys.stderr)

    canvas = extend_bottom_if_cropped(canvas)

    Image.fromarray(canvas, mode="RGBA").save(args.salida)
    print(f"Guardado: {args.salida} ({CANVAS_W}x{CANVAS_H})")


if __name__ == "__main__":
    main()
