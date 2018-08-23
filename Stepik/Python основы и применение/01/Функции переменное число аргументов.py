# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 20:05:32 2018

@author: user
"""

def printab(a,b,*args):
    print('positional argument a',a)
    print('positional argument b',b)
    print('additional arguments:')
    for arg in args:
        print(arg)
printab(1,2,3,4,5,6)

def printab1(a,b,**kwargs):
    print('positional argument a',a)
    print('positional argument b',b)
    print('additional arguments:')
    for key in kwargs:
        print(key,kwargs[key])
printab1(1,c=3,d=4,j=5,m=6,b=2)

def s(a, *vs, b=10):
   res = a + b
   for v in vs:
       res += v
   return res
#print(s(b=31, 0))
print(s(0, 0, 31))
#print(s(b=31))
print(s(11, 10, b=10))
print(s(11, 10, 10))
print(s(21))
print(s(5, 5, 5, 5, 1))
print(s(11, 10))
print(s(11, b=20))