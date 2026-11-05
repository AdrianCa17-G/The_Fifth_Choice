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
##      "celebrar"  comprar lo de la tarta antes de saber el resultado
##      "consolar"  chocolate «por si sale mal»
##      "vacio"     dejar el hueco vacío
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
    ("ichika",  ["honey", "chamomile tea", "instant oats"]),
    ("yotsuba", ["energy bars", "peanut butter", "whole milk"]),
    ("miku",    ["matcha powder", "sea salt", "sesame seeds"]),
    ("itsuki",  ["bread flour", "unsalted butter", "maple syrup"]),
    ("nino",    ["vanilla extract", "confectioners' sugar", "baking powder"]),
]

## (clave, título, subtítulo)
define MJ_N1_SEXTO = [
    ("celebrar", "Lo de una tarta de celebración", "Comprarlo antes de saber el resultado."),
    ("consolar", "Chocolate para consolar", "Por si sale mal."),
    ("vacio",    "Dejar el hueco vacío", "Ya se verá."),
]

init python:

    MJ_N1_GRUPO_DE = {}
    for _g in MJ_N1_GRUPOS:
        for _k in _g:
            MJ_N1_GRUPO_DE[_k] = _g

    class MJN1(object):
        """Estado vivo de las compras. Lo crea la screen (default): no se guarda."""

        def __init__(self, params, inicio, fallos_previos):
            self.p = params
            self.reloj = MJReloj()
            self.fallos_prev = fallos_previos
            if inicio > 4:
                inicio = 4
            self.lista = inicio
            base = float(params["tiempo_total"])
            tiempo = base * ((5 - inicio) / 5.0)
            if tiempo < base * 0.4:
                tiempo = base * 0.4
            self.total = tiempo
            self.gastado = 0.0
            self.penal = 0.0
            self.errores = 0
            self.sexto = ""
            self.fase = "compras"
            self.t_fase = 0.0
            self.globo = MJGlobo("nino")
            self.humor = ""
            self.humor_t = 0.0
            self.aviso = ""
            self.aviso_t = 0.0
            self.avisado_tiempo = False
            self.idx = 0
            self.hermana_lista = "ichika"
            self.claves = []
            self.encontrados = []
            self.malos = []
            self.estantes = []
            self.g0 = 0.0
            self.entrar_lista(inicio)
            self.globo.decir("inicio", True)

        def cambiar(self, fase):
            self.fase = fase
            self.t_fase = self.reloj.t

        def restante(self):
            r = self.total - self.gastado - self.penal
            if r < 0.0:
                r = 0.0
            return r

        def entrar_lista(self, idx):
            self.idx = idx
            datos = MJ_N1_LISTAS[idx]
            self.hermana_lista = datos[0]
            self.claves = datos[1]
            self.encontrados = []
            self.malos = []
            d = int(self.p["distractores"])
            if d < 1:
                d = 1
            if d > 3:
                d = 3
            estantes = []
            for k in self.claves:
                grupo = MJ_N1_GRUPO_DE[k]
                otros = []
                for x in grupo:
                    if x != k:
                        otros.append(x)
                renpy.random.shuffle(otros)
                cajas = [k]
                for x in otros[:d]:
                    cajas.append(x)
                renpy.random.shuffle(cajas)
                estantes.append(cajas)
            renpy.random.shuffle(estantes)
            self.estantes = estantes
            self.g0 = self.gastado
            self.cambiar("compras")

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

        def estado_caja(self, clave):
            if clave in self.encontrados:
                return "ok"
            if clave in self.malos:
                return "mal"
            return "libre"

        def poner_humor(self, que, seg):
            self.humor = que
            self.humor_t = seg

        # ---- resultado -------------------------------------------------------
        def resultado(self, que):
            return {
                "resultado": que,
                "progreso": self.lista,
                "datos": {"sexto": self.sexto, "errores": self.errores, "sobra": int(self.restante())},
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
            self.penal += float(self.p["penalizacion"])
            self.globo.decir("fallo", True)
            self.poner_humor("triste", 0.9)
            self.aviso = "Esa no."
            self.aviso_t = 0.9
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
            if self.aviso_t > 0.0:
                self.aviso_t -= dt
            if self.humor_t > 0.0:
                self.humor_t -= dt
                if self.humor_t <= 0.0 and self.fase != "perdiendo":
                    self.humor = ""
            f = self.fase

            if f == "compras":
                self.gastado += dt
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
screen mj_n1_caja(clave, estado, accion, trad_color, color):

    $ en = clave
    $ es_txt = MJ_N1_ITEMS[clave]
    $ fondo = "#2B1B3F"
    $ borde = color
    $ hover = ui_mezclar(color, "#000000", 0.55)
    if estado == "ok":
        $ fondo = "#1E5A3A"
        $ borde = "#58D68D"
    elif estado == "mal":
        $ fondo = "#4A2020"
        $ borde = "#7A4040"

    button:
        xysize (280, 120)
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
            spacing 4
            text en:
                xalign 0.5
                text_align 0.5
                size 27
                color "#FFFFFF"
            text es_txt:
                xalign 0.5
                text_align 0.5
                size 20
                color trad_color


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


screen mj_n1(hermana, params, inicio, intento, fallos, nivel, titulo):

    modal True
    zorder 95

    default vivo = MJN1(params, inicio, fallos)

    timer 0.033 repeat True action Function(vivo.tick)

    key "K_RETURN" action NullAction()

    $ col_l = PETALO_COLOR[vivo.hermana_lista]
    $ tono_l = TARJETA_TONO[vivo.hermana_lista]
    $ ta = vivo.trad_alpha()
    $ trad_color = "#CFC6E0" + "{:02x}".format(int(255 * ta))
    $ en_sexto = (vivo.fase == "sexto" or vivo.fase == "fin")

    add "bg_centro_comercial" fit "cover"

    use mj_marco(hermana, titulo, intento, fallos, nivel, vivo.lista, 5, vivo.restante(), vivo.total, "LISTAS"):

        ## --- La lista de la hermana ---
        fixed:
            xpos 60
            ypos 170
            xysize (540, 390)

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
                ypos 80
                spacing 12

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
                            text k size 29 color "#FFFFFF"
                            text MJ_N1_ITEMS[k] size 19 color trad_color

                hbox:
                    spacing 16
                    if vivo.sexto != "":
                        add Solid("#58D68D", xsize=24, ysize=24) yalign 0.5
                    else:
                        add Solid("#FFFFFF22", xsize=24, ysize=24) yalign 0.5
                    text "6.º hueco de la cesta" size 24 color "#FFE3A0"

        ## --- Aviso de error ---
        if vivo.aviso_t > 0.0:
            text vivo.aviso:
                xalign 0.5
                ypos 130
                font gui.name_text_font
                size 36
                color "#FFC4C4"
                outlines [(4, "#1B1026CC", 0, 0)]

        ## --- Estantes ---
        if not en_sexto:

            for fi in range(len(vivo.estantes)):

                $ cajas = vivo.estantes[fi]

                add Solid("#FFFFFF14", xsize=1210, ysize=180) xpos 650 ypos (190 + fi * 205)
                text ("ESTANTE " + "ABC"[fi]):
                    xpos 668
                    ypos (196 + fi * 205)
                    size 18
                    kerning 4
                    color "#FFFFFF88"

                hbox:
                    xpos 668
                    ypos (232 + fi * 205)
                    spacing 16

                    for clave in cajas:
                        use mj_n1_caja(clave, vivo.estado_caja(clave), Function(vivo.elegir, clave), trad_color, col_l)

        ## --- Sexto hueco ---
        else:

            text "Queda sitio para una cosa más en la cesta.":
                xpos 960
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
