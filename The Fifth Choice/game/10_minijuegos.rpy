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
        "dificil":  {"tiempo_total": 58,  "productos": 4, "distractores": 3, "mezclado": True,  "deriva": 140, "memoria": 5.0,   "mirar_costo": 2.0, "retardo_traduccion": 2.5, "penalizacion": 6, "racha_bonus": 1.5, "puntos_control": [3]},
        "media":    {"tiempo_total": 80,  "productos": 3, "distractores": 3, "mezclado": False, "deriva": 55,  "memoria": 12.0,  "mirar_costo": 1.0, "retardo_traduccion": 0.8, "penalizacion": 3, "racha_bonus": 2.0, "puntos_control": [1, 2, 3, 4, 5]},
        "asistida": {"tiempo_total": 115, "productos": 3, "distractores": 1, "mezclado": False, "deriva": 0,   "memoria": 999.0, "mirar_costo": 0.0, "retardo_traduccion": 0.0, "penalizacion": 1, "racha_bonus": 3.0, "puntos_control": [1, 2, 3, 4, 5]},
    },
    "it1": {
        "dificil":  {"pasos": 5, "tiempo": 55,  "numeros_trampa": 2, "trampa_marcada": False, "intentos": 3,    "ayuda_usos": 1,    "ayuda_costo": 10, "plausibilidad": False, "puntos_control": []},
        "media":    {"pasos": 4, "tiempo": 80,  "numeros_trampa": 1, "trampa_marcada": False, "intentos": 5,    "ayuda_usos": 2,    "ayuda_costo": 5,  "plausibilidad": True,  "puntos_control": []},
        "asistida": {"pasos": 3, "tiempo": 110, "numeros_trampa": 1, "trampa_marcada": True,  "intentos": None, "ayuda_usos": None, "ayuda_costo": 0,  "plausibilidad": True,  "puntos_control": []},
    },
    "m3": {
        "dificil":  {"fase1_notas": 56, "ventana_ms": 85,  "fallos_max": 7,  "fase2_notas": 28, "fase2_guia": "ninguna",
                    "caida": 1.05, "p_corchea": 0.45, "p_doble": 0.20, "p_silencio": 0.18,
                    "p_corchea2": 0.30, "p_silencio2": 0.22, "penal_extra": 0.5,
                    "combo_cada": 10, "regen_combo": 0.10, "regen_acierto": 0.0, "puntos_control": [28, 56]},
        "media":    {"fase1_notas": 40, "ventana_ms": 130, "fallos_max": 11, "fase2_notas": 20, "fase2_guia": "tenue",
                    "caida": 1.40, "p_corchea": 0.28, "p_doble": 0.10, "p_silencio": 0.12,
                    "p_corchea2": 0.15, "p_silencio2": 0.12, "penal_extra": 0.25,
                    "combo_cada": 8, "regen_combo": 0.10, "regen_acierto": 0.0, "puntos_control": [20, 40]},
        "asistida": {"fase1_notas": 30, "ventana_ms": 190, "fallos_max": 20, "fase2_notas": 14, "fase2_guia": "clara",
                    "caida": 1.85, "p_corchea": 0.08, "p_doble": 0.0,  "p_silencio": 0.0,
                    "p_corchea2": 0.0,  "p_silencio2": 0.0,  "penal_extra": 0.0,
                    "combo_cada": 5, "regen_combo": 0.10, "regen_acierto": 0.0, "puntos_control": [15, 30]},
    },
}

## Líneas de fallo por hermana e intento (1.º, 2.º, 3.º y siguientes).
## (quién, texto): "int" = voz interior de la hermana, "narrador" = narrador.
## RELLENO tomado de §5.5: lo sustituyen los guiones de los chats 3 y 4.
define MJ_FALLOS = {
    "yotsuba": [("int", "¡Otra vez!"), ("int", "¡Otra vez! ¡Esta sí!"), ("int", "...Otra vez. Despacio.")],
    "ichika":  [("narrador", "Se quedó en blanco. Sonrió para que no se notara."), ("narrador", "La sonrisa tardó un poco más en volver."), ("narrador", "Esta vez no sonrió. Respiró, y empezó otra vez.")],
    "nino":    [("int", "Tsk."), ("int", "...Otra vez. No mires."), ("int", "Otra vez.")],
    "itsuki":  [("int", "Revisaré desde el principio."), ("int", "Revisaré desde el principio."), ("int", "Revisaré desde el principio.")],
    "miku":    [("int", "...Perdón."), ("int", "...Perd—"), ("int", "...Otra vez.")],
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

    ## Entrada animada (10_mj_transicion.rpy): una sola vez, no en cada reintento.
    call mj_transicion("entrada", hermana, mj_estado["titulo"])

label .intento:

    $ mj_preparar_intento()
    $ mj_res = renpy.call_screen(mj_estado["pantalla"], **mj_args_pantalla())
    $ mj_registrar_intento(mj_res)

    ## Las salidas van ANTES de mj_cerrar: así el menú rápido, el rollback y el
    ## skip siguen bloqueados mientras duran.
    if mj_res["resultado"] == "ganado":
        call mj_transicion("ganado", hermana, mj_estado["titulo"])
        $ mj_cerrar("ganado")
        return "ganado"

    if mj_res["resultado"] == "saltado":
        call mj_transicion("saltado", hermana, mj_estado["titulo"])
        $ mj_cerrar("saltado")
        return "saltado"

    $ mj_linea_fallo()

    if mj_estado["fallos"] >= MJ_FALLOS_SALTO:
        $ mj_resp = mj_ofrecer_salto()
        if mj_resp == "saltar":
            call mj_transicion("saltado", hermana, mj_estado["titulo"])
            $ mj_cerrar("saltado")
            return "saltado"

    jump .intento

################################################################################
##  PARTE E · SCREENS
##  Marco común (dirección «columna de la hermana»). Medidas y reglas:
##  docs/MINIJUEGOS/MARCO_COMUN.md
################################################################################

## --- Zonas de la pantalla (1920×1080) -------------------------------------------
## Columna: x 0–400 (ui/mj_columna.png; MJ_COLUMNA en generar_ui.py).
define MJ_AREA_X = 440         ## área de juego: x 440–1880
define MJ_AREA_Y = 112         ##                y 112–932
define MJ_AREA_W = 1440
define MJ_AREA_H = 820
define MJ_AREA_CX = 1160       ## centro horizontal del área (xpos + xanchor 0.5)
define MJ_AVISO_Y = 1000       ## centro vertical de la franja de avisos
define MJ_AVISO_ANCHO = 1200
define MJ_HUD_X = 40           ## bloque del HUD dentro de la columna
define MJ_HUD_Y = 116
define MJ_HUD_ANCHO = 320
define MJ_VELO = "#0B0712A6"   ## velo sobre el fondo del minijuego

## Botones: (ancho, alto, tamaño de letra) para cinta_boton.
define MJ_BOTON = {
    "primario":   (420, 80, 34),
    "secundario": (340, 64, 26),
    "pequeno":    (220, 56, 24),
}

## Acento de la píldora de aviso. "info" usa el color de la hermana.
define MJ_AVISO_ACENTO = {"bien": "#9AE6B4", "mal": "#FF8A8A"}

## --- Tipografía: dos familias, un tamaño por nivel ---------------------------
## Shippori (gui.name_text_font): mayúsculas, cifras y botones.
## M PLUS Rounded (fuente por defecto): frases.

style mj_titulo is default:
    font gui.name_text_font
    size 40
    kerning 4
    color "#FFF8FC"

style mj_cifra_grande is default:
    font gui.name_text_font
    size 120
    color "#FFFFFF"
    outlines [(5, "#1B1026CC", 0, 0)]

style mj_cifra is default:
    font gui.name_text_font
    size 30
    color "#FFFFFF"
    outlines [(3, "#1B102699", 0, 0)]

style mj_etiqueta is default:
    font gui.name_text_font
    size 20
    kerning 3
    color "#E8E0F2"
    outlines [(3, "#1B102699", 0, 0)]

style mj_aviso_texto is default:
    size 34
    color "#F3EEFA"

style mj_globo_texto is default:
    size 28

style mj_cuerpo is default:
    size 24
    color "#E8E0F2"
    outlines [(3, "#1B102699", 0, 0)]

style mj_nota is default:
    size 18
    color "#CFC6E0"
    outlines [(3, "#1B102699", 0, 0)]

## --- Movimiento ------------------------------------------------------------------

transform mj_cinta_entrada:
    xoffset -800
    ease 0.35 xoffset 0

transform mj_aviso_anim:
    on appear, show:
        alpha 0.0
        yoffset 14
        ease 0.2 alpha 1.0 yoffset 0
    on hide:
        ease 0.25 alpha 0.0 yoffset 8


## Píldora de aviso, centrada en la franja fija bajo el área de juego.
## tipo: "bien" | "mal" | "info".
screen mj_aviso(texto, tipo, hermana):

    $ acento = PETALO_COLOR[hermana]
    if tipo in MJ_AVISO_ACENTO:
        $ acento = MJ_AVISO_ACENTO[tipo]

    frame:
        xpos MJ_AREA_CX
        ypos MJ_AVISO_Y
        xanchor 0.5
        yanchor 0.5
        xmaximum MJ_AVISO_ANCHO
        padding (40, 14, 40, 14)
        background Fixed(
            Transform(Frame("ui/opcion_neutra.png", 40, 40, 40, 40), matrixcolor=TintMatrix("#1B1026")),
            Transform(Frame("ui/opcion_marco.png", 40, 40, 40, 40), matrixcolor=TintMatrix(acento)))

        text texto:
            style "mj_aviso_texto"
            text_align 0.5
            xalign 0.5
            substitute False


## Una fila del HUD: etiqueta a la izquierda, cifra a la derecha.
screen mj_hud_fila(etiqueta, cifra, color_etiqueta="#E8E0F2"):

    fixed:
        xysize (MJ_HUD_ANCHO, 34)
        text etiqueta style "mj_etiqueta" color color_etiqueta xpos 0 yalign 0.5 substitute False
        if cifra != "":
            text cifra style "mj_cifra" xalign 1.0 yalign 0.5 substitute False


## MARCO COMÚN. Uso:  use mj_marco(...):  <contenido del área de juego>
## La screen llamadora declara `modal True` y `zorder 95`; los `key` se tragan
## rollback y skip. Los argumentos posicionales son los de siempre; `fallos`
## se acepta por compatibilidad y no se dibuja (vale intento - 1).
##   tiempo/tiempo_total  → barra de recurso (recurso_txt, recurso_unidad)
##   vidas/vidas_max      → iconos de su motivo (vidas_txt encima)
##   chibi/globo/anim     → chibi general a 1.0 en la columna (mj_retrato)
##   aviso/aviso_tipo     → píldora en la franja fija ("" = sin aviso; al
##                          vaciarse, sale con el último texto)
screen mj_marco(hermana, titulo, intento=1, fallos=0, nivel="dificil", progreso=0, total=1, tiempo=None, tiempo_total=None, unidad="ACIERTOS", recurso_txt="TIEMPO", recurso_unidad=" s", vidas=None, vidas_max=0, vidas_txt="", chibi=None, globo=None, anim="quieto", aviso="", aviso_tipo="info"):

    default aviso_ultimo = ""
    default tipo_ultimo = "info"
    if aviso != "":
        $ aviso_ultimo = aviso
        $ tipo_ultimo = aviso_tipo

    $ color = PETALO_COLOR[hermana]
    $ cinta = ui_mezclar(color, "#FFFFFF", 0.35)
    $ tinta = ui_mezclar(color, "#000000", 0.75)

    key "rollback" action NullAction()
    key "rollforward" action NullAction()
    key "skip" action NullAction()
    key "toggle_skip" action NullAction()
    key "fast_skip" action NullAction()

    add Solid(MJ_VELO)

    ## --- La columna de la hermana ---
    add "ui/mj_columna.png" xpos 0 ypos 0
    add "ui/mj_columna_banda.png" xpos 0 ypos 0 matrixcolor TintMatrix(color)

    $ etiqueta = "MINIJUEGO"
    if nivel == "asistida":
        $ etiqueta = "MINIJUEGO · ASISTENCIA"
    use hud_cinta_vista(titulo, etiqueta, hermana, cinta, tinta, mj_cinta_entrada)

    ## --- HUD: intento → vidas → recurso → progreso ---
    vbox:
        xpos MJ_HUD_X
        ypos MJ_HUD_Y
        xsize MJ_HUD_ANCHO
        spacing 12

        use mj_hud_fila("INTENTO", str(intento))

        if vidas is not None:
            vbox:
                spacing 6
                if vidas_txt != "":
                    text vidas_txt style "mj_etiqueta" substitute False
                hbox:
                    spacing 4
                    for k in range(vidas_max):
                        if k < vidas:
                            add Transform("ui/hud_icono_" + hermana + ".png", zoom=0.8, matrixcolor=TintMatrix(color))
                        else:
                            add Transform("ui/hud_icono_" + hermana + ".png", zoom=0.8, matrixcolor=TintMatrix("#FFFFFF"), alpha=0.2)

        if tiempo is not None and tiempo_total is not None:
            $ col_recurso = "#FFE3A0"
            if tiempo < 0.25 * tiempo_total:
                $ col_recurso = "#FF8A8A"
            $ cifra_recurso = str(int(tiempo + 0.999)) + recurso_unidad
            vbox:
                spacing 6
                use mj_hud_fila(recurso_txt, cifra_recurso)
                use barra_progreso(tiempo, tiempo_total, col_recurso, MJ_HUD_ANCHO)

        vbox:
            spacing 6
            use mj_hud_fila(unidad, str(progreso) + " / " + str(total))
            use barra_progreso(progreso, total, color, MJ_HUD_ANCHO)

    ## --- Área de juego ---
    transclude

    ## --- Chibi general y su globo (encima del área, dentro de la columna) ---
    if chibi is not None:
        use mj_retrato(hermana, chibi, globo, anim)

    ## --- Aviso: franja fija bajo el área de juego ---
    showif aviso != "":
        fixed:
            at mj_aviso_anim
            use mj_aviso(aviso_ultimo, tipo_ultimo, hermana)


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
    $ margen = int(params["fallos_max"]) + 1
    $ quedan = margen - vivo.fallos
    $ aviso = ""
    $ aviso_tipo = "info"
    if vivo.ultimo == "acierto":
        $ aviso = "¡Bien!"
        $ aviso_tipo = "bien"
    elif vivo.ultimo == "fallo":
        $ aviso = "Fallo"
        $ aviso_tipo = "mal"
    $ boton = MJ_BOTON["primario"]

    use mj_marco(hermana, titulo, intento, fallos, nivel, vivo.aciertos, vivo.necesarios, vidas=quedan, vidas_max=margen, vidas_txt="OPORTUNIDADES", aviso=aviso, aviso_tipo=aviso_tipo):

        text "Pulsa cuando la barra pase por la zona.":
            style "mj_cuerpo"
            xpos MJ_AREA_CX
            xanchor 0.5
            ypos 330

        fixed:
            xpos MJ_AREA_CX
            xanchor 0.5
            ypos 430
            xysize (ancho, 60)
            add Solid("#FFFFFF2A", xsize=ancho, ysize=40) yalign 0.5
            add Solid(color + "B0", xsize=zona_w, ysize=40) xpos zona_x yalign 0.5
            add Solid("#FFFFFF", xsize=8, ysize=60) xpos (marcador - 4)

        fixed:
            xpos MJ_AREA_CX
            xanchor 0.5
            ypos 600
            xysize (boton[0], boton[1])
            use cinta_boton("¡Ahora!", Function(vivo.pulsar), hermana, boton[0], boton[1], boton[2])


################################################################################
##  PARTE F · PRUEBA DEL MARCO
##  jump mj_probar_marco   (consola Shift+O). Abre el marco con cada hermana:
##  HUD completo, área de juego marcada, avisos, globo, reacciones y botones.
################################################################################

define MJ_PRUEBA_FONDO = {
    "ichika": "bg_sala_ensayo", "nino": "bg_centro_comercial", "miku": "bg_biblioteca",
    "yotsuba": "bg_pista_atletismo", "itsuki": "bg_aula_tarde",
}
define MJ_PRUEBA_UNIDAD = {
    "ichika": "LÍNEAS", "nino": "LISTAS", "miku": "NOTAS", "yotsuba": "TRAMOS", "itsuki": "PASOS",
}
## La línea de globo más larga de MJ_GLOBOS (la de Ichika): debe caber sobre la chibi sin pisar el HUD.
define MJ_PRUEBA_GLOBO_LARGO = "Me sé el guion. Falta saber cuál es el mío."
define MJ_PRUEBA_AVISO_LARGO = "Se cayó el testigo: Yotsuba vuelve a por él y el relevo sigue desde el último punto de control, sin perder los tramos ya corridos."

default mj_prueba_cola = []
default mj_prueba_h = "yotsuba"
default mj_prueba_quick = True

init python:

    class MJMarcoPrueba(object):
        """Estado de la pantalla de prueba del marco (no se guarda)."""
        def __init__(self, hermana):
            self.reloj = MJReloj()
            self.globo = MJGlobo(hermana)
            self.aviso = ""
            self.tipo = "info"
            self.aviso_t = 0.0
            self.anim = "quieto"
            self.anim_t = 0.0
            self.vidas = 3

        def tick(self):
            dt = self.reloj.avanzar()
            self.globo.avanzar(dt)
            if self.aviso_t > 0.0:
                self.aviso_t -= dt
                if self.aviso_t <= 0.0:
                    self.aviso = ""
            if self.anim_t > 0.0:
                self.anim_t -= dt
                if self.anim_t <= 0.0:
                    self.anim = "quieto"

        def avisar(self, texto, tipo, duracion=1.6):
            self.aviso = texto
            self.tipo = tipo
            self.aviso_t = duracion

        def reaccion(self, anim):
            self.anim = anim
            self.anim_t = 0.45

        def globo_largo(self, duracion=3.0):
            self.globo.poner(MJ_PRUEBA_GLOBO_LARGO, duracion)

        def vida(self, d):
            self.vidas += d
            if self.vidas < 0:
                self.vidas = 9
            if self.vidas > 9:
                self.vidas = 0


## fijo=True: globo largo y aviso largo sin caducar (para las capturas).
screen mj_marco_prueba(hermana, fijo=False):

    modal True
    zorder 95

    default p = MJMarcoPrueba(hermana)

    if fijo:
        on "show" action [Function(p.globo_largo, 999.0), Function(p.avisar, MJ_PRUEBA_AVISO_LARGO, "mal", 999.0)]

    timer 0.05 repeat True action Function(p.tick)

    $ juego = E6_MJ_JUEGO[hermana]
    $ titulo = MJ_REGISTRO[juego]["titulo"]
    $ sec = MJ_BOTON["secundario"]
    $ pri = MJ_BOTON["primario"]

    add MJ_PRUEBA_FONDO[hermana] fit "cover"

    use mj_marco(hermana, titulo, 2, 1, "asistida", 7, 28, 20.0, 80.0, MJ_PRUEBA_UNIDAD[hermana], vidas=p.vidas, vidas_max=9, vidas_txt="TESTIGOS", chibi="animo", globo=p.globo, anim=p.anim, aviso=p.aviso, aviso_tipo=p.tipo):

        ## Borde del área de juego (solo en la prueba).
        add Solid("#FFFFFF40", xsize=MJ_AREA_W, ysize=2) xpos MJ_AREA_X ypos MJ_AREA_Y
        add Solid("#FFFFFF40", xsize=MJ_AREA_W, ysize=2) xpos MJ_AREA_X ypos (MJ_AREA_Y + MJ_AREA_H - 2)
        add Solid("#FFFFFF40", xsize=2, ysize=MJ_AREA_H) xpos MJ_AREA_X ypos MJ_AREA_Y
        add Solid("#FFFFFF40", xsize=2, ysize=MJ_AREA_H) xpos (MJ_AREA_X + MJ_AREA_W - 2) ypos MJ_AREA_Y

        vbox:
            xpos MJ_AREA_CX
            xanchor 0.5
            ypos 160
            spacing 26

            text ("PRUEBA DEL MARCO · " + hermana.upper()):
                style "mj_titulo"
                xalign 0.5

            text "Cada botón dispara una pieza del marco. El rectángulo es el área de juego.":
                style "mj_cuerpo"
                xalign 0.5

            null height 10

            grid 3 3:
                xalign 0.5
                spacing 24
                use cinta_boton("Aviso: bien", Function(p.avisar, "¡Testigo recibido!", "bien"), hermana, sec[0], sec[1], sec[2])
                use cinta_boton("Aviso: fallo", Function(p.avisar, "Se cayó el testigo", "mal"), hermana, sec[0], sec[1], sec[2])
                use cinta_boton("Aviso: info", Function(p.avisar, "Mitad de la carrera", "info"), hermana, sec[0], sec[1], sec[2])
                use cinta_boton("Aviso largo", Function(p.avisar, MJ_PRUEBA_AVISO_LARGO, "mal", 3.0), hermana, sec[0], sec[1], sec[2])
                use cinta_boton("Globo largo", Function(p.globo_largo), hermana, sec[0], sec[1], sec[2])
                use cinta_boton("Globo corto", Function(p.globo.decir, "inicio", True), hermana, sec[0], sec[1], sec[2])
                use cinta_boton("Salto", Function(p.reaccion, "salto"), hermana, sec[0], sec[1], sec[2])
                use cinta_boton("Tiembla", Function(p.reaccion, "tiembla"), hermana, sec[0], sec[1], sec[2])
                use cinta_boton("Quitar vida", Function(p.vida, -1), hermana, sec[0], sec[1], sec[2])

            hbox:
                xalign 0.5
                spacing 24
                use cinta_boton("Deshabilitado", NullAction(), hermana, sec[0], sec[1], sec[2], False)
                use cinta_boton("Siguiente", Return(True), hermana, pri[0], pri[1], pri[2])


label mj_probar_marco:

    scene bg_negro
    $ mj_prueba_quick = quick_menu
    $ quick_menu = False

    menu:
        "Probar el marco común · ¿con qué hermana?"

        "Ichika":
            $ mj_prueba_cola = ["ichika"]
        "Nino":
            $ mj_prueba_cola = ["nino"]
        "Miku":
            $ mj_prueba_cola = ["miku"]
        "Yotsuba":
            $ mj_prueba_cola = ["yotsuba"]
        "Itsuki":
            $ mj_prueba_cola = ["itsuki"]
        "Las cinco seguidas":
            $ mj_prueba_cola = list(E6_ORDEN_CANON)
        "Volver":
            $ quick_menu = mj_prueba_quick
            return

    while len(mj_prueba_cola) > 0:
        $ mj_prueba_h = mj_prueba_cola.pop(0)
        call screen mj_marco_prueba(mj_prueba_h)

    $ quick_menu = mj_prueba_quick
    jump mj_probar_marco
