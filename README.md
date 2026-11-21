# The Fifth Choice

Fan visual novel basada en **Quintessential Quintuplets** (Go-toubun no Hanayome).
Arranca donde arranca el anime y sigue por su cuenta: los personajes son los de la
obra, la historia es propia. Las decisiones del jugador determinan con cuál de las
cinco quintillizas termina.

**Motor:** Ren'Py 8.5.3 · **Desarrollo:** Adrian (AdrianKiller17) · **Versión:** 1.0 (Prólogo + Capítulo 1)

**Descarga oficial (la única):** [adriankiller17.itch.io/the-fifth-choice](https://adriankiller17.itch.io/the-fifth-choice)
· Windows, Android y Linux · Solo en español

Fangame **no oficial y gratuito**. Es y será completo para todos; se aceptan
donaciones voluntarias en itch.io, pero ningún contenido depende de donar.
Aviso legal y atribuciones en [`CREDITOS.md`](CREDITOS.md).

---

## Estado

**Prólogo y Capítulo 1 lanzados el 21 de noviembre de 2026.** Faltan dos capítulos
y los finales.

| Fase | Archivos | Estado |
|---|---|---|
| Núcleo | `00_definiciones.rpy` | ✅ |
| Prólogo | `01_prologo.rpy` | ✅ Lanzado — 7 escenas |
| Capítulo 1 | `02_cap1_*.rpy` | ✅ Lanzado — apertura, 3 hubs, 5 eventos de hermana, 3 beats, Evento 6 y final malo (variantes A y B) |
| Minijuegos | `10_*.rpy` | ✅ Lanzado — uno por hermana, en el Evento 6 |
| Interfaz | `06_main_menu.rpy`, `07_ui.rpy`, `08_extras.rpy`, `09_menus_sistema.rpy`, `hub_mapa.rpy`, `12`–`16` | ✅ Lanzado |
| Capítulo 2 | `03_capitulo2.rpy` | ⬜ Pendiente |
| Capítulo 3 | `04_capitulo3.rpy` | ⬜ Pendiente |
| Finales | `05_finales.rpy` | 🟨 Solo el final malo del Capítulo 1; faltan el cálculo final, los cinco románticos, el final malo del Capítulo 3 y el secreto |

---

## Documentación

| Documento | Qué contiene |
|---|---|
| Este README | Qué es el juego, sistemas, personajes, estructura del repositorio |
| [`CREDITOS.md`](CREDITOS.md) | Aviso de fangame, atribuciones y licencias. Repite `16_creditos.rpy` |
| [`docs/GUIA_ARTE.md`](docs/GUIA_ARTE.md) | PixAI, LoRAs, prompts, estándar de sprites, posproducción |
| [`docs/GUIA_AUDIO.md`](docs/GUIA_AUDIO.md) | Fuentes, licencias, nombres, escala de volumen, montaje |
| [`docs/GUIA_RENPY.md`](docs/GUIA_RENPY.md) | Convenciones de código y trampas del motor ya encontradas |
| [`docs/GUIA_UI.md`](docs/GUIA_UI.md) | Interfaz: archivos, recetas (decisiones, hub, chat, barra, créditos) y trampas |
| [`docs/MINIJUEGOS/`](docs/MINIJUEGOS/) | Marco común y estado final de los cinco minijuegos |
| [`docs/PROLOGO.md`](docs/PROLOGO.md) | Resumen del prólogo cerrado |
| [`docs/CAPITULO_1/CAP1.md`](docs/CAPITULO_1/CAP1.md) | Resumen del Capítulo 1 cerrado |

Las guías son **transversales**: valen para los capítulos que faltan. Consultarlas
antes de generar arte, tocar audio, interfaz o motor.

El resto de `docs/` (guiones de escena, planes del Evento 6, evaluaciones de
sprites, revisiones de personaje, `superpowers/`) es **material de trabajo**:
explica la intención, pero no es estado ni regla. **Si un documento y el código no
coinciden, manda el código.**

---

## Estructura del repositorio

```
The_Fifth_Choice/
├── README.md
├── CREDITOS.md
├── .gitignore
├── docs/
│   ├── GUIA_ARTE.md · GUIA_AUDIO.md · GUIA_RENPY.md · GUIA_UI.md
│   ├── PROLOGO.md
│   ├── CAPITULO_1/        CAP1.md, apertura, HUBS_HERMANAS/, BEATS_CAP1/, EVENTO_6/
│   ├── MINIJUEGOS/        MARCO_COMUN.md y MJ_<hermana>.md
│   ├── EVAL_SPRITES/      evaluaciones de sprites del Cap. 1 (cerradas)
│   ├── REVISION_PERSONAJES_CAP1/   revisiones narrativas (cerradas)
│   └── superpowers/       planes y specs de sesiones de Claude Code
└── The Fifth Choice/      el proyecto de Ren'Py
    └── game/
        ├── *.rpy          ver la tabla de abajo
        ├── audio/         bgm/ (13 + bgm_hermanas/ con 5), sfx/ (efectos y cortinillas), ambientes
        ├── images/        bg/, cg/, sprites/, chibis/, hubs/, menu/
        ├── ui/            PNG de la interfaz, generados por script
        ├── gui/           plantilla del motor, retocada
        └── fonts/         4 familias SIL OFL, cada una con su licencia
```

Los scripts de Python de arte, interfaz y audio (`herramientas/`: normalizar
sprites, generar la interfaz, el logo, los fondos del collage, las cortinillas y el
mapa de pulsos de Miku) viven en la carpeta local del proyecto y **no están en el
repositorio**.

`cache/`, `saves/`, `tl/`, `libs/` y los `.rpyc` los genera Ren'Py. No se suben: el
`.gitignore` ya los excluye.

### Qué va en cada `.rpy`

| Archivo | Contenido |
|---|---|
| `00_definiciones.rpy` | Todo lo que no es narrativa: personajes, variables, fondos y sprites compartidos, transforms, audio, funciones de apoyo (`sumar_punto`, `rama_de`…), pantalla de nombre y `label start` |
| `01_prologo.rpy` | El prólogo y sus CG propios |
| `02_cap1_apertura.rpy` | Apertura del Capítulo 1 |
| `02_cap1_hubs.rpy` | Los tres hubs: mapa, evento y control de desaires |
| `02_cap1_<Hermana>.rpy` | Los cinco eventos de hermana |
| `02_cap1_beat_Itsuki.rpy`, `_beat_Nino`, `_beat_casa` | Los tres beats fijos |
| `02_cap1_conexiones.rpy` | Interconexiones entre bloques, reacciones de la hermana visitada y clima del capítulo |
| `02_cap1_evento6.rpy` | Evento 6: semana de exámenes y cierre del capítulo |
| `02_cap1_final_malo.rpy` | Despido temprano, variantes A y B |
| `05_finales.rpy` | Entrada al final malo del Capítulo 1; aquí irá el resto de finales |
| `06_main_menu.rpy` | Menú principal |
| `07_ui.rpy`, `07b_collage.rpy` | HUD, cinta del lugar, decisiones con peso; collage del beat casa |
| `08_extras.rpy` | Galería, Finales y Extras (minijuegos, animaciones, repetir) |
| `09_menus_sistema.rpy` | Guardar, Cargar, Opciones, Historial, Acerca de, Ayuda |
| `hub_mapa.rpy` | Pantalla del mapa de hubs y animación de tarde completada |
| `10_minijuegos.rpy`, `10_mj_*.rpy` | Marco común, los cinco minijuegos, chibis y transiciones |
| `11_e6_debug.rpy` | Pruebas del Evento 6 |
| `12_e6_pantallas.rpy` | Boletín de notas |
| `13_transiciones.rpy` | Cortinillas de capítulo, tarde, examen y finales |
| `14_progreso_chicas.rpy` | Barra de progreso de las chicas al cerrar capítulo |
| `15_chat_grupo.rpy` | Chat de grupo de las quintillizas |
| `16_creditos.rpy` | Aviso inicial, créditos (fuente única) y «Continuará» |
| `gui.rpy`, `options.rpy`, `screens.rpy` | Configuración del motor |

Los archivos de capítulo contienen su `label` y lo que solo ese bloque usa (sus CG,
fondos y audios). Si otro archivo lo reutiliza, sube a `00_definiciones.rpy`.
`label start` vive ahí y en ningún otro sitio.

---

## Estructura narrativa

```
PRÓLOGO → CAPÍTULO 1 → CAPÍTULO 2 → CAPÍTULO 3 → DECLARACIÓN → FINAL
```

Estilo *Doki Doki Literature Club*: el jugador no elige a una hermana desde un
menú; la elige con a quién busca y cómo le responde. La historia es **lineal desde
el prólogo**: ninguna quintilliza conocía antes al protagonista. El único trasfondo
previo es que Isanari y Maruo son viejos amigos, y por eso el protagonista consigue
el trabajo de tutor.

Cada capítulo cierra como un final en sí mismo.

### Protagonista

Nombre personalizable al inicio (`nombre_jugador`, Futaro por defecto). No lleva
el apellido Uesugi: solo lo tiene su padre. Habla de tres maneras —`mc`,
`narrador` y `mc_pensamiento`— y las tres son la misma persona.

**Nunca se muestra su rostro.** En escenas grupales es una silueta; en los CG va de
espaldas, desenfocado o cortado por el borde. No existe LoRA del personaje, y sin
rostro no hay nada que el modelo pueda estropear.

### Personajes

| Personaje | Color | Materia fuerte | En una línea |
|---|---|---|---|
| Ichika | `#FFB7C5` rosa | Matemáticas | Actriz; duerme por agotamiento, no por floja, y usa la simpatía como blindaje |
| Nino | `#C39BD3` morado | Inglés | Tsundere; no quiere más tutores porque ninguno duraba, y protege a las otras cuatro |
| Miku | `#5DADE2` azul | Sociales | Fan del periodo Sengoku; se corta sola cuando se entusiasma |
| Yotsuba | `#58D68D` verde | Japonés | Energética; cree que solo sirve para correr y animar a las demás |
| Itsuki | `#EC7063` rojo | Ciencias | Formal y estudiosa; la única que se esfuerza y aun así va mal |

Secundarios: **Raiha**, hermana menor del protagonista; **Isanari**, su padre,
bromista y fotógrafo; **Maruo**, padre de las quintillizas, médico y formal.

Itsuki aparece como **«Estudiante Nueva»** (`itsuki_inicio`) hasta que grita su
nombre en el prólogo; desde ahí, `itsuki`.

### Desviaciones del canon — decisiones cerradas

- **Nino lleva el pelo corto desde el inicio.** Nunca describirla con el pelo largo.
- **Miku es castaña**: el LoRA no da el azul pálido. Su color de interfaz sigue siendo `#5DADE2`.
- **Miku va de sudadera**, dentro y fuera de casa. La separa del bloque de hermanas.
- **Sus audífonos van al cuello**, nunca puestos; subírselos es un gesto con significado.
- **Ichika duerme por agotamiento**, no por pereza.
- Japonés y Literatura son **la misma materia**.

---

## Sistema de puntos

| Rama elegida en un evento de hermana | Efecto |
|---|---|
| Cálida | +3 con ella |
| Tibia | +1 con ella |
| Fría | 0 y +1 a `desaires_cap1` |

- Los puntos salen **solo de los eventos de hermana de los hubs**. Los beats fijos no dan puntos.
- Una visita por hermana y capítulo: **techo de 9** en los tres capítulos.
- **Punto 10:** al final, el jugador declara su amor y la elegida recibe +1. Si solo una hermana tiene 9, es la elegida por defecto.
- **Umbral 10** para evitar el final malo.
- **Desempate:** `primera_conexion`, la primera hermana con la que el jugador eligió rama cálida o tibia. Si no participa del empate: Ichika > Nino > Miku > Yotsuba > Itsuki.
- **Los puntos se ven** al cerrar cada capítulo en la barra de progreso de las chicas (`14_progreso_chicas.rpy`, % = puntos × 10). En el diálogo nunca se mencionan.

Siempre con el helper, nunca a mano:

```renpy
$ sumar_punto("miku", 3)
```

Es lo único que garantiza que `primera_conexion` se escriba una sola vez. La lógica
del cálculo final está documentada en comentarios en `00_definiciones.rpy` (§8).

El prólogo no da puntos: sus menús son cosméticos y reconvergen.

---

## Finales

Ocho: cinco románticos, dos malos y uno secreto.

| Final | Condición | Estado |
|---|---|---|
| Ichika / Nino / Miku / Yotsuba / Itsuki | La elegida llega a 10 | ⬜ |
| Despido temprano | Dos ramas frías en el Capítulo 1 | ✅ |
| Despedida | Ninguna alcanza 10 al cerrar el Capítulo 3 | ⬜ |
| Final secreto | Completar las cinco rutas románticas | ⬜ |

### Despido temprano

Dos frías en el Capítulo 1 bastan. Lo que cambia es **cuándo**:

- **Variante A:** las dos frías llegan en los hubs 1 y 2. Maruo despide al
  protagonista en el beat de la crisis de Nino.
- **Variante B:** una fría antes del beat. Maruo da un ultimátum y, si el jugador
  vuelve a elegir fría en el hub 3, el despido llega al cierre del hub.

Con una sola fría, el capítulo sigue. Si llegó antes del beat, el Evento 6 empieza
en el estado «superado» (sobrevivió al ultimátum); si no, en «bueno» o «mixto»
según el clima del capítulo. No hay cortes en el Capítulo 2.

El temprano es un portazo: despedido por decir que no cada vez que pudo decir que
sí. La despedida del Capítulo 3 es otra cosa: llegó al final, estuvo cerca de todas
y no alcanzó a ninguna.

---

## El Capítulo 1

```
APERTURA → HUB 1 → evento → BEAT Itsuki → HUB 2 → evento
→ BEAT crisis de Nino → HUB 3 → evento → BEAT casa → EVENTO 6
```

Entre beat y beat se abre el **mapa**: el jugador elige a quién ir a buscar. Hay
cinco eventos de hermana y se juegan **tres por partida**; dos hermanas se quedan
sin evento cada vez, y eso es lo que hace que elegir pese. Cada evento funciona en
cualquiera de los tres huecos. Los beats fijos dan presencia a las cinco aunque
nadie las busque.

| Destino | Hermana |
|---|---|
| Sala de ensayo | Ichika |
| Centro comercial | Nino |
| Biblioteca | Miku |
| Pista de atletismo | Yotsuba |
| Aula, después de clases | Itsuki |

**La tesis del capítulo:** no son cinco alumnas malas, son un estudiante completo
repartido en cinco personas. Sumando lo mejor de cada una sale un boletín perfecto.

El **Evento 6** es la semana de exámenes: un día por hermana, un minijuego para las
que tuvieron rama cálida, el chat de grupo, el boletín, la barra de progreso, los
créditos y el «Continuará».

Detalle en [`docs/CAPITULO_1/CAP1.md`](docs/CAPITULO_1/CAP1.md).

---

## Herramientas

| Para qué | Herramienta |
|---|---|
| Motor | Ren'Py 8.5.3 |
| Imágenes | PixAI (modelo base Tsubaki.2) con LoRAs de la comunidad |
| Posproducción | Scripts propios en Python (Pillow, NumPy, SciPy) y GIMP |
| Interfaz y logo | Scripts propios con Pillow |
| Música | 魔王魂, DOVA-SYNDROME (OpenTracks) y un cover de piano de TheChiporpoise, con permiso |
| Efectos | 効果音ラボ, Freesound (CC0), Springin' Sound Stock y síntesis propia |
| Edición de audio | Audacity |
| Tipografías | M PLUS Rounded 1c, Shippori Mincho B1, Klee One y Noto Sans JP (SIL OFL 1.1) |
| Asistencia de código y guion | Claude |

---

## Notas de desarrollo

- Assets solo contra guion escrito: primero el capítulo entero, luego la lista de
  assets y recién ahí generar.
- La diferencia entre expresiones tiene que estar en la silueta: a un 30 % de
  tamaño la cara no se lee.
- Guardar la semilla de cada fondo, CG y sprite que funcione.
- Probar en Ren'Py después de cada bloque. Ante un error, copiar el `traceback` completo.
- Ninguna línea de diálogo pasa de dos líneas de la caja de texto (~100 caracteres).
