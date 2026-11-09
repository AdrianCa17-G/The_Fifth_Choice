################################################################################
##  10_mj_nino.rpy — N1′ · Compras para seis (Evento 6, bloque de Nino)
##
##  Cinco listas, una por hermana (Ichika, Yotsuba, Miku, Itsuki, Nino), tres
##  productos cada una. Todo está en inglés, como lo lee Nino. La traducción al
##  español aparece sola tras `retardo_traduccion` segundos desde que se abre
##  cada lista («traduce sin darse cuenta»).
##  Cada producto está en un estante con `distractores` cajas casi idénticas
##  (caster sugar / confectioners' sugar…). Elegir mal quita `penalizacion`
##  segundos y bloquea esa caja. El tiempo es común a todo el intento.
##  Tras la quinta lista queda un SEXTO HUECO en la cesta: tres opciones, sin
##  respuesta correcta. Se anota en datos["sexto"]:
##      "taza"  Escribir «una taza más»
##      "blanco"  "Dejarlo en blanco
##      "cuando"     Anotar «cuando se sepa»
##  El guion lee e6_mj["nino"]["datos"]["sexto"] para decidir la línea.
##
##  Parámetros: MJ_PARAMS["n1"] (10_minijuegos.rpy).
##    tiempo_total, retardo_traduccion, distractores, penalizacion,
##    puntos_control (listas completadas).
##  Si se reanuda desde un punto de control, el tiempo se reduce en
##  proporción a las listas que faltan (mínimo el 40 %).
##
##  Devuelve: "ganado" | "perdido" | "saltado".
################################################################################

define N1_VENTANA_W = 1210
define N1_CAJA_W = 272
define N1_CAJA_H = 112
define N1_FILA_Y0 = 186
define N1_FILA_H = 166
define N1_CUENTA_S = 0.7
define N1_RACHA_N = 3

define MJ_N1_ITEMS = {
    "honey": "miel",
    "maple syrup": "sirope de arce",
    "golden syrup": "sirope dorado",
    "corn syrup": "jarabe de maíz",
    "chamomile tea": "té de manzanilla",
    "green tea": "té verde",
    "matcha powder": "matcha en polvo",
    "jasmine tea": "té de jazmín",
    "black tea": "té negro",
    "instant oats": "avena instantánea",
    "rolled oats": "copos de avena",
    "oat bran": "salvado de avena",
    "oat flour": "harina de avena",
    "energy bars": "barritas energéticas",
    "granola bars": "barritas de granola",
    "protein bars": "barritas de proteína",
    "cereal bars": "barritas de cereales",
    "peanut butter": "mantequilla de cacahuete",
    "unsalted butter": "mantequilla sin sal",
    "salted butter": "mantequilla con sal",
    "clarified butter": "mantequilla clarificada",
    "whole milk": "leche entera",
    "skimmed milk": "leche desnatada",
    "evaporated milk": "leche evaporada",
    "condensed milk": "leche condensada",
    "sea salt": "sal marina",
    "table salt": "sal de mesa",
    "rock salt": "sal gruesa",
    "pink salt": "sal rosa",
    "sesame seeds": "semillas de sésamo",
    "poppy seeds": "semillas de amapola",
    "chia seeds": "semillas de chía",
    "flax seeds": "semillas de lino",
    "bread flour": "harina de fuerza",
    "plain flour": "harina común",
    "self-raising flour": "harina con levadura",
    "cake flour": "harina para repostería",
    "whole wheat flour": "harina integral",
    "vanilla extract": "extracto de vainilla",
    "vanilla essence": "esencia de vainilla",
    "vanilla pods": "vainas de vainilla",
    "vanilla paste": "pasta de vainilla",
    "confectioners' sugar": "azúcar glas",
    "caster sugar": "azúcar extrafino",
    "brown sugar": "azúcar moreno",
    "granulated sugar": "azúcar granulado",
    "vanilla sugar": "azúcar avainillado",
    "baking powder": "levadura química",
    "baking soda": "bicarbonato",
    "instant yeast": "levadura instantánea",
    "cream of tartar": "crémor tártaro",
}

## Grupos de productos que se confunden entre sí. Los distractores de un
## estante salen del mismo grupo que el producto pedido.
define MJ_N1_GRUPOS = [
    ["honey", "maple syrup", "golden syrup", "corn syrup"],
    ["chamomile tea", "green tea", "matcha powder", "jasmine tea", "black tea"],
    ["instant oats", "rolled oats", "oat bran", "oat flour"],
    ["energy bars", "granola bars", "protein bars", "cereal bars"],
    ["peanut butter", "unsalted butter", "salted butter", "clarified butter"],
    ["whole milk", "skimmed milk", "evaporated milk", "condensed milk"],
    ["sea salt", "table salt", "rock salt", "pink salt"],
    ["sesame seeds", "poppy seeds", "chia seeds", "flax seeds"],
    ["bread flour", "plain flour", "self-raising flour", "cake flour", "whole wheat flour"],
    ["vanilla extract", "vanilla essence", "vanilla pods", "vanilla paste"],
    ["confectioners' sugar", "caster sugar", "brown sugar", "granulated sugar", "vanilla sugar"],
    ["baking powder", "baking soda", "instant yeast", "cream of tartar"],
]

## (hermana, [tres productos]). El orden es el del capítulo.
define MJ_N1_LISTAS = [
    ("ichika",  ["honey", "chamomile tea", "instant oats", "plain flour"]),
    ("yotsuba", ["energy bars", "peanut butter", "whole milk", "chia seeds"]),
    ("miku",    ["matcha powder", "sea salt", "sesame seeds", "granulated sugar"]),
    ("itsuki",  ["bread flour", "unsalted butter", "maple syrup", "instant yeast"]),
    ("nino",    ["vanilla extract", "confectioners' sugar", "baking powder", "evaporated milk"]),
]

## (clave, título, subtítulo)
define MJ_N1_SEXTO = [
    ("taza",   "Escribir «una taza más»", "Se compra igual aunque nadie la pida."),
    ("blanco", "Dejarlo en blanco",       "Sin tachar."),
    ("cuando", "Anotar «cuando se sepa»", "Con el resultado en la mano."),
]

init python:

    import math

    MJ_N1_GRUPO_DE = {}
    for _g in MJ_N1_GRUPOS:
        for _k in _g:
            MJ_N1_GRUPO_DE[_k] = _g

    def n1_mascara(clave):
        """'chamomile tea' -> 'c········ ···' (primera letra y huecos)."""
        res = clave[0]
        for ch in clave[1:]:
            if ch == " ":
                res = res + " "
            else:
                res = res + "·"
        return res

    def n1_ritmo(nivel):
        if nivel == "dificil":
            return 3
        if nivel == "media":
            return 2
        return 1

    def n1_reglas(p):
        """Reglas de la pantalla de explicación, según los parámetros vigentes."""
        reglas = []
        reglas.append(("LEE LA LISTA", "Cada pedido está en inglés y las cajas se parecen mucho. Busca la que dice EXACTAMENTE lo mismo."))

        partes = []
        if p["deriva"] > 0:
            partes.append("Los estantes se deslizan como una cinta.")
        if p["mezclado"]:
            partes.append("Las cajas están revueltas entre estantes.")
        if len(partes) == 0:
            partes.append("Cada estante guarda productos parecidos.")
        if p["memoria"] < 99.0:
            partes.append("La lista se esconde a los " + "{:g}".format(p["memoria"]) + " s: memorízala o mírala de nuevo (-" + "{:g}".format(p["mirar_costo"]) + " s).")
        reglas.append(("BUSCA RÁPIDO", " ".join(partes)))

        reglas.append(("NO TE EQUIVOQUES", "Cada error resta " + "{:g}".format(p["penalizacion"]) + " s y bloquea esa caja. Cada " + str(N1_RACHA_N) + " aciertos seguidos suman +" + "{:g}".format(p["racha_bonus"]) + " s."))
        reglas.append(("EL SEXTO HUECO", "Tras la quinta lista queda un hueco en la cesta. Ahí no hay respuesta correcta: elige tú."))
        return reglas

    class MJN1(object):
        """N1′ — Compras para seis. Estado vivo: lo crea la screen (default); no se guarda.
        fase: listo | cuenta | compras | ok | sexto | fin | perdiendo"""

        def __init__(self, params, inicio, fallos_previos, intento=1):
            self.p = params
            self.reloj = MJReloj()
            self.fallos_prev = fallos_previos

            if inicio > 4:
                inicio = 4
            self.lista = inicio

            n = int(round(params["productos"]))
            if n < 2:
                n = 2
            if n > 4:
                n = 4
            self.n_prod = n

            d = int(round(params["distractores"]))
            if d < 1:
                d = 1
            if d > 3:
                d = 3
            self.n_dist = d

            self.mezclado = bool(params["mezclado"])
            self.deriva = float(params["deriva"])
            self.memoria = float(params["memoria"])
            self.mirar_costo = float(params["mirar_costo"])
            self.bonus = float(params["racha_bonus"])

            base = float(params["tiempo_total"])
            tiempo = base * ((5 - inicio) / 5.0)
            if tiempo < base * 0.4:
                tiempo = base * 0.4
            if inicio > 0:
                tiempo = tiempo + 5.0
            self.total = tiempo

            self.gastado = 0.0
            self.penal = 0.0
            self.t_deriva = 0.0
            self.errores = 0
            self.racha = 0
            self.mejor_racha = 0
            self.mirones = 0
            self.sexto = ""
            self.mirada_t = 0.0
            self.popup_txt = ""
            self.popup_col = "#FFFFFF"
            self.popup_t = 0.0
            self.flash_t = 0.0
            self.humor = ""
            self.humor_t = 0.0
            self.avisado_tiempo = False
            self.globo = MJGlobo("nino")

            self.t_fase = 0.0
            self.idx = 0
            self.hermana_lista = "ichika"
            self.claves = []
            self.encontrados = []
            self.malos = []
            self.estantes = []
            self.g0 = 0.0
            self.entrar_lista(inicio)

            if intento <= 1:
                self.fase = "listo"
            else:
                self.cambiar("cuenta")

        # ---- utilidades ------------------------------------------------------
        def cambiar(self, fase):
            self.fase = fase
            self.t_fase = self.reloj.t

        def restante(self):
            r = self.total - self.gastado - self.penal
            if r < 0.0:
                r = 0.0
            return r

        def tension(self):
            return self.fase == "compras" and self.restante() < 15.0

        def pulso(self):
            return 0.5 + 0.5 * math.sin(self.reloj.t * 6.0)

        def cuenta_n(self):
            rest = N1_CUENTA_S * 3 - (self.reloj.t - self.t_fase)
            n = int(rest / N1_CUENTA_S) + 1
            if n > 3:
                n = 3
            if n < 1:
                n = 1
            return n

        def poner_humor(self, que, seg):
            self.humor = que
            self.humor_t = seg

        def popup(self, texto, color):
            self.popup_txt = texto
            self.popup_col = color
            self.popup_t = 1.2

        # ---- listas y estantes -----------------------------------------------
        def entrar_lista(self, idx):
            self.idx = idx
            datos = MJ_N1_LISTAS[idx]
            self.hermana_lista = datos[0]
            self.claves = list(datos[1][:self.n_prod])
            self.encontrados = []
            self.malos = []
            self.mirada_t = 0.0

            por_producto = []
            for k in self.claves:
                grupo = MJ_N1_GRUPO_DE[k]
                otros = []
                for x in grupo:
                    if x != k:
                        otros.append(x)
                renpy.random.shuffle(otros)
                cajas = [k]
                for x in otros[:self.n_dist]:
                    cajas.append(x)
                por_producto.append(cajas)

            if self.mezclado:
                todas = []
                for cajas in por_producto:
                    for c in cajas:
                        todas.append(c)
                renpy.random.shuffle(todas)
                filas = []
                for i in range(len(self.claves)):
                    filas.append([])
                for i in range(len(todas)):
                    filas[i % len(filas)].append(todas[i])
                self.estantes = filas
            else:
                for cajas in por_producto:
                    renpy.random.shuffle(cajas)
                renpy.random.shuffle(por_producto)
                self.estantes = por_producto

            self.g0 = self.gastado

        def cajas_fila(self, fi):
            """[(clave, x), ...] de la fila fi. Con deriva, la cinta da la vuelta:
            la caja que sale por la derecha reaparece por la izquierda."""
            cajas = self.estantes[fi]
            n = len(cajas)
            periodo = float(N1_VENTANA_W)
            paso = periodo / n
            centro = (paso - N1_CAJA_W) / 2.0
            sentido = 1.0
            if fi % 2 == 1:
                sentido = -1.0
            vel = self.deriva * (1.0 + 0.15 * fi)
            desplazo = sentido * vel * self.t_deriva
            res = []
            for k in range(n):
                x = (k * paso + centro + desplazo) % periodo
                res.append((cajas[k], int(x)))
                if x + N1_CAJA_W > periodo:
                    res.append((cajas[k], int(x - periodo)))
            return res

        def estado_caja(self, clave):
            if clave in self.encontrados:
                return "ok"
            if clave in self.malos:
                return "mal"
            return "libre"

        def trad_alpha(self):
            ret = float(self.p["retardo_traduccion"])
            if ret <= 0.0:
                return 1.0
            t = self.gastado - self.g0 - ret
            if t <= 0.0:
                return 0.0
            a = t / 0.4
            if a > 1.0:
                a = 1.0
            return a

        # ---- memoria (la lista se esconde) -----------------------------------
        def lista_visible(self):
            if self.memoria >= 99.0:
                return True
            if self.fase != "compras":
                return True
            if self.mirada_t > 0.0:
                return True
            if (self.gastado - self.g0) < self.memoria:
                return True
            return False

        def memoria_restante(self):
            if self.memoria >= 99.0 or self.fase != "compras":
                return -1.0
            r = self.memoria - (self.gastado - self.g0)
            if r < 0.0:
                r = 0.0
            return r

        def mirar(self):
            if self.fase != "compras":
                return None
            if self.lista_visible():
                return None
            self.penal += self.mirar_costo
            self.mirada_t = 1.6
            self.mirones += 1
            self.popup("-" + "{:g}".format(self.mirar_costo) + " s", "#FFE3A0")
            self.globo.decir("mirar", True)
            if self.restante() <= 0.0:
                return self.perder()
            return None

        # ---- flujo -----------------------------------------------------------
        def empezar(self):
            if self.fase != "listo":
                return None
            self.cambiar("cuenta")
            return None

        def resultado(self, que):
            return {
                "resultado": que,
                "progreso": self.lista,
                "datos": {"sexto": self.sexto, "errores": self.errores, "sobra": int(self.restante()),
                          "racha": self.mejor_racha, "mirones": self.mirones},
            }

        def perder(self):
            self.poner_humor("triste", 5.0)
            if MJ_FALLO_EN_GLOBO:
                self.globo.poner(mj_texto_fallo("nino", self.fallos_prev), 1.6)
            else:
                self.globo.decir("fallo", True)
            self.cambiar("perdiendo")
            return None

        # ---- entrada ---------------------------------------------------------
        def elegir(self, clave):
            if self.fase != "compras":
                return None
            if clave in self.encontrados or clave in self.malos:
                return None

            if clave in self.claves:
                self.encontrados.append(clave)
                self.racha += 1
                if self.racha > self.mejor_racha:
                    self.mejor_racha = self.racha
                if self.racha % N1_RACHA_N == 0 and self.bonus > 0.0:
                    self.total += self.bonus
                    self.popup("+" + "{:g}".format(self.bonus) + " s", "#CFFFD8")
                    self.globo.decir("racha", True)
                else:
                    self.globo.decir("acierto")
                if len(self.encontrados) >= len(self.claves):
                    self.lista += 1
                    if self.lista == 3:
                        self.globo.decir("mitad", True)
                    elif self.lista == 4:
                        self.globo.decir("casi", True)
                    else:
                        self.globo.decir("lista", True)
                    self.cambiar("ok")
                return None

            self.malos.append(clave)
            self.errores += 1
            self.racha = 0
            pen = float(self.p["penalizacion"])
            self.penal += pen
            self.popup("-" + "{:g}".format(pen) + " s", "#FFC4C4")
            self.flash_t = 0.35
            self.globo.decir("fallo", True)
            self.poner_humor("triste", 0.9)
            if self.restante() <= 0.0:
                return self.perder()
            return None

        def elegir_sexto(self, clave):
            if self.fase != "sexto":
                return None
            self.sexto = clave
            self.globo.decir("final", True)
            self.cambiar("fin")
            return None

        def tick(self):
            dt = self.reloj.avanzar()
            self.globo.avanzar(dt)
            if self.popup_t > 0.0:
                self.popup_t -= dt
            if self.flash_t > 0.0:
                self.flash_t -= dt
            if self.mirada_t > 0.0:
                self.mirada_t -= dt
            if self.humor_t > 0.0:
                self.humor_t -= dt
                if self.humor_t <= 0.0 and self.fase != "perdiendo":
                    self.humor = ""
            f = self.fase

            if f == "listo":
                return None

            if f == "cuenta":
                if self.reloj.t - self.t_fase >= N1_CUENTA_S * 3:
                    self.cambiar("compras")
                    self.globo.decir("inicio", True)
                return None

            if f == "compras":
                self.gastado += dt
                self.t_deriva += dt
                if self.restante() <= 0.0:
                    return self.perder()
                if self.restante() < 15.0 and not self.avisado_tiempo:
                    self.avisado_tiempo = True
                    self.globo.decir("tiempo", True)
                return None

            if f == "ok":
                if self.reloj.t - self.t_fase >= 0.7:
                    if self.lista >= 5:
                        self.globo.decir("sexto", True)
                        self.cambiar("sexto")
                    else:
                        self.entrar_lista(self.lista)
                        self.cambiar("compras")
                return None

            if f == "perdiendo":
                if self.reloj.t - self.t_fase >= 1.6:
                    return self.resultado("perdido")
                return None

            if f == "fin":
                self.humor = "feliz"
                if self.reloj.t - self.t_fase >= 1.5:
                    return self.resultado("ganado")
            return None

        def expresion_star(self):
            if self.humor == "" and self.tension():
                return "esfuerzo"
            return mj_chibi_expresion(self.lista, 5, self.humor)

        def anim_star(self):
            if self.humor == "feliz":
                return "salto"
            if self.humor == "triste":
                return "tiembla"
            return "bob"

    mj_registrar("n1", "mj_n1", "Compras para seis", True)


################################################################################
##  SCREENS
################################################################################

## Una caja de un estante. estado: libre | ok | mal
transform n1_entrada:
    alpha 0.0
    ease 0.3 alpha 1.0


## Una pastilla de información (tiempo, productos…).
screen mj_n1_chip(texto, color):

    frame:
        padding (22, 8, 22, 8)
        background Fixed(
            Transform(Frame("ui/opcion_neutra.png", 40, 40, 40, 40), matrixcolor=TintMatrix("#1B1026")),
            Transform(Frame("ui/opcion_marco.png", 40, 40, 40, 40), matrixcolor=TintMatrix(color)))

        text texto:
            size 22
            kerning 2
            color "#F3EEFA"
            substitute False


## Pantalla de explicación (primer intento).
screen mj_n1_intro(vivo, nivel):

    $ color = PETALO_COLOR["nino"]
    $ tinta = ui_mezclar(color, "#000000", 0.75)
    $ reglas = n1_reglas(vivo.p)
    $ ritmo = n1_ritmo(nivel)

    fixed:
        xalign 0.5
        ypos 150
        xysize (1180, 660)
        at n1_entrada

        add Transform(Frame("ui/opcion_neutra.png", 40, 40, 40, 40), matrixcolor=TintMatrix("#1B1026"))
        add Transform(Frame("ui/opcion_marco.png", 40, 40, 40, 40), matrixcolor=TintMatrix(color))

        text "COMPRAS PARA SEIS":
            xalign 0.5
            ypos 26
            font gui.name_text_font
            size 42
            kerning 4
            color "#FFF8FC"

        hbox:
            xalign 0.5
            ypos 92
            spacing 16

            use mj_n1_chip(("TIEMPO  " + "{:g}".format(vivo.total) + " s"), color)
            use mj_n1_chip(("5 LISTAS · " + str(vivo.n_prod) + " PRODUCTOS"), color)

            frame:
                padding (22, 8, 22, 8)
                background Fixed(
                    Transform(Frame("ui/opcion_neutra.png", 40, 40, 40, 40), matrixcolor=TintMatrix("#1B1026")),
                    Transform(Frame("ui/opcion_marco.png", 40, 40, 40, 40), matrixcolor=TintMatrix(color)))

                hbox:
                    spacing 8
                    text "RITMO" size 22 kerning 2 color "#F3EEFA" yalign 0.5
                    for i in range(3):
                        $ alfa_f = 0.22
                        if i < ritmo:
                            $ alfa_f = 1.0
                        add Transform("ui/flor.png", matrixcolor=TintMatrix(color), zoom=0.5, alpha=alfa_f) yalign 0.5

        vbox:
            xpos 60
            ypos 170
            spacing 14

            for i, r in enumerate(reglas):
                hbox:
                    spacing 24

                    fixed:
                        xysize (64, 64)
                        add Transform("ui/flor.png", matrixcolor=TintMatrix(color), zoom=1.15) align (0.5, 0.5)
                        text str(i + 1):
                            align (0.5, 0.5)
                            font gui.name_text_font
                            size 28
                            color tinta

                    vbox:
                        spacing 2
                        xsize 960
                        text r[0]:
                            font gui.name_text_font
                            size 26
                            kerning 3
                            color color
                        text r[1]:
                            size 23
                            color "#E8E0F2"
                            substitute False

        fixed:
            xalign 0.5
            ypos 556
            xysize (420, 80)
            use cinta_boton("Empezar", Function(vivo.empezar), "nino", 420, 80, 34)

        text "Enter o Espacio":
            xalign 0.5
            ypos 634
            size 18
            kerning 3
            color "#FFFFFF77"


## Una caja de un estante. estado: libre | ok | mal
screen mj_n1_caja(clave, estado, accion, trad_color, color):

    $ es_txt = MJ_N1_ITEMS[clave]
    $ fondo = "#2B1B3F"
    $ borde = color
    $ marca = ""
    $ hover = ui_mezclar(color, "#000000", 0.55)
    if estado == "ok":
        $ fondo = "#1E5A3A"
        $ borde = "#58D68D"
        $ marca = "OK"
    elif estado == "mal":
        $ fondo = "#4A2020"
        $ borde = "#7A4040"
        $ marca = "NO"

    button:
        xysize (N1_CAJA_W, N1_CAJA_H)
        sensitive (estado == "libre")
        action accion
        hover_sound audio.sfx_hover
        activate_sound audio.sfx_click
        background Fixed(
            Transform(Frame("ui/opcion_neutra.png", 40, 40, 40, 40), matrixcolor=TintMatrix(fondo)),
            Transform(Frame("ui/opcion_marco.png", 40, 40, 40, 40), matrixcolor=TintMatrix(borde)))
        hover_background Fixed(
            Transform(Frame("ui/opcion_neutra.png", 40, 40, 40, 40), matrixcolor=TintMatrix(hover)),
            Transform(Frame("ui/opcion_marco.png", 40, 40, 40, 40), matrixcolor=TintMatrix("#FFFFFF")))

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 2
            text clave:
                xalign 0.5
                text_align 0.5
                xmaximum (N1_CAJA_W - 28)
                size 25
                color "#FFFFFF"
                substitute False
            text es_txt:
                xalign 0.5
                text_align 0.5
                size 19
                color trad_color

        if marca != "":
            text marca:
                xpos 14
                ypos 8
                size 18
                kerning 3
                color borde


screen mj_n1(hermana, params, inicio, intento, fallos, nivel, titulo):

    modal True
    zorder 95

    default vivo = MJN1(params, inicio, fallos, intento)

    timer 0.033 repeat True action Function(vivo.tick)

    key "K_RETURN" action Function(vivo.empezar)
    key "K_SPACE" action Function(vivo.empezar)

    $ col_l = PETALO_COLOR[vivo.hermana_lista]
    $ tono_l = TARJETA_TONO[vivo.hermana_lista]
    $ ta = vivo.trad_alpha()
    $ trad_color = "#CFC6E0" + "{:02x}".format(int(255 * ta))
    $ en_sexto = (vivo.fase == "sexto" or vivo.fase == "fin")
    $ urgente = vivo.tension()
    $ lista_ok = vivo.lista_visible()
    $ mem_r = vivo.memoria_restante()

    add "bg_centro_comercial" fit "cover"

    use mj_marco(hermana, titulo, intento, fallos, nivel, vivo.lista, 5, vivo.restante(), vivo.total, "LISTAS"):

        ## --- Efectos de tensión (encima del velo del marco) ---
        if urgente:
            add Solid("#FF2D2D") alpha (0.05 + 0.10 * vivo.pulso())

        if vivo.flash_t > 0.0:
            add Solid("#FF3B3B") alpha (0.30 * vivo.flash_t / 0.35)

        if vivo.fase == "listo":

            use mj_n1_intro(vivo, nivel)

        else:

            ## --- Cronómetro grande, racha y popups ---
            $ col_t = "#FFFFFF"
            if urgente:
                $ col_t = "#FF8A8A"

            text ("%.1f" % vivo.restante()):
                xalign 0.5
                ypos 56
                font gui.name_text_font
                size 62
                color col_t
                outlines [(5, "#1B1026CC", 0, 0)]

            text "SEGUNDOS":
                xalign 0.5
                ypos 138
                size 18
                kerning 4
                color "#FFFFFFAA"

            if vivo.racha >= 2:
                text ("RACHA x" + str(vivo.racha)):
                    xpos 800
                    xanchor 1.0
                    ypos 84
                    font gui.name_text_font
                    size 30
                    color "#FFE3A0"
                    outlines [(4, "#1B1026CC", 0, 0)]

            if vivo.popup_t > 0.0:
                $ pa = vivo.popup_t / 0.4
                if pa > 1.0:
                    $ pa = 1.0
                $ col_p = vivo.popup_col + "{:02x}".format(int(255 * pa))
                text vivo.popup_txt:
                    xpos 1130
                    ypos 80
                    font gui.name_text_font
                    size 40
                    color col_p
                    outlines [(4, "#1B1026CC", 0, 0)]

            ## --- La lista de la hermana ---
            fixed:
                xpos 60
                ypos 170
                xysize (540, 400)

                add Transform(Frame("ui/opcion_neutra.png", 40, 40, 40, 40), matrixcolor=TintMatrix(tono_l))
                add Transform(Frame("ui/opcion_marco.png", 40, 40, 40, 40), matrixcolor=TintMatrix(col_l))

                text ("LISTA " + str(vivo.idx + 1) + "/5 · " + vivo.hermana_lista.capitalize()):
                    xpos 36
                    ypos 22
                    font gui.name_text_font
                    size 30
                    kerning 2
                    color col_l

                vbox:
                    xpos 36
                    ypos 78
                    spacing 10

                    for k in vivo.claves:
                        $ hecho = k in vivo.encontrados
                        hbox:
                            spacing 16
                            if hecho:
                                add Solid("#58D68D", xsize=24, ysize=24) yalign 0.5
                            else:
                                add Solid("#FFFFFF33", xsize=24, ysize=24) yalign 0.5
                            vbox:
                                spacing 0
                                if hecho:
                                    text k size 29 color "#8EE8B0" substitute False
                                elif lista_ok:
                                    text k size 29 color "#FFFFFF" substitute False
                                    text MJ_N1_ITEMS[k] size 19 color trad_color
                                else:
                                    text n1_mascara(k) size 29 color "#B9A8D8" substitute False

                    hbox:
                        spacing 16
                        if vivo.sexto != "":
                            add Solid("#58D68D", xsize=24, ysize=24) yalign 0.5
                        else:
                            add Solid("#FFFFFF22", xsize=24, ysize=24) yalign 0.5
                        text "6.º hueco de la cesta" size 24 color "#FFE3A0"

                if mem_r >= 0.0:
                    if vivo.mirada_t > 0.0:
                        text "MIRANDO...":
                            xpos 36
                            ypos 356
                            size 20
                            kerning 3
                            color "#FFE3A0"
                    elif lista_ok:
                        vbox:
                            xpos 36
                            ypos 344
                            spacing 4
                            text "MEMORIZA" size 18 kerning 3 color "#FFE3A0"
                            use barra_progreso(mem_r, vivo.memoria, "#FFE3A0", 468)
                    else:
                        fixed:
                            xpos 36
                            ypos 340
                            xysize (468, 48)
                            use cinta_boton(("Mirar lista (-" + "{:g}".format(vivo.mirar_costo) + " s)"), Function(vivo.mirar), vivo.hermana_lista, 468, 48, 22)

            ## --- Estantes (cinta) ---
            if not en_sexto:

                for fi in range(len(vivo.estantes)):

                    $ flecha = ""
                    if vivo.deriva > 0.0:
                        if fi % 2 == 0:
                            $ flecha = "   >>>"
                        else:
                            $ flecha = "   <<<"

                    fixed:
                        xpos 650
                        ypos (N1_FILA_Y0 + fi * N1_FILA_H)
                        xysize (N1_VENTANA_W, 150)
                        clipping True

                        add Solid("#FFFFFF14")

                        text ("ESTANTE " + "ABCD"[fi] + flecha):
                            xpos 18
                            ypos 6
                            size 18
                            kerning 4
                            color "#FFFFFF88"

                        for c in vivo.cajas_fila(fi):
                            fixed:
                                xpos c[1]
                                ypos 34
                                xysize (N1_CAJA_W, N1_CAJA_H)
                                use mj_n1_caja(c[0], vivo.estado_caja(c[0]), Function(vivo.elegir, c[0]), trad_color, col_l)

            ## --- Sexto hueco ---
            else:

                text "Queda sitio para una cosa más en la cesta.":
                    xpos 1180
                    xanchor 0.5
                    ypos 250
                    size 36
                    color "#FFFFFF"
                    outlines [(4, "#1B1026CC", 0, 0)]

                vbox:
                    xpos 1180
                    xanchor 0.5
                    ypos 330
                    spacing 22

                    for op in MJ_N1_SEXTO:
                        use mj_n1_sexto_op(op[1], op[2], Function(vivo.elegir_sexto, op[0]), PETALO_COLOR["nino"], (vivo.sexto == op[0]))

            ## --- Nino chibi y su globo ---
            use mj_retrato("nino", vivo.expresion_star(), vivo.globo, vivo.anim_star(), 200, 900, 0.5)

            ## --- Cuenta atrás ---
            if vivo.fase == "cuenta":
                add Solid("#0B0712A0")
                text str(vivo.cuenta_n()):
                    xalign 0.5
                    yalign 0.42
                    font gui.name_text_font
                    size 220
                    color "#FFFFFF"
                    outlines [(8, "#1B1026CC", 0, 0)]
                text "PREPÁRATE":
                    xalign 0.5
                    yalign 0.66
                    font gui.name_text_font
                    size 36
                    kerning 6
                    color "#FFE3A0"


## Una opción del sexto hueco.
screen mj_n1_sexto_op(titulo, sub, accion, color, elegido):

    $ fondo = "#2B1B3F"
    $ borde = color
    if elegido:
        $ fondo = "#1E5A3A"
        $ borde = "#58D68D"
    $ hover = ui_mezclar(color, "#000000", 0.55)

    button:
        xysize (820, 110)
        action accion
        hover_sound audio.sfx_hover
        activate_sound audio.sfx_click
        background Fixed(
            Transform(Frame("ui/opcion_neutra.png", 40, 40, 40, 40), matrixcolor=TintMatrix(fondo)),
            Transform(Frame("ui/opcion_marco.png", 40, 40, 40, 40), matrixcolor=TintMatrix(borde)))
        hover_background Fixed(
            Transform(Frame("ui/opcion_neutra.png", 40, 40, 40, 40), matrixcolor=TintMatrix(hover)),
            Transform(Frame("ui/opcion_marco.png", 40, 40, 40, 40), matrixcolor=TintMatrix("#FFFFFF")))

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 4
            text titulo:
                xalign 0.5
                text_align 0.5
                size 32
                color "#FFFFFF"
            text sub:
                xalign 0.5
                text_align 0.5
                size 22
                color "#CFC6E0"


################################################################################
##  PRUEBA — jump mj_probar_n1
################################################################################

label mj_probar_n1:

    scene bg_negro
    $ e6_estado = {}
    $ e6_mj = {}
    $ persistent.e6_mj_ganado_nino = False

    menu:
        "Probar N1′ · ¿con el boost de Nino?"

        "Sin boost (difícil)":
            $ nino_rama_beat = "tibia"

        "Con boost (media)":
            $ nino_rama_beat = "calida"

    call mj_ejecutar("n1", "nino")

    $ n1_res = _return
    $ n1_info = e6_mj["nino"]
    $ narrator("Resultado: " + str(n1_res) + " · intentos " + str(n1_info["intentos"]) + " · fallos " + str(n1_info["fallos"]) + " · nivel " + n1_info["nivel"] + " · sexto: " + str(n1_info["datos"].get("sexto", "")))
    return
