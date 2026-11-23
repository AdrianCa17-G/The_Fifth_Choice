################################################################################
##  07_ui.rpy — Interfaz propia (cajas de texto y flor de sakura)
################################################################################
## init -5: se ejecuta ANTES que los `define` de 00_definiciones.rpy,
## que necesitan estas funciones para crear los personajes.
## Las fuentes japonesas centran el carácter … en vertical (flota a media
## altura de las letras). Se cambia por tres puntos normales al mostrarlo.
init -5 python:

    def ui_escena(modo="normal", hermana=None, lugar=""):
        """Cambia la decoración de pantalla.
        modo: "normal", "hub" o "beat". hermana: "ichika"... o None (5 colores)."""
        store.ui_modo = modo
        store.ui_hermana = hermana
        store.ui_lugar = lugar
        if modo != "normal":
            renpy.hide_screen("lugar_aviso")

    ## Fondo -> nombre de lugar. "" = ignorar ese fondo.
    BG_LUGAR = {

        "bg_cuarto_mc": _("Habitación de [nombre_jugador]"),
        "bg_comedor": _("Casa de los Uesugi"),
        "bg_escuela": _("Instituto Asaba"),
        "bg_aula": _("Aula · Día"),
        "bg_aula_tarde": _("Aula Vacía"),
        "bg_aula_anochecer": _("Aula Vacía · Anochecer"),
        "bg_azotea": _("Azotea · Día"),
        "bg_azotea_tarde": _("Azotea · Atardecer"),
        "bg_edificio": _("Edificio de las Nakano"),
        "bg_entrada_edificio": _("Entrada · Edificio de las Nakano"),
        "bg_departamento": _("Departamento Nakano"),
        "bg_departamento_anochecer": _("Departamento Nakano · Anochecer"),
        "bg_cocina": _("Cocina de las Nakano"),
        "bg_sala_ensayo": _("Sala de ensayo"),
        "bg_sala_ensayo_anochecer": _("Sala de ensayo · Anochecer"),
        "bg_centro_comercial": _("Centro comercial"),
        "bg_centro_comercial_anochecer": _("Centro comercial · Anochecer"),
        "bg_biblioteca": _("Biblioteca"),
        "bg_biblioteca_anochecer": _("Biblioteca · Anochecer"),
        "bg_pista_atletismo": _("Pista de atletismo"),
        "bg_pista_atletismo_anochecer": _("Pista de atletismo · Anochecer"),
        "bg_negro": "",
    }

        ## Fondos cuyo nombre NO se enseña en el prólogo: el protagonista aún no
    ## sabe que ahí viven las Nakano.
    BG_OCULTOS_PROLOGO = [
        "bg_edificio",
        "bg_entrada_edificio",
        "bg_departamento",
        "bg_departamento_anochecer",
    ]

    def ui_revisar_lugar(event, interact=True, **kwargs):
        """Se ejecuta en cada línea de diálogo. Si el FONDO cambió y estamos en
        modo normal, enseña el aviso del lugar unos segundos."""
        if event != "begin":
            return
        actual = None
        for tag in BG_LUGAR:
            if renpy.showing(tag):
                actual = tag
        if actual is None:
            return
        if BG_LUGAR[actual] == "":
            return
        if store.ui_prologo and actual in BG_OCULTOS_PROLOGO:
            return
        if actual == store.ui_ultimo_lugar:
            return
        store.ui_ultimo_lugar = actual
        if store.ui_modo == "normal":
            renpy.show_screen("lugar_aviso", BG_LUGAR[actual])

    config.all_character_callbacks.append(ui_revisar_lugar)

    def ui_raya(i, modo, hermana):
        """Color y opacidad de la raya i (0 a 4) de las esquinas."""
        orden = ["ichika", "nino", "miku", "yotsuba", "itsuki"]
        if hermana is None:
            color = PETALO_COLOR[orden[i]]
        else:
            color = PETALO_COLOR[hermana]
        if modo == "normal":
            alfa = 0.55
        elif hermana is None:
            alfa = 0.85
        else:
            alfa = 0.95 - 0.12 * i
        return (color, alfa)

    config.overlay_screens.append("marco_juego")

    def ui_icono(nombre, activo):
        """Icono del menú rápido. activo=True es el estado con el ratón encima."""
        color = store.ICONO_COLOR[nombre]
        oscuro = "#2B1B3F"
        if activo:
            fondo = Transform("ui/ico_base.png", matrixcolor=TintMatrix(color))
            glifo = Transform("ui/ico_" + nombre + ".png", matrixcolor=TintMatrix(oscuro))
        else:
            fondo = Transform("ui/ico_base.png", matrixcolor=TintMatrix(oscuro), alpha=0.82)
            glifo = Transform("ui/ico_" + nombre + ".png", matrixcolor=TintMatrix(color))
        borde = Transform("ui/ico_borde.png", matrixcolor=TintMatrix(color))
        return Fixed(fondo, borde, glifo, xysize=(68, 68))

    def ui_ventana_vacia():
        """Ventana vacía que Ren'Py muestra durante show/hide/with.
        Usa la caja de quien habló por última vez para que no cambie."""
        personaje = store.narrator
        quien = getattr(store, "_last_say_who", None)
        if quien is not None:
            try:
                personaje = renpy.eval_who(quien)
            except Exception:
                personaje = store.narrator
        if personaje is None:
            personaje = store.narrator
        personaje("", interact=False)


    TARJETA_ALTOS = [208, 256, 304, 352]   # los mismos de generar_ui.py (2 a 5 líneas)
    TARJETA_MARGEN = 56                    # arriba y abajo del texto más largo

    def ui_altura_items(items):
        """Altura de tarjeta que le queda justa al texto más largo del menú.
        Cada línea mide 48 px: hay un alto por número de líneas."""
        mayor = 0
        for i in items:
            alto_texto = 0
            try:
                t = Text(i.caption, style="tarjeta_texto")
                alto_texto = renpy.render(t, 432, 2000, 0, 0).get_size()[1]
            except Exception:
                lineas = len(i.caption) // 20 + 1
                alto_texto = lineas * 50
            if alto_texto > mayor:
                mayor = alto_texto
        necesario = mayor + 2 * TARJETA_MARGEN
        for alto in TARJETA_ALTOS:
            if alto >= necesario:
                return int(alto)
        return int(TARJETA_ALTOS[-1])

    class DecItemPrueba(object):
        """Opción de menú mínima para dec_autocomprobar."""
        def __init__(self, caption):
            self.caption = caption
            self.action = NullAction()

    def dec_autocomprobar():
        """Asserts de las decisiones con peso. Consola: $ dec_autocomprobar()"""
        def alto(textos):
            return ui_altura_items([DecItemPrueba(t) for t in textos])
        nino = ["Tienes razón en desconfiar. Solo el tiempo lo va a demostrar.",
                "Cargarle la cesta, sin decir nada.", "Yo sí voy a durar."]
        miku = ["Preguntarle cuánto tardaba la sal en llegar.",
                "Decirle que se le da bien. Es la verdad.", "Lo de la sal no entra en el examen."]
        cortas = ["Sí.", "No.", "Quizá."]
        larga = ["Una opción muy larga que no termina nunca y sigue y sigue. " * 6]
        for textos, esperado in ((nino, 256), (miku, 208), (cortas, 208), (larga, 352)):
            r = alto(textos)
            assert type(r) is int, "ui_altura_items no devuelve int: " + repr(r)
            assert r == esperado, "alto " + str(r) + " en vez de " + str(esperado)
        ## decision_animar: llamar fuera de un rollback (tras una interacción).
        trans = preferences.transitions
        saltando = store.decision_saltando
        try:
            preferences.transitions = 0
            store.decision_saltando = False
            assert decision_animar() is False, "con Transiciones apagado debe salir directo"
            preferences.transitions = trans
            store.decision_saltando = True
            assert decision_animar() is False, "si venía saltando debe salir directo"
            store.decision_saltando = False
            if trans != 0:
                assert decision_animar() is True, "sin rollback ni salto debe animar"
        finally:
            preferences.transitions = trans
            store.decision_saltando = saltando
        return True

    def decision_animar():
        """¿Lleva «Hora de decidir»? No en rollback ni al cargar (ya la viste),
        no si venías saltando (ya la leíste), no con Transiciones apagado."""
        if renpy.in_rollback():
            return False
        if store.decision_saltando:
            return False
        if preferences.transitions == 0:
            return False
        return True

    def decision_peso(hermana, titulo, motivo, pistas=None):
        """Marca la siguiente decisión como 'con peso'.
        titulo: la pregunta. motivo: por qué importa esta decisión.
        pistas: temperatura de cada opción, en el orden en que aparecen."""
        anim_marcar("decidir_" + hermana)
        store.decision_hermana = hermana
        store.decision_titulo = titulo
        store.decision_motivo = motivo
        ## El menú corta el modo saltar antes de abrir la pantalla: se apunta aquí.
        store.decision_saltando = renpy.is_skipping()
        if pistas is None:
            store.decision_pistas = ["calida", "tibia", "fria"]
        else:
            store.decision_pistas = pistas
        ## Orden de las tarjetas, al azar: la posición no delata la temperatura.
        orden = list(range(len(store.decision_pistas)))
        renpy.random.shuffle(orden)
        store.decision_orden = orden

    def decision_ordenar(cantidad):
        """Orden de pantalla de las opciones. Si no cuadra con el menú, el original."""
        if len(store.decision_orden) != cantidad:
            return list(range(cantidad))
        return store.decision_orden


    config.empty_window = ui_ventana_vacia

    def ui_arreglar_texto(texto):
        return texto.replace("\u2026", "...")

    config.say_menu_text_filter = ui_arreglar_texto

    def ui_mezclar(color_a, color_b, t):
        """Mezcla dos colores hex. t=0 devuelve color_a, t=1 devuelve color_b."""
        a = color_a.lstrip("#")
        b = color_b.lstrip("#")
        resultado = "#"
        for k in (0, 2, 4):
            va = int(a[k:k + 2], 16)
            vb = int(b[k:k + 2], 16)
            v = int(va + (vb - va) * t)
            resultado = resultado + "{:02x}".format(v)
        return resultado

    def ui_personaje(nombre, color, petalo=None, deco=None):
        """Personaje con caja rellena de su color (y motivo opcional)."""
        placa = ui_mezclar(color, "#FFFFFF", 0.45)
        tinta = ui_mezclar(color, "#000000", 0.72)
        caja = Transform("ui/caja.png", matrixcolor=TintMatrix(color))
        fondo = caja
        if deco is not None:
            fondo = Composite((1340, 240), (0, 0), caja, (0, 0), deco)
        return Character(
            nombre,
            what_color="#241B33",
            window_style="caja",
            window_background=fondo,
            show_tipo="hablante",
            show_placa=placa,
            show_tinta=tinta,
            show_petalo=petalo,
            ctc="ctc_oscuro",
            ctc_position="nestled",
        )


    def ui_interior(color, hermana):
        """Voz interior de una hermana (Evento 6): caja de su color más clara que
        la de diálogo, SIN placa (who=None: la pantalla say no dibuja la namebox),
        texto en cursiva y su pétalo activo en la flor."""
        placa = ui_mezclar(color, "#FFFFFF", 0.45)
        tinta = ui_mezclar(color, "#000000", 0.72)
        base = ui_mezclar(color, "#FFFFFF", 0.35)
        caja = Transform("ui/caja.png", matrixcolor=TintMatrix(base))
        deco = Transform("ui/deco_" + hermana + ".png", alpha=0.6)
        fondo = Composite((1340, 240), (0, 0), caja, (0, 0), deco)
        return Character(
            None,
            what_color="#2B1B3F",
            what_italic=True,
            window_style="caja",
            window_background=fondo,
            show_tipo="interior",
            show_placa=placa,
            show_tinta=tinta,
            show_petalo=hermana,
            ctc="ctc_oscuro",
            ctc_position="nestled",
        )
        

define PETALO_ORDEN = ["ichika", "nino", "miku", "yotsuba", "itsuki"]

define PETALO_COLOR = {
    "ichika":  C_ICHIKA,
    "nino":    C_NINO,
    "miku":    C_MIKU,
    "yotsuba": C_YOTSUBA,
    "itsuki":  C_ITSUKI,
}

## Cada pétalo es la misma imagen rotada 72 grados * i alrededor de su centro.
transform petalo_giro(i, color, brillo):
    align (0.5, 0.5)
    rotate (i * 72)
    matrixcolor TintMatrix(color)
    alpha brillo

## Marca de agua dentro de la caja, a la derecha.
## - hermana activa: su pétalo en blanco
## - "todas": cada pétalo con su color
## - el resto: apagados (oscuros sobre caja clara, claros sobre la del narrador)
screen flor_sakura(activa=None, tipo="hablante", x=1450, y=844, color_activo="#FFFFFF"):
    fixed:
        xpos x
        ypos y
        xysize (160, 160)

        for i in range(5):
            $ hermana = PETALO_ORDEN[i]
            if activa == "todas":
                add "ui/petalo.png" at petalo_giro(i, PETALO_COLOR[hermana], 0.95)
            elif activa == hermana:
                add "ui/petalo.png" at petalo_giro(i, color_activo, 0.95)
            elif tipo == "narrador":
                add "ui/petalo.png" at petalo_giro(i, "#FFFFFF", 0.16)
            else:
                add "ui/petalo.png" at petalo_giro(i, "#000000", 0.14)


## --- Indicador de "sigue" (click to continue) --------------------------------
## Un pétalo pequeño que parpadea al final de la línea cuando el texto ya
## terminó de escribirse. Tres colores, según el fondo de la caja.

## Sobre cajas pastel (las hermanas y el resto de personajes)
image ctc_oscuro:
    "ui/flor.png"
    zoom 0.5
    matrixcolor TintMatrix("#2B1B3F")
    alpha 0.9
    linear 0.6 alpha 0.25
    linear 0.6 alpha 0.9
    repeat

## Sobre la caja oscura del narrador
image ctc_claro:
    "ui/flor.png"
    zoom 0.5
    matrixcolor TintMatrix("#FFFFFF")
    alpha 0.9
    linear 0.6 alpha 0.25
    linear 0.6 alpha 0.9
    repeat

## Sobre la hoja de libreta
image ctc_libreta:
    "ui/flor.png"
    zoom 0.5
    matrixcolor TintMatrix("#B94A4A")
    alpha 0.9
    linear 0.6 alpha 0.25
    linear 0.6 alpha 0.9
    repeat


## --- Decisiones con peso ----------------------------------------------------

## Qué tan visible es la pista de temperatura (0.0 = apagada, 0.5 = muy clara).
define PISTA_FUERZA = 0.00

## Altura del conjunto (pregunta + tarjetas): 0.0 arriba, 1.0 abajo.
## Si lo quieres más abajo, sube el número (máx. ~0.75, o chocará con el borde).
define DECISION_ALINEACION = 0.45

## Tono oscuro de cada hermana para su tarjeta (distinto del violeta de las ligeras).
define TARJETA_TONO = {
    "ichika":  "#5A3340",
    "nino":    "#522A57",
    "miku":    "#1F4660",
    "yotsuba": "#1E5A3A",
    "itsuki":  "#6A2A26",
}

transform ventana_oculta:
    alpha 0.0

## «Hora de decidir»: segundos de cada pieza. (inicio, duración) donde hay dos.
## Radial, desde el centro: las cortinillas son diagonales, el hub bandas y
## los minijuegos una columna.
define DEC_RITMOS = dict(
    velo=0.3, flor=0.30, linea=(0.25, 0.35), texto=(0.35, 0.30), sale=(0.95, 0.25),
    pregunta=0.95, tarjeta=0.95, paso=0.08, tarjeta_dur=0.30, listo=1.45)

transform decision_velo(dur):
    alpha 0.0
    linear dur alpha 0.5

transform pregunta_entrada(espera):
    alpha 0.0
    yoffset -40
    pause espera
    linear 0.4 alpha 1.0 yoffset 0

transform tarjeta_entrada(n, espera):
    alpha 0.0
    yoffset 70
    pause (espera + DEC_RITMOS["paso"] * n)
    linear DEC_RITMOS["tarjeta_dur"] alpha 1.0 yoffset 0

## Sin intro: nada se mueve (mismo dibujo que el último fotograma animado).
transform dec_quieto:
    alpha 1.0

transform dec_flor(dur):
    zoom 0.6 rotate -30 alpha 0.0
    parallel:
        ease dur zoom 1.0 rotate 0
    parallel:
        linear (dur * 0.5) alpha 1.0
    rotate None

transform dec_linea(espera, dur):
    xzoom 0.0
    pause espera
    ease dur xzoom 1.0

transform dec_texto(espera, dur):
    alpha 0.0 yoffset 12
    pause espera
    ease dur alpha 1.0 yoffset 0

transform dec_rotulo_sale(espera, dur):
    pause espera
    parallel:
        ease dur yoffset -30 zoom 0.92
    parallel:
        linear dur alpha 0.0

transform tarjeta_hover:
    on idle:
        linear 0.15 yoffset 0
    on hover:
        linear 0.15 yoffset -14

## La flor de la tarjeta, más pequeña: a tamaño completo pisaba el texto.
transform tarjeta_flor:
    zoom 0.7

style tarjeta_texto is default:
    size 31
    color "#F3EEFA"
    xpos 44
    yalign 0.5
    xsize 432
    line_spacing 4

style placa_centro is placa:
    xpos 0.5
    xanchor 0.5

screen choice_peso(items):

    $ color = PETALO_COLOR[decision_hermana]
    $ tinta = ui_mezclar(color, "#000000", 0.72)
    $ placa_color = ui_mezclar(color, "#FFFFFF", 0.45)
    $ claro = ui_mezclar(color, "#FFFFFF", 0.25)
    $ tono_fondo = TARJETA_TONO[decision_hermana]
    $ alto = ui_altura_items(items)

    ## Una vez por apertura: rollback, carga, modo saltar o Transiciones
    ## apagado = todo en su estado final y pulsable desde el principio.
    default intro = decision_animar()
    default listo = not intro

    python:
        if intro:
            anim_pregunta = pregunta_entrada(DEC_RITMOS["pregunta"])
        else:
            anim_pregunta = dec_quieto

    if intro:
        add Solid("#000000") at decision_velo(DEC_RITMOS["velo"])
        timer 0.01 action Function(cort_sonar, "mj_" + decision_hermana + "_saltado")
        timer DEC_RITMOS["listo"] action SetLocalVariable("listo", True)
    else:
        add Solid("#000000") alpha 0.5

    vbox:
        xalign 0.5
        yalign DECISION_ALINEACION
        spacing 60

        ## --- La pregunta: caja propia, centrada y por delante de todo ---
        fixed:
            at anim_pregunta
            xalign 0.5
            xysize (1340, 240)

            add Transform("ui/caja.png", matrixcolor=TintMatrix(color))
            add ("ui/deco_" + decision_hermana + ".png")

            window:
                style "placa_centro"
                background Transform(Frame("ui/placa.png", 40, 0, 40, 0),
                                     matrixcolor=TintMatrix(placa_color))
                text _("DECISIÓN") style "say_label" color tinta

            vbox:
                xalign 0.5
                yalign 0.5
                yoffset 6
                xsize 960
                spacing 10
                text decision_titulo font gui.name_text_font size 40 color tinta xalign 0.5 text_align 0.5
                text decision_motivo size 29 color tinta xalign 0.5 text_align 0.5

            use flor_sakura(decision_hermana, "hablante", 1160, 40, tinta)

        ## --- Las tarjetas ---
        hbox:
            xalign 0.5
            spacing 40

            for k, n in enumerate(decision_ordenar(len(items))):

                $ i = items[n]
                $ pista = decision_pistas[n]
                $ tono = "#FFFFFF"
                $ fuerza = 0.0
                if pista == "calida":
                    $ tono = "#FFC46B"
                    $ fuerza = PISTA_FUERZA
                elif pista == "fria":
                    $ tono = "#7FA6E8"
                    $ fuerza = PISTA_FUERZA

                python:
                    if intro:
                        anim_tarjeta = tarjeta_entrada(k, DEC_RITMOS["tarjeta"])
                    else:
                        anim_tarjeta = dec_quieto

                fixed:
                    xysize (520, alto)
                    at anim_tarjeta

                    button:
                        xysize (520, alto)
                        background None
                        sensitive listo
                        action i.action
                        hover_sound audio.sfx_hover
                        activate_sound audio.sfx_click
                        at tarjeta_hover

                        add ("ui/tarjeta_" + str(alto) + ".png") matrixcolor TintMatrix(tono_fondo)
                        add ("ui/halo_" + str(alto) + ".png") matrixcolor TintMatrix(tono) alpha fuerza
                        add ("ui/deco_tarjeta_" + decision_hermana + "_" + str(alto) + ".png") matrixcolor TintMatrix(claro)
                        add ("ui/tarjeta_marco_" + str(alto) + ".png") matrixcolor TintMatrix(color)
                        fixed:
                            at tarjeta_flor
                            xpos 402
                            ypos (alto - 118)
                            xysize (160, 160)
                            use flor_sakura(decision_hermana, "hablante", 0, 0, color)
                        text i.caption style "tarjeta_texto"

    ## --- «HORA DE DECIDIR»: la flor se abre, la línea crece, el rótulo sube ---
    if intro:
        fixed:
            at dec_rotulo_sale(DEC_RITMOS["sale"][0], DEC_RITMOS["sale"][1])
            xalign 0.5
            yalign 0.5
            xysize (1000, 320)

            fixed:
                at dec_flor(DEC_RITMOS["flor"])
                xpos 500
                ypos 80
                xanchor 0.5
                yanchor 0.5
                xysize (160, 160)
                for k in range(5):
                    if PETALO_ORDEN[k] == decision_hermana:
                        add "ui/petalo.png" at petalo_giro(k, color, 0.95)
                    else:
                        add "ui/petalo.png" at petalo_giro(k, "#FFFFFF", 0.25)

            add Solid(color, xsize=900, ysize=2):
                at dec_linea(DEC_RITMOS["linea"][0], DEC_RITMOS["linea"][1])
                xpos 500
                xanchor 0.5
                ypos 182

            text _("HORA DE DECIDIR"):
                at dec_texto(DEC_RITMOS["texto"][0], DEC_RITMOS["texto"][1])
                xpos 500
                xanchor 0.5
                ypos 206
                font HUD_FUENTE
                size 46
                kerning 10
                color "#FFFFFF"
                outlines [(4, tinta, 0, 0)]


## --- Iconos del menú rápido -------------------------------------------------
## Los mismos colores y el mismo orden que los botones del menú principal.
define ICONO_COLOR = {
    "historial": C_ICHIKA,
    "auto":      C_NINO,
    "saltar":    C_MIKU,
    "guardar":   C_YOTSUBA,
    "menu":      C_ITSUKI,
    "info":      "#FFFFFF",
    "ayuda":     "#FFFFFF",
    "salir":     "#FFFFFF",
}

transform icono_hover:
    on idle:
        linear 0.12 yoffset 0
    on hover:
        linear 0.12 yoffset 5


## --- Decoración de pantalla -------------------------------------------------

## Tipografía de la cinta. Cámbiala aquí si quieres probar otra.
define HUD_FUENTE = gui.name_text_font

define HUB_LUGAR = {
    "ichika":  _("Sala de ensayo"),
    "nino":    _("Centro comercial"),
    "miku":    _("Biblioteca"),
    "yotsuba": _("Pista de atletismo"),
    "itsuki":  _("Aula vacía"),
}

default ui_modo = "normal"
default ui_hermana = None
default ui_lugar = ""
default ui_ultimo_lugar = ""
default ui_prologo = True

transform hud_cinta_entrada:
    xoffset -800
    ease 0.45 xoffset 0

transform hud_aviso_anim:
    xoffset -800
    ease 0.45 xoffset 0
    pause 3.5
    ease 0.45 xoffset -800

style hud_cinta_win is default:
    xpos 0
    ypos 22
    ysize 64
    xminimum 380
    xmaximum 1100
    padding (54, 0, 76, 0)

## La cinta en sí. Se ajusta sola al ancho del texto.
screen hud_cinta_vista(lugar, etiqueta, clave, cinta, tinta, anim, deco=True):

    $ lugar_mayus = renpy.substitute(lugar).upper()
    $ tinta_suave = tinta + "BB"
    $ deco_alfa = 0.0
    if deco:
        $ deco_alfa = 1.0

    window:
        style "hud_cinta_win"
        at anim
        background Fixed(
            Transform(Frame("ui/hud_cinta.png", 40, 0, 40, 0), matrixcolor=TintMatrix(cinta)),
            Transform("ui/hud_cinta_deco_" + clave + ".png", xalign=1.0, alpha=deco_alfa))

        hbox:
            spacing 16
            yalign 0.5

            add ("ui/hud_icono_" + clave + ".png") matrixcolor TintMatrix(tinta) yalign 0.5

            vbox:
                yalign 0.5
                spacing 0

                if etiqueta != "":
                    text __(etiqueta) font HUD_FUENTE size 14 kerning 4 color tinta_suave substitute False

                text lugar_mayus font HUD_FUENTE size 27 kerning 2 color tinta substitute False


screen lugar_aviso(lugar):

    zorder 91

    if quick_menu:
        use hud_cinta_vista(lugar, "", "flor", "#E8E0F2", "#2B1B3F", hud_aviso_anim, False)

    timer 4.6 action Hide("lugar_aviso")

screen marco_juego():

    zorder 90

    ## Se oculta junto con el menú rápido (en el mapa del hub, por ejemplo).
    if quick_menu:

        $ base = "#E8E0F2"
        if ui_hermana is not None:
            $ base = PETALO_COLOR[ui_hermana]
        $ cinta = ui_mezclar(base, "#FFFFFF", 0.35)
        $ tinta_hud = ui_mezclar(base, "#000000", 0.75)

        add "ui/hud_sombra.png"

        ## En el prólogo no hay rayas: aparecen con el Capítulo 1.
        if not ui_prologo:
            for i in range(5):
                $ c, a = ui_raya(i, ui_modo, ui_hermana)
                add ("ui/hud_raya_" + str(i) + ".png") matrixcolor TintMatrix(c) alpha a xalign 0.0 yalign 1.0
                add ("ui/hud_rayad_" + str(i) + ".png") matrixcolor TintMatrix(c) alpha a xalign 1.0 yalign 1.0

        if ui_modo == "beat":
            add Solid(base, xsize=1920, ysize=5) alpha 0.9 ypos 0
            add Solid(base, xsize=1920, ysize=5) alpha 0.9 yalign 1.0

        if ui_lugar != "":

            $ clave = "flor"
            if ui_hermana is not None:
                $ clave = ui_hermana

            $ etiqueta = ""
            if ui_modo == "hub":
                $ etiqueta = _("ENCUENTRO")
            elif ui_modo == "beat":
                $ etiqueta = _("ESCENA CLAVE")

            use hud_cinta_vista(ui_lugar, etiqueta, clave, cinta, tinta_hud, hud_cinta_entrada)

            if ui_modo != "normal":
                text _("Quedan [tiempo_restante!t]") xpos 44 ypos 94 size 22 color "#FFFFFF" outlines [(3, "#1B102699", 0, 0)]