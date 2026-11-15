# N1′ «Compras para seis» · Adaptación al marco y distribución B — Plan

> **For agentic workers:** REQUIRED SUB-SKILL: superpowers:executing-plans. Steps use checkbox (`- [ ]`) syntax.

**Goal:** N1′ dentro del marco común, con la distribución B (lista arriba, estantes a todo lo ancho) elegida por el usuario, y menos reinicios de interacción (lag restante de la Parte 1).

**Architecture:** Un solo archivo, `game/10_mj_nino.rpy`. El marco (`mj_marco`) pone el reloj, el contador LISTAS, la chibi, el globo y el aviso. El área tiene dos bloques: la franja de la lista arriba y los estantes debajo. El reloj grande desaparece, y la barra de memoria y el fundido de la traducción pasan a ATL, así que la firma solo cambia por segundos enteros y por eventos.

**Spec:** mensaje de la tarea, PARTE 2 + `docs/MINIJUEGOS/MARCO_COMUN.md` §10 («Todos» y «Nino»). Elección del usuario: **B · Lista encima**.

## Global Constraints

- Contenido solo en x 440–1880, y 112–932. Centrado con `MJ_AREA_CX` + `xanchor 0.5` (`xalign 0.5` solo dentro de contenedores, como en Y2/I1/It1).
- Botones con `hover_sound audio.sfx_hover` y `activate_sound audio.sfx_click`. «Mirar lista» → `MJ_BOTON["secundario"]`; «Empezar» → `MJ_BOTON["primario"]`.
- Textos → estilos `mj_*`. Código completo, sin ternarios. La mecánica y `MJ_PARAMS["n1"]` no cambian.
- El sexto hueco conserva su sentido y sus tres opciones (`MJ_N1_SEXTO`).

## Zonas (B)

| Pieza | Medidas | Constante |
|---|---|---|
| Franja de la lista | x 440–1880, y 112–324 (1440×212), tono y borde de la hermana de la lista | `N1_LISTA_Y = MJ_AREA_Y`, `N1_LISTA_H = 212` |
| Bloque izquierdo | x 472: «LISTA n/5» (`mj_etiqueta`), nombre (`mj_titulo`, su color), «RACHA ×n» (`mj_cifra` `#FFE3A0`, desde 2) | — |
| Productos | Celdas de 260 desde x 780 (hasta 4 → x 1820), y 132: casilla 24 + EN `mj_cuerpo` + ES `mj_nota` | `N1_CELDA_X = 780`, `N1_CELDA_W = 260` |
| Fila inferior de la franja | y 252–316: «6.º hueco de la cesta» en x 472; MEMORIZA + barra de 1040 / «Mirar lista» 340×64 / «MIRANDO…» en x 780 | — |
| Estantes | x 440–1880; fila de 142 de alto (etiqueta en y+4, cajas en y+28), paso 150; bloque centrado en y 330–932 | `N1_VENTANA_W = 1440`, `N1_FILA_H = 150`, `N1_ESTANTES_Y = 330`, `n1_fila_y0(n)` |
| Cajas | 272×112 (sin cambio); paso horizontal 1440/4 = 360 en difícil | `N1_CAJA_W/H` |
| Destellos | Latido y destello rojos solo sobre el área (1440×820) | `MJ_AREA_*` |
| Cuenta atrás | Velo sobre el área + cifra `mj_cifra_grande` en (1160, centro del área) + «PREPÁRATE» `mj_etiqueta` | — |
| Intro | Panel de 1180×660 centrado en (1160, centro del área) | — |
| Sexto hueco | Franja de la lista (todo marcado) + frase `mj_aviso_texto` en y 400 + tres opciones de 820×110 desde y 470, centradas en x 1160 | — |

## Tasks

### Task 1: Clase `MJN1`
- [ ] Quitar `popup()`/`popup_txt`/`popup_col` y pasar a `avisar(texto, tipo)` con `aviso`, `aviso_tipo` y `aviso_t` = 1,2 s. Textos: error «Esa no es · −P s» (`"mal"`), mirar «Miras la lista · −C s» (`"info"`), racha «Racha ×n · +B s» (`"bien"`). Cifras con coma decimal.
- [ ] `firma()`: segundos enteros del reloj (`int(restante() + 0.999)`, lo que dibuja el marco), `trad_alpha() > 0` en vez de cuantizado, sin memoria cuantizada (ATL), `aviso_t > 0` y `aviso`.
- [ ] Quitar `trad_alpha()` cuantizado de la screen y usar `trad_visible()`.

### Task 2: Screens
- [ ] `mj_n1`: `use mj_marco(..., vivo.lista, 5, vivo.restante(), vivo.total, "LISTAS", chibi=, globo=, anim=, aviso=, aviso_tipo=)`; quitar `mj_retrato`, el reloj grande y el popup.
- [ ] Nueva `mj_n1_lista(vivo)` (franja), estantes con `n1_fila_y0`, sexto, cuenta atrás e intro según la tabla de zonas.
- [ ] `mj_n1_caja(clave, estado, accion, trad, color)`: `trad` es un bool; la ES entra con `n1_trad` (alpha 0 → 1 en 0,4 s) cuando el retardo es mayor que 0.
- [ ] Barra de memoria: `n1_vaciar(ancho, dur)` (xsize → 0 linear dur), con el ancho inicial calculado del tiempo restante. Así, si se reinicia a mitad, sigue bien.

### Task 3: Verificación
- [ ] Lint limpio.
- [ ] Capturas (arnés temporal) en los tres niveles: intro, compras, memoria oculta (difícil), error con aviso, cuenta atrás y sexto. Nada fuera del área, la franja no tapa el HUD y las cajas son legibles.
- [ ] Medición final de rendimiento en los tres niveles (mismo arnés) y comprobación de foco.
- [ ] `docs/MINIJUEGOS/MJ_NINO.md`. Borrar el arnés.
