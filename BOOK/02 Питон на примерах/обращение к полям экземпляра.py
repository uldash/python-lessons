# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 20:33:09 2018

@author: user
"""


class MyClass:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __setattr__(self, attr, val):
        if attr == "name":
            self.__dict__[attr] = val
        else:
            print("Операция не разрешена!")

    def __getattr__(self, attr):
        return "Такого поля нет!"

    def __delattr__(self, attr):
        print("Удалять поля запрещено!")


obj = MyClass("Исходное значение")
print(obj)
obj.name = "Новое значение"
print(obj)
obj.number = 100
print(obj.number)
del obj.name
print(obj)
