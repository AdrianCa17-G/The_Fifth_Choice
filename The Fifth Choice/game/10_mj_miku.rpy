################################################################################
##  10_mj_miku.rpy — M3 · El compás (Miku)
##  Fase 1: tres carriles al compás de audio.miku. Fase 2: se apagan los
##  audífonos y manda el reloj (tic propio + amb_reloj); vale cualquier carril.
##  Reloj propio (perf_counter), sin get_pos(). Devuelve el dict del marco.
################################################################################

## --- CONSTANTES DE REFERENCIA (medir en Audacity: tarea T-02) -----------------
define MIKU_BPM = 96.0              ## BPM de miku_tema («The calm seaside»)
define MIKU_OFFSET = 0.0            ## segundos hasta el primer pulso de la pista
define MIKU_USAR_TEMA = True        ## PLAN B: False = metrónomo en las dos fases
define MIKU_PRE_BEATS = 4           ## pulsos de cuenta antes de la primera nota
define MIKU_GAP_BEATS = 4           ## pulsos de hueco entre fase 1 y fase 2
define MIKU_PAUSA_GAP = 0.35        ## hueco entre ticks (s) que se trata como pausa
define M3_TIC = "audio/sfx/hover.mp3"   ## sonido del metrónomo (T-03: cámbialo si hay uno mejor)
define M3_TIC_VOL = 0.8
define M3_BAJAR_RELOJ = False       ## True = baja amb_reloj en la fase 2 (ver informe)
define M3_RELOJ_NIVEL = 0.15
define M3_CAIDA_S = 1.7             ## segundos que tarda una nota en caer
define M3_CARRILES_X = [700, 960, 1220]
define M3_ANCHO_CARRIL = 200
define M3_Y_TOP = 190
define M3_Y_META = 620

default persistent.m3_latencia_ms = 50
default m3_vol_reloj_prev = None


init python:

    import time

    def m3_reloj_bajar():
        if not M3_BAJAR_RELOJ:
            return
        try:
            store.m3_vol_reloj_prev = renpy.music.get_volume("ambiente")
            renpy.music.set_volume(M3_RELOJ_NIVEL, delay=0.6, channel="ambiente")
        except Exception:
            store.m3_vol_reloj_prev = None

    def m3_reloj_restaurar():
        if store.m3_vol_reloj_prev is None:
            return
        renpy.music.set_volume(store.m3_vol_reloj_prev, delay=0.6, channel="ambiente")
        store.m3_vol_reloj_prev = None

    class MJM3(object):
        """Estado vivo de un intento. Lo crea la screen (default); no se guarda.
        Notas: [carril, tiempo_reloj, estado] con estado pend | ok | fallo | hecha."""

        def __init__(self, params, inicio):
            self.globo = MJGlobo("miku")
            self.p = params
            self.beat = 60.0 / float(MIKU_BPM)
            self.n1 = int(params["fase1_notas"])
            self.n2 = int(params["fase2_notas"])
            self.total = self.n1 + self.n2
            self.ventana = float(params["ventana_ms"]) / 1000.0
            self.fallos_max = int(params["fallos_max"])
            self.guia = params["fase2_guia"]
            self.latencia = float(persistent.m3_latencia_ms) / 1000.0

            self.inicio = int(inicio)
            if self.inicio > self.n1:
                self.inicio = self.n1
            if self.inicio > self.total - 1:
                self.inicio = self.total - 1
            if self.inicio < 0:
                self.inicio = 0

            ## Mapa de carriles (la fase 2 va toda al carril central).
            self.carriles = []
            ultimo = -1
            repetidas = 0
            for k in range(self.total):
                if k >= self.n1:
                    self.carriles.append(1)
                else:
                    c = renpy.random.randint(0, 2)
                    if c == ultimo:
                        repetidas += 1
                    else:
                        repetidas = 1
                    if repetidas > 2:
                        c = (c + 1 + renpy.random.randint(0, 1)) % 3
                        repetidas = 1
                    ultimo = c
                    self.carriles.append(c)

            ## Línea de tiempo: pos0 = posición de la pista en el instante 0 del intento.
            self.lead = self.t_musica(0)
            self.pos0 = self.t_musica(self.inicio) - self.lead
            if self.pos0 < 0.0:
                self.pos0 = 0.0

            self.notas = []
            for k in range(self.total):
                estado = "pend"
                if k < self.inicio:
                    estado = "hecha"
                self.notas.append([self.carriles[k], self.t_musica(k) - self.pos0, estado])
            self.cursor = self.inicio

            self.usa_musica = MIKU_USAR_TEMA and self.inicio < self.n1
            self.musica_cortada = not self.usa_musica
            if self.inicio >= self.n1:
                self.t_cambio = -1.0
            else:
                self.t_cambio = self.abs_ranura(self.n1 + MIKU_PRE_BEATS) - self.pos0

            ## Tics del metrónomo (hueco y fase 2; o todo, en el plan B).
            self.tics = []
            r_ini = self.n1 + MIKU_PRE_BEATS
            if not MIKU_USAR_TEMA:
                r_ini = 0
            r_fin = self.ranura(self.total - 1)
            for r in range(r_ini, r_fin + 1):
                tc = self.abs_ranura(r) - self.pos0
                if tc >= 0.0:
                    self.tics.append(tc)
            self.tic_i = 0

            self.aciertos = 0
            self.perfectos = 0
            self.fallos = 0
            self.racha = 0
            self.flash = [0.0, 0.0, 0.0]
            self.flash_fallo = 0.0
            self.fb = ""
            self.fb_t = 0.0
            self.aviso_caida = False
            self.aviso_casi = False
            self.aviso_silencio = False
            self.estado = "listo"
            self.t0 = None
            self.ultimo = time.perf_counter()
            self.t_fin = 0.0
            self.resultado = None

        ## --- Línea de tiempo ---------------------------------------------------

        def abs_ranura(self, r):
            return MIKU_OFFSET + r * self.beat

        def ranura(self, k):
            r = k + MIKU_PRE_BEATS
            if k >= self.n1:
                r = r + MIKU_GAP_BEATS
            return r

        def t_musica(self, k):
            return self.abs_ranura(self.ranura(k))

        def reloj(self):
            if self.t0 is None:
                return 0.0
            return time.perf_counter() - self.t0

        def t_juego(self):
            return self.reloj() - self.latencia

        def en_fase2(self):
            if self.estado == "listo":
                return False
            return self.reloj() >= self.t_cambio

        ## --- Control -------------------------------------------------------------

        def ajustar_latencia(self, delta):
            v = int(persistent.m3_latencia_ms) + delta
            if v < 0:
                v = 0
            if v > 250:
                v = 250
            persistent.m3_latencia_ms = v
            self.latencia = float(v) / 1000.0
            return None

        def sonar_desde(self, pos):
            ruta = audio.miku
            if pos > 0.05:
                ruta = "<from " + str(round(pos, 3)) + ">" + audio.miku
            renpy.music.play(ruta, channel="music", loop=False)

        def parar_musica(self, fade):
            if self.usa_musica and not self.musica_cortada:
                renpy.music.stop(channel="music", fadeout=fade)
                self.musica_cortada = True

        def empezar(self):
            if self.estado != "listo":
                return None
            self.t0 = time.perf_counter()
            self.ultimo = self.t0
            self.estado = "juego"
            if self.usa_musica:
                self.sonar_desde(self.pos0)
            self.globo.decir("inicio", True)
            return None

        def resincronizar(self):
            """Tras una pausa (Esc): recoloca la pista en la posición del reloj."""
            if self.estado == "juego" and self.usa_musica and not self.musica_cortada:
                self.sonar_desde(self.pos0 + self.reloj())

        def terminar(self, res):
            if self.estado == "fin":
                return
            self.estado = "fin"
            self.parar_musica(0.5)
            m3_reloj_restaurar()
            prog = self.cursor
            if prog > self.n1:
                prog = self.n1
            if res == "ganado":
                prog = self.total
                self.t_fin = 1.0
                self.globo.decir("final", True)
            else:
                self.t_fin = 0.7
                self.globo.decir("perdida", True)
            datos = {
                "m3_fallos": self.fallos,
                "m3_aciertos": self.aciertos,
                "m3_perfectos": self.perfectos,
                "audifonos": (res == "ganado"),
            }
            self.resultado = {"resultado": res, "progreso": prog, "datos": datos}

        def avanzar_cursor(self):
            while self.cursor < self.total and self.notas[self.cursor][2] != "pend":
                self.cursor += 1

        def comprobar_fin(self):
            if self.estado == "juego" and self.cursor >= self.total:
                self.terminar("ganado")

        def registrar_fallo(self):
            self.fallos += 1
            self.racha = 0
            self.flash_fallo = 0.5
            self.fb = "fallo"
            self.fb_t = 0.4
            if self.fallos > self.fallos_max:
                self.terminar("perdido")
                return
            if (not self.aviso_caida) and self.fallos_max >= 2 and self.fallos >= self.fallos_max - 1:
                self.aviso_caida = True
                self.globo.decir("caida", True)
            else:
                self.globo.decir("fallo")

        def pulsar(self, carril):
            if self.estado == "listo":
                return self.empezar()
            if self.estado != "juego":
                return None
            t = self.t_juego()
            self.flash[carril] = 0.15

            mejor = -1
            mejor_d = 99.0
            i = self.cursor
            while i < self.total:
                nota = self.notas[i]
                if nota[1] - t > self.ventana * 2.0:
                    break
                if nota[2] == "pend":
                    d = abs(nota[1] - t)
                    if d < mejor_d:
                        mejor = i
                        mejor_d = d
                i += 1

            if mejor < 0:
                return None
            if mejor_d > self.ventana:
                if self.notas[mejor][1] > t:
                    self.fb = "pronto"
                else:
                    self.fb = "tarde"
                self.fb_t = 0.3
                return None

            nota = self.notas[mejor]
            libre = (mejor >= self.n1)
            if (not libre) and nota[0] != carril:
                nota[2] = "fallo"
                self.avanzar_cursor()
                self.registrar_fallo()
                self.comprobar_fin()
                return None

            nota[2] = "ok"
            self.aciertos += 1
            self.racha += 1
            if mejor_d <= self.ventana / 3.0:
                self.perfectos += 1
                self.fb = "perfecto"
            else:
                self.fb = "bien"
            self.fb_t = 0.3
            self.avanzar_cursor()

            if libre and not self.aviso_silencio:
                self.aviso_silencio = True
                self.globo.decir("silencio", True)
            elif self.racha == 4 or self.racha == 10 or self.racha == 18 or self.racha == 28 or self.racha == 40:
                self.globo.decir("racha")
            elif self.racha == 2:
                self.globo.decir("acierto")

            if (not self.aviso_casi) and (self.total - self.cursor) <= 4:
                self.aviso_casi = True
                self.globo.decir("casi", True)

            self.comprobar_fin()
            return None

        def tick(self):
            ahora = time.perf_counter()
            if self.estado == "listo":
                self.ultimo = ahora
                return None

            dt = ahora - self.ultimo
            self.ultimo = ahora
            if dt < 0.0:
                dt = 0.0
            if dt > MIKU_PAUSA_GAP:
                ## Menú abierto o ventana sin foco: el reloj se congela y la pista se recoloca.
                self.t0 += dt
                dt = 0.0
                self.resincronizar()

            self.globo.avanzar(dt)
            if self.flash_fallo > 0.0:
                self.flash_fallo -= dt
            if self.fb_t > 0.0:
                self.fb_t -= dt
                if self.fb_t <= 0.0:
                    self.fb = ""
            for i in range(3):
                if self.flash[i] > 0.0:
                    self.flash[i] -= dt

            if self.estado == "fin":
                self.t_fin -= dt
                if self.t_fin <= 0.0:
                    return self.resultado
                return None

            c = ahora - self.t0
            t = c - self.latencia

            ## Fin de la fase 1: se apagan los audífonos.
            if (not self.musica_cortada) and c >= self.t_cambio:
                self.parar_musica(0.8)
                m3_reloj_bajar()
                self.globo.decir("mitad", True)

            ## Metrónomo (se emite en el instante nominal; llega con la misma latencia que la pista).
            while self.tic_i < len(self.tics) and c >= self.tics[self.tic_i]:
                retraso = c - self.tics[self.tic_i]
                self.tic_i += 1
                if retraso < 0.15:
                    renpy.sound.play(M3_TIC, relative_volume=M3_TIC_VOL)

            ## Notas que se pasaron de largo.
            i = self.cursor
            while i < self.total and self.estado == "juego":
                nota = self.notas[i]
                if nota[1] + self.ventana >= t:
                    break
                if nota[2] == "pend":
                    nota[2] = "fallo"
                    self.registrar_fallo()
                i += 1
            if self.estado == "juego":
                self.avanzar_cursor()
                self.comprobar_fin()
            return None

        ## --- Datos para la pantalla ---------------------------------------------

        def rotulo_fase(self):
            if self.estado == "listo":
                return ""
            if self.estado == "fin" and self.resultado["resultado"] == "ganado":
                return "Compás completo."
            c = self.reloj()
            if c < self.t_cambio:
                if MIKU_USAR_TEMA:
                    return "FASE 1 · Con los audífonos"
                return "FASE 1 · Con el metrónomo"
            if c < self.t_cambio + MIKU_GAP_BEATS * self.beat:
                return "Los audífonos se apagan."
            return "FASE 2 · Solo el reloj"

        def rotulo_tecla(self, i):
            if self.en_fase2():
                return "TOCA"
            teclas = ["A", "S", "D"]
            return teclas[i]

        def cuenta(self):
            if self.estado != "juego":
                return ""
            t = self.t_juego()
            primera = self.notas[self.inicio][1]
            if t >= primera - 0.05:
                return ""
            n = int((primera - t) / self.beat) + 1
            if n > MIKU_PRE_BEATS:
                n = MIKU_PRE_BEATS
            return str(n)

        def pulso(self):
            if self.estado == "listo":
                return 0.5
            c = self.reloj() - self.latencia + self.pos0 - MIKU_OFFSET
            frac = (c / self.beat) % 1.0
            return 0.35 + 0.65 * (1.0 - frac)

        def feedback(self):
            if self.fb == "perfecto":
                return "Perfecto"
            if self.fb == "bien":
                return "Bien"
            if self.fb == "fallo":
                return "Fallo"
            if self.fb == "pronto":
                return "Pronto"
            if self.fb == "tarde":
                return "Tarde"
            return ""

        def expresion(self):
            if self.estado == "fin":
                if self.resultado["resultado"] == "ganado":
                    return "feliz"
                return "triste"
            if self.flash_fallo > 0.0:
                return "triste"
            if self.en_fase2():
                return "esfuerzo"
            if self.racha >= 4:
                return "animo"
            return "neutral"

        def anim(self):
            if self.estado == "fin":
                if self.resultado["resultado"] == "ganado":
                    return "salto"
                return "tiembla"
            return "bob"

        def visibles(self):
            """Notas a dibujar: (x, y, alto, alfa, color)."""
            res = []
            if self.estado == "listo":
                return res
            t = self.t_juego()
            color = PETALO_COLOR["miku"]
            i = self.cursor
            while i < self.total:
                nota = self.notas[i]
                dt = nota[1] - t
                if dt > M3_CAIDA_S:
                    break
                if nota[2] == "pend":
                    mostrar = True
                    alfa = 1.0
                    tinte = color
                    carril = nota[0]
                    if i >= self.n1:
                        tinte = "#FFFFFF"
                        carril = 1
                        if self.guia == "ninguna":
                            mostrar = False
                        elif self.guia == "tenue":
                            alfa = 0.35
                    if mostrar:
                        alto = 36 + ((i * 5) % 4) * 16
                        y = M3_Y_META - int((dt / M3_CAIDA_S) * (M3_Y_META - M3_Y_TOP)) - alto // 2
                        x = M3_CARRILES_X[carril] - 85
                        res.append((x, y, alto, alfa, tinte))
                i += 1
            return res

    mj_registrar("m3", "mj_m3", "El compás", True)


################################################################################
##  SCREEN
################################################################################

screen mj_m3(hermana, params, inicio, intento, fallos, nivel, titulo):

    modal True
    zorder 95

    default vivo = MJM3(params, inicio)

    timer 0.02 repeat True action Function(vivo.tick)

    key "K_a" action Function(vivo.pulsar, 0)
    key "K_s" action Function(vivo.pulsar, 1)
    key "K_d" action Function(vivo.pulsar, 2)
    key "K_SPACE" action Function(vivo.pulsar, 1)
    key "K_RETURN" action Function(vivo.empezar)

    $ color = PETALO_COLOR[hermana]
    $ tinta = ui_mezclar(color, "#000000", 0.75)
    $ fase2 = vivo.en_fase2()
    $ cuenta = vivo.cuenta()
    $ fb_texto = vivo.feedback()
    
    add "bg_biblioteca" fit "cover"

    use mj_marco(hermana, titulo, intento, fallos, nivel, vivo.cursor, vivo.total, None, None, "NOTAS"):

        text vivo.rotulo_fase():
            xalign 0.5
            ypos 118
            font gui.name_text_font
            size 30
            kerning 3
            color "#FFFFFF"
            outlines [(4, "#1B1026CC", 0, 0)]

        ## Carriles
        for i in range(3):
            $ alfa_c = 0.10
            if fase2 and i != 1:
                $ alfa_c = 0.03
            add Solid("#FFFFFF", xsize=M3_ANCHO_CARRIL, ysize=(M3_Y_META + 70 - M3_Y_TOP)) xpos (M3_CARRILES_X[i] - M3_ANCHO_CARRIL // 2) ypos M3_Y_TOP alpha alfa_c
            if vivo.flash[i] > 0.0:
                add Solid(color, xsize=M3_ANCHO_CARRIL, ysize=(M3_Y_META + 70 - M3_Y_TOP)) xpos (M3_CARRILES_X[i] - M3_ANCHO_CARRIL // 2) ypos M3_Y_TOP alpha 0.30

        ## Línea de meta (late con el compás)
        add Solid(color, xsize=700, ysize=6) xalign 0.5 ypos M3_Y_META alpha vivo.pulso()

        ## Notas
        for n in vivo.visibles():
            add Solid(n[4], xsize=170, ysize=n[2]) xpos n[0] ypos n[1] alpha n[3]

        if cuenta != "":
            text cuenta:
                xalign 0.5
                ypos 330
                size 110
                font gui.name_text_font
                color "#FFFFFF"
                outlines [(5, "#1B1026CC", 0, 0)]

        if fb_texto != "":
            text fb_texto:
                xalign 0.5
                ypos 660
                size 30
                color "#FFFFFF"
                outlines [(3, "#1B102699", 0, 0)]

        ## Botones de carril (teclado o toque)
        for i in range(3):
            button:
                xysize (M3_ANCHO_CARRIL, 100)
                xpos (M3_CARRILES_X[i] - M3_ANCHO_CARRIL // 2)
                ypos 705
                action Function(vivo.pulsar, i)
                background Solid(color + "55")
                hover_background Solid(color + "99")
                text vivo.rotulo_tecla(i):
                    xalign 0.5
                    yalign 0.5
                    font gui.name_text_font
                    size 40
                    color "#FFFFFF"
                    outlines [(3, "#1B102699", 0, 0)]

        use mj_retrato("miku", vivo.expresion(), vivo.globo, vivo.anim(), 280, 900, 0.5)

        ## Pantalla de inicio: instrucciones y calibración de latencia
        if vivo.estado == "listo":
            fixed:
                xalign 0.5
                ypos 190
                xysize (1060, 470)

                add Transform(Frame("ui/opcion_neutra.png", 40, 40, 40, 40), matrixcolor=TintMatrix("#1B1026"))
                add Transform(Frame("ui/opcion_marco.png", 40, 40, 40, 40), matrixcolor=TintMatrix(color))

                vbox:
                    xalign 0.5
                    ypos 32
                    xsize 940
                    spacing 14

                    text "EL COMPÁS":
                        xalign 0.5
                        font gui.name_text_font
                        size 40
                        kerning 4
                        color "#FFF8FC"

                    text "Pulsa el carril cuando la barra llegue a la línea. Teclas: A · S · D, o toca los carriles. Cuando se apaguen los audífonos, sigue el reloj: vale cualquier carril.":
                        xalign 0.5
                        text_align 0.5
                        size 26
                        color "#E8E0F2"

                    text ("Latencia de audio: " + str(persistent.m3_latencia_ms) + " ms"):
                        xalign 0.5
                        size 24
                        color "#CFC6E0"

                hbox:
                    xalign 0.5
                    ypos 262
                    spacing 20
                    use cinta_boton("−10 ms", Function(vivo.ajustar_latencia, -10), hermana, 200, 56, 24)
                    use cinta_boton("+10 ms", Function(vivo.ajustar_latencia, 10), hermana, 200, 56, 24)

                fixed:
                    xalign 0.5
                    ypos 350
                    xysize (420, 80)
                    use cinta_boton("Empezar", Function(vivo.empezar), hermana, 420, 80, 34)


################################################################################
##  PRUEBA SUELTA:  jump mj_probar_m3   (consola Shift+O)
##  Para probar con boost de Nino: $ nino_rama_beat = "calida" antes de saltar.
##  Si ya lo ganaste, borra el flag desde 11_e6_debug (Ajustes → borrar flags).
################################################################################

label mj_probar_m3:

    scene bg_negro

    call mj_ejecutar("m3", "miku")

    $ mj_msg = "Resultado: " + str(_return)
    $ mj_msg = mj_msg + " · intentos " + str(e6_mj["miku"]["intentos"])
    $ mj_msg = mj_msg + " · fallos " + str(e6_mj["miku"]["fallos"])
    $ mj_msg = mj_msg + " · nivel " + str(e6_mj["miku"]["nivel"])
    $ mj_msg = mj_msg + " · datos " + str(e6_mj["miku"]["datos"])
    $ narrator(mj_msg)
    return