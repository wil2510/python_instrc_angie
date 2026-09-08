producto = {
    "nombre": "Teclado",
    "precio": 50000,
    "cantidad_en_stock": 10
}

print("Producto:", producto["nombre"])
print("Precio:", producto["precio"])
print("Stock inicial:", producto["cantidad_en_stock"])

venta = 3

producto["cantidad_en_stock"] = producto["cantidad_en_stock"] - venta
print("Stock después de la venta:", producto["cantidad_en_stock"])