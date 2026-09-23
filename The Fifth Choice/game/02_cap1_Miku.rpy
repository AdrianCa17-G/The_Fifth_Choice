################################################################################
##  HUB DE MIKU
################################################################################

label hub_Miku:

    ############################################################################
    ##  MOVIMIENTO 1 · Llegada
    ##  Primer encuentro entre mc y Miku en la biblioteca
    ############################################################################

    #BG NUEVO — bg_biblioteca]` `[MUS stop fadeout 1.0]`

    narrador "La biblioteca municipal quedaba dos calles antes del edificio." 

    narrador "Pasaba por delante todos los días y nunca había entrado."

    narrador "Segunda planta, la sala de lectura. Cuatro mesas largas y nadie en tres de ellas."

    #CG NUEVO — cg_miku_biblioteca: Miku de tres cuartos en la mesa del fondo, leyendo, con la pila de libros a un lado y los audífonos COLGADOS DEL CUELLO, nunca puestos. Ventanal detrás, luz de tarde. Cámara desde un costado, no desde la puerta. Un solo personaje en el frame. Sostiene todo el movimiento 1, así que tiene que aguantar en pantalla.]`

    narrador "Estaba al fondo, de espaldas a la puerta, con una pila de libros a la izquierda y los 
    audífonos colgados del cuello."

    mc_pensamiento "Cuatro libros. Ninguno del temario."

    mc_pensamiento "Y no estaban amontonados. Estaban apilados por tamaño, con los lomos alineados."

    narrador "No pasaba las páginas. Se quedaba en cada una bastante más de lo que se tarda en leerla."

    mc_pensamiento "Así no se estudia."

    mc_pensamiento "Así se lee."

    mc_pensamiento "Y los audífonos estaban apagados."

    mc_pensamiento "A esta distancia no se oye algo, aunque sea un zumbido. No escuchaba nada."

    mc_pensamiento "El otro día, en el departamento, se los subió en cuanto saqué las hojas."

    mc_pensamiento "Me borró del mapa sin decir una palabra."

    mc_pensamiento "No los lleva para escuchar música."

    mc_pensamiento "Los lleva ahí abajo, listos, para el momento en que alguien se acerque."

    narrador "Me senté enfrente."

    narrador "Tardó tres segundos largos en levantar la vista."

    #`[BG bg_biblioteca with dissolve]` 
    
    show miku neutral at pj(0.5)

    miku "…"

    mc "Buenas tardes."

    miku "…"

    miku "…¿Cómo sabías que estaba aquí?"

    mc "No lo sabía. Llevo una hora dando vueltas."

    mc "Pasé por tu casa primero."

    mc "Ninguna de tus hermanas supo decirme dónde estabas."

    narrador "Algo se le movió en la cara al oír eso, tan rápido que no me dio tiempo a leerlo."

    miku "…¿Y entonces?"

    mc "El libro que llevabas el otro día tenía la etiqueta de una biblioteca."
    
    mc "Esta es la que queda cerca del edificio."

    narrador "Bajó el libro dos dedos, lo justo para mirarme por encima del canto."

    miku "…Ah."

    narrador "No pareció convencerle del todo, pero tampoco se levantó."

    ############################################################################
    ##  MOVIMIENTO 2 · El intento por la puerta principal
    ##  Mc decide ayudar a Miku en la asignatura que se le da bien
    ############################################################################

    play sound sfx_papel_mesa volume 2.5

    narrador "Saqué el temario de sociales y lo puse sobre la mesa, girado hacia ella."

    #`[CG NUEVO — cg_estudio_biblioteca: POV desde el sitio de Futaro. Primer término inferior, sus antebrazos y sus manos sosteniendo el temario abierto sobre la mesa, desenfocados y cortados por el borde. Enfrente, Miku de tres cuartos con su libro, sin devolver la mirada. Mismo lenguaje que cg_pupitre_manana y cg_manija_edificio: nada de cara, nada que el modelo pueda romper.]`

    mc "Quedan tres semanas y media para el examen." 

    mc "Historia es tu asignatura."

    miku "No es mi asignatura"

    mc "Es la que mas conocimientos tienes y la que más fácil puedes aprender."
    
    mc "Empezamos por ahí."

    miku "…"

    mc "Unificación de Japón. Del final de las guerras civiles al periodo Edo."

    miku "…Está bien."

    mc "¿Está bien que sí, o está bien que me calle?"

    miku "…"

    mc "Lo voy a tomar como que sí."

    narrador "Bajó la vista al temario tres segundos y la volvió a subir al libro que tenía abierto."

    mc_pensamiento "Tres segundos. Los conté."

    mc_pensamiento "Perfecto. Un muro de ladrillo, pero educado."

    mc_pensamiento "Llevo dos días haciendo lo mismo con las cinco y progresando con ninguna."

    mc_pensamiento "Repasemos lo que sé de Miku."

    mc_pensamiento "Uno: el primer día me habló de logística del período Sengoku sin que le preguntara, "

    mc_pensamiento "y luego se escondió detrás del libro en cuanto se oyó a sí misma."

    mc_pensamiento "Dos: en su hoja de ayer había una marca de borrador debajo de la respuesta equivocada." 

    mc_pensamiento "Escribió la correcta primero y la borró."

    mc_pensamiento "Tres: lleva unos audífonos apagados colgados del cuello,"

    mc_pensamiento "listos para subírselos en cuanto alguien le hable."

    mc_pensamiento "No es que no sepa." 
    
    mc_pensamiento "Es que no piensa hablar de nada que le importe delante de alguien que va a calificarla."

    mc_pensamiento "Y no se me ocurrió ninguna forma de resolver eso."

    mc_pensamiento "Solo se me ocurrió la de siempre."


    ############################################################################
    ##  MOVIMIENTO 3 · La página noventa
    ##  Mc ayuda a Miku a que hable sobre su hobby que es la historia
    ############################################################################

    narrador "Cerré el temario y saqué de la mochila otro libro, con la misma etiqueta en el lomo que los suyos."

    play sound sfx_papel_mesa volume 2.5

    narrador "Lo reconoció antes de que llegara a la mesa."

    #`[CG NUEVO — cg_miku_sorpresa: mismo encuadre y misma luz que cg_miku_biblioteca —esa semilla sirve de punto de partida— pero con el libro bajado del todo, los ojos abiertos y la mirada fuera del libro por primera vez. El ejemplar de Futaro entra en el cuadro por el borde inferior, sin mano. Es el otro lado de la moneda del primero: en aquel no miraba, en este mira.]`

    miku "…Ese es el que estaba leyendo yo."

    mc "Hay dos ejemplares. Lo saqué anoche."

    miku "…¿Por qué?"

    mc "Porque el otro día dijiste que las batallas las gana quien mueve el arroz y no entendí a que te referías."

    mc "Sentí intriga por lo que esa frase significaba."

    narrador "No dijo nada. Pero tampoco volvió al libro."

    mc "Llegué hasta la página noventa. Me quedé dormido a las tres."

    mc "Y creo que el tipo que lo escribió se equivoca."

    #`[BG bg_biblioteca with dissolve]` 
    
    show miku neutral at pj_habla(0.5)

    miku" …¿En qué?"

    mc "Le dedica cuarenta páginas a cómo se movía la comida y seis a la batalla más famosa del siglo."
    
    mc "Está al revés."

    mc "Las guerras se ganan en el campo de batalla. Lo demás es puro papeleo."

    narrador "Miku cerró el libro sobre el dedo índice, para no perder la página."

    mc_pensamiento "Era la primera vez en dos días que dejaba de mirar a otro lado."

    miku "…¿Y qué comían?"

    mc "¿Quiénes?"

    miku "…Los treinta mil hombres. En esa batalla famosa."

    mc "…"

    miku "…Tres veces al día. Todos los días. Durante las seis semanas que tardaron en llegar hasta ahí caminando."

    mc "Eso lo resolverían entre ellos. No es importante."

    #`[SPR NUEVO — miku animada at pj_habla(0.5)]` `[MUS NUEVO — descubrimiento fadein 2.0]`

    miku "Había un señor de la guerra que se llamaba Takeda Shingen."

    miku "Su provincia estaba metida entre montañas. No tenía nada de costa."

    mc "¿Y eso es un problema?"

    miku "Sin mar no hay sal. Y sin sal no se podía guardar la comida: no existían las neveras."

    miku "O salabas el pescado y la carne, o en tres días no servían."

    miku "Toda la sal que comía su gente se la compraban a los vecinos."

    narrador "Hablaba más rápido."

    narrador "No había subido la voz —seguíamos en una biblioteca—,"
    
    narrador " pero las frases le habían dejado de empezar con una pausa."

    miku "Y un día los vecinos se pusieron de acuerdo y dejaron de vendérsela."

    mc "…Sin atacarlo."

    miku "Sin un soldado. Sin salir de su casa. Solo dejaron de vender."

    mc "¿Y qué hizo?"

    miku "Nada. No había nada que hacer. Lo estaba perdiendo todo."

    miku "Y entonces le mandó sal Uesugi Kenshin. Su peor enemigo."

    miku "Llevaban diez años peleándose y ninguno de los dos había conseguido ganar."

    mc "¿Si era su enemigo?¿Por qué haría eso?"

    miku "Dijo que él peleaba con armas, no con comida." 

    miku "Que quería ganarle en un campo de batalla, no verlo morirse de hambre en su casa."

    miku "De ahí sale una frase que en Japón todavía se dice."

    miku "«Mandarle sal al enemigo.» "

    miku "Se usa para cuando ayudas a alguien que no soportas, porque hay cosas que no se hacen."

    miku "Aunque seguramente no pasó."

    mc "…¿Cómo que no pasó?"

    miku "Esa parte no aparece en ningún papel de la época."

    miku "Está escrita cien años después, solo para que la historia sonara más atractiva."

    miku "Lo que sí es seguro es que les quitaron el acceso a la sal y que ahí dentro siguió habiendo sal igual."

    miku "Alguien se la vendió."

    miku "Y a mí eso me parece mucho más—"

    #`[SPR NUEVO — miku encogida at pj(0.5)]` 
    
    stop music fadeout 1.5

    narrador "Se paró en mitad de la palabra."

    narrador "Creo que se oyó."

    narrador "Fue eso: se oyó a sí misma hablando en voz alta durante un minuto entero."

    miku "…"

    miku "…Perdón. Hablé mucho."

    narrador "Y volvió a abrir el libro por donde tenía el dedo."

    ############################################################################
    ##  MOVIMIENTO 4 · La decisión
    ##  Aqui mc decide si ayudar a aumentar la confianza de Miku o no
    ############################################################################

    mc_pensamiento "Tercera vez."

    mc_pensamiento "Tercera vez que dice algo que nadie le pidió y tercera vez que se disculpa por haberlo dicho."

    mc_pensamiento "Nadie se disculpa por decir algo cierto, a menos que le hayan enseñado que decirlo cuesta."

    ## Menú de sabor.
    menu:

        narrador "¿Que le dirás a Miku?"

        "Ponerla a prueba. Preguntarle por un detalle del libro.": 
        
            #(cálida — `[$ sumar_punto("miku", 1)]`)

            mc "¿Cuánto tardaba la sal en llegar desde el mar hasta allá?"

            #`[SPR miku encogida at pj_habla(0.5)]`

            miku "…¿Qué?"

            mc "Es una pregunta."

            mc "Montaña, carga a lomo de animal, hace quinientos años. Cuánto tardaba."

            miku "…Diez días. Doce si llovía."

            mc "¿Y cuánto aguantaban ellos sin sal?"

            #`[SPR miku animada at pj_habla(0.5)]` `[MUS descubrimiento fadein 2.0]`

            miku "Depende de la época del año. En verano, con el pescado, casi nada." 

            miku "Por eso quitarles el acceso a la sal no era una amenaza para más adelante, era de ese mismo mes."

            miku "Eso es lo que a la gente se le esca—"

            narrador "Se detuvo otra vez. Pero esta vez se detuvo distinto."
            
            narrador "Se detuvo mirándome a mí, no al libro."

            miku "…Per—"

            mc "No."

            miku "…"

            mc "Estabas contestando una pregunta que te hice yo. Eso no se disculpa."

            narrador "No dijo nada. Se le puso el libro a media altura, sin llegar a subirlo del todo."

            narrador "Y entonces miró el ejemplar que yo había dejado sobre la mesa."

            miku "…Dijiste que llegaste a la página noventa."

            mc "Noventa y dos."

            miku "…Lo de la sal está en la ciento veinte."

            narrador "Lo dijo despacio, como quien termina una cuenta."

            mc_pensamiento "Ahí estaba lo que acababa de entender."

            mc_pensamiento "No que yo supiera de esto."

            mc_pensamiento "Justo lo contrario: que no sabía nada, y que aun así me había pasado la noche en ello."

            mc "Voy a llegar a la ciento veinte."

            miku "…"

            mc "Lo que acabas de contarme son tres preguntas del examen."

            mc "Rutas de comercio, cómo se sostenía una provincia y por qué acabó unificándose el país."

            mc "No te falta la materia. "

            mc "Te falta creer que lo que sabes cuenta como saber."

            miku "…No es lo mismo."

            mc "Es exactamente lo mismo, y lo vas a comprobar en tres semanas."

            narrador "No me contestó."
            
            narrador "Pero cuando me levanté, el libro seguía a media altura y no había vuelto a subir."


        "Reconocer su nivel. Hacer una valoración de su esfuerzo.": 
        
            #(tibia — sin puntos, sin desaire)

            mc "Se te da bien esto."

            #`[SPR miku encogida at pj_habla(0.5)]`

            miku "…No se me da bien. Solo lo he leído."

            mc "Que es más de lo que ha hecho nadie en tu casa."

            miku "…Eso no es difícil."

            narrador "Lo dijo sin ninguna gracia, como quien cierra una puerta con educación."

            mc_pensamiento "Le acabo de poner una etiqueta."

            mc_pensamiento "Y ella lleva toda la vida escuchando etiquetas comparadas con otras cuatro."

            narrador" El libro le subió hasta media cara, y ahí se quedó."

            

        "El Sengoku no entra en el examen.": 
        
            #(fría — `[$ desaires_cap1 += 1]`)

            mc "Nada de eso entra en el examen."

            mc "Unificación de Japón, tres temas, y ninguno pregunta por la sal."

            mc "Si vas a dedicarle una hora a algo, que sea a lo que te van a preguntar."

            show miku neutral at pj(0.5)

            narrador "No protestó. No se defendió."

            narrador "Asintió una vez, muy despacio, como si le hubieran confirmado algo que ya sospechaba."

            miku "…Ya lo sé."

            narrador "Miró un segundo el ejemplar que yo había dejado sobre la mesa, y después apartó la vista."

            mc "Entonces empecemos por el tema uno."

            miku "…Hoy no."

            play sound sfx_silla volume 2.5

            narrador "Recogió los cuatro libros, los apiló y se subió los audífonos."

            narrador "Y esta vez, desde donde yo estaba, se oía la música."

            mc_pensamiento "…"

            mc_pensamiento "Antes no sonaban."

    ############################################################################
    ##  MOVIMIENTO 5 · Cierre
    ##  Fin de la interacción entre Miku y Mc.
    ##  Común a las tres ramas; la última línea cambia
    ############################################################################

   
    scene bg_negro 
    with fade

    narrador "Salí de la biblioteca cuando estaban apagando las luces de la segunda planta."

    mc_pensamiento "Una de cinco. Y ni siquiera entera."

    mc_pensamiento "Quedan tres semanas."

    #Cierre A (cálida)

    mc_pensamiento" Pero hoy alguien me habló durante un minuto seguido sin que yo se lo pidiera dos veces."

    mc_pensamiento" Eso, en esa casa, es un récord."

    #Cierre B (tibia)

    mc_pensamiento "Dijo cuatro frases y volvió a esconderse." 

    mc_pensamiento "No sé si perdí algo, pero desde luego no gané nada."

    #Cierre C (fría)

    mc_pensamiento "Tenía razón en lo del examen."

    mc_pensamiento "Lo raro es que llevo toda la tarde con la sensación de haber hecho algo mal teniendo razón."

    #`→ Vuelve al hub.`





