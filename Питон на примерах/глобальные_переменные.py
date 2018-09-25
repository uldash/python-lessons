# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 12:19:09 2018

@author: user
"""

x = 100


def test_vars():
    global x, y
    print("В теле функции х=", x)
    y = 200
    print("В теле функции y =", y)
    x = 300


test_vars()
print("Вне функции x =", x)
print("Вне функции y =", y)
