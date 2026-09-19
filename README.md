# The Fifth Choice

Fan visual novel basada en **Quintessential Quintuplets** (Go-toubun no Hanayome).
Parte del arranque del anime y sigue por su cuenta: los personajes son los de la
obra, la historia es propia. Las decisiones del jugador determinan con cuál de las
cinco quintillizas termina.

**Motor:** Ren'Py 8.5.3 · **Desarrollo:** Adrian (AdrianKiller17) · **Proyecto fan sin ánimo de lucro**

---

## Estado

| Fase | Archivo | Estado |
|---|---|---|
| 0 · Núcleo | `00_definiciones.rpy` | ✅ Terminado |
| 1 · Prólogo | `01_prologo.rpy` | ✅ Terminado — 7 escenas, arte y audio completos |
| 2 · Capítulo 1 | `02_capitulo1.rpy` | 🟨 En escritura — guion en `docs/CAP1.md`; apertura y evento de Miku, Yotsuba, Itsuki cerrados |
| 3 · Capítulo 2 | `03_capitulo2.rpy` | ⬜ Pendiente |
| 4 · Capítulo 3 | `04_capitulo3.rpy` | ⬜ Pendiente |
| 5 · Finales | `05_finales.rpy` | ⬜ Pendiente |
| — · Menú principal | `06_main_menu.rpy` | ✅ Terminado |

---

## Documentación

| Documento | Qué contiene |
|---|---|
| Este README | Estructura, sistemas de juego, personajes, progreso |
| [`docs/PROLOGO.md`](docs/PROLOGO.md) | Estado detallado del prólogo: escenas, guion, assets, problemas abiertos |
| [`docs/CAP1.md`](docs/CAP1.md) | Capítulo 1: decisiones de diseño, estructura de hubs, guion y assets pendientes |
| [`docs/GUIA_ARTE.md`](docs/GUIA_ARTE.md) | Generación de imágenes: PixAI, LoRAs, prompts, estándar de sprites, scripts de post |
| [`docs/GUIA_AUDIO.md`](docs/GUIA_AUDIO.md) | Fuentes, licencias, escala de volumen, montaje |
| [`docs/GUIA_RENPY.md`](docs/GUIA_RENPY.md) | Trampas del motor ya encontradas y convenciones de código |
| [`CREDITOS.md`](CREDITOS.md) | Atribuciones, licencias de los assets y aviso de proyecto fan |

Las tres guías son **transversales**: valen para los tres capítulos que quedan,
no solo para el prólogo. Consultarlas antes de generar arte nuevo o tocar audio.

---

## Estructura del proyecto

```
Quintuplets/
└── The Fifth Choice/
    ├── README.md                       ← esta página
    ├── docs/
    │   ├── PROLOGO.md
    │   ├── CAP1.md
    │   ├── GUIA_ARTE.md
    │   ├── GUIA_AUDIO.md
    │   └── GUIA_RENPY.md
    ├── herramientas/                    fuera de game/ — scripts de Python
    │   ├── normalizar_sprite.py
    │   ├── normalizar_extra.py
    │   ├── limpiar_halo.py
    │   └── escalar_cgs.py
    └── game/
        ├── audio/
        │   ├── bgm/                     8 pistas .ogg
        │   ├── sfx/                     11 efectos .mp3
        │   └── amb_viento.ogg
        ├── images/
        │   ├── bg/                      8 fondos, 1920×1080 WebP
        │   ├── cg/                      13 ilustraciones de escena
        │   ├── sprites/
        │   │   ├── ichika_sprites/
        │   │   ├── nino_sprites/
        │   │   ├── miku_sprites/
        │   │   ├── yotsuba_sprites/
        │   │   ├── itsuki_sprites/
        │   │   ├── raiha_sprites/
        │   │   └── isanari_sprites/
        │   ├── Fondo_Menu.png
        │   ├── Logo_Menu.png
        │   └── petal.png
        ├── fonts/
        │   ├── NotoSansJP-Regular.ttf    solo para el japonés de los créditos
        │   └── OFL.txt                   licencia, obligatorio distribuirla
        ├── 00_definiciones.rpy          ✅
        ├── 01_prologo.rpy               ✅
        ├── 06_main_menu.rpy             ✅
        ├── gui.rpy · options.rpy · screens.rpy
        │
        │   ── todavía no creados ──
        ├── 02_capitulo1.rpy             ← siguiente
        ├── 03_capitulo2.rpy
        ├── 04_capitulo3.rpy
        ├── 05_finales.rpy
        │
        │   ── generado por Ren'Py, no versionar ──
        ├── cache/  saves/  tl/  libs/  gui/
        └── *.rpyc
```

`cache/`, `saves/`, `tl/`, `libs/` y los `.rpyc` los crea y mantiene Ren'Py sola.
No deben subirse al repositorio: el `.gitignore` de la raíz ya los excluye.


### Qué va en cada `.rpy`

`00_definiciones.rpy` concentra **todo lo que no es narrativa**: personajes,
variables, imágenes compartidas (fondos y sprites), transforms, audio, funciones
de apoyo, la pantalla de nombre y `label start`.

Los archivos de capítulo contienen **solo su `label` y sus CG propios**. Un CG es
la ilustración de un momento concreto; si alguno acaba reutilizándose en otro
capítulo, se sube a definiciones.

Esto se cumple desde el reparto de bloques: el prólogo llegó a tener dentro los
fondos, los sprites, los transforms y todo el audio, y de ahí subieron. Con ellos
subieron `cg_calificacion`, `cg_maruo_reunion` y `cg_hermanas_estudiando`, que la
apertura del Capítulo 1 reutiliza. Los otros diez CG del prólogo siguen en su
archivo.

`label start` vive en `00_definiciones.rpy` y en ningún otro sitio.

---

## Estructura narrativa

```
PRÓLOGO → CAPÍTULO 1 → CAPÍTULO 2 → CAPÍTULO 3 → CÁLCULO SECRETO → EPÍLOGO
```

Estilo narrativo tipo *Doki Doki Literature Club*: el sistema de puntos es
invisible y el jugador no elige a nadie explícitamente.

### Protagonista

Futaro Uesugi por defecto, nombre personalizable al inicio (`nombre_jugador`).
**Nunca se muestra su rostro.** En escenas grupales aparece como silueta oscura,
y en los CG se encuadra de espaldas, desenfocado y cortado por el borde.

No es una decisión estética sino técnica: no existe LoRA de Futaro, así que
cualquier intento de generarlo de frente sale como silueta negra o con la cara
rota. Sin rostro no hay nada que el modelo pueda estropear.

---

## Las cinco quintillizas

| Personaje | Color | Personalidad |
|---|---|---|
| Ichika | `#FFB7C5` rosa | Actriz, coqueta, la primera en actuar |
| Nino | `#C39BD3` morado | Tsundere, protectora, la más intensa |
| Miku | `#5DADE2` azul | Tímida, historia, desarrollo lento |
| Yotsuba | `#58D68D` verde | Energética, noble, la más dulce |
| Itsuki | `#EC7063` rojo | Seria, estudiosa, rivalidad → amor |

Como las cinco tienen la misma cara, el jugador las distingue por silueta.
Cualquier expresión nueva tiene que leerse al 30 % de tamaño.

### Itsuki tiene dos objetos de personaje

El protagonista no sabe su nombre hasta la escena 5 del prólogo, cuando ella se
lo grita. Hasta entonces la caja de diálogo dice **«Estudiante Nueva»**
(`itsuki_inicio`); a partir de ahí, `itsuki`. El color va en la constante
`C_ITSUKI` para que los dos no puedan desincronizarse.

### Desviaciones del canon — decisiones cerradas

No son errores. Conviene tenerlas presentes al escribir diálogo para no
contradecirlas en el texto:

- **Nino lleva el pelo corto desde el inicio.** Los LoRAs disponibles solo la
  generan así. Nunca describirla con el pelo largo en narración.
- **Miku es castaña, no azul pálido.** El LoRA no da el tono azul. El color
  `#5DADE2` sigue valiendo para su caja de diálogo; lo que cambia es el pelo.
- **Miku va de sudadera, no de uniforme.** Decisión propia, no limitación de la
  herramienta. La separa visualmente de las otras cuatro justo en las escenas
  donde el bloque de hermanas es el problema, y fuera de casa sigue vestida
  igual: es su ropa, no un atuendo de escena.
- **Sus audífonos van colgados del cuello**, nunca puestos, y subírselos es un
  gesto con significado: es como cierra la puerta. Ninguna narración debe
  describirlos «puestos» si el sprite los tiene abajo.

---

## Sistema de finales

Ocho finales: cinco románticos, dos malos y uno secreto.

| Final | Condición |
|---|---|
| Ichika / Nino / Miku / Yotsuba / Itsuki | Más puntos con ella, mínimo 10 |
| Final Malo temprano | Tres desaires en el Capítulo 1 → despido inmediato |
| Final Malo | Ninguna alcanza 10 puntos al cerrar el Capítulo 3 |
| Final Secreto | Completar las cinco rutas románticas |

### Los dos finales malos no significan lo mismo

Son dos fracasos distintos y se narran distinto.

El **temprano** es el despido por no haber empezado nunca. Se dispara si el
jugador elige la opción fría en los tres eventos del Capítulo 1. Maruo no está
ni enojado: es seco y casi administrativo. Futaro vuelve a casa con la deuda
intacta. Cierra en `bg_cuarto_mc`, donde empezó todo.

El **del Capítulo 3** es el que ya estaba diseñado: llegó hasta el final, estuvo
cerca de todas y no alcanzó a ninguna. Ese duele porque hubo recorrido.

El primero es un portazo; el segundo es una despedida.

### Por qué esto resuelve la contradicción de Maruo

Maruo promete despido si una hermana reprueba. El juego mide afinidad. Eran dos
condiciones distintas y solo se ejecutaba la segunda.

Queda cerrado así: **la afinidad representa «logró llegar a ellas y por eso
estudian»**. Cada capítulo cierra con las hermanas aprobando, así que la
condición de Maruo se cumple mientras Futaro esté llegando a ellas. Si al final
no lo consiguió, el Final Malo se narra como el despido que él anunció en el
prólogo. Una sola condición, dicha una vez y ejecutada una vez.

### El contador de desaires

Va **aparte** de los puntos y también es invisible. Sube solo cuando el jugador
elige la opción fría dentro de un evento de hermana — no la tibia, no la
neutral: la que corta el vínculo. No resta afinidad.

```renpy
default desaires_cap1 = 0
```

Vive en `00_definiciones.rpy`, con los `puntos_*`.

Se lee una sola vez, al cerrar el Capítulo 1. Con 3 de 3, despido.

La diferencia con el umbral de 10 importa: al jugador no lo despiden por **no
haber sumado suficiente**, lo despiden por **haber dicho que no cada vez que
pudo decir que sí**. Eso el jugador lo reconoce, porque se acuerda de haberlo
elegido.

**Aviso diegético.** Si al llegar al beat de la crisis de Nino el contador ya
está alto, aparece una escena condicional corta: Maruo comenta que lleva un mes
y no ve diferencia con los tutores anteriores. El jugador que va camino al
despido recibe el aviso de boca del personaje que puso la condición, sin ver un
número. El que va bien nunca sabe que esa escena existe.

No hay cortes en el Capítulo 2. Un jugador que pasó el primero ya demostró que
está jugando.

### Cálculo secreto

Los puntos son **invisibles**: no se muestran, no se comentan en diálogo y no hay
menú de selección. Se resuelven al cerrar el Capítulo 3.

- **Umbral mínimo: 10 puntos.** Castiga al jugador disperso.
- **Orden de comparación:** ichika → nino → miku → yotsuba → itsuki.
- **Desempate:** gana `primera_conexion`, la primera chica con la que el jugador
  tuvo una decisión positiva. Si está vacía o no participa del empate, se aplica
  la prioridad canónica del orden anterior.

La lógica completa, con el esqueleto de código listo para la Fase 5, está
documentada en comentarios dentro de `00_definiciones.rpy`.

### Reglas al escribir decisiones

Usar **siempre** el helper, nunca sumar a mano:

```renpy
$ sumar_punto("miku", 2)
```

Es lo único que garantiza que `primera_conexion` se escriba una sola vez y que
el desempate de toda la partida quede bien fijado.

**El prólogo no otorga puntos.** Sus tres menús son cosméticos: cambian el
diálogo inmediato y reconvergen. La primera decisión puntuada del juego es la
elección de destino en el **primer hub del Capítulo 1**: el jugador no elige una
respuesta, elige a quién va a buscar. Eso escribe `primera_conexion`.

### Valores

| Acción | Puntos |
|---|---|
| Evento de hermana, primera vez en el capítulo | +2 |
| Decisión acertada dentro de ese evento | +1 |
| Revisitarla en el mismo capítulo (escena corta, sin decisión) | +1 |
| Preparar material para ella en la biblioteca | +1 |
| Beats fijos de trama | 0 |

Máximo por hermana y capítulo: **5**. Máximo en la partida: **15**.

Con esto, el jugador que se concentra cruza el umbral de 10 durante el Capítulo
3, que es donde debe pasar. El que alterna entre dos llega raspando con las dos
y el desempate hace su trabajo. El que reparte entre las cinco se queda en seis
o siete y cae en el Final Malo. El umbral de 10 funciona sin tocarlo.

---

## Herramientas

| Para qué | Herramienta |
|---|---|
| Motor | Ren'Py 8.5.3 |
| Generación de imágenes | PixAI (modelo base Tsubaki.2) |
| Corrección local de imágenes | Gemini |
| Post de sprites y CG | Scripts propios de Python (`herramientas/`) con pillow, numpy y scipy |
| Música | 魔王魂 y DOVA-SYNDROME |
| Efectos de sonido | 効果音ラボ |
| Ambiente | Springin' Sound Stock |
| Edición de audio | Audacity |
| Tipografía japonesa | Noto Sans JP (SIL OFL 1.1), solo para los créditos |
| Asistencia de código y guion | Claude |

Detalles de configuración en [`docs/GUIA_ARTE.md`](docs/GUIA_ARTE.md) y
[`docs/GUIA_AUDIO.md`](docs/GUIA_AUDIO.md).

---

## Estructura de los capítulos

Los tres capítulos que quedan no son lineales como el prólogo. Avanzan por
**beats fijos** de guion, y entre beat y beat se abre un **hub**: el mapa, el
jugador elige destino, ahí ocurre una escena, y el guion retoma. El tiempo entre
medias lo cuenta el narrador, no el motor.

Se descartó el modelo de calendario simulado. 60 días por capítulo con 6 eventos
deja 162 días vacíos en la partida y pide unos 70 fondos contando franjas
horarias. El hub da la misma libertad de elección sin un solo día muerto.

**Dos franjas horarias en todo el juego:** tarde y noche. El criterio es que si
no hay una razón narrativa para que una franja exista, no se genera.

### Esqueleto del Capítulo 1

```
APERTURA (fija) → HUB 1 → evento → BEAT Itsuki → HUB 2 → evento
→ BEAT crisis de Nino → HUB 3 → evento → BEAT casa → EVENTO 6 (fijo)
```

Cuatro bloques de guion y tres hubs. **Se escriben cinco eventos de hermana y el
jugador consume tres por partida**: dos hermanas se quedan sin evento cada vez.
Eso es el mecanismo, no un agujero — es lo que hace que elegir pese. Los beats
fijos existen para que las cinco tengan desarrollo aunque nadie las busque.

### El mapa

| Destino | Quién está ahí | Fondo |
|---|---|---|
| Aula, después de clases | Itsuki | ya existe |
| Pista de atletismo | Yotsuba | pendiente |
| Sala de ensayo | Ichika | pendiente |
| Centro comercial | Nino | pendiente |
| Biblioteca | Miku | pendiente |
| Casa de Futaro | Raiha | ya existe |

Cuatro fondos nuevos para todo el juego, reutilizados en los tres capítulos.

A Itsuki se la cruza en el terreno de él y a las otras cuatro hay que ir a
buscarlas al suyo. Sale gratis en arte y dice algo del personaje.

**La biblioteca** tiene dos verbos y son excluyentes en la misma visita: buscar a
Miku, o preparar material para una hermana concreta. Preparar material da un
punto con ella y le da línea propia en el evento 6. Así la biblioteca no necesita
una estadística de skills: lo que ganás no es un número, es una escena distinta
al final del capítulo.

El mapa crece y se encoge por capítulo. En el 1 el departamento es escenario de
beats, no destino. En el 2 se abren los cuartos de las hermanas, que es la
recompensa visible de haberse ganado su confianza. En el 3 el mapa se reduce:
menos opciones, más presión.

### Materias — reparto canónico

Las cinco nacieron con el mismo potencial y cada una desvió su atención a una
asignatura. Sumando el máximo de cada una sale un boletín perfecto, y eso cierra
sobre las cinco materias del examen japonés sin sobras ni huecos.

| Hermana | Materia |
|---|---|
| Ichika | Matemáticas |
| Nino | Inglés |
| Miku | Sociales / Historia |
| Yotsuba | Japonés / Literatura |
| Itsuki | Ciencias |

Esto es la tesis del Capítulo 1: **no son cinco alumnas malas, son un estudiante
completo repartido en cinco cuerpos.** Futaro no puede enseñarles a estudiar;
tiene que entrar por el único sitio donde cada una ya sabe que es buena. Es lo
que justifica el mapa, y hace que afinidad y rendimiento sean la misma medida.

El Final Secreto queda dicho por la obra misma: completar las cinco rutas es
reunir al estudiante perfecto.

### Criterio de arte

**Generar expresiones solo contra guion escrito**, nunca contra suposición.
`itsuki_timida` se generó antes de tener la escena y se quedó sin usar todo el
prólogo.

Esto vale para todo el arte, no solo para las expresiones. El orden es: escribir
el capítulo entero con marcadores, sacar la lista definitiva de assets del propio
guion, y recién ahí generar. Escribir es lo barato y lo corregible; un CG hecho
contra una escena que después cambia se tira entero.

---

## Notas

- Proyecto fan **gratuito**. No monetizar nunca.
- Trabajar un archivo `.rpy` por sesión.
- Probar en Ren'Py después de cada fase antes de continuar.
- Ante un error, copiar el `traceback` completo.
- **Guardar la semilla** de cada fondo, CG y sprite que funcione. Es lo único
  del trabajo de arte que no se puede recuperar después.
