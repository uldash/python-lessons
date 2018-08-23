# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 17:02:24 2018

@author: user
"""
import copy

a=[1,2,3]
b=a
print(a,"\n",b)
a.append(4)
print(b)
print()
c=a[:]
d=a.copy()
a[0]=-10
print(a,"\n",b,"\n",c,"\n",d)
print()
x=[10,20,[100,200],30,[300,400]]
print(x)
y=x[:]
z=x.copy()
print(y)
print(z)
x[2][1]=0
x[4]=0
print(x)
print(y)
print(z)

print()
x=[10,20,[100,200],30,[300,400]]
print(x)
z=copy.deepcopy(x)
print(z)
x[2][1]=0
x[4]=0
print(x)
print(z)

z.reverse()
print(z)