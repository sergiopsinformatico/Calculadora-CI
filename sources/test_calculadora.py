"""
Sergio Perez Sanchez - test_calculadora.py
"""

import calculadora
import unittest

class TestCalculatorMethods(unittest.TestCase):

	def test_suma(self):
		self.assertEqual(8, calculadora.suma(4, 4))

	def test_resta(self):
		self.assertEqual(2, calculadora.resta(5, 3))

if __name__ == '__main__':
    unittest.main()