#!/usr/bin/env python3
"""
normalizar_extra.py — Normaliza sprites de Raiha e Isanari (no son de las 5 hermanas).

Diferencias clave frente a normalizar_sprite.py:
  - Cada personaje tiene su PROPIA fila de ojos y su PROPIA IPD objetivo
    (no la de 199 / 77.2 del set de hermanas), porque a ellos la escala
    se les deriva de su altura real, no de una cabeza igual para todos.
    Ver GUIA_ARTE.md sección 3 "Personajes que no miden lo que las hermanas".
  - --ojos es OBLIGATORIO. No hay detección automática de ojos: con tan
    pocos renders no vale la pena arriesgarse a que una mancha azul del
    pelo o la ropa se confunda con un iris.
  - No hay detección de falda (ninguno de los dos lleva falda verde). El
    eje se calcula como el punto medio entre los dos ojos que tú pases,
    salvo que fuerces --eje a mano.
  - --corte funciona igual que en la versión final de normalizar_sprite.py:
    la escala se calcula para llenar el lienzo, pero nunca sube tanto como
    para cortar la cabeza/pelo/gafas; si al bajar la escala sobra lienzo,
    se recalcula el corte para usar pierna/cuerpo real en vez de estirar
    la última fila.

Lienzo: 760x930 (igual al set de hermanas, para que compartan fondo/escena).
"""

import sys
import argparse
import numpy as np
from PIL import Image
from scipy import ndimage

CANVAS_W, CANVAS_H = 760, 930
BOTTOM_EXTEND_MAX = 30

WHITE_HI = 250   # blanco casi puro -> fondo seguro
WHITE_LO = 225   # por debajo de esto ya es dibujo

# Estándares ya calibrados en GUIA_ARTE.md (sección 3).
# fila_ojos: en qué renglón del lienzo de 930px van los ojos de ese personaje.
# ipd_objetivo: a qué IPD final se escala.
PRESETS = {
    "isanari": dict(fila_ojos=109, ipd_objetivo=77.2),
    "raiha":   dict(fila_ojos=388, ipd_objetivo=68.3),
}


# ---------------------------------------------------------------------------
# 1. Fondo (con alpha suave + de-matte del borde)
# ---------------------------------------------------------------------------

def remove_background(img_rgba, suave=True):
    arr = np.array(img_rgba)
    rgb = arr[:, :, :3].astype(np.float32)
    whiteness = rgb.min(axis=2)

    core = whiteness > WHITE_HI
    labeled, _ = ndimage.label(core)
    border = set(labeled[0, :]) | set(labeled[-1, :]) | \
             set(labeled[:, 0]) | set(labeled[:, -1])
    border.discard(0)
    bg_core = np.isin(labeled, list(border))

    if not suave:
        return arr[:, :, :3].copy(), np.where(bg_core, 0, 255).astype(np.uint8), labeled, border

    # el halo de antialias es "casi blanco" y CONECTADO al fondo puro
    halo = whiteness > WHITE_LO
    bg = ndimage.binary_propagation(bg_core, mask=halo)

    t = np.clip((whiteness - WHITE_LO) / float(WHITE_HI - WHITE_LO), 0.0, 1.0)
    alpha = np.where(bg, (1.0 - t) * 255.0, 255.0)
    alpha[bg_core] = 0.0

    # de-matte: quitar el blanco que el antialias mezcló en el borde
    a = alpha[..., None] / 255.0
    parcial = bg & (alpha > 0.5)
    dem = (rgb - 255.0 * (1.0 - a)) / np.maximum(a, 1e-3)
    rgb_out = rgb.copy()
    rgb_out[parcial] = np.clip(dem[parcial], 0, 255)

    return rgb_out.astype(np.uint8), alpha.astype(np.uint8), labeled, border


def remove_enclosed_holes(rgb, alpha, labeled, border_labels):
    """Huecos blancos encerrados: se borran solo si son fondo (contorno cálido)."""
    all_labels = set(np.unique(labeled)) - {0} - set(border_labels)
    for lbl in all_labels:
        mask = labeled == lbl
        if mask.sum() < 40:
            continue
        if rgb[mask].min(axis=1).mean() < 253.5:
            continue
        ring = ndimage.binary_dilation(mask, iterations=2) & ~mask
        if ring.sum() == 0:
            continue
        px = rgb[ring].astype(np.int16)
        colored = px[px.mean(axis=1) > 70]
        if len(colored) == 0:
            continue
        if colored[:, 0].mean() - colored[:, 2].mean() >= 20:
            alpha[mask] = 0
    return alpha


# ---------------------------------------------------------------------------
# 2. Escalado con alpha premultiplicado
# ---------------------------------------------------------------------------

def resize_premultiplied(rgba_arr, new_size):
    arr = rgba_arr.astype(np.float32)
    rgb = arr[..., :3]
    alpha = arr[..., 3]
    premult = rgb * (alpha[..., None] / 255.0)

    chans = []
    for c in range(3):
        plane = np.ascontiguousarray(premult[..., c])
        im = Image.fromarray(plane, mode="F").resize(new_size, Image.LANCZOS)
        chans.append(np.array(im))

    a_im = Image.fromarray(np.ascontiguousarray(alpha), mode="F")
    new_alpha = np.clip(np.array(a_im.resize(new_size, Image.LANCZOS)), 0, 255)

    new_pre = np.clip(np.stack(chans, axis=-1), 0, None)
    with np.errstate(divide="ignore", invalid="ignore"):
        new_rgb = np.where(new_alpha[..., None] > 1.0,
                           new_pre / np.maximum(new_alpha[..., None] / 255.0, 1e-3),
                           0)
    return np.dstack([np.clip(new_rgb, 0, 255), new_alpha]).astype(np.uint8)


# ---------------------------------------------------------------------------
# 3. Extensión inferior (red de seguridad si sobra lienzo tras el corte)
# ---------------------------------------------------------------------------

def extend_bottom_if_cropped(canvas, max_gap=BOTTOM_EXTEND_MAX, offset=2):
    alpha = canvas[:, :, 3]
    rows = np.where(alpha.max(axis=1) > 8)[0]
    if len(rows) == 0:
        return canvas
    last = int(rows[-1])
    gap = (CANVAS_H - 1) - last
    if not (0 < gap <= max_gap):
        return canvas
    src = max(0, last - offset)
    canvas = canvas.copy()
    canvas[src + 1:CANVAS_H, :, :] = canvas[src, :, :]
    return canvas


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main():
    p = argparse.ArgumentParser(
        description="Normaliza un sprite de Raiha o Isanari (estándar propio, no el de las hermanas).")
    p.add_argument("entrada")
    p.add_argument("salida")
    p.add_argument("--personaje", choices=sorted(PRESETS), required=True,
                   help="Aplica la fila de ojos y la IPD objetivo ya calibradas para ese personaje.")
    p.add_argument("--ojos", metavar="x1,y1,x2,y2", required=True,
                   help="OBLIGATORIO. Coordenadas de los iris en la imagen ORIGINAL.")
    p.add_argument("--eje", type=float, metavar="X",
                   help="Fuerza el eje horizontal. Si no se pasa, se usa el punto medio de --ojos.")
    p.add_argument("--corte", type=int, metavar="Y",
                   help="Corta en esta fila Y (imagen ORIGINAL) y escala para llenar el lienzo, "
                        "sin cortar nunca la cabeza.")
    p.add_argument("--duro", action="store_true", help="Alpha binario en vez de suave.")
    g = p.add_mutually_exclusive_group()
    g.add_argument("--huecos", action="store_true")
    g.add_argument("--sin-huecos", action="store_true")
    args = p.parse_args()

    preset = PRESETS[args.personaje]
    EYE_ROW = preset["fila_ojos"]
    TARGET_IPD = preset["ipd_objetivo"]

    img = Image.open(args.entrada).convert("RGBA")
    rgb, alpha, labeled, border = remove_background(img, suave=not args.duro)
    if not args.sin_huecos:
        alpha = remove_enclosed_holes(rgb, alpha, labeled, border)
    rgba = np.dstack([rgb, alpha])
    H, W = rgba.shape[:2]

    v = [float(x) for x in args.ojos.split(",")]
    if len(v) != 4:
        sys.exit("--ojos requiere 4 valores: x1,y1,x2,y2")
    (x1, y1), (x2, y2) = (v[0], v[1]), (v[2], v[3])

    ipd_raw = float(np.hypot(x2 - x1, y2 - y1))
    eye_y_raw = (y1 + y2) / 2.0
    axis_x_raw = args.eje if args.eje is not None else (x1 + x2) / 2.0

    frac = ipd_raw / W
    if not (0.02 <= frac <= 0.30):
        print(f"AVISO: IPD={ipd_raw:.1f}px = {frac*100:.1f}% del ancho. Revisa las coordenadas de --ojos.",
              file=sys.stderr)

    # techo real de la cabeza (pelo, gafas en la frente, etc.) y fin real del dibujo
    filas_dibujo = np.where(rgba[:, :, 3].max(axis=1) > 8)[0]
    if len(filas_dibujo) == 0:
        sys.exit("ERROR: no quedó nada opaco tras quitar el fondo. Revisa el recorte.")
    y_top_raw = int(filas_dibujo[0])
    y_bottom_dibujo = int(filas_dibujo[-1])
    max_scale_cabeza = EYE_ROW / (eye_y_raw - y_top_raw)

    if args.corte is not None:
        if not (eye_y_raw < args.corte < H):
            sys.exit(f"--corte debe estar entre {eye_y_raw:.0f} (ojos) y {H - 1}.")

        scale = (CANVAS_H - EYE_ROW + 3) / (args.corte - eye_y_raw)
        if scale > max_scale_cabeza:
            print(f"AVISO: se reduce la escala de {scale:.4f} a {max_scale_cabeza:.4f} "
                  f"para no cortar la cabeza/pelo.", file=sys.stderr)
            scale = max_scale_cabeza

        corte_real = eye_y_raw + (CANVAS_H - EYE_ROW) / scale
        if corte_real <= y_bottom_dibujo:
            corte_final = int(round(corte_real))
            print(f"Corte ajustado a Y={corte_final} (usa cuerpo real, no estirado).")
        else:
            corte_final = y_bottom_dibujo
            print(f"AVISO: no hay suficiente dibujo ({y_bottom_dibujo}px) para llenar "
                  f"el lienzo a esta escala -> se estirará un poco el resto.", file=sys.stderr)

        rgba[corte_final:, :, 3] = 0
    else:
        scale = TARGET_IPD / ipd_raw
        if scale > max_scale_cabeza:
            print(f"AVISO: se reduce la escala de {scale:.4f} a {max_scale_cabeza:.4f} "
                  f"para no cortar la cabeza/pelo.", file=sys.stderr)
            scale = max_scale_cabeza

    print(f"[{args.personaje}] Ojos: ({x1:.0f},{y1:.0f}) y ({x2:.0f},{y2:.0f})")
    print(f"IPD {ipd_raw:.1f}px -> escala {scale:.4f}   (eje x={axis_x_raw:.1f}, fila_ojos={EYE_ROW})")
    print(f"IPD final: {ipd_raw * scale:.1f}px (objetivo {TARGET_IPD})")

    new_w, new_h = max(1, round(W * scale)), max(1, round(H * scale))
    resized = resize_premultiplied(rgba, (new_w, new_h))

    eye_y_s = eye_y_raw * scale
    axis_x_s = axis_x_raw * scale

    canvas = np.zeros((CANVAS_H, CANVAS_W, 4), dtype=np.uint8)
    off_x = round(CANVAS_W / 2 - axis_x_s)
    off_y = round(EYE_ROW - eye_y_s)

    sx0, sy0 = max(0, -off_x), max(0, -off_y)
    dx0, dy0 = max(0, off_x), max(0, off_y)
    cw = min(new_w - sx0, CANVAS_W - dx0)
    ch = min(new_h - sy0, CANVAS_H - dy0)

    if cw <= 0 or ch <= 0:
        sys.exit("ERROR: el sprite escalado cae entero fuera del lienzo. Revisa --ojos/--eje.")

    canvas[dy0:dy0 + ch, dx0:dx0 + cw] = resized[sy0:sy0 + ch, sx0:sx0 + cw]

    # informe de recorte real
    ys, xs = np.nonzero(resized[:, :, 3] > 8)
    if len(xs):
        bx0, bx1, by0, by1 = xs.min(), xs.max(), ys.min(), ys.max()
        perdido = []
        if by0 < sy0:                              perdido.append(f"arriba {sy0 - by0}px (CABEZA)")
        if by1 >= sy0 + ch and args.corte is None: perdido.append(f"abajo {by1 - (sy0 + ch) + 1}px")
        if bx0 < sx0:                              perdido.append(f"izquierda {sx0 - bx0}px")
        if bx1 >= sx0 + cw:                        perdido.append(f"derecha {bx1 - (sx0 + cw) + 1}px")
        if perdido:
            print("AVISO: se recortó contenido -> " + ", ".join(perdido), file=sys.stderr)
        else:
            print(f"Sin recorte. Aire sobre la cabeza: {by0 + off_y}px")

    # red de seguridad: rellena cualquier hueco residual estirando la última fila
    if args.corte is None:
        canvas = extend_bottom_if_cropped(canvas)
    else:
        canvas = extend_bottom_if_cropped(canvas, max_gap=CANVAS_H, offset=5)

    filas_out = np.where((canvas[:, :, 3] > 200).sum(axis=1) > 3)[0]
    if len(filas_out):
        print(f"Último renglón dibujado en el lienzo: Y={filas_out[-1]} (debería ser ~{CANVAS_H - 1})")

    Image.fromarray(canvas, mode="RGBA").save(args.salida)
    print(f"Guardado: {args.salida} ({CANVAS_W}x{CANVAS_H})")


if __name__ == "__main__":
    main()
