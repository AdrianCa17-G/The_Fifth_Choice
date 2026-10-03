################################################################################
##  BGs Y CGs PROPIOS DEL BEAT DE NINO 
##  1 sprite, 2 ilustraciones, 1 fondo, 1 BGM y 1 SFX nuevos de momentos 
##  concretos de este beat. Los que el beat reutiliza son todos los sprites 
##  de Nino, el departamento y algun BGM existente.
################################################################################

image bg_cocina = "images/bg/beats_hermanas/cocina.webp"

image cg_nino_confrontacion_cocina = "images/cg/cap1_beats/nino_confrontacion_cocina.webp"

image cg_nino_grieta_cocina = "images/cg/cap1_beats/nino_grieta_cocina.webp"

################################################################################
##  HUB DE NINO 
##  Encuentro entre mc, Maruo y Nino en la cocina de la casa. El tema principal
##  es que Nino quiere si o si el despido de mc, pero no porque mc sea malo,
##  sino porque teme a que sus hermanas se encariñen de nuevo con él.
################################################################################

label beat_Nino:

    ############################################################################
    ##  MOVIMIENTO 1 · Llegada
    ##  Mc observa la discusión entre Maruo y Nino sobre el despido de mc,
    ##  pero Maruo aún no encuentra una razón lógica del todo para despedirlo.
    ############################################################################

    scene bg_edificio
    scene bg_departamento
    with fade
    
    stop music fadeout 1.0

    narrador "Llegué al departamento a la hora de siempre."

    narrador "La puerta estaba entreabierta. Nadie la había cerrado del todo."

    scene cg_manija_edificio
    with fade

    play sound sfx_manija volume 1.5

    narrador "Antes de terminar de abrirla, escuché dos voces desde el fondo."

    mc_pensamiento "Una era de Maruo." 
    
    mc_pensamiento "Grave, pareja, sin subir nunca de tono."

    mc_pensamiento "La otra era de Nino." 
    
    mc_pensamiento "Y esta sí sonaba alterada."

    narrador "Me quedé en el umbral un segundo de más."

    mc_pensamiento "Podría abrir la puerta completamente y saludarlos."

    mc_pensamiento "O podía escuchar primero y decidir después."

    narrador "Elegí lo segundo."

    scene cg_nino_confrontacion_cocina
    with fade

    nino "…y no me importa lo que hayas firmado con él. Debes despedirlo."

    maruo "No."

    maruo "¡Es un tutor, no una sentencia de por vida!"

    maruo "Es exactamente un contrato."

    maruo "Y no lo voy a romper porque a ti no te guste su cara."

    narrador "Me acerqué lo suficiente para ver sin que me vieran a mí."

    mc_pensamiento "No es por mi cara. Es por algo que no tiene nada que ver conmigo."

    nino "No se trata de su cara." 
    
    nino "Se trata de que va a durar lo mismo que los anteriores, y ellas van a volver a creer que esta vez sí va a ser diferente."

    maruo "Eso ya lo decidiré yo, cuando corresponda."

    nino "¡Tú nunca estás aquí para verlo!"

    narrador "Ahí sí subió la voz de verdad."

    narrador "La única vez que la escuché gritarle a su padre."

    ############################################################################
    ##  MOVIMIENTO 2 · Maruo
    ##  Dependiendo de las decisiones del jugador en los 2 hubs anteriores,
    ##  Maruo amenaza o aún confia en mc, aunque Nino no esté de acuerdo.
    ############################################################################

    if desaires_cap1 >= 2:

        scene bg_departamento
        with fade

        narrador "Fue entonces cuando Maruo levantó la vista y me encontró en la puerta."

        scene cg_maruo_reunion
        with fade

        play music contrato fadein 2.0

        maruo "Ya que estás aquí, ahorrémonos el drama."

        mc "Perdón, no venía con la intención de interrumpirlos."

        maruo "Ya nos interrumpiste con solo entrar."

        narrador "Dejó la taza sobre la mesa, despacio, sin apurarse."

        maruo "Llevas más de una semana. No veo ningún cambio."

        mc "He tenido inconvenientes con sus hijas, pero eso no me es excusa."

        mc "Porfavor, ¡Le suplico que me espere hasta el final de los examenes!"

        mc "Los exámenes son en tres semanas, aun tenemos tiempo."

        maruo "No te pedí un cronograma. Te pedí resultados."

        narrador "Nino miraba entre los dos, sin intervenir por primera vez en toda la conversación."

        maruo "Las condiciones te las dije el primer día. No las voy a repetir una tercera vez."

        maruo "Si una sola de mis hijas reprueba, se acabó. Ese día no hay discusión ni segunda oportunidad."

        narrador "Lo dijo exactamente con el mismo tono que usó para cerrar la puerta esa primera noche."

        mc_pensamiento "No subió la voz ni una vez. No hacía falta."

        play sound sfx_puerta_cierra volume 1.0

        narrador "Recogió la taza y salió de la cocina sin esperar respuesta, dándonos la espalda a los dos por igual."

        scene bg_departamento
        with fade

        mc_pensamiento "Esa era la última vez que lo iba a decir."

        mc_pensamiento "Y los dos lo sabíamos."

    else:

        narrador "Maruo no llegó a notar que yo estaba en la puerta, o decidió no darse por enterado."

        maruo "No he visto ningún motivo todavía para cambiar nada."

        nino "¡Ese es el problema! ¡Que nunca ves ningún motivo hasta que ya es tarde!"

        maruo "Cuando lo sea, actuaré." 
        
        maruo "Hasta entonces, esta conversación está cerrada."

        narrador "Se sirvió el resto del café en el fregadero y salió de la cocina sin mirar a ninguno de los dos."

        play sound sfx_puerta_cierra volume 1.0

        scene bg_cocina
        with fade

        mc_pensamiento "No dijo mi nombre en toda la conversación."

        mc_pensamiento "Como si yo no fuera parte del problema que estaban discutiendo."

    narrador "Nino se quedó mirando el pasillo por donde se había ido su padre, todavía con los brazos cruzados."

    scene bg_cocina
    with fade

    show nino neutral at pj(0.5)
    with dissolve

    mc_pensamiento "Tengo que romper el hielo."

    mc "Hola..." 
    
    mc "No me mires así, solo iba de paso." 
    
    mc "No tengo intenciones de molestarte hoy, así que puedes ahorrarte tus quejas."

    nino "No es un buen momento."

    mc "Ya lo noté."

    ############################################################################
    ##  MOVIMIENTO 3 · La grieta
    ##  Muestra lo que realmente siente Nino por sus hermanas y por que 
    ##  no le agrada en absoluto a mc, no es el sino ella y su miedo.
    ############################################################################

    narrador "Entré del todo a la cocina. Ella no se movió de donde estaba."

    #[SFX sfx_taza_mesa NUEVO volume 2.0]

    narrador "Dejó su propia taza sobre la mesa con más fuerza de la necesaria." 
    
    narrador "El golpe sonó más alto que cualquier cosa que hubiera dicho."

    nino "Vas a preguntarme qué fue toda esta discusión."

    mc "No hace falta que me lo expliques." 
    
    mc "Escuché la mitad desde la puerta."

    nino "Entonces ya sabes lo que pienso de ti."

    mc "Sé lo que le dijiste a tu padre." 
    
    mc "Mas no de lo que piensas de mi, no es lo mismo."

    show nino molesta at pj(0.5)
    with disolucion_lenta

    nino "Da igual."

    nino "El resultado es el mismo: quiero que te vayas."

    mc "Tu padre acaba de decir que no."

    nino "Mi padre no tiene que vivir con esto todos los días. Yo sí."

    scene cg_nino_grieta_cocina
    with fade

    narrador "Se sentó en uno de los bancos de la cocina, de golpe, como si las piernas hubieran dejado de sostenerla el tiempo justo."

    #[MUS NUEVO — guardia fadein 2.5 volume 0.3]

    nino "No es porque seas malo en esto. Ni siquiera es porque me caigas mal, aunque me caes mal."

    nino "Es que ya vi esto pasar varias veces, y siempre fue igual."

    nino "Ichika finge que no le importa hasta que le importa." 
    
    nino "Yotsuba se esfuerza el doble para compensar algo que no puede compensar." 
    
    nino "Miku se encierra en su propia burbuja todavía más, y ya estaba bastante encerrada."

    nino "E Itsuki… Itsuki se lo toma como si fuera personal, porque para ella todo lo es."

    narrador "Hablaba rápido, sin las pausas que suele dejar entre frase y frase."

    nino "Y cuando se van, a mí me toca juntar los pedazos de las cuatro, porque soy la única que no se ilusionó nunca."

    nino "Alguien tiene que quedarse con la cabeza fría." 
    
    nino "Siempre soy yo."

    nino "Y estoy cansada de ser la única que ve venir el golpe antes de que llegue."

    narrador "Se detuvo de golpe, con la taza a medio camino de la boca."

    scene bg_cocina
    with fade

    show nino neutral at pj(0.5)
    with dissolve

    nino "…"

    show nino pillada at pj(0.5)
    with disolucion_lenta

    nino "No dije nada de esto."

    mc "Lo dijiste todo."

    narrador "No contestó." 
    
    narrador "Bajó la taza sin haber bebido nada."

    mc_pensamiento "No está exagerando." 
    
    mc_pensamiento "No conmigo, al menos."

    mc_pensamiento "Está describiendo un patrón que ya vio cumplirse varias veces seguidas, "
    
    mc_pensamiento " y la única variable que cambia cada vez es el nombre de quien se va."

    ############################################################################
    ##  MOVIMIENTO 4 · LA DECISIÓN
    ##  No otorga puntos como el hub de cada una de ellas, aunque si tiene un
    ##  efecto en la relación con Nino.
    ############################################################################

    narrador "Se puso de pie y se acomodó el uniforme, como quien intenta recomponer algo que ya se salió de su sitio."

    show nino neutral at pj(0.5)
    with disolucion_lenta

    nino "¿Y bien? ¿Vas a decir que esta vez es distinto?"

    mc_pensamiento "Si digo que sí, soy el siguiente tutor prometiendo lo mismo que los anteriores."

    mc_pensamiento "Si no digo nada, confirmo que tiene razón en no confiar."

    mc_pensamiento "No hay una respuesta que la deje tranquila." 
    
    mc_pensamiento "Solo hay una que no la deje peor."

    ## Menú del sabor

    menu:

        "¿Cómo respondes?"

        "¿Y quién junta tus pedazos?":   

            jump nino_beat_m4a

        "No decir nada. Recoger la taza que dejó y llevarla al fregadero.":

            jump nino_beat_m4b
                                                                            
        "Entonces deja de juntar los pedazos de las demás y ocúpate de los tuyos.": 

            jump nino_beat_m4c  

    ############################################################################
    ## Movimiento 4A · Rama cálida 
    ############################################################################

    label nino_beat_m4a:

        $ nino_rama_beat = "calida"

        #play music guardia fadein 2.0 volume 0.3    # descomentar cuando exista `guardia`

        mc "¿Y quién junta los tuyos?"

        nino "…¿Qué?"

        mc "Dijiste que te toca juntar los pedazos de las cuatro."

        mc "Pregunto quién junta los tuyos."

        nino "Nadie. No hace falta."

        mc "Hoy fuiste a pedirle a tu padre que me echara." 
        
        mc "Sola, sin avisarle a nadie."

        mc "Eso no lo hace alguien con la cabeza fría."

        narrador "Abrió la boca para contestar y no le salió nada."

        show nino nerviosa at pj(0.5)
        with disolucion_lenta

        nino "Lo hice porque—"

        narrador "Se detuvo sola. No la presioné para que terminara."

        nino "No es lo que piensas."

        mc "No pienso nada. Solo pregunté."

        narrador "Se quedó mirando la taza un rato largo."

        show nino pillada at pj(0.5)
        with disolucion_lenta

        nino "Hay que hacer la cena. Son cinco."

        mc "¿Y?"

        show nino molesta at pj(0.5)
        with disolucion_lenta

        nino "Y no pienso cocinar con alguien mirándome. Corta las cebollas. Finas."

        mc "Está bien."

        nino "No es una invitación."

        mc "Es una orden."

        show nino neutral at pj(0.5)
        with disolucion_lenta

        nino "Exacto."

        narrador "Me señaló la tabla con la barbilla, sin mirarme."

        narrador "Cortamos en silencio. En toda la tarde no volvió a hablar de despedirme."

        mc_pensamiento "No me dejó entrar. Me dio una tarea."

        mc_pensamiento "Con ella, eso es casi lo mismo."

        jump nino_beat_m5   


    ############################################################################
    ## Movimiento 4B · Rama tibia
    ############################################################################

    label nino_beat_m4b:

        $ nino_rama_beat = "tibia"

        narrador "No dije nada." 
        
        narrador "Rodeé la mesa y recogí la taza que había dejado a medio terminar."

        show nino molesta at pj(0.5)
        with disolucion_lenta

        nino "¿Qué haces?"

        mc "Llevarla al fregadero."

        mc "No hacía falta que la reventaras contra la mesa."

        nino "No la reventé."

        mc "Sonó como si lo hubieras hecho."

        narrador "No contestó a eso."

        narrador "Se quedó apoyada contra la mesa."
        
        narrador "Con los brazos cruzados otra vez, pero menos tensos que antes."

        show nino neutral at pj(0.5)
        with disolucion_lenta

        nino "No esperaba que te quedaras después de escuchar eso."

        mc "¿Preferías que me fuera?"

        nino "No dije eso tampoco."

        narrador "Terminé de lavar la taza en silencio."

        narrador "Ella no se movió de su sitio, pero tampoco volvió a sacar el tema con su padre."

        mc_pensamiento "No dijo nada más de lo que pensaba."

        mc_pensamiento "Y yo tampoco le pregunté." 

        jump nino_beat_m5      


    ############################################################################
    ## Movimiento 4C · Rama fría 
    ############################################################################

    label nino_beat_m4c:

        $ nino_rama_beat = "fria"

        mc "Entonces deja de juntar los pedazos de las demás y ocúpate de los tuyos."

        narrador "Lo dije pensando que la iba a hacer reaccionar."

        narrador "Reaccionó, pero no como esperaba."

        show nino molesta at pj(0.5)
        with disolucion_lenta

        nino "…"

        nino "Genial."

        nino "Ni un día entero de conocerme y ya sabes exactamente qué decirme para que me calle."

        mc "No dije que te callaras."

        show nino neutral at pj(0.5)
        with disolucion_lenta

        nino "Dijiste que me ocupara de lo mío. Es la forma elegante de lo mismo."

        narrador "Recogió su taza ella misma, sin dejar que me acercara."

        nino "Ahora entiendo por qué mi padre firmó contigo. Hablan el mismo idioma."

        mc_pensamiento "No sé si eso es un insulto o la descripción más precisa que me ha dado."

        narrador "Se fue a su habitación sin volver a mirarme, con la taza todavía en la mano."

        mc_pensamiento "Le dije justo lo que un padre le diría."

        mc_pensamiento "Y ella me contestó justo lo que le contesta a un padre."

        jump nino_beat_m5    

    ############################################################################
    ##  MOVIMIENTO 5 · CIERRE
    ##  Final del beat, es corto pero es para establecer de que la relación de
    ##  Nino y mc avanze, no rápido pero a su manera
    ############################################################################

    label nino_beat_m5:

        stop music fadeout 2.0

        hide nino
        with disolucion_lenta

        narrador "Me quedé un rato más en la cocina, solo, con el ruido del edificio de fondo."

        mc_pensamiento "Vino a pedir que me fuera."
        
        mc_pensamiento "Su padre dijo que no."

        mc_pensamiento "Y aun así, el que se quedó dando explicaciones fui yo."

        if desaires_cap1 >= 2:

            mc_pensamiento "Maruo no va a repetir esa advertencia una tercera vez."

            mc_pensamiento "La próxima vez que hable de esto, no va a ser una advertencia."

            mc_pensamiento "Será un despido asegurado."

        if nino_rama_beat == "calida":

            mc_pensamiento "Hoy fue a pelear sola y no le dijo a nadie."

            mc_pensamiento "Me puse a cortar cebollas y no volvió a hablar de despedirme."

            mc_pensamiento "Mi pregunta se quedó sin respuesta, y ella sabe que sigue ahí."

        elif nino_rama_beat == "tibia":

            mc_pensamiento "La taza quedó en el escurridor y ella no volvió a mirarla."

            mc_pensamiento "No me echó. Tampoco me dejó quedarme de verdad."

            mc_pensamiento "Hoy el silencio fue el único acuerdo que cabía entre los dos."

        else:

            mc_pensamiento "Maruo cerró la conversación sin alzar la voz."

            mc_pensamiento "Yo cerré la mía igual, una hora después y en la misma cocina."

            mc_pensamiento "Ella tuvo que ver la misma puerta cerrarse dos veces en una tarde."                        
 
    return 
    