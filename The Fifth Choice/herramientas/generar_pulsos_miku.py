#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generar_pulsos_miku.py — Mapa de pulsos de miku_tema.ogg para el minijuego M3.

La canción no tiene tempo fijo (≈75–79 BPM según el tramo), así que la fase 1 de
«El compás» no puede calcular las notas con un BPM. Este script saca el instante
de cada pulso con librosa y escribe game/10_mj_miku_pulsos.rpy con:

    define MIKU_PULSOS = [ ... ]     (segundos desde el inicio de la pista, 3 decimales)

Uso (desde «The Fifth Choice/»):
    pip install librosa
    python herramientas/generar_pulsos_miku.py
    python herramientas/generar_pulsos_miku.py --prueba    (autoprueba de las correcciones)

Cómo lo hace:
  1. Envolvente de ataques (hop 256 ≈ 11,6 ms de resolución).
  2. librosa.beat.beat_track con tempo de partida 76 BPM y TIGHTNESS 400: sigue
     la deriva del tempo, pero no salta a los contratiempos. (El seguimiento con
     bpm variable de librosa duplica el tempo en algunos tramos; por eso no se usa.)
  3. Correcciones, por si cambia la pista:
     - pulso doble (separación < 0,6 × la mediana) → se quita el segundo;
     - hueco (separación > 1,5 × la mediana) → se rellena con pulsos repartidos;
     - tramo inicial sin pulso claro: se quitan los primeros pulsos mientras su
       separación se aparte más de un 25 % de la mediana. No se inventan pulsos
       hacia atrás: la pista entra con una anacrusa (≈1,42 s) medio pulso antes
       del primer pulso real.
  4. Comprobación final (asserts) y resumen por tramos de 30 s.
"""

import os
import sys

import numpy as np
import librosa

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "game")
PISTA = os.path.join(BASE, "audio", "bgm", "bgm_hermanas", "miku_tema.ogg")
SALIDA = os.path.join(BASE, "10_mj_miku_pulsos.rpy")

SR = 22050
HOP = 256
BPM_INICIAL = 76.0
TIGHTNESS = 400
MIN_PULSOS = 80         ## la fase 1 pide como mucho ~69 (difícil); margen de sobra
TRAMO = 30.0


def detectar(y):
    oenv = librosa.onset.onset_strength(y=y, sr=SR, hop_length=HOP)
    _, b = librosa.beat.beat_track(onset_envelope=oenv, sr=SR, hop_length=HOP,
                                   start_bpm=BPM_INICIAL, tightness=TIGHTNESS, units="time")
    return oenv, [float(t) for t in b]


def corregir(p):
    notas = []
    med = float(np.median(np.diff(p)))

    p = list(p)
    quitados = 0
    while len(p) > 2 and abs((p[1] - p[0]) - med) > 0.25 * med:
        p.pop(0)
        quitados += 1
    if quitados:
        notas.append("%d pulsos erráticos quitados al principio (tramo inicial sin pulso claro)" % quitados)

    limpio = [p[0]]
    for t in p[1:]:
        if t - limpio[-1] < 0.6 * med:
            notas.append("pulso doble quitado en %.3f s" % t)
            continue
        limpio.append(t)

    relleno = [limpio[0]]
    for t in limpio[1:]:
        hueco = t - relleno[-1]
        if hueco > 1.5 * med:
            n = int(round(hueco / med))
            for k in range(1, n):
                relleno.append(relleno[-1] + hueco / n)
            notas.append("hueco de %.3f s rellenado con %d pulsos antes de %.3f s" % (hueco, n - 1, t))
        relleno.append(t)
    return relleno, med, notas


def comprobar(p, med):
    d = np.diff(p)
    assert len(p) >= MIN_PULSOS, "solo %d pulsos" % len(p)
    assert np.all(d > 0.6 * med), "quedan pulsos dobles"
    assert np.all(d < 1.5 * med), "quedan huecos"
    assert p[0] >= 0.0


def resumen(p, dur, oenv, notas):
    def fuerza(ts):
        f = librosa.time_to_frames(ts, sr=SR, hop_length=HOP)
        return float(np.mean([oenv[max(0, i - 3):i + 4].max() for i in f]))

    d = np.diff(p)
    print("Duración de la pista: %.2f s" % dur)
    print("Pulsos: %d  ·  primero %.3f s  ·  último %.3f s" % (len(p), p[0], p[-1]))
    print("Tempo medio: %.1f BPM  ·  separación %.3f–%.3f s" % (60.0 * (len(p) - 1) / (p[-1] - p[0]), d.min(), d.max()))
    a = 0.0
    while a < dur:
        s = [t for t in p if a <= t < a + TRAMO]
        if len(s) > 1:
            print("  %3d–%3d s: %5.1f BPM (%d pulsos)" % (a, a + TRAMO, 60.0 * (len(s) - 1) / (s[-1] - s[0]), len(s)))
        a += TRAMO
    medios = [(p[i] + p[i + 1]) / 2.0 for i in range(len(p) - 1)]
    print("Fuerza de ataque en el pulso / a medio pulso: %.2f / %.2f (fase correcta si la primera es mayor)" % (fuerza(p), fuerza(medios)))
    print("Correcciones: " + ("; ".join(notas) if notas else "ninguna"))


def escribir(p):
    filas = []
    for i in range(0, len(p), 10):
        filas.append("    " + ", ".join("%.3f" % t for t in p[i:i + 10]) + ",")
    with open(SALIDA, "w", encoding="utf-8") as f:
        f.write("################################################################################\n")
        f.write("##  10_mj_miku_pulsos.rpy — GENERADO, no editar a mano.\n")
        f.write("##  Instantes (s) de cada pulso de miku_tema.ogg para la fase 1 de M3.\n")
        f.write("##  Regenerar (desde «The Fifth Choice/»):\n")
        f.write("##      python herramientas/generar_pulsos_miku.py\n")
        f.write("##  %d pulsos · primero %.3f s · tempo medio %.1f BPM\n"
                % (len(p), p[0], 60.0 * (len(p) - 1) / (p[-1] - p[0])))
        f.write("################################################################################\n\n")
        f.write("define MIKU_PULSOS = [\n")
        f.write("\n".join(filas) + "\n")
        f.write("]\n")


def autoprueba():
    """Las correcciones no se activan con la pista actual: se prueban con datos sintéticos."""
    p = [3.0 + 0.8 * k for k in range(20)]
    p.insert(5, p[4] + 0.1)          ## pulso doble
    del p[12:14]                     ## hueco de 3 pulsos
    p = [0.5, 2.2] + p               ## intro errática (separaciones 1,7 y 0,8 → solo cae 0,5)
    r, med, notas = corregir(p)
    assert len(notas) == 3, notas
    assert abs(r[0] - 2.2) < 1e-6 and len(r) == 21, (r[0], len(r))
    assert np.allclose(np.diff(r), 0.8), np.diff(r)
    print("Autoprueba de correcciones: OK")


def main():
    if "--prueba" in sys.argv:
        return autoprueba()
    y, _ = librosa.load(PISTA, sr=SR)
    dur = len(y) / float(SR)
    oenv, crudos = detectar(y)
    pulsos, med, notas = corregir(crudos)
    pulsos = [round(t, 3) for t in pulsos]
    comprobar(pulsos, med)
    resumen(pulsos, dur, oenv, notas)
    escribir(pulsos)
    print("Escrito: " + os.path.normpath(SALIDA))


if __name__ == "__main__":
    sys.exit(main())
