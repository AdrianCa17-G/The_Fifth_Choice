# Revisión de personaje · Nino Nakano · Prólogo + Capítulo 1

> Repo revisado: `AdrianCa17-G/The_Fifth_Choice`, commit `762b89c` (09/11/2026).
> Los números de línea son de ese commit. Si aplicas cambios de arriba abajo en un mismo archivo,
> las líneas de más abajo se desplazan: guíate por la **línea actual citada**, no por el número.
> No toqué ningún `.rpy`. Nada de esto suma ni resta puntos (ver §7).

---

## 0. Cómo apliqué tus respuestas

| # | Tu respuesta | Qué hice con ella |
|---|---|---|
| 1 | Sí a una pista del miedo canónico | Dos líneas, sin escenas nuevas. En la interc. 1 Nino **hace suyo** el «Quiere dividirnos» de Miku. En la cocina añade que cada tutor que se va las deja «un poco menos juntas». Su `queja_nino` ya tenía «llegaron distintas»: ahora esa frase rima con las otras dos. N1. |
| 2 | La moda queda para el Cap. 2 o 3 | No la toco. |
| 3 | La receta es de la madre: insinuar sin decirlo | La tarjeta aparece en la cocina para **todos** los jugadores (el beat es fijo), con «letra redonda, no era la suya». El E6 cálido añade una línea sobre letras que se olvidan si no se miran. Nunca dice «madre». P2b y N2. |
| 4 | Tutores sin nombre; el conflicto es el puesto | Mantengo «perdí la cuenta» y «el último duró cuatro días». Pueden convivir: no sabe cuántos fueron, pero se acuerda del último. Solo quito un «los otros cuatro» que se confunde con las hermanas. P10. |
| 5 | ¿Conviene un arco con el padre? | **Sí, pero como semilla y sin escenas nuevas en el Cap. 1.** Ya tienes tres apuntes (la llamada del súper, el grito de la cocina y «Hablan el mismo idioma») y bastan. Conviene porque explica por qué ella hace de «adulta» en la casa: padre ausente, madre que solo queda en una tarjeta. Su ruta puede cerrarlo en el Cap. 2 o 3. Aquí solo corrijo la línea que copia un pensamiento de Ichika. P8. |
| 6 | Que yo proponga qué debe sentir el jugador | Ver §6.4: una idea central y cómo se nota en cada estado. Todas las propuestas se midieron contra ella. |
| 7 | Romance tsundere sin forzar | Tres propuestas, de menor a mayor: **R1** recalibra los «celos» de la interc. 2 (P4), **N4** el táper que «va a sobrar» y **N5** su nombre en la puerta. Las tres siguen la regla de §1: el cariño se ve en lo que **hace**, nunca en lo que dice. |
| 8 | Que yo dé un veredicto sobre el tic | **Nino termina sus frases. Corta las de los demás** («Yotsuba.»). **Las suyas solo se cortan cuando se da cuenta de que habló de más**, y entonces llega el «olvídalo». Corrijo las tres líneas que dicen otra cosa. P3. |
| 9 | ¿Está bien tan agresiva? | **Sí.** Regla: la dureza apunta al **puesto**, nunca a la persona; con sus hermanas, nunca un insulto. Los insultos son infantiles («tonto», «idiota», «nerd») y van bajando con la confianza. La curva actual ya cumple, del «¿A quién diablos…?» del prólogo al «Idiota.» sonrojado de la interc. 6. No quito nada. |
| 10 | Su nombre como hito | Hoy **nunca** lo dice. Lo dice una vez, en el E6 cálido, en la puerta y como una orden. N5. |
| 11 | Variantes con condición | Sin variables nuevas: `nino_visitada_cap1` en el beat y `len(hub_visitadas) == 2` en su evento (= hub 3, ya después de la cocina). P2. |
| 12 | Detonante de la cocina | **El chat de grupo.** El juego ya lo tenía a medias: en la interc. 4 Nino «miró el celular y se quedó quieta», ese mismo día el MC fantasea con «un grupo de chat sobre mí», y en la interc. 6 resulta que Nino lo silenció y se salió tres veces. Propongo que Yotsuba lo cree **esa mañana** con el nombre «+ Tutor». Para Nino es la prueba de que sus hermanas ya lo están metiendo en la familia. P6. |

---

## 1. Ficha del personaje tal como aparece hoy

**Rasgos.** Manda en la casa, y las demás la obedecen sin estar de acuerdo (Yotsuba). Desconfía del **puesto**, no de él: «No desconfía de mí. Desconfía del puesto». Cocina para todas («Nino cocina», «Siempre cocino yo»). Lee inglés de corrido y no sabe explicar cómo. Lleva la cuenta de todo (días, tutores, boletines: «Los conté dos veces»), menos de los tutores, de los que «perdió la cuenta».

**Voz.** Órdenes cortas y terminadas («Corta las cebollas. Finas.»). Pone etiqueta a sus propios actos para que no signifiquen nada: «Esto no significa nada», «Que quede claro», «No es una invitación», «Es una observación». Cuando la pillan, niega a gritos y en mayúsculas («¡NO! ¡Fue un «qué alivio»!»). Su quiebre es el contrario al de Miku: **habla de más, rápido**, y después se corta en seco («Olvida lo que dije»). Corta a los demás con un nombre: «Yotsuba.»

**Deseo.** Que sus hermanas no vuelvan a pasar por otra despedida. En el fondo, que **alguien se quede**.

**Miedo.** Ilusionarse y que el golpe la pille sin prepararse. Por eso «se adelanta» y pide que lo echen: «Así nunca duele a tiempo. Duele por adelantado» (E6). Con N1, también que el método «de una en una» las separe.

**Con el MC.** Lo pone «en la fila» de los anteriores desde la puerta («No vas a durar ni una semana»). Lo que lo saca de la fila no es una promesa, sino que **no prometa** (cálida) o que **haga algo sin pedirlo** (tibia: la cesta, la taza). Nunca dice su nombre: lo llama «tú», «tutor» u «oye, tú». Lo cuida a escondidas («Come algo antes de clases… si te desmayas, nos echan la culpa»).

**Su lista de motivos** (todo funciona): «cuatro días», «anota la fecha», la taza, las cebollas finas que fueron gruesas, el inglés que se lee pero no se explica, la tarjeta de receta, las listas de la compra y el chat del que se sale.

---

## 2. Mapa del arco (orden en que lo vive el jugador)

| # | Momento | Archivo · label · líneas | Condición |
|---|---|---|---|
| 1 | «¿A quién diablos le abriste la puerta?» · «No vas a durar ni una semana» | `01_prologo.rpy` · `prologo` · 597–620 | Siempre |
| 2 | «El último duró cuatro días» · «Quintillizas. Búscalo en un diccionario» | `01_prologo.rpy` · 685–940 | Siempre |
| 3 | No toca la hoja: «Un extraño dándome órdenes en mi propia casa» | `01_prologo.rpy` · 1096–1108 | Siempre |
| 4 | Organiza las cinco respuestas idénticas · «Yotsuba.» · corrige el **had to** | `02_cap1_apertura.rpy` · `cap1_apertura` · ~120–205 | Siempre |
| 5 | «Tu tercer fracaso» · «Treinta días, tutor» | `02_cap1_conexiones.rpy` · `cap1_interconexion_1` · 979–1222 | Siempre |
| 6 | **Su evento**: súper, etiquetas, «No es lo mismo leer que…», los tutores que sonreían, la tarjeta, la llamada a papá | `02_cap1_Nino.rpy` · `hub_Nino` → `nino_m4a/b/c` → `nino_m5` | Si la eliges (hub 1, 2 o 3) |
| 7 | A la mañana siguiente («Come algo» / «Sigue sin significar nada» / «Anota la fecha») | `conexiones` · `reaccion_nino` · 154–250 | Si la visitaste |
| 8 | Vigila a la hermana del hub 1 («¿Por qué no me buscaste a mí primero?» / «No armas escándalo» / «Hoy no la saludes») | `cap1_interconexion_2` · 1429–1576 | Si el hub 1 no fue ni Nino ni Itsuki |
| 9 | «Van casi diez días. Y seguimos igual» | `cap1_interconexion_3` · 1723–1744 | Siempre |
| 10 | Se va con el celular a ver a papá; las cuatro la explican | `cap1_interconexion_4` · 2127–2224 | Siempre |
| 11 | **Beat de la cocina**: «Debes despedirlo» · las cuatro una por una · «Siempre soy yo» · decisión | `02_cap1_beat_Nino.rpy` · `beat_Nino` | Siempre, tras el hub 2 (despido A si hay 2 desaires) |
| 12 | Cebollas gruesas / «Nadie toca mi taza» / «Empezando por no hablarte» | `cap1_interconexion_5` · 2376–2488 | Siempre (rama del beat) |
| 13 | «Alguien tiene que ser la que no cambia» | `queja_nino` · 674–740 | Si no la visitaste |
| 14 | «No fue el peor tutor» · tregua con Itsuki · correcciones a Yotsuba · chat | `cap1_interconexion_6` · 3036–3644 | Siempre (clima) |
| 15 | Su página en la libreta | `02_cap1_beat_casa.rpy` · `bcl_nino` · 461–613 | Si el jugador la elige |
| 16 | Despido A: «Era lo que pedí» / Despido B: guardia de 40 minutos, «Anota la fecha. Aquí la tienes» | `02_cap1_final_malo.rpy` | Ruta mala |
| 17 | E6: confesión del lunes → miércoles de inglés (monólogo, capa del beat, N1′ si cálida, gesto) → tarde → puerta → eco → «Cinco. Los conté dos veces» → foto → chat | `02_cap1_evento6.rpy` | Ruta buena |

**Lectura del arco.** Puerta → hoja → sabotaje → (súper) → cocina → examen. El hilo es **adelantarse al golpe**: pedir que lo echen antes de que se vaya solo. En la cálida, el cambio es pasar de «Así nunca duele a tiempo. Duele por adelantado» a «No pienso adelantar el golpe… Esperar no es rendirse», y entregar el examen **sin quedarse de guardia**. Es el arco más claro del capítulo después del de Itsuki. Lo debilitan tres cosas: la **revelación contada dos veces** sin que una escena reconozca a la otra, un **detonante que no se ve** el día de la cocina y un **tic que el narrador describe de dos maneras opuestas**.

---

## 3. Problemas (de más grave a menos grave)

### P1 · Crítico · El E6 se cae en todas las rutas donde no visitaste a Nino

`02_cap1_evento6.rpy` · `e6_nino_promesa` · l. 1266–1274

`mc_pensamieto` no existe. `e6_bloque` llama a este label siempre que Nino está «no_visitada», así que Ren'Py da `NameError` y la partida termina ahí. Además, la primera línea tiene la concordancia rota.

Actual:
```renpy
    mc_pensamiento "Esa vez me dijo que ni le molestaba que no la haya visitado."

    mc_pensamiento "Dijo que alguien tiene que ser la que no cambia." 

    mc_pensamiento "Para que las demás tengan a dónde volver."

    mc_pensamiento "También dijo que ya me había visto en su casa más de lo que quería." 

    mc_pensamieto "Que eso contaba como visita."
```
Reemplazo:
```renpy
    mc_pensamiento "Me dijo que ni le molestaba que no la hubiera ido a buscar."

    mc_pensamiento "Dijo que alguien tiene que ser la que no cambia."

    mc_pensamiento "Para que las demás tengan a dónde volver."

    mc_pensamiento "También dijo que ya me había visto en su casa más de lo que quería."

    mc_pensamiento "Que eso contaba como visita."
```

---

### P2 · Grave · Cuenta su miedo dos veces y ninguna escena reconoce a la otra

El evento cuenta **lo de los tutores** (sonreían el primer día, prometían quedarse). La cocina cuenta **lo de las hermanas** (cada una reacciona a su manera y ella junta los pedazos). Son dos mitades que encajan, pero el texto no lo sabe:

- **Evento en el hub 1 o 2:** en la cocina, el MC escucha la segunda mitad como si fuera nueva, y ella dice «No dije nada de esto» como si el súper no hubiera pasado.
- **Evento en el hub 3** (ya después de la cocina): el MC vuelve a preguntar «¿Por qué a mí me tratas de forma distinta?», cuando ya sabe por qué, y vuelve a pensar «Está protegiendo a sus hermanas» como si lo descubriera.

Tu borrador pedía que el evento «se leyera igual antes y después de la crisis». Hoy se lee igual, y justo por eso **no** funciona en los dos órdenes.

**2a.** `02_cap1_Nino.rpy` · `hub_Nino` · l. 197–212

Actual:
```renpy
    mc "¿Por qué a mí me tratas de forma distinta que a ellas?"

    nino "No te trato distinto."

    mc "Sí lo haces. Y no solo a mí."

    mc "A todos los que han entrado antes que yo."

    narrador "Ahí sí levantó la vista."

    show nino nerviosa at pj_habla(0.5)
    with disolucion_lenta

    nino "…"

    nino "Porque los que entraron antes también sonreían el primer día."
```
Reemplazo. `hub_visitadas` se rellena **después** de cada evento, así que aquí vale 2 solo en el hub 3:
```renpy
    if len(hub_visitadas) == 2:

        mc "En la cocina me hablaste de ellas."

        mc "De los que vinieron antes que yo no dijiste nada."

        nino "Porque no hace falta."

        narrador "Pero levantó la vista."

        show nino nerviosa at pj_habla(0.5)
        with disolucion_lenta

        nino "…"

        nino "Los que entraron antes también sonreían el primer día."

    else:

        mc "¿Por qué a mí me tratas de forma distinta que a ellas?"

        nino "No te trato distinto."

        mc "Sí lo haces. Y no solo a mí."

        mc "A todos los que han entrado antes que yo."

        narrador "Ahí sí levantó la vista."

        show nino nerviosa at pj_habla(0.5)
        with disolucion_lenta

        nino "…"

        nino "Porque los que entraron antes también sonreían el primer día."
```

`02_cap1_Nino.rpy` · `hub_Nino` · l. 235–247 (la l. 237 además pasa de 100 caracteres)

Actual:
```renpy
    mc_pensamiento "No está hablando de mí."

    mc_pensamiento "Está hablando de todos los que vinieron antes, y me está poniendo en la misma fila sin que yo haya hecho nada todavía."

    nino "Mis hermanas se ilusionan cada vez. Cada una a su manera, pero se ilusionan."

    nino "Y después les toca ver a alguien irse."

    narrador "Apretó la tarjeta un poco más fuerte contra el pecho."

    mc_pensamiento "No está protegiéndose a ella."

    mc_pensamiento "Está protegiendo a sus hermanas de algo que ya les pasó demasiadas veces."
```
Reemplazo:
```renpy
    mc_pensamiento "No está hablando de mí."

    mc_pensamiento "Está hablando de todos los que vinieron antes."

    mc_pensamiento "Y me pone en la misma fila sin que yo haya hecho nada todavía."

    nino "Mis hermanas se ilusionan cada vez. Cada una a su manera, pero se ilusionan."

    nino "Y después les toca ver a alguien irse."

    narrador "Apretó la tarjeta un poco más fuerte contra el pecho."

    if len(hub_visitadas) == 2:

        mc_pensamiento "Lo de sus hermanas ya lo sabía desde la cocina."

        mc_pensamiento "Lo nuevo era cómo apretaba esa tarjeta mientras lo decía."

    else:

        mc_pensamiento "No está protegiéndose a ella."

        mc_pensamiento "Está protegiendo a sus hermanas de algo que ya les pasó demasiadas veces."
```

**2b.** `02_cap1_beat_Nino.rpy` · `beat_Nino` · después de l. 305 (`narrador "Bajó la taza sin haber bebido nada."`) y antes de l. 307 (`mc_pensamiento "No está exagerando."`).

El beat reconoce el súper si ya ocurrió. Las dos primeras líneas son la **semilla de la receta** (N2): las ve todo jugador, porque el beat es fijo. Si no quieres la semilla, bórralas y deja solo el `if`.
```renpy
    narrador "Al bajarla, la taza quedó encima de una tarjeta escrita a mano."

    narrador "Tinta gastada, letra redonda. No era la suya."

    if nino_visitada_cap1:

        mc_pensamiento "La misma tarjeta del súper."

        mc_pensamiento "Allí me contó lo de los tutores. Hoy, lo de ellas."

        mc_pensamiento "Ahora tenía las dos mitades."
```

**2c.** `02_cap1_beat_casa.rpy` · `bcl_nino` · l. 575 (versión no visitada)

Actual:
```renpy
                mc_pensamiento "Gritó, y se frenó antes de decir por qué."
```
**Qué falla:** sí dijo por qué, a Maruo y después al MC. La línea siguiente («Habló de sus hermanas una por una») lo contradice.
Reemplazo:
```renpy
                mc_pensamiento "Gritó. Y después, sentada en la cocina, me explicó por qué."
```

---

### P3 · Media-alta · El narrador describe su tic de dos formas opuestas

En el evento, el narrador dice primero que lo habitual en ella es **cortar** las frases («Sin cortar la frase a la mitad como acostumbra») y después que **nunca** lo hace por accidente. En el final malo lo llama «táctica». Además, la l. 264 dice «Se cortó a mitad de frase» después de una frase completa («Olvida lo que dije»).

**Veredicto (respuesta 8).** Nino termina sus frases y corta las de los demás («Yotsuba.»). Las suyas solo se le cortan cuando se da cuenta de que habló de más, y entonces llega el «olvídalo». Es lo que ya hace en el mismo evento, l. 189–193: «No es lo mismo leer que…» → «Da igual. Olvídalo.» Basta con que el narrador lo señale.

`02_cap1_Nino.rpy` · `hub_Nino` · l. 220–226. Actual:
```renpy
    narrador "Se detuvo, pero solo un segundo."

    narrador "No fue el corte de siempre."

    narrador "Lo dijo más rápido de lo que suele hablar."

    narrador "Sin cortar la frase a la mitad como acostumbra."
```
Reemplazo:
```renpy
    narrador "Se detuvo, pero solo un segundo."

    narrador "Esperé el «olvídalo» de antes. No llegó."

    narrador "Siguió hablando, más rápido de lo que suele."
```

`02_cap1_Nino.rpy` · `hub_Nino` · l. 264. Actual:
```renpy
    narrador "Se cortó a mitad de frase, algo que ella nunca hace por accidente."
```
Reemplazo:
```renpy
    narrador "Ahí estaba el «olvídalo». Tarde, como le llega siempre que habla de más."
```

`02_cap1_final_malo.rpy` · `final_malo_hub3` · l. 1293. Actual:
```renpy
    narrador "Se cortó a mitad de frase. Esta vez no era una táctica."
```
Reemplazo:
```renpy
    narrador "Se cortó a mitad de frase. Esta vez no era por haber hablado de más."
```

---

### P4 · Media-alta · Los «celos» del día 4 suenan a guion (romance R1)

`02_cap1_conexiones.rpy` · `cap1_interconexion_2` · rama `calida` · l. 1466–1470 y 1492

**Qué falla.** El desliz («¿Y por qué no me buscaste a mí primero?») funciona: es tsundere y se puede negar. Lo que sobra:
- **El MC lo nombra** («¿Estás celosa?»). Eso convierte la escena en comedia romántica de manual cuatro días después de que ella pidiera que se fuera. Además, Futaro en el canon es el último en darse cuenta de estas cosas.
- **El narrador lo explica** («esa pregunta sí la dijo desde sus sentimientos»).

**Arreglo.** Ella tapa el desliz con su excusa de siempre, el **control** («las cosas pasan por mí»), y la excusa además roza su miedo canónico: que se lleve a sus hermanas de una en una. El MC solo pregunta lo literal.

Actual:
```renpy
            nino "¡Nada! ¡Era una pregunta retórica!"

            mc "Nino. ¿Estás celosa?"

            nino "¡¿CELOSA?! ¡Ni en tus sueños, tonto!"
```
Reemplazo:
```renpy
            nino "¡Nada! Que si te vas a llevar a mis hermanas de una en una, primero se me avisa."

            nino "Yo organizo esta casa. Las cosas pasan por mí."

            mc "¿Te molesta no haber sido la primera?"

            nino "¡Me molesta que hagas listas con mis hermanas, tonto!"
```
Actual (l. 1492):
```renpy
            mc_pensamiento "Pero parece que esa pregunta sí la dijo desde sus sentimientos."
```
Reemplazo:
```renpy
            mc_pensamiento "La excusa le llegó un segundo tarde. La pregunta, no."
```

---

### P5 · Media-alta · E6, tarde cálida: «sabe» el resultado antes de los boletines

`02_cap1_evento6.rpy` · `e6_nino_tarde_calida` · l. 2285–2287

Actual:
```renpy
        nino "Sin vigilar a nadie de mis hermanas. Sin quedarme de guardia." 

        nino "Se que ninguna falló en sus examenes."
```
**Qué falla:** los boletines llegan después (Mov. 8). Peor aún, contradice su propio cambio de la cálida: «No pienso adelantar el golpe… Esperar no es rendirse». Lo bonito es que no lo sepa **y no le haga falta saberlo**.
Reemplazo:
```renpy
        nino "Sin vigilar a ninguna de mis hermanas. Sin quedarme de guardia."

        nino "No sé cómo les fue. Por primera vez, no necesité saberlo antes."
```

---

### P6 · Media · La cocina no tiene detonante en pantalla (respuesta 12)

Hoy Nino se va «con el celular en la mano» y nadie sabe qué vio. Propuesta: **el chat de Yotsuba nace esa mañana**. Usa piezas que ya existen (el menú del MC sobre «un grupo de chat sobre mí», el «miró el celular y se quedó quieta» de Miku, el «lo silenció y se salió tres veces» de la interc. 6 y el «el chat sigue silenciado» del E6), y no hace falta ningún asset ni variable.

**6a.** `02_cap1_conexiones.rpy` · `cap1_interconexion_4` · l. 2191–2193

Actual:
```renpy
    show miku neutral at pj_calla(X_MIKU)
    show itsuki molesta at pj_habla(X_ITSUKI)
    with disolucion_lenta
```
Reemplazo (todo lo de Itsuki que sigue se queda igual: «la hipótesis más probable eres tú» ahora tiene una prueba):
```renpy
    show miku neutral at pj_calla(X_MIKU)
    show yotsuba incomoda at pj_habla(X_YOTSUBA)
    with disolucion_lenta

    yotsuba "…Puede que sea culpa mía."

    yotsuba "Esta mañana armé un grupo de chat. Las cinco… y tú."

    yotsuba "Le puse «¡Equipo Quintillizas + Tutor!». Nino lo leyó y se fue."

    narrador "Saqué el celular. Ahí estaba: un grupo nuevo, y mi número al final."

    mc_pensamiento "No era un grupo para burlarse de mí. Era peor: me incluía."

    show yotsuba incomoda at pj_calla(X_YOTSUBA)
    show itsuki molesta at pj_habla(X_ITSUKI)
    with disolucion_lenta
```

**6b.** `02_cap1_beat_Nino.rpy` · `beat_Nino` · l. 93–95 (la 95 pasa de 100 caracteres)

Actual:
```renpy
    nino "No se trata de su cara." 

    nino "Se trata de que va a durar lo mismo que los anteriores, y ellas van a volver a creer que esta vez sí va a ser diferente."
```
Reemplazo:
```renpy
    nino "No se trata de su cara."

    nino "Yotsuba ya le hizo un grupo de chat. Le puso «tutor» en el nombre."

    nino "Va a durar lo mismo que los anteriores."

    nino "Y ellas van a volver a creer que esta vez sí va a ser diferente."
```

**6c.** `02_cap1_conexiones.rpy` · `cap1_interconexion_6` · l. 3564–3566 (el grupo ya no es nuevo)

Actual:
```renpy
    narrador "Se llamaba «¡Equipo Quintillizas + Tutor!»." 

    narrador "Obra de Yotsuba. Con tres signos de exclamación de más."
```
Reemplazo:
```renpy
    narrador "El de Yotsuba. Seguía con sus tres signos de exclamación de más."
```

---

### P7 · Media · Rama tibia del evento: una «otra cesta» que no existe

`02_cap1_Nino.rpy` · `hub_Nino` · menú l. 305, `nino_m4b` · l. 394, 416, 425 y cierre l. 561

**Qué falla:** en la escena solo hay una cesta, la de ella. El menú habla de «bolsas», el MC levanta «la otra cesta», caminan «cada uno con su cesta» y el cierre dice «Cargué dos bolsas». El E6 tibio la recuerda bien («Cargó mi cesta»). La l. 416 además pasa de 100 caracteres.

Actual (l. 305):
```renpy
        "Ayudarla con las bolsas, sin decir nada.":
```
Reemplazo:
```renpy
        "Cargarle la cesta, sin decir nada.":
```
Actual (l. 394):
```renpy
    narrador "Levanté la otra cesta que había dejado en el suelo y empecé a caminar hacia la caja."
```
Reemplazo:
```renpy
    narrador "Le quité la cesta del brazo y empecé a caminar hacia la caja."
```
Actual (l. 416):
```renpy
    narrador "Fue lo más parecido a un agradecimiento que iba a conseguir, y terminó caminando a mi lado sin discutirlo."
```
Reemplazo:
```renpy
    narrador "Fue lo más parecido a un agradecimiento que iba a conseguir."

    narrador "Terminó caminando a mi lado sin discutirlo."
```
Actual (l. 425):
```renpy
    narrador "Hicimos el resto del pasillo en silencio, cada uno con su cesta."
```
Reemplazo:
```renpy
    narrador "Hicimos el resto del pasillo en silencio. Yo con su cesta; ella sin saber dónde poner las manos."
```
Actual (l. 561):
```renpy
        mc_pensamiento "Cargué dos bolsas y no dijimos nada importante."
```
Reemplazo:
```renpy
        mc_pensamiento "Cargué su cesta y no dijimos nada importante."
```

---

### P8 · Media · Beat: tres líneas que no cuadran con lo que ya vio el jugador

`02_cap1_beat_Nino.rpy`

**8a.** `nino_beat_m4a` · l. 370. Ichika dijo en la interc. 4 que Nino «dijo que iba a hablar algo urgente con nuestro papá», así que sí avisó.

Actual:
```renpy
        mc "Sola, sin avisarle a nadie."
```
Reemplazo:
```renpy
        mc "Sola. Sin que ninguna de ellas te lo pidiera."
```

**8b.** `nino_beat_m4c` · l. 497. Para ese momento van más de dos semanas.

Actual:
```renpy
        nino "Ni un día entero de conocerme y ya sabes exactamente qué decirme para que me calle."
```
Reemplazo:
```renpy
        nino "Dos semanas aquí y ya sabes exactamente qué decirme para que me calle."
```

**8c.** `nino_beat_m4c` · l. 514–516. Es casi idéntica a `02_cap1_Ichika.rpy` l. 469–471 («Dije exactamente lo que un padre le diría…»). Aquí tiene más sentido que en Ichika porque el padre está en la escena, así que hay que hacerla **concreta**: Maruo y la forma en que ella le contesta, que es irse.

Actual:
```renpy
        mc_pensamiento "Le dije justo lo que un padre le diría."

        mc_pensamiento "Y ella me contestó justo lo que le contesta a un padre."
```
Reemplazo:
```renpy
        mc_pensamiento "Le hablé como le habla Maruo."

        mc_pensamiento "Y ella me contestó como le contesta a Maruo: yéndose."
```

---

### P9 · Media · Interc. 5: «mirada de odio» en las tres ramas

`02_cap1_conexiones.rpy` · `cap1_interconexion_5` · l. 2376

Actual:
```renpy
    mc_pensamiento "Ya sabía quien era con solo ver esa mirada de odio hacia mi."
```
**Qué falla:** precede a las tres ramas del beat. En la cálida la viste cortar cebollas contigo; en la tibia, quedarse con su taza. «Odio» solo encaja con la fría.
Reemplazo (neutro):
```renpy
    mc_pensamiento "Ya sabía quién era antes de verle la cara. Solo una se me cruza así."
```

---

### P10 · Media-baja · Tres líneas del evento que dicen otra cosa de lo que pasó

`02_cap1_Nino.rpy`

Actual (l. 293), «los otros cuatro» se confunde con las hermanas:
```renpy
    mc_pensamiento "Lo que diga ahora decide si me pone en la misma fila que los otros cuatro, o no."
```
Reemplazo:
```renpy
    mc_pensamiento "Lo que diga ahora decide si me pone en la misma fila que los anteriores, o no."
```

Actual (l. 541–545). El MC tiene una deuda en casa: no va a «acercar la cartera» en un pasillo de importados. Y la escena **sí** la vio bajar la guardia.
```renpy
    narrador "En la caja, pagó ella misma, sin dejarme acercar la cartera."

    mc_pensamiento "Ni eso me lo iba a dejar hacer."

    mc_pensamiento "Una de cinco. Y esta no bajó la guardia ni un minuto entero."
```
Reemplazo:
```renpy
    narrador "En la caja pagó ella, sin mirar el total."

    mc_pensamiento "Lo que costaba esa cesta era lo que yo gasto en comida en un mes."

    mc_pensamiento "Una de las cinco. Y esta solo bajó la guardia un minuto."
```

---

### P11 · Media-baja · E6: el «cuatro días» se repite y aparece un tic de Itsuki

**11a.** `02_cap1_evento6.rpy` · `e6_lunes` · l. 412–416. En la ruta cálida el jugador oye «el último duró cuatro» el lunes y otra vez en el eco («El último duró cuatro días. Tú llevas treinta y cinco»), que es la buena. Dejo la cuenta de días que avanza (tu decisión: 30 → 32 → 35) y guardo el «cuatro» para el eco. La l. 416 pasa de 100 caracteres.

Actual:
```renpy
        nino "Treinta días. El último tutor duró cuatro. ...Haz la cuenta tú."

        nino "Y no pongas esa cara. Yo no dije nada. Los números hablan solos."

        nino "Repasé inglés leyendo etiquetas en voz baja. ...Si me viste mover los labios en el súper, no viste nada."
```
Reemplazo:
```renpy
        nino "Treinta días. Y sigues viniendo. ...No digo nada más."

        nino "Y no pongas esa cara. Yo no dije nada. Los números hablan solos."

        nino "Repasé inglés leyendo etiquetas en voz baja."

        nino "...Si me viste mover los labios en el súper, no viste nada."
```

**11b.** `e6_nino_mono_no_visitada` · l. 1202. «Datos sin conclusión» es vocabulario de Itsuki. El motivo propio de Nino son las **listas** (de la compra, «cinco listas, una por hermana»).

Actual:
```renpy
    nino_int "Eso queda en la columna de los datos sin conclusión."
```
Reemplazo:
```renpy
    nino_int "Eso no sé en qué lista ponerlo."
```

**11c.** `e6_nino_tarde_no_visitada` · l. 2341. En la ruta no visitada dice «observación» dos veces seguidas (aquí y en `e6_mesa` l. 3631). Quito esta.

Actual:
```renpy
        nino "Seguías en tu sitio. Eso es todo. Una observación."
```
Reemplazo:
```renpy
        nino "Seguías en tu sitio. Eso es todo."
```

---

### P12 · Baja · El menú del beat no dice lo mismo que la línea

`02_cap1_beat_Nino.rpy` · l. 338. El jugador elige «tus pedazos» y oye «los tuyos».

Actual:
```renpy
        "¿Y quién junta tus pedazos?":   
```
Reemplazo:
```renpy
        "¿Y quién junta los tuyos?":
```

---

### P13 · Baja · Despido A: la condición del reproche es frágil

`02_cap1_final_malo.rpy` · `final_malo_beat` · l. 113

Actual:
```renpy
    if "nino" in hub_visitadas:
```
**Qué falla:** hoy funciona por casualidad. El despido A exige dos frías en dos hubs, así que si Nino fue visitada, por fuerza fue fría. Si algún día cambia el umbral, una Nino cálida («no te voy a prometer nada») le reprocharía «Me dijiste que ibas a durar». Es mejor que la condición diga lo que de verdad comprueba.
Reemplazo:
```renpy
    if rama_de("nino") == "fria":
```

---

### P14 · Baja · Erratas en sus escenas

| Archivo · l. | Actual | Reemplazo |
|---|---|---|
| `conexiones` · 3080 | `nino "Solo haz empeorado las cosas."` | `nino "Solo has empeorado las cosas."` |
| `final_malo` · 141 | `nino "Aunque si deberías sentirte orgulloso."` | `nino "Aunque sí deberías sentirte orgulloso."` |
| `final_malo` · 577 | `nino "Alguien tiene que decirtelo y me toca a mí."` | `nino "Alguien tiene que decírtelo y me toca a mí."` |
| `evento6` · 1033 | `nino_int "«¿Y quién junta los tuyos?» No contesté. No supe que."` | `nino_int "«¿Y quién junta los tuyos?» No contesté. No supe qué."` |
| `evento6` · 1057 | `nino_int "'Deja de juntar los pedazos de los demás y concentrate en los tuyos'"` | `nino_int "«Deja de juntar los pedazos de las demás y ocúpate de los tuyos.»"` (la cita exacta del beat) |
| `evento6` · 1059 | `nino_int "Que gran respuesta, era de esperarse de un tonto como él."` | `nino_int "Qué gran respuesta. Era de esperarse de un tonto como él."` |
| `evento6` · 1150 | `nino_int "Le dije que se guardara su promesa vacia."` | `nino_int "Le dije que se guardara su promesa vacía."` |
| `evento6` · 1188 | `nino_int "No le dije si mejor o peor. No pienso decirselo."` | `nino_int "No le dije si mejor o peor. No pienso decírselo."` |
| `evento6` · 1285 | `narrador "Nino terminó, revisó la hoja una vez mas y dejó el lápiz sobre la mesa."` | `narrador "Nino terminó, revisó la hoja una vez más y dejó el lápiz sobre la mesa."` |
| `evento6` · 1297 | `narrador "Ya no hacia falta ver por las demas."` | `narrador "Ya no hacía falta vigilar a las demás."` |
| `evento6` · 2327 | `nino "Pues mira a alguien mas."` | `nino "Pues mira a otra."` |
| `evento6` · 3334 | `nino "Y fui yo. La que siempre recibe el golpe mas antes que todas."` | `nino "Y fui yo. La que siempre ve venir el golpe antes que nadie."` |
| `evento6` · 3629 | `nino "Hace un mes no habría apostado por que todos estuvieramos reunidos. Sin problemas."` | `nino "Hace un mes no habría apostado a vernos a los seis en esta mesa."` |
| `evento6` · 1015 | `mc_pensamiento "Además que no hay como hablar en un examen..."` | `mc_pensamiento "Además, en un examen no se habla."` |
| `evento6` · 1017 | `narrador "Mientras otros estaban en la primera pregunta."` | `narrador "Los demás seguían en la primera pregunta."` |
| `Nino` · 297 | `…"Ya perdió la cuenta de quienes prometieron quedarse. …"` | `…"Ya perdió la cuenta de quiénes prometieron quedarse. …"` |

Líneas de más de ~100 caracteres en sus escenas (divídelas así; la 237 del evento y la 95 del beat ya van en P2 y P6, y la 278 del beat en N1):

`02_cap1_Nino.rpy` · l. 144:
```renpy
    narrador "Dio un paso y se interpuso entre la estantería de importados y yo."

    narrador "Como si me hubiera acercado a un terreno prohibido."
```
`02_cap1_Nino.rpy` · l. 374:
```renpy
    narrador "Terminó de subir la cesta al brazo y siguió caminando hacia la caja."

    narrador "No me esperó. Tampoco me dijo que me fuera."
```
`02_cap1_beat_Nino.rpy` · l. 260:
```renpy
    narrador "Se sentó en uno de los bancos de la cocina, de golpe."

    narrador "Como si las piernas hubieran dejado de sostenerla el tiempo justo."
```
`02_cap1_beat_Nino.rpy` · l. 321:
```renpy
    narrador "Se puso de pie y se acomodó el uniforme."

    narrador "Como quien intenta recomponer algo que ya se salió de su sitio."
```
`02_cap1_evento6.rpy` · l. 1335:
```renpy
    narrador "Nino terminó. Soltó el lápiz sin ruido y giró la hoja boca abajo."

    narrador "Cruzó los brazos, un poco más fuerte que otras veces."
```
`02_cap1_evento6.rpy` · l. 3702:
```renpy
    narrador "Nino leyó el suyo. Luego, uno por uno, los de las demás."

    narrador "Movía los labios sin sonido."
```
`02_cap1_beat_casa.rpy` · l. 547:
```renpy
                mc_pensamiento "Que Ichika finge y Yotsuba se esfuerza el doble."

                mc_pensamiento "Que Miku se encierra más e Itsuki se lo toma personal."
```
`02_cap1_beat_casa.rpy` · l. 569:
```renpy
                mc_pensamiento "Cuando supo que no la había buscado dijo que le daba igual."

                mc_pensamiento "Que ya me había visto en su casa de sobra."
```

---

## 4. Líneas nuevas sugeridas

### N1 · La pista del miedo canónico (respuesta 1, **todas las rutas**)

**Para qué:** en el canon, Nino teme que alguien de fuera separe a las cinco. Aquí ese miedo queda como **capa de debajo** del tuyo, en dos líneas que el jugador oye siempre, y conecta con el «llegaron distintas» de su `queja_nino`.

**1a.** `02_cap1_conexiones.rpy` · `cap1_interconexion_1` · l. 1102–1104. Nino hace suyo el «Quiere dividirnos» que Miku acaba de decir.

Actual:
```renpy
    nino "¿Y a ti qué te importa dónde pasemos?"

    nino "Ninguna te lo va a decir."
```
Reemplazo:
```renpy
    nino "¿Y a ti qué te importa dónde pasamos la tarde?"

    nino "Ya oíste a Miku. Quiere separarnos, una por una."

    nino "Somos cinco. Ninguna te lo va a decir."
```

**1b.** `02_cap1_beat_Nino.rpy` · `beat_Nino` · l. 278 (también la divide, porque pasa de 100 caracteres).

Actual:
```renpy
    nino "Y cuando se van, a mí me toca juntar los pedazos de las cuatro, porque soy la única que no se ilusionó nunca."
```
Reemplazo:
```renpy
    nino "Y cuando se van, a mí me toca juntar los pedazos de las cuatro."

    nino "Porque soy la única que no se ilusionó nunca."

    nino "Cada vez que uno se va, quedamos un poco menos juntas. Y nadie lo nota."
```

---

### N2 · La tarjeta de la madre: misterio sin nombrarla (respuesta 3)

**Primera parte:** las dos líneas de narración de **P2b** (la tarjeta en la cocina, «No era la suya»), que ve todo jugador.

**Segunda parte:** `02_cap1_evento6.rpy` · `e6_nino_mono_calida`, después de l. 1104 (`nino_int "Hay cena, pase lo que pase con las notas. Cocino yo. Siempre cocino yo."`).
**Para qué:** solo en la cálida, que es donde se abre más, insinúa que la letra pertenece a alguien que ya no está. No dice «mamá». El Cap. 2 o 3 la puede cobrar.
```renpy
    nino_int "La receta de la tarjeta me la sé de memoria. La llevo igual."

    nino_int "Hay letras que, si dejas de mirarlas, se te olvida cómo eran."
```

---

### N3 · Beat, rama del ultimátum: Nino consigue lo que pidió a medias

**Dónde:** `02_cap1_beat_Nino.rpy` · `beat_Nino`, dentro del `elif desaires_cap1 == 1:`, después de l. 173 (`mc_pensamiento "Y los dos lo sabíamos."`).
**Para qué:** hoy Maruo amenaza al MC y Nino no reacciona. Es el momento en que su miedo se cumple a medias. Además prepara el «Hacía un minuto me quería fuera. Ahora me tenía fuera» del despido A.
```renpy
        narrador "Nino seguía junto a la isla. Había venido a pedir eso."

        narrador "Lo había conseguido a medias, y no tenía cara de haber ganado nada."
```

---

### N4 · Romance A · El táper que «va a sobrar» (beat cálido)

**Dónde:** `02_cap1_beat_Nino.rpy` · `nino_beat_m4a`, después de l. 416 (`narrador "Cortamos en silencio. En toda la tarde no volvió a hablar de despedirme."`) y antes de l. 418.
**Para qué:**
- Es el gesto canónico de Nino (cocinar como forma de querer), hecho a su manera: excusa práctica y una mentira que se le ve.
- Cobra el «Come algo antes de clases» de su `reaccion_nino` y la pobreza del MC (Raiha y el almuerzo).
- El MC entiende que no tiene que dar las gracias. Ese es el pacto tsundere sin que nadie lo diga.
```renpy
        narrador "Antes de ponerse con la olla, dejó un táper vacío junto a mi mochila."

        show nino molesta at pj(0.5)
        with disolucion_lenta

        nino "Eso es para ti. Lo que sobre."

        mc "Todavía no ha sobrado nada."

        show nino pillada at pj(0.5)
        with disolucion_lenta

        nino "...Va a sobrar."

        narrador "Sobró. Exactamente lo que cabía en el táper."

        mc_pensamiento "No le di las gracias. Me pareció que, si lo hacía, lo iba a tirar."

        show nino neutral at pj(0.5)
        with disolucion_lenta
```
**Eco en el E6** (opcional, requiere N4): `02_cap1_evento6.rpy` · `e6_nino_beat_calida`, después de l. 1039 (`nino_int "Parece que nunca escucha. Las usé igual."`).
```renpy
    nino_int "Le dejé un táper antes de cocinar. «Va a sobrar», le dije."

    nino_int "Cociné de más para que sobrara. Eso no lo sabe nadie."
```
Va en voz interior y no es romance declarado: es cuidado. Respeta P-11.

---

### N5 · Romance B · Su nombre, una vez y como orden (respuesta 10, **solo cálida**)

**Dónde:** `02_cap1_evento6.rpy` · `e6_nino_puerta_calida` · l. 2750.
**Para qué:** Nino no dice el nombre del MC en todo el capítulo. Que lo diga **dentro de una orden** es lo más Nino posible: el cariño escondido en una instrucción. Es el viernes, antes de los boletines y con los dos solos en la puerta, y se reserva la cálida como premio.

Actual:
```renpy
        nino "Sal. Si no sales tú, aquí no sale nadie."
```
Reemplazo (las líneas que siguen, «Esperó a que estuviera a su lado…», se quedan igual):
```renpy
        nino "Sal, [mc]. Si no sales tú, aquí no sale nadie."

        narrador "Era la primera vez que decía mi nombre. Lo dijo como una orden."

        mc_pensamiento "Supongo que, con ella, es lo mismo."
```

---

## 5. Fortalezas (no tocar)

- **«Desconfía del puesto, no de mí».** Es un núcleo claro, humano y distinto del canon sin traicionarlo. El jugador lo intuye en el súper y lo confirma en la cocina.
- **La rama cálida del evento.** «Esa es la primera vez que alguien no me promete nada» es la mejor línea del personaje: el MC la gana por **no** hacer lo que haría un protagonista.
- **«Anota la fecha».** Nace en la fría, vuelve en el despido B («Aquí la tienes»), en el monólogo frío del E6 («Es hoy») y en su eco. Es un motivo que cambia de sentido según la ruta.
- **Las cebollas finas que fueron gruesas** (interc. 5): un callback cómico que es a la vez una confesión.
- **La guardia de 40 minutos.** Funciona en espejo entre el despido B (se queda por ellas) y el E6 cálido (sale sin vigilarlas). Es la mejor imagen del capítulo para un cambio sin palabras.
- **`queja_nino` entera.** «Esa es la ventaja de no esperar: nadie te decepciona» y «Para que las demás tengan a dónde volver». Con eso, la ruta no visitada es casi tan rica como la visitada.
- **Las tres ramas son la misma chica.** La fría no la vuelve cruel: la vuelve **precisa** («Es la forma elegante de lo mismo»). La tibia vive de gestos (cesta, taza, bolsa) y el E6 los recuerda.
- **«Cinco. Los conté dos veces… Si alguien dice algo, me voy»**, con la voz quebrada, y Nino se queda. El momento de los boletines es suyo.
- **El chat.** Lo silencia, se sale y Yotsuba la vuelve a meter; en el E6 «no me salí»; en la pantalla final, «Que conste que no me salí». Es todo su arco contado en una app (y con P6 tiene un comienzo).

---

## 6. Veredicto

### 6.1 Notas
| Eje | Nota | Por qué |
|---|---|---|
| Identidad | **9/10** | Se la reconoce por la voz sin ver la placa: órdenes cortas, etiquetas («que quede claro»), el «Yotsuba.» y la negación a gritos. Solo pierde un punto por un par de préstamos de Itsuki en el E6 (P11). |
| Coherencia | **6/10** | El personaje nunca se rompe, pero la **fontanería** sí: el error que cuelga el juego (P1), la revelación duplicada según el orden (P2), el tic descrito al revés (P3), la cesta fantasma (P7) y el «sé que ninguna falló» (P5). |
| Progresión | **8/10** | Antes y después claros en las cuatro rutas, con detonantes en pantalla, salvo el de la cocina (P6). La cálida tiene una frase de cambio limpia. La no visitada avanza gracias a la queja y al beat fijo. |

### 6.2 Conclusión

Al cerrar el Cap. 1 el jugador sabe quién es Nino: la que se adelanta al golpe para que a sus hermanas no les duela. Nota el cambio, porque en la cálida sale del aula sin vigilarlas y en las otras rutas por lo menos «no se sale del chat». Y quiere seguirla, porque nunca admite nada y eso dan ganas de verlo. El personaje está bien escrito. Lo que falla es **cómo se reparte entre cinco eventos y tres huecos**: su miedo se cuenta dos veces y las escenas no se miran entre sí, un label del E6 cuelga la partida, y el narrador no se pone de acuerdo sobre cómo habla ella. En lo tonal, el romance asoma una vez demasiado pronto y demasiado explicado (interc. 2), y le faltaban los gestos pequeños que el canon le da: cocinar para él, decir su nombre sin querer. N4 y N5 los cubren sin escenas nuevas ni assets.

### 6.3 Las tres correcciones de mayor impacto
1. **P1:** la letra que falta en `mc_pensamieto`. Sin ella, todas las rutas buenas con Nino no visitada se caen.
2. **P2 (+ P6):** que el súper y la cocina se reconozcan como **dos mitades** según el orden, y que la cocina tenga un detonante en pantalla (el chat de Yotsuba).
3. **P3 + P4:** una sola regla para su tic y los «celos» recalibrados. Son las dos cosas que más afectan a su voz, y con ellas el romance pasa a ser lo que hace, no lo que se dice.

### 6.4 Qué debe sentir el jugador al cerrar el Cap. 1 (respuesta 6)

**Idea central: complicidad.** Nino fue la primera en ver venir el golpe, y esta vez se equivocó. El jugador debe cerrar el capítulo sabiendo algo que ella **nunca va a admitir**, y disfrutando de que no lo admita. No es pena ni conquista: es el placer de leer lo que no dice.

| Estado | Lo que debe sentir | Lo que ya lo sostiene | Lo que añado |
|---|---|---|---|
| Cálida | **Complicidad**: sabe que confía, ella sabe que él lo sabe, y ninguno lo dice | «No me prometiste nada», cebollas, sale del examen sin guardia, «Es distinto. Es distinto» | N5 (su nombre en la puerta), N4 (táper), N2 (la tarjeta) |
| Tibia | **Curiosidad**: una tregua de gestos. ¿Qué pasaría si le hablara de verdad? | Cesta, taza, la bolsa pesada del eco, «No te estoy esperando. Estoy sujetando una puerta» | P7 (la cesta, coherente) |
| Fría | **Pique y deuda**: ganas de demostrarle que se equivoca. «Anota la fecha» es un reto | «Anota la fecha», «Es hoy», «Sigues aquí. / Sigo.» | Nada: la fría ya está bien |
| No visitada | **Culpa leve e intriga**: se organizó para que no la buscaran, y aun así contaba los días | Queja, «a mí no se me busca», «treinta y dos días sin esperar nada», la promesa del pasillo de importados | P1 (que no se cuelgue) y N3 si hubo ultimátum |

**Para el Cap. 2.** Para saber en qué «fase» llega Nino no hace falta crear variables. Ya tienes:
- `nino_rama_cap1` / `rama_de("nino")`: cómo fue el súper.
- `nino_rama_beat`: cómo fue la cocina. Es independiente y siempre tiene valor en la ruta buena.
- El sexto hueco del N1′ (`e6_sexto_valor()`: «una taza más» / «cuando se sepa» / en blanco) y `e6_promesas` en la no visitada.
- Con N4, el táper existe en toda partida con beat cálido. Una cita del Cap. 2 en la que ella **cocina para él sin excusa** tiene ya su antecedente.
- El arco con Maruo (respuesta 5) y la tarjeta de la madre (respuesta 3) quedan sembrados para su ruta.

---

## 7. Avisos

- **Puntos:** ninguna propuesta toca `sumar_punto`, `desaires_cap1`, `primera_conexion`, las ramas ni la dificultad del N1′. Los condicionales nuevos solo **leen** `hub_visitadas`, `nino_visitada_cap1` y `rama_de()`.
- **Variables nuevas:** ninguna. **Assets nuevos:** ninguno. Todos los sprites usados existen (`nino neutral`, `pillada`, `nerviosa`, `molesta`; `yotsuba incomoda`).
- **Dependencias:** el eco del E6 de N4 requiere N4. La línea «La tarjeta…» de N2 funciona sola, pero gana fuerza con P2b.
- **Diferencias .md / .rpy:**
  - El borrador del evento pedía que se leyera «igual antes y después de su crisis». El borrador del beat decía que «no llegó a necesitar» una línea de reconocimiento. Las dos intenciones chocan con el sistema de tres huecos; las resuelve P2.
  - La contradicción del tic («sin cortar la frase como acostumbra» / «nunca por accidente») ya venía en el borrador; se resuelve en P3.
  - El borrador del beat dice que Nino va a ver a Maruo «sin avisarle a nadie», pero la interc. 4 hace que Ichika diga que sí avisó (P8a).
  - El borrador ponía `sumar_punto("nino", 1)` en la cálida; el `.rpy` pone 3, que es lo correcto con el sistema actual. El «delantal» del borrador pasó a «uniforme» y los «dos carritos» a uno: sin problema.
  - En el E6, la cuenta 30 → 32 → 35 es intencional (bloques B, D-02). P11a la conserva.
- **Fuera del alcance de Nino (lo anoto para la sesión que toque):**
  - **Yotsuba:** P6a le da tres líneas en la interc. 4, en su voz de siempre. Revísalas en su sesión.
  - **Ichika:** `02_cap1_Ichika.rpy` l. 469–471 usa el mismo «lo que un padre le diría». Con P8c ya no choca con Nino, pero conviene que sea solo de una.
  - **Maruo** (`beat_Nino` l. 189): «Se sirvió el resto del café en el fregadero» debería ser «Tiró el resto del café al fregadero».
  - **MC** (`beat_Nino` l. 244): «Mas no de lo que piensas de mí, no es lo mismo» suena forzado; algo como «No lo que piensas de mí. No es lo mismo».
  - Los comentarios de cabecera de `02_cap1_evento6.rpy` todavía dicen que Nino, Itsuki y Miku son stubs (Chat 9), aunque sus bloques ya están montados.
