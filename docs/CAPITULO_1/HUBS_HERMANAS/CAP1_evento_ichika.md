## Evento de hermana · Ichika — Sala de ensayo

**Escrito.** Assets pendientes. Encaja en cualquiera de los tres huecos.

Marcadores como en la apertura. `[BG]` fondo · `[CG]` ilustración · `[SPR]` sprite ·
`[MUS]` música · `[SFX]` efecto · `[NUEVO]` asset que no existe todavía ·
`[$]` línea de código.

---

### Decisiones de este evento

**No depende de nada.** No menciona la crisis de Nino, ni el beat de Itsuki, ni
los otros eventos. Todo lo que da por sabido ocurrió sí o sí: que Ichika fue la
primera en abrirle la puerta el primer día y que en la apertura del capítulo
fingió dormir para tapar una respuesta que no tenía. Se puede jugar primero,
segundo o tercero sin cambiar una línea.

**La sala de ensayo es suya, no de él.** Como con Yotsuba y Nino, hay que ir a
buscarla a su terreno. Es un club de teatro pequeño, con vestuario colgado y un
espejo de cuerpo entero, no un escenario de verdad — el escenario de verdad se lo
gana en una audición, y de eso todavía no hay ninguna cerrada.

**El recurso formal: la actuación constante.** Ichika no habla, actúa: cada
línea suya tiene una entonación pensada para un público, aunque el público sea
uno solo. Exclamaciones, pausas dramáticas, un guiño verbal detrás de cada frase.
Cuando la grieta aparece, la actuación se apaga de golpe: frases cortas, planas,
sin puntuación de más, como si de repente hablara sin dirección de escena. Cuando
se repone, la actuación vuelve, pero medio segundo tarde y un poco más rígida que
antes — el jugador no sabe por qué le suena distinta, pero le suena distinta.

**Futaro la encuentra dormida, no actuando.** A diferencia de Yotsuba —que no
sabe que la observan pero está despierta y en control— aquí el estado inicial es
el más desarmado posible: Ichika se queda dormida a mitad de un ensayo, sentada
en el suelo, con el guion resbalando de la mano. Es la prueba física de que
duerme poquísimo, sin que nadie tenga que decirlo en diálogo.

**La grieta sale por accidente, no por confesión.** Ella no decide contarle nada:
se le escapa una frase real a medio despertar, antes de que el filtro de la
actuación vuelva a activarse. Eso es lo que la hace válida — si lo dijera a
propósito, sería otra vez una actuación, la de la "hermana mayor que se sincera".

**Tres CG, siguiendo la regla del proyecto.** A partir de este evento, cada ruta
de hermana lleva un mínimo de dos y un máximo de tres CG nuevos. Aquí van los
tres: el hallazgo dormida, el instante exacto sin máscara, y la máscara
reactivándose vista desde Futaro. Los dos últimos son consecutivos, igual que el
par de Itsuki — no comparten semilla porque cambian de encuadre, pero sí deben
generarse con la misma luz y la misma sesión para leerse como el mismo minuto.

**Lo que este evento NO gasta.** No explica por qué actúa ni cuánto le preocupa
el dinero de la familia: eso pertenece a capítulos siguientes. Tampoco conecta
todavía su manejo de horarios imposibles con que Matemáticas sea su materia —
la punta se nombra (Movimiento 2, cuando calcula minutos y trenes de memoria
sin darse cuenta de que lo hace), el desarrollo es de más adelante. Es la misma
lógica que con Yotsuba y Literatura, y que con Nino e Inglés.

---

### Movimiento 1 · Llegada

`[BG NUEVO — bg_sala_ensayo]` `[MUS stop fadeout 1.0]`

**narrador:** El club de teatro tenía un cuarto propio detrás del auditorio.

**narrador:** Nadie me dijo que llamara antes de entrar.

**narrador:** La puerta estaba entreabierta.

`[CG NUEVO — cg_ichika_ensayo: Ichika sentada en el suelo, apoyada contra la
pared bajo un perchero con vestuario de utilería, dormida. El guion se le resbala
de la mano, algunas hojas ya en el piso. Espejo de cuerpo entero al fondo
reflejando parte de la sala. Luz de tarde entrando por una ventana alta. Un solo
personaje en el frame. Sostiene todo el movimiento 1, así que tiene que aguantar
en pantalla.]`

**narrador:** La reconocí por el pelo antes que por la cara.

**mc_pensamiento:** Está dormida.

**mc_pensamiento:** Sentada en el suelo. Con el guion en la mano.

**narrador:** A su lado había dos latas de energizante.

**narrador:** Una de ellas abollada, como si la hubiera apretado sin darse
cuenta.

**mc_pensamiento:** Y un horario escrito a mano, con tres columnas superpuestas.

**mc_pensamiento:** Clases. Ensayos. Algo tachado que no llegué a leer.

**narrador:** Me quedé en la puerta un momento, sin saber si entrar o
retroceder.

**narrador:** Decidí entrar.

**narrador:** Me acerqué despacio, tratando de no hacer ruido con los pasos.

**mc_pensamiento:** No sabía si despertarla o dejarla dormir un poco más.

**mc_pensamiento:** No llegué a decidirlo.

`[SFX sfx_hoja]`

**narrador:** El guion terminó de resbalarle de la mano y cayó al piso.

**narrador:** Eso la despertó.

---

### Movimiento 2 · La grieta

`[SPR ichika neutral at pj(0.5)]`

**narrador:** Abrió los ojos de golpe, sin saber todavía dónde estaba.

`[CG NUEVO — cg_ichika_desarmada: primer plano cerrado sobre Ichika, todavía
sentada en el suelo, recién despierta. Ojos entreabiertos y sin foco, pelo
suelto de un lado, boca ligeramente abierta, sin ningún rastro de la sonrisa que
usa en el resto del elenco. Misma luz de tarde y mismo ángulo de ventana que
`cg_ichika_ensayo`, pero encuadre mucho más cerrado sobre su cara: es el
fotograma exacto antes de que la actuación vuelva a encenderse, no una escena
nueva.]`

**ichika:** …¿Qué hora es?

**narrador:** Lo preguntó sin actuación, sin la voz que usa para todo.

**mc:** Las cuatro y media.

**ichika:** …

**ichika:** Perdí la tarde entera.

**narrador:** Lo dijo plano. Sin exclamación.

**narrador:** Sin la pausa que pone antes de un chiste.

**mc_pensamiento:** Esa no es su voz normal.

**mc_pensamiento:** Su voz normal tiene dirección de escena.

**mc_pensamiento:** Esta no tenía ninguna.

**narrador:** Duró medio segundo.

**narrador:** Después pareció darse cuenta de que yo estaba ahí, y de que la
había visto así.

`[SPR ichika sonrisa at pj(0.5)]`

**ichika:** ¡Ah, no! ¡Estaba practicando!

**mc:** ¿Practicando dormir?

**ichika:** ¡Es un método actoral! ¡Se llama sueño escénico!

**mc:** No existe eso.

**ichika:** ¡Claro que existe! ¡Lo inventé yo hace cinco minutos!

**narrador:** Se rió de su propio chiste, un poco más fuerte de lo que el chiste
merecía.

**mc_pensamiento:** Cambió de tema tan rápido que casi no lo noto.

**mc_pensamiento:** Casi.

**narrador:** Se puso de pie y se sacudió la falda.

**narrador:** Recogió el guion del suelo con un solo movimiento, como si llevara
ensayado también eso.

**mc:** ¿Cuánto tiempo dormiste anoche?

**ichika:** ¡Lo suficiente!

**mc:** Eso no es un número.

`[SPR ichika neutral at pj(0.5)]`

**ichika:** ¿Y desde cuándo un tutor de matemáticas pide cifras exactas de
otras cosas?

**narrador:** Lo dijo con una sonrisa, pero cambió de tema otra vez, y esta ya
era la segunda.

**narrador:** Guardó el horario doblándolo rápido.

**narrador:** Más rápido de lo necesario, antes de que yo pudiera leer lo que
estaba tachado.

**mc:** ¿Cuándo puedo verte para la próxima lección?

**narrador:** Se lo pregunté sin pensar mucho, solo para cambiar de tema yo
también.

**ichika:** Martes a las cinco y veinte. Nunca antes de eso.

**mc:** ¿Por qué no a las cinco y media, si total es casi lo mismo?

**ichika:** Porque el tren de las cinco cuarenta y cinco tarda seis minutos en
llegar a la estación desde aquí, y necesito cuatro para cambiarme.

**narrador:** Lo dijo sin pausar, sin contar con los dedos, como si ya tuviera
la cuenta hecha de memoria.

**mc_pensamiento:** Nadie improvisa ese número tan rápido.

`[SPR ichika sonrisa at pj(0.5)]`

**ichika:** ¡Es que soy muy organizada! ¡Parte del oficio!

**narrador:** Se rió, tapando otra vez algo que se le había escapado sin
querer.

**mc_pensamiento:** Dos latas de energizante.

**mc_pensamiento:** Un horario con algo tachado que no quiere que vea. 

**mc_pensamiento:** Una cuenta de minutos que le salió demasiado rápido.

**mc_pensamiento:** Y ahora esto.

**mc_pensamiento:** Ninguna de las cuatro cosas es una casualidad sola.

**mc_pensamiento:** Juntas, son un patrón.

---

### Movimiento 3 · La decisión

`[MUS NUEVO — descubrimiento, volumen 0 listo para subir]`

`[CG NUEVO — cg_ichika_mascara: punto de vista de Futaro, de pie, un paso atrás
del lugar donde ella se sienta. En primer término inferior, desenfocado y
cortado por el borde, el canto de su propia mochila colgada del hombro — el
objeto en primer plano, sin mano marcada. Ichika al fondo, ya sentada en una
silla plegable, con la sonrisa de vuelta en su sitio y el guion otra vez abierto,
mirando hacia cámara con la ceja levantada, como retando a que alguien diga algo.
Es el mismo minuto que `cg_ichika_desarmada` visto un paso después, con la
máscara ya reconstruida.]`

**narrador:** Se sentó en una de las sillas plegables.

**narrador:** Con el guion otra vez en la mano, y pasó una página sin leerla.

**ichika:** Bueno, ¿viniste a verme actuar o viniste a regañarme?

**mc:** Vine a buscarte para las clases de mañana.

**ichika:** ¡Qué aburrido!

**ichika:** Yo esperaba algo con más drama.

**narrador:** Sonrió, esperando la broma de vuelta.

**narrador:**  La que suele devolverle cualquiera que hable con ella.

**mc_pensamiento:** Tres cosas que acabo de ver y que ella escondió detras de
un chiste.

**mc_pensamiento:** Si le sigo la broma, la cuarta también va a quedar oculta.

**mc_pensamiento:** Y no va a haber una quinta oportunidad hoy.

```
MENÚ — ¿Cómo respondes?

A) No decir nada. Sostenerle la mirada en silencio, dándole tiempo.         [CÁLIDA]
B) Ceder. Reírte de la broma y dejar que oculte el tema.                     [TIBIA]
C) "Si tienes energía para hacer chistes, tienes energía para estudiar."   [FRÍA]
```
---

### Movimiento 4A · Rama cálida — Silencio

`[$ sumar_punto("ichika", 1)]`
`[MUS descubrimiento — fade in volumen 3.5]`

**narrador:** No dije nada.

**narrador:** Me quedé de pie, mirándola, sin devolverle el chiste.

`[SPR ichika neutral at pj(0.5)]`

**ichika:** …¿Qué?

**mc:** Nada.

**ichika:** No pusiste cara de nada.

**ichika:** Pusiste cara de estar esperando algo.

**mc:** Puede ser.

**narrador:** El silencio se estiró más de lo que suele durar entre los dos.

**narrador:** Ella fue la que lo rompió, y lo hizo sin la sonrisa de antes.

`[SPR ichika agotada at pj(0.5)]`

**ichika:** …No sé cuánto más puedo seguir haciendo esto.

**mc:** ¿Esto qué?

**ichika:** Todo.

**ichika:** Las audiciones. Las clases.

**ichika:** Fingir que puedo con las dos.

**narrador:** Lo dijo sin exclamación.

**narrador:** La primera frase larga de toda la tarde sin una sola.

**mc:** No dije que no pudieras.

**ichika:** No hacía falta.

**ichika:** Yo también me lo digo, y no me lo creo ni cuando lo digo yo.

**narrador:** Se quedó mirando el guion, sin pasar la página.

**mc_pensamiento:** La semana pasada faltó a algo. No sé a qué.

**mc_pensamiento:** Y por como dobló ese horario, tampoco creo que se lo haya
contado a nadie.

`[SPR ichika neutral at pj(0.5)]`

**ichika:** …

**ichika:** ¿No vas a decir nada aprovechado sobre esto?

**mc:** ¿Cómo qué?

**ichika:** No sé. Algo de tutor.

**ichika:** "Si estás cansada, deberías dormir más."

**mc:** Eso ya lo sabes tú sola.

**narrador:** Sonrió, esta vez más despacio, sin la energía de antes.

`[SPR ichika sonrisa at pj(0.5)]`

**ichika:** …Gracias por no decir la frase obvia.

**narrador:** Guardó el guion en la mochila, todavía sin la actuación completa
de vuelta.

**mc_pensamiento:** Volvió la sonrisa. Pero tardó, y no vino con exclamación.

**mc_pensamiento:** Es la primera vez que la veo actuar despacio.

---

### Movimiento 4B · Rama tibia — Seguirle la broma

*(sin puntos, sin desaire)*

`[SPR ichika sonrisa at pj(0.5)]`

**mc:** Con más drama, entonces.

**mc:** Entras corriendo, gritando mi nombre.

**ichika:** ¡Eso ya lo hice el primer día! Hay que innovar.

**mc:** ¿Qué tal un dragón?

**ichika:** ¡Un dragón que además sabe matemáticas!

**ichika:** ¡Perfecto para ti!

**narrador:** Se rió, esta vez de verdad, y la conversación se fue por ahí un
rato.

**mc_pensamiento:** Es una buena broma. Las suyas siempre lo son.

**mc_pensamiento:** Pero seguimos hablando de dragones y no de las dos latas de
energizante.

**ichika:** ¡Y el dragón tendría que usar lentes! ¡Para verse serio con los
números!

**mc:** Los dragones no necesitan lentes.

**ichika:** ¡Este sí! ¡Es miope de tanto leer contratos de audición!

**narrador:** Siguió inventando detalles del dragón durante un rato más, cada
uno más absurdo que el anterior.

**mc_pensamiento:** Cuanto más se ríe, menos espacio queda para preguntar nada
en serio.

**narrador:** Guardó el guion en la mochila sin volver a mirarlo.

**ichika:** Bueno, vamos, antes de que se haga de noche.

**mc_pensamiento:** No dijo nada más de lo que vi al entrar.

**mc_pensamiento:** Y yo tampoco insistí.

---

### Movimiento 4C · Rama fría — «Si tienes energía para hacer chistes, tienes energía para estudiar.»

`[$ desaires_cap1 += 1]`

**mc:** Si tienes tiempo para esto, tienes tiempo para estudiar.

**narrador:** La sonrisa no desapareció del todo, pero algo detrás de ella sí.

`[SPR ichika neutral at pj(0.5)]`

**ichika:** …

**ichika:** Ya veo.

**narrador:** Lo dijo con la voz más parecida a la de un adulto que le hubiera
oído usar.

`[SPR ichika sonrisa at pj(0.5)]`

**ichika:** ¡Tienes razón! ¡Debería aprovechar mejor el tiempo!

**narrador:** Guardó el guion de un solo movimiento, rápido.

**narrador:** Sin doblar las páginas con cuidado como antes.

**mc_pensamiento:** Dije exactamente lo que un padre le diría.

**mc_pensamiento:** Y ella me contestó exactamente lo que le contesta a un
padre.

**narrador:** Salió primero, sosteniendo la puerta apenas el tiempo justo para
no dejarla cerrarse en mi cara.

**mc_pensamiento:** No fue grosera. Fue correcta.

**mc_pensamiento:** Y eso, viniendo de ella, es peor que un portazo.

---

### Movimiento 5 · Cierre

*(común a las tres ramas; la última línea cambia)*

`[BG bg_sala_ensayo — luz de atardecer, entrando el conserje a apagar luces]`
`[MUS stop fadeout 1.5]`

**narrador:** Salimos cuando el conserje empezaba a apagar las luces del
pasillo.

**mc_pensamiento:** Una de cinco. Y esta se durmió antes de que yo dijera nada.

**mc_pensamiento:** Quedan tres semanas.

*Cierre A (cálida):*

**mc_pensamiento:** Dijo que no sabía cuánto más podía seguir así.

**mc_pensamiento:** No sé si me lo dijo a mí o si se le escapó.

**mc_pensamiento:** Tampoco sé si hay diferencia.

*Cierre B (tibia):*

**mc_pensamiento:** Hablamos de dragones durante diez minutos.

**mc_pensamiento:** Fue divertido.

**mc_pensamiento:** No estoy seguro de que haya sido nada más que eso.

*Cierre C (fría):*

**mc_pensamiento:** Tenía razón en lo que dije. Eso no me hace sentir mejor.

**mc_pensamiento:** Sostuvo la puerta el tiempo justo. Ni un segundo más.

`→ Vuelve al hub.`

---

### Assets del evento

| Asset | Tipo | Estado | Nota |
|---|---|---|---|
| `bg_sala_ensayo` | BG | pendiente | Cuarto de club de teatro, vestuario colgado, espejo de cuerpo entero, luz de tarde |
| `cg_ichika_ensayo` | CG | pendiente | Movimiento 1. Ichika dormida en el suelo, guion resbalando de la mano |
| `cg_ichika_desarmada` | CG | pendiente | Movimiento 2. Primer plano al despertar, antes de que vuelva la máscara |
| `cg_ichika_mascara` | CG | pendiente | Movimiento 3. POV de Futaro; la máscara ya reconstruida, ella retando con la mirada |
| `ichika_agotada` | sprite | pendiente | El instante sin actuación dentro del diálogo. Sin sonrisa, mirada perdida, ojeras |
| `ichika_neutral` | sprite | ya existe | Base fuera de la actuación completa |
| `ichika_sonrisa` | sprite | ya existe | La máscara en funcionamiento |
| `descubrimiento` | BGM | pendiente | Compartida con los otros eventos de hermana. Entra solo en rama cálida |

Reutilizados sin tocar: `sfx_hoja`.

**Tres CG, mínimo dos y máximo tres por regla del proyecto.** `cg_ichika_ensayo`
sostiene el movimiento 1. `cg_ichika_desarmada` y `cg_ichika_mascara` son
consecutivos y cubren el mismo minuto en dos encuadres: el primero es el
instante sin ninguna actuación, cerrado sobre su cara; el segundo es la máscara
ya reconstruida, visto desde Futaro con su mochila en primer término, siguiendo
el lenguaje de POV validado en `cg_manija_edificio`, `cg_estudio_biblioteca` y
`cg_itsuki_reto`. No comparten semilla porque los encuadres son distintos, pero
deben generarse en la misma sesión, con la misma luz de tarde, para que se lean
como el mismo minuto contado dos veces.

**`cg_ichika_ensayo`** — el detalle que no puede faltar son las dos latas de
energizante junto a ella: es la prueba física de "duerme poquísimo" sin que
ninguna línea tenga que explicarlo. El guion cayendo de la mano es lo segundo
más importante — si no se lee con claridad, el respaldo es mostrarlo ya caído en
el suelo, con las páginas abiertas.

**`cg_ichika_desarmada`** — la diferencia con cualquier otro momento de Ichika
en el set no puede ir en gestos grandes: ojos entreabiertos sin foco, boca
apenas abierta, pelo suelto de un lado, sin ningún rastro de sonrisa. Es la
única imagen del elenco donde Ichika no está actuando ni un poco, así que
cualquier resto de la sonrisa de base arruina la lectura.

**`cg_ichika_mascara`** — el reto en la mirada es la clave: no es una sonrisa
cualquiera, es la sonrisa sabiendo que la vieron caer y decidiendo no admitirlo.
Complementa directamente la línea «¿viniste a verme actuar o viniste a
regañarme?».

**`ichika_agotada`** — versión sprite del mismo estado que sostiene
`cg_ichika_desarmada`, para reutilizar dentro de los diálogos de las ramas sin
tener que volver al CG. Misma nota que con Itsuki y `timida`: si a un 30 % de
tamaño se confunde con `neutral`, el sprite no cumplió su función.

---

### Notas de implementación

- El evento abre con `$ sumar_punto("ichika", 2)` antes de cualquier línea de
  diálogo. Si el jugador eligió la sala de ensayo en el hub 1, esa llamada
  escribe `primera_conexion`.
- La rama cálida suma `+1` aparte, con una segunda llamada al helper. Nunca
  `puntos_ichika += 3` de golpe.
- La rama fría toca `desaires_cap1`, no los puntos.
- Marcar el evento como consumido — `ichika_visitada_cap1` — para el evento 6 y
  para que el hub ofrezca la revisita corta en lugar del evento entero.
- `ichika_agotada` solo aparece en el instante exacto de la grieta (Movimiento 2
  y, en la rama cálida, otra vez en el Movimiento 4A). Fuera de esos bloques,
  siempre `ichika_neutral` o `ichika_sonrisa` según corresponda.
- Ninguna línea de diálogo, narrador o pensamiento supera dos líneas de caja de
  texto, siguiendo la regla fijada en el evento de Itsuki.
- El intercambio sobre el horario del tren (Movimiento 2) no usa CG ni sprite
  nuevo — reutiliza `ichika_neutral` y `ichika_sonrisa`. Es la única pista de
  que calcula rápido y de memoria; no debe convertirse en una afirmación
  directa dentro de este evento, misma regla que con la punta de Nino.
- **Regla nueva del proyecto, aplicada desde este evento en adelante:** cada
  ruta de hermana lleva un mínimo de dos y un máximo de tres CG nuevos. Revisar
  que Nino, cuando se escriba, cumpla el mismo rango.
