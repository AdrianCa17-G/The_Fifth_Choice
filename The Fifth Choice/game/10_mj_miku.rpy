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
define M3_CARRILES = {"dificil": 4, "media": 3, "asistida": 3}
define M3_TECLAS = ["A", "S", "D", "F"]
define M3_GUIA_INICIAL = 8       ## eventos de la fase 2 que se ven aunque la guía sea "ninguna"
define M3_ANCHO_CARRIL = 200
define M3_Y_TOP = 190
define M3_Y_META = 620
define M3_ALFA_FANTASMA = 0.18   ## opacidad de las notas "sin guía" de la fase 2

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

    def m3_x(i, n):
        """x del centro del carril i cuando hay n carriles."""
        sep = 260
        if n >= 4:
            sep = 236
        return int(round(960 + (i - (n - 1) / 2.0) * sep))

    def m3_carril(nc, ultimo, repes, forzar_cambio):
        """Elige carril sin repetir más de 2 veces seguidas (o cambia siempre si forzar_cambio)."""
        c = renpy.random.randint(0, nc - 1)
        if c == ultimo:
            repes += 1
        else:
            repes = 1
        if repes > 2 or (forzar_cambio and c == ultimo):
            c = (c + 1 + renpy.random.randint(0, nc - 2)) % nc
            repes = 1
        return (c, repes)

    def m3_fase1(p, nc, cantidad, beat0):
        """Fase 1: patrón aleatorio con crescendo. Devuelve (eventos, beat_siguiente).
        Evento = [corcheas_desde_el_pulso_0, [carriles], libre]."""
        eventos = []
        pc = float(p["p_corchea"])
        ps = float(p["p_silencio"])
        pd = float(p["p_doble"])
        beat = beat0
        ultimo = -1
        repes = 0
        hubo_doble = False
        hubo_silencio = False
        while len(eventos) < cantidad:
            k = len(eventos)
            f = 0.35 + 0.65 * (float(k) / float(cantidad))
            calentando = (k < 6)
            if (not calentando) and (not hubo_silencio) and renpy.random.random() < ps * f:
                hubo_silencio = True
                beat += 1
                continue
            hubo_silencio = False
            tiempos = [beat * 2]
            if (not calentando) and renpy.random.random() < pc * f:
                tiempos.append(beat * 2 + 1)
            for idx in range(len(tiempos)):
                if len(eventos) >= cantidad:
                    break
                carriles = []
                r = m3_carril(nc, ultimo, repes, idx == 1)
                c = r[0]
                repes = r[1]
                carriles.append(c)
                ultimo = c
                if (len(tiempos) == 1) and (not calentando) and (not hubo_doble) and nc >= 3 and renpy.random.random() < pd * f:
                    c2 = (c + 1 + renpy.random.randint(0, nc - 2)) % nc
                    carriles.append(c2)
                    hubo_doble = True
                else:
                    hubo_doble = False
                eventos.append([tiempos[idx], carriles, False])
            beat += 1
        return (eventos, beat)

    def m3_fase2(p, cantidad, beat0):
        """Fase 2: un compás de 4 pulsos (con silencios y contratiempos) que se repite.
        Devuelve (eventos, beat_siguiente, plantilla)."""
        pc = float(p["p_corchea2"])
        ps = float(p["p_silencio2"])
        plantilla = []
        while len(plantilla) < 3:
            plantilla = []
            for b in range(4):
                if b > 0 and renpy.random.random() < ps:
                    continue
                plantilla.append(b * 2)
                if renpy.random.random() < pc:
                    plantilla.append(b * 2 + 1)
        eventos = []
        compas = 0
        while len(eventos) < cantidad:
            for tc in plantilla:
                if len(eventos) < cantidad:
                    eventos.append([beat0 * 2 + compas * 8 + tc, [1], True])
            compas += 1
        ultimo = eventos[len(eventos) - 1][0]
        return (eventos, ultimo // 2 + 1, plantilla)

    def m3_generar(p, nc, n1, n2):
        """Devuelve (todos_los_eventos, beat_donde_termina_la_fase_1, plantilla_fase_2)."""
        r1 = m3_fase1(p, nc, n1, MIKU_PRE_BEATS)
        r2 = m3_fase2(p, n2, r1[1] + MIKU_GAP_BEATS)
        return (r1[0] + r2[0], r1[1], r2[2])

    class MJM3(object):
        """Estado vivo de un intento. Evento = [tiempo_rel, [carriles], [estados], libre]
        estados por nota: pend | ok | fallo | hecha"""

        def __init__(self, params, inicio, nivel):
            self.globo = MJGlobo("miku")
            self.p = params
            self.nivel = nivel
            self.nc = M3_CARRILES.get(nivel, 3)
            self.beat = 60.0 / float(MIKU_BPM)
            self.n1 = int(params["fase1_notas"])
            self.n2 = int(params["fase2_notas"])
            self.total = self.n1 + self.n2
            self.ventana = float(params["ventana_ms"]) / 1000.0
            self.fallos_max = float(params["fallos_max"])
            self.guia = params["fase2_guia"]
            self.caida = float(params["caida"])
            self.penal_extra = float(params["penal_extra"])
            self.latencia = float(persistent.m3_latencia_ms) / 1000.0

            self.inicio = int(inicio)
            if self.inicio > self.n1:
                self.inicio = self.n1
            if self.inicio < 0:
                self.inicio = 0

            gen = m3_generar(params, self.nc, self.n1, self.n2)
            eventos = gen[0]
            beat_cambio = gen[1]

            abs_t = []
            for e in eventos:
                abs_t.append(MIKU_OFFSET + e[0] * 0.5 * self.beat)

            self.lead = abs_t[0]
            self.pos0 = abs_t[self.inicio] - self.lead
            if self.pos0 < 0.0:
                self.pos0 = 0.0

            self.ev = []
            for i in range(self.total):
                est = []
                for l in eventos[i][1]:
                    if i < self.inicio:
                        est.append("hecha")
                    else:
                        est.append("pend")
                self.ev.append([abs_t[i] - self.pos0, eventos[i][1], est, eventos[i][2]])
            self.cursor = self.inicio

            self.usa_musica = MIKU_USAR_TEMA and self.inicio < self.n1
            self.musica_cortada = not self.usa_musica
            if self.inicio >= self.n1:
                self.t_cambio = -1.0
            else:
                self.t_cambio = MIKU_OFFSET + beat_cambio * self.beat - self.pos0

            ## Tics del metrónomo (hueco y fase 2; o todo, en el plan B).
            self.tics = []
            r_ini = beat_cambio
            if not MIKU_USAR_TEMA:
                r_ini = 0
            r_fin = eventos[self.total - 1][0] // 2
            for r in range(r_ini, r_fin + 1):
                tc = MIKU_OFFSET + r * self.beat - self.pos0
                if tc >= 0.0:
                    self.tics.append(tc)
            self.tic_i = 0

            self.aciertos = 0
            self.perfectos = 0
            self.fallos = 0.0
            self.racha = 0
            self.mejor_racha = 0
            self.flash = [0.0, 0.0, 0.0, 0.0]
            self.flash_fallo = 0.0
            self.fb = ""
            self.fb_t = 0.0
            self.aviso_caida = False
            self.aviso_casi = False
            self.aviso_silencio = False
            self.plantilla = gen[2]
            self.t_f2 = MIKU_OFFSET + (beat_cambio + MIKU_GAP_BEATS) * self.beat - self.pos0
            self.combo_cada = int(params.get("combo_cada", 10))
            self.regen_combo = float(params.get("regen_combo", 0.10))
            self.regen_acierto = float(params.get("regen_acierto", 0.0))
            self.regen_t = 0.0
            self.regen_txt = ""
            self.estado = "listo"
            self.t0 = None
            self.ultimo = time.perf_counter()
            self.t_fin = 0.0
            self.resultado = None

        ## --- Reloj -----------------------------------------------------------------

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

        ## --- Control ---------------------------------------------------------------

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
                "m3_fallos": round(self.fallos, 1),
                "m3_aciertos": self.aciertos,
                "m3_perfectos": self.perfectos,
                "m3_mejor_racha": self.mejor_racha,
                "audifonos": (res == "ganado"),
            }
            self.resultado = {"resultado": res, "progreso": prog, "datos": datos}

        ## --- Lógica de juego -------------------------------------------------------

        def avanzar_cursor(self):
            while self.cursor < self.total:
                pendiente = False
                for s in self.ev[self.cursor][2]:
                    if s == "pend":
                        pendiente = True
                if pendiente:
                    break
                self.cursor += 1

        def comprobar_fin(self):
            if self.estado == "juego" and self.cursor >= self.total:
                self.terminar("ganado")

        def concentracion(self):
            c = self.fallos_max - self.fallos
            if c < 0.0:
                c = 0.0
            return c

        def fijar_latencia(self, valor):
            persistent.m3_latencia_ms = int(valor)
            self.latencia = float(valor) / 1000.0
            return None

        def recuperar(self, frac, aviso):
            """Devuelve concentración (frac = fracción del máximo)."""
            if frac <= 0.0 or self.fallos <= 0.0:
                return
            antes = self.fallos
            self.fallos -= frac * self.fallos_max
            if self.fallos < 0.0:
                self.fallos = 0.0
            if aviso:
                pct = int(round(100.0 * (antes - self.fallos) / self.fallos_max))
                if pct < 1:
                    pct = 1
                self.regen_t = 1.4
                self.regen_txt = "+" + str(pct) + " % CONCENTRACIÓN"
                self.globo.decir("racha", True)

        def slot_actual(self):
            """Corchea (0..7) del compás de la fase 2 que toca ahora; -1 si aún no."""
            if self.estado != "juego":
                return -1
            medio = 0.5 * self.beat
            t = self.t_juego()
            if t < self.t_f2 - 0.5 * medio:
                return -1
            return int((t - self.t_f2) / medio + 0.5) % 8

        def registrar_fallo(self, peso, fb):
            self.fallos += peso
            self.racha = 0
            self.flash_fallo = 0.5
            self.fb = fb
            self.fb_t = 0.4
            if self.fallos > self.fallos_max:
                self.terminar("perdido")
                return
            if (not self.aviso_caida) and self.fallos_max >= 2 and self.concentracion() <= 1.0:
                self.aviso_caida = True
                self.globo.decir("caida", True)
            else:
                self.globo.decir("fallo")

        def pulsacion_suelta(self):
            """Pulsar donde no hay nota cerca resta concentración (anti machaque)."""
            self.racha = 0
            if self.penal_extra > 0.0:
                self.registrar_fallo(self.penal_extra, "suelta")
            else:
                self.fb = "suelta"
                self.fb_t = 0.3
            return None

        def pulsar(self, carril):
            """carril 0..3. carril -1 = Espacio: solo vale en la fase 2."""
            if self.estado == "listo":
                return self.empezar()
            if self.estado != "juego":
                return None
            if carril >= self.nc:
                return None
            if carril < 0 and not self.en_fase2():
                return None
            t = self.t_juego()
            if carril >= 0:
                self.flash[carril] = 0.15
            else:
                for k in range(self.nc):
                    self.flash[k] = 0.15

            mejor_i = -1
            mejor_j = -1
            mejor_d = 99.0
            i = self.cursor
            while i < self.total:
                e = self.ev[i]
                if e[0] - t > self.ventana * 2.5:
                    break
                for j in range(len(e[1])):
                    if e[2][j] != "pend":
                        continue
                    if e[3] or carril < 0 or e[1][j] == carril:
                        d = abs(e[0] - t)
                        if d < mejor_d:
                            mejor_i = i
                            mejor_j = j
                            mejor_d = d
                i += 1

            if mejor_i < 0:
                return self.pulsacion_suelta()

            if mejor_d > self.ventana:
                if self.ev[mejor_i][0] > t:
                    self.fb = "pronto"
                else:
                    self.fb = "tarde"
                self.fb_t = 0.3
                return None

            e = self.ev[mejor_i]
            e[2][mejor_j] = "ok"
            self.aciertos += 1
            self.racha += 1
            if self.regen_acierto > 0.0:
                self.recuperar(self.regen_acierto, False)
            if self.combo_cada > 0 and self.racha % self.combo_cada == 0:
                self.recuperar(self.regen_combo, True)
            if mejor_d <= self.ventana / 3.0:
                self.perfectos += 1
                self.fb = "perfecto"
            else:
                self.fb = "bien"
            self.fb_t = 0.3
            self.avanzar_cursor()

            if e[3] and not self.aviso_silencio:
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
                self.t0 += dt
                dt = 0.0
                self.resincronizar()

            self.globo.avanzar(dt)
            if self.regen_t > 0.0:
                self.regen_t -= dt
            if self.flash_fallo > 0.0:
                self.flash_fallo -= dt
            if self.fb_t > 0.0:
                self.fb_t -= dt
                if self.fb_t <= 0.0:
                    self.fb = ""
            for i in range(4):
                if self.flash[i] > 0.0:
                    self.flash[i] -= dt

            if self.estado == "fin":
                self.t_fin -= dt
                if self.t_fin <= 0.0:
                    return self.resultado
                return None

            c = ahora - self.t0
            t = c - self.latencia

            if (not self.musica_cortada) and c >= self.t_cambio:
                self.parar_musica(0.8)
                m3_reloj_bajar()
                self.globo.decir("mitad", True)

            while self.tic_i < len(self.tics) and c >= self.tics[self.tic_i]:
                retraso = c - self.tics[self.tic_i]
                self.tic_i += 1
                if retraso < 0.15:
                    renpy.sound.play(M3_TIC, relative_volume=M3_TIC_VOL)

            ## Notas que se pasaron de largo.
            i = self.cursor
            while i < self.total and self.estado == "juego":
                e = self.ev[i]
                if e[0] + self.ventana >= t:
                    break
                n = len(e[2])
                for j in range(n):
                    if e[2][j] == "pend":
                        e[2][j] = "fallo"
                        self.registrar_fallo(1.0 / n, "fallo")
                        if self.estado != "juego":
                            break
                i += 1
            if self.estado == "juego":
                self.avanzar_cursor()
                self.comprobar_fin()
            return None

        ## --- Datos para la pantalla --------------------------------------------------

        def rotulo_fase(self):
            if self.estado == "listo":
                return ""
            if self.estado == "fin" and self.resultado["resultado"] == "ganado":
                return "Compás completo."
            if self.t_cambio < 0.0:
                return "FASE 2 · Solo el reloj"
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
            return M3_TECLAS[i]

        def cuenta(self):
            if self.estado != "juego":
                return ""
            t = self.t_juego()
            primera = self.ev[self.inicio][0]
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
            tabla = {"perfecto": "Perfecto", "bien": "Bien", "fallo": "Fallo",
                     "pronto": "Pronto", "tarde": "Tarde", "suelta": "¡Sin nota!"}
            return tabla.get(self.fb, "")

        def feedback_color(self):
            tabla = {"perfecto": "#FFE3A0", "bien": "#CFE9FF", "fallo": "#FF9A9A",
                     "pronto": "#C9C3D6", "tarde": "#C9C3D6", "suelta": "#FFB27A"}
            return tabla.get(self.fb, "#FFFFFF")

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

        def pista(self):
            if self.estado != "juego" or not self.en_fase2():
                return ""
            if self.guia == "ninguna" and (self.cursor - self.n1) >= M3_GUIA_INICIAL:
                return "Las notas se desvanecen: guíate por el patrón de la izquierda."
            return "Vale cualquier tecla. Cuenta los silencios."

        def visibles(self):
            """Notas a dibujar: (x, y, ancho, alto, alfa, color)."""
            res = []
            if self.estado == "listo":
                return res
            t = self.t_juego()
            color = PETALO_COLOR["miku"]
            x_izq = m3_x(0, self.nc)
            x_der = m3_x(self.nc - 1, self.nc)
            i = self.cursor
            while i < self.total:
                e = self.ev[i]
                dt = e[0] - t
                if dt > self.caida:
                    break
                alto = 34 + ((i * 5) % 4) * 14
                if e[3]:
                    alto = 30
                y = M3_Y_META - int((dt / self.caida) * (M3_Y_META - M3_Y_TOP)) - alto // 2
                if e[3]:
                    k2 = i - self.n1
                    alfa = 1.0
                    if self.guia == "ninguna" and k2 >= M3_GUIA_INICIAL:
                        alfa = M3_ALFA_FANTASMA
                    elif self.guia == "tenue":
                        alfa = 0.35
                    if e[2][0] == "pend":
                        ancho = (x_der - x_izq) + 170
                        res.append((x_izq - 85, y, ancho, alto, alfa, "#FFFFFF"))
                else:
                    for j in range(len(e[1])):
                        if e[2][j] == "pend":
                            tinte = color
                            if e[1][j] % 2 == 1:
                                tinte = ui_mezclar(color, "#FFFFFF", 0.35)
                            res.append((m3_x(e[1][j], self.nc) - 85, y, 170, alto, 1.0, tinte))
                i += 1
            return res

        mj_registrar("m3", "mj_m3", "El compás", True)


################################################################################
##  SCREEN
################################################################################

screen mj_m3(hermana, params, inicio, intento, fallos, nivel, titulo):

    modal True
    zorder 95

    default vivo = MJM3(params, inicio, nivel)

    timer 0.02 repeat True action Function(vivo.tick)

    key "K_a" action Function(vivo.pulsar, 0)
    key "K_s" action Function(vivo.pulsar, 1)
    key "K_d" action Function(vivo.pulsar, 2)
    key "K_f" action Function(vivo.pulsar, 3)
    key "K_SPACE" action Function(vivo.pulsar, -1)
    key "K_RETURN" action Function(vivo.empezar)

    $ color = PETALO_COLOR[hermana]
    $ claro = ui_mezclar(color, "#FFFFFF", 0.35)
    $ nc = vivo.nc
    $ xl = m3_x(0, nc)
    $ xr = m3_x(nc - 1, nc)
    $ x_panel = xl - 130
    $ w_panel = (xr - xl) + 260
    $ h_panel = M3_Y_META + 100 - M3_Y_TOP
    $ listo = (vivo.estado == "listo")
    $ fase2 = vivo.en_fase2()
    $ cuenta = vivo.cuenta()
    $ fb_texto = vivo.feedback()
    $ conc = vivo.concentracion()
    $ col_conc = color
    if conc <= vivo.fallos_max * 0.3:
        $ col_conc = "#FF8A8A"
    $ teclas = "A · S · D"
    if nc == 4:
        $ teclas = "A · S · D · F"
    $ tam_combo = 56
    if vivo.racha >= 10:
        $ tam_combo = 68
    if vivo.racha >= 25:
        $ tam_combo = 82
    $ slot = vivo.slot_actual()
    $ etiquetas_compas = ["1", "+", "2", "+", "3", "+", "4", "+"]
    $ lit_any = (vivo.flash[0] > 0.0 or vivo.flash[1] > 0.0 or vivo.flash[2] > 0.0 or vivo.flash[3] > 0.0)
    $ pct_combo = int(round(vivo.regen_combo * 100.0))
    $ falta_combo = 0
    if vivo.combo_cada > 0:
        $ falta_combo = vivo.combo_cada - (vivo.racha % vivo.combo_cada)

    add "bg_biblioteca" fit "cover"

    use mj_marco(hermana, titulo, intento, fallos, nivel, vivo.cursor, vivo.total, None, None, "NOTAS"):

        if not listo:

            ## --- Rótulo de fase y pista (separados del panel) ---
            text vivo.rotulo_fase():
                xalign 0.5
                ypos 100
                font gui.name_text_font
                size 30
                kerning 3
                color "#FFFFFF"
                outlines [(4, "#1B1026CC", 0, 0)]

            if vivo.pista() != "":
                text vivo.pista():
                    xalign 0.5
                    ypos 142
                    size 22
                    color "#FFE3A0"
                    outlines [(3, "#1B102699", 0, 0)]

            ## --- Panel de carriles ---
            add Solid("#0B0712B0", xsize=w_panel, ysize=h_panel) xpos x_panel ypos (M3_Y_TOP - 10)
            add Solid(color, xsize=4, ysize=h_panel) xpos x_panel ypos (M3_Y_TOP - 10) alpha 0.7
            add Solid(color, xsize=4, ysize=h_panel) xpos (x_panel + w_panel - 4) ypos (M3_Y_TOP - 10) alpha 0.7
            if vivo.flash_fallo > 0.0:
                add Solid("#FF5A5A", xsize=w_panel, ysize=h_panel) xpos x_panel ypos (M3_Y_TOP - 10) alpha 0.16

            for i in range(nc):
                $ alfa_c = 0.07
                if i % 2 == 1:
                    $ alfa_c = 0.11
                if fase2:
                    $ alfa_c = 0.04
                add Solid("#FFFFFF", xsize=M3_ANCHO_CARRIL, ysize=(M3_Y_META + 70 - M3_Y_TOP)) xpos (m3_x(i, nc) - M3_ANCHO_CARRIL // 2) ypos M3_Y_TOP alpha alfa_c
                if vivo.flash[i] > 0.0:
                    add Solid(color, xsize=M3_ANCHO_CARRIL, ysize=(M3_Y_META + 70 - M3_Y_TOP)) xpos (m3_x(i, nc) - M3_ANCHO_CARRIL // 2) ypos M3_Y_TOP alpha 0.32

            ## --- Línea de meta (late con el compás) ---
            add Solid(color, xsize=(w_panel - 40), ysize=22) xpos (x_panel + 20) ypos (M3_Y_META - 8) alpha (vivo.pulso() * 0.25)
            add Solid(claro, xsize=(w_panel - 40), ysize=6) xpos (x_panel + 20) ypos M3_Y_META alpha vivo.pulso()

            ## --- Notas (cuerpo + halo + brillo superior) ---
            for n in vivo.visibles():
                add Solid(n[5], xsize=(n[2] + 20), ysize=(n[3] + 20)) xpos (n[0] - 10) ypos (n[1] - 10) alpha (n[4] * 0.25)
                add Solid(n[5], xsize=n[2], ysize=n[3]) xpos n[0] ypos n[1] alpha n[4]
                add Solid("#FFFFFF", xsize=n[2], ysize=5) xpos n[0] ypos n[1] alpha (n[4] * 0.6)

            if cuenta != "":
                text cuenta:
                    xalign 0.5
                    ypos 330
                    size 110
                    font gui.name_text_font
                    color "#FFFFFF"
                    outlines [(5, "#1B1026CC", 0, 0)]

            ## --- Feedback ---
            if fb_texto != "":
                text fb_texto:
                    xalign 0.5
                    ypos 650
                    font gui.name_text_font
                    size 34
                    color vivo.feedback_color()
                    outlines [(4, "#1B1026CC", 0, 0)]

            ## --- Receptores ---
            if fase2:
                $ fondo_pad = color + "55"
                if lit_any:
                    $ fondo_pad = color + "EE"
                button:
                    xysize ((w_panel - 40), 100)
                    xpos (x_panel + 20)
                    ypos 705
                    action Function(vivo.pulsar, -1)
                    background Solid(fondo_pad)
                    hover_background Solid(color + "99")
                    text "TOCA  ·  cualquier tecla o Espacio":
                        xalign 0.5
                        yalign 0.5
                        font gui.name_text_font
                        size 34
                        color "#FFFFFF"
                        outlines [(3, "#1B102699", 0, 0)]
            else:
                for i in range(nc):
                    $ lit = vivo.flash[i] > 0.0
                    $ fondo_btn = color + "55"
                    if lit:
                        $ fondo_btn = color + "EE"
                    button:
                        xysize (M3_ANCHO_CARRIL, 100)
                        xpos (m3_x(i, nc) - M3_ANCHO_CARRIL // 2)
                        ypos 705
                        action Function(vivo.pulsar, i)
                        background Solid(fondo_btn)
                        hover_background Solid(color + "99")
                        text vivo.rotulo_tecla(i):
                            xalign 0.5
                            yalign 0.5
                            font gui.name_text_font
                            size 40
                            color "#FFFFFF"
                            outlines [(3, "#1B102699", 0, 0)]

            ## --- HUD izquierdo: concentración ---
            vbox:
                xpos 70
                ypos 250
                spacing 8
                text "CONCENTRACIÓN":
                    font gui.name_text_font
                    size 22
                    kerning 3
                    color "#FFFFFF"
                    outlines [(3, "#1B102699", 0, 0)]
                use barra_progreso(conc, vivo.fallos_max, col_conc, 340)
                text ("PERFECTOS  " + str(vivo.perfectos)):
                    size 22
                    color "#E8E0F2"
                    outlines [(3, "#1B102699", 0, 0)]
                if vivo.regen_t > 0.0:
                    text vivo.regen_txt:
                        size 24
                        color "#9BFFB8"
                        outlines [(3, "#1B102699", 0, 0)]

            ## --- HUD izquierdo: patrón del compás (fase 2) ---
            if fase2 and vivo.estado == "juego":
                vbox:
                    xpos 70
                    ypos 410
                    spacing 6
                    text "PATRÓN DEL COMPÁS":
                        font gui.name_text_font
                        size 22
                        kerning 3
                        color "#FFFFFF"
                        outlines [(3, "#1B102699", 0, 0)]
                    hbox:
                        spacing 4
                        for k in range(8):
                            fixed:
                                xysize (38, 44)
                                if k in vivo.plantilla:
                                    add Solid(color, xsize=38, ysize=44)
                                else:
                                    add Solid("#FFFFFF22", xsize=38, ysize=44)
                                if k == slot:
                                    add Solid("#FFE3A0", xsize=38, ysize=44) alpha 0.65
                    hbox:
                        spacing 4
                        for k in range(8):
                            text etiquetas_compas[k]:
                                xsize 38
                                text_align 0.5
                                size 16
                                color "#FFFFFFAA"

            ## --- HUD derecho: combo ---
            if vivo.racha >= 2:
                vbox:
                    xpos 1500
                    ypos 300
                    spacing 0
                    text "COMBO":
                        font gui.name_text_font
                        size 24
                        kerning 4
                        color "#FFFFFF"
                        outlines [(3, "#1B102699", 0, 0)]
                    text str(vivo.racha):
                        font gui.name_text_font
                        size tam_combo
                        color claro
                        outlines [(5, "#1B1026CC", 0, 0)]
                    if vivo.combo_cada > 0 and vivo.regen_combo > 0.0:
                        text ("+" + str(pct_combo) + " % en " + str(falta_combo)):
                            size 20
                            color "#9BFFB8"
                            outlines [(3, "#1B102699", 0, 0)]

        use mj_retrato("miku", vivo.expresion(), vivo.globo, vivo.anim(), 250, 1090, 1.0)

        ## --- Pantalla de inicio ---
        if listo:
            fixed:
                xalign 0.5
                ypos 150
                xysize (1100, 660)

                add Transform(Frame("ui/opcion_neutra.png", 40, 40, 40, 40), matrixcolor=TintMatrix("#1B1026"))
                add Transform(Frame("ui/opcion_marco.png", 40, 40, 40, 40), matrixcolor=TintMatrix(color))

                vbox:
                    xalign 0.5
                    ypos 28
                    xsize 980
                    spacing 12

                    text "EL COMPÁS":
                        xalign 0.5
                        font gui.name_text_font
                        size 40
                        kerning 4
                        color "#FFF8FC"

                    text ("Pulsa el carril cuando la nota llegue a la línea. Teclas: " + teclas + ", o toca los carriles (" + str(nc) + " carriles). Pulsar donde no hay nota te cuesta concentración. Cuando se apaguen los audífonos, sigue el reloj: vale cualquier tecla (o Espacio) y hay silencios; el panel de la izquierda te muestra el patrón. Cada " + str(vivo.combo_cada) + " aciertos seguidos recuperas " + str(pct_combo) + " % de concentración."):
                        xalign 0.5
                        text_align 0.5
                        size 24
                        color "#E8E0F2"

                    add Solid("#FFFFFF33", xsize=980, ysize=2) xalign 0.5

                    text "AJUSTE DE SINCRONÍA DE AUDIO":
                        xalign 0.5
                        font gui.name_text_font
                        size 22
                        kerning 3
                        color claro

                    text "Algunos equipos (sobre todo con audífonos Bluetooth) reproducen el sonido con un pequeño retraso. Si el juego te marca «Tarde» aunque pulses con la música, sube el valor con el botón +. Si te marca «Pronto», bájalo con −. Si todo se siente bien, no toques nada: se guarda para la próxima vez.":
                        xalign 0.5
                        text_align 0.5
                        size 21
                        color "#CFC6E0"

                    hbox:
                        xalign 0.5
                        spacing 18
                        use cinta_boton("−10 ms", Function(vivo.ajustar_latencia, -10), hermana, 190, 56, 24)
                        text (str(persistent.m3_latencia_ms) + " ms"):
                            xsize 150
                            text_align 0.5
                            yalign 0.5
                            size 34
                            color "#FFFFFF"
                        use cinta_boton("+10 ms", Function(vivo.ajustar_latencia, 10), hermana, 190, 56, 24)
                        use cinta_boton("Restablecer", Function(vivo.fijar_latencia, 50), hermana, 220, 56, 22)

                    text "Pulsa los botones para ajustar. Valor por defecto: 50 ms.":
                        xalign 0.5
                        size 19
                        color "#CFC6E0AA"

                fixed:
                    xalign 0.5
                    ypos 560
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