# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 15:24:59 2018

@author: user
"""


def greet(name):
    if name[0].isupper():
        return "Hello, " + name
    else:
        raise ValueError(name+' is inappropriate name')


print(greet("Anton"))
print(greet("anton"))
