# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 16:47:04 2018

@author: user
"""

s = [i * (10 - i) for i in range(11)]
print(s)
print("Удаляем элемент", s.pop(5), "\n", s)
print("Удаляем элемент со значением 21", s.remove(21), "\n", s)
print("Удаляем из списка элемент с индексом 3")
del s[3]
print(s)
print("Удаляем несколько элементов в списке")
s[2:5] = []
print(s)
s[1:3] = [-1, -2, -3, -4, -5]
print(s)
print(0 in s)
print(s.index(0, 4))
