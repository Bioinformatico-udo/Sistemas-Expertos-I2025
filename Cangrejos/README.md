# Clasificador de Especies de Crustáceos

Este proyecto es un sistema experto con red neuronal integrada que permite identificar especies de crustáceos a partir de sus características físicas y ecológicas. Está implementado con una interfaz gráfica amigable en Tkinter y usa TensorFlow para la predicción.

---

## ¿Cómo funciona?

1. El usuario ejecuta la interfaz `interfaz.py`.
2. Aparece una ventana con botones: Ascendente, Decreciente, Acerca De y Salir.
3. Al hacer clic en "Ascendente", se muestra un mensaje de confirmación para iniciar un cuestionario.
4. Si el usuario acepta, se presentan 19 preguntas cerradas (Sí/No) relacionadas con atributos del crustáceo.
5. Las respuestas se almacenan en un vector binario (1 = Sí, 0 = No).
6. Al finalizar el cuestionario, el usuario puede presionar "Predecir" para que el modelo clasifique la especie más probable.
7. La especie predicha se muestra en pantalla.

---

## Funcionalidades principales

- Interfaz gráfica en Python
- Cuestionario dinámico y visualmente centrado
- Predicción con red neuronal entrenada (modelo Keras)
- Carga automática del modelo y etiquetas desde archivos externos
- Botón "Predecir" que permite al usuario ejecutar la predicción manualmente
- Posibilidad de regresar al menú principal en cualquier momento durante el cuestionario
- Control total del flujo de navegación, incluso si el usuario cancela

---

## Archivos del proyecto

- `interfaz.py` — Script principal de la interfaz gráfica y cuestionario
- `modelo_crustaceos.h5` — Red neuronal entrenada con Keras
- `clases.npy` — Nombres de las especies en el mismo orden que el índice de salida del modelo

---

## Ejemplo de salida

Vector generado: [1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1] Especie predicha: Grapsus grapsus

---

## Requisitos

- Python 3.10 o superior
- TensorFlow
- NumPy

Instalación rápida:

```bash(consola)
pip install tensorflow numpy

---

## Desarrolladores

- Jesus Marichal (28.344.112)
- Gabriel Rosas (27650586)
- German ()

---
