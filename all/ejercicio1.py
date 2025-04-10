#!/usr/local/bin/python
# coding: latin-1
import random

def generar_coordenadas(num_pars):
    coordenadas = []
    for _ in range(num_pars):
        x = random.randint(-95, 95)
        y = random.randint(-95, 95)
        coordenadas.append((x, y))
    return coordenadas

def distancia_al_origen(coordenada):
    return (coordenada[0]**2 + coordenada[1]**2)**0.5

def encontrar_coordenada_mas_alejada(coordenadas):
    coordenadas_positivas_negativas = [(x, y) for x, y in coordenadas if x > 0 and y < 0]
    if not coordenadas_positivas_negativas:
        return None
    return max(coordenadas_positivas_negativas, key=distancia_al_origen)

num_pars = int(input("Ingrese la cantidad de pares de coordenadas: "))
coordenadas = generar_coordenadas(num_pars)

print("Estas son todas las coordenadas generadas: ")
print(f"| x   | y   |")
print(f" ------------")
for x, y in coordenadas:
    print(f"[{x}  ;  {y}  ]")

coordenada_mas_alejada = encontrar_coordenada_mas_alejada(coordenadas)
if coordenada_mas_alejada:
    print(f"La coordenada mas alejada con X positivo e Y negativo es: {coordenada_mas_alejada}")
else:
    print("No se encontraron coordenadas que cumplan con los criterios.")
