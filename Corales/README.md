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
