estudiante = ("yedinson", 1, "ADSO")


print("Nombre:", estudiante[0])
print("Edad:", estudiante[1])
print("Curso:", estudiante[2])

estudiante[2] = "Programación"

#File "c:\python-3\Ejercisio Tuplas\Ejercisio2-T.py", line 7, in <module> estudiante[2] = "Programación"
#Porque las tuplas son inmutables, es decir, después de crearlas no podemos modificar, agregar ni eliminar sus elementos.