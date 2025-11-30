class ListStack:
	"""Стек на основе списка"""
	
	def __init__(self):
		self._items = []
	
	def push(self, x: int) -> None:
		"""Добавление элемента в стек"""
		self._items.append(x)
	
	def pop(self) -> int:
		"""Извлечение элемента из стека"""
		if self.is_empty():
			raise IndexError("pop from empty stack")
		return self._items.pop()
	
	def peek(self) -> int:
		"""Просмотр верхнего элемента без извлечения"""
		if self.is_empty():
			raise IndexError("peek from empty stack")
		return self._items[-1]
	
	def is_empty(self) -> bool:
		"""Проверка на пустоту"""
		return len(self._items) == 0
	
	def __len__(self) -> int:
		"""Количество элементов в стеке"""
		return len(self._items)