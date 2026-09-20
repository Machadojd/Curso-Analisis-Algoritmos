"""Parte 4: comparacion empirica de insertion sort vs. merge sort.

Mide el tiempo de ejecucion de ambos algoritmos sobre el escenario A
(aleatorio) de Tamiza y genera la grafica ``parte4_tiempo.png`` en la
carpeta ``graficas/``. Los tamanos son los mismos de la Parte 3 y se
trabaja con la mediana de tres corridas para atenuar el ruido del
sistema operativo.
"""

from __future__ import annotations

import statistics
import time
from pathlib import Path

import matplotlib.pyplot as plt

from algoritmos import insertion_sort, merge_sort
from datos import generar_aleatorio


TAMAÑOS = [100, 200, 400, 800, 1600, 3200, 6400]
REPETICIONES = 3
SEMILLA = 42
CARPETA_GRAFICAS = Path(__file__).resolve().parent / "graficas"


def _medir(algoritmo, lote: list[int]) -> tuple[float, int]:
    tiempos = []
    comparaciones = None
    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        _, cuenta = algoritmo(lote)
        tiempos.append(time.perf_counter() - inicio)
        comparaciones = cuenta
    return statistics.median(tiempos), comparaciones


def main() -> None:
    CARPETA_GRAFICAS.mkdir(exist_ok=True)

    resultados = {"insertion sort": [], "merge sort": []}
    for n in TAMAÑOS:
        lote = generar_aleatorio(n, SEMILLA)
        t_ins, cmp_ins = _medir(insertion_sort, lote)
        t_mer, cmp_mer = _medir(merge_sort, lote)
        resultados["insertion sort"].append((n, t_ins, cmp_ins))
        resultados["merge sort"].append((n, t_mer, cmp_mer))
        print(
            f"n={n:>5}  insertion={t_ins*1000:8.3f} ms ({cmp_ins} cmp)  "
            f"merge={t_mer*1000:8.3f} ms ({cmp_mer} cmp)"
        )

    _graficar(resultados)


def _graficar(resultados: dict[str, list[tuple[int, float, int]]]) -> None:
    fig, eje = plt.subplots(figsize=(8, 5))
    estilos = {
        "insertion sort": {"color": "#d62728", "marker": "o"},
        "merge sort": {"color": "#1f77b4", "marker": "s"},
    }
    for nombre, datos in resultados.items():
        tamaños = [d[0] for d in datos]
        tiempos = [d[1] * 1000 for d in datos]
        eje.plot(
            tamaños,
            tiempos,
            **estilos[nombre],
            linewidth=2,
            markersize=7,
            label=nombre,
        )
    eje.set_title(
        "Parte 4 - Tiempo de ordenamiento vs. tamano de entrada\n"
        "Escenario A (aleatorio) - insertion sort vs. merge sort"
    )
    eje.set_xlabel("Tamano de entrada n (registros)")
    eje.set_ylabel("Tiempo de ejecucion (ms)")
    eje.legend(loc="upper left")
    eje.grid(True, which="both", linestyle="--", linewidth=0.5)
    fig.tight_layout()
    fig.savefig(CARPETA_GRAFICAS / "parte4_tiempo.png", dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    main()
