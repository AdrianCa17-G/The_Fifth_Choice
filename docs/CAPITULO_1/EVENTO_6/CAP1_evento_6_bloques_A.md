## Evento 6 · Guion de bloques A — Yotsuba, Ichika y Miku

> **Ruta en el repo:** `docs/CAPITULO_1/EVENTO_6/CAP1_evento_6_bloques_A.md`
> **Escrito.** Assets pendientes: tres CG (`cg_yotsuba_examen`, `cg_ichika_examen`, `cg_miku_examen`) y un sprite condicional (`miku sonrie`).
> Cubre los **Mov. 2, 3 y 6** del Evento 6 y los **doce ecos del Mov. 8** que corresponden a estas tres hermanas.
> Los Mov. 4 y 5 (Nino e Itsuki) son del chat 4. El marco, S1/S2/S3 y los demás ecos están en `CAP1_evento_6_nucleo.md`.

Marcadores como en el núcleo. `[BG]` fondo · `[CG]` ilustración · `[SPR]` sprite ·
`[MUS]` música · `[SFX]` efecto · `[AMB]` ambiente · `[$]` línea de código ·
`[NUEVO]` asset que no existe todavía · `[MJ]` llamada a minijuego · `[ECO]` bloque del Mov. 8.

Hablantes: `narrador`, `mc`, `mc_pensamiento`, `profe` y, para la voz interior, `yotsuba_int`, `ichika_int` y `miku_int` (ya definidos en `00_definiciones.rpy`).

---

### Decisiones de estos bloques

**El orden de lectura de un bloque es el de `e6_bloque`.** Núcleo → monólogo → minijuego (solo cálida) → promesa (solo no visitada) → gesto. El eco no forma parte del bloque: lo llama `e6_cinco` en el Mov. 8. La frase de cambio no tiene label propio: vive dentro del monólogo (tibia, fría, no visitada) o del minijuego (cálida), y `e6_marcar_ganchos` escribe `e6_frase[h]` por estado, no por línea.

**La voz interior se explica una sola vez, en el núcleo de Yotsuba.** Es el primer bloque, así que ahí cae la línea que enseña el código («En un examen nadie habla. Eso no quiere decir que nadie piense»). Ichika y Miku no la repiten.

**El recurso formal de cada una es una puntuación, y la puntuación dice quién habla.**
- **Yotsuba:** la exclamación es su armadura. Desaparece cuando dice la verdad y vuelve cuando vuelve la armadura. En la fría vuelve *sin motivo*, repetida, y sobra una.
- **Ichika:** la exclamación es la máscara. Sus frases sinceras no la llevan; la humorada que escapa antes de la verdad, sí.
- **Miku:** los puntos suspensivos son el escudo. Todo el monólogo cálida empieza con «…» hasta que se suelta; al soltarse, el «…» no vuelve y el «perdón» no llega.

**Cada monólogo lleva un eco literal de lo que MC hizo (o dejó de hacer).** Se cita lo que MC *dijo de verdad* en la rama, no el texto del menú: en `yotsuba_m4a` el menú dice «Tú vales tanto…» pero MC nunca lo pronuncia, así que el eco es «tu punto de partida no es cero».

**Los CG son estado-agnósticos.** La imagen no decide si ella está bien o mal: lo dice el texto. Por eso los CG llevan cara neutra y las diferencias entre cálida / tibia / fría / no visitada van en gesto, voz y narración.

**Música.** Cálida: `descubrimiento` durante el monólogo → el tema de la hermana en el minijuego → silencio con solo `amb_reloj` cuando cae la frase de cambio. En el resto de estados no suena nada: el tema solo suena si cálida y el jugador *oye* a quién alcanzó. `amb_reloj` ya está sonando desde el Mov. 1.

**Las promesas son silenciosas.** Son pensamientos de MC durante el examen (nadie habla en un examen). Coincide con la libreta del Mov. 10: «Dos promesas hechas sin que nadie me las pidiera». Cada una usa solo lo que MC sabe por la `queja_*` de esa hermana.

**Nada de puntos, nada de disculpa de Itsuki.** Los bloques no llaman a `sumar_punto`. Itsuki aparece solo como destinataria de una mirada de Yotsuba.

**No se repite `beat_casa` ni `reaccion_*`.** Se *cobra* lo sembrado ahí, con frases nuevas. Evitado a propósito: «siete y cuarto / redondeo hacia arriba» y «¿quién cuida de ti?» (Ichika), «alguien se pasó la noche en mi tema» (Miku), el diálogo del «1» con el corazón torcido (Yotsuba).

**Longitud.** Ninguna entrada pasa de ~100 caracteres (dos líneas de caja).

**Sin capa de déjà vu por `persistent` (P-17).** El núcleo ya tiene tres. Estos bloques no añaden más.

---

### Cobros obligatorios — dónde está cada uno

| Hermana | Cobro | Dónde |
|---|---|---|
| Yotsuba | «Uno por ciento» | N (observación de MC) |
| | Veintiocho, el número perfecto | M cálida (líneas 6–9) · J · microtextos de Y2 |
| | «1» → «100» en la muñeca (solo cálida) | E cálida |
| | «¿Qué siente el protagonista cuando se queda solo?» | M en los cuatro estados |
| Ichika | Problema de trenes | N · M cálida (1–2) · M tibia (1) · M no visitada (1) |
| | Papel nuevo | M cálida (9) · J · E cálida |
| | «Estoy bien» | M cálida (7) · I1′ línea 2 · F fría · E fría |
| Miku | Sal y rutas de comercio | N · M en los cuatro estados |
| | Página 120 con su primera sonrisa | E cálida |
| | «Mucho más—» terminada | J |
| | Primera línea sin «…» y sin «perdón» detrás | J |
| | Goma entera | N · G cálida |
| | «Perdón → Perd— → Otra vez» | `MJ_FALLOS` (anexo) |

---

---

## BLOQUE 1 · Yotsuba · Lunes · Japonés (Mov. 2)

### N · Núcleo — `e6_yotsuba_nucleo`

*(Todos los estados. Entra desde el Mov. 1: `amb_reloj` ya suena; sin música. El `scene` del CG retira solo la formación de las cinco.)*

`[$ ui_escena("beat", "yotsuba", "Aula · Japonés")]` `[$ tiempo_restante = "cinco exámenes"]`
`[CG NUEVO — cg_yotsuba_examen]` `[scene cg_yotsuba_examen · with dissolve]`

**narrador:** Lunes. Japonés. La primera de cinco hojas.

**narrador:** Mi pupitre quedaba en la segunda fila, junto al pasillo. Desde ahí se veían las cinco nucas.

**narrador:** Terminé el mío antes de la mitad. Lo dejé boca abajo, con el lápiz encima.

**mc_pensamiento:** Ahora solo me quedaba mirar.

**narrador:** En un examen nadie habla. Eso no quiere decir que nadie piense.

**narrador:** Yotsuba escribió su nombre primero. Siempre lo hace.

**mc_pensamiento:** El uno por ciento del primer día, bien hecho. Esta vez era solo el principio de la hoja.

---

### M · Monólogos — `e6_yotsuba_mono_<estado>`

#### M · cálida — `e6_yotsuba_mono_calida`

*(Foco: lo que cambió porque alguien la vio. Sin signos de exclamación en todo el monólogo.)*

`[MUS descubrimiento fadein 2.0]`

**yotsuba_int:** Pregunta uno. ¿Qué siente el protagonista cuando se queda solo?

**yotsuba_int:** Lo sé. Conté veintitrés vueltas sola, y alguien llevaba ocho mirándome.

**yotsuba_int:** Me dijo que mis hermanas no hacen lo que yo hago. Que él tampoco. Y que lo intenta.

**yotsuba_int:** Me dijo que mi punto de partida no era cero. Que nunca lo fue.

**yotsuba_int:** Dijo que es pésimo animando a la gente. Y me animó igual.

**yotsuba_int:** Veinticinco no es un número perfecto. Lo busqué: el perfecto es el veintiocho.

**yotsuba_int:** Sus divisores son uno, dos, cuatro, siete y catorce. Cinco números. Suman veintiocho.

**yotsuba_int:** Cinco números distintos, y ninguno sobra. Si falta uno, la cuenta no cierra.

**yotsuba_int:** Yo siempre pensé que era el uno. El más pequeño. El que nadie cuenta.

`[ACTIVA e6_yotsuba_mj — las dos últimas líneas]`

**yotsuba_int:** Me falta la segunda línea de la respuesta: qué pasa cuando alguien llega. Esa no me sale.

**yotsuba_int:** Un relevo no se gana corriendo más que nadie. Se gana recibiendo bien. Vamos.

#### M · tibia — `e6_yotsuba_mono_tibia`

*(Foco: la tarea y una pregunta abierta, «¿me ayudó o solo me dejó correr?». Silencio salvo `amb_reloj`. La frase queda cortada.)*

**yotsuba_int:** Pregunta uno. ¿Qué siente el protagonista cuando se queda solo?

**yotsuba_int:** Un minuto con diecisiete. Después, catorce. Tres segundos menos.

**yotsuba_int:** Dijo «claro, dame el cronómetro» sin preguntar nada más.

**yotsuba_int:** No sé si me sirvió que alguien mirara o si solo me dejó correr.

**yotsuba_int:** Las piernas me avisan siempre. Hoy no me avisan de nada.

**yotsuba_int:** Si termino rápido, ¿alguien va a necesitarme para algo?

**yotsuba_int:** Ichika duerme poco. Nino cocina. Miku ya sabe. Itsuki estudia.

**yotsuba_int:** Yo corro y animo, y en un examen no se anima a nadie.

**yotsuba_int:** Escribo que el protagonista se queda solo y espera. Eso sí lo sé.

**yotsuba_int:** Yo también im—

**yotsuba_int:** ¡Pregunta dos!

#### M · fría — `e6_yotsuba_mono_fria`

*(Foco: la herida convertida en método. Silencio salvo `amb_reloj`. La armadura grita dos veces.)*

**yotsuba_int:** Pregunta uno. ¿Qué siente el protagonista cuando se queda solo?

**yotsuba_int:** «Entonces concéntrate en correr. Si es lo tuyo, hazlo bien.» Eso dijo.

**yotsuba_int:** Pues lo hago bien. Escribo lo justo.

**yotsuba_int:** Antes miraba a Ichika, a Miku, a Itsuki. Mirar es perder tiempo. Ya no miro.

**yotsuba_int:** Dejé de contar las vueltas en voz alta. Ya no me hace falta.

**yotsuba_int:** Nadie me pidió que me callara. Solo que me concentrara.

**yotsuba_int:** Escribo que el protagonista se queda solo. Y ya está. Una línea. Con eso basta.

**yotsuba_int:** Lo mío es correr. Está bien.

**yotsuba_int:** ¡Está bien!

**yotsuba_int:** Pregunta dos.

#### M · no visitada — `e6_yotsuba_mono_no_visitada`

*(Foco: la espera y el grupo; responde a su `queja_yotsuba`. Silencio salvo `amb_reloj`.)*

**yotsuba_int:** Pregunta uno. ¿Qué siente el protagonista cuando se queda solo?

**yotsuba_int:** Sé cómo se siente esperar. Entrené quince minutos más cada tarde, por si venía.

**yotsuba_int:** Cronometré dos vueltas de más. Por si acaso. Las conté.

**yotsuba_int:** No vino. No pasa nada. Tres tardes no alcanzan para cinco. Eso lo entiende cualquiera.

**yotsuba_int:** Si nadie me necesita, ¿para qué me sobra tanta energía?

**yotsuba_int:** Entonces la reparto. Tres vueltas de ventaja para cuando venga. Si viene.

**yotsuba_int:** Escribo que el protagonista espera a alguien y no sabe si llega.

**yotsuba_int:** Es una buena respuesta. Y es la única que no puedo comprobar.

---

### J · Minijuego Y2 — `e6_yotsuba_mj` *(solo cálida)*

`[MUS yotsuba fadein 1.0 fadeout 1.5]`
`[MJ y2 · call mj_ejecutar("y2", "yotsuba") → "ganado" | "saltado"]`

*(Fallos: ver `MJ_FALLOS` en el anexo. Se dicen con `yotsuba_int`.)*

`[MUS stop fadeout 3.0]` *(la frase cae con solo `amb_reloj`)*

**narrador:** Yotsuba soltó el lápiz un segundo y respiró hondo, como se respira al acabar una serie.

**yotsuba_int:** Cada tramo mide lo mismo. Ninguna carrera la gana una sola.

**yotsuba_int:** Yo importo igual que mis hermanas.

**yotsuba_int:** Y el testigo no pesa menos por pasar por mis manos.

**yotsuba_int:** Segunda línea: el protagonista quería que alguien llegara. Y alguien llegó.

**yotsuba_int:** ¡Pregunta dos!

if `_return == "saltado"`:

> **narrador:** Hay carreras que se corren por dentro. Esta la corrió entera, de un tirón.

---

### F · La frase de cambio

| Estado | Frase | Dónde | `e6_frase[h]` |
|---|---|---|---|
| cálida | «Yo importo igual que mis hermanas.» *(sin signos; la exclamación vuelve después)* | J | `completa` |
| tibia | «Yo también im—» → «¡Pregunta dos!» *(el tic la interrumpe)* | M tibia, líneas 10–11 | `cortada` |
| fría | «Lo mío es correr. Está bien.» → «¡Está bien!» *(se endurece)* | M fría, líneas 8–9 | `cerrada` |
| no visitada | «Si nadie me necesita… entonces la reparto.» *(desplazada: no habla de su valor, habla de su energía)* | M no visitada, líneas 5–6 | `espera` |

---

### P · Promesa — `e6_yotsuba_promesa` *(solo no visitada)*

*(Corre entre el monólogo y el gesto.)*

**mc_pensamiento:** Quince minutos más cada tarde. Los contó, por si yo iba.

**mc_pensamiento:** No fui. Eso no se arregla con un examen.

**mc_pensamiento:** Cuando esto termine voy a la pista. Esas dos vueltas de más las cronometro yo.

---

### G · Gestos — `e6_yotsuba_gesto_<estado>`

*(Espejo de B3.1: allí miraba a las demás y la hoja quedaba en blanco. Aquí cambia qué hace con la mirada.)*

#### G · cálida

**narrador:** Escribía sin parar y, de vez en cuando, levantaba la vista hacia las demás.

**narrador:** Una vez miró a Ichika. Otra, a Miku. Después a Itsuki, y fue un saludo, no una alarma.

**mc_pensamiento:** Escribir y mirar a la vez. Nadie le había dicho que se podían hacer las dos cosas.

**narrador:** En la muñeca llevaba un 28 con una raya encima. Hoy no necesitaba la cuenta.

`[SFX sfx_timbre volume 1.5]` `[MUS stop]` *(si aún suena algo)*

#### G · tibia

**narrador:** Se le detuvo el lápiz a media palabra. Una sola vez.

**narrador:** Miró a las demás, volvió a la hoja y siguió con la pregunta dos, a toda velocidad.

**mc_pensamiento:** Esta vez no era una hoja en blanco. Era una frase en blanco.

**mc_pensamiento:** Lo que iba a escribir, lo dejó a medias. Y yo no sabía qué era.

`[SFX sfx_timbre volume 1.5]`

#### G · fría

**narrador:** Escribió de corrido, sin levantar la vista ni una vez. Fue la primera en entregar.

**narrador:** Pasó junto a mi pupitre sin mirarme. En la muñeca, ninguna cuenta.

**mc_pensamiento:** Esta vez la hoja estaba llena. Esta vez no miró a nadie.

**mc_pensamiento:** Lo que mejor sabe hacer, leer a las demás, lo había apagado. Y lo apagué yo.

`[SFX sfx_timbre volume 1.5]`

#### G · no visitada

**narrador:** Resolvió su hoja sin dramas. A la mitad se le rompió la punta del lápiz a Ichika.

**narrador:** Yotsuba ya tenía uno de repuesto en la mano antes de que Ichika levantara la suya.

**mc_pensamiento:** Ni siquiera la miró para saberlo. Eso no se aprende en un libro.

**mc_pensamiento:** Reparte lo que le sobra antes de que se lo pidan. Y se queda con lo que le falta.

`[SFX sfx_timbre volume 1.5]`

---

### E · Ecos (Mov. 8) — `e6_yotsuba_eco_<estado>`

*(Entra ya con `[SPR yotsuba neutral at pj(X_YOTSUBA)]`. Las hermanas presentes van en `pj_calla`. No cita ninguna nota. Termina en `pj_calla`.)*

#### E · cálida

**narrador:** Yotsuba llevaba el boletín boca abajo en una mano y el rotulador destapado en la otra.

`[SPR yotsuba neutral at pj_habla(X_YOTSUBA)]` `[with disolucion_lenta]`

**yotsuba:** Dame la muñeca. El uno se borró hace días.

**narrador:** Escribió un uno. Y detrás, sin pedir permiso, dos ceros.

**yotsuba:** Empecé en el uno por ciento. Todavía no sé dónde estoy. Pero ya cabe.

`[SPR yotsuba sonriendo at pj_habla(X_YOTSUBA)]` `[with disolucion_lenta]`

**yotsuba:** ¡Esta vez sin corazón torcido! ¡Solo cuenta!

`[SPR yotsuba sonriendo at pj_calla(X_YOTSUBA)]`

#### E · tibia

**narrador:** Yotsuba sostenía el boletín con las dos manos, sin darle la vuelta.

`[SPR yotsuba neutral at pj_habla(X_YOTSUBA)]` `[with disolucion_lenta]`

**yotsuba:** Un minuto con catorce. Eso lo sé. Lo demás, no tanto.

**yotsuba:** No sé si me ayudaste o solo me dejaste correr.

**mc:** Corriste tú.

`[SPR yotsuba sonriendo at pj_habla(X_YOTSUBA)]` `[with disolucion_lenta]`

**yotsuba:** ¡Equipo completo! ¡Piernas y cabeza!

**narrador:** Esta vez no sonó a chiste.

`[SPR yotsuba sonriendo at pj_calla(X_YOTSUBA)]`

#### E · fría

**narrador:** Yotsuba guardó el boletín sin mirarlo, con la sonrisa ya puesta.

`[SPR yotsuba sonriendo at pj_habla(X_YOTSUBA)]` `[with disolucion_lenta]`

**yotsuba:** ¡Terminé primera! ¡Eso es bueno! Lo mío es terminar.

**mc:** Yotsuba…

**yotsuba:** ¡Está bien! ¡De verdad! Hoy no hace falta contar nada.

**narrador:** Lo dijo igual de fuerte las dos veces. Una de las dos sobraba.

`[SPR yotsuba sonriendo at pj_calla(X_YOTSUBA)]`

#### E · no visitada

**narrador:** Yotsuba miró su boletín con la cara con la que se mira una pista vacía.

`[SPR yotsuba sonriendo at pj_habla(X_YOTSUBA)]` `[with disolucion_lenta]`

**yotsuba:** ¡Hola, [mc]! ¡No hace falta que digas nada! Tengo tres vueltas de ventaja.

**mc:** Hola, Yotsuba.

**yotsuba:** Las vueltas de ventaja no caducan, ¿verdad?

**mc:** No caducan.

**yotsuba:** ¡Entonces las guardo!

`[SPR yotsuba sonriendo at pj_calla(X_YOTSUBA)]`

---

### Assets y notas del bloque 1

**`cg_yotsuba_examen`** — Mismo POV, misma cámara, misma luz y mismo primer plano que `cg_yotsuba_fracaso`: el examen de MC terminado y boca abajo, un lápiz y el canto de una mano, desenfocados y cortados por el borde. Al fondo, Yotsuba escribiendo con el lápiz *en movimiento* (en el fracaso estaba quieto), cabeza sobre su hoja y mirada levantada hacia un costado, hombros abiertos (en el fracaso, la cabeza giraba). **Sin sonrisa:** boca cerrada, cejas relajadas, para que sirva en las cuatro ramas. Detalle que no puede faltar: marcas de rotulador en la muñeca de la mano que escribe, sin texto legible.

**Sprites:** ninguno nuevo. Se usan `yotsuba neutral` y `yotsuba sonriendo` (nombres del código).

**Audio:** `descubrimiento` (monólogo cálida) → `yotsuba` (tema, en Y2) → silencio con `amb_reloj` (frase). `sfx_timbre` al final del bloque, en los cuatro estados.

**Para el chat 5:** la pista de Y2 tiene **28 marcas** (cobro del número perfecto). Microtextos en el anexo.

---

---

## BLOQUE 2 · Ichika · Martes · Matemáticas (Mov. 3)

### N · Núcleo — `e6_ichika_nucleo`

`[$ ui_escena("beat", "ichika", "Aula · Matemáticas")]` `[$ tiempo_restante = "cuatro exámenes"]`
`[BG bg_negro]` `[with fade_dia]` *(`amb_reloj` sigue por debajo)*

**narrador:** Martes. Matemáticas.

`[SFX sfx_hoja volume 2.0]` `[CG NUEVO — cg_ichika_examen]` `[scene cg_ichika_examen · with fade]`

**narrador:** Mismo pupitre. Mi hoja boca abajo antes de la mitad, otra vez.

**narrador:** Ichika leyó el enunciado de principio a fin. Despacio, que en ella ya es una noticia.

**narrador:** El guion de la obra asomaba doblado en cuatro por el bolsillo de su falda. Lo había traído. No lo sacó.

**mc_pensamiento:** La cuatro era un problema de trenes. De los que se resuelven con una resta y un poco de aire.

**mc_pensamiento:** Aire es justo lo que a ella no le sobra.

---

### M · Monólogos — `e6_ichika_mono_<estado>`

#### M · cálida — `e6_ichika_mono_calida`

*(Foco: lo que cambió porque alguien esperó. Voz sincera: sin una sola exclamación.)*

`[MUS descubrimiento fadein 2.0]`

**ichika_int:** Pregunta cuatro. Un tren sale a las cuatro cuarenta y cinco.

**ichika_int:** Seis minutos a la estación, cuatro para cambiarse. Hay que salir a las cuatro treinta y cinco.

**ichika_int:** Me salió antes de terminar de leer. Siempre lo supe. Nunca pensé que eso era matemáticas.

**ichika_int:** Él lo notó. Dijo que nadie improvisa un número así. Yo lo llamé ser organizada.

**ichika_int:** Después se quedó de pie, sin devolverme el chiste, esperando. Y yo dije lo que no digo.

**ichika_int:** «No sé cuánto más puedo seguir haciendo esto.» Lo dije en voz alta. Nadie se cayó por eso.

**ichika_int:** Le digo «estoy bien» a todos. Es una contraseña. A él no se la dije.

**ichika_int:** Dijo que eso ya lo sabía yo sola. Tenía razón, que es lo más incómodo de todo.

**ichika_int:** El papel nuevo lo acepté sin pensar. Sigue en pie. Pero ahora sé que fue sin pensar.

`[ACTIVA e6_ichika_mj — las dos últimas líneas]`

**ichika_int:** Tengo doce líneas de la obra de memoria. Salen solas. Las mías tardan un segundo entero.

**ichika_int:** Vamos a repasarlas. Hoy quiero ver cuáles son mías.

#### M · tibia — `e6_ichika_mono_tibia`

*(Foco: la tarea y una pregunta abierta, «¿me dejó escapar por amable o por no mirar?». La humorada aparece justo antes de la verdad.)*

**ichika_int:** Pregunta cuatro. Trenes. Salen las cuatro treinta y cinco.

**ichika_int:** Me sale tan rápido que me da un poco de miedo. Cuando algo sale tan fácil, ¿es mío?

**ichika_int:** «Con más drama, entonces. ¿Qué tal un dragón?» Dijo eso. Y le seguí la broma.

**ichika_int:** El dragón leía contratos de audición. Lo bauticé «Contrato». Mi mejor material.

**ichika_int:** O mi mejor escondite. Hablamos diez minutos de un dragón. Los dos sabíamos de qué no.

**ichika_int:** ¿Me dejó escapar porque era amable, o porque no quiso mirar?

**ichika_int:** Si le sigo la broma, él se ríe y yo no tengo que explicar nada. Es cómodo.

**ichika_int:** Es demasiado cómodo. Hay una frase que lleva días esperando. «No tengo que po—

**ichika_int:** ¡Siguiente pregunta!

#### M · fría — `e6_ichika_mono_fria`

*(Foco: la herida convertida en método. La máscara es perfecta y ella lo sabe.)*

**ichika_int:** Pregunta cuatro. Trenes. Cuatro treinta y cinco.

**ichika_int:** «Si tienes tiempo para esto, tienes tiempo para estudiar.» Eso dijo.

**ichika_int:** Tenía razón. Contesté «tienes razón», con la sonrisa en su sitio. Salió perfecto.

**ichika_int:** Tan perfecto que no me lo creí ni yo.

**ichika_int:** Aprovechar el tiempo. Resolver, revisar, entregar. En un examen no hay chiste.

**ichika_int:** Nadie va a ver nada. Eso se me da bien.

**ichika_int:** Estoy bien. Que conste.

#### M · no visitada — `e6_ichika_mono_no_visitada`

*(Foco: la espera; responde a su `queja_ichika`. Los paréntesis son la máscara filtrándose en la voz interior.)*

**ichika_int:** Pregunta cuatro. Trenes. Cuatro treinta y cinco. Sale sola.

**ichika_int:** Ensayé tres formas de recibirlo, si venía. La graciosa. La dramática. La de «qué sorpresa».

**ichika_int:** No vino. Las ensayé igual, delante del espejo del club.

**ichika_int:** (Entra Ichika. Se detiene. Sonríe. Aquí iría el chiste.)

**ichika_int:** Eran tres. Ninguna era mía. No sé si tengo una cuarta.

**ichika_int:** Si no sé qué hacer, actúo. …Siempre.

---

### J · Minijuego I1′ — `e6_ichika_mj` *(solo cálida)*

`[MUS ichika fadein 1.0 fadeout 1.5]`
`[MJ i1 · call mj_ejecutar("i1", "ichika") → "ganado" | "saltado"]`

*(Las doce líneas que ve el jugador están en el anexo. Fallos: `MJ_FALLOS`, dichos por `narrador`.)*

`[MUS stop fadeout 3.0]`

**narrador:** Ichika levantó la vista del papel. No tenía ninguna expresión puesta.

**ichika_int:** No tengo que poder con todo.

**ichika_int:** Lo repetí una vez más, por dentro, a ver si se me quedaba. Se quedó.

**ichika_int:** Sonreí. La sonrisa llegó medio segundo tarde. Esta vez dejé que llegara.

**ichika_int:** Pregunta cinco. Antes de contestar, respiro.

if `_return == "saltado"`:

> **narrador:** Hay ensayos que se hacen por dentro, sin público. Este lo hizo entero.

---

### F · La frase de cambio

| Estado | Frase | Dónde | `e6_frase[h]` |
|---|---|---|---|
| cálida | «No tengo que poder con todo.» *(sin exclamación; la máscara vuelve «medio segundo tarde»)* | J | `completa` |
| tibia | «No tengo que po—» → «¡Siguiente pregunta!» | M tibia, líneas 8–9 | `cortada` |
| fría | «Estoy bien. Que conste.» | M fría, línea 7 | `cerrada` |
| no visitada | «Si no sé qué hacer, actúo. …Siempre.» | M no visitada, línea 6 | `espera` |

---

### P · Promesa — `e6_ichika_promesa` *(solo no visitada)*

**mc_pensamiento:** Ensayó tres formas de recibirme. La graciosa, la dramática, la de «qué sorpresa».

**mc_pensamiento:** Y dijo que no sabía si podría con otra cosa. Yo tampoco supe qué contestarle.

**mc_pensamiento:** Voy a ir a verla ensayar. Sin que tenga que prepararme ninguna de las tres caras.

---

### G · Gestos — `e6_ichika_gesto_<estado>`

*(Espejo de B3.2: allí sacaba el guion, cerraba los ojos y el profesor la despertaba. Aquí tiene los ojos abiertos y el guion sigue en el bolsillo.)*

#### G · cálida

**narrador:** Ichika resolvió la cuatro en lo que tarda en cerrarse una puerta.

**narrador:** Después se quedó mirando el resultado, como si se lo hubiera regalado otra persona.

**mc_pensamiento:** Ojos abiertos. El guion en el bolsillo, sin tocar. Ni una vez miró el reloj con miedo.

**mc_pensamiento:** Hoy no necesitaba hacer de nadie.

`[SFX sfx_timbre volume 1.5]` `[MUS stop]`

#### G · tibia

**narrador:** Resolvió la cuatro rápido y se quedó sonriéndole a su hoja.

**profe:** Nakano. Está sonriendo.

**ichika:** Es una técnica, profesor.

**narrador:** Nadie se rió. Ella tampoco. La sonrisa se le fue a mitad del problema siguiente.

**mc_pensamiento:** Un chiste justo antes de que se le escapara algo. Otra vez.

`[SFX sfx_timbre volume 1.5]`

#### G · fría

**narrador:** Resolvió sin una pausa, sin un tachón, sin una mirada a nadie.

**narrador:** La sonrisa estaba en su cara desde que empezó, igual de quieta que el reloj de la pared.

**mc_pensamiento:** Una hoja perfecta y una sonrisa perfecta. Eso era lo que se veía.

**mc_pensamiento:** Contesta como se contesta cuando alguien tiene razón: rápido y sin adornos.

`[SFX sfx_timbre volume 1.5]`

#### G · no visitada

**narrador:** Resolvía con una mano. Con la otra, bajo el pupitre, movía el guion doblado.

**narrador:** Una pregunta, una línea. Una línea, una pregunta. Las dos cosas a medias, y las dos bien.

**mc_pensamiento:** Eso no es hacer dos cosas. Es no soltar ninguna.

**mc_pensamiento:** Con ella el cansancio nunca se nota en lo que hace. Se nota en que no para.

`[SFX sfx_timbre volume 1.5]`

---

### E · Ecos (Mov. 8) — `e6_ichika_eco_<estado>`

#### E · cálida

**narrador:** Ichika salió con el guion cerrado bajo el brazo y la cara recién lavada.

`[SPR ichika neutral at pj_habla(X_ICHIKA)]` `[with disolucion_lenta]`

**ichika:** Anoche dormí once horas. Esta vez no redondeé.

**ichika:** Pensé antes de decir que sí a algo. Una sola vez. Me pareció una cosa nueva.

`[SPR ichika sonriendo at pj_habla(X_ICHIKA)]` `[with disolucion_lenta]`

**narrador:** La sonrisa le llegó medio segundo tarde. Esta vez la dejó llegar.

`[SPR ichika sonriendo at pj_calla(X_ICHIKA)]`

#### E · tibia

**narrador:** Ichika salió contando algo del dragón «Contrato», que ahora también leía exámenes.

`[SPR ichika sonriendo at pj_habla(X_ICHIKA)]` `[with disolucion_lenta]`

**ichika:** ¡Pidió prórroga! ¡Los dragones siempre piden prórroga!

**narrador:** Se rió sola. Se calló un segundo de más.

`[SPR ichika neutral at pj_habla(X_ICHIKA)]` `[with disolucion_lenta]`

**ichika:** Era un chiste. …Era un chiste, ¿verdad?

**mc:** Era un chiste.

**ichika:** Eso pensaba yo.

`[SPR ichika neutral at pj_calla(X_ICHIKA)]`

#### E · fría

**narrador:** Ichika salió a la hora exacta, con la sonrisa puesta, como todo lo demás.

`[SPR ichika sonriendo at pj_habla(X_ICHIKA)]` `[with disolucion_lenta]`

**ichika:** ¿Todo bien? Yo estoy bien. Que conste.

**mc:** No te lo había preguntado.

`[SPR ichika neutral at pj_habla(X_ICHIKA)]` `[with disolucion_lenta]`

**ichika:** Ya. Lo dije por si acaso.

`[SPR ichika neutral at pj_calla(X_ICHIKA)]`

#### E · no visitada

**narrador:** Ichika salió probándose una expresión. Se la quitó. Se puso otra.

`[SPR ichika neutral at pj_habla(X_ICHIKA)]` `[with disolucion_lenta]`

**ichika:** Ensayé cómo salir y no me sale ninguna.

**ichika:** Tengo la graciosa, la dramática y la de «qué sorpresa». La cuarta todavía no existe.

**mc:** No tiene que existir hoy.

`[SPR ichika sonriendo at pj_habla(X_ICHIKA)]` `[with disolucion_lenta]`

**ichika:** ¡Qué amable! …Esa fue la graciosa. Perdona el reflejo.

`[SPR ichika sonriendo at pj_calla(X_ICHIKA)]`

---

### Assets y notas del bloque 2

**`cg_ichika_examen`** — Misma cámara, luz y primer plano que `cg_ichika_fracaso`. Ichika sentada con la **espalda recta** (en el fracaso, tumbada sobre el brazo), **ojos abiertos** (allí, uno entreabierto vigilando), escribiendo, con el **guion doblado en cuatro asomando del bolsillo de la falda** (allí, bajo la hoja). Expresión neutra: ni sonrisa ni ceño. Silueta que se lee al 30 %: es la única de las tres que se sienta como una regla.

**Sprites:** ninguno nuevo. `ichika neutral` y `ichika sonriendo` (nombres del código). `ichika agotada` queda sin usar: es solo de la grieta del hub y del Final B.

**Audio:** igual que el bloque 1. El tema `ichika` suena solo en I1′.

---

---

## BLOQUE 3 · Miku · Viernes · Sociales (Mov. 6) — el clímax

### N · Núcleo — `e6_miku_nucleo`

`[$ ui_escena("beat", "miku", "Aula · Sociales")]` `[$ tiempo_restante = "un examen"]`
`[BG bg_negro]` `[with fade_dia]` *(solo `amb_reloj`)*

**narrador:** Viernes. El último día, y el último examen. Sociales.

`[SFX sfx_hoja volume 2.0]` `[CG NUEVO — cg_miku_examen]` `[scene cg_miku_examen · with fade]`

**narrador:** Segunda fila, mi hoja boca abajo. A este examen lo dejé más despacio. Quería quedarme a mirar.

**narrador:** Miku tenía el lápiz en la mano derecha y, junto al lápiz, la goma. Entera. Con las cuatro esquinas.

**mc_pensamiento:** En su hoja del segundo día, la goma había trabajado más que el lápiz.

**narrador:** Los audífonos colgaban de su cuello, apagados.

**mc_pensamiento:** La pregunta tres no decía «sal». Decía «rutas de comercio».

**mc_pensamiento:** Lo que escribiera de más sería ella. Lo que no escribiera, también.

---

### M · Monólogos — `e6_miku_mono_<estado>`

#### M · cálida — `e6_miku_mono_calida`

*(Foco: lo que cambió porque alguien se pasó la noche en su tema. Todas las líneas abren con «…» hasta que se suelta, en J.)*

`[MUS descubrimiento fadein 2.0]`

**miku_int:** …Pregunta tres. Rutas de comercio y sostén de una provincia sin costa.

**miku_int:** …Sal.

**miku_int:** …Me preguntó cuánto tardaba la sal en llegar. Diez días. Doce si llovía.

**miku_int:** …Contesté sin pensar. Iba a pedir perdón. No me dejó. Dijo que eso no se disculpa.

**miku_int:** …Estaba contestando una pregunta que me hizo él. Todavía no sé si le creo.

**miku_int:** …Dijo que no me faltaba la materia. Que me faltaba creer que lo que sé cuenta como saber.

**miku_int:** …Dijo que lo iba a comprobar. Hoy es el día. Esta pregunta es lo que sé, y el examen la pide.

**miku_int:** …Hablar cuesta. Escribir también, si es de algo que quiero. Cuesta igual.

**miku_int:** …Tengo una canción en la cabeza. Es la que pongo para que nadie se acerque.

`[ACTIVA e6_miku_mj — las dos últimas líneas]`

**miku_int:** …Voy a escribir con ella. Primero con la mía. Cuando se apague, queda el reloj del aula.

**miku_int:** …El reloj nunca ha pedido perdón. …Vamos.

#### M · tibia — `e6_miku_mono_tibia`

*(Foco: la tarea y una pregunta abierta, «¿era un elogio o una etiqueta?». Silencio salvo `amb_reloj`. La frase queda cortada.)*

**miku_int:** …Pregunta tres. Rutas de comercio y sostén de una provincia sin costa.

**miku_int:** …Dijo que se me daba bien. Yo dije que solo lo había leído.

**miku_int:** …Dijo que era más de lo que había hecho nadie en mi casa.

**miku_int:** …Era un elogio con una comparación dentro. …¿Me lo dijo a mí o me puso al lado de las demás?

**miku_int:** …Mis hermanas también leen. …No tanto, pero leen.

**miku_int:** …La sal entra por las rutas. Podría contarla.

**miku_int:** …Si la cuento y no suma, me habré pasado de hablar.

**miku_int:** …Si no la cuento, nadie va a saber que la sé.

**miku_int:** …Lo que amo no—

**miku_int:** …Pregunta cuatro.

#### M · fría — `e6_miku_mono_fria`

*(Foco: la herida convertida en método. Silencio salvo `amb_reloj`. El «…» se endurece.)*

**miku_int:** …Pregunta tres. Rutas de comercio y sostén de una provincia sin costa.

**miku_int:** …Dijo que el Sengoku no entra en el examen. Tres temas, y ninguno pregunta por la sal.

**miku_int:** …Tenía razón. La pregunta es de comercio.

**miku_int:** …Cuatro renglones del libro de texto: rutas, mercados, impuestos. Está todo.

**miku_int:** …Escribo eso. Lo que me van a preguntar.

**miku_int:** …La otra respuesta también la sé. Entera.

**miku_int:** …Hoy no.

#### M · no visitada — `e6_miku_mono_no_visitada`

*(Foco: la espera; responde a su `queja_miku`. Silencio salvo `amb_reloj`.)*

**miku_int:** …Pregunta tres. Rutas de comercio y sostén de una provincia sin costa.

**miku_int:** …Sal. La respuesta empezó a escribirse sola. Ya llevo cuatro renglones.

**miku_int:** …No debería. Es un examen. …Borro.

**miku_int:** …Hay una silla enfrente de la mía. Siempre está vacía.

**miku_int:** …Dejé el libro abierto en la misma página dos días. Por si hacía falta una excusa.

**miku_int:** …Nadie se sentó. No pasa nada.

**miku_int:** …Soy buena esperando.

**miku_int:** …Escribo tres líneas de rutas. La sal, otro día.

**miku_int:** …Perdón. Eso sonó triste. No era la idea.

---

### J · Minijuego M3 — `e6_miku_mj` *(solo cálida)*

`[MUS miku — lo arranca M3 en su fase 1; si el chat 6 no lo hace, poner aquí: play music miku fadein 1.0]`
`[MJ m3 · call mj_ejecutar("m3", "miku") → "ganado" | "saltado"]`

*(Fase 2: la música se corta y manda `amb_reloj`. Fallos: `MJ_FALLOS`, dichos por `miku_int`.)*

`[MUS stop]` *(solo el reloj)*

**narrador:** Se quitó los audífonos del cuello, despacio. Los plegó y los dejó en el pupitre, junto a la goma.

`[ECO DE LA FRASE — desde aquí desaparece el «…» inicial]`

**miku_int:** Alguien se la vendió. Y eso me parece mucho más importante que la leyenda.

**miku_int:** Dejaré de tener miedo a lo que más amo.

**miku_int:** Esperé el perdón. Es lo que viene después. No llegó.

**narrador:** Escribía sin levantar la cabeza. Sin detenerse al final de cada línea. Sin borrar.

if `_return == "saltado"`:

> **narrador:** Hay respuestas que se escriben solas. Esta lo hizo de una vez, de principio a fin.

*(La frase de cambio es la primera vez que Miku dice algo sin «…» al comienzo **y** sin que el «perdón» llegue detrás. «Mucho más—» queda terminada: «importante que la leyenda».)*

---

### F · La frase de cambio

| Estado | Frase | Dónde | `e6_frase[h]` |
|---|---|---|---|
| cálida | «Dejaré de tener miedo a lo que más amo.» *(sin «…», sin «perdón»)* | J | `completa` |
| tibia | «…Lo que amo no—» *(el cuadernillo le sube hasta media cara)* | M tibia, línea 9 | `cortada` |
| fría | «…Hoy no.» | M fría, línea 7 | `cerrada` |
| no visitada | «…Soy buena esperando.» *(desplazada: habla de esperar, no de lo que sabe)* | M no visitada, línea 7 | `espera` |

---

### P · Promesa — `e6_miku_promesa` *(solo no visitada)*

**mc_pensamiento:** Hay una silla enfrente de la suya. Siempre vacía.

**mc_pensamiento:** Dejó un libro abierto dos días por si alguien hacía falta de excusa.

**mc_pensamiento:** Voy a sentarme en esa silla. Y a leer lo mismo que ella, aunque no entienda nada.

---

### G · Gestos — `e6_miku_gesto_<estado>`

*(Espejo de B3.5: allí escribía, borraba, la goma era un tocón y la mano subía a los audífonos sin tocarlos. Aquí cada estado invierte un detalle distinto.)*

#### G · cálida

**narrador:** Cuando sonó el timbre, su hoja estaba llena hasta el último renglón. Sin un solo borrón.

**mc_pensamiento:** La goma seguía siendo una goma. Hace un mes eso habría sido una noticia.

**narrador:** No recogió los audífonos enseguida. Los miró un segundo, como quien comprueba que no se mueven solos.

**mc_pensamiento:** Plegados, no puestos. Como se dejan las llaves en la entrada.

**narrador:** Al final los recogió. Se los colgó al cuello. Sin subírselos.

`[SFX sfx_timbre volume 1.5]`

#### G · tibia

**narrador:** Escribió la respuesta de rutas sin una sola mención a la sal.

**narrador:** Cada vez que se acercaba a una frase larga, el cuadernillo le subía un poco más.

**mc_pensamiento:** Sabía cómo seguir. Se le veía en el lápiz, que dudaba justo antes de cada coma.

**mc_pensamiento:** No borró. Se detuvo. Es una forma de borrar que no deja goma.

`[SFX sfx_timbre volume 1.5]`

#### G · fría

**narrador:** Escribió firme, sin dudas, cuatro renglones exactos.

**narrador:** Hacia la mitad, la mano libre subió hasta los audífonos. Y se quedó ahí hasta el timbre.

**mc_pensamiento:** No se los puso. No los soltó. Era una respuesta correcta y me dolió mirarla.

**mc_pensamiento:** Tenía la razón de su lado. Esa fue otra forma de no ganar.

`[SFX sfx_timbre volume 1.5]`

#### G · no visitada

**narrador:** Escribió largo. Se detuvo a mitad de un renglón. Pasó la goma una sola vez, con cuidado.

**narrador:** La goma perdió un borde. No quedó en tocón.

**mc_pensamiento:** Desde la segunda fila no pude leer lo que borró. Pude ver cuánto ocupaba.

**mc_pensamiento:** Lo dejó en tres líneas. Las de quien no quiere molestar.

`[SFX sfx_timbre volume 1.5]`

---

### E · Ecos (Mov. 8) — `e6_miku_eco_<estado>`

#### E · cálida

*(Cobro de la página 120. Primera sonrisa. Habla sin «…» y sin «perdón».)*

**narrador:** Miku llegó con los audífonos al cuello, sin tocarlos, y el boletín en las dos manos.

`[SPR miku neutral at pj_habla(X_MIKU)]` `[with disolucion_lenta]`

**miku:** La página ciento veinte. ¿Llegaste?

**mc:** Ciento veintidós.

`[SPR NUEVO — miku sonrie at pj_habla(X_MIKU)]` *(fallback: `miku relajada`)* `[with disolucion_lenta]`

**narrador:** Se rió. Una sola nota, corta, como un acorde.

**miku:** Quería ver tu cara. Ya la vi.

`[SPR miku neutral at pj_calla(X_MIKU)]`

#### E · tibia

**narrador:** Miku tomó su boletín con el cuadernillo de preguntas todavía doblado bajo el brazo.

`[SPR miku neutral at pj_habla(X_MIKU)]` `[with disolucion_lenta]`

**miku:** …Dijiste que se me daba bien.

**miku:** …Todavía estoy pensando qué querías decir con eso.

**mc:** Lo que dije.

**miku:** …Puede ser. …Lo sigo pensando.

`[SPR miku neutral at pj_calla(X_MIKU)]`

#### E · fría

**narrador:** Miku llegó con los audífonos puestos. Esta vez sonaban: se oían desde la puerta.

`[SPR miku neutral at pj_habla(X_MIKU)]` `[with disolucion_lenta]`

**miku:** …Contesté lo que entraba. …Estuvo bien.

**miku:** …Hoy no.

**narrador:** No dijo a qué. No hizo falta.

`[SPR miku neutral at pj_calla(X_MIKU)]`

#### E · no visitada

**narrador:** Miku se detuvo en la puerta con el boletín contra el pecho, como se lleva un libro.

`[SPR miku neutral at pj_habla(X_MIKU)]` `[with disolucion_lenta]`

**miku:** …La silla sigue vacía. …No es un reproche. …Es información.

**mc:** Lo sé.

**miku:** …Dejé el libro abierto otra vez. …Por si acaso.

`[SPR miku neutral at pj_calla(X_MIKU)]`

---

### Assets y notas del bloque 3

**`cg_miku_examen`** — Misma cámara, luz y primer plano que `cg_miku_fracaso`. Miku **inclinada sobre su hoja, escribiendo**, hombros abiertos pero sin llegar a `animada` (allí, encogida). La **goma entera** junto al lápiz (allí, tocón y migas sobre un círculo gris). **Audífonos colgados del cuello**, mano libre apoyada plana en el pupitre, lejos de ellos (allí, la mano cerca). Sin texto legible en la hoja. Es el CG que cierra los cinco bloques: la goma entera responde a `cg_miku_fracaso`.

**El costo de P-15.** Como no hay `cg_miku_audifonos_mesa`, el gesto de dejar los audífonos sobre el pupitre (J y G cálida) queda **narrado** mientras el CG los muestra al cuello. Funciona porque la narración describe el cambio sobre una imagen que es solo el plano de apertura del bloque. Ver duda D-04.

**Sprite condicional `miku sonrie`** — solo para el eco cálida, el payoff de la página 120. Silueta: audífonos al cuello, boletín contra el pecho con las dos manos, hombros abiertos, barbilla recta. Sonrisa mínima, de comisura, **sin rubor** (lo daría por tímida). Si `miku relajada` ya lee como sonrisa mínima a 30 %, no hace falta. Ver duda D-03.

**Audio:** `descubrimiento` (monólogo cálida) → `miku` (fase 1 de M3) → solo `amb_reloj` (fase 2 y frase). La frase cae sobre el silencio más largo del evento. En los demás estados, nada más que el reloj.

---

---

## Anexo · Textos para los minijuegos

### I1′ · Las doce líneas (para el chat 6)

La obra de primavera es la de un andén de tren: acomoda el cobro de los trenes sin repetirlo. Cada línea ofrece **Actuada** (toque rápido, sube la máscara) o **Sincera** (mantener pulsado, baja la máscara). Las actuadas pueden llevar exclamación; las sinceras, nunca.

| # | Actuada | Sincera |
|---|---|---|
| 1 | «¡Llegué justo a tiempo! ¡Siempre llego justo a tiempo!» | «Llevo toda la semana llegando justa.» |
| 2 | «Estoy bien. Que conste.» | «Estoy cansada.» |
| 3 | «¡Dormir es para los débiles!» | «Necesito dormir.» |
| 4 | «¡Una audición más, y otra, y otra!» | «Me da miedo que no salga ninguna.» |
| 5 | «¡El público me adora, aunque esté vacío!» | «A veces actúo para una sala vacía.» |
| 6 | «Tengo tres formas de decir que sí.» | «Digo que sí antes de pensarlo.» |
| 7 | «¡Los dragones no se cansan!» | «Yo sí.» |
| 8 | «¡Mi risa es mi mejor entrada!» | «A veces me río para no contestar.» |
| 9 | «Pregúntame lo que quieras. Contestaré con un chiste.» | «Pregúntame dos veces.» |
| 10 | «¡Hoy no me cuesta nada!» | «Hoy me cuesta mucho.» |
| 11 | «¡Puedo con todo!» | «No sé hasta cuándo.» |
| 12 | *(solo sincera)* | «No tengo que poder con todo.» |

**Recorte por nivel:** *media* (10 líneas) quita la 4 y la 8; *asistida* (8) quita además la 5 y la 10. La 12 siempre queda y siempre es solo sincera.

### Y2 · Microtextos (para el chat 5)

| Elemento | Texto |
|---|---|
| Rótulos de tramo | «TRAMO 1/5 · Ichika» · «2/5 · Nino» · «3/5 · Miku» · «4/5 · Itsuki» · «5/5 · Yotsuba» |
| Acierto | «Testigo recibido.» |
| Salida en falso | «Salió antes de tiempo.» |
| Testigo caído | «Se cayó el testigo.» |
| Meta | La pista tiene 28 marcas; el 28 se ve en la línea de llegada. |

### M3 · Microtextos (para el chat 6)

| Elemento | Texto |
|---|---|
| Fase 1 | «FASE 1 · Con los audífonos» |
| Transición | «Los audífonos se apagan.» |
| Fase 2 | «FASE 2 · Solo el reloj» |
| Final | «Compás completo.» |

### `MJ_FALLOS` — listo para pegar

Sustituye **solo** las claves `yotsuba`, `ichika` y `miku` del `define MJ_FALLOS` de `10_minijuegos.rpy`. Nino e Itsuki los escribe el chat 4. El primer elemento es quién habla (`"int"` = la voz interior de la hermana, `"narrador"` = el narrador); el índice es el número de fallos, y a partir del tercero se repite el último.

```renpy
    "yotsuba": [("int", "¡Otra vez!"), ("int", "¡Otra vez! ¡Esta sí!"), ("int", "Otra vez. Despacio. Primero se recibe.")],
    "ichika":  [("narrador", "Se quedó en blanco. Sonrió para que no se notara."), ("narrador", "La sonrisa tardó un poco más en volver."), ("narrador", "Esta vez no sonrió. Respiró, y empezó otra vez.")],
    "miku":    [("int", "…Perdón."), ("int", "…Perd—"), ("int", "…Otra vez.")],
```

El fallo es carácter, no castigo: Yotsuba pasa de forzar la exclamación a decir la lección sin signos; Ichika pasa de tapar el blanco con la sonrisa a ni siquiera intentarlo; Miku deja de terminar el «perdón».

---

## Assets nuevos

| Asset | Tipo | Estado | Nota |
|---|---|---|---|
| `cg_yotsuba_examen` | CG | pendiente | POV de MC, espejo de `cg_yotsuba_fracaso`. Estado-agnóstico |
| `cg_ichika_examen` | CG | pendiente | POV de MC, espejo de `cg_ichika_fracaso`. Estado-agnóstico |
| `cg_miku_examen` | CG | pendiente | POV de MC, espejo de `cg_miku_fracaso`. Estado-agnóstico |
| `miku sonrie` | sprite | **condicional** | Solo el eco cálida. Alternativa: `miku relajada` (duda D-03) |

Generar los tres `*_examen` **en la misma sesión que los de Nino e Itsuki** (chat 4), con las semillas de sus `*_fracaso`. Los prompts los escribe el chat 7.

**Descartado:** `cg_miku_audifonos_mesa` (P-15, equidad de CG entre hermanas). Tampoco se piden `yotsuba serena` ni `ichika sincera`: los estados sinceros se resuelven con `neutral`.

**Reutilizados sin tocar:** `yotsuba neutral/sonriendo`, `ichika neutral/sonriendo`, `miku neutral` (y `relajada` como alternativa); temas `yotsuba`, `ichika` y `miku`; `descubrimiento`; `amb_reloj`; `sfx_hoja` y `sfx_timbre`.

---

## Flags

No hay variables nuevas. Lo que escriben estos bloques, ya existente:

| Variable | Qué escribe | Quién |
|---|---|---|
| `e6_frase[h]` | `completa` / `cortada` / `cerrada` / `espera`, según el estado | `e6_marcar_ganchos` (no lo escriben las líneas) |
| `e6_promesas` | `h` si no visitada, en orden de examen: yotsuba, ichika, (nino, itsuki), miku | `e6_marcar_ganchos` |
| `e6_mj[h]` | `resultado`, `intentos`, `fallos`, `nivel`, `boost`, `datos` | `mj_cerrar` |

**Contenido de cada promesa, para el Capítulo 2** (sin que el capítulo gire alrededor de esto):

| Hermana | Promesa de MC |
|---|---|
| Yotsuba | Ir a la pista a cronometrar las dos vueltas de más |
| Ichika | Ir a verla ensayar sin que prepare ninguna de sus tres caras |
| Miku | Sentarse en la silla vacía y leer lo mismo que ella |

---

## Notas de implementación

- **Orden de llamada.** `e6_bloque(h)` ya llama en el orden correcto: núcleo → mono → (mj si cálida) → (promesa si no visitada) → `e6_marcar_ganchos` → gesto. Los ecos los llama `e6_cinco`.
- **`E6_MJ_JUEGO`.** Hoy apunta todo a `"prueba"`. Cuando existan los minijuegos reales, cambiar a `yotsuba: "y2"`, `ichika: "i1"` y `miku: "m3"` (chats 5 y 6).
- **`_return`.** Los `if _return == "saltado"` se leen justo después del `call mj_ejecutar`, antes de cualquier otro `call` (si no, `_return` se pisa). Alternativa: leer `e6_mj[h]["resultado"]`.
- **`tiempo_restante`.** Cada núcleo lo fija: `"cuatro exámenes"` (Ichika) y `"un examen"` (Miku). Yotsuba repite `"cinco exámenes"` por seguridad; Nino e Itsuki (chat 4) fijan `"tres"` y `"dos"`.
- **Transición entre días.** Cada gesto cierra con `sfx_timbre`. El núcleo siguiente abre con `bg_negro` + `fade_dia`. `amb_reloj` no se corta nunca entre bloques: solo lo corta el Mov. 7.
- **`duck()`.** Ningún bloque lo necesita: los efectos caen sobre silencio (solo `amb_reloj`). Si en cálida el `sfx_hoja` del núcleo coincide con música, el núcleo no la tiene todavía: `descubrimiento` entra *después* del núcleo.
- **Todo `show` lleva posición.** Solo aparecen sprites en los ecos y todos usan `pj_habla` / `pj_calla` con su `X_*`. Las hermanas ya presentes van en `pj_calla` dentro del mismo `with`.
- **Después de un CG.** En los bloques no hay `show` tras el CG: las líneas de MC en los gestos van con el CG puesto. El eco ocurre en `bg_departamento`.
- **Galería.** Descomentar `("cg_yotsuba_examen", "Examen · Japonés")`, `("cg_ichika_examen", "Examen · Matemáticas")` y `("cg_miku_examen", "Examen · Sociales")` en las pestañas de cada hermana. Rediseñar la Galería para que los `*_fracaso` no cuenten para el 100 % queda fuera de este documento (P-17).
- **Móvil.** Nada de estos bloques depende de un minijuego para tener sentido: con `persistent.mj_modo = "saltar"` se lee la frase de cambio completa igual (el bloque `if saltado` cubre el puente).
- **Longitud.** Ninguna línea de diálogo, narrador o pensamiento pasa de ~100 caracteres.

---

## Dudas abiertas

| ID | Duda | Dónde mirarla | Qué propuse |
|---|---|---|---|
| **D-01** | El «100» de Yotsuba en la muñeca no puede ser una nota (el contrato de los ecos del núcleo prohíbe citarlas, y el chat del Mov. 10 revela el «CIEN»). | Bloque 1 · **E cálida** | Lo escribe como *cuenta*: «dos ceros» y «Empecé en el uno por ciento… ya cabe». Si prefieres que sea nota explícita, hay que relajar el contrato en el núcleo. |
| **D-02** | Las promesas del análisis eran habladas; aquí son pensamientos de MC porque el examen es silencioso. | Los tres bloques · **P** | Pensamiento silencioso, coherente con la libreta del Mov. 10. |
| **D-03** | `miku sonrie` está pedido solo para el payoff de la página 120. No pude ver si `miku relajada` ya lee como sonrisa mínima. | Bloque 3 · **E cálida** y **Assets** | Pedirlo solo si `relajada` no basta. El eco ya trae el fallback escrito. |
| **D-04** | Sin `cg_miku_audifonos_mesa`, dejar los audífonos sobre el pupitre queda narrado y el CG los muestra al cuello. | Bloque 3 · **J** y **Assets y notas** | Aceptarlo como costo de P-15. La alternativa sería un CG de cierre para las tres. |
| **D-05** | El análisis dice «primera línea del juego de Miku sin “…”». No es cierto: ya habla sin «…» cuando cuenta la sal en el hub y en `reaccion_miku`. | Bloque 3 · **J** (nota) | Reformulado: *primera vez sin «…» y sin «perdón» detrás*. |
| **D-06** | Escribí aquí las doce líneas de I1′ porque el chat 6 las necesita y nadie más las escribe. | **Anexo · I1′** | Que el chat 6 las tome tal cual; hay regla de recorte para *media* y *asistida*. |
| **D-07** | Los eco de Mov. 8 asumen que cada hermana ya tiene su boletín en la mano (el núcleo dice que «vienen a por él»). | **E** de los tres bloques | Mencionado como objeto, nunca con el verbo «tomar». |
