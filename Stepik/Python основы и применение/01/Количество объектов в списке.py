# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 16:09:16 2018
Реализуйте программу, которая будет вычислять количество различных
 объектов в списке.
Два объекта a и b считаются различными, если a is b равно False.

Вашей программе доступна переменная с названием objects, 
которая ссылается на список, содержащий не более 100 объектов. Выведите количество различных объектов в этом списке.

Формат ожидаемой программы:

ans = 0
for obj in objects: # доступная переменная objects
    ans += 1

print(ans)

Примечание:
Количеством различных объектов называется максимальный размер 
множества объектов, в котором любые два объекта являются различными.

Рассмотрим пример:
objects = [1, 2, 1, 2, 3] # будем считать, что одинаковые числа 
соответствуют одинаковым объектам, а различные – различным

Тогда все различные объекты являют собой множество {1, 2, 3}﻿. 
Таким образом, количество различных объектов равно трём.
@author: user
"""
import ctypes

objects = [1, 2, 1, 2, 3, True, False, '', 0, [1, 2], [1, 2]]
st = set()
for obj in objects:
    st.add(id(obj))
print(len(st))

st1 = list()
for i in st:
    st1.append(ctypes.cast(i, ctypes.py_object).value)
print(objects)
print(st)
print(st1)

print(len(set(map(id, objects))))
