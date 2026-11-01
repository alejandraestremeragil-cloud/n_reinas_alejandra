import time
import matplotlib.pyplot as plt


# Paso: VALIDAR la solución parcial
# Comprueba si se puede poner una reina en (fila, col)
def es_seguro(tablero, fila, col, n, prohibidas):
    # casilla prohibida
    if (fila, col) in prohibidas:
        return False

    # misma columna (miramos solo las filas de arriba)
    for i in range(fila):
        if tablero[i][col] == 1:
            return False

    # diagonal hacia arriba a la izquierda
    i = fila - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if tablero[i][j] == 1:
            return False
        i = i - 1
        j = j - 1

    # diagonal hacia arriba a la derecha
    i = fila - 1
    j = col + 1
    while i >= 0 and j < n:
        if tablero[i][j] == 1:
            return False
        i = i - 1
        j = j + 1

    return True


# Árbol de decisiones: cada fila es una decisión (en qué columna pongo la reina)
def resolver(tablero, fila, n, soluciones, prohibidas):
    # Finalizar: si hemos llegado al final, guardamos una COPIA de la solución
    if fila == n:
        copia = []
        for f in tablero:
            copia.append(f[:])
        soluciones.append(copia)
        return

    # Probamos todas las columnas de esta fila
    for col in range(n):
        if es_seguro(tablero, fila, col, n, prohibidas):
            tablero[fila][col] = 1                      # construir solución parcial
            resolver(tablero, fila + 1, n, soluciones, prohibidas)
            tablero[fila][col] = 0                      # retroceder (backtrack)


def n_reinas(n, prohibidas=[]):
    tablero = []
    for i in range(n):
        tablero.append([0] * n)
    soluciones = []
    resolver(tablero, 0, n, soluciones, prohibidas)
    return soluciones


def imprimir_tablero(tablero, prohibidas=[]):
    for f in range(len(tablero)):
        linea = ""
        for c in range(len(tablero)):
            if tablero[f][c] == 1:
                linea = linea + "Q "
            elif (f, c) in prohibidas:
                linea = linea + "X "
            else:
                linea = linea + ". "
        print(linea)
    print()


def dibujar_tablero(tablero, titulo, prohibidas=[]):
    n = len(tablero)
    fig, ax = plt.subplots()
    for f in range(n):
        for c in range(n):
            if (f, c) in prohibidas:
                color = "red"
            elif (f + c) % 2 == 0:
                color = "white"
            else:
                color = "gray"
            ax.add_patch(plt.Rectangle((c, n - 1 - f), 1, 1, color=color))
            if tablero[f][c] == 1:
                ax.text(c + 0.5, n - 1 - f + 0.5, "Q", ha="center", va="center", fontsize=20)
    ax.set_xlim(0, n)
    ax.set_ylim(0, n)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(titulo)
    plt.show()


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================
n = int(input("Tamaño del tablero N: "))

soluciones = n_reinas(n)
print("Se encontraron", len(soluciones), "soluciones para N =", n)
print()

if len(soluciones) <= 10:
    for i in range(len(soluciones)):
        print("Solución", i + 1, ":")
        imprimir_tablero(soluciones[i])
else:
    print("Son muchas, muestro solo la primera:")
    imprimir_tablero(soluciones[0])

# ==========================================
# BONUS: casillas prohibidas, N = 5, 6, 7, 8, tiempos y dibujo
# ==========================================
print("BONUS")
prohibidas = [(0, 1), (2, 3)]   # (fila, columna) donde no se puede poner reina
print("Casillas prohibidas (X):", prohibidas)
print()
print("N | sin prohibidas | con prohibidas | tiempo (s)")

for k in range(5, 9):
    inicio = time.time()
    sin = n_reinas(k)
    tiempo = time.time() - inicio

    con = n_reinas(k, prohibidas)
    print(k, "|", len(sin), "|", len(con), "|", round(tiempo, 4))

    if len(con) > 0:
        imprimir_tablero(con[0], prohibidas)
        dibujar_tablero(con[0], "N = " + str(k) + " con casillas prohibidas", prohibidas)