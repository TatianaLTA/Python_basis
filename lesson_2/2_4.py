# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое
# слово с новой строки. Строки нужно пронумеровать. Если слово длинное, выводить только
# первые 10 букв в слове.

sentense = input("Введите строку: ")
words = sentense.split(" ")
for i, v in enumerate(words):
    print(f'{i+1}) {words[i][:10]}')
