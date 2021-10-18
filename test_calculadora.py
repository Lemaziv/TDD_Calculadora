import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):

    def setUp(self):
        self.calc = Calculadora()

    def test_la_suma_de_5_mas_5_debe_dar_10(self):
        self.calc.suma(5,5)
        self.assertEqual(10, self.calc.valor())

    def test_la_resta_de_4_menos_2_debe_dar_2(self):
        self.calc.resta(4,2)
        self.assertEqual(2, self.calc.valor())

    def test_la_multiplicacion_de_8_por_3_debe_dar_24(self):
        self.calc.multiplicacion(8,3)
        self.assertEqual(24, self.calc.valor())

    def test_la_division_de_6_entre_2_debe_dar_3(self):
        self.calc.division(6,2)
        self.assertEqual(3, self.calc.valor())