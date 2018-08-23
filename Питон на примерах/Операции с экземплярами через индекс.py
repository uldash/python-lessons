# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 20:13:06 2018

@author: user
"""

class MyClass:
    Nmax=5
    def __init__(self):
        n=MyClass.Nmax
        self.nums=[0 for i in range(n)]
    def __str__(self):
        txt="|"
        for s in self.nums:
            txt+=" "+str(s)+" |"
        return txt
    def __setitem__(self,i,v):
        k=i % len(self.nums)
        self.nums[k]=v
    def __getitem__(self,i):
        k=i % len(self.nums)
        return self.nums[k]
    def __delitem__(self,i):
        k=i % len(self.nums)
        self.nums[k]="*"
obj=MyClass()
print(obj)
obj[0]=100
obj[2]=-3
obj[24]=123
print(obj)
print("Элемент с индексом 4:",obj[4])
print("Элемент с индексом 7:",obj[7])
del obj[0]
del obj[9]
print(obj)