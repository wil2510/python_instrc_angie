import numpy as np

ventas = np.array([120000, 95000, 150000, 80000, 200000, 175000, 110000])
ventas_aumentadas = ventas * 1.10
total_semana = np.sum(ventas_aumentadas)

print("Ventas aumentadas:", ventas_aumentadas)
print("Total de la semana:", total_semana)