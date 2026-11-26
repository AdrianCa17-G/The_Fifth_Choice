# Erratas del texto en español

El español de la v1.0 está **congelado** durante la traducción (regla 1 del plan). Ren'Py enlaza cada traducción
al hash de la línea original: si se corrige una línea en español, su traducción en `game/tl/english/` (y luego en
`tl/russian/`) queda huérfana.

Por eso las erratas **no se corrigen al encontrarlas**: se anotan aquí y se corrigen todas juntas al final de la
fase, regenerando después la traducción de esas líneas (Generate Translations) y revisando que no quede ninguna
huérfana.

Formato: una fila por errata. «Archivo:línea» tal como está en el momento de anotarla.

| Archivo:línea | Texto actual | Corrección | Anotada por / fecha |
|---|---|---|---|
| `08_extras.rpy:17` | «Un encuentro incomodo» | «Un encuentro incómodo» | Claude, 23/11/2026 |
| `08_extras.rpy:38` | «No puedo mas» | «No puedo más» | Claude, 23/11/2026 |
| `08_extras.rpy:44` | «Una receta con transfondo» | «Una receta con trasfondo» | Claude, 23/11/2026 |
| `08_extras.rpy:56` | «Quiero usar mis audifonos» | «Quiero usar mis audífonos» | Claude, 23/11/2026 |
| `08_extras.rpy:1198` | «Diviértete jugandolos.» | «Diviértete jugándolos.» | Claude, 23/11/2026 |
| `02_cap1_evento6.rpy:1895` + `07_ui.rpy` / `13_transiciones.rpy` | HUD «Quedan [tiempo_restante!t]» con «un examen» → «Quedan un examen» | «Queda un examen». Arreglo propuesto: la plantilla del HUD distingue singular, o el valor pasa a «solo un examen» con «Queda». En inglés no afecta ("one exam left"). | Claude, 23/11/2026 |
| `02_cap1_apertura.rpy:275` | «Es una observación minuiciosa.» | «Es una observación minuciosa.» | Claude, 24/11/2026 |
| `02_cap1_Itsuki.rpy:148` | «Cuando Itsuki tiene la respuesta, no repite la pregunta con la misma frase.» | «...no repite la respuesta con la misma frase.» (repite su respuesta, no la pregunta). En inglés se tradujo por el sentido: "she never repeats a line word for word". | Claude, 24/11/2026 |
| `02_cap1_conexiones.rpy:491` | «Anoche rehíce el ejercicio.» | «Anoche rehice el ejercicio.» (sin tilde) | Claude, 25/11/2026 |
| `02_cap1_conexiones.rpy:580` | «Lo rehíciste.» | «Lo rehiciste.» (sin tilde) | Claude, 25/11/2026 |
| `02_cap1_conexiones.rpy:2685` | «Esa semana si es importante...» | «Esa semana sí es importante...» | Claude, 25/11/2026 |
| `02_cap1_conexiones.rpy:3108` | «Adios.» (quintillizas) | «Adiós.» | Claude, 25/11/2026 |
| `02_cap1_conexiones.rpy:3430` | «...Pero pensandolo bien.» | «...Pero pensándolo bien.» | Claude, 25/11/2026 |
| `02_cap1_conexiones.rpy:3455` | «Ya lo veremos en la semana de examenes.» | «...en la semana de exámenes.» | Claude, 25/11/2026 |
| `02_cap1_conexiones.rpy:4021` | «Ni siquiera se tomaron la molestia en contestarme» | Falta el punto final: «...en contestarme.» | Claude, 25/11/2026 |
| `02_cap1_conexiones.rpy:4091` | `_("Casa de Futaro")` (nombre fijo) | `_("Casa de [nombre_jugador]")`, como ya hace «Habitación de [nombre_jugador]» en `07_ui.rpy`. Si el jugador cambia el nombre, el cartel sigue diciendo «Futaro». En inglés ya va con `[nombre_jugador]`. | Claude, 25/11/2026 |
| `02_cap1_evento6.rpy:1481` | «No. Aun me falta revisar unas cosas.» (Nino) | «No. Aún me falta revisar unas cosas.» (sin tilde en «Aún») | Claude, 25/11/2026 |
| `screens.rpy:1212-1217` (Ayuda → Teclado) | «Av. pág.» → «Retrocede al diálogo anterior.» y «Re. pág.» → «Avanza hacia el diálogo siguiente.» | Las teclas están cruzadas: Re. pág. (Page Up) retrocede y Av. pág. (Page Down) avanza. Basta con intercambiar las dos etiquetas. En inglés ya va bien ("Page Up · Rolls back…", "Page Down · Rolls forward…"). | Claude, 26/11/2026 |
| `08_extras.rpy:1002` | `_("El climax")` (Extras → Animaciones) | «El clímax» | Claude, 26/11/2026 |
