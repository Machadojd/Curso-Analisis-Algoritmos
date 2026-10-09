"""Pruebas de verificacion para las soluciones del subarreglo maximo.

Compara la suma devuelta por la fuerza bruta y por divide y venceras en
casos de resultado conocido, mas un lote de listas aleatorias donde ambas
deben coincidir. Los tramos se comparan por su suma, no por sus indices.
"""

from __future__ import annotations

import random

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo


def main() -> None:
    serie = [-3, 5, -2, 8, -6, 3, 9, -4]
    assert subarreglo_fuerza_bruta(serie)[2] == 17
    assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == 17

    unidad = [7]
    assert subarreglo_fuerza_bruta(unidad)[2] == 7
    assert subarreglo_maximo(unidad, 0, 0)[2] == 7

    negativos = [-4, -1, -8, -2, -5]
    assert subarreglo_fuerza_bruta(negativos)[2] == -1
    assert subarreglo_maximo(negativos, 0, len(negativos) - 1)[2] == -1

    positivos = [1, 2, 3, 4, 5]
    assert subarreglo_fuerza_bruta(positivos)[2] == 15
    assert subarreglo_maximo(positivos, 0, len(positivos) - 1)[2] == 15

    cruzado = [1, -2, 3, -1, 4, -3]
    assert subarreglo_fuerza_bruta(cruzado)[2] == 6
    assert subarreglo_maximo(cruzado, 0, len(cruzado) - 1)[2] == 6

    rng = random.Random(2026)
    for _ in range(30):
        n = rng.randint(1, 60)
        lista = [rng.randint(-100, 100) for _ in range(n)]
        suma_fb = subarreglo_fuerza_bruta(lista)[2]
        suma_dv = subarreglo_maximo(lista, 0, n - 1)[2]
        assert suma_fb == suma_dv, f"discrepancia en lista de n={n}: {lista}"

    print("Todas las pruebas pasaron.")


if __name__ == "__main__":
    main()