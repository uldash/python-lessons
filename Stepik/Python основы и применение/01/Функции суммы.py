# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 17:38:36 2018

@author: user
"""


def list_sum(lst):
    result = 0
    for element in lst:
        result += element
    return result


def sum(a, b):
    return a+b


y = sum(14, 28)
z = list_sum([1, 2, 3])
print(y)
print(z)

a = []


def foo(arg1, arg2):
    a.append("foo")


foo(a.append("arg1"), a.append("arg2"))
print(a)
