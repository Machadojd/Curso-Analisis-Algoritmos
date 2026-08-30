"""Calculo del promedio de una lista de numeros (estilo PEP 8).

Refactor del script de partida entregado en el Laboratorio 02.
Demuestra el uso de type hints, docstrings y entrada controlada
por la guarda `if __name__ == "__main__":`.
"""

from typing import Iterable


def calcular_promedio(valores: Iterable[float]) -> float:
    """Calcula la media aritmetica de una secuencia de numeros.

    Args:
        valores: iterable de numeros (enteros o flotantes) a promediar.

    Returns:
        Promedio aritmetico de los valores recibidos.

    Raises:
        ValueError: si el iterable esta vacio (no se puede promediar).
    """
    numeros = list(valores)
    if not numeros:
        raise ValueError("La lista de valores no puede estar vacia.")
    return sum(numeros) / len(numeros)


def main() -> None:
    """Punto de entrada del script: promedia la lista de ejemplo."""
    valores_de_ejemplo: list[int] = [1, 2, 3, 4, 5]
    promedio: float = calcular_promedio(valores_de_ejemplo)
    print(f"Lista: {valores_de_ejemplo}")
    print(f"Promedio: {promedio}")


if __name__ == "__main__":
    main()
