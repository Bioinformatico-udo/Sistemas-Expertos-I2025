import numpy as np
from keras.models import load_model
import os
import tensorflow as tf

# Carga el modelo entrenado
#modelo = load_model('modelo.h5')
# Cargar modelo y clases desde la misma carpeta
base_dir = os.path.dirname(os.path.abspath(__file__))
modelo_path = os.path.join(base_dir, "modelo_crustaceos.h5")
clases_path = os.path.join(base_dir, "clases.npy")

modelo = tf.keras.models.load_model(modelo_path)
clases = np.load(clases_path, allow_pickle=True)

# Ejemplo de entrada manual
# Por ejemplo, un vector de ejemplo (cambia los valores según la pregunta):
entrada_manual = np.array([[1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1]])

# Realiza la predicción
prediccion = modelo.predict(entrada_manual)

# La predicción suele ser un vector con probabilidades para cada clase,
# así que para obtener la clase con mayor probabilidad:
clase_predicha = np.argmax(prediccion, axis=1)

print("Predicción (probabilidades):", prediccion)
print("Clase predicha (índice):", clase_predicha)
