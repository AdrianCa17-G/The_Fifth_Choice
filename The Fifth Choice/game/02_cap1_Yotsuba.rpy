################################################################################
##  HUB DE YOTSUBA
##  La primera visita a Yotsuba, que se encuentra en la pista de atletismo.
##  Se puede visitar en cualquier momento.
################################################################################

label hub_Yotsuba:

    ############################################################################
    ##  MOVIMIENTO 1 · Llegada
    ##  Primer encuentro entre mc y Yotsuba. Se establece la dinámica de la relación.
    ############################################################################

    #`[BG NUEVO — bg_pista_atletismo]`
    
    stop music fadeout 1.0

    narrador "La pista de atletismo estaba al fondo del edificio de deportes."

    narrador "Tardé diez minutos en encontrarla."

    narrador "El club había cerrado. Las gradas estaban vacías y las luces de competición apagadas."

    narrador "Solo estaba encendido el sistema de emergencia, que daba una luz naranja pareja y sin sombras."

    #`[CG NUEVO — cg_yotsuba_pista: Yotsuba de espaldas en la recta final de la
    #pista, en plena carrera. Pista de tartán roja, líneas blancas. Luz naranja de
    #emergencia. Gradas vacías al fondo. Un solo personaje, sin nadie más. La
    #cámara está en las gradas, a media altura, con el fondo de la pista abierto
    #delante de ella. Sostiene los primeros tres bloques de narración.]`

    mc_pensamiento "El club se había ido hace por lo menos media hora."

    mc_pensamiento "Estaban marchandose a casa cuando salí de clase."

    mc_pensamiento "Ella sigue ahí."

    mc_pensamiento "Sola."

    narrador "Seguía dando vueltas, sin si quiera notar mi presencia."

    narrador "Fue la tercera vuelta cuando escuché lo que decía."

    yotsuba "¡Veinte! ¡Vamos, Yotsuba! ¡Tú puedes!" 
    
    yotsuba "¡La vuelta veintiuno es tuya! ¡Es tu vuelta favorita!"

    mc_pensamiento "Estaba contando en voz alta."

    mc_pensamiento "Y animándose a sí misma."

    narrador "Me quedé observandola y memorizando el número de vueltas que llevaba."

    #`[SFX sfx_pisadas_pista — pasos rítmicos de carrera, en loop suave]`

    yotsuba "¡Veintidós! ¡Esto es fácil! ¡Podría hacer cien! ¡Bueno, quizás no cien, pero sí veinticinco!" 
    
    yotsuba "¡Veinticinco es un número perfecto!"

    mc_pensamiento "No es un número perfecto."

    narrador "Lo estaba anotando. En la muñeca. Con rotulador."

    mc_pensamiento "Lleva las vueltas escritas en el brazo."

    narrador "Tomó la curva y me vio."

    #`[SFX sfx_pisadas_pista — STOP abrupto]`

    ############################################################################
    ##  MOVIMIENTO 2 · La grieta
    ##  Yotsuba se siente insuficiente y se compara con sus hermanas. 
    ############################################################################

    show yotsuba_sorprendida at pj(0.5)

    narrador "Se paró en seco a mitad de la pista, "
    
    narrador " murmurando algo entre dientes mientras contenía la respiración."

    yotsuba "…"

    mc "Llevas veintitrés vueltas Yotsuba."

    mc "Te va a dar algo si sigues hablando contigo misma."

    yotsuba "¡No estaba hablando sola! ¡Estaba haciendo técnica de concentración mental!" 
    
    yotsuba "¡Es un método avalado por atletas de élite!"

    mc "Ajá."

    yotsuba "¡Lo dijeron en un documental de la tele!"

    mc "¿Cuánto tiempo llevas aquí?"

    narrador "Pausa."

    show yotsuba_neutral at pj(0.5)

    yotsuba "…¿Cuánto llevas tú?"

    mc "Tus últimas ocho vueltas."

    yotsuba "…"

    yotsuba "Eso es mucho tiempo."

    mc "Sí. Lo es."
    
    mc "Y parece que no es la primera vez que te quedas después de que el club se va."

    #`[CG NUEVO — cg_yotsuba_rotulador: Yotsuba apoyada en la valla metálica
    #de la pista, plano medio-corto. Brazo izquierdo levantado, mirando el
    #rotulador en la muñeca con expresión entre avergonzada y descolocada.
    #Pelo naranja suelto por el esfuerzo, mejillas ligeramente sonrojadas por
    #la carrera. Chaleco amarillo, camisa manga corta, falda verde, medias
    #oscuras hasta la rodilla, loafers marrones. Fondo: pista de tartán roja,
    #gradas vacías, luz naranja de emergencia. Sin más personajes en el encuadre.
    #Cámara a altura de ojo. Sostiene desde «Se pasó el dorso de la mano»
    #hasta «Miró la pista, el rotulador, las gradas vacías».]`

    narrador "Se pasó el dorso de la mano por la frente y miró el rotulador de la muñeca con
    una mezcla de vergüenza y desconcierto"

    #`[SFX sfx_silencio_exterior — viento suave, pajaros lejanos]`

    yotsuba "¿Por qué estás aquí?"

    mc "Porque es donde estás tú."

    yotsuba "¿Y eso por qué importa?"

    mc "Porque soy tu tutor... y me preocupo por ti."

    narrador "Lo procesó un segundo."

    narrador "Luego asintió con la solemnidad de quien acaba de recordar algo obvio."

    yotsuba "¡Ah, claro! ¡Eso tiene sentido! ¡Pues bienvenido a la pista!"

    mc "Gracias. ¿Por qué sigues aquí si el club ya se fue?"

    narrador "La pregunta la pilló sin la exclamación preparada."

    yotsuba "…Quería terminar las series."

    mc "¿Cuántas series?"

    yotsuba "Las que me faltaban."

    mc "¿Cuántas te faltaban?"

    yotsuba "…Treinta."

    narrador "Treinta vueltas después de que el club cerró."

    mc_pensamiento "Eso es entre nueve y doce kilómetros, dependiendo del tamaño de la pista."

    mc_pensamiento "Sola."
    
    mc_pensamiento "Sin nadie que la anime."
    
    mc_pensamiento "Sin nadie que la cuide." 
     
    mc_pensamiento "Sin nadie que le diga que ya es suficiente."

    mc_pensamiento "Con el rotulador en la muñeca porque si no pierde la cuenta."

    mc "¿Entrenas así todos los días?"

    yotsuba "¡Solo cuando quiero mejorar!... Que si... ¡Es todos los días!"

    mc "¿Y el club no se queda?"

    narrador "Algo cambió en la forma en que se apoyó en la valla."

    yotsuba "El club tiene sus propios objetivos. Yo tengo los míos."

    mc "¿Cuáles son los tuyos?"

    narrador "No contestó de inmediato."

    narrador "Miró la pista, el rotulador, las gradas vacías."

    show yotsuba_neutral at pj(0.5)

    yotsuba "Mis hermanas son mejores que yo en casi todo."

    narrador "Lo dijo sin drama. Como quien dice que va a llover."

    yotsuba "Ichika actúa. Nino cocina. Miku sabe de historia. Itsuki estudia."

    yotsuba "Y yo…"

    narrador "Señaló la pista con la mano abierta."

    yotsuba "Yo corro y animo. Así que lo hago lo mejor que puedo."

    narrador "Sonrió. Era una sonrisa buena, sin fisuras visibles."

    mc_pensamiento "Si no supiera lo que acaba de decir, pensaría que está contenta."

    mc_pensamiento "Pero lo que acaba de decir es que su única razón para estar aquí es no quedarse atrás."

    mc_pensamiento  "Como si destrozarse el cuerpo en esa pista fuera un precio justo por sentirse útil."

    ############################################################################
    ##  MOVIMIENTO 3 ·  La decisión
    ##  El jugador decide cómo responder a Yotsuba.
    ##  La respuesta afecta la relación. 
    ############################################################################

    #`[MUS NUEVO — descubrimiento, volumen 0 listo para subir]`

    narrador "Se limpió el rotulador de la muñeca con el reverso de la camiseta y volvió a mirarme con esa sonrisa intacta."

    yotsuba "¡Bueno!" 

    yotsuba "¡Si has venido a verme entrenar, puedes cronometrarme en la siguiente vuelta!" 
    
    yotsuba "¡Soy más rápida cuando alguien mira!"

    mc_pensamiento "Cambió de tema."

    mc_pensamiento "Lo hizo tan rápido y con tanta energía que casi no lo noté."

    narrador "Pensé en lo que había visto estas últimas ocho vueltas."

    narrador "En lo que había dicho, y en lo que no."

    ############################################################################
    ##  MOVIMIENTO 4A · Rama cálida
    ##  MOVIMIENTO 4B · Rama tibia
    ##  MOVIMIENTO 4C · Rama fría
    ############################################################################

    ## Menú de sabor.

    menu:

        narrador "¿Cómo le ayudarias a sentirse mejor?"

        "Tú vales tanto como cualquiera de tus hermanas":

            #`[$ sumar_punto("yotsuba", 1)]`
            #`[MUS descubrimiento — fade in volumen 3.5]`

            mc "Antes de eso."

            yotsuba "¿Antes de qué?"

            mc "Dijiste que tus hermanas son mejores que tú en casi todo."

            yotsuba "¡Sí! ¡Pero eso no es malo! ¡Cada una tiene lo suyo!" 
            
            yotsuba "¡Y yo tengo lo mío!"

            mc "Lo sé. Pero te saltaste algo."

            narrador "Su sonrisa no desapareció,"
            
            narrador " pero tardó un poco más en reaccionar."

            yotsuba "…¿Qué me salté?"

            mc "Esta mañana, en el desayuno. Supiste que Nino no había dormido bien antes
            de que ella dijera nada."

            yotsuba "Estaba un poco más callada que de costumbre."

            mc "Y ayer le dijiste a Miku que el libro que buscaba estaba en la
            segunda planta antes de que Miku si quiera preguntara."

            yotsuba "Es que siempre lo deja ahí después de leerlo."

            mc "Y la semana pasada, cuando Ichika llegó tarde al departamento,
            fuiste la primera en saber si estaba cansada o si estaba preocupada." 

            mc "Y eran cosas distintas."

            narrador "Hubo un breve silencio."

            narrador "No el silencio de quien no tiene respuesta: 
            el de quien está revisando si los datos son correctos."

            yotsuba "…¿Me estabas observando?"

            mc "Soy tu tutor. Observar es parte del trabajo."

            yotsuba "Eso que describes no es nada especial."

            yotsuba "Cualquiera lo haría."

            mc "Ninguna de tus hermanas lo hace. Yo tampoco. Y lo intento."

            narrador "Eso no lo tenía preparado."

            show yotsuba_sorprendida at pj(0.5)

            yotsuba "…Pero eso no entra en ningún examen."

            mc "En Literatura entra algo que se llama comprensión lectora."

            mc "Solo que tú no lo haces con libros. Lo haces con personas."

            mc "Sabes leer lo que dicen y lo que se callan, aunque no lo expliquen."

            mc "Tú lo haces de forma natural con cinco personas a la vez."

            narrador "No dijo nada. Miraba la pista, pero no la pista de verdad."

            mc "No te digo que sea suficiente para el examen. "

            mc "Te digo que tu punto de partida no es cero. Nunca lo fue."

            yotsuba "…"

            narrador "Pasó un momento largo."

            show yotsuba_neutral at pj(0.5)

            yotsuba "No sé si eso es verdad o si eres muy bueno animando a la gente."

            mc "Soy pésimo animando a la gente. Pregúntale a cualquiera."

            narrador "Lo pensó."

            show yotsuba_sonrisa at pj(0.5)

            yotsuba "…Eso también es verdad."

            mc "Dame el cronómetro."

            narrador "Me lo pasó sin decir nada más."

            narrador "Cuando arrancó la vuelta veinticuatro, ya no le hizo falta gritar para darse ánimos."

            narrador "Algo en ella luce distinto. No era que estuviera más rápida. Era que estaba más segura."


        "Claro, dame el cronómetro.":

            #(sin puntos, sin desaire)

            narrador "Cogí el cronómetro que me tendió."

            yotsuba "¡Genial! ¡Preparado!"

            mc "Preparado."

            #[SFX sfx_pisadas_pista — arranca carrera]

            narrador "Salió disparada. Era rápida de verdad."

            narrador "No el tipo de rapidez de alguien que solo entrena por pasatiempo; corría en serio."

            narrador "Cuando terminó la vuelta, frenó delante de mí con los brazos abiertos, esperando el tiempo."

            mc "Un minuto con diecisiete."

            yotsuba "¡Sabía que hoy estaba bien! ¡Lo noté en el calentamiento!"

            mc "¿Lo notas en el calentamiento?"

            yotsuba "¡Siempre! Las piernas me avisan. ¡Es como un idioma secreto entre mis piernas y yo!"

            narrador "Sonreí sin querer."

            mc "¿Y tu cabeza?"

            yotsuba "¡Mi cabeza va a donde van las piernas! ¡Equipo completo!"

            narrador "Se rió de su propio chiste. Era una risa fácil, sin trampa."

            mc "Esquivó el tema."

            mc "O tal vez prefirió quedarse con el cronómetro porque era más sencillo."

            mc "No lo sé. Y ella tampoco me lo va a decir hoy."

            mc "Otra vuelta."

            yotsuba "¡Otra vuelta! ¡Esta va a ser mejor!"

            narrador "Y lo fue."

            narrador "No conseguí ayudarla a sentirse mejor, pero tampoco la hice sentir peor."


        "Si vas a seguir corriendo, deja de perder el tiempo.":

            #`[$ desaires_cap1 += 1]`

            mc "Entonces concéntrate en correr. Si es lo tuyo, hazlo bien."

            narrador "Asintió."

            narrador "Rápido, una sola vez, como quien recibe una instrucción."

            show yotsuba_sonrisa at pj(0.5)

            yotsuba "¡Tienes razón! ¡Eso estaba haciendo! ¡Qué bueno que lo entiendas!"

            narrador "Volvió a la pista sin esperar respuesta. La sonrisa era idéntica
            a la de antes."

            mc_pensamiento "Le dije exactamente lo que quería escuchar."

            mc_pensamiento "O lo que lleva siempre diciendose a si misma."

            narrador "Dio la vuelta veinticuatro en un silencio absoluto."

            narrador "Sin contar. Sin animarse."

            narrador "Al principio no le di importancia, pero para la vuelta veinticinco lo entendí."

            mc_pensamiento "Antes contaba en voz alta porque así no perdía el ritmo."

            mc_pensamiento "Ahora ya no le hacía falta."

            narrador "Seguí ahí parado hasta que terminó la serie."

            narrador "No sé muy bien por qué."

            mc_pensamiento "Acabo de decirle a alguien que se concentre en la única cosa que cree que la hace valer."

            mc_pensamiento "Y ahora mismo no sé si le di una instrucción o una sentencia."


    ############################################################################
    ## MOVIMIENTO 5 · Cierre
    ## Común a las tres ramas, con un cierre cálido, tibio o frío según la elección.
    ############################################################################

    #`[BG bg_pista_atletismo — luz más baja, atardecer avanzado]`
    #`[MUS stop fadeout 1.5]`

    narrador "Salí de la pista cuando ella terminó la vuelta treinta."

    mc_pensamiento "Una de cinco. Y esta acaba de llegar corriendo."

    mc_pensamiento "Solo quedan tres semanas."

    #*Cierre A (cálida):*

    mc_pensamiento "Me preguntó si era verdad o si solo era bueno animando a la gente."

    mc_pensamiento "La respuesta honesta es que no lo sé todavía."

    mc_pensamiento "Pero su punto de partida no era cero."

    mc_pensamiento "De eso sí estoy seguro."

    #*Cierre B (tibia):*

    mc_pensamiento "Un minuto con diecisiete. Un minuto con catorce en la última."

    mc_pensamiento "No sé si mejoró por el cronómetro o a pesar de él."

    mc_pensamiento "Tampoco sé qué iba a decir antes de que se lo diera."

    mc_pensamiento "Pero le puso tanta energía al asunto que ya no hubo forma de volver atrás."

    #*Cierre C (fría):*

    mc_pensamiento "Dejó de contar en voz alta después de lo que dije."

    mc_pensamiento "Puede que no importe."

    mc_pensamiento "Tal vez ese método suyo no servía para nada y mi consejo fue el correcto."

    mc_pensamiento "O tal vez le acabo de confirmar la única cosa de la que nadie 
    debería haberla convencido nunca."

    #`→ Vuelve al hub.`
        