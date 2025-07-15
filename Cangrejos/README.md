### 🦀 Clasificador de Especies de Crustáceos
Este proyecto presenta un sistema experto innovador con una red neuronal integrada diseñado para identificar especies de crustáceos basándose en sus características físicas y ecológicas. La aplicación cuenta con una interfaz gráfica de usuario (GUI) intuitiva desarrollada con Tkinter y utiliza TensorFlow para potentes capacidades de predicción.

### 💡 ¿Cómo Funciona?
    El clasificador guía al usuario a través de un proceso interactivo para determinar la especie de crustáceo.

    Inicio de la Aplicación: Ejecuta el archivo principal interfaz.py.

    Menú Principal: Una ventana inicial te dará la bienvenida con las siguientes opciones:

    Identificaion: Inicia el cuestionario de identificación.

    Verificacion: Inicia un formulario sobre el nombre de la especie que quiere buscar

    Pagina Web: Muestra información sobre el proyecto y los desarrolladores.

    Salir: Cierra la aplicación.

    Cuestionario Interactivo: Al seleccionar "Ascendente", se te pedirá que confirmes el inicio de un cuestionario de 23 preguntas de tipo Sí/No. Estas preguntas están diseñadas para recopilar atributos clave del crustáceo.

    Recopilación de Datos: Tus respuestas se almacenan dinámicamente en un vector binario (1 para Sí, 0 para No).

    Predicción de Especies: Una vez completado el cuestionario, el botón "Predecir" se habilitará. Al pulsarlo, el modelo de red neuronal procesará el vector de respuestas y clasificará la especie de crustáceo más probable.

    Resultado Final: La especie predicha se mostrará claramente en la interfaz.

### ✨ Características Principales
    Interfaz Gráfica Amigable: Desarrollada con Tkinter para una experiencia de usuario sencilla e intuitiva.

    Cuestionario Dinámico: Preguntas visualmente centradas que guían al usuario paso a paso.

    Motor de Predicción Robusto: Utiliza una red neuronal profunda (modelo Keras) para una clasificación precisa de especies.

    Carga Automática de Recursos: El modelo entrenado (modelo_crustaceos.h5) y las etiquetas de las clases (clases.npy) se cargan automáticamente al iniciar la aplicación.

    Control de Navegación: Permite regresar al menú principal en cualquier momento durante el cuestionario y gestiona el flujo de forma robusta, incluso si el usuario cancela la operación.

    Predicción Manual: El botón "Predecir" brinda al usuario el control de cuándo ejecutar el proceso de clasificación.

### 📁 Estructura del Proyecto
    El proyecto está organizado de la siguiente manera:

    interfaz.py: El script principal que contiene la lógica de la interfaz gráfica y gestiona el flujo del cuestionario.

    modelo_crustaceos.h5: El archivo del modelo de red neuronal entrenado, guardado en formato H5 de Keras. Este archivo es crucial para las predicciones.

    clases.npy: Un archivo NumPy que almacena los nombres de las especies de crustáceos. El orden de estos nombres debe coincidir con el índice de salida del modelo de la red neuronal.

### 🎯 Ejemplo de Uso
    Aquí tienes un ejemplo de cómo se vería una interacción y su resultado:

    Respuestas del usuario (vector generado):
    [1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1]

    Especie predicha:
    Grapsus grapsus

### 🛠️ Requisitos e Instalación
    Para ejecutar este proyecto, necesitas tener Python instalado junto con algunas bibliotecas específicas.

    Versión de Python
    Python 3.10 o superior

    Dependencias
    TensorFlow: La biblioteca de código abierto de Google para el aprendizaje automático.

    NumPy: La biblioteca fundamental para computación numérica en Python.

    Pillow (PIL): La biblioteca para el procesamiento de imágenes, necesaria para trabajar con PIL.Image y PIL.ImageTk.

    tkinter: La biblioteca estándar de Python para crear interfaces gráficas de usuario (GUI). (Generalmente incluida con Python, pero se menciona por su uso explícito).

    webbrowser: Un módulo que provee una interfaz para permitir la visualización de documentos web. (Generalmente incluida con Python, pero se menciona por su uso explícito).

    Instalación Rápida
    Puedes instalar todas las dependencias necesarias usando pip, el gestor de paquetes de Python:

    Bash

    pip install tensorflow numpy pillow

### 👨‍💻 Desarrolladores
Este proyecto fue desarrollado por:

Jesus Marichal (C.I.: 28.344.112)

Gabriel Rosas (C.I.: 27.650.586)

German (C.I.: 30.707.833)

