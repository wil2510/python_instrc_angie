import pandas as pd

datos = {
    'Nombre': ['Ana', 'Luis', 'Carlos'],
    'Edad': [25, 30, 22],
    'Ciudad': ['Madrid', 'Bogota', 'mexico']
}
df = pd.DataFrame(datos)
print(df)