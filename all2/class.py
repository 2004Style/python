class Perro:

  def __init__(self, nombre, color, edad):
    self._nombre = nombre
    self._color = color
    self._edad = edad

  def ladrar(self):
    print("Guau")

  def sumar(self,a,b):
    return a+b

class

p1 = Perro("fido", "marron", 5)
p1.ladrar()
tot = p1.sumar(2,3)
print(f"suma es {tot}")