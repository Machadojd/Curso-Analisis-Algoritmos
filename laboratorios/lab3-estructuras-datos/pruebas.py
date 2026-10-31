"""Pruebas de verificacion para la lista enlazada y la tabla hash.

Compara que ambas estructuras devuelven el mismo estado ante los mismos
datos, incluidas las busquedas de guias que no existen, y verifica la
colision forzada y el factor de carga.
"""

from __future__ import annotations

import random

from estructuras import ListaEnlazada, TablaHash


def main() -> None:
    lista = ListaEnlazada()
    lista.insertar(10, "en bodega")
    lista.insertar(24, "en reparto")
    lista.insertar(17, "entregado")
    assert lista.buscar(24) == "en reparto"
    assert lista.buscar(99) is None

    tabla = TablaHash(7)
    pares = ((10, "en bodega"), (24, "en reparto"), (17, "entregado"))
    for guia, estado in pares:
        tabla.insertar(guia, estado)
    assert tabla.buscar(24) == "en reparto"
    assert tabla.buscar(99) is None
    assert [tabla.hash(g) for g in (10, 24, 17)] == [3, 3, 3]
    assert tabla.casillas[3].tamano == 3
    assert tabla.factor_carga() == 3 / 7

    for estado in ("en bodega", "en reparto", "entregado"):
        assert estado in (tabla.buscar(10), tabla.buscar(24), tabla.buscar(17))

    rng = random.Random(20261031)
    for _ in range(30):
        n = rng.randint(1, 200)
        m = rng.randint(1, 97)
        lista = ListaEnlazada()
        tabla = TablaHash(m)
        guias: list[int] = []
        for _ in range(n):
            guia = rng.randint(10**9, 10**10 - 1)
            while guia in guias:
                guia = rng.randint(10**9, 10**10 - 1)
            estado = "en bodega" if guia % 2 == 0 else "en reparto"
            guias.append(guia)
            lista.insertar(guia, estado)
            tabla.insertar(guia, estado)

        for guia in guias:
            assert lista.buscar(guia) == tabla.buscar(guia)

        for _ in range(20):
            inexistente = rng.randint(10**9, 10**10 - 1)
            while inexistente in guias:
                inexistente = rng.randint(10**9, 10**10 - 1)
            assert lista.buscar(inexistente) is None
            assert tabla.buscar(inexistente) is None

    print("Todas las pruebas pasaron.")


if __name__ == "__main__":
    main()