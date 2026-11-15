# Guía de UI — The Fifth Choice

Todo lo aprendido montando la interfaz. **Transversal**: vale para los tres capítulos que quedan.

---

## 1. Idea de diseño

- **Cinco motivos, uno por hermana:** destello (Ichika), mariposa (Nino), ecualizador (Miku), trébol (Yotsuba), estrella (Itsuki). La **flor de sakura de cinco pétalos** es la marca del juego.
- **Colores:** `PETALO_COLOR` en `07_ui.rpy`. Neutro `#D9D2E6`; Isanari `#A9925C`; Raiha `#F5B7B1`. El rosa de Ichika es **solo de Ichika**.
- **Formas:** cintas en paralelogramo, panel izquierdo con borde inclinado y cinco bandas, cajas redondeadas translúcidas.
- **Regla:** cada hermana lleva su color en todo lo que es suyo (caja de diálogo, tarjeta, pestaña, final). El neutro va en lo que no es de nadie.

## 2. Archivos

| Archivo | Qué contiene |
|---|---|
| `00_definiciones.rpy` | los `Character` (con `ui_personaje`) |
| `07_ui.rpy` | funciones de UI, flor, HUD, cinta del lugar, decisiones con peso |
| `07b_collage.rpy` |	Collage de pensamientos del beat casa (datos `COLLAGE_CG` y `COLLAGE_POS`)
| `06_main_menu.rpy` | menú principal |
| `08_extras.rpy` | Galería (datos en GALERIA), Finales y el popup de versiones (final_versiones) |
| `09_menus_sistema.rpy` | Guardar, Cargar, Opciones, Historial, Acerca de, Ayuda, confirmaciones |
| `hub_mapa.rpy` |	Pantalla del mapa de hubs (`HUB_DESTINOS`, el orden de la tabla es el orden en pantalla)
| `14_progreso_chicas.rpy` | Barra de progreso de las chicas al cerrar un capítulo (`PROG_IMAGEN`, `progreso_chicas`) |
| `screens.rpy` | `say`, `choice`, menú rápido |
| `herramientas/generar_ui.py` | genera todos los PNG de `game/ui/` |
| `herramientas/generar_logo.py` | genera el logo con los sprites `neutral` |
| `herramientas/recortar_menu.py` | prepara los sprites del menú |
| `herramientas/generar_fondos_collage.py` | Genera `game/ui/collage_fondo_<hermana>.webp` |

## 3. Regenerar los PNG

`cd herramientas` y `python generar_ui.py` → `game/ui/`. Las constantes (opacidad de la decoración, alturas de tarjeta…) están arriba del script. **Si un número está también en un `.rpy`** (por ejemplo `TARJETA_ALTOS`, o `HUB_SELLO` = 128, que vive en `generar_ui.py` y en `hub_mapa.rpy`), cámbialo en los dos sitios.

Los fondos del collage: python `generar_fondos_collage.py`. Importa `generar_ui.py`, así que tienen que estar en la misma carpeta.

## 4. Recetas

- **Decisión con peso:** `$ decision_peso("hermana", "Pregunta", "Por qué importa")` justo antes del `menu:`. Las opciones van en orden cálida, tibia, fría.
- **Menú cuyas opciones son hermanas:** `$ ligera_hermanas = {"Ichika": "ichika"}` antes del `menu:` y `$ ligera_hermanas = {}` al terminar.
- **Hub o beat:** `$ ui_escena("hub", destino, lugar)` ... `$ ui_escena("normal")` (los beats usan `"beat"`).
- **Fondo nuevo:** añadirlo a `BG_LUGAR`; si no debe verse en el prólogo, también a `BG_OCULTOS_PROLOGO`. «Las variantes `_anochecer` se declaran con `Transform` sobre el mismo webp y también van en `BG_LUGAR`»
- **CG nuevo:** añadirlo a `GALERIA` (`08_extras.rpy`). El porcentaje se recalcula solo.
- **Sprite nuevo del menú:** generar (768×1280, cuerpo completo) → `recortar_menu.py` → ruta en `MENU_SPR` → calibrar `MENU_CORONILLA` con `MENU_GUIA = True`.
- **Personaje nuevo:** `ui_personaje(nombre, color, petalo, deco)`.
- **Capítulo en los guardados:** `$ save_name = "Capítulo 2"` al empezar cada capítulo.
- **Final revivible:** crear label final_<clave> que termine en return. La carta o caja de Finales se vuelve clicable sola cuando el final está conseguido y el label existe (final_label() usa renpy.has_label).
- **Final con versiones:** añadir cada versión a FINALES_TEMPRANO (08_extras.rpy) con su label y su scope, y poner su flag persistent.final_malo_temprano_<v>_visto en el cierre del final. El popup la muestra bloqueada hasta que se vea.
- **Nombre en replays:** todo Replay de Finales pasa por final_scope(), que añade persistent.nombre_jugador. Ese valor se guarda en configurar_nombre.
- **Galería:** el contador de cada pestaña es una pastilla de tamaño fijo con el motivo de la hermana de marca de agua. Se rellena cuando la sección está completa. La paginación usa el motivo de la hermana tintado con su color.
- **Collage de recuerdo:** `call collage_abrir("ichika")` … pensamientos … `call collage_cerrar`. Si la hermana no fue visitada, `collage_abrir` no hace nada y collage_cerrar tampoco.
- **Mapa de hub:** `$ quick_menu = False`, `call screen mapa_hub(n)`, `$ quick_menu = True`. Las visitadas se bloquean con `hub_visitadas`.
- **Indicador de tarde (mapa):** `screen hub_indicador_tarde(n)` bajo el subtítulo: tres `ui/flor.png` + «TARDE n DE 3» en `HUD_FUENTE`. La flor de cada tarde jugada lleva el tono de la hermana elegida según su rama (`hub_tono`, ver abajo; `hub_visitadas[k-1]` va en orden de tarde); la actual, blanca y más grande; las que faltan, blancas apagadas. Colores, alfas y zooms en `hub_flor_tarde(k, n)`. Con `marca=segundo` (lo usa `hub_completado`) la flor de la tarde `n` se tiñe animada de `marca_color`.
- **Tono por rama (sello y flor):** `hub_tono(hermana, rama)` en `hub_mapa.rpy` es el ÚNICO sitio que decide el color. Cálida = `PETALO_COLOR`; tibia = pálido (`ui_mezclar` hacia el neutro al 55 %); fría = gris `#8E8A96`; `None` (showcase, pruebas) = el color de siempre. La rama se lee con `rama_de(h)`: no hay historial aparte. Lo usan el sello del mapa, `hub_flor_tarde` y `hub_completado`.
- **Hub completado:** `call hub_completado(destino, n)` justo después de `$ hub_visitadas.append(destino)` (n = 1, 2 o 3). Sobre el mapa: la banda se enciende, hace el motivo de la hermana, se estampa el sello (parámetro `anim` de `hub_sello`) y la flor de la tarde se tiñe; después funde a negro. Variante por `rama_de(destino)`: cálida ~2,8 s (motivo con remate, pétalos), tibia ~1,5 s (media luz, motivo sin remate, tono pálido), fría ~0,6 s (sello gris seco, sin motivo). Tiempos en `HUBC_RITMOS`; los de `sello` y `flor` están copiados en `generar_cortinillas.py` (`RITMOS_HUBC`). Motivos: `HUBC_CHISPAS` (Ichika), `HUBC_EQ` (Miku), `HUBC_ESTELA` (Itsuki); PNG `ui/hub_motivo_<h>.png`, `hub_barra.png`, `hub_aro.png`. Sonido `cort_completado_<h>[_tibia].ogg` / `cort_completado_fria.ogg` por el canal `cortinilla` (si falta, sale mudo). Prueba: consola → `jump hub_completado_prueba` (5 hermanas × 3 ramas).
- **Entrada y salida de un minijuego:** viven en `10_mj_transicion.rpy` y las llama SOLO `mj_ejecutar`; ningún minijuego se toca. Idea: «la columna de la hermana se abre» (vertical + regla horizontal; las cortinillas son diagonales y el hub, bandas y sello). Entrada ~2 s, una vez por minijuego (no en los reintentos ni en el modo «saltar» ni en «Saltarlo»): velo y columna entran, la chibi hace su gesto y presenta «MINIJUEGO · MATERIA» (`E6_MATERIA`) + título del registro sobre una regla de su color; el título se recoge hacia la columna y el último fotograma es **idéntico** al primero de `mj_marco` (comprobado píxel a píxel: chibi `neutral` en `MJ_CHIBI_X/Y`, zoom 1.0). Salida «ganado» ~1,6 s (chibi `feliz`, celebración, la columna sale y funde a la escena); «saltado» ~1,4 s (chibi `animo`, asiente, un solo motivo, sin celebración). Gestos: Yotsuba corre y pasa el testigo (la regla sale disparada) / sale corriendo; Ichika foco y haz que enciende el título / reverencia y el foco se cierra; Nino sube con un «hmph» y una mariposa descubre el título / dos mariposas; Itsuki estrella que cae y título que se escribe y se subraya / la estrella sube; Miku todo en cuatro tiempos de 0,3 s, cortes secos / se mece tres tiempos y todo se corta en el cuarto (velo incluido). Tiempos en `MJTR_RITMOS` y `MJTR_CUES`; los de `MJTR_CUES` están copiados en `generar_cortinillas.py` (`RITMOS_MJTR`). PNG nuevo `ui/mj_foco.png` (foco de Ichika y halo de Itsuki); el resto reutiliza `hub_motivo_<h>`, `hub_barra`. Sonido `cort_mj_<h>_<entrada|ganado|saltado>.ogg` por el canal `cortinilla`, sin tocar el volumen de la música (las campanitas tienen ataque: no se duckea). Prueba: consola → `jump mj_transicion_prueba` (5 hermanas × entrada, marco, ganado, saltado).
- **Barra de progreso de las chicas (cierre de capítulo):** `call progreso_chicas` justo después de la cortinilla de fin (en el Cap. 1, tras `cortinilla_cap1_fin`; el final malo no pasa por ahí). Solo LEE `puntos_*`: % = puntos × 10, tope 100. Pantalla «Cinco nombres»: cinco tarjetas en `PETALO_ORDEN`; < 10 % silueta negra sobre gris ciruela (`PROG_GRIS`); 10–29 % silueta con brillo casi blanco teñido de su color; ≥ 30 % se revela la imagen. Imágenes por umbral en un solo dict, `PROG_IMAGEN` (0, 30, 60, 90, 100; los nombres futuros son `<h>_radiante`, `<h>_boda`, `<h>_boda_ramo`). Si falta un PNG, `prog_imagen` usa el del umbral inferior: para estrenar un umbral basta con crear el archivo. Flores-marca sin texto en 30/60/90/100. Animación: tarjetas escalonadas, llenado de una en una (0,025 s por 1 %), las de 0 % no gastan tiempo, un sting por hermana (`cort_completado_<h>` si ≥ 30, `_tibia` si 10–29) por el canal `cortinilla`, sin música. **El golpe de esos .ogg no está al principio**: cae en su «sello» (`HUBC_RITMOS[rama]["sello"]`, 1,20 s cálida / 0,70 s tibia), así que el sting se lanza antes para que el golpe coincida con el cruce del umbral, y la barra siguiente espera a que el anterior acabe (solapa solo 0,6 s, con fundido: `prog_sonar`). Duraciones en `PROG_STING_DUR`, copiadas de `j_completado` en `generar_cortinillas.py`. Tiempos en `PROG_*`, calculados por `prog_linea`. Un clic salta al estado final (el último fotograma es idéntico, comprobado píxel a píxel) y otro clic continúa. Con «Transiciones» apagado en Opciones sale directa en su estado final. Prueba: consola → `jump progreso_chicas_prueba` (5 presets + `prog_autocomprobar()`).
- **Sello de visitada (mapa):** `use hub_sello(hermana, color, x, y, anim=hub_sello_estado)`; el color sale de `hub_tono`. `x, y` = centro del disco en pantalla (la banda lo coloca en `HUB_SELLO_Y` siguiendo la diagonal con `hub_offset`). Va **fuera** del botón para que no le llegue el gris de `hub_visitado`. PNG: `ui/hub_sello_<hermana>.png` (doble aro y motivo, blanco, se tiñe) + `ui/hub_sello_fondo.png` (disco, se tiñe oscuro). Para animarlo (hub completado): pasarle otro transform en `anim` o cambiar `hub_sello_estado`; la banda no se toca.
- **Foco del mapa:** la banda con el ratón o el teclado sube y las demás se apagan con un velo negro con su forma (`hub_velos()`, `HUB_FOCO_VELO`). El foco se lee con `GetTooltip("mapa_hub")`. El velo va **encima** del botón y no lo envuelve: envolver el botón en un transform que cambia con el foco puede quitarle el foco.
- **Nombre de banda:** `use hub_banda_nombre(d)` dentro de un contenedor de `HUB_CARD_W` de ancho. Lo comparten el botón del mapa y `hub_completado`.
- **Rendimiento del mapa:** paneles, velos y sombra se montan una vez por apertura con `default` en `mapa_hub` (y en `hub_completado`). No llamar a `hub_panel()` dentro de la pantalla: son 32 capas de degradado por banda y se rehacían en cada hover.
- **Tipografía del mapa:** los nombres siguen en M PLUS Rounded (es el key visual promocional); las etiquetas pequeñas («TARDE n DE 3», «VISITADA») usan `HUD_FUENTE` en mayúsculas con `kerning 4`, como la cinta del HUD.
- **Botón nuevo:** `hover_sound` `audio.sfx_hover` y `activate_sound audio.sfx_click`. El mapa usa `sfx_hhover` y `sfx_hclick`.

## 5. Trampas

- Mayúsculas antes de interpolar rompe `[variable]`: `renpy.substitute()` primero.
- `hovered`/`unhovered` con variable se queda pegado al cambiar de pantalla: usar `tooltip`/`GetTooltip()`.
- El `Character` pisa el fondo que se ponga en la pantalla `say`.
- `narrator` (sin "d") es el narrador interno: cajas vacías de transiciones y preguntas de menú.
- Los cambios en `init python` no entran con recarga rápida: cerrar y abrir el juego.
- FINALES_TEMPRANO es un define: se evalúa en init y no puede leer persistent. Lo que dependa del jugador (el nombre) se añade en final_scope().
- **Pantalla + `renpy.pause` nunca con `modal True`.** El modal se traga el temporizador y el clic de la pausa (también con `hard=True`): la pausa no termina y el juego se queda colgado sin error. Por eso `cortinilla` y `hub_completado` no son modales. `modal` solo sirve con `call screen` (como `mapa_hub`).
- **Animación que debe empalmar con una pantalla:** el último fotograma tiene que dibujar lo mismo, en el mismo sitio y con los mismos valores finales (offset 0, alfa 1, zoom 1, `rotate None` al acabar un giro con `rotate_pad False`). El título con barrido usa `fixed: fit_first True` con una copia invisible del texto: el `crop` cambia el tamaño y, centrado, el texto se desplazaría.
- El collage apaga `quick_menu`, y de eso cuelga todo el HUD. Si se sale de un collage sin `call collage_cerrar`, la interfaz no vuelve.
