# Marco común de los minijuegos (Evento 6)

Referencia para las cinco sesiones de minijuego (Yotsuba, Nino, Miku, Ichika, Itsuki).
Refleja el código del 14/11/2026. **Si este documento y el código no coinciden, manda el código.**

Archivos del marco:
- `game/10_minijuegos.rpy`: Parte E (zonas, estilos, `mj_marco`, `mj_aviso`, `mj_prueba`) y Parte F (prueba del marco).
- `game/10_mj_chibi.rpy`: `mj_retrato`, `mj_globo` y las reacciones de la chibi.
- `game/09_menus_sistema.rpy`: `cinta_boton`.
- `game/ui/mj_columna.png` y `game/ui/mj_columna_banda.png`: los genera `herramientas/generar_ui.py` (`MJ_COLUMNA`).

---

## 1. Decisiones (no se reabren)

1. **Dirección «Columna de la hermana».** A la izquierda, una banda propia de la hermana con la cinta, el HUD, el globo y la chibi. A la derecha, un área de juego rectangular. Debajo, una franja fija para los avisos.
2. La **chibi general** va a **zoom 1.0**. Las demás chibis (las corredoras del relevo, por ejemplo) siguen pequeñas.
3. No se encoge a una hermana sola. Si falta sitio, se reorganiza el diseño o se encoge a todas por igual. Los accesorios (lazo, ahoge, moños) pueden sobresalir.
4. Cada hermana lleva **su color** (`PETALO_COLOR`) y **su motivo** (`ui/hud_icono_<h>.png`: destello, mariposa, ecualizador, trébol, estrella).
5. **Un solo contador de progreso** por minijuego, en el HUD.
6. Dos familias tipográficas, un tamaño por nivel.
7. Nada en bucle en el marco. Las reacciones duran entre 0,15 y 0,4 s.

## 2. Zonas (pantalla 1920×1080)

| Zona | Medidas | Constante |
|---|---|---|
| Columna | x 0–400. Relleno hasta x 380 arriba y x 360 abajo; banda de su color a +6 px (x 366–393) | `MJ_COLUMNA = (400, 380, 360)` en `generar_ui.py` |
| **Área de juego** | **x 440–1880, y 112–932 (1440×820)** | `MJ_AREA_X/Y/W/H` = 440, 112, 1440, 820 |
| Centro del área | x **1160** | `MJ_AREA_CX` (úsalo con `xanchor 0.5`, **nunca** `xalign 0.5`, que centra en 960) |
| Franja de avisos | centro (1160, 1000); ancho máximo 1200; caben 2 líneas | `MJ_AVISO_Y`, `MJ_AVISO_ANCHO` |
| Cinta del título | ypos 22, alto 64; puede salirse de la columna por arriba (termina en y 86 < 112) | `hud_cinta_vista` |
| HUD | x 40, y 116, 320 de ancho; termina hacia y 345 con todo activo | `MJ_HUD_X/Y/ANCHO` |
| Chibi general | centro x 180; borde inferior del PNG en y 1090 (pies en 1074); ocupa x 49–311 | `MJ_CHIBI_X/Y` |
| Globo | ancho máx. 300; punta 12 px sobre la coronilla más alta (lazo de Yotsuba) → borde inferior del globo en y 559; con 3 líneas el borde superior queda hacia y 403 | `MJ_GLOBO_ANCHO`, `MJ_GLOBO_HUECO` |

Nada interactivo del minijuego fuera del área. El velo (`MJ_VELO = "#0B0712A6"`) cubre toda la pantalla bajo la columna.

## 3. `mj_marco`: la interfaz

```
screen mj_marco(hermana, titulo, intento=1, fallos=0, nivel="dificil", progreso=0, total=1,
                tiempo=None, tiempo_total=None, unidad="ACIERTOS",
                recurso_txt="TIEMPO", recurso_unidad=" s",
                vidas=None, vidas_max=0, vidas_txt="",
                chibi=None, globo=None, anim="quieto",
                aviso="", aviso_tipo="info")
```

Uso: `use mj_marco(...):` y dentro, el contenido del área. La screen que lo llama declara `modal True` y `zorder 95`.

| Argumento | Qué dibuja |
|---|---|
| `titulo` | La cinta: «MINIJUEGO» + título. Con `nivel == "asistida"` la etiqueta pasa a «MINIJUEGO · ASISTENCIA» |
| `intento` | La fila «INTENTO  n». `fallos` se acepta por compatibilidad y **no se dibuja** (siempre vale intento − 1) |
| `vidas`, `vidas_max`, `vidas_txt` | Iconos de su motivo a zoom 0,8 (32 px, separación 4; caben 9). Los vivos en su color, los perdidos en blanco al 20 % |
| `tiempo`, `tiempo_total` | El recurso: fila `recurso_txt` + cifra (`int(tiempo + 0.999)` + `recurso_unidad`) + barra de 320. Amarilla `#FFE3A0`; roja `#FF8A8A` por debajo del 25 %. Sirve para cualquier recurso (p. ej. `recurso_txt="CONCENTRACIÓN", recurso_unidad=""`) |
| `progreso`, `total`, `unidad` | **El** contador: fila `unidad` + «7 / 28» + barra de su color |
| `chibi`, `globo`, `anim` | Chibi general en la columna (`mj_retrato`). `chibi` = expresión (`neutral`, `animo`, `esfuerzo`, `triste`, `feliz`); `globo` = un `MJGlobo`; `anim`: `"salto"`, `"tiembla"` o cualquier otro valor (quieta) |
| `aviso`, `aviso_tipo` | Píldora en la franja fija. `""` = sin aviso. Al pasar a `""` sale con el último texto. `aviso_tipo`: `"bien"`, `"mal"` o `"info"` |

Orden de dibujo: velo → columna → cinta → HUD → **contenido del minijuego** → chibi y globo → aviso.

## 4. Tipografía

Dos familias:
- **Shippori Mincho B1** (`gui.name_text_font`): mayúsculas espaciadas, cifras y botones.
- **M PLUS Rounded** (fuente por defecto): frases.
- Klee One solo como contenido dentro del cuaderno de Itsuki; no forma parte del marco.

| Estilo | Familia | Tamaño | Color | Contorno | Uso |
|---|---|---|---|---|---|
| `mj_titulo` | Shippori, kerning 4 | 40 | `#FFF8FC` | — | título de la intro |
| `mj_cifra_grande` | Shippori | 120 | `#FFFFFF` | 5 px | cuenta atrás |
| `mj_cifra` | Shippori | 30 | `#FFFFFF` | 3 px | cifras del HUD y del juego |
| `mj_etiqueta` | Shippori, kerning 3 | 20 | `#E8E0F2` | 3 px | etiquetas en mayúsculas |
| `mj_aviso_texto` | M PLUS | 34 | `#F3EEFA` | — | avisos |
| `mj_globo_texto` | M PLUS | 28 | tinta de la hermana | — | globo |
| `mj_cuerpo` | M PLUS | 24 | `#E8E0F2` | 3 px | reglas, instrucciones |
| `mj_nota` | M PLUS | 18 | `#CFC6E0` | 3 px | pistas pequeñas |

El contorno es siempre `#1B102699` (3 px) o `#1B1026CC` (5 px). Uso: `text "..." style "mj_cuerpo"`. Se puede cambiar el `color` si la semántica lo pide (gris deshabilitado, rojo de peligro).

Lo que no tiene estilo: los botones (los gestiona `cinta_boton`) y las cifras gigantes propias de un juego (combo de Miku); para estas, `mj_cifra_grande`.

## 5. Botones: `cinta_boton`

```
screen cinta_boton(texto, accion, clave, ancho=420, alto=58, tam=26, activo=True)
```

| Tamaño | `MJ_BOTON[...]` | ancho × alto, letra |
|---|---|---|
| Principal («Empezar», «¡Ahora!», «Entregar») | `"primario"` | 420 × 80, 34 |
| Secundario («Levantar la mano», «Mirar lista») | `"secundario"` | 340 × 64, 26 |
| Pequeño (ajustes, ±10 ms) | `"pequeno"` | 220 × 56, 24 |

Uso: `$ b = MJ_BOTON["primario"]` y luego `use cinta_boton("Empezar", accion, hermana, b[0], b[1], b[2])`.

Estados:
- **Normal:** relleno `#1B1026` al 80 % + borde de su color.
- **Hover:** relleno de su color aclarado al 35 % + borde blanco + texto oscuro.
- **Seleccionado:** relleno de su color + borde blanco.
- **Pulsado:** relleno de su color durante 0,14 s después del clic. Ren'Py no tiene estado de pulsado propio: se simula con `SetLocalVariable` + `timer` dentro del botón.
- **Deshabilitado** (`activo=False` o acción no sensible): relleno `#2A2236` al 80 %, borde `#6E6680`, texto `#8F8AA0`.
- Sonidos: `audio.sfx_hover` y `audio.sfx_click`, ya incluidos.

`cinta_boton` aporta **un solo** displayable, así que vale dentro de `grid`. Los botones propios de un juego (tarjetas, carriles, cajas) también llevan `hover_sound audio.sfx_hover` y `activate_sound audio.sfx_click`, salvo excepción decidida en la sesión (p. ej. carriles rítmicos).

## 6. Avisos (feedback)

- Una sola zona: la franja fija (centro 1160, 1000), que no tapa el área ni a las chibis.
- Una píldora: `opcion_neutra` teñida `#1B1026` + `opcion_marco` teñido del acento. Padding 40/14, texto `mj_aviso_texto` centrado.
- Acentos: `"bien"` `#9AE6B4`, `"mal"` `#FF8A8A`, `"info"` el color de la hermana.
- Movimiento: entra en 0,2 s (alpha 0→1, yoffset 14→0) y sale en 0,25 s (alpha →0, yoffset 8).
- El minijuego solo pasa `aviso=texto` mientras dure (su propio temporizador) y `""` al terminar.
- No transmitas el sentido solo con el color: el texto tiene que decirlo («Se cayó el testigo», «¡Bien!»).

## 7. Chibi general y globo

- `mj_retrato(hermana, expresion, globo, anim="quieto", x=MJ_CHIBI_X, y=MJ_CHIBI_Y, zoom=1.0)`. Lo normal es **no llamarlo**: se pasa `chibi=`, `globo=` y `anim=` a `mj_marco`.
- Reacciones de una sola pasada:
  - `mj_chibi_salto_uno`: 0,32 s, sube 26 px.
  - `mj_chibi_tiembla_uno`: 0,25 s.

  Se disparan cuando `anim` **cambia** a ese valor. Si se mantiene, no se repiten: para otra reacción, vuelve antes a `"quieto"`.
- Los transforms en bucle `mj_chibi_bob`, `mj_chibi_salto` y `mj_chibi_tiembla` siguen existiendo **solo** para chibis que son contenido del juego (corredoras de `mj_chibi_vista`).
- Globo: `MJGlobo` como siempre (`decir`, `poner`, `avanzar`). Entra en 0,18 s y sale en 0,2 s, con el último texto.

## 8. Movimiento

| Pieza | Animación | Duración |
|---|---|---|
| Cinta | `mj_cinta_entrada`, entra desde la izquierda | 0,35 s |
| Aviso | `mj_aviso_anim` | 0,2 s entrada / 0,25 s salida |
| Globo | `mj_globo_entra` | 0,18 s / 0,2 s |
| Chibi | `mj_chibi_salto_uno` / `mj_chibi_tiembla_uno` | 0,32 s / 0,25 s |
| Botón | pulsado | 0,14 s |

Regla para los minijuegos: lo que es **mecánica** (una marca que parpadea para indicar el momento, una nota que cae) puede moverse en bucle. La decoración y el marco, no.

## 9. Cómo probar

- **`jump mj_probar_marco`** (consola Shift+O): menú con cada hermana o las cinco seguidas. Sobre el fondo de cada una, abre el marco completo:
  - HUD con intento 2, asistida, 3 de 9 vidas, tiempo 20/80 y progreso 7/28.
  - El área de juego, marcada con un rectángulo.
  - Botones para cada aviso, el globo largo y corto, salto, tiembla, quitar vida, un botón deshabilitado y «Siguiente».
- `screen mj_marco_prueba(hermana, fijo=False)`: con `fijo=True` deja el globo largo y un aviso largo fijos, para capturas.
- `call mj_ejecutar("prueba", h)` (o el menú de depuración de `11_e6_debug.rpy`): el minijuego de prueba ya usa el marco nuevo (vidas = errores que quedan, aviso «¡Bien!/Fallo»).
- **Comprobado con capturas de las cinco hermanas:**
  - el globo más largo no pisa el HUD (unos 40 px de margen);
  - caben 9 vidas;
  - el título más largo («CADENA DE CONVERSIONES») no choca con nada;
  - el aviso de dos líneas cabe;
  - `cinta_boton` muestra bien los estados seleccionado, normal y deshabilitado (también en Opciones).
- **Sin comprobar automáticamente:** el destello de «pulsado» (necesita un clic real; pruébalo en `mj_probar_marco`).

## 10. Lo que tiene que adaptar cada minijuego

Mientras no se adapten, los cinco minijuegos funcionan, pero lo que dibujan a la izquierda de x 440 queda encima o debajo de la columna, y su chibi sigue en la posición antigua.

**Todos:**
- Quitar su `use mj_retrato(..., 250, 1090, 1.0)` y pasar `chibi=`, `globo=` y `anim=` a `mj_marco`.
- Todo el contenido dentro del área: `xpos MJ_AREA_CX xanchor 0.5` en vez de `xalign 0.5`, y nada en x < 440 ni en y > 932. Paneles de intro centrados en `MJ_AREA_CX` (≤ 1440 de ancho).
- Mensajes de acierto o fallo → `aviso=` / `aviso_tipo=`. Quitar sus textos de feedback sueltos.
- Textos con `font`/`size` sueltos → estilos `mj_*`.
- Botones principales → `MJ_BOTON`.
- Ningún contador de progreso propio: el del marco es el único.

**Yotsuba (`10_mj_yotsuba.rpy`, y2):**
- Testigos (`hbox` «TESTIGOS» en x 60) → `vidas=vivos_t, vidas_max=p["testigos"], vidas_txt="TESTIGOS"` (máx. 9 ✓).
- Quitar «TRAMO n / N · quién» (dejar solo quién corre), «VUELTA · nivel» (el nivel ya sale en la cinta) y el **«28» de la meta**.
- **Bug confirmado:** el «28» de la meta (l. 630) y las 28 marcas (`lit = int(28 * ...)`, `range(28)`) son fijos. Con 14 tramos (asistida) o 56 (difícil) la meta sigue diciendo 28. La meta no debe mostrar número (el progreso está en el HUD) y las marcas deben corresponder a la carrera real.
- Aviso dentro de la pista (`vivo.aviso`, tamaño 50) → `aviso=`.
- `Y2_CENTRO = 1180` → `MJ_AREA_CX`. La pista (x 500–1860) ya cabe en el área.
- Su `mj_retrato` con los pies en 830 desaparece.
- Ritmo y racha (x 1520) → dentro del área, como mecánica.
- `fixed at mj_chibi_tiembla`: tiembla toda la pantalla en bucle durante el error. Pasar a `mj_chibi_tiembla_uno` o quitarlo.
- `y2_pulso` en la MARCA: es mecánica; decidir si se queda.
- El botón «¡Ahora!» de 420×84 → `MJ_BOTON["primario"]`.
- El botón de pantalla completa (1920×1080) puede quedarse.

**Nino (`10_mj_nino.rpy`, n1):**
- La lista (x 60–600) + los estantes (`N1_VENTANA_W = 1210` desde x 650) ocupan 1800 px y no caben en 1440. Hay que rehacer la distribución (lista estrecha + ventana de ~1000, o lista encima).
- Cronómetro grande (y 56) **y** barra de tiempo del marco → uno solo (el marco ya recibe `vivo.restante()`, `vivo.total`).
- Popup en (1130, 80) → `aviso=`.
- Racha (x 800) → dentro del área.
- Los destellos rojos (`Solid("#FF2D2D")`, `#FF3B3B`) cubren toda la pantalla, columna incluida → limitarlos al área.
- Cuenta atrás de 220 → `mj_cifra_grande`.
- Intro (1180 de ancho, centrada en 960) → recentrar en `MJ_AREA_CX` (cabe).

**Miku (`10_mj_miku.rpy`, m3):**
- HUD izquierdo (x 70: CONCENTRACIÓN, PERFECTOS, PATRÓN DEL COMPÁS) → concentración al recurso del marco (`tiempo=conc, tiempo_total=vivo.fallos_max, recurso_txt="CONCENTRACIÓN", recurso_unidad=""`). Perfectos y el patrón del compás, dentro del área.
- Carriles centrados en 960 (`m3_x`) → centrados en `MJ_AREA_CX`.
- Feedback de ritmo (y 650): decidir en la sesión si pasa a `aviso=` o si es una excepción justificada junto a los carriles (es muy frecuente).
- Los botones de los carriles no tienen sonidos (probablemente a propósito, por el ritmo): confirmar.
- Intro (1100 de ancho) → `MJ_AREA_CX`.

**Ichika (`10_mj_ichika.rpy`, i1):**
- Barras MÁSCARA/ENERGÍA (`xalign 0.5`, 1020 de ancho) y tarjetas (x 640–1280) → recentrar en el área.
- Mensaje / consejo (y 865) → `aviso=` (o `mj_cuerpo` dentro del área si es una instrucción fija).
- Cambios de cifras en (1320, 545): revisar con el nuevo centro.
- Las tarjetas «EL PAPEL» y «LO QUE SIENTE» no tienen `activate_sound` (la segunda es «mantener»: decidir).
- Intro (1180 de ancho) → `MJ_AREA_CX`.

**Itsuki (`10_mj_itsuki.rpy`, it1):**
- Título del cuaderno, enunciado y «Tu hoja» en x 320 → ≥ 440.
- Tarjeta del paso (x 830–1690) → cabe; revisar después de mover la hoja.
- Avisos de revisión (`vivo.aviso`) y pista del profesor (`msg_pista`, y 752) → `aviso=` (la pista con `"info"`).
- «Sin ayuda», imitado con un `Solid` → `cinta_boton(..., activo=False)`.
- `it1_fila` e `it1_opcion` en hover: `it1_fila` no tiene `activate_sound`.
- El tiempo ya llega al marco (`t_rest`, `t_tot`) ✓.
- Klee One se queda en el cuaderno y la nota.
- Intro (1160 × 740) → `MJ_AREA_CX`; alto máximo 820.
