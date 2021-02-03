# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 18:52:13 2018

@author: user
"""


class MyClass:
    name = "Класс MyClass"

    def set(self, n):
        self.nickname = n

    def get(self):
        print("Значение поля:", self.nickname)

    def __init__(self, n):
        self.set(n)
        print("Создан экземпляр класса")
        self.get()


green = MyClass("Зеленый")
print("Принадлежность:", green.name)
red = MyClass("Красный")
print("Принадлежность:", red.name)
print("Default MyClass.name", MyClass.name)
MyClass.name = "Здесь могла быть Ваша реклама!"
print("Спрашивает зеленый", green.name)
print("Спрашивает красный", red.name)

green.name = "Здесь был Зеленый"
print(MyClass.name)
print(green.name)
print(red.name)
print()

MyClass.name = "Tada"
print("Спрашивает зеленый", green.name)
print("Спрашивает красный", red.name)
print()

del green.name
print("Спрашивает зеленый", green.name)
print("Спрашивает красный", red.name)
