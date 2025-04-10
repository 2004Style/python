# Precios de las habitaciones y otros servicios
precios = {
    'Simple': 60.00,
    'Matrimonial': 80.00,
    'Doble': 130.00,
    'Triple': 180.00,
    'Gaseosa': 1.50,
    'Vino': 25.00,
    'Chocolates': 1.50,
    'Caramelos': 0.20,
    'Agua Mineral': 2.00,
    'Almuerzo': 9.00,
    'Platos a la carta': 15.00,
    'Desayuno': 6.00,
    'Cena': 7.00,
    'Servicio Planchado Pantalón': 4.00,
    'Servicio Planchado Camisa': 5.00,
    'Servicio Lavado Pantalón': 3.00,
    'Servicio Lavado Polo': 2.50,
    'Servicio Lavado Camisa': 4.00,
}

# Movimientos de habitaciones vendidas
habitaciones_vendidas = {
    '101 Simple': 2,
    '103 Doble': 5,
    '106 Matrimonial': 2,
    '206 Simple': 10,
    '204 Triple': 1,
}

# Pedidos adicionales por habitación
pedidos_adicionales = {
    '101 Simple': {'Almuerzos': 2, 'Vinos': 2, 'Chocolates': 6, 'Serv. Planch. Pantalón': 2},
    '103 Doble': {'Caramelos': 5, 'Desayunos': 2, 'H2O Mineral': 5, 'Serv. Planch. Camisa': 1},
    '106 Matrimonial': {'Cenas': 2, 'Chocolates': 6, 'Vinos': 3, 'Serv. Lav. y Planc. Camisa': 3},
    '206 Simple': {'Caramelos': 10, 'Gaseosa': 1, 'Chocolates': 2, 'Serv. Lav. Polo': 1},
    '204 Triple': {'Chocolates': 5, 'H2O Mineral': 4, 'Serv. Lav. y Planc. Camisa': 1, 'Serv. Lav. y Planc. Pantalón': 1},
}

# Egresos
egresos = {
    'Papel Higiénico': 25.00,
    'Útiles de Limpieza': 75.00,
    'Servicios Básicos': 1850.00,
}

# Calcular ingresos por habitación y totales
ingresos_por_habitacion = {}
total_ingresos = 0.0

for habitacion, cantidad in habitaciones_vendidas.items():
    precio_habitacion = precios.get(habitacion.split()[1])
    ingresos_habitacion = cantidad * precio_habitacion
    
    for servicio, cantidad_servicio in pedidos_adicionales.get(habitacion, {}).items():
        precio_servicio = precios.get(servicio, 0)
        ingresos_habitacion += cantidad_servicio * precio_servicio

    ingresos_por_habitacion[habitacion] = ingresos_habitacion
    total_ingresos += ingresos_habitacion

# Calcular total de egresos
total_egresos = sum(egresos.values())

# Calcular arqueo de caja
fondos_fijos = 2250.00
otros_ingresos = 80.00

arqueo_de_caja = fondos_fijos + otros_ingresos + total_ingresos - total_egresos

# Imprimir resultados
print("Ingresos por habitación:")
for habitacion, ingresos in ingresos_por_habitacion.items():
    print(f"{habitacion}: S/. {ingresos:.2f}")

print(f"Total de ingresos: S/. {total_ingresos:.2f}")
print(f"Total de egresos: S/. {total_egresos:.2f}")
print(f"Arqueo de caja: S/. {arqueo_de_caja:.2f}")