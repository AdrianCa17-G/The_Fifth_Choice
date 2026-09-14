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

## 8. Evento de hermana · Miku — Biblioteca

**Escrito.** Assets pendientes. Encaja en cualquiera de los tres huecos.

Marcadores como en la apertura. `[BG]` fondo · `[CG]` ilustración · `[SPR]` sprite ·
`[MUS]` música · `[SFX]` efecto · `[NUEVO]` asset que no existe todavía ·
`[$]` línea de código.

---

### Decisiones de este evento

**No depende de nada.** No menciona la crisis de Nino, ni el beat de Itsuki, ni
los otros eventos. Todo lo que da por sabido ocurrió sí o sí: el libro de Sengoku
del prólogo y la marca de goma de la apertura. Se puede jugar primero, segundo o
tercero sin cambiar una línea.

**La biblioteca es municipal, no la del instituto.** El instituto es terreno de
Futaro; el mapa dice que a las otras cuatro hay que ir a buscarlas al suyo. Y
dice algo de ella: se va a leer lo que le gusta a un sitio donde nadie de su casa
la ve hacerlo.

**La historia se cuenta para quien no sabe nada de historia.** Ni un nombre de
batalla, ni una fecha, ni una provincia por su nombre. Solo dos personas —Shingen
y Kenshin—, y todo lo demás explicado por lo que se entiende sin estudiar: no
había refrigeradores, sin sal la comida se pudre, treinta mil hombres comen tres
veces al día. Si el jugador tiene que esforzarse para seguirla, deja de escuchar
a Miku y se pone a descifrar un temario, que es justo lo contrario de lo que hace
esta escena. El objetivo no es que aprenda del Sengoku: es que entienda por qué a
ella le brillan los ojos.

**El recurso formal: los puntos suspensivos.** Miku entra en todas sus frases con
«…» desde el prólogo. En el arranque de este evento también. Cuando se suelta,
**desaparecen**, y las frases se le alargan. Cuando se da cuenta de que ha
hablado, vuelven en la misma línea. Es el único indicador de que algo cambió y no
hace falta narrarlo: el jugador lo lee sin saber que lo está leyendo.

**Futaro se equivoca de verdad.** Ella no responde a preguntas, responde a
errores —así arrancó su primera línea del prólogo— pero el error no puede ser una
trampa. Miku es la única de las cinco con la que no hay cálculo: él se lee el
libro, llega hasta donde llega en una noche y se equivoca porque cuatro horas no
alcanzan. La llave sigue siendo el error; el motor pasa a ser el trabajo, que es
lo único que este protagonista sabe ofrecer.

Y el evento se cierra con que **ella se da cuenta de que él lo leyó**. No de que
la manipuló: de que alguien se pasó una noche con su tema. Ese es el hito de esta
ruta y conviene que llegue temprano, porque de ahí cuelga todo lo demás.

**Lo que este evento NO gasta.** El bloque de Miku del evento 6 —«habla sin
cortarse y sin pedir perdón después»— es el pago. Aquí como mucho llega a
tragarse el «perdón» a medias, y solo en la rama cálida. No se le entrega ninguna
hoja hecha a su medida: eso es del evento 6 y de preparar material.

---

### Movimiento 1 · Llegada

`[BG NUEVO — bg_biblioteca]` `[MUS stop fadeout 1.0]`

**narrador:** La biblioteca municipal quedaba dos calles antes del edificio. Pasaba por delante todos los días y nunca había entrado.

**narrador:** Segunda planta, la sala de lectura. Cuatro mesas largas y nadie en tres de ellas.

`[CG NUEVO — cg_miku_biblioteca: Miku de tres cuartos en la mesa del fondo, leyendo, con la pila de libros a un lado y los audífonos COLGADOS DEL CUELLO, nunca puestos. Ventanal detrás, luz de tarde. Cámara desde un costado, no desde la puerta. Un solo personaje en el frame. Sostiene todo el movimiento 1, así que tiene que aguantar en pantalla.]`

**narrador:** Estaba al fondo, de espaldas a la puerta, con una pila de libros a la izquierda y los audífonos colgados del cuello.

**mc_pensamiento:** Cuatro libros. Ninguno del temario.

**mc_pensamiento:** Y no estaban amontonados. Estaban apilados por tamaño, con los lomos alineados.

**narrador:** No pasaba las páginas. Se quedaba en cada una bastante más de lo que se tarda en leerla.

**mc_pensamiento:** Así no se estudia.

**mc_pensamiento:** Así se lee.

**mc_pensamiento:** Y los audífonos estaban apagados.

**mc_pensamiento:** A esa distancia se oye algo, aunque sea un zumbido. No había nada.

**mc_pensamiento:** El otro día, en el departamento, se los subió en cuanto saqué las hojas. Me borró del mapa sin decir una palabra.

**mc_pensamiento:** No los lleva para escuchar música. Los lleva ahí abajo, listos, para el momento en que alguien se acerque.

**narrador:** Me senté enfrente.

**narrador:** Tardó tres segundos largos en levantar la vista.

`[BG bg_biblioteca with dissolve]` `[SPR miku neutral at pj(0.5)]`

**miku:** …

**mc:** Buenas tardes.

**miku:** …

**miku:** …¿Cómo sabías que estaba aquí?

**mc:** No lo sabía. Llevo una hora dando vueltas.

**mc:** Pasé por tu casa primero. Ninguna de tus hermanas supo decirme dónde estabas.

**narrador:** Algo se le movió en la cara al oír eso, tan rápido que no me dio tiempo a leerlo.

**miku:** …¿Y entonces?

**mc:** El libro que llevabas el otro día tenía una etiqueta de biblioteca en el lomo. Esta es la que queda cerca del edificio.

**narrador:** Bajó el libro dos dedos, lo justo para mirarme por encima del canto.

**miku:** …Ah.

**narrador:** No pareció convencerle del todo, pero tampoco se levantó.

---

### Movimiento 2 · El intento por la puerta principal

`[SFX sfx_papel_mesa volume 2.5]`

**narrador:** Saqué el temario de sociales y lo puse sobre la mesa, girado hacia ella.

`[CG NUEVO — cg_estudio_biblioteca: POV desde el sitio de Futaro. Primer término inferior, sus antebrazos y sus manos sosteniendo el temario abierto sobre la mesa, desenfocados y cortados por el borde. Enfrente, Miku de tres cuartos con su libro, sin devolver la mirada. Mismo lenguaje que cg_pupitre_manana y cg_manija_edificio: nada de cara, nada que el modelo pueda romper.]`

**mc:** Tres semanas y media para el examen. Sociales es tu asignatura.

**miku:** …No es mi asignatura.

**mc:** Es la que tienes peor y la que más fácil sube. Empezamos por ahí.

**miku:** …

**mc:** Unificación de Japón. Del final de las guerras civiles al periodo Edo. Entra entero.

**miku:** …Está bien.

**mc:** ¿Está bien que sí, o está bien que me calle?

**miku:** …

**mc:** Lo voy a tomar como que sí.

**narrador:** Bajó la vista al temario tres segundos y la volvió a subir al libro que tenía abierto.

**mc_pensamiento:** Tres segundos. Los conté.

**mc_pensamiento:** Perfecto. Un muro de ladrillo, pero educado.

**mc_pensamiento:** Llevo dos días haciendo lo mismo con las cinco y funcionando con ninguna.

**mc_pensamiento:** Repasemos lo que sé de esta.

**mc_pensamiento:** Uno: en su hoja de ayer había una marca de goma debajo de la respuesta equivocada. Escribió la correcta primero y la borró.

**mc_pensamiento:** Dos: el otro día habló de logística del período Sengoku sin que nadie le preguntara, y se escondió detrás del libro en cuanto se oyó a sí misma.

**mc_pensamiento:** Tres: lleva unos audífonos apagados colgados del cuello, listos para subírselos en cuanto alguien le hable.

**mc_pensamiento:** No es que no sepa. Es que no piensa hablar de nada que le importe delante de alguien que va a calificarla.

**mc_pensamiento:** Y no se me ocurrió ninguna forma elegante de resolver eso.

**mc_pensamiento:** Solo se me ocurrió la de siempre.

---

### Movimiento 3 · La página noventa

**narrador:** Cerré el temario y saqué de la mochila otro libro, con la misma etiqueta en el lomo que los suyos.

`[SFX sfx_papel_mesa volume 2.5]`

**narrador:** Lo reconoció antes de que llegara a la mesa.

`[CG NUEVO — cg_miku_sorpresa: mismo encuadre y misma luz que cg_miku_biblioteca —esa semilla sirve de punto de partida— pero con el libro bajado del todo, los ojos abiertos y la mirada fuera del libro por primera vez. El ejemplar de Futaro entra en el cuadro por el borde inferior, sin mano. Es el otro lado de la moneda del primero: en aquel no miraba, en este mira.]`

**miku:** …Ese es el que estaba leyendo yo.

**mc:** Hay dos ejemplares. Lo saqué anoche.

**miku:** …¿Por qué?

**mc:** Porque el otro día dijiste que las batallas las gana quien mueve el arroz y no entendí nada.

**narrador:** No dijo nada. Pero tampoco volvió al libro.

**mc:** Llegué hasta la página noventa. Me quedé dormido a las tres.

**mc:** Y creo que el tipo que lo escribió se equivoca.

`[BG bg_biblioteca with dissolve]` `[SPR miku neutral at pj_habla(0.5)]`

**miku:** …¿En qué?

**mc:** Le dedica cuarenta páginas a cómo se movía la comida y seis a la batalla más famosa del siglo. Está al revés.

**mc:** Las guerras las ganan las batallas. Lo demás es papeleo.

**narrador:** Cerró el libro sobre el dedo índice, para no perder la página.

**mc_pensamiento:** Era la primera vez en dos días que dejaba de mirar a otro lado.

**miku:** …¿Y qué comían?

**mc:** ¿Quiénes?

**miku:** …Los treinta mil hombres. En esa batalla famosa.

**mc:** …

**miku:** …Tres veces al día. Todos los días. Durante las seis semanas que tardaron en llegar hasta ahí caminando.

**mc:** Eso lo resolvería alguien. No es lo importante.

`[SPR NUEVO — miku animada at pj_habla(0.5)]` `[MUS NUEVO — descubrimiento fadein 2.0]`

**miku:** Había un señor de la guerra que se llamaba Takeda Shingen.

**miku:** Su provincia estaba metida entre montañas. No tenía nada de costa.

**mc:** ¿Y eso es un problema?

**miku:** Sin mar no hay sal. Y sin sal no se podía guardar la comida: no existían las neveras. O salabas el pescado y la carne, o en tres días no servían.

**miku:** Toda la sal que comía su gente se la compraban a los vecinos.

**narrador:** Hablaba más rápido. No había subido la voz —seguíamos en una biblioteca—, pero las frases le habían dejado de empezar con una pausa.

**miku:** Y un día los vecinos se pusieron de acuerdo y dejaron de vendérsela.

**mc:** …Sin atacarlo.

**miku:** Sin un soldado. Sin salir de su casa. Solo dejaron de vender.

**mc:** ¿Y qué hizo?

**miku:** Nada. No había nada que hacer. Lo estaba perdiendo.

**miku:** Y entonces le mandó sal Uesugi Kenshin. Su peor enemigo. Llevaban diez años peleándose y ninguno de los dos había conseguido ganar.

**mc:** ¿Por qué haría eso?

**miku:** Dijo que él peleaba con armas, no con comida. Que quería ganarle en un campo de batalla, no verlo morirse de hambre en su casa.

**miku:** De ahí sale una frase que en Japón todavía se dice. «Mandarle sal al enemigo.» Se usa para cuando ayudas a alguien que no soportas, porque hay cosas que no se hacen.

**miku:** Aunque seguramente no pasó.

**mc:** …¿Cómo que no pasó?

**miku:** Esa parte no aparece en ningún papel de la época. Está escrita cien años después, cuando ya quedaba bonita.

**miku:** Lo que sí es seguro es que le cortaron la sal y que ahí dentro siguió habiendo sal igual. Alguien se la vendió.

**miku:** Y a mí eso me parece mucho más—

`[SPR NUEVO — miku encogida at pj(0.5)]` `[MUS stop fadeout 1.5]`

**narrador:** Se paró en mitad de la palabra.

**narrador:** Creo que se oyó. Fue eso: se oyó a sí misma hablando en voz alta durante un minuto entero.

**miku:** …

**miku:** …Perdón. Hablé mucho.

**narrador:** Y volvió a abrir el libro por donde tenía el dedo.

---

### Movimiento 4 · La decisión

**mc_pensamiento:** Tercera vez.

**mc_pensamiento:** Tercera vez que dice algo que nadie le pidió y tercera vez que se disculpa por haberlo dicho.

**mc_pensamiento:** Nadie se disculpa por decir algo cierto, a menos que le hayan enseñado que decirlo cuesta.

`menu:`

---

**Opción A · «Preguntarle otra cosa.»** *(cálida — `[$ sumar_punto("miku", 1)]`)*

**mc:** ¿Cuánto tardaba la sal en llegar desde el mar hasta allá?

`[SPR miku encogida at pj_habla(0.5)]`

**miku:** …¿Qué?

**mc:** Es una pregunta. Montaña, carga a lomo de animal, hace quinientos años. Cuánto tardaba.

**miku:** …Diez días. Doce si llovía.

**mc:** ¿Y cuánto aguantaban ellos sin sal?

`[SPR miku animada at pj_habla(0.5)]` `[MUS descubrimiento fadein 2.0]`

**miku:** Depende de la época del año. En verano, con el pescado, casi nada. Por eso cortarles la sal no era una amenaza para más adelante, era de ese mismo mes. Eso es lo que a la gente se le esca—

**narrador:** Se detuvo otra vez. Pero esta vez se detuvo distinto: se detuvo mirándome a mí, no al libro.

**miku:** …Per—

**mc:** No.

**miku:** …

**mc:** Estabas contestando una pregunta que te hice yo. Eso no se disculpa.

**narrador:** No dijo nada. Se le puso el libro a media altura, sin llegar a subirlo del todo.

**narrador:** Y entonces miró el ejemplar que yo había dejado sobre la mesa.

**miku:** …Dijiste que llegaste a la página noventa.

**mc:** Noventa y dos.

**miku:** …Lo de la sal está en la ciento veinte.

**narrador:** Lo dijo despacio, como quien termina una cuenta.

**mc_pensamiento:** Ahí estaba lo que acababa de entender.

**mc_pensamiento:** No que yo supiera de esto. Justo lo contrario: que no sabía nada, y que aun así me había pasado la noche con ello.

**mc:** Voy a llegar a la ciento veinte.

**miku:** …

**mc:** Lo que acabas de contarme son tres preguntas del examen. Rutas de comercio, cómo se sostenía una provincia y por qué acabó unificándose el país.

**mc:** No te falta la materia. Te falta creer que lo que sabes cuenta como saber.

**miku:** …No es lo mismo.

**mc:** Es exactamente lo mismo, y lo vas a comprobar en tres semanas.

**narrador:** No me contestó. Pero cuando me levanté, el libro seguía a media altura y no había vuelto a subir.

---

**Opción B · «Decirle que se le da bien.»** *(tibia — sin puntos, sin desaire)*

**mc:** Se te da bien esto.

`[SPR miku encogida at pj_habla(0.5)]`

**miku:** …No se me da bien. Solo lo he leído.

**mc:** Que es más de lo que ha hecho nadie en tu casa.

**miku:** …Eso no es difícil.

**narrador:** Lo dijo sin ninguna gracia, como quien cierra una puerta con educación.

**mc_pensamiento:** Le acabo de poner una nota.

**mc_pensamiento:** Y ella lleva toda la vida escuchando notas comparadas con otras cuatro.

**narrador:** El libro le subió hasta media cara, y ahí se quedó.

---

**Opción C · «El Sengoku no entra en el examen.»** *(fría — `[$ desaires_cap1 += 1]`)*

**mc:** Nada de eso entra en el examen.

**mc:** Unificación de Japón, tres temas, y ninguno pregunta por la sal. Si vas a dedicarle una hora a algo, que sea a lo que te van a preguntar.

`[SPR miku neutral at pj(0.5)]`

**narrador:** No protestó. No se defendió. Asintió una vez, muy despacio, como si le hubieran confirmado algo que ya sospechaba.

**miku:** …Ya lo sé.

**narrador:** Miró un segundo el ejemplar que yo había dejado sobre la mesa, y después apartó la vista.

**mc:** Entonces empecemos por el tema uno.

**miku:** …Hoy no.

`[SFX sfx_silla volume 2.5]`

**narrador:** Recogió los cuatro libros, los apiló y se subió los audífonos.

**narrador:** Y esta vez, desde donde yo estaba, se oía la música.

**mc_pensamiento:** …

**mc_pensamiento:** Antes no sonaban.

---

### Movimiento 5 · Cierre

*(común a las tres ramas; la última línea cambia)*

`[BG bg_negro with fade]`

**narrador:** Salí de la biblioteca cuando estaban apagando las luces de la segunda planta.

**mc_pensamiento:** Una de cinco. Y ni siquiera entera.

**mc_pensamiento:** Quedan tres semanas.

*Cierre A (cálida):*

**mc_pensamiento:** Pero hoy alguien me habló durante un minuto seguido sin que yo se lo pidiera dos veces.

**mc_pensamiento:** Eso, en esa casa, es un récord.

*Cierre B (tibia):*

**mc_pensamiento:** Dijo cuatro frases y volvió a esconderse. No sé si perdí algo, pero desde luego no gané nada.

*Cierre C (fría):*

**mc_pensamiento:** Tenía razón en lo del examen.

**mc_pensamiento:** Lo raro es que llevo toda la tarde con la sensación de haber hecho algo mal teniendo razón.

`→ Vuelve al hub.`

---

### Assets del evento

| Asset | Tipo | Estado | Nota |
|---|---|---|---|
| `bg_biblioteca` | BG | pendiente | Sala de lectura, tarde. Mesas largas, vacía. Ya estaba en el mapa |
| `cg_miku_biblioteca` | CG | pendiente | Movimiento 1. Ella leyendo, sin saber que la miran |
| `cg_estudio_biblioteca` | CG | pendiente | Movimiento 2. POV, solo antebrazos de Futaro |
| `cg_miku_sorpresa` | CG | pendiente | Movimiento 3. Reaprovecha la semilla del primero |
| `miku animada` | sprite | pendiente | El único sprite del juego donde habla por gusto |
| `miku encogida` | sprite | pendiente | El medio segundo después de oírse |
| `descubrimiento` | BGM | pendiente | Sirve para los cinco eventos, no solo este |

Reutilizados sin tocar: `miku neutral`, `sfx_papel_mesa`, `sfx_silla`, `bg_negro`.

**Los tres CG son un tercio del presupuesto de arte del capítulo.** Si hay que
recortar, el que se cae es `cg_estudio_biblioteca`: es el único cuyo momento
—Futaro estrellándose contra el muro— se sostiene igual de bien con
`bg_biblioteca` y el sprite. Los otros dos no son intercambiables entre sí: el
primero es ella sin saber que la miran y el tercero es ella mirando, y esa
inversión es el evento entero en dos imágenes.

**`cg_miku_biblioteca` y `cg_miku_sorpresa` van con la misma semilla.** Mismo
encuadre, misma luz, mismo sitio; lo único que cambia es la altura del libro y a
dónde va la mirada. Generarlos en la misma sesión y guardar la semilla: si se
hacen por separado con semanas de diferencia, no van a coincidir y la inversión
deja de leerse.

**`miku animada`** — la diferencia va en la **silueta**, no en la cara: el libro
abajo o fuera del cuadro, hombros abiertos, barbilla arriba. En todos los sprites
que existen de las cinco hay algo delante del cuerpo; aquí no hay nada. A un 30 %
de tamaño eso es lo único que se lee. Ojos abiertos, sonrisa mínima o ninguna
—no está contenta, está concentrada—, y **sin rubor**: el rubor la haría tímida y
en ese minuto no lo es.

**`miku encogida`** — misma pose que `neutral` pero con el libro subiendo, a
media cara, y la mirada de lado hacia el interlocutor. Es la que más se va a
reutilizar en los tres capítulos.

**`descubrimiento`** — entra dos veces y sale dos veces, siempre con ella
hablando. Nunca suena con Futaro razonando: si acompaña al monólogo de él deja de
ser el tema de las hermanas y pasa a ser fondo, que es lo que ya se decidió con
`hogar` en el prólogo. Si al final no se produce, la escena aguanta en silencio;
la biblioteca es el sitio del juego donde el silencio no se nota.

---

### Notas de implementación

- El evento abre con `$ sumar_punto("miku", 2)` en la primera línea del label,
  antes de nada. Si el jugador eligió la biblioteca en el hub 1, esa llamada es
  la que escribe `primera_conexion`.
- La opción cálida suma **+1 aparte**, con una segunda llamada al helper. Nunca
  `puntos_miku += 3` de golpe.
- La fría toca `desaires_cap1`, no los puntos. No resta afinidad: el jugador que
  la enfría se queda en 2, no en 1.
- Marcar el evento como consumido —`miku_visitada_cap1`— para el evento 6 y para
  que el hub ofrezca la revisita corta en lugar del evento entero.
- La exclusividad de la biblioteca (buscar a Miku **o** preparar material) se
  resuelve en el menú del hub, no aquí dentro.
- Todo `show` con su posición, incluidos los `pj_habla` de las respuestas de
  Miku. Está a 0.5 durante toda la escena porque es la única en pantalla.
