# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 15:12:17 2018

@author: user
"""

s=iter([1,2,3])
print(next(s))
print(next(s))
print(next(s))
try:
    print(next(s))
except Exception as err:
    print(err.__class__)