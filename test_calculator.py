import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def test_add_negative(self):
        self.assertEqual(self.calc.add(-1, -2), -3)
    def test_add_zero(self):
        self.assertEqual(self.calc.add(1,0), 1)

    # subtract
    def test_subtrac(self):
        self.assertEqual(self.calc.subtract(3, 3), 0)    
    def test_subtrac(self):
        self.assertEqual(self.calc.subtract(1, -2), 3)

    #multiply
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(10, 2), 20)
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(-5,2), -10) # type: ignore
    
    #divide
    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
    def test_divide(self):
        self.assertEqual(self.calc.divide(180, -6), -30)

    #modulo
    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)
    def test_modulo(self):
        self.assertEqual(self.calc.modulo(126, 5), 1)

    

if __name__ == '__main__':
    unittest.main()
