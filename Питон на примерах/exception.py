# -*- coding: utf-8 -*-
"""
Created on Thu May 31 20:01:15 2018

@author: user
"""

i=0
while i < 10:
    i+=1
    if i==5:
        break
else:
    printhh("sssss") #строка не вызовет ошибки, если не выполнится

print("Решаем урвнение ax=b")
try:
    a=float(input("Введите a: "))
    b=float(input("Введите b: "))
    x=b/a
    print("Решение уравнения: х =",x)
except ZeroDivisionError:
    print("Ошибка деления на 0!")
except ValueError:
    print("Нужно вводить числа")
except:
    print("Упс, что то пошло не так!")
else:
    print("Ошибок не было")
finally:
    print("End.")