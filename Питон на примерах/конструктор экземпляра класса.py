# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 18:23:02 2018

@author: user
"""

class MyClass:
    def __init__(self):
        self.number=0
        print("Создан экземпляр класса!")
    
obj=MyClass()
print("Значение поля:",obj.number)