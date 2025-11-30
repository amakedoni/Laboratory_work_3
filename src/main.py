"""
Главный файл лабораторной работы №3
"""
from math_functions import factorial, factorial_recursive, fibo, fibo_recursive
from sorting import bubble_sort, quick_sort, counting_sort, radix_sort, bucket_sort, heap_sort
from data_structures import ListStack, LinkedListStack, QueueStack
from utils import benchmark_math_functions, benchmark_sorts

def main():
	"""Демонстрация работы всех компонентов"""
	print("Лабораторная работа №3: Алгоритмический мини-пакет")
	
	# Тестирование математических функций
	print("\n=== Математические функции ===")
	print(f"Факториал 5: {factorial(5)}")
	print(f"Факториал рекурсивный 5: {factorial_recursive(5)}")
	print(f"Число Фибоначчи 6: {fibo(6)}")
	print(f"Число Фибоначчи рекурсивное 6: {fibo_recursive(6)}")
	
	# Бенчмарк математических функций
	print("\n=== Бенчмарк математических функций ===")
	math_values = [5, 10, 15, 20]
	math_algos = {
		"factorial": factorial,
		"factorial_recursive": factorial_recursive,
		"fibo": fibo,
		"fibo_recursive": fibo_recursive
	}
	
	math_results = benchmark_math_functions(math_values, math_algos)
	
	print("Результаты бенчмарка математических функций:")
	for func_name, timings in math_results.items():
		print(f"\n{func_name}:")
		for value, time_taken in timings.items():
			print(f"  n={value}: {time_taken:.6f} сек")
	
	# Тестирование сортировок
	print("\n=== Сортировки ===")
	test_array = [64, 34, 25, 12, 22, 11, 90]
	print(f"Исходный массив: {test_array}")
	print(f"Пузырьковая сортировка: {bubble_sort(test_array)}")
	print(f"Быстрая сортировка: {quick_sort(test_array)}")
	print(f"Сортировка подсчетом: {counting_sort(test_array)}")
	print(f"Поразрядная сортировка: {radix_sort(test_array)}")
	
	# Тестирование float массива для bucket sort
	float_array = [0.42, 0.32, 0.67, 0.89, 0.11, 0.53]
	print(f"Float массив: {float_array}")
	print(f"Ведерная сортировка: {bucket_sort(float_array)}")
	print(f"Пирамидальная сортировка: {heap_sort(test_array)}")
	
	# Бенчмарк сортировок
	print("\n=== Бенчмарк сортировок ===")
	arrays = {
		"small": [3, 1, 4, 1, 5, 9, 2, 6],
		"medium": [9, 2, 6, 5, 3, 5, 8, 9, 7, 1, 4, 2],
		"large": list(range(50, 0, -1)),  
	}
	sort_algos = {
		"bubble_sort": bubble_sort,
		"quick_sort": quick_sort,
		"counting_sort": counting_sort,
		"heap_sort": heap_sort,
	}
	
	sort_results = benchmark_sorts(arrays, sort_algos)
	print("Результаты бенчмарка сортировок:")
	for array_name, timings in sort_results.items():
		print(f"\n{array_name} (размер: {len(arrays[array_name])}):")
		for algo_name, time_taken in timings.items():
			print(f"  {algo_name}: {time_taken:.6f} сек")
	
	# Тестирование стеков
	print("\n=== Структуры данных (Стек) ===")
	
	print("1. Стек на списке:")
	stack1 = ListStack()
	stack1.push(1)
	stack1.push(2)
	stack1.push(3)
	print(f"   После push(1,2,3): peek={stack1.peek()}, len={len(stack1)}")
	print(f"   pop() = {stack1.pop()}")
	print(f"   После pop: peek={stack1.peek()}, len={len(stack1)}")
	
	print("2. Стек на связном списке:")
	stack2 = LinkedListStack()
	stack2.push(10)
	stack2.push(20)
	print(f"   После push(10,20): peek={stack2.peek()}, len={len(stack2)}")
	
	print("3. Стек на очередях:")
	stack3 = QueueStack()
	stack3.push(100)
	stack3.push(200)
	print(f"   После push(100,200): pop={stack3.pop()}")

if __name__ == "__main__":
	main()