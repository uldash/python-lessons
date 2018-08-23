# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 12:37:20 2018

@author: user
"""

def factor(mode=True):
    def sf(n):
        s=1
        i=n
        while i>1:
            s*=i
            i-=1
        return s
    def df(n):
        s=1
        i=n
        while i>1:
            s*=i
            i-=2
        return s
    if mode:
        return sf
    else:
        return df

print("5! =",factor()(5))
print("5! =",factor(True)(5))
print("5!! =",factor(False)(5))

def factor1(mode=True):
    def f(n,d):
        s=1
        i=n
        while i>1:
            s*=i
            i-=d
        return s
    d=1 if mode else 2
    return lambda n:f(n,d)

print("5! =",factor1()(5))
print("5! =",factor1(True)(5))
print("5!! =",factor1(False)(5))