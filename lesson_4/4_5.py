# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти чётные числа от 100 до 1000 (включая границы).
# Нужно получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().
from functools import reduce

numbers = [n for n in range(100, 1001) if n % 2 == 0]
print(numbers)
multiple_all = reduce(lambda x,y: x * y, numbers)
print(f'Result = {multiple_all}')