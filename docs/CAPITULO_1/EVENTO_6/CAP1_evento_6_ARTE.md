## Evento 6 · Fichas de arte — CG, chibis y sprites condicionales

> **Ruta en el repo:** `docs/CAPITULO_1/EVENTO_6/CAP1_evento_6_ARTE.md`
> **Escrito el 05/11/2026** contra `CAP1_evento_6_nucleo.md`, `_bloques_A.md`, `_bloques_B.md`, `CAP1_FINAL_MALO.md`, `GUIA_ARTE.md` y el código de `02_cap1_evento6.rpy` / `10_mj_*.rpy`.
> **Script que acompaña:** `herramientas/normalizar_chibi.py` (sección 7).

**Qué hay que generar.**

| Bloque | Cantidad | Prompts | Negativo |
|---|---|---|---|
| CG de examen `cg_<h>_examen` | 5 | completos | sí (si el modelo lo ofrece) |
| CG de las cinco: `cg_cinco_aula` y `cg_cinco_aprobadas` | 2 | completos | sí (si el modelo lo ofrece) |
| Chibis de minijuego (5 hermanas × 5 expresiones) | 25 (+1 opcional: `itsuki_mano`) | uno completo cada uno | no |
| Sprites condicionales (`miku sonrie`, `yotsuba animada`) | 0–2 | completos | no |

Los dos CG de las cinco son: el **nuevo** (`cg_cinco_aula`, Mov. 1 del núcleo, el que escribiste a mano) y `cg_cinco_aprobadas` (Mov. 8). `cg_miku_audifonos_mesa` queda **descartado** (P-15, equidad entre hermanas): el gesto de dejar los audífonos sobre el pupitre se narra sobre `cg_miku_examen`.

Marcadores de este documento: `[NUEVO]` asset que no existe todavía · «semilla de partida» = la semilla de un CG ya aprobado de la que se arranca · «bloque literal» = texto que se copia sin tocar entre fichas.

---

### 0. Lo que encontré y cómo lo resolví

| # | Hallazgo | Qué hice |
|---|---|---|
| A-01 | El CG nuevo no está en `ANALISIS_EVENTO_6.md` (ahí solo aparece `cg_miku_audifonos_mesa`, ya descartado): es `cg_cinco_aula`, en el Mov. 1 del núcleo | Ficha completa en 4.1. Interpreté «POV de ellas cinco mirándonos» como: la cámara es MC, las cinco de frente, en fila, mirando a cámara, cada una un paso hacia él |
| A-02 | **Tsubaki.2 no muestra campo negativo** (`GUIA_ARTE.md` §1) y los cinco LoRA de personaje son nativos de Tsubaki.2 | Cada CG lleva negativo **y** un positivo que se basta solo. Si el campo no aparece, el negativo no se pega; si cambias a un modelo que lo ofrezca, vacía antes el negativo por defecto (trae `simple background`, `transparent background`, `cropped`) |
| A-03 | Tu mensaje inicial dice «Ichika con blazer azul marino» y «Nino con blazer negro»; la guía de arte (cerrada, y los sprites ya existentes) dicen **Nino = única con blazer azul marino con ribete blanco; Ichika sin blazer, suéter amarillo a la cintura** | Seguí la guía. Si el cambio era intencional, hay que regenerar sprites, no solo estos prompts |
| A-04 | El núcleo usa `yotsuba animada` seis veces en el Mov. 8, y **no existe**: Yotsuba tiene `neutral`, `sonriendo`, `incomoda`, `sorprendida` | Lo más barato: cambiar esas líneas a `yotsuba sonriendo` (coste 0). Dejé ficha opcional en 5.2 por si prefieres un sprite propio |
| A-05 | Los prompts y semillas de los `cg_<h>_fracaso` **no están en el repo** (T-01: dijiste que guardaste las semillas) | Escribí prompts completos desde la receta de `CAP1_FINAL_MALO.md` y los bloques A/B, **y** un procedimiento de enganche (3.2) para que el examen herede cámara y primer plano del fracaso |
| A-06 | La fórmula de la guía cierra con `deep focus, entire scene in sharp detail`. En los CG con POV **contradice** el primer plano desenfocado | En los CG POV lo sustituí por `shallow depth of field` + `strong foreground blur`. En los CG de grupo sí va `deep focus` |
| A-07 | Luz de las escenas de examen: la guía pide luz dorada saturada en todos los CG; el `cg_itsuki_apertura` es «luz fría de primera hora» | Dorada, por coherencia de set. Si los `*_fracaso` quedaron en otra luz, **copia la de ellos**: la serie tiene que verse igual (3.2, paso 2) |
| A-08 | El núcleo pide `sfx_camara` («sfx camara (nuevo)») y `12_e6_pantallas.rpy` ya lo declara y lo reproduce solo si el archivo existe | No es arte, lo dejo anotado: falta el archivo `audio/sfx/camara.mp3` (obturador corto; 効果音ラボ o Freesound CC0) |
| A-09 | Los chibis se cargan por ruta (`mj_chibi_ruta`: `images/chibis/<h>_<expresion>.png`), sin `image …` | La tabla de la sección 8 no lleva declaración para ellos |

---

### 1. Reglas comunes de generación

**Plataforma.** PixAI, modelo base **Tsubaki.2** (SD 1.5). Siempre LoRA de personaje nativo de Tsubaki.2 (los cinco lo tienen). Pasos y CFG no se tocan (solo la semilla). Probar con pocos pasos antes de gastar créditos.

**Pesos de LoRA** (de `GUIA_ARTE.md`, ya calibrados):

| Caso | LoRA de serie (go-toubun) | LoRA de personaje |
|---|---|---|
| CG individual (los 5 de examen) | **0.3** (techo; si reaparece la banda blanca del fleco, 0.2) | **0.75** (rango 0.7–0.8) |
| CG de las cinco | **0.3** | ninguno |
| Chibis | ninguno | **0.7** (si con «chibi» pierde el parecido, bajar a 0.6) |
| Sprites condicionales | ninguno | 0.8 |

**Resolución.** CG: **1280×720 apaisado** (nunca vertical), luego `escalar_cgs.py` a 1920×1080 WebP 95. Chibis: **768×1024 vertical**. Sprites: 768×1280 vertical.

**Palabras gatillo.** Uso las etiquetas estilo danbooru `nakano <nombre>`. Si la ficha del LoRA en PixAI trae una palabra gatillo propia, sustitúyela o añádela junto a esa etiqueta.

**Futaro.** Nunca de frente, nunca el torso. En los CG POV solo aparece como objetos de primer plano y el canto de una mano, desenfocados y cortados por el borde. La mano no cuenta como personaje con LoRA (1 personaje con LoRA por frame).

**Reglas del prompt.** Todo en positivo y describiendo el resultado visible. Nunca «without X» ni «no X» (excepción: etiquetas entrenadas que la guía ya validó: `plain hair with no ribbons`, `not wearing headphones on ears`). Los descriptores difíciles llevan 2–3 tokens redundantes. Sin texto: la hoja se describe por lo que se ve (retícula de casillas vacías, un círculo rojo), nunca pidiendo «texto».

**Bloque negativo común** (solo si el modelo muestra el campo; **no incluye** `blurry`, `cropped`, `simple background`, `transparent background`: pelearían con el primer plano desenfocado y con el encuadre):

```
multiple views, split screen, collage, black bars, letterbox, frame, border, watermark, signature, text, jpeg artifacts, extra fingers, fused fingers, bad hands, deformed hands, extra limbs, extra arms, extra legs, extra people, crowd, male, 1boy, dark skin, jewelry, handcuffs, chains
```

**Tratamiento posterior.** `python escalar_cgs.py entrada/ salida/` (saturación objetivo 68–84; si una sale por debajo, se corrige en el escalado, no regenerando).

---

### 2. Receta de los `cg_<h>_examen` (serie de cinco)

Es el **negativo fotográfico** de los `cg_<h>_fracaso` del Final B: misma cámara, mismo primer plano, otra silueta de hermana (`CAP1_FINAL_MALO.md`, «receta común»).

**Primer plano común (idéntico en las cinco, bloque literal).** POV desde el pupitre de MC: su examen **terminado y boca abajo**, un lápiz encima y el canto de una mano, desenfocado y cortado por el borde inferior.

**Espejo, hermana por hermana** (lo que cambia respecto al fracaso):

| Hermana | `*_fracaso` | `*_examen` |
|---|---|---|
| Yotsuba | Cabeza girada hacia las otras, lápiz quieto sobre hoja casi en blanco, sin sonrisa | Lápiz **en movimiento**, cabeza sobre su hoja, mirada levantada de lado, hombros abiertos, sin sonrisa. Marcas de rotulador en la muñeca |
| Ichika | Tumbada sobre el brazo, guion bajo la hoja, un ojo entreabierto | **Espalda recta**, ojos abiertos escribiendo, guion doblado en cuatro asomando del bolsillo de la falda |
| Nino | Brazos cruzados, hoja boca abajo, lápiz soltado, mandíbula tensa | **Brazos sin cruzar**, hoja terminada **boca arriba**, lápiz en mano, mirada de lado, mandíbula relajada |
| Itsuki | Inclinada sobre tachones, lápiz apoyado, mirada de reojo a cámara | **Escribiendo**, mirada en su hoja, hombros abiertos, **índice izquierdo sobre un renglón** sin tocarlo |
| Miku | Encogida, goma reducida a un tocón, mano cerca de los audífonos | Inclinada **escribiendo**, hombros abiertos, **goma entera**, mano libre plana y lejos de los audífonos |

**Silueta a 30 %.** Cada una tiene que leerse sin cara: Yotsuba cuerpo abierto con la cabeza girada; Ichika la más recta (regla); Nino la única con blazer y sin cruzar brazos; Itsuki el dedo sobre el renglón; Miku el único sudadera azul.

#### 2.1 Bloques literales

**BLOQUE POV** (empieza todos los prompts de examen):

```
single seamless illustration, one continuous frame, widescreen visual novel CG, masterpiece, best quality, official anime screencap, go-toubun no hanayome style, slight high angle shot, first-person view from a school desk, pov, pov hands, large out of focus foreground at the bottom of the frame, a wooden school desk surface in the lower foreground, a single exam paper lying face down showing only its plain white back, a yellow pencil resting on top of the paper, the edge of a hand resting on the desk at the very bottom corner and cropped by the bottom edge of the image, strong foreground blur, shallow depth of field,
```

**BLOQUE AULA** (cierra todos los prompts de examen):

```
indoors, japanese high school classroom, rows of empty wooden desks and chairs, tall windows along the left wall with white curtains, blackboard far in the background, warm golden daylight pouring through the windows, long golden light rays and soft warm shadows across the desks, saturated golden color palette, quiet tense atmosphere, clean lineart, natural hands with five fingers
```

**POSICIÓN** (va en el bloque de cada hermana, mismo texto): `she sits two rows ahead at the right third of the frame, three-quarter profile facing left, upper body and desk visible`

> Si el `*_fracaso` pone a la hermana en otro sitio del cuadro, **copia su posición**: la composición manda sobre este texto.

#### 2.2 Cómo se enganchan con el fracaso (los cinco, misma sesión)

1. Recupera la semilla y el prompt guardados de `cg_<h>_fracaso` (T-01).
2. Arranca con **esa semilla**. Pega el prompt de abajo. Si el fracaso tenía luz distinta, sustituye solo el bloque de luz del BLOQUE AULA por el del fracaso.
3. Genera una tanda corta a pocos pasos. Elige **una** hermana como placa de primer plano (recomiendo **Nino**: pose más simple) y guarda su semilla.
4. Para las otras cuatro, usa la misma semilla de placa. Si el primer plano deriva (la mano cambia de sitio, el lápiz cambia de color), no sigas regenerando: **recorta el 28 % inferior del mejor render y pégalo sobre los demás** en GIMP con difuminado de 40 px, y como mucho una pasada de Gemini (sección 4.3) para igualar el trazo.
5. Anota todas las semillas en la tabla de la sección 9.

---

### 3. Fichas de los cinco CG de examen

Cada ficha: escena · qué cuenta · composición · prompt positivo · negativo · LoRA · criterio de terminado.

#### 3.1 `cg_yotsuba_examen` · Mov. 2 · lunes · Japonés

**Qué cuenta.** Yotsuba escribe, sin sonrisa, y de vez en cuando levanta la vista hacia las demás: lo que mejor sabe hacer, mirar, deja de ser alarma y se convierte en saludo (gesto cálida) o se apaga (fría). Estado-agnóstico: la cara es neutra a propósito.

**Composición.** BLOQUE POV + hermana a la derecha en tres cuartos, hombros abiertos, lápiz en movimiento, mirada hacia un costado.

**LoRA.** Serie 0.3 + Yotsuba 0.75. 1280×720.

**Prompt positivo:**

```
single seamless illustration, one continuous frame, widescreen visual novel CG, masterpiece, best quality, official anime screencap, go-toubun no hanayome style, slight high angle shot, first-person view from a school desk, pov, pov hands, large out of focus foreground at the bottom of the frame, a wooden school desk surface in the lower foreground, a single exam paper lying face down showing only its plain white back, a yellow pencil resting on top of the paper, the edge of a hand resting on the desk at the very bottom corner and cropped by the bottom edge of the image, strong foreground blur, shallow depth of field, 1girl, solo, only one person in the entire image, nakano yotsuba, short orange hair, green headband ribbon, yellow sweater vest, white short sleeve shirt, bare arms, sleeves ending above the elbow, green checkered bow at the collar, she sits two rows ahead at the right third of the frame, three-quarter profile facing left, upper body and desk visible, back straight and shoulders open, head bent over her answer sheet while her eyes look up and sideways toward the other side of the classroom, writing fast with the pencil in her right hand, pencil mid-motion, faint black marker tally lines on the wrist of the writing hand, calm neutral expression, closed mouth, relaxed eyebrows, indoors, japanese high school classroom, rows of empty wooden desks and chairs, tall windows along the left wall with white curtains, blackboard far in the background, warm golden daylight pouring through the windows, long golden light rays and soft warm shadows across the desks, saturated golden color palette, quiet tense atmosphere, clean lineart, natural hands with five fingers
```

**Negativo** (bloque común +):

```
smile, open mouth, grin, closed eyes, ribbon in hair, blazer, 2girls
```

**Criterio de terminado.** (a) Una sola chica; (b) lápiz con sensación de movimiento, no apoyado; (c) **sin sonrisa**; (d) cabeza girada/mirada de lado distingue a Yotsuba del resto; (e) marcas de rotulador en la muñeca sin texto legible; (f) primer plano igual al de las otras cuatro.

#### 3.2 `cg_ichika_examen` · Mov. 3 · martes · Matemáticas

**Qué cuenta.** Ichika despierta y recta resuelve un problema de trenes; el guion de la obra asoma doblado en cuatro por el bolsillo, **traído y sin sacar**. Es la única imagen del set donde Ichika no actúa ni duerme.

**Composición.** Igual que 3.1; silueta de regla.

**LoRA.** Serie 0.3 + Ichika 0.75.

**Prompt positivo:**

```
single seamless illustration, one continuous frame, widescreen visual novel CG, masterpiece, best quality, official anime screencap, go-toubun no hanayome style, slight high angle shot, first-person view from a school desk, pov, pov hands, large out of focus foreground at the bottom of the frame, a wooden school desk surface in the lower foreground, a single exam paper lying face down showing only its plain white back, a yellow pencil resting on top of the paper, the edge of a hand resting on the desk at the very bottom corner and cropped by the bottom edge of the image, strong foreground blur, shallow depth of field, 1girl, solo, only one person in the entire image, nakano ichika, short light pink hair, pastel pink hair, soft baby pink hair, plain hair with no ribbons, white shirt, yellow sweater tied around the waist, she sits two rows ahead at the right third of the frame, three-quarter profile facing left, upper body and desk visible, spine perfectly straight like a ruler, wide open attentive eyes fixed on her answer sheet, writing steadily with a pencil in her right hand, a small paper folded in four peeking out of her skirt pocket at the hip and left untouched, neutral expression, closed mouth, lips relaxed, indoors, japanese high school classroom, rows of empty wooden desks and chairs, tall windows along the left wall with white curtains, blackboard far in the background, warm golden daylight pouring through the windows, long golden light rays and soft warm shadows across the desks, saturated golden color palette, quiet tense atmosphere, clean lineart, natural hands with five fingers
```

**Negativo** (bloque común +):

```
hair ribbons, hair accessories, sleeping, closed eyes, head resting on arm, blazer, smile, 2girls
```

**Respaldo** si el papel del bolsillo no se lee (queda tapado por el pupitre): sustituir esa cláusula por `a small paper folded in four lying on the corner of the desk next to her answer sheet`.

**Criterio de terminado.** Ojos abiertos y espalda recta (si parece que duerme, falla); sin lazos; guion doblado visible; sin sonrisa.

#### 3.3 `cg_nino_examen` · Mov. 4 · miércoles · Inglés

**Qué cuenta.** El instante **antes** de decidir si se levanta y entrega (cálida) o cruza los brazos y se queda de guardia (las otras tres). Es la única imagen del set de exámenes donde Nino no está cerrada. Por eso la hoja ya está terminada, **boca arriba**, y los brazos aún no se cruzan.

**Composición.** Igual; Nino con la hoja a un lado, mirada de reojo a las demás.

**LoRA.** Serie 0.3 + Nino 0.75.

**Prompt positivo:**

```
single seamless illustration, one continuous frame, widescreen visual novel CG, masterpiece, best quality, official anime screencap, go-toubun no hanayome style, slight high angle shot, first-person view from a school desk, pov, pov hands, large out of focus foreground at the bottom of the frame, a wooden school desk surface in the lower foreground, a single exam paper lying face down showing only its plain white back, a yellow pencil resting on top of the paper, the edge of a hand resting on the desk at the very bottom corner and cropped by the bottom edge of the image, strong foreground blur, shallow depth of field, 1girl, solo, only one person in the entire image, nakano nino, short reddish pink hair, darker rose pink hair, large black and green ribbons tied on both sides of her head, twin ribbons, prominent hair ribbons, navy blue blazer with white trim, white buttoned shirt, she sits two rows ahead at the right third of the frame, three-quarter profile facing left, upper body and desk visible, arms resting loosely on her desk with the hands open and uncrossed, her finished answer sheet lying face up beside her with rows of empty answer boxes and one red circle, pencil held loosely in one hand, eyes glancing sideways toward the empty desks, relaxed jaw, calm neutral expression, closed mouth, indoors, japanese high school classroom, rows of empty wooden desks and chairs, tall windows along the left wall with white curtains, blackboard far in the background, warm golden daylight pouring through the windows, long golden light rays and soft warm shadows across the desks, saturated golden color palette, quiet tense atmosphere, clean lineart, natural hands with five fingers
```

**Negativo** (bloque común +):

```
crossed arms, closed eyes, red vest, long hair, smile, clenched jaw, 2girls
```

**Criterio de terminado.** Moños negros y verdes visibles; blazer azul marino; **brazos sin cruzar**; hoja boca arriba; mandíbula sin tensión. Si sale con brazos cruzados, es el fracaso: rehacer.

#### 3.4 `cg_itsuki_examen` · Mov. 5 · jueves · Ciencias

**Qué cuenta.** Itsuki escribe; el índice izquierdo descansa sobre un renglón **señalando sin tocar**: eco literal del «solo te digo dónde mirar». Vale igual si va a levantar la mano, a tardar o a negarse; lo decide el texto.

**Composición.** Igual; encuadre un poco más cercano en la mano izquierda (que se vea el dedo).

**LoRA.** Serie 0.3 + Itsuki 0.75.

**Prompt positivo:**

```
single seamless illustration, one continuous frame, widescreen visual novel CG, masterpiece, best quality, official anime screencap, go-toubun no hanayome style, slight high angle shot, first-person view from a school desk, pov, pov hands, large out of focus foreground at the bottom of the frame, a wooden school desk surface in the lower foreground, a single exam paper lying face down showing only its plain white back, a yellow pencil resting on top of the paper, the edge of a hand resting on the desk at the very bottom corner and cropped by the bottom edge of the image, strong foreground blur, shallow depth of field, 1girl, solo, only one person in the entire image, nakano itsuki, very long bright red hair, deep crimson red hair, vivid red hair reaching past her waist, long flowing hair falling over her shoulder, yellow star hairpins, red sweater vest, white short sleeve shirt, bare arms, sleeves ending above the elbow, she sits two rows ahead at the right third of the frame, three-quarter profile facing left, upper body and desk visible, straight back and open shoulders, eyes fixed on her answer sheet, writing with a pencil in her right hand, the index finger of her left hand resting just above one line of the answer sheet and pointing at it without touching the paper, one neat straight horizontal line crossed out on the sheet, calm focused eyes, neutral expression, closed mouth, indoors, japanese high school classroom, rows of empty wooden desks and chairs, tall windows along the left wall with white curtains, blackboard far in the background, warm golden daylight pouring through the windows, long golden light rays and soft warm shadows across the desks, saturated golden color palette, quiet tense atmosphere, clean lineart, natural hands with five fingers
```

(El ahoge se omite a propósito: `GUIA_ARTE.md` §7 avisa de que pedirlo genera dos. Con el pelo rojo y las estrellas ya se distingue.)

**Negativo** (bloque común +):

```
short hair, two ahoge, blazer, hair ribbons, smile, looking at the viewer, 2girls
```

**Criterio de terminado.** Pelo largo rojo por debajo de la cintura; estrellas amarillas; **dedo izquierdo sobre el renglón sin tocar** (a 30 % es lo que la distingue); mirada en la hoja, no a cámara.

#### 3.5 `cg_miku_examen` · Mov. 6 · viernes · Sociales (el último)

**Qué cuenta.** Responde a `cg_miku_fracaso`: la **goma entera** (allí, un tocón), la mano libre **plana y lejos** de los audífonos (allí, cerca), hombros abiertos (allí, encogida). Es el CG que cierra los cinco.

**Composición.** Igual. La sudadera azul la separa de las otras cuatro.

**LoRA.** Serie 0.3 + Miku 0.75.

**Prompt positivo:**

```
single seamless illustration, one continuous frame, widescreen visual novel CG, masterpiece, best quality, official anime screencap, go-toubun no hanayome style, slight high angle shot, first-person view from a school desk, pov, pov hands, large out of focus foreground at the bottom of the frame, a wooden school desk surface in the lower foreground, a single exam paper lying face down showing only its plain white back, a yellow pencil resting on top of the paper, the edge of a hand resting on the desk at the very bottom corner and cropped by the bottom edge of the image, strong foreground blur, shallow depth of field, 1girl, solo, only one person in the entire image, nakano miku, brown medium length hair, light blue zip-up hoodie, blue headphones around neck, headphones resting on collarbone, not wearing headphones on ears, she sits two rows ahead at the right third of the frame, three-quarter profile facing left, upper body and desk visible, leaning over her answer sheet and writing with a pencil in her right hand, shoulders open and relaxed, her free left hand lying flat on the desk far from the headphones, an intact white rectangular eraser with four sharp corners lying on the desk beside the answer sheet, eyes lowered to the paper, calm neutral expression, closed mouth, indoors, japanese high school classroom, rows of empty wooden desks and chairs, tall windows along the left wall with white curtains, blackboard far in the background, warm golden daylight pouring through the windows, long golden light rays and soft warm shadows across the desks, saturated golden color palette, quiet tense atmosphere, clean lineart, natural hands with five fingers
```

**Negativo** (bloque común +):

```
headphones on ears, wearing headphones, blue hair, school uniform, blazer, hands near headphones, eraser crumbs, smile, 2girls
```

**Criterio de terminado.** Audífonos **al cuello**, nunca puestos; goma entera con las cuatro esquinas; mano libre lejos de los audífonos; pelo castaño; hoja sin migas ni círculo gris.

---

### 4. Los dos CG de las cinco

Reglas de grupo (guía de arte §7): **plano frontal, las cinco en fila a la misma profundidad**; **solo LoRA de serie a 0.3** (los de personaje contaminan a las cinco); cada una **por rasgos, no por nombre**; **orden fijo de izquierda a derecha**: Ichika, Nino, Miku, Yotsuba, Itsuki (el mismo de `X_ICHIKA…X_ITSUKI`).

Separación que la guía ya validó (tokens de pelo para que el modelo no promedie rosa-rojo):

- **Ichika:** `short light pink hair, pastel pink hair, soft baby pink hair, plain hair with no ribbons`
- **Nino:** `short reddish pink hair, darker rose pink hair, large black and green ribbons tied on both sides of her head, twin ribbons, prominent hair ribbons`
- **Itsuki:** `very long bright red hair, deep crimson red hair, vivid red hair reaching past her waist`

**Jerarquía de qué defender** (guía): primero que sean **cinco**, luego los **colores de pelo**, luego las **poses**, y el **vestuario** al final. Para la contaminación de vestuario (el chaleco rojo de Itsuki se le pasa a Nino) cada prenda se encierra en su dueña: `… only on this girl`.

#### 4.1 `cg_cinco_aula` [NUEVO] · Mov. 1 · lunes · aula

**Escena.** Tras `S1`, en `bg_aula`: «Las cinco ya estaban en el aula, con los libros cerrados… Me miraron, y cada una se acercó hacia mí.» Cubre el discurso de MC («Hagan lo que saben… ¡sin excepción!») y la frase del cierre. Los sprites de las confesiones vienen **después**, sobre `bg_aula`.

**Qué cuenta.** El jueguecito invertido del capítulo: en la apertura las cinco miraban a cámara para dar miedo (`cg_cinco_sentadas`); aquí miran a cámara **esperando algo de él**, con los libros cerrados porque ya no hay más que repasar. Tensión contenida, no hostilidad.

**Composición.** Plano frontal, cintura para arriba, cinco en fila, misma profundidad, todas mirando a cámara, cada una inclinada un paso hacia el espectador. **Sin primer plano de MC**: con cinco figuras es lo que más rompe el frame, y la cámara ya *es* él. Partida: encuadre y semilla de `cg_cinco_sentadas` (mismo plano frontal en fila). Silueta a 30 %, de izquierda a derecha:

| Pos. | Hermana | Silueta |
|---|---|---|
| 1 | Ichika | Cabeza ladeada, peso en una cadera, una mano con el cuaderno cerrado al costado |
| 2 | Nino | Brazos cruzados sobre el pecho, cuaderno bajo un brazo, barbilla alta |
| 3 | Miku | Libro grueso abrazado al pecho con los dos brazos, hombros algo encogidos |
| 4 | Yotsuba | La más inclinada hacia cámara, manos a la espalda, sonrisita ansiosa |
| 5 | Itsuki | Espalda recta como regla, cuaderno cerrado en las dos manos a la altura de la cintura |

**LoRA.** Serie 0.3. Ningún LoRA de personaje. 1280×720.

**Prompt positivo:**

```
single seamless illustration, one continuous frame, widescreen visual novel CG, masterpiece, best quality, official anime screencap, go-toubun no hanayome style, 5girls, five sisters, quintuplets, identical faces, five girls standing in a row at the same depth, frontal view, flat horizontal line-up, all five looking straight at the viewer, waist-up shot, each girl leaning slightly toward the viewer as if stepping closer, tense hopeful expressions, each holding a closed notebook, first girl on the far left: short light pink hair, pastel pink hair, soft baby pink hair, plain hair with no ribbons, white shirt only, yellow sweater tied at the waist, head tilted slightly, weight on one hip, one hand holding a closed notebook at her side, closed mouth, second girl from the left: short reddish pink hair, darker rose pink hair, large black and green ribbons tied on both sides of her head, twin ribbons, prominent hair ribbons, navy blue blazer with white trim only on this girl, arms crossed over her chest with a closed notebook tucked under one arm, chin raised, closed mouth, girl in the center: brown medium length hair, light blue zip-up hoodie only on this girl, blue headphones around her neck, headphones resting on collarbone, not wearing headphones on ears, hugging a thick closed book against her chest with both arms, shoulders slightly hunched, fourth girl from the left: short orange hair, green headband ribbon, yellow sweater vest, white short sleeve shirt, bare arms, sleeves ending above the elbow, hands clasped behind her back, leaning forward the most of the five, small eager smile, girl on the far right: very long bright red hair, deep crimson red hair, vivid red hair reaching past her waist, yellow star hairpins, red sweater vest only on this girl, white short sleeve shirt, bare arms, back perfectly straight, holding a closed notebook in both hands in front of her waist, serious focused eyes, closed mouth, indoors, japanese high school classroom in the morning, rows of wooden desks behind them, tall windows with white curtains, blackboard in the distance, warm golden morning sunlight, soft long shadows, saturated golden color palette, deep focus, entire scene in sharp detail, clean lineart, natural hands with five fingers
```

**Negativo** (bloque común, sin `extra people`, + las contaminaciones de grupo):

```
multiple views, split screen, collage, black bars, letterbox, frame, border, watermark, signature, text, jpeg artifacts, extra fingers, fused fingers, bad hands, deformed hands, extra limbs, extra arms, 1girl, solo, 4girls, 6girls, extra girl, merged bodies, fused bodies, male, 1boy, dark skin, jewelry, handcuffs, chains, red vest on the second girl, blazer on the first girl, blazer on the center girl, blue hair, headphones on ears
```

**Criterio de terminado.** (1) Cinco figuras contadas dos veces; (2) orden Ichika-Nino-Miku-Yotsuba-Itsuki; (3) los tres rosa-rojo se distinguen por pelo; (4) Nino es la única con blazer; (5) Miku la única con sudadera, audífonos al cuello; (6) ninguna sostiene un boletín (aún no existe: libros cerrados); (7) mirada a cámara en todas.

#### 4.2 `cg_cinco_aprobadas` · Mov. 8 · la foto

**Escena.** MC saca la foto con el móvil de Yotsuba: «Digan cinco». Ellas, sentadas del mismo lado de la mesa del departamento, cada una con su boletín alzado hacia cámara. «Ninguna bajó el boletín.» Es **la imagen inversa de `cg_cinco_sentadas`**: nadie duerme, nadie mira a otro lado, nadie disimula; todas orgullosas.

**Composición.** Frontal, cinco en fila a la misma profundidad, sentadas tras la mesa larga, cámara a la altura de la mesa. Misma mesa y mismo encuadre que `cg_cinco_estudiando` (`cg_hermanas_estudiando` sirve de respaldo). **Semilla de partida: la de `cg_cinco_estudiando`.** El boletín se describe por su estructura (retícula de casillas y un círculo rojo): sin texto legible ni números (los números se enseñan después, en `boletin_cinco`). Silueta a 30 %:

| Pos. | Hermana | Silueta (del núcleo) |
|---|---|---|
| 1 | Ichika | Despierta, boletín **contra el pecho** con las dos manos, sonrisa relajada |
| 2 | Nino | **Un brazo cruzado** sobre el torso, la otra mano sostiene el boletín a la altura del hombro, medio sonrojo, sonrisa torcida, mirada de lado |
| 3 | Miku | **Manos delante del cuerpo** sosteniendo el boletín bajo, audífonos al cuello sin tocarlos, sonrisa pequeña |
| 4 | Yotsuba | Boletín **en alto sobre la cabeza** con los dos brazos, hombros abiertos, sonrisa enorme |
| 5 | Itsuki | **Derecha**, boletín recto y vertical con las dos manos a la altura del pecho, sonrisa leve |

**Estados de entrada.** Un solo CG para los tres: el tinte lo pone el código (`e6_tinte_superado` / `e6_tinte_bueno`), sin arte nuevo. Por eso la luz base tiene que ser **neutra-cálida**, ni fría ni sobresaturada, o el tinte se pisa.

**LoRA.** Serie 0.3. Ningún LoRA de personaje. 1280×720.

**Prompt positivo:**

```
single seamless illustration, one continuous frame, widescreen visual novel CG, masterpiece, best quality, official anime screencap, go-toubun no hanayome style, 5girls, five sisters, quintuplets, identical faces, five girls sitting in a row side by side behind a long dining table, frontal view, same depth, flat horizontal line-up, camera at table height facing them, all five looking at the viewer, upper body shot, each girl holding up a report card toward the viewer with its printed side facing the camera, each report card showing a grid of empty boxes and rows with a single red circle at the top, proud relieved happy expressions, first girl on the far left: short light pink hair, pastel pink hair, soft baby pink hair, plain hair with no ribbons, white shirt only, yellow sweater tied at the waist, wide awake, report card pressed against her chest with both hands, relaxed smile, second girl from the left: short reddish pink hair, darker rose pink hair, large black and green ribbons tied on both sides of her head, twin ribbons, prominent hair ribbons, navy blue blazer with white trim only on this girl, one arm crossed over her torso and the other hand holding the report card at shoulder height, light blush, crooked half smile, eyes glancing sideways, girl in the center: brown medium length hair, light blue zip-up hoodie only on this girl, blue headphones around her neck, headphones resting on collarbone, not wearing headphones on ears, both hands in front of her body holding the report card low at chest level, small gentle smile, fourth girl from the left: short orange hair, green headband ribbon, yellow sweater vest, white short sleeve shirt, bare arms, sleeves ending above the elbow, report card raised high above her head with both arms, open shoulders, huge open mouth smile, girl on the far right: very long bright red hair, deep crimson red hair, vivid red hair reaching past her waist, yellow star hairpins, red sweater vest only on this girl, white short sleeve shirt, bare arms, back perfectly straight, report card held flat and perfectly upright in both hands at chest height, faint confident smile, indoors, double height loft apartment, exposed red brick wall behind them, black metal staircase with glass railing on the left, long built-in aquarium glowing teal under the staircase, dark wooden cabinets, warm late afternoon sunlight streaming through a tall window, long light rays across the floor, soft warm shadows, teal glow from the aquarium, soft shading, saturated golden color palette, deep focus, entire scene in sharp detail, clean lineart, natural hands with five fingers
```

**Negativo** (mismo que 4.1, cambiando la última línea):

```
multiple views, split screen, collage, black bars, letterbox, frame, border, watermark, signature, text, jpeg artifacts, extra fingers, fused fingers, bad hands, deformed hands, extra limbs, extra arms, 1girl, solo, 4girls, 6girls, extra girl, merged bodies, fused bodies, male, 1boy, dark skin, jewelry, handcuffs, chains, red vest on the second girl, blazer on the first girl, blazer on the center girl, blue hair, headphones on ears, readable text on the report cards, sleeping, looking away
```

**Criterio de terminado.** (1) Cinco figuras y cinco boletines **visibles y sin texto legible**; (2) las cinco siluetas se leen a 30 % (Yotsuba brazos arriba, Nino un brazo cruzado, Miku manos bajas, Itsuki recta, Ichika pecho); (3) nadie duerme ni mira a otro lado; (4) misma mesa y encuadre que `cg_cinco_estudiando`; (5) saturación 68–84 tras `escalar_cgs.py`.

#### 4.3 Plan de edición con Gemini (máx. 3 pasadas)

Aplica a `cinco_aprobadas` y, si hace falta, a `cinco_aula`. Cada pasada reinterpreta la imagen entera y puede **deshacer** las anteriores (pasó dos veces con el chaleco de Nino): por eso se ordena por lo que más duele perder. Gemini comprime en JPEG: no subir el WebP sobre 95.

**Entradas.** El CG + el sprite de la hermana afectada (identificarla por **posición y rasgos**, no por nombre).

| Pasada | Qué defiende | Cuándo hacerla |
|---|---|---|
| 1 | **Cinco figuras exactas**, orden correcto y **colores de pelo** (Ichika rosa pálido sin lazos, Nino rosa oscuro con lazos, Itsuki rojo largo) | Siempre que haya figura de más/menos o pelos promediados |
| 2 | **Poses del núcleo** (boletín alto / pecho / bajo / recto / brazo cruzado) y el **boletín sin texto** | Si las poses salieron genéricas |
| 3 | **Vestuario** (blazer solo en Nino, sudadera solo en Miku, chaleco rojo solo en Itsuki) | Solo si queda contaminación; es la que menos se nota |

**Plantilla** (en inglés; se numera cada cambio y se enumera lo que no se toca):

```
Image 1 is a visual novel CG. Image 2 is the reference sprite of the girl described in CHANGE 1. Edit image 1 only as follows.

CHANGE 1: The girl on the far left (short pale pink hair, no ribbons, white shirt, yellow sweater tied at the waist) must hold her report card pressed against her chest with both hands. Match the pose of the girls' arms to this description only for her.
CHANGE 2: The second girl from the left (darker rose pink hair, large black and green ribbons on both sides of the head, navy blazer) must have one arm crossed over her torso and hold the report card at shoulder height with the other hand.
CHANGE 3: (add or delete as needed; one change per paragraph)

KEEP EXACTLY THE SAME: the table, the brick wall, the staircase, the aquarium glow, the lighting, the other three girls, their faces, their hair colors, their clothes and the number of girls (exactly five).

Match the line thickness, flat cel shading and color gradation of the original so the edit looks painted in the same pass. Return the full image at the same framing and resolution.
```

---

### 5. Sprites condicionales (solo si el guion los pide y P-23 lo permite)

Estándar del set (no cambiar): lienzo 760×930, ojos en y = 199, IPD 77,2, eje en el centro de la falda. Generar vertical 768×1280, fondo blanco liso, **solo LoRA de personaje a 0.8**. Flujo: `quitar_fondo_ia.py` → `normalizar_sprite.py --ojos x1,y1,x2,y2` → `limpiar_halo.py --solo-halo`. Borrar `game/cache` al reemplazar.

#### 5.1 `miku sonrie` (condicional · eco cálida, página 120)

**Cuándo.** Solo el payoff de la página 120 en el eco cálida de Miku («Quería ver tu cara. Ya la vi»). **Antes de generar, pruébalo con `miku relajada`**: si a 30 % ya lee como sonrisa mínima, **no hace falta** (el eco trae el sustituto escrito).

**Silueta (lo que se lee a 30 %).** Audífonos al cuello sin tocar, **boletín contra el pecho con las dos manos**, hombros abiertos, barbilla recta. Sin libro delante del cuerpo: en todos los sprites de Miku hay algo delante; aquí lo que hay es el boletín, y se sostiene alto, no tapa la cara. Sonrisa mínima de comisura, **sin rubor** (la haría tímida).

**Prompt:**

```
masterpiece, best quality, 1girl, solo, nakano miku, brown medium length hair, light blue zip-up hoodie, blue headphones around neck, headphones resting on collarbone, not wearing headphones on ears, dark tights, standing, cowboy shot reaching below the knees, shoulders open, chin level, holding a report card pressed against her chest with both hands, a very small smile at the corner of her mouth, calm eyes looking at the viewer, clear fair cheeks, plain pale skin tone, plain white background, flat white background, flat even lighting, clean lineart, simple cel shading
```

**Criterio.** Distinta de `neutral` y de `relajada` por la **silueta** (boletín al pecho), no por la cara; sin rubor; audífonos al cuello.

#### 5.2 `yotsuba animada` (opcional · decisión del núcleo, ver A-04)

**Recomendación:** no generarlo. Cambiar en el núcleo `yotsuba animada` por `yotsuba sonriendo` (existe). Si prefieres un sprite con nombre propio para el Mov. 8:

**Silueta.** Brazos en alto y hombros muy abiertos (lo opuesto a `incomoda`), ocupa más ancho que `sonriendo`. Sonrisa abierta.

```
masterpiece, best quality, 1girl, solo, nakano yotsuba, short orange hair, green headband ribbon, yellow sweater vest, white short sleeve shirt, bare arms, sleeves ending above the elbow, green checkered bow at the collar, dark knee-high socks, standing, cowboy shot reaching below the knees, both arms raised high above the head with open hands, shoulders wide open, huge open mouth smile, eyes bright and open, plain white background, flat white background, flat even lighting, clean lineart, simple cel shading
```

Se declararía `image yotsuba animada = "sprites/yotsuba_sprites/yotsuba_animada.png"` (atributo con espacio, **no** `yotsuba_animada`). Pasar `limpiar_halo.py --solo-halo` (excepción Yotsuba).

---

### 6. Chibis de los minijuegos (25 + 1 opcional)

Los usa `10_mj_chibi.rpy` (`mj_chibi(hermana, expresion)`): un chibi protagonista por minijuego con una escalera `neutral → animo → esfuerzo → feliz`, y `triste` al fallar. Y2 usa además a las cinco hermanas como corredoras.

**Archivo.** `game/images/chibis/<hermana>_<expresion>.png`, 512×512 RGBA, **pies en la fila ~496, eje en el centro**. Se obtienen con `normalizar_chibi.py` (sección 7).

**Cómo generar.** 768×1024 vertical, fondo blanco liso, **solo LoRA de personaje 0.7** (0.6 si pierde el parecido con «chibi»), sin LoRA de serie, **sin negativo**: un prompt por imagen, todo en positivo. **Una semilla por hermana**, repetida en sus cinco expresiones (el parecido entre expresiones depende de ello). Anota la semilla en la sección 9.

**La silueta decide** (a 30 % la cara no se lee): `neutral` erguida y quieta; `animo` puños al pecho y un paso adelante; `esfuerzo` cuerpo inclinado, rodillas dobladas; `triste` encogida abrazándose; `feliz` brazos arriba y saltando.

**Notas por hermana.** El ahoge de Itsuki se omite (la guía avisa: genera dos). Yotsuba: `normalizar_chibi.py --sin-huecos` (cuello blanco junto al chaleco amarillo). Miku: la sudadera cubre la cadera; sin falda a propósito.

#### 6.1 Ichika (LoRA Ichika 0.7 · semilla propia)

```
masterpiece, best quality, chibi, super deformed, 2 heads tall, full body, head to shoes visible, centered, 1girl, solo, only one character, nakano ichika, short light pink hair, pastel pink hair, plain hair with no ribbons, white shirt, yellow sweater tied around the waist, green pleated skirt, brown loafers, standing upright, arms relaxed at the sides, feet together, small calm smile, looking at the viewer, plain white background, flat white background, flat even lighting, clean lineart, simple cel shading
```
`ichika_neutral`

```
masterpiece, best quality, chibi, super deformed, 2 heads tall, full body, head to shoes visible, centered, 1girl, solo, only one character, nakano ichika, short light pink hair, pastel pink hair, plain hair with no ribbons, white shirt, yellow sweater tied around the waist, green pleated skirt, brown loafers, slight lean forward, both fists clenched in front of the chest, determined sparkling eyes, confident smile, one foot half a step forward, plain white background, flat white background, flat even lighting, clean lineart, simple cel shading
```
`ichika_animo`

```
masterpiece, best quality, chibi, super deformed, 2 heads tall, full body, head to shoes visible, centered, 1girl, solo, only one character, nakano ichika, short light pink hair, pastel pink hair, plain hair with no ribbons, white shirt, yellow sweater tied around the waist, green pleated skirt, brown loafers, body leaning strongly forward, knees bent, fists tight, gritted teeth, furrowed eyebrows, a sweat drop on the temple, intense focused expression, dynamic running stance, plain white background, flat white background, flat even lighting, clean lineart, simple cel shading
```
`ichika_esfuerzo`

```
masterpiece, best quality, chibi, super deformed, 2 heads tall, full body, head to shoes visible, centered, 1girl, solo, only one character, nakano ichika, short light pink hair, pastel pink hair, plain hair with no ribbons, white shirt, yellow sweater tied around the waist, green pleated skirt, brown loafers, shrunken curled posture, shoulders hunched inward, arms hugging herself, head bowed, knees together, downcast teary eyes, drooping eyebrows, small frown, a sweat drop, plain white background, flat white background, flat even lighting, clean lineart, simple cel shading
```
`ichika_triste`

```
masterpiece, best quality, chibi, super deformed, 2 heads tall, full body, head to shoes visible, centered, 1girl, solo, only one character, nakano ichika, short light pink hair, pastel pink hair, plain hair with no ribbons, white shirt, yellow sweater tied around the waist, green pleated skirt, brown loafers, both arms raised high above the head, jumping with both feet off the ground, big open smile, eyes closed in happiness, plain white background, flat white background, flat even lighting, clean lineart, simple cel shading
```
`ichika_feliz`

#### 6.2 Nino (LoRA Nino 0.7)

```
masterpiece, best quality, chibi, super deformed, 2 heads tall, full body, head to shoes visible, centered, 1girl, solo, only one character, nakano nino, short reddish pink hair, large black and green ribbons tied on both sides of the head, twin ribbons, navy blue blazer with white trim, white shirt, green pleated skirt, white knee-high socks, brown loafers, standing upright, arms relaxed at the sides, feet together, small calm smile, looking at the viewer, plain white background, flat white background, flat even lighting, clean lineart, simple cel shading
```
`nino_neutral`

```
masterpiece, best quality, chibi, super deformed, 2 heads tall, full body, head to shoes visible, centered, 1girl, solo, only one character, nakano nino, short reddish pink hair, large black and green ribbons tied on both sides of the head, twin ribbons, navy blue blazer with white trim, white shirt, green pleated skirt, white knee-high socks, brown loafers, slight lean forward, both fists clenched in front of the chest, determined sparkling eyes, confident smile, one foot half a step forward, plain white background, flat white background, flat even lighting, clean lineart, simple cel shading
```
`nino_animo`

```
masterpiece, best quality, chibi, super deformed, 2 heads tall, full body, head to shoes visible, centered, 1girl, solo, only one character, nakano nino, short reddish pink hair, large black and green ribbons tied on both sides of the head, twin ribbons, navy blue blazer with white trim, white shirt, green pleated skirt, white knee-high socks, brown loafers, body leaning strongly forward, knees bent, fists tight, gritted teeth, furrowed eyebrows, a sweat drop on the temple, intense focused expression, dynamic running stance, plain white background, flat white background, flat even lighting, clean lineart, simple cel shading
```
`nino_esfuerzo`

```
masterpiece, best quality, chibi, super deformed, 2 heads tall, full body, head to shoes visible, centered, 1girl, solo, only one character, nakano nino, short reddish pink hair, large black and green ribbons tied on both sides of the head, twin ribbons, navy blue blazer with white trim, white shirt, green pleated skirt, white knee-high socks, brown loafers, shrunken curled posture, shoulders hunched inward, arms hugging herself, head bowed, knees together, downcast teary eyes, drooping eyebrows, small frown, a sweat drop, plain white background, flat white background, flat even lighting, clean lineart, simple cel shading
```
`nino_triste`

```
masterpiece, best quality, chibi, super deformed, 2 heads tall, full body, head to shoes visible, centered, 1girl, solo, only one character, nakano nino, short reddish pink hair, large black and green ribbons tied on both sides of the head, twin ribbons, navy blue blazer with white trim, white shirt, green pleated skirt, white knee-high socks, brown loafers, both arms raised high above the head, jumping with both feet off the ground, big open smile, eyes closed in happiness, plain white background, flat white background, flat even lighting, clean lineart, simple cel shading
```
`nino_feliz`

#### 6.3 Miku (LoRA Miku 0.7)

```
masterpiece, best quality, chibi, super deformed, 2 heads tall, full body, head to shoes visible, centered, 1girl, solo, only one character, nakano miku, brown medium length hair, light blue zip-up hoodie long enough to cover the hips, blue headphones around the neck, headphones resting on collarbone, not wearing headphones on ears, dark tights, brown loafers, standing upright, arms relaxed at the sides, feet together, small calm smile, looking at the viewer, plain white background, flat white background, flat even lighting, clean lineart, simple cel shading
```
`miku_neutral`

```
masterpiece, best quality, chibi, super deformed, 2 heads tall, full body, head to shoes visible, centered, 1girl, solo, only one character, nakano miku, brown medium length hair, light blue zip-up hoodie long enough to cover the hips, blue headphones around the neck, headphones resting on collarbone, not wearing headphones on ears, dark tights, brown loafers, slight lean forward, both fists clenched in front of the chest, determined sparkling eyes, confident smile, one foot half a step forward, plain white background, flat white background, flat even lighting, clean lineart, simple cel shading
```
`miku_animo`

```
masterpiece, best quality, chibi, super deformed, 2 heads tall, full body, head to shoes visible, centered, 1girl, solo, only one character, nakano miku, brown medium length hair, light blue zip-up hoodie long enough to cover the hips, blue headphones around the neck, headphones resting on collarbone, not wearing headphones on ears, dark tights, brown loafers, body leaning strongly forward, knees bent, fists tight, gritted teeth, furrowed eyebrows, a sweat drop on the temple, intense focused expression, dynamic running stance, plain white background, flat white background, flat even lighting, clean lineart, simple cel shading
```
`miku_esfuerzo`

```
masterpiece, best quality, chibi, super deformed, 2 heads tall, full body, head to shoes visible, centered, 1girl, solo, only one character, nakano miku, brown medium length hair, light blue zip-up hoodie long enough to cover the hips, blue headphones around the neck, headphones resting on collarbone, not wearing headphones on ears, dark tights, brown loafers, shrunken curled posture, shoulders hunched inward, arms hugging herself, head bowed, knees together, downcast teary eyes, drooping eyebrows, small frown, a sweat drop, plain white background, flat white background, flat even lighting, clean lineart, simple cel shading
```
`miku_triste`

```
masterpiece, best quality, chibi, super deformed, 2 heads tall, full body, head to shoes visible, centered, 1girl, solo, only one character, nakano miku, brown medium length hair, light blue zip-up hoodie long enough to cover the hips, blue headphones around the neck, headphones resting on collarbone, not wearing headphones on ears, dark tights, brown loafers, both arms raised high above the head, jumping with both feet off the ground, big open smile, eyes closed in happiness, plain white background, flat white background, flat even lighting, clean lineart, simple cel shading
```
`miku_feliz`

#### 6.4 Yotsuba (LoRA Yotsuba 0.7)

```
masterpiece, best quality, chibi, super deformed, 2 heads tall, full body, head to shoes visible, centered, 1girl, solo, only one character, nakano yotsuba, short orange hair, green headband ribbon, yellow sweater vest, white short sleeve shirt, bare arms, green checkered bow at the collar, green pleated skirt, dark knee-high socks, brown loafers, standing upright, arms relaxed at the sides, feet together, small calm smile, looking at the viewer, plain white background, flat white background, flat even lighting, clean lineart, simple cel shading
```
`yotsuba_neutral`

```
masterpiece, best quality, chibi, super deformed, 2 heads tall, full body, head to shoes visible, centered, 1girl, solo, only one character, nakano yotsuba, short orange hair, green headband ribbon, yellow sweater vest, white short sleeve shirt, bare arms, green checkered bow at the collar, green pleated skirt, dark knee-high socks, brown loafers, slight lean forward, both fists clenched in front of the chest, determined sparkling eyes, confident smile, one foot half a step forward, plain white background, flat white background, flat even lighting, clean lineart, simple cel shading
```
`yotsuba_animo`

```
masterpiece, best quality, chibi, super deformed, 2 heads tall, full body, head to shoes visible, centered, 1girl, solo, only one character, nakano yotsuba, short orange hair, green headband ribbon, yellow sweater vest, white short sleeve shirt, bare arms, green checkered bow at the collar, green pleated skirt, dark knee-high socks, brown loafers, body leaning strongly forward, knees bent, fists tight, gritted teeth, furrowed eyebrows, a sweat drop on the temple, intense focused expression, dynamic running stance, plain white background, flat white background, flat even lighting, clean lineart, simple cel shading
```
`yotsuba_esfuerzo`

```
masterpiece, best quality, chibi, super deformed, 2 heads tall, full body, head to shoes visible, centered, 1girl, solo, only one character, nakano yotsuba, short orange hair, green headband ribbon, yellow sweater vest, white short sleeve shirt, bare arms, green checkered bow at the collar, green pleated skirt, dark knee-high socks, brown loafers, shrunken curled posture, shoulders hunched inward, arms hugging herself, head bowed, knees together, downcast teary eyes, drooping eyebrows, small frown, a sweat drop, plain white background, flat white background, flat even lighting, clean lineart, simple cel shading
```
`yotsuba_triste`

```
masterpiece, best quality, chibi, super deformed, 2 heads tall, full body, head to shoes visible, centered, 1girl, solo, only one character, nakano yotsuba, short orange hair, green headband ribbon, yellow sweater vest, white short sleeve shirt, bare arms, green checkered bow at the collar, green pleated skirt, dark knee-high socks, brown loafers, both arms raised high above the head, jumping with both feet off the ground, big open smile, eyes closed in happiness, plain white background, flat white background, flat even lighting, clean lineart, simple cel shading
```
`yotsuba_feliz`

#### 6.5 Itsuki (LoRA Itsuki 0.7)

```
masterpiece, best quality, chibi, super deformed, 2 heads tall, full body, head to shoes visible, centered, 1girl, solo, only one character, nakano itsuki, very long bright red hair reaching past the waist, yellow star hairpins, red sweater vest, white short sleeve shirt, bare arms, green pleated skirt, brown loafers, standing upright, arms relaxed at the sides, feet together, small calm smile, looking at the viewer, plain white background, flat white background, flat even lighting, clean lineart, simple cel shading
```
`itsuki_neutral`

```
masterpiece, best quality, chibi, super deformed, 2 heads tall, full body, head to shoes visible, centered, 1girl, solo, only one character, nakano itsuki, very long bright red hair reaching past the waist, yellow star hairpins, red sweater vest, white short sleeve shirt, bare arms, green pleated skirt, brown loafers, slight lean forward, both fists clenched in front of the chest, determined sparkling eyes, confident smile, one foot half a step forward, plain white background, flat white background, flat even lighting, clean lineart, simple cel shading
```
`itsuki_animo`

```
masterpiece, best quality, chibi, super deformed, 2 heads tall, full body, head to shoes visible, centered, 1girl, solo, only one character, nakano itsuki, very long bright red hair reaching past the waist, yellow star hairpins, red sweater vest, white short sleeve shirt, bare arms, green pleated skirt, brown loafers, body leaning strongly forward, knees bent, fists tight, gritted teeth, furrowed eyebrows, a sweat drop on the temple, intense focused expression, dynamic running stance, plain white background, flat white background, flat even lighting, clean lineart, simple cel shading
```
`itsuki_esfuerzo`

```
masterpiece, best quality, chibi, super deformed, 2 heads tall, full body, head to shoes visible, centered, 1girl, solo, only one character, nakano itsuki, very long bright red hair reaching past the waist, yellow star hairpins, red sweater vest, white short sleeve shirt, bare arms, green pleated skirt, brown loafers, shrunken curled posture, shoulders hunched inward, arms hugging herself, head bowed, knees together, downcast teary eyes, drooping eyebrows, small frown, a sweat drop, plain white background, flat white background, flat even lighting, clean lineart, simple cel shading
```
`itsuki_triste`

```
masterpiece, best quality, chibi, super deformed, 2 heads tall, full body, head to shoes visible, centered, 1girl, solo, only one character, nakano itsuki, very long bright red hair reaching past the waist, yellow star hairpins, red sweater vest, white short sleeve shirt, bare arms, green pleated skirt, brown loafers, both arms raised high above the head, jumping with both feet off the ground, big open smile, eyes closed in happiness, plain white background, flat white background, flat even lighting, clean lineart, simple cel shading
```
`itsuki_feliz`

**Opcional, `itsuki_mano`** (el minijuego It1 la usa mientras levanta la mano; si falta, el código cae a `neutral`):

```
masterpiece, best quality, chibi, super deformed, 2 heads tall, full body, head to shoes visible, centered, 1girl, solo, only one character, nakano itsuki, very long bright red hair reaching past the waist, yellow star hairpins, red sweater vest, white short sleeve shirt, bare arms, green pleated skirt, brown loafers, standing straight, one arm raised straight up with the open palm toward the viewer, serious calm expression, polite posture, plain white background, flat white background, flat even lighting, clean lineart, simple cel shading
```
`itsuki_mano`

---

### 7. `normalizar_chibi.py`

Va en `herramientas/` junto a `normalizar_extra.py` (de ahí reutiliza el recorte de fondo y el escalado con alfa premultiplicado). Requiere Pillow, numpy y scipy.

**Qué hace.** Quita el fondo blanco (o respeta el alfa si ya viene recortado), borra motas, mide cada expresión y aplica **una escala común por hermana**: el `neutral` queda en 420 px de alto, salvo que `feliz` (brazos arriba) o la expresión más ancha no quepan, en cuyo caso la escala baja y el informe lo dice. Coloca los pies en la fila 496 y el eje (centro de masa del 30 % inferior, no lo desplazan brazos ni pelo) en la columna 256. Guarda `<hermana>_<expresion>.png` en 512×512.

**Uso (desde `herramientas/`):**

```
python normalizar_chibi.py renders_crudos/chibis/ ../game/images/chibis/ --simular
python normalizar_chibi.py renders_crudos/chibis/ ../game/images/chibis/ --hermana nino
python normalizar_chibi.py renders_crudos/chibis/ ../game/images/chibis/ --hermana yotsuba --sin-huecos
python normalizar_chibi.py renders_crudos/chibis/ ../game/images/chibis/ --alto-neutral 400 --sobrescribir
```

- Procesa **las cinco expresiones de una hermana a la vez**: con un solo archivo hay que dar `--escala`.
- `--simular` informa sin escribir. `--eje masa|bbox` si el eje por pies descentra una pose (por ejemplo `triste` muy encogida).
- Tras reemplazar un chibi, borrar `game/cache`.
- Los renders crudos van en `renders_crudos/` (ya está en `.gitignore`).

---

### 8. Tabla definitiva de assets

Carpeta de los CG: `game/images/cg/cap1_evento6/` (la que ya busca `12_e6_pantallas.rpy` con `e6_cg_declarar`, que pone un cartel «CG PENDIENTE» mientras falte el archivo). Convención de nombres: minúsculas, sin tildes, sin espacios.

| Asset | Tipo | Archivo | Declaración `image` | Entrada de `GALERIA` |
|---|---|---|---|---|
| `cg_yotsuba_examen` | CG | `images/cg/cap1_evento6/yotsuba_examen.webp` | `e6_cg_declarar("cg_yotsuba_examen", "yotsuba_examen.webp")` | pestaña `yotsuba`: `("cg_yotsuba_examen", "Examen · Japonés")` |
| `cg_ichika_examen` | CG | `…/ichika_examen.webp` | `e6_cg_declarar("cg_ichika_examen", "ichika_examen.webp")` | `ichika`: `("cg_ichika_examen", "Examen · Matemáticas")` |
| `cg_nino_examen` | CG | `…/nino_examen.webp` | `e6_cg_declarar("cg_nino_examen", "nino_examen.webp")` | `nino`: `("cg_nino_examen", "Examen · Inglés")` |
| `cg_itsuki_examen` | CG | `…/itsuki_examen.webp` | `e6_cg_declarar("cg_itsuki_examen", "itsuki_examen.webp")` | `itsuki`: `("cg_itsuki_examen", "Examen · Ciencias")` |
| `cg_miku_examen` | CG | `…/miku_examen.webp` | `e6_cg_declarar("cg_miku_examen", "miku_examen.webp")` | `miku`: `("cg_miku_examen", "Examen · Sociales")` |
| `cg_cinco_aula` | CG [NUEVO] | `…/cinco_aula.webp` | `e6_cg_declarar("cg_cinco_aula", "cinco_aula.webp")` | `cap1`: `("cg_cinco_aula", "Hagan lo que saben")` |
| `cg_cinco_aprobadas` | CG | `…/cinco_aprobadas.webp` | `e6_cg_declarar("cg_cinco_aprobadas", "cinco_aprobadas.webp")` | `cap1`: `("cg_cinco_aprobadas", "Digan cinco")` |
| 5 × `<h>_<expresion>` | Chibi | `game/images/chibis/<h>_<expresion>.png` | *(ninguna: `mj_chibi_ruta`)* | — |
| `itsuki_mano` | Chibi (opc.) | `game/images/chibis/itsuki_mano.png` | *(ninguna)* | — |
| `miku sonrie` | Sprite (cond.) | `game/images/sprites/miku_sprites/miku_sonrie.png` | `image miku sonrie = "sprites/miku_sprites/miku_sonrie.png"` | — |
| `yotsuba animada` | Sprite (opc.) | `game/images/sprites/yotsuba_sprites/yotsuba_animada.png` | `image yotsuba animada = "sprites/yotsuba_sprites/yotsuba_animada.png"` | — |

**Dos detalles de código** (no son arte, pero dependen de estos assets):

- `12_e6_pantallas.rpy` ya añade las entradas de Galería por código (`e6_galeria_agregar`), pero **no incluye `cg_cinco_aula`**: ya aparece en la lista `"cap1"` de esa función, así que no hay que tocar nada. Si prefieres hacerlo en `08_extras.rpy`, descomenta las líneas «Examen · …» y añade las dos de `cap1` (así no se duplican: `e6_galeria_agregar` comprueba `if item not in s[3]`).
- **P-17** (los `*_fracaso` dejan de ser obligatorios en la sección de cada hermana) pide rediseñar el menú de Galería y queda fuera de este documento.

El tinte de `cg_cinco_aprobadas` por estado ya está en `12_e6_pantallas.rpy` (`e6_tinte_superado`, `e6_tinte_mixto`, `e6_tinte_bueno`). Importante: el guion hace `scene cg_cinco_aprobadas at e6_tinte_…` sobre **el mismo nombre de imagen**, así `renpy.seen_image` lo marca como visto y la Galería lo desbloquea. Si algún día se declara una imagen distinta por estado, la Galería nunca lo vería.

---

### 9. Orden de generación y semillas a guardar

**Orden recomendado** (lo caro primero, lo condicional al final; 10.000 créditos diarios):

1. **T-01.** Recuperar semillas y prompts de los cinco `cg_*_fracaso` y de `cg_cinco_estudiando`.
2. **Pruebas a pocos pasos** del BLOQUE POV con una sola hermana (Nino) hasta fijar el primer plano. Guardar semilla de placa.
3. **Los cinco `cg_*_examen` en la misma sesión**: Nino → Miku → Yotsuba → Ichika → Itsuki (de la silueta más simple a la más frágil). Si deriva el primer plano, composición en GIMP (2.2, paso 4).
4. **`cg_cinco_aprobadas`** con la semilla de `cg_cinco_estudiando` + hasta 3 pasadas de Gemini.
5. **`cg_cinco_aula`** [NUEVO] con encuadre/semilla de `cg_cinco_sentadas` + hasta 3 pasadas.
6. `escalar_cgs.py` a los siete CG → `game/images/cg/cap1_evento6/` → borrar `game/cache`.
7. **Chibis**: una sesión por hermana (misma semilla, cinco expresiones). Luego `normalizar_chibi.py` hermana a hermana. Orden: **Yotsuba** (Y2 la usa en las cinco carreras), Nino, Itsuki, Ichika, Miku. `itsuki_mano` al final.
8. **Condicionales** (`miku sonrie`, `yotsuba animada`): solo si la prueba con `miku relajada` / el cambio a `yotsuba sonriendo` no basta.
9. **Galería**: activar las entradas (sección 8). Revisar los siete CG a 30 % de tamaño.

**Semillas a guardar** (rellenar al generar; es lo único del trabajo de arte que no se recupera):

| Asset | Semilla de partida | Semilla final aprobada |
|---|---|---|
| Placa de primer plano (los 5 examen) | — | |
| `cg_yotsuba_examen` | semilla de `cg_yotsuba_fracaso` | |
| `cg_ichika_examen` | semilla de `cg_ichika_fracaso` | |
| `cg_nino_examen` | semilla de `cg_nino_fracaso` | |
| `cg_itsuki_examen` | semilla de `cg_itsuki_fracaso` | |
| `cg_miku_examen` | semilla de `cg_miku_fracaso` | |
| `cg_cinco_aprobadas` | semilla de `cg_cinco_estudiando` | |
| `cg_cinco_aula` | semilla de `cg_cinco_sentadas` | |
| Chibis: Ichika / Nino / Miku / Yotsuba / Itsuki | — | |
| `miku sonrie` / `yotsuba animada` | — | |

---

### 10. Dudas abiertas

| ID | Duda | Qué propuse |
|---|---|---|
| D-01 | **Blazer:** tu mensaje dice Ichika con blazer y Nino con blazer negro; la guía y los sprites dicen lo contrario (A-03) | Seguí la guía. Si era intencional, avísame |
| D-02 | **`yotsuba animada`** no existe y el núcleo la usa seis veces (A-04) | Cambiar a `yotsuba sonriendo` (coste 0). Ficha opcional en 5.2 |
| D-03 | **Negativo en Tsubaki.2**: no existe el campo (A-02) | Positivo autosuficiente + negativo listo por si el modelo lo muestra |
| D-04 | **Luz de los exámenes**: dorada por coherencia de set; los `*_fracaso` pueden ser distintos (A-07) | Copiar la luz de los fracasos al generar |
| D-05 | **`cg_cinco_aula`**: mi lectura de «POV de ellas mirándonos» (A-01) | Cámara = MC, cinco de frente a cámara, un paso hacia él, libros cerrados. Si querías otro plano, solo cambia la línea de encuadre del prompt |
| D-06 | **`sfx_camara`** falta (A-08) | Conseguir un obturador corto; el código ya lo espera |
| D-07 | `miku sonrie`: ¿hace falta, o `miku relajada` ya lee como sonrisa? | Probar primero; generar solo si no basta |
