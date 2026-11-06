################################################################################
##  02_cap1_evento6.rpy — EVENTO 6 · PARTE A (Chat 8)
##  Núcleo (Mov. 1, 7, 8, 9, 10) + bloques de Yotsuba (Mov. 2) e Ichika (Mov. 3).
##  Nino, Itsuki y Miku siguen como stubs (Chat 9). Pantallas: 12_e6_pantallas.rpy
################################################################################

default e6_i = 0
default e6_h = ""
default e6_cola = []
default e6_res = ""
default e6_presentes = []
default e6_expr = {}
default e6_p1 = ""
default e6_p2 = ""
default e6_boletin_fase = 1
default e6_chat_activo = False
default e6_disculpa_pendiente = False


################################################################################
##  AYUDAS DE SPRITES
##  Las formaciones usan renpy.show con at_list (pj / pj_habla / pj_calla): cada
##  sprite lleva SIEMPRE su posición absoluta. Así se evitan ~60 bloques de show.
################################################################################

init python:

    def e6_x(h):
        if h == "ichika":
            return X_ICHIKA
        if h == "nino":
            return X_NINO
        if h == "miku":
            return X_MIKU
        if h == "yotsuba":
            return X_YOTSUBA
        return X_ITSUKI

    def e6_limpiar():
        store.e6_presentes = []
        store.e6_expr = {}

    def e6_formacion(exprs):
        """Las cinco en su sitio, en pj (sin foco)."""
        store.e6_presentes = list(E6_ORDEN_CANON)
        store.e6_expr = dict(exprs)
        for h in store.e6_presentes:
            renpy.show(h + " " + store.e6_expr[h], at_list=[pj(e6_x(h))], tag=h)

    def e6_entrar(h):
        """Entra una hermana en pj, neutral. Las ya presentes no se tocan."""
        if h not in store.e6_presentes:
            store.e6_presentes.append(h)
        store.e6_expr[h] = "neutral"
        renpy.show(h + " neutral", at_list=[pj(e6_x(h))], tag=h)

    def e6_mostrar_foco(quien, expr):
        """quien habla (pj_habla); las demás presentes, pj_calla. quien="" = todas calla."""
        if quien != "":
            if quien not in store.e6_presentes:
                store.e6_presentes.append(quien)
            if expr != "":
                store.e6_expr[quien] = expr
        for h in store.e6_presentes:
            actual = store.e6_expr.get(h, "neutral")
            store.e6_expr[h] = actual
            if h == quien:
                tr = pj_habla(e6_x(h))
            else:
                tr = pj_calla(e6_x(h))
            renpy.show(h + " " + actual, at_list=[tr], tag=h)

    def e6_sexto_valor():
        """Normaliza el 6.º hueco de N1′ al vocabulario del guion.
        El guion usa taza / blanco / cuando; el minijuego implementado
        (10_mj_nino.rpy) devuelve celebrar / consolar / vacio.
        celebrar -> taza · consolar -> cuando · vacio -> blanco.
        Si no hay dato (minijuego saltado), vale «blanco»."""
        r = store.e6_mj.get("nino")
        if r is None:
            return "blanco"
        v = r["datos"].get("sexto", "blanco")
        if v == "taza" or v == "celebrar":
            return "taza"
        if v == "cuando" or v == "consolar":
            return "cuando"
        return "blanco"


label e6_formacion_neutral:
    $ e6_formacion({"ichika": "neutral", "nino": "neutral", "miku": "neutral", "yotsuba": "neutral", "itsuki": "neutral"})
    with dissolve
    return

label e6_entrar(h):
    $ e6_entrar(h)
    with dissolve
    return

label e6_foco(quien="", expr=""):
    $ e6_mostrar_foco(quien, expr)
    with disolucion_lenta
    return


################################################################################
##  EVENTO 6 — ORQUESTADOR
################################################################################

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


################################################################################
##  MOV. 1 · LUNES
################################################################################

label e6_lunes:

    $ ui_escena("beat", None, "Semana de exámenes")
    $ tiempo_restante = "cinco exámenes"
    $ e6_limpiar()

    stop music fadeout 1.0
    stop ambiente

    scene bg_escuela
    with fade_dia

    play sound audio.sfx_timbre volume 1.5

    narrador "El timbre sonó en un instituto donde nadie hablaba de otra cosa."

    narrador "Otra cosa que no sean los exámenes."

    mc_pensamiento "Lunes, japonés. Martes, matemáticas. Miércoles, inglés. Jueves, ciencias. Viernes, sociales."

    mc_pensamiento "Cada día, una materia. Y detrás de cada materia, una de ellas."

    mc_pensamiento "Como dijo Miku, son cinco materias y ellas con cinco."

    mc_pensamiento "Pensé que lo dijo por decir, pero esa frase tenía un gran significado."

    mc_pensamiento "Un significado que ahora descubriré."

    call expression ("e6_s1_" + e6_estado_entrada)

    ## --- Aula: el discurso de MC (POV de las cinco) ----------------------------
    scene bg_aula
    with fade

    scene cg_cinco_aula
    with dissolve

    narrador "Las cinco ya estaban en el aula, con los libros cerrados."

    narrador "No por desinterés: por haber llegado al final de lo que se podía repasar."

    narrador "Me miraron, y cada una se acercó hacia mí."

    mc_pensamiento "Supongo que esperan alguna típica frase de aliento por parte mía."

    mc_pensamiento "Nunca he sido bueno en eso, pero..."

    mc "¡Hola, chicas! ¿Preparadas para los exámenes?"

    mc "Sé que todas tienen dudas o miedos sobre si aprobarán o no."

    mc "Pero recuerden todo este mes que hemos estudiado."

    mc "¡Todos nosotros dimos nuestro mejor esfuerzo!"

    mc "¡Así que sé que lo lograrán! ¡Aprobarán los exámenes!"

    mc "¡Confío plenamente en ustedes!"

    mc "¡ASÍ QUE TODOS APROBAREMOS! ¡SIN EXCEPCIÓN!"

    mc_pensamiento "Fue una de las mejores frases de aliento que he lanzado en mi vida."

    mc_pensamiento "Di lo mejor de mí."

    mc_pensamiento "Y ellas escucharon lo que dije... Escuché lo que dije."

    narrador "Cada una reaccionó de distinta manera."

    narrador "Y me confesaron todo."

    ## --- Confesiones. Orden fijo: Yotsuba, Ichika, Miku, Itsuki, Nino ------------
    scene bg_aula
    with dissolve

    call e6_formacion_neutral

    ## Yotsuba
    if e6_estado_de("yotsuba") != "no_visitada":

        call e6_foco("yotsuba", "sonriendo")

        yotsuba "¡Estudié las lecturas dos veces! Y todavía recuerdo qué sentía cada personaje."

        yotsuba "Esta vez no las dejé para después: ayudé a Miku con las fechas y a Ichika con las fórmulas, ¡pero calenté mis lecturas primero!"

        yotsuba "Como antes de una carrera: si no calientas, el cuerpo se queja a mitad de camino."

        yotsuba "Así que no te preocupes por mí, [mc]. ¡Voy a llegar a la meta, y las cinco juntas!"

    else:

        call e6_foco("yotsuba", "neutral")

        yotsuba "¡Repasé las fechas con Miku y las fórmulas con Ichika!"

        yotsuba "…Mis lecturas, para después. Siempre se quedan para después."

        yotsuba "Quería terminar a tiempo para que nadie se desmayara de los nervios antes del examen, ¡tú incluido, [mc]!"

        yotsuba "¡Pero lo intentaré con toda la energía que me queda!"

    ## Ichika
    if e6_estado_de("ichika") != "no_visitada":

        call e6_foco("ichika", "sonriendo")

        ichika "Dormí cuatro horas por estudiar fórmulas, no en el papel de la obra."

        ichika "Rarísimo, ¿no? Yo, que me sé el guion entero y las fórmulas a medias."

        ichika "El guion está en la mochila, doblado, y de ahí no sale hasta el último timbre."

        ichika "Y si todo sale bien, tú, tutor terco, me debes una tarde entera sin libros."

    else:

        call e6_foco("ichika", "neutral")

        ichika "Dormí cuatro horas. Con el guion en una mano y las fórmulas en la otra."

        ichika "Supongo que me distraje pensando en si de verdad lograríamos aprobarlo todo."

        ichika "Aunque… un poco de compañía esa tarde no me habría venido mal, ¿sabes?"

        ichika "Las hermanas mayores también necesitamos que alguien nos eche una mano de vez en cuando, ¿no crees, [mc]?"

    ## Miku
    if e6_estado_de("miku") != "no_visitada":

        call e6_foco("miku", "animada")

        miku "…Sé más de lo que van a preguntar. …Lo comprobé tres veces."

        miku "…Repasé las batallas, los clanes, las fechas. …Hasta lo que ni sale en el libro."

        miku "…La silla de enfrente ya no se siente vacía."

        miku "…Por si acaso, lo comprobaré una cuarta vez. …Ya sé que es demasiado."

    else:

        call e6_foco("miku", "neutral")

        miku "…Repasé sola, como siempre."

        miku "…Las batallas, los clanes, las fechas. …Todo, dos veces."

        miku "…Dejé libre la silla de enfrente. …Por costumbre."

        miku "…No esperaba a nadie. …Eso quiero pensar."

    ## Itsuki
    if e6_estado_de("itsuki") != "no_visitada":

        call e6_foco("itsuki", "sonriendo")

        itsuki "He estudiado cada noche. Y por primera vez sé lo que hago."

        itsuki "Ya encontré por qué fallaba en las conversiones de unidades. Tres veces el mismo error, y yo sin verlo."

        itsuki "Sigo sin ser rápida. Pero ahora, cuando me trabo, sé por dónde volver."

        itsuki "No me felicites todavía. Esto se demuestra en el examen, no antes."

    else:

        call e6_foco("itsuki", "neutral")

        itsuki "He estudiado cada noche. Si tengo un problema que no sale. Saldrá."

        itsuki "Lo repito, lo reviso, lo repito otra vez. …Siempre llego a la misma cifra."

        itsuki "No pedí ayuda a nadie. Prefiero equivocarme por mi cuenta que acertar por ayuda de un tercero."

        itsuki "Dijiste «sin excepción». Pues prepárate: yo me lo tomo en serio."

    ## Nino
    if e6_estado_de("nino") != "no_visitada":

        call e6_foco("nino", "pillada")

        nino "Treinta días. El último tutor duró cuatro. …Haz la cuenta tú."

        nino "Y no pongas esa cara. Yo no dije nada. Los números hablan solos."

        nino "Repasé inglés leyendo etiquetas en voz baja. …Si me viste mover los labios en el súper, no viste nada."

        nino "Y la próxima vez que quieras dar un discurso, baja la voz. Se oyó hasta el pasillo."

    else:

        call e6_foco("nino", "neutral")

        nino "No viniste a buscarme y tampoco te fuiste. …No es un cumplido. Es un dato."

        nino "Repasé inglés sola, con las etiquetas de la cocina, en voz baja. …Nadie me escuchó. Mejor para mí."

        nino "Y no, no te estaba esperando. …Contaba los días. Es distinto."

        nino "Ahora cállate un momento y déjame repasar la última página."

    ## --- Cierre del movimiento -----------------------------------------------------
    $ e6_limpiar()

    scene cg_cinco_aula
    with dissolve

    narrador "Me miraron las cinco. Esperaban una frase para terminar."

    mc_pensamiento "Hace un mes no tenía nada que decirles que no fuera mentira."

    mc_pensamiento "Hoy sí. Cada una sabe algo, y yo ya sé que lo sabe."

    mc "Hagan lo que saben."

    narrador "No sonó a relleno. Cada palabra tenía un nombre detrás."

    if persistent.final_malo_temprano_b_visto:

        narrador "Sentí que ya había dicho esa frase antes. Con otro verbo, y con otro final."

        narrador "Siempre me imagino escenarios catastróficos antes de ver mi realidad."

    scene bg_aula
    with dissolve

    profe "Bien, todos a sus pupitres."

    profe "Volteen las hojas de sus exámenes."

    profe "Pueden empezar."

    play sound audio.sfx_hoja volume 2.0

    play ambiente amb_reloj fadein 2.0 volume 0.4

    return


## --- S1 · estado de entrada ------------------------------------------------------
label e6_s1_superado:

    mc_pensamiento "«Si una sola reprueba, se acabó.» Maruo lo dijo en la cocina y no lo repitió."

    mc_pensamiento "No hacía falta. Una frase así no se repite: se cumple."

    mc_pensamiento "Cinco exámenes, cinco días, y esa frase sentada al lado de cada uno."

    mc_pensamiento "Hace un mes comencé este trabajo con una palabra clavada: despedido."

    mc_pensamiento "Hoy entro con cinco nombres. Y con la palabra exactamente donde estaba."

    mc_pensamiento "La diferencia es que ahora sé quién está detrás de cada hoja."

    return

label e6_s1_mixto:

    mc_pensamiento "Treinta días no alcanzan para saber nada. Solo para dejar de ser un desconocido."

    mc_pensamiento "No sé si fue suficiente. Esa es la verdad completa, y es incómodamente corta."

    mc_pensamiento "No tengo una palabra clavada esta vez. Tengo un número: cinco."

    mc_pensamiento "Cinco exámenes que no puedo corregir, ni acompañar, ni adelantar."

    mc_pensamiento "Hoy no se evalúa lo que yo hice. Se evalúa lo que ellas ya sabían."

    return

label e6_s1_bueno:

    mc_pensamiento "Por primera vez en un mes, no me sudan las manos al cruzar la puerta del instituto."

    mc_pensamiento "Las conozco. No a todas igual, pero lo bastante para saber qué se les da bien."

    mc_pensamiento "Eso no garantiza nada. Lo sé. Una nota es una nota."

    mc_pensamiento "Pero esta mañana los cinco nombres suenan distinto:"

    mc_pensamiento "Ya no son una lista más de mi trabajo, son personas."

    mc_pensamiento "O más bien quintillizas, aunque luzcan iguales, cada una es un mundo diferente."

    mc_pensamiento "Y cada una me lo ha demostrado, a su modo."

    mc_pensamiento "Qué raro. Me da más miedo ahora que antes."

    mc_pensamiento "Pero confío en ellas."

    return


################################################################################
##  MOV. 7 · RESULTADOS Y MARUO
################################################################################

label e6_resultados:

    $ ui_escena("normal")
    $ e6_limpiar()

    stop ambiente fadeout 1.0

    scene bg_negro
    with fade_dia

    play sound audio.sfx_celular volume 1.5

    narrador "Sábado a media mañana."

    narrador "Estaba en mi casa, repasando todo lo que sucedió esta semana."

    narrador "Una semana totalmente diferente a las mismas de siempre."

    mc_pensamiento "No hacía nada más que pensar en los resultados de los exámenes."

    mc_pensamiento "No los míos, los de ellas."

    narrador "Sin embargo, el tiempo de espera duró poco."

    narrador "Mi teléfono sonó y tenía el nombre de quien diría el veredicto final."

    narrador "Maruo."

    narrador "El mensaje llegó y decía: «Cinco. Departamento.»."

    mc_pensamiento "Cinco: la hora. O la cuenta. Con Maruo, nunca se sabe cuál de las dos."

    narrador "Me alisté y fui directamente al departamento de las Nakano."

    scene bg_edificio
    with fade

    scene bg_departamento
    with dissolve

    scene cg_maruo_reunion
    with corte_seco

    if e6_estado_entrada == "superado":
        play music contrato fadein 2.0
    else:
        play music contrato fadein 2.0 volume 0.6

    mc "Buenas tardes, señor Maruo."

    maruo "Siéntate."

    mc "Sí, señor."

    narrador "Me senté. Esta vez no había nada que demostrar."

    narrador "Cinco boletines sobre la mesa, boca abajo, alineados al borde."

    maruo "Los resultados llegaron esta mañana."

    maruo "Cinco."

    if persistent.final_malo_temprano_b_visto:

        narrador "Esperé una segunda cifra. Por alguna razón, di por hecho que llegaría."

    mc_pensamiento "Era la cuenta. Era la hora. Y no dijo nada más."

    call expression ("e6_s2_" + e6_estado_entrada)

    maruo "Los exámenes no terminan aquí."

    mc "Lo sé."

    maruo "No lo sabes todavía. El contrato no habla de un examen. Habla de una graduación."

    mc "Entendido."

    maruo "Eso espero."

    play sound audio.sfx_puerta_cierra volume 1.0

    stop music fadeout 2.0

    narrador "Se puso el abrigo y salió. Sin portazo, como siempre. Esta vez, sin que doliera."

    mc_pensamiento "Aprobar no es lo mismo que salvarse. Hoy, por hoy, me alcanzaba con aprobar."

    mc_pensamiento "Aunque saldré de este departamento con un pensamiento totalmente nuevo."

    return


## --- S2 · Maruo según el estado de entrada -----------------------------------------
label e6_s2_superado:

    maruo "Te dije en la cocina que no repetiría la advertencia."

    maruo "No la repetí. Tampoco la cobré."

    mc "¿La condición…?"

    maruo "Se cumplió. Cinco aprobadas. La más baja llegó a sesenta."

    maruo "Un punto menos y esta conversación sería otra."

    narrador "Lo dijo como se anuncia un horario. Y por eso pesó el doble."

    mc_pensamiento "Un punto. Todo el mes colgando de un punto, y sin saber de cuál de las cinco."

    maruo "No esperes que lo celebre. Cumpliste lo que firmaste."

    mc "No lo esperaba."

    narrador "Era mentira, y los dos lo supimos. Maruo, por una vez, la dejó pasar."

    return

label e6_s2_mixto:

    maruo "Aprobaron las cinco. Hay márgenes que no me gustan."

    mc "¿Qué tienen de malo los márgenes?"

    maruo "Nada. Salvo que a veces se aprueba por poco y se cree que fue un éxito."

    narrador "Miró los boletines al decirlo. Pero la frase parecía dirigida a otra mesa."

    mc_pensamiento "No sonó a elogio. Tampoco a reproche. Sonó a alguien que sigue haciendo la cuenta."

    maruo "No me corresponde alegrarme. Tampoco quejarme."

    maruo "Me corresponde que el contrato siga. Y sigue."

    mc "Gracias."

    maruo "No me las des. No es un favor."

    return

label e6_s2_bueno:

    maruo "Tu padre me habló de alguien que no se rendía."

    maruo "Me faltaba ver qué hacía ese alguien mientras no se rendía."

    mc "¿Y qué vio?"

    maruo "Mis hijas llegan a casa y hablan de lo que estudian. Antes llegaban y se encerraban."

    maruo "Pensé que era la edad. Que se les pasaría."

    maruo "No era la edad."

    mc "Yo no hice tanto, señor."

    maruo "No te pedí humildad. Te dije lo que vi."

    maruo "Esta semana, cada noche, las cinco en la cocina discutiendo a la vez."

    maruo "Por quién lava los platos, por quién se queda con el último bocado."

    maruo "Una noche estuve diez minutos en el pasillo. No entré."

    maruo "No quería que se callaran."

    maruo "Parecía que alguien las había cambiado."

    stop music fadeout 0.3

    narrador "Alineó los boletines con dos dedos, aunque ya estaban alineados."

    narrador "Seguían boca abajo. Ninguno de los dos hizo el gesto de darles la vuelta."

    maruo "No te lo repetiré: esto no fue una casualidad."

    mc "…Gracias, señor."

    maruo "Aún no hay nada que agradecer."

    return


################################################################################
##  MOV. 8 · LAS CINCO (puertas → intento → mesa → foto)
##  Ecos de Yotsuba e Ichika: abajo. Los de Nino, Itsuki y Miku: stubs (Chat 9).
################################################################################

label e6_cinco:

    scene bg_departamento
    with dissolve

    $ e6_limpiar()

    narrador "Esperé a que ellas salieran."

    narrador "En esta sala el silencio y la espera siempre han sido lo mismo."

    if persistent.final_malo_temprano_b_visto:

        narrador "Conocía ese ruido de puertas abriéndose una por una. Lo recordaba terminando peor."

    $ e6_cola = e6_orden_ecos()
    $ e6_i = 0

    while e6_i < 5:

        $ e6_h = e6_cola[e6_i]

        if e6_i == 3:

            narrador "Las dos últimas puertas tardaron un poco más."

            narrador "Detrás de esas no había falta de ganas. Había costumbre de esperar."

        play sound audio.sfx_puerta_abre volume 1.2

        call e6_entrar(e6_h)

        if e6_i == 0:

            narrador "Cada una vino a por su boletín. Boca abajo, sin mirarlo."

            narrador "Como se lleva algo que todavía no es de uno."

        call expression ("e6_" + e6_h + "_eco_" + e6_estado_de(e6_h))

        $ e6_i += 1

    call e6_intento
    call e6_mesa

    return


## --- El intento interrumpido (la disculpa NO se gasta) ----------------------------
label e6_intento:

    narrador "Éramos seis en la sala, y por primera vez nadie parecía estar aquí por obligación."

    narrador "La primera en querer hablar fue ella, Itsuki."

    narrador "Itsuki dio un paso hacia mí. Yo, sin proponérmelo, di otro hacia ella."

    narrador "Aun había cosas pendientes que teníamos que resolver."

    call e6_foco("itsuki", "neutral")

    itsuki "Sobre lo del primer día—"

    mc "Sobre lo del asiento—"

    narrador "Nos detuvimos los dos. A media frase, a medio paso."

    itsuki "Tú primero."

    mc "No. Tú."

    itsuki "Dije que tú primero. Es una oración completa."

    mc "«No, tú» también lo es."

    mc "Además, las damas primero."

    itsuki "…Ese argumento es válido."

    call e6_foco("yotsuba", "sonriendo")

    yotsuba "¡¡Esperen!! ¡Antes de que se arruguen! ¡Los boletines! ¡Ya están en la mesa!"

    narrador "Itsuki se calló. Yo también me callé. La frase se quedó entre los dos, sin dueño."

    mc_pensamiento "La disculpa seguía entre nosotros. Y esta vez no me pareció tarde: me pareció pendiente."

    narrador "Así es, parece que eso aún seguirá pendiente."

    $ e6_disculpa_pendiente = True

    return


## --- La mesa, el discurso y la foto ------------------------------------------------
label e6_mesa:

    narrador "Nos sentamos alrededor de la mesa sin que nadie lo propusiera."

    narrador "Ellas, de un lado. Yo, enfrente. Cada una dejó su boletín frente a su silla, boca abajo."

    narrador "Ninguna lo tocó. Ninguna quería ser la primera en darle la vuelta."

    call e6_foco("itsuki", "neutral")

    itsuki "Propongo lo siguiente."

    itsuki "Cada una lo abre en silencio, lo lee dos veces y solo después comparamos."

    call e6_foco("ichika", "sonriendo")

    ichika "Qué plan tan ordenado, Itsuki."

    ichika "Hablas con mucha confianza para alguien que lleva un minuto con la mano encima del papel."

    call e6_foco("itsuki", "timida")

    itsuki "…Es para que no se vuele."

    call e6_foco("nino", "neutral")

    nino "No hay ninguna ventana abierta."

    call e6_foco("itsuki", "timida")

    itsuki "…Es por si acaso."

    call e6_foco("ichika", "neutral")

    ichika "Hablando por todas, debería decir que todo va a salir bien."

    ichika "…¡Corazonada de hermana mayor!"

    call e6_foco("yotsuba", "incomoda")

    yotsuba "¡A todas les habrá ido genial! ¡Seguro!"

    yotsuba "Y si a alguna no… ¡no pasa nada! ¡Cenaremos un plato hecho por Nino y se nos pasa!"

    yotsuba "…Pero si a mí no me fue bien, ¡que nadie ponga cara de puchero, eh!"

    call e6_foco("nino", "nerviosa")

    nino "Seis sillas ocupadas. …Seis personas en esta mesa."

    nino "Hace un mes no habría apostado por que todos estuvieramos reunidos. Sin problemas."

    nino "…Es una observación. No le des importancia."

    call e6_foco("miku", "encogida")

    narrador "Miku tenía las manos juntas delante del cuerpo y los audífonos colgados al cuello. Sin tocarlos."

    miku "…Hoy no me los puse."

    miku "…Quiero oír lo que diremos todas."

    miku "…Todas a la vez."

    call e6_foco("nino", "molesta")

    nino "Tú estuviste con él antes de que saliéramos. …Sabes algo."

    mc_pensamiento "Sabía que ninguna se quedaba fuera. No sabía nada más: ni cuánto, ni de quién."

    mc_pensamiento "Y sabía que no me tocaba a mí quitarles este momento."

    mc "Sé lo que Maruo me dijo a mí. Lo que dicen esos papeles es de ustedes."

    call e6_foco("ichika", "sonriendo")

    ichika "Qué tutor más cruel."

    mc "Lo sé."

    call e6_foco("itsuki", "neutral")

    itsuki "Tu expresión no es la de quien trae malas noticias. …Aunque no es una garantía."

    call e6_foco("yotsuba", "sonriendo")

    yotsuba "¡¡Entonces abrámolos ya!!"

    call e6_foco("nino", "neutral")

    nino "A la de tres. Y que nadie mire de reojo."

    nino "Una. Dos. Y…"

    ## Cinco hojas, un solo sonido: UN solo play (el canal sound es único).
    play sound audio.sfx_hoja volume 2.0

    narrador "Dieron vuelta a los cinco boletines a la vez. Y, claro, todas miraron de reojo."

    pause 1.5

    narrador "Cinco hojas, un solo sonido."

    play music main_theme fadein 1.5

    call e6_foco("miku", "encogida")

    miku "…Sonaron juntas. …Como si fuera una sola hoja."

    narrador "Una lágrima le recorrió por toda la cara. No se la secó."

    miku "…No es tristeza. …Es que no sé dónde poner esto."

    call e6_foco("ichika", "sonriendo")

    narrador "Ichika soltó una risa corta, de las que se escapan solas."

    ichika "Ja. …Ja, ja. …Me quedé sin chiste. A mí, que siempre tengo uno."

    ichika "Cuatro horas de sueño. …Y valieron cada minuto. Qué cosa más rara."

    call e6_foco("nino", "nerviosa")

    narrador "Nino leyó el suyo. Luego miró el de Miku, el de Yotsuba, el de Ichika, el de Itsuki. Movía los labios sin sonido."

    nino "Uno. Dos. Tres. Cuatro. …Cinco."

    nino "Cinco. Los conté dos veces."

    nino "…Que nadie diga nada. Si alguien dice algo, me voy."

    narrador "Se le quebró la voz en la última palabra. Nadie dijo nada. Nino se quedó."

    call e6_foco("yotsuba", "animada")

    narrador "Yotsuba ni miró el suyo. Miraba los de las demás, uno por uno, con los ojos muy abiertos."

    yotsuba "¡Todas! ¡¡Todas, todas, todas!!"

    yotsuba "¡¡Miku, mira el tuyo!! ¡¡Nino, el tuyo!!"

    ichika "Yotsuba. El tuyo."

    yotsuba "¿Eh? …¡Ah, el mío!"

    call e6_foco("yotsuba", "neutral")

    narrador "Bajó la vista. Y, por primera vez en todo el mes, Yotsuba se quedó callada."

    yotsuba "…Este es mi boletín. …Esta soy yo. …Esto lo hice yo."

    call e6_foco("yotsuba", "animada")

    yotsuba "¡¡Y lo hicimos todas!! ¡¡Y tú también, [mc]!!"

    yotsuba "¡Tú te quedaste hasta el último momento! ¡Eso también cuenta!"

    call e6_foco("itsuki", "sonriendo")

    narrador "Itsuki lo leyó línea por línea, como se lee un contrato. Dos veces, tal como había propuesto."

    itsuki "Lo leí dos veces. …El resultado no cambió."

    itsuki "Debería decir algo acorde a este momento."

    itsuki "…Estoy pensando qué decir, pero no tengo ni idea."

    itsuki "Lo que siento no lo puedo expresar con palabras."

    itsuki "…Anótenlo, provisionalmente, como «algo bueno»."

    narrador "Entonces levantó la vista y me miró. Quiso decirme algo. Pero nuevamente se calló."

    narrador "Yo asentí, apenas. Lo de antes seguía ahí, entre los dos, y esta vez ninguno intentó sacarlo."

    call e6_foco("ichika", "sonriendo")

    ichika "Y tú, tutor. Tienes cara de querer decirnos algo."

    mc "No tengo nada que decirles. Esta vez no."

    call e6_foco("itsuki", "neutral")

    itsuki "Es un alivio. Eres malo dando discursos."

    call e6_foco("ichika", "sonriendo")

    ichika "La última vez fue «sin excepción». A gritos."

    mc "Lo sé. Solo quiero decir una cosa, y corta."

    mc "Hace un mes, esta mesa me daba miedo. Cinco personas iguales mirándome, esperando que yo supiera qué hacer."

    mc "Los primeros días me botaron rápidamente de su departamento, no querían que sea su tutor."

    mc "No porque me odiaran, sino por los temores que cada una tenía."

    mc "Cargas que no podían aliviarlas solas y se las guardaban como si no fueran importantes."

    mc "Por eso yo no me rendí. Nunca lo hago."

    mc "A pesar de que me odiaran yo seguía yendo y yendo."

    mc "Creía que era solo por el trabajo y la paga."

    mc "Pero me di cuenta que no es así, hay algo de ustedes que intenté descubrir."

    mc "Hoy sigo sin saberlo del todo. Pero ya no veo cinco iguales."

    mc "Veo a una Yotsuba. A una Ichika. A una Miku. A una Itsuki. A una Nino."

    mc "Cada una con su cara, su manera, su ruido."

    mc "Lo que sea que diga ese papel lo escribieron ustedes. Nadie se los regaló."

    mc "Y estoy contento de haber estado sentado frente a esta mesa cuando lo abrieron."

    mc "Nada más."

    stop music fadeout 0.5

    call e6_foco("nino", "molesta")

    nino "…Eso fue un discurso."

    mc "Dije que no tenía mucho que decir."

    nino "Fue un resumen. Pocas frases. Las conté."

    call e6_foco("miku", "encogida")

    miku "…Fue lindo."

    miku "…A tu manera... Fue lindo."

    miku "…Gracias por tus palabras, [mc]."

    call e6_foco("itsuki", "neutral")

    itsuki "Breve. Aceptable. Bien dicho."

    mc_pensamiento "Hace un mes se pusieron de acuerdo para fallar igual."

    mc_pensamiento "Hoy se pusieron de acuerdo para mostrarse distintas."

    play music main_theme fadein 2.0

    call e6_foco("yotsuba", "animada")

    yotsuba "¡Cada una, muestre su examen! ¡Y nos tomaremos una foto!"

    yotsuba "¡La subiremos al grupo! ¡Sin trampas!"

    yotsuba "¡[mc], tú la sacas! ¡Tienes los brazos más largos!"

    mc "¿Y yo no salgo?"

    yotsuba "¡Tú sales en la próxima! ¡Hoy es de las cinco!"

    narrador "Me puse de pie al otro lado de la mesa, con el celular de Yotsuba en las manos."

    yotsuba "¡Más arriba! ¡El mío más arriba!"

    call e6_foco("ichika", "sonriendo")

    ichika "Que se me vea la cara, no el flequillo."

    call e6_foco("nino", "neutral")

    nino "Un solo brazo. Es mi mejor ángulo."

    call e6_foco("miku", "encogida")

    miku "…¿Dónde pongo las manos? …Mejor delante."

    call e6_foco("itsuki", "neutral")

    itsuki "Debo salir recta. Con el boletín recto."

    ## --- CG de las cinco: el estado de entrada solo cambia el tinte -----------------
    $ e6_limpiar()

    if e6_estado_entrada == "superado":

        scene cg_cinco_aprobadas at e6_tinte_superado
        with dissolve

    elif e6_estado_entrada == "bueno":

        scene cg_cinco_aprobadas at e6_tinte_bueno
        with dissolve

    else:

        scene cg_cinco_aprobadas at e6_tinte_mixto
        with dissolve

    mc "¡Digan «cinco»!"

    quintillizas "¡¡Cinco!!"

    if renpy.loadable("audio/sfx/camara.mp3"):
        play sound audio.sfx_camara volume 1.5

    narrador "Tomé la foto. Ninguna bajó el boletín."

    ichika "¿Ya está? …Me tiembla el brazo y no pienso ser la primera en bajarlo."

    nino "Yo tampoco. …Que baje primero Yotsuba."

    yotsuba "¡Yo no bajo nada! ¡Puedo quedarme así hasta mañana!"

    itsuki "Los brazos no funcionan así. Tarde o temprano se cansan."

    yotsuba "¡Pues que se cansen tarde!"

    miku "…Yo tampoco quiero bajar las manos todavía. …Mientras sigamos así, …esto sigue pasando."

    narrador "Nadie se rio. Se quedaron un momento en silencio, juntas, cada una en su sitio, con la hoja en alto."

    mc_pensamiento "Pensé en decirles que la foto ya estaba. No lo dije. Hay cosas que un «ya está» arruina."

    ichika "Oigan, ¿saben qué es lo más raro?"

    ichika "…Que esta mañana tenía miedo de abrirlo sola. Y no estaba sola."

    nino "…Nunca había estado tan cansada. …Y tan bien. …Que no se repita esa frase."

    itsuki "Lo anoto. «Nino dijo: tan bien.»"

    nino "Si lo anotas, te lo quito."

    itsuki "Es un registro. Los registros no se quitan."

    yotsuba "¡Quiero una foto así cada vez que algo salga bien!"

    yotsuba "¡Y cuando salga mal, también! ¡Igual de juntas!"

    itsuki "…Moción aceptada. Con una condición: el boletín, recto."

    miku "…Yo también. …Aunque salga mal. …Sobre todo si sale mal."

    nino "No hablemos de que salga mal el día en que salió bien."

    mc "Si sale mal, la foto la saco yo. Y la guardo igual que esta."

    ichika "Qué tutor más cursi. …Me gusta."

    mc "Pues yo no bajo el celular hasta que baje el último brazo."

    itsuki "Entonces será larga la espera. …Bajo en tres."

    yotsuba "¡Una! ¡Dos!"

    nino "…Y."

    narrador "Bajaron los brazos todas a la vez, sin contarlo. Igual que habían abierto los boletines."

    mc_pensamiento "No leí ni un solo número. No hacía falta: cinco caras que ya no fingían nada."

    mc_pensamiento "Dijeron «cinco». Y yo, detrás del celular, dije «seis». Bajito, para que no me oyeran."

    mc_pensamiento "Ahora formo parte de ellas, y ellas de mí."

    return


################################################################################
##  MOV. 9 · CASA
################################################################################

label e6_casa:

    scene bg_negro
    with fade

    narrador "Me despedí de todas y volví a casa."

    narrador "Con una gran sensación de seguir conservando mi trabajo."

    stop music fadeout 1.5

    scene bg_comedor
    with fade

    play music cena fadein 2.0

    narrador "Al llegar, alguien me estaba esperando, y yo también quería verla."

    mc_pensamiento "Mi hermana Raiha, la única que ha confiado en mí desde el principio."

    mc_pensamiento "Una de las razones por las que acepté el trabajo cuando no sabía qué decidir."

    narrador "El curry se olía por toda la casa."

    show raiha hablando at pj_habla(0.20)
    show isanari neutral at pj_calla(0.73)
    with dissolve

    raiha "¡Hermanito! Hice curry antes de saber cómo te iba a ir."

    raiha "Así, como te haya ido, la cena ya está hecha. ¡El curry nunca falla!"

    mc "Pues hoy comeremos un banquete, ¿no crees, Raiha?"

    mc "¡¡APROBARON LAS CINCO!!"

    raiha "…¿Las cinco?"

    mc "Las cinco."

    raiha "¡¡LAS CINCO!!"

    raiha "¡Te dije que podías con cinco a la vez!"

    mc "Me lo dijiste con voz de «ojalá»."

    mc "Aunque te perdono porque también dudaba de mí en ese momento, jeje."

    raiha "¡Pero la voz de «ojalá» también cuenta!"

    show raiha hablando at pj_calla(0.20)
    show isanari neutral at pj_habla(0.73)
    with disolucion_lenta

    isanari "Hola, [mc], veo que hoy ha sido un éxito para ti."

    isanari "Maruo llamó. Cobramos el mes entero."

    mc "Lo sé."

    isanari "Pareces menos contento de lo que dice el pago."

    mc "No estoy menos contento. Estoy pensando en otra cosa."

    isanari "¿Qué cosa vale más que cinco veces la tarifa?"

    mc "Todavía no lo sé."

    narrador "Mi padre no contestó. Pero se quedó mirando su plato más tiempo del necesario."

    show raiha hablando at pj_habla(0.20)
    show isanari neutral at pj_calla(0.73)
    with disolucion_lenta

    raiha "¡A comer! ¡Que se enfría!"

    mc_pensamiento "Hace un mes, «cinco veces la tarifa» era lo único que oía en esa frase."

    mc_pensamiento "Esta noche la oí de fondo, como se oye un reloj en otro cuarto."

    mc "Gracias por la comida."

    narrador "Lo dije por costumbre. Pero esta vez la costumbre pesaba lo mismo que las palabras."

    mc_pensamiento "Hace un mes, «todo» era una deuda y una hermana pequeña."

    mc_pensamiento "Esta noche el «todo» tenía cinco personas más. Y ninguna cabía en una factura."

    return


################################################################################
##  MOV. 10 · CUARTO, CHAT Y LIBRETA
################################################################################

label e6_cuarto:

    stop music fadeout 1.5

    hide raiha
    hide isanari

    scene bg_cuarto_mc
    with fade

    play music hogar fadein 1.5 volume 0.7

    narrador "El celular empezó a vibrar antes de que terminara de sentarme."

    $ duck()
    play sound audio.sfx_celular volume 1.5

    $ quick_menu = False
    show screen chat_grupo

    narrador "El grupo seguía llamándose «¡Equipo Quintillizas + Tutor!». Yotsuba nunca lo cambió."

    narrador "Nino no se había salido. Ni una vez en toda la semana de exámenes."

    mc_pensamiento "No contesté. Cualquier cosa que escribiera iba a ser menos que lo que acababa de leer."

    $ e6_chat_activo = True

    ## --- La cuenta ---------------------------------------------------------------
    hide screen chat_grupo
    with dissolve

    mc_pensamiento "Hay algo que sé hacer sin que nadie me enseñe: sumar."

    $ e6_boletin_fase = 1
    show screen boletin_cinco

    mc_pensamiento "Tomé la nota más alta de cada una."

    $ e6_boletin_fase = 2

    mc_pensamiento "Japonés, matemáticas, inglés, ciencias, sociales. Cien, cien, cien, cien, cien."

    $ e6_boletin_fase = 3

    mc_pensamiento "Cinco notas perfectas en cinco materias distintas. Esa diagonal lo delata."

    mc_pensamiento "Un boletín perfecto. De un alumno que no existe."

    mc_pensamiento "Existe, pero repartido: cada una guarda lo que a las otras cuatro les falta."

    mc_pensamiento "Y en todo el mes no se habían preguntado nada entre ellas."

    mc_pensamiento "No controlé ninguna de esas cinco notas."

    mc_pensamiento "Lo único que controlé fue a dónde fui."

    mc_pensamiento "Y a dónde no."

    mc_pensamiento "Cinco hojas en fila. Cinco notas de cien. Cada cien, de una persona distinta."

    mc_pensamiento "Y entonces lo entendí, lo que siempre me estaba preguntando."

    mc_pensamiento "Cada una, sola, es una quinta parte. Brillante, pero una parte."

    mc_pensamiento "Juntas son lo que ninguna sería sola: un estudiante perfecto. Capaz de cualquier cosa."

    mc_pensamiento "Yo creí que mi trabajo era enseñarles a estudiar."

    mc_pensamiento "Mi trabajo era conseguir que, por fin, se miraran entre ellas."

    hide screen boletin_cinco
    $ quick_menu = True

    ## --- La libreta ------------------------------------------------------------------
    scene cg_libreta
    with fade

    narrador "Abrí la libreta por la página de los cinco nombres. Seguía la frase de aquella noche."

    mc_pensamiento "«De frente y las cinco a la vez, pierdo siempre.»"

    narrador "Debajo escribí otra. La letra me salió más firme que la primera vez."

    narrador "«De una en una las alcancé. ¿Y de frente, las cinco a la vez?»"

    python:
        e6_p1 = ""
        e6_p2 = ""
        if len(e6_promesas) > 0:
            e6_p1 = e6_promesas[0].capitalize()
        if len(e6_promesas) > 1:
            e6_p2 = e6_promesas[1].capitalize()

    narrador "Y debajo, más chico, dos nombres: [e6_p1] y [e6_p2]."

    mc_pensamiento "Dos promesas hechas sin que nadie me las pidiera. Esas no caducan."

    call expression ("e6_s3_" + e6_estado_entrada)

    stop music fadeout 3.0

    scene bg_negro
    with fade

    return


## --- S3 · última línea del capítulo -------------------------------------------------
label e6_s3_superado:

    mc_pensamiento "Maruo dijo «cinco». No dijo «para siempre»."

    mc_pensamiento "La condición no se venció: se renovó."

    mc_pensamiento "Esta vez, un punto de margen. ¿Cuántos tendré la próxima?"

    return

label e6_s3_mixto:

    mc_pensamiento "Aprobaron las cinco. Lo repasé tres veces, por si el papel cambiaba de opinión."

    mc_pensamiento "No sé qué parte fue mía. Tampoco sé a quién preguntárselo."

    mc_pensamiento "La libreta no tiene una casilla para eso."

    return

label e6_s3_bueno:

    mc_pensamiento "Abrí las fotos sin contener el aire. Hace un mes no sabía hacerlo."

    mc_pensamiento "Los cinco nombres ya no son una lista. Son cinco personas que salieron bien."

    mc_pensamiento "Y cuando alguien te importa, lo único que queda por temer es lo que viene después."

    return


################################################################################
##  MOV. 2 · YOTSUBA · LUNES · JAPONÉS
################################################################################

label e6_yotsuba_nucleo:

    $ ui_escena("beat", "yotsuba", "Aula · Japonés")
    $ tiempo_restante = "cinco exámenes"
    $ e6_limpiar()

    scene cg_yotsuba_examen
    with dissolve

    narrador "Lunes. Japonés. La primera de cinco hojas."

    narrador "Mi pupitre quedaba en la segunda fila, junto al pasillo. Desde ahí se veían las cinco nucas."

    narrador "Terminé el mío antes de la mitad. Lo dejé boca abajo, con el lápiz encima."

    mc_pensamiento "Ahora solo me quedaba mirar."

    narrador "En un examen nadie habla. Eso no quiere decir que nadie piense."

    narrador "Yotsuba escribió su nombre primero. Siempre lo hace."

    mc_pensamiento "El uno por ciento del primer día, bien hecho. Esta vez era solo el principio de la hoja."

    return


label e6_yotsuba_mono_calida:

    play music descubrimiento fadein 2.0

    yotsuba_int "Pregunta uno. ¿Qué siente el protagonista cuando se queda solo?"

    yotsuba_int "Lo sé. Conté veintitrés vueltas sola, y alguien llevaba ocho mirándome."

    yotsuba_int "Me dijo que mis hermanas no hacen lo que yo hago. Que él tampoco. Y que lo intenta."

    yotsuba_int "Me dijo que mi punto de partida no era cero. Que nunca lo fue."

    yotsuba_int "Dijo que es pésimo animando a la gente. Y me animó igual."

    yotsuba_int "Veinticinco no es un número perfecto. Lo busqué: el perfecto es el veintiocho."

    yotsuba_int "Sus divisores son uno, dos, cuatro, siete y catorce. Cinco números. Suman veintiocho."

    yotsuba_int "Cinco números distintos, y ninguno sobra. Si falta uno, la cuenta no cierra."

    yotsuba_int "Yo siempre pensé que era el uno. El más pequeño. El que nadie cuenta."

    yotsuba_int "Me falta la segunda línea de la respuesta: qué pasa cuando alguien llega. Esa no me sale."

    yotsuba_int "Un relevo no se gana corriendo más que nadie. Se gana recibiendo bien. Vamos."

    return

label e6_yotsuba_mono_tibia:

    yotsuba_int "Pregunta uno. ¿Qué siente el protagonista cuando se queda solo?"

    yotsuba_int "Un minuto con diecisiete. Después, catorce. Tres segundos menos."

    yotsuba_int "Dijo «claro, dame el cronómetro» sin preguntar nada más."

    yotsuba_int "No sé si me sirvió que alguien mirara o si solo me dejó correr."

    yotsuba_int "Las piernas me avisan siempre. Hoy no me avisan de nada."

    yotsuba_int "Si termino rápido, ¿alguien va a necesitarme para algo?"

    yotsuba_int "Ichika duerme poco. Nino cocina. Miku ya sabe. Itsuki estudia."

    yotsuba_int "Yo corro y animo, y en un examen no se anima a nadie."

    yotsuba_int "Escribo que el protagonista se queda solo y espera. Eso sí lo sé."

    yotsuba_int "Yo también im—"

    yotsuba_int "¡Pregunta dos!"

    return

label e6_yotsuba_mono_fria:

    yotsuba_int "Pregunta uno. ¿Qué siente el protagonista cuando se queda solo?"

    yotsuba_int "«Entonces concéntrate en correr. Si es lo tuyo, hazlo bien.» Eso dijo."

    yotsuba_int "Pues lo hago bien. Escribo lo justo."

    yotsuba_int "Antes miraba a Ichika, a Miku, a Itsuki. Mirar es perder tiempo. Ya no miro."

    yotsuba_int "Dejé de contar las vueltas en voz alta. Ya no me hace falta."

    yotsuba_int "Nadie me pidió que me callara. Solo que me concentrara."

    yotsuba_int "Escribo que el protagonista se queda solo. Y ya está. Una línea. Con eso basta."

    yotsuba_int "Lo mío es correr. Está bien."

    yotsuba_int "¡Está bien!"

    yotsuba_int "Pregunta dos."

    return

label e6_yotsuba_mono_no_visitada:

    yotsuba_int "Pregunta uno. ¿Qué siente el protagonista cuando se queda solo?"

    yotsuba_int "Sé cómo se siente esperar. Entrené quince minutos más cada tarde, por si venía."

    yotsuba_int "Cronometré dos vueltas de más. Por si acaso. Las conté."

    yotsuba_int "No vino. No pasa nada. Tres tardes no alcanzan para cinco. Eso lo entiende cualquiera."

    yotsuba_int "Si nadie me necesita, ¿para qué me sobra tanta energía?"

    yotsuba_int "Entonces la reparto. Tres vueltas de ventaja para cuando venga. Si viene."

    yotsuba_int "Escribo que el protagonista espera a alguien y no sabe si llega."

    yotsuba_int "Es una buena respuesta. Y es la única que no puedo comprobar."

    return


label e6_yotsuba_mj:

    play music yotsuba fadein 1.0 fadeout 1.5

    call mj_ejecutar(E6_MJ_JUEGO["yotsuba"], "yotsuba")
    $ e6_res = _return

    stop music fadeout 3.0

    narrador "Yotsuba soltó el lápiz un segundo y respiró hondo, como se respira al acabar una serie."

    yotsuba_int "Cada tramo mide lo mismo. Ninguna carrera la gana una sola."

    yotsuba_int "Yo importo igual que mis hermanas."

    yotsuba_int "Y el testigo no pesa menos por pasar por mis manos."

    yotsuba_int "Segunda línea: el protagonista quería que alguien llegara. Y alguien llegó."

    yotsuba_int "¡Pregunta dos!"

    if e6_res == "saltado":

        narrador "Hay carreras que se corren por dentro. Esta la corrió entera, de un tirón."

    return


label e6_yotsuba_promesa:

    mc_pensamiento "Quince minutos más cada tarde. Los contó, por si yo iba."

    mc_pensamiento "No fui. Eso no se arregla con un examen."

    mc_pensamiento "Cuando esto termine voy a la pista. Esas dos vueltas de más las cronometro yo."

    return


label e6_yotsuba_gesto_calida:

    narrador "Escribía sin parar y, de vez en cuando, levantaba la vista hacia las demás."

    narrador "Una vez miró a Ichika. Otra, a Miku. Después a Itsuki, y fue un saludo, no una alarma."

    mc_pensamiento "Escribir y mirar a la vez. Nadie le había dicho que se podían hacer las dos cosas."

    narrador "En la muñeca llevaba un 28 con una raya encima. Hoy no necesitaba la cuenta."

    play sound audio.sfx_timbre volume 1.5

    stop music fadeout 1.0

    return

label e6_yotsuba_gesto_tibia:

    narrador "Se le detuvo el lápiz a media palabra. Una sola vez."

    narrador "Miró a las demás, volvió a la hoja y siguió con la pregunta dos, a toda velocidad."

    mc_pensamiento "Esta vez no era una hoja en blanco. Era una frase en blanco."

    mc_pensamiento "Lo que iba a escribir, lo dejó a medias. Y yo no sabía qué era."

    play sound audio.sfx_timbre volume 1.5

    return

label e6_yotsuba_gesto_fria:

    narrador "Escribió de corrido, sin levantar la vista ni una vez. Fue la primera en entregar."

    narrador "Pasó junto a mi pupitre sin mirarme. En la muñeca, ninguna cuenta."

    mc_pensamiento "Esta vez la hoja estaba llena. Esta vez no miró a nadie."

    mc_pensamiento "Lo que mejor sabe hacer, leer a las demás, lo había apagado. Y lo apagué yo."

    play sound audio.sfx_timbre volume 1.5

    return

label e6_yotsuba_gesto_no_visitada:

    narrador "Resolvió su hoja sin dramas. A la mitad se le rompió la punta del lápiz a Ichika."

    narrador "Yotsuba ya tenía uno de repuesto en la mano antes de que Ichika levantara la suya."

    mc_pensamiento "Ni siquiera la miró para saberlo. Eso no se aprende en un libro."

    mc_pensamiento "Reparte lo que le sobra antes de que se lo pidan. Y se queda con lo que le falta."

    play sound audio.sfx_timbre volume 1.5

    return


## --- Ecos de Yotsuba (Mov. 8). Entra ya en pj, neutral; termina en pj_calla ----------
label e6_yotsuba_eco_calida:

    narrador "Yotsuba llevaba el boletín boca abajo en una mano y el rotulador destapado en la otra."

    call e6_foco("yotsuba", "neutral")

    yotsuba "Dame la muñeca. El uno se borró hace días."

    narrador "Escribió un uno. Y detrás, sin pedir permiso, dos ceros."

    yotsuba "Empecé en el uno por ciento. Todavía no sé dónde estoy. Pero ya cabe."

    call e6_foco("yotsuba", "sonriendo")

    yotsuba "¡Esta vez sin corazón torcido! ¡Solo cuenta!"

    call e6_foco("", "")

    return

label e6_yotsuba_eco_tibia:

    narrador "Yotsuba sostenía el boletín con las dos manos, sin darle la vuelta."

    call e6_foco("yotsuba", "neutral")

    yotsuba "Un minuto con catorce. Eso lo sé. Lo demás, no tanto."

    yotsuba "No sé si me ayudaste o solo me dejaste correr."

    mc "Corriste tú."

    call e6_foco("yotsuba", "sonriendo")

    yotsuba "¡Equipo completo! ¡Piernas y cabeza!"

    narrador "Esta vez no sonó a chiste."

    call e6_foco("", "")

    return

label e6_yotsuba_eco_fria:

    narrador "Yotsuba guardó el boletín sin mirarlo, con la sonrisa ya puesta."

    call e6_foco("yotsuba", "sonriendo")

    yotsuba "¡Terminé primera! ¡Eso es bueno! Lo mío es terminar."

    mc "Yotsuba…"

    yotsuba "¡Está bien! ¡De verdad! Hoy no hace falta contar nada."

    narrador "Lo dijo igual de fuerte las dos veces. Una de las dos sobraba."

    call e6_foco("", "")

    return

label e6_yotsuba_eco_no_visitada:

    narrador "Yotsuba miró su boletín con la cara con la que se mira una pista vacía."

    call e6_foco("yotsuba", "sonriendo")

    yotsuba "¡Hola, [mc]! ¡No hace falta que digas nada! Tengo tres vueltas de ventaja."

    mc "Hola, Yotsuba."

    yotsuba "Las vueltas de ventaja no caducan, ¿verdad?"

    mc "No caducan."

    yotsuba "¡Entonces las guardo!"

    call e6_foco("", "")

    return


################################################################################
##  MOV. 3 · ICHIKA · MARTES · MATEMÁTICAS
################################################################################

label e6_ichika_nucleo:

    $ ui_escena("beat", "ichika", "Aula · Matemáticas")
    $ tiempo_restante = "cuatro exámenes"
    $ e6_limpiar()

    scene bg_negro
    with fade_dia

    narrador "Martes. Matemáticas."

    play sound audio.sfx_hoja volume 2.0

    scene cg_ichika_examen
    with fade

    narrador "Mismo pupitre. Mi hoja boca abajo antes de la mitad, otra vez."

    narrador "Ichika leyó el enunciado de principio a fin. Despacio, que en ella ya es una noticia."

    narrador "El guion de la obra asomaba doblado en cuatro por el bolsillo de su falda. Lo había traído. No lo sacó."

    mc_pensamiento "La cuatro era un problema de trenes. De los que se resuelven con una resta y un poco de aire."

    mc_pensamiento "Aire es justo lo que a ella no le sobra."

    return


label e6_ichika_mono_calida:

    play music descubrimiento fadein 2.0

    ichika_int "Pregunta cuatro. Un tren sale a las cuatro cuarenta y cinco."

    ichika_int "Seis minutos a la estación, cuatro para cambiarse. Hay que salir a las cuatro treinta y cinco."

    ichika_int "Me salió antes de terminar de leer. Siempre lo supe. Nunca pensé que eso era matemáticas."

    ichika_int "Él lo notó. Dijo que nadie improvisa un número así. Yo lo llamé ser organizada."

    ichika_int "Después se quedó de pie, sin devolverme el chiste, esperando. Y yo dije lo que no digo."

    ichika_int "«No sé cuánto más puedo seguir haciendo esto.» Lo dije en voz alta. Nadie se cayó por eso."

    ichika_int "Le digo «estoy bien» a todos. Es una contraseña. A él no se la dije."

    ichika_int "Dijo que eso ya lo sabía yo sola. Tenía razón, que es lo más incómodo de todo."

    ichika_int "El papel nuevo lo acepté sin pensar. Sigue en pie. Pero ahora sé que fue sin pensar."

    ichika_int "Tengo doce líneas de la obra de memoria. Salen solas. Las mías tardan un segundo entero."

    ichika_int "Vamos a repasarlas. Hoy quiero ver cuáles son mías."

    return

label e6_ichika_mono_tibia:

    ichika_int "Pregunta cuatro. Trenes. Salen las cuatro treinta y cinco."

    ichika_int "Me sale tan rápido que me da un poco de miedo. Cuando algo sale tan fácil, ¿es mío?"

    ichika_int "«Con más drama, entonces. ¿Qué tal un dragón?» Dijo eso. Y le seguí la broma."

    ichika_int "El dragón leía contratos de audición. Lo bauticé «Contrato». Mi mejor material."

    ichika_int "O mi mejor escondite. Hablamos diez minutos de un dragón. Los dos sabíamos de qué no."

    ichika_int "¿Me dejó escapar porque era amable, o porque no quiso mirar?"

    ichika_int "Si le sigo la broma, él se ríe y yo no tengo que explicar nada. Es cómodo."

    ichika_int "Es demasiado cómodo. Hay una frase que lleva días esperando. «No tengo que po—"

    ichika_int "¡Siguiente pregunta!"

    return

label e6_ichika_mono_fria:

    ichika_int "Pregunta cuatro. Trenes. Cuatro treinta y cinco."

    ichika_int "«Si tienes tiempo para esto, tienes tiempo para estudiar.» Eso dijo."

    ichika_int "Tenía razón. Contesté «tienes razón», con la sonrisa en su sitio. Salió perfecto."

    ichika_int "Tan perfecto que no me lo creí ni yo."

    ichika_int "Aprovechar el tiempo. Resolver, revisar, entregar. En un examen no hay chiste."

    ichika_int "Nadie va a ver nada. Eso se me da bien."

    ichika_int "Estoy bien. Que conste."

    return

label e6_ichika_mono_no_visitada:

    ichika_int "Pregunta cuatro. Trenes. Cuatro treinta y cinco. Sale sola."

    ichika_int "Ensayé tres formas de recibirlo, si venía. La graciosa. La dramática. La de «qué sorpresa»."

    ichika_int "No vino. Las ensayé igual, delante del espejo del club."

    ichika_int "(Entra Ichika. Se detiene. Sonríe. Aquí iría el chiste.)"

    ichika_int "Eran tres. Ninguna era mía. No sé si tengo una cuarta."

    ichika_int "Si no sé qué hacer, actúo. …Siempre."

    return


label e6_ichika_mj:

    play music ichika fadein 1.0 fadeout 1.5

    call mj_ejecutar(E6_MJ_JUEGO["ichika"], "ichika")
    $ e6_res = _return

    stop music fadeout 3.0

    narrador "Ichika levantó la vista del papel. No tenía ninguna expresión puesta."

    ichika_int "No tengo que poder con todo."

    ichika_int "Lo repetí una vez más, por dentro, a ver si se me quedaba. Se quedó."

    ichika_int "Sonreí. La sonrisa llegó medio segundo tarde. Esta vez dejé que llegara."

    ichika_int "Pregunta cinco. Antes de contestar, respiro."

    if e6_res == "saltado":

        narrador "Hay ensayos que se hacen por dentro, sin público. Este lo hizo entero."

    return


label e6_ichika_promesa:

    mc_pensamiento "Ensayó tres formas de recibirme. La graciosa, la dramática, la de «qué sorpresa»."

    mc_pensamiento "Y dijo que no sabía si podría con otra cosa. Yo tampoco supe qué contestarle."

    mc_pensamiento "Voy a ir a verla ensayar. Sin que tenga que prepararme ninguna de las tres caras."

    return


label e6_ichika_gesto_calida:

    narrador "Ichika resolvió la cuatro en lo que tarda en cerrarse una puerta."

    narrador "Después se quedó mirando el resultado, como si se lo hubiera regalado otra persona."

    mc_pensamiento "Ojos abiertos. El guion en el bolsillo, sin tocar. Ni una vez miró el reloj con miedo."

    mc_pensamiento "Hoy no necesitaba hacer de nadie."

    play sound audio.sfx_timbre volume 1.5

    stop music fadeout 1.0

    return

label e6_ichika_gesto_tibia:

    narrador "Resolvió la cuatro rápido y se quedó sonriéndole a su hoja."

    profe "Nakano. Está sonriendo."

    ichika "Es una técnica, profesor."

    narrador "Nadie se rió. Ella tampoco. La sonrisa se le fue a mitad del problema siguiente."

    mc_pensamiento "Un chiste justo antes de que se le escapara algo. Otra vez."

    play sound audio.sfx_timbre volume 1.5

    return

label e6_ichika_gesto_fria:

    narrador "Resolvió sin una pausa, sin un tachón, sin una mirada a nadie."

    narrador "La sonrisa estaba en su cara desde que empezó, igual de quieta que el reloj de la pared."

    mc_pensamiento "Una hoja perfecta y una sonrisa perfecta. Eso era lo que se veía."

    mc_pensamiento "Contesta como se contesta cuando alguien tiene razón: rápido y sin adornos."

    play sound audio.sfx_timbre volume 1.5

    return

label e6_ichika_gesto_no_visitada:

    narrador "Resolvía con una mano. Con la otra, bajo el pupitre, movía el guion doblado."

    narrador "Una pregunta, una línea. Una línea, una pregunta. Las dos cosas a medias, y las dos bien."

    mc_pensamiento "Eso no es hacer dos cosas. Es no soltar ninguna."

    mc_pensamiento "Con ella el cansancio nunca se nota en lo que hace. Se nota en que no para."

    play sound audio.sfx_timbre volume 1.5

    return


## --- Ecos de Ichika (Mov. 8) ----------------------------------------------------------
label e6_ichika_eco_calida:

    narrador "Ichika salió con el guion cerrado bajo el brazo y la cara recién lavada."

    call e6_foco("ichika", "neutral")

    ichika "Anoche dormí once horas. Esta vez no redondeé."

    ichika "Pensé antes de decir que sí a algo. Una sola vez. Me pareció una cosa nueva."

    call e6_foco("ichika", "sonriendo")

    narrador "La sonrisa le llegó medio segundo tarde. Esta vez la dejó llegar."

    call e6_foco("", "")

    return

label e6_ichika_eco_tibia:

    narrador "Ichika salió contando algo del dragón «Contrato», que ahora también leía exámenes."

    call e6_foco("ichika", "sonriendo")

    ichika "¡Pidió prórroga! ¡Los dragones siempre piden prórroga!"

    narrador "Se rió sola. Se calló un segundo de más."

    call e6_foco("ichika", "neutral")

    ichika "Era un chiste. …Era un chiste, ¿verdad?"

    mc "Era un chiste."

    ichika "Eso pensaba yo."

    call e6_foco("", "")

    return

label e6_ichika_eco_fria:

    narrador "Ichika salió a la hora exacta, con la sonrisa puesta, como todo lo demás."

    call e6_foco("ichika", "sonriendo")

    ichika "¿Todo bien? Yo estoy bien. Que conste."

    mc "No te lo había preguntado."

    call e6_foco("ichika", "neutral")

    ichika "Ya. Lo dije por si acaso."

    call e6_foco("", "")

    return

label e6_ichika_eco_no_visitada:

    narrador "Ichika salió probándose una expresión. Se la quitó. Se puso otra."

    call e6_foco("ichika", "neutral")

    ichika "Ensayé cómo salir y no me sale ninguna."

    ichika "Tengo la graciosa, la dramática y la de «qué sorpresa». La cuarta todavía no existe."

    mc "No tiene que existir hoy."

    call e6_foco("ichika", "sonriendo")

    ichika "¡Qué amable! …Esa fue la graciosa. Perdona el reflejo."

    call e6_foco("", "")

    return

################################################################################
##  EVENTO 6 · PARTE B (Chat 9)
##  Bloques de Nino (Mov. 4), Itsuki (Mov. 5) y Miku (Mov. 6), con sus capas
##  (N núcleo · M monólogo · J minijuego · P promesa · G gesto · E eco del Mov. 8)
##  y la capa de beat de Nino (nino_rama_beat) e Itsuki (azotea).
##
##  ESTA SECCIÓN SUSTITUYE los stubs «NINO», «ITSUKI» y «MIKU» de
##  game/02_cap1_evento6.rpy (todo lo que hay entre la cabecera
##  «## ===== NINO» y la cabecera «## ===== CAPÍTULO 2», sin incluirla).
##  La declaración de los CG (cg_nino_examen, cg_itsuki_examen, cg_miku_examen)
##  ya vive en 12_e6_pantallas.rpy: aquí no se vuelve a declarar.
##
##  Cableado: los minijuegos salen de E6_MJ_JUEGO (10_minijuegos.rpy). Sin puntos
##  (P-09: los puntos solo se suman en los hubs). Textos de los guiones
##  CAP1_evento_6_bloques_B.md (Nino, Itsuki) y _bloques_A.md (Miku).
################################################################################
## ============================== NINO ===========================================
##  Mov. 4 · Miércoles · Inglés

label e6_nino_nucleo:

    $ ui_escena("beat", "nino", "Aula · Inglés")
    $ tiempo_restante = "tres exámenes"
    $ e6_limpiar()

    scene bg_negro
    with fade_dia

    narrador "Miércoles. Inglés."

    play sound audio.sfx_hoja volume 2.0

    scene cg_nino_examen
    with fade

    narrador "Segunda fila. Mi hoja boca abajo antes de la mitad, y el lápiz encima."

    narrador "Nino leyó el texto de comprensión una sola vez, sin mover los labios."

    narrador "A media página se le movió la boca sola: una frase entera, sin voz. En inglés."

    mc_pensamiento "Pensaba en inglés, en un examen de inglés. Si se lo dijera, lo negaría."

    mc_pensamiento "Así que no se lo dije. Hay cosas que se cuidan mejor sin señalarlas."

    narrador "Su hoja avanzaba a la velocidad a la que otros copian su nombre."

    mc_pensamiento "A los quince minutos había terminado. Yo, tres antes. Ella lo sabía."

    return


## --- Capa de beat de Nino (se llama desde dentro de cada monólogo) ---------------

label e6_nino_beat_calida:

    nino_int "«¿Y quién junta los tuyos?» No contesté. La pregunta sigue en la cocina."

    nino_int "Le mandé cortar cebollas finas. Las cortó gruesas. Las usé igual."

    return

label e6_nino_beat_tibia:

    nino_int "Lavó mi taza sin que se lo pidiera. A mi taza no la toca nadie."

    nino_int "No le dije «quédate». Tampoco «vete». Los dos nos entendimos igual."

    return

label e6_nino_beat_fria:

    nino_int "Le dije que hablaba el mismo idioma que papá. Lo dije para que doliera."

    nino_int "No dolió. Asintió, como si ya lo hubiera oído. Eso fue peor."

    return


label e6_nino_mono_calida:

    play music descubrimiento fadein 2.0

    nino_int "Texto B. Pregunta nueve. Lo leo una vez. No hace falta más."

    nino_int "«Solo el tiempo lo va a demostrar.» Eso dijo, con cara de no estar prometiendo nada."

    nino_int "Y no prometió nada. Esa es la parte que no sé dónde poner."

    nino_int "Los otros prometían. Este no prometió y se quedó. Es una combinación rara."

    nino_int "Yo hablé de más y no se lo contó a nadie. Se lo pregunté a Yotsuba, que no guarda nada."

    nino_int "Yotsuba no sabía nada."

    nino_int "Eso no es confiar. Es llevar la cuenta. Es distinto."

    nino_int "Es distinto."

    call expression ("e6_nino_beat_" + nino_rama_beat)

    nino_int "Siempre veo venir el golpe. Me adelanto: me cierro antes, pido que se vayan antes."

    nino_int "Así nunca duele a tiempo. Duele por adelantado. Y duele siempre."

    nino_int "Hoy nadie me ha pegado. Y yo sigo con los brazos cruzados por dentro."

    nino_int "El chat sigue silenciado. Esta semana no me salí ni una vez. Nadie me lo pidió."

    nino_int "Hay cena, pase lo que pase con las notas. Cocino yo. Siempre cocino yo."

    nino_int "Cinco listas, una por cabeza. La mía la escribo la última, y es la más corta."

    nino_int "Y una sexta línea que todavía no sé cómo llenar. …Primero las cinco."

    return

label e6_nino_mono_tibia:

    nino_int "Texto B. Pregunta nueve. Lo leo una vez."

    nino_int "De los otros tutores perdí la cuenta. De este no. No sé por qué."

    nino_int "Cargó mi cesta sin que se lo pidiera. Pesaba. No dijo nada. Yo tampoco."

    nino_int "Dije «esto no significa nada». Lo dije yo, en voz alta, para que quedara dicho."

    call expression ("e6_nino_beat_" + nino_rama_beat)

    nino_int "¿Fue amable o fue método? Las dos cosas me cansan igual."

    nino_int "Si fue amable, no sé qué quiere. Si fue método, no sé hasta cuándo."

    nino_int "Mis hermanas ya no dicen «¿y si esta vez sí?». Lo dicen bajito, y lo oigo igual."

    nino_int "El chat sigue silenciado. Esta semana no me salí. No sé por qué no me salí."

    nino_int "Si aprobamos las cinco… quizás esta vez no—"

    nino_int "Revisa la ocho. Hay un «has» que debería ser «have»."

    nino_int "Ya terminé. Sigo en mi sitio. Hay que revisar."

    return

label e6_nino_mono_fria:

    nino_int "Texto B. Pregunta nueve. Lo leo una vez."

    nino_int "«Yo sí voy a durar.» Lo dijo como lo dijeron los otros. Casi palabra por palabra."

    nino_int "Le dije que se guardara la promesa. Prometió durar. Ha durado. Eso hay que reconocérselo."

    nino_int "No lo reconozco. Lo anoto. Son cosas distintas."

    call expression ("e6_nino_beat_" + nino_rama_beat)

    nino_int "Aún queda el resultado. Y tras el resultado, el siguiente. Siempre queda el siguiente."

    nino_int "Los que prometen se van rápido. Los que no prometen, más despacio. Todos se van."

    nino_int "Mis hermanas se ilusionan solas. Yo me ocupo de lo mío."

    nino_int "Lo mío es esto: revisar. Hoja por hoja, hasta la campana, por si acaso."

    nino_int "Sigo en el chat. No me salí. Es para vigilar lo que dicen de él. Nada más."

    nino_int "En la cabecera hay un renglón para la fecha. Lo llené al final, como siempre."

    nino_int "Anota la fecha. Es hoy."

    nino_int "Solo eso: una fecha."

    return

label e6_nino_mono_no_visitada:

    nino_int "Texto B. Pregunta nueve. Lo leo una vez."

    nino_int "Dije que no esperaba nada. Es cierto. Esa es la ventaja de no esperar."

    nino_int "Llevo treinta y dos días sin esperar nada. Y los llevo contados."

    call expression ("e6_nino_beat_" + nino_rama_beat)

    nino_int "Las que fue a ver llegaron distintas a casa. No le dije si mejor o peor. No pienso decirlo."

    nino_int "Alguien tiene que ser la que no cambia. Para que las demás tengan a dónde volver."

    nino_int "No vino a buscarme. Está bien. A mí no se me busca: se me encuentra en la cocina o no."

    nino_int "Me encontró en la cocina. Me oyó pedir que lo echaran. Y no se fue."

    nino_int "Eso queda en la columna de los datos sin conclusión."

    nino_int "El chat lo sigo leyendo. Alguien tiene que leerlo."

    nino_int "Alguien tiene que ver venir el golpe."

    nino_int "Sigo siendo yo."

    return


## --- Minijuego N1′ (solo cálida). Sin puntos: P-09 -------------------------------

label e6_nino_mj:

    play music nino fadein 1.0 fadeout 1.5

    call mj_ejecutar(E6_MJ_JUEGO["nino"], "nino")
    $ e6_res = _return

    stop music fadeout 3.0

    narrador "Nino dejó el lápiz sobre la mesa. No lo soltó: lo dejó. Hay una diferencia."

    if e6_res == "saltado":

        narrador "Hay compras que se hacen de memoria. Esta la hizo entera, de un tirón."

    if e6_sexto_valor() == "taza":

        nino_int "Escribí «una taza más». Se compra igual aunque nadie la pida. …No es por nadie."

    elif e6_sexto_valor() == "cuando":

        nino_int "Escribí «cuando se sepa». Se compra con el resultado en la mano, y no antes de saberlo."

    else:

        nino_int "Dejé la sexta línea en blanco. Sin tachar. Una línea en blanco no se pierde: se espera."

    nino_int "No pienso adelantar el golpe."

    nino_int "Si cae, cae. Pero no voy a ganarle la mano para que duela primero."

    nino_int "Esperar no es rendirse. Me costó treinta y dos días entenderlo."

    nino_int "Voy a entregar. Las demás terminarán a su ritmo. Esta vez no hago guardia."

    return


label e6_nino_promesa:

    mc_pensamiento "Dijo que alguien tiene que ser la que no cambia. Para que las demás tengan a dónde volver."

    mc_pensamiento "También dijo que ya me había visto en su casa más de lo que quería. Que eso contaba como visita."

    mc_pensamiento "Voy al centro comercial, al pasillo de importados. Y a cargar una cesta que no me haya pedido."

    return


label e6_nino_gesto_calida:

    narrador "Nino terminó, repasó la hoja una sola vez con el dedo y dejó el lápiz sobre la mesa."

    profe "Nakano. Si ya terminó, puede entregar."

    nino "Sí."

    play sound audio.sfx_silla volume 2.5

    narrador "Se levantó, dejó la hoja en la mesa del profesor y fue hacia la puerta sin mirar atrás."

    narrador "A las demás no les echó ni una mirada de guardia. Ni una."

    play sound audio.sfx_puerta_cierra volume 1.0

    mc_pensamiento "Quien ve venir el golpe se queda a esperarlo. Quien no lo adelanta, sale."

    mc_pensamiento "Se fue sin vigilarlas. Y nadie se cayó."

    play sound audio.sfx_timbre volume 1.5

    stop music fadeout 1.0

    return

label e6_nino_gesto_tibia:

    narrador "Nino terminó antes que casi todas. Soltó el lápiz. Giró la hoja boca abajo. Cruzó los brazos."

    profe "Nakano. Si ya terminó, puede entregar."

    nino "Aún no. Voy a revisar."

    narrador "Revisó cuarenta minutos, con el dedo, línea por línea. Y, de reojo, a las otras cuatro."

    mc_pensamiento "No había nada que revisar. Se quedaba por ellas. O por no estar a solas con lo que viene."

    mc_pensamiento "Quizás por las dos cosas. Ella no iba a decirme cuál."

    play sound audio.sfx_timbre volume 1.5

    return

label e6_nino_gesto_fria:

    narrador "Nino terminó. Soltó el lápiz sin ruido, giró la hoja boca abajo y cruzó los brazos, un poco más fuerte."

    profe "Nakano. Si ya terminó, puede entregar."

    nino "No."

    narrador "Se quedó revisando como quien patrulla una frontera. Sin mirar a nadie. A nadie."

    mc_pensamiento "Ni a mí, ni a ellas. Hace un mes me miraba para odiarme. Ahora ni eso."

    mc_pensamiento "Revisaba con el método de quien ya sabe cómo acaba y quiere llegar preparada."

    play sound audio.sfx_timbre volume 1.5

    return

label e6_nino_gesto_no_visitada:

    narrador "Nino terminó y repasó la hoja con el dedo. Soltó el lápiz. Giró la hoja. Cruzó los brazos."

    profe "Nakano. Si ya terminó, puede entregar."

    nino "Estoy revisando."

    narrador "Revisó cuarenta minutos. A la media hora levantó la vista y me miró una sola vez."

    mc_pensamiento "No con odio. Con la cara de quien comprueba que algo sigue donde lo dejó."

    mc_pensamiento "Seguía en mi asiento. Para ella, eso ya era una respuesta."

    play sound audio.sfx_timbre volume 1.5

    return


## --- Ecos de Nino (Mov. 8). Entra ya en pj, neutral (lo hace e6_cinco) -----------
label e6_nino_eco_calida:

    narrador "Nino llegó con el boletín doblado en cuatro y la barbilla en alto. Casi toda."

    call e6_foco("nino", "neutral")

    nino "El último duró cuatro días. Tú llevas treinta y cinco."

    mc "…"

    nino "No me mires así. Es aritmética."

    call e6_foco("nino", "pillada")

    nino "Y que no se entere Yotsuba de que llevaba la cuenta. Haría un cartel."

    call e6_foco("", "")

    return

label e6_nino_eco_tibia:

    narrador "Nino llegó con una bolsa del supermercado en cada mano, como si el boletín fuera lo de menos."

    call e6_foco("nino", "neutral")

    nino "Pesa. No te estoy pidiendo ayuda."

    mc "Entendido."

    nino "…Esta pesa más de lo que parece."

    narrador "Dejó la bolsa más pesada en mi brazo sin mirarme, y se llevó la otra. Ninguno dijo nada más."

    call e6_foco("", "")

    return

label e6_nino_eco_fria:

    narrador "Nino se detuvo a dos pasos de mí, con el boletín boca abajo contra el costado. Ni cerca ni lejos."

    call e6_foco("nino", "molesta")

    nino "Sigues aquí."

    mc "Sigo."

    nino "Pues anota la fecha. Para cuando te canses."

    narrador "Lo dijo sin rabia. Como quien deja una nota pegada en la nevera."

    call e6_foco("nino", "neutral")

    call e6_foco("", "")

    return

label e6_nino_eco_no_visitada:

    narrador "Nino se quedó junto al marco de la puerta, a media sala, como quien no ha decidido si entra."

    call e6_foco("nino", "neutral")

    nino "No me mires como si me debieras algo. No viniste a buscarme. Está bien."

    nino "Alguien tenía que ser la que no se busca. …Eso sonó mejor en mi cabeza."

    mc "Sonó bien."

    nino "No te pedí opinión de crítico. Treinta y cinco días no hacen una conversación."

    call e6_foco("", "")

    return


## ============================= ITSUKI ==========================================
##  Mov. 5 · Jueves · Ciencias

label e6_itsuki_nucleo:

    $ ui_escena("beat", "itsuki", "Aula · Ciencias")
    $ tiempo_restante = "dos exámenes"
    $ e6_limpiar()

    scene bg_negro
    with fade_dia

    narrador "Jueves. Ciencias."

    play sound audio.sfx_hoja volume 2.0

    scene cg_itsuki_examen
    with fade

    narrador "Segunda fila. Mi hoja boca abajo, el lápiz encima. Ya era costumbre."

    narrador "Itsuki escribía con la derecha. El índice de la izquierda recorría los renglones sin tocarlos."

    narrador "Llevaba tres líneas bien. La cuarta la leyó una vez, y otra, y otra."

    mc_pensamiento "Una conversión de unidades. De las que se resuelven con orden y sin prisa."

    mc_pensamiento "Ella tiene el orden. A veces le falta mirar un paso atrás."

    mc_pensamiento "Conozco el tipo de trampa. No podía decírsela: en un examen no se habla."

    return


## --- Capa de beat de Itsuki: eco de la azotea -------------------------------------
##  ayudada = hub visitado y rama no tibia (cálida o fría) · sola = el resto.

label e6_itsuki_beat_ayudada:

    itsuki_int "«No hace falta que sigas viniendo a comprobar cómo voy.» Lo dije yo. Vino igual."

    itsuki_int "Pasamos la hora sin abrir ningún libro. Fue la hora más útil del mes. No pienso decirlo."

    return

label e6_itsuki_beat_sola:

    itsuki_int "En la azotea no le pregunté dónde había estado. Él no me lo contó. Fue un buen acuerdo."

    itsuki_int "Pasamos la hora sin abrir ningún libro. Fue la hora más útil del mes. No pienso decirlo."

    return


label e6_itsuki_mono_calida:

    play music descubrimiento fadein 2.0

    itsuki_int "Pregunta cuatro. Conversión de unidades. Cinco pasos."

    itsuki_int "Planteé bien. Convertí el caudal. Pasé al tiempo. Y el resultado no cuadra."

    itsuki_int "Es el mismo error de siempre: en un sitio que no encuentro, con un número que reconozco."

    call e6_itsuki_beat_ayudada

    itsuki_int "Me dijo: «Solo te digo dónde mirar». No me dio la respuesta. Me dio una dirección."

    itsuki_int "El primer día le dije: «Ni se te ocurra decirme la respuesta». Era una regla para él."

    itsuki_int "Lo hice sola una vez. Salió. Eso ya lo sé. Lo que no sé es qué hago cuando no sale."

    itsuki_int "Preguntarle a mis hermanas sería admitir…"

    itsuki_int "Preguntarle a él sería—"

    itsuki_int "Basta."

    itsuki_int "El profesor no es ninguna de las dos cosas. Es el profesor."

    itsuki_int "Levantar la mano no es un favor. Es un procedimiento."

    itsuki_int "Tengo dos caminos, y los dos son legales. Elegiré después de revisar una vez."

    return

label e6_itsuki_mono_tibia:

    itsuki_int "Pregunta cuatro. Conversión de unidades. Cinco pasos."

    itsuki_int "Planteé bien. Convertí el caudal. Pasé al tiempo. Y el resultado no cuadra."

    itsuki_int "Hay un error. No sé dónde. Lo noto como una piedra en el zapato."

    call e6_itsuki_beat_sola

    itsuki_int "Me ofreció revisarlo desde el principio. Dije que no antes de saber qué iba a explicarme."

    itsuki_int "Todavía no sé qué iba a explicarme. Quizá un paso. Quizá otra cosa."

    itsuki_int "Dije «todavía no necesito tu ayuda». Era una expresión. No era una promesa."

    itsuki_int "…¿O sí lo era?"

    itsuki_int "Podría levantar la mano. Preguntarle al profesor. Preguntar sería—"

    itsuki_int "Revisaré desde el principio. Sola."

    return

label e6_itsuki_mono_fria:

    itsuki_int "Pregunta cuatro. Conversión de unidades. Cinco pasos."

    itsuki_int "Planteé bien. Convertí el caudal. Pasé al tiempo. Y el resultado no cuadra."

    itsuki_int "Revisaré cada paso, uno por uno, desde el primero. Sin ayuda."

    call e6_itsuki_beat_ayudada

    itsuki_int "Me quitó el cuaderno de las manos. Lo resolvió de pie, con mi propio lápiz."

    itsuki_int "Bien y rápido. No era el ejercicio lo que defendía. Era hacerlo."

    itsuki_int "Taché su solución y escribí la mía debajo. Le dije que ya tenía lo que necesitaba de él."

    itsuki_int "Lo mantengo."

    itsuki_int "Resolver sola cuesta el triple. Entrego sobre la campana. No importa."

    itsuki_int "Nadie va a decirme dónde mirar. Nadie va a decirme nada."

    itsuki_int "No necesito preguntar."

    return

label e6_itsuki_mono_no_visitada:

    itsuki_int "Pregunta cuatro. Conversión de unidades. Cinco pasos."

    itsuki_int "Es del mismo tipo que el del círculo a lápiz. Reconozco la forma antes de leer los números."

    itsuki_int "Planteé bien. Convertí el caudal. Pasé al tiempo. Y el resultado no cuadra."

    call e6_itsuki_beat_sola

    itsuki_int "Repasé aquel ejercicio hasta hundir el papel. Y me atasco en el mismo punto."

    itsuki_int "Dije que gané el juego. Una victoria que no vino a cobrar nadie."

    itsuki_int "Pedirlo habría sido…"

    itsuki_int "No. Termino la oración. Pedirlo habría sido empezar. Y no sé dónde se para uno después."

    itsuki_int "Si hubiera venido, no lo habría echado. No inmediatamente. Tampoco eso lo apunto."

    itsuki_int "Lo resuelvo sola. Como siempre."

    itsuki_int "…Tarde, pero sola."

    return

## --- Minijuego It1 (solo cálida). Frase A/B según it1_frase() --------------------

label e6_itsuki_mj:

    play music itsuki fadein 1.0 fadeout 1.5

    call mj_ejecutar(E6_MJ_JUEGO["itsuki"], "itsuki")
    $ e6_res = _return

    stop music fadeout 3.0

    if e6_res == "saltado":

        narrador "No supe si levantó la mano o la dejó abajo. Cuando volví a mirar, la cuatro estaba resuelta."

        itsuki_int "Preguntar no es perder."

    elif it1_frase() == "A":

        narrador "Levantó la mano. Despacio, con el codo recto, como se levanta algo que pesa."

        profe "¿Sí, Nakano?"

        itsuki "¿Podría repetir el enunciado de la cuatro? Entero."

        profe "Cómo no. «…durante una hora y media de funcionamiento continuo…»"

        narrador "Itsuki no esperó a que terminara. Ya había bajado la vista a su hoja."

        itsuki_int "Hora y media. Cinco mil cuatrocientos segundos. No noventa."

        itsuki_int "Preguntar no es perder."

        itsuki_int "Me dijo dónde mirar. El ejercicio lo resolví yo. Sigue siendo mío."

    else:

        narrador "No levantó la mano. Borró el «90» entero, con la goma, sin prisa."

        narrador "Y empezó otra vez desde la primera línea. Despacio. Sin saltarse ninguna unidad."

        itsuki_int "Una hora y media. Noventa minutos. Cinco mil cuatrocientos segundos. Ahora sí."

        itsuki_int "Me salió sola. Y tardé el doble. Las dos cosas son ciertas."

        itsuki_int "La próxima vez preguntaré."

    return


label e6_itsuki_promesa:

    mc_pensamiento "Subió a la azotea con un cuaderno y no lo abrió. Yo estaba ahí."

    mc_pensamiento "Dijo que si hubiera ido a buscarla no me habría echado. No inmediatamente. Y que no lo apuntara."

    mc_pensamiento "No lo apunté. Pero voy a subir con comida para dos, y a pedirle que suba ella sin el cuaderno. Una vez."

    return


label e6_itsuki_gesto_calida:

    narrador "Entregó con cuatro minutos de sobra. La cuarta tenía una sola raya, prolija."

    narrador "Al pasar junto a mi pupitre me miró un segundo. Esta vez no apartó la vista."

    narrador "Asintió una vez, seca, como quien confirma un dato y no pide aplauso."

    mc_pensamiento "Hace un mes apartar la mirada era su forma de no deberme nada. Hoy mirar era no ocultar nada."

    mc_pensamiento "No necesitó que yo le dijera dónde mirar. Ya sabía dónde. Y a quién preguntar, si hacía falta."

    play sound audio.sfx_timbre volume 1.5

    stop music fadeout 1.0

    return

label e6_itsuki_gesto_tibia:

    narrador "Entregó sobre la campana, con la cuarta tachada y reescrita dos veces."

    narrador "A media hoja había levantado la vista. Me miró un segundo. Apartó la mirada y volvió al papel."

    mc_pensamiento "Pudo preguntar. Eligió tardar. Con ella, tardar también es una forma de orgullo."

    mc_pensamiento "Revisó desde el principio, sola. Apretaba el lápiz no por rabia, sino por método."

    play sound audio.sfx_timbre volume 1.5

    return

label e6_itsuki_gesto_fria:

    narrador "Entregó sobre la campana. La hoja, impecable. Ni una pregunta, ni una mirada."

    narrador "Al terminar cerró el cuadernillo del examen con las dos manos, como cierra su cuaderno."

    mc_pensamiento "No levantó la vista ni una vez. Ni para odiarme."

    mc_pensamiento "Resolvió sola. Es lo único que no iba a dejar que nadie le quitara. Esta vez nadie lo intentó."

    play sound audio.sfx_timbre volume 1.5

    return

label e6_itsuki_gesto_no_visitada:

    narrador "Entregó pasada la campana, con la cuarta recién resuelta. Tarde, pero resuelta."

    narrador "A media hoja había levantado la vista. Me miró un segundo, y apartó la mirada."

    mc_pensamiento "La miré yo primero. Ella apartó la vista, como si hubiera algo que no estaba lista para devolverme."

    mc_pensamiento "Nunca me pidió nada. Y yo nunca fui. Los dos dejamos la misma pregunta sin hacer."

    play sound audio.sfx_timbre volume 1.5

    return


## --- Ecos de Itsuki (Mov. 8). Terminan antes del intento de disculpa ---------------

label e6_itsuki_eco_calida:

    narrador "Itsuki llegó con el bolígrafo del examen todavía en la mano. Se le había olvidado soltarlo."

    call e6_foco("itsuki", "neutral")

    itsuki "Dije que el juego se acabó. No dije quién ganó."

    mc "¿Y quién ganó?"

    itsuki "Eso no se pregunta."

    if it1_frase() == "A":

        itsuki "Levanté la mano en un examen. Es un informe, no una invitación a aplaudir."

    else:

        itsuki "No levanté la mano. Pero ya sé que puedo. Es un informe, no una invitación a aplaudir."

    call e6_foco("", "")

    return

label e6_itsuki_eco_tibia:

    narrador "Itsuki llegó con el boletín doblado por la mitad y el gesto de quien ya revisó dos veces."

    call e6_foco("itsuki", "neutral")

    itsuki "Aquel día dijiste «revisarlo desde el principio». …¿Qué ibas a—"

    narrador "Se detuvo. La oración se quedó abierta, sin sujeto. En ella, eso es casi un grito."

    mc "Cuando quieras."

    itsuki "…No dije que quisiera."

    call e6_foco("", "")

    return

label e6_itsuki_eco_fria:

    narrador "Itsuki llegó con el boletín en una mano y el puño cerrado sobre el bolígrafo del examen."

    call e6_foco("itsuki", "molesta")

    itsuki "Revisé desde el principio. Sola. Sale igual que si me lo hubieran resuelto. La diferencia es mía."

    mc "Lo sé."

    itsuki "No tienes que saberlo. …Es solo que cuenta."

    call e6_foco("itsuki", "neutral")

    call e6_foco("", "")

    return

label e6_itsuki_eco_no_visitada:

    narrador "Itsuki esperaba de pie junto a su sitio, con el cuaderno de ciencias cerrado bajo la mano."

    call e6_foco("itsuki", "neutral")

    itsuki "Dije que el juego se acabó, y gané. Es lo único que siempre me sale bien."

    mc "No sabía que había premio."

    itsuki "No lo hay. …Por eso es lo único que me sale."

    narrador "Lo dijo con la oración cerrada, con su punto. Pero el punto quedó flojo."

    call e6_foco("", "")

    return


## ============================== MIKU ===========================================
##  Mov. 6 · Viernes · Sociales (el clímax)

label e6_miku_nucleo:

    $ ui_escena("beat", "miku", "Aula · Sociales")
    $ tiempo_restante = "un examen"
    $ e6_limpiar()

    scene bg_negro
    with fade_dia

    narrador "Viernes. El último día, y el último examen. Sociales."

    play sound audio.sfx_hoja volume 2.0

    scene cg_miku_examen
    with fade

    narrador "Segunda fila, mi hoja boca abajo. A este examen lo dejé más despacio. Quería quedarme a mirar."

    narrador "Miku tenía el lápiz en la mano derecha y, junto al lápiz, la goma. Entera. Con las cuatro esquinas."

    mc_pensamiento "En su hoja del segundo día, la goma había trabajado más que el lápiz."

    narrador "Los audífonos colgaban de su cuello, apagados."

    mc_pensamiento "La pregunta tres no decía «sal». Decía «rutas de comercio»."

    mc_pensamiento "Lo que escribiera de más sería ella. Lo que no escribiera, también."

    return


label e6_miku_mono_calida:

    play music descubrimiento fadein 2.0

    miku_int "…Pregunta tres. Rutas de comercio y sostén de una provincia sin costa."

    miku_int "…Sal."

    miku_int "…Me preguntó cuánto tardaba la sal en llegar. Diez días. Doce si llovía."

    miku_int "…Contesté sin pensar. Iba a pedir perdón. No me dejó. Dijo que eso no se disculpa."

    miku_int "…Estaba contestando una pregunta que me hizo él. Todavía no sé si le creo."

    miku_int "…Dijo que no me faltaba la materia. Que me faltaba creer que lo que sé cuenta como saber."

    miku_int "…Dijo que lo iba a comprobar. Hoy es el día. Esta pregunta es lo que sé, y el examen la pide."

    miku_int "…Hablar cuesta. Escribir también, si es de algo que quiero. Cuesta igual."

    miku_int "…Tengo una canción en la cabeza. Es la que pongo para que nadie se acerque."

    miku_int "…Voy a escribir con ella. Primero con la mía. Cuando se apague, queda el reloj del aula."

    miku_int "…El reloj nunca ha pedido perdón. …Vamos."

    return

label e6_miku_mono_tibia:

    miku_int "…Pregunta tres. Rutas de comercio y sostén de una provincia sin costa."

    miku_int "…Dijo que se me daba bien. Yo dije que solo lo había leído."

    miku_int "…Dijo que era más de lo que había hecho nadie en mi casa."

    miku_int "…Era un elogio con una comparación dentro. …¿Me lo dijo a mí o me puso al lado de las demás?"

    miku_int "…Mis hermanas también leen. …No tanto, pero leen."

    miku_int "…La sal entra por las rutas. Podría contarla."

    miku_int "…Si la cuento y no suma, me habré pasado de hablar."

    miku_int "…Si no la cuento, nadie va a saber que la sé."

    miku_int "…Lo que amo no—"

    miku_int "…Pregunta cuatro."

    return

label e6_miku_mono_fria:

    miku_int "…Pregunta tres. Rutas de comercio y sostén de una provincia sin costa."

    miku_int "…Dijo que el Sengoku no entra en el examen. Tres temas, y ninguno pregunta por la sal."

    miku_int "…Tenía razón. La pregunta es de comercio."

    miku_int "…Cuatro renglones del libro de texto: rutas, mercados, impuestos. Está todo."

    miku_int "…Escribo eso. Lo que me van a preguntar."

    miku_int "…La otra respuesta también la sé. Entera."

    miku_int "…Hoy no."

    return

label e6_miku_mono_no_visitada:

    miku_int "…Pregunta tres. Rutas de comercio y sostén de una provincia sin costa."

    miku_int "…Sal. La respuesta empezó a escribirse sola. Ya llevo cuatro renglones."

    miku_int "…No debería. Es un examen. …Borro."

    miku_int "…Hay una silla enfrente de la mía. Siempre está vacía."

    miku_int "…Dejé el libro abierto en la misma página dos días. Por si hacía falta una excusa."

    miku_int "…Nadie se sentó. No pasa nada."

    miku_int "…Soy buena esperando."

    miku_int "…Escribo tres líneas de rutas. La sal, otro día."

    miku_int "…Perdón. Eso sonó triste. No era la idea."

    return


## --- Minijuego M3 (solo cálida). Su tema SOLO suena aquí, y lo arranca M3 --------
label e6_miku_mj:

    call mj_ejecutar(E6_MJ_JUEGO["miku"], "miku")
    $ e6_res = _return

    ## M3 corta su tema al terminar. Si se saltó, aún suena descubrimiento.
    stop music fadeout 3.0

    narrador "Se quitó los audífonos del cuello, despacio. Los plegó y los dejó en el pupitre, junto a la goma."

    miku_int "Alguien se la vendió. Y eso me parece mucho más importante que la leyenda."

    miku_int "Dejaré de tener miedo a lo que más amo."

    miku_int "Esperé el perdón. Es lo que viene después. No llegó."

    narrador "Escribía sin levantar la cabeza. Sin detenerse al final de cada línea. Sin borrar."

    if e6_res == "saltado":

        narrador "Hay respuestas que se escriben solas. Esta lo hizo de una vez, de principio a fin."

    return


label e6_miku_promesa:

    mc_pensamiento "Hay una silla enfrente de la suya. Siempre vacía."

    mc_pensamiento "Dejó un libro abierto dos días por si alguien hacía falta de excusa."

    mc_pensamiento "Voy a sentarme en esa silla. Y a leer lo mismo que ella, aunque no entienda nada."

    return


label e6_miku_gesto_calida:

    narrador "Cuando sonó el timbre, su hoja estaba llena hasta el último renglón. Sin un solo borrón."

    mc_pensamiento "La goma seguía siendo una goma. Hace un mes eso habría sido una noticia."

    narrador "No recogió los audífonos enseguida. Los miró un segundo, como quien comprueba que no se mueven solos."

    mc_pensamiento "Plegados, no puestos. Como se dejan las llaves en la entrada."

    narrador "Al final los recogió. Se los colgó al cuello. Sin subírselos."

    play sound audio.sfx_timbre volume 1.5

    return

label e6_miku_gesto_tibia:

    narrador "Escribió la respuesta de rutas sin una sola mención a la sal."

    narrador "Cada vez que se acercaba a una frase larga, el cuadernillo le subía un poco más."

    mc_pensamiento "Sabía cómo seguir. Se le veía en el lápiz, que dudaba justo antes de cada coma."

    mc_pensamiento "No borró. Se detuvo. Es una forma de borrar que no deja goma."

    play sound audio.sfx_timbre volume 1.5

    return

label e6_miku_gesto_fria:

    narrador "Escribió firme, sin dudas, cuatro renglones exactos."

    narrador "Hacia la mitad, la mano libre subió hasta los audífonos. Y se quedó ahí hasta el timbre."

    mc_pensamiento "No se los puso. No los soltó. Era una respuesta correcta y me dolió mirarla."

    mc_pensamiento "Tenía la razón de su lado. Esa fue otra forma de no ganar."

    play sound audio.sfx_timbre volume 1.5

    return

label e6_miku_gesto_no_visitada:

    narrador "Escribió largo. Se detuvo a mitad de un renglón. Pasó la goma una sola vez, con cuidado."

    narrador "La goma perdió un borde. No quedó en tocón."

    mc_pensamiento "Desde la segunda fila no pude leer lo que borró. Pude ver cuánto ocupaba."

    mc_pensamiento "Lo dejó en tres líneas. Las de quien no quiere molestar."

    play sound audio.sfx_timbre volume 1.5

    return

## --- Ecos de Miku (Mov. 8) --------------------------------------------------------

label e6_miku_eco_calida:

    narrador "Miku llegó con los audífonos al cuello, sin tocarlos, y el boletín en las dos manos."

    call e6_foco("miku", "neutral")

    miku "La página ciento veinte. ¿Llegaste?"

    mc "Ciento veintidós."

    ## Sprite condicional «miku sonrie»; si no existe, vale «relajada».
    $ e6_miku_sonrisa = "relajada"

    if renpy.has_image("miku sonrie"):

        $ e6_miku_sonrisa = "sonrie"

    call e6_foco("miku", e6_miku_sonrisa)

    narrador "Se rió. Una sola nota, corta, como un acorde."

    miku "Quería ver tu cara. Ya la vi."

    call e6_foco("", "")

    return

label e6_miku_eco_tibia:

    narrador "Miku tomó su boletín con el cuadernillo de preguntas todavía doblado bajo el brazo."

    call e6_foco("miku", "neutral")

    miku "…Dijiste que se me daba bien."

    miku "…Todavía estoy pensando qué querías decir con eso."

    mc "Lo que dije."

    miku "…Puede ser. …Lo sigo pensando."

    call e6_foco("", "")

    return

label e6_miku_eco_fria:

    narrador "Miku llegó con los audífonos puestos. Esta vez sonaban: se oían desde la puerta."

    call e6_foco("miku", "neutral")

    miku "…Contesté lo que entraba. …Estuvo bien."

    miku "…Hoy no."

    narrador "No dijo a qué. No hizo falta."

    call e6_foco("", "")

    return

label e6_miku_eco_no_visitada:

    narrador "Miku se detuvo en la puerta con el boletín contra el pecho, como se lleva un libro."

    call e6_foco("miku", "neutral")

    miku "…La silla sigue vacía. …No es un reproche. …Es información."

    mc "Lo sé."

    miku "…Dejé el libro abierto otra vez. …Por si acaso."

    call e6_foco("", "")

    return


## ============================= CAPÍTULO 2 ======================================
## Stub de salida. BORRAR cuando exista 03_capitulo2.rpy (label duplicado).
label cap2_inicio:
    narrador "[[STUB cap2_inicio · Capítulo 2 pendiente]"
    return