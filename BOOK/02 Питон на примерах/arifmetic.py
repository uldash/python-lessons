# -*- coding: utf-8 -*-
"""
Created on Thu May 31 09:26:22 2018

@author: user
"""

a = (5 + 2)**2 - 3 * 2
b = 6 - 5 / 2
c = 10 // 4 + 10 % 3
print("Result: \n", a, b, c)

a = "(5+2)**2-3*2"
b = "6-5/2"
c = "10//4+10%3"
print("Result:")
print(a + " =", eval(a))
print(b + " =", eval(b))
print(c + " =", eval(c))
