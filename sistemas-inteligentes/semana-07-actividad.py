import pandas as pd
from scipy.optimize import linprog

# 1. Importar datos desde el archivo CSV (con delimitador punto y coma)
df = pd.read_csv('/ventas.csv', delimiter=';')

# 2. Análisis Descriptivo
df['ganancia_por_unidad'] = df['Precio'] - df['Costo_de_Produccion']
df['ganancia_total'] = df['ganancia_por_unidad'] * df['Cantidad_Vendida']

# Mostrar estadísticas descriptivas
print("Estadísticas Descriptivas:")
print(df[['Producto', 'Precio', 'Cantidad_Vendida', 'Costo_de_Produccion', 'ganancia_por_unidad', 'ganancia_total']])

# 3. Optimización: Programación Lineal
# Coeficientes de la función objetivo (negados porque linprog minimiza)
c = -df['ganancia_total']

# Restricciones
# Supongamos que hay un límite de recursos, por ejemplo, un stock máximo total
# Aquí asumimos que podemos vender todos los productos que tenemos
A = []
b = []

# Resolver el problema de optimización
result = linprog(c, A_ub=A, b_ub=b, bounds=(0, None), method='highs')

# Mostrar resultados de la optimización
print("\nResultados de la Optimización:")
if result.success:
    print(f"Ganancia máxima optimizada: {-result.fun}")
    print("Cantidades óptimas a vender:")
    for i, cantidad in enumerate(result.x):
        print(f"{df['Producto'][i]}: {cantidad:.2f} unidades")
else:
    print("La optimización no fue exitosa.")

# 4. Simulación de Escenarios
# Simulación de un aumento del 10% en la demanda
aumento_demandas = df['Cantidad_Vendida'] * 1.1
df['nueva_cantidad_vendida'] = aumento_demandas

# Calcular nuevas ganancias
df['nueva_ganancia_total'] = df['ganancia_por_unidad'] * df['nueva_cantidad_vendida']

# Mostrar resultados de la simulación
print("\nResultados de la Simulación:")
print(df[['Producto', 'nueva_cantidad_vendida', 'nueva_ganancia_total']])
ganancia_maxima_nueva = df['nueva_ganancia_total'].sum()
print(f"\nGanancia máxima en el nuevo escenario: {ganancia_maxima_nueva:.2f}")

# Comparación de escenarios
diferencia_ganancia = ganancia_maxima_nueva + result.fun  # recuerda que result.fun está negado
print(f"Diferencia en la ganancia entre los dos escenarios: {diferencia_ganancia:.2f}")
