"""Generadores de lotes de registros para los escenarios de Tamiza.

Los tres generadores producen listas con valores enteros distintos en
el rango 0..999, que es el rango valido del indice de riesgo calculado
por la plataforma. Todos entregan lotes en la misma unidad con la que
trabajan ``insertion_sort`` y ``merge_sort``: ordenados de mayor a
menor es el resultado que Tamiza espera recibir.

Escenarios:

* A ``generar_aleatorio``: lote en orden aleatorio respecto al riesgo.
* B ``generar_casi_ordenado``: 98 % ya en el orden que Tamiza espera,
  2 % restante desordenado y anexado al final.
* C ``generar_inverso``: lote en orden exactamente contrario al que
  Tamiza espera.
"""

from __future__ import annotations

import random


def _muestreo_sin_repetidos(n: int, aleatorio: random.Random) -> list[int]:
    """Devuelve n valores enteros distintos en 0..n^2 sin repeticion."""
    poblacion = max(n + 1, n * n)
    return aleatorio.sample(range(poblacion), n)


def generar_aleatorio(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote de n registros en orden aleatorio (escenario A).

    Args:
        n: cantidad de registros del lote.
        semilla: semilla del generador aleatorio, para que el
            experimento sea reproducible.

    Returns:
        Lista de n indices de riesgo enteros distintos, desordenada,
        en el orden en que los laboratorios los subieron al portal.
    """
    aleatorio = random.Random(semilla)
    return _muestreo_sin_repetidos(n, aleatorio)


def generar_casi_ordenado(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote casi ordenado: 98 % ordenado y 2 % al final (escenario B).

    El 98 % del lote se entrega ya en el orden que Tamiza necesita
    (de mayor a menor riesgo). El 2 % restante son los registros
    nuevos del dia, desordenados y anexados al final del lote.

    Args:
        n: cantidad de registros del lote.
        semilla: semilla del generador aleatorio.

    Returns:
        Lista de n indices de riesgo enteros distintos, con el primer
        98 % en orden descendente y el 2 % final desordenado.
    """
    aleatorio = random.Random(semilla)
    valores = _muestreo_sin_repetidos(n, aleatorio)
    valores.sort(reverse=True)
    corte = int(0.98 * n)
    cabeza = valores[:corte]
    cola = valores[corte:]
    aleatorio.shuffle(cola)
    return cabeza + cola


def generar_inverso(n: int) -> list[int]:
    """Genera un lote en el orden exactamente contrario (escenario C).

    Args:
        n: cantidad de registros del lote.

    Returns:
        Lista de n indices de riesgo enteros distintos, en el orden
        inverso al que el algoritmo debe producir: de menor a mayor.
    """
    return list(range(n))
