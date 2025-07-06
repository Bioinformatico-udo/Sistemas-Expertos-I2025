import os
import numpy as np
import tensorflow as tf
import tkinter as tk
from tkinter import messagebox
import webbrowser


# Cargar modelo y clases desde la misma carpeta
base_dir = os.path.dirname(os.path.abspath(__file__))
modelo_path = os.path.join(base_dir, "modelo_crustaceos.h5")
clases_path = os.path.join(base_dir, "clases.npy")

modelo = tf.keras.models.load_model(modelo_path)
clases = np.load(clases_path, allow_pickle=True)

# Preguntas
preguntas = [
    "¿Vive en agua dulce?",                        # agua_dulce
    "¿Vive en agua salada?",                       # agua_salada
    "¿Es de tamaño pequeño? (2.0 cm a 3.0 cm)",    # pequeño
    "¿Es de tamaño mediano? (3.1 cm a 4.0 cm)",    # mediano
    "¿Es de tamaño grande? (más de 4.0 cm)",       # grande
    "¿Tiene caparazón redondo?",                   # caparazon_redondo
    "¿Tiene caparazón ovalado?",                   # caparazon_ovalado
    "¿Tiene caparazón alargado?",                  # caparazon_alargado
    "¿Su color es rojo?",                          # rojo
    "¿Su color es verde?",                         # verde
    "¿Su color es marrón?",                        # marron
    "¿Su cuerpo es transparente?",                 # transparente
    "¿Tiene pinzas grandes?",                      # pinzas_grandes
    "¿Tiene pinzas pequeñas?",                     # pinzas_pequeñas
    "¿Tiene patas nadadoras?",                     # patas_nadadoras
    "¿Tiene patas caminadoras?",                   # patas_caminadoras
    "¿Sus antenas son cortas?",                    # antenas_cortas
    "¿Sus antenas son largas?",                    # antenas_largas
    "¿Habita en zonas rocosas?",                   # habitat_rocoso
    "¿Habita en zonas de arena?",                  # habitat_arena
    "¿Vive en zonas de corrientes fuertes?",       # corrientes_fuertes
    "¿Vive en zonas de corrientes suaves?",        # corrientes_suaves
    "¿Está ovígera (con huevos)?"                 # ovigera
]


respuesta_vector = []
indice_pregunta = 0

ventana = tk.Tk()
ventana.title("Clasificación de Especies")
ventana.geometry("520x500")
ventana.configure(bg="#dbe4f0")
ventana.resizable(False, False)

# ================= FUNCIONES =================

def regresar_menu():
    titulo.pack(pady=20)
    texto.pack_forget()
    contenedor_botones.pack_forget()
    btn_salir_cuestionario.pack_forget()
    boton_predecir.pack_forget()
    for b in botones_inicio:
        b.pack(pady=5)

def iniciar_confirmacion():
    titulo.pack_forget()
    for b in botones_inicio:
        b.pack_forget()
    btn_salir_cuestionario.pack_forget()
    contenedor_botones.pack_forget()
    texto.pack_forget()
    boton_predecir.pack_forget()

    texto.config(
        text="A continuación se le hará un cuestionario para poder identificar la especie.\n¿Desea continuar?",
        font=("Segoe UI", 12),
        justify="center"
    )
    texto.pack(pady=150, anchor="center")
    contenedor_botones.pack()
    btn_si.config(command=confirmar_inicio_cuestionario)
    btn_no.config(command=regresar_menu)

def confirmar_inicio_cuestionario():
    global respuesta_vector, indice_pregunta
    respuesta_vector = []
    indice_pregunta = 0
    btn_si.config(command=lambda: registrar_respuesta(1))
    btn_no.config(command=lambda: registrar_respuesta(0))
    btn_salir_cuestionario.pack(pady=20)
    messagebox.showinfo(
        "ALERTA",
        "Por favor, responda correctamente a las preguntas que se van a mostrar."
    )
    mostrar_pregunta()

def mostrar_pregunta():
    if indice_pregunta >= len(preguntas):
        mostrar_resultado()
        return
    texto.config(
        text=preguntas[indice_pregunta],
        font=("Segoe UI", 13),
        justify="center"
    )
    texto.pack(pady=125)
    contenedor_botones.pack()

def registrar_respuesta(valor):
    global indice_pregunta
    respuesta_vector.append(valor)
    indice_pregunta += 1
    mostrar_pregunta()

def mostrar_resultado():
    contenedor_botones.pack_forget()
    texto.config(text="Cuestionario completado.\nPresione 'Predecir' para obtener la especie.",
                 font=("Segoe UI", 13), justify="center")
    texto.pack(pady=80)
    boton_predecir.pack(pady=10)
    btn_salir_cuestionario.pack(pady=10)

def predecir_especie():
    entrada = np.array([respuesta_vector])
    prediccion = modelo.predict(entrada)
    especie = clases[np.argmax(prediccion)]
    texto.config(text=f"Especie predicha: {especie}")
    boton_predecir.pack_forget()

def salir():
    ventana.destroy()

def mostrar_acerca_de():
    webbrowser.open("https://github.com/Bioinformatico-udo/Sistemas-Expertos-I2025/tree/main")

# ================ UI ==================

titulo = tk.Label(ventana, text="Clasificador de Especies",
                  font=("Segoe UI", 14, "bold"), bg="#dbe4f0", fg="#000000")
titulo.pack(pady=20)

botones_inicio = [
    tk.Button(ventana, text="Ascendente", bg="#6c757d", fg="white", font=("Segoe UI", 11),
              width=20, pady=8, command=iniciar_confirmacion),
    tk.Button(ventana, text="Decreciente", bg="#6c757d", fg="white", font=("Segoe UI", 11),
              width=20, pady=8, command=lambda: print("Orden descendente")),
    tk.Button(ventana, text="Acerca De", bg="#3b9c9c", fg="white", font=("Segoe UI", 11),
              width=20, pady=8, command=mostrar_acerca_de),
    tk.Button(ventana, text="Salir", bg="#c0392b", fg="white", font=("Segoe UI", 11),
              width=20, pady=8, command=salir)
]

for b in botones_inicio:
    b.pack(pady=5)

texto = tk.Label(ventana, text="", font=("Segoe UI", 12),
                 wraplength=440, bg="#dbe4f0", justify="center")

contenedor_botones = tk.Frame(ventana, bg="#dbe4f0")
btn_si = tk.Button(contenedor_botones, text="SI", bg="#3498db", fg="white", width=10, font=("Segoe UI", 11))
btn_no = tk.Button(contenedor_botones, text="NO", bg="#e74c3c", fg="white", width=10, font=("Segoe UI", 11))
btn_si.pack(side="left", padx=10, pady=5)
btn_no.pack(side="right", padx=10, pady=5)

btn_salir_cuestionario = tk.Button(ventana, text="Salir al menú", bg="#a93226", fg="white",
                                   font=("Segoe UI", 11), width=20, pady=6, command=regresar_menu)

boton_predecir = tk.Button(ventana, text="Predecir", bg="#2e86c1", fg="white",
                           font=("Segoe UI", 11), width=20, pady=6, command=predecir_especie)

ventana.mainloop()
