# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 19:11:24 2018

@author: user
"""

x = print('111')
print(x)
print(type(x))
print(x is None)


def closest_mod_5(x):
    lst = [i for i in range(x, x + 5 + 1)]
    for i in lst:
        if i % 5 == 0:
            return i


print(closest_mod_5(10))


def closest_mod_5_1(x):
    return x if x % 5 == 0 else closest_mod_5(x + 1)


print(closest_mod_5_1(21))


def closest_mod_5_2(x):
    while x % 5 != 0:
        x += 1
    return x


print(closest_mod_5_2(22))
