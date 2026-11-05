################################################################################
##  10_mj_itsuki.rpy — It1 · Cadena de conversiones (Evento 6, bloque de Itsuki)
##
##  Una cadena de conversiones de unidades paso a paso. En cada paso hay cuatro
##  resultados posibles calculados SOBRE EL VALOR QUE LLEVAS (si te equivocas en
##  un paso, el error se arrastra al siguiente: es lo que le pasa a Itsuki).
##  Trampas: el mismo número sin convertir, la conversión al revés, y el
##  «fantasma» (un número equivocado que se vuelve a colar a partir del paso 2;
##  sale en gris en el margen). Se pueden rehacer pasos tocando su fila.
##  Cuando todos los pasos están elegidos se pulsa «Entregar».
##
##  «Levantar la mano»: le pregunta al PROFESOR (no a MC). NO da la respuesta:
##  el profesor señala el primer paso que no cuadra («mira aquí»), o dice que
##  lo que llevas hasta ahora cuadra. Cuesta `ayuda_costo` segundos y se puede
##  usar `ayuda_usos` veces por intento (None = sin límite).
##
##  Parámetros: MJ_PARAMS["it1"] (10_minijuegos.rpy).
##    pasos          nº de pasos de la cadena (máx. 5)
##    tiempo         segundos
##    numeros_trampa trampas «de cálculo» por paso (fantasma sin convertir,
##                   conversión inversa); el resto de opciones son ruido ×10 ÷10
##    trampa_marcada True = la opción «mismo valor» lleva la etiqueta (¡ojo!)
##    intentos       ENTREGAS erróneas permitidas (None = sin límite)
##    ayuda_usos, ayuda_costo, plausibilidad (marca «raro» en los pasos que se
##    alejan ≥ 100× del valor correcto). puntos_control no se usa: es una sola
##    cadena y se reinicia entera.
##
##  RESULTADO PARA EL GUION: it1_frase() devuelve "A" (pidió ayuda o saltó el
##  minijuego) o "B" (resolvió sola desde el principio). También quedan en
##  e6_mj["itsuki"]["datos"]: ayuda_usada, ayudas, entregas_malas, fantasma.
##
##  Devuelve: "ganado" | "perdido" | "saltado".
################################################################################

## (unidad_origen, unidad_destino, "mult"|"div", factor, equivalencia)
define MJ_IT1_CADENAS = [
    {
        "titulo": "Velocidad",
        "inicios": [36, 54, 72, 90, 108],
        "pasos": [
            ("km/h", "m/h", "mult", 1000, "1 km = 1.000 m"),
            ("m/h", "m/min", "div", 60, "1 h = 60 min"),
            ("m/min", "m/s", "div", 60, "1 min = 60 s"),
            ("m/s", "cm/s", "mult", 100, "1 m = 100 cm"),
            ("cm/s", "mm/s", "mult", 10, "1 cm = 10 mm"),
        ],
    },
    {
        "titulo": "Caudal",
        "inicios": [3600, 7200, 10800],
        "pasos": [
            ("L/h", "mL/h", "mult", 1000, "1 L = 1.000 mL"),
            ("mL/h", "mL/min", "div", 60, "1 h = 60 min"),
            ("mL/min", "mL/s", "div", 60, "1 min = 60 s"),
            ("mL/s", "L/s", "div", 1000, "1 L = 1.000 mL"),
            ("L/s", "dL/s", "mult", 10, "1 L = 10 dL"),
        ],
    },
    {
        "titulo": "Densidad",
        "inicios": [2, 3, 5, 8],
        "pasos": [
            ("g/cm³", "kg/cm³", "div", 1000, "1 kg = 1.000 g"),
            ("kg/cm³", "kg/m³", "mult", 1000000, "1 m³ = 1.000.000 cm³"),
            ("kg/m³", "g/m³", "mult", 1000, "1 kg = 1.000 g"),
            ("g/m³", "g/L", "div", 1000, "1 m³ = 1.000 L"),
            ("g/L", "mg/L", "mult", 1000, "1 g = 1.000 mg"),
        ],
    },
]

define IT1_PLAUS_UMBRAL = 1.9
define IT1_T_FIN = 1.6
define IT1_T_PERDER = 1.6
define IT1_T_MANO = 2.4

init python:

    import math
    from fractions import Fraction

    def it1_agrupar(n):
        """12345 -> '12.345'."""
        s = "{:,}".format(int(n))
        return s.replace(",", ".")

    def it1_fmt(valor):
        """Fraction decimal exacta -> texto en español ('0,002', '2.700')."""
        f = Fraction(valor)
        for k in range(0, 10):
            m = f * (10 ** k)
            if m.denominator == 1:
                n = int(m)
                if k == 0:
                    return it1_agrupar(n)
                s = str(n)
                while len(s) < k + 1:
                    s = "0" + s
                ent = s[:len(s) - k]
                dec = s[len(s) - k:]
                return it1_agrupar(int(ent)) + "," + dec
        return ("{:.4f}".format(float(f))).replace(".", ",")

    def it1_aplicar(valor, paso):
        f = Fraction(paso[3])
        if paso[2] == "mult":
            return valor * f
        return valor / f

    def it1_frase():
        """'A' si Itsuki pidió ayuda (o se saltó el minijuego); 'B' si lo
        resolvió sola desde el principio. Léela justo después del minijuego."""
        r = store.e6_mj.get("itsuki")
        if r is None:
            return "A"
        if r["resultado"] == "saltado":
            return "A"
        if r["datos"].get("ayuda_usada", False):
            return "A"
        return "B"

    class MJIt1(object):
        """Estado vivo de la cadena. Lo crea la screen (default): no se guarda."""

        def __init__(self, params, inicio, fallos_previos):
            self.p = params
            self.reloj = MJReloj()
            self.fallos_prev = fallos_previos

            n = int(params["pasos"])
            if n < 1:
                n = 1
            if n > 5:
                n = 5
            self.n = n
            self.total = float(params["tiempo"])
            self.gastado = 0.0

            self.cadena = renpy.random.choice(MJ_IT1_CADENAS)
            self.inicial = Fraction(renpy.random.choice(self.cadena["inicios"]))
            self.pasos = self.cadena["pasos"][:n]
            self.verdad = []
            v = self.inicial
            for paso in self.pasos:
                v = it1_aplicar(v, paso)
                self.verdad.append(v)

            self.elegidas = []
            self.opciones = []
            self.pista = None
            self.msg_pista = ""
            self.ayudas = 0
            self.entregas_malas = 0
            self.t_mano = -100.0

            ## El fantasma: el número que se cuela. Si ya hubo un intento, es el
            ## número equivocado que quedó escrito; si no, el dato del enunciado.
            self.fantasma = self.inicial
            self.fantasma_fijado = False
            previo = None
            e = store.mj_estado
            if e:
                previo = e["datos"].get("fantasma")
            if previo is not None:
                try:
                    self.fantasma = Fraction(previo)
                    self.fantasma_fijado = True
                except Exception:
                    self.fantasma = self.inicial

            self.fase = "juego"
            self.t_fase = 0.0
            self.humor = ""
            self.aviso = ""
            self.aviso_t = 0.0
            self.avisado_tiempo = False
            self.globo = MJGlobo("itsuki")
            self.generar_opciones()
            self.globo.decir("inicio", True)

        # ---- utilidades ------------------------------------------------------
        def cambiar(self, fase):
            self.fase = fase
            self.t_fase = self.reloj.t

        def restante(self):
            r = self.total - self.gastado
            if r < 0.0:
                r = 0.0
            return r

        def valor_actual(self):
            if len(self.elegidas) == 0:
                return self.inicial
            return self.elegidas[len(self.elegidas) - 1]["valor"]

        def unidad_origen(self):
            return self.pasos[0][0]

        def unidad_actual(self):
            k = len(self.elegidas)
            if k == 0:
                return self.pasos[0][0]
            return self.pasos[k - 1][1]

        def ayuda_disponible(self):
            if self.fase != "juego":
                return False
            usos = self.p["ayuda_usos"]
            if usos is None:
                return True
            return self.ayudas < int(usos)

        def ayudas_restantes_texto(self):
            usos = self.p["ayuda_usos"]
            if usos is None:
                return ""
            return " (" + str(int(usos) - self.ayudas) + ")"

        def puede_entregar(self):
            return self.fase == "juego" and len(self.elegidas) >= self.n

        def raro(self, k):
            """¿La opción elegida en el paso k se aleja ≥ 100× del valor correcto?"""
            v = self.elegidas[k]["valor"]
            t = self.verdad[k]
            if v <= 0 or t <= 0:
                return False
            return abs(math.log10(float(v) / float(t))) >= IT1_PLAUS_UMBRAL

        def expresion_star(self):
            if self.fase == "fin":
                return "feliz"
            if self.fase == "perdiendo":
                return "triste"
            if self.reloj.t - self.t_mano < IT1_T_MANO:
                return "mano"
            return mj_chibi_expresion(len(self.elegidas), self.n, self.humor)

        def anim_star(self):
            if self.fase == "fin":
                return "salto"
            if self.fase == "perdiendo":
                return "tiembla"
            return "bob"

        # ---- opciones --------------------------------------------------------
        def generar_opciones(self):
            k = len(self.elegidas)
            if k >= self.n:
                self.opciones = []
                return
            paso = self.pasos[k]
            c = self.valor_actual()
            f = Fraction(paso[3])
            if paso[2] == "mult":
                correcta = c * f
                inversa = c / f
            else:
                correcta = c / f
                inversa = c * f

            ops = [{"valor": correcta, "tipo": "correcta"}]
            usados = [correcta]

            trampas = int(self.p["numeros_trampa"])
            candidatas = [
                {"valor": c, "tipo": "fantasma"},
                {"valor": inversa, "tipo": "inversa"},
            ]
            puestas = 0
            for cand in candidatas:
                if puestas >= trampas:
                    break
                if cand["valor"] not in usados:
                    ops.append(cand)
                    usados.append(cand["valor"])
                    puestas += 1

            ## El fantasma vuelve a colarse a partir del segundo paso.
            if k >= 1 and len(ops) < 4 and self.fantasma not in usados:
                ops.append({"valor": self.fantasma, "tipo": "fantasma"})
                usados.append(self.fantasma)

            ruido = [correcta * 10, correcta / 10, correcta * 100, correcta / 100]
            for r in ruido:
                if len(ops) >= 4:
                    break
                if r not in usados:
                    ops.append({"valor": r, "tipo": "ruido"})
                    usados.append(r)

            renpy.random.shuffle(ops)
            self.opciones = ops

        # ---- acciones --------------------------------------------------------
        def elegir(self, idx):
            if self.fase != "juego":
                return None
            if len(self.elegidas) >= self.n:
                return None
            if idx < 0 or idx >= len(self.opciones):
                return None
            op = self.opciones[idx]
            self.elegidas.append(op)
            if op["tipo"] != "correcta" and not self.fantasma_fijado:
                self.fantasma = op["valor"]
                self.fantasma_fijado = True
            self.generar_opciones()
            self.globo.decir("paso")
            return None

        def rehacer(self, k):
            if self.fase != "juego":
                return None
            if k < 0 or k >= len(self.elegidas):
                return None
            del self.elegidas[k:]
            if self.pista is not None and self.pista >= k:
                self.pista = None
                self.msg_pista = ""
            self.generar_opciones()
            return None

        def primer_error(self):
            for k in range(len(self.elegidas)):
                if self.elegidas[k]["tipo"] != "correcta":
                    return k
            return -1

        def levantar(self):
            if not self.ayuda_disponible():
                return None
            self.ayudas += 1
            self.gastado += float(self.p["ayuda_costo"])
            self.t_mano = self.reloj.t
            k = self.primer_error()
            self.pista = k
            if k >= 0:
                self.msg_pista = "El profesor se acerca y señala el paso " + str(k + 1) + "."
            else:
                self.msg_pista = "El profesor mira el cuaderno: lo que llevas hasta aquí cuadra."
            self.globo.decir("ayuda", True)
            if self.restante() <= 0.0:
                return self.perder()
            return None

        def entregar(self):
            if not self.puede_entregar():
                return None
            todo_bien = True
            for e in self.elegidas:
                if e["tipo"] != "correcta":
                    todo_bien = False
            if todo_bien:
                self.humor = "feliz"
                self.globo.decir("final", True)
                self.cambiar("fin")
                return None
            self.entregas_malas += 1
            self.aviso = "No cuadra."
            self.aviso_t = 1.1
            intentos = self.p["intentos"]
            if intentos is not None and self.entregas_malas >= int(intentos):
                return self.perder()
            if self.ayudas > 0:
                self.globo.decir("tras_ayuda", True)
            else:
                self.globo.decir("fallo", True)
            return None

        def perder(self):
            if MJ_FALLO_EN_GLOBO:
                self.globo.poner(mj_texto_fallo("itsuki", self.fallos_prev), 1.5)
            else:
                self.globo.decir("fallo", True)
            self.cambiar("perdiendo")
            return None

        def resultado(self, que):
            previo = False
            e = store.mj_estado
            if e:
                previo = bool(e["datos"].get("ayuda_usada", False))
            usada = previo or self.ayudas > 0
            return {
                "resultado": que,
                "progreso": len(self.elegidas),
                "datos": {
                    "ayuda_usada": usada,
                    "ayudas": self.ayudas,
                    "entregas_malas": self.entregas_malas,
                    "fantasma": str(self.fantasma),
                },
            }

        def tick(self):
            dt = self.reloj.avanzar()
            self.globo.avanzar(dt)
            if self.aviso_t > 0.0:
                self.aviso_t -= dt
            f = self.fase

            if f == "juego":
                self.gastado += dt
                if self.restante() <= 0.0:
                    return self.perder()
                if self.restante() < 12.0 and not self.avisado_tiempo:
                    self.avisado_tiempo = True
                    self.globo.decir("tiempo", True)
                return None

            if f == "perdiendo":
                if self.reloj.t - self.t_fase >= IT1_T_PERDER:
                    return self.resultado("perdido")
                return None

            if f == "fin":
                if self.reloj.t - self.t_fase >= IT1_T_FIN:
                    return self.resultado("ganado")
            return None

    mj_registrar("it1", "mj_it1", "Cadena de conversiones", True)


################################################################################
##  SCREEN
################################################################################

screen mj_it1(hermana, params, inicio, intento, fallos, nivel, titulo):

    modal True
    zorder 95

    default vivo = MJIt1(params, inicio, fallos)

    timer 0.033 repeat True action Function(vivo.tick)

    key "K_RETURN" action NullAction()

    $ color = PETALO_COLOR["itsuki"]
    $ tinta = ui_mezclar(color, "#000000", 0.75)
    $ hechas = len(vivo.elegidas)
    $ unidad_final = vivo.pasos[vivo.n - 1][1]

    add "bg_aula_tarde" fit "cover"

    use mj_marco(hermana, titulo, intento, fallos, nivel, hechas, vivo.n, vivo.restante(), vivo.total, "PASOS"):

        text ("CUADERNO DE CIENCIAS · " + vivo.cadena["titulo"].upper()):
            xpos 320
            ypos 150
            font gui.name_text_font
            size 34
            kerning 3
            color color
            outlines [(4, "#1B1026CC", 0, 0)]

        text ("Parte de " + it1_fmt(vivo.inicial) + " " + vivo.unidad_origen() + " y llega a " + unidad_final + ".   Cada paso parte de lo que llevas."):
            xpos 320
            ypos 205
            size 26
            color "#FFFFFF"
            outlines [(3, "#1B102699", 0, 0)]

        ## --- El fantasma, en el margen ---
        vbox:
            xpos 60
            ypos 300
            spacing 2
            text "ARRASTRADO":
                size 16
                kerning 3
                color "#FFFFFF55"
            text it1_fmt(vivo.fantasma):
                size 34
                color "#FFFFFF44"

        ## --- Los pasos ---
        for k in range(vivo.n):

            $ paso = vivo.pasos[k]
            $ hecha = k < hechas
            $ actual = (k == hechas)
            $ borde = color
            $ fondo = "#2B1B3F"
            if vivo.pista == k:
                $ borde = "#FFE3A0"
            elif not hecha and not actual:
                $ fondo = "#1B1026"
            $ valor_txt = "—"
            if hecha:
                $ valor_txt = it1_fmt(vivo.elegidas[k]["valor"]) + " " + paso[1]
            elif actual:
                $ valor_txt = "¿?"

            button:
                xpos 320
                ypos (300 + k * 108)
                xysize (700, 96)
                sensitive (hecha and vivo.fase == "juego")
                action Function(vivo.rehacer, k)
                hover_sound audio.sfx_hover
                background Fixed(
                    Transform(Frame("ui/opcion_neutra.png", 40, 40, 40, 40), matrixcolor=TintMatrix(fondo)),
                    Transform(Frame("ui/opcion_marco.png", 40, 40, 40, 40), matrixcolor=TintMatrix(borde)))
                hover_background Fixed(
                    Transform(Frame("ui/opcion_neutra.png", 40, 40, 40, 40), matrixcolor=TintMatrix(ui_mezclar(color, "#000000", 0.55))),
                    Transform(Frame("ui/opcion_marco.png", 40, 40, 40, 40), matrixcolor=TintMatrix("#FFFFFF")))

                text (str(k + 1) + " · " + paso[0] + " → " + paso[1]):
                    xpos 28
                    yalign 0.5
                    size 26
                    color "#CFC6E0"

                text valor_txt:
                    xalign 0.97
                    yalign 0.5
                    size 34
                    color "#FFFFFF"

                if hecha and vivo.p["plausibilidad"] and vivo.raro(k):
                    text "(¿raro?)":
                        xpos 330
                        yalign 0.5
                        size 22
                        color "#FFE3A0"

        ## --- Opciones del paso actual ---
        if hechas < vivo.n:

            $ paso_a = vivo.pasos[hechas]

            text ("Paso " + str(hechas + 1) + ": " + paso_a[0] + " → " + paso_a[1]):
                xpos 1090
                ypos 300
                size 30
                color "#FFFFFF"
                outlines [(3, "#1B102699", 0, 0)]

            text paso_a[4]:
                xpos 1090
                ypos 345
                size 28
                color "#FFE3A0"
                outlines [(3, "#1B102699", 0, 0)]

            vbox:
                xpos 1090
                ypos 400
                spacing 16

                for i in range(len(vivo.opciones)):

                    $ op = vivo.opciones[i]
                    $ etiqueta = ""
                    if vivo.p["trampa_marcada"] and op["tipo"] == "fantasma":
                        $ etiqueta = "  (¡ojo!)"

                    button:
                        xysize (660, 80)
                        action Function(vivo.elegir, i)
                        hover_sound audio.sfx_hover
                        activate_sound audio.sfx_click
                        background Fixed(
                            Transform(Frame("ui/opcion_neutra.png", 40, 40, 40, 40), matrixcolor=TintMatrix("#2B1B3F")),
                            Transform(Frame("ui/opcion_marco.png", 40, 40, 40, 40), matrixcolor=TintMatrix(color)))
                        hover_background Fixed(
                            Transform(Frame("ui/opcion_neutra.png", 40, 40, 40, 40), matrixcolor=TintMatrix(ui_mezclar(color, "#000000", 0.55))),
                            Transform(Frame("ui/opcion_marco.png", 40, 40, 40, 40), matrixcolor=TintMatrix("#FFFFFF")))

                        text (it1_fmt(op["valor"]) + " " + paso_a[1] + etiqueta):
                            xalign 0.5
                            yalign 0.5
                            size 34
                            color "#FFFFFF"

        else:

            text "Todos los pasos están hechos. Revisa tus filas o entrega.":
                xpos 1090
                ypos 400
                xsize 660
                size 30
                color "#FFFFFF"
                outlines [(3, "#1B102699", 0, 0)]

        ## --- Botones ---
        fixed:
            xpos 1090
            ypos 780
            xysize (320, 70)
            if vivo.ayuda_disponible():
                use cinta_boton("Levantar la mano" + vivo.ayudas_restantes_texto(), Function(vivo.levantar), "itsuki", 320, 70, 24)
            else:
                add Solid("#FFFFFF14", xsize=320, ysize=70)
                text "Sin ayuda":
                    xalign 0.5
                    yalign 0.5
                    size 24
                    color "#FFFFFF66"

        fixed:
            xpos 1440
            ypos 780
            xysize (310, 70)
            if vivo.puede_entregar():
                use cinta_boton("Entregar", Function(vivo.entregar), "itsuki", 310, 70, 28)
            else:
                add Solid("#FFFFFF14", xsize=310, ysize=70)
                text "Entregar":
                    xalign 0.5
                    yalign 0.5
                    size 28
                    color "#FFFFFF66"

        if vivo.msg_pista != "":
            text vivo.msg_pista:
                xpos 1090
                ypos 862
                xsize 700
                size 24
                color "#FFE3A0"
                outlines [(3, "#1B102699", 0, 0)]

        if vivo.aviso_t > 0.0:
            text vivo.aviso:
                xpos 1090
                xanchor 0
                ypos 735
                font gui.name_text_font
                size 36
                color "#FFC4C4"
                outlines [(4, "#1B1026CC", 0, 0)]

        ## --- Itsuki chibi y su globo ---
        use mj_retrato("itsuki", vivo.expresion_star(), vivo.globo, vivo.anim_star(), 170, 890, 0.5)


################################################################################
##  PRUEBA — jump mj_probar_it1
################################################################################

label mj_probar_it1:

    scene bg_negro
    $ e6_estado = {}
    $ e6_mj = {}
    $ persistent.e6_mj_ganado_itsuki = False

    menu:
        "Probar It1 · ¿con el boost de Nino?"

        "Sin boost (difícil)":
            $ nino_rama_beat = "tibia"

        "Con boost (media)":
            $ nino_rama_beat = "calida"

    call mj_ejecutar("it1", "itsuki")

    $ it1_res = _return
    $ it1_info = e6_mj["itsuki"]
    $ narrator("Resultado: " + str(it1_res) + " · intentos " + str(it1_info["intentos"]) + " · fallos " + str(it1_info["fallos"]) + " · nivel " + it1_info["nivel"] + " · frase " + it1_frase())
    return
