################################################################################
##  CG PROPIOS DE LA APERTURA
##  Ilustraciones de momentos concretos de estas cuatro escenas. Los tres que
##  la apertura del capitulo 1 reutiliza —cg_calificacion, cg_maruo_reunion y
##  cg_hermanas_estudiando— estan en 00_definiciones.rpy.
################################################################################

image cg_itsuki_apertura     = "cg/cap1_apertura/itsuki_apertura.webp"

image cg_cinco_sentadas      = "cg/cap1_apertura/cinco_sentadas.webp"

image cg_libreta             = "cg/cap1_apertura/libreta.webp"

################################################################################
##  APERTURA DEL CAPITULO 1
################################################################################

label cap1_apertura:

    ############################################################################
    ##  ESCENA 1 · Instituto, mañana.
    ##  Reencuentro de Itsuki y mc, esta vez el mc decidio cambiar
    ############################################################################

    scene bg_escuela 
    with fade

    play sound sfx_timbre volume 2.5

    mc_pensamiento "Dormí cuatro horas. No por estudiar, por primera vez en meses."

    mc_pensamiento "Me quedé mirando el techo repasando la escena entera."

    mc_pensamiento "Cinco caras idénticas y cinco formas distintas de decirme que sobro."

    mc_pensamiento "Y una palabra que no se me despegó en toda la noche."

    mc_pensamiento "Despedido."

    play music cotidiano fadein 3.0

    narrador "Llegué al instituto antes que casi nadie, como siempre. Esta vez no fue por costumbre."

    mc_pensamiento "Era el único sitio donde todavía sabía exactamente lo que estaba haciendo."

    scene bg_aula
    with fade

    narrador "Mi asiento estaba libre."

    scene cg_itsuki_apertura
    with fade

    mc_pensamiento "Libre, y con el pupitre de al lado ocupado."

    narrador "Itsuki tenía la mirada clavada en su cuaderno."
    
    narrador "Con una concentración que no le hacía falta a las siete y media de la mañana."

    mc_pensamiento "Me dejó el sitio a propósito." 
    
    mc_pensamiento "Eso también era un mensaje."

    scene bg_aula
    with fade

    play music incomodo fadeout 1.0 fadein 1.5

    show itsuki neutral at pj(0.5) 
    with dissolve

    mc "Buenos días."

    show itsuki molesta at pj(0.5)
    with dissolve

    itsuki "…"

    mc "Voy a ir esta tarde."

    itsuki "Ya sé que vas a ir." 
    
    itsuki "Tienes el mismo horario que yo desde ayer."

    mc "Solo lo estoy avisando."

    itsuki "Avisa lo que quieras. Yo no pienso estudiar contigo."

    mc_pensamiento "(...)"

    ## Menú de sabor.
    menu:

        "¿Cómo te tomas su respuesta?"

        "Con la misma frialdad.":

            mc_pensamiento "¡Bien!"
            
            mc_pensamiento "Si quiere jugar a las distancias, a mí me sobra paciencia para eso."

            mc_pensamiento "No es que necesite su compañía para nada."

        "Con algo de curiosidad.":

            mc_pensamiento "Es raro." 
            
            mc_pensamiento "Ayer gritaba que me odiaba y hoy ni siquiera se molesta en mirarme."

            mc_pensamiento "Como si ya hubiera decidido que no valgo ni para enojarse."

        "Con cierto alivio.":

            mc_pensamiento "Mejor así, la verdad." 
            
            mc_pensamiento "Menos ruido, menos discusiones."

            mc_pensamiento "(Aunque el silencio, viniendo de ella, se siente casi más pesado que los gritos.)"


    scene cg_itsuki_apertura
    with fade

    narrador "Volvió a su cuaderno con un gesto seco y no dijo una palabra más en toda la mañana."

    mc_pensamiento "Ahí estaba lo verdaderamente incómodo del asunto."

    mc_pensamiento "No era que me odiara."

    mc_pensamiento "Era que iba a odiarme desde las ocho hasta las tres, " 
    
    mc_pensamiento " y después iba a seguir odiándome desde las cuatro hasta que yo me fuera de su casa."

    mc_pensamiento "Sin pausa. Sin cambio de escenario."

    mc_pensamiento "Jornada completa."

    ############################################################################
    ##  ESCENA 2 · El segundo intento
    ##  Segundo encuentro entre mc y las quintillizas en el departamente
    ##  esta vez mc piensa que habrá un cambio en ellas
    ############################################################################

    stop music fadeout 1.5
    
    scene bg_edificio
    with fade
    
    scene bg_departamento
    with fade 
    
    play sound sfx_puerta_abre 

    narrador "Toqué a las cuatro en punto."

    narrador "Me abrió Ichika, otra vez, con la misma sonrisa de la primera vez."

    mc_pensamiento "Esta vez venía preparado."

    mc_pensamiento "Cinco cuadernos, un temario dividido por materias y ninguna expectativa."

    mc_pensamiento "Lo que no esperaba era lo que encontré al entrar."

    show cg_cinco_sentadas 
    with fade

    play music extraneza fadein 2.0

    narrador "Las cinco estaban sentadas alrededor de la mesa."

    narrador "Rectas. En silencio. Con los cuadernos abiertos."

    mc_pensamiento "…"

    mc_pensamiento "Esto está mal."

    yotsuba "¡Buenas tardes, profesor!"

    mc "No soy profesor."

    ichika "Hoy sí. Hoy vamos a portarnos bien."

    mc_pensamiento "Ayer tuve que arrastrarlas una por una para que se sentaran."
    
    mc_pensamiento "Hoy me estaban esperando."

    mc_pensamiento "Nadie cambia tanto en veinticuatro horas. Nadie."

    nino "¿Vas a quedarte parado o vas a dar la clase?"

    mc "Depende. ¿Qué es esto?"

    nino "Colaboración."

    mc "Ayer me dijiste que no ibas a gastar un solo segundo en esto."

    nino "Y hoy cambié de opinión."
    
    nino "¿Algún problema?"

    narrador "Lo dijo sin apartar la mirada. Ninguna de las otras cuatro se movió."

    mc_pensamiento "Ninguna de ellas está aquí porque quiera estar."

    mc_pensamiento "Están aquí porque Nino les dijo que se sentaran."

    mc_pensamiento "¡Bien!" 
    
    mc_pensamiento "Si quieren jugar a esto, juguemos."

    mc "Página doce. Empezamos por lo más simple del temario."

    narrador "Repartí el ejercicio."
    
    narrador "Cinco copias idénticas, seis preguntas cada una, nivel de primer curso."

    mc "Les tomará unos diez minutos."

    narrador "No hizo falta esperar los diez minutos."

    narrador "En solo cuatro minutos ya me habían devuelto las cinco hojas resueltas sobre la mesa."

    mc_pensamiento "Eso también estaba mal."

    $ duck()
    play sound sfx_hoja

    narrador "Corregí la primera hoja. Seis de seis mal."

    narrador "Corregí la segunda hoja. Seis de seis mal."

    mc_pensamiento "…"

    narrador "Las cinco hojas tenían exactamente las mismas seis respuestas equivocadas." 
    
    narrador "Palabra por palabra."

    mc_pensamiento "No es que no supieran hacerlo."

    mc_pensamiento "Es que se pusieron de acuerdo en cómo hacerlo mal."

    play music caos fadeout 0.5 fadein 1.0

    scene bg_departamento
    with fade

    mc "Nino."

    show nino neutral at pj_habla(0.5)
    with dissolve

    nino "¿Sí?"

    mc "Coordinar cinco respuestas idénticas cuesta más trabajo que responder bien."

    nino "Qué observación tan interesante."

    mc "Es una observación minuiciosa."
    
    mc "Si querían perder el tiempo, tenían formas más baratas."

    nino "Entonces tómalo como lo que es."

    nino "Cinco alumnas que no aprenden nada contigo, por escrito y por triplicado."

    nino "Mi padre va a leer esas hojas."

    mc_pensamiento "Ahí estaba."

    mc_pensamiento "No querían echarme a gritos. Querían mi carta de renuncia."

    mc "Vas a hacer que reprueben para que me despidan."

    nino "Voy a hacer que quede claro lo que ya era obvio ayer."

    nino "El último duró cuatro días. Tú llevas uno."

    show nino at pj(0.20)
    with mover

    show nino at pj_calla(0.20)
    show yotsuba incomoda at pj_habla(0.80)
    with dissolve
 
    yotsuba "Nino, eso no es justo. Él solo está—"

    show nino neutral at pj_habla(0.20)
    show yotsuba at pj_calla(0.80)
    with dissolve

    nino "Yotsuba."

    show nino neutral at pj_calla(0.20)
    show yotsuba at pj_habla(0.80)
    with dissolve
   
    yotsuba "…No dije nada."

    show yotsuba at pj_calla(0.80)
    with dissolve

    mc_pensamiento "Iba a defenderme. Y se arrepintió a mitad de frase."

    narrador" Se encogió en el sitio y se puso a alinear los bordes de su hoja con las dos manos, 
    muy despacio, como si eso fuera una tarea."

    mc_pensamiento "Yotsuba no está de acuerdo con Nino."

    mc_pensamiento "Pero está obedeciendola, que no es lo mismo."

    show ichika sonriendo at pj_habla(0.50)
    show nino at pj_calla(0.20)
    with dissolve 

    ichika "Bueno, tampoco hay que dramatizar."

    ichika "Contestamos las seis. Nadie dijo que hubiera que acertarlas."

    mc "Contestaron las seis igual de mal."

    ichika "¿Coincidencia?."
    
    ichika "Somos hermanas, pensamos parecido."

    mc_pensamiento "Mentía tan bien que casi daba gusto."

    scene cg_hermanas_estudiando
    with dissolve

    narrador "Para cuando volví a levantar la vista, Ichika ya tenía los ojos cerrados y la cabeza apoyada en el respaldo."

    mc_pensamiento "Y ahí se cayó la función."

    narrador "Miku no había levantado la vista de la mesa en todo el rato."
    
    narrador "Tenía los auriculares puestos y, esta vez, sonando."

    narrador "Itsuki estaba con los brazos tensos y la cara torcida hacia la ventana."

    mc_pensamiento "No participó en el plan, pero tampoco pensaba ayudarme."

    narrador "Junté las cinco hojas y las dejé en una pila."

    mc "Última pregunta y me voy. La pregunta siete no está en la hoja."

    mc "Veamos que tal les va en inglés"

    narrador "Empezé a leerles una oración"

    mc "«He didn't want to go, but he had to.»"

    narrador" Lo leí a propósito, con el peor acento que pude."

    scene bg_departamento
    with fade
    
    show nino neutral at pj_habla(0.5)
    with dissolve

    nino "Had to. No «jad tu». Se pega, no se separa."

    narrador "Se quedó en silencio."

    show nino pillada at pj(0.5)
    with dissolve

    nino "…"

    mc "Gracias."

    nino "¡No te he corregido a ti! ¡Es que dolía escucharlo!"

    mc "Claro."

    nino "¡Se acabó! ¡Fuera de mi casa!"

    $ duck()
    play sound sfx_puerta_cierra volume 2.0
    
    stop music fadeout 2.0

    hide nino
    with moveoutleft

    narrador "Se levantó y se encerró de un portazo, igual que el día anterior, 
    solo que esta vez se llevó su cuaderno con ella."

    narrador "Las otras tres tardaron menos de un minuto en desaparecer detrás de ella."

    narrador "Miku fue la última."

    narrador "Se detuvo a mitad del pasillo, de espaldas, con el libro apretado contra el pecho."

    show miku neutral at pj(0.5)
    with dissolve

    miku "…No fue idea mía."

    narrador "Lo dijo tan bajo que tuve que reconstruirlo un segundo después, cuando ya no estaba."

    narrador "Porque en cuanto lo dijo, se dio cuenta de que lo había dicho."

    miku "…Olvídalo. Perdón."

    hide miku  
    with moveoutleft

    mc_pensamiento "Es la segunda vez que habla sin querer y la segunda vez que pide perdón por haberlo hecho."

    mc_pensamiento "Nadie se disculpa por decir algo cierto, a menos que le hayan enseñado que decirlo cuesta."

    mc_pensamiento "Segundo día. Segundo fracaso."

    mc_pensamiento "Pero por primera vez me llevaba algo a casa."

    ############################################################################
    ##  ESCENA 3 · El plazo
    ############################################################################
    
    play sound sfx_puerta_abre volume 1.0

    narrador "Estaba recogiendo mis cosas cuando la puerta del fondo se abrió."

    show cg_maruo_reunion
    with fade
    
    play music contrato fadein 2.0

    maruo "Vi las hojas."

    mc_pensamiento "Rápido. Muy rápido."

    maruo "Seis errores idénticos por cinco." 
    
    maruo "Supongo que no hace falta que te explique lo que significa."

    mc "Si, no hace falta."

    maruo "¿Y bien?"

    mc "Significa que son capaces de coordinar cinco respuestas iguales en cuatro minutos."

    mc "Eso no lo hace alguien que no entiende el ejercicio."

    narrador "Me miró un momento más largo de lo que me había mirado el día anterior."

    maruo "Los exámenes son en un mes."

    maruo "Cinco asignaturas. Las cinco tienen que aprobarlas todas."

    mc "¿Y si una sola reprueba?"

    maruo "Ya te lo dije ayer y no lo voy a repetir dos veces."

    $ duck()
    play sound sfx_puerta_cierra volume 1.0

    narrador "Se fue como se había ido el día anterior, sin subir la voz y sin dejar espacio para contestar."

    mc_pensamiento "Un mes."

    mc_pensamiento "Treinta días para cinco alumnas que hoy se organizaron para reprobar."

    ############################################################################
    ##  ESCENA 4 · La cena
    ##  Raiha, Isanari y mc en el comedor hablando del segundo
    ##  día de trabajo. Incluye menú de sabor.
    ############################################################################

    stop music fadeout 2.0

    scene bg_negro
    with fade

    narrador "Salí del edificio pasadas las siete. Fui directo a casa."

    play music cena fadeout 1.5 fadein 2.0

    scene bg_comedor
    with fade

    narrador "La cena transcurrió casi en silencio, roto solo por el sonido de los cubiertos."

    show raiha hablando at pj(0.20)
    with dissolve

    raiha "Hermanito, te noto más callado que de costumbre."

    mc "Solo estoy cansado."

    show isanari neutral at pj(0.73)
    with dissolve

    isanari "¿Cansado, o el trabajo ya te está pasando factura?"

    mc "Un poco de las dos cosas."

    show isanari at pj_habla(0.73)
    show raiha regano at pj_calla(0.20)

    isanari "¿Qué tal el segundo día con esas alumnas?"

    ## Menú de sabor.
    menu:

        "¿Qué le cuentas de tu segundo día?"

        "La verdad completa: se coordinaron para hacerlo mal.":

            mc "Sinceramente... hoy fue peor que ayer."
            
            mc "Se pusieron de acuerdo para responder mal a propósito."

            show isanari at pj_calla(0.73)
            show raiha hablando at pj_habla(0.20)
            with dissolve

            raiha "¡Eso es horrible! ¿Por qué harían algo así?"

            mc "Todavía no lo sé. Pero pienso averiguarlo."

            show raiha at pj_calla(0.20)
            show isanari neutral at pj_habla(0.73)
            with dissolve

            isanari "Cinco cabezas puestas de acuerdo contra una... suena a un problema serio."

        "Suavizar la situación: 'Va bien, dentro de lo normal.'":

            mc "Va bien. Dentro de lo que cabe esperar de un segundo día."

            show isanari at pj_habla(0.73)
            with dissolve

            isanari "Ya veo. No sonaste muy convencido al decirlo."

            mc "Es solo cansancio, ya te dije."

            show raiha regano at pj_habla(0.20)
            with dissolve

            raiha "¡A mí no me engañas! ¡Se te nota en la cara que algo pasó!"

        "Cambiar de tema.":

            mc "¿Podemos hablar de otra cosa?" 
            
            mc "No quiero pensar en eso ahora mismo."

            show isanari neutral at pj_habla(0.73)
            with dissolve

            isanari "Como quieras. No voy a insistir."

            show raiha hablando at pj_habla(0.20)
            with dissolve

            raiha "¡Yo sí insisto un poquito! Pero está bien, lo dejo por hoy."


    show isanari sonriendo at pj_habla(0.73)
    show raiha at pj_calla(0.20)
    with dissolve

    isanari "Solo recuerda que un mes no es mucho tiempo, y el trato con esa familia depende de que cumplas."

    mc "Lo sé. No hace falta que me lo recuerdes."

    isanari "Tómalo como otro examen sorpresa."

    mc_pensamiento "Otra vez con esa frase..."

    mc_pensamiento "Aunque esta vez tiene más razón de la que me gustaría admitir."

    narrador "Terminada la cena, subí a mi habitación con las cinco hojas bajo el brazo."

    ############################################################################
    ##  ESCENA 5 · El cuarto de mc
    ##  Derivada de la Escena 4 original: el análisis de las hojas y la
    ##  interacción con Raiha.
    ############################################################################

    stop music fadeout 1.5

    scene bg_cuarto_mc
    with fade

    play music hogar fadein 1.5 volume 0.7

    narrador "Puse las cinco hojas sobre el escritorio y las dejé ahí un buen rato sin tocarlas."

    mc_pensamiento "Ayer pensé que el problema era que no querían estudiar."

    mc_pensamiento "Hoy sé que el problema es otro."

    mc_pensamiento "No es que no puedan. Es que se defienden."

    mc_pensamiento "Y se defienden juntas."

    $ duck()
    play sound sfx_toque_puerta volume 1.5
    
    show raiha hablando at pj(0.50)
    with dissolve

    raiha "Hermanito, llevas media hora mirando unos papeles en blanco."

    mc "No están en blanco."

    raiha "Están llenos de cosas mal hechas y tachones, que es casi peor."

    mc "Gracias por el ánimo."

    show raiha regano at pj(0.50)
    with dissolve

    raiha "¡Yo solo digo lo que veo!"

    raiha "¿Son de las chicas a las que les das clase?"

    mc "Sí."

    raiha "¿Y son tontas?"

    mc "No."

    narrador "Contesté antes de pensarlo, y me di cuenta de que lo decía en serio."

    mc "No, no lo son."

    raiha "Entonces no entiendo el problema."

    raiha "Bueno da igual, te deseo mucha suerte hermanito."

    raiha "¡Se que podrás lidiar con cinco a la vez!"

    ############################################################################
    ##  ESCENA 6 · El mapa de las cinco
    ##  Nueva escena, también derivada de la Escena 4 original: Raiha ayuda a
    ##  mc a adivinar dónde podría estar cada quintilliza según lo que él ya
    ##  sabe de ellas. Menú de sabor con las 5 hermanas: no continúa hasta
    ##  que las cinco han sido escuchadas (control por conjunto/condicional).
    ############################################################################

    mc_pensamiento "Cinco a la vez... ese es justo el problema."

    mc "Raiha, espera un segundo."

    show raiha at pj_habla(0.50)

    raiha "¿Mm? ¿Qué pasa?"

    mc "Tengo una duda algo rara."
    
    mc "Si tuvieras que adivinar dónde suele estar cada una de esas chicas despues de estudiar, "
    
    mc " ¿por dónde empezarías?"

    show raiha hablando at pj_habla(0.50)
    with dissolve

    raiha "¡Eso es fácil hermanito!" 
    
    raiha "Tú solo cuentame cómo es cada una y yo te digo dónde la buscaría."

    raiha "¡Como un juego de adivinanzas!"

    mc_pensamiento "No pierdo nada con intentarlo."

    $ hermanas_ubicadas = set()

    label cap1_adivinanza_hermanas:

        menu:

            "¿De cuál hermana le hablas primero?"

            "Ichika" if "ichika" not in hermanas_ubicadas:

                $ hermanas_ubicadas.add("ichika")

                mc "Hay una que se llama {color=#FFB7C5}{b}Ichika{/b}{/color}."

                mc "Es la primera hermana o hermana mayor de las cinco."
                
                mc "Duerme en cualquier parte y dice que tiene audiciones."

                raiha "¡Ah, esa es fácil!" 
                
                raiha "Si anda con audiciones, seguro se pasa las horas ensayando en la 
                {color=#F2879B}{b}sala de ensayo{/b}{/color} del colegio."

                raiha "O simplemente durmiendo la siesta en el sofá más cercano."

                mc_pensamiento "Actuación... o pereza disfrazada de actuación." 

                mc "¡Si! Probablemente ahí hace sus audiciones."
                
                mc "Bien. Anotado."

            "Nino" if "nino" not in hermanas_ubicadas:

                $ hermanas_ubicadas.add("nino")

                mc "Hay una que se llama {color=#C39BD3}{b}Nino{/b}{/color}." 

                mc "Es la segunda hermana de las cinco."
                
                mc "Manda sobre las demás." 
                
                mc "Y es muy rigurosa con las cosas." 
                
                mc "Hasta me corrigió mi pronunciación en inglés."

                raiha "¡Uy, esa suena a hermana mayor de verdad!" 
                
                raiha "Es como yo, pero enojona."

                raiha "Con esa actitud de jefa, seguro anda revisando que no falte nada en casa...." 
                
                raiha "Capaz la encuentras en el 
                {color=#9B6FB8}{b}centro comercial{/b}{/color} ,comprando lo que las demás olvidaron."

                mc_pensamiento "Centro comercial... Tiene sentido, viniendo de ella."

                mc "Bien. Anotado."

            "Miku" if "miku" not in hermanas_ubicadas:

                $ hermanas_ubicadas.add("miku")

                mc "Hay una que se llama {color=#5DADE2}{b}Miku{/b}{/color}."

                mc "Es la tercera hermana de las cinco."

                mc "La hermana del medio."
                
                mc "Casi no habla y usa sus audífonos todo el tiempo."
                
                mc "Aunque algo que destaco de ella es que sabe demasiado de historia."

                raiha "Con lo calladita que es, seguro se esconde entre libros en la
                {color=#3D8FC7}{b}biblioteca{/b}{/color}, sin que nadie la moleste."

                raiha "Las calladas siempre tienen su rincón secreto."

                mc_pensamiento "Un rincón secreto que sería la biblioteca."
                
                mc_pensamiento "Si la encuentro ahí, al menos no tendré que gritar para que me escuche."

                mc "Bien. Anotado."

            "Yotsuba" if "yotsuba" not in hermanas_ubicadas:

                $ hermanas_ubicadas.add("yotsuba")

                mc "Hay una que se llama {color=#58D68D}{b}Yotsuba{/b}{/color}." 
                
                mc "Es la cuarta hermana de las cinco."

                mc "Rebosa de energía, es muy alegre." 
                
                mc "Corrió por el pasillo para conocerme."

                raiha "¡Esa me cae bien solo de escucharla!" 

                raiha "Con esa energía, seguro es una atleta."
                
                raiha "Puede que se la pase entrenando en alguna 
                {color=#3FAF71}{b}pista de atletismo{/b}{/color}."

                mc_pensamiento "Entrenando al aire libre, entonces." 
                
                mc_pensamiento "Si empiezo por ella, tendré que correr detrás hasta atraparla."
                
                mc_pensamiento "Es broma... o no."

                mc "Bien. Anotado."


            "Itsuki" if "itsuki" not in hermanas_ubicadas:

                $ hermanas_ubicadas.add("itsuki")

                mc "Hay una que se llama {color=#EC7063}{b}Itsuki{/b}{/color}."

                mc "Es la última hermana de las cinco. La menor."

                mc "La que se sentó en mi puesto el primer día."

                mc "Y la que más problemas me ha causado."

                show raiha regano at pj_habla(0.50)
                with dissolve

                raiha "¡Espera, espera!"

                raiha "¿Es la misma con la que discutías ese día?"

                mc "...Sí, esa misma."

                raiha "¡Con razón te veías tan raro cuando volviste ese día!"

                show raiha hablando at pj_habla(0.50)
                with dissolve

                mc "Es bastante aplicada, eso sí. Se queda repasando después de que terminan
                las clases, aunque nadie se lo pida."

                raiha "Entonces no hay mucho misterio ahí." 
                
                raiha "Seguro sigue en el {color=#D35443}{b}aula vacía{/b}{/color}, después de clases, sola con sus apuntes."

                mc_pensamiento "Sola y sin que la molesten. Como ahora mismo, seguramente."

                mc "Listo. Anotado."

        if len(hermanas_ubicadas) < 5:
            jump cap1_adivinanza_hermanas

    show raiha at pj_habla(0.50)

    raiha "¡Ya está! Cinco hermanas, cinco escondites." 
    
    raiha "¡De nada, hermanito!"

    mc "...Gracias, Raiha. Puede que esto sirva más de lo que crees."

    raiha "¡Siempre sirvo, solo que casi nunca me lo agradecen!"

    hide raiha
    with moveoutleft

    narrador "Se fue tan rápido como había entrado, muy contenta de haber resuelto algo."

    mc_pensamiento "…"

    mc_pensamiento "Repasemos."

    mc_pensamiento "Cinco respuestas idénticas en cuatro minutos."

    mc_pensamiento "Eso requiere ponerse de acuerdo antes, concordar el error y sostenerlo delante de mí sin fallar ninguna."

    mc_pensamiento "Es un trabajo en equipo mejor ejecutado que la mitad de los proyectos de mi clase."

    mc_pensamiento "Y Nino me corrigió un had to sin pensarlo, molesta, en mitad de una discusión."

    mc_pensamiento "Nadie corrige por reflejo algo que no domina."

    narrador "Volví a mirar las cinco hojas."

    narrador "En la de Miku, debajo de la respuesta equivocada, había una marca de goma mal borrada."

    mc_pensamiento "Escribió la correcta primero."

    mc_pensamiento "Y después la borró."

    mc_pensamiento "Ayer me habló de logística del período Sengoku sin que nadie se lo preguntara."

    mc_pensamiento "No son cinco alumnas malas."

    mc_pensamiento "Son cinco personas que saben una cosa cada una y que han decidido no enseñármela."

    show cg_libreta
    with fade

    narrador "Abrí la libreta por la página donde había anotado los cinco nombres la noche anterior."

    narrador "Debajo de la línea escribí una sola frase."

    mc_pensamiento "De frente y las cinco a la vez, pierdo siempre. Son un muro y yo soy uno."

    mc_pensamiento "Así que no voy a ir de frente."

    mc_pensamiento "Voy a ir de una en una."

    mc_pensamiento "Y no en su casa, donde se cubren entre ellas."

    mc_pensamiento" Donde cada una esté sola."

    narrador "Apagué la lámpara."

    scene bg_negro 
    with fade

    narrador "Treinta días."

    narrador "Se que puedo lograrlo."

    narrador "Lograr que aprueben sus examenes."

    narrador "Si, asi será."

    jump hub_1