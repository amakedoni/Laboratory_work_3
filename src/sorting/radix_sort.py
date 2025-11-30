def radix_sort(a: list[int], base: int = 10) -> list[int]:
	"""Поразрядная сортировка"""
	if not a:
		return []
	
	arr = a.copy()
	max_val = max(arr)
	
	exp = 1
	while max_val // exp > 0:
		buckets = [[] for i in range(base)]
			
		for num in arr:
			digit = (num // exp) % base
			buckets[digit].append(num)
			
		arr = []
		for bucket in buckets:
			arr.extend(bucket)
			
		exp *= base
	
	return arr