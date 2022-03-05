# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 19:06:16 2022

@author: User

2. Пользователь вводит время в секундах. 
Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс. 
Используйте форматирование строк.
"""
time = int(input('Введите время в секундах: '))

hours = time // 3600
for_minutes = time % 3600
minutes = for_minutes // 60
secondes = for_minutes % 60

print(f'Время в формате чч:мм:сс - {hours:02d}:{minutes:02d}:{secondes:02d}')