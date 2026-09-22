class CarritoCompras:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, nombre, precio):
        self.productos.append({
            "nombre": nombre,
            "precio": precio
        })

    def total(self):
        total = 0

        for producto in self.productos:
            total += producto["precio"]

        return total


carrito = CarritoCompras()

carrito.agregar_producto("Camisa", 45000)
carrito.agregar_producto("Pantalón", 80000)

print("Total:", carrito.total())