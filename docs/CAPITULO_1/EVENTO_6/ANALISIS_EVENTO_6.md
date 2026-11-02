# Análisis del Evento 6 — cierre del Capítulo 1

> **Estado:** análisis cerrado. **No contiene guion final ni código.**
> **Redactado:** 31/10/2026, contra el repo tal como llegó a este chat (docs, `.rpy` y scripts de `herramientas/`).
> **Ruta en el repo:** `docs/CAPITULO_1/EVENTO_6/ANALISIS_EVENTO_6.md`
> **Plan de trabajo:** `docs/CAPITULO_1/EVENTO_6/PLAN_CHATS_EVENTO_6.md` (misma carpeta).

**Cómo leerlo.** Los hechos verificados en el repo llevan `F-xx`. Las decisiones que necesito de ti llevan `P-xx` (lista completa en §8; el registro vivo está en el plan, §1). «Mov.» es un movimiento del Evento 6, como en los hubs. Los IDs del anexo de minijuegos (Y2, I1, N1, It1, M3) se mantienen tal cual.

**Glosario.**

| Término | Significa |
|---|---|
| `estado_entrada` | `superado` · `mixto` · `bueno`. Se calcula una vez al entrar a E6. |
| `estado_h` | Estado de la hermana *h*: `calida` · `tibia` · `fria` · `no_visitada`. |
| Bloque | La secuencia de una hermana en su día de examen. |
| Capas | Piezas intercambiables de un bloque: núcleo, monólogo, minijuego, gesto, final, promesa. |

**Alcance de la auditoría.** Revisé texto y código. **No pude verificar** qué archivos de imagen o audio existen en disco (solo lo que `.rpy`, README y guías declaran). Cuando algo depende de un asset, lo marco.

---

## 0. Resumen ejecutivo

1. **E6 es el negativo fotográfico del Final Malo B.** `02_cap1_final_hub3.rpy` ya escribió la semana de exámenes en el aula con Futaro en la segunda fila, de lunes a viernes, en este orden: Yotsuba/Japonés, Ichika/Matemáticas, Nino/Inglés, Itsuki/Ciencias, Miku/Sociales. Luego Maruo con cinco boletines en fila, las despedidas por las puertas, el curry y la libreta. Diseñar E6 como la inversión punto por punto es lo más barato y lo más potente (Anexo A).
2. **La entrada ya está resuelta por el código.** Tres estados: `superado` (8 de 20 combinaciones de rama que sobreviven), `mixto` (8) y `bueno` (4). Siempre hay **como máximo una hermana fría** y **como máximo tres cálidas**. **4 de 20 combinaciones no tienen ningún minijuego.**
3. **Tu hipótesis del punto 7** acierta en la dirección y se queda corta. En no-cálida el monólogo no puede girar alrededor de MC; pero «menos MC» describe mal a la *fría* (piensa en MC, herida) y deja a *tibia* y *no visitada* sin diferencia. La reemplazo por un **modelo de focos + frase cortada** (§3).
4. **Los CG `*_fracaso` no son un examen anterior.** Son la semana real de exámenes del Final B (contrafactual). Quien sobrevive nunca los ve. Espejarlos conviene como **lenguaje visual**, no como payoff que dependa de haberlos visto (§1.7).
5. **Las no visitadas** tienen rama `None`, no tienen minijuego y sí material previo: las `queja_*` del viernes y, solo Nino e Itsuki, un beat fijo. E6 es el único sitio donde pueden recibir un gesto de MC: propongo una **promesa pendiente** que además siembra el Capítulo 2.
6. **`interconexion_6` ya gastó** la última sesión de estudio, la visita de Maruo del viernes, el chat y las puertas del domingo. El plan viejo de `CAP1.md` §4 (mesa con cinco hojas) está obsoleto: **E6 arranca el lunes.**
7. **Minijuegos elegidos:** Y2 relevo, I1 audición (modificada: *la máscara se cansa*), N1 compras (modificada: *para seis*), It1 conversiones con *levantar la mano*, M3 ritmo con audífonos (con el reloj del aula como segunda fase). Descarto Y3 y M1 con motivo (§5.1).
8. **Modelo de variantes:** núcleo + 6 capas. ≈ **830 líneas autoradas**, ≈ **400 leídas por partida**, **6–8 CG**. Sin escenas paralelas completas.
9. **Hallazgo de economía de puntos (importante):** el código da cálida +3 / tibia +1 / fría 0 por hub, no el +2 +1 de los docs. Con 3 hubs por capítulo y una visita por hermana, el techo por hubs en tres capítulos es 9, **por debajo del umbral de 10** (§1.9, P-09).
10. **Frustración:** «repetir hasta ganar» en *difícil* es el mayor riesgo del movimiento. Recomiendo puntos de control por fase, líneas de fallo *con carácter* (fallar es desarrollo, no castigo) y asistencia adaptativa que respete el boost de Nino (§5.5). La decisión es tuya.
11. **Qué no hacer:** que el minijuego decida notas o aprobar, mostrar números de afecto, gastar la disculpa de Itsuki, resolver la confianza de Nino, kanji, duelos (§6).
12. **Riesgos principales:** sincronía de audio en M3, pausa/rollback/skip en pantallas de juego, fatiga por cinco bloques seguidos, y duplicar el texto del beat casa (§8).

---

## 1. Auditoría del repo

### 1.1 Flujo real y dónde engancha E6

| Tramo | Label / archivo | Siguiente |
|---|---|---|
| Prólogo | `prologo` (`01_prologo.rpy`) | `jump cap1_apertura` |
| Apertura | `cap1_apertura` (`02_cap1_apertura.rpy`) | `jump cap1_interconexion_1` |
| Interconexión 1 | `02_cap1_conexiones.rpy` | `jump hub_1` |
| Hub 1 / 2 / 3 | `02_cap1_hubs.rpy` → `call expression (LABEL_EVENTO…)` → `hub_visitadas.append(destino)` | `cap1_interconexion_2` / `_4` / `_6` |
| Interconexión 2 | reacciones + chisme de Nino | `call beat_Itsuki` → `cap1_interconexion_3` |
| Interconexión 4 | reacciones + «quien lee a las demás» | `call beat_Nino` → `cap1_interconexion_5` |
| Hub 3 | tras el evento: `if maruo_ultimatum and rama_de(destino) == "fria": despido_cap1 = True` | `cap1_interconexion_6` |
| Interconexión 6 | clima, quejas de no visitadas, sesión del viernes, Maruo (si ultimátum), chat, puertas del domingo | `call beat_casa` |
| Salida | `if despido_cap1: jump final_malo_temprano` / `else: jump evento_6` | **`evento_6` no existe todavía** |

**F-01.** `jump evento_6` es el único punto de entrada. Al llegar por `jump`, la pila de `call` está vacía: los bloques internos deben usar `call … return`.
**F-02.** No existe destino posterior a E6 (`03_capitulo2.rpy` pendiente). E6 debe terminar en un `jump` a un stub de Cap. 2.

### 1.2 Variables y flags relevantes

| Variable | Valores | Se escribe en | Se lee en | Uso en E6 |
|---|---|---|---|---|
| `desaires_cap1` | int | hubs (rama fría `+= 1`) | `beat_Nino` | Solo lectura. No escribir. |
| `maruo_ultimatum` | bool | `beat_Nino` cuando `desaires_cap1 == 1` | hub 3, interc. 5 y 6 | Define `estado_entrada = superado`. |
| `despido_cap1` | bool | hub 3 | interc. 6, `beat_casa` | Siempre `False` en E6 (assert). |
| `clima_cap1` | `buena` / `mixta` / `mala` | interc. 6 | interc. 6 | En E6 solo `buena` o `mixta`. |
| `nino_rama_beat` | `None` / `calida` / `tibia` / `fria` | `beat_Nino` | interc. 5 | **Boost de dificultad** si `calida`. |
| `<h>_rama_cap1` | `None` / `calida` / `tibia` / `fria` | hubs | `rama_de(h)` | `None` = no visitada. |
| `<h>_visitada_cap1` | bool | final de cada hub | `beat_casa`, collage | Redundante con `rama_de(h) is not None`. |
| `hub_visitadas` | lista, **con orden** | hubs | hubs, interc. 6 | Orden de visita disponible (la última = hub 3). |
| `destino` | str | hubs | interc. | Tras hub 3 es la hermana del último hub. |
| `tiempo_restante` | str | hubs | HUD (`"Quedan " + …`) | Reutilizable como «Quedan cuatro exámenes». |
| `puntos_*`, `primera_conexion` | int / str | `sumar_punto` | cálculo final | Ver P-09. |

**F-03.** `rama_de(h)` devuelve `None` si no hubo hub con *h*. Es el test más limpio para «no visitada».
**F-04.** `nino_rama_beat` es **independiente** de la rama de hub de Nino. Hay cuatro combinaciones útiles (hub ∈ {c, t, f, ninguna}) × (beat ∈ {c, t, f}). El beat siempre se juega en los 20 sobrevivientes.
**F-05.** Tu texto dice que el beat de Nino ocurre «antes de su hub». No siempre: el beat va tras el hub 2, y el hub de Nino puede ser el 1, el 2 (antes del beat) o el 3 (después). Da igual para el boost (solo lee `nino_rama_beat`), pero conviene no escribir «antes de su hub» en el guion.

### 1.3 Los tres estados de entrada (derivados del código)

Sea (r1, r2, r3) la rama elegida en los hubs 1, 2 y 3 (c = cálida, t = tibia, f = fría).

- `beat_Nino`: dos frías en hubs 1–2 → despido A. Una fría → `maruo_ultimatum = True`. Ninguna → sin aviso.
- Hub 3: con ultimátum y fría en hub 3 → despido B.
- `clima` (interc. 6): `mala` si despido; `buena` si `n_frias == 0` y `n_calidas ≥ 2`; `mixta` en lo demás. `contar_ramas` cuenta las cinco variables `*_rama_cap1`.

De 27 combinaciones: 3 terminan en A, 4 en B, **20 sobreviven**.

| `estado_entrada` | Condición | Combinaciones | Clima |
|---|---|---|---|
| **superado** | `maruo_ultimatum` y hub 3 no fría | 8 | siempre `mixta` (hay ≥ 1 fría) |
| **mixto** | sin ultimátum y clima `mixta` | 8 (4 sin fría + 4 con fría solo en hub 3) | `mixta` |
| **bueno** | sin ultimátum, 0 frías, ≥ 2 cálidas | 4 | `buena` |

Se calcula así: `superado` si `maruo_ultimatum`; si no, `bueno` si `clima_cap1 == "buena"`; si no, `mixto`.

**F-06 (invariantes que simplifican todo).**
- **Como máximo una hermana fría** por partida (dos frías siempre desembocan en despido).
- **Como máximo tres cálidas** (y por tanto tres minijuegos).
- Siempre hay **exactamente 3 visitadas y 2 no visitadas**.
- **Minijuegos por partida:** 0 en 4 de 20 combinaciones, 1 en 9, 2 en 6, 3 en 1 (Anexo B).
- En `superado` Maruo *apareció el viernes* («Veo que no la desperdiciaste… No te confíes»). En `mixto` y `bueno` no.

### 1.4 Qué tiene ya cada hermana, esté o no visitada

| Hermana | Si visitada | Si no visitada | Material propio fuera del hub |
|---|---|---|---|
| Yotsuba | hub (3 ramas), `reaccion_yotsuba`, interc. 4 | `queja_yotsuba` | interc. 5 (nerviosa, lápiz al revés) |
| Ichika | hub (3 ramas + mensaje del papel), `reaccion_ichika` | `queja_ichika` | interc. 1 y 5 |
| Nino | hub, `reaccion_nino`, chisme | `queja_nino` | **beat crisis (siempre)** + interc. 5 en 3 ramas |
| Miku | hub, `reaccion_miku` | `queja_miku` | interc. 5 («somos cinco») |
| Itsuki | hub, `reaccion_itsuki` | `queja_itsuki` | **beat azotea (siempre)**, interc. 3 y 5 |

**F-07.** Las no visitadas **no tienen rama** y **no corresponde minijuego** (rama `None` ≠ `calida`). Sí tienen una `queja_*` (interc. 6, solo para las que no están en `hub_visitadas`), y esa queja es oro: cada una deja dicho qué esperaba de MC. E6 puede **responder a esa queja**.
**F-08.** Ichika, Miku y Yotsuba son las que menos material tienen si no se visitan. Por eso E6 debe cargar *más* con ellas, no menos.

### 1.5 Setups sin resolver (lo que E6 puede cobrar)

| # | Setup | Origen | Cobro propuesto en E6 |
|---|---|---|---|
| 1 | «Hagan lo que **sepan**» (frase de relleno) | Final B, Mov. 2 | «Hagan lo que **saben**». Un cambio de modo verbal. |
| 2 | «Veinticinco es un número perfecto» / «No lo es» | Hub Yotsuba, reacción cálida | El perfecto es el **28**; contador de vueltas. |
| 3 | «1» con corazón torcido en la muñeca de MC | `reaccion_yotsuba` cálida | «1» → «**100**» (solo cálida). |
| 4 | «Un uno por ciento bien hecho» | Prólogo, Final B | 100 en Japonés. |
| 5 | «Las batallas las gana quien mueve el arroz» | Prólogo, Miku | Pregunta de rutas de comercio; la **sal**. |
| 6 | «Lo vas a comprobar en tres semanas» | Hub Miku, cálida | El examen *es* el comprobante. |
| 7 | «Cuando llegues a la página de la sal, avísame. Quiero ver tu cara» (MC iba por la 95) | `reaccion_miku` cálida | MC llegó. Primera sonrisa de Miku. |
| 8 | «Y a mí eso me parece mucho más—» (frase cortada) | Hub Miku | Miku la **termina**. |
| 9 | Goma / marca de borrador, «Perdón» | Apertura, hub, Final B | Goma entera; primera frase sin «…» inicial. |
| 10 | «El último duró cuatro días» | Nino, prólogo y apertura | «Treinta y cinco.» |
| 11 | «Solo el tiempo lo va a demostrar» | Hub Nino, cálida | El tiempo pasó. |
| 12 | «Anota la fecha» | Nino fría (`reaccion_nino`, Final B) | Inversión («Anota la fecha. Es hoy»). |
| 13 | Tarjeta de receta vieja | Hub Nino | **No resolver** (hueco para Cap. 2). |
| 14 | «Ni se te ocurra decirme la respuesta» | Prólogo, Final B | Levanta la mano al *profesor*, no a MC. |
| 15 | Conversión de unidades; «dónde mirar» | Hub Itsuki | Trampa del número arrastrado. |
| 16 | **Disculpa guardada** de MC (y de Itsuki) | Prólogo → docs | **No gastar.** Intento interrumpido. |
| 17 | «El juego se acabó hoy» / «El juego sigue» | Itsuki, interc. 3 y 6 | Ella cierra el juego que abrió. |
| 18 | Tren de las 4:45, «martes 5:20», horario tachado | Hub Ichika | Problema de examen con trenes. |
| 19 | Papel nuevo de la obra aceptado sin pensar | Hub Ichika (m5), Final B4 | Dato canónico en cualquier estado. |
| 20 | «¡Se que podrás lidiar con cinco a la vez!» / «Entonces no entiendo el problema» | Raiha, apertura y Final B | Coda en casa. |
| 21 | «Gracias por la comida» sin sentir nada | Final B8 | Esta vez lo siente. |
| 22 | Chat «¡Equipo Quintillizas + Tutor!» (Nino se sale, Yotsuba la vuelve a meter) | Interc. 6, sábado | Nino **no se sale**. Pantalla de revelación final. |
| 23 | «Las notas son lo único que puedo controlar» / «la nota que más me importaba no era la mía» | Prólogo, interc. 6 | «Lo único que controlé fue a dónde fui.» |
| 24 | Cinco puertas con raya de luz (cinco / tres / una) | Interc. 6, domingo | Las puertas se *abren*. Las dos no visitadas, las últimas. |
| 25 | Maruo: «si una sola reprueba…» | Prólogo, apertura | Se cumple; condición futura. |

### 1.6 Materia fuerte confirmada

| Hermana | Materia | Fuentes |
|---|---|---|
| Ichika | Matemáticas | README; hub (calcula minutos y trenes); Final B3.2 |
| Nino | Inglés | README; hub (lee etiquetas); Final B3.3 |
| Miku | Sociales / Historia | README; hub (Sengoku); Final B3.5 |
| Yotsuba | Japonés / Literatura | README; hub («comprensión lectora con personas»); Final B3.1 |
| Itsuki | Ciencias | README; hub (conversión); Final B3.4 |

Coincide con tu lista y con el orden L→V del Final B.

### 1.7 Qué son los CG de examen 3.1–3.5 (punto 8 del contexto)

**F-09.** Son `cg_yotsuba_fracaso`, `cg_ichika_fracaso`, `cg_nino_fracaso`, `cg_itsuki_fracaso` y `cg_miku_fracaso`, declarados en `02_cap1_final_hub3.rpy` (`images/cg/cap1_final_malo/`). Solo se muestran dentro de `final_malo_hub3` y viven en la pestaña de cada hermana de la Galería. **No son un examen anterior**: son la semana real de exámenes de la línea en que MC fracasa.
**F-10.** Receta común (según `CAP1_FINAL_MALO.md`): POV desde el pupitre de MC, primer término con su examen terminado boca abajo, un lápiz y el canto de una mano; la hermana al fondo. Una silueta distinta por hermana.
**F-11.** Un jugador que sobrevive **no los ha visto**. Si el payoff dependiera de ellos, solo lo recibiría quien vio el Final B.

**Evaluación del espejo.** Conviene, con tres condiciones:
1. El espejo funciona **sin** haber visto el B: la mirada de cada hermana, la hoja y las manos cuentan la inversión por sí solas.
2. Los CG de E6 son **estado-agnósticos** (sirven en las cuatro ramas) para no multiplicar arte.
3. **Misma cámara, mismo primer plano.** Si guardaste las semillas de los `*_fracaso`, reutilízalas (P-15); si no, copia la composición y el prompt y acepta un fondo algo distinto.

Bonus barato para quien vio el B: **díptico en la Galería** (par «antes/después») y una capa opcional de líneas espejo por `persistent` (P-17).

### 1.8 Discrepancias entre docs, código y prompt

| # | Discrepancia | Gravedad | Qué hacer |
|---|---|---|---|
| 1 | **Puntos:** docs dicen +2 por visita +1 por decisión y beats +0; el código da cálida +3, tibia +1, fría 0, y `beat_Nino` cálida **+1**. | **Alta** | P-09. |
| 2 | **`CAP1.md` §4** describe E6 como mesa del departamento con cinco hojas y examen «en negro, sin Futaro». `CAP1_FINAL_MALO.md` y tu prompt lo mueven al aula con MC presente. | Alta | Plan nuevo (P-03). Actualizar docs **al final** (pediste no tocar README/CAP1.md hasta cerrar el capítulo). |
| 3 | `CAP1.md` y README siguen diciendo «tres desaires» y «preparar material» / «revisita +1»: **no existen en el código** (no hay revisitas ni «preparar material»). | Media | Quitar de E6 cualquier línea «si se preparó material». |
| 4 | `beat_casa` doc dice «el jugador elige **una** opción»; el código obliga a recorrer **las cinco**. | Media | E6 no puede repetir los pensamientos de MC sobre cada hermana. |
| 5 | Tren de Ichika: doc «5:45», código «4:45». | Baja | Usar el del código. |
| 6 | Nombres: docs `itsuki_sorpresa` / `nino_nerviosa` vs código `itsuki sorprendida` / `nino nerviosa`. | Baja | Usar los del código. |
| 7 | `itsuki timida` «solo en la grieta» (doc) pero el código la usa en beat, reacción y Final B. | Baja | Regla ya rota; E6 puede usarla solo en la frase. |
| 8 | `hub_visitadas` no se reinicia en ningún sitio. | Media | Cap. 2 debe reiniciarla. |
| 9 | La fría **no** llama a `sumar_punto`, así que no escribe `primera_conexion`. | Baja (no puede pasar con 1.ª fría + 1.ª decisión, ver F-06) | Anotarlo. |

### 1.9 Economía de puntos (hallazgo para P-09)

Con el código actual, por hub: cálida +3, tibia +1, fría 0. Cada hermana se visita **una sola vez por capítulo** (la lista de visitadas bloquea repetir). Más el beat de Nino (+1 si cálida).

- Techo por hermana por capítulo: **3** (Nino: 4).
- Techo en tres capítulos si Cap. 2 y 3 repiten la estructura: **9** (Nino: 12). El umbral es **10**.
- Si el README se cumpliera («máx. 5 por capítulo»), un jugador concentrado cruzaría 10 en el Cap. 3. Con el código, **solo Nino puede**.

**Opciones:** (a) E6 da **+1** por minijuego ganado en cálida (techo 4 por capítulo y por hermana); (b) E6 da 0 y se reequilibra en Cap. 2–3; (c) se baja el umbral tras medir. Recomiendo (a), con la condición de que el +1 vaya por `sumar_punto` y **solo en cálida**. La decisión es tuya (P-09).

### 1.9b Inventario reutilizable

- **BG:** `bg_aula`, `bg_aula_tarde`, `bg_aula_anochecer`, `bg_escuela`, `bg_departamento(_anochecer)`, `bg_comedor`, `bg_cuarto_mc`, `bg_negro`; más `bg_pista_atletismo`, `bg_sala_ensayo`, `bg_centro_comercial`, `bg_biblioteca` (y sus `_anochecer`).
- **CG ya existentes útiles:** `cg_maruo_reunion`, `cg_maruo_espaldas`, `cg_libreta`, `cg_cinco_estudiando`, `cg_cinco_repasando`, `cg_hermanas_estudiando`, `cg_cinco_sentadas`.
- **Sprites:** todas las expresiones de las cinco, Raiha e Isanari (incl. `ichika agotada/determinada`, `nino nerviosa/pillada/molesta`, `miku animada/relajada/encogida`, `yotsuba incomoda/sorprendida/neutral`, `itsuki timida/sorprendida`).
- **Audio:** `<hermana>` (tema por hermana), `descubrimiento`, `guardia`, `tregua`, `cotidiano`, `hogar`, `cena`, `contrato`, `derrota`, `amb_reloj`, `amb_viento`, SFX de hoja, timbre, lápiz, papel, puertas, celular, hover/click.
- **UI:** `ui_escena("beat", hermana, lugar)` tiñe la cinta y las esquinas con el color de la hermana y muestra «Quedan [tiempo_restante]». Es identidad visual gratis para cada bloque.
- **`ui_personaje`:** admite crear cajas de **voz interior** por hermana con cambios mínimos (§3.7).

---

## 2. Arco por hermana

Convención: **Cálida / Tibia / Fría / No visitada** = `estado_h`. «Frase» = la línea que condensa el cambio (candidata, a validar en P-05). La frase *completa* solo la dice la cálida; las otras tres la dicen **cortada**, **cerrada** o **desplazada** (modelo de §3.3).

Tabla resumen de frases:

| Hermana | Cálida (completa) | Tibia (cortada) | Fría (cerrada) | No visitada (espera) |
|---|---|---|---|---|
| Yotsuba | «Yo importo igual que mis hermanas.» | «Yo también im—» | «Lo mío es correr. Está bien.» | «Si nadie me necesita… entonces la reparto.» |
| Ichika | «No tengo que poder con todo.» | «No tengo que po— ¡Siguiente pregunta!» | «Estoy bien. Que conste.» | «Si no sé qué hacer, actúo. …Siempre.» |
| Nino | «No pienso adelantar el golpe.» | «Quizás esta vez no—» | «Anota la fecha. Es hoy.» | «Alguien tiene que ver venir el golpe. …Sigo siendo yo.» |
| Itsuki | «Preguntar no es perder.» | «Preguntar sería—» | «No necesito preguntar.» | «Lo resuelvo sola. Como siempre. …Tarde, pero sola.» |
| Miku | «Dejaré de tener miedo a lo que más amo.» | «…Lo que amo no—» | «…Hoy no.» | «…Soy buena esperando.» |

Cada frase escribe `e6_frase[h]` ∈ {`completa`, `cortada`, `cerrada`, `espera`}. **La frase cortada de Cap. 1 se completa en Cap. 2** (payoff diferido, §6).

---

### 2.1 Yotsuba — Japonés (lunes)

| Campo | Contenido |
|---|---|
| **Empezó** | Sonrisa de tapón; «…¿Verdad?» medio tono más bajo; escribe solo su nombre («un uno por ciento»); obedece a Nino aunque no esté de acuerdo. |
| **La dejó el juego** | *Cálida:* «tu punto de partida no es cero»; duda «¿verdad o animar?»; marcó un «1» con corazón torcido en la muñeca de MC. *Tibia:* cronómetro, 1:17 → 1:14, esquivó el tema. *Fría:* dejó de contar en voz alta; lo llama «tutor». *No visitada:* entrenó «por si venías», «tres vueltas de ventaja»; «si nadie me necesita, ¿para qué me sobra tanta energía?». |
| **Cambio en E6** | De «valgo por lo que doy» a «valgo sin dar». |
| **Recurso formal** | Exclamaciones. Se apagan en la grieta y vuelven al defenderse. La frase de cambio va **larga y sin signos**; la exclamación regresa al final. |
| **Minijuego** | **Y2 · Relevo de las cinco.** Cada tramo mide lo mismo: el diseño dice «importas igual». |
| **Setups que cobra** | 28 (el número perfecto); «1» → «100» en la muñeca (solo cálida); «un uno por ciento»; «si alguna reprueba, se acaba todo» (interc. 5). |
| **Tibia** | Responde la pregunta 1 con su propia soledad y se corta («Yo también im—»). Flag `cortada`. |
| **Fría** | Escribe lo justo, entrega primera, **no mira a nadie**. Su don (leerlas) se apaga: gancho para Cap. 2. |
| **No visitada** | Monólogo con callback a su queja; reparte energía a los demás. MC le **promete** ver «las veinticinco vueltas». |
| **Pregunta de examen** | «¿Qué siente el protagonista cuando se queda solo?» (ya sembrada en Final B3.1). Respuesta cálida: «que alguien llegara». |

### 2.2 Ichika — Matemáticas (martes)

| Campo | Contenido |
|---|---|
| **Empezó** | Sonrisa fácil; «la mayor, aunque no sirva de mucho»; duerme; actúa. |
| **La dejó el juego** | *Cálida:* «no sé cuánto más puedo seguir»; «gracias por no decir la frase obvia»; durmió «siete y cuarto, redondeo hacia arriba». *Tibia:* hablaron de dragones. *Fría:* «correcta» como con un padre; sonrisa tarde. *No visitada:* «ensayé tres formas de reaccionar cuando me encontraras… no sé si podría con otra cosa». Dato canónico para todas: aceptó el **papel nuevo** (Final B4 lo confirma). |
| **Cambio en E6** | De «puedo con todo» a «no tengo que poder con todo». |
| **Recurso formal** | Actuación constante; en la grieta, frases planas sin exclamación; la máscara vuelve medio segundo tarde. |
| **Minijuego** | **I1′ · La máscara se cansa.** Líneas *actuadas* (toque rápido, sube la máscara) o *sinceras* (mantener pulsado, baja la máscara). La mecánica es la metáfora. |
| **Setups que cobra** | Problema de examen con trenes (la punta que el hub «nombra y no desarrolla»); horario tachado; papel de la obra; «estoy bien». |
| **Tibia** | Resuelve rápido, se sorprende, y escapa con humor justo antes de la verdad (frase cortada). |
| **Fría** | Examen correcto, sonrisa puesta; «estoy bien. Que conste». |
| **No visitada** | Resuelve de memoria sin saber por qué; el monólogo nombra el hábito («si no sé qué hacer, actúo»). MC le promete verla ensayar **despierta**. |
| **Pregunta de examen** | Problema de trenes y minutos. El resultado «le sale tan rápido que se asusta». |

### 2.3 Nino — Inglés (miércoles)

| Campo | Contenido |
|---|---|
| **Empezó** | «No vas a durar ni una semana»; organiza el sabotaje; corrige un *had to* sin pensarlo. |
| **La dejó el juego** | *Hub cálida:* «primera vez que alguien no me promete nada». *Tibia:* «esto no significa nada». *Fría:* «guárdate la promesa». *No visitada:* «alguien tiene que ser la que no cambia». **Beat (siempre)**, aparte de la rama de hub: cálida «¿y quién junta los tuyos?» (+ cebollas), tibia (la taza), fría («hablan el mismo idioma»). |
| **Cambio en E6** | De «ver venir el golpe» (control por anticipación) a «no adelantarlo». **No** pasa a confiar: a lo sumo «no confío… todavía». |
| **Recurso formal** | Frases cortas sin dejar contestar; en la grieta habla de más y se corta. |
| **Minijuego** | **N1′ · Compras para seis.** Cinco listas, una por hermana, y un sexto hueco: comprar *antes* de saber el resultado. La traducción aparece sola (traduce sin darse cuenta). |
| **Setups que cobra** | «El último duró cuatro días» → «treinta y cinco»; «solo el tiempo lo va a demostrar»; «anota la fecha»; no se sale del chat; Final B3.3 (se queda «revisando»). **No** cobra la tarjeta de receta. |
| **Dos capas** | Estado de hub (4) **y** `nino_rama_beat` (3): el beat añade una línea de capa extra y **fija la dificultad** de los minijuegos. |
| **Tibia** | Termina primera y se queda «revisando» como en el Final B (nada cambió). |
| **Fría** | Se queda y no mira a MC; la frase invierte su amenaza. |
| **No visitada** | Se queda revisando para cuidar a las demás; gancho: «sigo siendo yo». |

### 2.4 Itsuki — Ciencias (jueves)

| Campo | Contenido |
|---|---|
| **Empezó** | Asiento y bento; «arrogante y carente de empatía»; «ni se te ocurra decirme la respuesta». |
| **La dejó el juego** | *Cálida:* «lo logré sola, del todo»; «puedes buscar tu cuaderno ahora». *Tibia:* «todavía no necesito tu ayuda». *Fría:* «ya tengo lo que necesitaba de ti»; rehízo el ejercicio «para que fuera mío». *No visitada:* «si hubieras venido, no te habría echado. No inmediatamente». **Beat azotea (siempre):** «ya no me queda ningún sitio que no lo sea». |
| **Cambio en E6** | De «pedir ayuda es darle la razón» a «preguntar no es perder». |
| **Recurso formal** | Oración cerrada (sujeto-verbo-punto). En la grieta se acorta y deja de cerrarse. |
| **Minijuego** | **It1 · Cadena de conversiones** con **«levantar la mano»**: le pregunta al *profesor*, no a MC. Respeta su regla («ni se te ocurra decirme la respuesta») y la rompe a la vez. |
| **Setups que cobra** | El error que arrastra el número del primer intento; «revisar desde el principio»; «el juego se acabó hoy»; Final B3.4 («apartó la mirada»). |
| **Disculpa** | **No se gasta.** En la escena final MC e Itsuki empiezan a hablar a la vez, se detienen («tú primero» / «no, tú») y Yotsuba los interrumpe. Queda pendiente. |
| **Tibia** | Revisa desde el principio **sola**, tarde; la frase queda cortada («Preguntar sería—»). |
| **Fría** | Resuelve sola, cierra el cuaderno con las dos manos; «no necesito preguntar». |
| **No visitada** | Se atasca, lo resuelve sola. MC le promete: «sube una vez sin el cuaderno». |

### 2.5 Miku — Sociales (viernes) · el clímax

| Campo | Contenido |
|---|---|
| **Empezó** | Sofá, libro de Sengoku, «es logística», se esconde detrás del libro; «quiere dividirnos»; «perdón». |
| **La dejó el juego** | *Cálida:* «lo vas a comprobar en tres semanas»; «dijiste que llegaste a la 92… lo de la sal está en la 120»; pidió que MC la avise al llegar. *Tibia:* «solo lo he leído… eso no es difícil», libro a media cara. *Fría:* «hoy no», se sube los audífonos y **suena la música**. *No visitada:* «hay una silla enfrente de la mía; siempre está vacía»; dejó el libro abierto dos días «por si hacía falta una excusa». |
| **Cambio en E6** | De «hablar cuesta» a «lo que amo cuenta». |
| **Recurso formal** | Puntos suspensivos iniciales que desaparecen cuando se suelta. **Su frase de cambio es la primera línea del juego de Miku sin «…» inicial y sin «perdón» detrás.** |
| **Minijuego** | **M3 · El compás.** Fase 1 con sus audífonos y su música; fase 2: *se los quita* y sigue el compás del **reloj del aula** (`amb_reloj`). La mecánica es la metáfora. |
| **Setups que cobra** | Sal / rutas de comercio (el examen los pregunta); «Y a mí eso me parece mucho más—» (se termina); **página 120**; goma; audífonos; «perdón» (los fallos del minijuego: «Perdón» → «Perd—» → «Otra vez»). |
| **Tibia** | Respuesta correcta, sin la historia de la sal; libro a media cara (frase cortada). |
| **Fría** | Respuesta correcta y segura; mano en los audífonos todo el examen; «hoy no». |
| **No visitada** | Escribe la historia de la sal *sin querer*, la borra, deja la respuesta seca. MC le pregunta por la silla vacía (promesa). |
| **Pregunta de examen** | Rutas de comercio / cómo se sostenía una provincia / por qué se unificó el país (las tres del hub). |

**Dato de orden:** Miku cierra la semana (viernes). La última imagen de los cinco bloques es la goma entera y los audífonos plegados sobre el pupitre: respuesta visual directa a `cg_miku_fracaso`.

---

## 3. Sistema de variantes (punto 7 del contexto)

### 3.1 Evaluación de tu hipótesis

> «En tibia/fría la chica piensa menos en MC y más en aprobar.»

| Aspecto | Evaluación |
|---|---|
| Dirección | **Correcta para tibia.** MC no la alcanzó; su atención se va a la tarea y a una duda. |
| Fría | **Incorrecta.** La fría piensa *mucho* en MC, pero como eco herido de lo que dijo («concéntrate en correr», «me lo resolviste», «hoy no»). «Menos MC» malgasta el material más dramático. |
| Productividad | «Pensar en aprobar» es genérico: no es lo que *esa* hermana quiere ni teme. Todos los monólogos se parecerían. |
| No visitada | La hipótesis no la distingue de la tibia. |
| Atribución | No resuelve que el jugador sienta que *él* lo logró en no-cálidas. |

**Reemplazo:** cada estado cambia el **foco** del monólogo (de qué trata), no solo cuánto piensa en MC.

### 3.2 Modelo recomendado: núcleo + capas

Nada de escenas paralelas completas. Cada bloque de hermana es **un núcleo fijo** más **capas intercambiables**:

| Capa | Qué es | Varía por | Líneas por variante |
|---|---|---|---|
| **N · Núcleo** | Narrador, día, CG de examen, observación de MC | nada | ~14 (fijo) |
| **M · Monólogo** | Voz interior de ella | `estado_h` (4) | ~10 |
| **J · Minijuego** | Encuadre, fallos con carácter, frase, salida | solo cálida | ~22 |
| **F · Frase** | Completa / cortada / cerrada / espera | `estado_h` (4) | 1–2 (dentro de M o J) |
| **G · Gesto** | Lo que MC *ve* de afuera al acabar | `estado_h` (4) | ~5 |
| **E · Eco final** | Su línea en la escena de las cinco | `estado_h` (4) | ~4 |
| **P · Promesa** | MC promete algo concreto | solo no visitada | ~3 |
| **B · Capa de beat** | Solo Nino (`nino_rama_beat`) e Itsuki (azotea) | 3 | ~2 |

Y el `estado_entrada` (3) toca **solo tres sitios** globales, no a las hermanas:

| Slot | Dónde | Variantes | Líneas |
|---|---|---|---|
| **S1** | Mov. 1 (lunes por la mañana) | 3 | ~8 |
| **S2** | Mov. 7 (Maruo y los boletines) | 3 | ~12 |
| **S3** | Mov. 10 (última línea del capítulo) | 3 | ~6 |

**Por qué no más:** si `estado_entrada` tocara también cada bloque, serían 3 × 4 × 5 = 60 monólogos. Así quedan **20** (4 × 5) y 9 piezas globales.

### 3.3 Modelo de focos (por estado)

| Estado | Foco del monólogo | MC aparece como… | Qué pasa con el miedo | Minijuego | Frase | Voz formal |
|---|---|---|---|---|---|---|
| **Cálida** | *Lo que cambió* porque alguien la vio. | Quien hizo X (**eco literal** de la decisión del jugador). | Se supera. | Sí | **Completa** | El tic *se suelta* (Yotsuba sin signos, Miku sin «…», Nino sin cortarse). |
| **Tibia** | La tarea y **una pregunta abierta**: «¿me ayudó o solo me dejó?». | Pregunta sin respuesta. | Se **nombra**, no se supera. | No | **Cortada** (la interrumpe su tic) → `pendiente` | El tic interrumpe la frase. |
| **Fría** | La herida convertida en **método**. | Eco de su frase fría. | Aprueba *con* la herida; el cambio es de cierre. | No | **Cerrada** (reafirma la defensa) → `cerrada` | El tic se endurece. |
| **No visitada** | **La espera** y el grupo; responde a su `queja_*`. | Quien **no vino**. | La grieta sigue; MC da una promesa. | No | **Desplazada** («sobre otra cosa») + promesa | Tic base. |

**Cómo siente el jugador que lo logró en las cuatro ramas.** Cada monólogo contiene un **eco de la decisión**: la frase que MC dijo (cálida/fría), el gesto que hizo (tibia) o la ausencia que dejó (no visitada). El jugador reconoce *su* elección. En la fría el coste es visible; en la no visitada, el hueco también. El aprobado es de ellas; el **cómo** es del jugador.

**Apoyo transversal:** la música lo dice sin texto (§4.4). Solo suena el tema de la hermana si fue cálida.

### 3.4 Qué cambia el `estado_entrada`

| Estado | Lo que cambia | Dónde |
|---|---|---|
| `superado` | La advertencia de Maruo está *viva*; MC lo siente. Maruo aparece con «No hizo falta que la repitiera». | S1, S2, S3 |
| `mixto` | Incertidumbre sin amenaza. Maruo es neutro y justo. | S1, S2, S3 |
| `bueno` | Las cinco llegan antes que MC; Maruo casi lo reconoce. Las puertas se abren casi a la vez. | S1, S2, S3, y color del CG final |

En el **CG de las cinco** el estado se resuelve con `matrixcolor` (como ya hacen los `bg_*_anochecer`), sin arte nuevo.

### 3.5 Sistema de notas (la «matriz diagonal»)

Cada hermana rinde las cinco materias (como en el Final B, todas hacen el mismo examen el mismo día).

- **Aprobado = 60** (supuesto, P-10).
- **Diagonal = 100** en su materia fuerte, en las cuatro ramas.
- **Fuera de la diagonal**, valores deterministas por estado de la hermana (no aleatorios):

| `estado_h` | Rango fuera de la diagonal |
|---|---|
| calida | 82–89 |
| tibia | 72–79 |
| no_visitada | 68–75 |
| fria | 60–66 (**raspando**) |

Ajuste por `estado_entrada`: `bueno` +3, `mixto` 0, `superado` −2 (recortado a 60–89).

Presentación recomendada: **pantalla `boletin_cinco`** (5 × 5), no un CG. Ventajas: refleja las variantes sin generar arte, la diagonal se ilumina y se funde en «**100 · 100 · 100 · 100 · 100**» (el *alumno que no existe*), y sirve de **pantalla persistente** en Cap. 2 y 3 (§6). **La matriz muestra solo notas académicas, nunca afinidad.**

### 3.6 Costos

**Líneas autoradas** (todas las variantes que hay que escribir):

| Pieza | Cálculo | Líneas |
|---|---|---|
| Mov. 1 núcleo + eco de confesiones (espejo de B2) | 45 + 20 | 65 |
| S1 | 3 × 8 | 24 |
| N (5 bloques) | 5 × 14 | 70 |
| M (monólogos) | 5 × 4 × 10 | 200 |
| J (minijuego, solo cálida) | 5 × 22 | 110 |
| G (gestos) | 5 × 4 × 5 | 100 |
| P (promesas) | 5 × 3 | 15 |
| B (capa de beat Nino/Itsuki) | 2 × 3 × 2 | 12 |
| S2 + núcleo Maruo | 14 + 3 × 12 | 50 |
| E · escena de las cinco | 24 núcleo + 5 × 4 × 4 | 104 |
| Boletín + chat + libreta | 22 + 3 × 6 | 40 |
| Coda en casa (si P-19) | 36 + 3 × 5 | 51 |
| **Total autorado** | | **≈ 840** |
| **Leídas por partida típica** | núcleo + 1 variante por capa + 1.5 minijuegos | **≈ 400** |

Referencia: un evento de hub ronda 250–300 líneas. E6 sería ~1,5 veces un hub, más 0–3 minijuegos de 2–4 minutos cada uno.

**CG** (todos estado-agnósticos salvo el opcional):

| Nivel | Contenido | Total |
|---|---|---|
| **A (mínimo)** | 5 × `cg_<h>_examen` (espejo de `*_fracaso`) + `cg_cinco_aprobadas` | **6** |
| **B (recomendado)** | A + `cg_miku_audifonos_mesa` (calida-only, la imagen firma) + 1 imagen del boletín/Maruo si el guion la pide | **8** |
| **C (máximo)** | B + 5 CG «interior» solo cálida (uno por hermana) | **13** |

Con A y B todos los CG salvo uno los ven **todos** los jugadores: la Galería sigue completable sin exigir una ruta cálida (P-21).

**Sprites candidatos** (solo si el guion los pide; regla de la guía: nunca antes del guion): `miku sonrie` (sonrisa mínima, libro abajo), `yotsuba serena`, `ichika sincera`, `nino suelta`, `itsuki serena`. La diferencia debe estar **en la silueta**, no en la cara.

**Minijuegos:** 5 escritos, **0–3 jugados** por partida.

### 3.7 Contrato técnico (para que guion, código y montaje no se pisen)

```
label evento_6:
    $ e6_iniciar()        # estado_entrada, e6_estado[h], nivel de minijuegos, notas
    call e6_lunes                      # Mov. 1  (S1)
    call e6_bloque("yotsuba")          # Mov. 2
    call e6_bloque("ichika")           # Mov. 3
    call e6_bloque("nino")             # Mov. 4
    call e6_bloque("itsuki")           # Mov. 5
    call e6_bloque("miku")             # Mov. 6
    call e6_resultados                 # Mov. 7  (S2)
    call e6_cinco                      # Mov. 8
    call e6_casa                       # Mov. 9  (si P-19)
    call e6_cuarto                     # Mov. 10 (S3)
    jump cap2_inicio                   # stub
```

Sub-labels por hermana *h* (nombres estables):
`e6_<h>_nucleo` · `e6_<h>_mono_<estado>` · `e6_<h>_mj` · `e6_<h>_gesto_<estado>` · `e6_<h>_eco_<estado>` · `e6_<h>_promesa`.

Variables nuevas: `e6_estado_entrada`, `e6_estado` (dict h → estado), `e6_frase` (h → tipo), `e6_promesas` (lista), `e6_notas` (matriz), `e6_mj` (h → intentos/resultado). Persistentes: `persistent.e6_mj_ganado_<h>` (permite *saltar* en repeticiones).

Voz interior: cinco `Character` nuevos (`yotsuba_int`…) con la caja de su color, **sin placa** (`who=None`) y estilo propio. Basta ampliar `ui_personaje` con `**kwargs` o crear `ui_interior()`. El historial los trata con `show_tipo="interior"`.

### 3.8 Invariantes y cómo verificarlos

| # | Invariante | Verificación |
|---|---|---|
| I1 | Todas aprueban | `min(e6_notas) ≥ 60` (assert) |
| I2 | 100 solo en la diagonal | ningún valor fuera de la diagonal = 100 |
| I3 | Minijuego solo si cálida | `e6_mj` solo contiene hermanas cálidas |
| I4 | Dificultad correcta | `mj_nivel() == "media"` ⇔ `nino_rama_beat == "calida"` |
| I5 | 0 ≤ minijuegos ≤ 3 | contador |
| I6 | Cada hermana tiene monólogo, frase, gesto y eco | tabla de cobertura |
| I7 | `despido_cap1 == False` en todo E6 | assert |
| I8 | No se escriben puntos salvo P-09 | diff de `puntos_*` |
| I9 | Sin texto duplicado de `beat_casa` | revisión |
| I10 | Flags de gancho escritos | `e6_frase`, `e6_promesas` |

---

## 4. Estructura del movimiento

### 4.1 Esquema (diez movimientos)

| Mov. | Escena | Lugar | Qué hace |
|---|---|---|---|
| **1** | Lunes antes del examen | `bg_escuela` → `bg_aula` | Espejo de B1/B2. «Hagan lo que **saben**». **S1.** |
| **2** | Yotsuba · Japonés | `bg_aula` | Bloque. Abre y fija las reglas. |
| **3** | Ichika · Matemáticas | `bg_aula` | Bloque. |
| **4** | Nino · Inglés | `bg_aula` | Bloque. Se queda en el aula en B; aquí es el cambio más visible. |
| **5** | Itsuki · Ciencias | `bg_aula` | Bloque. Pico de lucha. |
| **6** | Miku · Sociales | `bg_aula` | Bloque. **Clímax emocional.** Silencio y reloj. |
| **7** | Resultados y Maruo | `bg_departamento` | Cinco boletines en fila (espejo de B6). **S2.** |
| **8** | Las cinco | puertas → mesa | Las puertas **se abren**; escena final con las cinco aprobando. |
| **9** | Casa | `bg_comedor` | Curry (espejo de B8). «Gracias por la comida», esta vez sí. |
| **10** | Cuarto, chat y libreta | `bg_cuarto_mc` | Cinco fotos de boletines, cálculo del máximo, libreta. **S3.** |

### 4.2 Plantilla de un bloque (Mov. 2–6)

1. HUD: `ui_escena("beat", h, "Aula · <Materia>")` y `tiempo_restante = "N exámenes"`.
2. Narrador: el día y la materia (espejo de B: «las cinco lo hacían a la vez; yo solo podía mirar a una»).
3. **CG de examen** (POV de MC, espejo del `*_fracaso`).
4. MC: 2–3 líneas de lo que *ve* antes de saber.
5. **Voz interior** (cambia de caja y de color). Variante por `estado_h`.
6. **Si cálida:** minijuego → frase completa. **Si no:** frase cortada / cerrada / desplazada.
7. MC: gesto que ve de afuera (variante por estado). Timbre.

**Ironía dramática como motor.** MC ve el gesto; el jugador oyó la razón. Es el único lugar del juego donde el jugador sabe más que MC, y se limita a lo académico y emocional (nada de romance; P-11).

### 4.3 Ritmo y clímax

- **Orden L→V** igual que el Final B (Yotsuba, Ichika, Nino, Itsuki, Miku). Mantenerlo mejora el espejo.
- **Intensidad:** Yotsuba (ligera, fija reglas) → Ichika (media) → Nino (tensión) → Itsuki (lucha) → Miku (clímax y silencio).
- **Variedad entre bloques:** cambian la mecánica (timing → mantener → buscar → calcular → ritmo), el color de HUD y la música. Con ≤ 3 minijuegos por partida no hay fatiga de juego; el riesgo es fatiga de *estructura* (cinco veces la misma plantilla), por eso Mov. 2 y 6 rompen el patrón (ver §7).
- **Transición entre días:** `bg_negro` + `fade_dia` + timbre, de pocos segundos. Sin cinta nueva ni música de relleno.

### 4.4 Audio (todo reutilizado)

| Momento | Pista | Nota |
|---|---|---|
| Lunes | `sfx_timbre`, silencio | Como B1; luego `amb_reloj` bajo (0.4). |
| Examen, cálida | Monólogo con `descubrimiento`; minijuego con **el tema de la hermana** | `descubrimiento` suena solo mientras habla ella (regla de la guía). |
| Examen, no cálida | Solo `amb_reloj` y lápiz | **El tema solo suena si cálida:** el jugador *oye* a quién alcanzó. |
| Miku, fase 2 | Se corta la música; queda el reloj | La mecánica y el audio dicen lo mismo. |
| Maruo | `contrato` | `superado`: entra fuerte; `mixto`: bajo; `bueno`: se corta y entra `cotidiano`. |
| Las cinco | `cotidiano` | Espejo de `derrota` en B4. |
| Cuarto | `hogar` | Regla ya fijada: `hogar` suena siempre en `bg_cuarto_mc`. |

**Sin BGM nuevo.** Opcionales: dos SFX de minijuego (acierto/fallo) o reutilizar `sfx_hover`/`sfx_click` y `sfx_taza_mesa` (P-16).

### 4.5 Cierre del capítulo y huecos abiertos (a propósito)

La última imagen del capítulo no es un aplauso: es MC solo, con cinco hojas, calculando. Cierra el *tema* (un estudiante completo repartido en cinco) y **deja abierta la pregunta de Cap. 2**: ¿cómo consiguen que se vean entre ellas?

| Hueco | Dónde se planta | Para qué capítulo |
|---|---|---|
| Matriz diagonal: cada 100 es lo que a otra le falta | Mov. 10 | Cap. 2: enseñarse entre ellas. |
| Disculpa pendiente MC ↔ Itsuki (intento interrumpido) | Mov. 8 | Cap. 2–3. |
| Frases cortadas (`pendiente`) | Mov. 2–6 | Se *completan* en el evento de esa hermana en Cap. 2. |
| Promesas pendientes (2 por partida) | Mov. 2–6 | Cap. 2: primer destino de las no visitadas. |
| Tarjeta de receta de Nino | No se toca | Cap. 2. |
| Maruo: «los exámenes no terminan aquí» | Mov. 7 | Condición continúa. |
| Chat de grupo = primer espacio compartido | Mov. 10 | Cap. 2: las seis personas en un mismo sitio. |
| Estreno de la obra de Ichika, audición del prólogo | Mov. 3 | Cap. 2. |
| MC: «ya no solo por la deuda» | Mov. 9 | Desarrollo de MC. |

---

## 5. Minijuegos

### 5.1 Las 15 propuestas del anexo, evaluadas

Viabilidad = lo que cuesta hacerlo en Ren'Py 8.5.3. Encaje = cuánto expresa el arco de la hermana. Coste: S pequeño, M medio, L grande.

| ID | Idea | Viabilidad | Coste | Encaje | Veredicto |
|---|---|---|---|---|---|
| Y1 | Obstáculos en 3 carriles | Alta | S–M | **Bajo**: corre *sola*, justo lo que su arco desmonta | Descartado |
| **Y2** | Relevo de las cinco | Alta | S–M | **Alto**: tramos iguales («importas igual»), y *recibir* el testigo | **ELEGIDO** |
| Y3 | Carrera de kanji | Media | M–L | Bajo para un público hispanohablante; exclusión; exactitud | Descartado |
| **I1** | Audición: actuada vs sincera | Alta | M | **Alto** con la modificación de la máscara que se cansa | **ELEGIDO (modificado)** |
| I2 | Memoria tipo Simon | Alta | S | Medio-bajo | Plan B |
| I3 | Ecuaciones que revelan el guion | Alta | S–M | Medio: el acto de resolver no es el cambio | Plan B / modo extra |
| **N1** | Compras para las cinco | Alta | M | **Alto** (inglés + cuidar a las demás + sexto hueco) | **ELEGIDO (modificado)** |
| N2 | Cocina contrarreloj | Media | M | Medio; **adelanta** la tarjeta de receta (se queda para Cap. 2) | Descartado por ahora |
| N3 | Memoria de gustos | Alta | S | Medio | Plan B |
| **It1** | Conversiones + pedir ayuda | Alta | S–M | **Alto**: el error repetido es su grieta | **ELEGIDO** |
| It2 | Bento balanceado | Media | S–M | Medio; datos de nutrición a afinar | Plan B |
| It3 | Laboratorio | Media | M | Bajo-medio | Descartado |
| M1 | Duelo Sengoku (QTE) | Alta (técnica) | **L** (enemigos) | **Contradictorio**: «las batallas las gana quien mueve el arroz, no la espada» | Descartado |
| M2 | Estrategia Sekigahara | Media | M–L (mapa nuevo) | Alto para el contenido; no expresa *miedo a hablar* | Se usa como **pregunta de examen**, no como minijuego |
| **M3** | Ritmo con audífonos | Media-Alta | M | **Muy alto**: la mecánica es la metáfora | **ELEGIDO (con fase 2 del reloj)** |

**Criterio de selección:** que *la mecánica sea la metáfora* (el jugador hace el gesto que la hermana necesita hacer) y que ninguna exija saber inglés, japonés o historia real.

### 5.2 Los cinco minijuegos elegidos

| Hermana | Minijuego | Familia mecánica | Entrada | La metáfora |
|---|---|---|---|---|
| Yotsuba | **Y2 · Relevo** | Timing de un solo botón | Espacio / clic | Cinco tramos *iguales*; hay que **esperar a recibir**, no correr por delante. |
| Ichika | **I1′ · La máscara se cansa** | Gestión de recurso con *tocar* vs *mantener* | Clic / mantener | Actuar es rápido y agota; ser sincera cuesta un segundo y descansa. |
| Nino | **N1′ · Compras para seis** | Búsqueda y selección bajo tiempo | Clic | Compra las listas de las cinco y *decide* qué hacer con el sexto hueco: esperar sin adelantar el golpe. |
| Itsuki | **It1 · Conversiones** | Cálculo secuencial con trampa | Clic / teclado | El número arrastrado reaparece; **levantar la mano** revela dónde mirar. |
| Miku | **M3 · El compás** | Ritmo en carriles | 3 teclas / clic | Fase 1 con audífonos; fase 2 sin ellos, al compás del reloj del aula. |

Cinco familias distintas, una sola base técnica (§5.3).

**Detalles de diseño clave:**

- **Y2.** Cinco hermanas corren en carriles iguales. Salir demasiado pronto («salida en falso») y salir tarde (testigo al suelo) fallan igual. El número perfecto: la pista tiene **28** marcas.
- **I1′.** Doce líneas de un guion corto. Cada una ofrece *Actuada* (toque, ya) o *Sincera* (mantener 0,75 s). Barra de *máscara*: sube con cada actuada; si llega a 100 % se queda en blanco. La última línea del guion es la frase de cambio y **solo se puede decir sincera**.
- **N1′.** Cinco listas en inglés con su **traducción que aparece sola** a los 1,4 s (traduce sin darse cuenta). Etiquetas casi iguales (harina normal / con leudante, sugar / confectioners' sugar). Sin ilustraciones de producto: cajas con texto, generadas por script como el resto de la UI. El sexto hueco es una elección sin respuesta «correcta».
- **It1.** Cadena de 5 conversiones. El número equivocado del primer intento aparece como *fantasma gris* en el margen y vuelve a colarse en el paso 2. Botón **«Levantar la mano»**: consume tiempo, revela el paso equivocado (**no** da la respuesta, igual que «solo te digo dónde mirar»). Si lo usa, frase A; si resuelve «desde el principio» sola, frase B (cerrada, con «la próxima vez preguntaré»). Cuesta dos líneas más y respeta al jugador.
- **M3.** Fase 1: 3 carriles con barras de ecualizador (su motivo) al compás de `miku_tema`. Fase 2: la música se corta; sigue el tic del reloj (`amb_reloj`). Cuando acaba, se quita los audífonos y los deja sobre el pupitre.

### 5.3 Base técnica compartida

Todo con lenguaje de pantallas de Ren'Py, sin librerías externas.

| Pieza | Descripción |
|---|---|
| `mj_nivel()` | Devuelve `"media"` si `nino_rama_beat == "calida"`; si no, `"dificil"`. |
| Tabla de parámetros | `MJ_PARAMS[juego][nivel]` (§5.4). |
| `screen mj_marco(...)` | HUD común: barra de tiempo, intentos, motivo y color de la hermana (`PETALO_COLOR`, `hud_icono_<h>`). Oculta menú rápido y franjas (`quick_menu = False`). |
| `label mj_ejecutar(juego, hermana)` | Bucle de intentos: lanza la pantalla, recibe `ganado` / `perdido` / `saltado`, aplica asistencia y líneas de fallo. |
| Líneas de fallo | Diccionario por hermana y por número de intento (§5.5). |
| Aleatoriedad | `renpy.random` (compatible con rollback y guardado). |
| Persistencia | `persistent.e6_mj_ganado_<h>` habilita «saltar» en repeticiones. |
| Entradas | Ratón + espacio/flechas. Todo se puede jugar con **una mano y un botón** (P-20). |
| Estética | Piezas en estilo del juego (PNG de `generar_ui.py`, cintas, motivos). Sin arte nuevo. |

### 5.4 Dificultad (valores de partida; se calibran jugando)

**Y2 · Relevo**

| Parámetro | Difícil | Media | Asistida |
|---|---|---|---|
| Ventana de traspaso | ±0,12 s | ±0,26 s | ±0,40 s |
| Velocidad del marcador | 1,00 | 0,75 | 0,60 |
| Testigos que se pueden caer | 1 | 3 | 5 |
| Salida en falso | penaliza | avisa | ignora |
| Punto de control | tramo 3 | cada tramo | cada tramo |

**I1′ · La máscara se cansa**

| Parámetro | Difícil | Media | Asistida |
|---|---|---|---|
| Líneas | 12 | 10 | 8 |
| Máscara por línea actuada | +16 % | +10 % | +6 % |
| Máscara por línea sincera | −24 % | −30 % | −40 % |
| Mantener para ser sincera | 0,75 s | 0,50 s | 0,35 s |
| Tiempo por línea | 2,4 s | 3,4 s | 4,5 s |
| Punto de control | línea 6 | cada 4 | cada 3 |

**N1′ · Compras para seis**

| Parámetro | Difícil | Media | Asistida |
|---|---|---|---|
| Tiempo total | 75 s | 105 s | 140 s |
| Traducción aparece a | 1,4 s | 0,5 s | inmediata |
| Distractores casi iguales por estante | 3 | 2 | 1 |
| Penalización por error | −6 s | −3 s | −1 s |
| Punto de control | tras 3 listas | tras cada lista | tras cada lista |

**It1 · Conversiones**

| Parámetro | Difícil | Media | Asistida |
|---|---|---|---|
| Pasos | 5 | 4 | 3 |
| Tiempo | 55 s | 80 s | 110 s |
| Números trampa | 2 | 1 | 1 (marcado) |
| Intentos | 3 | 5 | ∞ |
| «Levantar la mano» | 1 vez, −10 s | 2 veces, −5 s | ilimitada, gratis |
| Indicador de plausibilidad | no | sí | sí |

**M3 · El compás**

| Parámetro | Difícil | Media | Asistida |
|---|---|---|---|
| Fase 1 | 48 notas | 36 | 28 |
| Ventana de acierto | ±80 ms | ±140 ms | ±200 ms |
| Fallos permitidos | 8 | 14 | 24 |
| Fase 2 (reloj) | 24 notas, sin guía | 16, guía tenue | 12, guía clara |
| Punto de control | inicio de fase 2 | cada 16 notas | cada 12 |

**Objetivos de calibración (para los playtests):** en *difícil*, 55–65 % de victorias al primer intento para un jugador medio; en *media*, 80–90 %. Máximo esperado: 2 intentos.

### 5.5 Frustración de «repetir hasta ganar» y qué recomiendo

**Riesgo:** una novela visual no suele atraer a jugadores de reflejos. Fallar ocho veces el ritmo de Miku *en el clímax del capítulo* destruye la escena.

**Recomendación (combinada, decisión tuya, P-07 y P-08):**

1. **Puntos de control por fase.** Fallar no reinicia todo.
2. **Fallar es carácter, no castigo.** Cada fallo muestra una línea de ella que cambia por intento:
   - Miku: «…Perdón.» → «…Perd—» → «…Otra vez.» (el jugador la va enseñando a no disculparse).
   - Yotsuba: «¡Otra vez!» → «¡Otra vez! ¡Esta sí!» → «…Otra vez. Despacio.»
   - Nino: «Tsk.» → «…Otra vez. No mires.» → «Otra vez.»
   - Itsuki: «Revisaré desde el principio.» (las tres veces; la tercera sin enojo).
   - Ichika: la sonrisa tarda más en volver en cada intento.
3. **Asistencia adaptativa.** Tras 2 fallos, un paso a medio camino hacia el siguiente nivel; tras 4, el paso completo; tras 6, ofrece **«Que lo haga ella»** (salto narrativo, sin penalización de historia).
4. **El boost de Nino se conserva** también bajo asistencia: sin boost, el suelo de la asistencia es *media*; con boost, el suelo es *asistida*. El jugador que fue cálido con Nino **siempre** lo nota.
5. **Saltar tras ganar una vez** (persistent), para repeticiones o rollback.
6. **Opción «Asistencia» en Opciones** para quien prefiera no jugarlos (no cambia el guion).

**Alternativa más pura** (si quieres respetar al pie de la letra «repetir hasta ganar»): solo los puntos 1 y 2. Es viable, pero la tasa de abandono en *difícil* será mayor. **Lo que no recomiendo** es *difícil* sin red.

### 5.6 Riesgos técnicos en Ren'Py (a verificar en una prueba de humo)

| Riesgo | Mitigación |
|---|---|
| **Rollback y saves** a mitad de minijuego | Estado solo en variables de pantalla; al cargar, el intento reinicia. Desactivar rollback durante la pantalla (`_rollback`/`config.rollback_enabled`: **verificar nombre exacto en 8.5.3**). |
| **Skip / Auto** | Anular skip dentro del minijuego (`_skipping`, **verificar**). Un skip jamás debe dar el minijuego por ganado. |
| **Pausa con Esc** | Comprobar que el menú detiene timers y ATL; si no, usar un reloj propio que se congele. |
| **Sincronía de audio (M3)** | `renpy.music.get_pos()` es poco fiable (puede dar `None`); usar reloj propio desde el inicio de la pista, ventanas generosas, calibración de latencia. **Plan B:** metrónomo (clic) en lugar del tema. |
| **Rendimiento** | El proyecto ya usa mucho `matrixcolor`. En minijuegos, imágenes pre-teñidas y pocos displayables. Probar en el equipo más lento. |
| **Aleatoriedad** | Solo `renpy.random`. |
| **HUD / overlays** | `quick_menu = False` durante el minijuego y restaurar al salir; `ui_escena` coherente. |
| **Dispositivos táctiles** | Fuera de alcance (P-20): el juego es PC-first. |

---

## 6. Innovación y qué NO hacer

### 6.1 Ideas con apuesta (realistas en Ren'Py)

| # | Idea | Por qué es poco habitual | Coste | Riesgo | Recomendación |
|---|---|---|---|---|---|
| 1 | **E6 como negativo del Final B** (Anexo A) | Un buen final «malo» sirve de plano de un final bueno | ~0 | Ninguno | **Sí** |
| 2 | **Boletín como matriz 5×5 persistente** | El *boletín* es la tesis (alumno completo) y a la vez un **tracker** de Cap. 2–3 y del Final Secreto | M | Que parezca «puntos visibles» | **Sí** (solo notas académicas) |
| 3 | **La música como marcador de relación** | Su tema suena solo si fue cálida; el jugador *oye* a quién llegó | ~0 | Ninguno | **Sí** |
| 4 | **Fallar como carácter** | El fallo es contenido, no Game Over | S | Textos repetidos | **Sí** |
| 5 | **Frase cortada que se completa en Cap. 2** | Payoff diferido de una frase del Cap. 1 | S | Hay que recordarlo | **Sí** (flags `e6_frase`) |
| 6 | **Promesas pendientes** para las no visitadas | Hace que quedar fuera pese, sin castigar | S | Obligación para Cap. 2 | **Sí** |
| 7 | **Primera frase de Miku sin «…»** | El tic formal *es* el desarrollo | 0 | Ninguno | **Sí** |
| 8 | **Chat de grupo como pantalla de revelación** | Un objeto ya canónico como mecánica | M | Más pantallas | Opcional (P-18) |
| 9 | **Capa por `persistent` para quien vio el Final B** | Memoria de otra línea sin romper la cuarta pared | S | Spoiler si se abusa | Opcional (P-17) |
| 10 | **Díptico «antes/después» en la Galería** | Compara `*_fracaso` y `*_examen` | S | Cambia el conteo | Opcional (P-21) |
| 11 | **«El mapa final»:** reutilizar `mapa_hub` como resumen (cinco bandas) | Un UI querido como informe del capítulo | M | Revela cálida/fría (ya hay pistas de color) | Opcional |
| 12 | **La voz interior solo aquí** | Primera vez que se oye a las hermanas por dentro | S | Rompe el punto de vista de MC | **Sí, acotado** (P-11) |

### 6.2 Qué NO conviene hacer aquí

| # | No hacer | Por qué |
|---|---|---|
| 1 | Que el minijuego decida la nota o el aprobado | Rompe «todas aprueban» y castiga a los menos hábiles. |
| 2 | Mostrar números de afinidad | El sistema es invisible; la matriz solo muestra notas. |
| 3 | Gastar la disculpa de Itsuki | Es la carta más fuerte que queda; B ya la gasta en su línea. |
| 4 | Resolver la confianza de Nino o la tarjeta de receta | Ambos son motor del Cap. 2. |
| 5 | Kanji (Y3) | Excluye al lector, riesgo de exactitud. |
| 6 | Duelos Sengoku (M1) | Contradice la tesis «las batallas las gana quien mueve el arroz». |
| 7 | Minijuego en el examen real | Se confunde con calificar; el minijuego es *interior*. |
| 8 | Game Over / final malo por perder un minijuego | El jugador decide qué hacer con el fracaso, no el motor. |
| 9 | Veinte escenas paralelas | Costo de ~3× por una diferencia mínima. |
| 10 | Usar la voz interior para romance o celos | Rompe el cálculo secreto y el misterio de las rutas. |
| 11 | Maruo cálido | Su calidez sería cobrada en capítulos siguientes. |
| 12 | BGM nuevo por inercia | La regla de la guía: una pista solo significa algo si antes hubo silencio. |
| 13 | Generar CG de variantes (calida) antes de cerrar el guion | Regla del proyecto: arte solo contra guion escrito. |
| 14 | Repetir los pensamientos de MC de `beat_casa` | Ya los leyó el jugador (código obliga a las cinco). |
| 15 | Que el «100» se lea como «valor moral» | Es su materia, no su valía. |

---

## 7. Boceto ilustrativo del guion

> **No es guion final.** Son líneas de muestra para fijar tono y mecánica. Marcadores como en los hubs: `[BG]` `[CG]` `[SPR]` `[MUS]` `[SFX]` `[$]`, `[NUEVO]` para assets inexistentes.

### Mov. 1 · Lunes antes del examen

`[BG bg_escuela]` `[SFX sfx_timbre volume 1.5]` `[$ ui_escena("beat", None, "Semana de exámenes")]`

**mc_pensamiento:** Lunes. Primer día de exámenes. Uno por día, toda la semana.
**mc_pensamiento:** Hace treinta días llegaba a este instituto con una palabra clavada: despedido.
**mc_pensamiento:** Hoy llego con cinco nombres.

*S1 (según `estado_entrada`):*
- **superado:** «Maruo no volvió a repetir la advertencia. Hoy no la necesita: se cumple o no se cumple.»
- **mixto:** «No sé si fue suficiente. Hoy lo voy a saber, uno por uno.»
- **bueno:** «Por primera vez no tengo que contar cabezas al entrar. Ya sé cuántas son.»

`[BG bg_aula]` `[SPR … at pj(X_*)]`
**narrador:** Las cinco ya estaban en el aula. Ninguna tenía el libro abierto. Esta vez no hacía falta.

*Espejo de las confesiones de B2 (una línea por hermana, variante «alcanzada» o «no alcanzada»):*
**ichika:** Dormí siete horas. Siete y cuarto. Redondeo hacia arriba.
**miku:** …Me sé la mitad de lo que van a preguntar. …Y la otra mitad también.
**itsuki:** He estudiado más que nadie en esta aula. Cada noche. Y lo sé. Eso es nuevo.
**nino:** Alguien tiene que decirlo y me toca a mí. Treinta días. El último duró cuatro.
**mc:** Lo sé.
**nino:** …No es un cumplido.

**mc:** Hagan lo que saben.
**narrador:** Lo dije y esta vez no sonó a relleno. Sonó a una lista con cinco nombres detrás.
**profe:** Pueden empezar.
`[SFX sfx_hoja volume 2.0]` `[AMB amb_reloj fadein 2.0 volume 0.4]`

### Mov. 2 · Yotsuba · Lunes · Japonés (variante *cálida*)

`[$ ui_escena("beat", "yotsuba", "Aula · Japonés")]` `[CG NUEVO — cg_yotsuba_examen]`
**narrador:** Lunes. Japonés. Las cinco lo hacían a la vez; yo solo podía mirar a una.
**mc_pensamiento:** Tenía el lápiz en movimiento. Y la cabeza quieta.
**mc_pensamiento:** Es la primera vez que no la veo mirar a las demás.

`[MUS descubrimiento]` *(voz interior, caja verde)*
**yotsuba (interior):** Pregunta uno. ¿Qué siente el protagonista cuando se queda solo?
**yotsuba (interior):** Lo sé. Lo sé porque conté veintitrés vueltas sola y a la veintitrés alguien me estaba mirando.
**yotsuba (interior):** Me dijo que no leo libros. Que leo personas.
**yotsuba (interior):** Cinco personas a la vez, dijo.
**yotsuba (interior):** Si eso cuenta… ¿cuenta cuando nadie me lo pide?

`[MJ y2]` `[MUS yotsuba]` *Fallos:* «¡Otra vez!» → «¡Otra vez! ¡Esta sí!» → «…Otra vez. Despacio.»
*Tras ganar (sin signos de exclamación):*
**yotsuba (interior):** Cada tramo mide lo mismo. Ninguna carrera la gana una sola.
**yotsuba (interior):** Yo importo igual que mis hermanas.
**yotsuba (interior):** ¡…Pregunta uno! Escribo que el protagonista quería que alguien llegara.
**mc_pensamiento:** Escribió sin levantar la vista. Una sola vez miró a Itsuki, y no fue por miedo: fue para saludarla.
**mc_pensamiento:** No dejó la hoja en blanco. No dejó de mirar a las demás. Aprendió a hacer las dos cosas.

*Contraste (mismas posiciones, otros estados):*
- **Tibia:** «Un minuto con catorce. No sé qué me dijo ese cronómetro. Si termino rápido, ¿alguien me va a necesitar para…? *Yo también im—* ¡Pregunta dos!»
- **Fría:** «Correr. Concentrarme en correr. Escribo lo justo. Ni una línea de más. …Contar en voz alta ya no hace falta.»
- **No visitada:** «Tres vueltas de ventaja. Las conté por si venía. …Si nadie me necesita, ¿para qué me sobra tanta energía? …Entonces la reparto.» + MC: «Quiero ver esas veinticinco vueltas. Cuando esto termine.»

### Mov. 5 · Itsuki · Jueves · Ciencias (variante *cálida*)

`[$ ui_escena("beat", "itsuki", "Aula · Ciencias")]` `[CG NUEVO — cg_itsuki_examen]`
**itsuki (interior):** Cuarta pregunta. Conversión de unidades. Tercer paso.
**itsuki (interior):** Copié el número del primer intento. Otra vez.
**itsuki (interior):** Tres veces. La misma cifra. El mismo sitio.
**itsuki (interior):** Podría revisar desde el principio. Es lo correcto. Pero llevo tres.
**itsuki (interior):** No.
**itsuki (interior):** Dijo: «solo te digo dónde mirar».
**itsuki (interior):** Eso no era darle la razón.

`[MJ it1]` botón **Levantar la mano** → *Frase A:* «Preguntar no es perder.»
**narrador:** Levantó la mano. Despacio. El profesor se acercó y ella dijo algo tan bajo que no lo oí.
**mc_pensamiento:** No me miró a mí. Le preguntó a quien debía. Eso es mucho más.
*(Espejo de B3.4: «Levantó la vista. Me miró un segundo… Apartó la mirada».)*

### Mov. 6 · Miku · Viernes · Sociales (variante *cálida*) — clímax

`[MUS stop]` `[AMB amb_reloj]` `[CG NUEVO — cg_miku_examen]`
**narrador:** Viernes. Sociales. El último.
**mc_pensamiento:** La goma estaba entera. Intacta, junto al lápiz.

*(voz interior, caja azul; esta vez el «…» inicial es parte del tic y desaparecerá)*
**miku (interior):** …Pregunta tres. Rutas de comercio.
**miku (interior):** …Sal.
**miku (interior):** …Alguien se la vendió.

`[MJ m3]` Fase 1 con su tema → los audífonos se apagan → **fase 2: solo el reloj.**
*Fallos:* «…Perdón.» → «…Perd—» → «…Otra vez.»
*Tras ganar:*
**miku (interior):** Y a mí eso me parece mucho más importante que quién ganó.
**miku (interior):** Dejaré de tener miedo a lo que más amo.
*(Primera línea de Miku sin «…» inicial ni «perdón» detrás.)*
**narrador:** Se quitó los audífonos y los dejó sobre el pupitre, plegados, como quien deja las llaves en la entrada.

*Contraste:*
- **Tibia:** «…Lo que amo no—» (se sube el libro a media cara).
- **Fría:** respuesta correcta y segura, mano en los audífonos todo el examen: «…Hoy no.»
- **No visitada:** escribe la historia de la sal sin querer, la borra, deja la respuesta seca. MC (promesa): «Hay una silla enfrente de la tuya. ¿Sigue vacía?»

### Mov. 7 · Maruo y los boletines (S2)

`[BG bg_departamento]` `[CG cg_maruo_reunion]` `[MUS contrato]`
**narrador:** Dejó cinco boletines sobre la mesa. Boca arriba, en fila.
**maruo:** Cinco.
- **superado:** «Te dije que no repetiría la advertencia. No hizo falta. …La condición se cumplió. Eso es todo.»
- **mixto:** «Cinco aprobadas. Con márgenes que no me gustan. Pero cinco. El contrato sigue.»
- **bueno:** «Tu padre me habló de alguien que no se rendía. No te rendiste. Y esta vez tampoco te quedaste quieto.»
**narrador:** No sonrió. Maruo no sonríe. Pero alineó los boletines con un dedo, como se alinea algo que importa.
**maruo:** Los exámenes no terminan aquí.

### Mov. 8 · Las cinco (puertas → mesa)

`[SFX sfx_puerta_abre]` Se abren las puertas (en B se *cerraban*). **Las dos no visitadas abren las últimas.**
`[MUS cotidiano]` `[CG NUEVO — cg_cinco_aprobadas]` *(frontal, cinco en fila, misma mesa que `cg_hermanas_estudiando` y `cg_cinco_estudiando`)*
**yotsuba (cálida):** ¡Cien! ¡Cien en japonés! …¿Me dejas la muñeca?
**mc:** Ya no queda sitio.
**yotsuba:** ¡Pues escribo encima!
**nino (cálida):** Que quede claro: no confío en ti. …Todavía.
**miku (cálida):** …La página ciento veinte. ¿Llegaste?
**mc:** Ciento veintidós.
**narrador:** Se rió. Una sola nota, corta, como un acorde. Quería ver mi cara.
**itsuki / mc:** (a la vez) El otro día… / Yo quería… — **yotsuba:** ¡Ah! ¿Quién va a querer curry? *(la disculpa queda pendiente)*

### Mov. 9 · Casa (espejo de B8)

**raiha:** ¡Hermanito! ¡Hice curry!
**mc:** Cinco.
**raiha:** …Te dije que podías con cinco a la vez.
**raiha:** Entonces no había problema.
**isanari:** Cobramos entero.
**mc_pensamiento:** No pensé en el dinero. Me di cuenta después.
**mc:** Gracias por la comida.
**mc_pensamiento:** Esta vez lo sentí.

### Mov. 10 · Cuarto, chat y libreta (S3)

`[BG bg_cuarto_mc]` `[MUS hogar]` `[SFX sfx_celular]`
**narrador:** Yotsuba mandó cinco fotos al chat «¡Equipo Quintillizas + Tutor!». Nino no se había salido.
**mc_pensamiento:** Cinco hojas. Cinco aprobadas. Hago lo que hago siempre: calcular.
**mc_pensamiento:** La nota más alta de cada una. Japonés, cien. Matemáticas, cien. Inglés, cien. Ciencias, cien. Sociales, cien.
**mc_pensamiento:** Un boletín perfecto. De un alumno que no existe.
**mc_pensamiento:** Cinco personas que saben, cada una, lo que a las otras cuatro les falta. Y que en todo el mes no se dijeron una palabra sobre eso.
**mc_pensamiento:** No controlé las notas. Lo único que controlé fue a dónde fui.
`[CG cg_libreta]` Escribe una frase nueva bajo la anterior: *«Ahora, juntas.»*
*Última línea (S3):*
- **superado:** «Maruo dijo cinco. No dijo hasta cuándo.»
- **mixto:** «No sé si lo logré yo o lo lograron ellas. Esa diferencia es la que no sé escribir.»
- **bueno:** «Les enseñé dónde mirar. Falta que se miren entre ellas.»

---

## 8. Riesgos y preguntas

### 8.1 Dónde discrepo de ti (con argumentos)

1. **«Menos MC, más aprobar» en tibia/fría** → reemplazado por focos (§3.1).
2. **«El beat de Nino ocurre antes de su hub»** → no necesariamente (F-05); no cambia nada técnico.
3. **Los CG 3.1–3.5 «podrían ser un examen anterior»** → no: son el Final B (F-09). Aun así conviene espejarlos.
4. **«Difícil base, repetir hasta ganar»** → viable pero arriesgado; recomiendo red (§5.5).
5. **«Futaro no está ahí» (`CAP1.md` §4)** → `CAP1_FINAL_MALO.md` ya cambió a MC presente. Conviene MC presente (P-03).
6. **Cinco CG «interior» (nivel C)** → alto costo para 0–3 apariciones; recomiendo A o B.
7. **Puntos:** el techo de 9 contradice el umbral de 10 (§1.9).

### 8.2 Riesgos

| # | Riesgo | Prob. | Impacto | Mitigación |
|---|---|---|---|---|
| R1 | Variantes fuera de control | Media | Alto | Modelo de capas y contrato de labels. |
| R2 | La voz interior rompe el punto de vista y filtra romance | Media | Alto | Solo lo académico/emocional; P-11. |
| R3 | M3: sincronía de audio y latencia | Alta | Medio | Reloj propio, ventanas amplias, metrónomo como plan B. |
| R4 | Frustración en *difícil* | Alta | Alto | §5.5. |
| R5 | Rollback, skip y guardado dentro de minijuegos | Media | Alto | Prueba de humo en el chat de cimientos. |
| R6 | Fatiga por la misma plantilla ×5 | Media | Medio | Romper el patrón en Mov. 2 y 6; música y mecánica distintas. |
| R7 | Duplicar texto de `beat_casa` | Media | Medio | Regla I9. |
| R8 | Consistencia del CG de grupo de cinco | Media | Alto | Misma semilla que `cg_cinco_estudiando`; edición con Gemini ≤ 3 pasadas. |
| R9 | Economía de puntos | Alta | Alto | P-09 antes del primer chat. |
| R10 | Documentación desactualizada (`README`, `CAP1.md`) | Alta | Bajo | Actualizar en bloque al final (lo pediste). |
| R11 | Galería: conteo y CG bloqueados | Media | Bajo | Preferir CG estado-agnósticos (nivel A/B). |
| R12 | Rendimiento (`matrixcolor`, pantallas) | Media | Medio | Imágenes pre-teñidas; pruebas en el equipo más lento. |

### 8.3 Decisiones que necesito de ti (`P-xx`)

Columna «Bloquea»: el primer chat que no puede empezar sin esa respuesta (numeración del plan). **Mi recomendación** va por defecto: si respondes «ok todo», se toma tal cual.

| ID | Decisión | Mi recomendación | Bloquea | Mi Respuesta |
|---|---|---|---|---|
| **P-01** | Los **cinco** tienen bloque completo (nombre, CG, monólogo); el minijuego solo en cálida. | Sí | 1, 2, 3, 4 | Si, de acuerdo |
| **P-02** | Modelo **núcleo + capas** y **focos por estado** en lugar de «menos MC». | Sí | 1, 2, 3, 4 | Si, de acuerdo |
| **P-03** | Examen **en el aula con MC presente** (espejo del Final B). | Sí | 2, 3, 4, 7 | Si, de acuerdo |
| **P-04** | Estructura: L→V (Y, I, N, It, M) → Maruo → las cinco → casa → cuarto; última línea sin resolver. | Sí | 2 | Si, de acuerdo |
| **P-05** | Frases de cambio (§2) y sus variantes cortada / cerrada / espera. | Sí, con ajustes tuyos | 3, 4 | Si, de acuerdo |
| **P-06** | Minijuegos: Y2, I1′, N1′, It1, M3. | Sí | 1, 5, 6 | Si, de acuerdo, aunque quiero saber si hay como adaptarlos a moviles |
| **P-07** | Política de fallo: puntos de control + líneas de fallo con carácter + asistencia adaptativa + saltar tras 6 o tras ganar una vez. | Sí | 1, 5, 6 | Si, de acuerdo |
| **P-08** | Dificultad: tablas de §5.4; boost por `nino_rama_beat`; boost se conserva bajo asistencia. | Sí | 1, 5, 6 | Si, de acuerdo |
| **P-09** | Puntos en E6: **+1 por minijuego ganado en cálida** (vía `sumar_punto`) o 0. | +1 | 1 | No, los puntos son solo en los hubs y solo ahí |
| **P-10** | Notas: aprobado = 60, diagonal 100, rangos de §3.5, boletín como **pantalla**. | Sí | 1, 2 | Si, de acuerdo |
| **P-11** | Voz interior con cajas propias (`<h>_int`), solo lo académico/emocional, sin romance. | Sí | 1, 3, 4 | Si, de acuerdo |
| **P-12** | No visitadas: monólogo con callback a su queja + **promesa pendiente** (flag). | Sí | 3, 4 | Si, de acuerdo |
| **P-13** | Disculpa de Itsuki: **no se gasta**; solo intento interrumpido. | Sí | 4 | Si, de acuerdo |
| **P-14** | Nino puede llegar a «no confío… todavía»; nunca a «confío». | Sí | 4 | Creo que ya debería confiar pero no admitirlo directamente, es decir duró mas que otro tutor y no hizo promesas vacias |
| **P-15** | Nivel de CG (A / B / C) y estado-agnósticos; ¿guardaste las semillas de los `*_fracaso` y de `cg_cinco_estudiando`? | B | 7 | Si, las guardé |
| **P-16** | Audio: sin BGM nuevo; su tema solo suena si cálida; reloj en el resto; SFX de acierto/fallo opcionales. | Sí | 3, 4, 6, 8 | Si, de acuerdo en todo |
| **P-17** | Capa opcional por `persistent` para quien vio el Final B. | No por ahora | 2 | Si, de acuerdo, de paso esos cg de fracaso ya no sean obligatorios que esten en la seccion de cada hermana, pero tocaria rediseñar el menu de galeria para que haya mas espacio o hacer mini menus. |
| **P-18** | Chat de grupo como pantalla de revelación. | Sí | 2, 8 | Si, de acuerdo es muy innovador |
| **P-19** | Coda en casa (curry) en E6. | Sí | 2 | Si, de acuerdo |
| **P-20** | Solo PC; minijuegos con un botón o ratón. | Sí | 1, 5, 6 | No estoy de acuerdo, es que tambien hay jugadores de movil, por eso pregunto si esos minigames se pueden adaptar a moviles o mejor en las versiones de movil poner que esos videojuesgos son exclusivos de pc para ahorrarnos adaptarlos. |
| **P-21** | Galería: añadir los CG de E6; díptico opcional. | Sí | 1, 7 | Si, de acuerdo |
| **P-22** | Ganchos para Cap. 2: `e6_frase`, `e6_promesas`, matriz persistente. | Sí | 1, 2 | Si, pero el cap2 no debe centrarse del todo en eso |
| **P-23** | Sprites nuevos (candidatos): decidir tras el guion. | Diferir | 7 | Si, si el guion lo necesita, ademas serian utiles para el cap2 donde habrian nuevas facetas de las hermanas |

Otra decision adicional es el del nuevo cg de miku_audifonos_mesa, no conviene en si, no digo que es mala idea pero tocaria que cada hermana tambien tuviera un
cg nuevo o que ichika y yotsuba tambien tengan un cg nuevo para que ellas 3 esten iguales, nino e itsuki se pordrian omitir porque son las que mas cgs tienen, no digo que es mala idea, pero por reparticion y equidad discrepo un poco.

Otra decision adicional tambien es respecto a la suma de puntos que estás confundido, bien, se quedan sollo en los hubs los puntos, y al final son 9 no? tu te preguntas y como llegamos a los 10, y ahi entra la decision final del jugador, digamos que el jugador en los 3 capitulos escogió calida en todos los hubs en las mismas 3 hermanas, ejemplo miku, nino e itsuki, las 3 tienen 9 puntos no? bueno en el final el jugador decidira a quien declarará su amor, a quien elija le suma 1 punto con lo cual esa chica llegará a 10 puntos y se desbloqueará su final, este punto final es decision del jugador, ahora hay caso hipotetico de que solo una chica llegó a 9 puntos y nadie mas, entonces por defecto ella será la elegída y la que obtendrá el punto adicional, osea supongo que si el jugaodr eligió a esa chica y fue calido con ella 3 veces es porque es su favorita, supongo. Con eso solucionamos el problema de los puntos.


Tambien respecto a lo del beat de nino, no debe sumar puntos en nada, solo debe servir de boost para los minijuegos, si hay que cambiar algo de codigo, me avisas.

---

## Anexo A · Espejo Final B ↔ Evento 6

| Final B (`02_cap1_final_hub3.rpy`) | Evento 6 |
|---|---|
| B1 Lunes: «Cuatro semanas para esto. Y llego igual que cuando empecé.» | «Hoy llego con cinco nombres.» |
| B2 Las cinco confiesan (no sé nada) | Las cinco confiesan (lo sé): ichika «siete y cuarto», miku «la otra mitad también», itsuki «y lo sé» |
| MC: «Hagan lo que **sepan**» (relleno) | «Hagan lo que **saben**» (lista con cinco nombres detrás) |
| `profe: Pueden empezar.` + hoja | Igual |
| B3.1 Yotsuba mira a las demás, hoja en blanco | Escribe y mira a las demás: las dos cosas |
| B3.2 Ichika finge dormir con el guion bajo la hoja | Ojos abiertos; guion plegado en el bolsillo |
| B3.3 Nino finge revisar 40 minutos | Entrega y sale (cálida) / se queda (tibia, fría, no visitada) |
| B3.4 Itsuki: «habría dado lo que fuera por decirle dónde mirar» | Levanta la mano al profesor |
| B3.5 Miku borra y reescribe, la goma es un tocón | Goma entera, audífonos sobre el pupitre |
| B4 Aula tarde: cinco confiesan el fracaso, suena `derrota` | Las cinco, suena `cotidiano` |
| B6 Maruo: «Una aprobó. Cuatro no.» | «Cinco.» |
| B6 «No te rendiste. Tampoco hiciste nada.» | «No te rendiste. Y esta vez tampoco te quedaste quieto.» |
| B7 Las puertas del pasillo, despedidas | Las puertas, *bienvenidas* |
| B8 Curry: «Era la primera vez que no sentía nada» | «Esta vez lo sentí» |
| B9 Libreta: «Los usé todos y no cambié a ninguna» | Libreta: «Ahora, juntas.» |

## Anexo B · Los 20 sobrevivientes

| Estado | (r1, r2, r3) | Cálidas |
|---|---|---|
| **superado** | (f,c,c) (c,f,c) | 2 |
| | (f,c,t) (f,t,c) (c,f,t) (t,f,c) | 1 |
| | (f,t,t) (t,f,t) | 0 |
| **mixto sin fría** | (c,t,t) (t,c,t) (t,t,c) | 1 |
| | (t,t,t) | 0 |
| **mixto con fría en hub 3** | (c,c,f) | 2 |
| | (c,t,f) (t,c,f) | 1 |
| | (t,t,f) | 0 |
| **bueno** | (c,c,c) | 3 |
| | (c,c,t) (c,t,c) (t,c,c) | 2 |

## Anexo C · Assets de E6

| Asset | Tipo | Estado | Nota |
|---|---|---|---|
| `cg_yotsuba_examen`, `cg_ichika_examen`, `cg_nino_examen`, `cg_itsuki_examen`, `cg_miku_examen` | CG | NUEVO (A) | POV desde el pupitre de MC, espejo de `*_fracaso`. Estado-agnósticos. |
| `cg_cinco_aprobadas` | CG | NUEVO (A) | Frontal, cinco en fila, misma mesa y semilla de `cg_cinco_estudiando`. |
| `cg_miku_audifonos_mesa` | CG | NUEVO (B, solo cálida) | La imagen firma de Miku. |
| `boletin_cinco`, `chat_grupo`, `mj_*` | pantallas | NUEVO | Sin arte; PNG por script. |
| 5 × `<h>_int` | Character | NUEVO | Caja de su color, sin placa. |
| `mj_acierto`, `mj_fallo` | SFX | Opcional | Alternativa: reutilizar `sfx_hover`/`sfx_click`. |
| Sprites `miku sonrie`, `yotsuba serena`, `ichika sincera`, `nino suelta`, `itsuki serena` | sprite | Condicional (P-23) | Solo si el guion los pide. |

## Anexo D · Checklist de pruebas (para el chat final)

- Recorrer **los 20 sobrevivientes** (Anexo B) y las **4 ramas de Nino × beat**.
- Cada hermana en cada estado: monólogo, frase, gesto y eco aparecen **una** vez.
- Minijuego solo en cálida; dificultad según `nino_rama_beat`; asistencia, puntos de control y «saltar».
- Notas ≥ 60 y diagonal 100; sin 100 fuera de la diagonal.
- `despido_cap1` nunca `True` dentro de E6.
- Guardar, cargar y retroceder durante y entre minijuegos; saltar texto no da victoria.
- HUD, música (tema solo si cálida), silencios y `amb_reloj`.
- Galería: nuevos CG sin romper el conteo.
