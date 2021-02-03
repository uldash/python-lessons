# -*- coding: utf-8 -*-
"""
Created on Thu May 31 13:45:27 2018

@author: user
"""

res = eval(input("Введите что-нибудь: "))
if type(res) == int:
    print("Вы ввели целое число!", res)
else:
    print("Это точно не целое число!")
print("Работа завершена")
