# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    name = ''

    @abstractmethod
    def __init__(self, r):
        self.size = r

    @abstractmethod
    def textile_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    def textile_consumption(self):
        res = (self.size / 6.5 + 0.5)
        return res


class Suit(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def textile_consumption(self):
        res = (2 * self.height + 0.3)
        return res


my_coat = Coat(44)
print(my_coat.textile_consumption())

my_suit = Suit(169)
print(my_suit.textile_consumption)

print(my_coat.textile_consumption() + my_suit.textile_consumption)