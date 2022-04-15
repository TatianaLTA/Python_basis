# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class ZeroDevExFunc(Exception):
    def __init__(self, txt):
        self.txt = txt


def divide_xy(x, y):
    if y == 0:
        raise ZeroDevExFunc('Попытка деления на ноль!')
    else:
        return f'{x} / {y} = {x/y:.2f}'


try:
    res = divide_xy(5, 0)
    print(res)
except ZeroDevExFunc as err:
    print(err)


res = divide_xy(5, 3)
print(res)

res = divide_xy(12, 2)
print(res)
