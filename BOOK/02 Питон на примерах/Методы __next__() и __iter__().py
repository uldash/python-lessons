# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 15:16:08 2018

@author: user
"""

s = [1, 2, 3].__iter__()
print(s.__next__())
print(s.__next__())
print(s.__next__())
try:
    print(s.__next__())
except Exception as err:
    print(err.__class__)
