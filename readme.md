# Лабораторная работа №3: Алгоритмический мини-пакет

## Оглавление
- [Описание](#описание)
- [Структура проекта](#структура-проекта)
- [Установка и запуск](#установка-и-запуск)
- [Компоненты проекта](#компоненты-проекта)
- [Тестирование](#тестирование)

## Описание

Этот проект реализует алгоритмический мини-пакет, включающий:
- **Математические функции** (факториал и числа Фибоначчи)
- **Алгоритмы сортировки** (6 различных видов)
- **Структуры данных** (3 реализации стека)
- **Инструменты бенчмаркинга** для измерения производительности

## Структура проекта
```src/
├── main.py # Главный демонстрационный файл
├── math_functions/ # Математические функции
│ ├── init.py
│ └── factorial_fibonacci.py
├── sorting/ # Алгоритмы сортировки
│ ├── init.py
│ ├── bubble_sort.py
│ ├── quick_sort.py
│ ├── counting_sort.py
│ ├── radix_sort.py
│ ├── bucket_sort.py
│ └── heap_sort.py
├── data_structures/ # Структуры данных
│ ├── init.py
│ └── stack/
│ ├── init.py
│ ├── list_stack.py
│ ├── linked_list_stack.py
│ └── queue_stack.py
├── utils/ # Вспомогательные инструменты
│ ├── init.py
│ └── benchmark.py
└── tests/ # Unit-тесты
├── init.py
├── test_math.py
├── test_sorting.py
└── test_utils.py
```

## Установка и запуск

1. **Клонируйте или скачайте проект** 
```bash
git clone https://github.com/amakedoni/Laboratory_work_3.git
cd Laboratory_work_3
cd src
```
2. **Запустите:**
```bash
python main.py
```

## Запуск отдельных компонентов

### Математические функции:

```python
from math_functions import factorial, fibo

print(factorial(5))  # 120
print(fibo(6))       # 8
```

### Сортировки:

```python
from sorting import bubble_sort, quick_sort

arr = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(arr))
print(quick_sort(arr))
```
### Структуры данных:

```python
from data_structures import ListStack

stack = ListStack()
stack.push(1)
stack.push(2)
print(stack.pop())  # 2
```

### Бенчмарки:

```python
from utils import benchmark_math_functions
from math_functions import factorial, fibo

results = benchmark_math_functions(
    [5, 10, 15], 
    {"factorial": factorial, "fibo": fibo}
)
```

## Компоненты проекта

### 1. Математические функции
```
Функция	Описание	Сложность
factorial(n)	Итеративный факториал	O(n)
factorial_recursive(n)	Рекурсивный факториал	O(n)
fibo(n)	Итеративное число Фибоначчи	O(n)
fibo_recursive(n)	Рекурсивное число Фибоначчи	O(2ⁿ)
```

### 2. Алгоритмы сортировки
```
Алгоритм	Тип	Сложность	Примечания
bubble_sort()	Сравнение	O(n²)	Стабильный
quick_sort()	Разделение	O(n log n)	Нестабильный
counting_sort()	Подсчет	O(n + k)	Только целые числа
radix_sort()	Поразрядная	O(d(n + k))	Основание настраивается
bucket_sort()	Ведерная	O(n + k)	Только float [0,1)
heap_sort()	Пирамидальная	O(n log n)	На месте
```

### 3. Структуры данных (Стек)
```
Реализация	Методы	Особенности
ListStack	push(), pop(), peek()	На основе списка
LinkedListStack	push(), pop(), peek()	На связном списке
QueueStack	push(), pop(), peek()	На двух очередях
```


### 4. Бенчмарки
```
Функция	Назначение
timeit_once(func)	Измерение времени выполнения
benchmark_math_functions()	Сравнение математических функций
benchmark_sorts()	Сравнение алгоритмов сортировки
```

## Тестирование

### Запуск всех тестов (из папки src)

```bash
python -m unittest discover tests
```

### Запуск отдельных тестов (из папки src)

```bash
# Тесты математических функций
python -m unittest tests.test_math

# Тесты сортировок
python -m unittest tests.test_sorting

# Тесты бенчмарков
python -m unittest tests.test_utils
```

### Запуск тестов с детализацией (из папки src)

```bash
python -m unittest discover tests -v
```


## Практические задачи (в папке leetcode)

