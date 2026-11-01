# Plan de chats — Evento 6 (cierre del Capítulo 1)

> **Ruta en el repo:** `docs/CAPITULO_1/EVENTO_6/PLAN_CHATS_EVENTO_6.md`
> **Análisis que lo respalda:** `docs/CAPITULO_1/EVENTO_6/ANALISIS_EVENTO_6.md`
> **Fecha:** 31/10/2026.

**Cómo usarlo.**
1. Responde las decisiones `P-xx` que bloquean el primer chat y **actualiza el §1.C** (cambia `PROPUESTA` por `DECIDIDO` o por tu versión).
2. Haz un commit antes de abrir cada chat.
3. Pega el prompt del chat correspondiente (cada uno es autosuficiente y remite a los dos archivos por ruta).
4. Al terminar un chat, sube sus archivos al repo y marca el chat como hecho en §2.

---

## 1. REGISTRO DE DECISIONES

### 1.A Decididas por ti (no se debaten)

| ID | Decisión |
|---|---|
| D-01 | El Evento 6 es el cierre **del capítulo**, no del juego. Puede dejar huecos abiertos a propósito y ser mucho más largo que los demás movimientos; debe ser perfecto. |
| D-02 | **Activación:** solo si los hubs llevaron a un cierre «sigue»: aviso superado, sin aviso con clima mixto, o sin aviso con clima bueno. El resto termina en despido (ya implementado). |
| D-03 | **Premisa:** cada hermana es una parte del estudiante perfecto. En E6 ocurren los exámenes y se muestra el mes de estudio. **Todas aprueban; solo sacan 100 en su asignatura fuerte.** El jugador debe sentir que lo logró por sus decisiones. Hay una **escena final con las cinco aprobando**. |
| D-04 | **Desarrollo de personaje real para las cinco**, incluidas las que el jugador no visitó. |
| D-05 | **CG nuevos.** BGM y SFX reutilizados salvo que el guion pida nuevos. |
| D-06 | **Minijuegos solo si MC fue cálido con esa hermana.** En tibia o fría el juego sigue sin minijuego. |
| D-07 | **Secuencia del minijuego:** el narrador nombra a la chica → CG con su monólogo interno (piensa en MC, en lo que hizo, en por qué está ahí y lo que ha logrado) → el monólogo activa el minijuego → el minijuego muestra su desarrollo: deja atrás su miedo y dice una frase que la cambia. |
| D-08 | **Se puede perder y se repite hasta ganar.** (La política exacta de ayudas se decide en P-07). |
| D-09 | **Dificultad base: difícil.** Si MC fue cálido con Nino **en su beat** (`nino_rama_beat == "calida"`), baja a media tirando a fácil. Es la recompensa de ese beat. |
| D-10 | **Materias fuertes (verificadas):** Ichika matemáticas, Nino inglés, Miku sociales, Yotsuba japonés, Itsuki ciencias. Orden de exámenes L→V del Final B: Yotsuba, Ichika, Nino, Itsuki, Miku. |
| D-11 | **Procedimiento:** el análisis y el plan viven en dos `.md`; el trabajo se hace en chats nuevos, independientes y con un prompt autosuficiente. No tocar `README.md` ni `CAP1.md` hasta cerrar todo el Capítulo 1 (se actualizan en bloque al final). |
| D-12 | **Convenciones de entrega:** respuestas en español; código **completo y copiable**, sin esqueletos parciales ni atajos tipo ternario (estructuras explícitas); todo `show` con su posición; el protagonista nunca muestra rostro. |

### 1.B Hechos verificados en el repo

| ID | Hecho |
|---|---|
| F-01 | La entrada es `jump evento_6` (pila de `call` vacía). El label **no existe aún**. No hay destino posterior (`cap2_inicio` es un stub a crear). |
| F-02 | `estado_entrada`: `superado` si `maruo_ultimatum`; si no, `bueno` si `clima_cap1 == "buena"`; si no, `mixto`. |
| F-03 | Sobreviven 20 de 27 combinaciones de rama. Siempre ≤ 1 hermana fría, ≤ 3 cálidas, 3 visitadas y 2 no visitadas. |
| F-04 | Minijuegos por partida: 0 en 4 combinaciones, 1 en 9, 2 en 6, 3 en 1. |
| F-05 | `rama_de(h)` devuelve `None` si no visitada. `nino_rama_beat` es independiente de la rama de hub de Nino. |
| F-06 | Los CG `*_fracaso` son del Final B, no de un examen anterior. |
| F-07 | Las no visitadas tienen una `queja_*` (viernes) y, solo Nino e Itsuki, un beat fijo. |
| F-08 | `interconexion_6` ya consumió la última sesión, la visita de Maruo (solo con ultimátum), el chat y las puertas. E6 arranca el **lunes**. |
| F-09 | Puntos reales en el código: hub cálida +3, tibia +1, fría 0; `beat_Nino` cálida +1. |
| F-10 | `hub_visitadas` mantiene el orden y no se reinicia. `ui_escena("beat", h, lugar)` tiñe el HUD con el color de la hermana. |

### 1.C Propuestas del análisis (confirmar o corregir)

Estado inicial: `PROPUESTA`. Al responder, cambia a `DECIDIDO` (y anota tu corrección).

| ID | Propuesta | Estado | Bloquea chats |
|---|---|---|---|
| P-01 | Los cinco tienen bloque completo (nombre, CG, monólogo); minijuego solo en cálida. | PROPUESTA | 1, 2, 3, 4 |
| P-02 | Modelo **núcleo + capas** y **focos por estado** (cálida: lo que cambió; tibia: tarea y duda; fría: herida como método; no visitada: la espera). | PROPUESTA | 1, 2, 3, 4 |
| P-03 | Exámenes **en el aula con MC presente**, espejo del Final B. | PROPUESTA | 2, 3, 4, 7 |
| P-04 | Orden: L→V → Maruo → las cinco → casa → cuarto/chat/libreta. Última línea sin resolver. | PROPUESTA | 2 |
| P-05 | Frases de cambio y variantes (cortada / cerrada / espera), según tabla del análisis §2. | PROPUESTA | 3, 4 |
| P-06 | Minijuegos: **Y2** relevo, **I1′** la máscara se cansa, **N1′** compras para seis, **It1** conversiones + levantar la mano, **M3** el compás. | PROPUESTA | 1, 5, 6 |
| P-07 | Fallos: puntos de control por fase, líneas de fallo con carácter, asistencia adaptativa (paso a mitad tras 2 fallos, completo tras 4, «Que lo haga ella» tras 6), saltar tras ganar una vez, opción «Asistencia». | PROPUESTA | 1, 5, 6 |
| P-08 | Dificultad: tablas del análisis §5.4; tres niveles (difícil / media / asistida); el boost de Nino sube el *suelo* de la asistencia. | PROPUESTA | 1, 5, 6 |
| P-09 | Puntos en E6: **+1 por minijuego ganado en cálida**, vía `sumar_punto`. (Alternativa: 0.) | PROPUESTA | 1 |
| P-10 | Notas: aprobado 60, diagonal 100, rangos por estado, boletín como pantalla `boletin_cinco`. | PROPUESTA | 1, 2 |
| P-11 | Voz interior: cinco `Character` `<h>_int` con su color y sin placa; solo lo académico y emocional, sin romance. | PROPUESTA | 1, 3, 4 |
| P-12 | No visitadas: monólogo con callback a su `queja_*` + **promesa pendiente** (flag para Cap. 2). | PROPUESTA | 3, 4 |
| P-13 | Disculpa de Itsuki: **no se gasta**; solo un intento interrumpido. | PROPUESTA | 4 |
| P-14 | Nino puede llegar a «no confío… todavía», nunca a «confío». | PROPUESTA | 4 |
| P-15 | Nivel de CG **B** (8): 5 de examen + `cg_cinco_aprobadas` + `cg_miku_audifonos_mesa` + 1 opcional; CG estado-agnósticos. Confirmar si hay semillas guardadas. | PROPUESTA | 7 |
| P-16 | Audio: sin BGM nuevo; su tema solo suena si cálida; `descubrimiento` durante su monólogo; reloj en el resto; SFX de acierto/fallo opcionales. | PROPUESTA | 3, 4, 6, 8 |
| P-17 | Capa opcional por `persistent` para quien vio el Final B. | PROPUESTA (no por ahora) | 2 |
| P-18 | Chat de grupo como pantalla de revelación final. | PROPUESTA | 2, 8 |
| P-19 | Coda en casa (curry) dentro de E6. | PROPUESTA | 2 |
| P-20 | Solo PC; minijuegos con ratón o un botón. | PROPUESTA | 1, 5, 6 |
| P-21 | Galería: añadir los CG de E6 (sin romper el conteo); díptico opcional. | PROPUESTA | 1, 7 |
| P-22 | Ganchos para Cap. 2: `e6_frase`, `e6_promesas` y matriz de notas persistente. | PROPUESTA | 1, 2 |
| P-23 | Sprites nuevos: diferir hasta tener el guion. | PROPUESTA | 7 |

### 1.D Reglas que valen en todos los chats

- **Principio de espejo:** E6 invierte el Final B punto por punto (análisis, Anexo A). Antes de escribir una escena, mirar su par en `02_cap1_final_hub3.rpy`.
- **Capas, no escenas paralelas.** Nada de duplicar bloques completos por estado.
- **Invariantes** (análisis §3.8): todas aprueban; 100 solo en la diagonal; minijuego solo cálida; `despido_cap1` nunca `True` en E6; no escribir puntos salvo P-09.
- **No repetir** los pensamientos de MC de `beat_casa` ni las `reaccion_*`.
- **Longitud de línea:** ninguna línea de diálogo supera dos líneas de caja de texto.
- **Arte solo contra guion escrito.**

---

## 2. Mapa de chats

| # | Nombre | Depende de | Esfuerzo | Volumen aprox. | Estado |
|---|---|---|---|---|---|
| 1 | Cimientos técnicos | — | Alto | ~700 líneas de código | ☐ |
| 2 | Guion núcleo | — (puede ir en paralelo con 1) | Máximo | ~255 líneas de guion · 2 notas de CG | ☐ |
| 3 | Guion hermanas A (Yotsuba, Ichika, Miku) | 2 | Máximo | ~345 líneas · 3 CG (+1 opcional) | ☐ |
| 4 | Guion hermanas B (Nino, Itsuki) | 2 (ideal: 3) | Máximo | ~245 líneas · 2 CG | ☐ |
| 5 | Minijuegos I: Yotsuba, Nino, Itsuki | 1 | Alto | ~900 líneas de código · 3 minijuegos | ☐ |
| 6 | Minijuegos II: Miku, Ichika | 1 (ideal: 5) | Alto | ~800 líneas de código · 2 minijuegos | ☐ |
| 7 | Fichas de arte (CG, sprites, prompts) | 2, 3, 4 | Medio | 6–8 CG · hasta 5 sprites | ☐ |
| 8 | Montaje I: núcleo + Yotsuba + Ichika | 1, 2, 3 | Alto | ~1 100 líneas de `.rpy` | ☐ |
| 9 | Montaje II: Nino, Itsuki, Miku + cableado | 1, 2, 4, 8 (y 5, 6 para jugar) | Alto | ~1 200 líneas de `.rpy` | ☐ |
| 10 | Integración y pruebas | todos | Alto | ~40 casos de prueba | ☐ |

**Paralelismo recomendado:** 1 ‖ 2 → 3 → 4 · 5 y 6 en paralelo con 3/4 · 7 tras 2–4 · 8 y 9 tras 1–4 (los minijuegos se enchufan por registro, no hace falta tenerlos terminados) · 10 al final.

**Totales aproximados:** ~840 líneas de guion autoradas (~400 leídas por partida), ~2 400 líneas de código de sistemas y minijuegos, ~2 300 líneas de `.rpy` narrativo, 6–8 CG, 5 minijuegos.

---

## 3. Fichas y prompts

**Bloque común** (ya incluido en cada prompt para que sea autosuficiente):

> CONTEXTO: Proyecto «The Fifth Choice» (novela visual fan de Quintessential Quintuplets, Ren'Py 8.5.3, repo en `The Fifth Choice/`). Trabajas conmigo en el **Evento 6 del Capítulo 1** (cierre del capítulo). Antes de hacer nada, lee en este orden: (1) `docs/CAPITULO_1/EVENTO_6/PLAN_CHATS_EVENTO_6.md` §1 (registro de decisiones: lo DECIDIDO no se debate; si necesitas algo que esté como PROPUESTA, pregúntamelo antes de seguir); (2) `docs/CAPITULO_1/EVENTO_6/ANALISIS_EVENTO_6.md` (las secciones que se indican abajo). Reglas fijas: español; código completo y copiable (sin esqueletos parciales ni atajos tipo ternario); todo `show` lleva su posición; el protagonista nunca muestra rostro; si falta un asset, márcalo `[NUEVO]`; no toques archivos que no estén en tu lista. Si te falta una decisión, pregúntamela **una sola vez, en bloque**, antes de producir.

---

### Chat 1 · Cimientos técnicos

| Campo | Contenido |
|---|---|
| **Orden** | 1 (puede ir en paralelo con el 2). |
| **Objetivo** | Dejar el esqueleto jugable de E6: variables, estados, helpers, voz interior, marco común de minijuegos, notas, depuración y prueba de humo del motor. |
| **Dependencias** | Ninguna. |
| **Lee** | `game/00_definiciones.rpy` · `game/07_ui.rpy` · `game/screens.rpy` (`say`) · `game/09_menus_sistema.rpy` (historial) · `game/08_extras.rpy` (`GALERIA`) · `game/02_cap1_hubs.rpy` · `game/02_cap1_conexiones.rpy` (interc. 6 y 5) · `game/02_cap1_beat_Nino.rpy` · `docs/GUIA_RENPY.md` · `docs/GUIA_UI.md` |
| **Decisiones previas** | P-01, P-02, P-06, P-07, P-08, P-09, P-10, P-11, P-20, P-21, P-22 |
| **Entregable** | Archivos nuevos: `game/02_cap1_evento6.rpy` (`label evento_6` + todos los sub-labels con texto de relleno), `game/10_minijuegos.rpy` (marco), `game/11_e6_debug.rpy`. Cambios mínimos en: `00_definiciones.rpy` (defaults + `Character` `<h>_int`), `07_ui.rpy` (`ui_interior` o kwargs), `08_extras.rpy` (entradas de Galería comentadas). Informe con los nombres exactos del motor verificados. |
| **Terminado cuando** | `jump evento_6` recorre los 10 movimientos con relleno en los 20 estados; el menú de depuración fuerza estado de entrada, ramas de las cinco y `nino_rama_beat`; el minijuego de prueba reintenta, aplica puntos de control, asistencia y «saltar»; Esc, guardar/cargar, retroceder y saltar texto no rompen el bucle; no hay errores de `lint`. |
| **Esfuerzo** | Alto |
| **Volumen** | ~700 líneas de código · 0 CG · 1 minijuego de prueba |

**PROMPT**

```
[BLOQUE COMÚN — pega aquí el bloque común de la parte superior de §3]

TAREA — CHAT 1: CIMIENTOS TÉCNICOS DEL EVENTO 6
Lee del análisis: §1 (auditoría), §3.7 (contrato técnico), §3.8 (invariantes), §5.3–5.6 (base de minijuegos, dificultad, riesgos de motor).

Construye:
1. En `00_definiciones.rpy`: `default` de `e6_estado_entrada`, `e6_estado` (dict), `e6_frase` (dict), `e6_promesas` (lista), `e6_notas` (matriz 5×5), `e6_mj` (dict); `default persistent.e6_mj_ganado_<h>` para las cinco; y los cinco `Character` `<h>_int` (caja del color de la hermana, sin placa, estilo propio; que el historial los trate bien).
2. En `07_ui.rpy`: ampliar `ui_personaje` con kwargs o crear `ui_interior()`, sin romper nada existente.
3. Funciones (en `10_minijuegos.rpy` o en un bloque `init python` claro): `e6_iniciar()` (calcula `estado_entrada` con la regla del análisis, el estado de cada hermana con `rama_de`, valida invariantes con assert legibles), `e6_estado(h)`, `mj_nivel()`, `e6_calcular_notas()` (matriz determinista del §3.5; devuelve y valida I1 e I2).
4. `02_cap1_evento6.rpy`: `label evento_6` y TODOS los sub-labels del contrato (Mov. 1–10 y `e6_<h>_nucleo`, `_mono_<estado>`, `_mj`, `_gesto_<estado>`, `_eco_<estado>`, `_promesa`), con texto de relleno `narrador "[STUB …]"`, y un stub `cap2_inicio`.
5. Marco de minijuegos en `10_minijuegos.rpy`: tablas `MJ_PARAMS` (valores del §5.4 como datos), `mj_ejecutar(juego, hermana)` con bucle de intentos, puntos de control por fase, líneas de fallo por hermana e intento (diccionario con relleno), asistencia adaptativa y «saltar», un `MJ_REGISTRO` para enchufar cada minijuego sin tocar el marco, `screen mj_marco` (HUD común), y un minijuego de prueba de un solo botón. Si P-09 es +1, suma el punto con `sumar_punto` solo al ganar en cálida (una vez por hermana).
6. `11_e6_debug.rpy`: `label e6_debug` con un menú para forzar `estado_entrada`, las cinco ramas (con la restricción de ≤1 fría) y `nino_rama_beat`, más presets para los 20 sobrevivientes.
7. Prueba de humo del motor (Ren'Py 8.5.3): comprueba y REPORTA el nombre exacto de lo que desactiva rollback y skip dentro de una pantalla, si Esc pausa timers y ATL, y qué pasa al guardar/cargar a mitad del minijuego de prueba. Si algo de mi análisis es incorrecto, dilo.

Reglas: no cambies comportamiento existente; muestra el diff de cada archivo modificado; no escribas guion final ni los minijuegos reales.

ENTREGABLE: los archivos anteriores + un informe de 15 líneas (qué hiciste, nombres verificados, riesgos).
TERMINADO CUANDO: cumple el criterio de «terminado» de la ficha del chat 1 en `PLAN_CHATS_EVENTO_6.md`.
AL FINAL: resumen de 5 líneas, lista de archivos tocados y pendientes.
```

---

### Chat 2 · Guion núcleo

| Campo | Contenido |
|---|---|
| **Orden** | 2. |
| **Objetivo** | Escribir las piezas globales de E6 (todo lo que no es un bloque de hermana) en el formato de los guiones de hubs. |
| **Dependencias** | Ninguna (puede ir en paralelo con el 1). |
| **Lee** | `docs/CAPITULO_1/CAP1_FINAL_MALO.md` (+ `game/02_cap1_final_hub3.rpy`) · `game/02_cap1_conexiones.rpy` (interc. 6 y 5) · `game/02_cap1_beat_casa.rpy` · `docs/CAPITULO_1/APERTURA_CAP1.md` · un guion de hub como modelo de formato (`docs/CAPITULO_1/HUBS_HERMANAS/CAP1_evento_nino.md`) |
| **Decisiones previas** | P-01, P-02, P-03, P-04, P-10, P-17, P-18, P-19, P-22 |
| **Entregable** | `docs/CAPITULO_1/EVENTO_6/CAP1_evento_6_nucleo.md` |
| **Terminado cuando** | Contiene Mov. 1 (con S1 ×3 y confesiones espejo de B2), Mov. 7 (Maruo, S2 ×3), el marco de Mov. 8 (puertas, mesa, huecos `[ECO <h>]` y el intento interrumpido de disculpa), Mov. 9 (casa, si P-19), Mov. 10 (chat de grupo si P-18, cálculo, libreta, S3 ×3), tabla de notas, lista de flags de gancho, notas de CG y de audio, y sección «Notas de implementación». Todas las líneas cumplen la regla de longitud. |
| **Esfuerzo** | Máximo |
| **Volumen** | ~255 líneas · 2 notas de CG (`cg_cinco_aprobadas`, boletines/Maruo) |

**PROMPT**

```
[BLOQUE COMÚN — pega aquí el bloque común de la parte superior de §3]

TAREA — CHAT 2: GUION NÚCLEO DEL EVENTO 6
Lee del análisis: §0, §3 (modelo de capas y slots S1/S2/S3), §4 (estructura, audio y huecos), §7 (boceto: mismo tono, NO copies sus líneas) y el Anexo A (espejo con el Final B).

Escribe, en el formato y con los marcadores de los guiones de hubs (`[BG]` `[CG]` `[SPR]` `[MUS]` `[SFX]` `[$]` `[NUEVO]`), un único documento con:
- «Decisiones de este movimiento» (breve, como en los hubs).
- Mov. 1 · Lunes: espejo de B1/B2; S1 en sus 3 variantes (superado / mixto / bueno); las confesiones pre-examen de las cinco (una línea cada una, con variante «alcanzada»/«no alcanzada»); «Hagan lo que saben».
- Mov. 7 · Resultados y Maruo: cinco boletines en fila; S2 en sus 3 variantes; que Maruo siga siendo seco (no cálido); «Los exámenes no terminan aquí».
- Mov. 8 · Las cinco: las puertas se abren (las dos no visitadas, las últimas); la mesa y el CG `cg_cinco_aprobadas`; marco con huecos `[ECO <hermana>]` que escribirán los chats 3 y 4; el intento interrumpido de disculpa MC–Itsuki (la disculpa NO se gasta) con Yotsuba interrumpiendo.
- Mov. 9 · Casa (curry), espejo de B8 («Gracias por la comida»: esta vez lo siente; MC nota que ya no es solo por el dinero).
- Mov. 10 · Cuarto: chat «¡Equipo Quintillizas + Tutor!» con cinco fotos (Nino no se sale), cálculo de la nota máxima de cada una, «lo único que controlé fue a dónde fui», libreta con una frase nueva, y la última línea en 3 variantes (S3). Termina sin resolver.
- Tabla de notas (diagonal 100; fuera de la diagonal según §3.5).
- Lista de flags de gancho para Cap. 2 y de CG/audio.
- «Notas de implementación».

Reglas: aplica las decisiones P-xx tal como estén en el plan; no repitas pensamientos de `beat_casa` ni líneas de `reaccion_*`; ninguna línea supera dos líneas de caja; el estado de entrada solo toca S1, S2 y S3.

ENTREGABLE: `docs/CAPITULO_1/EVENTO_6/CAP1_evento_6_nucleo.md`.
TERMINADO CUANDO: cumple el criterio de «terminado» de la ficha del chat 2.
AL FINAL: resumen de 5 líneas y lista de dudas abiertas.
```

---

### Chat 3 · Guion hermanas A (Yotsuba, Ichika, Miku)

| Campo | Contenido |
|---|---|
| **Orden** | 3. |
| **Objetivo** | Escribir los tres bloques completos, con todas sus capas. |
| **Dependencias** | Chat 2. |
| **Lee** | `CAP1_evento_6_nucleo.md` · los hubs de Yotsuba, Ichika y Miku (`.md` y `.rpy`) · `02_cap1_conexiones.rpy` (`reaccion_*` y `queja_*` de las tres) · `02_cap1_final_hub3.rpy` (B3.1, B3.2, B3.5, B4, B7) · `docs/CAPITULO_1/BEATS_CAP1/CAP1_beat_casa.md` |
| **Decisiones previas** | P-05, P-11, P-12, P-16 |
| **Entregable** | `docs/CAPITULO_1/EVENTO_6/CAP1_evento_6_bloques_A.md` |
| **Terminado cuando** | Por cada hermana: núcleo, 4 monólogos (cálida / tibia / fría / no visitada), encuadre del minijuego con 3 líneas de fallo, frase y salida, 4 gestos, 4 ecos para Mov. 8, promesa (no visitada), nota de CG, sprites solicitados, flags escritos y tabla de assets. Eco literal de la decisión del jugador en cada monólogo. |
| **Esfuerzo** | Máximo |
| **Volumen** | ~345 líneas · 3 CG (+ `cg_miku_audifonos_mesa` opcional) · 3 minijuegos (solo el texto) |

**PROMPT**

```
[BLOQUE COMÚN — pega aquí el bloque común de la parte superior de §3]

TAREA — CHAT 3: GUION DE LOS BLOQUES DE YOTSUBA, ICHIKA Y MIKU
Lee del análisis: §2.1, §2.2, §2.5 (arcos y frases), §3.2–3.3 (capas y focos), §4.2 (plantilla de bloque), §5.2 y §5.5 (qué hace cada minijuego y fallos con carácter), §7 (muestras de tono) y el Anexo A. Lee también `docs/CAPITULO_1/EVENTO_6/CAP1_evento_6_nucleo.md` (ya escrito: respeta sus huecos `[ECO <hermana>]`).

Para cada hermana (orden Yotsuba → Ichika → Miku) escribe, en el formato de los hubs:
- N · núcleo (narrador, día y materia, `[CG NUEVO — cg_<h>_examen]`, observación de MC), con `ui_escena("beat", h, "Aula · <Materia>")`.
- M · 4 monólogos de voz interior (cálida, tibia, fría, no visitada) según los focos del §3.3; cada uno con un eco literal de la decisión del jugador y usando el recurso formal de la hermana (Yotsuba sin signos / Miku sin «…» al soltarse / Ichika sin exclamación).
- J · solo cálida: la frase que activa el minijuego, 3 líneas de fallo por intento (las del §5.5 o mejores), la frase de cambio completa y la salida.
- F · la frase en sus 4 versiones (completa, cortada, cerrada, de espera) y qué valor de `e6_frase` escribe cada una.
- G · 4 gestos de lo que MC ve desde afuera (espejo de su `*_fracaso` / B3.x).
- E · 4 ecos para la escena de las cinco (Mov. 8).
- P · promesa pendiente de MC (solo no visitada), usando solo lo que MC sabe por su `queja_*`.
- Notas de CG (espejo del `*_fracaso`: misma cámara, primer plano de MC), sprites que pides (solo si hacen falta; la diferencia va en la silueta), audio (tema solo si cálida; `descubrimiento` durante el monólogo cálido), flags.

Cobros obligatorios: Yotsuba (28, «1»→«100» solo cálida, «uno por ciento», pregunta «qué siente el protagonista…»); Ichika (problema de trenes, papel nuevo, «estoy bien»); Miku (sal y rutas de comercio, página 120 con su primera sonrisa, la frase «mucho más—» terminada, primera línea sin «…» inicial, goma entera, fallos «Perdón → Perd— → Otra vez»).

Reglas: no gastes la disculpa de Itsuki; no repitas `beat_casa` ni `reaccion_*`; ninguna línea supera dos líneas de caja; sin romance en la voz interior.

ENTREGABLE: `docs/CAPITULO_1/EVENTO_6/CAP1_evento_6_bloques_A.md`.
TERMINADO CUANDO: cumple el criterio de «terminado» de la ficha del chat 3.
AL FINAL: resumen de 5 líneas, lista de assets nuevos y dudas abiertas.
```

---

### Chat 4 · Guion hermanas B (Nino, Itsuki)

| Campo | Contenido |
|---|---|
| **Orden** | 4. |
| **Objetivo** | Escribir los bloques de Nino e Itsuki, las dos con una capa extra por su beat. |
| **Dependencias** | Chat 2 (ideal también el 3, por coherencia de voz). |
| **Lee** | `CAP1_evento_6_nucleo.md` · `CAP1_evento_6_bloques_A.md` · hubs de Nino e Itsuki (`.md` y `.rpy`) · beats de Nino e Itsuki (`.md` y `.rpy`) · `02_cap1_conexiones.rpy` (interc. 5 y 6, `reaccion_*`, `queja_*`) · `02_cap1_final_hub3.rpy` (B3.3, B3.4, B7) |
| **Decisiones previas** | P-05, P-11, P-12, P-13, P-14, P-16 |
| **Entregable** | `docs/CAPITULO_1/EVENTO_6/CAP1_evento_6_bloques_B.md` |
| **Terminado cuando** | Igual que el chat 3 para Nino e Itsuki, más la capa B (Nino: `nino_rama_beat` ×3, 2 líneas cada una; Itsuki: eco del beat de la azotea), el intento interrumpido de disculpa coherente con el núcleo, y la lista de lo que Nino **no** hace (confiar, resolver la tarjeta). |
| **Esfuerzo** | Máximo |
| **Volumen** | ~245 líneas · 2 CG · 2 minijuegos (solo texto) |

**PROMPT**

```
[BLOQUE COMÚN — pega aquí el bloque común de la parte superior de §3]

TAREA — CHAT 4: GUION DE LOS BLOQUES DE NINO E ITSUKI
Lee del análisis: §2.3 y §2.4, §3.2–3.3, §4.2, §5.2 y §5.5, §7 y el Anexo A. Lee también los dos guiones ya escritos de E6 (`CAP1_evento_6_nucleo.md` y `CAP1_evento_6_bloques_A.md`) para mantener la voz y respetar los huecos `[ECO <hermana>]` y el intento interrumpido de disculpa.

Para Nino e Itsuki escribe lo mismo que en el chat 3 (N, M×4, J solo cálida, F×4, G×4, E×4, P, notas de CG/sprites/audio/flags), y además:
- NINO: capa B por `nino_rama_beat` (cálida / tibia / fría; 2 líneas cada una) que se suma a su estado de hub; la cálida del hub incluye el minijuego N1′ «Compras para seis» (cinco listas y un sexto hueco) y la frase «No pienso adelantar el golpe»; cobra «treinta y cinco días», «solo el tiempo lo va a demostrar», «anota la fecha», que no se sale del chat y el Final B3.3 (cuando se queda «revisando»). Puede llegar a «no confío… todavía»; NUNCA a «confío»; NO resuelvas la tarjeta de receta.
- ITSUKI: minijuego It1 con «levantar la mano» al profesor (frase A si lo usa, frase B si resuelve sola desde el principio); oraciones que se acortan en la grieta; cobra «el juego se acabó hoy», Final B3.4 y la azotea (sin gastar la disculpa); si no visitada, promesa «sube sin el cuaderno».

Reglas: respeta P-13 y P-14; sin romance en la voz interior; no repitas `beat_casa` ni `reaccion_*`; ninguna línea supera dos líneas de caja.

ENTREGABLE: `docs/CAPITULO_1/EVENTO_6/CAP1_evento_6_bloques_B.md`.
TERMINADO CUANDO: cumple el criterio de «terminado» de la ficha del chat 4.
AL FINAL: resumen de 5 líneas, lista de assets nuevos y dudas abiertas.
```

---

### Chat 5 · Minijuegos I (Yotsuba, Nino, Itsuki)

| Campo | Contenido |
|---|---|
| **Orden** | 5 (en paralelo con 3 y 4). |
| **Objetivo** | Programar Y2, N1′ y It1 sobre el marco del chat 1. |
| **Dependencias** | Chat 1. |
| **Lee** | `game/10_minijuegos.rpy` · `game/00_definiciones.rpy` · `game/07_ui.rpy` · `game/screens.rpy` · `herramientas/generar_ui.py` (para el estilo de PNG) · `docs/GUIA_RENPY.md` · `docs/GUIA_UI.md` |
| **Decisiones previas** | P-06, P-07, P-08, P-20 |
| **Entregable** | `game/10_mj_yotsuba.rpy`, `game/10_mj_nino.rpy`, `game/10_mj_itsuki.rpy` (y los PNG nuevos de interfaz si hacen falta, con el script correspondiente). Cada uno registrado en `MJ_REGISTRO` y con un label de prueba. |
| **Terminado cuando** | Cada minijuego: se juega con ratón/espacio, respeta las tres tablas de dificultad, tiene puntos de control, usa las líneas de fallo por intento, devuelve `ganado/perdido/saltado`, no usa `random` de Python, y pasa la prueba de humo (Esc, guardar/cargar, retroceder, saltar). |
| **Esfuerzo** | Alto |
| **Volumen** | ~900 líneas de código · 3 minijuegos |

**PROMPT**

```
[BLOQUE COMÚN — pega aquí el bloque común de la parte superior de §3]

TAREA — CHAT 5: MINIJUEGOS Y2 (YOTSUBA), N1′ (NINO) E It1 (ITSUKI)
Lee del análisis: §5.2 (diseño de cada uno), §5.3 (base compartida), §5.4 (tablas de dificultad), §5.5 (fallos y asistencia) y §5.6 (riesgos de motor). Lee `game/10_minijuegos.rpy` (el marco ya construido en el chat 1: no lo rehagas, enchúfate).

Programa, en archivos separados y registrados en `MJ_REGISTRO`:
1. Y2 · Relevo: cinco tramos iguales en carriles, un botón; salida en falso y testigo caído fallan; parámetros por nivel de la tabla.
2. N1′ · Compras para seis: cinco listas, etiquetas en inglés con la traducción que aparece sola tras el retardo del nivel, estantes con distractores casi iguales, y el sexto hueco como elección sin respuesta «correcta»; piezas en estilo UI del juego (cajas con texto, sin ilustraciones de producto).
3. It1 · Conversiones: cadena de pasos, el número equivocado del primer intento aparece como fantasma gris y reaparece, botón «Levantar la mano» (revela dónde mirar, NO da la respuesta; costo y usos según nivel), y que el minijuego devuelva si usó la ayuda (para que el guion elija la frase A o B).

Todo con datos en `MJ_PARAMS`, `renpy.random`, sin tocar el marco salvo para registrarse. Incluye un label de prueba por minijuego y una nota de calibración con los parámetros que más conviene tocar.

ENTREGABLE: los tres archivos `.rpy` (+ PNG/script si hacen falta) y un informe corto (qué falta calibrar jugando).
TERMINADO CUANDO: cumple el criterio de «terminado» de la ficha del chat 5.
AL FINAL: resumen de 5 líneas y riesgos detectados.
```

---

### Chat 6 · Minijuegos II (Miku, Ichika)

| Campo | Contenido |
|---|---|
| **Orden** | 6. |
| **Objetivo** | Programar M3 (el compás) e I1′ (la máscara se cansa). |
| **Dependencias** | Chat 1 (ideal: 5, para mantener el mismo estilo). |
| **Lee** | `game/10_minijuegos.rpy` · `game/10_mj_*.rpy` (si ya existen) · `game/00_definiciones.rpy` (audio: `miku`, `amb_reloj`) · `docs/GUIA_AUDIO.md` · `docs/GUIA_RENPY.md` |
| **Decisiones previas** | P-06, P-07, P-08, P-16, P-20 · **y la medición de BPM/offset de `miku_tema`** (tarea externa T-02) |
| **Entregable** | `game/10_mj_miku.rpy`, `game/10_mj_ichika.rpy`, labels de prueba. |
| **Terminado cuando** | M3 funciona con reloj propio (no depende de `get_pos()`), tiene fase 1 con música y fase 2 con el reloj, ventanas por nivel, puntos de control y **plan B con metrónomo** activable con una constante; I1′ implementa *tocar* vs *mantener*, la barra de máscara y la última línea solo sincera; ambos pasan la prueba de humo. |
| **Esfuerzo** | Alto |
| **Volumen** | ~800 líneas de código · 2 minijuegos |

**PROMPT**

```
[BLOQUE COMÚN — pega aquí el bloque común de la parte superior de §3]

TAREA — CHAT 6: MINIJUEGOS M3 (MIKU) E I1′ (ICHIKA)
Lee del análisis: §5.2, §5.3, §5.4, §5.5 y §5.6 (en especial el riesgo de sincronía de audio). Lee `game/10_minijuegos.rpy` (marco del chat 1) y, si existen, los minijuegos del chat 5 para mantener estilo y convenciones.

Programa, registrados en `MJ_REGISTRO`:
1. M3 · El compás: 3 carriles de barras tipo ecualizador (motivo de Miku). Fase 1 al compás de su tema (`audio.miku`) con las constantes `MIKU_BPM` y `MIKU_OFFSET` (yo te las daré medidas; por ahora déjalas como constantes claras), generando el mapa de notas desde el BPM; reloj propio, calibración de latencia y ventanas por nivel. Fase 2: la música se corta (los audífonos se apagan) y el compás lo marca `amb_reloj` o, si lo prefieres, un metrónomo propio. Plan B: una constante que sustituya el tema por metrónomo. Al ganar, que devuelva el resultado para que el guion haga que se quite los audífonos.
2. I1′ · La máscara se cansa: líneas de un guion; cada una ofrece «Actuada» (toque, rápida, sube la barra de máscara) o «Sincera» (mantener pulsado, baja la barra); si la barra llega al tope se queda en blanco; la última línea solo puede decirse sincera; parámetros por nivel.

Todo con datos en `MJ_PARAMS`, `renpy.random`, puntos de control por fase, y sin tocar el marco salvo para registrarse. Incluye label de prueba y nota de calibración. Si algo de §5.6 resulta incorrecto en 8.5.3, dilo y propone la corrección.

ENTREGABLE: `game/10_mj_miku.rpy`, `game/10_mj_ichika.rpy` y un informe corto (qué falta calibrar jugando y qué medir en el audio).
TERMINADO CUANDO: cumple el criterio de «terminado» de la ficha del chat 6.
AL FINAL: resumen de 5 líneas y riesgos detectados.
```

---

### Chat 7 · Fichas de arte (CG, sprites, prompts)

| Campo | Contenido |
|---|---|
| **Orden** | 7 (tras 2, 3 y 4). |
| **Objetivo** | Convertir las notas de CG y sprites de los guiones en fichas y prompts de PixAI, y cerrar la lista definitiva de assets. |
| **Dependencias** | Chats 2, 3 y 4. |
| **Lee** | Los tres guiones de E6 · `docs/GUIA_ARTE.md` · `docs/CAPITULO_1/CAP1_FINAL_MALO.md` (receta de los `*_fracaso`) · `game/02_cap1_final_hub3.rpy` y `game/00_definiciones.rpy` (nombres de imagen) |
| **Decisiones previas** | P-03, P-15, P-23 · respuesta sobre las semillas guardadas (tarea externa T-01) |
| **Entregable** | `docs/CAPITULO_1/EVENTO_6/CAP1_evento_6_ARTE.md` |
| **Terminado cuando** | Hay una ficha por CG con prompt positivo y negativo (si el modelo lo permite), pesos de LoRA según la guía, encuadre espejo del `*_fracaso` correspondiente, orden de generación, semillas a guardar y criterio de «terminado»; una lista de sprites solo si el guion los exige; y la tabla definitiva de assets con nombres de archivo e imagen `.rpy`. |
| **Esfuerzo** | Medio |
| **Volumen** | 6–8 CG · hasta 5 sprites (condicionales) |

**PROMPT**

```
[BLOQUE COMÚN — pega aquí el bloque común de la parte superior de §3]

TAREA — CHAT 7: FICHAS DE ARTE DEL EVENTO 6
Lee del análisis: §1.7 (qué son los `*_fracaso`), §3.6 (niveles de CG), Anexo A y Anexo C. Lee los tres guiones de E6 (`CAP1_evento_6_nucleo.md`, `_bloques_A.md`, `_bloques_B.md`) y `docs/GUIA_ARTE.md` completa.

Produce `docs/CAPITULO_1/EVENTO_6/CAP1_evento_6_ARTE.md` con:
1. Una ficha por CG según el nivel decidido en P-15: nombre, escena, qué cuenta, composición, prompt positivo (y negativo si el modelo base lo permite), pesos de LoRA (serie 0.3 máx.; personaje 0.7–0.8; grupo solo serie), resolución 1280×720, orden de generación y semilla a guardar.
2. Para los cinco `cg_<h>_examen`: espejo EXACTO de la cámara y el primer plano del `cg_<h>_fracaso` (leer sus fichas), cambiando solo la silueta de la hermana según el guion. Generarlos en la misma sesión.
3. Para `cg_cinco_aprobadas`: mismo encuadre y semilla que `cg_cinco_estudiando`; plan de edición con Gemini (máx. 3 pasadas) y qué defender primero (cinco figuras, luego pelo, luego poses, luego vestuario).
4. Solo si el guion los pide y P-23 lo permite: fichas de sprites nuevos (diferencia en la silueta, 760×930, línea de ojos en 199, IPD 77,2).
5. Tabla definitiva de assets: nombre de imagen, ruta de archivo sugerida, declaración `image …` y entrada de `GALERIA`.

Reglas: no inventes escenas que no estén en los guiones; respeta la guía de arte (nada de «without X»; tokens redundantes para descriptores difíciles; Futaro nunca de frente).

ENTREGABLE: el `.md` anterior.
TERMINADO CUANDO: cumple el criterio de «terminado» de la ficha del chat 7.
AL FINAL: resumen de 5 líneas y orden recomendado de generación.
```

---

### Chat 8 · Montaje I (núcleo + Yotsuba + Ichika)

| Campo | Contenido |
|---|---|
| **Orden** | 8. |
| **Objetivo** | Pasar a `.rpy` el guion núcleo y los bloques de Yotsuba e Ichika, e implementar las pantallas propias de E6. |
| **Dependencias** | Chats 1, 2 y 3. |
| **Lee** | `game/02_cap1_evento6.rpy` (stubs) · `game/10_minijuegos.rpy` · `CAP1_evento_6_nucleo.md` · `CAP1_evento_6_bloques_A.md` (partes de Yotsuba e Ichika) · `game/00_definiciones.rpy` · `game/07_ui.rpy` · `docs/GUIA_RENPY.md` · `docs/GUIA_AUDIO.md` · un `.rpy` de hub como modelo de estilo (`game/02_cap1_Yotsuba.rpy`) |
| **Decisiones previas** | P-16, P-18 · tener claros los nombres de assets |
| **Entregable** | Actualización de `game/02_cap1_evento6.rpy` (Mov. 1, 2, 3, 7, 8 parcial, 9 y 10; bloques de Yotsuba e Ichika), `screen boletin_cinco`, `screen chat_grupo`, declaraciones `image` de los CG de E6 con **sustituto** si el archivo aún no existe, y entradas de `GALERIA`. |
| **Terminado cuando** | Esas escenas se juegan de punta a punta con los estados forzados desde `e6_debug`; el HUD, la música (tema solo si cálida), los silencios y `amb_reloj` siguen la guía; Yotsuba e Ichika llaman a su minijuego solo si cálida (aunque sea con el de prueba); las pantallas muestran la diagonal y el chat. |
| **Esfuerzo** | Alto |
| **Volumen** | ~1 100 líneas de `.rpy` · 2 pantallas |

**PROMPT**

```
[BLOQUE COMÚN — pega aquí el bloque común de la parte superior de §3]

TAREA — CHAT 8: MONTAJE I DEL EVENTO 6 (NÚCLEO, YOTSUBA E ICHIKA)
Lee del análisis: §3.7 (contrato), §4 (estructura y audio), §5.3 (cómo se enchufan los minijuegos) y el Anexo C. Lee los guiones indicados en la ficha del chat 8 y `game/02_cap1_evento6.rpy` (stubs del chat 1).

Convierte a Ren'Py, respetando al pie de la letra las convenciones del proyecto (`show` siempre con posición y `pj`/`pj_habla`/`pj_calla`, `scene bg_*` tras cada CG, transiciones por `with`, `duck()` solo donde toca, volúmenes de la guía):
- Mov. 1, 7, 9 y 10 completos, y el marco de Mov. 8 con los ecos de Yotsuba e Ichika (los de las otras tres quedan como hueco marcado).
- Los bloques de Yotsuba e Ichika (Mov. 2 y 3) con sus capas por `e6_estado[h]`, llamando a `mj_ejecutar` solo en cálida y escribiendo `e6_frase` y `e6_promesas`.
- `screen boletin_cinco` (matriz 5×5 con la diagonal que se ilumina y se funde en «100» ×5) y `screen chat_grupo` (cinco fotos de boletines), con el estilo UI del juego.
- Declaraciones `image` de los CG de E6 con un sustituto visible si el archivo todavía no existe (por ejemplo `renpy.loadable`), y las entradas de `GALERIA`.

Reglas: no inventes líneas: el texto sale de los guiones; si falta algo, márcalo; no toques los minijuegos reales ni los bloques de Nino, Itsuki y Miku.

ENTREGABLE: `game/02_cap1_evento6.rpy` actualizado y los archivos de pantallas, con un diff por archivo y una lista de huecos pendientes.
TERMINADO CUANDO: cumple el criterio de «terminado» de la ficha del chat 8.
AL FINAL: resumen de 5 líneas y lista de lo que dejas para el chat 9.
```

---

### Chat 9 · Montaje II (Nino, Itsuki, Miku + cableado)

| Campo | Contenido |
|---|---|
| **Orden** | 9. |
| **Objetivo** | Montar los tres bloques restantes, completar los ecos de Mov. 8 y cablear los minijuegos reales. |
| **Dependencias** | Chats 1, 2, 4 y 8 (y 5 y 6 para jugar los minijuegos reales). |
| **Lee** | `game/02_cap1_evento6.rpy` · `game/10_minijuegos.rpy` · `game/10_mj_*.rpy` · `CAP1_evento_6_nucleo.md` · `CAP1_evento_6_bloques_A.md` (Miku) · `CAP1_evento_6_bloques_B.md` · `docs/GUIA_AUDIO.md` |
| **Decisiones previas** | P-14, P-16 |
| **Entregable** | `game/02_cap1_evento6.rpy` completo, con los cinco bloques, todos los ecos y el cableado de los cinco minijuegos y de `mj_nivel()`. |
| **Terminado cuando** | Los 20 sobrevivientes se recorren de punta a punta; cada hermana cálida lanza su minijuego real con la dificultad correcta; no hay textos de relleno; Mov. 8 tiene los cinco ecos; Cap. 2 recibe `e6_frase` y `e6_promesas`. |
| **Esfuerzo** | Alto |
| **Volumen** | ~1 200 líneas de `.rpy` |

**PROMPT**

```
[BLOQUE COMÚN — pega aquí el bloque común de la parte superior de §3]

TAREA — CHAT 9: MONTAJE II DEL EVENTO 6 (NINO, ITSUKI, MIKU Y CABLEADO)
Lee del análisis: §3.7, §4, §5.3 y el Anexo C. Lee el estado actual de `game/02_cap1_evento6.rpy` (chat 8) y los guiones de Nino, Itsuki y Miku.

Completa:
- Los bloques de Nino, Itsuki y Miku (Mov. 4, 5 y 6) con sus capas, incluida la capa de beat de Nino (`nino_rama_beat`) y el eco del beat de Itsuki.
- Los ecos de Mov. 8 que faltan.
- El cableado: cada hermana cálida llama a `mj_ejecutar` con su minijuego real; el nivel sale de `mj_nivel()`; el resultado alimenta la frase (A/B en Itsuki) y el punto de P-09 si procede.
- Miku: el momento en que deja los audífonos sobre el pupitre tras ganar M3, y la regla de que su tema solo suena si cálida.
- Revisión final de huecos: busca y elimina todo `[STUB …]`.

Reglas: texto solo de los guiones; mismas convenciones que el chat 8; no cambies los minijuegos (si ves un fallo, descríbelo).

ENTREGABLE: `game/02_cap1_evento6.rpy` completo y un informe de huecos.
TERMINADO CUANDO: cumple el criterio de «terminado» de la ficha del chat 9.
AL FINAL: resumen de 5 líneas y lista de casos que debe probar el chat 10.
```

---

### Chat 10 · Integración y pruebas

| Campo | Contenido |
|---|---|
| **Orden** | 10 (último). |
| **Objetivo** | Recorrer todas las combinaciones y cerrar el movimiento. |
| **Dependencias** | Todos. |
| **Lee** | Todo `game/02_cap1_*.rpy`, `10_*.rpy`, `11_e6_debug.rpy`, `08_extras.rpy`; ambos `.md` de `docs/CAPITULO_1/EVENTO_6/`; `docs/GUIA_RENPY.md` (sección de diagnóstico). |
| **Decisiones previas** | Ninguna nueva: cierra lo pendiente de `PLAN_CHATS_EVENTO_6.md`. |
| **Entregable** | Parches mínimos para lo que falle; `docs/CAPITULO_1/EVENTO_6/E6_PRUEBAS.md` con la matriz de resultados; y una lista de cambios que **tú** harás en `README.md` y `CAP1.md` al terminar el capítulo. |
| **Terminado cuando** | Los 20 sobrevivientes × ramas de Nino × beat se recorren sin errores; se verifican las invariantes I1–I10 con asserts; los minijuegos se prueban con y sin boost de Nino, en difícil, media y asistida, con puntos de control y saltar; guardar, cargar, retroceder y saltar texto no rompen; despidos A y B siguen funcionando; la Galería cuenta bien. |
| **Esfuerzo** | Alto |
| **Volumen** | ~40 casos de prueba |

**PROMPT**

```
[BLOQUE COMÚN — pega aquí el bloque común de la parte superior de §3]

TAREA — CHAT 10: INTEGRACIÓN Y PRUEBAS DEL EVENTO 6
Lee del análisis: §3.8 (invariantes), §5.5–5.6, Anexo B (los 20 sobrevivientes) y Anexo D (checklist). Lee el código real de E6 en `game/`.

Haz una revisión estática y dime qué casos hay que ejecutar a mano (no puedes ejecutar el juego):
1. Matriz de casos: los 20 sobrevivientes × `nino_rama_beat` (3) × estado de Nino en el hub. Para cada uno, qué debe pasar y en qué línea del código.
2. Invariantes I1–I10: dónde se comprueban y qué assert falta.
3. Minijuegos: dificultad correcta con y sin boost, asistencia adaptativa, puntos de control, «saltar», y que `skip`/rollback/Esc no los vuelvan trampa.
4. Regresión: despidos A y B, hubs, beats, `beat_casa` y el collage siguen intactos.
5. Galería y `persistent`: conteos y flags.
6. Rendimiento: pantallas y `matrixcolor` en minijuegos.
Corrige con parches mínimos lo que sea claramente un fallo; lo dudoso, descríbelo.

ENTREGABLE: parches (con diff), `docs/CAPITULO_1/EVENTO_6/E6_PRUEBAS.md` y la lista de ediciones pendientes de `README.md` y `CAP1.md`.
TERMINADO CUANDO: cumple el criterio de «terminado» de la ficha del chat 10.
AL FINAL: resumen de 5 líneas y lista de lo que debes probar tú jugando.
```

---

## 4. Tareas fuera de Claude

| ID | Tarea | Cuándo | Por qué |
|---|---|---|---|
| T-01 | Comprobar si guardaste las **semillas** de los 5 `cg_*_fracaso` y de `cg_cinco_estudiando`, y anotar sus prompts. | Antes del chat 7 | El espejo y la serie de la mesa dependen de ellas. |
| T-02 | Medir **BPM y offset** de `miku_tema` («The calm seaside») en Audacity y, si hace falta, exportar un corte limpio de 40–60 s. | Antes del chat 6 | M3 necesita `MIKU_BPM` y `MIKU_OFFSET`. |
| T-03 | (Opcional) Conseguir dos SFX cortos de acierto/fallo para minijuegos. | Antes del chat 6 | Si no, se reutilizan `sfx_hover`/`sfx_click`. |
| T-04 | Generar los CG en PixAI (nivel A o B) y escalar con `escalar_cgs.py`. | Después del chat 7; antes del chat 10 | Hasta entonces se usan sustitutos. |
| T-05 | Editar con Gemini `cg_cinco_aprobadas` (máx. 3 pasadas). | Tras generar la base | Es la imagen más cara. |
| T-06 | (Condicional) Generar sprites nuevos si el chat 7 los exige. | Después del chat 7 | Solo contra guion escrito. |
| T-07 | Playtest de minijuegos en el equipo más lento y con 2–3 personas ajenas. | Después de los chats 5, 6 y 9 | Calibrar difícil/media/asistida. |
| T-08 | Commit/rama antes de cada chat y copia de `game/saves`. | Siempre | Seguridad. |
| T-09 | Actualizar `README.md` y `CAP1.md` en bloque (puntos reales, «tres desaires», E6 en el aula, etc.). | Tras el chat 10 | Pediste no tocarlos hasta cerrar el capítulo. |
| T-10 | Decidir y aplicar la **corrección de la economía de puntos** si P-09 lo requiere en Cap. 2–3. | Antes de planificar el Cap. 2 | Hallazgo del análisis §1.9. |

---

## 5. Decisiones tuyas, chat por chat

| Chat | Debes tener resuelto antes |
|---|---|
| 1 | P-01, P-02, P-06, P-07, P-08, P-09, P-10, P-11, P-20, P-21, P-22 |
| 2 | P-01, P-02, P-03, P-04, P-10, P-17, P-18, P-19, P-22 |
| 3 | P-05, P-11, P-12, P-16 |
| 4 | P-05, P-11, P-12, P-13, P-14, P-16 |
| 5 | P-06, P-07, P-08, P-20 |
| 6 | P-06, P-07, P-08, P-16, P-20 · T-02 |
| 7 | P-03, P-15, P-23 · T-01 |
| 8 | P-16, P-18 · nombres de assets del chat 7 |
| 9 | P-14, P-16 |
| 10 | Ninguna nueva |

**Mínimo para abrir el chat 1 ya mismo:** P-01, P-02, P-06, P-07, P-08, P-09, P-10, P-11, P-20, P-21 y P-22.

---

## 6. Resumen de esfuerzo total

| Concepto | Cantidad |
|---|---|
| Líneas de guion autoradas | ~840 (≈ 400 leídas por partida) |
| Líneas de código de sistemas y minijuegos | ~2 400 |
| Líneas de `.rpy` narrativo | ~2 300 |
| CG nuevos | 6–8 (hasta 13 en el nivel máximo) |
| Minijuegos | 5 (0–3 jugados por partida) |
| Chats | 10 |
| Tareas externas | 10 (3 imprescindibles: T-01, T-02, T-04) |
