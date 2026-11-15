# N1′ · Compras para seis (Nino)

Estado final tras adaptarlo al marco común y corregir el lag (14/11/2026). Archivo: `game/10_mj_nino.rpy`.
Referencia del marco: `MARCO_COMUN.md`. **Si este documento y el código no coinciden, manda el código.**

## Zonas (pantalla 1920×1080) · distribución B «lista encima»

| Pieza | Posición / tamaño | Constante |
|---|---|---|
| Columna, cinta, HUD | Las del marco: INTENTO, TIEMPO (`vivo.restante()` / `vivo.total`) y LISTAS («n / 5»). En el sexto hueco el TIEMPO desaparece (se pasa `None`) | `mj_marco(..., vivo.lista, 5, t_rest, t_tot, "LISTAS")` |
| Chibi general (Nino) + globo | Columna: centro x 180, borde inferior del PNG en y 1090, zoom 1,0 | `MJ_CHIBI_X/Y`, a través de `mj_marco(chibi=, globo=, anim=)` |
| **Franja de la lista** | **x 440–1880, y 112–324** (1440×212). Fondo `n1_fondo(TARJETA_TONO[h], PETALO_COLOR[h])` de la hermana **de la lista**, no de Nino | `N1_LISTA_H = 212` |
| Bloque izquierdo | x 472: «LISTA n / 5» (`mj_etiqueta`, y 132), nombre (`mj_titulo` en su color, y 158), «RACHA ×n» (`mj_cifra` `#FFE3A0`, y 216, desde 2 y nunca en el sexto hueco), «6.º hueco de la cesta» (`mj_nota` `#FFE3A0`, y 272, casilla verde al elegir) | `N1_IZQ_X = 472` |
| Productos | Una celda por producto desde x 780, de 260 de ancho (4 → hasta x 1820), y 132: casilla 24 + EN `mj_cuerpo` + ES `mj_nota`. Los nombres largos («confectioners' sugar») ocupan 2 líneas | `N1_CELDA_X = 780`, `N1_CELDA_W = 260` |
| Memoria | En x 780: «MEMORIZA» (y 258) + barra de 1040×12 (y 290) que se vacía con ATL; o «Mirar lista (−C s)» 340×64 en y 244; o «MIRANDO…» en y 272 | `MJ_BOTON["secundario"]` |
| **Estantes** | **x 440–1880** (ventana de 1440). Fila de 144 de alto: etiqueta «ESTANTE A >>>» (`mj_etiqueta`) en y+0, cajas en y+32. Paso de 150. El bloque se centra en y 330–932: 4 filas → y 334/484/634/784 (fin 928); 3 filas → y 409/559/709 (fin 853) | `N1_VENTANA_W = 1440`, `N1_FILA_ALTO = 144`, `N1_FILA_H = 150`, `N1_ESTANTES_Y = 330`, `n1_fila_y0(n)` |
| Cajas | 272×112 (sin cambio). Separación horizontal = 1440 / cajas por fila (360 con 4, 720 con 2). EN `mj_cuerpo` blanco, ES `mj_nota`; «OK»/«NO» en `mj_nota` en (14, 4) | `N1_CAJA_W/H` |
| Latido de urgencia / destello de error | `Solid` de 1440×820 sobre el área, nunca sobre la columna | `n1_latido`, `n1_destello` |
| Cuenta atrás | Velo `#0B0712A0` sobre el área + cifra `mj_cifra_grande` centrada en (1160, 522) + «PREPÁRATE» (`mj_etiqueta` `#FFE3A0`, y 612) | — |
| Avisos | Franja del marco, centro (1160, 1000) | `aviso=vivo.aviso_vivo()`, `aviso_tipo=vivo.aviso_tipo` |
| Intro | Panel de 1180 de ancho centrado en (1160, 522), alto automático (máx. 820) | `MJ_AREA_CX` |
| **Sexto hueco** | Franja de la lista (lista 5, todo marcado) + «Queda sitio para una cosa más en la cesta.» (`mj_aviso_texto`, y 392) + tres opciones de 820×110 desde y 470 (hasta y 844), centradas en x 1160 | — |

Orden de dibujo dentro del área: latido → destello → intro **o** (franja → estantes o sexto → cuenta atrás). Después, el marco dibuja la chibi, el globo y el aviso.

## Rendimiento

Medido con un arnés temporal (ya borrado): ventana de 1536×864, gl2, AMD Radeon integrada, vsync a 60, 8 s en compras y sin clics. Para verlo en el juego: **F3** (contador de Ren'Py en modo desarrollador).

| | Asistida antes → después | Media antes → después | **Difícil antes → después** |
|---|---|---|---|
| fps | 22,6 → 21,1 (*) | 18,9 → **49,4** | 15,1 → **42,0** |
| ms por fotograma, media · p95 | 44 · 52 → 46 · 207 (*) | 53 · 59 → 20 · 26 | 66 · 77 → **24 · 30** |
| Fotogramas sin reevaluar la screen | — | 19 ms | 22 ms |
| Reevaluaciones de la screen por segundo | 22,5 | 18,9 → 1,4 | 15,1 → **1,5** |
| Coste de una reevaluación (fotograma) | — | 59 ms | 76 ms |
| Ticks de lógica por segundo (objetivo 30) | 22 → 30 | 19 → 27 | 15 → 23 |
| Salto de la fila más rápida por fotograma | — | 3,8 → 1,4 px | 13,7 → **4,8 px** |

(*) En asistida nada se mueve: Ren'Py solo redibuja cuando algo cambia. Por eso hay pocos fotogramas y el p95 es alto, y no es lag. La lógica va a 30 ticks/s.

**Causa raíz (confirmada midiendo):** `timer 0.033 … Function(vivo.tick)` reiniciaba la interacción en cada tick, así que cada fotograma reevaluaba, maquetaba y redibujaba la screen entera (fotogramas = ticks). Además, las cajas se movían a saltos de tick.

**Corrección:**
1. La cinta se mueve con `n1_cinta(dx, dur)`, un ATL por fila: `xoffset` lineal de un periodo, en bucle, con cada caja duplicada a un periodo de distancia.
2. El timer va con `_update_screens=False`, y `MJN1.tick()` solo llama a `renpy.restart_interaction()` si cambia `MJN1.firma()` (segundo entero del reloj, fase, cuenta, racha, memoria visible, traducción visible, aviso, globo, estados de las cajas…).
3. Lo que cambia de forma continua lo anima el motor, sin reevaluar la screen: la barra de memoria (`n1_vaciar`), el fundido de la traducción (`n1_trad` / `n1_oculto`), el latido (`n1_latido`) y el destello (`n1_destello`).
4. Los fondos de caja se construyen una vez por par de colores (`n1_fondo`), así que la screen reutiliza las cajas.
5. El cronómetro grande con décimas, que obligaba a 10 reevaluaciones por segundo, ya no existe.

**Sin resolver:**
- En difícil no se llega a 60 fps: un fotograma sin reevaluación cuesta unos 21 ms, sobre todo de dibujo en GPU (32 cajas visibles con 2 `Frame` teñidos cada una, más el fondo, el velo y la columna). La cinta se ve continua (4,8 px por fotograma), pero no a 60.
- Cada reevaluación (unas 1,5 por segundo, más una por clic) cuesta 60–76 ms: un tirón breve, una vez por segundo.
- Siguiente paso posible, sin probar: aplanar el fondo de cada estado de caja en una textura (`Flatten`) para reducir quads en la GPU.

## Decisiones

1. **Distribución B** (la eligió el usuario): las cajas conservan su tamaño de 272×112 y una caja tarda 7,1 s en cruzar la ventana en difícil (5,1 s con la opción A). La lista va arriba, en el color de la hermana que la pidió.
2. **Mecánica sin cambios:** `MJ_PARAMS["n1"]`, velocidad `deriva × (1 + 0,15·fi)`, sentido (pares →, impares ←), penalización, memoria, «mirar», retardo de la traducción y racha. Cambio menor aceptado: la cinta **no se congela** en la pausa de 0,7 s entre listas, en «perdiendo» ni durante la cuenta atrás (antes `t_deriva` se paraba). Las cajas no se pueden elegir fuera de `compras`.
3. **Un solo cronómetro**, el del marco, en segundos enteros. Se quitaron el reloj grande de y 56 y `pulso()`.
4. **Avisos** (`MJN1.avisar(texto, tipo)`, 1,2 s, `N1_AVISO_S`):
   - error: «Esa no es · −P s» (`"mal"`);
   - mirar: «Miras la lista · −C s» (`"info"`);
   - racha: «Racha ×n · +B s» (`"bien"`).
   
   Las cifras van con coma (`n1_seg`). En el sexto hueco no se muestra ningún aviso (`aviso_vivo()`).
5. **Sexto hueco:** es el momento emocional. Sin cinta, sin reloj (el HUD lo oculta), sin racha, sin avisos y sin latido rojo. Solo la lista de Nino completa, la frase y las tres opciones de `MJ_N1_SEXTO`, sin cambios en sentido, textos ni claves.
6. **La traducción ocupa su sitio desde el principio** (con alpha 0 hasta que asoma), para que el inglés no salte al aparecer el español.
7. Las cajas y las opciones del sexto hueco llevan `hover_sound` + `activate_sound`. «Mirar lista» y «Empezar» son `cinta_boton` con `MJ_BOTON`.
8. Ninguna constante de N1 está en `herramientas/generar_ui.py`.

## Para la sesión de animaciones de entrada y salida

- Bloques que pueden entrar por separado: la franja (`screen mj_n1_lista`), los estantes (`mj_n1_estantes`, una fila por `fixed`) y el sexto hueco (`mj_n1_sexto`).
- **No envuelvas la cinta en otro transform que reinicie su ATL:** `n1_cinta` conserva la fase entre reevaluaciones porque recibe siempre los mismos argumentos. Si una fila entra con una animación, pon el transform en el `fixed` exterior (el que lleva `clipping True`), no en el que se desplaza.
- Todo lo que dependa del tiempo tiene que ir en ATL o en `MJN1.firma()`. Si añades algo continuo dentro de la screen con un valor de Python, solo se actualizará una vez por segundo.
- La intro ya entra con `n1_entrada` (0,3 s). El marco anima la cinta del título, el aviso y el globo.
- Tiempos que no se pueden alargar sin tocar la mecánica: cuenta atrás 3 × 0,7 s (`N1_CUENTA_S`), pausa entre listas 0,7 s, «perdiendo» 1,6 s y «fin» 1,5 s (después se devuelve el resultado).

## Cómo probar

- `call mj_ejecutar("n1", "nino")` desde la consola (Shift+O), o `jump mj_probar_n1` (sin el boost = difícil; con boost = media). Para asistida: con el boost y modo «asistido» en los ajustes de `11_e6_debug.rpy`, o fallando en media.
- **Difícil:** pulsa F3 y mira la cinta de la fila D (la más rápida, ←). Tiene que deslizarse continua, sin saltos de una caja. Haz clic en una caja en movimiento y comprueba que se marca esa. Falla una: queda «NO», bloqueada y sin hover, el área destella en rojo y el aviso dice «Esa no es · −6 s». A los 5 s la lista se convierte en máscaras y aparece «Mirar lista (−2 s)».
- **Media:** la traducción aparece a los 0,8 s con un fundido. La barra MEMORIZA se vacía en 12 s.
- **Asistida:** cajas quietas, traducción inmediata y sin memoria.
- **Sexto hueco:** sin reloj ni racha en pantalla. Al elegir, la casilla «6.º hueco» se pone verde y a los 1,5 s se devuelve «ganado» con `datos["sexto"]`.
