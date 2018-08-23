# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 15:14:09 2018

@author: user
"""

class Adder:
    def __init__(self,number):
        self.number=number
    def __str__(self):
        txt="Значение поля number = "
        txt+=str(self.number)
        return txt
    def __add__(self,x):
        number=self.number+x
        tmp=Adder(number)
        return tmp
    def __radd__(self,x):
        return x+self.number
        #return self+x
a=Adder(10)
b=5+a
print(a)
print(type(b),b)

c=a+15        
print(a)
print(type(c),c)
    