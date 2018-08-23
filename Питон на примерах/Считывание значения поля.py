# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 14:40:15 2018

@author: user
"""
class MyClass:
    def __setattr__(self,attr,val):
        print("Выполняется метод __setattr__():")
        txt="*\tПолю "+str(attr)
        txt+=" присваивается значение "+str(val)
        print(txt)
        self.__dict__[attr]=val
        print("Метод __setattr__() выполнен")
    def __getattribute__(self,attr):
        print("Выполняется метод __getattribute__():")
        txt="*\tСчитывается значение поля "+str(attr)
        print(txt)
        try:
            res=object.__getattribute__(self,attr)
        except AttributeError:
            res="У экземпляра поля "+str(attr)+" нет!"
        print("Метод __getattribute__() завершает работу.")
        return res
    def __delattr__(self,attr):
        print("Выполняется метод __delattr__():")
        txt="*\tУдаляется поле "+str(attr)
        print(txt)
        try:
            del self.__dict__[attr]
        except KeyError:
            print("Нельзя удалить поле "+str(attr))
        print("Метод __delattr__() выполнен.")

obj=MyClass()
obj.name="Python"
print("Значение поля name:",obj.name)
del obj.name
print(obj.name)
del obj.name