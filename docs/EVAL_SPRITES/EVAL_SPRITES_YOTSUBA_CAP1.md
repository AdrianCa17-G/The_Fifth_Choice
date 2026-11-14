# Evaluación de sprites · Yotsuba · Prólogo + Capítulo 1

> Revisado sobre el árbol de trabajo actual (commit `19d226e`, con cambios sin commitear en otros archivos).
> Es una evaluación: no se tocó ningún `.rpy`. Los números de línea son los de hoy.
> **Estado (14/11/2026):** aprobada entera. Los 3 🔁 del §8 están aplicados (hub 312, conexiones 2831 y 3391) y el Lint sale limpio. El ➕ también está aplicado: `yotsuba_seria.png` está normalizado, la declaración va en `00_definiciones.rpy` l. 278 y las 8 sentencias están cambiadas. Lint limpio.
> **El lienzo de `seria` mide 760 × 980, no 930.** Con los ojos en la fila 199, la cinta no cabía. Se normalizó con `normalizar_sprite.py --extra-arriba 50` y después `limpiar_halo.py --solo-halo`. Queda la misma IPD (77,2) y la misma distancia de los ojos al borde de abajo (731 px). Como `pj` ancla por abajo, en pantalla los ojos y el tamaño de la cabeza coinciden con los de las hermanas; los 50 px de más son espacio para la cinta.
> Fuentes: `docs/GUIA_ARTE.md` §1, §2, §3, §6 y §9 · `docs/GUIA_RENPY.md` §1 («Las expresiones son atributos») y §2 (la regla del `show`) ·
> `docs/REVISION_PERSONAJES_CAP1/REVISION_YOTSUBA_CAP1.md` (manda sobre cualquier propuesta) ·
> `docs/CAPITULO_1/HUBS_HERMANAS/CAP1_evento_yotsuba.md` (guion del hub y sus notas de arte) · `docs/CAPITULO_1/EVENTO_6/` ·
> `docs/EVAL_SPRITES/EVAL_SPRITES_NINO_CAP1.md`, `…_MIKU_CAP1.md` y `…_ITSUKI_CAP1.md` (formato y criterios) · los seis `.rpy` del recorrido ·
> `10_mj_yotsuba.rpy` y `11_e6_debug.rpy` para el E6.

---

## 0. Avisos: dónde el encargo y los archivos no dicen lo mismo (mandan los archivos)

| # | El encargo dice | Los archivos dicen | Qué hice |
|---|---|---|---|
| 1 | Las evaluaciones de Nino, Miku e Itsuki están «aprobadas y aplicadas» | **Itsuki solo está aplicada a medias.** El 🎨 (`itsuki_sonriendo.png` rehecho) sí está. Los **11 🔁 de su §8 no están en el código**: por ejemplo, `02_cap1_apertura.rpy` l. 81 sigue con `show itsuki molesta at pj(0.5)` y `02_cap1_final_malo.rpy` l. 572 con `show itsuki molesta at pj_habla(X_ITSUKI)`. | Lo dejo anotado y no lo toco. Esos 11 cambios siguen esperando tu aprobación. |
| 2 | E6: 0 shows, 113 líneas | Es literal: `02_cap1_evento6.rpy` no tiene ningún `show yotsuba`. Pero la pinta con **28** `call e6_foco("yotsuba", …)`, **2** `call e6_formacion_neutral` (l. 259 y 2178) y **1** `call e6_entrar(e6_h)` (l. 3286). Las 113 líneas son **66** `yotsuba` + **47** `yotsuba_int`. | Evalué los 31. Diagnóstico en §3. |
| 3 | 105 shows · sonriendo 43 · incomoda 26 | Cuadra: hay **105** `show yotsuba` (prólogo 6 · apertura 4 · hub 18 · conexiones 62 · final malo 15). **82** llevan atributo (sonriendo 43 · incomoda 26 · neutral 9 · sorprendida 4) y **23** son de solo tinte (`show yotsuba at pj_calla(…)`). | Uso esas cifras. Los de tinte van dentro del momento que los contiene. |
| 4 | LoRA de serie ≤0.3 y LoRA individual 0.7–0.8 | `GUIA_ARTE.md` §1, «Pesos de LoRA»: sprite individual de una hermana → **sin LoRA de serie** y personaje a **0.8**. El 0.3 / 0.7–0.8 es para un **CG** individual. Es el mismo aviso que en Nino e Itsuki. | El prompt del §7 va sin LoRA de serie y con el de Yotsuba a 0.8. |
| 5 | Chaleco amarillo, lazo verde al cuello, medias oscuras hasta la rodilla | §2: «Chaleco amarillo, camisa blanca de manga corta, lazo verde a cuadros». El lazo a cuadros en el cuello sale en los cuatro PNG. **Las medias oscuras no salen en la GUIA ni en ningún PNG**: el lienzo corta a medio muslo. | Van en el prompt para que no haya incoherencias; el recorte las deja fuera. Convendría añadirlas a la ficha de §2 (no lo hice). |
| 6 | — | **El guion del hub pedía otro `neutral`.** `CAP1_evento_yotsuba.md` l. 537: «`yotsuba_neutral` · Sin la sonrisa». Las l. 559–563 dicen que la diferencia tenía que ir en la postura: «hombros ligeramente menos abiertos, mirada un punto más baja». **El PNG que existe sonríe** (sonrisa cerrada y suave) y tiene los brazos colgando, como `sonriendo`. El código escrito después, sobre todo el E6, ya usa `neutral` como esa sonrisa tranquila. | Mandan los archivos: `neutral` es la sonrisa suave. Por eso la cara sin sonrisa la propongo como ➕ y no como 🎨 de `neutral` (§1 y §7). |
| 7 | La cinta cortada arriba ya está anotada en GUIA §9 | Confirmado: §9, «El lazo de Yotsuba viene cortado en el propio render». | No la cuento como hallazgo. El prompt del §7 pide margen arriba. |

---

## 1. Ficha de los 4 sprites

Los cuatro son PNG RGBA de 760×930. Están declarados en `00_definiciones.rpy` l. 274–277.

| Sprite | Pose y brazos | Mirada | Boca | Lo que transmite de verdad | Lo que NO cubre |
|---|---|---|---|---|---|
| `yotsuba neutral` | De frente. **Brazos colgando** un poco separados del cuerpo, con las manos sueltas en el bajo de la falda. | Párpados algo caídos, tranquila, de frente. | **Sonrisa cerrada y suave.** Rubor leve. | Calma amable, la sonrisa a media potencia: la que «tardó un poco más en llegar», la sinceridad en voz baja. En Yotsuba, el reposo ya sonríe. | **Cualquier momento sin sonrisa.** Tampoco nervios ni euforia. |
| `yotsuba sonriendo` | **Brazos colgando, algo más abiertos**, con las manos junto a la falda. Cabeza un poco ladeada. | Ojos brillantes, muy abiertos, de frente. | **Sonrisa amplia con los dientes.** Rubor. | Alegría abierta y sincera. Las cejas están relajadas: no hay ninguna tensión en la cara. | La sonrisa forzada **por sí sola** (ver la pregunta clave). Tampoco calma ni tristeza. |
| `yotsuba incomoda` | **Manos escondidas a la espalda.** Es la silueta más estrecha del set (GUIA §9: «`yotsuba incomoda` ocupa menos ancho»). | Cejas algo alzadas y preocupadas. | **Sonrisa cerrada y torpe.** Rubor fuerte. | Apuro, nervios, que la pillen, culpa, defender a alguien y cortarse. Es la sonrisa que se tensa pero no se va. También vale para la vergüenza de dar las gracias. | La cara sin sonrisa. La tristeza seria. |
| `yotsuba sorprendida` | **Puño derecho alzado a la altura del hombro**; el brazo izquierdo cuelga. Es la única asimétrica. | Ojos muy abiertos. | Pequeña, en «o». | Sobresalto, el frenazo en seco, el «¡Espera!». | Todo lo contenido. No vale para el silencio aturdido de alguien que se queda pensando. |

**Regla de §9 (a un 30 % solo se lee la silueta):**

- **`neutral` ↔ `sonriendo`: es el par confundible.** Las dos tienen los brazos colgando. Las separan la boca (cerrada o con dientes), la cabeza ladeada y unos centímetros de apertura de brazos, y a un 30 % casi no se ve. **No propongo 🎨**, por dos motivos:
  - Todas las transiciones entre ellas son de grado: la sonrisa se ablanda o vuelve. Que se lean poco a distancia no cambia lo que pasa.
  - El único salto que tiene que verse sí o sí es la sonrisa que **desaparece**. Ese salto se lo lleva el ➕ `seria`, con silueta propia (§7).
- **`sonriendo` ↔ `incomoda`: se distinguen bien ✓.** Brazos a los lados contra brazos escondidos, y el ancho cambia mucho. Es la transición más importante del personaje, la de la grieta (queja 824, interc. 4 l. 2094 y 2328, interc. 5 l. 2870, eco cálido del E6 l. 3323), y se lee.
- **`neutral` ↔ `incomoda`: se distinguen ✓.** Por el mismo motivo.
- **`sorprendida` ↔ el resto: se distingue ✓.** Es la única con una mano alta.
- **Falta una emoción que se repite: la cara sin sonrisa.** El texto la pide en seis escenas de cuatro archivos («Sin sonrisa», «Lo dijo bajito», «No me digas que no es mi culpa»). Hoy esas líneas van con `neutral` o `incomoda`, que sonríen las dos. De ahí sale el ➕ del §7.

### La pregunta clave: ¿`sonriendo` puede leerse como sonrisa forzada?

**No. Por sí sola, `sonriendo` se lee como alegría sincera, y así tiene que seguir.**

- **La cara no tiene ninguna tensión.** Las cejas están relajadas, los ojos brillan y la boca está abierta. Nada en el dibujo dice «máscara».
- **De sus 43 usos, 24 son alegría de verdad** (prólogo 930, hub 434 y 462, reacción cálida 368 y 392, interc. 1 «¡Yo quiero jugar!», interc. 5 «¡Eso sí lo acepto!»…). Un `sonriendo` ambiguo estropearía todos esos.
- **La revisión y el guion quieren que la máscara no tenga fisuras.** La rama fría obedece «con la sonrisa intacta» (revisión §1). El guion del hub dice que es «una sonrisa buena, sin fisuras visibles» (`02_cap1_Yotsuba.rpy` l. 231). Que el jugador la descubra antes de tiempo por la cara rompería eso.

**Cómo se lee entonces la máscara: por el contexto.** De los 43 usos, **17 son máscara**, y en los 17 el texto la marca:

| Uso | Lo que la delata |
|---|---|
| Hub 249 | l. 247 «Y volvió a mirarme con esa sonrisa intacta.» · l. 260 «Cambió de tema.» |
| Hub fría 531 / 536 | l. 539 «La sonrisa era idéntica» |
| Reacción fría 431 | l. 438 «Me llamó «tutor» con el tono que se usa con un desconocido.» |
| Queja 810 / 813 / 839 | l. 853 «Se fue corriendo, con la sonrisa puesta.» · l. 855 «Pero al doblar la esquina bajó el ritmo» |
| Interc. 1, 1058 / 1063 | «...¡Digo! ¡Nada! ¡Era una broma!» después de que Nino la corte (revisión P10) |
| Interc. 4 tibia 2079 | l. 2092 «Lo dijo sonriendo. Pero la sonrisa tardó en llegar a sus ojos.» |
| Interc. 4 grupo 2279 / 2292 / 2321 | La cena sorpresa, y al momento: «...Aunque cuando sale así, es porque es un asunto serio.» |
| Interc. 5, 2861 | «estás sosteniendo tu lápiz al revés» |
| Interc. 6, 3352 / 3363 / 3384 | «¡Es un sesenta por ciento!»: infla el número porque le duele (revisión §1), e Itsuki la desinfla |

En el E6 pasa lo mismo: la fría del lunes (l. 290 «Lo dijo de corrido, sin mirar a ninguna de sus hermanas», revisión P2d), la fría de la tarde (l. 2557) y el eco frío (l. 3359 «con la sonrisa ya puesta»).

**Dónde se ve la grieta y qué cara le toca.** La grieta siempre es un **cambio de sprite**: la propia `sonriendo` nunca la lleva. Hay una escala:

| Grado | Sprite | Cuándo |
|---|---|---|
| La sonrisa se ablanda o tarda | `neutral` | Hub 364 («Su sonrisa no desapareció.»), reacción fría 442, E6 2528 y 2570 |
| La sonrisa se tensa pero sigue | `incomoda` | Queja 824, interc. 4 l. 2094 y 2328, interc. 5 l. 2870, E6 3323 y 3848. **Es la única sonrisa forzada visible del set.** En la mesa del E6 (l. 3848, «¡A todas les habrá ido genial! ¡Seguro!») es justo el ánimo forzado. |
| La sonrisa se va | **`seria` (➕)** | Interc. 4, «Sin sonrisa.» · E6 «Lo dijo bajito.» · hub y reacción cálidos · final malo |

---

## 2. Criterios aplicados (los de Nino, Miku e Itsuki, adaptados a Yotsuba)

- **C1 · La narración manda.** Si el narrador describe la cara, las manos o la voz, va el sprite que lo cumple: «Sin sonrisa» y «bajito» → **no** una cara que sonríe; «con las manos juntas delante» → **no** `incomoda`, que las tiene a la espalda; «con esa sonrisa puesta» → `sonriendo`; «cara de preocupación» → **no** `sonriendo`.
- **C2 · La escala de la grieta** (§1): `sonriendo` → `neutral` → `incomoda` → `seria`. Cada paso tiene que ser un cambio de sprite que motive una línea.
- **C3 · La máscara se lee por el contexto.** Una `sonriendo` que es máscara es ✅ si el texto la marca. No se cambia a otra cara: la revisión quiere la sonrisa «intacta». Solo se cambia cuando el texto dice que la cara **ya no** sonríe, o que sonríe y nadie más lo hace.
- **C4 · La revisión manda.** Se respetan tal cual:
  - P2d: lunes del E6, `sonriendo` en cálida, tibia y fría (en la fría, como máscara) y `neutral` en la no visitada.
  - P7: `sonriendo` en «Bueno.» / «¡Dame la mano!».
  - P10: `sonriendo` en pj_calla tras «¡Era una broma!».
  - P13: `incomoda` en el coro del prólogo.
  - R3: eco cálido, `sonriendo` → `incomoda`.
- **C5 · Parpadeo.** Nada de A → B → A en réplicas seguidas, ni cambios de cara que ninguna línea motive. Se arregla cambiando el atributo por el del vecino. Ningún `show` se borra.
- **C6 · Ramas.** En el mismo punto del guion, cálida, tibia y fría llevan caras distintas siempre que el texto lo permita.
- **C7 · Sin favoritismo visual.** Ninguna cara nueva puede ser un premio de la cálida. `seria` sale en la cálida, en la fría, en escenas que dependen de otra hermana y en el final malo. `sonriendo` no se concentra en la cálida: la fría la usa más, como máscara.

Veredictos: ✅ queda bien · 🔁 cambiar a otra expresión existente · 🎨 rehacer el sprite · ➕ sprite nuevo.

---

## 3. Evento 6: diagnóstico (mismo caso que Miku e Itsuki)

**Conclusión: el diagnóstico de Miku e Itsuki vale igual para Yotsuba.** De las 113 líneas, las **61** `yotsuba` dichas en escena tienen sprite por `e6_foco`. Las otras **52** (47 `yotsuba_int` y 5 `yotsuba`) van sobre un CG a propósito. Es el mismo diseño de `e6_mostrar_foco` (l. 91), que guarda la última cara de cada hermana y la vuelve a pintar atenuada cuando habla otra.

| Tramo (etiqueta · líneas) | Líneas de Yotsuba | Qué hay en pantalla | ¿Intencional o falta? |
|---|---|---|---|
| Lunes en el aula (`e6_lunes` · 262–304) | **15** `yotsuba`: cálida/tibia 7, fría 3, no visitada 5 | `bg_aula` (l. 256), formación neutral (l. 259) y `e6_foco` l. 264 / 282 / 294 | Sprite ✓ |
| Núcleo de Japonés (`e6_yotsuba_nucleo` · 583) | 0 | **CG `cg_yotsuba_examen`** (l. 589) | — |
| Voz interior (`e6_yotsuba_mono_<estado>` · 613–714) | **41** `yotsuba_int`: cálida 13, tibia 11, fría 10, no visitada 7 | El mismo CG | Intencional: monólogo sobre su CG |
| Minijuego (`e6_yotsuba_mj` · 717) | **6** `yotsuba_int` | El CG. Durante el juego, la screen con su **chibi** (`mj_retrato("yotsuba", …)`, `10_mj_yotsuba.rpy` l. 684) | Intencional: minijuego con chibi propio |
| Promesa y gesto (`e6_yotsuba_promesa` · 747, `e6_yotsuba_gesto_*` · 764–811) | 0 | El CG | — |
| Aula de la tarde, en grupo (`e6_despues`) | **1** `yotsuba` (2317) | `bg_aula_tarde` (l. 2175), formación (l. 2178), `e6_foco` l. 2315 | Sprite ✓ |
| Tarde por rama (`e6_yotsuba_tarde_*` · 2501–2582) | **16** `yotsuba`: cálida 5, tibia 3, fría 4, no visitada 4 | `e6_foco` l. 2503, 2513, 2524, 2528, 2534, 2545, 2564, 2570, 2576 | Sprite ✓ |
| La pregunta al MC (`e6_tarde_pregunta` · 2919) | **1** `yotsuba` (2935), todas menos la fría | `e6_foco` l. 2933 | Sprite ✓ |
| Departamento y eco (`e6_cinco` · 3286, `e6_yotsuba_eco_*` · 3307–3394) | **12** `yotsuba`: cálida 4, tibia 3, fría 2, no visitada 3 | `bg_departamento` (l. 3258), entra neutral (`e6_entrar`, l. 3286), `e6_foco` l. 3311, 3319, 3323, 3338, 3346, 3361, 3380 | Sprite ✓ |
| La disculpa interrumpida (`e6_intento` · 3756) | **1** `yotsuba` (3788) | `e6_foco` l. 3786 | Sprite ✓ |
| Mesa (`e6_mesa` · 3810–4081) | **15** `yotsuba` | `e6_foco` l. 3848, 3902, 3955, 3967, 3973, 4067 | Sprite ✓ |
| Foto (l. 4104–4171) | **5** `yotsuba` (4129, 4133, 4153, 4155, 4171) | **CG `cg_cinco_aprobadas`** (l. 4104 / 4109 / 4114, según el tinte) | Intencional: CG de las cinco |
| Chat del grupo (`e6_cuarto` · 4287) | 0 líneas de diálogo | `bg_cuarto_mc` + screen | Intencional: interfaz |

Cuenta: 15 + 1 + 16 + 1 + 12 + 1 + 15 = **61** con sprite · 41 + 6 = **47** `yotsuba_int` sobre CG · **5** `yotsuba` sobre CG. Total, **113** ✓.

**Excepciones, solo de expresión (no de diseño):**

- **l. 2315, «…Es que si salimos por esa puerta, se acaba la semana.»** Es su único foco en el aula de la tarde, y `incomoda` sonríe mientras el narrador dice «Lo dijo bajito». Es un ➕ (§5).
- **Eco frío, l. 3359.** `e6_entrar` la mete en `neutral` antes de que hable, y el narrador dice «con la sonrisa ya puesta» una línea antes del `e6_foco` en `sonriendo` (l. 3361). Como `neutral` ya sonríe un poco, no choca. Lo anoto en el §9 y no propongo nada.

---

## 4. Líneas de Yotsuba sin sprite fuera del E6

| Archivo · líneas | Qué hay en pantalla | ¿Intencional? |
|---|---|---|
| `01_prologo.rpy` 775 | `bg_departamento` con Nino: la voz llega de fuera de cuadro y el CG empieza en la l. 777 | Sí, entra en escena |
| `01_prologo.rpy` 784–808 | CG `cg_yotsuba_corriendo` (l. 777) | Sí, es CG |
| `01_prologo.rpy` 1154, 1162 | CG `cg_hermanas_estudiando` (l. 1131) | Sí, es CG |
| `02_cap1_apertura.rpy` 192 | CG `cg_cinco_sentadas` (l. 179) | Sí, es CG |
| `02_cap1_Yotsuba.rpy` 64–79 | CG `cg_yotsuba_pista` (l. 49) | Sí: el guion la quiere de espaldas, sin que se le vea la cara |
| `02_cap1_Yotsuba.rpy` 157–203 | CG `cg_yotsuba_rotulador` (l. 146) | Sí, es CG |
| `02_cap1_Yotsuba.rpy` 291, 301 | CG `cg_yotsuba_cronometro` (l. 270) | Sí, es CG |
| `02_cap1_conexiones.rpy` 3835, 3839 (clima buena), 3879 (mixta), 3919 (mala) | `bg_departamento` / `bg_departamento_anochecer` (l. 3796 / 3801), **sin ninguna hermana** | La misma decisión de escena que en Miku e Itsuki: en esa despedida no hay sprite para ninguna de las cinco (§9) |

---

## 5. Tabla por archivo

Un momento es el `show` (o `e6_foco`) donde cambia la expresión, más las líneas de Yotsuba que cubre. Los `show yotsuba at …` de solo tinte, y los que repiten la misma cara, van en el momento que los contiene. ➕ = pasa al sprite nuevo `seria` (§7).

### 01_prologo.rpy (6 shows)

| archivo:línea | Rama / escena | Diálogo (resumido) | Actual | Veredicto | Propuesta | Por qué |
|---|---|---|---|---|---|---|
| 930 (+933, 941, 971, 983) | Departamento, se entera de que ya se conocían | «¡O sea que ya se conocían! ¡Qué coincidencia tan increíble!» · «¡Eso significa que ya tenemos la mitad del camino completado!» | sonriendo | ✅ | — | Alegría sincera y despistada: no ve que se están matando con la mirada, y Nino se lo dice en la réplica siguiente |
| 1054 | Coro «¡No pensamos estudiar!» | (línea de `quintillizas`) | incomoda | ✅ | — | C4: revisión P13. l. 1062 «Yotsuba también. Medio tono más bajo que las demás.» |

### 02_cap1_apertura.rpy (4 shows)

| archivo:línea | Rama / escena | Diálogo (resumido) | Actual | Veredicto | Propuesta | Por qué |
|---|---|---|---|---|---|---|
| 302 (+308, 314, 319) | Departamento, defiende al MC de Nino | «Nino, eso no es justo. Él solo está—» · «...No dije nada.» | incomoda | ✅ | — | Apuro de verdad: la cortan y se arrepiente. l. 322 «Iba a defenderme. Y se arrepintió a mitad de frase.» |

### 02_cap1_Yotsuba.rpy (18 shows · hub con ramas)

`yotsuba_m4a` = cálida · `yotsuba_m4b` = tibia · `yotsuba_m4c` = fría. Hasta la l. 338 es común a las tres.

| archivo:línea | Rama / escena | Diálogo (resumido) | Actual | Veredicto | Propuesta | Por qué |
|---|---|---|---|---|---|---|
| 101 | Común · la pillan en la pista | «…» | sorprendida | ✅ | — | l. 104 «Se paró en seco a mitad de la pista.» El guion pide el frenazo con los ojos abiertos |
| 114 | Común | «¡No estaba hablando sola! ¡Estaba haciendo técnica de concentración mental!» · «¡Lo dijeron en un documental de la tele!» | incomoda | ✅ | — | La han pillado contando en voz alta: apuro de verdad |
| 129 | Común | «…¿Cuánto llevas tú, [mc]?» · «Eso es mucho tiempo.» | neutral | ✅ | — | l. 127 «Pausa.» La exclamación se le apaga. Es el primer grado de la grieta |
| 218 | Común · tras el CG del rotulador | «Mis hermanas son mejores que yo en casi todo.» · «Yo corro y animo. Así que lo hago lo mejor que puedo.» | neutral | ✅ | — | Lo dice como un dato (revisión §5), con la sonrisa suave. l. 231 «Sonrió.» tiene que poder crecer desde aquí. Que el `show` de la sonrisa llegue en la 249 lo anoto en el §9 |
| 249 | Común | «¡Bueno!» · «¡Soy más rápida cuando alguien mira!» · «¡Vamos, no hay tiempo que perder! ¡El sol no espera!» | sonriendo | ✅ | — | Máscara, marcada por el texto (C3): l. 247 «esa sonrisa intacta», l. 260 «Cambió de tema.» |
| 312 | Común · antes del menú | (sin líneas; el MC piensa «con esa sonrisa puesta») | neutral | 🔁 | **sonriendo** | C1: l. 305 «Después volvió a su sitio, como si nada.», l. 315 «se lo va a llevar igual: con esa sonrisa puesta». La sonrisa se torció en el CG y **ya volvió**. Con `neutral`, el jugador ve la grieta que el texto dice que se acaba de tapar. Las tres ramas arrancan desde la máscara: la cálida la rompe, la tibia la deja y la fría la confirma |
| 351 | Cálida | «¿Antes de qué?» · «¡Sí! ¡Pero eso no es malo! ¡Cada una tiene lo suyo!» · «¡Y yo tengo lo mío!» | sorprendida | ✅ | — | No esperaba que él volviera a lo que dijo |
| 364 | Cálida | «…¿Qué me salté?» · «Estaba un poco más callada que de costumbre.» · «Es que siempre lo deja en el mismo sitio después de leerlo.» | neutral | ✅ | — | Es la definición de `neutral`: l. 367 «Su sonrisa no desapareció.», l. 369 «Pero tardó un poco más en llegar.» |
| 389 | Cálida | «Oye, [mc]… ¿Me estabas observando?» · «Eso que describes no es nada especial.» · «Cualquiera lo haría.» | incomoda | ✅ | — | La pillan siendo vista: apuro de verdad |
| 402 | Cálida · la máscara cae | «…Pero eso no entra en ningún examen.» · «…» | sorprendida | ➕ | **seria** | C1: empieza con «…», en voz baja, y lo que sigue es l. 415 «No dijo nada. Miraba la pista, pero no la pista de verdad.» y l. 423 «Pasó un momento largo.» `sorprendida`, con el puño alto y la boca en «o», es un sobresalto, no ese silencio. **Es el momento en que la cálida baja la máscara** (pregunta e), y con `seria` deja la sonrisa del todo. Después vuelve por grados: seria → neutral (425) → sonriendo (434) |
| 425 | Cálida | «No sé si eso es verdad o si eres muy bueno animando a la gente.» | neutral | ✅ | — | La sonrisa vuelve a medias, con duda. Con el ➕ de la 402 este cambio por fin se ve |
| 434 (+441) | Cálida | «…Eso también es verdad.» | sonriendo | ✅ | — | Sonrisa sincera. l. 450 «Ahora la cuenta la llevábamos entre dos.» |
| 462 (+504) | Tibia | «¡Genial! ¡Preparado!» · «¡Siempre! Las piernas me avisan.» · «¡Mi cabeza va a donde van las piernas! ¡Equipo completo!» · «¡Otra vuelta! ¡Esta va a ser mejor!» | sonriendo | ✅ | — | La tibia se ríe y esquiva. l. 492 «Era una risa fácil, sin trampa.» Tras el 🔁 de la 312, el `show` no cambia nada en pantalla, y es correcto: la tibia no rompe la máscara |
| 524 | Fría | (sin líneas) | incomoda | ✅ | — | l. 529 «como quien recibe una instrucción». Las manos a la espalda son, literalmente, la postura de recibir una orden. Es la única grieta de la fría, y dura dos líneas del narrador |
| 531 (+536) | Fría | «¡Tienes razón! ¡Eso estaba haciendo! ¡Qué bueno que lo entiendas!» | sonriendo | ✅ | — | Máscara (C3): l. 539 «La sonrisa era idéntica». Con el 🔁 de la 312, es idéntica de verdad a la de antes del menú |

### 02_cap1_conexiones.rpy (62 shows)

| archivo:línea | Rama / escena | Diálogo (resumido) | Actual | Veredicto | Propuesta | Por qué |
|---|---|---|---|---|---|---|
| 368 | Reacción · cálida | «¡Buenos días, [mc]!» · «¡Veinticinco! ¡Es un número perfecto!» · «¡Para mí sí!» | sonriendo | ✅ | — | Alegría sincera: le sigue el chiste del número |
| 383 | Reacción · cálida | «...Ayer dijiste que mi punto de partida no era cero.» · «Anoche no pude dejar de pensarlo.» · «Nadie me había dicho algo así sin pedirme que sonriera.» | neutral | ➕ | **seria** | C1: la frase habla de no tener que sonreír, y el sprite sonríe. Es el segundo momento sin máscara de la cálida (pregunta e). Luego `sonriendo` en «Bueno.» (392, revisión P7) es la sonrisa que vuelve sola |
| 392 | Reacción · cálida | «Bueno.» · «¡Dame la mano!» · «¡Listo! ¡Ahora tú también llevas la cuenta!» | sonriendo | ✅ | — | C4: revisión P7 |
| 405 (+410) | Reacción · cálida | «¡No es un corazón! ¡Es... una vuelta!» | incomoda | ✅ | — | La pillan con el corazón torcido: apuro de verdad |
| 415 (+426) | Reacción · tibia | «¡Mira! ¡Un minuto con catorce!» · «¡Es mi cuaderno oficial!» | sonriendo | ✅ | — | Sincera: la tibia se queda con el cronómetro |
| 431 | Reacción · fría | «¡Buenos días, tutor!» · «¡Hoy voy a concentrarme en correr!» | sonriendo | ✅ | — | Máscara (C3): l. 438 «Me llamó «tutor» con el tono que se usa con un desconocido.» |
| 442 (+449) | Reacción · fría | «¡Tenías razón! ¡Correr es lo mío!» · «...Hoy serán cuarenta vueltas. ¡Cuarenta!» | neutral | ✅ | — | Infla el número (revisión §1) y la sonrisa baja un grado. l. 452 «No me miró mientras lo hacía.» La fría no llega a `seria`: obedece |
| 810 (+813) | Queja (no visitada) | «¡No pasa nada! ¡De verdad!» · «¡Tres tardes no alcanzan para cinco!» · «¡Te lo digo en serio!» | sonriendo | ✅ | — | Máscara, marcada por la propia insistencia y por la l. 853 |
| 824 | Queja | «...Aunque estuve entrenando por si venías.» · «Me quedé quince minutos más cada tarde. Los conté.» · «Y si nadie me necesita, ¿para qué me sobra tanta energía?» | incomoda | ✅ | — | La grieta: la sonrisa se tensa pero no se va (C2) |
| 839 (+850) | Queja | «¡Pero no importa! ¡Me sobra, así que la reparto!» · «¡La tercera la corro ahora mismo!» | sonriendo | ✅ | — | La máscara vuelve. l. 853 «Se fue corriendo, con la sonrisa puesta.» (revisión P9) |
| 970 (+989, 1012, 1019) | Interc. 1 · descanso, las cinco | «¿Un método efectivo? ¡Guau!» · «¿Y qué es? ¡Quiero saberlo! ¡Quiero saberlo!» | sonriendo | ✅ | — | Entusiasmo sincero |
| 1046 (+1052) | Interc. 1 | «¡Nino! Seguro no es eso. Él solo—» | incomoda | ✅ | — | Lo defiende y la cortan, igual que en la apertura |
| 1058 (+1063, 1075, 1090) | Interc. 1 | «...¡Digo! ¡Nada! ¡Era una broma!» | sonriendo | ✅ | — | C4: revisión P10. Máscara: la puesta a toda prisa |
| 1141 (+1146) | Interc. 1 | «¿Estilo quintillizas? ¡Hurra! ¡Yo quiero jugar!» | sonriendo | ✅ | — | Sincera |
| 1215 (+1220) | Interc. 1 | «¿Y elegirás a la que quieras conocer mejor? ¿O no?» | incomoda | ✅ | — | Vergüenza de preguntarlo: la esperanza que no se atreve a decir. El rubor fuerte de `incomoda` lo cubre |
| 1745 (+1754, 1776) | Interc. 3 · aula | fría «¡Buenos días, tutor! ¡Tienes cara de cansado!» / resto «¡Es un cumplido! ¡Los osos son fuertes!» | sonriendo | ✅ | — | Sincera en el resto. En la fría es máscara, marcada por la l. 1766 «Lo dijo mirando la pizarra.» El `show` es común (§9) |
| 2032 | Interc. 4 · se le cruza en el aula | (entrada, solo si el destino no es Yotsuba) | sonriendo | ✅ | — | Llega con algo que contar. Cada rama cambia la cara enseguida |
| 2037 (+2074) | Interc. 4 · cálida de la otra | «¡Es un secreto! ¡Rápido!» · «Que lo que le dijiste, o lo que hiciste, le dejó algo bueno por dentro.» · «Gracias por no rendirte con ella. ¡Es todo!» | sonriendo | ✅ | — | Sincera. l. 2072 «Se fue dando saltitos, igual que siempre.» |
| 2079 | Interc. 4 · tibia de la otra | «¡Y eso está bien! ¡A veces igual es lo mejor que se puede pedir!» | sonriendo | ✅ | — | Máscara, marcada: l. 2092 «Pero la sonrisa tardó en llegar a sus ojos.» |
| 2094 (+2103) | Interc. 4 · tibia de la otra | «...Es que no sé si le sirvió o no. Y eso me da un poco de cosa.» · «Porque yo siempre sé. Y esta vez, no.» | incomoda | ✅ | — | La grieta (C2) |
| 2108 (+2137) | Interc. 4 · fría de la otra | «¿Tienes un minuto?» · «Yo la conozco, y tal vez lo que le dijiste... le dolió.» · «Te lo digo porque ella nunca lo va a decir.» · «Arréglalo. Por favor.» | incomoda | ➕ | **seria** (también la 2137) | C1, el caso más claro: l. 2119 «Lo dijo sin levantar la voz. Sin sonrisa.» y l. 2121 «era la primera vez que la veía así» (revisión P2b). `incomoda` sonríe. La 2137 (pj_calla) también pasa a `seria`; si no, vuelve a sonreír al acabar «Arréglalo. Por favor.» |
| 2279 (+2292, 2321) | Interc. 4 · Nino se ha ido | «¡Seguro se reunirán en nuestra casa!» · «Ya sé. ¡Nos planean hacer una cena sorpresa!» | sonriendo | ✅ | — | Optimismo que tapa la preocupación (C3). La grieta llega en la réplica siguiente |
| 2328 (+2333, 2342, 2361) | Interc. 4 | «...Aunque cuando sale así, es porque es un asunto serio.» · «...Puede que sea culpa mía.» · «Nino lo leyó y se fue.» | incomoda | ✅ | — | Preocupación y culpa, con la sonrisa tensa. Sigue hablando con todas delante: no llega a `seria` |
| 2831 | Interc. 5 · víspera de exámenes | (sin líneas; l. 2849 «Me quedaron viendo con cara de preocupación.») | sonriendo | 🔁 | **incomoda** | C1: el MC dice que las cinco lo miran preocupadas, y Yotsuba es la única que sonríe de oreja a oreja. Con `incomoda`, la máscara **se pone delante del jugador** en la 2861 («súper tranquilas») y se cae en la 2870. Es la mejor respuesta a la pregunta clave: la sonrisa se lee como forzada porque se ve llegar |
| 2861 | Interc. 5 | «¡Eh, nosotras estamos súper tranquilas! ¡Para nada nerviosas!» · «¡Es una técnica! ¡Para aliviar los nervios!» | sonriendo | ✅ | — | Máscara, delatada por el lápiz al revés |
| 2870 | Interc. 5 | «...Bueno. Si te soy sincera...» · «Es que si alguna de nosotras reprueba, se acaba todo.» · fría «Porque las demás confían en ti.» | incomoda | ✅ | — | La grieta: nervios de verdad |
| 2893 (+2898, 2915, 2920, 3112) | Interc. 5 | «...¡Eso sí lo acepto!» · «¡Una materia para cada una! ¡Como un equipo de relevos!» | sonriendo | ✅ | — | Sincera |
| 3352 (+3363, 3384) | Interc. 6 · se acaba el juego | «¡Pero tres de cinco es más de la mitad! ¡Es un sesenta por ciento!» · «¡Un sesenta es un buen número!» | sonriendo | ✅ | — | Máscara: infla el número porque le duele (revisión §1) |
| 3391 | Interc. 6 · Itsuki la desinfla | (sin líneas; Itsuki: «Es un aprobado a medias, Yotsuba.») | sonriendo | 🔁 | **incomoda** | C1 y C5: hoy sigue sonriendo de oreja a oreja hasta el final de la escena, unas 190 líneas. En la mixta y la mala eso incluye «Solo has empeorado las cosas.» / «Todas lo sabemos.» (Nino) y l. 3582 «Nadie se rió.» Con `incomoda`, la grieta llega cuando Itsuki le corrige el número, que es donde duele. En la buena vuelve a `sonriendo` en la 3527 con su propia línea |
| 3527 | Interc. 6 · clima buena | «¡Va a salir bien! ¡Lo presiento!» · «¡[mc] ha hecho un buen trabajo con sus tutorías!» | sonriendo | ✅ | — | Sincera |
| 3534 (+3539) | Interc. 6 · clima buena | «En verdad te lo agradecemos mucho.» | incomoda | ✅ | — | Baja la voz para decir la verdad (revisión §1, su marca es el volumen). La vergüenza de dar las gracias, con rubor |

### 02_cap1_evento6.rpy (0 `show` + 28 `e6_foco` + 2 `e6_formacion_neutral` + 1 `e6_entrar`)

| archivo:línea | Rama / escena | Diálogo (resumido) | Actual | Veredicto | Propuesta | Por qué |
|---|---|---|---|---|---|---|
| 259 | Lunes · formación | (sin líneas) | neutral | ✅ | — | Formación común de las cinco |
| 264 | Lunes · cálida/tibia | «¡Estudié las lecturas dos veces!» · «¡Voy a llegar a la meta, y las cinco juntas!» | sonriendo | ✅ | — | C4: P2d. Sincera |
| 282 | Lunes · fría | «¡Hoy me concentro en lo mío! ¡Nada más!» | sonriendo | ✅ | — | C4: P2d. Máscara, l. 290 «Lo dijo de corrido, sin mirar a ninguna de sus hermanas.» |
| 294 | Lunes · no visitada | «…Mis lecturas, para después. Siempre se quedan para después.» · «¡Pero lo intentaré con toda la energía que me queda!» | neutral | ✅ | — | C4: P2d. La sonrisa a media potencia de quien se deja para el final |
| 2178 | Aula de la tarde · formación | (sin líneas) | neutral | ✅ | — | Formación común |
| 2315 | Aula de la tarde | «…Es que si salimos por esa puerta, se acaba la semana.» | incomoda | ➕ | **seria** | C1: l. 2319 «Lo dijo bajito. Yotsuba, que no dice nada bajito.» Es su marca de decir la verdad (revisión §1). Sin sonrisa, y se queda así, atenuada, mientras «Nadie contestó» (l. 2353) |
| 2503 | Tarde · cálida | «[mc]…» · «Yo sí sé una cosa.» · «Llené la hoja.» | neutral | ✅ | — | Sinceridad en voz baja |
| 2513 | Tarde · cálida | «No sé si está bien. Pero esta vez la hoja también era mía.» | sonriendo | ✅ | — | Alegría sincera. l. 2517 «Lo dijo sin gritar» habla de la voz, no de la cara |
| 2524 | Tarde · tibia | «¡[mc]! ¡Yo sí sé una cosa! ¡Terminé la hoja entera!» | sonriendo | ✅ | — | — |
| 2528 | Tarde · tibia | «Bueno… casi entera. Hubo una frase que empecé y no terminé.» | neutral | ✅ | — | Pequeña grieta, un grado (C2) |
| 2534 | Tarde · tibia | «¡Una que no venía en el examen!» | sonriendo | ✅ | — | Esquiva con una risa (l. 2538). A → B → A, pero cada cambio va con su línea |
| 2545 | Tarde · fría | «¡Tutor! ¡Hoja llena! ¡Sin mirar a nadie ni una sola vez!» · «¡Es lo que mejor sé hacer! Lo sé.» | sonriendo | ✅ | — | Máscara: l. 2557 «Me sonrió a mí. Hacia sus hermanas no giró la cabeza.» |
| 2564 | Tarde · no visitada | «¡[mc]! ¡Le pasé un lápiz a Ichika antes de que lo pidiera!» | sonriendo | ✅ | — | — |
| 2570 | Tarde · no visitada | «…¿Tú me viste? Desde la segunda fila.» | neutral | ✅ | — | Pequeña grieta |
| 2576 | Tarde · no visitada | «¡Entonces ya está!» | sonriendo | ✅ | — | l. 2580 «Le bastaba con que alguien hubiera mirado.» |
| 2933 | Pregunta al MC · todas menos la fría | «¡Espera! ¡Falta uno! ¿Y a ti cómo te fue, [mc]?» | sorprendida | ✅ | — | Se le ocurre de golpe |
| 3286 | Departamento · entra | (sin líneas) | neutral | ✅ | — | Entrada común. En la fría hay un roce de una línea (§3) |
| 3311 | Eco · cálida | «Dame la muñeca. El uno se borró hace días.» · «Empecé en el uno por ciento. Todavía no sé dónde estoy. Pero ya cabe.» | neutral | ✅ | — | Sinceridad tranquila |
| 3319 | Eco · cálida | «¡Esta vez sin corazón torcido!» | sonriendo | ✅ | — | C4: R3 |
| 3323 | Eco · cálida | «…Todavía no me sale recto. Lo estoy practicando.» | incomoda | ✅ | — | C4: R3. Vergüenza tierna, con rubor |
| 3338 | Eco · tibia | «Un minuto con catorce. Eso lo sé. Lo demás, no tanto.» · «No sé si me ayudaste o solo me dejaste correr.» | neutral | ✅ | — | — |
| 3346 | Eco · tibia | «¡Equipo completo! ¡Piernas y cabeza!» | sonriendo | ✅ | — | l. 3350 «Esta vez no sonó a chiste.» Sincera |
| 3361 | Eco · fría | «¡Terminé primera! ¡Eso es bueno! Lo mío es terminar.» · «¡Está bien! ¡De verdad! Hoy no hace falta contar nada.» | sonriendo | ✅ | — | Máscara, marcada dos veces: l. 3359 y l. 3369 «Una de las dos sobraba.» |
| 3380 | Eco · no visitada | «¡Hola, [mc]! ¡No hace falta que digas nada! Tengo tres vueltas de ventaja.» · «¡Entonces las guardo!» | sonriendo | ✅ | — | Máscara: l. 3378 «con la cara con la que se mira una pista vacía» va **antes** del foco. La cara vacía queda en la entrada (`neutral`) y la sonrisa se pone al hablar |
| 3786 | La disculpa interrumpida | «¡¡Esperen!! ¡Antes de que se arruguen! ¡Los boletines! ¡Ya están en la mesa!» | sonriendo | ✅ | — | — |
| 3848 | Mesa, antes de abrir | «¡A todas les habrá ido genial! ¡Seguro!» · «…Pero si a mí no me fue bien, ¡que nadie ponga cara de puchero, eh!» | incomoda | ✅ | — | El ánimo forzado: la sonrisa tensa de `incomoda` es justo eso |
| 3902 | Mesa | «¡¡Entonces abrámoslos ya!!» | sonriendo | ✅ | — | — |
| 3955 | Mesa · los boletines | «¡Todas! ¡¡Todas, todas, todas!!» · «¡¡Miku, mira el tuyo!! ¡¡Nino, el tuyo!!» · «¿Eh? …¡Ah, el mío!» | sonriendo | ✅ | — | Alegría sincera por las demás |
| 3967 | Mesa | «…Este es mi boletín. …Esta soy yo. …Esto lo hice yo.» | neutral | ✅ | — | l. 3969 «por primera vez en todo el mes, Yotsuba se quedó callada». Es emoción tranquila, no tristeza: la sonrisa suave sirve. `seria` sería un error aquí |
| 3973 | Mesa | «¡¡Y lo hicimos todas!! ¡¡Y tú también, [mc]!!» · fría «¡Tú te quedaste hasta el último momento! ¡Eso también cuenta!» | sonriendo | ✅ | — | — |
| 4067 | Mesa · la foto | «¡Cada una, muestre su examen! ¡Y nos tomaremos una foto!» · «¡Más arriba! ¡El mío más arriba!» | sonriendo | ✅ | — | — |

### 02_cap1_final_malo.rpy (15 shows)

| archivo:línea | Rama / escena | Diálogo (resumido) | Actual | Veredicto | Propuesta | Por qué |
|---|---|---|---|---|---|---|
| 176 (+189) | Despido A · sala | «¡Se oyó hasta la escalera!» · «¿Quién gritaba? ¿Fue...?» | sorprendida | ✅ | — | l. 186 «Se detuvo al verme la cara.» |
| 239 (+245) | Despido A | «Pero si él... él solo estaba...» | incomoda | ✅ | — | Lo defiende y Nino la corta, como en la apertura |
| 251 | Despido A | «...No dije nada.» | incomoda | ➕ | **seria** | C1: l. 256 «Se quedó mirando el suelo, con las manos juntas delante.» `incomoda` tiene las manos **a la espalda** y sonríe. La pose de `seria` es esa frase (§7). Es el eco de la apertura, pero esta vez sin la sonrisa: así se nota cuánto ha cambiado todo |
| 262 (+272) | Despido A · fría | «Me dijiste que me concentrara en correr.» · «Dejé de contar en voz alta. Pensé que así servía más.» · «Ahora no sé si servía de algo.» | neutral | ➕ | **seria** | Con la 251 en `seria`, dejarla en `neutral` le devolvería la sonrisa justo en el reproche más duro de la fría. En pantalla el `show` no cambia nada (C5). La rama sigue siendo distinta por l. 260 «Después, me miró a mí.» |
| 514 (+536, 553, 595) | Despido B · aula, semana de exámenes | fría «Buenos días, tutor.» / resto «Buenos días, [mc].» · «...Quería decirlo con más ganas. No me sale.» · «Cuando cierro el libro, no recuerdo qué sentía nadie.» | incomoda | ✅ | — | Es la sonrisa que **intenta** salir y no puede: «Quería decirlo con más ganas. No me sale.» Para eso está `incomoda`. Todavía queda el examen; `seria` llega después |
| 948 (+964, 983) | Aula de la tarde, tras el examen | «[mc]...» · «Mi hoja estuvo en blanco durante todo el examen.» · «Con toda esta energía que me sobra, y no pude hacer nada por ninguna.» · «No me digas que no es mi culpa.» | neutral | ➕ | **seria** | C1: l. 952 «Nadie recogía nada. Ninguna dijo «salió bien».» Es la derrota, y lo que dice es la frase más dura que tiene en el capítulo. La sonrisa suave de `neutral` lo contradice |
| 1259 | Despedida | «Gracias por venir todos los días.» · «No sé cómo despedirme de alguien que se va por mi culpa.» · «Lo sé. Pero así se siente.» · fría «Gracias por todo, tutor.» | incomoda | ✅ | — | No sabe cómo despedirse: la torpeza de `incomoda` es eso. Sin `seria` aquí, la despedida se distingue del aula de la tarde. La fría comparte el `show` (§9) |

---

## 6. Resumen

**Momentos evaluados: 87** (prólogo 2 · apertura 1 · hub 15 · conexiones 31 · E6 31 · final malo 7).

| Veredicto | Momentos | Dónde |
|---|---|---|
| ✅ | **77** | — |
| 🔁 | **3** (3 sentencias) | hub 312 · conexiones 2831, 3391 |
| 🎨 | **0** | La cinta cortada ya está en GUIA §9. `neutral` no se rehace por el aviso 6 |
| ➕ | **7** (8 sentencias) | `yotsuba seria`: hub 402 · conexiones 383, 2108 (+2137) · E6 2315 · final malo 251, 262, 948 |

**Uso de cada expresión** (sentencias `show yotsuba <expr>`; aparte, los `e6_foco` del E6):

| Expresión | Hoy (82 `show`) | Tras 🔁 y ➕ | E6 `e6_foco` hoy (28) | Tras ➕ |
|---|---|---|---|---|
| sonriendo | 43 | **42** | 17 | 17 |
| incomoda | 26 | **25** | 3 | **2** |
| neutral | 9 | **5** | 7 | 7 |
| sorprendida | 4 | **3** | 1 | 1 |
| seria (➕) | — | **7** | — | **1** |

A eso se suman, siempre en neutral, las 2 formaciones y la entrada del E6.

**Comprobaciones a–e:**

- **(a) La cara contradice la línea: 9 casos.** Todos tienen una línea del narrador o del MC que niega lo que muestra el sprite:
  - hub 312: «con esa sonrisa puesta», con `neutral`;
  - hub 402: «No dijo nada. Miraba la pista», con `sorprendida`;
  - reacción 383: «sin pedirme que sonriera», con una cara que sonríe;
  - interc. 4 2108: «Sin sonrisa.», con `incomoda`;
  - interc. 5 2831: «cara de preocupación», con `sonriendo`;
  - interc. 6 3391: «Nadie se rió», con `sonriendo`;
  - E6 2315: «Lo dijo bajito», con `incomoda`;
  - final malo 251: «con las manos juntas delante», con las manos a la espalda;
  - final malo 948: «Ninguna dijo «salió bien»», con `neutral`.

  La 262 no es una contradicción: la arrastra la 251.
- **(b) SONRIENDO (43): 24 sinceras, 17 máscara, 2 contradicción.**
  - Las **17 de máscara** están todas marcadas por el texto (tabla del §1), y en 8 de sus 9 escenas la grieta llega después con otro sprite o con el narrador. Se quedan como están (C3).
  - Las **2 de contradicción** (2831, 3391) no son máscara: son una sonrisa que sobra, y pasan a `incomoda`.
  - La grieta tiene su escala: `neutral` si la sonrisa se ablanda, `incomoda` si se tensa, `seria` si se va (§1).
- **(c) INCOMODA (26): 23 son apuro de verdad, 3 eran comodín.**
  - Las 23 de verdad: pillada, defender a alguien y que la corten, nervios, culpa o la vergüenza de dar las gracias.
  - Las 3 de comodín (interc. 4 2108 y 2137, final malo 251) son «no está contenta» llevado a la cara que tenía más a mano. Pasan a `seria`.
  - Ninguna `incomoda` pasa a `neutral`: donde el texto pide menos sonrisa, pide **ninguna**.
- **(d) Parpadeo: 0 casos hoy y 0 tras los cambios.** Las alternancias que quedan llevan una línea suya en cada cambio:
  - tarde tibia 2524 / 2528 / 2534 y tarde no visitada 2564 / 2570 / 2576 en el E6;
  - interc. 5, 2831 → 2861 → 2870 tras el 🔁: incomoda → sonriendo («súper tranquilas») → incomoda («Si te soy sincera»).
- **(e) Ramas tras los cambios:**
  - **Hub:** cálida sorprendida → neutral → incomoda → **seria** → neutral → sonriendo · tibia sonriendo de principio a fin · fría incomoda → sonriendo.
  - **Reacción:** cálida sonriendo → **seria** → sonriendo → incomoda · tibia sonriendo · fría sonriendo → neutral.
  - **E6 tarde:** cálida neutral → sonriendo · tibia y no visitada sonriendo → neutral → sonriendo · fría sonriendo sin grieta.
  - **E6 eco:** cálida neutral → sonriendo → incomoda · tibia neutral → sonriendo · fría y no visitada sonriendo.
  - **Final malo:** la fría habla y mira al MC, pero comparte `seria` con las otras (§9).
  - Lo que pide la pregunta (e) queda cubierto: **la cálida es la única rama que baja la máscara del todo en el hub y en la reacción**, y lo hace con `seria`, una cara distinta de su sonrisa. La fría nunca la baja delante del MC hasta el final malo.
  - Sin favoritismo (C7): `seria` sale en la cálida (hub, reacción), en la fría (final malo 262), en una escena que depende de la rama de **otra** hermana (interc. 4) y en escenas comunes (E6, final malo). No es un premio.

---

## 7. ➕ `yotsuba seria`: la cara sin sonrisa

**Por qué es un ➕ y no un 🎨 de `neutral`.** El guion del hub pedía que `neutral` no sonriera (aviso 6), pero el PNG sonríe, y el código ya cuenta con esa sonrisa suave. Rehacer `neutral` sin sonrisa rompería tres usos que hoy funcionan:

- hub 218 → l. 233 «Si no supiera lo que acaba de decir, pensaría que está contenta.» Necesita que parezca contenta.
- hub 364 → l. 367 «Su sonrisa no desapareció.»
- E6 3967 → «…Esta soy yo.»: emoción, no tristeza.

**Cuánto cubre (las condiciones del ➕):**

| Escena | Sentencia | Líneas de Yotsuba que cubre | Rama |
|---|---|---|---|
| Hub, la máscara cae | `02_cap1_Yotsuba.rpy:402` | 405, 421 → **2** | cálida |
| Reacción | `02_cap1_conexiones.rpy:383` | 386, 388, 390 → **3** | cálida |
| Interc. 4, «Sin sonrisa» | `02_cap1_conexiones.rpy:2108` (+2137) | 2113 / 2117 (alternativas), 2123, 2125, 2127, 2129, 2135 → **7** | fría de la hermana visitada |
| E6, aula de la tarde | `02_cap1_evento6.rpy:2315` | 2317 → **1** | todas |
| Final malo, despido A | `02_cap1_final_malo.rpy:251` y 262 | 254, 265, 267, 269 → **4** | todas (262: fría) |
| Final malo, aula de la tarde | `02_cap1_final_malo.rpy:948` | 967, 969, 971, 973, 975, 977, 981 → **7** | todas |

**24 líneas en el código** (23 por partida, porque 2113 y 2117 son alternativas) en **6 escenas de 4 archivos**. Cumple de sobra: muchas líneas y más de una escena.

**Pose y silueta (regla de §9).**
- **Las dos manos juntas delante, sobre la falda**, con los brazos rectos formando una V estrecha. Los hombros un poco hacia dentro y la cabeza un punto baja.
- La pose sale de dos sitios: del narrador (final malo l. 256: «Se quedó mirando el suelo, con las manos juntas delante.») y de lo que pedía el guion del hub para la cara sin sonrisa: «hombros ligeramente menos abiertos, mirada un punto más baja» (l. 562).
- Se distingue de las otras cuatro:
  - de los brazos colgando a los lados (`neutral`, `sonriendo`);
  - de las manos escondidas a la espalda (`incomoda`): aquí los antebrazos desnudos (manga corta) cruzan **por delante** de la falda verde, y ese contraste de color se ve a distancia;
  - del puño alto (`sorprendida`).
- **El riesgo es `incomoda`**, porque las dos son estrechas. Pasan una a otra en el final malo (245 → 251).
- **Prueba antes de aprobarla:** ponerla al 30 % junto a las cuatro. Si se confunde con `incomoda`, bajar las manos juntas hasta el bajo de la falda, para que la V de los brazos se vea más larga.

**Cara.** Boca cerrada y recta, sin curva. Mirada un punto por debajo de la cámara, sin llegar al suelo, porque en la interc. 4 le habla al MC a la cara («Arréglalo. Por favor.»). Cejas relajadas, apenas alzadas por dentro. Rubor muy leve o ninguno.

**Archivo y atributo.**
- PNG: `The Fifth Choice/game/images/sprites/yotsuba_sprites/yotsuba_seria.png`
- Declaración en `00_definiciones.rpy`, debajo de la l. 277 (`image yotsuba sorprendida …`):
  `image yotsuba seria = "sprites/yotsuba_sprites/yotsuba_seria.png"`
- Uso: `show yotsuba seria at …` / `call e6_foco("yotsuba", "seria")`.
- **Orden:** primero el PNG y la declaración, después los `show` del §8 marcados ➕. Sin la imagen, Ren'Py da error al llegar a ellos.

**Ajustes en PixAI** (§1 y §3 de `GUIA_ARTE.md`):
- Modelo base **Tsubaki.2**. LoRA de personaje `中野四葉 サンプル(アニメ)Tsubaki.2バージョン` a **0.8**. **Sin LoRA de serie**, porque es un sprite individual (aviso 4).
- **Vertical 768 × 1280.** Las de Yotsuba vinieron así y salieron a escala 1,011 (§3). Tsubaki.2 no tiene campo negativo: todo va en positivo. Apuntar la semilla.
- **Margen arriba para la cinta:** el prompt pide espacio libre sobre la cabeza y la cinta entera dentro del encuadre. Comprobar en el render crudo, antes de normalizar, que la fila 0 no tiene verde (§9).
- Post:
  - Normalizar con `normalizar_sprite.py` a **760 × 930** RGBA, con IPD **77,2** y los ojos en **y = 199**, centrado en el eje de la falda (§3).
  - Después de normalizar, volver a comprobar que la cinta no toca el borde superior.
  - Halo: `limpiar_halo.py` con `--solo-halo`, que es la excepción de Yotsuba (§4–§5).

**Prompt (positivo):**
```
masterpiece, best quality, official anime screencap, go-toubun no hanayome style,
1girl, solo, only one person in the entire image, nakano yotsuba,
standing, front view, facing viewer, centered, figure from head to knees, knees at the bottom edge, wide empty space above the head, entire hair ribbon inside the frame, plain white background, solid white background,
short orange hair, bob cut, hair ending above the shoulders, green hair ribbon tied in a large bow on top of the head, blue eyes,
subdued expression, quiet serious face, straight closed mouth, lips together, eyes looking slightly downward, relaxed eyebrows, faint blush,
both hands clasped together in front of the skirt, straight arms forming a narrow V, shoulders slightly drawn in, head slightly lowered,
yellow sweater vest, white collared shirt, short sleeve white shirt, bare arms, sleeves ending above the elbow, green plaid bow at the collar, green pleated skirt, dark knee-high socks,
flat even studio lighting, clean lineart, natural hands with five fingers, deep focus
```
- **La cara sin sonrisa lleva tres tokens redundantes en positivo** (`subdued expression, quiet serious face, straight closed mouth`), como pide §6 para las expresiones no sonrientes. Yotsuba es el caso más difícil, porque el LoRA la trae sonriendo.
- **La manga corta lleva la redundancia de §6** (`short sleeve white shirt, bare arms, sleeves ending above the elbow`).
- **No se nombra lo que no se quiere** (§6). Por eso el prompt pide «la cinta entera dentro del encuadre» y no «que no la corte».

---

## 8. Cambios por archivo (antes → después)

Solo cambia el atributo de expresión. La posición (`at …`), el `with` y el orden se quedan igual. Sin ternarios.
🔁 = se puede aplicar ya. ➕ = **solo después** de crear `yotsuba_seria.png` y su declaración (§7).

**`02_cap1_Yotsuba.rpy`**
```renpy
# l. 312 · 🔁
    show yotsuba neutral at pj_calla(0.5)
# →
    show yotsuba sonriendo at pj_calla(0.5)

# l. 402 · ➕ (dentro de label yotsuba_m4a)
    show yotsuba sorprendida at pj_habla(0.5)
# →
    show yotsuba seria at pj_habla(0.5)
```

**`02_cap1_conexiones.rpy`**
```renpy
# l. 383 · ➕ (dentro de if rama_hub == "calida":)
        show yotsuba neutral at pj_habla(0.5)
# →
        show yotsuba seria at pj_habla(0.5)

# l. 2108 · ➕ (dentro del else de la interc. 4)
            show yotsuba incomoda at pj_habla(0.5)
# →
            show yotsuba seria at pj_habla(0.5)

# l. 2137 · ➕ (mismo bloque)
            show yotsuba incomoda at pj_calla(0.5)
# →
            show yotsuba seria at pj_calla(0.5)

# l. 2831 · 🔁
    show yotsuba sonriendo at pj(X_YOTSUBA)
# →
    show yotsuba incomoda at pj(X_YOTSUBA)

# l. 3391 · 🔁
    show yotsuba sonriendo at pj_calla(X_YOTSUBA)
# →
    show yotsuba incomoda at pj_calla(X_YOTSUBA)
```

**`02_cap1_evento6.rpy`**
```renpy
# l. 2315 · ➕
    call e6_foco("yotsuba", "incomoda")
# →
    call e6_foco("yotsuba", "seria")
```

**`02_cap1_final_malo.rpy`**
```renpy
# l. 251 · ➕
    show yotsuba incomoda at pj_habla(X_YOTSUBA)
# →
    show yotsuba seria at pj_habla(X_YOTSUBA)

# l. 262 · ➕ (dentro de if rama_de("yotsuba") == "fria":)
        show yotsuba neutral at pj_habla(X_YOTSUBA)
# →
        show yotsuba seria at pj_habla(X_YOTSUBA)

# l. 948 · ➕
    show yotsuba neutral at pj(X_YOTSUBA)
# →
    show yotsuba seria at pj(X_YOTSUBA)
```

**`00_definiciones.rpy`** (➕, debajo de la l. 277)
```renpy
image yotsuba seria = "sprites/yotsuba_sprites/yotsuba_seria.png"
```

**Cómo probarlo (después de aplicar).** Desde la consola (Shift+O). Las etiquetas que terminan en `return` te devuelven al menú principal al acabar: sirven solo para ver la cara.
- **Hub (312 y 402):** `jump hub_Yotsuba`. La 312 sale en el menú, sea cual sea la rama. Para la 402, elige «No tomar el cronómetro todavía. Volver a lo que dijo.» (cálida).
- **Reacción cálida (383):** `$ destino = "yotsuba"`, `$ yotsuba_rama_cap1 = "calida"` y `jump cap1_interconexion_4`. La reacción sale al principio.
- **Interc. 4, la grieta seria (2108 / 2137):** `$ destino = "ichika"`, `$ ichika_rama_cap1 = "fria"` y `jump cap1_interconexion_4`.
- **Interc. 5 (2831):** `jump cap1_interconexion_5` y avanza hasta el aula.
- **Interc. 6 (3391):** `$ destino = "itsuki"` y `jump cap1_interconexion_6`. Sin cálidas sale clima mixta, que basta para verla quedarse en `incomoda`. Para la mala, añade antes `$ despido_cap1 = True`.
- **E6 (2315):** `jump e6_debug` → cualquier trío → «Ajustes» → modo de minijuegos «saltar» → «>> Jugar Evento 6». La 2315 está en el aula de la tarde, común a todas las combinaciones.
- **Final malo A (251 y 262):** `$ yotsuba_rama_cap1 = "fria"` y `jump final_malo_beat`. Con otra rama sale solo la 251.
- **Final malo B (948):** `jump final_malo_hub3` y avanza hasta el aula de la tarde.
- **Lint** después de aplicar: tiene que salir limpio, y en particular sin avisos de imagen `yotsuba seria` no declarada.

---

## 9. Fuera de alcance (anotado, no propuesto)

- **Hub l. 231, «Sonrió.»:** el `show` de la sonrisa amplia no llega hasta la l. 249, 18 líneas después. Hoy `neutral` ya sonríe algo y no choca. Si algún día se rehace `neutral`, habrá que insertar un `show yotsuba sonriendo` en la l. 231.
- **`show` compartidos entre ramas:**
  - interc. 3 l. 1754 (la fría mira la pizarra con la misma `sonriendo` que el resto);
  - final malo l. 1259 (la fría dice «tutor» «Con el tono que se usa con un desconocido» con la misma `incomoda`);
  - final malo 251 / 262 tras el ➕.

  Separarlos exige insertar un `show` en cada rama.
- **Eco frío del E6 (l. 3359):** `e6_entrar` la mete en `neutral` antes del foco en `sonriendo`, y el narrador ya dice «con la sonrisa ya puesta». Es una línea, y `neutral` sonríe un poco. Se arreglaría en `e6_cinco`, que es común a las cinco.
- **Despedida de conexiones (l. 3835–3919):** no hay sprite para ninguna de las cinco. Si se quiere, es una decisión de escena para todas.
- **`show` que repiten la cara.** Con tu regla (un `show` con atributo solo cuando cambia el sprite), los candidatos son:
  - hub 504 y 536;
  - conexiones 813, 989, 1012, 1019, 1052, 1063, 1146, 1754, 1776, 2074, 2103, 2292, 2321, 2333, 2342, 2361, 2898, 2915, 2920, 3363 y 3384;
  - final malo 245 y 595;
  - los que dejen sin efecto los cambios: hub 462 tras el 🔁 de la 312, y final malo 262 tras el ➕ de la 251.

  En ramas (conexiones 431, 2037, 2079, 2108, 3527) hay que mirarlo a mano. Es la misma limpieza que se hizo con Miku, en una pasada aparte.
- **`neutral` ↔ `sonriendo` comparten silueta** (§1). Con `seria` no hace falta tocarlo. Si en las pruebas al 30 % molesta, el arreglo sería una pose nueva para `neutral` que conserve su sonrisa suave. Sería un 🎨 aparte.
- **Ficha de vestuario de GUIA §2:** añadir las medias oscuras hasta la rodilla de Yotsuba (aviso 5).
