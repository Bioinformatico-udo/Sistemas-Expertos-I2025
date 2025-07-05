import pandas as pd
import numpy as np
import random
import os

def cargar_datos_csv(nombre_archivo):
    ruta_base = os.path.dirname(__file__)  # carpeta donde está este script
    ruta_completa = os.path.join(ruta_base, nombre_archivo)
    
    if not os.path.exists(ruta_completa):
        raise FileNotFoundError(f"No se encontró el archivo: {ruta_completa}")
    
    df = pd.read_csv(ruta_completa)
    return df

# Cargar el archivo original
df_base = cargar_datos_csv("crustaceos_petrolisthes.csv")

# Columnas que pueden variar entre individuos de una misma especie
atributos_variables = [
    'rojo', 'verde', 'marron', 'transparente',
    'pinzas_grandes', 'pinzas_pequeñas',
    'patas_nadadoras', 'patas_caminadoras',
    'antenas_cortas', 'antenas_largas'
]

# Columnas fijas (por especie)
atributos_fijos = [col for col in df_base.columns if col not in atributos_variables and col != 'especie']

# Generador de variaciones
def generar_variaciones(fila_base, n=10):
    variaciones = []
    for _ in range(n):
        nueva = fila_base.copy()
        for var in atributos_variables:
            nueva[var] = random.choice([0, 1])  # valor aleatorio controlado
        variaciones.append(nueva)
    return variaciones

# Crear nuevo dataset expandido
data_expandido = []

for _, fila in df_base.iterrows():
    ejemplo_base = fila.to_dict()
    variantes = generar_variaciones(ejemplo_base, n=10)
    data_expandido.extend(variantes)

# Guardar en nuevo archivo CSV
df_expandido = pd.DataFrame(data_expandido)
os.makedirs("Cangrejos/src", exist_ok=True)
df_expandido.to_csv("Cangrejos/src/crustaceos_entrenamiento.csv", index=False)

print("Dataset expandido generado: 80 ejemplos guardados en 'Cangrejos/src/crustaceos_entrenamiento.csv'")
