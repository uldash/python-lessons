# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 13:22:04 2018

@author: user
"""

class MyClass:
    pass

A=MyClass()
B=MyClass()
C=MyClass()

def hello():
    print("Метод экземпляра - 'hello'")
def hi():
    print("Еще один метод - 'hi'")

A.say=hello
C.say=hi

A.say()
try:
    B.say()
except AttributeError:
    print("Такого метода нет")
C.say()
try:
    MyClass.say("jjj")
except AttributeError:
    print("Такй функции нет")

del A.say
try:
    A.say()
except AttributeError:
    print("Такого метода нет")
C.say()

#MyClass.say=hello
#A.say()

str="aaa"
def myupper():
    print("dugahga")
str.upper=myupper
print(str.upper())
