## 📘 DOCUMENTACIÓN DEL SISTEMA EXPERTO MILLEPORA

## 🧠 Descripción General
Este sistema experto desarrollado en Python identifica especies del género *Millepora* presentes en aguas venezolanas. Incorpora una interfaz gráfica amigable construida con `customtkinter`, permitiendo a usuarios declarar características morfológicas mediante botones e imágenes ilustrativas.

---

## 🪸 Especies Identificables
1. **Millepora alcicornis** – Coral de fuego ramificado  
2. **Millepora complanata** – Coral de fuego aplanado  
3. **Millepora squarrosa** – Coral de fuego tipo boxwork

---

## 🔍 Características Morfológicas Utilizadas
- Forma de la colonia (ramificada, laminar, aplanada)
- Color (amarillo, naranja, marrón claro, beige)
- Oleaje del hábitat (fuerte, moderado)
- Estructura adicional (cilíndricas, abanico, cresta, someras, protuberancias, etc.)

---

## 📐 Lógica de Identificación
El motor experto utiliza reglas **IF–THEN** construidas sobre la librería `experta` (derivada de `pyknow`) para inferir la especie basada en la combinación de características morfológicas.

---

## 🖥️ Requisitos del Sistema

### Dependencias:
```bash
pip install experta customtkinter pillow pandas numpy
```

> ⚠️ A partir de Python 3.10, la clase `Mapping` fue movida. Instala una versión compatible de `frozendict` si `experta` falla:
```bash
pip install --upgrade frozendict
```

### Estructura de Carpetas Recomendada:
```
📁 millepora/
├── main.py                  # Ejecuta la interfaz
├── millepora_expert.py     # Lógica del sistema experto
├── assets/
│   ├── iconos/
│   ├── colores/
│   ├── forma/
│   ├── detalles/
│   ├── oleaje/
│   └── autores/
├── manual_usuario.pdf       # Manual accesible desde la interfaz
├── tests/
│   └── test_motor.py        # Tests automáticos (opcional)
└── README.md
```

---

## ▶️ Ejecución de la Interfaz

Desde el directorio principal, ejecuta:

```bash
python main.py
```

La GUI te guiará para seleccionar las características visibles del coral. Al hacer clic en **"🔍 IDENTIFICAR ESPECIE"**, el sistema inferirá la especie más probable basada en tus selecciones.

---

## 📄 Acceso al Manual de Usuario
Dentro de la pestaña **"Acerca de"**, encontrarás un botón que abre directamente el archivo `manual_usuario.pdf` en tu visor de PDF predeterminado.

---

## 🧪 Ejecutar Tests Unitarios
Si incluyes pruebas unitarias para el motor experto, puedes correrlas así:

```bash
python -m unittest discover -s tests
```

---

## ⚠️ Limitaciones
- Basado solo en características visuales/morfológicas
- No incluye análisis genético o molecular
- Limitado a especies comunes del Caribe venezolano
- Requiere conocimientos básicos para distinguir características taxonómicas

---

## 👥 Créditos
Desarrollado por:  
- Aaron Ortiz  
- Fabian Quijada  
- Eduardo Gonzales  

Colaboradores expertos:  
- Dr. Martin Rada  
- José Morillo  
