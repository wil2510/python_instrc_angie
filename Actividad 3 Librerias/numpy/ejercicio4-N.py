import numpy as np

calificaciones = np.array([
    [8.5, 7.0, 9.0, 8.0],
    [6.0, 7.5, 8.0, 7.0],
    [9.0, 8.5, 9.5, 9.0]
])

promedio_estudiantes = calificaciones.mean(axis=1)
promedio_materias = calificaciones.mean(axis=0)

print("Promedio por estudiante:", promedio_estudiantes)
print("Promedio por materia:", promedio_materias)