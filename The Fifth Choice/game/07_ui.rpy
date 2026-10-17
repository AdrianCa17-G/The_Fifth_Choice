################################################################################
##  07_ui.rpy — Interfaz propia (cajas de texto y flor de sakura)
################################################################################
## init -5: se ejecuta ANTES que los `define` de 00_definiciones.rpy,
## que necesitan estas funciones para crear los personajes.
## Las fuentes japonesas centran el carácter … en vertical (flota a media
## altura de las letras). Se cambia por tres puntos normales al mostrarlo.
init -5 python:

    def ui_escena(modo="normal", hermana=None, lugar=""):
        """Cambia la decoración de pantalla.
        modo: "normal", "hub" o "beat". hermana: "ichika"... o None (5 colores)."""
        store.ui_modo = modo
        store.ui_hermana = hermana
        store.ui_lugar = lugar
        if modo != "normal":
            renpy.hide_screen("lugar_aviso")

    ## Fondo -> nombre de lugar. "" = ignorar ese fondo.
    BG_LUGAR = {

        "bg_cuarto_mc": "Habitación de [nombre_jugador]",
        "bg_comedor": "Casa de los Uesugi",
        "bg_escuela": "Instituto Asaba",
        "bg_aula": "Aula · Día",
        "bg_aula_tarde": "Aula Vacía",
        "bg_aula_anochecer": "Aula Vacía · Anochecer",
        "bg_azotea": "Azotea · Día",
        "bg_azotea_tarde": "Azotea · Atardecer",
        "bg_edificio": "Edificio de las Nakano",
        "bg_entrada_edificio": "Entrada · Edificio de las Nakano",
        "bg_departamento": "Departamento Nakano",
        "bg_departamento_anochecer": "Departamento Nakano · Anochecer",
        "bg_cocina": "Cocina de las Nakano",
        "bg_sala_ensayo": "Sala de ensayo",
        "bg_sala_ensayo_anochecer": "Sala de ensayo · Anochecer",
        "bg_centro_comercial": "Centro comercial",
        "bg_centro_comercial_anochecer": "Centro comercial · Anochecer",
        "bg_biblioteca": "Biblioteca",
        "bg_biblioteca_anochecer": "Biblioteca · Anochecer",
        "bg_pista_atletismo": "Pista de atletismo",
        "bg_pista_atletismo_anochecer": "Pista de atletismo · Anochecer",
        "bg_negro": "",
    }

        ## Fondos cuyo nombre NO se enseña en el prólogo: el protagonista aún no
    ## sabe que ahí viven las Nakano.
    BG_OCULTOS_PROLOGO = [
        "bg_edificio",
        "bg_entrada_edificio",
        "bg_departamento",
        "bg_departamento_anochecer",
    ]

    def ui_revisar_lugar(event, interact=True, **kwargs):
        """Se ejecuta en cada línea de diálogo. Si el FONDO cambió y estamos en
        modo normal, enseña el aviso del lugar unos segundos."""
        if event != "begin":
            return
        actual = None
        for tag in BG_LUGAR:
            if renpy.showing(tag):
                actual = tag
        if actual is None:
            return
        if BG_LUGAR[actual] == "":
            return
        if store.ui_prologo and actual in BG_OCULTOS_PROLOGO:
            return
        if actual == store.ui_ultimo_lugar:
            return
        store.ui_ultimo_lugar = actual
        if store.ui_modo == "normal":
            renpy.show_screen("lugar_aviso", BG_LUGAR[actual])

    config.all_character_callbacks.append(ui_revisar_lugar)

    def ui_raya(i, modo, hermana):
        """Color y opacidad de la raya i (0 a 4) de las esquinas."""
        orden = ["ichika", "nino", "miku", "yotsuba", "itsuki"]
        if hermana is None:
            color = PETALO_COLOR[orden[i]]
        else:
            color = PETALO_COLOR[hermana]
        if modo == "normal":
            alfa = 0.55
        elif hermana is None:
            alfa = 0.85
        else:
            alfa = 0.95 - 0.12 * i
        return (color, alfa)

    config.overlay_screens.append("marco_juego")

    def ui_icono(nombre, activo):
        """Icono del menú rápido. activo=True es el estado con el ratón encima."""
        color = store.ICONO_COLOR[nombre]
        oscuro = "#2B1B3F"
        if activo:
            fondo = Transform("ui/ico_base.png", matrixcolor=TintMatrix(color))
            glifo = Transform("ui/ico_" + nombre + ".png", matrixcolor=TintMatrix(oscuro))
        else:
            fondo = Transform("ui/ico_base.png", matrixcolor=TintMatrix(oscuro), alpha=0.82)
            glifo = Transform("ui/ico_" + nombre + ".png", matrixcolor=TintMatrix(color))
        borde = Transform("ui/ico_borde.png", matrixcolor=TintMatrix(color))
        return Fixed(fondo, borde, glifo, xysize=(68, 68))

    def ui_ventana_vacia():
        """Ventana vacía que Ren'Py muestra durante show/hide/with.
        Usa la caja de quien habló por última vez para que no cambie."""
        personaje = store.narrator
        quien = getattr(store, "_last_say_who", None)
        if quien is not None:
            try:
                personaje = renpy.eval_who(quien)
            except Exception:
                personaje = store.narrator
        if personaje is None:
            personaje = store.narrator
        personaje("", interact=False)


    TARJETA_ALTOS = [220, 270, 320, 370]   # los mismos de generar_ui.py

    def ui_altura_items(items):
        """Altura de tarjeta que le queda justa al texto más largo del menú."""
        mayor = 0
        for i in items:
            alto_texto = 0
            try:
                t = Text(i.caption, style="tarjeta_texto")
                alto_texto = renpy.render(t, 432, 2000, 0, 0).get_size()[1]
            except Exception:
                lineas = len(i.caption) // 20 + 1
                alto_texto = lineas * 50
            if alto_texto > mayor:
                mayor = alto_texto
        necesario = mayor + 52 + 64
        for alto in TARJETA_ALTOS:
            if alto >= necesario:
                return alto
        return TARJETA_ALTOS[-1]

    def decision_peso(hermana, titulo, motivo, pistas=None):
        """Marca la siguiente decisión como 'con peso'.
        titulo: la pregunta. motivo: por qué importa esta decisión.
        pistas: temperatura de cada opción, en el orden en que aparecen."""
        store.decision_hermana = hermana
        store.decision_titulo = titulo
        store.decision_motivo = motivo
        if pistas is None:
            store.decision_pistas = ["calida", "tibia", "fria"]
        else:
            store.decision_pistas = pistas


    config.empty_window = ui_ventana_vacia

    def ui_arreglar_texto(texto):
        return texto.replace("\u2026", "...")

    config.say_menu_text_filter = ui_arreglar_texto

    def ui_mezclar(color_a, color_b, t):
        """Mezcla dos colores hex. t=0 devuelve color_a, t=1 devuelve color_b."""
        a = color_a.lstrip("#")
        b = color_b.lstrip("#")
        resultado = "#"
        for k in (0, 2, 4):
            va = int(a[k:k + 2], 16)
            vb = int(b[k:k + 2], 16)
            v = int(va + (vb - va) * t)
            resultado = resultado + "{:02x}".format(v)
        return resultado

    def ui_personaje(nombre, color, petalo=None, deco=None):
        """Personaje con caja rellena de su color (y motivo opcional)."""
        placa = ui_mezclar(color, "#FFFFFF", 0.45)
        tinta = ui_mezclar(color, "#000000", 0.72)
        caja = Transform("ui/caja.png", matrixcolor=TintMatrix(color))
        fondo = caja
        if deco is not None:
            fondo = Composite((1340, 240), (0, 0), caja, (0, 0), deco)
        return Character(
            nombre,
            what_color="#241B33",
            window_style="caja",
            window_background=fondo,
            show_tipo="hablante",
            show_placa=placa,
            show_tinta=tinta,
            show_petalo=petalo,
            ctc="ctc_oscuro",
            ctc_position="nestled",
        )

define PETALO_ORDEN = ["ichika", "nino", "miku", "yotsuba", "itsuki"]

define PETALO_COLOR = {
    "ichika":  C_ICHIKA,
    "nino":    C_NINO,
    "miku":    C_MIKU,
    "yotsuba": C_YOTSUBA,
    "itsuki":  C_ITSUKI,
}

## Cada pétalo es la misma imagen rotada 72 grados * i alrededor de su centro.
transform petalo_giro(i, color, brillo):
    align (0.5, 0.5)
    rotate (i * 72)
    matrixcolor TintMatrix(color)
    alpha brillo

## Marca de agua dentro de la caja, a la derecha.
## - hermana activa: su pétalo en blanco
## - "todas": cada pétalo con su color
## - el resto: apagados (oscuros sobre caja clara, claros sobre la del narrador)
screen flor_sakura(activa=None, tipo="hablante", x=1450, y=844, color_activo="#FFFFFF"):
    fixed:
        xpos x
        ypos y
        xysize (160, 160)

        for i in range(5):
            $ hermana = PETALO_ORDEN[i]
            if activa == "todas":
                add "ui/petalo.png" at petalo_giro(i, PETALO_COLOR[hermana], 0.95)
            elif activa == hermana:
                add "ui/petalo.png" at petalo_giro(i, color_activo, 0.95)
            elif tipo == "narrador":
                add "ui/petalo.png" at petalo_giro(i, "#FFFFFF", 0.16)
            else:
                add "ui/petalo.png" at petalo_giro(i, "#000000", 0.14)


## --- Indicador de "sigue" (click to continue) --------------------------------
## Un pétalo pequeño que parpadea al final de la línea cuando el texto ya
## terminó de escribirse. Tres colores, según el fondo de la caja.

## Sobre cajas pastel (las hermanas y el resto de personajes)
image ctc_oscuro:
    "ui/flor.png"
    zoom 0.5
    matrixcolor TintMatrix("#2B1B3F")
    alpha 0.9
    linear 0.6 alpha 0.25
    linear 0.6 alpha 0.9
    repeat

## Sobre la caja oscura del narrador
image ctc_claro:
    "ui/flor.png"
    zoom 0.5
    matrixcolor TintMatrix("#FFFFFF")
    alpha 0.9
    linear 0.6 alpha 0.25
    linear 0.6 alpha 0.9
    repeat

## Sobre la hoja de libreta
image ctc_libreta:
    "ui/flor.png"
    zoom 0.5
    matrixcolor TintMatrix("#B94A4A")
    alpha 0.9
    linear 0.6 alpha 0.25
    linear 0.6 alpha 0.9
    repeat


## --- Decisiones con peso ----------------------------------------------------

## Qué tan visible es la pista de temperatura (0.0 = apagada, 0.5 = muy clara).
define PISTA_FUERZA = 0.30

## Altura del conjunto (pregunta + tarjetas): 0.0 arriba, 1.0 abajo.
## Si lo quieres más abajo, sube el número (máx. ~0.75, o chocará con el borde).
define DECISION_ALINEACION = 0.45

## Tono oscuro de cada hermana para su tarjeta (distinto del violeta de las ligeras).
define TARJETA_TONO = {
    "ichika":  "#5A3340",
    "nino":    "#522A57",
    "miku":    "#1F4660",
    "yotsuba": "#1E5A3A",
    "itsuki":  "#6A2A26",
}

transform ventana_oculta:
    alpha 0.0

transform decision_velo:
    alpha 0.0
    linear 0.4 alpha 0.5

transform pregunta_entrada:
    alpha 0.0
    yoffset -40
    linear 0.4 alpha 1.0 yoffset 0

transform tarjeta_entrada(n):
    alpha 0.0
    yoffset 70
    pause (0.35 + 0.12 * n)
    linear 0.35 alpha 1.0 yoffset 0

transform tarjeta_hover:
    on idle:
        linear 0.15 yoffset 0
    on hover:
        linear 0.15 yoffset -14

style tarjeta_texto is default:
    size 31
    color "#F3EEFA"
    xpos 44
    ypos 52
    xsize 432
    line_spacing 4

style placa_centro is placa:
    xpos 0.5
    xanchor 0.5

screen choice_peso(items):

    $ color = PETALO_COLOR[decision_hermana]
    $ tinta = ui_mezclar(color, "#000000", 0.72)
    $ placa_color = ui_mezclar(color, "#FFFFFF", 0.45)
    $ claro = ui_mezclar(color, "#FFFFFF", 0.25)
    $ tono_fondo = TARJETA_TONO[decision_hermana]
    $ alto = ui_altura_items(items)

    add Solid("#000000") at decision_velo

    vbox:
        xalign 0.5
        yalign DECISION_ALINEACION
        spacing 60

        ## --- La pregunta: caja propia, centrada y por delante de todo ---
        fixed:
            at pregunta_entrada
            xalign 0.5
            xysize (1340, 240)

            add Transform("ui/caja.png", matrixcolor=TintMatrix(color))
            add ("ui/deco_" + decision_hermana + ".png")

            window:
                style "placa_centro"
                background Transform(Frame("ui/placa.png", 40, 0, 40, 0),
                                     matrixcolor=TintMatrix(placa_color))
                text "DECISIÓN" style "say_label" color tinta

            vbox:
                xalign 0.5
                yalign 0.5
                yoffset 6
                xsize 960
                spacing 10
                text decision_titulo font gui.name_text_font size 40 color tinta xalign 0.5 text_align 0.5
                text decision_motivo size 29 color tinta xalign 0.5 text_align 0.5

            use flor_sakura(decision_hermana, "hablante", 1160, 40, tinta)

        ## --- Las tarjetas ---
        hbox:
            xalign 0.5
            spacing 40

            for n, i in enumerate(items):

                $ pista = decision_pistas[n]
                $ tono = "#FFFFFF"
                $ fuerza = 0.0
                if pista == "calida":
                    $ tono = "#FFC46B"
                    $ fuerza = PISTA_FUERZA
                elif pista == "fria":
                    $ tono = "#7FA6E8"
                    $ fuerza = PISTA_FUERZA

                fixed:
                    xysize (520, alto)
                    at tarjeta_entrada(n)

                    button:
                        xysize (520, alto)
                        background None
                        action i.action
                        hover_sound audio.sfx_hover
                        activate_sound audio.sfx_click
                        at tarjeta_hover

                        add ("ui/tarjeta_" + str(alto) + ".png") matrixcolor TintMatrix(tono_fondo)
                        add ("ui/halo_" + str(alto) + ".png") matrixcolor TintMatrix(tono) alpha fuerza
                        add ("ui/deco_tarjeta_" + decision_hermana + "_" + str(alto) + ".png") matrixcolor TintMatrix(claro)
                        add ("ui/tarjeta_marco_" + str(alto) + ".png") matrixcolor TintMatrix(color)
                        use flor_sakura(decision_hermana, "hablante", 360, alto - 150, color)
                        text i.caption style "tarjeta_texto"


## --- Iconos del menú rápido -------------------------------------------------
## Los mismos colores y el mismo orden que los botones del menú principal.
define ICONO_COLOR = {
    "atras":     C_ICHIKA,
    "historial": C_NINO,
    "auto":      C_MIKU,
    "saltar":    C_YOTSUBA,
    "guardar":   C_ITSUKI,
    "menu":      "#FFFFFF",
    "info":      "#FFFFFF",
    "ayuda":     "#FFFFFF",
    "salir":     "#FFFFFF",
}

transform icono_hover:
    on idle:
        linear 0.12 yoffset 0
    on hover:
        linear 0.12 yoffset 5


## --- Decoración de pantalla -------------------------------------------------

## Tipografía de la cinta. Cámbiala aquí si quieres probar otra.
define HUD_FUENTE = gui.name_text_font

define HUB_LUGAR = {
    "ichika":  "Sala de ensayo",
    "nino":    "Centro comercial",
    "miku":    "Biblioteca",
    "yotsuba": "Pista de atletismo",
    "itsuki":  "Aula vacía",
}

default ui_modo = "normal"
default ui_hermana = None
default ui_lugar = ""
default ui_ultimo_lugar = ""
default ui_prologo = True

transform hud_cinta_entrada:
    xoffset -800
    ease 0.45 xoffset 0

transform hud_aviso_anim:
    xoffset -800
    ease 0.45 xoffset 0
    pause 3.5
    ease 0.45 xoffset -800

style hud_cinta_win is default:
    xpos 0
    ypos 22
    ysize 64
    xminimum 380
    xmaximum 1100
    padding (54, 0, 76, 0)

## La cinta en sí. Se ajusta sola al ancho del texto.
screen hud_cinta_vista(lugar, etiqueta, clave, cinta, tinta, anim, deco=True):

    $ lugar_mayus = renpy.substitute(lugar).upper()
    $ tinta_suave = tinta + "BB"
    $ deco_alfa = 0.0
    if deco:
        $ deco_alfa = 1.0

    window:
        style "hud_cinta_win"
        at anim
        background Fixed(
            Transform(Frame("ui/hud_cinta.png", 40, 0, 40, 0), matrixcolor=TintMatrix(cinta)),
            Transform("ui/hud_cinta_deco_" + clave + ".png", xalign=1.0, alpha=deco_alfa))

        hbox:
            spacing 16
            yalign 0.5

            add ("ui/hud_icono_" + clave + ".png") matrixcolor TintMatrix(tinta) yalign 0.5

            vbox:
                yalign 0.5
                spacing 0

                if etiqueta != "":
                    text etiqueta font HUD_FUENTE size 14 kerning 4 color tinta_suave substitute False

                text lugar_mayus font HUD_FUENTE size 27 kerning 2 color tinta substitute False


screen lugar_aviso(lugar):

    zorder 91

    if quick_menu:
        use hud_cinta_vista(lugar, "", "flor", "#E8E0F2", "#2B1B3F", hud_aviso_anim, False)

    timer 4.6 action Hide("lugar_aviso")

screen marco_juego():

    zorder 90

    ## Se oculta junto con el menú rápido (en el mapa del hub, por ejemplo).
    if quick_menu:

        $ base = "#E8E0F2"
        if ui_hermana is not None:
            $ base = PETALO_COLOR[ui_hermana]
        $ cinta = ui_mezclar(base, "#FFFFFF", 0.35)
        $ tinta_hud = ui_mezclar(base, "#000000", 0.75)

        add "ui/hud_sombra.png"

        for i in range(5):
            $ c, a = ui_raya(i, ui_modo, ui_hermana)
            add ("ui/hud_raya_" + str(i) + ".png") matrixcolor TintMatrix(c) alpha a xalign 0.0 yalign 1.0
            add ("ui/hud_rayad_" + str(i) + ".png") matrixcolor TintMatrix(c) alpha a xalign 1.0 yalign 1.0

        if ui_modo == "beat":
            add Solid(base, xsize=1920, ysize=5) alpha 0.9 ypos 0
            add Solid(base, xsize=1920, ysize=5) alpha 0.9 yalign 1.0

        if ui_lugar != "":

            $ clave = "flor"
            if ui_hermana is not None:
                $ clave = ui_hermana

            $ etiqueta = ""
            if ui_modo == "hub":
                $ etiqueta = "ENCUENTRO"
            elif ui_modo == "beat":
                $ etiqueta = "ESCENA CLAVE"

            use hud_cinta_vista(ui_lugar, etiqueta, clave, cinta, tinta_hud, hud_cinta_entrada)

            if ui_modo != "normal":
                text ("Quedan " + tiempo_restante) xpos 44 ypos 94 size 22 color "#FFFFFF" outlines [(3, "#1B102699", 0, 0)]