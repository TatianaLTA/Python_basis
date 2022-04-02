# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка
# будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список.
# Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.
import json

with open('text_7.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()
    #print(data)
    res_dict_1 = {}
    all_profit = 0
    n = 0
    for d in data:
        d_1 = d.strip().split()
        #print(d_1)
        try:
            profit = int(d_1[2]) - int(d_1[3])
            res_dict_1[d_1[0]] = profit
            if profit > 0:
                all_profit += profit
                n += 1
        except ValueError:
            'Неверное значение заданного параметра'
    average_profit = {'average_profit': int(all_profit/n)}
    res = [res_dict_1, average_profit]
    print(res)

with open("text_7_j.json", "w", encoding='utf-8') as f_j:
    json.dump(res, f_j)

with open("text_7_j.json") as read_j:
    dat = json.load(read_j)
    print(dat)
    print(type(dat))


