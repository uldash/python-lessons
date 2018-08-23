# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 19:03:08 2018

@author: user
"""

def F(A):
    class Alpha(A):
        def hi(self):
            print("Класс Alpha!")
    return Alpha

def Q(A):
    class Bravo(A):
        def hi(self):
            print("Класс Bravo!")
    return Bravo

@F
class First:
    def hello(self):
        print("Класс First!")
@F
class Second:
    def hello(self):
        print("Класс Seccond!")
    
@Q
@F
class Third:
    def hello(self):
        print("Класс Third!")

def show_obj(obj):
    print("Класс экземпляра:",obj.__class__)
    obj.hi()
    obj.hello()

def show_class(A):
    print("Имя класса:",A.__name__)
    print("Базовый класс:",A.__bases__)
    print("Цепочка наследования:",A.__mro__)

one=First()
two=Second()
three=Third()

print("\nЭкземпляры классов.")
for obj in (one,two,three):
    show_obj(obj)
print("\nКлассы:")
for A in [First,Second,Third]:
    show_class(A)
    