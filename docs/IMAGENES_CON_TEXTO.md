# Imágenes con texto incrustado

Inventario para la traducción (v1.1 inglés, y luego el ruso de la sección 6 del plan).
Revisado el 23/11/2026 sobre las 68 imágenes de `game/images/cg`, `game/images/bg` y `Fondo_Menu.png`,
y sobre las de `game/ui`, `game/gui`, `game/images/hubs`, `menu`, `chibis` y el logo. El juego no tiene vídeos.

## Resultado

**Ninguna imagen del juego tiene texto en español.** Todo el texto visible en pantalla (boletín, chat del grupo,
cortinillas, HUD, minijuegos, créditos, menús) se dibuja con `Text` de Ren'Py y ya entra en
`game/tl/english/` como `translate english strings`. No hace falta rehacer ninguna imagen para la v1.1.

## Imágenes que sí contienen texto (se quedan como están)

| Ruta (desde `game/`) | Texto | Decisión |
|---|---|---|
| `images/Logo_Menu_v2.png` | «The Fifth Choice», «五等分の花嫁», «QUINTESSENTIAL QUINTUPLETS FAN GAME» | Ya está en inglés y japonés. Sirve para todos los idiomas. |
| `images/bg/escuela.webp` | Placas del portón en kanji (ilegibles, decorado) | Ambientación japonesa. No se traduce. |
| `images/Fondo_Menu.png` | Cartel «自主創造» y la pizarra en kanji | Ambientación japonesa. No se traduce. |
| `images/bg/entrada_edificio.webp` | «30» en la puerta | Número. No se traduce. |
| `images/cg/cap1_apertura/libreta.webp` | Apuntes a mano en kanji (ilegibles) | Decorado. No se traduce. |
| `images/cg/examen.webp`, `cg/cap1_mov6/*`, `cg/cap1_final_malo/*` | Garabatos y números en hojas de examen | Sin palabras legibles. No se traduce. |
| `images/cg/cap1_hubs/nino_*.webp` | Envases y una lista de la compra con pseudo-japonés | Decorado. No se traduce. |
| `ui/ico_info.png`, `ui/ico_ayuda.png` | «i» y «?» (generados por `herramientas/generar_ui.py`) | Símbolos universales. No se traducen. |

## Cómo se reemplazaría una imagen si hiciera falta

Comprobado en la documentación de Ren'Py 8.5.3 (`doc/translation.html`, «Image and File Translations»):
cuando un idioma está activo, Ren'Py busca primero el archivo en `game/tl/<idioma>/` con **la misma ruta
relativa**, y si existe lo usa en lugar del original. No hace falta tocar ningún `.rpy`.

```
game/images/cg/ejemplo.webp               ← original (español)
game/tl/english/images/cg/ejemplo.webp    ← se usa al elegir English
game/tl/russian/images/cg/ejemplo.webp    ← se usa al elegir Русский
```

Reglas si en un capítulo futuro aparece una imagen con texto en español:

1. Mejor evitarla: poner el texto encima con `Text` (o `text` en una pantalla) marcado con `_()`, así entra
   en las plantillas de todos los idiomas sin rehacer arte.
2. Si el texto es parte del dibujo, crear la versión traducida con el **mismo tamaño en píxeles** y el mismo
   nombre, y guardarla en `game/tl/<idioma>/` con la ruta de arriba.
3. Añadir la fila a la tabla de este archivo (ruta, texto, tamaño) para el traductor al ruso.
