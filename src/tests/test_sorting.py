import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sorting import bubble_sort, quick_sort, counting_sort, radix_sort, bucket_sort, heap_sort

class TestSorting(unittest.TestCase):
	
	def setUp(self):
		self.test_arrays = {
			'empty': [],
			'single': [5],
			'sorted': [1, 2, 3, 4, 5],
			'reverse': [5, 4, 3, 2, 1],
			'random': [64, 34, 25, 12, 22, 11, 90],
			'duplicates': [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],
		}
		self.float_array = [0.42, 0.32, 0.67, 0.89, 0.11, 0.53]
	
	def test_bubble_sort(self):
		for name, arr in self.test_arrays.items():
			with self.subTest(array=name):
				sorted_arr = bubble_sort(arr)
				self.assertEqual(sorted_arr, sorted(arr))
	
	def test_quick_sort(self):
		for name, arr in self.test_arrays.items():
			with self.subTest(array=name):
				sorted_arr = quick_sort(arr)
				self.assertEqual(sorted_arr, sorted(arr))
	
	def test_counting_sort(self):
		for name, arr in self.test_arrays.items():
			with self.subTest(array=name):
				sorted_arr = counting_sort(arr)
				self.assertEqual(sorted_arr, sorted(arr))
	
	def test_radix_sort(self):
		for name, arr in self.test_arrays.items():
			with self.subTest(array=name):
				sorted_arr = radix_sort(arr)
				self.assertEqual(sorted_arr, sorted(arr))
	
	def test_bucket_sort(self):
		sorted_floats = bucket_sort(self.float_array)
		self.assertEqual(sorted_floats, sorted(self.float_array))
			
		with self.assertRaises(ValueError):
			bucket_sort([1.5, 0.3])  
	
	def test_heap_sort(self):
		for name, arr in self.test_arrays.items():
			with self.subTest(array=name):
				sorted_arr = heap_sort(arr)
				self.assertEqual(sorted_arr, sorted(arr))

if __name__ == '__main__':
	unittest.main()