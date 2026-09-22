class Cliente:
    def __init__(self, nombre, membresia_activa):
        self.nombre = nombre
        self.membresia_activa = membresia_activa

    def puede_entrenar(self):
        if self.membresia_activa:
            return "Puede entrenar"
        else:
            return "No puede entrenar"


cliente1 = Cliente("Carlos", True)

print(cliente1.nombre)
print(cliente1.puede_entrenar())