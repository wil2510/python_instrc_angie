def es_valida(contrasena):
    if len(contrasena) >= 8:
        return True
    else:
        return False


print(es_valida("12345678"))
print(es_valida("1234"))