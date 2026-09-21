# Capítulo 1 — estado

**En escritura.** Estructura cerrada, apertura terminada y los evento de Miku,
Yotsuba e Itsuki escrito (§8). Quedan dos eventos de hub, los tres beats fijos 
y el evento final.

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

**Escrito en §8.** Lo de arriba es el resumen; el guion cerrado, con sus tres
ramas y sus assets, está al final de este documento.

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

**Escrito en §8.** Lo de arriba es el resumen; el guion cerrado, con sus tres
ramas y sus assets, está al final de este documento.

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

