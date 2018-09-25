# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 17:03:36 2018

@author: user
"""


def fibs_gen(n):
    a = 1
    b = 1
    for i in range(n):
        res = a
        a, b = b, a + b
        yield res


print("Попытка N1")
for s in fibs_gen(10):
    print(s, end=" ")
print("\nПопытка N2")
for s in fibs_gen(10):
    print(s, end=" ")
print("\nПопытка N3")
f = fibs_gen(15)
for s in f:
    print(s, end=" ")
print("\nПопытка N4")
for s in f:
    print(s, end=" ")
print("END.")
