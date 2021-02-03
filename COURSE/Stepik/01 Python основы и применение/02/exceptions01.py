# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 10:27:48 2018

@author: user
"""

try:
    x = [1, 2, 'hello', 7]
    x.sort()
    print(x)
except TypeError:
    print('Type error :(')
print('I can catch')
