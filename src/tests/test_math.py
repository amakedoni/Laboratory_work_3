import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from math_functions import factorial, factorial_recursive, fibo, fibo_recursive

class TestMathFunctions(unittest.TestCase):
	
	def test_factorial(self):
		self.assertEqual(factorial(0), 1)
		self.assertEqual(factorial(1), 1)
		self.assertEqual(factorial(5), 120)
		self.assertEqual(factorial(7), 5040)
	
	def test_factorial_recursive(self):
		self.assertEqual(factorial_recursive(0), 1)
		self.assertEqual(factorial_recursive(1), 1)
		self.assertEqual(factorial_recursive(5), 120)
	
	def test_factorial_negative(self):
		with self.assertRaises(ValueError):
			factorial(-1)
		with self.assertRaises(ValueError):
			factorial_recursive(-5)
	
	def test_fibo(self):
		self.assertEqual(fibo(0), 0)
		self.assertEqual(fibo(1), 1)
		self.assertEqual(fibo(6), 8)
		self.assertEqual(fibo(10), 55)
	
	def test_fibo_recursive(self):
		self.assertEqual(fibo_recursive(0), 0)
		self.assertEqual(fibo_recursive(1), 1)
		self.assertEqual(fibo_recursive(6), 8)
	
	def test_fibo_negative(self):
		with self.assertRaises(ValueError):
			fibo(-1)
		with self.assertRaises(ValueError):
			fibo_recursive(-5)

if __name__ == '__main__':
	unittest.main()