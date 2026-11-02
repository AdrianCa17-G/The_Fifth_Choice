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

**mc_pensamiento:** Ya no son una lista mas de lo respecta a mi trabajo, son personas.

**mc_pensamiento:** O mas bien quintillizas, aunque luzcan iguales, cada una es un mundo diferente.

**mc_pensamiento:** Y cada una me lo ha demostrado, a su modo.

**mc_pensamiento:** Qué raro. Me da más miedo ahora que antes.

**mc_pensamiento:** Pero confío en ellas.

#### Aula

`[BG bg_aula]` `[with fade]`
`[SPR ichika neutral at pj(X_ICHIKA)]` `[SPR nino neutral at pj(X_NINO)]` `[SPR miku neutral at pj(X_MIKU)]`
`[SPR yotsuba sonriendo at pj(X_YOTSUBA)]` `[SPR itsuki neutral at pj(X_ITSUKI)]` `[with dissolve]`

**narrador:** Las cinco ya estaban en sus pupitres, con los libros cerrados.

**narrador:** No por desinterés: por haber llegado al final de lo que se podía repasar.

*Confesiones. Orden fijo: Yotsuba, Ichika, Miku, Itsuki, Nino. Una línea cada una; condición
`e6_estado_de(h) != "no_visitada"` para «alcanzada».*

`[SPR yotsuba sonriendo at pj_habla(X_YOTSUBA)]`

if alcanzada:

> **yotsuba:** ¡Estudié las lecturas dos veces! Y todavía recuerdo qué sentía cada personaje.
> **yotsuba:** Aunque... bueno, admito que a mitad de camino me distraje pensando en tí.
> **yotsuba:** Creí que te ibas a quedar dormido y llegarías tarde al examen, [mc].
> **yotsuba:** Pero ya que estás aquí... ¿me das un mensaje de aliento?

else:

> **yotsuba:** ¡Repasé las fechas con Miku y las fórmulas con Ichika! 
> **yotsuba:** …Mis lecturas, para después.
> **yotsuba:** Quería terminar a tiempo para asegurarme de que no te desmayaras de los nervios antes del examen, [mc].
> **yotsuba:** ¡Pero al menos lo intentaré con toda la energía que me queda!

`[SPR ichika sonriendo at pj_habla(X_ICHIKA)]` *(en «no alcanzada»: `ichika neutral`)*

if alcanzada:

> **ichika:** Dormí cuatro horas y las gasté en fórmulas, no en el papel de la obra.
> **ichika:** Rarísimo, ¿no? Y todo gracias a cierto tutor terco que no se me sale de la cabeza.
> **ichika:** Si no saco una nota perfecta después de este esfuerzo...
> **ichika:** Me vas a deber una cita muy larga tú a mí, [mc], ¿eh?

else:

> **ichika:** Dormí cuatro horas. Con el guion y con las fórmulas. 
> **ichika:** Supongo que me distraje pensando en si de verdad lograríamos aprobar todos estos exámenes. 
> **ichika:** Aunque... haber tenido un poco más de compañia esa tarde no habría estado mal, ¿sabes?
> **ichika:** Los hermanos mayores también necesitamos tiempo para nosotros mismo, ¿no crees, [mc]?

`[SPR miku neutral at pj_habla(X_MIKU)]`

if alcanzada:

> **miku:** …Sé más de lo que van a preguntar. …Lo comprobé tres veces. …Por si acaso.
> **miku:** Quería asegurarme de que no tuvieras que preocuparte por mí ni un solo segundo, [mc].
> **miku:** …Y si con esto logro sorprenderte.
> **miku:** …Venceré mis miedos por completo.

else:

> **miku:** …Repasé sola, como siempre. …Dejé libre la silla de enfrente. …Costumbre.

`[SPR itsuki neutral at pj_habla(X_ITSUKI)]`

if alcanzada:

> **itsuki:** He estudiado cada noche. Y por primera vez sé qué es lo que sé.

else:

> **itsuki:** He estudiado cada noche. Sola, como siempre. Hay un problema que no sale. Saldrá.

`[SPR nino neutral at pj_habla(X_NINO)]`

if alcanzada:

> **nino:** Treinta días. El último duró cuatro. …Haz la cuenta tú. Yo no dije nada.

else:

> **nino:** No viniste a buscarme y tampoco te fuiste. …No es un cumplido. Es un dato.

#### Cierre del movimiento

**narrador:** Me miraron las cinco. Esperaban una frase para empezar.

**mc_pensamiento:** Hace un mes no tenía nada que decirles que no fuera mentira.

**mc_pensamiento:** Hoy sí. Cada una sabe algo, y yo ya sé que lo sabe.

**mc:** Hagan lo que saben.

**narrador:** No sonó a relleno. Cada palabra tenía un nombre detrás.

if persistent.final_malo_temprano_b_visto:

> **narrador:** Sentí que ya había dicho esa frase antes. Con otro verbo, y con otro final.

**profe:** Pueden empezar.

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

**narrador:** El mensaje llegó el sábado a media mañana: «Cinco. Departamento.» Sin firma.

**mc_pensamiento:** Cinco: la hora. O la cuenta. Con Maruo, nunca se sabe cuál de las dos.

`[BG bg_edificio]` `[with fade]` `[BG bg_departamento]` `[with dissolve]` `[CG cg_maruo_reunion]` `[with corte_seco]`
`[MUS contrato fadein 2.0 · volumen según S2]`

**maruo:** Siéntate.

**mc:** Sí, señor.

**narrador:** Me senté. Esta vez no había nada que demostrar con las piernas.

**narrador:** Cinco boletines sobre la mesa, boca abajo, alineados al borde.

**maruo:** Llegaron esta mañana.

**maruo:** Cinco.

if persistent.final_malo_temprano_b_visto:

> **narrador:** Esperé una segunda cifra. Por alguna razón, di por hecho que llegaría.

**mc_pensamiento:** Era la cuenta. Era la hora. Y no dijo nada más.

`[SLOT S2 · call e6_s2_<estado_entrada>]`

#### S2 · superado — `e6_s2_superado` *(contrato a volumen pleno)*

**maruo:** Te dije en la cocina que no repetiría la advertencia.

**maruo:** No la repetí. Tampoco la cobré.

**mc:** ¿La condición…?

**maruo:** Se cumplió. Cinco aprobadas. La más justa marcó sesenta.

**maruo:** Un punto menos y esta conversación sería otra.

**narrador:** Lo dijo como se anuncia un horario. Y por eso pesó el doble.

**mc_pensamiento:** Un punto. Todo el mes colgando de un punto, y sin saber de cuál de las cinco.

**maruo:** No esperes que lo celebre. Cumpliste lo que firmaste.

**mc:** No lo esperaba.

**narrador:** Era mentira, y los dos lo supimos. Maruo, por una vez, la dejó pasar.

#### S2 · mixto — `e6_s2_mixto` *(contrato a volume 0.6)*

**maruo:** Aprobaron las cinco. Hay márgenes que no me gustan.

**mc:** ¿Qué tienen de malo los márgenes?

**maruo:** Nada. Salvo que a veces se aprueba por poco y se cree que fue por mucho.

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

`[MUS stop fadeout 0.3]`

**narrador:** Alineó los boletines con dos dedos, aunque ya estaban alineados.

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

---

### Movimiento 8 · Las cinco

`[BG bg_departamento]` `[with dissolve]` *(silencio: las puertas suenan sobre nada)*

**narrador:** Esperé. En esta sala el silencio y la espera siempre han sido lo mismo.

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

**narrador:** Éramos seis en la sala, y por primera vez nadie parecía estar de paso.

**narrador:** Itsuki dio un paso hacia mí. Yo, sin proponérmelo, di otro hacia ella.

`[SPR itsuki neutral at pj_habla(X_ITSUKI)]`

**itsuki:** Sobre lo del primer día—

**mc:** Sobre lo del asiento—

**narrador:** Nos detuvimos los dos. A media frase, a medio paso.

**itsuki:** Tú primero.

**mc:** No. Tú.

**itsuki:** Dije que tú primero. Es una oración completa.

**mc:** «No, tú» también lo es.

**itsuki:** …Ese argumento es válido.

`[SPR yotsuba sonriendo at pj_habla(X_YOTSUBA)]`

**yotsuba:** ¡¡Esperen!! ¡Antes de que se arruguen! ¡Los boletines! ¡A la mesa!

**narrador:** Itsuki cerró la boca. Yo cerré la mía. La frase se quedó entre los dos, sin dueño.

#### La mesa

`[CG cg_cinco_aprobadas NUEVO]` `[with dissolve]` `[MUS cotidiano fadein 2.0]` *(tinte según estado: ver notas de CG)*

**nino:** A la de tres. Y que nadie mire de reojo.

**nino:** Una. Dos. Y…

**narrador:** Dieron vuelta a los cinco boletines a la vez. Y, claro, todas miraron de reojo.

**mc_pensamiento:** Hace un mes se pusieron de acuerdo para fallar igual.

**mc_pensamiento:** Hoy se pusieron de acuerdo para mostrarse distintas.

**yotsuba:** ¡Cada una, la foto del suyo! ¡Y al grupo! ¡Sin trampas!

**mc_pensamiento:** La disculpa seguía entre nosotros. Y esta vez no me pareció tarde: me pareció pendiente.

`[$ e6_disculpa_pendiente = True]`

---

### Movimiento 9 · Casa

`[MUS stop fadeout 1.5]` `[BG bg_comedor]` `[with fade]` `[MUS cena fadein 2.0]`

**narrador:** El curry se olía desde el rellano.

`[SPR raiha hablando at pj(0.20)]` `[SPR isanari neutral at pj(0.73)]` `[with dissolve]`

**raiha:** ¡Hermanito! Hice curry antes de saber cómo salía todo.

**raiha:** Así, salga lo que salga, ya está hecho. ¡El curry nunca falla!

**mc:** Aprobaron las cinco.

**raiha:** …¿Las cinco?

**mc:** Las cinco.

**raiha:** ¡¡LAS CINCO!!

**raiha:** ¡Te dije que podías con cinco a la vez!

**mc:** Me lo dijiste con voz de «ojalá».

**raiha:** ¡Pero la voz de «ojalá» también cuenta!

`[SPR isanari neutral at pj_habla(0.73)]`

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
