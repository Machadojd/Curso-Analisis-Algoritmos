"""Medicion de tiempos de busqueda de la lista enlazada y la tabla hash.

Ejecuta dos experimentos y genera sus graficas en ``graficas/``:
el Experimento A compara la lista enlazada con la tabla hash frente al
numero de guias (n), y el Experimento B mide el efecto del factor de
carga (alfa) con n fijo.

Cada medicion cronometra unicamente las busquedas, nunca la construccion
de las estructuras ni la generacion de los datos. Se miden 200 busquedas
de guias inexistentes y se calcula el tiempo medio por busqueda; el
procedimiento completo se repite tres veces y se grafica la mediana.
"""

from __future__ import annotations

import random
import statistics
import time
from pathlib import Path

import matplotlib.pyplot as plt

from estructuras import ListaEnlazada, TablaHash

CARPETA_GRAFICAS = Path(__file__).resolve().parent / "graficas"

SEMILLA = 42
BUSQUEDAS = 200
BUSQUEDAS_B = 2000
REPETICIONES = 3
ESTADOS = ("en bodega", "en reparto", "entregado", "en oficina")


def generar_guias_inexistentes(
    existentes: set[int], cantidad: int, semilla: int = 7
) -> list[int]:
    """Genera guias de diez digitos que no estan en la coleccion.

    Args:
        existentes: guias almacenadas en las estructuras.
        cantidad: cuantas guias inexistentes generar.
        semilla: semilla del generador, para reproducir la medicion.

    Returns:
        Una lista con `cantidad` guias que no pertenecen a `existentes`.
    """
    azar = random.Random(semilla)
    inexistentes: list[int] = []
    while len(inexistentes) < cantidad:
        guia = azar.randint(10**9, 10**10 - 1)
        if guia not in existentes:
            inexistentes.append(guia)
    return inexistentes


def _generar_guias(n: int, semilla: int) -> list[int]:
    """Genera n guias de diez digitos, todas distintas.

    Args:
        n: cantidad de guias a generar.
        semilla: semilla del generador, para reproducir la medicion.

    Returns:
        Una lista con n guias distintas.
    """
    azar = random.Random(semilla)
    vistos: set[int] = set()
    guias: list[int] = []
    while len(guias) < n:
        guia = azar.randint(10**9, 10**10 - 1)
        if guia not in vistos:
            vistos.add(guia)
            guias.append(guia)
    return guias


def _estado_de(guia: int) -> str:
    """Asigna un estado determinista a una guia para la verificacion."""
    return ESTADOS[guia % len(ESTADOS)]


def _es_primo(num: int) -> bool:
    """Indica si un entero positivo es primo.

    Args:
        num: entero a comprobar.

    Returns:
        True si el numero es primo, False en caso contrario.
    """
    if num < 2:
        return False
    if num % 2 == 0:
        return num == 2
    divisor = 3
    while divisor * divisor <= num:
        if num % divisor == 0:
            return False
        divisor += 2
    return True


def _primo_cercano(objetivo: int) -> int:
    """Devuelve el primer numero primo mayor o igual que objetivo.

    Args:
        objetivo: valor alrededor del cual buscar el primo.

    Returns:
        Un numero primo mayor o igual que objetivo.
    """
    candidato = objetivo
    while not _es_primo(candidato):
        candidato += 1
    return candidato


def _tiempo_medio_busqueda(estructura: object, guias: list[int]) -> float:
    """Mide el tiempo medio por busqueda de una estructura.

    Args:
        estructura: objeto con el metodo buscar.
        guias: guias a buscar.

    Returns:
        Tiempo medio (en segundos) por cada busqueda.
    """
    inicio = time.perf_counter()
    for guia in guias:
        estructura.buscar(guia)
    return (time.perf_counter() - inicio) / len(guias)


def _medir(estructura: object, guias: list[int]) -> float:
    """Mide la mediana de REPETICIONES corridas de tiempo medio por busqueda.

    Args:
        estructura: objeto con el metodo buscar.
        guias: guias a buscar.

    Returns:
        La mediana de los tiempos medios por busqueda.
    """
    tiempos = [
        _tiempo_medio_busqueda(estructura, guias) for _ in range(REPETICIONES)
    ]
    return statistics.median(tiempos)


def _graficar_lista_vs_tabla(filas: list[tuple[int, float, float]]) -> None:
    """Grafica tiempo medio por busqueda frente a n para ambas estructuras."""
    tamanios = [fila[0] for fila in filas]
    t_lista = [fila[1] * 1000 for fila in filas]
    t_tabla = [fila[2] * 1000 for fila in filas]

    fig, eje = plt.subplots(figsize=(8, 5))
    eje.plot(tamanios, t_lista, "o-", color="#d62728", linewidth=2,
             markersize=6, label="Lista enlazada")
    eje.plot(tamanios, t_tabla, "s-", color="#1f77b4", linewidth=2,
             markersize=6, label="Tabla hash")
    eje.set_title(
        "Experimento A - tiempo medio por busqueda vs. numero de guias"
    )
    eje.set_xlabel("Numero de guias n")
    eje.set_ylabel("Tiempo medio por busqueda (ms)")
    eje.legend(loc="upper left")
    eje.grid(True, which="both", linestyle="--", linewidth=0.5)
    fig.tight_layout()
    fig.savefig(CARPETA_GRAFICAS / "lista_vs_tabla.png", dpi=150)
    plt.close(fig)


def _graficar_tiempo_vs_alfa(filas: list[tuple[float, float]]) -> None:
    """Grafica tiempo medio por busqueda frente al factor de carga alfa."""
    alfas = [fila[0] for fila in filas]
    t_tabla = [fila[1] * 1_000_000 for fila in filas]

    fig, eje = plt.subplots(figsize=(8, 5))
    eje.plot(alfas, t_tabla, "o-", color="#1f77b4", linewidth=2,
             markersize=6, label="Tabla hash")
    eje.set_title(
        "Experimento B - tiempo medio por busqueda vs. factor de carga"
    )
    eje.set_xlabel("Factor de carga alfa (n / m)")
    eje.set_ylabel("Tiempo medio por busqueda (us)")
    eje.legend(loc="upper left")
    eje.grid(True, which="both", linestyle="--", linewidth=0.5)
    fig.tight_layout()
    fig.savefig(CARPETA_GRAFICAS / "tiempo_vs_alfa.png", dpi=150)
    plt.close(fig)


def _experimento_a() -> None:
    """Ejecuta el Experimento A: lista frente a tabla segun n."""
    tamanios = [100, 500, 1000, 5000, 20000, 50000]
    filas: list[tuple[int, float, float]] = []
    for n in tamanios:
        guias = _generar_guias(n, SEMILLA)
        inexistentes = generar_guias_inexistentes(
            set(guias), BUSQUEDAS, semilla=7
        )

        lista = ListaEnlazada()
        tabla = TablaHash(_primo_cercano(n // 2))
        for guia in guias:
            lista.insertar(guia, _estado_de(guia))
            tabla.insertar(guia, _estado_de(guia))

        for guia in guias[:20]:
            assert lista.buscar(guia) == tabla.buscar(guia)

        t_lista = _medir(lista, inexistentes)
        t_tabla = _medir(tabla, inexistentes)
        filas.append((n, t_lista, t_tabla))
        print(
            f"n={n:>6} (m={tabla.m}, alfa={tabla.factor_carga():.2f})  "
            f"lista={t_lista * 1000:9.3f} ms  tabla={t_tabla * 1000:9.3f} ms"
        )

    _graficar_lista_vs_tabla(filas)


def _experimento_b() -> None:
    """Ejecuta el Experimento B: efecto del factor de carga con n fijo."""
    n = 20000
    alfas_objetivo = [0.5, 1.0, 4.0, 10.0]
    guias = _generar_guias(n, SEMILLA)
    inexistentes = generar_guias_inexistentes(
        set(guias), BUSQUEDAS_B, semilla=7
    )

    filas: list[tuple[float, float]] = []
    for alfa_objetivo in alfas_objetivo:
        m = _primo_cercano(round(n / alfa_objetivo))
        tabla = TablaHash(m)
        for guia in guias:
            tabla.insertar(guia, _estado_de(guia))
        t = _medir(tabla, inexistentes)
        alfa_real = tabla.factor_carga()
        filas.append((alfa_real, t))
        print(
            f"alfa={alfa_real:6.2f} (m={m})  tabla={t * 1_000_000:9.3f} us"
        )

    _graficar_tiempo_vs_alfa(filas)


def main() -> None:
    """Ejecuta los dos experimentos y genera sus graficas."""
    CARPETA_GRAFICAS.mkdir(exist_ok=True)
    _experimento_a()
    _experimento_b()


if __name__ == "__main__":
    main()