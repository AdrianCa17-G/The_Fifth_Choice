# Prólogo — estado

**Terminado.** Guion, arte, audio y nombres cerrados. Siete escenas, trece CG,
catorce sprites, ocho pistas de música, un ambiente y doce efectos.

Lo transversal —cómo se genera el arte, cómo se monta el audio, las trampas del
motor— está en las guías de `docs/`. Aquí solo vive lo propio de esta fase.

---

## 1. Decisión de diseño que condiciona todo

**El prólogo NO otorga puntos.** Ninguna variable `puntos_*` ni `primera_conexion`
se toca. Los tres menús que hay son cosméticos: cambian el diálogo inmediato y
reconvergen.

Esto significa que **la primera decisión puntuada del juego está al inicio del
Capítulo 1**, y es la que escribirá `primera_conexion` y, por tanto, el criterio
de desempate de toda la partida.

---

## 2. Las siete escenas

**1 · Casa de los Uesugi.** Presentación de Futaro por lo que le falta. Deuda
familiar, notas como única cosa que controla. Aparece Raiha.

**2 · La oferta.** Isanari propone el trabajo de tutor. Primer menú cosmético.

**3 · Instituto Asaba.** El profesor felicita por el examen; primer roce con
Itsuki (asiento y bento); azotea. Segundo menú cosmético.

**4 · Camino al departamento.** Futaro calcula mal las premisas.

**5 · La revelación.** Conoce a las cinco. Orden: Ichika, Nino, Miku, Yotsuba, e
Itsuki de última — cambio deliberado respecto al anime, para que el prólogo cierre
con golpe en vez de con enumeración.

**6 · El contrato.** Maruo. Aparece por primera vez la palabra «despedido»,
semilla narrativa del Final Malo.

**7 · El primer intento.** Clase fallida. Cada hermana se escapa a su manera.
Tercer menú cosmético. Cierra en fracaso, no en victoria.

Termina con `jump cap1_inicio`.

---

## 3. Itsuki se llama «Estudiante Nueva» hasta la escena 5

El protagonista no sabe su nombre hasta que ella se lo grita. Hasta ese momento la
caja de diálogo usa `itsuki_inicio`; a partir de ahí, `itsuki`.

Son **31 líneas** las que van con `itsuki_inicio`: doce en el aula, doce en la
azotea (seis de ellas dentro de los dos menús, fáciles de pasar por alto) y siete
en la discusión de la escena 5. Verificado: ni el narrador ni el pensamiento del
protagonista nombran a Itsuki antes de la revelación, así que no hay fuga.

Los `show itsuki` y `hide itsuki` **no cambian**: usan la etiqueta de imagen, que
es otra cosa distinta del personaje aunque se llame igual.

---

## 4. Anzuelos sembrados para recoger después

- **Miku:** Futaro comenta mal el libro de Sengoku y ella lo corrige sin levantar
  la vista — «es logística, las batallas las gana quien mueve el arroz» — y
  después se esconde detrás del libro al darse cuenta de que ha hablado. Cuatro
  líneas que encienden al personaje y plantan su ruta.
- **Itsuki:** el reencuentro en el departamento ya establece la rivalidad.
- **Nino:** «el último duró cuatro días, también entró diciendo que venía a
  trabajar». Es la única vez del prólogo en que tiene razón y Futaro no sabe qué
  contestar.
- **Yotsuba:** su «…¿Verdad?» medio tono más bajo, con el rebote inmediato a
  «¡Digo, claro que sí!». La primera grieta de la armadura.

---

## 5. Revisión de guion ya aplicada — no volver atrás

- **Isanari no revela el número.** Dice «un tutor privado para su familia» y
  «hasta la graduación». Antes decía «sus hijas» y «hasta que se gradúen», en
  plural, y luego Futaro planificaba para «un alumno»: era un agujero, no un
  cálculo mal hecho. El «cinco veces la tarifa» es ahora la única pista.
- **«Quintillizas» se dice después de que entre la quinta.** Antes Nino lo soltaba
  con cuatro en pantalla y desactivaba el remate de «Cinco».
- **Futaro no se disculpa en el prólogo** y no grita insultos. Donde antes decía
  «lamento lo de esta mañana» ahora reafirma su postura, y el «¡niña malcriada!»
  pasó a un «baja la voz, ni siquiera sé tu nombre» dicho en frío. Su disculpa hay
  que guardarla para el arco, no gastarla el primer día.
- **El monólogo del instituto se reescribió** porque el fondo está vacío: ahora
  llega antes que nadie y prefiere los pasillos vacíos. Antes describía pasillos
  llenos de alumnos que no están en pantalla.
- **El reproche repetido de Itsuki se fusionó en una línea.** Se contaba tres
  veces: aula, azotea y departamento.
- **Raiha tiene un registro bajo** además del regañón, e Isanari genera fricción
  con Futaro. Antes ella solo gritaba y él no producía ninguna reacción en su hijo.

---

## 6. CG del prólogo

Diez se declaran en `01_prologo.rpy`: son ilustraciones de momentos concretos de
estas escenas. Los otros tres —`cg_calificacion`, `cg_maruo_reunion` y
`cg_hermanas_estudiando`— subieron a `00_definiciones.rpy` porque la apertura del
Capítulo 1 los reutiliza.

| Archivo | Escena | Qué es |
|---|---|---|
| `cg_familia` | 1 | Retrato familiar. Primer vistazo de todo el juego |
| `cg_calificacion` | 1 | El cuarto con el examen y la nota sobre la mesa |
| `cg_examen` | 3 | Diálogo con el profesor |
| `cg_itsuki_sentada` | 3 | Primer encuentro, ella en su asiento |
| `cg_itsuki_azotea` | 3 | Segundo encuentro, el momento de tregua |
| `cg_manija_edificio` | 4 | La mano en el pomo antes de la revelación |
| `cg_ichika_puerta` | 5 | Primer encuentro con Ichika |
| `cg_nino_pasillo` | 5 | Primer encuentro con Nino |
| `cg_miku_sofa` | 5 | Primer encuentro con Miku |
| `cg_yotsuba_corriendo` | 5 | Primer encuentro con Yotsuba |
| `cg_itsuki_discusion` | 5 | Tercer encuentro con Itsuki, la reveladora |
| `cg_maruo_reunion` | 6 | Maruo establece las condiciones |
| `cg_hermanas_estudiando` | 7 | La sesión de estudio fallida |

### El retrato familiar

Es el CG que no se parece a ningún otro, y a propósito. Composición hecha a partir
de cuatro fuentes distintas (Isanari, la madre, Futaro y Raiha), igualando el
tamaño de las cabezas y unificando el color. **La madre está en escala de grises**
porque falleció; eso resuelve la inconsistencia temporal, ya que cuando murió
Futaro era niño y Raiha un bebé y no existen fotos de esa época.

**Decisión tomada: no se regenera en PixAI.** Es el peor caso posible para esa
herramienta — cuatro figuras en un frame con necesidades de LoRA incompatibles
(Isanari pide 0.1 como adulto masculino, Raiha pide 0.3 para reconocerse, y los
LoRAs no se aplican por región), más una madre que no tiene LoRA y cuyo parecido
es lo único que sostiene la idea narrativa.

En su lugar se hizo un **pase de unificación en post**. El orden importa:

1. Máscara del interior de la foto; el marco y el passepartout no se tocan.
2. Limpieza de los restos de subtítulo del fotograma original de Isanari.
3. Relleno del fleco cálido en la costura Isanari / Futaro.
4. **Igualación de grano**, antes de añadir nada. Isanari traía halftone fuerte
   (~13) y Futaro estaba limpio (~2). Si se añade el grano común antes de este
   paso, a Isanari se le suma al que ya trae.
5. Realce leve de la madre, para que su blandura parezca decidida y no un escalado
   mal hecho.
6. Pase común: suavizado, dominante cálida, viñeta y un solo grano para las cuatro
   figuras.

**Criterio de calidad para este CG:** no debe parecerse al resto del set. Los demás
son plano cerrado, cámara con ángulo y luz dorada saturada; este es una fotografía
enmarcada *dentro* del mundo del juego. Si se alinea con el lenguaje visual del
set, deja de leerse como foto. El estándar es «convence como fotografía», no
«combina con los otros CG».

### Errores que costaron rehacer tres CG

Conviene no repetirlos:

- **`cg_examen` venía con kanji inventado por toda la hoja.** El prompt llevaba
  `text, english text, japanese text` en el campo positivo, arrastrados de cuando
  se creía que había campo negativo. Nombrar lo que no quieres es pedirlo. Ahora
  el papel se describe por lo que se ve: retícula de casillas vacías, cabecera,
  filas numeradas y un maru rojo. Estructura sin escritura.
- **`cg_itsuki_azotea` tenía a Futaro de frente y sin cara.** Se rehízo con él de
  espaldas en primer término y desenfocado, cortado por el borde del cuadro.
- **`cg_nino_pasillo` era vertical**, y salía con bandas negras a los lados. Los CG
  van **siempre apaisados**, 1280×720.

---

## 7. Sprites usados en el prólogo

Catorce en total. Un solo atuendo por hermana: el uniforme escolar, también dentro
del departamento.

| Personaje | Expresión | Archivo |
|---|---|---|
| Ichika | Neutral / Sonriendo | `ichika_neutral` · `ichika_sonrisa` |
| Nino | Neutral | `nino_neutral` |
| Miku | Neutral | `miku_neutral` |
| Yotsuba | Sonriendo | `yotsuba_sonrisa` |
| Itsuki | Neutral / Sonriendo / Molesta / Sorpresa | `itsuki_neutral` · `itsuki_sonrisa` · `itsuki_molesta` · `itsuki_sorpresa` |
| Raiha | Hablando / Regaño | `raiha_hablando` · `raiha_regano` |
| Isanari | Neutral / Sonrisa | `isanari_neutral` · `isanari_sonrisa` |

El profesor, la madre y Maruo no necesitan sprite.

`itsuki_timida.png` existe pero **no se usa**: se generó antes de tener la escena y
no hubo momento para ella. De ahí el criterio adoptado de generar expresiones solo
contra guion escrito.

Se resolvió la confusión `neutral` / `neutral2` de Itsuki: el de brazos cruzados
pasó a llamarse `itsuki_molesta` y el neutral real ocupa `itsuki_neutral`. El alias
viejo `itsuki seria` ya no existe.

Por ese mismo criterio, `miku_aburrida` pasó a `miku_neutral`. Los párpados a
media asta son su cara en reposo, no una emoción; con el nombre viejo no habría
forma de escribirla aburrida de verdad más adelante.

---

## 8. Montaje de audio del prólogo

Los cues están escritos y probados. La escala de volumen, las fuentes y la función
`duck()` están en `docs/GUIA_AUDIO.md`.

### Reparto medido de cada pista

| Cue | Líneas |
|---|---|
| extraneza | 73 |
| cena | 52 |
| caos | 46 |
| azotea (solo viento) | 38 |
| incomodo | 30 |
| derrota | 26 + 25 en silencio |
| contrato | 21 |
| hogar (inicio) | 19 |
| cotidiano ×2 | 12 y 11 |
| hogar (final) | 7 |

### Los cinco silencios

- **El monólogo de apertura**, para que la entrada de `hogar` signifique algo.
- **La campana del instituto**, que suena sola durante una línea entera antes de
  que entre `cotidiano`.
- **`cg_manija_edificio`**, dos segundos de nada antes de la revelación.
- **Antes de que aparezca Maruo**, con `fadeout 0.3`.
- **Desde que sale del edificio hasta «Bien. Que sea difícil».**

---

## 9. Problemas conocidos del prólogo

Los que afectan al set completo están en `docs/GUIA_ARTE.md`. Aquí solo los de
estas escenas:

- **La madre en el retrato familiar** viene de una foto de artbook de 340 px de
  ancho, ampliada. Como sprite en escena funciona; en primer plano se notaría.
- **Composición del comedor:** la mesa está centrada y adelantada. Los sprites hay
  que colocarlos a los lados o quedan plantados encima del mueble. Ya aplicado:
  Raiha e Isanari a 0,20 y 0,73, y Raiha sola a 0,30.
- **El fondo del comedor está pintado con una cámara mucho más lejana que la de
  los personajes.** Isanari de cuerpo entero queda a un palmo de la campana
  extractora y encoge la habitación. En esa cocina conviene colocarlo hacia el
  hueco de la puerta, o reservar ese fondo para planos donde él no salga entero.
- **Itsuki dice que acaba de transferirse** y que las materias son más difíciles.
  Sus cuatro hermanas van al mismo instituto, así que se transfirieron todas. Es
  coherente, pero conviene que lo sea a propósito y no por descuido.

### Resueltos

Cambio de ropa y coleta de Raiha · nombres de sprites de Raiha ·
`itsuki_timida` 24 px corta · `Ichika_sonrisa.png` con mayúscula ·
contradicción texto-imagen en la escena 2 · composición del comedor ·
el interfono que contradecía «toqué la puerta» · la campana pisando a `cotidiano`.

**La condición de Maruo.** Prometía despido si una hermana reprobaba, y el juego
medía afinidad: dos condiciones distintas de las que solo se ejecutaba una. Queda
cerrado en el README — la afinidad representa «logró llegar a ellas y por eso
estudian», y el Final Malo se narra como el despido que él anunció aquí.

**«Auriculares» y «audífonos» en el mismo prólogo.** La escena 5 usaba una
palabra y las escenas 7 y 5 la otra. Ahora las tres dicen audífonos, igual que el
Capítulo 1.

---

## 10. Opcionales que quedaron abiertos

Ninguno bloquea el Capítulo 1:

1. `cg_maruo_espaldas` para el cierre de la escena 6. El prompt de Maruo ya está
   validado y sin rostro visible el LoRA no puede feminizarlo.
2. Variante de tarde de `bg_escuela`.
3. Aplicar el tinte cálido por escena a los sprites.
