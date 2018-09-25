# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 17:10:57 2018

@author: user
"""


class MyClass:
    def say_hello(self):
        print("Вас приветствует экземпляр класса")


obj = MyClass
print(obj.__class__)
obj = MyClass()
print(obj.__class__)
obj.say_hello()
