# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 11:01:51 2018

@author: user
"""

# Локальные пространства имен не создаются когда мы используем оператор выбора
# или цикл

x = 13
if x % 2 == 1:
    x += 1
print(x)

for i in range(5):
    x = i*i
print(x)

try:
    for i in []:
        y = i*i
    print(y)
except NameError as err:
    print(err)
