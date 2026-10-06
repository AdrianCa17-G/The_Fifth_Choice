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

    call beat_Itsuki
    jump interconexion_2


################################################################################
##  INTERCONEXIÓN 2 · BEAT ITSUKI -> HUB 2
################################################################################

label interconexion_2:

    scene bg_negro
    with fade

    narrador "Pasaron unos días."

    narrador "Una de las cinco ya no era una desconocida. Las otras cuatro seguían igual de lejos."

    jump hub_2


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