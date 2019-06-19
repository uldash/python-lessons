# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 15:28:51 2018

@author: user
"""


def greet(name):
    if name[0].isupper():
        return "Hello, " + name
    else:
        raise ValueError(name+' is inappropriate name')


while True:
    try:
        name = input('Please enter your name: ')
        greeting = greet(name)
        print(greeting)
    except ValueError:
        print('Please try again')
    else:
        break
