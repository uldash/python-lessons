# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 19:28:47 2018

@author: user
"""


def printab(a, b):
    print(a)
    print(b)


# CORRECT WAYS TO CALL A FUNCTION
printab(10, 20)
printab(b=20, a=10)
# keyword arguments always after non-keyword arguments
printab(10, b=20)

lst = [10, 20]
printab(*lst)  # =printab(lst[0],lst[1])

args = {'a': 10, 'b': 20}
printab(**args)  # =printab(key1=args[key1],key2=args[key2])
