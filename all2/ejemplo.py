#!/usr/local/bin/python
# coding: latin-1

def dar_cambio(monto, moneda):
    cambio = [0] * len(moneda)

    for i in range(len(moneda)):
        while monto >= moneda[i]:
            monto -= moneda[i]
            cambio[i] += 1

    return cambio

def main():
    moneda = [200, 100, 50, 20, 10, 5, 2, 1]

    monto = int(input("Ingrese el monto a pagar: "))

    cambio = dar_cambio(monto, moneda)

    for i in range(len(moneda)):
        if cambio[i] > 0:
            print(f"Monedas de S/.{moneda[i]}: {cambio[i]}")
main()
