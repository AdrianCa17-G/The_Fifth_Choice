################################################################################
##  THE FIFTH CHOICE — Fan Visual Novel
##  Archivo: 00_definiciones.rpy   (FASE 0 — Nucleo del proyecto)
##  Motor: Ren'Py 8.5.3
##
##  Aqui vive TODO lo que no es narrativa y lo comparte mas de un capitulo:
##  personajes, variables, fondos, sprites, CG reutilizados, transforms,
##  audio, funciones de apoyo, la pantalla de nombre y `label start`.
##
##  Los archivos de capitulo contienen SOLO su `label` y sus CG propios.
##  Si un CG acaba usandose en un segundo capitulo, sube aqui.
################################################################################

################################################################################
##  1. PERSONAJES
################################################################################

## Protagonista. Sin sprite: nunca se muestra su rostro.
## El corchete [nombre_jugador] se interpola en tiempo real, así que el nombre
## cambia automáticamente en cuanto el jugador lo personaliza.
define mc = Character(
    "[nombre_jugador]",
    color="#F2F3F4",
    what_color="#EAECEE"
)

## Voz interna del protagonista (monólogo). Útil para el estilo DDLC.
define mc_pensamiento = Character(
    None,
    what_color="#AEB6BF",
    what_italic=True
)

## Narrador: sin nombre en la caja, solo texto.
define narrador = Character(
    None,
    what_color="#D5D8DC"
)

## Las quintillizas.
## `color` tiñe el nombre en la caja de diálogo.
## Si además quieres teñir el texto hablado, añade what_color a cada una.

define ichika  = Character("Ichika",  color="#FFB7C5")
define nino    = Character("Nino",    color="#C39BD3")
define miku    = Character("Miku",    color="#5DADE2")
define yotsuba = Character("Yotsuba", color="#58D68D")

define C_ITSUKI = "#EC7063"

define itsuki_inicio = Character("Estudiante Nueva", color=C_ITSUKI)
define itsuki        = Character("Itsuki",           color=C_ITSUKI)

## Habla colectiva (las cinco a la vez) y voces sin identificar.
define quintillizas = Character("Las quintillizas", color="#F4D03F")
define voz          = Character("???",              color="#95A5A6")


## --- Secundarios --------------------------------------------------------------
## Viven aqui, no en el prologo: Raiha y Maruo vuelven en el Capitulo 1 y el
## profesor y el padre reaparecen mas adelante.

define isanari = Character("Isanari", color="#A9925C")
define raiha   = Character("Raiha",   color="#F5B7B1")
define maruo   = Character("Maruo",   color="#7F8C8D")
define profe   = Character("Profesor", color="#909497")

## NOTA DE ASSETS:
## En escenas grupales el protagonista aparece como silueta oscura.
## Cuando tengas el asset, descomenta y ajusta la ruta:
# image futaro_silueta = "images/sprites/futaro_silueta.webp"


################################################################################
##  2. VARIABLES
################################################################################

## --- Identidad del jugador ---------------------------------------------------
default nombre_jugador = "Futaro"

## --- Puntos de afinidad (INVISIBLES para el jugador) -------------------------
## Nunca se muestran en pantalla ni se comentan en el diálogo.
## Se acumulan a lo largo del Prólogo y los Capítulos 1 a 3.
default puntos_ichika  = 0
default puntos_nino    = 0
default puntos_miku    = 0
default puntos_yotsuba = 0
default puntos_itsuki  = 0

## --- Desempate ---------------------------------------------------------------
## Guarda el nombre de la primera chica con la que el jugador tuvo una decisión
## positiva. Se escribe UNA sola vez, en la primera elección con puntaje > 0.
default primera_conexion = ""
default primera_decision_hecha = False

## --- Progreso persistente (sobrevive entre partidas) -------------------------
## Se marcan True al alcanzar el final romántico correspondiente.
default persistent.ruta_ichika_completa  = False
default persistent.ruta_nino_completa    = False
default persistent.ruta_miku_completa    = False
default persistent.ruta_yotsuba_completa = False
default persistent.ruta_itsuki_completa  = False

## Se activa cuando las cinco rutas están completas.
default persistent.final_secreto_desbloqueado = False

## Opcional: registro de finales vistos, útil para una galería futura.
default persistent.final_malo_visto = False

## --- Contador de desaires del Capitulo 1 (INVISIBLE) -------------------------
## Va aparte de los puntos y no resta afinidad. Sube solo cuando el jugador
## elige la opcion fria dentro de un evento de hermana. Se lee una sola vez, al
## cerrar el Capitulo 1: con 3 de 3, despido temprano.
default desaires_cap1 = 0


################################################################################
##  3. FONDOS BG
################################################################################

image bg_cuarto_mc     = "bg/cuarto_mc.webp"
image bg_comedor       = "bg/comedor.webp"
image bg_escuela     = "bg/escuela.webp"
image bg_aula          = "bg/aula.webp"
image bg_azotea        = "bg/azotea.webp"
image bg_edificio      = "bg/edificio.webp" 
image bg_entrada_edificio      = "bg/entrada_edificio.webp" 
image bg_departamento  = "bg/departamento.webp"
 
image bg_negro         = Solid("#000000")



################################################################################
##  4. FONDOS CG COMPARTIDOS
##  Solo los que usa mas de un capitulo. Los trece CG del prologo siguen
##  declarados en 01_prologo.rpy; estos tres subieron porque la apertura del
##  Capitulo 1 los reutiliza sin tocarlos.
################################################################################

image cg_calificacion        = "cg/calificacion.webp"
image cg_maruo_reunion       = "cg/maruo_umbral.webp"
image cg_hermanas_estudiando = "cg/estudio_hermanas.webp"

################################################################################
##  5. SPRITES
################################################################################

image raiha hablando    = "sprites/raiha_sprites/raiha_hablando.png"
image raiha regano      = "sprites/raiha_sprites/raiha_regano.png"

image isanari neutral      = "sprites/isanari_sprites/isanari_neutral.png"
image isanari sonriendo    = "sprites/isanari_sprites/isanari_sonrisa.png"

image itsuki neutral   = "sprites/itsuki_sprites/itsuki_neutral.png"
image itsuki sonriendo   = "sprites/itsuki_sprites/itsuki_sonrisa.png"
image itsuki molesta   = "sprites/itsuki_sprites/itsuki_molesta.png"
image itsuki sorprendida   = "sprites/itsuki_sprites/itsuki_sorpresa.png"

image ichika neutral   = "sprites/ichika_sprites/ichika_neutral.png"
image ichika sonriendo   = "sprites/ichika_sprites/ichika_sonrisa.png"

image nino neutral   = "sprites/nino_sprites/nino_neutral.png"
image nino pillada   = "sprites/nino_sprites/nino_pillada.png"

image miku neutral   = "sprites/miku_sprites/miku_neutral.png"

image yotsuba sonriendo   = "sprites/yotsuba_sprites/yotsuba_sonrisa.png"
image yotsuba incomoda   = "sprites/yotsuba_sprites/yotsuba_incomoda.png"


## --- Pendientes del Capitulo 1 -----------------------------------------------
## Declararlos SIEMPRE como atributo, con espacio, igual que los de arriba.
## `image nino_pillada` crearia un tag distinto de `nino`: `hide nino` no lo
## quitaria y podrian convivir dos Ninos en pantalla. El .png si lleva guion
## bajo; la declaracion no.
# image nino pillada       = "sprites/nino_sprites/nino_pillada.png"
# image yotsuba incomoda   = "sprites/yotsuba_sprites/yotsuba_incomoda.png"


################################################################################
##  6. TRANSFORMS
################################################################################


## Posiciones de la formación de las cinco hermanas.
## Se usan solo en la escena 5; el resto de escenas van con literales.
define X_ICHIKA  = 0.13
define X_NINO    = 0.31
define X_MIKU    = 0.50
define X_YOTSUBA = 0.69
define X_ITSUKI  = 0.87

## REGLA DEL PROYECTO
## Todo `show` lleva SIEMPRE su posición, aunque solo cambie el tinte.
## `at` reemplaza el transform entero, no lo suma: si `pj_habla` no
## declarara la x, Ren'Py tendría que heredarla del transform anterior, y
## lo que hereda es el estado del instante. Con una animación a medias
## (clic rápido o regresión) el sprite se congela donde iba y se encima.
## Reafirmar la posición absoluta en cada show hace que eso no pueda pasar.

transform pj(x=0.5):
    xanchor 0.5
    yanchor 1.0
    xpos x
    ypos 1.0
    zoom 1.0
    matrixcolor TintMatrix("#ffffff")

transform pj_habla(x=0.5):
    xanchor 0.5
    yanchor 1.0
    xpos x
    ypos 1.0
    ease 0.25 zoom 1.01 matrixcolor TintMatrix("#ffffff")

transform pj_calla(x=0.5):
    # Se encoge un poquito y se oscurece con un tono grisáceo suave
    xanchor 0.5
    yanchor 1.0
    xpos x
    ypos 1.0
    ease 0.25 zoom 0.99 matrixcolor TintMatrix("#a0a0a0")

## Los desplazamientos van como TRANSICIÓN, nunca como `ease` dentro del
## transform. Un clic salta una transición a su estado final; un clic NO
## adelanta una animación ATL. Esa diferencia era el origen del bug.
##
## `mover` SOLO mueve. Los parámetros enter/leave de MoveTransition piden un
## transform con la posición de partida, no una transición: pasarles
## `dissolve` revienta con AttributeError al renderizar. Quien entra en
## escena se muestra en una sentencia aparte con `with dissolve`.
define mover = MoveTransition(0.6)

# Definir dissolve que dura 1.2 segundos
define disolucion_lenta = Dissolve(0.8)


################################################################################
##  7. AUDIO
##  El canal `ambiente` es aparte para que el viento de la azotea pueda sonar
##  por debajo de la musica sin cortarla.
################################################################################

init python:
    ## El canal `ambiente` va al mezclador de MUSICA, no al de efectos. Con
    ## "sfx" el viento se comportaba como un golpe puntual: se ponia delante
    ## del texto en vez de quedarse detras. Ademas, asi el jugador lo puede
    ## regular desde el control de musica de las preferencias.
    renpy.music.register_channel("ambiente", "music", loop=True)

    ## Ducking: aparta la musica un instante para que un efecto suave se lea
    ## por encima. La bajada es rapida y la vuelta lenta; al reves se nota.
    ##
    ## SOLO para sonidos sin ataque que compiten con una pista ya sonando. Los
    ## impactos (portazo, puertas, campana) no lo necesitan, y si esto se usa
    ## en todas partes deja de ser una excepcion y se oye como bombeo.
    def duck(nivel=0.4, bajada=0.2, subida=1.5):
        renpy.music.set_volume(nivel, delay=bajada, channel="music")
        renpy.music.set_volume(1.0, delay=subida, channel="music")

    renpy.music.set_volume(1.0, channel="music")

## Musica --------------------------------------------------------------------
## `hogar` suena SOLO dos veces en todo el prologo: bajo el retrato
## familiar y en "Bien. Que sea difícil." Es el tema de Futaro. Si sonara
## tambien durante la cena dejaria de ser un tema y seria fondo.
define audio.hogar     = "audio/bgm/hogar.ogg"
define audio.cena      = "audio/bgm/cena.ogg"
define audio.cotidiano = "audio/bgm/cotidiano.ogg"
define audio.incomodo  = "audio/bgm/incomodo.ogg"
define audio.extraneza = "audio/bgm/extraneza.ogg"
define audio.caos      = "audio/bgm/caos.ogg"
define audio.contrato  = "audio/bgm/contrato.ogg"
define audio.derrota   = "audio/bgm/derrota.ogg"

## Ambiente (en bucle) -------------------------------------------------------
define audio.amb_viento = "audio/amb_viento.ogg"

## Efectos -------------------------------------------------------------------
##
## ESCALA DE VOLUMEN — la referencia es 2.5, no 1.0. Ren'Py multiplica de
## verdad por encima de 1.0, y los efectos se calibraron contra la musica ya
## sonando, no en abstracto.
##
##   2.5  portazo de Itsuki (el mas alto del prologo, a proposito) y los tres
##        sonidos suaves de origen: papel, silla, bolsa. Estos ultimos estan
##        arriba porque el archivo es flojo, no porque la escena lo pida.
##   2.0  hoja, y la puerta de Nino en la escena 7.
##   1.75 pasos de Yotsuba.
##   1.5  campana, toque, pomo, puerta que abre Ichika.
##   1.2  las tres puertas que se cierran despues de la de Nino.
##   1.0  la puerta de Maruo: cierra "con la calma de quien ya dio una orden".
##        Es el sonido mas bajo del prologo y esta bien que lo sea.
##
## Lo que no puede pasar es que un pomo suene como un portazo. Si hay que
## subir algo, subir el archivo (comprimir + normalizar a -1 dB), no el numero.
## Los archivos viven en `game/audio/sfx/` y por eso el nombre del archivo NO
## repite el prefijo. La variable si lo conserva: en el guion, `play sound
## sfx_timbre` se distingue de un vistazo de `play music cotidiano`, que es lo
## que se pierde si se acortan los dos lados a la vez.
##
## El portazo de Itsuki se derivo de `puerta_cierra`: mismo impacto de hoja
## contra marco, amplificado y con la entrada recortada. Son la misma puerta a
## proposito. Si algun dia se sustituye uno, revisar el otro.
define audio.sfx_papel_mesa    = "audio/sfx/papel_mesa.mp3"
define audio.sfx_timbre        = "audio/sfx/timbre.mp3"
define audio.sfx_silla         = "audio/sfx/silla.mp3"
define audio.sfx_toque_puerta  = "audio/sfx/toque_puerta.mp3"
define audio.sfx_manija        = "audio/sfx/manija.mp3"
define audio.sfx_puerta_abre   = "audio/sfx/puerta_abre.mp3"
define audio.sfx_correr        = "audio/sfx/correr.mp3"
define audio.sfx_portazo       = "audio/sfx/portazo.mp3"
define audio.sfx_bolsa         = "audio/sfx/bolsa.mp3"
define audio.sfx_hoja          = "audio/sfx/hoja.mp3"
define audio.sfx_puerta_cierra = "audio/sfx/puerta_cierra.mp3"


################################################################################
##  8. LÓGICA DEL CÁLCULO SECRETO  (documentación — se implementa en FASE 5)
################################################################################
##
##  CUÁNDO SE EJECUTA
##  Al cerrar el Capítulo 3, antes del epílogo. El jugador no ve ningún número,
##  ningún menú de selección y ninguna pista explícita del sistema.
##
##  PASO 1 — UMBRAL MÍNIMO
##  mayor = max(puntos_ichika, puntos_nino, puntos_miku, puntos_yotsuba,
##              puntos_itsuki)
##  Si mayor < 10  ->  FINAL MALO (Futaro es despedido). Fin del cálculo.
##  El umbral castiga al jugador disperso: repartir atención entre las cinco
##  sin comprometerse con ninguna no debe premiarse.
##
##  PASO 2 — SELECCIÓN DE GANADORA
##  Se recorren las candidatas SIEMPRE en este orden fijo:
##      ichika -> nino -> miku -> yotsuba -> itsuki
##  Se conserva la primera que alcance el valor `mayor`.
##  Comparar con `>` (no con `>=`) garantiza que, ante empate, prevalezca la
##  primera del orden; el desempate real se resuelve en el Paso 3.
##
##  PASO 3 — DESEMPATE
##  Se construye la lista `empatadas` con todas las chicas cuyo puntaje == mayor.
##  a) Si len(empatadas) == 1        -> esa es la ganadora.
##  b) Si primera_conexion está en `empatadas` -> gana primera_conexion.
##     (La primera decisión positiva del jugador desempata: quien llegó antes
##      al corazón del protagonista.)
##  c) Si primera_conexion está vacía o no participa del empate -> se aplica la
##     prioridad canónica: Ichika > Nino > Miku > Yotsuba > Itsuki.
##
##  PASO 4 — MARCADO PERSISTENTE
##  Al entrar al final romántico X se ejecuta:
##      $ persistent.ruta_X_completa = True
##
##  PASO 5 — DESBLOQUEO DEL FINAL SECRETO
##  Tras marcar la ruta, se evalúa:
##      if (persistent.ruta_ichika_completa and persistent.ruta_nino_completa
##          and persistent.ruta_miku_completa and persistent.ruta_yotsuba_completa
##          and persistent.ruta_itsuki_completa):
##          $ persistent.final_secreto_desbloqueado = True
##  Con la bandera activa, el Final Secreto (polígamo) se ofrece DESPUÉS del
##  quinto final romántico, no antes: es una recompensa por completar el juego.
##
##  ESQUELETO DE REFERENCIA PARA FASE 5 (05_finales.rpy)
##  ------------------------------------------------------------------------
##  label calculo_secreto:
##      python:
##          candidatas = [
##              ("ichika",  puntos_ichika),
##              ("nino",    puntos_nino),
##              ("miku",    puntos_miku),
##              ("yotsuba", puntos_yotsuba),
##              ("itsuki",  puntos_itsuki),
##          ]
##          mayor = max(p for _, p in candidatas)
##          if mayor < 10:
##              ganadora = "ninguna"
##          else:
##              empatadas = [n for n, p in candidatas if p == mayor]
##              if len(empatadas) == 1:
##                  ganadora = empatadas[0]
##              elif primera_conexion in empatadas:
##                  ganadora = primera_conexion
##              else:
##                  ganadora = empatadas[0]   # ya viene en orden canónico
##      if ganadora == "ninguna":
##          jump final_malo
##      jump expression "final_" + ganadora
##  ------------------------------------------------------------------------
##
##  HELPER SUGERIDO PARA LAS DECISIONES (Capítulos 1 a 3)
##  Evita repetir la lógica de primera_conexion en cada choice:
##      $ sumar_punto("miku", 2)
##  Implementación disponible más abajo, en la sección 4.
##
################################################################################


################################################################################
##  9. FUNCIONES DE APOYO
################################################################################

init python:

    def sumar_punto(chica, cantidad=1):
        """
        Suma afinidad y registra la primera conexión del jugador.
        Uso dentro de un choice:  $ sumar_punto("nino", 2)
        """
        store_var = "puntos_" + chica
        setattr(store, store_var, getattr(store, store_var) + cantidad)

        if cantidad > 0 and not store.primera_decision_hecha:
            store.primera_conexion = chica
            store.primera_decision_hecha = True

    def rutas_completadas():
        """Cuántas rutas románticas lleva completadas el jugador (0 a 5)."""
        return sum([
            persistent.ruta_ichika_completa,
            persistent.ruta_nino_completa,
            persistent.ruta_miku_completa,
            persistent.ruta_yotsuba_completa,
            persistent.ruta_itsuki_completa,
        ])


################################################################################
##  10. PANTALLA DE ENTRADA DE NOMBRE
################################################################################

screen pantalla_nombre():

    modal True
    zorder 200

    ## Fondo sobrio. Si prefieres reutilizar el arte del menú, comenta la línea
    ## siguiente y descomenta la de Fondo_Menu.png.
    add "#0B0B10"
    # add "Fondo_Menu.png"

    frame:
        xalign 0.5
        yalign 0.5
        xsize 780
        xpadding 60
        ypadding 50
        background Solid("#15151FE6")

        vbox:
            spacing 26
            xalign 0.5

            text "Antes de empezar…":
                size 24
                color "#8E9AAF"
                xalign 0.5

            text "¿Cuál es tu nombre?":
                size 44
                color "#FFFFFF"
                xalign 0.5

            input:
                value VariableInputValue("nombre_jugador", returnable=True)
                length 16
                allow "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZáéíóúÁÉÍÓÚñÑüÜ '-"
                size 38
                color "#FFB7C5"
                xalign 0.5

            text "Deja «Futaro» si prefieres vivir la historia tal como fue.":
                size 19
                color "#6C7A89"
                italic True
                xalign 0.5

            textbutton "Continuar":
                xalign 0.5
                text_size 26
                action Return(True)

    ## Enter también confirma.
    key "K_RETURN" action Return(True)


label configurar_nombre:

    call screen pantalla_nombre

    python:
        nombre_jugador = nombre_jugador.strip()
        if not nombre_jugador:
            nombre_jugador = "Futaro"

    return


################################################################################
##  11. PUNTO DE ENTRADA
################################################################################
##  IMPORTANTE: `label start` vive AQUÍ y en ningún otro archivo.
##  01_prologo.rpy debe abrir con `label prologo:` — si define su propio
##  `label start`, Ren'Py lanzará un error de etiqueta duplicada.
################################################################################

label start:

    call configurar_nombre

    jump prologo
