import numpy as np

numeros = np.array([10,20,30,40,50])
print(numeros)
print(numeros + 2)
print(numeros * 2)
print(numeros / 10)


# import numpy as np
notas = np.array([[3.5, 4.0, 2.2, 5.0], [4.4, 5.0, 3.0, 3.0], [5.0, 3.8, 4.6, 4.0]])

print(notas.mean(axis = 1))
print(notas.max())
print(notas.min())

calificaciones = np.array([
    [8.5, 7.0, 9.0], #carlos
    [6.0, 7.5, 8.0]  #ana
])
print(calificaciones.shape) # (2, 3)
print(calificaciones[0]) # fila de carlos 
print(calificaciones[:, 0]) # columna 1