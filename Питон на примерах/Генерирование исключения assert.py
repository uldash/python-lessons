# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 14:30:44 2018

@author: user
"""

def show(arg):
    try:
       assert arg
       print("Штатный режим")
    except AssertionError as err:
        print("Исключение:",err.__class__)
    
show(True)
show(False)