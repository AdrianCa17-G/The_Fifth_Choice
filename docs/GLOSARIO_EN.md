# Glosario y guía de estilo: inglés (v1.1)

Referencia obligatoria para cada sesión de traducción (tareas C1–C5, E1) y base para el ruso (sección 6 del plan).
Si aparece un término que no está aquí: se decide, se añade a este archivo y se avisa a Adrian.

Las dudas pendientes están marcadas con **[DECIDIR]**. Cada una trae una recomendación; mientras Adrian no
diga otra cosa, se traduce con la recomendación.

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

## 3. Honoríficos  [DECIDIR]

**Dato del texto:** el español **no usa ningún honorífico** (0 apariciones de -kun, -san, -chan, -sama, senpai, sensei).
Las chicas llaman a Futaro por su nombre (`[mc]`) o «tutor»; Raiha le dice «hermanito»; el profesor dice «Nakano».

| Opción | Cómo queda | A favor | En contra |
|---|---|---|---|
| **A. Sin honoríficos (recomendada)** | "Thanks, [mc]." · "Big bro!" | Fiel al español, que ya los quitó. Lectura fluida. `[mc]` puede ser cualquier nombre del jugador, y «Pedro-kun» queda raro. | Pierde algo de sabor japonés. |
| B. Añadir -kun/-san/-chan | "Thanks, [mc]-kun." | Le gusta a parte del público del anime. | Hay que inventar el registro de cada pareja de personajes (el español no lo marca). Choca con nombres de jugador occidentales. Más trabajo y más errores en E1. |

**Recomendación: A.** Se aplica desde C1 salvo que Adrian diga lo contrario.

Términos de trato que sí existen en el español:

| Español | Inglés | Quién lo dice |
|---|---|---|
| hermanito | **big bro** (cariñoso; "Big bro!" a principio de frase) · [DECIDIR] alternativa: "Onii-chan" | Raiha |
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
| «jajaja» (chat) | **"lol"** · [DECIDIR] o "hahaha" | Recomendado "hahaha": más neutro para la voz de cada chica. |

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
- Siempre «hermanito» → **big bro** (ver §3). Cita a «la maestra» → "Teacher said so!"
- Muestra: «¡Hermanito! Hice curry.» → "Big bro! I made curry."

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
| Nino (Inglés) | Ver abajo | **[DECIDIR]** |

**Minijuego de Nino [DECIDIR].** En el código (`10_mj_nino.rpy`, `MJ_N1_ITEMS`) los productos están **en inglés**
("honey", "maple syrup"…) y la nota de cada uno está **en español** («miel», «sirope de arce»). Es un examen de
inglés para un jugador hispano. En la versión inglesa, si la nota se traduce al inglés, queda "honey" = "honey"
y el reto desaparece.
- **Recomendado:** en `tl/english`, las notas pasan a **japonés en romaji** ("hachimitsu", "mēpuru shiroppu"…).
  Encaja con la historia (instituto japonés, clase de inglés) y mantiene el reto de emparejar.
- Alternativa: dejar las notas en español (más fácil, pero raro para un jugador inglés).
- Alternativa: describirlas ("made by bees") — más trabajo y cambia la dificultad.

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

## 10. Dudas abiertas para Adrian

1. **[DECIDIR] Honoríficos:** A (sin honoríficos, recomendada) o B (-kun/-san/-chan). Ver §3.
2. **[DECIDIR] «hermanito»:** "big bro" (recomendado) u "Onii-chan".
3. **[DECIDIR] Minijuego de Nino:** notas en romaji (recomendado), en español, o descripciones. Ver §8.
4. **[DECIDIR] «jajaja» en el chat:** "hahaha" (recomendado) o "lol".
5. **[DECIDIR] Formato de números en la interfaz:** el español usa coma decimal y punto de miles; en inglés es al
   revés. Si algún texto de pantalla construye números con formato, se revisa en la tarea D.
