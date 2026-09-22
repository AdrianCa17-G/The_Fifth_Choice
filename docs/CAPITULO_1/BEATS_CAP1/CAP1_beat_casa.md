## Beat fijo · Casa — Noche antes del examen

**Escrito.** Assets pendientes. Se dispara en automático al cerrar el evento
de hermana del Hub 3 — cualquiera que sea — y antes del Evento 6.

**Nota de nombres:** este es el "BEAT casa" del esqueleto del capítulo — la
casa de **Futaro**, con Raiha e Isanari. No confundir con la cocina del
departamento de las quintillizas, que es donde ocurre el beat de la crisis de
Nino. Son dos "casas" distintas y dos beats distintos.

Marcadores como en el resto del capítulo. `[BG]` fondo · `[CG]` ilustración ·
`[SPR]` sprite · `[MUS]` música · `[SFX]` efecto · `[NUEVO]` asset que no existe
todavía · `[$]` línea de código.

---

### Decisiones de este beat

**Qué avanza.** Itsuki mostró el costo en la azotea de sí misma; Nino, el
costo en su propia casa. Este beat es el único que ocurre en el territorio de
Futaro, así que el costo que muestra es el de **él**: la rutina de tutor ya no
se queda en el departamento. Se le está filtrando a su propia familia sin que
se dé cuenta.

**El gesto: le habla a Raiha como le habla a ellas.** No es un lapsus de
nombre — es más incómodo que eso. Es el tono: la pregunta cerrada, señalar el
error sin resolverlo, el mismo método que usa con las cinco. Raiha lo nota
antes que él.

**Isanari genera fricción, por fin.** El prólogo lo dejó anotado y sin
desarrollar. Aquí aparece la primera fricción real: no le pregunta a Futaro
cómo está, solo si el dinero sigue llegando. No hay pelea ni grito — es
Isanari siendo exactamente quien ya era en el prólogo, y eso alcanza.

**No dispara nada mecánico.** El despido temprano se decide en el Evento 6,
leyendo `desaires_cap1` una sola vez al cerrar el capítulo — no aquí. Lo que
sí puede pasar aquí es que, si `desaires_cap1 >= 3`, Futaro tenga una duda
privada sobre su propio trabajo. Nunca se la dice a Raiha. Es una lectura,
nunca una escritura, y nunca corta la partida.

**El cierre innovador: la libreta, no un menú de sabor.** Los menús de los
otros beats existen para desarrollar el trato con una hermana en concreto.
Este beat no habla con ninguna de las cinco, así que ese formato no aplica.
En su lugar, Futaro reabre la libreta de la apertura — el mismo objeto de
`cg_libreta` — y el jugador elige en qué nombre se detiene la vista más
tiempo. No da puntos a nadie: es una reflexión, no una decisión de juego.

**Asimetría intencional en las cinco reflexiones.** Itsuki y Nino tienen beat
fijo propio — pase lo que pase en los hubs, el jugador ya las vio de cerca.
Miku, Yotsuba e Ichika solo tienen contenido si fueron elegidas. Por eso, si
Itsuki o Nino no fueron visitadas en su evento de hub, la reflexión igual
existe (referencia a su beat), en vez de fingir que no pasó nada con ellas.

---

### Movimiento 1 · Llegada

`[BG bg_edificio]` `[MUS stop fadeout 1.0]`

**narrador:** Llegué a casa más tarde de lo normal. Otra vez.

`[BG bg_comedor]` `[MUS cena fadein 2.0]`

**narrador:** El examen era al día siguiente. 

**narrador:** Faltaban horas, no días.

**mc_pensamiento:** Han pasado treinta días. 

**mc_pensamiento:** Contados desde la noche en que anoté los cinco nombres.

**mc_pensamiento:** Mañana sabré si sirvieron de algo.

**narrador:** Raiha estaba en la mesa, con su propio cuaderno abierto y la
cena ya servida y fría.

`[SPR raiha hablando at pj(0.20)]`

**raiha:** ¡Hermanito! Te guardé la cena, pero se enfrió como tres veces.

**mc:** Perdoname Raiha. Se me hizo tarde.

**raiha:** Desde que comenzaste tu tranajo como tutor, siempre se te hace tarde.

**narrador:** No lo dijo con reproche. Lo dijo como quien ya lleva la cuenta.

---

### Movimiento 2 · El gesto

**narrador:** Me senté a comer. Ella no cerró su cuaderno.

`[SPR raiha regano at pj(0.20)]`

**raiha:** Tengo un problema de matemáticas que no me sale.

**mc:** Muéstrame.

**narrador:** Lo dijo con la boca todavía llena. No pensé en cómo lo dije.

**narrador:** Miré la hoja. El error estaba en el segundo paso.

**mc:** ¿Revisaste esta línea?

**raiha:** ¿Cuál?

**mc:** Esta. No te la voy a resolver. Solo mira si el signo está bien.

`[CG NUEVO — cg_raiha_correccion: primer término inferior, desenfocada y
cortada por el borde, la mano de Futaro señalando una línea del cuaderno de
Raiha sin tocar el lápiz. Raiha al frente, de cuerpo entero, mirando la hoja y
después a él, con una expresión a medio camino entre la sorpresa y la gracia.
Luz cálida de comedor, de noche. Un solo personaje con LoRA en el frame,
siguiendo el lenguaje ya validado para escenas con Futaro presente. Sostiene
todo este movimiento.]`

**narrador:** Levantó la vista de la hoja antes de corregir nada.

`[SFX sfx_lapiz_mesa NUEVO volume 1.5]`

**narrador:** Dejó el lápiz sobre la mesa, despacio.

**raiha:** …Hablaste raro.

**mc:** ¿Raro cómo?

**raiha:** Como un profesor. Ni pareces mi hermano cuando dices esas cosas.

**narrador:** Lo dijo sin mala intención. Con la misma naturalidad con la que
señala cualquier otra cosa.

**mc_pensamiento:** No fue un chiste. Se lo tomó como algo raro de verdad.

**mc_pensamiento:** Llevo tres semanas diciéndoles a cinco personas «no te lo
voy a resolver, solo mira si está bien» tantas veces que ya no me sale de otra
forma.

**mc_pensamiento:** Ni siquiera con ella.

**raiha:** ¿Estás bien?

**mc:** Estoy cansado. Nada más.

**narrador:** Volvió a mirar su hoja, ya sin el mismo ánimo de antes.

**raiha:** …Está bien el signo.

**mc:** Entonces revisa el siguiente paso con la misma lógica.

**narrador:** Lo dije otra vez con el mismo tono. 

**narrador:** Esta vez lo noté yo también, medio segundo tarde.

---

### Movimiento 3 · Isanari

`[SFX sfx_puerta_abre volume 1.0]`

**narrador:** Mi padre entró cuando Raiha ya estaba guardando el cuaderno.

`[SPR isanari neutral at pj(0.73)]`

**isanari:** Vaya mc, te ves demasiado cansado.

**isanari:** ¿Como vas? ¿Todo marcha bien en tu trabajo?

**mc:** El examen es mañana.

**isanari:** ¿El tuyo o el de ellas?

**mc:** El de ellas. 

**mc:** El mío ya lo rendí hace un mes, cuando dijiste que sí por mí.

`[SPR isanari sonriendo at pj(0.73)]`

**isanari:** No suenes tan dramático. 

**isanari:** Te va bien, ¿no? El dinero sigue entrando.

**narrador:** No preguntó cómo estaba.

**narrador:** Preguntó si el dinero seguía llegando, en la misma frase.

**mc_pensamiento:** No es que me sorprenda.

**mc_pensamiento:** Es que después de un mes viéndolas a ellas cinco fingir
que no les importa, se siente distinto verlo a él sin fingir nada.

`[SPR raiha regano at pj(0.20)]`

**raiha:** ¡Papá! 

**raiha:** Pregúntale cómo está, no cuánto pagan.

**isanari:** Es la misma pregunta, Raiha. Si le fuera mal, no seguirían
pagando.

**narrador:** Lo dijo sin maldad.

**narrador:** Con la misma lógica fría con la que arregla todo lo demás.

**mc:** Esas cinco van a salir bien.

**isanari:** Eso espero. Cinco veces la tarifa no cae del cielo dos veces.

**narrador:** Se sirvió agua y volvió a su cuarto sin esperar respuesta,
exactamente con la misma calma con la que había entrado.

**mc_pensamiento:** No dijo suerte. No preguntó de qué se trataba el examen.

**mc_pensamiento:** Solo confirmó que el trato seguía en pie desde su lado.

**narrador:** Raiha se quedó mirando la puerta de su cuarto un momento más de
lo necesario.

**raiha:** No le hagas caso.

**mc:** No le hago caso.

**narrador:** Los dos sabíamos que no era del todo cierto.

---

### Movimiento 4 · A solas

`[BG bg_cuarto_mc]` `[MUS stop fadeout 1.5]`

**narrador:** Me encerré en mi cuarto antes de las diez.

**narrador:** Saqué la libreta del cajón. La misma de la primera noche.

`[CG cg_libreta]` `[MUS hogar fadein 3.0 volume 0.7]`

**mc_pensamiento:** Cinco nombres, en columna, con una línea debajo.

**mc_pensamiento:** Treinta días después, la letra sigue siendo la misma.

**mc_pensamiento:** Solo que ahora sé lo que cuesta cada nombre.

**narrador:** Dejé la vista quieta un momento antes de cerrarla.

```
¿En qué nombre se detiene la vista más tiempo?
```

---

**"Ichika"**

if ichika_visitada_cap1:

> **mc_pensamiento:** La encontré dormida en el salón del club, con el guion resbalándole de la mano.
> 
> **mc_pensamiento:** A su lado, dos latas de energizante.
> 
> **mc_pensamiento:** Una de ellas, abollada.
> 
> **mc_pensamiento:** Cuando despertó a medias, dijo que no sabía cuánto más podía seguir así.
> 
> **mc_pensamiento:** No sé si me lo dijo a mí o si se le escapó sin querer.
> 
> **mc_pensamiento:** Después volvió la sonrisa, como si nada.
>
> **mc_pensamiento:** Pero tardó un segundo de más en volver.
> 
> **mc_pensamiento:** Entiendo cómo se siente. Yo también tengo personas a quien cuidar.
> 
> **mc_pensamiento:** Hasta medio dormida, calculó minutos y trenes sin pensarlo dos veces.
> 
> **mc_pensamiento:** Sé que esa cabeza para los números la va a hacer sobresalir en su examen,
> aunque ella no se dé cuenta.


else:
> **mc_pensamiento:** No he interactuado mucho con ella desde el primer día,
>
> **mc_pensamiento:** cuando fingía que nada de esto le importaba.
> 
> **mc_pensamiento:** Sigue actuando igual que siempre frente a mí, sin ninguna grieta de por medio.
> 
> **mc_pensamiento:** No sé si sigue fingiendo o si dejó de hacerlo..

---

**"Nino"**

if nino_visitada_cap1:

> **mc_pensamiento:** Nino me corrigió una frase en inglés. No se lo pedí
> pero lo hizo.
>
> **mc_pensamiento:** Luego, la encontré en una sección de repostería internacional,
> tenia productos con nombres extranjeros, algunos que ni siquiera sabía su significado.
>
> **mc_pensamiento:** La encontré comparando dos cajas de harina, con una
> receta que no es suya escrita a mano.
>
> **mc_pensamiento:** Logré interactuar con ella acerca de los nombres de esos productos.
>
> **mc_pensamiento:** Con dificultad para entablar una conversacion pacifica...
>
> **mc_pensamiento:** Me di cuenta que tiene un talento innato para el ingles.
>
> **mc_pensamiento:** Aunque le cuesta hablarlo de manera fluida, sabe como leerlo y pronunciarlo.
>
> **mc_pensamiento:** Tambien me dijo que ya perdió la cuenta de cuántos tutores vio irse.
>
> **mc_pensamiento:** Yo no le prometí nada, no logré convencerla de lo contrario.
>
> **mc_pensamiento:** Y por último, ese dia, en su cocina, estuve escuchándola pedirle
> a su padre que me echara.
>
> **mc_pensamiento:** Se frenó antes de decir por qué.
>
> **mc_pensamiento:** Pero entendí que no está enojada conmigo.
>
> **mc_pensamiento:** Ella es un tren de emociones que nunca frena.

else:

> **mc_pensamiento:** No fui a buscarla al centro comercial.
>
> **mc_pensamiento:** Pero igual terminé en su cocina, escuchándola
> pedirle a su padre que me echara.
>
> **mc_pensamiento:** Se frenó antes de decir por qué.
>
> **mc_pensamiento:** Pero entendí que no está enojada conmigo.

---

**"Miku"**

if miku_visitada_cap1:

> **mc_pensamiento:** La encontré en la biblioteca.
>
> **mc_pensamiento:** Me habló de historia como si nadie fuera a interrumpirla.
>
> **mc_pensamiento:** Después se disculpó por hablar.
>
> **mc_pensamiento:** Como si eso también fuera un error suyo.
>
> **mc_pensamiento:** Es una chica muy reservada, pero cuando la conoces es
> una persona totalmente interesante.
>
> **mc_pensamiento:** Confío en que hará brillar sus conocimientos de historia.

else:

> **mc_pensamiento:** Sigo sin saber mucho de ella.
>
> **mc_pensamiento:** Los audífonos que lleva puestos en su cuello.
>
> **mc_pensamiento:** Y el libro que escondió la primera noche.
>
> **mc_pensamiento:** Ella es todo un misterio.

---

**"Yotsuba"**

if yotsuba_visitada_cap1:

> **mc_pensamiento:** La encontré corriendo sola en la pista, mucho después
> de que el club se fuera a casa.
>
> **mc_pensamiento:** Lleva las vueltas anotadas en la muñeca. Si no, pierde
> la cuenta.

else:

> **mc_pensamiento:** Sigo sin saber qué hace cuando nadie la mira.
>
> **mc_pensamiento:** Solo la sonrisa que le pone a todo, incluso a lo que no
> debería sonreírse.

---

"Itsuki"

if itsuki_visitada_cap1:

> **mc_pensamiento:** La encontré atascada en un ejercicio de ciencias.
>
> **mc_pensamiento:** Sola en el aula.
>
> **mc_pensamiento:** Con tres intentos tachados y la misma respuesta
> equivocada las tres veces.
>
> **mc_pensamiento:** No era que no supiera del tema.
>
> **mc_pensamiento:** El resto del cuaderno estaba lleno de ejercicios resueltos.
>
> **mc_pensamiento:** Uno detrás de otro, sin un solo error.
>
> **mc_pensamiento:** Le dije dónde estaba el error y lo entendió al segundo,
> como si solo le hubiera faltado que alguien más lo dijera en voz alta.
>
> **mc_pensamiento:** Me dejó ayudarla sin decir gracias.
>
> **mc_pensamiento:** Con ella, eso ya es bastante.
>
> **mc_pensamiento:** Y mas adelante, la encontré en la azotea, con un cuaderno que
>  no llegó a abrir.
>
> **mc_pensamiento:** Logramos dialogar y entender nuestras diferencias.
>
> **mc_pensamiento:** Ya no le queda ningún sitio donde no tenga que fingir
> que está bien.
>


else:

> **mc_pensamiento:** No fui a buscarla al aula.
>
> **mc_pensamiento:** Pero igual la encontré en la azotea.
>
> **mc_pensamiento:** Con un cuaderno que no llegó a abrir.
>
> **mc_pensamiento:** Ya no le queda ningún sitio donde no tenga que fingir
> que está bien.

---

**narrador:** Me quedé mirando ese nombre más tiempo que los otros cuatro.

if desaires_cap1 >= 3:

> **mc_pensamiento:** No sé si mañana esto sigue siendo mi trabajo.
>
> **mc_pensamiento:** Ninguna aprobó todavía.
>
> **mc_pensamiento:** Y las cinco llegan a este último tramo por caminos que yo elegí.
>
> **mc_pensamiento:** Uno a uno, sin preguntarles si querían que fuera así.
>
> **mc_pensamiento:** Si mañana me voy, me voy sabiendo exactamente por qué.
>
> **mc_pensamiento:** Todo el peso de mis decisiones caerán mañana.

---

### Movimiento 5 · Cierre

**mc_pensamiento:** Cerré la libreta y apagué la lámpara.

**narrador:** Desde el otro cuarto, todavía se oía a Raiha ordenando sus
cosas para el día siguiente, como si mañana fuera un día cualquiera.

**mc_pensamiento:** Para ella lo es.

**mc_pensamiento:** Ojalá pudiera decir lo mismo.

`[MUS stop fadeout 3.0]`

**narrador:** Mañana será el examen.

`→ Sale al Evento 6.`

---

### Assets del beat

| Asset | Tipo | Estado | Nota |
|---|---|---|---|
| `bg_edificio` / `bg_comedor` / `bg_cuarto_mc` | BG | ya existen | Sin cambios, del prólogo |
| `hogar` / `cena` | BGM | ya existen | `hogar` reaparece por primera vez desde el prólogo, a propósito — ver nota abajo |
| `cg_libreta` | CG | ya existe | Reutilizada tal cual de la apertura, mismo objeto físico |
| `cg_raiha_correccion` | CG | pendiente | Movimiento 2. POV de Futaro, mano señalando la hoja de Raiha |
| `sfx_lapiz_mesa` | SFX | pendiente | El lápiz de Raiha al dejarlo sobre la mesa |

Reutilizados sin tocar: `sfx_puerta_abre`, `raiha hablando`, `raiha regano`,
`isanari neutral`, `isanari sonriendo`.

**Por qué no hay BGM nueva.** `hogar` es el tema de Futaro, y la guía de audio
es explícita: solo significa algo si se usa poco. No sonó en todo el
capítulo — su regreso aquí, exactamente cuando reabre la misma libreta de la
apertura, es el eco que le da sentido a la regla en vez de romperla. Crear
una pista nueva para este momento habría sido más caro y habría dicho menos.

**`cg_raiha_correccion`** — sigue el lenguaje ya validado para Futaro en
cuadro (`cg_manija_edificio`, `cg_estudio_biblioteca`, `cg_itsuki_reto`): su
mano en primer término, desenfocada, cortada por el borde. Lo nuevo es el
contexto — es la primera vez que ese lenguaje se usa en una escena de familia
y no de tutoría, y esa mezcla es justo el punto de la escena.

**`sfx_lapiz_mesa`** — distinto de `sfx_taza_mesa` (cerámica) y de
`sfx_mochila_suelo` (tela): esto es un golpe seco y pequeño, de madera contra
madera. Marca el instante exacto en que Raiha nota el cambio de tono, no un
golpe de tensión como los otros dos.

---

### Notas de implementación

- Este beat **no otorga puntos a ninguna hermana**, en ningún branch del
  cierre de la libreta. Las cinco reflexiones son solo lectura de las
  variables `*_visitada_cap1`; ninguna las escribe.
- `desaires_cap1 >= 3` en el Movimiento 4 es **solo lectura**, igual que en
  el beat de Nino. No dispara ningún final, no salta de label, no interrumpe
  el flujo — es una línea de más en el monólogo interno. El despido temprano
  se sigue decidiendo únicamente en el Evento 6, leyendo la misma variable
  una vez.
- El menú de los cinco nombres se implementa como un `menu:` normal con
  cinco opciones fijas, siempre visibles sin importar qué se haya jugado:

  ```renpy
  menu:
      "Ichika":
          if ichika_visitada_cap1:
              mc_pensamiento "..."
          else:
              mc_pensamiento "..."
      "Nino":
          if nino_visitada_cap1:
              mc_pensamiento "..."
          else:
              mc_pensamiento "..."
      # ... Miku, Yotsuba, Itsuki igual
  ```

  El jugador elige **una sola** opción y el guion sigue directo al chequeo de
  `desaires_cap1` y al cierre. No hace falta permitir ver las cinco.
- Requiere los mismos cinco flags `*_visitada_cap1` ya señalados como
  pendientes en los beats de Itsuki y Nino. Con este beat, los tres
  documentos ya dependen de ellos — declararlos en `00_definiciones.rpy`
  antes de compilar cualquiera de los tres.
- Este beat se dispara **una sola vez**, al cerrar el evento del Hub 3, antes
  de saltar al label del Evento 6.
