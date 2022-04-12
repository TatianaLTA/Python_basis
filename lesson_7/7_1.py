# 1. Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
#
# 31    32         3    5    32        3    5    8    3
# 37    43         2    4    6         8    3    7    1
# 51    86        -1   64   -8
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
# первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, d):
        self.data = d

    def __add__(self, other):
        if len(self.data) == len(other.data):
            result = []
            for i in range(len(self.data)):
                if len(self.data[i]) == len(other.data[i]):
                    c = [x + y for x, y in zip(self.data[i], other.data[i])]
                    result.append(c)
                else:
                    print('Matrixes must be the same dimension!')
            return Matrix(result)
        else:
            print('Matrixes must be the same dimension!')

    def __str__(self):
        data_1 = '\n'.join(map(str, self.data))
        data_2 = data_1.replace(',', ' ')
        data_3 = data_2.replace('[', '')
        data_4 = data_3.replace(']', '')
        return f'{data_4}'


my_matrix_1 = Matrix([[1, 2], [3, 4], [6, 7]])
print(my_matrix_1)
print('')

my_matrix_2 = Matrix([[11, 12], [13, 14], [16, 17]])
print(my_matrix_2)
print('')

print(my_matrix_1 + my_matrix_2)





