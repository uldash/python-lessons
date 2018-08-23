# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 11:04:22 2018
Вашей программе будет доступна функция foo, которая может бросать 
исключения.

Вам необходимо написать код, который запускает эту функцию, 
затем ловит исключения ArithmeticError, AssertionError, 
ZeroDivisionError и выводит имя пойманного исключения.

Пример решения, которое вы должны отправить на проверку.

try:
    foo()
except Exception:
    print("Exception")
except BaseException:
    print("BaseException")
Подсказка: 
https://docs.python.org/3/library/exceptions.html#exception-hierarchy

@author: user
"""
def foo():
    1/0


try:
    foo()
#except (ZeroDivisionError,ArithmeticError,AssertionError) as err:
#    print(type(err).__name__)
except  ZeroDivisionError:
   print('ZeroDivisionError')
except ArithmeticError:
    print('ArithmeticError')
except AssertionError:
    print('AssertionError')