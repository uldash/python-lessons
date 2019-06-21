# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 19:10:43 2018

@author: user
"""

lst = [1, 2, 3, 4, 5, 6]

for i in lst:
    print(i)

it = iter(lst)
while True:
    try:
        i = next(it)
        print(i)
    except StopIteration:
        break
