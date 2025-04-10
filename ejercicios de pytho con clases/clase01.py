class Calculator:
    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b

    def multiplicacion(self, a, b):
        return a * b

    def divicion(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    def ej1(self, a, b):
        return 0;
