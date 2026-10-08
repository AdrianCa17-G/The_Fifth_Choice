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

    ## El ultimátum se activa dentro de beat_Nino si hay 2 desaires.
    call beat_Nino
    jump interconexion_3



# ------------------------------------------------------------
label hub_3:

    $ tiempo_restante = "una semana"

    call screen mapa_hub(3)
    $ destino = _return
    call expression (LABEL_EVENTO.get(destino, "evento_" + destino))
    $ hub_visitadas.append(destino)

    ## Con ultimátum activo, el tercer evento tiene que haber sido cálido.
    if maruo_ultimatum and rama_de(destino) != "calida":
        $ despido_cap1 = True
    else:
        $ despido_cap1 = False

    ## beat_casa lee despido_cap1 para mostrar la duda de Futaro.
    call beat_casa

    if despido_cap1:
        jump final_malo_temprano

    call evento_6
    jump capitulo2
