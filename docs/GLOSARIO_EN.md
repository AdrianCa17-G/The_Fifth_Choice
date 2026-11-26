# Glosario y guía de estilo: inglés (v1.1)

Referencia obligatoria para cada sesión de traducción (tareas C1–C5, E1) y base para el ruso (sección 6 del plan).
Si aparece un término que no está aquí: se decide, se añade a este archivo y se avisa a Adrian.

Las dudas del día 1 ya están resueltas por Adrian (23/11/2026, §10). Si surge una nueva, se marca **[DECIDIR]**
con una recomendación, y se traduce con la recomendación hasta que Adrian decida.

---

## 1. Reglas técnicas (recordatorio)

- Solo se escribe en `game/tl/english/`. Nunca en los `.rpy` del juego.
- Se conservan **exactas**: `[mc]`, `[nombre_jugador]`, `[tiempo_restante!t]`, `[nombre_h!t]`, `[e6_p1!t]`,
  `[e6_p2!t]`, `[n]` y todas las etiquetas `{i}`, `{b}`, `{w}`, `{nw}`, `{color=…}`, `{size=…}`, `{font=…}`.
- Los huecos `{}` de cadenas como `"Final de {}"` o `"{} miembros"` se conservan en el mismo número
  (se rellenan con `.format()` en el código). Pueden cambiar de sitio dentro de la frase: `"Ending: {}"`.
- `!t` significa que el valor que entra también se traduce (por ejemplo `tiempo_restante` = «casi cuatro
  semanas» se traduce en su propia cadena). No se quita.
- ~100 caracteres por línea de diálogo como máximo. Opciones de menú y botones: no más largos que el español.
- Las cadenas de interfaz (`translate english strings`) son **globales**: una misma cadena española se
  traduce una sola vez para todo el juego. Si una palabra suelta tuviera dos sentidos, se avisa (ver §9).
- Cursiva `{i}` y comillas angulares «» del español → comillas inglesas “ ” (o `"` dentro de las cadenas).
- Raya de diálogo cortado (`—`) se mantiene: `"I didn't mean—"`.

---

## 2. Nombres

Orden occidental en inglés: **nombre de pila + apellido** (es como lo usan el anime y el manga oficiales en inglés).
En el juego casi siempre se usa solo el nombre de pila.

| Español (juego) | Inglés | Notas |
|---|---|---|
| Futaro (nombre por defecto del jugador) | **Futaro** | Sin macrones (no «Fūtarō»). El jugador puede cambiarlo: siempre vía `[mc]`. |
| Uesugi (apellido de Futaro, Raiha, Isanari) | **Uesugi** | «Casa de los Uesugi» → **the Uesugi house**. |
| Ichika, Nino, Miku, Yotsuba, Itsuki | **Ichika, Nino, Miku, Yotsuba, Itsuki** | Igual. |
| Nakano (apellido de las quintillizas) | **Nakano** | El profesor llama «Nakano.» a cualquiera de las cinco: es el chiste. Se deja **"Nakano."** solo, sin Miss. |
| Raiha | **Raiha** | |
| Isanari | **Isanari** | Padre de Futaro. |
| Maruo | **Maruo** | Padre de las quintillizas. Nadie le llama por el nombre en voz alta; en placas y créditos, **Maruo**. |
| Profesor (placa) | **Teacher** | |
| Estudiante Nueva (placa de Itsuki antes de presentarse) | **New Student** | |
| Las quintillizas (placa de las cinco a la vez) | **The Quintuplets** | |
| ??? | ??? | |
| Instituto Asaba | **Asaba High** | Nombre inventado del juego; no cambiar por el del canon. |

---

## 3. Honoríficos: sin honoríficos (decidido)

**Dato del texto:** el español **no usa ningún honorífico** (0 apariciones de -kun, -san, -chan, -sama, senpai, sensei).
Las chicas llaman a Futaro por su nombre (`[mc]`) o «tutor»; Raiha le dice «hermanito»; el profesor dice «Nakano».

| Opción | Cómo queda | A favor | En contra |
|---|---|---|---|
| **A. Sin honoríficos (recomendada)** | "Thanks, [mc]." · "Morning, [mc]!" | Fiel al español, que ya los quitó. Lectura fluida. `[mc]` puede ser cualquier nombre del jugador, y «Pedro-kun» queda raro. | Pierde algo de sabor japonés. |
| B. Añadir -kun/-san/-chan | "Thanks, [mc]-kun." | Le gusta a parte del público del anime. | Hay que inventar el registro de cada pareja de personajes (el español no lo marca). Choca con nombres de jugador occidentales. Más trabajo y más errores en E1. |

**Decisión (Adrian, 23/11): A, sin honoríficos.** Nunca -kun, -san, -chan, -sama, senpai ni sensei.

Términos de trato que sí existen en el español:

| Español | Inglés | Quién lo dice |
|---|---|---|
| hermanito | **[mc]** por defecto; **big brother** en momentos de cercanía o broma | Raiha. Según la escena: "[mc]! Dinner!" pero "...You okay, big brother?". Nunca "Onii-chan" ni el nombre «Futaro» escrito: siempre `[mc]`. |
| tutor | **tutor** ("Thirty days, tutor.") | Nino, Yotsuba, Itsuki |
| papá / mi padre | **Dad** / **my father** | «papá» → Dad (Raiha, Futaro, Nino al teléfono, Ichika: "our dad"). «mi padre» → my father. |

---

## 4. Materias y exámenes

En el juego hay **cinco materias**, una por hermana (Evento 6, de lunes a viernes).
**«Japonés» es la materia de lengua y literatura japonesas: una sola materia**, no dos.

| Español | Inglés | Hermana del examen | Notas |
|---|---|---|---|
| Japonés | **Japanese** | Yotsuba | Lengua y literatura japonesas. Incluye «comprensión lectora» → **reading comprehension**. |
| Matemáticas | **Math** | Ichika | Inglés americano: Math, no Maths. |
| Inglés | **English** | Nino | Ojo con el minijuego de Nino (§8). |
| Ciencias | **Science** | Itsuki | |
| Sociales | **Social Studies** | Miku | «Historia es tu asignatura» → "History's your thing." (historia dentro de Sociales). |
| materia / asignatura | **subject** | | |
| temario | **syllabus** / **the material** | | |
| examen de práctica | **practice exam** | | |
| examen final / los exámenes | **finals** / **the exams** | | |
| aprobar / reprobar | **pass** / **fail** | | |
| nota / calificación | **grade** / **score** | | Cien → **a hundred** / **100**. |
| el primer lugar (de la clase) | **top of the class** | | |
| boletín (pantalla de notas) | **report card** | | Cabecera «LA CUENTA» → **THE TALLY**. |

---

## 5. Apodos, nombres propios y términos recurrentes

| Español | Inglés | Notas |
|---|---|---|
| «Contrato» (el dragón de Ichika) | **"Contract"** | Nombre propio del dragón; con mayúscula. |
| «¡Equipo Quintillizas + Tutor!» (grupo de chat) | **"Team Quintuplets + Tutor!"** | Aparece en varias cadenas del chat: igual en todas. |
| sexto integrante | **sixth member** | |
| tarde libre | **free afternoon** | |
| «TARDE {} DE 3» | **AFTERNOON {} OF 3** | |
| «Quedan [tiempo_restante!t]» | **"[tiempo_restante!t] left"** | El valor («casi cuatro semanas») se traduce aparte: "almost four weeks". |
| ENCUENTRO / ESCENA CLAVE | **ENCOUNTER** / **KEY SCENE** | Rótulos del HUD. |
| DECISIÓN / HORA DE DECIDIR | **DECISION** / **TIME TO DECIDE** | |
| final / final malo | **ending** / **BAD ENDING** | «Final de Ichika» → "Ichika's Ending". |
| rama cálida / tibia / fría | **warm / lukewarm / cold** | Catálogo de animaciones de Extras. |
| Sala de ensayo | **Rehearsal Room** | Hub de Ichika. |
| Centro comercial | **Shopping Mall** (en escena: **the supermarket** si es dentro de la tienda) | Hub de Nino. |
| Biblioteca | **Library** | Hub de Miku. |
| Pista de atletismo | **Track** | Hub de Yotsuba. |
| Aula vacía | **Empty Classroom** | Hub de Itsuki. |
| Azotea | **Rooftop** | |
| el contrato / la tarifa (de tutor) | **the contract** / **the rate** ("five times the going rate") | |
| despedido / Despido temprano | **fired** / **Early Dismissal** | |
| curry (de Raiha) | **curry** | |
| acuario | **aquarium** | |
| soda de matcha | **matcha soda** | |
| audífonos (de Miku) | **headphones** | |
| cronómetro (de Yotsuba) | **stopwatch** | |
| «jajaja» (chat) | **"hahaha"** | Decidido. Se adapta al momento y a quien escribe (p. ej. "haha" más seco, "HAHAHA" si es Yotsuba eufórica). |

---

## 6. Fichas de voz

Basadas en una muestra de ~30 líneas por personaje sacadas de los `.rpy` (01_, 02_ y 05_).
Entre paréntesis, cuántas líneas tiene cada uno en el Prólogo + Cap. 1.

### Protagonista: `mc` (698), `mc_pensamiento` (1.449) y `narrador` (1.303)
- **Los tres son Futaro.** El narrador también va en primera persona y en pasado ("That's when I saw her.").
- Habla seco, corto, lógico. Frases de 2 a 8 palabras. No adorna, no bromea en voz alta, pero su ironía
  se nota en el pensamiento ("The details are what ruin the math.").
- `mc_pensamiento` (libreta crema): notas para sí mismo, a veces sin verbo. "Five notebooks, a syllabus split by
  subject, and zero expectations." Contracciones sí, jerga no.
- `narrador`: descripción limpia, ritmo de novela juvenil, sin florituras. Pasado simple.
- Evitar: "gonna", "kinda", tacos. Futaro es correcto incluso cuando es borde.
- Muestra: «No dije que lo hicieras.» → "I didn't say to do it." · «Bien. Anotado.» → "Fine. Noted."

### Ichika (242)
- La mayor. Actriz. Juguetona, burlona con Futaro, siempre con un chiste o una metáfora de teatro
  (guion, papel, audición, escena).
- Debajo, cansancio y miedo; cuando se le cae la máscara, las frases se cortan y bajan de tono.
- En inglés: ligera, teasing, con ritmo de escenario. "Well, well…" · "Exclusive offer, just for you, [mc]."
- Muestra: «¡Multitarea de actriz!» → "Actress multitasking!" · «Y lo digo sin guiones.» → "And that's off-script."

### Nino (354)
- La segunda. La más hostil con el tutor al principio. Cortante, a la defensiva, órdenes y reproches.
  Protectora feroz de sus hermanas. Exclamaciones y mayúsculas cuando estalla.
- Tsundere: niega lo que siente ("Ni creas que me molesta." → "Don't think it bothers me.").
- En inglés: sharp, cutting, sarcástica. Contracciones y frases cortas. Nada de vulgaridades.
- Muestra: «Treinta días, tutor. A ver a cuántas logras encontrar.» → "Thirty days, tutor. Let's see how many of us you find."

### Miku (227)
- La tercera. Callada, monótona, frases que **empiezan con «...»** (casi todas). Muy pocas exclamaciones.
- Fan de la historia (batallas, comercio, la sal); cuando habla de historia, se suelta y dice frases largas.
- En inglés se conservan los «...» iniciales: "...Hi." · "...It's my favorite." Tono plano, palabras simples.
- Muestra: «...Correcto. ...Lo comprobé.» → "...Correct. ...I checked."

### Yotsuba (240)
- La cuarta. Energía pura: **exclamaciones dobles**, «¡Tutor!», metáforas de deporte (carrera, vueltas, relevos, calentar).
- Optimista hasta cuando duele; cuando se apaga, frases cortas y sin «¡!», y se nota.
- En inglés: enthusiastic, cheerful. "Let's go!" · "Full team!" Mayúsculas solo donde el español ya las pone.
- Muestra: «¡Equipo completo! ¡Piernas y cabeza!» → "Full team! Legs and brains!"

### Itsuki (258) e `itsuki_inicio` (31)
- La quinta. Formal, orgullosa, muy correcta. Usa un registro algo culto ("carente de empatía", "poco digna").
  Le gusta la comida (*Munch...*). Discute con Futaro como iguales.
- `itsuki_inicio`: su primer encuentro, más altiva y ofendida.
- En inglés: proper, slightly stiff, sin contracciones cuando se pone digna ("I do not accept food from my tutor.").
  Contracciones cuando baja la guardia.
- Muestra: «Qué imagen tan poco digna de un tutor.» → "Hardly a dignified look for a tutor."

### Voces interiores del Evento 6 (`ichika_int`, `nino_int`, `miku_int`, `yotsuba_int`, `itsuki_int`)
- Pensamientos de cada hermana durante su examen. Mantienen la voz de cada una, pero más desnuda: presente,
  frases muy cortas, enumeraciones ("Question four. Trains. Four thirty-five.").
- Miku interior también empieza con «...». Yotsuba interior pierde las exclamaciones salvo «¡Pregunta dos!».

### Raiha (129)
- Hermana pequeña de Futaro. Alegre, mandona en casa, cariñosa. Exclamaciones, preguntas encadenadas.
- «hermanito» → `[mc]` por defecto, **big brother** en momentos de cercanía o broma (ver §3). Cita a «la maestra» → "Teacher said so!"
- Muestra: «¡Hermanito! Hice curry.» → "[mc]! I made curry." · «Hermanito... ¿Te encuentras bien?» → "Big brother... are you okay?"

### Isanari (82)
- Padre de Futaro. Relajado, bromista, un poco irresponsable; habla de dinero sin pudor. Cuando se pone serio,
  aparecen frases de padre cortas y sinceras.
- En inglés: casual, dad-joke energy, contracciones. "Don't sound so dramatic."
- Muestra: «Cinco veces la tarifa no cae del cielo dos veces.» → "Five times the rate doesn't fall from the sky twice."

### Maruo (105)
- Padre de las quintillizas. Frío, preciso, frases muy cortas. Nunca levanta la voz, nunca bromea.
  Le habla a Futaro de tú, pero como un empleador.
- En inglés: clipped, formal, sin contracciones casi nunca. "Very well." · "I did not ask you to be kind to my daughters."
- Muestra: «Ya vi suficiente.» → "I have seen enough."

### Profesor (16)
- Trata de usted a las alumnas («Si ya terminó, puede entregar.»). En inglés no hay usted: tono de aula neutro.
- «Nakano. Despierte.» → "Nakano. Wake up."

---

## 7. Registro general

- **Inglés americano** (color, favorite, math, mall).
- Contracciones normales en diálogo, salvo Maruo e Itsuki cuando se ponen formales.
- Chistes y juegos de palabras: se adaptan para que funcionen en inglés, no se traducen literal. Si no hay
  forma, nota en el commit.
- Números en diálogo: en letra hasta el cien ("a hundred"), en cifra en la interfaz.
- Onomatopeyas entre asteriscos (`*Munch...*`) → equivalente inglés entre asteriscos (`*Munch...*` vale tal cual).

---

## 8. Minijuegos

| Minijuego | Qué se traduce | Nota |
|---|---|---|
| Ichika (Matemáticas) | Enunciados, reglas, botones | Normal. |
| Itsuki (Ciencias) | Enunciados, reglas, botones | Normal. |
| Miku (Sociales, ritmo) | Valoraciones del golpe | «Perfecto / Bien / Pronto / Tarde / Fallo» → **Perfect / Good / Early / Late / Miss**. |
| Yotsuba (Japonés) | Texto de comprensión lectora y preguntas | Normal. |
| Nino (Inglés) | Ver abajo | Notas en romaji (decidido) |

**Minijuego de Nino (decidido: romaji).** En el código (`10_mj_nino.rpy`, `MJ_N1_ITEMS`) los productos están **en inglés**
("honey", "maple syrup"…) y la nota de cada uno está **en español** («miel», «sirope de arce»). Es un examen de
inglés para un jugador hispano. En la versión inglesa, si la nota se traduce al inglés, queda "honey" = "honey"
y el reto desaparece.
- **Decisión (Adrian, 23/11):** en `tl/english`, las notas pasan a **japonés en romaji** ("hachimitsu", "mēpuru shiroppu"…).
  Encaja con la historia (instituto japonés, clase de inglés) y mantiene el reto de emparejar.

---

## 9. Cadenas cortas de interfaz (contexto)

Son globales: cada una se traduce una vez. Contexto comprobado en el código:

| Español | Inglés | Dónde |
|---|---|---|
| Tarde | **Late** | Minijuego de Miku (`10_mj_miku.rpy:682`). Solo aparece ahí; «Tarde libre» es otra cadena. |
| Pronto | **Early** | Minijuego de Miku. |
| Bien | **Good** | Minijuego de Miku. |
| Media | **Medium** | Dificultad en Extras → Repetir (`08_extras.rpy:1212`). |
| Vacío | **Empty** | Huecos de guardado. |
| Sí / No | **Yes / No** | Confirmaciones. |
| VISITADA | **VISITED** | Mapa de hubs. |
| CLIC PARA CONTINUAR | **CLICK TO CONTINUE** | |

---

## 10. Decisiones del día 1 (Adrian, 23/11/2026)

1. **Honoríficos:** ninguno. Ver §3.
2. **«hermanito»:** `[mc]` por defecto, **big brother** en momentos de cercanía o broma. Ver §3.
3. **Minijuego de Nino:** notas en japonés en romaji. Ver §8.
4. **«jajaja» en el chat:** "hahaha", adaptado al momento y a quien escribe.
5. **Formato de números en la interfaz:** se revisa en la tarea D.

---

## 11. Decisiones de traducción del día C1 (24/11/2026)

1. **Chiste de la pronunciación (apertura, Nino):** en español, Futaro lee «He didn't want to go, but he had to.» con
   mal acento y Nino corrige «jad tu» → «had to» (se pega, no se separa). En inglés la corrección pasa a la
   pronunciación «a trozos»: Nino: *Had to. Not "hah-doh too." It links together, you don't chop it up.*
   El pensamiento posterior de Futaro conserva "had to".
2. **«profesor» (Futaro al profe):** "sir" ("Thank you, sir."); la placa sigue siendo **Teacher**.
3. **«gemelas»** (primera impresión de Futaro, prólogo): **twins**.
4. **Frase de Maruo «Tu padre lleva media vida prometiéndome cosas»:** "Your father has been promising me
   things for half his life." Maruo sin contracciones en todo el archivo.
5. **Itsuki (inicio):** formal con la boca abierta ("I do not need you.", "do not go near him"), contracciones
   cuando baja la guardia o se disculpa/ablanda.
6. **Pistas del juego de adivinanza (apertura):** los lugares van con la etiqueta de color y coinciden con los hubs:
   rehearsal room, shopping mall, library, track, empty classroom.
7. **«Hermanito» de Raiha en estas escenas:** `[mc]` al llamarlo o al darle órdenes ("[mc]! Come down for dinner
   already!"); **big brother** cuando se pone cariñosa, bromea o da ánimos ("Good luck, big brother!").
8. **Nombre del capítulo en el guardado:** «Prólogo» → **Prologue**, «Capítulo 1» → **Chapter 1**.

---

## 12. Decisiones de traducción del día C3 (24/11/2026)

1. **Frases citadas en `beat_casa` (la libreta):** repiten exactamente lo ya traducido en C1/C2: "stage rest",
   "Contract", "It links together, you don't chop it up.", "You won't last a week.", "Battles are won by whoever
   moves the rice.", "...Right?", "I mean, of course you will!", "I run and cheer.", "As long as it takes.",
   "The unit doesn't cancel there.", "Forget what I said.". Si se retoca una, se retoca en todas.
2. **«¡Hermanito!» de Raiha** (final malo y beat de la casa): `[mc]!` al llamarlo o saludarlo; **big brother**
   cuando pide ayuda, se preocupa o consuela. El revisor marcará esas líneas como «[mc] sin original»: es a propósito.
3. **Maruo** sin contracciones en todo el archivo ("I do not need to tell you which."). Nino y el resto, con contracciones.
4. **«despido temprano»** en narración: "early dismissal" (minúscula); la etiqueta de menú/extra sigue siendo **Early Dismissal**.
5. **Profesor en el aula:** "Nakano. Wake up." y "You may begin."; las alumnas le dicen "sir".
6. **Mensaje de Maruo:** "Apartment. Five o'clock. Maruo." (departamento → apartment, como en el resto).

---

## 13. Decisiones de traducción del día C4 (25/11/2026)

1. **Raiha en las conexiones:** `[mc]` al saludar o dar órdenes ("Good morning, [mc]!") y también cuando finge alegría
   ("Good night, [mc]!" tras el sobre del banco); **big brother** cuando bromea o se pone tierna ("Curry is liquid love,
   big brother!", "Big brother, this came. I'll leave it here, okay?").
2. **Nino:** «tonto» → **idiot**; «Idiota.» → "Idiot."; «Ni creas que me molesta» → "Don't think it bothers me."
3. **«señora obvia»** (Futaro a Itsuki): "Captain Obvious."
4. **Despedidas de Miku e Itsuki:** Miku "...See you tomorrow." (narración: "A few words..."); Itsuki "Until tomorrow."
   (narración: "Two words..."), para que el recuento de palabras del narrador cuadre.
5. **«aprobado a medias» / «sesenta por ciento»** (Itsuki a Yotsuba): "It's a barely-passing grade, Yotsuba."
6. **Léxico fijo:** tardes libres → **free afternoons**; «busca y encuentra» → **hide-and-seek**; «dejar en visto» → **leave on read**;
   ojeras → **dark circles** (en la opción de menú del desayuno: "I'm running on eye bags."); pulpito de salchicha → **sausage octopus**;
   «hoja de diagnóstico» → **diagnostic sheet**; Maruo: "I have seen enough." (sin contracciones).
7. **Etiquetas de lugar** (`ui_escena`): Azotea → **Rooftop**, Departamento → **Apartment**, Casa de Futaro → **[nombre_jugador]'s House** (nunca "Futaro" fijo: el jugador puede cambiarse el nombre).
8. **Mensajes del chat del sábado (opciones de menú):** entre comillas rectas, con el mismo orden que el español.

---

## 14. Decisiones de traducción del día C5 (25/11/2026) · Evento 6, primera mitad

Corte de C5/C6: C5 llega hasta `e6_miku_gesto_no_visitada` (lunes + los cinco exámenes de la mañana); C6 empieza en `e6_despues`.

1. **Rótulos del HUD:** «Aula · Japonés» → **Classroom · Japanese**, y así con **Math / English / Science / Social Studies**.
   «Semana de exámenes» → **Exam Week**. Contador: «cinco / cuatro / tres / dos exámenes» → **five / four / three / two exams**,
   «un examen» → **one exam** (queda "one exam left"). En la tarea D, «Aula · Día» (`07_ui.rpy`) debe seguir el mismo patrón: **Classroom · Day**.
2. **«No tengo que poder con todo.»** (Ichika, también en el minijuego `10_mj_ichika.rpy:21`) → **"I don't have to handle everything."**
   El monólogo cortado «No tengo que po—» → "I don't have to han—". Usar la misma frase en el minijuego (tarea D).
3. **Voces interiores (`*_int`):** Itsuki interior **sin contracciones** ("I do not know where"), como en el resto de su registro formal;
   Yotsuba, Ichika y Nino con contracciones. Miku interior conserva «...» inicial **salvo** en el monólogo del minijuego (el original ya no lo lleva).
4. **Pregunta de examen de Yotsuba:** "What does the main character feel when he's left alone?" (siempre "main character", no "protagonist").
5. **Frases que enlazan con eventos anteriores** (se repiten tal cual): "my starting point wasn't zero. It never was.",
   "Then focus on running. If it's your thing, do it well.", "I run and cheer.", "If you have the energy to make jokes,
   you have the energy to study.", "Only time will prove it.", "I'm going to last.", "I'm only telling you where to look.",
   "...Ten days. Twelve if it rained.", "Then stop picking up everyone else's pieces and take care of your own.", "And who picks up yours?".
6. **Nino:** «el golpe» (el rechazo que ve venir) → **the blow** ("I always see the blow coming"); «táper» → **container** (como en el beat de Nino).
   «tonto» → **idiot** (§13). Su monólogo del minijuego usa «treinta y dos días» → "thirty-two days".
7. **Yotsuba:** «vuelta de ventaja» → **bonus lap**; «testigo» (relevos) → **baton**; «tomar las fechas / fórmulas» (ambiguo) → "went over dates with Miku and formulas with Ichika".
8. **Profesor:** "Nakano. If you're done, you may hand it in." / "Nakano. You're smiling." Las alumnas: "sir".
9. **Maruo (cita en la mente de Futaro):** "If even one of them fails, it's over." (sin contracciones, como siempre en su voz).

---

## 15. Decisiones de traducción del día C6 (25/11/2026) · Evento 6, segunda mitad

C6 cubre desde `e6_despues` (tarde del viernes) hasta `e6_retrato` (cierre del capítulo).

1. **Maruo:** «señor» (Futaro a Maruo) → **sir** ("Good afternoon, sir.", "Yes, sir."). Nadie dice «Mr. Maruo». Maruo sin contracciones, como siempre.
   Su mensaje: «Cinco. Departamento.» → "Five. Apartment." Futaro: «la cuenta / la hora» → **the tally / the hour**.
2. **Boletín (papel de notas)** → **report card** en todo el capítulo («Cinco boletines» → "five report cards"). Mini-secuencia final: «Cien» → **100**
   cuando va en lista ("100, 100, 100, 100, 100"), y «alumno que no existe» → "a student who doesn't exist".
3. **Itsuki, «el juego»:** enlaza con su evento ("The game ends today." / "Then I won the game."): en C6 → "I said the game ended today. I never said who won."
4. **Raiha en la noche del Evento 6:** `[mc]!` al recibirlo con el curry ("[mc]! I made curry…"); **big brother** en el cuarto, cuando se pone cariñosa o
   preocupada ("Big brother, are you still up?", "Good night, big brother."). Frases clave: «voz de "ojalá"» → **"I hope so" voice**; «¿¡Acerté!?» → "Was I right?!".
5. **Isanari:** «examen sorpresa» → **pop quiz** ("Pop quiz passed."), igual que en el evento 1; «Gracias por la comida» → **"Thanks for the food."**
6. **Menú del domingo:** «Llevar a Raiha a algún sitio.» → **Take Raiha somewhere.** · «Contestar al grupo.» → **Answer the group.** ·
   «Cumplir una promesa.» → **Keep a promise.** · «Dormir hasta tarde. Por una vez.» → **Sleep in. Just this once.**
   Rótulo: «Aula · Viernes por la tarde» → **Classroom · Friday Afternoon**.
7. **Foto de las cinco:** «¡Digan "cinco"!» → **Say "five"!**; la respuesta del coro (`quintillizas`) → "Five!!".
8. **Miku:** «La página ciento veinte» → "Page one-twenty." / "One twenty-two."; en la rama cálida (sin «...») habla de corrido; en las demás conserva «...».
9. **Yotsuba:** «vueltas de ventaja» → **bonus laps** (como en C5); «Empecé en el uno por ciento» → "I started at one percent." (motivo del Cap. 1).
10. **«cosa de ceremonias» / «vocación»** (cierre de Futaro): "I always said I didn't study because of some calling. That was for ceremonies." y
    "If that isn't a calling…" para que el último verso conecte.
11. **Pendiente para la tarea D:** el chat de grupo (`chat_e6`), el boletín animado (`12_e6_boletin.rpy`) y los textos que llegan por Python/pantallas.
    Los nombres de las promesas (`[e6_p1!t]`, `[e6_p2!t]`) se dejan idénticos (son nombres propios).
12. **Cita de la libreta:** "Head-on, all five at once, I always lose." (igual en apertura, evento 6 y final malo). Revisión de naturalidad (25/11):
    en C1 se suavizaron 29 líneas rígidas de Prólogo y Apertura ("I'm here to tutor you, not to make friends.", "Not happening.", "Fair point. But you'll want to hear about the pay.").

---

## 16. Decisiones de traducción de la tarea D (26/11/2026) · Interfaz, minijuegos, chat y créditos

1. **Lugares (HUD y mapa):** «Habitación de [nombre_jugador]» → **[nombre_jugador]'s Room** · «Casa Uesugi» → **Uesugi House** ·
   «Instituto Asaba» → **Asaba High** · «Edificio de las Nakano» → **The Nakanos' Building** · «Piso de las Nakano» → **Nakano Apartment** ·
   «Sala de ensayo» → **Rehearsal Room** · «Centro comercial» → **Shopping Mall** · «Biblioteca» → **Library** · «Pista» → **Track** ·
   «Aula vacía» → **Empty Classroom**. Momento del día tras « · »: **Day / Evening / Sunset** («Azotea · Atardecer» → Rooftop · Sunset).
2. **Rótulos del HUD:** ENCUENTRO → **ENCOUNTER** · ESCENA CLAVE → **KEY SCENE** · DECISIÓN → **DECISION** · HORA DE DECIDIR → **TIME TO DECIDE**.
   «Quedan [tiempo_restante]» → **"[tiempo_restante!tc] left"**: `!tc` pone en mayúscula la primera letra cuando abre la frase
   (también en los pensamientos de Ichika, Nino, Miku e Itsuki; el de Yotsuba empieza por "Only" y sigue con `!t`).
3. **Títulos de los minijuegos:** «Relevo de las cinco» → **Quintuplet Relay** (en la pantalla de reglas, «EL RELEVO DE LAS CINCO» → THE QUINTUPLET RELAY,
   como en español) · «La máscara se cansa» → **The Mask Grows Tired** · «Compras para seis» → **Shopping for Six** ·
   «Cadena de conversiones» → **Conversion Chain** · «El compás» → **The Beat**.
4. **Minijuego de Ichika:** «sincera / sincero» → **honest** ("An honest line lowers it", "IT CAN ONLY BE HONEST"); «actuar» → **acting**.
5. **Opciones de fallo:** «Inténtalo de nuevo» → **Try again** · «Saltarlo» → **Skip it** · «Que lo haga ella» → **Let her do it**.
6. **Extras:** Galería → **Gallery** · Finales → **Endings** · cálida / tibia / fría → **Warm / Lukewarm / Cold** · dificultad
   **Hard / Medium / Assisted** · «Fin del prólogo» → **End of Prologue** (sin artículo, para caber en la tarjeta de animaciones) ·
   «Un estudiante perfecto» → **A Perfect Student** · «Continuará...» → **To be continued...**
7. **Chat de grupo:** «¡Equipo Quintillizas + Tutor!» → **Team Quintuplets + Tutor!**; Itsuki sin contracciones ("It is a fact, not a celebration.",
   "Acknowledged."); Miku conserva «...»; Yotsuba en mayúsculas y con «!!» como en español.
8. **Boletín:** «LA CUENTA» → **THE TALLY**; materias según §4 (Japanese, Math, English, Science, Social Studies).
9. **Formato de números (decisión 5 del plan):** los separadores siguen el idioma activo con `ui_num()` (`07_ui.rpy`): en inglés **1,000** y **1.5**;
   en español no cambia (1.000 y 1,5). Las fechas de guardado en orden de EE. UU. (**11/26/2026 · 20:13**) con la entrada manual
   `{#file_time}` de `tl/english/09_menus_sistema.rpy`. El espacio antes de «%» (100 %) se mantiene en inglés porque lo pone el código
   en la galería, la barra de progreso y el medidor de Ichika.
10. **Pistas de los finales:** deben caber en 2 líneas como en español. Nino: «Quien más distancia pone, en el fondo solo espera a alguien
    que no se rinda con ella.» → "Behind all that distance, she's only waiting for someone who won't give up on her."
11. **Créditos:** sin mencionar herramientas de IA de texto; mismo texto en `tl/english/16_creditos.rpy` y en la sección inglesa de `CREDITOS.md`.
