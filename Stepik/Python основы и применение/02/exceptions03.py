# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 10:50:52 2018

@author: user
"""

try:
    15/0
    # err
except ZeroDivisionError:  # isinstance(err,ZeroD)ivisionError)==True
    print("Division by zero")

print(ZeroDivisionError.mro())
