# SFX v1.1 — propuesta (sin aplicar)

Mezcla calculada con el código de Ren'Py 8.5.3: archivo × volume × mezclador × 0,707, recorte duro a 0 dB;
música por defecto a -12 dB. Los niveles suponen los controles sin tocar. Descripciones: modelos de audio.

## 1. Filas para aprobar

| # | archivo:línea | Escena | Efecto | Ahora | Propuesta | Por qué |
|---|---|---|---|---|---|---|
| 1 | 01_prologo:406 · Miku:531 · evento6:1415 | Mordisco de Itsuki, Miku recoge los libros, Nino se levanta | silla | 2.5 | `volume 1.5` | A 2.5 suena casi tan fuerte como el portazo (-13,3 frente a -12,6) y recorta. |
| 2 | 01_prologo:837 | Miku llega con la compra | bolsa | 2.5 | `volume 1.5` | Igual de fuerte que el portazo; a 1.5 queda como la bolsa de Nino:94. |
| 3 | 01_prologo:168 · Miku:123 y 186 · apertura:223 | Papeles sobre la mesa | papel_mesa | 2.5 | `volume 1.5` | Recorta (+3,9 dB). El 2.5 es anterior a normalizar el archivo. |
| 4 | beat_Nino:252 | Taza «con más fuerza de la necesaria» | taza_mesa | 2.0 | `volume 1.5` | Supera al portazo (-11,7). A 1.5 sigue más fuerte que las otras tazas. |
| 5 | Itsuki:314 y 428 | Tacha la línea / resuelve con su lápiz | lapiz_mesa | 1.0 | `volume 2.0` | Casi se confunde con la música (1 dB sobre sus partes fuertes). |
| 6 | 01_prologo:452 (nueva, antes) | «La puerta de la azotea se abrió» | puerta_abre | mudo | `play sound audio.sfx_puerta_abre volume 1.2` | Suceso narrado en presente, sin sonido. |
| 7 | beat_Nino:284 (nueva) | «Se sentó en uno de los bancos, de golpe» | silla | mudo | `play sound audio.sfx_silla volume 1.5` | El golpe marca que le fallan las piernas. |
| 8 | Ichika:244 (nueva) | «Pasó una página sin leerla» | hoja | mudo | `play sound audio.sfx_hoja` | Suave, un diálogo después de la silla. |
| 9 | evento6:726 (nueva) | «Yotsuba soltó el lápiz» | lapiz_mesa | mudo | `play sound audio.sfx_lapiz_mesa volume 2.0` | Tras el minijuego, sobre silencio. |
| 10 | evento6:1347 (nueva) | «Dejó el lápiz sobre la mesa con cuidado» | lapiz_mesa | mudo | `play sound audio.sfx_lapiz_mesa volume 1.5` | Igual, más suave. |
| 11 | evento6:3503 (nueva) | Nino llega con bolsas | bolsa | mudo | `play sound audio.sfx_bolsa volume 1.5` | La bolsa solo se usa dos veces. |
| 12 | evento6:2076 -> antes de :2058 | «Cuando sonó el timbre, su hoja estaba llena» | timbre | suena al final | mover la línea `play sound` | El texto lo pone al principio y la escena sigue después. |

## 2. Archivos

| Archivo | Duración | Pico | A qué suena (earshot) | Nota |
|---|---|---|---|---|
| acierto | 0.36 s | -1.2 dB | a success chime (z +3.8), a kalimba note (z +2.8), a snare hit (z +2.7) |  |
| bolsa | 1.0 s | -1.1 dB | walking through dry leaves (z +4.0), paper rustling (z +3.2), leaves rustling (z +3.1) |  |
| camara | 0.55 s | -4.6 dB | a camera shutter click (z +4.7), a phone vibration buzz (z +3.1), a single mechanical keyboard key press (z +2.2) |  |
| celular | 1.17 s | -12.3 dB | an error buzz (z +2.9), a digital glitch (z +2.8), an alarm clock beeping (z +2.5) | **escúchalo**: se lee como pitido de error (86 %), no como vibración (<1 %) |
| click | 3.04 s | -9.7 dB | a success chime (z +3.7), a magic sparkle chime (z +2.2), a notification ding (z +2.2) |  |
| correr | 5.93 s | -6.4 dB | high heels walking (z +3.0), a horse galloping (z +2.9), footsteps on wood (z +2.9) |  |
| cort_capitulo | 6.8 s | -2.9 dB | a success chime (z +3.3), a kalimba note (z +2.6), a glockenspiel run (z +2.4) |  |
| cort_completado_fria | 0.8 s | -12.3 dB | a kick drum (z +3.9), a snare hit (z +3.2), a punchy impact hit (z +2.5) | unos 18 dB bajo las demás cortinillas; confirma que es a propósito |
| cort_completado_ichika | 3.2 s | -3.0 dB | a success chime (z +4.0), a kalimba note (z +3.1), a magic sparkle chime (z +2.3) |  |
| cort_completado_ichika_tibia | 1.9 s | -6.0 dB | a success chime (z +3.7), a doorbell (z +2.9), a notification ding (z +2.8) |  |
| cort_completado_itsuki | 3.2 s | -3.0 dB | a success chime (z +4.1), a kalimba note (z +2.9), a glissando on bar chimes (z +2.8) |  |
| cort_completado_itsuki_tibia | 1.9 s | -6.1 dB | a success chime (z +3.5), a doorbell (z +3.4), a notification ding (z +2.9) |  |
| cort_completado_miku | 3.2 s | -2.8 dB | a success chime (z +3.4), a kalimba note (z +2.9), a glissando on bar chimes (z +2.9) |  |
| cort_completado_miku_tibia | 1.9 s | -6.0 dB | a success chime (z +3.5), a doorbell (z +3.2), a notification ding (z +2.7) |  |
| cort_completado_nino | 3.2 s | -3.0 dB | a success chime (z +3.7), a kalimba note (z +3.0), a glissando on bar chimes (z +2.9) |  |
| cort_completado_nino_tibia | 1.9 s | -5.9 dB | a success chime (z +3.8), a notification ding (z +2.9), a kalimba note (z +2.8) |  |
| cort_completado_yotsuba | 3.2 s | -3.0 dB | a success chime (z +3.6), a glissando on bar chimes (z +3.3), a glockenspiel run (z +3.0) |  |
| cort_completado_yotsuba_tibia | 1.9 s | -6.0 dB | a success chime (z +3.7), a doorbell (z +3.0), a notification ding (z +2.7) |  |
| cort_examen | 8.2 s | -3.2 dB | a success chime (z +3.2), a glockenspiel run (z +2.5), a kalimba note (z +2.4) |  |
| cort_fin | 6.2 s | -3.1 dB | a success chime (z +3.2), a kalimba note (z +2.9), a music box melody (z +2.5) |  |
| cort_hermana_ichika | 3.8 s | -2.9 dB | a success chime (z +3.6), a glockenspiel run (z +3.0), a music box melody (z +2.9) |  |
| cort_hermana_itsuki | 3.8 s | -2.9 dB | a success chime (z +4.0), a music box melody (z +3.1), a glockenspiel run (z +3.0) |  |
| cort_hermana_miku | 3.8 s | -2.9 dB | a success chime (z +3.5), a glockenspiel run (z +2.6), a music box melody (z +2.6) |  |
| cort_hermana_nino | 3.8 s | -3.1 dB | a success chime (z +3.9), a kalimba note (z +2.7), a glockenspiel run (z +2.5) |  |
| cort_hermana_yotsuba | 3.8 s | -2.9 dB | a success chime (z +3.8), a glissando on bar chimes (z +3.1), a glockenspiel run (z +3.1) |  |
| cort_hub | 3.8 s | -3.0 dB | a success chime (z +3.6), a kalimba note (z +2.9), a glockenspiel run (z +2.6) |  |
| cort_mj_ichika_entrada | 2.6 s | -5.9 dB | a success chime (z +3.9), a kalimba note (z +2.9), a glockenspiel run (z +2.7) |  |
| cort_mj_ichika_ganado | 2.2 s | -5.9 dB | a success chime (z +4.1), a kalimba note (z +2.4), a notification ding (z +2.4) |  |
| cort_mj_ichika_saltado | 1.6 s | -9.5 dB | a success chime (z +3.4), a doorbell (z +2.9), a notification ding (z +2.8) |  |
| cort_mj_itsuki_entrada | 2.6 s | -5.9 dB | a success chime (z +3.9), a doorbell (z +3.0), a glockenspiel run (z +2.6) |  |
| cort_mj_itsuki_ganado | 2.2 s | -6.0 dB | a success chime (z +4.3), a notification ding (z +2.5), a kalimba note (z +2.5) |  |
| cort_mj_itsuki_saltado | 1.6 s | -9.8 dB | a success chime (z +3.4), a doorbell (z +3.3), a notification ding (z +2.8) |  |
| cort_mj_miku_entrada | 2.6 s | -5.8 dB | a success chime (z +3.7), a kalimba note (z +2.8), a doorbell (z +2.8) |  |
| cort_mj_miku_ganado | 1.25 s | -5.9 dB | a music box melody (z +3.3), a kalimba note (z +2.9), a success chime (z +2.9) |  |
| cort_mj_miku_saltado | 1.6 s | -9.5 dB | a success chime (z +3.3), a doorbell (z +3.0), a glass ting (z +2.7) |  |
| cort_mj_nino_entrada | 2.6 s | -6.0 dB | a success chime (z +3.9), a kalimba note (z +2.6), a notification ding (z +2.2) |  |
| cort_mj_nino_ganado | 2.2 s | -5.9 dB | a success chime (z +3.7), a kalimba note (z +2.1), a notification ding (z +2.1) |  |
| cort_mj_nino_saltado | 1.6 s | -10.1 dB | a success chime (z +3.6), a kalimba note (z +2.9), a notification ding (z +2.8) |  |
| cort_mj_yotsuba_entrada | 2.6 s | -6.1 dB | a success chime (z +3.5), a kalimba note (z +3.2), a glissando on bar chimes (z +2.9) |  |
| cort_mj_yotsuba_ganado | 2.2 s | -5.9 dB | a success chime (z +4.3), a notification ding (z +2.9), a kalimba note (z +2.7) |  |
| cort_mj_yotsuba_saltado | 1.6 s | -9.9 dB | a success chime (z +3.5), a kalimba note (z +3.0), a doorbell (z +2.8) |  |
| estomago | 3.58 s | -1.8 dB | a cow mooing (z +3.0), a rubber stretch (z +2.4), a squishy wet squelch (z +2.4) |  |
| fallo | 0.38 s | -1.2 dB | a success chime (z +3.5), a kalimba note (z +3.1), a chat message pop (z +2.3) |  |
| hoja | 0.88 s | -1.0 dB | a quick swipe (z +3.5), a short swish (z +2.8), a page turning (z +2.7) | casi la misma grabación que papel_mesa (parecido 0,99) |
| hover | 1.05 s | -9.7 dB | a kalimba note (z +3.9), a glass ting (z +3.1), a kick drum (z +2.2) |  |
| hub_click | 1.74 s | -12.7 dB | a success chime (z +3.8), a magic sparkle chime (z +3.0), a triangle hit (z +2.3) |  |
| hub_hover | 1.02 s | -11.5 dB | a success chime (z +3.8), a notification ding (z +3.1), a kalimba note (z +2.5) |  |
| lapiz_mesa | 0.84 s | -4.0 dB | dominoes falling (z +3.4), a small object dropping on a table (z +2.9), a wooden block hit (z +2.9) |  |
| manija | 0.82 s | -9.1 dB | a balloon squeak (z +4.4), a finger squeaking on glass (z +3.9), a rubber stretch (z +2.8) | **escúchalo**: se lee como chirrido de globo (>99 % frente a pomo) |
| mochila_suelo | 2.77 s | -0.9 dB | a body falling on the ground (z +4.2), a heavy thud (z +3.7), a punchy impact hit (z +3.1) |  |
| papel_mesa | 0.88 s | -1.1 dB | a quick swipe (z +3.2), a fast whoosh (z +2.8), a page turning (z +2.7) | casi la misma grabación que hoja (parecido 0,99) |
| pisadas_pista | 12.09 s | -7.2 dB | high heels walking (z +3.5), a horse galloping (z +3.5), footsteps on wood (z +3.4) | **escúchalo**: caballo 65 %, carrera 20 %, tacones 15 % |
| portazo | 0.35 s | -0.5 dB | a door slam (z +3.9), an old typewriter (z +3.0), a latch clicking shut (z +3.0) |  |
| puerta_abre | 1.13 s | -5.2 dB | an old typewriter (z +2.9), a squishy wet squelch (z +2.3), a body falling on the ground (z +2.3) | puerta que se abre (85 %) |
| puerta_cierra | 1.01 s | -6.0 dB | a door slam (z +3.6), an old typewriter (z +3.2), a latch clicking shut (z +3.1) |  |
| silla | 1.32 s | -1.0 dB | a big drum hit (z +2.7), a wooden knock (z +2.5), a body falling on the ground (z +2.3) | arrastre de silla (91 %) |
| taza_mesa | 0.47 s | 0.0 dB | a wooden block hit (z +3.4), a small object dropping on a table (z +2.9), a wooden knock (z +2.9) | taza en la mesa (60 %) |
| timbre | 5.75 s | -10.9 dB | a success chime (z +3.8), a kalimba note (z +2.5), a celesta note (z +2.5) |  |
| toque_puerta | 0.58 s | -1.0 dB | a knock on a door (z +3.3), a wooden knock (z +3.2), a punchy impact hit (z +2.8) |  |

## 3. Mapa de efectos (121 llamadas en el guion)

«Nivel» son los 0,4 s más fuertes; en golpes cortos queda por debajo de lo que se oye. «Fondo» es la media de la pista.

| archivo:línea | Efecto | volume | Pico real | ms recortados | Nivel / fondo (dB) | Línea siguiente |
|---|---|---|---|---|---|---|
| 01_prologo:168 | papel_mesa | 2.5 | +3.9 | 1 | -16 / extraneza: -34.0 | De repente, mi padre, Isanari, entró en el comedor y dejó caer un pape |
| 01_prologo:312 | timbre | 1.5 | -10.4 | 0 | -18 / silencio | A la mañana siguiente llegué al instituto antes que casi nadie. |
| 01_prologo:406 | silla | 2.5 | +4.0 | 3 | -14 / incomodo: -31.5 | La chica apretó los dientes y masticó el último bocado a la fuerza. |
| 01_prologo:582 | toque_puerta | 1.5 | -0.5 | 0 | -20 / cotidiano: -28.2 | Toqué la puerta con cuidado y, tras unos segundos, escuché una voz des |
| 01_prologo:599 | manija | 1.5 | -8.5 | 0 | -25 / silencio | Apenas puse la mano sobre el pomo, la puerta se abrió desde el otro la |
| 01_prologo:607 | puerta_abre | 1.5 | -4.7 | 0 | -16 / silencio | Apareció una chica de sonrisa fácil. |
| 01_prologo:767 | correr | 1.75 | -4.6 | 0 | -29 / extraneza: -34.0 | Algo me pasó por al lado a toda velocidad antes de que pudiera reaccio |
| 01_prologo:825 | portazo | 2.5 | +4.4 | 3 | -14 / extraneza: -34.0 | Antes de que pudiera terminar la palabra, la puerta al fondo del pasil |
| 01_prologo:837 | bolsa | 2.5 | +3.9 | 0 | -17 / caos: -33.1 | Se detuvo en seco a mitad del pasillo, congelada con la bolsa del supe |
| 01_prologo:1000 | puerta_abre | 1.0 | -8.2 | 0 | -20 / silencio | Cuando la figura de su padre apareció en el umbral. |
| 01_prologo:1079 | puerta_cierra | 1.0 | -9.0 | 0 | -27 / silencio | Se dio la vuelta y se fue, cerrando la puerta con calma. |
| 01_prologo:1120 | hoja | 2.0 | +2.1 | 0 | -19 / silencio | Una hoja con un diagnóstico rápido de veinte preguntas. |
| 01_prologo:1185 | puerta_cierra | 2.0 | -3.0 | 0 | -21 / silencio | Agarró su hoja sin tocar el lápiz y se retiró a su habitación, cerrand |
| 01_prologo:1198 | puerta_cierra | 1.2 | -7.4 | 0 | -26 / silencio | Miku ni se molestó en dar explicaciones. |
| 01_prologo:1204 | puerta_cierra | 1.2 | -7.4 | 0 | -26 / silencio | Yotsuba, aplastada por la culpa de ver a las demás irse, me pidió perd |
| 01_prologo:1210 | puerta_cierra | 1.2 | -7.4 | 0 | -26 / silencio | En menos de diez minutos, la mesa quedó vacía. |
| Ichika:76 | hoja | 2.0 | +2.1 | 0 | -19 / ichika: -32.7 | El guion terminó de resbalarle de la mano y cayó al piso. |
| Ichika:179 | hoja | 1.0 | -4.0 | 0 | -25 / ichika: -32.7 | Guardó el horario doblándolo rápido. |
| Ichika:240 | silla | 1.2 | -2.4 | 0 | -20 / silencio | Se sentó en una de las sillas plegables. |
| Ichika:492 | celular | 1.5 | -11.8 | 0 | -18 / descubrimiento: -32.9 | Se estaba colgando la mochila cuando le vibró el teléfono en el bolsil |
| Itsuki:105 | hoja | 2.0 | +2.1 | 0 | -19 / itsuki: -32.6 | Pasó a una hoja nueva del cuaderno, tapando la anterior con la mano. |
| Itsuki:210 | mochila_suelo | 1.5 | -0.4 | 0 | -18 / silencio | Dejé la mochila en el suelo. |
| Itsuki:314 | lapiz_mesa | 1.0 | -7.0 | 0 | -34 / descubrimiento: -32.9 | Tachó la línea entera, no solo el número. |
| Itsuki:428 | lapiz_mesa | 1.0 | -7.0 | 0 | -34 / descubrimiento: -32.9 | Lo resolví ahí mismo, de pie, con su propio lápiz. |
| Miku:80 | silla | 1.0 | -4.0 | 0 | -22 / miku: -32.9 | Me senté enfrente. |
| Miku:123 | papel_mesa | 2.5 | +3.9 | 1 | -16 / miku: -32.9 | Saqué el temario de sociales y lo puse sobre la mesa, girado hacia ell |
| Miku:186 | papel_mesa | 2.5 | +3.9 | 1 | -16 / miku: -32.9 | Lo reconoció antes de que llegara a la mesa. |
| Miku:531 | silla | 2.5 | +4.0 | 3 | -14 / descubrimiento: -32.9 | Recogió los cuatro libros, los apiló y se subió los audífonos. |
| Nino:94 | bolsa | 1.5 | -0.6 | 0 | -21 / nino: -30.7 | El ruido del plástico la hizo detenerse en seco. |
| Nino:512 | celular | 1.0 | -15.3 | 0 | -21 / silencio | Casi en la puerta, el celular de Nino sonó. |
| Yotsuba:74 | pisadas_pista | 1.75 | -5.4 | 0 | -19 / yotsuba: -32.1 | ¡Veintidós! ¡Esto es fácil! ¡Podría hacer cien! ¡Bueno, quizás no cien |
| Yotsuba:464 | pisadas_pista | 1.75 | -5.4 | 0 | -19 / descubrimiento: -32.9 | Salió disparada. Era rápida de verdad. |
| Yotsuba:579 | pisadas_pista | 1.75 | -5.4 | 0 | -19 / descubrimiento: -32.9 | Pero cuando llegué, ella ya había vuelto a la pista. |
| apertura:35 | timbre | 1.5 | -10.4 | 0 | -18 / silencio | Dormí cuatro horas. No por estudiar, por primera vez en meses. |
| apertura:152 | toque_puerta | 1.5 | -0.5 | 0 | -20 / silencio | Toqué a las 4 en punto. |
| apertura:156 | puerta_abre | 1.5 | -4.7 | 0 | -16 / silencio | Me abrió Ichika, otra vez, con la misma sonrisa de la primera vez. |
| apertura:223 | papel_mesa | 2.5 | +3.9 | 1 | -16 / extraneza: -34.0 | Repartí el ejercicio. |
| apertura:237 | hoja | 2.0 | +2.1 | 0 | -19 / extraneza: -34.0 | Corregí la primera hoja. Seis de seis mal. |
| apertura:392 | puerta_cierra | 2.0 | -3.0 | 0 | -21 / caos: -33.1 | Las otras tres tardaron menos de un minuto en desaparecer detrás de el |
| apertura:436 | puerta_abre | 1.0 | -8.2 | 0 | -20 / silencio | Estaba recogiendo mis cosas cuando la puerta del fondo se abrió. |
| apertura:471 | puerta_cierra | 1.0 | -9.0 | 0 | -27 / contrato: -31.4 | Se fue igual que ayer, sin subir la voz y sin dejarme contestar. |
| apertura:620 | toque_puerta | 1.5 | -0.5 | 0 | -20 / hogar: -28.3 | Hermanito, llevas media hora mirando unos papeles en blanco. |
| beat_Itsuki:85 | mochila_suelo | 1.5 | -0.4 | 0 | -18 / amb_viento: -38.5 | Me senté a un par de metros, sin decir nada todavía. |
| beat_Itsuki:241 | estomago | 1.5 | -1.3 | 0 | -13 / tregua: -31.9 | Eso no fue mi estómago. |
| beat_Itsuki:341 | timbre | 1.5 | -10.4 | 0 | -18 / silencio | El timbre sonó antes de que ninguno de los dos volviera a abrir un lib |
| beat_Nino:48 | manija | 1.5 | -8.5 | 0 | -25 / silencio | Antes de terminar de abrirla, escuché dos voces desde el fondo. |
| beat_Nino:154 | taza_mesa | 1.0 | -3.0 | 0 | -20 / contrato: -31.4 | Dejó la taza sobre la mesa, sin apurarse. |
| beat_Nino:182 | puerta_cierra | 1.0 | -9.0 | 0 | -27 / contrato: -31.4 | Recogió la taza y salió sin esperar respuesta. A los dos nos dio la es |
| beat_Nino:215 | puerta_cierra | 1.0 | -9.0 | 0 | -27 / guardia: -32.7 | No dijo mi nombre en toda la conversación. |
| beat_Nino:252 | taza_mesa | 2.0 | +3.0 | 5 | -14 / guardia: -32.7 | Dejó su propia taza sobre la mesa con más fuerza de la necesaria. |
| beat_casa:101 | lapiz_mesa | 2.5 | +1.0 | 0 | -26 / cena: -32.5 | Dejó el lápiz sobre la mesa, despacio. |
| beat_casa:154 | puerta_abre | 1.0 | -8.2 | 0 | -20 / silencio | Mi padre entró cuando Raiha ya estaba guardando el cuaderno. |
| beat_casa:218 | puerta_cierra | 1.5 | -5.5 | 0 | -24 / silencio | No dijo suerte. |
| conexiones:936 | timbre | 1.5 | -10.4 | 0 | -18 / silencio | Llegué al instituto temprano, como siempre. |
| conexiones:1416 | timbre | 1.5 | -10.4 | 0 | -18 / silencio | Llegué al instituto con el almuerzo de Raiha en la mochila y la cabeza |
| conexiones:1593 | timbre | 1.5 | -10.4 | 0 | -18 / silencio | El timbre del almuerzo sonó y el aula se vació en segundos. |
| conexiones:1659 | toque_puerta | 1.0 | -4.0 | 0 | -23 / hogar: -28.3 | Mi padre asomó la cabeza. Venía de fotografiar una boda y todavía olía |
| conexiones:2464 | toque_puerta | 1.5 | -0.5 | 0 | -20 / silencio | Hermanito, llegó esto. Lo dejo aquí, ¿sí? |
| conexiones:2575 | celular | 1.0 | -15.3 | 0 | -21 / silencio | Pasadas las 11, me sonó el teléfono. En la pantalla decía «Maruo». |
| conexiones:2645 | timbre | 1.5 | -10.4 | 0 | -18 / silencio | Llegué al instituto temprano, como siempre. |
| conexiones:3281 | timbre | 1.5 | -10.4 | 0 | -18 / silencio | Viernes. El instituto olía distinto: a papel subrayado y estudiantes p |
| conexiones:3727 | puerta_abre | 1.5 | -4.7 | 0 | -16 / silencio | Maruo apareció en la puerta del departamento. |
| conexiones:3751 | puerta_cierra | 1.0 | -9.0 | 0 | -27 / contrato: -31.4 | Cerró con la calma de siempre. |
| conexiones:3771 | puerta_cierra | 1.0 | -9.0 | 0 | -27 / contrato: -31.4 | Cerró con la calma de siempre. |
| conexiones:4036 | puerta_cierra | 1.2 | -7.4 | 0 | -26 / silencio | Pasadas las 8 salí del departamento, después de dejarles las últimas h |
| evento6:205 | timbre | 1.5 | -10.4 | 0 | -18 / silencio | El timbre sonó en un instituto donde nadie hablaba de otra cosa. |
| evento6:521 | hoja | 2.0 | +2.1 | 0 | -19 / silencio | «Si una sola reprueba, se acabó.» Maruo lo dijo en la cocina y no lo r |
| evento6:774 | timbre | 1.5 | -10.4 | 0 | -18 / silencio | Se le detuvo el lápiz a media palabra. Una sola vez. |
| evento6:791 | timbre | 1.5 | -10.4 | 0 | -18 / silencio | Escribió de corrido, sin levantar la vista ni una vez. Fue la primera  |
| evento6:806 | timbre | 1.5 | -10.4 | 0 | -18 / silencio | Resolvió su hoja sin dramas. A la mitad se le rompió la punta del lápi |
| evento6:821 | timbre | 1.5 | -10.4 | 0 | -18 / silencio | Martes. Matemáticas. |
| evento6:842 | hoja | 2.0 | +2.1 | 0 | -19 / silencio | Mismo pupitre. Mi hoja boca abajo antes de la mitad, otra vez. |
| evento6:1024 | timbre | 1.5 | -10.4 | 0 | -18 / silencio | Resolvió el examen rápido y se quedó sonriéndole a su hoja. |
| evento6:1043 | timbre | 1.5 | -10.4 | 0 | -18 / silencio | Resolvió el examen sin una pausa, sin un tachón, sin una mirada a nadi |
| evento6:1058 | timbre | 1.5 | -10.4 | 0 | -18 / silencio | Resolvía con una mano. |
| evento6:1077 | timbre | 1.5 | -10.4 | 0 | -18 / silencio | Miércoles. Inglés. |
| evento6:1100 | hoja | 2.0 | +2.1 | 0 | -19 / silencio | Segunda fila. Mi hoja boca abajo antes de la mitad, y el lápiz encima. |
| evento6:1415 | silla | 2.5 | +4.0 | 3 | -14 / silencio | Se levantó, dejó la hoja en la mesa del profesor y fue hacia la puerta |
| evento6:1421 | puerta_cierra | 1.0 | -9.0 | 0 | -27 / silencio | Se fue sin vigilarlas. Y no pasó nada. |
| evento6:1425 | timbre | 1.5 | -10.4 | 0 | -18 / silencio | Nino terminó antes que casi todas. Soltó el lápiz. |
| evento6:1450 | timbre | 1.5 | -10.4 | 0 | -18 / silencio | Nino terminó. Soltó el lápiz sin ruido y giró la hoja boca abajo. |
| evento6:1471 | timbre | 1.5 | -10.4 | 0 | -18 / silencio | Nino terminó y repasó la hoja con el dedo. Soltó el lápiz. Giró la hoj |
| evento6:1490 | timbre | 1.5 | -10.4 | 0 | -18 / silencio | Jueves. Ciencias. |
| evento6:1511 | hoja | 2.0 | +2.1 | 0 | -19 / silencio | Segunda fila. Mi hoja boca abajo, el lápiz encima. Ya era costumbre. |
| evento6:1788 | timbre | 1.5 | -10.4 | 0 | -18 / silencio | Entregó sobre la campana, con la cuarta tachada y reescrita dos veces. |
| evento6:1811 | timbre | 1.5 | -10.4 | 0 | -18 / silencio | Entregó sobre la campana. La hoja, impecable. |
| evento6:1828 | timbre | 1.5 | -10.4 | 0 | -18 / silencio | Entregó pasada la campana, con la cuarta recién resuelta. Tarde, pero  |
| evento6:1849 | timbre | 1.5 | -10.4 | 0 | -18 / silencio | Viernes. Sociales. |
| evento6:1874 | hoja | 2.0 | +2.1 | 0 | -19 / silencio | Segunda fila, mi hoja boca abajo. A este examen lo dejé más despacio. |
| evento6:2076 | timbre | 1.5 | -10.4 | 0 | -18 / silencio | Escribió la respuesta de rutas sin una sola mención a la sal. |
| evento6:2093 | timbre | 1.5 | -10.4 | 0 | -18 / silencio | Escribió firme, sin dudas, cuatro renglones exactos. |
| evento6:2112 | timbre | 1.5 | -10.4 | 0 | -18 / silencio | Escribió largo. Se detuvo a mitad de un renglón. |
| evento6:2129 | timbre | 1.5 | -10.4 | 0 | -18 / silencio | Sonó la última campana de la semana. |
| evento6:2384 | silla | 1.2 | -2.4 | 0 | -20 / silencio | Yo también me levanté. |
| evento6:3012 | puerta_cierra | 1.0 | -9.0 | 0 | -27 / silencio | Cerró detrás de mí. Despacio. |
| evento6:3067 | celular | 1.5 | -11.8 | 0 | -18 / silencio | Mi teléfono sonó y tenía el nombre de quien diría el veredicto final. |
| evento6:3135 | puerta_cierra | 1.5 | -5.5 | 0 | -24 / contrato: -35.8 | Se puso el abrigo y salió. Sin portazo, como siempre. Esta vez, sin qu |
| evento6:3279 | puerta_abre | 1.2 | -6.6 | 0 | -18 / silencio | Cada una vino a por su boletín. Boca abajo, sin mirarlo. |
| evento6:3908 | hoja | 2.0 | +2.1 | 0 | -19 / silencio | Dieron vuelta a los cinco boletines a la vez. Y, claro, todas miraron  |
| evento6:4116 | camara | 1.5 | -4.1 | 0 | -26 / main_theme: -30.4 | Tomé la foto. Ninguna bajó el boletín. |
| evento6:4546 | toque_puerta | 1.0 | -4.0 | 0 | -23 / hogar: -28.3 | Hermanito, ¿sigues despierto? Tienes la luz encendida. |
| evento6:4644 | celular | 1.5 | -11.8 | 0 | -18 / hogar: -28.3 | El celular vibró cinco veces seguidas. No las leí. |
| final_malo:55 | taza_mesa | 1.0 | -3.0 | 0 | -20 / contrato: -31.4 | Dejó la taza sobre la mesa, despacio. |
| final_malo:90 | puerta_cierra | 1.0 | -9.0 | 0 | -27 / contrato: -31.4 | Recogió la taza y salió de la cocina sin esperar respuesta. |
| final_malo:162 | puerta_abre | 1.0 | -8.2 | 0 | -20 / silencio | No pasó ni un minuto. |
| final_malo:341 | puerta_cierra | 1.0 | -9.0 | 0 | -27 / derrota: -35.5 | La cerré yo mismo. Sin portazo. |
| final_malo:482 | timbre | 1.5 | -10.4 | 0 | -18 / silencio | Lunes. Primer día de exámenes. |
| final_malo:607 | timbre | 1.5 | -10.4 | 0 | -18 / silencio | Mi pupitre estaba en la segunda fila. Ellas, repartidas delante y a lo |
| final_malo:639 | hoja | 2.0 | +2.1 | 0 | -19 / amb_reloj: -52.7 | Hoy, lunes. |
| final_malo:699 | timbre | 1.5 | -10.4 | 0 | -18 / amb_reloj: -52.7 | Día martes. |
| final_malo:705 | hoja | 2.0 | +2.1 | 0 | -19 / amb_reloj: -52.7 | Las cinco lo hacían a la vez; yo solo podía mirar a una. |
| final_malo:755 | timbre | 1.5 | -10.4 | 0 | -18 / amb_reloj: -52.7 | Día miércoles. |
| final_malo:761 | hoja | 2.0 | +2.1 | 0 | -19 / amb_reloj: -52.7 | Las cinco lo hacían a la vez; yo solo podía mirar a una. |
| final_malo:807 | timbre | 1.5 | -10.4 | 0 | -18 / amb_reloj: -52.7 | Día jueves. |
| final_malo:813 | hoja | 2.0 | +2.1 | 0 | -19 / amb_reloj: -52.7 | Las cinco lo hacían a la vez; yo solo podía mirar a una. |
| final_malo:851 | timbre | 1.5 | -10.4 | 0 | -18 / amb_reloj: -52.7 | Y ahí terminó el examen de Itsuki. |
| final_malo:859 | hoja | 2.0 | +2.1 | 0 | -19 / amb_reloj: -52.7 | Las cinco lo hacían a la vez; yo solo podía mirar a una. |
| final_malo:921 | timbre | 1.5 | -10.4 | 0 | -18 / amb_reloj: -52.7 | Sonó la última campana de la semana. |
| final_malo:1105 | toque_puerta | 1.5 | -0.5 | 0 | -20 / silencio | Hermanito, ¿cómo salieron esas chicas? |
| final_malo:1153 | celular | 1.0 | -15.3 | 0 | -21 / silencio | Al día siguiente, a media mañana, me sonó el teléfono. |
| final_malo:1223 | puerta_cierra | 1.0 | -9.0 | 0 | -27 / contrato: -31.4 | Recogió sus cosas y salió. |
