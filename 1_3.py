# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 19:23:11 2022

@author: User

3. Узнайте у пользователя число n. 
Найдите сумму чисел n + nn + nnn. 
Например, пользователь ввёл число 3. 
Считаем 3 + 33 + 333 = 369.
"""

n = int(input('Введите число: '))
nn = int(str(n)+str(n))
nnn = int(str(n)+str(n)+str(n))

result = n + nn + nnn

print(f"Сумма {n} + {nn} + {nnn} = ", result)
