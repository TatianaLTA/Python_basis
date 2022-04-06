# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker:
    def __init__(self, n, s, p, w, b):
        self.name = n
        self.surname = s
        self.position = p
        self._income = {'wage': w, 'bonus': b}


class Position(Worker):
    def get_full_name(self):
        full_name = self.name + ' ' + self.surname
        print(full_name)

    def get_total_income(self):
        try:
            total_income = (int(self._income['wage']) + int(self._income['bonus']))
            print(f'Суммарный доход равен {total_income}')
        except ValueError:
            print('Заданы неверные значения параметров')


position_1 = Position('Ivan', 'Petrov', 'driver', 10000, 5000)
print(position_1.name)
print(position_1.surname)
print(position_1.position)
print(position_1._income)
position_1.get_full_name()
position_1.get_total_income()
