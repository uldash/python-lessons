# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 13:03:04 2018

@author: user
"""

def print_text(txt="Значение аргумента по умолчанию."):
    print(txt)
def  show_args(a,b="Второй аргумент не указан."):
    print(a,b)
def my_func(x="1-й аргумент x.",y="2-Й аргумент y."):
    print(x,y)
def z_func(z):
    z+=1
def get_sum(*nums):
    s=0
    for a in nums:
        s+=a
    return s

print_text("Аргумент указан явно")
print_text()
show_args("Первый аргумент","Второй аргумент")
show_args("Первый аргумент")
my_func()
my_func("один из аргументов")
my_func(y="Один из аргументов.")

z=1
z_func(z)
print(z)

print("Сумма аргументов: ",get_sum(1,2,3,4,5,6))