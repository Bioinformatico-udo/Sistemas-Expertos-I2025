import pandas as pd
import numpy as np
import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical


def cargar_datos_csv(nombre_archivo):
    ruta_base = os.path.dirname(__file__)  # carpeta donde está este script
    ruta_completa = os.path.join(ruta_base, nombre_archivo)
    
    if not os.path.exists(ruta_completa):
        raise FileNotFoundError(f"No se encontró el archivo: {ruta_completa}")
    
    df = pd.read_csv(ruta_completa)
    return df

# Cargando el Archivo CSV que contiene las claves(Caracteristicas)
datos = cargar_datos_csv("crustaceos_entrenamiento.csv")
#print(datos)

# Separar características (X) y etiquetas (y)
X = datos.drop('especie', axis=1).values
y = datos['especie'].values

# Codificar etiquetas a números + one-hot
from sklearn.preprocessing import LabelEncoder
from keras.utils import to_categorical

encoder = LabelEncoder()
y_numerico = encoder.fit_transform(y)
y_categ = to_categorical(y_numerico)

# Dividir en entrenamiento y validación
from sklearn.model_selection import train_test_split

X_train, X_val, y_train, y_val = train_test_split(X, y_categ, test_size=0.25, random_state=42)

# Construcción del modelo MLP
from keras.models import Sequential
from keras.layers import Dense

modelo = Sequential([
    Dense(32, activation='relu', input_shape=(X.shape[1],)),
    Dense(32, activation='relu'),
    Dense(y_categ.shape[1], activation='softmax')
])

modelo.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Entrenar en 125 epocas, apartir de la 100 dejaba de aprender 
modelo.fit(X_train, y_train, epochs=125, batch_size=4, validation_data=(X_val, y_val))

# Guarda el modelo entrenado y las clases
modelo.save("Cangrejos/src/modelo_crustaceos.h5")
import numpy as np
np.save("Cangrejos/src/clases.npy", encoder.classes_)

print("Entrenamiento finalizado y modelo guardado con éxito.")
