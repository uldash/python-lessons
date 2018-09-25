# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 11:08:23 2018

@author: user
"""


def my_pow(n):
    return lambda x: x**n


for n in range(1, 4):
    for x in range(1, 11):
        print(my_pow(n)(x), end="\t")
    print()


def addition(x):
    return lambda y: x - y


add_to_ten = addition(10)
print(addition(10)(6))
print(add_to_ten(6))
print(addition(10)(8))
print(add_to_ten(8))
