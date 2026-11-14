# Revisión de personaje · Yotsuba Nakano · Prólogo + Capítulo 1

> Repo revisado: `AdrianCa17-G/The_Fifth_Choice`, commit `a1561c9` (10/11/2026, «Ichika Final»).
> Los números de línea son de ese commit. Si aplicas cambios de arriba abajo en un mismo archivo,
> las líneas de más abajo se desplazan: guíate por la **línea actual citada**, no por el número.
> No toqué ningún `.rpy`. Nada de esto suma ni resta puntos (ver §7).
> No toco ninguna línea de Ichika, Nino, Miku ni Itsuki. Sí toco líneas del MC y del narrador
> dentro de las escenas de Yotsuba (respuesta 10).

---

## 0. Cómo apliqué tus respuestas

| # | Tu respuesta | Qué hice con ella |
|---|---|---|
| 1 | Nada de la niña de Kioto; el juego es 100 % lineal desde el prólogo | Confirmado: **no hay ni una línea** que lo insinúe y no añado ninguna. Todo lo que Yotsuba siente por el MC nace en pantalla, a partir del día en que corre por el pasillo para conocerlo. |
| 2 | Romance: el que mejor convenga, sin que el fandom la odie | Veredicto completo en §6.5. Resumen: **su defecto (cederlo todo) es el obstáculo de su ruta, no su mérito.** Su romance se gana en pantalla, solo en la cálida, y siempre en su motivo propio: **la cuenta**. Cuatro toques nuevos (R1–R4), ninguno declara nada. |
| 3 | El club sí; no sabes cómo sería su cita del Cap. 2 sin reusar la pista | Propuesta en §6.6: **«Un día sin cuenta»**, en un escenario nuevo, con el club como conflicto. Ahí aparece por primera vez su «no». |
| 4 | Qué debe sentir el jugador: lo que convenga, sin odio | §6.4: **ganas de llevarle la cuenta a ella.** La animadora a la que nadie anima. |
| 5 | Cuenta sola; cuando la ven, se detiene. ¿Está pulido? | **Casi.** Las siete reglas del tic están en §1, y seis ya funcionan. Falla una, y es la importante: en la cálida, el hub termina igual que en la fría (ella deja de gritar), así que las dos ramas se parecen justo donde deberían separarse. P4 lo arregla: en la cálida **sigue contando en voz alta aunque la miren**, porque ahora la cuenta la llevan entre dos. |
| 6 | «Tutor» solo en la fría | El texto ya lo cumple en casi todo (lo comprobé: `tutor` sale en la reacción fría, en la despedida fría del final B, en el prólogo antes de conocerlo y en el nombre del chat). Lo que falla es **al revés**: la Yotsuba fría lo llama por su nombre en varios sitios después de su hub. P2. Y añado un pago: en la mesa del E6, la fría vuelve a decir su nombre por primera vez (N1). |
| 7 | Literatura y Japonés son la misma materia: una sola | **Japonés.** Es el nombre que usan el E6, el final B, `E6_MATERIA` y D-10, y en Japón la asignatura de lengua y literatura se llama así. Solo hay una «Literatura» en todo el juego (hub, l. 409). P11. |
| 8 | Coro del prólogo: lo grita porque lo gritan las demás | Sprite `incomoda` y una línea de narración que reutiliza su propia marca: «medio tono más bajo». P13. |
| 9 | «Ichika duerme poco»: error | Vuelve a «Ichika actúa», igual que en el hub. Así el monólogo tibio del E6 es un eco exacto de su frase de la pista. P14. |
| 10 | Puedo tocar líneas del MC | Toco cuatro: una que adelantaba la cálida antes del menú, el pensamiento que señalaba la respuesta «correcta», el título del menú y la opción fría (P8). |
| 11 | El E6 está desordenado y con bugs; quieres un solo `.rpy` ordenado | **Es lo más grave de esta revisión** (P1), pero no lo resuelvo aquí: es una reorganización de 4 567 líneas que afecta a las cinco hermanas. Te dejo el diagnóstico completo (12 puntos de fallo) y un plan en §8 para hacerlo en una sesión propia. Mis propuestas para el E6 son de contenido y valen igual antes y después de reordenar. |
| Extra | Romance «como con Ichika» | Va en su propia sección (R1–R4 en §4 y §6.5), no repartido por los problemas. |

---

## 1. Ficha del personaje tal como aparece hoy

**Rasgos.**
- **Corredora que entrena sola.** Se queda en la pista media hora después de que el club se va. «El club tiene sus propios objetivos. Yo tengo los míos.»
- **Lee a las personas sin darse cuenta.** Sabe que Nino no durmió, dónde deja Miku su libro y cómo sostiene el lápiz una hermana que no ha dormido. Es su don, y ella no lo cuenta como tal: «Eso que describes no es nada especial. Cualquiera lo haría».
- **La que incluye.** Crea el grupo «¡Equipo Quintillizas + Tutor!», mete a Nino de vuelta tres veces, organiza la foto («¡Hoy es de las cinco!») y es la que le pregunta al MC cómo le fue.
- **Obedece a Nino aunque no esté de acuerdo.** «Yotsuba no está de acuerdo con Nino. Pero está obedeciéndola, que no es lo mismo.» El corte («Yotsuba.» / «…No dije nada») sale tres veces.
- **Culpa fácil.** Pide perdón diez veces el primer día; en los finales malos la culpa es suya («No me digas que no es mi culpa»).

**Voz.**
- Ráfagas cortas con exclamaciones. Habla de sí misma en tercera persona cuando se anima («¡Vamos, Yotsuba!»).
- Vocabulario de atleta: «¡Palabra de atleta!», «Como antes de una carrera», «Equipo completo», «un equipo de relevos», «el testigo».
- **Su marca es el volumen, no la puntuación.** Cuando dice la verdad, baja la voz; el texto lo subraya bien («Yotsuba, que no dice nada bajito»). Ichika usa el mismo recurso con la exclamación, así que conviene que en Yotsuba el narrador hable de **volumen** y en Ichika de **exclamación**. Ajusto dos líneas (P14).
- **El tic de la cuenta (respuesta 5).** Siete reglas; seis ya funcionan:

| # | Regla | Dónde se ve | Estado |
|---|---|---|---|
| 1 | Cuenta en voz alta cuando está sola, y se anima en tercera persona | Hub, Mov. 1 | ✅ |
| 2 | Se calla en cuanto alguien la ve | Hub, «Se paró en seco» | ✅ |
| 3 | **Infla los números cuando algo le duele**: 25 «perfecto», 30 series, 40 vueltas en la fría, «un sesenta es un buen número», «tres vueltas de ventaja» | Hub, reacciones, interc. 6, queja | ✅, salvo la queja, donde no se nota que infla (P9) |
| 4 | Lo apunta en la muñeca: la cuenta es suya y privada | Hub, reacciones, E6 | ✅ |
| 5 | **Cálida: comparte la cuenta.** Le escribe el «1» al MC; en el E6 lo convierte en «100» | Reacción cálida, eco del E6 | ❌ El hub no lo prepara: termina con ella callada, igual que la fría (P4) |
| 6 | **Fría: la cuenta se vuelve interior.** Deja de contar en voz alta; «Hoy no hace falta contar nada» | Hub, reacción, E6 | ✅ |
| 7 | **Contagio**: el MC empieza a contar («once signos de exclamación. Los conté») y Nino también («que no se entere Yotsuba de que llevaba la cuenta») | Interc. 6, E6 | ✅ |

**Deseo.** Que alguien cuente con ella por lo que es y no por lo que hace. Lo dice el E6 cálido: «Yo importo igual que mis hermanas».

**Miedo.** **Sobrar.** Si deja de ser útil (correr, animar), no hay sitio para ella: «Si nadie me necesita, ¿para qué me sobra tanta energía?». Es distinto del miedo de Miku (ser de más cuando habla) y del de Ichika (no tener cara propia). Yotsuba es la única de las tres con la premisa de inferioridad, como querías.

**Con el MC.**
- Confía en él antes de conocerlo: «¡Yo confío en ti al cien por ciento!». Y se le escapa la duda: «…¿Verdad?».
- Intenta defenderlo dos veces delante de Nino y se frena.
- Le pregunta, delante de todas, si elegirá «a la que quiera conocer mejor».
- **Cálida:** él es el primero que nombra su don, y ella le escribe la cuenta en la muñeca.
- **Tibia:** él es su cronometrador; nada más y nada menos.
- **Fría:** él es quien le confirmó que solo sirve para correr, y ella lo llama «tutor».
- **No visitada:** lo esperó quince minutos cada tarde.
- En **todas** las rutas lo mete en el grupo, en el chat y en la foto. Esa inclusión no es romance: es su forma de querer a todo el mundo.

---

## 2. Mapa del arco (orden en que lo vive el jugador)

| # | Momento | Archivo · label · líneas | Condición |
|---|---|---|---|
| 1 | Entra corriendo: «¡Vas a hacerlo genial! …¿Verdad?» (`cg_yotsuba_corriendo`) | `01_prologo.rpy` · `prologo` · 724–763 | Siempre |
| 2 | «¡O sea que ya se conocían!» · el coro «¡No pensamos estudiar!» | `01_prologo.rpy` · 885–1007 | Siempre |
| 3 | Escribe solo su nombre («el uno por ciento») · pide perdón diez veces | `01_prologo.rpy` · 1080–1139 | Siempre |
| 4 | «¡Buenas tardes, profesor!» · defiende al MC y Nino la corta: «…No dije nada» | `02_cap1_apertura.rpy` · `cap1_apertura` · 189, 299–334 | Siempre |
| 5 | Raiha la sitúa en la pista | `02_cap1_apertura.rpy` · 769–786 | Si el jugador pregunta por ella |
| 6 | Segundo corte de Nino · «¿Y elegirás a la que quieras conocer mejor?» · «la única que miró atrás» | `02_cap1_conexiones.rpy` · `cap1_interconexion_1` · 1012–1254 | Siempre |
| 7 | **Su evento**: veintitrés vueltas, el rotulador, «Yo corro y animo», el cronómetro → decisión | `02_cap1_Yotsuba.rpy` · `hub_Yotsuba` → `yotsuba_m4a/b/c` → `m5` → `m6` | Si se elige (hub 1, 2 o 3) |
| 8 | A la mañana siguiente: el «1» con corazón / «Un minuto con catorce» / «¡Buenos días, tutor!» | `conexiones` · `reaccion_yotsuba` · 362–466 | Si fue visitada |
| 9 | «Tienes cara de haber peleado con un oso» | `cap1_interconexion_3` · 1705–1724 | Siempre |
| 10 | **La que lee a las demás**: le cuenta al MC cómo quedó la hermana del hub 2 | `cap1_interconexion_4` · 1968–2048 | Si el hub 2 no fue ella (si lo fue, Miku habla de ella) |
| 11 | El grupo de chat: «Nino lo leyó y se fue» | `cap1_interconexion_4` · 2229–2269 | Siempre |
| 12 | Lápiz al revés · «si alguna reprueba, se acaba todo» · «¡Como un equipo de relevos!» | `cap1_interconexion_5` · 2607–2658 | Siempre (salvo despido A) |
| 13 | Quince minutos más cada tarde · «¿para qué me sobra tanta energía?» | `queja_yotsuba` · 812–861 | Si no fue visitada |
| 14 | «Un sesenta es un buen número» · clima · chat del sábado | `cap1_interconexion_6` · 3099–3761 | Siempre (según clima) |
| 15 | Su página en la libreta | `02_cap1_beat_casa.rpy` · `bcl_yotsuba` · 775–880 | Siempre |
| 16 | Despido A: tercer corte de Nino · «Me dijiste que me concentrara en correr» · Despido B: hoja con solo su nombre, «No me digas que no es mi culpa» | `02_cap1_final_malo.rpy` | Ruta mala |
| 17 | E6: confesión del lunes → **lunes de japonés** (núcleo, monólogo, relevo si cálida, gesto) → tarde → eco (1 → 100) → «Esta soy yo» → foto | `02_cap1_evento6.rpy` | Ruta buena |

**Lectura del arco.** Es la hermana con más presencia fija de las tres y la que tiene **la tesis más limpia del capítulo**: el uno por ciento del prólogo, el 28 y sus cinco divisores, el «1» en la muñeca que acaba en «100». No hay ninguna escena que sobre. Lo que la debilita son costuras:
- **el E6 no se ve** (P1);
- **la Yotsuba fría** se cuela en escenas que no la tienen en cuenta (P2);
- una línea del hub que **no funciona en el hub 1** (P3);
- la cálida y la fría **terminan igual** en la pista (P4);
- una intención del borrador **perdida en el montaje** (P5).

---

## 3. Problemas (de más grave a menos grave)

### P1 · Crítico · Doce `call` caen en el label siguiente: el E6 se corta

`02_cap1_evento6.rpy` (respuesta 11)

**Qué falla.** En Ren'Py, cuando un `call` vuelve, la ejecución sigue en la línea siguiente. Si esa línea es un `label` escrito dentro del bloque, **el código entra en él**, y su `return` sale de la escena entera. Pasa en 12 sitios:

| l. | `call` | Cae en |
|---|---|---|
| 192 | `e6_s1_` + estado | `e6_s1_superado` |
| 2125 | `e6_s_tarde_` + estado | `e6_s_tarde_superado` |
| 2175 | `e6_yotsuba_tarde_` + estado | `e6_yotsuba_tarde_calida` |
| 2262 | `e6_ichika_tarde_` | `e6_ichika_tarde_calida` |
| 2347 | `e6_nino_tarde_` | `e6_nino_tarde_calida` |
| 2427 | `e6_itsuki_tarde_` | `e6_itsuki_tarde_calida` |
| 2508 | `e6_miku_tarde_` | `e6_miku_tarde_calida` |
| 2596 | `e6_tarde_pregunta` | `e6_tarde_pregunta` |
| 2814 | `e6_nino_puerta_` | `e6_nino_puerta_calida` |
| 3011 | `e6_s2_` + estado | `e6_s2_superado` |
| 3168 | `e6_` + h + `_eco_` | `e6_yotsuba_eco_calida` |
| 4232 | `e6_s3_` + estado | `e6_s3_superado` |

**Lo que pierde Yotsuba.** En la l. 192 el lunes se corta antes de las confesiones, así que su «¡Estudié las lecturas dos veces!» no sale nunca. En la l. 2125, el viernes se corta antes de las tardes. En la l. 3168, después del eco de la primera hermana que entra por la puerta, el código cae en el eco cálido de Yotsuba (aunque no le toque: el «100» en la muñeca) y la escena de los boletines se corta ahí.

**Arreglo.** No va en esta revisión: el plan está en §8. Mientras tanto, ninguna de mis propuestas de abajo depende de dónde quede cada label.

---

### P2 · Grave · La Yotsuba fría se cuela donde no la tienen en cuenta (respuesta 6)

El hub frío la deja llamándolo «tutor», con el tono de un desconocido, y convencida de que solo sirve para correr. Siete sitios no lo tienen en cuenta.

**2a.** `02_cap1_conexiones.rpy` · `cap1_interconexion_3` · l. 1718–1722 y 1767–1789. Si Yotsuba fue el hub 1:
- en la **fría**, unos días después de llamarlo «tutor», es la primera en saludarlo con un chiste, y poco después el narrador dice que **lo evitó**;
- en la **cálida**, después de gritarle lo del oso, el narrador dice que «sonrió, apenas».

Cambio el saludo en la fría y le doy a Yotsuba su propia huella en las tres ramas. La cálida es **R1**.

Actual (l. 1718–1722):
```renpy
    yotsuba "¡[mc]! ¿Cómo estás? ¡Tienes cara de haber peleado con un oso!"

    mc "Gracias, Yotsuba."

    yotsuba "¡Es un cumplido! ¡Los osos son fuertes!"
```
Reemplazo:
```renpy
    if destino == "yotsuba" and rama_hub == "fria":

        yotsuba "¡Buenos días, tutor! ¡Tienes cara de cansado!"

        mc "Gracias, Yotsuba."

        yotsuba "¡De nada!"

        narrador "Lo dijo mirando la pizarra."

    else:

        yotsuba "¡[mc]! ¿Cómo estás? ¡Tienes cara de haber peleado con un oso!"

        mc "Gracias, Yotsuba."

        yotsuba "¡Es un cumplido! ¡Los osos son fuertes!"
```

Actual (l. 1767–1789, la huella del hub 1):
```renpy
    if destino != "itsuki":

        if rama_hub == "calida":
```
Reemplazo: añado un bloque para Yotsuba delante y convierto el `if` en `elif`. Lo de dentro (Nino, la línea genérica, tibia y fría) **no cambia**:
```renpy
    if destino == "yotsuba":

        if rama_hub == "calida":

            narrador "Yotsuba me miró la muñeca. El «1» seguía ahí, a medio borrar."

            narrador "Sonrió como quien comprueba un resultado."

        elif rama_hub == "tibia":

            narrador "Yotsuba levantó el brazo desde su sitio: otro tiempo anotado en la muñeca."

        else:

            narrador "Después volvió a su sitio y se puso a ordenar la mochila. No me miró más."

    elif destino != "itsuki":

        if rama_hub == "calida":
```

**2b.** `02_cap1_conexiones.rpy` · `cap1_interconexion_4` · l. 1978, 2002, 2025–2029. Si la Yotsuba fría fue el hub 1, en el hub 2 va a contarle al MC cómo está su hermana. Eso es coherente (lo hace por la hermana, no por él), pero lo llama por su nombre. Además, «Era la primera vez que la veía así» no es verdad si el MC jugó su hub, donde ya la vio sin exclamaciones. Las líneas de la rama cálida del informe van en P6, junto con R2.

l. 1978. Actual:
```renpy
            yotsuba "¡[mc]! ¡Ven un momento!" 
```
Reemplazo:
```renpy
            if rama_de("yotsuba") == "fria":

                yotsuba "¡Tutor! ¡Ven un momento!"

            else:

                yotsuba "¡[mc]! ¡Ven un momento!"
```
l. 2002. Actual:
```renpy
            yotsuba "¡[mc]! [nombre_h] está igual que siempre."
```
Reemplazo:
```renpy
            if rama_de("yotsuba") == "fria":

                yotsuba "¡Tutor! [nombre_h] está igual que siempre."

            else:

                yotsuba "¡[mc]! [nombre_h] está igual que siempre."
```
l. 2025–2029. Actual:
```renpy
            yotsuba "[mc]. ¿Tienes un minuto?"

            narrador "Lo dijo sin exclamación. Sin sonrisa." 
            
            narrador "Era la primera vez que la veía así."
```
Reemplazo:
```renpy
            if rama_de("yotsuba") == "fria":

                yotsuba "Tutor. ¿Tienes un minuto?"

            else:

                yotsuba "[mc]. ¿Tienes un minuto?"

            narrador "Lo dijo sin levantar la voz. Sin sonrisa."

            narrador "En el aula, delante de todas, era la primera vez que la veía así."
```
`rama_de("yotsuba")` vale `None` si aún no la visitaste (le toca el hub 3), así que estas condiciones son seguras.

**2c.** `02_cap1_conexiones.rpy` · `cap1_interconexion_5` · l. 2621–2627. La Yotsuba fría, a la que el MC le dijo que se concentrara en lo suyo, dice «todas confían en ti». Con una palabra se ve dónde la dejó. Corrijo además la tilde de «más».

Actual:
```renpy
    yotsuba "Creo que estoy un poco mas nerviosa que las demás."

    yotsuba "Es que si alguna de nosotras reprueba, se acaba todo."

    yotsuba "¡Pero no va a pasar! ¡Digo... creo que no va a pasar!"

    yotsuba "Porque todas confían en ti."
```
Reemplazo:
```renpy
    yotsuba "Creo que estoy un poco más nerviosa que las demás."

    yotsuba "Es que si alguna de nosotras reprueba, se acaba todo."

    yotsuba "¡Pero no va a pasar! ¡Digo... creo que no va a pasar!"

    if rama_de("yotsuba") == "fria":

        yotsuba "Porque las demás confían en ti."

        mc_pensamiento "Las demás. Ella no se contó."

    else:

        yotsuba "Porque todas confían en ti."
```

**2d.** `02_cap1_evento6.rpy` · `e6_lunes` · l. 296–321. Tu núcleo pide confesiones que valgan en las tres ramas. La de Yotsuba no lo cumple: la **fría** dice «todavía recuerdo qué sentía cada personaje» y «¡las cinco juntas!», y diez minutos después su monólogo dice «Mirar es perder tiempo. Ya no miro». Separo la fría, sin que hable del MC.

Arreglo también la lógica de la versión visitada: «no las dejé para después […] ¡Pero calenté mis lecturas primero!» lleva un «pero» que contradice lo anterior. Y parto la línea de la no visitada que pasa de 100 caracteres.

Reemplazo del bloque `## Yotsuba` entero:
```renpy
    ## Yotsuba
    if e6_estado_de("yotsuba") == "calida" or e6_estado_de("yotsuba") == "tibia":

        call e6_foco("yotsuba", "sonriendo")

        yotsuba "¡Estudié las lecturas dos veces! Y todavía recuerdo qué sentía cada personaje."

        yotsuba "Esta vez no las dejé para después. Las calenté primero."

        yotsuba "Como antes de una carrera: si no calientas, el cuerpo se queja a mitad de camino."

        yotsuba "Después les tomé las fechas a Miku y las fórmulas a Ichika."

        yotsuba "Así que no te preocupes por mí, [mc]. ¡Voy a llegar a la meta, y las cinco juntas!"

    elif e6_estado_de("yotsuba") == "fria":

        call e6_foco("yotsuba", "sonriendo")

        yotsuba "¡Estudié las lecturas dos veces! ¡Y les tomé las fechas a Miku y las fórmulas a Ichika!"

        yotsuba "¡Hoy me concentro en lo mío! ¡Nada más!"

        narrador "Lo dijo de corrido, sin mirar a ninguna de sus hermanas."

    else:

        call e6_foco("yotsuba", "neutral")

        yotsuba "¡Repasé las fechas con Miku y las fórmulas con Ichika!"

        yotsuba "...Mis lecturas, para después. Siempre se quedan para después."

        yotsuba "Quería terminar a tiempo para que nadie se desmayara de los nervios."

        yotsuba "¡Tú incluido, [mc]!"

        yotsuba "¡Pero lo intentaré con toda la energía que me queda!"
```

**2e.** `02_cap1_evento6.rpy` · `e6_yotsuba_tarde_fria` · l. 2223 y 2231. Lo llama por su nombre, y «se hacer» lleva tilde.

Actual:
```renpy
        yotsuba "¡[mc]! ¡Hoja llena! ¡Sin mirar a nadie ni una sola vez!"
```
```renpy
        yotsuba "¡Es lo que mejor se hacer! Lo sé."
```
Reemplazo:
```renpy
        yotsuba "¡Tutor! ¡Hoja llena! ¡Sin mirar a nadie ni una sola vez!"
```
```renpy
        yotsuba "¡Es lo que mejor sé hacer! Lo sé."
```

**2f.** `02_cap1_final_malo.rpy` · `final_malo_hub3` · l. 535. El despido B llega con un desaire en el hub 3, que **puede ser el de Yotsuba**. Esa mañana lo saluda por su nombre. Dejo que «[mc]…» se le escape después del examen (l. 941), que es el momento en que se derrumba, y que la despedida vuelva a «tutor». Así el «tutor» del final pesa más.

Actual:
```renpy
    yotsuba "Buenos días, [mc]." 
```
Reemplazo:
```renpy
    if rama_de("yotsuba") == "fria":

        yotsuba "Buenos días, tutor."

    else:

        yotsuba "Buenos días, [mc]."
```

**2g.** `02_cap1_final_malo.rpy` · `final_malo_hub3` · l. 656 y 664. El despido B también puede llegar con Yotsuba **cálida** (en el hub 1 o el 2). Entonces «Nadie le había dicho que eso también contaba. Yo tampoco» es falso: se lo dijo él, en la pista, con esas palabras. Y en la fría el problema no fue no ayudarla, fue lo que le dijo.

Actual (l. 656):
```renpy
    mc_pensamiento "Nadie le había dicho que eso también contaba. Yo tampoco."
```
Reemplazo:
```renpy
    if rama_de("yotsuba") == "calida":

        mc_pensamiento "Se lo dije una vez, en la pista. Una sola vez no bastó."

    else:

        mc_pensamiento "Nadie le había dicho que eso también contaba. Yo tampoco."
```
Actual (l. 664):
```renpy
    mc_pensamiento "Aquel uno por ciento que pude ayudarle a aumentar, pero no lo hice."
```
Reemplazo:
```renpy
    if rama_de("yotsuba") == "calida":

        mc_pensamiento "Le dije que su punto de partida no era cero. Y se quedó en el uno."

    elif rama_de("yotsuba") == "fria":

        mc_pensamiento "Le dije que se concentrara en lo suyo. Nunca le dije qué era lo suyo."

    else:

        mc_pensamiento "Aquel uno por ciento que pude ayudarle a aumentar, pero no lo hice."
```

---

### P3 · Grave · El hub no funciona en los tres huecos

`02_cap1_Yotsuba.rpy` · `yotsuba_m4a` · l. 381–385

Tu `.md` dice: «Se puede jugar primero, segundo o tercero sin cambiar una línea». La cálida lo rompe:
- **«La semana pasada, cuando Ichika llegó tarde al departamento»**: si el hub es el 1, es el tercer día de trabajo y el MC no estaba ahí hace una semana.
- **«Fuiste la primera en saber que estaba agotada»** choca con lo que fijó la sesión de Ichika: lo de su cansancio y su audición solo lo sabe el MC, y solo en la cálida.
- **«Ayer»** solo vale en el hub 1 y el 3.
- **«La segunda planta»** no se sabe de qué.
- Dos líneas pasan de 100 caracteres.

Cambio los tres ejemplos por cosas que el MC **pudo ver** en cualquier hueco y que no revelan nada de nadie. El de Ichika es mejor que antes: no es que Yotsuba *sepa*, es que *actúa* sin que se lo pidan, que es justo su don.

Actual:
```renpy
    mc "Y ayer le dijiste a Miku que el libro que buscaba estaba en la segunda planta antes de que Miku siquiera preguntara."

    yotsuba "Es que siempre lo deja ahí después de leerlo."

    mc "Y la semana pasada, cuando Ichika llegó tarde al departamento, fuiste la primera en saber que estaba agotada." 
```
Reemplazo:
```renpy
    mc "Y le dijiste a Miku dónde estaba su libro antes de que ella preguntara."

    yotsuba "Es que siempre lo deja en el mismo sitio después de leerlo."

    mc "Y cuando Ichika se duerme en la mesa, eres la única que baja la voz."

    mc "Nadie te lo pidió. Ni siquiera ella."
```

La libreta cita la versión vieja. `02_cap1_beat_casa.rpy` · `bcl_yotsuba` · l. 821–823 (la 821 además pasa de 100 caracteres).

Actual:
```renpy
                    mc_pensamiento "Le conté lo que yo había notado: que supo que Nino no había dormido antes de que Nino dijera nada."

                    mc_pensamiento "Que sabía qué libro buscaba Miku y si Ichika estaba cansada o preocupada."
```
Reemplazo:
```renpy
                    mc_pensamiento "Le conté lo que yo había notado."

                    mc_pensamiento "Que supo que Nino no había dormido antes de que Nino dijera nada."

                    mc_pensamiento "Que sabía dónde dejaba Miku su libro, y que bajaba la voz cuando Ichika se dormía."
```

Y el indicio de la misma página, l. 855. «Quién miente» no lo respalda ninguna escena. Lo cambio por las tres cosas que sí se vieron:
```renpy
                mc_pensamiento "Sabe quién está cansada, quién está preocupada y quién miente, sin que nadie se lo diga."
```
Reemplazo:
```renpy
                mc_pensamiento "Sabe quién no durmió, quién busca algo y quién necesita silencio, sin que se lo digan."
```

---

### P4 · Media-alta · La cálida y la fría terminan igual en la pista (respuesta 5)

`02_cap1_Yotsuba.rpy` · `yotsuba_m4a` · l. 446–450

**Qué falla.** El tic dice: cuenta sola y se calla cuando la ven. El hub cobra eso en las dos ramas extremas **de la misma forma**:
- **cálida:** «ya no le hizo falta gritar para darse ánimos»;
- **fría:** «Dio la vuelta veinticuatro en un silencio absoluto. Sin contar. Sin animarse.»

El jugador ve el mismo resultado (Yotsuba callada) y tiene que fiarse del narrador para saber que uno es bueno y el otro malo. Además, la mañana siguiente la cálida le escribe un «1» en la muñeca y dice «¡Ahora tú también llevas la cuenta!». Ese «también» no tiene nada detrás.

**Qué cambia.** En la cálida **sigue contando en voz alta aunque él la mire**: rompe la regla 2 del tic, que es la que la protegía. Lo que deja es solo el grito de ánimo, porque el tiempo se lo dice él. Así la reacción del día siguiente es la continuación de esa vuelta. La fría queda como está: su silencio ahora contrasta con algo.

Actual:
```renpy
    narrador "Me lo pasó sin decir nada más."

    narrador "Cuando arrancó la vuelta veinticuatro, ya no le hizo falta gritar para darse ánimos."

    narrador "Algo en ella lucía distinto. No era que estuviera más rápida. Era que estaba más segura."
```
Reemplazo:
```renpy
    narrador "Me lo pasó sin decir nada más."

    narrador "Arrancó la vuelta veinticuatro. Al pasar por la grada, dijo el número en voz alta."

    narrador "Yo le contesté con el tiempo."

    narrador "Ya no se gritaba ánimos. Ahora la cuenta la llevábamos entre dos."
```

La libreta, `02_cap1_beat_casa.rpy` · l. 827. Actual:
```renpy
                    mc_pensamiento "En la vuelta veinticuatro ya no gritó para darse ánimos."
```
Reemplazo:
```renpy
                    mc_pensamiento "En la vuelta veinticuatro siguió contando en voz alta. El tiempo se lo decía yo."
```

---

### P5 · Media-alta · El monólogo cálido del E6 recupera las exclamaciones (intención perdida)

`02_cap1_evento6.rpy` · `e6_yotsuba_mono_calida` · l. 594–606 · y `e6_yotsuba_nucleo`

**Qué falla.** Tu `bloques_A.md` pedía, para este monólogo, «**sin signos de exclamación en todo el monólogo**»: la exclamación es su armadura, y en la cálida se la quita. El montaje añadió «¡Yotsuba! ¿En qué estas pensando?», «¡Concentremonos en el examen!» y «¡Vamos!». Eso vuelve a ponerle la armadura justo en el momento de la verdad. Además, el «¡Yotsuba!» es el ánimo a gritos que el hub cálido le acaba de quitar (P4).

**Qué cambia.** Conservo su manera de hablarse en tercera persona (es su tic), pero **sin gritar**. Esa diferencia es todo el cambio de la cálida. Corrijo también las tildes.

Actual:
```renpy
    yotsuba_int "Yo siempre pensé que era el uno. El más pequeño. El que nadie cuenta."

    yotsuba_int "¡Yotsuba! ¿En qué estas pensando?"

    yotsuba_int "¡Concentremonos en el examen!"

    yotsuba_int "Segunda pregunta. ¿Qué pasa cuando alguien llega para ayudarte?"

    yotsuba_int "Esa no me la sé del todo... pero creo que es como un relevo."

    yotsuba_int "Un relevo no se gana corriendo más que nadie. Se gana recibiendo bien. Trabajando juntos."
    
    yotsuba_int "¡Vamos!"
```
Reemplazo:
```renpy
    yotsuba_int "Yo siempre pensé que era el uno. El más pequeño. El que nadie cuenta."

    yotsuba_int "Vuelve al examen, Yotsuba. Despacio. Nadie te está cronometrando."

    yotsuba_int "Segunda pregunta. ¿Qué pasa cuando alguien llega para ayudarte?"

    yotsuba_int "Esa no me la sé del todo. Creo que es como un relevo."

    yotsuba_int "Un relevo no se gana corriendo más que nadie. Se gana recibiendo bien."
```

**La línea que enseñaba la voz interior también se perdió.** El `.md` decía que la voz interior se explica una sola vez, en el núcleo de Yotsuba, porque es el primer bloque: «En un examen nadie habla. Eso no quiere decir que nadie piense». En el `.rpy` no está, y el jugador oye `yotsuba_int` por primera vez sin aviso.

`e6_yotsuba_nucleo`, después de `mc_pensamiento "A Yotsuba."` y antes de `narrador "Yotsuba escribió su nombre primero. Siempre lo hace."`:
```renpy
    narrador "En un examen nadie habla. Eso no quiere decir que nadie piense."
```

`e6_yotsuba_mj` · l. 698 (pasa de 100 caracteres). Actual:
```renpy
    yotsuba_int "La segunda pregunta trataba de eso... de cuando alguien llega para ayudarte y no te deja correr sola."
```
Reemplazo:
```renpy
    yotsuba_int "La segunda pregunta trataba de eso."

    yotsuba_int "De cuando alguien llega para ayudarte y no te deja correr sola."
```

---

### P6 · Media · Reclama su don antes de que nadie se lo dé (+ romance R2)

`02_cap1_conexiones.rpy` · `cap1_interconexion_4` · rama `calida` del informe · l. 1986–1992

**Qué falla.** «¡Yo sé distinguir! **¡Es lo que mejor se me da!**» Yotsuba dice con orgullo lo que en el hub cálido niega («Eso que describes no es nada especial. Cualquiera lo haría») y lo que en la fría ni sabe que tiene. Es la línea que más se sale del personaje en todo el capítulo: si ya lo sabe, la cálida no le descubre nada.

**Qué cambia.** Si ella aún no fue cálida, minimiza («eso lo nota cualquiera»). Si ya lo fue, es el **escalón intermedio** entre la pista y el E6, el que faltaba: «Alguien me dijo que eso cuenta». Y, si la hermana del hub 2 también salió cálida, una línea mínima de lo que le cuesta alegrarse por otra (**R2**, §6.5).

Actual:
```renpy
            yotsuba "¡Yo sé distinguir! ¡Es lo que mejor se me da!"

            mc "¿Qué quieres decir?"

            yotsuba "Que lo que le dijiste, o lo que hiciste, le dejó algo bueno por dentro."

            yotsuba "Gracias por no rendirte con ella. ¡Es todo!"
```
Reemplazo:
```renpy
            if rama_de("yotsuba") == "calida":

                yotsuba "¡Yo sé distinguir! Alguien me dijo que eso cuenta."

            else:

                yotsuba "¡Yo sé distinguir! ...Bueno, eso lo nota cualquiera."

            mc "¿Qué quieres decir?"

            yotsuba "Que lo que le dijiste, o lo que hiciste, le dejó algo bueno por dentro."

            yotsuba "Gracias por no rendirte con ella. ¡Es todo!"

            if rama_de("yotsuba") == "calida":

                narrador "Antes de irse me miró la muñeca. El «1» ya casi no se veía."

                narrador "No dijo nada de eso. Se fue dando saltitos, igual que siempre."
```

---

### P7 · Media · La reacción cálida explica lo que el hub ya mostró

`02_cap1_conexiones.rpy` · `reaccion_yotsuba` · rama `calida` · l. 392–394

**Qué falla.** Las tres líneas anteriores son muy buenas y bastan, sobre todo «Nadie me había dicho algo así sin pedirme que sonriera». Lo que viene después las explica con lenguaje de ficha («lo que en verdad siento por dentro», «lo que reflejo a los demás»): no es su vocabulario. Y le resta efecto al «¡Dame la mano!», que funciona porque cambia de tema de golpe, como en el hub.

Borra estas dos líneas:
```renpy
        yotsuba "Tú entendiste lo que en verdad siento por dentro."

        yotsuba "No solo lo que reflejo a los demás."
```
Queda así:
```renpy
        yotsuba "...Ayer dijiste que mi punto de partida no era cero."

        yotsuba "Anoche no pude dejar de pensarlo."

        yotsuba "Nadie me había dicho algo así sin pedirme que sonriera."

        show yotsuba sonriendo at pj_habla(0.5)
        with disolucion_lenta

        yotsuba "Bueno."

        yotsuba "¡Dame la mano!"
```

---

### P8 · Media · El hub le dice al jugador cuál es la respuesta buena (respuesta 10)

`02_cap1_Yotsuba.rpy` · `hub_Yotsuba`

**8a.** l. 163. «Porque soy tu tutor... y me preocupo por ti.» El MC dice antes del menú lo que solo la cálida debería decir (en la fría, dos minutos después, le dice que no pierda el tiempo). Además, la reacción de ella («la solemnidad de quien acaba de recordar algo obvio», «¡Ah, claro! ¡Eso tiene sentido!») funciona mucho mejor con una respuesta seca: lo obvio es que es su tutor. Así, «Soy tu tutor. Observar es parte del trabajo» (cálida) queda como su eco.
```renpy
    mc "Porque soy tu tutor... y me preocupo por ti."
```
Reemplazo:
```renpy
    mc "Porque soy tu tutor."
```

**8b.** l. 317–319. El pensamiento del MC pone las opciones en términos de bien y mal («sonrisa intacta pero vacía» contra «su verdadero valor como persona»). Es el único hub que lo hace.
```renpy
    mc_pensamiento "Lo que diga ahora decide si se queda con esa sonrisa intacta pero vacía por dentro, "

    mc_pensamiento " o si le hago notar su verdadero valor como persona."
```
Reemplazo:
```renpy
    mc_pensamiento "Lo que diga ahora, se lo va a llevar igual: con esa sonrisa puesta."
```

**8c.** l. 333 y 341. Los otros cuatro hubs titulan el menú «¿Cómo respondes?» o «¿Qué le dirás a…?», sin narrador. El de Yotsuba pregunta «¿Cómo le ayudarías a sentirse mejor?», y con eso la opción fría no tiene sentido. Además, la opción fría no dice lo que el MC dice después, y los ecos (final A, E6) citan lo que dice el MC.
```renpy
        narrador "¿Cómo le ayudarías a sentirse mejor?"
```
```renpy
        "Si vas a seguir corriendo, deja de perder el tiempo.":
```
Reemplazo:
```renpy
        "¿Qué le dirás a Yotsuba?"
```
```renpy
        "Si correr es lo tuyo, concéntrate en eso.":
```

---

### P9 · Media · Ruta no visitada: el número que infla no se nota, y el E6 copia la queja literal

**9a.** `02_cap1_conexiones.rpy` · `queja_yotsuba` · l. 839–853. Dice «dos vueltas de más» y, seis líneas después, «tres vueltas de ventaja». Es su regla 3 (infla los números cuando algo le duele), pero nadie lo nota, así que parece un error. Hago que el MC la pille. Ella contesta con una promesa que la narración ya desmiente: al doblar la esquina se pone a caminar. «Hoy» tampoco cuadra: lo esperó varias tardes.

Actual:
```renpy
    yotsuba "No lo sientas. Es que pensé que a lo mejor hoy te hacía falta alguien que te animara."
```
Reemplazo:
```renpy
    yotsuba "No lo sientas. Es que pensé que a lo mejor te hacía falta alguien que te animara."
```
Actual:
```renpy
    yotsuba "¡Y para la próxima vez ya tengo tres vueltas de ventaja!"
```
Reemplazo:
```renpy
    yotsuba "¡Y para la próxima vez ya tengo tres vueltas de ventaja!"

    mc "Dijiste dos."

    yotsuba "¡La tercera la corro ahora mismo!"
```
Las dos líneas de narración del final («Se fue corriendo, con la sonrisa puesta» / «Pero al doblar la esquina bajó el ritmo y siguió caminando») se quedan como están. Ahora cobran algo: la tercera vuelta no existió.

**9b.** `02_cap1_evento6.rpy` · `e6_yotsuba_mono_no_visitada` · l. 660–676. En la ruta no visitada, el jugador oye «quince minutos más cada tarde… dos vueltas de más… Tres tardes no alcanzan para cinco… ¿para qué me sobra tanta energía?» en la queja, otra vez en la libreta, **casi palabra por palabra** en este monólogo y otra vez en la promesa del MC, justo después. Es el mismo caso que el P9 de Miku y el de Ichika. El monólogo debe decir algo que la queja no podía decir: lo que ella **no** le contó.

Reemplazo del label entero:
```renpy
label e6_yotsuba_mono_no_visitada:

    yotsuba_int "Pregunta uno. ¿Qué siente el protagonista cuando se queda solo?"

    yotsuba_int "Esa me la sé. Se queda quince minutos más en la pista. Por si acaso."

    yotsuba_int "Le dije que la tercera vuelta de ventaja la corría ese mismo día."

    yotsuba_int "No la corrí. Al doblar la esquina me puse a caminar."

    yotsuba_int "Tres suena mejor que dos. Tres suena a que no me importó tanto."

    yotsuba_int "Escribo que el protagonista espera a alguien y no sabe si llega."

    yotsuba_int "Es una buena respuesta. Y es la única que no puedo comprobar."

    return
```
El eco del E6 («Tengo tres vueltas de ventaja… ¿no caducan?») se queda: delante del MC sigue diciendo tres, y el jugador ya sabe que eran dos. La promesa del MC («Esas dos vueltas de más las cronometro yo») también se queda: él sí lleva la cuenta buena.

*(Sin 9a, este monólogo no se entiende: aplícalos juntos.)*

---

### P10 · Media-baja · El corte de Nino, dos días seguidos, sin que nadie lo note

`02_cap1_conexiones.rpy` · `cap1_interconexion_1` · después de l. 1061–1064

**Qué falla.** Apertura (día 2): «Nino, eso no es justo. Él solo está—» / «Yotsuba.» / «…No dije nada». Interconexión 1 (día 3): «¡Nino! Seguro no es eso. Él solo—» / «Yotsuba.» / «…¡Digo! ¡Nada! ¡Era una broma!». Se lee como texto repetido, no como patrón. La tercera vez (despido A) sí funciona como pago, y la libreta lo cita. No toco la línea de Nino: basta con que el MC lo vea.

Después de:
```renpy
    yotsuba "...¡Digo! ¡Nada! ¡Era una broma!"

    show yotsuba sonriendo at pj_calla(X_YOTSUBA)
    with disolucion_lenta
```
añade:
```renpy
    mc_pensamiento "Igual que ayer. A Nino le basta con decir su nombre."
```

---

### P11 · Media-baja · Una materia, dos nombres (respuesta 7)

`02_cap1_Yotsuba.rpy` · `yotsuba_m4a` · l. 409. Es la única «Literatura» del juego; el resto dice «Japonés».
```renpy
    mc "En Literatura entra algo que se llama comprensión lectora."
```
Reemplazo:
```renpy
    mc "En Japonés entra algo que se llama comprensión lectora."
```

---

### P12 · Media-baja · Sábado: «Me sorprende que ese mensaje venga de Yotsuba»

`02_cap1_conexiones.rpy` · `cap1_interconexion_6` · l. 3759–3761

**Qué falla.**
- En la cálida, el MC ya sabe desde hace semanas que Yotsuba «sabe más de lo que aparenta»: se lo dijo él.
- La línea va como `narrador` y en presente, cuando el resto del narrador va en pasado.
- «La culpa no se paga, se comparte» es una frase preciosa, y viene justo de la hermana que **nunca comparte la suya**.

Actual:
```renpy
            narrador "Me sorprende que ese mensaje venga de Yotsuba."

            narrador "Sabe más de lo que aparenta."
```
Reemplazo:
```renpy
            mc_pensamiento "Lo escribió la que siempre se queda con la culpa de las cinco."

            mc_pensamiento "A ella nadie se lo dice."
```

---

### P13 · Baja · El coro del prólogo (respuesta 8)

`01_prologo.rpy` · l. 1001 y 1007. Lo grita porque lo gritan las demás, y su propia presentación ya dio la clave del personaje: «La pregunta le salió **medio tono más bajo**».

Actual:
```renpy
    show yotsuba sonriendo at pj_habla(X_YOTSUBA)
```
Reemplazo:
```renpy
    show yotsuba incomoda at pj_habla(X_YOTSUBA)
```
Después de `narrador "Las cinco gritaron al mismo tiempo desde la entrada de la sala."`:
```renpy
    narrador "Yotsuba también. Medio tono más bajo que las demás."
```

`01_prologo.rpy` · l. 1137–1139. La 1137 es una frase sin verbo, y la 1139 pasa de 100 caracteres.

Actual:
```renpy
    narrador "Y Yotsuba, aplastada por la culpa de ver a las demás irse."
    
    narrador "Me pidió perdón unas diez veces haciendo reverencias antes de salir huyendo a su cuarto prometiendo 'estudiar el doble mañana'."
```
Reemplazo:
```renpy
    narrador "Yotsuba, aplastada por la culpa de ver a las demás irse, me pidió perdón unas diez veces."

    narrador "Con reverencias. Y salió huyendo a su cuarto, prometiendo «estudiar el doble mañana»."
```

---

### P14 · Baja · Detalles, voz y erratas

**14a · «Ichika actúa» (respuesta 9).** `02_cap1_evento6.rpy` · `e6_yotsuba_mono_tibia` · l. 624
```renpy
    yotsuba_int "Ichika duerme poco. Nino cocina. Miku sabe de historia. Itsuki estudia."
```
Reemplazo (eco exacto del hub):
```renpy
    yotsuba_int "Ichika actúa. Nino cocina. Miku sabe de historia. Itsuki estudia."
```

**14b · El 28 en la muñeca.** `e6_yotsuba_gesto_calida` · l. 733. «Un 28 con una raya encima» se lee como un número periódico o como algo tachado, y «Hoy no necesitaba la cuenta» no aclara cuál de los dos.
```renpy
    narrador "En la muñeca llevaba un 28 con una raya encima. Hoy no necesitaba la cuenta."
```
Reemplazo:
```renpy
    narrador "En la muñeca llevaba escrito un 28. No era una cuenta de vueltas."
```

**14c · Su marca es el volumen (§1, «Voz»).** Ichika ya tiene «Lo dijo sin exclamación» como señal propia. Para Yotsuba, el narrador habla de volumen. La l. 2027 de la interc. 4 ya va en P2b.

`02_cap1_evento6.rpy` · `e6_yotsuba_tarde_calida` · l. 2195
```renpy
        narrador "Lo dijo sin exclamación. En Yotsuba, eso sonaba más fuerte que un grito."
```
Reemplazo:
```renpy
        narrador "Lo dijo sin gritar. En Yotsuba, eso sonaba más fuerte que un grito."
```

**14d · El hub repite que «seguía ahí con el cronómetro».** `02_cap1_Yotsuba.rpy` · l. 271–273 y 303–309. La misma imagen sale tres veces en veinte líneas.

Borra la l. 273:
```renpy
    narrador "Ella seguía ahí, con el cronómetro en alto, esperando que lo tomara."
```
l. 303–309. Actual:
```renpy
    narrador "La sonrisa se le torció un instante."    

    narrador "Después volvió a sonreir nuevamente, como si nada."  

    narrador "Ella seguía ahí, con el brazo estirado esperando que tomara el cronómetro, "

    narrador " la sonrisa firme en su sitio."
```
Reemplazo:
```renpy
    narrador "La sonrisa se le torció un instante."

    narrador "Después volvió a su sitio, como si nada."

    narrador "Seguía con el brazo estirado. El cronómetro, colgando de su cordón."
```

**14e · El cronómetro se va con el MC.** `yotsuba_m5`. En la cálida y la tibia, el MC se queda con el cronómetro, y en el Mov. 5 se va sin devolverlo. Después de `narrador "Recogí mis cosas y caminé hacia la salida del graderío."`:
```renpy
    if yotsuba_rama_cap1 != "fria":

        narrador "Le dejé el cronómetro colgado de la valla, donde pudiera verlo."
```

**14f · Frases partidas con espacio inicial.** El hub parte varias frases en dos cuadros, con la segunda empezando por espacio y minúscula. En pantalla se ven como dos frases sueltas.

| l. | Actual | Reemplazo |
|---|---|---|
| 104–106 | `"Se paró en seco a mitad de la pista, "` · `" murmurando algo entre dientes mientras contenía la respiración."` | `narrador "Se paró en seco a mitad de la pista."` · `narrador "Murmuró algo entre dientes, sin aire."` |
| 262–264 | `"Dio un par de saltos en el sitio, sacudiendo los brazos, "` · `" como si con eso pudiera sacudirse también lo que acababa de decir."` | `narrador "Dio un par de saltos en el sitio, sacudiendo los brazos."` · `narrador "Como si así pudiera sacudirse también lo que acababa de decir."` |
| 371–373 | `"Su sonrisa no desapareció,"` · `" pero tardó un poco más en reaccionar."` | `narrador "Su sonrisa no desapareció."` · `narrador "Pero tardó un poco más en llegar."` |

**14g · La verdad se le escapa sin exclamación.** `02_cap1_Yotsuba.rpy` · l. 195. «Que sí…» no se entiende. Es el sitio perfecto para el recurso formal del `.md`: la parte verdadera va sin exclamación.
```renpy
    yotsuba "¡Solo cuando quiero mejorar!... Que sí... ¡Es todos los días!"
```
Reemplazo:
```renpy
    yotsuba "¡Solo cuando quiero mejorar!"

    yotsuba "…O sea, todos los días."
```

**14h · La libreta, ruta no visitada.** `02_cap1_beat_casa.rpy` · l. 873. El MC no le dijo «que no había tenido tiempo»: le dijo «Lo siento».
```renpy
                mc_pensamiento "Cuando le dije que no había tenido tiempo, repitió tres veces que no pasaba nada."
```
Reemplazo:
```renpy
                mc_pensamiento "Cuando le pedí perdón, me dijo de tres maneras distintas que no pasaba nada."
```

**14i · Erratas y líneas largas.**

| Archivo · l. | Actual | Reemplazo |
|---|---|---|
| `evento6` · 319 | `yotsuba "Quería terminar a tiempo para que nadie se desmayara de los nervios antes del examen, ¡tú incluido, [mc]!"` | Ya va en P2d |
| `evento6` · 2620–2622 | `narrador "Hasta al menos importante como yo."` | `narrador "Hasta al que nunca entraba en la cuenta: yo."` |
| `evento6` · 3752 | `yotsuba "¡¡Entonces abrámolos ya!!"` | `yotsuba "¡¡Entonces abrámoslos ya!!"` |
| `final_malo` · 258 | `if "yotsuba" in hub_visitadas:` | `if rama_de("yotsuba") == "fria":` (hoy funciona porque el despido A exige dos frías; es el mismo caso que en Nino, Miku e Ichika) |

---

## 4. Líneas nuevas sugeridas

### N1 · La fría vuelve a decir su nombre (respuesta 6)

`02_cap1_evento6.rpy` · `e6_mesa`, después de l. 3823 (`yotsuba "¡¡Y lo hicimos todas!! ¡¡Y tú también, [mc]!!"`).

**Para qué:** en la fría lo ha llamado «tutor» desde la pista (P2). Con los cinco boletines delante, sin pensarlo, vuelve a su nombre. Es el único momento de la ruta fría en que el jugador ve que algo se puede arreglar, y sirve de puente al Cap. 2 sin prometer nada.
```renpy
    if e6_estado_de("yotsuba") == "fria":

        narrador "Me llamó por mi nombre. Desde la pista no lo había vuelto a hacer."
```

### Romance · Solo en la cálida (respuestas 1, 2 y 4)

Todo va en el mismo objeto: **la cuenta en la muñeca**. Ninguna línea declara nada.

| # | Dónde | Qué hace | Ya incluido en |
|---|---|---|---|
| — | `reaccion_yotsuba`, cálida (existe) | El «1» con un corazón torcido: «¡No es un corazón! ¡Es… una vuelta!» | No se toca |
| **R1** | `cap1_interconexion_3` | Días después, le mira la muñeca: el «1» sigue ahí, a medio borrar. **Él no se lo lavó.** | P2a |
| **R2** | `cap1_interconexion_4` | «Alguien me dijo que eso cuenta». Si la otra hermana también salió cálida, le mira la muñeca: el «1» casi no se ve. Se alegra por su hermana y no dice nada de lo suyo | P6 |
| **R3** | `e6_yotsuba_eco_calida` | No retira el corazón: lo está practicando | abajo |
| **R4** | `e6_yotsuba_mono_calida` (existe) | «Conté veintitrés vueltas sola, y alguien llevaba ocho mirándome» | No se toca |

**R3.** `02_cap1_evento6.rpy` · `e6_yotsuba_eco_calida` · l. 3184–3188

**Qué falla hoy:** «¡Esta vez sin corazón torcido! ¡Solo cuenta!» **retira** la única señal romántica de la ruta justo en el cierre del capítulo. Leída así, Yotsuba se aparta, que es exactamente lo que el fandom le reprochó (§6.5). Con dos líneas, el corazón no desaparece: se queda pendiente, y en manos de ella.

Actual:
```renpy
            call e6_foco("yotsuba", "sonriendo")

            yotsuba "¡Esta vez sin corazón torcido! ¡Solo cuenta!"

            call e6_foco("", "")
```
Reemplazo:
```renpy
            call e6_foco("yotsuba", "sonriendo")

            yotsuba "¡Esta vez sin corazón torcido!"

            call e6_foco("yotsuba", "incomoda")

            yotsuba "...Todavía no me sale recto. Lo estoy practicando."

            narrador "No dijo para cuándo. Tapó el rotulador y se fue a su sitio."

            call e6_foco("", "")
```

El hilo completo en la cálida: él le escribe el tiempo → ella le escribe un «1» con corazón → él no se lo lava → se va borrando mientras ella ayuda a sus hermanas → ella lo convierte en «100» y deja el corazón para cuando le salga recto. Es un arco romántico entero contado con un rotulador, y **todo nace en pantalla**.

---

## 5. Fortalezas (no tocar)

- **El 28.** «Sus divisores son uno, dos, cuatro, siete y catorce. Cinco números. Suman veintiocho. […] Si falta uno, la cuenta no cierra.» Es la mejor idea del E6: cinco hermanas, ninguna sobra, y la que se creía el uno descubre que sin ella no da el total. Y nace de un chiste del hub («Veinticinco es un número perfecto» / «No es un número perfecto»).
- **El uno por ciento.** Escribe solo su nombre en el prólogo, y el E6 lo cobra en cuatro estados: «El uno por ciento del primer día, bien hecho. Esta vez era solo el principio de la hoja», hasta el «100» en la muñeca.
- **La llegada a la pista.** Ella contándose las vueltas y animándose sola, y el MC que la observa sin que lo sepa. El jugador entiende al personaje antes de que hable con él.
- **«Yo corro y animo.»** La grieta se dice como un dato, no como una queja, y por eso duele. Era tu intención del `.md` y el montaje la respetó.
- **Las tres ramas son la misma Yotsuba.** La cálida baja la guardia; la tibia se ríe y esquiva («Mi cabeza va a donde van las piernas. ¡Equipo completo!»); la fría obedece con la sonrisa intacta. Ninguna es cruel. La frialdad la pone el MC.
- **«Yotsuba nunca reprocha: solo informa.»** La interc. 4 es su mejor escena fuera del hub. Que su don se vea en **otras** rutas es lo que hace que la libreta («Sabe quién…») suene verdadera en cualquier partida.
- **El grupo de chat.** «No era un grupo para burlarse de mí. Era peor: me incluía.» Dispara la crisis de Nino sin que Yotsuba haga nada malo, y le da un hilo propio a todo el capítulo: Nino se sale tres veces, Yotsuba la vuelve a meter tres veces, y en la semana del examen Nino ya no se sale.
- **`queja_yotsuba`.** «Si nadie me necesita, ¿para qué me sobra tanta energía?» y el ritmo que baja al doblar la esquina. La ruta no visitada tiene peso propio con dos líneas de narración.
- **El final B.** «La pregunta uno preguntaba qué siente el protagonista cuando se queda solo», «Cuando cierro el libro, no recuerdo qué sentía nadie» y «No me digas que no es mi culpa». El E6 es su negativo exacto.
- **«…Este es mi boletín. …Esta soy yo. …Esto lo hice yo.»** Es la primera vez en el mes que se queda callada, y lo primero que hace al recuperar la voz es devolverles el mérito a todas.
- **«¡Tú sales en la próxima! ¡Hoy es de las cinco!»** Y el MC lo cobra en la última escena: «Yotsuba dijo que salgo en la próxima».

---

## 6. Veredicto

### 6.1 Notas

| Eje | Nota | Por qué |
|---|---|---|
| Identidad | **9/10** | Se la reconoce sin la placa: exclamaciones en ráfaga, tercera persona, vocabulario de atleta y, sobre todo, los números. Pierde un punto por dos líneas que hablan como una ficha («lo que en verdad siento por dentro», «¡Es lo que mejor se me da!»). |
| Coherencia | **6/10** | El personaje es consistente; el cableado no. El E6 no se ve (P1), la fría se cuela en siete escenas (P2), el hub no funciona en el hueco 1 (P3), la libreta cita frases que ya no existen y la queja cuenta dos números distintos. |
| Progresión | **8/10** | El arco cálido es el más claro de las tres hermanas (de 1 % a 100) y cada paso tiene un detonante visible. Faltaban el escalón intermedio entre la pista y el E6 (P6), que el hub separara la cálida de la fría (P4) y que el E6 no retirara la señal romántica (R3). Con eso llega a 9. |

### 6.2 Conclusión

Tenías razón en que Yotsuba es la que más desarrollo tiene de las tres. Al cerrar el Cap. 1 el jugador sabe **quién** es: la que corre sola, anima a todas y no se cuenta a sí misma. Sabe **qué** cambió: en la cálida se cuenta, en la fría deja de contar en voz alta y en la no visitada sigue esperando. Y quiere saber **qué hará** con eso. Su tesis (el uno por ciento, el 28, el «1» que pasa a «100») es la más limpia del capítulo, y ningún otro personaje tiene un motivo visual tan barato y tan eficaz como un rotulador.

Lo que la frena es casi todo fontanería:
- un E6 que hoy no se ejecuta entero (P1);
- una Yotsuba fría con la que siete escenas no cuentan (P2);
- un ejemplo del hub imposible en el hueco 1 (P3);
- una intención del borrador perdida (P5).

Los cambios de fondo son tres, y son pequeños: que en la cálida **siga contando aunque la miren** (P4), que no reclame su don antes de tiempo (P6) y que **no retire el corazón** (R3).

**Fidelidad al canon:**
- **Cambios intencionales que funcionan:** sin Kioto ni pasado compartido; el atletismo como su sitio propio (en el canon ayuda a varios clubes sin tener uno); el don de leer a las personas, que en el canon solo se insinúa y aquí es su eje.
- **Se respeta:** la energía, el lazo, el «¡sí!» fácil, que ayude a todas, la autoestima baja y el japonés como su materia fuerte, igual que en el canon.
- **Descuido:** ninguno de canon. Los fallos son de continuidad interna.

### 6.3 Las tres correcciones de mayor impacto

1. **P1:** las 12 caídas del E6. Sin esto, la ruta buena de Yotsuba no se ve.
2. **P2:** la Yotsuba fría en siete escenas. Es lo que hace que la fría y la cálida se contaminen.
3. **P4 + R1–R3:** la cuenta compartida. Convierte el tic en el hilo del romance y separa la cálida de la fría en el momento en que el jugador decide.

### 6.4 Qué debe sentir el jugador al cerrar el Cap. 1 (respuesta 4)

**Idea central: ganas de llevarle la cuenta a ella.** Yotsuba anima a todo el mundo y nadie la anima a ella. El jugador debe cerrar el capítulo queriendo ser quien le dice el tiempo desde la grada. No es lástima ni rescate: es **reciprocidad**. Este sentimiento la protege del odio del fandom: el jugador no la ve como «la que gana», sino como la que por fin recibe algo.

| Estado | Lo que debe sentir | Lo que ya lo sostiene | Lo que añado |
|---|---|---|---|
| Cálida | **Complicidad y ternura**: tienen algo de los dos (la cuenta) que nadie más entiende | «Nadie me había dicho algo así sin pedirme que sonriera», el 28, el relevo, el «100» | P4, P6, R1–R3 |
| Tibia | **Cariño con una espina**: es divertidísima y no le preguntó nada | «Equipo completo», «Yo también im—», la frase en blanco | P14a (el eco del hub) |
| Fría | **Remordimiento**: la hizo más eficaz y más sola | «Tutor», 40 vueltas, «Mirar es perder tiempo», «Una de las dos sobraba» | P2 (que se note en todas partes) y N1 (una puerta abierta) |
| No visitada | **Deuda**: alguien te esperó en una pista vacía | La queja, el ritmo al doblar la esquina, «¿no caducan?» | P9 (lo que no te contó) |

### 6.5 El romance: veredicto para que el fandom no la odie (respuestas 1, 2 y 4)

**Por qué el fandom odió a la Yotsuba ganadora** (y qué hace tu juego con cada cosa):

| Reproche al canon | Tu juego hoy | Regla para los Cap. 2 y 3 |
|---|---|---|
| El **destino**: la niña de hace cinco años, revelada al final | Eliminado (respuesta 1) | No volver a él nunca, ni como guiño |
| Ganó **sin construir el romance en pantalla**; las demás lo pelearon capítulo a capítulo | Su romance se construye entero en pantalla y solo en la cálida | Cada paso, con un detonante que el jugador vio y eligió |
| Ganó **apartándose**: ayudó a sus hermanas a acercarse a él mientras callaba lo suyo, y se premió esa renuncia | La renuncia existe como rasgo (interc. 4) | **Su defecto es el obstáculo, no el mérito.** Su ruta no premia que se aparte: le pide que **pida algo para ella en voz alta**. Es la frase que la tibia deja cortada: «Yo también im—». Su final romántico es terminarla |
| **Ocultó cosas** a sus hermanas (y al lector) | No oculta nada importante | Si siente celos, los dice a su manera, aunque sea con un número inflado que alguien le pilla. En su final, se lo cuenta ella a sus hermanas antes que a nadie |
| Fue **pasiva** | Es la que propone: el chat, la foto, la cuenta en la muñeca | Que siga proponiendo. El MC no la «salva»: le lleva la cuenta |

**Dos reglas más:**
- **Nunca gana a costa de una hermana.** Si en su ruta otra queda triste, Yotsuba lo nota primero (es su don) y no lo esconde. No hace falta resolverlo: basta con que no se lo calle.
- **Es la última en admitirlo.** Miku se enamora primero (tu canon) y Yotsuba lo admite la última. Así no compite en velocidad: su ruta es la de reconocerse.

**En el Cap. 1**, con R1–R3, se cumple todo: una cuenta compartida que nace en una pista, un corazón que no retira y nada declarado. Si el jugador cambia de hermana en el Cap. 2, Yotsuba solo le escribió un número en la muñeca.

### 6.6 La cita del Cap. 2 y el club (respuesta 3)

**Un aviso antes:** el «no saber decir que no» del canon choca con lo que fijaste para Ichika («Dice que sí antes de pensarlo», el papel de la obra). Para que no se pisen:
- **Ichika** dice que sí **por ella**: un papel, un escenario donde nadie la confunde.
- **Yotsuba** se ofrece **por los demás, antes de que se lo pidan.** Ya está en el texto: el lápiz de repuesto en la mano antes de que Ichika levante la suya, y «Reparte lo que le sobra antes de que se lo pidan».

Su conflicto con el club en el Cap. 2 tiene que ser ese: **se ofrece a cubrir a alguien**, nadie se lo pide.

**Propuesta (recomendada): «Un día sin cuenta».**
- **Escenario nuevo** (sin pista ni aula): una feria de barrio o un parque de atracciones. Es un BG `[NUEVO]` con mucho juego visual (colores, noria, puestos).
- **Premisa:** una tarde en la que ella no puede contar nada: ni vueltas, ni tiempos, ni minutos. La idea puede venir de él (cálida: «hoy cuento yo») o de ella (no visitada: «me debes dos vueltas; hoy las pago yo»).
- **Comedia:** cuenta igual, sin darse cuenta: los escalones, los peces del puesto, los segundos de la cola. El MC la pilla cada vez, y la cuenta de pilladas la lleva él.
- **Conflicto:** a media tarde, un mensaje del club: alguien se lesionó y ella **se ofrece** antes de que nadie termine la frase. Ahí está su «no». En la cálida, por primera vez, contesta que hoy no, y no sabe qué hacer con las manos. En la tibia, va al club y el MC se queda con un algodón de azúcar. En la fría, ni siquiera fue a la feria.
- **Romance:** en la noria, lo único que no se puede contar: ella pide algo para ella, o dibuja el corazón recto. Depende de cuánto quieras avanzar en el Cap. 2.
- **Celos (los que querías ver):** ve a una hermana feliz con el MC (en el chat, en una foto) y se alegra **demasiado rápido**. Él lo nota porque infla un número. «Me alegro por ella. Y me molesta alegrarme tan rápido.»

**Alternativa:** «El relevo del barrio». Un ekiden con el club, ella cubriendo una posta y él esperándola en el punto de entrega. Cobra el testigo del E6, pero es más deportiva que cita, y repite el tema «correr». La dejaría para el Cap. 3 si la necesitas.

**Variables que ya tienes** (no hace falta crear ninguna): `yotsuba_rama_cap1` / `rama_de("yotsuba")`, `yotsuba_visitada_cap1`, `e6_estado_de("yotsuba")` y, en la no visitada, `e6_promesas` (las dos vueltas que él va a cronometrar).

---

## 7. Avisos

- **Puntos:** ninguna propuesta toca `sumar_punto`, `desaires_cap1`, `primera_conexion` ni las ramas. Los condicionales nuevos solo **leen** `rama_de("yotsuba")`, `yotsuba_rama_cap1`, `e6_estado_de("yotsuba")`, `destino` y `rama_hub`. El título y el texto de la opción fría cambian (P8c), pero no su `jump`.
- **Variables nuevas:** ninguna. **Assets nuevos:** ninguno en el Cap. 1. Sprites usados, todos existentes: `yotsuba neutral`, `sonriendo`, `incomoda`, `sorprendida`. El escenario de la cita del Cap. 2 sería `[NUEVO]`.
- **Dependencias:**
  - P9b exige P9a.
  - P6 (R2) y P2a (R1) usan el «1» de la reacción cálida y hacen que se borre poco a poco; el eco del E6 ya dice «El uno se borró hace días». Aplica las tres o ninguna.
  - P3 y su arreglo en la libreta van juntos, igual que P4 y el suyo.
  - P2b y P6 tocan el mismo bloque de la interc. 4: P2b, la primera línea de cada rama; P6, el centro y el final de la rama cálida. No se pisan.
- **Diferencias `.md` / `.rpy`:**
  - **Intención perdida (E6):** el monólogo cálido debía ir sin exclamaciones (P5), y la línea que enseña la voz interior se quedó fuera (P5).
  - **Intención perdida (hub):** el `.md` decía que Ichika «estaba cansada o preocupada. Y eran cosas distintas». El `.rpy` lo redujo a «agotada» y añadió «la semana pasada». La libreta seguía citando el `.md`. P3 lo resuelve con un tercer ejemplo que funciona en todos los huecos.
  - **Intención perdida (hub):** el recurso formal del `.md` («cuando la grieta aparece… los signos desaparecen») casi no se usa en las líneas de Yotsuba del hub. P14g lo recupera en un sitio.
  - **Intención conservada:** el `.md` del hub dice que el vínculo completo con la lengua es del Cap. 2: «Futaro solo nombra la punta». Se respeta.
  - El `.md` del E6 tenía «Desde ahí se veían las cinco nucas» y «Segunda línea: el protagonista quería que alguien llegara». El montaje los cambió por otras versiones que funcionan igual. Sin problema.
  - **Puntos:** el `.md` del hub decía +2 al entrar y +1 en la cálida; el `.rpy` usa +3 / +1 / 0, que es el sistema vigente.
- **Fuera del alcance de Yotsuba:**
  - **Nino**, en la interc. 6 mixta (l. 3634): «la hoja de Yotsuba… tenía tres correcciones con su letra». «Su» puede leerse como la letra de Yotsuba. Es una línea de narración sobre Nino, así que no la toco. Si algún día quieres aclararlo: «con la letra de Nino».
  - **MC:** cambio cuatro líneas suyas (P8). Revísalas en su sesión.
  - **Tipografía:** el E6 escribe `...` y el resto del juego `…`. Mis propuestas respetan el de cada archivo.

---

## 8. Siguiente sesión: ordenar el E6 (respuesta 11)

Con Yotsuba quedan cerradas las cinco hermanas. Antes de seguir con MC, Raiha e Isanari, te recomiendo dedicar una sesión entera a `02_cap1_evento6.rpy`. Lo hace todo el mundo en la ruta buena, y hoy no se ejecuta entero.

**Objetivo:** un solo `.rpy`, en el orden en que lo vive el jugador, sin caídas y que pase `lint`.

**Plan:**
1. **Estructura fija.** Cada movimiento es un label de nivel superior que termina en `return`. Sus variantes (`_calida`, `_tibia`, `_fria`, `_no_visitada`, `_superado`, `_mixto`, `_bueno`) van **justo debajo**, también de nivel superior y con su propio `return`. No queda ningún `label` dentro de otro.
2. **Orden del archivo:** cabecera e `image` → ayudas Python → orquestador `evento_6` → `e6_bloque` → Mov. 1 → bloques Yotsuba, Ichika, Nino, Itsuki y Miku (núcleo, monólogos, minijuego, promesa, gestos) → Mov. 7 (tardes por hermana) → Mov. 8 → Mov. 9 (ecos por hermana, en el mismo orden) → Mov. 10 → `cap2_inicio`.
3. **Los 12 sitios de P1**, uno por uno.
4. **Limpieza:** comentarios de cabecera desactualizados (todavía dicen «Chat 8 / Chat 9»), `...` frente a `…`, y los `persistent` de prueba.
5. **Prueba:** `lint` y una pasada por cada estado de entrada (`superado`, `mixto`, `bueno`) con `11_e6_debug.rpy`.

**Para esa sesión, trae** el commit con los cambios de esta revisión ya aplicados (o dime cuáles descartaste), porque varias de mis propuestas (P2d, P2e, P5, P9b, P14, N1, R3) caen dentro del E6.
