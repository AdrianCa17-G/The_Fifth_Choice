# Guía de Ren'Py — The Fifth Choice

Trampas del motor ya encontradas y convenciones del proyecto. Todas están pagadas
con horas: leer antes de tocar código.

---

## 1. Convenciones del proyecto

### Dónde vive cada cosa

`00_definiciones.rpy` concentra todo lo que no es narrativa: personajes,
variables, fondos, sprites, transforms, audio, funciones, la pantalla de nombre y
`label start`.

La interfaz vive aparte: `06_main_menu.rpy`, `07_ui.rpy`, `08_extras.rpy` y
`09_menus_sistema.rpy` (ver `GUIA_UI.md`).

Los archivos de capítulo contienen su label y lo que solo ese evento usa: 
sus CG, sus fondos (con su variante _anochecer) y sus audios propios. Si otro 
archivo lo reutiliza, sube a 00_definiciones.rpy. Hoy pasa con `bg_aula_tarde`, 
`cg_nino_confrontacion_cocina` y `sfx_taza_mesa`, que usan los finales malos. 
Funciona porque los define son globales, pero es deuda, no bug.

Esto estuvo escrito antes que cumplido: el prólogo llevaba dentro los fondos, los
sprites, los transforms y el audio entero, y funcionaba solo porque los `define`
son globales. El Capítulo 1 habría colgado del archivo del prólogo. Antes de
abrir un capítulo nuevo, comprobar que lo que va a usar está declarado donde
corresponde.

### `label start` es único

Vive en `00_definiciones.rpy` y en ningún otro archivo. Los demás usan
`label prologo`, `label cap1_inicio`, etc. Un `label start` duplicado es un error
de carga.

### Los puntos se suman con el helper

```renpy
$ sumar_punto("nino", 2)
```

En los eventos de hermana: cálida `sumar_punto("x", 3)`, tibia `sumar_punto("x", 1)`, 
fría `$ desaires_cap1 += 1` (sin puntos). Cada evento guarda su rama en `<h>_rama_cap1`
("calida", "tibia", "fria"; se lee con `rama_de("x")`) y marca `<h>_visitada_cap1 = True` 
antes del return. El beat de Nino usa `nino_rama_beat` y no `toca desaires_cap1`.

Nunca tocar `puntos_*` a mano. El helper es lo único que garantiza que
`primera_conexion` se escriba una sola vez, y de eso depende el desempate de toda
la partida.

### Las expresiones son atributos, no nombres

```renpy
image miku neutral = "sprites/miku_sprites/miku_neutral.png"   # bien
image miku_animada = "sprites/miku_sprites/miku_animada.png"   # mal
```

Con guion bajo, Ren'Py no ve una expresión de Miku: ve un personaje distinto
llamado `miku_animada`. `hide miku` no lo quita, `show miku` no lo reemplaza y
acabas con dos Mikus en pantalla a la vez — el mismo destrozo que los sprites
encimados, por otra puerta. El `.png` sí lleva guion bajo; la declaración no.

Nombrar por expresión, nunca por rol: la cara en reposo es `neutral` aunque
parezca aburrida. `miku_aburrida` hubo que renombrarlo por eso.

### Nombres de archivo

Sin espacios, sin tildes, en minúsculas. Ren'Py distingue mayúsculas en Linux y
Android: funciona en Windows y revienta al exportar. `Ichika_sonrisa.png` con
mayúscula ya costó una regeneración.

Las imágenes se declaran con ruta explícita: `image bg_aula = "bg/aula.webp"`.

---

## 2. La regla del `show`

**Todo `show` lleva SIEMPRE su posición, aunque solo cambie el tinte.**

```renpy
show nino neutral at pj(X_NINO)
show nino at pj_habla(X_NINO)
show nino at pj_calla(X_NINO)
```

Esto no es estilo. Es lo único que impide que vuelva el bug más caro del proyecto.

### El bug de los sprites encimados

`at` **reemplaza el transform entero, no lo suma.** Cuando se escribía
`show nino at habla`, no se le añadía el tinte a la posición: se la quitaba.
Ren'Py intenta salvarlo heredando el estado del transform anterior, y lo que
hereda es el estado **en ese instante exacto**.

El transform de movimiento usaba `ease t xcenter x` con `t = 1` segundo. Si el
jugador hacía clic a los 200 ms, el sprite iba por el 20 % del recorrido, el
siguiente `show ... at habla` congelaba ese 20 % y ya no se movía nunca más. De
ahí los sprites encimados y las regresiones rotas.

La causa de fondo es una asimetría del motor que conviene tener grabada:

> **Un clic salta una transición a su estado final. Un clic NO adelanta una
> animación ATL.** Por eso el movimiento tiene que ser una transición, nunca un
> `ease` dentro del transform.

Reafirmar la posición absoluta en cada `show` hace que una transición interrumpida
se autocorrija en la línea siguiente.

### Movimientos y entradas

```renpy
show ichika at pj(0.25)
with mover

show nino neutral at pj(0.75)
with dissolve
```

Primero el desplazamiento de quien ya estaba, después la entrada del nuevo con
`dissolve`. Se encadenan solas sin clic de por medio.

**Trampa de `MoveTransition`:** sus parámetros `enter` y `leave` esperan un
**transform con la posición de partida** (`offscreenright` y similares), no una
transición. Pasarles `dissolve` no falla al cargar el juego — revienta en tiempo
de render con `AttributeError: 'NoneType' object has no attribute 'style'`, ya
dentro de la escena, y el error no menciona el parámetro culpable. Por eso `mover`
va pelado y las entradas se resuelven aparte.

Para salidas, `hide <tag>` con `moveoutleft`. Antes se movía el sprite a
`xcenter -0.5` y se quedaba cargado fuera de pantalla.

### Otras transiciones

| Transición | Cuándo |
|---|---|
| `dissolve` | BG↔CG de la misma escena y entrada de un sprite nuevo |
| `disolucion_lenta` (0.4 s)	| Cambio de expresión o de quién habla (`show x at pj_habla`(...)) |
| `fade` | Cambio de lugar dentro del mismo día |
| `fade_dia` (0.7 / 0.4 / 0.7) | Salto de día o noche explícito en el texto |
| `corte_seco` (0.1 s)	| Aparece Maruo o un golpe de guion |

Varios scene seguidos sin texto en medio: el primero con fade, el resto con dissolve.

---

## 3. Trampas ya encontradas

**Borrar el `.rpyc` junto al `.rpy`.** Si eliminas un archivo y dejas su
compilado, Ren'Py lo sigue cargando y el error reaparece idéntico. Es la causa
número uno de «lo borré y sigue fallando».

**Los cambios en un `init python` no entran con recarga rápida.** Hay que cerrar y
volver a abrir el juego entero. Si un cambio de comportamiento «no hace nada»,
este es el primer sospechoso, antes que el código.

**Al reemplazar un sprite hay que borrar `game/cache`** o Ren'Py sigue mostrando
la versión vieja. Es el equivalente del `.rpyc` para las imágenes: pasas media
hora normalizando un sprite y en pantalla no cambia nada.

**Renombrar un `define audio.X` obliga a renombrar todos sus `play`.** Al
reorganizar las carpetas se acortaron tres `play music` sin tocar sus `define`, y
el archivo quedó a medias: cinco pistas con prefijo y tres sin él, apuntando a
nombres inexistentes.

**Después de un CG hay que volver al fondo antes de mostrar un sprite.** `scene
cg_lo_que_sea` deja el CG como escena; si el siguiente `show` no lleva delante su
`scene bg_*`, el personaje aparece pegado encima de la ilustración. Va en la misma
línea de guion:

```renpy
scene bg_biblioteca
with dissolve
show miku neutral at pj(0.5)
```

**Las pantallas se dibujan por encima de los sprites**, así que la caja de diálogo
nunca queda tapada por un personaje.

**El canal `sound` es único.** Dos `play sound` seguidos con poco texto de por
medio se cortan entre sí si el jugador va rápido. O el primero dura menos de un
segundo, o hace falta registrar un segundo canal.

**`volume` multiplica de verdad por encima de 1.0.** No está limitado a 1. Pero
amplificar un archivo ya normalizado lo empuja por encima del techo digital y
puede saturar: si un efecto cruje, es esto.

**Mayúsculas antes de interpolar rompen `[variable]`.** `.upper()` convierte
`[mc]` en `[MC]`, que no existe: sustituir primero con `renpy.substitute()` y
después pasar a mayúsculas.

**`hovered` / `unhovered` con una variable se quedan «pegados»** si la pantalla
cambia con el ratón encima. Usar `tooltip` y `GetTooltip()`, que se limpian solos.

**`window_style` y `window_background` del `Character` pisan** lo que se ponga en
la pantalla `say`: los fondos por personaje van en el `Character`.

**`narrator` (sin la «d») es el narrador interno** de Ren'Py: lo usan las cajas
vacías de las transiciones y las preguntas de los `menu:`.

**Pantallas con el mismo nombre en archivos distintos:** gana la de mayor
prioridad de carga. Los estilos de `screens.rpy` (init −1) no ven variables de
`00_definiciones.rpy` (init 0): lo que usen va en `gui.rpy`.

**Un `default` dentro de una pantalla se evalúa una vez por apertura**, y sirve
para decidir «primera vez» (la entrada animada del menú principal).

**En ATL, las operaciones van entre paréntesis:** `rotate (i * 72)`.

**La música del menú principal se reinicia** si el `Play` va dentro de la
pantalla: usar `define config.main_menu_music`, que suena una sola vez aunque se
entre y salga de los submenús.

**`config.all_character_callbacks`** se ejecuta en cada línea de diálogo: sirve
para detectar cambios de fondo y enseñar la cinta del lugar con `renpy.show_screen`.

**`size_group`** en un estilo de botón iguala el ancho de todos los del grupo al
del más largo (las cajas de decisión ligeras).

**Un Replay arranca con el estado limpio.** Todas las variables vuelven a su default 
y solo sobrevive persistent. Lo que el label necesite
(nombre, *_rama_cap1, despido_en_beat) se pasa con Replay(label, scope={...}). 
Sin eso, las ramas leen None y se saltan los bloques «fría».
También arranca en negro: todo label revivible abre con su propio scene + with, 
o el Replay empieza sin fondo.

**play sound ... loop ocupa el canal sound hasta el stop sound:** cualquier otro play 
sound en medio lo corta.

**Salir de un call sin volver (un final malo desde un beat):** $ renpy.pop_call() y luego 
jump. Sin el pop_call, la pila queda con un return pendiente.

---

## 4. Diagnóstico rápido

Cuando algo «no hace nada», en este orden:

1. ¿Existe el `.rpyc` viejo? Bórralo y relanza.
2. ¿Es un cambio en `init python`? Cierra el juego entero, no recargues.
3. ¿Se está ejecutando la línea? Mete un `$ renpy.notify("aquí")` temporal justo
   antes. Si el aviso no aparece, el problema no es lo que crees que es.
4. ¿Estás saltando la escena con el avance rápido? Muchos efectos duran menos de
   dos segundos y pasan de largo.

Antes de dar por bueno un archivo grande, cruzar defines contra usos:

```python
import re, glob
s = "".join(open(f, encoding="utf-8-sig").read() for f in glob.glob("*.rpy"))
defs  = set(re.findall(r'define audio\.(\w+)\s*=', s))
plays = set(re.findall(r'play (?:sound|music|ambiente) (\w+)', s))
print("audio sin uso:", defs - plays)
print("audio sin define:", plays - defs)

imgs = {m.strip() for m in re.findall(r'^image ([\w ]+?)\s*=', s, re.M)}
tags = {i.split()[0] for i in imgs}
used = set(re.findall(r'^\s*(?:scene|show) ([a-z_]\w*)', s, re.M))
print("sin declarar:", {u for u in used if u not in tags and u not in imgs})

print("audio con punto (error):", re.findall(r'audio\.sfx\.\w+', s))
```


Sobre todos los `.rpy` a la vez, no sobre uno: desde que las declaraciones viven
en definiciones y los usos en los capítulos, mirar un archivo suelto da falsos
positivos en las dos direcciones.

Es diez segundos y pilla justo el fallo que no se ve leyendo.
