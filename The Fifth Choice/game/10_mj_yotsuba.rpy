################################################################################
##  10_mj_yotsuba.rpy — Y2 · Relevo de las cinco (Evento 6, bloque de Yotsuba)
##
##  Cinco tramos IGUALES, un solo botón (clic, toque, Espacio o Intro).
##  Cada tramo: la corredora con el testigo se acerca a la MARCA de la pista;
##  hay que pulsar justo cuando la pasa (ventana ± `ventana` segundos).
##    · pulsar antes  = salida en falso
##    · pulsar tarde  = se cae el testigo
##  Los cuatro primeros tramos son traspasos (Ichika → Nino → Miku → Itsuki →
##  Yotsuba); el quinto es la meta: Yotsuba se lanza a la cinta. La pista tiene
##  28 marcas (el número perfecto).
##
##  Parámetros: MJ_PARAMS["y2"] (10_minijuegos.rpy).
##    ventana       segundos de tolerancia a cada lado de la marca
##    velocidad     multiplica la velocidad de la corredora
##    testigos      «vidas»: errores que consumen un testigo; con 0 testigos
##                  restantes el intento se pierde. Tras un error el tramo se
##                  repite mientras queden testigos.
##    salida_falsa  "penaliza" (cuesta un testigo) · "avisa" (la 1.ª de cada
##                  tramo es gratis) · "ignora" (no pasa nada)
##    puntos_control  tramos completados donde se guarda el progreso
##
##  Devuelve (a través de mj_ejecutar): "ganado" | "perdido" | "saltado".
##  Datos que anota: caidos, falsas.
################################################################################

define Y2_ORDEN = ["ichika", "nino", "miku", "itsuki", "yotsuba"]
define Y2_X0 = 170
define Y2_LONG = 330
define Y2_SUELO = 775
define Y2_ZOOM = 0.34
define Y2_VEL_BASE = 0.55
define Y2_PREP_PRIMERO = 0.9
define Y2_PREP = 0.45
define Y2_T_PASA = 0.65
define Y2_T_FALSA = 0.7
define Y2_T_ERROR = 1.0
define Y2_T_ERROR_LARGO = 1.9
define Y2_T_LIBRE = 0.8
define Y2_T_FIN = 1.8

init python:

    import math

    def y2_x(i):
        """x de la línea de salida del tramo i (i = 0..5; 5 es la meta)."""
        return Y2_X0 + Y2_LONG * i

    class MJY2(object):
        """Estado vivo del relevo. Lo crea la screen (default): no se guarda;
        si se carga una partida a mitad, el intento reinicia desde el punto
        de control."""

        def __init__(self, params, inicio, fallos_previos):
            self.p = params
            self.reloj = MJReloj()
            self.tramo = inicio
            self.fallos_prev = fallos_previos
            self.caidos = 0
            self.falsas = 0
            self.gratis = {}
            self.globo = MJGlobo("yotsuba")
            self.aviso = ""
            self.aviso_color = "#FFFFFF"
            self.aviso_t = 0.0
            self.humor = ""
            self.dur_error = Y2_T_ERROR
            self.marca = 0.7
            self.v = 0.5
            self.t_marca = 1.0
            self.t0 = 0.0
            self.t_fase = 0.0
            self.fase = "listos"
            self.prep = Y2_PREP_PRIMERO
            self.nuevo_tramo(Y2_PREP_PRIMERO)
            self.globo.decir("inicio", True)

        # ---- tiempos ---------------------------------------------------------
        def cambiar(self, fase):
            self.fase = fase
            self.t_fase = self.reloj.t

        def dt_fase(self):
            return self.reloj.t - self.t_fase

        def t_tramo(self):
            return self.reloj.t - self.t0

        def nuevo_tramo(self, prep):
            self.marca = 0.55 + renpy.random.random() * 0.25
            self.v = Y2_VEL_BASE * self.p["velocidad"]
            self.t_marca = self.marca / self.v
            self.prep = prep
            self.humor = ""
            self.cambiar("listos")

        def es_final(self):
            return self.tramo == 4

        def texto(self, clave):
            final = self.es_final()
            if clave == "ok":
                if final:
                    return "Cruzó la meta."
                return "Testigo recibido."
            if clave == "falsa":
                if final:
                    return "Se lanzó antes de tiempo."
                return "Salió antes de tiempo."
            if clave == "tarde":
                if final:
                    return "Se le pasó la cinta."
                return "Se cayó el testigo."
            return ""

        def poner_aviso(self, texto, color):
            self.aviso = texto
            self.aviso_color = color
            self.aviso_t = 1.1

        # ---- geometría -------------------------------------------------------
        def x_fin(self, i):
            if i == 4:
                return y2_x(5) - 70
            return y2_x(i + 1) - 95

        def quien(self):
            i = self.tramo
            if i > 4:
                i = 4
            return Y2_ORDEN[i]

        def u_visual(self):
            f = self.fase
            if f == "listos":
                return 0.0
            if f == "pasa":
                s = self.dt_fase() / Y2_T_PASA
                if s > 1.0:
                    s = 1.0
                return self.marca + (1.0 - self.marca) * s
            if f == "fin":
                return 1.0
            u = self.t_tramo() * self.v
            if u > 1.0:
                u = 1.0
            return u

        def geometria(self):
            T = self.tramo
            if T > 4:
                T = 4
            xs = y2_x(T)
            xe = self.x_fin(T)
            marca_x = xs + self.marca * (xe - xs)
            zw = self.p["ventana"] * self.v * (xe - xs)
            return {
                "n": T + 1,
                "marca_x": int(round(marca_x)),
                "zona_x": int(round(marca_x - zw)),
                "zona_w": int(round(2.0 * zw)),
                "mostrar": self.fase != "fin",
            }

        def posiciones(self):
            res = []
            T = self.tramo
            u = self.u_visual()
            f = self.fase
            for i in range(5):
                r = {"h": Y2_ORDEN[i], "expr": "neutral", "anim": "quieto", "zoom": Y2_ZOOM, "x": y2_x(i)}
                if i < T:
                    r["x"] = self.x_fin(i)
                    r["expr"] = "animo"
                    r["anim"] = "bob"
                elif i == T:
                    xs = y2_x(i)
                    xe = self.x_fin(i)
                    r["x"] = xs + u * (xe - xs)
                    if f != "listos":
                        r["expr"] = "esfuerzo"
                        r["anim"] = "bob"
                    if f == "cae":
                        r["expr"] = "triste"
                        r["anim"] = "tiembla"
                elif i == T + 1:
                    if f == "falsa":
                        s = self.dt_fase() / Y2_T_FALSA
                        if s > 1.0:
                            s = 1.0
                        r["x"] = y2_x(i) + 150 * s
                        r["expr"] = "animo"
                        r["anim"] = "bob"
                    elif f == "pasa":
                        r["expr"] = "animo"
                        r["anim"] = "bob"
                if f == "fin":
                    r["expr"] = "feliz"
                    r["anim"] = "salto"
                r["x"] = int(round(r["x"]))
                res.append(r)
            return res

        def testigo(self):
            """(x, y, giro) del testigo, o None si no se dibuja."""
            T = self.tramo
            if T >= 5:
                return None
            pos = self.posiciones()
            c = pos[T]
            bx = c["x"] + 46
            by = Y2_SUELO - 118
            giro = -25
            f = self.fase
            if f == "pasa" and T < 4:
                s = self.dt_fase() / Y2_T_PASA
                if s > 1.0:
                    s = 1.0
                rx = y2_x(T + 1) + 40
                bx = bx + (rx - bx) * s
                by = by - 70.0 * math.sin(math.pi * s)
                giro = -25 + 340 * s
            elif f == "cae":
                s = self.dt_fase() / 0.5
                if s > 1.0:
                    s = 1.0
                by = by + 100.0 * s * s
                giro = 70 * s
            return (int(round(bx)), int(round(by)), int(round(giro)))

        def expresion_star(self):
            return mj_chibi_expresion(self.tramo, 5, self.humor)

        def anim_star(self):
            if self.humor == "feliz":
                return "salto"
            if self.humor == "triste":
                return "tiembla"
            return "bob"

        # ---- resultado -------------------------------------------------------
        def resultado(self, que):
            return {
                "resultado": que,
                "progreso": self.tramo,
                "datos": {"caidos": self.caidos, "falsas": self.falsas},
            }

        def error(self, clave_texto, evento):
            """Consume un testigo y arranca la animación de error."""
            self.caidos += 1
            self.poner_aviso(self.texto(clave_texto), "#FFC4C4")
            self.humor = "triste"
            self.dur_error = Y2_T_ERROR
            if self.caidos >= self.p["testigos"] and MJ_FALLO_EN_GLOBO:
                self.globo.poner(mj_texto_fallo("yotsuba", self.fallos_prev), 1.8)
                self.dur_error = Y2_T_ERROR_LARGO
            else:
                self.globo.decir(evento, True)

        # ---- entrada ---------------------------------------------------------
        def pulsar(self):
            if self.fase != "corre":
                return None
            self.reloj.avanzar()
            dif = self.t_tramo() - self.t_marca
            vent = self.p["ventana"]
            if dif > vent:
                self.error("tarde", "caida")
                self.cambiar("cae")
                return None
            if dif >= -vent:
                self.poner_aviso(self.texto("ok"), "#CFFFD8")
                self.cambiar("pasa")
                hechos = self.tramo + 1
                if hechos == 3:
                    self.globo.decir("mitad", True)
                elif hechos == 4:
                    self.globo.decir("casi", True)
                elif hechos < 5:
                    self.globo.decir("acierto", True)
                return None
            return self.salida_falsa()

        def salida_falsa(self):
            modo = self.p["salida_falsa"]
            self.falsas += 1
            if modo == "ignora":
                self.poner_aviso("Todavía no.", "#E8E0F2")
                return None
            if modo == "avisa" and not self.gratis.get(self.tramo, False):
                self.gratis[self.tramo] = True
                self.poner_aviso(self.texto("falsa"), "#FFE3A0")
                self.globo.decir("falsa", True)
                self.cambiar("libre")
                return None
            self.error("falsa", "falsa")
            self.cambiar("falsa")
            return None

        def tick(self):
            dt = self.reloj.avanzar()
            self.globo.avanzar(dt)
            if self.aviso_t > 0.0:
                self.aviso_t -= dt
            f = self.fase

            if f == "listos":
                if self.dt_fase() >= self.prep:
                    self.t0 = self.reloj.t
                    self.cambiar("corre")
                return None

            if f == "corre":
                if self.t_tramo() > self.t_marca + self.p["ventana"]:
                    self.error("tarde", "caida")
                    self.cambiar("cae")
                return None

            if f == "pasa":
                if self.dt_fase() >= Y2_T_PASA:
                    self.tramo += 1
                    if self.tramo >= 5:
                        self.humor = "feliz"
                        self.globo.decir("final", True)
                        self.cambiar("fin")
                    else:
                        self.nuevo_tramo(Y2_PREP)
                return None

            if f == "libre":
                if self.dt_fase() >= Y2_T_LIBRE:
                    self.nuevo_tramo(Y2_PREP)
                return None

            if f == "falsa" or f == "cae":
                if self.dt_fase() >= self.dur_error:
                    if self.caidos >= self.p["testigos"]:
                        return self.resultado("perdido")
                    self.nuevo_tramo(Y2_PREP)
                return None

            if f == "fin":
                if self.dt_fase() >= Y2_T_FIN:
                    return self.resultado("ganado")
            return None

    mj_registrar("y2", "mj_y2", "Relevo de las cinco", True)


################################################################################
##  SCREEN
################################################################################

screen mj_y2(hermana, params, inicio, intento, fallos, nivel, titulo):

    modal True
    zorder 95

    default vivo = MJY2(params, inicio, fallos)

    timer 0.033 repeat True action Function(vivo.tick)

    key "K_SPACE" action Function(vivo.pulsar)
    key "K_RETURN" action Function(vivo.pulsar)

    $ pos = vivo.posiciones()
    $ geo = vivo.geometria()
    $ bat = vivo.testigo()
    $ quien = vivo.quien()
    $ color_q = PETALO_COLOR[quien]
    $ vivos_t = vivo.p["testigos"] - vivo.caidos

    add "bg_pista_atletismo" fit "cover"

    use mj_marco(hermana, titulo, intento, fallos, nivel, vivo.tramo, 5, None, None, "TRAMOS"):

        ## Toda la pantalla es un botón: sirve el toque en móvil.
        button:
            xysize (1920, 1080)
            background None
            action Function(vivo.pulsar)

        text ("TRAMO " + str(geo["n"]) + "/5 · " + quien.capitalize()):
            xalign 0.5
            ypos 150
            font gui.name_text_font
            size 40
            kerning 3
            color color_q
            outlines [(5, "#1B1026CC", 0, 0)]

        text "Pulsa cuando la corredora pase la marca.":
            xalign 0.5
            ypos 210
            size 28
            color "#FFFFFF"
            outlines [(3, "#1B102699", 0, 0)]

        ## --- La pista ---
        add Solid("#B8453CE0", xsize=1720, ysize=190) xpos 110 ypos 610
        add Solid("#FFFFFFB0", xsize=1720, ysize=4) xpos 110 ypos 610
        add Solid("#FFFFFFB0", xsize=1720, ysize=4) xpos 110 ypos 796

        for k in range(6):
            add Solid("#FFFFFFAA", xsize=4, ysize=190) xpos (Y2_X0 + Y2_LONG * k - 2) ypos 610

        for k in range(28):
            add Solid("#FFFFFF77", xsize=3, ysize=14) xpos (Y2_X0 + int(k * (Y2_LONG * 5) / 27.0)) ypos 592

        text "28":
            xpos (Y2_X0 + Y2_LONG * 5)
            xanchor 0.5
            ypos 548
            font gui.name_text_font
            size 34
            color "#FFFFFF"
            outlines [(4, "#1B1026CC", 0, 0)]

        add Solid("#FFFFFF", xsize=8, ysize=190) xpos (Y2_X0 + Y2_LONG * 5 - 4) ypos 610

        ## --- Marca y ventana del tramo actual ---
        if geo["mostrar"]:
            add Solid(color_q + "66", xsize=geo["zona_w"], ysize=190) xpos geo["zona_x"] ypos 610
            add Solid("#FFE3A0", xsize=6, ysize=190) xpos (geo["marca_x"] - 3) ypos 610
            text "MARCA":
                xpos geo["marca_x"]
                xanchor 0.5
                ypos 566
                size 20
                color "#FFE3A0"
                outlines [(3, "#1B1026CC", 0, 0)]

        ## --- Las cinco chibis ---
        for r in pos:
            use mj_chibi_vista(r["h"], r["expr"], r["x"], Y2_SUELO, r["zoom"], r["anim"])

        if bat is not None:
            add Transform(Solid("#FFE3A0", xsize=46, ysize=10), rotate=bat[2]) xpos bat[0] ypos bat[1] xanchor 0.5 yanchor 0.5

        if vivo.aviso_t > 0.0:
            text vivo.aviso:
                xalign 0.5
                ypos 480
                font gui.name_text_font
                size 44
                color vivo.aviso_color
                outlines [(5, "#1B1026CC", 0, 0)]

        ## --- Testigos que quedan ---
        hbox:
            xpos 60
            ypos 112
            spacing 12
            text "TESTIGOS":
                size 22
                color "#FFFFFF"
                yalign 0.5
                outlines [(3, "#1B102699", 0, 0)]
            for k in range(vivo.p["testigos"]):
                if k < vivos_t:
                    add Solid("#FFE3A0", xsize=36, ysize=10) yalign 0.5
                else:
                    add Solid("#FFFFFF33", xsize=36, ysize=10) yalign 0.5

        ## --- Yotsuba chibi: el estado de ánimo y sus globos ---
        use mj_retrato("yotsuba", vivo.expresion_star(), vivo.globo, vivo.anim_star(), 250, 560, 0.6)

        fixed:
            xalign 0.5
            ypos 822
            xysize (420, 84)
            use cinta_boton("¡Ahora!", Function(vivo.pulsar), quien, 420, 84, 38)


################################################################################
##  PRUEBA — jump mj_probar_y2  (consola Shift+O, o desde un menú de depuración)
################################################################################

label mj_probar_y2:

    scene bg_negro
    $ e6_estado = {}
    $ e6_mj = {}
    $ persistent.e6_mj_ganado_yotsuba = False

    menu:
        "Probar Y2 · ¿con el boost de Nino?"

        "Sin boost (difícil)":
            $ nino_rama_beat = "tibia"

        "Con boost (media)":
            $ nino_rama_beat = "calida"

    call mj_ejecutar("y2", "yotsuba")

    $ y2_res = _return
    $ y2_info = e6_mj["yotsuba"]
    $ narrator("Resultado: " + str(y2_res) + " · intentos " + str(y2_info["intentos"]) + " · fallos " + str(y2_info["fallos"]) + " · nivel " + y2_info["nivel"] + " · caídos " + str(y2_info["datos"].get("caidos", 0)))
    return
