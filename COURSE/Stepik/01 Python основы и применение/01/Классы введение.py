# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 10:38:10 2018

@author: user
"""


class MyClass:
    a = 10

    def func(self):
        print('Hello')


x = MyClass()
print(type(x))
print(type(MyClass))


class Counter:
    pass


'''" Выражение "Counter" на отдельной строке служит лишь примером тому, 
что к этому моменту в памяти был создан объект, к которому можно обратиться 
по имени "Counter". Сам объект создается в памяти непосредственно в момент, 
когда интерпретатор считывает объявление класса
'''
Counter  # class object
x = Counter()  # экземпляр класса, вызов конструктора
print(x)
x.count = 0
x.count += 1
print(x.count)
