# -*- coding: utf-8 -*-
"""
Created on Thu May 31 13:30:19 2018

@author: user
"""

a = float(input("Enter first number:"))
b = float(input("Enter second number:"))
value_1 = "Первое больше второго"
value_2 = "Второе больше первого"
res = value_1 if a > b else value_2
print(res)
