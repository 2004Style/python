#!/usr/local/bin/python
# coding: latin-1

def factura():
    Tvebtasmayor300 = 0
    Tventas = 0
    MAXFrutasVendidas = 0
    VdFrutas = 0
    Rfacturas = 0

    while True:
        Gfactura = input("¿Desea generar una factura? (si/no): ")
        
        if Gfactura.lower() == "no":
            break
        
        Cliente = input("\nIngrese el nombre del cliente: ")
        NroDFrutas = int(input("Ingrese cuántos tipos de frutas desea comprar: "))
        
        Rfacturas += 1
        FacturaTot = 0
        FDFVendidas = 0
        
        for _ in range(NroDFrutas):
            NombreDF = input("Ingrese el nombre de la fruta: ")
            cantidad = int(input("Ingrese la cantidad de frutas a vender: "))
            PrecuiU = float(input("Ingrese el precio unitario en soles: "))
            
            subtotal = cantidad * PrecuiU
            FacturaTot += subtotal
            FDFVendidas += cantidad
        
        Tventas += FacturaTot
        
        if FacturaTot >= 300:
            Tvebtasmayor300 += 1
        
        if FDFVendidas > MAXFrutasVendidas:
            MAXFrutasVendidas = FDFVendidas
        
        if NroDFrutas == 1:
            VdFrutas += 1
        
        print(f"\nResumen de la factura:\nCliente: {Cliente}\nTotal en soles vendido: S/.{FacturaTot}\nTipos de frutas: {NroDFrutas}\n")
    
    if Rfacturas > 0:
        promedio_ventas = Tventas / Rfacturas
        print(f"\nCantidad de facturas con un monto de venta mayor igual a S/300: {Tvebtasmayor300}\nPromedio de ventas de las facturas en soles: {promedio_ventas}\nMáxima cantidad de frutas vendidas en una factura: {MAXFrutasVendidas}\nCantidad de facturas con un solo tipo de frutas: {VdFrutas}")
    else:
        print("No se ingresaron facturas.")

factura()