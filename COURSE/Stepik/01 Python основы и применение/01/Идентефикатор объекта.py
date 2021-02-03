# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 15:13:56 2018

@author: user
"""

# изменяется объект а не переменная
x = [1, 2, 3]
y = x
print(y is x)  # True
x.append(4)
print(x)
print(y)

x = [1, 2, 3]
y = x.copy()
print(y is x)  # True
x.append(4)
print(x)
print(y)
