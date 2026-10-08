################################################################################
##  BGs Y CGs PROPIOS DEL BEAT DE ITSUKI 
##  2 ilustraciones, 1 BGM y 1 SFX nuevos de momentos concretos de este beat. 
##  Los que el beat reutiliza son todos los sprites de itsuki, el fondo de la
##  azotea y algunos BGM existentes.
################################################################################

image bg_azotea = "images/bg/cap1_beats/azotea.webp"

image cg_itsuki_azotea_cuaderno = "images/cg/cap1_beats/itsuki_azotea_cuaderno.webp"

image cg_itsuki_azotea_manos = "images/cg/cap1_beats/itsuki_azotea_manos.webp"

define audio.sfx.mochila_suelo = "audio/sfx/mochila_suelo.mp3"

define audio.guardia   = "audio/bgm/guardia.ogg"

################################################################################
##  HUB DE ITSUKI 
##  Cuarto o tercer encuentro entre mc e Itsuki en la azotea en el dia. 
##  Itsuki sabe que este nuevo estilo de vida no solo ha afectado a mc sino
##  que tambien a ella mismo pero no lo quiere admitir.
################################################################################

label beat_Itsuki:

    ############################################################################
    ##  MOVIMIENTO 1 · Llegada
    ##  MC encuentra a Itsuki sola con su cuaderno de ciencias en la azotea
    ##  No está haciendo nada, solo esta mirando perdidamente
    ############################################################################

    stop music fadeout 1.0

    scene bg_azotea
    with fade

    narrador "Subí a la azotea a la hora del almuerzo, más por costumbre que por otra cosa."

    mc_pensamiento "Desde el primer día, es el único sitio del instituto donde nadie me pide nada."

    narrador "La puerta ya estaba abierta."

    scene cg_itsuki_azotea_cuaderno
    with fade

    play ambiente amb_viento fadein 2.0 volume 0.35

    mc_pensamiento "Ahí estaba. Con el cuaderno."

    mc_pensamiento "El mismo cuaderno de ciencias que siempre lleva encima."

    narrador "No lo estaba leyendo."

    narrador "Lo tenía abierto en una página y la vista en otro lado."

    if not itsuki_visitada_cap1:

        narrador "Desde la puerta alcancé a ver la página."

        narrador "Un solo ejercicio, con un círculo a lápiz alrededor, repasado tantas veces que había hundido el papel."

        mc_pensamiento "Lo reconocí."

        mc_pensamiento "Era el de la hoja de diagnóstico del primer día."

        mc_pensamiento "El que la tuvo tres minutos atascada mientras yo le decía que no pensaba ayudarla."

    mc_pensamiento "La primera vez que subí aquí, ella dijo que venía a tomar aire."

    mc_pensamiento "A alejarse de gente desagradable."

    mc_pensamiento "Esa gente desagradable era yo."

    mc_pensamiento "Y hoy trajo el cuaderno de todas formas, al mismo sitio del que dijo que venía a escapar."

    mc_pensamiento "Sin nada de comer al lado."

    mc_pensamiento "Ya van varias veces que la veo así, en apenas unos días."

    $ duck()
    play sound sfx.mochila_suelo volume 1.5

    narrador "Me senté a un par de metros, sin decir nada todavía."

    scene bg_azotea
    with fade

    show itsuki neutral at pj(0.5)
    with dissolve

    itsuki "No te oí llegar."

    mc "No hice ruido a propósito."

    itsuki "Da igual. Ya estás aquí."

    narrador "Lo dijo sin la hostilidad de siempre. Sonó más a un hecho que a una queja."

    ############################################################################
    ##  MOVIMIENTO 2 · El peso compartido
    ##  Itsuki sabe que este nuevo estilo de vida no solo afecta a mc si no
    ##  que tambien le afecta a ella mismo.
    ############################################################################

    mc "Pensé que este sitio era donde no estudiabas."

    show itsuki molesta at pj(0.5)
    with disolucion_lenta

    itsuki "Y lo era."

    narrador "Cerró el cuaderno, pero no lo guardó."

    narrador "Se quedó con la mano encima, como si todavía no hubiera decidido qué hacer con él."

    itsuki "Ya no me queda ningún sitio que no lo sea."

    narrador "Fue una frase corta. Más corta que las suyas de costumbre."

    mc_pensamiento "No se cortó a media idea. La terminó."

    mc_pensamiento "Simplemente no tenía más que decir, y eso es distinto."

    narrador "Extendí la mano hacia la mochila y saqué mi propio libro."

    show itsuki neutral at pj(0.5)
    with disolucion_lenta

    itsuki "¿Tú también?"

    mc "Yo desde antes de que fuera tu tutor."

    narrador "No dijo nada a eso. Pero tampoco volvió a abrir su cuaderno."

    mc "No hay mesa aquí arriba."

    itsuki "No hace falta mesa para tener un cuaderno abierto."

    mc "Pero no lo tienes abierto para leerlo."

    itsuki "…"

    narrador "No contestó."

    narrador "Cambió el cuaderno de posición sobre las rodillas, "
    
    narrador " como si reacomodarlo fuera, de algún modo, una respuesta."

    mc_pensamiento "Lo trajo por costumbre, no porque pensara usarlo."

    mc_pensamiento "Como quien ya no sabe estar en un sitio sin la excusa de tener algo que hacer ahí."

    scene cg_itsuki_azotea_manos
    with fade

    narrador "Tenía las manos apoyadas sobre la tapa, quietas. Sin una sola mancha de tinta."

    mc_pensamiento "No había escrito nada en toda la mañana."

    mc_pensamiento "Ella, que llena una hoja de tachones antes que nadie termine la primera línea."

    play music tregua fadein 1.5 fadeout 2.0

    narrador "El viento seguía sonando igual que siempre aquí arriba, pero por debajo empezó a sonar algo más..."

    narrador "Bajo, casi nada."

    itsuki "¿Vas a preguntarme por qué lo traje?"

    mc "No."

    itsuki "…¿Por qué no?"

    mc "Porque ya lo sé."

    narrador "No contestó. Pero no volvió a preguntar tampoco."

    scene bg_azotea 
    with fade

    if itsuki_visitada_cap1 and itsuki_rama_cap1 != "tibia":

        show itsuki molesta at pj(0.5)
        with disolucion_lenta

        itsuki "Ya me ayudaste con el ejercicio el otro día." 
        
        itsuki "No hace falta que sigas viniendo a comprobar cómo voy."

        mc "No vine a comprobar nada."

        narrador "No pareció creérselo del todo." 
        
        narrador "Pero no insistió."

    else:

        show itsuki molesta at pj(0.5)
        with disolucion_lenta

        itsuki "No voy a preguntarte a ti dónde has estado estos días."

        mc "No te lo iba a contar de todas formas."


    narrador "Los dos volvieron a mirar al frente, cada uno con su propio libro cerrado sobre las piernas."

    mc_pensamiento "Llevamos pocos días de esto y ya la convivencia se volvió jornada completa para las dos partes."

    mc_pensamiento "Ella tampoco tiene dónde bajar la guardia."
    
    mc_pensamiento "Yo tampoco."

    narrador "Nos quedamos ahí un rato largo, sin abrir ninguno de los dos libros."

    narrador "El viento se llevó una hoja suelta de mi cuaderno hasta la valla, "
    
    narrador " y ninguno de los dos se levantó a buscarla."

    mc_pensamiento "Antes de este trabajo me habría importado esa hoja."

    mc_pensamiento "Ahora me importa más no moverme."

    ############################################################################
    ##  MOVIMIENTO 3 · Menú comsetico
    ##  No otorga puntos como el hub de cada una de ellas, es mas como un
    ##  alivio cómico y que el jugador pueda interactuar un poco.
    ############################################################################

    # Menu del sabor

    menu:

        "¿Qué piensas decirle a Itsuki mientras el descanso se acaba?"

        "En que a este paso me va a tocar traer los libros hasta al baño.":

            mc_pensamiento "Al menos ahí nadie me interrumpe."

            itsuki "Qué imagen tan poco digna de un tutor."

            mc "No dije que fuera a hacerlo. Dije que a este paso."

            itsuki "Viendo ese nivel de planificación tuyo..."
            
            itsuki "No me extraña que no logres hacernos estudiar a todas."

        "En que ninguno de los dos va a admitir que está cansado.":

            mc_pensamiento "Y si lo hiciéramos, tampoco cambiaría nada."

            itsuki "Habla por ti." 

            itsuki "Yo si me estoy esforzando en resolver estos ejercicios"

            itsuki "A comparación tuya..."

            mc "Tienes el cuaderno cerrado hace diez minutos."

            show itsuki timida at pj(0.5)
            with disolucion_lenta

            itsuki "Estoy descansando la vista." 
            
            itsuki "Es distinto."

        "En nada. Solo quiero que termine esta hora.":

            mc_pensamiento "No todo necesita un análisis."

            itsuki "Al menos en eso estamos de acuerdo."

            mc "Al parecer es lo primero."

            itsuki "No te acostumbres."


    ############################################################################
    ##  MOVIMIENTO 4 · CIERRE
    ##  Final del beat, es corto pero es para establecer de que la relación de
    ##  Itsuki y mc avanze, no rápido pero a su manera
    ############################################################################

    stop music fadeout 2.0
    stop ambiente fadeout 2.0

    play audio sfx_timbre volume 1.5

    narrador "El timbre sonó antes de que ninguno de los dos volviera a abrir un libro."

    show itsuki neutral at pj(0.5)
    with disolucion_lenta

    itsuki "Se acabó el descanso."

    mc "Se acabó."

    hide itsuki 
    with disolucion_lenta

    narrador "Se levantó primero."

    narrador "Se sacudió la falda y bajó las escaleras sin esperarme, como cualquier otro día."

    mc_pensamiento "Pero hoy subió con el cuaderno."

    mc_pensamiento "Y no lo abrió ni una vez."

    mc_pensamiento "Quedan casi tres semanas."

    mc_pensamiento "Ella la va a pasar igual que hoy:" 
    
    mc_pensamiento "Sola, con un cuaderno que no necesita, en el único sitio que le quedaba para no estarlo del todo."

    if not itsuki_visitada_cap1:

        mc_pensamiento "Sigue en el mismo ejercicio." 
        
        mc_pensamiento "No lo ha resuelto y no se lo va a preguntar a nadie."

    mc_pensamiento "No sé si vine a ayudarla o solo a quitarle su tiempo."
 
    return 
    