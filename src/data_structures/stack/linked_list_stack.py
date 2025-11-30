class _Node:
	"""Узел связного списка"""
	def __init__(self, value: int, next_node=None):
		self.value = value
		self.next = next_node

class LinkedListStack:
	"""Стек на основе связного списка"""
	
	def __init__(self):
		self._head = None
		self._size = 0
	
	def push(self, x: int) -> None:
		"""Добавление элемента в стек"""
		new_node = _Node(x, self._head)
		self._head = new_node
		self._size += 1
	
	def pop(self) -> int:
		"""Извлечение элемента из стека"""
		if self.is_empty():
			raise IndexError("pop from empty stack")
			
		value = self._head.value
		self._head = self._head.next
		self._size -= 1
		return value
	
	def peek(self) -> int:
		"""Просмотр верхнего элемента без извлечения"""
		if self.is_empty():
			raise IndexError("peek from empty stack")
		return self._head.value
	
	def is_empty(self) -> bool:
		"""Проверка на пустоту"""
		return self._head is None
	
	def __len__(self) -> int:
		"""Количество элементов в стеке"""
		return self._size