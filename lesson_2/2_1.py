# 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт
# проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = [12, 126.1, 'hello', [2, 7, 9], (14, 12, 13), {1, 6, 9}, {1: 2, 2: 7, 9: 11}]

for i in range(len(my_list)):
    print(f'Элемент {my_list[i]} тип данных {type(my_list[i])}')
