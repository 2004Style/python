#!/usr/local/bin/python
# coding: latin-1

class PuestoDeTrabajo:
    def __init__(self, codigo, descripcion, area_solicitante, sueldo):
        self.codigo = codigo
        self.descripcion = descripcion
        self.area_solicitante = area_solicitante
        self.sueldo = sueldo

    def agregar_puesto(self, puestos):
        codigo = int(input("\nIngrese el codigo del puesto: "))
        descripcion = input("Ingrese la descripcion del puesto: ")
        area_solicitante = input("Ingrese el area solicitante: ")
        sueldo = float(input("Ingrese el sueldo del puesto: "))

        for puesto in puestos:
            if puesto.codigo == codigo or puesto.descripcion == descripcion or puesto.area_solicitante == area_solicitante:
                print("\nYa existe un puesto con el mismo codigo, descripcion o area solicitante.")
                return

        nuevo_puesto = PuestoDeTrabajo(codigo, descripcion, area_solicitante, sueldo)
        puestos.append(nuevo_puesto)
        print("\nPuesto de trabajo agregado con exito.")

    def mostrar_todo(self, puestos):
        if not puestos:
            print("\nNo hay puestos de trabajo registrados.")
        else:
            puestos.sort(key=lambda x: x.sueldo)

            print("\nListado de Puestos de Trabajo:")
            for puesto in puestos:
                print(f"Codigo: {puesto.codigo}, Descripcion: {puesto.descripcion}, Area Solicitante: {puesto.area_solicitante}, Sueldo: {puesto.sueldo}")

    def borrar_puesto(self, puestos):
        codigo_a_borrar = int(input("Ingrese el codigo del puesto a borrar: "))

        puestos.sort(key=lambda x: x.codigo)

        for puesto in puestos:
            if puesto.codigo == codigo_a_borrar:
                puestos.remove(puesto)
                print("\nPuesto de trabajo eliminado con exito.")
                return

        print("\nNo se encontro un puesto de trabajo con ese codigo.")

    def buscar(self, puestos):
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
            print("\nPuestos de trabajo encontrados:")
            self.mostrar_todo(resultados)
        else:
            print("\nNo se encontraron puestos de trabajo con ese sueldo.")

    def lista_mas_valiosa(self, puestos):
        monto_a_cubrir = float(input("\nIngrese el monto a invertir en salarios: "))

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
            print("\nPuestos contratados para cubrir el monto:")
            self.mostrar_todo(contratados)
        else:
            print("\nNo se pudieron contratar puestos para cubrir el monto especificado.")

def main():
    puestos = []
    puesto = PuestoDeTrabajo(0, '', '', 0)

    while True:
        print("\n\t=============Menu=============")
        print("\t0 >> Salir")
        print("\t1 >> Agregar Puesto de Trabajo")
        print("\t2 >> Mostrar Todos los Puestos")
        print("\t3 >> Borrar Puesto de Trabajo")
        print("\t4 >> Buscar por Sueldo")
        print("\t5 >> Lista Mas Valiosa")
        print("\t==============================")

        opcion = input("\tElija una opcion: ")
        if opcion == "0":
            print("Saliendo...")
            break
        elif opcion == "1":
            puesto.agregar_puesto(puestos)
        elif opcion == "2":
            puesto.mostrar_todo(puestos)
        elif opcion == "3":
            puesto.borrar_puesto(puestos)
        elif opcion == "4":
            puesto.buscar(puestos)
        elif opcion == "5":
            puesto.lista_mas_valiosa(puestos)
        else:
            print("\n\tPor favor ingrese una opcion valida!\n\tEjecutando menu nuevamente...\n")

main()