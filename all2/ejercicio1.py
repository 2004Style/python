#!/usr/local/bin/python
# coding: latin-1

def validar_numero(numero):
    return 25 <= numero <= 91

def contar_impares(numeros):
    return sum(1 for num in numeros if num % 2 != 0)

while True:
    numeros = []
    for i in range(3):
        while True:
            try:
                numero = int(input(f"Ingrese el n�mero {i + 1} entre 25 y 91: "))
                if validar_numero(numero):
                    numeros.append(numero)
                    break
                else:
                    print("El n�mero no est� en el rango v�lido (25-91). Int�ntelo nuevamente.")
            except ValueError:
                print("Entrada no v�lida. Ingrese un n�mero entero.")

    num_impares = contar_impares(numeros)

    if num_impares == 3:
        print("Ganador")
        break
    elif num_impares == 0:
        print("Perdio")
        break
    else:
        print("Debe ingresar 3 nuevos numeros.")