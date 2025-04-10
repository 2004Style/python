
#!/usr/local/bin/python
# coding: latin-1

def imprimir_laberinto(laberinto):
    for fila in laberinto:
        print(" ".join(map(str, fila)))

def resolver_laberinto(laberinto):
    def es_valida(x, y):
        return 0 <= x < len(laberinto) and 0 <= y < len(laberinto[0]) and laberinto[x][y] != 0

    def backtracking(x, y, puntos):
        if not es_valida(x, y):
            return False

        puntos += laberinto[x][y]  # Sumar los puntos en esta celda

        if x == 0 and y == 0:
            return puntos >= 23  # Verificar si se llegó a la celda de salida con suficientes puntos

        temp = laberinto[x][y]  # Temporalmente guardar el valor actual de la celda
        laberinto[x][y] = 0  # Marcar la celda como visitada

        if backtracking(x - 1, y, puntos) or backtracking(x, y + 1, puntos) or backtracking(x + 1, y, puntos) or backtracking(x, y - 1, puntos):
            return True

        laberinto[x][y] = temp  # Restaurar el valor original de la celda
        return False

    if backtracking(len(laberinto) - 1, 0, 0):
        return True
    return False

laberinto = [
    [4, 1, 1, 3, 0, 1, 1, 1, 3],
    [3, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 3, 1, 1],
    [3, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 3, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 4],
    [1, 3, 1, 0, 1, 1, 1, 1, 1]
]

if resolver_laberinto(laberinto):
    print("¡Se encontró una solución!")
    imprimir_laberinto(laberinto)
else:
    print("No se encontró una solución con suficientes puntos.")
