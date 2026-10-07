# ============================================================
# 02_capitulo1_conexiones.rpy
# ============================================================
# Encadena el Capítulo 1 tal como está en docs/CAP1.md §2 y hace
# las transiciones cortas entre los main events.
#
# Esqueleto:
# APERTURA → INTERCONEXIÓN 1 → HUB 1 → INTERCONEXIÓN 2 → BEAT Itsuki
# → INTERCONEXIÓN 3 → HUB 2 → INTERCONEXIÓN 4 → BEAT crisis de Nino  
# → INTERCONEXIÓN 4 → HUB 3 → INTERCONEXIÓN 5 → BEAT casa → EVENTO 6
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

    quintillizas "¿Qué?"

    mc "¿Dónde pasan las tardes después de clases?"

    mc "Sé que no siempre están juntas."

    mc "Aunque sean iguales, sus rutinas y pasatiempos no lo son."

    show miku neutral at pj_habla(X_MIKU)

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

    stop music fadeout 1.5

    nino "Treinta días, tutor. A ver a cuántas logras encontrar."

    hide ichika
    hide nino
    hide miku
    hide yotsuba
    with moveoutleft

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

    stop music fadeout 2.0

    jump hub_1


# ------------------------------------------------------------
label hub_1:

    $ tiempo_restante = "casi cuatro semanas"

    call screen mapa_hub(1)
    $ destino = _return
    call expression (LABEL_EVENTO.get(destino, "evento_" + destino))
    $ hub_visitadas.append(destino)

    jump interconexion_2


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

    stop music fadeout 1.5

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

    play music cotidiano fadein 2.0

    narrador "A la mañana siguiente, Raiha ya se había despertado."

    narrador "Me llamó al comedor muy alegre."

    narrador "Esa energía me recuerda a alguien. No sé a quién."

    show raiha hablando at pj(0.20)
    with dissolve

    raiha "¡Buenos días hermanito!"

    raiha "¿Qué quieres de desayuno? ¡Tienes que decidirlo ya!"

    menu:

        "¿Qué le contestas a Raiha?"

        "Lo que sea, menos curry.":

            mc "Lo que sea, menos curry."

            show raiha regano at pj(0.20)
            with dissolve

            raiha "¡El curry es amor líquido, hermanito!"

            mc "A esta hora de la mañana, el amor líquido es una apuesta."

        "Café en un tupper. Y listo.":

            mc "Café en un tupper. Y listo."

            raiha "¡No! ¡Hay arroz, tortilla y un pulpito de salchicha!"

            mc "¿Los pulpitos no se negocian?"

            show raiha regano at pj(0.20)
            with dissolve

            raiha "¡Nunca!"

        "Nada. Con estas ojeras ya voy servido.":

            mc "Nada. Con estas ojeras ya voy servido."

            show raiha preocupad at pj(0.20)
            with dissolve

            raiha "…Voy a prepararte doble porción."

            raiha "Recuerda que cuidarte a ti mismo y alimentarte bien tambien es importante."

            narrador "Lo dijo con el tono de quien ya tomó una decisión por los dos."

            show raiha regano at pj(0.20)
            with disolucion_lenta

    show raiha at pj(0.20)
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

    scene bg_escuela
    with fade

    narrador "Llegué al instituto con el almuerzo de Raiha en la mochila y la cabeza todavía en lo de ayer."

    scene bg_aula
    with fade

    narrador "Itsuki ya estaba en su pupitre, con el cuaderno de ciencias abierto."

    if destino == "itsuki":

        show itsuki neutral at pj(0.5)
        with dissolve

    else:

        show itsuki neutral at pj(0.78)
        with dissolve

    ############################################################################
    ##  Reacción de la hermana visitada
    ############################################################################

    if destino == "ichika":

        if rama_hub1 == "calida":

            show ichika sonriendo at pj_habla(0.28)
            with dissolve

            ichika "¡Buenos días, [mc]!"

            ichika "Logré dormir siete horas y media."

            ichika "¡He conseguido un récord personal!"

            mc "¿De verdad?"

            ichika "Siete y cuarto. Pero redondeo hacia arriba."

            show ichika neutral at pj_habla(0.28)
            with disolucion_lenta

            ichika "…Tú deberías hacer lo mismo. Dormir, digo."

            ichika "Siempre estás cuidando de las demás."

            show ichika determinada at pj_habla(0.28)
            with disolucion_lenta

            ichika "¿Y quién cuida de ti?"  

            ichika "Yo puedo hacerlo. Si me dejas."

            show ichika sonriendo at pj_habla(0.28)
            with disolucion_lenta

            ichika "Con mucho gusto. Jeje…"

            ichika "¡Consejo gratis! Exclusivo para ti [mc]"

            ichiika "¡No se lo cuentes a nadie!"

            show ichika at pj_calla(0.28)
            with disolucion_lenta

            mc_pensamiento "No supe qué contestar. Nadie me lo había preguntado en años."

      

        elif rama_hub1 == "tibia":

            show ichika sonriendo at pj_habla(0.28)
            with dissolve

            ichika "¡Buenos días, señor de los dragones!"

            mc "No empieces."

            ichika "El dragón ya tiene nombre." 

            ichika "Se llama Contrato."

            mc "Qué sutil."

            ichika "¡Es mi mejor material!"

            show ichika at pj_calla(0.28)
            with disolucion_lenta

        else:

            show ichika agotada at pj_habla(0.28)
            with dissolve

            ichika "Buenos días, [mc]." 

            mc "Buenos días Ichika."

            mc_pensamiento "Ichika... Lo que te dije ayer."

            mc_pensamiento "No sé que decirle."

            mc "¿Qué tienes planeado hacer hoy?"

            show ichika neutral at pj_habla(0.28)
            with disolucion_lenta

            ichika "Ya sé qué hacer con mi tiempo. Gracias por preguntar."

            show ichika sonriendo at pj_habla(0.28)
            with disolucion_lenta

            ichika "¡Y hoy me portaré muy bien! Que conste."

            show ichika at pj_calla(0.28)
            with disolucion_lenta

            narrador "La sonrisa llegó medio segundo tarde."

            narrador "Antes me recibía con una broma. Hoy, con mi nombre y nada más."

        hide ichika
        with moveoutleft

    elif destino == "nino":

        if rama_hub1 == "calida":

            show nino neutral at pj_habla(0.28)
            with dissolve

            nino "Oye tu."

            nino "Ni una palabra a mis hermanas de lo que pasó."

            mc "Claro, no iba a decir nada."

            show nino molesta at pj_habla(0.28)
            with disolucion_lenta

            nino "Bien. …Y come algo antes de clases."

            nino "Tienes cara de no haber desayunado."

            mc "¿Eso es preocupación?"

            show nino pillada at pj_habla(0.28)
            with disolucion_lenta

            nino "¡No! Es que si te desmayas, nos echan la culpa."

            nino "…Anoche pensé en lo que dijiste." 

            nino "Que no ibas a prometer nada."

            nino "Nadie me había hablado así. Sin intentar caerme bien."

            show nino molesta at pj_habla(0.28)
            with disolucion_lenta

            nino "Eso no significa que confíe en ti." 

            nino "No te hagas ideas."

            show nino at pj_calla(0.28)
            with disolucion_lenta

            narrador "Se fue rápido. Pero esta vez se le olvidó cruzar los brazos."

        elif rama_hub1 == "tibia":

            show nino neutral at pj_habla(0.28)
            with dissolve

            nino "Lo que pasó sigue sin significar nada."

            mc "No dije que significara algo."

            nino "Y que quede así."

            show nino at pj_calla(0.28)
            with disolucion_lenta

            narrador "Pero se tomó la molestia de buscarme solo para decirlo."

        else:

            show nino molesta at pj_habla(0.28)
            with dissolve

            nino "Guárdate el «buenos días». No lo voy a necesitar."

            mc "Ni siquiera dije nada."

            nino "Ya, pero ibas a decirlo."

            nino "«Yo sí voy a durar.»" 

            nino "Qué gracioso."

            nino "Anota la fecha." 

            nino "Cuando te vayas, te la voy a recordar."

            show nino at pj_calla(0.28)
            with disolucion_lenta

            narrador "Pasó a mi lado sin rozarme. Ni siquiera con el hombro."

        hide nino
        with moveoutleft

    elif destino == "miku":

        if rama_hub1 == "calida":

            show miku neutral at pj_habla(0.28)
            with dissolve

            miku "…¿Ya llegaste a la página ciento veinte?"

            mc "Voy por la noventa y cinco."

            show miku relajada at pj_habla(0.28)
            with disolucion_lenta

            miku "La primera mitad es lenta. Aguanta."

            miku "Cuando llegues a la página de la sal, avísame." 

            miku "Quiero ver tu cara."

            mc "¿Mi cara?"

            show miku animada at pj_habla(0.28)
            with disolucion_lenta

            miku "Anoche me quedé pensando en que alguien se pasó la noche en mi tema."

            miku "Nadie lo había hecho. Nunca."

            miku "Siento como si alguien al fin comprendiera mis gustos."

            show miku encogida at pj_habla(0.28)
            with disolucion_lenta

            miku "…Digo. Para ver si te sorprendes."

            miku "…Gracias por leerlo."

            miku "...Significa mucho para mi [mc]."

            show miku at pj_calla(0.28)
            with disolucion_lenta

            narrador "Se fue con los audífonos al cuello. Sin tocarlos."

        elif rama_hub1 == "tibia":

            show miku neutral at pj_habla(0.28)
            with dissolve

            miku "…Buenos días."

            show miku at pj_calla(0.28)
            with disolucion_lenta

            narrador "Lo dijo con el libro a media cara."

            mc "Buenos días."

            narrador "Dos palabras. Era mejor que ninguna."

        else:

            show miku neutral at pj(0.28)
            with dissolve

            narrador "Entró con los audífonos puestos y sonando."

            mc "Buenos días Miku."

            show miku neutral at pj_habla(0.28)
            with disolucion_lenta

            miku "…Voy a estudiar solo lo que entra en el examen."

            miku "Como dijiste."

            show miku at pj_calla(0.28)    
            with disolucion_lenta

            narrador "No hubo reproche." 

            narrador "Eso fue lo peor: lo dijo como quien acepta un reglamento."

        hide miku
        with moveoutleft

    elif destino == "yotsuba":

        if rama_hub1 == "calida":

            show yotsuba sonriendo at pj_habla(0.28)
            with dissolve

            yotsuba "¡Buenos días, [mc]!" 

            yotsuba "¡Hoy correré menos de treinta vueltas!"

            mc "¿Cuántas?"

            yotsuba "¡Veinticinco! ¡Es un número perfecto!"

            mc "No lo es."

            yotsuba "¡Para mí sí!"

            show yotsuba neutral at pj_habla(0.28)
            with disolucion_lenta

            yotsuba "…Ayer dijiste que mi punto de partida no era cero."

            yotsuba "Anoche no pude dejar de pensarlo."

            yotsuba "Nadie me había dicho algo así sin pedirme que sonriera."

            yotsuba "Tu entendiste lo que en verdad siento por dentro."

            yotsuba "No solo lo que reflejo a los demas."

            show yotsuba sonriendo at pj_habla(0.28)
            with disolucion_lenta

            yotsuba "Bueno."

            yotsuba "¡Dame la mano!"

            narrador "Sacó el rotulador y escribió en mi muñeca antes de que pudiera decir que no."

            yotsuba "¡Listo! ¡Ahora tú también llevas la cuenta!"

            mc_pensamiento "Decía «1». Con un corazón torcido al lado."

            show yotsuba incomoda at pj_habla(0.28)
            with disolucion_lenta

            yotsuba "¡No es un corazón! ¡Es… una vuelta!"

            show yotsuba at pj_calla(0.28)
            with disolucion_lenta

        elif rama_hub1 == "tibia":

            show yotsuba sonriendo at pj_habla(0.28)
            with dissolve

            yotsuba "¡Mira! ¡Un minuto con catorce!"

            narrador "Levantó el brazo: lo había anotado en la muñeca con rotulador, otra vez."

            mc "Tienes que dejar de escribirte en el brazo."

            yotsuba "¡Es mi cuaderno oficial!"

            show yotsuba at pj_calla(0.28)
            with disolucion_lenta

        else:

            show yotsuba sonriendo at pj_habla(0.28)
            with dissolve

            yotsuba "¡Buenos días, tutor!" 

            yotsuba "¡Hoy voy a concentrarme en correr!"

            narrador "Me llamó «tutor» con el tono que se usa con un desconocido."

            mc "Yotsuba, ayer yo…"

            show yotsuba neutral at pj_habla(0.28)
            with disolucion_lenta

            yotsuba "¡Tenías razón! ¡Correr es lo mío!"

            yotsuba "…Hoy serán cuarenta vueltas. ¡Cuarenta!"

            show yotsuba at pj_calla(0.28)

            narrador "Lo anotó en la muñeca. No me miró mientras lo hacía."

        hide yotsuba
        with moveoutleft

    else:

        ## destino == "itsuki": ya está en pantalla, centrada.

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

    ############################################################################
    ##  Chisme de Nino (solo si la visitada no fue ella ni Itsuki)
    ############################################################################

    if destino != "nino" and destino != "itsuki":

        if rama_hub1 == "calida":

            show nino neutral at pj_habla(0.28)
            with dissolve

            nino "¿Qué le hiciste a [nombre_h]? Anoche no paró de tararear."

            mc "Nada. Hablamos."

            nino "Qué molesto."

            hide nino
            with moveoutleft

        elif rama_hub1 == "fria":

            show nino molesta at pj_habla(0.28)
            with dissolve

            nino "Ya me enteré de lo que le dijiste a [nombre_h]."

            nino "Primero entras sonriendo. Después, esto."

            mc "No fue para tanto."

            nino "Eso dicen todos."

            hide nino
            with moveoutleft

    ############################################################################
    ##  Almuerzo -> enlace con el beat de Itsuki
    ############################################################################

    narrador "Las clases pasaron como pasan las que no escuchas."

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


################################################################################
##  INTERCONEXIÓN 3 · BEAT CRISIS DE NINO -> HUB 3
################################################################################

label interconexion_3:

    scene bg_negro
    with fade

    narrador "El calendario no esperó a que terminara de pensar en lo de la cocina."

    narrador "Quedaba una última tarde libre."

    jump hub_3


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
