# -*- coding: utf-8 -*-
"""
Created on Thu May 31 17:43:54 2018

@author: user
"""

print("Поиск совпадающих элементов.")
A = [2, False, 9.1, 2 - 1j, "hello", 5, "Python"]
B = [5, 3, "HELLO", 7, 12.5, "Python", True, False]
print("1-й список:", A)
print("2-й список:", B)
print("Совпадают:")
i = 0
for a in A:
    i += 1
    j = 0
    for b in B:
        j = j + 1
        if a == b:
            txt = str(i) + "-й элемент из 1-го списка и "
            txt = txt + str(j) + "-й элемент из 2-го списка"
            print(txt)
print("End.")
