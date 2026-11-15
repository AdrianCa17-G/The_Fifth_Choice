# M3 «El compás» · Adaptación al marco común — Plan de implementación

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Que `mj_m3` viva dentro del marco (columna, HUD, chibi, avisos) con todo su contenido en el área, y que el paso a la fase 2 se vea con calma.

**Architecture:** La screen `mj_m3` pasa a `use mj_marco(..., tiempo=conc, ..., chibi=, globo=, anim=, aviso=)`. El contenido se reordena en el área: cabecera (fase + PERFECTOS/PATRÓN) arriba, carriles centrados en `MJ_AREA_CX`, combo a la derecha del panel. Un único valor nuevo, `MJM3.apagado()` (0→1 durante el hueco entre fases), desatura los colores de Miku hacia el gris del reloj.

**Tech Stack:** Ren'Py 8.5.3, `game/10_mj_miku.rpy` (screen `mj_m3` y métodos de presentación de `MJM3`).

**Spec:** el mensaje de la tarea (PARTE 2) + `MARCO_COMUN.md` §10 (Todos y Miku) + la crítica de la sesión (capturas en `scratchpad/cap_m3`).

## Global Constraints

- Mecánica y temporización intactas: la Parte 1 (`t_pulso`, `beat2`, tics) no se toca. Mismos `MJ_PARAMS["m3"]`.
- Contenido solo en x 440–1880, y 112–932; `xpos MJ_AREA_CX` + `xanchor 0.5`, nunca `xalign 0.5`. Todo `add`/`text` lleva su posición. Sin ternarios.
- Estilos `mj_*`; botones de la intro con `MJ_BOTON`. Un solo contador de progreso (el del marco: NOTAS).
- Lint con los dos avisos conocidos.

## Zonas nuevas (1920×1080)

| Pieza | Posición | Constante |
|---|---|---|
| Cabecera izquierda | x 460: «FASE 1» (`mj_etiqueta`, y 128) + título de fase (`mj_titulo` del color vivo, y 152) + pista (`mj_nota` `#FFE3A0`, y 204). Motivo ecualizador (`hud_icono_miku.png`, zoom 0,8) a la izquierda del título, latiendo con el pulso | `M3_CAB_X = MJ_AREA_X + 20` |
| Cabecera derecha | x 1540 (320 de ancho): PERFECTOS (`mj_hud_fila`, y 128). En fase 2, debajo: «PATRÓN DEL COMPÁS» + 8 celdas de 36×40 (sep. 4 → 316) + «1 + 2 + …» | `M3_DER_X = MJ_AREA_X + MJ_AREA_W - 20 - MJ_HUD_ANCHO` |
| Panel de carriles | Centrado en `MJ_AREA_CX`: 4 carriles x 676–1644, 3 carriles x 770–1550. y 266–746 | `m3_x` con `MJ_AREA_CX`; `M3_Y_TOP = 276`, `M3_Y_META = 700` (caída de 424 px; antes 430) |
| Receptores | y 756–856 (`M3_Y_META + 56`) | — |
| Feedback de ritmo | `mj_cifra` de su color, centrado en `MJ_AREA_CX`, y `M3_Y_META − 64` (dentro del panel, sobre la línea) | — |
| Cuenta atrás | `mj_cifra_grande`, centrada en `MJ_AREA_CX`, y 400 | — |
| Combo | A la derecha del panel, centrado en x `(borde_panel + 1880) / 2`, y 420: «COMBO» (`mj_etiqueta`) + cifra (`mj_cifra_grande` a tamaño 56/68/82 según racha) + «+10 % en n» (`mj_nota` verde) | — |
| Intro | Panel de 1200 centrado en `MJ_AREA_CX`, ypos 152, alto automático; «Empezar» dentro del `vbox` (hoy se monta sobre la nota) | `MJ_BOTON["primario"]`, `["pequeno"]` |

## Decisiones

1. **Feedback de ritmo = excepción justificada junto a los carriles** (no `aviso=`). Sale en cada nota (más de una vez por segundo en difícil): en la píldora de y 1000 entraría y saldría sin parar, lejos de la línea donde mira el jugador, y taparía los avisos de verdad. Se queda en el panel, sobre la línea de meta, 0,3 s, con texto («Perfecto», «Tarde», «¡Sin nota!»), no solo color.
2. **`aviso=` queda para lo poco frecuente:** la recuperación por combo («+10 % de concentración», `"bien"`, 1,4 s, el `regen_txt` de hoy). **No se muestra durante el hueco entre fases.** Esa recuperación desaparece del HUD izquierdo.
3. **Concentración → recurso del marco:** `tiempo=vivo.concentracion(), tiempo_total=vivo.fallos_max, recurso_txt="CONCENTRACIÓN", recurso_unidad=""`. El marco ya la pinta en rojo por debajo del 25 % (hoy, 30 %).
4. **Carriles sin sonidos de hover/clic, a propósito:** un clic encima del tic o de la música ensucia el ritmo y mete un segundo «golpe» que no es el del compás. Se anota con un comentario en la screen. Lo mismo para la barra «TOCA» de la fase 2.
5. **Paso a la fase 2 (el momento emocional), sin avisos encima:**
   - `MJM3.apagado()`: 0 en la fase 1, sube lineal de 0 a 1 entre `t_cambio` y `t_f2` (los 4 pulsos del hueco, unos 3 s), 1 en la fase 2. Si se empieza en la fase 2 (`t_cambio < 0`), 1.
   - Todo lo que hoy es `color` (bordes del panel, línea de meta, notas, receptores, celdas del patrón, motivo, título) usa `col = ui_mezclar(color, M3_COLOR_RELOJ, 0.75 × apagado)`, con `M3_COLOR_RELOJ = "#C9C3D6"` (el gris lavanda que ya usan «Pronto»/«Tarde»).
   - El motivo ecualizador late con el pulso en la fase 1 (`alpha = pulso()`) y se queda quieto al 35 % en la fase 2: los audífonos se apagan.
   - La línea de meta sigue latiendo, ahora con el reloj (`beat2`), y la celda en curso del patrón se ilumina en dorado `#FFE3A0`: el reloj es lo único que sigue marcando.
   - La música se funde en 0,8 s (no cambia); el globo dice «…Solo queda el reloj.» (no cambia). Ningún aviso del marco durante el hueco.
6. **Rótulo de fase en dos piezas:** `rotulo_fase()` devuelve `(etiqueta, titulo)`: `("FASE 1", "Con los audífonos")` / `("FASE 1", "Con el metrónomo")`, `("", "Los audífonos se apagan.")`, `("FASE 2", "Solo el reloj")`, `("", "Compás completo.")`, `("", "")` en `listo`.
7. **Cambios de texto obligados por la nueva posición del patrón** (antes «a la izquierda»): intro «…y hay silencios; arriba a la derecha verás el patrón.» y pista «Las notas se desvanecen: guíate por el patrón del compás.» El resto del texto, igual.
8. **Chibi:** se quita `use mj_retrato(..., 250, 1090, 1.0)`; `mj_marco(chibi=vivo.expresion(), globo=vivo.globo, anim=vivo.anim())`. `anim()` devuelve `"quieto"` en vez de `"bob"` (el marco no hace bucles en la columna); `"salto"`/`"tiembla"` al terminar, sin cambios. Queda en el sitio del marco (centro x 180, borde inferior del PNG en y 1090).
9. **Textos sueltos → estilos:** letras de los carriles en `mj_titulo` (40), «TOCA · …» en `mj_cifra`, intro en `mj_titulo` / `mj_cuerpo` / `mj_etiqueta` / `mj_nota`. Botones de la intro: «Empezar» `MJ_BOTON["primario"]`; −10 ms, +10 ms, Restablecer `MJ_BOTON["pequeno"]`.

## Review Focus

1. 4 carriles (difícil): el combo con «82» cabe a la derecha del panel (236 px) sin salirse de x 1880. → Task 2, captura difícil fase 1 con racha ≥ 25.
2. Fase 2 con guía «ninguna»: el patrón (cabecera derecha) no queda bajo el globo de la chibi (hoy sí). → Task 2, captura difícil fase 2.
3. El título más largo («Los audífonos se apagan.») no choca con la cabecera derecha (x 1540). → Task 2, captura del hueco.
4. Intro de difícil: no se solapa nada y cabe en y ≤ 932. → Task 2, captura intro.
5. Con 3 carriles (media/asistida) todo sigue centrado en x 1160. → Task 2, capturas asistida.

---

### Task 1: Screen dentro del marco

**Files:** Modify `The Fifth Choice/game/10_mj_miku.rpy` (constantes, `m3_x`, `rotulo_fase`, `anim`, `pista`, nuevo `apagado`, screen `mj_m3` completa).

**Interfaces:** Produce `MJM3.apagado() -> float` (0–1), `MJM3.rotulo_fase() -> (str, str)`, constantes `M3_COLOR_RELOJ`, `M3_CAB_X`, `M3_DER_X`.

- [ ] **Step 1:** Constantes (`M3_Y_TOP 276`, `M3_Y_META 700`, `M3_COLOR_RELOJ`, `M3_CAB_X`, `M3_DER_X`) y `m3_x` centrado en `MJ_AREA_CX`.
- [ ] **Step 2:** `apagado()`, `rotulo_fase()` en tupla, `anim()` → `"quieto"`, texto de `pista()`.
- [ ] **Step 3:** Reescribir `mj_m3` según «Zonas nuevas» y «Decisiones» (orden de dibujo: cabecera → panel → carriles → línea → notas → feedback → cuenta → receptores → combo → intro). El `aviso` lo calcula la screen: `vivo.regen_txt` si `regen_t > 0` y no estamos en el hueco; si no, `""`.
- [ ] **Step 4:** Lint: sin errores nuevos. `grep -n "xalign 0.5\|mj_retrato\|ypos 100\|xpos 70" 10_mj_miku.rpy` sin resultados dentro de `mj_m3` (salvo `xalign`/`yalign` dentro de botones y `fixed` propios).

### Task 2: Capturas y pulido (Impeccable)

**Files:** temporal `The Fifth Choice/game/zz_capturas_tmp.rpy` (ya existe: intro, cuenta, fase 1, hueco, fase 2; añadir racha 30 en la fase 1 y una captura a mitad del hueco).

- [ ] **Step 1:** Capturas difícil y asistida. Comprobar los 5 puntos del Review Focus y que nada pasa de x 440–1880 / y 112–932.
- [ ] **Step 2:** Pasada de pulido sobre las capturas (alineación, espaciado, contraste del gris del reloj sobre el fondo de la biblioteca, el hueco). Arreglar lo que salga, repetir las capturas una vez.
- [ ] **Step 3:** Repetir la prueba de temporización de la Parte 1 (`scratchpad/zz_m3_prueba_tmp.rpy`, copiada a `game/`): `OK (45 casos)`. Borrar los dos `zz_*` y sus `.rpyc`. Lint limpio.
