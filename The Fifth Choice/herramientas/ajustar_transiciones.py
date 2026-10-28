#!/usr/bin/env python3
# ajustar_transiciones.py
# Cambia "with fade" por "with dissolve" en cambios BG<->CG y en scenes
# seguidos sin texto en medio.
# Uso (desde herramientas/):
#   python ajustar_transiciones.py            (solo informe)
#   python ajustar_transiciones.py --aplicar  (escribe los cambios)

import sys
from pathlib import Path

CARPETA = Path(__file__).resolve().parent.parent / "game"

# Estos se quedan con fade (o se pasan a corte_seco a mano)
EXCEPCIONES = ["cg_manija_edificio", "cg_maruo_reunion", "cg_maruo_espaldas"]


def main():
    aplicar = "--aplicar" in sys.argv
    total = 0

    for archivo in sorted(CARPETA.glob("*.rpy")):
        lineas = archivo.read_text(encoding="utf-8-sig").split("\n")
        escena_anterior = None
        hubo_algo_entre = True
        cambios = 0

        for i in range(len(lineas)):
            texto = lineas[i].strip()

            if texto.startswith("label "):
                escena_anterior = None
                hubo_algo_entre = True
                continue

            if texto.startswith("scene "):
                escena = texto.split()[1]

                # Buscar la siguiente línea que no esté vacía
                j = i + 1
                while j < len(lineas) and lineas[j].strip() == "":
                    j = j + 1

                if j < len(lineas) and lineas[j].strip() == "with fade":
                    cambiar = False

                    if escena_anterior is not None:
                        if escena != "bg_negro" and escena_anterior != "bg_negro":
                            if escena.startswith("cg_") or escena_anterior.startswith("cg_"):
                                cambiar = True
                            if not hubo_algo_entre:
                                cambiar = True

                    if escena in EXCEPCIONES:
                        cambiar = False

                    if cambiar:
                        lineas[j] = lineas[j].replace("with fade", "with dissolve")
                        cambios = cambios + 1
                        print(archivo.name + ":" + str(i + 1) + "  " + escena + "  fade -> dissolve")

                escena_anterior = escena
                hubo_algo_entre = False
                continue

            if texto == "" or texto.startswith("#") or texto.startswith("with "):
                continue

            hubo_algo_entre = True

        if cambios > 0 and aplicar:
            archivo.write_text("\n".join(lineas), encoding="utf-8")

        total = total + cambios

    if aplicar:
        print("\nAplicados: " + str(total))
    else:
        print("\nSolo informe. Cambios posibles: " + str(total) + "  (usa --aplicar para escribirlos)")


if __name__ == "__main__":
    main()