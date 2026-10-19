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
| `06_main_menu.rpy` | menú principal |
| `08_extras.rpy` | Galería (datos en `GALERIA`) y Finales |
| `09_menus_sistema.rpy` | Guardar, Cargar, Opciones, Historial, Acerca de, Ayuda, confirmaciones |
| `screens.rpy` | `say`, `choice`, menú rápido |
| `herramientas/generar_ui.py` | genera todos los PNG de `game/ui/` |
| `herramientas/generar_logo.py` | genera el logo con los sprites `neutral` |
| `herramientas/recortar_menu.py` | prepara los sprites del menú |

## 3. Regenerar los PNG

`cd herramientas` y `python generar_ui.py` → `game/ui/`. Las constantes (opacidad de la decoración, alturas de tarjeta…) están arriba del script. **Si un número está también en un `.rpy`** (por ejemplo `TARJETA_ALTOS`), cámbialo en los dos sitios.

## 4. Recetas

- **Decisión con peso:** `$ decision_peso("hermana", "Pregunta", "Por qué importa")` justo antes del `menu:`. Las opciones van en orden cálida, tibia, fría.
- **Menú cuyas opciones son hermanas:** `$ ligera_hermanas = {"Ichika": "ichika"}` antes del `menu:` y `$ ligera_hermanas = {}` al terminar.
- **Hub o beat:** `$ ui_escena("hub", destino, lugar)` ... `$ ui_escena("normal")` (los beats usan `"beat"`).
- **Fondo nuevo:** añadirlo a `BG_LUGAR`; si no debe verse en el prólogo, también a `BG_OCULTOS_PROLOGO`.
- **CG nuevo:** añadirlo a `GALERIA` (`08_extras.rpy`). El porcentaje se recalcula solo.
- **Sprite nuevo del menú:** generar (768×1280, cuerpo completo) → `recortar_menu.py` → ruta en `MENU_SPR` → calibrar `MENU_CORONILLA` con `MENU_GUIA = True`.
- **Personaje nuevo:** `ui_personaje(nombre, color, petalo, deco)`.
- **Capítulo en los guardados:** `$ save_name = "Capítulo 2"` al empezar cada capítulo.

## 5. Trampas

- Mayúsculas antes de interpolar rompe `[variable]`: `renpy.substitute()` primero.
- `hovered`/`unhovered` con variable se queda pegado al cambiar de pantalla: usar `tooltip`/`GetTooltip()`.
- El `Character` pisa el fondo que se ponga en la pantalla `say`.
- `narrator` (sin "d") es el narrador interno: cajas vacías de transiciones y preguntas de menú.
- Los cambios en `init python` no entran con recarga rápida: cerrar y abrir el juego.
