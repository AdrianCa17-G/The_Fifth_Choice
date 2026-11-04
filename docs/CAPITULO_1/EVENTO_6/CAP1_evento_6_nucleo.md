## Evento 6 · Guion núcleo — cierre del Capítulo 1

> **Ruta en el repo:** `docs/CAPITULO_1/EVENTO_6/CAP1_evento_6_nucleo.md`
> **Escrito.** Assets pendientes (un solo CG). Cubre los Mov. 1, 7, 8, 9 y 10.
> Los Mov. 2–6 (los cinco bloques de examen) los escriben los chats 3 y 4.

Marcadores como en los hubs. `[BG]` fondo · `[CG]` ilustración · `[SPR]` sprite ·
`[MUS]` música · `[SFX]` efecto · `[AMB]` ambiente · `[$]` línea de código ·
`[NUEVO]` asset que no existe todavía · `[SLOT]` punto donde entra una capa ·
`[SCREEN]` pantalla propia · `[ECO h]` hueco que llenan los chats 3 y 4.

---

### Decisiones de este movimiento

**Es el negativo del Final B.** Mismo lunes, mismo aula, mismas frases con el signo
cambiado (Anexo A del análisis). El espejo es de imagen y de estructura: ninguna línea
de B se repite literal, salvo «Gracias por la comida».

**Arranca el lunes.** La interconexión 6 ya gastó la última sesión, la visita de Maruo
del viernes, el chat del sábado y las puertas del domingo. Aquí no se vuelve a ellos.

**«Alcanzada» = visitada en su hub, con cualquier rama.** Las confesiones del Mov. 1
hablan de cómo llega cada una al examen y nunca de MC, así valen igual en cálida,
tibia y fría. El tono de la rama lo ponen los bloques (chats 3 y 4).

**El estado de entrada solo toca S1, S2 y S3.** Más dos cosas que no son texto: la
música de Maruo (Mov. 7) y el tinte del CG de las cinco (Mov. 8). Las confesiones, el
Mov. 9 y el resto del Mov. 10 son idénticos en los tres estados.

**Maruo sigue seco.** Dice menos de lo que sabe, no celebra, no sonríe. En «bueno» casi
reconoce, sin calidez. No se usa `cg_maruo_espaldas`: ese CG significa despido.

**Los boletines llegan boca abajo.** Ni MC ni el jugador ven un número hasta el Mov. 10
(única excepción: el «sesenta» de Maruo en superado). La imagen que cierra el Mov. 8 es
la vuelta de los cinco a la vez, vista desde la mesa.

**La disculpa de Itsuki no se gasta (P-13).** MC e Itsuki empiezan a la vez, se paran,
y Yotsuba los interrumpe. Queda marcada como pendiente para el Capítulo 2.

**Nino no admite que confía (P-14).** Cuenta los días y deja que el dato hable. Nunca
dice «confío».

**Capa opcional por `persistent` (P-17).** Tres líneas de déjà vu (Mov. 1, 7 y 8) para
quien tenga `persistent.final_malo_temprano_b_visto`. MC solo siente que ya vivió algo
parecido; no hay cuarta pared.

**Cero puntos, sprites ni BGM nuevos (P-09, P-16, P-23).** Un único CG nuevo:
`cg_cinco_aprobadas`. El de audífonos de Miku queda fuera por equidad (P-15, nivel A).

**Convención de foco.** Todo `[SPR h expr at pj_habla(X_H)]` implica a las otras cuatro
en `pj_calla(X_*)` dentro del mismo `with disolucion_lenta`. Posiciones de la formación:
`X_ICHIKA` `X_NINO` `X_MIKU` `X_YOTSUBA` `X_ITSUKI`.

---

### Movimiento 1 · Lunes

`[$ ui_escena("beat", None, "Semana de exámenes")]` `[$ tiempo_restante = "cinco exámenes"]`
`[MUS stop]` `[BG bg_escuela]` `[with fade_dia]` `[SFX sfx_timbre volume 1.5]`

*(Entra sobre el silencio de la noche anterior: el timbre suena solo durante la primera línea.)*

**narrador:** El timbre sonó en un instituto donde nadie hablaba de otra cosa.

**narrador:** Otra cosa que no sean los exámenes.

**mc_pensamiento:** Lunes, japonés. Martes, matemáticas. Miércoles, inglés. Jueves, ciencias. Viernes, sociales.

**mc_pensamiento:** Cada día, una materia. Y detrás de cada materia, una de ellas.

**mc_pensamiento:** Como dijo Miku, son cinco materias y ellas con cinco.

**mc_pensamiento:** Pensé que lo dijo por decir, pero esa frase tenía un gran significado.

**mc_pensamiento:** Un significado que ahora descubriré.

`[SLOT S1 · call e6_s1_<estado_entrada>]`

#### S1 · superado — `e6_s1_superado`

**mc_pensamiento:** «Si una sola reprueba, se acabó.» Maruo lo dijo en la cocina y no lo repitió.

**mc_pensamiento:** No hacía falta. Una frase así no se repite: se cumple.

**mc_pensamiento:** Cinco exámenes, cinco días, y esa frase sentada al lado de cada uno.

**mc_pensamiento:** Hace un mes comencé este trabajo con una palabra clavada: despedido.

**mc_pensamiento:** Hoy entro con cinco nombres. Y con la palabra exactamente donde estaba.

**mc_pensamiento:** La diferencia es que ahora sé quién está detrás de cada hoja.

#### S1 · mixto — `e6_s1_mixto`

**mc_pensamiento:** Treinta días no alcanzan para saber nada. Solo para dejar de ser un desconocido.

**mc_pensamiento:** No sé si fue suficiente. Esa es la verdad completa, y es incómodamente corta.

**mc_pensamiento:** No tengo una palabra clavada esta vez. Tengo un número: cinco.

**mc_pensamiento:** Cinco exámenes que no puedo corregir, ni acompañar, ni adelantar.

**mc_pensamiento:** Hoy no se evalúa lo que yo hice. Se evalúa lo que ellas ya sabían.

#### S1 · bueno — `e6_s1_bueno`

**mc_pensamiento:** Por primera vez en un mes, no me sudan las manos al cruzar la puerta del instituto.

**mc_pensamiento:** Las conozco. No a todas igual, pero lo bastante para saber qué se les da bien.

**mc_pensamiento:** Eso no garantiza nada. Lo sé. Una nota es una nota.

**mc_pensamiento:** Pero esta mañana los cinco nombres suenan distinto: 

**mc_pensamiento:** Ya no son una lista mas de mi trabajo, son personas.

**mc_pensamiento:** O mas bien quintillizas, aunque luzcan iguales, cada una es un mundo diferente.

**mc_pensamiento:** Y cada una me lo ha demostrado, a su modo.

**mc_pensamiento:** Qué raro. Me da más miedo ahora que antes.

**mc_pensamiento:** Pero confío en ellas.

#### Aula

`[BG bg_aula]` `[with fade]`

`[CG NUEVO — cg_cinco_aula: Las cinco hermanas en el aula mirando a mc.
nose como explicarte lo que quiero pero el punto es que es un POV de ellas
cinco mirandonos y tiene que concordar con todo el guió que sigue.]`

**narrador:** Las cinco ya estaban en el aula, con los libros cerrados.

**narrador:** No por desinterés: por haber llegado al final de lo que se podía repasar.

**narrador:** Me miraron, y cada una se acercó hacia mí.

**mc_pensamiento:** Supongo que esperan alguna típica frase de aliento por parte mía.

**mc_pensamiento:** Nunca he sido bueno en eso, pero...

**mc:** ¡Hola, chicas! ¿Preparadas para los exámenes?

**mc:** Sé que todas tienen dudas o miedos sobre si aprobarán o no.

**mc:** Pero recuerden todo este mes que hemos estudiado.

**mc:** ¡Todos nosotros dimos nuestro mejor esfuerzo!

**mc:** ¡Así que sé que lo lograrán! ¡Aprobarán los exámenes!

**mc:**  ¡Confío plenamente en ustedes!

**mc:**  ¡ASÍ QUE TODOS APROBAREMOS! ¡SIN EXCEPCIÓN! 

**mc_pensamiento:**  Fue una de las mejores frases de aliento que he lanzado en mi vida.

**mc_pensamiento:**  Di lo mejor de mí.

**mc_pensamiento:** Y ellas escucharon lo que dije... Escuché lo que dije.

**narrador:** Cada una reaccionó de distinta manera.

**narrador:** Y me confesaron todo.

*Confesiones. Orden fijo: Yotsuba, Ichika, Miku, Itsuki, Nino. Una línea cada una; condición
`e6_estado_de(h) != "no_visitada"` para «alcanzada».*

`[BG bg_aula]` `[with fade]`

`[SPR yotsuba sonriendo at pj_habla(X_YOTSUBA)]` *(en «no alcanzada»: `yotsuba neutral`)*

if alcanzada:

 > **yotsuba:** ¡Estudié las lecturas dos veces! Y todavía recuerdo qué sentía cada personaje.
 > **yotsuba:** Esta vez no las dejé para después: ayudé a Miku con las fechas y a Ichika con las fórmulas, ¡pero calenté mis lecturas primero!
 > **yotsuba:** Como antes de una carrera: si no calientas, el cuerpo se queja a mitad de camino.
 > **yotsuba:** Así que no te preocupes por mí, [mc]. ¡Voy a llegar a la meta, y las cinco juntas!

else:

 > **yotsuba:** ¡Repasé las fechas con Miku y las fórmulas con Ichika!
 > **yotsuba:** …Mis lecturas, para después. Siempre se quedan para después.
 > **yotsuba:** Quería terminar a tiempo para que nadie se desmayara de los nervios antes del examen, ¡tú incluido, [mc]!
 > **yotsuba:** ¡Pero lo intentaré con toda la energía que me queda!

`[SPR ichika sonriendo at pj_habla(X_ICHIKA)]` *(en «no alcanzada»: `ichika neutral`)*

if alcanzada:

 > **ichika:** Dormí cuatro horas por estudiar fórmulas, no en el papel de la obra.
 > **ichika:** Rarísimo, ¿no? Yo, que me sé el guion entero y las fórmulas a medias.
 > **ichika:** El guion está en la mochila, doblado, y de ahí no sale hasta el último timbre.
 > **ichika:** Y si todo sale bien, tú, tutor terco, me debes una tarde entera sin libros.

else:

 > **ichika:** Dormí cuatro horas. Con el guion en una mano y las fórmulas en la otra.
 > **ichika:** Supongo que me distraje pensando en si de verdad lograríamos aprobarlo todo.
 > **ichika:** Aunque… un poco de compañía esa tarde no me habría venido mal, ¿sabes?
 > **ichika:** Las hermanas mayores también necesitamos que alguien nos eche una mano de vez en cuando, ¿no crees, [mc]?

`[SPR miku animada at pj_habla(X_MIKU)]` *(en «no alcanzada»: `miku neutral`)*

if alcanzada:

 > **miku:** …Sé más de lo que van a preguntar. …Lo comprobé tres veces.
 > **miku:** …Repasé las batallas, los clanes, las fechas. …Hasta lo que ni sale en el libro.
 > **miku:** …La silla de enfrente ya no se siente vacía.
 > **miku:** …Por si acaso, lo comprobaré una cuarta vez. …Ya sé que es demasiado.

else:

 > **miku:** …Repasé sola, como siempre.
 > **miku:** …Las batallas, los clanes, las fechas. …Todo, dos veces.
 > **miku:** …Dejé libre la silla de enfrente. …Por costumbre.
 > **miku:** …No esperaba a nadie. …Eso quiero pensar.

`[SPR itsuki sonriendo at pj_habla(X_ITSUKI)]` *(en «no alcanzada»: `itsuki neutral`)*

if alcanzada:

 > **itsuki:** He estudiado cada noche. Y por primera vez sé lo que hago.
 > **itsuki:** Ya encontré por qué fallaba en las conversiones de unidades. Tres veces el mismo error, y yo sin verlo.
 > **itsuki:** Sigo sin ser rápida. Pero ahora, cuando me trabo, sé por dónde volver.
 > **itsuki:** No me felicites todavía. Esto se demuestra en el examen, no antes.

else:

 > **itsuki:** He estudiado cada noche. Si tengo un problema que no sale. Saldrá.
 > **itsuki:** Lo repito, lo reviso, lo repito otra vez. …Siempre llego a la misma cifra.
 > **itsuki:** No pedí ayuda a nadie. Prefiero equivocarme por mi cuenta que acertar por ayuda de un tercero.
 > **itsuki:** Dijiste «sin excepción». Pues prepárate: yo me lo tomo en serio.

`[SPR nino pillada at pj_habla(X_NINO)]` *(en «no alcanzada»: `nino neutral`)*

if alcanzada:

if alcanzada:

 > **nino:** Treinta días. El último tutor duró cuatro. …Haz la cuenta tú.
 > **nino:** Y no pongas esa cara. Yo no dije nada. Los números hablan solos.
 > **nino:** Repasé inglés leyendo etiquetas en voz baja. …Si me viste mover los labios en el súper, no viste nada.
 > **nino:** Y la próxima vez que quieras dar un discurso, baja la voz. Se oyó hasta el pasillo.

else:

 > **nino:** No viniste a buscarme y tampoco te fuiste. …No es un cumplido. Es un dato.
 > **nino:** Repasé inglés sola, con las etiquetas de la cocina, en voz baja. …Nadie me escuchó. Mejor para mí.
 > **nino:** Y no, no te estaba esperando. …Contaba los días. Es distinto.
 > **nino:** Ahora cállate un momento y déjame repasar la última página.

#### Cierre del movimiento

`[CG NUEVO — cg_cinco_aula: ya está definido anteriormente]`

**narrador:** Me miraron las cinco. Esperaban una frase para terminar.

**mc_pensamiento:** Hace un mes no tenía nada que decirles que no fuera mentira.

**mc_pensamiento:** Hoy sí. Cada una sabe algo, y yo ya sé que lo sabe.

**mc:** Hagan lo que saben.

**narrador:** No sonó a relleno. Cada palabra tenía un nombre detrás.

if persistent.final_malo_temprano_b_visto:

> **narrador:** Sentí que ya había dicho esa frase antes. Con otro verbo, y con otro final.

> **narrador:** Siempre me imagino escenarios catastróficos antes de ver mi realidad.

**profe:** Bien, todos a sus pupitres.

**profe:** Volteen las hojas de sus exámenes.

**profe:** Pueden empezar.

`[BG bg_aula]` `[with fade]`

`[SFX sfx_hoja volume 2.0]` `[AMB amb_reloj fadein 2.0 volume 0.4]`

`→ Mov. 2 (e6_bloque("yotsuba")).`

---

### Costura Mov. 1 → Mov. 6

Entra `amb_reloj` al terminar el Mov. 1 y sigue sonando por los cinco bloques; el Mov. 7
lo corta. Los sprites de la formación desaparecen solos con el `scene cg_<h>_examen` de
cada bloque. `tiempo_restante` baja con cada día: `"cuatro exámenes"` tras Yotsuba,
`"tres exámenes"`, `"dos exámenes"` y `"un examen"` al entrar Miku. HUD en modo `beat`
con la hermana del día; del Mov. 7 en adelante vuelve a `normal`.

---

### Movimiento 7 · Resultados y Maruo

`[$ ui_escena("normal")]` `[AMB stop fadeout 1.0]` `[BG bg_negro]` `[with fade_dia]` `[SFX sfx_celular volume 1.5]`

**narrador:** Sábado a media mañana.

**narrador:** Estaba en mi casa, repasando todo lo que sucedió esta semana.

**narrador:** Una semana totalmente diferente a las mismas de siempre.

**mc_pensamiento:** No hacía nada más que pensar en los resultados de los exámenes.

**mc_pensamiento:** No los míos, los de ellas.

**narrador:** Sin embargo, el tiempo de espera duró poco.

**narrador:** Mi teléfono sonó y tenía el nombre de quien diría el veredicto final.

**narrador:** Maruo.

**narrador:** El mensaje llegó y decía: «Cinco. Departamento.».

**mc_pensamiento:** Cinco: la hora. O la cuenta. Con Maruo, nunca se sabe cuál de las dos.

**narrador:** Me alisté y fui directamente al departamento de las Nakano.

`[BG bg_edificio]` `[with fade]` `[BG bg_departamento]` `[with dissolve]` `[CG cg_maruo_reunion]` `[with corte_seco]`
`[MUS contrato fadein 2.0 · volumen según S2]`

**mc:** Buenas tardes, señor Maruo.

**maruo:** Siéntate.

**mc:** Sí, señor.

**narrador:** Me senté. Esta vez no había nada que demostrar.

**narrador:** Cinco boletines sobre la mesa, boca abajo, alineados al borde.

**maruo:** Los resultados llegaron esta mañana.

**maruo:** Cinco.

if persistent.final_malo_temprano_b_visto:

> **narrador:** Esperé una segunda cifra. Por alguna razón, di por hecho que llegaría.

**mc_pensamiento:** Era la cuenta. Era la hora. Y no dijo nada más.

`[SLOT S2 · call e6_s2_<estado_entrada>]`

#### S2 · superado — `e6_s2_superado` *(contrato a volumen pleno)*

**maruo:** Te dije en la cocina que no repetiría la advertencia.

**maruo:** No la repetí. Tampoco la cobré.

**mc:** ¿La condición…?

**maruo:** Se cumplió. Cinco aprobadas. La más baja llegó a sesenta.

**maruo:** Un punto menos y esta conversación sería otra.

**narrador:** Lo dijo como se anuncia un horario. Y por eso pesó el doble.

**mc_pensamiento:** Un punto. Todo el mes colgando de un punto, y sin saber de cuál de las cinco.

**maruo:** No esperes que lo celebre. Cumpliste lo que firmaste.

**mc:** No lo esperaba.

**narrador:** Era mentira, y los dos lo supimos. Maruo, por una vez, la dejó pasar.

#### S2 · mixto — `e6_s2_mixto` *(contrato a volume 0.6)*

**maruo:** Aprobaron las cinco. Hay márgenes que no me gustan.

**mc:** ¿Qué tienen de malo los márgenes?

**maruo:** Nada. Salvo que a veces se aprueba por poco y se cree que fue un éxito.

**narrador:** Miró los boletines al decirlo. Pero la frase parecía dirigida a otra mesa.

**mc_pensamiento:** No sonó a elogio. Tampoco a reproche. Sonó a alguien que sigue haciendo la cuenta.

**maruo:** No me corresponde alegrarme. Tampoco quejarme.

**maruo:** Me corresponde que el contrato siga. Y sigue.

**mc:** Gracias.

**maruo:** No me las des. No es un favor.

#### S2 · bueno — `e6_s2_bueno` *(contrato a volumen 0.6; se corta en la línea 5)*

**maruo:** Tu padre me habló de alguien que no se rendía.

**maruo:** Me faltaba ver qué hacía ese alguien mientras no se rendía.

**mc:** ¿Y qué vio?

**maruo:** Mis hijas llegan a casa y hablan de lo que estudian. Antes llegaban y se encerraban.

**maruo:** Pensé que era la edad. Que se les pasaría.

**maruo:** No era la edad.

**mc:** Yo no hice tanto, señor.

**maruo:** No te pedí humildad. Te dije lo que vi.

**maruo:** Esta semana, cada noche, las cinco en la cocina discutiendo a la vez.

**maruo:** Por quién lava los platos, por quién se queda con el último bocado.

**maruo:** Una noche estuve diez minutos en el pasillo. No entré.

**maruo:** No quería que se callaran. 

**maruo:** Parecía que alguien las había cambiado. 

[MUS stop fadeout 0.3]

**narrador:** Alineó los boletines con dos dedos, aunque ya estaban alineados.

**narrador:** Seguían boca abajo. Ninguno de los dos hizo el gesto de darles la vuelta.

**maruo:** No te lo repetiré: esto no fue una casualidad.

**mc:** …Gracias, señor.

**maruo:** Aún no hay nada que agradecer.

#### Cierre del movimiento (común)

**maruo:** Los exámenes no terminan aquí.

**mc:** Lo sé.

**maruo:** No lo sabes todavía. El contrato no habla de un examen. Habla de una graduación.

**mc:** Entendido.

**maruo:** Eso espero.

`[SFX sfx_puerta_cierra volume 1.0]` `[MUS stop fadeout 2.0]` *(en «bueno» ya está en silencio)*

**narrador:** Se puso el abrigo y salió. Sin portazo, como siempre. Esta vez, sin que doliera.

**mc_pensamiento:** Aprobar no es lo mismo que salvarse. Hoy, por hoy, me alcanzaba con aprobar.

**mc_pensamiento:** Aunque saldré de este departamento con un pensamiento totalmente nuevo.

---

### Movimiento 8 · Las cinco

`[BG bg_departamento]` `[with dissolve]` *(silencio: las puertas suenan sobre nada)*

**narrador:** Esperé a que ellas salieran. 

**narrador:** En esta sala el silencio y la espera siempre han sido lo mismo.

if persistent.final_malo_temprano_b_visto:

> **narrador:** Conocía ese ruido de puertas abriéndose una por una. Lo recordaba terminando peor.

#### Las puertas

Se repite para cada `h` en `e6_orden_ecos()` (visitadas en orden de examen, luego las no
visitadas en el mismo orden):

`[SFX sfx_puerta_abre volume 1.2]` `[SPR h neutral at pj(X_H)]` `[with dissolve]` `[ECO h]`

- **Tras la primera puerta, antes de su eco:**

  **narrador:** Cada una vino a por su boletín. Boca abajo, sin mirarlo.

  **narrador:** Como se lleva algo que todavía no es de uno.

- **Antes de la cuarta puerta (la primera no visitada):**

  **narrador:** Las dos últimas puertas tardaron un poco más.

  **narrador:** Detrás de esas no había falta de ganas. Había costumbre de esperar.

**Contrato de cada `[ECO h]`** *(cuatro variantes por hermana, `e6_<h>_eco_<estado>`)*:
tres a cinco líneas; entra ya con su sprite en `pj(X_H)` y puede cambiar de expresión
con `pj_habla`; no alude al orden de salida ni a los ecos de las demás (el orden cambia
por partida); no cita ninguna nota; puede tener su boletín como objeto; termina en
`pj_calla`. Nino: sin «confío», según P-14.

#### El intento

*(Las cinco en formación, MC en la sala.)*

**narrador:** Éramos seis en la sala, y por primera vez nadie parecía estar aquí por obligación.

**narrador:** La primera en querer hablar fue ella, Itsuki.

**narrador:** Itsuki dio un paso hacia mí. Yo, sin proponérmelo, di otro hacia ella.

**narrador:** Aun habían cosas pendientes que teníamos que resolver.

`[SPR itsuki neutral at pj_habla(X_ITSUKI)]`

**itsuki:** Sobre lo del primer día—

**mc:** Sobre lo del asiento—

**narrador:** Nos detuvimos los dos. A media frase, a medio paso.

**itsuki:** Tú primero.

**mc:** No. Tú.

**itsuki:** Dije que tú primero. Es una oración completa.

**mc:** «No, tú» también lo es.

**mc:** Además, las damas primero.

**itsuki:** …Ese argumento es válido.

`[SPR yotsuba sonriendo at pj_habla(X_YOTSUBA)]`

**yotsuba:** ¡¡Esperen!! ¡Antes de que se arruguen! ¡Los boletines! ¡Ya están en la mesa!

**narrador:** Itsuki se calló. Yo tambien me callé. La frase se quedó entre los dos, sin dueño.

**mc_pensamiento:** La disculpa seguía entre nosotros. Y esta vez no me pareció tarde: me pareció pendiente.

**narrador:** Así es, parece que eso aun seguirá pendiente.

#### La mesa

**narrador:** Nos sentamos alrededor de la mesa sin que nadie lo propusiera.

**narrador:** Ellas, de un lado. Yo, enfrente. Cada una dejó su boletín frente a su silla, boca abajo.

**narrador:** Ninguna lo tocó. Ninguna quería ser la primera en darle la vuelta.

[SPR itsuki neutral at pj_habla(X_ITSUKI)]

**itsuki:** Propongo lo siguiente.

**itsuki:** Cada una lo abre en silencio, lo lee dos veces y solo después comparamos.

[SPR ichika sonriendo at pj_habla(X_ICHIKA)]

**ichika:** Qué plan tan ordenado, Itsuki. 

**ichika:** Hablas con mucha confianza para alguien que lleva un minuto con la mano encima del papel.

[SPR itsuki timida at pj_habla(X_ITSUKI)]

**itsuki:** …Es para que no se vuele.

[SPR nino neutral at pj_habla(X_NINO)]

**nino:**  No hay ninguna ventana abierta.

**itsuki:** …Es por si acaso.

[SPR ichika neutral at pj_habla(X_ICHIKA)]

**ichika:** Hablando por todas, debería decir que todo va a salir bien.

**ichika:** …¡Corazonada de hermana mayor!.

[SPR yotsuba incomoda at pj_habla(X_YOTSUBA)]

**yotsuba:** ¡A todas les habrá ido genial! ¡Seguro!

**yotsuba:** Y si a alguna no… ¡no pasa nada! ¡Cenaremos un plato hecho por Nino y se nos pasa!

**yotsuba:** …Pero si a mí no me fue bien, ¡que nadie ponga cara de puchero, eh!

[SPR nino nerviosa at pj_habla(X_NINO)]

**nino:** Seis sillas ocupadas. …Seis personas en esta mesa.

**nino:** Hace un mes no habría apostado por que todos estuvieramos reunidos. Sin problemas.

**nino:** …Es una observación. No le des importancia.

[SPR miku encogida at pj_habla(X_MIKU)]

**narrador:** Miku tenía las manos juntas delante del cuerpo y los audífonos colgados al cuello. Sin tocarlos.

**miku:** …Hoy no me los puse.

**miku:** …Quiero oír lo que diremos todas.

**miku:** …Todas a la vez.

[SPR nino molesta at pj_habla(X_NINO)]

**nino:** Tú estuviste con él antes de que saliéramos. …Sabes algo.

**mc_pensamiento:** Sabía que ninguna se quedaba fuera. No sabía nada más: ni cuánto, ni de quién.

**mc_pensamiento:** Y sabía que no me tocaba a mí quitarles este momento.

**mc:** Sé lo que Maruo me dijo a mí. Lo que dicen esos papeles es de ustedes.

[SPR ichika sonriendo at pj_habla(X_ICHIKA)]

**ichika:** Qué tutor más cruel.

**mc:** Lo sé.

[SPR itsuki neutral at pj_habla(X_ITSUKI)]

**itsuki:** Tu expresión no es la de quien trae malas noticias. …Aunque no es una garantía.

[SPR yotsuba animada at pj_habla(X_YOTSUBA)]

**yotsuba:** ¡¡Entonces abrámolos ya!!

[SPR nino neutral at pj_habla(X_NINO)]

**nino:** A la de tres. Y que nadie mire de reojo.

**nino:** Una. Dos. Y…

[SFX sfx_hoja volume 2.0]
[SFX sfx_hoja volume 2.0]
[SFX sfx_hoja volume 2.0]
[SFX sfx_hoja volume 2.0]
[SFX sfx_hoja volume 2.0]

**narrador:** Dieron vuelta a los cinco boletines a la vez. Y, claro, todas miraron de reojo.

(pausa de un segundo y medio, sin música)

**narrador:** Cinco hojas, un solo sonido.

play music main_theme fadein 1.5

[SPR miku encogida at pj_habla(X_MIKU)]

**miku:** …Sonaron juntas. …Como si fuera una sola hoja.

**narrador:** Una lágrima le recorrió por toda la cara. No se la secó.

**miku:** …No es tristeza. …Es que no sé dónde poner esto.

[SPR ichika sonriendo at pj_habla(X_ICHIKA)]

**narrador:** Ichika soltó una risa corta, de las que se escapan solas.

**ichika:** Ja. …Ja, ja. …Me quedé sin chiste. A mí, que siempre tengo uno.

**ichika:** Cuatro horas de sueño. …Y valieron cada minuto. Qué cosa más rara.

[SPR nino nerviosa at pj_habla(X_NINO)]

**narrador:** Nino leyó el suyo. Luego miró el de Miku, el de Yotsuba, el de Ichika, el de Itsuki. Movía los labios sin sonido.

**nino:** Uno. Dos. Tres. Cuatro. …Cinco.

**nino:** Cinco. Los conté dos veces.

**nino:** …Que nadie diga nada. Si alguien dice algo, me voy.

**narrador:** Se le quebró la voz en la última palabra. Nadie dijo nada. Nino se quedó.

[SPR yotsuba animada at pj_habla(X_YOTSUBA)]

**narrador:** Yotsuba ni miró el suyo. Miraba los de las demás, uno por uno, con los ojos muy abiertos.

**yotsuba:** ¡Todas! ¡¡Todas, todas, todas!!

**yotsuba:** ¡¡Miku, mira el tuyo!! ¡¡Nino, el tuyo!!

**ichika:** Yotsuba. El tuyo.

**yotsuba:** ¿Eh? …¡Ah, el mío!

[SPR yotsuba neutral at pj_habla(X_YOTSUBA)]

**narrador:** Bajó la vista. Y, por primera vez en todo el mes, Yotsuba se quedó callada.

**yotsuba:** …Este es mi boletin. …Esta soy yo. …Esto lo hice yo.

[SPR yotsuba animada at pj_habla(X_YOTSUBA)]

**yotsuba:** ¡¡Y lo hicimos todas!! ¡¡Y tú también, [mc]!! 

**yotsuba:** ¡Tú te quedaste hasta el último momento! ¡Eso también cuenta!

[SPR itsuki sonriendo at pj_habla(X_ITSUKI)]

**narrador:** Itsuki lo leyó línea por línea, como se lee un contrato. Dos veces, tal como había propuesto.

**itsuki:** Lo leí dos veces. …El resultado no cambió.

**itsuki:** Debería decir algo acorde a este momento.

**itsuki:** …Estoy pensando que decir pero no tengo ni idea.

**itsuki:** Lo que siento no lo puedo expresar con palabras.

**itsuki** …Anótenlo, provisionalmente, como «algo bueno».

**narrador:** Entonces levantó la vista y me miró. Quiso decirme algo. Pero nuevamente se calló.

**narrador:** Yo asentí, apenas. Lo de antes seguía ahí, entre los dos, y esta vez ninguno intentó sacarlo.

[SPR ichika sonriendo at pj_habla(X_ICHIKA)]

**ichika:** Y tú, tutor. Tienes cara de querer decirnos algo.

**mc:** No tengo nada que decirles. Esta vez no.

[SPR itsuki neutral at pj_habla(X_ITSUKI)]

**itsuki:** Es un alivio. Eres malo dando discursos.

**ichika:** La última vez fue «sin excepción». A gritos.

**mc:** Lo sé. Solo quiero decir una cosa, y corta.

**mc:** Hace un mes, esta mesa me daba miedo. Cinco personas iguales mirándome, esperando que yo supiera qué hacer.

**mc:** Los primeros días me botaron rápidamente de su departamento, no querían que sea su tutor.

**mc:** No por que me odiaran, sino por los temores que cada una tenía.

**mc:** Cargas que no podían aliviarlas solas y se las guardaban como si no fueran importantes.

**mc:** Por eso yo no me rendí. Nunca lo hago.

**mc:** A pesar de que me odiaran yo seguía yendo y yendo.

**mc:** Creía que era solo por el trabajo y la paga. 

**mc: **Pero me di cuenta que no es así, hay algo de ustedes que intenté descubrir.

**mc:** Hoy sigo sin saberlo del todo. Pero ya no veo cinco iguales.

**mc:** Veo a una Yotsuba. A una Ichika. A una Miku. A una Itsuki. A una Nino. 

**mc:** Cada una con su cara, su manera, su ruido.

**mc:** Lo que sea que diga ese papel lo escribieron ustedes. Nadie se los regaló.

**mc:** Y estoy contento de haber estado sentado frente a esta mesa cuando lo abrieron. 

**mc:** Nada más.

stop music fadeout 0.5

[SPR nino molesta at pj_habla(X_NINO)]

**nino:** …Eso fue un discurso.

**mc:** Dije que no tenía mucho que decir.

**nino:** Fue un resumen. Pocas frases. Las conté.

[SPR miku encogida at pj_habla(X_MIKU)]

**miku:** …Fue lindo.

**miku:** …A tu manera ...Fue lindo.

**miku:** …Gracias por tus palabras mc.

[SPR itsuki neutral at pj_habla(X_ITSUKI)]

**itsuki:** Breve. Aceptable. Bien dicho.

**mc_pensamiento:** Hace un mes se pusieron de acuerdo para fallar igual.

**mc_pensamiento:** Hoy se pusieron de acuerdo para mostrarse distintas.

[MUS main_theme fadein 2.0] 

[SPR yotsuba animada at pj_habla(X_YOTSUBA)]

**yotsuba:** ¡Cada una, muestre su examen! ¡Y nos tomaremos una foto! 

**yotsuba:** ¡La subiremos al grupo! ¡Sin trampas!

**yotsuba:** ¡[mc], tú la sacas! ¡Tienes los brazos más largos!

**mc:** ¿Y yo no salgo?

**yotsuba:** ¡Tú sales en la próxima! ¡Hoy es de las cinco!

**narrador:** Me puse de pie al otro lado de la mesa, con el celular de Yotsuba en las manos.

**yotsuba:** ¡Más arriba! ¡El mío más arriba!

**ichika:** Que se me vea la cara, no el flequillo.

**nino:** Un solo brazo. Es mi mejor ángulo.

**miku:** …¿Dónde pongo las manos? …Mejor delante.

**itsuki:** Debo salir recta. Con el boletín recto.

[CG cg_cinco_aprobadas] [with dissolve] (tinte según estado)

**mc:** ¡Digan «cinco»!

**quintillizas:** ¡¡Cinco!!

sfx camara (nuevo)

**narrador:** Tomé la foto. Ninguna bajó el boletín.

**ichika:** ¿Ya está? …Me tiembla el brazo y no pienso ser la primera en bajarlo.

**nino:** Yo tampoco. …Que baje primero Yotsuba.

**yotsuba:** ¡Yo no bajo nada! ¡Puedo quedarme así hasta mañana!

**itsuki:** Los brazos no funcionan así. Tarde o temprano se cansan.

**yotsuba:** ¡Pues que se cansen tarde!

**miku:** …Yo tampoco quiero bajar las manos todavía. …Mientras sigamos así, …esto sigue pasando.

**narrador:** Nadie se rio. Se quedaron un momento en silencio, juntas, cada una en su sitio, con la hoja en alto.

**mc_pensamiento:** Pensé en decirles que la foto ya estaba. No lo dije. Hay cosas que un «ya está» arruina.

**ichika:** Oigan, ¿saben qué es lo más raro? 

**ichika:** …Que esta mañana tenía miedo de abrirlo sola. Y no estaba sola.

**nino:** …Nunca había estado tan cansada. …Y tan bien. …Que no se repita esa frase.

**itsuki:** Lo anoto. «Nino dijo: tan bien.»

**nino:** Si lo anotas, te lo quito.

**itsuki:** Es un registro. Los registros no se quitan.

**yotsuba:** ¡Quiero una foto así cada vez que algo salga bien! 

**yotsuba:** ¡Y cuando salga mal, también! ¡Igual de juntas!

**itsuki:** …Moción aceptada. Con una condición: el boletín, recto.

**miku:** …Yo también. …Aunque salga mal. …Sobre todo si sale mal.

**nino:** No hablemos de que salga mal el día en que salió bien.

**mc:** Si sale mal, la foto la saco yo. Y la guardo igual que esta.

**ichika:** Qué tutor más cursi. …Me gusta.

**mc:** Pues yo no bajo el celular hasta que baje el último brazo.

**itsuki:** Entonces será larga la espera. …Bajo en tres.

**yotsuba:** ¡Una! ¡Dos!

**nino:** …Y.

**narrador:** Bajaron los brazos todas a la vez, sin contarlo. Igual que habían abierto los boletines.

**mc_pensamiento:** No leí ni un solo número. No hacía falta: cinco caras que ya no fingían nada.

**mc_pensamiento:** Dijeron «cinco». Y yo, detrás del celular, dije «seis». Bajito, para que no me oyeran.

**mc_pensamiento:** Ahora formo parte de ellas, y ellas de mí.

`[$ e6_disculpa_pendiente = True]`

---

### Movimiento 9 · Casa

`[BG bg_negro]`

**narrador:** Me despedí de todas y volví a casa.

**narrador:** Con una gran sensación de seguir conservando mi trabajo.

`[MUS stop fadeout 1.5]` `[BG bg_comedor]` `[with fade]` `[MUS cena fadein 2.0]`

**narrador:** Al llegar, alguien me estaba esperando, y yo tambien quería verla.

**mc_pensamiento:** Mi hermana Raiha, la única que ha confiado en mi desde el principio.

**mc_pensamiento:** Una de las razones por las que acepté el trabajo cuando no sabía que decidir.

**narrador:** El curry se olía por toda la casa.

`[SPR raiha hablando at pj(0.20)]` `[SPR isanari neutral at pj(0.73)]` `[with dissolve]`

**raiha:** ¡Hermanito! Hice curry antes de saber cómo te iba a ir.

**raiha:** Así, como te haya ido, la cena ya está hecha. ¡El curry nunca falla!

**mc:** Pues hoy comeremos un banquete, ¿No crees Raiha?

**mc:** ¡¡APROBARON LAS CINCO!!.

**raiha:** …¿Las cinco?

**mc:** Las cinco.

**raiha:** ¡¡LAS CINCO!!

**raiha:** ¡Te dije que podías con cinco a la vez!

**mc:** Me lo dijiste con voz de «ojalá». 

**mc:** Aunque te perdono porque tambien dudaba de mi en ese momento, jeje.

**raiha:** ¡Pero la voz de «ojalá» también cuenta!

`[SPR isanari neutral at pj_habla(0.73)]`

**isanari:** Hola mc, veo que hoy ha sido un éxito para tí.

**isanari:** Maruo llamó. Cobramos el mes entero.

**mc:** Lo sé.

**isanari:** Pareces menos contento de lo que dice el pago.

**mc:** No estoy menos contento. Estoy pensando en otra cosa.

**isanari:** ¿Qué cosa vale más que cinco veces la tarifa?

**mc:** Todavía no lo sé.

**narrador:** Mi padre no contestó. Pero se quedó mirando su plato más tiempo del necesario.

`[SPR raiha hablando at pj_habla(0.20)]`

**raiha:** ¡A comer! ¡Que se enfría!

**mc_pensamiento:** Hace un mes, «cinco veces la tarifa» era lo único que oía en esa frase.

**mc_pensamiento:** Esta noche la oí de fondo, como se oye un reloj en otro cuarto.

**mc:** Gracias por la comida.

**narrador:** Lo dije por costumbre. Pero esta vez la costumbre pesaba lo mismo que las palabras.

**mc_pensamiento:** Hace un mes, «todo» era una deuda y una hermana pequeña.

**mc_pensamiento:** Esta noche el «todo» tenía cinco personas más. Y ninguna cabía en una factura.

---

### Movimiento 10 · Cuarto, chat y libreta

`[MUS stop fadeout 1.5]` `[BG bg_cuarto_mc]` `[with fade]` `[MUS hogar fadein 1.5 volume 0.7]`

**narrador:** El celular empezó a vibrar antes de que terminara de sentarme.

`[$ duck()]` `[SFX sfx_celular volume 1.5]` `[$ quick_menu = False]` `[SCREEN chat_grupo]`

**narrador:** El grupo seguía llamándose «¡Equipo Quintillizas + Tutor!». Yotsuba nunca lo cambió.

#### El chat

Cabecera: «¡Equipo Quintillizas + Tutor!» · **6 miembros**. Mensajes en este orden, siempre
(no depende del estado). Cada `[foto]` es el boletín de su dueña, pequeño: los números no
se leen hasta la matriz.

| # | Quién | Mensaje |
|---|---|---|
| 1 | Yotsuba | `[foto]` ¡¡¡CIEN EN JAPONÉS!!! ¡¡¡MIREN!!! |
| 2 | Yotsuba | ¡¡Manden el suyo!! ¡¡Sin trampas!! |
| 3 | Ichika | `[foto]` Cien en matemáticas. Pueden aplaudir. Con moderación. |
| 4 | Miku | `[foto]` …Sociales: cien. |
| 5 | Nino | `[foto]` *(sin texto)* |
| 6 | Nino | Que conste que no me salí. |
| 7 | Itsuki | `[foto]` Ciencias: cien. Es un dato, no una celebración. |
| 8 | Yotsuba | ¡¡¡ES UNA CELEBRACIÓN!!! |
| 9 | Itsuki | Está bien. Una celebración pequeña. |

MC no escribe en el chat.

**narrador:** Nino no se había salido. Ni una vez en toda la semana de exámenes.

**mc_pensamiento:** No contesté. Cualquier cosa que escribiera iba a ser menos que lo que acababa de leer.

`[$ e6_chat_activo = True]`

#### La cuenta

**mc_pensamiento:** Hay algo que sé hacer sin que nadie me enseñe: sumar.

**mc_pensamiento:** Tomé la nota más alta de cada una.

`[SCREEN boletin_cinco · fase 1: la matriz de cinco filas, una por foto, con las notas de e6_notas · fase 2: se ilumina la diagonal y lo demás se apaga]`

**mc_pensamiento:** Japonés, matemáticas, inglés, ciencias, sociales. Cien, cien, cien, cien, cien.

`[SCREEN boletin_cinco · fase 3: la diagonal se funde en una sola fila de cinco cienes]` `[$ quick_menu = True]`

**mc_pensamiento:** Cinco máximos en cinco materias distintas. Ni un hueco, ni una repetida.

**mc_pensamiento:** Un boletín perfecto. De un alumno que no existe.

**mc_pensamiento:** Existe, pero repartido: cada una guarda lo que a las otras cuatro les falta.

**mc_pensamiento:** Y en todo el mes no se habían preguntado nada entre ellas.

**mc_pensamiento:** No controlé ninguna de esas cinco notas.

**mc_pensamiento:** Lo único que controlé fue a dónde fui.

**mc_pensamiento:** Y a dónde no.

**mc_pensamiento:** ¡ESO ES! ¡LO DESCUBRÍ!

**mc_pensamiento:** Separadas, son solo una quinta parte, una parte incompleta.

**mc_pensamiento:** Pero juntas, forman un estudiante perfecto, o a una chica perfecta.

**mc_pensamiento:** Capáz de superar cualquier obstaculo que se le atraviese.

#### La libreta

`[CG cg_libreta]` `[with fade]`

**narrador:** Abrí la libreta por la página de los cinco nombres. Seguía la frase de aquella noche.

**mc_pensamiento:** «De frente y las cinco a la vez, pierdo siempre.»

**narrador:** Debajo escribí otra. La letra me salió más firme que la primera vez.

**narrador:** «De una en una las alcancé. ¿Y de frente, las cinco a la vez?»

`[$ p1 = e6_promesas[0].capitalize()]` `[$ p2 = e6_promesas[1].capitalize()]`

**narrador:** Y debajo, más chico, dos nombres: [p1] y [p2].

**mc_pensamiento:** Dos promesas hechas sin que nadie me las pidiera. Esas no caducan.

`[SLOT S3 · call e6_s3_<estado_entrada>]` *(es lo último que se lee del capítulo)*

#### S3 · superado — `e6_s3_superado`

**mc_pensamiento:** Maruo dijo «cinco». No dijo «para siempre».

**mc_pensamiento:** La condición no se venció: se renovó.

**mc_pensamiento:** Esta vez, un punto de margen. ¿Cuántos tendré la próxima?

#### S3 · mixto — `e6_s3_mixto`

**mc_pensamiento:** Aprobaron las cinco. Lo repasé tres veces, por si el papel cambiaba de opinión.

**mc_pensamiento:** No sé qué parte fue mía. Tampoco sé a quién preguntárselo.

**mc_pensamiento:** La libreta no tiene una casilla para eso.

#### S3 · bueno — `e6_s3_bueno`

**mc_pensamiento:** Abrí las fotos sin contener el aire. Hace un mes no sabía hacerlo.

**mc_pensamiento:** Los cinco nombres ya no son una lista. Son cinco personas que salieron bien.

**mc_pensamiento:** Y cuando alguien te importa, lo único que queda por temer es lo que viene después.

`[MUS stop fadeout 3.0]` `[BG bg_negro]` `[with fade]`

`→ Sale al Capítulo 2 (jump cap2_inicio, tras e6_cerrar()).`

---

### Tabla de notas

Aprobado = 60. La diagonal (cada hermana en su materia fuerte) es siempre 100. Fuera de la
diagonal no hay 100 ni nada por debajo de 60. Ya está implementada en `e6_calcular_notas()`
(`10_minijuegos.rpy`); esta tabla fija lo que ese código produce:
`nota = base + desfase + ajuste`, recortada a 60–89.

| Estado de la alumna | Base | Valores posibles (antes de ajuste) |
|---|---|---|
| cálida | 82 | 82–89 |
| tibia | 72 | 72–79 |
| no visitada | 68 | 68–75 |
| fría | 60 | 60–66 |

| Ajuste por estado de entrada | superado | mixto | bueno |
|---|---|---|---|
| suma a toda nota fuera de la diagonal | −2 | 0 | +3 |

Desfases (fila = quién rinde; columna = materia; `—` es la diagonal). Con `base` de
cálida, tibia o no visitada (rango de 8 valores):

| | Mat | Ing | Soc | Jap | Cie |
|---|---|---|---|---|---|
| Ichika | — | 6 | 3 | 0 | 5 |
| Nino | 4 | — | 6 | 3 | 0 |
| Miku | 7 | 4 | — | 6 | 3 |
| Yotsuba | 2 | 7 | 4 | — | 6 |
| Itsuki | 5 | 2 | 7 | 4 | — |

Con `base` de fría (rango de 7 valores):

| | Mat | Ing | Soc | Jap | Cie |
|---|---|---|---|---|---|
| Ichika | — | 6 | 4 | 2 | 0 |
| Nino | 4 | — | 0 | 5 | 3 |
| Miku | 0 | 5 | — | 1 | 6 |
| Yotsuba | 3 | 1 | 6 | — | 2 |
| Itsuki | 6 | 4 | 2 | 0 | — |

**Ejemplo** (superado; Itsuki fría; Ichika y Nino cálidas; Miku y Yotsuba no visitadas):

| | Mat | Ing | Soc | Jap | Cie |
|---|---|---|---|---|---|
| Ichika | **100** | 86 | 83 | 80 | 85 |
| Nino | 84 | **100** | 86 | 83 | 80 |
| Miku | 73 | 70 | **100** | 72 | 69 |
| Yotsuba | 68 | 73 | 70 | **100** | 72 |
| Itsuki | 64 | 62 | 60 | 60 | **100** |

En superado la nota más baja es siempre 60 (la fila de la fría, con el −2 y el recorte),
y por eso Maruo puede decir «la más justa marcó sesenta» sin consultar nada.

---

### Flags de gancho para el Capítulo 2

| Variable | Valor | Quién la escribe | Uso en el Capítulo 2 |
|---|---|---|---|
| `e6_frase[h]` | `completa` · `cortada` · `cerrada` · `espera` | `e6_marcar_ganchos` (bloques) | Cada hermana retoma o completa su frase en su propio evento. No es el eje del capítulo |
| `e6_promesas` | lista de las dos no visitadas | `e6_marcar_ganchos` | Dos deudas de MC; la libreta del Mov. 10 las nombra |
| `e6_notas` | matriz 5×5 | `e6_iniciar` | Boletín persistente de la partida. Solo notas, nunca afinidad |
| `e6_estado_entrada` · `e6_estado` | ver análisis | `e6_iniciar` | Tono de apertura del capítulo |
| `e6_disculpa_pendiente` **NUEVA** | `True` | Mov. 8 | La disculpa MC–Itsuki sigue viva |
| `e6_chat_activo` **NUEVA** | `True` | Mov. 10 | El chat existe como primer espacio compartido de las seis personas |

Las dos variables nuevas necesitan su `default` en `00_definiciones.rpy` (`False`).

---

### Notas de CG y de audio

**CG nuevo: `cg_cinco_aprobadas`** (Mov. 8). Frontal, las cinco en fila a la misma
profundidad, en la misma mesa y con la semilla de `cg_cinco_estudiando`. Cada una sostiene
su boletín vuelto hacia cámara, sin esconderlo; sin texto legible en las hojas. Silueta
distinta por hermana, para que se lea al 30 %: Yotsuba con el boletín en alto y hombros
abiertos; Ichika despierta, el boletín contra el pecho; Nino con un solo brazo cruzado y el
otro sosteniendo; Miku con las dos manos delante del cuerpo y los audífonos al cuello, sin
tocarlos; Itsuki derecha, con el boletín recto. Misma actitud invertida que
`cg_cinco_sentadas`: nadie finge nada. Los prompts los escribe el chat 7.

Un solo CG para los tres estados; el estado se resuelve con tinte (sin arte nuevo):

| Estado | Transform |
|---|---|
| superado | `BrightnessMatrix(-0.05) * SaturationMatrix(0.90) * TintMatrix("#e0e6f5")` |
| mixto | sin tinte |
| bueno | `BrightnessMatrix(0.04) * SaturationMatrix(1.08) * TintMatrix("#fff0d8")` |

Reutilizados: `cg_maruo_reunion` (Mov. 7), `cg_libreta` (Mov. 10). Sin sprites nuevos.

**Audio** (todo reutilizado):

| Mov. | Pista o efecto | Notas |
|---|---|---|
| 1 | `sfx_timbre` 1.5 · `sfx_hoja` 2.0 · `amb_reloj` 0.4 (fadein 2.0) | Timbre solo sobre silencio. Sin música; el reloj entra con «Pueden empezar» |
| 7 | `sfx_celular` 1.5 · `contrato` · `sfx_puerta_cierra` 1.0 | `contrato`: pleno en superado, 0.6 en mixto, 0.6 y cortada en la quinta línea en bueno. La puerta de Maruo, la más baja, como siempre |
| 8 | `sfx_puerta_abre` 1.2 ×5 · `cotidiano` | Las puertas suenan sobre silencio. `cotidiano` entra con el CG de la mesa. El mismo archivo cinco veces: la última suena más sola |
| 9 | `cena` | Sin efectos. `cena` vuelve donde en B8 no sonaba nada |
| 10 | `hogar` 0.7 · `sfx_celular` 1.5 con `duck()` | Una sola vibración al abrir el chat; el canal `sound` es único |

---

### Notas de implementación

- **Dónde cae cada capa.** S1 va dentro de `e6_lunes`, entre las dos líneas de horario y el
  aula. S2 va dentro de `e6_resultados`, tras «Era la cuenta. Era la hora…». S3 va **al
  final** de `e6_cuarto`: el stub actual la llama al principio y hay que moverla.
- **Bucle de las puertas.** El `while` de `e6_cinco` ya recorre `e6_orden_ecos()`. Falta
  añadirle por iteración el `play sound`, el `show` en `pj(X_*)` con `dissolve`, y las
  dos líneas condicionales («Cada una vino a por su boletín…» solo en la primera vuelta;
  «Las dos últimas puertas…» solo en la cuarta).
- **Las tres líneas de déjà vu** (Mov. 1, 7, 8) leen `persistent.final_malo_temprano_b_visto`
  y no escriben nada. Replay arranca con `persistent` intacto, así que funcionan en Finales.
- **Pantallas de Mov. 10.** `chat_grupo` y `boletin_cinco` apagan `quick_menu` mientras
  están en pantalla y lo restauran (mismo patrón que el collage). `boletin_cinco` lee
  `e6_notas[h][materia_de_h]` y nunca muestra afinidad.
- **Promesas.** `p1` y `p2` salen de `e6_promesas` en el orden en que los bloques las
  añadieron (orden de examen).
- **Sin puntos.** El núcleo no llama a `sumar_punto` (P-09). `02_cap1_beat_Nino.rpy` ya
  no suma en ninguna rama (P-08): no hay nada que cambiar en código.
- **Móvil (P-20).** Nada de este documento depende de un minijuego. Si en táctil
  se fuerza `persistent.mj_modo = "saltar"`, el núcleo no cambia.
- **Galería (P-17, P-21).** Descomentar `("cg_cinco_aprobadas", "Cinco aprobadas")` en la
  sección «Capítulo 1» de `GALERIA`. Rediseñar la Galería para que los `*_fracaso` no
  cuenten para el 100 % de cada hermana queda fuera de este documento.
- **Cálculo de finales.** Que la declaración final del jugador sume el +1 que lleva a una
  hermana de 9 a 10 puntos pide actualizar el esquema de `00_definiciones.rpy` (§8) y
  `05_finales.rpy`. Tampoco es de este documento.
- **Longitud.** Ninguna entrada supera dos líneas de caja. Si con la tipografía definitiva
  alguna desborda, se parte; no se baja el tamaño de letra.
