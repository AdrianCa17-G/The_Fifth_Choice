# Evaluación de sprites · Ichika · Prólogo + Capítulo 1

> Revisado sobre el árbol de trabajo actual (commit `19d226e`, con los cambios ya aplicados de Nino, Miku, Itsuki y Yotsuba sin commitear).
> Es una evaluación: no se tocó ningún `.rpy`. Los números de línea son los de hoy.
> **Estado (14/11/2026):** aprobada entera. Las 10 sentencias del §7 están aplicadas tal cual y el Lint sale limpio (solo los dos avisos de antes). Conteo comprobado: neutral 33 · sonriendo 36 · agotada 12 · determinada 3; `e6_foco` sonriendo 20 · neutral 13.
> Fuentes:
> - `docs/GUIA_ARTE.md` §2, §3 y §9, y `docs/GUIA_RENPY.md` §1 y §2;
> - `docs/REVISION_PERSONAJES_CAP1/REVISION_ICHIKA_CAP1.md` (ya aplicada; manda sobre cualquier propuesta);
> - `docs/CAPITULO_1/HUBS_HERMANAS/CAP1_evento_ichika.md` (guion del hub y sus notas de arte) y `docs/CAPITULO_1/EVENTO_6/` (sobre todo `CAP1_evento_6_bloques_A.md`, con los `[SPR …]` de los ecos);
> - las evaluaciones de Nino, Miku, Itsuki y Yotsuba (formato y criterios);
> - los seis `.rpy` del recorrido, más `10_mj_ichika.rpy` y `11_e6_debug.rpy` para el E6.

---

## 0. Avisos: dónde el encargo y los archivos no dicen lo mismo (mandan los archivos)

| # | El encargo dice | Los archivos dicen | Qué hice |
|---|---|---|---|
| 1 | Vestuario: «Blazer azul marino, falda verde, suéter amarillo atado a la cintura» | GUIA §2: «Ichika va sin blazer para no parecerse a Nino» y «Camisa blanca, suéter amarillo atado a la cintura, falda verde plisada. Sin blazer.». Ninguno de los 4 PNG lleva blazer. | Manda la GUIA: Ichika va sin blazer. No hace falta prompt, porque no hay 🎨 ni ➕. |
| 2 | Apertura: 1 show y 7 líneas | Las 7 líneas existen, pero el `show ichika sonriendo` (l. 331) **solo cubre 4**: 335, 339, 343 y 345. La 169 «¡Un éxito rotundo!» se dice en `bg_departamento` sin ningún sprite. La 196 y la 198 van sobre el CG `cg_cinco_sentadas` (l. 179). | Evalué el `show` y anoté las otras tres en el §4. |
| 3 | E6: 0 shows, 109 líneas | Es literal: no hay ningún `show ichika`. La pintan **33** `call e6_foco("ichika", …)` (sonriendo 21 · neutral 12), **2** `call e6_formacion_neutral` (l. 259 y 2178) y **1** `call e6_entrar(e6_h)` (l. 3286). Las 109 líneas son: **60** `ichika` con sprite, **44** `ichika_int` sobre su CG y **5** `ichika` sobre otros CG. | Evalué los 36. Diagnóstico en el §3. |
| 4 | 107 shows · sonriendo 36 · neutral 37 · agotada 7 · determinada 3 | Cuadra: prólogo 14 · apertura 1 · hub 24 · conexiones 51 · final malo 17. **83** llevan atributo y **24** son de solo tinte (`show ichika at …`). | Uso esas cifras. |
| 5 | — | El guion del hub llama `sonrisa` al sprite (`CAP1_evento_ichika.md` l. 496). El archivo y el código usan **`sonriendo`**. El hub también marca `agotada` como «pendiente», pero el PNG ya existe. | Uso los nombres del código. |
| 6 | — | El guion del hub (l. 550–551) dice que el intercambio del tren «reutiliza `ichika_neutral` y `ichika_sonrisa`». El código usa **`determinada`** en la l. 188. | Lo dejo como está (✅, §5). La narración pide justo una cara distinta: l. 214 «tapando otra vez algo que se le había escapado sin querer». Además, la pista matemática no se convierte en una afirmación: la tapa la sonrisa de la l. 209. |

---

## 1. Ficha de los 4 sprites

Los cuatro son PNG RGBA de 760×930. Están declarados en `00_definiciones.rpy` l. 258–261. Ninguno lleva blazer.

| Sprite | Pose y brazos | Mirada | Boca | Lo que transmite de verdad | Lo que NO cubre |
|---|---|---|---|---|---|
| `ichika neutral` | De frente, cabeza un poco ladeada. **Brazos colgando**: la mano derecha junto al bajo de la falda, la izquierda algo separada, los dedos sueltos. | **Párpados a media asta**, mirada de quien sabe algo. | **Sonrisa cerrada, suave, de medio lado.** Rubor. | La hermana mayor segura y provocadora. Es la «base fuera de la actuación completa» (hub l. 495): la máscara a media potencia, o una calma sincera en voz baja. | La cara sin sonrisa. El cansancio. La decisión seria. |
| `ichika sonriendo` | **Palmas juntas bajo la barbilla**, como pidiendo «porfa». Es la silueta más reconocible del set. | **Ojos cerrados** (^^). | Sonrisa cerrada. Rubor. | El encanto actuado: el «porfa», el gracias teatral, el chiste para tapar algo. Con los ojos escondidos, es la máscara en funcionamiento (hub l. 496). También sirve para la alegría o el agradecimiento sincero, si el texto lo marca. | La seguridad tranquila, que vive en el medio lado de `neutral`. Cualquier momento de silencio o de seriedad. |
| `ichika agotada` | **Los dos brazos caídos y más abiertos**, con las manos flojas y separadas. | Párpados pesados. | Pequeña y plana, **sin sonrisa**. Rubor. | Cansancio de verdad: no hay ni media sonrisa ni bostezo. Es «el instante sin actuación» (hub l. 494). | La pereza cómica (el «papel» de floja del prólogo). La tristeza activa. |
| `ichika determinada` | **Brazos pegados al cuerpo**, con las manos a los lados de la falda y los dedos algo cerrados. | **Directa**, de frente. | Plana y cerrada, **sin sonrisa**. | Firmeza, una decisión, decir algo en serio y sin red. | Cualquier ligereza. |

**Regla de §9 (a un 30 % solo se lee la silueta):**

- **`neutral` ↔ `determinada`: es el par confundible.** Las dos tienen los brazos abajo y pegados. Las separan la boca (medio lado o plana), los párpados y la mano cerrada, y a un 30 % casi no se ve. **No propongo 🎨.** Los 3 usos de `determinada` (hub 188 y 509, reacción cálida 71) son a solas, en el centro (0.5) y en primer plano. Es el mismo caso que el par `neutral` ↔ `sonriendo` de Yotsuba, que tampoco se rehízo. El 🎨 de Itsuki se hizo porque su par salía en formaciones y en grupo, y aquí no pasa.
- **`neutral` ↔ `agotada`: se distinguen, aunque por poco.** `agotada` es más ancha (brazos abiertos, manos separadas) y no tiene sonrisa. El hub pedía que a un 30 % no se confundieran (l. 528–531), y se cumple a medias: la diferencia está en el ancho, no en una pose distinta. No lo propongo, porque `agotada` sale siempre en primer plano o en grupo con el texto marcándola.
- **`sonriendo` ↔ el resto: se distingue ✓.** Es la única con las manos arriba.

### Las preguntas clave

**¿`sonriendo` se lee como la sonrisa segura de hermana mayor, la máscara?** **Se lee como máscara, pero como máscara de encanto, no de seguridad.** Los ojos cerrados y las manos juntas son actuación pura: la sonrisa que pide, que agradece o que tapa. Por eso funciona en el «¡Era un chiste!», en el «¿Acaso planeas una cita con cada una?» y en el «¡Es que soy muy organizada!». La **seguridad** de hermana mayor (la que provoca, la que sabe) la lleva `neutral`, con su medio lado y los párpados a media asta: prólogo 724 y 920, «¡Corazonada de hermana mayor!» en el E6. Entre las dos cubren la máscara completa y no falta ningún sprite.

**¿`agotada` se lee como cansancio real o como pereza?** **Como cansancio real.** No hay ni sonrisa ni bostezo ni postura cómoda: las manos cuelgan sin fuerza y la boca se queda plana. Lo único que podría sugerir dejadez son las manos abiertas. Por eso no vale para el papel de floja del prólogo, que es justo lo que el código no le pide: el prólogo no la usa ni una vez. **Lo que pide la pregunta (c) es lo contrario: hay momentos de cansancio real que hoy siguen en `neutral` o `sonriendo` por inercia** (§6).

---

## 2. Criterios aplicados (los de las otras cuatro, adaptados a Ichika)

- **C1 · La narración manda.** Si el narrador describe la cara o la voz, va el sprite que lo cumple:
  - «Sonrió» y «ya está sonriendo» → **no** `agotada`;
  - «Ni un chiste. Ni una máscara.» → **no** `sonriendo`;
  - «Aquí no hace falta que sonría» → **no** una cara que sonríe;
  - «Se fue con la sonrisa puesta» → `sonriendo`.
- **C2 · La escala de la grieta de Ichika:** `sonriendo` (la máscara entera) → `neutral` (a media potencia) → `agotada` (sin actuación). `determinada` queda aparte: no es una grieta, es una decisión.
- **C3 · La máscara se lee por el contexto.** Una `sonriendo` que es máscara es ✅ si el texto la marca. Solo se cambia cuando el texto dice que ya no sonríe.
- **C4 · La revisión manda.** Se respetan tal cual:
  - **P2** (interc. 5): cálida `neutral` «Iba a decirte que estoy bien» → `sonriendo`; visitada tibia/fría `agotada` «Yo estoy bien. Que conste.» → `sonriendo`;
  - **P3** (lunes del E6): `sonriendo` en cálida, tibia y fría, y `neutral` en la no visitada;
  - **P7** (reacción cálida): `neutral` → `determinada` «¿Pero quién cuida de ti?» → `sonriendo`;
  - **§0 fila 5:** «el coqueteo es máscara en todas las rutas; el cuidado sincero es solo de la cálida»;
  - **§0 fila 1:** «La floja es el papel; la agotada es la persona.».
- **C5 · Parpadeo.** Nada de A → B → A en réplicas seguidas, ni cambios de cara que ninguna línea motive. Se arregla cambiando el atributo. Ningún `show` se borra.
- **C6 · Ramas.** En el mismo punto del guion, cálida, tibia y fría llevan caras distintas siempre que el texto lo permita. La cálida es la única que baja la máscara, y lo hace con una cara distinta de su sonrisa.
- **C7 · Sin favoritismo visual.** `agotada` no es un premio de la cálida: la revisión misma la pone en la tibia y la fría (P2, l. 3057), y el final malo la usa en todas las ramas. Lo exclusivo de la cálida es el **cuidado sincero**, no el cansancio.

Veredictos: ✅ queda bien · 🔁 cambiar a otra expresión existente · 🎨 rehacer el sprite · ➕ sprite nuevo.

---

## 3. Evento 6: diagnóstico (mismo caso que las otras cuatro)

**Conclusión: el diagnóstico vale igual para Ichika.** De las 109 líneas, las **60** `ichika` dichas en escena tienen sprite por `e6_foco`. Las otras **49** (44 `ichika_int` y 5 `ichika`) van sobre un CG a propósito. Es el mismo diseño de `e6_mostrar_foco` (l. 91).

| Tramo (etiqueta · líneas) | Líneas de Ichika | Qué hay en pantalla | ¿Intencional o falta? |
|---|---|---|---|
| Lunes en el aula (`e6_lunes` · 312–354) | **14** `ichika`: cálida 4, tibia 3, fría 2, no visitada 5 | Formación neutral (l. 259) y `e6_foco` l. 310 / 322 / 334 / 344 | Sprite ✓ |
| Núcleo de Matemáticas (`e6_ichika_nucleo` · 830) | 0 | **CG `cg_ichika_examen`** (l. 845) | — |
| Voz interior (`e6_ichika_mono_<estado>` · 871–968) | **40** `ichika_int`: cálida 18, tibia 9, fría 7, no visitada 6 | El mismo CG | Intencional: monólogo sobre su CG |
| Minijuego (`e6_ichika_mj` · 973) | **4** `ichika_int` | El CG. Durante el juego, la screen con su **chibi** (`mj_retrato("ichika", …)`, `10_mj_ichika.rpy` l. 648) | Intencional |
| Gesto tibio (`e6_ichika_gesto_tibia` · 1031) | **1** `ichika` (1037 «Es una técnica, profesor.») | El CG | Intencional: lo dice dentro del examen |
| Aula de la tarde, en grupo (`e6_despues`) | **5** `ichika` (2271–2379) | Formación (l. 2178) y `e6_foco` l. 2269, 2293, 2303, 2377 | Sprite ✓ |
| Tarde por rama (`e6_ichika_tarde_*` · 2587–2662) | **17** `ichika`: cálida 7, tibia 4, fría 2, no visitada 4 | `e6_foco` l. 2589, 2599, 2614, 2618, 2624, 2635, 2648, 2652, 2656 | Sprite ✓ |
| La pregunta al MC (`e6_tarde_pregunta` · 2919) | **2** `ichika` (2945, 2947), solo en el `else` | `e6_foco` l. 2943 | Sprite ✓ |
| Departamento y eco (`e6_cinco` · 3286, `e6_ichika_eco_*` · 3399–3474) | **10** `ichika`: cálida 2, tibia 3, fría 2, no visitada 3 | Entra neutral (`e6_entrar`, l. 3286), `e6_foco` l. 3403, 3409, 3422, 3428, 3445, 3451, 3464, 3472 | Sprite ✓ |
| Mesa (`e6_mesa` · 3826–4085) | **12** `ichika` | `e6_foco` l. 3824, 3842, 3892, 3931, 3999, 4009, 4083 | Sprite ✓ |
| Foto (l. 4104–4165) | **4** `ichika` (4125, 4141, 4143, 4165) | **CG `cg_cinco_aprobadas`** (l. 4104 / 4109 / 4114, según el tinte) | Intencional: CG de las cinco |

Cuenta: 14 + 5 + 17 + 2 + 10 + 12 = **60** con sprite · 40 + 4 = **44** `ichika_int` sobre CG · 1 + 4 = **5** `ichika` sobre CG. Total, **109** ✓.

**Excepciones, solo de expresión (no de diseño):**

- **l. 2599, tarde cálida.** El foco pasa a `sonriendo` (ojos cerrados, manos juntas: la máscara) justo antes de «No era otra persona. Eso es lo que todavía no me creo.», y el narrador cierra con l. 2607 «Ni un chiste. Ni una máscara. Solo lo que había pasado.». Es un 🔁 (§5).
- **l. 3963, «Yotsuba. El tuyo.».** Ichika lo dice mientras el foco es de Yotsuba (l. 3955), así que se ve atenuada con su última cara (`sonriendo`, de la l. 3931). Es una línea suelta de reparto y la cara no choca. Va al §9.

---

## 4. Líneas de Ichika sin sprite fuera del E6

| Archivo · líneas | Qué hay en pantalla | ¿Intencional? |
|---|---|---|
| `01_prologo.rpy` 622–636 | CG `cg_ichika_puerta` (l. 611) | Sí, es CG |
| `01_prologo.rpy` 649 | CG `cg_nino_pasillo` (l. 644) | Sí, es CG |
| `01_prologo.rpy` 1138, 1140 | CG `cg_hermanas_estudiando` (l. 1131) | Sí, es CG |
| `02_cap1_apertura.rpy` 169 «¡Un éxito rotundo!» | `bg_departamento`, **sin sprite**. Justo antes, l. 165: «Me abrió Ichika, otra vez, con la misma sonrisa de la primera vez.» | Es una puerta, como la del prólogo. Si se quisiera la sonrisa, habría que insertar un `show ichika sonriendo`. Va al §9 y no lo propongo (sería añadir un `show`, no cambiar un atributo) |
| `02_cap1_apertura.rpy` 196, 198 | CG `cg_cinco_sentadas` (l. 179) | Sí, es CG |
| `02_cap1_Ichika.rpy` 97–109 | CG `cg_ichika_desarmada` (l. 94) | Sí: Mov. 2, «el instante sin ninguna actuación» |
| `02_cap1_Ichika.rpy` 245–251 | CG `cg_ichika_mascara` (l. 236) | Sí: Mov. 3, la máscara reconstruida en POV |

---

## 5. Tabla por archivo

Un momento es el `show` (o `e6_foco`) donde cambia la expresión, más las líneas de Ichika que cubre. Los `show ichika at …` de solo tinte, y los que repiten la misma cara, van en el momento que los contiene. La única excepción es la l. 670, que es de solo tinte y es la que se propone cambiar.

### 01_prologo.rpy (14 shows)

| archivo:línea | Rama / escena | Diálogo (resumido) | Actual | Veredicto | Propuesta | Por qué |
|---|---|---|---|---|---|---|
| 724 (+729, 736, 749, 756) | Departamento, presenta a Nino y provoca al MC | «No te lo tomes como algo personal. Tarda en soltarse.» · «Vaya, qué frío.» · «Y yo que pensaba que los chicos como tú apreciaban estar con chicas bonitas como nosotras.» | neutral | ✅ | — | La hermana mayor segura y provocadora. El coqueteo va con el medio lado de `neutral`, no con el «porfa» de `sonriendo` |
| 893 (+898, 904) | Se entera de que Nino y el MC ya se conocían | «Vaya, vaya... Veo que no necesitan presentación.» | sonriendo | ✅ | — | La burla teatral de quien disfruta la escena |
| 920 (+926, 940, 968, 981) | Sigue pinchando a Nino | «¿Así que [mc] fue el que te rechazó la propuesta de estudiar juntos?» | neutral | ✅ | — | Provoca desde la seguridad. Vuelve a la base después del gesto teatral |
| 1051 | Coro «¡No pensamos estudiar!» | (línea de `quintillizas`) | neutral | ✅ | — | La formación del coro. Solo Yotsuba se distingue, por la revisión |

### 02_cap1_apertura.rpy (1 show)

| archivo:línea | Rama / escena | Diálogo (resumido) | Actual | Veredicto | Propuesta | Por qué |
|---|---|---|---|---|---|---|
| 331 | Departamento, defiende el examen de las seis | «Bueno, tampoco hay que dramatizar.» · «Contestamos las seis. Nadie dijo que hubiera que acertarlas.» · «Somos quintillizas, pensamos parecido.» | sonriendo | ✅ | — | Máscara marcada por el texto (C3): l. 337 «Lo dijo mirando a Yotsuba, no a mí.», l. 347 «Mentía tan bien que casi daba gusto.» |

### 02_cap1_Ichika.rpy (24 shows · hub con ramas)

`ichika_m4a` = cálida · `ichika_m4b` = tibia · `ichika_m4c` = fría · `ichika_m5` = el mensaje del papel, común a las tres. Hasta la l. 275 es común.

| archivo:línea | Rama / escena | Diálogo (resumido) | Actual | Veredicto | Propuesta | Por qué |
|---|---|---|---|---|---|---|
| 128 (+133) | Común · Mov. 2, recién despierta | «¿Yo?» · «Jaja, te preocupas demasiado por mí, [mc].» · «¡Estaba practicando!» | agotada | ✅ | — | Es uno de los dos sitios donde el hub permite `agotada` (l. 545–547). La voz ya actúa, pero la cara todavía no: la máscara solo vuelve en la 150 |
| 150 | Común | «¡Claro que existe! ¡Lo inventé yo hace cinco minutos!» | sonriendo | ✅ | — | l. 155 «Se rió de su propio chiste, un poco más fuerte.» Máscara |
| 167 | Común | «¡Lo suficiente!» · «¿Y desde cuándo un tutor pide cifras de algo que no entra en el examen?» | neutral | ✅ | — | l. 176 «Lo dijo con una sonrisa, pero cambió de tema otra vez». La sonrisa de medio lado de quien esquiva |
| 188 | Común · el horario del tren | «Martes a las cinco y veinte. Nunca antes de eso.» · «Salgo del ensayo a las cuatro treinta y cinco. Cuatro minutos para cambiarme.» | determinada | ✅ | — | Aviso 6. Lo dice «de corrido, sin titubear» (l. 205). Es lo que «se le había escapado sin querer» (l. 214), y tiene que verse distinto de la sonrisa que lo tapa en la 209 |
| 209 | Común | «¡Es que soy muy organizada! ¡Parte del oficio!» | sonriendo | ✅ | — | l. 214 «Se rió, tapando otra vez algo…». Máscara |
| 262 | Común · vuelta a la sala, antes del menú | (sin líneas; el MC: «Ahora espera el siguiente. El mío.») | agotada | 🔁 | **sonriendo** | C1: l. 253 «Sonrió, esperando la broma de vuelta.» y el menú, l. 275 «Ella ya está sonriendo.». El hub limita `agotada` al Mov. 2 y al 4A (l. 545–547). Las tres ramas arrancan desde la máscara: la cálida la baja (300 neutral, 317 agotada), la tibia la sigue (397 sonriendo) y la fría la deja intacta (452 neutral, l. 455) |
| 300 | Cálida · el MC no le sigue la broma | «...¿Qué?» · «No pusiste cara de nada.» · «Pusiste cara de estar esperando algo.» | neutral | ✅ | — | La sonrisa se le queda a media potencia cuando no le devuelven la broma |
| 317 | Cálida · baja la máscara | «...No sé cuánto más puedo seguir haciendo esto.» · «Todo.» · «Las audiciones. Las clases.» | agotada | ✅ | — | El 4A del hub. l. 315 «sin la sonrisa de antes». La bajada de máscara de la cálida tiene su propia cara, distinta de `sonriendo` (e) |
| 350 | Cálida | «¿No vas a decir nada aprovechado sobre esto?» · «No sé. Algo de tutor.» | neutral | ✅ | — | Vuelve la base, pero sin el «porfa» todavía |
| 367 (+372) | Cálida | «...Gracias por no decir la frase obvia.» | sonriendo | ✅ | — | l. 377 «Volvió la sonrisa. Pero tardó». La máscara vuelve tarde, que es el rasgo de la cálida (revisión P7) |
| 397 (+414, 431) | Tibia · le sigue la broma: el dragón | «¡Eso es de telenovela de la tarde! Hay que innovar.» · «¡Un dragón que además sabe matemáticas!» · «¡Y el dragón tendría que usar lentes! ¡Para verse serio con los números!» | sonriendo | ✅ | — | El MC es su público favorito: juega de verdad, sin grieta |
| 452 | Fría · el consejo de padre | «...» · «Ya veo.» | neutral | ✅ | — | l. 455 «La sonrisa no desapareció del todo, pero algo detrás de ella sí». Por eso `neutral`, que conserva media sonrisa, y no `agotada` |
| 463 (+468) | Fría | «¡Tienes razón! ¡Debería aprovechar mejor el tiempo!» | sonriendo | ✅ | — | Revisión: «le contesta como se le contesta a un padre: «tienes razón», sonriendo» |
| 502 | Común · Mov. 5, llega el mensaje | (sin líneas) | neutral | ✅ | — | Mira el móvil |
| 509 | Común | «Es del club. Dicen que hay un papel libre para la obra de primavera.» · «¡Es buenísimo! Es el papel que quería desde el año pasado.» | determinada | ✅ | — | l. 524 «Pero no sonrió al decirlo. No todavía.». El núcleo del personaje, en las tres ramas (revisión, l. 910) |
| 528 | Común | «Obvio que sí.» | sonriendo | ✅ | — | Ahora sí llega la sonrisa |
| 541 | Común | «No pongas esa cara.» · «Esa que dice que vas a sumar otra cosa a la lista de preguntas que no me vas a hacer.» · «Mentiroso.» | neutral | ✅ | — | Lo ve venir y lo dice de medio lado |
| 556 (+561) | Común | «Contestaré luego. Ahora tengo que acompañarte a la salida antes de que cierren el edificio.» | sonriendo | ✅ | — | Cierra el tema con la máscara |

### 02_cap1_conexiones.rpy (51 shows)

| archivo:línea | Rama / escena | Diálogo (resumido) | Actual | Veredicto | Propuesta | Por qué |
|---|---|---|---|---|---|---|
| 51 | Reacción · cálida | «¡Buenos días, [mc]!» · «Logré dormir siete horas y media.» · «¡He conseguido un récord personal!» | sonriendo | ✅ | — | Alegría sincera: ha dormido |
| 64 | Reacción · cálida | «...Tú deberías hacer lo mismo. Dormir, digo.» · «Siempre estás cuidando de las demás.» | neutral | ✅ | — | C4: P7 |
| 71 | Reacción · cálida | «¿Pero quién cuida de ti?» · «Yo puedo hacerlo. Si me dejas.» | determinada | ✅ | — | C4: P7. El cuidado sincero, solo de la cálida |
| 80 (+87) | Reacción · cálida | «¡Era un consejo gratis! Exclusivo para ti, [mc].» · «¡No se lo cuentes a nadie!» | sonriendo | ✅ | — | C4: P7. La máscara vuelve, y tarde |
| 97 (+112) | Reacción · tibia | «¡Buenos días, señor de los dragones!» · «El dragón ya tiene nombre.» · «Se llama «Contrato».» | sonriendo | ✅ | — | Juego de la tibia |
| 117 | Reacción · fría | «Buenos días, [mc].» | agotada | ✅ | — | C1: l. 143 «La sonrisa llegó medio segundo tarde.» y l. 145 «Hoy, con mi nombre y nada más.». Antes de la 135 la cara **no** sonríe, y `neutral` sí sonríe. La revisión también usa `agotada` en la fría (P2, l. 3057), así que no es una cara exclusiva de la cálida (C7) |
| 130 | Reacción · fría | «Ya sé qué hacer con mi tiempo. Gracias por preguntar.» | neutral | ✅ | — | Recompone la base |
| 135 (+140) | Reacción · fría | «¡Y hoy me portaré muy bien! Que conste.» | sonriendo | ✅ | — | La sonrisa que «llegó medio segundo tarde». Máscara |
| 619 (+622) | Queja · no la eligió | «Oye, [mc]. Tengo una queja formal.» · «Tres tardes. Tres. Y ninguna fue mía.» · «Qué cruel. Me siento como la actriz que se quedó sin papel.» | sonriendo | ✅ | — | Queja teatral: máscara |
| 639 | Queja | «...Estaba tan segura de que me ibas a elegir que ni preparé plan B.» · «Ensayé tres formas de reaccionar cuando me encontraras.» | neutral | ✅ | — | Baja a media potencia, a medio camino de la verdad |
| 656 | Queja | «¡Ay, no! ¡No me pidas perdón, que me da vergüenza ajena!» · «¡Era un chiste! ¡Soy una artista, siempre estoy espléndida!» | sonriendo | ✅ | — | Tapa |
| 663 | Queja | «...Pero la próxima vez, no tardes tanto.» · «Estas cosas se agradecen. Aunque no lo parezca.» | neutral | ✅ | — | La verdad, en voz baja |
| 670 | Queja · se va | (sin líneas; narrador) | (tinte) | 🔁 | **sonriendo** | C1: l. 673 «Se fue con la sonrisa puesta.» y l. 675 «como quien se ajusta un disfraz». Con el tinte solo se queda en `neutral`, y el narrador describe que se pone la máscara |
| 967 (+986) | Interc. 1 · grupo, entra | (sin líneas) | neutral | ✅ | — | Formación |
| 1020 (+1025, 1072, 1087) | Interc. 1 | «Vaya, resulta que además de cerebrito eres un estratega.» | sonriendo | ✅ | — | Coqueteo: máscara en todas las ramas (revisión §0 fila 5) |
| 1103 (+1114) | Interc. 1 | «Ay, [mc]. ¿Para qué quieres saberlo?» · «¿Acaso planeas una cita con cada una?» | sonriendo | ✅ | — | Ídem |
| 1197 (+1208) | Interc. 1 | «¿Entonces pasarás la tarde con tu quintilliza favorita?» · «Seguro me eliges a mí. Soy la más bonita de todas.» | sonriendo | ✅ | — | Ídem |
| 1742 (+1751) | Interc. 3 · grupo, entra | (sin líneas) | neutral | ✅ | — | Formación |
| 1777 (+1796) | Interc. 3 · le devuelve la pregunta del sueño | «Pregunta seria, [mc]: ¿cuántas horas llevas sin dormir bien?» · «Eso lo diría alguien que no duerme.» · «Qué tutor más terco.» | sonriendo | ✅ | — | La «pregunta seria» es la broma: le devuelve su propio interrogatorio del hub. El cuidado de verdad lo dice Miku en la réplica siguiente («...Tienes ojeras.») |
| 2277 | Interc. 4 · grupo, entra | (sin líneas) | neutral | ✅ | — | Formación |
| 2294 | Interc. 4 · ¿dónde está Nino? | «Te ves muy preocupado por Nino, ¿no, [mc]?» · «¿Acaso hay algo entre ustedes dos?» | sonriendo | ✅ | — | Coqueteo de máscara. La cálida se distingue por el texto (l. 2303 «se quedó esperando la respuesta un segundo de más») |
| 2307 (+2320) | Interc. 4 | «Pues salió de manera apresurada.» · «Con el celular en la mano y esa cara que ya conoces.» | neutral | ✅ | — | Informa |
| 2829 (+2858) | Interc. 5 · grupo, entra | (sin líneas) | neutral | ✅ | — | Formación |
| 3017 | Interc. 5 · última tarde libre | «Hoy es tu última tarde libre, ¿no?» · «Pues piénsatelo bien.» | sonriendo | ✅ | — | Lo plantea como broma |
| 3026 | Interc. 5 | «...Y no te lo digo por mí.» · «Te lo digo porque después ya no hay vuelta atrás.» | neutral | ✅ | — | Baja la broma |
| 3035 | Interc. 5 · cálida | «Iba a decirte que estoy bien.» · «Contigo ya no me sale.» | neutral | ✅ | — | C4: P2 |
| 3044 | Interc. 5 · cálida | «Solo... elige a quien de verdad lo necesite.» · «No a la que mejor lo disimule.» | sonriendo | ✅ | — | C4: P2 |
| 3057 | Interc. 5 · visitada (tibia/fría) | «Yo estoy bien. Que conste.» | agotada | ✅ | — | C4: P2. La cara desmiente la frase, y el MC lo nota |
| 3064 | Interc. 5 · visitada | «Solo... elige a quien de verdad lo necesite.» · «No a la que mejor lo disimule.» | sonriendo | ✅ | — | C4: P2 |
| 3085 | Interc. 5 · no visitada | «Yo ya sé que no me vas a elegir a mí.» · «¡Me da igual! ¡Soy la favorita de todos modos!» | sonriendo | ✅ | — | Máscara |
| 3092 (+3097, 3109) | Interc. 5 · no visitada | «...Es broma. Más o menos.» | neutral | ✅ | — | La grieta pequeña de quien no fue visitada |
| 3349 (+3360) | Interc. 6 · grupo, entra | (sin líneas) | neutral | ✅ | — | Formación |
| 3400 | Interc. 6 · el tutor que corría detrás de ellas | «Y el pobre tutor corriendo detrás de nosotras todo el mes.» · «Qué romántico.» · «A mí me encontró dormida en el suelo.» | sonriendo | ✅ | — | Coqueteo de máscara |
| 3425 | Interc. 6 · habla Nino, y sigue hasta el final | (sin líneas; se queda así hasta el `hide` de la l. 3590) | sonriendo | 🔁 | **neutral** | C1: en clima mala, l. 3582 «Nadie se rió. Ni siquiera Ichika.» y l. 3584 «Cuando Ichika no rellena un silencio con un chiste…». Con `sonriendo`, el «porfa» con los ojos cerrados se queda en pantalla toda la escena. Es el mismo arreglo que el aprobado para Yotsuba en la l. 3391, en el mismo punto (coherencia entre evaluaciones) |

### 02_cap1_evento6.rpy (0 `show` + 33 `e6_foco` + 2 `e6_formacion_neutral` + 1 `e6_entrar`)

| archivo:línea | Rama / escena | Diálogo (resumido) | Actual | Veredicto | Propuesta | Por qué |
|---|---|---|---|---|---|---|
| 259 | Lunes · formación | (sin líneas) | neutral | ✅ | — | Formación común |
| 310 | Lunes · cálida | «Dormí cuatro horas. Esta vez por las fórmulas, no por el papel de la obra.» | sonriendo | ✅ | — | C4: P3. El orgullo de haberlas gastado en lo que tocaba |
| 322 | Lunes · tibia | «¡Dormí cuatro horas! Mitad fórmulas, mitad guion.» · «¡Equilibrio artístico!» | sonriendo | ✅ | — | C4: P3 |
| 334 | Lunes · fría | «Dormí lo justo y repasé lo justo. Todo cronometrado.» · «Hoy me portaré muy bien. Que conste.» | sonriendo | ✅ | — | C4: P3. Máscara |
| 344 | Lunes · no visitada | «Dormí cuatro horas. Con el guion en una mano y las fórmulas en la otra.» | neutral | ✅ | — | C4: P3 |
| 2178 | Tarde · formación | (sin líneas) | neutral | ✅ | — | Formación común |
| 2269 | Aula de la tarde | «Qué tutor más raro.» | sonriendo | ✅ | — | Burla cariñosa |
| 2293 | Aula de la tarde | «Oigan. ¿Se han dado cuenta?» · «La campana sonó hace un buen rato. Y ninguna se ha ido.» | neutral | ✅ | — | Lo nota la hermana mayor, en serio pero con calma |
| 2303 | Aula de la tarde | «El pasillo está vacío desde hace diez minutos, Nino.» | sonriendo | ✅ | — | Pincha a Nino |
| 2377 | Aula de la tarde | «Aprobada por todas. Es la primera votación del mes que no gana Nino.» | sonriendo | ✅ | — | Ídem |
| 2589 | Tarde · cálida | «No me dormí en ningún examen.» · «Leí cada enunciado entero, con los ojos abiertos.» | neutral | ✅ | — | Lo cuenta sin actuar |
| 2599 | Tarde · cálida | «No era otra persona. Eso es lo que todavía no me creo.» · «Tú lo viste antes que yo, [mc]. En la sala de ensayo.» | sonriendo | 🔁 | **neutral** | C1: l. 2607 «Ni un chiste. Ni una máscara. Solo lo que había pasado.». `sonriendo` es la máscara (ojos cerrados, manos juntas). Se queda la calma de `neutral` de la 2589 |
| 2614 | Tarde · tibia | «¡El profesor me pilló sonriéndole a la hoja! Le dije que era una técnica.» | sonriendo | ✅ | — | Anécdota de actriz |
| 2618 | Tarde · tibia | «Lo resolví rápido, eso sí.» · «Lo que no sé es si… No tengo que po—» | neutral | ✅ | — | Casi se le escapa |
| 2624 | Tarde · tibia | «¡Olvídalo! Una línea de ensayo. Se me cuelan.» | sonriendo | ✅ | — | Tapa. A → B → A, pero con una línea suya en cada cambio |
| 2635 | Tarde · fría | «Resolví todo sin un tachón. Aproveché el tiempo, tal cual.» · «Y no, no estoy cansada. Por si alguien iba a preguntar.» | sonriendo | ✅ | — | La fría no baja la máscara (revisión §0 fila 5) |
| 2648 | Tarde · no visitada | «Hice el examen con una mano y ensayé con la otra. Debajo del pupitre.» | neutral | ✅ | — | — |
| 2652 | Tarde · no visitada | «Una pregunta, una línea. ¡Multitarea de actriz!» | sonriendo | ✅ | — | Máscara |
| 2656 | Tarde · no visitada | «…Salieron las dos bien, creo. No sé cuál de las dos era yo.» · «…Ah. Esa.» | neutral | ✅ | — | l. 2664 «Fue una sonrisa pequeña, de las que no se ensayan»: es el medio lado de `neutral` |
| 2943 | La pregunta · si nadie más la hace | «Falta alguien, ¿no?» · «¿Y a ti cómo te fue, tutor?» | neutral | ✅ | — | La hermana mayor que se acuerda del MC |
| 3286 | Departamento · entrada | (sin líneas) | neutral | ✅ | — | `e6_entrar`, común |
| 3403 | Eco · cálida | «Anoche dormí once horas. Esta vez no redondeé.» · «Pensé antes de decir que sí a algo. Una sola vez. Me pareció una cosa nueva.» | neutral | ✅ | — | `[SPR]` del guion del E6 |
| 3409 | Eco · cálida | (sin líneas) | sonriendo | ✅ | — | l. 3411 «La sonrisa le llegó medio segundo tarde. Esta vez la dejó llegar.». Sonrisa sincera, la única del E6 que el narrador valida así |
| 3422 | Eco · tibia | «¡Pidió prórroga! ¡Los dragones siempre piden prórroga!» | sonriendo | ✅ | — | `[SPR]` del guion |
| 3428 | Eco · tibia | «Era un chiste. …Era un chiste, ¿verdad?» · «Eso pensaba yo.» | neutral | ✅ | — | «Se calló un segundo de más» |
| 3445 | Eco · fría | «¿Todo bien? Yo estoy bien. Que conste.» | sonriendo | ✅ | — | «con la sonrisa puesta, como todo lo demás» |
| 3451 | Eco · fría | «Ya. Lo dije por si acaso.» | neutral | ✅ | — | `[SPR]` del guion |
| 3464 | Eco · no visitada | «Ensayé cómo salir y no me sale ninguna.» · «Me salen las tres de siempre. Y ninguna sirve para esto.» | neutral | ✅ | — | `[SPR]` del guion |
| 3472 | Eco · no visitada | «¡Qué amable! …Esa fue la graciosa. Perdona el reflejo.» | sonriendo | ✅ | — | La graciosa, nombrada como tal |
| 3824 | Mesa | «Qué plan tan ordenado, Itsuki.» · «Hablas con mucha confianza para alguien que lleva un minuto con la mano encima del papel.» | sonriendo | ✅ | — | Pincha a Itsuki |
| 3842 | Mesa | «Hablando por todas, debería decir que todo va a salir bien.» · «…¡Corazonada de hermana mayor!» | neutral | ✅ | — | La seguridad de hermana mayor, que vive en `neutral` |
| 3892 | Mesa | «Qué tutor más cruel.» | sonriendo | ✅ | — | Broma |
| 3931 | Mesa · ve su nota | «Ja. …Ja, ja. …Me quedé sin chiste. A mí, que siempre tengo uno.» · «Tantas noches cortas. …Y valieron cada minuto.» · «Eso no venía en el guion.» | sonriendo | ✅ | — | l. 3933, la risa se le escapa. Alegría sincera, no máscara |
| 3999 | Mesa | «Y tú, tutor. Tienes cara de querer decirnos algo.» | sonriendo | ✅ | — | Burla |
| 4009 | Mesa | «La última vez fue «sin excepción». A gritos.» | sonriendo | ✅ | — | Ídem |
| 4083 | Mesa · antes de la foto | «Que se me vea la cara, no el flequillo.» | sonriendo | ✅ | — | Pose para la foto |

### 02_cap1_final_malo.rpy (17 shows)

| archivo:línea | Rama / escena | Diálogo (resumido) | Actual | Veredicto | Propuesta | Por qué |
|---|---|---|---|---|---|---|
| 173 (+188, 195) | Beat · la noticia del despido | «Dime que fue una de las discusiones de siempre, Nino.» | neutral | ✅ | — | Todavía no se lo cree |
| 215 | Beat | «Bueno... al menos fue rápido. ¿No?» | sonriendo | ✅ | — | El chiste reflejo. l. 220 «Nadie se rió. Ni ella.», y la cara cae en la réplica siguiente (222). El cambio de sprite cuenta justo eso |
| 222 (+238) | Beat | «...Perdón. Es lo que hago cuando no sé qué decir.» · «No te voy a defender, [mc]. No sabría con qué.» | neutral | ✅ | — | Sin máscara pero sin hundirse: aún no es el cansancio |
| 511 (+532) | Hub 3 · el aula, en grupo | (sin líneas) | neutral | ✅ | — | Formación |
| 554 (+563) | Hub 3 · cada una cuenta cómo llega | «Dormí cuatro horas.» · «Y las pasé con el papel de la audición, no con las fórmulas.» · «No me mires así. Ya sé que no era lo que tocaba.» | neutral | 🔁 | **agotada** | (c) Cansancio real, y lo dice ella: no ha dormido y lo ha gastado en lo que no tocaba. Las otras cuatro hablan desde su grieta (Yotsuba «no recuerdo qué sentía nadie», Itsuki «no sé si me sé una sola cosa»). Ichika es la única que se queda en su base sonriente. El lunes del E6 dice lo mismo con `sonriendo` (P3), pero allí es orgullo; aquí, culpa |
| 593 | Hub 3 · «Me miraron las cinco» | (sin líneas) | neutral | 🔁 | **agotada** | C5: si la 554 pasa a `agotada`, esta la devuelve a `neutral` sin ninguna línea suya. Se queda la cara de la 554 |
| 739 | Hub 3 · la despiertan en el examen | «Disculpe profesor.» · «¡Estaba pensando! Los matemáticos piensan con los ojos cerrados.» · «Lo siento...» | sonriendo | 🔁 | **agotada** | (c) La acaban de despertar (l. 734 «Nakano. Despierte.»). El brief: «duerme por agotamiento, no por floja», y la cara tiene que sostenerlo. El chiste sale con la cara agotada y por eso suena hueco: l. 746 «Nadie se rió.» y l. 732 «esta vez la función no era para nadie». A diferencia de la 215, aquí no hay un `show` después que deje caer la sonrisa: con `sonriendo`, el «Lo siento...» saldría con las manos juntas y los ojos cerrados |
| 945 (+960) | Hub 3 · la tarde, en grupo, después de los exámenes | (sin líneas; l. 952 «Nadie recogía nada. Ninguna dijo «salió bien».») | neutral | 🔁 | **agotada** (las 2 sentencias) | Lo detectó el cierre de conjunto. C1 y coherencia con Yotsuba: su `show` de la l. 948, en esta misma formación, pasó a `seria` (aprobado) justo por esta línea. Las `neutral` de Nino, Miku e Itsuki no sonríen, y la de Ichika sí: hoy es la única de las cinco que sonríe mientras el narrador dice que ninguna lo hace. La 960 la vuelve a poner en `neutral` sin ninguna línea suya (C5), así que cambia con ella. La 984 queda repetida |
| 984 (+999) | Hub 3 · la tarde | «Me dormí delante de todos.» · «Me dieron el papel de la obra.» · «Y ni siquiera me alegré.» | agotada | ✅ | — | l. 995 «Y hoy no tengo ganas de inventar nada.» |
| 1285 | Despedida · común a las tres ramas | «Aquí no hace falta que sonría, ¿verdad?» · «Ni contar algún chiste.» · «Fue un placer conocerte, [mc]. Y lo digo sin guiones.» | neutral | 🔁 | **agotada** | C1: dice que no hace falta sonreír, y `neutral` sonríe. `agotada` es «el instante sin actuación» (hub l. 494). Cuadra con las tres ramas que siguen: la fría, «Hoy no me queda para ninguna de las dos» (l. 1310); la cálida, «me dejaste quedarme callada sin llenar el silencio»; la tibia, el dragón que deja «Contrato» |

---

## 6. Resumen

**Momentos evaluados: 103** (prólogo 4 · apertura 1 · hub 18 · conexiones 34 · E6 36 · final malo 10).

| Veredicto | Momentos | Dónde |
|---|---|---|
| ✅ | **94** | — |
| 🔁 | **9** (10 sentencias) | hub 262 · conexiones 670, 3425 · E6 2599 · final malo 554, 593, 739, 945 (+960), 1285 |
| 🎨 | **0** | El par `neutral` ↔ `determinada` no lo justifica (§1) |
| ➕ | **0** | No falta ninguna emoción repetida: la cara sin sonrisa ya existe (`agotada`) y la firmeza también (`determinada`) |

**Uso de cada expresión** (sentencias `show ichika <expr>`; aparte, los `e6_foco` del E6):

| Expresión | Hoy (83 `show`) | Tras 🔁 (84) | E6 `e6_foco` hoy (33) | Tras 🔁 |
|---|---|---|---|---|
| sonriendo | 36 | **36** | 21 | **20** |
| neutral | 37 | **33** | 12 | **13** |
| agotada | 7 | **12** | 0 | 0 |
| determinada | 3 | 3 | 0 | 0 |

Nota sobre `sonriendo`: pierde 3425 y 739, y gana 262 y 670. La 670 era de solo tinte, por eso los `show` con atributo pasan de 83 a 84. Aparte, siempre en `neutral`, quedan las 2 formaciones y la entrada del E6.

**Comprobaciones a–e:**

- **(a) La cara contradice la línea: 7 casos.** En los 7, el narrador o la propia Ichika niegan lo que muestra el sprite:
  - final malo 945: «Ninguna dijo «salió bien».», con `neutral`, que sonríe (lo encontró el cierre de conjunto);
  - hub 262: «ya está sonriendo», con `agotada`;
  - conexiones 670: «Se fue con la sonrisa puesta», con `neutral` (tinte);
  - conexiones 3425: «Nadie se rió. Ni siquiera Ichika.», con `sonriendo`;
  - E6 2599: «Ni un chiste. Ni una máscara.», con `sonriendo`;
  - final malo 739: la despiertan en el examen y dice «Lo siento...», con `sonriendo`;
  - final malo 1285: «Aquí no hace falta que sonría», con `neutral`.
- **(b) SONRIENDO (36 `show`): 2 sinceras, 32 máscara, 2 a cambiar.**
  - Sinceras: reacción cálida 51 (ha dormido) y tibia 397 (el juego del dragón con su público favorito).
  - Máscara (incluido todo el coqueteo): 32, todas marcadas por el texto o por la revisión (§0 fila 5). Se quedan (C3).
  - A cambiar: 3425 y 739. No son máscara: son una sonrisa que el texto ya ha quitado.
  - En el E6, de los 21 focos en `sonriendo`, 2 son sinceros sin duda (3409 «Esta vez la dejó llegar», 3931 la risa que se escapa) y 1 se cambia (2599).
  - **`sonriendo` frente a `neutral`:** `sonriendo` es la máscara de encanto (ojos cerrados, manos juntas) y `neutral` es la seguridad o la calma (medio lado). La sonrisa **sincera** pequeña va en `neutral` (E6 2656 «de las que no se ensayan»). La grande, solo si el narrador la valida (3409, 3931).
- **(c) AGOTADA (7) y DETERMINADA (3).**
  - `agotada`: 6 de 7 son correctas. La 262 sobraba, porque el texto dice que ya sonríe. **Faltaban 5 momentos de cansancio real** (7 sentencias), todos en el final malo (554 +593, 739, 945 +960, 1285): allí el cansancio ya no se tapa y el texto lo dice. Se queda en 12 usos, en 3 archivos y en todas las ramas, como la persona que hay debajo del papel.
  - `determinada`: los 3 usos son correctos (el tren, el papel de la obra y «¿Pero quién cuida de ti?»). No encontré ninguna decisión firme que se haya quedado en `neutral` por inercia: las demás frases serias de Ichika van en voz baja, no firmes, y eso es `neutral` o `agotada`.
- **(d) Parpadeo: 0 casos hoy y 0 tras los cambios.**
  - Las alternancias del E6 (tarde tibia 2614 / 2618 / 2624, tarde no visitada 2648 / 2652 / 2656) llevan una línea suya en cada cambio.
  - La 593 se cambia justo para no crear uno: 554 agotada → 593 neutral.
  - Tras el cambio, la 2599 repite el `neutral` de la 2589. Sin cambio visible, sin parpadeo.
- **(e) Ramas tras los cambios:**
  - **Hub:** común sonriendo (262) → cálida neutral → **agotada** → neutral → sonriendo tarde · tibia sonriendo de principio a fin · fría neutral → sonriendo.
  - **Reacción:** cálida sonriendo → neutral → **determinada** → sonriendo · tibia sonriendo · fría agotada → neutral → sonriendo.
  - **Interc. 5:** cálida neutral → sonriendo · visitada agotada → sonriendo · no visitada sonriendo → neutral.
  - **E6 tarde:** cálida neutral, sin máscara (tras el 🔁) · tibia sonriendo → neutral → sonriendo · fría sonriendo sin grieta · no visitada neutral → sonriendo → neutral.
  - **E6 eco:** cálida neutral → sonriendo sincera · tibia sonriendo → neutral · fría sonriendo → neutral · no visitada neutral → sonriendo.
  - **La bajada de máscara de la cálida tiene una cara propia:** `agotada` en el hub 317 y `determinada` en la reacción 71, las dos sin sonrisa, frente a la `sonriendo` de las demás ramas. La fría nunca deja de sonreír delante del MC hasta el final malo, donde se le acaba la energía (1285, «Hoy no me queda para ninguna de las dos»).
  - **Sin favoritismo (C7):** `agotada` sale en la cálida (hub 317), en la fría (reacción 117), en la tibia y la fría visitadas (interc. 5) y en el final malo común. `determinada` sale dos veces en escenas comunes (188, 509) y una en la cálida (71).

**PixAI:** no hace falta ningún prompt: no hay 🎨 ni ➕.

---

## 7. Cambios por archivo (antes → después)

Solo cambia el atributo de expresión. La posición (`at …`), el `with` y el orden se quedan igual. Sin ternarios. Las 10 se pueden aplicar ya: no hacen falta sprites nuevos.

**`02_cap1_Ichika.rpy`**
```renpy
# l. 262
    show ichika agotada at pj_calla(0.5)
# →
    show ichika sonriendo at pj_calla(0.5)
```

**`02_cap1_conexiones.rpy`**
```renpy
# l. 670 (label queja_ichika)
    show ichika at pj_calla(0.5)
# →
    show ichika sonriendo at pj_calla(0.5)

# l. 3425 (label cap1_interconexion_6)
    show ichika sonriendo at pj_calla(X_ICHIKA)
# →
    show ichika neutral at pj_calla(X_ICHIKA)
```

**`02_cap1_evento6.rpy`**
```renpy
# l. 2599 (label e6_ichika_tarde_calida)
    call e6_foco("ichika", "sonriendo")
# →
    call e6_foco("ichika", "neutral")
```

**`02_cap1_final_malo.rpy`**
```renpy
# l. 554
    show ichika neutral at pj_habla(X_ICHIKA)
# →
    show ichika agotada at pj_habla(X_ICHIKA)

# l. 593
    show ichika neutral at pj_habla(X_ICHIKA)
# →
    show ichika agotada at pj_habla(X_ICHIKA)

# l. 739
    show ichika sonriendo at pj_habla(0.5)
# →
    show ichika agotada at pj_habla(0.5)

# l. 945 (formación de la tarde)
    show ichika neutral at pj(X_ICHIKA) 
# →
    show ichika agotada at pj(X_ICHIKA) 

# l. 960
    show ichika neutral at pj_calla(X_ICHIKA)
# →
    show ichika agotada at pj_calla(X_ICHIKA)

# l. 1285
    show ichika neutral at pj_habla(0.5)
# →
    show ichika agotada at pj_habla(0.5)
```

**Cómo probarlo (después de aplicar).** Desde la consola (Shift+O). Las etiquetas que terminan en `return` te devuelven al menú principal al acabar: sirven solo para ver la cara.
- **Hub (262):** `jump hub_Ichika` y avanza hasta el menú. Tiene que verse con las manos juntas, atenuada, mientras el MC piensa.
- **Queja (670):** `jump queja_ichika` y avanza hasta que se va.
- **Interc. 6 (3425):** `$ destino = "itsuki"`, `$ despido_cap1 = True` y `jump cap1_interconexion_6`. Sale el clima malo, el del «Nadie se rió. Ni siquiera Ichika.».
- **E6 (2599):** `jump e6_debug` → un trío con Ichika en cálida → «Ajustes» → modo de minijuegos «saltar» → «>> Jugar Evento 6». Está en la tarde de Ichika.
- **Final malo (554, 593, 739, 945, 960 y 1285):** `jump final_malo_hub3` y avanza. La 554 y la 593 salen en el aula de la mañana, la 739 en el examen, la 945 y la 960 en el aula de la tarde y la 1285 en la despedida.
- **Lint** después de aplicar: tiene que salir limpio, salvo los dos avisos que ya había y que no tienen que ver con esto (`audio/sfx/camara.mp3` y las sentencias inalcanzables de `00_definiciones.rpy`).

---

## 8. Fuera de alcance (anotado, no propuesto)

- **Apertura l. 169, «¡Un éxito rotundo!»:** se dice sin sprite, y el narrador acaba de describir su sonrisa (l. 165). Para verla habría que insertar un `show ichika sonriendo`, y eso no es cambiar un atributo.
- **E6 l. 3963, «Yotsuba. El tuyo.»:** Ichika habla con el foco en Yotsuba. Solo afecta a una línea.
- **Bug narrativo en `02_cap1_conexiones.rpy` l. 3075–3081:** en el `elif ichika_visitada_cap1:` de la interc. 5, esas líneas repiten las 3067–3073. No es de sprites. Habría que revisarlo con el guion.
- **`neutral` ↔ `determinada` comparten silueta** (§1). Si en las pruebas al 30 % molesta, el arreglo sería una pose nueva para `determinada` (un brazo cruzado, un puño), en un 🎨 aparte.
- **`show` que repiten la cara.** Candidatos con tu regla (un `show` con atributo solo cuando cambia el sprite):
  - hub 133, 372, 414, 431 y 468;
  - conexiones 622, 986, 1114, 1208, 1796, 2320, 2858 y 3360, y 130 (`neutral` tras la reacción fría, si se quiere mantener);
  - final malo 188, 238, 532 y 984 (tras el 🔁 de la 945);
  - E6 2599, tras el 🔁 (repite el `neutral` de la 2589).

  Es la misma limpieza que se hizo con Miku, en una pasada aparte.
