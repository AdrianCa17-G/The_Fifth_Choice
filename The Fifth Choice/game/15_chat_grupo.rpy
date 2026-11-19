################################################################################
##  15_chat_grupo.rpy — Chat del grupo «¡Equipo Quintillizas + Tutor!»
##  Una sola pantalla para sus tres apariciones (debut en la interc. 4, decisión
##  del sábado en la interc. 6 y noche del Evento 6), alimentada por listas.
##
##  Uso:  call chat_ver(lista, desde)   → los mensajes desde `desde` entran con su
##        ritmo (los anteriores ya están: historial). Un clic completa el chat y
##        otro continúa. Al volver, el chat queda ATENUADO detrás de los diálogos.
##        hide screen chat_grupo + with dissolve para quitarlo.
##  Prueba: consola → jump chat_grupo_prueba
################################################################################

## --- Datos ---------------------------------------------------------------------
## Cada elemento es una tupla:
##   ("aviso", texto)          aviso del sistema, centrado
##   ("sale", h) / ("vuelve", h)   «h salió del grupo» / «Yotsuba añadió a h»
##   (h, texto) / (h, texto, foto)  mensaje; h = hermana o "mc". foto: "boletin",
##                                  "almohada", "grupo"
##   ("pausa", segundos)       espera más larga entre dos mensajes
##   ("borra", h)              el último mensaje de h pasa a «Se eliminó este mensaje»

define CHAT_CORAZON = "{font=DejaVuSans.ttf}{size=+8}♥{/size}{/font}"

define CHAT_DEBUT = [
    ("aviso", "Yotsuba creó el grupo «¡Equipo Quintillizas + Tutor!»"),
    ("aviso", "Yotsuba te añadió"),
    ("yotsuba", "¡¡¡Buenos días, equipo!!!"),
    ("yotsuba", "¡Las cinco y nuestro sexto integrante! ¡¡Equipo completo!!"),
    ("yotsuba", "¡Todo lo de estudiar, aquí! ¡¡Sin excepciones!!"),
    ("sale", "nino"),
    ("yotsuba", "¿¿Nino??"),
]

## La semana hasta el sábado: Nino se sale tres veces y Yotsuba la mete tres veces
## (la primera salida es la del debut; la primera vuelta, la del beat de Nino).
define CHAT_SEMANA = CHAT_DEBUT + [
    ("vuelve", "nino"),
    ("yotsuba", "¡¡Bienvenida de vuelta!!"),
    ("sale", "nino"),
    ("vuelve", "nino"),
    ("yotsuba", "¡Ese botón no es para eso!"),
    ("sale", "nino"),
    ("vuelve", "nino"),
    ("yotsuba", "¡Ya sé que lo silenciaste! ¡¡Igual cuenta!!"),
]

## Sábado: el mensaje del MC (mismos textos que el menú) y la respuesta de Yotsuba.
define CHAT_SABADO_OPCION = [
    [("mc", "Duerman bien. Recuerden que no es el fin del mundo."),
     ("yotsuba", "¡¡Ella ya está lista!!", "almohada")],
    [("mc", "Confío en las cinco. Pase lo que pase el lunes."),
     ("yotsuba", "¡¡¡¡¡GRACIAS!!!!!!")],
    [("mc", "Si algo sale mal, la culpa es mía. Para eso me pagan."),
     ("yotsuba", "¡La culpa no se paga, se comparte!")],
]

## Sábado: las demás, según clima_cap1. Cualquier otro clima: nadie más contesta.
define CHAT_SABADO_CLIMA = {
    "buena": [
        ("ichika", CHAT_CORAZON),
        ("ichika", "jajaja"),
        ("nino", "Qué dramático."),
        ("pausa", 1.8),
        ("nino", "Descansen."),
        ("miku", "..."),
        ("miku", "Gracias."),
        ("itsuki", "Recibido."),
    ],
    "mixta": [
        ("ichika", CHAT_CORAZON),
        ("pausa", 0.9),
        ("borra", "ichika"),
        ("ichika", "jajaja"),
        ("nino", "Qué dramático."),
    ],
}

default chat_lista = []
default chat_n = 0
default chat_atenuado = False
default chat_opcion = 0

init python:

    def chat_sabado(opcion, clima):
        """Historial de la semana + mensaje del MC + respuestas del sábado."""
        return CHAT_SEMANA + CHAT_SABADO_OPCION[opcion] + CHAT_SABADO_CLIMA.get(clima, [])

    def chat_e6(miku_calida):
        """Noche del Evento 6. El primero (la foto de la tarde) ya estaba: desde = 1.
        Miku pierde el «...» solo en la cálida (REVISION_MIKU_CAP1, P4)."""
        if miku_calida:
            miku = "Sociales: cien."
        else:
            miku = "...Sociales: cien."
        return [
            ("yotsuba", "¡¡La foto de hoy!! ¡¡La próxima, con fotógrafo incluido!!", "grupo"),
            ("yotsuba", "¡¡¡CIEN EN JAPONÉS!!! ¡¡¡MIREN!!!", "boletin"),
            ("yotsuba", "¡¡Manden el suyo!! ¡¡Sin trampas!!"),
            ("ichika", "Cien en matemáticas. Pueden aplaudir. Con moderación.", "boletin"),
            ("miku", miku, "boletin"),
            ("nino", "Que conste que no me salí.", "boletin"),
            ("itsuki", "Ciencias: cien. Es un dato, no una celebración.", "boletin"),
            ("yotsuba", "¡¡¡ES UNA CELEBRACIÓN!!!"),
            ("itsuki", "Está bien. Una celebración pequeña."),
        ]

    def chat_nombre(quien):
        if quien == "mc":
            return store.nombre_jugador
        return quien.capitalize()

    def chat_filas(lista, n):
        """Agrupa lista[:n] en filas para la pantalla y dice quién está fuera.
        Fila: ("aviso", texto) o (quien, [(texto, foto), ...]) con mensajes seguidos."""
        filas = []
        fuera = set()
        for item in lista[:n]:
            tipo = item[0]
            if tipo == "pausa":
                continue
            if tipo == "sale":
                fuera.add(item[1])
                filas.append(("aviso", chat_nombre(item[1]) + " salió del grupo"))
                continue
            if tipo == "vuelve":
                fuera.discard(item[1])
                filas.append(("aviso", "Yotsuba añadió a " + chat_nombre(item[1])))
                continue
            if tipo == "aviso":
                filas.append(("aviso", item[1]))
                continue
            if tipo == "borra":
                for fila in reversed(filas):
                    if fila[0] == item[1]:
                        fila[1][-1] = ("Se eliminó este mensaje", "borrado")
                        break
                continue
            foto = None
            if len(item) > 2:
                foto = item[2]
            if filas and filas[-1][0] == tipo:
                filas[-1][1].append((item[1], foto))
            else:
                filas.append((tipo, [(item[1], foto)]))
        return filas, fuera

    def chat_espera(item):
        """Cuánto tarda en llegar el siguiente después de este."""
        tipo = item[0]
        if tipo == "pausa":
            return item[1]
        if tipo in ("aviso", "sale", "vuelve", "borra"):
            return 0.7
        if tipo == "mc":
            return 0.6
        espera = min(1.6, 0.5 + 0.03 * len(item[1]))
        if len(item) > 2:
            espera += 0.4
        return espera

    def chat_reproducir(desde):
        """Hace entrar chat_lista[desde:] con su ritmo. Un clic lo completa.
        Sin animación (estado final directo) en rollback o partida cargada, en modo
        saltar y con «Transiciones» apagado. Suena sfx_celular una vez por ráfaga
        (mensajes seguidos de la misma hermana): la primera con duck, las demás a
        la mitad y sin duck, para que la música no bombee. El MC no suena."""
        lista = store.chat_lista
        if renpy.in_rollback() or renpy.is_skipping() or preferences.transitions == 0:
            store.chat_n = len(lista)
            return
        primero = True
        ultimo = None
        for k in range(desde, len(lista)):
            item = lista[k]
            quien = item[0]
            store.chat_n = k + 1
            if quien in PETALO_COLOR and quien != ultimo:
                if primero:
                    duck(0.4, 0.2, 2.5)
                    renpy.sound.play(audio.sfx_celular, relative_volume=1.5)
                    primero = False
                else:
                    renpy.sound.play(audio.sfx_celular, relative_volume=0.75)
            if quien != "pausa":
                ultimo = quien
            if renpy.pause(chat_espera(item)):
                store.chat_n = len(lista)
                return

    def chat_autocomprobar():
        """Asserts de los datos del chat. Consola: $ chat_autocomprobar()"""
        def cuenta(lista, tipo):
            return len([i for i in lista if i[0] == tipo])
        assert cuenta(CHAT_SEMANA, "sale") == 3, "Nino se sale 3 veces antes del sábado"
        assert cuenta(CHAT_SEMANA, "vuelve") == 3, "Yotsuba la mete 3 veces"
        filas, fuera = chat_filas(CHAT_DEBUT, len(CHAT_DEBUT))
        assert fuera == {"nino"}, "al acabar el debut Nino está fuera"
        filas, fuera = chat_filas(CHAT_SEMANA, len(CHAT_SEMANA))
        assert fuera == set(), "el sábado Nino está dentro"
        for calida in (True, False):
            e6 = chat_e6(calida)
            assert cuenta(e6, "sale") == 0, "en el E6 Nino no se sale"
        assert chat_e6(True)[4][1] == "Sociales: cien."
        assert chat_e6(False)[4][1] == "...Sociales: cien."
        for op in range(3):
            for clima in ("buena", "mixta", "mala"):
                lista = chat_sabado(op, clima)
                assert lista[len(CHAT_SEMANA)][0] == "mc", "el primero nuevo es el del MC"
                filas, fuera = chat_filas(lista, len(lista))
                assert fuera == set()
        filas, fuera = chat_filas(chat_sabado(0, "mixta"), len(chat_sabado(0, "mixta")))
        textos = [m[0] for f in filas if f[0] == "ichika" for m in f[1]]
        assert textos == ["Se eliminó este mensaje", "jajaja"], repr(textos)
        return True


## --- Medidas ---------------------------------------------------------------------
## El celular entero queda por encima de la caja de diálogo (que empieza en y 830):
## atenuado detrás de los diálogos, no tapa ni lo tapan.
define CHAT_W = 560
define CHAT_H = 790
define CHAT_Y = 16
define CHAT_BORDE = 14                 # bisel del celular
define CHAT_CAB = 104                  # alto del encabezado
define CHAT_BARRA = 64                 # alto de la barra de escribir
define CHAT_LISTA_W = CHAT_W - 2 * CHAT_BORDE - 28
define CHAT_LISTA_H = CHAT_H - 2 * CHAT_BORDE - CHAT_CAB - CHAT_BARRA - 20
define CHAT_GLOBO_W = 340
define CHAT_NEUTRO = "#D9D2E6"

init python:

    def chat_redondo(color, radio=14, alpha=1.0):
        """Rectángulo redondeado del color dado, a partir de opcion_neutra (radio 28)."""
        z = radio / 28.0
        return Frame(Transform("ui/opcion_neutra.png", zoom=z, matrixcolor=TintMatrix(color), alpha=alpha),
                     radio, radio, radio, radio)

    ## Foto de perfil: la cara de su chibi (images/chibis, 512×512) en un círculo de su color.
    ## Valor: (expresión, y del centro de la cara en el PNG).
    CHAT_PERFIL = {
        "ichika":  ("feliz", 205),
        "nino":    ("neutral", 222),
        "miku":    ("neutral", 205),
        "yotsuba": ("feliz", 190),
        "itsuki":  ("feliz", 190),
    }

    def chat_foto_perfil(quien, lado):
        expresion, cy = CHAT_PERFIL[quien]
        cara = Transform(MJ_CHIBI_RUTA + quien + "_" + expresion + ".png", crop=(161, cy - 85, 190, 190), xysize=(lado, lado))
        fondo = Transform("ui/hub_sello_fondo.png", matrixcolor=TintMatrix(ui_mezclar(PETALO_COLOR[quien], CORT_FONDO, 0.45)), xysize=(lado, lado))
        disco = Transform("ui/hub_sello_fondo.png", xysize=(lado, lado))
        return AlphaMask(Fixed(fondo, cara, xysize=(lado, lado)), disco)

    def chat_degradado():
        """Lo viejo se pierde por arriba: franjas del fondo, de opacas a transparentes."""
        capas = []
        for k in range(10):
            capas.append(Transform(Solid(CORT_FONDO), xsize=CHAT_LISTA_W, ysize=6, ypos=k * 6, alpha=0.95 - k * 0.095))
        return Fixed(*capas, xysize=(CHAT_LISTA_W, 60))


transform chat_entra:
    alpha 0.0 yoffset 14
    ease 0.25 alpha 1.0 yoffset 0

transform chat_velo:
    on appear:
        alpha 1.0
    on show:
        alpha 0.0
        ease 0.4 alpha 1.0
    on hide:
        ease 0.3 alpha 0.0


## --- Piezas ------------------------------------------------------------------------

## Avatar: la flor en el color de la hermana; el MC, su inicial (nunca una cara).
screen chat_avatar(quien, lado=36):
    fixed:
        xysize (lado, lado)
        if quien == "mc":
            add Transform("ui/hub_sello_fondo.png", matrixcolor=TintMatrix(CHAT_NEUTRO), xysize=(lado, lado))
            text nombre_jugador[:1].upper():
                align (0.5, 0.5)
                font gui.name_text_font
                size int(lado * 0.55)
                color "#2B1B3F"
        else:
            add chat_foto_perfil(quien, lado)

## Boletín en miniatura: los números no se leen.
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

## La almohada de Yotsuba, con cara dibujada.
screen chat_foto_almohada():
    fixed:
        xysize (160, 100)
        add Solid("#2E3A5C")
        add chat_redondo("#F3EEFA", 18):
            xysize (124, 64)
            align (0.5, 0.55)
        text "{font=DejaVuSans.ttf}•◡•{/font}":
            align (0.5, 0.56)
            size 26
            color "#3A2A55"

## La foto de la tarde: el CG en pequeño.
screen chat_foto_grupo():
    add Transform("cg_cinco_aprobadas", xysize=(224, 126))

screen chat_globo(texto, foto, fondo, tinta, quien):
    frame:
        background chat_redondo(fondo, 16)
        padding (16, 10, 16, 10)
        xmaximum CHAT_GLOBO_W
        vbox:
            spacing 8
            if foto == "boletin":
                use e6_chat_foto(quien)
            elif foto == "almohada":
                use chat_foto_almohada
            elif foto == "grupo":
                use chat_foto_grupo
            if foto == "borrado":
                text texto:
                    size 19
                    italic True
                    color "#B9B0C9"
            else:
                text texto:
                    size 21
                    color tinta
                    line_spacing 2

screen chat_fila_hermana(quien, mensajes):
    $ color = PETALO_COLOR[quien]
    hbox:
        spacing 10
        use chat_avatar(quien, 46)
        vbox:
            spacing 5
            text chat_nombre(quien):
                font gui.name_text_font
                size 18
                color color
            for texto, foto in mensajes:
                if foto == "borrado":
                    use chat_globo(texto, foto, ui_mezclar(color, CORT_FONDO, 0.85), "#B9B0C9", quien)
                else:
                    use chat_globo(texto, foto, ui_mezclar(color, CORT_FONDO, 0.62), "#FFF8FC", quien)

screen chat_fila_mc(mensajes):
    hbox:
        xalign 1.0
        spacing 10
        vbox:
            spacing 5
            text "[nombre_jugador]":
                xalign 1.0
                font gui.name_text_font
                size 18
                color CHAT_NEUTRO
            for texto, foto in mensajes:
                frame:
                    xalign 1.0
                    background chat_redondo(CHAT_NEUTRO, 16)
                    padding (16, 10, 16, 10)
                    xmaximum CHAT_GLOBO_W
                    text texto:
                        size 21
                        color "#2B1B3F"
                        line_spacing 2
        use chat_avatar("mc")

screen chat_aviso(texto):
    frame:
        xalign 0.5
        background chat_redondo(ui_mezclar(CORT_FONDO, "#FFFFFF", 0.12), 14)
        padding (16, 6, 16, 6)
        xmaximum 440
        text texto:
            size 17
            color "#E8DFF5"
            text_align 0.5
            xalign 0.5


## --- La pantalla ---------------------------------------------------------------------

screen chat_grupo():

    zorder -5

    default degradado = chat_degradado()

    $ filas, fuera = chat_filas(chat_lista, chat_n)
    $ miembros = 6 - len(fuera)

    add Solid("#0B0712C8")

    fixed:
        xalign 0.5
        ypos CHAT_Y
        xysize (CHAT_W, CHAT_H)

        ## Carcasa y pantalla ciruela
        add chat_redondo("#120A1C", 44) xysize (CHAT_W, CHAT_H)
        add Frame(Transform("ui/opcion_marco.png", zoom=44 / 28.0, matrixcolor=TintMatrix(CHAT_NEUTRO), alpha=0.35), 44, 44, 44, 44) xysize (CHAT_W, CHAT_H)
        add chat_redondo(CORT_FONDO, 32) xpos CHAT_BORDE ypos CHAT_BORDE xysize (CHAT_W - 2 * CHAT_BORDE, CHAT_H - 2 * CHAT_BORDE)

        ## Flor de agua
        add Transform("ui/flor.png", zoom=6.0, alpha=0.05, matrixcolor=TintMatrix(C_ICHIKA)) xalign 0.5 ypos (CHAT_BORDE + CHAT_CAB + 90)

        ## Encabezado: avatar del grupo, nombre y los seis miembros
        fixed:
            xpos CHAT_BORDE
            ypos CHAT_BORDE
            xysize (CHAT_W - 2 * CHAT_BORDE, CHAT_CAB)

            add chat_redondo(ui_mezclar(CORT_FONDO, "#FFFFFF", 0.07), 32) xysize (CHAT_W - 2 * CHAT_BORDE, CHAT_CAB)
            add Solid(ui_mezclar(CORT_FONDO, "#FFFFFF", 0.07)) ypos (CHAT_CAB - 34) xysize (CHAT_W - 2 * CHAT_BORDE, 34)
            add Solid(CHAT_NEUTRO, xsize=CHAT_W - 2 * CHAT_BORDE, ysize=1, alpha=0.18) ypos (CHAT_CAB - 1)

            fixed:
                xpos 18
                yalign 0.5
                xysize (60, 60)
                add Transform("ui/hub_sello_fondo.png", matrixcolor=TintMatrix(ui_mezclar(C_YOTSUBA, CORT_FONDO, 0.55)), xysize=(60, 60))
                add Transform("ui/flor.png", matrixcolor=TintMatrix("#FFF8FC"), xysize=(40, 40)) align (0.5, 0.5)

            vbox:
                xpos 92
                yalign 0.5
                spacing 6
                text "¡Equipo Quintillizas + Tutor!":
                    font gui.name_text_font
                    size 24
                    color "#FFF8FC"
                hbox:
                    spacing 4
                    for h in PETALO_ORDEN:
                        if h in fuera:
                            add Transform("ui/flor.png", matrixcolor=TintMatrix("#8E8A96"), alpha=0.35, xysize=(22, 22)) yalign 0.5
                        else:
                            add Transform("ui/flor.png", matrixcolor=TintMatrix(PETALO_COLOR[h]), xysize=(22, 22)) yalign 0.5
                    use chat_avatar("mc", 22)
                    null width 8
                    text (str(miembros) + " miembros"):
                        yalign 0.5
                        size 16
                        color "#CFC6E0"

        ## Mensajes: pegados abajo; lo viejo se va por arriba (el viewport recorta)
        viewport:
            xpos (CHAT_BORDE + 14)
            ypos (CHAT_BORDE + CHAT_CAB + 10)
            xysize (CHAT_LISTA_W, CHAT_LISTA_H)

            fixed:
                xysize (CHAT_LISTA_W, CHAT_LISTA_H)

                vbox:
                    yalign 1.0
                    xsize CHAT_LISTA_W
                    spacing 14

                    for fila in filas:
                        if fila[0] == "aviso":
                            fixed at chat_entra:
                                xsize CHAT_LISTA_W
                                yfit True
                                use chat_aviso(fila[1])
                        elif fila[0] == "mc":
                            fixed at chat_entra:
                                xsize CHAT_LISTA_W
                                yfit True
                                use chat_fila_mc(fila[1])
                        else:
                            fixed at chat_entra:
                                fit_first True
                                use chat_fila_hermana(fila[0], fila[1])

        add degradado xpos (CHAT_BORDE + 14) ypos (CHAT_BORDE + CHAT_CAB + 10)

        ## Barra de escribir (decorativa)
        fixed:
            xpos (CHAT_BORDE + 14)
            ypos (CHAT_H - CHAT_BORDE - CHAT_BARRA)
            xysize (CHAT_LISTA_W, CHAT_BARRA - 12)
            add chat_redondo(ui_mezclar(CORT_FONDO, "#FFFFFF", 0.08), 24) xysize (CHAT_LISTA_W - 64, CHAT_BARRA - 12)
            text "Mensaje":
                xpos 22
                yalign 0.5
                size 19
                color "#8E86A0"
            fixed:
                xalign 1.0
                xysize (CHAT_BARRA - 12, CHAT_BARRA - 12)
                add Transform("ui/hub_sello_fondo.png", matrixcolor=TintMatrix(ui_mezclar(C_ICHIKA, CORT_FONDO, 0.35)), xysize=(CHAT_BARRA - 12, CHAT_BARRA - 12))
                add Transform("ui/flor.png", matrixcolor=TintMatrix("#FFF8FC"), xysize=(30, 30)) align (0.5, 0.5)

        ## Atenuado: detrás de los diálogos
        showif chat_atenuado:
            add chat_redondo("#05030A", 44, 0.62) xysize (CHAT_W, CHAT_H) at chat_velo


## --- Etiquetas -------------------------------------------------------------------------

## lista: los mensajes. desde: cuántos ya estaban (historial, sin animar ni sonar).
label chat_ver(lista, desde=0):

    $ chat_lista = lista
    $ chat_atenuado = False
    window hide

    if not renpy.get_screen("chat_grupo"):
        $ chat_n = desde
        show screen chat_grupo
        with Dissolve(0.4)

    $ chat_reproducir(desde)

    ## Clic para continuar (el chat ya está entero).
    $ renpy.pause()

    $ chat_atenuado = True
    window auto

    return


## PRUEBA — consola (Shift+O): jump chat_grupo_prueba
## Recorre las tres apariciones: debut, sábado (3 mensajes × 3 climas) y Evento 6
## (Miku cálida y no cálida). No lee ni escribe variables de ruta ni puntos.
label chat_grupo_prueba:

    $ chat_autocomprobar()
    $ quick_menu = False
    scene bg_cuarto_mc
    with fade
    play music hogar fadein 1.0 volume 0.7

    narrador "Prueba del chat · 1 · Debut (interconexión 4)."

    call chat_ver(CHAT_DEBUT) from _call_chat_ver_4
    narrador "Debut: Nino fuera, 5 miembros."
    hide screen chat_grupo
    with dissolve

    $ chat_prueba_op = 0
    while chat_prueba_op < 3:
        $ chat_prueba_cl = 0
        while chat_prueba_cl < 3:
            $ chat_prueba_clima = ["buena", "mixta", "mala"][chat_prueba_cl]
            narrador "Sábado · mensaje [chat_prueba_op] · clima [chat_prueba_clima]."
            call chat_ver(CHAT_SEMANA, len(CHAT_SEMANA)) from _call_chat_ver_5
            narrador "Historial: tres salidas, tres vueltas."
            call chat_ver(chat_sabado(chat_prueba_op, chat_prueba_clima), len(CHAT_SEMANA)) from _call_chat_ver_6
            narrador "Fin del sábado [chat_prueba_op] / [chat_prueba_clima]."
            hide screen chat_grupo
            with dissolve
            $ chat_prueba_cl += 1
        $ chat_prueba_op += 1

    narrador "Evento 6 · Miku cálida."
    call chat_ver(chat_e6(True), 1) from _call_chat_ver_7
    narrador "Nino no se había salido. Ni una vez en toda la semana de exámenes."
    hide screen chat_grupo
    with dissolve

    narrador "Evento 6 · Miku tibia, fría o no visitada."
    call chat_ver(chat_e6(False), 1) from _call_chat_ver_8
    narrador "Fin de la prueba."
    hide screen chat_grupo
    with dissolve

    $ quick_menu = True
    return
