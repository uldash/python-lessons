# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 11:41:55 2018

@author: user
"""

def Fib(n):
    if n==1 or n==2:
        return 1
    else:
        return Fib(n-1)+Fib(n-2)

print("Числа Фибоначчи: ")
n = 15
x1=1
x2=1
print(x1,x2,end=" ")
for i in range(3,n+1):
    x3=x1+x2
    print(x3,end=" ")
    x1=x2
    x2=x3

print()    

for i in range(1,n+1):
    print(Fib(i),end=" ")


        