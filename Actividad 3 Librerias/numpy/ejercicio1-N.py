import numpy as np

notas = np.array([7.5, 8.0, 6.5, 9.0, 5.5, 8.5])

promedio = np.mean(notas)
maximo = np.max(notas)
minimo = np.min(notas)
desviacion = np.std(notas)

print("Promedio:", promedio)
print("Máximo:", maximo)
print("Mínimo:", minimo)
print("Desviación estándar:", desviacion)