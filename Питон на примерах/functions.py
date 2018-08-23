# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 12:45:09 2018

@author: user
"""

def your_name():
    print("Добрый день!")
    name=input("Как вас зовут?")
    return name
def say_hello(txt):
    print("Здравствуйте,",txt+"!")

my_name=your_name()
say_hello(my_name)