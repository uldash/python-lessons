# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 18:35:18 2018

@author: user
"""

class MyClass:
    def __init__(self):
        print("Привте всем!")
    def __del__(self):
        print("Пока всем!")
a=MyClass()
del a