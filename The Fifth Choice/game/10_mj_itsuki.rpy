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
        "titulo": _("Velocidad"),
        "inicios": [36, 54, 72, 90, 108],
        "pasos": [
            ("km/h", "m/h", "mult", 1000, _("1 km = 1.000 m")),
            ("m/h", "m/min", "div", 60, _("1 h = 60 min")),
            ("m/min", "m/s", "div", 60, _("1 min = 60 s")),
            ("m/s", "cm/s", "mult", 100, _("1 m = 100 cm")),
            ("cm/s", "mm/s", "mult", 10, _("1 cm = 10 mm")),
        ],
    },
    {
        "titulo": _("Caudal"),
        "inicios": [3600, 7200, 10800],
        "pasos": [
            ("L/h", "mL/h", "mult", 1000, _("1 L = 1.000 mL")),
            ("mL/h", "mL/min", "div", 60, _("1 h = 60 min")),
            ("mL/min", "mL/s", "div", 60, _("1 min = 60 s")),
            ("mL/s", "L/s", "div", 1000, _("1 L = 1.000 mL")),
            ("L/s", "dL/s", "mult", 10, _("1 L = 10 dL")),
        ],
    },
    {
        "titulo": _("Densidad"),
        "inicios": [2, 3, 5, 8],
        "pasos": [
            ("g/cm³", "kg/cm³", "div", 1000, _("1 kg = 1.000 g")),
            ("kg/cm³", "kg/m³", "mult", 1000000, _("1 m³ = 1.000.000 cm³")),
            ("kg/m³", "g/m³", "mult", 1000, _("1 kg = 1.000 g")),
            ("g/m³", "g/L", "div", 1000, _("1 m³ = 1.000 L")),
            ("g/L", "mg/L", "mult", 1000, _("1 g = 1.000 mg")),
        ],
    },
]

define IT1_PLAUS_UMBRAL = 1.9
define IT1_T_FIN = 1.6
define IT1_T_PERDER = 1.6
define IT1_T_MANO = 2.4
define IT1_T_PISTA = 4.0      ## segundos que la pista del profesor sale en el aviso del marco

## El cuaderno abierto: ocupa el área de juego del marco (x 440–1880, y 112–932).
define IT1_CUAD_X = MJ_AREA_X + 30                   ## 470
define IT1_CUAD_Y = MJ_AREA_Y + 16                   ## 128
define IT1_CUAD_W = MJ_AREA_W - 60                   ## 1380
define IT1_CUAD_H = 720                              ## hasta y 848
define IT1_PAG_W = IT1_CUAD_W // 2                   ## 690: cada página
define IT1_RENGLON = 44
define IT1_PIE_Y = IT1_CUAD_Y + IT1_CUAD_H + 20      ## 868: «Levantar la mano» (64 de alto → 932)
define IT1_OPCION = (290, 100)                       ## ficha de opción (rejilla 2×2)
define IT1_PAPEL = "#F6EEDC"
define IT1_PAPEL_CLARO = "#FBF6EA"
define IT1_MARCADOR = "#FFE3A0"

## Tinta del cuaderno (Klee One). Solo dentro del cuaderno y en la nota de la calculadora.
style it1_tinta is default:
    font gui.libreta_font
    size 26
    color "#2F2A44"

style it1_tinta_grande is it1_tinta:
    size 44

style it1_tinta_nota is it1_tinta:
    size 20
    color "#2F2A4499"

style it1_rotulo is it1_tinta:
    size 22
    kerning 3
    color "#B94A4A"

init python:

    import math
    from fractions import Fraction

    def it1_caja(fondo, borde):
        """Caja redondeada con el estilo de las opciones del juego."""
        return Fixed(
            Transform(Frame("ui/opcion_neutra.png", 40, 40, 40, 40), matrixcolor=TintMatrix(fondo)),
            Transform(Frame("ui/opcion_marco.png", 40, 40, 40, 40), matrixcolor=TintMatrix(borde)))

    def it1_ficha(fondo, borde):
        """Ficha de papel plana (opaca) con borde de 3 px: opciones del cuaderno."""
        return Fixed(
            Solid(borde),
            Transform(Solid(fondo), xpos=3, ypos=3, xsize=IT1_OPCION[0] - 6, ysize=IT1_OPCION[1] - 6))

    def it1_agrupar(n):
        """12345 -> '12.345' (en inglés '12,345')."""
        return ui_num("{:,}".format(int(n)))

    def it1_fmt(valor):
        """Fraction decimal exacta -> texto con los separadores del idioma ('0,002', '2.700' en español)."""
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
                return ui_num("{:,}".format(int(ent)) + "." + dec)
        return ui_num("{:.4f}".format(float(f)))

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

        def __init__(self, params, inicio, fallos_previos, intento=1):
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

            self.fase = "listo"
            if intento > 1:
                self.fase = "juego"
            self.t_fase = 0.0
            self.humor = ""
            self.aviso = ""
            self.aviso_t = 0.0
            self.avisado_tiempo = False
            self.globo = MJGlobo("itsuki")
            self.generar_opciones()
            if self.fase == "juego":
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

        def empezar(self):
            if self.fase != "listo":
                return None
            self.fase = "juego"
            self.t_fase = self.reloj.t
            self.globo.decir("inicio", True)
            return None

        def reglas(self):
            """Líneas de reglas para la pantalla de intro, según el nivel vigente."""
            lineas = []
            lineas.append(__("{} pasos · {} segundos.").format(self.n, int(self.total)))
            ent = self.p["intentos"]
            if ent is None:
                lineas.append(__("Puedes entregar las veces que quieras."))
            else:
                lineas.append(__("Entregas erróneas permitidas: {}.").format(int(ent)))
            usos = self.p["ayuda_usos"]
            if usos is None:
                lineas.append(__("«Levantar la mano»: ilimitada y gratis. El profesor te señala el paso que falla."))
            else:
                lineas.append(__("«Levantar la mano»: {} por intento, cuesta {} s. El profesor te señala el paso que falla.").format(int(usos), int(self.p["ayuda_costo"])))
            return lineas

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

        def aviso_marco(self):
            """(texto, tipo) para el aviso del marco. «No cuadra.» manda sobre la
            pista; la pista sale IT1_T_PISTA s (la fila sigue marcada en la hoja)."""
            if self.aviso_t > 0.0 and self.aviso != "":
                return (self.aviso, "mal")
            if self.msg_pista != "" and self.reloj.t - self.t_mano < IT1_T_PISTA:
                return (self.msg_pista, "info")
            return ("", "info")

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
                self.msg_pista = __("El profesor se acerca y señala el paso {}.").format(k + 1)
            else:
                self.msg_pista = _("El profesor mira el cuaderno: lo que llevas hasta aquí cuadra.")
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
                mj_sfx("acierto")
                self.humor = "feliz"
                self.globo.decir("final", True)
                self.cambiar("fin")
                return None
            mj_sfx("fallo")
            self.entregas_malas += 1
            self.aviso = _("No cuadra.")
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
            mj_sfx("fallo")
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

    mj_registrar("it1", "mj_it1", _("Cadena de conversiones"), True)


################################################################################
##  SCREEN
################################################################################

screen mj_it1(hermana, params, inicio, intento, fallos, nivel, titulo):

    modal True
    zorder 95

    default vivo = MJIt1(params, inicio, fallos, intento)

    timer 0.033 repeat True action Function(vivo.tick)

    key "K_RETURN" action Function(vivo.empezar)

    $ color = PETALO_COLOR["itsuki"]
    $ hechas = len(vivo.elegidas)
    $ t_rest = None
    $ t_tot = None
    if vivo.fase != "listo":
        $ t_rest = vivo.restante()
        $ t_tot = vivo.total
    $ av = vivo.aviso_marco()

    add "bg_aula_tarde" fit "cover"

    use mj_marco(hermana, titulo, intento, fallos, nivel, hechas, vivo.n, t_rest, t_tot, _("PASOS"), chibi=vivo.expresion_star(), globo=vivo.globo, anim=vivo.anim_star(), aviso=av[0], aviso_tipo=av[1]):

        if vivo.fase == "listo":
            use it1_intro(vivo, color)
        else:
            use it1_juego(vivo, color)


## --- Pantalla de explicación ----------------------
screen it1_intro(vivo, color):

    $ reglas = vivo.reglas()
    $ b = MJ_BOTON["primario"]

    fixed:
        xpos MJ_AREA_CX
        xanchor 0.5
        ypos (MJ_AREA_Y + 40)
        xysize (1160, 740)

        add it1_caja("#1B1026", color)

        vbox:
            xpos 50
            ypos 30
            xsize 1060
            spacing 26

            text _("CADENA DE CONVERSIONES"):
                style "mj_titulo"
                xalign 0.5

            text _("Itsuki convierte unidades paso a paso. En cada paso aparecen cuatro resultados: elige el correcto a partir del valor que llevas. Si te equivocas en uno, el error se arrastra a los siguientes (el número gris «arrastrado» es el que ella copia sin querer). Al terminar, pulsa «Entregar»; puedes tocar un paso ya hecho para rehacerlo."):
                style "mj_cuerpo"

            hbox:
                spacing 40

                vbox:
                    xsize 540
                    spacing 10

                    text _("REGLAS"):
                        style "mj_etiqueta"
                        color color

                    for r in reglas:
                        text ("· " + r):
                            style "mj_cuerpo"
                            color "#CFC6E0"

                ## Nota que rompe la cuarta pared (papel y Klee One: es la nota)
                fixed:
                    xysize (480, 250)
                    add Solid(IT1_PAPEL, xsize=480, ysize=250)
                    add Solid("#E8B04A", xsize=480, ysize=10)

                    vbox:
                        xpos 24
                        ypos 26
                        xsize 432
                        spacing 6

                        text _("NOTA FUERA DEL CUADERNO"):
                            style "it1_rotulo"
                            size 20

                        text _("Sí: aquí hay cuentas largas, de miles y millones. Ten una calculadora a mano (la del móvil o la del PC) y úsala sin culpa. Se evalúa tu método, no tu paciencia."):
                            style "it1_tinta"
                            size 24

        fixed:
            xalign 0.5
            ypos 600
            xysize (b[0], b[1])
            use cinta_boton(_("Empezar"), Function(vivo.empezar), "itsuki", b[0], b[1], b[2])


## --- El cuaderno abierto: papel, renglones, margen y lomo -----------------------
screen it1_cuaderno():

    fixed:
        xpos IT1_CUAD_X
        ypos IT1_CUAD_Y
        xysize (IT1_CUAD_W, IT1_CUAD_H)

        ## Papel opaco (opcion_neutra.png es translúcido y con degradado: se veía gris).
        add Solid("#0B071259", xsize=IT1_CUAD_W, ysize=IT1_CUAD_H) xpos 6 ypos 8
        add Solid("#D9CBB0", xsize=IT1_CUAD_W, ysize=IT1_CUAD_H) xpos 0 ypos 0
        add Solid(IT1_PAPEL, xsize=IT1_CUAD_W - 4, ysize=IT1_CUAD_H - 4) xpos 2 ypos 2

        ## Renglones en las dos páginas.
        for k in range(3, IT1_CUAD_H // IT1_RENGLON):
            add Solid("#8FB3D966", xsize=IT1_CUAD_W - 48, ysize=2) xpos 24 ypos (k * IT1_RENGLON)

        ## Margen rojo de la página izquierda.
        add Solid("#E07070AA", xsize=2, ysize=IT1_CUAD_H - 40) xpos 84 ypos 20

        ## Lomo: sombra y costura en el centro.
        add Solid("#2F2A441F", xsize=36, ysize=IT1_CUAD_H - 8) xpos (IT1_PAG_W - 18) ypos 4
        add Solid("#C9B99A", xsize=2, ysize=IT1_CUAD_H - 8) xpos (IT1_PAG_W - 1) ypos 4


## --- El juego: tu hoja (página izquierda) + el paso actual (página derecha) -----
screen it1_juego(vivo, color):

    $ hechas = len(vivo.elegidas)
    $ revision = (hechas >= vivo.n)
    $ unidad_final = vivo.pasos[vivo.n - 1][1]
    $ izq = IT1_CUAD_X + 110
    $ der = IT1_CUAD_X + IT1_PAG_W + 50
    $ centro_der = IT1_CUAD_X + IT1_PAG_W + IT1_PAG_W // 2

    use it1_cuaderno()

    ## --- Página izquierda: tu hoja ---
    text (__("CUADERNO DE CIENCIAS") + " · " + __(vivo.cadena["titulo"]).upper()):
        style "it1_rotulo"
        xpos izq
        ypos (IT1_CUAD_Y + 34)

    text __("Parte de {} {} y llega a {}.").format(it1_fmt(vivo.inicial), vivo.unidad_origen(), unidad_final):
        style "it1_tinta"
        xpos izq
        ypos (IT1_CUAD_Y + 70)
        xsize 540

    vbox:
        xpos izq
        ypos (IT1_CUAD_Y + 140)
        spacing 8

        if hechas == 0:
            text _("Tu hoja irá apareciendo aquí, paso a paso."):
                style "it1_tinta_nota"
        else:
            text _("Tu hoja · toca un paso para rehacerlo"):
                style "it1_tinta_nota"

        for k in range(hechas):
            use it1_fila(vivo, k, color)

    ## --- Página derecha: el número arrastrado, a lápiz ---
    vbox:
        xpos (IT1_CUAD_X + IT1_CUAD_W - 40)
        xanchor 1.0
        ypos (IT1_CUAD_Y + 24)
        text "arrastrado":
            style "it1_tinta_nota"
            xalign 1.0
        text it1_fmt(vivo.fantasma):
            style "it1_tinta"
            color "#2F2A4466"
            xalign 1.0

    if not revision:

        $ paso = vivo.pasos[hechas]

        text __("PASO {} DE {}").format(hechas + 1, vivo.n):
            style "it1_rotulo"
            xpos der
            ypos (IT1_CUAD_Y + 34)

        text (paso[0] + " → " + paso[1]):
            style "it1_tinta_grande"
            xpos der
            ypos (IT1_CUAD_Y + 66)

        hbox:
            xpos der
            ypos (IT1_CUAD_Y + 140)
            spacing 12
            text _("Equivalencia:"):
                style "it1_tinta_nota"
                yalign 0.5
            frame:
                yalign 0.5
                background Solid(IT1_MARCADOR + "CC")
                padding (12, 2, 12, 4)
                text paso[4] style "it1_tinta"

        text __("Llevas: {} {}").format(it1_fmt(vivo.valor_actual()), vivo.unidad_actual()):
            style "it1_tinta"
            xpos der
            ypos (IT1_CUAD_Y + 196)

        vbox:
            xpos der
            ypos (IT1_CUAD_Y + 268)
            spacing 20

            for fila in range(0, len(vivo.opciones), 2):
                hbox:
                    spacing 20
                    for i in range(fila, min(fila + 2, len(vivo.opciones))):
                        use it1_opcion(vivo, i, color)

    else:

        text _("REVISIÓN"):
            style "it1_rotulo"
            xpos der
            ypos (IT1_CUAD_Y + 34)

        text _("Tu resultado final"):
            style "it1_tinta"
            xpos der
            ypos (IT1_CUAD_Y + 80)

        text (it1_fmt(vivo.valor_actual()) + " " + unidad_final):
            style "it1_tinta_grande"
            xpos der
            ypos (IT1_CUAD_Y + 124)
            xsize 600

        text _("Si algún paso no te convence, tócalo en tu hoja (a la izquierda) y rehazlo desde ahí."):
            style "it1_tinta"
            xpos der
            ypos (IT1_CUAD_Y + 220)
            xsize 580

        if vivo.puede_entregar():
            $ b = MJ_BOTON["primario"]
            fixed:
                xpos centro_der
                xanchor 0.5
                ypos (IT1_CUAD_Y + 400)
                xysize (b[0], b[1])
                use cinta_boton(_("Entregar"), Function(vivo.entregar), "itsuki", b[0], b[1], b[2])

    ## --- Pie, fuera del cuaderno: levantar la mano + nota de la calculadora ---
    $ bs = MJ_BOTON["secundario"]
    fixed:
        xpos IT1_CUAD_X
        ypos IT1_PIE_Y
        xysize (bs[0], bs[1])
        if vivo.ayuda_disponible():
            use cinta_boton(__("Levantar la mano") + vivo.ayudas_restantes_texto(), Function(vivo.levantar), "itsuki", bs[0], bs[1], bs[2])
        else:
            use cinta_boton(_("Sin ayuda"), Function(vivo.levantar), "itsuki", bs[0], bs[1], bs[2], False)

    text _("Consejo fuera del cuaderno: la calculadora está permitida."):
        style "it1_tinta_nota"
        color IT1_MARCADOR
        outlines [(3, "#1B102699", 0, 0)]
        xpos (IT1_CUAD_X + bs[0] + 40)
        ypos (IT1_PIE_Y + 18)


## Una fila de «tu hoja»: paso ya hecho, escrito a mano. Se toca para rehacerlo.
## La que señala el profesor lleva fondo de marcador y «← mira aquí».
screen it1_fila(vivo, k, color):

    $ paso = vivo.pasos[k]
    $ senalada = (vivo.pista == k)
    $ raro = vivo.p["plausibilidad"] and vivo.raro(k)
    $ fondo = None
    if senalada:
        $ fondo = Solid(IT1_MARCADOR + "CC")

    button:
        xysize (550, 72)
        sensitive (vivo.fase == "juego")
        action Function(vivo.rehacer, k)
        hover_sound audio.sfx_hover
        activate_sound audio.sfx_click
        background fondo
        hover_background Solid(color + "33")
        insensitive_background fondo

        text (str(k + 1) + " · " + paso[0] + " → " + paso[1]):
            style "it1_tinta_nota"
            xpos 12
            ypos 4

        text (it1_fmt(vivo.elegidas[k]["valor"]) + " " + paso[1]):
            style "it1_tinta"
            xpos 12
            ypos 30

        if senalada:
            text _("← mira aquí"):
                style "it1_rotulo"
                xalign 0.97
                yalign 0.5
        elif raro:
            text _("(¿raro?)"):
                style "it1_tinta_nota"
                xalign 0.97
                yalign 0.5


## Una opción del paso actual: tarjetita de papel (rejilla de 2 columnas).
screen it1_opcion(vivo, i, color):

    $ op = vivo.opciones[i]
    $ paso = vivo.pasos[len(vivo.elegidas)]
    $ marcada = (vivo.p["trampa_marcada"] and op["tipo"] == "fantasma")

    button:
        xysize IT1_OPCION
        sensitive (vivo.fase == "juego")
        action Function(vivo.elegir, i)
        hover_sound audio.sfx_hover
        activate_sound audio.sfx_click
        background it1_ficha(IT1_PAPEL_CLARO, color)
        hover_background it1_ficha(color, color)
        insensitive_background it1_ficha(IT1_PAPEL_CLARO, color)

        text (it1_fmt(op["valor"]) + " " + paso[1]):
            style "it1_tinta"
            hover_color "#FFFFFF"
            xalign 0.5
            yalign 0.42
            xsize 262
            text_align 0.5

        if marcada:
            text _("(¡ojo!)"):
                style "it1_rotulo"
                size 18
                hover_color "#FFFFFF"
                xalign 0.5
                yalign 0.94


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

    call mj_ejecutar("it1", "itsuki") from _call_mj_ejecutar_7

    $ it1_res = _return
    $ it1_info = e6_mj["itsuki"]
    $ narrator("Resultado: " + str(it1_res) + " · intentos " + str(it1_info["intentos"]) + " · fallos " + str(it1_info["fallos"]) + " · nivel " + it1_info["nivel"] + " · frase " + it1_frase())
    return
