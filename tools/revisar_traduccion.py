"""Revisor automático de las traducciones de The Fifth Choice (solo biblioteca estándar).

Recorre game/tl/<idioma>/ y reporta:
  vacia       la traducción está vacía
  identica    la traducción es igual al español (salvo «...», nombres y palabras que no cambian)
  larga       diálogo u opción de menú de más de 100 caracteres visibles ([mc] cuenta como «Futaro»)
  menu        opción de menú más larga que la española (debe caber en su botón)
  etiquetas   [interpolaciones] o {etiquetas} distintas del original (cantidad u orden)
  sentencia   cambió el personaje o lo que va fuera de las comillas (with, id, etc.)
  glosario    término escrito distinto de docs/GLOSARIO_EN.md
  nombre      nombre propio mal escrito o «Futaro» fijo donde el español usa [mc]

Uso:
  python tools/revisar_traduccion.py            # english
  python tools/revisar_traduccion.py russian    # glosario y nombres solo si hay reglas para ese idioma
  python tools/revisar_traduccion.py --autotest
Sale con código 1 si hay avisos.
"""

import re
import sys
from collections import defaultdict
from pathlib import Path

GAME = Path(__file__).resolve().parent.parent / "The Fifth Choice" / "game"
MAX_CARACTERES = 100

RE_BLOQUE = re.compile(r'^translate (\w+) (\w+):\s*$')
RE_CADENA = re.compile(r'"((?:[^"\\]|\\.)*)"')
RE_OPCION = re.compile(r'^\s*"(?:[^"\\]|\\.)*"(\s+if\s+.+)?:\s*$')
# Etiquetas {…} e interpolaciones […]; {{ y [[ son llaves literales y {#…} son notas del traductor.
RE_ETIQUETA = re.compile(r'\{(?!\{)[^{}]*\}|\[(?!\[)[^\[\]]*\]')

# Palabras que se escriben igual en español y en el idioma destino: una línea hecha solo de ellas
# puede quedar idéntica sin ser un olvido.
IGUALES = {"no", "ok", "extras", "futaro", "uesugi", "ichika", "nino", "miku", "yotsuba", "itsuki",
           "nakano", "raiha", "isanari", "maruo", "asaba", "tsk", "combo", "auto", "escape", "ctrl", "d",
           "pad", "sticks", "a", "the", "fifth", "choice", "h", "min", "s", "m", "cm", "mm", "l", "dl"}

# Reglas por idioma: (expresión regular, forma correcta según el glosario).
GLOSARIO = {
    "english": [
        (r"-(kun|san|chan|sama)\b|\b(senpai|sensei|onii)\b", "sin honoríficos (§3)"),
        (r"\bprotagonist\b", "«main character» (§14.4)"),
        (r"\b(Mr\.?|Mister) Maruo\b", "nadie dice «Mr. Maruo»: «sir» (§15.1)"),
        (r"\b(Miss|Ms\.?|Mrs\.?) Nakano\b", "«Nakano.» a secas (§2)"),
        (r"\bAsaba (Academy|Institute|High School)\b", "«Asaba High» (§2)"),
        (r"\b(headset|earphones|earbuds)\b", "«headphones» (§5)"),
        (r"\bchronometer\b", "«stopwatch» (§5)"),
        (r"\b(report sheet|grade report|grade sheet|bulletin)\b", "«report card» (§4, §15.2)"),
        (r"\bShopping (Center|Centre)\b|\bthe mall\b(?=.*Shopping)", "«Shopping Mall» (§5)"),
        (r"\bRehearsal (Hall|Studio)\b", "«Rehearsal Room» (§5)"),
        (r"\bQuintuplets?\S*\+|\+Tutor|(?<!Team )Quintuplets \+ Tutor|Quintuplet \+",
         "«Team Quintuplets + Tutor!» (§5)"),
        (r"\b(colour\w*|favourite\w*|favour\w*|flavour\w*|honour\w*|behaviour\w*|neighbour\w*|centre\w*"
         r"|theatre\w*|(real|recogn|apolog|organ|memor|critic)is(e|ed|es|ing)|practis(e|ed|es|ing)"
         r"|mum|mums|grey|travell\w*|cancell(ed|ing)|programme\w*|learnt|spelt|whilst|maths)\b",
         "inglés americano (§7)"),
    ],
}
NOMBRES = {
    "english": ["Futaro", "Uesugi", "Ichika", "Nino", "Miku", "Yotsuba", "Itsuki", "Nakano", "Raiha",
                "Isanari", "Maruo", "Asaba"],
}
# Palabras reales parecidas a un nombre (distancia de edición pequeña) que no son erratas.
NO_SON_NOMBRES = {"english": {"nine", "mike", "maru", "nina", "mika", "milk", "mine", "nano", "mind",
                              "kind", "find", "wind", "mile"}}
# [mc]/[nombre_jugador] puede aparecer sin estar en el español cuando allí va «hermanito» o «Futaro» fijo
# (glosario §3, §12.2 y §13.7).
RE_MC_SIN_ORIGINAL = re.compile(r"hermanit|futaro", re.I)


def etiquetas(texto):
    """Etiquetas e interpolaciones en orden; !tc cuenta como !t (glosario §16.2)."""
    salida = []
    for e in RE_ETIQUETA.findall(texto.replace("{{", "").replace("[[", "")):
        if e.startswith("{#"):
            continue
        if e.startswith("[") and "!" in e:
            nombre, flags = e[1:-1].split("!", 1)
            e = "[%s!%s]" % (nombre, flags.replace("c", ""))
        salida.append(e)
    return salida


def visible(texto):
    """Texto tal como sale en pantalla, para medir y comparar."""
    t = texto.replace('\\"', '"').replace("{{", "\0").replace("[[", "\1")
    t = re.sub(r"\{[^{}]*\}", "", t)
    t = re.sub(r"\[[^\[\]]*\]", "Futaro", t)
    return t.replace("\0", "{").replace("\1", "[")


def distancia(a, b):
    previa = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        fila = [i]
        for j, cb in enumerate(b, 1):
            fila.append(min(previa[j] + 1, fila[j - 1] + 1, previa[j - 1] + (ca != cb)))
        previa = fila
    return previa[-1]


def leer(ruta, idioma):
    """Devuelve las entradas de un archivo tl: diálogo (bloques) y cadenas (old/new)."""
    entradas, bloque, es = [], None, None
    for n, linea in enumerate(ruta.read_text(encoding="utf-8-sig").splitlines(), 1):
        m = RE_BLOQUE.match(linea)
        if m:
            # Las etiquetas *_prueba solo se abren desde la consola y no se traducen (plan, tarea B).
            bloque = None if m.group(1) != idioma or "prueba" in m.group(2) else m.group(2)
            es = None
            continue
        s = linea.strip()
        if not s or bloque is None or bloque in ("python", "style"):
            continue
        if bloque == "strings":
            if s.startswith("old "):
                es = RE_CADENA.search(s).group(1)
            elif s.startswith("new ") and es is not None:
                entradas.append(dict(tipo="cadena", ruta=ruta, linea=n, es=es,
                                     en=RE_CADENA.search(s).group(1), sent_es="", sent_en=""))
                es = None
        elif s.startswith("#"):
            es = s[1:].strip()
        elif es is not None:
            me, mi = RE_CADENA.search(es), RE_CADENA.search(s)
            if me and mi:
                entradas.append(dict(tipo="dialogo", ruta=ruta, linea=n, es=me.group(1),
                                     en=mi.group(1), sent_es=RE_CADENA.sub('""', es),
                                     sent_en=RE_CADENA.sub('""', s)))
            es = None
    return entradas


_opciones = None


def es_opcion_de_menu(texto):
    """Por texto y no por línea: los «# game/…:N» de tl/ se desfasan cuando cambia el .rpy."""
    global _opciones
    if _opciones is None:
        _opciones = {RE_CADENA.search(l).group(1)
                     for ruta in GAME.glob("*.rpy")
                     for l in ruta.read_text(encoding="utf-8-sig").splitlines() if RE_OPCION.match(l)}
    return texto in _opciones


def revisar(e, idioma):
    """Lista de (tipo, detalle) para una entrada."""
    avisos = []
    es, en = e["es"], e["en"]
    vis_es, vis_en = visible(es), visible(en)
    motor = e["ruta"].name == "common.rpy"  # cadenas del motor: el original ya está en inglés

    if es.strip() and not en.strip():
        return [("vacia", "")]
    palabras = re.findall(r"[^\W\d_]+", vis_es.lower().replace("futaro", " "))
    if en == es and not motor and any(p not in IGUALES for p in palabras):
        avisos.append(("identica", ""))

    opcion = e["tipo"] == "cadena" and es_opcion_de_menu(es)
    if (e["tipo"] == "dialogo" or opcion) and len(vis_en) > MAX_CARACTERES:
        avisos.append(("larga", "%d caracteres" % len(vis_en)))
    if opcion and len(vis_en) > len(vis_es):
        avisos.append(("menu", "%d > %d caracteres" % (len(vis_en), len(vis_es))))

    t_es, t_en = etiquetas(es), etiquetas(en)
    if e["tipo"] == "cadena":  # en las cadenas de interfaz los huecos pueden cambiar de sitio (glosario §1)
        t_es, t_en = sorted(t_es), sorted(t_en)
    if t_es != t_en:
        sobra_mc = [t for t in t_en if t in ("[mc]", "[nombre_jugador]")]
        sin_mc = [t for t in t_en if t not in ("[mc]", "[nombre_jugador]")]
        if not (sobra_mc and sin_mc == t_es and RE_MC_SIN_ORIGINAL.search(es)):
            avisos.append(("etiquetas", "%s → %s" % (" ".join(t_es) or "—", " ".join(t_en) or "—")))
    if e["sent_es"] != e["sent_en"]:
        avisos.append(("sentencia", "%s → %s" % (e["sent_es"], e["sent_en"])))

    for patron, correcto in ([] if motor else GLOSARIO.get(idioma, [])):
        m = re.search(patron, vis_en, re.I)
        if m:
            avisos.append(("glosario", "«%s»: %s" % (m.group(0), correcto)))

    nombres = NOMBRES.get(idioma, [])
    sin_vars = lambda t: re.sub(r"\[[^\[\]]*\]", "", t)
    if "Futaro" in nombres and "Futaro" in sin_vars(en) and "Futaro" not in sin_vars(es):
        avisos.append(("nombre", "«Futaro» fijo: usa [mc] (§2)"))
    for palabra in set(re.findall(r"[^\W\d_]+", vis_en)):
        bajo = palabra.lower()
        if bajo in NO_SON_NOMBRES.get(idioma, ()):
            continue
        for nombre in nombres:
            nb = nombre.lower()
            if bajo == nb:
                if palabra not in (nombre, nombre.upper()):
                    avisos.append(("nombre", "«%s» → «%s»" % (palabra, nombre)))
            elif bajo != nb + "s" and palabra[0].isupper() and \
                    distancia(bajo, nb) <= (1 if len(nb) <= 5 else 2):
                avisos.append(("nombre", "«%s» → ¿«%s»?" % (palabra, nombre)))
    return avisos


def main(idioma):
    carpeta = GAME / "tl" / idioma
    if not carpeta.is_dir():
        print("No existe %s" % carpeta)
        return 2
    if idioma not in GLOSARIO:
        print("Aviso: no hay reglas de glosario ni de nombres para «%s»; solo se revisa la estructura.\n" % idioma)
    total, por_tipo, entradas = 0, defaultdict(int), 0
    for ruta in sorted(carpeta.glob("*.rpy")):
        for e in leer(ruta, idioma):
            entradas += 1
            for tipo, detalle in revisar(e, idioma):
                total += 1
                por_tipo[tipo] += 1
                print("%s:%d  [%s] %s" % (ruta.relative_to(GAME.parent), e["linea"], tipo, detalle))
                print("    ES: %s\n    %s: %s" % (e["es"], idioma[:2].upper(), e["en"]))
    print("\n%d entradas revisadas, %d avisos" % (entradas, total) +
          (": " + ", ".join("%s %d" % kv for kv in sorted(por_tipo.items())) if total else "."))
    return 1 if total else 0


def autotest():
    def e(es, en, tipo="dialogo", sent_es='mc ""', sent_en='mc ""'):
        return dict(tipo=tipo, ruta=Path("x.rpy"), linea=1, es=es, en=en,
                    sent_es=sent_es, sent_en=sent_en)

    def tipos(es, en, **kw):
        return [t for t, _ in revisar(e(es, en, **kw), "english")]

    assert tipos("Hola, [mc].", "Hi, [mc].") == []
    assert tipos("Hola, [mc].", "Hi.") == ["etiquetas"]
    assert tipos("{i}Sí{/i}", "Yes{/i}") == ["etiquetas"]
    assert tipos("Quedan [t!t]", "[t!tc] left") == []
    assert tipos("{} de [x]", "[x]'s {}", tipo="cadena", sent_es="", sent_en="") == []
    assert tipos("{} de [x]", "[x]'s {}") == ["etiquetas"]
    assert tipos("¡Hermanito!", "[mc]!") == []
    assert tipos("Casa de Futaro", "[nombre_jugador]'s House") == []
    assert tipos("Hola.", "Hola.") == ["identica"]
    assert tipos("...", "...") == [] and tipos("Itsuki.", "Itsuki.") == []
    assert tipos("Hola.", "") == ["vacia"]
    assert tipos("Hola.", "x" * 101) == ["larga"]
    assert tipos("Hola.", "Hi.", sent_en='miku ""') == ["sentencia"]
    assert tipos("Gracias.", "Thanks, Yotsuba-chan.") == ["glosario"]
    assert tipos("Mi color.", "My favourite colour.") == ["glosario"]
    assert tipos("Hola.", "Hi, Yotsubba.") == ["nombre"]
    assert tipos("Hola.", "Hi, itsuki.") == ["nombre"]
    assert tipos("Hola.", "Hi, Futaro.") == ["nombre"]
    assert tipos("Hola.", "Nine days, Nakanos.") == []
    assert tipos("Cien {{llaves}}", "Hundred {{braces}}") == []
    assert visible("{b}[mc]{/b} {{x}") == "Futaro {x}"
    print("autotest OK")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    if "--autotest" in sys.argv:
        autotest()
    else:
        sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "english"))
