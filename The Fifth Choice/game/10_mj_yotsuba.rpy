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
##  una marca por tramo de la carrera (28 en media: el número perfecto).
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
## La pista ocupa todo el ancho del área de juego del marco (x 440–1880).
define Y2_PISTA_X = MJ_AREA_X                 ## 440: x del rectángulo de la pista
define Y2_PISTA_W = MJ_AREA_W                 ## 1440: ancho de la pista
define Y2_X0 = Y2_PISTA_X + 90                ## 530: salida del primer carril (media chibi = 79 px + temblor)
define Y2_LONG = (Y2_PISTA_W - 110) // 5      ## 266: ancho de cada carril; meta en x 1860
define Y2_PISTA_Y = 350       ## y del borde superior de la pista
define Y2_PISTA_H = 400       ## alto de la pista
define Y2_CENTRO = MJ_AREA_CX                 ## 1160: centro de la pista (botón)
define Y2_SUELO = 735         ## línea de los pies de las corredoras
define Y2_ZOOM = 0.58         ## las cinco iguales; el lazo de Yotsuba queda en y ≈ 435
define Y2_ALFA_RESTO = 0.45   ## corredoras que no llevan ni reciben el testigo
define Y2_FRANJA = 6          ## alto de la franja de color de cada carril
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
            self.aviso_tipo = "info"
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
                    self.poner_aviso("Punto de control · tramo " + str(self.tramo + 1), "info")
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

        def poner_aviso(self, texto, tipo):
            """tipo: "bien" | "mal" | "info" (píldora de la franja del marco)."""
            self.aviso = texto
            self.aviso_tipo = tipo
            self.aviso_t = 1.0

        # ---- geometría -------------------------------------------------------
        def x_fin(self, i):
            if i == 4:
                return y2_x(5) - 70
            return y2_x(i + 1) - 90

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
            s_pasa = 0.0
            if f == "pasa":
                s_pasa = self.dt_fase() / Y2_T_PASA
                if s_pasa > 1.0:
                    s_pasa = 1.0
            for i in range(5):
                r = {"h": Y2_ORDEN[i], "expr": "neutral", "anim": "quieto", "zoom": Y2_ZOOM, "x": y2_x(i), "alfa": Y2_ALFA_RESTO}
                ## Legibilidad del traspaso: a pleno solo la portadora y la receptora.
                ## Al soltar el testigo, la que entrega se apaga y se enciende la siguiente receptora.
                if i == T and T == 4:
                    r["alfa"] = 1.0      ## Yotsuba cruza la meta: no entrega a nadie
                elif i == T:
                    r["alfa"] = 1.0 - (1.0 - Y2_ALFA_RESTO) * s_pasa
                elif i == T + 1:
                    r["alfa"] = 1.0
                elif i == T + 2:
                    r["alfa"] = Y2_ALFA_RESTO + (1.0 - Y2_ALFA_RESTO) * s_pasa
                if f == "fin":
                    r["alfa"] = 1.0
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
                        r["x"] = y2_x(i) + 100 * s
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
            """(x, y, giro, portadora) del testigo. portadora = hermana que lo
            lleva (da el color al testigo); cambia a mitad del arco del traspaso."""
            T = self.slot()
            pos = self.posiciones()
            c = pos[T]
            ## En la mano de la portadora (a la altura del pecho), no delante de la receptora.
            bx = c["x"] + 45
            by = Y2_SUELO - 120
            giro = -25
            portadora = Y2_ORDEN[T]
            f = self.fase
            if f == "pasa" and T < 4:
                s = self.dt_fase() / Y2_T_PASA
                if s > 1.0:
                    s = 1.0
                rx = y2_x(T + 1) + 45
                bx = bx + (rx - bx) * s
                by = by - 110.0 * math.sin(math.pi * s)
                giro = -25 + 340 * s
                if s >= 0.5:
                    portadora = Y2_ORDEN[T + 1]
            elif f == "cae":
                s = self.dt_fase() / 0.5
                if s > 1.0:
                    s = 1.0
                by = by + 100.0 * s * s      ## cae hasta los pies, sin salir de la pista
                giro = 70 * s
            return (int(round(bx)), int(round(by)), int(round(giro)), portadora)

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
            mj_sfx("fallo")
            self.caidos += 1
            self.racha = 0
            self.poner_aviso(self.texto(clave_texto), "mal")
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
            mj_sfx("acierto")
            if perfecto:
                self.perfectos += 1
                self.racha += 1
                if self.racha > self.mejor_racha:
                    self.mejor_racha = self.racha
                self.poner_aviso("¡Perfecto!", "bien")
            else:
                self.racha = 0
                self.poner_aviso(self.texto("ok"), "bien")

            curo = False
            if self.racha >= cura:
                if self.caidos > 0:
                    self.caidos -= 1
                    self.curados += 1
                    self.racha = 0
                    curo = True
                    self.poner_aviso("¡Testigo recuperado!", "bien")
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
                self.poner_aviso("Todavía no.", "info")
                return None
            if modo == "avisa" and not self.gratis.get(self.tramo, False):
                self.gratis[self.tramo] = True
                self.poner_aviso(self.texto("falsa"), "info")
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
                            self.poner_aviso("Vuelta " + str(self.tramo // 5 + 1), "info")
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
    $ T = vivo.slot()
    $ quien = vivo.quien()
    $ color_q = PETALO_COLOR[quien]
    $ vivos_t = vivo.p["testigos"] - vivo.caidos
    $ en_error = (vivo.fase == "cae" or vivo.fase == "falsa")
    $ en_intro = (vivo.fase == "intro")
    $ ritmo = vivo.ritmo()
    $ ritmo_txt = "{:.1f}".format(ritmo).replace(".", ",")
    $ py = Y2_PISTA_Y
    $ ph = Y2_PISTA_H
    $ pw = Y2_PISTA_W
    $ meta_x = Y2_X0 + Y2_LONG * 5
    $ aviso = ""
    if vivo.aviso_t > 0.0:
        $ aviso = vivo.aviso
    $ b = MJ_BOTON["primario"]

    add "bg_pista_atletismo" fit "cover"

    use mj_marco(hermana, titulo, intento, fallos, nivel, vivo.tramo, vivo.n, None, None, "TRAMOS", vidas=vivos_t, vidas_max=vivo.p["testigos"], vidas_txt="TESTIGOS", chibi=vivo.expresion_star(), globo=vivo.globo, anim=vivo.anim_star(), aviso=aviso, aviso_tipo=vivo.aviso_tipo):

        ## Toda la pantalla es un botón (sirve el toque en móvil). Inactivo en la explicación.
        ## Sin hover_sound a propósito: sonaría cada vez que el ratón entra en la pantalla.
        button:
            xpos 0
            ypos 0
            xysize (1920, 1080)
            background None
            sensitive (not en_intro)
            action Function(vivo.pulsar)

        ## --- Cabecera: quién corre (izquierda) · ritmo y racha (derecha) ---
        vbox:
            xpos (MJ_AREA_X + 20)
            ypos (MJ_AREA_Y + 16)
            spacing 2
            text "CORRE" style "mj_etiqueta"
            text quien.capitalize() style "mj_titulo" color color_q

        vbox:
            xpos (MJ_AREA_X + MJ_AREA_W - 20 - MJ_HUD_ANCHO)
            ypos (MJ_AREA_Y + 16)
            xsize MJ_HUD_ANCHO
            spacing 6
            use mj_hud_fila("RITMO", "×" + ritmo_txt)
            use barra_progreso(ritmo, 2.2, "#FF9F6B", MJ_HUD_ANCHO)
            null height 6
            use mj_hud_fila("RACHA", str(vivo.racha) + " / " + str(vivo.p["cura"]), "#FFF0A8")
            use barra_progreso(vivo.racha, vivo.p["cura"], "#FFE3A0", MJ_HUD_ANCHO)

        ## --- La pista (todo el ancho del área) ---
        add Solid("#B8453CE0", xsize=pw, ysize=ph) xpos Y2_PISTA_X ypos py
        if en_error:
            add Solid("#C0303033", xsize=pw, ysize=ph) xpos Y2_PISTA_X ypos py
        add Solid("#FFFFFFB0", xsize=pw, ysize=4) xpos Y2_PISTA_X ypos py
        add Solid("#FFFFFFB0", xsize=pw, ysize=4) xpos Y2_PISTA_X ypos (py + ph - 4)

        ## Cinco carriles iguales, cada uno con la franja de su corredora.
        for k in range(5):
            add Solid(PETALO_COLOR[Y2_ORDEN[k]], xsize=Y2_LONG, ysize=Y2_FRANJA) xpos (Y2_X0 + Y2_LONG * k) ypos (py + ph - 4 - Y2_FRANJA)

        for k in range(6):
            add Solid("#FFFFFFAA", xsize=4, ysize=ph) xpos (Y2_X0 + Y2_LONG * k - 2) ypos py

        ## Una marca por tramo de la carrera real (14, 28, 56… o los intermedios
        ## de la asistencia); la última cae sobre la meta. Se encienden al avanzar.
        for k in range(vivo.n):
            $ mx = Y2_X0 + int((k + 1) * Y2_LONG * 5 / float(vivo.n))
            if k < vivo.tramo:
                add Solid("#FFE3A0", xsize=4, ysize=20) xpos (mx - 2) ypos (py - 24)
            else:
                add Solid("#FFFFFF77", xsize=3, ysize=14) xpos (mx - 1) ypos (py - 18)

        add Solid("#FFFFFF", xsize=8, ysize=ph) xpos (meta_x - 4) ypos py

        ## --- Zona, señuelo y marca del tramo actual ---
        if geo["mostrar"]:
            if geo["zona_visible"]:
                add Solid(color_q + "66", xsize=geo["zona_w"], ysize=ph) xpos geo["zona_x"] ypos py
            if geo["senuelo_x"] is not None:
                add Solid("#FF8A8A99", xsize=4, ysize=ph) xpos (geo["senuelo_x"] - 2) ypos py
                text "×":
                    style "mj_cifra"
                    color "#FF8A8A"
                    xpos geo["senuelo_x"]
                    xanchor 0.5
                    ypos (py - 52)
            if geo["marca_visible"]:
                add Solid("#FFE3A0", xsize=6, ysize=ph) xpos (geo["marca_x"] - 3) ypos py at y2_pulso
                add Transform(Solid("#FFE3A0", xsize=20, ysize=20), rotate=45) xpos geo["marca_x"] xanchor 0.5 yanchor 0.5 ypos (py - 12) at y2_pulso
                text "MARCA":
                    style "mj_etiqueta"
                    color "#FFE3A0"
                    xpos geo["marca_x"]
                    xanchor 0.5
                    ypos (py - 62)

        ## --- Las cinco corredoras: la portadora, delante de todas ---
        for r in pos:
            if r["h"] != quien:
                use mj_chibi_vista(r["h"], r["expr"], r["x"], Y2_SUELO, r["zoom"], r["anim"], r["alfa"])
        $ rq = pos[T]
        use mj_chibi_vista(rq["h"], rq["expr"], rq["x"], Y2_SUELO, rq["zoom"], rq["anim"], rq["alfa"])

        ## El testigo, encima de todo y del color de quien lo lleva.
        if bat is not None:
            add Transform(Fixed(
                Solid("#1B1026", xsize=90, ysize=24),
                Transform(Solid("#FFFFFF", xsize=84, ysize=18), xpos=3, ypos=3),
                Transform(Solid(PETALO_COLOR[bat[3]], xsize=78, ysize=12), xpos=6, ypos=6),
                xysize=(90, 24)), rotate=bat[2]) xpos bat[0] ypos bat[1] xanchor 0.5 yanchor 0.5

        ## --- Botón ¡Ahora!, centrado bajo la pista (fuera en la intro y en la celebración final) ---
        if not en_intro and vivo.fase != "fin":
            fixed:
                xpos Y2_CENTRO
                xanchor 0.5
                ypos 790
                xysize (b[0], b[1])
                use cinta_boton("¡Ahora!", Function(vivo.pulsar), quien, b[0], b[1], b[2])

        ## --- Pantalla de explicación (solo al empezar), dentro del área ---
        if en_intro:
            $ reglas = vivo.reglas()

            add Solid("#0B0712CC", xsize=MJ_AREA_W, ysize=MJ_AREA_H) xpos MJ_AREA_X ypos MJ_AREA_Y

            frame:
                xpos MJ_AREA_CX
                xanchor 0.5
                ypos (MJ_AREA_Y + MJ_AREA_H // 2)
                yanchor 0.5
                xsize 1360
                ymaximum MJ_AREA_H
                padding (60, 40, 60, 40)
                background Fixed(
                    Transform(Frame("ui/opcion_neutra.png", 40, 40, 40, 40), matrixcolor=TintMatrix("#1B1026")),
                    Transform(Frame("ui/opcion_marco.png", 40, 40, 40, 40), matrixcolor=TintMatrix(PETALO_COLOR["yotsuba"])))

                vbox:
                    xsize 1240
                    spacing 14

                    text "EL RELEVO DE LAS CINCO":
                        style "mj_titulo"
                        xalign 0.5

                    text (Y2_NIVEL_TXT[nivel] + "  ·  " + str(vivo.n) + " TRAMOS"):
                        style "mj_etiqueta"
                        color PETALO_COLOR["yotsuba"]
                        xalign 0.5

                    null height 6

                    for r in reglas:
                        hbox:
                            spacing 14
                            text "•" style "mj_cuerpo"
                            text r:
                                style "mj_cuerpo"
                                xsize 1210

                    null height 18

                    fixed:
                        xalign 0.5
                        xysize (b[0], b[1])
                        use cinta_boton("Empezar", Function(vivo.empezar), "yotsuba", b[0], b[1], b[2])


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

    call mj_ejecutar("y2", "yotsuba") from _call_mj_ejecutar_10

    $ y2_res = _return
    $ y2_info = e6_mj["yotsuba"]
    $ narrator("Resultado: " + str(y2_res) + " · intentos " + str(y2_info["intentos"]) + " · fallos " + str(y2_info["fallos"]) + " · nivel " + y2_info["nivel"] + " · caídos " + str(y2_info["datos"].get("caidos", 0)))
    return
