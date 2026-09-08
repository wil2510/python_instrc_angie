animales=["gato","perro","vaca"]
animales.append("mono")
animales.remove("gato")
animales[1]="cerdo"
animales[0]="oveja"

print(animales)


temperaturas=[22,18,30,25,26,20]
temperaturas.append(20.5)
temperaturas[4]=16
temperaturas.remove(18)

promedio=sum(temperaturas)/len(temperaturas)
maximo=max(temperaturas)
minimo=min(temperaturas)
print("El promedio de las temperaturas es:", promedio)
print("La temperatura máxima es:", maximo)
print("La temperatura mínima es:", minimo)



persona={"nombre":"Ana", "edad":18}
persona["edad"]=22
persona["ciudad"]="Popayan"
print(persona)


estudiantes = {
    "nombre": "camila",
    "curso": "python basico",
    "nota": 4.5,
    "aprobado": True
},
{
    "nombre": "David",
    "curso": "python basico",
    "nota": 4.0,
    "aprobado": True
},
{
    "nombre": "Samuel",
    "curso": "python basico",
    "nota": 3.8,
    "aprobado": True
}
estudiantes[1]["nota"] = 5.0
for estudiante in estudiantes:
    for clave,valor in estudiantes.items():print(clave, valor)
