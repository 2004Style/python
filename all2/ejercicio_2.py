#!/usr/local/bin/python
# coding: latin-1


#2. Ordenar los 100 primeros números impares de unrango ingresado por teclado.

inicio = int(input("Ingrese el número de inicio del rango: "))
fin = int(input("Ingrese el número de fin del rango: "))

numeros_impares = [numero for numero in range(inicio, fin + 1) if numero % 2 != 0][:100]

numeros_impares.sort()

print("Los 100 primeros números impares en el rango especificado, ordenados:")
print(numeros_impares)
