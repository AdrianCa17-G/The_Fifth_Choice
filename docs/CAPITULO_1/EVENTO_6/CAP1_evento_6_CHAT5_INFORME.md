# Chat 5 · Informe de cierre — minijuegos Y2, N1′ e It1

> **Ruta en el repo:** `docs/CAPITULO_1/EVENTO_6/CAP1_evento_6_CHAT5_INFORME.md`
> **Cierre del chat 5.** Entregado: cuatro `.rpy` en `game/`. **Nada se ha ejecutado en Ren'Py.**

---

## 1. Qué se entregó y qué NO

| Archivo | Contenido | Estado |
|---|---|---|
| `game/10_mj_chibi.rpy` | Módulo compartido: chibis (con repuesto), `MJGlobo`, tablas de líneas, screens `mj_globo`, `mj_chibi_vista`, `mj_retrato` | Escrito, sin ejecutar |
| `game/10_mj_yotsuba.rpy` | Y2 · Relevo (`"y2"`) + `label mj_probar_y2` | Escrito, sin ejecutar |
| `game/10_mj_nino.rpy` | N1′ · Compras para seis (`"n1"`) + `label mj_probar_n1` | Escrito, sin ejecutar |
| `game/10_mj_itsuki.rpy` | It1 · Conversiones (`"it1"`) + `it1_frase()` + `label mj_probar_it1` | Escrito, sin ejecutar |

**No existe todavía, aunque lo planeé:** los PNG de chibis (ni siquiera los de repuesto), `generar_chibis_placeholder.py` y `normalizar_chibi.py`. Sin PNG, `mj_chibi()` cae sola a una flor del color de la hermana con su inicial: los minijuegos funcionan, pero sin chibis. **No pude probar la lógica**: mi arnés de prueba en Python falló por un fallo del propio arnés (no del código) y no llegó a correr. Tampoco se ha hecho la prueba de humo del motor (Esc, guardar/cargar, retroceder, saltar).

## 2. Para enchufarlo (cambio fuera de mi lista)

En `10_minijuegos.rpy`, `E6_MJ_JUEGO` sigue apuntando a `"prueba"`. Cambiar solo estas tres claves: `yotsuba: "y2"`, `nino: "n1"`, `itsuki: "it1"`. Para probar suelto: `jump mj_probar_y2` / `mj_probar_n1` / `mj_probar_it1` desde la consola (Shift+O).

**Opcional (fallos en globo).** `MJ_FALLO_EN_GLOBO = False` por defecto: el marco dice la línea de `MJ_FALLOS` con `renpy.say` y el globo usa reacciones propias. Para que la línea de fallo salga en el globo hay que poner `True` **y** añadir en `mj_linea_fallo()` del marco un `return` temprano cuando esa constante sea `True`; sin el parche se diría dos veces.

## 3. Qué calibrar jugando (por orden de importancia)

**Meta (del análisis §5.4):** difícil 55–65 % de victorias al primer intento; media 80–90 %; máximo esperado 2 intentos. Es la regla que hay que medir con 2–3 jugadores ajenos y el equipo más lento.

| Minijuego | Parámetro | Dónde | Qué vigilar |
|---|---|---|---|
| Y2 | `ventana` (0,12 / 0,26 / 0,40 s) | `MJ_PARAMS["y2"]` | El que más pesa. Con `testigos` = 1 en difícil un solo error pierde el intento: mi estimación (sin medir) es ≈ 50 % al primer intento |
| Y2 | `Y2_VEL_BASE` (0,55 tramos/s) y rango de la marca (0,55–0,80) | `10_mj_yotsuba.rpy` | Si la marca llega muy pronto o muy tarde se pierde la lectura visual |
| Y2 | `testigos` | `MJ_PARAMS["y2"]` | Lo interpreté como «vidas»: tras un error el tramo se repite mientras queden. Confirmar que es lo que querías |
| N1′ | `tiempo_total` (75 / 105 / 140 s) | `MJ_PARAMS["n1"]` | 15 productos + 5 pausas de 0,7 s. 75 s son ~4,5 s por producto |
| N1′ | `retardo_traduccion` y `penalizacion` | ídem | Con 1,4 s el que no sabe inglés espera; con −6 s por error se castiga rápido |
| N1′ | tiempo al reanudar | `MJN1.__init__` | Se reduce en proporción a las listas que faltan, mínimo 40 % |
| It1 | `tiempo` (55 / 80 / 110 s) y `intentos` (entregas erróneas) | `MJ_PARAMS["it1"]` | 5 pasos con cuatro opciones y una entrega en 55 s es ajustado |
| It1 | `ayuda_costo` (10 / 5 / 0 s) y `ayuda_usos` | ídem | Por intento, no acumulado |
| It1 | `IT1_PLAUS_UMBRAL` (1,9) | `10_mj_itsuki.rpy` | Con 1,9 la marca «(¿raro?)» solo avisa de errores ≥ 100×; más bajo delataría casi todas las opciones erróneas |
| Todos | `MJ_GLOBO_DURACION` (2,2 s) | `10_mj_chibi.rpy` | Si los globos tapan o se pisan |

## 4. Decisiones que registrar

**Cambios al registro de `PLAN_CHATS_EVENTO_6.md` §1.C (pegar tal cual):**

| ID | Decisión | Estado |
|---|---|---|
| P-20 | **Móvil: se adapta, no se excluye.** Los tres minijuegos se juegan solo con clic/toque (Y2: un toque en cualquier sitio; N1′ e It1: botones grandes), sin teclado. Mantienen `MJ_MODO_TACTIL` y la opción «saltar». Lo que sigue sin resolverse es la legibilidad en pantallas pequeñas (textos de 19–20 px) | DECIDIDO — pendiente de comprobar en un móvil real |
| P-24 (nueva) | **Chibis en los minijuegos.** Un chibi protagonista por minijuego con escalera de expresiones (neutral → animo → esfuerzo → feliz; triste al fallar) y globos de texto con líneas aleatorias por evento. Y2 usa además a las cinco como corredoras | DECIDIDO por Adrian; el arte va en la ficha del chat 7 |
| P-25 (nueva) | **Sexto hueco de N1′.** Tres opciones sin respuesta correcta (`celebrar` / `consolar` / `vacio`), guardada en `e6_mj["nino"]["datos"]["sexto"]`. El guion del chat 4 decide qué línea cuelga de cada una | DECIDIDO — el significado exacto del «sexto» es mío |
| P-26 (nueva) | **It1: frase A/B.** `it1_frase()` devuelve `"A"` si pidió ayuda o se saltó el minijuego; `"B"` si resolvió sola | DECIDIDO — confirmar que el salto debe dar la frase A |

**Cambios al mapa de chats §2:** marcar el chat 5 como hecho **con reservas** (sin probar en Ren'Py). El chat 7 gana una tarea: los chibis. El chat 6 puede reutilizar `10_mj_chibi.rpy` y debe escribir las líneas de globo de Ichika y Miku en `MJ_GLOBOS`.

**Ficha del chat 7 · chibis (para actualizar):**
- 25 imágenes: 5 hermanas × `neutral`, `animo`, `esfuerzo`, `triste`, `feliz`, más `itsuki_mano` (opcional).
- Archivo: `game/images/chibis/<hermana>_<expresion>.png`, 512×512, RGBA, pies en la fila ~496, eje en el centro.
- Generar en vertical 768×1024, fondo blanco liso, solo LoRA de personaje (0,6–0,8; si con «chibi» el LoRA pierde el parecido, bajar), todo en positivo. La silueta decide: feliz con brazos arriba, triste encogida, esfuerzo con cuerpo inclinado.
- **No usar** el chibi de tu cuarta imagen (lleva marca «SAMPLE», es arte oficial): vale solo como referencia de proporciones. Las imágenes 1–3 también son solo referencia.
- Falta un `normalizar_chibi.py` (recortar al contenido y centrar en 512×512 con una escala común por hermana): se puede escribir en el chat 7.

## 5. Resumen

1. Escritos los tres minijuegos (Y2, N1′, It1) y un módulo común de chibis y globos, todos con parámetros en `MJ_PARAMS` y registrados en `MJ_REGISTRO`.
2. La propuesta de chibis es viable y encaja con la regla de silueta; su coste real es arte: 25–26 imágenes en el chat 7.
3. Todo es de clic/toque, así que la adaptación a móvil no exige rehacer nada; falta comprobar tamaños de texto.
4. Falta lo verificable: ninguna línea se ha ejecutado, no hay PNG de chibis y no existen los dos scripts de arte previstos.
5. Para activarlos hay que tocar tres claves de `E6_MJ_JUEGO` en el marco.

## 6. Riesgos detectados

| # | Riesgo | Gravedad | Qué hacer |
|---|---|---|---|
| R1 | **Código sin ejecutar.** Puede haber errores de compilación o de motor | Alta | Primera tarea del siguiente chat: `lint` y `jump mj_probar_*` |
| R2 | **Error de sintaxis probable en `10_mj_itsuki.rpy`:** `text "CUADERNO DE CIENCIAS · " + vivo.cadena["titulo"].upper():` lleva una suma sin paréntesis tras un `text`, y Ren'Py suele rechazarlo. Arreglo: envolver toda la expresión en paréntesis | Alta (fallo seguro al compilar si ocurre) | Corregir ahora o en el chat 10; no lo he tocado porque pediste no escribir más código |
| R3 | Supuestos de motor sin comprobar: que `Function(...)` que devuelve un diccionario cierre la interacción (lo copié del marco), `add "bg_*" fit "cover"`, `frame` con `background Fixed(...)`, alfa por color hexadecimal en `text`, `Transform(Solid(...), rotate=...)` | Media | Prueba de humo del chat 1 + los labels de prueba |
| R4 | Sin PNG de chibis solo se ve una flor con inicial, y los globos salen sobre ella | Media | Decidir si hace falta un juego de repuesto antes del chat 7 |
| R5 | Estado dentro de pantalla (`default vivo = …`): al cargar una partida a mitad el intento reinicia desde el punto de control; Esc pausa pero el reloj propio recorta el hueco a 0,12 s | Media | Verificar con guardar/cargar y Esc |
| R6 | Rollback y skip dependen de lo que ya hace el marco; mis pantallas solo suman `key "K_RETURN"` anulado en N1′ e It1 | Media | Prueba de humo |
| R7 | Dificultad: en difícil Y2 con un solo testigo puede ser frustrante; la asistencia adaptativa la maneja el marco | Media | Medir; si hace falta `testigos` = 2 en difícil |
| R8 | Legibilidad en móvil: traducciones de 19–20 px, botones de 80 px de alto | Media | Probar en un móvil; subir tamaños si no se lee |
| R9 | It1: contenido corto (3 cadenas, 5 pasos) y números con separador de miles con punto (`3.000`), que un lector no hispano puede leer como decimal | Baja | Aceptable para el público; revisar si se traduce |
| R10 | El sexto hueco de N1′ y la frase A/B de It1 dependen de decisiones del guion (P-25, P-26) | Baja | Confirmar en el chat 4 |
| R11 | La lógica de «testigos = vidas», «entregas erróneas» y «ayuda por intento» es interpretación mía de la tabla §5.4 | Baja | Confirmar con el análisis |
