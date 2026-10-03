################################################################################
##  BGs Y CGs PROPIOS DEL BEAT DE LA CASA 
##  Solo 1 ilustración y 1 SFX nuevos de momentos concretos de este beat.
##  Los que el beat reutiliza son todos los sprites BGM, SFX y algunos
##  BGs y CGs ya existetes
################################################################################

image cg_raiha_correccion = "images/cg/cap1_beats/raiha_correccion.webp"

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

    mc_pensamiento "Han pasado treinta días."

    mc_pensamiento "Contados desde la noche en que anoté los cinco nombres."

    mc_pensamiento "Mañana sabré si sirvieron de algo."

    narrador "Raiha estaba en la mesa, con su propio cuaderno abierto y la cena ya servida y fría."

    show raiha hablando at pj(0.20)
    with dissolve

    raiha "¡Hermanito!" 
    
    raiha "Te guardé la cena, pero se enfrió como tres veces."

    mc "Perdoname Raiha." 
    
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
    with fade

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

    #[SFX sfx_lapiz_mesa NUEVO volume 1.5]

    narrador "Dejó el lápiz sobre la mesa, despacio."

    raiha "…Hablaste raro."

    mc "¿Raro cómo?"

    raiha "Como un profesor." 
    
    raiha "Ni pareces mi hermano cuando dices esas cosas."

    narrador "Lo dijo sin mala intención." 
    
    narrador "Con la misma naturalidad con la que señala cualquier otra cosa."

    mc_pensamiento "No fue un chiste." 
    
    mc_pensamiento "Se lo tomó como algo raro de verdad."

    mc_pensamiento "Llevo semanas diciéndoles a cinco personas «no te lo voy a resolver, 
    solo mira si está bien» tantas veces que ya no me sale de otra forma"
    
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
    with fade

    play sound sfx_puerta_abre volume 1.0

    narrador "Mi padre entró cuando Raiha ya estaba guardando el cuaderno."

    show isanari neutral at pj(0.73)
    with dissolve

    isanari "Vaya [mc], te ves demasiado cansado."

    isanari "¿Como vas? ¿Todo marcha bien en tu trabajo?"

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
    with fade
    
    play music hogar fadein 3.0 volume 0.7

    mc_pensamiento "Cinco nombres, en columna, con una línea debajo."

    mc_pensamiento "Treinta días después, la letra sigue siendo la misma."

    mc_pensamiento "Solo que ahora sé lo que cuesta cada nombre."

    narrador "Dejé la vista quieta un momento antes de cerrarla."

    if desaires_cap1 >= 3:

        mc_pensamiento "No sé si mañana esto sigue siendo mi trabajo."

        mc_pensamiento "Ninguna aprobó todavía."

        mc_pensamiento "Y las cinco llegan a este último tramo por caminos que yo elegí."

        mc_pensamiento "Uno a uno, sin preguntarles si querían que fuera así."

        mc_pensamiento "Si mañana me voy, me voy sabiendo exactamente por qué."

        mc_pensamiento "Todo el peso de mis decisiones caerá mañana."

    else:

        $ hermanas_pensamiento = set()

        label cap1_hermanas_pensamiento:

            ## Menú del sabor

            menu:

                "¿En qué nombre te fijas más tiempo?"
                
                "Ichika" if "ichika" not in hermanas_pensamiento:

                    $ hermanas_pensamiento.add("ichika")

                    if ichika_visitada_cap1:

                        mc_pensamiento "La encontré dormida en el salón del club."

                        mc_pensamiento "Con el guion resbalándole de la mano."

                        mc_pensamiento "A su lado, dos latas de energizante."

                        mc_pensamiento "Una de ellas, abollada."

                        if ichika_rama_cap1 == "calida":

                            mc_pensamiento "Cuando despertó a medias, dijo que no sabía cuánto más podía seguir así."

                            mc_pensamiento "No sé si me lo dijo a mí o si se le escapó sin querer."

                            mc_pensamiento "Después volvió la sonrisa, como si nada."

                            mc_pensamiento "Pero tardó un segundo de más en volver."

                        elif ichika_rama_cap1 == "tibia":

                            mc_pensamiento "Nos pusimos a hablar de tonterías, y ella se rió de verdad."

                            mc_pensamiento "No sé si eso cuenta como ayudarla." 
                            
                            mc_pensamiento "Probablemente no."

                        else:

                            mc_pensamiento "Le dije que si tenía tiempo para chistes, tenía tiempo para estudiar."

                            mc_pensamiento "Salimos sin decir nada y ella sonrió como siempre"

                            mc_pensamiento "Fue correcta conmigo. Nada más."

                        mc_pensamiento "Entiendo cómo se siente. Yo también tengo personas a quien cuidar."

                        mc_pensamiento "Hasta medio dormida, calculó minutos y trenes sin pensarlo dos veces."

                        mc_pensamiento "Sé que esa cabeza para los números la va a hacer sobresalir en su examen, aunque ella no se dé cuenta."

                        mc_pensamiento "Antes de irnos, le llegó un mensaje: un papel nuevo para la obra de primavera."

                        mc_pensamiento "Dijo que sí sin pensarlo, aunque ya no le quedaba tiempo para nada más."

                        mc_pensamiento "Ni siquiera respondió el mensaje. Solo lo guardó, como guarda todo lo demás."
                        
                    else:

                        mc_pensamiento "No he interactuado mucho con ella desde el primer día,"

                        mc_pensamiento " cuando fingía que nada de esto le importaba."

                        mc_pensamiento "Sigue actuando igual que siempre frente a mí, sin ninguna grieta de por medio." 

                        mc_pensamiento "No sé si sigue fingiendo o si dejó de hacerlo..."


                "Nino" if "nino" not in hermanas_pensamiento:

                    $ hermanas_pensamiento.add("nino")

                    if nino_visitada_cap1:

                        mc_pensamiento "Nino me corrigió una frase en inglés. No se lo pedí pero lo hizo."

                        mc_pensamiento "Luego, la encontré en una sección de repostería internacional, "
                        
                        mc_pensamiento " tenia productos con nombres extranjeros, algunos que ni siquiera sabía su significado."

                        mc_pensamiento "La encontré comparando dos cajas de harina, con una receta que no es suya escrita a mano."

                        mc_pensamiento "Logré interactuar con ella acerca de los nombres de esos productos."

                        mc_pensamiento "Con dificultad para entablar una conversacion pacifica..."

                        mc_pensamiento "Me di cuenta que tiene un talento innato para el ingles."

                        mc_pensamiento "Aunque le cuesta hablarlo de manera fluida, sabe como leerlo y pronunciarlo."

                        mc_pensamiento "Tambien me dijo que ya perdió la cuenta de cuántos tutores vio irse."

                        mc_pensamiento "Yo no le prometí nada, no logré convencerla de lo contrario."

                        if nino_rama_cap1 == "calida":

                            mc_pensamiento "Le dije que no le iba a prometer que esta vez fuera distinto."
                            
                            mc_pensamiento "Dijo que era la primera vez que alguien no le prometía nada."
                            
                            mc_pensamiento "No gané su confianza. Tampoco se la pedí."
                        
                            mc_pensamiento "Pero por primera vez no me trató como al siguiente de la fila."

                        elif nino_rama_cap1 == "tibia":

                            mc_pensamiento "No le dije nada. Solo le cargué una de las bolsas."
                            
                            mc_pensamiento "Hicimos el resto del pasillo en silencio."
                            
                            mc_pensamiento "No sé si eso cuenta como algo. Con ella, nunca se sabe."

                        else:

                            mc_pensamiento "Le prometí que yo sí iba a durar."
                        
                            mc_pensamiento "Ella ya había escuchado esa frase antes, casi palabra por palabra."
                        
                            mc_pensamiento "Yo mismo me puse en la misma fila que los anteriores."


                        mc_pensamiento "Y por último, ese dia, en su cocina."
                        
                        mc_pensamiento "Estuve escuchándola pedirle a su padre que me echara."
                        
                        mc_pensamiento "Se frenó antes de decir por qué."
                        
                        mc_pensamiento "Pero entendí que no está enojada conmigo."
                        
                        mc_pensamiento "Ella es un tren de emociones que nunca frena."

                    else:

                        mc_pensamiento "No fui a buscarla al centro comercial."

                        mc_pensamiento "Pero igual terminé en su cocina, escuchándola pedirle a su padre que me echara."

                        mc_pensamiento "Se frenó antes de decir por qué."

                        mc_pensamiento "Pero entendí que no está enojada conmigo."
                        

                "Miku" if "miku" not in hermanas_pensamiento:

                    $ hermanas_pensamiento.add("miku")

                    if miku_visitada_cap1:

                        mc_pensamiento "La encontré en la biblioteca."

                        mc_pensamiento "Con cuatro libros que no eran del temario."

                        mc_pensamiento "Apilados por tamaño y con los lomos alineados."

                        mc_pensamiento "Lleva los audífonos colgados del cuello, apagados."

                        mc_pensamiento "No son para escuchar música — "

                        mc_pensamiento " son para subírselos en cuanto alguien se acerca."

                        if miku_rama_cap1 == "calida":

                            mc_pensamiento "Le hice preguntas concretas sobre lo que leía y no la dejé disculparse por contestarlas."
                            
                            mc_pensamiento "Sabía en qué página del libro estaba cada dato, como quien ya se lo aprendió de memoria."
                            
                            mc_pensamiento "Le dije que lo que sabe cuenta como saber." 
                            
                            mc_pensamiento "No me lo discutió."

                        elif miku_rama_cap1 == "tibia":

                            mc_pensamiento "Le dije que se le daba bien esto, sin pensar que la estaba comparando con sus hermanas otra vez."
                            
                            mc_pensamiento "Cerró la puerta con educación: dijo que eso no era difícil."
                            
                            mc_pensamiento "El libro le subió hasta media cara, y ahí se quedó."

                        else:

                            mc_pensamiento "Le dije que eso no entraba en el examen."
                            
                            mc_pensamiento "No protestó. Recogió los libros y se subió los audífonos."
                            
                            mc_pensamiento "Esta vez sí se oía la música." 
                            
                            mc_pensamiento "Antes no sonaban."


                        mc_pensamiento "En su hoja del segundo día había una respuesta correcta borrada a medias."

                        mc_pensamiento "Sabía la respuesta, pero no confió lo suficiente en ella misma para dejarla ahí."

                        mc_pensamiento "Es una chica muy reservada."

                        mc_pensamiento "Pero cuando la conoces es una persona totalmente interesante."

                        mc_pensamiento "Confío en que hará brillar sus conocimientos de historia, en cuanto deje de disculparse por tenerlos."

                    else:

                        mc_pensamiento "Sigo sin saber mucho de ella."

                        mc_pensamiento "Los audífonos que lleva puestos en su cuello."

                        mc_pensamiento "Y el libro que escondió la primera noche."

                        mc_pensamiento "Ella es todo un misterio."


                "Yotsuba" if "yotsuba" not in hermanas_pensamiento:

                    $ hermanas_pensamiento.add("yotsuba")

                    if yotsuba_visitada_cap1:

                        mc_pensamiento "La encontré corriendo sola en la pista."

                        mc_pensamiento "Mucho después de que el club se fuera a casa."

                        mc_pensamiento "Lleva las vueltas anotadas en la muñeca."

                        mc_pensamiento "Si no, pierde la cuenta."

                        mc_pensamiento "Es una chica muy energetica y positiva."

                        mc_pensamiento "Siempre intenta verle el lado bueno a las cosas."

                        mc_pensamiento "Pero en el fondo, es alguien que tiene miedo a ser olvidada o no ser de utilidad para los demás."

                        mc_pensamiento "Dijo que sus hermanas tienen algo cada una, y que ella solo corre y anima."

            
                        if yotsuba_rama_cap1 == "calida":

                            mc_pensamiento "Le dije que nota cosas de sus hermanas que yo ni siquiera veo."
                            
                            mc_pensamiento "Me preguntó si eso era verdad o si solo soy bueno animando a la gente."
                            
                            mc_pensamiento "Todavía no lo sé." 
                            
                            mc_pensamiento "Pero cuando volvió a correr, ya no sonaba igual de insegura."

                        elif yotsuba_rama_cap1 == "tibia":

                            mc_pensamiento "Le tomé el tiempo con el cronómetro, un par de vueltas más."
                            
                            mc_pensamiento "No dijo nada más de lo que ya había dicho antes."
                            
                            mc_pensamiento "No sé si le ayudé en algo o si solo la dejé seguir corriendo."

                        else:

                            mc_pensamiento "Le dije que se concentrara en correr, ya que es lo suyo."
                            
                            mc_pensamiento "Dejó de contar las vueltas en voz alta después de eso."
                            
                            mc_pensamiento "Puede que le haya confirmado la única cosa de la que nadie debería haberla convencido nunca."


                        mc_pensamiento "Animar a cinco personas distintas."

                        mc_pensamiento "Cada una a su manera, no es tan simple como ella lo hace sonar."

                        mc_pensamiento "Sospecho que se le da mejor leer a la gente de lo que ella misma cree."

                        mc_pensamiento "Si."

                        mc_pensamiento "Eso es."

                    else:

                        mc_pensamiento "Sigo sin saber qué hace cuando nadie la mira."

                        mc_pensamiento "Solo la sonrisa que le pone a todo, incluso a lo que no debería sonreírse."

                        mc_pensamiento "¿Así será cuando nadie la ve?"

                        mc_pensamiento "¿O solo es una mascara?"

                        mc_pensamiento "No lo sé." 


                "Itsuki" if "itsuki" not in hermanas_pensamiento:

                    $ hermanas_pensamiento.add("itsuki")

                    if itsuki_visitada_cap1:

                        mc_pensamiento "La encontré atascada en un ejercicio de ciencias."

                        mc_pensamiento "Sola en el aula."

                        mc_pensamiento "Con tres intentos tachados y la misma respuesta equivocada las tres veces."

                        mc_pensamiento "No era que no supiera del tema."

                        mc_pensamiento "El resto del cuaderno estaba lleno de ejercicios resueltos."

                        mc_pensamiento "Uno detrás de otro, sin un solo error."

                        if itsuki_rama_cap1 == "calida":

                            mc_pensamiento "Le señalé que el error estaba más atrás, en el segundo paso, sin decirle cuál era."
                            
                            mc_pensamiento "Ella misma lo encontró y corrigió el ejercicio entera."
                            
                            mc_pensamiento "No me dio las gracias."
                            
                            mc_pensamiento "Tampoco me pidió que me fuera."

                        elif itsuki_rama_cap1 == "tibia":

                            mc_pensamiento "Le pregunté si quería que lo repasáramos desde el principio."
                            
                            mc_pensamiento "Dijo que no, sin siquiera dejarme explicarle de qué se trataba."
                        
                            mc_pensamiento "Cuando volví a pasar por su pupitre, seguía atascada en la misma línea."

                        else:

                            mc_pensamiento "Le quité el cuaderno de las manos y se lo resolví yo mismo."
                        
                            mc_pensamiento "Ahí de pie, con su propio lápiz."
                            
                            mc_pensamiento "Fue rápido y correcto."
                            
                            mc_pensamiento "Y le quité lo único que estaba defendiendo: hacerlo ella sola."

                    else:

                        mc_pensamiento "No fui a buscarla al aula."

                        mc_pensamiento "Pero igual la encontré en la azotea."

                        mc_pensamiento "Con un cuaderno que no llegó a abrir."

                        mc_pensamiento "Ya no le queda ningún sitio donde no tenga que fingir que está bien."

                        mc_pensamiento "Y tampoco se como hacer que se sienta bien"


            if len(hermanas_pensamiento) < 5:
                jump cap1_hermanas_pensamiento

    
    ############################################################################
    ##  MOVIMIENTO 5 · CIERRE
    ##  Final del beat, lineas rápidas y cortas para dar inicio al evento
    ##  final del capitulo 1
    ############################################################################

    mc_pensamiento "Cerré la libreta y apagué la lámpara."

    narrador "Desde el otro cuarto, todavía se oía a Raiha ordenando sus cosas para el día siguiente."
    
    narrador "Como si mañana fuera un día cualquiera."

    mc_pensamiento "Para ella lo es."

    mc_pensamiento "Ojalá pudiera decir lo mismo."

    stop music fadeout 3.0

    narrador "Mañana será el examen."                     
        
    return 
    