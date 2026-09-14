# Guía de audio — The Fifth Choice

Fuentes, licencias y todo lo aprendido montando la capa de audio del prólogo.
**Es transversal**: aplica a los tres capítulos que quedan.

---

## 1. Estructura y nombres

```
game/audio/bgm/    hogar, cena, cotidiano, incomodo,
                   extraneza, caos, contrato, derrota      (.ogg)
game/audio/sfx/    papel_mesa, timbre, silla, toque_puerta,
                   manija, puerta_abre, correr, portazo,
                   bolsa, hoja, puerta_cierra              (.mp3)
game/audio/        amb_viento.ogg
```

**Los nombres de archivo no repiten el prefijo de su carpeta. Las variables sí lo
conservan.** `define audio.sfx_timbre = "audio/sfx/timbre.mp3"`. En el guion,
`play sound sfx_timbre` se distingue de un vistazo de `play music cotidiano`, y
eso se pierde si se acortan los dos lados a la vez. Los ocho BGM no lo necesitan
porque `hogar`, `cena` o `contrato` ya son palabras que no se confunden.

**OGG para todo lo que cicle, MP3 para los efectos puntuales.** El MP3 mete un
silencio en el punto de bucle: un golpe de puerta no cicla, un viento sí.

Todo en minúsculas, sin espacios ni tildes. Ren'Py distingue mayúsculas en Linux
y Android: un `SFX_Papel.mp3` funciona en Windows y revienta al exportar.

**Renombrar un `define` obliga a renombrar todos sus `play`.** Es la causa de que
el archivo quedara a medias una vez, con cinco pistas con prefijo y tres sin él
apuntando a nombres inexistentes.

---

## 2. Fuentes y licencias

| Sitio | Condición |
|---|---|
| 効果音ラボ (soundeffect-lab.info) | Sin crédito, sin informe, sin enlace. Empaquetar en el juego permitido. Prohibido redistribuir los archivos sueltos y el uso adulto |
| 魔王魂 | CC BY 4.0. Crédito **obligatorio**: `音楽：魔王魂`. Autoriza el cifrado para creación de juegos |
| DOVA-SYNDROME | Uso en juegos permitido. Gestionan su propio Content ID y no reclaman. **Pasó a llamarse OpenTracks el 15/09/2026** |
| Springin' Sound Stock | Crédito opcional. Uso comercial y venta de juegos permitidos |
| PeriTune | Crédito opcional. Prohibido registrar en Content ID |

**効果音ラボ es la fuente por defecto para efectos.** Es la única que no pide
crédito de ninguna clase, y su catálogo es de vida cotidiana japonesa, que es
exactamente lo que pide este juego: campana escolar, silla de aula, bolsa de
conbini.

### Alternativas si algo no aparece

- **Freesound** con el filtro «Creative Commons 0»: más de 730.000 sonidos, cerca
  de la mitad CC0, sin crédito. El filtro se aplica **por búsqueda** y hay que
  volver a marcarlo cada vez.
- **Pixabay**: licencia propia, uso comercial y sin atribución. Catálogo más
  pequeño pero se busca en español.
- **Sonniss GDC bundle**: calidad de estudio, descarga directa sin cuenta. El
  paquete de 2026 son 7,47 GB en WAV.
- **OtoLogic**: CC BY 4.0, crédito «OtoLogic». Japonés, tiene campana escolar.
- **ポケットサウンド**: gratis con crédito; admiten ponerlo en la página de
  presentación si no cabe dentro del juego.

**On-Jin queda descartada:** piden contacto previo si hay actividad comercial.

**YouTube no es una fuente.** Los canales de «sin copyright» no son titulares de
casi nada de lo que reparten y lo que dan es una descripción de vídeo, no una
licencia.

### Cómo buscar en 効果音ラボ

El buscador **no entiende frases**, solo palabras sueltas: `書類を置く` da cero
resultados, `紙` da veinte. La descarga es **un clic izquierdo**, no clic derecho.
Baja el **WAV** si vas a recortar, y exporta a MP3 al final: recortar un MP3 y
volver a exportarlo comprime dos veces.

---

## 3. Las ocho pistas

| Cue | Pista | Fuente |
|---|---|---|
| `hogar` | ピアノ34「静寂の世界へ」 | 魔王魂 |
| `cena` | アコースティック04 | 魔王魂 |
| `cotidiano` | ピアノ25「Cookie Cookie」 | 魔王魂 |
| `incomodo` | Zany Escape (Kobat) | DOVA |
| `extraneza` | 日曜の午後 (KK) | DOVA |
| `caos` | Busy As A Bee (ハモおた) | DOVA |
| `contrato` | Night Shade Story (shimtone) | DOVA |
| `derrota` | ピアノ09 | 魔王魂 |
| `amb_viento` | 風 孤独感 | Springin' Sound Stock |

### La novena pista — pendiente

`descubrimiento`, para el Capítulo 1. Ninguna de las ocho sirve: `cotidiano` es
transición, `hogar` está reservado a Futaro y las cinco restantes son tensión o
derrota. Los cinco eventos de hermana necesitan lo mismo —algo tranquilo y con
curiosidad, sin dulzura— y una sola pista los cubre.

**Regla de uso: suena únicamente mientras habla la hermana**, entra cuando se
suelta y sale en el momento en que se corta. Si acompaña también al razonamiento
de Futaro deja de ser el tema de ellas y pasa a ser fondo, que es exactamente el
error del que nació `cena`.

Si no se produce, las escenas aguantan en silencio. En el evento de la biblioteca
ni se nota: es una biblioteca.

**`hogar` suena exactamente dos veces en todo el prólogo**: bajo el retrato
familiar y en «Bien. Que sea difícil». Es el tema de Futaro. Si sonara también
durante la cena dejaría de ser un tema y sería fondo — por eso existe `cena`.

**El viento se alargó a mano en Audacity.** El original dura 4 s y un ciclo tan
corto se reconoce enseguida. Se repitió 7 veces hasta 35 s con fundidos de un
segundo en los extremos. Queda un bajón de volumen cada 35 s, imperceptible
porque va por debajo del diálogo.

---

## 4. Los doce efectos

Todos de 効果音ラボ. Los términos de búsqueda son en japonés, que es lo único que
entiende su buscador.

| Variable | Origen | Notas de montaje |
|---|---|---|
| `sfx_papel_mesa` | 紙を広げる1 | Comprimido y normalizado: venía muy bajo |
| `sfx_timbre` | 学校のチャイム | Original 26 s → recortado a 5 s con fundido de salida |
| `sfx_silla` | 教室の机の椅子を引く | Normalizado; el archivo original era muy flojo |
| `sfx_toque_puerta` | 木のドアをノック1 | Dos golpes sobre madera |
| `sfx_manija` | ドアノブをひねる1 | Menos de 1 s a propósito, ver más abajo |
| `sfx_puerta_abre` | ドアを開ける2 (残響少なめ) | Pareja seca con `puerta_cierra` |
| `sfx_correr` | 学校の廊下を走る | 5,7 s → 1 s, últimos 4 pasos, con el último amplificado 3 dB para fabricar la frenada |
| `sfx_portazo` | derivado de `puerta_cierra` | Amplificado y con la entrada recortada |
| `sfx_bolsa` | ビニール袋 | 17 s → 1 s, el tramo del 0:14 al 0:15 |
| `sfx_hoja` | ページをめくる1 | La versión lenta, no la rápida |
| `sfx_puerta_cierra` | ドアを閉める2 (残響なし) | Un solo archivo, cinco reproducciones |

**`portazo` y `puerta_cierra` son la misma puerta a propósito.** El portazo se
fabricó a partir del cierre: amplificar al máximo sin distorsionar y recortar la
entrada, que es el roce de la hoja moviéndose antes del golpe. Sin esa entrada, el
oído lee el sonido como una puerta abierta de golpe. Si algún día se sustituye
uno, revisar el otro.

**`manija` tiene que quedar por debajo de un segundo.** El siguiente efecto entra
nueve líneas después y ambos caen en el canal `sound`, que es único: si el jugador
va rápido, uno corta al otro.

**Los sonidos secos importan.** `puerta_abre` y `puerta_cierra` se eligieron los
dos sin reverberación y casi seguro de la misma sesión de grabación. Sin cola de
eco, el mismo archivo aguanta bien los distintos volúmenes de la escena 7 sin que
se delate la repetición.

---

## 5. Escala de volumen

**La referencia es 2.5, no 1.0.** Ren'Py multiplica de verdad por encima de 1.0.

| Nivel | Qué |
|---|---|
| 2.5 | Portazo de Itsuki, y los tres sonidos suaves de origen: papel, silla, bolsa |
| 2.0 | Hoja, y la puerta de Nino en la escena 7 |
| 1.75 | Pasos de Yotsuba |
| 1.5 | Campana, toque de puerta, pomo, puerta que abre Ichika |
| 1.2 | Las tres puertas que se cierran después de la de Nino |
| 1.0 | La puerta de Maruo |

Los tres suaves están arriba **porque el archivo es flojo, no porque la escena lo
pida**. La de Maruo está abajo a propósito: cierra «con la calma de quien ya dio
una orden», y que suene bajísimo comparado con todo lo demás dice exactamente eso.

**Lo que no puede pasar es que un pomo suene como un portazo.** Si hay que subir
algo, subir el archivo, no el número.

### La regla de fondo

**Los volúmenes se calibran contra la música que suena debajo, no en abstracto.**
El papel se puso primero a 0.4 razonando sobre el papel solo, y estaba mal: `cena`
es guitarra acústica y ocupa su mismo rango de frecuencias. No era cuestión de
nivel sino de enmascaramiento.

### Nivel global de la mezcla

```renpy
renpy.music.set_volume(0.8, channel="music")
```

En el `init python` de `00_definiciones.rpy`. La música arranca al 80 %. Con las
ocho pistas al 100 % los efectos suaves quedaban tapados por completo. Esto no
pisa el control del jugador, solo cambia el punto de partida.

**Ojo al depurar:** el control de música de las preferencias es un multiplicador
global. Si el jugador lo pone al máximo y los efectos a la mitad, la proporción la
fija el menú y no el guion. Probar siempre con los dos controles a la par, que es
como va a llegar el juego a la gente.

### Cuando un efecto no se oye

En este orden:

1. **Normalizar** el archivo a −1 dB en Audacity. Si la onda ocupa una franja fina
   en el centro de la pista, viene grabado bajo y ningún número lo va a arreglar.
2. **Comprimir y volver a normalizar.** El compresor sube todo lo que está por
   debajo del pico y hace que el sonido ocupe más aunque el máximo no cambie. Ese
   orden —comprimir, luego normalizar— es el que gana volumen percibido.
3. **Ducking**, solo si sigue perdiéndose.
4. **Cambiar el archivo.** Si después de todo esto sigue tapado, la respuesta
   honesta no es seguir apretando: hay sonidos intrínsecamente pequeños y hay
   pistas que no les dejan sitio.

---

## 6. Ducking

```renpy
$ duck()
play sound sfx_papel_mesa volume 2.5
```

La función vive en el `init python` de `00_definiciones.rpy`:

```renpy
def duck(nivel=0.4, bajada=0.2, subida=1.5):
    renpy.music.set_volume(nivel, delay=bajada, channel="music")
    renpy.music.set_volume(1.0, delay=subida, channel="music")
```

Las dos llamadas no se encadenan: se lanzan a la vez con sus tiempos propios. Por
eso la subida es más lenta que la bajada — «se aparta rápido, vuelve despacio» es
lo que lo hace imperceptible. Al revés se nota muchísimo.

**Solo para sonidos sin ataque que compiten con una pista ya sonando.** Si se usa
en todas partes deja de ser una excepción y se oye como bombeo: una pista que se
encoge y se estira catorce veces suena a fallo técnico, no a intención.

En el prólogo hay exactamente tres: el papel bajo `cena`, la silla bajo
`incomodo` y la bolsa bajo `caos`. La hoja no lleva, porque suena sobre silencio.

Si un sitio necesita más margen, `duck(0.3)`. Si necesita más tiempo,
`duck(0.4, 0.2, 2.5)`.

---

## 7. Canales

```renpy
renpy.music.register_channel("ambiente", "music", loop=True)
```

Canal aparte para sonidos de fondo en bucle que deben sonar por debajo de la
música sin cortarla. **Va al mezclador de música, no al de efectos.** Con `sfx` el
viento se comportaba como un golpe puntual: se ponía delante del texto en vez de
quedarse detrás. Además así el jugador lo regula desde el control de música, que
es donde lo va a buscar.

El ambiente lleva volumen explícito y fundido largo:

```renpy
play ambiente amb_viento fadein 3.0 volume 0.35
```

Un ambiente no empieza, ya estaba ahí. Con tres segundos entra sin que se note el
momento exacto. El 0.35 es bajo a propósito: los ambientes funcionan mucho más
bajos de lo que uno cree, y el criterio es que a mitad de escena ya no te acuerdes
de que está sonando, pero que si lo quitaras lo echaras de menos.

---

## 8. Montaje — lo que se aprendió en el prólogo

### Los silencios rinden más que las pistas

Son la parte que más trabaja y la que más se olvida. En el prólogo hay cinco:

- **El monólogo de apertura.** Hace que la entrada de `hogar` signifique algo.
- **La campana del instituto.** Suena sola, sobre silencio, durante una línea
  entera; `cotidiano` entra después. Antes sonaban a la vez y chocaban: la campana
  es una melodía con notas concretas y la pista está en otra tonalidad. Dos
  melodías en tonalidades distintas disuenan aunque una esté bajita.
- **`cg_manija_edificio`.** Dos segundos de nada antes de la revelación.
- **Antes de que aparezca Maruo**, con `fadeout 0.3`. Corte seco: aquí el juego
  deja de ser una comedia.
- **Desde que sale del edificio hasta «Bien. Que sea difícil».** «Despedido.» cae
  en seco. La música vuelve cuando decide no rendirse, no antes.

### Medir cuántas líneas cubre cada pista

Es la comprobación que descubre errores invisibles leyendo el guion. En el prólogo
aparecieron dos: `caos` sonaba **5 líneas** (una pista de 2:52 desperdiciada) y
había un `cotidiano` de **6 líneas** que no daba tiempo ni a entrar con su propio
fundido.

Tres decisiones de montaje salieron de esa medición:

- **`caos` arranca en el portazo de Itsuki**, a la vez que el golpe, no después de
  «Quintillizas». Antes `extraneza` cargaba con 114 líneas y seis ánimos distintos.
- **La azotea va sin música, solo viento.** Ahí los dos están callados sin saber
  qué decirse: no es la bronca del aula, es lo contrario. Resolvió de paso que
  `incomodo` tuviera que servir a dos escenas opuestas, y sin gastar una pista.
- **`derrota` se corta antes del portazo de Nino.** Las cuatro puertas suenan sobre
  silencio, que pesa más, y la pista deja de dar cinco vueltas.

### El silencio también es el sitio

En el evento de la biblioteca el silencio no hay que fabricarlo, ya está en el
escenario. Eso lo convierte en el mejor lugar del juego para estrenar una pista:
cuando `descubrimiento` entra sobre una sala en la que no sonaba nada, la entrada
se oye entera. La regla general que deja el prólogo se sostiene aquí sin esfuerzo
— **una pista solo significa algo si antes hubo silencio.**

### Un capítulo entero puede no necesitar efectos nuevos

La apertura del Capítulo 1 y el evento de Miku se montan **con los doce efectos
que ya existen**: timbre, hoja, papel, silla y las dos puertas. Antes de salir a
buscar sonidos nuevos, revisar la tabla de arriba: los archivos ya están
recortados, normalizados y calibrados contra la música, que es la parte cara. Un
efecto nuevo cuesta una tarde; reutilizar uno cuesta escribir su nombre.

### La repetición idéntica es un recurso

Las cuatro puertas de la escena 7 usan el mismo archivo sin variar nada más que el
volumen. Que se repita igual es lo que hace que la última suene más sola que la
primera.
