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

    call screen mapa_hub(1)
    $ destino = _return
    call expression (LABEL_EVENTO.get(destino, "evento_" + destino))
    $ hub_visitadas.append(destino)

    jump interconexion_2



# ------------------------------------------------------------
label hub_2:

    $ tiempo_restante = "tres semanas"

    call screen mapa_hub(2)
    $ destino = _return
    call expression (LABEL_EVENTO.get(destino, "evento_" + destino))
    $ hub_visitadas.append(destino)

    jump interconexion_4



# ------------------------------------------------------------
label hub_3:

    $ tiempo_restante = "pocos días"

    call screen mapa_hub(3)
    $ destino = _return
    call expression (LABEL_EVENTO.get(destino, "evento_" + destino))
    $ hub_visitadas.append(destino)

    ## Con aviso activo, un segundo desaire en el hub 3 es el despido.
    if maruo_ultimatum and rama_de(destino) == "fria":
        $ despido_cap1 = True
    else:
        $ despido_cap1 = False

    jump interconexion_6
