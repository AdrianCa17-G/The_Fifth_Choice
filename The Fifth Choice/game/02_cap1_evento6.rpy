################################################################################
##  02_cap1_evento6.rpy — EVENTO 6 (cierre del Capítulo 1). STUBS del chat 1.
##  Entrada: jump evento_6 (desde cap1_interconexion_6). Pila de call vacía.
##  Contrato: ANALISIS_EVENTO_6.md §3.7.
################################################################################

default e6_i = 0
default e6_h = ""
default e6_cola = []

label evento_6:

    $ e6_iniciar()

    call e6_lunes
    call e6_bloque("yotsuba")
    call e6_bloque("ichika")
    call e6_bloque("nino")
    call e6_bloque("itsuki")
    call e6_bloque("miku")
    call e6_resultados
    call e6_cinco
    call e6_casa
    call e6_cuarto

    $ e6_cerrar()

    jump cap2_inicio


## --- Despachador de bloque (Mov. 2–6) -----------------------------------------
label e6_bloque(h):

    call expression ("e6_" + h + "_nucleo")
    call expression ("e6_" + h + "_mono_" + e6_estado_de(h))
    if e6_estado_de(h) == "calida":
        call expression ("e6_" + h + "_mj")
    if e6_estado_de(h) == "no_visitada":
        call expression ("e6_" + h + "_promesa")
    $ e6_marcar_ganchos(h)
    call expression ("e6_" + h + "_gesto_" + e6_estado_de(h))
    return


## --- Movimientos globales -----------------------------------------------------
label e6_lunes:
    narrador "[[STUB e6_lunes · Mov. 1]"
    call expression ("e6_s1_" + e6_estado_entrada)
    return

label e6_resultados:
    narrador "[[STUB e6_resultados · Mov. 7]"
    call expression ("e6_s2_" + e6_estado_entrada)
    return

label e6_cinco:
    narrador "[[STUB e6_cinco · Mov. 8]"
    $ e6_cola = e6_orden_ecos()
    $ e6_i = 0
    while e6_i < 5:
        $ e6_h = e6_cola[e6_i]
        call expression ("e6_" + e6_h + "_eco_" + e6_estado_de(e6_h))
        $ e6_i += 1
    return

label e6_casa:
    narrador "[[STUB e6_casa · Mov. 9]"
    return

label e6_cuarto:
    narrador "[[STUB e6_cuarto · Mov. 10]"
    call expression ("e6_s3_" + e6_estado_entrada)
    return


## --- Slots del estado_entrada (S1, S2, S3) ------------------------------------
label e6_s1_superado:
    narrador "[[STUB e6_s1_superado]"
    return

label e6_s1_mixto:
    narrador "[[STUB e6_s1_mixto]"
    return

label e6_s1_bueno:
    narrador "[[STUB e6_s1_bueno]"
    return

label e6_s2_superado:
    narrador "[[STUB e6_s2_superado]"
    return

label e6_s2_mixto:
    narrador "[[STUB e6_s2_mixto]"
    return

label e6_s2_bueno:
    narrador "[[STUB e6_s2_bueno]"
    return

label e6_s3_superado:
    narrador "[[STUB e6_s3_superado]"
    return

label e6_s3_mixto:
    narrador "[[STUB e6_s3_mixto]"
    return

label e6_s3_bueno:
    narrador "[[STUB e6_s3_bueno]"
    return


## ============================ YOTSUBA ==========================================
label e6_yotsuba_nucleo:
    narrador "[[STUB e6_yotsuba_nucleo]"
    return

label e6_yotsuba_mono_calida:
    narrador "[[STUB e6_yotsuba_mono_calida]"
    return

label e6_yotsuba_mono_tibia:
    narrador "[[STUB e6_yotsuba_mono_tibia]"
    return

label e6_yotsuba_mono_fria:
    narrador "[[STUB e6_yotsuba_mono_fria]"
    return

label e6_yotsuba_mono_no_visitada:
    narrador "[[STUB e6_yotsuba_mono_no_visitada]"
    return

label e6_yotsuba_mj:
    narrador "[[STUB e6_yotsuba_mj]"
    call mj_ejecutar(E6_MJ_JUEGO["yotsuba"], "yotsuba")
    return

label e6_yotsuba_promesa:
    narrador "[[STUB e6_yotsuba_promesa]"
    return

label e6_yotsuba_gesto_calida:
    narrador "[[STUB e6_yotsuba_gesto_calida]"
    return

label e6_yotsuba_gesto_tibia:
    narrador "[[STUB e6_yotsuba_gesto_tibia]"
    return

label e6_yotsuba_gesto_fria:
    narrador "[[STUB e6_yotsuba_gesto_fria]"
    return

label e6_yotsuba_gesto_no_visitada:
    narrador "[[STUB e6_yotsuba_gesto_no_visitada]"
    return

label e6_yotsuba_eco_calida:
    narrador "[[STUB e6_yotsuba_eco_calida]"
    return

label e6_yotsuba_eco_tibia:
    narrador "[[STUB e6_yotsuba_eco_tibia]"
    return

label e6_yotsuba_eco_fria:
    narrador "[[STUB e6_yotsuba_eco_fria]"
    return

label e6_yotsuba_eco_no_visitada:
    narrador "[[STUB e6_yotsuba_eco_no_visitada]"
    return


## ============================= ICHIKA ==========================================
label e6_ichika_nucleo:
    narrador "[[STUB e6_ichika_nucleo]"
    return

label e6_ichika_mono_calida:
    narrador "[[STUB e6_ichika_mono_calida]"
    return

label e6_ichika_mono_tibia:
    narrador "[[STUB e6_ichika_mono_tibia]"
    return

label e6_ichika_mono_fria:
    narrador "[[STUB e6_ichika_mono_fria]"
    return

label e6_ichika_mono_no_visitada:
    narrador "[[STUB e6_ichika_mono_no_visitada]"
    return

label e6_ichika_mj:
    narrador "[[STUB e6_ichika_mj]"
    call mj_ejecutar(E6_MJ_JUEGO["ichika"], "ichika")
    return

label e6_ichika_promesa:
    narrador "[[STUB e6_ichika_promesa]"
    return

label e6_ichika_gesto_calida:
    narrador "[[STUB e6_ichika_gesto_calida]"
    return

label e6_ichika_gesto_tibia:
    narrador "[[STUB e6_ichika_gesto_tibia]"
    return

label e6_ichika_gesto_fria:
    narrador "[[STUB e6_ichika_gesto_fria]"
    return

label e6_ichika_gesto_no_visitada:
    narrador "[[STUB e6_ichika_gesto_no_visitada]"
    return

label e6_ichika_eco_calida:
    narrador "[[STUB e6_ichika_eco_calida]"
    return

label e6_ichika_eco_tibia:
    narrador "[[STUB e6_ichika_eco_tibia]"
    return

label e6_ichika_eco_fria:
    narrador "[[STUB e6_ichika_eco_fria]"
    return

label e6_ichika_eco_no_visitada:
    narrador "[[STUB e6_ichika_eco_no_visitada]"
    return


## ============================== NINO ===========================================
label e6_nino_nucleo:
    narrador "[[STUB e6_nino_nucleo]"
    return

label e6_nino_mono_calida:
    narrador "[[STUB e6_nino_mono_calida]"
    return

label e6_nino_mono_tibia:
    narrador "[[STUB e6_nino_mono_tibia]"
    return

label e6_nino_mono_fria:
    narrador "[[STUB e6_nino_mono_fria]"
    return

label e6_nino_mono_no_visitada:
    narrador "[[STUB e6_nino_mono_no_visitada]"
    return

label e6_nino_mj:
    narrador "[[STUB e6_nino_mj]"
    call mj_ejecutar(E6_MJ_JUEGO["nino"], "nino")
    return

label e6_nino_promesa:
    narrador "[[STUB e6_nino_promesa]"
    return

label e6_nino_gesto_calida:
    narrador "[[STUB e6_nino_gesto_calida]"
    return

label e6_nino_gesto_tibia:
    narrador "[[STUB e6_nino_gesto_tibia]"
    return

label e6_nino_gesto_fria:
    narrador "[[STUB e6_nino_gesto_fria]"
    return

label e6_nino_gesto_no_visitada:
    narrador "[[STUB e6_nino_gesto_no_visitada]"
    return

label e6_nino_eco_calida:
    narrador "[[STUB e6_nino_eco_calida]"
    return

label e6_nino_eco_tibia:
    narrador "[[STUB e6_nino_eco_tibia]"
    return

label e6_nino_eco_fria:
    narrador "[[STUB e6_nino_eco_fria]"
    return

label e6_nino_eco_no_visitada:
    narrador "[[STUB e6_nino_eco_no_visitada]"
    return


## ============================= ITSUKI ==========================================
label e6_itsuki_nucleo:
    narrador "[[STUB e6_itsuki_nucleo]"
    return

label e6_itsuki_mono_calida:
    narrador "[[STUB e6_itsuki_mono_calida]"
    return

label e6_itsuki_mono_tibia:
    narrador "[[STUB e6_itsuki_mono_tibia]"
    return

label e6_itsuki_mono_fria:
    narrador "[[STUB e6_itsuki_mono_fria]"
    return

label e6_itsuki_mono_no_visitada:
    narrador "[[STUB e6_itsuki_mono_no_visitada]"
    return

label e6_itsuki_mj:
    narrador "[[STUB e6_itsuki_mj]"
    call mj_ejecutar(E6_MJ_JUEGO["itsuki"], "itsuki")
    return

label e6_itsuki_promesa:
    narrador "[[STUB e6_itsuki_promesa]"
    return

label e6_itsuki_gesto_calida:
    narrador "[[STUB e6_itsuki_gesto_calida]"
    return

label e6_itsuki_gesto_tibia:
    narrador "[[STUB e6_itsuki_gesto_tibia]"
    return

label e6_itsuki_gesto_fria:
    narrador "[[STUB e6_itsuki_gesto_fria]"
    return

label e6_itsuki_gesto_no_visitada:
    narrador "[[STUB e6_itsuki_gesto_no_visitada]"
    return

label e6_itsuki_eco_calida:
    narrador "[[STUB e6_itsuki_eco_calida]"
    return

label e6_itsuki_eco_tibia:
    narrador "[[STUB e6_itsuki_eco_tibia]"
    return

label e6_itsuki_eco_fria:
    narrador "[[STUB e6_itsuki_eco_fria]"
    return

label e6_itsuki_eco_no_visitada:
    narrador "[[STUB e6_itsuki_eco_no_visitada]"
    return


## ============================== MIKU ===========================================
label e6_miku_nucleo:
    narrador "[[STUB e6_miku_nucleo]"
    return

label e6_miku_mono_calida:
    narrador "[[STUB e6_miku_mono_calida]"
    return

label e6_miku_mono_tibia:
    narrador "[[STUB e6_miku_mono_tibia]"
    return

label e6_miku_mono_fria:
    narrador "[[STUB e6_miku_mono_fria]"
    return

label e6_miku_mono_no_visitada:
    narrador "[[STUB e6_miku_mono_no_visitada]"
    return

label e6_miku_mj:
    narrador "[[STUB e6_miku_mj]"
    call mj_ejecutar(E6_MJ_JUEGO["miku"], "miku")
    return

label e6_miku_promesa:
    narrador "[[STUB e6_miku_promesa]"
    return

label e6_miku_gesto_calida:
    narrador "[[STUB e6_miku_gesto_calida]"
    return

label e6_miku_gesto_tibia:
    narrador "[[STUB e6_miku_gesto_tibia]"
    return

label e6_miku_gesto_fria:
    narrador "[[STUB e6_miku_gesto_fria]"
    return

label e6_miku_gesto_no_visitada:
    narrador "[[STUB e6_miku_gesto_no_visitada]"
    return

label e6_miku_eco_calida:
    narrador "[[STUB e6_miku_eco_calida]"
    return

label e6_miku_eco_tibia:
    narrador "[[STUB e6_miku_eco_tibia]"
    return

label e6_miku_eco_fria:
    narrador "[[STUB e6_miku_eco_fria]"
    return

label e6_miku_eco_no_visitada:
    narrador "[[STUB e6_miku_eco_no_visitada]"
    return


## ============================= CAPÍTULO 2 ======================================
## Stub de salida. BORRAR cuando exista 03_capitulo2.rpy (label duplicado).
label cap2_inicio:
    narrador "[[STUB cap2_inicio · Capítulo 2 pendiente]"
    return