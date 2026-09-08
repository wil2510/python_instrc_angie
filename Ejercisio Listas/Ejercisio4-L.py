precios = [15000, 8000, 22000, 5000]
total = 0

for precio in precios:
    total += precio

promedio = total / len(precios)
print("Total:", total, "Promedio:", promedio)
