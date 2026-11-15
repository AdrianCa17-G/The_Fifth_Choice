# Y2 · Relevo de las cinco (Yotsuba)

Estado final tras adaptarlo al marco común (14/11/2026). Archivo: `game/10_mj_yotsuba.rpy`.
Referencia del marco: `MARCO_COMUN.md`. **Si este documento y el código no coinciden, manda el código.**

## Zonas (pantalla 1920×1080)

| Pieza | Posición / tamaño | Constante o fuente |
|---|---|---|
| Columna, cinta, HUD | Las del marco (x 0–400) | `mj_marco` |
| HUD: TESTIGOS | Vidas del marco: trébol, máximo 9 | `vidas=vivos_t, vidas_max=p["testigos"]` |
| HUD: TRAMOS | El único contador de progreso: «n / N» + barra | `progreso=vivo.tramo, total=vivo.n` |
| Chibi general (Yotsuba) + globo | Columna: centro x 180, borde inferior del PNG en y 1090, zoom 1,0 | `MJ_CHIBI_X/Y`, a través de `mj_marco(chibi=, globo=, anim=)` |
| Cabecera izquierda | «CORRE» (`mj_etiqueta`) + nombre en su color (`mj_titulo`), en (460, 128) | `MJ_AREA_X + 20`, `MJ_AREA_Y + 16` |
| Cabecera derecha | RITMO y RACHA (`mj_hud_fila` + barra de 320) en (1540, 128) | `MJ_AREA_X + MJ_AREA_W − 20 − MJ_HUD_ANCHO` |
| Marcas de tramo | Fila sobre la pista, y 326–350; «MARCA» en y 288 | `Y2_PISTA_Y − 24`, `− 62` |
| **Pista** | **x 440–1880, y 350–750** (todo el ancho del área) | `Y2_PISTA_X/W/Y/H` |
| Carriles | 5 de 266 px; salidas en x 530, 796, 1062, 1328, 1594; meta en x 1860 | `Y2_X0`, `Y2_LONG`, `y2_x(i)` |
| Franja de cada carril | 6 px del color de su corredora, y 740–746 | `Y2_FRANJA` |
| Suelo de las corredoras | y 735 (PNG anclado abajo); lazo de Yotsuba hacia y 435 | `Y2_SUELO`, `Y2_ZOOM = 0.58` |
| Botón «¡Ahora!» | 420×80 centrado en x 1160, y 790–870; color de quien corre | `MJ_BOTON["primario"]`, `Y2_CENTRO` |
| Avisos | Franja del marco, centro (1160, 1000) | `aviso=`, `aviso_tipo=` |
| Intro | Velo solo sobre el área; panel de 1360 de ancho centrado en (1160, 522); alto máximo 820 (la de difícil, con 7 reglas, cabe) | `MJ_AREA_*` |
| Toque en pantalla completa | Botón invisible de 1920×1080 en (0, 0), inactivo en la intro | — |

Orden de dibujo dentro del área: botón invisible → cabecera → pista (tinte rojo si hay error) → bordes → franjas → líneas de carril → marcas → meta → zona/señuelo/marca → cuatro corredoras → **portadora** → **testigo** → botón «¡Ahora!» → intro. Después, el marco dibuja la chibi general, el globo y el aviso.

## Constantes

```
Y2_PISTA_X = MJ_AREA_X              440
Y2_PISTA_W = MJ_AREA_W              1440
Y2_X0      = Y2_PISTA_X + 90        530   (media corredora = 79 px a zoom 0,58, más el temblor)
Y2_LONG    = (Y2_PISTA_W - 110)//5  266
Y2_CENTRO  = MJ_AREA_CX             1160
Y2_PISTA_Y 350 · Y2_PISTA_H 400 · Y2_SUELO 735 · Y2_ZOOM 0.58
Y2_ALFA_RESTO 0.45 · Y2_FRANJA 6
```

Ninguna de estas constantes aparece en `herramientas/generar_ui.py`. `MJ_PARAMS["y2"]` y los tiempos (`Y2_T_*`, `Y2_PREP*`) no han cambiado.

## Decisiones

1. **Marcas = tramos reales.** Hay `vivo.n` marcas (14, 28 o 56, o 21 y 42 con asistencia a medio camino). La marca `k` está en `Y2_X0 + (k+1)·1330/n`, de modo que la última cae sobre la meta. Se encienden las `k < tramo`. La meta no lleva número: el progreso numérico está en el HUD.
2. **El 28 en media:** se lee en la intro («MEDIA · 28 TRAMOS»), en el HUD («n / 28») y en las 28 marcas.
3. **Quién lleva el testigo:**
   - El testigo toma el color de quien lo lleva: contorno `#1B1026`, borde blanco y relleno de su color. Ya no es dorado como la marca.
   - En el traspaso cambia de color a mitad del arco.
   - Va en la mano de la portadora (x + 45, suelo − 120), no delante de la receptora. Al caer, baja 100 px, hasta los pies.
   - La portadora se dibuja delante de las demás y el testigo encima de todo.
4. **Atenuación** (`posiciones()` → `"alfa"`, que llega a `mj_chibi_vista(..., alfa)`):
   - a pleno, la portadora y la receptora; las demás, al 45 %;
   - en `"pasa"`, la que entrega se apaga y la siguiente receptora se enciende;
   - Yotsuba, cuando cierra la vuelta en la meta, no se apaga;
   - en `"fin"`, todas a pleno.
5. **El error ya no hace temblar la pantalla.**
   - Tiembla la corredora (contenido del juego, en bucle mientras dura el error).
   - La chibi de la columna hace `tiembla_uno` (vía `anim_star()` → `"tiembla"`).
   - El tinte rojo cubre solo la pista.
6. **Avisos** (`poner_aviso(texto, tipo)`):
   - `"bien"`: ¡Perfecto!, Testigo recibido, Cruzó la meta, ¡Testigo recuperado!
   - `"mal"`: Se cayó el testigo, Salió antes de tiempo…
   - `"info"`: punto de control, «Vuelta n», «Todavía no.», salida en falso gratis.
   - Duran 1 s (`aviso_t`).
7. **`y2_pulso`** en la marca se queda: es mecánica y ayuda a encontrar la marca, que cambia de sitio en cada tramo. Es lo único en bucle aparte de las corredoras.
8. **Franjas de color** en la base de cada carril («cinco tramos iguales»). Son estáticas.
9. **«¡Ahora!»** se oculta en la intro y en la celebración final (`fase == "fin"`).
10. **Botón invisible** de pantalla completa sin `hover_sound`, a propósito: sonaría cada vez que el ratón entra en la pantalla. «¡Ahora!» y «Empezar» son `cinta_boton`, con sus sonidos.

## Para la sesión de animaciones de entrada y salida

- Bloques que pueden entrar por separado:
  - la cabecera (dos `vbox`);
  - la pista con todas sus capas, de `add Solid("#B8453CE0"…)` a la meta;
  - las corredoras;
  - el botón «¡Ahora!».
- El marco ya anima la cinta (0,35 s), el aviso y el globo. No dupliques esas animaciones.
- Las corredoras usan `mj_chibi_vista`, que ya les aplica `bob`, `salto` o `tiembla`. Si una entrada necesita un transform, ponlo en un contenedor por encima: no cambies la `anim`.
- Tiempos que no se pueden alargar sin tocar la mecánica: la preparación del primer tramo (`Y2_PREP_PRIMERO` 0,7 s, más hasta 0,25 s aleatorios) y el final (`Y2_T_FIN` 1,8 s, después de los cuales se devuelve "ganado").

## Pendiente (propuestas no aplicadas)

- **A.** La carrera no siempre la cierra Yotsuba en la meta. Las cinco corren en ciclo, así que el último tramo lo corre Miku con 28, Itsuki con 14 e Ichika con 56. Arreglarlo es tocar la mecánica (empezar la carrera desfasada).
- **B.** Con asistencia a medio camino desde difícil, la cinta dice «media» pero la carrera tiene 42 tramos.

## Cómo probar

- `call mj_ejecutar("y2", "yotsuba")` desde la consola (Shift+O), o `jump mj_probar_y2` (sin el boost de Nino = difícil; con boost = media).
- Para asistida: con el boost y modo «asistido» (en el menú de ajustes de `11_e6_debug.rpy`), o fallando cuatro veces en media.
