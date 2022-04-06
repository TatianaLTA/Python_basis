# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw.
# Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, t):
        self.title = t

    def start_draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def start_draw(self):
        print('Запуск отрисовки ручкой')


class Pencil(Stationery):
    def start_draw(self):
        print('Запуск отрисовки карандашом')


class Handle(Stationery):
    def start_draw(self):
        print('Запуск отрисовки маркером')


my_pen = Pen('Brauberg')
my_pen.start_draw()

my_pen = Pencil('Erich')
my_pen.start_draw()

my_pen = Handle('PC')
my_pen.start_draw()
