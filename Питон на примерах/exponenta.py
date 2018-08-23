# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 12:50:58 2018

@author: user
"""

def my_exp(x,n):
    s=0
    q=1
    for k in range(n+1):
        s+=q
        q*=x/(k+1)
    return s
x=1
for n in range(11):
    print("n =",n,"->",my_exp(x,n))
    