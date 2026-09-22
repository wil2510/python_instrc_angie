correos = [
    "ana@gmail.com",
    "luis",
    "carlos@hotmail.com",
    "sena"
]

correos_validos = [
    correo
    for correo in correos
    if "@" in correo
]

print(correos_validos)