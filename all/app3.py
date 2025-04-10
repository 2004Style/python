#!/usr/local/bin/python
# coding: latin-1

# Solicitar las longitudes de los lados
a = int(input("ingrese el primer lado: "))
b = int(input("ingrese el segundo lado: "))
d = int(input("ingrese el tercer lado: "))

# Verificar si los valores forman un triángulo
if a + b > d and a + d > b and b + d > a:
    # Determinar el tipo de triángulo
    if a == b == d:
        tipo_triangulo = "equilátero"
    elif a == b or a == d or b == d:
        tipo_triangulo = "isósceles"
    else:
        tipo_triangulo = "escaleno"
    
    # Calcular el área del triángulo
    s = (a + b + d) / 2
    area = (s * (s - a) * (s - b) * (s - d)) ** 0.5
    
    # Mostrar resultados
    print(f"el triángulo es {tipo_triangulo}")
    print(f"su área es: {area}")
else:
    print("los valores no corresponden a un triángulo.")
    






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
        print("Voto inválido")

# Calcular el total de votos
total_votos = sum(votos.values())

# Mostrar los resultados
print("\nResultados de la elección:")
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
        print("Voto inválido")

total_votos = sum(votos.values())

print("\nResultados de la elección:")
for candidato, num_votos in votos.items():
    porcentaje = (num_votos / total_votos) * 100
    print(f"Candidato {candidato}: {num_votos} votos ({porcentaje}%)")
