# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 19:40:59 2018

@author: user
"""
# CORRECT


def printab(a, b):
    print(a)
    print(b)


def printab(a, b=10):
    print(a)
    print(b)


def printab(a=10, b=10):
    print(a)
    print(b)
# INCORECT


def printab(a=10, b):
    print(a)
    print(b)
