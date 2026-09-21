## Beat fijo · Itsuki — Azotea, día siguiente

**Escrito.** Assets pendientes. Se dispara en automático al cerrar el primer
evento de hermana que el jugador elija en el Hub 1 — cualquiera que sea, Itsuki
incluida — y antes de que se abra el Hub 2.

Marcadores como en el resto del capítulo. `[BG]` fondo · `[CG]` ilustración ·
`[SPR]` sprite · `[MUS]` música · `[SFX]` efecto · `[NUEVO]` asset que no existe
todavía · `[$]` línea de código.

---

### Decisiones de este beat

**No depende del evento que el jugador jugó, pero puede reconocerlo.** No hay
ramificación real: la escena es una sola, con una micro-variante de una sola
línea si `primera_conexion == "itsuki"` y `itsuki_visitada_cap1` es `True`. Fuera
de esa línea, el guion es idéntico se haya visitado a quien se haya visitado.

**Este beat pesa más que uno cualquiera, a propósito.** No hay garantía de que
el jugador vuelva a elegir a Itsuki en ningún hub del capítulo. Si no lo hace,
esta escena es su única aparición real hasta el evento 6. El guion se escribe
asumiendo ese peor caso, no el promedio.

**Sin grieta.** La grieta es propiedad de su evento de hub y no se repite aquí.
Lo que hay en su lugar es un gesto: algo que el jugador lee sin que nadie lo
explique. No hace falta que ella se abra para que el jugador entienda que la
rutina también la está desgastando a ella.

**El gesto: la azotea deja de ser su descanso.** En el prólogo, subía ahí a
alejarse de todo, Futaro incluido. Aquí sube con el cuaderno. El único sitio
del instituto donde no estudiaba dejó de serlo. Eso dice del peso de las tres
semanas mucho más que cualquier línea de diálogo.

**No se gasta la disculpa.** Sigue guardada desde el prólogo. Futaro no admite
nada de lo que pasó esa mañana ni la mañana siguiente.

**Registro de Itsuki sin romperse.** Sigue en oración cerrada, sujeto-verbo-
punto. No hay quiebre formal aquí — eso también pertenece al evento de hub. Lo
que sí puede pasar es que una frase se acorte por cansancio, no por grieta: la
diferencia es que se corta porque está agotada, no porque se le escape algo.

**Menú cosmético, sin puntos.** Tres sabores, reconvergen. Igual que los del
prólogo.

---

### Movimiento 1 · Llegada

`[BG bg_azotea]`

**narrador:** Subí a la azotea a la hora del almuerzo, más por costumbre que por
otra cosa.

**mc_pensamiento:** Desde el primer día, es el único sitio del instituto donde
nadie me pide nada.

**narrador:** La puerta ya estaba abierta.

`[CG NUEVO — cg_itsuki_azotea_cuaderno: Itsuki sentada contra la valla, de
perfil, con un cuaderno abierto sobre las rodillas que no está mirando. Luz de
mediodía, cielo despejado. Encuadre limpio, sin Futaro en cuadro — es él quien
la descubre desde la puerta. Sostiene todo el movimiento 1.]`

**mc_pensamiento:** Ahí estaba. Con el cuaderno.

**mc_pensamiento:** El mismo cuaderno de ciencias que siempre lleva encima.

**narrador:** No lo estaba leyendo.

**narrador:** Lo tenía abierto en una página y la vista en otro lado.

**mc_pensamiento:** La primera vez que subí aquí, ella dijo que venía a tomar aire.

**mc_pensamiento:** A alejarse de gente desagradable.

**mc_pensamiento:** Esa gente desagradable era yo.

**mc_pensamiento:** Y hoy trajo el cuaderno de todas formas, al mismo sitio
del que dijo que venía a escapar.

**mc_pensamiento:** Sin nada de comer al lado.

**mc_pensamiento:** Ya van varias veces que la veo así, en apenas unos días.

`[SFX sfx_mochila_suelo NUEVO volume 1.5]`

**narrador:** Me senté a un par de metros, sin decir nada todavía.

`[SPR itsuki neutral at pj(0.5)]`

**itsuki:** No te oí llegar.

**mc:** No hice ruido a propósito.

**itsuki:** Da igual. Ya estás aquí.

**narrador:** Lo dijo sin la hostilidad de siempre. Sonó más a un hecho que a
una queja.

---

### Movimiento 2 · El peso compartido

**mc:** Pensé que este sitio era donde no estudiabas.

`[SPR itsuki molesta at pj(0.5)]`

**itsuki:** Y lo era.

**narrador:** Cerró el cuaderno, pero no lo guardó.

**narrador:** Se quedó con la mano encima, como si todavía no hubiera decidido qué hacer con él.

**itsuki:** Ya no me queda ningún sitio que no lo sea.

**narrador:** Fue una frase corta. Más corta que las suyas de costumbre.

**mc_pensamiento:** No se cortó a media idea. La terminó.

**mc_pensamiento:** Simplemente no tenía más que decir, y eso es distinto.

**narrador:** Extendí la mano hacia la mochila y saqué mi propio libro.

**itsuki:** ¿Tú también?

**mc:** Yo desde antes de que existiera este trabajo.

**narrador:** No dijo nada a eso. Pero tampoco volvió a abrir su cuaderno.

**mc:** No hay mesa aquí arriba.

**itsuki:** No hace falta mesa para tener un cuaderno abierto.

**mc:** Pero no lo tienes abierto para leerlo.

**itsuki:** …

**narrador:** No contestó. 

**narrador:** Cambió el cuaderno de posición sobre las rodillas, como si
reacomodarlo fuera, de algún modo, una respuesta.

**mc_pensamiento:** Lo trajo por costumbre, no porque pensara usarlo.

**mc_pensamiento:** Como quien ya no sabe estar en un sitio sin la excusa de
tener algo que hacer ahí.

`[CG NUEVO — cg_itsuki_azotea_manos: punto de vista de Futaro, sentado. En
primer término inferior, desenfocada y cortada por el borde, la correa de su
propia mochila en el suelo junto a él. Itsuki al fondo, de perfil contra la
valla, con las manos apoyadas sobre el cuaderno cerrado, sin abrirlo. Misma luz
que `cg_itsuki_azotea_cuaderno`, encuadre mucho más cerrado. Sostiene el resto
del movimiento 2.]`

**narrador:** Tenía las manos apoyadas sobre la tapa, quietas. Sin una sola
mancha de tinta.

**mc_pensamiento:** No había escrito nada en toda la mañana.

**mc_pensamiento:** Ella, que llena una hoja de tachones antes que nadie
termine la primera línea.

`[MUS NUEVO — tregua fadein 3.0 volume 0.3]`

**narrador:** El viento seguía sonando igual que siempre aquí arriba, pero por
debajo empezó a sonar algo más...

**narrador:** Bajo, casi nada.

**itsuki:** ¿Vas a preguntarme por qué lo traje?

**mc:** No.

**itsuki:** …¿Por qué no?

**mc:** Porque ya lo sé.

**narrador:** No contestó. Pero no volvió a preguntar tampoco.

if primera_conexion == "itsuki" and itsuki_visitada_cap1:

> **itsuki:** Ya me ayudaste con el ejercicio el otro día. No hace falta que
> sigas viniendo a comprobar cómo voy.
>
> **mc:** No vine a comprobar nada.
>
> **narrador:** No pareció creérselo del todo. Pero no insistió.

else:

> **itsuki:** No voy a preguntarte a ti dónde has estado estos días.
>
> **mc:** No te lo iba a contar de todas formas.
>
> **narrador:** Los dos volvieron a mirar al frente, cada uno con su propio
> libro cerrado sobre las piernas.

**mc_pensamiento:** Llevamos pocos días de esto y ya la convivencia se volvió
jornada completa para las dos partes.

**mc_pensamiento:** Ella tampoco tiene dónde bajar la guardia. Yo tampoco.

**narrador:** Nos quedamos ahí un rato largo, sin abrir ninguno de los dos
libros.

**narrador:** El viento se llevó una hoja suelta de mi cuaderno hasta la
valla, y ninguno de los dos se levantó a buscarla.

**mc_pensamiento:** Antes de este trabajo me habría importado esa hoja.

**mc_pensamiento:** Ahora me importa más no moverme.

---

### Movimiento 3 · Menú cosmético

`menu:`

**"¿En qué piensas mientras el descanso se acaba?"**

- **"En que a este paso me va a tocar traer los libros hasta al baño."**
  - **mc_pensamiento:** Al menos ahí nadie me interrumpe.
  - `[SPR itsuki molesta at pj(0.5)]`
  - **itsuki:** Qué imagen tan poco digna de un tutor.
  - **mc:** No dije que fuera a hacerlo. Dije que a este paso.
  - **itsuki:** Con ese nivel de planificación, no me extraña que solo tengas un
    alumno.

- **"En que ninguno de los dos va a admitir que está cansado."**
  - **mc_pensamiento:** Y si lo hiciéramos, tampoco cambiaría nada.
  - `[SPR itsuki neutral at pj(0.5)]`
  - **itsuki:** Habla por ti.
  - **mc:** Tienes el cuaderno cerrado hace diez minutos.
  - **itsuki:** Estoy descansando la vista. Es distinto.

- **"En nada. Solo quiero que pase la hora."**
  - **mc_pensamiento:** No todo necesita un análisis.
  - `[SPR itsuki neutral at pj(0.5)]`
  - **itsuki:** Al menos en eso estamos de acuerdo.
  - **mc:** Es lo primero.
  - **itsuki:** No te acostumbres.

---

### Movimiento 4 · Cierre

`[MUS stop fadeout 2.0]`

**narrador:** El timbre sonó antes de que ninguno de los dos volviera a abrir
un libro.

**itsuki:** Se acabó el descanso.

**mc:** Se acabó.

**narrador:** Se levantó primero. 

**narrador:** Se sacudió la falda y bajó las escaleras sin
esperarme, como cualquier otro día.

**mc_pensamiento:** Pero hoy subió con el cuaderno.

**mc_pensamiento:** Y hoy no lo abrió ni una vez.

**mc_pensamiento:** Quedan casi tres semanas.

**mc_pensamiento:** Ella las va a pasar igual que hoy: sola, con un cuaderno
que no necesita, en el único sitio que le quedaba para no estarlo del todo.

**mc_pensamiento:** No sé si vine a ayudarla o solo a quitarle eso también.

`→ Vuelve al hub.`

---

### Assets del beat

| Asset | Tipo | Estado | Nota |
|---|---|---|---|
| `bg_azotea` | BG | ya existe | Mismo fondo del prólogo, sin cambios |
| `amb_viento` | ambiente | ya existe | Entra igual que en el prólogo, antes de cualquier música |
| `cg_itsuki_azotea_cuaderno` | CG | pendiente | Movimiento 1. Ella sola, Futaro fuera de cuadro |
| `cg_itsuki_azotea_manos` | CG | pendiente | Movimiento 2. POV de Futaro, manos de ella sobre el cuaderno cerrado |
| `tregua` | BGM | pendiente | Entra muy baja, solo en el gesto del movimiento 2. Nunca antes |
| `sfx_mochila_suelo` | SFX | pendiente | El golpe de la mochila de Futaro al sentarse |

Reutilizados sin tocar: `itsuki neutral`, `itsuki molesta`.

**`cg_itsuki_azotea_cuaderno`** — a diferencia de las CG con Futaro en cuadro,
esta va sin él: es el instante en que la descubre, así que el punto de vista
todavía no está "dentro" de la escena. Un solo personaje con LoRA, sin ningún
riesgo de silueta rota.

**`cg_itsuki_azotea_manos`** — sigue el lenguaje ya validado de
`cg_manija_edificio` y `cg_estudio_biblioteca`: objeto de Futaro desenfocado y
cortado por el borde, nunca su cuerpo. Lo que sostiene la imagen son las manos
de ella sobre el cuaderno cerrado, no su cara — es el mismo principio de
silueta-antes-que-expresión que ya rige los sprites nuevos del capítulo.

**`tregua`** — pensada para sonar solo dos o tres veces en toda la partida,
igual que `hogar`. Si entra en cualquier otro momento, deja de significar
"estos dos están cansados de la misma guerra" y pasa a ser fondo. Volumen bajo
a propósito: entra por debajo del viento, no encima.

**`sfx_mochila_suelo`** — distinto de `sfx_bolsa` (plástico) y de `sfx_papel_mesa`
(papel sobre madera): esto es peso de tela cayendo sobre concreto. Un solo golpe
sordo, sin eco, para no competir con el ambiente de viento que ya está sonando.

---

### Notas de implementación

- Este beat **no otorga puntos**. No lleva ningún `sumar_punto`, en ninguna
  rama del menú cosmético ni en la condicional de `primera_conexion`.
- El chequeo de la micro-variante va así, y **solo lee variables, no las
  escribe**:

  ```renpy
  if primera_conexion == "itsuki" and itsuki_visitada_cap1:
      itsuki "Ya me ayudaste con el ejercicio el otro día. No hace falta que sigas viniendo a comprobar cómo voy."
      mc "No vine a comprobar nada."
      narrador "No pareció creérselo del todo. Pero no insistió."
  else:
      itsuki "No voy a preguntarte a ti dónde has estado estos días."
      mc "No te lo iba a contar de todas formas."
      narrador "Los dos volvieron a mirar al frente, cada uno con su propio libro cerrado sobre las piernas."
  ```

- Se dispara **una sola vez**, justo al cerrar el evento de hermana del Hub 1
  y antes de abrir el Hub 2. No necesita variable de consumo propia porque no
  es revisitable: es un beat de trama, no un evento de mapa.
- El menú cosmético no requiere ninguna variable nueva. Las tres ramas
  reconvergen en la misma línea de cierre.
- `itsuki_timida` sigue reservada exclusivamente al instante de la grieta en su
  evento de hub. No aparece aquí bajo ninguna condición.
