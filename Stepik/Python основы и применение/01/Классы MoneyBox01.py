# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 11:37:22 2018

@author: user
"""

class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity

    def can_add(self, v):
        return self.capacity >= v

    def add(self, v):
        self.capacity -= v

test = MoneyBox(5)
print(test.can_add(5))
test.add(5)
test.add(5) 
test.add(5)
print(test.capacity) 