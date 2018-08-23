# -*- coding: utf-8 -*-
"""
Created on Thu May 31 16:50:48 2018

@author: user
"""

print("Сумма Натуральных чисел")
n=100
text="1+2+...+" + str(n) + " ="
i=1
s=0
while i <=n:
    s+=i
    i+=1
print(text,s)

i=1
s=0
while True:
    s+=i
    i+=1
    if i>n:
        break
print(text,s)
    