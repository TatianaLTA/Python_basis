# 6. Сформировать (не программно) текстовый файл.
# В нём каждая строка должна описывать учебный предмет и наличие лекционных, практических
# и лабораторных занятий по предмету. Сюда должно входить и количество занятий.
# Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

with open('text_6.txt', 'r', encoding='utf-8') as f:
    content = f.readlines()
    #print(content)
    content_1 =[]
    for s in content:
        s_1 = s.split(':')
        content_1.append(s_1)
    #print(content_1)
    res_dict = {}

    for n in content_1:
        n_1 = n[1].split(' ')
        #print(n_1)
        hours = 0
        for part in n_1:
            numbs = [numb for numb in part if numb.isdigit()]
            #print(numbs)
            numb_part = ''
            for r in numbs:
                numb_part = numb_part + r
            #print(numb_part)
            try:
                hours += int(numb_part)
            except ValueError:
                pass
        res_dict[n[0]] = hours
    print(res_dict)
