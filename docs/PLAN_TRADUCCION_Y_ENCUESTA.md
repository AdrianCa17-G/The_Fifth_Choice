# Plan: traducción al inglés (v1.1) + encuesta

**Periodo:** lunes 23 de noviembre a viernes 4 de diciembre de 2026
**Descanso previo:** viernes 20, sábado 21, domingo 22 (sin abrir Ren'Py)
**Inicio del Cap. 2:** sabado 5, domingo 6 o lunes 7 de diciembre

> Este archivo es la referencia de esta fase. Cada chat o sesión nueva debe leerlo antes de empezar
> y actualizar la tabla de **Progreso** al terminar. Una copia vive en `docs/PLAN_TRADUCCION_Y_ENCUESTA.md`
> del repo, para que Claude Code también la lea.

---

## 1. Datos de partida (medidos en el repo, 21/11/2026)

- Diálogo y narración: **~5.850 líneas, ~46.000 palabras**.
- No existe `game/tl/`. El sistema de traducción se monta desde cero.

| Archivo | Palabras aprox. |
|---|---|
| 02_cap1_evento6.rpy | 13.000 |
| 02_cap1_conexiones.rpy | 8.800 |
| 02_cap1_beat_casa.rpy | 3.900 |
| 01_prologo.rpy | 3.800 |
| 02_cap1_final_malo.rpy | 3.200 |
| 02_cap1_apertura.rpy | 2.200 |
| 02_cap1_beat_Nino.rpy | 1.700 |
| 02_cap1_Miku / Yotsuba / Ichika / Nino / Itsuki | 1.200–1.700 c/u (~7.700 en total) |
| 02_cap1_beat_Itsuki.rpy | 1.000 |
| Interfaz, minijuegos, chat, boletín, créditos | poco texto, pero repartido en muchos archivos |

**Ritmo supuesto:** borrador con IA + revisión completa de Adrian = **7.000–9.000 palabras al día**.
Si un día va más lento, se usa el colchón del viernes 4. No se recorta la fase de pruebas.

---

## 2. Reglas de la fase

1. **Congelar el texto en español de la v1.0.** Ren'Py enlaza cada traducción a un hash de la línea original.
   Si se corrige una línea en español, su traducción queda huérfana. Las erratas en español se anotan
   en `docs/ERRATAS_ES.md` y se corrigen todas juntas al final, regenerando la traducción de esas líneas.
2. **Nunca editar los .rpy del juego para traducir.** Todo va en `game/tl/english/`.
3. Se respeta `docs/GLOSARIO_EN.md` (se crea el día 1): nombres, honoríficos, materias, voz de cada personaje.
4. Ninguna línea en inglés supera ~100 caracteres (dos líneas de la caja de texto).
5. Se conservan intactas las interpolaciones y etiquetas: `[mc]`, `{i}`, `{b}`, `{w}`, `{nw}`, `{color}`, etc.
6. Los créditos en inglés se traducen vía `tl/`. Si cambia el texto de `16_creditos.rpy`, también cambia `CREDITOS.md`.
   Sin mencionar a Gemini ni ChatGPT.
7. Antes de tocar interfaz o motor: `docs/GUIA_UI.md` y `docs/GUIA_RENPY.md`.
8. Al terminar cada sesión: commit + push, y actualizar la tabla de **Progreso**.

---

## 3. Calendario

**Leyenda de herramientas**
- **Chat** = Claude en claude.ai, dentro de este proyecto (lee las instrucciones y este plan).
- **Code** = Claude Code local sobre la carpeta del juego (edita archivos y hace commits).
- **Esfuerzo**: bajo / medio / alto. En Claude Code se fija con `/effort`. En el chat, el razonamiento extendido equivale a "alto".

| Día | Tarea | Herramienta | Modelo · esfuerzo | ¿Sesión nueva? |
|---|---|---|---|---|
| **Lun 23** | A. Encuesta en español lista para Google Forms y publicada | Chat | Sonnet 5.5 · medio | Sí (chat nuevo) |
| **Lun 23** | B. Montar `tl/english`, selector de idioma, glosario, inventario de texto fuera del diálogo | Code | Opus 5.5 · alto | Sí |
| **Mar 24** | C1. Prólogo + apertura (~6.000) | Code | Sonnet 5.5 · alto | Sí |
| **Mar 24** | C2. Los 5 eventos de hermana (~7.700) | Code | Sonnet 5.5 · alto | Sí |
| **Mar 24** | C3. Beats de Itsuki, Nino y casa + final malo (~9.800) | Code | Sonnet 5.5 · alto | Sí |
| **Mié 25** | C4. Conexiones (~8.800) | Code | Sonnet 5.5 · alto | Sí |
| **Mié 25** | C5. Evento 6, primera mitad (~6.500) | Code | Sonnet 5.5 · alto | Sí |
| **Mié 25** | C6. Evento 6, segunda mitad (~6.500) | Code | Sonnet 5.5 · alto | Puede seguir la del Dom 29 si el contexto no está lleno; si no, nueva |
| **Jue 26** | D. Interfaz, minijuegos, chat de grupo, boletín, créditos, imágenes con texto | Code | Opus 5.5 · alto | Sí |
| **Jue 26*** | E1. Control automático (revisor) + pruebas manuales, primera mitad | Code | Opus 5.5 · alto | Sí |
| **Jue 26*** | E2. Pruebas manuales, segunda mitad + correcciones | Code | Sonnet 5.5 · medio | Puede seguir la del Mié 2 |
| **Vie 27** | F1. Builds Windows/Android/Linux, publicar v1.1 | Manual (launcher) | — | — |
| **Vie 27** | F2. Página de itch bilingüe, devlog v1.1, encuesta en inglés, textos de redes | Chat | Sonnet 5.5 · medio | Sí (chat nuevo) |
| **Sab 28** | Colchón. Si sobra: leer las respuestas de la encuesta y erratas en español | Chat | Opus 5.5 · alto | Sí |

**Por qué estos modelos**
- **Opus 5.5 · alto**: tareas de motor e interfaz (montaje, imágenes, revisor), donde un error se propaga a todo el juego.
- **Sonnet 5.5 · alto**: traducción en volumen. Rinde bien con un glosario claro y cuesta bastante menos. Si un día
  el tono de un personaje no convence (humor de Nino, Isanari, juegos de palabras), repetir ese bloque con Opus.
- **Sonnet 5.5 · medio**: encuesta, página, redes y correcciones puntuales.
- Una sesión de Code por día de traducción: cada día lee el glosario y archivos grandes, y una sesión
  demasiado larga empieza a perder detalles.

---

## 4. Prompts listos para copiar

### A · Lun 23 · Encuesta (Chat, Sonnet 5.5 · medio, chat nuevo)

```
Lee docs/PLAN_TRADUCCION_Y_ENCUESTA.md del proyecto. Hoy toca la tarea A: la encuesta en español
para jugadores del Prólogo + Cap. 1 de The Fifth Choice.

Requisitos:
- Para Google Forms, con secciones y saltos condicionales. Duración de 5 a 8 minutos, unas 15-20 preguntas.
- Primero preguntar qué jugó cada persona (plataforma, hasta dónde llegó, despido temprano,
  qué eventos de hermana jugó, si jugó más de una partida), porque cada partida ve solo 3 de los 5 eventos.
- Calificar del 1 al 5 a cada personaje (Ichika, Nino, Miku, Yotsuba, Itsuki, Raiha, Isanari, Maruo
  y el protagonista), con la opción "no jugué su evento".
- Escalas antes que sí/no. Nada en negativo. Sin edad exacta. Contacto opcional solo para avisar del Cap. 2.
- Incluir: historia, ritmo, peso de las decisiones, minijuegos (dificultad y diversión), barra de progreso,
  bugs, lo mejor, lo que cambiarías, qué esperan del Cap. 2, recomendación de 0 a 10.
- Sin spoilers en el enunciado de las preguntas.

Entrégame: título, texto de bienvenida, cada sección con sus preguntas, el tipo de pregunta de Forms,
las opciones y la lógica de salto. Después, un texto corto para publicar el enlace en el devlog de itch,
en TikTok y en Instagram.
```

### B · Lun 23 · Montaje de la traducción (Code, Opus 5.5 · alto, sesión nueva)

```
Lee docs/PLAN_TRADUCCION_Y_ENCUESTA.md, docs/GUIA_RENPY.md y docs/GUIA_UI.md antes de tocar nada.
Hoy toca la tarea B: preparar el juego para la traducción al inglés. Todavía no traduzcas diálogo.

1. Verifica que no existe game/tl/. Indícame cómo generar las plantillas desde el launcher de Ren'Py 8.5.3
   (Generate Translations → idioma "english") o genéralas tú por línea de comandos si es posible. Revisa
   que se hayan creado los archivos en game/tl/english/ y que el bloque "translate english strings" incluya
   los textos de la interfaz.
2. Busca texto visible que NO entre en las plantillas: cadenas sin _() en screens, minijuegos, chat de grupo,
   boletín, barra de progreso, créditos, hub_mapa, extras, notificaciones, y textos armados con Python.
   Envuélvelos con _() o la solución correcta de Ren'Py, sin cambiar el texto en español.
3. Añade un selector de idioma (Español / English) en Preferencias, con el estilo de GUIA_UI.md.
   Código completo, cada show con su posición. Déjalo preparado para añadir más idiomas (ver sección 6: ruso).
4. Haz un inventario de imágenes con texto incrustado (boletín, carteles, títulos, chat, etc.) en
   docs/IMAGENES_CON_TEXTO.md: ruta, qué texto lleva y cómo se reemplazará en inglés (imagen alternativa en
   game/tl/english/ con la misma ruta relativa, o Text de Ren'Py). Comprueba en la documentación de Ren'Py
   8.5.3 cómo funciona el reemplazo de imágenes por idioma antes de proponerlo.
5. Crea docs/GLOSARIO_EN.md con: nombres (orden y escritura), honoríficos (te pido que me plantees la decisión:
   conservar -kun/-san/-chan o adaptarlos), materias (Japonés y Literatura = una sola materia), apodos,
   términos recurrentes, y una ficha de voz en inglés para cada personaje (Ichika, Nino, Miku, Yotsuba,
   Itsuki, Raiha, Isanari, Maruo, el protagonista y el narrador), basada en cómo hablan en los .rpy.
   Deja marcadas con [DECIDIR] las dudas que tenga que resolver yo.
6. Crea docs/ERRATAS_ES.md vacío, con una cabecera que explique para qué sirve.
7. Ejecuta lint y confirma que el juego arranca y cambia de idioma, aunque las líneas sigan en español.
8. Copia este plan a docs/PLAN_TRADUCCION_Y_ENCUESTA.md si no está y marca la tarea B como hecha en Progreso.
   Commit y push.
```

### C1 a C6 · Traducción diaria (Code, Sonnet 5.5 · alto, sesión nueva cada día)

Cambia solo la línea de **ARCHIVOS DE HOY**.

```
Lee docs/PLAN_TRADUCCION_Y_ENCUESTA.md (sección 2, Reglas) y docs/GLOSARIO_EN.md completos.
Hoy toca traducir al inglés.

ARCHIVOS DE HOY: <ver tabla>
  C1: tl/english/01_prologo.rpy + 02_cap1_apertura.rpy
  C2: tl/english/02_cap1_Ichika, _Nino, _Miku, _Yotsuba, _Itsuki
  C3: tl/english/02_cap1_beat_Itsuki, _beat_Nino, _beat_casa, _final_malo
  C4: tl/english/02_cap1_conexiones.rpy
  C5: tl/english/02_cap1_evento6.rpy, primera mitad (hasta el label que marques como corte)
  C6: tl/english/02_cap1_evento6.rpy, resto

Cómo trabajar:
- Rellena solo los bloques "translate english" de game/tl/english/. No toques los .rpy en español.
  Lee el .rpy original al lado para tener contexto (quién habla, qué pasa en la escena, qué rama es).
- Inglés natural, no literal. Respeta la ficha de voz de cada personaje del glosario. Adapta los chistes
  en vez de traducirlos palabra por palabra.
- Máximo ~100 caracteres por línea. Conserva [mc] y todas las etiquetas {...} exactamente igual.
- Las opciones de menú también se traducen y deben caber en sus botones.
- Avanza por bloques de escena. Al terminar cada archivo, muéstrame una muestra de 10-15 líneas
  representativas (incluye humor y momentos emotivos) para que yo revise el tono antes de seguir.
- Si encuentras una errata en el español, NO la corrijas: anótala en docs/ERRATAS_ES.md.
- Si un término no está en el glosario, decídelo, añádelo al glosario y avísame.
- Al final: ejecuta lint, cuenta cuántas líneas de los archivos de hoy quedaron sin traducir (debe ser 0),
  actualiza Progreso en el plan, commit y push.
```

### D · Jue 26 · Todo lo que no es diálogo (Code, Opus 5.5 · alto, sesión nueva)

```
Lee docs/PLAN_TRADUCCION_Y_ENCUESTA.md, docs/GLOSARIO_EN.md, docs/IMAGENES_CON_TEXTO.md,
docs/GUIA_UI.md y docs/GUIA_RENPY.md. Hoy toca la tarea D.

1. Traduce el bloque "translate english strings" completo: menús, preferencias, extras, guardado/carga,
   confirmaciones, minijuegos, chat de grupo, boletín, barra de progreso, hub_mapa y notificaciones.
   Revisa que cada texto quepa en su botón o caja. Si no cabe, propón un texto más corto antes que achicar la letra.
2. Créditos: traduce 16_creditos.rpy vía tl/ y añade la sección en inglés a CREDITOS.md, para mantenerlos
   sincronizados. Sin mencionar a Gemini ni ChatGPT.
3. Imágenes con texto: aplica para cada una la solución acordada en IMAGENES_CON_TEXTO.md. Las que haya que
   rehacer a mano, déjalas listadas con el texto exacto en inglés y su tamaño en píxeles.
4. Lint, prueba de arranque en inglés, actualizar Progreso, commit y push.
```

### E1 · Jue 26 · Revisor automático + pruebas (Code, Opus 5.5 · alto, sesión nueva)

```
Lee docs/PLAN_TRADUCCION_Y_ENCUESTA.md y docs/GLOSARIO_EN.md. Hoy toca la tarea E1: control de calidad.

1. Escribe un script en tools/revisar_traduccion.py (solo biblioteca estándar) que recorra game/tl/english/
   y reporte: líneas vacías o idénticas al español; líneas de más de 100 caracteres; [mc] o etiquetas {…}
   que no coincidan con el original; términos del glosario escritos de otra forma; nombres mal escritos.
   Que el idioma sea un parámetro (english por defecto), para reutilizarlo con el ruso.
   Ejecútalo y corrige lo que reporte.
2. Ejecuta lint de Ren'Py y corrige.
3. Arma docs/CHECKLIST_PRUEBAS_EN.md con todas las rutas que hay que jugar en inglés: prólogo, cada uno de
   los 5 eventos en sus 3 ramas, despido variante A y variante B, final malo, los 5 minijuegos, chat de grupo,
   boletín, barra de progreso, créditos y «Continuará», menús y extras, Android (tamaño de texto en pantalla
   pequeña). Usa la consola o los saltos de debug del juego (11_e6_debug.rpy) para llegar rápido a cada punto.
4. Yo juego la checklist. Lo que te reporte, lo corriges. Actualiza Progreso, commit y push.
```

### E2 · Jue 26 · Cierre de pruebas (Code, Sonnet 5.5 · medio; puede seguir la sesión E1)

```
Seguimos con docs/CHECKLIST_PRUEBAS_EN.md. Te voy pasando lo que encuentro jugando; corrige cada punto,
vuelve a ejecutar tools/revisar_traduccion.py y lint al final. Después aplica las erratas de
docs/ERRATAS_ES.md al español, regenera la traducción solo de esas líneas y tradúcelas. Sube la versión a 1.1
en options.rpy, escribe el changelog en docs/CHANGELOG.md, actualiza Progreso, commit y push.
```

### F2 · Vie 27 · Página, devlog y encuesta en inglés (Chat, Sonnet 5.5 · medio, chat nuevo)

```
Lee docs/PLAN_TRADUCCION_Y_ENCUESTA.md y docs/CHANGELOG.md del proyecto. Hoy publico la v1.1 con inglés.

Necesito:
1. Descripción bilingüe para la página de itch.io (adriankiller17.itch.io/the-fifth-choice): primero en
   inglés, después en español. Que se entienda que es un fan game gratis ("name your own price") y que
   nada depende de donar. Plataformas: Windows, Android, Linux. Sin spoilers.
2. Devlog de la v1.1 en los dos idiomas: qué cambió y enlaces a las encuestas.
3. La encuesta de la tarea A traducida al inglés, con la misma estructura para poder comparar las respuestas.
4. Textos cortos para TikTok (@thefifthchoiceo_o) e Instagram (@thefifthchoice) anunciando la versión en inglés.
```

### Vie 27 · Colchón / análisis (Chat, Opus 5.5 · alto, chat nuevo)

```
Lee docs/PLAN_TRADUCCION_Y_ENCUESTA.md. Te paso las respuestas de la encuesta (CSV exportado de Google Forms).
Analízalas: cuántas respuestas hay y qué tan representativas son, calificación media por personaje según
cuántos jugaron su evento, temas que se repiten en las respuestas abiertas, bugs reportados y qué esperan
del Cap. 2. Separa lo que se repite de las opiniones aisladas y dime qué conviene tener en cuenta para el
Cap. 2, sin cambiar su estructura.
```

---

## 5. Progreso

| Tarea | Estado | Fecha | Notas |
|---|---|---|---|
| A · Encuesta ES | ✅ | 23/11 | Se ha generado mas de 200 respuestas de los usuarios en poco tiempo, las respuestas son demasiado útiles para el desarrollo del juego |
| B · Montaje tl / selector / glosario | ✅ | 23/11 | `tl/english` generado por CLI (36 archivos, `new` = copia del español). Texto de interfaz y Python marcado con `_()`/`__()`. Selector en Opciones (tabla `IDIOMAS`). GLOSARIO_EN, IMAGENES_CON_TEXTO (ninguna imagen con texto en español), ERRATAS_ES. 5 [DECIDIR] en el glosario. Las etiquetas de prueba (`prueba`, debug del E6) no se marcaron: no hace falta traducirlas. |
| C1 · Prólogo + apertura | ✅ | 24/11 | 733 bloques + 16 cadenas traducidas; lint sin errores en los archivos de hoy; tono aprobado por Adrian. La placa «Estudiante Nueva» se traduce en la tarea D (`tl/english/00_definiciones.rpy`). Líneas idénticas al español a propósito: nombres y «...». Chiste de «jad tu» adaptado (glosario §11). 1 errata anotada. |
| C2 · 5 eventos | ✅ | 24/11 | Ichika 199, Nino 197, Miku 198, Yotsuba 206, Itsuki 170 bloques + 25 cadenas de menú; lint sin errores; 0 líneas sin traducir (las 25 idénticas al español son «...», «Itsuki.» y «No.»). Tono revisado por Adrian archivo por archivo; Ichika y Nino repasadas después para quitar frases con aire de IA. 1 errata anotada (Itsuki:148). |
| C3 · Beats + final malo | ✅ | 24/11 | beat_Itsuki 121, beat_Nino 198, beat_casa 361, final_malo 479 bloques + 7 cadenas de menú; lint sin errores; 0 líneas sin traducir (las 21 idénticas al español son «...», «No.» y nombres). Tono revisado por Adrian archivo por archivo. 0 erratas. Los recuerdos de beat_casa reutilizan las frases ya traducidas en C1/C2. |
| C4 · Conexiones | ✅ | 25/11 | 1.161 bloques + 16 cadenas de menú; lint sin errores; 0 líneas sin traducir (las 6 idénticas al español son «...» y nombres). Tono aprobado por Adrian. 8 erratas anotadas (7 de tildes/punto y el cartel «Casa de Futaro» con nombre fijo; en inglés va `[nombre_jugador]'s House`). Decisiones en glosario §13. De paso se retocó la línea de la sal de Miku (`02_cap1_Miku.rpy`). |
| C5 · Evento 6 (1/2) | ⬜ | | |
| C6 · Evento 6 (2/2) | ⬜ | | |
| D · Interfaz, minijuegos, créditos, imágenes | ⬜ | | |
| E1 · Revisor + checklist | ⬜ | | |
| E2 · Pruebas + erratas + v1.1 | ⬜ | | |
| F1 · Builds y publicación | ⬜ | | |
| F2 · Página, devlog, encuesta EN | ⬜ | | |
| R0 · Respuesta de winbed13 | 🟨 | 22/11 | Mensaje enviado; esperando respuesta |
| R1 · Preparar tl/russian + fuente + paquete | ⬜ | | Después de F1 |
| R2 · Prueba (prólogo) revisada | ⬜ | | |
| R3 · Traducción completa recibida | ⬜ | | Sin fecha fija; a su ritmo |
| R4 · Integración + build privada de prueba | ⬜ | | |
| R5 · Publicar v1.2 con ruso + créditos | ⬜ | | |

Estados: ⬜ pendiente · 🟨 en curso · ✅ hecho · ⚠️ con problemas (explicar en Notas)

---

## 6. Traducción al ruso (colaborador externo, después de la v1.1)

**Contexto (22/11/2026):** winbed13 (itch.io) se ofreció a traducir el juego al ruso, revisar el texto y probar la build.
Se le respondió que sí, pero que empiece **después de publicar la v1.1 en inglés**. Se le dejó claro que es una
colaboración **voluntaria y sin pago**, con crédito en el juego. Quedó pendiente que diga si lee español o si
traducirá desde el inglés, y por dónde prefiere hablar (itch, Discord o email).

**Qué se le da y qué no**
- Sí: los archivos de `game/tl/russian/`, `docs/GLOSARIO_EN.md`, las reglas de abajo y, más adelante, una build privada.
  El juego ya lo puede descargar de itch para ver el contexto de cada escena.
- No: el repo, los .rpy del juego, imágenes, audio ni acceso a la cuenta de itch. El repo sigue sin compartirse hasta terminar el juego.
- Señal de alerta: que pida dinero por adelantado o acceso a cuentas o al repo.

**Reglas para el traductor**
1. Solo rellena los bloques `translate russian` de los archivos que se le envían; no cambia nada más.
2. `[mc]` y todas las etiquetas `{…}` quedan exactamente igual.
3. ~100 caracteres por línea como máximo (dos líneas de la caja de texto). Las opciones de menú deben caber en su botón.
4. Respeta el glosario (nombres, honoríficos, voz de cada personaje).
5. La versión rusa se publica solo en la página oficial de itch, gratis como el resto del juego.
6. Crédito en `16_creditos.rpy` y `CREDITOS.md` (los dos a la vez), con el nombre que él elija.

**Pasos (Adrian + Claude Code)**
1. **R1 · Preparar** (después de F1, sesión de Code, Opus 5.5 · alto; no ocupa más de una sesión):
   - Generar `game/tl/russian/` desde el launcher (Generate Translations → "russian").
   - Si traduce desde el inglés: script en `tools/` que ponga, junto a cada hueco de `tl/russian`, la línea en inglés
     de `tl/english` como comentario de referencia (las plantillas solo traen el español).
   - **Fuente con cirílico:** comprobar si las fuentes del juego tienen caracteres cirílicos. Si no, definir una
     fuente alternativa solo para el ruso (consultar GUIA_UI.md y GUIA_RENPY.md antes).
   - Añadir "Русский" al selector de idioma.
   - Imágenes con texto: por ahora quedan en inglés en la versión rusa, salvo que él quiera traducirlas
     (en ese caso se le pasa la lista de `IMAGENES_CON_TEXTO.md` con texto y tamaño).
   - Armar el paquete (zip con `tl/russian/` + glosario + estas reglas) y enviárselo.
2. **R2 · Prueba corta:** primero solo el prólogo. Revisar con traductor automático y, si se puede, con alguien
   que hable ruso. Si la calidad convence, sigue con el resto.
3. **R3 · Traducción completa:** a su ritmo, sin fecha fija. No bloquea el Cap. 2.
4. **R4 · Integrar:** copiar sus archivos a `game/tl/russian/`, ejecutar `tools/revisar_traduccion.py russian` y lint,
   generar una build privada (Google Drive, no itch) para que él la pruebe y reporte errores.
5. **R5 · Publicar v1.2:** builds en itch, créditos actualizados, devlog mencionándolo.

**Capítulos 2 y 3:** al publicar cada capítulo nuevo se repite el ciclo solo con el texto nuevo. La regla de congelar
el español también vale para el ruso: si se corrige una línea en español, su traducción rusa queda huérfana y hay que avisarle.
