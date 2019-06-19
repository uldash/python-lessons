# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 20:26:09 2018

@author: user
"""


def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)


print(fib(6))
