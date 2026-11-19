# ============================================================
# 02_cap1_hubs.rpy
# ============================================================
#
# hub_visitadas y las variables maruo_ultimatum, despido_cap1,
# tiempo_restante y nino_rama_beat se declaran en 00_definiciones.rpy.
# La función rama_de() también vive allí.

default LABEL_EVENTO = {
    "itsuki": "hub_Itsuki",
    "yotsuba": "hub_Yotsuba",
    "miku": "hub_Miku",
    "nino": "hub_Nino",
    "ichika": "hub_Ichika"
}


# ------------------------------------------------------------
label hub_1:

    $ tiempo_restante = "casi cuatro semanas"

    ## Tarjeta de entrada al hub; la música del mapa empieza después.
    call cortinilla_hub(1) from _call_cortinilla_hub

    play music hub fadein 1.5

    $ quick_menu = False
    call screen mapa_hub(1)
    $ quick_menu = True
    $ destino = _return

    ## Tarjeta de salida: color, lugar y nota de la hermana elegida.
    stop music fadeout 0.8
    call cortinilla_hermana(destino) from _call_cortinilla_hermana

    $ ui_escena("hub", destino, HUB_LUGAR[destino])
    call expression (LABEL_EVENTO.get(destino, "evento_" + destino)) from _call_expression_20
    $ ui_escena("normal")
    $ hub_visitadas.append(destino)
    call hub_completado(destino, 1) from _call_hub_completado

    stop music fadeout 1.0

    jump cap1_interconexion_2



# ------------------------------------------------------------
label hub_2:

    $ tiempo_restante = "dos semanas"

    call cortinilla_hub(2) from _call_cortinilla_hub_1

    play music hub fadein 1.5

    $ quick_menu = False
    call screen mapa_hub(2)
    $ quick_menu = True
    $ destino = _return

    stop music fadeout 0.8
    call cortinilla_hermana(destino) from _call_cortinilla_hermana_1

    $ ui_escena("hub", destino, HUB_LUGAR[destino])
    call expression (LABEL_EVENTO.get(destino, "evento_" + destino)) from _call_expression_21
    $ ui_escena("normal")
    $ hub_visitadas.append(destino)
    call hub_completado(destino, 2) from _call_hub_completado_1

    stop music fadeout 1.0

    jump cap1_interconexion_4



# ------------------------------------------------------------
label hub_3:

    $ tiempo_restante = "pocos días"

    call cortinilla_hub(3) from _call_cortinilla_hub_2

    play music hub fadein 1.5

    $ quick_menu = False
    call screen mapa_hub(3)
    $ quick_menu = True
    $ destino = _return

    stop music fadeout 0.8
    call cortinilla_hermana(destino) from _call_cortinilla_hermana_2

    $ ui_escena("hub", destino, HUB_LUGAR[destino])
    call expression (LABEL_EVENTO.get(destino, "evento_" + destino)) from _call_expression_22
    $ ui_escena("normal")
    $ hub_visitadas.append(destino)
    call hub_completado(destino, 3) from _call_hub_completado_2

    stop music fadeout 1.0

    ## Con aviso activo, un segundo desaire en el hub 3 es el despido.
    if maruo_ultimatum and rama_de(destino) == "fria":
        $ despido_cap1 = True
    else:
        $ despido_cap1 = False

    ## Foto para Extras → Repetir → Semana de exámenes (08_extras.rpy).
    $ extra_foto_hub3()
    ## Extras → Repetir → Días de tutoría acaba aquí (fuera de un Replay no hace nada).
    $ renpy.end_replay()

    jump cap1_interconexion_6