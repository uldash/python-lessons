# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 14:27:51 2018

@author: user
"""

class BaseClass:
    name_base="Класс BaseClass"
    def say_base(self):
        print("Метод say_base()")
        
class NewClass(BaseClass):
    name_new="Класс NewClass"
    def say_new(self):
        print("Метод say_new()")

obj_base=BaseClass()
obj_new=NewClass()
print("Класс BaseClass и экземпля obj_base:")
print(BaseClass.name_base)
obj_base.say_base()
print("\nКласс NewClass и экземпля obj_new:")
print(NewClass.name_base)
obj_new.say_base()

print(NewClass.name_new)
obj_new.say_new()