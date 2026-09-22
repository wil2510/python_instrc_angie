def calcular_propina(cuenta, porcentaje=10):
    propina = cuenta * porcentaje / 100
    return propina

cuenta = 50000

print("Propina:", calcular_propina(cuenta))