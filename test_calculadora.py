"""
Sergio Perez Sanchez - test_calculadora.py
"""

import calculadora

def test_suma():
	assert 8 == calculadora.suma(4, 4)

def test_resta():
	assert 2 == calculadora.resta(5, 3)

if __name__ == "__main__":
	test_suma();
	test_resta()
	print("Los Tests se han ejecutado correctamente")