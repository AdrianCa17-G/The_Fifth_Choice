# Pulido visual (sesión 1): diseño

Fecha: 2026-11-15 · Ren'Py 8.5.3 · 1920×1080

## 1. Intención

Este es el pulido antes del lanzamiento del Capítulo 1. No es un rediseño. Hay cuatro piezas:

- (A) Un rótulo breve antes de cada decisión con peso. Marca «esto importa» con el color de la hermana.
- (B) Tarjetas de decisión sin el hueco grande que hoy queda debajo del texto.
- (C) El boletín del Evento 6 como objeto: cinco boletines de papel. La diagonal de «100» se separa y forma una fila.
- (D) Limpieza de comentarios y guías.

## 2. Objetivos, no objetivos, anti-objetivos

**Objetivos**
- (A) va solo antes de `choice_peso` (5 en el Cap. 1). Es del mismo juego, pero distinto de las cortinillas (diagonal), de `hub_completado` (bandas y sello) y de los minijuegos (columna con chibi).
- (B) Texto centrado en vertical, márgenes iguales y la flor sin pisar el texto.
- (C) Matriz legible en papel, sellos de color de hermana y una transición de fase que cuente la historia.
- Label de prueba para la consola en (C).

**No objetivos**
- No se toca `choice_ligera`.
- `hub_completado` no lleva rótulo (decidido).
- No hay sonido nuevo.
- No hay cambios en los 5 archivos de capítulo ni en `02_cap1_evento6.rpy`.

**Anti-objetivos (sería un fracaso aunque funcione)**
- Pulsar una tarjeta antes de que termine de aparecer.
- Que el rótulo se repita entero al volver con rollback.
- Que el boletín muestre afinidad (D-13).
- Que algo del boletín quede bajo la caja de texto.
- Pausas que el guion no tenía.

## 3. Restricciones

- Un clic no adelanta un ATL. Sin `modal` si hay pausa (GUIA_UI §5). En (A) no hay pausa: la propia interacción del menú es la espera.
- Último fotograma animado = estado estático (comprobado por captura, píxel a píxel).
- Los PNG solo salen de `herramientas/generar_ui.py`, nunca a mano.
- Sin ternarios. Todo `show` lleva su posición. Diálogo de ≤ ~100 caracteres.
- Lint con el SDK al final de cada parte. Avisos previos conocidos: `camara.mp3` y las sentencias inalcanzables de `00_definiciones.rpy`.
- No tocar `README.md` ni `CAP1.md`.

## 4. Enfoques considerados

**(B) Tarjetas.**
- *P1 (elegido):* alto por número de líneas, texto centrado y flor al 70 % en la esquina.
- *P2:* flor de tamaño actual anclada junto al texto. Descartado: el pétalo de color tapa palabras (captura `ichika_P2`). Cada hermana tiene su pétalo en otra posición de la flor.
- *Frame de 9 cortes en vez de PNG por alto:* descartado. El texto mide múltiplos exactos de 48 px por línea, así que un PNG por número de líneas ya ajusta sin holgura. La decoración de motivos no se estira bien.

**(C) Boletín.**
- *C1, una sola hoja:* cuenta mejor «un alumno que no existe».
- *C2, cinco tiras (elegido):* cada fila es una persona y la fase 3 sale sola («cinco hojas en fila»). Boceto en `scratchpad/boceto_c2/`.

**(A) Rótulo.** Se buscaba un movimiento que no repitiera los de las otras animaciones: radial, desde el centro (flor que se abre y una línea horizontal). Las otras familias ya usan la diagonal, las bandas y la columna.

## 5. Decisiones del usuario

1. Rótulo «HORA DE DECIDIR», igual para todas. El color es el de la hermana.
2. Sonido: se reusa `cort_mj_<h>_saltado.ogg` (su nota, suave, golpe a 0,25 s).
3. Tarjetas: P1.
4. Boletín: C2.
5. `hub_completado` se queda sin rótulo.

## 6. Diseño

### 6.1 Archivos

| Archivo | Cambio |
|---|---|
| `game/07_ui.rpy` | (A) rótulo, `DEC_RITMOS`, `decision_animar`; (B) `TARJETA_ALTOS`, `ui_altura_items`, `tarjeta_texto`, flor; `screen choice_peso` |
| `herramientas/generar_ui.py` | (B) `TARJETA_ALTOS`; (C) `boletin_papel()` → `ui/boletin_papel.png` |
| `game/ui/` | (B) PNG nuevos 208/256/304/352; se borran los 220/270/320/370 (32 archivos) |
| `game/12_e6_pantallas.rpy` | (C) `screen boletin_cinco` reescrita, transforms, `label boletin_cinco_prueba`; (D) comentario de `sfx_camara` |
| `docs/GUIA_UI.md` | entradas de (A), (B) y (C) |
| `docs/GUIA_AUDIO.md` | `estomago` y `camara` en la tabla de efectos |

### 6.2 (A) «Hora de decidir»

**Cuándo sale.** Al abrir `choice_peso`, `default intro = decision_animar()`. Es False en cada uno de estos casos:
- `renpy.in_rollback()`: rollback o carga de partida. Ya viste la decisión: vuelves a elegir sin ceremonia.
- `decision_saltando`: lo apunta `decision_peso()` con `renpy.is_skipping()`, porque el `menu` corta el modo saltar antes de mostrar la pantalla. Si venías saltando, esta parte ya la habías leído.
- `preferences.transitions == 0`.

Con `intro` en False todo sale **en su estado final, ya pulsable**. La entrada corta de hoy también se omite.

**Línea de tiempo** (`DEC_RITMOS` en `07_ui.rpy`):

| t (s) | Qué |
|---|---|
| 0,00 | velo 0 → 50 % (0,3 s); suena `cort_mj_<h>_saltado` por el canal `cortinilla` (`cort_sonar`) |
| 0,00–0,30 | flor de 5 pétalos al centro de la pantalla: zoom 0,6 → 1,0 y giro −30° → 0, *ease*. Su pétalo en su color; los otros cuatro, blancos al 25 % |
| 0,25–0,60 | línea de 2 px de su color crece desde el centro a izquierda y derecha (`xzoom` 0 → 1, 900 px) bajo la flor |
| 0,35–0,65 | «HORA DE DECIDIR» (`HUD_FUENTE`, 46 px, `kerning` 10, color blanco con contorno de su tinta) sube 12 px y aparece |
| 0,95–1,20 | todo el rótulo sube 30 px, baja al 92 % y se desvanece |
| 0,95–1,35 | la caja de la pregunta entra (el `pregunta_entrada` de hoy, con espera) |
| 0,95 + 0,08·n | tarjeta n entra (0,3 s): la última termina en 1,41 |
| 1,45 | `listo = True`: las tarjetas pasan a pulsables (`sensitive listo`) |

- El rótulo no deja nada en el estado final. Velo, pregunta y tarjetas terminan en alfa 1, desplazamiento 0 y zoom 1: lo mismo que con `intro` en False.
- Los transforms de entrada reciben la espera como parámetro, y con `intro` en False no se aplica ninguno.
- La música no se baja (las campanitas tienen ataque; igual que en los minijuegos).
- `tarjeta_hover` se queda como está.
- También lo hereda el `decision_peso` de la secuencia de prueba de `00_definiciones.rpy:702`. Es aceptable.

### 6.3 (B) Tarjetas

- `TARJETA_ALTOS = [208, 256, 304, 352]` en `07_ui.rpy` y en `generar_ui.py`. Equivale a 2, 3, 4 y 5 líneas × 48 + 2 × 56 de margen.
- `ui_altura_items`: `necesario = mayor + 112`. Devuelve el primer alto ≥ `necesario` (como `int`) o el último. Con 1 línea devuelve 208.
- Las tres tarjetas siguen con el mismo alto.
- `tarjeta_texto`: deja `ypos 52` y pasa a `yalign 0.5`; `xpos 44` y `xsize 432` se quedan.
- La flor sigue en la esquina inferior derecha, a zoom 0,7 (112 px), en (402, alto − 118).
- Medidas reales y su resultado:

| Decisión | Antes | Después | Margen arriba/abajo de la opción más larga |
|---|---|---|---|
| Ichika, Nino, Itsuki (3 líneas) | 270 | 256 | 56 / 56 |
| Miku, Yotsuba (2 líneas) | 220 | 208 | 56 / 56 |

  Las opciones más cortas quedan centradas. Por ejemplo, «Yo sí voy a durar.» queda a 104 / 104.
- Se regeneran los PNG con `python generar_ui.py` y se borran los de los altos viejos tras comprobar que nada los usa (grep).

### 6.4 (C) Boletín: cinco tiras

**Pieza nueva:** `ui/boletin_papel.png`, generado con `generar_ui.py`.
- Papel crema plano `#F6EEDC` con radio 10 y un borde 1 px algo más oscuro, para usar como `Frame` de 9 cortes.
- Sin el degradado gris de `opcion_neutra`: en el boceto, ese degradado lo hacía parecer metal.
- El papel no se tiñe. El color de la hermana va en la franja, la flor y el sello.

**Composición, fases 1 y 2.** Todo cabe en y ≤ 730; la caja de texto empieza en 804.
- «LA CUENTA» se queda (`ypos 56`).
- Cabeceras de columna, por materia: icono `hud_icono_<m>` en su color, encima del nombre de la materia. Van centradas en las columnas, en y ≈ 140–205.
- Cinco tiras de 1340 × 84, en x = 290 (el mismo ancho que la caja de diálogo, alineadas con ella) y y = 226 + i·104. Cada tira lleva:
  - una sombra (negro al 35 %, desplazada 4 px);
  - una franja de 12 px de su color a la izquierda;
  - `flor.png` en su color y su nombre en tinta `#3A2A55`.
- Columnas: centros 720, 920, 1120, 1320 y 1520 (zona de nombre 290–620).
- Las 25 notas comparten fuente (`gui.text_font`), tamaño 40, color tinta y centrado vertical. Se arregla el desajuste de hoy, y la diagonal no se delata en la fase 1.

**Fase 1 → 2** («Esa diagonal lo delata»):
- Las notas fuera de la diagonal pasan a lápiz: alfa 0,45 en 0,6 s. Siguen legibles.
- En cada «100», un sello en orden de fila, con 0,12 s entre uno y otro:
  - doble aro de su color (dos `hub_aro`, uno a −8°);
  - disco `hub_sello_fondo` al 15 %, como tinta;
  - golpe: zoom 1,5 → 1,0 y alfa 0 → 1 en 0,22 s;
  - el «100» cambia a su tinta oscura (`ui_mezclar(color, negro, 0,45)`) con un fundido cruzado.
- Sin sonido.

**Fase 2 → 3** («Existe, pero repartido…»):
- Las tiras y las cabeceras bajan 20 px y se desvanecen (0,5 s).
- Cada sello con su «100» viaja de su celda (columna i, fila i) al centro de su hoja (0,7 s, *ease*, 0,06 s entre uno y otro) y crece hasta el tamaño de la hoja.
- Después aparece la hoja detrás (0,4 s) y luego el icono, la materia y la flor.
- Hojas: 5 de 250 × 380, separadas 50, centradas (x₀ = 235), y = 190. Cada una lleva:
  - el papel;
  - una franja superior de su color;
  - el icono;
  - el sello grande con «100» (80 px);
  - la materia (30 px);
  - una flor pequeña que **no** pisa la materia (en el boceto la pisaba).

**Mecánica.**
- Los cambios de fase siguen siendo `$ e6_boletin_fase = n` del guion: sin pausas, la animación corre bajo el texto.
- Cada grupo vive en un `showif` con eventos:
  - `appear`: sale ya en su estado final, para cargar una partida a mitad de escena;
  - `show`: anima;
  - `hide`: desvanece.
- El sello viajero es la versión «fila» que entra con `on show` desde las coordenadas de su celda. La versión «celda» se oculta al instante, así que el empalme no se ve.
- Rollback de la fase 3 a la 2: la fase 2 vuelve a entrar con su animación. Es aceptable y no duplica nada.
- La pantalla sigue en `zorder -5` y solo lee `e6_notas`, `E6_ORDEN_EXAMEN` y `E6_MATERIA`.

**Prueba.** `label boletin_cinco_prueba` en `12_e6_pantallas.rpy`, lanzable desde la consola:
1. `quick_menu = False`, `scene` con fondo y notas de ejemplo que cumplen I1/I2 (fuera de la diagonal entre 60 y 89, diagonal en 100).
2. Las tres fases con líneas cortas de `mc_pensamiento`.
3. `hide screen` y restaurar `quick_menu`.

### 6.5 (D) Limpieza

- `12_e6_pantallas.rpy` línea 8: quitar «[NUEVO]» y la frase «el guion lo reproduce solo si existe», que ya es falsa.
- `GUIA_AUDIO.md` §4: filas `sfx_estomago` (beat de Itsuki, 3,6 s) y `sfx_camara` (Evento 6, 0,6 s), con origen por confirmar si no consta. Antes hay que comprobar con grep que esos `define` existen con esos nombres.
- `GUIA_UI.md` §4: tres entradas nuevas («Hora de decidir», «Tarjetas de decisión», «Boletín del Evento 6») con el formato de `hub_completado` y de la barra de progreso. Se actualiza `TARJETA_ALTOS` en §3.

### 6.6 Verificación

- Capturas de antes y después de cada parte.
- (A): fotograma final animado = estado con `intro` en False, píxel a píxel, en las 5 hermanas.
- (C): fase 3 a la que se llega animando = fase 3 cargada directa.
- Revisión con `impeccable` antes de cerrar.
- Lint al final de cada parte.
- Ojo con el arnés de capturas: `run --warp` deja `renpy.game.after_rollback = True`, y (A) creería que viene de un rollback. El arnés hace una pausa antes de abrir la primera decisión, o pone esa variable a False.
- `default decision_saltando = False` junto a las demás variables de decisión.

## 7. Lo que queda al constructor

- Curvas de *ease* exactas y los últimos píxeles de las cabeceras y de la flor de las hojas, a ojo sobre captura.
- El nombre interno de los transforms nuevos.
- Si la sombra de las tiras es una capa de `Solid` o parte del PNG de papel.
