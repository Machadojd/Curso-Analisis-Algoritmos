# Retroalimentación — Laboratorio 3: Estructuras de datos

**Estudiante:** Juan David Machado Mosquera · **Laboratorio:** Laboratorio evaluativo 03 — Estructuras de datos
**Fecha límite:** 2026-11-01 23:59 · **Versión revisada:** commit `d9c1ed8`

Muy buen trabajo: las estructuras funcionan y el informe es claro.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 19 / 20 |
| Calidad de la explicación teórica | 20 / 20 |
| Corrección de la implementación | 23 / 25 |
| Calidad del análisis de las gráficas | 24 / 25 |
| Documentación y organización del informe | 9 / 10 |
| **Total** | **95 / 100** |
| **Nota (0–5)** | **4.75** |

## 1. Corrección conceptual (19 / 20)
**Lo que hizo bien:**
- Explica bien qué es una colisión y por qué ocurre aunque haya más casillas que guías, usando el ejemplo de `10`, `24` y `17` con `m = 7`.
- Compara encadenamiento y direccionamiento abierto con ventajas y costos de cada uno.
- Justifica por qué la tabla no sirve para rangos y estima la altura del árbol degenerado (400.000) frente al equilibrado (cerca de 19).
- Recomienda tabla hash más árbol equilibrado y declara la cifra de 5.000.000 como estimación.

**Lo que puede mejorar (y cómo corregirlo):**
- En la pregunta 4 dice cuántas comparaciones cuesta una búsqueda, pero no compara cuánto costaría llenar el árbol degenerado con las 400.000 inserciones frente al equilibrado.
  → *Cómo corregirlo:* piense cuántas comparaciones hace cada inserción según la altura que ya tiene el árbol, y súmelas para ambos casos.
- En la pregunta 5, la estimación de la lista es una multiplicación por 100 con una frase de justificación muy breve, y la de la tabla se apoya en que "sigue plana" sin discutir qué pasa a esa escala (memoria, caché).
  → *Cómo corregirlo:* explique por qué la forma de la curva medida permite extender el valor, y qué factores podrían alejar la tabla de lo plano con tantos envíos.

## 2. Calidad de la explicación teórica (20 / 20)
**Lo que hizo bien:**
- Justifica el `Θ(n)` de la lista y el `Θ(1 + α)` de la tabla, nombra el supuesto de hash uniforme simple y explica que, si todo cae en una casilla, la tabla se vuelve una lista con costo `Θ(n)`.

## 3. Corrección de la implementación (23 / 25)
**Lo que hizo bien:**
- Lista y tabla devuelven el estado correcto en búsquedas exitosas e infructuosas; la colisión forzada con `m = 7` cae en la casilla 3 con longitud 3; `factor_carga()` da `3/7`.
- La tabla reutiliza `ListaEnlazada`, sin `dict`, `set` ni `hash()` en `estructuras.py`; la búsqueda es iterativa.
- Las pruebas comparan lista y tabla en 30 colecciones aleatorias, con guías existentes e inexistentes.

**Lo que puede mejorar (y cómo corregirlo):**
- En `medicion.py`, la función `_estado_de` y las dos de graficar (`_graficar_lista_vs_tabla`, `_graficar_tiempo_vs_alfa`) tienen docstring sin las secciones `Args` y `Returns`.
  → *Cómo corregirlo:* complete cada docstring con las secciones `Args:` y `Returns:` (o solo `Args:` si la función no devuelve nada), como hizo en las demás funciones.

## 4. Calidad del análisis de las gráficas (24 / 25)
**Lo que hizo bien:**
- Ambas gráficas existen, con título, ejes rotulados y leyenda; la primera tiene seis valores de `n` con las dos curvas en los mismos ejes y la segunda cuatro valores de `α`.
- Calcula factores de crecimiento (5.000 a 20.000: el tiempo de la lista se multiplica por cerca de 3,75) y los compara con `Θ(n)`; en la segunda, compara 1 a 4 y 1 a 10 con lo que predice `1 + α`. Los valores que cita coinciden con lo que se lee en las gráficas.
- Reconoce que el punto `α = 0,5` queda por encima de `α = 1` y lo atribuye al ruido de la medición.

**Lo que puede mejorar (y cómo corregirlo):**
- El informe dice "Siete valores de `n`" pero se midieron seis.
  → *Cómo corregirlo:* corrija el número para que coincida con la tabla y la gráfica.

## 5. Documentación y organización del informe (9 / 10)
**Lo que hizo bien:**
- El laboratorio está en `laboratorios/lab3-estructuras-datos/`, con todos los archivos pedidos y las gráficas visibles en el informe con ruta relativa.
- Incluye su nombre, instrucciones de reproducción, enlaces al código en cada parte y cuatro commits con mensajes descriptivos.

**Lo que puede mejorar (y cómo corregirlo):**
- El informe dice "siete valores de `n`" pero se midieron seis, así que el texto no coincide con la tabla.
  → *Cómo corregirlo:* relea el informe contra las tablas y gráficas antes de entregar.

## ¿El código funciona?
Sí. Las pruebas pasan y la medición corre completa y regenera las dos gráficas sin errores. Las estructuras responden bien en los casos revisados.
