# Barra de progreso de las chicas (cierre del Cap. 1). Plan de implementación

> **Para agentes:** sub-skill: superpowers:executing-plans (ejecución en esta misma sesión). Los pasos usan casillas (`- [ ]`).

**Objetivo:** tras `cortinilla_cap1_fin`, una pantalla «Cinco nombres» con cinco tarjetas que muestran la afinidad de cada hermana como % (puntos×10), con silueta/contorno/retrato por umbral y llenado animado que se puede saltar.

**Arquitectura:** archivo nuevo `14_progreso_chicas.rpy` con datos (`PROG_IMAGEN`), funciones puras (`prog_imagen`, `prog_linea`), una sola `screen progreso_chicas(valores, anim)` y el `label progreso_chicas`. Patrón de `cortinilla`/`hub_completado`: tiempos precalculados al abrir, ATL por pieza, el guion espera con `renpy.pause`. La pantalla nunca escribe puntos.

**Tecnología:** Ren'Py 8.5.3 (screen language, ATL, `DynamicDisplayable`), 1920×1080.

**Especificación:** `docs/superpowers/specs/2026-11-15-barra-progreso-design.md`.

## Restricciones globales

- `porcentaje = min(100, puntos_<h> * 10)`. Solo lectura de `puntos_*`: ni `sumar_punto` ni asignaciones.
- Sin ternarios; todo `add`/`text`/`show` lleva su posición.
- Pantalla **sin** `modal` (GUIA_UI §5: se traga la pausa).
- Último fotograma animado = estado estático (`anim=False`), comprobado por captura.
- Stings por `cort_sonar(...)` (canal `cortinilla`): `"completado_<h>"` si pct ≥ 30, `"completado_<h>_tibia"` si 10 ≤ pct < 30. Sin música, sin ducking.
- Si `preferences.transitions == 0` → `anim=False`.
- Ningún texto por debajo de 30 px.
- Lint: `"/c/Users/PERSONAL/Desktop/renpy-8.5.3-sdk/renpy.exe" "The Fifth Choice" lint`. Avisos previos conocidos: `camara.mp3` y las sentencias inalcanzables de `00_definiciones.rpy`.
- No tocar `README.md` ni `CAP1.md`.

## Foco de revisión

1. Clic justo al terminar la tarjeta de fin: la pausa blindada de 0,5 s evita que ese clic salte la barra entera (comprobar en Tarea 4 con doble clic rápido).
2. Todas en 0 % (partida con tres frías no llega aquí, pero el preset sí): la pantalla no puede quedarse muda ni colgada; `total` mínimo 2,4 s.
3. Porcentajes fuera de los umbrales (20, 40, 70) en capítulos futuros: tratamiento por rango, no por igualdad (`prog_tratamiento`), cubierto en la autocomprobación.
4. Puntos > 10 (bonus futuro): tope 100, la barra no se sale.
5. Guardar/cargar o rollback dentro de la animación: vuelve a empezar desde 0 sin stings duplicados (la pantalla animada se reemplaza, sus `timer` mueren con ella).

---

### Tarea 1: Datos y lógica pura + autocomprobación

**Archivos:** crear `The Fifth Choice/game/14_progreso_chicas.rpy` (bloque `init python`).

**Produce:**
- `PROG_IMAGEN: dict[str, dict[int, str]]` — por hermana, umbral → ruta. Umbrales 0, 30, 60, 90, 100. Rutas `sprites/<h>_sprites/<h>_<expr>.png`; 0 = `neutral`; 30 = ichika `sonriendo`, nino `pillada`, miku `animada`, yotsuba `sonriendo`, itsuki `sonriendo`; 60 = `radiante`; 90 = `boda`; 100 = `boda_ramo`.
- `PROG_MARCAS = [30, 60, 90, 100]`
- `prog_valores() -> dict[str, int]` — lee `puntos_*`, `min(100, max(0, p * 10))`.
- `prog_imagen(h, pct) -> str` — umbrales de `PROG_IMAGEN[h]` de mayor a menor; primero `<= pct` con `renpy.loadable(ruta)`. El 0 siempre.
- `prog_tratamiento(pct) -> str` — `"silueta"` (< 10), `"contorno"` (10–29), `"retrato"` (≥ 30).
- `prog_linea(valores) -> dict` — `{"total": float, h: {"entra", "inicio", "dur", "sting_t", "jingle", "cambios": [(t, ruta), ...]}}`. Algoritmo:
  ```
  entra_i = 0.6 + i * 0.15
  T = 1.8
  para h en PETALO_ORDEN con pct > 0:
      inicio = T ; dur = 0.025 * pct
      sting_t = inicio + 0.025 * 30 si pct >= 30, si no inicio + 0.025 * 10
      cambios = [(inicio + 0.025*u, prog_imagen(h, u)) para u en 30,60,90,100 si u <= pct y la ruta cambia respecto a la anterior]
      T = inicio + dur + (1.4 si pct >= 30, si no 0.8)
  total = max(T, 2.4)
  ```
  Las de 0 %: `inicio = None`, sin sting, sin cambios.
- `prog_autocomprobar()` — asserts; la llama la Tarea 4.

- [ ] Escribir `prog_autocomprobar()` primero, con estos asserts:
  - `prog_tratamiento(0) == "silueta"`, `(9) == "silueta"`, `(10) == "contorno"`, `(20) == "contorno"`, `(30) == "retrato"`, `(70) == "retrato"`
  - `prog_imagen("nino", 30).endswith("nino_pillada.png")`; `prog_imagen("miku", 100).endswith("miku_animada.png")` (respaldo: no existen 60/90/100); `prog_imagen("ichika", 10).endswith("ichika_neutral.png")`
  - `L = prog_linea({"ichika": 30, "nino": 0, "miku": 10, "yotsuba": 30, "itsuki": 0})`: `L["nino"]["inicio"] is None`; `abs(L["ichika"]["inicio"] - 1.8) < 1e-6`; `abs(L["miku"]["inicio"] - (1.8 + 0.75 + 1.4)) < 1e-6`; `L["miku"]["jingle"] == "completado_miku_tibia"`; `L["ichika"]["jingle"] == "completado_ichika"`; `abs(L["total"] - (1.8 + 0.75 + 1.4 + 0.25 + 0.8 + 0.75 + 1.4)) < 1e-6`
  - `prog_linea({h: 0 para todas})["total"] == 2.4`
  - `len(prog_linea({"ichika": 100, ...0})["ichika"]["cambios"]) == 1` (solo el 30 cambia de ruta mientras no existan 60/90/100)
- [ ] Implementar lo de **Produce** hasta que `prog_autocomprobar()` pase (se ejecuta desde la consola: `$ prog_autocomprobar()` sin error).
- [ ] Lint limpio.

### Tarea 2: Piezas visuales (tarjeta estática)

**Archivos:** `14_progreso_chicas.rpy` (funciones y screens auxiliares).

**Consume:** Tarea 1. `ui_mezclar`, `PETALO_COLOR`, `PETALO_ORDEN`, `CORT_FONDO`, `HUB_FUENTE`, `HUD_FUENTE`, `gui.name_text_font`, `screen barra_progreso` (08_extras), `ui/flor.png`.

**Produce:**
- `prog_busto(ruta) -> Displayable` — `Crop((90, 0, 580, 560), ruta)` escalado al ancho del retrato.
- `prog_silueta(ruta) -> Displayable` — `Transform(prog_busto(ruta), matrixcolor=BrightnessMatrix(-1.0))`.
- `prog_contorno(ruta, color) -> Displayable` — 8 copias `BrightnessMatrix(1.0) * TintMatrix(color)` desplazadas ±3 px (incluidas diagonales), en un `Fixed`.
- `PROG_TARJ_W = 300`, `PROG_TARJ_SEP = 40`, `PROG_TARJ_X0 = (1920 - 5*300 - 4*40) // 2` (130), `PROG_BARRA_W = 260`.
- `screen prog_tarjeta(h, pct)` — estado final de una tarjeta: fondo `ui_mezclar(color, "#FFFFFF", 0.35)` (con `SaturationMatrix(0.0)` si pct == 0), retrato según `prog_tratamiento`, nombre (≥ 40 px, `gui.name_text_font`), `use barra_progreso(pct, 100, color, PROG_BARRA_W)`, flores de `PROG_MARCAS` sobre la barra en `x = PROG_BARRA_W * m / 100` (alcanzada: su color; si no, `#4A3D5C`; zoom ≈ 0,35), y «`pct` %» (≥ 56 px).

- [ ] Implementar lo de **Produce**.
- [ ] Lint limpio.

### Tarea 3: Pantalla completa animada + label + llamada

**Archivos:** `14_progreso_chicas.rpy`; modificar `02_cap1_evento6.rpy` (tras `call cortinilla_cap1_fin`, l. ~4794).

**Consume:** Tareas 1 y 2; transforms `cort_entra`, `cort_texto`, `cort_sube`, `cort_brota`, `cort_aparece`; `cort_rect`, `cort_y`, `cort_sonar`.

**Produce:**
- `screen progreso_chicas(valores, anim=True)` (zorder 80, sin modal):
  - `Solid(CORT_FONDO)`, líneas diagonales `cort_rect(5, ...)` como la cortinilla; rótulo «CAPÍTULO 01» (`HUB_FUENTE`, 40, kerning 8) y título «Cinco nombres» (84, contornos de la cortinilla) con `cort_texto`; «CLIC PARA CONTINUAR» (`HUD_FUENTE`, 30, kerning 4) abajo a la derecha, también en estático.
  - `anim=False`: cinco `use prog_tarjeta(h, valores[h])`, sin transforms.
  - `anim=True`: tarjeta `i` con `cort_sube(L[h]["entra"])`; dentro, la tarjeta dibuja silueta + fondo desaturado + barra en 0 y, si `inicio` no es None:
    - relleno `Solid(color)` de `PROG_BARRA_W × 12` con transform `prog_llena(inicio, dur)` (`xzoom 0.0` → `linear dur xzoom 1.0` tras `pause inicio`, `xanchor 0`) multiplicado por `pct/100` en el ancho
    - % en vivo: `DynamicDisplayable(prog_cuenta, inicio, dur, pct)` que devuelve `Text(str(int(...)) + " %")` con el mismo estilo que el estático
    - en `inicio + 0.25` (cruce 10 %): fondo `SaturationMatrix` 0 → 1 en 0,3 s; contorno `alpha` 0 → 1 con pulso (1 → 0,6 → 1) si `prog_tratamiento(pct) == "contorno"`
    - cada `(t, ruta)` de `cambios`: destello `Solid("#FFFFFF")` alfa 0 → 0,8 → 0 en 0,35 s; crossfade 0,4 s a `prog_busto(ruta)`; la silueta/contorno sale a alfa 0
    - flores-marca alcanzadas: `cort_brota(inicio + 0.025 * m)`
    - `timer L[h]["sting_t"] action Function(cort_sonar, L[h]["jingle"])`
  - Todo valor final de ATL igual al estático (alfa 1, xzoom 1, saturación 1, offset 0).
- `label progreso_chicas(valores=None)`: guarda/apaga `quick_menu`, `window hide`; `valores = prog_valores()` si None; `anim = preferences.transitions != 0`; `show screen progreso_chicas(valores, anim)` con `Dissolve(0.4)`; si anim: `renpy.pause(0.5, hard=True)`, `renpy.pause(total - 0.5)`, `show screen progreso_chicas(valores, False)`; luego `renpy.pause()`; `stop cortinilla fadeout 0.6`; `hide screen progreso_chicas` con `Dissolve(0.8)`; restaura `quick_menu`; `window auto`; `return`.
- En `02_cap1_evento6.rpy`: `call progreso_chicas` en la línea siguiente a `call cortinilla_cap1_fin`.

- [ ] Implementar la pantalla y el label.
- [ ] Añadir la llamada en `02_cap1_evento6.rpy`.
- [ ] Lint limpio.

### Tarea 4: Label de prueba + comprobación visual

**Archivos:** `14_progreso_chicas.rpy`; temporal `The Fifth Choice/game/zz_capturas_tmp.rpy` (crear y borrar con su `.rpyc`).

- [ ] `label progreso_chicas_prueba` (consola: `jump progreso_chicas_prueba`): `stop music`, `stop ambiente`, `$ prog_autocomprobar()`, y `call progreso_chicas(...)` con estos cinco presets en orden:
  1. todas 0
  2. ichika 30, nino 0, miku 30, yotsuba 30, itsuki 0
  3. ichika 30, nino 30, miku 10, yotsuba 0, itsuki 0
  4. ichika 30, nino 10, miku 0, yotsuba 0, itsuki 0
  5. ichika 60, nino 90, miku 100, yotsuba 30, itsuki 10
- [ ] Capturas con la técnica de los planes del 14-11 (`run --warp`, `renpy.screenshot` a la carpeta scratchpad, `renpy.quit()`). Para los presets 2, 4 y 5:
  - a) animada en `total + 0.3` s y b) estática → **comparar píxel a píxel** (Pillow `ImageChops.difference(...).getbbox()` debe ser `None`).
  - c) animada a mitad del llenado de la primera hermana (silueta + contorno encendido / barra a medias).
- [ ] Mirar las capturas: texto no recortado, nada < 30 px, siluetas legibles sobre su fondo, marcas sin texto.
- [ ] Si el warp falla: pedir al usuario que juegue `progreso_chicas_prueba` y compruebe a ojo, incluido el doble clic rápido (Foco 1) y guardar/cargar a mitad (Foco 5).
- [ ] Borrar `zz_capturas_tmp.rpy` y su `.rpyc`. Lint limpio.

### Tarea 5: Revisión de diseño (Impeccable)

- [ ] Pasar las capturas de la Tarea 4 por `impeccable:impeccable` en modo crítica, con este contexto: lenguaje de las cortinillas, tarjetas de hermana, sin estética de gacha.
- [ ] Aplicar solo los arreglos materiales que no contradigan el diseño aprobado; repetir capturas y la comparación píxel a píxel si cambia algo.

### Tarea 6: Documentación

**Archivos:** `00_definiciones.rpy:126-127`, `docs/CAPITULO_1/EVENTO_6/ANALISIS_EVENTO_6.md:711,719`, `docs/CAPITULO_1/EVENTO_6/PLAN_CHATS_EVENTO_6.md` §1.A, `docs/GUIA_UI.md` §2 y §4.

- [ ] `00_definiciones.rpy`: cabecera «Puntos de afinidad»; sustituir «INVISIBLES… Nunca se muestran en pantalla» por: se muestran solo en la barra de cierre de capítulo (`14_progreso_chicas.rpy`) como % = puntos×10; el diálogo nunca los menciona.
- [ ] `ANALISIS_EVENTO_6.md:711`: columna «No hacer» → «Mostrar números de afinidad en la escena o en la matriz»; columna «Por qué» → «La afinidad solo se ve como % en la barra de cierre de capítulo (D-13); la matriz solo muestra notas».
- [ ] `ANALISIS_EVENTO_6.md:719`: «Rompe el cálculo secreto» → «Rompe el misterio de las rutas; los puntos solo se ven en la barra de cierre (D-13)».
- [ ] `PLAN_CHATS_EVENTO_6.md` §1.A: fila **D-13**: «La afinidad se muestra como % (puntos×10) solo en la barra de cierre de capítulo; el diálogo y la voz interior siguen sin mencionar puntos».
- [ ] `GUIA_UI.md`: fila de `14_progreso_chicas.rpy` en la tabla §2; receta §4 «Barra de progreso de las chicas» (llamada, `PROG_IMAGEN` y el respaldo, cómo añadir imágenes de 60/90/100, prueba `jump progreso_chicas_prueba`, salto con «Transiciones» apagado).
- [ ] Sin tocar: `ANALISIS:385`, `CAP1_evento_6_nucleo.md:1137,1192`, `00_definiciones.rpy:186`, `README.md`, `CAP1.md`.
