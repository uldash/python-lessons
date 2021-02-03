# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 14:54:01 2018

@author: user
"""


class BaseClass:
    name = "Поле name базового класса"

    def say(self):
        print("Метод say() базового класса")


class NewClass(BaseClass):
    name = "Поле name производного класса"

    def say(self):
        print("Метод say() производного класса")


obj_base = BaseClass()
obj_new = NewClass()
print(obj_base.name)
obj_base.say()
print(obj_new.name)
obj_new.say()
