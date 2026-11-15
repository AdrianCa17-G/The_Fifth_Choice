# It1 · Cadena de conversiones (Itsuki)

Estado final tras adaptarlo al marco común (14/11/2026). Archivo: `game/10_mj_itsuki.rpy`.
Referencia del marco: `MARCO_COMUN.md`. **Si este documento y el código no coinciden, manda el código.**

## Zonas (pantalla 1920×1080)

| Pieza | Posición / tamaño | Constante |
|---|---|---|
| Columna, cinta, HUD | Las del marco: INTENTO, TIEMPO (recurso, `vivo.restante()` / `vivo.total`) y PASOS | `mj_marco(..., hechas, vivo.n, t_rest, t_tot, "PASOS")` |
| Chibi general (Itsuki) + globo | Columna: centro x 180, borde inferior del PNG en y 1090, zoom 1,0. La expresión `"mano"` usa `neutral` mientras falte `itsuki_mano.png` | `MJ_CHIBI_X/Y`, a través de `mj_marco(chibi=, globo=, anim=)` |
| **Cuaderno abierto** | **x 470–1850, y 128–848** (1380×720) | `IT1_CUAD_X/Y/W/H` |
| Página izquierda (tu hoja) | x 470–1160; el texto empieza en x 580 (después del margen rojo, en x 554) | `IT1_PAG_W` |
| Lomo | Centro x 1160: sombra de 36 px + costura de 2 px | — |
| Página derecha (paso actual) | El texto empieza en x 1210; centro de la página x 1505 | `IT1_CUAD_X + IT1_PAG_W + 50` |
| Renglones | Cada 44 px desde la fila 3 (y 260), azul `#8FB3D966` | `IT1_RENGLON` |
| Filas de la hoja | 550×72 desde y 268 (hasta 5 → hasta y ≈ 670) | `it1_fila` |
| Opciones | Rejilla 2×2 de fichas de 290×100, 20 de hueco, desde (1210, 396) | `IT1_OPCION` |
| «Entregar» (revisión) | 420×80, centrado en x 1505, y 528 | `MJ_BOTON["primario"]` |
| Pie (fuera del cuaderno) | «Levantar la mano» / «Sin ayuda» de 340×64 en (470, 868), hasta y 932; nota de la calculadora en (850, 886) | `IT1_PIE_Y`, `MJ_BOTON["secundario"]` |
| Avisos | Franja del marco, centro (1160, 1000) | `vivo.aviso_marco()` |
| Intro | Caja de 1160×740 centrada en x 1160, y 152–892 | `MJ_AREA_CX`, `MJ_AREA_Y + 40` |

Orden de dibujo dentro del área:
1. el cuaderno: sombra → borde → papel → renglones → margen → lomo;
2. la página izquierda: título, enunciado y filas;
3. la página derecha: «arrastrado» y el paso actual con sus opciones, o la revisión;
4. el pie, fuera del cuaderno.

Después, el marco dibuja la chibi, el globo y el aviso.

## Tinta (Klee One, solo en el cuaderno y la nota)

| Estilo | Tamaño | Color | Uso |
|---|---|---|---|
| `it1_tinta` | 26 | `#2F2A44` | enunciado, valores, «Llevas», opciones |
| `it1_tinta_grande` | 44 | `#2F2A44` | unidades del paso, resultado final |
| `it1_tinta_nota` | 20 | `#2F2A4499` (lápiz) | «Tu hoja…», «arrastrado», «(¿raro?)», nota de la calculadora (en `#FFE3A0` con contorno, fuera del papel) |
| `it1_rotulo` | 22, kerning 3 | `#B94A4A` (rojo) | «CUADERNO DE CIENCIAS · …», «PASO n DE N», «REVISIÓN», «← mira aquí», «(¡ojo!)» |

Fuera del cuaderno se usan los estilos `mj_*`: el título, el texto y las reglas de la intro.

## Decisiones

1. **El papel es opaco y está hecho con `Solid`** (sombra, borde `#D9CBB0` y papel `#F6EEDC`). `opcion_neutra.png` es translúcido y tiene degradado, y teñido se veía gris. Por lo mismo, las opciones son fichas planas (`it1_ficha`): papel claro `#FBF6EA` con borde de 3 px del color de Itsuki; en hover, todo de su color y el número en blanco.
2. **La pista del profesor:**
   - va al aviso «info» durante `IT1_T_PISTA` = 4 s;
   - **la fila señalada queda marcada en la hoja** (fondo de marcador `#FFE3A0CC` + «← mira aquí») hasta que se rehace;
   - el aviso va en la franja, así que no tapa la fila;
   - si a la vez hay «No cuadra.» (`"mal"`), manda «No cuadra.».
3. La equivalencia va sobre un trazo de marcador amarillo, y el número arrastrado, a lápiz en la esquina de la página derecha.
4. **«Sin ayuda»** es `cinta_boton(..., activo=False)`: aspecto deshabilitado estándar, ya no un `Solid`.
5. Las filas de la hoja tienen `hover_sound` + `activate_sound` (se tocan para rehacer); las opciones también.
6. Mecánica, `MJ_PARAMS["it1"]`, tiempos e `it1_frase()` sin cambios.

## Para la sesión de animaciones de entrada y salida

- El cuaderno es una sola screen (`it1_cuaderno`): puede entrar como un bloque, por ejemplo abriéndose desde el lomo (x 1160).
- El contenido de las páginas (`it1_juego`) se dibuja encima con coordenadas absolutas. Si se anima el cuaderno, conviene envolver el `use it1_cuaderno()` y el contenido en el mismo contenedor.
- Al elegir una opción, la fila nueva aparece en la hoja y las opciones se regeneran. Si se anima la escritura de la fila, no puede retrasar la entrada.
- En `fin` (1,6 s) y en `perdiendo` (1,6 s), el marco ya muestra la reacción de la chibi.

## Cómo probar

- `call mj_ejecutar("it1", "itsuki")` desde la consola, o `jump mj_probar_it1` (sin el boost = difícil; con boost = media).
- Para asistida: con el boost y modo «asistido» en los ajustes de `11_e6_debug.rpy`.
