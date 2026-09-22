notas = [4.5, 3.2, 2.8, 4.0, 3.7]
notas.append(4.8)
print("Notas después de agregar:", notas)

nota_baja = min(notas)
notas.remove(nota_baja)

print("Notas después de eliminar la más baja:", notas)