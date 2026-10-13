import pandas as pd

inventario = {
    "producto": ["Camisa", "Gorra", "Pantalón", "Medias", "Zapatos"],
    "precio": [45000, 30000, 89000, 8000, 150000],
    "stock": [20, 5, 12, 40, 3],
}

df = pd.DataFrame(inventario)

print(df.head())
print(df.shape)
print(df.columns)
print(df.describe())