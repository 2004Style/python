import random

def contar_cinco_cifras_recursivo(lista, indice):
    if indice == len(lista):
        return 0
    else:
        if 10000 <= lista[indice] <= 99999:
            return 1 + contar_cinco_cifras_recursivo(lista, indice + 1)
        else: elemento
            return contar_cinco_cifras_recursivo(lista, indice + 1)

tamaño = int(input("Ingresa el tamaño de la lista de los números: "))

lista_numeros = [random.randint(100, 999999) for _ in range(tamaño)]
print("Lista de los números que se han generado:", lista_numeros)

contador_cinco_cifras = contar_cinco_cifras_recursivo(lista_numeros, 0)

print(f"En la lista existen {contador_cinco_cifras} números con 5 cifras.")