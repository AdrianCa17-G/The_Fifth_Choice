# N1′ «Compras para seis» · Corrección del lag — Plan de implementación

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Que la cinta de N1′ se mueva fluida en los tres niveles (sobre todo en difícil, deriva 140) sin cambiar la mecánica.

**Architecture:** Hoy cada tick del `timer 0.033` reevalúa y redibuja la screen entera (fotogramas = ticks: 15 fps en difícil). La corrección separa movimiento y lógica: la cinta se desplaza con un transform ATL por fila (el motor la anima en cada fotograma sin reevaluar la screen); el timer sigue llevando la lógica pero solo reinicia la interacción cuando cambia algo visible; y los fondos de las cajas se construyen una vez por estado y color, para que Ren'Py reutilice las cajas al reevaluar.

**Tech Stack:** Ren'Py 8.5.3 (screen language 2, ATL), `game/10_mj_nino.rpy`.

**Spec:** el mensaje de la tarea (PARTE 1 · LAG) + el diagnóstico de la sesión (cifras «antes» abajo).

## Global Constraints

- La MECÁNICA no cambia: mismos `MJ_PARAMS["n1"]`, misma velocidad por fila `deriva * (1 + 0.15 * fi)`, mismo sentido (filas pares →, impares ←), misma penalización, memoria, «mirar», traducción con retardo y racha.
- Código completo, sin ternarios. Botones con `hover_sound audio.sfx_hover` y `activate_sound audio.sfx_click`.
- La distribución (Parte 2) no se toca aquí: las posiciones siguen siendo las actuales; todo lo nuevo usa `N1_VENTANA_W`, `N1_CAJA_W`, `N1_CAJA_H` para que la Parte 2 solo cambie constantes.
- No se toca el marco (`10_minijuegos.rpy`) ni `generar_ui.py`.

## Cifras «antes» (ventana 1536×864, gl2, AMD Radeon integrada, vsync 60)

| | asistida | media | difícil |
|---|---|---|---|
| fps | 22,6 | 18,9 | 15,1 |
| ms/fotograma media · p95 · máx | 44 · 52 · 139 | 53 · 59 · 70 | 66 · 77 · 113 |
| salto de la fila más rápida | — | 3,8 px | 13,7 px |

**Objetivo de «después» en difícil:** ≥ 55 fps de media; salto de la cinta ≤ 4 px por fotograma; tirones (máx.) reportados tal cual.

## Decisiones

1. **La cinta no se congela** en la pausa de 0,7 s entre listas ni en «perdiendo» (hoy `t_deriva` se para). Congelarla obligaría a reiniciar el ATL. Si el usuario lo quiere, se decide en la revisión.
2. **La fase inicial de la cinta** pasa a ser la de cuando aparece la fila (hoy lo es igual: `t_deriva` empieza en 0).
3. **`t_deriva` y `cajas_fila()` desaparecen**; los sustituyen `fila_base()` y `fila_mov()`.
4. **El cronómetro grande muestra décimas** («%.1f») y obliga a redibujar 10 veces por segundo. Se mantiene en la Parte 1 porque es distribución; la Parte 2 lo quita (un solo cronómetro, el del marco) y la firma pasará a medios segundos. Se mide aquí y otra vez al final.
5. **El latido rojo de urgencia** (hoy `sin()` evaluado en cada tick) pasa a un ATL en bucle, y **el destello de error** a un ATL de una pasada. Es el mismo aspecto, sin redibujar la screen. En la Parte 2 se limitan al área.

## Review Focus

1. Clic sobre una caja en movimiento: tiene que elegir esa caja (no la que había antes en esa posición). → Task 4, comprobación de rectángulos de foco.
2. Caja en estado «mal»: sigue sin poder pulsarse ni recibir hover mientras se mueve. → Task 4.
3. Al reevaluar la screen (acierto, error, aviso), la cinta **no** salta al inicio: el ATL conserva su fase. → Task 4, continuidad de posición.
4. Cambio de lista (`entrar_lista`): las cajas nuevas aparecen y las de la lista anterior no quedan pegadas en la cinta. → Task 4, captura tras forzar `elegir` de toda la lista.
5. La traducción con retardo sigue apareciendo (fundido de 0,4 s) aunque la screen ya no se redibuje en cada tick. → Task 3, la firma incluye el alpha cuantizado.

---

### Task 1: Fondos de caja cacheados

**Files:**
- Modify: `The Fifth Choice/game/10_mj_nino.rpy` (bloque `init python`, `screen mj_n1_caja`)

**Interfaces:**
- Produces: `n1_fondo(relleno, borde) -> Fixed`. Devuelve siempre **el mismo objeto** para el mismo par de colores (caché en el dict de módulo `N1_FONDOS = {}`, clave `(relleno, borde)`). Contenido: el mismo `Fixed(Transform(Frame("ui/opcion_neutra.png", 40,40,40,40), matrixcolor=TintMatrix(relleno)), Transform(Frame("ui/opcion_marco.png", 40,40,40,40), matrixcolor=TintMatrix(borde)))` de hoy.

- [ ] **Step 1:** Añadir `N1_FONDOS` y `n1_fondo()` en el `init python` de `10_mj_nino.rpy`.
- [ ] **Step 2:** En `mj_n1_caja`, `background n1_fondo(fondo, borde)` y `hover_background n1_fondo(hover, "#FFFFFF")`. Los colores por estado no cambian.
- [ ] **Step 3:** Lint (`renpy.exe "The Fifth Choice" lint`): sin errores nuevos.

### Task 2: Cinta con ATL

**Files:**
- Modify: `The Fifth Choice/game/10_mj_nino.rpy` (clase `MJN1`, transforms, bloque «Estantes» de `screen mj_n1`)

**Interfaces:**
- Produces:
  - `MJN1.fila_base(fi) -> [(clave, x_int), ...]`. Posición base `x = k * paso + centro`, con `paso = N1_VENTANA_W / n` y `centro = (paso - N1_CAJA_W) / 2`. Con `deriva > 0` añade una copia de cada caja en `x - sentido * N1_VENTANA_W`, para que el bucle no tenga corte. Con `deriva == 0`, solo las n cajas.
  - `MJN1.fila_mov(fi) -> (dx, dur)`: `dx = sentido * N1_VENTANA_W` y `dur = N1_VENTANA_W / (deriva * (1 + 0.15 * fi))`. Con `deriva == 0` devuelve `(0, 0.0)`.
  - `transform n1_cinta(dx, dur)`: `xoffset 0`, `linear dur xoffset dx`, `repeat`.

- [ ] **Step 1:** Sustituir `cajas_fila()` por `fila_base()` y `fila_mov()`. Quitar `t_deriva` de `__init__` y de `tick`.
- [ ] **Step 2:** En la screen, dentro del `fixed` con `clipping True` de cada fila, un `fixed` de `xysize (N1_VENTANA_W, 150)` con `at n1_cinta(dx, dur)` cuando `dur > 0`, y las cajas de `fila_base(fi)` a su `xpos` base. Sin deriva, el mismo `fixed` sin transform. La etiqueta «ESTANTE A >>>» queda fuera del `fixed` que se mueve.
- [ ] **Step 3:** Lint sin errores nuevos.

### Task 3: El timer solo reinicia cuando cambia algo visible

**Files:**
- Modify: `The Fifth Choice/game/10_mj_nino.rpy` (clase `MJN1`, transforms, `screen mj_n1`)

**Interfaces:**
- Consumes: `fila_mov` (Task 2).
- Produces:
  - `MJN1.firma() -> tuple`, con: `fase`, `cuenta_n()`, `int(restante() * 10)` (décimas del cronómetro grande; véase la decisión 4), `racha`, `lista_visible()`, `int(memoria_restante() * 4)`, `mirada_t > 0`, `int(trad_alpha() * 8)`, `int(popup_t * 10)` mientras `popup_t > 0`, `flash_t > 0`, `humor`, `globo.texto`, `globo.visible()`, `tension()`, `len(encontrados)`, `len(malos)`, `idx`, `sexto`.
  - `MJN1.firma_prev` (en `__init__`: `None`).
  - Al final de `tick()`, por **cualquier** camino de retorno: si `firma() != firma_prev`, se guarda y se llama a `renpy.restart_interaction()`. El valor de retorno de `tick()` (el dict de resultado) no cambia.
  - `transform n1_latido`: alpha 0.05 → 0.15 → 0.05 con `ease` de 0,52 s cada tramo, `repeat` (el mismo periodo que hoy da `sin(t*6)`).
  - `transform n1_destello`: alpha 0.30 → 0.0, `linear 0.35`.

- [ ] **Step 1:** En la screen, `timer 0.033 repeat True action Function(vivo.tick, _update_screens=False)`.
- [ ] **Step 2:** Añadir `firma()` y `firma_prev`. Reestructurar `tick()` en `_tick()` (el cuerpo actual) más un `tick()` que llama a `_tick()`, compara la firma y devuelve lo que devolvió `_tick()`.
- [ ] **Step 3:** El latido de urgencia pasa a `add Solid("#FF2D2D") at n1_latido` y el destello a `add Solid("#FF3B3B") at n1_destello` (dentro de `if vivo.flash_t > 0.0`). Se quita `pulso()` si nadie más lo usa (grep).
- [ ] **Step 4:** Las acciones de los botones (`elegir`, `mirar`, `empezar`, `elegir_sexto`) siguen con `Function(...)` normal, que reinicia al hacer clic. No hace falta tocarlas.
- [ ] **Step 5:** Lint sin errores nuevos.

### Task 4: Medir de nuevo y comprobar los clics

**Files:**
- Modify (temporal): `The Fifth Choice/game/zz_medir_tmp.rpy`

- [ ] **Step 1:** Ejecutar el arnés en los tres niveles (`ZZ_NIVEL=<nivel> renpy.exe "The Fifth Choice" run --warp game/zz_medir_tmp.rpy:3`). El arnés pasa a contar «reinicios de interacción» en vez de «ticks», y el salto por fotograma se calcula con los fotogramas reales.
- [ ] **Step 2:** Añadir al arnés la comprobación de foco. A los 4,0 s y a los 4,5 s, leer `renpy.display.focus.focus_list` y localizar el botón de una caja concreta de la fila más rápida. Esperado: su `x` avanza `vel * 0,5 s ± 15 px` en el sentido de la fila (cinta en movimiento con foco correcto, Review Focus 1). Después, `vivo.elegir(<una caja que no está en la lista>)`, forzar un reinicio y comprobar que esa caja **no** aparece en `focus_list` (estado «mal» = no sensible, Review Focus 2). Su posición a los 5,0 s debe seguir la progresión sin volver a la base (continuidad del ATL tras reevaluar, Review Focus 3).
- [ ] **Step 3:** Captura tras `elegir` todas las claves de la lista 1 (más 0,8 s): la cinta muestra solo cajas de la lista 2 (Review Focus 4). Captura a los 2,6 s de abrir la lista en media: traducciones visibles (Review Focus 5).
- [ ] **Step 4:** Dar las cifras de «después» junto a las de «antes», incluidos el máximo y el p95 (tirones al reiniciar). **Si difícil no llega a 55 fps o el p95 supera 25 ms**, parar y reportar con el desglose (reevaluación / maquetado / GPU), sin añadir más arreglos sin hablarlo.
- [ ] **Step 5:** Lint limpio. El arnés se queda hasta la medición final de la Parte 2 y se borra al terminar.
