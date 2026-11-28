################################################################################
## 08_extras.rpy — Galería y Finales
################################################################################

default persistent.final_malo_temprano_visto = False
default persistent.final_malo_temprano_a_visto = False
default persistent.final_malo_temprano_b_visto = False

## --- DATOS: al añadir CG nuevos, agrégalos aquí (el % se recalcula solo) ---
## (clave, título de la pestaña, hermana o None, [(imagen, nombre), ...])
define GALERIA = [
    ("prologo", _("Prólogo"), None, [
        ("cg_familia", _("Retrato familiar")),
        ("cg_calificacion", _("Mi lugar de pensamientos")),
        ("cg_examen", _("Examen perfecto")),
        ("cg_itsuki_sentada", _("¿Por qué estás en mi asiento?")),
        ("cg_itsuki_azotea", _("Un encuentro incómodo")),
        ("cg_manija_edificio", _("Abriendo mi sentencia")),
        ("cg_maruo_reunion", _("El contrato")),
        ("cg_hermanas_estudiando", _("La primera clase")),
    ]),
    ("cap1", _("Capítulo 1"), None, [
        ("cg_itsuki_apertura", _("No me interesa tu asiento")),
        ("cg_cinco_sentadas", _("¿Están tramando algo?")),
        ("cg_libreta", _("La libreta")),
        ("cg_cinco_repasando", _("Un avance no tan esperado")),
        ("cg_cinco_estudiando", _("Resultados perfectos de un mes")),
        ("cg_maruo_espaldas", _("Se terminó")),
        ("cg_raiha_correccion", _("Corrigiendo a Raiha")),
        ("cg_cinco_aula", _("Cinco miradas antes del examen")),
        ("cg_cinco_aprobadas", _("Un final feliz")),
    ]),
    ("ichika", _("Ichika"), "ichika", [
        ("cg_ichika_puerta", _("Bienvenido")),
        ("cg_ichika_ensayo", _("Sala de ensayo")),
        ("cg_ichika_desarmada", _("Sin máscara")),
        ("cg_ichika_mascara", _("La máscara")),
        ("cg_ichika_fracaso", _("No puedo más")),
        ("cg_ichika_examen", _("Las cuentas sí salieron")),
    ]),
    ("nino", _("Nino"), "nino", [
        ("cg_nino_pasillo", _("Ni una semana")),
        ("cg_nino_centro_comercial", _("Traduciendo")),
        ("cg_nino_receta", _("Una receta con trasfondo")),
        ("cg_nino_llamada", _("¿Está hablando de mí?")),
        ("cg_nino_confrontacion_cocina", _("Una discusión intensa")),
        ("cg_nino_grieta_cocina", _("La crisis de Nino")),
        ("cg_nino_fracaso", _("Se los dije")),
        ("cg_nino_examen", _("No te lo diré dos veces")),
    ]),
    ("miku", _("Miku"), "miku", [
        ("cg_miku_sofa", _("¿Hablando de Sengoku?")),
        ("cg_miku_biblioteca", _("Biblioteca")),
        ("cg_miku_estudio", _("El temario")),
        ("cg_miku_sorpresa", _("Sorpresa")),
        ("cg_miku_fracaso", _("Quiero usar mis audífonos")),
        ("cg_miku_examen", _("Mi propia historia")),
    ]),
    ("yotsuba", _("Yotsuba"), "yotsuba", [
        ("cg_yotsuba_corriendo", _("Bienvenido")),
        ("cg_yotsuba_pista", _("Vuelta veinte")),
        ("cg_yotsuba_rotulador", _("El rotulador")),
        ("cg_yotsuba_cronometro", _("Una vuelta más")),
        ("cg_yotsuba_fracaso", _("Solo me preocupan las demás")),
        ("cg_yotsuba_examen", _("Esta vez no me rendí")),
    ]),
    ("itsuki", _("Itsuki"), "itsuki", [
        ("cg_itsuki_discusion", _("¿Otra vez tú?")),
        ("cg_itsuki_atascada", _("Estoy atascada")),
        ("cg_itsuki_contraida", _("No pienso admitir mi error")),
        ("cg_itsuki_reto", _("¿Qué pasa?")),
        ("cg_itsuki_azotea_cuaderno", _("Mi rincón habitual")),
        ("cg_itsuki_azotea_manos", _("Manos quietas")),
        ("cg_itsuki_fracaso", _("El mismo error")),
        ("cg_itsuki_examen", _("Una hipótesis comprobada")),
    ]),
]

define FINALES_PISTAS = {
    "ichika":  _("A veces, quien más sonríe es quien más necesita que te quedes a su lado."),
    "nino":    _("Quien más distancia pone, en el fondo solo espera a alguien que no se rinda con ella."),
    "miku":    _("Aprende a escuchar sus silencios... es ahí donde guarda lo que de verdad siente."),
    "yotsuba": _("Hazle recordar la luz tan hermosa que tiene, incluso cuando ella no pueda verla."),
    "itsuki":  _("Sostén su mano cuando lo necesite, pero déjala sentir que camina por sí misma."),
}

## (clave, título, pista, color)
define FINALES_ESPECIALES = [
    ("temprano", _("Despido temprano"), _("Decir que no cada vez que pudiste decir que sí."), "#9AA7A8"),
    ("malo", _("Despedida"), _("Estar cerca de todas, y no llegar a ninguna."), "#C0504D"),
    ("secreto", _("Final secreto"), _("Cinco caminos, un solo estudiante completo."), "#F4D03F"),
]

## Pon True cuando existan los extras "Después de la boda".
define EXTRAS_DISPONIBLES = False


define FINALES_TEMPRANO = [
    {
        "clave": "a",
        "titulo": _("El portazo"),
        "resumen": _("En la cocina. Maruo corta el contrato antes de que nadie pueda despedirse."),
        "pista": _("Cuando la paciencia de Maruo se acaba pronto."),
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
        "titulo": _("La despedida"),
        "resumen": _("Tras la semana de exámenes. Cuatro reprueban y cada una dice lo que le faltaba decir."),
        "pista": _("Cuando la última oportunidad tampoco alcanza."),
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
        ## Va colocado desde arriba (ypos 16): el adorno extra se compensa subiéndolo.
        base, extra = sprite_busto("images/sprites/%s_sprites/%s_neutral.png" % (hermana, hermana), hermana + " neutral")
        sube = -int(round(extra * 0.55))
        if logrado:
            return Transform(base, zoom=0.55, yoffset=sube)
        return Transform(base, zoom=0.55, yoffset=sube, matrixcolor=TintMatrix("#0B0712"), alpha=0.85)

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

        text _("Volver"):
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
    $ titulo_sec = ui_mayus(__(sec[1]))
    $ pct_total = 0
    if total[1] > 0:
        $ pct_total = int(round(100.0 * total[0] / total[1]))
    $ pct_sec = 0
    if conteo[1] > 0:
        $ pct_sec = int(round(100.0 * conteo[0] / conteo[1]))

    add "main_menu_bg" fit "cover"
    add Solid("#120A1CCC")
    add "ui/menu_panel.png"

    text _("GALERÍA") xpos 70 ypos 48 font gui.name_text_font size 60 kerning 8 color "#FFF8FC" outlines [(5, "#1B1026CC", 0, 0)]

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
        text (__("CG DESBLOQUEADOS") + "   " + str(total[0]) + " / " + str(total[1]) + "   ·   " + str(pct_total) + " %") font gui.name_text_font size 26 kerning 3 color "#FFF8FC"
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

    text _("FINALES") xpos 88 ypos 20 font gui.name_text_font size 60 kerning 8 color "#FFF8FC" outlines [(5, "#1B1026CC", 0, 0)]

    vbox:
        xpos 980
        ypos 56
        spacing 10
        text (__("FINALES DESCUBIERTOS") + "   " + str(hechos) + " / 8   ·   " + str(pct) + " %") font gui.name_text_font size 26 kerning 3 color "#FFF8FC"
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
                $ titulo_f = __("Final de {}").format(__(nombre))
                $ sub_f = _("Final romántico conseguido")
                if jugable:
                    $ sub_f = _("Final romántico conseguido\nClic para revivirlo")

            $ chip_fondo = "#2A2236"
            $ chip_borde = "#6E6680"
            $ chip_texto = __("EXTRA  ·  Galería {}/{}").format(cg[0], cg[1])
            if extra_ok:
                $ chip_fondo = tono_h
                $ chip_borde = color_h
                $ chip_texto = _("EXTRA  ·  Próximamente")

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
            $ estado_e = _("BLOQUEADO")
            if ok:
                $ borde_f = color_f
                $ titulo_e = f[1]
                $ estado_e = _("CONSEGUIDO")
                if f[0] == "temprano":
                    $ estado_e = __("CONSEGUIDO  ·  {}/2 VERSIONES").format(temprano_versiones())
                elif jugable_f:
                    $ estado_e = _("CONSEGUIDO  ·  REVIVIR")
            $ pista_e = f[2]
            if f[0] == "secreto" and not ok:
                $ pista_e = __(f[2]) + "  " + __("({}/5 rutas)").format(rutas_completadas())

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
        text _("DESPIDO TEMPRANO") xalign 0.5 ypos 40 font gui.name_text_font size 38 kerning 4 color "#FFF8FC"
        text _("¿Qué versión quieres revivir?") xalign 0.5 ypos 102 size 24 color "#CFC6E0"

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
                $ estado_v = _("BLOQUEADA")
                $ color_texto = "#8F8AA0"
                if visto:
                    $ borde_v = color_f
                    $ letra_v = v["clave"].upper()
                    $ titulo_v = v["titulo"]
                    $ desc_v = v["resumen"]
                    $ estado_v = _("REVIVIR")
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

                    text (__("VERSIÓN") + " " + v["clave"].upper()):
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

        textbutton _("Cerrar"):
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


################################################################################
## EXTRAS DEL MENÚ: Minijuegos · Animaciones · Repetir
## Solo en el menú principal (cintas rosa Raiha bajo «Ayuda», 09_menus_sistema).
## Todo se reproduce con Replay: la partida y sus variables no se tocan.
################################################################################

## Foto de la última partida al cerrar el hub 3 (Repetir → Semana de exámenes).
default persistent.foto_hub3 = None
## Valores de la última barra de progreso vista (Animaciones → Cierre).
default persistent.prog_ultimo = None

## Variables que llegan por el scope del Replay.
default mj_extra_h = "yotsuba"
default ea_tipo = ""
default ea_h = "ichika"
default ea_v = ""
default extra_titulo = ""

## (texto, pantalla) de las cintas de EXTRAS.
define EXTRAS_NAV = [
    (_("Minijuegos"), "extra_minijuegos"),
    (_("Animaciones"), "extra_animaciones"),
    (_("Repetir"), "extra_repetir"),
]

## Lo que la foto del hub 3 guarda: todo lo que la interconexión 6 y el Evento 6 leen.
define EXTRA_FOTO_VARS = [
    "nombre_jugador", "mc_motivo",
    "puntos_ichika", "puntos_nino", "puntos_miku", "puntos_yotsuba", "puntos_itsuki",
    "primera_conexion", "primera_decision_hecha",
    "ichika_visitada_cap1", "nino_visitada_cap1", "miku_visitada_cap1",
    "yotsuba_visitada_cap1", "itsuki_visitada_cap1",
    "ichika_rama_cap1", "nino_rama_cap1", "miku_rama_cap1",
    "yotsuba_rama_cap1", "itsuki_rama_cap1",
    "tiempo_restante", "maruo_ultimatum", "despido_cap1", "nino_rama_beat",
    "despido_en_beat", "desaires_cap1", "hub_visitadas", "destino",
    "ui_prologo", "save_name",
]

## (clave, pestaña, descripción) de los grupos del teatro.
define ANIM_GRUPOS = [
    ("cort", _("Cortinillas"), _("Tarjetas de capítulo y de tarde libre")),
    ("encuentro", _("Encuentros"), _("La salida del hub hacia cada hermana")),
    ("tarde", _("Tardes"), _("Tarde completada, según cómo acabó")),
    ("mj", _("Minijuegos"), _("Entrada y salidas de cada minijuego")),
    ("decidir", _("Decidir"), _("«Hora de decidir» antes de cada decisión")),
    ("cierre", _("Cierre"), _("La barra de las chicas y los créditos al cerrar el capítulo")),
]

define ANIM_RAMA_TXT = {"calida": _("Cálida"), "tibia": _("Tibia"), "fria": _("Fría")}
define ANIM_MJ_TXT = {"entrada": _("Entrada"), "ganado": _("Ganado"), "saltado": _("Que lo haga ella")}
## En minúscula para la pista «Cierra una tarde con X (cálida)».
define ANIM_RAMA_MIN = {"calida": _("cálida"), "tibia": _("tibia"), "fria": _("fría")}

## Las cinco decisiones con peso, copiadas de 02_cap1_<Hermana>.rpy (pregunta,
## motivo, opciones en orden cálida, tibia, fría). Si cambian allí, cámbialas aquí.
define EXTRA_DECIDIR = {
    "ichika": (_("¿Qué le dirás a Ichika?"),
               _("Se durmió en el suelo del club, y ya está bromeando otra vez."),
               [_("No seguirle la broma. Esperar a que hable ella."),
                _("Seguirle la broma. Por hoy ya tuvo bastante."),
                _("Si tienes energía para hacer chistes, tienes energía\npara estudiar.")]),
    "nino": (_("¿Qué le dirás a Nino?"),
             _("Te contó más de lo que quería. Ahora espera tu respuesta."),
             [_("Tienes razón en desconfiar. Solo el tiempo lo va a demostrar."),
              _("Cargarle la cesta, sin decir nada."),
              _("Yo sí voy a durar.")]),
    "miku": (_("¿Qué le dirás a Miku?"),
             _("Habló un minuto entero de lo que ama. Y después pidió perdón."),
             [_("Preguntarle cuánto tardaba la sal en llegar."),
              _("Decirle que se le da bien. Es la verdad."),
              _("Lo de la sal no entra en el examen.")]),
    "yotsuba": (_("¿Qué le dirás a Yotsuba?"),
                _("Te ofrece el cronómetro. Lo que acaba de decir sigue ahí."),
                [_("No tomar el cronómetro todavía. Volver a lo que dijo."),
                 _("Claro, dame el cronómetro."),
                 _("Si correr es lo tuyo, concéntrate en eso.")]),
    "itsuki": (_("¿Qué le dirás a Itsuki?"),
               _("Tres intentos, el mismo error. No te va a pedir ayuda."),
               [_("Señalarle dónde mirar. Solo eso."),
                _("¿Quieres que lo revisemos desde el principio?"),
                _("Quitarle el cuaderno y resolverlo. Le ahorro la tarde.")]),
}


init python:

    import copy

    def anim_marcar(clave):
        """Primera vez que se ve una animación: la desbloquea en Extras → Animaciones."""
        setattr(persistent, "anim_" + clave, True)

    def anim_visto(clave):
        return bool(getattr(persistent, "anim_" + clave, False))

    def mj_jugado(juego):
        return bool(getattr(persistent, "mj_jugado_" + juego, False))

    def extra_foto_hub3():
        """Al cerrar el hub 3: guarda el estado para Repetir → Semana de exámenes."""
        foto = {}
        for v in EXTRA_FOTO_VARS:
            foto[v] = copy.deepcopy(getattr(store, v, None))
        persistent.foto_hub3 = foto

    def extra_foto_scope():
        """Copia de la foto para el Replay (una copia: el Replay no debe tocar la foto)."""
        return final_scope(copy.deepcopy(persistent.foto_hub3))

    def extra_prog_valores():
        if persistent.prog_ultimo is None:
            return {"ichika": 0, "nino": 0, "miku": 0, "yotsuba": 0, "itsuki": 0}
        return dict(persistent.prog_ultimo)

    def extra_decidir_items(h):
        items = []
        opciones = EXTRA_DECIDIR[h][2]
        for k in range(len(opciones)):
            items.append((opciones[k], k))
        return items

    def extra_tras_cargar():
        """Partidas de antes de Extras: lo que ya pasó en la partida cargada desbloquea."""
        if store.nino_rama_beat == "calida":
            persistent.nino_beat_calido = True
        for h in store.e6_mj:
            r = store.e6_mj[h]
            if r.get("intentos", 0) > 0:
                setattr(persistent, "mj_jugado_" + r["juego"], True)
                anim_marcar("mj_" + h + "_entrada")
                anim_marcar("mj_" + h + "_" + r["resultado"])
        if not store.ui_prologo:
            anim_marcar("cort_prologo_fin")
            anim_marcar("cort_cap1_inicio")
        for h in store.hub_visitadas:
            anim_marcar("cort_hub")
            anim_marcar("encuentro_" + h)
            rama = rama_de(h)
            if rama in ANIM_RAMA_TXT:
                anim_marcar("tarde_" + h + "_" + rama)
                anim_marcar("decidir_" + h)

    config.after_load_callbacks.append(extra_tras_cargar)


## init 1: el catálogo lee hub_tono (hub_mapa.rpy) y CORT_* (13_transiciones.rpy).
init 1 python:

    def anim_texto(p):
        """Pista del catálogo: texto, o (plantilla con {}, nombres...) que se traduce al mostrarla."""
        if isinstance(p, tuple):
            return __(p[0]).format(*[__(x) for x in p[1:]])
        return p

    def anim_catalogo():
        """[(clave, grupo, título, subtítulo, color, icono, pista, scope)], en orden."""
        lista = []
        cort = [
            ("prologo_fin", _("Fin del prólogo"), _("Cinco alumnas, cero interés"), CORT_LILA, _("Termina el prólogo.")),
            ("cap1_inicio", _("Capítulo 1"), _("Días de tutoría"), CORT_ROSA, _("Empieza el Capítulo 1.")),
            ("hub", _("Tarde libre"), _("Empieza tu decisión"), CORT_LILA, _("Llega a la primera tarde libre.")),
            ("cap1_examenes", _("Semana de exámenes"), _("El clímax"), CORT_ORO, _("Llega a la semana de exámenes.")),
            ("cap1_fin", _("Fin del Capítulo 1"), _("Un estudiante perfecto"), CORT_ROSA, _("Termina el Capítulo 1.")),
            ("final_malo", _("Final malo"), _("Despido temprano"), "#9AA7A8", _("Pierde el trabajo antes de tiempo.")),
        ]
        for c in cort:
            lista.append(("cort_" + c[0], "cort", c[1], c[2], c[3], "flor", c[4],
                          {"ea_tipo": "cort", "ea_v": c[0]}))
        for h in PETALO_ORDEN:
            nombre = h.capitalize()
            lista.append(("encuentro_" + h, "encuentro", nombre, HUB_LUGAR[h], PETALO_COLOR[h], h,
                          (_("Pasa una tarde libre con {}."), nombre),
                          {"ea_tipo": "encuentro", "ea_h": h}))
        for h in PETALO_ORDEN:
            nombre = h.capitalize()
            for rama in ["calida", "tibia", "fria"]:
                lista.append(("tarde_" + h + "_" + rama, "tarde", nombre, ANIM_RAMA_TXT[rama],
                              hub_tono(h, rama), h,
                              (_("Cierra una tarde con {} ({})."), nombre, ANIM_RAMA_MIN[rama]),
                              {"ea_tipo": "tarde", "ea_h": h, "ea_v": rama}))
        pistas_mj = {
            "entrada": _("Juega su minijuego."),
            "ganado": _("Gana su minijuego."),
            "saltado": _("Deja que lo haga ella."),
        }
        for h in E6_ORDEN_EXAMEN:
            for tipo in ["entrada", "ganado", "saltado"]:
                lista.append(("mj_" + h + "_" + tipo, "mj", h.capitalize(), ANIM_MJ_TXT[tipo],
                              PETALO_COLOR[h], h, pistas_mj[tipo],
                              {"ea_tipo": "mj", "ea_h": h, "ea_v": tipo}))
        for h in PETALO_ORDEN:
            nombre = h.capitalize()
            lista.append(("decidir_" + h, "decidir", nombre, _("Hora de decidir"), PETALO_COLOR[h], h,
                          (_("Llega a la decisión de {}."), nombre),
                          {"ea_tipo": "decidir", "ea_h": h}))
        lista.append(("cierre", "cierre", _("Cinco nombres"), _("Cierre del Capítulo 1"), CORT_ROSA, "flor",
                      _("Termina el Capítulo 1."), {"ea_tipo": "cierre"}))
        lista.append(("creditos", "cierre", _("Créditos"), _("Rol del Capítulo 1"), CORT_LILA, "flor",
                      _("Termina el Capítulo 1."), {"ea_tipo": "creditos"}))
        return lista

    ANIM_LISTA = anim_catalogo()

    ## Puente de una vez para partidas de antes de Extras (persistent ya cargado).
    for _h in E6_ORDEN_CANON:
        if getattr(persistent, "e6_mj_ganado_" + _h, False):
            setattr(persistent, "mj_jugado_" + E6_MJ_JUEGO[_h], True)
    if persistent.cap1_completado:
        for _k in ["cort_prologo_fin", "cort_cap1_inicio", "cort_hub", "cort_cap1_examenes", "cort_cap1_fin"]:
            anim_marcar(_k)
        if persistent.prog_ultimo is not None:
            anim_marcar("cierre")
        ## El rol llegó después: quien ya cerró el capítulo no tiene otra forma de verlo.
        anim_marcar("creditos")
    if persistent.final_malo_temprano_visto:
        anim_marcar("cort_final_malo")


## --- Piezas ------------------------------------------------------------------

## Tarjeta de las de Finales: fondo y borde teñidos (Frame de 9 cortes).
screen extra_fondo(fondo, borde):
    add Transform(Frame("ui/opcion_neutra.png", 40, 40, 40, 40), matrixcolor=TintMatrix(fondo))
    add Transform(Frame("ui/opcion_marco.png", 40, 40, 40, 40), matrixcolor=TintMatrix(borde))


screen extra_mj_tarjeta(h, nivel):

    $ juego = E6_MJ_JUEGO[h]
    $ jugado = mj_jugado(juego)
    $ color = PETALO_COLOR[h]
    $ fondo = "#2A2236"
    $ borde = "#6E6680"
    $ titulo = "???"
    $ chibi = Transform(mj_chibi(h, "neutral", 0.34), matrixcolor=TintMatrix("#0B0712"), alpha=0.85)
    if jugado:
        $ fondo = TARJETA_TONO[h]
        $ borde = color
        $ titulo = MJ_REGISTRO[juego]["titulo"]
        $ chibi = mj_chibi(h, "neutral", 0.34)

    button:
        xysize (190, 390)
        background None
        sensitive jugado
        action Replay("extra_mj", scope=final_scope({"mj_extra": True, "mj_extra_h": h, "mj_extra_nivel": nivel}), locked=False)
        hover_sound audio.sfx_hover
        activate_sound audio.sfx_click
        at tarjeta_hover

        use extra_fondo(fondo, borde)
        add chibi xalign 0.5 ypos 14

        vbox:
            xalign 0.5
            ypos 200
            xsize 166
            spacing 8

            text titulo xalign 0.5 text_align 0.5 xsize 166 font gui.name_text_font size 22 color "#FFF8FC"
            text (__(h.capitalize()) + " · " + __(E6_MATERIA[h])) xalign 0.5 text_align 0.5 size 16 color borde
            if not jugado:
                text _("Juégalo en la semana de exámenes.") xalign 0.5 text_align 0.5 xsize 166 size 16 color "#8F8AA0"


screen extra_anim_tarjeta(a):

    $ visto = anim_visto(a[0])
    $ fondo = "#2A2236"
    $ borde = "#6E6680"
    $ titulo = "???"
    $ sub = anim_texto(a[6])
    $ color_sub = "#8F8AA0"
    if visto:
        $ fondo = ui_mezclar(a[4], "#000000", 0.72)
        $ borde = a[4]
        $ titulo = a[2]
        $ sub = a[3]
        $ color_sub = "#CFC6E0"

    button:
        xysize (330, 118)
        background None
        sensitive visto
        action Replay("extra_anim", scope=final_scope(a[7]), locked=False)
        hover_sound audio.sfx_hover
        activate_sound audio.sfx_click
        at tarjeta_hover

        use extra_fondo(fondo, borde)
        add ("ui/hud_icono_" + a[5] + ".png") matrixcolor TintMatrix(borde) xpos 26 yalign 0.5

        vbox:
            xpos 82
            yalign 0.5
            xsize 226
            spacing 4

            text titulo font gui.name_text_font size 25 color "#FFF8FC"
            text sub xsize 226 size 17 color color_sub


screen extra_repetir_tarjeta(rotulo, titulo, texto, color, abierta, pista, accion):

    $ fondo = "#2A2236"
    $ borde = "#6E6680"
    $ t = "???"
    $ d = pista
    $ color_d = "#8F8AA0"
    if abierta:
        $ fondo = ui_mezclar(color, "#000000", 0.72)
        $ borde = color
        $ t = titulo
        $ d = texto
        $ color_d = "#CFC6E0"

    button:
        xysize (1006, 190)
        background None
        sensitive abierta
        action accion
        hover_sound audio.sfx_hover
        activate_sound audio.sfx_click
        at tarjeta_hover

        use extra_fondo(fondo, borde)
        add "ui/flor.png" matrixcolor TintMatrix(borde) alpha 0.85 xpos 44 yalign 0.5

        vbox:
            xpos 130
            yalign 0.5
            xsize 820
            spacing 8

            text rotulo size 17 kerning 5 color borde
            text t font gui.name_text_font size 38 color "#FFF8FC"
            text d xsize 820 size 21 color color_d


## --- MINIJUEGOS ---------------------------------------------------------------

screen extra_minijuegos():
    tag menu

    default nivel = "media"

    ## Sin el selector, nivel None = la dificultad por defecto del juego.
    $ nivel_replay = None
    if persistent.nino_beat_calido:
        $ nivel_replay = nivel

    use game_menu(_("Minijuegos")):

        vbox:
            ypos 70
            spacing 40

            text _("Los cinco minijuegos de la semana de exámenes. Diviértete jugándolos.") size 24 color "#CFC6E0"

            hbox:
                spacing 13
                for h in E6_ORDEN_EXAMEN:
                    use extra_mj_tarjeta(h, nivel_replay)

            if persistent.nino_beat_calido:
                vbox:
                    spacing 16
                    text _("DIFICULTAD") style "etiqueta_opcion"
                    hbox:
                        spacing 14
                        use cinta_boton(_("Difícil"), SetScreenVariable("nivel", "dificil"), "", 240, 58, 24)
                        use cinta_boton(_("Media"), SetScreenVariable("nivel", "media"), "", 240, 58, 24)
                        use cinta_boton(_("Asistida"), SetScreenVariable("nivel", "asistida"), "", 240, 58, 24)


## --- ANIMACIONES --------------------------------------------------------------

screen extra_animaciones():
    tag menu

    default grupo = "cort"

    $ items = []
    $ vistas = 0
    for a in ANIM_LISTA:
        if a[1] == grupo:
            $ items.append(a)
            if anim_visto(a[0]):
                $ vistas = vistas + 1
    $ desc = ""
    for g in ANIM_GRUPOS:
        if g[0] == grupo:
            $ desc = g[2]
    $ filas = (len(items) + 2) // 3

    use game_menu(_("Animaciones")):

        vbox:
            ypos 70
            spacing 24

            hbox:
                spacing 12
                for g in ANIM_GRUPOS:
                    use cinta_boton(g[1], SetScreenVariable("grupo", g[0]), "", 160, 56, 21)

            text (__(desc) + "   ·   " + str(vistas) + " / " + str(len(items))) size 24 color "#CFC6E0"

            vbox:
                spacing 16
                for fila in range(filas):
                    hbox:
                        spacing 16
                        for k in range(3):
                            $ idx = fila * 3 + k
                            if idx < len(items):
                                use extra_anim_tarjeta(items[idx])


## --- REPETIR ------------------------------------------------------------------

screen extra_repetir():
    tag menu

    $ abierto = bool(persistent.cap1_completado)
    $ hay_foto = persistent.foto_hub3 is not None
    $ pista_semana = _("Termina el Capítulo 1.")
    if abierto and not hay_foto:
        $ pista_semana = _("Juega otra vez hasta cerrar la tercera tarde.")

    $ accion_semana = NullAction()
    if hay_foto:
        $ accion_semana = Replay("cap1_interconexion_6", scope=extra_foto_scope(), locked=False)

    use game_menu(_("Repetir")):

        vbox:
            ypos 70
            spacing 26

            text _("Vuelve a jugar un tramo. Tus partidas guardadas no cambian.") size 24 color "#CFC6E0"

            use extra_repetir_tarjeta(_("PRÓLOGO"), _("Prólogo"), _("Desde el primer día. Al terminar, vuelves al menú."), CORT_LILA, abierto, _("Termina el Capítulo 1."), Replay("prologo", scope=final_scope({}), locked=False))
            use extra_repetir_tarjeta(_("CAPÍTULO 01"), _("Días de tutoría"), _("Desde la apertura hasta cerrar la tercera tarde, como en una partida nueva."), CORT_ROSA, abierto, _("Termina el Capítulo 1."), Replay("cap1_apertura", scope=final_scope({}), locked=False))
            use extra_repetir_tarjeta(_("CAPÍTULO 01"), _("Semana de exámenes"), _("Desde el final de la tercera tarde, con lo que elegiste la última vez."), CORT_ORO, abierto and hay_foto, pista_semana, accion_semana)


## --- REPRODUCCIÓN (siempre dentro de un Replay) --------------------------------

label extra_mj:

    scene expression MJ_PRUEBA_FONDO[mj_extra_h]
    with Dissolve(0.4)

    ## Como en el Evento 6: el tema de la hermana. M3 (Miku) arranca su propia música.
    if mj_extra_h != "miku":
        $ renpy.music.play(getattr(audio, mj_extra_h), channel="music", fadein=1.0)

    call mj_ejecutar(E6_MJ_JUEGO[mj_extra_h], mj_extra_h) from _call_mj_ejecutar_5

    stop music fadeout 1.5
    scene bg_negro
    with Dissolve(0.6)

    return


label extra_anim:

    $ quick_menu = False
    scene bg_negro
    with Dissolve(0.3)

    if ea_tipo == "cort":
        if ea_v == "hub":
            call cortinilla_hub(1) from _call_cortinilla_hub_3
        else:
            call expression ("cortinilla_" + ea_v) from _call_expression_23
    elif ea_tipo == "encuentro":
        call cortinilla_hermana(ea_h) from _call_cortinilla_hermana_3
    elif ea_tipo == "tarde":
        call hub_completado(ea_h, 1, ea_v) from _call_hub_completado_3
    elif ea_tipo == "mj":
        call extra_anim_mj from _call_extra_anim_mj
    elif ea_tipo == "decidir":
        call extra_anim_decidir from _call_extra_anim_decidir
    elif ea_tipo == "cierre":
        call progreso_chicas(extra_prog_valores()) from _call_progreso_chicas_1
    elif ea_tipo == "creditos":
        call creditos_rol from _call_creditos_rol

    return


label extra_anim_mj:

    scene expression MJ_PRUEBA_FONDO[ea_h]
    with Dissolve(0.4)
    $ renpy.music.play(getattr(audio, ea_h), channel="music", fadein=0.5)
    $ extra_titulo = MJ_REGISTRO[E6_MJ_JUEGO[ea_h]]["titulo"]

    if ea_v == "entrada":
        call mj_transicion("entrada", ea_h, extra_titulo) from _call_mj_transicion
        show screen mj_transicion_prueba_marco(ea_h, "neutral")
        $ renpy.pause(1.2, hard=True)
        hide screen mj_transicion_prueba_marco
        with Dissolve(0.4)
    else:
        ## Las salidas parten del marco, como en el juego.
        if ea_v == "ganado":
            show screen mj_transicion_prueba_marco(ea_h, "feliz")
        else:
            show screen mj_transicion_prueba_marco(ea_h, "neutral")
        with Dissolve(0.4)
        $ renpy.pause(0.8, hard=True)
        hide screen mj_transicion_prueba_marco
        call mj_transicion(ea_v, ea_h, extra_titulo) from _call_mj_transicion_1
        $ renpy.pause(0.6, hard=True)

    stop music fadeout 1.0
    return


label extra_anim_decidir:

    scene expression MJ_PRUEBA_FONDO[ea_h]
    with Dissolve(0.4)
    $ renpy.show(ea_h + " neutral", at_list=[pj(0.5)])
    with dissolve

    $ decision_peso(ea_h, EXTRA_DECIDIR[ea_h][0], EXTRA_DECIDIR[ea_h][1])
    $ renpy.display_menu(extra_decidir_items(ea_h))

    return
