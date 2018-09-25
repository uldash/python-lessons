# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 12:35:18 2018

@author: user
"""


class MyClass:
    def say(self):
        print("Все привет!")


obj = MyClass()
obj.say()
MyClass.say(obj)
MyClass.say("Какой то текст")
print(type(MyClass.say))
print(type(obj.say))
