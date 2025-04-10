#!/usr/local/bin/python
# coding: latin-1

# Solicitar las longitudes de los lados
a = int(input("ingrese el primer lado: "))
b = int(input("ingrese el segundo lado: "))
d = int(input("ingrese el tercer lado: "))

# Verificar si los valores forman un tri�ngulo
if a + b > d and a + d > b and b + d > a:
    # Determinar el tipo de tri�ngulo
    if a == b == d:
        tipo_triangulo = "equil�tero"
    elif a == b or a == d or b == d:
        tipo_triangulo = "is�sceles"
    else:
        tipo_triangulo = "escaleno"
    
    # Calcular el �rea del tri�ngulo
    s = (a + b + d) / 2
    area = (s * (s - a) * (s - b) * (s - d)) ** 0.5
    
    # Mostrar resultados
    print(f"el tri�ngulo es {tipo_triangulo}")
    print(f"su �rea es: {area}")
else:
    print("los valores no corresponden a un tri�ngulo.")
    






# Inicializar diccionario para contar los votos de cada candidato
votos = {1: 0, 2: 0, 3: 0, 4: 0}

# Solicitar los votos al usuario de manera desorganizada
print("Ingrese los votos de manera desorganizada (ingrese 0 para finalizar):")
while True:
    voto = int(input())
    if voto == 0:
        break
    if voto in votos:
        votos[voto] += 1
    else:
        print("Voto inv�lido")

# Calcular el total de votos
total_votos = sum(votos.values())

# Mostrar los resultados
print("\nResultados de la elecci�n:")
for candidato, num_votos in votos.items():
    porcentaje = (num_votos / total_votos) * 100
    print(f"Candidato {candidato}: {num_votos} votos ({porcentaje}%)")








votos = {1: 0, 2: 0, 3: 0, 4: 0}

print("Ingrese los votos (ingrese 0 para finalizar):")
while True:
    voto = int(input())
    if voto == 0:
        break
    if voto in votos:
        votos[voto] += 1
    else:
        print("Voto inv�lido")

total_votos = sum(votos.values())

print("\nResultados de la elecci�n:")
for candidato, num_votos in votos.items():
    porcentaje = (num_votos / total_votos) * 100
    print(f"Candidato {candidato}: {num_votos} votos ({porcentaje}%)")
