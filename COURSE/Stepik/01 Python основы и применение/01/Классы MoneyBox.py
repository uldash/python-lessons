# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 11:25:12 2018

@author: user
"""


class MoneyBox:
    def __init__(self, capacity):
        self.mb_capacity = capacity
        self.mb_count = 0

    def can_add(self, v):
        if self.mb_count + v <= self.mb_capacity:
            return True
        else:
            return False

    def add(self, v):
        if self.can_add(v):
            self.mb_count += v


m = MoneyBox(20)
m.add(10)
print(m.mb_count)
print(m.can_add(30))
