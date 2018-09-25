# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 16:50:35 2018

@author: user
"""


class Fibs:
    def __init__(self, n):
        self.start()
        self.n = n

    def start(self):
        self.count = 1
        self.a = 1
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count > self.n:
            self.start()
            raise StopIteration
        res = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return res


obj = Fibs(10)
for s in obj:
    print(s, end=" ")
print()
obj.a = 3
obj.b = 5
obj.count = 4
for s in obj:
    print(s, end=" ")
print()
obj.n = 15
for s in obj:
    print(s, end=" ")
