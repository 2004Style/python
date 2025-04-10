#!/usr/local/bin/python
# coding: latin-1

def ImprimilrL(lab):
    for fila in lab:
        print(" ".join(map(str, fila)))

def ResolverL(lab, fila, columna, PuntajeA, CaminoA):
    if (
        fila < 0
        or fila >= len(lab)
        or columna < 0
        or columna >= len(lab[0])
        or lab[fila][columna] == 0
    ):
        return

    PuntajeA += lab[fila][columna]
    CaminoA.append((fila, columna))

    if fila == 0 and columna == 0:
        if PuntajeA >= 23:
            print("laberinto resuelto exitosamente: ")
            ImprimilrL(lab)
            print("mostrando camino a seguir...")
            for paso in CaminoA:
                print(paso)
        return

    lab[fila][columna] = 0

    ResolverL(lab, fila - 1, columna, PuntajeA, CaminoA)
    ResolverL(lab, fila, columna + 1, PuntajeA, CaminoA)
    ResolverL(lab, fila + 1, columna, PuntajeA, CaminoA)
    ResolverL(lab, fila, columna - 1, PuntajeA, CaminoA)

    lab[fila][columna] = 1
    CaminoA.pop()


if __name__ == "__main__":
    lab = [
        [4, 1, 1, 3, 0, 1, 1, 1, 4],
        [3, 0, 0, 1, 0, 1, 0, 0, 1],
        [1, 1, 0, 1, 1, 1, 1, 0, 1],
        [0, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 3, 1, 1],
        [3, 0, 1, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 3, 1, 1, 1, 1],
        [1, 0, 0, 1, 0, 1, 0, 0, 4],
        [1, 1, 3, 1, 0, 1, 1, 1, 1],
    ]

    ResolverL(lab, len(lab) - 1, 0, 0, [])

    print("No se allo un camino viable.")