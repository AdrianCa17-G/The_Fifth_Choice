# ============================================================
# 02_capitulo1_conexiones.rpy
# ============================================================
# Encadena el Capítulo 1 tal como está en docs/CAP1.md §2 y hace
# las transiciones cortas entre los main events.
#
# Esqueleto:
# APERTURA → INTERCONEXIÓN 1 → HUB 1 → INTERCONEXIÓN 2 → BEAT Itsuki
# → INTERCONEXIÓN 3 → HUB 2 → INTERCONEXIÓN 4 → BEAT crisis de Nino  
# → INTERCONEXIÓN 5 → HUB 3 → INTERCONEXIÓN 5 → BEAT casa → EVENTO 6

################################################################################
##  REACCIONES DE LA HERMANA VISITADA (reutilizables)
##  Antes de llamar: $ rama_hub = rama_de(destino)  y  $ nombre_h = destino.capitalize()
################################################################################

label reaccion_hermana_visitada:

    if destino == "ichika":

        call reaccion_ichika

    elif destino == "nino":

        call reaccion_nino

    elif destino == "miku":

        call reaccion_miku

    elif destino == "yotsuba":

        call reaccion_yotsuba

    else:

        call reaccion_itsuki

    return


# ------------------------------------------------------------
label reaccion_ichika:

    play music ichika fadein 2.0

    if rama_hub1 == "calida":

        show ichika sonriendo at pj_habla(0.5)
        with dissolve

        ichika "¡Buenos días, [mc]!"

        ichika "Logré dormir siete horas y media."

        ichika "¡He conseguido un récord personal!"

        mc "¿De verdad?"

        ichika "Siete y cuarto. Pero redondeo hacia arriba."

        show ichika neutral at pj_habla(0.5)
        with disolucion_lenta

        ichika "…Tú deberías hacer lo mismo. Dormir, digo."

        ichika "Siempre estás cuidando de las demás."

        show ichika determinada at pj_habla(0.5)
        with disolucion_lenta

        ichika "¿Pero quién cuida de ti?"  

        show ichika sonriendo at pj_habla(0.5)
        with disolucion_lenta

        ichika "Yo puedo hacerlo. Si me dejas."

        ichika "Con mucho gusto. Jeje…"

        ichika "¡Consejo gratis! Exclusivo para ti [mc]"

        ichika "¡No se lo cuentes a nadie!"

        show ichika at pj_calla(0.5)
        with disolucion_lenta

        mc_pensamiento "No supe qué contestar. Nadie me lo había preguntado en años."


    elif rama_hub1 == "tibia":

        show ichika sonriendo at pj_habla(0.5)
        with dissolve

        ichika "¡Buenos días, señor de los dragones!"

        mc "No empieces."

        ichika "El dragón ya tiene nombre." 

        ichika "Se llama Contrato."

        mc "Qué sutil."

        ichika "¡Es mi mejor material!"

        show ichika at pj_calla(0.5)
        with disolucion_lenta

    else:

        show ichika agotada at pj_habla(0.5)
        with dissolve

        ichika "Buenos días, [mc]." 

        mc "Buenos días Ichika."

        mc_pensamiento "Ichika... Lo que te dije ayer."

        mc_pensamiento "No sé que decirle."

        mc "¿Qué tienes planeado hacer hoy?"

        show ichika neutral at pj_habla(0.5)
        with disolucion_lenta

        ichika "Ya sé qué hacer con mi tiempo. Gracias por preguntar."

        show ichika sonriendo at pj_habla(0.5)
        with disolucion_lenta

        ichika "¡Y hoy me portaré muy bien! Que conste."

        show ichika at pj_calla(0.5)
        with disolucion_lenta

        narrador "La sonrisa llegó medio segundo tarde."

        narrador "Antes me recibía con una broma. Hoy, con mi nombre y nada más."

    hide ichika
    with moveoutleft

    return


# ------------------------------------------------------------
label reaccion_nino:

    play music nino fadein 1.5 fadeout 2.0

    if rama_hub1 == "calida":

        show nino neutral at pj_habla(0.5)
        with dissolve

        nino "Oye tu."

        nino "Ni una palabra a mis hermanas de lo que pasó."

        mc "Claro, no iba a decir nada."

        show nino molesta at pj_habla(0.5)
        with disolucion_lenta

        nino "Bien. …Y come algo antes de clases."

        nino "Tienes cara de no haber desayunado."

        mc "¿Eso es preocupación?"

        show nino nerviosa at pj_habla(0.5)
        with disolucion_lenta

        nino "¡No! Es que si te desmayas, nos echan la culpa."

        nino "…Anoche pensé en lo que dijiste." 

        nino "Que no ibas a prometer nada."

        nino "Nadie me había hablado así. Sin intentar caerme bien."

        show nino molesta at pj_habla(0.5)
        with disolucion_lenta

        nino "Eso no significa que confíe en ti." 

        nino "No te hagas ideas."

        show nino at pj_calla(0.28)
        with disolucion_lenta

        narrador "Se fue rápido. Pero esta vez se le olvidó cruzar los brazos."

    elif rama_hub1 == "tibia":

        show nino neutral at pj_habla(0.5)
        with dissolve

        nino "Lo que pasó sigue sin significar nada."

        mc "No dije que significara algo."

        nino "Y que quede así."

        show nino at pj_calla(0.5)
        with disolucion_lenta

        narrador "Pero se tomó la molestia de buscarme solo para decirlo."

    else:

        show nino molesta at pj_habla(0.5)
        with dissolve

        nino "Guárdate el «buenos días». No lo voy a necesitar."

        mc "Ni siquiera dije nada."

        nino "Ya, pero ibas a decirlo."

        nino "«Yo sí voy a durar.»" 

        nino "Qué gracioso."

        nino "Anota la fecha." 

        nino "Cuando te vayas, te la voy a recordar."

        show nino at pj_calla(0.5)
        with disolucion_lenta

        narrador "Pasó a mi lado sin rozarme. Ni siquiera con el hombro."

    hide nino
    with moveoutleft

    return


# ------------------------------------------------------------
label reaccion_miku:

    play music miku fadein 2.0

    show miku neutral at pj(0.5)
    with dissolve

    if rama_hub1 == "calida":

        show miku relajada at pj_habla(0.5)
        with disolucion_lenta

        miku "Ah... [mc]. Qué bueno que llegaste..." 
        
        miku "Estaba... esperándote."

        miku "…¿Ya llegaste a la página ciento veinte?"

        mc "Voy por la noventa y cinco."

        miku "La primera mitad es lenta. Aguanta."

        miku "Cuando llegues a la página de la sal, avísame." 

        miku "Quiero ver tu cara."

        mc "¿Mi cara?"

        show miku animada at pj_habla(0.5)
        with disolucion_lenta

        miku "Anoche me quedé pensando en que alguien se pasó la noche en mi tema."

        miku "Nadie lo había hecho. Nunca."

        miku "Siento como si alguien al fin comprendiera mis gustos."

        show miku encogida at pj_habla(0.5)
        with disolucion_lenta

        miku "…Digo. Para ver si te sorprendes."

        miku "…Gracias por leerlo."

        miku "...Significa mucho para mi [mc]."

        show miku at pj_calla(0.5)
        with disolucion_lenta

        narrador "Se fue con los audífonos al cuello. Sin tocarlos."

    elif rama_hub1 == "tibia":

        show miku neutral at pj_habla(0.5)
        with dissolve

        miku "…Buenos días."

        show miku at pj_calla(0.5)
        with disolucion_lenta

        narrador "Lo dijo con el libro a media cara."

        mc "Buenos días."

        narrador "Dos palabras. Era mejor que ninguna."

    else:

        show miku neutral at pj(0.5)
        with dissolve

        narrador "Entró con los audífonos puestos y sonando."

        mc "Buenos días Miku."

        show miku neutral at pj_habla(0.5)
        with disolucion_lenta

        miku "…Voy a estudiar solo lo que entra en el examen."

        miku "Como dijiste."

        show miku at pj_calla(0.5)  
        with disolucion_lenta

        narrador "No hubo reproche." 

        narrador "Eso fue lo peor: lo dijo como quien acepta un reglamento."

    hide miku
    with moveoutleft

    return


# ------------------------------------------------------------
label reaccion_yotsuba:

    play music yotsuba fadein 1.5 fadeout 2.0

    if rama_hub1 == "calida":

        show yotsuba sonriendo at pj_habla(0.5)
        with dissolve

        yotsuba "¡Buenos días, [mc]!" 

        yotsuba "¡Hoy correré menos de treinta vueltas!"

        mc "¿Cuántas?"

        yotsuba "¡Veinticinco! ¡Es un número perfecto!"

        mc "No lo es."

        yotsuba "¡Para mí sí!"

        show yotsuba neutral at pj_habla(0.5)
        with disolucion_lenta

        yotsuba "…Ayer dijiste que mi punto de partida no era cero."

        yotsuba "Anoche no pude dejar de pensarlo."

        yotsuba "Nadie me había dicho algo así sin pedirme que sonriera."

        yotsuba "Tu entendiste lo que en verdad siento por dentro."

        yotsuba "No solo lo que reflejo a los demas."

        show yotsuba sonriendo at pj_habla(0.5)
        with disolucion_lenta

        yotsuba "Bueno."

        yotsuba "¡Dame la mano!"

        narrador "Sacó el rotulador y escribió en mi muñeca antes de que pudiera decir que no."

        yotsuba "¡Listo! ¡Ahora tú también llevas la cuenta!"

        mc_pensamiento "Decía «1». Con un corazón torcido al lado."

        show yotsuba incomoda at pj_habla(0.5)
        with disolucion_lenta

        yotsuba "¡No es un corazón! ¡Es… una vuelta!"

        show yotsuba at pj_calla(0.5)
        with disolucion_lenta

    elif rama_hub1 == "tibia":

        show yotsuba sonriendo at pj_habla(0.5)
        with dissolve

        yotsuba "¡Mira! ¡Un minuto con catorce!"

        narrador "Levantó el brazo: lo había anotado en la muñeca con rotulador, otra vez."

        mc "Tienes que dejar de escribirte en el brazo."

        yotsuba "¡Es mi cuaderno oficial!"

        show yotsuba at pj_calla(0.5)
        with disolucion_lenta

    else:

        show yotsuba sonriendo at pj_habla(0.5)
        with dissolve

        yotsuba "¡Buenos días, tutor!" 

        yotsuba "¡Hoy voy a concentrarme en correr!"

        narrador "Me llamó «tutor» con el tono que se usa con un desconocido."

        mc "Yotsuba, ayer yo…"

        show yotsuba neutral at pj_habla(0.5)
        with disolucion_lenta

        yotsuba "¡Tenías razón! ¡Correr es lo mío!"

        yotsuba "…Hoy serán cuarenta vueltas. ¡Cuarenta!"

        show yotsuba at pj_calla(0.5)

        narrador "Lo anotó en la muñeca. No me miró mientras lo hacía."

    hide yotsuba
    with moveoutleft

    return


# ------------------------------------------------------------

label reaccion_itsuki:

    play music itsuki fadein 2.0

    if rama_hub1 == "calida":

        show itsuki neutral at pj_habla(0.5)
        with dissolve

        itsuki "…Buenos días."

        mc "Buenos días."

        itsuki "Hoy no me senté en tu sitio."

        itsuki "Aprendo rápido." 

        itsuki "Es lo único que se me da bien."

        mc "No es lo único."

        show itsuki timida at pj_habla(0.5)
        with disolucion_lenta

        itsuki "…No digas cosas así. Sin avisar."

        show itsuki at pj_calla(0.5)
        with disolucion_lenta

        narrador "No me miró." 

        narrador "Pero tampoco giró la silla hacia la ventana."

    elif rama_hub1 == "tibia":

        show itsuki molesta at pj_habla(0.5)
        with dissolve

        itsuki "Sigo sin necesitar tu ayuda."

        mc "No ofrecí ninguna."

        itsuki "Lo estabas pensando."

        show itsuki molesta at pj_calla(0.5)
        with disolucion_lenta

    else:

        show itsuki molesta at pj_habla(0.5)
        with dissolve

        narrador "Su mochila estaba sobre mi pupitre."

        mc "Itsuki, ese es mi…"

        itsuki "Lo sé."

        itsuki "Ya tengo lo que necesitaba de ti. Eso fue todo."

        show itsuki at pj_calla(0.5)
        with disolucion_lenta

        narrador "Tuve que sentarme en el último pupitre."


    return



################################################################################
##  INTERCONEXIÓN 1 · APERTURA -> HUB 1
##  Itsuki propone "el juego de busca y encuentra": mc tiene que adivinar
##  dónde pasa cada una las tardes. Es la excusa diegética del mapa y de las
##  tres tardes. Sin assets nuevos.
################################################################################

label cap1_interconexion_1:

    stop music fadeout 1.5

    scene bg_escuela
    with fade

    play sound sfx_timbre volume 2.5

    narrador "Llegué al instituto temprano, como siempre."

    play music cotidiano fadein 2.5

    mc_pensamiento "Pero esta vez llegaba con un plan."

    mc_pensamiento "Ir de una en una. Es la única forma de hacerlas estudiar."

    mc_pensamiento "No será fácil, pero puedo lograrlo."

    scene bg_aula
    with fade

    narrador "En la hora de descanso las encontré a las cinco juntas."

    mc_pensamiento "No venía a obligarlas a estudiar todas juntas. Eso ya sé que no funciona."

    mc_pensamiento "Venía a comprobar si los lugares que mencionó Raiha eran de verdad los suyos."

    mc_pensamiento "Así podría ir por ellas de una en una."

    mc_pensamiento "Cada una sola es apenas una quinta parte de lo que son juntas."

    show ichika neutral at pj(X_ICHIKA)
    show nino neutral at pj(X_NINO)
    show miku neutral at pj(X_MIKU)
    show yotsuba sonriendo at pj(X_YOTSUBA)
    show itsuki neutral at pj(X_ITSUKI)
    with dissolve

    play music incomodo fadeout 1.0 fadein 1.5

    mc "Buenas tardes."

    mc "Veo que siguen igual de desorganizadas que siempre."

    mc "Tenemos mucho que repasar hoy."

    mc_pensamiento "Las saludé de la mejor manera posible."

    mc_pensamiento "Eso creo..."

    show ichika neutral at pj_calla(X_ICHIKA)
    show nino neutral at pj_habla(X_NINO)
    show miku neutral at pj_calla(X_MIKU)
    show yotsuba sonriendo at pj_calla(X_YOTSUBA)
    show itsuki neutral at pj_calla(X_ITSUKI)
    with disolucion_lenta

    nino "¿Otra vez con tus tonterías de que vamos a estudiar?"

    nino "No creas que hoy será diferente."

    nino "Hoy será el tercer día y tu tercer fracaso."

    mc_pensamiento "Nino, la de siempre. Habla por todas."

    mc_pensamiento "Las otras cuatro solo la escuchaban."

    mc "No te voy a dar la razón."

    mc "Pero sí es difícil hacerlas estudiar a las cinco a la vez."

    nino "¿Y entonces?"

    mc "Tengo otro método. Uno más efectivo contra ustedes."

    show nino neutral at pj_calla(X_NINO)
    show yotsuba sonriendo at pj_habla(X_YOTSUBA)

    yotsuba "¿Un método efectivo? ¡Guau!"

    yotsuba "¿Y qué es? ¡Quiero saberlo! ¡Quiero saberlo!"

    show yotsuba sonriendo at pj_calla(X_YOTSUBA)
    show ichika sonriendo at pj_habla(X_ICHIKA)

    ichika "Vaya, resulta que además de cerebrito eres un estratega."

    show ichika at pj_calla(X_ICHIKA)
    show itsuki molesta at pj_habla(X_ITSUKI)

    itsuki "Seguro es explotarnos estudiando todos los días y todas las noches."

    show itsuki molesta at pj_calla(X_ITSUKI)
    show miku neutral at pj_habla(X_MIKU)

    miku "…"

    show miku neutral at pj_calla(X_MIKU)
    show nino neutral at pj_habla(X_NINO)

    nino "No se preocupen, chicas. Su gran método es renunciar y largarse de nuestras vidas."

    nino "Y aunque no lo creas… esta vez sí te apoyaré."

    show nino neutral at pj_calla(X_NINO)
    show yotsuba incomoda at pj_habla(X_YOTSUBA)

    yotsuba "¡Nino! Seguro no es eso. Él solo—"

    show nino neutral at pj_habla(X_NINO)
    show yotsuba incomoda at pj_calla(X_YOTSUBA)

    nino "Yotsuba."

    show nino neutral at pj_calla(X_NINO)
    show yotsuba sonriendo at pj_habla(X_YOTSUBA)

    yotsuba "…¡Digo! ¡Nada! ¡Era una broma!"

    show yotsuba sonriendo at pj_calla(X_YOTSUBA)

    mc "Para ponerlo en marcha solo necesito que me respondan una pregunta."

    mc_pensamiento "Se quedaron calladas. Eso casi nunca pasa."

    show ichika at pj_habla(X_ICHIKA)
    show nino at pj_habla(X_NINO)
    show miku at pj_habla(X_MIKU)
    show yotsuba at pj_habla(X_YOTSUBA)
    show itsuki at pj_habla(X_ITSUKI)
    with disolucion_lenta

    quintillizas "¿Qué?"

    mc "¿Dónde pasan las tardes después de clases?"

    mc "Sé que no siempre están juntas."

    mc "Aunque sean iguales, sus rutinas y pasatiempos no lo son."

    show ichika at pj_calla(X_ICHIKA)
    show nino at pj_calla(X_NINO)
    show miku at pj_habla(X_MIKU)
    show yotsuba at pj_calla(X_YOTSUBA)
    show itsuki at pj_calla(X_ITSUKI)
    with disolucion_lenta

    miku "…Quiere dividirnos."

    show miku neutral at pj_calla(X_MIKU)

    mc_pensamiento "Fue la única que lo entendió. Y fue la que menos habló."

    mc_pensamiento "Me miraron entre sorprendidas y divertidas."

    show ichika sonriendo at pj_habla(X_ICHIKA)

    ichika "Ay, [mc]. ¿Para qué quieres saberlo?"

    ichika "¿Acaso planeas una cita con cada una?"

    ichika "No sabía que tenías ese lado."

    mc "No es eso. Pero..."

    show ichika sonriendo at pj_calla(X_ICHIKA)
    show nino neutral at pj_habla(X_NINO)

    nino "¿Y a ti qué te importa dónde pasemos?"

    nino "Ninguna te lo va a decir."

    mc "Ya lo suponía."

    show nino neutral at pj_calla(X_NINO)
    show itsuki sonriendo at pj_habla(X_ITSUKI)

    itsuki "Esperen. Tengo una idea."

    mc "¿Eh?"

    itsuki "Hagamos un juego. Al estilo quintillizas."

    show itsuki sonriendo at pj_calla(X_ITSUKI)
    show yotsuba sonriendo at pj_habla(X_YOTSUBA)

    yotsuba "¿Estilo quintillizas? ¡Hurra! ¡Yo quiero jugar!"

    show yotsuba sonriendo at pj_calla(X_YOTSUBA)
    show miku neutral at pj_habla(X_MIKU)

    miku "…Itsuki. Eso es justo lo que él quería."

    show miku neutral at pj_calla(X_MIKU)
    show itsuki sonriendo at pj_habla(X_ITSUKI)

    itsuki "Si [mc] dice que se preocupa por nosotras…"

    itsuki "…y que nos conoce mejor que nadie…"

    itsuki "…que adivine dónde pasamos las tardes."

    itsuki "Un juego de busca y encuentra."

    mc "¿¡QUÉÉÉ!?"

    show itsuki at pj_calla(X_ITSUKI)

    mc_pensamiento "Esto debe ser una broma. Y de muy mal gusto."

    mc_pensamiento "Pero en parte es mi culpa: fui yo quien preguntó."

    mc_pensamiento "Pero la parte buena es que cada una sí tiene su sitio."

    mc_pensamiento "Además, ya tengo la lista de Raiha."

    mc "Me parece bien, Itsuki. Acepto tu juego."

    mc "Sin querer me acabas de ayudar con mi plan. Bien hecho."

    show itsuki molesta at pj_habla(X_ITSUKI)

    itsuki "No me felicites. Solo te estoy complicando las cosas."

    itsuki "No podrás pasar toda la tarde con cada una. El tiempo es corto."

    itsuki "Y lo sabes."

    mc_pensamiento "Tenía razón."

    mc_pensamiento "Entre el instituto y el trabajo, solo me quedarán tres tardes libres."

    mc_pensamiento "Tres tardes. Cinco hermanas."

    mc "Iré de una en una, ya lo dije."

    show itsuki molesta at pj_calla(X_ITSUKI)
    show ichika sonriendo at pj_habla(X_ICHIKA)

    ichika "¿Entonces pasarás la tarde con tu quintilliza favorita?"

    ichika "Seguro me eliges a mí. Soy la más bonita de todas."

    mc "Tienen la misma cara."

    ichika "Detalles."

    show ichika sonriendo at pj_calla(X_ICHIKA)
    show nino neutral at pj_habla(X_NINO)

    nino "Ichika, no te rebajes. ¿Quién querría estar con ese nerd?"

    show nino neutral at pj_calla(X_NINO)
    show yotsuba incomoda at pj_habla(X_YOTSUBA)

    yotsuba "¿Y elegirás a la que quieras conocer mejor? ¿O no?"

    show yotsuba at pj_calla(X_YOTSUBA)
    show miku neutral at pj_habla(X_MIKU)

    miku "…No te preocupes por mi."

    miku "…Yo estoy bien sola."

    narrador "Se subió los audífonos antes de que pudiera contestar."

    show miku neutral at pj_calla(X_MIKU)
    show itsuki molesta at pj_habla(X_ITSUKI)

    itsuki "Yo no pienso esconderme. Estaré donde siempre."

    show itsuki molesta at pj_calla(X_ITSUKI)
    show nino neutral at pj_habla(X_NINO)

    nino "Treinta días, tutor. A ver a cuántas logras encontrar."

    hide ichika
    hide nino
    hide miku
    hide yotsuba
    with moveoutleft

    stop music fadeout 2.0

    narrador "Se fueron sin esperar respuesta."

    narrador "Yotsuba fue la única que miró atrás antes de salir."

    narrador "Y solo Itsuki tardó un poco más en salir."

    hide itsuki
    with dissolve

    narrador "El aula quedó en silencio."

    mc "Bien." 
    
    mc "Pasaré la tarde con una de ellas."

    mc "Solo es para reforzar sus conocimientos y conocerlas mejor."

    mc "No es para otro tipo de intenciones."

    mc_pensamiento "Bien, empecemos."

    jump hub_1


################################################################################
##  INTERCONEXIÓN 2 · EVENTO DEL HUB 1 -> BEAT ITSUKI
##  Casa de Futaro -> día siguiente en el instituto. Reacciones condicionadas
##  por la hermana visitada (destino) y por su rama (cálida/tibia/fría).
################################################################################

label interconexion_2:

    $ rama_hub1 = rama_de(destino)
    $ nombre_h = destino.capitalize()

    ############################################################################
    ##  NOCHE DESPUES DEL HUB 1
    ############################################################################
    
    play music hogar fadein 3.0

    scene bg_cuarto_mc
    with fade

    narrador "Esa noche no abrí la libreta. Ya sabía lo que decía."

    if rama_hub1 == "calida":

        mc_pensamiento "Dormí mejor de lo que esperaba."

        mc_pensamiento "Logré mejorar mi relación con [nombre_h]."

        mc_pensamiento "Eso para mi es un gran avance."

    elif rama_hub1 == "tibia":

        mc_pensamiento "Dormí. No sé si eso es buena o mala señal."

        mc_pensamiento "Lo que le dije a [nombre_h] aún me sigue dando en que pensar"

        mc_pensamiento "Parece que no avanzamos nada, ni tampoco retorcedimos."

        mc_pensamiento "Es como si nada hubiera pasado."

    else:

        mc_pensamiento "Me costó dormir." 

        mc_pensamiento "Repasé lo que dije más veces de las que voy a admitir."

        mc_pensamiento "Se suponía que iba a ver a [nombre_h] para mejorar nuestra relación."

        mc_pensamiento "Pero parece que solo empeoré las cosas."

        mc_pensamiento "Más de lo que ya estaban."

    ############################################################################
    ##  Desayuno · menú de sabor (cosmético, reconverge)
    ############################################################################

    scene bg_comedor
    with fade

    play music cena fadeout 1.5 fadein 2.0

    narrador "A la mañana siguiente, Raiha ya se había despertado."

    narrador "Me llamó al comedor muy alegre."

    narrador "Esa energía me recuerda a alguien. No sé a quién."

    show raiha hablando at pj_habla(0.20)
    with dissolve

    raiha "¡Buenos días hermanito!"

    raiha "¿Qué quieres de desayuno? ¡Tienes que decidirlo ya!"

    menu:

        "¿Qué le contestas a Raiha?"

        "Lo que sea, menos curry.":

            mc "Lo que sea, menos curry."

            show raiha regano at pj_habla(0.20)
            with disolucion_lenta

            raiha "¡El curry es amor líquido, hermanito!"

            mc "A esta hora de la mañana, el amor líquido es una apuesta."

        "Café en un tupper. Y listo.":

            mc "Café en un tupper. Y listo."

            raiha "¡No! ¡Hay arroz, tortilla y un pulpito de salchicha!"

            mc "¿Los pulpitos no se negocian?"

            show raiha regano at pj_habla(0.20)
            with disolucion_lenta

            raiha "¡Nunca!"

        "Nada. Con estas ojeras ya voy servido.":

            mc "Nada. Con estas ojeras ya voy servido."

            show raiha preocupada at pj_habla(0.20)
            with disolucion_lenta

            raiha "…Voy a prepararte doble porción."

            raiha "Recuerda que cuidarte a ti mismo y alimentarte bien tambien es importante."

            narrador "Lo dijo con el tono de quien ya tomó una decisión por los dos."

            show raiha regano at pj_habla(0.20)
            with disolucion_lenta

    raiha "¡Y no lo dejes olvidado en la mochila como la última vez!"

    mc "Prometido."

    narrador "Me lo entregó envuelto en un pañuelo, con el nudo más apretado que he visto en mi vida."

    hide raiha
    with moveoutleft

    narrador "Salí de casa y fuí al instituto."

    ############################################################################
    ##  Instituto
    ############################################################################

    stop music fadeout 1.0

    scene bg_escuela
    with fade

    scene bg_aula
    with fade

    play sound sfx_timbre volume 1.5

    narrador "Llegué al instituto con el almuerzo de Raiha en la mochila y la cabeza todavía en lo de ayer."

    narrador "En el aula, algunas ya estaban en sus pupitres y otras entraban de a una."

    narrador "Itsuki ya estaba en su pupitre, con el cuaderno de ciencias abierto."

    ############################################################################
    ##  Aula · reacción de la hermana visitada
    ############################################################################

    call reaccion_hermana_visitada
    
    ############################################################################
    ##  Chisme de Nino (solo si la visitada no fue ella ni Itsuki)
    ############################################################################

    if destino != "nino" and destino != "itsuki":

        play music incomodo fadeout 1.0 fadein 1.5

        if rama_hub1 == "calida":

            show nino neutral at pj_habla(0.5)
            with dissolve

            nino "¿Qué le hiziste a [nombre_h]?"

            nino "No paró de decir tu nombre anoche."

            nino "Tu nombre, lo genial que la pasaron, como la hiciste sentir."

            nino "¿Qué es lo que pretendes con [nombre_h]?"

            mc "No es lo que piensas, Nino."

            mc "Solo cumplí lo que les dije de mi método."

            show nino molesta at pj_habla(0.5)
            with disolucion_lenta

            nino "¿Pasaste la tarde a solas con ella?"

            mc "Sí. Era parte del método."

            nino "Ya. El método."

            show nino pillada at pj_habla(0.5)
            with disolucion_lenta

            nino "…¿Y por qué no me buscaste a mí primero?"

            mc "…¿Qué?"

            nino "¡Nada! ¡Era una pregunta retórica!"

            mc "Nino. ¿Estás celosa?"

            nino "¡¿CELOSA?! ¡Ni en tus sueños, tonto!"

            show nino molesta at pj_habla(0.5)
            with disolucion_lenta

            nino "[nombre_h] es mi hermana." 
            
            nino "Si le haces daño, te las vas a ver conmigo."

            nino "No me importa con cuál pases las tardes." 
            
            nino "Me importa que no se ilusione."

            nino "Y que quede claro: sigo diciendo que no vas a durar."

            narrador "Se fue rápido, con la cara girada hacia el pasillo."

            hide nino
            with moveoutleft

            mc_pensamiento "No pude ver si estaba roja." 
            
            mc_pensamiento "Pero parece que esa pregunta sí la dijo desde sus sentimientos."

        elif rama_hub1 == "tibia":

            show nino neutral at pj_habla(0.5)
            with dissolve

            nino "Oye, tú."

            nino "Anoche [nombre_h] llegó igual que se fue."

            nino "Ni contenta ni dolida. Como si no hubiera pasado nada."

            mc "Es que no pasó nada."

            nino "Bien. Es lo único que te reconozco: no armas escándalo."

            show nino molesta at pj_habla(0.5)
            with disolucion_lenta

            nino "No te lo tomes como un halago."

            mc "No lo hice."

            show nino neutral at pj_habla(0.5)
            with disolucion_lenta

            nino "…Pero sí. Me tranquiliza."

            nino "Los que entran haciendo ruido son los que más rápido se van."

            show nino neutral at pj_calla(0.5)

            narrador "Se fue con la misma cara con la que llegó."

            mc_pensamiento "Tardé un segundo en entender que eso también era un cumplido."

            hide nino
            with moveoutleft

           
        else:

            show nino neutral at pj_habla(0.5)
            with dissolve

            nino "Oye tú."

            narrador "Nino no gritó. Eso fue lo primero que me asustó."

            nino "Anoche vi a [nombre_h] muy mal, como si alguien la hubiera humillado."

            nino "Se encerró en su cuarto con una mirada perdida."

            nino "Toqué su puerta para ver como estaba."

            nino "Dijo que estaba bien. Lo dijo tres veces."

            nino "Nadie dice «estoy bien» tres veces si lo está."

            mc "No fue mi intención…"

            nino "Nunca lo es."

            nino "Te dije que ibas a hacerles daño. No pensé que tardarías tan poco."

            mc_pensamiento "No estaba enojada. Estaba decepcionada."

            mc_pensamiento "Y eso dolía mucho más que un grito."

            nino "Hoy no la saludes." 
            
            nino "No le expliques nada. Déjala."

            show nino neutral at pj_calla(0.5)
            with disolucion_lenta

            narrador "Se fue sin mirarme. No hubo insultos, porque no hacía falta."

            mc_pensamiento "Quise decir que me arrepentía."

            mc_pensamiento "Pero no sabía si tenía derecho a decirlo en voz alta."

            hide nino
            with moveoutleft

    ############################################################################
    ##  Almuerzo -> enlace con el beat de Itsuki
    ############################################################################

    narrador "Las clases terminaron rápidamente."

    stop music fadeout 0.5

    play sound sfx_timbre volume 1.5

    narrador "El timbre del almuerzo sonó y el aula se vació en segundos."

    narrador "Itsuki fue la primera en levantarse."

    narrador "Tomó el cuaderno de ciencias. No tomó nada más."

    narrador "Ninguna bolsa de almuerzo. Ninguna caja."

    hide itsuki
    with dissolve

    mc_pensamiento "No hacía falta preguntar adónde iba."

    mc_pensamiento "Solo hay un sitio al que se sube por esas escaleras."

    call beat_Itsuki
    jump interconexion_3


################################################################################
##  INTERCONEXIÓN 3 · BEAT ITSUKI -> HUB 2
##  Cuarto de Futaro -> unos días después en el aula. Sin menú: chequeo corto
##  de "¿cómo estás?" y Itsuki recuerda el juego antes de abrir el hub 2.
################################################################################

label interconexion_3:

    ############################################################################
    ##  Noche · eco del beat de Itsuki
    ############################################################################

    play music hogar fadein 3.0

    scene bg_cuarto_mc
    with fade

    if not itsuki_visitada_cap1:

        narrador "Esa noche saqué mi copia de la hoja de diagnóstico del primer día."

        mc_pensamiento "Busqué el ejercicio que Itsuki tenía rodeado en el cuaderno."

        mc_pensamiento "No era difícil. Ella lo resolvería con los ojos cerrados."

        mc_pensamiento "Y llevaba días hundiendo el papel con el lápiz sin intentarlo de verdad."

        mc_pensamiento "Eso no es falta de talento."

        mc_pensamiento "Es miedo a equivocarse delante de alguien."

    else:

        narrador "Esa noche volví a pensar en la azotea."

        mc_pensamiento "En el aula se atascó y se encerró sobre el cuaderno."

        mc_pensamiento "En la azotea ni siquiera lo abrió."

        mc_pensamiento "No sé cuál de las dos cosas me preocupa más."

    mc_pensamiento "Quedan casi tres semanas."

    ############################################################################
    ##  Transición
    ############################################################################

    scene bg_negro
    with fade

    narrador "Los días siguientes se me fueron entre clases, las tutorías y sueño atrasado."

    narrador "Para cuando levanté la cabeza, ya habían pasadon 10 días."

    stop music fadeout 1.0

    ############################################################################
    ##  Aula · chequeo corto
    ############################################################################

    scene bg_aula
    with fade

    play music cotidiano fadein 2.0

    show ichika neutral at pj(X_ICHIKA)
    show nino neutral at pj(X_NINO)
    show miku neutral at pj(X_MIKU)
    show yotsuba sonriendo at pj(X_YOTSUBA)
    show itsuki neutral at pj(X_ITSUKI)
    with dissolve

    narrador "Las cinco ya estaban en el aula cuando entré."

    show yotsuba sonriendo at pj_habla(X_YOTSUBA)

    yotsuba "¡[mc]! ¿Cómo estás? ¡Tienes cara de haber peleado con un oso!"

    mc "Gracias, Yotsuba."

    yotsuba "¡Es un cumplido! ¡Los osos son fuertes!"

    show yotsuba sonriendo at pj_calla(X_YOTSUBA)
    show ichika sonriendo at pj_habla(X_ICHIKA)
    with disolucion_lenta

    ichika "Pregunta seria, [mc]: ¿cuántas horas llevas sin dormir bien?"

    mc "He dormido bien, Las suficientes horas."

    mc "Cuidar de cinco bebés no es nada fácil."

    ichika "Eso lo diría alguien que no duerme."

    show ichika sonriendo at pj_calla(X_ICHIKA)
    show miku neutral at pj_habla(X_MIKU)
    with disolucion_lenta

    miku "…Tienes ojeras."

    mc "Ya me lo dijeron."

    miku "…Es verdad igual."

    show miku neutral at pj_calla(X_MIKU)
    show nino neutral at pj_habla(X_NINO)
    with disolucion_lenta

    nino "Van casi diez días. Y seguimos igual."

    mc "No seguimos igual."

    nino "Cuéntamelo cuando haya algo que contar."

    show nino neutral at pj_calla(X_NINO)
    with disolucion_lenta

    ## La hermana del hub 1 deja una huella corta según la rama.
    ## Itsuki queda fuera: su reacción va en su propio cierre.

    if destino != "itsuki":

        if rama_hub1 == "calida":

            if destino == "nino":

                narrador "Nino me buscó con la mirada. La apartó antes de que la pillara."

            else:

                narrador "[nombre_h] me buscó con la mirada desde su sitio y sonrió, apenas."

        elif rama_hub1 == "tibia":

            narrador "[nombre_h] me saludó con un gesto corto. Nada más, nada menos."

        else:

            narrador "[nombre_h] se puso a ordenar su mochila cuando pasé por su lado."

    ############################################################################
    ##  Itsuki cierra y empuja al hub 2
    ############################################################################

    if not itsuki_visitada_cap1:

        narrador "Itsuki seguía en su pupitre, con el cuaderno abierto en la misma página."

    else:

        narrador "Itsuki seguía en su pupitre, con el cuaderno de ciencias cerrado."

    show itsuki molesta at pj_habla(X_ITSUKI)
    with disolucion_lenta

    itsuki "El juego sigue."

    mc "Lo sé."

    itsuki "No me importa a quién elijas."

    itsuki "Solo digo que el reloj no espera."

    show itsuki molesta at pj_calla(X_ITSUKI)
    with disolucion_lenta

    mc_pensamiento "Tenía razón. Siempre la tiene cuando habla así."

    mc_pensamiento "Dos tardes libres. Cuatro hermanas por alcanzar."

    mc "Bien. A ver a quién busco hoy."

    stop music fadeout 1.5

    scene bg_negro
    with fade

    jump hub_2


################################################################################
##  INTERCONEXIÓN 4 · EVENTO DEL HUB 2 -> BEAT NINO
##  Casa de Futaro -> instituto. Reacción de la hermana visitada (labels),
##  Yotsuba (o Miku) cuenta lo que notó, y Nino desaparece antes de la última
##  clase: pista del beat.
################################################################################

label interconexion_4:

    $ rama_hub = rama_de(destino)
    $ nombre_h = destino.capitalize()

    ############################################################################
    ##  Noche
    ############################################################################

    play music hogar fadein 3.0

    scene bg_cuarto_mc
    with fade

    narrador "Esa noche me quedé un rato con la luz apagada."

    if rama_hub1 == "calida":

        mc_pensamiento "Dormí mejor de lo que esperaba."

        mc_pensamiento "Logré mejorar mi relación con [nombre_h]."

        mc_pensamiento "Eso para mi es un gran avance."

    elif rama_hub1 == "tibia":

        mc_pensamiento "Dormí. No sé si eso es buena o mala señal."

        mc_pensamiento "Lo que le dije a [nombre_h] aún me sigue dando en que pensar"

        mc_pensamiento "Parece que no avanzamos nada, ni tampoco retorcedimos."

        mc_pensamiento "Es como si nada hubiera pasado."

    else:

        mc_pensamiento "Me costó dormir." 

        mc_pensamiento "Repasé lo que dije más veces de las que voy a admitir."

        mc_pensamiento "Se suponía que iba a ver a [nombre_h] para mejorar nuestra relación."

        mc_pensamiento "Pero parece que solo empeoré las cosas."

        mc_pensamiento "Más de lo que ya estaban."


    mc_pensamiento "Dos de cinco. Y el calendario seguía corriendo."

    ############################################################################
    ##  Camino al instituto · menú de sabor (cosmético, reconverge)
    ############################################################################

    scene bg_escuela
    with fade

    play music cotidiano fadein 2.0

    narrador "De camino al instituto, la cabeza no me dejaba en paz."

    mc_pensamiento "No sé si es por mi falta de sueño."

    mc_pensamiento "O por todos los días que llevo aguantando a esas cinco."

    menu:

        "¿En qué piensas mientras caminas?"

        "En que ya me acostumbré a dormir cuatro horas.":

            mc_pensamiento "Eso es peligroso."

            mc_pensamiento "Raiha ya me lo dijo. Debo cuidar mi salud."

            mc_pensamiento "Pero con este cronograma, es imposible."

            mc_pensamiento "Lo peor es que ya no se siente raro."

        "En si las cinco tienen un grupo de chat sobre mí.":

            mc_pensamiento "Seguro lo tienen. Seguro tiene un nombre ridículo."

            mc_pensamiento "Seguro me andan humillando de la peor manera posible."

            mc_pensaiento "O inventandome apodos tontos."

            mc_pensamiento "Solo espero no lo publiquen en algún lado."

        "En nada. Solo camino.":

            mc_pensamiento "Me concedí cuatro cuadras de silencio."

            mc_pensamiento "Con mi agenda, es casi un lujo."

    ############################################################################
    ##  Aula · reacción de la hermana visitada
    ############################################################################

    stop music fadeout 1.5

    scene bg_aula
    with fade

    narrador "En el aula, algunas ya estaban en sus pupitres y otras entraban de a una."

    call reaccion_hermana_visitada

    ############################################################################
    ##  Quien lee a las demás cuenta lo que notó
    ##  Yotsuba, salvo que la visitada haya sido ella: entonces, Miku.
    ############################################################################

    play music derrota fadein 2.5

    if destino != "yotsuba":

        show yotsuba sonriendo at pj(0.5)
        with dissolve

        if rama_hub == "calida":

            show yotsuba sonriendo at pj_habla(0.5)
            with disolucion_lenta

            yotsuba "¡[mc]! ¡Ven un momento!" 
            
            yotsuba "¡Es un secreto! ¡Rápido!"

            yotsuba "[nombre_h] se quedó despierta hasta tarde."

            yotsuba "No estaba estudiando. Estaba como… pensando con una sonrisa."

            yotsuba "¡Yo sé distinguir! ¡Es lo que mejor se me da!"

            mc "¿Qué quieres decir?"

            yotsuba "Que lo que le dijiste, o lo que hiciste, le dejó algo bueno por dentro."

            show yotsuba sonriendo at pj_calla(0.5)
            with disolucion_lenta

            yotsuba "Gracias por no rendirte con ella. ¡Es todo!"

        elif rama_hub == "tibia":

            show yotsuba sonriendo at pj_habla(0.5)
            with disolucion_lenta

            yotsuba "¡[mc]! [nombre_h] está igual que siempre."

            yotsuba "¡Y eso está bien! ¡A veces igual es lo mejor que se puede pedir!"

            narrador "Lo dijo sonriendo. Pero la sonrisa tardó en llegar a sus ojos."

            show yotsuba incomoda at pj_habla(0.5)
            with disolucion_lenta

            yotsuba "…Es que no sé si le sirvió o no. Y eso me da un poco de cosa."

            mc "¿Por qué?"

            yotsuba "Porque yo siempre sé. Y esta vez, no."

            show yotsuba incomoda at pj_calla(0.5)
            with disolucion_lenta

        else:

            show yotsuba incomoda at pj_habla(0.5)
            with disolucion_lenta

            yotsuba "[mc]. ¿Tienes un minuto?"

            narrador "Lo dijo sin exclamación. Sin sonrisa." 
            
            narrador "Era la primera vez que la veía así."

            yotsuba "[nombre_h] no durmió bien. Se le nota en cómo sostiene el lápiz."

            yotsuba "Yo la conozco, y tal vez lo que le dijiste… le dolió."

            yotsuba "No te lo digo para que te sientas mal."

            yotsuba "Te lo digo porque ella nunca lo va a decir."

            mc_pensamiento "Me dolió más que un reproche." 
            
            mc_pensamiento "Yotsuba nunca reprocha: solo informa."

            yotsuba "Arréglalo. Por favor."

            show yotsuba incomoda at pj_calla(0.5)
            with disolucion_lenta

        hide yotsuba
        with moveoutleft

    else:

        show miku neutral at pj(0.5)
        with dissolve

        if rama_hub == "calida":

            show miku neutral at pj_habla(0.5)
            with disolucion_lenta

            miku "Hola, [mc]."

            narrador "Me saludó sin pausa antes de la primera palabra. Eso ya era un cambio."

            miku "Tienes un número escrito en la muñeca."

            miku "Un uno. Con algo al lado. Torcido."

            mc "Es largo de explicar."

            miku "Yotsuba habló dormida anoche. Decía números."

            miku "Y sonreía."

            show miku relajada at pj_habla(0.5)
            with disolucion_lenta

            miku "Hoy tú tienes uno en el brazo. No creo que sea casualidad."

            miku "Está más rara de lo normal. Pero contenta."

            miku "Eso casi no pasa."

            mc "Me alegra."

            show miku encogida at pj_habla(0.5)
            with disolucion_lenta

            miku "…No es por ti."

            miku "…Bueno. Un poco."

            show miku neutral at pj_calla(0.5)
            with disolucion_lenta

        elif rama_hub == "tibia":

            show miku neutral at pj_habla(0.5)
            with disolucion_lenta

            miku "…Buenos días, [mc]."

            narrador "Lo dijo mirándome una vez. Después volvió al libro."

            miku "…Yotsuba llegó anoche a la hora de siempre."

            miku "…Cenó dos platos. Hizo ruido. Normal."

            miku "…Tenía números escritos en el brazo. Como siempre."

            miku "…Pero esta vez se los quedó mirando un buen rato antes de lavárselos."

            mc "¿Y qué significa eso?"

            miku "…No sé. No es mi sección."

            miku "…Ayer te tocaba tu juego, ¿no? …Solo pregunto."

            show miku neutral at pj_calla(0.5)
            with disolucion_lenta

        else:

            narrador "Tenía los audífonos a medias: una oreja libre y la otra no."

            show miku neutral at pj_habla(0.5)
            with disolucion_lenta

            miku "…Hola."

            mc "Hola, Miku."

            miku "…Yotsuba llegó tarde anoche. Con el brazo lleno de rotulador."

            miku "…No se lo lavó. Se acostó con él."

            miku "…No hizo ruido en toda la cena."

            miku "…Yotsuba siempre hace ruido. Aunque nadie se lo pida."

            narrador "Lo dijo mirando el libro. Pero las páginas no se movían."

            miku "…No sé si fuiste tú. Ayer te tocaba tu juego."

            miku "…Pero si fuiste tú, no lo dejes así."

            show miku neutral at pj_calla(0.5)
            with disolucion_lenta

        hide miku
        with moveoutleft

    ############################################################################
    ##  Pista del beat · Nino se va antes de la última clase
    ############################################################################

    stop music fadeout 1.5

    narrador "El resto de la mañana pasó entre apuntes y miradas de reojo."

    narrador "Terminadas las clases, noté que el pupitre de Nino estaba vacío."

    play music extraneza fadein 2.0

    narrador "Su mochila ya no estaba."

    show ichika neutral at pj(X_ICHIKA)
    show miku neutral at pj(X_MIKU)
    show yotsuba sonriendo at pj(X_YOTSUBA)
    show itsuki neutral at pj(X_ITSUKI)
    with dissolve

    narrador "Las otras cuatro seguían ahí." 
    
    narrador "El hueco entre Ichika y Miku se notaba más que cualquier cosa que dijeran."

    mc "Disculpen chicas."

    mc "¿Alguien sabe dónde está Nino?"

    show ichika sonriendo at pj_habla(X_ICHIKA)
    with disolucion_lenta

    ichika "Te ves muy preocupado por Nino, ¿no [mc]?"

    ichika "¿Acaso hay algo entre ustedes dos?"

    mc "Ve al grano Ichika."

    show ichika neutral at pj_habla(X_ICHIKA)
    with disolucion_lenta

    ichika "Pues salió de manera apresurada."

    ichika "Con el celular en la mano y esa cara que ya conoces."

    ichika "Dijo que iba a hablar algo urgente con nuestro papá"

    show ichika neutral at pj_calla(X_ICHIKA)
    show yotsuba sonriendo at pj_habla(X_YOTSUBA)
    with disolucion_lenta

    yotsuba "¡Seguro se reunirán en nuestra casa!"

    yotsuba "Ya sé. ¡Nos planean hacer una cena sorpresa!"

    show yotsuba incomoda at pj_habla(X_YOTSUBA)
    with disolucion_lenta

    yotsuba "…Aunque cuando sale así, es porque es un asunto serio."

    show yotsuba incomoda at pj_calla(X_YOTSUBA)
    show miku neutral at pj_habla(X_MIKU)
    with disolucion_lenta

    miku "…Miró el celular y se quedó quieta."

    miku "…Nino nunca se queda quieta."

    show miku neutral at pj_calla(X_MIKU)
    show itsuki molesta at pj_habla(X_ITSUKI)
    with disolucion_lenta

    itsuki "Nino no se va sin avisar. Es un hecho."

    itsuki "Si se fue, tiene un motivo."

    itsuki "No es asunto tuyo. Pero tampoco es casualidad."

    itsuki "Tú tienes algo que ver con esto, estoy segura."

    show itsuki molesta at pj_calla(X_ITSUKI)
    with disolucion_lenta

    narrador "Nadie dijo nada más." 
    
    narrador "Las cuatro me miraron, y las cuatro apartaron la vista casi al mismo tiempo."

    hide ichika
    hide miku
    hide yotsuba
    hide itsuki
    with dissolve

    mc_pensamiento "Nino no era de las que se iban sin avisar."

    mc_pensamiento "Y menos sin dejarme una frase hiriente de despedida."

    mc_pensamiento "Las cuatro lo habían notado. Cada una a su manera."

    mc_pensamiento "Como dijo Yotsuba, debe estar en su casa con Maruo."

    mc_pensamiento "Tengo el presentimiento de que esta tarde va a ser más larga de lo normal."

    scene bg_negro
    with fade

    call beat_Nino
    jump interconexion_5