# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
# (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Data:
    def __init__(self, d):
        self.data = d
        self.day = None
        self.month = None
        self.year = None
        try:
            self.day = self.numbers(self.data)[0]
            self.month = self.numbers(self.data)[1]
            self.year = self.numbers(self.data)[2]
            Data.validation(self.numbers(self.data))
        except TypeError:
            print('Data should consists of integer numbers!')

    @classmethod
    def numbers(cls, dat):
        try:
            numbers = list(map(int, dat.split('-')))
            return numbers
        except TypeError:
            print('Data should consists of integer numbers!')
        except ValueError:
            print('Data should consists of integer numbers!')

    @staticmethod
    def validation(numbers):
        if numbers[0] < 0 or numbers[0] > 31:
            print('Wrong day')
        if numbers[1] < 0 or numbers[1] > 12:
            print('Wrong month')
        if numbers[2] <= 0 or numbers[2] > 9999:
            print('Wrong year')


my_data = Data('13-10-2012')
print(f'Day {my_data.day}')
print(f'Month {my_data.month}')
print(f'Year {my_data.year}')
