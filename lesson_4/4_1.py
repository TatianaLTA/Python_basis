# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

script_name, hours, cost, bonus = argv

try:
    salary = (int(hours) * int(cost)) + int(bonus)
    print(f'Salary is {salary}')
except TypeError:
    print('Enter integer values')
except ValueError:
    print('Enter integer values')
