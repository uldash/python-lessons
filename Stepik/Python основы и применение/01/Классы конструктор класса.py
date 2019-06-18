# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 10:59:08 2018

@author: user
"""


class Counter:
    def __init__(self, start=0):
        self.count = start

    def __str__(self):
        return str(self.count)


x = Counter(10)
print(x.count)
x.count += 1
print(x)
