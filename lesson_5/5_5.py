# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

with open('numbers_5.txt', 'w+', encoding='utf-8') as f:
    numbers = input('Введите набор чисел, разделенных пробелами: ')
    f.write(numbers)
    f.seek(0)
    content = f.read().split()
    #print(content)
    sum_numbers = 0
    for n in content:
        try:
            n = float(n)
            sum_numbers += n
        except ValueError:
            print('При расчете суммы учитываются только числа. Введен другой символ')
    print(f'Сумма чисел = {sum_numbers}')

