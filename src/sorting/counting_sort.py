def counting_sort(a: list[int]) -> list[int]:
	"""Сортировка подсчетом"""
	if not a:
		return []
	
	min_val = min(a)
	max_val = max(a)
	
	count = [0] * (max_val - min_val + 1)
	
	for num in a:
		count[num - min_val] += 1
	
	result = []
	for i in range(len(count)):
		result.extend([i + min_val] * count[i])
	
	return result