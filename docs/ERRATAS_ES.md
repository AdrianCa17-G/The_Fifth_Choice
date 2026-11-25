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
