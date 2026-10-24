# Retroalimentación — Laboratorio 2: Dividir y vencer

**Estudiante:** Juan David Machado Mosquera · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-21 23:59 · **Versión revisada:** commit `b0799e1`

Excelente trabajo: un laboratorio completo, correcto y bien sustentado con sus propios datos.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 18 / 20 |
| Calidad de la explicación teórica | 18 / 20 |
| Corrección de la implementación | 25 / 25 |
| Calidad del análisis de las gráficas | 22 / 25 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **93 / 100** |
| **Nota (0–5)** | **4.65** |

## 1. Corrección conceptual (18 / 20)
**Lo que hizo bien:**
- Identifica que divide y vencerás empieza a ganar desde n = 50 y explica por qué la fuerza bruta gana en n = 10 (constante pequeña).
- En la comparación con el máximo de un arreglo, justifica con el costo de combinar (trivial) y la recurrencia `T(n) = 2T(n/2) + Θ(1)`.
- La recomendación para la gerente es clara y la estimación a 1.000.000 de registros está declarada como estimación, escalando cada algoritmo por su propio orden.

**Lo que puede mejorar:**
- En la pregunta 4 dice "caso 1" pero no comprueba la condición (que `Θ(1)` es menor que `n^1`).
- Las estimaciones (11 segundos y 39 horas) parten de una sola medición; convendría decir que son un orden de magnitud aproximado.

## 2. Calidad de la explicación teórica (18 / 20)
**Lo que hizo bien:**
- Explica de dónde sale cada término: dos subproblemas de tamaño `n/2` y un caso cruzado de costo lineal.
- Resuelve con el método maestro (a = 2, b = 2, caso 2) y obtiene `Θ(n log n)`.
- Justifica el `Θ(n²)` de la fuerza bruta con la suma `n(n+1)/2`.

**Lo que puede mejorar:**
- Al aplicar el método maestro, escriba explícitamente por qué `f(n) = Θ(n)` coincide con `n^(log_b a)`, y no solo afirmarlo.

## 3. Corrección de la implementación (25 / 25)
**Lo que hizo bien:**
- Las tres funciones dan la suma correcta en todos los casos pedidos y coinciden en listas aleatorias (usted probó 30).
- `subarreglo_maximo` resuelve los tres casos sin llamar a la fuerza bruta y ninguna función modifica la lista.
- El código tiene buen estilo, *type hints* y *docstrings* en cada función.

## 4. Calidad del análisis de las gráficas (22 / 25)
**Lo que hizo bien:**
- La gráfica tiene título, ejes rotulados, leyenda y ambas curvas en los mismos ejes, con 7 tamaños.
- Los valores del informe (por ejemplo, unos 8900 ms para la fuerza bruta en n = 8000) coinciden con lo que muestra la gráfica.
- Calcula el factor al duplicar n (4.15× para la fuerza bruta) y lo contrasta con la teoría. La gráfica log-log y la tabla ayudan mucho.

**Lo que puede mejorar:**
- Para divide y vencerás obtuvo 1.78× frente a 2.17× esperado y lo atribuyó al ruido sin comprobarlo. Con más repeticiones o con otro par de tamaños habría podido sustentarlo.
- Apóyese también en lo que se lee en la gráfica, no solo en la tabla.

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- El README sigue el orden pedido, trae instrucciones de reproducción, enlaces al código y las imágenes se ven.
- Tiene tres commits descriptivos del laboratorio.
- La carpeta `laboratorios/lab2-divide-y-vencer/` está en una ubicación válida.

## ¿El código funciona?
Sí. Las pruebas pasan, la medición corre completa y genera las dos gráficas.

## Para el próximo laboratorio
- Compruebe siempre la condición del caso del método maestro que aplique, en cada recurrencia.
- Si un resultado medido se aparta de la teoría, verifíquelo con más repeticiones en vez de solo atribuirlo al ruido.
- Cite en el análisis valores leídos directamente de la gráfica.
- Presente las estimaciones como un rango aproximado, indicando su margen de error.
