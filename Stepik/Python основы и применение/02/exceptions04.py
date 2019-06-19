# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 10:55:10 2018

@author: user
"""


def divide(x, y):
    try:
        result = x/y
    except ZeroDivisionError:
        print('division by zero')
    else:
        print('result is', result)
    finally:
        print('finally')


divide(2, 1)
divide(2, 0)
divide(2, [])
