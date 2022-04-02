# 3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их
# окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч,
# вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
#
# Иванов 23543.12
# Петров 13749.32

with open('text_3.txt', 'r', encoding='utf-8') as f:
    content = f.readlines()
    data = []
    for i in content:
        d = i.split()
        data.append(d)
    print(data)

    data_dict = {}
    for n in data:
        data_dict[n[0]] = n[1]
    #print(data_dict)
    all_salary = 0
    print('Сотрудники с зарплатой менее 20000:')
    n = 0
    for key in data_dict.keys():
        try:
            salary = float(data_dict[key])
            all_salary += salary
        except ValueError:
            print('Неверное значение')
        except TypeError:
            print('Неверное значение')
        if salary < 20000:
            print(key)
            n += 1
    if n == 0:
        print('Отсутствуют')
    print(f'Средняя зарплата сотрудников равна {all_salary/len(data_dict)}')

