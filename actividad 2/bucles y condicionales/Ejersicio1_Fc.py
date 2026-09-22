precios = [45000, 120000, 8000, 300000]

for precio in precios:
    if precio > 100000:
        descuento = precio * 0.15
        precio_final = precio - descuento
    else:
        precio_final = precio

    print("Precio final:", precio_final)