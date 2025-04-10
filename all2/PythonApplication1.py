#!/usr/local/bin/python
# coding: latin-1

def suma(lista, indice=0, total=0):
    if indice == len(lista):
        return total
    total += lista[indice]
    for _ in lista:
        return suma(lista, indice + 1, total)

numeros = [1, 2, 3, 4, 5]
resultado = suma(numeros)
print(f"La suma de la lista es: {resultado}")