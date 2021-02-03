# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 19:48:47 2018

@author: user
"""


class MyClass:
    def __init__(self, txt):
        self.name = txt

    def __str__(self):
        return self.name

    def __len__(self):
        return len(self.name)

    def __round__(self):
        self.name = "Сброс значения"
        return self

    def __index__(self):
        p = self.name.count(" ") + 1
        return p


txt = "Раз, два, три, четыре, пять. "
txt += "\nВышел зайчик погулять."
obj = MyClass(txt)
print(obj)
print("Количество букв (символов):", len(obj))
# print("Количество слов:",obj.__index__())
print("В двоичном коде:", bin(obj))
print("В восмеричном коде:", oct(obj))
print("В шестнадцатеричном коде:", hex(obj))
print(round(obj))
print(obj)
