# ============================================================
# HUB — selección de destino (Capítulo 1)
# Estilo key visual: 5 bandas diagonales de altura completa.
#   fondo del lugar  →  velo del color  →  sprite  →  unificador
#
# Los sprites se normalizan por ALTURA REAL del archivo, así no
# importa que cada PNG mida distinto.
#
# hub_visitadas sigue declarándose SOLO en 00_definiciones.rpy.
# ============================================================

init python:
    import math

    HUB_ANG   = 10.0
    HUB_W     = config.screen_width
    HUB_H     = config.screen_height
    HUB_GAP   = 10

    # --- ANCHO DE CADA FRANJA ---------------------------------------
    # Peso relativo de cada franja, en el MISMO orden que HUB_DESTINOS
    # (Ichika, Nino, Miku, Yotsuba, Itsuki).
    #   1.0 = ancho parejo. Mas alto = franja mas ancha.
    # Los pesos se normalizan solos: siempre llenan la pantalla completa.
    # [1, 1, 1, 1, 1] = el reparto anterior (todas iguales).
    HUB_PESOS = [0.96, 1.00, 1.08, 1.00, 0.96]

    HUB_N    = len(HUB_PESOS)
    HUB_SLOT = HUB_W // HUB_N      # ancho promedio (solo referencia)

    def hub_calcular_cortes():
        """Posicion x (a media altura) donde empieza/termina cada franja."""
        suma = float(sum(HUB_PESOS))
        cortes = [0.0]
        for p in HUB_PESOS:
            cortes.append(cortes[-1] + HUB_W * p / suma)
        return cortes

    HUB_CORTES   = hub_calcular_cortes()
    HUB_SLOT_MAX = max(HUB_CORTES[i + 1] - HUB_CORTES[i] for i in range(HUB_N))

    def hub_slot_w(i):
        return HUB_CORTES[i + 1] - HUB_CORTES[i]

    def hub_slot_cx(i):
        return (HUB_CORTES[i] + HUB_CORTES[i + 1]) / 2.0

    HUB_DESPL  = int(HUB_H / 2.0 * math.tan(math.radians(abs(HUB_ANG))))
    # la "tarjeta" es del tamano de la franja MAS ANCHA; todas comparten tamano
    HUB_CARD_W = int(HUB_SLOT_MAX) + 2 * HUB_DESPL + 40

    # --- look ---
    HUB_FUENTE      = "fonts/MPLUSRounded1c-Bold.ttf"
    HUB_FUENTE_FINA = "fonts/MPLUSRounded1c-Medium.ttf"
    HUB_VELO   = 0.24
    HUB_UNIFY  = 0.10
    HUB_SOMBRA = 0.78

    # El panel sigue HUB_EXTRA px por debajo de la pantalla, todo franja de
    # color: al subir en hover no asoma el negro y la franja se ve más gruesa.
    HUB_EXTRA = 24
    # Cuánto se oscurecen las bandas SIN foco mientras otra está en hover/teclado.
    HUB_FOCO_VELO = 0.30

    # --- sello de visitada ---
    HUB_SELLO   = 128   # lado del PNG; el mismo número en generar_ui.py
    HUB_SELLO_Y = 690   # y del centro del sello (encima del nombre)

    # --- encuadre de sprites ---
    # El canvas ya está normalizado (760x930) pero el CONTENIDO no:
    # cada chica ocupa distinta porción y arranca a distinta altura.
    # Por eso medimos el bounding box opaco en vez de usar el archivo.
    HUB_CONT_ALTO = 880    # altura en px de la chica ya escalada
    HUB_CABEZA    = 150    # y donde queda la coronilla de TODAS
    HUB_GUIA      = False  # True = línea de cabeza + datos medidos

    _hub_bbox = {}

    def hub_bbox(ruta):
        """(top, bottom) del contenido NO transparente, en px del archivo.
        Se mide una sola vez y queda cacheado."""
        if ruta in _hub_bbox:
            return _hub_bbox[ruta]

        res = None
        try:
            surf = renpy.display.im.load_surface(renpy.display.im.Image(ruta))
            try:
                # camino rápido
                r = surf.get_bounding_rect(20)
                res = (r.top, r.top + r.height)
            except Exception:
                # fallback: escaneo por filas, con paso
                w, h = surf.get_size()
                top, bot = None, None
                for y in range(0, h, 3):
                    for x in range(0, w, 6):
                        if surf.get_at((x, y))[3] > 8:
                            if top is None:
                                top = y
                            bot = y
                            break
                if top is not None:
                    res = (top, bot)
        except Exception:
            res = None

        if res is None:
            # si algo falla, usamos el canvas entero: no rompe nada
            try:
                res = (0, renpy.image_size(ruta)[1])
            except Exception:
                res = (0, 930)

        _hub_bbox[ruta] = res
        return res

    def hub_sprite(ruta, escala=1.0, xoff=0, yoff=0, coronilla=None):
        """Sprite escalado por altura REAL de la chica y con la
        coronilla clavada en HUB_CABEZA. Si se pasa `coronilla` (fila
        del PNG donde esta la parte alta del pelo), se usa en vez del
        primer pixel opaco: sirve cuando un lazo, una mano o un objeto
        sobresale por encima de la cabeza."""
        top, bot = hub_bbox(ruta)
        if coronilla is not None:
            top = coronilla
        alto = max(1, bot - top)
        z = (HUB_CONT_ALTO / float(alto)) * escala
        # yoffset compensa el relleno transparente de arriba
        y = HUB_CABEZA - int(top * z) + yoff
        return Transform(ruta, zoom=z, xalign=0.5,
                         yanchor=0.0, ypos=0,
                         xoffset=xoff, yoffset=y)

    def hub_offset(y):
        return -int((y - HUB_H / 2.0) * math.tan(math.radians(HUB_ANG)))

    def hub_claro(color_hex, f=0.30):
        """
        Aclara un color hex mezclandolo hacia blanco en la fraccion f
        (0.0 = igual, 1.0 = blanco puro). Devuelve SIEMPRE un string
        hex plano ("#rrggbb"), nunca un objeto Color — asi no hay
        riesgo de que Ren'Py intente reparsear su representacion.
        """ 
        texto = color_hex.lstrip("#")
        r = int(texto[0:2], 16)
        g = int(texto[2:4], 16)
        b = int(texto[4:6], 16)

        r = int(r + (255 - r) * f)
        g = int(g + (255 - g) * f)
        b = int(b + (255 - b) * f)

        return "#{:02x}{:02x}{:02x}".format(r, g, b)    
    
    def hub_subtitulo(n):
        if n == 1:
            return "Tres tardes por delante. Empieza por quien más ganas tengas de ver."
        elif n == 2:
            return "Quedan dos tardes. Que cada una sea especial a su manera."
        else:
            return "La última tarde. Que sea una que quieras recordar."

    def hub_mask(i, borde=None):
        ancho = int((hub_slot_w(i) - HUB_GAP) * math.cos(math.radians(HUB_ANG)))
        dx = 0
        extra = 2 * HUB_DESPL + 80
        if borde == "izq":
            ancho += extra
            dx = -extra // 2
        elif borde == "der":
            ancho += extra
            dx = extra // 2
        # centrada en HUB_H / 2 (no en el alto del panel) para que la
        # diagonal no se corra con HUB_EXTRA
        return Fixed(
            Transform("#ffffff",
                      xysize=(ancho, int(HUB_H * 2.4)),
                      rotate=HUB_ANG,
                      xalign=0.5, ypos=HUB_H // 2, yanchor=0.5, xoffset=dx),
            xysize=(HUB_CARD_W, HUB_H + HUB_EXTRA),
        )

    def hub_degradado(alto, alpha_max=HUB_SOMBRA, pasos=32):
        a = 1.0 - (1.0 - alpha_max) ** (1.0 / pasos)
        capas = []
        for i in range(pasos):
            h = int(alto * (i + 1) / float(pasos))
            capas.append(Transform(Solid("#000000"),
                                   xysize=(HUB_CARD_W, h),
                                   alpha=a, yalign=1.0))
        return Fixed(*capas, xysize=(HUB_CARD_W, HUB_H))


    def hub_sombra_superior(alto=200, alpha_max=0.55, pasos=24):
        """Degradado negro que baja desde el borde superior: asegura que
        el titulo se lea sobre cualquier fondo. Misma tecnica que
        hub_degradado, pero pegado arriba."""
        a = 1.0 - (1.0 - alpha_max) ** (1.0 / pasos)
        capas = []
        for i in range(pasos):
            h = int(alto * (i + 1) / float(pasos))
            capas.append(Transform(Solid("#000000"),
                                   xysize=(HUB_W, h),
                                   alpha=a, yalign=0.0))
        return Fixed(*capas, xysize=(HUB_W, HUB_H))


    def hub_panel(i, fondo, ruta, color, escala=1.0, xoff=0, yoff=0, borde=None, coronilla=None):
        capas = [
            Transform(fondo, xysize=(HUB_CARD_W, HUB_H), fit="cover"),
            Transform(Solid(color), xysize=(HUB_CARD_W, HUB_H), alpha=HUB_VELO),
            hub_sprite(ruta, escala, xoff, yoff, coronilla),
            Transform(Solid(color), xysize=(HUB_CARD_W, HUB_H), alpha=HUB_UNIFY),
            hub_degradado(520),
            Transform(Solid(color), xysize=(HUB_CARD_W, 12 + HUB_EXTRA), ypos=HUB_H - 12),
        ]
        return AlphaMask(Fixed(*capas, xysize=(HUB_CARD_W, HUB_H + HUB_EXTRA)), hub_mask(i, borde))


    def hub_paneles():
        """Los paneles de las 5 bandas, en el orden de HUB_DESTINOS.
        mapa_hub lo llama UNA vez por apertura (default): antes se rehacían
        las ~190 capas en cada hover."""
        paneles = []
        for i, d in enumerate(HUB_DESTINOS):
            borde = None
            if i == 0:
                borde = "izq"
            elif i == HUB_N - 1:
                borde = "der"
            paneles.append(hub_panel(i, d["fondo"], d["sprite"], d["color"],
                                     d.get("escala", 1.0), d.get("xoff", 0), d.get("yoff", 0),
                                     borde, d.get("coronilla")))
        return paneles


    def hub_velos():
        """Velo negro con la forma de cada banda: apaga las que no tienen foco.
        Va ENCIMA del botón y no lo envuelve, así cambiarlo no le quita el foco."""
        velos = []
        for i in range(HUB_N):
            borde = None
            if i == 0:
                borde = "izq"
            elif i == HUB_N - 1:
                borde = "der"
            velos.append(AlphaMask(Solid("#000000", xysize=(HUB_CARD_W, HUB_H + HUB_EXTRA)),
                                   hub_mask(i, borde)))
        return velos


    def hub_flor_tarde(k, n):
        """Flor k (1 a 3) del indicador, estando en la tarde n.
        Devuelve (color, alfa, zoom). Las tardes jugadas llevan el color de la
        hermana elegida esa tarde (hub_visitadas va en orden de tarde)."""
        if k < n:
            color = "#D9D2E6"   # neutro: entrar al hub sin historial (showcase, pruebas)
            if len(hub_visitadas) >= k:
                color = PETALO_COLOR.get(hub_visitadas[k - 1], color)
            return (color, 0.95, 0.62)
        elif k == n:
            return ("#FFFFFF", 1.0, 0.80)
        else:
            return ("#FFFFFF", 0.28, 0.62)


# ------------------------------------------------------------
# Placeholders de fondo 
# ------------------------------------------------------------

image ph_bg_ensayo     = "bg/cap1_hubs/sala_ensayo.webp"
image ph_bg_comercial  = "bg/cap1_hubs/centro_comercial.webp"
image ph_bg_biblioteca = "bg/cap1_hubs/biblioteca.webp"
image ph_bg_aula       = "bg/cap1_hubs/aula_tarde.webp"
image ph_bg_pista      = "bg/cap1_hubs/pista_atletismo.webp"


# ------------------------------------------------------------
# Tabla de destinos — el ORDEN acá es el orden en pantalla
#
#   sprite = RUTA del archivo (no un nombre de imagen), porque
#            hay que poder medirlo con renpy.image_size().
#   escala = ajuste fino SOBRE la altura ya normalizada.
#            1.0 = igual que todas. 1.05 = 5% más grande.
#   yoff   = negativo la sube, positivo la baja.
# ------------------------------------------------------------
init 2 python:
    HUB_DESTINOS = [
        dict(hermana="ichika",  nombre="Ichika",  lugar="Sala de ensayo",
             fondo="ph_bg_ensayo",
             sprite="hubs/ichika_hub.png",
             color="#FFB7C5", escala=1.00, xoff=0, yoff=0),

        dict(hermana="nino",    nombre="Nino",    lugar="Centro comercial",
             fondo="ph_bg_comercial",
             sprite="hubs/nino_hub.png",
             color="#C39BD3", escala=1.00, xoff=0, yoff=0),

        dict(hermana="miku",    nombre="Miku",    lugar="Biblioteca",
             fondo="ph_bg_biblioteca",
             sprite="hubs/miku_hub.png",
             color="#5DADE2", escala=1.00, xoff=0, yoff=0),

        dict(hermana="yotsuba", nombre="Yotsuba", lugar="Pista de atletismo",
             fondo="ph_bg_pista",
             sprite="hubs/yotsuba_hub.png",
             color="#58D68D", escala=1.00, xoff=0, yoff=0, coronilla=124),

        dict(hermana="itsuki",  nombre="Itsuki",  lugar="Aula vacía",
             fondo="ph_bg_aula",
             sprite="hubs/itsuki_hub.png",
             color=C_ITSUKI, escala=1.00, xoff=0, yoff=0, coronilla=90),
    ]


# ------------------------------------------------------------
# Screen principal
# ------------------------------------------------------------
screen mapa_hub(hub_actual=1):
    tag menu
    modal True

    ## Se montan UNA vez por apertura, no en cada hover.
    default paneles = hub_paneles()
    default velos = hub_velos()
    default sombra = hub_sombra_superior(270, 0.60)

    ## Hermana con el foco (ratón o teclado). Con tooltip y no con hovered:
    ## hovered se queda pegado al cambiar de pantalla (GUIA_RENPY).
    $ foco = GetTooltip("mapa_hub")

    add "#07070a"

    fixed:
        xysize (HUB_W, HUB_H)

        for i, d in enumerate(HUB_DESTINOS):
            fixed:
                xysize (HUB_W, HUB_H)
                at hub_entrada(i)
                use destino_hub(i, d, paneles[i], velos[i], foco)

    # sombra bajo el titulo
    add sombra

    vbox:
        xalign 0.5
        ypos 20
        spacing 6
        at hub_titulo_entrada

        text "¿Con cuál quintilliza pasarás esta tarde?":
            font HUB_FUENTE
            size 54 color "#ffffff" xalign 0.5
            outlines [(3, "#000000cc", 0, 0), (0, "#00000080", 0, 4)]

        text hub_subtitulo(hub_actual):
            font HUB_FUENTE_FINA
            size 23 color "#e2e2e2" xalign 0.5
            outlines [(2, "#000000cc", 0, 0), (0, "#00000080", 0, 2)]

        use hub_indicador_tarde(hub_actual)

    # reglas de calibracion: pon HUB_GUIA = True para alinear cabezas
    if HUB_GUIA:
        add Solid("#00ff00"):
            xysize (HUB_W, 2)
            ypos HUB_CABEZA

        add Solid("#00ff0060"):
            xysize (HUB_W, 2)
            ypos (HUB_CABEZA + HUB_CONT_ALTO)
        vbox:
            xpos 10
            ypos 200
            for d in HUB_DESTINOS:
                $ _t, _b = hub_bbox(d["sprite"])
                text "[d['nombre']]: top=[_t] bot=[_b] alto=[(_b - _t)]":
                    size 18 color "#00ff00" outlines [(2, "#000", 0, 0)]

# ------------------------------------------------------------
# Indicador de tarde: tres flores + "TARDE n DE 3"
#   jugada  = color de la hermana elegida esa tarde
#   actual  = blanca y más grande
#   futura  = blanca apagada
# ------------------------------------------------------------
screen hub_indicador_tarde(n):
    hbox:
        xalign 0.5
        spacing 14

        hbox:
            yalign 0.5
            spacing 4
            for k in range(1, 4):
                $ color, alfa, zoom = hub_flor_tarde(k, n)
                fixed:
                    xysize (46, 46)
                    add "ui/flor.png" matrixcolor TintMatrix(color) alpha alfa zoom zoom align (0.5, 0.5)

        text "TARDE [n] DE 3":
            font HUD_FUENTE
            size 18 kerning 4 color "#FFFFFF" yalign 0.5
            outlines [(2, "#000000aa", 0, 0)]

# ------------------------------------------------------------
# Una banda
# ------------------------------------------------------------
screen destino_hub(indice, d, panel, velo, foco):
    $ visitada = d["hermana"] in hub_visitadas
    $ card_x = int(hub_slot_cx(indice) - HUB_CARD_W / 2.0)

    if visitada:
        $ estado = hub_visitado
    else:
        $ estado = hub_normal

    ## Con una banda en foco, las demás se apagan un poco.
    if foco is not None and foco != d["hermana"]:
        $ luz = hub_velo_on
    else:
        $ luz = hub_velo_off

    fixed:
        xysize (HUB_W, HUB_H)

        button:

            sensitive not visitada

            hover_sound audio.sfx_hhover
            activate_sound audio.sfx_hclick

            xpos card_x
            ypos 0
            xysize (HUB_CARD_W, HUB_H + HUB_EXTRA)
            background None
            focus_mask True
            tooltip d["hermana"]
            action Return(d["hermana"])
            at estado

            add panel

            vbox:
                xalign 0.5
                ypos 816
                xoffset hub_offset(870)
                spacing 0

                text d["nombre"]:
                    font HUB_FUENTE
                    size 44 color hub_claro(d["color"]) xalign 0.5 text_align 0.5
                    outlines [(5, "#000000", 0, 0), (2, "#000000", 0, 2)]

                text d["lugar"]:
                    font HUB_FUENTE_FINA
                    size 23 color "#e0e0e0" xalign 0.5 text_align 0.5
                    outlines [(4, "#000000", 0, 0)]

        ## Fuera del botón: así no le llega el gris de hub_visitado.
        if visitada:
            use hub_sello(d["hermana"], d["color"],
                          int(hub_slot_cx(indice)) + hub_offset(HUB_SELLO_Y), HUB_SELLO_Y)

        ## Velo de foco: encima de todo lo de la banda, sin foco propio (los clics pasan).
        add velo:
            xpos card_x
            ypos 0
            at luz

# ------------------------------------------------------------
# Sello de hermana visitada. Pieza aparte para la animación de
# "hub completado": pasarle otro transform en `anim` (o cambiar
# hub_sello_estado) sin tocar la banda.
#   x, y = centro del disco, en coordenadas de pantalla.
# ------------------------------------------------------------
screen hub_sello(hermana, color, x, y, anim=hub_sello_estado):
    fixed:
        xysize (HUB_SELLO + 60, HUB_SELLO + 40)
        xpos x
        ypos y
        xanchor 0.5
        yanchor (HUB_SELLO // 2)
        at anim

        fixed:
            xysize (HUB_SELLO, HUB_SELLO)
            xalign 0.5
            add "ui/hub_sello_fondo.png" matrixcolor TintMatrix("#1B1026") alpha 0.55
            add ("ui/hub_sello_" + hermana + ".png"):
                matrixcolor TintMatrix(hub_claro(color, 0.25))
                rotate HUB_ANG
                align (0.5, 0.5)

        ## la etiqueta sigue la diagonal de la banda
        text "VISITADA":
            font HUD_FUENTE
            size 16 kerning 4 color hub_claro(color, 0.55)
            xalign 0.5 yalign 1.0
            xoffset (hub_offset(y + 80) - hub_offset(y))
            outlines [(2, "#000000aa", 0, 0)]


transform hub_sello_estado:
    alpha 1.0

transform hub_normal:
    matrixcolor BrightnessMatrix(-0.06) * SaturationMatrix(0.92)
    yoffset 0
    on hover:
        linear 0.12 matrixcolor BrightnessMatrix(0.10) * SaturationMatrix(1.25) yoffset -10
    on idle:
        linear 0.12 matrixcolor BrightnessMatrix(-0.06) * SaturationMatrix(0.92) yoffset 0

## Un botón insensible no recibe hover: la visitada es un estado fijo.
transform hub_visitado:
    matrixcolor SaturationMatrix(0.12) * BrightnessMatrix(-0.22)

transform hub_velo_off:
    linear 0.15 alpha 0.0

transform hub_velo_on:
    linear 0.15 alpha HUB_FOCO_VELO

transform hub_entrada(indice):
    alpha 0.0
    yoffset 40
    pause (0.10 * indice)
    linear 0.45 alpha 1.0 yoffset 0

transform hub_titulo_entrada:
    alpha 0.0
    pause 0.35
    linear 0.5 alpha 1.0
