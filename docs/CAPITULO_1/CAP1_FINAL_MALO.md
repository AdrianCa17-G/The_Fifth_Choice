## Final Malo · Despido temprano — Capítulo 1

**Escrito y codificado** en `02_cap1_final_beat.rpy` (A), `02_cap1_final_hub3.rpy` (B) y 
`05_finales.rpy` (dispatcher y cierre). Todos los CG están hechos. Un solo final con dos
variantes: **A** (el portazo, en la cocina del beat de Nino) y 
**B** (la despedida, después del hub 3 y del examen).

Marcadores como en el resto del capítulo. `[BG]` fondo · `[CG]` ilustración · `[SPR]` sprite ·
`[MUS]` música · `[SFX]` efecto · `[NUEVO]` asset que no existe todavía ·
`[$]` línea de código.

---

### Decisiones de este final

**Cuándo se dispara cada variante** (Tabla de 27 combinaciones):

| Variante | Combinaciones | Condición real en el código |
|---|---|---|
| **A · cocina** | 13, 14, 15 | `desaires_cap1 >= 2` al llegar al beat de Nino (los hubs 1 y 2 fueron fríos) |
| **B · tras el hub 3** | 5, 11, 17, 23 | `maruo_ultimatum` y hub 3 fría → `despido_cap1`. Se dispara después del beat casa |

**Dos fracasos distintos, como dice el README.** A es un portazo: Maruo corta, mc no puede
ni hablar, nadie se despide. B es una despedida: hubo un mes, un examen y una última
oportunidad, y cada persona dice lo que le faltaba decir. Por eso B tiene que doler más.

**La culpa no se consigue con gritos, se consigue con calma.** Nadie le reprocha nada a voces
a mc. Maruo no levanta la voz, las hermanas no lo insultan, Isanari no se enfada. El castigo
es que todos tienen razón y lo dicen bajito. Ninguna defiende a mc porque no hay con qué.

**Nino no celebra.** Consigue exactamente lo que pidió y no sabe dónde ponerlo. Su motivo
es proteger a las otras cuatro de ilusionarse con alguien que se va, así que su frase es
«mejor hoy, antes de que se ilusionen más»; y en cuanto aparecen las cuatro se ve que ya
era tarde. En B pasa lo mismo, más grande: es la única que aprueba y se queda sola con eso.

**La disculpa guardada desde el prólogo se gasta aquí, y solo en B.** En A, Itsuki se la
corta («un "lo siento" ahora sería para ti, no para nosotras»). En B mc por fin la dice y
llega un mes tarde. Es una decisión de este final, no del canon: en la ruta principal sigue
guardada.

**El examen ocurre en el aula, con mc dentro.** Es alumno del mismo instituto: hace sus
propios exámenes y los termina pronto. Eso resuelve la focalización (sigue en primera
persona) y es peor que ausentarse: tiene que quedarse sentado, en silencio, viéndolas
hundirse sin poder hablar. Es la versión del «no puedo hacer nada» que pedías.

**Cinco días, un examen por día, todo en el aula.** Lunes japonés, martes matemáticas,
miércoles inglés, jueves ciencias, viernes sociales. Se cuenta lineal y rápido: cada día
se nombra en una línea y la cámara se queda con la hermana de esa materia. Sin
transiciones escuela → casa → cuarto entre un día y otro: el escenario no cambia hasta
que termina la semana.

**Resultado del examen en B.** Aprueba solo Nino. Maruo no dice cuál; mc lo sabe porque la
vio quedarse hasta la campana. Cuatro reprueban, así que la condición del prólogo
(«si una sola reprueba») se cumple literal.

**Las cinco con el bloque «no visitada» en el examen.** Tal como pediste, aunque mc haya
sido cálido en algún hub: no pasó el umbral, así que lo que se ve es el defecto sin tocar.
Los pensamientos de mc en el examen son de observación y no contradicen lo que haya vivido
el jugador. Solo las **despedidas de B** leen `rama_de(h) == "fria"` para añadir una línea
de eco a la hermana con la que fue frío.

**Defectos del examen (adaptados al aula, ya no al departamento):**

| Hermana | Qué pasa |
|---|---|
| Yotsuba | No toca su hoja: mira a sus hermanas sufrir. Solo escribe su nombre (eco del prólogo) |
| Ichika | Finge dormir, con la mente en el papel de la obra. Eco de la apertura |
| Nino | Termina primera y perfecto, pero no entrega: finge revisar hasta la campana para no dejarlas solas |
| Itsuki | Se atasca en el mismo problema y no pregunta. Mira a mc un segundo y vuelve al papel |
| Miku | Escribe la respuesta correcta, la borra, la vuelve a escribir, la borra. La hoja queda gris |

Nino era la que no tenías clara. Esta es mi propuesta porque sale de lo que ya es: no
desconfía de su inglés, desconfía del puesto, y es la que ve venir el golpe. Hacerla
quedarse fingiendo que revisa es «hace bien en silencio y no lo admite», pero convertido
en protección.

**Lo que este final NO gasta.** No usa `itsuki_timida` ni `itsuki_sorpresa` (reservados a
su hub). No hay música ni efectos nuevos. No hay sprites nuevos.

---

### Dónde engancha en el código

```renpy
## 00_definiciones.rpy — ya declarada
default despido_en_beat = False
```

**Variante A.** En `02_cap1_beat_Nino.rpy`, el bloque `if desaires_cap1 >= 2:` se queda con
solo estas tres líneas (se borra todo lo demás de esa rama, está reescrito abajo):

```renpy
    if desaires_cap1 >= 2:
        $ despido_en_beat = True
        $ renpy.pop_call()
        jump final_malo_temprano
```

**Variante B.** Ya engancha: `interconexion_6` hace `call beat_casa` y después
`jump final_malo_temprano` si `despido_cap1`.

**Dispatcher** (en el futuro `05_finales.rpy`):

```renpy
label final_malo_temprano:

    $ ui_escena("normal")
    stop music fadeout 1.0

    if despido_en_beat:
        jump final_malo_beat

    jump final_malo_hub3
```

---

# PARTE A · El portazo (cocina)

*Continúa justo después de «La única vez que la escuché gritarle a su padre».
`[BG bg_cocina]`, mc en la puerta.*

### A · Movimiento 1 · Maruo

`[MUS stop fadeout 1.0]`

**narrador:** Fue entonces cuando Maruo levantó la vista y me encontró en la puerta.

`[CG cg_maruo_reunion]` `[MUS contrato fadein 2.0]`

**maruo:** Qué oportuno.

**mc:** Disculpe, no venía a interrumpir. Yo solo…

**maruo:** Ya que estás aquí, me ahorras la llamada.

**narrador:** Dejó la taza sobre la mesa, despacio.

**maruo:** Mañana no hace falta que vengas.

**mc:** …¿Perdón?

**maruo:** El contrato queda terminado. Tu padre cobrará lo trabajado hasta hoy.

**mc:** Señor, todavía quedan semanas. Si me deja explicarle…

**maruo:** No hay nada que explicar.

**maruo:** Dos tardes, dos de mis hijas, y ninguna está más cerca de aprobar que el primer día.

**maruo:** Las condiciones las sabías desde el principio.

**mc:** Por favor, solo un…

**maruo:** No.

**narrador:** No levantó la voz. Nunca la levanta.

**narrador:** Eso fue lo peor. Ni siquiera sonaba enfadado. Sonaba a trámite.

**narrador:** Nino miraba entre los dos. Abrió la boca para decir algo.

**narrador:** Y no lo dijo.

`[CG NUEVO — cg_maruo_espaldas]` `[SFX sfx_puerta_cierra volume 1.0]` `[MUS stop fadeout 2.0]`

**narrador:** Recogió la taza y salió de la cocina sin esperar respuesta.

**narrador:** Dándonos la espalda a los dos por igual.

**mc_pensamiento:** Lo que ella había pedido a gritos acababa de pasar sin que nadie gritara.

*(Silencio. Un par de líneas sin música, a propósito.)*

---

### A · Movimiento 2 · Lo que pidió

`[BG bg_cocina]` `[SPR nino neutral at pj(0.5)]`

if "nino" in hub_visitadas:

> **nino:** Me dijiste que ibas a durar.
>
> **nino:** …
>
> **nino:** Ya ves.

**narrador:** Nino no se movió. Seguía con las manos apoyadas en la isla.

**narrador:** Hacía un minuto me quería fuera. Ahora me tenía fuera.

**nino:** …

**nino:** Bueno.

**mc:** ¿«Bueno»?

**nino:** Era lo que pedí. ¿Qué esperabas? ¿Que me pusiera a llorar por ti?

**narrador:** Lo dijo con la barbilla en alto, como siempre.

**narrador:** Pero la frase le tardó medio segundo de más en salir.

**nino:** El último duró cuatro días. Tú aguantaste más.

**nino:** No es un cumplido.

**mc_pensamiento:** Tenía que sentirse como ganar. Ella lo sabía. Yo lo sabía.

**mc_pensamiento:** Y tenía la cara de quien consigue justo lo que pidió y no sabe dónde ponerlo.

**nino:** Es mejor así. Hoy. Antes de que se ilusionen más.

**mc:** Nino…

**nino:** Y no me mires con esa cara de pena. No te va a servir de nada.

---

### A · Movimiento 3 · Las cuatro

`[SFX sfx_puerta_abre volume 1.0]`

**narrador:** No pasó ni un minuto. Las cuatro aparecieron por el pasillo casi a la vez.

**narrador:** Con cara de haberse levantado de golpe.

`[SPR ichika neutral at pj(X_ICHIKA)]` `[SPR nino neutral at pj(X_NINO)]` `[SPR miku neutral at pj(X_MIKU)]` `[SPR yotsuba sonriendo at pj(X_YOTSUBA)]` `[SPR itsuki neutral at pj(X_ITSUKI)]` `[with dissolve]`

**yotsuba:** ¡Se oyó hasta la escalera! ¿Quién gritaba? ¿Fue…?

**narrador:** Se detuvo al verme la cara.

**ichika:** Dime que fue una de las discusiones de siempre, Nino.

**nino:** Papá lo despidió.

**narrador:** Nadie dijo nada. Del pasillo llegaba el ruido del edificio, muy lejos.

**itsuki:** …¿Hoy?

**nino:** Hoy. Hace cinco minutos.

*Cada hermana reacciona con `pj_habla` / las demás `pj_calla`. Ninguna defiende a mc. Si la
hermana está en `hub_visitadas`, lleva además su bloque «fría» (fue fría con ella en su hub).*

**Ichika**

`[SPR ichika sonriendo at pj_habla(X_ICHIKA)]`

**ichika:** Bueno… al menos fue rápido. ¿No?

**narrador:** Nadie se rió. Ni ella.

`[SPR ichika neutral at pj_habla(X_ICHIKA)]`

**ichika:** …Perdón. Es lo que hago cuando no sé qué hacer.

**ichika:** No te voy a defender, [mc]. No sabría con qué.

if "ichika" in hub_visitadas:

> **ichika:** Fuiste correcto conmigo. Como un padre.
>
> **ichika:** Y yo te contesté como se contesta a un padre: sonriendo. No sirvió de nada.

**Yotsuba**

`[SPR yotsuba incomoda at pj_habla(X_YOTSUBA)]`

**yotsuba:** Pero si él… él solo estaba…

**nino:** Yotsuba.

**yotsuba:** …No dije nada.

**narrador:** Se quedó mirando el suelo, con las manos juntas delante.

if "yotsuba" in hub_visitadas:

> **yotsuba:** Me dijiste que me concentrara en correr.
>
> **yotsuba:** Dejé de contar en voz alta. Pensé que así servía más.
>
> **yotsuba:** Ahora no sé si servía de algo.

*(Sin signos de exclamación en esta tanda: es la señal de que algo duele.)*

**Miku**

`[SPR miku neutral at pj_habla(X_MIKU)]`

**miku:** …Yo no pedí esto.

**miku:** …Tampoco lo evité.

**narrador:** Se llevó las manos a los audífonos. No se los subió. Los dejó ahí, apoyadas.

if "miku" in hub_visitadas:

> **miku:** …Dijiste que el Sengoku no entraba en el examen.
>
> **miku:** …Tenías razón. Por eso no volví a abrir el libro.

**Itsuki**

`[SPR itsuki neutral at pj_habla(X_ITSUKI)]`

**itsuki:** Te lo dije el primer día. Esto no iba a funcionar.

**itsuki:** Ahora lo tengo confirmado. No me hace ninguna gracia.

if "itsuki" in hub_visitadas:

> **itsuki:** Me quitaste el cuaderno de las manos. Me lo resolviste delante de mí.
>
> **itsuki:** Eso no se me va a olvidar.

**Cierre del movimiento**

`[MUS derrota fadein 2.5]`

**narrador:** Abrí la boca. Itsuki lo notó antes que yo.

**itsuki:** No lo digas. Un «lo siento» ahora sería para ti, no para nosotras.

**narrador:** La cerré. No tenía otra cosa.

**mc_pensamiento:** Tenía razón. Otra vez.

**narrador:** Recogí mi mochila. Nadie me detuvo.

**narrador:** Tampoco nadie me acompañó hasta la puerta.

`[SFX sfx_puerta_cierra volume 1.5]`

**narrador:** La cerré yo mismo. Sin portazo. Para que no pareciera que me enfadaba.

---

### A · Movimiento 4 · Casa

`[BG bg_comedor]` `[MUS stop fadeout 1.5]`

**narrador:** Llegué a casa a una hora a la que no llegaba desde hace semanas.

`[SPR raiha hablando at pj(0.20)]` `[SPR isanari neutral at pj(0.73)]` `[with dissolve]`

**raiha:** ¡Hermanito! Llegaste temprano. ¡Todavía no hay curry!

**narrador:** Se quedó callada al verme la cara.

**mc:** Me despidieron.

`[SPR raiha preocupada at pj(0.20)]`

**raiha:** …¿Qué?

**isanari:** ¿Quién?

**mc:** Maruo. Hoy.

**isanari:** ¿Y el mes? ¿Pagan lo trabajado?

**mc:** Eso dijo.

`[SPR raiha regano at pj(0.20)]`

**raiha:** ¡Papá!

**raiha:** Pregúntale cómo está, no cuánto pagan.

**isanari:** …

**narrador:** Isanari abrió la boca. No contestó.

**narrador:** Se bajó las gafas de la cabeza y las dejó sobre la mesa, sin mirarlas.

**isanari:** Le di mi palabra a Maruo.

**isanari:** Le dije que te tomarías esto en serio.

**mc:** Me lo tomé en serio.

**isanari:** No lo suficiente.

`[SPR raiha preocupada at pj(0.20)]`

**raiha:** Hermanito…

**mc:** Todavía no era el examen, Raiha. Me despidieron antes.

**raiha:** ¿Pero por qué?

**mc:** Porque no hice nada. Dos semanas, y no hice nada.

**narrador:** Raiha no dijo que no fuera verdad.

**narrador:** Eso me dolió más que si lo hubiera dicho.

---

### A · Movimiento 5 · La libreta

`[BG bg_cuarto_mc]` `[CG cg_libreta]`

*(Sin `hogar`. Es el cuarto donde empezó todo y esta vez no suena nada.)*

**narrador:** Abrí la libreta por la página de los cinco nombres.

**narrador:** Debajo de la línea estaba la frase de aquella noche.

**mc_pensamiento:** «Voy a ir de una en una.»

**mc_pensamiento:** Fui de una en una. Y las dos veces me equivoqué.

**mc_pensamiento:** Ni siquiera llegué a la mitad de los treinta días.

**mc_pensamiento:** La deuda sigue exactamente donde estaba.

**narrador:** Cerré la libreta. Apagué la lámpara.

**narrador:** No hubo ninguna frase que anotar esta vez.

`[→ final_malo_cierre]`

---

# PARTE B · La despedida (después del hub 3)

*Continúa después del `call beat_casa` de `interconexion_6` (el beat ya dio la duda de mc en
su cuarto: aquí no se repite).*

### B · Movimiento 1 · Lunes por la mañana

`[BG bg_escuela]` `[SFX sfx_timbre volume 1.5]`

**mc_pensamiento:** Lunes. Primer día de exámenes. Uno por día, toda la semana.

**mc_pensamiento:** Maruo dijo: «Al terminar la semana lo confirmo.»

**mc_pensamiento:** «Confirmar» significa que todavía existe un resultado que podría cambiarlo.

**mc_pensamiento:** Es la única palabra a la que me estoy agarrando.

**mc_pensamiento:** Si aprueban, todo lo demás no importa.

**mc_pensamiento:** Si no aprueban, hoy es mi último día como su tutor. Y lo sé.

**mc_pensamiento:** Cuatro semanas para esto. Y llego igual que cuando empecé.

---

### B · Movimiento 2 · Antes del examen

`[BG bg_aula]` `[MUS stop]`

`[SPR ichika neutral at pj(X_ICHIKA)]` `[SPR nino neutral at pj(X_NINO)]` `[SPR miku neutral at pj(X_MIKU)]` `[SPR yotsuba sonriendo at pj(X_YOTSUBA)]` `[SPR itsuki neutral at pj(X_ITSUKI)]` `[with dissolve]`

**narrador:** Las cinco ya estaban en el aula. Nadie había abierto un libro.

**narrador:** Lo habían abierto tanto estas semanas que ya no servía de nada abrirlo.

`[SPR yotsuba incomoda at pj_habla(X_YOTSUBA)]`

**yotsuba:** Buenos días, [mc]. …Quería decirlo con más ganas. No me sale.

**yotsuba:** Estudié las lecturas dos veces. Cuando cierro el libro, no recuerdo qué sentía nadie.

`[SPR ichika neutral at pj_habla(X_ICHIKA)]`

**ichika:** Dormí cuatro horas. Y las pasé con el papel de la audición, no con las fórmulas.

**ichika:** No me mires así. Ya sé que no era lo que tocaba.

`[SPR miku neutral at pj_habla(X_MIKU)]`

**miku:** …Me sé la mitad de lo que van a preguntar.

**miku:** …Y no me fío de la mitad que me sé.

`[SPR nino neutral at pj_habla(X_NINO)]`

**nino:** Alguien tiene que decirlo y me toca a mí.

**nino:** No aprendimos nada. Ni él nos enseñó, ni nosotras quisimos.

**nino:** No es solo culpa tuya. Eso no cambia que no sirvió.

`[SPR itsuki molesta at pj_habla(X_ITSUKI)]`

**itsuki:** He estudiado más que nadie en esta aula. Cada noche.

**itsuki:** Y no sé si me sé una sola cosa.

**itsuki:** Quisiera poder culparte. Sería más fácil.

**narrador:** Me miraron las cinco. Esperando algo.

**mc_pensamiento:** No tenía nada que decirles que no fuera mentira.

**mc:** Hagan lo que sepan.

**narrador:** Lo dije y sonó a lo que era: una frase de relleno.

`[SFX sfx_timbre volume 1.5]`

---

### B · Movimiento 3 · Los cinco exámenes

*Una semana, un examen por día, todo en el aula y sin cambiar de escenario. Cada día se
nombra en una línea y la cámara se queda con la hermana de esa materia. mc está sentado en su
pupitre de la segunda fila, termina los suyos antes de la mitad, y se queda mirando.*

`[BG bg_aula]` `[MUS stop]` *(sin música todo el movimiento: solo campana, hojas y silencio)*

**narrador:** Mi pupitre estaba en la segunda fila. Ellas, repartidas delante y a los lados.

**narrador:** Cada día, un examen. Cada día terminaba el mío antes de la mitad.

**mc_pensamiento:** Ahora venía lo peor: no tener nada que hacer más que mirar.

**profe:** Pueden empezar.

`[SFX sfx_hoja volume 2.0]`

#### 3.1 · Lunes · Japonés · Yotsuba

`[CG NUEVO — cg_yotsuba_fracaso]`

**narrador:** Lunes. Japonés. Las cinco lo hacían a la vez; yo solo podía mirar a una.

**narrador:** Yotsuba no escribía. Tenía el lápiz quieto y la cabeza girada.

**mc_pensamiento:** No miraba su hoja. Miraba a Ichika. Después a Miku. Después a Itsuki.

**mc_pensamiento:** Otra vez a Ichika.

**narrador:** Cada vez que una de ellas se frotaba la cara, ella se encogía un poco.

**mc_pensamiento:** Es lo que mejor hace: leer a las demás.

**mc_pensamiento:** Nadie le había dicho que eso también contaba. Yo tampoco.

**narrador:** La pregunta uno preguntaba qué siente el protagonista cuando se queda solo.

**narrador:** La hoja de Yotsuba tenía su nombre. Nada más.

**mc_pensamiento:** El mismo uno por ciento del primer día. Esta vez nadie se rió.

`[SFX sfx_timbre volume 1.5]`

#### 3.2 · Martes · Matemáticas · Ichika

`[CG NUEVO — cg_ichika_fracaso]`

**narrador:** Martes. Matemáticas.

**narrador:** Ichika escribió su nombre y las dos primeras líneas.

**narrador:** Después sacó algo doblado de debajo de la hoja. Un guion.

**mc_pensamiento:** Movía los labios sin sonido. Repetía una frase una y otra vez.

**mc_pensamiento:** No era una fórmula. Era un papel que no es de este examen.

**narrador:** Al rato apoyó la cabeza en el brazo y cerró los ojos.

**mc_pensamiento:** Igual que el segundo día. La misma función.

**mc_pensamiento:** Solo que esta vez la función no era para nadie.

**profe:** Nakano. Despierte.

`[SPR ichika sonriendo at pj_habla(0.5)]`

**ichika:** ¡Estaba pensando! Los matemáticos piensan con los ojos cerrados.

**narrador:** Nadie se rió. El profesor tampoco.

**profe:** Pensando se piensa con los ojos abiertos.

`[SFX sfx_timbre volume 1.5]`

#### 3.3 · Miércoles · Inglés · Nino

`[CG NUEVO — cg_nino_fracaso]`

**narrador:** Miércoles. Inglés.

**narrador:** Nino terminó la primera.

**narrador:** Letra apretada, sin tachones, sin levantar la vista. Como si el examen le debiera algo.

**narrador:** Soltó el lápiz. Giró la hoja boca abajo. Cruzó los brazos.

**profe:** Nakano. Puede entregar.

**nino:** No. Voy a revisar.

**mc_pensamiento:** No había nada que revisar.

**mc_pensamiento:** Miraba de lado. A Yotsuba, a Itsuki, a Miku. Con la mandíbula tensa.

**mc_pensamiento:** Se quedó cuarenta minutos fingiendo que revisaba. Para no dejarlas solas.

**narrador:** Me miró una sola vez. No fue odio. Fue como quien comprueba una cuenta.

**mc_pensamiento:** Ella lo había visto venir antes que nadie. Y era la única que no podía hacer nada.

`[SFX sfx_timbre volume 1.5]`

#### 3.4 · Jueves · Ciencias · Itsuki

`[CG NUEVO — cg_itsuki_fracaso]`

**narrador:** Jueves. Ciencias.

**narrador:** Itsuki llevaba tres líneas bien. La cuarta se la comía.

**narrador:** Pasó a la siguiente pregunta. Volvió a la cuarta. Otra vez.

**mc_pensamiento:** Una raya horizontal, prolija. No un garabato de rabia.

**mc_pensamiento:** El mismo problema del primer día. El mismo error, en el mismo sitio.

**narrador:** Levantó la vista. Me miró un segundo.

**mc_pensamiento:** Habría dado lo que fuera por decirle dónde mirar.

**mc_pensamiento:** No se puede hablar en un examen. Y aunque se pudiera, me lo había prohibido.

**mc_pensamiento:** «Ni se te ocurra decirme la respuesta.»

**narrador:** Apartó la mirada. Volvió al papel.

**narrador:** No preguntó. Preguntar habría sido darme la razón.

`[SFX sfx_timbre volume 1.5]`

#### 3.5 · Viernes · Sociales · Miku

`[CG NUEVO — cg_miku_fracaso]`

**narrador:** Viernes. Sociales. El último.

**narrador:** Miku escribió una respuesta larga. Se detuvo.

**narrador:** La borró. La volvió a escribir. La borró.

**mc_pensamiento:** Escribió la correcta primero. Y después la borró.

**mc_pensamiento:** Igual que en la hoja del segundo día. Igual que siempre.

**narrador:** La goma ya no era goma. Era un trozo de nada.

**narrador:** Al final escribió una sola línea. La respuesta que cabe en una línea.

**mc_pensamiento:** No le falta saber. Le falta creérselo.

**mc_pensamiento:** Lo vi en su hoja hace semanas. Y no hice nada.

**narrador:** Su mano subió hasta el cuello, hasta los audífonos. Se quedó ahí.

**narrador:** No se los puso. Un examen no se puede hacer con música. Pero tampoco los soltó.

`[SFX sfx_timbre volume 1.5]`

---

### B · Movimiento 4 · Después del examen

`[BG bg_aula_tarde]` `[MUS derrota fadein 2.5]`

*(Entra `derrota` por primera vez en toda la semana: antes hubo silencio, así que se oye.)*

`[SPR ichika neutral at pj(X_ICHIKA)]` `[SPR nino neutral at pj(X_NINO)]` `[SPR miku neutral at pj(X_MIKU)]` `[SPR yotsuba neutral at pj(X_YOTSUBA)]` `[SPR itsuki neutral at pj(X_ITSUKI)]` `[with dissolve]`

**narrador:** Sonó la última campana de la semana. El aula se fue vaciando.

**narrador:** Ellas se quedaron.

**narrador:** Nadie recogía nada. Ninguna dijo «salió bien».

`[SPR yotsuba neutral at pj_habla(X_YOTSUBA)]`

**yotsuba:** Mi hoja está en blanco. Solo escribí mi nombre.

**yotsuba:** Estuve mirando a las demás todo el tiempo. No pude parar.

**yotsuba:** Con toda esta energía que me sobra, y no pude hacer nada por ninguna.

**mc:** Yotsuba, no es tu…

**yotsuba:** No me digas que no es mi culpa.

`[SPR ichika agotada at pj_habla(X_ICHIKA)]`

**ichika:** Me dormí delante de todos.

**ichika:** Me dieron el papel de la obra. Y ni siquiera me alegré.

**ichika:** No me preguntes por qué. Si me preguntas voy a inventarme algo.

**ichika:** Y hoy no tengo ganas de inventar nada.

`[SPR miku encogida at pj_habla(X_MIKU)]`

**miku:** …Sabía las respuestas. …Las escribí. …Las borré.

**miku:** …Perdón.

**mc:** No pidas perdón.

**miku:** …Es lo único que sé decir.

`[SPR itsuki molesta at pj_habla(X_ITSUKI)]`

**itsuki:** Estudié todas las noches. Y en cuanto vi la hoja, se me fue todo.

**itsuki:** Te pedí que no me ayudaras. Y no lo hiciste.

**itsuki:** No sé qué es peor.

`[SPR nino neutral at pj_habla(X_NINO)]`

**nino:** Va a pasar lo que dije que pasaría.

**nino:** Te lo dije el primer día. Y no me siento mejor por tener razón.

**mc:** Te vi quedarte hasta la campana.

**nino:** No sé de qué hablas.

**mc_pensamiento:** Un mes. Y mi única contribución había sido sentarme a mirar.

**mc_pensamiento:** Cinco personas que saben una cosa cada una. Y ninguna la había enseñado.

**mc_pensamiento:** Yo tampoco había preguntado.

---

### B · Movimiento 5 · Noche en casa (todavía no lo saben)

`[BG bg_cuarto_mc]` `[MUS stop fadeout 1.5]`

**narrador:** Esa noche volví a mi cuarto. No abrí la libreta.

**mc_pensamiento:** Repasé el mes. Cada vez que pude decir que sí, dije que no.

**mc_pensamiento:** Cada vez que alguien necesitaba que me quedara callado, hablé.

**mc_pensamiento:** Y cada vez que necesitaba hablar, me quedé callado.

`[SFX sfx_toque_puerta volume 1.5]` `[SPR raiha hablando at pj(0.30)]`

**raiha:** Hermanito, ¿cómo salió?

**mc:** No lo sé todavía. Mañana llegan las notas.

**raiha:** Si se esforzaron, saldrá bien.

**mc:** Se esforzaron. Algunas.

**raiha:** Entonces hiciste lo que pudiste.

**narrador:** Lo dijo con tanta convicción que me dieron ganas de creerle.

**mc:** …Sí.

**mc_pensamiento:** No. No lo hice.

`[SPR isanari neutral at pj(0.73)]`

**isanari:** Mañana Maruo cierra el mes. Cobramos entero.

**isanari:** Cinco veces la tarifa. Es lo mejor que nos ha pasado en años.

**narrador:** Raiha me miró. Yo no le devolví la mirada.

**mc_pensamiento:** Ellos todavía no sabían que el despido estaba firmado desde el viernes.

**mc_pensamiento:** Y yo todavía no tenía valor para decírselo.

---

### B · Movimiento 6 · Maruo

`[BG bg_negro]`

**narrador:** Al día siguiente del último examen, a media mañana, me vibró el teléfono.

**narrador:** «Departamento. Cinco de la tarde. Maruo.»

**narrador:** Nada más. No hacía falta.

`[BG bg_edificio]` `[BG bg_departamento]` `[CG cg_maruo_reunion]` `[MUS contrato fadein 2.0]`

**maruo:** Siéntate.

**mc:** Prefiero estar de pie.

**maruo:** Como quieras.

**narrador:** Dejó cinco boletines sobre la mesa. Boca arriba, en fila.

**maruo:** Las notas llegaron esta mañana.

**maruo:** Una aprobó. Cuatro no.

**mc:** ¿Quién…?

**maruo:** No necesito decirte cuál.

**mc_pensamiento:** Lo sabía. La que se quedó hasta la campana.

**maruo:** Te advertí en esa cocina que no repetiría la advertencia. Y no la repetí.

**maruo:** No esperaba esto de ti, [mc].

**maruo:** Tu padre me habló de alguien que no se rendía.

**mc:** No me rendí.

**maruo:** No te rendiste. Tampoco hiciste nada.

**narrador:** Lo dijo sin dureza. Y por eso se me clavó.

**maruo:** No te pedí que fueras amable con mis hijas. Te pedí que estudiaran.

**maruo:** No lo conseguiste con ninguna.

**mc:** Si me diera un mes más…

**maruo:** Ya tuviste uno.

**maruo:** Y tuviste una última oportunidad. Yo no me alegro de esto.

**maruo:** Tu padre recibirá el pago de lo trabajado. Hasta aquí.

`[CG cg_maruo_espaldas]` `[SFX sfx_puerta_cierra volume 1.0]` `[MUS stop fadeout 2.0]`

**narrador:** Recogió sus cosas y salió. Sin portazo. Dándome la espalda.

**mc_pensamiento:** Esta vez no pude decir «eso no es justo». Porque lo era.

---

### B · Movimiento 7 · Las despedidas

`[BG bg_departamento]`

**narrador:** No me dio tiempo a irme.

**narrador:** Se abrieron las puertas del pasillo. Una por una.

*Cada una se despide a su manera. Los bloques «fría» se leen con `rama_de("hermana") == "fria"`.*

**Yotsuba**

`[SPR yotsuba incomoda at pj_habla(0.5)]`

**yotsuba:** Gracias por venir todos los días.

**yotsuba:** No sé cómo se despide uno de alguien que se va por mi culpa.

**mc:** No es por tu culpa.

**yotsuba:** Lo sé. Pero así se siente.

if rama_de("yotsuba") == "fria":

> **yotsuba:** Gracias por todo, tutor.
>
> **narrador:** Me llamó «tutor». Con el tono que se usa con un desconocido.

**Ichika**

`[SPR ichika neutral at pj_habla(0.5)]`

**ichika:** Aquí no hace falta que sonría, ¿verdad?

**ichika:** Fue un placer, [mc]. Y lo digo sin guion.

if rama_de("ichika") == "fria":

> **ichika:** Nunca me contestaste el chiste. Entendí por qué. Tenías razón en no hacerlo.

**Miku**

`[SPR miku neutral at pj_habla(0.5)]`

**miku:** …Adiós, [mc].

**miku:** …Yo te lo habría contado. …Todo lo que sé.

**miku:** …Si hubieras preguntado.

**narrador:** Se subió los audífonos. Y esta vez sí sonó la música.

if rama_de("miku") == "fria":

> **miku:** …Hoy no, dijiste tú. …Hoy no, dije yo. …Ya no hay otro día.

**Nino**

`[SPR nino neutral at pj_habla(0.5)]`

**nino:** Mi padre te va a pagar lo del mes. Acéptalo.

**mc:** Gracias, Nino.

**nino:** No me des las gracias.

`[SPR nino nerviosa at pj_habla(0.5)]`

**nino:** Yo ni siquiera sé si…

**narrador:** Se cortó a mitad de frase. Esta vez no era una táctica.

**nino:** Cuídate.

if rama_de("nino") == "fria":

> **nino:** Anota la fecha, te dije. Aquí la tienes.

**Itsuki**

`[SPR itsuki neutral at pj_habla(0.5)]`

**itsuki:** Te vas sin que nadie te lo pida. Eso es raro en ti.

**mc:** Itsuki.

**mc:** Debí disculparme el primer día. Por lo del asiento. Por todo.

**itsuki:** Sí. Debiste.

**itsuki:** …

**itsuki:** Yo tampoco dije que lo sentía. Eso lo hace parejo, supongo.

**itsuki:** Ya no sirve de nada. Pero aceptada.

**narrador:** Fue la única disculpa que dije en todo el mes. Y llegó tarde.

if rama_de("itsuki") == "fria":

> **itsuki:** Me quitaste el cuaderno de las manos. Aun así, lo agradezco. No sé por qué.

`[MUS derrota fadein 2.5]`

**narrador:** Salí del departamento. Esta vez nadie me acompañó. Nadie me pidió que me quedara.

**mc_pensamiento:** Ni siquiera hubo un portazo. Eso era lo más cruel.

---

### B · Movimiento 8 · La cena

`[BG bg_comedor]` `[MUS stop fadeout 1.5]`

**narrador:** En casa olía a curry.

`[SPR raiha hablando at pj(0.20)]`

**raiha:** ¡Hermanito! Hice curry. Pensé que si las notas salían bien, celebrábamos.

**narrador:** Entonces vio mi cara. Y se le apagó la sonrisa entera.

`[SPR isanari neutral at pj(0.73)]`

**isanari:** Maruo me llamó. Hace una hora.

**raiha:** ¿Llamó por qué?

**isanari:** Díselo tú.

**mc:** Me despidieron, Raiha.

`[SPR raiha preocupada at pj(0.20)]`

**raiha:** …¿Qué?

**mc:** Cuatro reprobaron. Y yo… no pude hacer nada.

**mc:** Tuve un mes. Y tuve una última oportunidad. Y no la aproveché.

**raiha:** Pero dijiste que no eran tontas.

**mc:** Y no lo son.

**raiha:** Entonces no entiendo el problema.

**narrador:** Lo dijo igual que la otra noche. Solo que esta vez la voz le temblaba.

**isanari:** Esa familia pagaba cinco veces la tarifa. Cubría lo que ni tú ni yo cubrimos.

**isanari:** No te lo digo para hundirte. Contaba con eso. Es todo.

**raiha:** Papá, déjalo.

**isanari:** …

**narrador:** Isanari se sentó. No dijo nada más.

**raiha:** …No pasa nada, hermanito.

**raiha:** Vamos a comer. El curry se enfría.

**narrador:** Nos sentamos. Ninguno tenía hambre.

**mc:** Gracias por la comida.

**narrador:** Lo dije por costumbre. Era la primera vez que no sentía nada al decirlo.

---

### B · Movimiento 9 · La libreta

`[BG bg_cuarto_mc]` `[CG cg_libreta]`

**narrador:** Abrí la libreta. La página de los cinco nombres.

**mc_pensamiento:** «De frente y las cinco a la vez, pierdo siempre.»

**mc_pensamiento:** Fui de una en una. Y perdí igual.

**mc_pensamiento:** Dos semanas con las tres tardes que me dieron.

**mc_pensamiento:** Treinta días.

**mc_pensamiento:** Los usé todos. Y no se los entregué a ninguna.

**narrador:** Cerré la libreta. Apagué la lámpara.

`[→ final_malo_cierre]`

---

# Cierre común

Vive en `05_finales.rpy`. Marca qué versión se vio (A si `despido_en_beat`, B si no) y el flag general, que es el que enciende la caja «Despido temprano» en Finales.

```renpy
label final_malo_cierre:

    scene bg_negro
    with fade

    if despido_en_beat:
        $ persistent.final_malo_temprano_a_visto = True
    else:
        $ persistent.final_malo_temprano_b_visto = True

    $ persistent.final_malo_temprano_visto = True

    ## Tarjeta de final: texto centrado sobre negro, sin música.
    narrador "FINAL MALO · Despido temprano"

    return
```

El `return` con la pila vacía cierra la partida y vuelve al menú principal; dentro de un replay, cierra el replay. Si más adelante `05_finales.rpy` tiene una pantalla de final, sustituir `narrador` por ella.

---

### Assets del final

| Asset | Tipo | Estado | Nota |
|---|---|---|---|
| `cg_maruo_espaldas` | CG | hecho | **Uno solo, compartido por A y B.** Declarado en `02_cap1_final_beat.rpy` |
| `cg_yotsuba_fracaso` | CG | hecho | Movimiento B3.1. Declarado en `02_cap1_final_hub3.rpy` |
| `cg_ichika_fracaso` | CG | hecho | Movimiento B3.2 |
| `cg_nino_fracaso` | CG | hecho | Movimiento B3.3 |
| `cg_itsuki_fracaso` | CG | hecho | Movimiento B3.4 |
| `cg_miku_fracaso` | CG | hecho | Movimiento B3.5 |

Reutilizados sin tocar: `cg_maruo_reunion`, `cg_libreta`, `bg_cocina`, `bg_aula`,
`bg_aula_tarde`, `bg_escuela`, `bg_edificio`, `bg_departamento`, `bg_comedor`,
`bg_cuarto_mc`, todos los sprites de las cinco, Raiha e Isanari. Audio: `contrato`,
`derrota`, `sfx_timbre`, `sfx_hoja`, `sfx_puerta_abre`, `sfx_puerta_cierra`,
`sfx_toque_puerta`. **No hay música, efectos ni sprites nuevos.**

**Cuántos CG de Maruo: uno nuevo, no dos.** El Maruo hablando ya existe
(`cg_maruo_reunion`) y sirve en las dos variantes. Lo único que falta es verlo
irse, y ese gesto es idéntico en A y B: la diferencia entre «portazo» y «decepción» la
llevan el diálogo y el tono, no el encuadre. Maruo no tiene sprite, así que si le doy dos
CG nuevos solo uno de los dos se vería por partida. **Total nuevo: 6 CG** (5 de examen
más `cg_maruo_espaldas`).

**Los cinco CG de examen — receta común.** POV desde el pupitre de mc, con el lenguaje ya
validado (`cg_manija_edificio`, `cg_itsuki_reto`): primer término inferior, su examen
**terminado y boca abajo**, un lápiz y el canto de una mano, desenfocado y cortado por el
borde. Es el **mismo primer plano en las cinco**; solo cambia la hermana al fondo, así
las cinco se leen como un set. Un solo personaje con LoRA por frame (serie 0.3 +
personaje 0.7–0.8). **Generarlos en la misma sesión y guardar la semilla**, igual que los
pares de Miku e Itsuki. Cinco siluetas distintas, para que se lean al 30 %:

- **`cg_yotsuba_fracaso`** — cabeza girada hacia las otras, lápiz quieto sobre la hoja casi
  en blanco, sin sonrisa (cejas hacia arriba por dentro, boca pequeña cerrada).
- **`cg_ichika_fracaso`** — tumbada sobre el brazo, un guion doblado asomando bajo la hoja,
  y **un ojo entreabierto vigilando**: finge dormir.
- **`cg_nino_fracaso`** — brazos cruzados, hoja terminada boca abajo, lápiz soltado,
  mirada de lado y mandíbula tensa. Es la silueta más cerrada de las cinco.
- **`cg_itsuki_fracaso`** — inclinada sobre una hoja con tachones prolijos, el lápiz
  apoyado, y la mirada de reojo hacia la cámara un segundo.
- **`cg_miku_fracaso`** — encogida, la goma reducida a un tocón, migas sobre un círculo
  gris en la hoja, audífonos al cuello con la mano cerca sin tocarlos.

**`cg_maruo_espaldas`** — Maruo de espaldas en el marco de la puerta de la cocina, la taza
en la mano. LoRA de serie 0.1, ficha de prompt de Maruo ya validada. Sin rostro visible
el LoRA no lo puede feminizar.

---

### Notas de implementación

- **Galería.** Los 5 CG de examen van en la pestaña de su hermana (`cg_<hermana>_fracaso`)
y `cg_maruo_espaldas` en «Capítulo 1». Consecuencia: el 100 % de cada hermana, que
desbloquea su extra, exige haber visto el final malo B. Está asumido así.

- **`FINALES_ESPECIALES`**: la pista de «temprano» dice «Tres puertas cerradas en el primer
  mes», que era la regla vieja. Propuesta: «Decir que no cada vez que pudiste decir que sí.»
- **`ui_escena("normal")`** se llama al inicio de `final_malo_temprano`. En A el beat dejó
  el HUD en modo `beat`, y `renpy.pop_call()` sale sin pasar por el `ui_escena("normal")`
  de `interconexion_4`.
- **Todo `show` lleva su posición**, incluidos los `pj_habla` / `pj_calla` de cada
  hermana, y tras cada CG hay que volver a su `scene bg_*` antes de mostrar sprites.
- `nino nerviosa` y `ichika agotada` solo aparecen en el instante de quiebre de B
  (B4 y B7). `itsuki timida` y `itsuki sorprendida` no aparecen.
- Ninguna línea supera las dos líneas de caja de texto.
- **Revivir desde Finales.** La caja «Despido temprano» abre un popup (`final_versiones`)
  con las dos versiones, definidas en `FINALES_TEMPRANO` (`08_extras.rpy`). Cada versión
  lleva su `label` (`final_malo_beat` / `final_malo_hub3`) y un `scope`, porque un replay
  arranca con todas las variables en su `default`. El `scope` de A fuerza
  `despido_en_beat = True`: el cierre lo lee para saber qué flag marcar. Los de B
  dejan `maruo_ultimatum` y `despido_cap1` en `True` y simulan tres hubs visitados (dos fríos).
- **Flags.** `persistent.final_malo_temprano_a_visto` y `_b_visto` bloquean o desbloquean
  cada versión en el popup. `final_malo_temprano_visto` se mantiene para encender la caja.
- **Nombre del jugador en replays.** Todo `Replay` pasa por `final_scope()`, que añade
  `persistent.nombre_jugador`. Ese valor se guarda en `configurar_nombre`.
- **Pendiente:** borrar el «puente de una sola vez» del `init python` de `08_extras.rpy`,
  que desbloquea A y B a quien ya tenía el flag antiguo.

---

### Cosas del repo (revisadas)

Resueltas en el código: `despido_en_beat` ya está declarada, el hablante de «¡Es un tutor, 
no una sentencia de por vida!» ya es `nino`, y las fechas del examen cuadran
(`beat_casa` dice «el examen es mañana», que vale para el lunes;
Maruo ya no usa «El lunes lo confirmo»).

**Pendiente:** `README.md` y `CAP1.md` siguen diciendo «tres desaires» y 
«Evento 6 en la mesa del departamento». La regla real es: dos desaires antes del beat
(versión A), o uno más un segundo en el hub 3 (versión B). 
Y el evento 6 sucede en el aula durante el examen.
