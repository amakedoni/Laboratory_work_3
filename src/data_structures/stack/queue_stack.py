from collections import deque

class QueueStack:
	"""Стек на основе очередей"""
	
	def __init__(self):
		self._q1 = deque()
		self._q2 = deque()
	
	def push(self, x: int) -> None:
		"""Добавление элемента в стек"""
		self._q2.append(x)
			
		while self._q1:
			self._q2.append(self._q1.popleft())
			
		self._q1, self._q2 = self._q2, self._q1
	
	def pop(self) -> int:
		"""Извлечение элемента из стека"""
		if self.is_empty():
			raise IndexError("pop from empty stack")
		return self._q1.popleft()
	
	def peek(self) -> int:
		"""Просмотр верхнего элемента без извлечения"""
		if self.is_empty():
			raise IndexError("peek from empty stack")
		return self._q1[0]
	
	def is_empty(self) -> bool:
		"""Проверка на пустоту"""
		return len(self._q1) == 0
	
	def __len__(self) -> int:
		"""Количество элементов в стеке"""
		return len(self._q1)