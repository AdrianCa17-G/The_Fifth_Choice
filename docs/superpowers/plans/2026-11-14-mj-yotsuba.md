# Y2 · Relevo de las cinco: adaptación al marco común. Plan de implementación

> **Para agentes:** sub-skill: superpowers:executing-plans (ejecución en esta misma sesión). Los pasos usan casillas (`- [ ]`).

**Objetivo:** que `10_mj_yotsuba.rpy` use el marco común (columna, HUD, avisos, chibi general), que la pista ocupe el área de 1440 px, que las marcas correspondan a la carrera real y que en cada traspaso se vea quién lleva el testigo.

**Arquitectura:** solo cambian la screen `mj_y2`, las constantes `Y2_*` y tres métodos de `MJY2` (`poner_aviso`, `posiciones`, `testigo`). La mecánica, los tiempos y `MJ_PARAMS["y2"]` no se tocan. Única pieza compartida: un parámetro opcional `alfa=1.0` en `mj_chibi_vista` (`10_mj_chibi.rpy`).

**Tecnología:** Ren'Py 8.5.3 (screen language, ATL), 1920×1080.

**Especificación:** `docs/MINIJUEGOS/MARCO_COMUN.md` §10 (Yotsuba) + el encargo de la sesión.

## Restricciones globales

- Área: x 440–1880, y 112–932. Centrado con `xpos MJ_AREA_CX xanchor 0.5`, nunca `xalign 0.5`.
- Sin ternarios; todo `add`/`text` lleva su posición.
- Botones con `hover_sound audio.sfx_hover` / `activate_sound audio.sfx_click` (`cinta_boton` ya los trae). Excepción ya existente: el botón invisible de pantalla completa (sin sonido de hover: sonaría al mover el ratón por la pista).
- Las cinco corredoras al mismo `Y2_ZOOM` (0,58).
- Nada en bucle fuera de la mecánica (la marca puede pulsar; la pantalla no tiembla).
- Lint: `"/c/Users/PERSONAL/Desktop/renpy-8.5.3-sdk/renpy.exe" "The Fifth Choice" lint`. Avisos previos conocidos: `camara.mp3` y las sentencias inalcanzables de `00_definiciones.rpy`.
- `Y2_*` no aparece en `herramientas/generar_ui.py` (comprobado): no hay segundo sitio que cambiar.

## Foco de revisión

1. Niveles mezclados: con asistencia a medio camino `tramos` vale 42 o 21. Las marcas tienen que salir bien con cualquier `n`, no solo con 14, 28 y 56.
2. Traspaso cuando la que entrega llega al final de su carril y se solapa con la que recibe (`x_fin = inicio siguiente − 90`): el testigo tiene que verse encima de las dos.
3. Tramo final de vuelta (slot 4, Yotsuba): no hay receptora (`T + 1` no existe). La atenuación no puede fallar ni atenuar a quien no toca.
4. Errores seguidos: la reacción de la chibi de la columna se repite en cada error (vuelve a `"quieto"` entre uno y otro porque `nuevo_tramo` borra `humor`).
5. Intro de difícil (7 reglas): el panel no puede pasar de 820 px de alto.

---

### Tarea 1: Geometría de la pista y marcas reales (bug del 28)

**Archivos:** modificar `The Fifth Choice/game/10_mj_yotsuba.rpy` (constantes l. 27–47; screen l. 532–639).

- [ ] Constantes, calculadas a partir del área:
  - `Y2_PISTA_X = MJ_AREA_X` (440); nueva `Y2_PISTA_W = MJ_AREA_W` (1440)
  - `Y2_X0 = Y2_PISTA_X + 90` (530): la chibi más ancha mide ±79 px a zoom 0,58, más los 7 px del temblor
  - `Y2_LONG = (Y2_PISTA_W - 110) // 5` (266, antes 258). Meta en x 1860; la pista acaba en 1880
  - `Y2_CENTRO = MJ_AREA_CX` (1160)
  - En vertical se queda igual: `Y2_PISTA_Y` 350, `Y2_PISTA_H` 400, `Y2_SUELO` 735. El lazo de Yotsuba queda en y ≈ 435, dentro de la pista, así que no hace falta tocar `Y2_ZOOM`
- [ ] En la screen: `pw = Y2_PISTA_W`; borrar `lit`.
- [ ] Marcas: `for k in range(vivo.n)`, en `mx = Y2_X0 + int((k + 1) * Y2_LONG * 5 / float(vivo.n))`; encendida si `k < vivo.tramo`. La última cae sobre la meta.
- [ ] Borrar el `text "28"` de la meta.
- [ ] Comprobar a mano: con n = 14, 21, 28, 42 y 56, la marca `n − 1` cae en x 1860 y la primera en `530 + 1330 / n`.

### Tarea 2: Adaptación al marco

**Archivos:** modificar `10_mj_yotsuba.rpy` (`poner_aviso` y sus 9 llamadas; screen entera).

- [ ] `MJY2.poner_aviso(texto, tipo)`: guarda `self.aviso_tipo` en lugar de `aviso_color`. Correspondencia:
  - `"bien"`: ¡Perfecto!, Testigo recibido / Cruzó la meta, ¡Testigo recuperado!
  - `"mal"`: los errores (`error()`)
  - `"info"`: punto de control, «Vuelta n», «Todavía no.», salida en falso gratis (`avisa`)
- [ ] La screen calcula `aviso = ""` y, si `vivo.aviso_t > 0.0`, `aviso = vivo.aviso`. Lo pasa a `mj_marco` con `aviso_tipo=vivo.aviso_tipo`. Se borra el `text vivo.aviso` de tamaño 50.
- [ ] Llamada a `mj_marco`: `vidas=vivos_t, vidas_max=vivo.p["testigos"], vidas_txt="TESTIGOS", chibi=vivo.expresion_star(), globo=vivo.globo, anim=vivo.anim_star()`. Se borran el `hbox` de testigos (x 60) y el `use mj_retrato(..., 245, 830, 1.0)`.
- [ ] Fila de cabecera (ypos `MJ_AREA_Y + 16`):
  - a la izquierda (x `MJ_AREA_X + 20`): `text "CORRE" style "mj_etiqueta"` y debajo el nombre con `style "mj_titulo" color color_q`
  - a la derecha (x `MJ_AREA_X + MJ_AREA_W - 20 - MJ_HUD_ANCHO`): `use mj_hud_fila("RITMO", "×" + ritmo_txt)` + su barra, y `use mj_hud_fila("RACHA", str(racha) + " / " + str(cura), "#FFF0A8")` + su barra
  - se borran «TRAMO n / N · quién» y «VUELTA · nivel»
- [ ] Error:
  - se quita `fixed at (mj_chibi_tiembla if en_error else y2_quieto)` y el transform `y2_quieto`
  - el tinte rojo `#C0303033` pasa a cubrir solo la pista (`pw × ph` en `Y2_PISTA_X, py`)
  - la reacción la hacen la corredora (ya tiembla, es contenido) y la chibi de la columna (`tiembla_uno` vía `anim`)
- [ ] Textos sueltos a estilos: «MARCA» → `mj_etiqueta` con color `#FFE3A0`; «×» del señuelo → `mj_cifra` con color `#FF8A8A`.
- [ ] Botón «¡Ahora!»: `b = MJ_BOTON["primario"]` (420×80, 34), en `xpos Y2_CENTRO xanchor 0.5 ypos 790`.
- [ ] Intro:
  - el velo `#0B0712CC` cubre solo el área
  - el `frame` va en `xpos MJ_AREA_CX xanchor 0.5`, `ypos MJ_AREA_Y + MJ_AREA_H // 2 yanchor 0.5`, `xsize 1360`, `ymaximum MJ_AREA_H`
  - título `mj_titulo`; subtítulo `mj_etiqueta` con el color de Yotsuba; reglas `mj_cuerpo`
  - «Empezar» con `MJ_BOTON["primario"]`
- [ ] Se queda el botón invisible de pantalla completa (sirve el toque en móvil). `y2_pulso` también se queda: es mecánica, ayuda a encontrar la marca, que cambia de sitio en cada tramo.
- [ ] Lint limpio.

### Tarea 3: Quién lleva el testigo

**Archivos:** modificar `10_mj_yotsuba.rpy` (`posiciones`, `testigo`, bucle de chibis) y `10_mj_chibi.rpy` (`mj_chibi_vista`).

- [ ] `mj_chibi_vista(hermana, expresion, x, y, zoom=0.34, anim="bob", alfa=1.0)`: añadir `alpha alfa` a los cuatro `add`. Los demás que la llaman no cambian.
- [ ] `posiciones()`: cada fila lleva `"alfa"`:
  - 1,0 para la portadora (`i == T`) y para la receptora (`i == T + 1`, si existe)
  - `Y2_ALFA_RESTO = 0.45` para las demás
  - en `"pasa"`, la que entrega baja de 1,0 a 0,45 con `s`
  - en `"fin"`, todas a 1,0
- [ ] `testigo()` devuelve `(x, y, giro, portadora)`: la portadora es `Y2_ORDEN[T]`, y en `"pasa"` con `s >= 0.5` pasa a ser `Y2_ORDEN[T + 1]`.
- [ ] Orden de dibujo: primero las cuatro que no llevan el testigo, después la portadora y por último el testigo.
- [ ] El testigo pasa a ser un `Fixed` de 3 capas, girado: contorno `#1B1026` 90×24, borde blanco 84×18 y relleno 78×12 del color de quien lo lleva. Así deja de ser del mismo dorado que la marca y sigue leyéndose sobre el rojo de la pista, también con el color de Itsuki (`#EC7063`).
- [ ] Lint limpio.

### Tarea 4: Verificación con capturas y pasada de pulido

**Archivos:** crear y borrar `The Fifth Choice/game/zz_capturas_tmp.rpy`.

- [ ] Un label que, para `dificil`, `media` y `asistida`, hace `show screen mj_y2("yotsuba", MJ_PARAMS["y2"][nivel], 0, 2, 1, nivel, "Relevo de las cinco")`. Luego coge `vivo` con `renpy.get_screen("mj_y2").scope["vivo"]`, congela `vivo.tick`, fuerza los estados y hace `renpy.screenshot` en el scratchpad:
  - corre a mitad de tramo
  - `pasa` con `s ≈ 0,5`
  - `cae` con aviso «mal»
  - `fin`
  - intro (con `intento = 1`)
  - en difícil, también con n = 42
- [ ] Comprobar en las capturas:
  - nada a la izquierda de x 440
  - las marcas cuentan n y la meta no lleva número
  - el testigo se ve encima en el traspaso
  - el globo no pisa el HUD
  - el panel de intro de difícil cabe
  - la píldora del aviso queda en la franja
- [ ] Pulido con las capturas (alineación de la cabecera con el borde de la pista, contraste de «MARCA», atenuación). Una segunda ronda de capturas. Borrar `zz_capturas_tmp.rpy` y su `.rpyc`. Lint limpio.

### Tarea 5: Documentación

- [ ] Crear `docs/MINIJUEGOS/MJ_YOTSUBA.md`: zonas y constantes finales, decisiones (testigo, atenuación, sin temblor), chibi general en la columna (`MJ_CHIBI_X/Y`), rectángulos de la pista, la cabecera y el botón, y orden de dibujo (para la sesión de animaciones de entrada y salida).
- [ ] Guardar las decisiones en claude-mem.
