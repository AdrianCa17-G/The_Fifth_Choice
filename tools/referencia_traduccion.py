"""Pone, junto a cada hueco de game/tl/<destino>/, la línea ya traducida de game/tl/<referencia>/
como comentario (solo biblioteca estándar).

Para traductores que trabajan desde el inglés: las plantillas de Ren'Py solo traen el español.
  diálogo  se empareja por el id del bloque («translate turkish prologo_13fe8e7a»)
  cadenas  se empareja por el texto «old» (las cadenas son globales en Ren'Py)

El comentario va justo encima del hueco:
    # narrador "Hay dos clases de personas en este mundo."
    # english: narrador "There are two kinds of people in this world."
    narrador "Hay dos clases de personas en este mundo."

Se puede ejecutar las veces que haga falta: borra los comentarios «# <referencia>:» de antes y los
vuelve a poner con el texto actual de la referencia. Respeta BOM y saltos de línea de cada archivo.

Uso:
  python tools/referencia_traduccion.py turkish            # referencia: english
  python tools/referencia_traduccion.py russian english
  python tools/referencia_traduccion.py --autotest
Sale con código 1 si queda algún hueco sin referencia.
"""

import re
import sys
from pathlib import Path

GAME = Path(__file__).resolve().parent.parent / "The Fifth Choice" / "game"

RE_BLOQUE = re.compile(r'^translate (\w+) (\w+):\s*$')


def leer_referencia(lineas, idioma):
    """{id de bloque: [sentencias]} y {texto old: 'new "…"'} de un archivo tl de referencia."""
    dialogo, cadenas, bloque, old = {}, {}, None, None
    for linea in lineas:
        m = RE_BLOQUE.match(linea)
        if m:
            bloque = m.group(2) if m.group(1) == idioma else None
            old = None
            continue
        s = linea.strip()
        if bloque is None or not s or s.startswith("#") or bloque in ("python", "style"):
            continue
        if bloque == "strings":
            if s.startswith("old "):
                old = s[4:]
            elif s.startswith("new ") and old is not None:
                cadenas[old] = s[4:]
                old = None
        else:
            dialogo.setdefault(bloque, []).append(s)
    return dialogo, cadenas


def anotar(lineas, idioma, ref, dialogo, cadenas):
    """Devuelve (líneas anotadas, huecos, huecos sin referencia). Las líneas conservan su fin de línea."""
    marca = "# %s:" % ref
    salida, bloque, old, pendiente = [], None, None, False
    huecos = sin_ref = 0
    for linea in lineas:
        if linea.strip().startswith(marca):
            continue  # comentario de una pasada anterior: se rehace
        fin = linea[len(linea.rstrip("\r\n")):] or "\n"
        m = RE_BLOQUE.match(linea)
        if m:
            bloque = m.group(2) if m.group(1) == idioma else None
            old, pendiente = None, bloque not in (None, "strings", "python", "style")
            salida.append(linea)
            continue
        s = linea.strip()
        sangria = linea[:len(linea) - len(linea.lstrip())]
        if bloque == "strings" and s.startswith("old "):
            old = s[4:]
        elif bloque == "strings" and s.startswith("new ") and old is not None:
            huecos += 1
            if old in cadenas:
                salida.append("%s%s %s%s" % (sangria, marca, cadenas[old], fin))
            else:
                sin_ref += 1
            old = None
        elif pendiente and s and not s.startswith("#"):
            # Primera sentencia del bloque de diálogo: el hueco.
            huecos += 1
            pendiente = False
            for sentencia in dialogo.get(bloque, []):
                salida.append("%s%s %s%s" % (sangria, marca, sentencia, fin))
            if bloque not in dialogo:
                sin_ref += 1
        salida.append(linea)
    return salida, huecos, sin_ref


def leer_lineas(ruta):
    with open(ruta, encoding="utf-8-sig", newline="") as f:
        return f.read().splitlines(keepends=True)


def main(destino, ref):
    carpeta, carpeta_ref = GAME / "tl" / destino, GAME / "tl" / ref
    for c in (carpeta, carpeta_ref):
        if not c.is_dir():
            print("No existe %s" % c)
            return 2
    dialogo, cadenas = {}, {}
    for ruta in sorted(carpeta_ref.glob("*.rpy")):
        d, c = leer_referencia(leer_lineas(ruta), ref)
        dialogo.update(d)
        cadenas.update(c)

    total = total_sin = 0
    for ruta in sorted(carpeta.glob("*.rpy")):
        lineas = leer_lineas(ruta)
        nuevas, huecos, sin_ref = anotar(lineas, destino, ref, dialogo, cadenas)
        total, total_sin = total + huecos, total_sin + sin_ref
        if nuevas != lineas:
            bom = ruta.read_bytes().startswith(b"\xef\xbb\xbf")
            with open(ruta, "w", encoding="utf-8-sig" if bom else "utf-8", newline="") as f:
                f.write("".join(nuevas))
        if sin_ref:
            print("%s: %d huecos sin referencia" % (ruta.name, sin_ref))
    print("%d huecos en tl/%s, %d sin referencia de tl/%s." % (total, destino, total_sin, ref))
    return 1 if total_sin else 0


def autotest():
    ref = ['translate english a_1:\n', '\n', '    # mc "Hola."\n', '    mc "Hi."\n', '\n',
           'translate english strings:\n', '\n', '    old "Sí"\n', '    new "Yes"\n']
    dest = ['translate turkish a_1:\n', '\n', '    # mc "Hola."\n', '    mc "Hola."\n', '\n',
            'translate turkish b_2:\n', '\n', '    # mc "Nada."\n', '    mc "Nada."\n', '\n',
            'translate turkish strings:\n', '\n', '    # game/x.rpy:1\n', '    old "Sí"\n',
            '    new "Sí"\n']
    d, c = leer_referencia(ref, "english")
    assert d == {"a_1": ['mc "Hi."']} and c == {'"Sí"': '"Yes"'}, (d, c)
    una, huecos, sin = anotar(dest, "turkish", "english", d, c)
    assert (huecos, sin) == (3, 1), (huecos, sin)
    assert una[3] == '    # english: mc "Hi."\n' and una[4] == '    mc "Hola."\n', una
    assert '    # english: "Yes"\n' in una and una.index('    # english: "Yes"\n') == len(una) - 2
    dos, _, _ = anotar(una, "turkish", "english", d, c)
    assert dos == una, "la segunda pasada no debe cambiar nada"
    crlf, _, _ = anotar([l.replace("\n", "\r\n") for l in dest], "turkish", "english", d, c)
    assert crlf[3] == '    # english: mc "Hi."\r\n'
    print("autotest OK")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    if "--autotest" in sys.argv:
        autotest()
    elif len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    else:
        sys.exit(main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "english"))
