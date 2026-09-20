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

`[BG bg_azotea]` `[SFX sfx_mochila_suelo NUEVO volume 1.5]`

**narrador:** Subí a la azotea a la hora del almuerzo, más por costumbre que por
otra cosa.

**mc_pensamiento:** Desde el primer día, es el único sitio del instituto donde
nadie me pide nada.

**narrador:** La puerta ya estaba abierta.

`[CG NUEVO — cg_itsuki_azotea_cuaderno: Itsuki sentada contra la valla, de
perfil, con un cuaderno abierto sobre las rodillas que no está mirando. Luz de
mediodía, cielo despejado. Encuadre limpio, sin Futaro en cuadro — es él quien
la descubre desde la puerta. Sostiene todo el movimiento 1.]`

**mc_pensamiento:** Ahí estaba. Itsuki. Con el cuaderno.

**mc_pensamiento:** El mismo cuaderno de ciencias que tenía ayer en el aula.

**narrador:** No lo estaba leyendo.

**narrador:** Lo tenía abierto en una página y la vista en otro lado.

**mc_pensamiento:** Desde que la conocí por primera vez,

**mc_pensamiento:** ya habiamos estado en este lugar antes.

**mc_pensamiento:** Es la única de las cinco de la que puedo decir eso con
seguridad, porque me lo dijo ella misma, discutiendo.

**mc_pensamiento:** Y hoy trajo el cuaderno de todas formas.

**narrador:** Me senté a un par de metros, sin decir nada todavía.

`[SPR itsuki neutral at pj(0.5)]`

**itsuki:** No te until.

**mc:** No hice ruido a propósito.

**itsuki:** Da igual. Ya estás aquí.

**narrador:** Lo dijo sin la hostilidad de siempre. Sonó más a un hecho que a
una queja.

---

### Movimiento 2 · El peso compartido

**mc:** Pensé que este sitio era donde no estudiabas.

`[SPR itsuki molesta at pj(0.5)]`

**itsuki:** Y lo era.

**narrador:** Cerró el cuaderno, pero no lo guardó. Se quedó con la mano
encima, como si todavía no hubiera decidido qué hacer con él.

**itsuki:** Ya no me queda ningún sitio que no lo sea.

**narrador:** Fue una frase corta. Más corta que las suyas de costumbre.

**mc_pensamiento:** No se cortó a media idea. La terminó.

**mc_pensamiento:** Simplemente no tenía más que decir, y eso es distinto.

**narrador:** Extendí la mano hacia la mochila y saqué mi propio libro.

**itsuki:** ¿Tú también?

**mc:** Yo desde antes de que existiera este trabajo.

**narrador:** No dijo nada a eso. Pero tampoco volvió a abrir su cuaderno.

`[CG NUEVO — cg_itsuki_azotea_manos: punto de vista de Futaro, sentado. En
primer término inferior, desenfocada y cortada por el borde, la correa de su
propia mochila en el suelo junto a él. Itsuki al fondo, de perfil contra la
valla, con las manos apoyadas sobre el cuaderno cerrado, sin abrirlo. Misma luz
que `cg_itsuki_azotea_cuaderno`, encuadre mucho más cerrado. Sostiene el resto
del movimiento 2.]`

**narrador:** Tenía las manos apoyadas sobre la tapa, quietas. No los dedos
manchados de tinta que suele traer del aula: hoy los tenía limpios.

**mc_pensamiento:** No había escrito nada en toda la mañana.

**mc_pensamiento:** Ella, que llena una hoja de tachones antes que nadie
termine la primera línea.

`[MUS NUEVO — tregua fadein 3.0 volume 0.3]`

**narrador:** El viento seguía sonando igual que siempre aquí arriba, pero por
debajo empezó a sonar algo más. Bajo, casi nada.

**itsuki:** ¿Vas a preguntarme por qué lo traje?

**mc:** No.

**itsuki:** …¿Por qué no?

**mc:** Porque ya lo sé.

**narrador:** No contestó. Pero no volvió a preguntar tampoco.

if (persistent.primera_conexion == "itsuki" and persistent.itsuki_visitada_cap1):

> **itsuki:** …Sigues viniendo aquí después de lo de la biblioteca —o lo que
> sea que hicieras ayer. No cambió nada.
>
> **mc:** No dije que hubiera cambiado.
>
> **narrador:** Fue lo más cerca que estuvo de reconocer que sabía dónde había
> estado el día anterior.

else:

> **itsuki:** No voy a preguntarte a ti a dónde fuiste ayer.
>
> **mc:** No te lo iba a contar de todas formas.
>
> **narrador:** Los dos volvieron a mirar al frente, cada uno con su propio
> libro cerrado sobre las piernas.

**mc_pensamiento:** Llevamos un día y medio de esto y ya la convivencia se
volvió jornada completa para las dos partes.

**mc_pensamiento:** Ella tampoco tiene dónde bajar la guardia. Yo tampoco.

**narrador:** Nos quedamos ahí un rato largo, sin abrir ninguno de los dos
libros.

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

**narrador:** Se levantó primero. Se sacudió la falda y bajó las escaleras sin
esperarme, como cualquier otro día.

**mc_pensamiento:** Pero hoy subió con el cuaderno.

**mc_pensamiento:** Y hoy no lo abrió ni una vez.

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
      itsuki "…Sigues viniendo aquí después de lo de la biblioteca —o lo que sea que hicieras ayer. No cambió nada."
      mc "No dije que hubiera cambiado."
      narrador "Fue lo más cerca que estuvo de reconocer que sabía dónde había estado el día anterior."
  else:
      itsuki "No voy a preguntarte a ti a dónde fuiste ayer."
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
