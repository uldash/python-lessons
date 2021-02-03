# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 13:53:06 2018

@author: user
"""


def f1(a):
    a[0] = 'two'
    a[1] += 1


args = ['one', 9]
f1(args)
print(args)


def f2(a, b):
    a = 'two'
    b += 1
    return a, b


a = 'one'
b = 9
c, d = f2(a, b)
print(a, b)
print(c, d)
