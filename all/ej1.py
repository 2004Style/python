#!/usr/local/bin/python
# coding: latin-1

class puestosdetrabajo:
    def __init__(self, codigo, descripcion, era, sueldo):
        self.codigo = codigo
        self.descripcion = descripcion
        self.era = era
        self.sueldo = sueldo

def agregar(puestos):
    codigo = int(input("Ingrese el código del puesto: "))
    descripcion = input("Ingrese la descripción del puesto: ")
    era = input("Ingrese el área solicitante: ")
    sueldo = float(input("Ingrese el sueldo del puesto: "))
    
    for puesto in puestos:
        if puesto.codigo == codigo or puesto.descripcion == descripcion or puesto.era == era:
            print("Ya existe un puesto con el mismo código, descripción o área solicitante.")
            return
    
    nuevo_puesto = puestosdetrabajo(codigo, descripcion, era, sueldo)
    puestos.append(nuevo_puesto)
    print("Puesto de trabajo agregado.")

def mostrar(puestos):
    for puesto in puestos:
        print(f"Código: {puesto.codigo}, Descripción: {puesto.descripcion}, Área Solicitante: {puesto.era}, Sueldo: {puesto.sueldo}")

def borrar(puestos):
    codigo_a_borrar = int(input("Ingrese el código del puesto a borrar: "))
    
    puestos.sort(key=lambda x: x.codigo)
    
    for puesto in puestos:
        if puesto.codigo == codigo_a_borrar:
            puestos.remove(puesto)
            print("Puesto de trabajo eliminado.")
            return
    
    print("No se encontró un puesto de trabajo con ese código.")

def buscar(puestos):
    sueldo_a_buscar = float(input("Ingrese el sueldo a buscar: "))
    
    puestos.sort(key=lambda x: x.sueldo, reverse=True)
    
    resultados = []
    
    left, right = 0, len(puestos) - 1
    while left <= right:
        mid = (left + right) // 2
        if puestos[mid].sueldo == sueldo_a_buscar:
            resultados.append(puestos[mid])
            left = mid + 1
        elif puestos[mid].sueldo < sueldo_a_buscar:
            right = mid - 1
        else:
            left = mid + 1
    
    if resultados:
        print("Puestos de trabajo encontrados:")
        mostrar(resultados)
    else:
        print("No se encontraron puestos de trabajo con ese sueldo.")

def listavaliosa(puestos):
    monto_a_cubrir = float(input("Ingrese el monto a invertir en salarios: "))
    
    n = len(puestos)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if puestos[j].sueldo < puestos[j + 1].sueldo:
                puestos[j], puestos[j + 1] = puestos[j + 1], puestos[j]
    
    suma_salarios = 0
    contratados = []
    
    for puesto in puestos:
        if suma_salarios + puesto.sueldo <= monto_a_cubrir:
            contratados.append(puesto)
            suma_salarios += puesto.sueldo
        else:
            break
    
    if contratados:
        print("Puestos contratados para cubrir el monto:")
        mostrar(contratados)
    else:
        print("No se pudieron contratar puestos para cubrir el monto especificado.")

def main():
    puestos = []
    
    while True:
        print("Menú:")
        print("1 - Agregar Puesto de Trabajo")
        print("2 - Mostrar Todos los Puestos")
        print("3 - Borrar Puesto de Trabajo")
        print("4 - Buscar por Sueldo")
        print("5 - Lista Más Valiosa")
        print("6 - Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar(puestos)
        elif opcion == "2":
            mostrar(puestos)
        elif opcion == "3":
            borrar(puestos)
        elif opcion == "4":
            buscar(puestos)
        elif opcion == "5":
            listavaliosa(puestos)
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

main()