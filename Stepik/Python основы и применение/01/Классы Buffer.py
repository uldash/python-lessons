# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 12:00:15 2018

@author: user
"""

class Buffer:
    def __init__(self):
        self.lst=list()
    def add(self,*a):
        self.lst.extend(a)
        while len(self.lst)>=5:
            print(sum(self.lst[:5]))
            del self.lst[:5]
    def get_current_part(self):
        return self.lst

buf = Buffer()
buf.add(1, 2, 3)
print(buf.get_current_part()) # вернуть [1, 2, 3]
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
print(buf.get_current_part()) # вернуть [6]
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
print(buf.get_current_part()) # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
print(buf.get_current_part()) # вернуть [1]