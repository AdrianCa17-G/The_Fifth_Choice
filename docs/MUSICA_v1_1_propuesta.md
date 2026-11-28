# Música v1.1 — propuesta (sin aplicar)

## 1. Pistas

Primeros 30 s de cada una con earshot (etiquetas de modelos de audio y medidas); ánimo y energía son juicio
sobre eso. Duración y hueco del bucle se midieron sobre el archivo entero (hueco = silencio final + inicial).

| Pista | Ánimo | Energía | Duración | Punto de bucle | Sirve para |
|---|---|---|---|---|---|
| hogar | piano solo, melancólico, íntimo | 1 | 3:55 | **se nota**: 9,7 s de hueco | cuarto de Futaro (su tema) |
| cena | guitarra acústica, cálida y pareja | 2 | 1:00 | **se nota**: 3,3 s | mesa de casa |
| cotidiano | piano alegre, regular | 3 | 1:00 | se nota algo: 1,6 s | instituto, rutina |
| incomodo | juguetón, cómico | 4 | 2:26 | leve: 2,0 s | roces, quejas |
| extraneza | marimba y pizzicato, curioso | 2 | 1:46 | casi no: 0,3 s | algo no cuadra |
| caos | jazz con metales, festivo y rápido | 5 | 2:52 | **se nota**: 4,9 s | alboroto, comedia grande |
| contrato | bajo marcado, frío (etiquetas débiles; manda el uso) | 3 | 2:17 | no | Maruo |
| derrota | piano suave y triste, el más bajo | 1 | 1:18 | **se nota**: 6,4 s | pérdida, final malo |
| descubrimiento | caja de música, pensativo | 2 | 1:54 | se nota: 2,6 s | monólogo antes de decidir |
| guardia | arpa y pizzicato, contenido | 2 | 1:50 | **se nota**: 4,0 s | tensión (beat de Nino) |
| tregua | teclado grave, cálido y triste | 1 | 2:08 | **se nota**: 3,9 s | beat de Itsuki |
| hub | animado, esperanzado, pulso fijo | 3 | 1:12 | no | mapa de hubs |
| main_theme | piano épico, esperanzado | 4 | 3:38 | no (fundido breve) | menú, créditos |
| ichika | caja de música y ukelele, pícaro | 3 | 1:13 | sin hueco; salto de volumen de ~7 dB | solo Ichika |
| nino | lo-fi hip hop, relajado | 2 | 2:38 | **se nota mucho**: 10,9 s | solo Nino |
| miku | cuerdas pulsadas, lento y melancólico | 1 | 3:00 | leve: 0,9 s | solo Miku |
| yotsuba | luminoso, soñador, muy activo | 4 | 1:32 | **se nota**: 3 s y reentrada suave | solo Yotsuba |
| itsuki | piano, melancólico | 2 | 3:43 | leve: 0,6 s | solo Itsuki |
| amb_viento | ráfagas de viento | 1 | 1:04 | **se nota**: 5,8 s mudos | azotea, exterior |
| amb_silencio_exterior | pájaros, campo | 1 | 1:26 | leve: 2,0 s | exterior tranquilo |
| amb_reloj | tic-tac | 1 | 0:04 | no (es un patrón) | cuenta atrás |

## 2. Filas para aprobar

Líneas de diálogo a 4 s cada una; «vueltas» es el camino más largo. Las líneas nuevas se insertan antes de la indicada o tras su `scene`.

| # | archivo:línea | Escena | Pista actual | Vueltas | Propuesta | Por qué |
|---|---|---|---|---|---|---|
| 1 | 01_prologo.rpy:165 (nueva) | La oferta: entra Isanari | cena (desde :121) | 3,8 | `play music extraneza fadeout 1.5 fadein 2.0` | Escena nueva. cena queda en 13 líneas (0,9) y extraneza cubre 43 (1,6). Casi no se usa, y el trato «con truco» le va. Además cena enmascara el papel. |
| 2 | 02_cap1_beat_casa.rpy:151 (nueva) | Movimiento 3: Isanari llega | cena (desde :40) | 5,2 | `stop music fadeout 1.5` | cena queda en 42 líneas (2,8). Su visita fría cae sobre silencio (38 líneas) hasta hogar en el cuarto. |
| 3 | 02_cap1_Ichika.rpy:90 (nueva) | La grieta: despierta sin actuar | ichika (desde :47) | 3,8 | `stop music fadeout 1.5` | Escena nueva. Se le cae la máscara y se va su tema (14 líneas en silencio). |
| 4 | 02_cap1_Ichika.rpy:125 (nueva) | «Luces demasiado cansada»: vuelve la actuación | silencio (tras fila 3) | 2,2 | `play music ichika fadein 2.0` | Cambio de plano a la sala. Vuelve su tema con la máscara: 0,8 + 2,2 vueltas. Va junto con la 3. |
| 5 | 02_cap1_conexiones.rpy:2831 | Aula, víspera de exámenes | cotidiano | 4,0 | `play music extraneza fadein 1.5` | No hay corte posible dentro (una sola conversación), así que pista más larga: 2,3 vueltas. Nervios disimulados. |
| 6 | 02_cap1_beat_Itsuki.rpy:178 (nueva) | Azotea, tras el plano de las manos | amb_viento (desde :49) | 5,5 | `stop ambiente fadeout 2.0` | Baja a 3,3. La guía pide cortarlo en :158 (2,8), pero la línea :160 dice «El viento seguía soplando». Alternativa: cortar en :158. |
| 7 | 02_cap1_evento6.rpy:223 | Discurso y confesiones antes del examen | cotidiano | 2,5-3,2 | **sin cambio** | En una partida suenan 37-48 líneas, no ~90 (el resto son variantes por estado). Es una sola conversación y el exceso es mínimo. |
| 8 | 02_cap1_conexiones.rpy:3660 | Departamento, clima mixto (opcional) | cotidiano | 2,3 | `play music extraneza fadein 2.0` | Variedad: la rama mixta deja de sonar igual que la buena. «Parecía la misma escena del primer día». Cambia la regla de la guía. |
| 9 | 02_cap1_conexiones.rpy:4054 | Domingo, clima mixto (opcional) | cotidiano | 0,5 | `play music extraneza fadein 2.5` | Solo si apruebas la 8, para que la rama sea coherente. |
| 10 | 02_cap1_conexiones.rpy:1957 | Camino al instituto (opcional) | cotidiano | 0,5 | `stop music fadeout 1.5` | Un cotidiano menos; hogar no debe salir a la calle. El silencio separa cuarto y aula. |

## 3. Mapa actual

Calculado recorriendo el árbol de Ren'Py (menús, ifs, saltos y calls); mínimo y máximo por camino, sin repetir bucles.
No incluye los `renpy.music.play` en Python (minijuegos y extras).

| archivo:línea | Escena | Pista | Líneas | Vueltas | Termina en |
|---|---|---|---|---|---|
| 01_prologo.rpy:71 | prologo · cg_familia | hogar | 21 | 0.4 | 01_prologo.rpy:121 [play cena] |
| 01_prologo.rpy:121 | prologo · bg_comedor | cena | 56 | 3.8 | 01_prologo.rpy:305 [stop ] |
| 01_prologo.rpy:318 | prologo · cg_examen | cotidiano | 9 | 0.6 | 01_prologo.rpy:344 [play incomodo] |
| 01_prologo.rpy:344 | prologo · cg_itsuki_sentada | incomodo | 32 | 0.9 | 01_prologo.rpy:435 [stop ] |
| 01_prologo.rpy:440 | prologo · bg_azotea_tarde | amb_viento | 27-28 | 1.7-1.8 | 01_prologo.rpy:533 [stop ] |
| 01_prologo.rpy:552 | prologo · bg_edificio | cotidiano | 12 | 0.8 | 01_prologo.rpy:588 [stop ] |
| 01_prologo.rpy:610 | prologo · cg_ichika_puerta | extraneza | 76 | 2.9 | 01_prologo.rpy:829 [play caos] |
| 01_prologo.rpy:829 | prologo · cg_itsuki_discusion | caos | 44 | 1.0 | 01_prologo.rpy:996 [stop ] |
| 01_prologo.rpy:1005 | prologo · cg_maruo_reunion | contrato | 26 | 0.8 | 01_prologo.rpy:1070 [stop ] |
| 01_prologo.rpy:1122 | prologo · cg_hermanas_estudiando | derrota | 27 | 1.4 | 01_prologo.rpy:1181 [stop ] |
| 01_prologo.rpy:1332 | prologo · bg_cuarto_mc | hogar | 7 | 0.1 | 01_prologo.rpy:1355 [stop ] |
| 02_cap1_Ichika.rpy:47 | hub_Ichika · cg_ichika_ensayo | ichika | 68 | 3.8 | Ichika.rpy:225 [stop ] |
| 02_cap1_Ichika.rpy:257 | hub_Ichika · bg_sala_ensayo | descubrimiento | 40-61 | 1.4-2.1 | Ichika.rpy:574 [stop ] |
| 02_cap1_Itsuki.rpy:50 | hub_Itsuki · cg_itsuki_atascada | itsuki | 59-61 | 1.1-1.1 | Itsuki.rpy:205 [stop ] |
| 02_cap1_Itsuki.rpy:233 | hub_Itsuki · bg_aula_tarde | descubrimiento | 23-37 | 0.8-1.3 | Itsuki.rpy:483 [stop ] |
| 02_cap1_Miku.rpy:48 | hub_Miku · cg_miku_biblioteca | miku | 108 | 2.4 | Miku.rpy:314 [stop ] |
| 02_cap1_Miku.rpy:342 | hub_Miku | descubrimiento | 12-36 | 0.4-1.3 | Miku.rpy:560 [stop ] |
| 02_cap1_Nino.rpy:55 | hub_Nino | nino | 75-77 | 1.9-1.9 | Nino.rpy:268 [stop ] |
| 02_cap1_Nino.rpy:296 | hub_Nino | descubrimiento | 22-29 | 0.8-1.0 | Nino.rpy:510 [stop ] |
| 02_cap1_Yotsuba.rpy:47 | hub_Yotsuba · cg_yotsuba_pista | yotsuba | 35 | 1.5 | Yotsuba.rpy:143 [stop ] |
| 02_cap1_Yotsuba.rpy:154 | hub_Yotsuba · cg_yotsuba_rotulador | amb_silencio_exterior | 26 | 1.2 | Yotsuba.rpy:208 [stop ] |
| 02_cap1_Yotsuba.rpy:215 | hub_Yotsuba · bg_pista_atletismo | yotsuba | 25 | 1.1 | Yotsuba.rpy:282 [stop ] |
| 02_cap1_Yotsuba.rpy:294 | hub_Yotsuba | descubrimiento | 30-55 | 1.1-1.9 | Yotsuba.rpy:606 [stop ] |
| 02_cap1_apertura.rpy:47 | cap1_apertura · bg_aula | cotidiano | 8 | 0.5 | apertura.rpy:74 [play incomodo] |
| 02_cap1_apertura.rpy:74 | cap1_apertura · bg_aula | incomodo | 17 | 0.5 | apertura.rpy:144 [stop ] |
| 02_cap1_apertura.rpy:175 | cap1_apertura · cg_cinco_sentadas | extraneza | 36 | 1.4 | apertura.rpy:253 [play caos] |
| 02_cap1_apertura.rpy:253 | cap1_apertura · bg_departamento | caos | 48 | 1.1 | apertura.rpy:394 [stop ] |
| 02_cap1_apertura.rpy:443 | cap1_apertura · cg_maruo_reunion | contrato | 16 | 0.5 | apertura.rpy:485 [stop ] |
| 02_cap1_apertura.rpy:492 | cap1_apertura · bg_comedor | cena | 18-22 | 1.2-1.5 | apertura.rpy:600 [stop ] |
| 02_cap1_apertura.rpy:605 | cap1_apertura · cg_calificacion | hogar | 70-74 | 1.2-1.3 | conexiones.rpy:931 [stop ] |
| 02_cap1_beat_Itsuki.rpy:49 | beat_Itsuki · cg_itsuki_azotea_cuaderno | amb_viento | 75-87 | 4.7-5.5 | beat_Itsuki.rpy:337 [stop ] |
| 02_cap1_beat_Itsuki.rpy:158 | beat_Itsuki · cg_itsuki_azotea_manos | tregua | 37-43 | 1.2-1.3 | beat_Itsuki.rpy:336 [stop ] |
| 02_cap1_beat_Nino.rpy:74 | beat_Nino · cg_nino_confrontacion_cocina | guardia | 21-117 | 0.8-4.3 | beat_Nino.rpy:139 [stop ], beat_Nino.rpy:581 [stop ] (+1) |
| 02_cap1_beat_Nino.rpy:146 | beat_Nino · cg_maruo_reunion | contrato | 17 | 0.5 | beat_Nino.rpy:186 [stop ] |
| 02_cap1_beat_Nino.rpy:199 | beat_Nino · bg_cocina | guardia | 67-88 | 2.4-3.2 | beat_Nino.rpy:581 [stop ] |
| 02_cap1_beat_casa.rpy:40 | beat_casa · bg_comedor | cena | 77 | 5.2 | beat_casa.rpy:255 [stop ] |
| 02_cap1_beat_casa.rpy:266 | beat_casa · cg_libreta | hogar | 5-28 | 0.1-0.5 | beat_casa.rpy:1047 [play hogar], beat_casa.rpy:361 [play ichika] (+6) |
| 02_cap1_beat_casa.rpy:361 | bcl_ichika | ichika | 26-30 | 1.4-1.7 | beat_casa.rpy:455 [play hogar] |
| 02_cap1_beat_casa.rpy:455 | bcl_ichika | hogar | 1-20 | 0.0-0.3 | beat_casa.rpy:1047 [play hogar], beat_casa.rpy:361 [play ichika] (+6) |
| 02_cap1_beat_casa.rpy:494 | bcl_nino | nino | 36-58 | 0.9-1.5 | beat_casa.rpy:1047 [play hogar], beat_casa.rpy:361 [play ichika] (+6) |
| 02_cap1_beat_casa.rpy:648 | bcl_nino | hogar | 1-20 | 0.0-0.3 | beat_casa.rpy:1047 [play hogar], beat_casa.rpy:361 [play ichika] (+6) |
| 02_cap1_beat_casa.rpy:669 | bcl_miku | miku | 29-30 | 0.6-0.7 | beat_casa.rpy:759 [play hogar] |
| 02_cap1_beat_casa.rpy:759 | bcl_miku | hogar | 1-20 | 0.0-0.3 | beat_casa.rpy:1047 [play hogar], beat_casa.rpy:361 [play ichika] (+6) |
| 02_cap1_beat_casa.rpy:800 | bcl_yotsuba | yotsuba | 22-25 | 1.0-1.1 | beat_casa.rpy:880 [play hogar] |
| 02_cap1_beat_casa.rpy:880 | bcl_yotsuba | hogar | 1-20 | 0.0-0.3 | beat_casa.rpy:1047 [play hogar], beat_casa.rpy:361 [play ichika] (+6) |
| 02_cap1_beat_casa.rpy:919 | bcl_itsuki | itsuki | 32-56 | 0.6-1.0 | beat_casa.rpy:1047 [play hogar], beat_casa.rpy:361 [play ichika] (+6) |
| 02_cap1_beat_casa.rpy:1047 | bcl_itsuki | hogar | 1-20 | 0.0-0.3 | beat_casa.rpy:1047 [play hogar], beat_casa.rpy:361 [play ichika] (+6) |
| 02_cap1_conexiones.rpy:47 | reaccion_ichika | ichika | 6-14 | 0.3-0.8 | conexiones.rpy:147 [stop ] |
| 02_cap1_conexiones.rpy:158 | reaccion_nino | nino | 4-13 | 0.1-0.3 | conexiones.rpy:244 [stop ] |
| 02_cap1_conexiones.rpy:255 | reaccion_miku | miku | 4-21 | 0.1-0.5 | conexiones.rpy:353 [stop ] |
| 02_cap1_conexiones.rpy:364 | reaccion_yotsuba | yotsuba | 4-15 | 0.2-0.7 | conexiones.rpy:455 [stop ] |
| 02_cap1_conexiones.rpy:467 | reaccion_itsuki | itsuki | 14-19 | 0.3-0.3 | conexiones.rpy:604 [stop ] |
| 02_cap1_conexiones.rpy:940 | cap1_interconexion_1 · bg_aula | cotidiano | 8 | 0.5 | conexiones.rpy:968 [play incomodo] |
| 02_cap1_conexiones.rpy:968 | cap1_interconexion_1 | incomodo | 79 | 2.2 | conexiones.rpy:1246 [stop ] |
| 02_cap1_conexiones.rpy:1293 | cap1_interconexion_2 · bg_cuarto_mc | hogar | 5 | 0.1 | conexiones.rpy:1334 [play cena] |
| 02_cap1_conexiones.rpy:1334 | cap1_interconexion_2 · bg_comedor | cena | 13-14 | 0.9-0.9 | conexiones.rpy:1408 [stop ] |
| 02_cap1_conexiones.rpy:1438 | cap1_interconexion_2 | incomodo | 12-25 | 0.3-0.7 | conexiones.rpy:1591 [stop ] |
| 02_cap1_conexiones.rpy:1628 | cap1_interconexion_3 · bg_cuarto_mc | hogar | 25-27 | 0.4-0.5 | conexiones.rpy:1717 [stop ] |
| 02_cap1_conexiones.rpy:1729 | cap1_interconexion_3 · bg_aula | cotidiano | 21-25 | 1.4-1.7 | conexiones.rpy:1881 [stop ] |
| 02_cap1_conexiones.rpy:1916 | cap1_interconexion_4 · bg_cuarto_mc | hogar | 5 | 0.1 | conexiones.rpy:1957 [play cotidiano] |
| 02_cap1_conexiones.rpy:1957 | cap1_interconexion_4 · bg_escuela | cotidiano | 6-8 | 0.4-0.5 | conexiones.rpy:1999 [stop ] |
| 02_cap1_conexiones.rpy:2015 | cap1_interconexion_4 · bg_aula | derrota | 6-18 | 0.3-0.9 | conexiones.rpy:2254 [stop ] |
| 02_cap1_conexiones.rpy:2260 | cap1_interconexion_4 | extraneza | 37-38 | 1.4-1.4 | beat_Nino.rpy:33 [stop ] |
| 02_cap1_conexiones.rpy:2653 | cap1_interconexion_5 · bg_escuela | cotidiano | 6 | 0.4 | conexiones.rpy:2694 [stop ] |
| 02_cap1_conexiones.rpy:2702 | cap1_interconexion_5 | incomodo | 10-14 | 0.3-0.4 | conexiones.rpy:2814 [stop ] |
| 02_cap1_conexiones.rpy:2831 | cap1_interconexion_5 | cotidiano | 50-60 | 3.3-4.0 | conexiones.rpy:3108 [stop ] |
| 02_cap1_conexiones.rpy:3117 | cap1_interconexion_5 | amb_reloj | 3 | 3.0 | conexiones.rpy:3125 [stop ] |
| 02_cap1_conexiones.rpy:3195 | cap1_interconexion_6 · bg_cuarto_mc | hogar | 7-14 | 0.1-0.2 | conexiones.rpy:3259 [stop ] |
| 02_cap1_conexiones.rpy:3291 | cap1_interconexion_6 · bg_aula | cotidiano | 6 | 0.4 | conexiones.rpy:158 [play nino], conexiones.rpy:255 [play miku] (+3) |
| 02_cap1_conexiones.rpy:3317 | cap1_interconexion_6 | derrota | 32-40 (solo suenan 2 quejas) | 1.6-2.1 | conexiones.rpy:3334 [stop ] |
| 02_cap1_conexiones.rpy:3356 | cap1_interconexion_6 | incomodo | 21-49 | 0.6-1.3 | conexiones.rpy:3455 [stop ], conexiones.rpy:3590 [stop ] |
| 02_cap1_conexiones.rpy:3617 | cap1_interconexion_6 · cg_cinco_estudiando | cotidiano | 18-41 | 1.2-2.7 | conexiones.rpy:3722 [stop ], conexiones.rpy:3926 [stop ] |
| 02_cap1_conexiones.rpy:3660 | cap1_interconexion_6 · cg_cinco_repasando | cotidiano | 12-35 | 0.8-2.3 | conexiones.rpy:3722 [stop ], conexiones.rpy:3926 [stop ] |
| 02_cap1_conexiones.rpy:3691 | cap1_interconexion_6 · cg_hermanas_estudiando | derrota | 11-34 | 0.6-1.8 | conexiones.rpy:3722 [stop ], conexiones.rpy:3926 [stop ] |
| 02_cap1_conexiones.rpy:3729 | cap1_interconexion_6 · cg_maruo_reunion | contrato | 11-13 | 0.3-0.4 | conexiones.rpy:3779 [stop ] |
| 02_cap1_conexiones.rpy:3938 | cap1_interconexion_6 · bg_cuarto_mc | hogar | 7-12 | 0.1-0.2 | conexiones.rpy:4024 [stop ] |
| 02_cap1_conexiones.rpy:4044 | cap1_interconexion_6 · bg_departamento_anochecer | cotidiano | 7-8 | 0.5-0.5 | beat_casa.rpy:30 [stop ] |
| 02_cap1_conexiones.rpy:4054 | cap1_interconexion_6 | cotidiano | 6-7 | 0.4-0.5 | beat_casa.rpy:30 [stop ] |
| 02_cap1_evento6.rpy:223 | e6_lunes · bg_aula | cotidiano | 37-48 | 2.5-3.2 | evento6.rpy:495 [stop ] |
| 02_cap1_evento6.rpy:523 | e6_lunes | amb_reloj | 0 | 0.0 | return evento6.rpy:525 |
| 02_cap1_evento6.rpy:615 | e6_yotsuba_mono_calida | descubrimiento | 13 | 0.5 | return evento6.rpy:643 |
| 02_cap1_evento6.rpy:719 | e6_yotsuba_mj | yotsuba | 0 | 0.0 | evento6.rpy:724 [stop ] |
| 02_cap1_evento6.rpy:875 | e6_ichika_mono_calida | descubrimiento | 18 | 0.6 | return evento6.rpy:913 |
| 02_cap1_evento6.rpy:977 | e6_ichika_mj | ichika | 0 | 0.0 | evento6.rpy:982 [stop ] |
| 02_cap1_evento6.rpy:1188 | e6_nino_mono_calida | descubrimiento | 19 | 0.7 | return evento6.rpy:1230 |
| 02_cap1_evento6.rpy:1340 | e6_nino_mj | nino | 0 | 0.0 | evento6.rpy:1345 [stop ] |
| 02_cap1_evento6.rpy:1569 | e6_itsuki_mono_calida | descubrimiento | 19 | 0.7 | return evento6.rpy:1606 |
| 02_cap1_evento6.rpy:1701 | e6_itsuki_mj | itsuki | 0 | 0.0 | evento6.rpy:1706 [stop ] |
| 02_cap1_evento6.rpy:1905 | e6_miku_mono_calida | descubrimiento | 17 | 0.6 | return evento6.rpy:1941 |
| 02_cap1_evento6.rpy:2171 | e6_despues · bg_aula_tarde | derrota | 24-25 | 1.2-1.3 | evento6.rpy:2262 [play cotidiano] |
| 02_cap1_evento6.rpy:2262 | e6_despues | cotidiano | 14 | 0.9 | evento6.rpy:2308 [stop ] |
| 02_cap1_evento6.rpy:2424 | e6_despues · bg_escuela_atardecer | cotidiano | 12 | 0.8 | evento6.rpy:2450 [stop ] |
| 02_cap1_evento6.rpy:3089 | e6_resultados · cg_maruo_reunion | contrato | 18-19 | 0.5-0.6 | evento6.rpy:3137 [stop ] |
| 02_cap1_evento6.rpy:3091 | e6_resultados · cg_maruo_reunion | contrato | 18-19 | 0.5-0.6 | evento6.rpy:3137 [stop ] |
| 02_cap1_evento6.rpy:3916 | e6_mesa | main_theme | 46-47 | 0.8-0.9 | evento6.rpy:4034 [stop ] |
| 02_cap1_evento6.rpy:4060 | e6_mesa | main_theme | 43 | 0.8 | return evento6.rpy:4178 |
| 02_cap1_evento6.rpy:4199 | e6_casa · bg_comedor | cena | 31 | 2.1 | return evento6.rpy:4275 |
| 02_cap1_evento6.rpy:4292 | e6_cuarto · bg_cuarto_mc | hogar | 27 | 0.5 | evento6.rpy:4384 [stop ] |
| 02_cap1_evento6.rpy:4457 | e6_retrato · cg_familia | hogar | 74-79 | 1.3-1.3 | evento6.rpy:4775 [stop ] |
| 02_cap1_final_malo.rpy:45 | final_malo_beat · cg_maruo_reunion | contrato | 19 | 0.6 | final_malo.rpy:92 [stop ] |
| 02_cap1_final_malo.rpy:325 | final_malo_beat | derrota | 9 | 0.5 | final_malo.rpy:357 [stop ] |
| 02_cap1_final_malo.rpy:637 | final_malo_hub3 · bg_negro | amb_reloj | 89-90 | 89.0-90.0 | final_malo.rpy:930 [stop ] |
| 02_cap1_final_malo.rpy:943 | final_malo_hub3 · bg_aula_tarde | derrota | 39-40 | 2.0-2.1 | final_malo.rpy:1091 [stop ] |
| 02_cap1_final_malo.rpy:1170 | final_malo_hub3 · cg_maruo_reunion | contrato | 24 | 0.7 | final_malo.rpy:1225 [stop ] |
| 02_cap1_final_malo.rpy:1424 | final_malo_hub3 | derrota | 4 | 0.2 | final_malo.rpy:1447 [stop ] |
| 02_cap1_hubs.rpy:26 | hub_1 | hub | espera del jugador | — | hubs.rpy:34 [stop ] |
| 02_cap1_hubs.rpy:56 | hub_2 | hub | espera del jugador | — | hubs.rpy:63 [stop ] |
| 02_cap1_hubs.rpy:85 | hub_3 | hub | espera del jugador | — | hubs.rpy:92 [stop ] |
| 15_chat_grupo.rpy:555 | chat_grupo_prueba · bg_cuarto_mc | hogar | 6 | 0.1 | return 15_chat_grupo.rpy:592 |
| 16_creditos.rpy:340 | creditos_rol · bg_negro | main_theme | 0 | 0.0 | return 16_creditos.rpy:354 |

`stop music` / `stop ambiente` (121): 00_definiciones.rpy:653, 00_definiciones.rpy:654, 00_definiciones.rpy:714, 01_prologo.rpy:57, 01_prologo.rpy:58, 01_prologo.rpy:305, 01_prologo.rpy:435, 01_prologo.rpy:533, 01_prologo.rpy:588, 01_prologo.rpy:996, 01_prologo.rpy:1070, 01_prologo.rpy:1181, 01_prologo.rpy:1270, 01_prologo.rpy:1355, apertura.rpy:144, apertura.rpy:394, apertura.rpy:485, apertura.rpy:600, beat_casa.rpy:30, beat_casa.rpy:255, beat_Itsuki.rpy:35, beat_Itsuki.rpy:336, beat_Itsuki.rpy:337, beat_Nino.rpy:33, beat_Nino.rpy:139, beat_Nino.rpy:186, beat_Nino.rpy:581, conexiones.rpy:147, conexiones.rpy:244, conexiones.rpy:353, conexiones.rpy:455, conexiones.rpy:604, conexiones.rpy:931, conexiones.rpy:1246, conexiones.rpy:1408, conexiones.rpy:1591, conexiones.rpy:1717, conexiones.rpy:1881, conexiones.rpy:1999, conexiones.rpy:2254, conexiones.rpy:2412, conexiones.rpy:2694, conexiones.rpy:2814, conexiones.rpy:3108, conexiones.rpy:3125, conexiones.rpy:3259, conexiones.rpy:3334, conexiones.rpy:3455, conexiones.rpy:3590, conexiones.rpy:3722, conexiones.rpy:3779, conexiones.rpy:3926, conexiones.rpy:4024, evento6.rpy:196, evento6.rpy:197, evento6.rpy:495, evento6.rpy:724, evento6.rpy:776, evento6.rpy:982, evento6.rpy:1026, evento6.rpy:1345, evento6.rpy:1427, evento6.rpy:1706, evento6.rpy:1790, evento6.rpy:2018, evento6.rpy:2153, evento6.rpy:2308, evento6.rpy:2397, evento6.rpy:2450, evento6.rpy:3052, evento6.rpy:3137, evento6.rpy:3230, evento6.rpy:4034, evento6.rpy:4194, evento6.rpy:4284, evento6.rpy:4384, evento6.rpy:4775, final_malo.rpy:38, final_malo.rpy:92, final_malo.rpy:357, final_malo.rpy:509, final_malo.rpy:624, final_malo.rpy:930, final_malo.rpy:1091, final_malo.rpy:1225, final_malo.rpy:1447, hubs.rpy:34, hubs.rpy:43, hubs.rpy:63, hubs.rpy:72, hubs.rpy:92, hubs.rpy:101, Ichika.rpy:37, Ichika.rpy:225, Ichika.rpy:574, Itsuki.rpy:40, Itsuki.rpy:205, Itsuki.rpy:483, Miku.rpy:38, Miku.rpy:314, Miku.rpy:560, Nino.rpy:43, Nino.rpy:268, Nino.rpy:510, Nino.rpy:558, Yotsuba.rpy:37, Yotsuba.rpy:143, Yotsuba.rpy:208, Yotsuba.rpy:282, Yotsuba.rpy:606, 05_finales.rpy:14, 08_extras.rpy:1303, 08_extras.rpy:1362, 10_mj_transicion.rpy:618, 10_mj_transicion.rpy:626, 13_transiciones.rpy:430, 13_transiciones.rpy:431, 14_progreso_chicas.rpy:535, 14_progreso_chicas.rpy:536, hub_mapa.rpy:1037, hub_mapa.rpy:1038
