# 1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд,
# второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов.
# При его нарушении выводить соответствующее сообщение и завершать скрипт.
import time
from itertools import cycle


class TrafficLight:
    __color = 'red'

    def running(self):
        n = 0
        for c in cycle(['red', 'yellow', 'green', 'yellow']):
            if n > 10:
                break
            self.__color = c
            #print(self.__color)
            n += 1
            if c == 'red':
                print('\033[31m {}'.format(self.__color))
                time.sleep(7)
            elif c == 'yellow':
                print('\033[33m {}'.format(self.__color))
                time.sleep(2)
            else:
                print('\033[32m {}'.format(self.__color))
                time.sleep(10)


my_traffic_light = TrafficLight()
my_traffic_light.running()
