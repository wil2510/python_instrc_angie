asistencias = [1, 1, 0, 1, 0, 0, 1]

faltas = 0

for asistencia in asistencias:
    if asistencia == 0:
        faltas += 1

print("Cantidad de faltas:", faltas)

if faltas > 2:
    print("Alerta: tiene más de 2 inasistencias")
else:
    print("No tiene alerta")