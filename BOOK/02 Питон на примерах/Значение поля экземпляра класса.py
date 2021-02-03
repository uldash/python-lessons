# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 17:39:52 2018

@author: user
"""


class MyClass:
    pass


obj = MyClass()
obj.number = 100
print("Значение поля:", obj.number)

# Разные экземпляры одного и тогоже класса могут иметь разный набор полей
txt = "34"
print(txt)
txt.abrakadabra = 200
print(txt.abrakadabra)
