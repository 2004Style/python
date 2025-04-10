#!/usr/local/bin/python
# coding: latin-1
import random


def GenerarCordenadas(Npares):
    coordenadas = []
    for _ in range(Npares):
        x = random.randint(-95, 95)
        y = random.randint(-95, 95)
        coordenadas.append((x, y))
    return coordenadas


def DistanciaAlOrigen(coordenada):
    return (coordenada[0] ** 2 + coordenada[1] ** 2) ** 0.5


def EcordenadaLejana(coordenadas):
    coordenadas_positivas_negativas = [
        (x, y) for x, y in coordenadas if x > 0 and y < 0
    ]
    if not coordenadas_positivas_negativas:
        return None
    return max(coordenadas_positivas_negativas, key=DistanciaAlOrigen)


Npares = int(input("Ingrese la cantidad de pares de coordenadas: "))
coordenadas = GenerarCordenadas(Npares)

print("Estas son todas las coordenadas generadas: ")
print(f"================")
print(f"|| x   || y   ||")
print(f"================")
for x, y in coordenadas:
    print(f"|| {x}  ||  {y} ||")
print(f"================")

CmasLejana = EcordenadaLejana(coordenadas)
if CmasLejana:
    print(f"La coordenada mas alejada con X positivo e Y negativo es: {CmasLejana}")
else:
    print("No hay coordenadas que cumplan con los criterios.")
