################################################################################
##  BGs Y CGs PROPIOS DEL HUB DE ICHIKA 
##  3 ilustraciones y 1 fondo nuevos de momentos concretos de este hub. Los que
##  el hub reutiliza son todos los sprites de Ichika, de ahí se crea un 
##  nuevos sprite que se definen en 00_definiciones
################################################################################

image bg_sala_ensayo = "images/bg/hubs_hermanas/sala_ensayo.webp"

image bg_sala_ensayo_anochecer = Transform(
    "images/bg/hubs_hermanas/sala_ensayo.webp",
    matrixcolor = BrightnessMatrix(-0.06) * SaturationMatrix(0.88) * TintMatrix("#e0d8f0")
)

image cg_ichika_ensayo = "images/cg/hubs_hermanas/ichika_ensayo.webp"

image cg_ichika_desarmada = "images/cg/hubs_hermanas/ichika_desarmada.webp"

image cg_ichika_mascara = "images/cg/hubs_hermanas/ichika_mascara.webp"

################################################################################
##  HUB DE ICHIKA
##  Primer encuentro entre mc e Ichika en la sala de ensayo del club de teatro.
##  Ichika no tiene energía, y el jugador puede notar que algo no está bien.
################################################################################

label hub_Ichika:

    $ sumar_punto("ichika", 2)

    # Si el jugador eligió la sala de ensayo en el hub 1, se marca la primera
    # conexión. Ajustar el string si el hub usa otra clave para este destino.
    #if hub_choice == "sala_ensayo":
    #    $ primera_conexion = True

    ############################################################################
    ##  MOVIMIENTO 1 · Llegada
    ##  Futaro encuentra a Ichika dormida en la sala de ensayo del club de teatro,
    ##  con latas de energizante y un guión colgado a mano
    ############################################################################

    scene sala_ensayo 
    with fade

    stop music fadeout 1.0

    narrador "El club de teatro tenía un cuarto propio detrás del auditorio."

    narrador "Nadie me dijo que llamara antes de entrar."

    narrador "La puerta estaba entreabierta."

    narrador "Y fue ahí cuando la ví."

    scene ichika_ensayo
    with fade

    narrador "La reconocí por el pelo antes que por la cara."

    mc_pensamiento "Está dormida."

    mc_pensamiento "Sentada en el suelo. Con el guion en la mano."

    narrador "A su lado había dos latas de energizante."

    narrador "Una de ellas abollada, como si la hubiera apretado sin darse cuenta."

    mc_pensamiento "Y un horario escrito a mano, con tres columnas superpuestas."

    mc_pensamiento "Clases. Ensayos. Algo tachado que no llegué a leer."

    narrador "Me quedé en la puerta un momento, sin saber si entrar o retroceder."

    narrador "Decidí entrar."

    narrador "Me acerqué despacio, tratando de no hacer ruido con los pasos."

    mc_pensamiento "No sabía si despertarla o dejarla dormir un poco más."

    mc_pensamiento "No llegué a decidirlo."

    play sound sfx_hoja volume 1.0

    narrador "El guion terminó de resbalarle de la mano y cayó al piso."

    narrador "Eso la despertó."

    ############################################################################
    ##  MOVIMIENTO 2 · La grieta
    ##  Se despierta sin la actuación encendida todavía. Dura medio segundo.
    ##  Se da cuenta de que perdió toda la tarde durmiendo.
    ############################################################################

    scene bg_sala_ensayo
    with fade

    narrador "Abrió los ojos de golpe, sin saber todavía dónde estaba."

    scene cg_ichika_desarmada
    with fade

    ichika "…¿[mc]?"

    ichika "¿Qué haces aquí?"

    ichika "…¿Qué hora es?"

    narrador "Me preguntó sin actuación, sin la voz que usa para todo."

    mc "Las cuatro y media."

    ichika "…"

    ichika "Perdí la tarde entera."

    narrador "Lo dijo plano. Sin exclamación."

    narrador "Sin la pausa que pone antes de un chiste."

    mc_pensamiento "Esa no es su voz normal."

    mc_pensamiento "Su voz normal tiene dirección de escena."

    mc_pensamiento "Esta no tenía ninguna."

    narrador "Duró medio segundo."

    narrador "Después pareció darse cuenta de que yo estaba ahí, y de que la había visto así."

    scene bg_sala_ensayo
    with fade

    show ichika agotada at pj(0.5)
    with dissolve

    mc "Luces demasiado cansada"

    ichika "¿Yo?"

    ichika "Jaja, te preocupas demasiado por mi [mc]"

    mc "¿Entonces que estabas haciendo?"

    ichika "¡Estaba practicando!"

    mc "¿Practicando dormir?"

    ichika "¡Es un método actoral! ¡Se llama sueño escénico!"

    mc "No existe eso."

    show ichika sonriendo at pj(0.5)
    with disolucion_lenta

    ichika "¡Claro que existe! ¡Lo inventé yo hace cinco minutos!"

    narrador "Se rió de su propio chiste, un poco más fuerte."

    mc_pensamiento "Cambió de tema tan rápido que casi no lo noto."

    mc_pensamiento "Casi."

    narrador "Se puso de pie y se sacudió la falda."

    narrador "Recogió el guion del suelo con un solo movimiento, como si llevara ensayado también eso."

    mc "¿Cuánto tiempo dormiste anoche?"

    show ichika neutral at pj(0.5)
    with disolucion_lenta

    ichika "¡Lo suficiente!"

    mc "Eso no es un número."
   
    ichika "¿Y desde cuándo un tutor de matemáticas pide cifras exactas de otras cosas?"

    narrador "Lo dijo con una sonrisa, pero cambió de tema otra vez, y esta ya era la segunda."

    narrador "Guardó el horario doblándolo rápido."

    narrador "Más rápido de lo necesario, antes de que yo pudiera leer lo que estaba tachado."

    mc "¿Cuándo puedo verte para la próxima lección?"

    narrador "Se lo pregunté sin pensar mucho, solo para cambiar de tema yo también."

    ichika "Martes a las cinco y veinte. Nunca antes de eso."

    mc "¿Por qué no a las cinco y media, si total es casi lo mismo?"

    ichika "Porque el tren de las cuatro cuarenta y cinco tarda seis minutos en llegar a la estación desde aquí, y necesito cuatro para cambiarme."

    mc_pensamiento "Vaya, tiene un horario muy bien cronometrado."

    mc_pensamiento "Lo cual me preocupa bastante"

    mc "Lo dijiste sin pausar, sin contar con los dedos, como si ya tuvieras la cuenta hecha de memoria."

    mc "Nadie improvisa ese número tan rápido."

    show ichika sonriendo at pj(0.5)
    with disolucion_lenta

    ichika "¡Es que soy muy organizada! ¡Parte del oficio!"

    narrador "Se rió, tapando otra vez algo que se le había escapado sin querer."

    mc_pensamiento "Dos latas de energizante."

    mc_pensamiento "Un horario con algo tachado que no quiere que vea."

    mc_pensamiento "Una cuenta de minutos que le salió demasiado rápido."

    mc_pensamiento "Y ahora esto."

    mc_pensamiento "Ninguna de las cuatro cosas es una casualidad sola."

    mc_pensamiento "Juntas, son un patrón."

    ############################################################################
    ##  MOVIMIENTO 3 · La decisión
    ##  El jugador decide si le da tiempo en silencio, si sigue la broma, o si
    ##  la confronta directamente.
    ############################################################################

    # [MUS NUEVO — descubrimiento, volumen 0 listo para subir]

    scene cg_ichika_mascara
    with fade

    narrador "Se sentó en una de las sillas plegables."

    narrador "Con el guion otra vez en la mano, y pasó una página sin leerla."

    ichika "Bueno, ¿viniste a verme actuar o viniste a regañarme?"

    mc "Vine a buscarte para las clases de mañana."

    ichika "¡Qué aburrido!"

    ichika "Yo esperaba algo con más drama."

    narrador "Sonrió, esperando la broma de vuelta."

    narrador "La que suele devolverle cualquiera que hable con ella."

    scene bg_sala_ensayo
    with fade

    show ichika agotada at pj(0.5)
    with dissolve

    mc_pensamiento "Tres cosas que acabo de ver y que ella escondió detrás de un chiste."

    mc_pensamiento "Si le sigo la broma, la cuarta también va a quedar oculta."

    mc_pensamiento "Y no va a haber una quinta oportunidad hoy."

    menu:

        "¿Cómo respondes?"

        "No decir nada. Sostenerle la mirada en silencio, dándole tiempo.":
            jump ichika_m4a

        "Ceder. Reírte de la broma y dejar que oculte el tema.":
            jump ichika_m4b

        "\"Si tienes energía para hacer chistes, tienes energía para estudiar.\"":
            jump ichika_m4c


############################################################################
##  MOVIMIENTO 4A · Rama cálida — Silencio
############################################################################

label ichika_m4a:

    $ ichika_rama_cap1 = "calida"
    $ sumar_punto("ichika", 1)

    # [MUS descubrimiento — fade in volumen 3.5]

    narrador "No dije nada."

    narrador "Me quedé de pie, mirándola, sin devolverle el chiste."

    show ichika neutral at pj(0.5)
    with disolucion_lenta

    ichika "…¿Qué?"

    mc "Nada."

    ichika "No pusiste cara de nada."

    ichika "Pusiste cara de estar esperando algo."

    mc "Puede ser."

    narrador "El silencio se estiró más de lo que suele durar entre los dos."

    narrador "Ella fue la que lo rompió, y lo hizo sin la sonrisa de antes."

    show ichika agotada at pj(0.5)
    with disolucion_lenta

    ichika "…No sé cuánto más puedo seguir haciendo esto."

    mc "¿Esto qué?"

    ichika "Todo."

    ichika "Las audiciones. Las clases."

    ichika "Fingir que puedo con las dos."

    narrador "Lo dijo sin exclamación."

    narrador "La primera frase larga de toda la tarde sin una sola."

    mc "No dije que no pudieras."

    ichika "No hacía falta."

    ichika "Yo también me lo digo, y no me lo creo ni cuando lo digo yo."

    narrador "Se quedó mirando el guion, sin pasar la página."

    mc_pensamiento "La semana pasada faltó a algo. No sé a qué."

    mc_pensamiento "Y por como dobló ese horario, tampoco creo que se lo haya contado a nadie."

    show ichika neutral at pj(0.5)
    with disolucion_lenta

    ichika "…"

    ichika "¿No vas a decir nada aprovechado sobre esto?"

    mc "¿Cómo qué?"

    ichika "No sé. Algo de tutor."

    ichika "\"Si estás cansada, deberías dormir más.\""

    mc "Eso ya lo sabes tú sola."

    narrador "Sonrió, esta vez más despacio, sin la energía de antes."

    show ichika sonriendo at pj(0.5)
    with disolucion_lenta

    ichika "…Gracias por no decir la frase obvia."

    narrador "Guardó el guion en la mochila, todavía sin la actuación completa de vuelta."

    mc_pensamiento "Volvió la sonrisa. Pero tardó, y no vino con exclamación."

    mc_pensamiento "Es la primera vez que la veo actuar despacio."

    jump ichika_m5


############################################################################
##  MOVIMIENTO 4B · Rama tibia — Seguirle la broma
############################################################################

label ichika_m4b:

    $ ichika_rama_cap1 = "tibia"
    ## sin puntos, sin desaire

    show ichika sonriendo at pj(0.5)
    with disolucion_lenta

    mc "Con más drama, entonces."

    mc "Entras corriendo, gritando mi nombre."

    ichika "¡Eso ya lo hice el primer día! Hay que innovar."

    mc "¿Qué tal un dragón?"

    ichika "¡Un dragón que además sabe matemáticas!"

    ichika "¡Perfecto para ti!"

    narrador "Se rió, esta vez de verdad, y la conversación se fue por ahí un rato."

    mc_pensamiento "Es una buena broma. Las suyas siempre lo son."

    mc_pensamiento "Pero seguimos hablando de dragones y no de las dos latas de energizante."

    ichika "¡Y el dragón tendría que usar lentes! ¡Para verse serio con los números!"

    mc "Los dragones no necesitan lentes."

    ichika "¡Este sí! ¡Es miope de tanto leer contratos de audición!"

    narrador "Siguió inventando detalles del dragón durante un rato más, cada uno más absurdo que el anterior."

    mc_pensamiento "Cuanto más se ríe, menos espacio queda para preguntar nada en serio."

    narrador "Guardó el guion en la mochila sin volver a mirarlo."

    ichika "Bueno, vamos, antes de que se haga de noche."

    mc_pensamiento "No dijo nada más de lo que vi al entrar."

    mc_pensamiento "Y yo tampoco insistí."

    jump ichika_m5


############################################################################
##  MOVIMIENTO 4C · Rama fría
############################################################################

label ichika_m4c:

    $ ichika_rama_cap1 = "fria"
    $ desaires_cap1 += 1

    mc "Si tienes tiempo para esto, tienes tiempo para estudiar."

    show ichika neutral at pj(0.5)
    with disolucion_lenta

    narrador "La sonrisa no desapareció del todo, pero algo detrás de ella sí."

    ichika "…"

    ichika "Ya veo."

    narrador "Lo dijo con la voz más parecida a la de un adulto que le hubiera oído usar."

    show ichika sonriendo at pj(0.5)
    with disolucion_lenta

    ichika "¡Tienes razón! ¡Debería aprovechar mejor el tiempo!"

    narrador "Guardó el guion de un solo movimiento, rápido."

    narrador "Sin doblar las páginas con cuidado como antes."

    mc_pensamiento "Dije exactamente lo que un padre le diría."

    mc_pensamiento "Y ella me contestó exactamente lo que le contesta a un padre."

    narrador "Salió primero, sosteniendo la puerta apenas el tiempo justo para no dejarla cerrarse en mi cara."

    mc_pensamiento "No fue grosera. Fue correcta."

    mc_pensamiento "Y eso, viniendo de ella, es peor que un portazo."

    jump ichika_m5


############################################################################
##  MOVIMIENTO 5 · Cierre
##  Común a las tres ramas; el cierre final cambia según ichika_rama_cap1.
############################################################################

label ichika_m5:

    hide ichika 
    with dissolve

    scene bg_sala_ensayo_anochecer
    with fade

    stop music fadeout 1.5

    narrador "Salimos cuando el conserje empezaba a apagar las luces del pasillo."

    mc_pensamiento "Una de cinco." 
    
    mc_pensamiento "Y esta se durmió antes de que yo dijera nada."

    mc_pensamiento "Quedan tres semanas."

    
    if ichika_rama_cap1 == "calida":

        mc_pensamiento "Dijo que no sabía cuánto más podía seguir así."

        mc_pensamiento "No sé si me lo dijo a mí o si se le escapó."

        mc_pensamiento "Tampoco sé si hay diferencia."

    elif ichika_rama_cap1 == "tibia":

        mc_pensamiento "Hablamos de dragones durante diez minutos."

        mc_pensamiento "Fue divertido."

        mc_pensamiento "No estoy seguro de que haya sido nada más que eso."

        mc_pensamiento "No hubo ningún cambio en ella."

        mc_pensamiento "Siento como si no hubiera hecho nada para ayudarla"

    else:

        mc_pensamiento "Tenía razón en lo que dije." 
        
        mc_pensamiento "Pero no me hace sentir mejor."

        mc_pensamiento "Sostuvo la puerta el tiempo justo. Ni un segundo más."

    # Marca el evento como consumido para el evento 6 y para que el hub
    # ofrezca la revisita corta en lugar del evento completo.
    $ ichika_visitada_cap1 = True

    jump hub
