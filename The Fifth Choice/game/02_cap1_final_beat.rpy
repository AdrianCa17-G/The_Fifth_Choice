############################################################################
##  DESPIDO TRAS BEAT 1
##  Despido directo en el beat (Cocina): Maruo despide al MC de forma 
##  inmediata y fría tras una fuerte discusión, provocando la profunda 
############################################################################

label final_malo_beat:

    ############################################################################
    ##  MOVIMIENTO 1 · Maruo
    ##  Maruo se dirige a mc de una manera tensa y fría, mc ya sabe que su
    ##  despido está asegurado, solo falta la sentencia final de Maruo.
    ############################################################################

    stop music fadeout 1.0

    narrador "Fue entonces cuando Maruo levantó la vista y me encontró en la puerta."

    scene cg_maruo_reunion
    with fade
    
    play music contrato fadein 2.0

    maruo "Qué oportuno."

    mc "Buenas tardes."

    mc "Disculpe, no venía a interrumpirlos. Yo solo…"

    maruo "Ya que estás aquí, me ahorras la llamada y  mi tiempo."

    narrador "Dejó la taza sobre la mesa, despacio."

    maruo "Mañana no vengas."

    mc "…¿Perdón?"

    maruo "El contrato queda terminado. Tu padre cobrará lo trabajado hasta hoy."

    mc "Señor, todavía quedan semanas. Si me deja explicarle…"

    ##[CG NUEVO — cg_maruo_espaldas] 

    maruo "No hay nada que explicar."

    maruo "Muchas tardes con mis hijas, y ninguna está más cerca de aprobar que el primer día."

    maruo "Están incluso peor desde que viniste."

    maruo "Las condiciones las sabías desde el principio."

    mc "Por favor, solo un…"

    maruo "No."

    narrador "No levantó la voz. Nunca la levanta."

    narrador "Eso fue lo peor. Ni siquiera sonaba enfadado. Sonaba igual."

    narrador "Nino miraba entre los dos. Quiso decir algo."

    narrador "Pero no lo dijo."
    
    play sound sfx_puerta_cierra volume 1.0
    
    stop music fadeout 2.0

    narrador "Recogió la taza y salió de la cocina sin esperar respuesta."

    narrador "Dándonos la espalda a los dos por igual."

    mc_pensamiento "Lo que ella había pedido a gritos acababa de pasar sin que nadie gritara."

    ############################################################################
    ##  MOVIMIENTO 2 · Lo que pidió
    ##  Nino se da cuenta de lo que provocó, sabe en parte que el despido
    ##  de mc tiene que ver con ella, pero por las actitudes de mc, ella no
    ##  siente nada de culpa.
    ############################################################################

    scene bg_departamento
    with fade
    
    show nino neutral at pj_habla(0.5)
    with dissolve

    if "nino" in hub_visitadas:

        nino "Me dijiste que ibas a durar."

        nino "…"

        nino "Ya ves."

    narrador "Nino no se movió. Seguía con las manos apoyadas en la mesa."

    narrador "Hacía un minuto me quería fuera. Ahora me tenía fuera."

    nino "…"

    nino "Bueno."

    mc "¿«Bueno»? ¿Y así nomás?"

    nino "Era lo que pedí. ¿Qué esperabas? ¿Que me pusiera a llorar por ti?"

    narrador "Lo dijo con esa mirada fría, como siempre."

    narrador "Pero la frase le tardó medio segundo de más en salir."

    nino "El último duró cuatro días. Tú aguantaste más."

    nino "No es un cumplido."

    nino "Aunque si deberías sentirte orgulloso."

    mc_pensamiento "Tenía que sentirse como ganar. Ella lo sabía. Yo lo sabía."

    mc_pensamiento "Y tenía la cara de quien consigue justo lo que pidió."

    mc_pensamiento "Pero sin un sabor de victoria."

    nino "Es mejor así. Hoy. Antes de que se ilusionen más."

    mc "Nino…"

    nino "Y no me mires con esa cara de pena. No te va a servir de nada."

    ############################################################################
    ##  MOVIMIENTO 3 · Las cuatro
    ##  Luego de la discusión, las cuatro hermanas restantes llegan y se
    ##  enteran de lo sucedido, saben que el despido de mc se veía venir, por
    ##  eso no tienen igualmente sentimiento de culpa.
    ############################################################################

    play sound sfx_puerta_abre volume 1.0

    narrador "No pasó ni un minuto." 
    
    narrador "Las cuatro aparecieron por el pasillo casi a la vez."

    narrador "Con cara de haberse levantado de golpe."

    show nino neutral at pj(X_NINO)
    with mover

    show ichika neutral at pj_calla(X_ICHIKA)
    show nino neutral at pj_calla(X_NINO)
    show miku neutral at pj_calla(X_MIKU)
    show yotsuba sorprendida at pj_habla(X_YOTSUBA)
    show itsuki neutral at pj_calla(X_ITSUKI)
    with dissolve

    yotsuba "¡Se oyó hasta la escalera!" 

    yotsuba "Y vimos a papá retirándose del edificio."
    
    yotsuba "¿Quién gritaba? ¿Fue…?"

    narrador "Se detuvo al verme la cara."

    show ichika neutral at pj_habla(X_ICHIKA)
    show yotsuba at pj_calla(X_YOTSUBA)
    with disolucion_lenta

    ichika "Dime que fue una de las discusiones de siempre, Nino."

    show nino neutral at pj_habla(X_NINO)
    show ichika at pj_calla(X_ICHIKA)
    with disolucion_lenta

    nino "Papá lo despidió."

    narrador "Nadie dijo nada. Del pasillo llegaba el ruido del edificio, muy lejos."

    show itsuki at pj_habla(X_ITSUKI)
    show nino neutral at pj_calla(X_NINO)
    with disolucion_lenta

    itsuki "…¿Hoy?"

    show itsuki at pj_calla(X_ITSUKI)
    show nino neutral at pj_habla(X_NINO)
    with disolucion_lenta

    nino "Hoy. Hace cinco minutos."

    show nino neutral at pj_calla(X_NINO)   
    show ichika sonriendo at pj_habla(X_ICHIKA)
    with disolucion_lenta

    ichika "Bueno… al menos fue rápido. ¿No?"

    narrador "Nadie se rió. Ni ella."

    show ichika neutral at pj_habla(X_ICHIKA)
    with disolucion_lenta

    ichika "…Perdón. Es lo que hago cuando no sé qué decir."

    ichika "No te voy a defender, [mc]. No sabría con qué."

    if "ichika" in hub_visitadas:

        ichika "Fuiste correcto conmigo. Como un padre."

        ichika "Y yo te contesté como se contesta a un padre: sonriendo." 
        
        ichika "No sirvió de nada."


    show ichika neutral at pj_calla(X_ICHIKA)
    show yotsuba incomoda at pj_habla(X_YOTSUBA)
    with disolucion_lenta

    yotsuba "Pero si él… él solo estaba…"

    show nino neutral at pj_habla(X_NINO)
    show yotsuba incomoda at pj_calla(X_YOTSUBA)
    with disolucion_lenta

    nino "Yotsuba."

    show nino neutral at pj_calla(X_NINO)
    show yotsuba incomoda at pj_habla(X_YOTSUBA)
    with disolucion_lenta

    yotsuba "…No dije nada."

    narrador "Se quedó mirando el suelo, con las manos juntas delante."

    if "yotsuba" in hub_visitadas:

        narrador "Después, me miró a mí."

        show yotsuba neutral at pj_habla(X_YOTSUBA)
        with disolucion_lenta

        yotsuba "Me dijiste que me concentrara en correr."

        yotsuba "Dejé de contar en voz alta. Pensé que así servía más."

        yotsuba "Ahora no sé si servía de algo."


    show yotsuba at pj_calla(X_YOTSUBA)
    show miku neutral at pj_habla(X_MIKU)
    with disolucion_lenta

    miku "…Yo no pedí esto."

    miku "…Tampoco lo evité."

    narrador "Se llevó las manos a los audífonos." 
    
    narrador "No se los subió. Los dejó ahí, apoyadas."

    if "miku" in hub_visitadas:

        show miku encogida at pj_habla(X_MIKU)
        with disolucion_lenta

        miku "…Dijiste que el Sengoku no entraba en el examen."

        miku "…Tenías razón." 
        
        miku "Por eso no volví a abrir el libro."

    show miku at pj_calla(X_MIKU)
    show itsuki at pj_habla(X_ITSUKI)
    with disolucion_lenta

    itsuki "Te lo dije el primer día. Esto no iba a funcionar."

    itsuki "Ahora lo tengo confirmado. No me hace ninguna gracia."

    if "itsuki" in hub_visitadas:

        itsuki "Me quitaste el cuaderno de las manos." 
        
        itsuki "Me lo resolviste delante de mí."

        itsuki "Eso no se me va a olvidar."


    play music derrota fadein 2.5

    narrador "Intenté decir algo. Itsuki lo notó antes que yo."

    itsuki "No lo digas." 
    
    itsuki "Un «lo siento» ahora sería para ti, no para nosotras."

    narrador "Me quedé callado. No tenía otra cosa que hacer."

    mc_pensamiento "Itsuki tenía razón. Otra vez."

    narrador "Recogí mi mochila. Nadie me detuvo."

    narrador "Tampoco nadie me acompañó hasta la puerta."

    play sound sfx_puerta_cierra volume 1.5

    narrador "La cerré yo mismo. Sin portazo." 
    
    narrador "Para que no pareciera que me enfadaba."

    ############################################################################
    ##  MOVIMIENTO 4 · Casa
    ##  mc llega a casa, a contarles la noticia de su despido, termina en
    ##  un cierre demasiado amargo por parte del lector, ya que sabía que 
    ##  podía tomar mejores decisiones.
    ############################################################################

    scene bg_comedor
    with fade

    stop music fadeout 1.5

    narrador "Llegué a casa a una hora a la que no llegaba desde hace semanas."

    show raiha hablando at pj_habla(0.20)
    show isanari neutral at pj(0.73)
    with dissolve

    raiha "¡Hermanito! Llegaste temprano. ¡Todavía no hay curry!"

    narrador "Se quedó callada al verme la cara."

    raiha "Hermanito... ¿Te encuentras bien?"

    mc "Disculpame, Raiha."

    mc "Me despidieron."

    show raiha preocupada at pj_habla(0.20)
    with disolucion_lenta

    raiha "…¿Qué?"

    isanari "¿Quién?"

    mc "Maruo. Hoy."

    isanari "¿Y el mes? ¿Te pagó lo trabajado?"

    mc "Dijo que si."

    show raiha regano at pj(0.20)
    with disolucion_lenta

    raiha "¡Papá!"

    raiha "Pregúntale cómo está, no cuánto le pagaron."

    isanari "…"

    narrador "Mi papá intentó decir algo. No contestó."

    narrador "Se bajó las gafas de la cabeza y las dejó sobre la mesa, sin mirarlas."

    isanari "Le di mi palabra a Maruo."

    isanari "Le dije que te tomarías esto en serio."

    mc "Me lo tomé en serio."

    isanari "No lo suficiente."

    show raiha preocupada at pj(0.20)
    with disolucion_lenta

    raiha "Hermanito…"

    mc "Todavía no era el examen, Raiha. Me despidieron antes."

    raiha "¿Pero por qué?"

    mc "Porque no hice nada. Dos semanas, y no hice nada."

    narrador "Raiha no dijo que no fuera verdad."

    narrador "Eso me dolió más que si lo hubiera dicho."

    ############################################################################
    ##  MOVIMIENTO 5 · La libreta
    ##  Cierre final, del despido temprano, mc vuelve a abrir su libreta
    ##  y se da cuenta que no hizo nada y que todo fue en vano.
    ############################################################################

    scene bg_cuarto_mc
    with fade
    
    scene cg_libreta
    with fade

    narrador "Abrí la libreta por la página de los cinco nombres."

    narrador "Debajo de la línea estaba la frase de aquella noche."

    mc_pensamiento "«Voy a ir de una en una.»"

    mc_pensamiento "Fui de una en una. Y las dos veces me equivoqué."

    mc_pensamiento "Ni siquiera llegué a la mitad de los treinta días."

    mc_pensamiento "La deuda sigue exactamente donde estaba."

    narrador "Cerré la libreta. Apagué la lámpara."

    narrador "No hubo ninguna frase que anotar esta vez."

    narrador "Todo terminó. En un fracaso." 
    
    narrador "Y un despido temprano."

    jump final_malo_cierre