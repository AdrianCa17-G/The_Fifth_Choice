################################################################################
##  La Variante A del final malo del Capítulo 1 representa el 
##  fracaso absoluto del protagonista como tutor al no lograr conectar ni guiar
##  a las quintillizas. 
##  Despido directo en el beat (Cocina): Maruo despide al MC de forma 
##  inmediata y fría tras una fuerte discusión, provocando la profunda 
##  tristeza y decepción de Raiha e Isanari en casa. 
################################################################################

label final_malo_temprano:


    $ ui_escena("normal")
    stop music fadeout 1.0

    if despido_en_beat:
        jump final_malo_beat

    jump final_malo_hub3


label final_malo_cierre:

    scene bg_negro
    with fade

    $ persistent.final_malo_temprano_visto = True

    ## Tarjeta de final: texto centrado sobre negro, sin música.
    narrador "FINAL MALO · Despido temprano"

    return
