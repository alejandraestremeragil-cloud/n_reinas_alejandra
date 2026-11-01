import time
import matplotlib.pyplot as plt


def n_reinas(n, prohibidas=None):
    """Devuelve todas las soluciones como listas: reinas[fila] = columna.
    prohibidas: set de casillas (fila, col) donde no se puede poner reina."""
    prohibidas = prohibidas or set()
    reinas = [0] * n
    cols, diag_principal, diag_secundaria = set(), set(), set()
    soluciones = []

    def backtrack(fila):
        if fila == n:
            soluciones.append(reinas[:])  # copia, no referencia
            return
        for col in range(n):
            if (fila, col) in prohibidas:
                continue
            if col in cols or (fila - col) in diag_principal or (fila + col) in diag_secundaria:
                continue
            # colocar reina
            reinas[fila] = col
            cols.add(col)
            diag_principal.add(fila - col)
            diag_secundaria.add(fila + col)
            backtrack(fila + 1)
            # retroceder
            cols.remove(col)
            diag_principal.remove(fila - col)
            diag_secundaria.remove(fila + col)

    backtrack(0)
    return soluciones


def imprimir_tablero(reinas):
    n = len(reinas)
    for fila in range(n):
        print(" ".join("Q" if reinas[fila] == c else "." for c in range(n)))
    print()


def dibujar_tablero(reinas, titulo=""):
    n = len(reinas)
    fig, ax = plt.subplots(figsize=(4, 4))
    for f in range(n):
        for c in range(n):
            color = "#eeeed2" if (f + c) % 2 == 0 else "#769656"
            ax.add_patch(plt.Rectangle((c, n - 1 - f), 1, 1, color=color))
    for f, c in enumerate(reinas):
        ax.text(c + 0.5, n - 1 - f + 0.5, "♛", ha="center", va="center", fontsize=28)
    ax.set_xlim(0, n)
    ax.set_ylim(0, n)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(titulo)
    plt.show()


if __name__ == "__main__":
    # --- Parte principal: N = 4 ---
    n = 4
    soluciones = n_reinas(n)
    print(f"Se encontraron {len(soluciones)} soluciones para N = {n}.\n")
    for idx, sol in enumerate(soluciones, 1):
        print(f"Solución {idx}:")
        imprimir_tablero(sol)

    # --- Bonus 1: casillas prohibidas ---
    prohibidas = {(0, 1), (2, 3)}
    con_restr = n_reinas(6, prohibidas)
    print(f"N = 6 con casillas prohibidas {prohibidas}: {len(con_restr)} soluciones\n")

    # --- Bonus 2: conteo y tiempos para N = 5..8 ---
    print("N | soluciones | tiempo (s)")
    for k in range(5, 9):
        inicio = time.perf_counter()
        total = len(n_reinas(k))
        print(f"{k} | {total:^10} | {time.perf_counter() - inicio:.4f}")

    # --- Bonus 3: visualización ---
    for idx, sol in enumerate(soluciones, 1):
        dibujar_tablero(sol, f"Solución {idx} (N = {n})")