# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 12:24:29 2018

@author: user
"""


def sq_sum():
    def get_n():
        n = int(input("Слагаемых в сумме: "))
        return n

    def find_sq_sum():
        s = 0
        for i in range(1, n + 1):
            s += i**2
        return s

    n = get_n()
    return find_sq_sum


z = sq_sum()()
print("Сумма квадратов равна:", z)
