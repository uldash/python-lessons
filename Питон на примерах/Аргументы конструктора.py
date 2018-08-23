# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 18:26:54 2018

@author: user
"""

class MyClass:
    def set(self,n):
        self.num=n
    def get(self):
        print("Значение поля:",self.num)
    def __init__(self,n=0):
        self.set(n)
        print("Создан экземпляр класса.")
        self.get()

a=MyClass()
b=MyClass(100)
        