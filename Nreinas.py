def verificacion(tablero, fila, columna):
    # SE VERIFICA SI COLOCAR O NO LA REINA EN LA POSICIÓN
    # SE VERIFICA LA FILA ACTUAL
    for i in range(columna):
        if tablero[fila][i] == 1:
            return False
    
    # SE VERIFICA LA DIAGONAL SUPERIOR IZQUIERDA
    for i, j in zip(range(fila, -1, -1), range(columna, -1, -1)):
        if tablero[i][j] == 1:
            return False
    
    # SE VERIFICA LA DIAGONAL INFERIOR IZQUIERDA
    for i, j in zip(range(fila, len(tablero), 1), range(columna, -1, -1)):
        if tablero[i][j] == 1:
            return False
    
    return True

def solucion(tablero, columna):
    # SOLUCIÓN
    if columna >= len(tablero):
        return True

    for i in range(len(tablero)):
        # VERIFICACIÓN DE LA COLOCACIÓN DE LA REINA
        if verificacion(tablero, i, columna):
            # Q0
            tablero[i][columna] = 1

            # Q1, Q2, Q3...................QX
            if solucion(tablero, columna + 1):
                return True

            # PROCESO BACKTRACKING
            tablero[i][columna] = 0

    # NO HAY SOLUCIÓN
    return False

def tableroX(tablero):
    for fila in tablero:
        print(' '.join(['Q' if x == 1 else '.' for x in fila]))

def main():
    n = 6  # REINAS Y TAMAÑO DEL TABLERO
    tablero = [[0] * n for _ in range(n)]

    if solucion(tablero, 0):
        print("Solución:")
        tableroX(tablero)
    else:
        print("Sin solución.")

if __name__ == "__main__":
    main()
