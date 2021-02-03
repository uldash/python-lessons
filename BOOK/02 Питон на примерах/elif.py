# -*- coding: utf-8 -*-
"""
Created on Thu May 31 16:43:41 2018

@author: user
"""

res = eval(input("Введите что-нибудь: "))
resType = type(res)
if resType == int:
    print("Это целое число!")
elif resType == float:
    print("Это действительное число!")
else:
    print("Это текст!")
