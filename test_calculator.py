import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_add_2(self):
        self.assertEqual(self.calc.add(10,-20),-10)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(-20,-10),-10)

    def test_subtract_2(self):
        self.assertEqual(self.calc.subtract(-20,-50),30)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3,2),6)

    def test_multiply_2(self):
        self.assertEqual(self.calc.multiply(-20,5),-100)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10,2),5)

    def test_divide_2(self):
        self.assertEqual(self.calc.divide(-20,2),-10)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(-20,5),0)

    def test_modulo_2(self):
        self.assertEqual(self.calc.modulo(2,5),2)

    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main(verbosity=2)