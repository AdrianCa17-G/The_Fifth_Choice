## Guion — Apertura

**Bloque fijo. Sin decisiones. Sin puntos.**
Continúa directamente después de `jump cap1_inicio`.

Cuatro escenas: retoma la mañana siguiente, muestra el segundo intento fracasando
de una forma distinta a la del prólogo, pone fecha al examen y llega a la
conclusión que abre el mapa.

Marcadores entre corchetes. `[BG]` fondo · `[CG]` ilustración · `[SPR]` sprite ·
`[MUS]` música · `[SFX]` efecto · `[NUEVO]` asset que no existe todavía.

---

### Escena 1 · Instituto, mañana

`[BG bg_escuela]` `[SFX sfx_timbre]` `[MUS cotidiano fadein 2.5]`

**mc_pensamiento:** Dormí cuatro horas. No por estudiar, por primera vez en meses.

**mc_pensamiento:** Me quedé mirando el techo repasando la escena entera. Cinco caras idénticas y cinco formas distintas de decirme que sobro.

**mc_pensamiento:** Y una palabra que no se me despegó en toda la noche.

**mc_pensamiento:** Despedido.

**narrador:** Llegué al instituto antes que casi nadie, como siempre. Esta vez no fue por costumbre.

**mc_pensamiento:** Era el único sitio donde todavía sabía exactamente lo que estaba haciendo.

`[BG bg_aula]`

**narrador:** Mi asiento estaba libre.

`[CG NUEVO — cg_pupitre_manana: POV desde el pupitre de Futaro. Primer término inferior, su mesa y su cuaderno abierto, desenfocados y cortados por el borde. Al lado, Itsuki de tres cuartos, estudiando, sin devolver la mirada. Aula vacía al fondo, luz fría de primera hora.]`

**mc_pensamiento:** Libre, y con el pupitre de al lado ocupado.

**narrador:** Itsuki tenía la mirada clavada en su cuaderno con una concentración que no le hacía falta a las siete y media de la mañana.

**mc_pensamiento:** Me dejó el sitio a propósito. Eso también era un mensaje.

`[BG bg_aula]` `[SPR itsuki neutral at pj(0.65)]` `[MUS incomodo fadeout 1.0 fadein 1.5]`

**mc:** Buenos días.

`[SPR itsuki molesta at pj(0.65)]`

**itsuki:** …

**mc:** Voy a ir esta tarde.

**itsuki:** Ya sé que vas a ir. Vives en el mismo horario que yo desde ayer.

**mc:** Solo lo estoy avisando.

**itsuki:** Avisa lo que quieras. Yo no pienso participar.

**narrador:** Volvió a su cuaderno con un gesto seco y no dijo una palabra más en toda la mañana.

**mc_pensamiento:** Ahí estaba lo verdaderamente incómodo del asunto.

**mc_pensamiento:** No era que me odiara. Era que iba a odiarme desde las ocho hasta las tres, y después iba a seguir odiándome desde las cuatro hasta que yo me fuera de su casa.

**mc_pensamiento:** Sin pausa. Sin cambio de escenario.

**mc_pensamiento:** Jornada completa.

---

### Escena 2 · El segundo intento

`[MUS stop fadeout 1.5]`
`[BG bg_edificio]` → `[BG bg_departamento]` `[SFX sfx_puerta_abre]`

**narrador:** Toqué a las cuatro en punto. Me abrió Ichika, otra vez, con la misma sonrisa de la primera vez.

**mc_pensamiento:** Esta vez venía preparado. Cinco cuadernos, un temario dividido por materias y ninguna expectativa.

**mc_pensamiento:** Lo que no esperaba era lo que encontré al entrar.

`[CG NUEVO — cg_cinco_sentadas: las cinco a la misma mesa, sentadas, rectas, cuadernos abiertos, mirando hacia cámara. Mismo encuadre y misma luz que cg_hermanas_estudiando —esa semilla sirve de punto de partida—, pero con la actitud invertida: nadie duerme, nadie mira a otro lado, nadie disimula. Es la imagen que da miedo. Sostiene toda la primera mitad de la escena, así que tiene que aguantar en pantalla.]`

`[MUS extraneza fadein 2.0]`

**narrador:** Las cinco estaban sentadas alrededor de la mesa. Rectas. En silencio. Con los cuadernos abiertos.

**mc_pensamiento:** …

**mc_pensamiento:** Esto está mal.

**yotsuba:** ¡Buenas tardes, profesor!

**mc:** No soy profesor.

**ichika:** Hoy sí. Hoy vamos a portarnos bien.

**mc_pensamiento:** Ayer tuve que arrastrarlas una por una para que se sentaran. Hoy me estaban esperando.

**mc_pensamiento:** Nadie mejora tanto en veinticuatro horas. Nadie.

**nino:** ¿Vas a quedarte parado o vas a dar la clase?

**mc:** Depende. ¿Qué es esto?

**nino:** Colaboración.

**mc:** Ayer me dijiste que no ibas a gastar un solo segundo en esto.

**nino:** Y hoy cambié de opinión. ¿Algún problema?

**narrador:** Lo dijo sin apartar la mirada. Ninguna de las otras cuatro se movió.

**mc_pensamiento:** Ninguna de ellas está aquí porque quiera estar.

**mc_pensamiento:** Están aquí porque ella les dijo que se sentaran.

**mc_pensamiento:** Bien. Si quieren jugar a esto, juguemos.

**mc:** Página doce. Empezamos por lo más simple del temario.

**narrador:** Repartí el ejercicio. Cinco copias idénticas, seis preguntas cada una, nivel de primer curso.

**mc:** Diez minutos.

**narrador:** No hizo falta esperar diez. En cuatro ya las tenía las cinco encima de la mesa.

**mc_pensamiento:** Eso también estaba mal.

`[SFX sfx_hoja]`

**narrador:** Corregí la primera. Seis de seis mal.

**narrador:** Corregí la segunda. Seis de seis mal.

**mc_pensamiento:** …

**narrador:** Las cinco hojas tenían exactamente las mismas seis respuestas equivocadas. Palabra por palabra.

**mc_pensamiento:** No es que no supieran hacerlo.

**mc_pensamiento:** Es que se pusieron de acuerdo en cómo hacerlo mal.

`[MUS caos fadeout 0.5 fadein 1.0]`

**mc:** Nino.

**nino:** ¿Sí?

**mc:** Coordinar cinco respuestas idénticas cuesta más trabajo que responder bien.

**nino:** Qué observación tan interesante.

**mc:** Es una observación matemática. Si querían perder el tiempo, tenían formas más baratas.

**nino:** Entonces tómalo como lo que es.

**nino:** Cinco alumnas que no aprenden nada contigo, por escrito y por triplicado.

**nino:** Mi padre va a leer esas hojas.

**mc_pensamiento:** Ahí estaba.

**mc_pensamiento:** No querían echarme a gritos. Querían un informe.

**mc:** Vas a hacer que reprueben para que me despidan.

**nino:** Voy a hacer que quede claro lo que ya era obvio ayer.

**nino:** El último duró cuatro días. Tú llevas uno.

`[BG bg_departamento with dissolve]` `[SPR NUEVO — yotsuba_incomoda at pj(0.70)]`

**yotsuba:** Nino, eso no es justo. Él solo está—

**nino:** Yotsuba.

**yotsuba:** …No dije nada.

**mc_pensamiento:** Iba a defenderme. Y se arrepintió a mitad de frase.

**narrador:** Se encogió en el sitio y se puso a alinear los bordes de su hoja con las dos manos, muy despacio, como si eso fuera una tarea.

**mc_pensamiento:** Esa no está de acuerdo.

**mc_pensamiento:** Está obedeciendo, que no es lo mismo.

`[SPR ichika sonriendo at pj(0.30)]` `[SPR yotsuba at pj_calla(0.70)]`

**ichika:** Bueno, tampoco hay que dramatizar. Contestamos las seis. Nadie dijo que hubiera que acertarlas.

**mc:** Contestaron las seis igual de mal.

**ichika:** Coincidencia. Somos hermanas, pensamos parecido.

**mc_pensamiento:** Esa mentía tan bien que casi daba gusto.

`[CG cg_hermanas_estudiando]`

**narrador:** Para cuando volví a levantar la vista, Ichika ya tenía los ojos cerrados y la cabeza apoyada en el respaldo.

**mc_pensamiento:** Y ahí se cayó la función.

**narrador:** Miku no había levantado la vista de la mesa en todo el rato. Tenía los auriculares puestos y, esta vez, sonando.

**narrador:** Itsuki estaba sentada aparte, con los brazos cruzados y la cara torcida hacia la ventana.

**mc_pensamiento:** Y esa no participó del plan, pero tampoco pensaba salvarme.

**narrador:** Junté las cinco hojas y las dejé en una pila.

**mc:** Última pregunta y me voy. La siete no estaba en la hoja.

**mc:** *«He didn't want to go, but he had to.»*

**narrador:** Lo leí a propósito plano, con el peor acento que pude.

`[BG bg_departamento with dissolve]` `[SPR nino neutral at pj_habla(0.5)]`

**nino:** *Had to.* No *«jad tu»*. Se pega, no se separa.

**narrador:** Silencio.

`[SPR NUEVO — nino_sorprendida at pj(0.5)]`

**nino:** …

**mc:** Gracias.

**nino:** ¡No te he corregido a ti! ¡Es que dolía escucharlo!

**mc:** Claro.

**nino:** ¡Se acabó! ¡Fuera de mi casa!

`[SFX sfx_puerta_cierra volume 2.0]` `[MUS stop fadeout 2.0]`

**narrador:** Se levantó y se encerró de un portazo, igual que el día anterior, solo que esta vez se llevó su cuaderno con ella.

**narrador:** Las otras tres tardaron menos de un minuto en desaparecer detrás de ella.

**narrador:** Miku fue la última. Se detuvo a mitad del pasillo, de espaldas, con el libro apretado contra el pecho.

`[SPR miku aburrida at pj(0.5)]`

**miku:** …No fue idea mía.

**narrador:** Lo dijo tan bajo que tuve que reconstruirlo un segundo después, cuando ya no estaba.

**narrador:** Porque en cuanto lo dijo, se dio cuenta de que lo había dicho.

**miku:** …Olvídalo. Perdón.

`[SPR miku hide with moveoutleft]`

**mc_pensamiento:** Es la segunda vez que habla sin querer y la segunda vez que pide perdón por haberlo hecho.

**mc_pensamiento:** Nadie se disculpa por decir algo cierto, a menos que le hayan enseñado que decirlo cuesta.

**mc_pensamiento:** Segundo día. Segundo fracaso.

**mc_pensamiento:** Pero por primera vez me llevaba algo a casa.

---

### Escena 3 · El plazo

`[BG bg_departamento]` `[SFX sfx_puerta_abre volume 1.0]`

**narrador:** Estaba recogiendo cuando la puerta del fondo se abrió.

`[CG cg_maruo_reunion]` `[MUS contrato fadein 2.0]`

**maruo:** Vi las hojas.

**mc_pensamiento:** Rápido. Muy rápido.

**maruo:** Seis errores idénticos por cinco. Supongo que no hace falta que te explique lo que significa.

**mc:** No hace falta.

**maruo:** ¿Y bien?

**mc:** Significa que son capaces de coordinar cinco respuestas iguales en cuatro minutos.

**mc:** Eso no lo hace alguien que no entiende el ejercicio.

**narrador:** Maruo me miró un momento más largo de lo que me había mirado el día anterior.

**maruo:** Los exámenes trimestrales son en un mes.

**maruo:** Cinco asignaturas. Las cinco tienen que aprobarlas todas.

**mc:** ¿Y si una sola reprueba?

**maruo:** Ya te lo dije ayer y no lo voy a repetir dos veces.

`[SFX sfx_puerta_cierra volume 1.0]`

**narrador:** Se fue como se había ido el día anterior, sin subir la voz y sin dejar espacio para contestar.

**mc_pensamiento:** Un mes.

**mc_pensamiento:** Treinta días para cinco alumnas que hoy se organizaron para reprobar.

---

### Escena 4 · La conclusión

`[MUS stop fadeout 2.0]`
`[BG bg_negro with fade]`

**narrador:** Salí del edificio pasadas las siete. Esta vez no fui directo a casa.

`[BG bg_cuarto_mc]` `[MUS hogar fadein 1.5 volume 0.7]`

**narrador:** Puse las cinco hojas sobre el escritorio y las dejé ahí un buen rato sin tocarlas.

**mc_pensamiento:** Ayer pensé que el problema era que no querían estudiar.

**mc_pensamiento:** Hoy sé que el problema es otro.

**mc_pensamiento:** No es que no puedan. Es que se defienden.

**mc_pensamiento:** Y se defienden juntas.

`[SFX sfx_toque_puerta volume 1.5]` `[SPR raiha hablando at pj(0.30)]`

**raiha:** Hermanito, llevas media hora mirando unos papeles en blanco.

**mc:** No están en blanco.

**raiha:** Están llenos de cosas mal, que es casi peor.

**mc:** Gracias por el ánimo.

`[SPR raiha regano at pj(0.30)]`

**raiha:** ¡Yo solo digo lo que veo!

**raiha:** ¿Son de las chicas esas a las que les das clase?

**mc:** Sí.

**raiha:** ¿Y son tontas?

**mc:** No.

**narrador:** Contesté antes de pensarlo, y me di cuenta de que lo decía en serio.

**mc:** No, no lo son.

**raiha:** Entonces no entiendo el problema.

`[SPR raiha hide with moveoutleft]`

**narrador:** Se fue tan rápido como había entrado, muy contenta de haber resuelto algo.

**mc_pensamiento:** …

**mc_pensamiento:** Repasemos.

**mc_pensamiento:** Cinco respuestas idénticas en cuatro minutos. Eso requiere ponerse de acuerdo antes, repartirse el error y sostenerlo delante de mí sin fallar ninguna.

**mc_pensamiento:** Es un trabajo en equipo mejor ejecutado que la mitad de los proyectos de mi clase.

**mc_pensamiento:** Y Nino me corrigió un *had to* sin pensarlo, molesta, en mitad de una discusión.

**mc_pensamiento:** Nadie corrige por reflejo algo que no domina.

**narrador:** Volví a mirar las cinco hojas. En la de Miku, debajo de la respuesta equivocada, había una marca de goma mal borrada.

**mc_pensamiento:** Escribió la correcta primero.

**mc_pensamiento:** Y después la borró.

**mc_pensamiento:** Es la misma que ayer me habló de logística del período Sengoku sin que nadie se lo preguntara.

**mc_pensamiento:** No son cinco alumnas malas.

**mc_pensamiento:** Son cinco personas que saben una cosa cada una y que han decidido no enseñármela.

**narrador:** Abrí la libreta por la página donde había anotado los cinco nombres la noche anterior.

**narrador:** Debajo de la línea escribí una sola frase.

`[CG NUEVO — cg_libreta: la libreta abierta, los cinco nombres en columna y una frase debajo. Plano cenital cerrado, luz de lámpara. Texto ilegible a propósito: se lee la forma, no las palabras.]`

**mc_pensamiento:** De frente y las cinco a la vez, pierdo siempre. Son un bloque y yo soy uno.

**mc_pensamiento:** Así que no voy a ir de frente.

**mc_pensamiento:** Voy a ir de una en una.

**mc_pensamiento:** Y no en esa casa, donde se cubren entre ellas.

**mc_pensamiento:** Donde cada una esté sola.

**narrador:** Apagué la lámpara.

`[BG bg_negro with fade]`

**narrador:** Treinta días.

---

→ **Sale al hub 1.** La primera elección del jugador escribe `primera_conexion`.

---
