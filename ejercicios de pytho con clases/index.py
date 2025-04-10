# importamos la clase que hemos creado
from clase01 import Calculator

# almacenamos en una variable la clase
cal = Calculator()

# creamos dos veriables para almacenar los numeros
num1 = 10
num2 = 5

# usamos el metodo de suma
print(cal.suma(num1, num2))

# usamos el metodo de resta
print(cal.resta(num1, num2))

# usamos el metodo de multiplicacion
print(cal.multiplicacion(num1, num2))

# usamos el metodo de divicion
print(cal.divicion(num1, num2))
