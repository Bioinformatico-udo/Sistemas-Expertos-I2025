import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
from millepora_expert import MilleporaExpert, CoralCharacteristic

class TestMilleporaExpert(unittest.TestCase):

    def setUp(self):
         # Crear instancia del motor
        self.expert = MilleporaExpert()

    # Ejemplo de uso - Caso 1: M. alcicornis
    # CASO 1: Identificación de muestra ramificada
    def test_millepora_alcicornis(self):
        self.expert.reset()
        self.expert.declare(CoralCharacteristic(superficie='con_poros'))
        self.expert.declare(CoralCharacteristic(septa='ausentes'))
        self.expert.declare(CoralCharacteristic(forma_colonia='ramificada'))
        self.expert.declare(CoralCharacteristic(forma_ramas='delgadas_aplanadas'))
        self.expert.declare(CoralCharacteristic(espesor_ramas='10-15mm'))
        self.expert.declare(CoralCharacteristic(color='amarillo-naranja'))
        self.expert.declare(CoralCharacteristic(profundidad='0-50m'))
        self.expert.declare(CoralCharacteristic(habitat='aguas_tranquilas_agitadas'))
        self.expert.run()
        self.assertEqual(self.expert.identified_species, 'Millepora alcicornis')
        self.assertGreaterEqual(self.expert.confidence, 0.85)

    # Ejemplo de uso - Caso 2: M. complanata
    # CASO 2: Identificación de muestra laminar
    def test_millepora_complanata(self):
        self.expert.reset()
        self.expert.declare(CoralCharacteristic(superficie='con_poros'))
        self.expert.declare(CoralCharacteristic(septa='ausentes'))
        self.expert.declare(CoralCharacteristic(forma_colonia='laminar'))
        self.expert.declare(CoralCharacteristic(forma_ramas='hojas_delgadas'))
        self.expert.declare(CoralCharacteristic(base='incrustante'))
        self.expert.declare(CoralCharacteristic(color='mostaza_marron'))
        self.expert.declare(CoralCharacteristic(profundidad='0-15m'))
        self.expert.declare(CoralCharacteristic(habitat='arrecifes_poco_profundos'))
        self.expert.run()
        self.assertEqual(self.expert.identified_species, 'Millepora complanata')
        self.assertGreaterEqual(self.expert.confidence, 0.85)

    # Ejemplo de uso - Caso 3: M. squarrosa
    # CASO 3: Identificación de muestra boxwork
    def test_millepora_squarrosa(self):
        self.expert.reset()
        self.expert.declare(CoralCharacteristic(superficie='con_poros'))
        self.expert.declare(CoralCharacteristic(septa='ausentes'))
        self.expert.declare(CoralCharacteristic(forma_colonia='boxwork'))
        self.expert.declare(CoralCharacteristic(forma_ramas='robustas_interconectadas'))
        self.expert.declare(CoralCharacteristic(superficie='rugosa'))
        self.expert.run()
        self.assertEqual(self.expert.identified_species, 'Millepora squarrosa')
        self.assertGreaterEqual(self.expert.confidence, 0.80)

    # Ejemplo de uso - Caso 3: Coral desconocido.
    def test_coral_desconocido(self):
        self.expert.reset()
        self.expert.declare(CoralCharacteristic(superficie='sin_poros'))
        self.expert.declare(CoralCharacteristic(septa='presentes'))
        self.expert.declare(CoralCharacteristic(forma_colonia='desconocida'))
        self.expert.declare(CoralCharacteristic(color='desconocido'))
        self.expert.run()
        self.assertIsNone(self.expert.identified_species)
        self.assertEqual(self.expert.confidence, 0.0)

if __name__ == '__main__':
    unittest.main()
