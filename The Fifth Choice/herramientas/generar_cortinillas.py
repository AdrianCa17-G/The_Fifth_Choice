"""
generar_cortinillas.py — Assets de las tarjetas de capitulo (13_transiciones.rpy)

Genera, desde cero y sin material ajeno:
  game/ui/cort_cinta.png                 cinta blanca (se tiñe en Ren'Py)
  game/audio/sfx/cort_capitulo.ogg       inicio de capitulo (una nota por hermana)
  game/audio/sfx/cort_examen.ogg         igual, con el cambio a "Semana de examenes"
  game/audio/sfx/cort_fin.ogg            fin de prologo / fin de capitulo
  game/audio/sfx/cort_hub.ogg            entrada al hub
  game/audio/sfx/cort_hermana_<h>.ogg    salida del hub hacia cada hermana

Los sonidos son campanitas sintetizadas (tipo celesta) en Re mayor pentatonico.
Cada hermana tiene SU nota: Ichika Re, Nino Mi, Miku Fa#, Yotsuba La, Itsuki Si.

IMPORTANTE: los tiempos de RITMOS son los mismos que CORT_RITMOS en
13_transiciones.rpy. Si cambias uno, cambia el otro y vuelve a generar.

Uso:   python herramientas/generar_cortinillas.py
Necesita: numpy, scipy, Pillow y ffmpeg en el PATH (para pasar a .ogg).
"""

import os
import shutil
import subprocess
import sys

import numpy as np
from PIL import Image, ImageDraw
from scipy.io import wavfile
from scipy.signal import fftconvolve

AQUI = os.path.dirname(os.path.abspath(__file__))
GAME = os.path.join(AQUI, "..", "game")
SR = 44100

RITMOS = {
    "largo": dict(numero=0.55, hermanas=1.30, paso=0.25, titulo=2.90,
                  cinta=3.50, flores=3.75, paso_flor=0.09, cambio=4.70),
    "medio": dict(numero=0.50, titulo=1.50, cinta=2.20, flores=2.50, paso_flor=0.18),
    "corto": dict(numero=0.30, hermanas=0.70, paso=0.0, titulo=1.10,
                  cinta=1.50, flores=1.70, paso_flor=0.07),
}

RE3, LA3, FAS4 = 146.83, 220.00, 369.99
RE4, LA4 = 293.66, 440.00
RE5, MI5, FAS5, LA5, SI5 = 587.33, 659.25, 739.99, 880.00, 987.77
RE6, MI6, FAS6, LA6, SI6 = 1174.66, 1318.51, 1479.98, 1760.00, 1975.53

HERMANAS = ["ichika", "nino", "miku", "yotsuba", "itsuki"]
NOTA = dict(zip(HERMANAS, [RE5, MI5, FAS5, LA5, SI5]))
BRILLO = [RE6, MI6, FAS6, LA6, SI6]


# ------------------------------------------------------------------ audio ---

class Pista:
    def __init__(self, dur):
        self.n = int(dur * SR)
        self.x = np.zeros((self.n, 2))

    def _suma(self, t0, onda, pan):
        i = int(t0 * SR)
        onda = onda[: max(0, self.n - i)]
        self.x[i:i + len(onda), 0] += onda * (1.0 - pan) ** 0.5
        self.x[i:i + len(onda), 1] += onda * pan ** 0.5

    def campana(self, f, t0, amp=0.5, cola=1.6, pan=0.5):
        """Campanita tipo celesta: parciales que se apagan a distinto ritmo."""
        t = np.arange(int(cola * 3 * SR)) / SR
        onda = np.zeros_like(t)
        for mult, peso, vida in [(1.0, 1.0, 1.0), (2.0, 0.32, 0.55),
                                 (3.0, 0.10, 0.30), (4.02, 0.05, 0.18)]:
            onda += peso * np.sin(2 * np.pi * f * mult * t) * np.exp(-t / (cola * vida / 3.0))
        ataque = np.minimum(1.0, t / 0.004)
        self._suma(t0, onda * ataque * amp, pan)

    def colchon(self, notas, t0, dur, amp=0.10):
        """Acorde sostenido muy suave, con entrada y salida lentas."""
        t = np.arange(int(dur * SR)) / SR
        onda = np.zeros_like(t)
        for f in notas:
            onda += np.sin(2 * np.pi * f * t) + 0.6 * np.sin(2 * np.pi * f * 1.004 * t + 1.0)
        env = np.minimum(1.0, t / 0.9) * np.minimum(1.0, (dur - t) / 1.4)
        self._suma(t0, onda / len(notas) * env * amp, 0.5)

    def escalera(self, t0, paso, amp=0.16):
        """Cinco notas agudas: las cinco flores encendiendose."""
        for i, f in enumerate(BRILLO):
            self.campana(f, t0 + i * paso, amp, cola=0.9, pan=0.25 + 0.125 * i)

    def render(self):
        rng = np.random.default_rng(5)
        t = np.arange(int(1.8 * SR)) / SR
        sala = rng.standard_normal((len(t), 2)) * np.exp(-t / 0.42)[:, None]
        sala[: int(0.012 * SR)] = 0
        humedo = np.stack([fftconvolve(self.x[:, c], sala[:, c])[: self.n] for c in (0, 1)], axis=1)
        humedo /= (np.abs(humedo).max() + 1e-9)
        y = self.x / (np.abs(self.x).max() + 1e-9) * 0.80 + humedo * 0.22
        fin = np.minimum(1.0, (self.n - np.arange(self.n)) / (0.35 * SR))
        y *= fin[:, None]
        return y / np.abs(y).max() * 10 ** (-3.0 / 20.0)


def j_capitulo(examen=False):
    r = RITMOS["largo"]
    p = Pista(8.2 if examen else 6.8)
    p.colchon([RE3, LA3, FAS4], 0.0, 5.6)
    p.campana(RE4, r["numero"], 0.45, cola=2.2)
    for i, h in enumerate(HERMANAS):
        p.campana(NOTA[h], r["hermanas"] + i * r["paso"], 0.50, pan=0.2 + 0.15 * i)
    for i, f in enumerate([RE5, FAS5, LA5]):
        p.campana(f, r["titulo"] + i * 0.06, 0.42, cola=2.0)
    p.campana(RE4, r["titulo"], 0.30, cola=2.4)
    p.campana(RE6, r["cinta"], 0.36, cola=1.4)
    if not examen:
        p.escalera(r["flores"], r["paso_flor"])
        return p
    c = r["cambio"]
    p.colchon([LA3, MI5 / 2, LA4], c - 0.2, 3.4, 0.09)
    for i, f in enumerate([LA4, RE5, MI5]):          # suspension: algo empieza
        p.campana(f, c + i * 0.05, 0.46, cola=1.6)
    for i, f in enumerate([RE5, FAS5, LA5, RE6]):    # y resuelve, mas brillante
        p.campana(f, c + 0.45 + i * 0.05, 0.50, cola=2.2)
    p.escalera(c + 0.45, r["paso_flor"])
    return p


def j_fin():
    r = RITMOS["medio"]
    p = Pista(6.2)
    p.colchon([RE3, LA3, FAS4], 0.0, 5.4, 0.09)
    p.campana(LA4, r["numero"], 0.40, cola=2.4)
    p.campana(RE5, r["titulo"], 0.42, cola=2.2)
    p.campana(FAS5, r["titulo"] + 0.07, 0.42, cola=2.2)
    p.campana(LA5, r["cinta"], 0.38, cola=1.8)
    for i, f in enumerate([SI5, LA5, FAS5, MI5, RE5]):   # baja y descansa: nana
        p.campana(f, r["flores"] + i * r["paso_flor"], 0.44, cola=2.0, pan=0.8 - 0.15 * i)
    for f in [RE4, LA4, RE5]:
        p.campana(f, r["flores"] + 5 * r["paso_flor"] + 0.25, 0.34, cola=2.8)
    return p


def j_hub():
    r = RITMOS["corto"]
    p = Pista(3.8)
    p.colchon([RE3, LA3, FAS4], 0.0, 3.0, 0.08)
    p.campana(LA4, r["numero"], 0.40, cola=1.6)
    p.campana(RE5, r["titulo"], 0.44)
    p.campana(LA5, r["titulo"] + 0.06, 0.44)
    p.campana(RE6, r["cinta"], 0.34, cola=1.2)
    p.escalera(r["flores"], r["paso_flor"], 0.14)
    return p


def j_hermana(h):
    r = RITMOS["corto"]
    f = NOTA[h]
    p = Pista(3.8)
    p.colchon([RE3, LA3], 0.0, 3.0, 0.07)
    p.campana(RE4, r["numero"], 0.36, cola=1.8)
    p.campana(f, r["hermanas"], 0.52, cola=1.8)          # su nota
    p.campana(f * 2, r["hermanas"] + 0.05, 0.20, cola=1.2)
    p.campana(f, r["titulo"], 0.40)
    p.campana(f * 1.5, r["titulo"] + 0.06, 0.40)         # su nota + la quinta
    p.campana(RE6, r["cinta"], 0.30, cola=1.2)
    i = HERMANAS.index(h)
    p.campana(BRILLO[i], r["flores"] + i * r["paso_flor"], 0.20, cola=0.9)
    return p


def guardar(pista, nombre, ffmpeg):
    carpeta = os.path.join(GAME, "audio", "sfx")
    wav = os.path.join(carpeta, nombre + ".wav")
    ogg = os.path.join(carpeta, nombre + ".ogg")
    wavfile.write(wav, SR, (pista.render() * 32767).astype(np.int16))
    if ffmpeg is None:
        print("  (sin ffmpeg: queda en .wav)", wav)
        return
    subprocess.run([ffmpeg, "-v", "error", "-y", "-i", wav, "-c:a", "libvorbis", "-q:a", "5", ogg],
                   check=True)
    os.remove(wav)
    print("  ", os.path.relpath(ogg, GAME))


# ------------------------------------------------------------------ cinta ---

def cinta():
    """Cinta blanca de 600x72 con el extremo derecho en cola de golondrina."""
    W, H, S = 600, 72, 4
    im = Image.new("RGBA", (W * S, H * S), (255, 255, 255, 0))
    d = ImageDraw.Draw(im)
    w, h, r, cola = W * S, H * S, 20 * S, 34 * S
    d.rounded_rectangle([0, 0, w - cola, h - 1], radius=r, fill=(255, 255, 255, 255))
    d.rectangle([r, 0, w - cola, h - 1], fill=(255, 255, 255, 255))
    d.polygon([(w - cola, 0), (w - 1, 0), (w - cola // 2 - 2 * S, h // 2), (w - 1, h - 1),
               (w - cola, h - 1)], fill=(255, 255, 255, 255))
    # dos pespuntes finos: al teñir quedan un punto mas oscuros que la cinta
    for y in (9 * S, h - 10 * S):
        d.line([(r, y), (w - cola - 6 * S, y)], fill=(255, 255, 255, 150), width=2 * S)
    im = im.resize((W, H), Image.LANCZOS)
    ruta = os.path.join(GAME, "ui", "cort_cinta.png")
    im.save(ruta)
    print("  ", os.path.relpath(ruta, GAME))


if __name__ == "__main__":
    ffmpeg = shutil.which("ffmpeg")
    print("Cinta:")
    cinta()
    print("Sonidos:")
    guardar(j_capitulo(), "cort_capitulo", ffmpeg)
    guardar(j_capitulo(examen=True), "cort_examen", ffmpeg)
    guardar(j_fin(), "cort_fin", ffmpeg)
    guardar(j_hub(), "cort_hub", ffmpeg)
    for h in HERMANAS:
        guardar(j_hermana(h), "cort_hermana_" + h, ffmpeg)
    if ffmpeg is None:
        sys.exit("ffmpeg no esta en el PATH: convierte los .wav a .ogg a mano.")
