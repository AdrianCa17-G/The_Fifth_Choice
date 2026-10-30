################################################################################
##  BGs Y CGs PROPIOS DEL BEAT DE LA CASA 
##  Solo 1 ilustración y 1 SFX nuevos de momentos concretos de este beat.
##  Los que el beat reutiliza son todos los sprites BGM, SFX y algunos
##  BGs y CGs ya existetes
################################################################################

image cg_raiha_correccion = "images/cg/cap1_beats/raiha_correccion.webp"

define audio.sfx_lapiz_mesa = "audio/sfx/lapiz_mesa.mp3"

################################################################################
##  HUB DE LA CASA 
##  Encuentro entre mc, Raiha e Isanari un dia antes del examen final, este es
##  el beat que cierra definitamente el esqueleto del cpaitulo 1 antes de 
##  terminar con el movimiento 6 final del capitulo
################################################################################

label beat_casa:

    ############################################################################
    ##  MOVIMIENTO 1 · Llegada
    ##  Mc nuevamente llega tarde a su casa, Raiha lo recibe pero con un tono
    ##  regañador puesto a que ya son varias veces que llega tarde.
    ############################################################################

    scene bg_comedor
    with fade
    
    stop music fadeout 1.0

    narrador "Llegué a casa más tarde de lo normal." 
    
    narrador "Otra vez."

    narrador "El examen era al día siguiente."

    narrador "Faltaban horas, no días."

    play music cena fadeout 1.5 fadein 2.0

    mc_pensamiento "Han pasado treinta días."

    mc_pensamiento "Contados desde la noche en que anoté los cinco nombres."

    mc_pensamiento "Mañana sabré si sirvieron de algo."

    narrador "Raiha estaba en la mesa, con su propio cuaderno abierto y la cena ya servida y fría."

    show raiha hablando at pj(0.20)
    with dissolve

    raiha "¡Hermanito!" 
    
    raiha "Te guardé la cena, pero se enfrió como tres veces."

    mc "Perdóname, Raiha." 
    
    mc "Se me hizo tarde."

    show raiha regano at pj(0.20)
    with disolucion_lenta

    raiha "Desde que comenzaste tu trabajo como tutor, siempre se te hace tarde."

    narrador "No lo dijo con reproche. Lo dijo como quien ya lleva la cuenta."

    ############################################################################
    ##  MOVIMIENTO 2 · El gesto
    ##  Raiha se da cuenta de que Mc está actuando de otra manera debido a 
    ##  las tantas semanas que el ha pasado como tutor
    ############################################################################

    narrador "Me senté a comer." 
    
    narrador "Raiha no cerró su cuaderno."

    scene cg_raiha_correccion
    with dissolve

    raiha "Hermanito, tengo un problema de matemáticas que no me sale."

    mc "Muéstrame."

    narrador "Lo dije con la boca todavía llena." 
    
    narrador "No pensé en cómo lo dije."

    narrador "Miré la hoja. El error estaba en el segundo paso."

    mc "¿Revisaste esta línea?"

    raiha "¿Cuál?"

    mc "Esta. No te la voy a resolver." 
    
    mc "Solo mira si el signo está bien."

    narrador "Levantó la vista de la hoja antes de corregir."

    $ duck()
    play sound audio.sfx_lapiz_mesa volume 2.5

    narrador "Dejó el lápiz sobre la mesa, despacio."

    raiha "…Hablaste raro."

    mc "¿Raro cómo?"

    raiha "Como un profesor." 
    
    raiha "Ni pareces mi hermano cuando dices esas cosas."

    narrador "Lo dijo sin mala intención." 
    
    narrador "Con la misma naturalidad con la que señala cualquier otra cosa."

    mc_pensamiento "No fue un chiste." 
    
    mc_pensamiento "Se lo tomó como algo raro de verdad."

    mc_pensamiento "Llevo semanas diciéndoles a cinco personas «no te lo voy a resolver, solo mira si está bien»." 
    
    mc_pensamiento "Lo he repetido tantas veces que ya no me sale de otra forma."
    
    mc_pensamiento "Ni siquiera con ella."

    raiha "¿Estás bien?"

    mc "Estoy cansado. Nada más."

    narrador "Volvió a mirar su hoja, ya sin el mismo ánimo de antes."

    raiha "…Está bien el signo."

    mc "Entonces revisa el siguiente paso con la misma lógica."

    narrador "Lo dije otra vez con el mismo tono."

    narrador "Esta vez lo noté yo también, medio segundo tarde."

    ############################################################################
    ##  MOVIMIENTO 3 · Isanari
    ##  Isanari llega y pregunta a mc como le va, supone que le va bien porque
    ##  sigue recibiendo el dinero, pero no pregunta por su estado emocional.
    ############################################################################

    scene bg_comedor
    with dissolve

    play sound audio.sfx_puerta_abre volume 1.0

    narrador "Mi padre entró cuando Raiha ya estaba guardando el cuaderno."

    show isanari neutral at pj(0.73)
    with dissolve

    isanari "Vaya [mc], te ves demasiado cansado."

    isanari "¿Cómo vas? ¿Todo marcha bien en tu trabajo?"

    mc "El examen es mañana."

    isanari "¿El tuyo o el de ellas?"

    mc "El de ellas."

    mc "El mío ya lo rendí hace un mes, cuando dijiste que sí por mí."

    show isanari sonriendo at pj(0.73)
    with disolucion_lenta

    isanari "No suenes tan dramático."

    isanari "Te va bien, ¿no? El dinero sigue entrando."

    narrador "No preguntó cómo estaba."

    narrador "Preguntó si el dinero seguía llegando, en la misma frase."

    mc_pensamiento "No es que me sorprenda."

    mc_pensamiento "Es que después de un mes viéndolas a ellas cinco fingir que no les importo,
    se siente distinto verlo a él sin fingir nada."

    show raiha regano at pj(0.20)
    with disolucion_lenta

    raiha "¡Papá!"

    raiha "Pregúntale cómo está, no cuánto pagan."

    isanari "Es la misma pregunta, Raiha." 
    
    isanari "Si le fuera mal, no seguirían pagando."

    narrador "Lo dijo sin maldad."

    narrador "Con la misma lógica fría con la que arregla todo lo demás."

    mc "Las cinco van a salir bien."

    isanari "Eso espero." 
    
    isanari "Cinco veces la tarifa no cae del cielo dos veces."

    play sound audio.sfx_puerta_cierra volume 1.0

    narrador "Se sirvió agua y volvió a su cuarto sin esperar respuesta, "
    
    narrador " exactamente con la misma calma con la que había entrado."

    mc_pensamiento "No dijo suerte." 
    
    mc_pensamiento "No preguntó de qué se trataba el examen."

    mc_pensamiento "Solo confirmó que el trato seguía en pie desde su lado."

    narrador "Raiha se quedó mirando la puerta de su cuarto un momento más de lo necesario."

    show raiha hablando at pj(0.20)
    with disolucion_lenta

    raiha "No le hagas caso."

    mc "No le hago caso."

    narrador "Los dos sabíamos que no era del todo cierto."

    ############################################################################
    ##  MOVIMIENTO 4 · A SOLAS
    ##  Momento crucial antes del examen, mc reflexiona sobre lo que ha pasado 
    ##  en el mes que lleva como tutor y lo que ha aprendido de las cinco 
    ##  hermanas, y de sí mismo, los pensamientos de cada hermana se
    ##  desbloquean si es que las visitó en cada hub.
    ############################################################################

    scene bg_cuarto_mc
    with fade
     
    stop music fadeout 1.5

    narrador "Me encerré en mi cuarto antes de las diez."

    narrador "Saqué la libreta del cajón." 
    
    narrador "La misma de la primera noche."

    scene cg_libreta
    with dissolve
    
    play music hogar fadein 1.5 

    mc_pensamiento "Cinco nombres, en columna, con una línea debajo."

    mc_pensamiento "Treinta días después, la letra sigue siendo la misma."

    mc_pensamiento "Solo que ahora sé lo que cuesta cada nombre."

    narrador "Dejé la vista quieta un momento antes de cerrarla."

    if despido_cap1:

        mc_pensamiento "No sé si mañana esto sigue siendo mi trabajo."

        mc_pensamiento "Ninguna aprobó todavía."

        mc_pensamiento "Y las cinco llegan a este último tramo por caminos que yo elegí."

        mc_pensamiento "Uno a uno, sin preguntarles si querían que fuera así."

        mc_pensamiento "Si mañana me voy, me voy sabiendo exactamente por qué."

        mc_pensamiento "Todo el peso de mis decisiones caerá mañana."

    else:

        label beat_casa_libreta:

            $ hermanas_pensamiento = set()

            ## Solo las visitadas llevan el color de su hermana en el menú.
            $ ligera_hermanas = {}
            if ichika_visitada_cap1:
                $ ligera_hermanas["Ichika"] = "ichika"
            if nino_visitada_cap1:
                $ ligera_hermanas["Nino"] = "nino"
            if miku_visitada_cap1:
                $ ligera_hermanas["Miku"] = "miku"
            if yotsuba_visitada_cap1:
                $ ligera_hermanas["Yotsuba"] = "yotsuba"
            if itsuki_visitada_cap1:
                $ ligera_hermanas["Itsuki"] = "itsuki"

            jump bcl_menu


        label bcl_menu:

            menu:

                "¿En qué nombre te fijas más tiempo?"

                "Ichika" if "ichika" not in hermanas_pensamiento:
                    jump bcl_ichika

                "Nino" if "nino" not in hermanas_pensamiento:
                    jump bcl_nino

                "Miku" if "miku" not in hermanas_pensamiento:
                    jump bcl_miku

                "Yotsuba" if "yotsuba" not in hermanas_pensamiento:
                    jump bcl_yotsuba

                "Itsuki" if "itsuki" not in hermanas_pensamiento:
                    jump bcl_itsuki


        label bcl_fin:

            if len(hermanas_pensamiento) < 5:
                jump bcl_menu

            $ ligera_hermanas = {}

            return


        ################################################################################
        ##  ICHIKA
        ################################################################################

        label bcl_ichika:

            $ hermanas_pensamiento.add("ichika")

            call collage_abrir("ichika")

            if ichika_visitada_cap1:

                play music ichika fadeout 1.0 fadein 1.5

                ## --- Primer encuentro y apertura ---

                mc_pensamiento "Ichika fue la primera cara que vi en ese departamento."

                mc_pensamiento "Me abrió la puerta con una sonrisa fácil, como si llevara un rato esperándome."

                mc_pensamiento "Pidió perdón por adelantado por el desorden, el ruido y todo lo que iba a ver."

                mc_pensamiento "Pensé que era cortesía. Era un aviso."

                mc_pensamiento "Al día siguiente fingió dormir para no contestar una hoja que ya habían decidido fallar."

                mc_pensamiento "Dijo «coincidencia, somos hermanas» sin que le temblara nada."

                mc_pensamiento "Mentía tan bien que casi daba gusto. Casi."

                ## --- Hub ---

                mc_pensamiento "Por eso, al entrar al club de teatro, ya no me fiaba de ninguna de sus sonrisas."

                mc_pensamiento "La encontré dormida en el suelo, con el guion resbalándole de la mano."

                mc_pensamiento "A su lado, dos latas de energizante. Una de ellas, abollada."

                mc_pensamiento "Y un horario con tres columnas superpuestas y algo tachado que no quiso que leyera."

                mc_pensamiento "Al despertar, durante medio segundo, no hubo actuación."

                mc_pensamiento "Dijo «perdí la tarde entera» con una voz que no tenía dirección de escena."

                mc_pensamiento "Después volvió la sonrisa, y con ella el chiste del «descanso escénico»."

                if ichika_rama_cap1 == "calida":

                    mc_pensamiento "No le seguí la broma. Me quedé callado, esperando."

                    mc_pensamiento "Fue ella quien rompió el silencio: dijo que no sabía cuánto más podía seguir así."

                    mc_pensamiento "Las audiciones, las clases, fingir que puede con las dos."

                    mc_pensamiento "No creo que me lo dijera a mí. Creo que se le escapó."

                    mc_pensamiento "Al día siguiente me contó que había dormido siete horas y cuarto. Y que redondeaba hacia arriba."

                    mc_pensamiento "Y que ya podía cuidarme ella a mí, si la dejaba."

                    mc_pensamiento "Nadie me había preguntado por mi sueño en años."

                elif ichika_rama_cap1 == "tibia":

                    mc_pensamiento "Le seguí la broma y acabamos inventando un dragón que lee contratos de audición."

                    mc_pensamiento "Se rió de verdad. Fue un buen rato."

                    mc_pensamiento "Pero mientras hablábamos del dragón, las latas siguieron sin explicación."

                    mc_pensamiento "Al día siguiente bautizó al dragón «Contrato». Dice que es su mejor material."

                else:

                    mc_pensamiento "Le dije que si tenía energía para chistes, la tenía para estudiar."

                    mc_pensamiento "No se enfadó. Contestó «tienes razón» sonriendo y guardó el guion sin doblarlo."

                    mc_pensamiento "Fue correcta conmigo. Eso, viniendo de ella, es peor que un portazo."

                    mc_pensamiento "Al día siguiente la sonrisa llegó medio segundo tarde."

                    mc_pensamiento "Me recibió con mi nombre y nada más."

                mc_pensamiento "Antes de irnos le llegó un mensaje: un papel nuevo en la obra de primavera."

                mc_pensamiento "Dijo que sí sin pensarlo, con una agenda que ya no le cabía."

                mc_pensamiento "Ni siquiera contestó el mensaje. Lo guardó, como guarda todo lo demás."

                ## --- Indicio ---

                mc_pensamiento "Aun así, hay algo en ella que no encaja."

                mc_pensamiento "No sabe cuántas horas durmió, pero sabe cuántos minutos tarda un tren y cuántos necesita para cambiarse."

                mc_pensamiento "Lo dijo de corrido, sin contar con los dedos. Y después lo llamó «ser organizada»."

                mc_pensamiento "Una cabeza así no se improvisa. Y ella ni siquiera lo considera un talento."

                call collage_cerrar

                play music hogar fadeout 1.5 fadein 2.0 volume 0.7

            else:

                mc_pensamiento "A Ichika no fui a buscarla."

                mc_pensamiento "La primera vez me abrió la puerta con una sonrisa fácil y una disculpa por adelantado."

                mc_pensamiento "Al día siguiente fingió dormir para tapar una hoja que había contestado mal a propósito."

                mc_pensamiento "Desde entonces, cada vez que la veo, hay un chiste antes de que yo diga nada."

                mc_pensamiento "Cuando se enteró de que no la había elegido, soltó que había ensayado tres reacciones."

                mc_pensamiento "Una graciosa, una dramática y una de «qué sorpresa, no te esperaba»."

                mc_pensamiento "Luego dijo que eran todas actuación, y que no sabía si habría podido con otra cosa."

                mc_pensamiento "Cuando sonríe, parece que se acomoda un disfraz."

                mc_pensamiento "No sé si sigue actuando o si dejó de hacerlo."

            jump bcl_fin


        ################################################################################
        ##  NINO  (su beat de la cocina ocurrió siempre, se visitara o no el hub)
        ################################################################################

        label bcl_nino:

            $ hermanas_pensamiento.add("nino")

            call collage_abrir("nino")

            if nino_visitada_cap1:

                play music nino fadeout 1.0 fadein 1.5

                ## --- Primer encuentro y apertura ---

                mc_pensamiento "Nino fue la segunda, y la primera en dejarme claro que sobraba."

                mc_pensamiento "«¿A quién diablos le abriste la puerta?», dijo, sin saber siquiera mi nombre."

                mc_pensamiento "Me dio una semana. Después dijo que el último tutor había durado cuatro días."

                mc_pensamiento "No lo dijo con rabia. Lo dijo como quien recita un dato que ya se sabe de memoria."

                mc_pensamiento "Al día siguiente organizó a las cinco para que contestaran igual de mal."

                mc_pensamiento "Cinco hojas, seis errores idénticos y un informe listo para su padre."

                mc_pensamiento "Pero cuando leí una frase en inglés con mi peor acento, no pudo evitarlo."

                mc_pensamiento "Me corrigió. Molesta, en mitad de la discusión, sin pensarlo."

                mc_pensamiento "«Se pega, no se separa.» Nadie corrige por reflejo algo que no domina."

                ## --- Hub ---

                mc_pensamiento "La encontré en el pasillo de importados, comparando dos cajas de harina."

                mc_pensamiento "Leía las etiquetas moviendo apenas los labios, como quien lee en su propia lengua."

                mc_pensamiento "Llevaba una tarjeta de receta escrita a mano, vieja, de alguien que no era ella."

                mc_pensamiento "Lo leyó todo sin buscar una sola palabra. Y cuando intentó explicar cómo, se trabó."

                mc_pensamiento "«No es lo mismo leer que...» Y no terminó la frase."

                mc_pensamiento "Luego, por una vez, habló de más: dijo que los tutores anteriores también sonreían el primer día."

                mc_pensamiento "Que sus hermanas se ilusionan cada vez, y que después les toca ver a alguien irse."

                mc_pensamiento "No desconfía de mí. Desconfía del puesto."

                if nino_rama_cap1 == "calida":

                    mc_pensamiento "Le dije que tenía razón en desconfiar y que solo el tiempo lo demostraría."

                    mc_pensamiento "Dijo que era la primera vez que alguien no le prometía nada."

                    mc_pensamiento "Eso no significa que confíe en mí. Lo dejó bien claro."

                    mc_pensamiento "Pero al día siguiente me ordenó comer algo antes de clases, y se le olvidó cruzar los brazos."

                elif nino_rama_cap1 == "tibia":

                    mc_pensamiento "Le cargué una cesta sin decir nada y terminó caminando a mi lado sin discutirlo."

                    mc_pensamiento "«Esto no significa nada», dijo. Fue lo más parecido a un gracias que iba a sacarle."

                else:

                    mc_pensamiento "Le prometí que yo sí iba a durar."

                    mc_pensamiento "Se rió, pero no de gracia: eso mismo había dicho el que llegó antes que yo."

                    mc_pensamiento "Me dijo que anotara la fecha. Que cuando me fuera, me la iba a recordar."

                mc_pensamiento "Mientras la acompañaba a la salida, la llamó su padre."

                mc_pensamiento "Ella dijo que el tutor nuevo aún no la convencía, y que no quería explicar por qué."

                ## --- Beat de la cocina ---

                mc_pensamiento "Y después llegó la cocina."

                mc_pensamiento "Entré al departamento y la oí pedirle a Maruo que me despidiera."

                mc_pensamiento "Es la única vez que la escuché gritarle a su padre."

                mc_pensamiento "Dijo que no se trataba de mí, sino de que iba a durar lo mismo que los anteriores."

                mc_pensamiento "Que Ichika finge, que Yotsuba se esfuerza el doble, que Miku se encierra más y que Itsuki se lo toma personal."

                mc_pensamiento "Y que a ella le toca juntar los pedazos de las cuatro porque es la única que nunca se ilusionó."

                mc_pensamiento "«Alguien tiene que quedarse con la cabeza fría.»"

                mc_pensamiento "Se detuvo con la taza a medio camino y dijo que no había dicho nada de eso."

                mc_pensamiento "Lo había dicho todo."

            else:

                mc_pensamiento "No fui a buscarla al centro comercial."

                mc_pensamiento "Pero a Nino la conozco desde la primera puerta: «no vas a durar ni una semana»."

                mc_pensamiento "Desde el segundo día: organizó a las cinco para que fallaran juntas."

                mc_pensamiento "Aun así me corrigió un «had to» sin pensarlo, molesta, a mitad de discusión."

                mc_pensamiento "Nadie corrige por reflejo algo que no domina."

                mc_pensamiento "Cuando supo que no la había buscado dijo que le daba igual, que ya me había visto en su casa de sobra."

                mc_pensamiento "Y que alguien tiene que ser la que no cambia, para que las demás tengan a dónde volver."

                mc_pensamiento "Después vino la cocina. La oí pedirle a su padre que me echara."

                mc_pensamiento "Gritó, y se frenó antes de decir por qué."

                mc_pensamiento "Habló de sus hermanas una por una, y de sí misma como la única que nunca se ilusionó."

            ## El desenlace de la cocina depende de lo que le contestó mc, no del hub.

            if nino_rama_beat == "calida":

                mc_pensamiento "Le pregunté quién juntaba los pedazos de ella."

                mc_pensamiento "No supo qué contestar, y me puso a cortar cebollas."

                mc_pensamiento "En toda la tarde no volvió a hablar de despedirme."

            elif nino_rama_beat == "tibia":

                mc_pensamiento "No dije nada. Recogí su taza y la lavé en silencio."

                mc_pensamiento "No me echó, pero tampoco me dejó quedarme de verdad."

            else:

                mc_pensamiento "Le dije que se ocupara de lo suyo y dejara de juntar los pedazos de las demás."

                mc_pensamiento "Contestó que ahora entendía por qué su padre había firmado conmigo: hablamos el mismo idioma."

                mc_pensamiento "No supe si era un insulto o la descripción más exacta que me habían dado de esa casa."

            mc_pensamiento "Entendí que no está enojada conmigo."

            if nino_visitada_cap1:

                ## --- Indicio ---

                mc_pensamiento "Aunque lo que más se me quedó fue otra cosa."

                mc_pensamiento "Lee de corrido un idioma que no es el suyo y corrige un error sin pensarlo."

                mc_pensamiento "Lo único que no puede hacer es explicarlo en voz alta sin trabarse."

                mc_pensamiento "Ahí dentro hay mucho más de lo que deja ver."

                call collage_cerrar

                play music hogar fadeout 1.5 fadein 2.0 volume 0.7

            else:

                mc_pensamiento "Con ella el ruido es una forma de cuidar a las otras."

            jump bcl_fin


        ################################################################################
        ##  MIKU
        ################################################################################

        label bcl_miku:

            $ hermanas_pensamiento.add("miku")

            call collage_abrir("miku")

            if miku_visitada_cap1:

                play music miku fadeout 1.0 fadein 1.5

                ## --- Primer encuentro y apertura ---

                mc_pensamiento "Miku fue la tercera, y la que menos ruido hizo."

                mc_pensamiento "Estaba en el sofá, con unos audífonos azules colgando del cuello y un libro de estrategas del Sengoku."

                mc_pensamiento "Le pregunté si eso eran samuráis y duelos. Dijo «no, es logística» sin levantar la vista."

                mc_pensamiento "«Las batallas las gana quien mueve el arroz.» Y se escondió detrás del libro al darse cuenta."

                mc_pensamiento "Al día siguiente, en la mesa, se subió los audífonos en cuanto saqué las hojas."

                mc_pensamiento "Me borró del mapa sin decir una palabra."

                mc_pensamiento "Al irse se detuvo en el pasillo y dijo «no fue idea mía». Y enseguida pidió perdón."

                mc_pensamiento "En su hoja había una marca de goma debajo de la respuesta equivocada."

                mc_pensamiento "Escribió la correcta primero. Y la borró."

                mc_pensamiento "Fue la única que entendió mi plan antes de que lo dijera: «quiere dividirnos»."

                ## --- Hub ---

                mc_pensamiento "En la biblioteca estaba al fondo, de espaldas a la puerta."

                mc_pensamiento "Cuatro libros que no eran del temario, apilados por tamaño y con los lomos alineados."

                mc_pensamiento "Los audífonos colgando, apagados. No los lleva para escuchar música."

                mc_pensamiento "Los lleva ahí, listos, para el momento en que alguien se acerque."

                mc_pensamiento "Esa noche me había leído su libro hasta la página noventa y dos."

                mc_pensamiento "Se quedó mirando el ejemplar sobre la mesa y, por primera vez, miró hacia fuera del libro."

                mc_pensamiento "Me contó lo de la sal de Takeda Shingen, y cómo los vecinos dejaron de vendérsela sin mover un soldado."

                mc_pensamiento "Hablaba más rápido, sin la pausa de siempre delante de cada frase."

                mc_pensamiento "Y de golpe se oyó a sí misma y dijo «perdón, hablé mucho»."

                if miku_rama_cap1 == "calida":

                    mc_pensamiento "Le hice una pregunta concreta y siguió contestando."

                    mc_pensamiento "Cuando fue a disculparse, la corté: eso no se disculpa."

                    mc_pensamiento "Me dijo que lo de la sal estaba en la página ciento veinte. Lo dijo despacio, como quien termina una cuenta."

                    mc_pensamiento "Al día siguiente me pidió que le avisara al llegar a esa página. Quería ver mi cara."

                elif miku_rama_cap1 == "tibia":

                    mc_pensamiento "Le dije que se le daba bien. Contestó que solo lo había leído."

                    mc_pensamiento "Era un halago, pero sonó a otra etiqueta más."

                    mc_pensamiento "El libro le subió hasta media cara y ahí se quedó."

                else:

                    mc_pensamiento "Le dije que el Sengoku no entraba en el examen."

                    mc_pensamiento "No protestó. Recogió sus libros, se subió los audífonos y esta vez sí sonaba la música."

                    mc_pensamiento "Dijo «hoy no»." 
                    
                    mc_pensamiento "Tenía razón en lo del examen, y aun así salí con la sensación de haber hecho algo mal."

                ## --- Indicio ---

                mc_pensamiento "No le falta saber. Eso lo tengo claro."

                mc_pensamiento "Sabe cómo se sostiene un lugar entero y por qué se cae."

                mc_pensamiento "Lo cuenta como si lo hubiera vivido. Y después borra la respuesta antes de que alguien la lea."

                call collage_cerrar

                play music hogar fadeout 1.5 fadein 2.0 volume 0.7

            else:

                mc_pensamiento "A Miku no fui a buscarla a la biblioteca."

                mc_pensamiento "Pero la recuerdo desde el sofá: los audífonos al cuello y la frase del arroz."

                mc_pensamiento "«Las batallas las gana quien mueve el arroz.» Y detrás del libro."

                mc_pensamiento "En su hoja del segundo día, una respuesta correcta borrada a medias."

                mc_pensamiento "Sabía la respuesta y no confió lo bastante en ella para dejarla ahí."

                mc_pensamiento "Fue la única que entendió mi plan antes de que lo dijera."

                mc_pensamiento "Después me dijo que así estuvo bien. Pero que habría acertado con el sitio."

                mc_pensamiento "Que hay una silla vacía enfrente de la suya, y que dejó un libro abierto dos días por si hacía falta una excusa."

                mc_pensamiento "Dijo que no pasaba nada. Y pidió perdón por haber sonado triste."

                mc_pensamiento "Es todo un misterio. Y creo que es de las que saben esperar."

            jump bcl_fin


        ################################################################################
        ##  YOTSUBA
        ################################################################################

        label bcl_yotsuba:

            $ hermanas_pensamiento.add("yotsuba")

            call collage_abrir("yotsuba")

            if yotsuba_visitada_cap1:

                play music yotsuba fadeout 1.0 fadein 1.5

                ## --- Primer encuentro y apertura ---

                mc_pensamiento "Yotsuba pasó por mi lado corriendo antes de que pudiera reaccionar."

                mc_pensamiento "Se frenó a medio metro, con una sonrisa que ocupaba media habitación."

                mc_pensamiento "«¡Vas a hacerlo genial! ...¿Verdad?» Esa última palabra le salió medio tono más baja."

                mc_pensamiento "Y se corrigió al instante: «¡Digo, claro que sí!»"

                mc_pensamiento "Esa primera tarde escribió su nombre en la hoja con un entusiasmo desmedido. Solo su nombre."

                mc_pensamiento "Después pidió perdón unas diez veces por ver cómo las demás se iban."

                mc_pensamiento "Al día siguiente intentó defenderme delante de Nino."
                
                mc_pensamiento "«Él solo está...» «Yotsuba.» «...No dije nada.»"

                mc_pensamiento "Se puso a alinear los bordes de su hoja, como si eso fuera una tarea."

                ## --- Hub ---

                mc_pensamiento "La encontré en la pista, mucho después de que el club se fuera a casa."

                mc_pensamiento "Contaba las vueltas en voz alta y se animaba sola."

                mc_pensamiento "Llevaba la cuenta anotada en la muñeca con rotulador. Si no, pierde el número."

                mc_pensamiento "Primero dijo veinticinco series. Después, treinta."

                mc_pensamiento "Dijo que sus hermanas son mejores que ella en casi todo."

                mc_pensamiento "«Yo corro y animo.» Lo dijo sonriendo, como quien dice que va a llover."

                if yotsuba_rama_cap1 == "calida":

                    mc_pensamiento "Le conté lo que yo había notado: que supo que Nino no había dormido antes de que Nino dijera nada."

                    mc_pensamiento "Que sabía qué libro buscaba Miku y si Ichika estaba cansada o preocupada."

                    mc_pensamiento "Le dije que su punto de partida no era cero. Que nunca lo había sido."

                    mc_pensamiento "En la vuelta veinticuatro ya no gritó para darse ánimos."

                    mc_pensamiento "Al día siguiente me escribió un «1» en la muñeca con un corazón torcido. Dijo que era una vuelta."

                elif yotsuba_rama_cap1 == "tibia":

                    mc_pensamiento "Le tomé el tiempo: un minuto con diecisiete."

                    mc_pensamiento "Se rió, esquivó el tema y dijo que sus piernas le hablan en un idioma secreto."

                    mc_pensamiento "No supe si la ayudé o solo la dejé correr."

                else:

                    mc_pensamiento "Le dije que se concentrara en correr."

                    mc_pensamiento "Asintió con la misma sonrisa y dejó de contar en voz alta."

                    mc_pensamiento "Al día siguiente me llamó «tutor», con el tono que se usa con un desconocido."

                    mc_pensamiento "Le confirmé la única cosa de la que nadie debería haberla convencido."

                mc_pensamiento "Cuando me fui, ya había vuelto a la pista. No se despidió, ninguno de los dos lo hizo."

                ## --- Indicio ---

                mc_pensamiento "Y sin embargo hay algo que sí lee, y lo lee mejor que yo."

                mc_pensamiento "Sabe quién está cansada, quién está preocupada y quién miente, sin que nadie se lo diga."

                mc_pensamiento "Lo hace con cinco personas a la vez, y ni siquiera lo cuenta como un mérito."

                call collage_cerrar

                play music hogar fadeout 1.5 fadein 2.0 volume 0.7

            else:

                mc_pensamiento "A Yotsuba tampoco fui a buscarla."

                mc_pensamiento "La conocí corriendo hacia mí, con una sonrisa enorme y un «¿verdad?» medio tono más bajo."

                mc_pensamiento "El primer día escribió su nombre en la hoja. Solo su nombre."

                mc_pensamiento "El segundo intentó defenderme y Nino la cortó."

                mc_pensamiento "Cuando le dije que no había tenido tiempo, repitió tres veces que no pasaba nada."

                mc_pensamiento "Pero entrenó quince minutos más cada tarde, por si yo iba. Los contó."

                mc_pensamiento "«Si nadie me necesita, ¿para qué me sobra tanta energía?»"

                mc_pensamiento "Se fue corriendo y, al doblar la esquina, bajó el ritmo."

                mc_pensamiento "Sigo sin saber qué hace cuando nadie la mira."

                mc_pensamiento "Solo la sonrisa que le pone a todo, incluso a lo que no debería sonreírse."

            jump bcl_fin


        ################################################################################
        ##  ITSUKI  (su beat de la azotea ocurrió siempre, se visitara o no el hub)
        ################################################################################

        label bcl_itsuki:

            $ hermanas_pensamiento.add("itsuki")

            call collage_abrir("itsuki")

            if itsuki_visitada_cap1:

                play music itsuki fadeout 1.0 fadein 1.5

                ## --- Primer encuentro y apertura ---

                mc_pensamiento "A Itsuki la conocí antes de saber su nombre."

                mc_pensamiento "Estaba sentada en mi sitio, almorzando, y me pidió que le enseñara un poco."

                mc_pensamiento "Le dije que no. Que aprender es un proceso personal."

                mc_pensamiento "Me devolvió una frase que todavía recuerdo: arrogante y carente de empatía."

                mc_pensamiento "Esa tarde nos cruzamos en la azotea. Nos quedamos en silencio, cada uno en un extremo del banco."

                mc_pensamiento "Y por la noche, en la puerta del departamento, descubrí que ella vivía ahí."

                mc_pensamiento "Dijo que prefería reprobar todos los exámenes antes que recibir una sola clase mía."

                mc_pensamiento "Hay algo de ese primer día que sigo sin saldar con ella."

                mc_pensamiento "Al día siguiente me dejó mi asiento libre a propósito. Eso también era un mensaje."

                mc_pensamiento "Dijo que no pensaba estudiar conmigo."
                
                mc_pensamiento "Aun así, fue ella quien se inventó el juego de busca y encuentra."

                mc_pensamiento "Y dijo que no pensaba esconderse. Que estaría donde siempre."

                ## --- Hub ---

                mc_pensamiento "Estaba en el aula vacía, con la luz entrando de lado."

                mc_pensamiento "Tenía el lápiz levantado, quieto, y tres respuestas tachadas con la misma cifra al final."

                mc_pensamiento "«El tiempo que hace falta», contestó. Y lo repitió palabra por palabra. Eso la delató."

                mc_pensamiento "Dijo que las otras podían decir que no lo habían intentado. Que ella no tenía esa excusa."

                mc_pensamiento "Y enseguida: «olvida lo que dije»."

                mc_pensamiento "Se hundió sobre el cuaderno, y entendí por qué no le preguntaba a nadie."

                mc_pensamiento "Preguntarle a sus hermanas era admitir algo. Preguntarme a mí, darme la razón."

                mc_pensamiento "No era que no supiera resolverlo. Arrastraba el mismo error del medio sin tocarlo."

                if itsuki_rama_cap1 == "calida":

                    mc_pensamiento "Le señalé el segundo paso, sin decirle qué estaba mal."

                    mc_pensamiento "Lo encontró ella sola: «la unidad no se cancela ahí»."

                    mc_pensamiento "No me dio las gracias. Tampoco me pidió que me fuera."

                    mc_pensamiento "Al día siguiente me contó que había rehecho el ejercicio desde el principio, sin mirar la corrección."

                    mc_pensamiento "Salió bien."

                elif itsuki_rama_cap1 == "tibia":

                    mc_pensamiento "Le ofrecí revisarlo desde el principio y dijo que no antes de saber qué iba a explicarle."

                    mc_pensamiento "Cerró el cuaderno un centímetro, lo justo para rechazar la oferta."

                    mc_pensamiento "Al día siguiente dijo que todavía no necesitaba mi ayuda. Y que «todavía» era solo una expresión."

                else:

                    mc_pensamiento "Le quité el cuaderno y se lo resolví yo, de pie, con su propio lápiz."

                    mc_pensamiento "Rápido y correcto. Y le quité lo único que estaba defendiendo: hacerlo ella sola."

                    mc_pensamiento "Al día siguiente había rehecho todo el ejercicio debajo de mi solución, tachada."

                    mc_pensamiento "«Lo que hiciste ayer no cuenta. Quería que fuera mío.»"

            else:

                mc_pensamiento "No fui a buscarla al aula."

                mc_pensamiento "A Itsuki la conocí por un asiento, y ella a mí por arrogante. No le faltó razón."

                mc_pensamiento "Dijo que prefería reprobar todos los exámenes antes que recibir una clase mía."

                mc_pensamiento "Aun así, fue ella quien se inventó el juego de busca y encuentra."

                mc_pensamiento "Cuando supo que no la había ido a buscar, dijo que había ganado el juego."

                mc_pensamiento "Que tener razón es lo único que siempre le sale bien."

                mc_pensamiento "Y que, si hubiera ido, no me habría echado. No inmediatamente."

            ## --- Beat de la azotea (siempre) ---

            mc_pensamiento "Unos días después subí a la azotea y estaba ahí, con el cuaderno cerrado sobre las rodillas."

            if not itsuki_visitada_cap1:

                mc_pensamiento "Antes de que lo cerrara alcancé a ver la página: un ejercicio con un círculo a lápiz."

                mc_pensamiento "Repasado tantas veces que había hundido el papel. Era el de la hoja de diagnóstico del primer día."

            mc_pensamiento "Ya no le quedaba ningún sitio donde no tuviera que estudiar."

            mc_pensamiento "Tenía las manos quietas sobre la tapa, sin una mancha de tinta."

            mc_pensamiento "Nos quedamos un rato largo sin abrir ninguno de los dos libros."

            mc_pensamiento "Se me voló una hoja hasta la valla y ninguno fue a buscarla."

            mc_pensamiento "Esas semanas la estaban gastando a ella tanto como a mí."

            if itsuki_visitada_cap1:

                ## --- Indicio ---

                mc_pensamiento "Y sigo dándole vueltas a lo mismo."

                mc_pensamiento "Plantea bien, un problema tras otro. El resto de su cuaderno no tenía un solo error."

                mc_pensamiento "A veces le basta con que alguien le diga dónde mirar para ver todo lo demás."

                mc_pensamiento "Lo que le falta no es método. Tampoco es esfuerzo."

                call collage_cerrar

                play music hogar fadeout 1.5 fadein 2.0 volume 0.7

            else:

                mc_pensamiento "Lo que sea que le pase, no es falta de esfuerzo."

                mc_pensamiento "Y tampoco sé cómo hacer que deje de fingir que está bien."

            jump bcl_fin

    
    ############################################################################
    ##  MOVIMIENTO 5 · CIERRE
    ##  Final del beat, lineas rápidas y cortas para dar inicio al evento
    ##  final del capitulo 1
    ############################################################################

    scene bg_cuarto_mc
    with fade

    mc_pensamiento "Cerré la libreta y apagué la lámpara."

    narrador "Desde el otro cuarto, todavía se oía a Raiha ordenando sus cosas para el día siguiente."
    
    narrador "Como si mañana fuera un día cualquiera."

    mc_pensamiento "Para ella lo es."

    mc_pensamiento "Ojalá pudiera decir lo mismo."

    narrador "Mañana será el examen."                     
        
    return 
    