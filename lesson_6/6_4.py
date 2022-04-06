# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

class Car:
    def __init__(self, s, c, n, i=False):
        self.speed = s
        self.color = c
        self.name = n
        self.is_police = i

    def go(self):
        print(f'Car {self.name} is going with speed {self.speed}')

    def stop(self):
        print(f'Car {self.name} stopped')

    def turn(self, d='right'):
        print(f'Car {self.name} turned to the {d}')

    def show_speed(self):
        print(f'The current speed is {self.speed}')


class TownCar(Car):
    def show_speed(self):
        print(f'Скорость автомобиля {self.speed} км/ч')
        if self.speed > 60:
            print(f'Превышение скорости на {self.speed - 60} км/ч')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f'Скорость автомобиля {self.speed} км/ч')
        if self.speed > 40:
            print(f'Превышение скорости на {self.speed - 40} км/ч')


class PoliceCar(Car):
    def __init__(self, s, c, n):
        super().__init__(s, c, n)
        self.is_police = True


my_town_car = TownCar(70, 'blue', 'Mazda')
print(my_town_car.name)
print(my_town_car.speed)
print(my_town_car.color)
print(my_town_car.is_police)
my_town_car.go()
my_town_car.turn('left')
my_town_car.stop()
my_town_car.show_speed()

my_town_car = SportCar(200, 'red', 'Ferrary')
print(my_town_car.name)
print(my_town_car.speed)
print(my_town_car.color)
print(my_town_car.is_police)
my_town_car.go()
my_town_car.turn()
my_town_car.stop()
my_town_car.show_speed()

my_town_car = WorkCar(60, 'black', 'Huyndai')
print(my_town_car.name)
print(my_town_car.speed)
print(my_town_car.color)
print(my_town_car.is_police)
my_town_car.go()
my_town_car.turn('left')
my_town_car.stop()
my_town_car.show_speed()

my_town_car = PoliceCar(50, 'white', 'Lada')
print(my_town_car.name)
print(my_town_car.speed)
print(my_town_car.color)
print(my_town_car.is_police)
my_town_car.go()
my_town_car.turn()
my_town_car.stop()
my_town_car.show_speed()

