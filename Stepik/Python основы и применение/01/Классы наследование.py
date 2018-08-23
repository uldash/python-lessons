# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 15:04:31 2018

@author: user
"""

class MyList(list):
    def even_length(self):
        return len(self)%2==0

x=MyList()
print(x)
x.extend([1,2,3,4,5])
print(x)
print(x.even_length())
x.append(6)
print(x.even_length())