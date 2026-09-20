"""Algoritmos de ordenamiento instrumentados para el Laboratorio 1.

Todos los algoritmos de este modulo estan adaptados al criterio de
Tamiza: ordenan de mayor a menor segun el indice de riesgo. Cada
funcion devuelve una copia ordenada de la lista recibida y el numero
de comparaciones entre elementos realizadas durante el proceso.
"""

from __future__ import annotations


def insertion_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de insercion.

    No modifica la lista recibida: trabaja sobre una copia. Produce la
    lista ordenada de mayor a menor, que es como Tamiza la necesita
    para que el centro de contacto llame primero a los pacientes con
    mayor riesgo.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    arreglo = list(datos)
    n = len(arreglo)
    comparaciones = 0
    for i in range(1, n):
        clave = arreglo[i]
        j = i - 1
        while j > -1 and arreglo[j] < clave:
            comparaciones += 1
            arreglo[j + 1] = arreglo[j]
            j -= 1
        if j > -1:
            comparaciones += 1
        arreglo[j + 1] = clave
    return arreglo, comparaciones


def merge_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de mezcla.

    No modifica la lista recibida: trabaja sobre una copia. Produce la
    lista ordenada de mayor a menor, igual que ``insertion_sort``.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas dentro de la mezcla.
    """
    arreglo = list(datos)
    comparaciones = [0]
    _merge_sort_recursivo(arreglo, 0, len(arreglo) - 1, comparaciones)
    return arreglo, comparaciones[0]


def _merge_sort_recursivo(
    arreglo: list[int], inicio: int, fin: int, comparaciones: list[int]
) -> None:
    if inicio >= fin:
        return
    medio = (inicio + fin) // 2
    _merge_sort_recursivo(arreglo, inicio, medio, comparaciones)
    _merge_sort_recursivo(arreglo, medio + 1, fin, comparaciones)
    _mezclar(arreglo, inicio, medio, fin, comparaciones)


def _mezclar(
    arreglo: list[int], inicio: int, medio: int, fin: int, comparaciones: list[int]
) -> None:
    izquierda = arreglo[inicio : medio + 1]
    derecha = arreglo[medio + 1 : fin + 1]
    i = 0
    j = 0
    k = inicio
    while i < len(izquierda) and j < len(derecha):
        comparaciones[0] += 1
        if izquierda[i] >= derecha[j]:
            arreglo[k] = izquierda[i]
            i += 1
        else:
            arreglo[k] = derecha[j]
            j += 1
        k += 1
    while i < len(izquierda):
        arreglo[k] = izquierda[i]
        i += 1
        k += 1
    while j < len(derecha):
        arreglo[k] = derecha[j]
        j += 1
        k += 1
