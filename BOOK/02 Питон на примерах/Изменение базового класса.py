# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 14:40:23 2018

@author: user
"""


class BaseClass:
    name = "Поле name"

    def say(self):
        print("Метод say()")


class NewClass(BaseClass):
    pass


obj = NewClass()
print(obj.name)


def hello(self):
    print("новый метод hello()")


BaseClass.say = hello
BaseClass.name = "Новое значение поля name"
print(NewClass.name)
obj.say()
