# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 17:23:10 2018

@author: user
"""

import random


def show(a):
    n = len(a)
    print(n, "D-вектор: <", sep="", end="")
    for i in range(n - 1):
        print(a[i], end=" | ")
    print(a[n - 1], ">.", sep="")


def random_vector(n):
    r = []
    for i in range(n):
        r.append(random.randint(0, 6))
    return r


def scal_prod(a, b):
    Na = len(a)
    Nb = len(b)
    N = min(Na, Nb)
    s = 0
    for i in range(N):
        s += a[i] * b[i]
    return s


random.seed(2014)
a = random_vector(3)
b = random_vector(5)
show(a)
show(b)
p = scal_prod(a, b)
print("Скалярное произведение:", p)
