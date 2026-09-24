################################################################################
##  BGs Y CGs PROPIOS DEL HUB DE ITSUKI 
##  Ilustraciones y fondos de momentos concretos de este hub. Los  que
##  el hub reutiliza son todos los sprites de itsuki y el de timida que nunca
##  se usó en la apertura
################################################################################

image bg_aula_tarde = "images/bg/hubs_hermanas/aula_tarde.webp"

image cg_itsuki_atascada = "images/cg/hubs_hermanas/itsuki_atascada.webp"

image cg_itsuki_contraida = "images/cg/hubs_hermanas/itsuki_contraida.webp"

image cg_itsuki_reto = "images/cg/hubs_hermanas/itsuki_reto.webp"


################################################################################
##  HUB DE ITSUKI 
##  Cuarto encuentro entre mc e Itsuki en el aula de tarde. 
##  Itsuki no sabe resolver un ejercicio y el jugador puede ayudarla, 
##  pero la forma de hacerlo afectará la relación.
################################################################################

label hub_Itsuki:

    $ sumar_punto("itsuki", 2)

    # Si el jugador eligió el aula en la tarde en el hub 1, se marca la primera
    # conexión. Ajustar el string si el hub usa otra clave para este destino.
    #if hub_choice == "aula_tarde":
    #    $ primera_conexion = True

    ############################################################################
    ##  MOVIMIENTO 1 · Llegada
    ##  Primer encuentro entre mc e Itsuki en el aula de tarde
    ############################################################################

    scene bg_aula_tarde
    with fade
    
    stop music fadeout 1.0

    narrador "Volví al aula a buscar el cuaderno que había dejado en el pupitre."

    narrador "Ya no quedaba nadie a esa hora. Ni siquiera el personal de limpieza."

    narrador "La luz entraba baja, de lado."

    narrador "Se cortaba en franjas sobre los pupitres vacíos."

    scene cg_itsuki_atascada
    with fade

    narrador "Menos un pupitre."

    mc_pensamiento "Itsuki."

    mc_pensamiento "No estaba escribiendo."

    mc_pensamiento "Tenía el lápiz levantado, quieto, como si llevara así un rato."

    narrador "No me había oído entrar."

    narrador "O me había oído y decidió que no era asunto suyo quién entraba."

    mc_pensamiento "A su lado había tres respuestas tachadas."

    mc_pensamiento "Una sola raya horizontal cada vez, prolija. No un garabato de rabia."

    mc_pensamiento "Y la misma cifra al final de los tres."

    narrador "Me acerqué a buscar la mochila."

    narrador "Fue entonces cuando levantó la vista."

    scene bg_aula_tarde
    with fade

    show itsuki neutral at pj(0.5)
    with dissolve

    itsuki "¿Olvidaste algo?"

    mc "El cuaderno."

    itsuki "Está en tu pupitre. Donde lo dejaste."

    mc "Gracias."

    narrador "No aparté la vista tan rápido como debería."

    ############################################################################
    ##  MOVIMIENTO 2 · La grieta
    ##  Itsuki se repliega sobre sí misma y deja ver que no sabe
    ##  resolver el ejercicio.
    ############################################################################

    play sound sfx_hoja volume 1.0

    narrador "Pasó a una hoja nueva del cuaderno, tapando la anterior con la mano."

    narrador "Y siguió sin escribir nada."

    mc "¿Ciencias?"

    itsuki "No te incumbe."

    mc "Es tu asignatura."

    mc "Sí me incumbe."

    show itsuki molesta at pj(0.5)
    with dissolve

    itsuki "Me incumbe a mí. Tú te vas a las cuatro."

    mc "Son las cuatro y media."

    narrador "No contestó a eso."

    narrador "Volvió a mirar el cuaderno como si la frase no se hubiera dicho."

    mc_pensamiento "Tres tachones. Misma cifra las tres veces."

    mc_pensamiento "Eso no es no saber."

    mc_pensamiento "Eso es equivocarse siempre en el mismo sitio sin encontrarlo."

    mc "¿Cuánto llevas con ese ejercicio?"

    itsuki "El tiempo que hace falta."

    mc "¿Y cuánto es?"

    show itsuki neutral at pj(0.5)
    with dissolve

    itsuki "El que haga falta, he dicho."

    narrador "Lo repitió exactamente igual, palabra por palabra."

    narrador "Y eso fue lo que la delató."

    mc_pensamiento "Cuando Itsuki tiene la respuesta, no repite la pregunta con la misma frase."

    mc_pensamiento "La cambia. La corrige. La mejora."

    mc_pensamiento "Esta vez solo la devolvió intacta."

    mc_pensamiento "Está ganando, o perdiendo tiempo."

    mc "Las demás no estudian nada y les va igual de mal que a ti."

    narrador "Eso sí le tocó algo."

    show itsuki molesta at pj(0.5)
    with dissolve

    itsuki "No es lo mismo."

    mc "¿Por qué no?"

    itsuki "Porque ellas pueden decir que no lo intentaron."

    itsuki "Yo no tengo esa excusa."

    narrador "Lo dijo rápido. Más rápido que el resto de la conversación."

    narrador "Como quien suelta algo antes de poder impedírselo."

    show itsuki timida at pj(0.5)
    with dissolve

    itsuki "…"

    itsuki "Olvida lo que dije."

    mc_pensamiento "Ahí estaba."

    mc_pensamiento "No es que le vaya mal."

    mc_pensamiento "Es que le va mal *estudiando*."

    mc_pensamiento "Y esa es la única excusa que no tiene guardada."

    narrador "Bajó la vista al cuaderno."

    narrador "La postura no había cambiado, pero algo en los hombros sí."

    scene cg_itsuki_contraida
    with fade

    narrador "Se dejó caer sobre el pupitre. No dormida, hundida."

    narrador "La cabeza entre los brazos, tapando el cuaderno sin proponérselo."

    narrador "Los ojos seguían abiertos. Fijos en un punto del papel que ya no leía."

    mc_pensamiento "Preguntarle a sus hermanas sería admitir algo."

    mc_pensamiento "Que ella, la que sí estudia, no entiende esto."

    mc_pensamiento "Preguntarme a mí sería peor."

    mc_pensamiento "Sería darme la razón sobre por qué estoy como su tutor."

    mc_pensamiento "Así que no le pregunta a nadie."

    mc_pensamiento "Se queda ahí, hundida sobre la misma página, hasta que se va la luz."

    ############################################################################
    ##  MOVIMIENTO 3 · La decisión
    ##  El jugador decide si ayuda de manera involuntaria, si la ayuda anque
    ##  signifique romper su orgullo, o si la ayuda de manera fría y directa.
    ############################################################################

    #"`[MUS NUEVO — descubrimiento, volumen 0 listo para subir]`"

    scene cg_itsuki_reto
    with fade

    narrador "Dejé la mochila en el suelo."

    narrador "Me acerqué un paso. No dos."

    narrador "Lo suficiente para ver el cuaderno sin que hiciera falta que me lo mostrara."

    narrador "Tres líneas de planteamiento correctas."

    narrador "La conversión de unidades del segundo paso, mal."

    narrador "El mismo error, repetido igual las tres veces."

    narrador "Porque volvía a copiar el número equivocado del primer intento cada vez que empezaba de nuevo."

    mc_pensamiento "No es que no sepa resolverlo."

    narrador "Es que no está revisando desde el principio."

    narrador "Está corrigiendo el final y arrastrando el error del medio sin tocarlo."

    scene bg_aula_tarde
    with fade

    show itsuki neutral at pj(0.5)
    with dissolve

    itsuki "¿Vas a quedarte mirando o vas a buscar tu cuaderno?"

    mc "Las dos cosas, si me dejas."

    itsuki "No te dejo."

    narrador "Pero no se movió del pupitre. Ni cerró el cuaderno."

    mc_pensamiento "Tres formas de hacer esto."

    mc_pensamiento "Y solo una no la deja peor de lo que ya está."

    # Menu del sabor

    menu:

        "¿Cómo respondes?"

        "Se nota tu esfuerzo. Quizás el tropiezo esté un poco más atrás, en el segundo paso.":
            jump itsuki_m4a

        "¿Quieres que lo revisemos desde el principio?":
            jump itsuki_m4b

        "Estás perdiendo el tiempo. Déjame el cuaderno y lo resuelvo.":
            jump itsuki_m4c


############################################################################
##  MOVIMIENTO 4A · Rama cálida
############################################################################

label itsuki_m4a:    

    $ itsuki_rama_cap1 = "calida"
    $ sumar_punto("itsuki", 1)
    
    #[MUS descubrimiento — fade in volumen 3.5]`"

    narrador "Señalé la línea con el dedo. Sin tocar el papel."

    narrador "Sin acercarme más de lo que ya estaba."

    show itsuki molesta at pj(0.5)
    with dissolve

    itsuki "¿Qué tiene el segundo paso?"

    mc "Nada que yo vaya a decirte."

    mc "Solo te digo dónde mirar."

    narrador "Se quedó quieta un segundo, decidiendo si eso contaba como ayuda."

    narrador "Debió decidir que no del todo, porque volvió a mirar el cuaderno."

    show itsuki neutral at pj(0.5)
    with dissolve

    itsuki "…"

    narrador "Repasó la línea. Una vez. Dos veces."

    itsuki "La unidad no se cancela ahí."

    itsuki "Arrastré el valor sin convertir."

    mc "¿Eso lo sabías o te lo estoy diciendo yo?"

    show itsuki molesta at pj(0.5)
    with dissolve

    itsuki "Lo sabía. Se me pasó."

    mc "No dije que no."

    narrador "Tachó la línea entera, no solo el número."

    narrador "Volvió a empezar desde ahí con la letra un poco más apretada que\nel resto del cuaderno."

    mc_pensamiento "No me pidió que me fuera."

    mc_pensamiento "Tampoco me pidió que me quedara."

    mc_pensamiento "Pero el simple hecho de tolerar mi presencia ya demuestra todo lo que necesito."

    narrador "Me quedé de pie, sin sentarme, mientras terminaba el paso."
    
    show itsuki timida at pj(0.5)
    with dissolve

    itsuki "…El resultado me da distinto ahora."

    mc "¿Y?"

    itsuki "…Es el que tenía que dar."

    narrador "No lo dijo como un triunfo."

    narrador "Lo dijo como quien reporta un dato, todavía sin mirarme."

    show itsuki neutral at pj(0.5)
    with dissolve
    
    itsuki "Puedes buscar tu cuaderno ahora."

    mc "Ya lo sé. No me voy a ir todavía."

    narrador "Levantó la vista, un segundo, para comprobar si hablaba en serio."

    narrador "Y volvió al cuaderno sin decir nada más."

    narrador "Pero sin pedirme que me fuera tampoco."

    jump itsuki_m5

############################################################################
##  MOVIMIENTO 4B · Rama tibia
############################################################################
   
label itsuki_m4b:  

    $ itsuki_rama_cap1 = "tibia"
    ## sin puntos, sin desaire      

    show itsuki molesta at pj(0.5)
    with dissolve

    itsuki "No."

    mc "Ni siquiera sabes qué te iba a explicar."

    itsuki "No hace falta. La respuesta es no."

    narrador "Cerró el cuaderno un centímetro. No del todo."

    narrador "Lo suficiente para que entendiera que la oferta ya estaba rechazada."

    mc "Está bien."

    itsuki "Bien."

    narrador "Me quedé un momento más de lo necesario, esperando algo que no llegó."

    narrador "Fui a buscar mi cuaderno."

    mc_pensamiento "No dijo que no supiera."

    mc_pensamiento "Dijo que no quería que se lo explicara."

    mc_pensamiento "Con ella eso puede ser lo mismo, o lo contrario. Hoy no lo voy a averiguar."

    narrador "Cuando volví a pasar por su pupitre, seguía en el mismo ejercicio."

    narrador "La misma línea. Sin tacharla todavía."

    jump itsuki_m5

############################################################################
##  MOVIMIENTO 4C · Rama fría
############################################################################
   
label itsuki_m4c:   
        
    $ itsuki_rama_cap1 = "fria"
    $ desaires_cap1 += 1
    
    narrador "Estiré la mano hacia el cuaderno antes de que pudiera contestar."

    show itsuki sorpresa at pj(0.5)
    with dissolve

    itsuki "¿Qué haces?"

    mc "Ahorrarte tiempo."

    mc "El error está en el segundo paso, la conversión."

    narrador "Lo resolví ahí mismo, de pie, con su propio lápiz."

    narrador "Le devolví el cuaderno con el ejercicio terminado."

    show itsuki molesta at pj(0.5)
    with dissolve

    itsuki "…"

    mc "Listo. El resultado es ese."

    itsuki "Ya lo veo."

    narrador "Lo dijo sin agradecerlo y sin discutirlo."

    narrador "En ella, esa es la forma más fría de aceptar algo."

    mc_pensamiento "Se lo resolví bien. Rápido, correcto, sin margen de error."

    mc_pensamiento "Y le quité la única cosa que estaba defendiendo."

    mc_pensamiento "No era el ejercicio. Era hacerlo ella sola."

    show itsuki neutral at pj(0.5)
    with dissolve

    itsuki "Puedes irte. Ya tengo lo que necesitaba."

    narrador "Cerró el cuaderno del todo esta vez, con las dos manos."

    narrador "No volvió a levantar la vista."

    jump itsuki_m5

############################################################################
## MOVIMIENTO 5 · Cierre
## Común a las tres ramas, con un cierre cálido, tibio o frío según la elección.
############################################################################

label itsuki_m5:

    scene bg_aula_tarde
    with fade
     
    stop music fadeout 1.5

    narrador "Salí del aula cuando ya casi no quedaba luz de ventana."

    narrador "Ella seguía en su pupitre."

    mc_pensamiento "Una de cinco. Y esta no pidió nada."

    mc_pensamiento "Quedan tres semanas."

    if itsuki_rama_cap1 == "calida":

        mc_pensamiento "No me dio las gracias. No esperaba que lo hiciera."

        mc_pensamiento "Pero tampoco me dijo que me fuera."

        mc_pensamiento "Llevo dos días aprendiendo que con ella eso cuenta más que un gracias."

    elif itsuki_rama_cap1 == "tibia":

        mc_pensamiento "Rechazó la ayuda antes de saber qué era."

        mc_pensamiento "Puede que no confíe en mí."

        mc_pensamiento "O puede que no confíe en que nadie la ayude sin cobrárselo después."

    else:

        mc_pensamiento "Se lo resolví bien y rápido. Ni siquiera protestó."

        mc_pensamiento "Eso debería sentirse como ganar."

        mc_pensamiento "No se siente así."


    ## Marcar el evento como consumido para el evento 6 y para que el hub
    ## ofrezca la revisita corta en lugar del evento completo.
    $ itsuki_visitada_cap1 = True

        
    jump hub
    