import pandas as pd
import numpy as np
import random
import os

# Función que carga un archivo CSV a partir del nombre del archivo
def cargar_datos_csv(nombre_archivo):
    ruta_base = os.path.dirname(__file__)  # Obtiene la ruta donde se encuentra este script
    ruta_completa = os.path.join(ruta_base, nombre_archivo)  # Une la ruta base con el nombre del archivo

    # Verifica si el archivo existe
    if not os.path.exists(ruta_completa):
        raise FileNotFoundError(f"No se encontró el archivo: {ruta_completa}")
    
    df = pd.read_csv(ruta_completa)  # Carga el archivo CSV como un DataFrame
    return df

# Carga el archivo original de crustáceos
df_base = cargar_datos_csv("crustaceos_petrolisthes.csv")

# Lista de atributos que pueden variar entre individuos de una misma especie
atributos_variables = [
    'rojo', 'verde', 'marron', 'transparente',
    'pinzas_grandes', 'pinzas_pequeñas',
    'patas_nadadoras', 'patas_caminadoras',
    'antenas_cortas', 'antenas_largas'
]

# Obtiene el resto de atributos considerados "fijos" (que no se alteran entre muestras)
atributos_fijos = [col for col in df_base.columns if col not in atributos_variables and col != 'especie']

# Función que genera múltiples variaciones de un individuo, modificando solo los atributos variables
def generar_variaciones(fila_base, n=10):
    variaciones = []
    for _ in range(n):
        nueva = fila_base.copy()
        for var in atributos_variables:
            nueva[var] = random.choice([0, 1])  # Asigna un valor aleatorio (0 o 1) a cada atributo variable
        variaciones.append(nueva)
    return variaciones

# Crea una lista para almacenar todas las filas del nuevo dataset
data_expandido = []

# Recorre cada fila del DataFrame original
for _, fila in df_base.iterrows():
    ejemplo_base = fila.to_dict()  # Convierte la fila en diccionario
    variantes = generar_variaciones(ejemplo_base, n=10)  # Genera 10 variaciones de esa fila
    data_expandido.extend(variantes)  # Agrega las variaciones a la lista principal

# Convierte los datos expandidos a un nuevo DataFrame
df_expandido = pd.DataFrame(data_expandido)

# Asegura que la carpeta de salida exista
os.makedirs("Cangrejos/src", exist_ok=True)

# Guarda el nuevo dataset en un archivo CSV
df_expandido.to_csv("Cangrejos/src/crustaceos_entrenamiento.csv", index=False)

# Mensaje final de confirmación
print("Dataset expandido generado: 80 ejemplos guardados en 'Cangrejos/src/crustaceos_entrenamiento.csv'")
