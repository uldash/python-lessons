# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 15:11:34 2018

@author: user
"""
class MyClass1:
    def __init__(self,txt):
        self.txt=txt
    def __str__(self):
        return self.txt
    def __int__(self):
        return(len(self.txt))
        
class MyClass:
    def __init__(self, nums):
        self.nums = list()
        for n in nums:
            self.nums.append(n)
    def __str__(self):
        txt = "Значение поля-списка:\n| "
        for n in self.nums:
            txt += str(n)+" | "
        return txt
    def __int__(self):
        return len(self.nums)
    def __float__(self):
        avr = sum(self.nums)/int(self)
        return avr
    def __bool__(self):
        if int(self)%2 == 1:
            return True
        else:
            return False
    def __complex__(self):
        mn = min(self.nums)
        mx = max(self.nums)
        z = complex(mx, mn)
        return z
obj = MyClass({2.8, 4.1, 7.5, 2.5, 3.2})
print(obj)
print("Элементов в списке:", int(obj))
if obj:
    print("Нечетное количество элементов")
print("Среднее значение:", float(obj))
print("Минимум и максимум:", complex(obj))

obj1=MyClass1("MyClass1")
print(obj1)
print(int(obj1))