# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает
# сумму наибольших двух аргументов.

def sum_max(n_1, n_2, n_3):
    if n_1.isdigit() and n_2.isdigit() and n_3.isdigit():
        n_1 = float(n_1)
        n_2 = float(n_2)
        n_3 = float(n_3)
        numbers = [n_1, n_2, n_3]
        min_n = min(numbers)
        sum_max_n = n_1 + n_2 + n_3 - min_n
        print(f'Сумма двух наибольших аргументов равна {sum_max_n}')
        return sum_max_n
    else:
        print('Ошибка ввода')

result = sum_max(input('Введите первое число: '), input('Введите второе число: '), input('Введите третье число: '))


