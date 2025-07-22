# Sistema Experto para Reconocimiento de Corales Millepora en Venezuela

from experta import *
import sys

# Definición de hechos (Facts)
class CoralCharacteristic(Fact):
    """Características morfológicas del coral"""
    pass

class IdentificationResult(Fact):
    """Resultado de la identificación"""
    pass

class MilleporaExpert(KnowledgeEngine):
    """Sistema experto para identificación de especies de Millepora"""

    def __init__(self):
        super().__init__()
        self.identified_species = None
        self.confidence = 0.0

    # Reglas de identificación

    @Rule(CoralCharacteristic(superficie='con_poros'),
          CoralCharacteristic(septa='ausentes'))
    def es_millepora(self):
        """Identifica si es del género Millepora"""
        self.declare(CoralCharacteristic(genero='Millepora'))
        print("✓ Identificado como género Millepora")

    @Rule(CoralCharacteristic(genero='Millepora'),
          CoralCharacteristic(forma_colonia='ramificada'),
          CoralCharacteristic(forma_ramas='delgadas_aplanadas'),
          CoralCharacteristic(espesor_ramas='10-15mm'))
    def es_millepora_alcicornis(self):
        """Identifica M. alcicornis"""
        self.identified_species = "Millepora alcicornis"
        self.confidence = 0.85
        self.declare(IdentificationResult(species="Millepora alcicornis", confidence=0.85))
        print("✓ Identificado como Millepora alcicornis (85% confianza)")

    @Rule(CoralCharacteristic(genero='Millepora'),
          CoralCharacteristic(forma_colonia='laminar'),
          CoralCharacteristic(forma_ramas='hojas_delgadas'),
          CoralCharacteristic(base='incrustante'))
    def es_millepora_complanata(self):
        """Identifica M. complanata"""
        self.identified_species = "Millepora complanata"
        self.confidence = 0.90
        self.declare(IdentificationResult(species="Millepora complanata", confidence=0.90))
        print("✓ Identificado como Millepora complanata (90% confianza)")

    @Rule(CoralCharacteristic(genero='Millepora'),
          CoralCharacteristic(forma_colonia='boxwork'),
          CoralCharacteristic(forma_ramas='robustas_interconectadas'),
          CoralCharacteristic(superficie='rugosa'))
    def es_millepora_squarrosa(self):
        """Identifica M. squarrosa"""
        self.identified_species = "Millepora squarrosa"
        self.confidence = 0.80
        self.declare(IdentificationResult(species="Millepora squarrosa", confidence=0.80))
        print("✓ Identificado como Millepora squarrosa (80% confianza)")

    @Rule(CoralCharacteristic(genero='Millepora'),
          CoralCharacteristic(color='amarillo-naranja'))
    def refuerza_alcicornis(self):
        """Refuerza identificación de M. alcicornis por color"""
        if self.identified_species == "Millepora alcicornis":
            self.confidence = min(0.95, self.confidence + 0.10)
            print("✓ Confianza aumentada para M. alcicornis por color característico")

    @Rule(CoralCharacteristic(genero='Millepora'),
          CoralCharacteristic(color='mostaza_marron'))
    def refuerza_complanata(self):
        """Refuerza identificación de M. complanata por color"""
        if self.identified_species == "Millepora complanata":
            self.confidence = min(0.95, self.confidence + 0.05)
            print("✓ Confianza aumentada para M. complanata por color característico")

    @Rule(CoralCharacteristic(genero='Millepora'),
          CoralCharacteristic(profundidad='0-15m'),
          CoralCharacteristic(habitat='arrecifes_poco_profundos'))
    def habitat_complanata(self):
        """Identifica habitat típico de M. complanata"""
        if self.identified_species == "Millepora complanata":
            self.confidence = min(0.95, self.confidence + 0.05)
            print("✓ Habitat confirma M. complanata")

    @Rule(CoralCharacteristic(genero='Millepora'),
          CoralCharacteristic(profundidad='0-50m'),
          CoralCharacteristic(habitat='aguas_tranquilas_agitadas'))
    def habitat_alcicornis(self):
        """Identifica habitat amplio de M. alcicornis"""
        if self.identified_species == "Millepora alcicornis":
            self.confidence = min(0.95, self.confidence + 0.05)
            print("✓ Habitat amplio confirma M. alcicornis")

    @Rule(NOT(IdentificationResult()))
    def no_identification(self):
        """Cuando no se puede identificar la especie"""
        print("⚠ No se pudo identificar la especie con certeza")
        print("Revisar características morfológicas adicionales")

# Función para crear nueva identificación interactiva
def interactive_identification():
    """Identificación interactiva paso a paso"""
    print("\n=== IDENTIFICACIÓN INTERACTIVA ===")
    print("Responda las siguientes preguntas sobre el coral:")

    expert = MilleporaExpert()
    expert.reset()

    # Preguntas básicas
    superficie = input("¿La superficie tiene pequeños poros? (si/no): ").lower()
    if superficie == 'si':
        expert.declare(CoralCharacteristic(superficie='con_poros'))

    septa = input("¿Hay septa presentes? (si/no): ").lower()
    if septa == 'no':
        expert.declare(CoralCharacteristic(septa='ausentes'))

    forma = input("¿Forma de la colonia? (ramificada/laminar/boxwork): ").lower()
    expert.declare(CoralCharacteristic(forma_colonia=forma))

    if forma == 'ramificada':
        ramas = input("¿Forma de las ramas? (delgadas_aplanadas/robustas): ").lower()
        expert.declare(CoralCharacteristic(forma_ramas=ramas))

        if ramas == 'delgadas_aplanadas':
            espesor = input("¿Espesor de ramas? (10-15mm/otro): ").lower()
            expert.declare(CoralCharacteristic(espesor_ramas=espesor))

    elif forma == 'laminar':
        base = input("¿Tiene base incrustante? (si/no): ").lower()
        if base == 'si':
            expert.declare(CoralCharacteristic(base='incrustante'))
        expert.declare(CoralCharacteristic(forma_ramas='hojas_delgadas'))

    elif forma == 'boxwork':
        expert.declare(CoralCharacteristic(forma_ramas='robustas_interconectadas'))
        superficie_rugosa = input("¿Superficie rugosa? (si/no): ").lower()
        if superficie_rugosa == 'si':
            expert.declare(CoralCharacteristic(superficie='rugosa'))

    # Ejecutar motor de inferencia
    expert.run()

    if expert.identified_species:
        print(f"\nRESULTADO: {expert.identified_species}")
        print(f"Confianza: {expert.confidence:.2f}")
    else:
        print("\nNo se pudo identificar la especie con certeza")
        print("Consulte con un taxonomista especializado")

if __name__ == "__main__":
    interactive_identification()
