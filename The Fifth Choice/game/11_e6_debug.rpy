################################################################################
##  11_e6_debug.rpy — Menú de depuración del Evento 6 (solo desarrollo)
##  Entrada: consola (Shift+O):  jump e6_debug
##  Se puede borrar el archivo entero antes de publicar (e6_iniciar usa getattr).
################################################################################

default e6_dbg_ramas = {"ichika": "calida", "nino": "calida", "miku": "tibia", "yotsuba": None, "itsuki": None}
default e6_dbg_orden = ["ichika", "nino", "miku"]
default e6_dbg_preset = ("c", "c", "t")
default e6_dbg_idx = 0
default e6_dbg_beat = "tibia"
default e6_forzar_entrada = None
default e6_dbg_op = ""
default e6_dbg_sel = 0
default e6_dbg_err = ""
default e6_dbg_msg = ""

## Los 20 sobrevivientes (Anexo B): (rama en hub 1, hub 2, hub 3).
define E6_SOBREVIVIENTES = [
    ("Superado", [("f", "c", "c"), ("c", "f", "c"), ("f", "c", "t"), ("f", "t", "c"),
                  ("c", "f", "t"), ("t", "f", "c"), ("f", "t", "t"), ("t", "f", "t")]),
    ("Mixto",    [("c", "t", "t"), ("t", "c", "t"), ("t", "t", "c"), ("t", "t", "t"),
                  ("c", "c", "f"), ("c", "t", "f"), ("t", "c", "f"), ("t", "t", "f")]),
    ("Bueno",    [("c", "c", "c"), ("c", "c", "t"), ("c", "t", "c"), ("t", "c", "c")]),
]

init python:

    from itertools import combinations

    E6_DBG_TRIOS = list(combinations(["ichika", "nino", "miku", "yotsuba", "itsuki"], 3))
    E6_DBG_RAMA = {"c": "calida", "t": "tibia", "f": "fria"}
    E6_DBG_CICLO = [None, "calida", "tibia", "fria"]
    E6_DBG_ENTRADAS = [None, "superado", "mixto", "bueno"]
    E6_DBG_BEATS = ["calida", "tibia", "fria"]
    E6_DBG_MODOS = ["normal", "asistido", "saltar"]

    def e6_dbg_resumen():
        partes = []
        for h in E6_ORDEN_CANON:
            r = store.e6_dbg_ramas[h]
            if r is None:
                r = "-"
            partes.append(h.capitalize() + " " + r)
        nombres = []
        for h in store.e6_dbg_orden:
            nombres.append(h.capitalize())
        forzada = store.e6_forzar_entrada
        if forzada is None:
            forzada = "auto"
        return ("Orden de hubs: " + ", ".join(nombres) + ". Ramas: " + " · ".join(partes)
                + ". Beat de Nino: " + store.e6_dbg_beat + ". Entrada: " + forzada
                + ". Minijuegos: " + persistent.mj_modo + ".")

    def e6_dbg_validar():
        ramas = store.e6_dbg_ramas
        visitadas = 0
        frias = 0
        for h in E6_ORDEN_CANON:
            if ramas[h] is not None:
                visitadas += 1
                if ramas[h] == "fria":
                    frias += 1
        if visitadas != 3:
            return "Debe haber exactamente 3 hermanas visitadas (hay " + str(visitadas) + ")."
        if frias > 1:
            return "Máximo 1 hermana fría (dos frías terminan en despido)."
        return ""

    def e6_dbg_aplicar_preset(preset, trio):
        ramas = {}
        for h in E6_ORDEN_CANON:
            ramas[h] = None
        for i in range(3):
            ramas[trio[i]] = E6_DBG_RAMA[preset[i]]
        store.e6_dbg_ramas = ramas
        store.e6_dbg_orden = list(trio)
        store.e6_dbg_preset = preset

    def e6_dbg_siguiente_trio():
        store.e6_dbg_idx = (store.e6_dbg_idx + 1) % len(E6_DBG_TRIOS)
        e6_dbg_aplicar_preset(store.e6_dbg_preset, E6_DBG_TRIOS[store.e6_dbg_idx])

    def e6_dbg_ciclar(h):
        actual = store.e6_dbg_ramas[h]
        i = (E6_DBG_CICLO.index(actual) + 1) % len(E6_DBG_CICLO)
        store.e6_dbg_ramas[h] = E6_DBG_CICLO[i]

    def e6_dbg_ciclar_beat():
        i = (E6_DBG_BEATS.index(store.e6_dbg_beat) + 1) % len(E6_DBG_BEATS)
        store.e6_dbg_beat = E6_DBG_BEATS[i]

    def e6_dbg_ciclar_entrada():
        i = (E6_DBG_ENTRADAS.index(store.e6_forzar_entrada) + 1) % len(E6_DBG_ENTRADAS)
        store.e6_forzar_entrada = E6_DBG_ENTRADAS[i]

    def e6_dbg_ciclar_modo():
        i = (E6_DBG_MODOS.index(persistent.mj_modo) + 1) % len(E6_DBG_MODOS)
        persistent.mj_modo = E6_DBG_MODOS[i]

    def e6_dbg_borrar_flags():
        for h in E6_ORDEN_CANON:
            setattr(persistent, "e6_mj_ganado_" + h, False)

    def e6_dbg_aplicar():
        """Escribe en el store lo mismo que habrían dejado los hubs, el beat y la interconexión 6."""
        ramas = store.e6_dbg_ramas
        orden = []
        for h in store.e6_dbg_orden:
            if ramas[h] is not None:
                orden.append(h)
        for h in E6_ORDEN_CANON:
            if ramas[h] is not None and h not in orden:
                orden.append(h)
        frias_total = 0
        frias_hubs12 = 0
        calidas = 0
        for i in range(3):
            r = ramas[orden[i]]
            if r == "fria":
                frias_total += 1
                if i < 2:
                    frias_hubs12 += 1
            if r == "calida":
                calidas += 1
        for h in E6_ORDEN_CANON:
            setattr(store, h + "_rama_cap1", ramas[h])
            setattr(store, h + "_visitada_cap1", ramas[h] is not None)
        store.hub_visitadas = list(orden)
        store.desaires_cap1 = frias_total
        store.maruo_ultimatum = (frias_hubs12 == 1)
        store.despido_cap1 = False
        store.despido_en_beat = False
        store.nino_rama_beat = store.e6_dbg_beat
        store.ui_prologo = False
        store.tiempo_restante = "pocos días"
        if frias_total == 0 and calidas >= 2:
            store.clima_cap1 = "buena"
        else:
            store.clima_cap1 = "mixta"

    def e6_dbg_items_principal():
        nombres = []
        for h in store.e6_dbg_orden:
            nombres.append(h.capitalize())
        return [
            ("Trío de hubs: " + ", ".join(nombres) + " (cambiar)", "trio"),
            ("Cargar preset de sobreviviente…", "preset"),
            ("Editar ramas a mano…", "manual"),
            ("Ajustes (beat de Nino, entrada, minijuegos)…", "ajustes"),
            ("Probar el minijuego de prueba", "probar"),
            (">> Jugar Evento 6", "jugar"),
            ("Salir", "salir"),
        ]

    def e6_dbg_items_grupos():
        items = []
        for i in range(len(E6_SOBREVIVIENTES)):
            g = E6_SOBREVIVIENTES[i]
            items.append((g[0] + " (" + str(len(g[1])) + ")", i))
        items.append(("Volver", -1))
        return items

    def e6_dbg_items_presets(g):
        items = []
        lista = E6_SOBREVIVIENTES[g][1]
        for i in range(len(lista)):
            p = lista[i]
            items.append(("(" + p[0] + ", " + p[1] + ", " + p[2] + ")  ·  " + str(p.count("c")) + " cálidas", i))
        items.append(("Volver", -1))
        return items

    def e6_dbg_items_manual():
        items = []
        for h in E6_ORDEN_CANON:
            r = store.e6_dbg_ramas[h]
            if r is None:
                r = "no visitada"
            items.append((h.capitalize() + ": " + r, h))
        items.append(("Listo (validar)", "listo"))
        items.append(("Volver", "cancelar"))
        return items

    def e6_dbg_fijar_orden_manual():
        orden = []
        for h in E6_ORDEN_CANON:
            if store.e6_dbg_ramas[h] is not None:
                orden.append(h)
        store.e6_dbg_orden = orden

    def e6_dbg_items_ajustes():
        entrada = store.e6_forzar_entrada
        if entrada is None:
            entrada = "auto"
        return [
            ("nino_rama_beat: " + store.e6_dbg_beat + " (cambiar)", "beat"),
            ("Entrada forzada: " + entrada + " (cambiar)", "entrada"),
            ("Modo de minijuegos: " + persistent.mj_modo + " (cambiar)", "modo"),
            ("Borrar flags persistent de minijuegos", "borrar"),
            ("Volver", "volver"),
        ]

    def e6_dbg_items_hermanas():
        items = []
        for h in E6_ORDEN_CANON:
            items.append((h.capitalize(), h))
        items.append(("Volver", "volver"))
        return items

    def e6_dbg_texto_resultado(h, resultado):
        r = store.e6_mj[h]
        return ("Resultado: " + str(resultado) + " · intentos " + str(r["intentos"])
                + " · fallos " + str(r["fallos"]) + " · nivel " + r["nivel"]
                + " · boost " + str(r["boost"]))


label e6_debug:

    scene bg_negro
    $ quick_menu = False
    $ ui_escena("normal")

label e6_debug_menu:

    $ narrator(e6_dbg_resumen(), interact=False)
    $ e6_dbg_op = renpy.display_menu(e6_dbg_items_principal())

    if e6_dbg_op == "trio":
        $ e6_dbg_siguiente_trio()
        jump e6_debug_menu

    if e6_dbg_op == "preset":
        call e6_debug_preset
        jump e6_debug_menu

    if e6_dbg_op == "manual":
        call e6_debug_manual
        jump e6_debug_menu

    if e6_dbg_op == "ajustes":
        call e6_debug_ajustes
        jump e6_debug_menu

    if e6_dbg_op == "probar":
        call e6_debug_probar
        jump e6_debug_menu

    if e6_dbg_op == "jugar":
        $ e6_dbg_err = e6_dbg_validar()
        if e6_dbg_err != "":
            $ narrator("No se puede jugar: " + e6_dbg_err)
            jump e6_debug_menu
        $ e6_dbg_aplicar()
        $ quick_menu = True
        jump evento_6

    $ quick_menu = True
    return


label e6_debug_preset:

    $ narrator("Grupo de estado de entrada", interact=False)
    $ e6_dbg_sel = renpy.display_menu(e6_dbg_items_grupos())
    if e6_dbg_sel < 0:
        return

    $ e6_dbg_idx_grupo = e6_dbg_sel
    $ narrator("Rama en hub 1, hub 2 y hub 3", interact=False)
    $ e6_dbg_sel = renpy.display_menu(e6_dbg_items_presets(e6_dbg_idx_grupo))
    if e6_dbg_sel < 0:
        return

    $ e6_dbg_aplicar_preset(E6_SOBREVIVIENTES[e6_dbg_idx_grupo][1][e6_dbg_sel], store.e6_dbg_orden)
    return


label e6_debug_manual:

    $ narrator("Toca una hermana para cambiar su estado (no visitada, calida, tibia, fria).", interact=False)
    $ e6_dbg_op = renpy.display_menu(e6_dbg_items_manual())

    if e6_dbg_op == "cancelar":
        return

    if e6_dbg_op == "listo":
        $ e6_dbg_err = e6_dbg_validar()
        if e6_dbg_err != "":
            $ narrator("Inválido: " + e6_dbg_err)
            jump e6_debug_manual
        $ e6_dbg_fijar_orden_manual()
        return

    $ e6_dbg_ciclar(e6_dbg_op)
    jump e6_debug_manual


label e6_debug_ajustes:

    $ narrator(e6_dbg_resumen(), interact=False)
    $ e6_dbg_op = renpy.display_menu(e6_dbg_items_ajustes())

    if e6_dbg_op == "volver":
        return

    if e6_dbg_op == "beat":
        $ e6_dbg_ciclar_beat()

    if e6_dbg_op == "entrada":
        $ e6_dbg_ciclar_entrada()

    if e6_dbg_op == "modo":
        $ e6_dbg_ciclar_modo()

    if e6_dbg_op == "borrar":
        $ e6_dbg_borrar_flags()

    jump e6_debug_ajustes


label e6_debug_probar:

    $ narrator("Hermana para el minijuego de prueba", interact=False)
    $ e6_dbg_op = renpy.display_menu(e6_dbg_items_hermanas())
    if e6_dbg_op == "volver":
        return

    $ e6_estado = {}
    $ e6_mj = {}
    $ nino_rama_beat = e6_dbg_beat
    $ e6_dbg_h = e6_dbg_op

    call mj_ejecutar("prueba", e6_dbg_h)

    $ e6_dbg_msg = e6_dbg_texto_resultado(e6_dbg_h, _return)
    $ narrator(e6_dbg_msg)
    return