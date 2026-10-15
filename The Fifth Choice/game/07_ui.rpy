################################################################################
##  07_ui.rpy — Interfaz propia (cajas de texto y flor de sakura)
################################################################################
## init -5: se ejecuta ANTES que los `define` de 00_definiciones.rpy,
## que necesitan estas funciones para crear los personajes.
## Las fuentes japonesas centran el carácter … en vertical (flota a media
## altura de las letras). Se cambia por tres puntos normales al mostrarlo.
init -5 python:

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


    def decision_peso(hermana, pistas=None):
        """Marca la siguiente decisión como 'con peso'.
        pistas: temperatura de cada opción, en el orden en que aparecen."""
        store.decision_hermana = hermana
        if pistas is None:
            store.decision_pistas = ["calida", "tibia", "fria"]
        else:
            store.decision_pistas = pistas


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
screen flor_sakura(activa=None, tipo="hablante", x=1450, y=844):
    fixed:
        xpos x
        ypos y
        xysize (160, 160)

        for i in range(5):
            $ hermana = PETALO_ORDEN[i]
            if activa == "todas":
                add "ui/petalo.png" at petalo_giro(i, PETALO_COLOR[hermana], 0.95)
            elif activa == hermana:
                add "ui/petalo.png" at petalo_giro(i, "#FFFFFF", 0.95)
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
define PISTA_FUERZA = 0.30

transform decision_velo:
    alpha 0.0
    linear 0.4 alpha 0.5

transform tarjeta_entrada(n):
    alpha 0.0
    yoffset 70
    pause (0.12 * n)
    linear 0.35 alpha 1.0 yoffset 0

transform tarjeta_hover:
    on idle:
        linear 0.15 yoffset 0
    on hover:
        linear 0.15 yoffset -14

style tarjeta_texto is default:
    size 31
    color "#F3EEFA"
    xpos 44
    ypos 60
    xsize 432
    line_spacing 4

screen choice_peso(items):

    $ color = PETALO_COLOR[decision_hermana]

    add Solid("#000000") at decision_velo

    hbox:
        xalign 0.5
        yalign 0.40
        spacing 40

        for n, i in enumerate(items):

            $ pista = decision_pistas[n]
            $ tono = "#FFFFFF"
            $ fuerza = 0.0
            if pista == "calida":
                $ tono = "#FFC46B"
                $ fuerza = PISTA_FUERZA
            elif pista == "fria":
                $ tono = "#7FA6E8"
                $ fuerza = PISTA_FUERZA

            fixed:
                xysize (520, 440)
                at tarjeta_entrada(n)

                button:
                    xysize (520, 440)
                    background None
                    action i.action
                    hover_sound audio.sfx_hover
                    activate_sound audio.sfx_click
                    at tarjeta_hover

                    add "ui/tarjeta.png"
                    add "ui/halo.png" matrixcolor TintMatrix(tono) alpha fuerza
                    add ("ui/deco_tarjeta_" + decision_hermana + ".png")
                    add "ui/tarjeta_marco.png" matrixcolor TintMatrix(color)
                    use flor_sakura(decision_hermana, "hablante", 380, 290)
                    text i.caption style "tarjeta_texto"