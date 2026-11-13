################################################################################
##  13_transiciones.rpy — Tarjetas de capítulo y de sección ("cortinillas")
##
##  Una tarjeta se arma PIEZA POR PIEZA hasta enseñar la imagen completa:
##    franja diagonal → número → rótulo → hermanas (una por una) → título
##    → cinta → cinco flores (una por hermana)
##
##  USO (una línea por tarjeta):
##      call cortinilla(rotulo="CAPÍTULO 01", numero="01",
##                      titulo="Un estudiante perfecto", cinta="Días de tutoría",
##                      hermanas=PETALO_ORDEN, jingle="capitulo")
##      call cortinilla_hub(1)            # entrada al hub 1, 2 o 3
##      call cortinilla_hermana(destino)  # salida del hub hacia una hermana
##
##  PROBARLAS TODAS:  consola (Shift+O)  →  jump cortinilla_prueba
##
##  SONIDO: campanitas en Re mayor, una nota por hermana. Las genera
##  herramientas/generar_cortinillas.py. Si falta un .ogg la tarjeta sale muda,
##  no falla. Los tiempos de CORT_RITMOS están copiados en ese script: si
##  cambias uno, cambia el otro y regenera.
##
##  REGLA DEL PROYECTO: un clic NO adelanta un ATL. Por eso la tarjeta entera es
##  una pantalla y el guion espera con renpy.pause: un clic la corta limpia.
################################################################################

init python:
    import math

    ## Canal propio, en el mezclador de MÚSICA: es un motivo musical, no un
    ## golpe, y así no pisa ni el canal `sound` ni la pista que esté sonando.
    renpy.music.register_channel("cortinilla", "music", loop=False)

    CORT_W     = config.screen_width
    CORT_H     = config.screen_height
    CORT_ANG   = -5.0       # la franja sube hacia la derecha
    CORT_CY    = 450        # centro vertical de la franja
    CORT_ALTO  = 520        # grosor de la franja
    CORT_TAN   = math.tan(math.radians(abs(CORT_ANG)))
    CORT_FONDO = "#1B1026"  # el ciruela oscuro de la interfaz, no negro puro
    CORT_ROSA  = "#F7A8C4"
    CORT_LILA  = "#CDB9EE"
    CORT_ORO   = "#F4D03F"

    ## Segundo en que entra cada pieza. `total` = cuánto dura la tarjeta.
    CORT_RITMOS = {
        ## capítulo: con las cinco hermanas
        "largo": dict(franja=0.0, lineas=0.30, numero=0.55, rotulo=0.90,
                      hermanas=1.30, paso=0.25, titulo=2.90, cinta=3.50,
                      flores=3.75, paso_flor=0.09, cambio=4.70, total=6.4),
        ## fin de prólogo / fin de capítulo: sin hermanas, más pausado
        "medio": dict(franja=0.0, lineas=0.30, numero=0.50, rotulo=0.90,
                      hermanas=1.20, paso=0.0, titulo=1.50, cinta=2.20,
                      flores=2.50, paso_flor=0.18, cambio=3.6, total=5.4),
        ## hub: entra y sale rápido, se ve tres veces por partida
        "corto": dict(franja=0.0, lineas=0.20, numero=0.30, rotulo=0.50,
                      hermanas=0.70, paso=0.0, titulo=1.10, cinta=1.50,
                      flores=1.70, paso_flor=0.07, cambio=2.4, total=3.3),
    }

    def cort_y(x, dy=0):
        """Altura (px) de la diagonal de la franja en la columna x.
        dy desplaza la diagonal: -CORT_ALTO/2 es el borde de arriba."""
        return int(CORT_CY + dy - (x - CORT_W / 2.0) * CORT_TAN)

    def cort_rect(alto, cy, color="#ffffff"):
        """Rectángulo inclinado de lado a lado de la pantalla, centrado en cy."""
        return Fixed(
            Transform(Solid(color), xysize=(int(CORT_W * 1.4), int(alto)),
                      rotate=CORT_ANG, xalign=0.5, yalign=0.5,
                      yoffset=int(cy - CORT_H / 2.0)),
            xysize=(CORT_W, CORT_H))

    def cort_franja(fondo, color, gris=False):
        """La franja: el fondo del lugar lavado hacia el color de la tarjeta."""
        if gris:
            matriz = BrightnessMatrix(-0.08) * SaturationMatrix(0.0)
            velo = 0.0
        else:
            matriz = TintMatrix(ui_mezclar(color, "#FFFFFF", 0.35)) * SaturationMatrix(0.30)
            velo = 0.30
        capas = [
            Transform(fondo, xysize=(CORT_W, CORT_H), fit="cover", matrixcolor=matriz),
            Transform(Solid(color), xysize=(CORT_W, CORT_H), alpha=velo),
        ]
        return AlphaMask(Fixed(*capas, xysize=(CORT_W, CORT_H)),
                         cort_rect(CORT_ALTO, CORT_CY))

    def cort_tapa():
        """Todo lo que queda por debajo de la franja, del color del fondo.
        Va ENCIMA de los sprites: les da el corte en diagonal sin máscaras."""
        return cort_rect(1200, CORT_CY + CORT_ALTO / 2.0 + 600, CORT_FONDO)

    def cort_sprite(hermana, alto):
        """(ruta, zoom, px de relleno sobre la coronilla) del busto del hub."""
        d = [x for x in HUB_DESTINOS if x["hermana"] == hermana][0]
        top, bot = hub_bbox(d["sprite"])
        if d.get("coronilla") is not None:
            top = d["coronilla"]
        z = alto / float(max(1, bot - top))
        return d["sprite"], z, int(top * z)

    def cort_xs(n):
        """Centro horizontal de cada hermana."""
        if n <= 1:
            return [1400]
        ## Agrupadas a la izquierda: a la derecha tiene que verse el número.
        return [270 + int(i * 1040.0 / (n - 1)) for i in range(n)]

    def cort_sonar(jingle):
        if jingle is None:
            return
        ruta = "audio/sfx/cort_" + jingle + ".ogg"
        if renpy.loadable(ruta):
            renpy.music.play(ruta, channel="cortinilla", loop=False)


################################################################################
##  MOVIMIENTOS
################################################################################

transform cort_aparece(espera=0.0, dur=0.5, a=1.0):
    alpha 0.0
    pause espera
    linear dur alpha a

## Entra deslizándose (franja, líneas).
transform cort_entra(espera=0.0, dx=-140, dur=0.7):
    alpha 0.0 xoffset dx
    pause espera
    parallel:
        ease dur xoffset 0
    parallel:
        linear (dur * 0.6) alpha 1.0

## Texto inclinado igual que la franja. x, y en PÍXELES ENTEROS.
transform cort_texto(x, y, espera=0.0, dx=-80, xa=0.0, dur=0.5):
    subpixel True
    transform_anchor True
    rotate_pad False
    rotate CORT_ANG
    xpos x ypos y xanchor xa yanchor 0.5
    alpha 0.0 xoffset dx
    pause espera
    parallel:
        ease dur xoffset 0
    parallel:
        linear (dur * 0.7) alpha 1.0

## Igual, pero en el segundo `cambio` se va por la derecha (cinta que se releva).
transform cort_texto_sale(x, y, espera=0.0, cambio=4.0, dx=-80):
    subpixel True
    transform_anchor True
    rotate_pad False
    rotate CORT_ANG
    xpos x ypos y xanchor 0.0 yanchor 0.5
    alpha 0.0 xoffset dx
    pause espera
    parallel:
        ease 0.5 xoffset 0
    parallel:
        linear 0.35 alpha 1.0
    pause (max(0.05, cambio - espera - 0.5))
    parallel:
        ease 0.35 xoffset 260
    parallel:
        linear 0.30 alpha 0.0

## Una hermana: sube, se pasa un poco y se asienta.
transform cort_sube(espera=0.0):
    alpha 0.0 yoffset 46
    pause espera
    parallel:
        ease 0.34 yoffset -10
        ease 0.20 yoffset 0
    parallel:
        linear 0.26 alpha 1.0

## Una flor: brota.
transform cort_brota(espera=0.0):
    alpha 0.0 zoom 0.2
    pause espera
    parallel:
        linear 0.12 alpha 1.0
    parallel:
        ease 0.16 zoom 1.30
        ease 0.14 zoom 1.0


################################################################################
##  PANTALLA
################################################################################

style cort_cinta_win is default:
    ysize 72
    xminimum 360
    padding (46, 0, 92, 0)

## La cinta con su texto y, si `flores` no es None, las cinco flores detrás.
## `solo`: nombre de una hermana; las otras cuatro flores quedan apagadas.
screen cort_cinta_vista(texto, color, flores=None, paso=0.09, solo=None):

    $ claro = ui_mezclar(color, "#FFFFFF", 0.45)
    $ tinta = ui_mezclar(color, "#000000", 0.74)

    hbox:
        spacing 20

        window:
            style "cort_cinta_win"
            background Transform(Frame("ui/cort_cinta.png", 40, 0, 80, 0), matrixcolor=TintMatrix(claro))

            text texto:
                yalign 0.5
                font gui.name_text_font
                size 34
                kerning 2
                color tinta

        if flores is not None:
            hbox:
                yalign 0.5
                spacing 2
                for i, h in enumerate(PETALO_ORDEN):
                    fixed:
                        xysize (60, 60)
                        add "ui/flor.png":
                            align (0.5, 0.5)
                            matrixcolor TintMatrix(PETALO_COLOR[h] if solo in (None, h) else "#4A3D5C")
                            at cort_brota(flores + i * paso)


screen cortinilla(rotulo="", titulo="", cinta="", numero="", color="#F7A8C4",
                  fondo="bg_escuela", hermanas=(), ritmo="largo",
                  cinta_b=None, color_b=None, gris=False, solo=None):

    zorder 80

    $ t = CORT_RITMOS[ritmo]
    $ borde_arriba = CORT_CY - CORT_ALTO / 2.0
    $ borde_abajo = CORT_CY + CORT_ALTO / 2.0
    $ t_flores = t["flores"]
    if cinta_b is not None:
        $ t_flores = t["cambio"] + 0.45
    ## El final malo no lleva flores: ninguna de las cinco se encendió.
    if gris:
        $ t_flores = None

    add Solid(CORT_FONDO) at cort_aparece(0.0, 0.35)

    ## --- 1 · La franja -------------------------------------------------------
    add cort_franja(fondo, color, gris) at cort_entra(t["franja"], -160, 0.7)

    if color_b is not None:
        add cort_franja(fondo, color_b) at cort_aparece(t["cambio"], 0.6)

    ## --- 2 · El número, grande y casi transparente ---------------------------
    if numero != "":
        text numero:
            at cort_texto(1850, cort_y(1850) + 6, t["numero"], 170, 1.0, 0.6)
            font gui.name_text_font
            size 430
            color "#FFFFFF42"

    ## --- 3 · Las hermanas, una por una ---------------------------------------
    ## Línea del borde de arriba: entra por la derecha y queda DETRÁS de ellas.
    add cort_rect(5, borde_arriba - 14, ui_mezclar(color, "#FFFFFF", 0.5)) at cort_entra(t["lineas"], 420, 0.8)

    ## asoma = cuánto sobresale la coronilla por encima de la franja.
    $ alto_spr = 640
    $ asoma = 70
    if len(hermanas) == 1:
        $ alto_spr = 780
        $ asoma = 30

    for i, h in enumerate(hermanas):
        $ ruta, z, relleno = cort_sprite(h, alto_spr)
        $ x = cort_xs(len(hermanas))[i]
        add ruta:
            zoom z
            xanchor 0.5
            xpos x
            ypos (cort_y(x, -CORT_ALTO / 2.0) - asoma - relleno)
            at cort_sube(t["hermanas"] + i * t["paso"])

    ## El corte en diagonal de los bustos.
    add cort_tapa()

    ## Línea del borde de abajo: entra por la izquierda, encima del corte.
    add cort_rect(5, borde_abajo + 14, ui_mezclar(color, "#FFFFFF", 0.5)) at cort_entra(t["lineas"] + 0.1, -420, 0.8)

    ## --- 4 · Rótulo, arriba a la derecha -------------------------------------
    if rotulo != "":
        text rotulo:
            at cort_texto(1850, cort_y(1850, -CORT_ALTO / 2.0) - 50, t["rotulo"], 90, 1.0)
            font HUB_FUENTE
            size 40
            kerning 8
            color "#FFFFFF"
            outlines [(4, "#1B1026CC", 0, 0)]

    ## --- 5 · Título ----------------------------------------------------------
    text titulo:
        at cort_texto(120, cort_y(120, CORT_ALTO / 2.0) + 92, t["titulo"], -90)
        font gui.name_text_font
        size 84
        kerning 2
        color "#FFF8FC"
        outlines [(7, "#1B1026", 0, 0), (2, ui_mezclar(color, "#FFFFFF", 0.2), 0, 0)]

    ## --- 6 · Cinta + flores --------------------------------------------------
    $ cinta_y = cort_y(120, CORT_ALTO / 2.0) + 196

    if cinta_b is None:
        fixed:
            fit_first True
            at cort_texto(120, cinta_y, t["cinta"], -220)
            use cort_cinta_vista(cinta, color, t_flores, t["paso_flor"], solo)
    else:
        ## La primera cinta se va y la releva la segunda, ya con otro color.
        fixed:
            fit_first True
            at cort_texto_sale(120, cinta_y, t["cinta"], t["cambio"], -220)
            use cort_cinta_vista(cinta, color)
        fixed:
            fit_first True
            at cort_texto(120, cinta_y, t["cambio"] + 0.25, -220)
            use cort_cinta_vista(cinta_b, color_b, t_flores, t["paso_flor"])

    ## --- Pétalos por encima de todo (los mismos del menú principal) ----------
    if not gris:
        add "sakura_petals" at cort_aparece(0.3, 1.6, 0.85)


################################################################################
##  ETIQUETAS
################################################################################

default cort_qm_previo = True
default cort_d = None

## sosten: segundos extra con la tarjeta ya completa (tarjetas de FIN).
label cortinilla(rotulo="", titulo="", cinta="", numero="", color=CORT_ROSA, fondo="bg_escuela", hermanas=(), ritmo="largo", jingle=None, cinta_b=None, color_b=None, gris=False, sosten=0.0, solo=None):

    $ cort_qm_previo = quick_menu
    $ quick_menu = False
    window hide

    scene bg_negro
    with Dissolve(0.4)

    ## La música que esté sonando se aparta mientras dura la tarjeta.
    $ renpy.music.set_volume(0.25, delay=0.4, channel="music")
    $ cort_sonar(jingle)

    show screen cortinilla(rotulo, titulo, cinta, numero, color, fondo, hermanas, ritmo, cinta_b, color_b, gris, solo)

    ## Medio segundo blindado: el clic que cerró la línea anterior no se la lleva.
    $ renpy.pause(0.6, hard=True)
    $ renpy.pause(CORT_RITMOS[ritmo]["total"] - 0.6 + sosten + (CORT_RITMOS[ritmo]["cambio"] - CORT_RITMOS[ritmo]["flores"] + 1.6 if cinta_b is not None else 0.0))

    stop cortinilla fadeout 0.6
    hide screen cortinilla
    with Dissolve(0.8)

    $ renpy.music.set_volume(1.0, delay=1.0, channel="music")
    $ quick_menu = cort_qm_previo
    window auto

    return


## Entrada al hub n (1, 2 o 3).
label cortinilla_hub(n=1):

    call cortinilla(rotulo="TARDE " + str(n) + " DE 3", numero=str(n), titulo="Tarde libre", cinta="Quedan " + tiempo_restante, color=CORT_LILA, fondo="bg_escuela", ritmo="corto", jingle="hub")

    return


## Salida del hub: la tarjeta toma el color, el lugar y el número de la hermana.
label cortinilla_hermana(hermana="ichika"):

    $ cort_d = [x for x in HUB_DESTINOS if x["hermana"] == hermana][0]

    call cortinilla(rotulo="ENCUENTRO", numero=str(PETALO_ORDEN.index(hermana) + 1), titulo=cort_d["nombre"], cinta=cort_d["lugar"], color=cort_d["color"], fondo=cort_d["fondo"], hermanas=[hermana], ritmo="corto", jingle="hermana_" + hermana, solo=hermana)

    return


## Las tarjetas de capítulo, con nombre propio para no repetir argumentos.
label cortinilla_prologo_fin:
    call cortinilla(rotulo="PRÓLOGO", titulo="Cinco alumnas, cero interés", cinta="Fin del prólogo", color=CORT_LILA, fondo="bg_cuarto_mc", ritmo="medio", jingle="fin")
    return

label cortinilla_cap1_inicio:
    call cortinilla(rotulo="CAPÍTULO 01", numero="01", titulo="Un estudiante perfecto", cinta="Días de tutoría", color=CORT_ROSA, fondo="bg_escuela", hermanas=PETALO_ORDEN, ritmo="largo", jingle="capitulo")
    return

label cortinilla_cap1_examenes:
    call cortinilla(rotulo="CAPÍTULO 01", numero="01", titulo="Un estudiante perfecto", cinta="Días de tutoría", cinta_b="Semana de exámenes", color=CORT_ROSA, color_b=CORT_ORO, fondo="bg_aula", hermanas=PETALO_ORDEN, ritmo="largo", jingle="examen")
    return

label cortinilla_cap1_fin:
    call cortinilla(rotulo="CAPÍTULO 01", numero="01", titulo="Un estudiante perfecto", cinta="Fin del capítulo", color=CORT_ROSA, fondo="cg_familia", ritmo="medio", jingle="fin", sosten=4.0)
    return

## Sin sonido y en gris a propósito: el final malo se queda en silencio.
label cortinilla_final_malo:
    call cortinilla(rotulo="FINAL MALO", titulo="Despido temprano", cinta="Fin", color="#9AA7A8", fondo="bg_cuarto_mc", ritmo="medio", gris=True, sosten=4.0)
    return


## PRUEBA — consola (Shift+O): jump cortinilla_prueba
label cortinilla_prueba:

    stop music fadeout 0.5
    stop ambiente

    call cortinilla_prologo_fin
    call cortinilla_cap1_inicio
    call cortinilla_hub(1)

    call cortinilla_hermana("ichika")
    call cortinilla_hermana("nino")
    call cortinilla_hermana("miku")
    call cortinilla_hermana("yotsuba")
    call cortinilla_hermana("itsuki")

    call cortinilla_cap1_examenes
    call cortinilla_cap1_fin
    call cortinilla_final_malo

    return
