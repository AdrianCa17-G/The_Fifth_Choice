# M3 «El compás» · Fase 1 sobre el mapa de pulsos — Plan de implementación

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Que las notas de la fase 1 caigan en los pulsos reales de `miku_tema.ogg` (tempo variable), con la fase 2 a tempo fijo enlazado con el final de la fase 1, sin cambiar la mecánica.

**Architecture:** Toda la temporización de `MJM3` pasa por una sola función `t_pulso(k)` (instante en la canción del pulso k). Hasta el pulso del cambio de fase lee `MIKU_PULSOS`; desde ahí suma pulsos fijos de `beat2`. Las corcheas, el cambio de fase, los tics, la cuenta atrás, el latido de la meta y el patrón del compás derivan de ella. El plan B fabrica una lista de pulsos uniforme y usa el mismo camino.

**Tech Stack:** Ren'Py 8.5.3, `game/10_mj_miku.rpy`, `game/10_mj_miku_pulsos.rpy` (generado en el paso 1).

**Spec:** el mensaje de la tarea (PARTE 1 · MAPA DE PULSOS) + el resumen del paso 1 (223 pulsos, primero 1,788 s).

## Global Constraints

- La MECÁNICA no cambia: mismos `MJ_PARAMS["m3"]`, `m3_fase1`, `m3_fase2`, `m3_generar`, carriles, combos, concentración, ventana y fases. Los eventos siguen contándose en corcheas desde el pulso 0.
- `persistent.m3_latencia_ms` y su ajuste quedan tal cual.
- Plan B (`MIKU_USAR_TEMA = False` → metrónomo en las dos fases) sigue funcionando.
- Código completo, sin ternarios. No se tocan el marco, la screen `mj_m3` (la adaptación al marco va en el plan siguiente) ni los `.md` existentes.
- Sin commits (no se han pedido).
- Lint: `"/c/Users/PERSONAL/Desktop/renpy-8.5.3-sdk/renpy.exe" "The Fifth Choice" lint`. Avisos previos conocidos: `camara.mp3` y las sentencias inalcanzables de `00_definiciones.rpy`.

## Decisiones

1. **Corchea → tiempo.** Corchea par `c`: `t_pulso(c // 2)`. Impar: punto medio entre `t_pulso(c // 2)` y `t_pulso(c // 2 + 1)`.
2. **Tempo de la fase 2:** `beat2 = (t_pulso(bc) − t_pulso(bc − 8)) / 8`, donde `bc` es el pulso del cambio. Es la media de los dos últimos compases que sonaron. Con el mapa actual sale entre 0,763 y 0,829 s (72,4–78,6 BPM; el cambio cae entre 24 y 56 s según nivel y sorteo). Con 4 pulsos salía entre 71,5 y 85,1 BPM por el rubato: se notaba. Constante `MIKU_F2_MEDIA = 8`.
3. **El hueco y la fase 2 arrancan en el pulso del cambio:** el primer tic suena en `t_pulso(bc)`, un pulso real de la canción, mientras la música se funde en 0,8 s. Luego, cada `beat2`.
4. **Plan B:** `self.pulsos = [k × 60 / MIKU_BPM]` para k = 0…bc. `MIKU_BPM` pasa a **76,9** (media de la canción, para que el plan B se sienta igual) y su comentario dice que solo vale para el plan B. **`MIKU_OFFSET` se borra**: el mapa ya lleva el desfase y en el plan B no hay música que alinear.
5. **Puntos de control** (`inicio > 0`): la fórmula `pos0 = abs_t[inicio] − abs_t[0]` se queda. Como `abs_t` ya son tiempos reales de la canción, la música arranca 4,98 s antes de la nota de reanudación: la misma entrada que la primera vez (1,79 s de intro + 4 pulsos locales). `sonar_desde` y `resincronizar` trabajan con la posición en la canción (`pos0 + reloj`) y no dependen del tempo: no cambian.
6. **Fuera del mapa:** `t_pulso` extrapola con el último intervalo si se pide un pulso más allá del final de `MIKU_PULSOS` (o con el primero, antes del pulso 0). Hoy no ocurre (como mucho se pide el pulso 68 de 223). La extrapolación solo evita un error si algún día se suben las notas.
7. **Modo de depuración:** `define M3_DEPURAR_TIC = False`. Con `True`, los tiempos de las notas de la fase 1 (desde `inicio`) se añaden a `self.tics`, y el tic suena en cada nota sobre la música. Se activa en la consola: `$ M3_DEPURAR_TIC = True` y luego `jump mj_probar_m3`.

## Review Focus

1. Reanudar desde un punto de control a mitad de la fase 1: las notas siguen cayendo en los pulsos de la música que arranca en `pos0`. → Task 1, prueba `inicio=12`.
2. Empezar directamente en la fase 2 (`inicio ≥ n1`): sin música, tics a `beat2`, sin error. → Task 1.
3. Plan B: rejilla uniforme a 60/76,9 s en las dos fases y cambio de fase coherente. → Task 1.
4. Cuenta atrás: muestra 4, 3, 2, 1 cambiando en cada pulso real (no con un tempo fijo). → Task 1.
5. Patrón del compás de la fase 2 (`slot_actual`) alineado con los tics. → Task 1.

---

### Task 1: Temporización por pulsos en `MJM3`

**Files:**
- Modify: `The Fifth Choice/game/10_mj_miku.rpy` (constantes l. 8–19; `MJM3.__init__` l. 146–234; `slot_actual`, `rotulo_fase`, `cuenta`, `pulso`)
- Test (temporal): `The Fifth Choice/game/zz_m3_prueba_tmp.rpy`

**Interfaces (métodos nuevos de `MJM3`):**
- `self.pulsos: list[float]`, `self.bc: int` (pulso del cambio de fase = `gen[1]`), `self.beat2: float`.
- `t_pulso(k: int) -> float`: segundos en la canción del pulso k (decisiones 2, 3 y 6).
- `t_corchea(c: int) -> float`: decisión 1.
- `fase_pulso(s: float) -> (int, float)`: para un instante `s` de la canción, el pulso en curso y la fracción recorrida (0–1). Por debajo de `t_pulso(bc)`, `bisect.bisect_right(self.pulsos, s) − 1`, y para `k < 0` se extrapola con el primer intervalo (usar `math.floor`). Desde `t_pulso(bc)`, analítico con `beat2`.
- Se elimina `self.beat`.

- [ ] **Step 1: Prueba (falla).** Crear `zz_m3_prueba_tmp.rpy` con un `init 999 python:` que, con `renpy.random.seed(n)`, construya `MJM3(MJ_PARAMS["m3"][nivel], inicio, nivel)` para los tres niveles, `inicio ∈ {0, 12}` y semillas 1–5. Que escriba `OK`/el fallo en `<scratchpad>/m3_prueba.txt` y compruebe:
  - para cada evento `i < n1`: `abs(v.ev[i][0] + v.pos0 − v.t_corchea(c)) < 1e-6`, y si `c` es par, `t_corchea(c) == MIKU_PULSOS[c // 2]`;
  - `abs(v.t_cambio + v.pos0 − MIKU_PULSOS[v.bc]) < 1e-6`;
  - `abs(v.beat2 − (MIKU_PULSOS[v.bc] − MIKU_PULSOS[v.bc − 8]) / 8) < 1e-9` y `0.70 < v.beat2 < 0.86`;
  - los tics son ≥ `t_cambio` y están separados `beat2` (± 1e-6);
  - `fase_pulso(MIKU_PULSOS[20] + 0.25 × (MIKU_PULSOS[21] − MIKU_PULSOS[20]))` da `(20, 0.25 ± 1e-6)`;
  - cuenta: con `v.estado = "juego"` y un `t0` fingido para que `t_juego() + pos0 = MIKU_PULSOS[k] + 0.01`, `cuenta()` da `"4"`, `"3"`, `"2"`, `"1"` para los 4 pulsos anteriores a la primera nota;
  - `inicio = n1`: `t_cambio == -1.0`, `usa_musica` es False, hay tics y no salta ninguna excepción;
  - plan B (`store.MIKU_USAR_TEMA = False` y restaurarlo después): todos los tics separados `60 / MIKU_BPM`; con `inicio=0`, el primero en 0,0; y las notas en la rejilla.
- [ ] **Step 2:** Lint → el archivo de prueba informa del fallo (`t_corchea` no existe).
- [ ] **Step 3: Constantes.** `MIKU_BPM = 76.9` (comentario: tempo del plan B; la fase 1 con tema usa `MIKU_PULSOS`). Borrar `MIKU_OFFSET`. Añadir `define MIKU_F2_MEDIA = 8` (comentario: compases que promedia el tempo de la fase 2). Añadir `import bisect` y `import math` en el `init python`.
- [ ] **Step 4: `__init__`.** Tras `gen = m3_generar(...)`: `self.bc = gen[1]`; `self.pulsos = MIKU_PULSOS` con tema, o la lista uniforme del plan B; `self.beat2` (decisión 2). `abs_t` con `t_corchea(e[0])`. `t_cambio = t_pulso(bc) − pos0`. Tics con `t_pulso(r) − pos0` para el mismo rango `r_ini…r_fin` de hoy. `t_f2 = t_pulso(bc + MIKU_GAP_BEATS) − pos0`. Guardar `self.c_inicio = eventos[self.inicio][0]` para la cuenta.
- [ ] **Step 5: Métodos.**
  - `slot_actual`: `medio = 0.5 * self.beat2`.
  - `rotulo_fase`: `c < self.t_f2` en lugar de `t_cambio + GAP × beat`.
  - `cuenta`: `k = fase_pulso(t_juego() + pos0)[0]`, `kn = (c_inicio + 1) // 2`, `n = kn − k`, recortado a `MIKU_PRE_BEATS`. `""` si `n < 1` o en las condiciones de hoy.
  - `pulso`: la fracción de `fase_pulso(reloj() − latencia + pos0)`; la fórmula de brillo `0.35 + 0.65 × (1 − frac)` queda igual.
- [ ] **Step 6:** Lint → `m3_prueba.txt` dice `OK` en todos los casos; sin errores nuevos.

### Task 2: Modo de depuración del tic

**Files:**
- Modify: `The Fifth Choice/game/10_mj_miku.rpy` (constantes, final del bloque de tics de `__init__`)
- Test (temporal): `zz_m3_prueba_tmp.rpy`

**Interfaces:**
- Consume: `t_corchea`, `self.pos0`, `self.tics` (Task 1).
- Produce: `define M3_DEPURAR_TIC = False`.

- [ ] **Step 1: Prueba.** Con `store.M3_DEPURAR_TIC = True` (restaurarlo después): para cada nota de fase 1 con `i ≥ inicio`, su tiempo `v.ev[i][0]` está en `v.tics` (± 1e-6) y `v.tics` está ordenada. Con `False`, ninguna nota de la fase 1 cae en `v.tics` en el modo con tema.
- [ ] **Step 2: Implementar:** si `M3_DEPURAR_TIC`, añadir `t_corchea(e[0]) − pos0` de las notas `inicio…n1−1` (una vez por evento, aunque sea doble) y ordenar `self.tics`. El bucle de `tick` ya los hace sonar.
- [ ] **Step 3:** Lint → `OK`. Borrar `zz_m3_prueba_tmp.rpy` y su `.rpyc`. Lint final limpio.
- [ ] **Step 4: Escucha (usuario).** Consola: `$ M3_DEPURAR_TIC = True`, después `jump mj_probar_m3`, en los tres niveles. El tic de cada nota en pulso debe caer encima del pulso de la música, y el de una corchea, justo a mitad entre dos pulsos.
