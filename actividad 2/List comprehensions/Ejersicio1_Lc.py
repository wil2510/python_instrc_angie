productos = [
    {"nombre": "Camisa", "precio": 45000},
    {"nombre": "Pantalón", "precio": 89000},
    {"nombre": "Media", "precio": 8000}
]

ofertas = [
    producto["nombre"]
    for producto in productos
    if producto["precio"] < 50000
]

print(ofertas)