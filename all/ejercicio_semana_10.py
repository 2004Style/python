#!/usr/local/bin/python
# coding: latin-1
def encontrar_mayor(lista):
    if len(lista) == 1:
        return lista[0]
    
    mitad = len(lista) // 2
    mitad_izquierda = lista[:mitad]
    mitad_derecha = lista[mitad:]

    max_izquierda = encontrar_mayor(mitad_izquierda)
    max_derecha = encontrar_mayor(mitad_derecha)

    return max(max_izquierda, max_derecha)

lista_de_numeros = [3, 7, 1, 9, 5, 2, 8]
mayor = encontrar_mayor(lista_de_numeros)
print("El número mayor en la lista es:", mayor)