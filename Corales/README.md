<<<<<<< HEAD
# DOCUMENTACIÓN DEL SISTEMA EXPERTO MILLEPORA

## Descripción General
Sistema experto desarrollado en Python utilizando la librería experta para la identificación automatizada de especies del género Millepora encontradas en aguas venezolanas.

## Especies Incluidas
1. **Millepora alcicornis** - Coral de fuego ramificado
2. **Millepora complanata** - Coral de fuego aplanado  
3. **Millepora squarrosa** - Coral de fuego boxwork

## Características Morfológicas Utilizadas
- Forma de la colonia (ramificada, laminar, boxwork)
- Forma de las ramas (delgadas aplanadas, hojas delgadas, robustas interconectadas)
- Espesor de las ramas
- Superficie (lisa, rugosa, con poros)
- Color (amarillo-naranja, mostaza-marrón, variable)
- Presencia/ausencia de septa
- Tipo de base (incrustante, libre)
- Hábitat y profundidad

## Reglas de Identificación
El sistema utiliza un conjunto de reglas IF-THEN que evalúan las características morfológicas:

1. **Identificación de género**: Superficie con poros + ausencia de septa → Millepora
2. **Identificación de especies**: Combinación de forma, estructura y características específicas
3. **Factores de refuerzo**: Color, hábitat y profundidad aumentan la confianza

## Información de implementación del sistema experto

### Librerías requeridas:
- experta (fork de pyknow)
- pandas (para manejo de datos)
- numpy (para cálculos)

### Instalación:
```bash
pip install experta pandas numpy
```

### Instalar una Versión Compatible de frozendict
A partir de Python 3.10, la clase Mapping ya no está en el módulo collections, sino en collections.abc. lo que provoca error al intentar importar la clase frozendict dentro de la librería experta.

```bash
pip install --upgrade frozendict
```

## Ejecutar los tests
Para ejecutar todos los tests sitúate en la raíz del proyecto y ejecuta el siguiente comando:
```bash
python -m unittest discover -s tests
```

## Uso del Sistema
```python
# Instanciar el sistema
expert = MilleporaExpert()

# Declarar características observadas
expert.declare(CoralCharacteristic(superficie='con_poros'))
expert.declare(CoralCharacteristic(septa='ausentes'))
expert.declare(CoralCharacteristic(forma_colonia='ramificada'))

# Ejecutar motor de inferencia
expert.run()
```

## Limitaciones
- Basado en características morfológicas únicamente
- No incluye análisis molecular
- Requiere experiencia taxonómica para la observación de características
- Limitado a especies del Caribe venezolano
=======
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
>>>>>>> 2622e5865734682b1d44baeb16ccd72223b945e3
