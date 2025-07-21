from experta import *

class CoralCharacteristic(Fact):
    """Características observables del coral"""
    pass

class IdentificationResult(Fact):
    """Resultado de la identificación"""
    pass

class MilleporaExpert(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.identified_species = None
        self.confidence = 0.0
        self.diagnostic_features = []
        self.species_info = {
            "Millepora alcicornis": {
                "description": "Colonia ramificada con ramas cilíndricas o aplanadas. "
                               "Las ramas pueden ser gruesas o delgadas, generalmente "
                               "con puntas redondeadas.",
                "color": "Marrón amarillento a anaranjado",
                "habitat": "Arrecifes someros con fuerte oleaje (1-35m de profundidad). "
                           "Prefiere zonas expuestas a corrientes.",
                "distribution": "Veracruz, Banco de Campeche, Caribe mexicano, "
                                "Florida, Bahamas, Antillas Mayores y Menores"
            },
            "Millepora complanata": {
                "description": "Láminas verticales en forma de abanico o cresta. "
                               "Las láminas pueden ser lisas o con pequeñas "
                               "protuberancias en la superficie.",
                "color": "Amarillo dorado a marrón claro",
                "habitat": "Áreas con oleaje moderado a fuerte (1-18m de profundidad). "
                           "Común en crestas arrecifales y pendientes.",
                "distribution": "Caribe mexicano, Banco de Campeche, Veracruz, "
                                "Belice, Honduras, Islas Cayman"
            },
            "Millepora squarrosa": {
                "description": "Forma aplanada con protuberancias distintivas, "
                               "crecimiento irregular. Superficie rugosa con "
                               "numerosas pequeñas elevaciones.",
                "color": "Marrón claro a beige",
                "habitat": "Zonas someras poco conocidas, generalmente entre "
                           "1-5m de profundidad. Prefiere áreas protegidas.",
                "distribution": "Arrecife Triángulo Oeste (México), "
                                "algunos reportes en Cuba y Jamaica"
            }
        }

        self.scores = {
            "Millepora alcicornis": 0,
            "Millepora complanata": 0,
            "Millepora squarrosa": 0
        }

    @Rule(CoralCharacteristic(forma="ramificada"), CoralCharacteristic(ramas=MATCH.ramas))
    def puntuar_alcicornis_forma(self, ramas):
        if ramas in ["cilindricas", "aplanadas"]:
            self.scores["Millepora alcicornis"] += 30
            self.diagnostic_features.append("Forma ramificada con ramas cilíndricas o aplanadas")

    @Rule(CoralCharacteristic(color=MATCH.color))
    def puntuar_alcicornis_color(self, color):
        if color in ["amarillo", "naranja"]:
            self.scores["Millepora alcicornis"] += 20
            self.diagnostic_features.append(f"Color {color}")

    @Rule(CoralCharacteristic(oleaje="fuerte"))
    def puntuar_alcicornis_oleaje(self):
        self.scores["Millepora alcicornis"] += 20
        self.diagnostic_features.append("Habita en zonas de oleaje fuerte")

    @Rule(CoralCharacteristic(forma="laminar"), CoralCharacteristic(estructura=MATCH.estructura))
    def puntuar_complanata_forma(self, estructura):
        if estructura in ["abanico", "cresta"]:
            self.scores["Millepora complanata"] += 30
            self.diagnostic_features.append("Forma laminar en abanico o cresta")

    @Rule(CoralCharacteristic(color=MATCH.color))
    def puntuar_complanata_color(self, color):
        if color in ["amarillo", "marron_claro"]:
            self.scores["Millepora complanata"] += 20
            self.diagnostic_features.append(f"Color {color}")

    @Rule(CoralCharacteristic(oleaje=MATCH.oleaje))
    def puntuar_complanata_oleaje(self, oleaje):
        if oleaje in ["moderado", "fuerte"]:
            self.scores["Millepora complanata"] += 20
            self.diagnostic_features.append(f"Habita en zonas de oleaje {oleaje}")

    @Rule(CoralCharacteristic(forma="aplanada"), CoralCharacteristic(superficie="protuberancias"))
    def puntuar_squarrosa_forma(self):
        self.scores["Millepora squarrosa"] += 30
        self.diagnostic_features.append("Forma aplanada con protuberancias")

    @Rule(CoralCharacteristic(color=MATCH.color))
    def puntuar_squarrosa_color(self, color):
        if color in ["marron_claro", "beige"]:
            self.scores["Millepora squarrosa"] += 20
            self.diagnostic_features.append(f"Color {color}")

    @Rule(CoralCharacteristic(habitat="someras"))
    def puntuar_squarrosa_habitat(self):
        self.scores["Millepora squarrosa"] += 20
        self.diagnostic_features.append("Habita en aguas someras")

    @Rule(NOT(IdentificationResult()))
    def evaluar_puntuaciones(self):
        max_score = max(self.scores.values())
        if max_score > 40:
            for species, score in self.scores.items():
                if score == max_score:
                    self.identified_species = species
                    self.confidence = max_score / 100
                    self.declare(IdentificationResult(
                        species=species,
                        confidence=self.confidence,
                        info=self.species_info[species]
                    ))
                    self.diagnostic_features.append(f"Identificado por puntuación: {species}")
        else:
            self.declare(IdentificationResult(
                species="Indeterminado",
                confidence=0.0,
                info={"description": "No hay suficientes datos para identificar la especie."}
            ))
