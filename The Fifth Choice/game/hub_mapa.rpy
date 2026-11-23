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
            return _("Tres tardes por delante. Empieza por quien más ganas tengas de ver.")
        elif n == 2:
            return _("Quedan dos tardes. Que cada una sea especial a su manera.")
        else:
            return _("La última tarde. Que sea una que quieras recordar.")

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
                h = hub_visitadas[k - 1]
                if h in PETALO_COLOR:
                    color = hub_tono(h, rama_de(h))
            return (color, 0.95, 0.62)
        elif k == n:
            return ("#FFFFFF", 1.0, 0.80)
        else:
            return ("#FFFFFF", 0.28, 0.62)


    def hub_tono(hermana, rama):
        """Color del sello y de la flor de tarde de una hermana según su rama.
        Cálida = su color; tibia = pálido; fría = gris. Sin rama (showcase,
        pruebas) = su color, como antes. Lo usan el mapa y hub_completado."""
        color = PETALO_COLOR[hermana]
        if rama == "tibia":
            return ui_mezclar(color, "#D9D2E6", 0.55)
        elif rama == "fria":
            return "#8E8A96"
        return color


    ## --- Hub completado ------------------------------------------------------
    ## Segundo en que entra cada pieza. Los de `sello` y `flor` están copiados
    ## en herramientas/generar_cortinillas.py (RITMOS_HUBC): cambia los dos.
    ##   banda: se enciende la banda (sat/luz/sube = cómo queda; velo = alfa final)
    ##   motivo: arranca el gesto de la hermana (None = sin motivo)
    ##   total: cuánto dura antes del fundido a negro
    HUBC_RITMOS = {
        "calida": dict(banda=0.20, sat=1.25, luz=0.10, sube=-10, velo=0.0,
                       motivo=0.40, sello=1.20, flor=1.55, pico=1.3, total=2.8),
        "tibia":  dict(banda=0.15, sat=0.55, luz=-0.04, sube=-5, velo=HUB_FOCO_VELO * 0.5,
                       motivo=0.25, sello=0.70, flor=0.95, pico=1.3, total=1.5),
        "fria":   dict(banda=0.0, sat=0.12, luz=-0.22, sube=0, velo=HUB_FOCO_VELO,
                       motivo=None, sello=0.15, flor=0.30, pico=1.0, total=0.6),
    }

    ## Velo de las bandas que no son de esta tarde (más oscuro que el foco del
    ## mapa, HUB_FOCO_VELO: aquí la única banda que cuenta es la de la hermana).
    HUBC_VELO_OTRAS = 0.5

    HUBC_TAN = math.tan(math.radians(HUB_ANG))
    HUBC_COS = math.cos(math.radians(HUB_ANG))
    HUBC_SIN = math.sin(math.radians(HUB_ANG))
    ## yanchor del centro del disco dentro de hub_sello, en fracción: así el
    ## zoom del estampado crece desde el centro del sello y no desde su borde.
    HUBC_SELLO_YA = (HUB_SELLO / 2.0) / (HUB_SELLO + 40)

    ## Ichika: dónde brotan los tres destellos, respecto al centro del sello.
    HUBC_CHISPAS = [(-78, -40), (72, -86), (-14, -112)]
    ## Miku: altura de cada barra en sus tres pulsos y al asentarse (= el motivo).
    HUBC_EQ = [
        [0.70, 1.00, 0.50, 0.85, 0.60],
        [0.45, 0.75, 1.00, 0.60, 0.90],
        [0.90, 0.60, 0.80, 1.00, 0.50],
        [0.50, 0.90, 0.65, 1.00, 0.55],
    ]
    ## Itsuki: la estela, (retraso, alfa, zoom) de cada copia.
    HUBC_ESTELA = [(0.0, 1.0, 0.60), (0.05, 0.45, 0.50), (0.10, 0.20, 0.42)]

    def hubc_jingle(hermana, rama):
        if rama == "fria":
            return "completado_fria"
        elif rama == "tibia":
            return "completado_" + hermana + "_tibia"
        return "completado_" + hermana


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
        dict(hermana="ichika",  nombre=_("Ichika"),  lugar=_("Sala de ensayo"),
             fondo="ph_bg_ensayo",
             sprite="hubs/ichika_hub.png",
             color="#FFB7C5", escala=1.00, xoff=0, yoff=0),

        dict(hermana="nino",    nombre=_("Nino"),    lugar=_("Centro comercial"),
             fondo="ph_bg_comercial",
             sprite="hubs/nino_hub.png",
             color="#C39BD3", escala=1.00, xoff=0, yoff=0),

        dict(hermana="miku",    nombre=_("Miku"),    lugar=_("Biblioteca"),
             fondo="ph_bg_biblioteca",
             sprite="hubs/miku_hub.png",
             color="#5DADE2", escala=1.00, xoff=0, yoff=0),

        dict(hermana="yotsuba", nombre=_("Yotsuba"), lugar=_("Pista de atletismo"),
             fondo="ph_bg_pista",
             sprite="hubs/yotsuba_hub.png",
             color="#58D68D", escala=1.00, xoff=0, yoff=0, coronilla=124),

        dict(hermana="itsuki",  nombre=_("Itsuki"),  lugar=_("Aula vacía"),
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

    ## En táctil no hay hover: el foco es la hermana tocada una vez.
    on "show" action SetVariable("hub_toque", None)
    if renpy.variant("touch") and hub_toque is not None:
        $ foco = hub_toque

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

        text _("¿Con cuál quintilliza pasarás esta tarde?"):
            font HUB_FUENTE
            size 54 color "#ffffff" xalign 0.5
            outlines [(3, "#000000cc", 0, 0), (0, "#00000080", 0, 4)]

        text hub_subtitulo(hub_actual):
            font HUB_FUENTE_FINA
            size 23 color "#e2e2e2" xalign 0.5
            outlines [(2, "#000000cc", 0, 0), (0, "#00000080", 0, 2)]

        use hub_indicador_tarde(hub_actual)

        if renpy.variant("touch") and hub_toque is not None:
            text _("Vuelve a tocar para confirmar"):
                font HUB_FUENTE_FINA
                size 23 color "#ffffff" xalign 0.5
                outlines [(2, "#000000cc", 0, 0), (0, "#00000080", 0, 2)]

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
##   marca = segundo en que la flor de la tarde n se tiñe de marca_color
##   (hub_completado). None = el indicador quieto del mapa.
screen hub_indicador_tarde(n, marca=None, marca_color="#FFFFFF", marca_pico=1.3):
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
                    if k == n and marca is not None:
                        add "ui/flor.png" matrixcolor TintMatrix(color) alpha alfa zoom zoom align (0.5, 0.5) at hubc_flor_sale(marca)
                        add "ui/flor.png" matrixcolor TintMatrix(marca_color) align (0.5, 0.5) at hubc_brota(marca, 0.62, marca_pico)
                    else:
                        add "ui/flor.png" matrixcolor TintMatrix(color) alpha alfa zoom zoom align (0.5, 0.5)

        text _("TARDE [n] DE 3"):
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

    ## Táctil: el primer toque solo selecciona; el segundo elige.
    $ accion = Return(d["hermana"])
    if renpy.variant("touch") and hub_toque != d["hermana"]:
        $ accion = SetVariable("hub_toque", d["hermana"])

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
            action accion
            at estado

            add panel
            use hub_banda_nombre(d)

        ## Fuera del botón: así no le llega el gris de hub_visitado.
        ## El tono sigue la rama de esa tarde (color, pálido o gris).
        if visitada:
            use hub_sello(d["hermana"], hub_tono(d["hermana"], rama_de(d["hermana"])),
                          int(hub_slot_cx(indice)) + hub_offset(HUB_SELLO_Y), HUB_SELLO_Y)

        ## Velo de foco: encima de todo lo de la banda, sin foco propio (los clics pasan).
        add velo:
            xpos card_x
            ypos 0
            at luz

## Nombre y lugar al pie de la banda. Pieza aparte: la usan el botón del
## mapa y hub_completado (que no tiene botones). Va dentro de un contenedor
## de HUB_CARD_W de ancho.
screen hub_banda_nombre(d):
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
        text _("VISITADA"):
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


################################################################################
##  HUB COMPLETADO — "esta tarde quedó marcada"
##
##  USO (en cada hub, tras $ hub_visitadas.append(destino)):
##      call hub_completado(destino, n)        # n = 1, 2 o 3
##  La variante sale de rama_de(destino): cálida (~2.8 s), tibia (~1.5 s),
##  fría (~0.6 s). Sobre el mapa: la banda de la hermana se enciende, hace
##  su motivo, se estampa el sello y la flor de la tarde se tiñe.
##
##  PROBARLAS TODAS:  consola (Shift+O)  →  jump hub_completado_prueba
##
##  REGLA DEL PROYECTO: un clic NO adelanta un ATL. Por eso es una pantalla y
##  el guion espera con renpy.pause: un clic la corta limpia (fundido a negro).
##  Sonido: cort_completado_*.ogg (generar_cortinillas.py), canal cortinilla.
################################################################################

## SIN `modal`: un modal se traga el temporizador y el clic de renpy.pause y la
## pausa no termina nunca (el juego se queda colgado). Igual que cortinilla.
screen hub_completado(hermana, n, rama):
    zorder 80

    ## Se montan UNA vez por apertura, como en mapa_hub.
    default paneles = hub_paneles()
    default velos = hub_velos()
    default sombra = hub_sombra_superior(200, 0.55)

    $ t = HUBC_RITMOS[rama]
    $ tono = hub_tono(hermana, rama)
    $ claro = hub_claro(tono, 0.4)
    $ remate = rama == "calida"
    $ con_motivo = t["motivo"] is not None
    $ a = t["motivo"]
    $ s = t["sello"]
    $ i = [x["hermana"] for x in HUB_DESTINOS].index(hermana)
    $ dh = HUB_DESTINOS[i]
    $ card_x = int(hub_slot_cx(i) - HUB_CARD_W / 2.0)
    $ sx = int(hub_slot_cx(i)) + hub_offset(HUB_SELLO_Y)
    $ sy = HUB_SELLO_Y
    $ salto = 0
    if hermana == "yotsuba" and remate:
        $ salto = -6

    add "#07070a"

    ## --- Las otras cuatro bandas: quietas, con su velo ------------------------
    for k, d in enumerate(HUB_DESTINOS):
        if d["hermana"] != hermana:
            $ x_k = int(hub_slot_cx(k) - HUB_CARD_W / 2.0)
            $ visitada = d["hermana"] in hub_visitadas
            if visitada:
                $ estado = hub_visitado
            else:
                $ estado = hub_normal
            fixed:
                xpos x_k
                xysize (HUB_CARD_W, HUB_H + HUB_EXTRA)
                at estado
                add paneles[k]
                use hub_banda_nombre(d)
            if visitada:
                use hub_sello(d["hermana"], hub_tono(d["hermana"], rama_de(d["hermana"])),
                              int(hub_slot_cx(k)) + hub_offset(HUB_SELLO_Y), HUB_SELLO_Y)
            add velos[k] xpos x_k alpha HUBC_VELO_OTRAS

    ## --- La banda de la hermana: se enciende ----------------------------------
    fixed:
        xysize (HUB_W, HUB_H + HUB_EXTRA)
        at hubc_salto(s, salto)

        fixed:
            xpos card_x
            xysize (HUB_CARD_W, HUB_H + HUB_EXTRA)
            at hubc_banda(t["banda"], t["sat"], t["luz"], t["sube"])
            add paneles[i]
            use hub_banda_nombre(dh)

        add velos[i] xpos card_x at hubc_velo(t["banda"], t["velo"])

    ## Ichika: el foco de escenario cruza la banda (solo cálida).
    if hermana == "ichika" and remate:
        add velos[i] xpos card_x matrixcolor BrightnessMatrix(1.0) at hubc_foco(a)

    ## Miku: las barras suben DETRÁS del sello.
    if hermana == "miku" and con_motivo:
        for k in range(5):
            $ bx = sx + int((k - 2) * 32 * HUBC_COS)
            $ by = sy + int((k - 2) * 32 * HUBC_SIN)
            if remate:
                $ h2 = HUBC_EQ[1][k]
                $ h3 = HUBC_EQ[2][k]
                $ hfin = HUBC_EQ[3][k]
                $ pulso = 0.14
                $ fuera = 0.4
            else:
                ## tibia: un pulso y se apagan sin asentarse
                $ h2 = 0.3
                $ h3 = 0.3
                $ hfin = 0.05
                $ pulso = 0.0
                $ fuera = 0.0
            add "ui/hub_barra.png" matrixcolor TintMatrix(hub_claro(tono, 0.3)) at hubc_barra(bx, by, a, HUBC_EQ[0][k], h2, h3, hfin, pulso, fuera)

    ## --- El sello se estampa --------------------------------------------------
    if rama == "fria":
        use hub_sello(hermana, tono, sx, sy, anim=hubc_estampa_seca(s))
    else:
        use hub_sello(hermana, tono, sx, sy, anim=hubc_estampa(s))
        add "ui/hub_aro.png" matrixcolor TintMatrix(hub_claro(tono, 0.5)) at hubc_aro(sx, sy, s + 0.14)

    ## --- El motivo de la hermana ----------------------------------------------
    if hermana == "ichika" and con_motivo:
        for k, xy in enumerate(HUBC_CHISPAS):
            add "ui/hub_motivo_ichika.png" matrixcolor TintMatrix(hub_claro(tono, 0.6)) at hubc_chispa(sx + xy[0], sy + xy[1], a + k * 0.08, 0.45)
        if remate:
            add "ui/hub_motivo_ichika.png" matrixcolor TintMatrix(hub_claro(tono, 0.7)) at hubc_destello(sx, sy, s + 0.02)

    if hermana == "nino" and con_motivo:
        if remate:
            ## se posa en el sello, cierra las alas y se funde con él
            add "ui/hub_motivo_nino.png" matrixcolor TintMatrix(claro) at hubc_mariposa(sx, sy, a, s - a - 0.10, 0, 0, 0.2, 5)
        else:
            ## pasa de largo por encima del sello
            add "ui/hub_motivo_nino.png" matrixcolor TintMatrix(claro) at hubc_mariposa(sx, sy, a, s - a, 60, -100, 1.0, 3)

    if hermana == "yotsuba" and con_motivo:
        if remate:
            add "ui/hub_motivo_yotsuba.png" matrixcolor TintMatrix(claro) at hubc_trebol(sx, sy, a, 0.22, 120, 0.13, 50, 0.09, 22, 0.07, 90)
        else:
            add "ui/hub_motivo_yotsuba.png" matrixcolor TintMatrix(claro) at hubc_trebol(sx, sy, a, 0.22, 70, 0.11, 0, 0.0, 0, 0.0, 0)

    if hermana == "itsuki" and con_motivo:
        $ caida = 0.45
        if remate:
            $ caida = 0.5
        for e in HUBC_ESTELA:
            add "ui/hub_motivo_itsuki.png" matrixcolor TintMatrix(claro) at hubc_estrella(sx, sy, s - caida + e[0], caida, e[1], e[2])
        if remate:
            add "ui/hub_sello_fondo.png" matrixcolor TintMatrix(hub_claro(tono, 0.7)) at hubc_halo(sx, sy, s)
            add "ui/hub_motivo_itsuki.png" matrixcolor TintMatrix(hub_claro(tono, 0.5)) at hubc_brillo(sx, sy, s)

    ## --- Arriba: la flor de esta tarde se tiñe --------------------------------
    add sombra

    vbox:
        xalign 0.5
        ypos 26
        use hub_indicador_tarde(n, t["flor"], tono, t["pico"])

    if remate:
        add "sakura_petals" at cort_aparece(s + 0.4, 1.0, 0.85)


## --- Movimientos de hub completado -------------------------------------------

## La banda pasa del gris de visitada a su luz (y sube como en el hover).
transform hubc_banda(espera, sat, luz, sube):
    matrixcolor SaturationMatrix(0.12) * BrightnessMatrix(-0.22)
    yoffset 0
    pause espera
    ease 0.4 matrixcolor SaturationMatrix(sat) * BrightnessMatrix(luz) yoffset sube

## Golpe del trébol: la banda entera da un saltito (alto = 0, quieta).
transform hubc_salto(espera, alto):
    yoffset 0
    pause espera
    easein 0.08 yoffset alto
    ease 0.14 yoffset 0

transform hubc_velo(espera, fin):
    alpha HUBC_VELO_OTRAS
    pause espera
    linear 0.4 alpha fin

## Foco de escenario de Ichika: el velo de la banda, en blanco, un instante.
transform hubc_foco(espera):
    alpha 0.0
    pause espera
    linear 0.15 alpha 0.22
    linear 0.5 alpha 0.0

## El sello cae grande, frena en seco contra el mapa y se asienta. Sin elástico.
transform hubc_estampa(espera):
    xanchor 0.5 yanchor HUBC_SELLO_YA
    alpha 0.0 zoom 1.6
    pause espera
    parallel:
        linear 0.08 alpha 1.0
    parallel:
        easeout 0.16 zoom 0.94
        easein 0.12 zoom 1.0

## Fría: sin caída, un golpe seco.
transform hubc_estampa_seca(espera):
    xanchor 0.5 yanchor HUBC_SELLO_YA
    alpha 0.0 zoom 1.12
    pause espera
    alpha 1.0
    linear 0.1 zoom 1.0

## La marca del golpe: un aro que se abre y se apaga.
transform hubc_aro(x, y, espera):
    xpos x ypos y xanchor 0.5 yanchor 0.5
    alpha 0.0 zoom 0.95
    pause espera
    alpha 0.8
    parallel:
        easein 0.45 zoom 1.7
    parallel:
        linear 0.45 alpha 0.0

## Flor del indicador: la blanca se va y brota la de color.
transform hubc_flor_sale(espera):
    alpha 1.0
    pause espera
    linear 0.12 alpha 0.0

transform hubc_brota(espera, z, pico):
    alpha 0.0 zoom (z * 0.3)
    pause espera
    parallel:
        linear 0.12 alpha 0.95
    parallel:
        ease 0.16 zoom (z * pico)
        ease 0.14 zoom z

## Ichika: destello pequeño que brota, gira y se apaga.
transform hubc_chispa(x, y, espera, z):
    xpos x ypos y xanchor 0.5 yanchor 0.5
    alpha 0.0 zoom 0.01 rotate 0
    pause espera
    parallel:
        linear 0.08 alpha 1.0
    parallel:
        easein 0.22 zoom z
        easeout 0.22 zoom 0.01
    parallel:
        linear 0.44 rotate 45

## Ichika (remate): destello grande que se abre sobre el sello.
transform hubc_destello(x, y, espera):
    xpos x ypos y xanchor 0.5 yanchor 0.5
    alpha 0.0 zoom 0.4 rotate 0
    pause espera
    alpha 1.0
    parallel:
        easein 0.5 zoom 1.7
    parallel:
        linear 0.5 rotate 45
    parallel:
        pause 0.1
        linear 0.4 alpha 0.0

## Nino: sube en curva desde abajo a la izquierda aleteando y acaba en
## (fx, fy) respecto al sello. cierre = ancho de las alas al terminar.
transform hubc_mariposa(x, y, espera, vuelo, fx, fy, cierre, aleteos):
    xpos x ypos y xanchor 0.5 yanchor 0.5
    zoom 0.55 alpha 0.0 rotate -20
    xoffset -120 yoffset 240
    pause espera
    parallel:
        linear 0.12 alpha 1.0
    parallel:
        ease (vuelo * 0.5) xoffset 70
        ease (vuelo * 0.5) xoffset fx
    parallel:
        easein vuelo yoffset fy
    parallel:
        ease vuelo rotate 0
    parallel:
        block:
            linear 0.07 xzoom 0.35
            linear 0.07 xzoom 1.0
            repeat aleteos
    linear 0.10 xzoom cierre
    linear 0.14 alpha 0.0

## Miku: una barra que pulsa tres veces y se asienta en hfin.
## pulso = 0 salta los pulsos 2 y 3 (tibia).
transform hubc_barra(x, y, espera, h1, h2, h3, hfin, pulso, fuera):
    xpos x ypos y xanchor 0.5 yanchor 0.5
    rotate HUB_ANG
    alpha 0.0 yzoom 0.05
    pause espera
    parallel:
        linear 0.08 alpha 0.9
    parallel:
        easein 0.16 yzoom h1
    ease 0.14 yzoom 0.3
    easein pulso yzoom h2
    ease pulso yzoom 0.3
    easein pulso yzoom h3
    ease 0.10 yzoom hfin
    pause fuera
    linear 0.3 alpha 0.0

## Yotsuba: cae por la diagonal de la banda y bota contra el sello.
## h = altura de cada bote, d = medio bote en segundos (0 = no bota).
transform hubc_trebol(x, y, espera, caida, h1, d1, h2, d2, h3, d3, giro):
    xpos x ypos y xanchor 0.5 yanchor 0.5
    zoom 0.6 alpha 0.0 rotate 0
    xoffset (320 * HUBC_TAN) yoffset -320
    pause espera
    parallel:
        linear 0.06 alpha 1.0
    parallel:
        easeout caida xoffset 0 yoffset 0
    easein d1 xoffset (h1 * HUBC_TAN) yoffset (-h1)
    easeout d1 xoffset 0 yoffset 0
    easein d2 xoffset (h2 * HUBC_TAN) yoffset (-h2)
    easeout d2 xoffset 0 yoffset 0
    parallel:
        easein d3 xoffset (h3 * HUBC_TAN) yoffset (-h3)
        easeout d3 xoffset 0 yoffset 0
    parallel:
        linear (d3 * 2) rotate giro
    linear 0.12 alpha 0.0

## Itsuki: la estrella cae por la diagonal de la banda (una copia de la estela).
transform hubc_estrella(x, y, espera, caida, a, z):
    xpos x ypos y xanchor 0.5 yanchor 0.5
    zoom z alpha 0.0 rotate 0
    xoffset (480 * HUBC_TAN) yoffset -480
    pause espera
    parallel:
        linear 0.08 alpha a
    parallel:
        easeout caida xoffset 0 yoffset 0
    parallel:
        linear caida rotate 72
    linear 0.10 alpha 0.0

## Itsuki (remate): se queda sobre el sello y brilla.
transform hubc_brillo(x, y, espera):
    xpos x ypos y xanchor 0.5 yanchor 0.5
    alpha 0.0 zoom 0.6 rotate 0
    pause espera
    alpha 1.0
    parallel:
        easein 0.18 zoom 0.85
        ease 0.3 zoom 0.6
    parallel:
        easein 0.48 rotate 36
    pause 0.3
    linear 0.4 alpha 0.0

transform hubc_halo(x, y, espera):
    xpos x ypos y xanchor 0.5 yanchor 0.5
    alpha 0.0 zoom 0.5
    pause espera
    alpha 0.35
    parallel:
        easein 0.6 zoom 1.3
    parallel:
        linear 0.6 alpha 0.0


## --- Etiquetas ---------------------------------------------------------------

default hubc_qm_previo = True

## Táctil: hermana tocada una vez en el mapa (el segundo toque confirma).
default hub_toque = None

## rama: None = la lee de rama_de(hermana). Sin rama (showcase) = cálida.
label hub_completado(hermana="ichika", n=1, rama=None):

    if rama is None:
        $ rama = rama_de(hermana)
    if rama not in HUBC_RITMOS:
        $ rama = "calida"
    $ anim_marcar("tarde_" + hermana + "_" + rama)

    $ hubc_qm_previo = quick_menu
    $ quick_menu = False
    window hide

    $ renpy.music.set_volume(0.25, delay=0.3, channel="music")
    $ cort_sonar(hubc_jingle(hermana, rama))
    show screen hub_completado(hermana, n, rama)
    $ renpy.transition(Dissolve(0.3))

    ## Blindado: el clic que cerró la última línea del evento no se la lleva.
    $ renpy.pause(0.3, hard=True)
    $ renpy.pause(HUBC_RITMOS[rama]["total"] - 0.3)

    stop cortinilla fadeout 0.4
    scene bg_negro
    hide screen hub_completado
    with Dissolve(0.5)

    $ renpy.music.set_volume(1.0, delay=1.0, channel="music")
    $ quick_menu = hubc_qm_previo
    window auto

    return


## PRUEBA — consola (Shift+O): jump hub_completado_prueba
## Cálida en la tarde 1, tibia en la 2, fría en la 3.
label hub_completado_prueba:

    stop music fadeout 0.5
    stop ambiente

    call hub_completado("ichika", 1, "calida") from _call_hub_completado_4
    call hub_completado("nino", 1, "calida") from _call_hub_completado_5
    call hub_completado("miku", 1, "calida") from _call_hub_completado_6
    call hub_completado("yotsuba", 1, "calida") from _call_hub_completado_7
    call hub_completado("itsuki", 1, "calida") from _call_hub_completado_8

    call hub_completado("ichika", 2, "tibia") from _call_hub_completado_9
    call hub_completado("nino", 2, "tibia") from _call_hub_completado_10
    call hub_completado("miku", 2, "tibia") from _call_hub_completado_11
    call hub_completado("yotsuba", 2, "tibia") from _call_hub_completado_12
    call hub_completado("itsuki", 2, "tibia") from _call_hub_completado_13

    call hub_completado("ichika", 3, "fria") from _call_hub_completado_14
    call hub_completado("nino", 3, "fria") from _call_hub_completado_15
    call hub_completado("miku", 3, "fria") from _call_hub_completado_16
    call hub_completado("yotsuba", 3, "fria") from _call_hub_completado_17
    call hub_completado("itsuki", 3, "fria") from _call_hub_completado_18

    return
