## 8. Evento de hermana · Miku — Biblioteca

**Escrito.** Assets pendientes. Encaja en cualquiera de los tres huecos.

Marcadores como en la apertura. `[BG]` fondo · `[CG]` ilustración · `[SPR]` sprite ·
`[MUS]` música · `[SFX]` efecto · `[NUEVO]` asset que no existe todavía ·
`[$]` línea de código.

---

### Decisiones de este evento

**No depende de nada.** No menciona la crisis de Nino, ni el beat de Itsuki, ni
los otros eventos. Todo lo que da por sabido ocurrió sí o sí: el libro de Sengoku
del prólogo y la marca de goma de la apertura. Se puede jugar primero, segundo o
tercero sin cambiar una línea.

**La biblioteca es municipal, no la del instituto.** El instituto es terreno de
Futaro; el mapa dice que a las otras cuatro hay que ir a buscarlas al suyo. Y
dice algo de ella: se va a leer lo que le gusta a un sitio donde nadie de su casa
la ve hacerlo.

**La historia se cuenta para quien no sabe nada de historia.** Ni un nombre de
batalla, ni una fecha, ni una provincia por su nombre. Solo dos personas —Shingen
y Kenshin—, y todo lo demás explicado por lo que se entiende sin estudiar: no
había refrigeradores, sin sal la comida se pudre, treinta mil hombres comen tres
veces al día. Si el jugador tiene que esforzarse para seguirla, deja de escuchar
a Miku y se pone a descifrar un temario, que es justo lo contrario de lo que hace
esta escena. El objetivo no es que aprenda del Sengoku: es que entienda por qué a
ella le brillan los ojos.

**El recurso formal: los puntos suspensivos.** Miku entra en todas sus frases con
«…» desde el prólogo. En el arranque de este evento también. Cuando se suelta,
**desaparecen**, y las frases se le alargan. Cuando se da cuenta de que ha
hablado, vuelven en la misma línea. Es el único indicador de que algo cambió y no
hace falta narrarlo: el jugador lo lee sin saber que lo está leyendo.

**Futaro se equivoca de verdad.** Ella no responde a preguntas, responde a
errores —así arrancó su primera línea del prólogo— pero el error no puede ser una
trampa. Miku es la única de las cinco con la que no hay cálculo: él se lee el
libro, llega hasta donde llega en una noche y se equivoca porque cuatro horas no
alcanzan. La llave sigue siendo el error; el motor pasa a ser el trabajo, que es
lo único que este protagonista sabe ofrecer.

Y el evento se cierra con que **ella se da cuenta de que él lo leyó**. No de que
la manipuló: de que alguien se pasó una noche con su tema. Ese es el hito de esta
ruta y conviene que llegue temprano, porque de ahí cuelga todo lo demás.

**Lo que este evento NO gasta.** El bloque de Miku del evento 6 —«habla sin
cortarse y sin pedir perdón después»— es el pago. Aquí como mucho llega a
tragarse el «perdón» a medias, y solo en la rama cálida. No se le entrega ninguna
hoja hecha a su medida: eso es del evento 6 y de preparar material.

---

### Movimiento 1 · Llegada

`[BG NUEVO — bg_biblioteca]` `[MUS stop fadeout 1.0]`

**narrador:** La biblioteca municipal quedaba dos calles antes del edificio. 

**narrador:** Pasaba por delante todos los días y nunca había entrado.

**narrador:** Segunda planta, la sala de lectura. Cuatro mesas largas y nadie en tres de ellas.

`[CG NUEVO — cg_miku_biblioteca: Miku de tres cuartos en la mesa del fondo, leyendo, con la pila de libros a un lado y los audífonos COLGADOS DEL CUELLO, nunca puestos. Ventanal detrás, luz de tarde. Cámara desde un costado, no desde la puerta. Un solo personaje en el frame. Sostiene todo el movimiento 1, así que tiene que aguantar en pantalla.]`

**narrador:** Estaba al fondo, de espaldas a la puerta, con una pila de libros a la izquierda y los audífonos colgados del cuello.

**mc_pensamiento:** Cuatro libros. Ninguno del temario.

**mc_pensamiento:** Y no estaban amontonados. Estaban apilados por tamaño, con los lomos alineados.

**narrador:** No pasaba las páginas. Se quedaba en cada una bastante más de lo que se tarda en leerla.

**mc_pensamiento:** Así no se estudia.

**mc_pensamiento:** Así se lee.

**mc_pensamiento:** Y los audífonos estaban apagados.

**mc_pensamiento:** A esa distancia se oye algo, aunque sea un zumbido. No había nada.

**mc_pensamiento:** El otro día, en el departamento, se los subió en cuanto saqué las hojas.

**mc_pensamiento:** Me borró del mapa sin decir una palabra.

**mc_pensamiento:** No los lleva para escuchar música.

**mc_pensamiento:** Los lleva ahí abajo, listos, para el momento en que alguien se acerque.

**narrador:** Me senté enfrente.

**narrador:** Tardó tres segundos largos en levantar la vista.

`[BG bg_biblioteca with dissolve]` `[SPR miku neutral at pj(0.5)]`

**miku:** …

**mc:** Buenas tardes.

**miku:** …

**miku:** …¿Cómo sabías que estaba aquí?

**mc:** No lo sabía. Llevo una hora dando vueltas.

**mc:** Pasé por tu casa primero.

**mc:** Ninguna de tus hermanas supo decirme dónde estabas.

**narrador:** Algo se le movió en la cara al oír eso, tan rápido que no me dio tiempo a leerlo.

**miku:** …¿Y entonces?

**mc:** El libro que llevabas el otro día tenía la etiqueta de una biblioteca. Esta es la que queda cerca del edificio.

**narrador:** Bajó el libro dos dedos, lo justo para mirarme por encima del canto.

**miku:** …Ah.

**narrador:** No pareció convencerle del todo, pero tampoco se levantó.

---

### Movimiento 2 · El intento por la puerta principal

`[SFX sfx_papel_mesa volume 2.5]`

**narrador:** Saqué el temario de sociales y lo puse sobre la mesa, girado hacia ella.

`[CG NUEVO — cg_estudio_biblioteca: POV desde el sitio de Futaro. Primer término inferior, sus antebrazos y sus manos sosteniendo el temario abierto sobre la mesa, desenfocados y cortados por el borde. Enfrente, Miku de tres cuartos con su libro, sin devolver la mirada. Mismo lenguaje que cg_pupitre_manana y cg_manija_edificio: nada de cara, nada que el modelo pueda romper.]`

**mc:** Quedan tres semanas y media para el examen. 

**mc:** Historia es tu asignatura.

**miku:** …No es mi asignatura.

**mc:** Es la que tienes peor y la que más fácil sube. Empezamos por ahí.

**miku:** …

**mc:** Unificación de Japón. Del final de las guerras civiles al periodo Edo. Entra entero.

**miku:** …Está bien.

**mc:** ¿Está bien que sí, o está bien que me calle?

**miku:** …

**mc:** Lo voy a tomar como que sí.

**narrador:** Bajó la vista al temario tres segundos y la volvió a subir al libro que tenía abierto.

**mc_pensamiento:** Tres segundos. Los conté.

**mc_pensamiento:** Perfecto. Un muro de ladrillo, pero educado.

**mc_pensamiento:** Llevo dos días haciendo lo mismo con las cinco y funcionando con ninguna.

**mc_pensamiento:** Repasemos lo que sé de Miku.

**mc_pensamiento:** Uno: en su hoja de ayer había una marca de borrador debajo de la respuesta equivocada. 

**mc_pensamiento:** Escribió la correcta primero y la borró.

**mc_pensamiento:** Dos: el primer día me habló de logística del período Sengoku sin que le preguntara,

**mc_pensamiento:** y luego se escondió detrás del libro en cuanto se oyó a sí misma.

**mc_pensamiento:** Tres: lleva unos audífonos apagados colgados del cuello,

**mc_pensamiento:** listos para subírselos en cuanto alguien le hable.

**mc_pensamiento:** No es que no sepa. Es que no piensa hablar de nada que le importe delante de alguien que va a calificarla.

**mc_pensamiento:** Y no se me ocurrió ninguna forma de resolver eso.

**mc_pensamiento:** Solo se me ocurrió la de siempre.

---

### Movimiento 3 · La página noventa

**narrador:** Cerré el temario y saqué de la mochila otro libro, con la misma etiqueta en el lomo que los suyos.

`[SFX sfx_papel_mesa volume 2.5]`

**narrador:** Lo reconoció antes de que llegara a la mesa.

`[CG NUEVO — cg_miku_sorpresa: mismo encuadre y misma luz que cg_miku_biblioteca —esa semilla sirve de punto de partida— pero con el libro bajado del todo, los ojos abiertos y la mirada fuera del libro por primera vez. El ejemplar de Futaro entra en el cuadro por el borde inferior, sin mano. Es el otro lado de la moneda del primero: en aquel no miraba, en este mira.]`

**miku:** …Ese es el que estaba leyendo yo.

**mc:** Hay dos ejemplares. Lo saqué anoche.

**miku:** …¿Por qué?

**mc:** Porque el otro día dijiste que las batallas las gana quien mueve el arroz y no entendí nada.

**narrador:** No dijo nada. Pero tampoco volvió al libro.

**mc:** Llegué hasta la página noventa. Me quedé dormido a las tres.

**mc:** Y creo que el tipo que lo escribió se equivoca.

`[BG bg_biblioteca with dissolve]` `[SPR miku neutral at pj_habla(0.5)]`

**miku:** …¿En qué?

**mc:** Le dedica cuarenta páginas a cómo se movía la comida y seis a la batalla más famosa del siglo. Está al revés.

**mc:** Las guerras las ganan las batallas. Lo demás es papeleo.

**narrador:** Miku cerró el libro sobre el dedo índice, para no perder la página.

**mc_pensamiento:** Era la primera vez en dos días que dejaba de mirar a otro lado.

**miku:** …¿Y qué comían?

**mc:** ¿Quiénes?

**miku:** …Los treinta mil hombres. En esa batalla famosa.

**mc:** …

**miku:** …Tres veces al día. Todos los días. Durante las seis semanas que tardaron en llegar hasta ahí caminando.

**mc:** Eso lo resolvería alguien. No es lo importante.

`[SPR NUEVO — miku animada at pj_habla(0.5)]` `[MUS NUEVO — descubrimiento fadein 2.0]`

**miku:** Había un señor de la guerra que se llamaba Takeda Shingen.

**miku:** Su provincia estaba metida entre montañas. No tenía nada de costa.

**mc:** ¿Y eso es un problema?

**miku:** Sin mar no hay sal. Y sin sal no se podía guardar la comida: no existían las neveras.

**miku:** O salabas el pescado y la carne, o en tres días no servían.

**miku:** Toda la sal que comía su gente se la compraban a los vecinos.

**narrador:** Hablaba más rápido. 

**narrador:** No había subido la voz —seguíamos en una biblioteca—, pero las frases le habían dejado de empezar con una pausa.

**miku:** Y un día los vecinos se pusieron de acuerdo y dejaron de vendérsela.

**mc:** …Sin atacarlo.

**miku:** Sin un soldado. Sin salir de su casa. Solo dejaron de vender.

**mc:** ¿Y qué hizo?

**miku:** Nada. No había nada que hacer. Lo estaba perdiendo.

**miku:** Y entonces le mandó sal Uesugi Kenshin. Su peor enemigo.

**miku:** Llevaban diez años peleándose y ninguno de los dos había conseguido ganar.

**mc:** ¿Por qué haría eso?

**miku:** Dijo que él peleaba con armas, no con comida. 

**miku:** Que quería ganarle en un campo de batalla, no verlo morirse de hambre en su casa.

**miku:** De ahí sale una frase que en Japón todavía se dice. 

**miku:** «Mandarle sal al enemigo.» 

**miku:** Se usa para cuando ayudas a alguien que no soportas, porque hay cosas que no se hacen.

**miku:** Aunque seguramente no pasó.

**mc:** …¿Cómo que no pasó?

**miku:** Esa parte no aparece en ningún papel de la época.

**miku:** Está escrita cien años después, solo para que la historia sonara más atractiva.

**miku:** Lo que sí es seguro es que les quitaron el acceso a la sal y que ahí dentro siguió habiendo sal igual. 

**miku:** Alguien se la vendió.

**miku:** Y a mí eso me parece mucho más—

`[SPR NUEVO — miku encogida at pj(0.5)]` `[MUS stop fadeout 1.5]`

**narrador:** Se paró en mitad de la palabra.

**narrador:** Creo que se oyó. 

**narrador:** Fue eso: se oyó a sí misma hablando en voz alta durante un minuto entero.

**miku:** …

**miku:** …Perdón. Hablé mucho.

**narrador:** Y volvió a abrir el libro por donde tenía el dedo.

---

### Movimiento 4 · La decisión

**mc_pensamiento:** Tercera vez.

**mc_pensamiento:** Tercera vez que dice algo que nadie le pidió y tercera vez que se disculpa por haberlo dicho.

**mc_pensamiento:** Nadie se disculpa por decir algo cierto, a menos que le hayan enseñado que decirlo cuesta.

`menu:`

---

**Opción A · «Ponerla a prueba. Preguntarle por un detalle del libro.»** *(cálida — `[$ sumar_punto("miku", 1)]`)*

**mc:** ¿Cuánto tardaba la sal en llegar desde el mar hasta allá?

`[SPR miku encogida at pj_habla(0.5)]`

**miku:** …¿Qué?

**mc:** Es una pregunta.

**mc:** Montaña, carga a lomo de animal, hace quinientos años. Cuánto tardaba.

**miku:** …Diez días. Doce si llovía.

**mc:** ¿Y cuánto aguantaban ellos sin sal?

`[SPR miku animada at pj_habla(0.5)]` `[MUS descubrimiento fadein 2.0]`

**miku:** Depende de la época del año. En verano, con el pescado, casi nada. 

**miku:** Por eso quitarles el acceso a la sal no era una amenaza para más adelante, era de ese mismo mes.

**miku:** Eso es lo que a la gente se le esca—

**narrador:** Se detuvo otra vez. Pero esta vez se detuvo distinto: se detuvo mirándome a mí, no al libro.

**miku:** …Per—

**mc:** No.

**miku:** …

**mc:** Estabas contestando una pregunta que te hice yo. Eso no se disculpa.

**narrador:** No dijo nada. Se le puso el libro a media altura, sin llegar a subirlo del todo.

**narrador:** Y entonces miró el ejemplar que yo había dejado sobre la mesa.

**miku:** …Dijiste que llegaste a la página noventa.

**mc:** Noventa y dos.

**miku:** …Lo de la sal está en la ciento veinte.

**narrador:** Lo dijo despacio, como quien termina una cuenta.

**mc_pensamiento:** Ahí estaba lo que acababa de entender.

**mc_pensamiento:** No que yo supiera de esto. 

**mc_pensamiento:** Justo lo contrario: que no sabía nada, y que aun así me había pasado la noche en ello.

**mc:** Voy a llegar a la ciento veinte.

**miku:** …

**mc:** Lo que acabas de contarme son tres preguntas del examen.

**mc:** Rutas de comercio, cómo se sostenía una provincia y por qué acabó unificándose el país.

**mc:** No te falta la materia. 

**mc:** Te falta creer que lo que sabes cuenta como saber.

**miku:** …No es lo mismo.

**mc:** Es exactamente lo mismo, y lo vas a comprobar en tres semanas.

**narrador:** No me contestó. Pero cuando me levanté, el libro seguía a media altura y no había vuelto a subir.

---

**Opción B · «Reconocer su nivel. Hacer una valoración de su esfuerzo.»** *(tibia — sin puntos, sin desaire)*

**mc:** Se te da bien esto.

`[SPR miku encogida at pj_habla(0.5)]`

**miku:** …No se me da bien. Solo lo he leído.

**mc:** Que es más de lo que ha hecho nadie en tu casa.

**miku:** …Eso no es difícil.

**narrador:** Lo dijo sin ninguna gracia, como quien cierra una puerta con educación.

**mc_pensamiento:** Le acabo de poner una nota.

**mc_pensamiento:** Y ella lleva toda la vida escuchando notas comparadas con otras cuatro.

**narrador:** El libro le subió hasta media cara, y ahí se quedó.

---

**Opción C · «El Sengoku no entra en el examen.»** *(fría — `[$ desaires_cap1 += 1]`)*

**mc:** Nada de eso entra en el examen.

**mc:** Unificación de Japón, tres temas, y ninguno pregunta por la sal.

**mc:** Si vas a dedicarle una hora a algo, que sea a lo que te van a preguntar.

`[SPR miku neutral at pj(0.5)]`

**narrador:** No protestó. No se defendió. 

**narrador:** Asintió una vez, muy despacio, como si le hubieran confirmado algo que ya sospechaba.

**miku:** …Ya lo sé.

**narrador:** Miró un segundo el ejemplar que yo había dejado sobre la mesa, y después apartó la vista.

**mc:** Entonces empecemos por el tema uno.

**miku:** …Hoy no.

`[SFX sfx_silla volume 2.5]`

**narrador:** Recogió los cuatro libros, los apiló y se subió los audífonos.

**narrador:** Y esta vez, desde donde yo estaba, se oía la música.

**mc_pensamiento:** …

**mc_pensamiento:** Antes no sonaban.

---

### Movimiento 5 · Cierre

*(común a las tres ramas; la última línea cambia)*

`[BG bg_negro with fade]`

**narrador:** Salí de la biblioteca cuando estaban apagando las luces de la segunda planta.

**mc_pensamiento:** Una de cinco. Y ni siquiera entera.

**mc_pensamiento:** Quedan tres semanas.

*Cierre A (cálida):*

**mc_pensamiento:** Pero hoy alguien me habló durante un minuto seguido sin que yo se lo pidiera dos veces.

**mc_pensamiento:** Eso, en esa casa, es un récord.

*Cierre B (tibia):*

**mc_pensamiento:** Dijo cuatro frases y volvió a esconderse. 

**mc_pensamiento:** No sé si perdí algo, pero desde luego no gané nada.

*Cierre C (fría):*

**mc_pensamiento:** Tenía razón en lo del examen.

**mc_pensamiento:** Lo raro es que llevo toda la tarde con la sensación de haber hecho algo mal teniendo razón.

`→ Vuelve al hub.`

---

### Assets del evento

| Asset | Tipo | Estado | Nota |
|---|---|---|---|
| `bg_biblioteca` | BG | pendiente | Sala de lectura, tarde. Mesas largas, vacía. Ya estaba en el mapa |
| `cg_miku_biblioteca` | CG | pendiente | Movimiento 1. Ella leyendo, sin saber que la miran |
| `cg_estudio_biblioteca` | CG | pendiente | Movimiento 2. POV, solo antebrazos de Futaro |
| `cg_miku_sorpresa` | CG | pendiente | Movimiento 3. Reaprovecha la semilla del primero |
| `miku animada` | sprite | pendiente | El único sprite del juego donde habla por gusto |
| `miku encogida` | sprite | pendiente | El medio segundo después de oírse |
| `descubrimiento` | BGM | pendiente | Sirve para los cinco eventos, no solo este |

Reutilizados sin tocar: `miku neutral`, `sfx_papel_mesa`, `sfx_silla`, `bg_negro`.

**Los tres CG son un tercio del presupuesto de arte del capítulo.** Si hay que
recortar, el que se cae es `cg_estudio_biblioteca`: es el único cuyo momento
—Futaro estrellándose contra el muro— se sostiene igual de bien con
`bg_biblioteca` y el sprite. Los otros dos no son intercambiables entre sí: el
primero es ella sin saber que la miran y el tercero es ella mirando, y esa
inversión es el evento entero en dos imágenes.

**`cg_miku_biblioteca` y `cg_miku_sorpresa` van con la misma semilla.** Mismo
encuadre, misma luz, mismo sitio; lo único que cambia es la altura del libro y a
dónde va la mirada. Generarlos en la misma sesión y guardar la semilla: si se
hacen por separado con semanas de diferencia, no van a coincidir y la inversión
deja de leerse.

**`miku animada`** — la diferencia va en la **silueta**, no en la cara: el libro
abajo o fuera del cuadro, hombros abiertos, barbilla arriba. En todos los sprites
que existen de las cinco hay algo delante del cuerpo; aquí no hay nada. A un 30 %
de tamaño eso es lo único que se lee. Ojos abiertos, sonrisa mínima o ninguna
—no está contenta, está concentrada—, y **sin rubor**: el rubor la haría tímida y
en ese minuto no lo es.

**`miku encogida`** — misma pose que `neutral` pero con el libro subiendo, a
media cara, y la mirada de lado hacia el interlocutor. Es la que más se va a
reutilizar en los tres capítulos.

**`descubrimiento`** — entra dos veces y sale dos veces, siempre con ella
hablando. Nunca suena con Futaro razonando: si acompaña al monólogo de él deja de
ser el tema de las hermanas y pasa a ser fondo, que es lo que ya se decidió con
`hogar` en el prólogo. Si al final no se produce, la escena aguanta en silencio;
la biblioteca es el sitio del juego donde el silencio no se nota.

---

### Notas de implementación

- El evento abre con `$ sumar_punto("miku", 2)` en la primera línea del label,
  antes de nada. Si el jugador eligió la biblioteca en el hub 1, esa llamada es
  la que escribe `primera_conexion`.
- La opción cálida suma **+1 aparte**, con una segunda llamada al helper. Nunca
  `puntos_miku += 3` de golpe.
- La fría toca `desaires_cap1`, no los puntos. No resta afinidad: el jugador que
  la enfría se queda en 2, no en 1.
- Marcar el evento como consumido —`miku_visitada_cap1`— para el evento 6 y para
  que el hub ofrezca la revisita corta en lugar del evento entero.
- La exclusividad de la biblioteca (buscar a Miku **o** preparar material) se
  resuelve en el menú del hub, no aquí dentro.
- Todo `show` con su posición, incluidos los `pj_habla` de las respuestas de
  Miku. Está a 0.5 durante toda la escena porque es la única en pantalla.
