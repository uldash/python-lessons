# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 11:26:21 2018

@author: user
"""
from copy import copy,deepcopy

class MyClass:
    def __init__(self,name,nums):
        self.name=name
        self.nums=nums
    def show(self):
        print("name ->",self.name)
        print("nums ->",self.nums)
x=MyClass("Python",[1,2,3])
print("Экземпляр х:")
x.show()

y=copy(x)
z=deepcopy(x)
print("Экземпляр y:")
y.show()
print("Экземпляр z:")
z.show()
print("Поля экземпляра х изменяются")
x.name="Java"
x.nums[0]=0
print("Экземпляр х")
x.show()
print("Экземпляр y:")
y.show()
print("Экземпляр z:")
z.show()

x.nums=(5,"sss")
print("Экземпляр х")
x.show()
print("Экземпляр y:")
y.show()
print("Экземпляр z:")
z.show()


