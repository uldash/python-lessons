# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 19:31:35 2018

@author: user
"""

def simple_gen():
    print('Chekpoint 1')
    yield 1
    print('Chekpoint 2')
    yield 2
    print('Chekpoint 3')

gen=simple_gen()

x=next(gen)
print(x)
y=next(gen)
print(y)
z=next(gen)