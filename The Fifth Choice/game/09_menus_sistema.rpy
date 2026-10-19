################################################################################
## 09_menus_sistema.rpy — Menús de sistema al estilo de las quintillizas
## Sustituye (por prioridad de carga) a las pantallas de screens.rpy:
## game_menu, file_slots (Guardar/Cargar), preferences, history, about, confirm.
################################################################################

## Nombre del capítulo que se muestra en cada hueco de guardado.
## Se cambia desde el guion:  $ save_name = "Capítulo 1"
default save_name = ""

## (texto, pantalla, motivo de la hermana, solo dentro de la partida)
define NAV_SISTEMA = [
    ("Historial", "history", "nino", True),
    ("Guardar", "save", "itsuki", True),
    ("Cargar", "load", "yotsuba", False),
    ("Opciones", "preferences", "miku", False),
    ("Acerca de", "about", "ichika", False),
    ("Ayuda", "help", "flor", False),
]


init python:

    def hist_estilo(h):
        """Estilo de una línea del historial, tomado de los show_ del personaje."""
        args = {}
        try:
            args = h.show_args
        except Exception:
            args = {}
        if args is None:
            args = {}
        tipo = args.get("tipo", "narrador")
        placa = args.get("placa", "#C9C3D6")
        tinta = args.get("tinta", "#2B1B3F")
        return (tipo, placa, tinta)


## --- Estilos ----------------------------------------------------------------

style vscrollbar:
    xsize 12
    base_bar Solid("#FFFFFF1F")
    thumb Solid("#FFB7C5")
    unscrollable "hide"

style etiqueta_opcion is default:
    font gui.name_text_font
    size 24
    kerning 4
    color "#ffffff"

style hist_placa is default:
    ysize 36
    xminimum 140
    padding (28, 0, 34, 0)

style help_label_text:
    color "#FFB7C5"
    size 26

style help_text:
    color "#EDE7F6"
    size 24


## --- Cinta genérica (interruptores, confirmaciones…) -------------------------
## Se enciende sola cuando su acción está activa (selected).

screen cinta_boton(texto, accion, clave, ancho=420, alto=58, tam=26):

    $ color = "#E8E0F2"
    if clave in PETALO_COLOR:
        $ color = PETALO_COLOR[clave]
    $ oscuro = ui_mezclar(color, "#000000", 0.72)
    $ claro = ui_mezclar(color, "#FFFFFF", 0.35)

    button:
        xysize (ancho, alto)
        action accion
        hover_sound audio.sfx_hover
        activate_sound audio.sfx_click

        background Fixed(
            Transform("ui/menu_cinta.png", xysize=(ancho, alto), fit="fill", matrixcolor=TintMatrix("#1B1026"), alpha=0.80),
            Transform("ui/menu_cinta_borde.png", xysize=(ancho, alto), fit="fill", matrixcolor=TintMatrix(color)))
        hover_background Fixed(
            Transform("ui/menu_cinta.png", xysize=(ancho, alto), fit="fill", matrixcolor=TintMatrix(claro)),
            Transform("ui/menu_cinta_borde.png", xysize=(ancho, alto), fit="fill", matrixcolor=TintMatrix("#FFFFFF")))
        selected_background Fixed(
            Transform("ui/menu_cinta.png", xysize=(ancho, alto), fit="fill", matrixcolor=TintMatrix(color)),
            Transform("ui/menu_cinta_borde.png", xysize=(ancho, alto), fit="fill", matrixcolor=TintMatrix("#FFFFFF")))

        text texto:
            xalign 0.5
            yalign 0.5
            font gui.name_text_font
            size tam
            kerning 2
            color "#F2EDF5"
            hover_color oscuro
            selected_color oscuro


## --- Barra de volumen / velocidad ----------------------------------------------

screen control_barra(etiqueta, valor, hermana):

    $ color = PETALO_COLOR[hermana]

    vbox:
        spacing 12

        text etiqueta font gui.name_text_font size 26 kerning 3 color color

        bar:
            value valor
            xsize 480
            ysize 24
            left_bar Solid(color)
            right_bar Solid("#FFFFFF26")
            thumb Transform(Solid("#FFFFFF"), xysize=(24, 24))
            thumb_offset 12


## --- MARCO COMÚN ---------------------------------------------------------------

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    add "main_menu_bg" fit "cover"
    add Solid("#120A1CD2")
    add "ui/menu_panel.png"

    $ titulo_mayus = title.upper()
    text titulo_mayus xpos 70 ypos 48 font gui.name_text_font size 60 kerning 8 color "#FFF8FC" outlines [(5, "#1B1026CC", 0, 0)] substitute False

    ## --- Cintas de navegación ---
    vbox:
        xpos 70
        ypos 175
        spacing 24

        for nombre, pantalla, clave, solo_juego in NAV_SISTEMA:

            $ mostrar = True
            if solo_juego and main_menu:
                $ mostrar = False
            if pantalla == "help" and not renpy.variant("pc"):
                $ mostrar = False

            if mostrar:

                $ col = "#E8E0F2"
                if clave != "flor":
                    $ col = PETALO_COLOR[clave]
                $ osc = ui_mezclar(col, "#000000", 0.72)

                button:
                    xysize (440, 68)
                    action ShowMenu(pantalla)
                    selected (title == nombre)
                    hover_sound audio.sfx_hover
                    activate_sound audio.sfx_click
                    background ui_cinta_menu(col, clave, False)
                    hover_background ui_cinta_menu(col, clave, True)
                    selected_background ui_cinta_menu(col, clave, True)
                    at boton_slide

                    text nombre:
                        xpos 112
                        yalign 0.5
                        font gui.name_text_font
                        size 30
                        kerning 2
                        color "#F2EDF5"
                        hover_color osc
                        selected_color osc

        if not main_menu:

            button:
                xysize (440, 68)
                action MainMenu()
                hover_sound audio.sfx_hover
                activate_sound audio.sfx_click
                background ui_cinta_menu("#E8E0F2", "flor", False)
                hover_background ui_cinta_menu("#E8E0F2", "flor", True)
                at boton_slide

                text "Menú principal":
                    xpos 112
                    yalign 0.5
                    font gui.name_text_font
                    size 30
                    kerning 2
                    color "#F2EDF5"
                    hover_color "#2B1B3F"

    ## --- Contenido de cada menú ---
    fixed:
        xpos 862
        ypos 56
        xsize 1022
        ysize 960

        if scroll == "viewport":

            viewport:
                yinitial yinitial
                scrollbars "vertical"
                mousewheel True
                draggable True
                pagekeys True
                side_yfill True

                vbox:
                    spacing spacing

                    transclude

        else:

            transclude

    use cinta_volver


## --- GUARDAR Y CARGAR ----------------------------------------------------------

screen punto_pagina(texto, accion, n):

    $ color = PETALO_COLOR[PETALO_ORDEN[n % 5]]

    button:
        xysize (46, 46)
        action accion
        hover_sound audio.sfx_hover
        background Transform("ui/flor.png", matrixcolor=TintMatrix(color), alpha=0.40, zoom=0.82)
        hover_background Transform("ui/flor.png", matrixcolor=TintMatrix(color), alpha=0.85, zoom=0.82)
        selected_background Transform("ui/flor.png", matrixcolor=TintMatrix(color), alpha=1.0, zoom=0.82)

        text texto xalign 0.5 yalign 0.5 size 17 color "#FFFFFF" hover_color "#2B1B3F" selected_color "#2B1B3F"


screen slot_tarjeta(slot):

    $ color = PETALO_COLOR[PETALO_ORDEN[(slot - 1) % 5]]
    $ cargable = FileLoadable(slot)

    vbox:
        spacing 8

        fixed:
            xysize (322, 181)

            button:
                xysize (322, 181)
                background None
                action FileAction(slot)
                hover_sound audio.sfx_hover
                activate_sound audio.sfx_click
                at tarjeta_hover

                if cargable:
                    add Transform(FileScreenshot(slot), xysize=(322, 181), fit="fill")
                else:
                    add "ui/gal_bloqueo.png"
                    add "ui/flor.png" matrixcolor TintMatrix("#FFFFFF") alpha 0.22 zoom 1.5 align (0.5, 0.5)

                add "ui/gal_marco.png" matrixcolor TintMatrix(color)

                key "save_delete" action FileDelete(slot)

            if cargable:
                textbutton "×":
                    xalign 1.0
                    yalign 0.0
                    xoffset -8
                    action FileDelete(slot)
                    text_size 36
                    text_idle_color "#FFFFFFAA"
                    text_hover_color "#FFB7C5"

        fixed:
            xysize (322, 26)
            text FileTime(slot, format="{#file_time}%d/%m/%Y  ·  %H:%M", empty="Vacío") xalign 0.0 yalign 0.5 size 19 color "#CFC6E0"
            text FileSaveName(slot) xalign 1.0 yalign 0.5 size 19 color color


screen file_slots(title):

    use game_menu(title):

        $ pagina = str(FileCurrentPage())
        $ encabezado = "PÁGINA " + pagina
        if pagina == "auto":
            $ encabezado = "GUARDADO AUTOMÁTICO"
        elif pagina == "quick":
            $ encabezado = "GUARDADO RÁPIDO"

        fixed:
            xysize (1022, 960)

            text encabezado xpos 0 ypos 0 font gui.name_text_font size 30 kerning 4 color "#FFB7C5" substitute False

            vbox:
                ypos 56
                spacing 36

                for fila in range(3):
                    hbox:
                        spacing 20

                        for col_n in range(3):
                            $ slot = fila * 3 + col_n + 1
                            use slot_tarjeta(slot)

            hbox:
                xalign 0.5
                ypos 810
                spacing 12

                textbutton "<":
                    action FilePagePrevious()
                    yalign 0.5
                    text_size 34
                    text_idle_color "#BDB3D1"
                    text_hover_color "#FFB7C5"
                    text_insensitive_color "#FFFFFF33"

                key "save_page_prev" action FilePagePrevious()

                if config.has_autosave:
                    use punto_pagina("A", FilePage("auto"), 0)

                if config.has_quicksave:
                    use punto_pagina("R", FilePage("quick"), 1)

                for p in range(1, 10):
                    use punto_pagina(str(p), FilePage(p), p + 1)

                textbutton ">":
                    action FilePageNext()
                    yalign 0.5
                    text_size 34
                    text_idle_color "#BDB3D1"
                    text_hover_color "#FFB7C5"
                    text_insensitive_color "#FFFFFF33"

                key "save_page_next" action FilePageNext()

            if config.has_sync:
                if CurrentScreenName() == "save":
                    textbutton "Subir Sync":
                        xalign 0.5
                        ypos 890
                        action UploadSync()
                        text_idle_color "#BDB3D1"
                        text_hover_color "#FFB7C5"
                else:
                    textbutton "Descargar Sync":
                        xalign 0.5
                        ypos 890
                        action DownloadSync()
                        text_idle_color "#BDB3D1"
                        text_hover_color "#FFB7C5"


## --- OPCIONES ------------------------------------------------------------------

screen preferences():

    tag menu

    use game_menu(_("Opciones")):

        hbox:
            ypos 70
            spacing 70

            vbox:
                spacing 18
                xsize 440

                if renpy.variant("pc") or renpy.variant("web"):
                    text "PANTALLA" style "etiqueta_opcion"
                    use cinta_boton("Ventana", Preference("display", "window"), "ichika")
                    use cinta_boton("Pantalla completa", Preference("display", "fullscreen"), "ichika")
                    null height 34

                text "SALTAR" style "etiqueta_opcion"
                use cinta_boton("Texto no visto", Preference("skip", "toggle"), "nino")
                use cinta_boton("Tras elecciones", Preference("after choices", "toggle"), "nino")
                use cinta_boton("Transiciones", InvertSelected(Preference("transitions", "toggle")), "nino")
                null height 34

                text "SONIDO" style "etiqueta_opcion"
                use cinta_boton("Silenciar todo", Preference("all mute", "toggle"), "itsuki")

            vbox:
                spacing 74
                xsize 480

                use control_barra("MÚSICA", Preference("music volume"), "miku")
                use control_barra("EFECTOS DE SONIDO", Preference("sound volume"), "yotsuba")
                use control_barra("VELOCIDAD DEL TEXTO", Preference("text speed"), "ichika")
                use control_barra("AUTOAVANCE", Preference("auto-forward time"), "nino")


## --- HISTORIAL -----------------------------------------------------------------

screen history():

    tag menu

    predict False

    use game_menu(_("Historial"), scroll="viewport", yinitial=1.0, spacing=24):

        for h in _history_list:

            $ estilo = hist_estilo(h)
            $ tipo_h = estilo[0]
            $ placa_h = estilo[1]
            $ tinta_h = estilo[2]
            $ texto_h = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)

            $ fuente_h = gui.text_font
            $ tam_h = 28
            $ color_h = "#EDE7F6"
            if tipo_h == "pensamiento":
                $ fuente_h = gui.libreta_font
                $ tam_h = 30
                $ color_h = "#CBBDE6"
            elif tipo_h == "narrador":
                $ color_h = "#BDB3D1"

            vbox:
                spacing 8

                if h.who:
                    window:
                        style "hist_placa"
                        background Transform(Frame("ui/placa.png", 40, 0, 40, 0), matrixcolor=TintMatrix(placa_h))
                        text h.who font gui.name_text_font size 22 kerning 2 color tinta_h yalign 0.5 substitute False

                text texto_h font fuente_h size tam_h color color_h xsize 940 substitute False

        if not _history_list:
            text "El historial está vacío." size 28 color "#BDB3D1"


## --- ACERCA DE -----------------------------------------------------------------

screen about():

    tag menu

    use game_menu(_("Acerca de"), scroll="viewport", spacing=22):

        add "main_menu_logo" xalign 0.5

        text _("Versión [config.version!t]") xalign 0.5 size 22 color "#CFC6E0"

        if gui.about:
            text "[gui.about!t]" xsize 960 size 24 color "#EDE7F6"

        text _("Hecho con {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]") xsize 960 size 20 color "#BDB3D1"


## --- CONFIRMACIONES (salir, sobrescribir, volver al menú…) ---------------------

screen confirm(message, yes_action, no_action):

    modal True
    zorder 200

    add Solid("#0B0712CC")

    fixed:
        xalign 0.5
        yalign 0.5
        xysize (1000, 380)

        add Transform(Frame("ui/opcion_neutra.png", 40, 40, 40, 40), matrixcolor=TintMatrix("#2B1B3F"))
        add Transform(Frame("ui/opcion_marco.png", 40, 40, 40, 40), matrixcolor=TintMatrix("#FFB7C5"))

        text _(message):
            xalign 0.5
            ypos 80
            xsize 860
            text_align 0.5
            font gui.name_text_font
            size 36
            color "#FFF8FC"

        hbox:
            xalign 0.5
            ypos 250
            spacing 40

            use cinta_boton("Sí", yes_action, "itsuki", 360, 64, 30)
            use cinta_boton("No", no_action, "miku", 360, 64, 30)

    key "game_menu" action no_action