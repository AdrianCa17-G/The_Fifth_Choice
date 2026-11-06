################################################################################
##  12_e6_pantallas.rpy — Evento 6: pantallas, CG declarados, tintes, galería
##  boletin_cinco · chat_grupo · image cg_* (con sustituto) · GALERIA · audio
################################################################################

## --- Audio que el guion usa y 00_definiciones no declara ------------------------
define audio.main_theme = "audio/bgm/main_theme.ogg"
define audio.sfx_camara = "audio/sfx/camara.mp3"        ## [NUEVO] el guion lo reproduce solo si existe

## --- Tintes del CG de las cinco según estado_entrada (sin arte nuevo) -----------
transform e6_tinte_superado:
    matrixcolor BrightnessMatrix(-0.05) * SaturationMatrix(0.90) * TintMatrix("#e0e6f5")

transform e6_tinte_mixto:
    matrixcolor TintMatrix("#ffffff")

transform e6_tinte_bueno:
    matrixcolor BrightnessMatrix(0.04) * SaturationMatrix(1.08) * TintMatrix("#fff0d8")


################################################################################
##  CG DEL EVENTO 6 — con sustituto visible si el archivo no existe
################################################################################

define E6_CG_CARPETA = "images/cg/cap1_evento6/"

init python:

    def e6_cg_declarar(nombre, archivo):
        ruta = E6_CG_CARPETA + archivo
        if renpy.loadable(ruta):
            renpy.image(nombre, ruta)
        else:
            renpy.image(nombre, Fixed(
                Solid("#1B1026"),
                Text("CG PENDIENTE · " + nombre, size=48, color="#FFB7C5", xalign=0.5, yalign=0.5, substitute=False),
                xysize=(1920, 1080)))

    e6_cg_declarar("cg_cinco_aula", "cinco_aula.webp")
    e6_cg_declarar("cg_cinco_aprobadas", "cinco_aprobadas.webp")
    e6_cg_declarar("cg_yotsuba_examen", "yotsuba_examen.webp")
    e6_cg_declarar("cg_ichika_examen", "ichika_examen.webp")
    e6_cg_declarar("cg_nino_examen", "nino_examen.webp")
    e6_cg_declarar("cg_itsuki_examen", "itsuki_examen.webp")
    e6_cg_declarar("cg_miku_examen", "miku_examen.webp")


################################################################################
##  GALERÍA — se añaden sin tocar 08_extras.rpy (no duplica si luego descomentas)
##  Alternativa: descomentar en 08_extras las líneas "Examen · …" y "Cinco aprobadas".
################################################################################

init 10 python:

    def e6_galeria_agregar():
        extra = {
            "cap1":    [("cg_cinco_aula", "Cinco miradas"), ("cg_cinco_aprobadas", "Cinco aprobadas")],
            "yotsuba": [("cg_yotsuba_examen", "Examen · Japonés")],
            "ichika":  [("cg_ichika_examen", "Examen · Matemáticas")],
            "nino":    [("cg_nino_examen", "Examen · Inglés")],
            "itsuki":  [("cg_itsuki_examen", "Examen · Ciencias")],
            "miku":    [("cg_miku_examen", "Examen · Sociales")],
        }
        for s in GALERIA:
            if s[0] in extra:
                for item in extra[s[0]]:
                    if item not in s[3]:
                        s[3].append(item)

    e6_galeria_agregar()


################################################################################
##  TRANSFORM COMÚN (showif): aparece y desaparece con fundido
################################################################################

transform e6_aparece:
    on appear:
        alpha 1.0
    on show:
        alpha 0.0
        ease 0.8 alpha 1.0
    on hide:
        ease 0.6 alpha 0.0


################################################################################
##  BOLETIN_CINCO — matriz 5×5 (filas: quien rinde; columnas: materia de cada una)
##  Se controla con la variable e6_boletin_fase desde el guion:
##    1 = matriz completa · 2 = se apaga lo que no es diagonal · 3 = cinco «100»
##  Muestra SOLO notas académicas, nunca afinidad. Orden: E6_ORDEN_EXAMEN.
##  zorder -5: por debajo de la caja de diálogo.
################################################################################

screen boletin_cinco():

    zorder -5

    $ fase = e6_boletin_fase

    add Solid("#0B0712E8")

    text "LA CUENTA":
        xalign 0.5
        ypos 56
        font gui.name_text_font
        size 54
        kerning 8
        color "#FFF8FC"
        outlines [(5, "#1B1026CC", 0, 0)]

    ## --- Fases 1 y 2: la matriz -------------------------------------------------
    showif fase < 3:

        fixed at e6_aparece:

            xysize (1920, 1080)

            ## Cabeceras: materia de cada columna
            for j, m in enumerate(E6_ORDEN_EXAMEN):
                text E6_MATERIA[m]:
                    xpos (700 + j * 230)
                    xanchor 0.5
                    ypos 168
                    font gui.name_text_font
                    size 28
                    kerning 2
                    color PETALO_COLOR[m]
                    outlines [(3, "#1B1026CC", 0, 0)]

            for i, h in enumerate(E6_ORDEN_EXAMEN):

                text h.capitalize():
                    xpos 180
                    ypos (262 + i * 96)
                    font gui.name_text_font
                    size 32
                    color PETALO_COLOR[h]
                    outlines [(3, "#1B1026CC", 0, 0)]

                for j, m in enumerate(E6_ORDEN_EXAMEN):

                    $ nota = e6_notas[h][m]
                    $ cx = 700 + j * 230
                    $ cy = 236 + i * 96

                    if i == j:

                        showif fase >= 2:

                            fixed at e6_aparece:
                                xpos (cx - 105)
                                ypos cy
                                xysize (210, 84)
                                add Transform(Frame("ui/opcion_neutra.png", 40, 40, 40, 40), matrixcolor=TintMatrix(TARJETA_TONO[h]))
                                add Transform(Frame("ui/opcion_marco.png", 40, 40, 40, 40), matrixcolor=TintMatrix(PETALO_COLOR[h]))

                        text str(nota):
                            xpos cx
                            xanchor 0.5
                            ypos (cy + 14)
                            font gui.name_text_font
                            size 48
                            color "#FFFFFF"
                            outlines [(4, "#1B1026CC", 0, 0)]

                    else:

                        showif fase < 2:

                            text str(nota) at e6_aparece:
                                xpos cx
                                xanchor 0.5
                                ypos (cy + 18)
                                size 40
                                color "#CFC6E0"

    ## --- Fase 3: la diagonal se funde en una sola fila de cinco «100» -----------
    showif fase >= 3:

        fixed at e6_aparece:

            xysize (1920, 1080)

            for k, h in enumerate(E6_ORDEN_EXAMEN):

                fixed:
                    xpos (255 + k * 300)
                    ypos 230
                    xysize (250, 340)
                    add Transform(Frame("ui/opcion_neutra.png", 40, 40, 40, 40), matrixcolor=TintMatrix(TARJETA_TONO[h]))
                    add Transform(Frame("ui/opcion_marco.png", 40, 40, 40, 40), matrixcolor=TintMatrix(PETALO_COLOR[h]))
                    add ("ui/hud_icono_" + h + ".png") matrixcolor TintMatrix(PETALO_COLOR[h]) xalign 0.5 ypos 36
                    text "100":
                        xalign 0.5
                        ypos 108
                        font gui.name_text_font
                        size 92
                        color "#FFFFFF"
                        outlines [(5, "#1B1026CC", 0, 0)]
                    text E6_MATERIA[h]:
                        xalign 0.5
                        ypos 250
                        font gui.name_text_font
                        size 28
                        kerning 2
                        color PETALO_COLOR[h]


################################################################################
##  CHAT_GRUPO — «¡Equipo Quintillizas + Tutor!» · 6 miembros
##  Los mensajes aparecen solos, uno por segundo. MC no escribe.
##  Los mensajes consecutivos de una misma persona comparten globo (así caben).
##  Las «fotos» son boletines en miniatura: los números no se leen.
################################################################################

define E6_CHAT_FILAS = [
    ("yotsuba", True,  ["¡¡¡CIEN EN JAPONÉS!!! ¡¡¡MIREN!!!", "¡¡Manden el suyo!! ¡¡Sin trampas!!"]),
    ("ichika",  True,  ["Cien en matemáticas. Pueden aplaudir. Con moderación."]),
    ("miku",    True,  ["…Sociales: cien."]),
    ("nino",    True,  ["Que conste que no me salí."]),
    ("itsuki",  True,  ["Ciencias: cien. Es un dato, no una celebración."]),
    ("yotsuba", False, ["¡¡¡ES UNA CELEBRACIÓN!!!"]),
    ("itsuki",  False, ["Está bien. Una celebración pequeña."]),
]

screen e6_chat_foto(quien):

    $ color = PETALO_COLOR[quien]

    fixed:
        xysize (120, 76)
        add Solid("#F6EEDC")
        add Solid(color, xsize=120, ysize=14)
        add Solid("#B9B1A0", xsize=84, ysize=4) xpos 12 ypos 26
        add Solid("#B9B1A0", xsize=96, ysize=4) xpos 12 ypos 38
        add Solid("#B9B1A0", xsize=70, ysize=4) xpos 12 ypos 50
        add Transform("ui/flor.png", matrixcolor=TintMatrix("#D35443"), zoom=0.4) xpos 84 ypos 40


screen e6_chat_burbuja(quien, foto, textos):

    $ color = PETALO_COLOR[quien]

    hbox:
        spacing 14

        fixed:
            xysize (150, 56)
            add Transform("ui/flor.png", matrixcolor=TintMatrix(color), zoom=0.5) yalign 0.5
            text quien.capitalize():
                xpos 42
                yalign 0.5
                size 22
                color color

        frame:
            background Transform(Frame("ui/opcion_neutra.png", 40, 40, 40, 40), matrixcolor=TintMatrix("#3A2A55"))
            padding (22, 10, 22, 10)

            hbox:
                spacing 16

                if foto:
                    use e6_chat_foto(quien)

                vbox:
                    yalign 0.5
                    spacing 2
                    for t in textos:
                        text t:
                            size 26
                            color "#F3EEFA"
                            xmaximum 700


screen chat_grupo():

    zorder -5

    default n = 0

    timer 1.0 repeat True action If(n < len(E6_CHAT_FILAS), SetScreenVariable("n", n + 1), NullAction())

    add Solid("#0B0712E8")

    fixed:
        xalign 0.5
        ypos 36
        xysize (1180, 790)

        add Transform(Frame("ui/opcion_neutra.png", 40, 40, 40, 40), matrixcolor=TintMatrix("#2B1B3F"))
        add Transform(Frame("ui/opcion_marco.png", 40, 40, 40, 40), matrixcolor=TintMatrix("#D9D2E6"))

        text "¡Equipo Quintillizas + Tutor!":
            xpos 60
            ypos 26
            font gui.name_text_font
            size 38
            color "#FFF8FC"

        text "6 miembros":
            xpos 62
            ypos 76
            size 22
            color "#CFC6E0"

        vbox:
            xpos 50
            ypos 124
            spacing 6

            for k, fila in enumerate(E6_CHAT_FILAS):

                showif n > k:

                    hbox at e6_aparece:
                        use e6_chat_burbuja(fila[0], fila[1], fila[2])