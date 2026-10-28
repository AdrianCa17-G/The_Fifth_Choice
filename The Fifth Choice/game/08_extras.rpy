################################################################################
## 08_extras.rpy — Galería y Finales
################################################################################

default persistent.final_malo_temprano_visto = False
default persistent.final_malo_temprano_a_visto = False
default persistent.final_malo_temprano_b_visto = False

## --- DATOS: al añadir CG nuevos, agrégalos aquí (el % se recalcula solo) ---
## (clave, título de la pestaña, hermana o None, [(imagen, nombre), ...])
define GALERIA = [
    ("prologo", "Prólogo", None, [
        ("cg_familia", "Retrato familiar"),
        ("cg_calificacion", "La calificación"),
        ("cg_examen", "El examen"),
        ("cg_manija_edificio", "La manija"),
        ("cg_maruo_reunion", "El contrato"),
        ("cg_hermanas_estudiando", "La primera clase"),
    ]),
    ("cap1", "Capítulo 1", None, [
        ("cg_cinco_sentadas", "Cinco sentadas"),
        ("cg_libreta", "La libreta"),
        ("cg_cinco_estudiando", "Mesa de estudio"),
        ("cg_cinco_repasando", "Repaso final"),
        ("cg_raiha_correccion", "Raiha corrige"),
        ("cg_maruo_espaldas", "Dándome la espalda"),
    ]),
    ("ichika", "Ichika", "ichika", [
        ("cg_ichika_puerta", "Bienvenido"),
        ("cg_ichika_ensayo", "Sala de ensayo"),
        ("cg_ichika_desarmada", "Sin máscara"),
        ("cg_ichika_mascara", "La máscara"),
        ("cg_ichika_fracaso", "La función"),
    ]),
    ("nino", "Nino", "nino", [
        ("cg_nino_pasillo", "Ni una semana"),
        ("cg_nino_centro_comercial", "Harina"),
        ("cg_nino_receta", "La receta"),
        ("cg_nino_llamada", "La llamada"),
        ("cg_nino_confrontacion_cocina", "La discusión"),
        ("cg_nino_grieta_cocina", "La grieta"),
        ("cg_nino_fracaso", "Revisando"),
    ]),
    ("miku", "Miku", "miku", [
        ("cg_miku_sofa", "Logística"),
        ("cg_miku_biblioteca", "Biblioteca"),
        ("cg_miku_estudio", "El temario"),
        ("cg_miku_sorpresa", "Sorpresa"),
        ("cg_miku_fracaso", "La goma"),
    ]),
    ("yotsuba", "Yotsuba", "yotsuba", [
        ("cg_yotsuba_corriendo", "Bienvenido"),
        ("cg_yotsuba_pista", "Vuelta veinte"),
        ("cg_yotsuba_rotulador", "El rotulador"),
        ("cg_yotsuba_cronometro", "Una vuelta más"),
        ("cg_yotsuba_fracaso", "Mirando a las demás"),
    ]),
    ("itsuki", "Itsuki", "itsuki", [
        ("cg_itsuki_sentada", "Mi asiento"),
        ("cg_itsuki_azotea", "Tregua"),
        ("cg_itsuki_discusion", "Quién eres"),
        ("cg_itsuki_apertura", "Primera hora"),
        ("cg_itsuki_azotea_cuaderno", "El cuaderno"),
        ("cg_itsuki_azotea_manos", "Manos quietas"),
        ("cg_itsuki_atascada", "Atascada"),
        ("cg_itsuki_contraida", "Encogida"),
        ("cg_itsuki_reto", "La mirada"),
        ("cg_itsuki_fracaso", "El mismo error"),
    ]),
]

define FINALES_PISTAS = {
    "ichika":  "A veces, quien más sonríe es quien más necesita que te quedes a su lado.",
    "nino":    "Quien más distancia pone, en el fondo solo espera a alguien que no se rinda con ella.",
    "miku":    "Aprende a escuchar sus silencios... es ahí donde guarda lo que de verdad siente.",
    "yotsuba": "Hazle recordar la luz tan hermosa que tiene, incluso cuando ella no pueda verla.",
    "itsuki":  "Sostén su mano cuando lo necesite, pero déjala sentir que camina por sí misma.",
}

## (clave, título, pista, color)
define FINALES_ESPECIALES = [
    ("temprano", "Despido temprano", "Decir que no cada vez que pudiste decir que sí.", "#9AA7A8"),
    ("malo", "Despedida", "Estar cerca de todas, y no llegar a ninguna.", "#C0504D"),
    ("secreto", "Final secreto", "Cinco caminos, un solo estudiante completo.", "#F4D03F"),
]

## Pon True cuando existan los extras "Después de la boda".
define EXTRAS_DISPONIBLES = False


define FINALES_TEMPRANO = [
    {
        "clave": "a",
        "titulo": "El portazo",
        "resumen": "En la cocina. Maruo corta el contrato antes de que nadie pueda despedirse.",
        "pista": "Cuando la paciencia de Maruo se acaba pronto.",
        "label": "final_malo_beat",
        "scope": {
            "despido_en_beat": True,
            "ui_prologo": False,
            "hub_visitadas": ["yotsuba", "itsuki"],
            "yotsuba_rama_cap1": "fria",
            "itsuki_rama_cap1": "fria",
        },
    },
    {
        "clave": "b",
        "titulo": "La despedida",
        "resumen": "Tras la semana de exámenes. Cuatro reprueban y cada una dice lo que le faltaba decir.",
        "pista": "Cuando la última oportunidad tampoco alcanza.",
        "label": "final_malo_hub3",
        "scope": {
            "despido_en_beat": False,
            "ui_prologo": False,
            "maruo_ultimatum": True,
            "despido_cap1": True,
            "hub_visitadas": ["ichika", "miku", "itsuki"],
            "ichika_rama_cap1": "calida",
            "miku_rama_cap1": "fria",
            "itsuki_rama_cap1": "fria",
        },
    },
]


init python:

    def galeria_seccion(clave):
        for s in GALERIA:
            if s[0] == clave:
                return s
        return GALERIA[0]

    def galeria_conteo(clave):
        s = galeria_seccion(clave)
        vistos = 0
        for item in s[3]:
            if renpy.seen_image(item[0]):
                vistos = vistos + 1
        return (vistos, len(s[3]))

    def galeria_total():
        vistos = 0
        total = 0
        for s in GALERIA:
            c = galeria_conteo(s[0])
            vistos = vistos + c[0]
            total = total + c[1]
        return (vistos, total)

    def galeria_completa(clave):
        c = galeria_conteo(clave)
        return c[1] > 0 and c[0] == c[1]

    def final_logrado(clave):
        if clave == "temprano":
            return bool(persistent.final_malo_temprano_visto)
        if clave == "malo":
            return bool(persistent.final_malo_visto)
        if clave == "secreto":
            return bool(persistent.final_secreto_desbloqueado)
        return bool(getattr(persistent, "ruta_" + clave + "_completa", False))

    def finales_conseguidos():
        cuenta = 0
        for clave in ["ichika", "nino", "miku", "yotsuba", "itsuki", "temprano", "malo", "secreto"]:
            if final_logrado(clave):
                cuenta = cuenta + 1
        return cuenta

    def final_sprite(hermana, logrado):
        base = Crop((90, 0, 580, 560), hermana + " neutral")
        if logrado:
            return Transform(base, zoom=0.55)
        return Transform(base, zoom=0.55, matrixcolor=TintMatrix("#0B0712"), alpha=0.85)

    def ui_cinta_menu(color, icono, activa):
        """Fondo de una cinta del menú (reposo o activa). icono=None -> solo borde."""
        oscuro = ui_mezclar(color, "#000000", 0.72)
        claro = ui_mezclar(color, "#FFFFFF", 0.35)
        if activa:
            capas = [
                Transform("ui/menu_cinta.png", matrixcolor=TintMatrix(claro)),
                Transform("ui/menu_cinta_borde.png", matrixcolor=TintMatrix("#FFFFFF")),
            ]
            if icono is not None:
                capas.append(Transform("ui/hud_icono_" + icono + ".png", matrixcolor=TintMatrix(oscuro), xpos=52, yalign=0.5))
        else:
            capas = [
                Transform("ui/menu_cinta.png", matrixcolor=TintMatrix("#1B1026"), alpha=0.80),
                Transform("ui/menu_cinta_borde.png", matrixcolor=TintMatrix(color)),
            ]
            if icono is not None:
                capas.append(Transform("ui/hud_icono_" + icono + ".png", matrixcolor=TintMatrix(color), xpos=52, yalign=0.5))
        return Fixed(*capas)

    def final_label(clave):
        """Label que reproduce ese final, o None si todavía no existe."""
        if clave == "temprano":
            return None
        nombre = "final_" + clave
        if renpy.has_label(nombre):
            return nombre
        return None

    def final_replay_ok(clave):
        """True si el final está conseguido y se puede revivir."""
        if not final_logrado(clave):
            return False
        if clave == "temprano":
            return True
        return final_label(clave) is not None

    def temprano_visto(version):
        return bool(getattr(persistent, "final_malo_temprano_" + version + "_visto", False))

    def temprano_versiones():
        cuenta = 0
        if temprano_visto("a"):
            cuenta = cuenta + 1
        if temprano_visto("b"):
            cuenta = cuenta + 1
        return cuenta

    ## Puente de una sola vez: tu persistent actual solo sabe que viste "algún"
    ## final temprano, no cuál. Desbloquea las dos versiones para poder probar.
    ## Bórralo cuando termines de experimentar.
    if persistent.final_malo_temprano_visto:
        if not persistent.final_malo_temprano_a_visto and not persistent.final_malo_temprano_b_visto:
            persistent.final_malo_temprano_a_visto = True
            persistent.final_malo_temprano_b_visto = True


    def final_scope(base):
        """Copia el scope de un replay y le añade el nombre que eligió el jugador."""
        scope = dict(base)
        if persistent.nombre_jugador:
            scope["nombre_jugador"] = persistent.nombre_jugador
        return scope


## --- Piezas comunes ---------------------------------------------------------

screen barra_progreso(vistos, total, color, ancho):

    $ lleno = 0
    if total > 0:
        $ lleno = int(ancho * vistos / float(total))

    fixed:
        xysize (ancho, 12)
        add Solid("#FFFFFF2A")
        if lleno > 0:
            add Solid(color, xsize=lleno, ysize=12)


screen barra_arcoiris(vistos, total, ancho):

    $ porcentaje = 0.0
    if total > 0:
        $ porcentaje = 100.0 * vistos / total
    $ segmento = (ancho - 4 * 6) // 5

    hbox:
        spacing 6

        for k in range(5):

            $ color_k = PETALO_COLOR[PETALO_ORDEN[k]]
            $ parte = (porcentaje - 20.0 * k) / 20.0
            if parte < 0.0:
                $ parte = 0.0
            if parte > 1.0:
                $ parte = 1.0
            $ lleno = int(segmento * parte)

            fixed:
                xysize (segmento, 12)
                add Solid("#FFFFFF2A")
                if lleno > 0:
                    add Solid(color_k, xsize=lleno, ysize=12)


screen cinta_volver():

    button:
        xpos 70
        ypos 940
        xysize (440, 68)
        action Return()
        hover_sound audio.sfx_hover
        activate_sound audio.sfx_click
        background ui_cinta_menu("#E8E0F2", "flor", False)
        hover_background ui_cinta_menu("#E8E0F2", "flor", True)
        at boton_slide

        text "Volver":
            xpos 112
            yalign 0.5
            font gui.name_text_font
            size 33
            kerning 2
            color "#F2EDF5"
            hover_color "#2B1B3F"

    key "game_menu" action Return()


## --- GALERÍA ------------------------------------------------------------------

screen galeria():
    tag menu

    default seccion = "prologo"
    default pagina = 0

    $ sec = galeria_seccion(seccion)
    $ items = sec[3]
    $ color_sec = "#E8E0F2"
    $ ico_sec = "flor"
    if sec[2] is not None:
        $ ico_sec = sec[2]
    $ osc_sec = ui_mezclar(color_sec, "#000000", 0.72)
    if sec[2] is not None:
        $ color_sec = PETALO_COLOR[sec[2]]
    $ conteo = galeria_conteo(seccion)
    $ total = galeria_total()
    $ paginas = (len(items) + 8) // 9
    $ visibles = items[pagina * 9:pagina * 9 + 9]
    $ titulo_sec = sec[1].upper()
    $ pct_total = 0
    if total[1] > 0:
        $ pct_total = int(round(100.0 * total[0] / total[1]))
    $ pct_sec = 0
    if conteo[1] > 0:
        $ pct_sec = int(round(100.0 * conteo[0] / conteo[1]))

    add "main_menu_bg" fit "cover"
    add Solid("#120A1CCC")
    add "ui/menu_panel.png"

    text "GALERÍA" xpos 70 ypos 48 font gui.name_text_font size 60 kerning 8 color "#FFF8FC" outlines [(5, "#1B1026CC", 0, 0)]

    ## --- Pestañas ---
    vbox:
        xpos 70
        ypos 175
        spacing 35

        for s in GALERIA:

            $ c = galeria_conteo(s[0])
            $ col = "#E8E0F2"
            $ ico = "flor"
            if s[2] is not None:
                $ col = PETALO_COLOR[s[2]]
                $ ico = s[2]
            $ osc = ui_mezclar(col, "#000000", 0.72)

            button:
                xysize (440, 68)
                action [SetScreenVariable("seccion", s[0]), SetScreenVariable("pagina", 0)]
                selected (seccion == s[0])
                hover_sound audio.sfx_hover
                activate_sound audio.sfx_click
                background ui_cinta_menu(col, ico, False)
                hover_background ui_cinta_menu(col, ico, True)
                selected_background ui_cinta_menu(col, ico, True)
                at boton_slide

                text s[1]:
                    xpos 112
                    yalign 0.5
                    font gui.name_text_font
                    size 30
                    kerning 2
                    color "#F2EDF5"
                    hover_color osc
                    selected_color osc

                text (str(c[0]) + "/" + str(c[1])):
                    xalign 0.93
                    yalign 0.5
                    size 24
                    color "#F2EDF5"
                    hover_color osc
                    selected_color osc

    ## --- Progreso total ---
    vbox:
        xpos 862
        ypos 56
        spacing 10
        text ("CG DESBLOQUEADOS   " + str(total[0]) + " / " + str(total[1]) + "   ·   " + str(pct_total) + " %") font gui.name_text_font size 26 kerning 3 color "#FFF8FC"
        use barra_arcoiris(total[0], total[1], 1006)

    ## --- Sección actual ---
    vbox:
        xpos 862
        ypos 150
        spacing 10
        text (titulo_sec + "   " + str(conteo[0]) + " / " + str(conteo[1]) + "   ·   " + str(pct_sec) + " %") font gui.name_text_font size 30 kerning 3 color color_sec
        use barra_progreso(conteo[0], conteo[1], color_sec, 1006)

    ## --- Cuadrícula 3x3 ---
    vbox:
        xpos 862
        ypos 262
        spacing 52

        for fila in range(3):
            hbox:
                spacing 20

                for col_n in range(3):

                    $ idx = fila * 3 + col_n

                    if idx >= len(visibles):

                        null width 322 height 181

                    else:

                        $ nombre_img = visibles[idx][0]
                        $ rotulo = visibles[idx][1]

                        if renpy.seen_image(nombre_img):

                            button:
                                xysize (322, 181)
                                background None
                                action Show("visor_cg", img=nombre_img, rotulo=rotulo)
                                hover_sound audio.sfx_hover
                                activate_sound audio.sfx_click
                                at tarjeta_hover

                                add Transform(nombre_img, xysize=(322, 181), fit="cover")
                                add "ui/gal_marco.png" matrixcolor TintMatrix(color_sec)
                                text rotulo xalign 0.5 yalign 0.94 size 20 color "#FFFFFF" outlines [(3, "#000000AA", 0, 0)]

                        else:

                            fixed:
                                xysize (322, 181)
                                add "ui/gal_bloqueo.png"
                                add "ui/flor.png" matrixcolor TintMatrix("#FFFFFF") alpha 0.22 zoom 1.5 align (0.5, 0.42)
                                text "???" xalign 0.5 yalign 0.86 size 22 color "#FFFFFF66"

    ## --- Paginación ---
    if paginas > 1:

        fixed:
            xpos 862
            ypos 944
            xysize (1006, 52)

            hbox:
                xalign 0.5
                yalign 0.5
                spacing 14

                textbutton "<":
                    yalign 0.5
                    action SetScreenVariable("pagina", pagina - 1)
                    sensitive (pagina > 0)
                    hover_sound audio.sfx_hover
                    text_size 34
                    text_idle_color color_sec
                    text_hover_color "#FFFFFF"
                    text_insensitive_color "#FFFFFF33"

                for p in range(paginas):

                    button:
                        xysize (46, 46)
                        yalign 0.5
                        action SetScreenVariable("pagina", p)
                        hover_sound audio.sfx_hover
                        background Transform("ui/hud_icono_" + ico_sec + ".png", matrixcolor=TintMatrix(color_sec), alpha=0.40, zoom=1.15, align=(0.5, 0.5))
                        hover_background Transform("ui/hud_icono_" + ico_sec + ".png", matrixcolor=TintMatrix(color_sec), alpha=0.85, zoom=1.15, align=(0.5, 0.5))
                        selected_background Transform("ui/hud_icono_" + ico_sec + ".png", matrixcolor=TintMatrix(color_sec), alpha=1.0, zoom=1.15, align=(0.5, 0.5))

                        text str(p + 1):
                            xalign 0.5
                            yalign 0.5
                            size 20
                            color "#FFFFFF"
                            hover_color osc_sec
                            selected_color osc_sec
                            outlines [(2, "#00000066", 0, 0)]

                textbutton ">":
                    yalign 0.5
                    action SetScreenVariable("pagina", pagina + 1)
                    sensitive (pagina < paginas - 1)
                    hover_sound audio.sfx_hover
                    text_size 34
                    text_idle_color color_sec
                    text_hover_color "#FFFFFF"
                    text_insensitive_color "#FFFFFF33"


    use cinta_volver


screen visor_cg(img, rotulo):

    modal True
    zorder 300

    add Solid("#000000F2")
    add Transform(img, xysize=(1920, 1080), fit="contain")
    text rotulo xalign 0.5 yalign 0.975 size 28 color "#FFFFFF" outlines [(4, "#000000CC", 0, 0)]

    button:
        xysize (1920, 1080)
        background None
        action Hide("visor_cg")

    key "dismiss" action Hide("visor_cg")
    key "game_menu" action Hide("visor_cg")


## --- FINALES ------------------------------------------------------------------

screen finales():
    tag menu

    $ hechos = finales_conseguidos()
    $ pct = int(round(100.0 * hechos / 8))

    add "main_menu_bg" fit "cover"
    add Solid("#120A1CD8")
    add "sakura_petals"

    text "FINALES" xpos 88 ypos 20 font gui.name_text_font size 60 kerning 8 color "#FFF8FC" outlines [(5, "#1B1026CC", 0, 0)]

    vbox:
        xpos 980
        ypos 56
        spacing 10
        text ("FINALES DESCUBIERTOS   " + str(hechos) + " / 8   ·   " + str(pct) + " %") font gui.name_text_font size 26 kerning 3 color "#FFF8FC"
        use barra_arcoiris(hechos, 8, 860)


## --- Los cinco finales románticos ---
    hbox:
        xalign 0.5
        ypos 132
        spacing 28

        for h in ["ichika", "nino", "miku", "yotsuba", "itsuki"]:

            $ nombre = h.capitalize()
            $ color_h = PETALO_COLOR[h]
            $ claro_h = ui_mezclar(color_h, "#FFFFFF", 0.25)
            $ tono_h = TARJETA_TONO[h]
            $ logrado = final_logrado(h)
            $ extra_ok = galeria_completa(h)
            $ cg = galeria_conteo(h)
            $ jugable = final_replay_ok(h)

            $ borde_h = "#6E6680"
            $ titulo_f = "???"
            $ sub_f = FINALES_PISTAS[h]
            if logrado:
                $ borde_h = color_h
                $ titulo_f = "Final de " + nombre
                $ sub_f = "Final romántico conseguido"
                if jugable:
                    $ sub_f = "Final romántico conseguido\nClic para revivirlo"

            $ chip_fondo = "#2A2236"
            $ chip_borde = "#6E6680"
            $ chip_texto = "EXTRA  ·  Galería " + str(cg[0]) + "/" + str(cg[1])
            if extra_ok:
                $ chip_fondo = tono_h
                $ chip_borde = color_h
                $ chip_texto = "EXTRA  ·  Próximamente"

            $ chip_activo = extra_ok and EXTRAS_DISPONIBLES

            vbox:
                spacing 12

                button:
                    xysize (320, 490)
                    background None
                    sensitive jugable
                    action Replay("final_" + h, scope=final_scope({}))
                    hover_sound audio.sfx_hover
                    activate_sound audio.sfx_click
                    at tarjeta_hover

                    add Transform(Frame("ui/opcion_neutra.png", 40, 40, 40, 40), matrixcolor=TintMatrix(tono_h))
                    add ("ui/deco_final_" + h + ".png") matrixcolor TintMatrix(claro_h)
                    add final_sprite(h, logrado) xalign 0.5 ypos 16
                    add "ui/final_velo.png"
                    add Transform(Frame("ui/opcion_marco.png", 40, 40, 40, 40), matrixcolor=TintMatrix(borde_h))

                    vbox:
                        xalign 0.5
                        ypos 316
                        xsize 280
                        spacing 6
                        text titulo_f xalign 0.5 text_align 0.5 font gui.name_text_font size 30 color "#FFFFFF" outlines [(3, "#000000AA", 0, 0)]
                        text sub_f xalign 0.5 text_align 0.5 xsize 280 size 18 color "#FFFFFF" outlines [(3, "#000000AA", 0, 0)]

                button:
                    xysize (320, 56)
                    sensitive chip_activo
                    action Replay("extra_" + h, scope=final_scope({}))
                    hover_sound audio.sfx_hover
                    activate_sound audio.sfx_click
                    background Fixed(
                        Transform(Frame("ui/opcion_neutra.png", 40, 40, 40, 40), matrixcolor=TintMatrix(chip_fondo)),
                        Transform(Frame("ui/opcion_marco.png", 40, 40, 40, 40), matrixcolor=TintMatrix(chip_borde)))
                    hover_background Fixed(
                        Transform(Frame("ui/opcion_neutra.png", 40, 40, 40, 40), matrixcolor=TintMatrix(chip_borde)),
                        Transform(Frame("ui/opcion_marco.png", 40, 40, 40, 40), matrixcolor=TintMatrix("#FFFFFF")))

                    text chip_texto xalign 0.5 yalign 0.5 size 19 color "#F2EDF5" hover_color "#2B1B3F" insensitive_color "#CFC6E0"


    ## --- Malos y secreto ---
    hbox:
        xalign 0.5
        ypos 716
        spacing 28

        for f in FINALES_ESPECIALES:

            $ ok = final_logrado(f[0])
            $ jugable_f = final_replay_ok(f[0])
            $ color_f = f[3]
            $ tono_f = ui_mezclar(color_f, "#000000", 0.72)
            $ borde_f = "#6E6680"
            $ titulo_e = "???"
            $ estado_e = "BLOQUEADO"
            if ok:
                $ borde_f = color_f
                $ titulo_e = f[1]
                $ estado_e = "CONSEGUIDO"
                if f[0] == "temprano":
                    $ estado_e = "CONSEGUIDO  ·  " + str(temprano_versiones()) + "/2 VERSIONES"
                elif jugable_f:
                    $ estado_e = "CONSEGUIDO  ·  REVIVIR"
            $ pista_e = f[2]
            if f[0] == "secreto" and not ok:
                $ pista_e = f[2] + "  (" + str(rutas_completadas()) + "/5 rutas)"

            $ accion_f = None
            if jugable_f:
                if f[0] == "temprano":
                    $ accion_f = Show("final_versiones")
                else:
                    $ accion_f = Replay("final_" + f[0], scope=final_scope({}))

            button:
                xysize (560, 170)
                background None
                sensitive jugable_f
                action accion_f
                hover_sound audio.sfx_hover
                activate_sound audio.sfx_click
                at tarjeta_hover

                add Transform(Frame("ui/opcion_neutra.png", 40, 40, 40, 40), matrixcolor=TintMatrix(tono_f))
                add Transform(Frame("ui/opcion_marco.png", 40, 40, 40, 40), matrixcolor=TintMatrix(borde_f))
                add "ui/hud_icono_flor.png" matrixcolor TintMatrix(borde_f) xpos 36 ypos 32

                vbox:
                    xpos 100
                    ypos 28
                    xsize 420
                    spacing 6
                    text titulo_e font gui.name_text_font size 32 color "#FFF8FC"
                    text pista_e size 19 xsize 420 color "#CFC6E0"
                    text estado_e size 16 kerning 4 color borde_f

    use cinta_volver
    

screen final_versiones():

    modal True
    zorder 300

    $ color_f = "#9AA7A8"
    $ tono_f = ui_mezclar(color_f, "#000000", 0.72)
    $ hover_fondo = ui_mezclar(color_f, "#000000", 0.50)

    add Solid("#0B0712DD")

    ## Clic fuera del panel = cerrar.
    button:
        xysize (1920, 1080)
        background None
        action Hide("final_versiones")

    fixed:
        xalign 0.5
        yalign 0.5
        xysize (1180, 620)

        add Transform(Frame("ui/opcion_neutra.png", 40, 40, 40, 40), matrixcolor=TintMatrix(tono_f))
        add Transform(Frame("ui/opcion_marco.png", 40, 40, 40, 40), matrixcolor=TintMatrix(color_f))

        ## Título con una flor a cada lado
        add "ui/flor.png" matrixcolor TintMatrix(color_f) alpha 0.7 zoom 0.7 xpos 300 ypos 40
        add "ui/flor.png" matrixcolor TintMatrix(color_f) alpha 0.7 zoom 0.7 xpos 840 ypos 40
        text "DESPIDO TEMPRANO" xalign 0.5 ypos 40 font gui.name_text_font size 38 kerning 4 color "#FFF8FC"
        text "¿Qué versión quieres revivir?" xalign 0.5 ypos 102 size 24 color "#CFC6E0"

        hbox:
            xalign 0.5
            ypos 170
            spacing 40

            for v in FINALES_TEMPRANO:

                $ visto = temprano_visto(v["clave"])
                $ borde_v = "#6E6680"
                $ letra_v = "?"
                $ titulo_v = "???"
                $ desc_v = v["pista"]
                $ estado_v = "BLOQUEADA"
                $ color_texto = "#8F8AA0"
                if visto:
                    $ borde_v = color_f
                    $ letra_v = v["clave"].upper()
                    $ titulo_v = v["titulo"]
                    $ desc_v = v["resumen"]
                    $ estado_v = "REVIVIR"
                    $ color_texto = "#CFC6E0"

                button:
                    xysize (500, 340)
                    sensitive visto
                    action [Hide("final_versiones"), Replay(v["label"], scope=final_scope(v["scope"]))]
                    hover_sound audio.sfx_hover
                    activate_sound audio.sfx_click
                    at tarjeta_hover

                    background Fixed(
                        Transform(Frame("ui/opcion_neutra.png", 40, 40, 40, 40), matrixcolor=TintMatrix("#232728")),
                        Transform(Frame("ui/opcion_marco.png", 40, 40, 40, 40), matrixcolor=TintMatrix(borde_v)))
                    hover_background Fixed(
                        Transform(Frame("ui/opcion_neutra.png", 40, 40, 40, 40), matrixcolor=TintMatrix(hover_fondo)),
                        Transform(Frame("ui/opcion_marco.png", 40, 40, 40, 40), matrixcolor=TintMatrix("#FFFFFF")))

                    ## Letra gigante de marca de agua (Corregido con at Transform)
                    text letra_v:
                        xalign 0.93
                        yalign 0.95
                        font gui.name_text_font
                        size 220
                        color borde_v
                        at Transform(alpha=0.10)

                    text ("VERSIÓN " + v["clave"].upper()):
                        xpos 40
                        ypos 32
                        size 18
                        kerning 5
                        color borde_v

                    text titulo_v:
                        xpos 40
                        ypos 62
                        font gui.name_text_font
                        size 38
                        color "#FFF8FC"

                    add Solid(borde_v, xsize=420, ysize=2) xpos 40 ypos 136 alpha 0.5

                    text desc_v:
                        xpos 40
                        ypos 154
                        xsize 400
                        size 22
                        color color_texto

                    add "ui/flor.png" matrixcolor TintMatrix(borde_v) zoom 0.4 xpos 36 ypos 290
                    text estado_v:
                        xpos 76
                        ypos 296
                        size 16
                        kerning 5
                        color borde_v

        textbutton "Cerrar":
            xalign 0.5
            ypos 556
            action Hide("final_versiones")
            text_size 26
            text_idle_color "#BDB3D1"
            text_hover_color "#FFFFFF"

    key "game_menu" action Hide("final_versiones")
            

## --- Extras (provisionales) ---------------------------------------------------
## Aquí irá el epílogo "Después de la boda" de cada hermana.

label extra_ichika:
    scene bg_negro
    narrador "Extra de Ichika: próximamente."
    return

label extra_nino:
    scene bg_negro
    narrador "Extra de Nino: próximamente."
    return

label extra_miku:
    scene bg_negro
    narrador "Extra de Miku: próximamente."
    return

label extra_yotsuba:
    scene bg_negro
    narrador "Extra de Yotsuba: próximamente."
    return

label extra_itsuki:
    scene bg_negro
    narrador "Extra de Itsuki: próximamente."
    return