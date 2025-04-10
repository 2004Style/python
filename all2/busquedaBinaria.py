#!/usr/local/bin/python
# coding: latin-1

#1. Encontrar el valor indicado por el usuario de unalista de números generada aleatoriamente.

import random

lista = sorted([random.randint(1, 1000) for _ in range(100)])

valor_a_buscar = int(input("Ingrese el valor que desea buscar en la lista: "))

def busqueda_binaria(lista, valor):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == valor:
            return medio 
        elif lista[medio] < valor:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1 

resultado = busqueda_binaria(lista, valor_a_buscar)

if resultado != -1:
    print(f"El valor {valor_a_buscar} se encuentra en la posición {resultado} de la lista.")
else:
    print(f"El valor {valor_a_buscar} no se encuentra en la lista.")
