# Marco común de minijuegos — Plan de implementación

> **Para agentes:** sub-skill requerido: superpowers:executing-plans (o subagent-driven-development). Pasos con casillas `- [ ]`.

**Objetivo:** un solo marco visual para los cinco minijuegos del Evento 6: la columna de la hermana a la izquierda (cinta, HUD, globo y chibi a 1.0), un área de juego rectangular a la derecha y una franja fija para los avisos.

**Arquitectura:** se amplía `screen mj_marco`. Los argumentos posicionales actuales no cambian, para que los cinco minijuegos sigan cargando, y se añaden argumentos nuevos con valor por defecto. `mj_retrato`, `mj_globo` y `cinta_boton` se reutilizan con estados y movimiento nuevos. El fondo de la columna sale de `menu_panel()` en `generar_ui.py`, con parámetros. Los minijuegos **no se tocan**: cada sesión adapta el suyo siguiendo `MARCO_COMUN.md`.

**Tecnología:** Ren'Py 8.5.3 (screen language, ATL), Python 3 + Pillow para `generar_ui.py`.

**Spec:** la dirección «A · Columna de la hermana» aprobada en la conversación del 14/11/2026. Se resume en la sección «Diseño».

## Diseño (lo que se decidió)

Pantalla de 1920×1080. Medidas en px.

| Zona | Dónde | Contenido |
|---|---|---|
| Columna | x 0–400. Borde inclinado: relleno hasta x 380 arriba y x 360 abajo; banda de su color a +6 px | Cinta (ypos 22), HUD (x 40, y 116, 320 de ancho), globo y chibi |
| Área de juego | x 440–1880, y 112–952 (1440×840); centro x **1160** | Lo dibuja cada minijuego |
| Franja de avisos | centrada en x 1160, y 1012; ancho máx. 1200 | `mj_aviso` |
| Chibi general | x 180, borde inferior del PNG en y 1090 (pies en 1074), zoom 1.0 | Ocupa x 49–311 (la más ancha, Nino, 261 px) |
| Globo | ancho máx. 300, centrado en x 180, punta a 12 px sobre la coronilla más alta (fila 10 del PNG, lazo de Yotsuba) → borde inferior del globo en y 559 | 3 líneas de 28 → arriba ≈ 400 |

**Orden del HUD** (de arriba abajo): cinta del título → `INTENTO n` (+ `ASISTENCIA` si el nivel es asistida) → vidas (iconos de su motivo, `hud_icono_<h>.png` a 0,8) → recurso (barra, «TIEMPO» por defecto) → progreso (etiqueta de la unidad + «7 / 28» + barra de su color). **Un solo contador de progreso.** Se quita «FALLIDOS», porque siempre vale intento − 1.

**Tipografía:** dos familias.
- Shippori Mincho B1 (`gui.name_text_font`): mayúsculas, cifras y botones.
- M PLUS Rounded (fuente por defecto): frases.
- Klee One queda solo como contenido dentro del cuaderno de Itsuki.

Escala (un estilo por nivel):

| Estilo | Familia | Tamaño | Uso |
|---|---|---|---|
| `mj_titulo` | Shippori, kerning 4 | 40 | título de la intro |
| `mj_cifra_grande` | Shippori | 120 | cuenta atrás |
| `mj_cifra` | Shippori | 30 | cifras del HUD |
| `mj_etiqueta` | Shippori, kerning 3 | 20 | etiquetas en mayúsculas |
| `mj_aviso_texto` | M PLUS | 34 | avisos |
| `mj_globo_texto` | M PLUS | 28 | globo |
| `mj_cuerpo` | M PLUS | 24 | reglas e instrucciones |
| `mj_nota` | M PLUS | 18 | pistas pequeñas |

Botones (`cinta_boton`, Shippori): primario 420×80 a 34, secundario 340×64 a 26, pequeño 220×56 a 24.

**Avisos:** un solo estilo de píldora (`opcion_neutra` teñida `#1B1026` + `opcion_marco` teñido del acento). Acentos: `bien` `#9AE6B4`, `mal` `#FF8A8A`, `info` color de la hermana. Entra en 0,2 s (alpha + yoffset 14→0) y sale en 0,25 s.

**Botones:** estados normal / hover / pulsado / deshabilitado.
- Ren'Py no tiene estado «pulsado»: `Button` solo emite hover, idle e insensitive (comprobado en `renpy/display/behavior.py`).
- Se simula así: al hacer clic, la cinta se rellena con el color de la hermana durante 0,14 s, mediante `SetLocalVariable` + `timer`.
- Deshabilitado: relleno `#2A2236`, borde `#6E6680`, texto `#8F8AA0` (los grises que ya usa Ichika).

**Movimiento:** nada en bucle en el marco.
- La chibi general se queda quieta; «salto» y «tiembla» pasan a ser una sola reacción de 0,32 s y 0,25 s.
- El globo entra en 0,18 s y sale en 0,2 s.
- La cinta entra en 0,35 s.
- `mj_chibi_bob`, `mj_chibi_salto` y `mj_chibi_tiembla` (los bucles) siguen existiendo para las corredoras del relevo, que son contenido del juego.

**Velo:** `#0B0712B8` → `#0B0712A6`, porque el fondo apenas se veía. Se ajusta con la pasada de pulido.

## Restricciones globales

- No se toca la lógica de ningún minijuego, ni `MJ_PARAMS`, ni `10_mj_<h>.rpy`.
- Los argumentos posicionales de `mj_marco`, `mj_retrato` y `cinta_boton` no cambian de orden ni de nombre: los cinco minijuegos y los menús del sistema tienen que seguir pasando el lint sin cambios.
- Todo botón nuevo lleva `hover_sound audio.sfx_hover` y `activate_sound audio.sfx_click`.
- Todo `add`/`text` del marco lleva su posición. Las x/y son enteros.
- Código completo, sin ternarios.
- No se tocan README.md ni los .md existentes.
- Commits: solo si el usuario los pide.

## Puntos de revisión

1. **El globo más largo** («Me sé el guion. Falta saber cuál es el mío.», Ichika) no debe pisar el HUD: su borde superior debe quedar ≥ y 380. Se comprueba en la captura de Ichika.
2. **9 vidas** (testigos de Yotsuba en asistida) caben en una fila de 340 px. Se comprueba en la captura de Yotsuba.
3. **El título más largo** («CADENA DE CONVERSIONES») sale de la columna por la cinta, pero termina por encima de y 86 < 112. Se comprueba en la captura de Itsuki.
4. **Menús del sistema:** las cintas de Opciones siguen encendiéndose al estar seleccionadas tras el cambio de `cinta_boton`. Se comprueba abriendo Opciones.
5. **Aviso largo** (más de 1200 px) se parte en dos líneas dentro de la píldora, sin salirse. Se comprueba en la pantalla de prueba.

---

### Tarea 1: Fondo de la columna en `generar_ui.py`

**Archivos:**
- Modificar: `The Fifth Choice/herramientas/generar_ui.py` (`menu_panel()` ~l. 495; `__main__` ~l. 676)
- Crear (generados): `The Fifth Choice/game/ui/mj_columna.png`, `The Fifth Choice/game/ui/mj_columna_banda.png`

**Produce:** `ui/mj_columna.png` (400×1080, relleno con sakuras y sin bandas) y `ui/mj_columna_banda.png` (400×1080, una banda blanca para teñir).

- [ ] Cambiar la firma a `menu_panel(ancho=860, sup=780, inf=650, relleno=True, colores=None)`. Con `colores is None` usa `COLORES_HERMANAS`. Con `relleno=False` no dibuja el degradado ni las sakuras. `menu_panel.png` tiene que salir **idéntico** a antes.
- [ ] Añadir arriba la constante `MJ_COLUMNA = (400, 380, 360)  # ancho, borde arriba, borde abajo — coincide con MJ_AREA_X = 440 en 10_minijuegos.rpy`, y en `__main__`:
  `guardar(menu_panel(*MJ_COLUMNA, True, []), "mj_columna.png")` y `guardar(menu_panel(*MJ_COLUMNA, False, [(255, 255, 255)]), "mj_columna_banda.png")`.
- [ ] Generar solo los dos PNG nuevos y el panel de control, sin regenerar todo `game/ui/`:
  `cd "The Fifth Choice/herramientas" && python -c "import generar_ui as g; g.guardar(g.menu_panel(*g.MJ_COLUMNA, True, []), 'mj_columna.png'); g.guardar(g.menu_panel(*g.MJ_COLUMNA, False, [(255,255,255)]), 'mj_columna_banda.png'); g.guardar(g.menu_panel(), r'<scratchpad>\menu_panel_control.png')"` (el tercero va al scratchpad con ruta absoluta; `guardar` usa `os.path.join`, que respeta las rutas absolutas).
  Esperado: `menu_panel.png` y el del scratchpad son idénticos byte a byte (`cmp`), y los dos PNG nuevos miden 400×1080.
- [ ] Mirar los dos PNG (Read). La banda sigue el borde inclinado.

### Tarea 2: Constantes y estilos del marco

**Archivos:** Modificar `The Fifth Choice/game/10_minijuegos.rpy`, al principio de la Parte E.

**Produce:** `MJ_AREA_X=440`, `MJ_AREA_Y=112`, `MJ_AREA_W=1440`, `MJ_AREA_H=840`, `MJ_AREA_CX=1160`, `MJ_AVISO_Y=1012`, `MJ_AVISO_ANCHO=1200`, `MJ_HUD_X=40`, `MJ_HUD_Y=116`, `MJ_HUD_ANCHO=320`, `MJ_VELO="#0B0712A6"`, `MJ_BOTON={"primario": (420, 80, 34), "secundario": (340, 64, 26), "pequeno": (220, 56, 24)}`, `MJ_AVISO_ACENTO={"bien": "#9AE6B4", "mal": "#FF8A8A"}` y los estilos `mj_titulo`, `mj_cifra_grande`, `mj_cifra`, `mj_etiqueta`, `mj_aviso_texto`, `mj_globo_texto`, `mj_cuerpo`, `mj_nota` con los valores de la tabla de Diseño. Contorno `[(3, "#1B102699", 0, 0)]` en `mj_cifra`, `mj_cifra_grande`, `mj_etiqueta`, `mj_cuerpo` y `mj_nota`. Colores: título `#FFF8FC`, cifra `#FFFFFF`, etiqueta `#E8E0F2`, aviso `#F3EEFA`, cuerpo `#E8E0F2`, nota `#CFC6E0`.

- [ ] Escribir los `define` y los `style`.
- [ ] Lint: `"/c/Users/PERSONAL/Desktop/renpy-8.5.3-sdk/renpy.exe" "The Fifth Choice" lint`. Esperado: sin errores nuevos. Avisos previos conocidos: `camara.mp3` y las sentencias inalcanzables de `00_definiciones.rpy`.

### Tarea 3: `cinta_boton` con deshabilitado y pulsado

**Archivos:** Modificar `The Fifth Choice/game/09_menus_sistema.rpy:81-113`.

**Interfaz:** `screen cinta_boton(texto, accion, clave, ancho=420, alto=58, tam=26, activo=True)`. Las 21 llamadas existentes no cambian.

- [ ] `default pulsado = False`; `action [SetLocalVariable("pulsado", True), accion]`; `selected renpy.is_selected(accion)`; `sensitive (activo and renpy.is_sensitive(accion))`.
- [ ] Mientras `pulsado` es True, `background` e `hover_background` usan el mismo `Fixed` que `selected_background` (relleno de su color + borde blanco). `if pulsado: timer 0.14 action SetLocalVariable("pulsado", False)`.
- [ ] `insensitive_background`: relleno `#2A2236` (alpha 0.8) + borde `#6E6680`. `insensitive_color "#8F8AA0"` en el texto.
- [ ] Lint limpio. Comprobación manual del punto 4: abrir Opciones en el juego. Las cintas activas siguen llenas y el clic hace el destello.

### Tarea 4: Chibi general y globo (`10_mj_chibi.rpy`)

**Archivos:** Modificar `The Fifth Choice/game/10_mj_chibi.rpy` (transforms l. 244-273, screens l. 297-331).

**Produce:**
- `define MJ_CHIBI_X = 180`, `MJ_CHIBI_Y = 1090`, `MJ_GLOBO_ANCHO = 300`, `MJ_GLOBO_HUECO = 12`.
- `screen mj_retrato(hermana, expresion, globo, anim="quieto", x=MJ_CHIBI_X, y=MJ_CHIBI_Y, zoom=1.0)`.
- `screen mj_globo(texto, hermana, x, y, ancho=MJ_GLOBO_ANCHO)`, donde (x, y) sigue siendo la punta.

- [ ] Transforms nuevos de una sola pasada: `mj_chibi_salto_uno` (ease 0.15 → yoffset −26, ease 0.17 → 0) y `mj_chibi_tiembla_uno` (5 tramos lineales de 0,05 s: −6, 6, −4, 4, 0). Los transforms en bucle no se tocan.
- [ ] `mj_globo_entra` pasa a eventos: `on appear, show:` alpha 0 / yoffset 8 → `ease 0.18` alpha 1 / yoffset 0; `on hide:` `ease 0.2 alpha 0.0`. Sin zoom (en un `fixed` a pantalla completa desplazaría el globo).
- [ ] `mj_retrato` dibuja la chibi él mismo, sin `use mj_chibi_vista`:
  - `anim == "salto"` → `mj_chibi_salto_uno`
  - `"tiembla"` → `mj_chibi_tiembla_uno`
  - cualquier otro valor («bob», «quieto») → sin transform

  Ancla (0.5, 1.0) en (x, y). Punta del globo: `y - int(502 * zoom) - MJ_GLOBO_HUECO`.
- [ ] El globo va en `showif globo.visible():` con **un solo hijo**: un `fixed` con `at mj_globo_entra` que contiene el `frame` y el rombo. Motivo: `Container` no pasa show/hide a sus hijos (`config.containers_pass_transform_events` solo incluye hover, idle e insensitive). El borde inferior del frame va a punta − 17 y el rombo se centra ahí. Texto con `style "mj_globo_texto"` y `color tinta`.
- [ ] Lint limpio.

### Tarea 5: `mj_marco` en columna + `mj_aviso`

**Archivos:** Modificar `The Fifth Choice/game/10_minijuegos.rpy:557-621` (screen `mj_marco`).

**Consume:** Tareas 1–4.

**Interfaz:**
```
screen mj_marco(hermana, titulo, intento=1, fallos=0, nivel="dificil", progreso=0, total=1,
                tiempo=None, tiempo_total=None, unidad="ACIERTOS",
                recurso_txt="TIEMPO", vidas=None, vidas_max=0, vidas_txt="",
                chibi=None, globo=None, anim="quieto",
                aviso="", aviso_tipo="info", aviso_on=None)
screen mj_aviso(texto, tipo, hermana)
transform mj_cinta_entrada      ## xoffset -800 → ease 0.35 xoffset 0
transform mj_aviso_anim         ## on appear, show / on hide (valores de Diseño)
```
`fallos` se mantiene por compatibilidad y no se dibuja. `aviso_on=None` significa «visible si `aviso != ""`». Los minijuegos que tengan temporizador pasan `aviso_on=(vivo.aviso_t > 0.0)`, para que el texto siga ahí mientras se desvanece.

- [ ] Orden de dibujo:
  1. `key` (los mismos de ahora)
  2. `Solid(MJ_VELO)`
  3. `ui/mj_columna.png` en (0, 0)
  4. `ui/mj_columna_banda.png` teñida con su color en (0, 0)
  5. cinta (`hud_cinta_vista(..., mj_cinta_entrada)`)
  6. bloque del HUD (`vbox` en MJ_HUD_X / MJ_HUD_Y, spacing 14)
  7. `transclude`
  8. `if chibi is not None: use mj_retrato(hermana, chibi, globo, anim)`
  9. `showif` del aviso → `use mj_aviso`

  Se quita `flor_sakura`, porque la columna ya lleva la marca.
- [ ] HUD:
  - `INTENTO` (`mj_etiqueta`) + número (`mj_cifra`); debajo, `ASISTENCIA` en `#FFE3A0` si `nivel == "asistida"`.
  - Vidas: si `vidas is not None`, etiqueta `vidas_txt` + `hbox spacing 4` de `vidas_max` iconos `ui/hud_icono_<h>.png` a zoom 0.8. Los vivos con TintMatrix de su color y los perdidos en `#FFFFFF` con alpha 0.2.
  - Recurso: si hay `tiempo`, etiqueta `recurso_txt` + `barra_progreso(tiempo, tiempo_total, col, 320)`, con `col` `#FFE3A0`, o `#FF8A8A` si `tiempo < 0.25 * tiempo_total`.
  - Progreso: etiqueta `unidad` + cifra `"{} / {}"` + `barra_progreso(progreso, total, color, 320)`.
- [ ] `mj_aviso`: `frame` con xpos MJ_AREA_CX, ypos MJ_AVISO_Y, ancla (0.5, 0.5), `xmaximum MJ_AVISO_ANCHO`, padding (40, 14, 40, 14), `at mj_aviso_anim`, fondo de píldora con su acento, `text` con `style "mj_aviso_texto"`, `text_align 0.5` y `substitute False`.
- [ ] Lint limpio. Los cinco minijuegos siguen compilando sin cambios. Lo esperado hasta su sesión: el contenido que tienen en x < 440 queda debajo o encima de la columna.

### Tarea 6: Pantalla y label de prueba + capturas

**Archivos:**
- Modificar `The Fifth Choice/game/10_minijuegos.rpy`: Parte F nueva al final, más los ajustes de `mj_prueba` (l. 625-676).
- Crear y luego borrar: `The Fifth Choice/game/zz_capturas_tmp.rpy`.

**Produce:** `label mj_probar_marco` (menú: las cinco hermanas, «Las cinco seguidas» y «Volver») y `screen mj_marco_prueba(hermana)`.

- [ ] `mj_marco_prueba(hermana)`:
  - `modal True`, `zorder 95`, fondo `bg_negro`.
  - Título sacado de `MJ_REGISTRO[E6_MJ_JUEGO[hermana]]["titulo"]`.
  - Intento 2, nivel «asistida», vidas 3 de 9 («TESTIGOS»), tiempo 20/80, progreso 7/28 («TRAMOS»).
  - `default g = MJGlobo(hermana)` + `timer 0.05 repeat True action Function(g.avanzar, 0.05)`.
  - Rectángulo del área dibujado con 4 `Solid` de 2 px en `#FFFFFF40`.
  - Dentro del área, `cinta_boton` para: «Aviso bien», «Aviso fallo», «Aviso info», «Aviso largo» (> 1200 px), «Globo largo» (`g.poner(...)` con la línea de Ichika del punto 1), «Salto», «Tiembla», uno deshabilitado (`activo=False`) y «Siguiente» (`Return()`).
- [ ] `mj_prueba`: sus `xalign 0.5` pasan a `xpos MJ_AREA_CX xanchor 0.5`; el «¡Bien!/Fallo» pasa a `aviso`; el botón usa `MJ_BOTON["primario"]`. Su mecánica no cambia.
- [ ] Capturas: en `zz_capturas_tmp.rpy`, un label que, para cada hermana, haga `show screen mj_marco_prueba(h)` con el globo largo y un aviso puestos, `pause 0.8`, `$ renpy.screenshot(r"<scratchpad>\mj_marco_<h>.png")`, y al final `$ renpy.quit()`. Lanzarlo con `renpy.exe "The Fifth Choice" run --warp game/zz_capturas_tmp.rpy:<línea del label>`. Si el warp falla, pedir al usuario que juegue `mj_probar_marco` y haga las capturas.
- [ ] Mirar las cinco capturas y comprobar los puntos 1, 2, 3 y 5. Borrar `zz_capturas_tmp.rpy` y su `.rpyc`.
- [ ] Lint limpio.

### Tarea 7: Pasada de pulido (Impeccable polish, en Ren'Py)

- [ ] Con las capturas: alineación del HUD con la cinta, separación entre el globo y el HUD, contraste de la etiqueta sobre la columna, opacidad del velo, grosor de la banda y la entrada del aviso. Arreglar lo que salga en las capturas, repetir las capturas una vez y lint.

### Tarea 8: `docs/MINIJUEGOS/MARCO_COMUN.md` + memoria

- [ ] Escribir el .md a partir del **código final**: zonas y medidas, firmas de `mj_marco` / `mj_retrato` / `cinta_boton` / `mj_aviso`, estilos, colores, botones, movimiento, cómo probar, y la lista por minijuego de abajo, revisada contra el código.
- [ ] Guardar en claude-mem un resumen con las medidas finales.

**Lista por minijuego para `MARCO_COMUN.md` (borrador):**
- **Todos:**
  - Quitar su `use mj_retrato(..., 250, 1090, 1.0)` y pasar `chibi=`, `globo=` y `anim=` a `mj_marco`.
  - Avisos → `aviso=`, `aviso_tipo=` y `aviso_on=`.
  - Textos sueltos → estilos `mj_*`.
  - Botones principales → `MJ_BOTON`.
  - Paneles de intro centrados en `MJ_AREA_CX`, no en 960.
- **Yotsuba (y2):**
  - Testigos → `vidas=`.
  - Quitar «TRAMO n/N», «VUELTA · nivel» y el «28» fijo de la meta (**bug**: con 14 o 56 tramos sigue diciendo 28; también las 28 marcas fijas).
  - Aviso de la pista → `aviso`.
  - `Y2_CENTRO` 1180 → `MJ_AREA_CX`.
  - Su propio `mj_retrato` (pies en 830) desaparece.
  - El `fixed at mj_chibi_tiembla` (bucle sobre toda la pantalla) → reacción de una sola pasada.
  - Decidir si el `y2_pulso` de la MARCA se queda (es mecánica).
- **Nino (n1):**
  - Lista (x 60–600) + estantes (1210 px desde x 650) no caben en 1440: hay que rehacer la distribución.
  - Cronómetro grande y barra de tiempo del marco → uno solo.
  - Popup (1130, 80) → `aviso`.
  - Destello rojo a pantalla completa → solo en el área.
  - Cuenta atrás de 220 → `mj_cifra_grande`.
- **Miku (m3):**
  - CONCENTRACIÓN → `tiempo` / `recurso_txt` (o vidas). Mover PERFECTOS y el patrón del compás (x 70) al área.
  - Carriles centrados en 960 → `MJ_AREA_CX`.
  - Feedback a y 650: decidir entre `aviso` o una excepción junto a los carriles.
  - Los carriles no tienen sonidos (decidir).
- **Ichika (i1):**
  - Barras MÁSCARA/ENERGÍA y tarjetas → recentrar en el área.
  - Mensaje a y 865 → `aviso`.
  - Cambios de cifras en (1320, 545): revisar.
  - «EL PAPEL» no tiene `activate_sound`.
- **Itsuki (it1):**
  - «Tu hoja» y el título en x 320 → ≥ 440.
  - Avisos y pista del profesor → `aviso`.
  - «Sin ayuda» → `cinta_boton(..., activo=False)`.
  - `it1_fila` no tiene `activate_sound`.
  - Klee One se queda en el cuaderno.
