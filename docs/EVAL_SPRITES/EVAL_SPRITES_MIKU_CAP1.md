# Evaluación de sprites · Miku · Prólogo + Capítulo 1

> Revisado sobre el árbol de trabajo actual (commit `19d226e`, con cambios sin commitear en otros archivos).
> Es una evaluación: no se tocó ningún `.rpy`. Los números de línea son los de antes de aplicar.
> **Estado (13/11/2026):** los 3 🔁 del §8 están aprobados y aplicados, y conexiones l. 2159 pasó a `narrador`. Después se limpiaron los `show` que repetían la cara (regla del usuario: un `show` con atributo solo cuando cambia el sprite):
> - Se borraron hub l. 297 y 314, que quedaban en `animada`, igual que la l. 268.
> - 35 `show miku neutral at pj_habla/pj_calla` pasaron a `show miku at …`, solo tinte (hub 499 · conexiones 338, 756, 988, 1032, 1037, 1096, 1147, 1152, 1221, 1234, 1797, 1806, 2150, 2208, 2229, 2236, 2257, 2291, 2334, 2341, 2859, 2903, 2914, 2921, 3362, 3479, 3490, 3560, 3569 · final malo 273, 534, 564, 594, 962).
>
> Quedan 38 `show` con atributo: neutral 19 · encogida 12 · relajada 5 · animada 2. Lint, sin errores de sprites. Los `e6_foco` del E6 no se tocaron.
> Fuentes: `docs/GUIA_ARTE.md` §1, §2, §3 y §9 · `docs/REVISION_PERSONAJES_CAP1/REVISION_MIKU_CAP1.md` (manda sobre cualquier propuesta) ·
> `docs/EVAL_SPRITES/EVAL_SPRITES_NINO_CAP1.md` (formato y criterios) · los seis `.rpy` del recorrido · `10_minijuegos.rpy`, `10_mj_miku.rpy`, `10_mj_chibi.rpy` y `12_e6_pantallas.rpy` para el E6.

---

## 0. Avisos: dónde el encargo y los archivos no dicen lo mismo (mandan los archivos)

| # | El encargo dice | Los archivos dicen | Qué hice |
|---|---|---|---|
| 1 | E6: 0 shows, 109 líneas | Es literal: `02_cap1_evento6.rpy` no tiene ningún `show miku`. Pero la pinta con **22** `call e6_foco("miku", …)`, **2** `call e6_formacion_neutral` (l. 259 y 2178) y **1** `call e6_entrar(e6_h)` (l. 3286). Las 109 líneas son **62** `miku` + **47** `miku_int`. | Evalué los 25. Diagnóstico completo en §3: **60 de las 62 líneas `miku` tienen sprite** y las otras 49 van sobre un CG a propósito. |
| 2 | 75 shows, neutral = 57 | En los seis archivos hay **97** `show miku`: **75** con atributo (neutral 57 · encogida 10 · relajada 5 · animada 3) y **22** de solo tinte (`show miku at pj_calla(…)`). Las cifras del encargo son las de los 75. | Uso las mismas. Los de tinte van dentro del momento que los contiene. |
| 3 | relajada 5 usos, animada 3 | Son los `show`. Además el E6 usa relajada 2 veces y animada 2 (l. 360, 2357, 2835, 3685). | Los cuento por separado en §6. |
| 4 | «Hoodie celeste» (y `GUIA_ARTE.md` §2: «sudadera azul claro con capucha y cremallera») | **Corregido por el usuario: en el canon es el cárdigan**, y los cuatro PNG se leen como cárdigan. La falda sale en dos verdes (claro en `neutral` y `encogida`, oscuro en `animada` y `relajada`). | Los sprites están bien. El prompt de §7 va con cárdigan. La GUIA §2 (l. 104) sigue diciendo «sudadera». |
| 5 | — | `GUIA_ARTE.md` §9: «`miku animada` se queda sin nada delante del cuerpo». El PNG lleva **los dos puños cerrados delante del pecho**. | Describo el PNG. La silueta sigue siendo distinta de las otras tres (codos doblados contra brazos rectos). |
| 6 | — | Conexiones l. 2159: `miku "Eso ya era un cambio."`. En la revisión (P4b) es la segunda mitad de la línea del **narrador** de la l. 2157. | No es de sprites y no lo toco. Anotado en §9. |

---

## 1. Ficha de los 4 sprites

| Sprite | Pose y brazos | Mirada | Boca | Lo que transmite de verdad | Lo que NO cubre |
|---|---|---|---|---|---|
| `miku neutral` | De frente, recta. **Brazos colgando** a los lados, con las manos sueltas junto a la falda. | Párpados a media altura, mirada al frente y un poco baja. El mechón le tapa medio ojo derecho. | Cerrada, una línea corta. Rubor leve. | Reserva, desgana, un «déjame» sin hostilidad. Es su armadura callada y su forma de estar en grupo. | Alegría, calidez, vergüenza y tristeza abierta. |
| `miku animada` | **Los dos puños cerrados delante del pecho**, con los codos pegados al cuerpo. | Ojos muy abiertos y brillantes, de frente. | **Abierta, sonrisa grande.** Rubor. | Entusiasmo, «¡mira!», el arrebato cuando habla de lo suyo. | Calma, timidez y todo lo contenido. Es la más intensa: no sirve para una sonrisa tranquila. |
| `miku relajada` | **Brazo derecho extendido hacia un lado con la palma abierta hacia arriba**, el gesto de explicar. El otro brazo, abajo. La cabeza un poco ladeada. | Ojos suaves, de frente. | Sonrisa cerrada y tranquila. Rubor leve. | Comodidad, calidez tranquila, explicar algo que domina. | Euforia, vergüenza y tristeza. |
| `miku encogida` | **Manos juntas abajo, delante de la falda.** Hombros hacia dentro y brazos rectos pegados al cuerpo. | Ojos entornados, mirada apartada hacia un lado. | Sonrisa torcida y apretada. **Rubor fuerte y gota de sudor.** | Vergüenza, timidez, el «perdón», no saber dónde ponerse. | Llanto, tristeza seca y frialdad. |

**Regla de §9 (a un 30 % solo se lee la silueta):**

- **`neutral` ↔ `encogida`: es el par peligroso.** Las dos tienen los brazos rectos y la silueta estrecha. Las separa dónde terminan las manos: a los lados en `neutral` y juntas en el centro, formando una V, en `encogida`. En los planos a solas (x = 0.5) se lee bien. En el grupo (`X_MIKU`) cuesta más, pero ahí `encogida` solo sale en la interc. 5 (l. 2928 y 2946), con Miku hablando y resaltada.
- **`animada` ↔ el resto:** es la única con los codos doblados y las manos a la altura del pecho. Se distingue ✓.
- **`relajada` ↔ el resto:** es la única asimétrica y la más ancha (el brazo hacia fuera). Es la que mejor se lee ✓.
- **Ningún sprite cubre el llanto ni la mano en los audífonos.** Lo de los audífonos es a propósito: §2 de la GUIA los quiere siempre al cuello y deja el gesto de subírselos a la narración. La lágrima es una sola línea (E6 l. 3927), así que no justifica un ➕.

---

## 2. Criterios aplicados (los de Nino, adaptados a Miku)

- **C1 · La narración manda.** Si el narrador describe brazos, manos o mirada, va el sprite que lo cumple. Por ejemplo: «libro a media cara» o «manos juntas delante del cuerpo» → `encogida`; «hablaba más rápido» → `animada`.
- **C2 · «Perdón» y oírse a sí misma → `encogida`.** Es el uso que ya hace la revisión: hub l. 319 y 410, queja l. 777, interc. 5 l. 2928 y 2946, E6 l. 2872 y 2902, final malo l. 1000.
- **C3 · Deslices breves.** Un `show miku at pj_calla(…)` de solo tinte conserva la cara y no se toca.
- **C4 · La revisión manda.** P3b (lunes del E6), P3c (mesa), P4a (reacción cálida), P4b (interc. 4), N2 (interc. 5), N3 (soda) y N5 se respetan tal cual.
- **C5 · Parpadeo.** Nada de A → B → A en réplicas seguidas ni cambios de cara sin una línea que los motive. Se arregla cambiando el atributo por el del vecino, y entonces el siguiente `show` no cambia nada en pantalla. Ningún `show` se borra.
- **C6 · Ramas.** En el mismo punto del guion, cálida, tibia y fría llevan caras distintas siempre que el texto lo permita.
- **C7 · `neutral` es su reserva, no un hueco.** En las escenas de grupo y en la rama fría se queda neutral: es lo que tiene que transmitir. No se cambia por inercia.
- **C8 · El arco.** Al principio del capítulo, cara cerrada (`neutral`/`encogida`). `relajada` y `animada` solo cuando está en su tema o cuando la rama se ha abierto (cálida). Igual que el «…», que desaparece con el desarrollo.

Veredictos: ✅ queda bien · 🔁 cambiar a otra expresión existente · 🎨 rehacer el sprite · ➕ sprite nuevo.

---

## 3. Evento 6: diagnóstico tramo por tramo (PRIORIDAD)

**Conclusión: en el E6 no falta ningún sprite.** De las 109 líneas, **60** `miku` se dicen con su sprite en pantalla. Las otras **49** (47 `miku_int` y 2 `miku`) van sobre un CG, y eso es a propósito: un sprite taparía el CG.

| Tramo (etiqueta · líneas) | Líneas de Miku | Qué hay en pantalla | ¿Intencional o falta? |
|---|---|---|---|
| Lunes en el aula (`e6_lunes` · 256–410) | **19** `miku` (362–410): cálida 6, tibia 4, fría 5, no visitada 4 | `bg_aula` (l. 256), formación neutral (l. 259) y `e6_foco` por rama (l. 360, 376, 388 y 402) | Sprite ✓ |
| Lunes, CG de las cinco (l. 473) | 0 | `cg_cinco_aula` | — |
| Núcleo de Sociales (`e6_miku_nucleo` · 1864–1905) | 0 (narrador y MC) | `bg_negro` (l. 1870) → **CG `cg_miku_examen`** (l. 1883) | Intencional: CG |
| Voz interior (`e6_miku_mono_<estado>` · 1907–2012) | **44** `miku_int`: cálida 18, tibia 11, fría 8, no visitada 7 | El mismo CG | Intencional: monólogo sobre su CG |
| Minijuego M3 (`e6_miku_mj` · 2018–2044) | **3** `miku_int` (2030–2034), después del juego | El CG, y durante el juego la screen `mj_m3`. Sus líneas de fallo son datos (`MJ_FALLOS`, `10_minijuegos.rpy` l. 110) y la acompaña un **chibi** (`mj_retrato("miku", …)`, `10_mj_miku.rpy` l. 897, `images/chibis/miku_*.png`) | Intencional: minijuego con chibi propio |
| Promesa y gesto (`e6_miku_promesa` · 2047, `e6_miku_gesto_*` · 2064–2150) | 0 (MC y narrador) | El CG | — |
| Después del examen, en grupo (`e6_despues` · 2157–2397) | **4** `miku` (2359–2371): 2 cálida, 2 resto | `bg_aula_tarde` (l. 2175), formación neutral (l. 2178) y `e6_foco` l. 2357 / 2367 | Sprite ✓ |
| Tarde por rama (`e6_miku_tarde_*` · 2831–2910) | **16** `miku`: cálida 4, tibia 5, fría 2, no visitada 5 | Mismo fondo, `e6_foco` l. 2835, 2853, 2862, 2872, 2883, 2896 y 2902 | Sprite ✓ |
| Cuando hablan las otras (todo el aula de la tarde) | — | Miku se queda en pantalla, atenuada (`pj_calla`), con su última cara (`e6_mostrar_foco`, l. 98–105) | Sprite ✓ |
| Llegada al departamento y eco (`e6_cinco` · 3256, `e6_miku_eco_*` · 3675–3750) | **11** `miku`: cálida 3, tibia 3, fría 2, no visitada 3 | `bg_departamento` (l. 3258), entra neutral (`e6_entrar`, l. 3286) y `e6_foco` l. 3679, 3685, 3702, 3723 y 3740 | Sprite ✓ |
| Mesa (`e6_mesa` · 3810–4095) | **10** `miku` | `e6_foco` encogida (l. 3864, 3923, 4049 y 4091) | Sprite ✓ |
| Foto (l. 4100–4160) | **2** `miku` (4135, 4159) | **CG `cg_cinco_aprobadas`** (l. 4104 / 4109 / 4114, según el tinte) | Intencional: CG de las cinco |
| Chat del grupo (`e6_cuarto` · l. 4305) | 0 líneas de diálogo. Su mensaje («...Sociales: cien.») es un dato de la screen (`12_e6_pantallas.rpy` l. 220) | `bg_cuarto_mc` + screen `chat_grupo` | Intencional: interfaz |

Cuenta: 19 + 4 + 16 + 11 + 10 = **60** con sprite · 44 + 3 = **47** `miku_int` sobre CG · **2** `miku` sobre CG. Total, **109** ✓.

---

## 4. Líneas de Miku sin sprite fuera del E6

| Archivo · líneas | Qué hay en pantalla | ¿Intencional? |
|---|---|---|
| `01_prologo.rpy` 697, 707, 713 | CG `cg_miku_sofa` (l. 676) | Sí, es CG |
| `02_cap1_Miku.rpy` 132–146 | CG `cg_miku_estudio` (l. 127) | Sí, es CG |
| `02_cap1_Miku.rpy` 195–213 | CG `cg_miku_sorpresa` (l. 192) | Sí, es CG |
| `02_cap1_conexiones.rpy` 3855 (clima buena), 3889 (clima mixta) | `bg_departamento` / `bg_departamento_anochecer` (l. 3796 / 3801), **sin ninguna hermana** | Parece decisión de escena: en esa despedida no hay sprite para ninguna de las cinco (Yotsuba, Nino e Itsuki también hablan sin él). No es una carencia de Miku. Anotado en §9 |

---

## 5. Tabla por archivo

Un momento es el `show` (o `e6_foco`) donde cambia la expresión, más las líneas de Miku que cubre. Los `show miku at …` que solo cambian el tinte van en el momento que los contiene.

### 01_prologo.rpy (5 shows)

| archivo:línea | Rama / escena | Diálogo (resumido) | Actual | Veredicto | Propuesta | Por qué |
|---|---|---|---|---|---|---|
| 957 (+961, 970, 982) | Sala, las cinco | «…Demasiado ruido» · «…Avisen cuando terminen de gritar» | neutral | ✅ | — | Su primera cara con sprite: cerrada, aparte del ruido (C8) |
| 1053 | Coro «¡No pensamos estudiar!» | (línea de `quintillizas`) | neutral | ✅ | — | Bloque del grupo (C7) |

### 02_cap1_apertura.rpy (1 show)

| archivo:línea | Rama / escena | Diálogo (resumido) | Actual | Veredicto | Propuesta | Por qué |
|---|---|---|---|---|---|---|
| 417 | Pasillo, la última en irse | «…No fue idea mía» · «…Olvídalo. Perdón.» | neutral | 🔁 | **encogida** | C1: l. 415 «con el libro apretado contra el pecho» y l. 424 «se dio cuenta de que lo había dicho». C2: termina en «Perdón». `encogida` es el único sprite con las manos juntas delante. Sigue siendo una cara cerrada (C8) |

### 02_cap1_Miku.rpy (20 shows · hub con ramas)

`miku_m4a` = cálida · `miku_m4b` = tibia · `miku_m4c` = fría. Hasta la l. 374 es común a las tres.

| archivo:línea | Rama / escena | Diálogo (resumido) | Actual | Veredicto | Propuesta | Por qué |
|---|---|---|---|---|---|---|
| 89 | Biblioteca, llegada | «…» · «[mc]… ¿Cómo sabías que estaba aquí?» · «…Ah.» | neutral | ✅ | — | Detrás del libro (l. 112, «lo justo para mirarme por encima del canto») |
| 228 | Biblioteca | «…¿Y qué comían?» · «…Tres veces al día. Todos los días» | neutral | ✅ | — | La curiosidad asoma, todavía con pausa |
| 245 | Biblioteca | «Había un señor de la guerra que se llamaba Takeda Shingen» · «Sin mar no hay sal» | relajada | ✅ | — | Entra en su tema: la mano abierta de explicar. Las frases ya no empiezan con «…» (l. 266) |
| 268 | Biblioteca | «dejaron de vendérsela» · «le mandó sal Uesugi Kenshin» · «Mandarle sal al enemigo» | animada | ✅ | — | C1: l. 262 «Hablaba más rápido» |
| 297 | Biblioteca | «Aunque seguramente no pasó» · «Está escrita cien años después» · «Alguien se la vendió» | neutral | 🔁 | **animada** | C5: animada (268) → neutral → animada (314) en el mismo arrebato. El narrador dice que habló «un minuto entero» (l. 328). El giro de historiadora es justo lo que la entusiasma («a mí eso me parece mucho más—», l. 317). Así, la 314 ya no cambia nada en pantalla |
| 314 | Biblioteca | «Y a mí eso me parece mucho más—» | animada | ✅ | — | El clímax, justo antes de cortarse |
| 319 (+342) | Biblioteca | «…Perdón. Hablé mucho» · «…La de esperar a que termine» | encogida | ✅ | — | Se oye (l. 328) (C2) |
| 388 | m4a · cálida | «…¿Qué?» · «…Diez días. Doce si llovía» | neutral | ✅ | — | La pregunta la pilla desprevenida |
| 401 | cálida | «Depende de la época del año» · «Eso es lo que a la gente se le esca—» | animada | ✅ | — | Contesta sin pausa y vuelve el arrebato |
| 410 | cálida | «…Per—» · «…» | encogida | ✅ | — | Iba a pedir perdón y el MC la corta (C2) |
| 429 (+438) | cálida | «…Dijiste que llegaste a la página noventa» · «…Lo de la sal está en la ciento veinte» | relajada | ✅ | — | l. 441 «despacio, como quien termina una cuenta»: la primera complicidad |
| 459 (+466) | cálida | «…No es lo mismo.» | encogida | ✅ | — | El elogio la encoge. l. 471: el libro se queda a media altura |
| 487 (tinte) | m4b · tibia | «…No se me da bien. Solo lo he leído.» | encogida (de la 319) | ✅ | — | El elogio la incomoda |
| 494 (+499) | tibia | «…Eso no es difícil.» | neutral | ✅ | — | l. 502 «como quien cierra una puerta con educación». l. 508: el libro sube a media cara |
| 532 (+546) | m4c · fría | «…Ya lo sé.» · «…Hoy no.» | neutral | ✅ | — | l. 530 «como si le hubieran confirmado algo que ya sospechaba»: la armadura (C7) |

### 02_cap1_conexiones.rpy (57 shows)

En `reaccion_miku`, `rama_hub` es la rama de Miku. En las interconexiones, `rama_hub` es la rama de la hermana visitada (en la interc. 4, Yotsuba). La de Miku es `rama_de("miku")`.

| archivo:línea | Rama / escena | Diálogo (resumido) | Actual | Veredicto | Propuesta | Por qué |
|---|---|---|---|---|---|---|
| 259 | Reacción · cálida | «…Buenos días, [mc]» · «…¿Ya llegaste a la página ciento veinte?» · «…Quiero ver tu cara» | relajada | ✅ | — | Revisión P4a (C4) |
| 276 | Reacción · cálida | «…La de esperar a que termine» · «…Gracias por leerlo, [mc]» · «…Soda de matcha» | encogida | ✅ | — | Revisión P4a: da las gracias y regala la soda |
| 301 (+308) | Reacción · cálida | «…Sí. …Es lo bueno.» | relajada | ✅ | — | Revisión N3 (soda) |
| 315 (+320) | Reacción · tibia | «…Buenos días.» | neutral | 🔁 | **encogida** | C1: l. 323 «Lo dijo con el libro a media cara». C6: hoy tibia y fría llevan la misma `neutral`. La fría (audífonos puestos, l. 334) se queda neutral. Además coincide con su eco tibia del E6 (l. 3702, `encogida`) |
| 331 (+338, 345) | Reacción · fría | «…Voy a estudiar solo lo que entra en el examen» · «Como dijiste» | neutral | ✅ | — | l. 350 «como quien acepta un reglamento»: armadura (C7) |
| 753 (+756) | Queja · no visitada | «…No me buscaste» · «…Así estuvo bien. Estuve tranquila» · «…Hay una silla enfrente de la mía» | neutral | ✅ | — | Tranquila en la superficie. l. 775: «no lo subió hasta media cara» |
| 777 (+796) | Queja · no visitada | «…Dejé el libro abierto en la misma página dos días» · «…Soy buena esperando» · «…Perdón. Eso sonó triste» | encogida | ✅ | — | Confiesa y se disculpa (C2). l. 799: ahora sí sube el libro |
| 969 (+988, 1032, 1037, 1074, 1089, 1096, 1147, 1152, 1221, 1234) | Interc. 1 · grupo | «…» · «…Quiere dividirnos» · «…Itsuki. Eso es justo lo que él quería» · «…Yo estoy bien sola» | neutral | ✅ | — | Bloque de grupo tenso. Se sube los audífonos (l. 1228) (C7) |
| 1744 (+1753, 1797, 1806) | Interc. 3 | «…Tienes ojeras» · «…Es verdad igual» | neutral | ✅ | — | Observación seca |
| 2145 (+2150) | Interc. 4 · observadora, `rama_hub` cálida | «Hola, [mc]» (Miku cálida) / «…Hola, [mc]» · «…Tienes un número escrito en la muñeca» · «…Y sonreía» | neutral | ✅ | — | Revisión P4b: neutral → relajada → encogida (C4). El mismo `show` sirve para su rama cálida y para las demás, y no se puede separar sin insertar (§9) |
| 2175 | Interc. 4 · `rama_hub` cálida | «…Hoy tú tienes uno en el brazo» · «…Está más rara de lo normal. Pero contenta» | relajada | ✅ | — | Revisión P4b |
| 2188 (+2203) | Interc. 4 · `rama_hub` cálida | «…No es por ti» · «…Bueno. Un poco» · (Miku cálida) «…A mí me debes una página» | encogida | ✅ | — | Revisión P4b + N4 (los celos) |
| 2208 (+2229) | Interc. 4 · `rama_hub` tibia | «…Buenos días, [mc]» · «…Cenó dos platos. Hizo ruido. Normal» · «…Solo pregunto» | neutral | ✅ | — | l. 2213 «Lo dijo mirándome una vez. Después volvió al libro» |
| 2236 (+2257) | Interc. 4 · `rama_hub` fría | «…Hola» · «…Yotsuba siempre hace ruido» · «…Pero si fuiste tú, no lo dejes así» | neutral | ✅ | — | l. 2234 «audífonos a medias»; l. 2251 «las páginas no se movían». Preocupación contenida |
| 2278 (+2291, 2334, 2341) | Interc. 4 · grupo | «…Miró el celular y se quedó quieta» · «…Nino nunca se queda quieta» | neutral | ✅ | — | Observadora del grupo (C7) |
| 2830 (+2859, 2903, 2914, 2921) | Interc. 5 · grupo | «…Son cinco materias de examen» · «…Y nosotras somos cinco» · «…Eso quise decir» | neutral | ✅ | — | Revisión N5: el bloque va neutral (C4) |
| 2928 (+2939) | Interc. 5 · Miku cálida | «…Perd—» · «…Que eso no se disculpa» | encogida | ✅ | — | Revisión N2 (C2) |
| 2946 (+2955) | Interc. 5 · resto | «…Perdón. Pienso cosas raras cuando hay examen» · «…Está bien» | encogida | ✅ | — | Revisión N2 (C2) |
| 3110 (tinte) | Interc. 5 · cierre | (línea de `quintillizas`, «Adios.») | encogida (de la 2928 / 2946) | ✅ | — | Línea de grupo. Ver §9 sobre cuánto dura esa `encogida` |
| 3351 (+3362, 3479, 3490) | Interc. 6 · grupo | «…Entonces ya no hay dónde esconderse» · «…Ya lo sé» · «…Pero suena a eso» | neutral | ✅ | — | Grupo (C7) |
| 3560 (+3569) | Interc. 6 · clima mixta | «…Yo me quedo hasta tarde» · «…Si no tengo que hablar mucho» | neutral | ✅ | — | Se ofrece desde la reserva |

### 02_cap1_evento6.rpy (0 `show` + 22 `e6_foco` + 2 `e6_formacion_neutral` + 1 `e6_entrar`)

| archivo:línea | Rama / escena | Diálogo (resumido) | Actual | Veredicto | Propuesta | Por qué |
|---|---|---|---|---|---|---|
| 259 | Lunes, formación | (sin líneas) | neutral | ✅ | — | Formación |
| 360 | Lunes · cálida | «…Sé más de lo que van a preguntar» · «…La silla de enfrente ya no se siente vacía» · «…Ya sé que es demasiado» | animada | ✅ | — | Revisión P3b (C4) |
| 376 | Lunes · tibia | «…Todo, dos veces» · «…Creo que lo sé» · «…No me digas si se me da bien» | neutral | ✅ | — | Revisión P3b |
| 388 | Lunes · fría | «…Estudié lo que entra. …Tres temas» · «…Lo renové» · «…No sé por qué» | neutral | ✅ | — | Revisión P3b. Armadura (C7) |
| 402 | Lunes · no visitada | «…Repasé sola, como siempre» · «…No esperaba a nadie. …Eso quiero pensar» | neutral | ✅ | — | Tranquila en la superficie, como en su queja |
| 2178 | Aula tarde, formación | (sin líneas) | neutral | ✅ | — | Formación |
| 2357 | Aula tarde · cálida | «Entonces salgamos todas a la vez» · «Así nadie se queda de última» | relajada | ✅ | — | Sin «…»: la idea es suya y la dice tranquila (C8) |
| 2367 | Aula tarde · resto | «…Entonces salgamos todas a la vez» · «…Así nadie se queda de última» | neutral | ✅ | — | Misma frase con pausas: la cara también se distingue (C6) |
| 2835 | Tarde · cálida | «Escribí todo lo que sabía» · «Escribí de la sal, hasta el último renglón» · «La goma está entera. Miren» | animada | ✅ | — | Primera vez en voz alta sin «…» (C8) |
| 2853 | Tarde · cálida | «…Eso fue raro. …Pero no retiro lo que dije» | encogida | ✅ | — | Se oye, pero no se disculpa |
| 2862 | Tarde · tibia | «…Escribí lo de las rutas. …Sin la sal» · «…Lo que amo no—» | neutral | ✅ | — | Contenida |
| 2872 | Tarde · tibia | «…Nada. …Perdón.» | encogida | ✅ | — | C2 |
| 2883 | Tarde · fría | «…Cuatro renglones. …Lo que preguntaban» · «…Correcto. …Lo comprobé» | neutral | ✅ | — | Armadura. La mano en los audífonos (l. 2881) no la tiene ningún sprite (§1) |
| 2896 | Tarde · no visitada | «…Escribí largo. …Después borré un poco» · «…Las de no molestar» | neutral | ✅ | — | Contenida |
| 2902 | Tarde · no visitada | «…Perdón. …No quería que sonara triste» · «…Mientes un poco» · «…Gracias igual» | encogida | ✅ | — | C2 |
| 3286 | Departamento, entrada | (narración de llegada: l. 3677 / 3700 / 3719 / 3738) | neutral | ✅ | — | Entrada común a las cinco |
| 3679 | Eco · cálida | «La página ciento veinte. ¿Llegaste?» | neutral | ✅ | — | Pregunta seca, de broma. La risa (l. 3687, «Se rió») es la que motiva el cambio a relajada |
| 3685 | Eco · cálida | «Quería ver tu cara. Ya la vi» · «Gracias, [mc]» | relajada | ✅ | — | Tranquila, sin «…» (C8) |
| 3702 | Eco · tibia | «…Dijiste que se me daba bien» · «…Puede ser. …Lo sigo pensando» | encogida | ✅ | — | El elogio con comparación todavía le pesa |
| 3723 | Eco · fría | «…Contesté lo que entraba. …Estuvo bien» · «…Hoy no» | neutral | ✅ | — | Armadura. Llega «con los audífonos puestos» (l. 3719): §9 |
| 3740 | Eco · no visitada | «…La silla sigue vacía» · «…Dejaré el libro abierto otra vez» · «…Alguien viene» | neutral | ✅ | — | Tranquila en la superficie |
| 3864 | Mesa | «…Hoy me los quito» (fría) / «…Hoy no me los puse» · «…Quiero oír lo que diremos todas» | encogida | ✅ | — | Revisión P3c. l. 3874 «las manos juntas delante del cuerpo» es literalmente el sprite (C1) |
| 3923 | Mesa | «…Sonaron juntas» · «…No es tristeza. …Es que no sé dónde poner esto» | encogida | ✅ | — | Desbordada. La lágrima (l. 3927) no la tiene ningún sprite; `encogida` es lo más cercano |
| 4049 | Mesa | «…Fue lindo» · «…A tu manera… Fue lindo» · «…Gracias por tus palabras, [mc]» | encogida | ✅ | — | Agradecimiento tímido. La mesa es común a todas las ramas, y `relajada` no encajaría en la fría |
| 4091 | Mesa | «…¿Dónde pongo las manos? …Mejor delante» | encogida | ✅ | — | El texto describe el sprite (C1) |

### 02_cap1_final_malo.rpy (14 shows)

| archivo:línea | Rama / escena | Diálogo (resumido) | Actual | Veredicto | Propuesta | Por qué |
|---|---|---|---|---|---|---|
| 175 (+273) | Beat, sala | «…Yo no pedí esto» · «…Tampoco lo evité» | neutral | ✅ | — | Cerrada. l. 280: «Se llevó las manos a los audífonos» |
| 286 (+295) | Beat · Miku fría | «…Dijiste que lo de la sal no entraba en el examen» · «…Tenías razón» · «…Por eso no volví a abrir el libro» | encogida | ✅ | — | No es un reproche a gritos: se encoge al decirlo. Es la única rama con cara propia (C6) |
| 513 (+534, 564, 571, 594) | Hub 3, aula | «…Solo sé la mitad de lo que van a preguntar» · «…Y no sé si esa mitad está bien» | neutral | ✅ | — | Grupo derrotado (C7) |
| 947 (+962) | Aula tarde | (sin líneas) | neutral | ✅ | — | Grupo |
| 1000 (+1015) | Aula tarde | «…Sabía las respuestas» · «…Las escribí. …Las borré» · «…Perdón» | encogida | ✅ | — | C2 |
| 1317 | Despedida | «…Adiós, [mc]» · cálida «…Me preguntaste» / resto «…Yo te lo habría contado» · fría «…Este es el final» | neutral | ✅ | — | Se cierra: l. 1338 «Se subió los audífonos». El `show` es común a las tres ramas (§9) |

---

## 6. Resumen

**Momentos evaluados: 70** (prólogo 2 · apertura 1 · hub 15 · conexiones 21 · E6 25 · final malo 6).

| Veredicto | Momentos | Dónde |
|---|---|---|
| ✅ | **67** | — |
| 🔁 | **3** | apertura 417 · hub 297 · conexiones 315 |
| 🎨 | **0** | Los cuatro sprites cubren todos sus usos. La única carencia (llanto) es de una línea. La diferencia de ropa entre PNG no afecta a ninguna expresión (§0 aviso 4) |
| ➕ | **0** | Ninguna emoción sin sprite se repite en varias líneas en más de una escena |

**Uso de cada expresión** (sentencias `show miku <expr>`; aparte, los `e6_foco` del E6):

| Expresión | Hoy (75 `show`) | Tras 🔁 | E6 `e6_foco` hoy (22) | Tras 🔁 |
|---|---|---|---|---|
| neutral | 57 | 54 | 10 | 10 |
| encogida | 10 | 12 | 8 | 8 |
| relajada | 5 | 5 | 2 | 2 |
| animada | 3 | 4 | 2 | 2 |

A eso se suman, siempre en neutral, las 2 formaciones y la entrada del E6.

**Comprobaciones a–e:**
- **(a) Contradicción con el texto:** dos casos, apertura 417 («libro apretado contra el pecho» + «Perdón») y conexiones 315 («libro a media cara»). Los dos pasan a `encogida`.
- **(b) Inercia de `neutral`:** de las 57, 54 se quedan. Todas son escenas de grupo, ramas fría o no visitada, o momentos en que el narrador la describe cerrada. Ninguna se cambia por inercia (C7).
- **(c) Parpadeo:** uno, hub 297 (animada → neutral → animada). El resto de cambios seguidos llevan una línea que los motiva: interc. 4 (P4b) y el eco cálido del E6 («Se rió», l. 3687).
- **(d) Ramas tras los cambios:**
  - Hub: cálida neutral → animada → encogida → relajada → encogida · tibia encogida → neutral · fría neutral.
  - Reacción: cálida relajada → encogida → relajada · tibia **encogida** (hoy neutral, igual que la fría) · fría neutral.
  - E6 lunes: cálida animada · tibia, fría y no visitada neutral.
  - E6 tarde: cálida animada → encogida · tibia neutral → encogida · fría neutral · no visitada neutral → encogida.
  - E6 eco: cálida neutral → relajada · tibia encogida · fría neutral · no visitada neutral.
  - Final malo: fría encogida en el beat · el resto neutral.
- **(e) Arco:** el prólogo y la apertura solo tienen caras cerradas (neutral; con el 🔁, neutral y encogida). `animada` y `relajada` solo salen cuando habla de lo suyo (hub 245–314, 401, 429) o cuando la rama se ha abierto (reacción cálida 259/301, E6 cálida 360/2357/2835/3685). Hay una excepción, que manda la revisión: la `relajada` de la interc. 4 (l. 2175) la ve cualquier Miku si Yotsuba va por la cálida (P4b). El 🔁 del hub suma un `animada` dentro del mismo tema, así que no adelanta el arco.

---

## 7. Prompt PixAI

**No hace falta ninguno:** no hay 🎨 ni ➕. Queda como base para una expresión futura (vestuario canon: cárdigan, §0 aviso 4). Va sin LoRA de serie, con el LoRA de personaje `中野三玖 アニメ(サンプル)Tsubaki.2バージョン` a **0.8** (§1), lienzo 768×1280 en vertical, normalizado luego a 760×930 con los ojos en la fila 199 (§3) y con cada expresión en silueta propia (§9):

```
masterpiece, best quality, official anime screencap, go-toubun no hanayome style,
1girl, solo, only one person in the entire image, nakano miku,
standing, front view, facing viewer, centered, figure from head to knees, knees at the bottom edge, plain white background, solid white background,
brown hair, medium length hair, shoulder length hair, long bangs covering one eye, blue eyes,
<expresión y pose de la ficha §1, con 2–3 tokens redundantes>,
light blue cardigan, buttoned cardigan, long sleeves past the wrists, white collared shirt, green pleated skirt, dark pantyhose, black tights,
blue headphones, headphones around neck, headphones resting on collarbone, not wearing headphones on ears,
flat even studio lighting, clean lineart, natural hands with five fingers, deep focus
```

Archivo: `game/images/sprites/miku_sprites/miku_<expresion>.png` · declaración: `image miku <expresion> = "sprites/miku_sprites/miku_<expresion>.png"` (las cuatro actuales están en `00_definiciones.rpy` l. 269–272).

---

## 8. Cambios 🔁 por archivo (antes → después)

Solo cambia el atributo de expresión. La posición (`at …`), el `with` y el orden se quedan igual.

**`02_cap1_apertura.rpy`**
```renpy
# l. 417
    show miku neutral at pj(0.5)
# →
    show miku encogida at pj(0.5)
```

**`02_cap1_Miku.rpy`**
```renpy
# l. 297
    show miku neutral at pj_habla(0.5)
# →
    show miku animada at pj_habla(0.5)
```

**`02_cap1_conexiones.rpy`**
```renpy
# l. 315
        show miku neutral at pj_habla(0.5)
# →
        show miku encogida at pj_habla(0.5)
```

**Cómo probarlo (después de aplicar):** en la consola (Shift+O):
- `jump cap1_apertura` y avanza hasta el pasillo (l. 413–426).
- `jump hub_Miku` → la explicación de la sal (l. 245–340).
- Para la reacción tibia: `$ rama_hub = "tibia"` y luego `jump reaccion_miku`. Al terminar, el `return` del bloque te saca al menú principal: es solo para ver la cara.

---

## 9. Fuera de alcance (anotado, no propuesto)

- **Conexiones l. 2159 · `miku "Eso ya era un cambio."`:** es narración del MC puesta en boca de Miku. En la revisión (P4b) es una sola línea del narrador: `narrador "Me saludó sin pausa antes de la primera palabra. Eso ya era un cambio."`. Hoy Miku dice en voz alta lo que piensa el MC. Se arregla cambiando `miku` por `narrador`. **Aplicado** con la aprobación del usuario.
- **Audífonos «puestos» en la narración y al cuello en el sprite:** conexiones l. 334 y 1228, E6 l. 2881 y 3719, final malo l. 280 y 1338. Es por diseño: §2 de la GUIA los quiere siempre al cuello y deja el gesto a la narración. No es un defecto.
- **`encogida` que se alarga en `pj_calla`:** después del «Perdón» de la interc. 5 (l. 2939 / 2955), Miku se queda encogida y atenuada hasta el `hide` de la l. 3123, unas 165 líneas sin hablar. Pasa lo mismo, más corto, en la interc. 4 (l. 2203). Para que se recomponga habría que **añadir** un atributo a un `show` de solo tinte (`show miku neutral at pj_calla(X_MIKU)`). La regla es cambiar el atributo que ya está, y atenuada se lee como «sigue con el libro a media cara». No lo propongo.
- **`show` compartidos entre ramas:** interc. 4 l. 2150 (la Miku cálida, que saluda sin pausa, y la que no) y final malo l. 1317 (cálida, tibia y fría). Separarlos exige insertar `show` dentro de cada rama.
- **Despedida de conexiones (l. 3855 / 3889):** no hay sprite para ninguna de las cinco. Si se quiere, es una decisión de escena para todas, no de Miku.
- **Falda de dos verdes entre los PNG** (§0 aviso 4). No justifica regenerar nada.
- **Tinte repetido en bloques de grupo:** prólogo l. 970 y conexiones l. 1089 repiten `show miku at pj_habla(X_MIKU)` dentro de un bloque que pone el tinte a las cinco. No cambian la cara ni el tinte. Se dejaron para no romper el bloque.
