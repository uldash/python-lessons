# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 15:32:44 2018

@author: user
"""


class BadName(Exception):
    pass


def greet(name):
    if name[0].isupper():
        return "Hello, " + name
    else:
        raise BadName(name+' is inappropriate name')


while True:
    try:
        name = input('Please enter your name: ')
        greeting = greet(name)
        print(greeting)
    except BadName:
        print('Please try again')
    else:
        break
