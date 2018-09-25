# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 11:59:27 2018

@author: user
"""


def test_vars1():
    print("В теле функции x =", x)


def test_vars2():
    x = "локальная переменная"
    print("В теле функции x =", x)


x = 100
test_vars1()
test_vars2()
print("Вне функции x =", x)
