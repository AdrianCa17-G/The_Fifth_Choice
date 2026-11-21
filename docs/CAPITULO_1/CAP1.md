# Capítulo 1 — resumen del capítulo cerrado

**Terminado y lanzado** en la versión 1.0 (21/11/2026). Este documento resume qué
es el capítulo y qué deja preparado para el Capítulo 2. **No es el guion:** el
guion vive en los `.rpy` y en los borradores de esta carpeta. Si este resumen y el
código no coinciden, manda el código.

Lo transversal (arte, audio, motor, interfaz) está en las guías de `docs/`.

---

## 1. Esqueleto

```
APERTURA → HUB 1 → evento → BEAT Itsuki → HUB 2 → evento
→ BEAT crisis de Nino → HUB 3 → evento → BEAT casa → EVENTO 6
```

Las interconexiones entre bloques viven en `02_cap1_conexiones.rpy`.

| Bloque | Archivo |
|---|---|
| Apertura | `02_cap1_apertura.rpy` |
| Hubs (mapa, evento, control de desaires) | `02_cap1_hubs.rpy` + `hub_mapa.rpy` |
| Eventos de hermana | `02_cap1_Ichika.rpy`, `_Nino`, `_Miku`, `_Yotsuba`, `_Itsuki` |
| Beats fijos | `02_cap1_beat_Itsuki.rpy`, `_beat_Nino`, `_beat_casa` (con `07b_collage.rpy`) |
| Evento 6 | `02_cap1_evento6.rpy` + `10_*.rpy`, `12_e6_pantallas.rpy`, `15_chat_grupo.rpy` |
| Despido temprano | `02_cap1_final_malo.rpy` (entrada en `05_finales.rpy`) |
| Cierre | `14_progreso_chicas.rpy`, `16_creditos.rpy` |

---

## 2. Decisiones de diseño cerradas

**Hubs, no calendario.** El capítulo avanza por beats fijos; entre uno y otro se
abre el mapa y el jugador elige a quién buscar. El tiempo lo narra el texto.

**Cinco eventos, tres por partida.** Dos hermanas se quedan sin evento cada vez, y
eso es lo que hace que elegir pese. **Cada evento funciona en cualquiera de los
tres huecos**: ninguno depende de otro ni de que un beat haya pasado.

**Itsuki y Nino empujan el conflicto.** Son las únicas con beat propio. En el
Capítulo 2 conviene invertirlo y darles los beats fijos a Miku y Yotsuba.

**Reparto canónico de materias.** Ichika matemáticas, Nino inglés, Miku sociales,
Yotsuba japonés (Japonés y Literatura son la misma materia), Itsuki ciencias.
Cierra sobre las cinco asignaturas del examen sin sobras ni huecos.

**La tesis:** no son cinco alumnas malas, son un estudiante completo repartido en
cinco personas. El Evento 6 lo vuelve imagen con el boletín.

**Linealidad.** Ninguna hermana conocía antes al protagonista. Nada de la niña de
Kioto.

---

## 3. Los cinco eventos de hermana

Anatomía común: **Llegada → Grieta → Decisión → Cierre.** La decisión usa
`decision_peso` (rótulo «Hora de decidir» y tarjetas) y siempre tiene tres ramas:

| Rama | Efecto | Qué es |
|---|---|---|
| Cálida | `sumar_punto(h, 3)` | Entender lo que la hermana no dijo |
| Tibia | `sumar_punto(h, 1)` | Amable, pero se queda en la superficie |
| Fría | `desaires_cap1 += 1` | El protagonista del día 1. Nunca crueldad |

Cada evento guarda su rama en `<h>_rama_cap1` (se lee con `rama_de(h)`) y marca
`<h>_visitada_cap1`. El sello del mapa, la animación de tarde completada y el
Evento 6 leen esa rama.

| Hermana · lugar | La grieta | Cálida | Tibia | Fría |
|---|---|---|---|---|
| **Ichika** · Sala de ensayo | Se durmió en el suelo del club de puro agotamiento y lo tapa con bromas | No seguirle la broma; esperar a que hable | Seguirle la broma | «Si tienes energía para chistes, tienes energía para estudiar» |
| **Nino** · Centro comercial | No desconfía de él, desconfía del puesto: los tutores anteriores no duraban | Darle la razón: solo el tiempo lo demostrará | Cargarle la cesta sin decir nada | «Yo sí voy a durar» |
| **Miku** · Biblioteca | Habla un minuto entero de lo que ama y después pide perdón | Hacerle una pregunta concreta para que siga | Decirle que se le da bien | «Lo de la sal no entra en el examen» |
| **Yotsuba** · Pista de atletismo | Cree que solo sirve para correr y animar a sus hermanas | No tomar el cronómetro; volver a lo que dijo | Tomar el cronómetro | «Si correr es lo tuyo, concéntrate en eso» |
| **Itsuki** · Aula, después de clases | La única que estudia y aun así va mal; no pedirá ayuda | Señalarle dónde mirar, solo eso | Revisarlo juntos desde el principio | Quitarle el cuaderno y resolverlo |

El romance en este capítulo es solo una reacción ambigua en las ramas cálidas.

---

## 4. Los beats fijos

No dan puntos. Dan presencia a las cinco aunque nadie las busque.

- **Beat Itsuki** (azotea): tregua a medias; Itsuki no admite que la nueva rutina
  también la afecta a ella.
- **Beat crisis de Nino** (cocina): Nino quiere el despido del tutor y Maruo
  decide. Aquí se lee `desaires_cap1` (ver §5). Guarda su propia rama en
  `nino_rama_beat`, que no toca los desaires.
- **Beat casa:** la noche antes del examen con Raiha e Isanari, con el collage de
  pensamientos de las hermanas visitadas.

---

## 5. Desaires, despido y clima

Dos frías en el capítulo son el despido. Lo que cambia es cuándo:

| Situación | Resultado |
|---|---|
| 2 frías en los hubs 1 y 2 | **Variante A:** despido en el beat de Nino (`despido_en_beat`) |
| 1 fría antes del beat | Ultimátum de Maruo (`maruo_ultimatum`) |
| Ultimátum + otra fría en el hub 3 | **Variante B:** despido al cierre del hub 3 (`despido_cap1`) |
| 0 o 1 fría en total | Sigue al Evento 6 |

El **clima** del capítulo (`clima_cap1`) se decide una vez, en las
interconexiones: **buena** sin frías y con al menos dos cálidas, **mala** con
despido, **mixta** en todo lo demás. Colorea las interconexiones finales y, con el
ultimátum, fija el **estado de entrada** del Evento 6:

| Estado de entrada | Cuándo |
|---|---|
| `superado` | Sobrevivió al ultimátum |
| `bueno` | Clima buena |
| `mixto` | Clima mixta sin ultimátum |

---

## 6. Evento 6 — semana de exámenes

El cierre del capítulo. Un solo archivo, doce movimientos; cada uno es un `label`
de nivel superior que termina en `return`.

| Mov. | Contenido |
|---|---|
| 1 | Lunes en el aula, según el estado de entrada |
| 2–6 | Un día por hermana, en orden de examen: Yotsuba (japonés), Ichika (matemáticas), Nino (inglés), Itsuki (ciencias), Miku (sociales) |
| 7 | Después del examen: las cinco cuentan lo que hicieron distinto, sin saber las notas |
| 8 | Resultados y Maruo |
| 9 | Las cinco: ecos de cada hermana, la mesa y la foto del grupo |
| 10 | Casa |
| 11 | Cuarto, chat del grupo y libreta |
| 12 | El retrato: epílogo que responde a la escena 1 del prólogo |

**Cada día de hermana** (`e6_bloque`) se arma con piezas según su estado (cálida,
tibia, fría o no visitada): núcleo común, monólogo, **minijuego solo si fue
cálida**, promesa si no fue visitada y gesto final.

**Notas.** Todas aprueban, siempre. Cada una saca 100 en su materia y entre 60 y
89 en las demás, según su estado y el estado de entrada. El boletín
(`12_e6_pantallas.rpy`) solo muestra notas, nunca afinidad.

**Minijuegos** (detalle en `docs/MINIJUEGOS/`):

| Hermana | Minijuego |
|---|---|
| Yotsuba | Relevo de las cinco |
| Ichika | La máscara se cansa |
| Nino | Compras para seis |
| Itsuki | Cadena de conversiones |
| Miku | El compás (sincronizado con `miku_tema`) |

La dificultad base es media si el jugador fue cálido con Nino en su beat y difícil
si no. Se pueden saltar. En Extras se repiten, y el selector de dificultad aparece
solo si alguna vez fue cálido con Nino en su beat.

**Chat del grupo** (`15_chat_grupo.rpy`): debuta cuando Yotsuba crea el grupo,
reaparece con una decisión de qué escribir y cierra completo en el Evento 6. Miku
escribe sin «...» solo si fue cálida.

**Cierre:** cortinilla de fin → barra de progreso de las chicas (% = puntos × 10)
→ rol de créditos → «Continuará» → menú principal. Marca
`persistent.cap1_completado`.

---

## 7. Lo que el Capítulo 1 deja para el 2

Variables que el Capítulo 2 puede leer:

| Variable | Qué guarda |
|---|---|
| `puntos_*`, `primera_conexion` | Afinidad acumulada y desempate |
| `<h>_rama_cap1`, `<h>_visitada_cap1` | Cómo terminó cada evento de hermana |
| `nino_rama_beat` | Cómo terminó el beat de Nino |
| `clima_cap1`, `e6_estado_entrada` | Cómo salió el capítulo en conjunto |
| `e6_promesas` | Hermanas no visitadas a las que el protagonista les prometió algo |
| `e6_disculpa_pendiente` | La disculpa con Itsuki queda pendiente y anotada |
| `e6_domingo`, `e6_domingo_hermana` | El único menú del epílogo: qué hace con su primer domingo libre (`raiha`, `grupo`, `promesa` con una hermana, `dormir`). Sin puntos |

Ganchos narrativos sembrados a propósito:

- La tarjeta de receta de Nino es de su madre (aquí solo se insinúa).
- El vínculo de Raiha con Yotsuba; Raiha conoce a las quintillizas en la apertura del Capítulo 2.
- Maruo empieza a volver a casa.
- La disculpa del protagonista con Itsuki.
- Pendientes de cada hermana para el Capítulo 2: el talento matemático y la obra de Ichika, la moda de Nino, el club de atletismo de Yotsuba y el lado glotón de Itsuki.

**Dirección del Capítulo 2:** vida cotidiana, no exámenes. Los hubs son citas con
las hermanas. Cuando exista, el rol de créditos del Capítulo 1 debe saltar a
`cap2_inicio`.

---

## 8. Arte del capítulo

Cerrado: no se añaden CG. Los CG están en `images/cg/` (`cap1_apertura/`,
`cap1_hubs/`, `cap1_beats/`, `cap1_mov6/`, `cap1_final_malo/`) y la Galería
(`GALERIA` en `08_extras.rpy`) los agrupa por capítulo y por hermana. Los fondos
nuevos del capítulo están en `bg/cap1_hubs/` y `bg/cap1_beats/`.
