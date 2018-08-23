# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 17:30:44 2018

@author: user
"""

class MyClass:
    def set(self,n):
        print("Внимание! Присваивается значение!")
        self.number=n
    def get(self):
        print("Значение поля:",self.number)
        
obj=MyClass()
obj.set(100)
obj.get()

obj.number=200
obj.get()