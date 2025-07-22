from experta import *
import os

class CoralCharacteristic(Fact):
    pass

class MilleporaExpert(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.identified_species = None
        self.confidence = 0.0

        base_path = os.path.join(os.path.dirname(__file__), "assets", "especies")
        self.species_info = {
            "Millepora alcicornis": {
                "descripcion": "Forma ramificada y color amarillo o marrón claro. Presente en aguas con oleaje moderado a fuerte.",
                "imagen": os.path.join(base_path, "alcicornis.jpg")
            },
            "Millepora complanata": {
                "descripcion": "Color beige o marrón claro. Forma laminar o aplanada. Oleaje moderado o fuerte.",
                "imagen": os.path.join(base_path, "complanata.jpg")
            },
            "Millepora squarrosa": {
                "descripcion": "Forma abanico o cresta, estructura aplanada, color anaranjado. Oleaje moderado.",
                "imagen": os.path.join(base_path, "squarrosa.jpg")
            }
        }

    @DefFacts()
    def _initial_action(self):
        yield Fact(start=True)

    @Rule(CoralCharacteristic(forma='ramificada'),
          CoralCharacteristic(color='amarillo'),
          CoralCharacteristic(oleaje='fuerte'),
          CoralCharacteristic(estructura='cilindricas'))
    def especie_alcicornis(self):
        self.identified_species = "Millepora alcicornis"
        self.confidence = 1.0

    @Rule(CoralCharacteristic(forma='laminar'),
          CoralCharacteristic(color='beige'),
          CoralCharacteristic(oleaje='moderado'),
          CoralCharacteristic(superficie='aplanadas'))
    def especie_complanata(self):
        self.identified_species = "Millepora complanata"
        self.confidence = 1.0

    @Rule(CoralCharacteristic(forma='aplanada'),
          CoralCharacteristic(color='naranja'),
          CoralCharacteristic(estructura='abanico'),
          CoralCharacteristic(oleaje='moderado'))
    def especie_squarrosa(self):
        self.identified_species = "Millepora squarrosa"
        self.confidence = 1.0

    def get_diagnosis_summary(self):
        lines = []
        if self.identified_species == "Millepora alcicornis":
            lines.append("- Forma ramificada y color amarillo o marrón claro sugiere Millepora alcicornis.")
        elif self.identified_species == "Millepora complanata":
            lines.append("- Forma laminar o aplanada y color beige o marrón claro sugiere Millepora complanata.")
        elif self.identified_species == "Millepora squarrosa":
            lines.append("- Forma abanico o cresta, estructura aplanada y color anaranjado sugiere Millepora squarrosa.")
        return "\n".join(lines)

    def get_result_info(self):
        if not self.identified_species:
            return None
        data = self.species_info[self.identified_species]
        return {
            "nombre": self.identified_species,
            "confianza": round(self.confidence * 100, 1),
            "descripcion": data["descripcion"],
            "imagen": data["imagen"]
        }
