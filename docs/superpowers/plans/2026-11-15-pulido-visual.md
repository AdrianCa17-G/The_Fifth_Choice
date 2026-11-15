# Pulido visual (sesión 1). Plan de implementación

> **Para agentes:** sub-skill: superpowers:executing-plans (ejecución en esta misma sesión). Los pasos usan casillas (`- [ ]`).

**Objetivo:** un rótulo «HORA DE DECIDIR» antes de las decisiones con peso, tarjetas de decisión ajustadas a su texto, el boletín del Evento 6 como cinco tiras de papel con sellos, y la limpieza de comentarios y guías.

**Arquitectura:**
- (A) y (B) viven en `screen choice_peso` (`07_ui.rpy`). No se toca ningún archivo de capítulo.
- (C) reescribe `screen boletin_cinco` (`12_e6_pantallas.rpy`) con `showif` y eventos `appear` / `show` / `hide`. El guion sigue cambiando `e6_boletin_fase` sin pausas.
- Los PNG nuevos salen de `herramientas/generar_ui.py`.

**Tecnología:** Ren'Py 8.5.3 (screen language, ATL), Python 3 + Pillow para `generar_ui.py`, 1920×1080.

**Especificación:** `docs/superpowers/specs/2026-11-15-pulido-visual-design.md` (aprobada). Las capturas de «antes» están en el scratchpad de la sesión: `antes/`, `spike_b/` y `boceto_c2/`.

## Restricciones globales

- Sin ternarios. Todo `show` lleva su posición. Ninguna línea de diálogo de más de ~100 caracteres.
- Sin `modal` en pantallas con pausa (GUIA_UI §5).
- Un clic no adelanta un ATL.
- Último fotograma animado = estado estático, comprobado píxel a píxel.
- PNG solo con `cd herramientas && python generar_ui.py`, nunca a mano. Un número que esté en `generar_ui.py` y en un `.rpy` se cambia en los dos.
- (C) no muestra afinidad (D-13): solo `e6_notas`.
- (C) vive en `zorder -5`, con todo en y ≤ 730; la caja de texto empieza en 804.
- Lint: `"/c/Users/PERSONAL/Desktop/renpy-8.5.3-sdk/renpy.exe" "The Fifth Choice" lint` al final de cada tarea. Avisos previos conocidos: las sentencias inalcanzables de `00_definiciones.rpy`.
- No tocar `README.md`, `CAP1.md` ni los archivos `02_cap1_*.rpy`.
- Sin commits por tarea. Se hace commit solo si el usuario lo pide al final.
- Capturas: técnica de los planes del 14-11.
  - Arnés `game/zz_capturas_tmp.rpy` (ya existe; se amplía y se borra en la Tarea 5 con su `.rpyc`).
  - Se lanza con `renpy.exe "The Fifth Choice" run --warp game/zz_capturas_tmp.rpy:<línea del primer statement del label>` y termina con `renpy.quit()`.
  - Las capturas van a `<scratchpad>/despues/`.
  - El warp deja `renpy.game.after_rollback = True`: el arnés hace `renpy.pause(0.5, hard=True)` antes de la primera captura.
  - Las alturas que salen de `renpy.render` son `float`: pasarlas por `int()` antes de usarlas como tamaño. Un `float` se lee como fracción.

## Foco de revisión

1. **Teclado o clic durante la intro de (A).** Enter o un clic sobre una tarjeta antes de 1,45 s no elige nada, porque `sensitive listo` es falso. Lo cubre la Tarea 2, paso «`listo`».
2. **Rollback o carga en la decisión.** El menú reaparece en estado final, sin rótulo ni sonido, y se puede pulsar al instante. Lo cubre la Tarea 2, prueba manual del usuario, porque el warp no puede simular un rollback.
3. **Menú con todas las opciones de una línea, u opción de más de 5 líneas.** Altos 208 y 352 (tope). El texto va centrado. Más de 5 líneas desborda la tarjeta, igual que hoy pasaba con más de 6: ninguna opción del Cap. 1 pasa de 3. Lo cubre la Tarea 1 (`dec_autocomprobar`).
4. **Clics rápidos por el boletín.** Fase 1 → 2 → 3 antes de que terminen los sellos: el resultado tiene que ser idéntico a la fase 3 cargada directamente. Lo cubre la Tarea 3, comparación píxel a píxel con cambios de fase a 0,1 s.
5. **Guardar a mitad del boletín y cargar.** La fase en curso aparece directamente en su estado final (`on appear`). Lo cubre la Tarea 3, captura «directa» de cada fase comparada con la animada.

---

### Tarea 1: (B) Tarjetas ajustadas al texto

**Archivos:** `herramientas/generar_ui.py:29`; `game/07_ui.rpy:123-142, 339-345, 410-427`; `game/ui/` (PNG).

**Produce:**
- `TARJETA_ALTOS = [208, 256, 304, 352]` en los dos archivos. En `07_ui.rpy`, además, `TARJETA_MARGEN = 56`.
- `ui_altura_items(items) -> int`: `necesario = mayor + 2 * TARJETA_MARGEN`. Devuelve el primer alto ≥ `necesario`, o `TARJETA_ALTOS[-1]`, siempre como `int`. El respaldo `except` se queda.
- `style tarjeta_texto`: quita `ypos 52` y añade `yalign 0.5`. El resto queda igual.
- La flor de la tarjeta: `fixed` de 160×160 en `xpos 402`, `ypos (alto - 118)`, con `at tarjeta_flor` (`transform tarjeta_flor: zoom 0.7`), y dentro `use flor_sakura(decision_hermana, "hablante", 0, 0, color)`.
- `dec_autocomprobar()` en el `init -5 python` de `07_ui.rpy` (la amplía la Tarea 2).

- [ ] Escribir `dec_autocomprobar()` con estos asserts (los `items` se crean con una clase mínima de `caption` + `action`):
  - Nino `["Tienes razón en desconfiar. Solo el tiempo lo va a demostrar.", "Cargarle la cesta, sin decir nada.", "Yo sí voy a durar."]` → `256`
  - Miku `["Preguntarle cuánto tardaba la sal en llegar.", "Decirle que se le da bien. Es la verdad.", "Lo de la sal no entra en el examen."]` → `208`
  - `["Sí.", "No.", "Quizá."]` → `208`
  - una opción de 8 líneas (texto largo repetido) → `352`
  - `type(resultado) is int` en todos los casos.
- [ ] Lanzarla desde el arnés (`$ dec_autocomprobar()`): falla con los altos viejos (270 ≠ 256).
- [ ] Cambiar `TARJETA_ALTOS` en `generar_ui.py`, ejecutar `python generar_ui.py` y comprobar que existen `tarjeta_`, `tarjeta_marco_` y `halo_` × {208, 256, 304, 352} y `deco_tarjeta_<h>_<alto>` × 5 hermanas.
- [ ] Hacer el grep `tarjeta_(220|270|320|370)|halo_(220|270|320|370)|_(220|270|320|370)\.png` en `*.rpy` y `*.py`. Solo debe salir el arnés. Después, borrar los 32 PNG viejos de `game/ui/` y vaciar `game/cache`.
- [ ] Implementar lo de **Produce** en `07_ui.rpy`. `dec_autocomprobar()` pasa.
- [ ] Capturas `despues/decision_<h>.png` de las 5 hermanas, con el mismo arnés que `antes/`. Mirarlas junto a `antes/`:
  - texto centrado;
  - márgenes de 56 / 56 en la opción más larga;
  - ningún pétalo de color toca el texto (sobre todo en Ichika e Itsuki);
  - halo cálido / frío visible.
- [ ] Lint limpio.

### Tarea 2: (A) «Hora de decidir»

**Archivos:** `game/07_ui.rpy` (funciones, transforms, `screen choice_peso`).

**Consume:** Tarea 1. Además: `cort_sonar(jingle)` (`13_transiciones.rpy`), `petalo_giro`, `HUD_FUENTE`, `ui_mezclar`, `PETALO_COLOR` y `PETALO_ORDEN`.

**Produce:**
- `default decision_saltando = False`. `decision_peso()` añade `store.decision_saltando = renpy.is_skipping()`.
- `decision_animar() -> bool`: False si `renpy.in_rollback()`, si `store.decision_saltando` o si `preferences.transitions == 0`; si no, True.
- `define DEC_RITMOS = dict(velo=0.3, flor=0.30, linea=(0.25, 0.35), texto=(0.35, 0.30), sale=(0.95, 0.25), pregunta=0.95, tarjeta=0.95, paso=0.08, tarjeta_dur=0.30, listo=1.45)`, con los valores de la tabla de la especificación §6.2.
- Transforms:
  - `dec_flor`: zoom 0,6 → 1,0 y rotate −30 → 0, *ease* 0,30; luego `rotate None`.
  - `dec_linea`: `xzoom` 0 → 1 desde el centro.
  - `dec_texto`: alfa 0 → 1 y `yoffset` 12 → 0.
  - `dec_rotulo_sale`: tras la espera de `sale`, `yoffset` 0 → −30, zoom 1 → 0,92 y alfa → 0.
  - `decision_velo(intro)`, `pregunta_entrada(espera)` y `tarjeta_entrada(n, espera)`: los de hoy, con `espera` delante.
  - Todos terminan en alfa 1, offset 0 y zoom 1, menos el rótulo, que termina en alfa 0.
- `screen choice_peso(items)`:
  - `default intro = decision_animar()` y `default listo = not intro`.
  - Con `intro`:
    - `timer 0.01 action Function(cort_sonar, "mj_" + decision_hermana + "_saltado")`;
    - `timer DEC_RITMOS["listo"] action SetScreenVariable("listo", True)`;
    - el rótulo, centrado en (960, 540) dentro de un `fixed` con `dec_rotulo_sale`: flor de 5 pétalos (160 px; el suyo en su color al 95 %, los demás blancos al 25 %), línea `Solid(color)` de 900 × 2 debajo y «HORA DE DECIDIR» (46 px, `kerning 10`, blanco, `outlines [(4, tinta, 0, 0)]`);
    - velo, pregunta y tarjetas con sus transforms de entrada.
  - Sin `intro`: velo `alpha 0.5`, pregunta y tarjetas sin transform de entrada.
  - El `button` lleva `sensitive listo`.
  - Sin `modal`.
- `dec_autocomprobar()` amplía con:
  - `preferences.transitions = 0` → `decision_animar() is False`;
  - restaurar y poner `decision_saltando = True` → False;
  - las dos restauradas → `True`, llamada después de una interacción.

- [ ] Añadir los asserts de `decision_animar` a `dec_autocomprobar()` y comprobar que fallan (`decision_animar` no existe).
- [ ] Implementar lo de **Produce**. `dec_autocomprobar()` pasa.
- [ ] Capturas para las 5 hermanas: `anim_<h>_0.25.png` (flor abierta), `anim_<h>_0.70.png` (rótulo completo), `anim_<h>_1.10.png` (relevo) y `anim_<h>_2.00.png`. Además `estatico_<h>.png`, con `preferences.transitions = 0`, que el arnés restaura después.
- [ ] Comparar `anim_<h>_2.00` con `estatico_<h>`: `ImageChops.difference(...).getbbox()` es `None` en las 5.
- [ ] `listo`: con la pantalla abierta, el arnés lee `renpy.get_screen("choice_peso").scope["listo"]`. Debe valer False a 1,0 s y True a 1,6 s.
- [ ] Mirar las capturas:
  - el rótulo no se parece a la cortinilla, ni al hub ni a los minijuegos;
  - el color de cada hermana es el correcto;
  - el texto es legible sobre el velo y sobre fondos claros (`bg_biblioteca` de día).
- [ ] Prueba manual del usuario (no se puede automatizar). En una partida, en la decisión de cualquier hermana:
  1. al llegar: rótulo, sonido y tarjetas pulsables solo al final;
  2. elegir, retroceder con la rueda: el menú sale directo, sin rótulo ni sonido;
  3. guardar en el menú y cargar: directo;
  4. Opciones → Transiciones apagado: directo;
  5. con «Saltar» activo hasta la decisión: directo.
- [ ] Lint limpio.

### Tarea 3: (C) El boletín en cinco tiras

**Archivos:** `herramientas/generar_ui.py` (función nueva y su `guardar`); `game/12_e6_pantallas.rpy:79-206` (pantalla) y una sección nueva al final del bloque del boletín (constantes, transforms y label de prueba).

**Consume:** `E6_ORDEN_EXAMEN`, `E6_MATERIA`, `e6_notas`, `e6_boletin_fase`, `PETALO_COLOR`, `ui_mezclar`, `ui/flor.png`, `ui/hud_icono_<h>.png`, `ui/hub_aro.png` y `ui/hub_sello_fondo.png`.

**Produce:**
- `generar_ui.py`: `boletin_papel()` → `ui/boletin_papel.png`, de 64×64. Rectángulo redondeado (radio 10) de color (246, 238, 220, 255) con borde de 1 px (205, 192, 168, 255). Se usa como `Frame(..., 12, 12, 12, 12)`.
- Constantes en `12_e6_pantallas.rpy`:
  - `BOL_X = 290`, `BOL_W = 1340`, `BOL_Y0 = 226`, `BOL_PASO = 104`, `BOL_ALTO = 84`;
  - `BOL_COLX = [720, 920, 1120, 1320, 1520]`;
  - `BOL_TINTA = "#3A2A55"`;
  - `BOL_HOJA_X0 = 235`, `BOL_HOJA_PASO = 300`, `BOL_HOJA_Y = 190`, `BOL_HOJA_W = 250`, `BOL_HOJA_H = 380`;
  - `BOL_SELLO_Y = 200` (centro del sello dentro de la hoja).
- `screen bol_sello(h)`: el sello grande, centrado en su origen. Lleva:
  - `hub_sello_fondo` al 15 % y dos `hub_aro` de su color (zoom 1,45 a −8° y alfa 0,95; zoom 1,25 y alfa 0,6);
  - «100» de 80 px en `gui.name_text_font`, color `ui_mezclar(PETALO_COLOR[h], "#000000", 0.45)`.

  Se dibuja a tamaño de hoja y se reduce con zoom 0,5 en la celda, para que el texto no se emborrone.
- Transforms. Cada uno tiene `on appear` = su estado final sin animar.
  - `bol_entra(espera)`: aparece con fundido.
  - `bol_sale`: `on hide`, `yoffset` +20 y alfa → 0 en 0,5 s.
  - `bol_lapiz`: alfa 1 → 0,45 en 0,6 s.
  - `bol_golpe(k)`: tras 0,12·k s, zoom 0,75 → 0,5 y alfa 0 → 1 en 0,22 s. Es el 1,5 → 1,0 de la especificación, aplicado sobre la base 0,5. `on hide`: alfa 0 al instante.
  - `bol_viaja(x0, y0, x1, y1, k)`: parte de la celda con zoom 0,5; tras 0,06·k s, `ease` 0,7 hasta la hoja con zoom 1,0.
  - `bol_hoja(k)`: fundido de 0,4 s tras 0,5 + 0,06·k s.
  - `bol_detalle(k)`: fundido de 0,3 s tras 0,8 + 0,06·k s.
- `screen boletin_cinco()` reescrita según la especificación §6.4:
  - `zorder -5`, fondo `Solid("#0B0712E8")` y «LA CUENTA» como hoy.
  - `showif fase < 3`: las cabeceras (icono encima de la materia) y las tiras. Cada tira lleva sombra, `boletin_papel`, franja, flor y nombre.
  - Notas fuera de la diagonal: `showif fase < 2`, en tinta; `showif fase >= 2`, la misma nota con `bol_lapiz`.
  - Diagonal: `showif fase < 2`, «100» en tinta igual que las demás notas; `showif fase == 2`, `use bol_sello(h)` con `bol_golpe(k)` en su celda; `showif fase >= 3`, `use bol_sello(h)` con `bol_viaja` (celda `(BOL_COLX[k], BOL_Y0 + k*BOL_PASO + 42)` → hoja `(BOL_HOJA_X0 + k*BOL_HOJA_PASO + 125, BOL_HOJA_Y + BOL_SELLO_Y)`).
  - Las 25 notas comparten el mismo estilo (`gui.text_font`, 40, `BOL_TINTA`) y van centradas en vertical en su tira.
  - `showif fase >= 3`: las hojas detrás del sello viajero (`bol_hoja`), con franja superior, icono (y 52), materia (30 px, y 300) y una flor pequeña (y 344) que no pisa la materia (`bol_detalle`).
- `label boletin_cinco_prueba` (consola: `jump boletin_cinco_prueba`):
  - `$ quick_menu = False` y `scene bg_aula` con `with fade`;
  - `e6_notas` de ejemplo: diagonal en 100 y fuera de ella `62 + (i*7 + j*11) % 27` (todo entre 62 y 88; cumple I1/I2);
  - `show screen boletin_cinco` y las tres fases, cada una con una o dos líneas de `mc_pensamiento` copiadas del guion de `02_cap1_evento6.rpy:4320-4354`;
  - `hide screen boletin_cinco`, `$ quick_menu = True` y `return`.

- [ ] Añadir `boletin_papel()` a `generar_ui.py`, ejecutar `python generar_ui.py` y comprobar que existe `game/ui/boletin_papel.png` (64×64).
- [ ] Implementar las constantes, `bol_sello`, los transforms, la pantalla y el label.
- [ ] Capturas, sin caja de texto, con `preferences.text_cps` sin tocar:
  - `bol_f<n>_anim.png`: fase 1 al abrir, y luego cambiar la fase con la pantalla abierta, 3 s después de cada cambio;
  - `bol_f<n>_directa.png`: pantalla abierta de cero ya en la fase n;
  - `bol_f3_rapida.png`: cambios 1 → 2 → 3 a 0,1 s y captura 3 s después.
- [ ] Comparaciones: `bol_f<n>_anim` frente a `bol_f<n>_directa` para n = 1, 2, 3, y `bol_f3_rapida` frente a `bol_f3_directa`. En todas, `getbbox()` es `None`.
- [ ] Capturas a mitad de cada transición: 0,15 s, 0,35 s y 0,6 s tras pasar a la fase 2 y a la fase 3. Mirarlas: los sellos golpean en orden, los «100» viajan desde su celda y nada parpadea en el relevo entre celda y viaje.
- [ ] Capturas con `mc_pensamiento` encima (como en `antes/boletin_f<n>.png`):
  - nada importante bajo la caja;
  - las notas a lápiz se leen;
  - el papel parece papel y no metal;
  - los colores de las hermanas son correctos.
- [ ] Lint limpio.

### Tarea 4: Revisión de diseño (Impeccable)

- [ ] Pasar por `impeccable:impeccable` en modo crítica las capturas `despues/` de las Tareas 1 a 3, junto a las de `antes/`, con este contexto: «pulido, no rediseño; VN con lenguaje de cortinillas, flor de cinco pétalos, colores de hermana».
- [ ] Aplicar solo los arreglos materiales que no contradigan la especificación aprobada. Si cambia algo, repetir las capturas y las comparaciones píxel a píxel de la tarea afectada.

### Tarea 5: (D) Limpieza y documentación

**Archivos:** `game/12_e6_pantallas.rpy:8`, `docs/GUIA_AUDIO.md` §4, `docs/GUIA_UI.md` §2–§4 y `game/zz_capturas_tmp.rpy` (se borra).

- [ ] `12_e6_pantallas.rpy:8`: el comentario queda como `## Evento 6: foto del grupo (camara.mp3)`, sin «[NUEVO]» y sin «solo si existe».
- [ ] `GUIA_AUDIO.md` §4, dos filas nuevas en la tabla de efectos:
  - `sfx_estomago` | (origen por confirmar) | «Beat de Itsuki, 3,6 s; `play audio`, volumen 1.5»;
  - `sfx_camara` | (origen por confirmar) | «Evento 6, foto del grupo, 0,6 s; `play audio`, volumen 1.5».
- [ ] `GUIA_UI.md`:
  - §3: los altos nuevos de `TARJETA_ALTOS`.
  - §4, receta nueva «Hora de decidir». Dónde vive (`choice_peso`); que no hace falta llamar a nada; cuándo sale directo (rollback o carga, modo saltar, Transiciones apagado), con el porqué; `DEC_RITMOS`; el sonido `cort_mj_<h>_saltado`; `sensitive listo`; y en qué se distingue de las otras familias (radial).
  - §4, receta nueva «Tarjetas de decisión». Alto por líneas (48 px por línea + 2 × 56), texto centrado, la flor a 0,7 en la esquina, y cómo cambiar los altos en los dos sitios.
  - §4, receta nueva «Boletín del Evento 6». Las fases con `$ e6_boletin_fase`; `boletin_papel.png`; `bol_sello`; la regla `appear` = final; que solo muestra notas; y la prueba `jump boletin_cinco_prueba`.
- [ ] Borrar `game/zz_capturas_tmp.rpy` y su `.rpyc`. `git status` no muestra archivos sueltos fuera de lo previsto.
- [ ] Lint final limpio.
- [ ] Informe al usuario con las rutas de `antes/` y `despues/`, la prueba manual pendiente de la Tarea 2, los «origen por confirmar» de GUIA_AUDIO, y la pregunta de si se hace commit.
