contactos = [
    {"nombre": "Ana", "numero": "3001234567", "f_nacimiento": "1995-03-15", "favorito": True},
    {"nombre": "Carlos", "numero": "3109876543", "f_nacimiento": "1990-05-20", "favorito": False},
    {"nombre": "Beatriz", "numero": "3205551234", "f_nacimiento": "1998-03-02", "favorito": True},
    {"nombre": "David", "numero": "3154449876", "f_nacimiento": "2001-11-10", "favorito": False}
]

print(" Lista de Contactos")
for contacto in contactos:
    print(f"Nombre: {contacto['nombre']} - Número: {contacto['numero']}")

print("\nContactos Favoritos ")
for contacto in contactos:
    if contacto["favorito"]:
        print(f"Favorito: {contacto['nombre']}")

mes_buscado = 2
cumpleaños_mes = sum(1 for c in contactos if int(c["f_nacimiento"].split("-")[1]) == mes_buscado)
print(f"\nCumpleaños en el mes {mes_buscado} ")
print(f"Total de personas que cumplen años: {cumpleaños_mes}")

nombres = [c["nombre"] for c in contactos]
print("\nLista solo con nombres")
print(nombres)

print("\nBúsqueda de contacto")
nombre_buscar = input("Ingresa el nombre a buscar: ") if False else "Ana" 

encontrado = False
for contacto in contactos:
    if contacto["nombre"].lower() == nombre_buscar.lower():
        print(f"Número de {contacto['nombre']}: {contacto['numero']}")
        encontrado = True
        break

if not encontrado:
    print("Contacto no existe")