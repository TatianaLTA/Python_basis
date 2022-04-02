# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

with open('user_text.txt', 'r', encoding='utf-8') as f:
    content = f.readlines()
    print(f'Количество строк в файле равно {len(content)}')
    for i, val in enumerate(content):
        i_str = val.split()
        print(f'Количество слов в строке {i+1} равно {len(i_str)}')
        