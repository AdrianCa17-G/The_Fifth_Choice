################################################################################
##  14_progreso_chicas.rpy — Barra de progreso de las chicas (cierre de capítulo)
##
##  Muestra la afinidad de cada hermana como % = puntos × 10. SOLO LEE puntos_*:
##  aquí nunca se suma ni se escribe un punto.
##
##  USO:   call progreso_chicas            (tras call cortinilla_cap1_fin)
##  PRUEBA: consola (Shift+O) → jump progreso_chicas_prueba
################################################################################

init python:

    ## Umbral → imagen. Para estrenar un umbral basta con crear el PNG: si falta,
    ## prog_imagen usa el del umbral inferior. 10 % no tiene imagen: es la
    ## silueta con contorno (tratamiento, no archivo).
    PROG_IMAGEN = {
        "ichika": {
            0: "images/sprites/ichika_sprites/ichika_neutral.png",
            30: "images/sprites/ichika_sprites/ichika_sonriendo.png",
            60: "images/sprites/ichika_sprites/ichika_radiante.png",
            90: "images/sprites/ichika_sprites/ichika_boda.png",
            100: "images/sprites/ichika_sprites/ichika_boda_ramo.png",
        },
        "nino": {
            0: "images/sprites/nino_sprites/nino_neutral.png",
            30: "images/sprites/nino_sprites/nino_pillada.png",
            60: "images/sprites/nino_sprites/nino_radiante.png",
            90: "images/sprites/nino_sprites/nino_boda.png",
            100: "images/sprites/nino_sprites/nino_boda_ramo.png",
        },
        "miku": {
            0: "images/sprites/miku_sprites/miku_neutral.png",
            30: "images/sprites/miku_sprites/miku_animada.png",
            60: "images/sprites/miku_sprites/miku_radiante.png",
            90: "images/sprites/miku_sprites/miku_boda.png",
            100: "images/sprites/miku_sprites/miku_boda_ramo.png",
        },
        "yotsuba": {
            0: "images/sprites/yotsuba_sprites/yotsuba_neutral.png",
            30: "images/sprites/yotsuba_sprites/yotsuba_sonriendo.png",
            60: "images/sprites/yotsuba_sprites/yotsuba_radiante.png",
            90: "images/sprites/yotsuba_sprites/yotsuba_boda.png",
            100: "images/sprites/yotsuba_sprites/yotsuba_boda_ramo.png",
        },
        "itsuki": {
            0: "images/sprites/itsuki_sprites/itsuki_neutral.png",
            30: "images/sprites/itsuki_sprites/itsuki_sonriendo.png",
            60: "images/sprites/itsuki_sprites/itsuki_radiante.png",
            90: "images/sprites/itsuki_sprites/itsuki_boda.png",
            100: "images/sprites/itsuki_sprites/itsuki_boda_ramo.png",
        },
    }

    ## Flores-marca sobre la barra (sin texto: no adelantan qué hay en cada una).
    PROG_MARCAS = [30, 60, 90, 100]

    ## Tiempos (s). PROG_PASO = segundos por cada 1 % de llenado.
    PROG_ENTRA   = 0.6
    PROG_ESCALON = 0.15
    PROG_LLENADO = 1.8
    PROG_PASO    = 0.025
    PROG_RESPIRO_CALIDA = 1.4
    PROG_RESPIRO_TIBIA  = 0.8
    PROG_TOTAL_MIN = 2.4

    ## Stings de hub completado: el golpe NO está al principio del .ogg, sino en
    ## su «sello» (HUBC_RITMOS[rama]["sello"]: 1,20 s cálida, 0,70 s tibia). Se
    ## lanzan antes para que el golpe caiga en el cruce del umbral.
    ## Duración de cada .ogg: copiada de Pista(...) en j_completado
    ## (herramientas/generar_cortinillas.py). Si cambia allí, cambia aquí.
    PROG_STING_DUR = {"calida": 3.2, "tibia": 1.9}
    ## El siguiente sting puede entrar este tanto antes de que acabe el anterior,
    ## que se funde en ese tiempo en vez de cortarse.
    PROG_STING_SOLAPE = 0.6

    def prog_sonar(jingle):
        """Como cort_sonar, pero fundiendo el sting que siga sonando."""
        ruta = "audio/sfx/cort_" + jingle + ".ogg"
        if renpy.loadable(ruta):
            renpy.music.play(ruta, channel="cortinilla", loop=False, fadeout=PROG_STING_SOLAPE)

    def prog_valores():
        """Porcentaje de cada hermana, leído de puntos_* (sin escribirlos)."""
        valores = {}
        for h in PETALO_ORDEN:
            pct = getattr(store, "puntos_" + h) * 10
            pct = max(0, min(100, pct))
            valores[h] = pct
        return valores

    def prog_tratamiento(pct):
        if pct >= 30:
            return "retrato"
        if pct >= 10:
            return "contorno"
        return "silueta"

    def prog_imagen(h, pct):
        """Imagen del umbral más alto alcanzado cuyo archivo exista."""
        tabla = PROG_IMAGEN[h]
        for umbral in sorted(tabla.keys(), reverse=True):
            if umbral <= pct and renpy.loadable(tabla[umbral]):
                return tabla[umbral]
        return tabla[0]

    def prog_linea(valores):
        """Línea de tiempo de la animación, calculada una vez al abrir."""
        linea = {}
        t = PROG_LLENADO
        ## Primer segundo en que el canal cortinilla queda libre (menos el fundido).
        libre = 0.0
        for i, h in enumerate(PETALO_ORDEN):
            pct = valores[h]
            d = dict(entra=PROG_ENTRA + i * PROG_ESCALON, inicio=None, dur=0.0,
                     sting_t=None, jingle=None, cambios=[])
            if pct > 0:
                if pct >= 30:
                    rama = "calida"
                    cruce = PROG_PASO * 30
                    d["jingle"] = "completado_" + h
                    respiro = PROG_RESPIRO_CALIDA
                else:
                    rama = "tibia"
                    cruce = PROG_PASO * 10
                    d["jingle"] = "completado_" + h + "_tibia"
                    respiro = PROG_RESPIRO_TIBIA
                golpe = HUBC_RITMOS[rama]["sello"]
                ## La barra espera si el sting anterior aún no ha terminado.
                t = max(t, libre + golpe - cruce)
                d["inicio"] = t
                d["dur"] = PROG_PASO * pct
                d["sting_t"] = t + cruce - golpe
                libre = d["sting_t"] + PROG_STING_DUR[rama] - PROG_STING_SOLAPE
                anterior = prog_imagen(h, 0)
                for u in PROG_MARCAS:
                    if u <= pct:
                        ruta = prog_imagen(h, u)
                        if ruta != anterior:
                            d["cambios"].append((t + PROG_PASO * u, ruta))
                            anterior = ruta
                t = t + d["dur"] + respiro
            linea[h] = d
        linea["total"] = max(t, PROG_TOTAL_MIN)
        return linea

    ## --- Geometría (1920×1080) ------------------------------------------------
    PROG_TARJ_W    = 300
    PROG_TARJ_H    = 500
    PROG_TARJ_SEP  = 40
    PROG_TARJ_X0   = (1920 - 5 * PROG_TARJ_W - 4 * PROG_TARJ_SEP) // 2
    PROG_TARJ_Y    = 360
    PROG_RETRATO_H = 300
    PROG_NOMBRE_Y  = PROG_RETRATO_H + 12
    PROG_BARRA_W   = 260
    PROG_BARRA_X   = (PROG_TARJ_W - PROG_BARRA_W) // 2
    PROG_BARRA_Y   = 392
    PROG_PCT_Y     = 418
    PROG_APAGADO   = "#4A3D5C"
    PROG_GRIS      = "#6E6878"
    ## Centro vertical de las dos líneas diagonales (en x = 960).
    PROG_LINEA_ARRIBA = 250
    PROG_LINEA_ABAJO  = 960

    ## --- Piezas -----------------------------------------------------------
    def prog_busto(ruta):
        """Busto del sprite (mismo recorte que final_sprite), al ancho de la tarjeta."""
        return Transform(Crop((90, 0, 580, 560), ruta), zoom=PROG_TARJ_W / 580.0)

    def prog_silueta(ruta):
        return Transform(prog_busto(ruta), matrixcolor=BrightnessMatrix(-1.0))

    def prog_contorno(ruta, color):
        """Ocho copias del busto casi blancas teñidas de su color, desplazadas 4 px:
        el brillo que asoma detrás de la silueta negra. Casi blanco porque su color
        puro no se lee sobre su propio fondo lavado."""
        brillo = ui_mezclar(color, "#FFFFFF", 0.75)
        lleno = Transform(prog_busto(ruta), matrixcolor=TintMatrix(brillo) * BrightnessMatrix(1.0))
        capas = []
        for dx, dy in [(-4, -4), (0, -4), (4, -4), (-4, 0), (4, 0), (-4, 4), (0, 4), (4, 4)]:
            capas.append(Transform(lleno, xoffset=dx, yoffset=dy))
        return Fixed(*capas, fit_first=True)

    def prog_capa(d):
        """Una capa del retrato: abajo y centrada, recortada a la caja del retrato."""
        caja = Fixed(Transform(d, xalign=0.5, yalign=1.0), xysize=(PROG_TARJ_W, PROG_RETRATO_H))
        return Crop((0, 0, PROG_TARJ_W, PROG_RETRATO_H), caja)

    def prog_fondo(color, gris):
        """Fondo de la tarjeta: retrato lavado en su color + franja de datos oscura."""
        ## Apagada: gris ciruela medio. Las de 0 % no deben ser lo más brillante.
        if gris:
            color = PROG_GRIS
            claro = PROG_GRIS
        else:
            claro = ui_mezclar(color, "#FFFFFF", 0.35)
        oscuro = ui_mezclar(color, CORT_FONDO, 0.70)
        return Fixed(
            Transform(Solid(claro), xysize=(PROG_TARJ_W, PROG_RETRATO_H)),
            Transform(Solid(oscuro), xysize=(PROG_TARJ_W, PROG_TARJ_H - PROG_RETRATO_H), ypos=PROG_RETRATO_H),
            xysize=(PROG_TARJ_W, PROG_TARJ_H))

    def prog_flor(color):
        return Transform("ui/flor.png", zoom=0.34, matrixcolor=TintMatrix(color))

    def prog_pct_texto(n):
        return Text(str(n) + " %", substitute=False, font=gui.name_text_font, size=56,
                    color="#FFF8FC", outlines=[(4, "#1B1026", 0, 0)])

    def prog_cuenta(st, at, inicio, dur, pct):
        """% en vivo para DynamicDisplayable: 0 hasta `inicio`, luego sube a pct."""
        if st <= inicio:
            return prog_pct_texto(0), 0.05
        if st >= inicio + dur:
            return prog_pct_texto(pct), None
        return prog_pct_texto(int(pct * (st - inicio) / dur)), 1.0 / 30

    def prog_autocomprobar():
        """Asserts de la lógica pura. La llama progreso_chicas_prueba."""
        assert prog_tratamiento(0) == "silueta"
        assert prog_tratamiento(9) == "silueta"
        assert prog_tratamiento(10) == "contorno"
        assert prog_tratamiento(20) == "contorno"
        assert prog_tratamiento(30) == "retrato"
        assert prog_tratamiento(70) == "retrato"

        assert prog_imagen("nino", 30).endswith("nino_pillada.png")
        assert prog_imagen("miku", 100).endswith("miku_animada.png")
        assert prog_imagen("ichika", 10).endswith("ichika_neutral.png")

        L = prog_linea({"ichika": 30, "nino": 0, "miku": 10, "yotsuba": 30, "itsuki": 0})
        assert L["nino"]["inicio"] is None
        assert abs(L["ichika"]["inicio"] - 1.8) < 1e-6
        assert L["miku"]["jingle"] == "completado_miku_tibia"
        assert L["ichika"]["jingle"] == "completado_ichika"
        ## El golpe del sting (su «sello», a 1,20 s cálida / 0,70 s tibia dentro
        ## del .ogg) cae justo cuando la barra cruza el umbral.
        assert abs(L["ichika"]["sting_t"] + 1.20 - (L["ichika"]["inicio"] + 0.75)) < 1e-6
        assert abs(L["miku"]["sting_t"] + 0.70 - (L["miku"]["inicio"] + 0.25)) < 1e-6
        ## Un sting no entra hasta que el anterior casi acabó (solo el fundido de 0,6 s).
        assert L["miku"]["sting_t"] >= L["ichika"]["sting_t"] + 3.2 - 0.6 - 1e-6
        assert L["yotsuba"]["sting_t"] >= L["miku"]["sting_t"] + 1.9 - 0.6 - 1e-6
        assert abs(L["miku"]["inicio"] - 4.4) < 1e-6
        assert abs(L["yotsuba"]["inicio"] - 5.7) < 1e-6
        assert abs(L["total"] - 7.85) < 1e-6

        ceros = {"ichika": 0, "nino": 0, "miku": 0, "yotsuba": 0, "itsuki": 0}
        assert prog_linea(ceros)["total"] == 2.4

        cien = dict(ceros)
        cien["ichika"] = 100
        assert len(prog_linea(cien)["ichika"]["cambios"]) == 1

        return True


################################################################################
##  MOVIMIENTOS (todos acaban en alfa 1 / xzoom 1 / zoom 1 o en alfa 0:
##  el último fotograma es el estado estático)
################################################################################

## Sin animación: lo usa el estado estático en lugar de cort_sube y compañía.
transform prog_fijo:
    alpha 1.0

## Texto inclinado como la cortinilla, ya en su sitio (estático de cort_texto).
transform prog_texto_fijo(x, y, xa=0.0):
    subpixel True
    transform_anchor True
    rotate_pad False
    rotate CORT_ANG
    xpos x ypos y xanchor xa yanchor 0.5

transform prog_llena(espera=0.0, dur=0.5):
    xzoom 0.0
    pause espera
    linear dur xzoom 1.0

transform prog_desvanece(espera=0.0, dur=0.4):
    alpha 1.0
    pause espera
    linear dur alpha 0.0

## Imagen intermedia (60/90 si existen): entra y la releva la siguiente.
transform prog_entra_sale(espera=0.0, sale=1.0):
    alpha 0.0
    pause espera
    linear 0.4 alpha 1.0
    pause (max(0.0, sale - espera - 0.4))
    linear 0.4 alpha 0.0

## Contorno que se enciende al cruzar el 10 %.
transform prog_pulso(espera=0.0):
    alpha 0.0
    pause espera
    linear 0.15 alpha 1.0
    linear 0.20 alpha 0.5
    linear 0.30 alpha 1.0

## Igual, y se apaga cuando se revela el retrato (cruce del 30 %).
transform prog_pulso_sale(espera=0.0, sale=1.0):
    alpha 0.0
    pause espera
    linear 0.15 alpha 1.0
    linear 0.20 alpha 0.5
    linear 0.30 alpha 1.0
    pause (max(0.0, sale - espera - 0.65))
    linear 0.4 alpha 0.0

transform prog_destello(espera=0.0):
    alpha 0.0
    pause espera
    linear 0.12 alpha 0.75
    linear 0.25 alpha 0.0


################################################################################
##  PANTALLAS
################################################################################

## Una tarjeta. d = su entrada de prog_linea (solo se usa con anim=True).
screen prog_tarjeta(h, pct, d, anim):

    $ color = PETALO_COLOR[h]
    $ neutral = prog_imagen(h, 0)
    $ trat = prog_tratamiento(pct)
    $ lleno = int(PROG_BARRA_W * pct / 100.0)
    $ animada = anim and pct > 0

    ## --- Fondo y retrato -----------------------------------------------------
    if pct == 0:
        add prog_fondo(color, True)
        add prog_capa(prog_silueta(neutral))

    elif not animada:
        add prog_fondo(color, False)
        if trat == "retrato":
            add prog_capa(prog_busto(prog_imagen(h, pct)))
        else:
            add prog_capa(prog_contorno(neutral, color))
            add prog_capa(prog_silueta(neutral))

    else:
        $ t10 = d["inicio"] + PROG_PASO * 10
        add prog_fondo(color, True)
        add prog_fondo(color, False) at cort_aparece(t10, 0.3)

        if len(d["cambios"]) > 0:
            $ t30 = d["cambios"][0][0]
            add prog_capa(prog_contorno(neutral, color)) at prog_pulso_sale(t10, t30)
            add prog_capa(prog_silueta(neutral)) at prog_desvanece(t30)
            for k, cambio in enumerate(d["cambios"]):
                if k + 1 < len(d["cambios"]):
                    add prog_capa(prog_busto(cambio[1])) at prog_entra_sale(cambio[0], d["cambios"][k + 1][0])
                else:
                    add prog_capa(prog_busto(cambio[1])) at cort_aparece(cambio[0], 0.4)
                add Transform(Solid("#FFFFFF"), xysize=(PROG_TARJ_W, PROG_RETRATO_H)) at prog_destello(cambio[0])
        else:
            add prog_capa(prog_contorno(neutral, color)) at prog_pulso(t10)
            add prog_capa(prog_silueta(neutral))

    ## --- Nombre ----------------------------------------------------------------
    text h.capitalize():
        xalign 0.5
        ypos PROG_NOMBRE_Y
        font gui.name_text_font
        size 44
        color "#FFF8FC"
        outlines [(3, "#1B1026", 0, 0)]

    ## --- Barra -----------------------------------------------------------------
    fixed:
        xpos PROG_BARRA_X
        ypos PROG_BARRA_Y
        xysize (PROG_BARRA_W, 12)
        if animada:
            add Solid("#FFFFFF2A")
            add Solid(color, xsize=lleno, ysize=12) at prog_llena(d["inicio"], d["dur"])
        else:
            use barra_progreso(pct, 100, color, PROG_BARRA_W)

    ## Flores-marca: apagadas siempre debajo; la de color brota al alcanzarla.
    for m in PROG_MARCAS:
        $ fx = PROG_BARRA_X + int(PROG_BARRA_W * m / 100.0)
        add prog_flor(PROG_APAGADO):
            xpos fx
            ypos PROG_BARRA_Y + 6
            anchor (0.5, 0.5)
        if m <= pct:
            if animada:
                add prog_flor(color):
                    at cort_brota(d["inicio"] + PROG_PASO * m)
                    xpos fx
                    ypos PROG_BARRA_Y + 6
                    anchor (0.5, 0.5)
            else:
                add prog_flor(color):
                    xpos fx
                    ypos PROG_BARRA_Y + 6
                    anchor (0.5, 0.5)

    ## --- Porcentaje ------------------------------------------------------------
    if animada:
        add DynamicDisplayable(prog_cuenta, d["inicio"], d["dur"], pct):
            xalign 0.5
            ypos PROG_PCT_Y
    else:
        add prog_pct_texto(pct):
            xalign 0.5
            ypos PROG_PCT_Y

    ## --- Sting -----------------------------------------------------------------
    ## _update_screens=False: sonar no debe reiniciar la interacción.
    if animada:
        timer d["sting_t"] action Function(prog_sonar, d["jingle"], _update_screens=False)


## SIN `modal` (GUIA_UI §5): un modal se traga la pausa y el juego se cuelga.
screen progreso_chicas(valores, anim=True):

    zorder 80

    default L = prog_linea(valores)

    $ linea_color = ui_mezclar(CORT_ROSA, "#FFFFFF", 0.5)

    if anim:
        $ tr_linea_a = cort_entra(0.0, 420, 0.8)
        $ tr_linea_b = cort_entra(0.1, -420, 0.8)
        $ tr_rotulo = cort_texto(120, 118, 0.3, -80)
        $ tr_titulo = cort_texto(120, 196, 0.5, -90)
        $ tr_aviso = cort_aparece(L["total"], 0.4)
    else:
        $ tr_linea_a = prog_fijo
        $ tr_linea_b = prog_fijo
        $ tr_rotulo = prog_texto_fijo(120, 118)
        $ tr_titulo = prog_texto_fijo(120, 196)
        $ tr_aviso = prog_fijo

    add Solid(CORT_FONDO)

    add cort_rect(5, PROG_LINEA_ARRIBA, linea_color) at tr_linea_a
    add cort_rect(5, PROG_LINEA_ABAJO, linea_color) at tr_linea_b

    text "CAPÍTULO 01":
        at tr_rotulo
        font HUB_FUENTE
        size 40
        kerning 8
        color "#FFFFFF"
        outlines [(4, "#1B1026CC", 0, 0)]

    text "Cinco nombres":
        at tr_titulo
        font gui.name_text_font
        size 84
        kerning 2
        color "#FFF8FC"
        outlines [(7, "#1B1026", 0, 0), (2, ui_mezclar(CORT_ROSA, "#FFFFFF", 0.2), 0, 0)]

    for i, h in enumerate(PETALO_ORDEN):
        if anim:
            $ tr_tarjeta = cort_sube(L[h]["entra"])
        else:
            $ tr_tarjeta = prog_fijo
        fixed:
            at tr_tarjeta
            xpos PROG_TARJ_X0 + i * (PROG_TARJ_W + PROG_TARJ_SEP)
            ypos PROG_TARJ_Y
            xysize (PROG_TARJ_W, PROG_TARJ_H)
            use prog_tarjeta(h, valores[h], L[h], anim)

    text "CLIC PARA CONTINUAR":
        at tr_aviso
        xpos 1840
        xanchor 1.0
        ypos 1010
        yanchor 0.5
        font HUD_FUENTE
        size 30
        kerning 4
        color "#E8DFF5"


################################################################################
##  ETIQUETAS
################################################################################

default prog_qm_previo = True

## valores: None = leer puntos_* (partida). Un dict {hermana: %} = prueba.
label progreso_chicas(valores=None):

    if valores is None:
        $ valores = prog_valores()
        ## Extras → Animaciones la repite con los valores de la última vez
        ## (las pruebas y el propio teatro pasan `valores` y no la pisan).
        $ persistent.prog_ultimo = dict(valores)
        $ anim_marcar("cierre")

    $ prog_qm_previo = quick_menu
    $ quick_menu = False
    window hide

    ## «Transiciones» apagado en Opciones = sin animación: estado final directo.
    if preferences.transitions == 0:
        show screen progreso_chicas(valores, False)
        with Dissolve(0.4)
    else:
        show screen progreso_chicas(valores, True)
        with Dissolve(0.4)
        ## Blindado: el clic que cerró la tarjeta de fin no se la lleva.
        $ renpy.pause(0.5, hard=True)
        ## Un clic aquí salta al estado final.
        $ renpy.pause(max(0.1, prog_linea(valores)["total"] + 0.4 - 0.9))
        show screen progreso_chicas(valores, False)

    ## Clic para continuar.
    $ renpy.pause()

    stop cortinilla fadeout 0.6
    hide screen progreso_chicas
    with Dissolve(0.8)

    $ quick_menu = prog_qm_previo
    window auto

    return


## PRUEBA — consola (Shift+O): jump progreso_chicas_prueba
## Valores forzados: no lee ni escribe puntos_*.
label progreso_chicas_prueba:

    stop music fadeout 0.5
    stop ambiente
    scene bg_negro

    $ prog_autocomprobar()

    ## 1 · Todo en 0
    call progreso_chicas({"ichika": 0, "nino": 0, "miku": 0, "yotsuba": 0, "itsuki": 0})
    ## 2 · Tres cálidas
    call progreso_chicas({"ichika": 30, "nino": 0, "miku": 30, "yotsuba": 30, "itsuki": 0})
    ## 3 · Dos cálidas + una tibia
    call progreso_chicas({"ichika": 30, "nino": 30, "miku": 10, "yotsuba": 0, "itsuki": 0})
    ## 4 · Una de cada tipo (cálida, tibia, fría, no visitadas)
    call progreso_chicas({"ichika": 30, "nino": 10, "miku": 0, "yotsuba": 0, "itsuki": 0})
    ## 5 · Umbrales futuros: comprueba el respaldo de imágenes
    call progreso_chicas({"ichika": 60, "nino": 90, "miku": 100, "yotsuba": 30, "itsuki": 10})

    return
