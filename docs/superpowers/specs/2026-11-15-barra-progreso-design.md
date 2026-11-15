# Barra de progreso de las chicas — diseño

Fecha: 2026-11-15 · Ren'Py 8.5.3 · 1920×1080

## 1. Intención

Al cerrar el Capítulo 1 (solo final bueno), el jugador ve por primera vez cuánto
avanzó con cada hermana. Es la recompensa visible de un capítulo de decisiones
invisibles: las que trató bien «aparecen»; las que no, siguen siendo sombras.
El sistema de puntos deja de ser secreto **solo aquí**: el diálogo y la voz
interior siguen sin mencionar puntos.

## 2. Objetivos, no objetivos, anti-objetivos

**Objetivos**
- Cinco tarjetas, orden canónico `PETALO_ORDEN`, con retrato que se revela por
  umbral y barra con %.
- Sistema de umbrales completo (0/10/30/60/90/100) con respaldo de imagen, para
  que los capítulos 2 y 3 solo añadan PNG.
- Habla el lenguaje de `13_transiciones.rpy`: `CORT_FONDO`, líneas diagonales,
  `cort_texto`, `cort_sube`, `cort_brota`, flores.

**No objetivos**
- Entrada en Extras (decidido: solo cierre de capítulo).
- Sonido de llenado nuevo (no hace falta: los stings cargan el momento).
- Música (decidido: silencio + stings, GUIA_AUDIO §8).
- Nuevas imágenes.

**Anti-objetivos (sería un fracaso aunque funcione)**
- Que escriba o sume puntos.
- Que aparezca en el final malo.
- Que el último fotograma de la animación difiera del estado estático.
- Que parezca un HUD de gacha («Affection Lv.», corazones, niveles con nombre).
- Que spoilee los umbrales futuros (nada de «boda» escrito en pantalla).

## 3. Restricciones

- Cálculo: `porcentaje = puntos_<h> * 10`, tope visual 100. Cap. 1: 0, 10 o 30.
  Solo 3 hubs por partida: al menos 2 hermanas en 0 %.
- Lectura sin escritura: la pantalla recibe un dict `{hermana: porcentaje}`;
  el label lo arma leyendo `puntos_*` o lo recibe ya hecho (pruebas).
- Convenciones D-12: código completo, sin ternarios, todo `show` con posición.
- GUIA_UI: pantalla + `renpy.pause` **sin** `modal`. Último fotograma = estático.
- Canal `cortinilla` para los stings (`cort_sonar`).

## 4. Enfoques considerados

| | Enfoque | Contra principal |
|---|---|---|
| **A (elegido)** | Una pantalla con tiempos precalculados al abrir; ATL para piezas, `DynamicDisplayable` para el contador, `timer` para los stings; el guion espera con `renpy.pause` | Algo de cuenta en Python al abrir |
| B | Estado que avanza con `timer 0.03 repeat` | Redibuja sin parar, estado mutable frágil en rollback/carga, más código |
| C | Guion paso a paso (`show screen` + pausas) | Un clic salta un paso, no todo; rollback paso a paso |

Elegido A por el usuario: es el patrón de `cortinilla` y `hub_completado`, y el
estado final coincide con el estático por construcción.

## 5. Decisiones del usuario

1. **10 %:** silueta negra con contorno de su color (3–4 px), sin imagen nueva.
2. **Imagen del 30 %:** Ichika `sonriendo`, Nino `pillada`, Miku `animada`,
   Yotsuba `sonriendo`, Itsuki `sonriendo`.
3. **Fondo:** `CORT_FONDO` liso + las dos líneas diagonales de la cortinilla.
   Cada tarjeta lleva su fondo lavado en su color (contraste con la silueta);
   en 0 % ese fondo va desaturado.
4. **Título:** rótulo «CAPÍTULO 01», título «Cinco nombres» (eco de «Hace un mes
   anoté cinco nombres…»).
5. **Extras:** no. Solo en el cierre.
6. **Animaciones reducidas:** no existe preferencia propia; si
   `preferences.transitions == 0` (Opciones → «Transiciones» apagado) se muestra
   el estado final directo.
7. **Música:** ninguna. Stings sobre silencio.
8. **Enfoque A.**

## 6. Diseño

### 6.1 Archivos
- **Nuevo** `game/14_progreso_chicas.rpy`: datos, funciones, transforms,
  pantalla, `label progreso_chicas`, `label progreso_chicas_prueba`.
- `02_cap1_evento6.rpy`: una línea `call progreso_chicas` tras
  `call cortinilla_cap1_fin` (línea ~4794). Esa ruta ya excluye el final malo
  (que usa `cortinilla_final_malo` en otra rama).
- `08_extras.rpy`: se **reutiliza** `screen barra_progreso` para pista + relleno
  del estado estático (sin cambios). La versión animada dibuja el mismo
  `Solid` con `xzoom` 0→1 anclado a la izquierda, que termina idéntico.

### 6.2 Umbrales e imágenes (un solo dict)

```
PROG_IMAGEN = {
  "ichika":  {0: ".../ichika_neutral.png", 30: ".../ichika_sonriendo.png",
              60: ".../ichika_radiante.png", 90: ".../ichika_boda.png",
              100: ".../ichika_boda_ramo.png"},
  ... (las cinco)
}
PROG_UMBRALES = [0, 10, 30, 60, 90, 100]
PROG_MARCAS   = [30, 60, 90, 100]
```

- Rutas de archivo (no nombres de `image`), para comprobar con `renpy.loadable`.
- `prog_imagen(h, pct)`: recorre los umbrales con imagen de mayor a menor; toma
  el primero `<= pct` cuyo archivo exista. Si falta, baja al siguiente. El 0
  (neutral) siempre existe.
- Tratamiento: `pct < 10` silueta; `10 <= pct < 30` silueta + contorno;
  `pct >= 30` imagen revelada.
- Nombres futuros `_radiante`, `_boda`, `_boda_ramo`: **llamada mía** (regla
  GUIA_RENPY: nombrar por expresión; la boda es atuendo). Hoy no existen y caen
  al `sonriendo`/`pillada`/`animada`.

### 6.3 Silueta y contorno (en código)
- Silueta: `Transform(img, matrixcolor=BrightnessMatrix(-1.0))` (negro, conserva
  alfa).
- Contorno: 8 copias de la silueta teñidas de `PETALO_COLOR[h]`
  (`TintMatrix` sobre la versión blanca `BrightnessMatrix(1.0)`), desplazadas
  ±3 px en las 8 direcciones, detrás de la silueta negra.
- Retrato: el busto se recorta como `final_sprite` (`Crop((90, 0, 580, 560))`,
  sprites 760×930), escalado al ancho de la tarjeta.

### 6.4 Composición (1920×1080)
- Fondo `Solid(CORT_FONDO)` + líneas diagonales arriba y abajo (`cort_rect`).
- Rótulo «CAPÍTULO 01» (`HUB_FUENTE`, 40, kerning 8) y título «Cinco nombres»
  (`gui.name_text_font`, 84, contornos como la cortinilla), con `cort_texto`
  arriba a la izquierda.
- Cinco tarjetas de ~300 px de ancho, separación ~40 px, centradas (≈1660 px).
  Cada una, de arriba abajo: retrato sobre fondo lavado en su color · nombre
  (≥ 40 px) · barra con marcas · porcentaje grande (≥ 56 px).
- Marcas 30/60/90/100: `ui/flor.png` pequeña sobre la barra. Alcanzada = su
  color; no alcanzada = `#4A3D5C` (el «apagado» de las flores de la cortinilla).
  Sin texto en las marcas.
- Indicación de cierre «CLIC PARA CONTINUAR» (`HUD_FUENTE`, ≥ 30 px, kerning 4)
  abajo a la derecha, visible igual en animado y estático.
- Legibilidad en móvil: ningún texto por debajo de 30 px.

### 6.5 Línea de tiempo (animado)
- 0,0 s: fondo y líneas (`cort_entra`); 0,3 s rótulo; 0,5 s título.
- 0,6 s + i·0,15 s: tarjeta i sube (`cort_sube`), en silueta, fondo
  desaturado, barra 0, «0 %».
- Desde 1,8 s: llenado **de una en una** en orden canónico, solo las que tienen
  `pct > 0` (las de 0 % ya están en su estado final y no gastan tiempo).
  - Llenado lineal, 0,25 s por cada 10 %; el % cuenta en vivo.
  - Al cruzar 10 %: el fondo de la tarjeta recupera saturación y se enciende el
    contorno (pulso de alfa).
  - Al cruzar 30 % (y 60/90/100 si cambia la imagen): destello blanco sobre el
    retrato (alfa 0→0,8→0 en 0,35 s) + crossfade 0,4 s silueta→imagen. Las
    flores-marca alcanzadas brotan (`cort_brota`).
  - **Sting: uno por hermana, el del umbral final** (llamada mía: dos stings en
    0,75 s chocarían en un canal único): `cort_completado_<h>.ogg` si
    `pct >= 30`, `cort_completado_<h>_tibia.ogg` si `10 <= pct < 30`. Suena al
    cruzar ese umbral.
  - Respiro antes de la siguiente: 1,4 s tras un 30 %+, 0,8 s tras un 10 %.
- Peor caso Cap. 1 (3 × 30 %): ≈ 1,8 + 3·(0,75 + 1,4) ≈ 8,3 s.

### 6.6 Guion y control
```
label progreso_chicas(valores=None):
    quick_menu off, window hide (como cortinilla)
    valores None -> {h: min(100, puntos_h * 10)}
    si transiciones apagadas: anim False
    show screen progreso_chicas(valores, anim)   (sin modal)
    si anim:
        renpy.pause(0.5, hard=True)       # el clic que cerró la tarjeta no se la lleva
        renpy.pause(total - 0.5)          # clic -> pasa al estado final
        show screen progreso_chicas(valores, False)
    renpy.pause()                         # clic para continuar
    stop cortinilla fadeout 0.6
    hide screen + Dissolve(0.8), restaurar quick_menu, window auto
```
- Clic durante la animación: se muestra el estático; los stings pendientes ya no
  suenan (sus `timer` viven en la versión animada). El sting en curso termina.
- Guardar/cargar o rollback dentro de la animación: la sentencia se repite y la
  animación vuelve a empezar. Aceptado (es lo que hacen `cortinilla` y
  `hub_completado`). La pantalla no guarda estado propio.

### 6.7 Prueba
`label progreso_chicas_prueba` (consola, Shift+O → `jump progreso_chicas_prueba`),
presets sin tocar `puntos_*`:
1. Todo en 0.
2. Tres cálidas (30/30/30/0/0).
3. Dos cálidas + una tibia.
4. Una de cada tipo (30 / 10 / 0 fría / 0 / 0).
5. Forzado 60 / 90 / 100 / 30 / 10 (comprueba el respaldo de imágenes).

### 6.8 Docs
- `00_definiciones.rpy:126-127`: quitar «INVISIBLES»; explicar que la barra del
  cierre de capítulo los muestra como % (puntos×10).
- `ANALISIS_EVENTO_6.md:711` y `:719`: actualizar (la afinidad se ve en la barra
  de cierre; la voz interior sigue sin hablar de ella).
- `PLAN_CHATS_EVENTO_6.md` §1.A: **D-13** «La afinidad se muestra como %
  (puntos×10) solo en la barra de cierre de capítulo; el diálogo y la voz
  interior siguen sin mencionar puntos».
- `GUIA_UI.md` §4: receta «Barra de progreso de las chicas».
- **No se tocan** (siguen siendo ciertas): `ANALISIS:385`,
  `CAP1_evento_6_nucleo.md:1137` y `:1192` (la matriz de notas nunca muestra
  afinidad), `00_definiciones.rpy:186` (desaires siguen invisibles).
  Ni `README.md` ni `CAP1.md`.

## 7. Lo que queda al constructor
- Medidas finas de tarjeta, alto del retrato y posición del título, siempre que
  el texto quepa y nada baje de 30 px.
- Forma exacta del pulso del contorno y del destello.
- Revisión visual final con Impeccable antes de cerrar.
