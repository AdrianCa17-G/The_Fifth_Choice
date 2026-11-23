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

## Chibi general (la hermana que acompaña): vive en la columna del marco.
define MJ_CHIBI_X = 180        ## centro horizontal (la más ancha ocupa x 49–311)
define MJ_CHIBI_Y = 1090       ## borde inferior del PNG: los pies quedan en y 1074
define MJ_GLOBO_ANCHO = 300    ## ancho máximo del globo (cabe en la columna)
define MJ_GLOBO_HUECO = 12     ## px entre la punta del globo y la coronilla más alta (lazo de Yotsuba, fila 10)

## False (por defecto): la línea de fallo del marco (MJ_FALLOS) la dice el
## marco con rcenpy.say, como hasta ahora, y el globo del minijuego usa sus
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
    "inicio":  [_("...Vamos.")],
    "acierto": [_("...Bien.")],
    "fallo":   [_("...Otra vez.")],
    "final":   [_("...Listo.")],
}

define MJ_GLOBOS = {

    ## Yotsuba: exclamaciones durante el juego (la armadura); en el final
    ## desaparecen, porque ahí dice la verdad.
    "yotsuba": {
        "inicio":  [_("¡Vamos, equipo!"), _("¡Todas juntas!"), _("¡Listas! ¡Preparadas!")],
        "acierto": [_("¡Testigo recibido!"), _("¡Bien! ¡Siguiente!"), _("¡Eso! ¡Así se pasa!")],
        "mitad":   [_("¡Ya vamos por la mitad!"), _("¡Mitad de la carrera!")],
        "casi":    [_("¡Falta poco! ¡Poquísimo!"), _("¡Última vuelta! ¡Última, última!")],
        "falsa":   [_("¡Ups! ¡Muy pronto!"), _("¡Esperen! ¡Salí antes!")],
        "caida":   [_("¡Ay! ¡El testigo!"), _("¡Se cayó! ¡Lo recojo!")],
        "fallo":   [_("¡Otra vez! ¡Con ganas!"), _("¡No pasa nada! ¡Otra!")],
        "final":   [_("Llegamos. Todas."), _("Llegamos todas.")],
        "racha":   [_("¡Vamos en racha!"), _("¡No paramos!"), _("¡Así, así!")],
        "cura":    [_("¡Testigo nuevo! ¡Gracias, equipo!"), _("¡Recuperado!")],
    },

    ## Nino: corta, seca, sin dejar contestar.
    "nino": {
        "inicio":  [_("Tres cosas por lista. Sin perder el tiempo."), _("Lee bien. No adivines."), _("Lee las etiquetas. Todas.")],
        "acierto": [_("Esa."), _("Bien. Siguiente."), _("...Correcto.")],
        "lista":   [_("Una lista menos."), _("Ahí va otra."), _("Siguiente. Rápido.")],
        "mitad":   [_("Vamos bien. No lo celebres.")],
        "casi":    [_("Falta una. Una.")],
        "fallo":   [_("Esa no. Lee la etiqueta."), _("Tsk. Casi igual no es igual."), _("Otra vez. No mires tanto.")],
        "tiempo":  [_("Se nos acaba el tiempo."), _("Rápido. Pero no a lo loco.")],
        "sexto":   [_("...Queda un hueco. Elige tú."), _("Sitio para una cosa más. No me mires.")],
        "final":   [_("Hecho. Y no lo comentes."), _("...Ya está. Vámonos.")],
        "racha":   [_("Bien. Sigue así."), _("Tres seguidas. No te confíes."), _("Eso. Sin pausas.")],
        "mirar":   [_("Tsk. ¿Ya se te olvidó la lista?"), _("Mírala. Pero eso cuesta tiempo.")],
    },

    ## Itsuki: oración cerrada, sujeto-verbo-punto.
    "itsuki": {
        "inicio":     [_("Despacio. Paso a paso."), _("Revisaré cada paso."), _("Empiezo por el principio.")],
        "paso":       [_("Siguiente paso."), _("Anotado."), _("Ese paso está hecho.")],
        "fallo":      [_("El resultado no cuadra."), _("Hay un error en alguna parte."), _("No cuadra. Otra vez.")],
        "tiempo":     [_("Queda poco tiempo."), _("El tiempo corre.")],
        "ayuda":      [_("...Profesor. ¿Puede mirar esto?"), _("Una duda. Solo una.")],
        "tras_ayuda": [_("Entendido. Lo reviso."), _("Ahí. Ahora lo veo.")],
        "final":      [_("Cuadra. Esta vez cuadra."), _("Salió. Lo hice yo.")],
    },

    ## Miku: «...» al inicio mientras se esconde; cuando se suelta (final) desaparece.
    "miku": {
        "inicio":   [_("...Vale. Empiezo."), _("...Cuento hasta cuatro."), _("...Con los audífonos puestos, sí."), _("...Esto es solo compás.")],
        "acierto":  [_("...Ahí."), _("...Eso."), _("...Sí."), _("...Encaja.")],
        "racha":    [_("...Se oye bien."), _("...Ya casi no pienso."), _("...Sigo, sigo."), _("...Va solo.")],
        "fallo":    [_("...Uy."), _("...Sigo."), _("...Otra nota.")],
        "caida":    [_("...Aguanta."), _("...No te escondas ahora."), _("...Despacio. ...Despacio.")],
        "mitad":    [_("...Se apagaron."), _("...Solo queda el reloj."), _("...Sin música. ...Sigo.")],
        "silencio": [_("...Lo oigo. ...Es el reloj."), _("...El reloj no pide perdón."), _("...Sin audífonos suena igual.")],
        "casi":     [_("...Ya queda poco."), _("...Casi. ...Casi."), _("...No pares ahora.")],
        "final":    [_("Esto sí lo sé."), _("Lo tenía."), _("No me escondí.")],
        "perdida":  [_("...Se me fue el compás."), _("...Perdí el hilo.")],
    },

    ## Ichika: exclamación = máscara; sin exclamación = sincera.
    "ichika": {
        "inicio":    [_("¡Telón! ...Las líneas, una a una."), _("Respira, Ichika. Tú puedes."), _("Me sé el guion. Falta saber cuál es el mío."), _("¡Luces, cámara...!")],
        "actuada":   [_("¡Ta-chán!"), _("¡Qué entrada!"), _("¡Aplausos, por favor!"), _("¡Sonríe, Ichika!")],
        "sincera":   [_("...Eso era mío."), _("Eso salió sin guion."), _("Pesó menos de lo que pensaba."), _("Ya. Lo dije.")],
        "improviso": [_("¡Improviso! ...Me sale solo."), _("Ay. Actué sin querer."), _("Actué sin querer. Otra vez.")],
        "mitad":     [_("Mitad de función. La sonrisa pesa."), _("Ya van varias. ...Sigo."), _("Tres cuartos de sonrisa.")],
        "caida":     [_("La sonrisa se me cae..."), _("Me pesa la cara."), _("Casi me quedo en blanco.")],
        "casi":      [_("La última. Esta no se actúa."), _("Una más. Solo mía."), _("Ya llega la última.")],
        "blanco":    [_("...Me quedé en blanco."), _("Se apagaron las luces."), _("No me sale nada. Ni el chiste.")],
        "final":     [_("Respira. Ya está."), _("Sonreí despacio. ...Mejor."), _("Eso no lo ensayé.")],
        "sinfuerzas": [_("Me quedé sin pilas..."), _("Sin energía. Actúo por inercia."), _("No me da la voz."), _("Necesito un respiro.")],
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

## Reacciones de UNA sola pasada para la chibi general (nada en bucle en el marco).
transform mj_chibi_salto_uno:
    yoffset 0
    ease 0.15 yoffset -26
    ease 0.17 yoffset 0

transform mj_chibi_tiembla_uno:
    xoffset 0
    linear 0.05 xoffset -6
    linear 0.05 xoffset 6
    linear 0.05 xoffset -4
    linear 0.05 xoffset 4
    linear 0.05 xoffset 0

## Entrada y salida del globo (va en el único hijo de un showif).
transform mj_globo_entra:
    on appear, show:
        alpha 0.0
        yoffset 8
        ease 0.18 alpha 1.0 yoffset 0
    on hide:
        ease 0.2 alpha 0.0


################################################################################
##  SCREENS
################################################################################

## Un chibi con los pies en (x, y). anim: quieto | bob | salto | tiembla.
## x e y SIEMPRE enteros (un float se leería como fracción de pantalla).
## alfa: opacidad (el relevo atenúa a las que no llevan el testigo).
screen mj_chibi_vista(hermana, expresion, x, y, zoom=0.34, anim="bob", alfa=1.0):

    $ img = mj_chibi(hermana, expresion, zoom)

    if anim == "salto":
        add img at mj_chibi_salto xpos int(x) ypos int(y) xanchor 0.5 yanchor 1.0 alpha alfa
    elif anim == "tiembla":
        add img at mj_chibi_tiembla xpos int(x) ypos int(y) xanchor 0.5 yanchor 1.0 alpha alfa
    elif anim == "bob":
        add img at mj_chibi_bob xpos int(x) ypos int(y) xanchor 0.5 yanchor 1.0 alpha alfa
    else:
        add img xpos int(x) ypos int(y) xanchor 0.5 yanchor 1.0 alpha alfa


## Globo de texto con el color de la hermana. (x, y) = punta del globo.
## Se dibuja siempre; quien lo use decide cuándo (mj_retrato lo envuelve en showif).
screen mj_globo(texto, hermana, x, y, ancho=MJ_GLOBO_ANCHO):

    $ color = PETALO_COLOR[hermana]
    $ fondo = ui_mezclar(color, "#FFFFFF", 0.80)
    $ tinta = ui_mezclar(color, "#000000", 0.78)

    frame:
        xpos int(x)
        ypos (int(y) - 17)
        xanchor 0.5
        yanchor 1.0
        xmaximum ancho
        padding (28, 18, 28, 18)
        background Fixed(
            Transform(Frame("ui/opcion_neutra.png", 40, 40, 40, 40), matrixcolor=TintMatrix(fondo)),
            Transform(Frame("ui/opcion_marco.png", 40, 40, 40, 40), matrixcolor=TintMatrix(color)))

        text __(texto):
            style "mj_globo_texto"
            color tinta
            text_align 0.5
            xalign 0.5
            substitute False

    add Transform(Solid(fondo, xsize=24, ysize=24), rotate=45) xpos int(x) ypos (int(y) - 17) xanchor 0.5 yanchor 0.5


## Chibi general de un minijuego + su globo encima. Por defecto vive en la
## columna del marco (lo normal es pasarla a mj_marco con chibi=/globo=/anim=).
## anim: "salto" y "tiembla" = una reacción; cualquier otro valor = quieta.
screen mj_retrato(hermana, expresion, globo, anim="quieto", x=MJ_CHIBI_X, y=MJ_CHIBI_Y, zoom=1.0):

    $ img = mj_chibi(hermana, expresion, zoom)
    $ punta = int(y) - int(502 * zoom) - MJ_GLOBO_HUECO

    if anim == "salto":
        add img at mj_chibi_salto_uno xpos int(x) ypos int(y) xanchor 0.5 yanchor 1.0
    elif anim == "tiembla":
        add img at mj_chibi_tiembla_uno xpos int(x) ypos int(y) xanchor 0.5 yanchor 1.0
    else:
        add img xpos int(x) ypos int(y) xanchor 0.5 yanchor 1.0

    if globo is not None:
        showif globo.visible():
            fixed:
                at mj_globo_entra
                use mj_globo(globo.texto, hermana, x, punta)
