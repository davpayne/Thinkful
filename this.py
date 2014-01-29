import unittest
from Calculator import Calculator
class TddInPythonExample(unittest.TestCase):
	def setUp(self):
 		self.calc = Calculator()
 		
 	def test_calculator_add_method_returns_correct_result(self):
		calc = Calculator()
		result = self.calc.add(2,2)
		self.assertEqual(4, result)