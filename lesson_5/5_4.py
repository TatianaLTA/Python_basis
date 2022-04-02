# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

with open('text_4.txt', 'r', encoding='utf-8') as f:
    content = f.readlines()
    ss = []
    numbers = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

    for s in content:
        s_i = s.split()
        s_i[0] = numbers[s_i[0]]
        ss.append(s_i)

    print(ss)

with open('text_4_red.txt', 'w', encoding='utf-8') as f_1:
    for n in ss:
        p = ' '.join(n)
        print(p)
        f_1.write(str(p)+'\n')

