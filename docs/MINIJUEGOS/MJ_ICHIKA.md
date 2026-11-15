# I1 · La máscara se cansa (Ichika)

Estado final tras adaptarlo al marco común (14/11/2026). Archivo: `game/10_mj_ichika.rpy`.
Referencia del marco: `MARCO_COMUN.md`. **Si este documento y el código no coinciden, manda el código.**

## Zonas (pantalla 1920×1080)

| Pieza | Posición / tamaño | Constante |
|---|---|---|
| Columna, cinta, HUD | Las del marco. El HUD solo muestra INTENTO y LÍNEAS («i / n») | `mj_marco(..., vivo.i, vivo.n, ..., "LÍNEAS")` |
| Chibi general (Ichika) + globo | Columna: centro x 180, borde inferior del PNG en y 1090, zoom 1,0 | `MJ_CHIBI_X/Y`, a través de `mj_marco(chibi=, globo=, anim=)` |
| Bloque de juego | 1360 de ancho, x 480–1840, centrado en `MJ_AREA_CX` | `I1_ANCHO`, `I1_X` |
| Columnas | Dos de 660 + 40 de hueco: izquierda x 480, derecha x 1180 | `I1_TARJETA_W`, `I1_X2` |
| **Barras MÁSCARA / ENERGÍA** | y 176; fila de cifra (34) + barra de **28 px** + nota → hasta y ≈ 290 | `I1_BARRAS_Y`, `I1_BARRA_H`, screen `i1_medidor` |
| Reloj de la línea | y 328: «TIEMPO PARA ELEGIR» + barra de 1360 (12 px). En la última línea, el texto «ÚLTIMA LÍNEA · SIN PRISA · SOLO PUEDE SER SINCERA» | `I1_RELOJ_Y` |
| Tarjetas | y 410–740, 660×330 cada una. EL PAPEL a la izquierda, LO QUE SIENTE a la derecha | `I1_TARJETAS_Y`, `I1_TARJETA_H` |
| Consejo | Centrado en x 1160, y 774 (`mj_cuerpo`) | `I1_CONSEJO_Y` |
| Avisos | Franja del marco, centro (1160, 1000) | `aviso=msg[0], aviso_tipo=msg[1]` |
| Intro | Velo solo sobre el área; panel de 1360 de ancho centrado en (1160, 522) | `MJ_AREA_*` |

Orden de dibujo dentro del área: barras → reloj → EL PAPEL → LO QUE SIENTE → consejo → intro. Después, el marco dibuja la chibi, el globo y el aviso.

## Las barras (el corazón)

`screen i1_medidor(etiqueta, valor, cifra, cambio, color_cambio, color, nota, zona=None, marca=None)`:
- Arriba: etiqueta (`mj_etiqueta`) y, a la derecha, la cifra (`mj_cifra`). En `resp` y `fin`, el cambio con signo va **junto a la cifra**: verde si ayuda, rojo o naranja si cuesta.
- **MÁSCARA:**
  - fondo del tramo 75–100 teñido `#FF8A8A40` (la zona de «en blanco», `I1_MASCARA_PELIGRO`);
  - relleno del color de Ichika, que pasa a `#FF8A8A` desde 75.
- **ENERGÍA:**
  - **marca blanca de 3 px en el coste de una sincera** (`costo_sincera()`); no aparece en la intro ni en la última línea, que es gratis;
  - relleno `#8FD3FF`, o `#FFB38A` si no llega al coste;
  - la nota cambia en la última línea.

## Decisiones

1. **Tarjetas una al lado de la otra** (aprobado): elección binaria y simétrica. La línea va en `mj_aviso_texto` (34, la frase grande del marco). La más larga («Pregúntame lo que quieras. Contestaré con un chiste.») ocupa 2 líneas y cabe.
2. **Sonido:**
   - EL PAPEL: `hover_sound` + `activate_sound` (clic al tocar).
   - LO QUE SIENTE: `hover_sound` y **sin `activate_sound`**. Ese sonaría al soltar, que es tarde si ya se resolvió, o un falso acierto si se soltó antes.
   - El clic suena en `MJI1.resolver("sincera")` (`renpy.sound.play(audio.sfx_click)`), justo cuando se completa la sincera. Mientras se mantiene no suena nada.
   - La tecla A no suena (no es un botón); al mantener S, suena al completarse.
3. **Avisos** (`mensaje()` → `(texto, tipo)`):
   - `"bien"`: «Silencio. Y se oyó.» y «Esta vez no hubo máscara.»
   - `"info"`: «Aplauso. La sonrisa pesa un poco más.» y «Mantén un poco más.»
   - `"mal"`: improvisó, energía desperdiciada, «Se quedó en blanco.» y «Sin fuerzas. Actúa para recuperar energía.»
4. **Consejo** (`consejo()`): es una instrucción fija, así que va en el área como `mj_cuerpo`, no como aviso.
5. Desaparecen el texto suelto de y 865 y los cambios en (1320, 545): ahora salen en las barras.
6. Mecánica, `MJ_PARAMS["i1"]` y tiempos sin cambios.

## Para la sesión de animaciones de entrada y salida

- Bloques que pueden entrar por separado: las barras (`fixed` en `I1_X, I1_BARRAS_Y`), el reloj, las dos tarjetas y el consejo.
- La barra de mantener y el `timer 0.02` son mecánica: no los retrases.
- Cuando la máscara llega a 100 (`fin`, 0,9 s) o se gana (`fin`, 1,1 s), el marco ya muestra el aviso. La chibi hace `salto` o `tiembla` una sola vez.

## Cómo probar

- `call mj_ejecutar("i1", "ichika")` desde la consola, o `jump mj_probar_i1`. El nivel sigue al boost de Nino y al modo del menú de ajustes de `11_e6_debug.rpy`, como en Y2.
