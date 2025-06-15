import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 4), -4)

   def test_multiplication(self):
    self.assertEqual(self.calc.multiply(2, 3), 6)
    self.assertEqual(self.calc.multiply(-1, 5), -5)
       
   def test_division(self):
    self.assertEqual(self.calc.divide(10, 2), 5)
    self.assertEqual(self.calc.divide(5, 2), 2.5)
    self.assertIsNone(self.calc.divide(5, 0))  



    def test_divide_by_zero(self):
        """Test division by zero returns None."""
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(0, 0))

if __name__ == '__main__':
    unittest.main()
