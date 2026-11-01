import time

def contar_soluciones(n, prohibidas=None):
    prohibidas = prohibidas or set()   # {(fila, col), ...}
    reinas = [0] * n                   # reinas[fila] = columna
    cols, diag1, diag2 = set(), set(), set()
    soluciones = []

    def bt(fila):
        if fila == n:
            soluciones.append(reinas[:])
            return
        for col in range(n):
            if (fila, col) in prohibidas:
                continue
            if col in cols or (fila - col) in diag1 or (fila + col) in diag2:
                continue
            reinas[fila] = col
            cols.add(col); diag1.add(fila - col); diag2.add(fila + col)
            bt(fila + 1)
            cols.remove(col); diag1.remove(fila - col); diag2.remove(fila + col)

    bt(0)
    return soluciones

# Bonus 2: tiempos
for n in range(4, 9):
    t = time.perf_counter()
    total = len(contar_soluciones(n))
    print(f"N={n}: {total} soluciones, {time.perf_counter() - t:.4f} s")