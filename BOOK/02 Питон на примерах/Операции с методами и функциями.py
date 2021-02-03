# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 10:56:34 2018

@author: user
"""


class MyClass:
    def __init__(self, n):
        self.name = n

    def say(self):
        print("Класс MyClass:", self.name)


A = MyClass("A")
B = MyClass("B")
A.say()
B.say()
F = A.say
F()
A.say = "Поле экземпляра A"
print(A.say)
try:
    A.say()
except TypeError:
    print("Неверная команда")
B.say()
F()
