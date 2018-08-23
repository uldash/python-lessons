# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 15:07:41 2018

@author: user
"""

x=[1,2,3]
print(id(x))
print(id([1,2,3]))

#Ссылаются ли две переменные на один объект можно проверить оператором is
x=[1,2,3]
y=x
print(y is x)
print(y is [1,2,3])
x[0]=5
print(x)
print(y)

a=1
b=a
print(b is a)
print(b is 1)
a=3
print(a)
print(b)

a=True
b=a
print(b is a)
print(b is True)
a=False
print(a)
print(b)
