################################################################################
##  10_mj_chibi.rpy — Chibis y globos de texto de los minijuegos (Evento 6)
##
##  Módulo COMPARTIDO por Y2, N1′, It1 (chat 5) y por I1′, M3 (chat 6).
##  No es un minijuego: solo contiene
##    · mj_chibi()          displayable de un chibi (con repuesto si falta el PNG)
##    · mj_chibi_expresion  escalera de expresiones según el progreso
##    · MJGlobo             globo de texto con líneas aleatorias por evento
##    · screens             mj_globo, mj_chibi_vista, mj_retrato
##
##  Arte: game/images/chibis/<hermana>_<expresion>.png  (512x512, RGBA, pies en
##  la fila ~496, eje en el centro). Las cinco hermanas × cinco expresiones:
##  neutral · animo · esfuerzo · triste · feliz   (+ itsuki_mano.png opcional).
##  Mientras no estén los PNG definitivos, los de herramientas/
##  generar_chibis_placeholder.py ocupan su sitio con el mismo nombre.
##
##  Carga: va DESPUÉS de 10_minijuegos.rpy (orden alfabético) y ANTES de los
##  tres minijuegos. No toca el marco.
################################################################################

define MJ_CHIBI_RUTA = "images/chibis/"

## Duración de un globo en pantalla (segundos).
define MJ_GLOBO_DURACION = 2.2

## False (por defecto): la línea de fallo del marco (MJ_FALLOS) la dice el
## marco con renpy.say, como hasta ahora, y el globo del minijuego usa sus
## propias reacciones. True: el globo de la pantalla enseña la línea de
## MJ_FALLOS en el momento de perder — pide el parche de 2 líneas en
## mj_linea_fallo() (ver CAP1_evento_6_CHAT5_INFORME.md) o se dice dos veces.
define MJ_FALLO_EN_GLOBO = False


################################################################################
##  LÍNEAS DE LOS GLOBOS
##  Evento → lista de líneas; se elige una al azar sin repetir la anterior.
##  Eventos usados: inicio · acierto · racha · mitad · casi · fallo · caida ·
##  falsa · lista · sexto · tiempo · paso · ayuda · tras_ayuda · final
##  Ichika y Miku las escribe el chat 6; mientras tanto vale el genérico.
################################################################################

define MJ_GLOBOS_GENERICO = {
    "inicio":  ["…Vamos."],
    "acierto": ["…Bien."],
    "fallo":   ["…Otra vez."],
    "final":   ["…Listo."],
}

define MJ_GLOBOS = {

    ## Yotsuba: exclamaciones durante el juego (la armadura); en el final
    ## desaparecen, porque ahí dice la verdad.
    "yotsuba": {
        "inicio":  ["¡Vamos, equipo!", "¡Todas juntas!", "¡Listas! ¡Preparadas!"],
        "acierto": ["¡Testigo recibido!", "¡Bien! ¡Siguiente!", "¡Eso! ¡Así se pasa!"],
        "mitad":   ["¡Ya vamos por la mitad!", "¡Mitad de la carrera!"],
        "casi":    ["¡Falta poco! ¡Poquísimo!", "¡Última vuelta! ¡Última, última!"],
        "falsa":   ["¡Ups! ¡Muy pronto!", "¡Esperen! ¡Salí antes!"],
        "caida":   ["¡Ay! ¡El testigo!", "¡Se cayó! ¡Lo recojo!"],
        "fallo":   ["¡Otra vez! ¡Con ganas!", "¡No pasa nada! ¡Otra!"],
        "final":   ["Llegamos. Todas.", "Llegamos todas."],
    },

    ## Nino: corta, seca, sin dejar contestar.
    "nino": {
        "inicio":  ["Tres cosas por lista. Sin perder el tiempo.", "Lee bien. No adivines.", "Lee las etiquetas. Todas."],
        "acierto": ["Esa.", "Bien. Siguiente.", "…Correcto."],
        "lista":   ["Una lista menos.", "Ahí va otra.", "Siguiente. Rápido."],
        "mitad":   ["Vamos bien. No lo celebres."],
        "casi":    ["Falta una. Una."],
        "fallo":   ["Esa no. Lee la etiqueta.", "Tsk. Casi igual no es igual.", "Otra vez. No mires tanto."],
        "tiempo":  ["Se nos acaba el tiempo.", "Rápido. Pero no a lo loco."],
        "sexto":   ["…Queda un hueco. Elige tú.", "Sitio para una cosa más. No me mires."],
        "final":   ["Hecho. Y no lo comentes.", "…Ya está. Vámonos."],
    },

    ## Itsuki: oración cerrada, sujeto-verbo-punto.
    "itsuki": {
        "inicio":     ["Despacio. Paso a paso.", "Revisaré cada paso.", "Empiezo por el principio."],
        "paso":       ["Siguiente paso.", "Anotado.", "Ese paso está hecho."],
        "fallo":      ["El resultado no cuadra.", "Hay un error en alguna parte.", "No cuadra. Otra vez."],
        "tiempo":     ["Queda poco tiempo.", "El tiempo corre."],
        "ayuda":      ["…Profesor. ¿Puede mirar esto?", "Una duda. Solo una."],
        "tras_ayuda": ["Entendido. Lo reviso.", "Ahí. Ahora lo veo."],
        "final":      ["Cuadra. Esta vez cuadra.", "Salió. Lo hice yo."],
    },
}


################################################################################
##  FUNCIONES Y CLASES
################################################################################

init python:

    _mj_chibi_cache = {}

    def mj_chibi_ruta(hermana, expresion):
        return MJ_CHIBI_RUTA + hermana + "_" + expresion + ".png"

    def mj_chibi(hermana, expresion="neutral", zoom=1.0):
        """Displayable de un chibi. Si falta el PNG de esa expresión usa el
        neutral; si falta también, una flor del color de la hermana con su
        inicial (para que el minijuego nunca falle por falta de arte)."""
        clave = (hermana, expresion, zoom)
        if clave in _mj_chibi_cache:
            return _mj_chibi_cache[clave]

        ruta = mj_chibi_ruta(hermana, expresion)
        if not renpy.loadable(ruta):
            ruta = mj_chibi_ruta(hermana, "neutral")

        if renpy.loadable(ruta):
            d = Transform(ruta, zoom=zoom)
        else:
            color = PETALO_COLOR[hermana]
            lado = int(512 * zoom)
            d = Fixed(
                Transform("ui/flor.png", matrixcolor=TintMatrix(color), zoom=(lado / 56.0) * 0.8, align=(0.5, 0.5)),
                Text(hermana[:1].upper(), size=int(150 * zoom), color="#FFFFFF", xalign=0.5, yalign=0.5),
                xysize=(lado, lado))

        _mj_chibi_cache[clave] = d
        return d

    def mj_chibi_expresion(progreso, total, estado=""):
        """Escalera de expresiones del chibi protagonista de un minijuego.
        estado: "" (según progreso) | "triste" | "feliz"."""
        if estado == "feliz":
            return "feliz"
        if estado == "triste":
            return "triste"
        if total <= 0:
            return "neutral"
        f = float(progreso) / float(total)
        if f >= 1.0:
            return "feliz"
        if f >= 0.6:
            return "esfuerzo"
        if f > 0.0:
            return "animo"
        return "neutral"

    def mj_texto_fallo(hermana, fallos_previos):
        """La línea de MJ_FALLOS que el marco diría tras este fallo."""
        lineas = MJ_FALLOS.get(hermana)
        if lineas is None:
            return ""
        i = fallos_previos
        if i >= len(lineas):
            i = len(lineas) - 1
        if i < 0:
            i = 0
        return lineas[i][1]

    class MJGlobo(object):
        """Globo de texto de un chibi. Vive dentro del objeto del minijuego
        (no se guarda). decir(evento) elige una línea al azar."""

        def __init__(self, hermana, duracion=None):
            self.hermana = hermana
            self.duracion = MJ_GLOBO_DURACION
            if duracion is not None:
                self.duracion = duracion
            self.texto = ""
            self.restante = 0.0
            self.espera = 0.0
            self.ultimo = ""

        def poner(self, texto, duracion=None):
            self.texto = texto
            self.ultimo = texto
            self.restante = self.duracion
            if duracion is not None:
                self.restante = duracion
            self.espera = 0.7

        def decir(self, evento, forzar=False):
            tabla = MJ_GLOBOS.get(self.hermana)
            if tabla is None:
                tabla = MJ_GLOBOS_GENERICO
            lineas = tabla.get(evento)
            if lineas is None:
                lineas = MJ_GLOBOS_GENERICO.get(evento)
            if lineas is None:
                return
            if len(lineas) == 0:
                return
            if self.espera > 0.0 and not forzar:
                return
            texto = renpy.random.choice(lineas)
            intentos = 0
            while texto == self.ultimo and len(lineas) > 1 and intentos < 5:
                texto = renpy.random.choice(lineas)
                intentos += 1
            self.poner(texto)

        def avanzar(self, dt):
            if self.restante > 0.0:
                self.restante -= dt
            if self.espera > 0.0:
                self.espera -= dt

        def visible(self):
            return self.restante > 0.0 and self.texto != ""


################################################################################
##  TRANSFORMS
################################################################################

transform mj_chibi_bob:
    yoffset 0
    block:
        ease 0.45 yoffset -8
        ease 0.45 yoffset 0
        repeat

transform mj_chibi_salto:
    yoffset 0
    block:
        ease 0.22 yoffset -34
        ease 0.22 yoffset 0
        pause 0.25
        repeat

transform mj_chibi_tiembla:
    xoffset 0
    block:
        linear 0.05 xoffset -7
        linear 0.05 xoffset 7
        linear 0.05 xoffset -5
        linear 0.05 xoffset 5
        linear 0.05 xoffset 0
        pause 0.35
        repeat

transform mj_globo_entra:
    alpha 0.0
    zoom 0.92
    ease 0.12 alpha 1.0 zoom 1.0


################################################################################
##  SCREENS
################################################################################

## Un chibi con los pies en (x, y). anim: quieto | bob | salto | tiembla.
## x e y SIEMPRE enteros (un float se leería como fracción de pantalla).
screen mj_chibi_vista(hermana, expresion, x, y, zoom=0.34, anim="bob"):

    $ img = mj_chibi(hermana, expresion, zoom)

    if anim == "salto":
        add img at mj_chibi_salto xpos int(x) ypos int(y) xanchor 0.5 yanchor 1.0
    elif anim == "tiembla":
        add img at mj_chibi_tiembla xpos int(x) ypos int(y) xanchor 0.5 yanchor 1.0
    elif anim == "bob":
        add img at mj_chibi_bob xpos int(x) ypos int(y) xanchor 0.5 yanchor 1.0
    else:
        add img xpos int(x) ypos int(y) xanchor 0.5 yanchor 1.0


## Globo de texto con el color de la hermana. (x, y) = punta del globo.
screen mj_globo(texto, hermana, x, y, ancho=520):

    $ color = PETALO_COLOR[hermana]
    $ fondo = ui_mezclar(color, "#FFFFFF", 0.80)
    $ tinta = ui_mezclar(color, "#000000", 0.78)

    frame:
        xpos int(x)
        ypos (int(y) - 20)
        xanchor 0.5
        yanchor 1.0
        xmaximum ancho
        padding (36, 22, 36, 22)
        at mj_globo_entra
        background Fixed(
            Transform(Frame("ui/opcion_neutra.png", 40, 40, 40, 40), matrixcolor=TintMatrix(fondo)),
            Transform(Frame("ui/opcion_marco.png", 40, 40, 40, 40), matrixcolor=TintMatrix(color)))

        text texto:
            size 30
            color tinta
            text_align 0.5
            xalign 0.5
            substitute False

    add Transform(Solid(fondo, xsize=24, ysize=24), rotate=45) xpos int(x) ypos (int(y) - 20) xanchor 0.5 yanchor 0.5


## Chibi protagonista de un minijuego + su globo encima.
screen mj_retrato(hermana, expresion, globo, anim="bob", x=250, y=560, zoom=0.6):

    use mj_chibi_vista(hermana, expresion, x, y, zoom, anim)

    if globo.visible():
        use mj_globo(globo.texto, hermana, x + 40, y - int(500 * zoom) - 8)
