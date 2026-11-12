################################################################################
##  02_cap1_evento6.rpy — EVENTO 6 · SEMANA DE EXÁMENES (cierre del Capítulo 1)
##  Orden del archivo = orden en que lo vive el jugador:
##    Mov. 1  Lunes (aula)                     Mov. 7  Después del examen
##    Mov. 2  Yotsuba · japonés                Mov. 8  Resultados y Maruo
##    Mov. 3  Ichika · matemáticas             Mov. 9  Las cinco (ecos, intento, mesa)
##    Mov. 4  Nino · inglés                    Mov. 10 Casa
##    Mov. 5  Itsuki · ciencias                Mov. 11 Cuarto, chat y libreta
##    Mov. 6  Miku · sociales                  Mov. 12 El retrato (epílogo)
##  Regla: cada movimiento es un label de nivel superior que termina en return.
##  Sus variantes (_calida, _tibia, _fria, _no_visitada, _superado, _mixto,
##  _bueno) van justo debajo, también de nivel superior y con su propio return.
##  Ningún label va dentro de otro: tras un `call`, Ren'Py sigue en la línea
##  siguiente, y un label incrustado ahí se ejecutaría y cortaría la escena.
##  Ayudas y estado: 10_minijuegos.rpy · Pantallas: 12_e6_pantallas.rpy
##  Pruebas: 11_e6_debug.rpy
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
default e6_domingo = ""
default e6_domingo_hermana = ""
default persistent.cap1_completado = False

image cg_cinco_aula  = "cg/cap1_mov6/cinco_aula.webp"

image cg_cinco_aprobadas = "cg/cap1_mov6/cinco_aprobadas.webp"

image cg_yotsuba_examen = "cg/cap1_mov6/yotsuba_examen.webp"

image cg_ichika_examen = "cg/cap1_mov6/ichika_examen.webp"

image cg_nino_examen = "cg/cap1_mov6/nino_examen.webp"

image cg_itsuki_examen = "cg/cap1_mov6/itsuki_examen.webp"

image cg_miku_examen = "cg/cap1_mov6/miku_examen.webp"

## Fondo derivado (Transform), no es un asset nuevo.
image bg_escuela_atardecer = Transform(
    "bg/escuela.webp",
    matrixcolor = BrightnessMatrix(-0.04) * SaturationMatrix(0.92) * TintMatrix("#ffdcb8")
)

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
    call e6_despues
    call e6_resultados
    call e6_cinco
    call e6_casa
    call e6_cuarto
    call e6_retrato

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

    mc_pensamiento "Como dijo Miku, son cinco materias y ellas son cinco."

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

    narrador "Cada una."

    mc_pensamiento "Supongo que esperan una frase motivacional por parte mía."

    mc_pensamiento "Nunca he sido bueno en eso, pero…"

    mc "¡Hola chicas! ¿Preparadas para los exámenes?"

    mc "Sé que todas tienen dudas o miedos sobre si aprobarán o no."

    mc "Pero recuerden todo este mes que hemos estudiado."

    mc "¡Todos nosotros dimos nuestro mejor esfuerzo!"

    mc "¡Y ese esfuerzo lo demostraremos toda esta semana!"

    mc "¡Así que sé que lo lograrán! ¡Lo lograremos!"

    mc "¡Aprobarán los exámenes!"

    mc "¡Confío plenamente en ustedes!"

    mc "¡Sin excepción!"

    mc_pensamiento "Fue una de las mejores frases de aliento que he lanzado en mi vida."

    mc_pensamiento "Di lo mejor de mí."

    mc_pensamiento "Y ellas escucharon lo que dije… Escuché lo que dije."

    narrador "Cada una reaccionó de distinta manera."

    narrador "Y me confesaron todo."

    ## --- Confesiones. Orden fijo: Yotsuba, Ichika, Miku, Itsuki, Nino ------------
    scene bg_aula
    with dissolve

    call e6_formacion_neutral

    ## Yotsuba
    if e6_estado_de("yotsuba") == "calida" or e6_estado_de("yotsuba") == "tibia":

        call e6_foco("yotsuba", "sonriendo")

        yotsuba "¡Estudié las lecturas dos veces!"

        yotsuba "Y todavía recuerdo qué sentía cada personaje."

        yotsuba "Esta vez no las dejé para después. Las calenté primero."

        yotsuba "Como antes de una carrera: si no calientas, el cuerpo se queja a mitad de camino."

        yotsuba "Después les tomé las fechas a Miku y las fórmulas a Ichika."

        yotsuba "Así que no te preocupes por mí, [mc]."

        yotsuba "¡Voy a llegar a la meta, y las cinco juntas!"

    elif e6_estado_de("yotsuba") == "fria":

        call e6_foco("yotsuba", "sonriendo")

        yotsuba "¡Estudié las lecturas dos veces!"

        yotsuba "¡Y les tomé las fechas a Miku y las fórmulas a Ichika!"

        yotsuba "¡Hoy me concentro en lo mío! ¡Nada más!"

        narrador "Lo dijo de corrido, sin mirar a ninguna de sus hermanas."

    else:

        call e6_foco("yotsuba", "neutral")

        yotsuba "¡Repasé las fechas con Miku y las fórmulas con Ichika!"

        yotsuba "…Mis lecturas, para después. Siempre se quedan para después."

        yotsuba "Quería terminar a tiempo para que nadie se desmayara de los nervios."

        yotsuba "¡Tú incluido, [mc]!"

        yotsuba "¡Pero lo intentaré con toda la energía que me queda!"


    ## Ichika
    if e6_estado_de("ichika") == "calida":

        call e6_foco("ichika", "sonriendo")

        ichika "Dormí cuatro horas. Esta vez por las fórmulas, no por el papel de la obra."

        ichika "Yo, que me sé el guion entero. Las fórmulas, a medias. …Bueno, a tres cuartos."

        ichika "El guion va en el bolsillo, doblado, y de ahí no sale hasta el último timbre."

        ichika "Y si todo sale bien, tutor terco, me debes una tarde entera sin libros."

    elif e6_estado_de("ichika") == "tibia":

        call e6_foco("ichika", "sonriendo")

        ichika "¡Dormí cuatro horas! Mitad fórmulas, mitad guion."

        ichika "¡Equilibrio artístico!"

        ichika "El guion viene conmigo. Por si el examen pide drama."

        narrador "Lo dijo riéndose. No dijo si pensaba sacarlo."

    elif e6_estado_de("ichika") == "fria":

        call e6_foco("ichika", "sonriendo")

        ichika "Dormí lo justo y repasé lo justo. Todo cronometrado."

        ichika "Hoy me portaré muy bien. Que conste."

        narrador "La sonrisa, en su sitio. Los ojos, en la pizarra."

    else:

        call e6_foco("ichika", "neutral")

        ichika "Dormí cuatro horas. Con el guion en una mano y las fórmulas en la otra."

        ichika "Supongo que me distraje pensando en si de verdad lograríamos aprobarlo todo."

        ichika "Aunque… compañía alguna de esas tardes no me habría venido mal, ¿sabes?"

        ichika "Las hermanas mayores también necesitamos que nos echen una mano."

        ichika "¿No crees, [mc]?"

    ## Miku

    if e6_estado_de("miku") == "calida":

        call e6_foco("miku", "animada")

        miku "…Sé más de lo que van a preguntar. …Lo comprobé tres veces."

        miku "…Repasé las batallas, los clanes, las fechas."

        miku "…Hasta lo que no sale en el libro."

        miku "…La silla de enfrente ya no se siente vacía."

        miku "…Por si acaso, lo comprobaré una cuarta vez."

        miku "…Ya sé que es demasiado."

    elif e6_estado_de("miku") == "tibia":

        call e6_foco("miku", "neutral")

        miku "…Repasé las batallas, los clanes, las fechas."

        miku "…Todo, dos veces."

        miku "…Creo que lo sé."

        miku "…No me digas si se me da bien."

    elif e6_estado_de("miku") == "fria":

        call e6_foco("miku", "neutral")

        miku "…Estudié lo que entra. …Tres temas."

        miku "…Como me dijeron."

        miku "…El libro de la biblioteca lo devolví."

        miku "…Bueno. …Lo renové."

        miku "…No sé por qué."

    else:

        call e6_foco("miku", "neutral")

        miku "…Repasé sola, como siempre."

        miku "…Las batallas, los clanes, las fechas. …Todo, dos veces."

        miku "…Dejé libre la silla de enfrente. …Por costumbre."

        miku "…No esperaba a nadie. …Eso quiero pensar."


    ## Itsuki

    if e6_estado_de("itsuki") == "calida" or e6_estado_de("itsuki") == "fria":

        call e6_foco("itsuki", "sonriendo")

        itsuki "He estudiado cada noche. Y por primera vez sé lo que hago."

        itsuki "Ya sé por qué fallaba en las conversiones de unidades."

        itsuki "Tres veces el mismo error, y yo sin verlo."

        itsuki "Saberlo no impide que vuelva a pasar. Pero ya sé por dónde volver."

        itsuki "No me felicites todavía. Esto se demuestra en el examen, no antes."

    else:

        call e6_foco("itsuki", "neutral")

        itsuki "He estudiado cada noche. Si un problema no sale, lo repito hasta que salga."

        itsuki "Lo repito, lo reviso, lo repito otra vez. …Siempre llego a la misma cifra."

        itsuki "No pedí ayuda a nadie. Prefiero equivocarme sola que acertar con ayuda."

        itsuki "Dijiste «sin excepción». Me lo tomo en serio. Tú también deberías."


    ## Nino

    if e6_estado_de("nino") != "no_visitada":

        call e6_foco("nino", "pillada")

        nino "Treinta días. Y sigues viniendo. …No digo nada más."

        nino "Y no pongas esa cara. Yo no dije nada. Los números hablan solos."

        nino "Repasé inglés leyendo etiquetas en voz baja."

        nino "…Si me viste mover los labios en el súper, no viste nada."

        nino "Y la próxima vez que quieras dar un discurso, baja la voz. Se oyó hasta el pasillo."

    else:

        call e6_foco("nino", "neutral")

        nino "No viniste a buscarme y tampoco te fuiste. …No es un cumplido. No lo repitas."

        nino "Repasé inglés sola, con las etiquetas de la cocina, en voz baja. …Nadie me escuchó. Mejor para mí."

        nino "Y no, no te estaba esperando. …Contaba los días. Es distinto."

        nino "Ahora cállate un momento y déjame repasar la última página."

    ## --- Cierre del movimiento -----------------------------------------------------
    $ e6_limpiar()

    scene cg_cinco_aula
    with dissolve

    narrador "Me miraron las cinco. Esperaban una frase para terminar."

    mc_pensamiento "Hace un mes no tenía nada que decirles que no fuera mentira."

    mc_pensamiento "Hoy sí. Cada una sabe algo, y yo ya sé que lo saben."

    mc "Hagan lo que saben."

    narrador "No era una frase cualquiera."

    narrador "Cada palabra tenía un nombre detrás."

    if persistent.final_malo_temprano_b_visto:

        narrador "Sentí que ya había dicho esa frase antes. Con otro verbo, y con otro final."

        narrador "Siempre me imagino escenarios catastróficos antes de ver mi realidad."

    scene bg_aula
    with dissolve

    profe "Bien, todos a sus pupitres."

    profe "Volteen las hojas de sus exámenes."

    profe "Pueden empezar."

    scene bg_negro
    with fade

    narrador "Y así empezaron los exámenes."

    narrador "Ellas, sentadas delante y concentradas."

    narrador "Cada día, un examen. Cada día terminaba el mío antes de la mitad del tiempo."

    mc_pensamiento "Pero siempre me quedaba por ellas."

    mc_pensamiento "Siempre me quedaba por una a quien mirar."

    narrador "En un examen nadie habla. Eso no quiere decir que nadie piense."

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
##  MOV. 2 · YOTSUBA · LUNES · JAPONÉS
################################################################################

label e6_yotsuba_nucleo:

    $ ui_escena("beat", "yotsuba", "Aula · Japonés")
    $ tiempo_restante = "cinco exámenes"
    $ e6_limpiar()

    scene cg_yotsuba_examen
    with dissolve

    narrador "Lunes. Japonés. La primera prueba de cinco."

    narrador "Mi pupitre quedaba en la segunda fila, junto al pasillo."

    narrador "Terminé el mío antes de la mitad. Lo dejé boca abajo, con el lápiz encima."

    mc_pensamiento "Ahora solo me quedaba mirar."

    narrador "Las cinco lo hacían a la vez; yo solo podía mirar a una."

    mc_pensamiento "A Yotsuba."

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

    yotsuba_int "Vuelve al examen, Yotsuba. Despacio. Nadie te está cronometrando."

    yotsuba_int "Segunda pregunta. ¿Qué pasa cuando alguien llega para ayudarte?"

    yotsuba_int "Esa no me la sé del todo. Creo que es como un relevo."

    yotsuba_int "Un relevo no se gana corriendo más que nadie. Se gana recibiendo bien."

    return


label e6_yotsuba_mono_tibia:

    yotsuba_int "Pregunta uno. ¿Qué siente el protagonista cuando se queda solo?"

    yotsuba_int "Un minuto con diecisiete. Después, catorce. Tres segundos menos."

    yotsuba_int "Dijo «claro, dame el cronómetro» sin preguntar nada más."

    yotsuba_int "No sé si me sirvió que alguien mirara o si solo me dejó correr."

    yotsuba_int "Las piernas me avisan siempre. Hoy no me avisan de nada."

    yotsuba_int "Si termino rápido, ¿alguien va a necesitarme para algo?"

    yotsuba_int "Ichika actúa. Nino cocina. Miku sabe de historia. Itsuki estudia."

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

    yotsuba_int "Esa me la sé. Se queda quince minutos más en la pista. Por si acaso."

    yotsuba_int "Le dije que la tercera vuelta de ventaja la corría ese mismo día."

    yotsuba_int "No la corrí. Al doblar la esquina me puse a caminar."

    yotsuba_int "Tres suena mejor que dos. Tres suena a que no me importó tanto."

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

    yotsuba_int "La segunda pregunta trataba de eso."

    yotsuba_int "De cuando alguien llega para ayudarte y no te deja correr sola."

    yotsuba_int "Alguien llegó. Y esta vez… supe recibir el testigo."

    if e6_res == "saltado":

        narrador "Hay carreras que se corren por dentro. Esta la corrió entera, de un tirón."

    return


label e6_yotsuba_promesa:

    mc_pensamiento "Ese día me dijo que no pasaba nada."

    mc_pensamiento "Que no me preocupara por ella."

    mc_pensamiento "Eran tres tardes y cinco hermanas. Cualquiera lo habría entendido."

    mc_pensamiento "Quince minutos más cada tarde. Los contó, por si yo iba."

    mc_pensamiento "No fui. Eso no se arregla con un examen."

    mc_pensamiento "Cuando esto termine voy a la pista. Esas dos vueltas de más las cronometro yo."

    return


label e6_yotsuba_gesto_calida:

    narrador "Escribía sin parar y, de vez en cuando, levantaba la vista hacia las demás."

    narrador "Una vez miró a Ichika. Otra, a Miku. Después a Itsuki, y fue un saludo, no una alarma."

    mc_pensamiento "Escribir y mirar a la vez. Nadie le había dicho que se podían hacer las dos cosas."

    narrador "En la muñeca llevaba escrito un 28. No era una cuenta de vueltas."

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

    narrador "La segunda prueba de cinco."

    play sound audio.sfx_hoja volume 2.0

    scene cg_ichika_examen
    with fade

    narrador "Mismo pupitre. Mi hoja boca abajo antes de la mitad, otra vez."

    narrador "Las cinco lo hacían a la vez; yo solo podía mirar a una."

    mc_pensamiento "A Ichika."

    narrador "Ichika leyó el enunciado de principio a fin."

    narrador "Despacio, sin dormirse. Eso en ella ya es una noticia."

    narrador "El guion de la obra asomaba doblado por el bolsillo de su falda."

    narrador "Lo había traído, como siempre."

    mc_pensamiento "La pregunta cuatro era un problema de trenes."

    mc_pensamiento "De los que se resuelven con una resta y un poco de aire."

    mc_pensamiento "Aire es justo lo que a ella no le sobra."

    return


label e6_ichika_mono_calida:

    play music descubrimiento fadein 2.0

    ichika_int "Pregunta cuatro. Un tren sale a las cuatro cuarenta y cinco."

    ichika_int "Seis minutos a la estación, cuatro para cambiarse. Hay que salir a las cuatro treinta y cinco."

    ichika_int "Me salió antes de terminar de leer. Siempre lo supe. Nunca pensé que eso era matemáticas."

    ichika_int "Él lo notó. Dijo que nadie improvisa un número así. Yo lo llamé ser organizada."

    ichika_int "Después se quedó de pie, sin devolverme el chiste, esperando. Y yo dije lo que no digo."

    ichika_int "«No sé cuánto más puedo seguir haciendo esto.»"

    ichika_int "Lo dije en voz alta. Nada cambió por eso."

    ichika_int "A todos les digo «estoy bien». Me sale antes que el saludo."

    ichika_int "A él no se lo dije. Ni lo intenté."

    ichika_int "Le pedí la frase de tutor y no me la dio. «Eso ya lo sabes tú sola.»"

    ichika_int "Tenía razón, que es lo más incómodo de todo."

    ichika_int "El papel nuevo lo acepté sin pensar. Sigue en pie."

    ichika_int "En un escenario nadie me confunde con otra. Por eso digo que sí a todo."

    ichika_int "Y si la mayor encuentra algo suyo, las otras cuatro pueden buscar lo suyo."

    ichika_int "Pero ahora sé que dije que sí sin pensar."

    ichika_int "Tengo doce líneas del guion de la obra memorizadas."

    ichika_int "Salen solas. Las mías tardan un segundo entero."

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

    ichika_int "«Si tienes energía para hacer chistes, tienes energía para estudiar.» Eso dijo."

    ichika_int "Contesté «tienes razón», con mi sonrisa de siempre. Salió perfecto."

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

        narrador "Hay ensayos que se hacen por dentro, sin público. Este lo hizo completo."

    return


label e6_ichika_promesa:

    mc_pensamiento "Ichika ensayó tres caras para recibirme. No le di ocasión de usar ninguna."

    mc_pensamiento "Me pidió que la próxima vez no tardara tanto."

    mc_pensamiento "Voy a ir a verla ensayar. Sin avisar."

    mc_pensamiento "Que no le dé tiempo a preparar ninguna cara."

    return


label e6_ichika_gesto_calida:

    narrador "Ichika resolvió el examen en lo que tarda en cerrarse una puerta."

    narrador "Después se quedó mirando los resultados, como si se lo hubiera hecho otra persona."

    narrador "No era otra persona, era ella. Y lo sabía."

    mc_pensamiento "Ojos abiertos. El guion en el bolsillo, sin tocar. Ni una vez miró el reloj con miedo."

    mc_pensamiento "Hoy no necesitaba hacer de nadie. Ni fingir las cosas."

    play sound audio.sfx_timbre volume 1.5

    stop music fadeout 1.0

    return


label e6_ichika_gesto_tibia:

    narrador "Resolvió el examen rápido y se quedó sonriéndole a su hoja."

    profe "Nakano. Está sonriendo."

    ichika "Es una técnica, profesor."

    narrador "Nadie se rió. Ella tampoco. La sonrisa se le fue a mitad del problema siguiente."

    mc_pensamiento "Un chiste justo antes de que se le escapara algo. Otra vez."

    play sound audio.sfx_timbre volume 1.5

    return


label e6_ichika_gesto_fria:

    narrador "Resolvió el examen sin una pausa, sin un tachón, sin una mirada a nadie."

    narrador "La sonrisa estaba en su cara desde que empezó, igual de quieta que el reloj de la pared."

    mc_pensamiento "Una hoja perfecta y una sonrisa perfecta. Eso era lo que se veía."

    mc_pensamiento "Contesta como se contesta cuando alguien tiene razón: rápido y sin adornos."

    play sound audio.sfx_timbre volume 1.5

    return


label e6_ichika_gesto_no_visitada:

    narrador "Resolvía con una mano."

    narrador "Con su otra mano, bajo el pupitre, movía el guion doblado."

    narrador "Resolvía una pregunta, ensayaba una línea."

    narrador "Una línea, una pregunta. Las dos cosas a medias, y las dos bien."

    mc_pensamiento "Eso no es hacer dos cosas. Es no soltar ninguna."

    mc_pensamiento "Con ella el cansancio nunca se nota en lo que hace."

    mc_pensamiento "Se nota en que nunca para."

    play sound audio.sfx_timbre volume 1.5

    return


################################################################################
##  MOV. 4 · NINO · MIÉRCOLES · INGLÉS
################################################################################

label e6_nino_nucleo:

    $ ui_escena("beat", "nino", "Aula · Inglés")
    $ tiempo_restante = "tres exámenes"
    $ e6_limpiar()

    scene bg_negro
    with fade_dia

    narrador "Miércoles. Inglés."

    narrador "Ya estamos a mitad de los exámenes."

    narrador "La tercera prueba de cinco."

    play sound audio.sfx_hoja volume 2.0

    scene cg_nino_examen
    with fade

    narrador "Segunda fila. Mi hoja boca abajo antes de la mitad, y el lápiz encima."

    narrador "Las cinco lo hacían a la vez; yo solo podía mirar a una."

    mc_pensamiento "A Nino."

    narrador "Nino leyó el texto de comprensión una sola vez."

    narrador "Sin mover los labios. Sin improvisar."

    narrador "A media página se le movió la boca sola: una frase entera, sin voz. En inglés."

    mc_pensamiento "Pensaba en inglés, en un examen de inglés."

    mc_pensamiento "Si se lo hiciera notar, lo negaría."

    mc_pensamiento "Así que no se lo dije. Hay cosas que es mejor no señalarlas."

    mc_pensamiento "Además, en un examen no se habla."

    narrador "Los demás seguían en la primera pregunta."

    narrador "Nino iba a la velocidad de un tren que no frena."

    mc_pensamiento "A los quince minutos había terminado."

    mc_pensamiento "Yo, tres minutos antes. Ella lo sabía."

    mc_pensamiento "Pero ni siquiera levantó la vista. Ni siquiera me miró."

    return


## --- Capa de beat de Nino (se llama desde dentro de cada monólogo) ---------------

label e6_nino_beat_calida:

    nino_int "«¿Y quién junta los tuyos?» No contesté. No supe qué."

    nino_int "La pregunta sigue en la cocina. Y ahí se quedará."

    nino_int "Le mandé cortar cebollas finas. Las cortó gruesas."

    nino_int "Parece que nunca escucha. Las usé igual."

    nino_int "Le dejé un táper antes de cocinar. «Va a sobrar», le dije."

    nino_int "Cociné de más para que sobrara. Eso no lo sabe nadie."

    return


label e6_nino_beat_tibia:

    nino_int "Lavó mi taza sin que se lo pidiera."

    nino_int "A mi taza no la toca nadie."

    nino_int "¿Quién se creía ser en ese momento?"

    nino_int "No le dije «quédate». Tampoco «vete». Los dos nos entendimos igual."

    return


label e6_nino_beat_fria:

    nino_int "«Deja de juntar los pedazos de las demás y ocúpate de los tuyos.»"

    nino_int "Qué gran respuesta. Era de esperarse de un tonto como él."

    nino_int "Le dije que hablaba el mismo idioma que papá. Lo dije para que le doliera."

    nino_int "No dolió. Asintió, como si ya lo hubiera oído. Eso fue peor."

    return


label e6_nino_mono_calida:

    play music descubrimiento fadein 2.0

    nino_int "Texto B. Pregunta nueve. Lo leo una vez. No hace falta más."

    nino_int "«Solo el tiempo lo va a demostrar.» Eso dijo, con cara de no estar prometiendo nada."

    nino_int "Y no prometió nada. Esa es la parte que me dejó sin nada que decir."

    nino_int "Los otros prometían. Este no prometió y se quedó. Es una combinación rara."

    nino_int "Yo hablé de más y no se lo contó a nadie."

    nino_int "Se lo pregunté a Yotsuba, que no guarda nada."

    nino_int "Yotsuba no sabía nada."

    nino_int "Eso no es confiar. Es llevar la cuenta. Es distinto."

    nino_int "Es distinto."

    call expression ("e6_nino_beat_" + nino_rama_beat)

    nino_int "Siempre veo venir el golpe. Me adelanto: me cierro antes, pido que se vayan antes."

    nino_int "Así nunca duele a tiempo. Duele por adelantado. Y duele siempre."

    nino_int "Hoy no me ha dolido por adelantado."

    nino_int "Sigo con los brazos cruzados por dentro."

    nino_int "El chat sigue silenciado."

    nino_int "Esta semana no me salí ni una vez. Nadie me lo pidió."

    nino_int "Hay cena, pase lo que pase con las notas. Cocino yo. Siempre cocino yo."

    nino_int "La receta de la tarjeta me la sé de memoria. La llevo igual."

    nino_int "Hay letras que, si dejas de mirarlas, se te olvida cómo eran."

    nino_int "Cinco listas, una por hermana. La mía la escribo la última, y es la más corta."

    nino_int "Y una sexta línea que todavía no sé cómo llenar. …Primero las cinco."

    return


label e6_nino_mono_tibia:

    nino_int "Texto B. Pregunta nueve. Lo leo una vez."

    nino_int "De los otros tutores perdí la cuenta. De este no. No sé por qué."

    nino_int "Cargó mi cesta sin que se lo pidiera."

    nino_int "Pesaba. No dijo nada. Yo tampoco."

    nino_int "Dije «esto no significa nada». Lo dije yo, en voz alta, para que quedara dicho."

    call expression ("e6_nino_beat_" + nino_rama_beat)

    nino_int "¿Fue amable o fue su famoso método? Las dos cosas me cansan igual."

    nino_int "Si fue amable, no sé qué quiere. Si fue su método, no sé hasta cuándo."

    nino_int "Mis hermanas ya no dicen «¿y si esta vez sí?». Lo dicen bajito, y lo oigo igual."

    nino_int "El chat sigue silenciado. Esta semana no me salí. No sé por qué no me salí."

    nino_int "Si aprobamos las cinco… quizás esta vez no—"

    nino_int "Revisa la ocho. Hay un «has» que debería ser «have»."

    nino_int "Ya terminé. Seguiré en mi sitio. Hay que revisar."

    return


label e6_nino_mono_fria:

    nino_int "Texto B. Pregunta nueve. Lo leo una vez."

    nino_int "«Yo sí voy a durar.» Lo dijo como lo dijeron los otros."

    nino_int "Casi palabra por palabra."

    nino_int "Le dije que se guardara su promesa vacía."

    nino_int "Prometió durar. Ha durado. Eso hay que reconocérselo."

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

    nino_int "Las que fue a ver llegaron distintas a casa."

    nino_int "No le dije si mejor o peor. No pienso decírselo."

    nino_int "Alguien tiene que ser la que no cambia."

    nino_int "Para que las demás tengan a dónde volver."

    nino_int "No vino a buscarme. Está bien."

    nino_int "A mí no se me busca, yo no se lo he pedido a nadie."

    nino_int "Igualmente me encontró en la cocina. Me oyó pedir que lo echaran."

    nino_int "Y no se fue."

    nino_int "Eso no sé en qué lista ponerlo."

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

        narrador "Hay compras que se hacen de memoria."

        narrador "Esta la hizo completa, de un tirón."

    if e6_sexto_valor() == "taza":

        nino_int "Escribí «una taza más»."

        nino_int "Se compra igual aunque nadie la pida. De repuesto."

        nino_int "…No es por nadie."

    elif e6_sexto_valor() == "cuando":

        nino_int "Escribí «cuando se sepa»."

        nino_int "Se compra con el resultado en la mano."

        nino_int "No antes de saberlo."

    else:

        nino_int "Dejé la sexta línea en blanco."

        nino_int "Sin tachar. Una línea en blanco no se pierde: se espera."

    nino_int "No pienso adelantar el golpe."

    nino_int "Si cae, cae. Pero no voy a ganarle la mano para que duela primero."

    nino_int "Esperar no es rendirse. Me costó treinta y dos días entenderlo."

    nino_int "Voy a entregar. Las demás terminarán a su ritmo. Esta vez no hago guardia."

    return


label e6_nino_promesa:

    mc_pensamiento "Me dijo que ni le molestaba que no la hubiera ido a buscar."

    mc_pensamiento "Dijo que alguien tiene que ser la que no cambia."

    mc_pensamiento "Para que las demás tengan a dónde volver."

    mc_pensamiento "También dijo que ya me había visto en su casa más de lo que quería."

    mc_pensamiento "Que eso contaba como visita."

    mc_pensamiento "Voy al centro comercial, al pasillo de importados."

    mc_pensamiento "Y a cargar cualquier cesta aunque no me lo pida."

    return


label e6_nino_gesto_calida:

    narrador "Nino terminó. Soltó el lápiz sin ruido y giró la hoja boca abajo."

    narrador "Cruzó los brazos, un poco más fuerte que otras veces."

    profe "Nakano. Si ya terminó, puede entregar."

    nino "Sí."

    play sound audio.sfx_silla volume 2.5

    narrador "Se levantó, dejó la hoja en la mesa del profesor y fue hacia la puerta sin mirar atrás."

    narrador "A las demás no les echó ni una mirada de guardia. Ni una."

    narrador "Ya no hacía falta vigilar a las demás."

    play sound audio.sfx_puerta_cierra volume 1.0

    mc_pensamiento "Quien ve venir el golpe se queda a esperarlo. Quien no lo adelanta, sale."

    mc_pensamiento "Se fue sin vigilarlas. Y nadie se cayó."

    play sound audio.sfx_timbre volume 1.5

    stop music fadeout 1.0

    return


label e6_nino_gesto_tibia:

    narrador "Nino terminó antes que casi todas. Soltó el lápiz."

    narrador "Giró la hoja boca abajo. Cruzó los brazos."

    profe "Nakano. Si ya terminó, puede entregar."

    nino "Aún no. Voy a revisar."

    narrador "Revisó cuarenta minutos, línea por línea. Y, de reojo, a las otras cuatro."

    mc_pensamiento "No había nada que revisar."

    mc_pensamiento "Se quedaba por ellas. O por no estar a solas con lo que viene."

    mc_pensamiento "Quizás por las dos cosas. Ella no iba a decirme cuál."

    play sound audio.sfx_timbre volume 1.5

    return


label e6_nino_gesto_fria:

    narrador "Nino terminó. Soltó el lápiz sin ruido, giró la hoja boca abajo y cruzó los brazos, un poco más fuerte."

    profe "Nakano. Si ya terminó, puede entregar."

    nino "No. Aun me falta revisar unas cosas."

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


################################################################################
##  MOV. 5 · ITSUKI · JUEVES · CIENCIAS
################################################################################

label e6_itsuki_nucleo:

    $ ui_escena("beat", "itsuki", "Aula · Ciencias")
    $ tiempo_restante = "dos exámenes"
    $ e6_limpiar()

    scene bg_negro
    with fade_dia

    narrador "Jueves. Ciencias."

    narrador "La penúltima prueba de cinco."

    play sound audio.sfx_hoja volume 2.0

    scene cg_itsuki_examen
    with fade

    narrador "Segunda fila. Mi hoja boca abajo, el lápiz encima. Ya era costumbre."

    narrador "Las cinco lo hacían a la vez; yo solo podía mirar a una."

    mc_pensamiento "A Itsuki."

    narrador "Itsuki escribía con la derecha. El índice de la izquierda recorría los renglones sin tocarlos."

    narrador "Llevaba tres líneas bien. La cuarta la leyó una vez, y otra, y otra."

    mc_pensamiento "Una conversión de unidades. De las que se resuelven con orden y sin prisa."

    mc_pensamiento "Ella tiene el orden. A veces le falta mirar un paso atrás."

    mc_pensamiento "Conozco el tipo de trampa. No podía decírsela: en un examen no se habla."

    return


## --- Capa de beat de Itsuki: eco de la azotea -------------------------------------
##  ayudada = su evento fue el hub 1 (rama cálida o fría) · sola = el resto.

label e6_itsuki_beat_ayudada:

    itsuki_int "«No hace falta que sigas viniendo a comprobar cómo voy.»"

    itsuki_int "Lo dije yo. Vino igual."

    itsuki_int "Pasamos la hora sin abrir ningún libro."

    itsuki_int "Fue la hora más útil del mes. No pienso decirlo."

    return


label e6_itsuki_beat_sola:

    itsuki_int "En la azotea no le pregunté cómo iba su juego."

    itsuki_int "Él no me lo contó. Fue un buen acuerdo."

    itsuki_int "Pasamos la hora sin abrir ningún libro."

    itsuki_int "Fue la hora más útil del mes. No pienso decirlo."

    return


label e6_itsuki_mono_calida:

    play music descubrimiento fadein 2.0

    itsuki_int "Pregunta cuatro."

    itsuki_int "Conversión de unidades. Cinco pasos."

    itsuki_int "Planteé bien. Convertí el caudal. Pasé al tiempo. Y el resultado no cuadra."

    itsuki_int "Es el mismo error de siempre: en un sitio que no encuentro, con un número que reconozco."

    if hub_visitadas[0] == "itsuki":
        call e6_itsuki_beat_ayudada
    else:
        call e6_itsuki_beat_sola

    itsuki_int "Me dijo: «Solo te digo dónde mirar»."

    itsuki_int "No me dio la respuesta. Me dio una dirección."

    itsuki_int "El primer día le dije: «Ni se te ocurra decirme la respuesta»."

    itsuki_int "Era una regla para él."

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

    itsuki_int "Me ofreció revisarlo desde el principio."

    itsuki_int "Dije que no antes de saber qué iba a explicarme."

    itsuki_int "Todavía no sé qué iba a explicarme. Quizá un paso. Quizá otra cosa."

    itsuki_int "Dije «todavía no necesito tu ayuda». Era mi forma de expresarme."

    itsuki_int "No era una promesa."

    itsuki_int "…¿O sí lo era?"

    itsuki_int "Podría levantar la mano. Preguntarle al profesor. Preguntar sería—"

    itsuki_int "Revisaré desde el principio. Sola."

    return


label e6_itsuki_mono_fria:

    itsuki_int "Pregunta cuatro. Conversión de unidades. Cinco pasos."

    itsuki_int "Planteé bien. Convertí el caudal. Pasé al tiempo. Y el resultado no cuadra."

    itsuki_int "Revisaré cada paso, uno por uno, desde el primero. Sin ayuda."

    if hub_visitadas[0] == "itsuki":
        call e6_itsuki_beat_ayudada
    else:
        call e6_itsuki_beat_sola

    itsuki_int "Me quitó el cuaderno de las manos. Lo resolvió de pie, con mi propio lápiz."

    itsuki_int "Bien y rápido. No era el ejercicio lo que defendía. Era hacerlo por mí misma."

    itsuki_int "Taché su solución y escribí la mía debajo. Le dije que ya tenía lo que necesitaba de él."

    itsuki_int "Lo mantengo."

    itsuki_int "Resolver sola cuesta el triple. Entrego sobre la campana. No importa."

    itsuki_int "Nadie va a decirme dónde mirar. Nadie va a decirme nada."

    itsuki_int "No necesito preguntar."

    return


label e6_itsuki_mono_no_visitada:

    itsuki_int "Pregunta cuatro. Conversión de unidades. Cinco pasos."

    itsuki_int "Es del mismo tipo que el del círculo a lápiz."

    itsuki_int "Reconozco la forma antes de leer los números."

    itsuki_int "Planteé bien. Convertí el caudal. Pasé al tiempo. Y el resultado no cuadra."

    call e6_itsuki_beat_sola

    itsuki_int "Repasé aquel ejercicio hasta hundir el papel. Y me atasco en el mismo punto."

    itsuki_int "Dije que gané el juego. Una victoria que no vino a cobrar nadie."

    itsuki_int "Pedirlo habría sido…"

    itsuki_int "No. Termino la oración. Pedirlo habría sido empezar. Y no sé dónde se para uno después."

    itsuki_int "Si hubiera venido, no lo habría echado. No inmediatamente. Eso no."

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

        narrador "No supe si levantó la mano o la dejó abajo."

        narrador "Cuando volví a mirar, la cuatro estaba resuelta."

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

        narrador "Y empezó otra vez desde la primera línea."

        narrador "Despacio. Sin saltarse ninguna unidad."

        itsuki_int "Una hora y media. Noventa minutos. Cinco mil cuatrocientos segundos. Ahora sí."

        itsuki_int "Me salió sola. Y tardé el doble. Las dos cosas son ciertas."

        itsuki_int "La próxima vez preguntaré."

    return


label e6_itsuki_promesa:

    mc_pensamiento "Subió a la azotea con un cuaderno y no lo abrió. Yo estaba ahí."

    mc_pensamiento "Me dijo que no se iba a esconder. No lo hizo."

    mc_pensamiento "Estaba donde siempre, estudiando. Sola."

    mc_pensamiento "Dijo que si hubiera ido a buscarla no me habría echado."

    mc_pensamiento "No inmediatamente. Y que no lo apuntara."

    mc_pensamiento "Todavía me debe cuatro bocados del almuerzo de Raiha. No pienso cobrárselos."

    mc_pensamiento "No lo apunté. Pero voy a subir con comida para dos, y a pedirle que suba ella sin el cuaderno."

    mc_pensamiento "Una vez."

    return


label e6_itsuki_gesto_calida:

    narrador "Entregó con cuatro minutos de sobra. La cuarta tenía una sola raya, prolija."

    narrador "Al pasar junto a mi pupitre me miró un segundo. Esta vez no apartó la vista."

    narrador "Asintió una vez, seca, como quien confirma un dato y no pide aplauso."

    mc_pensamiento "Hace un mes apartar la mirada era su forma de no deberme nada."

    mc_pensamiento "Hoy mirar era no ocultar nada."

    mc_pensamiento "No necesitó que yo le dijera dónde mirar el error."

    mc_pensamiento "Ya sabía dónde. Y a quién preguntar, si hacía falta."

    play sound audio.sfx_timbre volume 1.5

    stop music fadeout 1.0

    return


label e6_itsuki_gesto_tibia:

    narrador "Entregó sobre la campana, con la cuarta tachada y reescrita dos veces."

    narrador "A media hoja había levantado la vista."

    narrador "Me miró un segundo. Apartó la mirada y volvió al papel."

    mc_pensamiento "Pudo preguntar. Eligió tardarse."

    mc_pensamiento "Con ella, tardarse también es una forma de orgullo."

    mc_pensamiento "Revisó desde el principio, sola."

    mc_pensamiento "Apretaba el lápiz no por rabia, sino por su forma de ser."

    play sound audio.sfx_timbre volume 1.5

    return


label e6_itsuki_gesto_fria:

    narrador "Entregó sobre la campana. La hoja, impecable."

    narrador "Ni una pregunta, ni una mirada."

    narrador "Al terminar guardó su formulario con las dos manos, rápido."

    mc_pensamiento "No levantó la vista ni una vez. Ni para odiarme."

    mc_pensamiento "Resolvió sola. Es lo único que no iba a dejar que nadie le quitara. Esta vez nadie lo intentó."

    play sound audio.sfx_timbre volume 1.5

    return


label e6_itsuki_gesto_no_visitada:

    narrador "Entregó pasada la campana, con la cuarta recién resuelta. Tarde, pero resuelta."

    narrador "A media hoja había levantado la vista."

    narrador "Me miró un segundo, y apartó la mirada."

    mc_pensamiento "La miré yo primero."

    mc_pensamiento "Ella apartó la vista, como si hubiera algo que no estaba lista para decirme."

    mc_pensamiento "Nunca me pidió nada. Y yo nunca fui."

    mc_pensamiento "Los dos dejamos la misma pregunta sin hacer. Nadie avanzó."

    play sound audio.sfx_timbre volume 1.5

    return


################################################################################
##  MOV. 6 · MIKU · VIERNES · SOCIALES
################################################################################

label e6_miku_nucleo:

    $ ui_escena("beat", "miku", "Aula · Sociales")
    $ tiempo_restante = "un examen"
    $ e6_limpiar()

    scene bg_negro
    with fade_dia

    narrador "Viernes. Sociales."

    narrador "Hoy es el último día de exámenes."

    narrador "Hoy termina todo."

    narrador "La última prueba."

    play sound audio.sfx_hoja volume 2.0

    scene cg_miku_examen
    with fade

    narrador "Segunda fila, mi hoja boca abajo. A este examen lo dejé más despacio."

    narrador "Las cinco lo hacían a la vez; yo solo podía mirar a una."

    mc_pensamiento "A Miku."

    narrador "Miku tenía el lápiz en la mano derecha y, junto al lápiz, la goma."

    narrador "Limpia, entera. Con las cuatro esquinas sin usarse."

    mc_pensamiento "En su hoja del segundo día, la goma había trabajado más que el lápiz."

    narrador "Los audífonos colgaban de su cuello, apagados."

    mc_pensamiento "La pregunta tres no decía «sal». Decía «rutas de comercio»."

    mc_pensamiento "Lo que escribiera de más sería ella. Lo que no escribiera, también."

    return


label e6_miku_mono_calida:

    play music descubrimiento fadein 2.0

    miku_int "…Pregunta tres. Rutas de comercio y sostén de una provincia sin costa."

    miku_int "…Sal."

    miku_int "…No dice «sal». Pero la respuesta es la sal."

    miku_int "…Él me preguntó cuánto tardaba en llegar. …Diez días. Doce si llovía."

    miku_int "…Contesté sin pensar. Iba a pedir perdón."

    miku_int "…No me dejó. Dijo que eso no se disculpa."

    miku_int "…Estaba contestando una pregunta que me hizo él."

    miku_int "…Todavía no sé si le creo."

    miku_int "…Dijo que no me faltaba la materia."

    miku_int "…Que me faltaba creer que lo que sé cuenta como saber."

    miku_int "…Dijo que lo iba a comprobar. Hoy es el día."

    miku_int "…Esta pregunta es lo que sé, y el examen la pide."

    miku_int "…Hablar cuesta. Escribir también, si es de algo que quiero. Cuesta igual."

    miku_int "…Tengo una canción en la cabeza. Es la que pongo para que nadie se acerque."

    miku_int "…Voy a escribir pensando en ella."

    miku_int "…Cuando acabe de pensar en esa canción, quedará el sonido del reloj del aula."

    miku_int "…El reloj nunca ha pedido perdón."

    miku_int "…Vamos."

    return


label e6_miku_mono_tibia:

    miku_int "…Pregunta tres. Rutas de comercio y sostén de una provincia sin costa."

    miku_int "…Dijo que se me daba bien. Yo dije que solo lo había leído."

    miku_int "…Dijo que era más de lo que había hecho nadie en mi casa."

    miku_int "…Era un elogio con una comparación dentro."

    miku_int "…¿Me lo dijo a mí o me puso al lado de las demás?"

    miku_int "…Mis hermanas también leen. …No tanto, pero leen."

    miku_int "…La sal entra por las rutas. Podría contarla."

    miku_int "…Si la cuento y no suma, me habré pasado de hablar."

    miku_int "…Si no la cuento, nadie va a saber que la sé."

    miku_int "…Lo que amo no—"

    miku_int "…Pregunta cuatro."

    return


label e6_miku_mono_fria:

    miku_int "…Pregunta tres. Rutas de comercio y sostén de una provincia sin costa."

    miku_int "…«Sin costa». …Eso es Shingen. …Eso es la sal."

    miku_int "…Dijo que lo de la sal no entraba. Tres temas, y ninguno pregunta por ella."

    miku_int "…La pregunta no dice «sal». …Entonces tenía razón."

    miku_int "…Cuatro renglones del libro de texto: rutas, mercados, impuestos. Está todo."

    miku_int "…Escribo eso. Lo que me van a preguntar."

    miku_int "…La otra respuesta también la sé. Entera."

    miku_int "…Hoy no."

    return


label e6_miku_mono_no_visitada:

    miku_int "…Pregunta tres. Rutas de comercio y sostén de una provincia sin costa."

    miku_int "…Sal. La respuesta empezó a escribirse sola. Ya llevo cuatro renglones."

    miku_int "…No debería. Es un examen. …Borro."

    miku_int "…Cuando hablo de esto, la gente pone una cara. La de esperar a que termine."

    miku_int "…El papel no pone caras. …Igual borro."

    miku_int "…La silla de enfrente sigue vacía. …Eso ya lo dije una vez."

    miku_int "…Escribo tres líneas de rutas. La sal, otro día."

    return


## --- Minijuego M3 (solo cálida). Su tema SOLO suena aquí, y lo arranca M3 --------
label e6_miku_mj:

    call mj_ejecutar(E6_MJ_JUEGO["miku"], "miku")
    $ e6_res = _return

    ## M3 corta su tema al terminar. Si se saltó, aún suena descubrimiento.
    stop music fadeout 3.0

    narrador "Se quitó los audífonos del cuello, despacio."

    narrador "Los plegó y los dejó en el pupitre, junto a la goma."

    miku_int "Alguien se la vendió. Y eso me parece mucho más importante que la leyenda."

    miku_int "Si alguien pone la cara de esperar a que termine, que espere."

    miku_int "Esperé el perdón. Es lo que viene después. No llegó."

    narrador "Escribía sin levantar la cabeza. Sin detenerse al final de cada línea. Sin borrar."

    if e6_res == "saltado":

        narrador "Hay respuestas que se escriben solas."

        narrador "Esta lo hizo de una vez, de principio a fin."

    return


label e6_miku_promesa:

    mc_pensamiento "Me dijo que así había estado bien. Que estuvo tranquila."

    mc_pensamiento "Y que habría acertado con el sitio."

    mc_pensamiento "También, que hay una silla enfrente de la suya. Siempre vacía."

    mc_pensamiento "Dejó un libro abierto dos días, por si hacía falta una excusa."

    mc_pensamiento "Voy a sentarme en esa silla."

    mc_pensamiento "Y a leer lo mismo que ella, aunque no entienda nada."

    return


label e6_miku_gesto_calida:

    narrador "Cuando sonó el timbre, su hoja estaba llena hasta el último renglón."

    narrador "Sin un solo borrón."

    mc_pensamiento "La goma seguía siendo una goma."

    mc_pensamiento "Hace un mes eso habría sido una noticia."

    narrador "No recogió los audífonos enseguida. Los miró un segundo, como quien comprueba que no se mueven solos."

    mc_pensamiento "Plegados, no puestos. Como se dejan las llaves en la entrada."

    narrador "Al final los recogió. Se los colgó al cuello."

    narrador "Sin subírselos."

    play sound audio.sfx_timbre volume 1.5

    return


label e6_miku_gesto_tibia:

    narrador "Escribió la respuesta de rutas sin una sola mención a la sal."

    narrador "Cada vez que se acercaba a una frase larga, el cuadernillo le subía un poco más."

    mc_pensamiento "Sabía cómo seguir. Se le veía en el lápiz, que dudaba justo antes de cada coma."

    mc_pensamiento "No borró. Se detuvo."

    mc_pensamiento "Es una forma de borrar en la que no se usa goma."

    play sound audio.sfx_timbre volume 1.5

    return


label e6_miku_gesto_fria:

    narrador "Escribió firme, sin dudas, cuatro renglones exactos."

    narrador "Hacia la mitad, la mano libre subió hasta los audífonos."

    narrador "Y se quedó ahí hasta el timbre."

    mc_pensamiento "No se los puso. No los soltó."

    mc_pensamiento "Era una respuesta correcta y me dolió mirarla."

    mc_pensamiento "Tuve razón en la letra del temario. Esa fue otra forma de no ganar."

    play sound audio.sfx_timbre volume 1.5

    return


label e6_miku_gesto_no_visitada:

    narrador "Escribió largo. Se detuvo a mitad de un renglón."

    narrador "Pasó la goma una sola vez, con cuidado."

    narrador "A la goma le faltaba un borde. Aún se podía usar."

    mc_pensamiento "Desde la segunda fila no pude leer lo que borró. Pude ver cuánto ocupaba."

    mc_pensamiento "Lo dejó en tres líneas. Las de quien no quiere molestar."

    play sound audio.sfx_timbre volume 1.5

    return


################################################################################
##  MOV. 7 · DESPUÉS DEL EXAMEN
##  Viernes, última campana. Espejo del Mov. 4 de final_malo_hub3 («Después
##  del examen»): misma aula de tarde, las mismas cinco que se quedan. Allí
##  confiesan el fracaso con «derrota»; aquí cuentan lo que hicieron distinto,
##  sin saber todavía las notas. MC no dice «sé cómo terminó», dice «no sé».
##  Núcleo común + 3 capas:
##    S-tarde (estado de entrada, 3 variantes, solo pensamiento de MC)
##    e6_<h>_tarde_<estado> (4 variantes por hermana, coherentes con su gesto)
##    e6_nino_puerta_<estado> (salida, 4 variantes)
##  No toca: notas, ecos del Mov. 9, disculpa de Itsuki, frases cortadas.
##  Variantes (S-tarde, tardes por hermana, pregunta, puerta): debajo de e6_despues.
################################################################################


label e6_despues:

    $ ui_escena("beat", None, "Aula · Viernes por la tarde")
    $ e6_limpiar()

    stop ambiente fadeout 1.0

    scene bg_negro
    with fade

    narrador "Sonó la última campana de la semana."

    narrador "El aula se fue vaciando."

    narrador "Todos los estudiantes se retiraban a sus hogares."

    narrador "Ellas se quedaron."

    scene bg_aula_tarde
    with fade

    call e6_formacion_neutral

    if persistent.final_malo_temprano_b_visto:

        narrador "Conocía esta aula a esta hora. La recordaba con cinco caras que ya sabían cómo había ido."

    narrador "Nadie recogía nada. Ninguna dijo «salió bien»."

    narrador "Esta vez no era por miedo a decirlo."

    narrador "Era porque nadie lo sabía todavía."

    mc_pensamiento "Ni siquiera sonaba el reloj."

    mc_pensamiento "Después de cinco días, el silencio se oía raro."

    ## --- MC: el espejo de «Sé cómo terminó todo esto» --------------------------------

    mc "Bueno. Se acabó."

    mc "Pensé en algo bonito para decirles. Lo ensayé de camino al aula."

    mc "Pero la verdad es que no sé cómo terminó esto."

    call expression ("e6_s_tarde_" + e6_estado_entrada)


    mc "No sé si salió bien. Hasta mañana, nadie lo sabe."

    mc "Y no voy a decirles «bien hecho» por algo que todavía no sé."

    narrador "Era lo más honesto que les había dicho en un mes. Y lo más corto."

    ## --- Lo que hizo cada una. Mismo orden que el Final B y el Mov. 1 --------------

    ## --- YOTSUBA · japonés (lunes) -----------------------------------------------------

    call expression ("e6_yotsuba_tarde_" + e6_estado_de("yotsuba"))


    ## --- ICHIKA · matemáticas (martes) ------------------------------------------------

    call expression ("e6_ichika_tarde_" + e6_estado_de("ichika"))


    ## --- NINO · inglés (miércoles) -----------------------------------------------------

    call expression ("e6_nino_tarde_" + e6_estado_de("nino"))


    ## --- ITSUKI · ciencias (jueves) ----------------------------------------------------

    call expression ("e6_itsuki_tarde_" + e6_estado_de("itsuki"))


    ## --- MIKU · sociales (viernes) ------------------------------------------------------

    call expression ("e6_miku_tarde_" + e6_estado_de("miku"))


    ## --- «¿Y a ti cómo te fue?» ------------------------------------------------------

    call e6_tarde_pregunta


    mc "¿A mí?"

    mc "Bien. Creo."

    narrador "Intenté recordar una sola pregunta de mis cinco exámenes. No me vino ninguna."

    mc "…La verdad es que no me acuerdo."

    call e6_foco("nino", "molesta")

    nino "¿Cómo que no te acuerdas?"

    nino "Hiciste cinco exámenes. Igual que nosotras."

    mc "Terminaba antes de la mitad. Y luego…"

    mc "Luego las miraba a ustedes."

    call e6_foco("", "")

    narrador "Hubo un silencio corto. De los que se llenan solos."

    narrador "Alguien se rió primero. Después, las demás. No supe quién empezó."

    play music cotidiano fadein 2.5 volume 0.6

    call e6_foco("ichika", "sonriendo")

    ichika "Qué tutor más raro."

    call e6_foco("", "")

    mc_pensamiento "Cinco exámenes míos, y no recordaba ni una pregunta."

    mc_pensamiento "Recordaba un nombre escrito antes que nada. Ese uno por ciento que iba progresando."

    mc_pensamiento "Un guion doblado que no salió del bolsillo. De alguien que ya no se durmió."

    mc_pensamiento "Unos labios moviéndose en inglés. Y observando a quienes protege."

    mc_pensamiento "Un dedo recorriendo renglones sin tocarlos. Y resolviendolos con confianza."

    mc_pensamiento "Y unos audífonos al cuello, apagados. Sin tocarlos."

    mc_pensamiento "Cinco personas que saben una cosa cada una."

    mc_pensamiento "Esta semana no les enseñé nada. Me senté atrás y aprendí yo."

    ## --- Nadie se ha ido -------------------------------------------------------------

    call e6_foco("ichika", "neutral")

    ichika "Oigan. ¿Se han dado cuenta?"

    ichika "La campana sonó hace un buen rato. Y ninguna se ha ido."

    call e6_foco("nino", "molesta")

    nino "Estoy esperando a que se vacíe el pasillo."

    call e6_foco("ichika", "sonriendo")

    ichika "El pasillo está vacío desde hace diez minutos, Nino."

    call e6_foco("nino", "pillada")

    nino "…Pues espero a que se vacíe más."

    call e6_foco("", "")

    stop music fadeout 3.0

    call e6_foco("yotsuba", "incomoda")

    yotsuba "…Es que si salimos por esa puerta, se acaba la semana."

    narrador "Lo dijo bajito. Yotsuba, que no dice nada bajito."

    call e6_foco("itsuki", "neutral")

    itsuki "Y el mes. El plazo era de un mes."

    call e6_foco("", "")

    narrador "Nadie dijo lo que venía después. No hacía falta."

    narrador "El plazo era el mío. Ese mes era la razón por la que yo seguía en esta aula."

    mc_pensamiento "Mañana un papel diría si seguía. Ellas lo sabían igual que yo."

    narrador "Me miraron las cinco. Cinco preguntas iguales, y ninguna en voz alta."

    call e6_foco("nino", "neutral")

    nino "Nadie le va a preguntar nada."

    nino "Lo que tenga que pasar, que pase mañana."

    nino "Mañana se sabe. Y ya."

    call e6_foco("", "")

    mc_pensamiento "Podía decirles que el lunes estaría con ellas. Sonaría bien."

    mc_pensamiento "Y sería exactamente lo que les dijeron todos los que se fueron."

    mc "No voy a prometerles nada. Ya les han prometido bastante."

    mc "Solo sé una cosa: hoy no me voy de esta aula hasta que salga la última."

    narrador "Nadie contestó. Itsuki bajó la vista a su pupitre. Nino descruzó los brazos."

    if e6_estado_de("miku") == "calida":

        call e6_foco("miku", "relajada")

        miku "Entonces salgamos todas a la vez."

        miku "Así nadie se queda de última."

        narrador "Sin pausa delante. Lo dijo como se dice algo que ya estaba decidido."

    else:

        call e6_foco("miku", "neutral")

        miku "…Entonces salgamos todas a la vez."

        miku "…Así nadie se queda de última."

    call e6_foco("itsuki", "sonriendo")

    itsuki "Apoyo la idea."

    call e6_foco("ichika", "sonriendo")

    ichika "Aprobada por todas. Es la primera votación del mes que no gana Nino."

    call e6_foco("nino", "molesta")

    nino "No hubo votación."

    call e6_foco("", "")

    narrador "No contó nadie. Se levantaron las cinco a la vez, como si lo hubieran ensayado."

    play sound audio.sfx_silla volume 1.2

    narrador "Yo también me levanté."

    $ e6_limpiar()

    hide ichika
    hide nino
    hide miku
    hide yotsuba
    hide itsuki
    with disolucion_lenta

    scene bg_aula_atardecer
    with dissolve

    narrador "Antes de salir miré atrás una sola vez."

    narrador "Cinco pupitres vacíos, la luz de la tarde encima, los lápices ya guardados."

    if persistent.final_malo_temprano_b_visto:

        narrador "Esa imagen la recordaba de otra forma: conmigo dentro, y nadie en la puerta."

    mc_pensamiento "Hace un mes, esta imagen me habría parecido el final de algo."

    mc_pensamiento "Hoy solo parecía un aula vacía un viernes."

    mc_pensamiento "Las aulas vacías se vuelven a llenar."

    call expression ("e6_nino_puerta_" + e6_estado_de("nino"))


    ## --- Fuera ------------------------------------------------------------------------

    scene bg_escuela_atardecer
    with fade

    play music cotidiano fadein 3.0 volume 0.5

    narrador "Bajamos la cuesta del instituto sin prisa. Nadie propuso a dónde ir."

    narrador "El sol de la tarde nos estiraba las sombras sobre la acera."

    narrador "Las suyas iban delante, largas, casi iguales."

    narrador "Una con audífonos al cuello. Una con un mechón rebelde en lo alto de la cabeza."

    narrador "Una con dos moños de mariposa. Una que daba un saltito cada tres pasos."

    narrador "Y una que caminaba como si la estuviera mirando un público."

    mc_pensamiento "Hace un mes no habría sabido decir cuál era cuál."

    mc_pensamiento "Hoy las distinguía hasta por la sombra."

    narrador "Mi sombra iba detrás. Lo bastante larga para rozar las suyas."

    mc_pensamiento "No sabía cómo había terminado esto. Mañana lo diría un papel."

    mc_pensamiento "Pero esta tarde nadie se quedó de último."

    narrador "No saberlo todavía me pesaba. Lo que cambió fue que esta vez no lo cargaba solo."

    stop music fadeout 3.0

    return


## --- S-tarde · estado de entrada (solo pensamiento de MC; ellas no lo oyen) ------

label e6_s_tarde_superado:

    mc_pensamiento "«Si una sola reprueba, se acabó.»"

    mc_pensamiento "Mañana esa frase iba a tener un número al lado."

    mc_pensamiento "Una sola nota por debajo de sesenta, y esta sería mi última tarde con este trabajo."

    mc_pensamiento "Lo sabía yo. No hacía falta que lo cargaran ellas también."

    return


label e6_s_tarde_mixto:

    mc_pensamiento "Cinco exámenes terminados, y ni una sola pista de cómo habían salido."

    mc_pensamiento "No sabía si había hecho suficiente o poco."

    mc_pensamiento "Desde hoy, ya no había forma de hacer más."

    mc_pensamiento "Solo quedaba esperar. Y esperar nunca se me dio bien."

    return


label e6_s_tarde_bueno:

    mc_pensamiento "El lunes dije que confiaba en ellas."

    mc_pensamiento "Era verdad, pero era una apuesta. En las apuestas o se gana o se pierde."

    mc_pensamiento "Hoy, además, las había visto escribir. A las cinco, una por una."

    mc_pensamiento "Aun así, un papel puede decir otra cosa. Los papeles no conocen a nadie."

    return


##  Espejo B4: «Mi hoja estuvo en blanco. Solo escribí mi nombre.»

label e6_yotsuba_tarde_calida:

    call e6_foco("yotsuba", "neutral")

    yotsuba "[mc]…"

    yotsuba "Yo sí sé una cosa."

    yotsuba "El lunes escribí mi nombre primero, como siempre. Pero después seguí escribiendo."

    yotsuba "Llené la hoja. Y miré a mis hermanas igual, pero para saludarlas."

    call e6_foco("yotsuba", "sonriendo")

    yotsuba "No sé si está bien. Pero esta vez la hoja también era mía."

    narrador "Lo dijo sin gritar. En Yotsuba, eso sonaba más fuerte que un grito."

    return


label e6_yotsuba_tarde_tibia:

    call e6_foco("yotsuba", "sonriendo")

    yotsuba "¡[mc]! ¡Yo sí sé una cosa! ¡Terminé la hoja entera!"

    call e6_foco("yotsuba", "neutral")

    yotsuba "Bueno… casi entera. Hubo una frase que empecé y no terminé."

    mc "¿Cuál?"

    call e6_foco("yotsuba", "sonriendo")

    yotsuba "¡Una que no venía en el examen!"

    narrador "Se rió. La frase se quedó donde la había dejado el lunes."

    return


label e6_yotsuba_tarde_fria:

    call e6_foco("yotsuba", "sonriendo")

    yotsuba "¡Tutor! ¡Hoja llena! ¡Sin mirar a nadie ni una sola vez!"

    yotsuba "Me concentré en lo mío. Como dijiste."

    mc "Yotsuba…"

    yotsuba "¡Es lo que tenía que hacer!"

    yotsuba "¡Es lo que mejor sé hacer! Lo sé."

    narrador "Me sonrió a mí. Hacia sus hermanas no giró la cabeza. Ni siquiera ahora."

    return


label e6_yotsuba_tarde_no_visitada:

    call e6_foco("yotsuba", "sonriendo")

    yotsuba "¡[mc]! ¡Le pasé un lápiz a Ichika antes de que lo pidiera!"

    yotsuba "Eso no sale en el examen, ¡pero cuenta!"

    call e6_foco("yotsuba", "neutral")

    yotsuba "…¿Tú me viste? Desde la segunda fila."

    mc "Te vi."

    call e6_foco("yotsuba", "sonriendo")

    yotsuba "¡Entonces ya está!"

    narrador "No preguntó qué había visto. Le bastaba con que alguien hubiera mirado."

    return


##  Espejo B4: «Me dormí delante de todos.»

label e6_ichika_tarde_calida:

    call e6_foco("ichika", "neutral")

    ichika "No me dormí en ningún examen."

    ichika "Leí cada enunciado entero, con los ojos abiertos."

    ichika "El guion se quedó en el bolsillo. No lo saqué ni una vez."

    ichika "Al terminar me quedé mirando la hoja como si la hubiera hecho otra persona."

    call e6_foco("ichika", "sonriendo")

    ichika "No era otra persona. Eso es lo que todavía no me creo."

    ichika "Tú lo viste antes que yo, [mc]. En la sala de ensayo."

    ichika "…Eso tampoco me lo creo."

    narrador "Ni un chiste. Ni una máscara. Solo lo que había pasado."

    return


label e6_ichika_tarde_tibia:

    call e6_foco("ichika", "sonriendo")

    ichika "¡El profesor me pilló sonriéndole a la hoja! Le dije que era una técnica."

    call e6_foco("ichika", "neutral")

    ichika "Lo resolví rápido, eso sí."

    ichika "Lo que no sé es si… No tengo que po—"

    call e6_foco("ichika", "sonriendo")

    ichika "¡Olvídalo! Una línea de ensayo. Se me cuelan."

    narrador "Se rió antes que nadie. Para que nadie tuviera tiempo de preguntar."

    return


label e6_ichika_tarde_fria:

    call e6_foco("ichika", "sonriendo")

    ichika "Resolví todo sin un tachón. Aproveché el tiempo, tal cual."

    ichika "Y no, no estoy cansada. Por si alguien iba a preguntar."

    narrador "Nadie iba a preguntar. Ella lo sabía. Lo dijo igual."

    return


label e6_ichika_tarde_no_visitada:

    call e6_foco("ichika", "neutral")

    ichika "Hice el examen con una mano y ensayé con la otra. Debajo del pupitre."

    call e6_foco("ichika", "sonriendo")

    ichika "Una pregunta, una línea. ¡Multitarea de actriz!"

    call e6_foco("ichika", "neutral")

    ichika "…Salieron las dos bien, creo. No sé cuál de las dos era yo."

    mc "Yo vi a alguien resolviendo problemas de trenes."

    ichika "…Ah. Esa."

    narrador "No sonrió para nadie. Fue una sonrisa pequeña, de las que no se ensayan."

    return


##  Espejo B4: «Va a pasar lo que dije.» / MC: «Te vi quedarte hasta la campana.»
##  Cálida: se fue sin hacer guardia, y no se corta al hablar.

label e6_nino_tarde_calida:

    call e6_foco("nino", "neutral")

    nino "Terminé mi examen a los quince minutos. Y me fui."

    nino "Sin vigilar a ninguna de mis hermanas. Sin quedarme de guardia."

    nino "No sé cómo les fue. Por primera vez, no necesité saberlo antes."

    mc "Te vi salir."

    call e6_foco("nino", "pillada")

    nino "…No sé de qué hablas."

    narrador "Lo dijo como siempre. Esta vez no le salió la mentira, y no intentó arreglarla."

    return


label e6_nino_tarde_tibia:

    call e6_foco("nino", "neutral")

    nino "El miércoles terminé antes que casi todas. Me quedé revisando."

    mc "Te vi quedarte hasta la campana."

    nino "Había un «has» que tenía que ser «have». Hay que revisar."

    nino "Si aprobamos las cinco… quizás esta vez no—"

    call e6_foco("nino", "molesta")

    nino "Olvídalo. Da igual."

    return


label e6_nino_tarde_fria:

    call e6_foco("nino", "molesta")

    nino "Revisé hasta la campana. Hoja por hoja."

    nino "No por ellas. Por si acaso. Siempre hay un examen siguiente."

    mc "Te vi quedarte."

    nino "Pues mira a otra."

    nino "¿Por qué te fijas en mí?"

    return


label e6_nino_tarde_no_visitada:

    call e6_foco("nino", "neutral")

    nino "Revisé cuarenta minutos mi examen."

    nino "A la media hora levanté la vista."

    nino "Seguías en tu sitio. Eso es todo."

    mc "Seguía."

    call e6_foco("nino", "molesta")

    nino "No te lo estoy agradeciendo. Solo te lo estoy recalcando."

    return


##  Espejo B4: «Te pedí que no me ayudaras. Y no lo hiciste. No sé qué es peor.»

label e6_itsuki_tarde_calida:

    call e6_foco("itsuki", "neutral")

    if it1_frase() == "A":

        itsuki "Ayer levanté la mano. En un examen. Delante de toda la clase."

        itsuki "Le pedí al profesor que repitiera un enunciado."

        itsuki "Nada más. Con eso bastó."

    else:

        itsuki "Ayer encontré el error sola."

        itsuki "Tardé el doble, pero lo encontré."

        itsuki "Antes de encontrarlo pensé en levantar la mano."

        itsuki "Lo pensé. Eso es nuevo. Me ganó mi orgullo."

    call e6_foco("itsuki", "timida")

    itsuki "Que conste: no fue un favor. Fue un procedimiento."

    narrador "Terminó la oración con su punto."

    narrador "Firme. Esta vez no se le quedó nada colgando."

    return


label e6_itsuki_tarde_tibia:

    call e6_foco("itsuki", "neutral")

    itsuki "La cuarta la reescribí dos veces. Entregué casi terminando la hora."

    itsuki "Podría haber preguntado. Preguntar sería—"

    narrador "Se detuvo. La oración se quedó a medio camino."

    itsuki "…Lo revisé sola. Y salió."

    return


label e6_itsuki_tarde_fria:

    call e6_foco("itsuki", "molesta")

    itsuki "Resolví sola. Cada paso. Sin preguntar a nadie."

    itsuki "No necesitaba ayuda. El examen lo demuestra."

    narrador "Lo dijo sin mirarme. Pero lo dijo hacia mí."

    return


label e6_itsuki_tarde_no_visitada:

    call e6_foco("itsuki", "neutral")

    itsuki "Entregué pasada la hora. La cuarta, recién resuelta."

    itsuki "Tarde. Pero todo lo hice yo."

    itsuki "…Si alguien me hubiera dicho dónde mirar, habría llegado a tiempo."

    mc "Itsuki…"

    itsuki "No lo digo por ti. Lo digo porque es verdad."

    return


##  Espejo B4: «Sabía las respuestas. Las escribí. Las borré. Perdón.»
##  Cálida: primera vez que habla EN VOZ ALTA sin «…» ni «perdón» (su cambio es de hoy).

label e6_miku_tarde_calida:

    narrador "Miku se tocó los audífonos una vez, sin subirlos."

    call e6_foco("miku", "animada")

    miku "Escribí todo lo que sabía."

    narrador "Las cuatro giraron la cabeza a la vez."

    narrador "La miraron sorprendidas. Como si algo hubiera cambiado en ella."

    narrador "Y claro. Lo había dicho de corrido."

    narrador "Sin el silencio de siempre delante. Sin «perdón» detrás."

    miku "La pregunta tres. Escribí de la sal, hasta el último renglón."

    miku "La goma está entera. Miren. Sin desgastarse."

    narrador "La sacó del estuche y la dejó sobre el pupitre. Las cuatro esquinas, sin usar."

    call e6_foco("miku", "encogida")

    miku "…Eso fue raro. …Pero no retiro lo que dije."

    return


label e6_miku_tarde_tibia:

    call e6_foco("miku", "neutral")

    miku "…Escribí lo de las rutas. …Sin la sal."

    miku "…Se me daba bien. …Eso me dijeron."

    miku "…No borré nada. …Solo paré antes."

    miku "…Lo que amo no—"

    call e6_foco("miku", "encogida")

    miku "…Nada. …Perdón."

    return


label e6_miku_tarde_fria:

    narrador "Miku tenía la mano en los audífonos. No la había bajado desde la mitad del examen."

    call e6_foco("miku", "neutral")

    miku "…Cuatro renglones. …Lo que preguntaban."

    miku "…Correcto. …Lo comprobé."

    narrador "No dijo nada más. La mano siguió donde estaba."

    return


label e6_miku_tarde_no_visitada:

    call e6_foco("miku", "neutral")

    miku "…Escribí largo. …Después borré un poco."

    miku "…Quedaron tres líneas. …Las de no molestar."

    call e6_foco("miku", "encogida")

    miku "…Perdón. …No quería que sonara triste."

    mc "No sonó triste."

    miku "…Mientes un poco."

    miku "…Gracias igual."

    return


## --- «¿Y a ti cómo te fue?»: quién pregunta ----------------------------------------
##  Itsuki si fue cálida (su cambio es preguntar). Si no, Yotsuba, salvo que esté
##  fría (dejó de mirar a los demás). Si no, Ichika. Nunca hay dos frías.

label e6_tarde_pregunta:

    if e6_estado_de("itsuki") == "calida":

        call e6_foco("itsuki", "neutral")

        itsuki "Falta un resultado. ¿Y a ti cómo te fue?"

        narrador "Lo preguntó sin rodeos."

        narrador "Itsuki, que prefería equivocarse sola antes que preguntar."

    elif e6_estado_de("yotsuba") != "fria":

        call e6_foco("yotsuba", "sorprendida")

        yotsuba "¡Espera! ¡Falta uno! ¿Y a ti cómo te fue, [mc]?"

        narrador "Yotsuba, siempre la primera en incluir a todas."

        narrador "Hasta al que nunca entraba en la cuenta: yo."

    else:

        call e6_foco("ichika", "neutral")

        ichika "Falta alguien, ¿no?"

        ichika "¿Y a ti cómo te fue, tutor?"

        narrador "Lo preguntó como hermana mayor. Por costumbre de contar a todos."

    call e6_foco("", "")

    return


## --- La puerta (salida). Nino, según su estado ------------------------------------

label e6_nino_puerta_calida:

    show nino neutral at pj_habla(X_NINO)
    with dissolve

    narrador "Nino ya estaba en la puerta, sujetándola abierta con la espalda."

    nino "Sal, [mc]. Si no sales tú, aquí no sale nadie."

    narrador "Era la primera vez que decía mi nombre. Lo dijo como una orden."

    mc_pensamiento "Supongo que, con ella, es lo mismo."

    narrador "Esperó a que estuviera a su lado. Cruzamos la puerta juntos."

    mc_pensamiento "Y al mismo tiempo."

    mc_pensamiento "Lo había calculado. Pero no lo iba a admitir nunca."

    hide nino
    with dissolve

    return


label e6_nino_puerta_tibia:

    show nino neutral at pj_habla(X_NINO)
    with dissolve

    narrador "Nino sujetaba la puerta con una mano y miraba al pasillo."

    nino "No te estoy esperando. Estoy sujetando una puerta."

    narrador "Una puerta con tope en el suelo. Se sujeta sola."

    narrador "Salió cuando salí yo. Ni un paso antes."

    hide nino
    with dissolve

    return


label e6_nino_puerta_fria:

    show nino molesta at pj_habla(X_NINO)
    with dissolve

    narrador "Nino esperaba en el pasillo, con los brazos cruzados."

    nino "Has tardado."

    mc "¿Me esperabas?"

    nino "Esperaba a que salieras para cerrar."

    play sound audio.sfx_puerta_cierra volume 1.0

    narrador "Cerró detrás de mí. Despacio."

    narrador "Como se cierra algo que todavía no ha terminado."

    hide nino
    with dissolve

    return


label e6_nino_puerta_no_visitada:

    show nino neutral at pj_habla(X_NINO)
    with dissolve

    narrador "Nino estaba junto a la puerta, con la mano en el picaporte."

    nino "Siempre salgo última. Para cerrar."

    nino "Hoy que la cierre el viento."

    narrador "Salimos a la vez."

    narrador "La puerta se quedó abierta detrás de nosotros."

    hide nino
    with dissolve

    return


################################################################################
##  MOV. 8 · RESULTADOS Y MARUO
################################################################################

label e6_resultados:

    $ ui_escena("normal")
    $ e6_limpiar()

    stop ambiente fadeout 1.0

    scene bg_negro
    with fade_dia

    narrador "Sábado a media mañana."

    narrador "Estaba en mi casa, repasando todo lo que sucedió esta semana."

    narrador "Una semana totalmente diferente a las mismas de siempre."

    mc_pensamiento "No hacía nada más que pensar en los resultados de los exámenes."

    mc_pensamiento "No los míos, los de ellas."

    narrador "Sin embargo, el tiempo de espera duró poco."

    play sound audio.sfx_celular volume 1.5

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
##  MOV. 9 · LAS CINCO (puertas → intento → mesa → foto)
##  Ecos por hermana justo debajo de e6_cinco, en orden Yotsuba, Ichika,
##  Nino, Itsuki, Miku (el orden en que entran lo decide e6_orden_ecos()).
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


## --- Ecos de Yotsuba (Mov. 9). Entra ya en pj, neutral; termina en pj_calla ----------

label e6_yotsuba_eco_calida:

    narrador "Yotsuba llevaba el boletín boca abajo en una mano y el rotulador destapado en la otra."

    call e6_foco("yotsuba", "neutral")

    yotsuba "Dame la muñeca. El uno se borró hace días."

    narrador "Escribió un uno. Y detrás, sin pedir permiso, dos ceros."

    yotsuba "Empecé en el uno por ciento. Todavía no sé dónde estoy. Pero ya cabe."

    call e6_foco("yotsuba", "sonriendo")

    yotsuba "¡Esta vez sin corazón torcido!"

    call e6_foco("yotsuba", "incomoda")

    yotsuba "…Todavía no me sale recto. Lo estoy practicando."

    narrador "No dijo para cuándo. Tapó el rotulador y se fue a su sitio."

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


## --- Ecos de Ichika (Mov. 9) ----------------------------------------------------------

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

    ichika "Me salen las tres de siempre. Y ninguna sirve para esto."

    mc "Hoy no necesitas ninguna."

    call e6_foco("ichika", "sonriendo")

    ichika "¡Qué amable! …Esa fue la graciosa. Perdona el reflejo."

    call e6_foco("", "")

    return


## --- Ecos de Nino (Mov. 9). Entra ya en pj, neutral (lo hace e6_cinco) -----------

label e6_nino_eco_calida:

    narrador "Nino llegó con el boletín doblado en cuatro y con su cara en alto. Casi toda."

    call e6_foco("nino", "neutral")

    nino "El último duró cuatro días. Tú llevas treinta y cinco."

    mc "…"

    nino "No me mires así. Son cálculos."

    call e6_foco("nino", "pillada")

    nino "Y que no se entere Yotsuba de que llevaba la cuenta."

    nino "Haría un cartel."

    call e6_foco("", "")

    return


label e6_nino_eco_tibia:

    narrador "Nino llegó con una bolsa del supermercado en cada mano, como si el boletín fuera lo de menos."

    call e6_foco("nino", "neutral")

    nino "Pesa. No te estoy pidiendo ayuda."

    mc "Entendido."

    nino "…Esta pesa más de lo que parece."

    narrador "Dejó la bolsa más pesada en mi brazo sin mirarme, y se llevó la otra."

    narrador "Ninguno dijo nada más."

    call e6_foco("", "")

    return


label e6_nino_eco_fria:

    narrador "Nino se detuvo a dos pasos de mí, con el boletín boca abajo contra el costado."

    narrador "Ni cerca ni lejos."

    call e6_foco("nino", "molesta")

    nino "Sigues aquí."

    mc "Sigo."

    nino "Pues anota la fecha. Para cuando te canses."

    narrador "Lo dijo sin rabia. Como quien deja una nota pegada en la nevera."

    narrador "Sabe que voy a seguir con el trabajo."

    call e6_foco("nino", "neutral")

    call e6_foco("", "")

    return


label e6_nino_eco_no_visitada:

    narrador "Nino se quedó junto al marco de la puerta, a media sala, como quien no ha decidido si entra."

    call e6_foco("nino", "neutral")

    nino "No me mires como si me debieras algo."

    nino "No viniste a buscarme. Está bien."

    nino "Alguien tenía que ser a la que no iban a buscar."

    nino "Y fui yo. La que siempre ve venir el golpe antes que nadie."

    nino "…Eso sonó mejor en mi cabeza."

    mc "Sonó bien."

    nino "No te pedí opinión de crítico."

    nino "Treinta y cinco días no hacen un avance."

    call e6_foco("", "")

    return


## --- Ecos de Itsuki (Mov. 9). Terminan antes del intento de disculpa ---------------

label e6_itsuki_eco_calida:

    narrador "Itsuki llegó con el bolígrafo del examen todavía en la mano."

    narrador "Se le había olvidado soltarlo."

    call e6_foco("itsuki", "sonriendo")

    itsuki "Dije que el juego se acabó. No dije quién ganó."

    mc "¿Y quién ganó?"

    itsuki "Eso no se pregunta, [mc]."

    if it1_frase() == "A":

        itsuki "Levanté la mano en un examen. Es un informe, no una invitación a aplaudir."

    else:

        itsuki "No levanté la mano. Pero ya sé que puedo. Es un informe, no una invitación a aplaudir."

    narrador "Dijo mi nombre como quien firma al pie de un informe."

    narrador "Y aun así tardó en soltar el bolígrafo."

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

    itsuki "Dije que el juego se acabó, y gané."

    itsuki "Es lo único que siempre me sale bien."

    mc "No sabía que había premio."

    itsuki "No lo hay. …Por eso es lo único que me sale."

    narrador "Lo dijo con la oración cerrada y terminada."

    narrador "Pero no sonó a victoria."

    call e6_foco("", "")

    return


## --- Ecos de Miku (Mov. 9) --------------------------------------------------------

label e6_miku_eco_calida:

    narrador "Miku llegó con los audífonos al cuello, sin tocarlos, y el boletín en las dos manos."

    call e6_foco("miku", "neutral")

    miku "La página ciento veinte. ¿Llegaste?"

    mc "Ciento veintidós."

    call e6_foco("miku", "relajada")

    narrador "Se rió. Una sola nota, corta, como un acorde."

    miku "Quería ver tu cara. Ya la vi."

    miku "Gracias, [mc]."

    call e6_foco("", "")

    return


label e6_miku_eco_tibia:

    narrador "Miku tomó su boletín con el cuadernillo de preguntas todavía doblado bajo el brazo."

    call e6_foco("miku", "encogida")

    miku "…Dijiste que se me daba bien."

    miku "…Todavía estoy pensando qué querías decir con eso."

    mc "Lo que dije."

    miku "…Puede ser. …Lo sigo pensando."

    call e6_foco("", "")

    return


label e6_miku_eco_fria:

    narrador "Miku llegó con los audífonos puestos."

    narrador "Esta vez sonaban: se oían desde la puerta."

    call e6_foco("miku", "neutral")

    miku "…Contesté lo que entraba. …Estuvo bien."

    miku "…Hoy no."

    narrador "No dijo a qué. No hizo falta."

    call e6_foco("", "")

    return


label e6_miku_eco_no_visitada:

    narrador "Miku se detuvo en la puerta con el boletín contra el pecho, como se lleva un libro."

    call e6_foco("miku", "neutral")

    miku "…La silla sigue vacía. …No es un reproche. …Solo está ahí."

    mc "Lo sé."

    miku "…Dejaré el libro abierto otra vez. …Por si acaso."

    miku "…Alguien viene."

    call e6_foco("", "")

    return


## --- El intento interrumpido (la disculpa NO se gasta) ----------------------------
label e6_intento:

    narrador "Éramos seis en la sala, y por primera vez nadie parecía estar aquí por obligación."

    narrador "La primera en querer hablar fue ella, Itsuki."

    narrador "Itsuki dio un paso hacia mí. Yo, sin proponérmelo, di otro hacia ella."

    narrador "Aún había cosas pendientes que teníamos que resolver."

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

    call e6_foco("itsuki", "timida")

    itsuki "…Queda pendiente."

    itsuki "Esta vez sí lo anoto."

    narrador "Lo dijo sin mirarme. Pero se le habían puesto rojas las orejas."

    call e6_foco("", "")

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

    nino "Hace un mes no habría apostado a vernos a los seis en esta mesa."

    nino "…Es una observación. No le des importancia."

    call e6_foco("miku", "encogida")

    if e6_estado_de("miku") == "fria":

        narrador "Miku se bajó los audífonos al cuello antes de sentarse. La música se cortó a medio compás."

        miku "…Hoy me los quito."

    else:

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

    yotsuba "¡¡Entonces abrámoslos ya!!"

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

    narrador "Le corrió una lágrima por la cara. No se la secó."

    miku "…No es tristeza. …Es que no sé dónde poner esto."

    call e6_foco("ichika", "sonriendo")

    narrador "Ichika soltó una risa corta, de las que se escapan solas."

    ichika "Ja. …Ja, ja. …Me quedé sin chiste. A mí, que siempre tengo uno."

    ichika "Tantas noches cortas. …Y valieron cada minuto."

    ichika "Eso no venía en el guion."

    call e6_foco("nino", "nerviosa")

    narrador "Nino leyó el suyo. Luego, uno por uno, los de las demás."

    narrador "Movía los labios sin sonido."

    nino "Uno. Dos. Tres. Cuatro. …Cinco."

    nino "Cinco. Los conté dos veces."

    nino "…Que nadie diga nada. Si alguien dice algo, me voy."

    narrador "Se le quebró la voz en la última palabra. Nadie dijo nada. Nino se quedó."

    call e6_foco("yotsuba", "sonriendo")

    narrador "Yotsuba ni miró el suyo. Miraba los de las demás, uno por uno, con los ojos muy abiertos."

    yotsuba "¡Todas! ¡¡Todas, todas, todas!!"

    yotsuba "¡¡Miku, mira el tuyo!! ¡¡Nino, el tuyo!!"

    ichika "Yotsuba. El tuyo."

    yotsuba "¿Eh? …¡Ah, el mío!"

    call e6_foco("yotsuba", "neutral")

    narrador "Bajó la vista. Y, por primera vez en todo el mes, Yotsuba se quedó callada."

    yotsuba "…Este es mi boletín. …Esta soy yo. …Esto lo hice yo."

    call e6_foco("yotsuba", "sonriendo")

    yotsuba "¡¡Y lo hicimos todas!! ¡¡Y tú también, [mc]!!"

    if e6_estado_de("yotsuba") == "fria":

        narrador "Me llamó por mi nombre. Desde la pista no lo había vuelto a hacer."

    yotsuba "¡Tú te quedaste hasta el último momento! ¡Eso también cuenta!"

    call e6_foco("itsuki", "sonriendo")

    narrador "Itsuki lo leyó línea por línea, como se lee un contrato. Dos veces, tal como había propuesto."

    itsuki "Lo leí dos veces. …El resultado no cambió."

    itsuki "Debería decir algo acorde al momento. Algo con sujeto, verbo y—"

    narrador "No le salió el punto. Por una vez, no pareció importarle."

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

    miku "…A tu manera… Fue lindo."

    miku "…Gracias por tus palabras, [mc]."

    call e6_foco("itsuki", "neutral")

    itsuki "Breve. Aceptable. Bien dicho."

    mc_pensamiento "Hace un mes se pusieron de acuerdo para fallar igual."

    mc_pensamiento "Hoy se pusieron de acuerdo para mostrarse distintas."

    play music main_theme fadein 2.0

    call e6_foco("yotsuba", "sonriendo")

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

    play audio audio.sfx_camara volume 1.5

    narrador "Tomé la foto. Ninguna bajó el boletín."

    ichika "¿Ya está? …Me tiembla el brazo y no pienso ser la primera en bajarlo."

    nino "Yo tampoco. …Que baje primero Yotsuba."

    yotsuba "¡Yo no bajo nada! ¡Puedo quedarme así hasta mañana!"

    itsuki "Los brazos no funcionan así. Tarde o temprano se cansan."

    yotsuba "¡Pues que se cansen tarde!"

    miku "…Yo tampoco quiero bajar las manos todavía. …Mientras sigamos así, …esto sigue pasando."

    narrador "Nadie se rio. Se quedaron un momento en silencio, juntas, cada una en su sitio, con la hoja en alto."

    mc_pensamiento "Pensé en decirles que la foto ya estaba. No lo dije. Hay cosas que un «ya está» arruina."

    ichika "Oigan. ¿Les confieso algo?"

    ichika "…Esta mañana tenía miedo de abrirlo sola. Y no estaba sola."

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
##  MOV. 10 · CASA
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

    mc_pensamiento "Mi hermana Raiha. La primera que dijo que yo podía con las cinco."

    mc_pensamiento "Una de las razones por las que acepté el trabajo cuando no sabía qué decidir."

    narrador "El curry se olía por toda la casa."

    show raiha hablando at pj_habla(0.20)
    show isanari neutral at pj_calla(0.73)
    with dissolve

    raiha "¡Hermanito! Hice curry antes de saber cómo te iba a ir."

    raiha "Así, como te haya ido, la cena ya está hecha. ¡El curry nunca falla!"

    mc "Pues hoy comeremos un banquete, ¿no crees, Raiha?"

    mc "¡¡Aprobaron las cinco!!"

    raiha "…¿Las cinco?"

    mc "Las cinco."

    raiha "¡¡LAS CINCO!!"

    raiha "¡Te dije que podías con cinco a la vez!"

    mc "Me lo dijiste con voz de «ojalá»."

    mc "Aunque te perdono porque también dudaba de mí en ese momento."

    raiha "¡Pero la voz de «ojalá» también cuenta!"

    show raiha hablando at pj_calla(0.20)
    show isanari neutral at pj_habla(0.73)
    with disolucion_lenta

    isanari "[mc], veo que hoy ha sido todo un éxito para ti."

    isanari "Maruo llamó. Cobramos el mes entero."

    mc "Lo sé."

    isanari "Pareces menos contento de lo que dice el pago."

    mc "No estoy menos contento. Estoy pensando en otra cosa."

    isanari "¿Qué cosa vale más que cinco veces la tarifa?"

    mc "Todavía no lo sé."

    narrador "Mi padre no contestó."

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
##  MOV. 11 · CUARTO, CHAT Y LIBRETA
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

    mc_pensamiento "Japonés, matemáticas, inglés, ciencias, sociales. Cien, cien, cien, cien, cien."

    $ e6_boletin_fase = 2

    mc_pensamiento "Cinco notas perfectas en cinco materias distintas. Esa diagonal lo delata."

    mc_pensamiento "Un boletín perfecto. De un alumno que no existe."

    $ e6_boletin_fase = 3

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

    mc_pensamiento "Dos promesas hechas sin que nadie me las pidiera."

    mc_pensamiento "Esas no caducan. Se cumplen."

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
##  MOV. 12 · EL RETRATO (EPÍLOGO DEL CAPÍTULO 1)
##  Espejo de la Escena 1 del prólogo: mismas tres líneas sobre negro, «hogar»
##  sobre silencio y cg_familia. Contesta a «dos clases de personas» y a
##  «Me permití el lujo de equivocarme. Y salió caro» (Final B). Guion general:
##  el estado de entrada ya ramificó en S3. Único menú del E6: el domingo.
##  Sin puntos. Escribe e6_domingo (y e6_domingo_hermana) para el Cap. 2.
################################################################################

label e6_retrato:

    $ ui_escena("normal")

    ## El Mov. 11 termina en bg_negro y sin música: se entra sobre silencio.

    scene cg_calificacion
    with fade

    narrador "Hay dos clases de personas en este mundo."

    narrador "Las que pueden permitirse el lujo de equivocarse."

    narrador "Y las que no."

    mc_pensamiento "Hace un mes lo tenía clarísimo: yo pertenecía a la segunda."

    mc_pensamiento "Y siempre pensé que iba a pertenecer ahí."

    mc_pensamiento "Ahora, esa realidad ha cambiado, no del todo, pero ha cambiado."

    play music hogar fadein 3.0

    scene cg_familia
    with fade

    mc_pensamiento "La foto de siempre. La que miro cada noche sin mirarla de verdad."

    mc_pensamiento "La deuda sigue donde estaba. Un mes de sueldo no la borra: apenas la reduce."

    mc_pensamiento "Raiha sigue mereciendo un futuro mejor que este. Eso no cambió esta semana."

    mc_pensamiento "Sigo siendo de los que no pueden permitirse equivocarse."

    mc_pensamiento "Y aun así, este mes me equivoqué. Dos tardes que no fueron. Dos nombres esperando."

    mc_pensamiento "Pensé que lo pagaría caro. No lo pagué solo."

    mc_pensamiento "Cinco personas que tampoco podían fallar se sentaron conmigo en la misma semana."

    mc_pensamiento "Eso no viene en ningún libro: los que no pueden equivocarse no tienen por qué hacerlo solos."

    mc_pensamiento "Siempre dije que no estudiaba por vocación. Que eso era cosa de ceremonias."

    mc_pensamiento "Esta semana no abrí un libro mío. Pasé cinco días mirando estudiar a otras."

    mc_pensamiento "Y fue la semana en que más aprendí."

    mc_pensamiento "Si eso no es una vocación, no se que palabra podría definirla."

    ## --- Las dos fotos ----------------------------------------------------------------

    narrador "Tenía el celular en la otra mano. En el grupo, sobre los cinco boletines, estaba la foto de la tarde."

    if e6_estado_entrada == "superado":
        scene cg_cinco_aprobadas at e6_tinte_superado
        with dissolve
    elif e6_estado_entrada == "bueno":
        scene cg_cinco_aprobadas at e6_tinte_bueno
        with dissolve
    else:
        scene cg_cinco_aprobadas at e6_tinte_mixto
        with dissolve

    mc_pensamiento "Cinco boletines en alto. Cinco caras que ya no fingían nada."

    mc_pensamiento "Y yo en ninguna parte. Detrás del celular, que es donde estuve todo el mes."

    scene cg_familia
    with disolucion_lenta

    mc_pensamiento "Dos fotos. Una guarda a alguien que ya no está."

    mc_pensamiento "La otra deja fuera a alguien que estuvo ahí todo el tiempo. Yo."

    mc_pensamiento "Yotsuba dijo que salgo en la próxima."

    mc_pensamiento "Hasta hoy, las fotos eran para recordar lo que perdí."

    mc_pensamiento "Esta es la primera que me hace pensar en la siguiente."

    ## --- Raiha y el domingo -------------------------------------------------------------

    play sound audio.sfx_toque_puerta volume 1.0

    scene bg_cuarto_mc
    with dissolve

    show raiha hablando at pj_habla(0.5)
    with dissolve

    raiha "Hermanito, ¿sigues despierto? Tienes la luz encendida."

    raiha "¿Qué miras? …¿Esas son las quintillizas?"

    raiha "¡Son iguales! ¿Cómo las distingues?"

    mc "No se parecen en nada."

    show raiha regano at pj_habla(0.5)
    with disolucion_lenta

    raiha "¡Hermanito, si tienen la misma cara!"

    mc "La misma cara. Nada más."

    show raiha hablando at pj_habla(0.5)
    with disolucion_lenta

    raiha "¿Y cuál es la de la pista? ¿La que me cae bien?"

    mc "La del lazo verde."

    if yotsuba_visitada_cap1:

        mc "Estaba justo donde dijiste."

    else:

        mc "Me esperó en esa pista varias tardes. Justo donde dijiste."

    raiha "¿¡Acerté!?"

    raiha "¡Te dije que siempre sirvo!"

    mc "Gracias, Raiha. Esta vez lo digo en serio."

    raiha "...Algún día quiero conocerla."

    narrador "Raiha se rió. Me miró un rato, como quien busca algo que no encuentra."

    raiha "Oye. Mañana es domingo."

    raiha "Tu primer domingo sin ningún examen que preparar."

    raiha "¿Qué vas a hacer?"

    menu:

        mc_pensamiento "¿Qué hago con un domingo libre?"

        "Llevar a Raiha a algún sitio.":

            $ e6_domingo = "raiha"

            mc "Te llevo a algún sitio. Tú eliges."

            raiha "¿¡De verdad!? ¿A cualquier sitio?"

            mc "A cualquiera que cueste menos de lo que estás pensando."

            raiha "¡Al acuario! …No, al parque."

            mc_pensamiento "El parque es gratis. Lo pensó antes que yo."

            mc "Dijiste acuario primero."

            raiha "¡¡Al acuario!!"

            mc_pensamiento "Para alguien a quien ya no le gustaban los peces, lo dijo muy rápido."

            mc_pensamiento "Hace un mes, el dinero de este trabajo ya estaba gastado antes de cobrarlo."

            mc_pensamiento "Mañana, una parte va a ser suya." 
            
            mc_pensamiento "Aunque sea una entrada de acuario."

        "Contestar al grupo.":

            $ e6_domingo = "grupo"

            mc "Primero, contestar un mensaje."

            raiha "¿A las cinco? ¡Hermanito, ya tienes amigas!"

            narrador "Escribí. Lo borré. Escribí otra cosa. La borré también."

            mc_pensamiento "Así se siente Miku, entonces."

            narrador "Al final mandé una sola línea: «¿Y la próxima foto, cuándo?»"

            play sound audio.sfx_celular volume 1.5

            narrador "El celular vibró cinco veces seguidas. No las leí."

            narrador "Ya sabía de quién era cada una."

        "Cumplir una promesa.":

            $ e6_domingo = "promesa"

            mc "Tengo algo pendiente. Dos cosas, en realidad."

            menu:

                mc_pensamiento "¿Por cuál empiezo?"

                "[e6_p1]":
                    $ e6_domingo_hermana = e6_promesas[0]

                "[e6_p2]":
                    $ e6_domingo_hermana = e6_promesas[1]

            raiha "¿Pendiente? ¿Con quién?"

            mc "Con alguien que me esperó. Y no fui."

            show raiha preocupada at pj_habla(0.5)
            with disolucion_lenta

            raiha "Entonces tienes que ir. Esperar es lo peor."

            narrador "Lo dijo como lo dice alguien que espera a su hermano cada noche con la cena hecha."

        "Dormir hasta tarde. Por una vez.":

            $ e6_domingo = "dormir"

            mc "Dormir. Hasta tarde."

            show raiha preocupada at pj_habla(0.5)
            with disolucion_lenta

            raiha "…¿Estás enfermo?"

            mc "Estoy cansado. Es distinto."

            raiha "Hermanito… Nunca te había oído decir eso."

            raiha "…Dormir también es importante."

            mc "Lo sé. Me lo dijiste tú."

            show raiha hablando at pj_habla(0.5)
            with disolucion_lenta

            raiha "¡Pues mañana no te despierto! …Salvo que haya curry."

    show raiha hablando at pj_habla(0.5)
    with disolucion_lenta

    raiha "Buenas noches, hermanito."

    raiha "Hoy pareces el de siempre."

    raiha "Pero sin la cara de estar haciendo cuentas."

    hide raiha
    with dissolve

    ## --- Isanari: el «gracias por la comida» del Mov. 10 ---------------------------

    show isanari neutral at pj_habla(0.5)
    with dissolve

    narrador "Mi padre se asomó a la puerta poco después. Miró la foto antes de mirarme a mí."

    isanari "En la cena dijiste «gracias por la comida»."

    mc "Lo digo siempre."

    show isanari sonriendo at pj_habla(0.5)
    with disolucion_lenta

    isanari "No así. Así lo decía tu madre."

    isanari "Como si de verdad estuviera dando las gracias por algo."

    narrador "No dijo nada más."

    narrador "Me dio las buenas noches."

    narrador "Y se retiró."

    mc_pensamiento "En la cena se quedó mirando su plato más tiempo del necesario."

    mc_pensamiento "Ahora sé por qué."

    hide isanari
    with dissolve

    ## --- La lámpara (espejo del prólogo y del Final B) ----------------------------

    scene cg_familia
    with disolucion_lenta

    narrador "Dejé el celular boca abajo, junto a la foto."

    narrador "Como se dejan los boletines antes de leerlos."

    narrador "Apagué la lámpara."

    mc_pensamiento "Hace un mes anoté cinco nombres y escribí que al día siguiente empezaba la verdadera batalla."

    mc_pensamiento "Mañana no empieza ninguna."

    mc_pensamiento "Mañana las cosas van a ser diferentes."

    mc_pensamiento "Empieza una nueva etapa."

    mc_pensamiento "Una nueva etapa de mi vida."

    stop music fadeout 4.0

    scene bg_negro
    with fade

    pause 1.0

    $ persistent.cap1_completado = True

    ## Tarjeta de fin: mismo formato que la del final malo, sobre negro y sin música.
    narrador "FIN DEL CAPÍTULO 1 · Un estudiante perfecto"

    return


## ============================= CAPÍTULO 2 ======================================
## Stub de salida. BORRAR cuando exista 03_capitulo2.rpy (label duplicado).
label cap2_inicio:
    narrador "[[STUB cap2_inicio · Capítulo 2 pendiente]"
    return
