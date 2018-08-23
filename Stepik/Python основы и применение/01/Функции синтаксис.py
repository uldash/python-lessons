# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 17:05:09 2018

@author: user
"""

    
def function_name(arg1,arg2):
    return arg1+arg2
x=function_name(2,8)
y=function_name(x,21)
print(y)
print(type(function_name),id(function_name))

#функции это объекты, интерпретатор прежде чем начать выполнять код 
#создает объект функцию, и если там ошибка синтаксиса останавливает работу
#даже если до вызова функции дело еще не дошло
#вот такая вот проверка перед выполнением.
def function_name(arg1,arg2):
    s=arg1+arg2
    rerturn s
 