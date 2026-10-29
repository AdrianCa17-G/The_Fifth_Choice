################################################################################
##  07b_collage.rpy — Collage de pensamientos (beat casa)
##
##  Cuando mc piensa en una hermana que SÍ visitó, se enseña un collage:
##  fondo de pétalos de su color y su motivo → su sprite → los 4 CG, uno a uno.
##  Mientras dura se ocultan la cinta del beat, el menú rápido y las franjas
##  de los bordes (todo cuelga de `quick_menu`); solo quedan collage y caja.
##  Al terminar se vuelve a la libreta y la interfaz regresa.
##
##  Si la hermana NO fue visitada no pasa nada: solo la caja de pensamiento.
##
##  Fondos: herramientas/generar_fondos_collage.py → game/ui/collage_fondo_*.webp
##  Uso desde el guion (dos líneas por hermana, ver CAP1_beat_casa):
##      call collage_abrir("ichika")
##      ...pensamientos...
##      call collage_cerrar
################################################################################


################################################################################
##  DATOS — aquí se ajusta todo
################################################################################

## Los 4 CG de cada hermana, en este orden de aparición. Las posiciones son
## las de COLLAGE_POS: arriba-izq, abajo-izq, arriba-der, abajo-der.
define COLLAGE_CG = {
    "ichika":  ["cg_ichika_puerta", "cg_ichika_ensayo", "cg_ichika_desarmada", "cg_ichika_mascara"],
    "nino":    ["cg_nino_pasillo", "cg_nino_centro_comercial", "cg_nino_receta", "cg_nino_grieta_cocina"],
    "miku":    ["cg_miku_sofa", "cg_miku_biblioteca", "cg_miku_estudio", "cg_miku_sorpresa"],
    "yotsuba": ["cg_yotsuba_corriendo", "cg_yotsuba_pista", "cg_yotsuba_rotulador", "cg_yotsuba_cronometro"],
    "itsuki":  ["cg_itsuki_azotea_cuaderno", "cg_itsuki_atascada", "cg_itsuki_contraida", "cg_itsuki_reto"],
}

## (x, y, ángulo) del CENTRO de cada polaroid, en píxeles de 1920x1080.
## Ángulo positivo = gira a la derecha. Sube las dos filas de abajo si la
## caja de texto te tapa demasiado (por ejemplo y = 660 en vez de 708).
define COLLAGE_POS = [
    (400, 220, 5),
    (400, 640, -5),
    (1539, 220, -5),
    (1539, 640, 5),
]

## Tiempos (segundos)
define COLLAGE_PAUSA_FOTO = 0.55     # entre un CG y el siguiente
define collage_t_fondo = Dissolve(0.9)
define collage_t_sprite = Dissolve(0.7)

default collage_activo = False


################################################################################
##  TRANSFORMS
################################################################################

## El sprite va centrado, apoyado abajo, un poco ampliado.
transform collage_sprite_pos:
    xanchor 0.5
    yanchor 1.0
    xpos 0.5
    ypos 1.0
    zoom 1.15

## Cada polaroid "cae" sobre el fondo: aparece, se achica y se endereza.
## Anclada por el centro para que el giro no la desplace.
transform collage_polaroid_in(cx, cy, ang):
    xanchor 0.5
    yanchor 0.5
    xpos cx
    ypos cy
    rotate (ang - 7)
    alpha 0.0
    zoom 1.18
    ease 0.55 alpha 1.0 zoom 1.0 rotate ang


################################################################################
##  FUNCIONES
################################################################################

## Va en init 10 para que existan PETALO_ORDEN y los define de 07_ui.rpy.
init 10 python:

    ## Un fondo por hermana: muro de pétalos (PNG) + pétalos cayendo encima.
    for _h in PETALO_ORDEN:
        renpy.image("collage_fondo_" + _h, Fixed(
            "ui/collage_fondo_" + _h + ".webp",
            SnowBlossom("ui/caida_" + _h + "_petalo.png", count=5, border=50,
                        yspeed=(60, 130), xspeed=(20, 60)),
            SnowBlossom("ui/caida_" + _h + "_flor.png", count=2, border=50,
                        yspeed=(50, 110), xspeed=(20, 50)),
        ))

    def collage_visitada(hermana):
        """True si esa hermana tuvo su evento de hub (sin importar la rama)."""
        return bool(getattr(store, hermana + "_visitada_cap1", False))

    def collage_polaroid(nombre_cg):
        """Foto con marco blanco, sin posición: la pone el transform."""
        foto = Transform(nombre_cg, xysize=(520, 293), fit="cover")
        return Fixed(
            Solid("#FFF8FC", xsize=548, ysize=321),
            Transform(foto, xpos=14, ypos=14),
            xysize=(548, 321))

    def collage_poner_fotos(hermana):
        """Enseña los CG uno a uno. Cada uno tiene su propia etiqueta para que
        `scene` los borre todos de golpe al cerrar."""
        fotos = COLLAGE_CG[hermana]
        for n in range(len(fotos)):
            x, y, ang = COLLAGE_POS[n]
            etiqueta = "collage_foto_" + str(n)
            renpy.show(etiqueta,
                       what=collage_polaroid(fotos[n]),
                       at_list=[collage_polaroid_in(x, y, ang)],
                       tag=etiqueta)
            renpy.pause(COLLAGE_PAUSA_FOTO)


################################################################################
##  LABELS
################################################################################

## Abre el collage de una hermana. Si no fue visitada, no hace nada.
label collage_abrir(hermana):

    if not collage_visitada(hermana):
        return

    $ collage_activo = True

    ## Sin cinta del beat, sin menú rápido, sin franjas.
    $ quick_menu = False

    ## 1 · El fondo.
    scene expression ("collage_fondo_" + hermana)
    with collage_t_fondo

    ## 2 · El sprite.
    show expression (hermana + " neutral") as collage_sprite at collage_sprite_pos
    with collage_t_sprite

    ## 3 · Los 4 CG, uno tras otro.
    $ collage_poner_fotos(hermana)

    return


## Cierra el collage y vuelve a la libreta. Si no había collage, no hace nada.
label collage_cerrar:

    if not collage_activo:
        return

    $ collage_activo = False

    ## `scene` borra fondo, sprite y polaroids de una vez.
    scene cg_libreta
    with fade

    $ quick_menu = True

    return
