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
image main_menu_logo = "images/Logo_Menu.png"

image spr_ichika  = "images/sprites/ichika_nakano.png"
image spr_nino    = "images/sprites/nino_nakano.png"
image spr_miku    = "images/sprites/miku_nakano.png"
image spr_yotsuba = "images/sprites/yotsuba_nakano.png"
image spr_itsuki  = "images/sprites/itsuki_nakano.png"

image sakura_petals = SnowBlossom("images/petal.png", count=25, border=50)

## Hermana cuyo botón tiene el ratón encima (None = ninguna).
default menu_activa = None


# ==============================================================
# CONFIGURACIÓN Y FUNCIONES
# ==============================================================
init python:

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

    def menu_brillo(quien):
        """Brillo del sprite: la hermana del botón activo se enciende, el resto se apaga."""
        if store.menu_activa is None:
            return 0.0
        if store.menu_activa == quien:
            return 0.06
        return -0.32

    def menu_subida(quien):
        """La hermana activa sube un poco."""
        if store.menu_activa == quien:
            return -16
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
        hovered SetVariable("menu_activa", hermana)
        unhovered SetVariable("menu_activa", None)
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

    on "show"    action Play("music", "audio/bgm/main_theme.ogg", loop=True, fadeout=1.0)
    on "replace" action Play("music", "audio/bgm/main_theme.ogg", loop=True, fadeout=1.0)

    add "main_menu_bg" fit "cover"
    add "sakura_petals"

    add panel_lateral() at panel_fadein

    add Solid(PANEL_ACENTO, xsize=2, ysize=config.screen_height):
        xpos PANEL_ANCHO
        alpha 0.30
        at panel_fadein

    ## --- SPRITES: la hermana de la cinta con el ratón encima se enciende ---
    fixed:
        at sprite_tono(menu_brillo("ichika"), menu_subida("ichika"))
        add "spr_ichika" at sprite_anim(0.0, 0.0) xalign 0.29 yalign 1.0

    fixed:
        at sprite_tono(menu_brillo("nino"), menu_subida("nino"))
        add "spr_nino" at sprite_anim(0.2, 0.4) xalign 0.50 yalign 1.0

    fixed:
        at sprite_tono(menu_brillo("miku"), menu_subida("miku"))
        add "spr_miku" at sprite_anim(0.4, 0.8) xalign 0.70 yalign 1.0

    fixed:
        at sprite_tono(menu_brillo("yotsuba"), menu_subida("yotsuba"))
        add "spr_yotsuba" at sprite_anim(0.6, 1.2) xalign 0.90 yalign 1.0

    fixed:
        at sprite_tono(menu_brillo("itsuki"), menu_subida("itsuki"))
        add "spr_itsuki" at sprite_anim(0.8, 1.6) xalign 1.08 yalign 1.0

    ## --- LOGO ---
    add "main_menu_logo":
        xalign 0.03
        yalign 0.03
        at logo_fadein

    ## --- TAGLINE ---
    text "¿A quién elegirás?":
        xalign 0.65
        yalign 0.045
        font gui.name_text_font
        color "#FFF8FC"
        size 32
        kerning 2
        outlines [
            (5, "#1B1026CC", 0, 0),
            (2, "#FF9FBE", 0, 0)
        ]
        at tagline_fadein

    text "Cinco sonrisas únicas, pero solo una será tu respuesta definitiva":
        xalign 0.69
        yalign 0.10
        color "#FFD9E6CC"
        size 20
        italic True
        outlines [(2, "#1B102688", 0, 0)]
        at tagline_fadein

    ## --- LAS CINCO CINTAS ---
    vbox:
        xpos 90
        yalign 0.68
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

    $ rotulo = GetTooltip()
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

# Sprite: se enciende o se apaga según el botón activo
transform sprite_tono(brillo, subida):
    ease 0.2 matrixcolor BrightnessMatrix(brillo) yoffset subida

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