################################################################################
##  10_mj_ichika.rpy — I1′ · La máscara se cansa (Ichika)
##  Cada línea: «Actuada» (toque, sube la máscara) o «Sincera» (mantener, baja).
##  Máscara al 100 % = se queda en blanco. Sin elegir a tiempo, improvisa
##  (cuenta como actuada). La última línea solo puede ser sincera y no tiene prisa.
################################################################################

## (actuada, sincera). None = esa línea no se puede actuar. Del anexo de bloques A.
define I1_LINEAS = [
    ("¡Llegué justo a tiempo! ¡Siempre llego justo a tiempo!", "Llevo toda la semana llegando justa."),
    ("Estoy bien. Que conste.", "Estoy cansada."),
    ("¡Dormir es para los débiles!", "Necesito dormir."),
    ("¡Una audición más, y otra, y otra!", "Me da miedo que no salga ninguna."),
    ("¡El público me adora, aunque esté vacío!", "A veces actúo para una sala vacía."),
    ("Tengo tres formas de decir que sí.", "Digo que sí antes de pensarlo."),
    ("¡Los dragones no se cansan!", "Yo sí."),
    ("¡Mi risa es mi mejor entrada!", "A veces me río para no contestar."),
    ("Pregúntame lo que quieras. Contestaré con un chiste.", "Pregúntame dos veces."),
    ("¡Hoy no me cuesta nada!", "Hoy me cuesta mucho."),
    ("¡Puedo con todo!", "No sé hasta cuándo."),
    (None, "No tengo que poder con todo."),
]

## Líneas (1-based) que se quitan al bajar de nivel. La 12 nunca.
define I1_QUITAR = [4, 8, 5, 10, 3, 9, 2, 6]
define I1_MASCARA_INICIAL = 20.0
define I1_MASCARA_REINICIO = 35.0     ## máscara al reanudar desde un punto de control
define I1_PAUSA_RESPUESTA = 0.55


init python:

    import time

    def i1_seleccionar(n):
        """Las n líneas del nivel actual (siempre incluye la última)."""
        total = len(I1_LINEAS)
        quitar = total - n
        if quitar < 0:
            quitar = 0
        fuera = []
        for num in I1_QUITAR:
            if len(fuera) < quitar:
                fuera.append(num)
        res = []
        for i in range(total):
            if (i + 1) not in fuera:
                res.append(I1_LINEAS[i])
        return res

    class MJI1(object):
        """Estado vivo de un intento. Estados: listo | linea | resp | fin."""

        def __init__(self, params, inicio):
            self.globo = MJGlobo("ichika")
            self.lineas = i1_seleccionar(int(params["lineas"]))
            self.n = len(self.lineas)
            self.i = int(inicio)
            if self.i > self.n - 1:
                self.i = self.n - 1
            if self.i < 0:
                self.i = 0
            self.sube = float(params["mascara_actuada"])
            self.baja = float(params["mascara_sincera"])
            self.mantener = float(params["mantener"])
            self.tlinea = float(params["tiempo_linea"])
            if self.i > 0:
                self.mascara = I1_MASCARA_REINICIO
            else:
                self.mascara = I1_MASCARA_INICIAL

            self.estado = "listo"
            self.restante = self.tlinea
            self.sostenido = 0.0
            self.sosteniendo = False
            self.sobre = None
            self.pausa = 0.0
            self.flash = 0.0
            self.aviso = ""
            self.aviso_t = 0.0
            self.respuesta = ""
            self.actuadas = 0
            self.sinceras = 0
            self.aviso_mitad = False
            self.aviso_alta = False
            self.resultado = None
            self.t_fin = 0.0
            self.ultimo = time.perf_counter()

        def linea_actual(self):
            return self.lineas[self.i]

        def es_ultima(self):
            return self.i >= self.n - 1

        def empezar(self):
            if self.estado != "listo":
                return None
            self.estado = "linea"
            self.restante = self.tlinea
            self.ultimo = time.perf_counter()
            self.globo.decir("inicio", True)
            return None

        ## --- Entradas ------------------------------------------------------------

        def actuada(self):
            if self.estado != "linea":
                return None
            if self.linea_actual()[0] is None:
                return None
            self.resolver("actuada")
            return None

        def sincera_inicio(self):
            if self.estado != "linea":
                return None
            if self.sosteniendo:
                return None
            self.sosteniendo = True
            self.sostenido = 0.0
            return None

        def sincera_fin(self):
            if self.sosteniendo and self.estado == "linea":
                self.sosteniendo = False
                self.sostenido = 0.0
                self.aviso = "Mantén un poco más."
                self.aviso_t = 0.8
            return None

        def set_sobre(self, valor):
            self.sobre = valor
            return None

        def mouse_down(self):
            if self.sobre == "s":
                self.sincera_inicio()
            return None

        def mouse_up(self):
            self.sincera_fin()
            return None

        ## --- Lógica --------------------------------------------------------------

        def resolver(self, modo):
            self.sosteniendo = False
            self.sostenido = 0.0
            if modo == "sincera":
                self.mascara -= self.baja
                if self.mascara < 0.0:
                    self.mascara = 0.0
                self.sinceras += 1
                self.respuesta = "sincera"
                self.globo.decir("sincera")
            else:
                self.mascara += self.sube
                self.actuadas += 1
                if modo == "auto":
                    self.respuesta = "improviso"
                    self.globo.decir("improviso", True)
                else:
                    self.respuesta = "actuada"
                    self.globo.decir("actuada")
            self.estado = "resp"
            self.pausa = I1_PAUSA_RESPUESTA
            self.flash = 0.5
            if self.mascara >= 100.0:
                self.mascara = 100.0
                self.terminar("perdido")
            elif self.es_ultima():
                self.terminar("ganado")

        def terminar(self, res):
            self.estado = "fin"
            prog = self.i
            if res == "ganado":
                prog = self.n
                self.t_fin = 1.1
                self.globo.decir("final", True)
            else:
                self.respuesta = "blanco"
                self.t_fin = 0.9
                self.globo.decir("blanco", True)
            datos = {
                "i1_mascara": int(round(self.mascara)),
                "i1_actuadas": self.actuadas,
                "i1_sinceras": self.sinceras,
            }
            self.resultado = {"resultado": res, "progreso": prog, "datos": datos}

        def siguiente(self):
            self.i += 1
            self.estado = "linea"
            self.restante = self.tlinea
            self.sostenido = 0.0
            self.sosteniendo = False
            if self.mascara < 60.0:
                self.aviso_alta = False
            if self.es_ultima():
                self.globo.decir("casi", True)
            elif self.mascara >= 75.0 and not self.aviso_alta:
                self.aviso_alta = True
                self.globo.decir("caida", True)
            elif self.i == self.n // 2 and not self.aviso_mitad:
                self.aviso_mitad = True
                self.globo.decir("mitad")

        def tick(self):
            ahora = time.perf_counter()
            dt = ahora - self.ultimo
            self.ultimo = ahora
            if dt < 0.0:
                dt = 0.0
            if dt > 0.12:
                dt = 0.12

            self.globo.avanzar(dt)
            if self.flash > 0.0:
                self.flash -= dt
            if self.aviso_t > 0.0:
                self.aviso_t -= dt
                if self.aviso_t <= 0.0:
                    self.aviso = ""

            if self.estado == "listo":
                return None
            if self.estado == "fin":
                self.t_fin -= dt
                if self.t_fin <= 0.0:
                    return self.resultado
                return None
            if self.estado == "resp":
                self.pausa -= dt
                if self.pausa <= 0.0:
                    self.siguiente()
                return None

            ## estado "linea"
            if self.sosteniendo:
                self.sostenido += dt
                if self.sostenido >= self.mantener:
                    self.resolver("sincera")
                    return None
            if not self.es_ultima():
                self.restante -= dt
                if self.restante <= 0.0:
                    self.resolver("auto")
            return None

        ## --- Datos para la pantalla ----------------------------------------------

        def fraccion_hold(self):
            if self.sosteniendo and self.mantener > 0.0:
                f = self.sostenido / self.mantener
                if f > 1.0:
                    f = 1.0
                return f
            return 0.0

        def mensaje(self):
            if self.estado == "fin":
                if self.resultado["resultado"] == "ganado":
                    return "Esta vez no hubo máscara."
                return "Se quedó en blanco."
            if self.estado == "resp":
                if self.respuesta == "actuada":
                    return "Aplauso. La sonrisa pesa un poco más."
                if self.respuesta == "sincera":
                    return "Silencio. Y se oyó."
                if self.respuesta == "improviso":
                    return "Se le acabó el tiempo y actuó sin querer."
            if self.aviso_t > 0.0:
                return self.aviso
            return ""

        def expresion(self):
            if self.estado == "fin":
                if self.resultado["resultado"] == "ganado":
                    return "feliz"
                return "triste"
            if self.mascara >= 60.0:
                return "esfuerzo"
            if self.mascara <= 25.0 and self.sinceras > 0:
                return "animo"
            return "neutral"

        def anim(self):
            if self.estado == "fin":
                if self.resultado["resultado"] == "ganado":
                    return "salto"
                return "tiembla"
            return "bob"

    mj_registrar("i1", "mj_i1", "La máscara se cansa", True)


################################################################################
##  SCREEN
##  «Mantener»: botón sobre la tarjeta + mousedown_1 / mouseup_1 (ratón y toque),
##  o la tecla S (keydown_ / keyup_). Actuada: clic o tecla A.
################################################################################

screen mj_i1(hermana, params, inicio, intento, fallos, nivel, titulo):

    modal True
    zorder 95

    default vivo = MJI1(params, inicio)

    timer 0.02 repeat True action Function(vivo.tick)

    key "K_a" action Function(vivo.actuada)
    key "keydown_K_s" action Function(vivo.sincera_inicio)
    key "keyup_K_s" action Function(vivo.sincera_fin)
    key "mousedown_1" action Function(vivo.mouse_down)
    key "mouseup_1" action Function(vivo.mouse_up)
    key "K_RETURN" action Function(vivo.empezar)

    $ color = PETALO_COLOR[hermana]
    $ claro = ui_mezclar(color, "#FFFFFF", 0.25)
    $ tinta = ui_mezclar(color, "#000000", 0.75)
    $ tono = TARJETA_TONO[hermana]
    $ linea = vivo.linea_actual()
    $ hay_actuada = (linea[0] is not None)
    $ txt_actuada = linea[0]
    if txt_actuada is None:
        $ txt_actuada = "(Esta no se actúa.)"
    $ col_barra = color
    if vivo.mascara >= 75.0:
        $ col_barra = "#FF8A8A"
    $ t_rest = None
    $ t_tot = None
    if vivo.estado != "listo" and not vivo.es_ultima():
        $ t_rest = vivo.restante
        $ t_tot = vivo.tlinea

    add "bg_sala_ensayo" fit "cover"

    use mj_marco(hermana, titulo, intento, fallos, nivel, vivo.i, vivo.n, t_rest, t_tot, "LÍNEAS"):

        ## Barra de máscara
        vbox:
            xalign 0.5
            ypos 130
            spacing 8
            text ("MÁSCARA   " + str(int(round(vivo.mascara))) + " %"):
                xalign 0.5
                font gui.name_text_font
                size 24
                kerning 3
                color "#FFFFFF"
                outlines [(3, "#1B102699", 0, 0)]
            use barra_progreso(vivo.mascara, 100.0, col_barra, 900)

        if vivo.estado != "listo":

            text ("LÍNEA " + str(vivo.i + 1) + " / " + str(vivo.n)):
                xalign 0.5
                ypos 200
                font gui.name_text_font
                size 24
                kerning 3
                color "#E8E0F2"
                outlines [(3, "#1B102699", 0, 0)]

            ## ACTUADA
            button:
                xpos 320
                ypos 240
                xysize (620, 280)
                sensitive (hay_actuada and vivo.estado == "linea")
                action Function(vivo.actuada)
                hover_sound audio.sfx_hover
                background Fixed(
                    Transform(Frame("ui/opcion_neutra.png", 40, 40, 40, 40), matrixcolor=TintMatrix(tono)),
                    Transform(Frame("ui/opcion_marco.png", 40, 40, 40, 40), matrixcolor=TintMatrix(color)))
                hover_background Fixed(
                    Transform(Frame("ui/opcion_neutra.png", 40, 40, 40, 40), matrixcolor=TintMatrix(color)),
                    Transform(Frame("ui/opcion_marco.png", 40, 40, 40, 40), matrixcolor=TintMatrix("#FFFFFF")))
                insensitive_background Fixed(
                    Transform(Frame("ui/opcion_neutra.png", 40, 40, 40, 40), matrixcolor=TintMatrix("#2A2236")),
                    Transform(Frame("ui/opcion_marco.png", 40, 40, 40, 40), matrixcolor=TintMatrix("#6E6680")))

                vbox:
                    xpos 36
                    ypos 28
                    xsize 548
                    spacing 16
                    text "ACTUADA  ·  toca  (A)":
                        font gui.name_text_font
                        size 22
                        kerning 3
                        color claro
                        hover_color tinta
                        insensitive_color "#8F8AA0"
                    text txt_actuada:
                        size 32
                        color "#F3EEFA"
                        hover_color tinta
                        insensitive_color "#8F8AA0"
                        xsize 548

            ## SINCERA (mantener)
            button:
                xpos 980
                ypos 240
                xysize (620, 280)
                action NullAction()
                hovered Function(vivo.set_sobre, "s")
                unhovered Function(vivo.set_sobre, None)
                background Fixed(
                    Transform(Frame("ui/opcion_neutra.png", 40, 40, 40, 40), matrixcolor=TintMatrix(tono)),
                    Transform(Frame("ui/opcion_marco.png", 40, 40, 40, 40), matrixcolor=TintMatrix(color)))
                hover_background Fixed(
                    Transform(Frame("ui/opcion_neutra.png", 40, 40, 40, 40), matrixcolor=TintMatrix(color)),
                    Transform(Frame("ui/opcion_marco.png", 40, 40, 40, 40), matrixcolor=TintMatrix("#FFFFFF")))

                vbox:
                    xpos 36
                    ypos 28
                    xsize 548
                    spacing 16
                    text "SINCERA  ·  mantén pulsado  (S)":
                        font gui.name_text_font
                        size 22
                        kerning 3
                        color claro
                        hover_color tinta
                    text linea[1]:
                        size 32
                        color "#F3EEFA"
                        hover_color tinta
                        xsize 548

                fixed:
                    xpos 36
                    ypos 244
                    xysize (548, 14)
                    use barra_progreso(vivo.fraccion_hold(), 1.0, "#FFFFFF", 548)

            text vivo.mensaje():
                xalign 0.5
                ypos 560
                size 28
                color "#FFFFFF"
                outlines [(3, "#1B102699", 0, 0)]

        use mj_retrato("ichika", vivo.expresion(), vivo.globo, vivo.anim(), 280, 900, 0.5)

        ## Pantalla de inicio
        if vivo.estado == "listo":
            fixed:
                xalign 0.5
                ypos 210
                xysize (1060, 430)

                add Transform(Frame("ui/opcion_neutra.png", 40, 40, 40, 40), matrixcolor=TintMatrix("#1B1026"))
                add Transform(Frame("ui/opcion_marco.png", 40, 40, 40, 40), matrixcolor=TintMatrix(color))

                vbox:
                    xalign 0.5
                    ypos 32
                    xsize 940
                    spacing 16

                    text "LA MÁSCARA SE CANSA":
                        xalign 0.5
                        font gui.name_text_font
                        size 40
                        kerning 4
                        color "#FFF8FC"

                    text "Cada línea: toca ACTUADA (rápida, la máscara sube) o mantén pulsado SINCERA (cuesta, la máscara baja). Si la barra llega al tope, te quedas en blanco. Si no eliges a tiempo, improvisa y cuenta como actuada. La última línea solo puede decirse sincera.":
                        xalign 0.5
                        text_align 0.5
                        size 26
                        color "#E8E0F2"

                fixed:
                    xalign 0.5
                    ypos 320
                    xysize (420, 80)
                    use cinta_boton("Empezar", Function(vivo.empezar), hermana, 420, 80, 34)


################################################################################
##  PRUEBA SUELTA:  jump mj_probar_i1
################################################################################

label mj_probar_i1:

    scene bg_negro

    call mj_ejecutar("i1", "ichika")

    $ mj_msg = "Resultado: " + str(_return)
    $ mj_msg = mj_msg + " · intentos " + str(e6_mj["ichika"]["intentos"])
    $ mj_msg = mj_msg + " · fallos " + str(e6_mj["ichika"]["fallos"])
    $ mj_msg = mj_msg + " · nivel " + str(e6_mj["ichika"]["nivel"])
    $ mj_msg = mj_msg + " · datos " + str(e6_mj["ichika"]["datos"])
    $ narrator(mj_msg)
    return