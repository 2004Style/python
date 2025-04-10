def prueba(a,b):
    y = ((a+b)/(5*b))**2
    print(f"el valor es: {y}")

prueba(100,5)

def increment(i):
    
    while i<20:
        i=i+1
        print(i)

increment(17)

def hola(name, edad):
    print(f'hola {name} tu edad es: {edad}')

hola('ruben', 20)


def suma(a,b):
    y=a+b
    print(y)

a = int(input('ingresa el primer numero: '))
b = int(input('ingresa el segundo numero: '))
suma(a,b)