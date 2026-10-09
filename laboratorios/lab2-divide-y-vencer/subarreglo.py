"""Subarreglo maximo: fuerza bruta y divide y venceras."""

from __future__ import annotations


def subarreglo_fuerza_bruta(valores: list[float]) -> tuple[int, int, float]:
    """Encuentra la mejor racha probando todos los pares de dias (i, j).

    Args:
        valores: variacion diaria de caja, una por dia. Tiene al menos
            un elemento.

    Returns:
        Una tupla (inicio, fin, suma) con los indices inclusivos del
        tramo de mayor suma y el valor de esa suma.
    """
    n = len(valores)
    mejor_inicio = 0
    mejor_fin = 0
    mejor_suma = valores[0]
    for inicio in range(n):
        suma_actual = 0.0
        for fin in range(inicio, n):
            suma_actual += valores[fin]
            if suma_actual > mejor_suma:
                mejor_suma = suma_actual
                mejor_inicio = inicio
                mejor_fin = fin
    return mejor_inicio, mejor_fin, mejor_suma


def suma_cruzada(
    valores: list[float], inicio: int, medio: int, fin: int
) -> tuple[int, int, float]:
    """Encuentra el mejor tramo que cruza el punto medio.

    Args:
        valores: variacion diaria de caja.
        inicio: indice inicial del rango considerado (inclusive).
        medio: indice del ultimo elemento de la mitad izquierda.
        fin: indice final del rango considerado (inclusive).

    Returns:
        Una tupla (inicio, fin, suma) del mejor tramo que incluye al
        menos un elemento de cada mitad.
    """
    inicio_izq = medio
    mejor_suma_izq = float("-inf")
    suma_izq = 0.0
    for i in range(medio, inicio - 1, -1):
        suma_izq += valores[i]
        if suma_izq > mejor_suma_izq:
            mejor_suma_izq = suma_izq
            inicio_izq = i

    fin_der = medio + 1
    mejor_suma_der = float("-inf")
    suma_der = 0.0
    for j in range(medio + 1, fin + 1):
        suma_der += valores[j]
        if suma_der > mejor_suma_der:
            mejor_suma_der = suma_der
            fin_der = j

    return inicio_izq, fin_der, mejor_suma_izq + mejor_suma_der


def subarreglo_maximo(
    valores: list[float], inicio: int, fin: int
) -> tuple[int, int, float]:
    """Encuentra la mejor racha por divide y venceras.

    Args:
        valores: variacion diaria de caja.
        inicio: indice inicial del rango a considerar (inclusive).
        fin: indice final del rango a considerar (inclusive).

    Returns:
        Una tupla (inicio, fin, suma) del mejor tramo dentro de
        valores[inicio..fin].
    """
    if inicio == fin:
        return inicio, fin, valores[inicio]

    medio = (inicio + fin) // 2
    mejor_izquierdo = subarreglo_maximo(valores, inicio, medio)
    mejor_derecho = subarreglo_maximo(valores, medio + 1, fin)
    mejor_cruzado = suma_cruzada(valores, inicio, medio, fin)

    mejor = mejor_izquierdo
    if mejor_derecho[2] > mejor[2]:
        mejor = mejor_derecho
    if mejor_cruzado[2] > mejor[2]:
        mejor = mejor_cruzado
    return mejor