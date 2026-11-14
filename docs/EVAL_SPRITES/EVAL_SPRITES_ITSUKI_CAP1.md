# Evaluación de sprites · Itsuki · Prólogo + Capítulo 1

> Revisado sobre el árbol de trabajo actual (commit `19d226e`, con cambios sin commitear en otros archivos).
> Es una evaluación: no se tocó ningún `.rpy`. Los números de línea son los de hoy.
> **Estado (14/11/2026):** el 🎨 del §7 está aplicado. `itsuki_sonriendo.png` es el render nuevo con las manos a la espalda, normalizado a 760×930. Antes de normalizar se bajó el ahoge 14 px, comprimiendo en vertical las filas 8–70 del original, porque el lienzo lo cortaba. La copia retocada está en `herramientas/itsuki_sonriendo_ahoge.png`. No hizo falta tocar ningún `.rpy`. Los 11 🔁 del §8 (13 sentencias) están aplicados tal cual, y el Lint sale limpio.
> Fuentes: `docs/GUIA_ARTE.md` §1, §2, §3, §6 y §9 · `docs/GUIA_RENPY.md` §1 («Las expresiones son atributos») y §2 (la regla del `show`) ·
> `docs/REVISION_PERSONAJES_CAP1/REVISION_ITSUKI_CAP1.md` (manda sobre cualquier propuesta) ·
> `docs/EVAL_SPRITES/EVAL_SPRITES_NINO_CAP1.md` y `EVAL_SPRITES_MIKU_CAP1.md` (formato y criterios) · los siete `.rpy` del recorrido ·
> `10_mj_itsuki.rpy` y `12_e6_pantallas.rpy` para el E6.

---

## 0. Avisos: dónde el encargo y los archivos no dicen lo mismo (mandan los archivos)

| # | El encargo dice | Los archivos dicen | Qué hice |
|---|---|---|---|
| 1 | E6: 0 shows, 125 líneas | Es literal: `02_cap1_evento6.rpy` no tiene ningún `show itsuki`. Pero la pinta con **25** `call e6_foco("itsuki", …)`, **2** `call e6_formacion_neutral` (l. 259 y 2178) y **1** `call e6_entrar(e6_h)` (l. 3286). Las 125 líneas son **63** `itsuki` + **62** `itsuki_int`. | Evalué los 28. Diagnóstico en §3. |
| 2 | «SONRIENDO: hoy solo aparece en el prólogo; en todo el Cap. 1 no sonríe nunca» | Solo es cierto para los `show`. **El E6 la pone en `sonriendo` cuatro veces:** lunes cálida/fría (l. 417, revisión P4), «Apoyo la idea» (l. 2373), eco cálida (l. 3587) y los boletines (l. 3983). | La pregunta (e) la contesto para todo lo anterior al E6 (§6). |
| 3 | 128 shows, neutral 50 · molesta 44 | Cuadra: hay **128** `show itsuki`. **105** llevan atributo (neutral 50 · molesta 44 · timida 6 · sorprendida 4 · sonriendo 1) y **23** son de solo tinte (`show itsuki at pj_calla(…)`). | Uso esas cifras. Los de tinte van dentro del momento que los contiene. |
| 4 | LoRA de serie ≤0.3 y LoRA individual 0.7–0.8 | `GUIA_ARTE.md` §1, «Pesos de LoRA»: sprite individual de una hermana → **sin LoRA de serie** y personaje a **0.8**. El 0.3 / 0.7–0.8 es para un **CG** individual. Igual que en el aviso 5 de Nino. | El prompt del §7 va sin LoRA de serie y con el de Itsuki a 0.8. |
| 5 | Horquillas de estrella doradas · ahoge | §2: «pasadores de estrella amarilla, un ahoge». Los cinco PNG llevan estrellas amarillas. §6 avisa de que `one strand of hair sticking up` genera **dos** ahoges. | En el prompt van `yellow star hair clips` y la etiqueta `ahoge` sola, sin la frase. Hay que revisar que salga uno. |
| 6 | El lado glotón no justifica caras en el Cap. 1 | El beat ya lleva aplicada la N1 de la revisión (el almuerzo de Raiha, l. 244–274), con `sorprendida` y `timida`. | Esas dos caras las justifico por la vergüenza de que la pillen, no por la comida. |

---

## 1. Ficha de los 5 sprites

Los cinco son PNG RGBA de 760×930 (comprobado en la cabecera de cada archivo).

| Sprite | Pose y brazos | Mirada | Boca | Lo que transmite de verdad | Lo que NO cubre |
|---|---|---|---|---|---|
| `itsuki neutral` | De frente, recta. **Brazos colgando** un poco separados del cuerpo, con las manos sueltas a la altura del bajo de la falda. | De frente, párpados algo caídos, tranquila. | Cerrada, una línea corta. Rubor leve. | Calma, compostura, reserva. Por el texto sirve para la firmeza formal: la cara no es dura, pero tampoco se ablanda. | Enojo, alegría, vergüenza. Tampoco una frialdad dura: la cara es suave. |
| `itsuki molesta` | **Brazos cruzados** altos sobre el pecho. | Cejas fruncidas, mira de frente, fija. | Mohín hacia abajo. Rubor. | Indignación, pique, reproche. De lejos, los brazos cruzados se leen como «cerrada»; de cerca, el mohín se lee como enfado. | Calma, tristeza, preocupación. No vale para la firmeza tranquila: el mohín la hace emocional. |
| `itsuki timida` | **Manos juntas abajo, delante de la falda**, con los brazos en V. Hombros hacia dentro y cabeza un poco gacha. | Párpados entornados, mirada baja. | **Sonrisa cerrada.** **Rubor fuerte.** | Vergüenza de que la pillen, el cumplido que no sabe recibir, la ternura que se le escapa. | Vergüenza sin sonrisa (cuando se avergüenza de sí misma), tristeza, firmeza. |
| `itsuki sorprendida` | **Puño derecho en el cuello de la camisa**; brazo izquierdo separado hacia atrás. El pelo se abre. | Ojos muy abiertos. | **Abierta.** Rubor. | Sobresalto, el «¡¿Eh?!» indignado. | Calma y todo lo contenido. |
| `itsuki sonriendo` | **Brazos colgando**, con las manos pellizcando el bajo de la falda a los lados. Cabeza ladeada. | Ojos suaves, de frente. | Sonrisa cerrada. Rubor. | Amabilidad cortés, contento tranquilo. | Euforia, risa, firmeza. Es el único render con el faldón de la camisa asomando bajo el chaleco. |

**Regla de §9 (a un 30 % solo se lee la silueta):**

- **`neutral` ↔ `molesta`: se distinguen bien ✓.** Brazos colgando contra brazos cruzados: es el mejor contraste del set. Una consecuencia: a distancia, `molesta` se lee como «cerrada» antes que como «enfadada», y el enfado solo aparece de cerca, en el mohín. Por eso cada `molesta` tiene que ser enojo de verdad. Si es firmeza, el jugador que la mira de cerca ve un enfado que el texto no dice (§2, C2).
- **`neutral` ↔ `sonriendo`: es el par peligroso.** Tienen la misma silueta: brazos abajo y un poco separados, manos a la altura del bajo de la falda. Las separan la cabeza ladeada, la sonrisa y unos dedos en la tela: todo detalle de cara, que a un 30 % no se lee. En pantalla, el paso de una a otra casi no se ve. Pasa en los cinco usos de `sonriendo`, y tres son con las cinco en formación (E6 l. 417, 2373 y 3983). De ahí sale el 🎨 del §7.
- **`neutral` ↔ `timida`:** se distinguen por dónde acaban las manos (a los lados o juntas en el centro, en V). Se lee bien a solas (x = 0.5) y peor en grupo (`X_ITSUKI` = 0.90), pero en grupo `timida` solo sale en la mesa del E6 (l. 3830 y 3838), hablando y resaltada.
- **`sorprendida` ↔ el resto:** es la única asimétrica y con una mano a la altura del pecho. Se distingue ✓.
- **No falta ninguna emoción que se repita.** La frialdad dura (fría, final malo) la cubre `neutral` por el texto, que es lo que pide el encargo. Ninguna otra emoción se repite en varias escenas: no hay ➕.

---

## 2. Criterios aplicados (los de Nino y Miku, adaptados a Itsuki)

- **C1 · La narración manda.** Si el narrador describe postura, mirada o tono, va el sprite que lo cumple: «se cruzó de brazos» → `molesta`; «sin la hostilidad de siempre», «sin discutirlo», «ni me mira» → **no** `molesta`; «rojas las orejas», «sin mirarme» → `timida`.
- **C2 · La firmeza no es enojo.** Organizar, informar, corregir, poner nota, despedir con frialdad → `neutral`. `molesta` solo cuando hay pique, indignación o reproche dirigido a alguien, y el texto lo respalda. Es la distinción que pide el encargo y la que más cambios da.
- **C3 · Cortarse sola o que la pillen.** Es el criterio de Nino. Si se corta sola con un «olvídalo» y nadie la ha pillado, está molesta consigo misma → `molesta`. Si la pilla otro (el MC, una hermana) o le llega un cumplido → `timida`. Volver a la armadura en la réplica siguiente es parte del gesto y no cuenta como parpadeo.
- **C4 · La revisión manda.** Se respetan tal cual P4 (lunes del E6), P5 (propuesta del juego: neutral → molesta), P6 (el nombre en la cálida), N1 (azotea: sorprendida → timida → neutral), N4 (timida) y N5 (eco cálido). **P1 solo cambió el texto del beat** y copió el `show itsuki molesta` que ya había en las tres variantes: no es una decisión de cara.
- **C5 · Parpadeo.** Nada de A → B → A en réplicas seguidas, ni cambios de cara sin una línea que los motive. Se arregla cambiando el atributo por el del vecino, y entonces el `show` siguiente no cambia nada en pantalla. Ningún `show` se borra.
- **C6 · Ramas.** En el mismo punto del guion, cálida, tibia y fría llevan caras distintas siempre que el texto lo permita.
- **C7 · La sonrisa es un hito, como el nombre.** La revisión (§1) dice que el nombre «lo usó cuando era amable y lo perdió en cuanto él la rechazó». Con la sonrisa pasa lo mismo: `sonriendo` sale en el prólogo antes del «No» y no vuelve hasta el E6. Entre medias, la calidez de la cálida va en `timida`, que ya tiene sonrisa cerrada.

Veredictos: ✅ queda bien · 🔁 cambiar a otra expresión existente · 🎨 rehacer el sprite · ➕ sprite nuevo.

---

## 3. Evento 6: diagnóstico (mismo caso que Miku)

**Conclusión: el diagnóstico de Miku vale igual para Itsuki, sin excepciones.** De las 125 líneas, las **57** `itsuki` dichas en escena tienen sprite por `e6_foco`. Las otras **68** (62 `itsuki_int` y 6 `itsuki`) van sobre un CG a propósito: un sprite taparía el CG. Es el mismo diseño de `e6_mostrar_foco` (l. 91), que guarda la última cara de cada hermana y la vuelve a pintar atenuada cuando habla otra.

| Tramo (etiqueta · líneas) | Líneas de Itsuki | Qué hay en pantalla | ¿Intencional o falta? |
|---|---|---|---|
| Lunes en el aula (`e6_lunes` · 415–439) | **9** `itsuki`: cálida/fría 5, tibia/no visitada 4 | `bg_aula` (l. 256), formación neutral (l. 259) y `e6_foco` l. 417 / 431 | Sprite ✓ |
| Núcleo de Ciencias (`e6_itsuki_nucleo` · 1507) | 0 | `bg_negro` (l. 1513) → **CG `cg_itsuki_examen`** (l. 1522) | — |
| Voz interior (`e6_itsuki_mono_<estado>` · 1573–1700) | **47** `itsuki_int`: cálida 15, tibia 11, fría 10, no visitada 11 | El mismo CG (la siguiente `scene` es la l. 1870) | Intencional: monólogo sobre su CG |
| Recuerdo de la azotea (`e6_itsuki_beat_ayudada` / `_sola` · 1547 / 1560, los llaman los monólogos) | **8** `itsuki_int` (4 + 4) | El mismo CG | Intencional |
| Minijuego It1 (`e6_itsuki_mj` · 1705) | **7** `itsuki_int` + **1** `itsuki` al profesor (l. 1728, «¿Podría repetir el enunciado de la cuatro? Entero.») | El CG. Durante el juego, la screen con su **chibi** (`mj_retrato("itsuki", …)`, `10_mj_itsuki.rpy` l. 492) | Intencional: minijuego con chibi propio |
| Promesa y gesto (`e6_itsuki_promesa` · 1757, `e6_itsuki_gesto_*` · 1778–1839) | 0 | El CG | — |
| Aula de la tarde, en grupo (`e6_despues`) | **2** `itsuki` (2323, 2375) | `bg_aula_tarde` (l. 2175), formación (l. 2178), `e6_foco` l. 2321 / 2373 | Sprite ✓ |
| Tarde por rama (`e6_itsuki_tarde_*` · 2750–2825) | **17** `itsuki`: cálida 8 (variante A 3 o B 4, más 1 común), tibia 3, fría 2, no visitada 4 | `e6_foco` l. 2752, 2772, 2785, 2800, 2813 | Sprite ✓ |
| La pregunta al MC (`e6_tarde_pregunta` · 2919) | **1** `itsuki` (2925), solo cálida | `e6_foco` l. 2923 | Sprite ✓ |
| Departamento y eco (`e6_cinco` · 3286, `e6_itsuki_eco_*` · 3581–3664) | **11** `itsuki`: cálida 4, tibia 2, fría 2, no visitada 3 | `bg_departamento` (l. 3258), entra neutral (`e6_entrar`, l. 3286), `e6_foco` l. 3587, 3616, 3635, 3643, 3654 | Sprite ✓ |
| La disculpa interrumpida (`e6_intento` · 3756) | **6** `itsuki` | `e6_foco` l. 3766 / 3794 | Sprite ✓ |
| Mesa (`e6_mesa` · 3810–4097) | **11** `itsuki` | `e6_foco` l. 3818, 3830, 3838, 3898, 3983, 4005, 4057, 4095 | Sprite ✓ |
| Foto (l. 4100–4170) | **5** `itsuki` (4131, 4147, 4151, 4157, 4169) | **CG `cg_cinco_aprobadas`** (l. 4104 / 4109 / 4114, según el tinte) | Intencional: CG de las cinco |
| Chat del grupo (`e6_cuarto`) | 0 líneas de diálogo. Sus mensajes son datos de la screen (`12_e6_pantallas.rpy` l. 222 y 224) | `bg_cuarto_mc` + screen | Intencional: interfaz |

Cuenta: 9 + 2 + 17 + 1 + 11 + 6 + 11 = **57** con sprite · 47 + 8 + 7 = **62** `itsuki_int` sobre CG · 1 + 5 = **6** `itsuki` sobre CG. Total, **125** ✓.

---

## 4. Líneas de Itsuki sin sprite fuera del E6

| Archivo · líneas | Qué hay en pantalla | ¿Intencional? |
|---|---|---|
| `01_prologo.rpy` 364 | CG `cg_itsuki_sentada` (l. 349) | Sí, es CG |
| `01_prologo.rpy` 833 | `bg_departamento`, antes de que entre: la voz llega tras el portazo (l. 829) y el CG empieza en la l. 837 | Sí, entra en escena |
| `01_prologo.rpy` 848–880 | CG `cg_itsuki_discusion` (l. 837) | Sí, es CG |
| `01_prologo.rpy` 515, 519, 521 (opción 2 de la azotea) | CG `cg_itsuki_azotea` (l. 510) | Sí, es CG |
| `01_prologo.rpy` 1168, 1172 | CG `cg_hermanas_estudiando` (l. 1131) | Sí, es CG |
| `02_cap1_beat_Itsuki.rpy` 173, 177 | CG `cg_itsuki_azotea_manos` (l. 156) | Sí, es CG |
| `02_cap1_conexiones.rpy` 3849 (clima buena), 3927 (clima mala) | `bg_departamento` / `bg_departamento_anochecer` (l. 3796 / 3801), **sin ninguna hermana** | La misma decisión de escena que en Miku: en esa despedida no hay sprite para ninguna de las cinco (§9) |

---

## 5. Tabla por archivo

Un momento es el `show` (o `e6_foco`) donde cambia la expresión, más las líneas de Itsuki que cubre. Los `show itsuki at …` de solo tinte, y los que repiten la misma cara, van en el momento que los contiene.

### 01_prologo.rpy (19 shows)

| archivo:línea | Rama / escena | Diálogo (resumido) | Actual | Veredicto | Propuesta | Por qué |
|---|---|---|---|---|---|---|
| 371 | Aula, le pide ayuda | «Escuché al profesor diciendo que tu examen fue de cien puntos» · «¿Podrías enseñarme un poco? Te lo agradecería mucho.» | sonriendo | 🎨 | sonriendo rehecho (§7) | La cara es la correcta: la Itsuki amable de antes del «No» (C7). El 🎨 es solo por la silueta (§1) |
| 386 | Aula, tras el «No» | «¡¿Eh?! ¡Ni siquiera te lo pensaste!» · «¡Solo te pido algo de orientación mientras almuerzo!» · «...» | sorprendida | ✅ | — | El sobresalto indignado |
| 403 | Aula | «Está bien. No te necesito.» · «…solo demostraste ser una persona arrogante y carente de empatía.» | molesta | ✅ | — | C1: l. 410 «apretó los dientes», l. 424 «sin ocultar su indignación». Enojo de verdad |
| 456 | Azotea, se abre la puerta | «...» · «¿Otra vez tú?» | sorprendida | ✅ | — | No esperaba encontrarlo |
| 465 | Azotea | «Ni se te ocurra pensar que te vine a buscar.» · «…a alejarme de gente desagradable.» | molesta | ✅ | — | Hostilidad abierta del primer día |
| 493 | Azotea · opción «Sacar los apuntes» | «...¿En serio vas a seguir estudiando…?» · «Qué persona tan agotadora.» · «No me extraña en lo absoluto.» | molesta | ✅ | — | Repite la cara de la 465. La opción 2 no tiene `show` y sigue en `molesta`: l. 508 «se cruzó de brazos» es el sprite (C1) |
| 901 (+905–984, tinte) | Departamento, con Ichika y luego las cinco | «¡Ichika, no te le acerques! Es el maleducado del asiento.» · «¡Te pedí un favor amablemente y me trataste como al ser más despreciable del mundo!» | molesta | ✅ | — | Indignación a gritos |
| 1055 | Coro «¡No pensamos estudiar!» | (línea de `quintillizas`) | molesta | ✅ | — | Bloque hostil del grupo |
| 1223 | Anochecer, la última | «...Esto no va a funcionar, ¿sabes?» · «¿Por qué aún no te rindes?» · opción 3: «...Entendido. Haz lo que quieras.» | neutral | ✅ | — | Pregunta en serio, sin enojo (C2). La opción 3 se queda en `neutral` y se distingue de las otras dos (C6) |
| 1245 | Opción «Porque me pagan» | «Qué actitud tan desagradable.» · «...Al menos eres honesto, por horrible que suene.» | molesta | ✅ | — | Reproche educado y cortante (revisión P13) |
| 1259 | Opción «Porque no dejo problemas sin resolver.» | «Mis hermanas y yo no somos un problema de matemáticas.» | molesta | ✅ | — | Se indigna por sus hermanas |

### 02_cap1_apertura.rpy (2 shows)

| archivo:línea | Rama / escena | Diálogo (resumido) | Actual | Veredicto | Propuesta | Por qué |
|---|---|---|---|---|---|---|
| 76 | Aula, él llega | (ninguna línea suya; el MC dice «Buenos días.») | neutral | ✅ | — | Sigue con su cuaderno |
| 81 | Aula | «...» · «Ya sé que vas a ir.» · «Mi padre nos dio tu horario anoche.» · «Avisa lo que quieras. Yo no pienso estudiar contigo.» | molesta | 🔁 | **neutral** | C1: l. 101 «Ni me mira», l. 115 «hoy ni siquiera se molesta en mirarme», l. 117 «Como si ya hubiera decidido que no valgo ni para enojarse». La revisión (§2, momento 5) lo llama «frialdad». `molesta` es el ceño mirando de frente: el enojo que el texto dice que ya no hay. Con `neutral`, el «...» es justo eso: no reacciona al saludo. La 76 y la 81 quedan iguales, y el `show` de la 81 no cambia nada |

### 02_cap1_Itsuki.rpy (20 shows · hub con ramas)

`itsuki_m4a` = cálida · `itsuki_m4b` = tibia · `itsuki_m4c` = fría. Hasta la l. 296 es común a las tres.

| archivo:línea | Rama / escena | Diálogo (resumido) | Actual | Veredicto | Propuesta | Por qué |
|---|---|---|---|---|---|---|
| 86 | Común, llegada | «¿Olvidaste algo?» · «Está en tu pupitre. Donde lo dejaste.» · «No te incumbe.» | neutral | ✅ | — | Firmeza seca (C2) |
| 120 | Común | «Me incumbe a mí. Tú te vas a las cuatro.» · «El tiempo que hace falta.» | molesta | 🔁 | **neutral** | C2: lo corrige y se cierra, sin enojo. l. 127 «No contestó a eso.» y l. 129 «Volvió a mirar el cuaderno como si la frase no se hubiera dicho.». C5: hoy va molesta (120) → neutral (145) → molesta (168) en tres réplicas. Con el cambio, la 145 no cambia nada y queda un solo salto, en la 168, donde sí hay golpe |
| 145 | Común | «El que haga falta, he dicho.» | neutral | ✅ | — | l. 150: lo repite «palabra por palabra». Es la misma cara |
| 168 | Común | «No es lo mismo.» · «Porque ellas pueden decir que no lo intentaron.» · «Yo no tengo esa excusa.» | molesta | ✅ | — | La compara con las que no estudian, y ahí salta: l. 179 «Eso sí le tocó algo», l. 181 «Lo dijo rápido» |
| 185 | Común | «…» · «Olvida lo que dije.» | timida | 🔁 | **molesta** | C1: l. 202 «La postura no había cambiado, pero algo en los hombros sí». `timida` descruza los brazos y junta las manos, así que cambia la postura entera. C3: se corta sola y nadie la ha pillado, así que está molesta consigo misma. La sonrisa de `timida` no cabe aquí. Con el cambio, el `show` no cambia nada en pantalla |
| 263 (+272) | Común, tras el CG | «¿Vas a quedarte mirando o vas a buscar tu cuaderno?» · «No te dejo.» | neutral | ✅ | — | Recompuesta. l. 275 «no se movió del pupitre» |
| 312 | m4a · cálida | «¿Qué tiene el segundo paso?» | molesta | 🔁 | **neutral** | C2: l. 321 «Se quedó quieta un segundo, decidiendo si eso contaba como ayuda»: es duda, no enojo. C5: hoy va molesta → neutral (325) → molesta (338) en tres réplicas. Con el cambio, la cálida sigue con la cara de la 263 y su único pico de orgullo es la 338 |
| 325 | cálida | «…» · «La unidad no se cancela ahí.» · «Arrastré el valor sin convertir.» | neutral | ✅ | — | Trabaja: l. 330 «Repasó la línea. Una vez. Dos veces» |
| 338 | cálida | «Lo sabía. Se me pasó.» | molesta | ✅ | — | El MC le pincha el orgullo: «¿Eso lo sabías o te lo estoy diciendo yo?» |
| 359 | cálida | «…El resultado me da distinto ahora.» · «…Es el que tenía que dar.» | timida | ✅ | — | l. 368 «No lo dijo como un triunfo»; l. 370 «todavía sin mirarme». Por eso va `timida` (sonrisa cerrada, mirada baja) y no `sonriendo` (C7) |
| 372 (+383) | cálida | «Puedes buscar tu cuaderno ahora.» · «…Como quieras, [mc].» | neutral | ✅ | — | Revisión P6 (C4): el hito del nombre lo marca el narrador (l. 381), no la cara. l. 386 «Levantó la vista, un segundo, para comprobar si hablaba en serio» |
| 403 (+422) | m4b · tibia | «No.» · «No hace falta. La respuesta es no.» · «Bien.» | molesta | ✅ | — | Rechazo seco: l. 412–416 cierra el cuaderno «Lo suficiente para que entendiera que la oferta ya estaba rechazada». Los brazos cruzados son esa puerta cerrada, y separan la tibia de las otras dos (C6) |
| 454 | m4c · fría | «¿Qué haces?» | sorprendida | ✅ | — | C1: él le quita el cuaderno (l. 452) |
| 469 (+478) | fría | «…» · «Ya lo veo.» | molesta | 🔁 | **neutral** (469 y 478) | C1/C2: l. 481 «Lo dijo sin agradecerlo y sin discutirlo», l. 483 «la forma más fría de aceptar algo», l. 550 «Ni siquiera protestó». `molesta` es la protesta que el texto niega. Con `neutral`, la fría se lee como está escrita: el susto (454) y luego la cara se apaga. La 478 (`molesta at pj_calla`) cambia también, si no, vuelve a cruzar los brazos mientras calla. La 495 deja de cambiar nada. El rencor de la fría sale a la mañana siguiente (reacción, conexiones l. 565), no aquí |
| 495 (+500) | fría | «Puedes irte. Ya tengo lo que necesitaba.» | neutral | ✅ | — | l. 503–505 «Cerró el cuaderno del todo… No volvió a levantar la vista» |

### 02_cap1_beat_Itsuki.rpy (11 shows)

| archivo:línea | Rama / escena | Diálogo (resumido) | Actual | Veredicto | Propuesta | Por qué |
|---|---|---|---|---|---|---|
| 91 | Azotea, común | «No te oí llegar.» · «Da igual. Ya estás aquí.» | neutral | ✅ | — | C1: l. 100 «sin la hostilidad de siempre» |
| 110 | Común | «Y lo era.» · «Ya no me queda ningún sitio que no lo sea.» | molesta | 🔁 | **neutral** | C1: l. 121–125 «Fue una frase corta… Simplemente no tenía más que decir»: es resignación, no enojo, y diez líneas antes el narrador ha dicho «sin la hostilidad de siempre». C5: neutral (91) → molesta → neutral (129). Con el cambio, la 129 no cambia nada |
| 129 | Común | «¿Tú también?» · «No hace falta mesa para tener un cuaderno abierto.» · «…» | neutral | ✅ | — | Las l. 173 y 177 van sobre el CG (§4) |
| 188 | Visitada · cálida | «Ya me ayudaste con el ejercicio el otro día.» · «No hace falta que sigas viniendo a comprobar cómo voy.» | molesta | 🔁 | **neutral** | C6: hoy las tres variantes van en `molesta`. En la cálida no hay rencor: él la ayudó y ella lo admite («Ya me ayudaste»). Es orgullo formal (C2): l. 197 «No pareció creérselo del todo.» y l. 199 «Pero no insistió.». La revisión no decidió esta cara: P1 solo cambió el texto (C4) |
| 203 | Visitada · fría | «Ya me resolviste el ejercicio el otro día.» · «No hace falta que sigas viniendo a comprobar cómo voy.» | molesta | ✅ | — | El rencor de la fría (C6), el mismo que en su reacción |
| 218 | Tibia y no visitada | «No voy a preguntarte cómo va tu juego.» | molesta | ✅ | — | La rivalidad del juego. Sin un evento que la abra, sigue cerrada |
| 246 | Común (N1) | «Eso no fue mi estómago.» · «Lo ibas a decir.» | sorprendida | ✅ | — | Revisión N1 (C4). Se lee como el susto de que la pillen (aviso 6) |
| 259 | Común (N1) | «No pienso aceptar comida de mi tutor.» · «...Un bocado. Y queda anotado como deuda.» | timida | ✅ | — | Revisión N1. l. 264 «Lo dijo mirando el arroz»: la mirada baja del sprite |
| 276 | Común, y el menú | op. 1 «Qué imagen tan poco digna de un tutor.» · op. 2 «Habla por ti.» · op. 3 «Al menos en eso estamos de acuerdo.» · «No te acostumbres.» | neutral | ✅ | — | Revisión N1 (cierra con `neutral`). Ironía seca: firmeza, no enojo (C2) |
| 315 | op. 2 | «Estoy descansando la vista.» · «Es distinto.» | timida | ✅ | — | La pilla: «Tienes el cuaderno cerrado hace diez minutos» (C3) |
| 346 | Común | «Se acabó el descanso.» | neutral | ✅ | — | Se recompone con el timbre. En las op. 1 y 3 no cambia nada |

### 02_cap1_conexiones.rpy (60 shows)

En `reaccion_itsuki`, `rama_hub` es la rama de Itsuki. `queja_itsuki` es la ruta no visitada.

| archivo:línea | Rama / escena | Diálogo (resumido) | Actual | Veredicto | Propuesta | Por qué |
|---|---|---|---|---|---|---|
| 471 | Reacción · cálida | «...Buenos días.» · «Ayer me viste equivocarme. No va a ser costumbre.» · «Corrijo rápido. Es lo único que se me da bien.» | neutral | ✅ | — | Revisión P7 (C4): tono de informe |
| 484 | Reacción · cálida | «...No digas cosas así. Sin avisar.» · «Anoche rehíce el ejercicio.» · «...Salió bien.» · «Lo logré sola. Del todo.» | timida | ✅ | — | El cumplido la pilla (C3). Su sonrisa cerrada cubre el «Lo logré sola» sin gastar `sonriendo` (C7) |
| 501 (+514) | Reacción · cálida | «No te lo cuento para que me felicites.» · «Bien. Porque solo era una conversión.» · «...Lo sé.» | neutral | ✅ | — | Se recompone. l. 517 «No me miró. Pero tampoco giró la silla hacia la ventana» |
| 523 | Reacción · tibia | «Sigo sin necesitar tu ayuda.» · «Tienes la costumbre de mirar como si fueras a corregir.» · «Sí. Y es una costumbre desagradable.» | molesta | ✅ | — | Reproche educado y cortante (P13) |
| 542 | Reacción · tibia | «...Todavía.» · «Todavía no necesito tu ayuda.» · «Es una expresión. No es una promesa.» | neutral | ✅ | — | El desliz que sostiene su eco del E6 (revisión §5) |
| 553 (+558) | Reacción · tibia | «Y no me mires así.» | molesta | ✅ | — | Vuelve a la armadura (C3). Va molesta → neutral → molesta, pero cada cambio lo motiva una réplica |
| 565 (+594) | Reacción · fría | «Lo sé.» · «Anoche. Sola.» · «Lo que hiciste ayer no cuenta. Quería que fuera mío.» · «Ya tengo lo que necesitaba de ti. Eso fue todo.» | molesta | ✅ | — | Ahora sí: la mochila en el pupitre de él (l. 568) y la raya sobre su solución (l. 576). Es el rencor que en el hub no salió (C6) |
| 866 (+869) | Queja · no visitada | «Dije que no me iba a esconder. Y no lo hice.» · «Entonces gané el juego.» · «Tener razón. Es lo único que siempre me sale bien.» | neutral | ✅ | — | — |
| 886 | Queja | «No te rías.» · «Se te nota en la voz.» | molesta | ✅ | — | Pique |
| 895 | Queja | «...Tampoco esperaba que me buscaras.» · «Yo no iba a pedírtelo. Pedirlo habría sido...» · «Nada. Una tontería.» | neutral | ✅ | — | La oración sin cerrar (l. 902) |
| 908 (+919) | Queja | «Solo digo que, si hubieras venido, no te habría echado.» · «No inmediatamente.» · «Y no lo apuntes en ningún sitio.» | molesta | ✅ | — | La revisión pide no tocar esta escena (§5). Aquí el amor-odio va con la armadura, y se paga en el E6 con la `timida` de «Esta vez sí lo anoto» (l. 3798, N4) |
| 971 (+990) | Interc. 1 · grupo | (sin líneas) | neutral | ✅ | — | — |
| 1026 (+1031, 1076, 1091) | Interc. 1 | «Supongo que consiste en hacernos estudiar de día y de noche.» · coro «¿Qué?» | molesta | ✅ | — | Sarcasmo hostil del grupo (P13) |
| 1127 (+1140) | Interc. 1 | «Al contrario. Que lo averigüe él.» · «Entonces resuelve esto: dónde pasa la tarde cada una.» | neutral | ✅ | — | Revisión P5 (C4) |
| 1153 (+1164, 1179, 1196, 1235, 1240) | Interc. 1 | «No. Él quería que se lo dijéramos…» · «Te estoy evaluando…» · «No me felicites. Solo te estoy complicando las cosas.» · «Yo no pienso esconderme. Estaré donde siempre.» | molesta | ✅ | — | Revisión P5 (C4): la revancha por la hoja de diagnóstico |
| 1746 (+1755) | Interc. 3 · grupo | (sin líneas) | neutral | ✅ | — | — |
| 1872 | Interc. 3 | «El juego sigue.» · «No me importa a quién elijas.» · «Solo digo que el reloj no espera.» · «Y cada uno lo sabe.» | molesta | 🔁 | **neutral** | C2: es la organizadora informando del plazo, con su tono de informe. l. 1902: «Itsuki tenía razón. Siempre la tiene cuando habla así». Antes (l. 1866 / 1870) el narrador solo dice que sigue en su pupitre: nada motiva el ceño |
| 2280 (+2293) | Interc. 4 · grupo | (sin líneas) | neutral | ✅ | — | — |
| 2362 (+2373) | Interc. 4 | «Nino no se va sin avisar. Es un hecho.» · «No es asunto tuyo. Pero tampoco es casualidad.» · «Y la hipótesis más probable eres tú.» | molesta | ✅ | — | Acusa al MC por su hermana: enojo de verdad, dicho con lógica (P12) |
| 2832 (+2857, 2966) | Interc. 5 | «Estoy repasando.» · «Estoy repasando con profundidad.» | neutral | ✅ | — | l. 2962 «ni se molestó en levantar los ojos del cuaderno» |
| 2979 (+2990) | Interc. 5 · visitada | «Los temas ya me los sé. Eso no es lo que me preocupa.» · «Me preocupa llegar el día del examen y que no salgan.» · «No te pedí que lo dijeras.» | molesta | 🔁 | **neutral** | C1/C2: confiesa una preocupación. l. 2993: «No dio las gracias. Pero tampoco me pidió que me callara». C6: hoy visitada y no visitada llevan la misma cara. La no visitada (2997) se queda en `molesta`, así que el evento cambia algo también en la cara |
| 2997 (+3010, 3108) | Interc. 5 · no visitada | «Y no hace falta que te preocupes por mí.» · «Entonces deja de mirarme el cuaderno.» · «Y quita esa cara de querer intrometerte.» | molesta | ✅ | — | A la defensiva. l. 3013 «Lo cerró con las dos manos» |
| 3353 (+3364, 3383) | Interc. 6 | «El juego se acabó hoy.» · «Era la última tarde libre. No quedan más.» · «Te dije que no alcanzarías para todas. Tres de cinco.» | neutral | ✅ | — | Informe (C2) |
| 3392 (+3399) | Interc. 6 | «Es un aprobado a medias, Yotsuba.» · «Hay algo de esfuerzo, pero no lo suficiente.» | molesta | 🔁 | **neutral** (3392 y 3399) | C2: le pone nota a su hermana; con Yotsuba no hay enojo. C5: neutral (3364) → molesta → neutral (3491), y entre medias se queda en `molesta`, atenuada, unas 90 líneas (3399–3491). La 3399 (`molesta at pj_calla`) cambia también, para que no vuelva a cruzar los brazos al callarse |
| 3491 (+3502, 3509, 3518) | Interc. 6 | «Por lo tanto, hoy no queda nada que adivinar.» · «Esta tarde se estudia en casa.» · «Nadie. Pero alguien tiene que decirlo.» | neutral | ✅ | — | La firmeza que organiza al grupo, el caso de manual (C2). l. 3523 «Eso, con ella, ya era una señal» |
| 3540 (+3547) | Interc. 6 · clima buena | «No te emociones tanto. Todavía no aprobamos nada.» · «…se lo agradeceremos, si se lo merece.» | neutral | ✅ | — | Frena a Yotsuba. Era candidata a `sonriendo`; descartada (C7, §6 e) |
| 3554 (+3559) | Interc. 6 · clima mixta | «Aprovecha la tarde. No va a haber otra.» | neutral | ✅ | — | — |
| 3574 (+3579) | Interc. 6 · clima mala | «Y procura no empeorarlo.» | molesta | ✅ | — | El único clima con reproche (C6). l. 3582 «Nadie se rió» |

### 02_cap1_evento6.rpy (0 `show` + 25 `e6_foco` + 2 `e6_formacion_neutral` + 1 `e6_entrar`)

| archivo:línea | Rama / escena | Diálogo (resumido) | Actual | Veredicto | Propuesta | Por qué |
|---|---|---|---|---|---|---|
| 259 | Lunes, formación | (sin líneas) | neutral | ✅ | — | Formación |
| 417 | Lunes · cálida y fría | «He estudiado cada noche. Y por primera vez sé lo que hago.» · «…Pero ya sé por dónde volver.» · «No me felicites todavía.» | sonriendo | 🎨 | sonriendo rehecho (§7) | Revisión P4 (C4). Es la primera sonrisa desde el prólogo (C7). El 🎨 es por la silueta: en formación, el paso desde `neutral` no se ve |
| 431 | Lunes · tibia y no visitada | «…lo repito hasta que salga.» · «No pedí ayuda a nadie. Prefiero equivocarme sola que acertar con ayuda.» · «Me lo tomo en serio.» | neutral | ✅ | — | Revisión P4 |
| 2178 | Aula de la tarde, formación | (sin líneas) | neutral | ✅ | — | Formación |
| 2321 | Aula de la tarde | «Y el mes. El plazo era de un mes.» | neutral | ✅ | — | Informe |
| 2373 | Aula de la tarde | «Apoyo la idea.» | sonriendo | 🎨 | sonriendo rehecho (§7) | La idea de Miku, que todas salgan a la vez: calidez de grupo dicha en su registro formal |
| 2752 | Tarde · cálida | A: «Ayer levanté la mano. En un examen. Delante de toda la clase.» / B: «Ayer encontré el error sola.» · «Me ganó mi orgullo.» | neutral | ✅ | — | Informe |
| 2772 | Tarde · cálida | «Que conste: no fue un favor. Fue un procedimiento.» | timida | ✅ | — | El «que conste» tapa que pidió ayuda o pensó en pedirla: de ahí el rubor. «Firme» (l. 2778) habla de la oración, que esta vez cierra con su punto, no del cuerpo |
| 2785 | Tarde · tibia | «La cuarta la reescribí dos veces.» · «Preguntar sería—» · «…Lo revisé sola. Y salió.» | neutral | ✅ | — | La oración que se queda a medias |
| 2800 | Tarde · fría | «Resolví sola. Cada paso. Sin preguntar a nadie.» · «No necesitaba ayuda. El examen lo demuestra.» | molesta | ✅ | — | l. 2806 «Lo dijo sin mirarme. Pero lo dijo hacia mí»: va contra él (C6) |
| 2813 | Tarde · no visitada | «Tarde. Pero todo lo hice yo.» · «…Si alguien me hubiera dicho dónde mirar, habría llegado a tiempo.» · «No lo digo por ti.» | neutral | ✅ | — | — |
| 2923 | La pregunta · cálida | «Falta un resultado. ¿Y a ti cómo te fue?» | neutral | ✅ | — | l. 2927 «Lo preguntó sin rodeos» |
| 3286 | Departamento, entrada | (narración de llegada: l. 3583, 3614, 3633, 3652) | neutral | ✅ | — | Entrada común a las cinco |
| 3587 | Eco · cálida | «Dije que el juego se acabó. No dije quién ganó.» · «Eso no se pregunta, [mc].» · «Es un informe, no una invitación a aplaudir.» | sonriendo | 🎨 | sonriendo rehecho (§7) | Revisión N5 (C4): firma con su nombre |
| 3616 | Eco · tibia | «Aquel día dijiste «revisarlo desde el principio». …¿Qué ibas a—» · «…No dije que quisiera.» | neutral | ✅ | — | — |
| 3635 | Eco · fría | «Revisé desde el principio. Sola… La diferencia es mía.» · «No tienes que saberlo. …Es solo que cuenta.» | molesta | ✅ | — | l. 3633 «el puño cerrado sobre el bolígrafo del examen» |
| 3643 | Eco · fría | (sin línea; va justo antes de `e6_foco("", "")`) | neutral | ✅ | — | Se suelta tras «…Es solo que cuenta» y llega a la mesa sin el ceño |
| 3654 | Eco · no visitada | «Dije que el juego se acabó, y gané.» · «No lo hay. …Por eso es lo único que me sale.» | neutral | ✅ | — | l. 3664 «con la oración cerrada y terminada» |
| 3766 | La disculpa | «Sobre lo del primer día—» · «Dije que tú primero. Es una oración completa.» · «…Ese argumento es válido.» | neutral | ✅ | — | — |
| 3794 | La disculpa (N4) | «…Queda pendiente.» · «Esta vez sí lo anoto.» | timida | ✅ | — | Revisión N4 (C4). l. 3800 «se le habían puesto rojas las orejas» |
| 3818 | Mesa | «Propongo lo siguiente.» · «Cada una lo abre en silencio…» | neutral | ✅ | — | Organiza (C2) |
| 3830 | Mesa | «…Es para que no se vuele.» | timida | ✅ | — | La pilla Ichika (C3) |
| 3838 | Mesa | «…Es por si acaso.» | timida | ✅ | — | La pilla Nino. Es la misma cara: solo pasa el foco |
| 3898 | Mesa | «Tu expresión no es la de quien trae malas noticias. …Aunque no es una garantía.» | neutral | ✅ | — | — |
| 3983 | Mesa, los boletines | «Lo leí dos veces. …El resultado no cambió.» · «…Algo con sujeto, verbo y—» · «…Anótenlo, provisionalmente, como «algo bueno».» | sonriendo | 🎨 | sonriendo rehecho (§7) | Revisión P10. l. 3991 «No le salió el punto. Por una vez, no pareció importarle» |
| 4005 | Mesa | «Es un alivio. Eres malo dando discursos.» | neutral | ✅ | — | Ironía seca |
| 4057 | Mesa | «Breve. Aceptable. Bien dicho.» | neutral | ✅ | — | Le pone nota como a un informe: la gracia está en no sonreír |
| 4095 | Mesa, la foto | «Debo salir recta. Con el boletín recto.» | neutral | ✅ | — | C1: «recta» es el sprite, con los brazos rectos |

### 02_cap1_final_malo.rpy (16 shows)

| archivo:línea | Rama / escena | Diálogo (resumido) | Actual | Veredicto | Propuesta | Por qué |
|---|---|---|---|---|---|---|
| 177 (+202, 208, 296) | Despido A · sala | «...¿Hoy?» · «Te lo dije el primer día. Esto no iba a funcionar.» · fría «Eso no se me va a olvidar.» / cálida «Pensé que habría una segunda.» / tibia «Ahora no voy a saber qué ibas a explicarme.» · «Un «lo siento» ahora sería para ti, no para nosotras.» | neutral | ✅ | — | Frialdad, no gritos: l. 301 «No me hace ninguna gracia», l. 335 «Itsuki tenía razón. Otra vez». Las tres ramas comparten el `show` de la 296 (§9) |
| 515 (+535) | Despido B · aula | (sin líneas) | neutral | ✅ | — | Grupo |
| 572 (+581, 596) | Despido B · aula | «He estudiado más que nadie en esta aula. Cada noche.» · «Y no sé si me sé una sola cosa.» · «Quisiera poder culparte. Sería más fácil.» | molesta | 🔁 | **neutral** | C1: dice que no puede culparle. Es duda y derrota, no enojo. El bloque que sigue es el del grupo derrotado (l. 593–599) |
| 949 (+963) | Aula de la tarde · grupo | (sin líneas) | neutral | ✅ | — | — |
| 1016 (+1047) | Aula de la tarde | «Estudié todas las noches.» · «…no supe qué contestar.» · cálida «No sé si la culpa es tuya o mía.» / fría «Me resolviste un ejercicio.» · «Uno. Y no aprendí nada de él.» / resto «Te pedí que no me ayudaras. Y no lo hiciste.» · «No sé qué es peor.» | molesta | ✅ | — | Ahora sí le reprocha (revisión P3). Contrasta con la 572: antes del examen no podía culparle; después, sí |
| 1384 | Despedida | «Te vas sin que nadie te lo pida. Eso es raro en ti.» · «Sí. Debiste.» · «...» | neutral | ✅ | — | — |
| 1399 | Despedida | «Yo tampoco dije que lo sentía.» · «Eso lo hace parejo, supongo.» · «Ya no sirve de nada.» · «Pero acepto tu disculpa.» | timida | ✅ | — | La disculpa llega tarde y es agridulce. La sonrisa cerrada de `timida` es la reconciliación que ya no sirve |
| 1416 | Despedida · fría | «Me quitaste el cuaderno de las manos.» · «Aun así, lo agradezco. No sé por qué.» | neutral | ✅ | — | La fría recupera la distancia (C6) |

---

## 6. Resumen

**Momentos evaluados: 103** (prólogo 11 · apertura 2 · hub 15 · beat 11 · conexiones 28 · E6 28 · final malo 8).

| Veredicto | Momentos | Dónde |
|---|---|---|
| ✅ | **87** | — |
| 🔁 | **11** (13 líneas) | apertura 81 · hub 120, 185, 312, 469 (+478) · beat 110, 188 · conexiones 1872, 2979, 3392 (+3399) · final malo 572 |
| 🎨 | **5** (un solo sprite) | `itsuki sonriendo`: prólogo 371 · E6 417, 2373, 3587, 3983. La cara está bien elegida en los cinco; lo que falla es la silueta (§1, §7) |
| ➕ | **0** | Ninguna emoción sin sprite se repite en varias escenas. La frialdad la cubre `neutral` (C2) |

**Uso de cada expresión** (sentencias `show itsuki <expr>`; aparte, los `e6_foco` del E6):

| Expresión | Hoy (105 `show`) | Tras 🔁 | E6 `e6_foco` hoy (25) | Tras 🔁 |
|---|---|---|---|---|
| neutral | 50 | **62** | 15 | 15 |
| molesta | 44 | **33** | 2 | 2 |
| timida | 6 | **5** | 4 | 4 |
| sorprendida | 4 | 4 | 0 | 0 |
| sonriendo | 1 | 1 (rehecho) | 4 | 4 (rehecho) |

A eso se suman, siempre en neutral, las 2 formaciones y la entrada del E6.

**Comprobaciones a–e:**
- **(a) Contradicción con el texto:** 6 casos, todos con una línea del narrador que niega lo que muestra el sprite:
  - apertura 81: «no valgo ni para enojarse»;
  - hub 185: «La postura no había cambiado»;
  - hub 469: «sin discutirlo», «Ni siquiera protestó»;
  - beat 110: «Simplemente no tenía más que decir», tras «sin la hostilidad de siempre»;
  - conexiones 2979: confiesa que le preocupa el examen, y el narrador dice que «tampoco me pidió que me callara»;
  - final malo 572: «Quisiera poder culparte».
- **(b) neutral y molesta por inercia:** de los 44 `show` en `molesta`, **12 (10 momentos) eran firmeza, frialdad o derrota** y pasan a `neutral`. La 185 va al revés, de `timida` a `molesta`, así que quedan 33. Esas 33 tienen un blanco: el MC del primer día, su orgullo pinchado, el rencor de la fría, la acusación por Nino, el clima malo o el reproche tras el examen. No encontré ninguna `neutral` donde la emoción ya hubiera cambiado sin que la cara la siguiera.
- **(c) Parpadeo:** 4 casos de A → B → A, y todos se arreglan con los 🔁: hub 120 / 145 / 168, hub cálida 312 / 325 / 338, beat 91 / 110 / 129 e interc. 6 3364 / 3392 / 3491. A eso se suma la apertura 76 → 81, un cambio sin réplica suya que también desaparece. Se quedan dos alternancias porque cada cambio lo motiva una réplica: la queja (869 → 886 → 895 → 908, escena que la revisión pide no tocar) y la reacción tibia (523 → 542 → 553, el desliz del «Todavía»).
- **(d) Ramas tras los cambios:**
  - Hub: cálida neutral → molesta (338) → timida → neutral · tibia molesta · fría sorprendida → neutral.
  - Beat: cálida neutral · fría molesta · el resto molesta.
  - Reacción: cálida neutral → timida → neutral · tibia molesta → neutral → molesta · fría molesta.
  - Interc. 5: visitada neutral · no visitada molesta (hoy, las dos molesta).
  - Interc. 6 por clima: buena y mixta neutral · mala molesta.
  - E6 lunes: cálida y fría sonriendo · tibia y no visitada neutral.
  - E6 tarde: cálida neutral → timida · tibia neutral · fría molesta · no visitada neutral.
  - E6 eco: cálida sonriendo · tibia neutral · fría molesta → neutral · no visitada neutral.
  - Final malo: el `show` es común; en la despedida, la fría vuelve a neutral (1416).
  - La fría queda con un arco limpio: se queda helada en el hub, el rencor sale a la mañana siguiente y lo arrastra hasta el eco.
- **(e) SONRIENDO:** hasta el E6 **no propongo ninguna**. Revisé las candidatas:
  - hub cálida 359: el narrador dice «No lo dijo como un triunfo»;
  - reacción cálida 497–499, «Lo logré sola»: la cubre el `show` de la 484, que tiene que ser `timida` por «No digas cosas así», y separarlas exige insertar un `show`;
  - beat: la azotea es contención, y la revisión (§5) lo pide así;
  - interc. 6 buena 3540: frena a Yotsuba («No te emociones tanto»).

  La ausencia no es una decisión escrita de la revisión, pero sigue su lógica: el nombre «lo usó cuando era amable y lo perdió en cuanto él la rechazó» (§1), y P4 pone la primera sonrisa del capítulo en el lunes del E6. Entre medias, la calidez de la cálida se ve en `timida` (hub 359, reacción 484), que ya sonríe con la boca cerrada (C7).

---

## 7. 🎨 `itsuki sonriendo`: rehacer con otra silueta

**Por qué.** Es el par peligroso de §1: `sonriendo` y `neutral` tienen la misma silueta, y la regla de §9 de la GUIA lo dice tal cual: «Si dos expresiones tienen la misma silueta, en pantalla son la misma». Sus cinco usos son los momentos de calidez del arco (prólogo 371 · E6 417, 2373, 3587, 3983), y en los cinco viene de `neutral` o de la formación neutral. No es un ➕: no hace falta una emoción nueva, sino que la que ya existe se vea.

**Nueva pose: manos juntas a la espalda.** Es la única opción libre: `neutral` lleva los brazos a los lados, `molesta` cruzados, `timida` las manos juntas delante y `sorprendida` una mano en el pecho. A la espalda no queda nada delante del cuerpo, igual que el criterio de `miku animada`. Comprobado contra los cinco usos:

| Uso | ¿Sigue sirviendo? |
|---|---|
| Prólogo 371, pide ayuda con educación | ✓ Las manos a la espalda son pose de pedir algo con cortesía. Mejor que hoy |
| E6 417, «No me felicites todavía» | ✓ Orgullo compuesto |
| E6 2373, «Apoyo la idea.» | ✓ Y en formación el cambio desde `neutral` (2321) por fin se ve |
| E6 3587, eco cálido | ✓ El narrador dice que llega «con el bolígrafo del examen todavía en la mano» (l. 3583). Con las manos atrás el bolígrafo no se ve; hoy tampoco sale en el sprite |
| E6 3983, lee el boletín | ✓ El sprite no muestra el papel, ni hoy ni rehecho |

**Prompt de PixAI** (sin campo negativo, todo en positivo). Modelo Tsubaki.2 · **sin LoRA de serie** (GUIA §1, aviso 4) · LoRA de personaje `中野五月 サンプル(アニメ)Tsubaki.2バージョン` a **0.8** · lienzo **768×1280 en vertical** (§3: las de Itsuki vinieron apaisadas y la neutral necesitó escala 1,584) · apunta la semilla.

```
masterpiece, best quality, official anime screencap, go-toubun no hanayome style,
1girl, solo, only one person in the entire image, nakano itsuki,
standing, front view, facing viewer, centered, figure from head to knees, knees at the bottom edge, plain white background, solid white background,
very long bright red hair, deep crimson red hair, vivid red hair reaching past her waist, long flowing hair, waist length hair, ahoge, yellow star hair clips on both sides of her bangs, blue eyes,
gentle smile, closed mouth smile, soft happy eyes, light blush, head slightly tilted,
hands clasped behind her back, arms behind back, both hands hidden behind her back, elbows pointing slightly outward, chest open, relaxed shoulders,
red sweater vest, v-neck red knit vest, white collared shirt, short sleeve white shirt, bare forearms, shirt tucked into the skirt, green pleated skirt,
flat even studio lighting, clean lineart, deep focus
```

Después, normalizar con `normalizar_sprite.py` al estándar cerrado del set (§3): **760×930 RGBA**, ojos en la fila **199**, IPD **77,2** y eje en el centro de la falda. Comprobar que sale **un** solo ahoge (aviso 5) y que el faldón de la camisa no asoma.

**Archivo y atributo:** sustituye a `game/images/sprites/itsuki_sprites/itsuki_sonriendo.png`. La declaración no cambia: `image itsuki sonriendo = "sprites/itsuki_sprites/itsuki_sonriendo.png"` (`00_definiciones.rpy` l. 253). **No hay que tocar ningún `.rpy`.**

---

## 8. Cambios 🔁 por archivo (antes → después)

Solo cambia el atributo de expresión. La posición (`at …`), el `with` y el orden se quedan igual. Sin ternarios.

**`02_cap1_apertura.rpy`**
```renpy
# l. 81
    show itsuki molesta at pj(0.5)
# →
    show itsuki neutral at pj(0.5)
```

**`02_cap1_Itsuki.rpy`**
```renpy
# l. 120
    show itsuki molesta at pj_habla(0.5)
# →
    show itsuki neutral at pj_habla(0.5)

# l. 185
    show itsuki timida at pj_habla(0.5)
# →
    show itsuki molesta at pj_habla(0.5)

# l. 312
    show itsuki molesta at pj_habla(0.5)
# →
    show itsuki neutral at pj_habla(0.5)

# l. 469
    show itsuki molesta at pj_habla(0.5)
# →
    show itsuki neutral at pj_habla(0.5)

# l. 478
    show itsuki molesta at pj_calla(0.5)
# →
    show itsuki neutral at pj_calla(0.5)
```

**`02_cap1_beat_Itsuki.rpy`**
```renpy
# l. 110
    show itsuki molesta at pj(0.5)
# →
    show itsuki neutral at pj(0.5)

# l. 188 (dentro de if itsuki_visitada_cap1 and itsuki_rama_cap1 == "calida":)
        show itsuki molesta at pj(0.5)
# →
        show itsuki neutral at pj(0.5)
```

**`02_cap1_conexiones.rpy`**
```renpy
# l. 1872
    show itsuki molesta at pj_habla(X_ITSUKI)
# →
    show itsuki neutral at pj_habla(X_ITSUKI)

# l. 2979 (dentro de if itsuki_visitada_cap1:)
        show itsuki molesta at pj_habla(X_ITSUKI)
# →
        show itsuki neutral at pj_habla(X_ITSUKI)

# l. 3392
    show itsuki molesta at pj_habla(X_ITSUKI)
# →
    show itsuki neutral at pj_habla(X_ITSUKI)

# l. 3399
    show itsuki molesta at pj_calla(X_ITSUKI)
# →
    show itsuki neutral at pj_calla(X_ITSUKI)
```

**`02_cap1_final_malo.rpy`**
```renpy
# l. 572
    show itsuki molesta at pj_habla(X_ITSUKI)
# →
    show itsuki neutral at pj_habla(X_ITSUKI)
```

**Cómo probarlo (después de aplicar).** En la consola (Shift+O). Las etiquetas que terminan en `return` te devuelven al menú principal al acabar: es solo para ver la cara.
- `jump cap1_apertura` y avanza hasta el aula (l. 76–131).
- `jump hub_Itsuki`. Cubre la 120 y la 185, y el menú elige la rama: «Señalarle dónde mirar» = cálida (312), «Quitarle el cuaderno» = fría (469 / 478).
- Beat cálida: `$ itsuki_visitada_cap1 = True`, `$ itsuki_rama_cap1 = "calida"` y `jump beat_Itsuki` (110 y 188).
- Interc. 3: `$ destino = "ichika"`, `$ rama_hub = "tibia"` y `jump cap1_interconexion_3` (1872, al final).
- Interc. 5 visitada: `$ itsuki_visitada_cap1 = True` y `jump cap1_interconexion_5` (2979).
- Interc. 6: `$ destino = "itsuki"`, `$ itsuki_rama_cap1 = "calida"` y `jump cap1_interconexion_6` (3392 / 3399, en la parte común).
- Final malo B: `jump final_malo_hub3` (572).
- El E6 no cambia: no hace falta `11_e6_debug.rpy`.

---

## 9. Fuera de alcance (anotado, no propuesto)

- **`show` que repiten la cara.** Con la regla del usuario (un `show` con atributo solo cuando cambia el sprite), quedan candidatos en todos los archivos: prólogo 493, hub 272 / 383 / 500, conexiones 514, 869, 990, 1031, 1140, 1179, 1196, 1235, 1240, 2293, 2373, 2857, 2966, 3364, 3383, 3502, 3509, 3518, final malo 535 / 963, y los que dejen sin efecto los 🔁 (apertura 81, hub 145 y 495, beat 129, y la 2979, que pasaría a ser un repetido de la 2966). En ramas (prólogo 1259, beat 203 / 218, conexiones 565 / 2997 / 3540 / 3554) hay que mirarlo a mano. Es la misma limpieza que se hizo con Miku, en una pasada aparte.
- **`show` compartido entre ramas en el final malo:** l. 296 (fría «Eso no se me va a olvidar», cálida «Pensé que habría una segunda») y l. 1016 (cálida «No sé si la culpa es tuya o mía»). Separarlos exige insertar un `show` dentro de cada rama.
- **Despedida de conexiones (l. 3849 / 3927):** no hay sprite para ninguna de las cinco. Si se quiere, es una decisión de escena para todas.
- **`itsuki neutral` es el render más ampliado del set** (escala 1,584, GUIA §3). Es una cuestión de resolución, no de expresión. Si algún día se regenera, que sea en vertical.
- **E6 l. 417, `sonriendo` también en la fría:** la revisión (P4) junta cálida y fría porque las dos «saben dónde mirar». Se respeta (C4), aunque es la única `sonriendo` de la ruta fría.
