# ============================================================
# 02_capitulo1_conexiones.rpy
# ============================================================
# Única función: encadenar el Capítulo 1 tal como está en
# docs/CAP1.md §2. NO contiene diálogo propio — solo call/jump a
# los labels que viven en el resto de los .rpy de este capítulo.
#
# hub_visitadas se declara UNA sola vez, en 00_definiciones.rpy.
# No repetir el "default" acá.
#
# Esqueleto:
# APERTURA → HUB 1 → evento → BEAT Itsuki → HUB 2 → evento
# → BEAT crisis de Nino → HUB 3 → evento → BEAT casa → EVENTO 6
#
# 02_cap1_apertura.rpy termina con "jump hub_1" — por eso hub_1,
# hub_2 y hub_3 son labels propios acá abajo, no un solo bloque.

# ------------------------------------------------------------
# Mapa de excepciones: hermana → nombre real del label, solo para
# los casos donde no sigue la convención "evento_<hermana>".
# Si el label de alguien no está acá, se asume "evento_<hermana>".
# ------------------------------------------------------------
default LABEL_EVENTO = {
    "itsuki": "hub_Itsuki",
    "miku": "hub_Miku",
    # agregar acá más excepciones a medida que aparezcan, ej:
    # "nino": "nino_evento_real",
}


# ------------------------------------------------------------
label hub_1:
    call screen mapa_hub(1)
    $ destino = _return
    call expression (LABEL_EVENTO.get(destino, "evento_" + destino))
    $ hub_visitadas.append(destino)
    if desaires_cap1 >= 3:
        jump final_malo_temprano

    call beat_itsuki
    jump hub_2

# ------------------------------------------------------------
label hub_2:
    call screen mapa_hub(2)
    $ destino = _return
    call expression (LABEL_EVENTO.get(destino, "evento_" + destino))
    $ hub_visitadas.append(destino)
    if desaires_cap1 >= 3:
        jump final_malo_temprano

    # Aviso diegético (README "El contador de desaires")
    if desaires_cap1 >= 2:
        call aviso_maruo

    call beat_nino_crisis
    jump hub_3

# ------------------------------------------------------------
label hub_3:
    call screen mapa_hub(3)
    $ destino = _return
    call expression (LABEL_EVENTO.get(destino, "evento_" + destino))
    $ hub_visitadas.append(destino)
    if desaires_cap1 >= 3:
        jump final_malo_temprano

    call beat_casa
    call evento_6
    jump capitulo2   # todavía no existe (README: 03_capitulo2.rpy pendiente)
