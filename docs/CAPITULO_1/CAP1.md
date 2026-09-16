# Capítulo 1 — estado

**En escritura.** Estructura cerrada, apertura terminada y el evento de Miku
escrito (§8). Quedan cuatro eventos de hub, los tres beats fijos y el evento
final.

Lo transversal —cómo se genera el arte, cómo se monta el audio, las trampas del
motor— está en las guías de `docs/`. Aquí solo vive lo propio de esta fase.

---

## 1. Decisiones de diseño cerradas

Las tres que bloqueaban el capítulo quedaron resueltas. No volver atrás sobre
ellas sin revisar lo que cuelga de cada una.

**Modelo de interacción: hubs, no calendario.** El capítulo avanza por beats
fijos; entre beat y beat se abre el mapa y el jugador elige destino. El tiempo lo
narra el texto. Se descartó simular 60 días por capítulo: dejaba 162 días vacíos
y pedía unos 70 fondos contando franjas horarias.

**Primera decisión puntuada: la elección de destino del hub 1.** El jugador no
elige una respuesta de diálogo, elige a quién va a buscar. Eso escribe
`primera_conexion` y con ella el desempate de toda la partida. Es más limpio que
un menú porque el desempate queda fijado por a quién buscó, no por lo que
contestó.

**Maruo: dos finales malos.** La afinidad representa «logró llegar a ellas y por
eso estudian». El despido temprano del Capítulo 1 se dispara por desaires, no por
puntos. Detalle completo en el README.

**Reparto canónico de materias.** Ichika matemáticas, Nino inglés, Miku sociales,
Yotsuba literatura, Itsuki ciencias. Cierra sobre las cinco asignaturas del examen
sin sobras ni huecos, y de ahí sale la tesis del capítulo.

---

## 2. Esqueleto

```
APERTURA (fija) → HUB 1 → evento → BEAT Itsuki → HUB 2 → evento
→ BEAT crisis de Nino → HUB 3 → evento → BEAT casa → EVENTO 6 (fijo)
```

Se escriben **cinco** eventos de hermana y el jugador consume **tres** por
partida. Dos se quedan fuera cada vez: eso es lo que hace que elegir pese.

Los tres beats fijos —Itsuki en el instituto, la crisis de Nino, la noche en casa
con Raiha— no dan puntos. Su función es que las cinco tengan presencia aunque
nadie las busque.

Entre beats y eventos, Itsuki y Nino aparecen más que las otras tres en este
capítulo. Es deliberado: son las que empujan el conflicto. En el Capítulo 2
conviene invertirlo y darles los beats fijos a Miku y Yotsuba.

### Restricción que condiciona los cinco eventos

**Cada evento tiene que funcionar en cualquiera de los tres huecos.** El jugador
puede visitar a Miku en el hub 1 o en el hub 3, antes o después de la crisis de
Nino. Ninguno puede depender de que otro haya ocurrido ni de que un beat fijo haya
pasado. Si un evento necesita saber qué pasó antes, o se reescribe o se convierte
en beat fijo.

Caso concreto: el evento de Nino tiene que leerse como «todavía no confía» tanto
antes como después de su crisis.

---

## 3. Los cinco eventos de hermana

Anatomía común: llegada, la hermana haciendo algo que la define, la grieta, la
decisión, cierre corto. Ocho a doce minutos de lectura.

### Yotsuba · Pista de atletismo

Entrenando sola con el club ya vacío. **Grieta:** cree que si deja de ser útil
deja de tener lugar; dice con naturalidad que sus hermanas son mejores en todo y
que lo suyo es correr y animar. **Cálida:** Futaro le señala que ella nota cosas
de sus hermanas que él no ve, y que eso tiene nombre y se califica. **Fría:**
darle la razón y decirle que se concentre en correr. Suena amable y es lo peor
que le puede decir nadie.

### Ichika · Sala de ensayo

Repasando un guion, sola, con tres horas de sueño. **Grieta:** no es floja, está
agotada y usa la simpatía como blindaje; se le cae la máscara medio segundo y la
vuelve a poner con un chiste. **Cálida:** que Futaro no le siga el chiste, se
quede callado y espere. **Fría:** decirle que si tiene tiempo para audiciones
tiene tiempo para estudiar. Es el reproche que espera de todo el mundo.

### Nino · Centro comercial

Comprando ingredientes de una receta extranjera que lee en el idioma original, y
traduciendo sin darse cuenta. **Grieta:** no desconfía de Futaro, desconfía del
puesto; ya vio a varios entrar prometiendo y salir cobrando. Su hostilidad es
protección de las otras cuatro. **Cálida:** concederle que tiene razón y que solo
el tiempo lo demostrará. **Fría:** prometerle que él sí va a durar. Ya escuchó esa
frase y viene con fecha de caducidad.

### Miku · Biblioteca

Con el libro de Sengoku, auriculares puestos sin música. **Grieta:** se entusiasma
explicando algo, se corta sola a mitad de frase y pide perdón por hablar. Ese
«perdón» es el corazón del personaje. **Cálida:** que Futaro le haga una pregunta
concreta que la obligue a seguir — no elogiarla, preguntarle. **Fría:** cortarla
él primero y decirle que el Sengoku no entra en el examen. Es cierto, y le enseña
que hablar tiene costo.

Recordar la exclusividad: buscar a Miku y preparar material son la misma visita y
no se pueden hacer las dos. Sin eso, la biblioteca es siempre el destino óptimo.

**Escrito en §8.** Lo de arriba es el resumen; el guion cerrado, con sus tres
ramas y sus assets, está al final de este documento.

### Itsuki · Aula, después de clases

Sola y atascada. Eco directo del prólogo. **Grieta:** es la única que sí estudia y
aun así va mal, y eso le da más vergüenza que a las otras ir mal sin esforzarse;
no tiene a quién preguntarle porque preguntarle a él sería darle la razón.
**Cálida:** señalarle dónde está el error y callarse. Respeta literalmente lo que
ella exigió en el prólogo y a la vez la ayuda. **Fría:** resolvérselo delante de
ella y devolvérselo hecho. Rápido, correcto, y le quita lo único que defendía.

**No gastar aquí la disculpa de Futaro.** Sigue guardada desde el prólogo y es la
carta más fuerte que queda. Aquí él la ayuda sin admitir nada y ella lo acepta sin
agradecer.

Candidato de sprite: `itsuki_timida`, huérfano desde el prólogo, encaja en el
momento en que pide ayuda sin pedir la respuesta.

---

## 4. Evento 6 — el cierre

Mesa del centro del departamento, el mismo encuadre del prólogo. La escena que
cerró el prólogo en fracaso cierra el capítulo en victoria raspada.

**Movimiento 1 · Entrada.** Futaro hace lo contrario que en el prólogo: allí sacó
cinco cuadernos idénticos y una hoja igual para todas; aquí saca cinco hojas
distintas, una por materia, y las reparte por sitio. La tesis del capítulo hecha
imagen, sin explicarla.

Reparte cuatro y a Nino no le da ninguna. Ella se sienta sola, ofendida por la
exclusión, exigiendo la suya. Es la única forma de que se siente sin que Futaro le
pida nada. **Este detalle es del evento 6, no de la apertura.**

Todo el movimiento va en silencio; la música entra cuando las cinco están
sentadas.

**Movimiento 2 · Los cinco bloques.** Durante la sesión, no en los resultados.
Orden fijo: el del examen japonés, que no coincide con el orden canónico de las
hermanas y así no se lee como lista. Cada bloque, cuatro o cinco líneas, con dos
variantes según si fue visitada.

| Bloque | Visitada | No visitada |
|---|---|---|
| Yotsuba · literatura | dice qué siente el personaje antes de que se lo pregunten | se ofrece a ayudar a las otras y no toca su hoja |
| Ichika · matemáticas | resuelve rápido y se sorprende de sí misma | avanza mientras repasa el guion, las dos cosas a medias |
| Nino · inglés | traduce sin darse cuenta; cuando se lo señalan, lo niega | lo hace bien en silencio y no lo admite |
| Itsuki · ciencias | se atasca y pide — no la respuesta, si el planteamiento está bien | se atasca en el mismo problema del prólogo y calla |
| Miku · sociales | habla sin cortarse y sin pedir perdón después | acierta todo y no levanta la vista |

Si se preparó material para alguna, **una sola línea** dentro de su variante de
visitada donde se nota que la hoja está hecha a su medida. No un tercer bloque.

**Movimiento 3 · El examen.** Tres o cuatro líneas en negro, sin sprites. Futaro
no está ahí y eso es lo que hay que transmitir. También separa la sesión del
resultado.

**Movimiento 4 · Resultados.** Aprueban raspando **todas**, pase lo que pase, y
cada una destaca solo en la suya. El capítulo no se corta aquí por afinidad. Lo
que cambia con las visitas es el margen y el tono, no si se salva el trabajo.
Ninguna reprobó, así que Futaro conserva el empleo: la promesa del prólogo se
cumple literalmente por primera vez.

**Movimiento 5 · El boletín.** Solo, después de que se van, Futaro pone las cinco
hojas en fila y hace lo que hace siempre: calcular. Toma la nota más alta de cada
una y las suma. Le sale un boletín perfecto. Cinco asignaturas, cinco máximos,
cero huecos: un alumno completo que no existe, repartido en cinco personas que no
se hablan durante el estudio.

La última línea es suya, en pensamiento, y no resuelve nada.

CG opcional: las cinco hojas alineadas sobre la mesa, plano cenital. Si no se
genera, la narración lo sostiene.

---

## 5. Assets del capítulo

**Fondos nuevos para la apertura: ninguno.** Todo se resuelve con los ocho que ya
existen.

| Asset | Tipo | Dónde | Estado |
|---|---|---|---|
| `cg_pupitre_manana` | CG | apertura, escena 1 | pendiente |
| `cg_cinco_sentadas` | CG | apertura, escena 2 | pendiente |
| `cg_libreta` | CG | apertura, escena 4 | pendiente |
| `yotsuba incomoda` | sprite | apertura, escena 2 | pendiente |
| `nino pillada` | sprite | apertura, escena 2 | pendiente |
| `bg_biblioteca` | BG | evento Miku + preparar material | pendiente |
| `cg_miku_biblioteca` | CG | evento Miku, mov. 1 | pendiente |
| `cg_estudio_biblioteca` | CG | evento Miku, mov. 2 | pendiente |
| `cg_miku_sorpresa` | CG | evento Miku, mov. 3 | pendiente |
| `miku animada` | sprite | evento Miku | pendiente |
| `miku encogida` | sprite | evento Miku | pendiente |
| `descubrimiento` | BGM | los cinco eventos | pendiente |
| pista de atletismo | BG | evento Yotsuba | pendiente |
| sala de ensayo | BG | evento Ichika | pendiente |
| centro comercial | BG | evento Nino | pendiente |

Los sprites nuevos se declaran **como atributo, con espacio** —`image nino
pillada`, no `image nino_pillada`—, o Ren'Py los trata como un tag distinto del
personaje. El `.png` sí lleva guion bajo.

Reutilizados sin tocar: `cg_hermanas_estudiando`, `cg_maruo_reunion`,
`cg_calificacion`, y los sprites del prólogo.

### Notas de generación

**`cg_pupitre_manana`** — POV desde el pupitre de Futaro. Primer término inferior,
su mesa y su cuaderno, desenfocados y cortados por el borde. Al lado, Itsuki de
tres cuartos, estudiando, sin devolver la mirada. Aula vacía al fondo, luz fría de
primera hora. **Un solo personaje en el frame:** dos figuras con un LoRA
inexistente es donde se rompen las generaciones. El lenguaje ya está validado en
`manija_edificio`.

**`cg_cinco_sentadas`** — cinco personajes en un frame, lo más caro del capítulo.
La semilla y el encuadre de `estudio_hermanas` sirven de punto de partida: es el
mismo plano con la actitud invertida. Nadie duerme, nadie mira a otro lado, nadie
disimula.

**`yotsuba_incomoda`** — la diferencia tiene que estar en la **silueta**, no solo
en la cara: manos abajo y juntas delante, hombros encogidos, brazos pegados al
cuerpo, que ocupe menos ancho que `yotsuba_sonrisa`. Sonrisa pequeña y forzada,
sin dientes; cejas hacia arriba por dentro; mirada abajo y a un lado. **No hacerla
triste:** está incómoda mientras intenta que no se note.

**`nino_pillada`** — **descruzar los brazos.** Es la silueta más cerrada de las
cinco y descruzarla se lee a cualquier tamaño; es el único sprite del juego donde
Nino no está defendida. Ojos abiertos, boca pequeña entreabierta y rubor. El rubor
es lo que separa sorpresa de vergüenza, y aquí es vergüenza: no la sorprendieron,
se delató sola. Nombre `nino_pillada` y no `nino_sorprendida`, para dejar libre
una sorpresa real más adelante.

Los sprites nuevos, con **el mismo atuendo, encuadre y canvas** que los
existentes, o al normalizar quedan a distinta altura y el cambio de expresión se
ve como un salto. `normalizar_sprite.py` corrige tamaño, no pose.

---

## 6. Pendiente de escribir

- Cuatro eventos de hermana a nivel de escena: Yotsuba, Ichika, Nino e Itsuki
- Los tres beats fijos
- El evento 6, con sus diez bloques condicionales
- La escena de despido temprano y el aviso condicional de Maruo
- La variante del evento 6 para la ruta de tres desaires
- La pantalla del mapa y sus trampas de motor (documentar en `GUIA_RENPY.md`)

---

## 7. Guion — Apertura

**Bloque fijo. Sin decisiones. Sin puntos.**
Continúa directamente después de `jump cap1_inicio`.

Cuatro escenas: retoma la mañana siguiente, muestra el segundo intento fracasando
de una forma distinta a la del prólogo, pone fecha al examen y llega a la
conclusión que abre el mapa.

Marcadores entre corchetes. `[BG]` fondo · `[CG]` ilustración · `[SPR]` sprite ·
`[MUS]` música · `[SFX]` efecto · `[NUEVO]` asset que no existe todavía.

---

### Escena 1 · Instituto, mañana

`[BG bg_escuela]` `[SFX sfx_timbre]` `[MUS cotidiano fadein 2.5]`

**mc_pensamiento:** Dormí cuatro horas. No por estudiar, por primera vez en meses.

**mc_pensamiento:** Me quedé mirando el techo repasando la escena entera. Cinco caras idénticas y cinco formas distintas de decirme que sobro.

**mc_pensamiento:** Y una palabra que no se me despegó en toda la noche.

**mc_pensamiento:** Despedido.

**narrador:** Llegué al instituto antes que casi nadie, como siempre. Esta vez no fue por costumbre.

**mc_pensamiento:** Era el único sitio donde todavía sabía exactamente lo que estaba haciendo.

`[BG bg_aula]`

**narrador:** Mi asiento estaba libre.

`[CG NUEVO — cg_pupitre_manana: POV desde el pupitre de Futaro. Primer término inferior, su mesa y su cuaderno abierto, desenfocados y cortados por el borde. Al lado, Itsuki de tres cuartos, estudiando, sin devolver la mirada. Aula vacía al fondo, luz fría de primera hora.]`

**mc_pensamiento:** Libre, y con el pupitre de al lado ocupado.

**narrador:** Itsuki tenía la mirada clavada en su cuaderno con una concentración que no le hacía falta a las siete y media de la mañana.

**mc_pensamiento:** Me dejó el sitio a propósito. Eso también era un mensaje.

`[BG bg_aula]` `[SPR itsuki neutral at pj(0.65)]` `[MUS incomodo fadeout 1.0 fadein 1.5]`

**mc:** Buenos días.

`[SPR itsuki molesta at pj(0.65)]`

**itsuki:** …

**mc:** Voy a ir esta tarde.

**itsuki:** Ya sé que vas a ir. Vives en el mismo horario que yo desde ayer.

**mc:** Solo lo estoy avisando.

**itsuki:** Avisa lo que quieras. Yo no pienso participar.

**narrador:** Volvió a su cuaderno con un gesto seco y no dijo una palabra más en toda la mañana.

**mc_pensamiento:** Ahí estaba lo verdaderamente incómodo del asunto.

**mc_pensamiento:** No era que me odiara. Era que iba a odiarme desde las ocho hasta las tres, y después iba a seguir odiándome desde las cuatro hasta que yo me fuera de su casa.

**mc_pensamiento:** Sin pausa. Sin cambio de escenario.

**mc_pensamiento:** Jornada completa.

---

### Escena 2 · El segundo intento

`[MUS stop fadeout 1.5]`
`[BG bg_edificio]` → `[BG bg_departamento]` `[SFX sfx_puerta_abre]`

**narrador:** Toqué a las cuatro en punto. Me abrió Ichika, otra vez, con la misma sonrisa de la primera vez.

**mc_pensamiento:** Esta vez venía preparado. Cinco cuadernos, un temario dividido por materias y ninguna expectativa.

**mc_pensamiento:** Lo que no esperaba era lo que encontré al entrar.

`[CG NUEVO — cg_cinco_sentadas: las cinco a la misma mesa, sentadas, rectas, cuadernos abiertos, mirando hacia cámara. Mismo encuadre y misma luz que cg_hermanas_estudiando —esa semilla sirve de punto de partida—, pero con la actitud invertida: nadie duerme, nadie mira a otro lado, nadie disimula. Es la imagen que da miedo. Sostiene toda la primera mitad de la escena, así que tiene que aguantar en pantalla.]`

`[MUS extraneza fadein 2.0]`

**narrador:** Las cinco estaban sentadas alrededor de la mesa. Rectas. En silencio. Con los cuadernos abiertos.

**mc_pensamiento:** …

**mc_pensamiento:** Esto está mal.

**yotsuba:** ¡Buenas tardes, profesor!

**mc:** No soy profesor.

**ichika:** Hoy sí. Hoy vamos a portarnos bien.

**mc_pensamiento:** Ayer tuve que arrastrarlas una por una para que se sentaran. Hoy me estaban esperando.

**mc_pensamiento:** Nadie mejora tanto en veinticuatro horas. Nadie.

**nino:** ¿Vas a quedarte parado o vas a dar la clase?

**mc:** Depende. ¿Qué es esto?

**nino:** Colaboración.

**mc:** Ayer me dijiste que no ibas a gastar un solo segundo en esto.

**nino:** Y hoy cambié de opinión. ¿Algún problema?

**narrador:** Lo dijo sin apartar la mirada. Ninguna de las otras cuatro se movió.

**mc_pensamiento:** Ninguna de ellas está aquí porque quiera estar.

**mc_pensamiento:** Están aquí porque ella les dijo que se sentaran.

**mc_pensamiento:** Bien. Si quieren jugar a esto, juguemos.

**mc:** Página doce. Empezamos por lo más simple del temario.

**narrador:** Repartí el ejercicio. Cinco copias idénticas, seis preguntas cada una, nivel de primer curso.

**mc:** Diez minutos.

**narrador:** No hizo falta esperar diez. En cuatro ya las tenía las cinco encima de la mesa.

**mc_pensamiento:** Eso también estaba mal.

`[SFX sfx_hoja]`

**narrador:** Corregí la primera. Seis de seis mal.

**narrador:** Corregí la segunda. Seis de seis mal.

**mc_pensamiento:** …

**narrador:** Las cinco hojas tenían exactamente las mismas seis respuestas equivocadas. Palabra por palabra.

**mc_pensamiento:** No es que no supieran hacerlo.

**mc_pensamiento:** Es que se pusieron de acuerdo en cómo hacerlo mal.

`[MUS caos fadeout 0.5 fadein 1.0]`

**mc:** Nino.

**nino:** ¿Sí?

**mc:** Coordinar cinco respuestas idénticas cuesta más trabajo que responder bien.

**nino:** Qué observación tan interesante.

**mc:** Es una observación matemática. Si querían perder el tiempo, tenían formas más baratas.

**nino:** Entonces tómalo como lo que es.

**nino:** Cinco alumnas que no aprenden nada contigo, por escrito y por triplicado.

**nino:** Mi padre va a leer esas hojas.

**mc_pensamiento:** Ahí estaba.

**mc_pensamiento:** No querían echarme a gritos. Querían un informe.

**mc:** Vas a hacer que reprueben para que me despidan.

**nino:** Voy a hacer que quede claro lo que ya era obvio ayer.

**nino:** El último duró cuatro días. Tú llevas uno.

`[BG bg_departamento with dissolve]` `[SPR NUEVO — yotsuba_incomoda at pj(0.70)]`

**yotsuba:** Nino, eso no es justo. Él solo está—

**nino:** Yotsuba.

**yotsuba:** …No dije nada.

**mc_pensamiento:** Iba a defenderme. Y se arrepintió a mitad de frase.

**narrador:** Se encogió en el sitio y se puso a alinear los bordes de su hoja con las dos manos, muy despacio, como si eso fuera una tarea.

**mc_pensamiento:** Esa no está de acuerdo.

**mc_pensamiento:** Está obedeciendo, que no es lo mismo.

`[SPR ichika sonriendo at pj(0.30)]` `[SPR yotsuba at pj_calla(0.70)]`

**ichika:** Bueno, tampoco hay que dramatizar. Contestamos las seis. Nadie dijo que hubiera que acertarlas.

**mc:** Contestaron las seis igual de mal.

**ichika:** Coincidencia. Somos hermanas, pensamos parecido.

**mc_pensamiento:** Esa mentía tan bien que casi daba gusto.

`[CG cg_hermanas_estudiando]`

**narrador:** Para cuando volví a levantar la vista, Ichika ya tenía los ojos cerrados y la cabeza apoyada en el respaldo.

**mc_pensamiento:** Y ahí se cayó la función.

**narrador:** Miku no había levantado la vista de la mesa en todo el rato. Tenía los auriculares puestos y, esta vez, sonando.

**narrador:** Itsuki estaba sentada aparte, con los brazos cruzados y la cara torcida hacia la ventana.

**mc_pensamiento:** Y esa no participó del plan, pero tampoco pensaba salvarme.

**narrador:** Junté las cinco hojas y las dejé en una pila.

**mc:** Última pregunta y me voy. La siete no estaba en la hoja.

**mc:** *«He didn't want to go, but he had to.»*

**narrador:** Lo leí a propósito plano, con el peor acento que pude.

`[BG bg_departamento with dissolve]` `[SPR nino neutral at pj_habla(0.5)]`

**nino:** *Had to.* No *«jad tu»*. Se pega, no se separa.

**narrador:** Silencio.

`[SPR NUEVO — nino_sorprendida at pj(0.5)]`

**nino:** …

**mc:** Gracias.

**nino:** ¡No te he corregido a ti! ¡Es que dolía escucharlo!

**mc:** Claro.

**nino:** ¡Se acabó! ¡Fuera de mi casa!

`[SFX sfx_puerta_cierra volume 2.0]` `[MUS stop fadeout 2.0]`

**narrador:** Se levantó y se encerró de un portazo, igual que el día anterior, solo que esta vez se llevó su cuaderno con ella.

**narrador:** Las otras tres tardaron menos de un minuto en desaparecer detrás de ella.

**narrador:** Miku fue la última. Se detuvo a mitad del pasillo, de espaldas, con el libro apretado contra el pecho.

`[SPR miku aburrida at pj(0.5)]`

**miku:** …No fue idea mía.

**narrador:** Lo dijo tan bajo que tuve que reconstruirlo un segundo después, cuando ya no estaba.

**narrador:** Porque en cuanto lo dijo, se dio cuenta de que lo había dicho.

**miku:** …Olvídalo. Perdón.

`[SPR miku hide with moveoutleft]`

**mc_pensamiento:** Es la segunda vez que habla sin querer y la segunda vez que pide perdón por haberlo hecho.

**mc_pensamiento:** Nadie se disculpa por decir algo cierto, a menos que le hayan enseñado que decirlo cuesta.

**mc_pensamiento:** Segundo día. Segundo fracaso.

**mc_pensamiento:** Pero por primera vez me llevaba algo a casa.

---

### Escena 3 · El plazo

`[BG bg_departamento]` `[SFX sfx_puerta_abre volume 1.0]`

**narrador:** Estaba recogiendo cuando la puerta del fondo se abrió.

`[CG cg_maruo_reunion]` `[MUS contrato fadein 2.0]`

**maruo:** Vi las hojas.

**mc_pensamiento:** Rápido. Muy rápido.

**maruo:** Seis errores idénticos por cinco. Supongo que no hace falta que te explique lo que significa.

**mc:** No hace falta.

**maruo:** ¿Y bien?

**mc:** Significa que son capaces de coordinar cinco respuestas iguales en cuatro minutos.

**mc:** Eso no lo hace alguien que no entiende el ejercicio.

**narrador:** Maruo me miró un momento más largo de lo que me había mirado el día anterior.

**maruo:** Los exámenes trimestrales son en un mes.

**maruo:** Cinco asignaturas. Las cinco tienen que aprobarlas todas.

**mc:** ¿Y si una sola reprueba?

**maruo:** Ya te lo dije ayer y no lo voy a repetir dos veces.

`[SFX sfx_puerta_cierra volume 1.0]`

**narrador:** Se fue como se había ido el día anterior, sin subir la voz y sin dejar espacio para contestar.

**mc_pensamiento:** Un mes.

**mc_pensamiento:** Treinta días para cinco alumnas que hoy se organizaron para reprobar.

---

### Escena 4 · La conclusión

`[MUS stop fadeout 2.0]`
`[BG bg_negro with fade]`

**narrador:** Salí del edificio pasadas las siete. Esta vez no fui directo a casa.

`[BG bg_cuarto_mc]` `[MUS hogar fadein 1.5 volume 0.7]`

**narrador:** Puse las cinco hojas sobre el escritorio y las dejé ahí un buen rato sin tocarlas.

**mc_pensamiento:** Ayer pensé que el problema era que no querían estudiar.

**mc_pensamiento:** Hoy sé que el problema es otro.

**mc_pensamiento:** No es que no puedan. Es que se defienden.

**mc_pensamiento:** Y se defienden juntas.

`[SFX sfx_toque_puerta volume 1.5]` `[SPR raiha hablando at pj(0.30)]`

**raiha:** Hermanito, llevas media hora mirando unos papeles en blanco.

**mc:** No están en blanco.

**raiha:** Están llenos de cosas mal, que es casi peor.

**mc:** Gracias por el ánimo.

`[SPR raiha regano at pj(0.30)]`

**raiha:** ¡Yo solo digo lo que veo!

**raiha:** ¿Son de las chicas esas a las que les das clase?

**mc:** Sí.

**raiha:** ¿Y son tontas?

**mc:** No.

**narrador:** Contesté antes de pensarlo, y me di cuenta de que lo decía en serio.

**mc:** No, no lo son.

**raiha:** Entonces no entiendo el problema.

`[SPR raiha hide with moveoutleft]`

**narrador:** Se fue tan rápido como había entrado, muy contenta de haber resuelto algo.

**mc_pensamiento:** …

**mc_pensamiento:** Repasemos.

**mc_pensamiento:** Cinco respuestas idénticas en cuatro minutos. Eso requiere ponerse de acuerdo antes, repartirse el error y sostenerlo delante de mí sin fallar ninguna.

**mc_pensamiento:** Es un trabajo en equipo mejor ejecutado que la mitad de los proyectos de mi clase.

**mc_pensamiento:** Y Nino me corrigió un *had to* sin pensarlo, molesta, en mitad de una discusión.

**mc_pensamiento:** Nadie corrige por reflejo algo que no domina.

**narrador:** Volví a mirar las cinco hojas. En la de Miku, debajo de la respuesta equivocada, había una marca de goma mal borrada.

**mc_pensamiento:** Escribió la correcta primero.

**mc_pensamiento:** Y después la borró.

**mc_pensamiento:** Es la misma que ayer me habló de logística del período Sengoku sin que nadie se lo preguntara.

**mc_pensamiento:** No son cinco alumnas malas.

**mc_pensamiento:** Son cinco personas que saben una cosa cada una y que han decidido no enseñármela.

**narrador:** Abrí la libreta por la página donde había anotado los cinco nombres la noche anterior.

**narrador:** Debajo de la línea escribí una sola frase.

`[CG NUEVO — cg_libreta: la libreta abierta, los cinco nombres en columna y una frase debajo. Plano cenital cerrado, luz de lámpara. Texto ilegible a propósito: se lee la forma, no las palabras.]`

**mc_pensamiento:** De frente y las cinco a la vez, pierdo siempre. Son un bloque y yo soy uno.

**mc_pensamiento:** Así que no voy a ir de frente.

**mc_pensamiento:** Voy a ir de una en una.

**mc_pensamiento:** Y no en esa casa, donde se cubren entre ellas.

**mc_pensamiento:** Donde cada una esté sola.

**narrador:** Apagué la lámpara.

`[BG bg_negro with fade]`

**narrador:** Treinta días.

---

→ **Sale al hub 1.** La primera elección del jugador escribe `primera_conexion`.

---
