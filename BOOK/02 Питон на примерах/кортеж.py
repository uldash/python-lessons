# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 14:08:55 2018

@author: user
"""

# Пустой кортеж
a = tuple()
print(a)

d = tuple("Python")
print(d)
b = tuple([1, 2, 3, 4, 5])
print(b)

a = b + (40, [1, 2, 3], 60)
print(a)
print(a[2:5])
