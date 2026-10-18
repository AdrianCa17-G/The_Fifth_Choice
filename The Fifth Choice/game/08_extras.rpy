################################################################################
## 08_extras.rpy — Galería y Finales
################################################################################

default persistent.final_malo_temprano_visto = False

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
    ]),
    ("ichika", "Ichika", "ichika", [
        ("cg_ichika_puerta", "Bienvenido"),
        ("cg_ichika_ensayo", "Sala de ensayo"),
        ("cg_ichika_desarmada", "Sin máscara"),
        ("cg_ichika_mascara", "La máscara"),
    ]),
    ("nino", "Nino", "nino", [
        ("cg_nino_pasillo", "Ni una semana"),
        ("cg_nino_centro_comercial", "Harina"),
        ("cg_nino_receta", "La receta"),
        ("cg_nino_llamada", "La llamada"),
        ("cg_nino_confrontacion_cocina", "La discusión"),
        ("cg_nino_grieta_cocina", "La grieta"),
    ]),
    ("miku", "Miku", "miku", [
        ("cg_miku_sofa", "Logística"),
        ("cg_miku_biblioteca", "Biblioteca"),
        ("cg_miku_estudio", "El temario"),
        ("cg_miku_sorpresa", "Sorpresa"),
    ]),
    ("yotsuba", "Yotsuba", "yotsuba", [
        ("cg_yotsuba_corriendo", "Bienvenido"),
        ("cg_yotsuba_pista", "Vuelta veinte"),
        ("cg_yotsuba_rotulador", "El rotulador"),
        ("cg_yotsuba_despedida", "Una vuelta más"),
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
    ("temprano", "Despido temprano", "Tres puertas cerradas en el primer mes.", "#9AA7A8"),
    ("malo", "Despedida", "Estar cerca de todas, y no llegar a ninguna.", "#C0504D"),
    ("secreto", "Final secreto", "Cinco caminos, un solo estudiante completo.", "#F4D03F"),
]

## Pon True cuando existan los extras "Después de la boda".
define EXTRAS_DISPONIBLES = False


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
        """Fondo de una cinta del menú (reposo o activa)."""
        oscuro = ui_mezclar(color, "#000000", 0.72)
        claro = ui_mezclar(color, "#FFFFFF", 0.35)
        if activa:
            return Fixed(
                Transform("ui/menu_cinta.png", matrixcolor=TintMatrix(claro)),
                Transform("ui/menu_cinta_borde.png", matrixcolor=TintMatrix("#FFFFFF")),
                Transform("ui/hud_icono_" + icono + ".png", matrixcolor=TintMatrix(oscuro), xpos=52, yalign=0.5))
        return Fixed(
            Transform("ui/menu_cinta.png", matrixcolor=TintMatrix("#1B1026"), alpha=0.80),
            Transform("ui/menu_cinta_borde.png", matrixcolor=TintMatrix(color)),
            Transform("ui/hud_icono_" + icono + ".png", matrixcolor=TintMatrix(color), xpos=52, yalign=0.5))


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
        hbox:
            xpos 862
            ypos 952
            spacing 18

            textbutton "<":
                action SetScreenVariable("pagina", pagina - 1)
                sensitive (pagina > 0)
                text_size 32
                text_idle_color "#BDB3D1"
                text_hover_color "#FFB7C5"
                text_insensitive_color "#FFFFFF33"

            for p in range(paginas):
                textbutton str(p + 1):
                    action SetScreenVariable("pagina", p)
                    text_size 32
                    text_idle_color "#BDB3D1"
                    text_hover_color "#FFB7C5"
                    text_selected_color "#FFFFFF"

            textbutton ">":
                action SetScreenVariable("pagina", pagina + 1)
                sensitive (pagina < paginas - 1)
                text_size 32
                text_idle_color "#BDB3D1"
                text_hover_color "#FFB7C5"
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
        ypos 150
        spacing 28

        for h in ["ichika", "nino", "miku", "yotsuba", "itsuki"]:

            $ nombre = h.capitalize()
            $ color_h = PETALO_COLOR[h]
            $ claro_h = ui_mezclar(color_h, "#FFFFFF", 0.25)
            $ tono_h = TARJETA_TONO[h]
            $ logrado = final_logrado(h)
            $ extra_ok = galeria_completa(h)
            $ cg = galeria_conteo(h)

            $ borde_h = "#6E6680"
            $ titulo_f = "???"
            $ sub_f = FINALES_PISTAS[h]
            if logrado:
                $ borde_h = color_h
                $ titulo_f = "Final de " + nombre
                $ sub_f = "Final romántico conseguido"

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

                fixed:
                    xysize (320, 450)
                    add Transform(Frame("ui/opcion_neutra.png", 40, 40, 40, 40), matrixcolor=TintMatrix(tono_h))
                    add ("ui/deco_final_" + h + ".png") matrixcolor TintMatrix(claro_h)
                    add final_sprite(h, logrado) xalign 0.5 ypos 16
                    add Transform(Frame("ui/opcion_marco.png", 40, 40, 40, 40), matrixcolor=TintMatrix(borde_h))

                    vbox:
                        xalign 0.5
                        ypos 316
                        xsize 280
                        spacing 4
                        text titulo_f xalign 0.5 text_align 0.5 font gui.name_text_font size 30 color "#FFF8FC"
                        text sub_f xalign 0.5 text_align 0.5 xsize 280 size 17 color "#CFC6E0"

                button:
                    xysize (320, 56)
                    sensitive chip_activo
                    action Replay("extra_" + h)
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
        ypos 706
        spacing 28

        for f in FINALES_ESPECIALES:

            $ ok = final_logrado(f[0])
            $ color_f = f[3]
            $ tono_f = ui_mezclar(color_f, "#000000", 0.72)
            $ borde_f = "#6E6680"
            $ titulo_e = "???"
            $ estado_e = "BLOQUEADO"
            if ok:
                $ borde_f = color_f
                $ titulo_e = f[1]
                $ estado_e = "CONSEGUIDO"
            $ pista_e = f[2]
            if f[0] == "secreto" and not ok:
                $ pista_e = f[2] + "  (" + str(rutas_completadas()) + "/5 rutas)"

            fixed:
                xysize (560, 170)
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