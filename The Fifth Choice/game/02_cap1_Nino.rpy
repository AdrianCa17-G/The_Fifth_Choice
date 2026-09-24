
## ==========================================================================
## EVENTO PRINCIPAL
## ==========================================================================

label hub_Nino:

    ############################################################################
    ##  MOVIMIENTO 1 · Llegada
    ##  Primer encuentro con Nino en el centro comercial.
    ############################################################################

    #scene bg centro_comercial
    stop music fadeout 1.0

    narrador "La encontré en la zona de repostería internacional."

    narrador "Dos pasillos después de la entrada."

    narrador "Era de esos estantes donde las etiquetas venían en otro idioma y los precios no perdonaban."

    narrador "Casi nadie a esa hora."

    narrador "El resto de la sección estaba vacío. Dos carritos abandonados a medio pasillo, sin dueño."

    mc_pensamiento "De las cinco, era la que menos pistas dejaba de dónde encontrarla."

    mc_pensamiento "Las otras cuatro, sin querer, siempre dejan algo."
    
    mc_pensamiento "Un horario, una costumbre, un lugar que mencionan de pasada."

    mc_pensamiento "Ella no."

    narrador "Tuve que preguntar dos veces en información antes de que alguien recordara haberla visto entrar."

    mc_pensamiento "Y aun así no dijeron hacia dónde."

    narrador "La encontré por descarte, no porque alguien me lo dijera."

    ## CG 1 — el hallazgo: Nino comparando etiquetas sin saber que la miran.
    #scene cg nino_centro_comercial with dissolve

    narrador "Tenía una caja en cada mano, leyendo la etiqueta de una y después la otra."

    mc_pensamiento "Harina normal. Harina con leudante."

    mc_pensamiento "Las dos en inglés, sin una palabra en japonés en ninguna caja."

    narrador "Movía los labios leyendo, muy bajo, casi sin sonido."

    mc_pensamiento "No estaba traduciendo con esfuerzo."

    mc_pensamiento "Estaba leyendo, directo, como quien no necesita traducir nada."

    narrador "Sacó la tarjeta de receta del bolsillo del delantal y volvió a comparar."

    mc_pensamiento "Letra a mano. Vieja."

    mc_pensamiento "De alguien que la escribió hace tiempo."

    narrador "Me quedé un momento en la esquina del pasillo, sin que ella lo notara."

    narrador "Terminó eligiendo una de las dos cajas y la metió en la cesta."

    play sound audio.sfx_bolsa volume 1.5

    narrador "El ruido del plástico la hizo detenerse en seco."

    narrador "Giró la cabeza..."

    narrador "Y sus ojos se clavaron en los míos antes de que pudiera disimularlo."


    ############################################################################
    ##  MOVIMIENTO 2 · La grieta
    ##  Nino se abre un poco, pero no lo suficiente. 
    ##  La conversación se vuelve más personal, pero no hay promesas.
    ############################################################################

    #scene bg centro_comercial

    show nino neutral at pj(0.5)
    with dissolve

    nino "¿Tu?"

    nino "¿Qué haces aquí?"

    mc "Buscarte. Me tocó adivinar dónde estabas."

    nino "No te pedí que me buscaras."

    mc "No hacía falta que me lo pidieras."

    mc "Es mi trabajo como tu tutor."

    narrador "Cerró la cesta contra su cuerpo, como si yo pudiera ver algo más adentro."

    mc "¿Vienes seguido a este pasillo?"

    nino "Eso no te importa."

    narrador "Dio un paso, poniéndose entre yo y la estantería de importados, como si hubiera pisado algo que no me tocaba."

    mc "En tu casa hay despensa. ¿Para qué venir hasta aquí?"

    nino "Porque en la despensa no hay nada que valga la pena."

    narrador "Lo dijo cortante, cerrando el tema de un golpe."

    mc "¿Vas a comprar toda la tienda o solo la mitad?"

    nino "Busca a otra a quien fastidiar."

    mc "Las otras cuatro no están aquí."

    narrador "No contestó a eso."
    
    narrador "Volvió a mirar las dos cajas de harina, aunque ya había decidido."

    mc "¿Qué dice esta lata? No reconozco ni la mitad de las palabras."

    narrador "Señalé una al azar, en el estante de al lado, solo por decir algo que no sonara a interrogatorio."

    nino "Extracto de vainilla. Doble concentración."

    narrador "Lo leyó sin pausa, sin buscar la palabra, como si estuviera leyendo en japonés."

    mc "¿Y esto?"

    narrador "Señalé otra caja, una palabra más larga, de esas que se traban al leerlas."

    nino "'Confectioners' sugar."

    narrador "Lo dijo bien. Demasiado bien para alguien que en clase apenas levanta la mano."

    mc "Se te da mejor de lo que aparentas en el salón."

    nino "No es lo mismo leer que..."

    narrador "Se detuvo, buscando cómo seguir la frase."

    nino "Da igual. Olvídalo."

    narrador "Le costó más terminar esa frase que leer la etiqueta entera."

    mc "¿Por qué a mí me tratas distinto que a ellas?"

    nino "No te trato distinto."

    mc "Sí lo haces. Y no solo a mí."
    
    mc "A todos los que han entrado antes que yo."

    narrador "Ahí sí levantó la vista."

    show nino nerviosa at pj(0.5)
    with dissolve

    nino "…"

    nino "Porque los que entraron antes también sonreían el primer día."

    nino "Y no es que yo sea así porque sí, ¿sabes? No es un capricho."

    nino "Es que ya perdí la cuenta de cuántas veces mis hermanas..."

    narrador "Se detuvo, pero solo un segundo. No fue el corte de siempre."

    narrador "Lo dijo más rápido de lo que suele hablar."

    narrador "Sin cortar la frase a la mitad como acostumbra."

    ## CG 2 — la grieta: plano cerrado sobre la tarjeta de receta.

    # scene cg nino_receta with dissolve

    nino "También decían que iban a quedarse. Que esta vez iba a ser distinto."

    nino "Y a la semana siguiente ya no estaban."

    mc_pensamiento "No está hablando de mí."

    mc_pensamiento "Está hablando de todos los que vinieron antes, y me está poniendo en la misma fila sin que yo haya hecho nada todavía."

    nino "Mis hermanas se ilusionan cada vez. Cada una a su manera, pero se ilusionan."

    nino "Y después les toca ver a alguien irse."

    narrador "Apretó la tarjeta un poco más fuerte contra el pecho."

    mc_pensamiento "No está protegiéndose a ella."
    
    mc_pensamiento "Está protegiendo a sus hermanas de algo que ya les pasó demasiadas veces."

    #scene bg centro_comercial

    show nino neutral at pj(0.5) 
    with dissolve

    nino "…"

    nino "Olvida lo que dije."

    narrador "Se cortó a mitad de frase, algo que ella nunca hace por accidente."

    narrador "Guardó la tarjeta en el bolsillo del delantal."

    narrador "Rápido, como quien tapa algo que se le cayó."

    mc_pensamiento "No pregunté más. Habría sido pedirle algo que no me tocaba todavía."

    narrador "Se acomodó el delantal, como si con eso pudiera acomodar también lo que acababa de decir."

    ## ---------------------------------------------------------------
    ## Movimiento 3 · La decisión
    ## ---------------------------------------------------------------

    #play music audio.descubrimiento volume 0.0

    narrador "Se agachó a recoger la cesta del suelo, sin mirarme."

    nino "¿Y bien? ¿Vas a decir algo o te vas a quedar ahí parado?"

    mc_pensamiento "Tiene razón en desconfiar."

    mc_pensamiento "Eso no se lo puedo discutir."

    mc_pensamiento "Lo que diga ahora decide si me pone en la misma fila que los otros cuatro, o no."

    # Menu del sabor

    menu:
        "¿Cómo respondes?"

        "Tienes razón en desconfiar. Solo el tiempo lo va a demostrar.":
            jump nino_centro_comercial_m4a

        "Ayudarla con las bolsas, sin decir nada.":
            jump nino_centro_comercial_m4b

        "Yo sí voy a durar.":
            jump nino_centro_comercial_m4c


## ---------------------------------------------------------------
## Movimiento 4A · Rama cálida
## ---------------------------------------------------------------

label nino_centro_comercial_m4a:

    $ nino_rama_cap1 = "calida"
    $ sumar_punto("nino", 1)

    #play music audio.descubrimiento fadein 1.0 volume 3.5

    mc "Tienes razón en desconfiar."

    show nino neutral at pj(0.5)
    with dissolve

    nino "…¿Qué?"

    mc "No te voy a decir que esta vez es distinto."

    mc "Ya lo escuchaste demasiadas veces."

    mc "Solo el tiempo lo va a demostrar."

    mc "Hablar de más no va a convencerte."

    narrador "Se quedó quieta, con la cesta a medio subir, como si esperara el resto de la frase que no llegó."

    show nino nerviosa at pj(0.5)
    with dissolve

    nino "…"

    nino "Esa es la primera vez que alguien no me promete nada."

    mc "No tengo nada que prometer todavía."

    mc "No he hecho nada que lo merezca."

    narrador "Lo pensó un momento, sin la hostilidad de antes ni la calma que tampoco tiene."

    show nino neutral at pj(0.5)
    with dissolve

    nino "Eso no significa que confíe en ti."

    mc "No dije que lo hicieras."

    nino "Bien. Que quede claro."

    narrador "Se quedó mirando la tarjeta de receta un segundo más, antes de guardarla del todo."

    nino "…No le digas a mis hermanas que hablé de más."

    mc "No dije nada de más."

    nino "Tú entendiste. Con eso alcanza."

    narrador "Terminó de subir la cesta al brazo y siguió caminando hacia la caja, sin esperarme, pero sin decirme que me fuera tampoco."

    mc_pensamiento "No gané su confianza. Todavía no."
  
    mc_pensamiento "Pero por lo menos entendió que no iba a regalarle promesas vacías."

    jump nino_centro_comercial_m5


## ---------------------------------------------------------------
## Movimiento 4B · Rama tibia
## ---------------------------------------------------------------

label nino_centro_comercial_m4b:

    $ nino_rama_cap1 = "tibia"
    ## sin puntos, sin desaire

    narrador "No dije nada."

    narrador "Levanté la otra cesta que había dejado en el suelo y empecé a caminar hacia la caja."

    show nino neutral at pj(0.5)
    with dissolve

    nino "¿Qué haces?"

    mc "Ayudarte con esto. Pesa."

    nino "No te pedí ayuda."

    mc "No la pediste. Te la estoy dando igual."

    narrador "Se quedó un segundo sin saber qué contestar a eso."

    nino "…Esa cesta pesa más de lo que parece."

    mc "Ya lo noté."

    narrador "Fue lo más parecido a un agradecimiento que iba a conseguir, y terminó caminando a mi lado sin discutirlo."

    nino "Esto no significa nada."

    mc "No dije que significara algo."

    narrador "Hicimos el resto del pasillo en silencio, cada uno con su cesta."

    mc_pensamiento "No dijo nada más de lo que se le escapó."

    mc_pensamiento "Y yo preferí dejarlo así."

    mc_pensamiento "A veces el silencio es lo único que se puede compartir."

    jump nino_centro_comercial_m5


## ---------------------------------------------------------------
## Movimiento 4C · Rama fría
## ---------------------------------------------------------------

label nino_centro_comercial_m4c:

    $ nino_rama_cap1 = "fria"
    $ desaires_cap1 += 1

    mc "Yo sí voy a durar."

    narrador "Lo dije para tranquilizarla."

    narrador "No funcionó."

    show nino neutral at pj(0.5)
    with dissolve

    nino "…"

    narrador "Se rió, pero no de gracia."

    nino "Eso mismo dijo el que llegó antes de ti."

    nino "Palabra por palabra, casi."

    mc "Yo no soy él."

    nino "Todos dicen eso también."

    mc "Entonces qué querías que dijera."

    nino "Nada. Ese es el punto."

    narrador "Terminó de acomodar la cesta en el brazo, ya sin mirarme."

    nino "Guárdate la promesa. No la voy a necesitar."

    mc_pensamiento "Le dije exactamente lo que no quería oír."

    mc_pensamiento "Y lo peor es que lo dije pensando que la iba a ayudar."

    narrador "Caminó hacia la caja sin esperarme, ocultando el papel antes de que pudiera ver algo más."

    jump nino_centro_comercial_m5


## ==========================================================================
## Movimiento 5 · Cierre (común a las tres ramas)
## ==========================================================================

label nino_centro_comercial_m5:

    #scene bg centro_comercial tarde
    stop music fadeout 1.5

    narrador "La acompañé hasta la salida, cargando lo que me dejó cargar."

    mc_pensamiento "Una de cinco. Y esta no bajó la guardia ni un minuto entero."

    narrador "En la caja, pagó ella misma, sin dejarme acercar la cartera."


    mc_pensamiento "Ni eso me lo iba a dejar hacer."
    
    mc_pensamiento "Quedan tres semanas."

    ## ---------------------------------------------------------------
    ## Movimiento 6 · La llamada (común a las tres ramas)
    ## ---------------------------------------------------------------

    narrador "Casi en la puerta, el celular le sonó en el bolsillo del delantal."

    nino "¿Qué?"

    narrador "Contestó sin mirar la pantalla. Debía saber de memoria quién era."

    nino "Sí, papá. Ya voy para allá."

    narrador "Se adelantó un paso, dándome la espalda, como si eso bastara para que no la escuchara."

    nino "Sobre el tutor nuevo..."

    narrador "Bajó la voz. No lo suficiente."

    nino "Aún no me convence."

    mc_pensamiento "No dijo mi nombre. No hacía falta."

    nino "No, no pasó nada."

    narrador "Se quedó escuchando lo que fuera que le contestaran del otro lado, con la mandíbula apretada."

    nino "Porque no quiero explicarlo, por eso."

    narrador "Colgó antes de que la respuesta la obligara a decir algo más."

    narrador "Guardó el teléfono y siguió caminando hacia la salida, sin voltear a verme."

    hide nino 
    with dissolve

    mc_pensamiento "No dijo por qué."

    mc_pensamiento "Y por primera vez, no sonó a que me odiara."

    mc_pensamiento "Sonó a que no sabía cómo explicarlo sin decir de más."

    ## ---------------------------------------------------------------
    ## Movimiento 7 · Cierre final (varía según la rama elegida)
    ## ---------------------------------------------------------------

    if nino_rama_cap1 == "calida":

        mc_pensamiento "No confía en mí."

        mc_pensamiento "Lo dijo ella misma, y no tengo motivos para no creerle."

        mc_pensamiento "Pero por primera vez no me trató como al siguiente de la fila."

        mc_pensamiento "Me trató como algo todavía sin decidir."

    elif nino_rama_cap1 == "tibia":

        mc_pensamiento "Cargué dos bolsas y no dijimos nada importante."

        mc_pensamiento "No sé si eso cuenta como algo."

        mc_pensamiento "Con ella, nunca se sabe si avanzaste o retrocediste."

    else:
        mc_pensamiento "Le prometí que iba a durar."

        mc_pensamiento "Ella ya había escuchado esa frase antes."

        mc_pensamiento "Yo mismo la puse en la misma fila que los anteriores."

    ## Marcar el evento como consumido para el evento 6 y para que el hub
    ## ofrezca la revisita corta en lugar del evento completo.
    $ nino_visitada_cap1 = True

    jump hub
