# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 13:08:44 2018

@author: user
"""


class Box:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def __call__(self):
        volume = self.width * self.height * self.depth
        print("Объем равен:", volume)


obj = Box(10, 20, 30)
obj()


class Box1:
    def __init__(self, width, height, depth):
        print("Объем равен:", self(width, height, depth))

    def __call__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth
        volume = self.width * self.height * self.depth
        return volume


obj1 = Box1(10, 20, 30)
print("Новое значение", obj1(1, 2, 3))
