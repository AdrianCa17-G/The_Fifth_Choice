################################################################################
## 06_main_menu.rpy (v5)
## Menú principal - The Fifth Choice
## v5: cinco cintas (una por hermana, con su motivo). Al pasar el ratón por una
##     se enciende su sprite. Galería y Finales como opciones nuevas. Iconos de
##     utilidad (Acerca de, Ayuda, Salir) arriba a la derecha.
################################################################################


# ==============================================================
# REGISTRO DE IMÁGENES
# ==============================================================
image main_menu_bg = "images/Fondo_Menu.png"
image main_menu_logo = Transform("images/Logo_Menu_v2.png", zoom=0.48)

image sakura_petals = Fixed(
    SnowBlossom("ui/caida_ichika_petalo.png",  count=2, border=50, yspeed=(60, 130), xspeed=(20, 60)),
    SnowBlossom("ui/caida_ichika_flor.png",    count=1, border=50, yspeed=(50, 110), xspeed=(20, 50)),
    SnowBlossom("ui/caida_nino_petalo.png",    count=2, border=50, yspeed=(70, 140), xspeed=(20, 60)),
    SnowBlossom("ui/caida_nino_flor.png",      count=1, border=50, yspeed=(50, 120), xspeed=(20, 50)),
    SnowBlossom("ui/caida_miku_petalo.png",    count=2, border=50, yspeed=(60, 120), xspeed=(20, 60)),
    SnowBlossom("ui/caida_miku_flor.png",      count=1, border=50, yspeed=(55, 115), xspeed=(20, 50)),
    SnowBlossom("ui/caida_yotsuba_petalo.png", count=2, border=50, yspeed=(65, 135), xspeed=(20, 60)),
    SnowBlossom("ui/caida_yotsuba_flor.png",   count=1, border=50, yspeed=(50, 110), xspeed=(20, 50)),
    SnowBlossom("ui/caida_itsuki_petalo.png",  count=2, border=50, yspeed=(60, 130), xspeed=(20, 60)),
    SnowBlossom("ui/caida_itsuki_flor.png",    count=1, border=50, yspeed=(55, 120), xspeed=(20, 50)),
)

# ==============================================================
# CONFIGURACIÓN Y FUNCIONES
# ==============================================================
init python:

    ## La entrada animada solo ocurre la primera vez que se abre el menú en esta sesión.
    _menu_estado = {"entrada_hecha": False}

    def menu_entrada_pendiente():
        return not _menu_estado["entrada_hecha"]

    def menu_marcar_entrada():
        _menu_estado["entrada_hecha"] = True

    ## Archivo de cada sprite. Cámbialo por "menu/ichika_menu.png", etc.
    MENU_SPR = {
        "ichika":  "images/menu/ichika_menu.png",
        "nino":    "images/menu/nino_menu.png",
        "miku":    "images/menu/miku_menu.png",
        "yotsuba": "images/menu/yotsuba_menu.png",
        "itsuki":  "images/menu/itsuki_menu.png",
    }

    ## True = dibuja una línea verde: el pelo de las cinco debe tocarla.
    MENU_GUIA = False

    ## Alto (px) que mide cada hermana DESDE LA CORONILLA hasta los pies.
    MENU_SPR_ALTO = 820

    ## Centro horizontal (px) de cada hermana.
    MENU_SPR_X = {"ichika": 935, "nino": 1160, "miku": 1365, "yotsuba": 1575, "itsuki": 1755}

    ## Fila del PNG (contando desde arriba) donde empieza el PELO, sin contar el
    ## lazo de Yotsuba ni el ahoge de Itsuki. Es lo que iguala el tamaño de las cinco.
    MENU_CORONILLA = {"ichika": 0, "nino": 0, "miku": 0, "yotsuba": 75, "itsuki": 65}

    PANEL_ANCHO  = 600
    PANEL_COLOR  = "#2B1B3F"
    PANEL_A_INI  = 0.88
    PANEL_A_FIN  = 0.00
    PANEL_PASOS  = 48
    PANEL_ACENTO = "#FFB7C5"

    def panel_lateral(color=None, a_ini=None, a_fin=None, ancho=None, pasos=None):
        """Columna vertical opaca a la izquierda que se desvanece a la derecha."""
        color = color if color is not None else PANEL_COLOR
        a_ini = a_ini if a_ini is not None else PANEL_A_INI
        a_fin = a_fin if a_fin is not None else PANEL_A_FIN
        ancho = ancho if ancho is not None else PANEL_ANCHO
        pasos = pasos if pasos is not None else PANEL_PASOS

        alto  = config.screen_height
        base  = ancho // pasos
        resto = ancho % pasos

        args = []
        x = 0
        for i in range(pasos):
            t = i / float(pasos - 1)
            a = a_ini + (a_fin - a_ini) * t
            w = base + (1 if i < resto else 0)
            args.append((x, 0))
            args.append(Solid(color + "%02x" % int(round(a * 255)),
                            xsize=w, ysize=alto))
            x += w

        return Composite((ancho, alto), *args)

    _menu_spr_cache = {}

    def menu_sprite(hermana):
        """Sprite escalado. Se crea UNA sola vez y se reutiliza: crear uno nuevo en
        cada actualización de pantalla era una de las causas del lag."""
        if hermana not in _menu_spr_cache:
            ruta = MENU_SPR[hermana]
            ancho, alto = renpy.image_size(ruta)
            contenido = alto - MENU_CORONILLA[hermana]
            _menu_spr_cache[hermana] = Transform(ruta, zoom=MENU_SPR_ALTO / float(contenido))
        return _menu_spr_cache[hermana]

    def menu_alfa(hermana, quien):
        """Opacidad: si el ratón está sobre la cinta de OTRA hermana, esta baja un poco."""
        if quien is None:
            return 1.0
        if quien == hermana:
            return 1.0
        if quien in MENU_SPR:
            return 0.62
        return 1.0

    def menu_subida(hermana, quien):
        """La hermana de la cinta bajo el ratón sube unos píxeles."""
        if quien == hermana:
            return -14
        return 0


# ==============================================================
# BOTÓN: una cinta con el color y el motivo de su hermana
# ==============================================================
screen boton_menu(texto, accion, hermana):

    $ color = PETALO_COLOR[hermana]
    $ oscuro = ui_mezclar(color, "#000000", 0.72)
    $ claro = ui_mezclar(color, "#FFFFFF", 0.35)

    button:
        action accion
        xysize (440, 68)
        hover_sound audio.sfx_hover
        activate_sound audio.sfx_click
        tooltip hermana
        at boton_slide

        background Fixed(
            Transform("ui/menu_cinta.png", matrixcolor=TintMatrix("#1B1026"), alpha=0.80),
            Transform("ui/menu_cinta_borde.png", matrixcolor=TintMatrix(color)),
            Transform("ui/hud_icono_" + hermana + ".png", matrixcolor=TintMatrix(color), xpos=52, yalign=0.5))

        hover_background Fixed(
            Transform("ui/menu_cinta.png", matrixcolor=TintMatrix(claro)),
            Transform("ui/menu_cinta_borde.png", matrixcolor=TintMatrix("#FFFFFF")),
            Transform("ui/hud_icono_" + hermana + ".png", matrixcolor=TintMatrix(oscuro), xpos=52, yalign=0.5))

        text texto:
            xpos 112
            yalign 0.5
            font gui.name_text_font
            size 33
            kerning 2
            color "#F2EDF5"
            hover_color oscuro


# ==============================================================
# PANTALLA PRINCIPAL
# ==============================================================
screen main_menu():
    tag menu

    ## `default` se evalúa una vez por pantalla: decide si esta apertura lleva entrada animada.
    default entrada = menu_entrada_pendiente()
    on "show" action Function(menu_marcar_entrada)

    $ t_panel = estatico
    $ t_logo = estatico
    $ t_tag = estatico
    if entrada:
        $ t_panel = panel_fadein
        $ t_logo = logo_fadein
        $ t_tag = tagline_fadein

    add "main_menu_bg" fit "cover"
    add "sakura_petals"

    add "ui/menu_panel.png" at t_panel

    $ quien = GetTooltip()

    ## --- SPRITES: la hermana de la cinta con el ratón encima se enciende ---
    for n, h in enumerate(["ichika", "itsuki", "nino", "yotsuba", "miku"]):
        $ reaccion = sprite_luz(menu_alfa(h, quien), menu_subida(h, quien))
        if entrada:
            add menu_sprite(h) at [sprite_anim(0.2 * n, 0.4 * n), reaccion] xpos MENU_SPR_X[h] xanchor 0.5 ypos 1092 yanchor 1.0
        else:
            add menu_sprite(h) at reaccion xpos MENU_SPR_X[h] xanchor 0.5 ypos 1092 yanchor 1.0

    if MENU_GUIA:
        add Solid("#00FF00", xsize=1920, ysize=2) ypos (1092 - MENU_SPR_ALTO)

    ## --- LOGO ---
    add "main_menu_logo":
        xalign 0.03
        yalign 0.03
        at t_logo

    ## --- TAGLINE ---
    text "¿A quién elegirás?":
        xpos 1350
        xanchor 0.5
        ypos 36
        font gui.name_text_font
        color "#FFF8FC"
        size 44
        kerning 3
        outlines [
            (6, "#1B1026CC", 0, 0),
            (2, "#FF9FBE", 0, 0)
        ]
        at t_tag

    text "Todas saben algo que no te quieren enseñar. Tú decides a quién escuchas.":
        xpos 1350
        xanchor 0.5
        ypos 104
        xsize 900
        text_align 0.5
        font gui.name_text_font
        color "#FFE3EE"
        size 27
        outlines [(3, "#1B1026CC", 0, 0)]
        at t_tag

    ## --- LAS CINCO CINTAS ---
    vbox:
        xpos 90
        yalign 0.78
        spacing 10

        use boton_menu("Comenzar", Start(), "ichika")
        use boton_menu("Cargar", ShowMenu("load"), "nino")
        use boton_menu("Galería", ShowMenu("galeria"), "miku")
        use boton_menu("Finales", ShowMenu("finales"), "yotsuba")
        use boton_menu("Opciones", ShowMenu("preferences"), "itsuki")

    ## --- ICONOS DE UTILIDAD, arriba a la derecha ---
    hbox:
        xalign 1.0
        yalign 0.0
        xoffset -36
        yoffset 24
        spacing 10

        button:
            xysize (68, 68)
            background ui_icono("info", False)
            hover_background ui_icono("info", True)
            action ShowMenu("about")
            tooltip "Acerca de"
            at icono_hover

        if renpy.variant("pc"):
            button:
                xysize (68, 68)
                background ui_icono("ayuda", False)
                hover_background ui_icono("ayuda", True)
                action ShowMenu("help")
                tooltip "Ayuda"
                at icono_hover

        button:
            xysize (68, 68)
            background ui_icono("salir", False)
            hover_background ui_icono("salir", True)
            action Quit(confirm=True)
            tooltip "Salir"
            at icono_hover

    ## El letrero de los iconos no debe mostrar el nombre de una hermana.
    $ rotulo = quien
    if quien in MENU_SPR:
        $ rotulo = None
    if rotulo:
        text rotulo:
            xalign 1.0
            xoffset -40
            ypos 104
            size 22
            color "#FFFFFF"
            outlines [(3, "#1B102699", 0, 0)]

    ## --- VERSIÓN ---
    text "v1.0":
        xalign 0.98
        yalign 0.98
        color "#FFFFFF44"
        size 18

# ==============================================================
# TRANSFORMACIONES
# ==============================================================

# Cinta: se desliza a la derecha al pasar el ratón
transform boton_slide:
    on idle:
        linear 0.18 xoffset 0
    on hover:
        linear 0.18 xoffset 24

transform estatico:
    alpha 1.0

# Sprite: se enciende o se apaga según el botón activo
transform sprite_luz(alfa, subida):
    ease 0.12 alpha alfa yoffset subida

# Capa lateral: entra deslizándose desde la izquierda
transform panel_fadein:
    alpha 0
    xoffset -60
    linear 0.9 alpha 1.0 xoffset 0

# Sprite: entrada desde abajo + flotación suave en loop
transform sprite_anim(delay, float_offset):
    alpha 0
    yoffset 40
    pause delay
    linear 0.8 alpha 1.0 yoffset 0
    pause float_offset
    block:
        ease 2.2 yoffset -10
        ease 2.2 yoffset 0
        repeat

# Logo: fade in suave
transform logo_fadein:
    alpha 0
    pause 0.3
    linear 1.5 alpha 1.0

# Tagline: aparece después del logo
transform tagline_fadein:
    alpha 0
    pause 1.8
    linear 1.0 alpha 1.0

