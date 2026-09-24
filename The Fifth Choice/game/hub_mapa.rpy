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
    HUB_N     = 5
    HUB_SLOT  = HUB_W // HUB_N
    HUB_GAP   = 10

    HUB_DESPL  = int(HUB_H / 2.0 * math.tan(math.radians(abs(HUB_ANG))))
    HUB_CARD_W = HUB_SLOT + 2 * HUB_DESPL + 40

    # --- look ---
    HUB_VELO   = 0.24
    HUB_UNIFY  = 0.10
    HUB_SOMBRA = 0.78

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
                r = surf.get_bounding_rect(1)
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

    def hub_sprite(ruta, escala=1.0, xoff=0, yoff=0):
        """Sprite escalado por altura REAL de la chica y con la
        coronilla clavada en HUB_CABEZA."""
        top, bot = hub_bbox(ruta)
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
            return "Tres tardes. Cinco hermanas. Solo vas a alcanzar a tres."
        elif n == 2:
            return "Te quedan dos tardes. Dos de ellas van a quedar afuera."
        else:
            return "Última tarde. Elegí con quién la terminás."

    def hub_mask(borde=None):
        ancho = int((HUB_SLOT - HUB_GAP) * math.cos(math.radians(HUB_ANG)))
        dx = 0
        extra = 2 * HUB_DESPL + 80
        if borde == "izq":
            ancho += extra
            dx = -extra // 2
        elif borde == "der":
            ancho += extra
            dx = extra // 2
        return Fixed(
            Transform("#ffffff",
                      xysize=(ancho, int(HUB_H * 2.4)),
                      rotate=HUB_ANG,
                      xalign=0.5, yalign=0.5, xoffset=dx),
            xysize=(HUB_CARD_W, HUB_H),
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

    def hub_panel(fondo, ruta, color, escala=1.0, xoff=0, yoff=0, borde=None):
        capas = [
            Transform(fondo, xysize=(HUB_CARD_W, HUB_H), fit="cover"),
            Transform(Solid(color), xysize=(HUB_CARD_W, HUB_H), alpha=HUB_VELO),
            hub_sprite(ruta, escala, xoff, yoff),
            Transform(Solid(color), xysize=(HUB_CARD_W, HUB_H), alpha=HUB_UNIFY),
            hub_degradado(520),
            Transform(Solid(color), xysize=(HUB_CARD_W, 12), yalign=1.0),
        ]
        return AlphaMask(Fixed(*capas, xysize=(HUB_CARD_W, HUB_H)), hub_mask(borde))


# ------------------------------------------------------------
# Placeholders de fondo — borralos cuando tengas los reales
# ------------------------------------------------------------
image ph_bg_aula       = "bg/hubs_hermanas/aula_tarde.webp"
image ph_bg_pista      = Solid("#1d3a28")
image ph_bg_ensayo     = Solid("#3a1d2c")
image ph_bg_comercial  = Solid("#2c1d3a")
image ph_bg_biblioteca = Solid("#1d2c3a")


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
             sprite="sprites/ichika_sprites/ichika_neutral.png",
             color="#FFB7C5", escala=1.00, xoff=0, yoff=0),

        dict(hermana="nino",    nombre="Nino",    lugar="Centro comercial",
             fondo="ph_bg_comercial",
             sprite="sprites/nino_sprites/nino_neutral.png",
             color="#C39BD3", escala=1.00, xoff=0, yoff=0),

        dict(hermana="miku",    nombre="Miku",    lugar="Biblioteca",
             fondo="ph_bg_biblioteca",
             sprite="sprites/miku_sprites/miku_neutral.png",
             color="#5DADE2", escala=1.00, xoff=0, yoff=0),

        dict(hermana="yotsuba", nombre="Yotsuba", lugar="Pista de atletismo",
             fondo="ph_bg_pista",
             sprite="sprites/yotsuba_sprites/yotsuba_sonrisa.png",
             color="#58D68D", escala=1.00, xoff=0, yoff=0),

        dict(hermana="itsuki",  nombre="Itsuki",  lugar="Aula vacía",
             fondo="ph_bg_aula",
             sprite="sprites/itsuki_sprites/itsuki_sonrisa.png",
             color=C_ITSUKI,  escala=1.00, xoff=0, yoff=0),
    ]


# ------------------------------------------------------------
# Screen principal
# ------------------------------------------------------------
screen mapa_hub(hub_actual=1):
    tag menu
    modal True

    add "#07070a"

    fixed:
        xysize (HUB_W, HUB_H)

        for i, d in enumerate(HUB_DESTINOS):
            use destino_hub(i, d)

    vbox:
        xalign 0.5
        ypos 30
        spacing 6

        text "¿Con cuál quintilliza pasarás esta tarde?":
            size 54 color "#ffffff" xalign 0.5
            outlines [(6, "#000000", 0, 0), (2, "#000000", 0, 3)]

        text hub_subtitulo(hub_actual):
            size 23 color "#e2e2e2" xalign 0.5
            outlines [(5, "#000000", 0, 0), (2, "#000000", 0, 2)]

    # reglas de calibración: poné HUB_GUIA = True para alinear cabezas
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
# Una banda
# ------------------------------------------------------------
screen destino_hub(indice, d):
    $ visitada = d["hermana"] in hub_visitadas
    $ borde = "izq" if indice == 0 else ("der" if indice == HUB_N - 1 else None)

    button:
        xpos indice * HUB_SLOT - (HUB_CARD_W - HUB_SLOT) // 2
        ypos 0
        xysize (HUB_CARD_W, HUB_H)
        background None
        focus_mask True
        action Return(d["hermana"])
        at (hub_visitado if visitada else hub_normal)

        add hub_panel(d["fondo"], d["sprite"], d["color"],
                      d.get("escala", 1.0), d.get("xoff", 0), d.get("yoff", 0),
                      borde)

        vbox:
            xalign 0.5
            ypos 816
            xoffset hub_offset(870)
            spacing 0

            text d["nombre"]:
                size 44 color hub_claro(d["color"]) xalign 0.5 text_align 0.5
                outlines [(5, "#000000", 0, 0), (2, "#000000", 0, 2)]

            text d["lugar"]:
                size 23 color "#e0e0e0" xalign 0.5 text_align 0.5
                outlines [(4, "#000000", 0, 0)]

            if visitada:
                text "ya visitada":
                    size 17 color "#a8a8a8" xalign 0.5
                    outlines [(3, "#000000", 0, 0)]


transform hub_normal:
    matrixcolor BrightnessMatrix(-0.06) * SaturationMatrix(0.92)
    yoffset 0
    on hover:
        linear 0.12 matrixcolor BrightnessMatrix(0.10) * SaturationMatrix(1.25) yoffset -10
    on idle:
        linear 0.12 matrixcolor BrightnessMatrix(-0.06) * SaturationMatrix(0.92) yoffset 0

transform hub_visitado:
    matrixcolor SaturationMatrix(0.22) * BrightnessMatrix(-0.18)
    yoffset 0
    on hover:
        linear 0.12 matrixcolor SaturationMatrix(0.65) * BrightnessMatrix(-0.04) yoffset -6
    on idle:
        linear 0.12 matrixcolor SaturationMatrix(0.22) * BrightnessMatrix(-0.18) yoffset 0