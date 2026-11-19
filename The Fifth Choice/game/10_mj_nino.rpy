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

## Distribución «lista encima» (docs/MINIJUEGOS/MJ_NINO.md): franja de la lista
## arriba del área y estantes a todo lo ancho debajo.
define N1_LISTA_H = 212          ## franja: y 112–324
define N1_IZQ_X = 472            ## bloque izquierdo de la franja (LISTA n/5, nombre, racha)
define N1_CELDA_X = 780          ## celdas de producto: desde x 780, 260 cada una
define N1_CELDA_W = 260
define N1_ESTANTES_Y = 330       ## los estantes se centran en y 330–932
define N1_VENTANA_W = 1440       ## = MJ_AREA_W
define N1_CAJA_W = 272
define N1_CAJA_H = 112
define N1_FILA_ALTO = 144        ## etiqueta (y+0) + cajas (y+32)
define N1_FILA_H = 150           ## paso entre filas
define N1_CUENTA_S = 0.7
define N1_RACHA_N = 3
define N1_AVISO_S = 1.2

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

    ## Un fondo por par de colores, siempre el mismo objeto: así la screen
    ## reutiliza las cajas al reevaluarse en vez de volver a maquetarlas.
    N1_FONDOS = {}

    def n1_fondo(relleno, borde):
        clave = (relleno, borde)
        if clave not in N1_FONDOS:
            N1_FONDOS[clave] = Fixed(
                Transform(Frame("ui/opcion_neutra.png", 40, 40, 40, 40), matrixcolor=TintMatrix(relleno)),
                Transform(Frame("ui/opcion_marco.png", 40, 40, 40, 40), matrixcolor=TintMatrix(borde)))
        return N1_FONDOS[clave]

    def n1_fila_y0(n_filas):
        """y de la primera fila: el bloque de estantes, centrado bajo la franja."""
        alto = (n_filas - 1) * N1_FILA_H + N1_FILA_ALTO
        return N1_ESTANTES_Y + (MJ_AREA_Y + MJ_AREA_H - N1_ESTANTES_Y - alto) // 2

    def n1_seg(x):
        """1.5 -> '1,5'."""
        return "{:g}".format(x).replace(".", ",")

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
            partes.append("La lista se esconde a los " + n1_seg(p["memoria"]) + " s: memorízala o mírala de nuevo (−" + n1_seg(p["mirar_costo"]) + " s).")
        reglas.append(("BUSCA RÁPIDO", " ".join(partes)))

        reglas.append(("NO TE EQUIVOQUES", "Cada error resta " + n1_seg(p["penalizacion"]) + " s y bloquea esa caja. Cada " + str(N1_RACHA_N) + " aciertos seguidos suman +" + n1_seg(p["racha_bonus"]) + " s."))
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
            self.errores = 0
            self.racha = 0
            self.mejor_racha = 0
            self.mirones = 0
            self.sexto = ""
            self.mirada_t = 0.0
            self.aviso = ""
            self.aviso_tipo = "info"
            self.aviso_t = 0.0
            self.flash_t = 0.0
            self.humor = ""
            self.humor_t = 0.0
            self.avisado_tiempo = False
            self.globo = MJGlobo("nino")
            self.firma_prev = None

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

        def avisar(self, texto, tipo):
            """Píldora del marco durante N1_AVISO_S. tipo: bien | mal | info."""
            self.aviso = texto
            self.aviso_tipo = tipo
            self.aviso_t = N1_AVISO_S

        def aviso_vivo(self):
            """El aviso que se ve ahora. En el sexto hueco, ninguno."""
            if self.aviso_t <= 0.0 or self.fase == "sexto" or self.fase == "fin":
                return ""
            return self.aviso

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

        def fila_sentido(self, fi):
            if fi % 2 == 1:
                return -1
            return 1

        def fila_base(self, fi):
            """[(clave, x), ...] de la fila fi en reposo. Con deriva, cada caja
            lleva una copia a un periodo de distancia (detrás, según el sentido):
            así la cinta (n1_cinta) da la vuelta sin corte."""
            cajas = self.estantes[fi]
            n = len(cajas)
            periodo = float(N1_VENTANA_W)
            paso = periodo / n
            centro = (paso - N1_CAJA_W) / 2.0
            res = []
            for k in range(n):
                x = k * paso + centro
                res.append((cajas[k], int(x)))
                if self.deriva > 0.0:
                    res.append((cajas[k], int(x - self.fila_sentido(fi) * periodo)))
            return res

        def fila_mov(self, fi):
            """(dx, dur) del bucle de la fila fi: recorre un periodo entero a
            deriva * (1 + 0.15 * fi) px/s. Sin deriva, (0, 0.0)."""
            if self.deriva <= 0.0:
                return (0, 0.0)
            vel = self.deriva * (1.0 + 0.15 * fi)
            return (self.fila_sentido(fi) * N1_VENTANA_W, N1_VENTANA_W / vel)

        def estado_caja(self, clave):
            if clave in self.encontrados:
                return "ok"
            if clave in self.malos:
                return "mal"
            return "libre"

        def trad_visible(self):
            """La traducción aparece sola `retardo_traduccion` s después de abrir
            la lista (el fundido de 0,4 s lo hace n1_trad)."""
            ret = float(self.p["retardo_traduccion"])
            if ret <= 0.0:
                return True
            return (self.gastado - self.g0) > ret

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
            self.avisar("Miras la lista · −" + n1_seg(self.mirar_costo) + " s", "info")
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
            mj_sfx("fallo")
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
                mj_sfx("acierto")
                self.encontrados.append(clave)
                self.racha += 1
                if self.racha > self.mejor_racha:
                    self.mejor_racha = self.racha
                if self.racha % N1_RACHA_N == 0 and self.bonus > 0.0:
                    self.total += self.bonus
                    self.avisar("Racha ×" + str(self.racha) + " · +" + n1_seg(self.bonus) + " s", "bien")
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

            mj_sfx("fallo")
            self.malos.append(clave)
            self.errores += 1
            self.racha = 0
            pen = float(self.p["penalizacion"])
            self.penal += pen
            self.avisar("Esa no es · −" + n1_seg(pen) + " s", "mal")
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

        def firma(self):
            """Todo lo que la screen muestra y cambia con el tiempo. No están ni
            la cinta (n1_cinta), ni la barra de memoria (n1_vaciar), ni el
            fundido de la traducción (n1_trad): los anima el motor. El reloj
            va en segundos enteros, como lo dibuja el marco."""
            return (self.fase, self.cuenta_n(), int(self.restante() + 0.999), self.racha,
                    self.lista_visible(), self.mirada_t > 0.0, self.trad_visible(),
                    self.aviso_vivo(), self.flash_t > 0.0, self.humor,
                    self.globo.texto, self.globo.visible(), self.tension(),
                    len(self.encontrados), len(self.malos), self.idx, self.sexto)

        def tick(self):
            """Lo llama el timer sin reiniciar la interacción
            (_update_screens=False): solo se reinicia si cambia la firma."""
            rv = self._tick()
            f = self.firma()
            if f != self.firma_prev:
                self.firma_prev = f
                renpy.restart_interaction()
            return rv

        def _tick(self):
            dt = self.reloj.avanzar()
            self.globo.avanzar(dt)
            if self.aviso_t > 0.0:
                self.aviso_t -= dt
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
##  Distribución «lista encima» dentro del área del marco (x 440–1880,
##  y 112–932): franja de la lista arriba y estantes a todo lo ancho debajo.
##  Medidas y decisiones: docs/MINIJUEGOS/MJ_NINO.md
################################################################################

transform n1_entrada:
    alpha 0.0
    ease 0.3 alpha 1.0

## La cinta de un estante: recorre un periodo (dx px) en dur s, en bucle.
## Lo anima el motor en cada fotograma, sin reevaluar la screen.
transform n1_cinta(dx, dur):
    xoffset 0
    linear dur xoffset dx
    repeat

## Latido rojo de urgencia (mismo periodo que el antiguo sin(t * 6)).
transform n1_latido:
    alpha 0.05
    ease 0.52 alpha 0.15
    ease 0.52 alpha 0.05
    repeat

## Destello rojo de un error.
transform n1_destello:
    alpha 0.30
    linear 0.35 alpha 0.0

## La traducción, antes de asomar (ocupa su sitio para que nada salte).
transform n1_oculto:
    alpha 0.0

## La traducción asoma: fundido de 0,4 s.
transform n1_trad:
    alpha 0.0
    linear 0.4 alpha 1.0

## Barra de memoria que se vacía sola: de `ancho` a 0 en `dur` s. Si la screen
## se reevalúa a mitad, vuelve a empezar desde el ancho de ese momento.
transform n1_vaciar(ancho, dur):
    xsize ancho
    linear dur xsize 0


init python:

    def n1_trad_at(vivo):
        """Transform de las traducciones: sin retardo, ninguno."""
        if float(vivo.p["retardo_traduccion"]) <= 0.0:
            return []
        if vivo.trad_visible():
            return [n1_trad]
        return [n1_oculto]


## Una pastilla de información (tiempo, productos…).
screen mj_n1_chip(texto, color):

    frame:
        padding (22, 10, 22, 10)
        background n1_fondo("#1B1026", color)

        text texto:
            style "mj_etiqueta"
            color "#F3EEFA"
            substitute False


## Pantalla de explicación (primer intento), centrada en el área.
screen mj_n1_intro(vivo, nivel):

    $ color = PETALO_COLOR["nino"]
    $ tinta = ui_mezclar(color, "#000000", 0.75)
    $ reglas = n1_reglas(vivo.p)
    $ ritmo = n1_ritmo(nivel)
    $ b = MJ_BOTON["primario"]

    frame:
        xpos MJ_AREA_CX
        xanchor 0.5
        ypos (MJ_AREA_Y + MJ_AREA_H // 2)
        yanchor 0.5
        xsize 1180
        ymaximum MJ_AREA_H
        padding (60, 34, 60, 30)
        background n1_fondo("#1B1026", color)
        at n1_entrada

        vbox:
            xsize 1060
            spacing 16

            text "COMPRAS PARA SEIS":
                style "mj_titulo"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 16

                use mj_n1_chip(("TIEMPO  " + n1_seg(vivo.total) + " s"), color)
                use mj_n1_chip(("5 LISTAS · " + str(vivo.n_prod) + " PRODUCTOS"), color)

                frame:
                    padding (22, 10, 22, 10)
                    background n1_fondo("#1B1026", color)

                    hbox:
                        spacing 8
                        text "RITMO" style "mj_etiqueta" color "#F3EEFA" yalign 0.5
                        for i in range(3):
                            $ alfa_f = 0.22
                            if i < ritmo:
                                $ alfa_f = 1.0
                            add Transform("ui/flor.png", matrixcolor=TintMatrix(color), zoom=0.5, alpha=alfa_f) yalign 0.5

            null height 4

            for i, r in enumerate(reglas):
                hbox:
                    spacing 24

                    fixed:
                        xysize (64, 64)
                        add Transform("ui/flor.png", matrixcolor=TintMatrix(color), zoom=1.15) align (0.5, 0.5)
                        text str(i + 1):
                            style "mj_cifra"
                            outlines []
                            align (0.5, 0.5)
                            color tinta

                    vbox:
                        spacing 2
                        xsize 960
                        text r[0] style "mj_etiqueta" color color
                        text r[1] style "mj_cuerpo" substitute False

            null height 6

            fixed:
                xalign 0.5
                xysize (b[0], b[1])
                use cinta_boton("Empezar", Function(vivo.empezar), "nino", b[0], b[1], b[2])

            text "Enter o Espacio":
                style "mj_nota"
                xalign 0.5


## Una caja de un estante. estado: libre | ok | mal
## trad_at: transform de la traducción (n1_trad_at).
screen mj_n1_caja(clave, estado, accion, trad_at, color):

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
        background n1_fondo(fondo, borde)
        hover_background n1_fondo(hover, "#FFFFFF")

        vbox:
            xalign 0.5
            yalign 0.5
            yoffset 6
            spacing 2
            text clave:
                style "mj_cuerpo"
                color "#FFFFFF"
                xalign 0.5
                text_align 0.5
                xmaximum (N1_CAJA_W - 28)
                substitute False
            text es_txt:
                style "mj_nota"
                xalign 0.5
                text_align 0.5
                xmaximum (N1_CAJA_W - 28)
                at trad_at

        if marca != "":
            text marca:
                style "mj_nota"
                xpos 14
                ypos 4
                color borde


## Franja de la lista (arriba del área): quién la pidió, los productos, la
## racha, el sexto hueco y la memoria (barra, «Mirar lista» o «MIRANDO…»).
screen mj_n1_lista(vivo, trad_at):

    $ col_l = PETALO_COLOR[vivo.hermana_lista]
    $ tono_l = TARJETA_TONO[vivo.hermana_lista]
    $ lista_ok = vivo.lista_visible()
    $ mem_r = vivo.memoria_restante()
    $ izq = N1_IZQ_X - MJ_AREA_X
    $ cel = N1_CELDA_X - MJ_AREA_X
    $ ancho_mem = N1_CELDA_W * 4
    $ sec = MJ_BOTON["secundario"]

    fixed:
        xpos MJ_AREA_X
        ypos MJ_AREA_Y
        xysize (MJ_AREA_W, N1_LISTA_H)

        add n1_fondo(tono_l, col_l)

        ## --- Bloque izquierdo: de quién es la lista y la racha ---
        text ("LISTA " + str(vivo.idx + 1) + " / 5"):
            style "mj_etiqueta"
            xpos izq
            ypos 20

        text vivo.hermana_lista.capitalize():
            style "mj_titulo"
            color col_l
            xpos izq
            ypos 46

        if vivo.racha >= 2 and vivo.fase != "sexto" and vivo.fase != "fin":
            text ("RACHA ×" + str(vivo.racha)):
                style "mj_cifra"
                color "#FFE3A0"
                xpos izq
                ypos 104

        hbox:
            xpos izq
            ypos 160
            spacing 12
            if vivo.sexto != "":
                add Solid("#58D68D", xsize=20, ysize=20) yalign 0.5
            else:
                add Solid("#FFFFFF22", xsize=20, ysize=20) yalign 0.5
            text "6.º hueco de la cesta" style "mj_nota" color "#FFE3A0" yalign 0.5

        ## --- Productos: una celda por producto ---
        hbox:
            xpos cel
            ypos 20

            for k in vivo.claves:
                $ hecho = k in vivo.encontrados
                fixed:
                    xysize (N1_CELDA_W, 112)

                    if hecho:
                        add Solid("#58D68D", xsize=24, ysize=24) ypos 6
                    else:
                        add Solid("#FFFFFF33", xsize=24, ysize=24) ypos 6

                    vbox:
                        xpos 36
                        xsize (N1_CELDA_W - 48)
                        spacing 0
                        if hecho:
                            text k style "mj_cuerpo" color "#8EE8B0" substitute False
                        elif lista_ok:
                            text k style "mj_cuerpo" color "#FFFFFF" substitute False
                            text MJ_N1_ITEMS[k] style "mj_nota" at trad_at
                        else:
                            text n1_mascara(k) style "mj_cuerpo" color "#B9A8D8" substitute False

        ## --- Memoria: barra que se vacía, «MIRANDO…» o «Mirar lista» ---
        if mem_r >= 0.0:
            if vivo.mirada_t > 0.0:
                text "MIRANDO…":
                    style "mj_etiqueta"
                    color "#FFE3A0"
                    xpos cel
                    ypos 160
            elif lista_ok:
                text "MEMORIZA":
                    style "mj_etiqueta"
                    color "#FFE3A0"
                    xpos cel
                    ypos 146
                fixed:
                    xpos cel
                    ypos 178
                    xysize (ancho_mem, 12)
                    add Solid("#FFFFFF2A")
                    add Solid("#FFE3A0", ysize=12) at n1_vaciar(int(ancho_mem * mem_r / vivo.memoria), mem_r)
            else:
                fixed:
                    xpos cel
                    ypos 132
                    xysize (sec[0], sec[1])
                    use cinta_boton(("Mirar lista (−" + n1_seg(vivo.mirar_costo) + " s)"), Function(vivo.mirar), vivo.hermana_lista, sec[0], sec[1], sec[2])


## Los estantes: una cinta por fila, a todo lo ancho del área.
screen mj_n1_estantes(vivo, trad_at):

    $ col_l = PETALO_COLOR[vivo.hermana_lista]
    $ y0 = n1_fila_y0(len(vivo.estantes))

    for fi in range(len(vivo.estantes)):

        $ flecha = ""
        if vivo.deriva > 0.0:
            if vivo.fila_sentido(fi) > 0:
                $ flecha = "   >>>"
            else:
                $ flecha = "   <<<"

        $ mov = vivo.fila_mov(fi)
        $ cinta = []
        if mov[1] > 0.0:
            $ cinta = [n1_cinta(mov[0], mov[1])]

        fixed:
            xpos MJ_AREA_X
            ypos (y0 + fi * N1_FILA_H)
            xysize (N1_VENTANA_W, N1_FILA_ALTO)
            clipping True

            add Solid("#FFFFFF14")

            text ("ESTANTE " + "ABCD"[fi] + flecha):
                style "mj_etiqueta"
                xpos 18
                ypos 0

            fixed:
                xysize (N1_VENTANA_W, N1_FILA_ALTO)
                at cinta
                for c in vivo.fila_base(fi):
                    fixed:
                        xpos c[1]
                        ypos 32
                        xysize (N1_CAJA_W, N1_CAJA_H)
                        use mj_n1_caja(c[0], vivo.estado_caja(c[0]), Function(vivo.elegir, c[0]), trad_at, col_l)


## El sexto hueco: sin cinta, sin prisa y sin avisos. Debajo de la franja,
## la frase y las tres opciones, centradas en el área.
screen mj_n1_sexto(vivo):

    text "Queda sitio para una cosa más en la cesta.":
        style "mj_aviso_texto"
        color "#FFF8FC"
        xpos MJ_AREA_CX
        xanchor 0.5
        ypos 392

    vbox:
        xpos MJ_AREA_CX
        xanchor 0.5
        ypos 470
        spacing 22

        for op in MJ_N1_SEXTO:
            use mj_n1_sexto_op(op[1], op[2], Function(vivo.elegir_sexto, op[0]), PETALO_COLOR["nino"], (vivo.sexto == op[0]))


screen mj_n1(hermana, params, inicio, intento, fallos, nivel, titulo):

    modal True
    zorder 95

    default vivo = MJN1(params, inicio, fallos, intento)

    ## La lógica, sin reiniciar la interacción: tick() la reinicia solo si
    ## cambia algo visible (MJN1.firma).
    timer 0.033 repeat True action Function(vivo.tick, _update_screens=False)

    key "K_RETURN" action Function(vivo.empezar)
    key "K_SPACE" action Function(vivo.empezar)

    $ trad_at = n1_trad_at(vivo)
    $ en_sexto = (vivo.fase == "sexto" or vivo.fase == "fin")
    ## En el sexto hueco no hay prisa: el reloj desaparece del HUD.
    $ t_rest = vivo.restante()
    $ t_tot = vivo.total
    if en_sexto:
        $ t_rest = None
        $ t_tot = None

    add "bg_centro_comercial" fit "cover"

    use mj_marco(hermana, titulo, intento, fallos, nivel, vivo.lista, 5, t_rest, t_tot, "LISTAS", chibi=vivo.expresion_star(), globo=vivo.globo, anim=vivo.anim_star(), aviso=vivo.aviso_vivo(), aviso_tipo=vivo.aviso_tipo):

        ## --- Tensión: solo sobre el área, nunca sobre la columna ---
        if vivo.tension():
            add Solid("#FF2D2D", xsize=MJ_AREA_W, ysize=MJ_AREA_H) xpos MJ_AREA_X ypos MJ_AREA_Y at n1_latido

        if vivo.flash_t > 0.0:
            add Solid("#FF3B3B", xsize=MJ_AREA_W, ysize=MJ_AREA_H) xpos MJ_AREA_X ypos MJ_AREA_Y at n1_destello

        if vivo.fase == "listo":

            use mj_n1_intro(vivo, nivel)

        else:

            use mj_n1_lista(vivo, trad_at)

            if en_sexto:
                use mj_n1_sexto(vivo)
            else:
                use mj_n1_estantes(vivo, trad_at)

            ## --- Cuenta atrás, sobre el área ---
            if vivo.fase == "cuenta":
                add Solid("#0B0712A0", xsize=MJ_AREA_W, ysize=MJ_AREA_H) xpos MJ_AREA_X ypos MJ_AREA_Y
                text str(vivo.cuenta_n()):
                    style "mj_cifra_grande"
                    xpos MJ_AREA_CX
                    xanchor 0.5
                    ypos (MJ_AREA_Y + MJ_AREA_H // 2)
                    yanchor 0.5
                text "PREPÁRATE":
                    style "mj_etiqueta"
                    color "#FFE3A0"
                    xpos MJ_AREA_CX
                    xanchor 0.5
                    ypos (MJ_AREA_Y + MJ_AREA_H // 2 + 90)


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
        background n1_fondo(fondo, borde)
        hover_background n1_fondo(hover, "#FFFFFF")

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 4
            text titulo:
                style "mj_aviso_texto"
                color "#FFFFFF"
                xalign 0.5
                text_align 0.5
            text sub:
                style "mj_cuerpo"
                color "#CFC6E0"
                xalign 0.5
                text_align 0.5

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

    call mj_ejecutar("n1", "nino") from _call_mj_ejecutar_9

    $ n1_res = _return
    $ n1_info = e6_mj["nino"]
    $ narrator("Resultado: " + str(n1_res) + " · intentos " + str(n1_info["intentos"]) + " · fallos " + str(n1_info["fallos"]) + " · nivel " + n1_info["nivel"] + " · sexto: " + str(n1_info["datos"].get("sexto", "")))
    return
