# Evaluación de sprites · Cierre de conjunto · Prólogo + Capítulo 1

> Revisado sobre el árbol de trabajo actual. Ya tiene aplicadas las evaluaciones aprobadas de Nino, Miku, Itsuki y Yotsuba, y lleva **simuladas** las 10 sentencias propuestas para Ichika (pendientes de tu aprobación).
> Es una evaluación: no se tocó ningún `.rpy`. No reabro ninguna decisión aprobada; donde algo choca, solo lo señalo.
> **Estado (14/11/2026):** aprobado. Las 10 sentencias de Ichika ya están aplicadas (ya no son una simulación) y el Lint sale limpio. No propone ningún cambio propio. El único hallazgo con cambio (Ichika, final malo 945 y 960) se trató en `EVAL_SPRITES_ICHIKA_CAP1.md` y ya está aplicado.
> Fuentes: las cinco evaluaciones (`EVAL_SPRITES_NINO_CAP1.md`, `…_MIKU_…`, `…_ITSUKI_…`, `…_YOTSUBA_…`, `…_ICHIKA_…`), las fichas de sus §1, `docs/GUIA_ARTE.md` §9 y los `.rpy` del recorrido. El «antes» es `git show 19d226e` (HEAD).

---

## 0. Avisos

| # | Qué | Detalle |
|---|---|---|
| 1 | **La base del «antes» es HEAD (`19d226e`, 13/11, «Narrativa Terminada»)** | Ese commit no declara `nino seria` ni `yotsuba seria`, así que es anterior a las cinco evaluaciones. El «después» es el árbol de trabajo actual más las 10 sentencias propuestas de Ichika. |
| 2 | **Alcance de los conteos** | `01_prologo.rpy` y los 13 `02_cap1_*.rpy`, incluidos los beats y `02_cap1_hubs.rpy`. Se cuentan las sentencias `show <hermana> <expr> at …` y, aparte, los `call e6_foco("<hermana>", "<expr>")`. Los `show <hermana> at …` sin atributo cuentan como «tinte». |
| 3 | **Miku: `neutral` 57 → 19 no es un cambio de cara** | Es la limpieza de los `show` que repetían la misma cara (sesión del 13/11): pasaron a ser de solo tinte, que suben de 22 a 57. La cara en pantalla es la misma. Lo aviso para que la tabla del §4 no se lea como «Miku perdió 38 neutrales». |
| 4 | **El hallazgo del conjunto va en el documento de Ichika** | Final malo l. 945 y 960 → `agotada` (§2, tabla del final malo). |

---

## 1. Qué significa `neutral` en cada hermana (la clave de las escenas de grupo)

Cuando las cinco están en formación, casi todas llevan `neutral`. **Pero `neutral` no es la misma cara en las cinco** (fichas del §1 de cada evaluación):

| Hermana | Su `neutral` | ¿Sonríe? | Consecuencia en grupo |
|---|---|---|---|
| Ichika | Medio lado, párpados a media asta | **Sí, suave** | Si el narrador dice que **ninguna** sonríe, Ichika necesita otra cara (`agotada`) |
| Nino | Brazos cruzados, dientes apretados. «No es una cara en reposo.» | No | Vale para cualquier escena tensa |
| Miku | Párpados a media altura, boca en línea | No | Vale para cualquier escena tensa |
| Yotsuba | Sonrisa cerrada y suave | **Sí, suave** | Ídem que Ichika: necesita `seria` (o `incomoda`) |
| Itsuki | Boca en línea, compostura | No | Vale para cualquier escena tensa |

**Regla que sale del conjunto:** en una formación triste o tensa, Nino, Miku e Itsuki pueden quedarse en `neutral`. **Ichika y Yotsuba, no**, si el texto niega la sonrisa. Ya se aplicó con Yotsuba (final malo 948 → `seria`, aprobado) y faltaba en Ichika, en la misma formación (§2). Para el Cap. 2, conviene escribir así las formaciones tristes desde el principio.

---

## 2. Tabla por archivo (escenas con varias hermanas)

Caras en el orden de la formación: **I**chika · **N**ino · **M**iku · **Y**otsuba · i**T**suki. Las abreviaturas son `neut`, `sonr`, `agot`, `mole`, `inco`, `enco`, `seri`, `sorp`, `pill`, `nerv` y `timi`. ⟨prop⟩ = propuesta de Ichika pendiente.

Criterios: **R** = reacciones desiguales a la misma noticia · **E** = equidad (nadie destaca sin que la escena lo pida) · **K** = coherencia entre evaluaciones (el mismo tipo de momento, resuelto igual).

### 01_prologo.rpy

| archivo:línea | Escena | Línea / narración | Caras (I N M Y T) | Veredicto | Propuesta | Por qué |
|---|---|---|---|---|---|---|
| 975 | Las cinco a la vez por primera vez | l. 977 «Eran cinco. Cinco rostros idénticos mirándome al mismo tiempo.» | neut · neut · neut · sonr · mole | ✅ | — | E: cada una con su cara de presentación. Itsuki sigue molesta por el almuerzo y Yotsuba, contenta por la «coincidencia». Lo pide el diálogo de antes |
| 1051 | Coro «¡No pensamos estudiar!» | l. 1062 «Yotsuba también. Medio tono más bajo que las demás.» | neut · neut · neut · inco · mole | ✅ | — | E: Yotsuba destaca porque la escena lo pide (revisión P13, aprobado). Itsuki, molesta, es su papel de esa noche |

### 02_cap1_apertura.rpy

| archivo:línea | Escena | Línea / narración | Caras (I N M Y T) | Veredicto | Propuesta | Por qué |
|---|---|---|---|---|---|---|
| 331 | Defienden el examen de las seis | l. 337 «Lo dijo mirando a Yotsuba, no a mí. Yotsuba soltó el borde de la hoja.» | sonr · neut · — · inco · — | ✅ | — | R: Ichika tapa con la máscara y Yotsuba sigue apurada porque la acaban de cortar (302). La diferencia está escrita |

### 02_cap1_conexiones.rpy

| archivo:línea | Escena | Línea / narración | Caras (I N M Y T) | Veredicto | Propuesta | Por qué |
|---|---|---|---|---|---|---|
| 967 | Interc. 1 · llegan | (el MC: «Buenas tardes.») | neut · neut · neut · sonr · neut | ✅ | — | Formación con la cara base de cada una |
| 1079 | Interc. 1 · coro «¿Qué?» | (línea de `quintillizas`) | sonr · neut · neut · sonr · mole | ✅ | — | R: ninguna pone cara de sorpresa, y ninguna destaca. Es lo mismo que en los otros coros (K: un coro no cambia caras, salvo P13) |
| 1244 | Interc. 1 · «Treinta días, tutor.» | — | sonr · mole · neut · inco · mole | ✅ | — | Cada una acaba la escena en la cara de su última línea |
| 1742 | Interc. 3 · llegan | l. 1749 «Las cinco ya estaban en el aula cuando entré.» | neut · neut · neut · sonr · neut | ✅ | — | Formación |
| 2277 | Interc. 4 · se ha ido Nino | l. 2283 «Las otras cuatro seguían ahí.» | neut · — · neut · sonr · neut | ✅ | — | Formación |
| 2365 | Interc. 4 · la misma noticia, cuatro reacciones | l. 2378 «Las cuatro me miraron, y las cuatro apartaron la vista casi al mismo tiempo.» | neut · — · neut · inco · mole | ✅ | — | R: las cuatro reaccionan distinto, pero cada una tiene su línea: Ichika informa, Miku describe («...Miró el celular y se quedó quieta.»), Yotsuba se culpa («...Puede que sea culpa mía.») e Itsuki lo niega («Nino no se va sin avisar. Es un hecho.»). No es desigualdad: es reparto |
| 2829 | Interc. 5 · llegan | l. 2835 «Las otras cuatro fueron llegando de a una. Esta vez nadie hizo ruido.» | neut · mole · neut · inco · neut | ✅ | — | Nadie sonríe abiertamente. Yotsuba, `incomoda` (aprobado, 2831); el medio lado de Ichika no choca con «nadie hizo ruido» |
| 3115 | Interc. 5 · coro «Adios» | l. 3117 «Todas se fueron.» | neut · neut · enco · sonr · mole | ✅ | — | Cada una se va con la cara de su última línea |
| 3349 | Interc. 6 · llegan | l. 3356 «Faltaba la cereza del pastel.» | neut · neut · neut · sonr · neut | ✅ | — | Formación |
| 3391–3426 | Interc. 6 · «Dejen de hacerlo parecer una hazaña.» | (Nino corta el chiste de Ichika) | **neut ⟨prop⟩** · neut · neut · inco · neut | ✅ | — | K: Yotsuba (3391 → `incomoda`, aprobado) e Ichika (3425 → `neutral`, propuesta) bajan un escalón **en el mismo punto y por la misma razón**. Hoy, sin la propuesta, Ichika sería la única con la sonrisa entera hasta el final |
| 3582 | Interc. 6 · clima malo | l. 3582 «Nadie se rió. Ni siquiera Ichika.» | neut ⟨prop⟩ · neut · neut · inco · mole | ✅ | — | Con la propuesta de Ichika, ninguna sonríe abiertamente. Yotsuba, con su sonrisa torcida, es la decisión aprobada |

### 02_cap1_evento6.rpy

| archivo:línea | Escena | Línea / narración | Caras (I N M Y T) | Veredicto | Propuesta | Por qué |
|---|---|---|---|---|---|---|
| 259 / 2178 | Formaciones (`e6_formacion_neutral`) | — | neut ×5 | ✅ | — | E: la misma cara para todas. Ver K-4 en el §3 |
| 3286 | Departamento (`e6_entrar`) | — | neut ×5 | ✅ | — | Ídem |
| 3923–3995 | Mesa · dan la vuelta a los boletines: la misma noticia para las cinco | l. 3919 «Cinco hojas, un solo sonido.» | sonr · nerv · enco · sonr → neut → sonr · sonr | ✅ | — | R: cinco reacciones distintas, cada una escrita: Miku llora (l. 3927 «Le corrió una lágrima por la cara.»), Ichika se ríe (l. 3933), a Nino se le quiebra la voz (l. 3953), Yotsuba se queda callada por primera vez (l. 3969) e Itsuki lee como quien lee un contrato (l. 3985). Que tres sonrían y dos no es lo que dice el texto |
| 4083–4095 | Mesa · posan para la foto | l. 4079 «Me puse de pie al otro lado de la mesa, con el celular de Yotsuba en las manos.» | sonr · neut · enco · sonr · neut | ✅ | — | E: cada una posa a su manera. Nino posa con los brazos cruzados, que es su manera de posar. Va justo antes del CG `cg_cinco_aprobadas` |

### 02_cap1_final_malo.rpy

| archivo:línea | Escena | Línea / narración | Caras (I N M Y T) | Veredicto | Propuesta | Por qué |
|---|---|---|---|---|---|---|
| 173 | Beat · llegan corriendo | l. 168 «Con cara de haberse levantado de golpe.» | neut · neut · neut · sorp · neut | ✅ | — | Yotsuba es la que habla («¡Se oyó hasta la escalera!») |
| 198 | Beat · «Papá lo despidió.» | l. 200 «Nadie dijo nada.» | neut · neut · neut · sorp · neut | ✅ | — | R: Yotsuba conserva la sorpresa de su línea anterior y las otras se quedan en su base. El medio lado de Ichika es la cara de antes del chiste reflejo (215), que el texto castiga en la l. 220 «Nadie se rió. Ni ella.». Todo cuadra |
| 511 | Hub 3 · el aula de la mañana | l. 520 «Nadie había abierto un libro.» | neut · neut · neut · inco · neut | ✅ | — | La narración no habla de caras |
| 554–599 | Hub 3 · cada una dice cómo llega | l. 599 «Me miraron las cinco. Esperando que les dijera algo.» | **agot ⟨prop⟩** · seri · neut · inco · neut | ✅ | — | E/K: cada una habla desde su grieta, con su cara. Sin la propuesta, Ichika sería la única sonriente de las cinco mientras dice «Dormí cuatro horas» |
| **945** | Hub 3 · la tarde, después de los exámenes | l. 952 «Nadie recogía nada. Ninguna dijo «salió bien».» | **neut** · neut · neut · seri · neut | 🔁 | **Ichika `agotada`** (945 y 960) | **Hallazgo del conjunto.** K: en esta misma formación, Yotsuba pasó de `neutral` a `seria` (aprobado) justo por esta línea, porque su `neutral` sonríe. El de Ichika también sonríe (§1), así que hoy es **la única de las cinco** que sonríe mientras el narrador dice que ninguna lo hace. Ya está metido en el documento de Ichika (§5, §6 y §7) |
| 1051 | Hub 3 · «Va a pasar lo que dije que pasaría.» | — | agot · seri · enco · seri · mole | ✅ | — | Cada una con la cara de su confesión |
| 1259–1420 | Despedida, una por una | — | Y inco · I **agot ⟨prop⟩** · M neut · N seri → nerv · T neut → timi → neut | ✅ | — | E: cada despedida tiene su arco. Ver K-6 en el §3 sobre Yotsuba |

---

## 3. Coherencia entre las cinco evaluaciones

| # | Tipo de momento | Cómo se resolvió en cada una | ¿Coherente? |
|---|---|---|---|
| K-1 | **El texto niega la sonrisa** («Nadie se rió», «Sin sonrisa») | Yotsuba: interc. 6 3391 → `incomoda`, interc. 5 2831 → `incomoda`. Ichika: 3425 → `neutral`, 739 y 1285 → `agotada`, E6 2599 → `neutral`. Final malo 215 → 222: ya lo resuelve el cambio de sprite | ✅ La misma regla: un escalón abajo en **su propia** escala, o hasta el fondo si el texto lo dice entero |
| K-2 | **Una línea de grupo que niega la sonrisa a todas** («Ninguna dijo «salió bien»») | Yotsuba 948 → `seria` (aprobado). Ichika 945 → `agotada` (propuesta nueva). Nino, Miku e Itsuki: su `neutral` ya no sonríe | ✅ Tras la propuesta |
| K-3 | **La máscara** (Ichika, Yotsuba) | Las dos se leen por el contexto (C3 en las dos evaluaciones). La sonrisa de máscara se queda si el texto la marca. La bajada de máscara de la cálida va con una cara propia, sin sonrisa: Yotsuba `seria`, Ichika `agotada` / `determinada` | ✅ El mismo criterio. La fría no la baja en ninguna de las dos hasta el final malo |
| K-4 | **Formaciones de entrada** | E6: `e6_formacion_neutral` pone a las cinco en `neutral`. Conexiones: Yotsuba llega en `sonriendo` a las formaciones de las interc. 1, 3 y 6, y el resto en `neutral` | ⚠️ **Lo señalo, no lo cambio.** Es una pequeña diferencia de criterio entre el E6 y conexiones, solo en Yotsuba. Como su `neutral` ya sonríe, en pantalla la diferencia es de grado. Las dos cosas están aprobadas |
| K-5 | **Coros** (`quintillizas`) | Ninguna cambia de cara para un coro, salvo Yotsuba en el prólogo (P13) | ✅ |
| K-6 | **Despedidas del final malo** | Ichika baja la sonrisa (⟨prop⟩ `agotada`: «Aquí no hace falta que sonría»). Nino: `seria` → `nerviosa`. Itsuki: `neutral` → `timida` → `neutral`. Miku: `neutral`. Yotsuba se queda en `incomoda`, que sonríe torcido, incluida su rama fría («Me llamó «tutor». Con el tono que se usa con un desconocido.») | ⚠️ **Lo señalo, no lo cambio.** Yotsuba es la única que se despide con una sonrisa, aunque sea torcida. El texto lo sostiene en sus ramas cálida y tibia («Gracias por venir todos los días»). En la fría es más discutible, y ya está anotado en su §9 como `show` compartido entre ramas |
| K-7 | **«Dormí cuatro horas»** | E6 lunes (P3, aprobado en la revisión): `sonriendo`, por el orgullo de haberlas gastado en las fórmulas. Final malo 554: `agotada` ⟨prop⟩, por la culpa de haberlas gastado en la audición | ✅ La misma frase, contextos opuestos y caras opuestas. Es a propósito |
| K-8 | **La misma noticia para todas** (despido, nota del examen, Nino se va) | Cada hermana reacciona con la cara de **su** línea, y ninguna reacciona sin línea | ✅ En las tres escenas. Nadie destaca sin texto |

**Equidad (E), en resumen:** en ninguna escena de grupo hay una hermana con cara expresiva sin que una línea suya o del narrador lo pida. Las dos excepciones que había, Ichika sonriendo en la interc. 6 y en la tarde del final malo, las arreglan las propuestas de Ichika. Antes de las cinco evaluaciones había más casos, todos ya resueltos en las aprobadas: Yotsuba sonriendo en la interc. 5 (2831) y en la interc. 6 (3391), e Itsuki con su `molesta` de comodín.

---

## 4. Uso de cada expresión, por hermana: antes de las cinco evaluaciones y al terminar

Antes = HEAD `19d226e`. Después = el árbol actual más las 10 sentencias de Ichika. Sentencias `show <hermana> <expr>`; entre paréntesis, los `e6_foco` del E6.

| Hermana | Expresión | Antes | Después | Δ |
|---|---|---|---|---|
| **Ichika** | neutral | 37 (12) | **33 (13)** | −4 (+1) |
| | sonriendo | 36 (21) | **36 (20)** | 0 (−1) |
| | agotada | 7 | **12** | +5 |
| | determinada | 3 | 3 | 0 |
| | *tinte* | 24 | 23 | −1 |
| **Nino** | neutral | 83 (12) | **63 (8)** | −20 (−4) |
| | molesta | 20 (9) | 20 **(10)** | 0 (+1) |
| | pillada | 9 (4) | **17 (5)** | +8 (+1) |
| | nerviosa | 6 (2) | 6 (2) | 0 |
| | seria ➕ | — | **6 (2)** | +6 (+2) |
| | *tinte* | 24 | 27 | +3 |
| **Miku** | neutral | 57 (10) | **19** (10) | −38 (aviso 3) |
| | encogida | 10 (8) | **12** (8) | +2 |
| | relajada | 5 (2) | 5 (2) | 0 |
| | animada | 3 (2) | **2** (2) | −1 |
| | *tinte* | 22 | **57** | +35 (aviso 3) |
| **Yotsuba** | sonriendo | 43 (17) | **42** (17) | −1 |
| | incomoda | 26 (3) | **25 (2)** | −1 (−1) |
| | neutral | 9 (7) | **5** (7) | −4 |
| | sorprendida | 4 (1) | **3** (1) | −1 |
| | seria ➕ | — | **7 (1)** | +7 (+1) |
| | *tinte* | 23 | 23 | 0 |
| **Itsuki** | neutral | 50 (15) | **62** (15) | +12 |
| | molesta | 44 (2) | **33** (2) | −11 |
| | timida | 6 (4) | **5** (4) | −1 |
| | sorprendida | 4 | 4 | 0 |
| | sonriendo 🎨 | 1 (4) | 1 (4) | 0 (sprite rehecho) |
| | *tinte* | 23 | 23 | 0 |

**Lectura rápida:**

- **Sale lo que sobraba:** el `molesta` de comodín de Itsuki (−11), el `neutral` de Nino que no era reposo (−20) y la sonrisa de Yotsuba donde el texto la niega.
- **Entra lo que faltaba:** las dos caras sin sonrisa nuevas (`nino seria`, `yotsuba seria`) y el cansancio de Ichika (+5 `agotada`).
- **Las caras secundarias se usan más que antes.** Nino dependía de `neutral` en 83 de 118 `show` con atributo (70 %) y ahora en 63 de 112 (56 %). Hoy ninguna hermana pasa del 60 % con una sola cara. La que más se acerca es Itsuki (`neutral` 62 de 105, 59 %): es su compostura, y su evaluación lo aprobó así. Miku no entra en esta cuenta por el aviso 3.

---

## 5. Qué hacer

- **Nada propio de este documento.** El único 🔁 que sale del conjunto (Ichika 945 + 960) va con la aprobación de Ichika.
- **Señalado, sin proponer (ya aprobado en otras):** K-4 (Yotsuba entra sonriendo en las formaciones de conexiones y en `neutral` en las del E6) y K-6 (Yotsuba se despide en `incomoda` también en su rama fría).
- **Para el Cap. 2:** en las formaciones tristes, escribir desde el principio `ichika agotada` y `yotsuba seria` (o `incomoda`). El `neutral` de esas dos sonríe (§1).
