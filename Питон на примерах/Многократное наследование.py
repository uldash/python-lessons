# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 20:33:06 2018

@author: user
"""

class Alpha:
    def hi():
        print("Класс Alpha")
class Bravo:
    def hi():
        print("Класс Bravo")
class Charlie:
    def hi():
        print("Класс Charlie")
class Delta(Alpha):
    pass
class Echo(Delta):
    pass
class Foxtrot(Bravo,Alpha):
    pass
class Golf(Foxtrot):
    pass
class Hotel(Echo,Charlie,Golf):
    pass
Echo.hi()
Golf.hi()
print(Hotel.__mro__)
Hotel.hi()