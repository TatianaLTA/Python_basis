# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 19:32:32 2022

@author: User

4. Пользователь вводит целое положительное число. 
Найдите самую большую цифру в числе. 
Для решения используйте цикл while и арифметические операции.
"""
number = int(input('Введите целое положительное число: '))
max_digit = 0

while number > 10:
    digit = number % 10
    number = number // 10
    if digit > max_digit:
        max_digit = digit
        
if number > max_digit:
    max_digit = number
       
print('Самая большая цифра в числе: ', max_digit)
        