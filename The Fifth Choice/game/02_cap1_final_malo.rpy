################################################################################
##  CGs PROPIOS DEL FINAL MALO CON SUS 2 VARIANTES
##  A: Es únicamente un nuevo CG, es el de Maruo dandole la espalda a mc y
##     retirandose, este CG se reusa en ambos finales del juego
##  B: Son 5 CGs nuevos, cada 1 de cada quintilliza, todas han fracasado en sus
##  examenes, cada CG muestra la faceta de fracaso de cada hermana.
################################################################################

image cg_maruo_espaldas = "images/cg/cap1_final_malo/maruo_espaldas.webp"

image cg_ichika_fracaso = "images/cg/cap1_final_malo/ichika_fracaso.webp"

image cg_nino_fracaso = "images/cg/cap1_final_malo/nino_fracaso.webp"

image cg_miku_fracaso = "images/cg/cap1_final_malo/miku_fracaso.webp"

image cg_yotsuba_fracaso = "images/cg/cap1_final_malo/yotsuba_fracaso.webp"

image cg_itsuki_fracaso = "images/cg/cap1_final_malo/itsuki_fracaso.webp"

############################################################################
##  DESPIDO TRAS BEAT 2
##  Despido directo en el beat (Cocina): Maruo despide al MC de forma 
##  inmediata y fría tras una fuerte discusión, provocando la profunda 
############################################################################

label final_malo_beat:

    ############################################################################
    ##  MOVIMIENTO 1 · Maruo
    ##  Maruo se dirige a mc de una manera tensa y fría, mc ya sabe que su
    ##  despido está asegurado, solo falta la sentencia final de Maruo.
    ############################################################################

    scene cg_nino_confrontacion_cocina
    with dissolve

    stop music fadeout 1.0

    narrador "Fue entonces cuando Maruo levantó la vista y me encontró en la puerta."

    scene cg_maruo_reunion
    with corte_seco
    
    play music contrato fadein 2.0

    maruo "Qué oportuno."

    mc "Buenas tardes."

    mc "Disculpe, no venía a interrumpirlos. Yo solo..."

    maruo "Ya que estás aquí, me ahorras la llamada."

    play sound audio.sfx_taza_mesa volume 1.0

    narrador "Dejó la taza sobre la mesa, despacio."

    maruo "Mañana no vengas."

    mc "...¿Perdón?"

    maruo "El contrato queda terminado. Tu padre cobrará lo trabajado hasta hoy."

    mc "Señor, todavía quedan semanas. Si me deja explicarle..."

    scene cg_maruo_espaldas
    with corte_seco

    maruo "No hay nada que explicar."

    maruo "Anoche revisé sus cuadernos. Los cinco."

    maruo "Muchas tardes con mis hijas, y ninguna está más cerca de aprobar que el primer día."

    maruo "Las condiciones las sabías desde el principio."

    mc "Por favor, solo un..."

    maruo "No."

    narrador "No levantó la voz. Nunca la levanta."

    narrador "Eso fue lo peor. Ni siquiera sonaba enfadado. Sonaba igual."

    narrador "Nino miraba entre los dos. Quiso decir algo."

    narrador "Pero no lo dijo."
    
    play sound audio.sfx_puerta_cierra volume 1.0
    
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
    with dissolve
    
    show nino neutral at pj_habla(0.5)
    with dissolve

    if rama_de("nino") == "fria":

        nino "Me dijiste que ibas a durar."

        nino "..."

        nino "Ya ves."

    narrador "Nino no se movió. Seguía con las manos apoyadas en la mesa."

    narrador "Hacía un minuto me quería fuera. Ahora me tenía fuera."

    nino "..."

    nino "Bueno."

    mc "¿«Bueno»? ¿Y así nomás?"

    nino "Era lo que pedí. ¿Qué esperabas? ¿Que me pusiera a llorar por ti?"

    narrador "Lo dijo con esa mirada fría, como siempre."

    narrador "Pero la frase le tardó medio segundo de más en salir."

    nino "El último duró cuatro días. Tú aguantaste más."

    nino "No es un cumplido."

    nino "Aunque sí deberías sentirte orgulloso."

    mc_pensamiento "Tenía que sentirse como ganar. Ella lo sabía. Yo lo sabía."

    mc_pensamiento "Y tenía la cara de quien consigue justo lo que pidió."

    mc_pensamiento "Pero sin un sabor de victoria."

    nino "Es mejor así. Hoy. Antes de que se ilusionen más."

    mc "Nino..."

    nino "Y no me mires con esa cara de pena. No te va a servir de nada."

    ############################################################################
    ##  MOVIMIENTO 3 · Las cuatro
    ##  Luego de la discusión, las cuatro hermanas restantes llegan y se
    ##  enteran de lo sucedido, saben que el despido de mc se veía venir, por
    ##  eso no tienen igualmente sentimiento de culpa.
    ############################################################################

    play sound audio.sfx_puerta_abre volume 1.0

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
    
    yotsuba "¿Quién gritaba? ¿Fue...?"

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

    itsuki "...¿Hoy?"

    show itsuki at pj_calla(X_ITSUKI)
    show nino neutral at pj_habla(X_NINO)
    with disolucion_lenta

    nino "Hoy. Hace cinco minutos."

    show nino neutral at pj_calla(X_NINO)   
    show ichika sonriendo at pj_habla(X_ICHIKA)
    with disolucion_lenta

    ichika "Bueno... al menos fue rápido. ¿No?"

    narrador "Nadie se rió. Ni ella."

    show ichika neutral at pj_habla(X_ICHIKA)
    with disolucion_lenta

    ichika "...Perdón. Es lo que hago cuando no sé qué decir."

    ichika "No te voy a defender, [mc]. No sabría con qué."

    if rama_de("ichika") == "fria":

        ichika "Fuiste correcto conmigo. Como un padre."

        ichika "Y yo te contesté como se contesta a un padre: sonriendo." 
        
        ichika "No sirvió de nada."


    show ichika neutral at pj_calla(X_ICHIKA)
    show yotsuba incomoda at pj_habla(X_YOTSUBA)
    with disolucion_lenta

    yotsuba "Pero si él... él solo estaba..."

    show nino neutral at pj_habla(X_NINO)
    show yotsuba incomoda at pj_calla(X_YOTSUBA)
    with disolucion_lenta

    nino "Yotsuba."

    show nino neutral at pj_calla(X_NINO)
    show yotsuba incomoda at pj_habla(X_YOTSUBA)
    with disolucion_lenta

    yotsuba "...No dije nada."

    narrador "Se quedó mirando el suelo, con las manos juntas delante."

    if rama_de("yotsuba") == "fria":

        narrador "Después, me miró a mí."

        show yotsuba neutral at pj_habla(X_YOTSUBA)
        with disolucion_lenta

        yotsuba "Me dijiste que me concentrara en correr."

        yotsuba "Dejé de contar en voz alta. Pensé que así servía más."

        yotsuba "Ahora no sé si servía de algo."


    show yotsuba at pj_calla(X_YOTSUBA)
    show miku neutral at pj_habla(X_MIKU)
    with disolucion_lenta

    miku "...Yo no pedí esto."

    miku "...Tampoco lo evité."

    narrador "Se llevó las manos a los audífonos." 
    
    narrador "No se los subió. Los dejó ahí, apoyadas."

    if rama_de("miku") == "fria":

        show miku encogida at pj_habla(X_MIKU)
        with disolucion_lenta

        miku "...Dijiste que lo de la sal no entraba en el examen."

        miku "...Tenías razón."

        miku "...Por eso no volví a abrir el libro."

    show miku at pj_calla(X_MIKU)
    show itsuki at pj_habla(X_ITSUKI)
    with disolucion_lenta

    itsuki "Te lo dije el primer día. Esto no iba a funcionar."

    itsuki "Ahora lo tengo confirmado. No me hace ninguna gracia."

    if "itsuki" in hub_visitadas:

        if rama_de("itsuki") == "fria":

            itsuki "Me quitaste el cuaderno de las manos."

            itsuki "Me lo resolviste delante de mí."

            itsuki "Eso no se me va a olvidar."

        elif rama_de("itsuki") == "calida":

            itsuki "Me dijiste dónde mirar. Una vez."

            itsuki "Pensé que habría una segunda."

        elif rama_de("itsuki") == "tibia":

            itsuki "Me ofreciste revisarlo desde el principio. Te dije que no."

            itsuki "Ahora no voy a saber qué ibas a explicarme."

    play music derrota fadein 2.5

    narrador "Intenté decir algo. Itsuki lo notó antes que yo."

    itsuki "No lo digas." 
    
    itsuki "Un «lo siento» ahora sería para ti, no para nosotras."

    narrador "Me quedé callado. No tenía otra cosa que hacer."

    mc_pensamiento "Itsuki tenía razón. Otra vez."

    narrador "Recogí mi mochila. Nadie me detuvo."

    narrador "Tampoco nadie me acompañó hasta la puerta."

    play sound audio.sfx_puerta_cierra volume 1.0

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

    show raiha preocupada at pj_habla(0.20)
    with disolucion_lenta

    raiha "Hermanito... ¿Te encuentras bien?"

    mc "Discúlpame, Raiha."

    mc "Me despidieron."

    raiha "...¿Qué?"

    isanari "¿Quién?"

    mc "Maruo. Hoy."

    isanari "¿Y el mes? ¿Te pagó lo trabajado?"

    mc "Dijo que sí."

    show raiha regano at pj(0.20)
    with disolucion_lenta

    raiha "¡Papá!"

    raiha "¡Primero mírale la cara!"

    isanari "..."

    narrador "Mi papá intentó decir algo. No contestó."

    narrador "Se acomodó las gafas oscuras, aunque era de noche." 
    
    narrador "Como para no tener que mirarme."

    isanari "Le di mi palabra a Maruo."

    isanari "Le dije que te tomarías esto en serio."

    mc "Me lo tomé en serio."

    isanari "No lo suficiente."

    narrador "Lo dijo mirando la mesa. No supe si me lo decía a mí o a él mismo."

    show raiha preocupada at pj(0.20)
    with disolucion_lenta

    raiha "Hermanito..."

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
    with dissolve

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


############################################################################
##  DESPIDO TRAS HUB 3
##  Tras desperdiciar una segunda oportunidad, las quintillizas reflejan
##  sus peores inseguridades y defectos en los exámenes escolares. 
##  Esto lleva a un despido lleno de decepción por parte de Maruo y a un 
##  cierre desolador con la familia del MC.
############################################################################

label final_malo_hub3:

    ############################################################################
    ##  MOVIMIENTO 1 · Lunes por la mañana
    ##  Mc llega a la escuela y se plantea una pregunta antes de entrar y es
    ##  si las hermanas lograrán pasar sus examenes o no.
    ############################################################################

    scene bg_escuela
    with fade_dia
    
    play sound audio.sfx_timbre volume 1.5

    mc_pensamiento "Lunes. Primer día de exámenes." 
    
    mc_pensamiento "Uno por día, toda la semana."

    mc_pensamiento "Maruo dijo: «Al terminar la semana lo confirmo.»"

    mc_pensamiento "«Confirmar» significa que todavía existe un resultado que podría cambiarlo."

    mc_pensamiento "Es la única palabra a la que me estoy aferrando."

    mc_pensamiento "Si aprueban, todo lo demás no importa."

    mc_pensamiento "Si no aprueban, hoy es mi último día como su tutor. Y lo sé."

    mc_pensamiento "Cuatro semanas para esto. Y llego igual que cuando empecé."

    ############################################################################
    ##  MOVIMIENTO 2 · Antes del examen
    ##  Las quintillizas hablan con mc, ellas saben que no hubo progreso en
    ##  sus sesiones de estudio, saben que se viene un fracaso.
    ############################################################################

    scene bg_aula
    with fade
    
    stop music fadeout 1.5

    show ichika neutral at pj(X_ICHIKA)
    show nino neutral at pj(X_NINO)
    show miku neutral at pj(X_MIKU)
    show yotsuba incomoda at pj(X_YOTSUBA)
    show itsuki neutral at pj(X_ITSUKI)
    with dissolve

    narrador "Las cinco ya estaban en el aula." 
    
    narrador "Nadie había abierto un libro."

    narrador "Lo habían abierto tanto estas semanas que ya no servía de nada abrirlo."

    mc "Hola, chicas. Estamos en semana de exámenes."

    mc "Espero les vaya bien."

    mc_pensamiento "Nadie estaba emocionada, se veía venir."

    mc_pensamiento "Ellas saben que desperdiciamos todo este mes, y que no progresamos nada."

    show ichika neutral at pj_calla(X_ICHIKA)
    show nino neutral at pj_calla(X_NINO)
    show miku neutral at pj_calla(X_MIKU)
    show itsuki neutral at pj_calla(X_ITSUKI)
    show yotsuba at pj_habla(X_YOTSUBA)
    with disolucion_lenta

    if rama_de("yotsuba") == "fria":

        yotsuba "Buenos días, tutor."

    else:

        yotsuba "Buenos días, [mc]."
    
    yotsuba "...Quería decirlo con más ganas. No me sale."

    yotsuba "Estudié las lecturas dos veces." 
    
    yotsuba "Cuando cierro el libro, no recuerdo qué sentía nadie."

    show yotsuba at pj_calla(X_YOTSUBA)
    show ichika neutral at pj_habla(X_ICHIKA)
    with disolucion_lenta

    ichika "Dormí cuatro horas." 
    
    ichika "Y las pasé con el papel de la audición, no con las fórmulas."

    ichika "No me mires así. Ya sé que no era lo que tocaba."

    show ichika at pj_calla(X_ICHIKA)
    show miku neutral at pj_habla(X_MIKU)
    with disolucion_lenta

    miku "...Solo sé la mitad de lo que van a preguntar."

    miku "...Y no sé si esa mitad está bien."

    show miku at pj_calla(X_MIKU)
    show itsuki molesta at pj_habla(X_ITSUKI)
    with disolucion_lenta

    itsuki "He estudiado más que nadie en esta aula. Cada noche."

    itsuki "Y no sé si me sé una sola cosa."

    itsuki "Quisiera poder culparte. Sería más fácil."

    show itsuki at pj_calla(X_ITSUKI)
    show nino neutral at pj_habla(X_NINO)
    with disolucion_lenta

    nino "Ya basta de rodeos."

    nino "Alguien tiene que decírtelo y me toca a mí."

    nino "No aprendimos nada. Ni nos enseñaste, ni nosotras quisimos."

    nino "Aunque no sea solo culpa tuya. Eso no cambia que no sirvió."

    show ichika neutral at pj_habla(X_ICHIKA)
    show miku neutral at pj_habla(X_MIKU)
    show yotsuba incomoda at pj_habla(X_YOTSUBA)
    show itsuki at pj_habla(X_ITSUKI)
    with disolucion_lenta

    narrador "Me miraron las cinco. Esperando que les dijera algo."

    mc_pensamiento "No tenía nada que decirles que no fuera una mentira."

    mc "Hagan lo que sepan."

    narrador "Lo dije y sonó a lo que era: una frase vacía e inútil."

    play sound audio.sfx_timbre volume 1.5

    ############################################################################
    ##  MOVIMIENTO 3 · Los cinco exámenes
    ##  Una semana, un examen por día, todo en el aula y sin cambiar de 
    ##  escenario. Cada día se nombra en una línea y la cámara se queda con 
    ##  la hermana de esa materia. mc está sentado en su pupitre de la 
    ##  segunda fila, termina los suyos antes de la mitad, y se queda mirando.
    ############################################################################

    hide ichika 
    hide nino 
    hide miku 
    hide yotsuba 
    hide itsuki
    with disolucion_lenta 

    stop music fadeout 1.5

    scene bg_negro
    with fade

    narrador "Mi pupitre estaba en la segunda fila. Ellas, repartidas delante y a los lados."

    narrador "Cada día, un examen. Cada día terminaba el mío antes de la mitad."

    mc_pensamiento "Ahora venía lo peor: no tener nada que hacer más que mirar."

    profe "Pueden empezar."

    play ambiente amb_reloj fadein 2.0 volume 0.4

    play sound audio.sfx_hoja volume 2.0

    ## 3.1 · Lunes · Japonés · Yotsuba

    narrador "Hoy, lunes." 
    
    narrador "Examen de japonés." 

    scene cg_yotsuba_fracaso
    with fade

    narrador "Las cinco lo hacían a la vez; yo solo podía mirar a una."

    mc_pensamiento "Yotsuba..."

    narrador "Yotsuba no escribía. Tenía el lápiz quieto y la cabeza mirando a otros lados."

    mc_pensamiento "No miraba su hoja." 
    
    mc_pensamiento "Miraba a Ichika. Después a Miku. Después a Itsuki."

    mc_pensamiento "Otra vez a Ichika."

    narrador "Cada vez que una de ellas parecía en problemas, ella se preocupaba un poco."

    mc_pensamiento "Es lo que mejor hace: leer a las demás."

    if rama_de("yotsuba") == "calida":

        mc_pensamiento "Se lo dije una vez, en la pista. Una sola vez no bastó."

    else:

        mc_pensamiento "Nadie le había dicho que eso también contaba. Yo tampoco."

    narrador "La pregunta uno preguntaba qué siente el protagonista cuando se queda solo."

    narrador "La hoja de Yotsuba tenía su nombre. Nada más."

    mc_pensamiento "El mismo uno por ciento del primer día."

    if rama_de("yotsuba") == "calida":

        mc_pensamiento "Le dije que su punto de partida no era cero." 
        
        mc_pensamiento "Y se quedó en el uno."

    elif rama_de("yotsuba") == "fria":

        mc_pensamiento "Le dije que se concentrara en lo suyo."
        
        mc_pensamiento "Nunca le dije qué era lo suyo."

    else:

        mc_pensamiento "Aquel uno por ciento que pude ayudarle a aumentar, pero no lo hice."

    scene bg_negro
    with fade_dia

    play sound audio.sfx_timbre volume 1.5

    narrador "Día martes." 
    
    narrador "Examen de matemáticas."

    play sound audio.sfx_hoja volume 2.0

    ## 3.2 · Martes · Matemáticas · Ichika

    scene cg_ichika_fracaso
    with fade

    narrador "Las cinco lo hacían a la vez; yo solo podía mirar a una."

    mc_pensamiento "Ichika..."

    narrador "Ichika escribió su nombre y las dos primeras líneas."

    narrador "Después sacó algo doblado debajo de la hoja." 
    
    narrador "Un guion."

    mc_pensamiento "Movía los labios sin sonido." 
    
    mc_pensamiento "Repetía una frase una y otra vez."

    mc_pensamiento "No era una fórmula. Era un papel que no es de este examen."

    narrador "Al rato apoyó la cabeza en el brazo y cerró los ojos."

    mc_pensamiento "Igual que el segundo día. La misma función."

    mc_pensamiento "Solo que esta vez la función no era para nadie."

    profe "Nakano. Despierte."

    scene bg_aula
    with dissolve

    show ichika sonriendo at pj_habla(0.5)
    with dissolve

    ichika "Disculpe profesor."
    
    ichika "¡Estaba pensando! Los matemáticos piensan con los ojos cerrados."

    narrador "Nadie se rió. El profesor tampoco."

    profe "Se piensa con los ojos abiertos."

    ichika "Lo siento..."

    scene bg_negro
    with fade_dia

    play sound audio.sfx_timbre volume 1.5

    narrador "Día miércoles." 
    
    narrador "Examen de inglés."

    play sound audio.sfx_hoja volume 2.0

    ## 3.3 · Miércoles · Inglés · Nino

    scene cg_nino_fracaso
    with fade

    narrador "Las cinco lo hacían a la vez; yo solo podía mirar a una."

    mc_pensamiento "Nino..."

    narrador "Nino terminó segunda, después de mí."

    narrador "Letra legible, sin tachones, sin levantar la vista."
    
    narrador "Como si su examen fuera lo de menos."

    narrador "Soltó el lápiz. Giró la hoja boca abajo. Cruzó los brazos."

    narrador "Y esperó."

    profe "Nakano. Si ya terminó su examen lo puede entregar."

    nino "Aún no. Voy a revisar que esté todo correcto."

    mc_pensamiento "No había nada que revisar."

    mc_pensamiento "Miraba de lado." 
    
    mc_pensamiento "A Yotsuba, a Itsuki, a Miku. Con una expresión tensa."

    mc_pensamiento "Se quedó cuarenta minutos fingiendo que revisaba." 
    
    mc_pensamiento "Para no dejarlas solas."

    narrador "Me miró una sola vez. No con una mirada de odio."
    
    narrador "Con una mirada de quien sabía que lo qué decía era correcto."

    mc_pensamiento "Ella lo había visto venir antes que nadie." 
    
    mc_pensamiento "Y era la única que no podía hacer nada."

    scene bg_negro
    with fade_dia

    play sound audio.sfx_timbre volume 1.5

    narrador "Día jueves." 
    
    narrador "Examen de Ciencias."

    play sound audio.sfx_hoja volume 2.0

    ## 3.4 · Jueves · Ciencias · Itsuki

    scene cg_itsuki_fracaso
    with fade

    narrador "Las cinco lo hacían a la vez; yo solo podía mirar a una."

    mc_pensamiento "Itsuki..."

    narrador "Itsuki llevaba tres líneas bien." 
    
    narrador "En la cuarta se estancó."

    narrador "Pasó a la siguiente pregunta. Volvió a la cuarta. Otra vez."

    mc_pensamiento "Una simple línea recta. Dibujada con calma, sin enojo."

    mc_pensamiento "El mismo problema del primer día. El mismo error, en el mismo sitio."

    narrador "Levantó la vista. Me miró un segundo."

    mc_pensamiento "Habría dado lo que fuera por decirle dónde está el error."

    mc_pensamiento "No se puede hablar en un examen." 
    
    mc_pensamiento "Y aunque se pudiera, me lo había prohibido."

    mc_pensamiento "«Ni se te ocurra decirme la respuesta.»"

    narrador "Apartó la mirada. Volvió al papel."

    narrador "No preguntó. Preguntar habría sido darme la razón."
    
    scene bg_negro
    with fade_dia

    play sound audio.sfx_timbre volume 1.5

    narrador "Y ahí terminó el examen de Itsuki."

    narrador "Último día. Viernes." 
    
    narrador "Examen de Sociales."

    play sound audio.sfx_hoja volume 2.0

    ## 3.5 · Viernes · Sociales · Miku
    
    scene cg_miku_fracaso
    with fade

    narrador "Las cinco lo hacían a la vez; yo solo podía mirar a una."

    mc_pensamiento "Miku..."

    narrador "Miku escribió una respuesta larga y bien detallada." 
    
    narrador "Se detuvo."

    narrador "La borró. La volvió a escribir. La borró."

    mc_pensamiento "Escribió la correcta primero. Y después la borró."

    mc_pensamiento "Igual que en la hoja del segundo día. Igual que siempre."

    narrador "Su goma quedó desgastada de tanto uso."

    narrador "De tanto desconfiar de lo que ella sabía."

    narrador "Al final escribió una sola línea. La respuesta que cabe en una línea."

    mc_pensamiento "No le faltan conocimientos. Le falta confianza."

    if rama_de("miku") == "calida":

        mc_pensamiento "Le dije que lo que sabe cuenta como saber." 
        
        mc_pensamiento "No bastó con decírselo una vez."

    elif rama_de("miku") == "tibia":

        mc_pensamiento "Le dije que se le daba bien." 
        
        mc_pensamiento "Una etiqueta más. No le servía de nada."

    elif rama_de("miku") == "fria":

        mc_pensamiento "Le dije que estudiara solo lo que entraba." 
        
        mc_pensamiento "Lo que borró era justo lo que sabía."

    else:

        mc_pensamiento "Lo vi en su hoja hace semanas." 
        
        mc_pensamiento "Y no hice nada."

    narrador "Su mano subió hasta el cuello, hasta los audífonos. Se quedó ahí."

    narrador "No se los puso. Un examen no se puede hacer con música." 
    
    narrador "Pero tampoco los soltó."

    scene bg_negro
    with fade
    
    play sound audio.sfx_timbre volume 1.5

    ############################################################################
    ##  MOVIMIENTO 4 · Después del examen
    ##  Final de los examenes, las chicas y mc se reunen para dialogar de lo
    ##  sucedido, aquí es la cúspide de los mayores temores y miedos de las
    ##  chicas, saben que tanto ellas como mc fracasaron en todo ese mes.
    ############################################################################

    stop ambiente fadeout 1.0

    narrador "Sonó la última campana de la semana." 
    
    narrador "El aula se fue vaciando."

    narrador "Todos los estudiantes se retiraban a sus hogares."

    narrador "Ellas se quedaron."

    scene bg_aula_tarde
    with fade

    play music derrota fadein 2.5

    show ichika neutral at pj(X_ICHIKA) 
    show nino neutral at pj(X_NINO)
    show miku neutral at pj(X_MIKU)
    show yotsuba neutral at pj(X_YOTSUBA)
    show itsuki neutral at pj(X_ITSUKI)
    with dissolve

    narrador "Nadie recogía nada. Ninguna dijo «salió bien»."

    mc "Sé cómo terminó todo esto."

    mc "No se sientan culpables." 
    
    mc "Si alguien tiene la culpa aquí, soy yo."

    show ichika neutral at pj_calla(X_ICHIKA)
    show nino neutral at pj_calla(X_NINO)
    show miku neutral at pj_calla(X_MIKU)
    show itsuki neutral at pj_calla(X_ITSUKI)
    show yotsuba at pj_habla(X_YOTSUBA)
    with disolucion_lenta

    yotsuba "[mc]..."

    yotsuba "Mi hoja estuvo en blanco durante todo el examen." 
    
    yotsuba "Solo escribí mi nombre."

    yotsuba "Estuve mirando a las demás todo el tiempo." 
    
    yotsuba "No pude parar."

    yotsuba "Con toda esta energía que me sobra, y no pude hacer nada por ninguna."

    mc "Yotsuba, no es tu..."

    yotsuba "No me digas que no es mi culpa."

    show yotsuba at pj_calla(X_YOTSUBA)
    show ichika agotada at pj_habla(X_ICHIKA)
    with disolucion_lenta

    ichika "Me dormí delante de todos."

    ichika "Me dieron el papel de la obra." 
    
    ichika "Y ni siquiera me alegré."

    ichika "No me preguntes por qué. Si me preguntas voy a inventarme algo."

    ichika "Y hoy no tengo ganas de inventar nada."

    mc "Ichika..."

    show ichika at pj_calla(X_ICHIKA)
    show miku encogida at pj_habla(X_MIKU)
    with disolucion_lenta

    miku "...Sabía las respuestas." 
    
    miku "...Las escribí. ...Las borré."

    miku "...Perdón."

    mc "No pidas perdón."

    miku "...Es lo único que sé decir."

    miku "...Lo único en lo que sí tengo confianza."

    show miku at pj_calla(X_MIKU)
    show itsuki molesta at pj_habla(X_ITSUKI)
    with disolucion_lenta

    itsuki "Estudié todas las noches."

    itsuki "Y en cuanto vi la hoja, no supe qué contestar."

    if rama_de("itsuki") == "calida":

        itsuki "Una vez me dijiste dónde mirar." 
        
        itsuki "Una vez no alcanzó."

        itsuki "No sé si la culpa es tuya o mía."

    elif rama_de("itsuki") == "fria":

        itsuki "Me resolviste un ejercicio." 
        
        itsuki "Uno. Y no aprendí nada de él."

        itsuki "No sé qué es peor."

    else:

        itsuki "Te pedí que no me ayudaras. Y no lo hiciste."

        itsuki "No sé qué es peor."

    mc "Itsuki... Yo..."

    show itsuki at pj_calla(X_ITSUKI)
    show nino neutral at pj_habla(X_NINO)
    with disolucion_lenta

    nino "Va a pasar lo que dije que pasaría."

    nino "Te lo dije el primer día." 
    
    nino "Y no me siento mejor por tener razón."

    mc "Te vi quedarte hasta la campana."

    nino "No sé de qué hablas."

    show nino neutral at pj_calla(X_NINO)
    with disolucion_lenta

    mc_pensamiento "Un mes." 
    
    mc_pensamiento "Y mi única contribución había sido sentarme a mirar."

    mc_pensamiento "Cinco personas que saben una cosa cada una." 
    
    mc_pensamiento "Y ninguna me había enseñado."

    mc_pensamiento "Y yo no pregunté lo suficiente."

    hide ichika 
    hide nino 
    hide miku 
    hide yotsuba 
    hide itsuki
    with disolucion_lenta 

    ############################################################################
    ##  MOVIMIENTO 5 · Noche en casa (todavía no lo saben)
    ##  Mc regresa a casa y aún no sabe como decirles la verdad a Raiha e
    ##  Isanari sobre su despido, miente de una forma que logre aliviar las
    ##  cosas, aunque sabe que tarde o temprano les deberá decir.
    ############################################################################

    scene bg_cuarto_mc
    with fade
    
    stop music fadeout 1.5

    narrador "Esa noche volví a mi cuarto." 
    
    narrador "No abrí la libreta."

    mc_pensamiento "Repasé todo lo que hice en el mes." 
    
    mc_pensamiento "Tres tardes." 
    
    mc_pensamiento "En dos dije lo que me pareció correcto. Y lo correcto no alcanzó."

    mc_pensamiento "Cada vez que alguien necesitaba que me quedara callado, hablé."

    mc_pensamiento "Y cada vez que necesitaba hablar, me quedé callado."

    play sound audio.sfx_toque_puerta volume 1.5 
    
    show raiha hablando at pj(0.30)
    with dissolve

    raiha "Hermanito, ¿cómo salieron esas chicas?"

    mc "No lo sé todavía. Mañana llegan las notas."

    raiha "Si se esforzaron, saldrá bien."

    mc "Se esforzaron. Algunas."

    raiha "Entonces hiciste lo que pudiste."

    narrador "Lo dijo con tanta convicción que me dieron ganas de creerle."

    mc "...Sí."

    mc_pensamiento "No. No lo hice."

    show isanari neutral at pj(0.73)
    with dissolve

    narrador "Mi padre se asomó detrás de ella."

    isanari "Mañana Maruo cierra el mes."

    isanari "Si salen bien, el domingo cenamos fuera. Los tres."

    isanari "Es lo mejor que nos ha pasado en años."

    narrador "Raiha me miró. Yo no le devolví la mirada."

    mc_pensamiento "Ellos todavía no sabían que el despido estaba firmado desde hoy."

    mc_pensamiento "Y yo todavía no tenía valor para decírselo."

    ############################################################################
    ##  MOVIMIENTO 6 · Maruo
    ##  Mc recibe una llamada por parte de Maruo, se entabla una conversación
    ##  directa entre los dos, y se anuncia el despedido de mc, Maruo se siente
    ##  decepcionado de que mc no aprovechara su última oportunidad.
    ############################################################################
 
    scene bg_negro
    with fade_dia

    play sound audio.sfx_celular volume 1.0

    narrador "Al día siguiente, a media mañana, me sonó el teléfono."

    narrador "«Departamento. Cinco de la tarde. Maruo.»"

    narrador "Nada más. No hacía falta."

    scene bg_edificio
    with fade
    
    scene bg_departamento
    with dissolve
    
    scene cg_maruo_reunion
    with corte_seco
    
    play music contrato fadein 2.0

    maruo "Siéntate."

    mc "Prefiero estar de pie."

    maruo "Como quieras."

    narrador "Dejó cinco boletines sobre la mesa."
    
    narrador "Boca arriba, en fila."

    maruo "Las notas llegaron esta mañana."

    maruo "Una aprobó. Cuatro no."

    mc "¿Quién...?"

    maruo "No necesito decirte cuál."

    mc_pensamiento "Lo sabía. La que se quedó hasta la campana."

    scene cg_maruo_espaldas
    with corte_seco
    
    maruo "Te advertí en esa cocina que no repetiría la advertencia. Y no la repetí."

    maruo "Esperaba equivocarme contigo, [mc]."

    maruo "Tu padre me habló de alguien que no se rendía."

    mc "No me rendí."

    maruo "No te rendiste. Tampoco hiciste nada."

    narrador "Lo dijo sin dureza. Y por eso me dolió más."

    maruo "No te pedí que fueras amable con mis hijas." 
    
    maruo "Te pedí que estudiaran."

    maruo "Con cuatro de ellas no lo conseguiste."

    mc "Si me diera un mes más..."

    maruo "Ya tuviste uno."

    maruo "Y tuviste una última oportunidad. Yo no me alegro de esto."

    maruo "Tu padre recibirá el pago de lo trabajado." 
    
    maruo "Hasta aquí."

    play sound audio.sfx_puerta_cierra volume 1.0
    
    stop music fadeout 2.0

    narrador "Recogió sus cosas y salió." 
    
    narrador "Sin portazo. Dándome la espalda."

    mc_pensamiento "Esta vez no pude decir «eso no es justo»." 
    
    mc_pensamiento "Porque sí lo era."

    mc_pensamiento "Tenía razón."

    mc_pensamiento "Fracasé."

    ############################################################################
    ##  MOVIMIENTO 7 · Las despedidas
    ##  Las quintillizas se despiden de mc, una a una, es una despedida muy
    ##  triste, porque ellas también sentían algo de culpa. Cada una se despide
    ##  a su manera. Los bloques «fría» se leen con rama_de("hermana") == "fria".
    ############################################################################

    scene bg_departamento_anochecer
    with dissolve

    narrador "No me dio tiempo a irme."

    narrador "Cuando estaba a punto de retirarme, ellas salieron."

    narrador "Se abrieron las puertas del pasillo. Una por una."

    ## Yotsuba

    show yotsuba incomoda at pj_habla(0.5)
    with dissolve

    yotsuba "Gracias por venir todos los días."

    yotsuba "No sé cómo despedirme de alguien que se va por mi culpa."

    mc "No es por tu culpa."

    mc "Ni la culpa de ninguna de ustedes."

    yotsuba "Lo sé. Pero así se siente."

    if rama_de("yotsuba") == "fria":

        yotsuba "Gracias por todo, tutor."

        narrador "Me llamó «tutor»." 
        
        narrador "Con el tono que se usa con un desconocido."

    hide yotsuba 
    with disolucion_lenta

    ## Ichika

    show ichika neutral at pj_habla(0.5)
    with dissolve

    ichika "Aquí no hace falta que sonría, ¿verdad?"

    ichika "Ni contar algún chiste."

    ichika "Fue un placer conocerte, [mc]. Y lo digo sin guiones."

    if rama_de("ichika") == "calida":

        ichika "Una vez me dejaste quedarme callada sin llenar el silencio."

        ichika "Eso me lo llevo."

    elif rama_de("ichika") == "tibia":

        ichika "El dragón te lo dejo. Cuídalo."

        ichika "Se llama «Contrato». Pero eso ya lo sabías."

    elif rama_de("ichika") == "fria":

        ichika "Me dijiste que si tenía energía para chistes, la tenía para estudiar."

        ichika "Hoy no me queda para ninguna de las dos."

    hide ichika 
    with disolucion_lenta

    ## Miku

    show miku neutral at pj_habla(0.5)
    with dissolve

    miku "...Adiós, [mc]."

    if rama_de("miku") == "calida":

        miku "...Me preguntaste." 
        
        miku "...Y te lo conté."

        miku "...Lo que no supe fue escribirlo sin que nadie me preguntara."

    else:

        miku "...Yo te lo habría contado." 
        
        miku "...Todo lo que sé."

        miku "...Si hubieras preguntado."

    narrador "Se subió los audífonos." 
    
    narrador "Y esta vez sí sonó la música."

    if rama_de("miku") == "fria":

        miku "...Hoy no, dije esa vez." 
        
        miku "...Ya no hay otro día."

        miku "...Este es el final."
    
    hide miku 
    with disolucion_lenta

    ## Nino

    show nino neutral at pj_habla(0.5)
    with dissolve

    nino "Mi padre te va a pagar lo del mes. Acéptalo."

    mc "Gracias, Nino."

    nino "No me des las gracias."

    show nino nerviosa at pj_habla(0.5)
    with disolucion_lenta

    nino "Yo ni siquiera sé si..."

    narrador "Se cortó a mitad de frase. Esta vez no era por haber hablado de más."

    nino "Cuídate."

    if rama_de("nino") == "fria":

        nino "Anota la fecha, te dije. Aquí la tienes."

        nino "Llegó ese día."

    hide nino 
    with disolucion_lenta

    ## Itsuki

    show itsuki neutral at pj_habla(0.5)
    with dissolve

    itsuki "Te vas sin que nadie te lo pida. Eso es raro en ti."

    mc "Itsuki."

    mc "Debí disculparme el primer día." 
    
    mc "Por lo del asiento. Por todo."

    itsuki "Sí. Debiste."

    itsuki "..."

    show itsuki timida at pj_habla(0.5)
    with disolucion_lenta

    itsuki "Yo tampoco dije que lo sentía." 
    
    itsuki "Eso lo hace parejo, supongo."

    itsuki "Ya no sirve de nada." 
    
    itsuki "Pero acepto tu disculpa."

    narrador "Fue la única disculpa que dije en todo el mes." 
    
    narrador "Y llegó tarde."

    if rama_de("itsuki") == "fria":

        show itsuki neutral at pj_habla(0.5)
        with disolucion_lenta

        itsuki "Me quitaste el cuaderno de las manos." 
        
        itsuki "Aun así, lo agradezco. No sé por qué."

    hide itsuki 
    with disolucion_lenta

    play music derrota fadein 2.5

    narrador "Y así concluyó todo."

    narrador "Salí del departamento." 
    
    narrador "Esta vez nadie me acompañó. Nadie me pidió que me quedara."

    mc_pensamiento "Ni siquiera hubo un portazo." 
    
    mc_pensamiento "Eso era lo más cruel."

    scene bg_negro
    with fade

    ############################################################################
    ##  MOVIMIENTO 8 · La cena
    ##  Mc llega a su hogar e Isanari le dice de la llamada a mc, mc finalmente
    ##  confiesa que fue despedido, Raiha e Isanari se quedan tristes, ya que
    ##  esa era una de sus pocas fuentes de ingresos.
    ########################################################## ##################

    scene bg_comedor
    with fade

    stop music fadeout 1.5

    narrador "En casa olía a curry."

    narrador "Parecía que iba a ser otra cena familiar normal."

    narrador "No lo era."

    show raiha hablando at pj(0.20)
    with dissolve

    raiha "¡Hermanito! Hice curry." 
    
    raiha "Pensé que si las notas salían bien, celebrábamos."

    narrador "Entonces vio mi cara." 
    
    narrador "Y se le apagó la sonrisa entera."

    show raiha preocupada at pj(0.20)
    with disolucion_lenta

    show isanari neutral at pj(0.73)
    with dissolve

    isanari "Maruo me llamó. Hace una hora."

    raiha "¿Llamó por qué?"

    isanari "Díselo tú."

    mc "Me despidieron, Raiha."

    show raiha preocupada at pj_habla(0.20)
    with disolucion_lenta

    raiha "...¿Qué?"

    mc "Cuatro reprobaron. Y yo... no pude hacer nada."

    mc "Tuve un mes. Y tuve una última oportunidad." 
    
    mc "Y no la aproveché."

    raiha "Pero dijiste que no eran tontas."

    mc "Y no lo son."

    raiha "Entonces no entiendo el problema."

    narrador "Lo dijo igual que aquella noche." 
    
    narrador "Solo que esta vez la voz le temblaba."

    isanari "Esa familia pagaba cinco veces la tarifa." 
    
    isanari "Cubría lo que ni tú ni yo cubrimos."

    isanari "No te lo digo para hundirte."

    isanari "Conté con eso. Y no tenía derecho a contar contigo para eso."

    raiha "Papá, déjalo."

    isanari "..."

    narrador "Mi padre se sentó. No dijo nada más."

    raiha "...No pasa nada, hermanito."

    raiha "Vamos a comer. El curry se enfría."

    narrador "Nos sentamos. El ambiente era de todo menos alegre."

    mc "Gracias por la comida."

    narrador "Lo dije por costumbre." 
    
    narrador "Era la primera vez que no sentía nada al decirlo."

    ############################################################################
    ##  MOVIMIENTO 8 · La libreta
    ##  Mc llega a su hogar e Isanari le dice de la llamada a mc, mc finalmente
    ##  confiesa que fue despedido, Raiha e Isanari se quedan tristes, ya que
    ##  esa era una de sus pocas fuentes de ingresos.
    ############################################################################

    scene bg_cuarto_mc
    with fade
    
    scene cg_libreta
    with dissolve

    narrador "Abrí la libreta. La página de los cinco nombres."

    mc_pensamiento "«De frente y las cinco a la vez, pierdo siempre.»"

    mc_pensamiento "Fui de una en una. Y perdí igual."

    mc_pensamiento "Tres tardes que me dieron."

    mc_pensamiento "Treinta días."

    mc_pensamiento "Los usé todos. Y no cambié a ninguna."

    mc_pensamiento "Me permití el lujo de equivocarme."

    mc_pensamiento "Y salió caro."

    narrador "Cerré la libreta. Apagué la lámpara."

    narrador "Y ahí terminó."

    jump final_malo_cierre
