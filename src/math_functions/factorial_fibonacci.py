def factorial(n: int) -> int:
	if n < 0:
		raise ValueError(f"Число n: {n} должно быть положительным")
	
	res = 1
	for i in range(1, n + 1):
		res *= i

	return res

def factorial_recursive(n: int) -> int:
	if n < 0:
		raise ValueError(f"Число n: {n} должно быть положительным")
	
	if n == 0:
		return 1
	
	else:
		return n * factorial_recursive(n - 1)

def fibo(n: int) -> int:
	if n < 0:
		raise ValueError(f"Число n: {n} должно быть положительным")
	
	if n <= 1:
		return n

	a, b = 0, 1
	for i in range(2, n + 1):
		a, b = b, a + b
	
	return b

def fibo_recursive(n:int) -> int:
	if n < 0:
		raise ValueError(f"Число n: {n} должно быть положительным")
	
	if n <= 1:
		return n
	
	return fibo_recursive(n - 1) + fibo_recursive(n - 2)
