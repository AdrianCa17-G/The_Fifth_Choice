# Guía de arte — The Fifth Choice

Todo lo aprendido generando el arte del prólogo. **Es transversal**: aplica a los
tres capítulos que quedan. Leer antes de generar cualquier imagen nueva.

---

## 1. Plataformas y configuración

**PixAI** para generar y **Gemini** para composiciones y correcciones locales
sobre imágenes ya generadas. PixAI en cuenta gratuita: 10.000 créditos diarios
que no caducan.

- **Modelo base por defecto: Tsubaki.2.**
- El LoRA debe coincidir con el modelo base o no hace nada y gasta créditos en
  silencio. Es el fallo más caro de la plataforma.
- **El campo negativo depende del modelo base, no de la cuenta.** Con Tsubaki.2
  no aparece, y de ahí venía la idea de que la cuenta gratuita no lo tenía. Con
  Haruka v2 sí existe, y además **viene relleno con un negativo por defecto** que
  conviene revisar: trae `simple background` y `transparent background`, que
  pelean contra el fondo blanco liso que se pide para los sprites, y `cropped`,
  que pelea contra el encuadre de cuerpo entero. De ahí salían los marcos
  decorativos y los textos japoneses de la nada.
- **Cuando hay campo negativo, úsalo para lo que el positivo no puede:**
  `handcuffs, chains, jewelry, frame, border, multiple views, 2girls, dark skin`.
- **Sin campo negativo, todo va en positivo y describiendo el resultado
  visible**, nunca lo que se quiere evitar.
- Tsubaki.2 no tiene ajustes avanzados salvo la semilla. No hay pasos ni CFG que
  tocar, así que el prompt es la única palanca.

### Compatibilidad de LoRA y modelo base

- **Tsubaki.2 es SD 1.5.** El LoRA de serie de Gotoubun es de esta familia.
- **Los LoRA marcados «Illustrious XL» son SDXL.** Con Tsubaki.2 no hacen nada.
  PixAI autoselecciona **Haruka v2** (SDXL) al cargarlos: no es coincidencia
  exacta pero sí compatible, aunque el LoRA rinde por debajo de su valor nominal.
  Por eso el de Raiha se usó a 0.85 y no a 0.75.
- **Al cambiar de base se pierde el LoRA de serie**, que es de Tsubaki. Con un
  LoRA de personaje Illustrious se va sin LoRA de serie; el de personaje ya trae
  su estilo dentro.

### LoRA de personaje encontrados

| Personaje | LoRA | Base | Fuerza |
|---|---|---|---|
| Ichika | 中野一花 サンプル(アニメ)Tsubaki.2バージョン | Tsubaki.2 nativo | 0.8 |
| Nino | 中野二乃 アニメ(サンプル)Tsubaki.2バージョン | Tsubaki.2 nativo | 0.8 |
| Miku | 中野三玖 アニメ(サンプル)Tsubaki.2バージョン | Tsubaki.2 nativo | 0.8 |
| Yotsuba | 中野四葉 サンプル(アニメ)Tsubaki.2バージョン | Tsubaki.2 nativo | 0.8 |
| Itsuki | 中野五月 サンプル(アニメ)Tsubaki.2バージョン | Tsubaki.2 nativo | 0.8 |
| Raiha | «Raiha Uesugi - The Quintessential Quintuplets», trigger `raihau, hair bow, striped shirt, blue overalls` | Illustrious XL → usar Haruka v2 | 0.7 – 0.85 |

Las cinco hermanas tienen LoRA propio y **nativo de Tsubaki.2**: enganchan a su
valor nominal sin subirles la fuerza, al contrario que Raiha. Con LoRA de
personaje nativo la semilla deja de ser crítica para mantener el parecido entre
expresiones — conviene apuntarla igual, pero ya no obliga a rehacer sets enteros.

Con LoRA de personaje **hay que quitar la redundancia del prompt**, no sumarla:
competir con él es lo que rompe el parecido. El de Raiha trae los ojos turquesa
del anime; se corrigen a marrón por prompt sin pelea.

**Futaro no tiene LoRA.** Esa es la razón de fondo de que salga como silueta
negra cada vez que se le pide de frente. La solución no es prompting: es
encuadrarlo de espaldas, desenfocado y cortado por el borde.

### Pesos de LoRA — ya calibrados

| Caso | LoRA de serie | LoRA de personaje |
|---|---|---|
| Sprite individual de una hermana | **Ninguno** | 0.8 |
| CG individual | 0.3 | 0.7 – 0.8 |
| CG de grupo con las cinco | 0.3 | Ninguno |
| Maruo u otro adulto masculino | 0.1 | Ninguno |

- Los sprites de las hermanas se generan **solo con su LoRA de personaje**. El
  de serie encima metería un cambio de estilo justo en la hermana que se intenta
  emparejar, y el de personaje ya trae su propio estilo dentro.
- **0.3 es el techo del LoRA de serie.** Por encima aparece un artefacto
  constante: una banda blanca sobre el fleco. Si reaparece a 0.3, bajar a 0.2.
- **Sí se apilan LoRAs** (serie + personaje) para figuras individuales. Lo que
  no se puede es aplicarlos **por región**: en un CG de grupo contaminan a las
  cinco, así que en grupo se va solo con el de serie y se describe a cada
  hermana **por rasgos, no por nombre**.
- Con Maruo, el LoRA de serie a 0.2–0.3 le feminiza y envejece el rostro, le da
  volumen al pelo y le contagia ojos azules. A 0.1 se comporta.

---

## 2. Referencia de vestuario y pelo

**Obligatoria para cualquier arte nueva.** Si no está escrito, cada render les
pone otra ropa.

Un solo atuendo por hermana: el uniforme escolar, también dentro del
departamento. Ahorra un set entero de cuerpos y nadie lo cuestiona. Pero **el
uniforme no es igual entre las cinco**: lo único común es la falda verde
plisada, y esa diferencia es justo lo que las hace distinguibles en pantalla.

| Hermana | Pelo | Vestuario |
|---|---|---|
| Ichika | Corto rosa pálido, flequillo en mechones separados de largo desigual con las puntas hacia dentro, silueta redondeada que se ahueca a los lados de la cara. Sin lazos. | Blazer azul marino con ribete blanco, camisa blanca, suéter amarillo atado a la cintura. |
| Nino | Corto, rosa más oscuro y apagado, lazos negros con verde a ambos lados de la cabeza. | Blazer azul marino con ribete blanco, camisa blanca abotonada, calcetas blancas altas. |
| Miku | Castaño, media melena. | Sudadera azul claro con capucha y cremallera, **audífonos azules colgados del cuello, nunca puestos**, medias oscuras. Sin blazer. |
| Yotsuba | Corto naranja, cinta verde en la cabeza. | Chaleco amarillo, camisa blanca de manga corta, lazo verde a cuadros. |
| Itsuki | Rojo intenso, muy largo (por debajo de la cintura), pasadores de estrella amarilla, un ahoge. | Chaleco rojo, camisa blanca de manga corta. Sin blazer. |

| Personaje | Pelo | Vestuario |
|---|---|---|
| Futaro | Negro corto, con un mechón levantado. | **Cárdigan gris claro abierto**, manga larga, camisa blanca de cuello debajo, pantalón azul marino. No es el blazer azul de las hermanas: son prendas distintas y no hay que mezclarlas. |
| Isanari | Rubio arena apagado, corto y en pinchos, gafas de sol apoyadas en la cabeza. Ojos marrones. Delgado y fibroso, **no musculado**. | Camiseta gris oscuro de manga corta, cinturón marrón, pantalón beige, zapatos marrones. |
| Raiha | Castaño oscuro muy largo, flequillo recto, coleta alta con lazo rosa. **Ojos marrones rojizos y piel clara.** | Camiseta de rayas blancas y rosa coral de manga corta, peto vaquero azul con bajos remangados, sandalias. |

Las marcas en negrita de Isanari y Raiha son correcciones que costaron tandas: el
modelo tira a hacerle a él cuerpo de gimnasio y a ella la piel tostada, y ninguna
de las dos cede sin tokens redundantes.

**Miku es la única que no va de uniforme**, y es decisión de guion, no límite de
la herramienta: la separa del bloque de hermanas justo en las escenas donde el
bloque es el problema. Sus audífonos van **siempre al cuello**. Subírselos es un
gesto narrativo —así cierra la puerta cuando alguien se acerca— y si un render se
los pone en las orejas, el gesto deja de existir y hay líneas de diálogo que
dejan de tener sentido. `headphones around neck, headphones resting on
collarbone, not wearing headphones on ears`.

---

## 3. Estándar del set de sprites — cerrado, no cambiar

Toda expresión nueva tiene que salir con estas cuatro constantes o rompe la
continuidad del elenco:

- Lienzo **760 × 930 px**, PNG RGBA con transparencia real.
- Línea de ojos en la fila **y = 199**.
- Distancia interpupilar (IPD) ya escalada: **77,2 px**.
- Eje horizontal: **el centro de la falda** (eje del cuerpo), no el centro del
  bounding box, porque los brazos y el pelo suelto lo desplazan.

**Nombrar por expresión, nunca por rol.** La cara en reposo es `neutral` aunque
parezca aburrida o seria. Con el nombre puesto por lo que transmite, la primera
vez que haga falta la emoción de verdad no queda hueco: pasó con
`itsuki_neutral2` y volvió a pasar con `miku_aburrida`. Y en la declaración de
Ren'Py la expresión va como atributo con espacio, no con guion bajo — ahí está
explicado en `GUIA_RENPY.md`.

La normalización se hace **por distancia interpupilar**, lo único que no depende
del peinado, la pose ni los accesorios. Normalizar por altura de lienzo o por
bounding box fue el error original: las cinco medían 630×930 pero cada una estaba
a una escala distinta por dentro y en pantalla no parecían quintillizas.

### Escalas aplicadas

| Render | IPD crudo | Escala |
|---|---|---|
| `miku_neutral` (antes `miku_aburrida`) | 73,9 | 1,045 |
| `itsuki_molesta` | 60,8 | 1,270 |
| `yotsuba_sonrisa` | 76,4 | **1,011** |
| `nino_neutral` | 71,3 | 1,083 |
| `ichika_neutral` | 68,1 | 1,134 |
| `ichika_sonrisa` (ojos cerrados) | 105,8 | 0,730 |
| `itsuki_sorpresa` | 63,9 | 1,209 |
| `itsuki_timida` | 61,6 | 1,254 |
| `itsuki_sonrisa` | 53,9 | 1,431 |
| `itsuki_neutral` | 48,7 | **1,584** |

**Generar en vertical 768 × 1280 importa mucho.** Yotsuba y Nino vinieron así y
salieron a escala 1,01 y 1,08, prácticamente sin reescalar. Las cuatro de Itsuki
vinieron apaisadas a 1280 × 720 y necesitaron hasta 1,58 de ampliación. Se
compensa con realce con umbral, pero la resolución perdida no vuelve.

**Ojos cerrados: el arco del `^_^` engaña.** En `ichika_sonrisa` los centroides
de los arcos quedan más separados que las pupilas y sobreestiman el IPD un 10 %.
Se calibró comparando el perfil de silueta del pelo contra su propio neutral,
hasta dar con 0,730. Si vuelve a pasar, ese es el método.

El margen superior de 199 px lo fija el lazo de Yotsuba, el accesorio más alto
del elenco. El corte inferior lo fija Itsuki.

### Personajes que no miden lo que las hermanas

Normalizar por IPD iguala el **tamaño de la cabeza**, no la altura. Para un
adulto y una niña hay que mover además la línea de ojos, o los tres acaban con
la cara a la misma altura y la diferencia de estatura no existe.

Partiendo del set (IPD 77,2 con los ojos en 199) y de las alturas 178 / 165 / 138
cm, la escala del juego sale a **7,44 px por centímetro** y el suelo cae en la
fila 1348, muy por debajo del lienzo.

| | escala | fila de ojos | IPD final |
|---|---|---|---|
| Hermanas | referencia | 199 | 77,2 |
| Isanari | por IPD | **109** | 77,2 |
| Raiha | por altura | **388** | **68,3** |

A los tres el lienzo los corta a la misma altura física del suelo, unos 56 cm.
Eso es media pantorrilla en un adulto y por encima de la rodilla en una niña, que
es lo que pasaría en una foto real: la línea de corte es del encuadre, no del
personaje.

Tres cosas que no conviene volver a discutir:

- **Raiha no se normaliza por IPD.** Misma distancia entre pupilas significa misma
  cabeza, y una niña con cabeza de adolescente queda flotando respecto al suelo.
  Su IPD se deriva de la altura una sola vez (68,3) y se aplica igual a sus dos
  expresiones, para que la cara no cambie de tamaño al alternarlas.
- **Isanari a 109**, aunque recorte 24 px de las puntas del pelo en el neutral y
  17 en la sonrisa. A 132 quedaba casi a la altura de las hermanas y la diferencia
  de estatura se perdía entera. Con silueta de pelo en pinchos el recorte no se ve.
- **109 es el techo del lienzo.** Para subirlo habría que recortarle cráneo, no
  puntas. Si algún día se quiere más diferencia hay que cambiar el margen superior
  del set, no su escala.

---

## 4. Recorte y limpieza de sprites

### Huecos blancos: fondo o ropa

Al recortar hay que decidir qué blanco encerrado es fondo (transparente) y cuál es
ropa (opaco). El criterio del entorno no vale: el hueco entre los dedos está
rodeado de piel igual que la raya de la camiseta lo está de tela.

La primera regla fue la pureza, y **no basta**. Con Ichika borraba su camisa
entera: mide 250,9–254,5 de pureza, exactamente lo mismo que el fondo, y los dos
parches del pecho (4151 y 3913 px) cumplían el umbral al pie de la letra.

**El discriminante que sí funciona es el color del contorno.** Un hueco de fondo
está rodeado de piel o pelo, que son cálidos; la ropa blanca y sus sombras son
frías. Un hueco encerrado se borra solo si cumple **las dos** condiciones:

- **Pureza media ≥ 253,5**, y
- **calidez del contorno (r − b) ≥ 20**.

Separación medida: hueco de pelo de Itsuki 254,8 / +66. Camisa de Ichika 253,7 /
+4. Dientes 250,9, protegidos por el filtro de pureza. No está al límite.

**El filtro de lineart del contorno se mide por luminancia, no por canal mínimo.**
Descartar la lineart con `min(r,g,b) > 120` parece razonable hasta que llega el
pelo rojo de Itsuki, cuyo canal mínimo ronda 70–111: el contorno entero se
descartaba y le quedaba un parche blanco de 3445 px, visible a leguas. Con
`media > 70` se quita la lineart negra sin tocar el pelo saturado. Área mínima
del hueco: 40 px.

**Excepción conocida — Yotsuba.** Su paleta es amarillo, naranja y verde, así que
su cuello blanco está pegado al chaleco amarillo y mide cálido igual que el pelo.
La regla no puede distinguirlos y le comió una tira del cuello. Sobre un PNG ya
recortado hay que usar `--solo-halo`; desde el render original sí funciona bien.

### Halo blanco del contorno

Los recortes binarios dejan los píxeles del borde con el blanco del fondo mezclado
dentro del color, y al componer sobre el fondo oscuro del apartamento se ve un
contorno lechoso. Yotsuba lo tenía: sus píxeles de borde promediaban RGB
(206, 190, 183).

Se corrige por **desmatteado**. El píxel guarda `C = a·C_real + (1−a)·255`, así
que se despeja `C_real`. No hace falta filtrar por color: si el píxel es blanco
de verdad, quitarle el blanco devuelve blanco. Solo se excluyen los alphas por
debajo de 0,28, donde la división amplifica el ruido.

**Y al escalar hay que premultiplicar el alpha.** Si se reescala el RGBA sin
premultiplicar, Lanczos mezcla el RGB de los píxeles transparentes —que sigue
siendo el blanco del fondo— dentro del borde.

**Aviso para no perder el tiempo:** la línea clara fina entre los mechones **no es
halo, es el dibujo**. Escaneando el render crudo aparece un píxel en
(207, 168, 169) entre dos valores de rojo oscuro. Es la separación de mechones que
dibuja el modelo. Si se intenta quitar, se rompe el pelo.

---

## 5. Herramientas de post

Cuatro scripts de Python en `herramientas/`, **fuera de `game/`**. No son scripts
de Ren'Py. Requieren Python de python.org con `pillow`, `numpy` y `scipy`.

| Script | Qué hace |
|---|---|
| `normalizar_sprite.py` | Recorta el fondo y normaliza un sprite de hermana al estándar del set. Opciones: `--ojos`, `--eje`, `--huecos`, `--sin-huecos`. |
| `limpiar_halo.py` | Sobre un sprite **ya normalizado**: desmatteado del contorno y borrado de huecos encerrados. `--solo-halo` para Yotsuba. |
| `normalizar_extra.py` | Lo mismo para Isanari y Raiha, con sus filas de ojos propias y el modo por altura de Raiha. |
| `escalar_cgs.py` | Pasa un lote de CG y fondos a 1920×1080 con Lanczos y WebP 95. Realce de nitidez **solo a las fuentes JPEG** y con umbral. |

```
python normalizar_sprite.py entrada.png salida.png
python limpiar_halo.py entrada.png salida.png [--solo-halo]
```

**Detección de ojos: los scripts buscan iris azul.** Isanari y Raiha los tienen
marrones y Maruo negros, así que con ellos hay que pasar `--ojos x1,y1,x2,y2`
copiando las coordenadas de las pupilas de otra versión del mismo render. Con los
ojos cerrados la detección también falla.

Dos trampas ya resueltas en la detección: el umbral del azul subió a `b−r > 60` y
`b−g > 50`, y la búsqueda se restringe al 42 % superior de la figura. Con el
umbral flojo, los brillos azules del blazer de Ichika eran más grandes que su iris
y ganaban por tamaño: su neutral medía IPD 184 en vez de 68.

**Extensión inferior automática:** si el render venía cortado por el borde del
frame y al normalizar el contenido se queda hasta 30 px corto, el script prolonga
la última fila. Ahí solo hay pierna y el corte lo marca el encuadre. Es lo que
resolvió el problema de los 24 px de `itsuki_timida`.

Si se tiene el render original, siempre es mejor volver a pasar
`normalizar_sprite.py` que usar `limpiar_halo.py`: trabaja antes de recortar y
escalar, y el resultado es más limpio.

**Saturación de referencia del set:** los CG aprobados están entre **68 y 84** de
saturación media. Los que salgan muy por debajo se corrigen en el escalado, no
regenerando — salvo que el contenido justifique el color bajo.

---

## 6. Prompting

### Fórmula que funciona — bloques en este orden

1. `single seamless illustration, one continuous frame, widescreen visual novel CG, masterpiece, best quality, official anime screencap, go-toubun no hanayome style`
2. **Encuadre** — hay que forzarlo con tokens redundantes; el modelo tiende al
   plano medio centrado y a la figura de pie.
3. **Personaje** — `1girl, solo, only one person in the entire image` + nombre +
   rasgos + expresión.
4. **Pose y vestuario.**
5. **Background** — copiar literal entre CG para mantener la continuidad.
6. **Iluminación** + `deep focus, entire scene in sharp detail, clean lineart, natural hands with five fingers`.

### Reglas aprendidas

- **Nunca escribir «without X» ni «no X»**: el modelo ignora la negación
  gramatical y genera X. Nombrar lo que no quieres es pedirlo.
- **Excepción:** las etiquetas tipo danbooru sí funcionan aunque suenen a
  negación (`no humans`, `plain hair with no ribbons`). Son etiquetas entrenadas.
- Los descriptores difíciles (largo de pelo, estar sentada, expresión no
  sonriente) necesitan **2–3 tokens redundantes distintos**.
- Para expresiones serias funcionan mejor los conceptos en positivo
  (`calm neutral`, `subdued`, `closed mouth`) que las negaciones.
- Generar tandas de prueba con **steps bajos** antes de gastar créditos.

### Plantilla para fondos

```
masterpiece, best quality, absurdres, scenery, indoors, no humans,
[DESCRIPCIÓN DE LA ESCENA],
soft lighting, bright colors, pastel colors, soft shading,
detailed background, anime background art, wide shot
```

El que hace el trabajo es `no humans`. Si aun así se cuela una figura, reforzar
en positivo (`empty room, unoccupied, scenery only`) o cambiar la semilla.

Para el cuarto de Futaro añadir: `sparse room, bare walls, worn furniture, old
books, shabby, few belongings`. Los generadores tienden a hacer habitaciones
demasiado acogedoras, y la casa es de una familia que cuenta el dinero.

### Bloque de fondo del departamento

Copiar **literal** entre CG donde se ve la sala completa. Versión luz de tarde:

```
indoors, double height loft apartment living room, exposed red brick wall,
black metal staircase with glass railing leading to a second floor landing,
long horizontal built in aquarium glowing under the staircase, green aquatic
plants and a fish inside the tank, dark wooden cabinets covering the back wall,
white leather three seater sofa with cushions, low dark wood coffee table,
white shaggy rug, black leather armchair, small round table lamp,
dining table with dark chairs behind the sofa, kitchen counter on the right
with hanging pendant lights, dark hardwood floor, floor to ceiling window on
the left, low wide steps beside the window, dark wooden interior door in the
back wall,
warm late afternoon sunlight streaming through the tall window, long light rays
across the floor, soft warm shadows, teal glow from the aquarium, soft shading,
anime background art
```

**Noche:** el ventanal es lo único que delata la hora. Si el encuadre apunta a la
pared del fondo, el ventanal queda fuera de plano y el interior puede estar bien
iluminado sin contradecir la noche. El segundo párrafo pasa a:

```
warm interior lighting, all indoor lamps turned on, glowing pendant lights over
the counter, bright evenly lit room, teal glow from the aquarium, soft warm
shadows on the floor, soft shading, bright colors, anime background art
```

Para una versión nocturna sin regenerar, `bg_departamento_noche` ya está definida
en `00_definiciones.rpy` con `MatrixColor`.

### Ficha de prompt de Maruo

Adulto joven de treinta y pocos, delgado, cara estrecha de mandíbula suave, ojos
pequeños y negros de párpado caído, pelo negro muy corto con matiz verdoso solo
en los brillos y flequillo recto. Traje negro, camisa blanca, corbata azul
**sólida** (sin rayas). Trazo más plano que el de las hermanas.

```
young adult man in his early thirties, soft rounded jawline, plain simple face,
small narrow eyes, drooping half lidded eyes, black eyes, dark black eyes,
very short black hair, pure black hair, jet black hair with faint dark green
highlights, low volume hair, matte hair with minimal highlights,
simple flat shading on the face
```

El LoRA tira fuerte hacia los ojos azules de las hermanas: los tres tokens
redundantes de negro no son opcionales.

---

## 7. Estilo visual de los CG

Todos los CG comparten este lenguaje. Cualquier CG nuevo debe cumplirlo:

- **Plano cerrado y cámara con ángulo.** Nada de plano medio centrado y frontal:
  picado, contrapicado o dutch angle, con la figura ocupando casi todo el alto.
- **El fondo se sugiere, no se describe entero.** Dos o tres elementos
  reconocibles (ladrillo, escalera, acuario, lámpara) y el resto recortado o
  desenfocado. Describir la sala completa produce una ilustración de catálogo de
  muebles.
- **Luz dorada muy saturada** en todos. Es lo que da unidad al set; un CG en tonos
  fríos canta aunque el encuadre sea perfecto.
- **Bandas de brillo horizontales muy marcadas en el pelo.** Lo trae el LoRA de
  serie y es parte de la firma visual: no hay que corregirlo.
- **Excepción:** los CG de grupo van en **plano frontal, las cinco en fila a la
  misma profundidad**. Es la disposición que mejor tolera el modelo, porque cada
  cara ocupa su propio espacio horizontal. Las composiciones a distintas
  profundidades son más cinematográficas y mucho más frágiles.

### CG con Futaro en cuadro — el POV

No tiene LoRA, así que de frente sale roto. El lenguaje ya validado en
`cg_manija_edificio` y `cg_itsuki_azotea` es el que se repite en todos los CG
nuevos donde él aparece:

- **Primer término inferior**, sus manos o antebrazos sosteniendo algo (el pomo,
  el cuaderno, el temario), **desenfocados y cortados por el borde del cuadro**.
- **Nunca la cara, nunca el torso entero, nunca de frente.** Si hay que verle el
  cuerpo, de espaldas y desenfocado.
- **Un solo personaje con LoRA en el frame.** Él no cuenta porque no es un
  personaje para el modelo: es un objeto en primer plano.

`cg_pupitre_manana` y `cg_estudio_biblioteca` van los dos con esta receta. La
ventaja no es solo técnica: un plano subjetivo obliga al jugador a mirar desde
donde mira él, que es justo lo que hace el juego con el protagonista sin rostro.

### CG en pareja — misma semilla, un solo cambio

Cuando dos CG son el mismo plano con una diferencia deliberada —`cg_cinco_sentadas`
contra `cg_hermanas_estudiando`, o `cg_miku_biblioteca` contra `cg_miku_sorpresa`—
la lectura depende por completo de que todo lo demás coincida: encuadre, luz,
distancia, sitio. **Generarlos en la misma sesión, partiendo de la misma semilla,
y guardarla.** Si se hacen con semanas de diferencia no van a coincidir, y la
comparación que sostiene la escena deja de leerse: el jugador ve dos ilustraciones
distintas en vez de un antes y un después.

### CG de grupo — separar a las cinco

Ichika, Nino e Itsuki están las tres en la gama rosa-roja y el modelo las promedia:

- **Ichika:** `short light pink hair, pastel pink hair, soft baby pink hair, plain hair with no ribbons`
- **Nino:** `short reddish pink hair, darker rose pink hair, large black and green ribbons tied on both sides of her head, twin ribbons, prominent hair ribbons`
- **Itsuki:** `very long bright red hair, deep crimson red hair, vivid red hair reaching past her waist, long flowing hair, waist length hair`

`one strand of hair sticking up` para el ahoge de Itsuki tiende a generar **dos**
ahoges. Con el pelo rojo y las estrellas ya se distingue de sobra, así que se
puede omitir.

Yotsuba en manga corta necesita redundancia: `short sleeve white shirt, bare arms,
sleeves ending above the elbow`. El token que más trabaja es `bare arms`, porque
describe el resultado visible en vez del corte de la manga.

**Contaminación de vestuario:** con cinco figuras los atributos se difunden entre
vecinas (el chaleco rojo de Itsuki se le pasa a Nino, que están pegadas). Se
mitiga engordando el vestuario del afectado con redundancia y encerrando el
atributo en su dueña (`red vest only on this girl`).

**Jerarquía de qué defender cuando no sale todo:** primero que sean cinco, luego
los colores de pelo, luego las poses, y el vestuario al final. Un blazer mal
asignado se nota mucho menos que una sexta hermana.

---

## 8. Resoluciones y postproducción

- **CG y fondos:** generar a **1280×720** y escalar a 1920×1080 con Lanczos.
  Generar directo a 1920 produce composiciones duplicadas. Si la fuente es JPEG,
  aplicar realce de nitidez **con umbral** — el umbral evita amplificar los
  bloques de compresión en las zonas planas. Guardar en WebP calidad 95.
- **Sprites:** generar **siempre en vertical, 768×1280**, nunca apaisado. Un
  render apaisado corta las piernas demasiado arriba y arrastra a todo el elenco.
  Encuadre de cuerpo entero que llegue al menos por debajo de la rodilla, fondo
  blanco liso, sin sombra proyectada. Los sprites **no** pasan por el flujo de
  escalado: van por `normalizar_sprite.py`.

### Corrección local en Gemini — flujo validado

Para arreglar detalles de un CG ya generado sin volver a tirar tandas:

- Se le dan **dos imágenes**: el CG y el sprite de referencia del personaje.
- Se **numera cada cambio** («CHANGE 1», «CHANGE 2») y se identifica al personaje
  **por posición y rasgos, no por nombre**.
- Se enumera **explícitamente todo lo que debe quedar igual**: las otras hermanas,
  la mesa, el fondo, la iluminación.
- Se insiste en igualar grosor de línea, sombreado plano y gradación de color, y
  en que la edición parezca pintada en la misma pasada.
- Se pide la imagen completa al mismo encuadre y resolución.

**Riesgo:** cada pasada reinterpreta la imagen entera y puede **deshacer
correcciones anteriores** (pasó dos veces con el chaleco rojo de Nino). Además el
trazo se ablanda y el fondo pierde definición con cada iteración. Máximo dos o
tres ediciones encadenadas. Gemini comprime en JPEG y eso **no se recupera**:
subir el WebP por encima de 95 solo guarda los artefactos con más fidelidad.

### Lo que no funciona

Quitar personajes de fotogramas del anime por clonado o inpainting clásico. Se
intentó con un fotograma del comedor y falla: detrás de los personajes hay ollas,
muebles, patas de mesa y sombras que no son repetitivas, y no hay franjas limpias
de las que copiar. Para eso hace falta inpainting generativo o generar el fondo
desde cero.

---

## 9. Pendientes del set

Cosas abiertas que afectan a todo el arte, no solo al prólogo:

- **El pelo de Miku no coincide entre CG y sprite.** En los CG quedó castaño
  oscuro tras la corrección en Gemini; el sprite sigue en castaño claro. Hay que
  decidir cuál manda, porque si no la inconsistencia se arrastra a todo el juego.
  **Esto se decide antes de generar el evento de la biblioteca**, que trae tres CG
  suyos: si se generan sin resolverlo, el problema pasa de dos imágenes a cinco.
- **La falda de `itsuki_neutral` es olivácea.** Color medio (92, 102, 74) frente a
  (90, 118, 63) del resto del set. Alternar esa expresión con otra en la misma
  escena hace que la falda cambie de tono en pantalla. Se corrige en post con un
  ajuste de tono sobre la región verde, sin regenerar.
- **El corte inferior del set sigue fijado por Itsuki.** Sus cuatro renders
  vinieron apaisados en 1280 × 720. Para subir el corte hay que regenerarla en
  vertical y rehacer las cinco. Cuanto más tarde, más sprites hay que rehacer.
- **El lazo de Yotsuba viene cortado en el propio render**: hay verde en la fila 0
  del PNG original de PixAI. No es la normalización. Para tenerlo entero hay que
  regenerar con más margen arriba.
- **Los sprites vienen con luz de estudio plana y los fondos con luz cálida.** Se
  arregla con un tinte cálido por escena aplicado a los sprites, no al fondo. No
  hay que regenerar nada.
- **Las gafas de Isanari cambian de sitio entre sus dos sprites**: caladas en el
  neutral, en la frente en la sonrisa. Decisión tomada: se asume. Lo único que
  conviene evitar es alternarlos en réplicas consecutivas.
- **Faltan expresiones a Nino, Miku y Yotsuba.** Cuatro ya tienen guion detrás y
  se pueden generar: `nino pillada` y `yotsuba incomoda` (apertura del Capítulo 1)
  y `miku animada` y `miku encogida` (evento de la biblioteca). Las fichas de las
  cuatro están en `docs/CAP1.md`. Para las que no tienen escena todavía sigue
  valiendo la lección de `itsuki_timida`: generar contra suposición produce arte
  que no se usa.
- **La diferencia entre expresiones tiene que estar en la silueta.** Es la regla
  que sale de las cuatro fichas nuevas y vale para todas las que vengan: a un 30 %
  de tamaño la cara no se lee. `nino pillada` descruza los brazos, `yotsuba
  incomoda` ocupa menos ancho, `miku animada` se queda sin nada delante del
  cuerpo. Si dos expresiones tienen la misma silueta, en pantalla son la misma.
