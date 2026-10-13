import pandas as pd
from sklearn.tree import DecisionTreeClassifier

archivo = '../datos.xlsx'

xls = pd.ExcelFile(archivo)
df = pd.read_excel(xls, sheet_name=xls.sheet_names[0], header=None)

X = df.iloc[:, [0]].values
y = df.iloc[:, 1].values

modelo = DecisionTreeClassifier(random_state=42)
modelo.fit(X, y)

prediccion = modelo.predict([[8000]])

if prediccion[0] == 1:
    print("El cliente puede comprar")
else:
    print("El cliente no puede comprar")