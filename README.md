# N-Reinas con Backtracking
Resuelve el problema de las N-Reinas con backtracking, siguiendo el pseudocódigo del enunciado.

# ¿Qué hace?

Coloca N reinas en un tablero de N × N sin que ninguna se ataque (ni en fila, ni en columna, ni en diagonal) y encuentra todas las soluciones posibles.

Para N = 4 hay 2 soluciones:

. Q . .      . . Q .
. . . Q      Q . . .
Q . . .      . . . Q
. . Q .      . Q . .
```

# Cómo funciona

- `n_reinas(n)`: crea el tablero y devuelve la lista de soluciones.
- `resolver_n_reinas(...)`: backtracking, coloca una reina por fila y retrocede si no hay opción.
- `es_seguro(...)`: comprueba columna y diagonales.
- `imprimir_tablero(...)`: muestra el tablero (`Q` = reina, `.` = vacío).

# Cómo ejecutarlo

Requisitos: Python 3 y matplotlib.

El programa pide el tamaño N del tablero y muestra las soluciones encontradas.

# Bonus

Se ejecuta siempre al final, con N = 5, 6, 7 y 8:

- **Casillas prohibidas:** se pueden bloquear casillas (marcadas en rojo) y el algoritmo las evita.
- **Conteo y tiempos:** número de soluciones y tiempo de ejecución para cada N (10, 4, 40 y 92 soluciones sin restricciones).
- **Visualización:** dibujo del tablero con matplotlib.

## Respuestas a las preguntas del ejercicio

1. **¿Cuántas soluciones hay para 4 × 4?** 2.
2. **¿Cómo encontrar todas las soluciones para cualquier N?** El backtracking no se detiene al encontrar la primera solución: guarda una copia, retrocede y sigue probando hasta agotar todas las opciones. Como todo depende de `n`, basta con cambiar su valor.