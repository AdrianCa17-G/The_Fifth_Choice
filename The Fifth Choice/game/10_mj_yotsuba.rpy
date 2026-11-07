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
define Y2_PREP_PRIMERO = 0.7
define Y2_PREP = 0.28
define Y2_PREP_VUELTA = 0.55
define Y2_PREP_JITTER = 0.25      ## aleatoriedad en la espera: no se puede contar el ritmo
define Y2_MIN_T_MARCA = 0.45      ## segundos mínimos hasta la marca (siempre da tiempo a reaccionar)
define Y2_T_PASA = 0.40
define Y2_T_FALSA = 0.7
define Y2_T_ERROR = 0.85
define Y2_T_ERROR_LARGO = 1.9
define Y2_T_LIBRE = 0.8
define Y2_T_FIN = 1.8

define Y2_NIVEL_TXT = {"dificil": "DIFÍCIL", "media": "MEDIA", "asistida": "ASISTIDA"}

transform y2_quieto:
    xoffset 0

transform y2_pulso:
    alpha 1.0
    block:
        ease 0.25 alpha 0.55
        ease 0.25 alpha 1.0
        repeat
    

init python:

    import math

    def y2_x(i):
        """x de la línea de salida del carril i (i = 0..5; 5 es la meta)."""
        return Y2_X0 + Y2_LONG * i

    class MJY2(object):
        """Relevo de N tramos (N sale de MJ_PARAMS). Las cinco corren en ciclo.
        Lo crea la screen (default): no se guarda; al cargar reinicia desde el punto de control."""

        def __init__(self, params, inicio, fallos_previos, intro=False):
            self.p = params
            self.reloj = MJReloj()
            self.n = int(params["tramos"])
            tope = self.n - 5
            if tope < 0:
                tope = 0
            if inicio > tope:
                inicio = tope
            if inicio < 0:
                inicio = 0
            self.tramo = int(inicio)
            self.fallos_prev = fallos_previos
            self.caidos = 0
            self.falsas = 0
            self.perfectos = 0
            self.curados = 0
            self.racha = 0
            self.mejor_racha = 0
            self.gratis = {}
            self.globo = MJGlobo("yotsuba")
            self.aviso = ""
            self.aviso_color = "#FFFFFF"
            self.aviso_t = 0.0
            self.humor = ""
            self.dur_error = Y2_T_ERROR
            self.marca = 0.7
            self.senuelo = None
            self.v = 0.5
            self.ventana = float(params["ventana"])
            self.t_marca = 1.0
            self.t0 = 0.0
            self.t_fase = 0.0
            self.prep = Y2_PREP_PRIMERO
            self.fase = "listos"
            self.nuevo_tramo(Y2_PREP_PRIMERO)
            if intro:
                self.fase = "intro"
            else:
                if self.tramo > 0:
                    self.poner_aviso("Punto de control · tramo " + str(self.tramo + 1), "#E8E0F2")
                self.globo.decir("inicio", True)

        # ---- reglas (para la pantalla de explicación) -----------------------
        def reglas(self):
            p = self.p
            r = []
            r.append("Es un relevo de " + str(self.n) + " tramos: las cinco corren por turnos y el testigo no puede caerse.")
            r.append("Pulsa ¡AHORA! (clic, toque o Espacio) justo cuando la corredora cruce la MARCA dorada.")
            r.append("Pronto es salida en falso; tarde, se cae el testigo. Cada error gasta uno de tus " + str(p["testigos"]) + " testigos. Sin testigos, pierdes el intento.")
            r.append("Encadena " + str(p["cura"]) + " aciertos «Perfectos» seguidos y recuperas un testigo.")
            r.append("Cada tramo es más rápido y la ventana de acierto se estrecha.")
            if not p["zona"]:
                r.append("Aquí no hay zona sombreada: confía en el ritmo.")
            if p["ocultar"] < 1.0:
                r.append("La marca se esconde antes de que llegue la corredora.")
            if p["senuelo"] > 0.0:
                r.append("Ojo con los señuelos rojos (×): no son la marca.")
            if p["salida_falsa"] == "ignora":
                r.append("En asistencia, salir antes de tiempo no cuenta como error.")
            return r

        # ---- tiempos ---------------------------------------------------------
        def cambiar(self, fase):
            self.fase = fase
            self.t_fase = self.reloj.t

        def dt_fase(self):
            return self.reloj.t - self.t_fase

        def t_tramo(self):
            return self.reloj.t - self.t0

        def fraccion(self):
            if self.n <= 1:
                return 0.0
            f = float(self.tramo) / float(self.n - 1)
            if f > 1.0:
                f = 1.0
            return f

        def ritmo(self):
            return self.v / Y2_VEL_BASE

        def tramo_vis(self):
            t = self.tramo
            if t > self.n - 1:
                t = self.n - 1
            return t

        def slot(self):
            return self.tramo_vis() % 5

        def nuevo_tramo(self, prep):
            f = self.fraccion()
            self.v = Y2_VEL_BASE * float(self.p["velocidad"]) * (1.0 + float(self.p["rampa"]) * f)
            fin = float(self.p["ventana_fin"])
            self.ventana = float(self.p["ventana"]) * (1.0 + (fin - 1.0) * f)

            marca = 0.40 + renpy.random.random() * 0.45
            minimo = Y2_MIN_T_MARCA * self.v
            if marca < minimo:
                marca = minimo
            if marca > 0.90:
                marca = 0.90
            self.marca = marca
            self.t_marca = marca / self.v

            self.senuelo = None
            if renpy.random.random() < float(self.p["senuelo"]):
                pos = marca - (0.10 + renpy.random.random() * 0.10)
                if pos > 0.12:
                    self.senuelo = pos

            self.prep = prep + renpy.random.random() * Y2_PREP_JITTER
            self.humor = ""
            self.cambiar("listos")

        def es_final(self):
            return self.slot() == 4

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
            self.aviso_t = 1.0

        # ---- geometría -------------------------------------------------------
        def x_fin(self, i):
            if i == 4:
                return y2_x(5) - 70
            return y2_x(i + 1) - 95

        def quien(self):
            return Y2_ORDEN[self.slot()]

        def u_visual(self):
            f = self.fase
            if f == "listos" or f == "intro":
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
            T = self.slot()
            xs = y2_x(T)
            xe = self.x_fin(T)
            ancho = xe - xs
            marca_x = xs + self.marca * ancho
            zw = self.ventana * self.v * ancho
            sen_x = None
            if self.senuelo is not None:
                sen_x = int(round(xs + self.senuelo * ancho))
            visible = (self.fase != "fin")
            oc = float(self.p["ocultar"])
            if self.fase == "corre" and oc < 1.0:
                if self.u_visual() >= self.marca * oc:
                    visible = False
            return {
                "n": self.tramo_vis() + 1,
                "vuelta": self.tramo_vis() // 5 + 1,
                "marca_x": int(round(marca_x)),
                "zona_x": int(round(marca_x - zw)),
                "zona_w": int(round(2.0 * zw)),
                "senuelo_x": sen_x,
                "marca_visible": visible,
                "zona_visible": visible and bool(self.p["zona"]),
                "mostrar": self.fase != "fin",
            }

        def posiciones(self):
            res = []
            T = self.slot()
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
                    if f != "listos" and f != "intro":
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
            T = self.slot()
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
            return mj_chibi_expresion(self.tramo, self.n, self.humor)

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
                "datos": {
                    "caidos": self.caidos,
                    "falsas": self.falsas,
                    "perfectos": self.perfectos,
                    "curados": self.curados,
                    "mejor_racha": self.mejor_racha,
                },
            }

        def error(self, clave_texto, evento):
            """Consume un testigo, corta la racha y arranca la animación de error."""
            self.caidos += 1
            self.racha = 0
            self.poner_aviso(self.texto(clave_texto), "#FFC4C4")
            self.humor = "triste"
            self.dur_error = Y2_T_ERROR
            if self.caidos >= self.p["testigos"] and MJ_FALLO_EN_GLOBO:
                self.globo.poner(mj_texto_fallo("yotsuba", self.fallos_prev), 1.8)
                self.dur_error = Y2_T_ERROR_LARGO
            else:
                self.globo.decir(evento, True)

        # ---- entrada ---------------------------------------------------------
        def empezar(self):
            if self.fase != "intro":
                return None
            self.reloj.avanzar()
            self.globo.decir("inicio", True)
            self.cambiar("listos")
            return None

        def accion(self):
            if self.fase == "intro":
                return self.empezar()
            return self.pulsar()

        def pulsar(self):
            if self.fase != "corre":
                return None
            self.reloj.avanzar()
            dif = self.t_tramo() - self.t_marca
            vent = self.ventana
            if dif > vent:
                self.error("tarde", "caida")
                self.cambiar("cae")
                return None
            if dif >= -vent:
                return self.acierto(dif)
            return self.salida_falsa()

        def acierto(self, dif):
            perfecto = (abs(dif) <= self.ventana * 0.5)
            cura = int(self.p["cura"])
            if perfecto:
                self.perfectos += 1
                self.racha += 1
                if self.racha > self.mejor_racha:
                    self.mejor_racha = self.racha
                self.poner_aviso("¡Perfecto!", "#FFF0A8")
            else:
                self.racha = 0
                self.poner_aviso(self.texto("ok"), "#CFFFD8")

            curo = False
            if self.racha >= cura:
                if self.caidos > 0:
                    self.caidos -= 1
                    self.curados += 1
                    self.racha = 0
                    curo = True
                    self.poner_aviso("¡Testigo recuperado!", "#CFFFD8")
                else:
                    self.racha = cura

            self.cambiar("pasa")
            hechos = self.tramo + 1
            if curo:
                self.globo.decir("cura", True)
            elif hechos == self.n // 2:
                self.globo.decir("mitad", True)
            elif hechos == self.n - 2:
                self.globo.decir("casi", True)
            elif perfecto and self.racha == max(2, cura // 2):
                self.globo.decir("racha", True)
            elif hechos % 6 == 0:
                self.globo.decir("acierto", True)
            return None

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

            if f == "intro":
                return None

            if f == "listos":
                if self.dt_fase() >= self.prep:
                    self.t0 = self.reloj.t
                    self.cambiar("corre")
                return None

            if f == "corre":
                if self.t_tramo() > self.t_marca + self.ventana:
                    self.error("tarde", "caida")
                    self.cambiar("cae")
                return None

            if f == "pasa":
                if self.dt_fase() >= Y2_T_PASA:
                    self.tramo += 1
                    if self.tramo >= self.n:
                        self.humor = "feliz"
                        self.globo.decir("final", True)
                        self.cambiar("fin")
                    else:
                        prep = Y2_PREP
                        if self.slot() == 0:
                            prep = Y2_PREP_VUELTA
                            self.poner_aviso("Vuelta " + str(self.tramo // 5 + 1), "#E8E0F2")
                        self.nuevo_tramo(prep)
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

    default vivo = MJY2(params, inicio, fallos, (intento == 1 and inicio == 0))

    timer 0.033 repeat True action Function(vivo.tick)

    key "K_SPACE" action Function(vivo.accion)
    key "K_RETURN" action Function(vivo.accion)

    $ pos = vivo.posiciones()
    $ geo = vivo.geometria()
    $ bat = vivo.testigo()
    $ quien = vivo.quien()
    $ color_q = PETALO_COLOR[quien]
    $ vivos_t = vivo.p["testigos"] - vivo.caidos
    $ en_error = (vivo.fase == "cae" or vivo.fase == "falsa")
    $ en_intro = (vivo.fase == "intro")
    $ lit = int(28 * vivo.tramo / float(vivo.n))
    $ ritmo = vivo.ritmo()
    $ ritmo_txt = "{:.1f}".format(ritmo).replace(".", ",")

    add "bg_pista_atletismo" fit "cover"

    use mj_marco(hermana, titulo, intento, fallos, nivel, vivo.tramo, vivo.n, None, None, "TRAMOS"):

        ## Toda la pantalla es un botón (sirve el toque en móvil). Inactivo en la explicación.
        button:
            xysize (1920, 1080)
            background None
            sensitive (not en_intro)
            action Function(vivo.pulsar)

        fixed at (mj_chibi_tiembla if en_error else y2_quieto):
            xysize (1920, 1080)

            if en_error:
                add Solid("#C0303033")

            ## --- Cabecera ---
            text ("TRAMO " + str(geo["n"]) + " / " + str(vivo.n) + " · " + quien.capitalize()):
                xalign 0.5
                ypos 135
                font gui.name_text_font
                size 44
                kerning 3
                color color_q
                outlines [(5, "#1B1026CC", 0, 0)]

            text ("VUELTA " + str(geo["vuelta"]) + "   ·   " + Y2_NIVEL_TXT[nivel]):
                xalign 0.5
                ypos 196
                size 24
                kerning 3
                color "#E8E0F2"
                outlines [(3, "#1B102699", 0, 0)]

            ## --- Testigos (izquierda) ---
            hbox:
                xpos 60
                ypos 112
                spacing 10
                text "TESTIGOS":
                    size 22
                    color "#FFFFFF"
                    yalign 0.5
                    outlines [(3, "#1B102699", 0, 0)]
                for k in range(vivo.p["testigos"]):
                    if k < vivos_t:
                        add Solid("#FFE3A0", xsize=26, ysize=10) yalign 0.5
                    else:
                        add Solid("#FFFFFF33", xsize=26, ysize=10) yalign 0.5

            ## --- Ritmo y racha (derecha) ---
            vbox:
                xpos 1480
                ypos 150
                spacing 8
                text ("RITMO  ×" + ritmo_txt):
                    font gui.name_text_font
                    size 22
                    kerning 3
                    color "#FFFFFF"
                    outlines [(3, "#1B102699", 0, 0)]
                use barra_progreso(ritmo, 2.2, "#FF9F6B", 360)
                null height 6
                text ("RACHA  " + str(vivo.racha) + " / " + str(vivo.p["cura"])):
                    font gui.name_text_font
                    size 22
                    kerning 3
                    color "#FFF0A8"
                    outlines [(3, "#1B102699", 0, 0)]
                use barra_progreso(vivo.racha, vivo.p["cura"], "#FFE3A0", 360)

            ## --- La pista ---
            add Solid("#B8453CE0", xsize=1720, ysize=190) xpos 110 ypos 610
            add Solid("#FFFFFFB0", xsize=1720, ysize=4) xpos 110 ypos 610
            add Solid("#FFFFFFB0", xsize=1720, ysize=4) xpos 110 ypos 796

            for k in range(6):
                add Solid("#FFFFFFAA", xsize=4, ysize=190) xpos (Y2_X0 + Y2_LONG * k - 2) ypos 610

            ## Las 28 marcas se iluminan con el progreso.
            for k in range(28):
                if k < lit:
                    add Solid("#FFE3A0", xsize=4, ysize=20) xpos (Y2_X0 + int(k * (Y2_LONG * 5) / 27.0)) ypos 586
                else:
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

            ## --- Zona, señuelo y marca del tramo actual ---
            if geo["mostrar"]:
                if geo["zona_visible"]:
                    add Solid(color_q + "66", xsize=geo["zona_w"], ysize=190) xpos geo["zona_x"] ypos 610
                if geo["senuelo_x"] is not None:
                    add Solid("#FF8A8A99", xsize=4, ysize=190) xpos (geo["senuelo_x"] - 2) ypos 610
                    text "×":
                        xpos geo["senuelo_x"]
                        xanchor 0.5
                        ypos 556
                        size 34
                        color "#FF8A8A"
                        outlines [(3, "#1B1026CC", 0, 0)]
                if geo["marca_visible"]:
                    add Solid("#FFE3A0", xsize=6, ysize=190) xpos (geo["marca_x"] - 3) ypos 610 at y2_pulso
                    add Transform(Solid("#FFE3A0", xsize=20, ysize=20), rotate=45) xpos geo["marca_x"] xanchor 0.5 yanchor 0.5 ypos 590 at y2_pulso
                    text "MARCA":
                        xpos geo["marca_x"]
                        xanchor 0.5
                        ypos 538
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
                    ypos 440
                    font gui.name_text_font
                    size 50
                    color vivo.aviso_color
                    outlines [(5, "#1B1026CC", 0, 0)]

        ## --- Yotsuba chibi y sus globos ---
        use mj_retrato("yotsuba", vivo.expresion_star(), vivo.globo, vivo.anim_star(), 250, 560, 0.6)

        ## --- Botón ¡Ahora! ---
        if not en_intro:
            fixed:
                xalign 0.5
                ypos 822
                xysize (420, 84)
                use cinta_boton("¡Ahora!", Function(vivo.pulsar), quien, 420, 84, 38)

        ## --- Pantalla de explicación (solo al empezar) ---
        if en_intro:
            $ reglas = vivo.reglas()

            fixed:
                xalign 0.5
                ypos 100
                xysize (1200, 760)

                add Transform(Frame("ui/opcion_neutra.png", 40, 40, 40, 40), matrixcolor=TintMatrix("#1B1026"))
                add Transform(Frame("ui/opcion_marco.png", 40, 40, 40, 40), matrixcolor=TintMatrix(PETALO_COLOR["yotsuba"]))

                vbox:
                    xalign 0.5
                    ypos 30
                    xsize 1080
                    spacing 12

                    text "EL RELEVO DE LAS CINCO":
                        xalign 0.5
                        font gui.name_text_font
                        size 40
                        kerning 4
                        color "#FFF8FC"

                    text (Y2_NIVEL_TXT[nivel] + "  ·  " + str(vivo.n) + " tramos"):
                        xalign 0.5
                        font gui.name_text_font
                        size 26
                        kerning 3
                        color PETALO_COLOR["yotsuba"]

                    null height 8

                    for r in reglas:
                        text ("•  " + r):
                            size 24
                            color "#E8E0F2"
                            xsize 1080

                fixed:
                    xalign 0.5
                    ypos 665
                    xysize (420, 70)
                    use cinta_boton("Empezar", Function(vivo.empezar), "yotsuba", 420, 70, 34)


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
