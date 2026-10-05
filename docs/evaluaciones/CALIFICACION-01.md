# Retroalimentación — Laboratorio 1: Fundamentos, complejidad y recurrencias

**Estudiante:** Juan David Machado Mosquera · **Laboratorio:** Plataforma Tamiza — fundamentos, complejidad y recurrencias
**Fecha límite:** 2026-10-04 23:59 · **Versión revisada:** commit `67900fd`

Muy buen trabajo: el informe está completo y sus afirmaciones se apoyan en sus propias mediciones.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 21 / 25 |
| Calidad de la explicación teórica | 21 / 25 |
| Corrección de la implementación | 14 / 20 |
| Calidad del análisis de las gráficas | 17 / 20 |
| Documentación y organización del informe | 9 / 10 |
| **Total** | **82 / 100** |
| **Nota (0–5)** | **4.10** |

## 1. Corrección conceptual (21 / 25)
**Lo que hizo bien:**
- Distingue bien entre algoritmo correcto y viable, y nombra la ventana de cuatro horas como la restricción que se incumple.
- Explica por qué duplicar la velocidad del servidor no basta: el trabajo crece al cuadrado.
- Da un segundo ejemplo propio (la ferretería) con cantidad de datos y límite de tiempo.
- Relaciona el tiempo de ejecución con la energía gastada cada madrugada durante años y nombra quién asume el costo de cada perjuicio.

**Lo que puede mejorar:**
- En el ejemplo de la ferretería, los tiempos que cuenta (800 ms a 1,2 s con 1.500 productos) no concuerdan con lo que usted mismo midió en el laboratorio. Use cifras que pueda respaldar.
- En la Parte 2 mezcla los escenarios: dice que el escenario C deja la lista incompleta y que los de la cola son de menor riesgo pero críticos, lo cual confunde. Explique con claridad qué paciente sale perjudicado en cada caso.
- La energía se menciona, pero sin una estimación aproximada (horas extra, kWh).

## 2. Calidad de la explicación teórica (21 / 25)
**Lo que hizo bien:**
- Define peor, mejor y promedio indicando sobre qué se toma cada uno, justifica usar el peor caso y deja la predicción antes del experimento.
- Plantea `T(n) = 2T(n/2) + Θ(n)`, explica cada término y la resuelve con el método maestro verificando la condición del caso 2.
- Incluye la tabla de complejidades.

**Lo que puede mejorar:**
- El conteo de insertion sort línea a línea es incompleto: no asigna un costo a cada línea ni suma esos costos para llegar a la cota. La tabla da solo los totales.
- La línea de la comparación y la del desplazamiento se tratan casi como la misma; explique por qué difieren en una unidad.

## 3. Corrección de la implementación (14 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien, no cambian la lista recibida y cuentan solo comparaciones entre elementos. Merge sort tiene su propia mezcla recursiva.
- Los generadores usan semilla y entregan valores distintos del tamaño pedido.

**Lo que puede mejorar:**
- `generar_casi_ordenado` usa `sort` de Python para armar el 98 % ordenado. La regla era no usar funciones de ordenamiento de la librería; hágalo sin ellas (por ejemplo, con su propio algoritmo).
- La documentación de `datos.py` dice que los valores van de 0 a 999, pero el código genera valores mucho más grandes (hasta cerca de n al cuadrado).
- Faltan *docstrings* estilo Google en varias funciones (`main`, `_graficar`, `_mezclar`, `_merge_sort_recursivo`) y *type hints* en los parámetros de algoritmo/generador de los scripts de medición.
- Hay dos pequeños avisos de estilo PEP 8 en `algoritmos.py` (espacios en las rebanadas).

## 4. Calidad del análisis de las gráficas (17 / 20)
**Lo que hizo bien:**
- Las tres gráficas tienen título, ejes con unidades y leyenda, y muestran las curvas pedidas en los mismos ejes.
- Identifica con datos el peor caso (C), el mejor (B) y el promedio (A), y contrasta con su predicción.
- El concepto técnico recomienda merge sort, responde sobre el servidor con un dato medido, estima la ventana de cuatro horas diciendo que es una estimación y discute la memoria extra.

**Lo que puede mejorar:**
- Hay cifras que no cuadran: dice que de 800 a 1.600 el tiempo crece 5 veces y a la vez que el trabajo se multiplica por cuatro; y llama "consistente con cuadrático" a un factor de 15 sin explicar la diferencia con 16.
- Para ver mejor la forma de merge sort, una escala logarítmica o un segundo gráfico ayudaría, porque en la actual parece una línea plana.

## 5. Documentación y organización del informe (9 / 10)
**Lo que hizo bien:**
- Siguió la estructura de carpetas acordada, con todos los archivos y gráficas pedidos, gráficas visibles en el informe y enlaces al código en cada parte.
- Incluye instrucciones para reproducir y cinco commits con mensajes descriptivos.

**Lo que puede mejorar:**
- Los cinco commits se hicieron en pocos minutos; conviene ir subiendo el avance poco a poco.
- Hay erratas (por ejemplo "mesureado").

## ¿El código funciona?
Sí. Los scripts corren sin errores, ambos algoritmos ordenan correctamente y se generan las tres gráficas.

## Para el próximo laboratorio
- Evite funciones de ordenamiento de Python en cualquier parte del código, incluidos los generadores de datos.
- Agregue *docstring* y *type hints* a todas las funciones, también las auxiliares.
- Desarrolle los cálculos línea a línea con el costo de cada línea y la suma final.
- Revise que las cifras citadas coincidan entre secciones y con sus mediciones.
- Haga commits pequeños a lo largo del trabajo.
