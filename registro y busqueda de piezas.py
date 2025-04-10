piezas_vehiculos = {}

marcas = [
    "Toyota",
    "Honda",
    "Ford",
    "Chevrolet",
    "Nissan",
    "Volkswagen",
    "Hyundai",
    "BMW",
    "Mercedes-Benz",
    "Audi",
]

for marca in marcas:
    piezas = [
        "Batería",
        "Frenos",
        "Aceite del motor",
        "Filtro de aire",
        "Neumáticos",
        "Suspensión",
        "Luces",
        "Alternador",
        "Radiador",
        "Embrague",
        "Transmisión",
        "Escape",
        "Arranque",
        "Correa de distribución",
        "Amortiguadores",
        "Parabrisas",
        "Espejos",
        "Radiador",
        "Sensor de oxígeno",
        "Aceite de transmisión",
    ]
    cantidades = [
        10,
        20,
        15,
        30,
        25,
        18,
        12,
        22,
        8,
        35,
        5,
        17,
        9,
        7,
        11,
        13,
        6,
        16,
        14,
        19,
    ]

    piezas_disponibles = {}
    for i in range(len(piezas)):
        piezas_disponibles[piezas[i]] = cantidades[i]

    piezas_vehiculos[marca] = piezas_disponibles


def registrar_pieza():
    marca = input("\n\nIngrese la marca del vehículo: ")
    pieza = input("Ingrese el nombre de la pieza: ")
    cantidad = int(input("Ingrese la cantidad de piezas disponibles: "))

    if marca in piezas_vehiculos:
        if pieza in piezas_vehiculos[marca]:
            piezas_vehiculos[marca][pieza] += cantidad
        else:
            piezas_vehiculos[marca][pieza] = cantidad
    else:
        piezas_vehiculos[marca] = {pieza: cantidad}


def buscar_piezas():
    marca = input("\n\nIngrese la marca del vehículo para buscar piezas disponibles: ")

    if marca in piezas_vehiculos:
        piezas_disponibles = piezas_vehiculos[marca]
        print(f"\n\nPiezas disponibles para la marca {marca}:")
        for pieza, cantidad in piezas_disponibles.items():
            print(f"{pieza}: {cantidad} unidades disponibles")
        print("\n\n")
    else:
        print(f"No se encontraron piezas disponibles para la marca {marca}.\n\n")


while True:
    print("1. Registrar pieza")
    print("2. Buscar piezas disponibles por marca")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_pieza()
    elif opcion == "2":
        buscar_piezas()
    elif opcion == "3":
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida.")