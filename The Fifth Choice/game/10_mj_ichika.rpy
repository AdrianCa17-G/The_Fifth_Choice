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
define I1_MASCARA_REINICIO = 40.0     ## al reanudar desde un punto de control
define I1_ENERGIA_REINICIO = 60.0
define I1_ENERGIA_MAX = 100.0
define I1_PAUSA_RESPUESTA = 0.55

## Distribución dentro del área de juego del marco (x 440–1880, y 112–932).
define I1_ANCHO = 1360                          ## bloque de juego: x 480–1840
define I1_X = MJ_AREA_CX - I1_ANCHO // 2        ## 480
define I1_TARJETA_W = 660                       ## barras y tarjetas: dos columnas de 660 + 40 de hueco
define I1_TARJETA_H = 330
define I1_X2 = I1_X + I1_ANCHO - I1_TARJETA_W   ## 1180: columna derecha
define I1_BARRAS_Y = MJ_AREA_Y + 64             ## MÁSCARA / ENERGÍA
define I1_BARRA_H = 28
define I1_RELOJ_Y = MJ_AREA_Y + 216             ## tiempo para elegir
define I1_TARJETAS_Y = MJ_AREA_Y + 298          ## EL PAPEL / LO QUE SIENTE
define I1_CONSEJO_Y = I1_TARJETAS_Y + I1_TARJETA_H + 34
define I1_MASCARA_PELIGRO = 75.0                ## desde aquí la barra se pone roja (zona de «en blanco»)


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

    def i1_signo(n):
        n = int(round(n))
        if n >= 0:
            return "+" + str(n)
        return "-" + str(abs(n))

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
            self.e_gana = float(params["energia_actuada"])
            self.e_cuesta = float(params["energia_sincera"])
            self.peso = float(params["peso_mascara"])
            self.mantener = float(params["mantener"])
            self.tlinea = float(params["tiempo_linea"])
            if self.i > 0:
                self.mascara = I1_MASCARA_REINICIO
                self.energia = I1_ENERGIA_REINICIO
            else:
                self.mascara = float(params["mascara_ini"])
                self.energia = float(params["energia_ini"])

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
            self.d_mascara = 0.0
            self.d_energia = 0.0
            self.desperdicio = False
            self.aviso_mitad = False
            self.aviso_alta = False
            self.resultado = None
            self.t_fin = 0.0
            self.ultimo = time.perf_counter()

        def linea_actual(self):
            return self.lineas[self.i]

        def es_ultima(self):
            return self.i >= self.n - 1

        def costo_sincera(self):
            if self.es_ultima():
                return 0.0
            return self.e_cuesta

        def puede_sincera(self):
            return self.energia >= self.costo_sincera()

        def req_hold(self):
            """Segundos que hay que mantener: sube con la máscara."""
            return self.mantener * (1.0 + self.peso * (self.mascara / 100.0))

        def consejo(self):
            if self.estado != "linea" or self.es_ultima():
                return ""
            if not self.puede_sincera():
                return "Sin energía: solo puedes actuar. Actuar la recupera."
            if self.mascara >= 70.0:
                return "La máscara pesa. Una sincera la baja."
            if self.mascara <= 20.0:
                return "Poca máscara: actuar sale barato y recupera energía."
            return ""

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
            if not self.puede_sincera():
                self.aviso = "Sin fuerzas. Actúa para recuperar energía."
                self.aviso_t = 1.2
                self.globo.decir("sinfuerzas")
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
            m_antes = self.mascara
            e_antes = self.energia
            self.desperdicio = False
            if modo == "sincera":
                if m_antes < self.baja and not self.es_ultima():
                    self.desperdicio = True
                self.mascara -= self.baja
                if self.mascara < 0.0:
                    self.mascara = 0.0
                self.energia -= self.costo_sincera()
                if self.energia < 0.0:
                    self.energia = 0.0
                self.sinceras += 1
                self.respuesta = "sincera"
                self.globo.decir("sincera")
                ## El clic de LO QUE SIENTE suena aquí, al completarse: ni al pulsar
                ## (adelantaría el resultado) ni al soltar (llegaría tarde o mentiría).
                renpy.sound.play(audio.sfx_click)
            else:
                self.mascara += self.sube
                self.energia += self.e_gana
                if self.energia > I1_ENERGIA_MAX:
                    self.energia = I1_ENERGIA_MAX
                self.actuadas += 1
                if modo == "auto":
                    self.respuesta = "improviso"
                    self.globo.decir("improviso", True)
                else:
                    self.respuesta = "actuada"
                    self.globo.decir("actuada")
            self.d_mascara = self.mascara - m_antes
            self.d_energia = self.energia - e_antes
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
            elif not self.puede_sincera():
                self.globo.decir("sinfuerzas", True)
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
                if self.sostenido >= self.req_hold():
                    self.resolver("sincera")
                    return None
            if not self.es_ultima():
                self.restante -= dt
                if self.restante <= 0.0:
                    self.resolver("auto")
            return None

        ## --- Datos para la pantalla ----------------------------------------------

        def fraccion_hold(self):
            req = self.req_hold()
            if self.sosteniendo and req > 0.0:
                f = self.sostenido / req
                if f > 1.0:
                    f = 1.0
                return f
            return 0.0

        def mensaje(self):
            """(texto, tipo) para el aviso del marco. tipo: "bien" | "mal" | "info"."""
            if self.estado == "fin":
                if self.resultado["resultado"] == "ganado":
                    return ("Esta vez no hubo máscara.", "bien")
                return ("Se quedó en blanco.", "mal")
            if self.estado == "resp":
                if self.respuesta == "actuada":
                    return ("Aplauso. La sonrisa pesa un poco más.", "info")
                if self.respuesta == "improviso":
                    return ("Se le acabó el tiempo y actuó sin querer.", "mal")
                if self.desperdicio:
                    return ("Casi no había máscara que quitar. Energía gastada de más.", "mal")
                return ("Silencio. Y se oyó.", "bien")
            if self.aviso_t > 0.0:
                if self.aviso == "Mantén un poco más.":
                    return (self.aviso, "info")
                return (self.aviso, "mal")
            return ("", "info")

        def expresion(self):
            if self.estado == "fin":
                if self.resultado["resultado"] == "ganado":
                    return "feliz"
                return "triste"
            if self.mascara >= 60.0 or not self.puede_sincera():
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

## Una barra grande (MÁSCARA o ENERGÍA): etiqueta, cifra, cambio y nota.
## zona: desde qué valor se tiñe el fondo de rojo (None = sin zona).
## marca: dónde va la marca blanca del coste (None = sin marca).
screen i1_medidor(etiqueta, valor, cifra, cambio, color_cambio, color, nota, zona=None, marca=None):

    $ w = I1_TARJETA_W
    $ lleno = int(w * valor / 100.0)
    if lleno > w:
        $ lleno = w

    vbox:
        xsize w
        spacing 8

        fixed:
            xysize (w, 34)
            text etiqueta style "mj_etiqueta" xpos 0 yalign 0.5
            hbox:
                xalign 1.0
                yalign 0.5
                spacing 18
                if cambio != "":
                    text cambio style "mj_cifra" color color_cambio
                text cifra style "mj_cifra"

        fixed:
            xysize (w, I1_BARRA_H)
            add Solid("#FFFFFF2A", xsize=w, ysize=I1_BARRA_H) xpos 0 ypos 0
            if zona is not None:
                $ zx = int(w * zona / 100.0)
                add Solid("#FF8A8A40", xsize=w - zx, ysize=I1_BARRA_H) xpos zx ypos 0
            if lleno > 0:
                add Solid(color, xsize=lleno, ysize=I1_BARRA_H) xpos 0 ypos 0
            if marca is not None:
                add Solid("#FFFFFF", xsize=3, ysize=I1_BARRA_H + 12) xpos (int(w * marca / 100.0) - 1) ypos -6

        text nota style "mj_nota"


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
        $ txt_actuada = "Esta línea no se puede actuar."
    $ ultima = vivo.es_ultima()
    $ puede_s = vivo.puede_sincera()
    $ costo_s = int(round(vivo.costo_sincera()))
    $ hold_txt = "{:.1f}".format(vivo.req_hold()).replace(".", ",")
    $ en_juego = (vivo.estado != "listo")

    $ col_masc = color
    if vivo.mascara >= I1_MASCARA_PELIGRO:
        $ col_masc = "#FF8A8A"
    $ col_ener = "#8FD3FF"
    if not puede_s:
        $ col_ener = "#FFB38A"
    $ col_tiempo = "#FFE3A0"
    if vivo.restante < 1.0:
        $ col_tiempo = "#FF8A8A"

    ## Marca del coste de una sincera en la barra de energía (la última es gratis).
    $ marca_e = None
    $ nota_e = "Ser sincera cuesta energía (la raya blanca). Actuar la recupera."
    if en_juego and not ultima and costo_s > 0:
        $ marca_e = costo_s
    if ultima:
        $ nota_e = "La última línea sincera no cuesta energía."

    ## Cambio de la última decisión, junto a la cifra de su barra.
    $ cambio_m = ""
    $ cambio_e = ""
    if vivo.estado == "resp" or vivo.estado == "fin":
        $ cambio_m = i1_signo(vivo.d_mascara)
        $ cambio_e = i1_signo(vivo.d_energia)
    $ col_dm = "#FF9A9A"
    if vivo.d_mascara < 0.0:
        $ col_dm = "#9AE6B4"
    $ col_de = "#FFB38A"
    if vivo.d_energia > 0.0:
        $ col_de = "#9AE6B4"

    $ fondo_s = tono
    $ borde_s = color
    $ hover_fondo_s = color
    $ hover_borde_s = "#FFFFFF"
    if not puede_s:
        $ fondo_s = "#2A2236"
        $ borde_s = "#6E6680"
        $ hover_fondo_s = "#2A2236"
        $ hover_borde_s = "#6E6680"

    $ sub_s = "lo que no dice  ·  mantén (S) " + hold_txt + " s"
    $ chip_e = "ENERGÍA -" + str(costo_s)
    if ultima:
        $ sub_s = "la última  ·  gratis  ·  mantén (S) " + hold_txt + " s"
        $ chip_e = "ENERGÍA GRATIS"

    $ msg = vivo.mensaje()
    $ consejo = vivo.consejo()

    add "bg_sala_ensayo" fit "cover"

    use mj_marco(hermana, titulo, intento, fallos, nivel, vivo.i, vivo.n, None, None, "LÍNEAS", chibi=vivo.expresion(), globo=vivo.globo, anim=vivo.anim(), aviso=msg[0], aviso_tipo=msg[1]):

        ## --- Las dos barras: el corazón del minijuego ---
        fixed:
            xpos I1_X
            ypos I1_BARRAS_Y
            xysize (I1_ANCHO, 110)
            fixed:
                xpos 0
                ypos 0
                xysize (I1_TARJETA_W, 110)
                use i1_medidor("MÁSCARA", vivo.mascara, str(int(round(vivo.mascara))) + " %", cambio_m, col_dm, col_masc, "Al llegar a 100 %, se queda en blanco.", I1_MASCARA_PELIGRO)
            fixed:
                xpos (I1_X2 - I1_X)
                ypos 0
                xysize (I1_TARJETA_W, 110)
                use i1_medidor("ENERGÍA", vivo.energia, str(int(round(vivo.energia))), cambio_e, col_de, col_ener, nota_e, None, marca_e)

        if en_juego:

            ## --- Reloj de la línea ---
            if ultima:
                text "ÚLTIMA LÍNEA  ·  SIN PRISA  ·  SOLO PUEDE SER SINCERA":
                    style "mj_etiqueta"
                    color "#FFE3A0"
                    xpos MJ_AREA_CX
                    xanchor 0.5
                    ypos (I1_RELOJ_Y + 10)
            else:
                vbox:
                    xpos I1_X
                    ypos I1_RELOJ_Y
                    xsize I1_ANCHO
                    spacing 8
                    text "TIEMPO PARA ELEGIR" style "mj_etiqueta"
                    use barra_progreso(vivo.restante, vivo.tlinea, col_tiempo, I1_ANCHO)

            ## --- EL PAPEL (actuada): izquierda ---
            button:
                xpos I1_X
                ypos I1_TARJETAS_Y
                xysize (I1_TARJETA_W, I1_TARJETA_H)
                sensitive (hay_actuada and vivo.estado == "linea")
                action Function(vivo.actuada)
                hover_sound audio.sfx_hover
                activate_sound audio.sfx_click
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
                    ypos 24
                    xsize 588
                    spacing 6
                    text "EL PAPEL":
                        style "mj_etiqueta"
                        color claro
                        hover_color tinta
                        insensitive_color "#8F8AA0"
                    text "lo que pide el guion  ·  toca (A)":
                        style "mj_nota"
                        hover_color tinta
                        insensitive_color "#8F8AA0"
                    null height 10
                    text txt_actuada:
                        style "mj_aviso_texto"
                        hover_color tinta
                        insensitive_color "#8F8AA0"
                        xsize 588

                hbox:
                    xpos 36
                    ypos (I1_TARJETA_H - 52)
                    spacing 28
                    text ("MÁSCARA +" + str(int(round(vivo.sube)))):
                        style "mj_etiqueta"
                        color "#FF9A9A"
                        hover_color tinta
                        insensitive_color "#8F8AA0"
                    text ("ENERGÍA +" + str(int(round(vivo.e_gana)))):
                        style "mj_etiqueta"
                        color "#9AE6B4"
                        hover_color tinta
                        insensitive_color "#8F8AA0"

            ## --- LO QUE SIENTE (sincera, mantener): derecha ---
            ## Sin activate_sound a propósito: se mantiene pulsada y el clic suena
            ## en MJI1.resolver() al completarse (ver la nota allí).
            button:
                xpos I1_X2
                ypos I1_TARJETAS_Y
                xysize (I1_TARJETA_W, I1_TARJETA_H)
                action NullAction()
                hovered Function(vivo.set_sobre, "s")
                unhovered Function(vivo.set_sobre, None)
                hover_sound audio.sfx_hover
                background Fixed(
                    Transform(Frame("ui/opcion_neutra.png", 40, 40, 40, 40), matrixcolor=TintMatrix(fondo_s)),
                    Transform(Frame("ui/opcion_marco.png", 40, 40, 40, 40), matrixcolor=TintMatrix(borde_s)))
                hover_background Fixed(
                    Transform(Frame("ui/opcion_neutra.png", 40, 40, 40, 40), matrixcolor=TintMatrix(hover_fondo_s)),
                    Transform(Frame("ui/opcion_marco.png", 40, 40, 40, 40), matrixcolor=TintMatrix(hover_borde_s)))

                vbox:
                    xpos 36
                    ypos 24
                    xsize 588
                    spacing 6
                    text "LO QUE SIENTE":
                        style "mj_etiqueta"
                        color claro
                        hover_color tinta
                    text sub_s:
                        style "mj_nota"
                        hover_color tinta
                    null height 10
                    text linea[1]:
                        style "mj_aviso_texto"
                        hover_color tinta
                        xsize 588

                fixed:
                    xpos 36
                    ypos (I1_TARJETA_H - 84)
                    xysize (588, 12)
                    use barra_progreso(vivo.fraccion_hold(), 1.0, "#FFFFFF", 588)

                hbox:
                    xpos 36
                    ypos (I1_TARJETA_H - 52)
                    spacing 28
                    text ("MÁSCARA -" + str(int(round(vivo.baja)))):
                        style "mj_etiqueta"
                        color "#9AE6B4"
                        hover_color tinta
                    text chip_e:
                        style "mj_etiqueta"
                        color "#FFB38A"
                        hover_color tinta

                if not puede_s:
                    text "SIN FUERZAS":
                        style "mj_cifra"
                        color "#FFB38A"
                        xalign 0.5
                        yalign 0.62

            ## --- Consejo: instrucción fija bajo las tarjetas ---
            if consejo != "":
                text consejo:
                    style "mj_cuerpo"
                    xpos MJ_AREA_CX
                    xanchor 0.5
                    ypos I1_CONSEJO_Y

        ## --- Pantalla de inicio, dentro del área ---
        if not en_juego:
            $ b = MJ_BOTON["primario"]

            add Solid("#0B0712CC", xsize=MJ_AREA_W, ysize=MJ_AREA_H) xpos MJ_AREA_X ypos MJ_AREA_Y

            frame:
                xpos MJ_AREA_CX
                xanchor 0.5
                ypos (MJ_AREA_Y + MJ_AREA_H // 2)
                yanchor 0.5
                xsize I1_ANCHO
                ymaximum MJ_AREA_H
                padding (60, 40, 60, 40)
                background Fixed(
                    Transform(Frame("ui/opcion_neutra.png", 40, 40, 40, 40), matrixcolor=TintMatrix("#1B1026")),
                    Transform(Frame("ui/opcion_marco.png", 40, 40, 40, 40), matrixcolor=TintMatrix(color)))

                vbox:
                    xsize (I1_ANCHO - 120)
                    spacing 18

                    text "LA MÁSCARA SE CANSA":
                        style "mj_titulo"
                        xalign 0.5

                    text "Ichika repasa su papel. Cada línea tiene dos versiones: lo que el guion pide decir... y lo que de verdad siente.":
                        style "mj_cuerpo"
                        xalign 0.5
                        text_align 0.5

                    hbox:
                        xalign 0.5
                        spacing 60

                        vbox:
                            xsize 520
                            spacing 8
                            text "EL PAPEL  ·  TOCA (A)":
                                style "mj_etiqueta"
                                color claro
                            text "{color=#FF9A9A}MÁSCARA sube{/color}  ·  {color=#9AE6B4}ENERGÍA se recupera{/color}":
                                style "mj_cuerpo"
                            text "Es rápido y cómodo. Pero la máscara se llena.":
                                style "mj_nota"

                        vbox:
                            xsize 520
                            spacing 8
                            text "LO QUE SIENTE  ·  MANTÉN (S)":
                                style "mj_etiqueta"
                                color claro
                            text "{color=#9AE6B4}MÁSCARA baja{/color}  ·  {color=#FFB38A}ENERGÍA se gasta{/color}":
                                style "mj_cuerpo"
                            text "Cuesta, y cuesta más cuanta más máscara tengas.":
                                style "mj_nota"

                    text "OBJETIVO: llegar a la última línea sin que la máscara llegue a 100 %. Todo actuada: te quedas en blanco. Todo sincera: te quedas sin energía. Alterna.":
                        style "mj_cuerpo"
                        color "#FFE3A0"
                        xalign 0.5
                        text_align 0.5

                    null height 6

                    fixed:
                        xalign 0.5
                        xysize (b[0], b[1])
                        use cinta_boton("Empezar", Function(vivo.empezar), hermana, b[0], b[1], b[2])


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
    ## Llaves dobladas: un dict tiene {…} y Ren'Py lo leería como etiqueta de texto.
    $ mj_msg = mj_msg + " · datos " + str(e6_mj["ichika"]["datos"]).replace("{", "{{")
    $ narrator(mj_msg)
    return