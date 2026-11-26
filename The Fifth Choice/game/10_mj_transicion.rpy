################################################################################
##  10_mj_transicion.rpy — Entrada y salida de los minijuegos (Evento 6)
##
##  "La columna de la hermana se abre": la columna del marco entra, la chibi
##  hace su gesto y presenta el título sobre una regla horizontal; al terminar
##  todo queda EXACTAMENTE como el primer fotograma de mj_marco (velo, columna
##  y chibi neutral en MJ_CHIBI_X/Y, zoom 1.0). La salida arranca de ahí.
##
##  USO: solo desde mj_ejecutar (10_minijuegos.rpy). Ningún minijuego la llama.
##      call mj_transicion("entrada", hermana, titulo)   # una vez, antes de .intento
##      call mj_transicion("ganado",  hermana, titulo)   # antes de mj_cerrar
##      call mj_transicion("saltado", hermana, titulo)   # «Que lo haga ella»
##
##  PROBARLAS TODAS:  consola (Shift+O)  →  jump mj_transicion_prueba
##
##  REGLA DEL PROYECTO: un clic NO adelanta un ATL. Pantalla + renpy.pause:
##  un clic la corta limpia. Sin `modal` (se tragaría la pausa).
##  Sonido: cort_mj_<hermana>_<tipo>.ogg (generar_cortinillas.py), canal
##  cortinilla. Si falta, sale muda. No toca el volumen de la música.
################################################################################

## Duración de cada tipo. entrada: `recoge` = el título se recoge hacia la
## columna. ganado/saltado: `sale` = la columna sale por la izquierda.
define MJTR_RITMOS = {
    "entrada": dict(recoge=1.6, total=2.0),
    "ganado":  dict(sale=0.95, total=1.25),
    "saltado": dict(sale=0.75, total=1.05),
}

## Segundo de cada golpe por hermana. Están COPIADOS en
## herramientas/generar_cortinillas.py (RITMOS_MJTR): si cambias uno, cambia
## el otro y regenera. Algunos salen del propio ATL (se indica al lado).
define MJTR_CUES = {
    "entrada": {
        "yotsuba": dict(pasos=(0.30, 0.50, 0.70), regla=0.72, titulo=0.76),  ## pasos: mjtr_e_corre
        "ichika":  dict(telon=0.20, haz=0.55, luz=0.80, chispas=(0.90, 0.98, 1.06)),
        "nino":    dict(vuelo=0.50, titulo=0.65),
        "itsuki":  dict(caida=0.15, impacto=0.60, titulo=0.70, regla=1.20),
        "miku":    dict(tiempos=(0.35, 0.65, 0.95, 1.25)),
    },
    "ganado": {
        "yotsuba": dict(aterriza=0.42, corre=0.62),
        "ichika":  dict(reverencia=0.20, chispas=(0.30, 0.38, 0.46), destello=0.50, cierre=0.75),
        "nino":    dict(asiente=0.10, mariposas=(0.30, 0.42)),
        "itsuki":  dict(sube=0.12, brilla=0.47),
        "miku":    dict(tiempos=(0.10, 0.40, 0.70), corte=1.00),
    },
    "saltado": {"asiente": 0.25},
}

## Título en el área: centro del bloque y la regla de su color debajo.
define MJTR_TITULO_Y = 515
define MJTR_REGLA_Y = 610
define MJTR_REGLA_W = 1100
## Ichika: el foco, centrado en el cuerpo de la chibi.
define MJTR_FOCO_Y = 830
## Miku: las barras del ecualizador, sobre la cabeza (base en y 560).
define MJTR_BARRAS_Y = 560

init python:

    def mjtr_total(hermana, tipo):
        """Segundos que espera la etiqueta. Miku gana y corta en seco."""
        if tipo == "ganado" and hermana == "miku":
            return MJTR_CUES["ganado"]["miku"]["corte"] + 0.05
        return MJTR_RITMOS[tipo]["total"]


style mjtr_ante is default:
    font HUD_FUENTE
    size 24
    kerning 6
    outlines [(3, "#1B102699", 0, 0)]

style mjtr_titulo is default:
    font gui.name_text_font
    size 76
    kerning 2
    color "#FFF8FC"
    outlines [(6, "#1B1026CC", 0, 0)]


################################################################################
##  PANTALLA
################################################################################

screen mj_transicion(hermana, tipo, titulo):
    zorder 95

    $ color = PETALO_COLOR[hermana]
    $ claro = ui_mezclar(color, "#FFFFFF", 0.5)
    $ brillo = ui_mezclar(color, "#FFFFFF", 0.7)
    $ r = MJTR_RITMOS[tipo]
    $ cx = MJ_CHIBI_X

    if tipo == "entrada":

        $ c = MJTR_CUES["entrada"][hermana]
        $ recoge = r["recoge"]

        add Solid(MJ_VELO) at cort_aparece(0.0, 0.25)

        fixed:
            at mjtr_columna_entra
            add "ui/mj_columna.png" xpos 0 ypos 0
            add "ui/mj_columna_banda.png" xpos 0 ypos 0 matrixcolor TintMatrix(color)

        ## --- Detrás de la chibi ------------------------------------------------
        if hermana == "ichika":
            add Transform("ui/mj_foco.png", matrixcolor=TintMatrix(brillo)) at mjtr_foco(c["telon"], 0.45, recoge, 1.0)
            add Transform("ui/mj_foco.png", matrixcolor=TintMatrix(brillo)) at mjtr_haz(c["haz"])

        if hermana == "itsuki":
            ## halo suave y redondo: el foco de Ichika aplastado a círculo
            add Transform("ui/mj_foco.png", xzoom=0.8, yzoom=0.53, matrixcolor=TintMatrix(brillo)) at hubc_halo(cx, 820, c["impacto"])

        if hermana == "miku":
            $ t0 = c["tiempos"][0]
            for k in range(5):
                add Transform("ui/hub_barra.png", matrixcolor=TintMatrix(claro)) at mjtr_barra(cx + (k - 2) * 34, t0, HUBC_EQ[0][k], HUBC_EQ[1][k], HUBC_EQ[2][k], HUBC_EQ[3][k], 0.05)

        ## --- La chibi: acaba neutral, en su sitio, zoom 1.0 ----------------------
        $ anim = mjtr_e_corte(0.0)
        if hermana == "yotsuba":
            $ anim = mjtr_e_corre
        elif hermana == "ichika":
            $ anim = mjtr_e_revela
        elif hermana == "nino":
            $ anim = mjtr_e_sube
        elif hermana == "itsuki":
            $ anim = mjtr_e_impacto(c["impacto"])
        elif hermana == "miku":
            $ anim = mjtr_e_corte(c["tiempos"][3])
        add mj_chibi(hermana, "neutral", 1.0) at anim xpos cx ypos MJ_CHIBI_Y xanchor 0.5 yanchor 1.0

        ## --- Delante de la chibi -----------------------------------------------
        if hermana == "itsuki":
            for e in HUBC_ESTELA:
                add Transform("ui/hub_motivo_itsuki.png", matrixcolor=TintMatrix(claro)) at hubc_estrella(cx, 820, c["caida"] + e[0], c["impacto"] - c["caida"], e[1], e[2])

        ## --- El título: antetítulo, título y regla -----------------------------
        ## Cómo se descubre cada pieza (ante, título, regla).
        $ ante_t = cort_aparece(0.6, 0.2)
        $ titulo_t = mjtr_barrido(0.0, 0.01, "linear")
        $ regla_t = mjtr_regla(0.0, 0.01, "linear", recoge)
        if hermana == "yotsuba":
            ## el testigo: la regla sale disparada desde la columna
            $ ante_t = cort_aparece(c["titulo"], 0.2)
            $ titulo_t = mjtr_barrido(c["titulo"], 0.30, "easeout")
            $ regla_t = mjtr_regla(c["regla"], 0.22, "easeout", recoge)
        elif hermana == "ichika":
            ## el título está en penumbra y se enciende cuando lo cruza el haz
            $ ante_t = mjtr_enciende(c["haz"] - 0.1, c["luz"])
            $ titulo_t = mjtr_enciende(c["haz"] - 0.1, c["luz"])
            $ regla_t = mjtr_regla(c["haz"], 0.4, "ease", recoge)
        elif hermana == "nino":
            ## la mariposa vuela sobre la regla y descubre el título
            $ titulo_t = mjtr_barrido(c["titulo"], 0.6, "linear")
            $ regla_t = mjtr_regla(c["titulo"], 0.6, "linear", recoge)
        elif hermana == "itsuki":
            ## se escribe a ritmo constante y luego se subraya
            $ titulo_t = mjtr_barrido(c["titulo"], 0.55, "linear")
            $ regla_t = mjtr_regla(c["regla"], 0.25, "easeout", recoge)
        elif hermana == "miku":
            ## a tiempo: antetítulo y regla en el 2, título en el 3
            $ ante_t = cort_aparece(c["tiempos"][1], 0.01)
            $ titulo_t = cort_aparece(c["tiempos"][2], 0.01)
            $ regla_t = mjtr_regla_pulso(c["tiempos"][1], recoge)

        add Solid(color, xsize=MJTR_REGLA_W, ysize=4) at regla_t xpos (MJ_AREA_CX - MJTR_REGLA_W // 2) ypos MJTR_REGLA_Y yanchor 0.5

        vbox:
            at mjtr_recoge(recoge)
            xpos MJ_AREA_CX
            ypos MJTR_TITULO_Y
            xanchor 0.5
            yanchor 0.5
            spacing 6

            text (__("MINIJUEGO") + " · " + __(E6_MATERIA[hermana]).upper()):
                style "mjtr_ante"
                color claro
                xalign 0.5
                substitute False
                at ante_t

            ## fit_first: la copia invisible fija el tamaño; así el barrido
            ## (crop) no cambia el ancho del bloque ni lo desplaza.
            fixed:
                fit_first True
                xalign 0.5
                text __(titulo) style "mjtr_titulo" substitute False at mjtr_oculto
                text __(titulo) style "mjtr_titulo" substitute False at titulo_t

        ## --- Encima de todo ----------------------------------------------------
        if hermana == "ichika":
            for k, t in enumerate(c["chispas"]):
                $ xy = [(MJ_AREA_CX - 470, 470), (MJ_AREA_CX + 480, 450), (MJ_AREA_CX + 380, 585)][k]
                add Transform("ui/hub_motivo_ichika.png", matrixcolor=TintMatrix(brillo)) at hubc_chispa(xy[0], xy[1], t, 0.45)

        if hermana == "nino":
            add Transform("ui/hub_motivo_nino.png", matrixcolor=TintMatrix(brillo)) at mjtr_mariposa_entra(c["vuelo"])

    else:

        ## --- Salida: arranca del último fotograma del marco ---------------------
        $ ganado = (tipo == "ganado")
        $ expr = "animo"
        if ganado:
            $ expr = "feliz"
            $ c = MJTR_CUES["ganado"][hermana]

        $ velo_t = mjtr_quieto
        $ sale_t = mjtr_columna_sale(r["sale"])
        if ganado and hermana == "miku":
            ## el compás termina: todo se corta a la vez, velo incluido
            $ velo_t = mjtr_corte_seco(c["corte"])
            $ sale_t = mjtr_corte_seco(c["corte"])

        add Solid(MJ_VELO) at velo_t

        fixed:
            at sale_t
            add "ui/mj_columna.png" xpos 0 ypos 0
            add "ui/mj_columna_banda.png" xpos 0 ypos 0 matrixcolor TintMatrix(color)

            ## --- Detrás de la chibi -------------------------------------------
            if hermana == "ichika":
                if ganado:
                    add Transform("ui/mj_foco.png", matrixcolor=TintMatrix(brillo)) at mjtr_foco(0.05, 0.5, c["cierre"], 0.15)
                else:
                    add Transform("ui/mj_foco.png", matrixcolor=TintMatrix(brillo)) at mjtr_foco_apaga

            if hermana == "itsuki" and ganado:
                add Transform("ui/mj_foco.png", xzoom=0.5, yzoom=0.33, matrixcolor=TintMatrix(brillo)) at hubc_halo(cx, 520, c["brilla"])

            if hermana == "miku":
                for k in range(5):
                    if ganado:
                        add Transform("ui/hub_barra.png", matrixcolor=TintMatrix(claro)) at mjtr_barra(cx + (k - 2) * 34, c["tiempos"][0], HUBC_EQ[1][k], HUBC_EQ[2][k], HUBC_EQ[3][k], HUBC_EQ[0][k], 2.0)
                    else:
                        add Transform("ui/hub_barra.png", matrixcolor=TintMatrix(claro)) at mjtr_barra(cx + (k - 2) * 34, MJTR_CUES["saltado"]["asiente"], HUBC_EQ[0][k] * 0.6, 0.25, 0.25, 0.25, 2.0)

            ## --- La chibi -------------------------------------------------------
            $ anim = mjtr_asiente(MJTR_CUES["saltado"]["asiente"])
            if ganado:
                if hermana == "yotsuba":
                    $ anim = mjtr_g_corre(c["aterriza"], c["corre"])
                elif hermana == "ichika":
                    $ anim = mjtr_g_reverencia(c["reverencia"], c["cierre"])
                elif hermana == "nino":
                    $ anim = mjtr_g_asiente(c["asiente"])
                elif hermana == "itsuki":
                    $ anim = mjtr_salto(c["brilla"])
                elif hermana == "miku":
                    $ anim = mjtr_mece(c["tiempos"][0])
            add mj_chibi(hermana, expr, 1.0) at anim xpos cx ypos MJ_CHIBI_Y xanchor 0.5 yanchor 1.0

            ## --- Delante de la chibi --------------------------------------------
            if hermana == "yotsuba":
                if ganado:
                    for k, xy in enumerate([(70, 560), (135, 500), (225, 500), (290, 560)]):
                        add Transform("ui/hub_motivo_yotsuba.png", zoom=0.45, matrixcolor=TintMatrix(claro)) at cort_brota(c["aterriza"] + k * 0.06) xpos xy[0] ypos xy[1] xanchor 0.5 yanchor 0.5
                else:
                    add Transform("ui/hub_motivo_yotsuba.png", zoom=0.45, matrixcolor=TintMatrix(claro)) at mjtr_cae(300, 640, 1040, 0.2)

            if hermana == "ichika" and ganado:
                for k, t in enumerate(c["chispas"]):
                    $ xy = [(60, 620), (300, 580), (180, 520)][k]
                    add Transform("ui/hub_motivo_ichika.png", matrixcolor=TintMatrix(brillo)) at hubc_chispa(xy[0], xy[1], t, 0.45)
                add Transform("ui/hub_motivo_ichika.png", matrixcolor=TintMatrix(brillo)) at hubc_destello(cx, 600, c["destello"])

            if hermana == "nino":
                if ganado:
                    add Transform("ui/hub_motivo_nino.png", matrixcolor=TintMatrix(brillo)) at mjtr_mariposa_vuela(250, 700, c["mariposas"][0], 560, -620, 0.75, 5)
                    add Transform("ui/hub_motivo_nino.png", matrixcolor=TintMatrix(brillo)) at mjtr_mariposa_vuela(130, 720, c["mariposas"][1], 460, -700, 0.75, 5)
                else:
                    add Transform("ui/hub_motivo_nino.png", matrixcolor=TintMatrix(brillo)) at mjtr_mariposa_vuela(-40, 560, 0.1, 520, -120, 0.7, 5)

            if hermana == "itsuki":
                if ganado:
                    add Transform("ui/hub_motivo_itsuki.png", matrixcolor=TintMatrix(claro)) at mjtr_estrella_sube(c["sube"])
                    add "ui/hub_motivo_itsuki.png" matrixcolor TintMatrix(brillo) at hubc_brillo(cx, 520, c["brilla"])
                else:
                    add Transform("ui/hub_motivo_itsuki.png", zoom=0.4, matrixcolor=TintMatrix(claro)) at cort_aparece(0.15, 0.3, 0.45) xpos cx ypos 540 xanchor 0.5 yanchor 0.5


################################################################################
##  MOVIMIENTOS
################################################################################

transform mjtr_quieto:
    alpha 1.0

transform mjtr_oculto:
    alpha 0.0

## --- Columna ---------------------------------------------------------------
transform mjtr_columna_entra:
    xoffset -420
    ease 0.35 xoffset 0

transform mjtr_columna_sale(sale):
    xoffset 0
    pause sale
    easein 0.3 xoffset -440

transform mjtr_corte_seco(t):
    alpha 1.0
    pause t
    alpha 0.0

## --- Título ----------------------------------------------------------------
## Barrido de izquierda a derecha (crop relativo). w = nombre del warper.
transform mjtr_barrido(espera, dur, w):
    crop (0, 0, 0.001, 1.0)
    pause espera
    warp renpy.atl.warpers[w] dur crop (0, 0, 1.0, 1.0)

## Ichika: en penumbra y luego encendido.
transform mjtr_enciende(tenue, luz):
    alpha 0.0
    pause tenue
    linear 0.15 alpha 0.15
    pause (luz - tenue - 0.15)
    linear 0.2 alpha 1.0

## El bloque del título se recoge: sube y se apaga.
transform mjtr_recoge(recoge):
    pause recoge
    ease 0.3 yoffset -16 alpha 0.0

## La regla crece desde la columna (anclada a la izquierda) y se repliega hacia ella.
transform mjtr_regla(espera, dur, w, recoge):
    xzoom 0.001
    pause espera
    warp renpy.atl.warpers[w] dur xzoom 1.0
    pause (recoge - espera - dur)
    easein 0.3 xzoom 0.001

## Miku: aparece en un tiempo y late en los dos siguientes (0,3 s por tiempo).
transform mjtr_regla_pulso(espera, recoge):
    xzoom 0.001
    pause espera
    xzoom 1.0 yzoom 3.0
    ease 0.25 yzoom 1.0
    pause 0.05
    yzoom 3.0
    ease 0.25 yzoom 1.0
    pause 0.05
    yzoom 3.0
    ease 0.25 yzoom 1.0
    pause (recoge - espera - 0.9)
    easein 0.3 xzoom 0.001

## --- Chibi: entradas (todas acaban en offset 0, alfa 1, zoom 1, sin giro) ---
## Yotsuba: entra corriendo, tres botes (aterriza en 0.3, 0.5, 0.7) y frena.
transform mjtr_e_corre:
    xoffset -420 yoffset 0
    pause 0.1
    parallel:
        linear 0.6 xoffset 10
        ease 0.12 xoffset 0
    parallel:
        block:
            easeout 0.1 yoffset -22
            easein 0.1 yoffset 0
            repeat 3

## Ichika: el foco la descubre (0.2) y hace una reverencia (1.15).
transform mjtr_e_revela:
    alpha 0.0 yoffset 0
    pause 0.2
    linear 0.3 alpha 1.0
    pause 0.65
    ease 0.14 yoffset 10
    ease 0.2 yoffset 0

## Nino: sube decidida y se asienta con un «hmph».
transform mjtr_e_sube:
    transform_anchor True
    rotate_pad False
    alpha 0.0 yoffset 140 rotate -4
    pause 0.15
    parallel:
        easeout 0.3 yoffset 0
    parallel:
        linear 0.15 alpha 1.0
    ease 0.15 rotate 0
    rotate None

## Itsuki: aparece con el impacto de la estrella.
transform mjtr_e_impacto(espera):
    alpha 0.0 zoom 0.85
    pause espera
    parallel:
        linear 0.08 alpha 1.0
    parallel:
        easeout 0.25 zoom 1.0

## Miku: de golpe, en el tiempo 4.
transform mjtr_e_corte(espera):
    alpha 0.0 zoom 1.04
    pause espera
    alpha 1.0
    linear 0.1 zoom 1.0

## --- Chibi: salidas ----------------------------------------------------------
## Yotsuba: salto, y sale corriendo por la derecha (botes en .77, .92, 1.07).
## 2400: la columna se la lleva 440 a la izquierda al salir; tiene que seguir fuera.
transform mjtr_g_corre(aterriza, corre):
    pause (aterriza - 0.32)
    easeout 0.16 yoffset -60
    easein 0.16 yoffset 0
    pause (corre - aterriza)
    parallel:
        easein 0.45 xoffset 2400
    parallel:
        block:
            easeout 0.075 yoffset -18
            easein 0.075 yoffset 0
            repeat 3

## Ichika: reverencia y el foco se cierra sobre ella.
transform mjtr_g_reverencia(espera, cierre):
    pause espera
    ease 0.14 yoffset 12
    ease 0.2 yoffset 0
    pause (cierre - espera - 0.34)
    linear 0.3 alpha 0.0

## Nino: asiente satisfecha.
transform mjtr_g_asiente(espera):
    transform_anchor True
    rotate_pad False
    pause espera
    ease 0.12 rotate -5 yoffset 4
    ease 0.2 rotate 0 yoffset 0
    rotate None

transform mjtr_salto(espera):
    pause espera
    easeout 0.15 yoffset -18
    easein 0.17 yoffset 0

## Miku: se mece en cada tiempo (0,3 s).
transform mjtr_mece(espera):
    pause espera
    block:
        easeout 0.06 yoffset 8
        ease 0.24 yoffset 0
        repeat 3

## Saltado: asiente.
transform mjtr_asiente(espera):
    pause espera
    ease 0.15 yoffset 6
    ease 0.15 yoffset 0

## --- Motivos -----------------------------------------------------------------
## Ichika: foco detrás de la chibi. cierre = se apaga (zfin < 1: se cierra en iris).
transform mjtr_foco(espera, a, cierre, zfin):
    xpos MJ_CHIBI_X ypos MJTR_FOCO_Y xanchor 0.5 yanchor 0.5
    alpha 0.0 zoom 1.0
    pause espera
    linear 0.25 alpha a
    pause (cierre - espera - 0.25)
    parallel:
        ease 0.3 zoom zfin
    parallel:
        linear 0.3 alpha 0.0

transform mjtr_foco_apaga:
    xpos MJ_CHIBI_X ypos MJTR_FOCO_Y xanchor 0.5 yanchor 0.5
    alpha 0.35
    pause 0.1
    linear 0.6 alpha 0.0

## Ichika: el haz cruza el área a la altura del título.
transform mjtr_haz(espera):
    xpos MJ_AREA_X ypos MJTR_TITULO_Y xanchor 0.5 yanchor 0.5
    zoom 0.9 alpha 0.0
    pause espera
    parallel:
        linear 0.1 alpha 0.35
        pause 0.3
        linear 0.1 alpha 0.0
    parallel:
        linear 0.5 xoffset MJ_AREA_W

## Miku: una barra que late en cuatro tiempos (0,3 s) y se apaga tras `fuera`.
transform mjtr_barra(x, espera, h1, h2, h3, h4, fuera):
    xpos x ypos MJTR_BARRAS_Y xanchor 0.5 yanchor 1.0
    alpha 0.0 yzoom 0.1
    pause espera
    alpha 0.9 yzoom h1
    ease 0.3 yzoom 0.25
    yzoom h2
    ease 0.3 yzoom 0.25
    yzoom h3
    ease 0.3 yzoom 0.25
    yzoom h4
    ease 0.3 yzoom 0.25
    pause fuera
    linear 0.3 alpha 0.0

## Nino (entrada): sale de su hombro, recorre la regla (x 610 → 1710) y se va.
transform mjtr_mariposa_entra(espera):
    xpos 260 ypos 700 xanchor 0.5 yanchor 0.5
    zoom 0.55 alpha 0.0
    pause espera
    parallel:
        linear 0.1 alpha 1.0
        pause 0.85
        linear 0.3 alpha 0.0
    parallel:
        ease 0.15 xoffset 350 yoffset (MJTR_REGLA_Y - 50 - 700)
        linear 0.6 xoffset 1450
        easein 0.3 xoffset 1620 yoffset -320
    parallel:
        block:
            linear 0.07 xzoom 0.35
            linear 0.07 xzoom 1.0
            repeat 8

## Nino (salida): vuela de (x, y) a (x + dx, y + dy) aleteando y se apaga.
transform mjtr_mariposa_vuela(x, y, espera, dx, dy, dur, aleteos):
    xpos x ypos y xanchor 0.5 yanchor 0.5
    zoom 0.5 alpha 0.0
    pause espera
    parallel:
        linear 0.1 alpha 1.0
        pause (dur - 0.3)
        linear 0.2 alpha 0.0
    parallel:
        ease dur xoffset dx
    parallel:
        easein dur yoffset dy
    parallel:
        block:
            linear 0.07 xzoom 0.35
            linear 0.07 xzoom 1.0
            repeat aleteos

## Itsuki (ganado): la estrella sube de la chibi a encima de su cabeza.
transform mjtr_estrella_sube(espera):
    xpos MJ_CHIBI_X ypos 820 xanchor 0.5 yanchor 0.5
    zoom 0.5 alpha 0.0 rotate 0
    pause espera
    parallel:
        linear 0.1 alpha 1.0
    parallel:
        easeout 0.35 yoffset -300
    parallel:
        linear 0.35 rotate 72
    linear 0.08 alpha 0.0

## Yotsuba (saltado): un trébol cae a sus pies y se queda.
transform mjtr_cae(x, y0, y1, espera):
    xpos x ypos y0 xanchor 0.5 yanchor 0.5
    alpha 0.0 rotate 0
    pause espera
    parallel:
        linear 0.1 alpha 0.9
    parallel:
        easein 0.35 yoffset (y1 - y0)
    parallel:
        linear 0.35 rotate 30


################################################################################
##  ETIQUETAS
################################################################################

label mj_transicion(tipo="entrada", h="ichika", titulo=""):

    $ anim_marcar("mj_" + h + "_" + tipo)
    window hide

    ## Las salidas parten del marco (o del menú de «Que lo haga ella»): fundido corto.
    if tipo != "entrada":
        $ renpy.transition(Dissolve(0.2))

    $ cort_sonar("mj_" + h + "_" + tipo)
    show screen mj_transicion(h, tipo, titulo)

    ## Blindado: el clic que cerró la última línea no se la lleva.
    $ renpy.pause(0.3, hard=True)
    $ renpy.pause(mjtr_total(h, tipo) - 0.3)

    stop cortinilla fadeout 0.5
    hide screen mj_transicion

    if tipo == "entrada":
        ## Columna y chibi coinciden con el marco: solo entran HUD, cinta y panel.
        ## (Si se cortó con un clic, el fundido recoge lo que estuviera a medias.)
        $ renpy.transition(Dissolve(0.25))
    else:
        with Dissolve(0.4)
        window auto

    return


## PRUEBA — consola (Shift+O): jump mj_transicion_prueba
## Por hermana: entrada → marco quieto → salida ganado → salida saltado.
screen mj_transicion_prueba_marco(hermana, expresion):
    zorder 95
    use mj_marco(hermana, MJ_REGISTRO[E6_MJ_JUEGO[hermana]]["titulo"], chibi=expresion):
        null

default mjtr_qm_previo = True

label mj_transicion_prueba:

    $ mjtr_qm_previo = quick_menu
    $ quick_menu = False
    stop ambiente

    call mj_transicion_prueba_una("ichika") from _call_mj_transicion_prueba_una
    call mj_transicion_prueba_una("nino") from _call_mj_transicion_prueba_una_1
    call mj_transicion_prueba_una("miku") from _call_mj_transicion_prueba_una_2
    call mj_transicion_prueba_una("yotsuba") from _call_mj_transicion_prueba_una_3
    call mj_transicion_prueba_una("itsuki") from _call_mj_transicion_prueba_una_4

    stop music fadeout 1.0
    $ quick_menu = mjtr_qm_previo

    return

label mj_transicion_prueba_una(h="ichika"):

    $ renpy.scene()
    $ renpy.show(MJ_PRUEBA_FONDO[h])
    with Dissolve(0.4)
    $ renpy.music.play(getattr(audio, h), channel="music", fadein=0.5)

    call mj_transicion("entrada", h, MJ_REGISTRO[E6_MJ_JUEGO[h]]["titulo"]) from _call_mj_transicion_6
    show screen mj_transicion_prueba_marco(h, "neutral")
    $ renpy.pause(1.2, hard=True)
    show screen mj_transicion_prueba_marco(h, "feliz")
    $ renpy.pause(0.4, hard=True)
    hide screen mj_transicion_prueba_marco

    call mj_transicion("ganado", h, MJ_REGISTRO[E6_MJ_JUEGO[h]]["titulo"]) from _call_mj_transicion_7
    $ renpy.pause(0.8, hard=True)
    call mj_transicion("saltado", h, MJ_REGISTRO[E6_MJ_JUEGO[h]]["titulo"]) from _call_mj_transicion_8
    $ renpy.pause(0.8, hard=True)

    return
