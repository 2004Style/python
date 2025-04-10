nt1 = int(input("Ingrese la primera nota: "))
nt2 = int(input("Ingrese la segunda nota: "))
nt3 = int(input("Ingrese la tercera nota: "))
promedio = (nt1 + nt2 + nt3) // 3

print(f"El promedio de las tres notas es: {promedio}")

D = 0
if D > 0:
    print(f"el numero {D} es mayor a 0")
elif D < 0:
    print(f"el numero {D} no es mayor a 0")
else:    
    print(f"el numero {D} es igual a 0")
    
count = 0
while count < 10:
    print(f"el contador es: {count}")
    count += 1
    
frutas = ["manzana", "pera", "fresa"]
for fruta in frutas:
    print(f"me gusta {fruta}")
    
for i in range(20):
    print(f"Numero: {i}")
    
for idx, fruta in enumerate(frutas):
    print(f"indice: {idx} fruta{fruta}")
    
for i in range(3):
    for j in range(2):
        print(f"i: {i} j:{j}")
        
for i in range(12):
    if i == 5:
        break
    if i % 2 == 0:
        continue
    print(f"numero: {i}")