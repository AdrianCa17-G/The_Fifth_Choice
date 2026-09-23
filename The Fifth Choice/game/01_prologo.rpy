################################################################################
##  THE FIFTH CHOICE — 01_prologo.rpy
##  FASE 1 — Prologo (version extendida)
##
##  Adapta el arranque del anime: la oferta del padre, el primer roce con
##  Itsuki, el encuentro con las cinco hermanas y el primer intento fallido
##  de dar clase.
##
##  NOTA DE DISENO: el prologo NO otorga puntos de afinidad.
##  Las variables puntos_* y primera_conexion permanecen intactas hasta la
##  primera decision real del Capitulo 1. Los menus de este archivo solo
##  cambian el dialogo inmediato y vuelven a converger.
##
##  Personajes, fondos, sprites, transforms y audio viven en
##  00_definiciones.rpy. Aqui solo quedan los CG propios de estas escenas y
##  el `label prologo`.
################################################################################


################################################################################
##  CG PROPIOS DEL PROLOGO
##  Ilustraciones de momentos concretos de estas siete escenas. Los tres que
##  el Capitulo 1 reutiliza —cg_calificacion, cg_maruo_reunion y
##  cg_hermanas_estudiando— estan en 00_definiciones.rpy.
################################################################################

image cg_familia            = "cg/foto_familiar.webp"
image cg_examen             = "cg/examen.webp"
image cg_manija_edificio    = "cg/manija_edificio.webp"

image cg_itsuki_sentada     = "cg/itsuki_asiento.webp"
image cg_itsuki_azotea      = "cg/itsuki_azotea.webp"
image cg_itsuki_discusion   = "cg/itsuki_discusion.webp"

image cg_ichika_puerta      = "cg/ichika_puerta.webp"
image cg_nino_pasillo       = "cg/nino_pasillo.webp"
image cg_miku_sofa          = "cg/miku_sofa.webp"
image cg_yotsuba_corriendo  = "cg/yotsuba_corriendo.webp"


################################################################################
##  PRÓLOGO
################################################################################

label prologo:

    ############################################################################
    ##  ESCENA 1 · Casa de los Uesugi
    ##  Presentación del protagonista por lo que le falta, no por lo que es.
    ############################################################################

    ## Apertura en silencio a proposito: la entrada de `hogar` sobre el
    ## retrato familiar solo significa algo si antes no sonaba nada.
    stop music
    stop ambiente

    scene bg_negro
    with fade

    narrador "Hay dos clases de personas en este mundo."

    narrador "Las que pueden permitirse el lujo de equivocarse."

    narrador "Y las que no."

    mc_pensamiento "Yo pertenezco a la segunda."

    play music hogar fadein 3.0

    scene cg_familia
    with dissolve

    mc_pensamiento "Mi madre murió cuando yo era pequeño, dejándonos una deuda que todavía nos persigue." 

    mc_pensamiento "Mi padre y yo trabajamos hasta el cansancio."

    mc_pensamiento "(Aunque a veces eso no es suficiente para cubrir esta deuda...)" 

    mc_pensamiento "Luego está Raiha, que sin lugar a dudas, merece un futuro mejor que esta pobreza." 

    mc_pensamiento "Por eso estudio." 
    
    mc_pensamiento "No por vocación o por esas cosas bonitas que dicen los profesores en las ceremonias de ingreso."

    mc_pensamiento "Estudio porque las notas son lo único que puedo controlar."

    scene cg_calificacion
    with dissolve

    mc_pensamiento "Esta pila de libros es la única herramienta que tengo para cambiar nuestra realidad."

    mc_pensamiento "Logré el primer puesto en el examen nacional. Otra vez."

    mc_pensamiento "No es como que me alegre, eso no llenará la nevera."

    narrador "De repente, una voz infantil interrumpió los pensamientos intrusivos de [mc]."

    raiha "¡Hermanito! ¡Baja a cenar de una vez!"

    mc "Dame un segundo Raiha, ya mismo termino la tarea."

    raiha "¡Llevas media hora con el mismo 'segundo'! ¡Y el curry no va a durar caliente para siempre!"

    mc_pensamiento "(¿Curry? ¿Hoy no tocaba solo sopa de miso...?)"

    mc "Está bien... Ya voy."

    mc_pensamiento "Raiha. Mi hermana pequeña."
    
    mc_pensamiento "La única persona en esta casa que sigue creyendo que las cosas pueden salir bien."

    mc_pensamiento "Y la única razón por la que no me he rendido todavía."

    play music cena fadeout 1.5 fadein 2.0

    scene bg_comedor
    with fade

    mc "Hoy es una noche especial. ¡Raiha preparó curry!"

    mc_pensamiento "Para muchas personas, la cena es una simple reunión; un momento donde la familia come algo y ya."

    mc_pensamiento "Pero para mí, es el instante en el que doy gracias por todo."

    mc_pensamiento "A pesar de la gran deuda que cargamos, tengo una familia maravillosa. Una a la que siempre amaré y protegeré."

    narrador "Ya en la mesa, devoré el plato en cuestión de segundos."

    show raiha hablando at pj(0.20)
    with dissolve

    mc "¡Gracias por la comida!"

    raiha "Hermanito, hoy en la escuela dijeron que los hermanos mayores tienen que dar el ejemplo."

    mc "¿En serio? Supongo que yo soy un ejemplo perfecto para ti... ¿no?"

    show raiha regano at pj(0.20)
    with dissolve

    raiha "¡Por supuesto! Tú das el ejemplo de alguien obsesionado con los estudios y que no duerme bien."

    mc "La parte de dormir es negociable."

    raiha "¡No lo es! ¡Cuidar tu salud durmiendo bien también es importante!"

    raiha "…Anoche también te escuché pasar páginas a las tres."

    narrador "Lo dijo sin gritar, que en ella era prácticamente un susurro."

    mc_pensamiento "Se lo tomó tan en serio que casi me sentí culpable. Casi."

    ############################################################################
    ##  ESCENA 2 · La oferta
    ############################################################################

    ## Compite con `cena`, guitarra acustica en su mismo rango.
    $ duck()
    play sound sfx_papel_mesa volume 2.5

    narrador "De repente, mi padre, Isanari, entró en el comedor y dejó caer un papel sobre la mesa."

    show isanari neutral at pj(0.73)
    with dissolve

    show isanari neutral at pj_habla(0.73)
    show raiha regano at pj_calla(0.20)

    isanari "[mc]. Tengo un trabajo para ti."

    mc "¿Un trabajo? ¿De qué tipo?"

    isanari "Un conocido mío está buscando un tutor privado para su familia."

    mc "¿Tutor privado?... Creo que esta vez paso."
    
    mc "No me llama la atención y tampoco soy del tipo que sabe enseñarle a los demás."

    isanari "En eso tienes un punto, pero lo que sí te va a interesar es saber el pago."

    show isanari neutral at pj_calla(0.73)

    mc_pensamiento "Al escuchar la palabra 'pago', puse la mayor atención posible."

    mc_pensamiento "(No es como que crea que el dinero lo es todo, pero en esta situación que nos encontramos...)"

    mc "¿De cuánto estamos hablando?"

    show isanari neutral at pj_habla(0.73)

    isanari "Cinco veces la tarifa normal de un tutor."

    narrador "Hubo un silencio breve. El tipo de silencio que delata a alguien que ya aceptó la propuesta en su mente."

    mc "...Entiendo. ¿Tienes más detalles?"

    isanari "Es una familia adinerada. Un solo domicilio y clases particulares hasta la graduación."

    mc_pensamiento "Suena demasiado perfecto... Seguro debe haber una trampa."

    mc "¿Y el truco?"

    isanari "¿Por qué asumes que hay un truco?"

    mc "Porque nadie paga cinco veces más por algo que se consigue por una."

    show isanari sonriendo at pj_habla(0.73)
    with dissolve

    narrador "Mi padre sonrió. Aquello significaba que el truco existía y que habría que descubrirlo por las buenas o por las malas."

    isanari "Detalles menores. Ya los verás."

    mc "Los detalles menores son los que arruinan los cálculos."

    isanari "Entonces trátalo como un examen sorpresa. Se te dan bien."

    mc_pensamiento "Sabe exactamente qué tecla tocar. Siempre lo ha sabido."

    mc_pensamiento "Y siempre la toca cuando necesita algo de mí."

    show isanari sonriendo at pj_calla(0.73)
    show raiha hablando at pj_habla(0.20)

    raiha "¡Hermanito, deberías aceptar!"

    raiha "¡Así podrías estudiar tranquilo sin andar contando cada cosa que compramos!"

    mc "Me lo pensaré, Raiha."

    show raiha hablando at pj_calla(0.20)

    mc_pensamiento "No es el trabajo de mis sueños, pero..."

    mc_pensamiento "¡Debo aceptarlo a como dé lugar! ¡Esa deuda no se pagará sola!"

    ## Menú de sabor.
    menu:
        "¿Qué te empuja a aceptar?"

        "El dinero. Sin adornos.":
            mc_pensamiento "No voy a fingir nobleza. Aceptaré por el dinero, y punto."
            mc_pensamiento "Las buenas intenciones no pagan las facturas."

        "La cara de Raiha.":
            mc_pensamiento "¡Raiha merece una vida mejor!"
            mc_pensamiento "¡Lo haré por ella!"

        "La costumbre de no rendirme.":
            mc_pensamiento "Nunca he abandonado un problema a medio resolver."
            mc_pensamiento "Y este no será la excepción."

    mc "Está bien. Lo haré."

    show isanari sonriendo at pj_habla(0.73)
   
    isanari "Sabía que entrarías en razón."

    show raiha hablando at pj_habla(0.20)

    mc_pensamiento "Enseñar a otros no es lo mío... pero dada nuestra situación, no puedo darme el lujo de rechazarlo."

    ############################################################################
    ##  ESCENA 3 · Instituto Asaba
    ##  Primer roce con Itsuki. El jugador aún no sabe que son cinco.
    ############################################################################

    stop music fadeout 1.0

    scene bg_escuela
    with fade

    play sound sfx_timbre volume 1.5

    mc_pensamiento "A la mañana siguiente llegué al instituto antes que casi nadie."

    mc_pensamiento "Prefiero esta hora, cuando los pasillos todavía están vacíos."

    mc_pensamiento "Es el único rato del día en que este sitio no me recuerda que los demás sí pueden permitirse estar tranquilos."

    play music cotidiano fadein 2.5

    mc_pensamiento "(Cierto... hoy entregan los resultados de los exámenes de práctica. Iré al salón)."

    scene cg_examen
    with dissolve

    profe "[mc]. Enhorabuena por el examen de práctica. Otra vez el primer lugar."

    mc "Gracias, profesor. Solo mantengo el nivel."

    profe "Con estas notas, no me cabe duda de que te espera un gran futuro."

    mc_pensamiento "(Palabras bonitas. Lástima que el futuro no pague las facturas de hoy)."

    scene bg_aula
    with dissolve

    mc_pensamiento "Con mi examen perfecto en mano, fui a buscar mi asiento habitual."

    mc_pensamiento "Mi rincón habitual."

    mc_pensamiento "El único lugar de esta aula donde podía concentrarme sin escuchar tonterías."

    mc_pensamiento "Sin embargo, mi sitio..."

    play music incomodo fadeout 1.0 fadein 1.5

    scene cg_itsuki_sentada
    with dissolve

    mc_pensamiento "¡Estaba ocupado!"

    mc_pensamiento "¿Quién se cree que es para tomar mi lugar?"

    mc_pensamiento "¿Y encima se pone a comer tranquilamente en mi puesto?"

    mc "Perdona. Estás en mi asiento."

    mc_pensamiento "Tenía una ligera cara de preocupación... como si cargara con un problema encima o los exámenes le hubieran salido pésimo."

    itsuki_inicio "*Munch...* ¿Mm? Ah... tú debes ser [mc]."

    narrador "Sostuvo los palillos a mitad de camino y fijó su mirada en la hoja de examen que él llevaba en la mano."

    scene bg_aula
    with dissolve
   
    show itsuki sonriendo at pj(0.5)
    with dissolve

    itsuki_inicio "Escuché al profesor diciendo que tu examen fue de cien puntos." 
    
    itsuki_inicio "Además, dijo que eras el mejor de la clase." 
    
    itsuki_inicio "Verás, acabo de transferirme y las materias aquí son más difíciles..."
    
    itsuki_inicio "Así que..."

    itsuki_inicio "¿Podrías enseñarme un poco? Te lo agradecería mucho."

    mc "No."

    show itsuki sorprendida at pj(0.5)
    with dissolve

    itsuki_inicio "¡¿Eh?! ¡Ni siquiera te lo pensaste!"

    itsuki_inicio "¡Solo te pido algo de orientación mientras almuerzo!"

    mc "Aprender es un proceso personal."

    mc "Gastar mi tiempo para explicar cosas básicas no tiene sentido para mí."

    mc "Para eso están los profesores."
    
    mc "Ahora, si me disculpas, necesito mi asiento."

    itsuki_inicio "..."

    show itsuki molesta at pj(0.5)
    with dissolve

    ## Compite con `incomodo`. El arrastre no tiene ataque y se disuelve.
    $ duck()
    play sound sfx_silla volume 2.5

    narrador "La chica apretó los dientes, masticando el último bocado a la fuerza antes de levantarse en silencio."

    itsuki_inicio "Está bien. No te necesito."

    itsuki_inicio "Ingenuamente pensé que el mejor alumno de la clase sería alguien más amable."

    itsuki_inicio "Pero solo demostraste ser una persona arrogante y carente de empatía."

    # Sale del aula: la salida es una transición, no un ease.
    hide itsuki
    with moveoutleft

    narrador "Recogió sus cosas rápidamente y abandonó el aula sin ocultar su indignación."

    mc_pensamiento "..."

    mc_pensamiento "Tal vez fui un poco duro..."

    mc_pensamiento "Sin embargo..."

    mc_pensamiento "Enseñar a otros no viene en el examen final."

    mc_pensamiento "No gano nada haciéndolo gratis."

    ## La azotea va SIN musica, solo viento. Aqui los dos estan callados sin
    ## saber que decirse: no es la bronca del aula, es lo contrario, y el
    ## silencio hace mejor ese trabajo que cualquier pista.
    stop music fadeout 2.0

    scene bg_azotea
    with fade

    play ambiente amb_viento fadein 2.0 volume 1.5

    mc_pensamiento "Cuando por fin terminaron las clases, subí a la azotea a despejarme un poco."

    mc_pensamiento "No quería admitirlo."
    
    mc_pensamiento "Pero haber sido tan tajante con la chica nueva me dejó un mal sabor de boca el resto del día."

    narrador "Mientras reflexionaba, su momento de tranquilidad duró poco."

    narrador "Apenas diez minutos después, la puerta de la azotea se abrió."

    show itsuki sorprendida at pj(0.5)
    with dissolve

    itsuki_inicio "..."

    mc "..."

    itsuki_inicio "¿Otra vez tú?"

    show itsuki molesta at pj(0.5)
    with dissolve

    itsuki_inicio "Ni se te ocurra pensar que te vine a buscar."

    itsuki_inicio "Ni siquiera sabía que estabas aquí."

    mc "Tranquila, no me creo tan importante."

    mc "Aunque parece que hoy no me sale una bien."

    itsuki_inicio "Si tanto te molesta cruzarte conmigo, puedes irte."

    itsuki_inicio "Yo solo vine a tomar aire... y a alejarme de gente desagradable."

    mc_pensamiento "Perfecto. La azotea acaba de volverse el lugar más tenso del instituto."

    mc_pensamiento "(Esto se está volviendo ridículamente incómodo...)"

    ## Menú de sabor.
    menu:

        narrador "¿Cómo manejas esta situación?"
        
        "Ignorarla y ponerme a estudiar.":

            mc_pensamiento "Saqué mis apuntes de la mochila y dejé que el silencio hiciera su trabajo."

            show itsuki molesta at pj(0.5)
            with dissolve

            itsuki_inicio "…¿En serio vas a seguir estudiando incluso al terminar las clases?"
            mc "El temario del próximo examen no se va a repasar solo."
            itsuki_inicio "Qué persona tan agotadora."
            mc "Me lo dicen bastante."
            itsuki_inicio "No me extraña en lo absoluto."

        "Intentar rebajar la tensión.":

            narrador "La chica dejó escapar un pequeño suspiro y se cruzó de brazos, mirando al horizonte."

            scene cg_itsuki_azotea
            with fade

            mc "Si te sirve de algo, no fui desagradable por gusto. Solo soy celoso con mi tiempo."
            itsuki_inicio "Eso no quita que hayas sido un grosero."
            mc "Tal vez, pero es la verdad."
            itsuki_inicio "…"
            itsuki_inicio "Al menos eres honesto..."
            mc "Fingir cortesía sería un gasto innecesario de energía."
            

    scene bg_azotea
    with fade

    mc_pensamiento "Permanecimos en silencio con la luz del atardecer, cada uno en un extremo del banco." 
    
    mc_pensamiento "Como dos países que firman una tregua sin reconocerse."

    mc_pensamiento "Ella conocía mi apellido por el examen, pero no intercambiamos una sola palabra más."

    stop ambiente fadeout 2.0

    scene bg_negro
    with fade

    narrador "Ninguno de los dos sospechaba lo mucho que aquello terminaría importando."

    ############################################################################
    ##  ESCENA 4 · Camino al departamento
    ############################################################################

    mc_pensamiento "Al bajar de la azotea y recoger mi mochila, revisé el teléfono."

    mc_pensamiento "Tenía un mensaje de mi padre con una dirección y una instrucción clara:"
    
    narrador "'Ve hoy mismo al terminar las clases. La paga es excelente, no los hagas esperar'."

    mc_pensamiento "Acepté el trabajo sin dudarlo, pero no imaginaba a dónde me mandaba."

    play music cotidiano fadeout 1.0 fadein 2.0

    scene bg_edificio
    with dissolve

    narrador "La dirección que me dio correspondía a un edificio que solo había visto de lejos."

    mc_pensamiento "El tipo de zona donde la gente no mira los precios y el conserje te mide de arriba a abajo solo por pasar cerca."

    mc_pensamiento "(Bien... pongamos orden a esto antes de tocar la puerta)."

    scene bg_entrada_edificio
    with dissolve

    mc_pensamiento "Un alumno. Nivel probablemente bajo." 
    
    mc_pensamiento "Priorizar las materias con más peso para el examen."

    mc_pensamiento "Tres meses para estabilizar hábitos. Seis para ver resultados reales."

    mc_pensamiento "Nada que no haya resuelto antes en papel."

    narrador "Es curioso lo tranquilo que uno puede estar cuando no sabe a lo que se enfrenta."

    mc_pensamiento "Piso alto. Puerta doble de madera fina. El tipo de lugar que impone silencio solo con verlo."

    play sound sfx_toque_puerta volume 1.5
    mc_pensamiento "Toqué la puerta cuidadosamente y, tras unos segundos, escuché una voz desde dentro."

    voz "—¡Adelante! Puedes pasar."

    ## Silencio antes de abrir la puerta. Dos segundos de nada hacen que la
    ## revelacion entre con mas peso.
    stop music fadeout 2.0

    scene cg_manija_edificio
    with dissolve

    mc_pensamiento "(Muy bien... empecemos)."

    mc_pensamiento "Cero distracciones. Presentación formal, evaluación rápida y fijar el horario. Diez minutos máximo."

    play sound sfx_manija volume 1.5

    narrador "Apenas puse la mano sobre el pomo, la puerta se abrió desde el otro lado..."


    ############################################################################
    ##  ESCENA 5 · La revelación
    ############################################################################

    play sound sfx_puerta_abre volume 1.5

    scene cg_ichika_puerta
    with dissolve

    play music extraneza fadein 2.0

    narrador "Apareció una chica de sonrisa fácil, sosteniendo la perilla como si llevara un buen rato esperando al otro lado."

    ## --- Ichika ---------------------------------------------------------------

    ichika "¡Ah! Tú debes ser el nuevo tutor. Pasa, pasa."

    mc "[mc]. Vengo por el empleo."

    ichika "Ichika. La mayor... aunque entre nosotras eso no sirva de mucho."

    mc_pensamiento "¿La mayor?"

    ichika "Una disculpa por adelantado por el desorden. Y por el ruido."
    
    ichika "Bueno, mejor dicho, por todo lo que vas a ver en los próximos minutos."

    mc "Esa clase de advertencias suelen ser de todo menos tranquilizadoras."

    ichika "Tranquilo, entra, no mordemos... bueno, al menos la mayoría de nosotras no."

    narrador "Entré. El pasillo era más largo de lo que esperaba."

    narrador "Y no estaba desierto."

    ## --- Nino ---------------------------------------------------------------

    scene cg_nino_pasillo
    with dissolve

    nino "Ichika. ¿A quién diablos le abriste la puerta?"

    ichika "Al tutor, Nino. Ya te lo había avisado hoy en la mañana."

    nino "Y yo te dije que era una pérdida de tiempo."

    narrador "Solo entonces desvió su mirada hacia mí, evaluándome de pies a cabeza con desdén."

    nino "No vas a durar ni una semana."

    mc "Tampoco es que me hayas dado la oportunidad de presentarme..."
    
    mc "Nino, ¿cierto?"

    nino "A ti no te importa cómo me llamo. Vete."

    mc "¿Cuántos tutores han pasado antes que yo?"

    nino "Los suficientes como para saber cómo termina esto."

    scene bg_departamento
    with dissolve

    mc_pensamiento "Gemelas, entonces. Bien... eso explica el sueldo ridículamente alto."

    mc_pensamiento "...O tal vez no."

    ## --- Miku ---------------------------------------------------------------

    scene cg_miku_sofa
    with dissolve

    narrador "En el sofá, una tercera chica —la misma cara, otra vez— leía con los audífonos colgando del cuello."

    mc_pensamiento "Tres. Son tres."

    mc_pensamiento "Si esto sigue así, voy a empezar a pensar que tengo un problema en la vista..."
    
    mc_pensamiento "...o que mi padre me metió en un psiquiátrico."

    narrador "Me acerqué un poco, intentando averiguar con quién diablos se supone que debía hablar."

    mc "¿Tú también eres...?"

    narrador "Levantó la vista antes de que terminara la pregunta."
    
    narrador "No con molestia: con la cautela de quien preferiría no haber sido vista."

    narrador "Cerró el libro contra el pecho, como si lo hubiera atrapado leyendo algo que no debía."

    miku "…Miku."

    narrador "Nada más. Volvió a bajar la mirada, aunque el libro siguió cerrado un rato largo."

    narrador "Alcancé a leer el título antes de que lo apartara de su vista." 
    
    narrador "Trataba sobre estrategas del período Sengoku."

    mc "¿Sengoku? Eso son samuráis y duelos, ¿no?"

    miku "…No. Es logística."

    narrador "Lo dijo sin levantar la vista, pero sin pensarlo, como si la respuesta llevara horas esperando su turno."

    miku "Las batallas las gana quien mueve el arroz. No quien mueve la espada."

    narrador "Entonces pareció darse cuenta de que había hablado, y el libro volvió a subirle hasta media cara."

    mc_pensamiento "Nadie lee eso por obligación escolar."

    mc_pensamiento "Esto es cada vez más extraño."

    scene bg_departamento
    with dissolve

    show ichika neutral at pj(0.5)
    with dissolve

    ichika "No te lo tomes como algo personal. Tarda en soltarse."

    show ichika at pj(0.25)
    with mover

    show nino neutral at pj(0.75)
    with dissolve

    show nino at pj_habla(0.75)
    show ichika at pj_calla(0.25)

    nino "Tarda en soltarse con gente que vale la pena." 
    
    nino "Contigo probablemente tarde años."

    show nino at pj_calla(0.75)

    mc "Mi trabajo es ser su tutor, no formar amistades bonitas con ustedes."

    show nino at pj_habla(0.75)
    show ichika at pj_calla(0.25)

    nino "El último duró cuatro días. También entró diciendo que venía a trabajar."

    narrador "No se me ocurrió nada que contestar que no fuera exactamente lo que ya había dicho."

    show ichika at pj_habla(0.25)
    show nino at pj_calla(0.75)

    ichika "Vaya, qué frío."
    
    ichika "Y yo que pensaba que los chicos como tu apreciaban estar con chicas bonitas como nosotras."

    show nino at pj_habla(0.75)

    nino "Déjalo. Lo único que le interesa ha de ser los libros para nerds."

    ## --- Yotsuba -------------------------------------------------------------

    play sound sfx_correr volume 1.75

    narrador "Algo me pasó por al lado a toda velocidad antes de que pudiera reaccionar."

    yotsuba "¡¿Ya llegó?! ¡¿Ya llegó el tutor?!"

    scene cg_yotsuba_corriendo
    with dissolve

    narrador "Se frenó a medio metro de mí."
    
    narrador "Con un listón verde en el pelo y una sonrisa que ocupaba media habitación."

    yotsuba "¡Hola! ¡Soy Yotsuba!"
    
    yotsuba "¡Bienvenido! ¡Vas a hacerlo genial!"

    yotsuba "…¿Verdad?"

    narrador "La pregunta le salió medio tono más baja que todo lo anterior."

    yotsuba "¡Digo, claro que sí! ¡Obviamente!"

    mc "Emmm... Gracias supongo..."
    
    mc "Aunque ni siquiera he empezado."

    yotsuba "¡No importa! ¡Yo confío en ti al cien por ciento!"

    mc "…Pero si ni siquiera me conoces."

    yotsuba "¡Pues te conoceré a partir de hoy!" 
    
    yotsuba "¡Vamos a llevarnos súper bien!"

    nino "Yotsuba, no le des falsas esperanzas."

    yotsuba "¡Alguien tiene que dárselas!"

    scene bg_departamento
    with dissolve

    mc_pensamiento "Cuatro."

    mc "Cuatro chicas con exactamente la misma cara."

    show nino neutral at pj(0.5)
    with dissolve

    nino "¿Y eso te parece raro?"

    mc "¿Cuatro chicas con la misma cara? Un poco, sí."

    ## --- Itsuki ---------------------------------------------------------------

    show nino at pj_calla(0.5)
    
    play sound sfx_portazo volume 2.5
  
    narrador "Antes de que pudiera terminar la palabra, la puerta al fondo del pasillo se abrió de golpe."

    itsuki_inicio "Ya volví. Compré el pan que faltaba y—"

    play music caos fadeout 0.5 fadein 1.0

    scene cg_itsuki_discusion
    with dissolve

    ## Compite con `caos`, que va a tope en esta escena.
    $ duck()
    play sound sfx_bolsa volume 2.5

    narrador "Se detuvo en seco a mitad del pasillo, congelada con la bolsa del supermercado en la mano."

    mc_pensamiento "Fue ahí cuando la reconocí."

    itsuki_inicio "…¿Tú?"

    mc "…Tú."

    itsuki_inicio "¿Qué demonios haces en mi casa?"

    mc "Podría preguntarte exactamente lo mismo."

    itsuki_inicio "¡Es obvio! ¡Yo vivo aquí!"

    mc "…Ah. Claro."

    mc_pensamiento "De entre todos los departamentos de la ciudad, tenía que ser el suyo."
    
    itsuki_inicio "¿Me estuviste siguiendo desde la escuela? ¿Eres un acosador?"

    mc "Ni que tuviera tiempo libre para malgastarlo contigo."

    itsuki_inicio "¡Entonces explica qué haces parado en la entrada como si fueras el dueño!"

    mc "Vine a trabajar." 

    mc "Aunque ahora mismo siento que me están pagando poco para lo que voy a tener que aguantar."

    itsuki_inicio "¡¿Qué dijiste?!"

    mc "Lo que escuchaste."

    mc "Y baja la voz. Ni siquiera sé tu nombre para discutir contigo en condiciones."

    itsuki "¡Me llamo Itsuki, para tu información!"

    itsuki "¡Y prefiero reprobar todos los exámenes del año antes que recibir una sola clase tuya!"

    mc_pensamiento "Itsuki..."

    mc_pensamiento "Vaya..."
    
    mc_pensamiento "Llevamos discutiendo desde la mañana y apenas me entero de cómo se llama."

    mc_pensamiento "Sentí un golpe de culpa... aunque ni loco se lo admitiría en la cara."

    scene bg_departamento
    with dissolve

    show ichika sonriendo at pj(0.5)
    with dissolve

    ichika "Vaya, vaya… Veo que no necesitan presentación."

    show ichika at pj(0.30)
    with mover

    show itsuki molesta at pj(0.70)
    with dissolve

    show ichika at pj_calla(0.30)
    show itsuki at pj_habla(0.70)
    
    itsuki "¡Ichika, no te le acerques! Es el idiota del asiento de la escuela."

    show itsuki at pj_calla(0.70)

    mc "Si es por lo del almuerzo, dije lo que pensaba. No voy a fingir que no."

    show itsuki at pj_habla(0.70)

    itsuki "¡Te pedí un favor amablemente y me trataste como al ser más despreciable del mundo!"

    show ichika neutral at pj_habla(0.30)
    show itsuki at pj_calla(0.70)
    with dissolve

    ichika "¿Así que [mc] fue el que te rechazó la propuesta de estudiar juntos?"

    show ichika at pj_calla(0.20)
    show itsuki at pj_calla(0.80)
    with mover

    show yotsuba sonriendo at pj(0.50)
    with dissolve

    show yotsuba at pj_habla(0.50)

    yotsuba "¡O sea que ya se conocían! ¡Qué coincidencia tan increíble!"

    yotsuba "¡Eso significa que ya tenemos la mitad del camino completado!"

    show ichika at pj_calla(X_ICHIKA)
    show yotsuba at pj_calla(X_YOTSUBA)
    show itsuki at pj_calla(X_ITSUKI)
    with mover

    show nino neutral at pj(X_NINO)
    with dissolve

    show nino at pj_habla(X_NINO)

    nino "Por favor, Yotsuba. ¿No ves que se están matando con la mirada?"

    nino "Como si no fuera suficiente tener a un desconocido metido en la casa..."

    nino "Resulta que es el sujeto con el que se peleó en la mañana."

    show miku neutral at pj(X_MIKU)
    with dissolve

    show nino at pj_calla(X_NINO)
    show miku at pj_habla(X_MIKU)

    miku "…Demasiado ruido."

    miku "…Avisen cuando terminen de gritar."

    show ichika at pj_habla(X_ICHIKA)
    show nino at pj_habla(X_NINO)
    show miku at pj_habla(X_MIKU)
    show yotsuba at pj_habla(X_YOTSUBA)
    show itsuki at pj_habla(X_ITSUKI)

    narrador "Cinco."

    narrador "Eran cinco. Cinco rostros idénticos mirándome al mismo tiempo."

    mc "¿Cinco? Pero entonces ustedes son…"

    show ichika at pj_calla(X_ICHIKA)
    show miku at pj_calla(X_MIKU)
    show yotsuba at pj_calla(X_YOTSUBA)
    show itsuki at pj_calla(X_ITSUKI)

    nino "Quintillizas. Búscalo en un diccionario."

    narrador "Y yo de pie con la mochila colgando y la sensación exacta de haber firmado algo sin leerlo."

    mc_pensamiento "Cinco veces la tarifa normal."

    mc_pensamiento "Ahora entiendo por qué la paga era tan ridículamente alta."

    mc_pensamiento "Y entiendo por qué mi padre sonreía."

    ############################################################################
    ##  ESCENA 6 · El contrato
    ############################################################################

    narrador "No alcanzamos a cruzar otra palabra."
    
    stop music fadeout 0.3

    play sound sfx_puerta_abre volume 1.0

    narrador "Cuando la figura de su padre apareció en el umbral."

    scene cg_maruo_reunion
    with dissolve

    play music contrato fadein 2.0

    narrador "Un hombre serio, de pocas palabras y que no perdió el tiempo en saludos."

    maruo "Seré directo, [mc]. Las calificaciones de mis hijas son un desastre."
    
    maruo "Todas están al borde de reprobar."

    maruo "No te contraté solo para dar clases normales."
    
    maruo "Te contraté porque tu único objetivo es asegurar que aprueben y se gradúen."

    mc_pensamiento "Por como están las cosas, dudo que estas niñas de la noche a la mañana cambien..."

    mc "¿Qué pasa si no lo consigo?"

    maruo "Entonces no hay trabajo, no hay pago y fin de la historia."

    narrador "Lo dijo con total frialdad. Sin amenazar, simplemente dejando las cosas claras."

    maruo "Han pasado tutores antes. Ninguno duró más de una semana."

    mc "¿Y qué le hace pensar que yo sí?"

    maruo "Tienes notas perfectas y tu padre me prometió que te tomarías esto en serio."

    mc_pensamiento "Mi papá confía en mi..."
    
    mc_pensamiento "Me toca aguantarme. Sea como sea. ¡Por mi papá y Raiha!"

    scene bg_departamento
    show ichika neutral at pj_habla(X_ICHIKA)
    show nino neutral at pj_habla(X_NINO)
    show miku neutral at pj_habla(X_MIKU)
    show yotsuba sonriendo at pj_habla(X_YOTSUBA)
    show itsuki molesta at pj_habla(X_ITSUKI)
    with dissolve

    quintillizas "¡No pensamos estudiar!"

    narrador "Las cinco gritaron al mismo tiempo desde la entrada de la sala."

    scene cg_maruo_reunion
    with dissolve

    maruo "Ese es exactamente el problema que te estoy pagando por resolver."

    mc "Aun así, poner de acuerdo a las cinco no va a ser nada fácil."

    maruo "No me interesan las dificultades, [mc]. Solo los resultados."

    maruo "Tienen exámenes pronto."
    
    maruo "Si una sola de ellas reprueba, estás despedido en ese mismo instante."

    stop music fadeout 1.5

    mc "…Entendido."

    scene bg_departamento
    with dissolve

    play sound sfx_puerta_cierra volume 1.0

    narrador "Se dio la vuelta y se fue, cerrando la puerta con la calma de quien ya dio una orden y no acepta réplicas."

    ############################################################################
    ##  ESCENA 7 · El primer intento
    ############################################################################

    narrador "El 'click' de la cerradura retumbó en toda la casa."

    mc_pensamiento "Quedamos a solas." 
    
    narrador "Cinco pares de ojos se clavaron en mí con distintos niveles de desprecio y desinterés."

    mc_pensamiento "Da igual la actitud que tengan. Estoy aquí por el dinero."

    narrador "Caminé hasta la mesa del centro, solté la mochila y saqué mi material sin pedir permiso."

    narrador "Coloqué cinco cuadernos sobre la mesa."
    
    narrador "Cinco lápices."
    
    play sound sfx_hoja volume 2.0

    narrador "Una hoja con un diagnóstico rápido de veinte preguntas."

    play music derrota fadein 2.5

    scene cg_hermanas_estudiando
    with dissolve

    mc "Bien. Vamos a empezar por lo básico."
    
    mc "Necesito saber qué tanto saben... o qué tanto no saben."

    ichika "Aww... ¿De verdad tenemos que hacer esto ahora?"

    ichika "Tengo una audición mañana y apenas pude dormir tres horas."

    mc "Tu audición es mañana. La hoja es para hoy."

    narrador "Ichika soltó una sonrisa perezosa y recostó la cabeza en el respaldo del sillón, cerrando los ojos al instante."

    narrador "Miku intentó responder, pero se rindió rápidamente."
    
    narrador "Se subió los audífonos, miró perdidamente y me borró del mapa por completo."

    mc_pensamiento "Dos fuera en menos de diez segundos. Excelente récord."

    yotsuba "¡Listo! ¡Terminé la primera parte!"

    narrador "Yotsuba escribió su nombre en la hoja con un entusiasmo desmedido." 
    
    narrador "Solo su nombre..."

    mc "Escribiste tu nombre. Eso es un uno por ciento de la hoja."

    yotsuba "¡Pero un uno por ciento bien hecho! ¡Poco a poco se llega lejos!"

    narrador "Itsuki, por su parte, era la única que de verdad estaba intentando responder..." 
    
    narrador "Aunque llevaba tres minutos atascada en el mismo problema."

    itsuki "Ni se te ocurra decirme la respuesta. Puedo resolverlo sola."

    mc "Tranquila, no tenía ninguna intención de ayudarte."

    itsuki "Perfecto. Sigue así."

    narrador "Y Nino ni siquiera tocó la hoja sobre la mesa."
    
    narrador "Se quedó mirándome con los brazos cruzados."

    nino "Yo no voy a hacer esa basura."

    mc "Te digo que es una prueba de diagnóstico. No un examen de Harvard."

    nino "Y yo te estoy diciendo que me da igual lo que sea." 
    
    nino "No pienso gastar un solo segundo en esto."

    nino "Un extraño dándome órdenes en mi propia casa... eso sí que no lo pienso tolerar."

    stop music fadeout 2.0

    play sound sfx_puerta_cierra volume 2.0

    narrador "Agarró su hoja sin tocar el lápiz y se retiró a su habitación, cerrando la puerta con fuerza."

    narrador "Su salida fue solo el detonante de un fracaso que ya se veía venir."

    scene bg_departamento
    with dissolve

    narrador "Ichika se puso de pie bostezando, alegando que el estrés le arruinaría la piel para su audición de mañana."

    play sound sfx_puerta_cierra volume 1.2

    narrador "Miku ni se molestó en dar explicaciones."
    
    narrador "Simplemente se ajustó los audífonos y se marchó a su habitación en completo silencio."

    play sound sfx_puerta_cierra volume 1.2

    narrador "Y Yotsuba, aplastada por la culpa de ver a las demás irse."
    
    narrador "Me pidió perdón unas diez veces haciendo reverencias antes de salir huyendo a su cuarto prometiendo 'estudiar el doble mañana'."

    play sound sfx_puerta_cierra volume 1.2

    narrador "En menos de diez minutos, la mesa quedó vacía."

    narrador "Bueno, casi vacía."

    narrador "Solo quedó Itsuki, que se levantó lentamente y decidió dirigirme la palabra."

    show itsuki neutral at pj(0.5)
    with dissolve

    itsuki "…Esto no va a funcionar, ¿sabes?"

    mc "Te seré sincero: me quedó bastante claro desde los dos primeros minutos."

    itsuki "Y aun así vas a volver mañana."

    mc "Sí, voy a volver mañana."

    itsuki "¿Por qué aún no te rindes?"

    ## Menú de sabor.
    menu:
        "¿Qué le respondes?"

        "Porque me pagan.":
            mc "Porque me pagan."
            show itsuki molesta at pj(0.5)
            with dissolve
            itsuki "Qué actitud tan desagradable."
            mc "Es la verdad."
            itsuki "…Al menos eres honesto, por horrible que suene."

        "Porque no sé perder.":
            mc "Porque nunca he dejado un problema sin resolver."
            show itsuki molesta at pj(0.5)
            with dissolve
            itsuki "Mis hermanas y yo no somos un problema de matemáticas."
            mc "Todavía no sé lo que son."

        "No responder.":
            narrador "No dije nada. Recogí los cuadernos uno por uno."
            itsuki "…Entendido. Haz lo que quieras."
            narrador "No sé qué fue lo que interpretó, pero no volvió a insistir."

    ## Silencio hasta que decida seguir adelante. "Despedido." cae en seco.
    stop music fadeout 2.0

    scene bg_negro
    with fade

    narrador "Salí del edificio pasadas las nueve. La ciudad estaba fría y el trayecto a casa era largo."

    scene bg_cuarto_mc
    with fade

    mc_pensamiento "Cinco alumnas. Cero interés."

    mc_pensamiento "Ninguna de ellas quiere esto. Ninguna me quiere ahí."

    mc_pensamiento "Y hay una palabra rondándome la cabeza desde que crucé esa puerta:"

    mc_pensamiento "Despedido."

    narrador "Debería haberme sentido derrotado. Lo raro es que no lo estaba."

    ## Vuelve el tema de casa: la musica regresa cuando el decide no rendirse.
    play music hogar fadein 1.0 volume 0.7

    mc_pensamiento "Bien. Que sea difícil."

    mc_pensamiento "A mí nunca me han regalado nada."

    narrador "Abrí mi libreta, anoté los cinco nombres y tracé una línea debajo."
    
    narrador "Mañana empezaría la verdadera batalla."

    narrador "Apagué la lámpara del escritorio y me acosté."

    scene bg_negro
    with fade

    narrador "Así empezó todo."

    narrador "Y no, no tenía ni la más remota idea de en qué me estaba metiendo."

    ############################################################################
    ##  SALIDA AL CAPÍTULO 1
    ############################################################################

    stop music fadeout 3.0

    jump cap1_apertura
