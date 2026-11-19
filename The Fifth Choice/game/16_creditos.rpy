################################################################################
##  16_creditos.rpy — Créditos (fuente única), aviso inicial, rol final y
##  pantalla «Continuará».
##
##  CREDITOS_AVISO, CREDITOS_GRATIS y CREDITOS son el ÚNICO texto de créditos:
##  los usan el aviso inicial (splashscreen), «Acerca de» (09_menus_sistema) y el
##  rol del final del Capítulo 1. CREDITOS.md (raíz del repo) dice lo mismo: si
##  cambias algo aquí, cámbialo allí.
##
##  Líneas de una sección: ("sub", texto) encabezado pequeño · ("linea", texto)
##  · ("nota", texto) · ("enlace", texto, url) (clicable solo en «Acerca de»).
##  Los caracteres japoneses se envuelven solos en Noto Sans JP (cred_jp).
##
##  PRUEBA — consola (Shift+O):
##    jump splashscreen        aviso inicial ($ persistent.aviso_visto = False
##                             para ver el bloqueo de la primera vez)
##    jump cap1_continuara     rol + «Continuará» + menú ($ persistent.creditos_vistos
##                             = False para verlo sin poder saltar)
##    cred_autocomprobar()
################################################################################

default persistent.aviso_visto = False
default persistent.creditos_vistos = False

## Página oficial (la única de descarga) y redes. El botón de apoyo abre la
## página de itch.io: cambia CREDITOS_DONAR si abres otra vía de donación.
define CREDITOS_WEB = "https://adriankiller17.itch.io/"
define CREDITOS_DONAR = CREDITOS_WEB

define CREDITOS_AVISO = [
    "The Fifth Choice es un fangame no oficial y gratuito basado en Quintessential Quintuplets (五等分の花嫁), obra de Negi Haruba publicada por Kodansha. El anime es de Tezuka Productions y Bibury Animation Studios.",
    "No tiene ninguna afiliación con los titulares de la obra original, ni su autorización ni su patrocinio. Los personajes, nombres y elementos de la historia pertenecen a sus respectivos titulares.",
    "Página oficial, la única de descarga: adriankiller17.itch.io",
]

define CREDITOS_GRATIS = [
    "The Fifth Choice es y será gratuito y completo para todos. Se aceptan donaciones voluntarias para apoyar al desarrollador, pero ningún contenido, ventaja ni acceso anticipado depende de donar.",
    "Si un titular de derechos solicita su retirada, se retirará.",
]

define CREDITOS = [
    ("Desarrollo", [
        ("sub", "Guion, dirección, arte y montaje"),
        ("linea", "Adrian (AdrianKiller17)"),
    ]),
    ("Obra original", [
        ("linea", "Quintessential Quintuplets (五等分の花嫁)"),
        ("nota", "Manga de Negi Haruba, publicado por Kodansha"),
        ("nota", "Anime de Tezuka Productions y Bibury Animation Studios"),
    ]),
    ("Música", [
        ("sub", "Tema principal"),
        ("linea", "«Gotoubun no Kimochi»"),
        ("nota", "Canción original del anime, interpretada por Nakano-ke no Itsutsugo"),
        ("nota", "Cover de piano: TheChiporpoise (YouTube), usado con permiso del autor"),
        ("sub", "音楽：魔王魂 — CC BY 4.0"),
        ("linea", "ピアノ34「静寂の世界へ」"),
        ("linea", "アコースティック04"),
        ("linea", "ピアノ25「Cookie Cookie」"),
        ("linea", "ピアノ09"),
        ("sub", "DOVA-SYNDROME (OpenTracks)"),
        ("linea", "Zany Escape — Kobat"),
        ("linea", "日曜の午後 — KK"),
        ("linea", "Busy As A Bee — ハモおた"),
        ("linea", "Night Shade Story — shimtone"),
        ("linea", "Dreaming world — 蒲鉾さちこ"),
        ("linea", "Rippling heartbeat — 蒲鉾さちこ"),
        ("linea", "The calm seaside — 蒲鉾さちこ"),
        ("linea", "Fancy Pop — 蒲鉾さちこ"),
        ("linea", "Lonely Town — 蒲鉾さちこ"),
        ("linea", "New Departure — FLASH BEAT"),
        ("linea", "Mad Trick (Prod. Khaim) — KHAIM"),
        ("linea", "Blue Moon — Hayato Sadohara"),
        ("linea", "Dailyfountain — かずち"),
    ]),
    ("Efectos de sonido", [
        ("linea", "効果音ラボ (incluido 振り子時計)"),
        ("linea", "Freesound (CC0)"),
        ("linea", "Springin' Sound Stock"),
        ("nota", "Efectos adicionales generados por síntesis con scripts propios"),
    ]),
    ("Imágenes", [
        ("linea", "Ilustraciones generadas con PixAI (modelo base Tsubaki.2)"),
        ("nota", "LoRA de personaje por creadores de la comunidad de PixAI"),
        ("nota", "Composición y postproducción con herramientas propias en Python (Pillow, NumPy, SciPy) y GIMP"),
        ("linea", "Menú principal: diseño propio (Adrian)"),
        ("nota", "Logo compuesto con scripts propios a partir de los sprites del juego"),
    ]),
    ("Tipografías", [
        ("linea", "M PLUS Rounded 1c · Shippori Mincho B1 · Klee One · Noto Sans JP"),
        ("nota", "SIL Open Font License 1.1 — cada licencia va con el juego en game/fonts/"),
    ]),
    ("Motor", [
        ("linea", "Ren'Py 8.5.3 — licencia MIT"),
        ("nota", "Interfaz propia generada con scripts en Python (Pillow); algunos elementos parten de las plantillas del motor (MIT)"),
    ]),
    ("Contacto", [
        ("sub", "Página oficial (descarga solo desde aquí)"),
        ("enlace", "adriankiller17.itch.io", "https://adriankiller17.itch.io/"),
        ("sub", "Redes"),
        ("enlace", "Instagram — @thefifthchoice", "https://www.instagram.com/thefifthchoice/"),
        ("enlace", "TikTok — @thefifthchoiceo_o", "https://www.tiktok.com/@thefifthchoiceo_o"),
        ("nota", "Consultas sobre derechos o solicitudes de retirada: por cualquiera de estas vías"),
    ]),
]

## Rol: velocidad, hueco antes del logo, alto del bloque final (logo + gracias).
define CRED_VELOCIDAD = 70.0
define CRED_ESPACIO_SECCION = 90
define CRED_HUECO_FIN = 220
define CRED_FIN_ALTO = 560
define CRED_SOSTEN = 4.0
## ypos final (fracción): el bloque final queda centrado en pantalla.
define CRED_FIN_Y = (540 + CRED_FIN_ALTO / 2.0) / 1080.0
## Alto aproximado de cada tipo de línea (solo para calcular la duración).
define CRED_ALTO_LINEA = {"sub": 40, "linea": 48, "nota": 36, "enlace": 48}

## Aviso inicial: segundos sin poder saltarlo la primera vez.
define AVISO_BLOQUEO = 5.0

## Cintas de capítulo apagadas en «Continuará».
define CONT_APAGADO = "#6E6680"


init python:

    import re

    _CRED_JP = re.compile(u"([　-鿿＀-￯]+)")

    def cred_jp(s):
        """Envuelve los tramos japoneses en Noto Sans JP (las otras fuentes no los traen)."""
        return _CRED_JP.sub(u"{font=fonts/NotoSansJP-Regular.ttf}\\1{/font}", s)

    def cred_linea(l, enlaces, claro):
        """(texto, fuente, tamaño, color) de una línea de CREDITOS."""
        tipo = l[0]
        texto = cred_jp(l[1])
        if tipo == "enlace" and enlaces:
            texto = "{a=" + l[2] + "}" + texto + "{/a}"
        if tipo == "sub":
            return (texto, gui.name_text_font, 26, claro)
        if tipo == "nota":
            return (texto, gui.text_font, 24, "#BDB3D1")
        return (texto, gui.text_font, 32, "#FFF8FC")

    def creditos_duracion():
        """Segundos de subida del rol. El alto es una estimación: solo fija la velocidad;
        dónde acaba lo decide el ancla (cred_sube), con el alto real."""
        alto = CRED_HUECO_FIN + CRED_FIN_ALTO
        for s in CREDITOS:
            alto += CRED_ESPACIO_SECCION + 72 + 20
            for l in s[1]:
                alto += CRED_ALTO_LINEA[l[0]] + 12
        return (alto + 540 - CRED_FIN_ALTO / 2.0) / CRED_VELOCIDAD

    def cred_autocomprobar():
        assert cred_jp("ab 魔王魂 cd") == "ab {font=fonts/NotoSansJP-Regular.ttf}魔王魂{/font} cd"
        assert cred_jp("Ren'Py 8.5.3") == "Ren'Py 8.5.3"
        assert cred_linea(("enlace", "x", "https://a"), True, "#FFF")[0] == "{a=https://a}x{/a}"
        assert cred_linea(("enlace", "x", "https://a"), False, "#FFF")[0] == "x"
        for s in CREDITOS:
            for l in s[1]:
                assert l[0] in CRED_ALTO_LINEA, l
                assert "ChatGPT" not in l[1] and "Gemini" not in l[1], l
        assert creditos_duracion() > 20
        renpy.notify("Créditos: autocomprobación OK")
        return True


################################################################################
##  PIEZAS
################################################################################

transform cred_agua:
    zoom 4.0
    alpha 0.07

## Sube de abajo arriba: arranca con el borde de arriba en el pie de la pantalla
## y acaba con el de abajo en fin_y. Interpolar ypos y yanchor a la vez da un
## movimiento lineal con el alto real del contenido.
transform cred_sube(dur, fin_y):
    subpixel True
    xalign 0.5
    ypos 1.0 yanchor 0.0
    linear dur ypos fin_y yanchor 1.0

transform aviso_pista(espera):
    alpha 0.0
    pause espera
    linear 0.5 alpha 1.0
    block:
        linear 0.9 alpha 0.55
        linear 0.9 alpha 1.0
        repeat

## La flor de cinco pétalos de marca de agua, en el centro.
screen cred_flor_agua():
    fixed:
        xysize (160, 160)
        align (0.5, 0.5)
        at cred_agua
        use flor_sakura("todas", "hablante", 0, 0)

## Párrafos centrados (aviso, gratuidad).
screen creditos_parrafos(lista, ancho=1200, tam=28, color="#EDE7F6"):
    vbox:
        xalign 0.5
        spacing 18
        for p in lista:
            text cred_jp(p) xsize ancho xalign 0.5 text_align 0.5 size tam color color

## Todas las secciones: cinta teñida por turnos con una hermana + sus líneas.
screen creditos_cuerpo(enlaces=False, ancho=1200):
    vbox:
        xalign 0.5
        xsize ancho
        spacing CRED_ESPACIO_SECCION
        for i, s in enumerate(CREDITOS):
            $ color = PETALO_COLOR[PETALO_ORDEN[i % 5]]
            $ claro = ui_mezclar(color, "#FFFFFF", 0.45)
            vbox:
                xalign 0.5
                spacing 12
                fixed:
                    fit_first True
                    xalign 0.5
                    use cort_cinta_vista(s[0], color)
                null height 8
                for l in s[1]:
                    $ t, fuente, tam, tinta = cred_linea(l, enlaces, claro)
                    text t xsize ancho xalign 0.5 text_align 0.5 font fuente size tam color tinta


################################################################################
##  AVISO INICIAL (splashscreen)
##  Primera vez: AVISO_BLOQUEO s sin poder saltar (las cinco flores brotan como
##  cuenta atrás). Después: un clic. Sin modal (GUIA_UI §5: modal + pause cuelga).
################################################################################

screen aviso_inicial(espera):
    $ paso = 0.09
    if espera > 0:
        $ paso = espera / 4.0

    add Solid(CORT_FONDO)
    use cred_flor_agua

    vbox:
        xalign 0.5
        yalign 0.44
        spacing 48

        fixed:
            fit_first True
            xalign 0.5
            at cort_entra(0.2, -140)
            use cort_cinta_vista("Fangame no oficial", CORT_ROSA, 0.0, paso)

        vbox:
            xalign 0.5
            at cort_aparece(0.5, 0.6)
            use creditos_parrafos(CREDITOS_AVISO, 1240, 30)

    text "Haz clic para continuar":
        xalign 0.5
        ypos 960
        font HUD_FUENTE
        size 24
        kerning 4
        color "#CFC6E0"
        at aviso_pista(espera)


label splashscreen:
    scene bg_negro

    $ aviso_espera = 0.0
    if not persistent.aviso_visto:
        $ aviso_espera = AVISO_BLOQUEO

    show screen aviso_inicial(aviso_espera)
    with Dissolve(0.6)

    if aviso_espera > 0:
        $ renpy.pause(aviso_espera, hard=True)
        $ persistent.aviso_visto = True
        $ renpy.save_persistent()

    $ renpy.pause()

    hide screen aviso_inicial
    with Dissolve(0.6)
    return


################################################################################
##  ROL DE CRÉDITOS
##  Saltable (clic o cinta «Saltar») solo si ya se vio entero una vez.
################################################################################

screen creditos_rol(saltable=False):
    zorder 80

    add Solid(CORT_FONDO)
    use cred_flor_agua

    vbox:
        at cred_sube(creditos_duracion(), CRED_FIN_Y)

        use creditos_cuerpo(False, 1200)

        null height CRED_HUECO_FIN

        fixed:
            xysize (1200, CRED_FIN_ALTO)
            add "main_menu_logo" xalign 0.5 ypos 0
            text "Gracias por jugar el Capítulo 1":
                xalign 0.5
                ypos 500
                font gui.name_text_font
                size 34
                kerning 2
                color "#FFF8FC"

    if saltable:
        vbox:
            xalign 0.97
            yalign 0.95
            use cinta_boton("Saltar", Return(True), "", 220, 54, 22)


label creditos_rol:
    $ anim_marcar("creditos")
    $ cred_saltable = bool(persistent.creditos_vistos)

    scene bg_negro
    with Dissolve(0.5)

    play music main_theme fadein 2.0

    show screen creditos_rol(cred_saltable)
    with Dissolve(1.0)

    if cred_saltable:
        $ renpy.pause(creditos_duracion() + CRED_SOSTEN)
    else:
        $ renpy.pause(creditos_duracion() + CRED_SOSTEN, hard=True)

    $ persistent.creditos_vistos = True

    hide screen creditos_rol
    with Dissolve(1.0)
    return


################################################################################
##  «CONTINUARÁ» — el juego sigue en desarrollo
################################################################################

screen continuara():

    add Solid(CORT_FONDO)
    use cred_flor_agua

    ## Tres puntos, no «…»: Shippori dibuja la elipsis centrada, a la japonesa.
    text "Continuará...":
        xalign 0.5
        ypos 80
        font gui.name_text_font
        size 96
        kerning 2
        color "#FFF8FC"
        outlines [(7, "#1B1026", 0, 0), (2, ui_mezclar(CORT_ROSA, "#FFFFFF", 0.2), 0, 0)]
        at cort_aparece(0.0, 0.8)

    vbox:
        xalign 0.5
        ypos 290
        spacing 22

        fixed:
            fit_first True
            at cort_entra(0.5, -140)
            use cort_cinta_vista("Capítulo 1 · Un estudiante perfecto", CORT_ROSA, 1.0)
        fixed:
            fit_first True
            at cort_entra(0.7, -140)
            use cort_cinta_vista("Capítulo 2 · En desarrollo", CONT_APAGADO)
        fixed:
            fit_first True
            at cort_entra(0.9, -140)
            use cort_cinta_vista("Capítulo 3 · En desarrollo", CONT_APAGADO)

    vbox:
        xalign 0.5
        ypos 610
        spacing 16
        at cort_aparece(1.4, 0.6)

        text "The Fifth Choice sigue en desarrollo: faltan el Capítulo 2 y el Capítulo 3.":
            xalign 0.5
            text_align 0.5
            xsize 1400
            size 30
            color "#FFF8FC"
        text "Si te ha gustado y te apetece, puedes apoyar el desarrollo con una donación voluntaria. No hace falta: no desbloquea ni adelanta nada.":
            xalign 0.5
            text_align 0.5
            xsize 1300
            size 26
            color "#CFC6E0"
        text "El juego seguirá siendo gratis y completo para todos.":
            xalign 0.5
            text_align 0.5
            xsize 1300
            size 26
            color ui_mezclar(CORT_ROSA, "#FFFFFF", 0.4)

    hbox:
        xalign 0.5
        ypos 880
        spacing 40
        at cort_aparece(1.8, 0.6)

        use cinta_boton("Apoyar el desarrollo", OpenURL(CREDITOS_DONAR), "", 480, 64, 28)
        use cinta_boton("Volver al menú", Return(), "", 380, 64, 28)


## Final del Capítulo 1 fuera de un Replay (evento_6 salta aquí tras end_replay).
## persistent.cap1_completado ya lo marca e6_retrato antes de la tarjeta de fin.
## Cuando exista el Capítulo 2: saltar a cap2_inicio después del rol.
label cap1_continuara:
    $ quick_menu = False

    call creditos_rol from _call_creditos_rol_1

    $ renpy.block_rollback()
    call screen continuara with Dissolve(0.8)

    $ renpy.full_restart()
