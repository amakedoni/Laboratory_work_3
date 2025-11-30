def _sort_bucket(bucket: list[float]) -> list[float]:
	"""Вспомогательная функция для сортировки ведра (используем пузырьковую сортировку)"""
	arr = bucket.copy()
	n = len(arr)
	for i in range(n):
		swapped = False
		for j in range(0, n - i - 1):
			if arr[j] > arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
				swapped = True
		if not swapped:
			break
	return arr

def bucket_sort(a: list[float], buckets: int | None = None) -> list[float]:
	"""Ведерная сортировка для float в диапазоне [0, 1)"""
	if not a:
		return []
	
	arr = a.copy()
	
	for num in arr:
		if num < 0 or num >= 1:
			raise ValueError("Сортировка ведром требует дипазон [0, 1)")
	
	n = len(arr)
	if buckets is None:
		buckets = n
	
	bucket_list = [[] for _ in range(buckets)]
	
	for num in arr:
		index = int(num * buckets)
		if index == buckets:  #
			index = buckets - 1
		bucket_list[index].append(num)
	
	for i in range(buckets):
		bucket_list[i] = _sort_bucket(bucket_list[i])
	
	result = []
	for bucket in bucket_list:
		result.extend(bucket)
	
	return result