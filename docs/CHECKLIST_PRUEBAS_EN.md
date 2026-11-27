# Checklist de pruebas · inglés (v1.1)

Tareas E1/E2 del plan. Se juega todo en **English**; cada punto se marca al terminarlo.
El texto ya pasó por `tools/revisar_traduccion.py` (0 avisos) y por lint: aquí se busca lo que una máquina
no ve, como el tono, que el texto quepa, texto en español que se cuele o una rama que se rompa.

---

## 0. Preparación

- [✅] Abrir el juego **desde el launcher de Ren'Py** (la consola solo funciona así, no en las builds de itch).
- [✅] Opciones → **LANGUAGE** → English.
- [✅] Revisor y lint antes de empezar: `python tools/revisar_traduccion.py` (debe decir 0 avisos).

**Consola:** `Shift+O`. Acepta `jump <label>`, `save <slot>`, `load <slot>` y Python con `$` (varias órdenes en una
línea, separadas por `;`). `Esc` la cierra. Para los `jump`, lo más seguro es empezar una partida nueva y abrir la
consola en el primer diálogo. Una etiqueta que termina en `return` sin nada debajo vuelve al menú principal.

**Ojo al saltar texto (Ctrl / Skip):** Ren'Py marca como «visto» lo que ya leíste **en español**, así que el salto
también pasa por encima de eso. Úsalo solo en tramos que ya revisaste en inglés.

**En cada pantalla, mirar siempre:**
1. Texto en español que se cuela (diálogo, botón, rótulo, burbuja, notificación).
2. Texto que no cabe: más de 2 líneas en la caja, palabras cortadas en botones o tarjetas, texto encima de otro.
3. Etiquetas que se ven tal cual: `[mc]`, `{i}`, `{color=…}`, `\n`, `%s`.
4. Tono: la voz de cada personaje según el glosario (§6), y que la rama fría no suene cruel.

**Cómo reportar** (una línea por fallo): `ID · pantalla o escena · texto que sale · qué esperabas`.
Captura: tecla **S** (queda como `screenshot0001.png` en la carpeta del proyecto).

**Ranuras de guardado sugeridas** (página 1):

| Ranura | Momento |
|---|---|
| 1 | Mapa de la tarde 1 (después de la apertura) |
| 2 | Justo antes de «TIME TO DECIDE» del evento que estés jugando |
| 3 | Antes del menú del sábado (interconexión 6) |
| 4 | Antes de la decisión de la tarde 3 de la ruta B |
| 5 | Antes del menú del domingo (Evento 6) |

---

## 1. Prólogo y apertura (partida nueva)

- [✅] **P1 · Aviso inicial:** consola `$ persistent.aviso_visto = False` y `jump splashscreen`. Texto y botones.
- [✅] **P2 · Nombre:** pantalla del nombre («Keep "Futaro" if you'd rather…»). Primera pasada con **Futaro**.
- [✅] **P3 · Prólogo completo.** Guardar antes de cada menú y probar todas las opciones:
  - Motivo: «The money. No frills.» · «Raiha's face.» · «The habit of not giving up.»
  - Primera clase: «Notes out. I owe her no conversation.» · «Explain why I was so curt.»
  - Por qué das clases: «Because it pays.» · «Because I finish every problem.» · «Say nothing. Pick up the notebooks.»
- [✅] **P4 · Cortinillas:** «End of Prologue» y la de inicio del Capítulo 1.
- [✅] **P5 · Apertura:** el juego de adivinar con las pistas de color (rehearsal room, shopping mall, library, track,
  empty classroom), el chiste de pronunciación de Nino («Had to. Not "hah-doh too."») y sus menús
  («Wonder what changed overnight.» · «Welcome the silence.» · «Ask to change the subject.»).
- [✅] **P6 · Interconexión 1 → mapa de la tarde 1:** cortinilla («AFTERNOON 1 OF 3», «Free Afternoon», «Almost four weeks left»),
  HUD y nombres de los lugares en el mapa. **Guardar en la ranura 1.**

---

## 2. Los 5 eventos en sus 3 ramas

Las tarjetas de decisión salen **en orden aleatorio**: elige por el texto. En cada evento, guarda (ranura 2) justo
antes de «TIME TO DECIDE», juega una rama hasta la animación de tarde completada (sello WARM/LUKEWARM/COLD en el mapa),
carga y repite con las otras dos. Mira también la tarjeta (título, motivo, que el texto quepa en la tarjeta).

| Hermana · lugar | Cálida | Tibia | Fría |
|---|---|---|---|
| Ichika · Rehearsal Room | Don't play along. Wait for her to speak. | Play along. She's had enough for today. | If you have the energy to make jokes, you have the energy to study. |
| Nino · Shopping Mall | You're right not to trust me. Only time will prove it. | Carry her basket without a word. | I'm going to last. |
| Miku · Library | Ask her how long the salt took to arrive. | Tell her she's good at this. It's true. | The salt stuff isn't on the exam. |
| Yotsuba · Track | Don't take it yet. Go back to what she said. | Sure, hand it over. | If running is your thing, focus on that. |
| Itsuki · Empty Classroom | Just point out where to look. | Want to go over it from the beginning? | Take the notebook, solve it. Save her the afternoon. |

Se cubren las 15 en dos rutas que salen de la ranura 1:

**Ruta A: Ichika → Nino (acaba en el despido A)**
- [ ✅] **H-ICH-C** · [ ✅] **H-ICH-T** · [ ✅] **H-ICH-F**: tarde 1, Ichika. Seguir con **fría**.
- [✅ ] **I2 · Interconexiones 2 y 3:** menú del desayuno («Anything but curry.» · «Tupperware coffee. Done.» ·
  «Nothing. I'm running on eye bags.») y beat de Itsuki en la azotea (sus 3 opciones: «…hauling my books to the bathroom.» ·
  «…neither of us will admit we're tired.» · «Nothing. I just want this hour to end.»).
- [ ✅] **H-NIN-C** · [✅ ] **H-NIN-T** · [✅ ] **H-NIN-F**: tarde 2, Nino. Seguir con **fría**.
- [✅ ] **I4 · Interconexión 4:** menú del paseo («I've gotten used to sleeping four hours.» · «Whether all five have a group chat
  about me.» · «Nothing. I just walk.») y **CH1 · chat de estreno**: «Team Quintuplets + Tutor!», Nino fuera del grupo y el
  contador de miembros.
- [ ✅] **FA · Despido variante A:** beat de Nino en la cocina → Maruo despide → casa con Raiha e Isanari → tarjeta gris de final.

**Ruta B: Itsuki → Miku → Yotsuba (despido B y, desde la misma partida, el Evento 6 real)**
- [ ✅] **H-ITS-C** · [ ] **H-ITS-T** · [ ] **H-ITS-F**: tarde 1, Itsuki. Seguir con **fría** (ultimátum de Maruo).
- [ ✅] **H-MIK-C** · [ ] **H-MIK-T** · [ ] **H-MIK-F**: tarde 2, Miku. Seguir con **cálida**.
- [ ✅] **BN · Beat de Nino con ultimátum:** guardar antes de su menú y probar las 3 ramas
  («And who picks up yours?» · «Say nothing. Take her cup to the sink.» · «Then stop picking up everyone else's pieces…»).
- [ ✅] **I5 · Interconexión 5:** el sobre del banco («Read it twice, in case it magically changed.» · «Count the days left on
  my fingers.» · «Pretend I don't care.»).
- [ ✅] **H-YOT-C** · [ ] **H-YOT-T** · [ ] **H-YOT-F**: tarde 3, Yotsuba. **Guardar en la ranura 4** antes de decidir.
- [ ✅] **FB · Despido variante B:** cargar la ranura 4 y elegir Yotsuba **fría** → interconexión 6 (clima «mala») → beat de la casa
  con la duda de Futaro → despedida de las cuatro → tarjeta gris.
- [✅ ] Cargar la ranura 4 otra vez, elegir Yotsuba **cálida** y seguir:
  - [✅ ] **CH2 · Interconexión 6:** historial del chat de la semana y menú del sábado. Guardar en la ranura 3 y probar los 3
    mensajes («"Sleep well. It's not the end of the world."» · «"I trust you five. Whatever happens Monday."» ·
    «"If it goes wrong, blame me. That's what I'm paid for."»). Cada uno cambia las respuestas del chat. El clima «buena»
    no sale en estas rutas: se ve en **C1**.
  - [ ✅] **BC · Beat de la casa:** collage de pensamientos de las hermanas visitadas y «Shut the notebook.».
  - [ ✅] Evento 6 (sección 4, corrida **R**).

---

## 3. Final malo

- [ ✅] **FM1 · Tarjetas de final** de A y B (en gris, sin sonido).
- [✅ ] **FM2 · Extras → Endings:** «Early Dismissal», «The Slammed Door» (A) y «The Farewell» (B) desbloqueados, con sus
  pistas. Las pistas de las cinco hermanas y la de «Secret Ending» caben en 2 líneas.

**Cobertura extra (opcional, para E2).** Los dos finales malos cambian según la rama de cada hermana visitada. Las rutas A y B
cubren Ichika y Nino fría (A), e Itsuki fría, Miku cálida y Yotsuba fría (B). El resto se prepara desde la consola. Pega la línea
entera, cambia los valores y después `jump final_malo_temprano`:

```
$ ichika_rama_cap1 = None; nino_rama_cap1 = None; miku_rama_cap1 = "fria"; yotsuba_rama_cap1 = "fria"; itsuki_rama_cap1 = None; hub_visitadas = ["yotsuba", "miku"]; despido_en_beat = True
```

| ID | Variante | Ramas (en el orden de `hub_visitadas`) | `despido_en_beat` |
|---|---|---|---|
| [ ✅] FA2 | A | Yotsuba fría, Miku fría | True |
| [✅ ] FA3 | A | Itsuki fría, Nino fría | True |
| [✅ ] FB2 | B | Ichika fría, Yotsuba cálida, Miku fría | False |
| [ ✅] FB3 | B | Nino fría, Itsuki cálida, Yotsuba fría | False |
| [✅ ] FB4 | B | Ichika cálida, Nino fría, Miku fría | False |
| [ ✅] FB5 | B | Ichika tibia, Nino fría, Yotsuba fría | False |
| [ ✅] FB6 | B | Ichika fría, Miku tibia, Yotsuba fría | False |

Las hermanas que no aparecen en la fila van en `None`.

---

## 4. Evento 6 (semana de exámenes)

**Corrida R (real):** sale de la ruta B. Entrada «superado», con Itsuki fría, Miku cálida, Yotsuba cálida, Ichika y Nino sin
visitar. Es la única forma de ver la pieza de Itsuki «ayudada» (Itsuki en la tarde 1).

**Corridas D1–D5 (debug):** consola `jump e6_debug` → «Editar ramas a mano…» (toca cada hermana hasta su estado) →
«Listo (validar)» → «Ajustes…» para el beat de Nino → «>> Jugar Evento 6». El menú de debug está en español a propósito
(solo es para desarrollo). La entrada sale sola según el orden.

| Corrida | Ichika | Nino | Miku | Yotsuba | Itsuki | Beat de Nino | Entrada |
|---|---|---|---|---|---|---|---|
| [✅ ] R | — | — | cálida | cálida | fría | lo que elegiste | superado |
| [ ✅] D1 | cálida | cálida | tibia | — | — | tibia | bueno |
| [ ✅] D2 | — | tibia | — | fría | cálida | cálida | superado |
| [ ✅] D3 | tibia | cálida | fría | — | — | fría | mixto |
| [ ✅] D4 | fría | — | — | tibia | tibia | tibia | superado |
| [✅ ] D5 | — | fría | tibia | — | cálida | tibia | superado |

`—` = no visitada. Entre todas cubren los 4 estados de cada hermana, las 3 entradas, los 3 beats de Nino, los 5 minijuegos
(solo salen con la hermana cálida), el chat nocturno con Miku cálida y sin ella, e Itsuki «ayudada» y «sola».
En R se lee todo. En D1–D5, el núcleo común de cada día se puede pasar rápido: hay que leer con calma el monólogo, la
promesa (hermanas no visitadas, `[e6_p1]`/`[e6_p2]`), el gesto, la tarde, la puerta de Nino y los ecos.

En cada corrida, mirar:
- [✅ ] **E6-HUD:** «Exam Week», «Classroom · Japanese / Math / English / Science / Social Studies», «five exams left» … «one exam left»
  y «Classroom · Friday Afternoon» (el rótulo más largo: que quepa).
- [ ✅] **E6-VOCES:** voces interiores (Itsuki sin contracciones, Miku con «...»), el profesor («Nakano. Wake up.»).
- [ ✅] **E6-BOLETIN:** boletín animado «THE TALLY» con las cinco materias, en los resultados con Maruo.
- [ ✅] **E6-FOTO:** «Say "five"!» → «Five!!».
- [✅ ] **E6-DOMINGO:** guardar en la ranura 5 y probar las 4 opciones («Take Raiha somewhere.» · «Answer the group.» ·
  «Keep a promise.» · «Sleep in. Just this once.»). «Keep a promise.» abre un submenú con las dos promesas
  (`[e6_p1]` / `[e6_p2]`, las hermanas no visitadas).
- [ ✅] **E6-CHAT:** chat de la noche (cambia con Miku cálida o no).
- [ ✅] **E6-CIERRE:** libreta, retrato, tarjeta de fin del capítulo, barra de progreso, créditos y «To be continued...».

---

## 5. Los 5 minijuegos

Desde **Extras → minijuegos** (siempre abiertos), cada uno en **Hard / Medium / Assisted**, y una vez dentro del Evento 6.
Atajos de consola: `jump mj_probar_i1` (Ichika) · `mj_probar_n1` (Nino) · `mj_probar_m3` (Miku) · `mj_probar_y2` (Yotsuba) ·
`mj_probar_it1` (Itsuki) · `mj_transicion_prueba` (entradas y salidas de los cinco).

En cada uno: tarjeta de título, reglas, textos durante el juego, burbujas del chibi y salida al ganar. Además, **perder a propósito
una vez** para ver las opciones de fallo («Try again» · «Skip it» · «Let her do it»).

- [ ✅] **MJ-ICH · The Mask Grows Tired:** medidor («An honest line lowers it», «IT CAN ONLY BE HONEST»), porcentajes con espacio («100 %»).
- [✅ ] **MJ-NIN · Shopping for Six:** productos en inglés con nota en **romaji** («hachimitsu»…), lista de la compra y reglas.
- [ ✅] **MJ-MIK · The Beat:** «Perfect / Good / Early / Late / Miss», «COMBO», «PERFECTS».
- [✅ ] **MJ-YOT · Quintuplet Relay:** reglas del relevo («THE QUINTUPLET RELAY», el testigo = «baton») y textos de cada tramo.
- [ ✅] **MJ-ITS · Conversion Chain:** conversiones de unidades, números en formato inglés (**1,000** y **1.5**) y la nota de la calculadora.

---

## 6. Chat de grupo, boletín, barra de progreso, créditos y «Continuará»

- [✅ ] **C1 · Chat:** además de CH1, CH2 y E6-CHAT, `jump chat_grupo_prueba` recorre todos los chats seguidos. La narración de esa
  etiqueta de prueba está en español a propósito; solo se revisan las burbujas.
- [✅ ] **C2 · Boletín:** `jump boletin_cinco_prueba` (misma nota: la narración de prueba va en español).
- [ ✅] **C3 · Barra de progreso:** `jump progreso_chicas_prueba`. Nombres, porcentajes y los retratos (Yotsuba e Itsuki al mismo
  tamaño que sus hermanas desde el 26/11).
- [ ✅] **C4 · Créditos y «Continuará»:** `$ persistent.creditos_vistos = False` y `jump cap1_continuara` (el rol sin poder saltar, y luego
  «To be continued...» y su menú). El texto coincide con la sección inglesa de `CREDITOS.md`, sin Gemini ni ChatGPT.
- [ ✅] **C5 · Cortinillas y animaciones:** `jump cortinilla_prueba` (todas las tarjetas) y `jump hub_completado_prueba` (sellos de tarde completada).

---

## 7. Menús y extras

- [✅ ] **M1 · Menú principal** y su bloque de «Who will you choose?».
- [ ✅] **M2 · Opciones:** DISPLAY, SKIP, SOUND, MUSIC, SOUND EFFECTS, TEXT SPEED, AUTO-FORWARD, LANGUAGE, Reset («Defaults restored»).
- [ ✅] **M3 · Cambio de idioma en mitad de una escena**, en las dos direcciones: el diálogo actual y el HUD cambian.
- [ ✅] **M4 · Una partida guardada en español carga bien en inglés**, y al revés.
- [ ✅] **M5 · Guardar/Cargar:** páginas AUTOSAVES y QUICK SAVES (letras A y Q), «Empty», fechas en formato de EE. UU. (**11/26/2026 · 20:13**),
  nombre del capítulo en la ranura («Prologue», «Chapter 1»).
- [✅ ] **M6 · Confirmaciones:** sobrescribir, borrar, cargar, volver al menú y salir.
- [ ✅] **M7 · Menú rápido, historial y notificaciones** (guardado rápido, modo salto, auto).
- [ ✅] **M8 · Ayuda:** teclas y ratón (las teclas Re Pág/Av Pág cruzadas son una errata del español anotada en ERRATAS_ES).
- [ ✅] **M9 · Acerca de:** créditos con enlaces y «Version …».
- [ ✅] **M10 · Extras → Gallery:** títulos de los CG y «CGs UNLOCKED».
- [ ✅] **M11 · Extras → animaciones:** tarjetas de capítulo y tarde, encuentros, tardes Warm/Lukewarm/Cold, entradas y salidas de los
  minijuegos, «Time to Decide», cierre, «End of Prologue» (cabe en su tarjeta).
- [✅ ] **M12 · Extras → repetir secciones:** PROLOGUE, CHAPTER 01 y la semana («Replay a section. Your saves won't change.»).

---

## 8. Android (pantalla pequeña)

Simulación en el PC (PowerShell; la variable solo dura en esa ventana):

```powershell
$env:RENPY_VARIANT = "small touch mobile android"
& "C:\Users\PERSONAL\Desktop\renpy-8.5.3-sdk\renpy.exe" "C:\Users\PERSONAL\Desktop\The_Fifth_Choice\The Fifth Choice"
```

Con esa variante la letra del diálogo pasa de 34 a 42 px. La línea inglesa más larga tiene 100 caracteres y la española más
larga 126, así que el riesgo está en los nombres largos, no en el diálogo con «Futaro».

- [✅ ] **A1 · Nombre de 16 caracteres** (el máximo, p. ej. «Maximilian-Josef») y jugar el prólogo: las líneas con `[mc]` siguen en 2 líneas.
  La más larga sin nombre está al principio del prólogo: «On the couch, a third girl—same face, again—was reading…».
- [✅ ] **A2 · Botones de opción y tarjetas de decisión** (las tarjetas crecen hasta 5 líneas). Las opciones más largas son la fría
  del beat de Nino («Then stop picking up everyone else's pieces and take care of your own.») y la fría de Ichika.
- [✅ ] **A3 · HUD:** «Classroom · Friday Afternoon» y «[tiempo] left».
- [✅ ] **A4 · Mapa de tardes, chat, boletín y barra de progreso.**
- [ ✅] **A5 · Reglas de los 5 minijuegos** y sus botones táctiles.
- [✅ ] **A6 · Guardar/Cargar** (fechas) y **Opciones → LANGUAGE.**
- [✅ ] **A7 · Créditos y «To be continued...».**
- [ ✅] **A8 · En un teléfono real** con la APK de F1: prólogo hasta el primer menú, una tarjeta de decisión y un minijuego.

---

## 9. Cierre (E2)

- [✅] Todo lo reportado, corregido.
- [✅] `python tools/revisar_traduccion.py` → 0 avisos.
- [✅] Lint de Ren'Py sin errores y con los mismos bloques en el juego y en la traducción.
- [✅] Progreso actualizado en `docs/PLAN_TRADUCCION_Y_ENCUESTA.md`, commit y push.
