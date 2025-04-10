# importamos librerias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# seguido importamos los datos
dataset = pd.read_csv("Data.csv")
print(dataset)
# identificación de variables
# variable independiente -> x
# Variable dependiente -> y
x = dataset.iloc[:, 0:3].values
y = dataset.iloc[:, -1].values  # puede ser 0:10 o :
print(x)
print(y)
# Curar los datos: datos nulos o faltantes
# scikit-learn
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
imputer.fit(x[:, 1:3])
x[:, 1:3] = imputer.transform(x[:, 1:3])
print(x)

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

L = ColumnTransformer(
    transformers=[("encoder", OneHotEncoder(), [0])], remainder="passthrough"
)

x = np.array(L.fit_transform(x))
print("-" * 20)
print(x)
# ------------------
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
y = le.fit_transform(y)
print(y)
# Separar datos de entranamiento de datos de prueba from
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)
print(x_train, x_test, y_train, y_train)
# escalado de datos :standarización
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
x_train[:, 3:] = sc.fit_transform(x_train[:, 3:])
x_test[:, 3:] = sc.transform(x_test[:, 3:])
print(x_train, x_test)
