## Beat fijo · La crisis de Nino — Departamento, cocina

**Escrito.** Assets pendientes. Se dispara en automático al cerrar el evento
de hermana del Hub 2 — cualquiera que sea — y antes de que se abra el Hub 3.

Marcadores como en el resto del capítulo. `[BG]` fondo · `[CG]` ilustración ·
`[SPR]` sprite · `[MUS]` música · `[SFX]` efecto · `[NUEVO]` asset que no existe
todavía · `[$]` línea de código.

---

### Decisiones de este beat

**Qué es "la crisis".** No es algo que le pasa a Nino: es algo que ella
**hace**. Ya la vimos actuar antes de sentir — en el prólogo organizó a las
cinco para sabotear el diagnóstico y amenazó con llevarle las hojas a su
padre. Aquí repite el gesto en serio: sin avisarle a nadie, va directo a
Maruo y le pide que corte la tutoría antes de que sus hermanas se encariñen
con alguien que, cree ella, también se va a ir. No la dispara nada que Futaro
haga mal. La dispara su propio miedo a que el patrón se repita.

**Ella es quien activa el aviso de Maruo, sin saberlo.** Al ir a buscar a su
padre, lo pone en la misma habitación que Futaro en el momento exacto en que
Maruo decide, si corresponde, soltar la advertencia. Nino no es consciente de
haber activado nada — desde su punto de vista, solo fue a pelear su propia
batalla y salió mal.

**Se repite el recurso de "habla de más y se corta".** Igual que en su evento
de hub, pero más largo: esta vez se sostiene varias líneas antes de frenarse,
porque la presión es mayor.

**Restricción dura, heredada de su evento de hub.** Ninguna rama puede dejarla
confiando en Futaro. Lo que cambia aquí no es la confianza — es que ella
decide no llevar la pelea hasta el final. Se frena a sí misma, no a él.

**No se gasta la disculpa.** Sigue guardada desde el prólogo.

**El aviso de Maruo es condicional y puramente narrativo.** Se activa con
`desaires_cap1 >= 2` — es decir, si el jugador ya fue frío en los dos eventos
de hermana que van del capítulo (Hub 1 y Hub 2). No escribe ninguna variable
nueva, solo lee. El jugador que va bien nunca ve esta rama.

**Corrección de redacción sobre el README.** El texto original decía que
Maruo comenta "que lleva un mes" sin ver diferencia. A esta altura del
capítulo van poco más de dos semanas de los treinta días, así que la línea de
Maruo se ajusta a "más de una semana" en vez de "un mes", conservando la
misma función de aviso.

**Maruo repite la amenaza original, más afilado.** No es una amenaza nueva —
es la misma del prólogo ("si una reprueba, quedas fuera"), pero esta vez la
dice como quien no piensa repetirla una tercera vez. Es la última advertencia
antes de que la condición se resuelva de verdad al cierre del evento 6.

**Micro-variante — corregida respecto al patrón usado con Itsuki.** Ahí
usamos `primera_conexion == "itsuki"` porque su beat iba justo después del
Hub 1, donde solo pudo haber pasado un evento. Este beat va después del
Hub 2, así que Nino pudo haber sido la elección del Hub 1 **o** del Hub 2.
Comprobar solo `primera_conexion` dejaría fuera el caso más probable — que
la hayan visitado recién, en el Hub 2 — así que aquí la condición es
simplemente `nino_visitada_cap1`, sin importar en qué hub ocurrió.

---

### Movimiento 1 · Llegada

`[BG bg_edificio]` `[MUS stop fadeout 1.0]`

**narrador:** Llegué al departamento a la hora de siempre.

**narrador:** La puerta estaba entreabierta. Nadie la había cerrado del todo.

`[SFX sfx_manija volume 1.5]`

**narrador:** Antes de terminar de abrirla, escuché voces desde el fondo.

**mc_pensamiento:** Una era de Maruo. Grave, pareja, sin subir nunca de tono.

**mc_pensamiento:** La otra era de Nino. Y esa sí estaba subiendo.

**narrador:** Me quedé en el umbral un segundo de más.

**mc_pensamiento:** Podía tocar el timbre y anunciarme.

**mc_pensamiento:** O podía escuchar primero y decidir después.

**narrador:** Elegí lo segundo.

`[BG bg_departamento]`

**nino:** …y no me importa lo que hayas firmado con él. Puedes deshacerlo.

**maruo:** No.

**nino:** ¡Es un tutor, no un contrato de matrimonio!

**maruo:** Es exactamente un contrato. Y no lo voy a romper porque a ti no te
guste su cara.

**narrador:** Me acerqué lo suficiente para ver sin que me vieran a mí.

`[CG NUEVO — cg_nino_confrontacion_cocina: Nino de pie frente a Maruo, en la
cocina de la sala principal, con la isla de la cocina entre los dos. Ella con
los brazos cruzados con fuerza, mandíbula tensa. Maruo de perfil, sereno,
traje sin corbata, con una taza de café a medio terminar en la mano. Luz de
tarde entrando por el ventanal del fondo. Dos personajes en el frame, cada
uno con su propia receta ya validada del proyecto — Nino con su LoRA de
personaje, Maruo con su ficha de prompt establecida. Futaro no aparece:
observa desde fuera de cuadro. Sostiene todo el movimiento 1.]`

**mc_pensamiento:** No es por mi cara. Es por algo que no tiene nada que ver
conmigo.

**nino:** No se trata de su cara. Se trata de que va a durar lo mismo que los
otros cuatro, y ellas van a volver a creer que esta vez sí.

**maruo:** Eso ya lo decidiré yo, cuando corresponda.

**nino:** ¡Tú nunca estás aquí para verlo!

**narrador:** Ahí sí subió la voz de verdad. La única vez que la escuché
gritarle a su padre.

---

### Movimiento 2 · Maruo

if desaires_cap1 >= 2:

> **narrador:** Fue entonces cuando Maruo levantó la vista y me encontró en
> la puerta.
>
> `[SPR nino neutral at pj(0.35)]` `[MUS contrato fadein 2.0]`
>
> **maruo:** Ya que estás aquí, ahorrémonos la actuación.
>
> **mc:** No vine a interrumpir nada.
>
> **maruo:** Ya la interrumpiste con solo entrar.
>
> **narrador:** Dejó la taza sobre la isla de la cocina, despacio, sin
> apurarse.
>
> **maruo:** Llevas más de una semana. No veo ningún cambio.
>
> **mc:** Los exámenes son en tres semanas, no mañana.
>
> **maruo:** No te pedí un cronograma. Te pedí resultados.
>
> **narrador:** Nino miraba entre los dos, sin intervenir por primera vez en
> toda la conversación.
>
> **maruo:** Las condiciones te las dije el primer día. No las voy a repetir
> una tercera vez.
>
> **maruo:** Si una sola de mis hijas reprueba, se acabó. Ese día no hay
> discusión ni segunda oportunidad.
>
> **narrador:** Lo dijo exactamente con el mismo tono que usó para cerrar la
> puerta esa primera noche.
>
> **mc_pensamiento:** No subió la voz ni una vez. No hacía falta.
>
> **narrador:** Recogió la taza y salió de la cocina sin esperar respuesta,
> dándonos la espalda a los dos por igual.
>
> `[SFX sfx_puerta_cierra volume 1.0]`
>
> **mc_pensamiento:** Esa era la última vez que lo iba a decir.
>
> **mc_pensamiento:** Y los dos lo sabíamos.

else:

> **narrador:** Maruo no llegó a notar que yo estaba en la puerta, o decidió
> no darse por enterado.
>
> **maruo:** No he visto ningún motivo todavía para cambiar nada.
>
> **nino:** ¡Ese es el problema! ¡Que nunca ves ningún motivo hasta que ya es
> tarde!
>
> **maruo:** Cuando lo sea, actuaré. Hasta entonces, esta conversación está
> cerrada.
>
> **narrador:** Se sirvió el resto del café en el fregadero y salió de la
> cocina sin mirar a ninguno de los dos.
>
> `[SFX sfx_puerta_cierra volume 1.0]`
>
> **mc_pensamiento:** No dijo mi nombre en toda la conversación.
>
> **mc_pensamiento:** Como si yo no fuera parte del problema que estaban
> discutiendo.

**narrador:** Nino se quedó mirando el pasillo por donde se había ido su
padre, todavía con los brazos cruzados.

**mc:** Buenas tardes.

`[SPR nino neutral at pj(0.5)]`

**nino:** No es un buen momento.

**mc:** Ya lo noté.

---

### Movimiento 3 · La grieta

**narrador:** Entré del todo a la cocina. Ella no se movió de donde estaba.

`[SFX sfx_taza_mesa NUEVO volume 2.0]`

**narrador:** Dejó su propia taza sobre la isla con más fuerza de la
necesaria. El golpe sonó más alto que cualquier cosa que hubiera dicho.

**nino:** Vas a preguntarme qué fue eso.

**mc:** No hacía falta que me lo explicaras. Escuché la mitad desde la
puerta.

**nino:** Entonces ya sabes lo que pienso de ti.

**mc:** Sé lo que le dijiste a tu padre. No es lo mismo.

`[SPR nino molesta at pj(0.5)]`

**nino:** Da igual. El resultado es el mismo: quiero que te vayas.

**mc:** Tu padre acaba de decir que no.

**nino:** Mi padre no tiene que vivir con esto todos los días. Yo sí.

**narrador:** Se sentó en uno de los bancos de la isla, de golpe, como si las
piernas hubieran dejado de sostenerla el tiempo justo.

`[MUS NUEVO — guardia fadein 2.5 volume 0.3]`

**nino:** No es porque seas malo en esto. Ni siquiera es porque me caigas
mal, aunque me caes mal.

**nino:** Es que ya vi esto pasar cuatro veces, y las cuatro veces fue igual.

**nino:** Ichika finge que no le importa hasta que le importa. Yotsuba se
esfuerza el doble para compensar algo que no puede compensar. Miku se cierra
todavía más, y ya estaba bastante cerrada.

**nino:** E Itsuki… Itsuki se lo toma como si fuera personal, porque para
ella todo lo es.

**narrador:** Hablaba rápido, sin las pausas que suele dejar entre frase y
frase.

`[CG NUEVO — cg_nino_grieta_cocina: Nino sentada sola en el banco de la
cocina, de perfil, con las manos alrededor de la taza sin bebérsela. Mirada
baja, hombros menos rectos que su postura habitual. Misma luz de tarde que
`cg_nino_confrontacion_cocina`, pero encuadre cerrado solo sobre ella —
Maruo ya no está, y Futaro tampoco entra en cuadro. Sostiene el resto del
movimiento 3.]`

**nino:** Y cuando se van, a mí me toca juntar los pedazos de las cuatro,
porque soy la única que no se ilusionó nunca.

**nino:** Alguien tiene que quedarse con la cabeza fría. Siempre soy yo.

**nino:** Y estoy cansada de ser la única que ve venir el golpe antes de que
llegue.

**narrador:** Se detuvo de golpe, con la taza a medio camino de la boca.

`[SPR nino neutral at pj(0.5)]`

**nino:** …

**nino:** No dije nada de esto.

**mc:** Lo dijiste todo.

**narrador:** No contestó. Bajó la taza sin haber bebido nada.

**mc_pensamiento:** No está exagerando. No conmigo, al menos.

**mc_pensamiento:** Está describiendo un patrón que ya vio cumplirse cuatro
veces seguidas, y la única variable que cambia cada vez es el nombre de quien
se va.

---

### Movimiento 4 · La decisión

**narrador:** Se puso de pie y se acomodó el delantal, como quien intenta
recomponer algo que ya se salió de su sitio.

**nino:** ¿Y bien? ¿Vas a decir que esta vez es distinto?

**mc_pensamiento:** Si digo que sí, soy el quinto tutor prometiendo lo mismo
que los cuatro anteriores.

**mc_pensamiento:** Si no digo nada, confirmo que tiene razón en no confiar.

**mc_pensamiento:** No hay una respuesta que la deje tranquila. Solo hay una
que no la deje peor.

```
MENÚ — ¿Cómo respondes?

A) "No voy a decirte que esta vez es distinto. Voy a decirte que entiendo por qué te toca ser tú la que se queda con la cabeza fría."   [CÁLIDA]
B) No decir nada. Recoger la taza que dejó y llevarla al fregadero.                                                                      [TIBIA]
C) "Entonces deja de juntar los pedazos de las demás y ocúpate de los tuyos."                                                            [FRÍA]
```

---

### Movimiento 4A · Rama cálida

`[MUS guardia — sostener volumen]`

**mc:** No voy a decirte que esta vez es distinto.

`[SPR nino neutral at pj(0.5)]`

**nino:** …¿No?

**mc:** No. Ya perdiste la cuenta de cuántas veces escuchaste esa frase.

**mc:** Pero entiendo por qué te toca a ti ser la que se queda con la cabeza
fría mientras las otras cuatro se ilusionan.

**nino:** No es que me toque. Es que alguien tiene que hacerlo.

**mc:** Es lo mismo. Solo que tú lo elegiste sin que nadie te lo pidiera.

**narrador:** Se quedó mirándome un momento, con la misma cara con la que
mira una etiqueta que no termina de convencerla.

`[SPR nino_nerviosa at pj(0.5)]`

**nino:** …No vas a convencerme de que confíe en ti con dos frases bonitas.

**mc:** No lo intenté.

**nino:** Bien. Que quede claro.

**narrador:** Recogió su propia taza y la llevó al fregadero, dándome la
espalda.

**nino:** Esto no cambia nada de lo que le dije a mi padre.

**mc:** No dije que lo hiciera.

**narrador:** Pero no volvió a mencionar lo de deshacer el contrato en toda
la tarde.

---

### Movimiento 4B · Rama tibia

**narrador:** No dije nada. Rodeé la isla y recogí la taza que había dejado a
medio terminar.

`[SPR nino neutral at pj(0.5)]`

**nino:** ¿Qué haces?

**mc:** Llevarla al fregadero. No hacía falta que la reventaras contra la
mesa.

**nino:** No la reventé.

**mc:** Sonó como si lo hubieras hecho.

**narrador:** No contestó a eso. Se quedó apoyada contra la isla, con los
brazos cruzados otra vez, pero menos tensos que antes.

**nino:** No esperaba que te quedaras después de escuchar eso.

**mc:** ¿Preferías que me fuera?

**nino:** No dije eso tampoco.

**narrador:** Terminé de lavar la taza en silencio. Ella no se movió de su
sitio, pero tampoco volvió a sacar el tema con su padre.

**mc_pensamiento:** No dijo nada más de lo que se le escapó.

**mc_pensamiento:** Y yo tampoco le pregunté.

---

### Movimiento 4C · Rama fría

*(sin efecto en `desaires_cap1` — ver nota en "Notas de implementación")*

**mc:** Entonces deja de juntar los pedazos de las demás y ocúpate de los
tuyos.

**narrador:** Lo dije pensando que la iba a hacer reaccionar.

**narrador:** Reaccionó, pero no como esperaba.

`[SPR nino molesta at pj(0.5)]`

**nino:** …

**nino:** Genial. Ni un día entero de conocerme y ya sabes exactamente qué
decirme para que me calle.

**mc:** No dije que te callaras.

**nino:** Dijiste que me ocupara de lo mío. Es la forma elegante de lo mismo.

**narrador:** Recogió su taza ella misma, sin dejar que me acercara.

**nino:** Ahora entiendo por qué mi padre firmó contigo. Hablan el mismo
idioma.

**mc_pensamiento:** No sé si eso es un insulto o la descripción más precisa
que me ha dado nadie de esta casa.

**narrador:** Se fue a su habitación sin volver a mirarme, con la taza
todavía en la mano.

**mc_pensamiento:** Le dije justo lo que un padre le diría.

**mc_pensamiento:** Y ella me contestó justo lo que le contesta a un padre.

---

### Movimiento 5 · Cierre

*(común a las tres ramas; la última línea cambia)*

`[MUS stop fadeout 2.0]`

**narrador:** Me quedé un rato más en la cocina, solo, con el ruido del
edificio de fondo.

**mc_pensamiento:** Vino a pedir que me fueran. Su padre dijo que no.

**mc_pensamiento:** Y aun así, la que se quedó dando explicaciones fui yo.

if desaires_cap1 >= 2:

> **mc_pensamiento:** Maruo no va a repetir esa advertencia una tercera vez.
>
> **mc_pensamiento:** La próxima vez que hable de esto, no va a ser una
> advertencia.

*Cierre A (cálida):*

**mc_pensamiento:** No confía en mí. No esperaba que un par de frases
cambiara eso.

**mc_pensamiento:** Pero dejó de insistir con lo de mi padre. Con ella, eso
también cuenta como algo.

*Cierre B (tibia):*

**mc_pensamiento:** Lavé una taza y no dijimos nada importante.

**mc_pensamiento:** Con ella, nunca se sabe si el silencio es una tregua o
solo eso: silencio.

*Cierre C (fría):*

**mc_pensamiento:** Le dije justo lo que temía escuchar de un adulto más.

**mc_pensamiento:** Confirmé el patrón que llevaba cuatro veces viendo
cumplirse, en la primera oportunidad que tuve.

`→ Vuelve al hub.`

---

### Assets del beat

| Asset | Tipo | Estado | Nota |
|---|---|---|---|
| `bg_edificio` / `bg_departamento` | BG | ya existen | Sin cambios. La cocina es parte del mismo loft, no hace falta un fondo aparte |
| `cg_nino_confrontacion_cocina` | CG | pendiente | Movimiento 1-2. Nino y Maruo en la isla de la cocina |
| `cg_nino_grieta_cocina` | CG | pendiente | Movimiento 3. Ella sola, ya sin Maruo ni Futaro en cuadro |
| `guardia` | BGM | pendiente | Entra solo cuando ella se explica de más. Nunca antes, nunca con Futaro razonando |
| `sfx_taza_mesa` | SFX | pendiente | La taza golpeando la isla de la cocina |

Reutilizados sin tocar: `sfx_manija`, `sfx_puerta_cierra`, `contrato`, `nino
neutral`, `nino molesta`, `nino_nerviosa`.

**`cg_nino_confrontacion_cocina`** — a diferencia de las CG con Futaro en
cuadro, aquí no hace falta esconderlo: es Maruo quien acompaña a Nino, y
Maruo ya tiene su propia receta de generación validada desde el prólogo
(LoRA de serie a 0.1, sin LoRA de personaje). Es la primera vez del proyecto
en que dos personajes con LoRA propio comparten un CG que no es el grupo
completo de las cinco — mantiene el criterio de "cada uno por su receta
individual", sin apilar nada por región.

**`cg_nino_grieta_cocina`** — vuelve al estándar de un solo personaje una vez
que Maruo se retira. La postura es la clave: manos alrededor de la taza sin
beberla, hombros menos rectos que su neutral de siempre. Es el mismo
principio de silueta que ya rige el resto del elenco.

**`guardia`** — pensada para sonar solo en este tipo de momento: cuando
alguna de las cinco explica, sin quererlo, por qué se protege. No es
`descubrimiento` porque esa pista queda reservada a los cinco eventos de
hermana en sentido estricto; esta es distinta a propósito, para no diluir el
significado de la otra. Entra bajo, por debajo de 0.35, y sale en cuanto ella
se corta a mitad de frase.

**`sfx_taza_mesa`** — un solo golpe seco de cerámica sobre superficie dura,
sin rebote. Marca el instante exacto en que la tensión de la escena se vuelve
física antes de volverse verbal.

---

### Notas de implementación

- Este beat **no otorga puntos** en ninguna rama, y **tampoco toca
  `desaires_cap1`** — ni siquiera en la rama fría. El README fija esa
  variable exclusivamente a "los tres eventos" de hermana del capítulo (los
  de hub); si un beat también la incrementara, el contador podría superar 3
  y romper el cálculo de "3 de 3" que dispara el despido temprano. La rama
  fría de este beat es fría solo en el tono, no en la mecánica.
- El chequeo del aviso de Maruo **solo lee** `desaires_cap1`, nunca lo
  escribe:

  ```renpy
  if desaires_cap1 >= 2:
      # rama del aviso serio — jump a label_beat_nino_aviso
  else:
      # rama sin aviso — jump a label_beat_nino_sin_aviso
  ```

- El chequeo de la micro-variante final (`if desaires_cap1 >= 2` en el
  Movimiento 5) es independiente del anterior: puede volver a evaluarse sin
  problema porque la variable no cambió entre medio.
- La condición de reconocimiento de que Nino ya fue visitada usa solo
  `nino_visitada_cap1`, **sin** combinarla con `primera_conexion` — a
  diferencia del beat de Itsuki, aquí sí importa distinguir si fue el Hub 1 o
  el Hub 2, porque ambos son posibles en este punto del capítulo. (Este beat,
  tal como está escrito arriba, no llegó a necesitar esa línea de
  reconocimiento explícita porque el contenido ya funciona igual en los dos
  casos — pero si más adelante se agrega una línea que dependa de ello, usar
  `nino_visitada_cap1` solo, nunca `primera_conexion`.)
- Requiere que `nino_visitada_cap1`, `itsuki_visitada_cap1`,
  `miku_visitada_cap1`, `yotsuba_visitada_cap1` e `ichika_visitada_cap1`
  existan como `default = False` en `00_definiciones.rpy`. Ya se señaló esto
  mismo para el beat de Itsuki; siguen pendientes de declarar antes de que
  compile cualquiera de los dos.
- `nino_nerviosa` es el mismo sprite de su evento de hub — no hace falta uno
  nuevo para este beat, y no debería usarse fuera de un instante de grieta
  real, aquí o allá.
