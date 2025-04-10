def holamundo():
    print ('hola mundo')

holamundo()

nombre = 'ronald'
edad = 20
altura = 1.75

print (nombre, edad, altura)
print(type(nombre),type(edad),type(altura))

num1 = int(input("ingrese el numero 1 -> "))
num2 = int(input("ingrese el numero 2 -> "))
suma = num1 + num2

print(f"la suma es {suma}")


def suma(num1, num2):
    suma = num1 + num2
    print(f"la suma es {suma}")


num1 = int(input("ingrese el numero 1 -> "))
num2 = int(input("ingrese el numero 2 -> "))
suma(num1, num2)

# condicionales con python
num1 = int(input("igrese el numero 1: "))
if num1 < 10:
    potencia = num1**2
    # potencia es igual a num1 por num1
else:
    potencia = num1**3
    # potencia es igual a num1 por num1 por num1
print(f"la potecia es: {potencia}")

# bucle for
num1 = int(input("ingrese el numero base"))
num2 = int(input("ingrese el numero tope"))


for i in range(num1, num2 + 1):
    print(i)


# funciones
def potencia(base, exponente):
    if exponente % 2 == 0:
        print("el exponente es par")
    else:
        print("el ecponente es impar")
    potencia = 1
    for i in range(exponente):
        potencia = potencia * base
    print(f"el resultado de la potencia es: {potencia}")


potencia(5, 3)

# funciones lambda nivel basico
# funcion tradicional
# funcion que me devuelve el cuadrado de un numero


def funcioncuadrado(num1):
    return num1**2


print(f"el resultado es {funcioncuadrado(4)}")


# ejercicio: si es menor a 10 elevar el numero al cuadrado caso contrario elevar al cubo
def potenciacion(num1):
    if num1 < 10:
        return num1**2
    else:
        return num1**3


print(f"el resultado es: {potenciacion(20)}")
