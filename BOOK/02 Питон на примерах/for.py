# -*- coding: utf-8 -*-
"""
Created on Thu May 31 17:25:41 2018

@author: user
"""

print("Сумма натуральных чисел!")
n = 100
text = "1+2+...+" + str(n) + " ="
s = 0
for i in range(1, n + 1):
    s += i
print(text, s)

txt = "Python"
i = 1
for s in txt:
    t = str(i) + "-я буква:"
    print(t, s)
    i += 1
print("End.")
