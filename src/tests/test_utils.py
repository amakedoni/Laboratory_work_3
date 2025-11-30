import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import timeit_once, benchmark_math_functions, benchmark_sorts
from math_functions import factorial, fibo
from sorting import bubble_sort

class TestBenchmark(unittest.TestCase):
	
	def test_timeit_once(self):
		"""Тест измерения времени выполнения"""
		def dummy_func():
			return sum(range(1000))
		
		time_taken = timeit_once(dummy_func)
		self.assertIsInstance(time_taken, float)
		self.assertGreater(time_taken, 0)
	
	def test_benchmark_math_functions(self):
		"""Тест бенчмарка математических функций"""
		values = [5, 10]
		algos = {
			"factorial": factorial,
			"fibo": fibo
		}
		
		results = benchmark_math_functions(values, algos)
		
		self.assertIn("factorial", results)
		self.assertIn("fibo", results)
		self.assertIn(5, results["factorial"])
		self.assertIn(10, results["fibo"])
		
		for func_name, timings in results.items():
			for value, time_taken in timings.items():
				self.assertIsInstance(time_taken, float)
				self.assertGreaterEqual(time_taken, 0)
	
	def test_benchmark_sorts(self):
		"""Тест бенчмарка сортировок"""
		arrays = {
			"test1": [3, 1, 4, 2],
			"test2": [5, 4, 3, 2, 1]
		}
		algos = {
			"bubble_sort": bubble_sort
		}
			
		results = benchmark_sorts(arrays, algos)
		
		self.assertIn("test1", results)
		self.assertIn("test2", results)
		self.assertIn("bubble_sort", results["test1"])
		
		for array_name, timings in results.items():
			for algo_name, time_taken in timings.items():
				self.assertIsInstance(time_taken, float)
				self.assertGreaterEqual(time_taken, 0)

if __name__ == '__main__':
	unittest.main()