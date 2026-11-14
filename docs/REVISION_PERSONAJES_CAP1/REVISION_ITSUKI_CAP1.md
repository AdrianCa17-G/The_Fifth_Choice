# Revisión de personaje · Itsuki Nakano · Prólogo + Capítulo 1

> Repo revisado: `AdrianCa17-G/The_Fifth_Choice`, commit `8b0ec70` (09/11/2026).
> Los números de línea son de ese commit. Si aplicas cambios de arriba abajo en un mismo archivo,
> las líneas de más abajo se desplazan: guíate por la **línea actual citada**, no por el número.
> No toqué ningún `.rpy`. Nada de esto suma ni resta puntos (ver §7).

---

## 0. Cómo apliqué tus respuestas

| # | Tu respuesta | Qué hice con ella |
|---|---|---|
| 1 | Lo glotón quedó relegado sin querer | No meto escenas cómicas largas ni CG. En el Cap. 1 la comida ya funciona como **ausencia** (sube a la azotea sin almuerzo): propongo **un solo gag** en el beat fijo que lo hace legible y deja una «deuda» que el Cap. 2 puede cobrar en sus citas (N1, N3). |
| 2 | Que se quede en el canon sin afectar su desarrollo | Mantengo el **tú** (pasar a «usted» sería reescribir todas sus escenas y cambiaría la dinámica). La cortesía canónica se marca con **vocabulario**: sin «demonios», «idiota» ni muletillas coloquiales; reproches formales («maleducado», «desagradable»), conectores lógicos. P13. |
| 3 | Ecos buscados | Los conservo. Solo ajusto donde el tic se **concentra** en el E6 o donde **otra hermana** lo usa (P11, P14). |
| 4 | Su nombre como hito de calidez | Hoy lo dice 3 veces y una es en un sarcasmo (interc. 1). Lo quito de ahí y lo convierto en hito visible: prólogo (lo sabe), evento cálido (lo vuelve a decir y el narrador lo marca), E6 cálido (lo firma). P5, P6, N5. |
| 5 | Rivalidad que sigue pero sin tensión, amor-odio, disculpa pendiente | Es la vara con la que medí las propuestas de romance (N4, N5): cariño que se nota en el cuerpo, nunca en una confesión. |
| 6 | En el Cap. 2 los hubs serán citas y ahí sale lo glotón | Ver §6.4: qué variables ya existen para que el Cap. 2 sepa en qué «fase» está Itsuki sin crear ninguna nueva. |
| 7 | Propuestas de romance sin salirse del personaje | Tres opciones, de menor a mayor: N1 (todas las rutas), N4 (todas las rutas), N5 (solo cálida). Elige las que quieras; son independientes salvo N3, que depende de N1. |
| 8 | El sarcasmo del juego parece forzado; ella organiza con Nino | Reescribo la propuesta del juego como **revancha por la hoja de diagnóstico**: Nino empuja con hostilidad; Itsuki, con reglas y lógica. P5. |
| 9 | Condicionales o frases neutras: decide tú | **Neutras por defecto**; condicional solo cuando el texto depende de algo que el jugador vio. Para saber si el beat la mostró «ayudada» uso `hub_visitadas[0] == "itsuki"` (ya existe y mantiene el orden): **cero variables nuevas**. |
| 10 | Arreglar el final malo | P2 y P3. |

---

## 1. Ficha del personaje tal como aparece hoy

**Rasgos.** Es la única de las cinco que estudia de verdad, y aun así falla. Orgullosa y metódica. Respeta un argumento válido aunque venga del rival («…Ese argumento es válido»). Junto con Nino lleva al grupo: Nino lo empuja con desconfianza; Itsuki, con reglas («Esta tarde se estudia en casa», «Propongo lo siguiente»).

**Voz.** Oración cerrada (sujeto, verbo, punto) y tono de informe («Es un hecho», «Es un procedimiento», «Es un registro»). Cuando se agrieta, la frase se le corta y no la termina («Pedirlo habría sido…»). Tiene una ironía seca muy suya: «No inmediatamente». Tutea al MC. La muletilla del informe casi no aparece antes del E6 (una vez en la interc. 4) y en el E6 sale seis veces en la ruta cálida.

**Deseo.** Aprobar por mérito propio: que lo que consiga sea **suyo** («Quería que fuera mío»).

**Miedo.** Que pedir ayuda demuestre que no sirve. «Ellas pueden decir que no lo intentaron. Yo no tengo esa excusa.»

**Con el MC.** Fue rival desde el asiento. Los dos se deben una disculpa y ninguno la dice. Lo respeta a regañadientes y lo vigila («Tienes la costumbre de mirar como si fueras a corregir»). Decir su nombre mide la cercanía: lo usó cuando era amable y lo perdió en cuanto él la rechazó.

**Comida.** Hoy es una ausencia: el *Munch* del prólogo y después ya nada; sube a la azotea «sin nada de comer al lado». Leída así, es una glotona a la que el estrés le quitó el hambre, y eso funciona si el jugador lo llega a notar (N1).

---

## 2. Mapa del arco (orden en que lo vive el jugador)

| # | Momento | Archivo · label · líneas | Condición |
|---|---|---|---|
| 1 | Le pide ayuda amable en su asiento; él dice «No» | `01_prologo.rpy` · `prologo` · 312–393 | Siempre |
| 2 | Azotea: tregua sin palabras | `01_prologo.rpy` · 400–499 | Siempre (menú de sabor) |
| 3 | «¿Qué demonios haces en mi casa?» · grita su nombre | `01_prologo.rpy` · 784–869 | Siempre |
| 4 | **«Ni se te ocurra decirme la respuesta»** (la regla del arco) · «¿Por qué aún no te rindes?» | `01_prologo.rpy` · 1084–1176 | Siempre (menú de sabor) |
| 5 | Le deja el asiento libre: frialdad | `02_cap1_apertura.rpy` · `cap1_apertura` · 53–140 | Siempre |
| 6 | Propone el juego · «Estaré donde siempre» | `02_cap1_conexiones.rpy` · `cap1_interconexion_1` · 1109–1236 | Siempre |
| 7 | **Su evento**: «Yo no tengo esa excusa» · decisión | `02_cap1_Itsuki.rpy` · `hub_Itsuki` → `itsuki_m4a/b/c` → `itsuki_m5` | Si la eliges (hub 1, 2 o 3) |
| 8 | A la mañana siguiente | `02_cap1_conexiones.rpy` · `reaccion_itsuki` · 455–600 | Si la visitaste |
| 9 | **Beat azotea**: «Ya no me queda ningún sitio que no lo sea» | `02_cap1_beat_Itsuki.rpy` · `beat_Itsuki` | Siempre, tras el hub 1 |
| 10 | «El juego sigue» | `cap1_interconexion_3` · 1757–1779 | Siempre |
| 11 | Acusa al MC por la ausencia de Nino | `cap1_interconexion_4` · 2190–2199 | Siempre |
| 12 | «Estoy repasando con profundidad» | `cap1_interconexion_5` · 2586–2639 | Siempre (2 variantes) |
| 13 | «Gané el juego… No inmediatamente» | `queja_itsuki` · 850–911 | Si no la visitaste |
| 14 | Cierra el juego, convoca la sesión · «…Gracias» a Nino | `cap1_interconexion_6` · 2987–3530 | Siempre (variantes por clima) |
| 15 | Su página en la libreta | `02_cap1_beat_casa.rpy` · `bcl_itsuki` · 870–1012 | Si el jugador la elige |
| 16 | Despido A / Despido B | `02_cap1_final_malo.rpy` · `final_malo_beat` / `final_malo_hub3` | Ruta mala |
| 17 | E6: confesión del lunes → examen del jueves (monólogo por estado, It1 si cálida, gesto) → tarde → eco → **disculpa interrumpida** → boletines → foto → chat | `02_cap1_evento6.rpy` · `e6_lunes`, `e6_itsuki_*`, `e6_intento`, `e6_mesa` | Ruta buena |

**Lectura del arco.** Diagnóstico → aula → azotea → examen: siempre el **mismo error arrastrado** en una conversión de unidades. En la cálida el cambio es pasar de «ni se te ocurra decirme la respuesta» a «levantar la mano no es un favor, es un procedimiento». Está bien construido. Lo que lo debilita hoy son **costuras de orden** (líneas que suponen en qué hueco cayó su evento) y **líneas del final malo que no miran la rama**.

---

## 3. Problemas (de más grave a menos grave)

### P1 · Grave · El E6 cita una frase que el jugador quizá nunca oyó (y el beat tiene una línea confusa)

Si visitas a Itsuki en el **hub 2 o 3** (cálida o fría), el beat de la azotea ya se jugó con la variante «no visitada». Aun así, el monólogo del E6 llama a `e6_itsuki_beat_ayudada`, que cita «No hace falta que sigas viniendo a comprobar cómo voy», una frase que en esa partida ella **no dijo**. Además, la línea de la otra variante del beat, «dónde has estado estos días», no se entiende: lo que quiere decir es «no te voy a preguntar por tu juego».

**1a.** `02_cap1_beat_Itsuki.rpy` · `beat_Itsuki` · l. 182–205

Actual:
```renpy
    if itsuki_visitada_cap1 and itsuki_rama_cap1 != "tibia":

        show itsuki molesta at pj(0.5)
        with disolucion_lenta

        itsuki "Ya me ayudaste con el ejercicio el otro día." 
        
        itsuki "No hace falta que sigas viniendo a comprobar cómo voy."

        mc "No vine a comprobar nada."

        narrador "No pareció creérselo del todo." 
        
        narrador "Pero no insistió."

    else:

        show itsuki molesta at pj(0.5)
        with disolucion_lenta

        itsuki "No voy a preguntarte a ti dónde has estado estos días."

        mc "No te lo iba a contar de todas formas."
```
Reemplazo. La fría ya no dice «ayudaste», porque él no la ayudó: se lo resolvió. La segunda línea queda igual en las dos ramas para que el E6 la pueda citar.
```renpy
    if itsuki_visitada_cap1 and itsuki_rama_cap1 == "calida":

        show itsuki molesta at pj(0.5)
        with disolucion_lenta

        itsuki "Ya me ayudaste con el ejercicio el otro día."

        itsuki "No hace falta que sigas viniendo a comprobar cómo voy."

        mc "No vine a comprobar nada."

        narrador "No pareció creérselo del todo."

        narrador "Pero no insistió."

    elif itsuki_visitada_cap1 and itsuki_rama_cap1 == "fria":

        show itsuki molesta at pj(0.5)
        with disolucion_lenta

        itsuki "Ya me resolviste el ejercicio el otro día."

        itsuki "No hace falta que sigas viniendo a comprobar cómo voy."

        mc "No vine a comprobar nada."

        narrador "No pareció creérselo del todo."

        narrador "Pero no insistió."

    else:

        show itsuki molesta at pj(0.5)
        with disolucion_lenta

        itsuki "No voy a preguntarte cómo va tu juego."

        mc "No te lo iba a contar de todas formas."
```

**1b.** `02_cap1_evento6.rpy` · `e6_itsuki_beat_sola` · l. 1421 (sincroniza con 1a)

Actual:
```renpy
    itsuki_int "En la azotea no le pregunté dónde había estado." 
```
Reemplazo:
```renpy
    itsuki_int "En la azotea no le pregunté cómo iba su juego."
```

**1c.** `02_cap1_evento6.rpy` · `e6_itsuki_mono_calida` · l. 1444 y `e6_itsuki_mono_fria` · l. 1506

Actual (aparece igual en las dos):
```renpy
    call e6_itsuki_beat_ayudada
```
Reemplazo (en las dos). El primer elemento de `hub_visitadas` dice si el beat la encontró ya visitada:
```renpy
    if hub_visitadas[0] == "itsuki":
        call e6_itsuki_beat_ayudada
    else:
        call e6_itsuki_beat_sola
```
Actualiza también el comentario de l. 1405:
```renpy
##  ayudada = su evento fue el hub 1 (rama cálida o fría) · sola = el resto.
```

---

### P2 · Grave · Despido A: el reproche del cuaderno no mira la rama

`02_cap1_final_malo.rpy` · `final_malo_beat` · l. 303–309

Actual:
```renpy
    if "itsuki" in hub_visitadas:

        itsuki "Me quitaste el cuaderno de las manos." 
        
        itsuki "Me lo resolviste delante de mí."

        itsuki "Eso no se me va a olvidar."
```
**Qué falla:** si la visitaste en cálida o en tibia, le reprocha algo que él nunca hizo.
**Reemplazo:** una línea por rama. La tibia enlaza con su eco del E6 («¿Qué ibas a—»).
```renpy
    if rama_de("itsuki") == "fria":

        itsuki "Me quitaste el cuaderno de las manos."

        itsuki "Me lo resolviste delante de mí."

        itsuki "Eso no se me va a olvidar."

    elif rama_de("itsuki") == "calida":

        itsuki "Me dijiste dónde mirar. Una vez."

        itsuki "Pensé que habría una segunda."

    elif rama_de("itsuki") == "tibia":

        itsuki "Me ofreciste revisarlo desde el principio. Te dije que no."

        itsuki "Ahora no voy a saber qué ibas a explicarme."
```

---

### P3 · Grave · Despido B: «Y no lo hiciste» aunque la hayas ayudado

`02_cap1_final_malo.rpy` · `final_malo_hub3` · l. 958–964

Actual:
```renpy
    itsuki "Estudié todas las noches." 

    itsuki "Y en cuanto vi la hoja, no supe que contestar."

    itsuki "Te pedí que no me ayudaras. Y no lo hiciste."

    itsuki "No sé qué es peor."
```
**Qué falla:** no tiene condición; en cálida o fría contradice lo jugado. También falta la tilde de «qué».
**Reemplazo.** El `else` cubre tibia y no visitada, donde la línea original sí es verdad:
```renpy
    itsuki "Estudié todas las noches."

    itsuki "Y en cuanto vi la hoja, no supe qué contestar."

    if rama_de("itsuki") == "calida":

        itsuki "Una vez me dijiste dónde mirar. Una vez no alcanzó."

        itsuki "No sé si la culpa es tuya o mía."

    elif rama_de("itsuki") == "fria":

        itsuki "Me resolviste un ejercicio. Uno. Y no aprendí nada de él."

        itsuki "No sé qué es peor."

    else:

        itsuki "Te pedí que no me ayudaras. Y no lo hiciste."

        itsuki "No sé qué es peor."
```

---

### P4 · Media-alta · La confesión del lunes (E6) contradice su examen del jueves

`02_cap1_evento6.rpy` · `e6_lunes` · l. 377–399

**Qué falla.** El bloque `!= "no_visitada"` incluye la **tibia**, que el jueves piensa «Hay un error. No sé dónde.»; el lunes, en cambio, dice «Ya encontré por qué fallaba». Y en la **cálida** el «ya encontré» suena a problema resuelto, cuando el jueves vuelve a atascarse. Hay que decirlo como «sé dónde mirar», que es justo el aprendizaje de la cálida. Además, la l. 383 pasa de 100 caracteres y la l. 393 tiene la sintaxis rota.

Actual:
```renpy
    if e6_estado_de("itsuki") != "no_visitada":

        call e6_foco("itsuki", "sonriendo")

        itsuki "He estudiado cada noche. Y por primera vez sé lo que hago."

        itsuki "Ya encontré por qué fallaba en las conversiones de unidades. Tres veces el mismo error, y yo sin verlo."

        itsuki "Sigo sin ser rápida. Pero ahora, cuando me trabo, sé por dónde volver."

        itsuki "No me felicites todavía. Esto se demuestra en el examen, no antes."

    else:

        call e6_foco("itsuki", "neutral")

        itsuki "He estudiado cada noche. Si tengo un problema que no sale. Saldrá."

        itsuki "Lo repito, lo reviso, lo repito otra vez. ...Siempre llego a la misma cifra."

        itsuki "No pedí ayuda a nadie. Prefiero equivocarme por mi cuenta que acertar por ayuda de un tercero."

        itsuki "Dijiste «sin excepción». Pues prepárate: yo me lo tomo en serio."
```
Reemplazo. La tibia pasa al segundo bloque, donde «No pedí ayuda a nadie» es exactamente su verdad:
```renpy
    if e6_estado_de("itsuki") == "calida" or e6_estado_de("itsuki") == "fria":

        call e6_foco("itsuki", "sonriendo")

        itsuki "He estudiado cada noche. Y por primera vez sé lo que hago."

        itsuki "Ya sé por qué fallaba en las conversiones de unidades."

        itsuki "Tres veces el mismo error, y yo sin verlo."

        itsuki "Saberlo no impide que vuelva a pasar. Pero ya sé por dónde volver."

        itsuki "No me felicites todavía. Esto se demuestra en el examen, no antes."

    else:

        call e6_foco("itsuki", "neutral")

        itsuki "He estudiado cada noche. Si un problema no sale, lo repito hasta que salga."

        itsuki "Lo repito, lo reviso, lo repito otra vez. ...Siempre llego a la misma cifra."

        itsuki "No pedí ayuda a nadie. Prefiero equivocarme sola que acertar con ayuda."

        itsuki "Dijiste «sin excepción». Me lo tomo en serio. Tú también deberías."
```

---

### P5 · Media-alta · La propuesta del juego suena forzada (y gasta su nombre)

`02_cap1_conexiones.rpy` · `cap1_interconexion_1` · l. 1108–1147

**Qué falla:** sonríe y suelta un sarcasmo sobre algo que el MC nunca dijo («se preocupa por nosotras… nos conoce mejor que nadie»). No se entiende por qué ella, que lo detesta, le propone un juego. Y dice «[mc]» en mitad de una burla, cuando su nombre tiene que ser un hito de calidez.
**Arreglo:** que sea una **revancha por la hoja de diagnóstico**. Él las evaluó a ellas; ahora ella lo evalúa a él. Así nace de su orgullo y de su lógica, y queda claro en qué se distingue de Nino.

Actual:
```renpy
    show nino neutral at pj_calla(X_NINO)
    show itsuki sonriendo at pj_habla(X_ITSUKI)
    with disolucion_lenta

    itsuki "Esperen. Tengo una idea."

    mc "¿Eh?"

    itsuki "Hagamos un juego. Al estilo quintillizas."

    show itsuki sonriendo at pj_calla(X_ITSUKI)
    show yotsuba sonriendo at pj_habla(X_YOTSUBA)
    with disolucion_lenta

    yotsuba "¿Estilo quintillizas? ¡Hurra! ¡Yo quiero jugar!"

    show yotsuba sonriendo at pj_calla(X_YOTSUBA)
    show miku neutral at pj_habla(X_MIKU)
    with disolucion_lenta

    miku "…Itsuki. Eso es justo lo que él quería."

    show miku neutral at pj_calla(X_MIKU)
    show itsuki sonriendo at pj_habla(X_ITSUKI)
    with disolucion_lenta

    itsuki "Si [mc] dice que se preocupa por nosotras…"

    itsuki "…y que nos conoce mejor que nadie…"

    itsuki "…que adivine dónde pasamos las tardes."

    itsuki "Un juego de busca y encuentra."

    mc "¿¡QUÉÉÉ!?"

    show itsuki at pj_calla(X_ITSUKI)
    with disolucion_lenta

    mc_pensamiento "Esto debe ser una broma. Y de muy mal gusto."
```
Reemplazo (lo que sigue, «Pero en parte es mi culpa…», se queda igual):
```renpy
    show nino neutral at pj_calla(X_NINO)
    show itsuki neutral at pj_habla(X_ITSUKI)
    with disolucion_lenta

    itsuki "Al contrario. Que lo averigüe él."

    mc "¿Eh?"

    itsuki "El profesor dice que eres el mejor alumno de la clase."

    itsuki "Entonces resuelve esto: dónde pasa la tarde cada una."

    itsuki "Un juego de busca y encuentra. Al estilo quintillizas."

    show itsuki neutral at pj_calla(X_ITSUKI)
    show yotsuba sonriendo at pj_habla(X_YOTSUBA)
    with disolucion_lenta

    yotsuba "¿Estilo quintillizas? ¡Hurra! ¡Yo quiero jugar!"

    show yotsuba sonriendo at pj_calla(X_YOTSUBA)
    show miku neutral at pj_habla(X_MIKU)
    with disolucion_lenta

    miku "…Itsuki. Eso es justo lo que él quería."

    show miku neutral at pj_calla(X_MIKU)
    show itsuki molesta at pj_habla(X_ITSUKI)
    with disolucion_lenta

    itsuki "No. Él quería que se lo dijéramos. Yo le propongo que lo descubra."

    itsuki "Si se equivoca de sitio, pierde la tarde. Es justo."

    mc "¿Me estás retando?"

    itsuki "Te estoy evaluando. Como tú a nosotras con tu hoja."

    show itsuki at pj_calla(X_ITSUKI)
    with disolucion_lenta

    mc_pensamiento "No era una broma. Era una revancha por la hoja de diagnóstico."
```

---

### P6 · Media · Su evento no funciona igual en los tres huecos

`02_cap1_Itsuki.rpy` · `itsuki_m5` · l. 520 y 530 (y `itsuki_m4a` · l. 369–373)

Tu `.md` dice «se puede jugar primero, segundo o tercero sin cambiar una línea», pero el propio borrador ya traía «Llevo dos días…», así que la intención se perdió desde el guion. Si su evento cae en el hub 2 o 3, han pasado semanas.

Actual (l. 520 y 530):
```renpy
    mc_pensamiento "Una de cinco. Y esta no pidió nada."
```
```renpy
        mc_pensamiento "Llevo dos días aprendiendo que con ella eso cuenta más que un gracias."
```
Reemplazo (neutras):
```renpy
    mc_pensamiento "Una de las cinco. Y esta no pidió nada."
```
```renpy
        mc_pensamiento "Con ella empiezo a entender que eso cuenta más que un gracias."
```

**El nombre como hito (respuesta 4).** Hoy el «[mc]...» va pegado a «Puedes buscar tu cuaderno ahora», así que suena a despedida y el MC responde a otra cosa.

Actual (l. 369–373):
```renpy
    itsuki "Puedes buscar tu cuaderno ahora."

    itsuki "[mc]..."

    mc "Ya lo sé. No me voy a ir todavía."
```
Reemplazo:
```renpy
    itsuki "Puedes buscar tu cuaderno ahora."

    mc "Ya lo sé. No me voy a ir todavía."

    itsuki "…Como quieras, [mc]."

    narrador "Era la primera vez que decía mi nombre desde el día del asiento."
```

---

### P7 · Media · La reacción cálida contradice la apertura y su propia identidad

`02_cap1_conexiones.rpy` · `reaccion_itsuki` · l. 468–470

Actual:
```renpy
        itsuki "Hoy no me senté en tu sitio."

        itsuki "Aprendo rápido. Es lo único que se me da bien."
```
**Qué falla:**
- Ya le dejó el sitio libre en la apertura, así que «hoy no» no tiene sentido; y si su evento cae en el hub 3, el comentario llega semanas tarde.
- «Aprendo rápido» contradice el núcleo del personaje: es la que tarda el doble.

**Reemplazo.** Mantiene la familia del eco («es lo único que…») y no depende del hueco:
```renpy
        itsuki "Ayer me viste equivocarme. No va a ser costumbre."

        itsuki "Corrijo rápido. Es lo único que se me da bien."
```

---

### P8 · Media · La libreta de la casa supone el orden y le pone un tema de Ichika

`02_cap1_beat_casa.rpy` · `bcl_itsuki` · l. 972–978 y l. 1010

Actual (l. 972 y 974):
```renpy
            mc_pensamiento "Unos días después subí a la azotea y estaba ahí, con el cuaderno cerrado sobre las rodillas."
```
```renpy
            if not itsuki_visitada_cap1:
```
**Qué falla:** si su evento fue en el hub 2 o 3, la azotea fue **antes**, no «unos días después», y el círculo a lápiz sí se vio en el beat aunque hoy esté visitada.
Reemplazo:
```renpy
            mc_pensamiento "En la azotea la encontré con el cuaderno cerrado sobre las rodillas."
```
```renpy
            if hub_visitadas[0] != "itsuki":
```

Actual (l. 1010):
```renpy
                mc_pensamiento "Y tampoco sé cómo hacer que deje de fingir que está bien."
```
**Qué falla:** «fingir que está bien» es la máscara de Ichika. Itsuki no finge estar bien: finge **no necesitar ayuda**.
Reemplazo:
```renpy
                mc_pensamiento "Y no sé cómo ofrecerle ayuda sin que la tome como una derrota."
```

---

### P9 · Media · La interconexión 3 la describe como alguien que no lo intenta

`02_cap1_conexiones.rpy` · `cap1_interconexion_3` · l. 1631–1637 (rama `not itsuki_visitada_cap1`)

Actual:
```renpy
        mc_pensamiento "No era difícil. Ella lo resolvería con los ojos cerrados."

        mc_pensamiento "Y llevaba días hundiendo el papel con el lápiz sin intentarlo de verdad."

        mc_pensamiento "Eso no es falta de talento."

        mc_pensamiento "Es miedo a equivocarse delante de alguien."
```
**Qué falla:** su herida es justo la contraria: «Yo no tengo esa excusa». Lo intenta y aun así falla. Además, en la azotea estaba sola, así que el «delante de alguien» tampoco encaja.
**Reemplazo.** Siembra el «dónde mirar» que el E6 paga:
```renpy
        mc_pensamiento "No era difícil. Un paso de conversión, nada más."

        mc_pensamiento "Y llevaba días repasándolo sin ver dónde se le torcía."

        mc_pensamiento "Eso no es falta de esfuerzo."

        mc_pensamiento "Es que nadie le ha dicho dónde mirar. Y ella no va a pedirlo."
```

---

### P10 · Media · En los boletines del E6 su voz se vuelve genérica

`02_cap1_evento6.rpy` · `e6_mesa` · l. 3716–3720

Actual:
```renpy
    itsuki "Debería decir algo acorde a este momento."

    itsuki "...Estoy pensando qué decir, pero no tengo ni idea."

    itsuki "Lo que siento no lo puedo expresar con palabras."
```
**Qué falla:** son frases que podría decir cualquiera. Es el gran momento del capítulo y aquí debería aparecer su recurso: la oración que no se cierra, esta vez por alegría.
**Reemplazo** (la l. 3722, «Anótenlo, provisionalmente…», se queda igual):
```renpy
    itsuki "Debería decir algo acorde al momento. Algo con sujeto, verbo y—"

    narrador "No le salió el punto. Por una vez, no pareció importarle."
```

---

### P11 · Media-baja · Otras hermanas usan el tic de Itsuki

Si Nino y Miku hablan en clave de «dato», el recurso deja de ser de Itsuki. *(Son líneas de sus sesiones; las dejo aquí porque afectan a la identidad de Itsuki.)*

`02_cap1_evento6.rpy` · `e6_lunes` · l. 418 (Nino). Actual:
```renpy
        nino "No viniste a buscarme y tampoco te fuiste. ...No es un cumplido. Es un dato."
```
Reemplazo:
```renpy
        nino "No viniste a buscarme y tampoco te fuiste. ...No es un cumplido. No lo repitas."
```

`02_cap1_evento6.rpy` · `e6_miku_eco_no_visitada` · l. 3486 (Miku). Actual:
```renpy
            miku "...La silla sigue vacía. ...No es un reproche. ...Es información."
```
Reemplazo:
```renpy
            miku "...La silla sigue vacía. ...No es un reproche. ...Solo está ahí."
```

---

### P12 · Media-baja · En la interc. 4 acusa como lo haría Nino

`02_cap1_conexiones.rpy` · `cap1_interconexion_4` · l. 2199

Actual:
```renpy
    itsuki "Tú tienes algo que ver con esto, estoy segura."
```
**Qué falla:** «estoy segura» es una intuición, y eso es más de Nino. Itsuki empuja el conflicto **con lógica**, y eso además sigue bien su «Es un hecho» de dos líneas antes.
Reemplazo:
```renpy
    itsuki "Y la hipótesis más probable eres tú."
```

---

### P13 · Baja · Registro: la cortesía del canon (respuesta 2)

Conservo el tú y quito lo coloquial. Así sus enojos suenan **educados y cortantes**, como en el original.

| Archivo · label · l. | Actual | Reemplazo |
|---|---|---|
| `01_prologo.rpy` · 803 | `itsuki_inicio "¿Qué demonios haces en mi casa?"` | `itsuki_inicio "¿Se puede saber qué haces en mi casa?"` |
| `01_prologo.rpy` · 813 | `itsuki_inicio "¿Me estuviste siguiendo desde la escuela? ¿Eres un acosador?"` | `itsuki_inicio "¿Me seguiste desde la escuela? Eso tiene un nombre, y es acoso."` |
| `01_prologo.rpy` · 859 | `itsuki "¡Ichika, no te le acerques! Es el idiota del asiento de la escuela."` | `itsuki "¡Ichika, no te le acerques! Es el maleducado del asiento."` |
| `conexiones` · `reaccion_itsuki` · 530 | `itsuki "Sí. Y es un fastidio."` | `itsuki "Sí. Y es una costumbre desagradable."` |
| `conexiones` · `interconexion_1` · 1015 | `itsuki "Seguro es explotarnos estudiando todos los días y todas las noches."` | `itsuki "Supongo que consiste en hacernos estudiar de día y de noche."` |
| `conexiones` · `interconexion_6` · 2995 | `itsuki "El trabajo es pesado, ¿no?"` | `itsuki "El trabajo resultó más pesado de lo que creías."` |
| `conexiones` · `interconexion_6` · 3100 | `itsuki "Pues hoy no queda nada que adivinar."` | `itsuki "Por lo tanto, hoy no queda nada que adivinar."` |
| `conexiones` · `interconexion_6` · 3120 | `itsuki "Y todas pensábamos lo mismo, ¿no?"` | `itsuki "Y todas pensábamos lo mismo. No hace falta votarlo."` |

Cada fila es una sustitución de una sola línea, con la indentación del original. La l. 399 del E6 ya va corregida en P4.

---

### P14 · Baja · La muletilla del informe se amontona en el E6

En la ruta cálida, el jugador oye «procedimiento» (×2), «informe» (×2), «registro» y «dato» en una sola semana, y antes del E6 solo una vez («Es un hecho», interc. 4). Los dos «procedimiento» son un eco buscado (lo piensa y luego lo dice en voz alta): se quedan. Quito un «informe».

`02_cap1_evento6.rpy` · `e6_tarde_pregunta` · l. 2521. Actual:
```renpy
            itsuki "Falta un informe. ¿Y a ti cómo te fue?"
```
Reemplazo:
```renpy
            itsuki "Falta un resultado. ¿Y a ti cómo te fue?"
```
Para que el tic no parezca nacer en el E6, P12 ya añade un «hipótesis» en la interc. 4 y N1 añade una «deuda» que ella **anota**.

---

### P15 · Baja · Prólogo: «apellido» frente a nombre

`01_prologo.rpy` · `prologo` · l. 492

Actual:
```renpy
    mc_pensamiento "Ella conocía mi apellido por el examen, pero no intercambiamos una sola palabra más."
```
**Qué falla:** ella le dijo «tú debes ser [mc]» (nombre, no apellido). Además, esta línea es el punto de partida del hito del nombre (respuesta 4).
Reemplazo:
```renpy
    mc_pensamiento "Ella sabía mi nombre por el profesor. Yo no sabía el suyo, y no lo pregunté."
```

---

### P16 · Baja · Tres líneas que no se entienden a la primera

`02_cap1_Itsuki.rpy` · `hub_Itsuki` · l. 110 y 158. Actual:
```renpy
    mc "Es tu asignatura."
```
```renpy
    mc_pensamiento "Está ganando o perdiendo tiempo."
```
Reemplazo:
```renpy
    mc "Soy tu tutor."
```
```renpy
    mc_pensamiento "No está pensando. Está esperando a que el error se corrija solo."
```

`02_cap1_apertura.rpy` · `cap1_apertura` · l. 87. Actual:
```renpy
    itsuki "Tienes el mismo horario que yo desde ayer."
```
Reemplazo:
```renpy
    itsuki "Mi padre nos dio tu horario anoche."
```

---

### P17 · Baja · Interc. 6: el MC responde a una pregunta que nadie hizo

`02_cap1_conexiones.rpy` · `cap1_interconexion_6` · l. 2989–2991

Actual:
```renpy
    mc "¿Ya?"

    mc "Obviamente que lo sabía, señora obvia."
```
Reemplazo:
```renpy
    mc "¿Ya?"

    itsuki "Era la última tarde libre. No quedan más."

    mc "Ya lo sabía, señora obvia."
```

---

### P18 · Baja · Erratas y líneas largas en sus escenas

| Archivo · l. | Actual | Reemplazo |
|---|---|---|
| `evento6` · 1378 | `narrador "La penultima prueba de cinco."` | `narrador "La penúltima prueba de cinco."` |
| `evento6` · 1510 | `…Era hacerlo por mi misma."` | `…Era hacerlo por mí misma."` |
| `evento6` · 2408 | `itsuki "Tarde. Pero todo lo hize yo."` | `itsuki "Tarde. Pero todo lo hice yo."` |
| `evento6` · 3515 | `narrador "Aun había cosas pendientes que teníamos que resolver."` | `narrador "Aún había cosas pendientes que teníamos que resolver."` |
| `conexiones` · 2612 | `mc "Saldrán. Confía en tí."` | `mc "Saldrán. Confía en ti."` |
| `conexiones` · 2634 | `itsuki "Y con esa cara de que quieres intrometerte."` | `itsuki "Y quita esa cara de querer intrometerte."` |
| `conexiones` · 3151 | `…En la semana de examenes se lo agradeceremos…` | `…En la semana de exámenes se lo agradeceremos…` |
| `beat_Itsuki` · 207 | `narrador "Los dos volvieron a mirar al frente, …"` | `narrador "Los dos volvimos a mirar al frente, …"` (el narrador es el MC) |
| `beat_Itsuki` · 237 | `"En que a este paso me va a tocar traer los libros hasta al baño.":` | `"En que a este paso me va a tocar traer los libros hasta el baño.":` |

Líneas de más de ~100 caracteres en sus escenas (divídelas así):

`02_cap1_beat_Itsuki.rpy` · l. 61:
```renpy
        narrador "Un solo ejercicio, con un círculo a lápiz alrededor."

        narrador "Repasado tantas veces que había hundido el papel."
```
`02_cap1_beat_Itsuki.rpy` · l. 165:
```renpy
    narrador "El viento seguía soplando igual que siempre aquí arriba."

    narrador "Pero por debajo de él comenzó a percibirse otra cosa..."
```
`02_cap1_beat_casa.rpy` · l. 932:
```renpy
                    mc_pensamiento "Al día siguiente me contó que había rehecho el ejercicio desde el principio."

                    mc_pensamiento "Sin mirar la corrección."
```

---

### P19 · Baja · Dos remates del E6 que sobran o se quedan cortos

`02_cap1_evento6.rpy` · `e6_intento` · l. 3545. **Eliminar** (repite la línea 3543 con menos fuerza):
```renpy
    narrador "Así es, parece que eso aún seguirá pendiente."
```
Si aplicas N4, sus líneas van justo en ese hueco.

`02_cap1_evento6.rpy` · `e6_itsuki_eco_no_visitada` · l. 3414. Actual:
```renpy
            narrador "Pero su frase tenía sentimientos.."
```
Reemplazo:
```renpy
            narrador "Pero no sonó a victoria."
```

---

## 4. Líneas nuevas sugeridas

### N1 · Beat azotea: el almuerzo de Raiha (lo glotón + romance suave, **todas las rutas**)

**Dónde:** `02_cap1_beat_Itsuki.rpy` · `beat_Itsuki`, después de l. 223 (`mc_pensamiento "Ahora me importa más no moverme."`) y antes del bloque `## MOVIMIENTO 3`.
**Para qué:**
- Cobra un setup que hoy no se paga: la interc. 2 dice que el MC llega «con el almuerzo de Raiha en la mochila» y que ella sube «sin bolsa de almuerzo».
- Hace legible la ausencia de comida y siembra lo glotón para el Cap. 2.
- Deja una **deuda** que ella anota, conectada con su tic del registro.
- Es un acercamiento sin palabras de amor: comparten comida.

```renpy
    narrador "Entonces sonó algo que no era el viento."

    show itsuki sorprendida at pj(0.5)
    with disolucion_lenta

    itsuki "Eso no fue mi estómago."

    mc "No dije nada."

    itsuki "Lo ibas a decir."

    narrador "Saqué la caja de almuerzo que Raiha me había preparado y la abrí entre los dos."

    mc "Raiha siempre pone de más. Dice que estudio con el estómago vacío."

    show itsuki timida at pj(0.5)
    with disolucion_lenta

    itsuki "No pienso aceptar comida de mi tutor."

    narrador "Lo dijo mirando el arroz. Fijo. Sin parpadear."

    mc "Entonces no es del tutor. Es de Raiha."

    itsuki "...Un bocado. Y queda anotado como deuda."

    narrador "Fueron cuatro bocados. Yo no dije nada. Ella tampoco lo anotó."

    mc_pensamiento "Desde el primer día no la había vuelto a ver comer."

    mc_pensamiento "Comía como si se le hubiera olvidado cuánto le gustaba."

    show itsuki neutral at pj(0.5)
    with disolucion_lenta
```
Assets: todos existen (`itsuki sorprendida`, `itsuki timida`, `itsuki neutral`, `disolucion_lenta`). Si quieres un efecto de estómago, sería `[NUEVO] audio.sfx_estomago`; sin él, el narrador lo resuelve.

---

### N2 · Su evento en el hub 2 o 3: reconoce el ejercicio del círculo (respuesta 9)

**Dónde:** `02_cap1_Itsuki.rpy` · `hub_Itsuki`, después de l. 71 (`mc_pensamiento "Y la misma cifra al final de las tres."`).
**Para qué:** si el jugador ya vio el beat con el círculo a lápiz, el evento lo reconoce y la continuidad se convierte en recompensa. En el hub 1 no se dispara: ahí `hub_visitadas` todavía está vacía.
```renpy
    if len(hub_visitadas) > 0:

        mc_pensamiento "En el margen, un círculo a lápiz. Repasado hasta hundir el papel."

        mc_pensamiento "El ejercicio del diagnóstico. El mismo que se llevó a la azotea."
```

---

### N3 · E6, no visitada: la promesa cobra la deuda (requiere N1)

**Dónde:** `02_cap1_evento6.rpy` · `e6_itsuki_promesa`, antes de l. 1618 (`mc_pensamiento "No lo apunté. Pero voy a subir con comida para dos, …"`).
**Para qué:** la «comida para dos» deja de ser un detalle suelto y queda enlazada con la azotea. Es el gancho glotón que el Cap. 2 puede cobrar.
```renpy
    mc_pensamiento "Todavía me debe cuatro bocados del almuerzo de Raiha. No pienso cobrárselos."
```

---

### N4 · Romance B · La disculpa interrumpida (todas las rutas buenas)

**Dónde:** `02_cap1_evento6.rpy` · `e6_intento`, en lugar de la l. 3545 que elimina P19, justo antes de `$ e6_disculpa_pendiente = True`.
**Para qué:** el amor-odio se nota en el cuerpo, sin decirse nada. «Esta vez sí lo anoto» le da la vuelta a su «Y no lo apuntes en ningún sitio».
```renpy
    call e6_foco("itsuki", "timida")

    itsuki "...Queda pendiente."

    itsuki "Esta vez sí lo anoto."

    narrador "Lo dijo sin mirarme. Pero se le habían puesto rojas las orejas."

    call e6_foco("", "")
```

---

### N5 · Romance C · El nombre firmado (solo cálida, respuestas 4 y 7)

**Dónde:** `02_cap1_evento6.rpy` · `e6_itsuki_eco_calida`.

Cambia la l. 3348. Actual:
```renpy
            itsuki "Eso no se pregunta."
```
Reemplazo:
```renpy
            itsuki "Eso no se pregunta, [mc]."
```
E inserta después del bloque `if it1_frase() == "A": … else: …` y antes de `call e6_foco("", "")` (l. 3358):
```renpy
            narrador "Dijo mi nombre como quien firma al pie de un informe."

            narrador "Y aun así tardó en soltar el bolígrafo."
```
Va en narración y en diálogo, no en `itsuki_int`, para respetar tu decisión P-11 (la voz interior del E6, sin romance).

---

## 5. Fortalezas (no tocar)

- **La oración cerrada como recurso.** Está bien definida, el narrador la señala en el momento justo (queja l. 888, eco tibia del E6) y el E6 la paga.
- **El motivo del error arrastrado.** La misma conversión de unidades une el diagnóstico, el aula, la azotea, el Final B y el E6. El espejo B/E6 funciona («El mismo problema del primer día»).
- **La regla que se invierte.** «Ni se te ocurra decirme la respuesta» se convierte en «Levantar la mano no es un favor. Es un procedimiento». Es el mejor arco de una sola línea del capítulo.
- **`queja_itsuki` entera.** «No inmediatamente. / Y no lo apuntes en ningún sitio» resume tu amor-odio en dos líneas.
- **Las tres ramas del evento son la misma chica.** La fría castiga el gesto y no la intención; la tibia deja el «…Todavía. / Es una expresión. No es una promesa», que luego sostiene todo su eco del E6.
- **La disciplina con la disculpa.** No se gasta en el hub, el Final B la gasta tarde y el E6 la interrumpe y la deja como gancho.
- **El beat de la azotea**: mucha contención («No se cortó a media idea. La terminó»), y es el único sitio que le queda.
- **El eco «Al menos eres honesto»** en los dos menús del prólogo.
- **«…Gracias»** a Nino en la sesión de casa: su primer agradecimiento va para una hermana, no para el MC. Es el orden correcto.

---

## 6. Veredicto

### 6.1 Notas
| Eje | Nota | Por qué |
|---|---|---|
| Identidad | **8/10** | Se la reconoce por la voz sin ver la placa. Le resta la Itsuki cómica y glotona (ausente) y algunas líneas de grupo genéricas. |
| Coherencia | **6/10** | Ningún fallo de carácter grave, pero sí **costuras de orden** (P1, P6, P8) y **ramas ciegas** en el final malo (P2, P3) que el jugador nota. |
| Progresión | **8/10** | Hay un antes y un después claro con detonantes en pantalla, en las cuatro rutas. La cálida es la más redonda; la no visitada también avanza gracias a la queja y la promesa. |

### 6.2 Conclusión

Al cerrar el Cap. 1, el jugador sabe quién es Itsuki: la que estudia más que nadie y no pregunta. Nota que algo cambió en ella, porque la frase final del arco es literalmente su miedo superado. Y le quedan ganas de seguirla gracias a la disculpa pendiente, que es un gancho limpio. El problema no es el personaje sino la **fontanería**: con tres huecos para cinco eventos, varias líneas suponen que su evento fue el primero, y el final malo no comprueba qué rama jugaste. Arreglado eso, el único hueco real es tonal: le falta un momento ligero que haga legible la «glotona apagada», y N1 lo cubre sin CG ni assets nuevos mientras deja la deuda para las citas del Cap. 2.

### 6.3 Las tres correcciones de mayor impacto
1. **P1 (y P6, P8):** blindar el orden con `hub_visitadas[0]` y frases neutras. Es lo que más se nota al rejugar.
2. **P2 + P3:** líneas del final malo según la rama. Ahora mismo le mienten al jugador que fue cálido.
3. **P5 + N1:** reescribir la propuesta del juego (Itsuki deja de ser un instrumento de la trama y empuja con lógica) y añadir el almuerzo de la azotea (lo glotón, el amor-odio y el gancho del Cap. 2).

### 6.4 Para el Cap. 2 (respuesta 6)

Para saber en qué «fase» llega Itsuki no hace falta crear variables. Ya tienes:
- `itsuki_visitada_cap1` / `rama_de("itsuki")`: fase 1 (no visitada) o fase 2, y con qué tono.
- `e6_disculpa_pendiente`: la disculpa de los dos sigue abierta.
- `e6_promesas` (no visitada): la subida a la azotea con comida para dos.
- Con N1, la «deuda de cuatro bocados» existe en **todas** las rutas, así que una primera cita en la que coman juntos tiene un motivo dentro del juego en cualquier partida.

---

## 7. Avisos

- **Puntos:** ninguna propuesta toca `sumar_punto`, `desaires_cap1`, `primera_conexion` ni las ramas. Los condicionales nuevos solo **leen** `hub_visitadas`, `rama_de()` e `itsuki_rama_cap1`.
- **Variables nuevas:** ninguna. **Assets nuevos:** ninguno obligatorio (solo el opcional `[NUEVO] audio.sfx_estomago` de N1).
- **Diferencias .md / .rpy:** el borrador del beat (`CAP1_beat_itsuki.md`) condicionaba la línea «Ya me ayudaste» con `primera_conexion == "itsuki"`; el `.rpy` usa la visita. El borrador del evento decía «sin cambiar una línea» pero ya incluía «Llevo dos días». Las dos intenciones se resuelven con P1 y P6.
- **Fuera del alcance de Itsuki (lo anoto para la sesión que toque):**
  - Cronología: el beat y la interc. 3 dicen «Quedan casi tres semanas», luego pasan «10 días» y el hub 2 vuelve a decir «tres semanas».
  - Los comentarios de la cabecera de `02_cap1_evento6.rpy` y de su l. 3034 todavía dicen que Itsuki es un stub (Chat 9), aunque su bloque ya está montado entero.
