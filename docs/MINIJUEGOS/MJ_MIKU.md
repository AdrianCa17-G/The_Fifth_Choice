# M3 · El compás (Miku)

Estado final tras sincronizarlo con un mapa de pulsos y adaptarlo al marco común (14/11/2026).
Archivos: `game/10_mj_miku.rpy`, `game/10_mj_miku_pulsos.rpy` (generado) y `herramientas/generar_pulsos_miku.py`.
Referencia del marco: `MARCO_COMUN.md`. **Si este documento y el código no coinciden, manda el código.**

## Mapa de pulsos (fase 1)

`miku_tema.ogg` («The calm seaside») no tiene tempo fijo: va de ~75 a ~79 BPM según el tramo. La fase 1 ya no calcula las notas con un BPM, sino con los instantes reales de cada pulso.

**Regenerarlo** (por ejemplo, si cambia la pista), desde `The Fifth Choice/`:

```
pip install librosa
python herramientas/generar_pulsos_miku.py            (escribe game/10_mj_miku_pulsos.rpy)
python herramientas/generar_pulsos_miku.py --prueba   (autoprueba de las correcciones)
```

El `.rpy` no se edita a mano. El script:
1. Calcula la envolvente de ataques (hop 256, unos 11,6 ms).
2. Ejecuta `librosa.beat.beat_track` con tempo de partida 76 BPM y `tightness` 400. El seguimiento con BPM variable de librosa duplicaba el tempo en algunos tramos (152 y 144 BPM) y se descartó.
3. Corrige tres casos: pulsos dobles (separación < 0,6 × la mediana), huecos (> 1,5 × la mediana) y pulsos erráticos al principio (se apartan más de un 25 % de la mediana). Con la pista actual no hace falta ninguna corrección.
4. Comprueba el resultado con asserts y saca un resumen por tramos de 30 s.

**Resultado actual:**

| | |
|---|---|
| Pulsos | 223, del primero en **1,788 s** al último en 174,928 s |
| Tempo medio | 76,9 BPM; un pulso dura entre 0,650 y 0,871 s |
| Tempo por tramos de 30 s | 75,4 · 75,3 · 77,4 · 77,9 · 78,7 · 76,9 |
| Fase | Energía de ataque 5,15 en el pulso y 1,29 a medio pulso: los pulsos caen en el tiempo fuerte |

El ataque de 1,416 s es una anacrusa medio pulso antes del primer pulso. No se inventan pulsos hacia atrás.

**Cuántos pulsos pide la fase 1** (simulación del generador, 20 000 partidas por nivel): difícil acaba entre el pulso 43 y el 68, media entre el 33 y el 50, y asistida entre el 28 y el 34. Como mucho se usan unos 55 s de canción, así que sobran pulsos.

## Temporización (`MJM3`)

Todo pasa por `t_pulso(k)`, el instante del pulso k en la canción:
- **Hasta `bc`** (el pulso del cambio de fase, `gen[1]`), lee `self.pulsos`: `MIKU_PULSOS` con el tema, o una lista uniforme a `MIKU_BPM` en el plan B.
- **Desde `bc`**, suma pulsos fijos de `beat2`.
- **Fuera del mapa**, extrapola con el primer o el último intervalo. Hoy no ocurre.

| Función | Qué hace |
|---|---|
| `t_corchea(c)` | Corchea par: su pulso. Impar: el punto medio entre su pulso y el siguiente |
| `fase_pulso(s)` | Para un instante `s` de la canción, el pulso en curso y la fracción recorrida (`bisect` en la fase 1, cálculo directo después) |
| `t_cambio`, `t_f2`, tics | `t_pulso(bc)`, `t_pulso(bc + MIKU_GAP_BEATS)` y `t_pulso(r)`, todos menos `pos0` |
| `cuenta()` | 4-3-2-1, cambia en cada pulso real |
| `pulso()` | Latido de la línea de meta: sigue la música en la fase 1 y el reloj en la 2 |
| `slot_actual()` | Casilla del patrón que toca ahora; usa `beat2` |

**Tempo de la fase 2:** `beat2 = (t_pulso(bc) − t_pulso(bc − 8)) / 8`, la media de los dos últimos compases que sonaron (`MIKU_F2_MEDIA = 8`). Con el mapa actual sale entre 0,763 y 0,829 s (**72,4–78,6 BPM**), según dónde caiga el cambio (entre 24 y 56 s). Con 4 pulsos salía hasta 85 BPM por el rubato, y el salto se notaba. El primer tic del hueco suena en el pulso real del cambio, mientras la música se funde en 0,8 s.

**Puntos de control:** `pos0 = abs_t[inicio] − abs_t[0]`. La música arranca 4,98 s antes de la nota en la que se reanuda: la misma entrada que la primera vez (intro de 1,79 s + 4 pulsos). `sonar_desde` y `resincronizar` trabajan con la posición en la canción, así que no dependen del tempo.

**Plan B** (`MIKU_USAR_TEMA = False`): metrónomo en las dos fases a `MIKU_BPM = 76,9` (la media de la canción). Usa el mismo código que la versión con música.

**Latencia del jugador:** `persistent.m3_latencia_ms` sin cambios (por defecto 50 ms; se ajusta en la intro).

## Zonas (pantalla 1920×1080)

| Pieza | Posición / tamaño | Constante |
|---|---|---|
| Columna, cinta, HUD | Las del marco: INTENTO, CONCENTRACIÓN (recurso, sin unidad; roja por debajo del 25 %) y NOTAS («n / total») | `mj_marco(..., vivo.cursor, vivo.total, vivo.concentracion(), vivo.fallos_max, "NOTAS", recurso_txt="CONCENTRACIÓN", recurso_unidad="")` |
| Chibi general (Miku) + globo | Columna: centro x 180, borde inferior del PNG en y 1090, zoom 1,0 | `MJ_CHIBI_X/Y`, a través de `mj_marco(chibi=, globo=, anim=)` |
| Cabecera izquierda | x 460: «FASE n» (`mj_etiqueta`, y 128); motivo ecualizador (`hud_icono_miku`, zoom 0,8, 32 px) en (460, 168); título de fase (`mj_titulo`, color claro) en (506, 152); pista (`mj_nota` `#FFE3A0`, y 208) | `M3_CAB_X = MJ_AREA_X + 20` |
| Cabecera derecha (solo fase 2) | x 1540: «PATRÓN DEL COMPÁS» (`mj_etiqueta`, y 128), 8 celdas de 36×40 con separación 4 (316 de ancho) y «1 + 2 + 3 + 4 +» centrados debajo. Termina hacia y 222 | `M3_DER_X = MJ_AREA_X + MJ_AREA_W − 20 − MJ_HUD_ANCHO` |
| Panel de carriles | Centrado en x 1160. Con 4 carriles (difícil): x 676–1644, carriles en x 806 / 1042 / 1278 / 1514. Con 3 (media y asistida): x 770–1550, carriles en x 900 / 1160 / 1420. y 266–746 | `m3_x(i, n)` (sep. 236 / 260), `M3_ANCHO_CARRIL = 200` |
| Carriles y caída | Carriles en y 276–740; las notas caen de `M3_Y_TOP = 276` a `M3_Y_META = 700` (424 px) | `M3_Y_TOP`, `M3_Y_META` |
| Línea de meta | Halo de 22 px en y 692 + línea de 6 px en y 700, con alpha `pulso()` | — |
| Feedback de ritmo | `mj_cifra` de su color, centrado en x 1160, y 636 (sobre la línea) | `M3_Y_META − 64` |
| Cuenta atrás | `mj_cifra_grande`, centrada en x 1160, y 400 | — |
| Receptores | y 756–856: teclas de 200×100 (`mj_titulo`) o, en la fase 2, la barra «TOCA · cualquier tecla o Espacio» (`mj_cifra`) a lo ancho del panel | `M3_Y_META + 56` |
| Columna derecha | Centrada entre el borde del panel y x 1880 (x 1762 con 4 carriles, x 1715 con 3): PERFECTOS (`mj_etiqueta` + `mj_cifra`, y 300) y COMBO (`mj_etiqueta` + cifra `mj_cifra_grande` a 56/68/82 según la racha + «+10 % en n» `mj_nota` verde, y 420) | — |
| Avisos | Franja del marco, centro (1160, 1000): solo «Combo: +N % de concentración» (`"bien"`, 1,4 s) | `aviso=`, `aviso_tipo="bien"` |
| Intro | Panel de 1200 de ancho centrado en (1160, 152), alto automático (hacia y 825): título, reglas (`mj_cuerpo`), ajuste de sincronía (`mj_nota`), tres `MJ_BOTON["pequeno"]` y «Empezar» `MJ_BOTON["primario"]` dentro del mismo `vbox` | `MJ_AREA_CX`, `MJ_AREA_Y + 40` |

Orden de dibujo dentro del área: cabecera izquierda → patrón → panel → destello rojo (solo el panel) → carriles → línea de meta → notas → cuenta → feedback → receptores → perfectos/combo → intro. Después, el marco dibuja la chibi, el globo y el aviso.

## Constantes

```
MIKU_BPM 76.9 (solo plan B) · MIKU_F2_MEDIA 8 · MIKU_USAR_TEMA True · M3_DEPURAR_TIC False
MIKU_PRE_BEATS 4 · MIKU_GAP_BEATS 4 · MIKU_PAUSA_GAP 0.35
M3_TIC "audio/sfx/hover.mp3" · M3_TIC_VOL 0.8 · M3_BAJAR_RELOJ False · M3_RELOJ_NIVEL 0.15
M3_CARRILES {"dificil": 4, "media": 3, "asistida": 3} · M3_TECLAS A S D F · M3_GUIA_INICIAL 8
M3_ANCHO_CARRIL 200 · M3_Y_TOP 276 · M3_Y_META 700 · M3_ALFA_FANTASMA 0.18
M3_COLOR_RELOJ "#C9C3D6" · M3_CAB_X 460 · M3_DER_X 1540
```

`MIKU_OFFSET` ya no existe. `MJ_PARAMS["m3"]` no ha cambiado. Ninguna de estas constantes está en `herramientas/generar_ui.py`.

## Decisiones

1. **El paso a la fase 2 es el momento emocional, sin avisos encima.** `MJM3.apagado()` vale 0 en la fase 1 y sube de forma lineal hasta 1 durante el hueco (de `t_cambio` a `t_f2`, 4 pulsos, unos 3 s). `color_vivo()` mezcla el azul de Miku un 75 % hacia el gris del reloj `#C9C3D6`. Lo usan los bordes del panel, la línea de meta, las notas, los receptores, las celdas del patrón, el motivo y el título.
   - El motivo ecualizador late con el pulso mientras suenan los audífonos y se queda quieto al 35 % cuando se apagan.
   - Lo único que sigue marcando es la línea de meta, al compás del reloj, y la casilla dorada `#FFE3A0` del patrón.
   - Durante el hueco, el título dice «Los audífonos se apagan.», el globo «…Solo queda el reloj.» y no sale ningún aviso del marco (`en_hueco()`).
2. **El feedback de ritmo es una excepción justificada junto a los carriles**, no `aviso=`. Sale en cada nota, más de una vez por segundo en difícil: en la píldora de y 1000 entraría y saldría sin parar, lejos de la línea donde mira el jugador, y taparía los avisos de verdad. Dura 0,3 s y siempre lleva texto: Perfecto, Bien, Fallo, Pronto, Tarde, ¡Sin nota!.
3. **`aviso=` queda para lo poco frecuente:** la recuperación por combo, con el texto «Combo: +N % de concentración».
4. **Los carriles y la barra «TOCA» no tienen `hover_sound` ni `activate_sound`, a propósito.** Un clic encima de la música o del tic mete un golpe que no es el del compás y ensucia el ritmo. Está anotado en la screen. «Empezar» y los botones de sincronía sí llevan sonido: son `cinta_boton`.
5. **PERFECTOS y COMBO** van a la derecha del panel, y **el patrón del compás** arriba a la derecha. Antes estaban en la columna, donde el globo tapaba el patrón justo en la fase 2.
6. **`rotulo_fase()` devuelve `(etiqueta, título)`.** `anim()` devuelve `"quieto"` en lugar de `"bob"` (el marco no tiene bucles en la columna); `"salto"` y `"tiembla"` al terminar no cambian.
7. **Textos cambiados por la nueva posición del patrón** (aprobado):
   - intro: «…y hay silencios; arriba a la derecha verás el patrón.»;
   - pista: «Las notas se desvanecen: guíate por el patrón del compás.»
8. **Mecánica sin cambios:** `MJ_PARAMS["m3"]`, patrones (`m3_fase1`, `m3_fase2`), carriles, combos, concentración, ventana y fases. La caída pasa de 430 a 424 px, con el mismo tiempo de caída.

## Para la sesión de animaciones de entrada y salida

- Bloques que pueden entrar por separado: la cabecera izquierda, el patrón (solo fase 2), el panel con carriles, línea y notas, los receptores, la columna derecha y la intro (un `frame`).
- **No retrases nada de lo que depende del reloj:** notas, línea de meta, cuenta y receptores se dibujan desde `vivo.t_juego()` en cada tick (`timer 0.02`). Si el panel entra con una animación, que sea solo en la intro → juego (cuando `estado` pasa a `"juego"` ya está sonando la música) o que no cambie la posición de la línea de meta.
- **El hueco entre fases ya tiene su animación** (`apagado()`, unos 3 s, ligada al reloj del juego). No le superpongas otra.
- El marco ya anima la cinta (0,35 s), el aviso y el globo; la chibi hace `salto` o `tiembla` una vez al terminar («fin»: 1,0 s ganado, 0,7 s perdido).

## Cómo probar

- **Partida normal:** `call mj_ejecutar("m3", "miku")` desde la consola (Shift+O), o `jump mj_probar_m3` (sin el boost de Nino = difícil; con `$ nino_rama_beat = "calida"` = media). Para asistida: modo «asistido» en los ajustes de `11_e6_debug.rpy`, o fallando en media. Si ya está ganado, borra los flags desde `11_e6_debug`.
- **Modo de depuración del tic:** en la consola, `$ M3_DEPURAR_TIC = True` y después `jump mj_probar_m3`. Suena el tic en cada nota de la fase 1, encima de la música. Para quitarlo, `$ M3_DEPURAR_TIC = False` o reinicia el juego.
- **Qué escuchar:**
  - el tic de cada nota en pulso cae justo encima del golpe de la música; el de una corchea, a mitad entre dos golpes;
  - sin deriva a lo largo de la fase 1, aunque la canción acelere hacia 78 BPM;
  - en el cambio, el primer tic del reloj llega en un pulso de la música y la fase 2 sigue a la misma velocidad que se oía.
- **Qué mirar:**
  - la línea de meta late con la música;
  - en el hueco, los colores se apagan hacia el gris en unos 3 s, el ecualizador deja de latir y no sale ningún aviso;
  - en la fase 2, la casilla dorada del patrón avanza con el tic.
- El tic de depuración se dispara con el mismo reloj que la música, así que el ajuste de latencia de la intro no lo mueve: ese ajuste solo corrige cuándo cuenta tu pulsación. El tic puede llegar hasta unos 20 ms tarde (se lanza en el tick de 0,02 s); un retraso pequeño e igual en todas las notas es eso, no el mapa. Un desfase que crece o cambia a lo largo de la canción sí sería del mapa.
