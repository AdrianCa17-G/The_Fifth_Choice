# Evaluación de sprites · Nino · Prólogo + Capítulo 1

> Revisado sobre el árbol de trabajo actual (commit `19d226e`, con cambios sin commitear en otros archivos).
> Es una evaluación: no se tocó ningún `.rpy`. Los números de línea son los de hoy.
> **Estado (13/11/2026):** los 19 🔁 del §7 están aprobados y aplicados; Lint no da errores de sprites. El ➕ `nino seria` también está aplicado: el PNG (760×930 RGBA, ojos en la fila ~201) está declarado en `00_definiciones.rpy` l. 267 y los 8 cambios del §8 están puestos. Lint no da errores nuevos.
> Fuentes: `docs/GUIA_ARTE.md` §2, §3, §6 y §9 · `docs/GUIA_RENPY.md` §1 («Las expresiones son atributos») y §2 (la regla del `show`) ·
> `docs/REVISION_PERSONAJES_CAP1/REVISION_NINO_CAP1.md` (manda sobre cualquier propuesta) · los siete `.rpy` del recorrido.

---

## 0. Avisos: dónde el encargo y los archivos no dicen lo mismo (mandan los archivos)

| # | El encargo dice | Los archivos dicen | Qué hice |
|---|---|---|---|
| 1 | E6: 4 shows | `02_cap1_evento6.rpy` además pinta a Nino con **27** `call e6_foco("nino", …)`, **2** `call e6_formacion_neutral` (l. 259 y 2178) y **1** `call e6_entrar(e6_h)` (l. 3286). Ninguno cuenta en los 118. | Los evalué todos. En E6 Nino tiene 32 momentos con sprite, no 4. |
| 2 | Blazer negro | `GUIA_ARTE.md` §2: «Blazer azul marino con ribete blanco». Los cuatro PNG lo tienen azul marino. | Prompt con azul marino. |
| 3 | Moños negros | §2: «lazos negros con verde a ambos lados de la cabeza». Los PNG llevan lazos negros con alas verdes de mariposa. | Prompt con lazos negros y verdes. |
| 4 | Medias altas blancas | §2: «calcetas blancas altas». No se ven en ningún sprite: el lienzo corta por encima de la rodilla. | Van en el prompt por continuidad; el recorte las deja fuera. |
| 5 | LoRA de serie ≤0.3 y LoRA individual 0.7–0.8 | §1, «Pesos de LoRA»: sprite individual de una hermana → **sin LoRA de serie**, personaje **0.8**. El 0.3 / 0.7–0.8 es para un **CG** individual. | Prompt sin LoRA de serie y con el de Nino a 0.8. |

---

## 1. Ficha de los 4 sprites

| Sprite | Pose y brazos | Mirada | Boca | Lo que transmite de verdad | Lo que NO cubre |
|---|---|---|---|---|---|
| `nino neutral` | De frente, **brazos cruzados** altos sobre el pecho, piernas juntas. | Cejas fruncidas, ojos de frente. | **Dientes apretados**, mueca. Rubor. | Fastidio a la defensiva, el tsundere con la guardia arriba. **No es una cara en reposo.** | Calma, sinceridad, tristeza contenida, orgullo tranquilo. |
| `nino molesta` | **Brazos en jarra** (manos en la cadera, codos hacia fuera). | Párpados a media altura, mirada plana. | Cerrada, un mohín pequeño. Rubor leve. | Reproche frío, mandona («Corta las cebollas. Finas.»), una mirada fría. | Rabia caliente, vergüenza, vulnerabilidad. |
| `nino pillada` | **Brazos abajo**, separados del cuerpo, **puños cerrados** a los lados de la falda. Descruza los brazos. | Ojos abiertos, apartando un poco la vista. | Puchero ondulado con colmillo. **Rubor fuerte.** | Pillada: niega a gritos, se le escapa el cariño. | Seriedad, tristeza, frialdad. |
| `nino nerviosa` | **Una mano al mentón o al cuello**; la otra cuelga. El cuerpo se ladea un poco. | Ojos inquietos, cejas arriba. | Entreabierta, temblando. Rubor. | Inquietud, duda, vulnerabilidad, la voz a punto de quebrarse. | Calma, firmeza, frialdad. |

**Regla de §9 (a un 30 % solo se lee la silueta):**

- **`neutral` ↔ `molesta`: la silueta las separa, la emoción no.** Brazos cruzados contra brazos en jarra se distinguen bien. Pero las dos dicen «hostil»: pasar de una a otra se lee como que *se movió*, no como que *cambió de emoción*. Sirve para marcar un cambio de compás, no un cambio de sentimiento.
- **`pillada` ↔ cara en reposo: es el par peligroso.** Con los brazos abajo, `pillada` tiene la silueta más «quieta» de las cuatro. Lo que la hace pillada (rubor y puchero) está en la cara, y a un 30 % no se ve. En los planos a solas (x = 0.5) se lee. En formación de cinco (E6 l. 446 y 2307, interc. 6 l. 3447) se lee peor.
- **`pillada` ↔ `nerviosa`:** las dos van ruborizadas y sin cruzar los brazos, pero la mano levantada de `nerviosa` las separa. Se distinguen ✓.
- **No hay ninguna cara tranquila.** El único sprite que el juego llama `neutral` aprieta los dientes. Es correcto como reposo *narrativo*: el texto confirma cinco veces que su postura de siempre son los brazos cruzados (beat l. 216 y 511; conexiones l. 201; E6 l. 2353 y 3007). Pero todos los momentos serenos, sinceros o tristes de verdad caen en `neutral` y pasan a leerse como fastidio. De ahí sale el ➕ del §6.

---

## 2. Criterios aplicados (los mismos servirán para las otras cuatro)

- **C1 · La narración manda.** Si el narrador describe brazos, manos o mirada, va el sprite que lo cumple (por ejemplo: «con los brazos cruzados» → `neutral`; «mirada fría» → `molesta`).
- **C2 · Cuándo es `pillada`.** Cuando alguien la pilla (el MC, el narrador o una hermana) o cuando el cariño se le escapa en una frase. Si se corta sola con un «olvídalo» y nadie la ha pillado, va `molesta`: está molesta consigo misma.
- **C3 · La cara se escapa en la línea y el `pj_calla` la recompone.** En los deslices breves no se cambia el `show … pj_calla` que viene después: volver a la armadura *es* el gesto tsundere. No vale para los estados de ánimo que duran toda la escena.
- **C4 · La revisión manda.** N4 (el táper: `molesta` → `pillada` → `neutral`) se respeta tal cual. N5 dice que el nombre va «escondido en una instrucción», así que en la puerta cálida va la cara de dar órdenes, no la de pillada.
- **C5 · Parpadeo.** Nada de A → B → A en réplicas seguidas, ni cambios de cara sin una línea que los motive. Se arregla cambiando el atributo por el del vecino, que entonces no cambia nada en pantalla. Ningún `show` se borra.
- **C6 · Ramas.** En el mismo punto del guion, cálida, tibia y fría llevan caras distintas siempre que el texto lo permita.
- **C7 · `neutral` es su armadura, no su reposo.** No se cambia por inercia en las escenas de grupo hostiles, porque ahí es justo lo que tiene que transmitir.

Veredictos: ✅ queda bien · 🔁 cambiar a otra expresión existente · 🎨 rehacer el sprite · ➕ sprite nuevo.

---

## 3. Líneas de Nino sin sprite en pantalla

| Archivo · líneas | Qué hay en pantalla | ¿Intencional? |
|---|---|---|
| `01_prologo.rpy` 647–665 | CG `cg_nino_pasillo` (l. 644) | Sí, es CG |
| `01_prologo.rpy` 806 | CG `cg_yotsuba_corriendo` (l. 777) | Sí, es CG |
| `01_prologo.rpy` 1178–1186 | CG `cg_hermanas_estudiando` (l. 1131) | Sí, es CG |
| `02_cap1_apertura.rpy` 206–216 | CG `cg_cinco_sentadas` (l. 179) | Sí, es CG |
| `02_cap1_Nino.rpy` 250–262 | CG `cg_nino_receta` (l. 247) | Sí, es CG |
| `02_cap1_Nino.rpy` 534–554 | CG `cg_nino_llamada` (l. 531): la llamada a papá | Sí, es CG |
| `02_cap1_beat_Nino.rpy` 79–103 y 199 | CG `cg_nino_confrontacion_cocina` (l. 76). La 199 está en el `else:` (l. 193), que no cambia de escena | Sí, es CG |
| `02_cap1_beat_Nino.rpy` 280–306 | CG `cg_nino_grieta_cocina` (l. 273) | Sí, es CG |
| `02_cap1_conexiones.rpy` 3847 | `bg_departamento_anochecer` (l. 3801) sin ningún sprite: Yotsuba e Itsuki hablan igual sin sprite | Parece intencional: escena coral de montaje en la que nadie tiene sprite |
| `02_cap1_evento6.rpy` 1145–1385 (los **87** `nino_int`) y 1417, 1448, 1471, 1490 | CG `cg_nino_examen` (l. 1105). El minijuego (`mj_ejecutar`) usa `call_screen` y no cambia la escena | Sí: voz interior sobre CG |
| `02_cap1_evento6.rpy` 4127–4173 | CG `cg_cinco_aprobadas` (l. 4104/4109/4114) | Sí, es CG |
| `02_cap1_final_malo.rpy` 784 | CG `cg_nino_fracaso` (l. 765) | Sí, es CG |

**No falta ningún sprite.** Las 87 líneas de `nino_int` del E6 son voz interior sobre el CG del examen. Las líneas habladas del E6 sí tienen sprite, por `e6_foco`.

---

## 4. Tabla por archivo

Un momento es el `show` (o `e6_foco`) donde cambia la expresión más las líneas de Nino que cubre. Los `show nino at …` que solo cambian el tinte van en el momento que los contiene.

### 01_prologo.rpy (13 shows)

| archivo:línea | Rama / escena | Diálogo (resumido) | Actual | Veredicto | Propuesta | Por qué |
|---|---|---|---|---|---|---|
| 732 (+735, 743, 748, 757, 764) | Sala, con Ichika | «Contigo probablemente tarde años» · «El último duró cuatro días» · «libros para nerds» | neutral | ✅ | — | Hostil a la defensiva: es su primera cara de verdad (C7) |
| 817 (+826) | Sala | «¿Y eso te parece raro?» | neutral | ✅ | — | Seca, cortante |
| 945 (+948, 960, 969) | Sala, las cinco | «¿No ves que se están matando con la mirada?» · «Quintillizas. Búscalo en un diccionario» | neutral | ✅ | — | Sarcasmo con los brazos cruzados, lidera al grupo |
| 1052 | Coro «¡No pensamos estudiar!» | (línea de `quintillizas`) | neutral | ✅ | — | Bloque hostil del grupo |

### 02_cap1_apertura.rpy (8 shows)

| archivo:línea | Rama / escena | Diálogo (resumido) | Actual | Veredicto | Propuesta | Por qué |
|---|---|---|---|---|---|---|
| 269 (+298, 301, 307, 313, 332) | Hojas idénticas | «Qué observación tan interesante» · «El último duró cuatro días. Tú llevas uno» · «Yotsuba.» | neutral | ✅ | — | Sabotaje frío desde la armadura |
| 381 | Anochecer | «Had to. No "jad tu". Se pega, no se separa» | neutral | ✅ | — | Corrige sin pensarlo: todavía no se ha dado cuenta |
| 388 | Anochecer | «…» · «¡No te he corregido a ti!» · «¡Fuera de mi casa!» | pillada | ✅ | — | La pillada de manual (C2) |

### 02_cap1_Nino.rpy (17 shows · hub con ramas)

| archivo:línea | Rama / escena | Diálogo (resumido) | Actual | Veredicto | Propuesta | Por qué |
|---|---|---|---|---|---|---|
| 116 (+123) | Súper, todas | «¿Tú?» · «No te pedí que me buscaras» · «Busca a otra a quien fastidiar» · lee las etiquetas | neutral | ✅ | — | Protege la cesta con los brazos cruzados |
| 188 | Todas | «No es lo mismo leer que…» · «Da igual. Olvídalo» | molesta | ✅ | — | Se corta sola y nadie la ha pillado (C2) |
| 209 / 228 | Hub 3 / hubs 1–2 | «Los que entraron antes también sonreían el primer día» · «perdí la cuenta…» | nerviosa | ✅ | — | Se abre, vulnerable |
| 283 (+290, 313) | Todas, tras el CG; y la fría m4c 487–505 sin `show` propio | «Olvida lo que dije» · «¿Y bien?» / fría: «Eso mismo dijo el que llegó antes de ti» · «Guárdate la promesa» | neutral | ✅ | — | Vuelve a la armadura (narrador: «Se acomodó el uniforme»). En la fría no se abre en toda la escena (C6) |
| 365 | Cálida | «Esa es la primera vez que alguien no me promete nada» | nerviosa | ✅ | — | La l. 376 dice «sin la hostilidad de antes ni la calma que tampoco tiene»: una cara tranquila contradiría el texto |
| 378 | Cálida | «Eso no significa que confíe en ti» · «Que quede claro» | molesta | ✅ | — | La etiqueta mandona |
| 389 | Cálida | «No le digas a mis hermanas que hablé de más» | pillada | ✅ | — | Pillada |
| 396 | Cálida | «Tú entendiste. Con eso alcanza» | neutral | 🔁 | **pillada** | C5: pillada (1 línea) → neutral (1 línea) en réplicas seguidas. Además es el cariño de la cálida que se le escapa (e) |
| 428 | Tibia | «¿Qué haces?» · «No te pedí ayuda» | molesta | ✅ | — | Reproche |
| 441 | Tibia | «…Esa cesta pesa más de lo que parece» · «Esto no significa nada» | neutral | 🔁 | **pillada** | La l. 448 dice «lo más parecido a un agradecimiento»: es el cariño que se le escapa (e). Y la l. 461 dice «ella sin saber dónde poner las manos»: los brazos cruzados lo contradicen (C1) |
| 454 | Tibia (calla) | narración 459–467 | neutral | 🔁 | **pillada** | La l. 461 cae durante este `calla`: necesita los brazos sueltos (C1 manda sobre C3) |
| 507 | Fría (calla) | narración 510–514 | neutral | ✅ | — | Fría: cerrada hasta el final (C6) |

### 02_cap1_beat_Nino.rpy (17 shows · ramas `nino_rama_beat`)

| archivo:línea | Rama / escena | Diálogo (resumido) | Actual | Veredicto | Propuesta | Por qué |
|---|---|---|---|---|---|---|
| 218 (+229) | Todas | «No es un buen momento» · «Entonces ya sabes lo que pienso de ti» | neutral | ✅ | — | La l. 216: «todavía con los brazos cruzados» (C1) |
| 262 | Todas | «Quiero que te vayas» · «Mi padre no tiene que vivir con esto…» | molesta | ✅ | — | Confrontación |
| 313 | Todas, vuelta del CG | «…» | neutral | 🔁 | **pillada** | C5: una sola línea en neutral y en la siguiente ya está pillada (318). Vuelve del CG ya pillada por haber hablado de más |
| 318 | Todas | «No dije nada de esto» | pillada | ✅ | — | Pillada |
| 359 | Todas + inicio de la cálida (396, 402) | «¿Vas a decir que esta vez es distinto?» · «¿¿Qué?» · «Nadie. No hace falta» | neutral | ✅ | — | La l. 355 dice «se acomodó el uniforme»: vuelve a la armadura |
| 412 | Cálida | «Lo hice porque…» · «No es lo que piensas» | nerviosa | ✅ | — | Vulnerable |
| 425 | Cálida | «Hay que hacer la cena. Son las cinco» | pillada | ✅ | — | Cambia de tema porque la han pillado |
| 432 | Cálida | «Corta las cebollas. Finas» · «No es una invitación» | molesta | ✅ | — | Órdenes |
| 445 | Cálida | «Exacto.» | neutral | 🔁 | **molesta** | C5: molesta → neutral (1 línea) → molesta (456). Sigue dando órdenes |
| 456 | Cálida (N4) | «Eso es para ti. Lo que sobre» | molesta | ✅ | — | La revisión N4 la pide (C4) |
| 463 | Cálida (N4) | «…Va a sobrar» | pillada | ✅ | — | N4 (C4) |
| 472 | Cálida (N4) | (sin líneas) | neutral | ✅ | — | N4 (C4) |
| 494 | Tibia | «¿Qué haces?» · «No la reventé» | molesta | ✅ | — | Reproche |
| 513 | Tibia | «No esperaba que te quedaras…» · «No dije eso tampoco» | neutral | ✅ | — | La l. 511: «Con los brazos cruzados otra vez» (C1) |
| 547 | Fría | «Genial» · «Dos semanas aquí y ya sabes… para que me calle» | molesta | ✅ | — | Frialdad dolida |
| 558 | Fría | «Es la forma elegante de lo mismo» · «Hablan el mismo idioma» | neutral | 🔁 | **molesta** | C6: hoy la tibia y la fría hacen la misma secuencia (molesta → neutral). La fría es «precisa», la mirada fría de `molesta` |

### 02_cap1_conexiones.rpy (65 shows)

| archivo:línea | Rama / escena | Diálogo (resumido) | Actual | Veredicto | Propuesta | Por qué |
|---|---|---|---|---|---|---|
| 162 | reaccion_nino · cálida | «Oye, tú» · «Ni una palabra a mis hermanas» | neutral | ✅ | — | Armadura |
| 171 | Cálida | «Y come algo antes de clases» · «Tienes la peor cara…» | molesta | ✅ | — | El cuidado va disfrazado de regaño, y la revisión (§1 · «Lo cuida a escondidas») lo quiere así. La cara cambia cuando la pillan (siguiente fila) |
| 180 | Cálida | «¡No! Es que si te desmayas, nos echan la culpa» · «…Nadie me había hablado así» | nerviosa | 🔁 | **pillada** | La pilla el MC en la l. 178 («¿Eso es preocupación?») y responde «¡No!», negando a gritos (C2). Es el cariño que se le escapa (e) |
| 191 (+198) | Cálida | «Eso no significa que confíe en ti» · «No te hagas ideas» | molesta | ✅ | — | La l. 201 dice «se le olvidó cruzar los brazos»: brazos en jarra ✓ (C1) |
| 205 (+214) | Tibia | «Lo que pasó sigue sin significar nada» · «Y que quede así» | neutral | ✅ | — | Tibia distinta de la cálida (C6) |
| 221 (+238) | Fría | «Guárdate el "buenos días"» · «Anota la fecha» | molesta | ✅ | — | Fría = mirada fría (C6) |
| 686 (+689) | queja_nino | «Ni creas que me molesta» · «Me da exactamente igual» | neutral | ✅ | — | Armadura |
| 702 | queja_nino | «Eso cuenta como visita. Por desgracia» · «¡NO! ¡Fue un "qué alivio"!» | molesta | 🔁 | **pillada** | La revisión §1 pone esta línea (711) como su forma de reaccionar cuando la pillan: «niega a gritos y en mayúsculas» (C2, C4) |
| 713 | queja_nino | «…Mira. No esperaba nada» · «alguien tiene que ser la que no cambia. Para que las demás tengan a dónde volver» | neutral | ➕ | **seria** (§6) · mientras tanto ✅ | Sinceridad tranquila: los dientes apretados la contradicen. Ninguno de los cuatro sprites la cubre |
| 730 (+739) | queja_nino | «Que quede claro» · «¡Y deja de poner esa cara de culpa!» | pillada | ✅ | — | Pillada |
| 968 (+987, 1011, 1038, 1045, 1051, 1057, 1073, 1088, 1115, 1126, 1209, 1214) | Interc. 1, las cinco | «tu tercer fracaso» · «renunciar y largarse» · «Yotsuba.» · «Quiere separarnos» · «¿Quién querría estar con ese nerd?» | neutral | ✅ | — | Lidera la hostilidad del grupo (C7) |
| 1241 | Interc. 1, cierre | «Treinta días, tutor. A ver a cuántas logras encontrar» | neutral | 🔁 | **molesta** | (b): 13 shows seguidos en neutral. El cierre es un reto y lleva brazos en jarra |
| 1448 | Interc. 2 · cálida (l. 1446) | «¿Qué le hiciste a [nombre_h]?» | neutral | ✅ | — | Interrogatorio |
| 1463 | Cálida | «Ya. El método» | molesta | ✅ | — | Sospecha |
| 1472 | Cálida | «¿Y por qué no me buscaste a mí primero?» · «¡Me molesta que hagas planes…, tonto!» | pillada | ✅ | — | Pillada (R1 de la revisión) |
| 1489 | Cálida | «[nombre_h] es mi hermana» · «sigo diciendo que no vas a durar» | molesta | ✅ | — | Recupera el mando |
| 1513 | Interc. 2 · tibia (l. 1511) | «Oye, tú» · «no armas escándalo» | neutral | ✅ | — | Armadura |
| 1526 | Tibia | «No te lo tomes como un halago» | molesta | 🔁 | **neutral** | C5: neutral → molesta (1 línea) → neutral. Niega sin descruzar los brazos |
| 1533 | Tibia | «…Pero sí. Me tranquiliza» · «Los que entran haciendo ruido…» | neutral | 🔁 | **pillada** | Es el cariño que se le escapa (e) |
| 1540 | Tibia (calla) | narración | neutral | ✅ | — | La l. 1543 dice «Se fue con la misma cara con la que llegó»: vuelve a `neutral` (C1, C3) |
| 1553 (+1584) | Interc. 2 · fría (l. 1551) | «Nadie dice "estoy bien" tres veces si lo está» · «No pensé que tardarías tan poco» · «Hoy no la saludes» | neutral | ➕ | **seria** (§6) · si el ➕ no se aprueba: 🔁 **molesta** | La l. 1558 dice «Nino no gritó»; la 1576, «No estaba enojada. Estaba decepcionada»; la 1587, «No hubo insultos». Los dientes apretados dicen rabia. `molesta` (boca cerrada, mirada fría) se acerca; `seria` es la cara exacta |
| 1743 (+1752, 1807, 1816) | Interc. 3 | «Van casi diez días. Y seguimos igual» | neutral | ✅ | — | Armadura |
| 2712 (+2719) | Interc. 5 · cálida (l. 2715) | «No me mires así» · «Y no sabes nada» | neutral | ✅ | — | Armadura |
| 2732 | Cálida | «…Gruesas. Las cortaste gruesas» | pillada | ✅ | — | Pillada |
| 2739 | Cálida | «No fue una invitación. Que quede claro» · «Exacto» | molesta | ✅ | — | Órdenes |
| 2748 | Cálida | «Solo… hoy no me preguntes nada» · «no voy a saber qué contestar» | neutral | 🔁 | **nerviosa** | La l. 2758 lo llama «un ruego disfrazado de orden». La cara tiene que enseñar el ruego |
| 2755 | Cálida (calla) | narración 2758 | neutral | ✅ | — | Vuelve a la armadura: es el disfraz (C3) |
| 2762 | Tibia (l. 2760) | «Sigo sin tener ganas de hablar de aquello» · «Más te vale» | neutral | ✅ | — | Armadura |
| 2773 | Tibia | «…Lavaste mi taza» · «Nadie toca mi taza» | molesta | ✅ | — | Reproche |
| 2784 | Tibia | «…O sea. Haz lo que quieras» | neutral | 🔁 | **pillada** | La l. 2792 dice «lo más parecido a un "gracias"»: es el cariño que se le escapa (e) |
| 2789 | Tibia (calla) | narración 2792 | neutral | ✅ | — | Se recompone (C3) |
| 2802 (+2811) | Fría (l. 2794) | «No lo repitas» · «Empezando por no hablarte» | molesta | ✅ | — | La l. 2816 dice «Con la misma calma que su padre»: frialdad (C1) |
| 2826 (tinte) · 2860 · 3111 (tinte) | Las cinco, exámenes | (sin líneas de Nino) | (la de la rama) / neutral | ✅ | — | Está callada |
| 3350 (+3361, 3426) | Interc. 6 · todas; mixta 3458–3462, mala 3468–3472 | «Dejen de hacerlo parecer una hazaña» · buena: «no fue el peor tutor» · mixta: «Ya lo veremos» · mala: «Solo has empeorado las cosas» | neutral | ✅ | — | El sonrojo lo marca la l. 3445 *después* del «no fue el peor tutor», y ahí entra `pillada` |
| 3447 (+3478) | Buena | «Idiota» · «Que quede claro que eso no es un cumplido» | pillada | ✅ | — | Pillada |
| 3503 (+3508) | Todas | «¿Y quién te nombró jefa?» | neutral | ✅ | — | Choque con Itsuki |

### 02_cap1_evento6.rpy (4 `show` + 27 `e6_foco` + 2 `e6_formacion_neutral` + 1 `e6_entrar`)

| archivo:línea | Rama / escena | Diálogo (resumido) | Actual | Veredicto | Propuesta | Por qué |
|---|---|---|---|---|---|---|
| 259 | Lunes, formación | (sin líneas) | neutral | ✅ | — | Formación |
| 446 | Lunes · visitada (cálida/tibia/fría) | «Treinta días. Y sigues viniendo» · «Y no pongas esa cara» · «Si me viste mover los labios…, no viste nada» | pillada | ✅ | — | Negar después de que la pillen |
| 460 | Lunes · no visitada | «No viniste a buscarme…» · «Contaba los días. Es distinto» | neutral | ✅ | — | Cerrada (§6.4 de la revisión: culpa e intriga) |
| 2178 | Aula tarde, formación | (sin líneas) | neutral | ✅ | — | Formación |
| 2251 (+2299) | Aula tarde | «¿Cómo que no te acuerdas?» · «Estoy esperando a que se vacíe el pasillo» | molesta | ✅ | — | Regaño / excusa |
| 2307 | Aula tarde | «…Pues espero a que se vacíe más» | pillada | ✅ | — | La pilla Ichika |
| 2335 | Aula tarde | «Nadie le va a preguntar nada» · «Mañana se sabe. Y ya» | neutral | ✅ | — | La l. 2353 («Nino descruzó los brazos») necesita que antes los tenga cruzados (C1). El descruce se ve recién en la l. 2381 (ver §8) |
| 2381 | Aula tarde | «No hubo votación» | molesta | ✅ | — | Brazos ya descruzados ✓ |
| 2674 | Tarde · cálida | «Terminé… Y me fui» · «Sin quedarme de guardia» · «Por primera vez, no necesité saberlo antes» | neutral | ➕ | **seria** (§6) · mientras tanto ✅ | La culminación serena del arco. Los dientes apretados la contradicen |
| 2684 | Cálida | «…No sé de qué hablas» | pillada | ✅ | — | La pilla el «Te vi salir» |
| 2695 | Tarde · tibia | «Me quedé revisando» · «Si aprobamos las cinco… quizás esta vez no—» | neutral | ✅ | — | Armadura |
| 2705 | Tibia | «Olvídalo. Da igual» | molesta | ✅ | — | Se corta sola (C2) |
| 2714 | Tarde · fría | «Revisé hasta la campana» · «Pues mira a otra» | molesta | ✅ | — | Fría (C6) |
| 2731 | Tarde · no visitada | «Revisé cuarenta minutos» · «Seguías en tu sitio» | neutral | ✅ | — | Armadura |
| 2741 | No visitada | «No te lo estoy agradeciendo» | molesta | ✅ | — | Etiqueta |
| 2960 | Puerta · cálida | «Sal, [mc]. Si no sales tú, aquí no sale nadie» | neutral | 🔁 | **molesta** | La l. 2967 dice «Lo dijo como una orden», y la revisión N5 habla de «el cariño escondido en una instrucción» (C4): va la cara de dar órdenes. Además separa la cálida de las otras dos (C6) |
| 2985 | Puerta · tibia | «No te estoy esperando. Estoy sujetando una puerta» | neutral | 🔁 | **pillada** | La l. 2992 la desmiente («Una puerta con tope en el suelo. Se sujeta sola»): la pilla el narrador (C2, C6) |
| 3004 | Puerta · fría | «Has tardado» · «Esperaba a que salieras para cerrar» | molesta | 🔁 | **neutral** | La l. 3007 dice «con los brazos cruzados» (C1) |
| 3029 | Puerta · no visitada | «Siempre salgo última. Para cerrar» | neutral | ✅ | — | Armadura. Ningún sprite tiene la mano en el picaporte |
| 3286 (`e6_entrar`) + 3487 | Eco · cálida | «Tú llevas treinta y cinco» · «Son cálculos» | neutral | ✅ | — | La l. 3485 dice «con su cara en alto» |
| 3495 | Cálida | «Que no se entere Yotsuba de que llevaba la cuenta» | pillada | ✅ | — | Pillada |
| 3510 | Eco · tibia | «Pesa. No te estoy pidiendo ayuda» · «…Esta pesa más de lo que parece» | neutral | 🔁 | **pillada** | La l. 3508 dice «con una bolsa del supermercado en cada mano»: no puede tener los brazos cruzados (C1). `pillada` tiene los brazos abajo y los puños cerrados. Repite el hub tibio (l. 441, que también pasa a `pillada`) |
| 3533 | Eco · fría | «Sigues aquí» · «Pues anota la fecha» | molesta | ✅ | — | La l. 3541 dice «sin rabia»: mirada fría |
| 3545 | Eco · fría | (sin líneas: le sigue `e6_foco("", "")`) | neutral | 🔁 | **molesta** | C5: cambia de cara sin ninguna línea que lo motive |
| 3556 | Eco · no visitada | «Alguien tenía que ser a la que no iban a buscar» · «…Eso sonó mejor en mi cabeza» | neutral | ➕ | **seria** (§6) · mientras tanto ✅ | Melancolía sincera |
| 3834 | Mesa | «No hay ninguna ventana abierta» | neutral | ✅ | — | Seca |
| 3856 | Mesa | «Seis personas en esta mesa» · «Es una observación» | nerviosa | ✅ | — | Tensión antes de los boletines |
| 3882 | Mesa | «Tú estuviste con él… Sabes algo» | molesta | ✅ | — | Acusa |
| 3906 | Mesa | «A la de tres» · «Una. Dos. Y…» | neutral | ✅ | — | Organiza |
| 3941 | Mesa | «Cinco. Los conté dos veces» · «Si alguien dice algo, me voy» | nerviosa | ✅ | — | La l. 3953 dice «Se le quebró la voz»: la mano al cuello acompaña |
| 4041 | Mesa | «…Eso fue un discurso» · «Las conté» | molesta | ✅ | — | Desvía el tema |
| 4087 | Mesa | «Un solo brazo. Es mi mejor ángulo» | neutral | ✅ | — | Broma seca |

### 02_cap1_final_malo.rpy (18 shows)

| archivo:línea | Rama / escena | Diálogo (resumido) | Actual | Veredicto | Propuesta | Por qué |
|---|---|---|---|---|---|---|
| 110 | Despido A (cocina) | «Ya ves» · «Era lo que pedí» · «No es un cumplido» · «Es mejor así» | neutral | 🔁 | **molesta** | La l. 133 dice «Lo dijo con esa mirada fría, como siempre» (C1). Los dientes apretados son rabia, no frialdad |
| 170 (+174, 194, 203, 209, 214, 244, 250) | Despido A, llegan las cuatro | «Papá lo despidió» · «Hoy. Hace cinco minutos» · «Yotsuba.» | neutral | ✅ | — | Con el `show` de la 110 cambiado, el cambio cae aquí, cuando entran sus hermanas: delante de ellas vuelve la armadura |
| 512 (+533) | Hub 3 malo · aula | (sin líneas) | neutral | ✅ | — | Formación |
| 582 | Aula | «Ya basta de rodeos» · «No aprendimos nada» · «Aunque no sea solo culpa tuya» | neutral | ➕ | **seria** (§6) · mientras tanto ✅ | Franca, no rabiosa |
| 946 (+961) | Aula tarde | (sin líneas) | neutral | ✅ | — | Formación |
| 1048 (+1061) | Aula tarde | «Va a pasar lo que dije que pasaría» · «Y no me siento mejor por tener razón» · «No sé de qué hablas» | neutral | ➕ | **seria** (§6) en la 1048 · mientras tanto ✅ | Tristeza contenida. El `calla` de la 1061 se queda en neutral (C3) |
| 1355 | Despido B | «Mi padre te va a pagar lo del mes. Acéptalo» · «No me des las gracias» | neutral | ➕ | **seria** (§6) · mientras tanto ✅ | Despedida sobria |
| 1364 | Despido B | «Yo ni siquiera sé si…» · «Cuídate» / fría: «Anota la fecha… Aquí la tienes» | nerviosa | ✅ | — | Se corta a mitad de frase |

---

## 5. Resumen

**Momentos evaluados: 111** (prólogo 4 · apertura 3 · hub 12 · beat 16 · conexiones 36 · E6 32 · final malo 8).

| Veredicto | Momentos | Dónde |
|---|---|---|
| ✅ | **85** | — |
| 🔁 | **19** | Hub 396, 441, 454 · beat 313, 445, 558 · conexiones 180, 702, 1241, 1526, 1533, 2748, 2784 · E6 2960, 2985, 3004, 3510, 3545 · final malo 110 |
| 🎨 | **0** | Rehacer `neutral` cambiaría sus 83 + 12 usos, y el texto pide los brazos cruzados (cinco citas, §1). No se toca |
| ➕ | **7** | conexiones 713 y 1553 · E6 2674 y 3556 · final malo 582, 1048 y 1355 → `nino seria` |

**Uso de cada expresión** (sentencias `show nino <expr>`; aparte, los `e6_foco` del E6):

| Expresión | Hoy (118 `show`) | Tras 🔁 | Tras 🔁 + ➕ | E6 `e6_foco` hoy (27) | Tras 🔁 | Tras 🔁 + ➕ |
|---|---|---|---|---|---|---|
| neutral | 83 | 72 | 66 | 12 | 10 | 8 |
| molesta | 20 | 22 | 22 | 9 | 10 | 10 |
| pillada | 9 | 18 | 18 | 4 | 5 | 5 |
| nerviosa | 6 | 6 | 6 | 2 | 2 | 2 |
| seria | — | — | 6 | — | — | 2 |

Si el ➕ no se aprueba y se aplica la alternativa de conexiones 1553/1584, `show` queda así: neutral 70 · molesta 24 · pillada 18 · nerviosa 6.

**Ramas tras los cambios (d):**
- Hub: cálida nerviosa → molesta → pillada · tibia molesta → pillada · fría neutral de principio a fin.
- Beat: cálida nerviosa → pillada → molesta → pillada · tibia molesta → neutral · fría molesta de principio a fin.
- Puerta del E6: cálida molesta · tibia pillada · fría neutral.
- Eco del E6: cálida neutral → pillada · tibia pillada · fría molesta.

**Tsundere (e):** el cariño que se le escapa tiene cara propia, `pillada`, y nunca `molesta`. Pasa a usarse en todos los deslices que el narrador señala: «lo más parecido a un agradecimiento / un "gracias"» (hub 448, interc. 5 2792), «Me tranquiliza» (1533), «Tú entendiste» (396) y el «¡No!» de la 183. Hay una excepción a propósito: la puerta cálida, donde la revisión N5 pide que el cariño vaya **escondido en una orden**.

---

## 6. ➕ Sprite nuevo: `nino seria`

**Por qué.** Ninguno de los cuatro tiene la boca relajada ni la mirada tranquila: los cuatro están ruborizados y tres de ellos crispados. Los momentos serenos, sinceros o de tristeza contenida acaban en `neutral`, que aprieta los dientes.

**Qué cubriría: 36 líneas en 7 escenas de 3 archivos, en las cuatro rutas.**

| Escena | archivo:línea del `show` | Líneas de Nino | Ruta |
|---|---|---|---|
| queja_nino | `02_cap1_conexiones.rpy:713` | 716, 718, 720, 724, 726, 728 → **6** | no visitada |
| Interc. 2, fría | `02_cap1_conexiones.rpy:1553` (+1584) | 1556, 1560, 1562, 1564, 1566, 1568, 1572, 1574, 1580, 1582 → **10** | hub 1 en fría |
| E6, tarde cálida | `02_cap1_evento6.rpy:2674` | 2676, 2678, 2680 → **3** | cálida |
| E6, eco no visitada | `02_cap1_evento6.rpy:3556` | 3558, 3560, 3562, 3564, 3566, 3570, 3572 → **7** | no visitada |
| Final malo, aula | `02_cap1_final_malo.rpy:582` | 585, 587, 589, 591 → **4** | mala |
| Final malo, aula tarde | `02_cap1_final_malo.rpy:1048` | 1051, 1053, 1055, 1059 → **4** | mala |
| Despido B | `02_cap1_final_malo.rpy:1355` | 1358, 1362 → **2** | mala |

**Silueta (regla de §9).** Las **dos manos juntas delante, a la altura del cinturón**, con los brazos relajados. Es una V cerrada en el centro. Se distingue de los brazos cruzados a la altura del pecho (`neutral`), de los codos hacia fuera (`molesta`), de los brazos abiertos con los puños a los lados (`pillada`) y de la mano al cuello (`nerviosa`). **Prueba antes de aprobarla:** ponerla al 30 % junto a las cuatro. Si se confunde con `pillada`, que es el riesgo, separar más los codos del cuerpo.

**Archivo y atributo.**
- PNG: `The Fifth Choice/game/images/sprites/nino_sprites/nino_seria.png`
- Declaración en `00_definiciones.rpy`, debajo de la l. 266 (`image nino molesta …`):
  `image nino seria   = "sprites/nino_sprites/nino_seria.png"`
- Uso: `show nino seria at …` / `call e6_foco("nino", "seria")`.

**Ajustes en PixAI** (§1 y §3 de `GUIA_ARTE.md`):
- Modelo base **Tsubaki.2**. LoRA de personaje `中野二乃 アニメ(サンプル)Tsubaki.2バージョン` a **0.8**. **Sin LoRA de serie**, porque es un sprite individual.
- **Vertical 768 × 1280.** Tsubaki.2 no tiene campo negativo: todo va en positivo. Apuntar la semilla.
- Post: normalizar por IPD a **77,2 px**, con los ojos en **y = 199**, en un lienzo de **760 × 930** RGBA, centrado en el eje de la falda. Quitar el fondo. Corregir el halo (§4).

**Prompt (positivo):**
```
masterpiece, best quality, official anime screencap, go-toubun no hanayome style,
1girl, solo, only one person in the entire image, nakano nino,
standing, front view, facing viewer, centered, figure from head to knees, knees at the bottom edge, plain white background, solid white background,
short hair, bob cut, hair ending above the shoulders, dark muted pink hair, black and green butterfly hair ribbons on both sides of the head, blue eyes,
calm serious expression, composed face, subdued, closed mouth, lips together, relaxed lips, level gaze at viewer, relaxed eyebrows, faint blush,
both hands clasped together in front of the waist, relaxed arms, shoulders level, upright posture,
navy blue blazer with white trim, open blazer, white collared shirt buttoned, green pleated skirt, white knee-high socks,
flat even studio lighting, clean lineart, natural hands with five fingers, deep focus
```
La longitud del pelo lleva tres tokens redundantes (`short hair, bob cut, hair ending above the shoulders`) porque es justo lo que el LoRA tiende a cambiar (§6). La cara seria va en positivo (`calm serious expression, closed mouth, lips together`), como pide §6 para las expresiones no sonrientes.

---

## 7. Cambios 🔁 por archivo (antes → después)

Solo cambia el atributo de expresión. La posición (`at …`), el `with` y el orden se quedan igual.

**`02_cap1_Nino.rpy`**
```renpy
# l. 396
    show nino neutral at pj_habla(0.5)
# →
    show nino pillada at pj_habla(0.5)

# l. 441
    show nino neutral at pj_habla(0.5)
# →
    show nino pillada at pj_habla(0.5)

# l. 454
    show nino neutral at pj_calla(0.5)
# →
    show nino pillada at pj_calla(0.5)
```

**`02_cap1_beat_Nino.rpy`**
```renpy
# l. 313
    show nino neutral at pj(0.5)
# →
    show nino pillada at pj(0.5)

# l. 445
        show nino neutral at pj(0.5)
# →
        show nino molesta at pj(0.5)

# l. 558
        show nino neutral at pj(0.5)
# →
        show nino molesta at pj(0.5)
```

**`02_cap1_conexiones.rpy`**
```renpy
# l. 180
        show nino nerviosa at pj_habla(0.5)
# →
        show nino pillada at pj_habla(0.5)

# l. 702
    show nino molesta at pj_habla(0.5)
# →
    show nino pillada at pj_habla(0.5)

# l. 1241
    show nino neutral at pj_habla(X_NINO)
# →
    show nino molesta at pj_habla(X_NINO)

# l. 1526
            show nino molesta at pj_habla(0.5)
# →
            show nino neutral at pj_habla(0.5)

# l. 1533
            show nino neutral at pj_habla(0.5)
# →
            show nino pillada at pj_habla(0.5)

# l. 2748
        show nino neutral at pj_habla(0.5)
# →
        show nino nerviosa at pj_habla(0.5)

# l. 2784
        show nino neutral at pj_habla(0.5)
# →
        show nino pillada at pj_habla(0.5)
```

**`02_cap1_evento6.rpy`**
```renpy
# l. 2960
    show nino neutral at pj_habla(X_NINO)
# →
    show nino molesta at pj_habla(X_NINO)

# l. 2985
    show nino neutral at pj_habla(X_NINO)
# →
    show nino pillada at pj_habla(X_NINO)

# l. 3004
    show nino molesta at pj_habla(X_NINO)
# →
    show nino neutral at pj_habla(X_NINO)

# l. 3510
    call e6_foco("nino", "neutral")
# →
    call e6_foco("nino", "pillada")

# l. 3545
    call e6_foco("nino", "neutral")
# →
    call e6_foco("nino", "molesta")
```

**`02_cap1_final_malo.rpy`**
```renpy
# l. 110
    show nino neutral at pj_habla(0.5)
# →
    show nino molesta at pj_habla(0.5)
```

**Alternativa si el ➕ no se aprueba** (`02_cap1_conexiones.rpy`, interc. 2 fría):
```renpy
# l. 1553
            show nino neutral at pj_habla(0.5)
# →
            show nino molesta at pj_habla(0.5)

# l. 1584
            show nino neutral at pj_calla(0.5)
# →
            show nino molesta at pj_calla(0.5)
```

---

## 8. Cambios que dependen de `nino seria` (solo cuando exista el PNG y su `image`)

```renpy
# 02_cap1_conexiones.rpy l. 713
    show nino neutral at pj_habla(0.5)
# →
    show nino seria at pj_habla(0.5)

# 02_cap1_conexiones.rpy l. 1553
            show nino neutral at pj_habla(0.5)
# →
            show nino seria at pj_habla(0.5)

# 02_cap1_conexiones.rpy l. 1584
            show nino neutral at pj_calla(0.5)
# →
            show nino seria at pj_calla(0.5)

# 02_cap1_evento6.rpy l. 2674
    call e6_foco("nino", "neutral")
# →
    call e6_foco("nino", "seria")

# 02_cap1_evento6.rpy l. 3556
    call e6_foco("nino", "neutral")
# →
    call e6_foco("nino", "seria")

# 02_cap1_final_malo.rpy l. 582
    show nino neutral at pj_habla(X_NINO)
# →
    show nino seria at pj_habla(X_NINO)

# 02_cap1_final_malo.rpy l. 1048
    show nino neutral at pj_habla(X_NINO)
# →
    show nino seria at pj_habla(X_NINO)

# 02_cap1_final_malo.rpy l. 1355
    show nino neutral at pj_habla(0.5)
# →
    show nino seria at pj_habla(0.5)
```

---

## 9. Fuera de alcance (anotado, no propuesto)

- **E6 l. 2353 → 2381:** el narrador dice «Nino descruzó los brazos» y el sprite no lo hace hasta 28 líneas después (`molesta` en la 2381). Arreglarlo exige **añadir** una línea, y eso lo prohíbe la regla de solo cambiar atributos. Si se quiere, se inserta `call e6_foco("nino", "molesta")` justo antes del narrador de la 2353, aunque eso la pondría en `pj_habla` mientras habla el narrador.
- **Ningún sprite tiene la mano en una puerta o en una mesa:** E6 l. 2988 («sujetaba la puerta con una mano»), l. 3032 («la mano en el picaporte») y final malo l. 121 («las manos apoyadas en la mesa»). No justifica un sprite nuevo: son tres líneas de narración en tres escenas sueltas.
- **El nombre `nino neutral`** no describe una cara en reposo (§3 pide nombrar por expresión). No se renombra: son 83 + 12 usos más 2 formaciones, y el texto confirma que su reposo son los brazos cruzados.
