# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 19:13:27 2018

@author: user
"""
from random import random

class RandomIterator():
    def __iter__(self):
        return self
    def __init__(self,k):
        self.k=k
        self.i=0
    def __next__(self):
        if self.i < self.k:
            self.i+=1
            return random()
        else:
            raise StopIteration

x=RandomIterator(3)
'''print(next(x))
print(next(x))
print(next(x))
iter(x)'''
for i in RandomIterator(5):
    print(i)