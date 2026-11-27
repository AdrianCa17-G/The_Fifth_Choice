# Revisión de naturalidad de diálogos · v1.1

Auditoría por tandas. Los números de línea son los de antes de aplicar cada tanda. **No se edita ningún `.rpy` hasta que la línea esté aprobada.** Cada cambio en español
cambia el id de traducción de Ren'Py y deja huérfana la línea inglesa, así que lo aprobado se aplica en una
sola pasada con el mismo proceso que las erratas de E2 (aplicar → regenerar → volver a enlazar el inglés).

## Reglas

QUÉ BUSCAR (conteos aproximados en todo el Prólogo + Cap. 1)
1. "como quien ..." (~29). Objetivo: como máximo 1 por archivo. Hay frases duplicadas entre archivos,
   como "Lo dijo despacio, como quien termina una cuenta" (Miku y beat_casa).
2. Narrador que empieza con "Lo dijo..." (~65), sobre todo el molde "No lo dijo con X. Lo dijo como quien Y".
   Muchas se pueden borrar: si el diálogo ya transmite el tono, la acotación sobra.
3. "Es distinto" / "y eso es distinto" usado como remate (~10, en varios personajes y en el MC).
   Objetivo: como mucho uno en todo el capítulo, y solo si funciona como chiste o callback.
4. El contraste "No era X. Era Y." / "No fue X. Fue Y." / "No es que X. Es que Y.".
5. Exceso de "como si" (~73), "casi" (~52), "por primera vez" (~16), "No dije nada" (~14) y "en silencio" (~14).
   No hay que eliminarlos: solo reducir los que estén amontonados o repetidos cerca.
6. Líneas de las chicas demasiado poéticas o sentenciosas: aforismos, metáforas elaboradas,
   remates redondos al final de cada intercambio. Hay que hacerlas más directas y coloquiales,
   con interrupciones, muletillas humanas ("eh", "o sea", "bueno...") y frases a medias.
7. Pensamientos del MC que explican la emoción en vez de dejar que se note
   ("Y eso dolía mucho más que un grito"). Proponer cortarlos o hacerlos más secos.

REGLAS PARA LAS PROPUESTAS
- Si una línea suena natural, no se toca, aunque contenga una palabra de la lista.
- Respetar la voz que ya tiene cada personaje en el archivo; no homogeneizar.
  La rama fría sigue siendo el MC del día 1, distante pero nunca cruel.
- Máximo ~100 caracteres por línea (dos líneas de la caja de texto).
- No introducir muletillas nuevas ("de alguna manera", "algo en su mirada", "por un instante",
  "y ahí lo entendí", etc.).
- Misma información, mismo orden, mismas ramas. Proponer "BORRAR" está permitido si la línea sobra.
- Ortografía española correcta (¿?, ¡!, tildes), pero registro hablado.

**Formato de ID:** `<archivo>-<nn>` (ICH = Ichika, ITS = Itsuki, MIK = Miku, NIN = Nino, YOT = Yotsuba,
APE = apertura, CON = conexiones, E6 = evento6, FM = final_malo, BC/BI/BN = beats, PRO = prólogo,
HOR = horarios). Las líneas son de `The Fifth Choice/game/` a fecha 27/11/2026 (v1.1, commit 4cdceae).
En **aprobado** se marca ✅, ❌ o se escribe la versión corregida.

## 02_cap1_Ichika.rpy

Conteo en el archivo: «como quien» 0 · «Lo dijo» (narrador) 6 · «como si» 6 · «casi» 3 · «sin exclamación» 2 (+1
«no vino con exclamación») · «sin (la) actuación» 3 · «guardó / guardar» 8. Pasan de 6 a 2 los «Lo dijo» y de
8 a 5 los «guardar», sin tocar el motivo (Ichika guarda todo) en las líneas 566 y 375/427/471.

| ID | línea | personaje | texto actual | problema (n.º) | propuesta | aprobado |
|---|---|---|---|---|---|---|
| ICH-01 | 103 | narrador | Me preguntó sin actuación, sin la voz que usa para todo. | 2, 7 (111-119 ya dicen que la voz suena plana) | BORRAR | ✅ aplicado 27/11 |
| ICH-02 | 176 | narrador | Lo dijo con una sonrisa, pero cambió de tema otra vez, y esta ya era la segunda. | 2 | Sonrió. Y volvió a cambiar de tema. Ya iban dos. | ✅ aplicado 27/11 |
| ICH-03 | 205 | mc | Lo dijiste de corrido, sin titubear, como si ya tuvieras la cuenta hecha en la cabeza. | 5 (el MC habla como narrador) | Lo dijiste de corrido. Ya tenías la cuenta hecha. | ✅ aplicado 27/11 |
| ICH-04 | 330 | narrador | Lo dijo sin exclamación. | 2 (repite la 111) | BORRAR | ✅ aplicado 27/11 |
| ICH-05 | 332 | narrador | La primera frase larga de toda la tarde sin una sola. | 2 (depende de la 330; además «Fingir que puedo con las dos» no es una frase larga) | BORRAR | ✅ aplicado 27/11 |
| ICH-06 | 338 | ichika | Yo también me lo digo, y no me lo creo ni cuando lo digo yo. | 6 | Me lo digo yo sola todo el tiempo. Y ni yo me lo creo. | ✅ aplicado 27/11 |
| ICH-07 | 355 | ichika | ¿No vas a decir nada aprovechado sobre esto? | 6 («aprovechado» no suena hablado) | ¿No vas a decir nada sobre esto? | ✅ aplicado 27/11 |
| ICH-08 | 377 | mc_pensamiento | Volvió la sonrisa. Pero tardó, y no vino con exclamación. | 5 (tercera «exclamación»), 7 | Volvió a sonreír. Pero le costó. | ✅ aplicado 27/11 |
| ICH-09 | 461 | narrador | Lo dijo con la voz más parecida a la de un adulto que le hubiera oído usar. | 2 | Fue la voz más adulta que le había oído. | ✅ aplicado 27/11 |
| ICH-10 | 481 | mc_pensamiento | No fue grosera. Fue correcta. | 4 | No fue grosera. Solo... correcta. | ✅ aplicado 27/11 |
| ICH-11 | 483 | mc_pensamiento | Y eso, viniendo de ella, es peor que un portazo. | 7 (el mismo molde que «dolía más que un grito») | BORRAR | ✅ aplicado 27/11 |
| ICH-12 | 500 | narrador | Terminó de guardar el guion en la mochila cuando el teléfono le vibró en el bolsillo. | 5 (las tres ramas acaban de guardar el guion) | Se estaba colgando la mochila cuando le vibró el teléfono en el bolsillo. | ✅ aplicado 27/11 |
| ICH-13 | 507 | narrador | Pero en cuanto vio la pantalla, algo en su postura cambió. | muletilla vetada («algo en su») | Pero al ver la pantalla, se enderezó. | ✅ aplicado 27/11 |
| ICH-14 | 548 | ichika | Esa que dice que vas a sumar otra cosa a la lista de preguntas que no me vas a hacer. | 6 | Esa. La de «otra cosa más que no te voy a preguntar». | ✅ aplicado 27/11 |
| ICH-15 | 554 | narrador | Lo dijo casi riendo, y por un segundo volvió a ser la de siempre. | 2, 5, muletilla («por un segundo») | Se le escapó una risa. Esa sí era la de siempre. | ✅ aplicado 27/11 |
| ICH-16 | 559 | ichika | Contestaré luego. Ahora tengo que acompañarte a la salida antes de que cierren el edificio. | 6 (futuro formal, 92 car.) | Luego contesto. Ahora te acompaño a la salida, que van a cerrar el edificio. | ✅ aplicado 27/11 |
| ICH-17 | 568 | narrador | Guardó el teléfono en el bolsillo de la falda. | 5 (la 566 ya dice «Solo lo guardó») | BORRAR | ✅ aplicado 27/11 |
| ICH-18 | 570 | narrador | Con el mismo movimiento con el que había guardado el guion. | 5, 7 (explica el paralelo que la 566 ya marca) | BORRAR | ✅ aplicado 27/11 |
| ICH-19 | 609 | mc_pensamiento | Como si admitir que no puede con todo no cambiara en nada lo que va a seguir haciendo mañana. | 5, 7 | Admitirlo no le cambió nada. Mañana va a seguir igual. | ✅ aplicado 27/11 |
| ICH-20 | 621 | mc_pensamiento | Siento como si no hubiera hecho nada para ayudarla. | 7 (la 617 y la 619 ya lo dicen) | No la ayudé en nada. | ✅ aplicado 27/11 |
| ICH-21 | 637 | mc_pensamiento | Como si hoy solo le hubiera enseñado a esconder mejor la cuenta. | 5, 7 | Hoy solo le enseñé a esconder mejor la cuenta. | ✅ aplicado 27/11 |
| ICH-22 | 639 | mc_pensamiento | No a hacerla más corta. | 6 (remate redondo; la 637 ya lo transmite) | BORRAR | ✅ aplicado 27/11 |

### Se dejan como están (a propósito)

- **111-119** («Lo dijo plano. Sin exclamación.» / «Su voz normal tiene dirección de escena.»): es la primera vez
  que se ve su voz sin actuar y la imagen teatral es de Ichika. Al borrar la 103 y la 330 queda una sola vez.
- **157-159** («...casi no lo noto. / Casi.»): funciona como chiste.
- **224-226**, **475-477**, **379**: son la voz analítica del MC y no se repiten.
- **592-594** «Una de cinco. Y esta...»: los cinco hubs cierran igual (Itsuki 516, Miku 579, Nino 581,
  Yotsuba 614). Parece un callback a propósito, así que no se toca aquí. Si se quiere variar, hay que decidirlo
  para los cinco a la vez.

### Notas de coherencia (aprobadas y aplicadas el 27/11 con las propuestas de abajo)

- **265** «Tres cosas que acabo de ver...» contradice la 216-226, que enumera cuatro («Cuatro ya son un patrón»).
  Propuesta: «Cuatro cosas, y un chiste encima de cada una.»
- **479** (rama fría) dice que Ichika *sale primero* sosteniendo la puerta, pero en el movimiento 5 sigue en la
  sala guardando cosas y dice «tengo que acompañarte a la salida». Al cierre, la 633 vuelve a hablar de la puerta.
  Propuesta mínima para la 479: «Fue hasta la puerta antes que yo y me esperó ahí, sin mirarme.»
  (Sin esto, «Sostuvo la puerta el tiempo justo» en la 633 se refiere a una salida que no ocurre después.)

## Horarios en números (todos los archivos)

En la encuesta dicen que los horarios en letras confunden, sobre todo la cuenta de trenes de Ichika
(«las cuatro treinta y cinco... el tren de las cuatro cuarenta y cinco») y su eco en el Evento 6. No hay ningún
arreglo ni lista que genere estas horas: están escritas a mano en cada línea, así que el cambio es línea por
línea, en español **y** en inglés (el inglés también las tiene en letras).

Criterio: hora del reloj → cifras (`4:35`, `a las 3`). Las horas en punto van sin «:00» («a las 4 en punto»).
Las duraciones («veinticinco», «media hora», «hora y media») se quedan en letras.

**No se cambia:** `02_cap1_evento6.rpy:3097-3099` («Cinco. Departamento.» / «Cinco: la hora. O la cuenta.»). El
chiste es justamente que el «cinco» del mensaje de Maruo es ambiguo, y con «5» se pierde.

| ID | archivo:línea | texto actual (ES) | propuesta (ES) | propuesta (EN) | aprobado |
|---|---|---|---|---|---|
| HOR-01 | 01_prologo:155 | ...Anoche también te escuché pasar páginas a las tres. | ...Anoche también te escuché pasar páginas a las 3. | ...I heard you turning pages at 3 last night, too. | ✅ aplicado 27/11 |
| HOR-02 | 01_prologo:1282 | Salí del edificio pasadas las nueve. La ciudad... | Salí del edificio pasadas las 9. La ciudad... | I left the building past 9. The city... | ✅ aplicado 27/11 |
| HOR-03 | 01_prologo:1296 | Son más de las nueve, Raiha. | Son más de las 9, Raiha. | It's after 9, Raiha. | ✅ aplicado 27/11 |
| HOR-04 | apertura:65 | ...a las siete y media de la mañana. | ...a las 7:30 de la mañana. | ...at 7:30 in the morning. | ✅ aplicado 27/11 |
| HOR-05 | apertura:134 | Era que iba a odiarme desde las ocho hasta las tres. | Era que iba a odiarme desde las 8 hasta las 3. | ...hate me from 8 to 3. | ✅ aplicado 27/11 |
| HOR-06 | apertura:136 | Y después, desde las cuatro hasta que me fuera de su casa. | Y después, desde las 4 hasta que me fuera de su casa. | And then, from 4 until I left her house. | ✅ aplicado 27/11 |
| HOR-07 | apertura:158 | Toqué a las cuatro en punto. | Toqué a las 4 en punto. | I knocked at 4 on the dot. | ✅ aplicado 27/11 |
| HOR-08 | apertura:496 | Salí del edificio pasadas las siete. Fui directo a casa. | Salí del edificio pasadas las 7. Fui directo a casa. | I left the building after 7. I went straight home. | ✅ aplicado 27/11 |
| HOR-09 | Ichika:105 | Las cuatro y media. | Las 4:30. | 4:30. | ✅ aplicado 27/11 |
| HOR-10 | Ichika:191 | Martes a las cinco y veinte. Nunca antes de eso. | Martes a las 5:20. Nunca antes de eso. | Tuesday at 5:20. Never before that. | ✅ aplicado 27/11 |
| HOR-11 | Ichika:193 | ¿Por qué no a las cinco? Es más redondo. | ¿Por qué no a las 5? Es más redondo. | Why not 5? It's a rounder number. | ✅ aplicado 27/11 |
| HOR-12 | Ichika:195 | Salgo del ensayo a las cuatro treinta y cinco. Cuatro minutos para cambiarme. | Salgo del ensayo a las 4:35. Cuatro minutos para cambiarme. | Rehearsal ends at 4:35. Four minutes to change. | ✅ aplicado 27/11 |
| HOR-13 | Ichika:197 | Seis hasta la estación. El tren de las cuatro cuarenta y cinco tarda veinticinco. | Seis hasta la estación. El tren de las 4:45 tarda veinticinco. | Six to the station. The 4:45 train takes twenty-five. | ✅ aplicado 27/11 |
| HOR-14 | Ichika:199 | Y diez andando hasta casa. Cinco y veinte. | Y diez andando hasta casa. Las 5:20. | And ten more on foot to get home. 5:20. | ✅ aplicado 27/11 |
| HOR-15 | Itsuki:120 | Me incumbe a mí. Tú te vas a las cuatro. | Me incumbe a mí. Tú te vas a las 4. | It's my business. You go home at 4. | ✅ aplicado 27/11 |
| HOR-16 | Itsuki:122 | Son las cuatro y media. | Son las 4:30. | It's 4:30. | ✅ aplicado 27/11 |
| HOR-17 | Miku:209 | ...Me quedé dormido a las tres. | ...Me quedé dormido a las 3. | ...Fell asleep at 3. | ✅ aplicado 27/11 |
| HOR-18 | beat_Nino:435 | Hay que hacer la cena. Son las cinco. | Hay que hacer la cena. Son las 5. | Dinner needs making. It's 5 o'clock. | ✅ aplicado 27/11 |
| HOR-19 | beat_casa:264 | Me encerré en mi cuarto antes de las diez. | Me encerré en mi cuarto antes de las 10. | I shut myself in my room before 10. | ✅ aplicado 27/11 |
| HOR-20 | conexiones:2581 | Pasadas las once, me sonó el teléfono... | Pasadas las 11, me sonó el teléfono... | A little after 11, my phone rang... | ✅ aplicado 27/11 |
| HOR-21 | conexiones:2623 | Me llamó desde un hospital, a las once, para preguntar... | Me llamó desde un hospital, a las 11, para preguntar... | ...from a hospital, at 11, to ask... | ✅ aplicado 27/11 |
| HOR-22 | conexiones:3824 / 3862 / 3896 | Terminamos pasadas las seis. ... (×3, una por clima) | Terminamos pasadas las 6. ... | We finished a little after 6. ... | ✅ aplicado 27/11 |
| HOR-23 | conexiones:4046 | Pasadas las ocho salí del departamento... | Pasadas las 8 salí del departamento... | After 8 I left the apartment... | ✅ aplicado 27/11 |
| HOR-24 | evento6:883 | Pregunta cuatro. Un tren sale a las cuatro cuarenta y cinco. | Pregunta cuatro. Un tren sale a las 4:45. | Question four. A train leaves at 4:45. | ✅ aplicado 27/11 |
| HOR-25 | evento6:885 | ...Hay que salir a las cuatro treinta y cinco. | ...Hay que salir a las 4:35. | ...Have to leave at 4:35. | ✅ aplicado 27/11 |
| HOR-26 | evento6:924 | Pregunta cuatro. Trenes. Salen las cuatro treinta y cinco. | Pregunta cuatro. Trenes. Salen las 4:35. | Question four. Trains. Leave at 4:35. | ✅ aplicado 27/11 |
| HOR-27 | evento6:947 | Pregunta cuatro. Trenes. Cuatro treinta y cinco. | Pregunta cuatro. Trenes. 4:35. | Question four. Trains. 4:35. | ✅ aplicado 27/11 |
| HOR-28 | evento6:966 | Pregunta cuatro. Trenes. Cuatro treinta y cinco. Sale sola. | Pregunta cuatro. Trenes. 4:35. Sale sola. | Question four. Trains. 4:35. It comes out on its own. | ✅ aplicado 27/11 |

Notas:
- HOR-10 a HOR-14 y HOR-24 a HOR-28 van juntas: el Evento 6 repite la cuenta del hub de Ichika y tienen que
  verse igual. La cuenta cuadra (4:35 + 4 + 6 = 4:45; + 25 + 10 = 5:20).
- «Pregunta cuatro» se deja en letras porque es el número de la pregunta, no una hora.
- Al aplicarlo, `tools/revisar_traduccion.py` compara las etiquetas, no los números; conviene buscar `[0-9]:[0-9]`
  en `tl/english` después de regenerar para confirmar que no quedó ninguna hora en letras.

## 02_cap1_Itsuki.rpy

Los horarios de este archivo ya se aplicaron (HOR-15 y HOR-16). Itsuki casi no se toca: sus frases son cortas y
suenan a ella. El problema está en la narración y los pensamientos del MC: «como quien» 2 (pasa a 0) y cinco
contrastes «No es X. Es Y.» seguidos (quedan 1: la revelación de las líneas 185-187).

| ID | línea | personaje | texto actual | problema (n.º) | propuesta | aprobado |
|---|---|---|---|---|---|---|
| ITS-01 | 132 | mc_pensamiento | Eso no es no saber. | 4 | BORRAR | ✅ aplicado 27/11 |
| ITS-02 | 134 | mc_pensamiento | Eso es equivocarse siempre en el mismo sitio sin encontrarlo. | 4 (va con ITS-01) | Se equivoca siempre en el mismo sitio y no lo encuentra. | ✅ aplicado 27/11 |
| ITS-03 | 146 | narrador | Y eso fue lo que la delató. | 7 (la 148-156 ya lo explica) | BORRAR | ✅ aplicado 27/11 |
| ITS-04 | 158 | mc_pensamiento | No está pensando. Está esperando a que el error se corrija solo. | 4 | Está esperando a que el error se corrija solo. | ✅ aplicado 27/11 |
| ITS-05 | 173 | narrador | Eso sí le tocó algo. | 7 | BORRAR | ✅ aplicado 27/11 |
| ITS-06 | 175 | narrador | Lo dijo rápido. Más rápido que el resto de la conversación. | 2 | Lo soltó mucho más rápido que todo lo demás. | ✅ aplicado 27/11 |
| ITS-07 | 177 | narrador | Como quien suelta algo antes de poder impedírselo. | 1 | BORRAR | ✅ aplicado 27/11 |
| ITS-08 | 189 | mc_pensamiento | Y esa es la única excusa que no tiene guardada. | 6, 7 (repite lo que Itsuki dice en 169-171) | BORRAR | ✅ aplicado 27/11 |
| ITS-09 | 193 | narrador | La postura no había cambiado, pero algo en los hombros sí. | muletilla vetada («algo en») | Seguía sentada igual, pero se le cayeron los hombros. | ✅ aplicado 27/11 |
| ITS-10 | 210 | mc_pensamiento | Sería darme la razón sobre por qué estoy como su tutor. | frase enredada | Sería admitir que sí necesita un tutor. | ✅ aplicado 27/11 |
| ITS-11 | 243 | mc_pensamiento | No es que no sepa resolverlo. | 4 | BORRAR | ✅ aplicado 27/11 |
| ITS-12 | 245 | mc_pensamiento | Es que no está revisando desde el principio. | 4 | Sabe resolverlo. Solo que no revisa desde el principio. | ✅ aplicado 27/11 |
| ITS-13 | 247 | mc_pensamiento | Está corrigiendo el final y arrastrando el error del medio sin tocarlo. | 5 | Corrige el final y arrastra el error del medio. | ✅ aplicado 27/11 |
| ITS-14 | 270 | mc_pensamiento | Lo difícil no es el ejercicio. Es cómo decírselo. | 4 | Lo difícil va a ser decírselo. | ✅ aplicado 27/11 |
| ITS-15 | 356 | narrador | No lo dijo como un triunfo. | 2 | BORRAR | ✅ aplicado 27/11 |
| ITS-16 | 358 | narrador | Lo dijo como quien reporta un dato, todavía sin mirarme. | 1, 2 | Sonó a dato, no a triunfo. Seguía sin mirarme. | ✅ aplicado 27/11 |
| ITS-17 | 378 | narrador | Pero sin pedirme que me fuera tampoco. | 5 (repite la 339 y la 524) | BORRAR | ✅ aplicado 27/11 |
| ITS-18 | 469 | narrador | Lo dijo sin agradecerlo y sin discutirlo. | 2 | Ni me dio las gracias ni discutió. | ✅ aplicado 27/11 |
| ITS-19 | 471 | narrador | En ella, esa es la forma más fría de aceptar algo. | 6, 7 | BORRAR | ✅ aplicado 27/11 |
| ITS-20 | 479 | mc_pensamiento | No era el ejercicio. | 4 | BORRAR | ✅ aplicado 27/11 |
| ITS-21 | 481 | mc_pensamiento | Era hacerlo ella sola. | 4 (va con ITS-20) | Hacerlo ella sola. | ✅ aplicado 27/11 |
| ITS-22 | 526 | mc_pensamiento | Con ella empiezo a entender que eso cuenta más que un gracias. | 7 | Con ella, eso cuenta más que un gracias. | ✅ aplicado 27/11 |

### Notas de coherencia (para aprobar aparte)

| ID | línea | personaje | texto actual | problema | propuesta | aprobado |
|---|---|---|---|---|---|---|
| ITS-23 | 144 | narrador | Lo repitió exactamente igual, palabra por palabra. | las líneas 138 y 142 no son iguales | Me contestó casi con las mismas palabras. | ✅ aplicado 27/11 |
| ITS-24 | 237 | narrador | El segundo paso tiene mal la conversión de unidades. | presente en una narración en pasado | El segundo paso tenía mal la conversión de unidades. | ✅ aplicado 27/11 |

## 02_cap1_Miku.rpy

El horario de este archivo ya se aplicó (HOR-17). El relato de Miku sobre la sal no se toca: suena a ella.
«como quien» pasa de 2 a 1 (queda la 496). La frase duplicada de la 435 sigue en `beat_casa`; se revisa en su tanda.

| ID | línea | personaje | texto actual | problema (n.º) | propuesta | aprobado |
|---|---|---|---|---|---|---|
| MIK-01 | 104 | narrador | Algo se le movió en la cara al oír eso, tan rápido que no me dio tiempo a leerlo. | muletilla («algo») | Puso una cara rara al oírlo, tan rápido que no me dio tiempo a leerla. | ✅ aplicado 27/11 |
| MIK-02 | 172 | mc_pensamiento | No es que no sepa. | 4 | BORRAR | ✅ aplicado 27/11 |
| MIK-03 | 174 | mc_pensamiento | Es que no piensa hablar de nada que le importe delante de alguien que va a calificarla. | 4 | Sí sabe. Pero no va a hablar de lo que le importa con alguien que la va a calificar. | ✅ aplicado 27/11 |
| MIK-04 | 226 | mc_pensamiento | Era la primera vez que dejaba de mirar a otro lado. | 5 | Por fin dejó de mirar a otro lado. | ✅ aplicado 27/11 |
| MIK-05 | 320 | narrador | Creo que se oyó. | 7 (repite la 322) | BORRAR | ✅ aplicado 27/11 |
| MIK-06 | 322 | narrador | Fue eso: se oyó a sí misma hablando en voz alta durante un minuto entero. | 7 | Se había oído: llevaba un minuto entero hablando en voz alta. | ✅ aplicado 27/11 |
| MIK-07 | 352 | mc_pensamiento | Nadie le enseñó a callarse. Se lo fueron enseñando las caras de los demás. | 6, 7 | A callarse no la mandó nadie. Lo aprendió viendo las caras de la gente. | ✅ aplicado 27/11 |
| MIK-08 | 407 | narrador | Se detuvo otra vez. Pero esta vez se detuvo distinto. | 3 | Se detuvo otra vez. | ✅ aplicado 27/11 |
| MIK-09 | 409 | narrador | Se detuvo mirándome a mí, no al libro. | 3 (va con MIK-08) | Pero ahora me miraba a mí, no al libro. | ✅ aplicado 27/11 |
| MIK-10 | 419 | narrador | No dijo nada. Se le puso el libro a media altura, sin llegar a subirlo del todo. | 5 | El libro se le quedó a media altura, sin llegar a subir del todo. | ✅ aplicado 27/11 |
| MIK-11 | 435 | narrador | Lo dijo despacio, como quien termina una cuenta. | 1, 2 (duplicada en beat_casa) | BORRAR | ✅ aplicado 27/11 |
| MIK-12 | 437 | mc_pensamiento | Ahí estaba lo que acababa de entender. | 7 | Ahí lo había entendido ella. | ✅ aplicado 27/11 |
| MIK-13 | 439 | mc_pensamiento | No que yo supiera de esto. | 4 | Le daba igual que yo supiera del tema. | ✅ aplicado 27/11 |
| MIK-14 | 441 | mc_pensamiento | Justo lo contrario: que no sabía nada, y que aun así me había pasado la noche en ello. | 4, 7 | Lo que le llegó es que, sin saber nada, me pasé la noche leyéndolo. | ✅ aplicado 27/11 |
| MIK-15 | 524 | narrador | Asintió una vez, muy despacio, como si le hubieran confirmado algo que ya sospechaba. | 5, muletilla («algo») | Asintió una vez, muy despacio. Eso ya se lo esperaba. | ✅ aplicado 27/11 |

### Notas de coherencia (para aprobar aparte)

| ID | línea | personaje | texto actual | problema | propuesta | aprobado |
|---|---|---|---|---|---|---|
| MIK-16 | 116 | narrador | No pareció convencerle del todo, pero tampoco se levantó. | gramática: el sujeto es Miku | No parecía convencida del todo, pero tampoco se levantó. | ✅ aplicado 27/11 |

### Se dejan como están (a propósito)

- **64-66** «Así no se estudia. / Así se lee.» y **154** «Un muro de ladrillo, pero educado.»: son la voz del MC.
- **496** «como quien cierra una puerta con educación»: es el único «como quien» del archivo.
- **586-588** «Miku no es callada. / Está callada, que no es lo mismo.»: la distinción es la idea de la ruta.

## 02_cap1_Nino.rpy

Las réplicas de Nino son cortas y cortantes, y no se tocan. «como quien» pasa de 2 a 1 (queda la 297),
«como si» de 6 a 3 y «por primera vez» del MC de 2 a 0.

| ID | línea | personaje | texto actual | problema (n.º) | propuesta | aprobado |
|---|---|---|---|---|---|---|
| NIN-01 | 53 | narrador | El resto de la sección estaba vacío. | repite la 51 | BORRAR | ✅ aplicado 27/11 |
| NIN-02 | 71 | narrador | La encontré por descarte, no porque alguien me lo dijera. | 4 | La encontré por descarte. | ✅ aplicado 27/11 |
| NIN-03 | 84 | mc_pensamiento | No estaba traduciendo con esfuerzo. | 4 | BORRAR | ✅ aplicado 27/11 |
| NIN-04 | 86 | mc_pensamiento | Estaba leyendo, directo, como quien no necesita traducir nada. | 1, 4 | Estaba leyendo de corrido, sin traducir nada. | ✅ aplicado 27/11 |
| NIN-05 | 146 | narrador | Como si me hubiera acercado a un terreno prohibido. | 5, 6 | BORRAR | ✅ aplicado 27/11 |
| NIN-06 | 154 | narrador | Lo dijo cortante, cerrando el tema de un golpe. | 2 | BORRAR | ✅ aplicado 27/11 |
| NIN-07 | 174 | narrador | Lo leyó sin pausa, sin buscar la palabra, como si estuviera leyendo en japonés. | 5 | Lo leyó de corrido, sin pensarse ni una palabra. | ✅ aplicado 27/11 |
| NIN-08 | 182 | narrador | Lo dijo bien. | 2 | Y lo pronunció bien. | ✅ aplicado 27/11 |
| NIN-09 | 254 | mc_pensamiento | No está hablando de mí. | 4 | BORRAR | ✅ aplicado 27/11 |
| NIN-10 | 256 | mc_pensamiento | Está hablando de todos los que vinieron antes. | 4 (va con NIN-09) | Habla de todos los que vinieron antes. | ✅ aplicado 27/11 |
| NIN-11 | 274 | mc_pensamiento | No está protegiéndose a ella. | 4 | BORRAR | ✅ aplicado 27/11 |
| NIN-12 | 276 | mc_pensamiento | Está protegiendo a sus hermanas de algo que ya les pasó demasiadas veces. | 4 (va con NIN-11) | Más que a ella, cuida a sus hermanas de algo que ya les pasó demasiadas veces. | ✅ aplicado 27/11 |
| NIN-13 | 293 | narrador | Ahí estaba el «olvídalo». Tarde, como le llega siempre que habla de más. | 6 | Ahí estaba el «olvídalo». Llegó tarde. | ✅ aplicado 27/11 |
| NIN-14 | 301 | narrador | Se acomodó el uniforme, como si con eso pudiera acomodar también lo que acababa de decir. | 5, 6 | Se acomodó el uniforme y no volvió sobre el tema. | ✅ aplicado 27/11 |
| NIN-15 | 363 | narrador | Se quedó quieta, con la cesta a medio subir, como si esperara el resto de la frase que no llegó. | 5 | Se quedó con la cesta a medio subir, esperando el resto de la frase. | ✅ aplicado 27/11 |
| NIN-16 | 376 | narrador | Lo pensó un momento, sin la hostilidad de antes ni la calma que tampoco tiene. | 6 | Lo pensó un momento. Ya sin tanta hostilidad. | ✅ aplicado 27/11 |
| NIN-17 | 467 | mc_pensamiento | A veces el silencio es lo único que se puede compartir. | 6, 7 | BORRAR | ✅ aplicado 27/11 |
| NIN-18 | 562 | mc_pensamiento | Y por primera vez, no sonó a que me odiara. | 5 | Y esta vez no sonó a que me odiara. | ✅ aplicado 27/11 |
| NIN-19 | 591 | mc_pensamiento | Pero por primera vez no me trató como al siguiente de la fila. | 5 | Pero ya no me trató como al siguiente de la fila. | ✅ aplicado 27/11 |

### Notas de coherencia (para aprobar aparte)

| ID | línea | personaje | texto actual | problema | propuesta | aprobado |
|---|---|---|---|---|---|---|
| NIN-20 | 387 | narrador | Se quedó mirando la tarjeta de receta un segundo más, antes de guardarla del todo. | la 295 ya la guardó en el bolsillo | Se quedó un segundo con la mano sobre el bolsillo de la tarjeta. | ✅ aplicado 27/11 |
| NIN-21 | 394 | mc | No dije nada de más. | quien «habló de más» fue Nino | No dijiste nada de más. | ✅ aplicado 27/11 |
| NIN-22 | 514 | narrador | Caminó hacia la caja sin esperarme, ocultando el papel antes de que pudiera ver algo más. | la tarjeta ya estaba guardada | Caminó hacia la caja sin esperarme, con una mano sobre el bolsillo. | ✅ aplicado 27/11 |

## 02_cap1_Yotsuba.rpy

Las réplicas de Yotsuba (exclamaciones, «¡Equipo completo!») suenan a ella y no se tocan. «como quien / de quien»
pasa de 2 a 1 (queda la 529) y «como si» de 6 a 2 (289 y 305).

| ID | línea | personaje | texto actual | problema (n.º) | propuesta | aprobado |
|---|---|---|---|---|---|---|
| YOT-01 | 151 | narrador | Como si acabara de darse cuenta de que alguien la estaba viendo. | 5 | Acababa de darse cuenta de que alguien la miraba. | ✅ aplicado 27/11 |
| YOT-02 | 167 | narrador | Luego asintió con la solemnidad de quien acaba de recordar algo obvio. | 1 | Luego asintió, muy solemne. | ✅ aplicado 27/11 |
| YOT-03 | 173 | narrador | La pregunta la pilló sin la exclamación preparada. | 6 | Esa pregunta no la vio venir. | ✅ aplicado 27/11 |
| YOT-04 | 201 | narrador | Algo cambió en la forma en que se apoyó en la valla. | muletilla («algo») | Se reacomodó contra la valla. | ✅ aplicado 27/11 |
| YOT-05 | 237 | mc_pensamiento | Como si destrozarse el cuerpo en esa pista fuera un precio justo por sentirse útil. | 5 | Y destrozarse en esa pista le parece un precio justo por sentirse útil. | ✅ aplicado 27/11 |
| YOT-06 | 266 | narrador | Como si así pudiera sacudirse también lo que acababa de decir. | 5, 6 | BORRAR | ✅ aplicado 27/11 |
| YOT-07 | 385 | narrador | Hubo un breve silencio. | 5 (va con YOT-08) | BORRAR | ✅ aplicado 27/11 |
| YOT-08 | 387 | narrador | Un silencio de una Yotsuba que está comprobando si todo eso fue verdad. | 6 | Se quedó callada, repasando si todo eso era verdad. | ✅ aplicado 27/11 |
| YOT-09 | 415 | narrador | No dijo nada. Miraba la pista, pero no la pista de verdad. | 4, 6 | No dijo nada. Miraba la pista sin verla. | ✅ aplicado 27/11 |
| YOT-10 | 593 | mc_pensamiento | Solo volvió a correr, como si la conversación nunca hubiera interrumpido nada. | 5 | Solo siguió corriendo. | ✅ aplicado 27/11 |

### Notas de coherencia (para aprobar aparte)

| ID | línea | personaje | texto actual | problema | propuesta | aprobado |
|---|---|---|---|---|---|---|
| YOT-11 | 450 | narrador | Ya no se gritaba ánimos. Ahora la cuenta la llevábamos entre dos. | gramática | Ya no se gritaba ánimos a sí misma. La cuenta la llevábamos entre dos. | ✅ aplicado 27/11 |

### Cifras que se comparan (27/11, a pedido tuyo) · ✅ aplicado

Números solo donde se comparan: tiempos del cronómetro (`1:17`, `1:14`) y «25 → 30», en Yotsuba, beat_casa,
conexiones y Evento 6. Las vueltas contadas en voz alta y las duraciones siguen en letras.

## 02_cap1_apertura.rpy

Los horarios ya se aplicaron (HOR-04 a HOR-08). Los diálogos suenan naturales y casi no se tocan. Quedan dos
contrastes «No es que X. Es que Y.» con peso (255-257 y 891-893). No toqué las líneas partidas en dos renglones.

| ID | línea | personaje | texto actual | problema (n.º) | propuesta | aprobado |
|---|---|---|---|---|---|---|
| APE-01 | 122 | mc_pensamiento | (Aunque el silencio, viniendo de ella, se siente casi más pesado que los gritos.) | 6, 7 | (Aunque, viniendo de ella, casi prefiero que me grite.) | ✅ aplicado 27/11 |
| APE-02 | 130 | mc_pensamiento | Ahí estaba lo verdaderamente incómodo del asunto. | 7 | BORRAR | ✅ aplicado 27/11 |
| APE-03 | 287 | mc_pensamiento | No querían echarme a gritos. Querían mi carta de renuncia. | 4 | Nada de echarme a gritos: querían mi carta de renuncia. | ✅ aplicado 27/11 |
| APE-04 | 326 | mc_pensamiento | Pero está obedeciéndola, que no es lo mismo. | 3 | Pero igual le hace caso. | ✅ aplicado 27/11 |
| APE-05 | 432 | mc_pensamiento | Nadie se disculpa por decir algo cierto, a menos que le hayan enseñado que decirlo cuesta. | 6 | Nadie pide perdón por decir la verdad, salvo que ya le haya salido caro antes. | ✅ aplicado 27/11 |
| APE-06 | 436 | mc_pensamiento | Pero por primera vez me llevaba algo a casa. | 5 | Pero esta vez me llevaba algo a casa. | ✅ aplicado 27/11 |
| APE-07 | 467 | narrador | Me miró un momento más largo de lo que me había mirado el día anterior. | frase enredada | Me miró más rato que el día anterior. | ✅ aplicado 27/11 |
| APE-08 | 479 | narrador | Se fue como se había ido el día anterior, sin subir la voz y sin dejar espacio para contestar. | 5 | Se fue igual que ayer, sin subir la voz y sin dejarme contestar. | ✅ aplicado 27/11 |
| APE-09 | 622 | mc_pensamiento | No es que no puedan. Es que se defienden. | 4 | Sí pueden. Se están defendiendo. | ✅ aplicado 27/11 |
| APE-10 | 776 | mc_pensamiento | Un rincón secreto que sería la biblioteca. | frase enredada | Así que el rincón secreto es la biblioteca. | ✅ aplicado 27/11 |
| APE-11 | 871 | mc_pensamiento | Eso requiere ponerse de acuerdo antes y concordar el error. | 6 («concordar el error») | Para eso hay que ponerse de acuerdo antes, hasta en los errores. | ✅ aplicado 27/11 |

### Notas de coherencia (para aprobar aparte)

| ID | línea | personaje | texto actual | problema | propuesta | aprobado |
|---|---|---|---|---|---|---|
| APE-12 | 419 | narrador | Lo dijo tan bajo que tuve que reconstruirlo un segundo después, cuando ya no estaba. | Miku sigue ahí: habla otra vez en la 423 | Lo dijo tan bajo que tardé un segundo en entenderlo. | ✅ aplicado 27/11 |
| APE-13 | 421 | narrador | Porque en cuanto lo dijo, se dio cuenta de que lo había dicho. | va con APE-12 | Y en cuanto se oyó, se dio cuenta de lo que había dicho. | ✅ aplicado 27/11 |
