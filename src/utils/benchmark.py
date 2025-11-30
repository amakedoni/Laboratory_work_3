import time
from typing import Dict, List, Callable, Any

def timeit_once(func: Callable, *args, **kwargs) -> float:
	"""
	Измеряет время выполнения функции один раз
	
	Args:
		func: Функция для измерения
		*args: Аргументы функции
		**kwargs: Именованные аргументы функции
			
	Returns:
		Время выполнения в секундах
	"""
	start_time = time.perf_counter()
	result = func(*args, **kwargs)  
	end_time = time.perf_counter()
	return end_time - start_time

def benchmark_math_functions(values: List[int], algos: Dict[str, Callable]) -> Dict[str, Dict[int, float]]:
	"""
	Бенчмарк для математических функций (факториал и Фибоначчи)
	
	Args:
		values: Список значений для тестирования
		algos: Словарь с математическими функциями {имя: функция}
			
	Returns:
		Словарь с результатами timing {имя_функции: {значение: время}}
	"""
	results = {}
	
	for algo_name, algo_func in algos.items():
		results[algo_name] = {}
			
		for value in values:
			try:
				time_taken = timeit_once(algo_func, value)
				results[algo_name][value] = time_taken
			except Exception as e:
				print(f"Ошибка в {algo_name} со значением {value}: {e}")
				results[algo_name][value] = float('inf')
	
	return results

def benchmark_sorts(arrays: Dict[str, List], algos: Dict[str, Callable]) -> Dict[str, Dict[str, float]]:
	"""
	Бенчмарк для сортировок
	
	Args:
		arrays: Словарь с тестовыми массивами {имя: массив}
		algos: Словарь с алгоритмами сортировки {имя: функция}
			
	Returns:
		Словарь с результатами timing {имя_массива: {имя_алгоритма: время}}
	"""
	results = {}
	
	for array_name, array in arrays.items():
		results[array_name] = {}
			
		for algo_name, algo_func in algos.items():
			try:
				time_taken = timeit_once(algo_func, array)
				results[array_name][algo_name] = time_taken
			except Exception as e:
				print(f"Ошибка в {algo_name} с массивом {array_name}: {e}")
				results[array_name][algo_name] = float('inf')
	
	return results