# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 15:27:43 2018

@author: user
"""

m=[1,5,10,15,20,25]
print(m[1:3])
print(m[3:1])
print(m[1:5:2])
print(m[4])
print(m[4:1:-2])
print(m[-1:-5:-1])
print(m[::-1])
m.append(100)
print(m)
m.extend([1,2])
print(m)
m.insert(2,"insert")
print(m)
m[3:3]=["insert1","insert2"]
print(m)
m[3:5]=["insert3","insert4"]
print(m)
