class Curso:
    def __init__(self):
        self.estudiantes = []

    def inscribir(self, nombre, edad):
        if edad > 15:
            self.estudiantes.append({
                "nombre": nombre,
                "edad": edad
            })
            print(nombre, "fue inscrito correctamente")
        else:
            print(nombre, "no puede inscribirse")

    def listar_mayores_edad(self):
        mayores = [
            estudiante["nombre"]
            for estudiante in self.estudiantes
            if estudiante["edad"] > 18
        ]

        return mayores


curso = Curso()

curso.inscribir("Carlos", 20)
curso.inscribir("Ana", 16)
curso.inscribir("Luis", 14)
curso.inscribir("María", 22)

print("Estudiantes mayores de edad:")
print(curso.listar_mayores_edad())