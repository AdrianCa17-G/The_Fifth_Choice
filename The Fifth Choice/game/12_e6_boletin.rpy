################################################################################
##  12_e6_boletin.rpy — Evento 6: boletín de notas, tintes y audio
##  boletin_cinco · tintes del CG de las cinco · audio
##  Los CG del Evento 6 se declaran en 02_cap1_evento6.rpy.
##  La Galería vive entera en 08_extras.rpy (GALERIA).
################################################################################

## --- Audio que el guion usa y 00_definiciones no declara ------------------------
define audio.main_theme = "audio/bgm/main_theme.ogg"
define audio.sfx_camara = "audio/sfx/camara.mp3"        ## Evento 6: foto del grupo (camara.mp3)

## --- Tintes del CG de las cinco según estado_entrada (sin arte nuevo) -----------
transform e6_tinte_superado:
    matrixcolor BrightnessMatrix(-0.05) * SaturationMatrix(0.90) * TintMatrix("#e0e6f5")

transform e6_tinte_mixto:
    matrixcolor TintMatrix("#ffffff")

transform e6_tinte_bueno:
    matrixcolor BrightnessMatrix(0.04) * SaturationMatrix(1.08) * TintMatrix("#fff0d8")

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
##  BOLETIN_CINCO — cinco tiras de papel, una por boletín (filas: quien rinde;
##  columnas: materia de cada una). La controla e6_boletin_fase desde el guion:
##    1 = las cinco tiras con todas las notas en tinta
##    2 = las notas que no son diagonal pasan a lápiz; cada «100» recibe su sello
##    3 = las tiras se van y cada sello viaja a su hoja: cinco hojas en fila
##  Muestra SOLO notas académicas, nunca afinidad (D-13). Orden: E6_ORDEN_EXAMEN.
##  zorder -5: por debajo de la caja de diálogo. Todo en y ≤ 740 (la caja, 804).
##  Regla: cada pieza tiene `on appear` = su estado final. Si se carga una partida
##  a mitad de la escena, la fase sale ya puesta; los cambios de fase animan.
##  Prueba: consola → jump boletin_cinco_prueba
################################################################################

## Tiras (fases 1 y 2): mismo ancho que la caja de diálogo, alineadas con ella.
define BOL_X = 290
define BOL_W = 1340
define BOL_Y0 = 236
define BOL_PASO = 104
define BOL_ALTO = 84
define BOL_COLX = [720, 920, 1120, 1320, 1520]
define BOL_TINTA = "#3A2A55"

## Hojas (fase 3).
define BOL_HOJA_X0 = 235
define BOL_HOJA_PASO = 300
define BOL_HOJA_Y = 190
define BOL_HOJA_W = 250
define BOL_HOJA_H = 400
define BOL_SELLO_Y = 200     # centro del sello dentro de la hoja

init python:

    def e6_notas_ejemplo():
        """Notas de prueba que cumplen I1/I2: diagonal 100, el resto entre 62 y 88."""
        notas = {}
        for i, h in enumerate(E6_ORDEN_CANON):
            notas[h] = {}
            for j, m in enumerate(E6_ORDEN_CANON):
                if i == j:
                    notas[h][m] = 100
                else:
                    notas[h][m] = 62 + (i * 7 + j * 11) % 27
        return notas

## Fases 1–2: el contenedor de las tiras.
transform bol_sale:
    on appear:
        alpha 1.0 yoffset 0
    on show:
        alpha 0.0 yoffset 0
        linear 0.5 alpha 1.0
    on hide:
        parallel:
            linear 0.5 alpha 0.0
        parallel:
            ease 0.5 yoffset 20

## Nota en tinta (fase 1) y la misma a lápiz (fase 2): fundido cruzado.
transform bol_tinta:
    on appear:
        alpha 1.0
    on show:
        alpha 0.0
        linear 0.6 alpha 1.0
    on hide:
        linear 0.6 alpha 0.0

transform bol_lapiz:
    on appear:
        alpha 0.45
    on show:
        alpha 0.0
        linear 0.6 alpha 0.45
    on hide:
        linear 0.3 alpha 0.0

## El sello golpea su «100», uno por fila. Dibujado a tamaño de hoja: en la
## celda va a 0,5 (así el texto no se emborrona al crecer en la fase 3).
transform bol_golpe(k):
    on appear:
        zoom 0.5 alpha 1.0
    on show:
        zoom 0.75 alpha 0.0
        pause (0.12 * k)
        ease 0.22 zoom 0.5 alpha 1.0
    on hide:
        alpha 0.0

## Fase 3: el sello sale de su celda y viaja a su hoja.
transform bol_viaja(x0, y0, x1, y1, k):
    on appear:
        xanchor 0.5 yanchor 0.5 xpos x1 ypos y1 zoom 1.0 alpha 1.0
    on show:
        xanchor 0.5 yanchor 0.5 xpos x0 ypos y0 zoom 0.5 alpha 1.0
        pause (0.06 * k)
        ease 0.7 xpos x1 ypos y1 zoom 1.0
    on hide:
        linear 0.3 alpha 0.0

transform bol_hoja(k):
    on appear:
        alpha 1.0
    on show:
        alpha 0.0
        pause (0.5 + 0.06 * k)
        linear 0.4 alpha 1.0
    on hide:
        linear 0.3 alpha 0.0

transform bol_detalle(k):
    on appear:
        alpha 1.0
    on show:
        alpha 0.0
        pause (0.8 + 0.06 * k)
        linear 0.3 alpha 1.0
    on hide:
        linear 0.3 alpha 0.0

## El sello de cada hermana: tinta de fondo, doble aro de su color y «100».
screen bol_sello(h):

    $ c = PETALO_COLOR[h]

    fixed:
        xysize (200, 200)
        add Transform("ui/hub_sello_fondo.png", matrixcolor=TintMatrix(c), zoom=1.25, alpha=0.15) align (0.5, 0.5)
        add Transform("ui/hub_aro.png", matrixcolor=TintMatrix(c), zoom=1.45, rotate=-8, alpha=0.95) align (0.5, 0.5)
        add Transform("ui/hub_aro.png", matrixcolor=TintMatrix(c), zoom=1.25, alpha=0.6) align (0.5, 0.5)
        text "100":
            align (0.5, 0.5)
            font gui.name_text_font
            size 72
            color ui_mezclar(c, "#000000", 0.45)

## Papel con sombra, del tamaño dado.
screen bol_papel(w, h):
    add Transform(Frame("ui/boletin_papel.png", 12, 12, 12, 12), matrixcolor=TintMatrix("#000000"), alpha=0.35):
        xpos 4
        ypos 4
        xysize (w, h)
    add Frame("ui/boletin_papel.png", 12, 12, 12, 12) xysize (w, h)

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

    ## --- Fases 1 y 2: las cinco tiras ------------------------------------------
    showif fase < 3:

        fixed at bol_sale:

            xysize (1920, 1080)

            ## Cabeceras: motivo encima del nombre de la materia
            for j, m in enumerate(E6_ORDEN_EXAMEN):
                vbox:
                    xpos BOL_COLX[j]
                    xanchor 0.5
                    ypos 142
                    spacing 4
                    add ("ui/hud_icono_" + m + ".png") matrixcolor TintMatrix(PETALO_COLOR[m]) xalign 0.5
                    text E6_MATERIA[m]:
                        xalign 0.5
                        font gui.name_text_font
                        size 28
                        kerning 2
                        color PETALO_COLOR[m]
                        outlines [(3, "#1B1026CC", 0, 0)]

            for i, h in enumerate(E6_ORDEN_EXAMEN):

                $ y = BOL_Y0 + i * BOL_PASO

                fixed:
                    xpos BOL_X
                    ypos y
                    xysize (BOL_W, BOL_ALTO)
                    use bol_papel(BOL_W, BOL_ALTO)
                    add Solid(PETALO_COLOR[h], xsize=12, ysize=60) xpos 14 ypos 12
                    add Transform("ui/flor.png", matrixcolor=TintMatrix(PETALO_COLOR[h]), zoom=0.6) xpos 44 yalign 0.5
                    text h.capitalize():
                        xpos 92
                        yalign 0.5
                        font gui.name_text_font
                        size 32
                        color BOL_TINTA

                for j, m in enumerate(E6_ORDEN_EXAMEN):

                    $ nota = str(e6_notas[h][m])

                    showif fase < 2:
                        text nota at bol_tinta:
                            xpos BOL_COLX[j]
                            xanchor 0.5
                            ypos (y + BOL_ALTO // 2)
                            yanchor 0.5
                            size 40
                            color BOL_TINTA

                    if i != j:
                        showif fase >= 2:
                            text nota at bol_lapiz:
                                xpos BOL_COLX[j]
                                xanchor 0.5
                                ypos (y + BOL_ALTO // 2)
                                yanchor 0.5
                                size 40
                                color BOL_TINTA
                    else:
                        showif fase == 2:
                            fixed at bol_golpe(i):
                                xpos BOL_COLX[j]
                                xanchor 0.5
                                ypos (y + BOL_ALTO // 2)
                                yanchor 0.5
                                xysize (200, 200)
                                use bol_sello(h)

    ## --- Fase 3: cinco hojas en fila; cada «100» viaja a la suya ------------------
    for k, h in enumerate(E6_ORDEN_EXAMEN):

        $ hx = BOL_HOJA_X0 + k * BOL_HOJA_PASO

        showif fase >= 3:
            fixed at bol_hoja(k):
                xpos hx
                ypos BOL_HOJA_Y
                xysize (BOL_HOJA_W, BOL_HOJA_H)
                use bol_papel(BOL_HOJA_W, BOL_HOJA_H)
                add Solid(PETALO_COLOR[h], xsize=BOL_HOJA_W - 40, ysize=12) xpos 20 ypos 16

        showif fase >= 3:
            fixed at bol_detalle(k):
                xpos hx
                ypos BOL_HOJA_Y
                xysize (BOL_HOJA_W, BOL_HOJA_H)
                add ("ui/hud_icono_" + h + ".png") matrixcolor TintMatrix(PETALO_COLOR[h]) xalign 0.5 ypos 44
                text E6_MATERIA[h]:
                    xalign 0.5
                    ypos 306
                    font gui.name_text_font
                    size 30
                    kerning 2
                    color BOL_TINTA
                add Transform("ui/flor.png", matrixcolor=TintMatrix(PETALO_COLOR[h]), zoom=0.5) xalign 0.5 ypos 354

    for k, h in enumerate(E6_ORDEN_EXAMEN):

        showif fase >= 3:
            fixed at bol_viaja(BOL_COLX[k], BOL_Y0 + k * BOL_PASO + BOL_ALTO // 2, BOL_HOJA_X0 + k * BOL_HOJA_PASO + BOL_HOJA_W // 2, BOL_HOJA_Y + BOL_SELLO_Y, k):
                xysize (200, 200)
                use bol_sello(h)


## PRUEBA — consola (Shift+O): jump boletin_cinco_prueba
## Notas de ejemplo: no salen de un examen jugado.
label boletin_cinco_prueba:

    $ quick_menu = False
    scene bg_aula
    with fade

    $ e6_notas = e6_notas_ejemplo()
    $ e6_boletin_fase = 1
    show screen boletin_cinco

    mc_pensamiento "Tomé la nota más alta de cada una."

    $ e6_boletin_fase = 2

    mc_pensamiento "Cinco notas perfectas en cinco materias distintas. Esa diagonal lo delata."

    $ e6_boletin_fase = 3

    mc_pensamiento "Cinco hojas en fila. Cinco notas de cien. Cada cien, de una persona distinta."

    hide screen boletin_cinco
    $ quick_menu = True

    return


## El chat del grupo vive en 15_chat_grupo.rpy (lo comparten las interc. 4 y 6 y el Evento 6).
