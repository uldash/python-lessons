# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 21:18:52 2018

@author: user
"""

class MyClass:
    name="name"
    def __init__(self):
        print("__init__")
    def hi(self):
        print("hi")
a=MyClass()
print("__bases__:\t",MyClass.__bases__)
print("__dict__:\t",MyClass.__dict__)
#список атрибутов экземпляра класса
print("__dir__:\t",dir(a))
print("__name__:\t",MyClass.__name__)
print("__qualname__:\t",MyClass.__qualname__)
print("__class__:\t",MyClass.__class__)
print("__mro__:\t",MyClass.__mro__)
print(a.__class__)

class Alpha:
    def hello():
        pass
    class Bravo:
        pass
class Charlie(Alpha):
    pass
class Delta(Charlie):
    pass
obj=Alpha()
print("\nПоле __class__")
print("Экземпляр obj:\t",obj.__class__)        
print("Класс Alpha:\t",Alpha.__class__)
print("Класс Alpha.Bravo:\t",Alpha.Bravo.__class__)
print("Класс Charlie:\t",Charlie.__class__)

print("\nПоля __bases__ и __mro__")
print("Класс Delta, поле __bases__\t",Delta.__bases__)
print("Класс Delta, поле __mro__\t",Delta.__mro__)
print("Класс Alpha, поле __bases__\t",Alpha.__bases__)
print("Класс Alpha, поле __mro__\t",Alpha.__mro__)

print("\nПоле __doc__")
print("Описание класса Alpha:",Alpha.__doc__)
Delta.__doc__="Класс Delta наследует класс Charlie"
print("Описание класса Delta:",Delta.__doc__)

print("\nПоле __module__")
print("Модуль класса Alpha:",Alpha.__module__)

print("\nПоле __dict__")
print("Атрибуты класса Alpha:",Alpha.__dict__)
print("Атрибуты класса Alpha.Bravo:",Alpha.Bravo.__dict__)
print("Атрибуты класса Delta:",Delta.__dict__)

print("\nПоля __name__ ")
print("Класс Alpha, поле __name__:",Alpha.__name__)
print("Класс Alpha, поле __qualname__:",Alpha.__qualname__)
print("Класс Alpha.Bravo, поле __name__:",Alpha.Bravo.__name__)
print("Класс Alpha.Bravo, поле __qualname__:",Alpha.Bravo.__qualname__)
print("Класс Delta, поле __name__:",Delta.__name__)
print("Класс Delta, поле __qualname__:",Delta.__qualname__)