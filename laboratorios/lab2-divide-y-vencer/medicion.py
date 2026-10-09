"""Medicion de tiempos del subarreglo maximo frente al tamano de entrada.

Genera listas con una semilla fija, cronometra la fuerza bruta y el
divide y venceras sobre la misma lista en cada tamano y produce dos
graficas en ``graficas/``: una en escala lineal (la requerida por el
laboratorio) y otra en escala log-log para apreciar la curva del divide
y venceras cuando la fuerza bruta la aplasta contra el eje.

Cada medicion se repite tres veces y se grafica la mediana, para atenuar
el ruido del sistema operativo. Solo se cronometra la llamada al
algoritmo, nunca la generacion de los datos.
"""

from __future__ import annotations

import random
import statistics
import time
from pathlib import Path

import matplotlib.pyplot as plt

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo

TAMANIOS = [10, 50, 100, 500, 1000, 4000, 8000]
REPETICIONES = 3
SEMILLA = 42
CARPETA_GRAFICAS = Path(__file__).resolve().parent / "graficas"


def _generar_datos(n: int, semilla: int) -> list[int]:
    """Genera n variaciones enteras entre -100 y 100 con una semilla fija."""
    rng = random.Random(semilla)
    return [rng.randint(-100, 100) for _ in range(n)]


def _medir_fuerza_bruta(valores: list[int]) -> float:
    """Mide la mediana de REPETICIONES corridas de la fuerza bruta."""
    tiempos = []
    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        subarreglo_fuerza_bruta(valores)
        tiempos.append(time.perf_counter() - inicio)
    return statistics.median(tiempos)


def _medir_divide_y_vencer(valores: list[int]) -> float:
    """Mide la mediana de REPETICIONES corridas del divide y venceras."""
    tiempos = []
    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        subarreglo_maximo(valores, 0, len(valores) - 1)
        tiempos.append(time.perf_counter() - inicio)
    return statistics.median(tiempos)


def main() -> None:
    """Ejecuta el experimento: mide ambos algoritmos y genera las graficas."""
    CARPETA_GRAFICAS.mkdir(exist_ok=True)

    filas: list[tuple[int, float, float]] = []
    for n in TAMANIOS:
        valores = _generar_datos(n, SEMILLA)

        suma_fb = subarreglo_fuerza_bruta(valores)[2]
        suma_dv = subarreglo_maximo(valores, 0, n - 1)[2]
        assert suma_fb == suma_dv, f"suma distinta en n={n}"

        t_fb = _medir_fuerza_bruta(valores)
        t_dv = _medir_divide_y_vencer(valores)
        filas.append((n, t_fb, t_dv))
        print(
            f"n={n:>5}  fuerza_bruta={t_fb * 1000:10.3f} ms  "
            f"divide_venceras={t_dv * 1000:10.3f} ms  suma={suma_fb}"
        )

    _graficar_lineal(filas)
    _graficar_loglog(filas)


def _graficar_lineal(filas: list[tuple[int, float, float]]) -> None:
    """Grafica ambas curvas en escala lineal (la grafica requerida)."""
    tamanios = [fila[0] for fila in filas]
    t_fb = [fila[1] * 1000 for fila in filas]
    t_dv = [fila[2] * 1000 for fila in filas]

    fig, eje = plt.subplots(figsize=(8, 5))
    eje.plot(tamanios, t_fb, "o-", color="#d62728", linewidth=2, markersize=6,
             label="Fuerza bruta")
    eje.plot(tamanios, t_dv, "s-", color="#1f77b4", linewidth=2, markersize=6,
             label="Divide y venceras")
    eje.set_title("Tiempo del subarreglo maximo vs. tamano de entrada")
    eje.set_xlabel("Tamano de entrada n (dias)")
    eje.set_ylabel("Tiempo de ejecucion (ms)")
    eje.legend(loc="upper left")
    eje.grid(True, which="both", linestyle="--", linewidth=0.5)
    fig.tight_layout()
    fig.savefig(CARPETA_GRAFICAS / "tiempo_vs_n.png", dpi=150)
    plt.close(fig)


def _graficar_loglog(filas: list[tuple[int, float, float]]) -> None:
    """Grafica ambas curvas en escala log-log para ver la forma de cada una."""
    tamanios = [fila[0] for fila in filas]
    t_fb = [fila[1] * 1000 for fila in filas]
    t_dv = [fila[2] * 1000 for fila in filas]

    fig, eje = plt.subplots(figsize=(8, 5))
    eje.plot(tamanios, t_fb, "o-", color="#d62728", linewidth=2, markersize=6,
             label="Fuerza bruta")
    eje.plot(tamanios, t_dv, "s-", color="#1f77b4", linewidth=2, markersize=6,
             label="Divide y venceras")
    eje.set_xscale("log")
    eje.set_yscale("log")
    eje.set_title("Tiempo del subarreglo maximo vs. tamano (escala log-log)")
    eje.set_xlabel("Tamano de entrada n (dias)")
    eje.set_ylabel("Tiempo de ejecucion (ms)")
    eje.legend(loc="upper left")
    eje.grid(True, which="both", linestyle="--", linewidth=0.5)
    fig.tight_layout()
    fig.savefig(CARPETA_GRAFICAS / "tiempo_vs_n_loglog.png", dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    main()