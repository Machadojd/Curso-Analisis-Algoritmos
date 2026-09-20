"""Parte 3: peor, mejor y caso promedio de insertion sort en Tamiza.

Mide tiempo de ejecucion y numero de comparaciones de ``insertion_sort``
sobre los tres escenarios de entrada definidos en ``datos.py`` y genera
las dos graficas de comparaciones y tiempo en ``graficas/``.
"""

from __future__ import annotations

import time
from pathlib import Path

import matplotlib.pyplot as plt

from algoritmos import insertion_sort
from datos import generar_aleatorio, generar_casi_ordenado, generar_inverso


TAMAÑOS = [100, 200, 400, 800, 1600, 3200, 6400]
REPETICIONES = 3
SEMILLA = 42
CARPETA_GRAFICAS = Path(__file__).resolve().parent / "graficas"


def _medir_insertion_sort(generador) -> tuple[float, int]:
    """Cronometra y cuenta comparaciones de insertion sort para un lote.

    El cronometro cubre unicamente la llamada al algoritmo; la
    generacion del lote se hace afuera de medicion.
    """
    lote = generador()
    tiempo_total = 0.0
    comparaciones_acumuladas = 0
    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        _, comparaciones = insertion_sort(lote)
        tiempo_total += time.perf_counter() - inicio
        comparaciones_acumuladas += comparaciones
    return tiempo_total / REPETICIONES, comparaciones_acumuladas // REPETICIONES


def main() -> None:
    CARPETA_GRAFICAS.mkdir(exist_ok=True)

    escenarios = {
        "A aleatorio": lambda n: generar_aleatorio(n, SEMILLA),
        "B casi ordenado": lambda n: generar_casi_ordenado(n, SEMILLA),
        "C inverso": generar_inverso,
    }

    resultados: dict[str, list[tuple[int, float, int]]] = {
        nombre: [] for nombre in escenarios
    }
    for n in TAMAÑOS:
        for nombre, generador in escenarios.items():
            lote = generador(n)
            tiempo, comparaciones = _medir_insertion_sort(lambda: lote)
            resultados[nombre].append((n, tiempo, comparaciones))

    for nombre, datos in resultados.items():
        print(f"Escenario {nombre}:")
        for n, tiempo, cmp in datos:
            print(f"  n={n:>5}  tiempo={tiempo*1000:8.3f} ms  comparaciones={cmp}")

    _graficar(resultados)


def _graficar(resultados: dict[str, list[tuple[int, float, int]]]) -> None:
    colores = {
        "A aleatorio": "#1f77b4",
        "B casi ordenado": "#2ca02c",
        "C inverso": "#d62728",
    }
    marcadores = {
        "A aleatorio": "o",
        "B casi ordenado": "s",
        "C inverso": "^",
    }

    fig, eje = plt.subplots(figsize=(8, 5))
    for nombre, datos in resultados.items():
        tamaños = [d[0] for d in datos]
        comparaciones = [d[2] for d in datos]
        eje.plot(
            tamaños,
            comparaciones,
            marker=marcadores[nombre],
            color=colores[nombre],
            label=nombre,
        )
    eje.set_title(
        "Parte 3 - Comparaciones de insertion sort vs. tamano de entrada\n"
        "Escenarios A (aleatorio), B (casi ordenado) y C (inverso)"
    )
    eje.set_xlabel("Tamano de entrada n (registros)")
    eje.set_ylabel("Numero de comparaciones entre elementos")
    eje.legend(loc="upper left")
    eje.grid(True, which="both", linestyle="--", linewidth=0.5)
    fig.tight_layout()
    fig.savefig(CARPETA_GRAFICAS / "parte3_comparaciones.png", dpi=150)
    plt.close(fig)

    fig, eje = plt.subplots(figsize=(8, 5))
    for nombre, datos in resultados.items():
        tamaños = [d[0] for d in datos]
        tiempos = [d[1] * 1000 for d in datos]
        eje.plot(
            tamaños,
            tiempos,
            marker=marcadores[nombre],
            color=colores[nombre],
            label=nombre,
        )
    eje.set_title(
        "Parte 3 - Tiempo de insertion sort vs. tamano de entrada\n"
        "Escenarios A (aleatorio), B (casi ordenado) y C (inverso)"
    )
    eje.set_xlabel("Tamano de entrada n (registros)")
    eje.set_ylabel("Tiempo de ejecucion (ms)")
    eje.legend(loc="upper left")
    eje.grid(True, which="both", linestyle="--", linewidth=0.5)
    fig.tight_layout()
    fig.savefig(CARPETA_GRAFICAS / "parte3_tiempo.png", dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    main()
