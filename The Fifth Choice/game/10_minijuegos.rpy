################################################################################
##  10_minijuegos.rpy — Núcleo del Evento 6 y marco de minijuegos
##  Parte A: constantes y datos · Parte B: funciones E6 · Parte C: marco mj_*
##  Parte D: label mj_ejecutar · Parte E: screens (marco + minijuego de prueba)
################################################################################

default mj_estado = {}
default mj_res = {}
default mj_resp = ""
default persistent.mj_modo = "normal"      ## "normal" | "asistido" | "saltar"

################################################################################
##  PARTE A · CONSTANTES Y DATOS
################################################################################

define E6_ORDEN_CANON  = ["ichika", "nino", "miku", "yotsuba", "itsuki"]
define E6_ORDEN_EXAMEN = ["yotsuba", "ichika", "nino", "itsuki", "miku"]

define E6_MATERIA = {
    "ichika": "Matemáticas", "nino": "Inglés", "miku": "Sociales",
    "yotsuba": "Japonés", "itsuki": "Ciencias",
}

define E6_FRASE_DE_ESTADO = {
    "calida": "completa", "tibia": "cortada", "fria": "cerrada", "no_visitada": "espera",
}

## Notas fuera de la diagonal (§3.5) y ajuste por estado_entrada.
define E6_RANGO_NOTA = {
    "calida": (82, 89), "tibia": (72, 79), "no_visitada": (68, 75), "fria": (60, 66),
}
define E6_AJUSTE_NOTA = {"bueno": 3, "mixto": 0, "superado": -2}

## Qué minijuego del MJ_REGISTRO usa cada hermana. Ahora todos "prueba":
## los chats 5 y 6 cambian aquí a "y2", "i1", "n1", "it1", "m3".
define E6_MJ_JUEGO = {
    "yotsuba": "y2", "ichika": "i1", "nino": "n1",
    "itsuki": "it1", "miku": "m3",
}

define MJ_NIVELES = ["dificil", "media", "asistida"]
define MJ_FALLOS_MEDIO = 2       ## fallos → asistencia a medio camino
define MJ_FALLOS_COMPLETO = 4    ## fallos → asistencia completa (un nivel más)
define MJ_FALLOS_SALTO = 6       ## fallos → se ofrece «Que lo haga ella»
define MJ_MODO_TACTIL = "normal" ## modo que se fuerza en móvil/tablet ("asistido" si quieres)

## Registro: los chats 5 y 6 enchufan aquí sus minijuegos con mj_registrar().
define MJ_REGISTRO = {}

## Parámetros (§5.4). Convención: numéricos se interpolan en la asistencia;
## el resto (listas, textos, bool, None=infinito) «saltan» al nivel siguiente.
## puntos_control = unidades de progreso donde se guarda checkpoint
## (la unidad la define cada minijuego: tramo, línea, lista, paso, nota…).
define MJ_PARAMS = {
    "prueba": {
        "dificil":  {"aciertos": 8, "ventana": 0.10, "velocidad": 1.00, "fallos_max": 3, "puntos_control": [4]},
        "media":    {"aciertos": 6, "ventana": 0.16, "velocidad": 0.75, "fallos_max": 5, "puntos_control": [2, 4]},
        "asistida": {"aciertos": 4, "ventana": 0.24, "velocidad": 0.60, "fallos_max": 8, "puntos_control": [2]},
    },
    "y2": {
        "dificil":  {"tramos": 56, "ventana": 0.05, "ventana_fin": 0.60, "velocidad": 1.00, "rampa": 1.3,
                    "testigos": 4, "cura": 10, "senuelo": 0.20, "ocultar": 0.70, "zona": False,
                    "salida_falsa": "penaliza", "puntos_control": [14, 28, 42]},
        "media":    {"tramos": 28, "ventana": 0.22, "ventana_fin": 0.80, "velocidad": 0.80, "rampa": 0.6,
                    "testigos": 6, "cura": 8, "senuelo": 0.08, "ocultar": 1.0, "zona": True,
                    "salida_falsa": "avisa", "puntos_control": [7, 14, 21]},
        "asistida": {"tramos": 14, "ventana": 0.36, "ventana_fin": 1.00, "velocidad": 0.65, "rampa": 0.3,
                    "testigos": 9, "cura": 6, "senuelo": 0.0, "ocultar": 1.0, "zona": True,
                    "salida_falsa": "ignora", "puntos_control": [7]},
    },
    "i1": {
        "dificil":  {"lineas": 12, "mascara_ini": 25, "energia_ini": 90,  "mascara_actuada": 32, "mascara_sincera": 20, "energia_actuada": 6,  "energia_sincera": 26, "peso_mascara": 1.0, "mantener": 0.70, "tiempo_linea": 2.6, "puntos_control": [6]},
        "media":    {"lineas": 10, "mascara_ini": 25, "energia_ini": 90,  "mascara_actuada": 16, "mascara_sincera": 22, "energia_actuada": 9,  "energia_sincera": 22, "peso_mascara": 0.7, "mantener": 0.50, "tiempo_linea": 3.4, "puntos_control": [4, 8]},
        "asistida": {"lineas": 8,  "mascara_ini": 20, "energia_ini": 100, "mascara_actuada": 8, "mascara_sincera": 26, "energia_actuada": 12, "energia_sincera": 18, "peso_mascara": 0.4, "mantener": 0.35, "tiempo_linea": 4.5, "puntos_control": [3, 6]},
    },
    "n1": {
        "dificil":  {"tiempo_total": 75,  "retardo_traduccion": 1.4, "distractores": 3, "penalizacion": 6, "puntos_control": [3]},
        "media":    {"tiempo_total": 105, "retardo_traduccion": 0.5, "distractores": 2, "penalizacion": 3, "puntos_control": [1, 2, 3, 4, 5]},
        "asistida": {"tiempo_total": 140, "retardo_traduccion": 0.0, "distractores": 1, "penalizacion": 1, "puntos_control": [1, 2, 3, 4, 5]},
    },
    "it1": {
        "dificil":  {"pasos": 5, "tiempo": 55,  "numeros_trampa": 2, "trampa_marcada": False, "intentos": 3,    "ayuda_usos": 1,    "ayuda_costo": 10, "plausibilidad": False, "puntos_control": []},
        "media":    {"pasos": 4, "tiempo": 80,  "numeros_trampa": 1, "trampa_marcada": False, "intentos": 5,    "ayuda_usos": 2,    "ayuda_costo": 5,  "plausibilidad": True,  "puntos_control": []},
        "asistida": {"pasos": 3, "tiempo": 110, "numeros_trampa": 1, "trampa_marcada": True,  "intentos": None, "ayuda_usos": None, "ayuda_costo": 0,  "plausibilidad": True,  "puntos_control": []},
    },
    "m3": {
        "dificil":  {"fase1_notas": 48, "ventana_ms": 80,  "fallos_max": 8,  "fase2_notas": 24, "fase2_guia": "ninguna", "puntos_control": [48]},
        "media":    {"fase1_notas": 36, "ventana_ms": 140, "fallos_max": 14, "fase2_notas": 16, "fase2_guia": "tenue",   "puntos_control": [16, 32, 36]},
        "asistida": {"fase1_notas": 28, "ventana_ms": 200, "fallos_max": 24, "fase2_notas": 12, "fase2_guia": "clara",   "puntos_control": [12, 24, 28]},
    },
}

## Líneas de fallo por hermana e intento (1.º, 2.º, 3.º y siguientes).
## (quién, texto): "int" = voz interior de la hermana, "narrador" = narrador.
## RELLENO tomado de §5.5: lo sustituyen los guiones de los chats 3 y 4.
define MJ_FALLOS = {
    "yotsuba": [("int", "¡Otra vez!"), ("int", "¡Otra vez! ¡Esta sí!"), ("int", "…Otra vez. Despacio.")],
    "ichika":  [("narrador", "Se quedó en blanco. Sonrió para que no se notara."), ("narrador", "La sonrisa tardó un poco más en volver."), ("narrador", "Esta vez no sonrió. Respiró, y empezó otra vez.")],
    "nino":    [("int", "Tsk."), ("int", "…Otra vez. No mires."), ("int", "Otra vez.")],
    "itsuki":  [("int", "Revisaré desde el principio."), ("int", "Revisaré desde el principio."), ("int", "Revisaré desde el principio.")],
    "miku":    [("int", "…Perdón."), ("int", "…Perd—"), ("int", "…Otra vez.")],
}

################################################################################
##  PARTE B · FUNCIONES DEL EVENTO 6
################################################################################

init python:

    import time

    def e6_verificar(condicion, mensaje):
        """Invariante rota → excepción con mensaje legible."""
        if not condicion:
            raise Exception("[E6] " + mensaje)

    def e6_puntos_actuales():
        res = {}
        for h in E6_ORDEN_CANON:
            res[h] = getattr(store, "puntos_" + h)
        return res

    def e6_estado_de(h):
        """Estado de la hermana h en E6: calida | tibia | fria | no_visitada.
        (La variable es e6_estado; la función NO puede llamarse igual.)"""
        est = store.e6_estado.get(h)
        e6_verificar(est is not None, "e6_estado no tiene a '" + h + "': ¿se llamó a e6_iniciar()?")
        return est

    def e6_calcular_notas():
        """Matriz determinista 5×5 (§3.5): notas[quien_rinde][materia_de]. Valida I1 e I2."""
        entrada = store.e6_estado_entrada
        e6_verificar(entrada in E6_AJUSTE_NOTA, "estado_entrada desconocido: " + str(entrada))
        ajuste = E6_AJUSTE_NOTA[entrada]
        notas = {}
        for i in range(5):
            h = E6_ORDEN_CANON[i]
            rango = E6_RANGO_NOTA[e6_estado_de(h)]
            lo = rango[0]
            amplitud = rango[1] - rango[0] + 1
            fila = {}
            for j in range(5):
                m = E6_ORDEN_CANON[j]
                if i == j:
                    fila[m] = 100
                else:
                    v = lo + ((i * 3 + j * 5 + 1) % amplitud) + ajuste
                    if v < 60:
                        v = 60
                    if v > 89:
                        v = 89
                    fila[m] = v
            notas[h] = fila
        for h in E6_ORDEN_CANON:
            for m in E6_ORDEN_CANON:
                nota = notas[h][m]
                e6_verificar(nota >= 60, "I1: " + h + " reprueba " + m + " con " + str(nota))
                if h == m:
                    e6_verificar(nota == 100, "I2: la diagonal de " + h + " no es 100")
                else:
                    e6_verificar(nota < 100, "I2: 100 fuera de la diagonal (" + h + " en " + m + ")")
        return notas

    def e6_iniciar():
        """Se llama una vez al entrar a E6. Calcula estados, entrada y notas; valida."""
        e6_verificar(not store.despido_cap1, "I7: despido_cap1 es True; E6 no puede activarse.")
        e6_verificar(store.nino_rama_beat in ("calida", "tibia", "fria"),
                     "nino_rama_beat es " + str(store.nino_rama_beat) + ": el beat de Nino no se jugó.")
        estados = {}
        visitadas = 0
        frias = 0
        for h in E6_ORDEN_CANON:
            rama = rama_de(h)
            if rama is None:
                estados[h] = "no_visitada"
            else:
                e6_verificar(rama in ("calida", "tibia", "fria"), "rama inválida en " + h + ": " + str(rama))
                estados[h] = rama
                visitadas += 1
                if rama == "fria":
                    frias += 1
        e6_verificar(visitadas == 3, "Debe haber exactamente 3 visitadas (hay " + str(visitadas) + ").")
        e6_verificar(frias <= 1, "Máximo 1 fría (hay " + str(frias) + "): dos frías terminan en despido.")

        forzada = getattr(store, "e6_forzar_entrada", None)
        if forzada is not None:
            entrada = forzada
        else:
            e6_verificar(store.clima_cap1 in ("buena", "mixta"), "clima_cap1 es '" + str(store.clima_cap1) + "'.")
            if store.maruo_ultimatum:
                e6_verificar(frias >= 1, "maruo_ultimatum sin ninguna hermana fría.")
                entrada = "superado"
            elif store.clima_cap1 == "buena":
                entrada = "bueno"
            else:
                entrada = "mixto"

        store.e6_estado = estados
        store.e6_estado_entrada = entrada
        store.e6_frase = {}
        store.e6_promesas = []
        store.e6_mj = {}
        store.e6_puntos_ini = e6_puntos_actuales()
        store.e6_notas = e6_calcular_notas()

    def e6_marcar_ganchos(h):
        """Escribe e6_frase[h] (y e6_promesas si no visitada). Lo llama e6_bloque."""
        est = e6_estado_de(h)
        store.e6_frase[h] = E6_FRASE_DE_ESTADO[est]
        if est == "no_visitada":
            if h not in store.e6_promesas:
                store.e6_promesas.append(h)

    def e6_orden_ecos():
        """Orden de Mov. 8: visitadas en orden de examen; las no visitadas, las últimas."""
        presentes = []
        ausentes = []
        for h in E6_ORDEN_EXAMEN:
            if e6_estado_de(h) == "no_visitada":
                ausentes.append(h)
            else:
                presentes.append(h)
        return presentes + ausentes

    def e6_cerrar():
        """Comprobación final de invariantes (I1–I3, I5–I8, I10). Al final de evento_6."""
        e6_verificar(not store.despido_cap1, "I7: despido_cap1 es True al cerrar E6.")
        ini = store.e6_puntos_ini
        e6_verificar(len(ini) == 5, "e6_puntos_ini vacío: ¿se llamó a e6_iniciar()?")
        for h in E6_ORDEN_CANON:
            e6_verificar(getattr(store, "puntos_" + h) == ini[h],
                         "I8: E6 modificó puntos_" + h + " (" + str(ini[h]) + " → " + str(getattr(store, "puntos_" + h)) + ")")
        for h in store.e6_mj:
            e6_verificar(e6_estado_de(h) == "calida", "I3: hubo minijuego con " + h + ", que está en " + e6_estado_de(h))
        e6_verificar(len(store.e6_mj) <= 3, "I5: más de 3 minijuegos (" + str(len(store.e6_mj)) + ").")
        for h in E6_ORDEN_CANON:
            e6_verificar(h in store.e6_frase, "I6/I10: falta e6_frase['" + h + "'].")
        e6_calcular_notas()

################################################################################
##  PARTE C · MARCO DE MINIJUEGOS (funciones y clases)
################################################################################

    def mj_registrar(clave, pantalla, titulo, persistente=True):
        """Enchufa un minijuego. Su screen recibe: hermana, params, inicio, intento,
        fallos, nivel, titulo; y debe devolver {"resultado": "ganado"|"perdido"|"saltado",
        "progreso": n, "datos": {...}}. Debe declarar modal True y zorder 95."""
        MJ_REGISTRO[clave] = {"pantalla": pantalla, "titulo": titulo, "persistente": persistente}

    def mj_nivel():
        """Nivel base: «media» si MC fue cálido con Nino en su beat; si no, «dificil»."""
        if store.nino_rama_beat == "calida":
            return "media"
        return "dificil"

    def mj_mezclar(a, b, t):
        """Interpola numéricos entre dos niveles; lo demás salta a b si t >= 0.5."""
        res = {}
        for k in a:
            va = a[k]
            vb = b.get(k, va)
            if type(va) in (int, float) and type(vb) in (int, float):
                v = va + (vb - va) * t
                if type(va) is int and type(vb) is int:
                    v = int(round(v))
                res[k] = v
            else:
                if t >= 0.5:
                    res[k] = vb
                else:
                    res[k] = va
        return res

    def mj_fallos_efectivos(e):
        n = e["fallos"]
        if e["modo"] == "asistido" and n < MJ_FALLOS_COMPLETO:
            n = MJ_FALLOS_COMPLETO
        return n

    def mj_paso(fallos):
        if fallos >= MJ_FALLOS_COMPLETO:
            return 1.0
        if fallos >= MJ_FALLOS_MEDIO:
            return 0.5
        return 0.0

    def mj_params_para(e):
        """Parámetros vigentes: nivel base + asistencia (un solo escalón).
        Sin boost: dificil → media (suelo = media). Con boost: media → asistida."""
        base = MJ_NIVELES.index(mj_nivel())
        hasta = base + 1
        if hasta > 2:
            hasta = 2
        tabla = MJ_PARAMS[e["juego"]]
        t = mj_paso(mj_fallos_efectivos(e))
        return mj_mezclar(tabla[MJ_NIVELES[base]], tabla[MJ_NIVELES[hasta]], t)

    def mj_nivel_efectivo(e):
        base = MJ_NIVELES.index(mj_nivel())
        if mj_paso(mj_fallos_efectivos(e)) >= 0.5:
            base = base + 1
        if base > 2:
            base = 2
        return MJ_NIVELES[base]

    def mj_calcular_checkpoint(puntos, progreso, actual):
        mejor = actual
        for p in puntos:
            if p <= progreso and p > mejor:
                mejor = p
        return mejor

    def mj_bloquear(activo):
        """Rollback y skip fuera mientras dura el minijuego (la pantalla además
        se traga las teclas, porque config.* no se guarda: tras cargar vuelve a True)."""
        e = store.mj_estado
        if activo:
            config.rollback_enabled = False
            config.allow_skipping = False
            config.skipping = None
            store.quick_menu = False
        else:
            config.rollback_enabled = e["prev_rollback"]
            config.allow_skipping = e["prev_skip"]
            store.quick_menu = e["prev_quick"]

    def mj_iniciar(juego, hermana):
        reg = MJ_REGISTRO.get(juego)
        e6_verificar(reg is not None, "Minijuego '" + str(juego) + "' no está en MJ_REGISTRO (registrados: " + ", ".join(sorted(MJ_REGISTRO.keys())) + ").")
        e6_verificar(juego in MJ_PARAMS, "Faltan parámetros de '" + juego + "' en MJ_PARAMS.")
        e6_verificar(hermana in E6_ORDEN_CANON, "Hermana desconocida: " + str(hermana))
        est = store.e6_estado.get(hermana)
        if est is not None:
            e6_verificar(est == "calida", "I3: minijuego solo en cálida; " + hermana + " está en '" + est + "'.")

        modo = persistent.mj_modo
        if modo not in ("normal", "asistido", "saltar"):
            modo = "normal"
        if modo == "normal" and renpy.variant("touch"):
            modo = MJ_MODO_TACTIL

        store.mj_estado = {
            "juego": juego,
            "hermana": hermana,
            "pantalla": reg["pantalla"],
            "titulo": reg["titulo"],
            "persistente": reg["persistente"],
            "boost": (store.nino_rama_beat == "calida"),
            "modo": modo,
            "repeticion": bool(getattr(persistent, "e6_mj_ganado_" + hermana, False)),
            "intentos": 0,
            "fallos": 0,
            "checkpoint": 0,
            "datos": {},
            "prev_rollback": config.rollback_enabled,
            "prev_skip": config.allow_skipping,
            "prev_quick": store.quick_menu,
        }
        mj_bloquear(True)

    def mj_preparar_intento():
        mj_bloquear(True)
        renpy.block_rollback()

    def mj_args_pantalla():
        e = store.mj_estado
        return {
            "hermana": e["hermana"],
            "params": mj_params_para(e),
            "inicio": e["checkpoint"],
            "intento": e["intentos"] + 1,
            "fallos": e["fallos"],
            "nivel": mj_nivel_efectivo(e),
            "titulo": e["titulo"],
        }

    def mj_registrar_intento(res):
        e = store.mj_estado
        e6_verificar(type(res) is dict or hasattr(res, "get"), "La screen del minijuego debe devolver un dict.")
        e6_verificar(res["resultado"] in ("ganado", "perdido", "saltado"), "Resultado inválido: " + str(res["resultado"]))
        e["intentos"] += 1
        datos = res.get("datos")
        if datos:
            for k in datos:
                e["datos"][k] = datos[k]
        if res["resultado"] == "perdido":
            e["fallos"] += 1
            puntos = mj_params_para(e).get("puntos_control", [])
            e["checkpoint"] = mj_calcular_checkpoint(puntos, res.get("progreso", 0), e["checkpoint"])

    def mj_linea_fallo():
        """Dice la línea de fallo de la hermana según el nº de fallos acumulados."""
        e = store.mj_estado
        lineas = MJ_FALLOS.get(e["hermana"])
        if lineas is None:
            return
        i = e["fallos"]
        if i > len(lineas):
            i = len(lineas)
        quien = lineas[i - 1][0]
        texto = lineas[i - 1][1]
        if quien == "int":
            hablante = getattr(store, e["hermana"] + "_int")
        else:
            hablante = store.narrador
        renpy.say(hablante, texto)

    def mj_ofrecer_salto():
        narrator("Varios intentos fallidos.", interact=False)
        return renpy.display_menu([("Intentarlo otra vez", "otra"), ("Que lo haga ella", "saltar")])

    def mj_preguntar_repeticion():
        narrator("Ya superaste este minijuego.", interact=False)
        return renpy.display_menu([("Jugarlo otra vez", "jugar"), ("Saltarlo", "saltar")])

    def mj_cerrar(resultado):
        """Restaura la interfaz, anota e6_mj[hermana] (sin puntos: P-09) y cierra el rollback."""
        e = store.mj_estado
        mj_bloquear(False)
        h = e["hermana"]
        store.e6_mj[h] = {
            "juego": e["juego"],
            "resultado": resultado,
            "intentos": e["intentos"],
            "fallos": e["fallos"],
            "nivel": mj_nivel_efectivo(e),
            "boost": e["boost"],
            "datos": dict(e["datos"]),
        }
        if resultado == "ganado" and e["persistente"]:
            setattr(persistent, "e6_mj_ganado_" + h, True)
        renpy.block_rollback()

    class MJReloj(object):
        """Reloj propio. El dt se capa: si el juego estuvo en pausa (Esc), ese
        hueco cuenta como máximo `tope` segundos."""
        def __init__(self, tope=0.12):
            self.tope = tope
            self.t = 0.0
            self.ultimo = None

        def avanzar(self):
            ahora = time.perf_counter()
            if self.ultimo is None:
                self.ultimo = ahora
            dt = ahora - self.ultimo
            self.ultimo = ahora
            if dt < 0.0:
                dt = 0.0
            if dt > self.tope:
                dt = self.tope
            self.t += dt
            return dt

    class MJPrueba(object):
        """Minijuego de prueba de un botón. Estado vivo: lo crea la screen (default),
        no se guarda; al cargar, el intento reinicia desde el checkpoint."""
        def __init__(self, params, inicio):
            self.p = params
            self.reloj = MJReloj()
            self.aciertos = inicio
            self.necesarios = params["aciertos"]
            self.fallos = 0
            self.zona = 0.15 + renpy.random.random() * 0.70
            self.ultimo = ""
            self.flash = 0.0

        def posicion(self):
            fase = (self.reloj.t * self.p["velocidad"] * 0.5) % 1.0
            return abs(fase * 2.0 - 1.0)

        def tick(self):
            dt = self.reloj.avanzar()
            if self.flash > 0.0:
                self.flash -= dt
                if self.flash <= 0.0:
                    self.ultimo = ""
            return None

        def pulsar(self):
            self.reloj.avanzar()
            if abs(self.posicion() - self.zona) <= self.p["ventana"] / 2.0:
                self.aciertos += 1
                self.ultimo = "acierto"
                self.flash = 0.35
                self.zona = 0.15 + renpy.random.random() * 0.70
                if self.aciertos >= self.necesarios:
                    return {"resultado": "ganado", "progreso": self.aciertos, "datos": {}}
            else:
                self.fallos += 1
                self.ultimo = "fallo"
                self.flash = 0.35
                if self.fallos > self.p["fallos_max"]:
                    return {"resultado": "perdido", "progreso": self.aciertos, "datos": {}}
            return None

    mj_registrar("prueba", "mj_prueba", "Prueba de un botón", True)

################################################################################
##  PARTE D · LABEL mj_ejecutar
##  Uso:  call mj_ejecutar("y2", "yotsuba")  →  _return = "ganado" | "saltado"
##  («perdido» es resultado de intento: el bucle repite. El guion trata
##  "ganado" y "saltado" como éxito; el detalle queda en e6_mj[hermana].)
################################################################################

label mj_ejecutar(juego, hermana):

    $ mj_iniciar(juego, hermana)

    if mj_estado["modo"] == "saltar":
        $ mj_cerrar("saltado")
        return "saltado"

    if mj_estado["repeticion"]:
        $ mj_resp = mj_preguntar_repeticion()
        if mj_resp == "saltar":
            $ mj_cerrar("saltado")
            return "saltado"

label .intento:

    $ mj_preparar_intento()
    $ mj_res = renpy.call_screen(mj_estado["pantalla"], **mj_args_pantalla())
    $ mj_registrar_intento(mj_res)

    if mj_res["resultado"] == "ganado":
        $ mj_cerrar("ganado")
        return "ganado"

    if mj_res["resultado"] == "saltado":
        $ mj_cerrar("saltado")
        return "saltado"

    $ mj_linea_fallo()

    if mj_estado["fallos"] >= MJ_FALLOS_SALTO:
        $ mj_resp = mj_ofrecer_salto()
        if mj_resp == "saltar":
            $ mj_cerrar("saltado")
            return "saltado"

    jump .intento

################################################################################
##  PARTE E · SCREENS
################################################################################

## HUD común. Uso:  use mj_marco(...):  <contenido>   (la screen llamadora debe
## declarar `modal True` y `zorder 95`; los `key` se tragan rollback y skip).
screen mj_marco(hermana, titulo, intento=1, fallos=0, nivel="dificil", progreso=0, total=1, tiempo=None, tiempo_total=None, unidad="ACIERTOS"):

    $ color = PETALO_COLOR[hermana]
    $ cinta = ui_mezclar(color, "#FFFFFF", 0.35)
    $ tinta = ui_mezclar(color, "#000000", 0.75)

    key "rollback" action NullAction()
    key "rollforward" action NullAction()
    key "skip" action NullAction()
    key "toggle_skip" action NullAction()
    key "fast_skip" action NullAction()

    add Solid("#0B0712B8")

    use flor_sakura(hermana, "narrador", 1690, 800, color)

    use hud_cinta_vista(titulo, "MINIJUEGO", hermana, cinta, tinta, hud_cinta_entrada)

    vbox:
        xalign 1.0
        xoffset -44
        ypos 30
        spacing 6
        text ("INTENTO " + str(intento)):
            xalign 1.0
            font gui.name_text_font
            size 24
            kerning 3
            color "#FFFFFF"
            outlines [(3, "#1B102699", 0, 0)]
        if fallos > 0:
            text ("FALLIDOS " + str(fallos)):
                xalign 1.0
                font gui.name_text_font
                size 20
                kerning 3
                color "#E8E0F2"
                outlines [(3, "#1B102699", 0, 0)]
        if nivel == "asistida":
            text "ASISTENCIA":
                xalign 1.0
                font gui.name_text_font
                size 20
                kerning 3
                color "#FFE3A0"
                outlines [(3, "#1B102699", 0, 0)]

    vbox:
        xalign 0.5
        ypos 920
        spacing 10
        text (unidad + "   " + str(progreso) + " / " + str(total)):
            xalign 0.5
            font gui.name_text_font
            size 22
            kerning 3
            color "#FFFFFF"
            outlines [(3, "#1B102699", 0, 0)]
        use barra_progreso(progreso, total, color, 900)
        if tiempo is not None and tiempo_total is not None:
            use barra_progreso(tiempo, tiempo_total, "#FFE3A0", 900)

    transclude


## Minijuego de prueba: un botón (clic, toque o Espacio/Intro).
screen mj_prueba(hermana, params, inicio, intento, fallos, nivel, titulo):

    modal True
    zorder 95

    default vivo = MJPrueba(params, inicio)

    timer 0.03 repeat True action Function(vivo.tick)

    key "K_SPACE" action Function(vivo.pulsar)
    key "K_RETURN" action Function(vivo.pulsar)

    $ color = PETALO_COLOR[hermana]
    $ ancho = 900
    $ marcador = int(vivo.posicion() * ancho)
    $ zona_x = int((vivo.zona - params["ventana"] / 2.0) * ancho)
    $ zona_w = int(params["ventana"] * ancho)

    use mj_marco(hermana, titulo, intento, fallos, nivel, vivo.aciertos, vivo.necesarios):

        text "Pulsa cuando la barra pase por la zona.":
            xalign 0.5
            ypos 330
            size 30
            color "#FFFFFF"
            outlines [(3, "#1B102699", 0, 0)]

        fixed:
            xalign 0.5
            ypos 430
            xysize (ancho, 60)
            add Solid("#FFFFFF2A", xsize=ancho, ysize=40) yalign 0.5
            add Solid(color + "B0", xsize=zona_w, ysize=40) xpos zona_x yalign 0.5
            add Solid("#FFFFFF", xsize=8, ysize=60) xpos (marcador - 4)

        if vivo.ultimo == "acierto":
            text "¡Bien!" xalign 0.5 ypos 520 size 32 color "#CFFFD8" outlines [(3, "#1B102699", 0, 0)]
        elif vivo.ultimo == "fallo":
            text "Fallo" xalign 0.5 ypos 520 size 32 color "#FFC4C4" outlines [(3, "#1B102699", 0, 0)]

        text ("ERRORES  " + str(vivo.fallos) + " / " + str(params["fallos_max"])):
            xalign 0.5
            ypos 580
            size 24
            color "#E8E0F2"
            outlines [(3, "#1B102699", 0, 0)]

        fixed:
            xalign 0.5
            ypos 650
            xysize (420, 96)
            use cinta_boton("¡Ahora!", Function(vivo.pulsar), hermana, 420, 96, 40)