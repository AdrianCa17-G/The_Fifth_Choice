################################################################################
##  07_ui.rpy — Interfaz propia (cajas de texto y flor de sakura)
################################################################################

## init -5: se ejecuta ANTES que los `define` de 00_definiciones.rpy,
## que necesitan estas funciones para crear los personajes.
init -5 python:

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

    def ui_personaje(nombre, color, petalo=None):
        """Personaje con caja rellena de su color.
        - la caja usa `color`
        - la placa del nombre es el mismo color, más claro
        - el texto del nombre es el mismo color, mucho más oscuro
        """
        placa = ui_mezclar(color, "#FFFFFF", 0.45)
        tinta = ui_mezclar(color, "#000000", 0.72)
        return Character(
            nombre,
            what_color="#241B33",
            window_style="caja",
            window_background=Transform("ui/caja.png", matrixcolor=TintMatrix(color)),
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
screen flor_sakura(activa=None, tipo="hablante"):
    fixed:
        xpos 1450
        ypos 844
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