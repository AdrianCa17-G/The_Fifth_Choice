## Evento 6 · Guion de bloques B — Nino e Itsuki

> **Ruta en el repo:** `docs/CAPITULO_1/EVENTO_6/CAP1_evento_6_bloques_B.md`
> **Escrito.** Assets pendientes: dos CG (`cg_nino_examen`, `cg_itsuki_examen`). Sin sprites nuevos.
> Cubre los **Mov. 4 y 5** del Evento 6 y los **ocho ecos del Mov. 8** que corresponden a estas dos hermanas.
> Los Mov. 2, 3 y 6 (Yotsuba, Ichika, Miku) están en `CAP1_evento_6_bloques_A.md`. El marco, S1/S2/S3 y el intento interrumpido de disculpa están en `CAP1_evento_6_nucleo.md`.

Marcadores como en el núcleo y en los bloques A. `[BG]` fondo · `[CG]` ilustración · `[SPR]` sprite ·
`[MUS]` música · `[SFX]` efecto · `[AMB]` ambiente · `[$]` línea de código ·
`[NUEVO]` asset que no existe todavía · `[MJ]` llamada a minijuego · `[CALL]` capa B ·
`[SLOT]` punto donde una variable elige entre líneas.

Hablantes: `narrador`, `mc`, `mc_pensamiento`, `profe` y, para la voz interior, `nino_int` e `itsuki_int`
(ya definidos en `00_definiciones.rpy`).

---

### Decisiones de estos bloques

**Orden de lectura.** El de `e6_bloque`: núcleo → monólogo → minijuego (solo cálida) → promesa
(solo no visitada) → gesto. El eco lo llama `e6_cinco` en el Mov. 8. La frase de cambio no tiene label
propio: vive dentro del monólogo (tibia, fría, no visitada) o del minijuego (cálida), y
`e6_marcar_ganchos` escribe `e6_frase[h]` por estado, no por línea.

**La capa B no es un label del contrato.** El beat de Nino (`nino_rama_beat`) y el beat de la azotea de
Itsuki se escriben aparte, dos líneas cada uno, y se llaman **desde dentro del monólogo**, en el punto
marcado `[CALL …]`. Así no se toca el despachador `e6_bloque`. Detalle en «Notas de implementación».

**Nino se desborda, no se calla.** Su tic no es hablar poco: son órdenes cortas a sí misma («Revisa.
No mires. Otra vez.») que se alargan cuando la grieta aparece y que ella misma corta. En cálida, por
primera vez, la frase **termina**. En tibia se corta y la orden la tapa. En fría se cierra con una orden.
En no visitada se queda en el patrón de siempre.

**Itsuki cierra todas las oraciones; la grieta es la que no se cierra.** Sujeto, verbo, punto. Cuando
algo le duele, los sujetos desaparecen y las oraciones se quedan a medias («Preguntarle a él sería—»).
Cuando se repone, vuelve a la oración completa, más seca que antes. En cálida la oración que antes no
cerraba **cierra, en otra dirección**. En no visitada la termina por dentro y no la dice.

**El eco literal.** Cada monólogo cita lo que MC *hizo de verdad* en la rama (no el texto del menú):

| | Cálida | Tibia | Fría | No visitada |
|---|---|---|---|---|
| **Nino** (hub) | «Solo el tiempo lo va a demostrar» y que no prometió nada | Cargó la cesta sin decir nada | «Yo sí voy a durar» | Que no vino, y que «ya me vio en su casa más de lo que quería» |
| **Itsuki** (hub) | «Solo te digo dónde mirar» | «¿Quieres que lo revisemos desde el principio?» | Le quitó el cuaderno y lo resolvió de pie | Que no fue; «si hubieras venido, no te habría echado» |

**Los números de Nino avanzan con la semana.** El núcleo (lunes) dice «Treinta días». Su monólogo del
miércoles cuenta **treinta y dos**. El eco del Mov. 8 (sábado) dice **treinta y cinco**. Es la misma
cuenta en tres fechas; si el Mov. 7 cambiara de día, hay que mover los números.

**P-14, cómo se resuelve.** Nino ya confía, y no lo admite. Lo que lleva la confianza no es una frase: es
que **cuenta los días de este tutor** (de los otros perdió la cuenta), que no se sale del chat y que, en
cálida, se levanta y entrega sin quedarse de guardia. Nunca dice «confío». Su negación más fuerte es
«Eso no es confiar. Es llevar la cuenta. Es distinto» —dicha dos veces seguidas, que es lo que la
delata—. No aparece «no confío… todavía»: el prompt del chat lo permitía, pero la versión DECIDIDA de
P-14 pide que ya confíe y lo niegue, y ese «todavía» sería admitir el futuro. Ver duda D-01.

**P-13, la disculpa de Itsuki no se gasta.** Ni MC ni ella dicen «perdón» ni «lo siento» en estos bloques.
El intento ya está en el Mov. 8 del núcleo. El eco de Itsuki termina antes de que ese intento empiece y
no menciona «el primer día» ni «el asiento».

**El profesor es el tercero neutral.** Preguntarle a sus hermanas es admitir algo; preguntarle a MC es
darle la razón (hub). El profesor no es ninguna de las dos cosas. Por eso su pregunta es legítima y
pequeña: **pide que repita el enunciado**. No le da la respuesta; le devuelve «dónde mirar».

**Música.** Cálida: `descubrimiento` durante el monólogo → el tema de la hermana durante el minijuego →
silencio con solo `amb_reloj` cuando cae la frase. Tibia, fría y no visitada: solo `amb_reloj`. El tema
solo suena si cálida. `guardia` **no** suena aquí: se reserva a cuando ella se explica ante MC.

**Lo que estos bloques NO hacen.** No hay puntos (`sumar_punto` no se llama). No se resuelve la tarjeta
de receta de Nino ni se nombra. No hay disculpas. No hay romance en la voz interior. No hay sprites ni
BGM nuevos. No se repiten los pensamientos de `beat_casa` ni las líneas de `reaccion_*`: se *cobra* lo
sembrado allí con frases nuevas.

**Longitud.** Ninguna entrada pasa de ~100 caracteres (dos líneas de caja).

---

### Cobros obligatorios — dónde está cada uno

| Hermana | Cobro | Dónde |
|---|---|---|
| Nino | «El último duró cuatro días. Tú llevas treinta y cinco.» (cierra la apertura: «Tú llevas uno») | E cálida, dicho en voz alta |
| | «Solo el tiempo lo va a demostrar» | M cálida |
| | «Anota la fecha» (invertido: ahora es ella quien la anota) | M fría · E fría |
| | No se sale del chat | M de los cuatro estados (planta la línea que el núcleo cobra en el Mov. 10) |
| | Final B3.3: se queda «revisando» | G tibia, fría y no visitada (espejo); en cálida, entrega y sale |
| | «No pienso adelantar el golpe» | J (frase cálida) |
| | Nunca «confío»; la tarjeta de receta no se toca | Todos |
| Itsuki | «El juego se acabó» | E cálida · E no visitada |
| | Final B3.4: la mirada de un segundo y el «no preguntó» | G (cuatro variantes) |
| | La azotea: «ya no me queda ningún sitio…» | Capa B (`e6_itsuki_beat_*`) |
| | «Solo te digo dónde mirar» | M cálida · J |
| | «Ni se te ocurra decirme la respuesta» | M cálida |
| | «Pedirlo habría sido…» terminada, solo por dentro | M no visitada |
| | «Sube sin el cuaderno» | P no visitada |
| | La disculpa **no** se gasta | Ningún sitio de este documento |

---

---

## BLOQUE 4 · Nino · Miércoles · Inglés (Mov. 4)

### N · Núcleo — `e6_nino_nucleo`

*(Todos los estados. `amb_reloj` ya suena desde el Mov. 1; sin música. El `scene` del CG retira la formación.)*

`[$ ui_escena("beat", "nino", "Aula · Inglés")]` `[$ tiempo_restante = "tres exámenes"]`
`[BG bg_negro]` `[with fade_dia]`

**narrador:** Miércoles. Inglés.

`[SFX sfx_hoja volume 2.0]` `[CG NUEVO — cg_nino_examen]` `[scene cg_nino_examen · with fade]`

**narrador:** Segunda fila. Mi hoja boca abajo antes de la mitad, y el lápiz encima.

**narrador:** Nino leyó el texto de comprensión una sola vez, sin mover los labios.

**narrador:** A media página se le movió la boca sola: una frase entera, sin voz. En inglés.

**mc_pensamiento:** Pensaba en inglés, en un examen de inglés. Si se lo dijera, lo negaría.

**mc_pensamiento:** Así que no se lo dije. Hay cosas que se cuidan mejor sin señalarlas.

**narrador:** Su hoja avanzaba a la velocidad a la que otros copian su nombre.

**mc_pensamiento:** A los quince minutos había terminado. Yo, tres antes. Ella lo sabía.

---

### M · Monólogos — `e6_nino_mono_<estado>`

*(Texto B, pregunta nueve: es la comprensión lectora. Todas las líneas son de `nino_int`. En los cuatro
estados hay una línea sobre el chat y un punto `[CALL e6_nino_beat_<nino_rama_beat>]`.)*

#### M · cálida — `e6_nino_mono_calida`

*(Foco: lo que cambió porque nadie le prometió nada. Las órdenes a sí misma se alargan y esta vez no se
cortan. Sin cifras: la cuenta es del eco.)*

`[MUS descubrimiento fadein 2.0]`

**nino_int:** Texto B. Pregunta nueve. Lo leo una vez. No hace falta más.

**nino_int:** «Solo el tiempo lo va a demostrar.» Eso dijo, con cara de no estar prometiendo nada.

**nino_int:** Y no prometió nada. Esa es la parte que no sé dónde poner.

**nino_int:** Los otros prometían. Este no prometió y se quedó. Es una combinación rara.

**nino_int:** Yo hablé de más y no se lo contó a nadie. Se lo pregunté a Yotsuba, que no guarda nada.

**nino_int:** Yotsuba no sabía nada.

**nino_int:** Eso no es confiar. Es llevar la cuenta. Es distinto.

**nino_int:** Es distinto.

`[CALL e6_nino_beat_<nino_rama_beat> — dos líneas, ver «B · Capa de beat»]`

**nino_int:** Siempre veo venir el golpe. Me adelanto: me cierro antes, pido que se vayan antes.

**nino_int:** Así nunca duele a tiempo. Duele por adelantado. Y duele siempre.

**nino_int:** Hoy nadie me ha pegado. Y yo sigo con los brazos cruzados por dentro.

**nino_int:** El chat sigue silenciado. Esta semana no me salí ni una vez. Nadie me lo pidió.

**nino_int:** Hay cena, pase lo que pase con las notas. Cocino yo. Siempre cocino yo.

`[ACTIVA e6_nino_mj — las tres últimas líneas]`

**nino_int:** Cinco listas, una por cabeza. La mía la escribo la última, y es la más corta.

**nino_int:** Y una sexta línea que todavía no sé cómo llenar. …Primero las cinco.

#### M · tibia — `e6_nino_mono_tibia`

*(Foco: la tarea y una pregunta abierta, «¿fue amable o fue método?». Silencio salvo `amb_reloj`. La frase queda
cortada y la orden la tapa.)*

**nino_int:** Texto B. Pregunta nueve. Lo leo una vez.

**nino_int:** De los otros tutores perdí la cuenta. De este no. No sé por qué.

**nino_int:** Cargó mi cesta sin que se lo pidiera. Pesaba. No dijo nada. Yo tampoco.

**nino_int:** Dije «esto no significa nada». Lo dije yo, en voz alta, para que quedara dicho.

`[CALL e6_nino_beat_<nino_rama_beat> — dos líneas]`

**nino_int:** ¿Fue amable o fue método? Las dos cosas me cansan igual.

**nino_int:** Si fue amable, no sé qué quiere. Si fue método, no sé hasta cuándo.

**nino_int:** Mis hermanas ya no dicen «¿y si esta vez sí?». Lo dicen bajito, y lo oigo igual.

**nino_int:** El chat sigue silenciado. Esta semana no me salí. No sé por qué no me salí.

**nino_int:** Si aprobamos las cinco… quizás esta vez no—

**nino_int:** Revisa la ocho. Hay un «has» que debería ser «have».

**nino_int:** Ya terminé. Sigo en mi sitio. Hay que revisar.

#### M · fría — `e6_nino_mono_fria`

*(Foco: la herida convertida en método. Silencio salvo `amb_reloj`. Frases cortas, sin salida.)*

**nino_int:** Texto B. Pregunta nueve. Lo leo una vez.

**nino_int:** «Yo sí voy a durar.» Lo dijo como lo dijeron los otros. Casi palabra por palabra.

**nino_int:** Le dije que se guardara la promesa. Prometió durar. Ha durado. Eso hay que reconocérselo.

**nino_int:** No lo reconozco. Lo anoto. Son cosas distintas.

`[CALL e6_nino_beat_<nino_rama_beat> — dos líneas]`

**nino_int:** Aún queda el resultado. Y tras el resultado, el siguiente. Siempre queda el siguiente.

**nino_int:** Los que prometen se van rápido. Los que no prometen, más despacio. Todos se van.

**nino_int:** Mis hermanas se ilusionan solas. Yo me ocupo de lo mío.

**nino_int:** Lo mío es esto: revisar. Hoja por hoja, hasta la campana, por si acaso.

**nino_int:** Sigo en el chat. No me salí. Es para vigilar lo que dicen de él. Nada más.

**nino_int:** En la cabecera hay un renglón para la fecha. Lo llené al final, como siempre.

**nino_int:** Anota la fecha. Es hoy.

**nino_int:** Solo eso: una fecha.

#### M · no visitada — `e6_nino_mono_no_visitada`

*(Foco: la espera; responde a su `queja_nino`. Silencio salvo `amb_reloj`. Cuenta treinta y dos: es miércoles.)*

**nino_int:** Texto B. Pregunta nueve. Lo leo una vez.

**nino_int:** Dije que no esperaba nada. Es cierto. Esa es la ventaja de no esperar.

**nino_int:** Llevo treinta y dos días sin esperar nada. Y los llevo contados.

`[CALL e6_nino_beat_<nino_rama_beat> — dos líneas]`

**nino_int:** Las que fue a ver llegaron distintas a casa. No le dije si mejor o peor. No pienso decirlo.

**nino_int:** Alguien tiene que ser la que no cambia. Para que las demás tengan a dónde volver.

**nino_int:** No vino a buscarme. Está bien. A mí no se me busca: se me encuentra en la cocina o no.

**nino_int:** Me encontró en la cocina. Me oyó pedir que lo echaran. Y no se fue.

**nino_int:** Eso queda en la columna de los datos sin conclusión.

**nino_int:** El chat lo sigo leyendo. Alguien tiene que leerlo.

**nino_int:** Alguien tiene que ver venir el golpe.

**nino_int:** Sigo siendo yo.

---

### B · Capa de beat — `e6_nino_beat_<calida|tibia|fria>`

*(Dos líneas de `nino_int` por rama del beat de la cocina. Se llaman desde dentro de cualquiera de los cuatro
M. Valen igual en los cuatro estados de hub: no nombran la rama del hub.)*

#### B · cálida — `e6_nino_beat_calida`

**nino_int:** «¿Y quién junta los tuyos?» No contesté. La pregunta sigue en la cocina.

**nino_int:** Le mandé cortar cebollas finas. Las cortó gruesas. Las usé igual.

#### B · tibia — `e6_nino_beat_tibia`

**nino_int:** Lavó mi taza sin que se lo pidiera. A mi taza no la toca nadie.

**nino_int:** No le dije «quédate». Tampoco «vete». Los dos nos entendimos igual.

#### B · fría — `e6_nino_beat_fria`

**nino_int:** Le dije que hablaba el mismo idioma que papá. Lo dije para que doliera.

**nino_int:** No dolió. Asintió, como si ya lo hubiera oído. Eso fue peor.

*(`nino_rama_beat` además fija el nivel de los minijuegos: `mj_nivel()` devuelve «media» si es `calida`. Aquí no
hace falta tocar nada.)*

---

### J · Minijuego N1′ — `e6_nino_mj` *(solo cálida)*

`[MUS nino fadein 1.0 fadeout 1.5]`
`[MJ n1 · call mj_ejecutar("n1", "nino") → "ganado" | "saltado"]`

*(Dificultad por `mj_nivel()`. Fallos: `MJ_FALLOS`, dichos por `nino_int`. Las cinco listas y las tres
acciones del sexto hueco están en el anexo.)*

`[MUS stop fadeout 3.0]` *(la frase cae con solo `amb_reloj`)*

**narrador:** Nino dejó el lápiz sobre la mesa. No lo soltó: lo dejó. Hay una diferencia.

if `e6_mj["nino"]["resultado"] == "saltado"`:

> **narrador:** Hay compras que se hacen de memoria. Esta la hizo entera, de un tirón.

`[SLOT sexto hueco · e6_mj["nino"]["datos"].get("sexto", "blanco")]`

if `"taza"`:

> **nino_int:** Escribí «una taza más». Se compra igual aunque nadie la pida. …No es por nadie.

if `"blanco"`:

> **nino_int:** Dejé la sexta línea en blanco. Sin tachar. Una línea en blanco no se pierde: se espera.

if `"cuando"`:

> **nino_int:** Escribí «cuando se sepa». Se compra con el resultado en la mano, y no antes de saberlo.

**nino_int:** No pienso adelantar el golpe.

**nino_int:** Si cae, cae. Pero no voy a ganarle la mano para que duela primero.

**nino_int:** Esperar no es rendirse. Me costó treinta y dos días entenderlo.

**nino_int:** Voy a entregar. Las demás terminarán a su ritmo. Esta vez no hago guardia.

*(La frase de cambio es la primera vez que Nino dice algo largo sobre sí misma **sin cortarse a mitad**.)*

---

### F · La frase de cambio

| Estado | Frase | Dónde | `e6_frase[h]` |
|---|---|---|---|
| cálida | «No pienso adelantar el golpe.» *(entera, y le sigue una explicación sin interrupción)* | J, primeras líneas | `completa` |
| tibia | «Si aprobamos las cinco… quizás esta vez no—» → «Revisa la ocho.» *(la orden tapa la frase)* | M tibia, antepenúltima | `cortada` |
| fría | «Anota la fecha. Es hoy.» → «Solo eso: una fecha.» | M fría, últimas dos | `cerrada` |
| no visitada | «Alguien tiene que ver venir el golpe. …Sigo siendo yo.» | M no visitada, últimas dos | `espera` |

---

### P · Promesa — `e6_nino_promesa` *(solo no visitada)*

*(Corre entre el monólogo y el gesto. Pensamiento silencioso de MC. Usa solo lo que MC sabe por su
`queja_nino` y por la cocina.)*

**mc_pensamiento:** Dijo que alguien tiene que ser la que no cambia. Para que las demás tengan a dónde volver.

**mc_pensamiento:** También dijo que ya me había visto en su casa más de lo que quería. Que eso contaba como visita.

**mc_pensamiento:** Voy al centro comercial, al pasillo de importados. Y a cargar una cesta que no me haya pedido.

---

### G · Gestos — `e6_nino_gesto_<estado>`

*(Espejo de B3.3: allí terminaba, giraba la hoja, cruzaba los brazos y se quedaba «revisando» cuarenta minutos
para no dejarlas solas. Aquí **cálida entrega y sale**; en las otras tres sigue de guardia.)*

#### G · cálida

**narrador:** Nino terminó, repasó la hoja una sola vez con el dedo y dejó el lápiz sobre la mesa.

**profe:** Nakano. Si ya terminó, puede entregar.

**nino:** Sí.

`[SFX sfx_silla volume 2.5]`

**narrador:** Se levantó, dejó la hoja en la mesa del profesor y fue hacia la puerta sin mirar atrás.

**narrador:** A las demás no les echó ni una mirada de guardia. Ni una.

`[SFX sfx_puerta_cierra volume 1.0]`

**mc_pensamiento:** Quien ve venir el golpe se queda a esperarlo. Quien no lo adelanta, sale.

**mc_pensamiento:** Se fue sin vigilarlas. Y nadie se cayó.

`[SFX sfx_timbre volume 1.5]` `[MUS stop]` *(si aún suena algo)*

#### G · tibia

**narrador:** Nino terminó antes que casi todas. Soltó el lápiz. Giró la hoja boca abajo. Cruzó los brazos.

**profe:** Nakano. Si ya terminó, puede entregar.

**nino:** Aún no. Voy a revisar.

**narrador:** Revisó cuarenta minutos, con el dedo, línea por línea. Y, de reojo, a las otras cuatro.

**mc_pensamiento:** No había nada que revisar. Se quedaba por ellas. O por no estar a solas con lo que viene.

**mc_pensamiento:** Quizás por las dos cosas. Ella no iba a decirme cuál.

`[SFX sfx_timbre volume 1.5]`

#### G · fría

**narrador:** Nino terminó. Soltó el lápiz sin ruido, giró la hoja boca abajo y cruzó los brazos, un poco más fuerte.

**profe:** Nakano. Si ya terminó, puede entregar.

**nino:** No.

**narrador:** Se quedó revisando como quien patrulla una frontera. Sin mirar a nadie. A nadie.

**mc_pensamiento:** Ni a mí, ni a ellas. Hace un mes me miraba para odiarme. Ahora ni eso.

**mc_pensamiento:** Revisaba con el método de quien ya sabe cómo acaba y quiere llegar preparada.

`[SFX sfx_timbre volume 1.5]`

#### G · no visitada

**narrador:** Nino terminó y repasó la hoja con el dedo. Soltó el lápiz. Giró la hoja. Cruzó los brazos.

**profe:** Nakano. Si ya terminó, puede entregar.

**nino:** Estoy revisando.

**narrador:** Revisó cuarenta minutos. A la media hora levantó la vista y me miró una sola vez.

**mc_pensamiento:** No con odio. Con la cara de quien comprueba que algo sigue donde lo dejó.

**mc_pensamiento:** Seguía en mi asiento. Para ella, eso ya era una respuesta.

`[SFX sfx_timbre volume 1.5]`

---

### E · Ecos (Mov. 8) — `e6_nino_eco_<estado>`

*(Entra ya con `[SPR nino neutral at pj(X_NINO)]`. Las hermanas presentes van en `pj_calla`. No cita ninguna nota, no
alude al orden de salida y no dice «confío». Termina en `pj_calla`.)*

#### E · cálida

**narrador:** Nino llegó con el boletín doblado en cuatro y la barbilla en alto. Casi toda.

`[SPR nino neutral at pj_habla(X_NINO)]` `[with disolucion_lenta]`

**nino:** El último duró cuatro días. Tú llevas treinta y cinco.

**mc:** …

**nino:** No me mires así. Es aritmética.

`[SPR nino pillada at pj_habla(X_NINO)]` `[with disolucion_lenta]`

**nino:** Y que no se entere Yotsuba de que llevaba la cuenta. Haría un cartel.

`[SPR nino neutral at pj_calla(X_NINO)]`

#### E · tibia

**narrador:** Nino llegó con una bolsa del supermercado en cada mano, como si el boletín fuera lo de menos.

`[SPR nino neutral at pj_habla(X_NINO)]` `[with disolucion_lenta]`

**nino:** Pesa. No te estoy pidiendo ayuda.

**mc:** Entendido.

**nino:** …Esta pesa más de lo que parece.

**narrador:** Dejó la bolsa más pesada en mi brazo sin mirarme, y se llevó la otra. Ninguno dijo nada más.

`[SPR nino neutral at pj_calla(X_NINO)]`

#### E · fría

**narrador:** Nino se detuvo a dos pasos de mí, con el boletín boca abajo contra el costado. Ni cerca ni lejos.

`[SPR nino molesta at pj_habla(X_NINO)]` `[with disolucion_lenta]`

**nino:** Sigues aquí.

**mc:** Sigo.

**nino:** Pues anota la fecha. Para cuando te canses.

**narrador:** Lo dijo sin rabia. Como quien deja una nota pegada en la nevera.

`[SPR nino neutral at pj_calla(X_NINO)]`

#### E · no visitada

**narrador:** Nino se quedó junto al marco de la puerta, a media sala, como quien no ha decidido si entra.

`[SPR nino neutral at pj_habla(X_NINO)]` `[with disolucion_lenta]`

**nino:** No me mires como si me debieras algo. No viniste a buscarme. Está bien.

**nino:** Alguien tenía que ser la que no se busca. …Eso sonó mejor en mi cabeza.

**mc:** Sonó bien.

**nino:** No te pedí opinión de crítico. Treinta y cinco días no hacen una conversación.

`[SPR nino neutral at pj_calla(X_NINO)]`

---

### Assets y notas del bloque 4

**`cg_nino_examen`** — Misma cámara, luz y primer plano que `cg_nino_fracaso`: el examen de MC terminado y
boca abajo, un lápiz y el canto de una mano, desenfocados y cortados por el borde. Al fondo, Nino de perfil o
tres cuartos, **brazos sin cruzar** (allí, cruzados), la hoja **terminada y boca arriba** a un lado del pupitre
(allí, boca abajo), el lápiz todavía en una mano y la mirada de lado, hacia el resto del aula, con la mandíbula
relajada (allí, tensa). Sin texto legible. Es la única imagen del set de exámenes donde Nino no está cerrada,
y por eso es **estado-agnóstico**: es el instante *antes* de que decida si se levanta (cálida) o si cruza los
brazos y se queda (las otras tres), y ambas cosas se narran. Pelo corto y moños, como siempre.

**Sprites:** ninguno nuevo. `nino neutral`, `nino molesta` y `nino pillada` (nombres del código). `pillada` solo
en el eco cálida: es su vergüenza de haberse delatado, no una sorpresa. `nino nerviosa` queda sin usar: es de la
grieta del hub y del Final B.

**Audio:** `descubrimiento` (monólogo cálida) → `nino` (tema, en N1′) → silencio con `amb_reloj` (frase). `sfx_silla`
y `sfx_puerta_cierra` solo en G cálida, sobre silencio: no hacen falta `duck()`. `sfx_timbre` al final de los otros
tres gestos.

---

---

## BLOQUE 5 · Itsuki · Jueves · Ciencias (Mov. 5)

### N · Núcleo — `e6_itsuki_nucleo`

`[$ ui_escena("beat", "itsuki", "Aula · Ciencias")]` `[$ tiempo_restante = "dos exámenes"]`
`[BG bg_negro]` `[with fade_dia]` *(solo `amb_reloj`)*

**narrador:** Jueves. Ciencias.

`[SFX sfx_hoja volume 2.0]` `[CG NUEVO — cg_itsuki_examen]` `[scene cg_itsuki_examen · with fade]`

**narrador:** Segunda fila. Mi hoja boca abajo, el lápiz encima. Ya era costumbre.

**narrador:** Itsuki escribía con la derecha. El índice de la izquierda recorría los renglones sin tocarlos.

**narrador:** Llevaba tres líneas bien. La cuarta la leyó una vez, y otra, y otra.

**mc_pensamiento:** Una conversión de unidades. De las que se resuelven con orden y sin prisa.

**mc_pensamiento:** Ella tiene el orden. A veces le falta mirar un paso atrás.

**mc_pensamiento:** Conozco el tipo de trampa. No podía decírsela: en un examen no se habla.

---

### M · Monólogos — `e6_itsuki_mono_<estado>`

*(Pregunta cuatro: conversión de unidades, cinco pasos; el enunciado y su cadena están en el anexo. Todas las
líneas son de `itsuki_int`. Los monólogos **no revelan** dónde está el error: eso lo hace el minijuego o el
profesor. En los cuatro estados hay un punto `[CALL …beat…]`.)*

#### M · cálida — `e6_itsuki_mono_calida`

*(Foco: lo que cambió porque alguien le dijo dónde mirar y se calló. La grieta son tres fragmentos; la
recuperación, una oración seca y completa.)*

`[MUS descubrimiento fadein 2.0]`

**itsuki_int:** Pregunta cuatro. Conversión de unidades. Cinco pasos.

**itsuki_int:** Planteé bien. Convertí el caudal. Pasé al tiempo. Y el resultado no cuadra.

**itsuki_int:** Es el mismo error de siempre: en un sitio que no encuentro, con un número que reconozco.

`[CALL e6_itsuki_beat_<ayudada|sola> — dos líneas, ver «B · Capa de beat»]`

**itsuki_int:** Me dijo: «Solo te digo dónde mirar». No me dio la respuesta. Me dio una dirección.

**itsuki_int:** El primer día le dije: «Ni se te ocurra decirme la respuesta». Era una regla para él.

**itsuki_int:** Lo hice sola una vez. Salió. Eso ya lo sé. Lo que no sé es qué hago cuando no sale.

**itsuki_int:** Preguntarle a mis hermanas sería admitir…

**itsuki_int:** Preguntarle a él sería—

**itsuki_int:** Basta.

**itsuki_int:** El profesor no es ninguna de las dos cosas. Es el profesor.

**itsuki_int:** Levantar la mano no es un favor. Es un procedimiento.

`[ACTIVA e6_itsuki_mj — la última línea]`

**itsuki_int:** Tengo dos caminos, y los dos son legales. Elegiré después de revisar una vez.

#### M · tibia — `e6_itsuki_mono_tibia`

*(Foco: la tarea y una pregunta abierta, «¿qué iba a explicarme?». Silencio salvo `amb_reloj`. La frase queda
cortada; lo que sigue es la oración seca de quien se repone.)*

**itsuki_int:** Pregunta cuatro. Conversión de unidades. Cinco pasos.

**itsuki_int:** Planteé bien. Convertí el caudal. Pasé al tiempo. Y el resultado no cuadra.

**itsuki_int:** Hay un error. No sé dónde. Lo noto como una piedra en el zapato.

`[CALL e6_itsuki_beat_<ayudada|sola> — dos líneas]`

**itsuki_int:** Me ofreció revisarlo desde el principio. Dije que no antes de saber qué iba a explicarme.

**itsuki_int:** Todavía no sé qué iba a explicarme. Quizá un paso. Quizá otra cosa.

**itsuki_int:** Dije «todavía no necesito tu ayuda». Era una expresión. No era una promesa.

**itsuki_int:** …¿O sí lo era?

**itsuki_int:** Podría levantar la mano. Preguntarle al profesor. Preguntar sería—

**itsuki_int:** Revisaré desde el principio. Sola.

#### M · fría — `e6_itsuki_mono_fria`

*(Foco: la herida convertida en método. Silencio salvo `amb_reloj`. Oraciones cerradas, sin una grieta: es la
que mejor se defiende.)*

**itsuki_int:** Pregunta cuatro. Conversión de unidades. Cinco pasos.

**itsuki_int:** Planteé bien. Convertí el caudal. Pasé al tiempo. Y el resultado no cuadra.

**itsuki_int:** Revisaré cada paso, uno por uno, desde el primero. Sin ayuda.

`[CALL e6_itsuki_beat_<ayudada|sola> — dos líneas]`

**itsuki_int:** Me quitó el cuaderno de las manos. Lo resolvió de pie, con mi propio lápiz.

**itsuki_int:** Bien y rápido. No era el ejercicio lo que defendía. Era hacerlo.

**itsuki_int:** Taché su solución y escribí la mía debajo. Le dije que ya tenía lo que necesitaba de él.

**itsuki_int:** Lo mantengo.

**itsuki_int:** Resolver sola cuesta el triple. Entrego sobre la campana. No importa.

**itsuki_int:** Nadie va a decirme dónde mirar. Nadie va a decirme nada.

**itsuki_int:** No necesito preguntar.

#### M · no visitada — `e6_itsuki_mono_no_visitada`

*(Foco: la espera; responde a su `queja_itsuki` y a la azotea. Silencio salvo `amb_reloj`. Termina por dentro la
oración que dejó abierta en la queja, y aun así no cambia lo que hace.)*

**itsuki_int:** Pregunta cuatro. Conversión de unidades. Cinco pasos.

**itsuki_int:** Es del mismo tipo que el del círculo a lápiz. Reconozco la forma antes de leer los números.

**itsuki_int:** Planteé bien. Convertí el caudal. Pasé al tiempo. Y el resultado no cuadra.

`[CALL e6_itsuki_beat_<ayudada|sola> — dos líneas]`

**itsuki_int:** Repasé aquel ejercicio hasta hundir el papel. Y me atasco en el mismo punto.

**itsuki_int:** Dije que gané el juego. Una victoria que no vino a cobrar nadie.

**itsuki_int:** Pedirlo habría sido…

**itsuki_int:** No. Termino la oración. Pedirlo habría sido empezar. Y no sé dónde se para uno después.

**itsuki_int:** Si hubiera venido, no lo habría echado. No inmediatamente. Tampoco eso lo apunto.

**itsuki_int:** Lo resuelvo sola. Como siempre.

**itsuki_int:** …Tarde, pero sola.

---

### B · Capa de beat — `e6_itsuki_beat_<ayudada|sola>`

*(Dos líneas de `itsuki_int`: el eco de la azotea. La **variante** replica la condición del propio beat:
`ayudada` si Itsuki fue visitada y su rama no fue tibia, es decir, estado «calida» o «fria»; `sola` en cualquier
otro caso. La **segunda línea es común**.)*

#### B · ayudada — `e6_itsuki_beat_ayudada`

**itsuki_int:** «No hace falta que sigas viniendo a comprobar cómo voy.» Lo dije yo. Vino igual.

**itsuki_int:** Pasamos la hora sin abrir ningún libro. Fue la hora más útil del mes. No pienso decirlo.

#### B · sola — `e6_itsuki_beat_sola`

**itsuki_int:** En la azotea no le pregunté dónde había estado. Él no me lo contó. Fue un buen acuerdo.

**itsuki_int:** Pasamos la hora sin abrir ningún libro. Fue la hora más útil del mes. No pienso decirlo.

---

### J · Minijuego It1 — `e6_itsuki_mj` *(solo cálida)*

`[MUS itsuki fadein 1.0 fadeout 1.5]`
`[MJ it1 · call mj_ejecutar("it1", "itsuki") → "ganado" | "saltado"]`

*(Fallos: `MJ_FALLOS`, dichos por `itsuki_int`. El minijuego debe dejar `datos["ayuda"]` en True o False: lo lee
este bloque. El enunciado y la cadena están en el anexo.)*

`[MUS stop fadeout 3.0]` *(la frase cae con solo `amb_reloj`)*

`[SLOT A/B · e6_mj["itsuki"]["datos"].get("ayuda", True)]` *(si el minijuego se saltó, `datos` viene vacío y vale la A)*

if `e6_mj["itsuki"]["resultado"] == "saltado"`:

> **narrador:** No supe si levantó la mano o la dejó abajo. Cuando volví a mirar, la cuatro estaba resuelta.
>
> **itsuki_int:** Preguntar no es perder.

else if `ayuda == True` → **Frase A**:

> **narrador:** Levantó la mano. Despacio, con el codo recto, como se levanta algo que pesa.
>
> **profe:** ¿Sí, Nakano?
>
> **itsuki:** ¿Podría repetir el enunciado de la cuatro? Entero.
>
> **profe:** Cómo no. «…durante una hora y media de funcionamiento continuo…»
>
> **narrador:** Itsuki no esperó a que terminara. Ya había bajado la vista a su hoja.
>
> **itsuki_int:** Hora y media. Cinco mil cuatrocientos segundos. No noventa.
>
> **itsuki_int:** Preguntar no es perder.
>
> **itsuki_int:** Me dijo dónde mirar. El ejercicio lo resolví yo. Sigue siendo mío.

else (`ayuda == False`) → **Frase B**:

> **narrador:** No levantó la mano. Borró el «90» entero, con la goma, sin prisa.
>
> **narrador:** Y empezó otra vez desde la primera línea. Despacio. Sin saltarse ninguna unidad.
>
> **itsuki_int:** Una hora y media. Noventa minutos. Cinco mil cuatrocientos segundos. Ahora sí.
>
> **itsuki_int:** Me salió sola. Y tardé el doble. Las dos cosas son ciertas.
>
> **itsuki_int:** La próxima vez preguntaré.

*(La A es la que cierra el arco: la oración que antes no cerraba, «Preguntar sería—», cierra en otra dirección. La B
es una cálida de segundo orden: no pide, pero ya sabe que puede. Las dos escriben `e6_frase["itsuki"] = "completa"`.)*

---

### F · La frase de cambio

| Estado | Frase | Dónde | `e6_frase[h]` |
|---|---|---|---|
| cálida | **A** «Preguntar no es perder.» · **B** «La próxima vez preguntaré.» | J | `completa` |
| tibia | «Preguntar sería—» → «Revisaré desde el principio. Sola.» | M tibia, últimas dos | `cortada` |
| fría | «No necesito preguntar.» | M fría, última | `cerrada` |
| no visitada | «Lo resuelvo sola. Como siempre. …Tarde, pero sola.» | M no visitada, últimas dos | `espera` |

---

### P · Promesa — `e6_itsuki_promesa` *(solo no visitada)*

*(Pensamiento silencioso de MC. Usa solo lo que MC sabe por su `queja_itsuki` y por la azotea.)*

**mc_pensamiento:** Subió a la azotea con un cuaderno y no lo abrió. Yo estaba ahí.

**mc_pensamiento:** Dijo que si hubiera ido a buscarla no me habría echado. No inmediatamente. Y que no lo apuntara.

**mc_pensamiento:** No lo apunté. Pero voy a subir con comida para dos, y a pedirle que suba ella sin el cuaderno. Una vez.

---

### G · Gestos — `e6_itsuki_gesto_<estado>`

*(Espejo de B3.4: allí llevaba tres líneas bien, la cuarta se la comía, me miraba un segundo, apartaba la vista y
«no preguntó. Preguntar habría sido darme la razón». Aquí cada estado cambia un detalle distinto de esa mirada.)*

#### G · cálida

**narrador:** Entregó con cuatro minutos de sobra. La cuarta tenía una sola raya, prolija.

**narrador:** Al pasar junto a mi pupitre me miró un segundo. Esta vez no apartó la vista.

**narrador:** Asintió una vez, seca, como quien confirma un dato y no pide aplauso.

**mc_pensamiento:** Hace un mes apartar la mirada era su forma de no deberme nada. Hoy mirar era no ocultar nada.

**mc_pensamiento:** No necesitó que yo le dijera dónde mirar. Ya sabía dónde. Y a quién preguntar, si hacía falta.

`[SFX sfx_timbre volume 1.5]` `[MUS stop]` *(si aún suena algo)*

#### G · tibia

**narrador:** Entregó sobre la campana, con la cuarta tachada y reescrita dos veces.

**narrador:** A media hoja había levantado la vista. Me miró un segundo. Apartó la mirada y volvió al papel.

**mc_pensamiento:** Pudo preguntar. Eligió tardar. Con ella, tardar también es una forma de orgullo.

**mc_pensamiento:** Revisó desde el principio, sola. Apretaba el lápiz no por rabia, sino por método.

`[SFX sfx_timbre volume 1.5]`

#### G · fría

**narrador:** Entregó sobre la campana. La hoja, impecable. Ni una pregunta, ni una mirada.

**narrador:** Al terminar cerró el cuadernillo del examen con las dos manos, como cierra su cuaderno.

**mc_pensamiento:** No levantó la vista ni una vez. Ni para odiarme.

**mc_pensamiento:** Resolvió sola. Es lo único que no iba a dejar que nadie le quitara. Esta vez nadie lo intentó.

`[SFX sfx_timbre volume 1.5]`

#### G · no visitada

**narrador:** Entregó pasada la campana, con la cuarta recién resuelta. Tarde, pero resuelta.

**narrador:** A media hoja había levantado la vista. Me miró un segundo, y apartó la mirada.

**mc_pensamiento:** La miré yo primero. Ella apartó la vista, como si hubiera algo que no estaba lista para devolverme.

**mc_pensamiento:** Nunca me pidió nada. Y yo nunca fui. Los dos dejamos la misma pregunta sin hacer.

`[SFX sfx_timbre volume 1.5]`

---

### E · Ecos (Mov. 8) — `e6_itsuki_eco_<estado>`

*(Entra ya con `[SPR itsuki neutral at pj(X_ITSUKI)]`. Las hermanas presentes van en `pj_calla`. No cita notas, no
alude al orden de salida y **termina antes** del intento de disculpa del núcleo: no dice «primer día» ni
«asiento» ni «perdón». Termina en `pj_calla`.)*

#### E · cálida

**narrador:** Itsuki llegó con el bolígrafo del examen todavía en la mano. Se le había olvidado soltarlo.

`[SPR itsuki neutral at pj_habla(X_ITSUKI)]` `[with disolucion_lenta]`

**itsuki:** Dije que el juego se acabó. No dije quién ganó.

**mc:** ¿Y quién ganó?

**itsuki:** Eso no se pregunta.

`[SLOT · e6_mj["itsuki"]["datos"].get("ayuda", True)]`

if `ayuda == True`:

> **itsuki:** Levanté la mano en un examen. Es un informe, no una invitación a aplaudir.

else:

> **itsuki:** No levanté la mano. Pero ya sé que puedo. Es un informe, no una invitación a aplaudir.

`[SPR itsuki neutral at pj_calla(X_ITSUKI)]`

#### E · tibia

**narrador:** Itsuki llegó con el boletín doblado por la mitad y el gesto de quien ya revisó dos veces.

`[SPR itsuki neutral at pj_habla(X_ITSUKI)]` `[with disolucion_lenta]`

**itsuki:** Aquel día dijiste «revisarlo desde el principio». …¿Qué ibas a—

**narrador:** Se detuvo. La oración se quedó abierta, sin sujeto. En ella, eso es casi un grito.

**mc:** Cuando quieras.

**itsuki:** …No dije que quisiera.

`[SPR itsuki neutral at pj_calla(X_ITSUKI)]`

#### E · fría

**narrador:** Itsuki llegó con el boletín en una mano y el puño cerrado sobre el bolígrafo del examen.

`[SPR itsuki molesta at pj_habla(X_ITSUKI)]` `[with disolucion_lenta]`

**itsuki:** Revisé desde el principio. Sola. Sale igual que si me lo hubieran resuelto. La diferencia es mía.

**mc:** Lo sé.

**itsuki:** No tienes que saberlo. …Es solo que cuenta.

`[SPR itsuki neutral at pj_calla(X_ITSUKI)]`

#### E · no visitada

**narrador:** Itsuki esperaba de pie junto a su sitio, con el cuaderno de ciencias cerrado bajo la mano.

`[SPR itsuki neutral at pj_habla(X_ITSUKI)]` `[with disolucion_lenta]`

**itsuki:** Dije que el juego se acabó, y gané. Es lo único que siempre me sale bien.

**mc:** No sabía que había premio.

**itsuki:** No lo hay. …Por eso es lo único que me sale.

**narrador:** Lo dijo con la oración cerrada, con su punto. Pero el punto quedó flojo.

`[SPR itsuki neutral at pj_calla(X_ITSUKI)]`

---

### Assets y notas del bloque 5

**`cg_itsuki_examen`** — Misma cámara, luz y primer plano que `cg_itsuki_fracaso`: el examen de MC terminado y
boca abajo, un lápiz y el canto de una mano, desenfocados y cortados por el borde. Al fondo, Itsuki **escribiendo**
con la derecha, el lápiz en movimiento (allí, apoyado y quieto), la mirada **en su hoja** (allí, de reojo hacia
cámara) y la espalda recta, con los hombros abiertos y no tensos. El detalle que la distingue a un 30 %: el
**índice de la mano izquierda apoyado sobre un renglón de la hoja, señalando sin tocar** —eco literal del «solo te
digo dónde mirar»—. La hoja trae cuatro líneas limpias y una sola raya horizontal prolija. Ahoge y pelo largo
cayendo sobre el hombro; expresión neutra. Sin texto legible. **Estado-agnóstico**: el dedo sobre el renglón vale
igual si va a preguntar, si va a tardar o si va a negarse; lo que decide cada caso es el texto.

**Sprites:** ninguno nuevo. `itsuki neutral` y `itsuki molesta` (nombres del código). `itsuki timida` y
`itsuki sorprendida` quedan sin usar. En el eco cálida se podría subir un `itsuki timida` en «No dije quién ganó»:
rompe la regla de que `timida` es solo de la grieta, y el código ya la rompe en `reaccion_itsuki`; **no lo pido**.

**Audio:** `descubrimiento` (monólogo cálida) → `itsuki` (tema, en It1) → silencio con `amb_reloj` (frase). Todo lo
demás, solo el reloj. `sfx_timbre` al cierre de cada gesto.

---

---

## Anexo · Textos y datos para los minijuegos

*(Los escribe este chat porque nadie más los escribe: el chat 5 los toma tal cual o los ajusta. Mismo criterio que
el anexo de I1′ en los bloques A.)*

### N1′ · Cinco listas y un sexto hueco (para el chat 5)

**Qué ve el jugador.** Cinco listas de **tres artículos** y, después, un sexto hueco. Los artículos se muestran
en **inglés**, y el estante ofrece el correcto más hasta tres rótulos casi iguales: hay que **leer con cuidado y
elegir el que coincide exactamente**. La traducción al español se escribe sola, en gris, junto al artículo (a los
1,4 s, a los 0,5 s o al instante, según el nivel): Nino traduce sin darse cuenta, y ninguna mecánica le pide
traducir. Distractores por estante: **3** en difícil, **2** en media, **1** en asistida (los primeros de su fila).

| Lista | Para | Artículo (correcto) | Traducción | Distractores, en orden de aparición |
|---|---|---|---|---|
| 1 | Ichika · pancakes | all-purpose flour | harina de todo uso | self-rising flour · cake flour · bread flour |
| | | unsalted butter | mantequilla sin sal | salted butter · whipped butter · clarified butter |
| | | maple syrup | jarabe de arce | pancake syrup · golden syrup · corn syrup |
| 2 | Yotsuba · desayuno de pista | rolled oats | copos de avena | instant oats · steel-cut oats · oat flour |
| | | whole milk | leche entera | skim milk · evaporated milk · condensed milk |
| | | ripe bananas | plátanos maduros | green bananas · plantains · banana chips |
| 3 | Miku · té y galletas | green tea | té verde | roasted green tea · jasmine tea · matcha powder |
| | | shortbread | galletas de mantequilla | shortcake · digestive biscuits · graham crackers |
| | | soy milk | leche de soja | almond milk · oat milk · rice milk |
| 4 | Itsuki · hamburguesas | ground beef | carne molida | lean ground beef · minced pork · ground turkey |
| | | burger buns | panes de hamburguesa | dinner rolls · hot dog buns · sandwich bread |
| | | sharp cheddar | cheddar curado | mild cheddar · cream cheese · sliced cheese |
| 5 | Nino · *(sin nombre de plato)* | vanilla extract | extracto de vainilla | vanilla essence · vanilla paste · vanilla sugar |
| | | confectioners' sugar | azúcar glas | granulated sugar · caster sugar · brown sugar |
| | | heavy cream | nata para montar | whipping cream · light cream · sour cream |

La lista de Nino **no nombra el plato** a propósito, y repite dos rótulos que ella leyó sin esfuerzo en el centro
comercial (`vanilla extract`, `confectioners' sugar`). No se asocia a ninguna receta ni se nombra la tarjeta: la
tarjeta de receta sigue intacta para el Capítulo 2.

**El sexto hueco.** Tras la lista 5, el tiempo se detiene y aparece un renglón vacío rotulado «LISTA 6 · ???».
Hay **tres acciones, todas válidas y todas ganan**; ninguna es «la correcta». Sirven para que el jugador elija
el matiz de **una** línea. Ninguna es «tachar»: eso sería adelantar el golpe, que es lo que Nino deja de hacer.

| Acción | Botón | Valor de `datos["sexto"]` |
|---|---|---|
| Escribir un artículo | «Escribir "una taza más"» | `"taza"` |
| No escribir nada | «Dejarlo en blanco» | `"blanco"` |
| Dejarlo para después | «Anotar "cuando se sepa"» | `"cuando"` |

**Microtextos.**

| Elemento | Texto |
|---|---|
| Rótulo de lista | «LISTA 1/5 · Ichika» · «2/5 · Yotsuba» · «3/5 · Miku» · «4/5 · Itsuki» · «5/5 · Nino» |
| Acierto | «Ese.» |
| Error | «No. Lee otra vez.» (penaliza según nivel) |
| Traducción | Sale sola, en gris, con la etiqueta «(sin darse cuenta)» solo en el tutorial del primer uso |
| Fin de la lista 5 | «Cinco listas. Falta una línea.» |
| Sexto hueco | «¿Y la sexta?» |

**El minijuego debe devolver** `{"resultado": "ganado", "progreso": …, "datos": {"sexto": "taza" | "blanco" | "cuando"}}`.
Si se salta, `datos` viene vacío y el bloque usa `"blanco"`.

### It1 · Conversión de unidades (para el chat 5)

**Enunciado de la pregunta 4.** «Un depósito se llena con un caudal de 0,45 L/s durante 1 h 30 min. Considera que
1 L de agua pesa 1 kg.»

**La cadena** (cinco pasos en difícil; la pregunta final cambia con el nivel):

| Paso | Pide | Resultado correcto | Trampa |
|---|---|---|---|
| 1 | Pasa 1 h 30 min a minutos | 90 min | — |
| 2 | Pasa los minutos a segundos | 5400 s | **90** (el valor arrastrado sin convertir) |
| 3 | Caudal × tiempo, en litros | 2430 L | **243** (coma mal puesta) — solo en difícil |
| 4 | Pasa los litros a kilogramos | 2430 kg | — |
| 5 | Pasa los kilogramos a toneladas | 2,43 t | — |

- **Difícil:** 5 pasos, dos trampas (90 y 243). Pregunta final: «¿Cuántas toneladas?».
- **Media:** 4 pasos, una trampa (90). Pregunta final: «¿Cuántos kilogramos?» (se quita el paso 5).
- **Asistida:** 3 pasos, una trampa **marcada** (90). Pregunta final: «¿Cuántos litros?» (se quitan los pasos 4 y 5).

**El fantasma.** El **90** del primer intento aparece en gris en el margen derecho de la hoja, con la etiqueta
«(primer intento)», y se ofrece como respuesta del paso 2. Es lo que Itsuki hace siempre: arrastra el número del
medio sin convertirlo. Elegirlo es el error.

**«Levantar la mano».** Botón. Consume el coste de tiempo del nivel y **resalta el paso 2** con el texto «El profesor
repite el enunciado: dice “hora y media”, no “noventa”.». **No da la respuesta.** Deja `datos["ayuda"] = True`. Si
el jugador termina sin usarlo, `datos["ayuda"] = False`.

**Indicador de plausibilidad** (media y asistida): bajo cada paso, «Magnitud plausible.» o «Eso no se llenó en hora y
media.» (para un resultado como 40,5 L).

**Microtextos.**

| Elemento | Texto |
|---|---|
| Cabecera | «CIENCIAS · PREGUNTA 4» |
| Rótulo de paso | «PASO 1/5» … «PASO 5/5» (el total baja a 4 o 3 según el nivel) |
| Acierto | «Cuadra.» |
| Error | «Las unidades no se cancelan.» |
| Botón | «Levantar la mano» |

**El minijuego debe devolver** `{"resultado": "ganado", "progreso": …, "datos": {"ayuda": True | False}}`.

### `MJ_FALLOS` — listo para pegar

Sustituye **solo** las claves `nino` e `itsuki` del `define MJ_FALLOS` de `10_minijuegos.rpy`. Yotsuba, Ichika y
Miku están en el anexo de `CAP1_evento_6_bloques_A.md`. El primer elemento es quién habla (`"int"` = la voz interior
de la hermana); el índice es el número de fallos, y a partir del tercero se repite el último.

```renpy
    "nino":    [("int", "Tsk."), ("int", "…Otra vez. No mires."), ("int", "Otra vez. Cabeza fría.")],
    "itsuki":  [("int", "Revisaré desde el principio."), ("int", "Revisaré desde el principio. Otra vez."), ("int", "Revisaré desde el principio. Sin enfadarme.")],
```

El fallo es carácter, no castigo: Nino pasa de maldecir a la orden seca y a su propia consigna («cabeza fría»);
Itsuki repite la misma frase, y a la tercera la dice sin enfado.

---

## Assets nuevos

| Asset | Tipo | Estado | Nota |
|---|---|---|---|
| `cg_nino_examen` | CG | pendiente | POV de MC, espejo de `cg_nino_fracaso`. Brazos sin cruzar, hoja terminada boca arriba. Estado-agnóstico |
| `cg_itsuki_examen` | CG | pendiente | POV de MC, espejo de `cg_itsuki_fracaso`. Escribiendo, índice sobre un renglón. Estado-agnóstico |

Generar estos dos **en la misma sesión** que los tres del chat 3 (`cg_yotsuba_examen`, `cg_ichika_examen`,
`cg_miku_examen`), con las semillas de sus `*_fracaso`, para que las cinco se lean como un set. Los prompts los
escribe el chat 7.

**Sprites nuevos: ninguno.** Opcionales para el Capítulo 2 (P-23), **no pedidos**: `nino suelta` (hombros caídos,
brazos descruzados, sin rubor: en el eco cálida lo cubre `pillada`) e `itsuki serena`.

**Reutilizados sin tocar:** `nino neutral/molesta/pillada`, `itsuki neutral/molesta`; temas `nino` e `itsuki`;
`descubrimiento`; `amb_reloj`; `sfx_hoja`, `sfx_timbre`, `sfx_silla`, `sfx_puerta_cierra`.

---

## Flags

No hay variables nuevas. Lo que escriben estos bloques, ya existente:

| Variable | Qué escribe | Quién |
|---|---|---|
| `e6_frase[h]` | `completa` / `cortada` / `cerrada` / `espera`, según el estado | `e6_marcar_ganchos` (no lo escriben las líneas) |
| `e6_promesas` | `"nino"` e `"itsuki"` si no visitadas, en el orden de examen | `e6_marcar_ganchos` |
| `e6_mj[h]["datos"]` | `{"sexto": …}` para Nino y `{"ayuda": …}` para Itsuki | Los minijuegos (chat 5) |

**Contenido de cada promesa, para el Capítulo 2** (sin que el capítulo gire alrededor de esto):

| Hermana | Promesa de MC |
|---|---|
| Nino | Ir al pasillo de importados del centro comercial y cargar una cesta que ella no le haya pedido |
| Itsuki | Subir a la azotea con comida para dos y pedirle que suba ella sin el cuaderno, una sola vez |

**Frases cortadas para el Capítulo 2** (`e6_frase == "cortada"`): Nino «Quizás esta vez no—» e Itsuki
«Preguntar sería—». Cada una se completa, si procede, en su propio evento del Capítulo 2.

**Quién lo lee después.** `e6_mj["itsuki"]["datos"]["ayuda"]` distingue la frase A de la B para el Capítulo 2, si
interesa. No hace falta para el cierre de este.

---

## Notas de implementación

- **Orden de llamada.** `e6_bloque(h)` ya llama en el orden correcto (núcleo → mono → mj si cálida → promesa si
  no visitada → `e6_marcar_ganchos` → gesto). Los ecos los llama `e6_cinco`.
- **Cinco labels nuevos fuera del contrato:** `e6_nino_beat_calida`, `e6_nino_beat_tibia`, `e6_nino_beat_fria`,
  `e6_itsuki_beat_ayudada` y `e6_itsuki_beat_sola`. Se llaman **desde dentro** de cada uno de los cuatro `*_mono_*`,
  en el punto marcado `[CALL …]`. Sin ternarios:

  ```renpy
      ## En cada e6_nino_mono_<estado>:
      call expression ("e6_nino_beat_" + nino_rama_beat)

      ## En cada e6_itsuki_mono_<estado>:
      if e6_estado_de("itsuki") == "calida" or e6_estado_de("itsuki") == "fria":
          call e6_itsuki_beat_ayudada
      else:
          call e6_itsuki_beat_sola
  ```

- **Lectura de los datos de los minijuegos.** `e6_mj` se rellena en `mj_cerrar`. Se lee justo después del
  `call mj_ejecutar`, antes de cualquier otro `call` que pise `_return`:

  ```renpy
      ## e6_nino_mj
      call mj_ejecutar(E6_MJ_JUEGO["nino"], "nino")
      $ e6_sexto = e6_mj["nino"]["datos"].get("sexto", "blanco")

      ## e6_itsuki_mj
      call mj_ejecutar(E6_MJ_JUEGO["itsuki"], "itsuki")
      $ e6_ayuda = e6_mj["itsuki"]["datos"].get("ayuda", True)
  ```

  El eco de Itsuki (Mov. 8) lee otra vez `e6_mj["itsuki"]["datos"]`: no depende de `e6_ayuda`, que se pisa al
  cambiar de label.
- **`E6_MJ_JUEGO`.** Hoy apunta todo a `"prueba"`. Cuando existan los minijuegos reales, cambiar a
  `nino: "n1"` e `itsuki: "it1"` (chat 5).
- **Dificultad.** `mj_nivel()` ya lee `nino_rama_beat`: «media» si `calida`. No hay nada que cambiar en código.
- **`tiempo_restante`.** Nino fija `"tres exámenes"` e Itsuki `"dos exámenes"`.
- **Transición entre días.** Cada gesto cierra con `sfx_timbre`; el núcleo siguiente abre con `bg_negro` + `fade_dia`.
  `amb_reloj` no se corta entre bloques: solo lo corta el Mov. 7.
- **`duck()`.** Ningún bloque lo necesita: los efectos caen sobre silencio (solo `amb_reloj`, que va por otro canal).
- **Todo `show` lleva posición.** Solo aparecen sprites en los ecos y todos usan `pj_habla` / `pj_calla` con su `X_*`.
- **Después de un CG.** En los bloques no hay `show` tras el CG: las líneas de MC en los gestos van con el CG puesto.
- **Galería.** Descomentar `("cg_nino_examen", "Examen · Inglés")` y `("cg_itsuki_examen", "Examen · Ciencias")`
  en las pestañas de cada hermana. Rediseñar la Galería para que los `*_fracaso` no cuenten para el 100 % queda
  fuera de este documento (P-17).
- **Móvil (P-20).** Nada de estos bloques depende de un minijuego para tener sentido: con
  `persistent.mj_modo = "saltar"` las ramas `if saltado` cubren el puente, el sexto hueco vale `"blanco"` y la
  ayuda vale `True` (frase A).
- **Longitud.** Ninguna línea de diálogo, narrador o pensamiento pasa de ~100 caracteres. Si con la tipografía
  definitiva alguna desborda, se parte; no se baja el tamaño.

---

## Dudas abiertas

| ID | Duda | Dónde mirarla | Qué propuse |
|---|---|---|---|
| **D-01** | El prompt del chat decía que Nino «puede llegar a no confío… todavía», pero la versión **DECIDIDA** de P-14 (la tuya) pide que ya confíe y no lo admita. Son incompatibles en el «todavía». | M de Nino (los cuatro estados) · E cálida | Gana tu versión. Nunca «confío» ni «no confío… todavía»: la confianza se ve en que cuenta los días, no se sale del chat y, en cálida, entrega y sale. Su negación más fuerte es «Eso no es confiar. Es llevar la cuenta». Si prefieres el «todavía», hay que cambiar solo dos líneas de M cálida |
| **D-02** | El «treinta y cinco días» no cuadra con el «Treinta días» que Nino dice el lunes en el núcleo si se dice el mismo día. | E cálida de Nino · M no visitada | Lo resolví por cronología: lunes 30 (núcleo) → miércoles 32 (interior de Nino) → sábado 35 (eco). Si el Mov. 7 se mueve de día, mover los números |
| **D-03** | Los minijuegos deben **devolver datos** nuevos: `datos["sexto"]` (Nino) y `datos["ayuda"]` (Itsuki). El marco ya los guarda en `e6_mj[h]["datos"]`, pero el chat 5 tiene que escribirlos. | Anexo | Dejado en el contrato de cada minijuego. Con valores por defecto si se salta |
| **D-04** | Escribí aquí las cinco listas de N1′ y la cadena de It1 porque nadie más las escribe. | Anexo | El chat 5 las toma tal cual o las ajusta. Los números de It1 están calculados: 0,45 × 5400 = 2430 |
| **D-05** | La capa B no es un label del contrato: introduce cinco labels nuevos que se llaman desde dentro de los monólogos. | Notas de implementación | Así no se toca `e6_bloque`. Si prefieres que lo llame el despachador, es un cambio de dos líneas en el chat 9 |
| **D-06** | El eco cálida de Itsuki tiene una variante condicional (con o sin ayuda) y el eco de Nino cálida roza las 5 líneas del contrato. | E de ambas | Las dos caben en 5 líneas contando la variante como una |
| **D-07** | Los gestos de Nino en tibia, fría y no visitada **reproducen casi literal** los de B3.3 (giraba la hoja, cruzaba los brazos). Quien vio el Final B lo reconoce, y es intencional (Anexo A del análisis), pero quien no lo vio lo lee como una conducta normal de Nino. | G de Nino | Mantenido. Funciona sin haber visto el B |
| **D-08** | El CG de Nino es estado-agnóstico y la muestra con los brazos sin cruzar justo antes de decidir; en tres de cuatro estados se cruzan en la línea siguiente. | `cg_nino_examen` | Aceptado: la imagen es el instante previo a la decisión, no la decisión |
| **D-09** | El «dedo sobre el renglón» del CG de Itsuki repite el gesto de MC del hub («señalé la línea con el dedo, sin tocar el papel»). Funciona como eco, pero obliga a que la imagen no sea ambigua. | `cg_itsuki_examen` | Cuidarlo en el prompt (chat 7) |
| **D-10** | No añadí capa de déjà vu por `persistent.final_malo_temprano_b_visto`: el núcleo ya trae tres (P-17) y estos bloques ya se reflejan en el B por estructura. | — | Si quieres una cuarta, la mejor candidata es G cálida de Nino («Se fue sin vigilarlas») |
